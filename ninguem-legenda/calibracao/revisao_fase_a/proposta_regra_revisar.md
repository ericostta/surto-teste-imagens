# Proposta mínima: regra de acionamento do REVISAR

Data: 22/10/2026. Fase A. Texto de proposta, nada implementado. Crítico v2.1, Auditor Lógico v1, gabaritos, comparações, revisões e classificações externas permanecem como estão. Nenhum agente novo.

## 1. Diagnóstico em duas linhas

(a) A regra E2 do v2.1 ("se 2 ou 3 leitores cegos capturaram a revelação, o máximo é REVISAR") fez da previsibilidade um gatilho. (b) A instrução de revisão que ela gera ("deslocar a revelação para algo que a foto não sugira") pede para trocar a ideia central, e foi isso que degradou J01 e J15.

## 2. A regra

Mudança 1. A previsão cega deixa de ser condição e vira evidência. Continua sendo coletada e registrada. Ela só pesa por dentro de falhas legítimas: se os leitores capturaram a revelação e o Crítico não consegue nomear uma perspectiva específica (E5), isso é clichê efetivo; se capturaram porque a foto entrega, é redundância. Capturar, sozinho, não reprova nem manda revisar.

Mudança 2. O Crítico decide pela existência de defeito concreto. Três ramos, todos por defeito nomeado:

A. APROVAR: nenhum defeito das listas B e C, e E1 (transformação), E3 (clareza), E4 (elo humano) e E5 (perspectiva específica) satisfeitas. A revelação pode ser relativamente previsível se tiver segunda leitura, ligação específica com a foto e perspectiva própria.

B. REVISAR: existe ao menos um defeito concreto, nomeável e corrigível sem trocar a revelação central. Lista fechada: relação narrativa insuficiente (elo implícito demais), ambiguidade de referência prejudicial, contradição, plausibilidade comprometida, redundância parcial ou elemento visual dispensável que antecipa, perda da segunda leitura por excesso de explicação, clichê efetivo que o Crítico consegue corrigir apontando que tipo de detalhe específico acrescentar.

C. REPROVAR: defeito estrutural. Conexão arbitrária, obscuridade, sentimentalismo ou moralismo, ausência de segunda leitura, redundância integral ou foto que entrega a revelação inteira, clichê sem transformação e sem como ser corrigido, repetição, veto. Se a correção exigiria outra ideia, é nova candidata (inclusive pela triagem de foto já aprovada).

Mudança 3. Como a instrução de REVISAR passa a ser escrita. Todo REVISAR traz: o defeito (da lista B), o trecho citado, a correção mínima e o que NÃO pode mudar, incluindo explicitamente a revelação central. Fica proibida instrução do tipo "mude a revelação". Um REVISAR sem defeito nomeado e sem trecho é inválido (verificação determinística simples, no mesmo molde do validar_avaliacao.py).

Mudança 4. Recuperação continua exigindo ser superior à original na comparação rigorosa, e o Auditor Lógico segue só experimental, fora da regra.

O que mudaria nos arquivos, se autorizado: o texto de E2, T1 e da seção "Quando é REPROVADA" em prompts/critico.md (nasceria uma v2.2, a v2.1 fica preservada), o validador, e a seção REVISAR do Criador. Nada disso foi feito.

## 3. Aplicação aos casos históricos (leitura dos campos já registrados; não é reexecução nem reclassificação)

| Caso | Registro v2.1 | Onde a regra levaria | Observação |
|---|---|---|---|
| J15 original | REVISAR. Único defeito acionador: 3 de 3 leitores previram. O próprio Crítico registrou perspectiva específica ("ritual semanal de deixar a mesa pronta antes de qualquer aviso") | A, sujeito ao Crítico confirmar E5. Sem a regra de previsão, não resta defeito concreto | Coerente com a classificação externa BOA. A revisão r1 não teria sido acionada |
| J01 original | REVISAR. Defeitos: previsão (cai fora), contraste que a foto já mostra, "último dia" sem motivo (dois tons incompatíveis). Perspectiva específica só parcial | B, com defeito concreto único e corrigível: a ambiguidade do "último dia". Instrução mínima: dizer o motivo em poucas palavras. Preservar a revelação e o contraste calma contra despedida | Divergência residual com a classificação externa BOA: o Crítico ainda não daria A por causa de E5. Pelo menos a revisão não deslocaria mais a ideia |
| J06 original | REPROVADA. Eliminatórias: foto entrega (elemento dispensável: o dedo), redundância com a foto, clichê sem perspectiva. Perspectiva específica "nenhuma" | Fronteira entre B e C. O elemento da foto é corrigível; o clichê só é corrigível se o Crítico nomear o detalhe a acrescentar. Nos registros originais ele não nomeou; na reavaliação de f1 nomeou ("para quem ela encena o gosto") | A regra deixaria J06 em C pelo registro original. A decisão externa de encerrar J06 prevalece e não é alterada |
| J08 | APROVADA, E1 a E5, 1 de 3 leitores capturaram. O Crítico já anotou a tensão dos marcadores e a descartou ("embora possam ser antigos") | A, sem mudança | O defeito apontado pelo Auditor v1 não está confirmado (decisão externa). O Crítico já separava contradição verdadeira de leitura alternativa plausível; o Auditor v1 não. Registro apenas como lição para qualquer versão futura do Auditor |

## 4. Riscos e como não aumentá-los

- Risco: tirar o gatilho pode deixar passar clichê. Mitigação já existente: T10 e E5 continuam obrigatórios para A, e 2 ou 3 leitores capturando sem perspectiva específica passa a ser prova de clichê efetivo.
- Risco: o Crítico aprovar mais. A regra só retira um motivo de REVISAR; não afrouxa nenhum teste de A. Se o total de aprovações subir, a causa seria E5 julgado com generosidade, e isso deve ser olhado antes de qualquer decisão.
- Fronteira B contra C continua sendo julgamento (J06). A regra obriga o Crítico a nomear o detalhe corrigível, o que torna a decisão auditável.

## 5. Se autorizado, validação mínima (não executada)

Reescrever só os trechos citados em uma v2.2, preservando a v2.1; testar em um conjunto pequeno e inédito, com rótulo externo anterior à execução, medindo apenas: aprovações de itens externamente RUIM (deve ser zero), BOA enviadas a REVISAR por previsibilidade (deve ser zero), e se cada REVISAR traz defeito nomeado. Sem calibração ampla e sem ajuste a partir dos itens usados até aqui.
