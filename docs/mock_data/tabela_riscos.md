# Tabela de Riscos — PX Ativos Judiciais

**Versao:** 2.3 | **Vigencia:** 01/03/2025 | **Classificacao:** Interno — Uso Restrito

Valores ilustrativos baseados em benchmarks publicos do setor — a serem validados com dados reais da PX.

---

## 1. Matriz de Riscos por Tipo de Acao

### 1.1 Visao Consolidada

| Tipo de Acao | Prob. Sucesso Media | Prazo Medio (meses) | Volatilidade do Valor | Risco Recomendado | Retorno Esperado (liquido) | Acao Recomendada |
|--------------|---------------------|---------------------|----------------------|-------------------|---------------------------|------------------|
| Trabalhista (exec. com garantia) | 82% | 16 | Baixa | Baixo | 1.4x — 1.9x | Prioridade alta |
| Trabalhista (exec. provisorio) | 62% | 28 | Media | Medio | 1.3x — 1.7x | Seletivo |
| Trabalhista (grupo economico) | 48% | 40 | Alta | Alto | 1.0x — 1.5x | Cautela — apenas com garantia |
| Civel (precatorio inscrito) | 78% | 32 | Baixa | Baixo-Medio | 1.5x — 2.0x | Prioridade (com preferencia) |
| Civel (precatorio nao inscrito) | 60% | 48 | Media | Medio | 1.2x — 1.6x | Seletivo |
| Civel (execucao particular) | 55% | 30 | Alta | Alto | 1.1x — 1.5x | Cautela — DD patrimonial rigoroso |
| Consumidor (sentenca transitada) | 80% | 8 | Baixa | Baixo | 1.4x — 1.7x | Prioridade alta |
| Consumidor (exec. provisorio) | 58% | 20 | Media | Medio | 1.2x — 1.5x | Seletivo |
| Previdenciario (RPV) | 88% | 5 | Muito baixa | Muito baixo | 1.3x — 1.6x | Prioridade maxima |
| Previdenciario (precatorio) | 72% | 36 | Media | Medio | 1.3x — 1.8x | Seletivo (verificar preferencia) |

### 1.2 Classificacao de Risco Detalhada

#### Risco Muito Baixo
- **Perfil:** RPVs previdenciarias com beneficio concedido e valor definido
- **Probabilidade de recebimento:** > 85%
- **Prazo tipico:** 3-7 meses
- **Volatilidade:** Minima — pagamento pelo INSS e praticamente garantido dentro do prazo legal
- **Recomendacao:** Aporte ate 65% do valor atualizado. Score SVP esperado: 8-10.

#### Risco Baixo
- **Perfil:** Execucoes trabalhistas com penhora sobre dinheiro; consumeristas com sentenca transitada contra empresa solida
- **Probabilidade de recebimento:** 75-85%
- **Prazo tipico:** 6-18 meses
- **Volatilidade:** Baixa — valor definido e devedor identificavel
- **Recomendacao:** Aporte ate 60% do valor atualizado. Score SVP esperado: 7-8.5.

#### Risco Medio
- **Perfil:** Execucoes provisorias (trabalhistas e consumeristas); precatorios inscritos sem preferencia; execucoes civeis com patrimonio identificavel
- **Probabilidade de recebimento:** 55-75%
- **Prazo tipico:** 20-40 meses
- **Volatilidade:** Moderada — depende de recursos pendentes e tempo de execucao
- **Recomendacao:** Aporte ate 50% do valor atualizado. Score SVP esperado: 5.5-7.0. Requer analise mais rigorosa.

#### Risco Alto
- **Perfil:** Execucoes contra devedores sem patrimonio; grupos economicos em recuperacao; precatorios nao inscritos; acoes com teses controversas
- **Probabilidade de recebimento:** 35-55%
- **Prazo tipico:** 36-60+ meses
- **Volatilidade:** Alta — resultado depende de multiplos fatores incertos
- **Recomendacao:** Aporte ate 35% do valor atualizado. Score SVP esperado: 3.5-5.0. Requer aprovacao do Comite com justificativa.

---

## 2. Fatores de Ajuste

Os fatores abaixo modificam a probabilidade de exito e o score de risco de qualquer tipo de acao:

### 2.1 Fatores que Reduzem Risco (ajustam probabilidade +5-15 p.p.)

| Fator | Impacto | Aplicavel a |
|-------|---------|-------------|
| Garantia real constituida (penhora sobre dinheiro) | +15 p.p. | Todos |
| Cedente com idade >= 60 anos (preferencia em precatorios) | +10 p.p. | Civel, Previdenciario |
| Devedor com rating investment grade | +10 p.p. | Consumidor, Civel |
| Sentenca transitada em julgado (sem recursos pendentes) | +10 p.p. | Todos |
| Acordo de parcelamento com clausula de confissao de divida | +5 p.p. | Todos |

