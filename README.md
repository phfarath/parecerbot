# ParecerBot

> **Knowledge Agent interno** que indexa documentacao da PX Ativos Judiciais e responde perguntas com precisao, citando fontes e cruzando informacoes entre documentos.

**Status:** POC com dados mockados | **Stack:** Python + Streamlit + ChromaDB + Claude Haiku 4.5

---

## O que e (e o que nao e)

O ParecerBot e uma **prova de conceito** desenhada para demonstrar como um agente RAG bem construido pode acelerar a primeira onda de adocao de IA na PX. E a Onda 1 do roadmap descrito em [`docs/playbook.md`](docs/playbook.md).

**O que e:**
- Um agente funcional que indexa 8 documentos internos e responde perguntas com citacao de fonte.
- Um ponto de partida para discussao sobre adocao de IA — nao um produto pronto para producao.
- Um repositorio de decisoes tecnicas explicitas (por que ChromaDB, por que Haiku, por que Streamlit).

**O que nao e:**
- Substituto para o trabalho do time de analise.
- Solucao completa para adocao de IA — esta e apenas a primeira de tres ondas.
- Sistema rodando com dados reais. Os 8 documentos em `docs/mock_data/` sao ficticios.

> **Aviso:** os documentos em `docs/mock_data/` foram criados exclusivamente para demonstracao desta POC. Nao refletem politicas, dados ou operacoes reais da PX Ativos Judiciais ou de qualquer outra empresa. Valores, casos e identificadores sao ilustrativos.

---

## Setup em 3 comandos

```bash
make setup                                  # cria venv, instala deps, copia .env
echo 'ANTHROPIC_API_KEY=sk-ant-...' >> .env # configure sua chave
make ingest && make run                     # indexa e abre http://localhost:8501
```

Pre-requisitos: Python 3.11+, `make`, conta na Anthropic com chave de API.

---

## O que o agente faz

| Capacidade | Exemplo de query |
|---|---|
| **Q&A com fonte** | *"Qual o valor minimo de aceite na triagem?"* |
| **Analise cruzada** | *"Compare a DD entre acoes civeis e trabalhistas"* |
| **Geracao** | *"Gere um rascunho de parecer para uma acao consumidor de R$ 200mil"* |
| **Deteccao de gap** | *"Qual a previsao do tempo em SP?"* -> responde "informacao nao disponivel" |
| **Auditoria** | Toda query e logada em `logs/queries.jsonl` com timestamp, chunks e latencia |

---

## Arquitetura

```
docs/mock_data/*.md  ->  ingest.py  ->  ChromaDB  ->  agent.py  ->  Claude Haiku 4.5  ->  Streamlit
                       ^ chunking          ^ retrieval     ^ streaming + log
                       tiktoken            top-8 cosine    JSONL auditavel
```

**Tres modulos, responsabilidades claras:**

| Modulo | O que faz |
|---|---|
| `src/ingest.py` | Chunking heading-based (tiktoken `cl100k_base`, 500 tokens, overlap 50) + embeddings `all-MiniLM-L6-v2` + ChromaDB persistente |
| `src/agent.py` | Retrieval top-8 cosine + Claude Haiku 4.5 com streaming + memoria FIFO de 10 turnos + logging estruturado JSONL |
| `src/app.py` | Chat Streamlit com fontes expasiveis, quick actions, exportar conversa |

---

## Configuracao

Arquivo `.env`:

| Variavel | Padrao | Descricao |
|---|---|---|
| `ANTHROPIC_API_KEY` | — | Chave de API (obrigatoria) |
| `RETRIEVAL_TOP_K` | 8 | Chunks recuperados por query |
| `RETRIEVAL_DISTANCE_MAX` | 1.0 | Distancia maxima cosine (menor = mais similar) |
| `CHROMA_PERSIST_DIR` | `./chroma_db` | Persistencia do indice |
| `MOCK_DATA_DIR` | `./docs/mock_data` | Documentos para indexar |

> Convencao do ChromaDB: distancia cosine, **menor = mais similar**. Threshold padrao (1.0) e permissivo de proposito para a POC; em producao, recalibrar com queries reais.

---

## Decisoes tecnicas

| Decisao | Escolha | Por que |
|---|---|---|
| Vector store | ChromaDB local | Zero infra, persistente, suficiente para POC |
| LLM | Claude Haiku 4.5 | Custo-beneficio (US$ 1/5 por 1M tokens) e latencia baixa |
| Embeddings | `all-MiniLM-L6-v2` | Roda local, sem custo de API, qualidade adequada |
| Tokenizer | `tiktoken cl100k_base` | Aproximacao generica, evita ambiguidade de "500 tokens" |
| Top-K | 8 | Queries comparativas precisam de chunks de multiplos docs (top-5 tende a concentrar em um so) |
| Streaming | Resposta strima, citacoes renderizam ao final | Parsear citacao durante streaming complica sem ganho real |
| Memoria | FIFO 10 turnos | Suficiente para sessao curta; sem persistencia cross-session por design |

