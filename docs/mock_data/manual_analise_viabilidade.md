# Manual de Analise de Viabilidade — PX Ativos Judiciais

**Versao:** 2.1 | **Vigencia:** 01/02/2025 | **Classificacao:** Interno — Uso Restrito

---

## 1. Metodologia de Scoring

A Analise de Viabilidade constitui a terceira e decisiva etapa do pipeline de aquisicao de creditos judiciais da PX. Recebe os outputs da Due Diligence e aplica um modelo quantitativo de risco-retorno para determinar se o credito deve ser adquirido, sob quais condicoes e qual o valor maximo de aporte.

### 1.1 Score de Viabilidade PX (SVP)

O SVP e composto por quatro fatores ponderados:

| Fator | Peso | Descricao |
|-------|------|-----------|
| Probabilidade Juridica de Sucesso (PJS) | 35% | Chance de recebimento integral ou parcial do credito, com base na analise juridica da DD |
| Multiplo de Retorno Ajustado (MRA) | 25% | Retorno esperado ponderado pelo risco, descontado pelo custo de capital |
| Prazo de Recuperacao (PR) | 20% | Tempo estimado para efetivo recebimento, com penalizacao por prazos longos |
| Qualidade Patrimonial do Devedor (QPD) | 20% | Solidez e liquidez dos bens identificados para garantia da execucao |

**SVP = (PJS x 0,35) + (MRA x 0,25) + (PR x 0,20) + (QPD x 0,20)**

Cada fator e pontuado de 1 a 10. O SVP resultante varia de 1 a 10.

### 1.2 Limiares de Decisao

| SVP | Classificacao | Decisao | Aporte Maximo |
|-----|---------------|---------|---------------|
| 8.0 — 10.0 | Excelente | Aprovacao automatica | 65% do valor nominal |
| 6.5 — 7.9 | Bom | Aprovacao com condicoes padrao | 55% do valor nominal |
| 5.0 — 6.4 | Aceitavel | Aprovacao condicionada — requer Comite | 45% do valor nominal |
| 3.5 — 4.9 | Marginal | Rejeicao recomendada — pode ser submetido ao Comite com justificativa | 35% do valor nominal |
| Abaixo de 3.5 | Inviavel | Rejeicao obrigatoria | N/A |

---

## 2. Matriz Risco x Retorno

### 2.1 Cenarios de Analise

Todo credito deve ser avaliado em tres cenarios:

| Cenario | Premissa | Utilizacao |
|---------|----------|------------|
| Otimista | Recebimento integral no prazo minimo estimado, sem incidentes processuais | Referencia superior — nao usado para decisao isoladamente |
| Base | Recebimento de 75-85% do valor atualizado no prazo medio estimado | Cenario primario para decisao |
| Pessimista | Recebimento de 50-65% do valor atualizado no prazo maximo estimado, com custas adicionais | Teste de estresse — SVP nao pode ser inferior a 5.0 neste cenario |

### 2.2 Tabela de Probabilidades por Tipo de Acao

Valores ilustrativos baseados em benchmarks publicos do setor — a serem validados com dados reais da PX.

| Tipo de Acao | Prob. Sucesso Base | Faixa Pessimista | Faixa Otimista | Volatilidade |
|--------------|-------------------|------------------|----------------|--------------|
| Trabalhista (execucao com garantia) | 80% | 60% | 92% | Baixa |
| Trabalhista (execucao provisorio) | 65% | 40% | 82% | Media |
| Civel (precatorio inscrito) | 75% | 55% | 88% | Baixa |
| Civel (execucao contra particular) | 60% | 35% | 78% | Alta |
| Consumidor (sentenca transitada) | 78% | 58% | 90% | Baixa |
| Consumidor (execucao provisorio) | 55% | 30% | 75% | Alta |
| Previdenciario (RPV) | 85% | 70% | 95% | Muito baixa |
| Previdenciario (precatorio) | 70% | 50% | 85% | Media |

### 2.3 Multiplos de Retorno Esperado

| Tipo de Acao | Multiplo Bruto (base) | Multiplo Liquido (apos custos) | Taxa Interna de Retorno anual |
|--------------|-----------------------|-------------------------------|------------------------------|
| Trabalhista | 1.8x — 2.5x | 1.4x — 1.9x | 18% — 28% |
| Civel | 1.6x — 2.8x | 1.3x — 2.1x | 15% — 25% |
| Consumidor | 1.5x — 2.2x | 1.2x — 1.7x | 14% — 22% |
| Previdenciario | 1.7x — 2.3x | 1.3x — 1.8x | 16% — 24% |

---

## 3. Valor Presente Estimado

### 3.1 Metodologia de Calculo

O Valor Presente Liquido (VPL) e calculado utilizando a seguinte formula:

**VPL = Σ (CFt / (1 + r)^t) - Investimento Inicial**

Onde:
- **CFt** = Fluxo de caixa estimado no periodo t (recebimento parcial ou integral)
- **r** = Taxa de desconto ajustada ao risco (ver Secao 4)
- **t** = Periodo em meses ate o recebimento
- **Investimento Inicial** = Valor aportado pela PX na antecipacao (valor pago ao cedente + custas + honorarios)

