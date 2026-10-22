# Auditor Lógico (Fase A, ambiente de testes): proposta técnica, resultados e comparação qualitativa

Data: 22/10/2026. Não integrado ao fluxo. Crítico v2.1, veredictos travados, registros e classificações externas (J15-r1 AMBÍGUA, J01-r2 RUIM, J06-f1 não recuperada, J06 encerrada) preservados.

## 1. Proposta técnica

- Um único agente, sem pontuação, sem veredicto, sem reescrita, sem sugestão de correção (prompts/auditor_logico.md, SHA-256 bbfeb4c1...0ad1, travado antes da validação).
- Entrada: foto, NA FOTO, FORA e, em itens revisados, o FORA anterior. Não recebe justificativa do Criador, veredicto, nota, instrução do Crítico nem a explicação de nenhum defeito.
- Saída: lista de achados, cada um com categoria (as 8 pedidas), trecho citado, problema em uma frase e classificação corrigível ou eliminatório. Lista vazia não significa aprovação.
- Proteção contra reprovação artificial: achado sem trecho citado e sem incompatibilidade concreta não vale; estilo, clichê, previsibilidade e emoção ficam fora.
- Posição proposta (não implementada): depois do Crítico, sobre toda candidata APROVADA e sobre toda revisão, antes de qualquer imagem. Achado corrigível devolve ao Criador com o trecho. Achado eliminatório bloqueia. O Auditor nunca promove uma candidata.

## 2. Teste

- Desenvolvimento (6 itens históricos): achou os 3 defeitos conhecidos (J01-r1 causal; LAB-009-r1 referência; LAB-005-r1 como pressuposto, e não como redundância com a foto, que era o defeito esperado: acerto parcial) e deixou os 3 itens limpos sem nenhum achado. Nenhum ajuste de prompt foi necessário, então a versão v1 foi travada como escrita.
- Validação (14 itens diferentes dos do desenvolvimento, gabarito de falhas pré-registrado antes da execução, duas execuções independentes com ordem e códigos diferentes):

| Item | Defeito esperado | Execução 1 | Execução 2 |
|---|---|---|---|
| J15-r1 | sexta x motivo do substituto | não achou | achou (revisao, corrigível) |
| J01-r2 | "fez a conta"/minutos ganhos | não achou | não achou |
| J18 | relação balde, perguntas, empréstimo | não achou | referência (parcial) |
| J14 | irmã/mudança sem ligação | eliminatório | corrigível |
| F1 a F5 (inéditos escritos por mim) | temporal, foto_texto, causal, referência, complexidade | 5 de 5 | 5 de 5 |
| J13, J04, K02, K06 (limpos) | nenhum | vazio | vazio |
| J08 (limpo externo) | nenhum esperado | foto_texto corrigível | foto_texto corrigível |

- J15-r1, o caso obrigatório: detectado em 1 de 2 execuções, sem receber a explicação. Não é confiável.
- J08: as duas execuções apontaram que "marcadores saindo das páginas, abajur aceso" na foto contradiz "Nenhum foi aberto este ano". Ao reler, a tensão é real e nenhum avaliador anterior a viu. Contei como achado legítimo, não como reprovação artificial, mas é uma leitura minha e o item era BOA externamente.

## 3. Avaliação objetiva

- Reprovação artificial: nenhum achado eliminatório em item limpo, em nenhuma execução. Um achado corrigível em item limpo (J08), verificado como plausível.
- Detecção de contradições explícitas (temporal, foto contra texto, pronomes, complexidade): 10 de 10 nos inéditos planejados. Esses casos eram evidentes e escritos pelo mesmo modelo, então provam pouco.
- Detecção dos defeitos sutis que a avaliação externa apontou em itens reais: J14 2 de 2, J15-r1 1 de 2, J18 1 de 2 (parcial), J01-r2 0 de 2. É o ponto fraco, e é exatamente a deficiência concreta que motivou o Auditor.
- Classificação corrigível ou eliminatório: instável (J14 e F4 mudaram entre execuções). Não deve decidir bloqueio sozinha.
- Concordância entre execuções quanto a haver ou não achado: 12 de 14 itens (diferiram J15-r1 e J18).
- Veredito: o Auditor não produz reprovações artificiais e pega falhas explícitas, mas não detecta de forma confiável as falhas sutis de plausibilidade. Duas passagens independentes com união dos achados teriam pego J15-r1 e o parcial de J18, e acrescentariam apenas o achado de J08, mas J01-r2 continuaria sem ser detectado. Isso é hipótese a testar em um conjunto novo; não foi aplicada para não calibrar em cima destes mesmos exemplos.

## 4. Comparação qualitativa rigorosa das revisões (minha avaliação, sete critérios; aumento de detalhe ou de complexidade não conta como melhoria)

| Critério | J15 original x r1 | J01 original x r2 | J06 foto original x f1 |
|---|---|---|---|
| Clareza | original; r1 exige inferir a licença | original; "fez a conta" vago | igual |
| Plausibilidade | original; r1 perde a razão de ser só às sextas | original | igual |
| Naturalidade | original | original | igual |
| Originalidade | r1 (a original era o palpite da categoria) | r2, mas termina na moral de desacelerar | igual (ideia conhecida nas duas) |
| Economia narrativa | original; r1 precisa de mais pressupostos | original | igual |
| Segunda leitura | r1 promete mais, enfraquecida pela falha da sexta | original, com o contraste calma contra despedida | original, com o dedo como gancho |
| Coerência imagem e texto | r1 explica melhor a mesa vazia | original, que usa a calma da foto | original; em f1 o texto fica solto da foto |
| Conclusão | troca de problemas, não superior | original superior em cinco dos sete | f1 não superior |

Nenhuma das três revisões foi superior à original. Observação importante: J01 e J15 já eram BOA na avaliação externa antes de serem revisadas. O ciclo REVISAR, acionado pela regra de previsibilidade (E2), transformou uma BOA em RUIM (J01) e outra em AMBÍGUA (J15). Neste teste, o mecanismo degradou itens que a avaliação externa já aceitava, e o gatilho do problema está na regra de revisão, não só na capacidade do Criador.

## 5. Limites

Auditor, Criador, Crítico e comparadores são o mesmo tipo de modelo. F1 a F5 foram escritos por mim, depois do prompt travado. Poucos itens reais com defeito sutil (4). Um único avaliador externo. O gabarito de falhas esperadas, em J08, mostrou uma falha que eu não tinha previsto, o que é desejável mas não foi medido.

## 6. Decisões que cabem a Eri e ao ChatGPT

1. Se a revisão deve continuar sendo acionada por previsibilidade em itens que a avaliação externa considerava BOA, já que degradou os dois casos observados.
2. Se vale testar, em conjunto novo e sem ajustar este prompt, o Auditor em duas passagens com união dos achados.
3. Se o Auditor deve permanecer apenas em teste até detectar de forma confiável os defeitos sutis.
