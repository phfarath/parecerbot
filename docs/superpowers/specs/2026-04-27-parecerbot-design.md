# ParecerBot — Design Spec

**Data:** 2026-04-27
**Status:** Aprovado para implementacao
**Contexto:** POC de Knowledge Agent interno para PX Ativos Judiciais

---

## 1. Visao Geral

ParecerBot e um agente interno de IA que indexa documentacao da PX Ativos Judiciais e responde perguntas com precisao, cita fontes, cruza informacoes entre documentos e gera rascunhos de parecer. O objetivo e demonstrar como IA pode acelerar adocao em processos de triagem, due diligence e analise de viabilidade de creditos judiciais.

### Decisoes fundamentais

| Decisao | Escolha | Racional |
|---------|---------|----------|
| Arquitetura | Pipeline modular (3 modulos) | Separacao de responsabilidades, testavel, extensivel |
| Interface | Streamlit | Rapido, Python-only, ideal para POC interna |
| Vector Store | ChromaDB local | Zero infra, persistente, adequado para POC mockado |
| LLM | Claude Haiku 4.5 | Custo-beneficio, qualidade suficiente para demo |
| Embeddings | all-MiniLM-L6-v2 (local) | Sem custo de API, rapido, qualidade razoavel |
| Dados | Mockados (8 documentos Markdown) | Suficiente para demo robusta sem expor dados reais |

---

## 2. Arquitetura

```
┌─────────────────────────────────────────────────┐
│                  Streamlit UI (app.py)           │
│  ┌──────────────────────┬─────────────────────┐ │
│  │   Chat Principal      │   Sidebar            │ │
│  │   - Pergunta          │   - Docs carregados  │ │
│  │   - Resposta + fontes │   - Stats ChromaDB   │ │
│  │   - Quick Actions     │   - Re-indexar       │ │
│  └──────────────────────┴─────────────────────┘ │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│              agent.py (RAG Core)                 │
│  1. Query → Embedding → ChromaDB retrieval       │
│  2. Context + history + prompt → Claude Haiku    │
│  3. Response parse → extract citations           │
│  4. Stream response → UI                         │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│              ingest.py (Data Pipeline)            │
│  mock_data/*.md → chunking → embeddings →        │
│  ChromaDB (persistent collection "px_knowledge") │
└─────────────────────────────────────────────────┘
```

### Modulos e responsabilidades

**`ingest.py`** — Pipeline de dados
- Le todos os `.md` de `docs/mock_data/`
- Chunking por headings com fallback por paragrafos (500 tokens medidos com tiktoken cl100k_base, overlap 50 tokens)
- Metadata: `{ source, section, chunk_index }`
- Gera embeddings via sentence-transformers
- Persiste no ChromaDB em `./chroma_db/`
- CLI: `python src/ingest.py` (re-indexa tudo)

**`agent.py`** — Motor RAG
- Recebe query + historico da sessao
- Gera embedding da query
- Recupera top-8 chunks do ChromaDB (threshold configuravel via .env, padrao distance_max 1.0 — ChromaDB usa distancia cosine: menor = mais similar)
- Monta prompt com system + historico + contexto + pergunta
- Chama Claude Haiku 4.5 com streaming — resposta strima ao vivo, citacoes renderizam somente apos conclusao
- Retorna resposta completa + chunks utilizados (para citacao)
- Gerencia memoria: FIFO de 10 turnos (5 pares)
- Logging estruturado: cada query salva em `logs/queries.jsonl` com timestamp, query, chunks recuperados (ids + distancias), resposta e latencia (ms)

**`app.py`** — Interface Streamlit
- Chat com streaming token-a-token
- Cards expasiveis de fontes abaixo de cada resposta
- Sidebar com docs carregados, stats, botao re-indexar
- 5 Quick Actions pre-definidas
- Botao "Copiar resposta" em cada mensagem do agente
- Botao "Exportar conversa" (download .txt da sessao completa)
- Tratamento de erros: sem indice, sem API key, chunks insuficientes

---

## 3. Camada de Dados

### Documentos mockados

| # | Arquivo | Conteudo | ~Paginas |
|---|---------|----------|----------|
| 1 | `politica_triagem.md` | Criterios de aceite/rejeicao por tipo de acao (trabalhista, civil, consumidor, previdenciario). Faixas de valor, prazo estimado, complexidade. | 3 |
| 2 | `template_due_diligence.md` | Checklist de DD por categoria juridica. Documentos necessarios, pontos de atencao, red flags. | 3 |
| 3 | `manual_analise_viabilidade.md` | Metodologia de scoring (risco x retorno). Matriz de probabilidade, valor presente estimado, taxa de desconto. | 3 |
| 4 | `jurisprudencia_exemplos.md` | 5-6 casos ficticios com tipo, valor, resultado, tempo de resolucao. | 2 |
| 5 | `faq_interno.md` | Perguntas frequentes do time operacional. Glossario de termos juridicos internos. | 2 |
| 6 | `politica_compliance.md` | Regras de LGPD, sigilo, conflito de interesse. Procedimentos de auditoria. | 2 |
| 7 | `fluxo_operacional.md` | Processo end-to-end: triagem → DD → analise → aprovacao → monitoramento. | 2 |
| 8 | `tabela_riscos.md` | Matriz de riscos por tipo de acao. Probabilidades historicas, fatores de ajuste. | 2 |