### 3.2 Premissas de Calculo

- Atualizacao monetaria: INPC ate 12/2021, IPCA-E a partir de 01/2022
- Juros de mora: conforme tipo de acao (ver tabela por categoria na DD)
- Custos operacionais estimados: 3-5% do valor aportado (honorarios, custas, consultas)
- Taxa de administracao do portfolio: 1.5% a.a. sobre o valor investido
- Provision para perdas: 5-15% conforme score de complexidade (Score 1 = 5%, Score 4 = 15%)

---

## 4. Taxas de Desconto Aplicaveis

### 4.1 Tabela de Taxas por Tipo de Acao e Score de Complexidade

Valores ilustrativos baseados em benchmarks publicos do setor — a serem validados com dados reais da PX.

| Tipo de Acao | Score 1-2 | Score 3 | Score 4 | Base de Calculo |
|--------------|-----------|---------|---------|-----------------|
| Trabalhista | 18% — 20% | 20% — 24% | 24% — 28% | CDI + spread de risco |
| Civel | 15% — 18% | 18% — 20% | 20% — 24% | CDI + spread de risco |
| Consumidor | 12% — 16% | 16% — 18% | 18% — 22% | CDI + spread de risco |
| Previdenciario | 20% — 24% | 24% — 26% | 26% — 30% | CDI + spread de risco + prazo |

### 4.2 Componentes da Taxa de Desconto

A taxa de desconto e composta por:

1. **Taxa livre de risco:** CDI acumulado dos ultimos 12 meses (proxy para custo de capital)
2. **Spread de risco juridico:** 5-15 pontos percentuais conforme complexidade e probabilidade de exito
3. **Spread de prazo:** 2-5 pontos percentuais para prazos superiores a 36 meses
4. **Spread de liquidez:** 2-4 pontos percentuais para creditos de dificil execucao ou devedores sem patrimonio liquido

### 4.3 Revisao de Taxas

As taxas de desconto sao revisadas trimestralmente pelo Comite de Risco Financeiro, com base em:
- Variacao do CDI e Selic
- Taxa de inadimplencia do portfolio nos ultimos 12 meses
- Realizado vs. projetado de creditos liquidados no periodo

---

## 5. Criterios de Aprovacao

### 5.1 Requisitos Obrigatorios

Todo credito deve atender cumulativamente a:

1. **SVP minimo de 5.0** no cenario base
2. **VPL positivo** no cenario base e nao negativo no cenario pessimista
3. **Probabilidade de recebimento** minima de 50% no cenario pessimista
4. **Concentracao de portfolio:** nenhum credito pode representar mais de 10% do portfolio total da PX
5. **Concentracao por tipo:** maximo de 35% do portfolio em um unico tipo de acao
6. **Concentracao por devedor:** maximo de 15% do portfolio vinculado ao mesmo devedor ou grupo economico

### 5.2 Niveis de Aprovacao

| Valor Nominal do Credito | Aprovacao Necessaria |
|--------------------------|---------------------|
| Ate R$ 100.000 | Coordenador de Origination + Analista Financeiro |
| R$ 100.001 — R$ 300.000 | Diretor de Operacoes + Diretor Financeiro |
| R$ 300.001 — R$ 500.000 | Comite de Aprovacao (3 diretores) |
| Acima de R$ 500.000 | Comite de Aprovacao + CEO (aprovacao unanime) |

---

## 6. Excecoes e Ressalvas

### 6.1 Excecoes Permitidas

Excecoes aos criterios acima podem ser concedidas nas seguintes situacoes:

1. **Credito com garantia real constituída** (penhora sobre dinheiro, imovel com matricula limpa): SVP minimo pode ser reduzido para 4.0
2. **Cedente estrategico** (parceria de longo prazo, volume recorrente): Aporte maximo pode ser aumentado em ate 10 p.p., mediante aprovacao do Diretor Comercial
3. **Credito previdenciario RPV** (prazo curto, baixa volatilidade): Score de complexidade pode ser reduzido em 1 ponto
4. **Precatorio com preferencia legal** (idoso, doenca grave): Prazo de recuperacao pode ser desconsiderado no calculo do SVP

### 6.2 Registro de Excecoes

Toda excecao deve ser:

- Formalmente solicitada pelo analista responsavel
- Aprovada pelo nivel hierarquico imediatamente superior ao requerido normalmente
- Registrada no sistema de gestao com a justificativa completa
- Reportada ao Comite de Risco na reuniao mensal seguinte
- Contabilizada no limite de excecoes do trimestre (maximo 10% dos deals aprovados)

### 6.3 Ressalvas Gerais

- Os parametros deste manual sao referenciais e nao substituem o julgamento profissional dos analistas e diretores envolvidos na decisao
- Casos com caracteristicas atipicas nao previstas neste manual devem ser submetidos diretamente ao Comite de Aprovacao
- Divergencias entre analistas sobre pontuacao do SVP sao resolvidas pela media aritmetica das pontuacoes, arredondada para o inteiro mais proximo

---

*Documento aprovado pelo Comite de Risco Financeiro em 25/01/2025. Proxima revisao: 25/07/2025.*
