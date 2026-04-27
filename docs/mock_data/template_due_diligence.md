# Template de Due Diligence

**Documento:** DD-001
**Versão:** 2.4
**Vigência:** A partir de 15/01/2026
**Aprovação:** Diretoria Jurídica
**Revisão:** Anual

---

## 1. Propósito

Este documento padroniza a execução da Due Diligence (DD) sobre ativos pré-aceitos na triagem (PT-001). A DD tem objetivo confirmatório: validar que os pressupostos da triagem se sustentam diante de análise documental aprofundada e identificar riscos que justifiquem reprecificação ou rejeição.

A DD precede a Análise de Viabilidade (MV-001) e gera o parecer técnico que subsidia a decisão de aquisição.

## 2. Estrutura da DD

A DD é organizada em **cinco blocos** executados em ordem. Falha bloqueante em qualquer bloco interrompe o processo e gera relatório de não conformidade.

| Bloco | Foco | Responsável |
|---|---|---|
| 1. Documental | Completude e autenticidade | Analista Jr |
| 2. Processual | Histórico do processo, fase, recursos | Analista Pleno |
| 3. Cedente | Capacidade jurídica e patrimonial | Analista Pleno |
| 4. Devedor | Solvência, restrições, contingências | Analista Sr |
| 5. Risco específico | Red flags por natureza | Analista Sr + Coord. |

## 3. Bloco 1 — Documental

Validação obrigatória dos seguintes documentos. Ausência de qualquer item bloqueia o avanço da DD.

| Item | Origem | Validação |
|---|---|---|
| Petição inicial | Autos | Conferir partes, pedido, valor da causa |
| Sentença | Autos | Conferir dispositivo, condenação líquida ou ilíquida |
| Acórdão (se houver) | Autos | Verificar trânsito, eventuais reformas |
| Certidão de trânsito em julgado | Autos / cartório | Data, integralidade |
| Cálculo homologado | Contadoria judicial | Bater valor com pedido de cumprimento |
| Procuração do cedente | Cedente | Vigência, poderes específicos |
| Documentos pessoais cedente | Cedente | RG, CPF, comprovante de endereço |
| CNDs do cedente | Receita Federal / PGFN / Trabalhista | Verificar débitos que possam afetar a cessão |

**Red flag bloqueante:** divergência entre o valor da sentença e o valor pleiteado superior a 10% sem justificativa documental.

## 4. Bloco 2 — Processual

Revisão integral do andamento processual com foco em:

### 4.1 Fase atual
Cumprimento de sentença iniciado, intimado o devedor, embargos pendentes ou já julgados, expedição de precatório/RPV.

### 4.2 Histórico de recursos
Mapear todos os recursos interpostos (ordinários e extraordinários). Recurso especial ou extraordinário ainda admitido implica risco residual de reforma.

### 4.3 Prescrição intercorrente
Calcular janela de prescrição. Em ações trabalhistas, considerar a Lei 11.232/2005 (prazo de 2 anos da última movimentação). Em ações cíveis, aplicar o prazo prescricional originário.

### 4.4 Cumulação de cessões
Verificar se houve cessão anterior do mesmo crédito ou parte dele. Consultar averbações nos autos e certidão de inteiro teor.

**Red flag bloqueante:** existência de penhora no rosto dos autos em favor de terceiro não solucionada.

## 5. Bloco 3 — Cedente

### 5.1 Capacidade jurídica
- Pessoa física: capacidade civil plena, ausência de interdição
- Pessoa jurídica: regularidade dos atos constitutivos, poderes do signatário
- Espólio: inventário em andamento ou concluído, alvará judicial específico para a cessão

### 5.2 Capacidade patrimonial
- Pesquisa em órgãos de proteção ao crédito (Serasa, SCR Bacen quando aplicável)
- Verificação de execuções pessoais em desfavor do cedente
- Análise de risco de pedido de revogação por fraude contra credores (art. 158-165 CC)

### 5.3 Conflito de interesse
Cruzar cedente com base de partes relacionadas da PX (vide PC-001). Identificação de relação não declarada é red flag bloqueante.

## 6. Bloco 4 — Devedor

A profundidade da análise varia pela natureza do devedor:

### 6.1 Devedor privado (pessoa jurídica)
- Situação cadastral CNPJ
- Análise de demonstrações financeiras dos últimos 3 exercícios (quando obrigatórias)
- Pesquisa de protestos e ações em desfavor
- Risco de recuperação judicial ou falência (índice Z-Score quando aplicável)
- Histórico de pagamento em ações similares

### 6.2 Devedor público (precatórios)
- Identificar ente devedor (União, Estado, Município)
- Estoque de precatórios do ente — consulta TR-001
- Histórico de pagamento (em dia, atrasado, regime especial)
- Posição do crédito na fila cronológica
- Risco político (mudança de gestão, EC 109/2021, etc.)

## 7. Bloco 5 — Risco Específico

Cada natureza de ação tem checklist próprio aplicado neste bloco.

### 7.1 Trabalhista
- Verificar grupo econômico do empregador
- Avaliar risco de redirecionamento para sócios
- Conferir cálculos de juros e correção (taxa Selic vs IPCA-E vs TR)

### 7.2 Cível
- Mapear seguradoras envolvidas
- Verificar denunciações da lide
- Avaliar risco de responsabilidade subsidiária

### 7.3 Consumidor
- Histórico do réu em demandas similares
- Risco de litigância de massa (precedentes desfavoráveis ao réu)

### 7.4 Previdenciário
- Confirmar expedição da requisição (RPV ou precatório)
- Verificar se há retenção de IR ou contribuição previdenciária

### 7.5 Tributário
- Parecer tributário externo obrigatório acima de R$ 1.000.000
- Verificar trânsito consolidado da tese
- Risco de compensação rejeitada pela RFB

## 8. Saídas da DD

A DD produz três entregas obrigatórias:

1. **Relatório de DD** — documento estruturado nos cinco blocos
2. **Matriz de riscos identificados** — com classificação (alto / médio / baixo) e mitigação proposta
3. **Recomendação** — uma de três:
   - **Aprovar com preço de referência:** segue para Análise de Viabilidade
   - **Aprovar com ressalva:** segue com desconto adicional precificado
   - **Rejeitar:** com motivo formal

## 9. SLAs

| Tamanho do ticket | Prazo para conclusão da DD |
|---|---|
| Até R$ 200.000 | 3 dias úteis |
| R$ 200.001 – R$ 1.000.000 | 5 dias úteis |
| R$ 1.000.001 – R$ 5.000.000 | 8 dias úteis |
| Acima de R$ 5.000.000 | 12 dias úteis |

## 10. Governança

Pareceres com recomendação de "Aprovar com ressalva" e ticket acima de R$ 1.000.000 exigem aprovação do Coordenador Jurídico antes do encaminhamento à Análise de Viabilidade.

## 11. Documentos Relacionados

- PT-001 — Política de Triagem
- MV-001 — Manual de Análise de Viabilidade
- TR-001 — Tabela de Riscos
- PC-001 — Política de Compliance
- FO-001 — Fluxo Operacional