---

## Limitacoes conhecidas

Honestidade intelectual e parte da entrega:

- **Sem autenticacao.** Qualquer um com acesso ao processo Streamlit acessa todo o conhecimento indexado.
- **Sem isolamento por usuario.** Memoria de conversa e por sessao, mas dados indexados sao globais.
- **Sem fine-tuning.** O agente responde com o conhecimento *do prompt* (RAG), nao com conhecimento internalizado. Isso e uma escolha consciente — fine-tuning nao vale o custo nesta fase.
- **Top-K fixo.** Nao ha reranking nem retrieval adaptativo. Para a Onda 2, recomendo introduzir cross-encoder ou hybrid search (BM25 + dense).
- **Citacoes em texto livre.** O agente e instruido a citar fontes inline, mas a verificacao programatica e heuristica. Em producao, vale extrair citacoes estruturadas via tool use.
- **Sem testes automatizados.** Validacao e manual via `tests/smoke_tests.md` — adequado para POC, inadequado para producao.

---

## Como expandir para producao

A stack foi escolhida para evoluir sem reescrita. Esta tabela e parte do playbook — ver [`docs/playbook.md`](docs/playbook.md) secao 8 para detalhes:

| Componente | POC (hoje) | Producao (Onda 2-3) | Quando migrar |
|---|---|---|---|
| **Dados** | 8 docs mockados em Markdown | Conectores ao sistema de gestao (Pipefy, Drive, ERP) | Onda 1, sem-2 |
| **Vector store** | ChromaDB local | Pinecone (managed) ou pgvector | Onda 2 |
| **LLM** | Claude Haiku 4.5 | Sonnet para analise complexa, Haiku para Q&A | Onda 2 |
| **Embeddings** | `all-MiniLM-L6-v2` | `text-embedding-3-large` ou modelo fine-tuned com vocabulario PX | Onda 2-3 |
| **Interface** | Streamlit | Next.js dedicado ou integracao no sistema de gestao | Onda 3 |
| **Observabilidade** | JSONL local | LangSmith / Helicone / dashboard proprio | Onda 2 |
| **Auth** | Nenhuma | SSO corporativo (Okta, Azure AD) | Onda 2 |
| **Retrieval** | Top-8 cosine simples | Hybrid search + cross-encoder reranking | Onda 2 |
| **Avaliacao** | Smoke tests manuais | Eval set automatizado com ground-truth | Onda 2 |
| **Compliance** | Disclaimer no README | LGPD plena, audit trail imutavel, retencao configuravel | Onda 1 antes de dados reais |

### Proximas decisoes criticas (em ordem)

1. **Validar com dados reais (semana 1-2 da Onda 1).** Substituir os 8 mockados por uma amostra controlada de documentos reais da PX e medir se a qualidade das respostas se mantem.
2. **Definir metricas de sucesso mediveis.** Os KPIs do playbook secao 7 precisam de baseline real antes de virarem metas.
3. **Decidir o modelo de governanca.** Quem aprova queries, quem revisa o agente trimestralmente, quem responde quando o agente erra.
4. **Roadmap de integracao.** Conectar com Pipefy e diferente de conectar com ERP. Priorizar pelo workflow que da mais ROI (ver matriz no playbook secao 5).

---

## Estrutura do repo

```
ParecerBot/
├── README.md                    # este arquivo
├── docs/
│   ├── playbook.md              # documento estrategico (9 secoes)
│   └── mock_data/               # 8 documentos ficticios
├── src/
│   ├── config.py                # configuracao via .env
│   ├── ingest.py                # pipeline de chunking + embeddings
│   ├── agent.py                 # RAG + Claude + logging
│   └── app.py                   # interface Streamlit
├── tests/
│   └── smoke_tests.md           # 10 queries de validacao manual
├── logs/                        # queries.jsonl (gerado em runtime)
├── requirements.txt
├── .env.example
├── Makefile
└── .gitignore
```

---

## Documentos relacionados

- **[`docs/playbook.md`](docs/playbook.md)** — Playbook estrategico de adocao de IA na PX (9 secoes)
- **[`tests/smoke_tests.md`](tests/smoke_tests.md)** — Script de validacao manual com 10 queries
- **[`docs/mock_data/`](docs/mock_data/)** — Os 8 documentos ficticios indexados

---

## Sobre esta entrega

Esta POC foi construida como prova de pensamento estrategico + capacidade de execucao tecnica, no contexto de uma conversa sobre o time da PX. Nao e um produto comercial, nao e uma proposta formal e nao substitui o trabalho de um time interno. E um ponto de partida para discussao.

Feedback tecnico ou estrategico e bem-vindo — abrir issue ou comentar direto.
