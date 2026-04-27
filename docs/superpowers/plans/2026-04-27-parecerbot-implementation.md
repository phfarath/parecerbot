# ParecerBot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Knowledge Agent POC that indexes mocked PX Ativos Judiciais docs, answers questions via RAG with Claude Haiku 4.5, cites sources, and delivers a strategic playbook.

**Architecture:** Modular pipeline — `ingest.py` chunks Markdown docs into ChromaDB, `agent.py` handles RAG retrieval + Claude streaming + memory + logging, `app.py` provides a Streamlit chat interface with source citations and quick actions.

**Tech Stack:** Python 3.11+, Streamlit, Anthropic SDK, ChromaDB, sentence-transformers (all-MiniLM-L6-v2), tiktoken (cl100k_base)

**Spec:** `docs/superpowers/specs/2026-04-27-parecerbot-design.md`

---

## File Structure

```
ParecerBot/
├── README.md                                    # Task 8
├── .gitignore                                   # Task 1
├── .env.example                                 # Task 1
├── requirements.txt                             # Task 1
├── Makefile                                     # Task 1
├── docs/
│   ├── playbook.md                              # Task 7
│   ├── mock_data/
│   │   ├── politica_triagem.md                  # Task 2
│   │   ├── template_due_diligence.md            # Task 2
│   │   ├── manual_analise_viabilidade.md        # Task 2
│   │   ├── jurisprudencia_exemplos.md           # Task 2
│   │   ├── faq_interno.md                       # Task 2
│   │   ├── politica_compliance.md               # Task 2
│   │   ├── fluxo_operacional.md                 # Task 2
│   │   └── tabela_riscos.md                     # Task 2
│   └── superpowers/
│       ├── specs/                               # Already exists
│       └── plans/                               # Already exists
├── src/
│   ├── __init__.py                              # Task 1
│   ├── config.py                                # Task 1
│   ├── ingest.py                                # Task 3
│   ├── agent.py                                 # Task 4
│   └── app.py                                   # Task 5
├── tests/
│   └── smoke_tests.md                           # Task 6
├── logs/
│   └── .gitkeep                                 # Task 1
└── chroma_db/                                   # Generated at runtime
```

---

### Task 1: Project Scaffolding

**Files:**
- Create: `.gitignore`
- Create: `.env.example`
- Create: `requirements.txt`
- Create: `Makefile`
- Create: `src/__init.py`
- Create: `src/config.py`
- Create: `logs/.gitkeep`

- [ ] **Step 1: Create directory structure**

```bash
cd /Volumes/SSD/phfarath/Codes/ParecerBot
mkdir -p src docs/mock_data tests logs chroma_db
touch src/__init__.py logs/.gitkeep
```

- [ ] **Step 2: Write .gitignore**

Create `.gitignore`:

```
__pycache__/
*.pyc
.env
chroma_db/
logs/queries.jsonl
.superpowers/
.venv/
*.egg-info/
dist/
.DS_Store
```

- [ ] **Step 3: Write .env.example**

Create `.env.example`:

```
ANTHROPIC_API_KEY=sk-ant-...
RETRIEVAL_TOP_K=8
RETRIEVAL_DISTANCE_MAX=1.0
CHROMA_PERSIST_DIR=./chroma_db
MOCK_DATA_DIR=./docs/mock_data
LOG_DIR=./logs
```

- [ ] **Step 4: Write requirements.txt**

Create `requirements.txt`:

```
streamlit>=1.37.0
anthropic>=0.40.0
chromadb>=0.5.0
sentence-transformers>=3.0.0
python-dotenv>=1.0.0
tiktoken>=0.7.0
```

- [ ] **Step 5: Write config.py**

Create `src/config.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
RETRIEVAL_TOP_K = int(os.getenv("RETRIEVAL_TOP_K", "8"))
RETRIEVAL_DISTANCE_MAX = float(os.getenv("RETRIEVAL_DISTANCE_MAX", "1.0"))
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")
MOCK_DATA_DIR = os.getenv("MOCK_DATA_DIR", "./docs/mock_data")
LOG_DIR = os.getenv("LOG_DIR", "./logs")
COLLECTION_NAME = "px_knowledge"
CHUNK_MAX_TOKENS = 500
CHUNK_OVERLAP_TOKENS = 50
MEMORY_MAX_TURNS = 10
MODEL_NAME = "claude-haiku-4-5-20250415"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
```

