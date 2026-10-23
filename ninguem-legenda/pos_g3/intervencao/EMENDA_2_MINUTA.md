# Emenda 2 (MINUTA): verificação limitada da candidata C1b

Estado: MINUTA de 23/10/2026. Não executada, não homologada, não publicada como emenda em vigor. Só vira emenda com autorização expressa de Eri, e só será registrada e verificada mecanicamente ANTES de qualquer produção de história ou execução de Crítico, no mesmo padrão da Emenda 1 (`validacao_g1/g3_reduzida/emenda_g3_reduzida.md`). O protocolo original (M1, commit 3dd05e5) e a Emenda 1 permanecem intactos.

## 1. Natureza

Verificação limitada, de ciclo único, entre o Crítico v2.2 (controle) e a candidata C1b (corrigida após a devolutiva técnica), sobre doze histórias inéditas mais a regressão com as seis histórias arbitradas, totalizando 72 avaliações. Não é G3, não homologa nada e não autoriza promoção automática. Resultado possível inclui INCONCLUSIVO. Não constitui validação editorial independente.

## 2. Diferenças em relação às emendas anteriores

1. Material novo: doze histórias inéditas produzidas para esta verificação. Os 60 itens da G1 não são reutilizados como validação nova.
2. A v2.2 é reexecutada nas mesmas condições da C1b (mesmos pacotes e previsões), em vez de usar a G3 como baseline.
3. Referência única: a classificação cega de Eri, com anotação do papel do detalhe numérico. Não se usam rótulos do ChatGPT como gabarito.
4. Quatro desfechos, incluindo INCONCLUSIVO distinto de evidência negativa (protocolo, seção 7).
5. Proteção explícita de histórias cujo significado depende de número, idade ou quantidade.

## 3. Documentos e hashes (a recalcular e conferir na publicação)

| Documento | SHA-256 no momento da minuta |
|---|---|
| prompts/critico_v2_2.md (controle, congelado) | 468fd3823f83909dd87127d7a4affd835df4be09c7601e62c37b38dc54b553a3 |
| validar_avaliacao.py (congelado) | 04a0183bc93598ed72e41ea7a1294cbb1db8d0b92bf175dbe8c65442e4c487f1 |
| pos_g3/intervencao/critico_v2_2_c1b.md (candidata) | a1b5b47ef79ea9f2252d57cd80074ff570828090e578a01aae24d02f683e5d32 |
| pos_g3/intervencao/diff_c1_para_c1b.diff | 3f447102b1036a50c41e0c2df5f83f1c124c8cc3768b1c893ec67679a26ff6ac |
| pos_g3/intervencao/diff_v2_2_para_c1b.diff | 20dbc961425b8a2a2542dcbbc998417a02bf05dc80a705e29afbbb5388d73a35 |
| pos_g3/intervencao/PROTOCOLO_VERIFICACAO_C1B.md | a registrar na publicação |
| critico_v2_2_c1.md (C1 anterior, substituída, preservada como histórico) | af123add988cf6e69b593b0775f1a46a11112433e187aa97a331d27791835a89 |

Após a publicação, nenhum desses arquivos pode ser alterado. Mudança exige nova emenda.

## 4. Entradas e condições

Conforme `PROTOCOLO_VERIFICACAO_C1B.md`, seções 2, 3 e 5: cinco grupos (3 N, 3 D, 2 M, 2 A, 2 P); previsões cegas frescas; pacote de 18 itens; códigos e ordem embaralhados por execução; duas execuções por versão em agentes novos e isolados; validador congelado; saídas literais lacradas antes de abrir classificações e mapa; uma reexecução por parte em falha técnica; nenhuma execução escolhida depois. O isolamento é documental e o avaliador é da mesma família de modelos que produziu as histórias (limitação declarada).

## 5. Referência

Classificação cega de Eri (BOA, AMBÍGUA, RUIM) e papel do detalhe numérico (FUNCIONAL, DECORATIVO, SEM DETALHE NUMÉRICO), registrada literalmente e lacrada com SHA-256 antes de qualquer execução de Crítico, com nota de natureza. Mapa de códigos privado até o lacre. As decisões já tomadas por Eri sobre as seis histórias da regressão valem como estão; a anotação do papel numérico delas é opcional.

## 6. Medidas, regra de decisão e desfechos

Os do protocolo, seções 6 e 7, que ficam incorporadas a esta emenda por referência de hash: frágil, oportunidade, corrigido, perda de BOA, proteção numérica testável; condições C-a a C-d; desfechos BENEFÍCIO CLARO, PIORA OBSERVADA, SEM BENEFÍCIO e INCONCLUSIVO, avaliados nesta ordem: falha técnica, piora, testabilidade, ausência de benefício, benefício.

## 7. Proibições

- Nenhuma nova rodada, nenhum ajuste sucessivo do prompt, nenhuma ampliação automática da amostra, em nenhum desfecho.
- Nenhuma promoção automática da C1b, nenhuma homologação, nenhuma alteração da v2.2 em `prompts/`.
- Nenhum recálculo da G3 com as novas decisões de Eri. Nenhum uso dos 60 itens da G1 como validação nova.
- Nenhuma imagem, crédito, n8n, grade, fila, publicadas, skills, contador real ou publicação.
- Nenhuma apresentação de concordância entre modelos como validação independente.

## 8. Sequência e lacres

1. Publicação desta emenda e verificação mecânica de hashes (script de verificação a escrever e congelar antes, no padrão de `verificar_g3.py`; ainda não existe).
2. Produção das doze histórias e das previsões; lacre dos pedidos de produção e dos textos.
3. Pacote cego para Eri; classificação; registro literal e lacre.
4. Execuções e lacre das saídas brutas.
5. Abertura do mapa e análise por script pré-declarado; relatório com listas de itens.
6. Decisão de Eri sobre o resultado. A emenda não decide nada sozinha.

## 9. Pendências de decisão de Eri antes de publicar

1. Contar RUIM, além de AMBÍGUA, como item frágil (proposto). Se não, só AMBÍGUA conta e RUIM aprovado é apenas relatado.
2. Aceitar 72 avaliações (v2.2 também sobre as seis) em vez de 60 (proposto, por comparação em condições idênticas).
3. Anotar ou não o papel do número nas seis da regressão (opcional; sem a anotação, a proteção numérica depende só das inéditas).
4. Confirmar que INCONCLUSIVO encerra a rodada sem ampliar a amostra, e que qualquer material novo exige nova autorização e novo pré-registro.
