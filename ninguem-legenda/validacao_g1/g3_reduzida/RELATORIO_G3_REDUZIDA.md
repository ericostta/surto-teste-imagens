# Relatório da G3 reduzida: Crítico v2.2 contra v2.4-exp

Data: 23/10/2026. Base: Emenda 1 (commit 4ecd489), saídas brutas lacradas em e5cc8d0 antes de abrir os rótulos. Resultados completos em `analise_g3_resultados.json`; matriz item a item em `matriz_g3.md`. Nada foi homologado, implantado ou publicado. Nenhum prompt, item, rótulo ou arquivo do M1 foi alterado.

## 0. Resposta curta

1. **Conclusão pelo critério da emenda: SUPERIORIDADE NÃO DEMONSTRADA.** A v2.4-exp corrigiu alguns erros, mas perdeu histórias BOA, introduziu erros novos e ficou menos consistente entre as duas execuções. Fora dos itens em tensão, o saldo é praticamente nulo.
2. **Referência editorial provisória para a próxima etapa de laboratório: v2.2**, sem declarar superioridade nem homologação.
3. **Gate:** nenhum dos três desenhos protege de forma suficiente. O mais econômico é o Gate 3 sobre a v2.2, mas ele quase não evita erro. Nenhum serve como base para publicação automática.
4. **Risco dominante:** as duas versões aprovam 8 dos 11 RUIM e 12 ou 13 das 16 AMBÍGUA, e 5 RUIM e 11 AMBÍGUA passam nas quatro execuções. Esses erros não são pegos por segunda avaliação nem pelos sinais de risco.
5. **Avanço:** formalizar o núcleo de identidade pode seguir. A Fase B visual só pode seguir com aprovação editorial humana de cada história, e a apresentação de custo não gera imagens. A autonomia editorial continua não demonstrada.

## 1. Integridade da execução

- 8 partes, 240 avaliações, 30 itens por parte, cobertura de códigos completa e JSON válido em todas. Modelo registrado nos agentes: claude-sonnet-5-5.
- Nenhuma execução foi repetida ou descartada. Nenhuma execução favorável foi escolhida.
- Validador formal (`validar_avaliacao.py`, inalterado): 20 de 240 avaliações com inconsistência apontada (3 na v2.2, 17 na v2.4-exp). Não são falhas de formato, e por isso não houve reexecução. Na v2.4-exp quase todas são objeção bloqueante sem o campo `atinge_nucleo`, ou seja, o prompt candidato é menos obedecido em sua própria estrutura. Registro em `execucoes/validacao_formal_saida.txt`.
- Elegibilidade automática da v2.4-exp: toda APROVADA bruta foi elegível, nenhuma foi barrada. Portanto, **nenhuma diferença entre as versões vem da elegibilidade**. Declaração de divergência material: um único caso (G1-D15, execução 2), sem efeito no veredicto.

Limites: referência de um único avaliador que é um modelo; sem auditoria humana independente; mesmo modelo gera e avalia; isolamento dos agentes documental; as quatro avaliações por item repetem os mesmos 60 textos e as mesmas previsões comuns, não são amostras independentes; só 11 RUIM, e cada item vale cerca de 9 pontos percentuais.

## 2. Composição e tensões

| | BOA | AMBÍGUA | RUIM |
|---|---|---|---|
| Fluxo (30) | 20 | 6 | 4 |
| Desafio (30) | 13 | 10 | 7 |
| Em tensão (17) | 6 (tipo A) | 0 | 11 (tipo B) |
| Fora de tensão (43) | 27 | 16 | **0** |

Todos os 11 RUIM estão em tensão. Por isso nenhuma taxa de RUIM aprovado foi calculada fora das tensões, e a ausência de RUIM nesse grupo não é resultado favorável a nenhuma versão. Os RUIM são, por construção, itens que as previsões cegas não anteciparam e que o rótulo externo reprovou: é exatamente onde o rótulo tem menor confiabilidade.

## 3. Veredictos brutos por execução

