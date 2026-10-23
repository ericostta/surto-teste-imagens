# Plano experimental conceitual: a referência editorial produz julgamento confiável?

Data: 22/10/2026. Fase A. Plano para discussão e aprovação de Eri. Conceitual: não há prompts experimentais, não há novos textos, não há execuções, não há v2.4. Nada aqui altera registros congelados, a grade das dez janelas, o n8n, a fila ou as skills. Nada é homologado.

Pergunta que orienta o plano, nas palavras de Eri: não queremos saber se o Crítico aprendeu novas palavras ou formatos de justificativa, e sim se ele reconhece melhor a qualidade, erra menos e decide com maior consistência.

## 1. Hipótese concreta

H principal: um Crítico que aplica a referência editorial conceitual (integridade narrativa mais mérito positivo demonstrado, com os requisitos de B e a simetria de rigor) comete menos aprovações indevidas do que a v2.2 num conjunto inédito, sem perder as BOA, e decide com maior consistência entre execuções.

Desdobrada em hipóteses que podem falhar separadamente:
- H1, aprovações indevidas: menos itens de estado REVISAR ou REPROVADA são aprovados, em especial os de premissa sentimental conhecida com gesto concreto, a zona onde a v2.2 e a v2.3-exp falharam.
- H2, reconhecimento de mérito: as BOA continuam aprovadas, e pela razão certa.
- H3, fronteiras: o Crítico separa REVISAR de REPROVADA conforme a possibilidade de correção pontual.
- H4, B contra C: o Crítico não inventa defeitos em BOA nem dispensa falhas relevantes como periféricas.
- H5, consistência: as execuções repetidas concordam mais, e a diferença excede a variação entre execuções da própria v2.2.

Comparador: a v2.2 (principal) e a v2.3-exp (secundário), nas mesmas condições. A versão candidata só será redigida depois da aprovação deste plano, e então travada por hash antes de qualquer execução.

## 2. Melhoria real contra concordância com o avaliador externo

Concordar com um avaliador não é o mesmo que decidir melhor. Cinco salvaguardas:

1. Mais de uma referência, e a referência antes do teste. Rótulos do avaliador externo (cego) e de Eri (cega aos Críticos) sobre todos os itens do teste, ou, se a carga for excessiva, sobre os itens em disputa. O estado de cada item será fixado e selado com hash antes de qualquer execução. Um segundo avaliador de outra família de modelos, se Eri puder obtê-lo, aumenta a independência.
2. Núcleo de consenso e zona contestada. Itens em que todas as referências concordam formam o núcleo (onde o erro é sem desculpa). Itens em que divergem são classificados por Eri como divergência legítima ou erro de leitura (decisão de 22/10). Nos contestados, o Crítico não é medido por escolher o lado de um avaliador, e sim por reconhecer que o caso é contestável e por qual tipo de fundamento (A, B ou C) apoia sua decisão.
3. Razão, não só veredicto. Acerto pelo motivo errado não conta como pleno (regra já adotada). A justificativa é avaliada contra o motivo de referência por um julgador que recebe o contexto completo (foto, textos anteriores, texto integral), corrigindo a limitação do julgador anterior.
4. Controles contra o "aprendeu palavras". (a) Itens com o vocabulário do rubrico ("gesto concreto", "segunda leitura") mas fracos; (b) itens fortes sem esse vocabulário; (c) pares de variações superficiais do mesmo item, em que a qualidade não muda e o veredicto não deve mudar. Se o desempenho melhora no conjunto geral mas desaparece nesses controles, não é melhoria de julgamento.
5. Linhas de base triviais. Um "aprova tudo", um "reprova tudo" e a v2.2 mostram o que cada métrica significaria sem julgamento.

Sem ajustes depois de ver resultados: o conjunto de teste é separado (held-out), nunca foi visto por quem redige o Crítico, e uma vez usado fica queimado para ajustes. Se a versão candidata falhar e for modificada, o novo teste exige novo conjunto.

## 3. Exemplos independentes e variados

Fontes sugeridas, para decisão de Eri sobre o que é viável:
- Textos escritos por Eri (alguns).
- Textos de outras famílias de modelos (por exemplo, pedidos a ChatGPT ou Gemini por Eri), sem passar pelas regras do projeto.
- Edições reais da série já aprovadas por Eri (exemplos positivos humanos).
- Claude com processos de criação variados (o que já fizemos, com independência limitada, declarada).
- Variações superficiais e quase-erros de itens do próprio conjunto, para os controles da seção 2.

Princípios: geração em excesso (por exemplo, cerca de 90 candidatos) e seleção posterior apenas pelos rótulos de referência, nunca pelos resultados do Crítico, de modo a obter estratos que não são construídos mecanicamente para ilustrar categorias; tamanho final de aproximadamente 60 itens, com no mínimo cerca de 12 itens por estrato em que se queira afirmar algo (BOA de consenso, RUIM de consenso, zona contestada, premissa sentimental com gesto concreto). Estratos com menos de 10 itens servem só como descrição, não como prova. Procedência registrada em mapa privado e aberta somente depois.

Inclui, por decisão de Eri, casos que mostrem se o Crítico distingue correção pontual de reconstrução. Para isso, a referência classificará cada item não BOA com um campo adicional: "correção pontual possível?" (com a descrição da correção em uma frase) ou "exige outra ideia".

## 4. Reconhecimento do mérito editorial positivo

