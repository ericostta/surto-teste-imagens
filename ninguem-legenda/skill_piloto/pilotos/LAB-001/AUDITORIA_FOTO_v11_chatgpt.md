# Auditoria da foto v11 (ChatGPT), 30/10/2026

Arquivo: foto_real_L8CFD_chatgpt_v11.png, 941 x 1672, proporção 0,5628 (9:16 ok), SHA-256 d37c6619e2259e32d0504ea8de5eec1000a9508c62983d1f1d224c06c354c880. Resolução abaixo de 1080 x 1920 (aviso já conhecido, mesma das versões anteriores).

## Suporte físico (I1): atende
Guarda-chuva aberto inclinado, com a borda da copa encostada na parede à esquerda e a ponteira do cabo no piso, dentro de uma poça. A parede sustenta o objeto e o cabo inclina em direção a ela. Resolve a objeção de Eri à v10 (guarda-chuva em pé sem apoio). Aprovação visual e editorial da foto continua com Eri.

## Composição e legibilidade (I8): NÃO atende no layout atual
O guarda-chuva ocupa a faixa central e baixa do quadro, onde ficam os blocos de texto: a copa e o cabo atravessam NA FOTO e FORA DO ENQUADRAMENTO. Contraste efetivo medido (script medir_contraste.py, perfil de rótulos da composição de teste; o campo "numero" dessa medição refere-se ao layout antigo e deve ser ignorado):
- título: média 5,05, pior decil 2,22 (limite provisório 3,0);
- rótulo NA FOTO: média 3,69 (limite 4,5), pior decil 1,97;
- texto NA FOTO: média 5,23, pior decil 1,57 (limite 3,0);
- rótulo FORA: média 3,77, pior decil 2,58;
- texto FORA: média 12,07, pior decil 7,15 (ok);
- assinatura: média 6,94 (ok).
Resultado provisório: AJUSTAR (REFAZER a composição, não a física). Os limiares são provisórios e não homologados.

## Recomendação
Pedir ao gerador o mesmo arranjo físico com o guarda-chuva menor e mais alto no quadro, deixando livre o terço inferior (piso liso) e o topo sem elementos claros demais.

## Correção de 30/10/2026 (medição)
Os valores de contraste desta auditoria foram medidos com os parâmetros do perfil B (rótulos em alfa 170, degradê do topo mais leve), e não com o layout de teste B215/C. Medidos pelo compor_story.py da v0.2 no perfil C, os valores são mais altos. Ver ENTREGA_PILOTO_V02.md.