| | v2.2 e1 | v2.2 e2 | v2.4 e1 | v2.4 e2 |
|---|---|---|---|---|
| Aprovadas (de 60) | 52 | 52 | 47 | 49 |
| RUIM aprovadas (de 11) | 8 | 8 | 8 | 5 |
| AMBÍGUA aprovadas (de 16) | 13 | 12 | 12 | 12 |
| BOA aprovadas (de 33) | 31 | 32 | 27 | 32 |
| BOA não aprovadas | 2 | 1 | 6 | 1 |

Por estrato:

| | Fluxo RUIM aprov. (de 4) | Fluxo AMB aprov. (de 6) | Fluxo BOA aprov. (de 20) | Desafio RUIM aprov. (de 7) | Desafio AMB aprov. (de 10) | Desafio BOA aprov. (de 13) |
|---|---|---|---|---|---|---|
| v2.2 e1 | 3 | 6 | 20 | 5 | 7 | 11 |
| v2.2 e2 | 3 | 6 | 19 | 5 | 6 | 13 |
| v2.4 e1 | 3 | 6 | 18 | 5 | 6 | 9 |
| v2.4 e2 | 2 | 6 | 20 | 3 | 6 | 12 |

Leitura: na amostra de fluxo, as duas versões aprovam todas as AMBÍGUA e 2 a 3 dos 4 RUIM. No desafio, a v2.4-exp aprovou menos AMBÍGUA e menos RUIM na execução 2, mas à custa de BOA na execução 1.

## 4. Comparação pareada por item

**Corrigidos completos pela v2.4-exp (erro da v2.2 nas duas execuções, acerto da v2.4-exp nas duas):**

| Item | Estrato | Rótulo | Tensão | v2.2 | v2.4-exp |
|---|---|---|---|---|---|
| G1-D24 | desafio | AMBÍGUA | não | A, A | Rep, Rep |
| G1-D35 | desafio | RUIM | B | A, A | Rev, Rep |
| G1-F16 | fluxo | RUIM | B | A, A | Rev, Rev |

Corrigidos parciais (uma execução): G1-D11 (AMBÍGUA, fora de tensão), G1-D33 (RUIM, B), G1-F29 (BOA, A).

**Novos erros da v2.4-exp:**

| Item | Estrato | Rótulo | Tensão | v2.2 | v2.4-exp | Tipo |
|---|---|---|---|---|---|---|
| G1-D23 | desafio | AMBÍGUA | não | Rev, Rev | A, A | novo erro completo |
| G1-D30 | desafio | RUIM | B | Rev, Rev | A, Rev | parcial |
| G1-F03 | fluxo | RUIM | B | Rev, Rev | A, Rev | parcial |

**Perdas de BOA (todas registradas, mesmo em uma execução):**

| Item | Estrato | Tensão | v2.2 | v2.4-exp |
|---|---|---|---|---|
| G1-D03 | desafio | A | A, A | Rev, A |
| G1-D08 | desafio | não | Rev, A | Rep, A |
| G1-D13 | desafio | A | A, A | Rep, A |
| G1-D15 | desafio | A | Rev, A | **Rev, Rep (perda nas duas)** |
| G1-F01 | fluxo | A | A, A | Rep, A |
| G1-F07 | fluxo | não | A, A | Rev, A |
| G1-F29 | fluxo | A | A, Rev | A, A (ganho) |

A v2.2 perdeu BOA em 3 itens (D08, D15, F29), nenhum de forma consistente. A v2.4-exp perdeu em 6 itens, um deles (D15) nas duas execuções, e quatro dos seis são BOA de tensão tipo A (rótulo menos confiável, pois as previsões cegas anteciparam a revelação). Duas perdas (D08, F07) estão fora de tensão.

**Consistência entre as duas execuções da mesma versão:** v2.2 divergiu em 5 itens (D08, D10, D11, D15, F29). v2.4-exp divergiu em 11 itens (D03, D08, D11, D13, D15, D30, D33, D35, F01, F03, F07). A v2.4-exp ficou menos estável.

