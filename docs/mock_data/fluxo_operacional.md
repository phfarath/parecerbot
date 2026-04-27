# Fluxo Operacional — PX Ativos Judiciais

**Versao:** 4.0 | **Vigencia:** 01/03/2025 | **Classificacao:** Interno — Uso Restrito

---

## 1. Visao Geral do Processo

O pipeline de aquisicao de creditos judiciais da PX e composto por cinco etapas sequenciais, cada uma com entradas, saidas, responsaveis e SLAs definidos. O objetivo e garantir que cada credito seja avaliado com rigor, velocidade e rastreabilidade.

```
Oportunidade → Triagem → Due Diligence → Analise de Viabilidade → Aprovacao → Monitoramento
```

**Tempo total estimado (melhor caso):** 20 dias uteis (triagem + DD + analise + aprovacao)
**Tempo total estimado (caso complexo):** 45 dias uteis

---

## 2. Etapa 1: Triagem Inicial

### Entradas
- Formulario de oportunidade preenchido (canal: site, e-mail, parceiro, API)
- Documentacao minima: peticao inicial + sentenca ou decisao relevante
- Dados do cedente (identificacao, contato, relacao com o credito)

### Processamento
1. Recebimento e registro no sistema (protocolo PX-TRI-AAAA-NNNNN)
2. Verificacao de completude documental minima
3. Classificacao por tipo de acao (trabalhista, civel, consumidor, previdenciario)
4. Aplicacao dos criterios de aceite/rejeicao por tipo (Politica de Triagem, Secao 2)
5. Enquadramento na faixa de valor e prazo (Politica de Triagem, Secao 3)
6. Atribuicao do Score de Complexidade (1-5)
7. Decisao: aprovado para DD / retido / rejeitado

### Saidas
- Parecer de triagem com score e recomendacao
- Classificacao e prioridade do deal
- Lista de documentos complementares solicitados (se aplicavel)

### Responsaveis

| Funcao | Papel |
|--------|-------|
| Analista de Triagem | Execucao da triagem, score, recomendacao |
| Coordenador de Origination | Homologacao de scores >= 4 |
| Diretor Juridico | Decisao sobre casos borderline |

### SLA
- **5 dias uteis** a partir do recebimento completo da documentacao
- Deals com prioridade critica (valor > R$ 500k): 3 dias uteis

### Gargalos Conhecidos
- Cedentes que nao enviam documentacao completa na primeira submissao (causa de 40% dos atrasos)
- Classificacao de acoes com caracteristicas hibridas (ex: trabalhista + civil) requer consulta ao Diretor Juridico
- Volume de oportunidades em periodos de campanha de parceiros pode gerar fila de triagem

---

## 3. Etapa 2: Due Diligence

### Entradas
- Parecer de triagem aprovado com score
- Documentacao do cedente (completa apos complementacoes da triagem)
- Documentos processuais (peticao, sentenca, acordao, COP)

### Processamento
1. Verificacao documental (checklist de documentos obrigatorios e complementares)
2. Analise juridica (solidez da sentenca, riscos recursais, qualidade da execucao)
3. Pesquisa patrimonial do devedor (SISBAJUD, INFOJUD, CADIM, cartorios, SERASA)
4. Consulta de acoes conexas e dependentes
5. Verificacao de red flags e deal-breakers
6. Calculo financeiro preliminar (valor atualizado, estimativa de custos)
7. Emissao do relatorio de DD

### Saidas
- Relatorio de DD completo (juridico, financeiro, patrimonial)
- Lista de red flags identificados (classificados por severidade)
- Score de complexidade confirmado ou retificado
- Recomendacao de prosseguimento ou rejeicao

### Responsaveis

| Funcao | Papel |
|--------|-------|
| Analista de DD | Execucao da DD e relatorio |
| Revisor Juridico | Revisao de deals com score >= 3 |
| Assistente de DD | Pesquisas patrimoniais e consultas |
| Coordenador de DD | Parecer consolidado e recomendacao final |

### SLA
- Score 1-2: **5 dias uteis**
- Score 3: **10 dias uteis**
- Score 4: **15 dias uteis**

### Gargalos Conhecidos
- Pesquisa patrimonial em comarcas sem sistema online (requer expedicao de oficios fisicos — prazo de 15-30 dias)
- Consulta ao SISBAJUD pode retornar dados desatualizados (saldo de conta pode ter sido movido)
- Pericias medica em acoes consumeristas/previdenciarias podem estar pendentes e nao agendadas

---

## 4. Etapa 3: Analise de Viabilidade

### Entradas
- Relatorio de DD aprovado
- Score de complexidade confirmado
- Dados financeiros (valor atualizado, custos estimados, prazo de execucao)
- Pesquisa patrimonial consolidada

### Processamento
1. Pontuacao dos quatro fatores do SVP (PJS, MRA, PR, QPD)
2. Calculo do SVP consolidado
3. Calculo do VPL em tres cenarios (otimista, base, pessimista)
4. Definicao da taxa de desconto aplicavel (por tipo de acao e score)
5. Determinacao do valor maximo de aporte
6. Verificacao de limites de concentracao de portfolio
7. Emissao do parecer de viabilidade

