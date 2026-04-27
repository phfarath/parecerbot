import json
import os
import sys
import time
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import anthropic
import chromadb
from chromadb.utils import embedding_functions

from src.config import (
    ANTHROPIC_API_KEY,
    COLLECTION_NAME,
    CHROMA_PERSIST_DIR,
    EMBEDDING_MODEL,
    LOG_DIR,
    MEMORY_MAX_TURNS,
    MODEL_NAME,
    RETRIEVAL_DISTANCE_MAX,
    RETRIEVAL_TOP_K,
)


SYSTEM_PROMPT = """Voce e um agente interno da PX Ativos Judiciais. Sua funcao
e responder perguntas sobre documentacao interna, analisar
informacoes cruzadas e gerar rascunhos de parecer.

Principios:
- Responda direto na primeira frase. Sem preambulos.
- Sempre cite a fonte: [documento, secao].
- Se a resposta nao estiver nos documentos indexados, diga
  isso explicitamente. Nao invente.
- Estrutura padrao: resposta -> fonte -> ressalva (se houver).
- Tom: analitico, conciso, em portugues corporativo brasileiro.
- Evite floreios, emojis, exclamacoes.

Capacidades:
- Q&A: responda perguntas factuais sobre processos e politicas.
- Analise: cruze informacoes entre documentos, compare cenarios,
  identifique riscos ou inconsistencias.
- Geracao: produza rascunhos de parecer, resumos executivos ou
  checklists quando solicitado.

Sempre que possivel, quantifique. Use os dados de jurisprudencia
e tabelas de risco como referencia."""


def _log_query(query: str, chunks: list[dict], response: str, latency_ms: float):
    os.makedirs(LOG_DIR, exist_ok=True)
    log_path = os.path.join(LOG_DIR, "queries.jsonl")
    entry = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "query": query,
        "chunks_retrieved": [
            {
                "id": c["id"],
                "source": c["metadata"]["source"],
                "section": c["metadata"]["section"],
                "distance": c["distance"],
            }
            for c in chunks
        ],
        "response_length": len(response),
        "latency_ms": round(latency_ms),
        "model": MODEL_NAME,
    }
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def retrieve(query: str) -> list[dict]:
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL
    )
    client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_fn,
        metadata={"hnsw:space": "cosine"},
    )
    if collection.count() == 0:
        return []
    query_embedding = embedding_fn([query])
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=min(RETRIEVAL_TOP_K, collection.count()),
        include=["documents", "metadatas", "distances"],
    )
    chunks = []
    for i in range(len(results["ids"][0])):
        distance = results["distances"][0][i]
        if distance <= RETRIEVAL_DISTANCE_MAX:
            chunks.append({
                "id": results["ids"][0][i],
                "content": results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
                "distance": distance,
            })
    return chunks


def build_context(chunks: list[dict]) -> str:
    if not chunks:
        return "Nenhum documento relevante encontrado na base de conhecimento."
    parts = []
    for i, chunk in enumerate(chunks, 1):
        source = chunk["metadata"]["source"]
        section = chunk["metadata"]["section"]
        content = chunk["content"]
        parts.append(f"[Fonte {i}: {source}, secao '{section}']\n{content}")
    return "\n\n---\n\n".join(parts)


def build_messages(history: list[dict], context: str, query: str) -> list[dict]:
    context_message = {
        "role": "user",
        "content": f"Documentos de referencia:\n\n{context}\n\n"
        f"Pergunta do usuario: {query}",
    }
    context_confirmation = {
        "role": "assistant",
        "content": "Entendido. Vou responder com base nos documentos de referencia fornecidos.",
    }
    recent = history[-MEMORY_MAX_TURNS:] if len(history) > MEMORY_MAX_TURNS else history
    return recent + [context_message, context_confirmation]


def query_stream(query: str, history: list[dict]):
    start_time = time.time()
    chunks = retrieve(query)
    context = build_context(chunks)
    messages = build_messages(history, context, query)
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    full_response = ""
    with client.messages.stream(
        model=MODEL_NAME,
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=messages,
    ) as stream:
        for text in stream.text_stream:
            full_response += text
            yield {"type": "token", "content": text}
    latency_ms = (time.time() - start_time) * 1000
    _log_query(query, chunks, full_response, latency_ms)
    yield {
        "type": "done",
        "response": full_response,
        "sources": [
            {
                "source": c["metadata"]["source"],
                "section": c["metadata"]["section"],
                "content": c["content"][:200],
                "distance": c["distance"],
            }
            for c in chunks
        ],
        "latency_ms": latency_ms,
    }


def get_collection_stats() -> dict:
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL
    )
    client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)
    try:
        collection = client.get_collection(
            name=COLLECTION_NAME, embedding_function=embedding_fn
        )
        return {"chunks": collection.count(), "collection": COLLECTION_NAME}
    except Exception:
        return {"chunks": 0, "collection": COLLECTION_NAME}


def get_documents_list() -> list[str]:
    client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)
    try:
        collection = client.get_collection(name=COLLECTION_NAME)
        all_meta = collection.get(include=["metadatas"])
        sources = sorted(set(m["source"] for m in all_meta["metadatas"]))
        return sources
    except Exception:
        return []