- [ ] **Step 6: Write Makefile**

Create `Makefile`:

```makefile
.PHONY: setup ingest run clean

setup:
	python -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt
	cp -n .env.example .env || true
	@echo "Configure ANTHROPIC_API_KEY no arquivo .env"

ingest:
	. .venv/bin/activate && python -m src.ingest

run:
	. .venv/bin/activate && streamlit run src/app.py --server.port 8501

clean:
	rm -rf chroma_db/
	rm -f logs/queries.jsonl
	@echo "Indice e logs removidos"
```

- [ ] **Step 7: Initialize git and commit**

```bash
cd /Volumes/SSD/phfarath/Codes/ParecerBot
git init
git add .
git commit -m "chore: scaffold project structure, config, and tooling"
```

---

### Task 2: Mock Data (8 Documents)

**Files:**
- Create: `docs/mock_data/politica_triagem.md`
- Create: `docs/mock_data/template_due_diligence.md`
- Create: `docs/mock_data/manual_analise_viabilidade.md`
- Create: `docs/mock_data/jurisprudencia_exemplos.md`
- Create: `docs/mock_data/faq_interno.md`
- Create: `docs/mock_data/politica_compliance.md`
- Create: `docs/mock_data/fluxo_operacional.md`
- Create: `docs/mock_data/tabela_riscos.md`

- [ ] **Step 1: Write politica_triagem.md**

Create `docs/mock_data/politica_triagem.md` — ~3 pages of triage criteria per action type (trabalhista, cível, consumidor, previdenciário), value ranges, estimated timelines, complexity scoring. Must include sections:
- `## 1. Visao Geral`
- `## 2. Criterios por Tipo de Acao` with `### Trabalhista`, `### Civel`, `### Consumidor`, `### Previdenciario`
- `## 3. Faixas de Valor e Prazos`
- `## 4. Score de Complexidade` (1-5 scale with criteria)

Content should reference realistic Brazilian legal terminology and PX-specific processes.

- [ ] **Step 2: Write template_due_diligence.md**

Create `docs/mock_data/template_due_diligence.md` — ~3 pages with DD checklists per legal category. Sections:
- `## 1. Objetivo da Due Diligence`
- `## 2. Documentacao Obrigatoria` (universal checklist)
- `## 3. DD por Categoria` with `### Acoes Trabalhistas`, `### Acoes Civeis`, `### Acoes de Consumo`, `### Acoes Previdenciarias`
- `## 4. Red Flags` (list of deal-breakers)
- `## 5. Prazos e Entregaveis`

- [ ] **Step 3: Write manual_analise_viabilidade.md**

Create `docs/mock_data/manual_analise_viabilidade.md` — ~3 pages with scoring methodology. Sections:
- `## 1. Metodologia de Scoring`
- `## 2. Matriz Risco x Retorno` (table with probabilities and multipliers)
- `## 3. Valor Presente Estimado` (discount rates, calculation methodology)
- `## 4. Taxas de Desconto Aplicaveis` (per action type)
- `## 5. Criterios de Aprovacao` (thresholds)
- `## 6. Excecoes e Ressalvas`

- [ ] **Step 4: Write jurisprudencia_exemplos.md**

Create `docs/mock_data/jurisprudencia_exemplos.md` — ~2 pages with 5-6 fictitious cases. Sections:
- `## Casos de Referencia`
- Each case as `### Caso N: [Type] - [Brief description]` with fields: Tipo, Valor Reclamado, Valor Ofertado, Resultado, Tempo de Resolução, Probabilidade Inicial vs Realizada, Lições

- [ ] **Step 5: Write faq_interno.md**

Create `docs/mock_data/faq_interno.md` — ~2 pages. Sections:
- `## Perguntas Frequentes` (10-12 Q&A covering common operational questions)
- `## Glossario` (15-20 legal terms with definitions used internally at PX)

- [ ] **Step 6: Write politica_compliance.md**

Create `docs/mock_data/politica_compliance.md` — ~2 pages. Sections:
- `## 1. LGPD e Protecao de Dados`
- `## 2. Sigilo e Confidencialidade`
- `## 3. Conflito de Interesse`
- `## 4. Auditoria Interna` (quarterly review procedures)
- `## 5. Penalidades`

- [ ] **Step 7: Write fluxo_operacional.md**

