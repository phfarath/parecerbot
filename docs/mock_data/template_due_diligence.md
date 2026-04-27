# Template de Due Diligence — PX Ativos Judiciais

**Versao:** 2.4 | **Vigencia:** 15/01/2025 | **Classificacao:** Interno — Uso Restrito

---

## 1. Objetivo da Due Diligence

A Due Diligence (DD) e a segunda etapa do pipeline de aquisicao de creditos judiciais da PX Ativos Judiciais. Sua funcao e verificar, de forma exhaustiva, a solidez juridica e economica do credito apresentado, confirmando ou retificando os parametros levantados na triagem inicial.

A DD e disparada automaticamente apos aprovacao da triagem com Score de Complexidade de 1 a 4. Casos com Score 5 sao rejeitados na origem e nao seguem para DD.

A DD deve ser concluida dentro dos seguintes prazos, contados do recebimento do deal pela equipe de DD:

| Score de Complexidade | Prazo Maximo (dias uteis) | Responsavel |
|-----------------------|---------------------------|-------------|
| 1-2                   | 5                         | Analista de DD |
| 3                     | 10                        | Analista de DD + Revisor Juridico |
| 4                     | 15                        | Analista de DD + Diretor Juridico |

### 1.1 Escopo

A DD cobre tres dimensoes:

1. **Dimension Juridica:** Validade do credito, solidez da sentenca, riscos recursais, qualidade da execucao.
2. **Dimension Financeira:** Confirmacao do valor, atualizacao monetaria, calculo do VPL, verificacao de encargos.
3. **Dimension Operacional:** Identificacao patrimonial do devedor, viabilidade de execucao, estimativa de prazo real de recebimento.

---

## 2. Documentacao Obrigatoria

Todo credito submetido a DD deve conter, no minimo, os seguintes documentos:

| # | Documento | Obrigatorio | Observacao |
|---|-----------|-------------|------------|
| 1 | Peticao inicial (copia integral) | Sim | Inclui pedidos, causas de pedir e valor atribuido |
| 2 | Sentenca ou decisao que reconheceu o credito | Sim | Deve estar com certidao de transito em julgado ou indicacao de recursos pendentes |
| 3 | Acordao (se houver) | Condicional | Obrigatorio se houve apelacao julgada |
| 4 | Certidao de objeto e peça (COP) | Sim | Emitida ha no maximo 30 dias |
| 5 | Procuracao outorgada ao advogado do cedente | Sim | Com poderes especificos para cessao de credito |
| 6 | Carta de cessao de credito (rascunho) | Sim | Modelo padrao PX, preenchido pelo cedente |
| 7 | Documento de identidade do cedente (PF) ou contrato social (PJ) | Sim | CNPJ/CPF, comprovacao de residencia/sede |
| 8 | Certidao de casamento ou pacto antenupcial (PF) | Condicional | Se cedente casado, necessario para validade da cessao |
| 9 | Certidoes negativas do cedente (CND federal, estadual, municipal, trabalhista) | Sim | Emitidas ha no maximo 90 dias |
| 10 | Comprovacao de propriedade do credito | Sim | Demonstracao da cadeia successoria ou originaria do direito |

### 2.1 Documentos Complementares (solicitados conforme caso)

- Laudos periciais (medicos, contabeis, engenharia)
- Planilha de calculo de atualizacao monetaria (HF, SELIC, INPC conforme aplicavel)
- Certidao de inteiro teor da distribuicao da acao
- Declaracao de inexibilidade de preferencia ou prioridade legal
- Comprovante de residencia do exequente para fins de penhora

---

## 3. DD por Categoria

### Acoes Trabalhistas

**Verificacoes especificas:**

1. **Legitimidade do credito trabalhista:**
   - Confirmar existencia de vinculo empregaticio (CTPS, contrato, testemunhas)
   - Verificar se as verbas deferidas estao individualizadas na sentenca
   - Conferir calculo de horas extras com reflexos (DSR, ferias + 1/3, 13o, FGTS + 40%, aviso previo)

2. **Situacao do reclamado:**
   - Consulta SERASA/SPC para verificar situacao financeira
   - Consulta ao DJe e CENPROT para identificar outras execucoes em curso
   - Verificar existencia de grupo economico (contratos sociais, NFs, site da empresa)
   - Consultar lista de empresas em recuperacao judicial e falencia

