# Manual de Análise de Viabilidade

**Documento:** MV-001
**Versão:** 4.0
**Vigência:** A partir de 01/03/2026
**Aprovação:** Comitê de Investimentos
**Revisão:** Trimestral

---

## 1. Objetivo

Este manual descreve a metodologia de precificação e scoring aplicada após a Due Diligence (DD-001). A análise de viabilidade transforma o parecer técnico da DD em uma decisão de investimento com preço-alvo, faixa de aceite e classificação de risco.

A decisão final de aquisição cabe ao Comitê de Investimentos, mas todo ativo deve ter parecer de viabilidade emitido conforme este manual.

## 2. Estrutura da análise

A análise de viabilidade é composta por quatro etapas:

1. **Estimativa de fluxo de caixa** — quanto e quando o ativo paga
2. **Cálculo do valor presente** — desconto pela taxa apropriada
3. **Scoring de risco** — classificação em A / B / C / D
4. **Precificação final** — preço-alvo e faixa de aceite

## 3. Etapa 1 — Estimativa de fluxo de caixa

### 3.1 Valor de face

Valor nominal da condenação na data de referência da análise, atualizado pelos índices definidos na sentença ou, na ausência, pelos critérios padrão por natureza:

| Natureza | Correção monetária | Juros |
|---|---|---|
| Trabalhista (após reforma 2017) | TR | 1% a.m. simples |
| Cível | IPCA-E | 1% a.m. simples (Selic a partir de 2021) |
| Consumidor | IPCA-E | 1% a.m. simples |
| Previdenciário federal | IPCA-E | 1% a.m. simples |
| Tributário (repetição) | Selic | Incluída na Selic |

### 3.2 Estimativa de prazo

Prazo até o efetivo recebimento, em meses, considerando:

| Natureza / Devedor | Prazo médio (meses) | Faixa típica |
|---|---|---|
| Trabalhista — devedor solvente | 8 | 4 – 18 |
| Trabalhista — recuperação judicial | 36 | 24 – 72 |
| Cível — réu privado solvente | 10 | 6 – 24 |
| Cível — precatório expedido | 18 | 12 – 36 |
| Consumidor — réu solvente | 6 | 3 – 12 |
| RPV federal | 3 | 2 – 4 |
| Precatório federal | 18 | 12 – 24 |
| Precatório estadual (em dia) | 24 | 18 – 36 |
| Precatório estadual (atraso) | 60 | 36 – 120 |
| Tributário | 12 | 8 – 24 |

Os prazos são revisados trimestralmente com base no histórico de pagamento da carteira.

### 3.3 Haircut por riscos identificados

Sobre o valor de face atualizado, aplicar haircut conforme a Tabela de Riscos (TR-001), que considera:

- Risco de devedor (solvência)
- Risco processual (recursos pendentes, prescrição)
- Risco de execução (penhora frutífera, bens livres)

## 4. Etapa 2 — Valor presente

O valor presente do ativo é calculado descontando o fluxo de caixa estimado pela taxa de desconto da PX:

```
VP = FC_estimado / (1 + i)^t
```

Onde:
- `FC_estimado` = valor de face atualizado × (1 − haircut total)
- `i` = taxa de desconto mensal equivalente à meta de retorno por classe de risco
- `t` = prazo estimado em meses

### 4.1 Taxa de desconto por classe de risco

A taxa de desconto reflete a meta de retorno mínima exigida por classe.

| Classe | Retorno-alvo (TIR a.a.) | Taxa mensal equivalente |
|---|---|---|
| A | 18% | 1,389% |
| B | 24% | 1,808% |
| C | 30% | 2,210% |
| D | 36%+ | 2,596%+ |

Operações classificadas como D são aprovadas apenas com aval expresso do Comitê.

## 5. Etapa 3 — Scoring de risco

O scoring de risco classifica o ativo em A, B, C ou D combinando três dimensões. Cada dimensão recebe nota de 1 (melhor) a 4 (pior). A classe final é a **pior nota** entre as três.

### 5.1 Dimensão 1 — Devedor

| Nota | Critério |
|---|---|
| 1 | União, grandes empresas listadas em IBOV, bancos top 5 |
| 2 | Estados em dia com precatórios, empresas de capital aberto |
| 3 | Empresas de capital fechado solventes, municípios capitais |
| 4 | Empresas em RJ, Estados em atraso, municípios sem histórico |

### 5.2 Dimensão 2 — Risco processual

| Nota | Critério |
|---|---|
| 1 | Trânsito em julgado, sem recursos pendentes, cálculo homologado |
| 2 | Trânsito em julgado, recursos extraordinários ainda admissíveis |
| 3 | Cumprimento iniciado mas com embargos pendentes |
| 4 | Risco de prescrição em até 12 meses ou disputa sobre cessão |

### 5.3 Dimensão 3 — Liquidez

| Nota | Prazo estimado |
|---|---|
| 1 | Até 6 meses |
| 2 | 7 a 18 meses |
| 3 | 19 a 36 meses |
| 4 | Acima de 36 meses |

### 5.4 Exemplo de classificação

Ativo trabalhista contra empresa de capital aberto, sentença transitada, recurso especial não admitido, prazo estimado de 10 meses:

- Devedor: nota 2
- Processual: nota 1
- Liquidez: nota 2
- **Classe final: B**

## 6. Etapa 4 — Precificação

### 6.1 Preço-alvo

Preço-alvo é o valor presente calculado conforme seção 4, ajustado pela margem de operação (5% a 8% sobre o VP).

### 6.2 Faixa de aceite

A faixa de aceite define os limites de negociação:

| Classe | Limite inferior | Limite superior |
|---|---|---|
| A | 92% do VP | 100% do VP |
| B | 88% do VP | 100% do VP |
| C | 80% do VP | 95% do VP |
| D | 70% do VP | 90% do VP |

Aquisições no limite superior exigem expectativa de retorno superior à média da carteira da classe.

## 7. Critérios de rejeição na viabilidade

Mesmo após DD positiva, o ativo pode ser rejeitado na análise de viabilidade se:

1. Valor presente inferior a 50% do valor de face
2. Prazo estimado superior a 60 meses sem prêmio compatível
3. Classe D sem aval do Comitê
4. Concentração: ativo levaria a exposição > 5% da carteira em um único devedor

## 8. Documentação do parecer

O parecer de viabilidade deve conter:

- Identificação do ativo (número do processo, partes, natureza)
- Resumo da DD (referência ao relatório DD)
- Estimativa de fluxo de caixa (valor de face, haircut, valor líquido)
- Cálculo do valor presente (taxa, prazo)
- Scoring de risco (notas das três dimensões + classe final)
- Preço-alvo e faixa de aceite
- Recomendação ao Comitê

## 9. Revisão e backtesting

Trimestralmente, o time de Risco compara prazos e taxas de recuperação reais contra as estimativas usadas nos pareceres. Desvios sistemáticos acima de 15% disparam revisão deste manual.

## 10. Documentos Relacionados

- PT-001 — Política de Triagem
- DD-001 — Template de Due Diligence
- TR-001 — Tabela de Riscos
- JE-001 — Jurisprudência: Exemplos de Casos
- FO-001 — Fluxo Operacional
