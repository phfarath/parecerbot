import glob
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import chromadb
import tiktoken
from chromadb.utils import embedding_functions

from src.config import (
    CHUNK_MAX_TOKENS,
    CHUNK_OVERLAP_TOKENS,
    COLLECTION_NAME,
    CHROMA_PERSIST_DIR,
    EMBEDDING_MODEL,
    MOCK_DATA_DIR,
)


def count_tokens(text: str, encoding_name: str = "cl100k_base") -> int:
    enc = tiktoken.get_encoding(encoding_name)
    return len(enc.encode(text))


def split_by_headings(markdown: str) -> list[dict]:
    pattern = r'^(#{1,3}\s+.+)$'
    parts = re.split(pattern, markdown, flags=re.MULTILINE)
    chunks = []
    current_section = "Inicio"
    buffer = ""
    for part in parts:
        if re.match(r'^#{1,3}\s+', part):
            if buffer.strip():
                chunks.append({"section": current_section, "content": buffer.strip()})
            current_section = part.strip().lstrip('#').strip()
            buffer = part + "\n"
        else:
            buffer += part
    if buffer.strip():
        chunks.append({"section": current_section, "content": buffer.strip()})
    return chunks


def split_by_paragraphs(text: str, max_tokens: int, overlap_tokens: int) -> list[str]:
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    chunks = []
    current = ""
    for para in paragraphs:
        candidate = current + "\n\n" + para if current else para
        if count_tokens(candidate) > max_tokens and current:
            chunks.append(current.strip())
            if overlap_tokens > 0:
                enc = tiktoken.get_encoding("cl100k_base")
                tokens = enc.encode(current)
                overlap_text = enc.decode(tokens[-overlap_tokens:])
                current = overlap_text + "\n\n" + para
            else:
                current = para
        else:
            current = candidate
    if current.strip():
        chunks.append(current.strip())
    return chunks


def chunk_document(filepath: str) -> list[dict]:
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    heading_chunks = split_by_headings(content)
    final_chunks = []
    for hc in heading_chunks:
        token_count = count_tokens(hc["content"])
        if token_count <= CHUNK_MAX_TOKENS:
            final_chunks.append({
                "source": filename,
                "section": hc["section"],
                "content": hc["content"],
            })
        else:
            sub_chunks = split_by_paragraphs(
                hc["content"], CHUNK_MAX_TOKENS, CHUNK_OVERLAP_TOKENS
            )
            for i, sc in enumerate(sub_chunks):
                final_chunks.append({
                    "source": filename,
                    "section": hc["section"],
                    "content": sc,
                })
    for i, chunk in enumerate(final_chunks):
        chunk["chunk_index"] = i
    return final_chunks


def ingest() -> dict:
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL
    )
    client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_fn,
        metadata={"hnsw:space": "cosine"},
    )
    md_files = sorted(glob.glob(os.path.join(MOCK_DATA_DIR, "*.md")))
    if not md_files:
        print(f"Nenhum documento encontrado em {MOCK_DATA_DIR}")
        return {"documents": 0, "chunks": 0}
    all_chunks = []
    for filepath in md_files:
        chunks = chunk_document(filepath)
        all_chunks.extend(chunks)
        print(f"  {os.path.basename(filepath)}: {len(chunks)} chunks")
    if not all_chunks:
        return {"documents": len(md_files), "chunks": 0}
    ids = [f"chunk_{i}" for i in range(len(all_chunks))]
    documents = [c["content"] for c in all_chunks]
    metadatas = [
        {"source": c["source"], "section": c["section"], "chunk_index": c["chunk_index"]}
        for c in all_chunks
    ]
    batch_size = 100
    for i in range(0, len(documents), batch_size):
        collection.add(
            ids=ids[i : i + batch_size],
            documents=documents[i : i + batch_size],
            metadatas=metadatas[i : i + batch_size],
        )
    print(f"\nTotal: {len(md_files)} documentos, {len(all_chunks)} chunks indexados")
    print(f"Colecao: {COLLECTION_NAME}")
    print(f"Persistido em: {CHROMA_PERSIST_DIR}")
    return {"documents": len(md_files), "chunks": len(all_chunks)}


if __name__ == "__main__":
    result = ingest()
    print(f"\nResultado: {result}")
