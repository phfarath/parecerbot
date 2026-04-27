# Fluxo Operacional

**Documento:** FO-001
**Versão:** 3.5
**Vigência:** A partir de 15/02/2026
**Aprovação:** Diretoria de Operações
**Revisão:** Semestral

---

## 1. Propósito

Este documento descreve o fluxo end-to-end das operações da PX Ativos Judiciais, desde a captação de oportunidades até o monitoramento pós-aquisição. Serve como referência única para a sequência de etapas, papéis envolvidos, sistemas utilizados e SLAs.

## 2. Visão geral do fluxo

```
Originação → Triagem → Due Diligence → Análise de Viabilidade
    → Comitê → Formalização → Pagamento → Cumprimento
    → Recebimento → Liquidação
```

Cada etapa é detalhada nas seções abaixo.

## 3. Etapa 1 — Originação

### 3.1 Canais
- Originadores diretos (parceiros recorrentes)
- Intermediários (boutique, despachantes)
- Leilões judiciais
- Indicação direta de cedentes

### 3.2 Atividades
1. Captação da oportunidade
2. Recepção de documentação preliminar (sentença, valor, partes)
3. Cadastro em sistema (Pipefy, módulo "Originação")
4. Encaminhamento para triagem

### 3.3 Responsável
Time de Originação.

### 3.4 SLA
24 horas para cadastro a partir do recebimento da documentação.

## 4. Etapa 2 — Triagem

### 4.1 Atividades
1. Aplicação dos critérios da PT-001
2. Validação de documentação mínima
3. Pré-aceite ou rejeição com motivo formal

### 4.2 Saída
- Pré-aceite: encaminhamento à DD
- Rejeição: comunicação ao originador com motivo

### 4.3 Responsável
Coordenação de Triagem.

### 4.4 SLA
- Pré-aceite/rejeição: 48 horas úteis
- Encaminhamento à DD após pré-aceite: 5 dias úteis

## 5. Etapa 3 — Due Diligence

### 5.1 Atividades
Execução dos cinco blocos da DD-001:
1. Documental (Analista Jr)
2. Processual (Analista Pleno)
3. Cedente (Analista Pleno)
4. Devedor (Analista Sr)
5. Risco específico (Analista Sr + Coord.)

### 5.2 Saída
Relatório de DD com uma das três recomendações:
- Aprovar com preço de referência
- Aprovar com ressalva
- Rejeitar

### 5.3 Responsável
Time Jurídico.

### 5.4 SLA
Conforme tabela do DD-001:
- Até R$ 200k: 3 dias úteis
- R$ 200k–1M: 5 dias úteis
- R$ 1M–5M: 8 dias úteis
- Acima de R$ 5M: 12 dias úteis

## 6. Etapa 4 — Análise de Viabilidade

### 6.1 Atividades
Aplicação da metodologia do MV-001:
1. Estimativa de fluxo de caixa
2. Cálculo do valor presente
3. Scoring de risco (A/B/C/D)
4. Definição de preço-alvo e faixa de aceite

### 6.2 Saída
Parecer de viabilidade ao Comitê.

### 6.3 Responsável
Time de Análise (Risco e Investimentos).

### 6.4 SLA
2 dias úteis após conclusão da DD.

## 7. Etapa 5 — Comitê de Investimentos

### 7.1 Atividades
1. Apresentação do parecer pelo time de Análise
2. Discussão de riscos
3. Decisão: aprovar, aprovar com ressalva, rejeitar, solicitar diligência adicional

### 7.2 Composição
- CIO (presidente)
- Diretor Jurídico
- Compliance Officer
- Head de Risco

### 7.3 Frequência
Reuniões semanais regulares e extraordinárias para urgências.

### 7.4 Limites de delegação
| Decisor | Ticket máximo |
|---|---|
| Coordenador Jurídico (com ressalva) | R$ 1.000.000 |
| CIO | R$ 5.000.000 |
| Comitê pleno | Acima de R$ 5.000.000 |

## 8. Etapa 6 — Formalização

### 8.1 Atividades
1. Negociação final com cedente
2. Elaboração do termo de cessão
3. Coleta de assinaturas (cedente, cessionária, testemunhas)
4. Notificação ao devedor (quando aplicável)
5. Habilitação no processo (juntada do termo de cessão e substituição processual)