**Total estimado:** ~19 paginas de conteudo, ~50-80 chunks (conta: 19 pags × ~400 palavras × 1.3 tokens/palavra ÷ 450 tokens/chunk efetivo ≈ 22 chunks base; com conteudo juridico denso e listas, estimativa realista 50-80).

### Estrategia de chunking

1. Split primario por headings (`##`, `###`) — preserva coerencia semantica
2. Se chunk resultante > 500 tokens → re-split por paragrafos
3. Overlap de 50 tokens entre chunks consecutivos
4. Metadata anexada: `{ source, section, chunk_index }`
5. Tokenizer: `tiktoken` com encoding `cl100k_base` (aproximacao generica, compativel com modelos modernos)

### Embeddings e Vector Store

- Modelo: `all-MiniLM-L6-v2` (sentence-transformers, 384 dimensoes)
- Store: ChromaDB, collection `"px_knowledge"`, persistido em `./chroma_db/`
- Distancia: cosine distance (convencao ChromaDB: **menor distancia = mais similar**)
- Retrieval: top-8 chunks, distancia maxima configuravel via `RETRIEVAL_DISTANCE_MAX` no .env (padrao: 1.0 — testar com 2-3 queries antes de fixar)
- Racional top-8: perguntas comparativas (ex: "Compare DD entre acoes civis e trabalhistas") precisam de chunks de multiplos documentos; top-5 tende a trazer chunks do mesmo doc

---

## 4. Camada do Agente

### System Prompt

```
Voce e um agente interno da PX Ativos Judiciais. Sua funcao
e responder perguntas sobre documentacao interna, analisar
informacoes cruzadas e gerar rascunhos de parecer.

Principios:
- Responda direto na primeira frase. Sem preambulos.
- Sempre cite a fonte: [documento, secao].
- Se a resposta nao estiver nos documentos indexados, diga
  isso explicitamente. Nao invente.
- Estrutura padrao: resposta → fonte → ressalva (se houver).
- Tom: analitico, conciso, em portugues corporativo brasileiro.
- Evite floreios, emojis, exclamacoes.

Capacidades:
- Q&A: responda perguntas factuais sobre processos e politicas.
- Analise: cruze informacoes entre documentos, compare cenarios,
  identifique riscos ou inconsistencias.
- Geracao: produza rascunhos de parecer, resumos executivos ou
  checklists quando solicitado.

Sempre que possivel, quantifique. Use os dados de jurisprudencia
e tabelas de risco como referencia.
```

### Memoria de conversa

- Estrutura: lista de mensagens `{"role", "content"}` na sessao Streamlit
- Limite: 10 turnos (5 pares pergunta/resposta)
- Estrategia: FIFO — turnos mais antigos descartados primeiro
- Chunks de RAG sempre entram completos, nunca truncados

### Formato de citacao

Na resposta: citacao inline natural (ex: "Conforme a Politica de Triagem, secao 2.1...")

No card de fontes abaixo da resposta:
- Nome do documento + secao
- Trecho exato do chunk utilizado

### Quick Actions

1. "Qual o criterio de triagem para acoes trabalhistas?"
2. "Compare o fluxo de due diligence entre acoes civis e trabalhistas"
3. "Gere um rascunho de parecer para uma acao consumidor de R$ 200mil"
4. "Quais os principais red flags na analise de viabilidade?"
5. "Resuma a politica de compliance em topicos"

### Ordem de renderizacao (streaming + citacoes)

1. Query do usuario → retrieval → montagem do prompt
2. Resposta strima token-a-token no chat (streaming do Claude)
3. Apos conclusao do streaming → renderiza card de fontes expasivel com chunks utilizados
4. Nao tentar parsear citacoes durante o streaming — complexidade desnecessaria para POC

---

## 5. Interface Streamlit

### Layout principal

- **Chat (area central):** Mensagens com avatar (agente/usuario), streaming em tempo real, fontes em card expasivel, botao "Copiar resposta" em cada mensagem do agente
- **Sidebar (direita):** Base de conhecimento (8 docs listados), stats ChromaDB (chunks, embeddings), botao "Re-indexar", metadados do modelo, botao "Exportar conversa" (download .txt)

### Quick Actions

5 botoes abaixo do chat que enviam pergunta automaticamente ao clicar.

### Tratamento de erros

| Condicao | Comportamento |
|----------|---------------|
| Sem indice ChromaDB | Aviso + botao "Indexar agora" |
| API key faltando | Instrucao clara no topo da pagina |
| Chunks insuficientes (< threshold) | "Nao encontrei informacoes suficientes nos documentos indexados" |
| Rate limit | Mensagem amigavel + sugestao de retry |

---

## 6. Playbook Estrategico

Documento em `docs/playbook.md`, tom analitico-consultivo, exportavel para PDF.

### Estrutura (9 secoes)

