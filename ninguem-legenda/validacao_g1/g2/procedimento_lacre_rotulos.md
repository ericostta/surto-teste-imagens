# G2: logística documental e lacre dos rótulos (preparada, não executada)

Data: 23/10/2026. Autorizado por Eri (00h21, decisão 5) apenas como preparação. Nenhum pacote foi enviado, nenhum subagente de triagem foi executado, nenhum Crítico ou julgador foi executado, nenhuma classificação existe.

## 1. O que está preparado

- `pacotes/pacote_externa.md|json`: 60 itens para o avaliador externo, códigos iniciados por P.
- `pacotes/pacote_triagem.md|json`: os mesmos 60 itens, códigos iniciados por T e ordem diferente, para os subagentes de triagem. A instrução de triagem está no cabeçalho do pacote (instrumento novo, ainda não executado, a aprovar por Eri antes do uso).
- `privado/mapa_codigos_opacos.json`: código opaco para código interno, por trilha. Derivação determinística (hash do conjunto congelado mais código interno), sem frase-semente e sem sorteio. Qualquer pessoa reproduz com `gerar_pacotes_g2.py`.
- `../mapa_privado.json`: procedência, ordem de produção, conceito sorteado e célula de intenção. Continua fora de qualquer pacote.
- `pacotes/hashes_pacotes.json`: SHA-256 dos quatro arquivos de pacote.

Cada pacote contém só `codigo`, `foto` (conceito fotográfico), `na_foto` e `fora`. Não contém código interno, amostra, ordem de produção, conceito sorteado, célula, ambiente, versão de Crítico, rótulo ou resultado. `verificar_pacotes_g2.py` confere isso (60 itens, códigos únicos, campos, termos proibidos, ordens diferentes entre trilhas, itens e hashes do manifesto G1 inalterados).

## 2. Arquivos que nunca entram em pacote nem são entregues a avaliadores, preditores, Críticos ou julgadores

`mapa_privado.json`, `g2/privado/`, `geracao/`, `brutos/`, `manifesto_g1.json`, `RELATORIO_G1.md`, `auditoria_duplicatas_g1.md`, `representatividade_fluxo_g1.md`, e tudo que for criado em `g2/lacrado/`. Quem receber um pacote recebe somente o caminho do arquivo do pacote.

## 3. Ordem obrigatória na execução da G2 (a autorizar por Eri)

1. Triagem: os subagentes leem `pacote_triagem` e devolvem previsões; as previsões são gravadas sem edição em `g2/lacrado/triagem_bruta.*`, com SHA-256, e commitadas e publicadas antes de qualquer rótulo existir.
2. Avaliação externa: Eri leva `pacote_externa.md` ao avaliador externo.
3. Lacre dos rótulos (seção 4).
4. Decodificação pelo mapa privado e cálculo dos conflitos de triagem.
5. Pacote humano misturado (conflitos mais 20% dos sem conflito, mínimo de 10, selecionado conforme o procedimento já aprovado), classificado por Eri sem rótulos nem previsões; só depois o confronto.
6. Só então a G3.

## 4. Lacre dos rótulos

1. No mesmo turno em que Eri trouxer os rótulos, o orquestrador grava o texto recebido, literal, em `g2/lacrado/rotulos_externos_bruto.txt`, sem corrigir formatação nem decodificar.
2. Calcula o SHA-256 do arquivo, registra a hora e a origem, e faz commit e push antes de abrir o mapa de códigos ou de qualquer análise. O horário do push no repositório é a evidência externa de data.
3. Os rótulos nunca são copiados para `prompts/`, `calibracao/`, `lote/`, `referencia_editorial/` nem para a pasta de pacotes, e não vão em pacote de Crítico, preditor ou julgador. Julgador e auditoria recebem a referência por pacote próprio, só na G3.
4. Cada leitura dos rótulos entra em `registro_acessos_g1.jsonl` (quem, quando, passo).
5. Exposição inevitável, já declarada: o orquestrador vê os rótulos ao recebê-los, porque Eri os cola no chat. Isso não alimenta o desenvolvimento, pois a candidata, os controles, os instrumentos e o protocolo estão congelados no M1.
6. Rótulos lacrados não são reescritos. Discordância ou correção posterior entra como novo registro, com data, sem apagar o original.

## 5. Verificação de que nada futuro está disponível antes

Na preparação não existem rótulos, previsões, avaliações nem resultados em nenhuma pasta. Os pacotes foram gerados do manifesto G1 e não leem nada além dos três campos de cada item. Os rótulos e resultados futuros só passam a existir depois dos passos 1 a 3 da seção 3, e `g2/lacrado/` não é lido por nenhum gerador de pacote.