## 5. Dependência de itens contestáveis

| | Em tensão (17) | Fora de tensão (43) |
|---|---|---|
| RUIM aprovadas | v2.2: 8, 8. v2.4: 8, 5 | não se aplica (zero RUIM) |
| AMBÍGUA aprovadas | 0, 0, 0, 0 | v2.2: 13, 12. v2.4: 12, 12 |
| BOA não aprovadas | v2.2: 1, 1. v2.4: 4, 1 | v2.2: 1, 0. v2.4: 2, 0 |

Os ganhos de D35 e F16 estão em itens de tensão B. O ganho fora de tensão é um só item completo (D24) e um parcial (D11), contra um erro novo completo fora de tensão (D23) e duas perdas de BOA fora de tensão (D08, F07). O saldo fora das tensões é próximo de zero.

## 6. Aplicação do critério da emenda

Critério 1 (melhoria operacional com ressalvas) exigia, juntas, ganhos em mais de um item, ausência de piora grave ou sistemática, nenhuma perda consistente ou editorialmente relevante de BOA, ganhos não dependentes de itens contestáveis e consistência não pior.

- Ganhos em mais de um item no veredicto bruto: **sim** (D24, D35, F16).
- Perda consistente de BOA: **sim** (D15, Rev e Rep). Isso sozinho impede a conclusão 1 e bloqueia promoção automática.
- Ganhos independentes de itens contestáveis: **parcialmente** (D24 e D11 apenas).
- Consistência não pior: **não** (11 divergências contra 5).
- Piora grave (BOA reprovada nas duas execuções ou RUIM aprovado nas duas que a v2.2 não aprovava): **não ocorreu**. Por isso a conclusão 3 (piora observada) também não se sustenta: as perdas e os erros novos têm compensação parcial.

Resultado: **SUPERIORIDADE NÃO DEMONSTRADA**. Não é um achado de equivalência, e a sobreposição de resultados não prova equivalência. A v2.2 permanece como referência provisória para o próximo passo do laboratório, sem declaração de superioridade e sem homologação. A v2.4-exp não é promovida.

O que a v2.4-exp mostrou de útil: uma segunda execução mais rigorosa (5 RUIM aprovados em vez de 8) e a correção de D24, D35 e F16. O que não ficou demonstrado: que isso se mantém numa execução seguinte sem perder BOA.

## 7. O que nenhuma versão corrigiu

Em todas as quatro execuções são aprovados:
- 5 RUIM: G1-D04, G1-D31, G1-D32, G1-F22, G1-F26. Todos tiveram zero previsões que capturaram a revelação e perspectiva específica aceita pelo Crítico, ou seja, o Crítico leu a imprevisibilidade como mérito, e o rótulo externo leu como defeito.
- 11 AMBÍGUA: G1-D05, D07, D19, D20, D21, F06, F08, F10, F12, F14, F19.

Se a divergência está no Crítico ou no rótulo único do ChatGPT, os dados não decidem. É o ponto que só a auditoria humana independente, ainda pendente, resolve.

## 8. Simulação do gate (sem novas avaliações)

Primeira avaliação = execução 1 ou execução 2. Sinais S1 (3 itens), S2 (5 itens) e S3 (por avaliação) definidos antes dos resultados.

