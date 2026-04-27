# ParecerBot - Smoke Tests

Rodar antes de cada entrega. Iniciar o app com `make run` e testar cada pergunta.

## Perguntas

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

## Verificacoes adicionais

- [ ] Sidebar mostra 8 documentos e contagem de chunks
- [ ] Quick Actions enviam pergunta ao clicar
- [ ] Card de fontes expande com trecho + nome do documento + secao
- [ ] Botao "Exportar conversa" gera arquivo .txt
- [ ] logs/queries.jsonl e atualizado apos cada query
- [ ] Re-indexar funciona sem erros
