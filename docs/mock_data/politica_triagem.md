# Politica de Triagem — PX Ativos Judiciais

**Versao:** 3.2 | **Vigencia:** 01/03/2025 | **Classificacao:** Interno — Uso Restrito

---

## 1. Visao Geral

A triagem constitui o estagio inicial do pipeline de aquisicao de creditos judiciais da PX Ativos Judiciais. Seu objetivo e filtrar, classificar e priorizar oportunidades de antecipacao de creditos judiciais antes que avancem para a etapa de due diligence e analise de viabilidade economica.

O processo de triagem e de responsabilidade do Departamento de Origination, com supervisao do Comite de Risco Juridico. Todo credito judicial apresentado a PX deve obrigatoriamente passar pela triagem padrao, sem excecao, inclusive oriundos de canal de parceiros, referral ou captacao direta.

### 1.1 Princípios Norteadores

- **Eficiencia operacional:** Triagem deve ser concluida em ate 5 (cinco) dias uteis contados do recebimento completo da documentacao inicial.
- **Seletividade informada:** Aceitar apenas creditos com probabilidade juridica minimamente razoavel de adimplemento, evitando desperdicio de recursos em analises de baixo potencial.
- **Padronizacao:** Todo credito e avaliado sob os mesmos criterios objetivos, independentemente do canal de origem ou da relacao com o cedente.
- **Registro:** Cada triagem gera um numero de protocolo interno (formato PX-TRI-AAAA-NNNNN) e e registrado no sistema de gestao de deals com o status correspondente.

### 1.2 Fluxo Simplificado

1. Recebimento da oportunidade via formulario padrao, e-mail institucional ou API de parceiro.
2. Verificacao de completeness documental minima (peticao inicial + sentenca ou decisao interlocutoria relevante).
3. Classificacao por tipo de acao (trabalhista, civel, consumidor, previdenciario).
4. Aplicacao dos criterios especificos por tipo (Secao 2).
5. Enquadramento na faixa de valor e prazo (Secao 3).
6. Atribuicao do Score de Complexidade (Secao 4).
7. Decisao: Aprovado para DD / Retido em triagem / Rejeitado com fundamentacao.

### 1.3 Responsaveis

| Funcao                          | Responsabilidade                                    |
|---------------------------------|-----------------------------------------------------|
| Analista de Triagem             | Classificacao, score, recomendacao inicial          |
| Coordenador de Origination      | Homologacao de triagens com score >= 4              |
| Diretor Juridico                | Decisao sobre casos borderline ou conflito de classe|
| Comite de Risco Juridico        | Revisao mensal dos criterios e faixas              |

---

## 2. Criterios por Tipo de Acao

### Trabalhista

**Aceitacao preferencial:**

- Acoes com sentenca de primeiro grau procedente ou parcialmente procedente, com transito em julgado ou com recurs pendentes de julgamento.
- Reclamatorias trabalhistas com verbas rescisorias deferidas (saldo de salario, aviso previo proporcional, multa de 40% sobre FGTS, horas extras com reflexos).
- Acoes em que o reclamado e empresa com patrimonio liquido comprovadamente superior a 3x o valor da condenacao.
- Creditos derivados de acordos judiciais homologados com parcelamento em curso e garantia real ou penhora ja efetivada.

**Criterios de rejeicao:**

- Reclamada em fase de recuperacao judicial ou falencia sem garantia real constituída.
- Acoes com pedido de danos morais exclusivamente, sem calculo material fundamentado.
- Creditos de substitutos processuais (sindicatos) sem individuacao completa dos substituidos e suas cotas.
- Presenca de discussao sobre vinculo empregaticio com provas contraditoras substanciais.
- Valor nominal do credito inferior a R$ 20.000,00 (vinte mil reais).

**Indicadores de complexidade trabalhista:**

- Numero de reclamadas (cada reclamada adicional aumenta complexidade).
- Existencia de grupo economico discutido (caracterizacao de solidariedade).
- Pedidos de successoria ou responsibility de terceiros.
- Execucao provisoria com bloqueio via SISBAJUD ja frustrado.

### Civel

**Aceitacao preferencial:**

