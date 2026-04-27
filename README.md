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
mock_data/*.md -> ingest.py -> ChromaDB -> agent.py -> Claude Haiku -> Streamlit
```

- `src/ingest.py` - Chunking (tiktoken cl100k_base) + embeddings (all-MiniLM-L6-v2) + ChromaDB
- `src/agent.py` - RAG retrieval (top-8) + Claude streaming + memoria + logging JSONL
- `src/app.py` - Chat com fontes expasiveis, quick actions, exportar conversa

## Configuracao (.env)

| Variavel | Padrao | Descricao |
|----------|--------|-----------|
| ANTHROPIC_API_KEY | - | Chave de API (obrigatoria) |
| RETRIEVAL_TOP_K | 8 | Chunks recuperados por query |
| RETRIEVAL_DISTANCE_MAX | 1.0 | Distancia maxima cosine (menor = mais similar) |
| CHROMA_PERSIST_DIR | ./chroma_db | Diretorio de persistencia |
| MOCK_DATA_DIR | ./docs/mock_data | Documentos para indexar |

## Entregaveis

- [x] Repo com README claro
- [ ] Playbook estrategico (`docs/playbook.md`)
- [ ] Demo + walkthrough
