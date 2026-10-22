# Relatório 4: comparação no conjunto inédito (J01 a J18)

Rótulos: avaliação independente 2, feita pelo ChatGPT e encaminhada por Eri (conjunto2/rotulos_chatgpt_2.json). Veredictos do v2 e do v2.1 travados antes (SHA-256 no repositório), sem alteração retroativa. O v1 não foi executado neste conjunto.

| Fonte | Concordância exata | Polares (BOA x RUIM) |
|---|---|---|
| Criador (intenção) | 12/18 (67%) | 0 |
| Crítico v2 | 14/18 (78%) | 1 (J03 aprovada, rótulo RUIM) |
| Crítico v2.1 | 13/18 (72%) | 1 (J06 reprovada, rótulo BOA) |

Aprovou RUIM: v2 em J03; v2.1 em nenhum. Reprovou BOA: v2 em nenhum; v2.1 em J06.
Aprovações: v2 5 (4 BOA, 1 RUIM); v2.1 3 (3 BOA). BOA aprovadas: v2 4 de 6; v2.1 3 de 6.
BOA que ficaram em REVISAR: v2 J06, J15; v2.1 J01, J15. RUIM que ficaram em REVISAR: v2 J17; v2.1 J03, J18.
AMBÍGUA (J02, J16): ambos os Críticos deram REVISAR nas duas, exato.

Originalidade (v2 para v2.1): ganhos J03 (saiu de APROVADA) e J17 (passou a REPROVADA, exato). Perdas J01 (APROVADA para REVISAR, rótulo BOA), J06 (REVISAR para REPROVADA, rótulo BOA) e J18 (REPROVADA para REVISAR, rótulo RUIM). Saldo exato: -1. O teste cortou o único falso positivo, mas custou uma BOA.
A flag "é a associação mais comum" marcou 7 de 10 RUIM e 3 de 6 BOA (J01, J06, J15). Discrimina pouco.
Padrão dominante: J01, J06 e J15 (BOA) foram previstas pelas 3 leituras cegas, e a regra E2 as limita a REVISAR. A severidade vem da previsibilidade, não do T10.

Limitações: um único avaliador, que é um modelo (correlação com o Crítico), não Eri; n=18, uma mudança de item vale 5,5 pontos; v2.1 caiu de 15/18 (em amostra) para 13/18 (inédito); rótulos AMBÍGUA são só 2; sem v1 aqui. Nada foi ajustado a partir desta rodada.
