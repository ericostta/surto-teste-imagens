# Relatório de calibração 2: Crítico v2 (diagnóstico) e fluxo REVISAR

Data: 22/10/2026. Fase A, só texto. Nada aqui é validação independente.

## Como a execução foi feita

- Previsão cega: um subagente separado viu só a descrição da foto e o NA FOTO dos 36 itens e previu a revelação. Isso substitui a "previsão" que o Crítico v1 fazia sabendo o texto.
- Crítico v2: três subagentes independentes, cada um em contexto limpo, lendo só o prompt e o seu pacote. Filtros omitidos de propósito, para o julgamento do Crítico não ser ajudado por eles.
- Conferência de integridade: cada subagente usou só os arquivos permitidos (o do conjunto inédito fez uma operação a mais, só para contar os próprios veredictos).
- Códigos embaralhados e sem identificação de origem.
- Registros da primeira calibração (rótulos de Eri, gabarito v1, registro.csv, avaliação v1) permanecem intactos.

## 1. Diagnóstico nos 18 itens da calibração 1

Conjunto já usado para ajustar o Crítico: serve só como diagnóstico.

| | v1 | v2 |
|---|---|---|
| Concordância exata com Eri | 11 de 18 (61%) | 12 de 18 (67%) |
| Divergências polares (BOA contra RUIM) | 0 | 0 |
| Negativos óbvios reprovados | 6 de 6 | 6 de 6 |

A diferença é de um item e está dentro do ruído. Não se deve dizer que o v2 melhorou. O que se pode dizer: o v2 não relaxou nos negativos óbvios e continua sem divergência polar.

Divergências do v2 com Eri:

| Item | Origem | Eri | v2 | Direção |
|---|---|---|---|---|
| K01 | cama de solteiro | BOA | REVISAR | v2 mais severo |
| K03 | diploma | BOA | REVISAR | v2 mais severo |
| K13 | planta | BOA | REVISAR | v2 mais severo |
| K16 | mala | BOA | REVISAR | v2 mais severo |
| K08 | marmita | AMBÍGUA | APROVADA | v2 mais brando, dois degraus acima do v1 |
| K17 | escovas de dente | AMBÍGUA | APROVADA | v2 mais brando, dois degraus acima do v1 |

### Achado principal: o v2 perdeu o teste de originalidade

Marmita e escovas foram de REPROVADA (v1) para APROVADA (v2). A leitura do raciocínio do v2 mostra a causa: o v1 reprovava como "trope" e "sentimentalismo de manual", e o v2 não tem nenhum teste de clichê. Ele pergunta se há segunda leitura, elo humano, concretude e ambiguidade, mas não pergunta se a ideia é o primeiro palpite da sua categoria (mãe com marmita, escova de dente como intimidade, cadeira vazia como ausência, mala pronta como espera). O critério "Originalidade, 0 a 20 pontos" do DNA ficou sem teste correspondente. Isso é o risco de flexibilização artificial que você apontou, e veio de uma omissão do ajuste, não de intenção.

Proposta (não aplicada, fora da autorização): T10 ORIGINALIDADE. A ideia é o clichê da categoria? Se sim, no máximo REVISAR, com instrução de deslocar a revelação para algo que a categoria não sugere.

### Previsão cega

A previsão feita por outro leitor mudou vários julgamentos em relação ao v1, que era contaminado. Mas é uma tentativa única por item, e dois itens mostram sua fragilidade: o leitor previu "solidão" na marmita (o Crítico entendeu como "não previu") e previu "partida adiada" na mala com confiança alta (o Crítico entendeu como "previu quase tudo"). Um preditor por item é instável. Se a previsibilidade continuar pesando no veredicto, vale usar 2 ou 3 previsões independentes por item.

## 2. Fluxo REVISAR (diagnóstico)

Os 7 itens que o v2 classificou como REVISAR na calibração 1 voltaram ao Criador com a instrução do Crítico, foram corrigidos (versões -r1), passaram de novo pelos filtros e foram reavaliados por um Crítico novo, sem ver a versão anterior nem a instrução.

| Revisão | Resultado | Observação |
|---|---|---|
| LAB-011-r1 (diploma) | APROVADA, não previu, nota 86 | revelação inverteu a leitura da foto |
| LAB-004-r1 (planta) | APROVADA, nota 76 | a vizinha como testemunha cega foi o deslocamento |
| LAB-012-r1 (cadeira de balanço) | APROVADA, nota 66 | a ideia passou de luto para humor doméstico (o gato), mantendo o gesto de contornar |
| LAB-001-r1 (cadeira de escritório) | APROVADA, mas INVÁLIDA | aprovada sem a evidência E3, que as regras do próprio Crítico exigem |
| LAB-006-r1 (mala) | REVISAR | revelação continua confirmando a leitura óbvia |
| LAB-005-r1 (cama) | REVISAR, piorou | minha revisão reenumerou os objetos visíveis da foto |
| LAB-009-r1 (relógio) | REVISAR | minha revisão criou ambiguidade de pronomes |

Leitura:
- Aprovações válidas: 3 de 7 em um ciclo, não 4. A inválida foi detectada pelo validador determinístico (validar_avaliacao.py), que passa a fazer parte do fluxo: nenhuma aprovação segue sem as 4 evidências.
- Duas das falhas persistentes (cama, relógio) foram introduzidas pelo Criador na correção, não pelo Crítico. A qualidade da revisão depende do Criador.
- Tensão estrutural: a instrução do primeiro Crítico mandava preservar "a falta de explicação" do relógio, e o Crítico limpo, que não conhece essa restrição, pediu para eliminá-la. É o custo de reavaliar em contexto limpo. O limite de 2 ciclos contém o risco, e a decisão final de descartar ou aceitar cabe às regras e não a um ciclo infinito.
- Nenhuma revisão é validação: os itens já eram do conjunto de ajuste e os rótulos de Eri são da versão original, não da revisada.

## 3. Conjunto inédito (conjunto 2)

18 itens novos, todos aprovados nos filtros determinísticos, incluindo um redundante sutil e um moralismo sem palavras-chave, que só o Crítico pode pegar. As avaliações do Crítico v2 estão travadas no repositório (gabarito_claude2.json, com SHA-256 registrado antes dos rótulos de Eri) e só serão comparadas depois que Eri rotular. Este relatório não as revela.

Verificação de coerência interna das 43 avaliações do v2: 1 inconsistência (a revisão da cadeira de escritório, acima). As demais, inclusive as do conjunto inédito, estão coerentes com as regras.

## Pendências e decisões de Eri

1. Autorizar ou não o T10 de originalidade (v2.1). Se autorizado antes de Eri rotular o conjunto 2, o v2.1 pode ser avaliado nele com a mesma garantia de cegueira. Depois dos rótulos, qualquer teste do v2.1 nesse conjunto fica contaminado.
2. Autorizar 2 ou 3 previsões independentes por item.
3. Rotular o conjunto 2 (calibracao/conjunto2/para_eri_2.md).