- Acoes de cobranca com titulo executivo judicial constituído (sentenca liquida ou liquidacao por artigos concluida).
- Acoes indenizatorias com responsabilidade civil configurada e quantum ja fixado ou arbitravel com baixa margem de controversia.
- Execucoes contra a Fazenda Publica com precatorio ja inscrito ou em fase de inscricao.
- Acoes de ressarcimento derivadas de seguros com apolice vigente a epoca do sinistro e cobertura reconhecida.

**Criterios de rejeicao:**

- Acoes exclusivamente declaratorias sem pedido condenatorio.
- Demandas envolvendo direito de familia (alimentos, inventario, partilha) ou Successao.
- Acoes com discussao predominantemente tributaria que nao configurem executivo fiscal com credito certo.
- Condenacao dependente de liquidacao por artigos complexa envolvendo mais de 10 (dez) itens.
- Valor nominal inferior a R$ 30.000,00 (trinta mil reais).

**Indicadores de complexidade civel:**

- Existencia de litisconsortes passivos com defensas autonomas.
- Intervention de assistente ou opoente.
- Execucao contra devedor sem patrimio identificavel (consultas ao INFOJUD, SISBAJUD e CADIM negativas).
- Precatorios sem ordem cronologica definida ou com preferencia disputada.

### Consumidor

**Aceitacao preferencial:**

- Acoes de cobranca de valores indevidos com sentenca procedente contra instituicoes financeiras, operadoras de telecomunicacoes ou planos de saude.
- Danos morais e materiais decorrentes de relacao de consumo com nexo causal claro e comprovado.
- Acoes com decisao de first instancia favoravel e apelacao do reu sem efeito suspensivo (execucao provisoria viavel).
- Casos em que o reu possui rating de credito investment grade ou patrimonio liquido divulgado compativel.

**Criterios de rejeicao:**

- Acoes propostas contra microempresas ou empresas individuais sem patrimonio dissociavel.
- Pedidos de danos esteticos ou morais sem pericia medica ou prova documental robusta.
- Casos com multiple reclamados e solidariedade nao reconhecida na sentenca.
- Demandas envolvendo compra de imoveis na planta com discussao de retardation de obra sem sentença definitiva.
- Valor nominal inferior a R$ 15.000,00 (quinze mil reais).

**Indicadores de complexidade consumidor:**

- Inversao do onus da probatorio pendente de analise pericial.
- Grau de judicializacao do reu (volume de acoes em andamento como proxy de dificuldade de execucao).
- Existencia de acoes coletivas conexas (art. 104 do CDC).
- Necessidade de pericia tecnica nao realizada.

### Previdenciario

**Aceitacao preferencial:**

- Acoes de concessao de beneficio com sentenca de procedencia e implementation pendente.
- Acoes de revision de beneficio com diferenças atrasadas ja calculadas em liquidacao.
- Creditos derivados de mandados de seguranca concessorios com beneficio mantido.
- Restituicao de contribuicoes previdenciarias indevidas com transito em julgado.

**Criterios de rejeicao:**

- Ações em que o INSS demonstrou boa-fé objetiva e a tese do autor foi superada por jurisprudencia pacificada desfavoravel.
- Pedidos de beneficios urbanos sem comprovação de carencia minima.
- Acoes com dependentes habilitados em conflito sobre a herança do credito.
- Creditos cujo valor mensal do beneficio seja inferior a 1 (um) salario-minimo.
- Ações com discussao sobre qualidade de segurado sem comprovacao de atividade rural.
- Valor nominal inferior a R$ 10.000,00 (dez mil reais).

**Indicadores de complexidade previdenciario:**

- Necessidade de produzao de provas testemunhais ou periciais ainda nao realizadas.
- Acao pendente de julgamento de apelacao pelo TRF com teses controversas.
- Discusssao sobre BPC/LOAS com renda per capita borderline (proxima ao corte de 1/4 do salario-minimo).
- Beneficio com mais de um titular ou beneficiario com tutela/curatela em debate.

---

## 3. Faixas de Valor e Prazos

A tabela abaixo define as faixas de valor nominal do credito judicial, os prazos estimados de resolucao e o multiplo de retorno esperado pela PX. Estes parametros servem como referencia para enquadramento inicial — a analise detalhada ocorre na Due Diligence e na Analise de Viabilidade.

