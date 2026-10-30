# Auditoria da foto v12 (ChatGPT), 30/10/2026

Arquivo: foto_real_L8CFD_chatgpt_v12.png, 941 x 1672 (9:16 ok), SHA-256 fe0b6e97fc05f8ff649c5f7b843060a1ce00fb2f09eebda14388b6806b02442b. Resolução abaixo de 1080 x 1920 (aviso conhecido).

## Composição (I8): melhora clara
Guarda-chuva menor e alto no quadro (aproximadamente 18% a 50% da altura), terço inferior de piso liso. Não cruza os blocos NA FOTO e FORA.
Contraste efetivo (medir_contraste.py, layout com número no topo; ignorar o campo "numero"): título média 7,58 e pior decil 2,43 (limite provisório 3,0); rótulos NA FOTO e FORA média 4,94 e 5,06, pior decil 3,3; texto NA FOTO média 5,73 e pior decil 2,55 (limite 3,0); texto FORA 12,75 e 10,62; assinatura 6,57. Dois pontos abaixo do limite provisório no pior decil (título e texto NA FOTO), ambos sobre parede com reflexos claros.

## Suporte físico (I1): dúvida relevante
Ajuste de reta nos pixels escuros da haste (linhas 600 a 790): inclinação de 25,0 graus com o TOPO DA HASTE AFASTADO da parede (ponteira junto ao rodapé). A borda da copa toca a parede. Estaticamente, a parede só empurra para longe dela; com a ponteira mais próxima da parede que o topo da haste e o centro da copa à direita da ponteira, o conjunto tende a cair para longe da parede. É a configuração "escada invertida". Nas versões anteriores, inclinação com o topo afastado já havia sido tratada como defeito I1 (v7 a v9, cerca de 10 graus); v4 (7,4 graus em direção à parede) não tinha esse problema.
Correção de registro: a descrição da v11 como "cabo inclinado em direção à parede" estava errada. Pela imagem, a v11 apresenta o mesmo padrão (topo da haste afastado da parede). A v11 não foi medida por ajuste de reta.
Resultado provisório da v12: AJUSTAR (física), composição adequada. Decisão visual e editorial é de Eri.

## Correção de 30/10/2026 (medição)
Os valores de contraste desta auditoria foram medidos com os parâmetros do perfil B (rótulos em alfa 170, degradê do topo mais leve), e não com o layout de teste B215/C. Medidos pelo compor_story.py da v0.2 no perfil C, os valores são mais altos. Ver ENTREGA_PILOTO_V02.md.
