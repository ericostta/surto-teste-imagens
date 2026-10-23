# Assinatura e numeração (regras PROVISÓRIAS do piloto v0.1)

Nada aqui está homologado. Posição, tamanho e hierarquia dos elementos são proposta visual para avaliação de Eri.

## Elementos (decisões conceituais recuperadas)
- Formato 1080 x 1920, 9:16.
- Topo: O QUE NINGUÉM LEGENDA com o número público da edição.
- Blocos NA FOTO e FORA DO ENQUADRAMENTO.
- Assinatura inferior: apenas @surtodelucidez (a forma extensa "SURTO DE LUCIDEZ @surtodelucidez" é de uma versão anterior do DNA).
- Elementos discretos, em posições consistentes entre edições, respeitando as margens de segurança da interface do Instagram.
- As zonas de segurança usadas (cerca de 250 px no topo e 340 px embaixo) são valores provisórios e precisam de verificação.

## Numeração
- Exclusiva da série: 001, 002, 003...
- Durante o desenvolvimento, peças de teste usam identificadores de laboratório (LAB-001, LAB-002...) e nunca um número público.
- Um número público é RESERVADO ANTES da composição da peça real e só é CONSUMIDO depois que Eri confirmar que a publicação manual aconteceu. Falha, cancelamento, descarte, revisão, teste e simulação não consomem número. Se houver falha, o número reservado é liberado e pode ser reutilizado.
- Um número CONFIRMADO nunca é reutilizado nem reatribuído.
- O piloto NÃO altera nem aciona o contador real do sistema de publicação. O controle do piloto é um arquivo CSV (assets/registro_piloto_modelo.csv) operado por `scripts/registro_numeracao.py`, que recusa o registro.csv do laboratório.

## Estados do registro do piloto
Estados canônicos do registro: RASCUNHO, TEXTO_APROVADO, FOTO_APROVADA, ARTE_APROVADA, RESERVADO, PUBLICADO, LIBERADO, DESCARTADO.
Estados legados lidos como equivalentes: ARTE_VALIDADA->ARTE_APROVADA, NA_FILA->ARTE_APROVADA, PUBLICADA->PUBLICADO, TEXTO_REPROVADO->DESCARTADO.
Estados que entram no controle de similaridade, repetição e diversidade: TEXTO_APROVADO, FOTO_APROVADA, ARTE_APROVADA, RESERVADO, PUBLICADO, LIBERADO.
- Estado desconhecido não é ignorado: conta por precaução e gera aviso.
- Registros legados são lidos, nunca reescritos. A skill só escreve no registro do piloto, por comando explícito.

## Procedimento
1. `python3 scripts/registro_numeracao.py reservar --registro registro_piloto.csv --id LAB-003` (história aprovada recebe o menor número livre e passa a RESERVADO).
2. Composição com `--registro registro_piloto.csv --id LAB-003 --numero 004`: o script só compõe se o número estiver RESERVADO para aquela história. Peças LAB- dispensam reserva.
3. Só depois de Eri dizer que publicou: `confirmar --id LAB-003` (RESERVADO passa a PUBLICADO, número consumido, e fica também no arquivo `.confirmados.jsonl`).
4. Falha ou cancelamento: `liberar --id LAB-003 --motivo "..."`.
5. `verificar` detecta duplicidade, número sem história e número confirmado alterado, removido ou reutilizado.
- Sem registro anexado por Eri, use apenas LAB-.