| Versão e ordem | Desenho | Aprovadas | RUIM aprov. | AMB aprov. | BOA aprov. | Erros evitados | BOA atrasadas | 2ª avaliações |
|---|---|---|---|---|---|---|---|---|
| v2.2, e1 primeiro | G1 uma avaliação | 52 | 8 | 13 | 31 | | | 0 |
| | G2 dupla aprovação | 50 | 8 | 12 | 30 | 1 (D11) | 1 (F29) | 52 |
| | G3 por sinais | 50 | 8 | 12 | 30 | 1 (D11) | 1 (F29) | 16 de 52 |
| v2.2, e2 primeiro | G1 | 52 | 8 | 12 | 32 | | | 0 |
| | G2 | 50 | 8 | 12 | 30 | 0 | 2 (D08, D15) | 52 |
| | G3 | 51 | 8 | 12 | 31 | 0 | 1 (D15) | 14 de 52 |
| v2.4, e1 primeiro | G1 | 47 | 8 | 12 | 27 | | | 0 |
| | G2 | 44 | 5 | 12 | 27 | 3 RUIM (D30, D33, F03) | 0 | 47 |
| | G3 | 44 | 5 | 12 | 27 | 3 RUIM | 0 | 22 de 47 |
| v2.4, e2 primeiro | G1 | 49 | 5 | 12 | 32 | | | 0 |
| | G2 | 44 | 5 | 12 | 27 | 0 | 5 (D03, D08, D13, F01, F07) | 49 |
| | G3 | 44 | 5 | 12 | 27 | 0 | 5 | 27 de 49 |

Leitura:
- **Erros que permanecem:** em qualquer desenho, os 5 RUIM persistentes e as 12 AMBÍGUA persistentes continuam aprovados. Na v2.2, os 8 RUIM aprovados permanecem nos três desenhos.
- **Aprovados indevidos sem nenhum sinal de risco:** v2.2, 16 dos 21 (e1); v2.4, 11 dos 20 (e1) e 7 dos 17 (e2). Ausência de alerta não é ausência de risco, e os sinais S1 a S3 cobrem pouco.
- **Dependência da ordem:** a v2.4-exp só protege quando a execução 1 vem primeiro (evita 3 RUIM sem atrasar BOA). Com a execução 2 primeiro, evita 0 e atrasa 5 BOA. Isso reflete a instabilidade da v2.4-exp e impede tratar o ganho do gate como estável.
- **Custo:** o Gate 3 aciona 27% a 31% de segundas avaliações na v2.2 e 47% a 55% na v2.4-exp. O Gate 2 aciona 100% e, nestes dados, nunca protege mais do que o Gate 3.
- **Melhor equilíbrio observado:** Gate 3 sobre a v2.2 (mesmo resultado do Gate 2 com cerca de um terço do custo, 1 BOA atrasada ou menos). Mas protege quase nada (0 a 1 erro evitado). **Nenhum desenho é homologado para publicação automática**, e a decisão sobre gate fica para depois deste relatório.

## 9. Riscos editoriais que permanecem

1. Aprovação de RUIM e AMBÍGUA pelas duas versões, correlacionada entre execuções: repetir a avaliação com o mesmo Crítico e as mesmas previsões não desfaz o erro.
2. Confusão entre imprevisibilidade e qualidade: os RUIM persistentes foram aprovados por terem revelação não prevista.
3. Referência única e de modelo: sem auditoria humana independente, não se sabe quais divergências são erro do Crítico e quais são erro do rótulo (tensões A e B).
4. Amostra concentrada (M01 em 36 de 60 itens, pequeno_vs_grande em 42 de 60), sem controles especiais e sem julgador de motivos.
5. Mesmo modelo gera e avalia; os itens candidatos têm uma só candidata por conceito.

## 10. Próximo passo recomendado

- **Núcleo de identidade:** pode ser formalizado, pois não depende da superioridade do Crítico.
- **Fase B visual:** concordar com seis histórias variadas com Visual Auditor, mas com aprovação editorial humana de cada texto antes de qualquer imagem e com apresentação prévia de custo real por geração, consumo estimado e política de retentativas. Nenhuma imagem foi gerada.
- **Autonomia:** não avançar. O que decide é a auditoria humana independente de um conjunto pequeno e dirigido: os 5 RUIM e 11 AMBÍGUA persistentes, as BOA em disputa (D15, D03, D13, F01, F29, D08, F07) e as tensões. Isso diz se o limite está no Crítico ou na referência.
- Não houve execução de v2.3-exp, julgador de motivos, controles especiais, imagens, Metricool, n8n, grade, fila ou publicações.