| Faixa de Valor Nominal              | Prazo Estimado de Resolucao | Multiplo de Retorno Bruto | Taxa de Desconto Media | Aporte Maximo PX (% do valor nominal) | Prioridade Triagem |
|--------------------------------------|-----------------------------|---------------------------|------------------------|---------------------------------------|--------------------|
| R$ 10.000 — R$ 30.000               | 12 — 24 meses              | 1.3x — 1.6x              | 22% — 28%             | 55% — 65%                            | Baixa              |
| R$ 30.001 — R$ 100.000              | 18 — 36 meses              | 1.5x — 2.2x              | 18% — 24%             | 50% — 65%                            | Media              |
| R$ 100.001 — R$ 300.000             | 24 — 48 meses              | 1.8x — 2.8x              | 15% — 22%             | 45% — 60%                            | Alta               |
| R$ 300.001 — R$ 500.000             | 30 — 54 meses              | 2.0x — 3.2x              | 14% — 20%             | 40% — 55%                            | Alta               |
| Acima de R$ 500.000                 | 36 — 60 meses              | 2.2x — 3.8x              | 12% — 18%             | 35% — 50%                            | Critica            |

### 3.1 Notas Metodologicas

- **Multiplo de retorno bruto:** Refere-se a relacao entre o valor total recebido pela PX ao final do processo (principal + juros + correcao) e o valor aportado na antecipacao. Nao inclui custos operacionais internos.
- **Prazo estimado:** Calculado a partir da data de assinatura do contrato de cessao de credito. Inclui periodo de execucao, eventuais recursos e efetivo recebimento via deposito judicial ou leilao.
- **Aporte maximo:** Percentual maximo do valor nominal que a PX esta disposta a adiantar ao cedente. Casos com score de complexidade >= 4 podem ter o aporte reduzido em ate 15 pontos percentuais.
- **Prioridade de triagem:** Determina a ordem de processamento quando ha volume superior a capacidade operacional do time de triagem.

### 3.2 Prazos por Tipo de Acao

Os prazos acima sao medias ponderadas. A tabela abaixo apresenta os ranges especificos por tipo:

| Tipo de Acao    | Prazo Minimo (meses) | Prazo Medio (meses) | Prazo Maximo (meses) | Observacoes                                              |
|-----------------|----------------------|---------------------|----------------------|----------------------------------------------------------|
| Trabalhista     | 8                    | 24                  | 48                   | Execucao provisoria pode antecipar recebimento parcial  |
| Civel           | 12                   | 36                  | 60                   | Precatorios federais seguem calendario do tribunal       |
| Consumidor      | 6                    | 18                  | 36                   | Empresas de grande porte tendem a cumprir espontaneamente|
| Previdenciario  | 12                   | 30                  | 54                   | Depende de oficio ao INSS e regime de precatorios       |

---

## 4. Score de Complexidade

Todo credito submetido a triagem recebe um Score de Complexidade entre 1 (menos complexo) e 5 (mais complexo). O score e atribuido pelo Analista de Triagem com base nos criterios objetivos abaixo e confirmado pelo Coordenador de Origination para scores >= 4.

### Escala e Criterios

#### Score 1 — Simples / Baixo Risco

- Sentenca transitada em julgado com valor liquido certo.
- Execucao com garantia ja penhorada (dinheiro, imovel com matricula limpa).
- Devedor com patrimonio manifesto e sem outras execucoes significantes.
- Sem recursos pendentes, sem incidentes processuais.
- Documentacao completa e sem lacunas.
- Probabilidade de recebimento estimada > 85%.

**Exemplo tipico:** Execucao trabalhista com penhora sobre conta bancaria do reclamado ja bloqueada via SISBAJUD.

#### Score 2 — Moderado-Simples

- Sentenca com transito em julgado, mas execucao ainda nao iniciada.
- Recursos pendentes sem efeito suspensivo (execucao provisoria viavel).
- Devedor identificado com patrimonio, mas sem garantia constituída.
- Incidentes processuais menores (impugnacao ao cumprimento de sentenca com tese frágil).
- Documentacao completa ou com lacunas menores passiveis de obtencao rapida.
- Probabilidade de recebimento estimada: 70% — 85%.

**Exemplo tipico:** Acao de cobranca consumerista com sentenca procedente, apelacao do reu sem efeito suspensivo, devedor e operadora de telecom com rating solido.