### 8.2 Saída
Termo de cessão registrado e protocolizado.

### 8.3 Responsável
Time Jurídico (formalização).

### 8.4 SLA
5 dias úteis a partir da aprovação do Comitê.

## 9. Etapa 7 — Pagamento ao cedente

### 9.1 Atividades
1. Validação dos dados bancários do cedente
2. Conferência de CNDs (quando aplicável à operação)
3. Liberação do pagamento

### 9.2 Responsável
Financeiro.

### 9.3 SLA
2 dias úteis após formalização completa e validação.

## 10. Etapa 8 — Cumprimento de sentença

### 10.1 Atividades (devedor privado)
1. Petição de habilitação da PX como cessionária
2. Acompanhamento de embargos do executado, se opostos
3. Atos executórios: penhora online (Sisbajud), penhora de bens, registro de protesto
4. Negociações de acordo, se aplicável

### 10.2 Atividades (precatórios)
1. Habilitação do crédito perante o ente devedor
2. Acompanhamento da fila cronológica
3. Atualização monetária periódica

### 10.3 Responsável
Time Jurídico (recuperação) ou escritório terceirizado quando aplicável.

### 10.4 SLA
Variável conforme natureza e devedor (vide MV-001, seção 3.2).

## 11. Etapa 9 — Recebimento

### 11.1 Atividades
1. Levantamento de alvará judicial ou recebimento direto
2. Conferência do valor recebido vs. valor esperado
3. Registro contábil
4. Atualização do status no sistema

### 11.2 Responsável
Financeiro + Jurídico.

## 12. Etapa 10 — Liquidação

### 12.1 Atividades
1. Reconciliação final do ativo
2. Cálculo da TIR efetiva
3. Atualização do backtesting (vide MV-001, seção 9)
4. Encerramento contábil
5. Arquivamento documental conforme PC-001

### 12.2 Responsável
Risco e Financeiro.

## 13. Pontos de medição (KPIs operacionais)

| KPI | Definição | Meta |
|---|---|---|
| Taxa de pré-aceite | % de oportunidades originadas que passam na triagem | 35% |
| Taxa de aprovação | % de pré-aceitos aprovados pelo Comitê | 60% |
| Taxa de aquisição efetiva | % de aprovados que viram aquisição | 80% |
| Tempo médio de ciclo | Originação → Aquisição | ≤ 25 dias úteis |
| TIR média da carteira | Retorno realizado | ≥ 22% a.a. |
| Erro médio de prazo | Diferença entre prazo estimado e realizado | ≤ ±15% |

## 14. Pontos de dor identificados

A revisão semestral de 2025-S2 identificou:

1. **Triagem manual repetitiva:** validação documental absorve 40% do tempo do Analista Jr — candidato a automação prioritária
2. **Heterogeneidade na DD:** documentos similares são analisados de forma inconsistente entre analistas — oportunidade para padronização assistida por IA
3. **Demora na produção do parecer de viabilidade:** modelos de planilha exigem retrabalho — oportunidade para automação parcial do scoring
4. **Conhecimento institucional disperso:** decisões passadas em casos similares nem sempre são consultadas — oportunidade para Knowledge Agent (referência a JE-001)

## 15. Sistemas utilizados

| Sistema | Uso |
|---|---|
| Pipefy | Workflow de operações (originação → liquidação) |
| Drive corporativo | Repositório documental |
| Slack | Comunicação interna |
| Sisbajud | Penhora online em cumprimentos |
| Plataforma processual (PJe / eproc / esaj) | Acompanhamento processual |
| ERP financeiro | Controle de pagamentos e recebimentos |
| Excel + Google Sheets | Modelagem de viabilidade (legado, em revisão) |

## 16. Documentos Relacionados

- PT-001 — Política de Triagem
- DD-001 — Template de Due Diligence
- MV-001 — Manual de Análise de Viabilidade
- TR-001 — Tabela de Riscos
- PC-001 — Política de Compliance
- JE-001 — Jurisprudência: Exemplos de Casos
- FAQ-001 — FAQ Interno