Create `docs/mock_data/fluxo_operacional.md` — ~2 pages. Sections:
- `## 1. Visao Geral do Processo`
- `## 2. Etapa 1: Triagem Inicial` (inputs, outputs, responsible, SLA)
- `## 3. Etapa 2: Due Diligence`
- `## 4. Etapa 3: Analise de Viabilidade`
- `## 5. Etapa 4: Aprovacao`
- `## 6. Etapa 5: Monitoramento`
- `## 7. Gargalos Conhecidos`

- [ ] **Step 8: Write tabela_riscos.md**

Create `docs/mock_data/tabela_riscos.md` — ~2 pages. Sections:
- `## 1. Matriz de Riscos por Tipo de Acao` (table: tipo, probabilidade sucesso, prazo medio, volatilidade valor, risco recomendado)
- `## 2. Fatores de Ajuste` (what increases/decreases risk per type)
- `## 3. Limites de Exposicao` (max portfolio allocation per type)
- `## 4. Cenarios de Stress` (pessimistic/base/optimistic)

- [ ] **Step 9: Commit mock data**

```bash
cd /Volumes/SSD/phfarath/Codes/ParecerBot
git add docs/mock_data/
git commit -m "feat: add 8 mock documents for PX Ativos Judiciais knowledge base"
```

---

### Task 3: Ingest Pipeline (ingest.py)

**Files:**
- Create: `src/ingest.py`

**Depends on:** Task 1, Task 2

- [ ] **Step 1: Write ingest.py**

Create `src/ingest.py`:

```python
import glob
import os
import re

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
                    "chunk_index": i,
                })
    for i, chunk in enumerate(final_chunks):
        chunk["chunk_index"] = i
    return final_chunks


def ingest() -> dict:
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL
    )
    client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)
    client.delete_collection(COLLECTION_NAME)
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
```

- [ ] **Step 2: Verify ingest runs**

```bash
cd /Volumes/SSD/phfarath/Codes/ParecerBot
. .venv/bin/activate && python -m src.ingest
```

Expected: Output showing 8 documents, ~50-80 chunks, ChromaDB persisted in `./chroma_db/`. No errors.

- [ ] **Step 3: Commit ingest pipeline**

```bash
cd /Volumes/SSD/phfarath/Codes/ParecerBot
git add src/ingest.py
git commit -m "feat: add document ingestion pipeline with heading-based chunking"
```

---

### Task 4: RAG Agent (agent.py)

**Files:**
- Create: `src/agent.py`

**Depends on:** Task 1, Task 3

- [ ] **Step 1: Write agent.py**

Create `src/agent.py`:

```python
import json
import os
import time
from datetime import datetime

import anthropic
import chromadb
from chromadb.utils import embedding_functions

from src.config import (
    ANTHROPIC_API_KEY,
    CHUNK_MAX_TOKENS,
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
```

- [ ] **Step 2: Verify agent module loads**

```bash
cd /Volumes/SSD/phfarath/Codes/ParecerBot
. .venv/bin/activate && python -c "from src.agent import retrieve, get_collection_stats; print(get_collection_stats())"
```

Expected: `{'chunks': <number>, 'collection': 'px_knowledge'}` — no import errors.

- [ ] **Step 3: Commit agent**

```bash
cd /Volumes/SSD/phfarath/Codes/ParecerBot
git add src/agent.py
git commit -m "feat: add RAG agent with retrieval, streaming, memory, and logging"
```

---

### Task 5: Streamlit Interface (app.py)

**Files:**
- Create: `src/app.py`

**Depends on:** Task 3, Task 4

- [ ] **Step 1: Write app.py**

Create `src/app.py`:

```python
import os
import streamlit as st

from src.agent import get_collection_stats, get_documents_list, query_stream
from src.config import EMBEDDING_MODEL, MODEL_NAME, RETRIEVAL_TOP_K

st.set_page_config(page_title="ParecerBot — PX Ativos", page_icon="⚖️", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "history" not in st.session_state:
    st.session_state.history = []

QUICK_ACTIONS = [
    "Qual o criterio de triagem para acoes trabalhistas?",
    "Compare o fluxo de due diligence entre acoes civis e trabalhistas",
    "Gere um rascunho de parecer para uma acao consumidor de R$ 200mil",
    "Quais os principais red flags na analise de viabilidade?",
    "Resuma a politica de compliance em topicos",
]


def render_sources(sources: list[dict]):
    if not sources:
        return
    with st.expander(f"Fontes ({len(sources)})", expanded=False):
        for src in sources:
            st.markdown(f"**{src['source']}** > {src['section']}")
            st.caption(src["content"])
            st.divider()


def check_environment():
    from src.config import ANTHROPIC_API_KEY

    if not ANTHROPIC_API_KEY:
        st.error("ANTHROPIC_API_KEY nao configurada. Adicione ao arquivo .env")
        st.code("echo 'ANTHROPIC_API_KEY=sk-ant-...' >> .env")
        return False
    stats = get_collection_stats()
    if stats["chunks"] == 0:
        st.warning("Base de conhecimento vazia. Indexe os documentos primeiro.")
        if st.button("Indexar agora", type="primary"):
            with st.spinner("Indexando documentos..."):
                from src.ingest import ingest

                ingest()
            st.success("Documentos indexados!")
            st.rerun()
        return False
    return True


def main():
    st.title("ParecerBot")
    st.caption("Agente interno — PX Ativos Judiciais")

    with st.sidebar:
        st.header("Base de Conhecimento")
        stats = get_collection_stats()
        st.metric("Chunks indexados", stats["chunks"])
        docs = get_documents_list()
        if docs:
            st.subheader("Documentos")
            for doc in docs:
                st.text(f"  {doc}")
        if st.button("Re-indexar documentos"):
            with st.spinner("Re-indexando..."):
                from src.ingest import ingest

                ingest()
            st.success("Re-indexado!")
            st.rerun()
        st.divider()
        st.subheader("Sobre")
        st.caption(f"Modelo: {MODEL_NAME}")
        st.caption(f"Embeddings: {EMBEDDING_MODEL}")
        st.caption(f"Top-K: {RETRIEVAL_TOP_K}")
        st.divider()
        if st.button("Exportar conversa (.txt)"):
            lines = []
            for msg in st.session_state.messages:
                prefix = "Usuario" if msg["role"] == "user" else "ParecerBot"
                lines.append(f"{prefix}:\n{msg['content']}\n")
            text = "\n---\n\n".join(lines)
            st.download_button(
                "Download",
                data=text,
                file_name="parecerbot_conversa.txt",
                mime="text/plain",
            )

    for msg in st.session_state.messages:
        avatar = "👤" if msg["role"] == "user" else "⚖️"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])
            if "sources" in msg and msg["sources"]:
                render_sources(msg["sources"])

    cols = st.columns(len(QUICK_ACTIONS))
    for i, action in enumerate(QUICK_ACTIONS):
        with cols[i]:
            if st.button(action[:25] + "...", key=f"qa_{i}", use_container_width=True):
                st.session_state.pending_query = action

    if prompt := st.chat_input("Faca uma pergunta sobre os processos da PX..."):
        st.session_state.pending_query = prompt

    if "pending_query" in st.session_state and st.session_state.pending_query:
        query = st.session_state.pending_query
        del st.session_state.pending_query
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user", avatar="👤"):
            st.markdown(query)
        with st.chat_message("assistant", avatar="⚖️"):
            response_placeholder = st.empty()
            full_response = ""
            sources = []
            for event in query_stream(query, st.session_state.history):
                if event["type"] == "token":
                    full_response += event["content"]
                    response_placeholder.markdown(full_response + "▌")
                elif event["type"] == "done":
                    response_placeholder.markdown(full_response)
                    sources = event.get("sources", [])
                    render_sources(sources)
        st.session_state.messages.append({
            "role": "assistant",
            "content": full_response,
            "sources": sources,
        })
        st.session_state.history.append({"role": "user", "content": query})
        st.session_state.history.append({"role": "assistant", "content": full_response})
        st.rerun()


if __name__ == "__main__":
    env_ok = check_environment()
    if env_ok or get_collection_stats()["chunks"] > 0:
        main()
    else:
        st.info("Configure o ambiente e indexe os documentos para comecar.")
```

- [ ] **Step 2: Verify Streamlit loads**

```bash
cd /Volumes/SSD/phfarath/Codes/ParecerBot
. .venv/bin/activate && streamlit run src/app.py --server.headless true --server.port 8501 &
sleep 3 && curl -s -o /dev/null -w "%{http_code}" http://localhost:8501
```

Expected: HTTP 200. Page loads without errors. Sidebar shows chunk count. Chat input visible.

- [ ] **Step 3: Kill test server**

```bash
pkill -f "streamlit run src/app.py" 2>/dev/null || true
```

- [ ] **Step 4: Commit app**