#### Score 3 — Moderado

- Sentenca de primeiro grau favoravel com apelacao pendente e efeito suspensivo.
- Execucao iniciada sem localizacao de bens do devedor (consultas preliminares negativas).
- Liquidacao por artigos em andamento com itens contestados.
- Devedor com patrimonio, mas com outras execucoes em curso (concorrencia de credores).
- Necessidade de complementacao documental relevante (ex: atualizacao de guias previdenciarias).
- Probabilidade de recebimento estimada: 55% — 70%.

**Exemplo tipico:** Acao civil publica derivada de relaao de consumo com sentenca procedente, reu recorrendo com efeito suspensivo, patrimoni identificavel mas com gravames.

#### Score 4 — Complexo

- Decisao de primeiro grau favoravel, mas com tese juridica passivel de revisao em instancia superior.
- Devedor em dificuldade financeira (consultas a SERASA, CADIM, SISBAJUD indicam multiplos bloqueios frustrados).
- Grupo economico discutido: necessidade de demonstracao de solidarity entre pessoas juridicas.
- Conflito de competência entre turmas ou secoes do tribunal.
- Precatorio com disputa de preferencia ou em posicao distante na ordem cronologica.
- Documentacao com lacunas significantes (ex: ausencia de peticao inicial original).
- Probabilidade de recebimento estimada: 40% — 55%.

**Exemplo tipico:** Reclamatoria trabalhista com condenacao solidaria entre 4 empresas do mesmo grupo economico, duas delas em recuperacao judicial, com penhora frustrada e bens de terceiros em discussao.

#### Score 5 — Altamente Complexo / Alto Risco

- Teses juridicas inovadoras ou contra jurisprudencia dominante do STF/STJ/TST.
- Devedor em falencia ou liquidacao judicial sem perspectiva de pagamento integral.
- Acao com incidente de resolucao de demandas repetitivas (IRDR) ou assento vinculativo pendente.
- Execucao contra a Fazenda Publica com precatorio nao inscrito e autor sem preferencia legal.
- Fraud execution configurada ou suspeita de fraude na cadeia de creditos.
- Multiple creditors disputando o mesmo ativo com penhoras concorrentes.
- Probabilidade de recebimento estimada: < 40%.

**Exemplo tipico:** Acao previdenciaria revisional com tese sobre tempo de serviço rural sem provas materiais, sentenca procedente reformada pelo TRF, recurso especial com repercussao geral reconhecida pelo STF.

### Fatores que Elevam o Score

Cada fator abaixo adiciona +1 ao score base (limitado ao maximo de 5):

1. Reu em recuperacao judicial, falencia ou intervencao (exceto se garantia real ja constituída).
2. Recurso especial ou extraordinario pendente com repercussao geral ou assunto relevante.
3. Conflito de competencia territorial ou funcional nao resolvido.
4. Ausencia de patrimonio identificavel do devedor apos pesquisa patrimonial preliminar.
5. Documentacao incompleta com mais de 3 itens essenciais ausentes.
6. Existencia de acoes conexas ou dependentes que possam impactar o credito.
7. Cedente com historico de anulacao de cessao de credito em operacoes anteriores.
8. Credito derivado de acao coletiva sem individualizacao da cota-parte.
9. Discussao sobre legitimidade ativa ou passiva pendente de resolucao.
10. Acao tramitando em vara com tempo medio de julgamento superior a 36 meses.

### 4.1 Limiares de Decisao

| Score | Decisao                                         | Proximo Passo                                    |
|-------|-------------------------------------------------|--------------------------------------------------|
| 1-2   | Aprovado automaticamente para Due Diligence     | Encaminhar ao time de DD em ate 2 dias uteis    |
| 3     | Aprovado com ressalva — requer validacao do Coordenador | Coordenador analisa em ate 3 dias uteis     |
| 4     | Retido para analise do Diretor Juridico         | Diretor emite parecer em ate 5 dias uteis       |
| 5     | Rejeitado — recomendacao de nao prosseguimento  | Comunicar cedente com fundamentacao em ate 3 dias|

---

*Documento aprovado pelo Comite de Risco Juridico em 28/02/2025. Proxima revisao: 31/08/2025.*
