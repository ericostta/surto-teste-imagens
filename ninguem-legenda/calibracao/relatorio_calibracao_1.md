# Relatório de calibração 1: Crítico x Eri

Data: 22/10/2026. Conjunto de 18 itens (12 do lote real, 6 negativos construídos).
Equivalência usada: APROVADA = BOA, REVISAR = AMBÍGUA, REPROVADA = RUIM.

## Resultado

- Concordância exata: 11 de 18 (61%). A meta inicial de 80% NÃO foi atingida.
- Negativos construídos: 6 de 6 (todos reprovados por ambos).
- Lote real: 5 de 12 (42%).
- Divergências polares (BOA contra RUIM): 0. Nenhum item que Eri considerou RUIM foi aprovado pelo Crítico.
- Todas as 7 divergências são de um degrau (algo contra AMBÍGUA).

## Divergências

| Item | Origem | Crítico | Eri | Direção |
|---|---|---|---|---|
| K02 | LAB-007 fila sem motivo | REVISAR | BOA | Crítico mais severo |
| K03 | LAB-011 diploma antes da pintura | REVISAR | BOA | Crítico mais severo |
| K08 | LAB-003 marmita | REPROVADA | AMBÍGUA | Crítico mais severo |
| K09 | LAB-009 relógio e pai | REPROVADA | AMBÍGUA | Crítico mais severo |
| K17 | LAB-010 escovas de dente | REPROVADA | AMBÍGUA | Crítico mais severo |
| K18 | LAB-012 cadeira de balanço | REPROVADA | AMBÍGUA | Crítico mais severo |
| K15 | LAB-001 cadeira de escritório | APROVADA | AMBÍGUA | Crítico mais brando |

## Leitura

1. Neste conjunto o Crítico errou mais por severidade (6 casos) do que por inflação (1 caso). O risco de "nota alta demais" que eu temia não apareceu de forma clara, mas a amostra é pequena.
2. Quatro dos cinco textos afetivos e melancólicos que reprovei (marmita, relógio, escovas, cadeira de balanço) Eri classificou como AMBÍGUA, não como RUIM. Para ela, "previsível" rebaixa, mas não elimina. No Crítico atual, previsibilidade pesa como eliminatória.
3. Os dois textos de humor e observação que mandei revisar (fila, diploma) Eri achou BOA. A objeção de "generalidade" que apliquei à fila talvez seja rigorosa demais.
4. O único aprovado por mim que Eri não aprovou (LAB-001) é o que eu mesmo anotei com ressalva ("a primeira" ambíguo).
5. Os 6 negativos foram fáceis, então não provam calibração fina. Só provam que o Crítico não aprova lixo evidente.

## Limites desta medida

- 18 itens é amostra pequena: um item muda 5,5 pontos percentuais.
- O Crítico rodou no mesmo ambiente do Criador, em pacote cego mas sem isolamento real.
- Eri rotulou o texto e a descrição da foto, sem foto. O julgamento pode mudar com a imagem.
- Este conjunto agora serve para AJUSTAR o Crítico. Validar com ele seria avaliar o sistema com o que ele já conhece.

## Ajustes propostos (ainda não aplicados)

A. Previsibilidade deixa de ser eliminatória sozinha. Passa a rebaixar para REVISAR. REPROVADA fica para: redundância entre foto e texto, conexão arbitrária, linguagem proibida, repetição, foto que entrega a revelação.
B. Ambiguidade de referência vira checagem explícita do Crítico (ex.: "a primeira", "ela", "isso" sem antecedente claro).
C. Generalidade (teste de troca de cena) passa a pesar menos quando o humor é de observação social.
D. Separar no registro REVISAR de REPROVADA: REVISAR volta ao Criador com a instrução do que mudar, em vez de ser descartado.

## Próximo passo sugerido

1. Aplicar A a D no prompt do Crítico.
2. Rodar o Crítico revisado como subagente isolado nas mesmas 12 candidatas (só para medir mudança, não como validação).
3. Gerar um conjunto NOVO e inédito de cerca de 18 itens para validação, com muitos casos de fronteira e poucos negativos óbvios.