### 2.2 Fatores que Aumentam Risco (ajustam probabilidade -5-20 p.p.)

| Fator | Impacto | Aplicavel a |
|-------|---------|-------------|
| Reu em recuperacao judicial ou falencia | -20 p.p. | Todos |
| Ausencia de bens penhoraveis na pesquisa inicial | -15 p.p. | Todos |
| Recurso especial ou extraordinario pendente | -10 p.p. | Todos |
| Devedor com mais de 50 execucoes em curso | -10 p.p. | Todos |
| Sentenca com fundamentacao contraditoria ou generica | -10 p.p. | Todos |
| Precatorio sem preferencia e posicao > top 50% da fila | -10 p.p. | Civel, Previdenciario |
| Pericia controversa ou nao realizada | -10 p.p. | Consumidor, Previdenciario |
| Discussao sobre grupo economico | -5 p.p. | Trabalhista |
| Conflito de competencia pendente | -5 p.p. | Todos |
| Cedente com historico de anulacao de cessao | -15 p.p. | Todos |

---

## 3. Limites de Exposicao

### 3.1 Limites por Deal

| Faixa de Valor Nominal | % Maximo do Portfolio | Aporte Maximo (% do nominal) | Score Minimo |
|------------------------|-----------------------|------------------------------|-------------|
| Ate R$ 50 mil | 3% | 65% | 5.0 |
| R$ 50 — 150 mil | 5% | 60% | 5.0 |
| R$ 150 — 300 mil | 8% | 55% | 5.5 |
| R$ 300 — 500 mil | 10% | 50% | 6.0 |
| Acima de R$ 500 mil | 10% | 45% | 6.5 |

### 3.2 Limites por Tipo de Acao

| Tipo de Acao | % Maximo do Portfolio | Justificativa |
|--------------|-----------------------|---------------|
| Trabalhista | 35% | Volume alto, risco moderado, boa diversificacao |
| Civel | 30% | Prazos longos em precatorios — concentracao eleva risco |
| Consumidor | 25% | Tickets menores, boa velocidade — limite por concentracao |
| Previdenciario | 25% | Baixo risco individual mas dependencia de orgao publico unico |

### 3.3 Limites por Devedor

| Condicao | % Maximo do Portfolio |
|----------|-----------------------|
| Mesmo devedor (PJ) | 15% |
| Mesmo grupo economico | 20% |
| Mesmo orgao publico (INSS, Fazenda) | 30% |

### 3.4 Limites por Score de Complexidade

| Score | % Maximo do Portfolio |
|-------|-----------------------|
| 1-2 | Sem limite |
| 3 | 40% |
| 4 | 15% |
| 5 | 0% (rejeicao obrigatoria) |

---

## 4. Cenarios de Stress

### 4.1 Parametros por Cenario

| Parametro | Pessimista | Base | Otimista |
|-----------|------------|------|----------|
| Prob. recebimento media do portfolio | 50% | 70% | 85% |
| Prazo medio de resolucao | +40% vs. estimado | Estimado | -20% vs. estimado |
| Taxa de inadimplencia do portfolio | 25% | 12% | 5% |
| Recuperacao em caso de default | 30% | 55% | 75% |
| Custo de capital (CDI) | 14% a.a. | 10% a.a. | 8% a.a. |
| Valor residual do portfolio | 60% do investido | 80% | 95% |

### 4.2 Teste de Stress Obrigatorio

Todo credito com valor nominal acima de R$ 100 mil deve ser submetido ao teste de stress:

1. Aplicar cenario pessimista a todos os parametros do deal
2. Recalcular VPL com taxa de desconto majorada em 5 p.p.
3. Verificar se o portfolio (incluindo o novo deal) nao viola nenhum limite de concentracao no cenario pessimista
4. Se VPL pessimista for negativo: deal so prossegue com aprovacao do Comite + CEO

### 4.3 Stress Teste Trimestral do Portfolio

O Comite de Risco realiza teste de stress trimestral do portfolio completo:

1. Simular cenario pessimista em 100% dos deals em andamento
2. Calcular perda potencial total e comparar com patrimonio de referencia
3. Verificar se limites de concentracao sao violados no cenario pessimista
4. Identificar deals com deterioracao significativa (prob. realizada < prob. inicial - 20 p.p.)
5. Recomendar provision adicional ou saida antecipada para deals deteriorados

---

*Documento aprovado pelo Comite de Risco Financeiro em 15/02/2025. Proxima revisao: 15/08/2025.*
