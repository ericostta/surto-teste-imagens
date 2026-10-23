# Crítico v2.2 experimental: alterações documentadas

Data: 22/10/2026. Fase A. Experimental, não homologada. Autorização: decisões de Eri de 22/10/2026 (retirada da previsibilidade como gatilho; preservação do núcleo narrativo; informação implícita não é defeito automático; v2.1 preservada).

## Arquivos

| Arquivo | Situação |
|---|---|
| prompts/critico.md | INALTERADO (v2.1, SHA-256 9910c786...2c15) |
| prompts/critico_v2_1.md | cópia idêntica da v2.1, só para nomear a versão |
| prompts/critico_v2_2.md | NOVO (v2.2 experimental) |
| validar_avaliacao.py | modo v2.2 acrescentado; modo v2.1 idêntico (revalidei 43 avaliações anteriores com o mesmo resultado) |
| calibracao/v2_2/teste_validador.py | NOVO, 12 testes sintéticos do modo v2.2, todos passando |
| prompts/criador.md | acrescentada uma seção "Revisão sob o Crítico v2.2"; o texto anterior não mudou |
| config.json | chaves novas (revisao.criterio_v2_2_experimental, critico_experimental); versao_critico continua "v2.1" |
| filtros.py, taxonomia.json, registro.csv, Auditor Lógico, gabaritos, relatórios anteriores | INALTERADOS |

O diff completo do prompt está em alteracoes_prompt_critico.diff.

## Mudanças no Crítico

1. Previsão cega: de condição (E2 antiga, "2 ou 3 leitores capturaram, máximo REVISAR") para evidência auxiliar. Não gera REVISAR nem REPROVADA sozinha. Só entra como prova dentro de um defeito da lista (cliché efetivo ou redundância).
2. Nova E2: plausibilidade e naturalidade humana (a decisão pede plausibilidade no ramo A).
3. REVISAR e REPROVADA exigem defeito demonstrado de lista fechada, com categoria, trecho citado, demonstração e gravidade (corrigível ou estrutural). Defeito hipotético apresentado como fato não vale. "Previsibilidade" não é categoria.
4. Informação implícita não é defeito automático: só vira defeito se o Crítico demonstrar com o texto que a omissão compromete compreensão, plausibilidade ou coerência. Omissões legítimas vão em observacoes_descartadas, com o motivo.
5. Seis distinções obrigatórias: familiaridade e clichê, imprevisibilidade e originalidade, omissão e obscuridade, sofisticação e profundidade, complexidade e qualidade, sentimentalismo e sensibilidade.
6. Instrução de revisão: "Defeito:", "Mudar:" (pontual, na formulação do FORA ou em elemento visual dispensável) e "NÃO pode mudar:" (sempre o núcleo narrativo e o acontecimento central). Proibido trocar o acontecimento central ou inventar outra revelação. Se isso for preciso, vira REPROVADA e, se retomada, nova candidata.
7. Mantidos da v2.1: T2 a T10 (T1 passa a ser auxiliar), E1, E3, E4, E5, lista de reprovação estrutural, regra contra flexibilização, as três previsões cegas como entrada.

## O que NÃO foi alterado de propósito

O teste de originalidade (T10 e E5) continua obrigatório para aprovar. Cliché efetivo, obviedade sem transformação, redundância e falta de originalidade seguem como defeitos legítimos. A v2.2 só retira um motivo de REVISAR, não afrouxa nenhum requisito de aprovação.

## Validador

No modo v2.2: APROVADA exige E1 a E5, nenhum defeito demonstrado e nenhuma eliminatória; REVISAR exige defeitos todos corrigíveis, cada um com categoria válida, trecho e demonstração, e instrução com "Defeito", "Mudar", "NÃO pode mudar" e menção ao núcleo ou ao acontecimento central; REPROVADA exige defeito estrutural ou eliminatória; qualquer categoria de previsibilidade é inválida; linguagem hipotética na demonstração gera aviso. O validador não mede qualidade, só coerência interna.

## Casos históricos

Servem apenas como diagnóstico e não são usados como prova de melhoria. Posições de Eri registradas: J15 original no caminho A; J01 original BOA (defeito do caminho B não comprovado); J06 encerrada; J08 no caminho A. Os registros históricos não foram alterados.
