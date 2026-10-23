# Protocolo de validação independente do Crítico v2.2 (pré-registrado)

Data: 22/10/2026. Nada abaixo foi executado. A execução só começa depois que os rótulos externos estiverem recebidos e fixados no repositório.

## Conjunto

24 itens inéditos escritos por Claude, 3 de cada tipo pedido por Eri: boa história relativamente previsível; clichê com aparência de profundidade; revelação surpreendente mas arbitrária; omissão narrativa legítima; ambiguidade que compromete a compreensão; ideia boa com defeito pontual corrigível; proposta estruturalmente ruim; história simples, original e plausível. Todos passam nos filtros determinísticos (conjunto/resultado_filtros.json). Códigos embaralhados Q01 a Q24. O tipo pretendido de cada item está em conjunto/gabarito_tipos_privado.json (SHA-256 registrado), só para cobertura; não é rótulo de qualidade. Nenhum item histórico entra.

## Ordem de execução

1. Eri/ChatGPT classificam Q01 a Q24 (BOA, AMBÍGUA, RUIM, com motivo para AMBÍGUA e RUIM) sem ver nenhum veredicto. Os rótulos são commitados antes de qualquer execução.
2. Três previsões cegas independentes por item (leitores novos, só foto e NA FOTO).
3. Crítico v2.2 em duas execuções independentes, ordem e códigos diferentes, contexto limpo, sem filtros.
4. Controle: Crítico v2.1 em uma execução sobre as mesmas previsões, só para verificar que a v2.2 não ficou mais permissiva.
5. validar_avaliacao.py em todas as saídas (modo v2.2 para a v2.2).
6. Nada é ajustado depois de ver os resultados.

## O que será registrado (sem usar um percentual isolado como prova)

1. Falsas aprovações: APROVADA em item rotulado RUIM; e, à parte, APROVADA em item AMBÍGUA (aprovação contestável).
2. Falsas reprovações: REPROVADA em item rotulado BOA.
3. Revisões desnecessárias: REVISAR em item rotulado BOA.
4. Defeitos corretamente identificados: o defeito citado coincide com o motivo externo (em RUIM e AMBÍGUA).
5. Defeitos inventados ou insuficientemente demonstrados: defeito sem trecho, com demonstração hipotética ou genérica, ou que contradiz o texto; incluindo defeitos citados em itens BOA.
6. Consistência: concordância de veredicto e de categoria de defeito entre as duas execuções da v2.2.
Mais: contagem de aprovações da v2.2 contra a v2.1 no controle, por tipo de item. Toda discordância com o rótulo externo será examinada caso a caso, com o trecho que a motivou.

## Sinais de alerta pré-definidos

Qualquer falsa aprovação em item RUIM. Qualquer REVISAR ou REPROVADA cuja justificativa dependa só de previsão. Qualquer defeito sem trecho ou demonstração. Aprovação da v2.2 em item de clichê com ar de profundidade ou de surpresa arbitrária. Divergência entre as duas execuções em mais de uma categoria de tipo.

## Limitações declaradas

Itens escritos pelo mesmo modelo que depois os avalia; 3 itens por tipo é pouco; um único avaliador externo, que também é um modelo; os tipos pretendidos são intenção minha e não verdade; o critério externo é o mesmo único critério dos rótulos anteriores. Por isso nenhum resultado será tratado como homologação, e a decisão de homologar fica com Eri.