```bash
cd /Volumes/SSD/phfarath/Codes/ParecerBot
git add src/app.py
git commit -m "feat: add Streamlit chat interface with sources, quick actions, and export"
```

---

### Task 6: Smoke Tests

**Files:**
- Create: `tests/smoke_tests.md`

**Depends on:** Task 5

- [ ] **Step 1: Write smoke_tests.md**

Create `tests/smoke_tests.md`:

```markdown
# ParecerBot — Smoke Tests

Rodar antes de cada entrega. Iniciar o app com `make run` e testar cada pergunta.

| # | Pergunta | Esperado | Status |
|---|----------|----------|--------|
| 1 | Qual o criterio de triagem para acoes trabalhistas? | Criterios especificos de politica_triagem.md, com faixas de valor e score de complexidade | [ ] |
| 2 | Compare o fluxo de due diligence entre acoes civis e trabalhistas | Dados de template_due_diligence.md cobrindo ambas categorias, com diferencas explicitas | [ ] |
| 3 | Gere um rascunho de parecer para uma acao consumidor de R$ 200mil | Rascunho estruturado com fonte citada + ressalva sobre valores ilustrativos | [ ] |
| 4 | Quais os principais red flags na analise de viabilidade? | Lista com fontes de template_due_diligence.md secao Red Flags | [ ] |
| 5 | Resuma a politica de compliance em topicos | Topicos de politica_compliance.md (LGPD, sigilo, conflito, auditoria) | [ ] |
| 6 | Qual a taxa de desconto aplicavel? | Valor + secao de manual_analise_viabilidade.md | [ ] |
| 7 | O que e score de complexidade? | Definicao + escala + fonte de politica_triagem.md | [ ] |
| 8 | Qual a previsao do tempo em SP? | Resposta explicita: informacao nao disponivel nos documentos indexados | [ ] |
| 9 | (Apos pergunta 1) E como fica isso para acoes previdenciarias? | Contexto mantido: responde sobre triagem previdenciaria usando conversa anterior | [ ] |
| 10 | Quais acoes tem maior probabilidade de exito? | Dados de tabela_riscos.md com probabilidades + jurisprudencia_exemplos.md | [ ] |

**Verificacoes adicionais:**

- [ ] Sidebar mostra 8 documentos e contagem de chunks
- [ ] Quick Actions enviam pergunta ao clicar
- [ ] Card de fontes expande com trecho + nome do documento + secao
- [ ] Botao "Copiar" aparece em cada resposta (se implementado via botao)
- [ ] Botao "Exportar conversa" gera arquivo .txt
- [ ] logs/queries.jsonl e atualizado apos cada query
- [ ] Re-indexar funciona sem erros
```

- [ ] **Step 2: Run smoke tests manually**

```bash
cd /Volumes/SSD/phfarath/Codes/ParecerBot
make run
```

Open http://localhost:8501 and execute all 10 questions + additional checks. Mark results in smoke_tests.md.

- [ ] **Step 3: Commit smoke tests**

```bash
cd /Volumes/SSD/phfarath/Codes/ParecerBot
git add tests/smoke_tests.md
git commit -m "docs: add manual smoke test script with 10 queries"
```

---

### Task 7: Strategic Playbook

**Files:**
- Create: `docs/playbook.md`

**Depends on:** Nothing (can run in parallel with Tasks 2-5)

- [ ] **Step 1: Write playbook.md**

Create `docs/playbook.md` — 9 sections, analytical-consultive tone, 5-7 min read. Structure:

1. **Executivo** — 1 paragraph: what ParecerBot is, what it solves, current status (POC with mock data, ready for validation)
2. **Por que Agora** — Market thesis: inference costs dropped 10x (2024-2025), models with 200k+ context enable reliable document analysis, competitors in judicial claims sector already testing AI
3. **Diagnostico** — Current PX state: manual triage processes, dispersed documentation across drives/email, dependence on senior analysts for DD, bottlenecks at viability analysis stage
4. **Mapa de Workflows** — End-to-end flow: Triagem → DD → Analise → Aprovacao → Monitoramento, with pain points marked at each stage
5. **Matriz ROI x Complexidade** — Explicit criteria: ROI = analyst-hours/month × average cost. Complexity = structured data dependency + integrations + error tolerance. 5-6 use cases plotted. Disclaimer: "Valores ilustrativos baseados em benchmarks publicos do setor — a serem validados com dados reais da PX"
6. **Roadmap 90 dias** — Wave 1 (days 1-30): Knowledge Agent POC + internal validation. Wave 2 (days 31-60): Real data expansion + triage automation. Wave 3 (days 61-90): Scoring + integration with existing systems
7. **Metricas de Sucesso** — 4 KPIs: average response time to internal queries (-60%), responses with correctly cited source (>90%), internal NPS of agent, reduction in senior team tickets (-40%)
8. **Stack Recomendada** — Table: Component → POC Choice → Production Evolution (ChromaDB→Pinecone, Streamlit→Next.js, Haiku→Sonnet, etc.)
9. **Governanca e Riscos** — LGPD compliance, hallucination mitigation via source citation, human validation gate, response audit log (queries.jsonl)

