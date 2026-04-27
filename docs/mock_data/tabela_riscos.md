# Tabela de Riscos

**Documento:** TR-001
**Versão:** 5.1
**Vigência:** A partir de 01/03/2026
**Aprovação:** Head de Risco
**Revisão:** Trimestral
**Última calibração:** 2026-Q1, com base no histórico 2022-2025

---

## 1. Propósito

Esta tabela consolida os fatores de risco aplicados na precificação de ativos pela PX. Os haircuts indicados são baseados em histórico próprio da carteira e em benchmarks públicos. São aplicados sobre o valor de face na etapa de Análise de Viabilidade (MV-001, seção 3.3).

Os valores são calibrados trimestralmente pelo time de Risco com base em backtesting da carteira própria.

## 2. Como ler esta tabela

Cada fator de risco recebe:
- **Probabilidade**: estimativa histórica de ocorrência
- **Severidade**: impacto típico no fluxo de caixa
- **Haircut sugerido**: redução aplicada sobre o valor de face

Quando múltiplos fatores se aplicam, o haircut total é calculado como:

```
haircut_total = 1 − (1 − h1) × (1 − h2) × ... × (1 − hn)
```

Esta fórmula evita haircuts compostos superiores a 100%.

---

## 3. Riscos por natureza do devedor

### 3.1 União

| Fator | Probabilidade | Severidade | Haircut |
|---|---|---|---|
| Atraso no cronograma orçamentário | Baixa (5%) | Média | 2% |
| EC com modulação de pagamento | Baixa (3%) | Alta | 5% |
| Compensação rejeitada (tributário) | Média (15%) | Alta | 8% |

### 3.2 Estados — em dia com precatórios

São Paulo, Distrito Federal, Mato Grosso, Paraná (status 2026-Q1).

| Fator | Probabilidade | Severidade | Haircut |
|---|---|---|---|
| Atraso pontual no pagamento | Baixa (10%) | Baixa | 3% |
| Mudança de regime após eleição | Baixa (5%) | Média | 4% |

### 3.3 Estados — atraso histórico

Rio de Janeiro, Minas Gerais, Rio Grande do Sul, Goiás (status 2026-Q1, sujeito a revisão).

| Fator | Probabilidade | Severidade | Haircut |
|---|---|---|---|
| Atraso no cronograma | Alta (75%) | Alta | 15% |
| Acordo de deságio com credores | Média (30%) | Alta | 12% adicional se ocorrer |
| Risco político (mudança de gestão) | Média (40% por ciclo) | Média | 4% |

### 3.4 Municípios

Avaliação caso a caso. Capitais de estados em dia: tratar como nota 3 do scoring. Demais municípios: requer parecer específico.

| Fator | Probabilidade | Severidade | Haircut |
|---|---|---|---|
| Inexistência de cronograma público | Variável | Alta | 10% mínimo |
| Histórico de inadimplência > 24 meses | Alta (60%) | Alta | 18% |

### 3.5 Empresas privadas — capital aberto, IBOV

| Fator | Probabilidade | Severidade | Haircut |
|---|---|---|---|
| Embargos com redução parcial | Média (25%) | Baixa | 4% |
| Acordo com deságio voluntário | Baixa (15%) | Média | 5% |
| Pedido de RJ no horizonte de 24 meses | Baixa (3%) | Catastrófica | reclassifica |

### 3.6 Empresas privadas — capital fechado solventes

| Fator | Probabilidade | Severidade | Haircut |
|---|---|---|---|
| Resistência à execução | Alta (60%) | Média | 8% |
| Embargos com efeito suspensivo | Média (35%) | Média | 6% |
| Pedido de RJ no horizonte de 24 meses | Média (12%) | Catastrófica | 10% (provisão) |

### 3.7 Empresas em situação especial

#### 3.7.1 Recuperação judicial

| Fator | Probabilidade | Severidade | Haircut |
|---|---|---|---|
| Aprovação do plano com deságio | Alta (85%) | Alta | 50-70% |
| Conversão em falência | Média (20%) | Catastrófica | 80% |
| Atraso no pagamento conforme plano | Alta (50%) | Média | 8% |

#### 3.7.2 Falência

Crédito quirografário em massa falida com ativos: avaliar caso a caso, recuperação típica entre 5% e 25% do face.

---

## 4. Riscos processuais

