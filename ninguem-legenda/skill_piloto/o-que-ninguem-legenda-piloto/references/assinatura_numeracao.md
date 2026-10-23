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
- Um número público pode ser RESERVADO ao preparar a peça real, mas só é CONSUMIDO depois que Eri confirmar que a publicação aconteceu. Falha, cancelamento, descarte, revisão, teste e simulação não consomem número. Se houver falha, o número pode ser reutilizado.
- O piloto NÃO altera nem aciona o contador real do sistema de publicação. O controle do piloto é o registro manual (assets/registro_piloto_modelo.csv): colunas id, numero (vazio até a confirmação), estado e status_publicacao.
- Proposta de estados do registro manual: RASCUNHO, TEXTO_APROVADO, FOTO_APROVADA, ARTE_APROVADA, RESERVADO (número reservado), PUBLICADO (confirmado por Eri; só aqui o número é consumido), LIBERADO (falha comprovada; número reutilizável), DESCARTADO.
- Antes de reservar um número, confira no registro anexado por Eri o último PUBLICADO e evite duplicidade. Se não houver registro anexado, peça-o ou use apenas LAB-.