### Saidas
- Parecer de viabilidade com SVP e VPL
- Valor maximo de aporte recomendado
- Cenarios de retorno (multiplo bruto e liquido)
- Condicoes especiais ou excecoes (se aplicavel)

### Responsaveis

| Funcao | Papel |
|--------|-------|
| Analista Financeiro | Calculo do SVP, VPL e cenarios |
| Coordenador de Origination | Validacao do parecer |

### SLA
- **3 dias uteis** para scores 1-3
- **5 dias uteis** para scores 4

### Gargalos Conhecidos
- Divergencia entre analistas sobre pontuacao dos fatores do SVP (resolvida por media aritmetica)
- Cenarios pessimistas com VPL negativo exigem recalculo com parametros alternativos
- Verificacao de limites de concentracao requer acesso ao portfolio atualizado (sistema pode estar desatualizado)

---

## 5. Etapa 4: Aprovacao

### Entradas
- Parecer de triagem
- Relatorio de DD
- Parecer de viabilidade
- Proposta de aporte (valor, condicoes, prazo)

### Processamento
1. Verificacao de aderencia aos criterios de aprovacao (valor, score, concentracao)
2. Avaliacao do nivel de aprovacao requerido (conforme valor nominal)
3. Reuniao ou deliberacao do nivel competente
4. Decisao: aprovado / rejeitado / condicionado (com contrapartidas)
5. Emissao da aprovacao formal

### Saidas
- Aprovacao formal (ou rejeicao fundamentada)
- Valor de aporte autorizado (pode ser inferior ao recomendado)
- Condicoes especiais (prazos de acompanhamento, gatilhos de revisao)

### Responsaveis

| Faixa de Valor | Aprovador |
|----------------|-----------|
| Ate R$ 100 mil | Coordenador + Analista Financeiro |
| R$ 100-300 mil | Diretor de Operacoes + Diretor Financeiro |
| R$ 300-500 mil | Comite de Aprovacao (3 diretores) |
| Acima de R$ 500 mil | Comite + CEO (unanimidade) |

### SLA
- **2 dias uteis** para aprovacoes de Coordenador/Diretor
- **5 dias uteis** para Comite de Aprovacao
- **7 dias uteis** para Comite + CEO

### Gargalos Conhecidos
- Comite de Aprovacao se reune semanalmente — deals submetidos fora do prazo podem aguardar ate 7 dias
- Deals condicionados exigem nova rodada de aprovacao apos atendimento das condicoes
- CEO pode solicitar analise complementar para deals acima de R$ 500 mil

---

## 6. Etapa 5: Monitoramento

### Entradas
- Contrato de cessao de credito assinado
- Credito judicial em nome da PX (apos cessao)
- Plano de execucao e acompanhamento

### Processamento
1. Acompanhamento processual mensal (andamento da acao, decisoes, recursos)
2. Execucao judicial (requerimento de penhora, leilao, oficios)
3. Monitoramento financeiro (atualizacao de VPL, cenarios revisados)
4. Reporte mensal ao Comite de Risco (status do portfolio)
5. Provision trimestral para perdas (conforme politica contabil)
6. Encerramento apos liquidacao integral do credito

### Saidas
- Relatorio mensal de acompanhamento por deal
- Atualizacao de VPL e cenarios
- Provision para perdas
- Relatorio de portfolio para stakeholders

### Responsaveis

| Funcao | Papel |
|--------|-------|
| Analista de Acompanhamento | Monitoramento processual e execucao |
| Advogado Externo | Representacao judicial (quando necessario) |
| Coordenador de Portfolio | Reporte ao Comite e provision |

### SLA
- Relatorio mensal: ate o dia 10 do mes seguinte
- Provision trimestral: ate o dia 15 do mes seguinte ao trimestre
- Alertas criticos (ex: decisao judicial desfavoravel): comunicacao em ate 24 horas

### Gargalos Conhecidos
- Acompanhamento de precatorios federais e lento (poucas atualizacoes no sistema do tribunal)
- Execucao judicial em comarcas do interior pode ter andamento lento (sobrecarga da vara)
- Atualizacao de VPL requer recalculo manual quando parametros mudam (Selic, INPC)

---

## 7. Gargalos Conhecidos (Visao Consolidada)

| Etapa | Gargalo Principal | Impacto | Mitigacao |
|-------|-------------------|---------|-----------|
| Triagem | Documentacao incompleta do cedente | +3-5 dias por ciclo de complementacao | Checklist online com validacao automatica |
| DD | Pesquisa patrimonial em comarcas offline | +15-30 dias | Parceria com cartorios digitais (ARISP, CNS) |
| DD | Pericias pendentes nao agendadas | Impede conclusao da DD | Verificar status da pericia na triagem |
| Analise | Divergencia entre analistas | +1-2 dias | Media aritmetica + documentar discrepancia |
| Aprovacao | Periodicidade do Comite | +2-7 dias | Reunioes extraordinarias para deals criticos |
| Monitoramento | Comarcas com andamento lento | Prazo real > prazo estimado | Priorizar deals com execucao provisoria |

---

*Documento aprovado pela Diretoria Executiva em 20/02/2025. Proxima revisao: 20/08/2025.*
