# G2: logística, cegueira e lacres (revisão 2, 23/10/2026)

Revisão conforme as decisões de Eri de 23/10 (00h27). A primeira versão (commit 981fc3e) trazia um pacote de triagem com o FORA DO ENQUADRAMENTO e uma tarefa de prever rótulos. Eri a reprovou antes de qualquer uso; nunca foi enviada nem executada. O arquivo foi substituído nesta árvore e a versão antiga permanece no histórico do repositório.

## 1. Pacotes

- `pacotes/pacote_triagem.md|json` (preditores Claude): código opaco (T…), conceito fotográfico, NA FOTO e a instrução da tarefa de previsão, que é o texto de `prompts/preditor.md` sem nenhuma alteração. Nenhum FORA DO ENQUADRAMENTO. A tarefa é inferir o que um leitor comum acharia que o texto vai revelar, antes de conhecer a revelação.
- `pacotes/pacote_externa.md|json` (avaliação editorial pelo ChatGPT): código opaco (P…), conceito fotográfico, NA FOTO, FORA DO ENQUADRAMENTO e a referência editorial para o avaliador (`referencia_editorial_avaliador.md`, síntese autônoma do critério, sem menção a versões de Crítico, prompts, amostras ou autoria). Sem contexto anterior da série: nenhum texto anterior é incluído. Sem fonte, intenção, previsões, veredictos ou rótulos.
- `privado/mapa_codigos_opacos.json`: código opaco para código interno, por trilha. Derivação por hash, sem sorteio. Códigos e ordens diferem entre as trilhas.
- Arquivos que nunca entram em pacote: `mapa_privado.json`, `g2/privado/`, `geracao/`, `brutos/`, `manifesto_g1.json`, relatórios e auditorias, e tudo em `g2/lacrado/`. Quem recebe um pacote recebe só o caminho do pacote.
- `verificar_pacotes_g2.py` confere tudo isso e grava `verificacao_preparacao.json`.

## 2. Papel e independência

Os preditores Claude são ferramenta de triagem, não avaliadores independentes. Suas previsões não determinam nem corrigem o rótulo do ChatGPT. Os resultados da triagem e da avaliação externa permanecem ocultos um do outro até que ambos os registros estejam lacrados. O ChatGPT nunca recebe previsões; os preditores nunca recebem rótulos. O orquestrador vê os dois resultados ao recebê-los (inevitável neste ambiente) e não os confronta antes dos dois lacres.

## 3. Ordem

1. Três preditores independentes (um subagente cada) leem `pacote_triagem.md` e devolvem uma lista JSON (codigo, previsao, confianca). As saídas são gravadas sem edição em `g2/lacrado/triagem_run1.txt` a `triagem_run3.txt` com SHA-256, e commitadas e publicadas.
2. O pacote externo é entregue a Eri para classificação pelo ChatGPT. Aguarda-se o retorno, sem antecipar confronto.
3. Os rótulos recebidos são lacrados (seção 4).
4. Só depois dos dois lacres: organização da conferência humana (conflitos e amostra de controle de 20%, mínimo de 10), em pacote misturado, com classificação de Eri às cegas antes do confronto. Esta etapa depende de autorização e de uma definição de conflito de triagem a aprovar antes de os rótulos serem abertos.
5. Não se usam resultados parciais para modificar instrumentos, candidatos ou instruções. A G3 não é iniciada.

## 4. Lacre dos rótulos

1. No mesmo turno em que Eri trouxer os rótulos, grava-se o texto literal em `g2/lacrado/rotulos_externos_bruto.txt`, sem corrigir formatação nem decodificar.
2. Calcula-se o SHA-256, registra-se hora e origem, e faz-se commit e push antes de abrir o mapa de códigos ou de qualquer análise. O horário do push é a evidência externa de data.
3. Os rótulos não são copiados para `prompts/`, `calibracao/`, `lote/`, `referencia_editorial/` nem para a pasta de pacotes, e não vão a pacote de preditor, Crítico ou julgador.
4. Cada leitura entra em `registro_acessos_g1.jsonl`.
5. Rótulos lacrados não são reescritos; correção posterior é novo registro datado.
