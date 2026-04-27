# FAQ Interno

**Documento:** FAQ-001
**Versão:** 2.1
**Vigência:** A partir de 20/02/2026
**Aprovação:** Coordenação Operacional
**Revisão:** Trimestral ou ad hoc

---

## 1. Sobre este documento

Este FAQ consolida dúvidas recorrentes do time operacional sobre processos, políticas e terminologia. Não substitui as políticas e manuais formais (PT-001, DD-001, MV-001, TR-001, PC-001, FO-001), apenas complementa.

Em caso de divergência entre este FAQ e qualquer documento normativo, prevalece o documento normativo.

---

## 2. Triagem

### 2.1 Posso aceitar um ativo de R$ 25.000 isolado?

Não. O valor unitário mínimo é R$ 30.000 (vide PT-001, seção 3). A exceção são lotes que agreguem valor superior a R$ 200.000.

### 2.2 E se o originador insistir em um ticket pequeno?

Recuse cordialmente. Tickets abaixo do mínimo desviam tempo do time de DD com retorno operacional desfavorável. Se o originador trouxer recorrência de tickets pequenos, sugira agregação em lote.

### 2.3 O que fazer com ações ainda em fase de conhecimento?

Rejeitar automaticamente, mesmo com sentença favorável. Falta de trânsito em julgado é rejeição automática (PT-001, seção 5).

### 2.4 Aceitamos ações criminais ou de família?

Não. Estão fora do escopo de atuação da PX (PT-001, seção 2).

---

## 3. Due Diligence

### 3.1 A documentação chegou incompleta. O que faço?

Solicitar ao originador o complemento. Após a segunda solicitação não atendida, rejeitar (PT-001, seção 5, item 5).

### 3.2 Como saber se há cessão anterior do mesmo crédito?

Solicitar certidão de inteiro teor do processo e verificar averbações. Em alguns tribunais, é possível consultar diretamente no sistema processual eletrônico. Se houver dúvida, escalar ao Coordenador Jurídico.

### 3.3 O que é "penhora no rosto dos autos"?

Penhora determinada em outro processo sobre o crédito que está sendo executado nestes autos. Se o terceiro tem prioridade sobre o cedente, o ativo é inviável até que essa penhora seja resolvida. Red flag bloqueante na DD (DD-001, seção 4).

### 3.4 Quando é obrigatório o parecer tributário externo?

Em ativos tributários acima de R$ 1.000.000 de valor de face (DD-001, seção 7.5).

### 3.5 Posso usar a mesma DD para vários ativos do mesmo lote?

Sim, desde que os ativos sejam efetivamente homogêneos (mesma natureza, mesmo réu, mesma tese, intervalo de valores compatível). Aplicar amostragem da documentação por amostra estatística mínima de 20% ou 10 ativos, o que for maior.

---

## 4. Análise de Viabilidade

### 4.1 Qual a diferença entre valor de face e valor presente?

**Valor de face:** valor nominal da condenação, atualizado pelos índices judiciais até a data de referência.

**Valor presente:** valor de face descontado pelo prazo estimado de recebimento e pela taxa de retorno-alvo da PX. É o quanto o crédito vale hoje, considerando o tempo até o pagamento e o risco.

Exemplo: ativo de R$ 100.000 que paga em 12 meses com taxa de desconto de 24% a.a. tem valor presente de aproximadamente R$ 80.645.

### 4.2 Como calcular a TIR a posteriori?

Após o pagamento integral, a TIR efetiva é calculada como:

```
TIR mensal = (valor recebido / valor pago) ^ (1 / meses) − 1
TIR a.a. = (1 + TIR mensal) ^ 12 − 1
```

Exemplo: pagamos R$ 80.000, recebemos R$ 100.000 em 12 meses → TIR mensal ≈ 1,87% → TIR anual ≈ 24,9%.

### 4.3 O que é "haircut"?

Desconto aplicado sobre o valor de face para refletir riscos identificados (insolvência parcial, redução em embargos, retenções tributárias). É diferente da taxa de desconto, que reflete o valor do dinheiro no tempo.

### 4.4 Quando reclassificar um ativo já adquirido?