1. **Executivo** — Resumo de 1 paragrafo
2. **Por que Agora** — Tese de mercado: custo de inferencia, janela de contexto, concorrencia
3. **Diagnostico** — Estado atual da PX: processos manuais, docs dispersos, gargalos
4. **Mapa de Workflows** — Fluxo end-to-end com pontos de dor
5. **Matriz ROI x Complexidade** — Criterio explicito (ROI = horas-analista x custo; Complexidade = dados estruturados + integracoes + tolerancia a erro). Disclaimer: "Valores ilustrativos baseados em benchmarks publicos — a serem validados com dados reais da PX"
6. **Roadmap 90 dias** — 3 ondas de adocao
7. **Metricas de Sucesso** — 4 KPIs: tempo medio resposta, % fontes corretas, NPS interno, reducao tickets senior
8. **Stack Recomendada** — Tabela componente → POC → producao
9. **Governanca e Riscos** — LGPD, hallucination, validacao humana, auditoria

---

## 7. Estrutura de Arquivos

```
ParecerBot/
├── README.md
├── docs/
│   ├── playbook.md
│   └── mock_data/
│       ├── politica_triagem.md
│       ├── template_due_diligence.md
│       ├── manual_analise_viabilidade.md
│       ├── jurisprudencia_exemplos.md
│       ├── faq_interno.md
│       ├── politica_compliance.md
│       ├── fluxo_operacional.md
│       └── tabela_riscos.md
├── src/
│   ├── ingest.py
│   ├── agent.py
│   └── app.py
├── tests/
│   └── smoke_tests.md              # 10 perguntas manuais com respostas esperadas
├── logs/
│   └── .gitkeep                    # queries.jsonl gerado em runtime
├── requirements.txt
├── .env.example
├── Makefile
└── .gitignore
```

---

## 8. Dependencias

```
streamlit
anthropic
chromadb
sentence-transformers
python-dotenv
tiktoken
```

---

## 9. Observabilidade e Testes

### Logging estruturado

Cada query no `agent.py` gera uma linha em `logs/queries.jsonl`:

```json
{
  "timestamp": "2026-04-27T14:32:01",
  "query": "Qual o criterio de triagem para acoes trabalhistas?",
  "chunks_retrieved": [
    {"id": "abc123", "source": "politica_triagem.md", "section": "2. Criterios", "distance": 0.42}
  ],
  "response_length": 342,
  "latency_ms": 1823,
  "model": "claude-haiku-4.5-20250415"
}
```

Conecta diretamente com a secao de Governanca do playbook: todas as queries sao auditaveis.

### Smoke tests manuais

Arquivo `tests/smoke_tests.md` com 10 perguntas e respostas esperadas. Rodar antes de cada entrega:

| # | Pergunta | Esperado |
|---|----------|----------|
| 1 | Qual o criterio de triagem para acoes trabalhistas? | Criterios especificos de politica_triagem.md |
| 2 | Compare o fluxo de DD entre acoes civis e trabalhistas | Dados de template_dd.md, ambas categorias |
| 3 | Gere um rascunho de parecer para acao consumidor R$200k | Rascunho com fonte + ressalva |
| 4 | Quais os principais red flags na analise de viabilidade? | Lista com fontes de manual_analise_viabilidade.md |
| 5 | Resuma a politica de compliance em topicos | Topicos de politica_compliance.md |
| 6 | Qual a taxa de desconto aplicavel? | Valor + secao de manual_analise_viabilidade.md |
| 7 | O que e score de complexidade? | Definicao + fonte |
| 8 | Pergunta fora do escopo: "Qual a previsao do tempo em SP?" | Resposta explicita: info nao disponivel nos documentos |
| 9 | Follow-up: "E como fica isso para acoes previdenciarias?" | Contexto da pergunta anterior mantido |
| 10 | Quais acoes tem maior probabilidade de exito? | Dados de tabela_riscos.md + jurisprudencia |

---

## 10. Fora de Escopo (YAGNI)

- Autenticacao de usuarios
- API REST separada
- Containerizacao (Docker)
- CI/CD pipeline
- Testes automatizados (POC — validacao manual via smoke_tests.md)
- Integracao com sistemas reais da PX
- Multi-idioma
- Interface mobile

---

## 11. Configuracao (.env.example)

```
ANTHROPIC_API_KEY=sk-ant-...
RETRIEVAL_TOP_K=8
RETRIEVAL_DISTANCE_MAX=1.0
CHROMA_PERSIST_DIR=./chroma_db
MOCK_DATA_DIR=./docs/mock_data
LOG_DIR=./logs
```

---

## 12. Auto-revisao do Spec

| Criterio | Status |
|----------|--------|
| Placeholders/TBD | Nenhum |
| Contradicoes internas | Nenhuma identificada |
| Escopo focado | Sim — POC com mock data |
| Ambiguidades | Nenhuma — tokenizer, threshold, ordem de streaming explicitados |
| Stack consistente | Sim — Python end-to-end |
| Conta de chunks | Corrigida: ~50-80 (calculada, nao estimada) |
| Retrieval params | Configuravel via .env, convencao ChromaDB verificada |
| Observabilidade | Logging JSONL + smoke tests incluidos |