- [ ] **Step 2: Commit playbook**

```bash
cd /Volumes/SSD/phfarath/Codes/ParecerBot
git add docs/playbook.md
git commit -m "docs: add strategic playbook with 9 sections for AI adoption at PX"
```

---

### Task 8: README

**Files:**
- Create: `README.md`

**Depends on:** All previous tasks

- [ ] **Step 1: Write README.md**

Create `README.md`:

```markdown
# ParecerBot

Knowledge Agent interno para PX Ativos Judiciais. Indexa documentacao interna e responde perguntas com precisao, citando fontes.

## Setup

```bash
make setup
# Configure sua API key
echo 'ANTHROPIC_API_KEY=sk-ant-...' >> .env
```

## Uso

```bash
# Indexar documentos
make ingest

# Iniciar interface
make run
```

Acesse http://localhost:8501

## Arquitetura

```
mock_data/*.md → ingest.py → ChromaDB → agent.py → Claude Haiku → Streamlit
```

- `src/ingest.py` — Chunking (tiktoken cl100k_base) + embeddings (all-MiniLM-L6-v2) + ChromaDB
- `src/agent.py` — RAG retrieval (top-8) + Claude streaming + memoria + logging JSONL
- `src/app.py` — Chat com fontes expasiveis, quick actions, exportar conversa

## Configuracao (.env)

| Variavel | Padrao | Descricao |
|----------|--------|-----------|
| ANTHROPIC_API_KEY | — | Chave de API (obrigatoria) |
| RETRIEVAL_TOP_K | 8 | Chunks recuperados por query |
| RETRIEVAL_DISTANCE_MAX | 1.0 | Distancia maxima cosine (menor = mais similar) |
| CHROMA_PERSIST_DIR | ./chroma_db | Diretorio de persistencia |
| MOCK_DATA_DIR | ./docs/mock_data | Documentos para indexar |

## Entregaveis

- [x] Repo com README claro
- [ ] Playbook estrategico (`docs/playbook.md`)
- [ ] Demo + walkthrough
```

- [ ] **Step 2: Final commit**

```bash
cd /Volumes/SSD/phfarath/Codes/ParecerBot
git add README.md
git commit -m "docs: add README with setup, architecture, and configuration docs"
```

---

## Self-Review

### Spec coverage

| Spec Section | Covered by Task |
|-------------|-----------------|
| 1. Visao Geral | Task 8 (README) |
| 2. Arquitetura | Tasks 3, 4, 5 |
| 3. Camada de Dados | Tasks 2, 3 |
| 4. Camada do Agente | Task 4 |
| 5. Interface Streamlit | Task 5 |
| 6. Playbook Estrategico | Task 7 |
| 7. Estrutura de Arquivos | Task 1 |
| 8. Dependencias | Task 1 |
| 9. Observabilidade e Testes | Task 4 (logging), Task 6 (smoke tests) |
| 10. Fora de Escopo | Not implemented (by design) |
| 11. Configuracao | Task 1 (config.py + .env.example) |

### Placeholder scan

No TBD, TODO, or placeholder patterns found. All steps contain complete code or explicit content descriptions.

### Type consistency

- `retrieve()` returns `list[dict]` with keys `id, content, metadata, distance` — consumed by `build_context()`, `query_stream()`, and `_log_query()` consistently
- `query_stream()` yields dicts with `type` field — consumed by `app.py` event loop consistently
- `get_collection_stats()` returns `dict` with `chunks, collection` — consumed by `app.py` sidebar consistently
- `get_documents_list()` returns `list[str]` — consumed by `app.py` sidebar consistently
- Config variables all defined in `config.py` and imported consistently across modules