| Fator | Probabilidade | Severidade | Haircut |
|---|---|---|---|
| Recurso especial admitido | Baixa (10%) | Alta | 7% |
| Embargos do executado opostos | Média (35%) | Média | 5% |
| Embargos com redução de valor (>10%) | Baixa (12%) | Média | 4% |
| Penhora no rosto dos autos por terceiro | n/a | Bloqueante | rejeitar |
| Alegação de prescrição intercorrente | Baixa (8%) | Alta | 6% |

---

## 5. Riscos por natureza da ação

### 5.1 Trabalhista

| Fator | Probabilidade | Severidade | Haircut |
|---|---|---|---|
| Redirecionamento para sócios (necessário) | Média (25%) | Média | 5% |
| Discussão sobre índices de correção | Média (30%) | Baixa | 3% |
| Acordo na fase de execução | Alta (50%) | Baixa | 4% — costuma reduzir prazo |

### 5.2 Cível

| Fator | Probabilidade | Severidade | Haircut |
|---|---|---|---|
| Denunciação à seguradora | Média (20%) | Baixa | benéfico se solvente |
| Responsabilidade subsidiária | Baixa (15%) | Média | 5% |
| Dano moral com revisão pelo TJ | Média (30%) | Média | 6% |

### 5.3 Consumidor

| Fator | Probabilidade | Severidade | Haircut |
|---|---|---|---|
| Réu adota estratégia de atraso | Alta (60%) | Baixa | 3% (ajuste de prazo) |
| Embargos com base em CDC | Média (25%) | Baixa | 3% |
| Tese revertida por overruling | Baixa (5%) | Catastrófica | 50% |

### 5.4 Previdenciário

| Fator | Probabilidade | Severidade | Haircut |
|---|---|---|---|
| Retenção de IR pelo INSS | Alta (90%) | Média | 8% (se não previsto) |
| Erro no cálculo da contadoria | Baixa (10%) | Baixa | 2% |
| Cessão de benefício em juízo | Baixa (5%) | Alta | rejeitar (vide PT-001) |

### 5.5 Tributário

| Fator | Probabilidade | Severidade | Haircut |
|---|---|---|---|
| Habilitação parcialmente rejeitada | Média (25%) | Alta | 10% |
| Modulação dos efeitos pelo STF | Baixa (8%) | Catastrófica | 30% |
| Demora na restituição administrativa | Alta (70%) | Média | 6% (ajuste de prazo) |

---

## 6. Riscos de cedente

| Fator | Probabilidade | Severidade | Haircut |
|---|---|---|---|
| Cessão anterior não declarada | Baixa (3%) | Bloqueante | rejeitar |
| Cedente em insolvência (fraude contra credores) | Baixa (5%) | Alta | 15% + provisão |
| Espólio sem alvará específico | n/a | Bloqueante | aguardar regularização |
| Conflito de interesse não declarado | n/a | Bloqueante | rejeitar (vide PC-001) |

---

## 7. Casos especiais

### 7.1 Lotes pulverizados

Em lotes com mais de 30 ativos, aplicar haircut adicional de 2-4% para cobrir:
- Variabilidade da execução individual
- Custo operacional de gestão de muitos processos
- Possibilidade de parte dos ativos não se confirmarem na DD por amostragem

### 7.2 Originadores novos

Operações com originadores sem histórico têm haircut adicional de 3% nos primeiros R$ 5 milhões transacionados, removido após validação da qualidade.

### 7.3 Concentração

Quando uma operação leva a exposição superior a 5% da carteira em um único devedor, aplicar haircut adicional de 5% ou recusar (vide MV-001, seção 7).

---

## 8. Calibração e backtesting

A tabela é recalibrada trimestralmente. A calibração de 2026-Q1 ajustou:

- **Estados em atraso (RJ, MG, RS, GO):** haircut elevado de 12% para 15% após observação de atrasos médios maiores que o previsto
- **Tributário:** introdução de haircut de 10% para habilitação parcialmente rejeitada, após o caso TRB-FED-2023-0021 (vide JE-001)
- **Empresas em RJ:** ampliação da faixa de 50-70% (era 40-60%) após análise da carteira 2022-2024

A próxima revisão ocorre em julho/2026.

## 9. Fontes de dados

- Carteira própria da PX (2018-2025): histórico de 412 operações liquidadas
- Anuário CNJ "Justiça em Números"
- Relatórios CNJ de cumprimento de precatórios pelos estados
- Demonstrações financeiras públicas (CVM, B3)
- Decisões do STJ e STF em teses paradigmáticas

## 10. Documentos Relacionados

- MV-001 — Manual de Análise de Viabilidade
- DD-001 — Template de Due Diligence
- JE-001 — Jurisprudência: Exemplos de Casos
- PT-001 — Política de Triagem