Sempre que houver evento material: pedido de RJ do devedor, decisão judicial relevante, mudança no estoque de precatórios. A reclassificação afeta o provisionamento e a expectativa de retorno.

---

## 5. Terminologia jurídica

### 5.1 RPV vs Precatório

**RPV (Requisição de Pequeno Valor):** modalidade de pagamento de débitos judiciais da Fazenda Pública abaixo do teto legal. Em 2026, o teto federal é R$ 78.000 (60 salários mínimos). Pagamento em até 60 dias após a requisição.

**Precatório:** ordem de pagamento da Fazenda para débitos acima do teto. Inscrito no orçamento do exercício seguinte se requisitado até 02/04. Pagamento conforme cronograma do ente.

### 5.2 Trânsito em julgado

Momento em que a decisão se torna imutável, por esgotamento dos recursos cabíveis ou pelo decurso do prazo recursal sem manifestação. É pressuposto para o cumprimento de sentença na maioria dos casos.

### 5.3 Cumprimento de sentença

Fase processual em que se executa a obrigação reconhecida na sentença. Distingue-se do processo de execução de título extrajudicial.

### 5.4 Cessão de crédito

Transferência onerosa ou gratuita de um direito creditório do cedente (titular original) ao cessionário (no caso, a PX). Regulada pelos arts. 286-298 do Código Civil.

### 5.5 Sucumbência

Honorários advocatícios devidos pela parte vencida ao advogado da parte vencedora. Em geral, integram o crédito a ser executado, mas a PX não adquire honorários sucumbenciais isolados (vide PT-001, seção 4.1).

### 5.6 Prescrição intercorrente

Prescrição que ocorre durante o curso do processo, em razão da paralisação por culpa do credor. Em ações trabalhistas, o prazo é de 2 anos da última movimentação (Lei 11.232/2005). Em ações cíveis, aplica-se o prazo prescricional originário do direito.

### 5.7 Embargos à execução

Defesa do executado contra a execução. Pode versar sobre excesso de execução, inexistência da dívida, prescrição e outras matérias. Suspende a execução em determinadas hipóteses.

### 5.8 Modulação dos efeitos

Decisão do STF que limita os efeitos temporais de uma declaração de inconstitucionalidade. Relevante em teses tributárias.

---

## 6. Operacional

### 6.1 Onde registro o ativo no sistema?

Após pré-aceite, o ativo é cadastrado no Pipefy (módulo "Originação"). Após DD, é movido para o módulo "Análise". Após aprovação do Comitê, vai para "Aquisição".

### 6.2 Como solicitar parecer tributário externo?

Abrir ticket no Slack #juridico-externo com: número do processo, valor, tese tributária, urgência. SLA do escritório parceiro: 5 dias úteis.

### 6.3 Qual o canal para dúvidas urgentes em DD?

Slack #due-diligence durante horário comercial. Em casos críticos fora do horário, contato direto com o Coordenador Jurídico.

### 6.4 Como reportar suspeita de fraude?

Imediatamente ao Compliance Officer (vide PC-001). Não prosseguir com a operação até parecer formal.

---

## 7. Pessoas e papéis

| Papel | Responsabilidade principal |
|---|---|
| Originador | Captura de oportunidades, primeira interlocução com cedentes |
| Analista Jr | Bloco 1 da DD (documental) |
| Analista Pleno | Blocos 2 e 3 da DD (processual e cedente) |
| Analista Sr | Blocos 4 e 5 da DD (devedor e risco específico) |
| Coordenador Jurídico | Aprovação de pareceres com ressalva, casos limítrofes |
| Time de Risco | Backtesting, atualização da TR-001 e MV-001 |
| Comitê de Investimentos | Decisão final de aquisição acima dos limites delegados |

---

## 8. Documentos Relacionados

- PT-001 — Política de Triagem
- DD-001 — Template de Due Diligence
- MV-001 — Manual de Análise de Viabilidade
- TR-001 — Tabela de Riscos
- PC-001 — Política de Compliance
- FO-001 — Fluxo Operacional
- JE-001 — Jurisprudência: Exemplos de Casos