O risco é aprovar o "tecnicamente correto". Dois testes complementares:
- Itens limpos e vazios: plausíveis, sem defeito A ou B, mas sem segunda leitura (o texto só complementa a foto). O Crítico não deve aprová-los. Este é o teste direto da distinção integridade contra mérito.
- Itens com mérito e imperfeições periféricas: o Crítico deve aprová-los. Este é o teste contra o excesso de zelo.
Para cada APROVADA, o julgador de contexto completo avalia se os quatro elementos exigidos (segunda leitura, o que muda, elemento específico, por que a objeção relevante não compromete) estão presentes e corretos. Aprovação com mérito mal demonstrado é registrada como acerto sem fundamento pleno, mesmo que o rótulo coincida.

## 5. Fronteiras entre APROVADA, REVISAR e REPROVADA

Medida por matriz de confusão contra o estado de referência, com gravidade ordenada antes do teste: aprovar um item que a referência manda revisar ou reprovar é o erro mais grave; reprovar um BOA, o segundo; confundir REVISAR com REPROVADA, o menos grave. Além do veredicto, verifica-se se o REVISAR veio com os três elementos exigidos (o que preservar, a deficiência, a intervenção localizada) e se a intervenção coincide com a correção pontual descrita pela referência. REVISAR sem esses elementos conta como depósito, não como acerto.

Fronteira B contra C: verificada em dois sentidos. Falsos defeitos: defeito B ou "objeção" em itens de consenso BOA. Dispensas indevidas: itens com falha que a referência considera relevante, em que o Crítico registra a observação e aprova ou revisa por defeito diferente.

## 6. Consistência sem seleção retrospectiva

- Número de execuções por versão fixado antes (proposta: no mínimo 3), com ordem e códigos distintos, contexto limpo, mesma entrada.
- Todas as execuções entram na análise. Nenhum "melhor resultado", nenhuma exclusão posterior. Falha técnica (formato inválido, truncamento) pode ser reexecutada uma vez, com o mesmo prompt, e registrada com o motivo.
- Medidas: concordância de veredicto por item; trocas entre aprovar e não aprovar (o desacordo que mais importa); trocas entre classes; estabilidade da razão citada; todas por estrato.
- Referência de ruído: a variação entre execuções da própria v2.2 no mesmo conjunto (no experimento anterior, RUIM aprovadas variaram de 6 para 2 entre duas execuções). Uma melhoria só conta se estiver fora dessa faixa de variação.
- Variações superficiais (seção 2) medem a estabilidade a mudanças que não alteram a qualidade.

## 7. O que justificaria continuar o desenvolvimento

Condições propostas, todas necessárias, a aprovar por Eri antes do teste (os números são ponto de partida para discussão):
1. Nenhuma aprovação em item de consenso RUIM em nenhuma das execuções.
2. Aprovações de itens de consenso REVISAR ou AMBÍGUA menores que as da v2.2 em todas as execuções, e fora da faixa de variação da v2.2.
3. Pelo menos 90% das BOA de consenso aprovadas em cada execução, com mérito corretamente demonstrado na maioria; nenhuma reprovação de BOA.
4. Troca de aprovar para não aprovar entre execuções não maior que a da v2.2.
5. A maior parte dos acertos com razão correta (acerto pleno), e nenhum defeito inventado em BOA de consenso.
6. Desempenho preservado nos controles de vocabulário e de variação superficial.
7. Bom desempenho no estrato de premissa sentimental conhecida com gesto concreto, ou ao menos melhora clara sobre a v2.2 nele.
8. Sem piora em estratos em que a v2.2 já acertava.

## 8. O que indicaria reconsiderar a estratégia

- A melhoria dentro da faixa de ruído da v2.2.
- Aprovações indevidas persistindo no estrato sentimental, mesmo com a referência aplicada.
- Trocas entre aprovar e não aprovar tão frequentes quanto antes, o que sugere instabilidade que instruções não removem.
- Maioria dos acertos pelo motivo errado ou com justificativas fluentes que a referência desmente (sinal de "aprendeu o formato").
- Melhora que some nos controles de vocabulário ou de variação superficial.
- O Crítico acompanhar um avaliador específico (externo ou Eri) sem separar consenso de zona contestada, ou falhar em reconhecer contestabilidade.
- Aprovações de itens limpos e vazios (mérito não distinguido de integridade).
Qualquer um deles aponta para as alternativas já mapeadas no diagnóstico (reduzir a ambição do Crítico, outra família de modelos como juiz, atacar a geração), e não para mais regras.

## 9. Decisões que preciso de Eri antes de qualquer passo seguinte

1. Rotulagem: Eri rotula todos os itens de teste, só os contestados, ou nenhum além do avaliador externo?
2. Existe acesso a um segundo avaliador de outra família de modelos?
3. Quais fontes de exemplos independentes são viáveis (seção 3)?
4. Tamanho do conjunto e número de execuções por versão (propostos: cerca de 60 itens e 3 execuções).
5. Aprovação ou ajuste dos oito critérios de continuidade e dos sinais de reconsideração.
6. Autoriza controles de variação superficial e itens "limpos e vazios", que exigem criar textos em etapa posterior?

## 10. Limitações do plano

Redigido pelo mesmo modelo que gerou itens e Críticos; as fontes disponíveis de textos independentes são limitadas; um único avaliador externo (e Eri como segunda referência, após conhecer resultados anteriores, mas cega nos itens novos se o protocolo for seguido); o julgador de contexto completo também é um modelo; o tamanho proposto ainda dá pouco poder para estratos pequenos; os critérios numéricos são ponto de partida e não limiares de homologação, que continua sendo decisão de Eri.
