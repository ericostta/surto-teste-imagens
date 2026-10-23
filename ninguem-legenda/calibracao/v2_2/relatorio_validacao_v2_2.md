# Relatório: validação independente do Crítico v2.2 experimental

Data: 22/10/2026. Fase A. Protocolo executado como pré-registrado. Rótulos externos fixados antes (SHA-256 7b47574b...c2ef, commit 819d8c7). Nenhum prompt, rótulo ou item foi ajustado depois. A v2.2 NÃO foi homologada e este relatório não propõe homologá-la.

Execuções: 3 previsões cegas por item; Crítico v2.2 em duas execuções independentes (ordem e códigos diferentes); Crítico v2.1 em uma execução de controle sobre as mesmas previsões. Validador: 0 inconsistências nas 72 avaliações. Resultados brutos em conjunto/resultados/.

## 1. Quadro geral (rótulos externos: 5 BOA, 8 AMBÍGUA, 11 RUIM)

| | v2.1 (controle) | v2.2 execução 1 | v2.2 execução 2 |
|---|---|---|---|
| Aprovadas / revisar / reprovadas | 4 / 9 / 11 | 7 / 7 / 10 | 10 / 5 / 9 |
| 1. Falsa aprovação (RUIM aprovada) | 0 | 0 | 0 |
| Aprovação contestável (AMBÍGUA aprovada) | 3 (Q10, Q17, Q18) | 4 (Q06, Q10, Q17, Q22) | 5 (Q02, Q06, Q10, Q18, Q22) |
| 2. Falsa reprovação (BOA reprovada) | 0 | 0 | 0 |
| AMBÍGUA reprovada | 1 (Q08) | 0 | 0 |
| BOA aprovadas | 1 de 5 | 3 de 5 | 5 de 5 |
| 3. Revisão desnecessária (BOA em REVISAR) | 4 (Q05, Q09, Q12, Q15) | 2 (Q05, Q15) | 0 |
| RUIM em REVISAR | 1 (Q21) | 1 (Q21) | 2 (Q21, Q23) |
| Concordância exata (informativa, não é prova) | 15 de 24 | 17 de 24 | 17 de 24 |

Leitura: nenhuma versão aprovou um item RUIM nem reprovou um BOA. A v2.2 reduz as revisões desnecessárias de BOA (4, 2, 0) e recupera BOA aprovadas, mas aprova mais AMBÍGUAS (3, 4, 5) e fica menos estável.

## 2. Pelas seis métricas pedidas

1. Falsas aprovações: zero nas três. Nenhum item de clichê com ar de profundidade (Q07, Q13, Q14) nem de surpresa arbitrária (Q16, Q20, Q23) foi aprovado em nenhuma execução.
2. Falsas reprovações: zero.
3. Revisões desnecessárias: ver quadro. Na execução 1 da v2.2 elas persistiram em Q05 e Q15 por um motivo que a decisão queria eliminar (item 5 abaixo).
4. Defeitos corretamente identificados: nos 11 RUIM, o defeito citado coincide com o motivo externo (aforismo e sentimentalismo em Q01, Q04, Q07, Q13, Q14; redundância em Q03; arbitrariedade em Q16, Q20, Q23; obscuridade e pronomes em Q19). Q21 e Q23 (r2) foram suavizados para REVISAR com o defeito certo. Nas 8 AMBÍGUAS: Q24 identificado nas duas execuções; Q08 nas duas (por clichê, parcialmente coincidente); Q18 e Q02 só na execução 1; Q17 só na execução 2 (a ambiguidade de "diz" que o avaliador externo também sentiu); Q06, Q10 e Q22 não identificados em nenhuma execução da v2.2 (Q10 também aprovado pela v2.1).
5. Defeitos inventados ou insuficientemente demonstrados:
   - Q05, execução 1: o defeito "contradicao" ("nunca esfria" contra "esquenta de novo") é admitido pelo próprio Crítico como tendo leitura plausível, o que a regra da contradição exclui. A execução 2 descartou essa mesma observação como "hipótese sem demonstração". Um exemplo direto da inconsistência.
   - Q05 e Q15, execução 1: o REVISAR depende da concordância dos três leitores cegos (cliche_efetivo e redundancia sustentados pela previsão). A decisão dizia que a previsão não pode, sozinha, produzir REVISAR. A redação permite essa brecha (previsão como prova dentro de um defeito), e a execução 1 a usou; a execução 2 não.
   - Nenhum defeito sem trecho ou sem demonstração; o validador não apontou nenhum aviso de linguagem hipotética.