3. **Riscos trabalhistas especificos:**
   - Existencia de embargos de terceiro sobre bens penhorados
   - Possibilidade de modulacao de efeitos pelo TST em recursos vinculados
   - Discussao sobre base de calculo do FGTS (saldo ou deposito)
   - Preferencia de creditos trabalhistas no limite de 150 salarios minimos (art. 83, I, LF)

4. **Calculo:**
   - Atualizacao: INPC ate 12/2021, IPCA-E a partir de 01/2022
   - Juros: 1% ao mes ate 08/2023, taxa Selic a partir de 09/2023 (Lei 13.467/2017)
   - Imposto de renda: verificar faixa de isencao conforme art. 6o, V, Lei 7.713/88

### Acoes Civeis

**Verificacoes especificas:**

1. **Titulo executivo:**
   - Confirmar liquidez e certeza do titulo judicial
   - Verificar se liquidacao por artigos ou arbitramento foi concluida
   - Em precatorios: confirmar inscricao, ordem cronologica e existencia de preferencia

2. **Situacao do devedor:**
   - Consulta ao CADIM (Cadastro de Inadimplentes)
   - Consulta ao INFOJUD para identificacao de bens e rendas
   - Verificar existencia de bens imoveis via matricula no cartorio de registro de imoveis
   - Consultar Sistema ARISP para bens imoveis no Estado de Sao Paulo

3. **Riscos civeis especificos:**
   - Possibilidade de anulacao de sentenca por fraude (art. 485, CPC)
   - Existencia de litispendencia ou coisa julgada em acao identica
   - Clausulas de nao responsabilizacao ou limitacao de danos no contrato original
   - Exequibilidade de penhora sobre bem de familia (art. 3o, Lei 8.009/90 — excecoes)

4. **Calculo:**
   - Atualizacao: INPC ou IPCA-E conforme periodo
   - Juros moratorios: 1% ao mes (regra geral) ou taxa Selic (execucao fiscal)
   - Honorarios successivos: verificar se inclusos na condenacao ou pendentes

### Acoes de Consumo

**Verificacoes especificas:**

1. **Relacao de consumo:**
   - Confirmar enquadramento como consumidor (destinatario final, pessoa fisica ou juridica)
   - Verificar se o fornecedor e empresa com capacidade tecnica e financeira para cumprimento
   - Existencia de codigo de defesa do consumidor aplicavel (art. 6o e 14, CDC)

