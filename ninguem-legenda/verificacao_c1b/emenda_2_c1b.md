# Emenda 2: verificação limitada da candidata C1b

Data: 23/10/2026. Autorização expressa de Eri (23/10, 16:53, "Decisão sobre a C1b e autorização condicionada da verificação"), condicionada à incorporação e ao congelamento prévio das correções, que constam do protocolo anexo. Esta emenda é um documento separado. O protocolo original (M1, commit 3dd05e5) e a Emenda 1 (G3 reduzida) permanecem intactos, e nenhum arquivo do M1, da G1, da G2 ou da G3 é modificado. Esta emenda é registrada, publicada e verificada mecanicamente ANTES da produção de qualquer história e da primeira execução de Crítico.

## 1. Natureza

Verificação limitada, de ciclo único, entre o Crítico v2.2 (controle) e a candidata C1b, sobre doze histórias inéditas mais a regressão com as seis histórias já arbitradas, totalizando 72 avaliações (18 itens x 2 execuções x 2 versões). Não é G3, não homologa nada e não autoriza promoção automática da C1b em nenhum desfecho. Resultado possível inclui INCONCLUSIVO, que encerra a rodada. Não constitui validação editorial independente: a referência é de Eri (possivelmente conversada com ChatGPT) e todos os avaliadores são da mesma família de modelos que gera as histórias.

## 2. Texto normativo

O texto normativo da verificação é `pos_g3/intervencao/PROTOCOLO_VERIFICACAO_C1B.md`, incorporado a esta emenda por hash (seção 3). Ele define: material (cinco grupos), regressão, referência em duas etapas, execuções, medidas, regra de decisão e quatro desfechos, e limites. Decisões de Eri incorporadas:
1. AMBÍGUA e RUIM contam como itens frágeis, com ganhos apresentados separadamente por categoria; correções apenas em RUIM não demonstram resolução da fronteira BOA e AMBÍGUA.
2. 72 avaliações, com a v2.2 reexecutada nas seis conhecidas em condições equivalentes.
3. Papel narrativo dos números anotado nas seis conhecidas, sem reclassificação editorial (as decisões lacradas em d4399f4 permanecem).
4. INCONCLUSIVO encerra a rodada, sem ampliação automática, ajuste sucessivo ou novo experimento sem autorização expressa e pré-registro independente.
5. Perda de BOA definida por redução efetiva de aprovações entre as versões (a(C1b) menor que a(v2.2)), com oscilações, comparações individuais e perdas reais registradas separadamente, em execuções emparelhadas (mesmo pacote e ordem).
6. Salvaguarda interpretativa sem aprovação automática: múltiplas leituras legítimas não são defeito, mas a aprovação depende de E1 a E5 e da ausência de defeitos demonstrados.
7. Lote cego em duas etapas: primeiro as 12 inéditas, sem previsões, veredictos, grupos ou pistas; depois de lacradas, as seis conhecidas, apenas para anotar o papel dos números.

## 3. Documentos sob hash

Os hashes estão em `verificacao_c1b/lacre_emenda2.json` (gerado no commit que publica esta emenda e conferido por `verificacao_c1b/verificar_c1b.py`): este documento, o protocolo, a C1b, os dois diffs, a C1 anterior (histórico), o próprio script de verificação, o instrumento `instrumentos_g1/montar_pacotes.py`, a v2.2, o validador e o instrumento de hashes. Após a publicação, nenhum desses arquivos pode ser alterado. Mudança exige nova emenda.

## 4. Condições de execução

- Prompts: `prompts/critico_v2_2.md` (v2.2, sem alteração, conferido contra o M1) e `pos_g3/intervencao/critico_v2_2_c1b.md`. Mesmo modelo e configuração em todas as execuções, registrados depois a partir dos registros dos agentes.
- Produção das histórias: Criador existente (`prompts/criador.md`, sem alteração) em agentes novos e isolados, com a instrução de grupo (apenas a condição de produção, sem Críticos, rótulos, as seis conhecidas ou resultados). Pedidos e saídas guardados literalmente e lacrados. Previsões cegas: três por item, por agentes novos que veem somente foto e NA FOTO (`prompts/preditor.md`).
- Filtros determinísticos do pipeline (`filtros.py`) rodam sobre as 12, com resultado registrado. Histórias que falham em filtro duro continuam no lote e são relatadas, para não selecionar o material depois de ver resultados. Itens fora do protocolo (por exemplo, sem detalhe numérico em N ou D) são registrados, não substituídos.
- Pacotes de Crítico: 18 itens (12 inéditas + 6 conhecidas), campos `codigo, conceito_foto, na_foto, fora, previsoes_cegas, textos_anteriores` (lista vazia). Para as seis conhecidas, usam-se as três previsões lacradas da G2, como na G3. Execução 1: um pacote, usado pela v2.2 e pela C1b. Execução 2: outro pacote, com outros códigos e outra ordem. Códigos opacos, sem identificador, rótulo, origem, versão ou grupo.
- Cada execução, em agente novo e isolado, lê somente o prompt e o arquivo do pacote. Isolamento documental, não técnico. Saídas validadas por `validar_avaliacao.py` e guardadas literalmente.
- Falha técnica (formato inválido, truncamento): uma reexecução, com o mesmo prompt e o motivo registrado. Todas as execuções entram na análise. Nenhuma execução favorável é escolhida depois.

## 5. Sequência e lacres

1. Publicação desta emenda e verificação mecânica pré (`verificar_c1b.py`), antes de produzir qualquer história.
2. Produção das 12 histórias e das previsões; filtros; lacre dos pedidos e saídas de produção.
3. Etapa 1 do lote cego: pacote das 12 para Eri; sua classificação (BOA, AMBÍGUA, RUIM e papel do número); registro literal, SHA-256, commit e verificação do lacre.
4. Etapa 2: pacote separado das seis conhecidas para anotação do papel do número; registro e lacre.
5. Montagem dos pacotes de Crítico e lacre dos pacotes; só então, as quatro execuções. Saídas brutas lacradas antes de abrir o mapa de códigos e as classificações.
6. Abertura do mapa e análise por script pré-declarado; relatório por história (decisão de Eri, veredictos de ambas as versões nas duas execuções, diferenças entre execuções, ganhos, perdas e justificativas citadas), em listas, sem taxa global.
7. Decisão de Eri sobre o resultado. Nada é promovido ou implantado antes.

## 6. Proibições

- Nenhuma nova rodada, ajuste sucessivo do prompt ou ampliação automática da amostra, em nenhum desfecho.
- Nenhuma promoção automática da C1b, homologação ou alteração da v2.2 em `prompts/`.
- Nenhum recálculo da G3 com as novas decisões de Eri. Nenhum uso dos 60 itens da G1 como validação nova.
- Nenhuma imagem, compra de crédito, publicação, alteração de skills, n8n, fila, publicadas ou contador real. A grade operacional existente permanece intacta.
- Nenhuma apresentação de concordância entre modelos como validação independente.
- Menos aprovações, isoladamente, não é melhoria editorial.