6. Consistência entre as duas execuções da v2.2: veredicto igual em 18 de 24. Divergiram Q02, Q05, Q15, Q17, Q18 e Q23, todas na fronteira entre APROVADA e REVISAR, exceto Q23 (REPROVADA contra REVISAR). As 9 reprovações coincidentes mostram as mesmas categorias de defeito. A fronteira de aprovação é onde o Crítico é instável.

## 3. Alertas pré-definidos

- Falsa aprovação em RUIM: não disparou.
- REVISAR ou REPROVADA justificado só por previsão: disparou na execução 1 (Q05, Q15). Q08 também depende da previsão nas duas execuções, mas o veredicto coincide com o rótulo externo.
- Defeito sem trecho ou demonstração: não disparou; um defeito insuficientemente demonstrado (Q05, execução 1).
- Aprovação em clichê com aparência de profundidade ou surpresa arbitrária: não disparou.
- Divergência entre execuções em mais de uma categoria de tipo: disparou (cinco tipos).

## 4. Pontos críticos

- A permissividade não apareceu onde mais importa (RUIM), mas apareceu em AMBÍGUA: Q06, Q10 e Q22 foram aprovados nas duas execuções da v2.2. O avaliador externo apontou imprecisões reais (referência da frase "para o lugar continuar dela", personagens e motivo da fita em Q10, razão do segredo em Q22). Para a regra "defeito demonstrado", o Crítico não conseguiu ou não quis demonstrá-las. Há tensão genuína entre evitar defeito hipotético e perder imprecisão real.
- A instabilidade é maior que a da v2.1 controle em um aspecto: a execução 2 aprovou 10 itens contra 7 da execução 1. A diferença de rigor entre duas execuções do mesmo prompt pesa mais que a diferença entre versões.
- Os tipos pretendidos por mim nem sempre coincidiram com o rótulo externo: dos três itens de omissão legítima, só Q15 foi BOA; Q02 e Q08 foram AMBÍGUAS. O teste de "omissão legítima" ficou menos informativo do que o planejado.
- Q09 (BOA) e Q11 (BOA) foram aprovados nas duas execuções e a v2.1 reprovou o primeiro para REVISAR: é o ganho real da mudança. Q12 também.

## 5. Conclusão

Nesta amostra, a v2.2 cumpriu o que tinha de cumprir: não aprovou nada RUIM, não reprovou nada BOA, e reduziu o REVISAR indevido por previsibilidade. Mas não está pronta para homologação. A fronteira entre aprovar e revisar é instável entre execuções, a brecha da previsão como prova de cliché ou redundância ainda produz REVISAR indevido em uma das execuções, e AMBÍGUAS com imprecisões reais passam. Continua experimental.

Possíveis correções, que NÃO foram aplicadas (exigem autorização e um conjunto novo): impedir que a previsão seja a única prova de cliché ou redundância; exigir, para "contradição", que o Crítico escreva a leitura em que ambos os trechos sejam verdadeiros e só reporte se não houver; revisar como a v2.2 trata imprecisões que o avaliador externo percebe mas o Crítico considera "implícito legítimo". Duplicar a execução não é proposto.

## 6. Limitações

Itens escritos por mim e avaliados por agentes do mesmo tipo; 3 itens por tipo; um único avaliador externo, que é um modelo; as duas execuções da v2.2 não esgotam a variabilidade; a concordância exata não é prova; nada foi ajustado depois dos resultados.