2. **Situacao do fornecedor:**
   - Rating de credito (Moody's, S&P, Fitch ou equivalente nacional)
   - Volume de acoes em andamento (indicador de dificuldade financeira)
   - Existencia de recall, comunicados ou acordos com orgaos de fiscalizacao

3. **Riscos consumeristas especificos:**
   - Inversao do onus probatorio que possa prejudicar a execucao
   - Acoes coletivas conexas que possam afetar o credito individual (art. 104, CDC)
   - Necessidade de pericia tecnica ou medica nao realizada
   - Danos morais puros com quantum discutivel (ausencia de parametro objetivo)

4. **Calculo:**
   - Danos materiais: comprovacao do prejuizo + atualizacao
   - Danos morais: parametros de razoabilidade (TJSP media: R$ 5k-20k para casos simples)
   - Multa por descumprimento de tutela antecipada: verificar percentual fixado

### Acoes Previdenciarias

**Verificacoes especificas:**

1. **Beneficio previdenciario:**
   - Confirmar concessao ou revisao deferida na sentenca
   - Verificar se implementation ja ocorreu (oficio ao INSS, DER)
   - Confirmar diferencas atrasadas calculadas em liquidacao
   - Verificar se existe acumulo ilegitimo de beneficios

2. **Situacao do INSS como devedor:**
   - Regime de precatorios (federal): verificar posicao na fila e valor inscrito
   - Verificar se beneficio de prestacao continuada (BPC/LOAS) — depende de renda per capita
   - Confirmar se existe RPV (Requisicao de Pequeno Valor) elegivel (ate 60 salarios minimos)

3. **Riscos previdenciarios especificos:**
   - Recurso especial com tese de repercussao geral pendente no STF
   - Comprovacao de atividade rural (reconhecimento de tempo de servico sem provas materiais)
   - Mudanca de entendimento do STF sobre tema (ex: tempo especial, contribuinte individual)
   - Existencia de dependentes habilitados com conflito sobre cotas-partes

4. **Calculo:**
   - Atualizacao: INPC (art. 41-A, Lei 8.213/91)
   - Juros: Selic a partir da citacao (Sumula 204, STJ)
   - Honorarios successivos: 10% sobre as prestacoes vencidas (Sumula 111, STJ)
   - IRPF: verificar isencao conforme faixa (art. 6o, V, Lei 7.713/88)

---

## 4. Red Flags

A presenca de qualquer um dos itens abaixo constitui sinal de alerta critico. O analista de DD deve classificar como Red Flag ou Deal-Breaker:

### Deal-Breakers (rejeicao obrigatoria)

| # | Red Flag | Fundamentacao |
|---|----------|---------------|
| 1 | Acao em segredo de justica | Impossibilidade de verificacao de conteudo e terceiros interessados |
| 2 | Reu em recuperacao judicial ou falencia sem garantia real constituida | Art. 49 e 83, Lei 11.101/05 — credito quirografario com baixa recuperacao |
| 3 | Risco de prescricao intercorrente | Art. 40, Lei 6.830/80 — perda do direito de acao se arquivado ha mais de 1 ano |
| 4 | Fraude na cadeia de cessao | Art. 120-131, CPC — anulacao de actos processuais |
| 5 | Cedente declarando falencia ou insolvente | Art. 130, CPC — invalidade da cessao de credito |
| 6 | Conflito de competencia nao resolvido | Incerteza sobre foro competente pode extender prazo indefinidamente |
| 7 | Acao de competencia originaria de tribunal superior | Custos de acompanhamento inviabilizam retorno |

### Red Flags (requer analise aprofundada)

| # | Red Flag | Acao Recomendada |
|---|----------|-----------------|
| 1 | Devedor com mais de 50 execucoes em curso | Avaliar concorrencia de credores e patrimoni disponivel |
| 2 | Sentenca com fundamentacao generica ou contradictoria | Solicitar parecer juridico independente |
| 3 | Pericia controversa com laudos divergentes | Avaliar necessidade de terceiro perito |
| 4 | Ausencia de bens penhoraveis na primeira pesquisa | Ampliar busca (online,offline, bens intangiveis) |
| 5 | Cedente com historico de litigios sobre cessao de credito | Verificar casuistica e fundamentacao |
| 6 | Acao com valor nominal sub judice (recurso sobre quantum) | Recalcular VPL com cenario conservador |
| 7 | Existencia de denuncia da lide ou chamamento ao processo | Avaliar impacto no prazo e complexidade |
| 8 | Precatorio em posicao superior a 5 anos na ordem cronologica | Verificar razoes do atraso e perspectiva real |

---

## 5. Prazos e Entregaveis

### 5.1 Cronograma de DD

| Etapa | Prazo (dias uteis) | Responsavel | Entregavel |
|-------|-------------------|-------------|------------|
| Verificacao documental | D+1 a D+3 | Analista de DD | Checklist preenchido |
| Analise juridica | D+2 a D+5 | Analista de DD | Parecer juridico preliminar |
| Pesquisa patrimonial | D+1 a D+7 | Assistente de DD | Relatorio de bens e consultas |
| Calculo financeiro | D+3 a D+7 | Analista Financeiro | Planilha de VPL e cenarios |
| Parecer consolidado | D+5 a D+10 | Coordenador de DD | Relatorio final de DD |
| Decisao | D+10 a D+15 | Comite de Aprovacao | Aprovado / Rejeitado / Condicionado |

### 5.2 Formato do Relatorio de DD

O relatorio final deve conter:

1. Capa com dados do deal (protocolo, cedente, tipo de acao, valor)
2. Resumo executivo (1 pagina)
3. Analise juridica completa
4. Analise financeira com cenarios (otimista, base, pessimista)
5. Relatorio de pesquisa patrimonial
6. Classificacao de risco e score final
7. Recomendacao (aprovar/rejeitar/condicionar) com fundamentacao
8. Anexos (documentos, calculos, consultas)

### 5.3 Escalacao

| Situacao | Escalar para |
|----------|-------------|
| Red Flag identificado | Coordenador de DD imediatamente |
| Prazo de DD excedido em mais de 3 dias | Diretor de Operacoes |
| Divergencia entre analista e revisor | Diretor Juridico |
| Deal com valor nominal > R$ 500.000 | Comite de Aprovacao obrigatorio |

---

*Documento aprovado pelo Comite de Risco Juridico em 10/01/2025. Proxima revisao: 10/07/2025.*
