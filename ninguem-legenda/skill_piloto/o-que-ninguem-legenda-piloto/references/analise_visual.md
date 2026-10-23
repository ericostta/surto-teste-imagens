# Análise visual da fotografia gerada (piloto v0.1)

Entrada: imagem anexada por Eri, mais a história aprovada (NA FOTO, FORA, conceito_foto). Abra a imagem de fato (Read com o caminho do arquivo anexado) e rode `python3 scripts/analisar_foto.py FOTO.png`, que mede dimensões, proporção e luminância por zona. Os números ajudam, o julgamento é da leitura da imagem.

## Checagens
1. Fidelidade ao NA FOTO e ao conceito_foto: o sujeito principal, o estado, a posição e o ambiente conferem? Registre o que falta ou sobra.
2. Não antecipa a revelação: a imagem contém algo que só faz sentido depois do FORA (segundo objeto simbólico, etiqueta, nome, vínculo, pista de quem/porquê)? Isso é defeito, ainda que a foto seja bonita. A foto NÃO precisa mostrar o que está fora do enquadramento.
3. Realismo documental: parece fotografia real? Sinais de IA: mãos e dedos, simetrias impossíveis, texturas cerosas, reflexos incoerentes, objetos que se fundem, sombras sem fonte, brilho publicitário.
4. Texto e marcas: letras, números, logotipos ou marcas-d'água legíveis ou pseudo-legíveis. Qualquer um é defeito.
5. Pessoas e rosto: o padrão é sem rosto. Rosto ou figura humana não prevista é defeito.
6. Formato: 9:16. Se a proporção for outra, diga como será cortado e se perde o sujeito. Resolução mínima desejável 1080 x 1920.
7. Composição para o texto: a parte inferior (onde ficam os blocos de texto e a assinatura) é calma o bastante? O sujeito escapa da área coberta pela interface (cerca de 13% no topo e 20% embaixo, valores provisórios)? A luminância média da faixa dos blocos permite legibilidade com o degradê do layout? Se não, proponha corte, deslocamento ou nova geração.
8. Protagonismo: a foto sustenta a peça sozinha, sem o texto?

## Resultado
- APTA: pode ir para a composição.
- AJUSTAR: dá para corrigir com corte ou ajuste leve; diga qual.
- REFAZER: nova geração, com a correção do prompt (máximo de 2 gerações por história no piloto).
Liste defeitos com o que se vê, onde e a gravidade. Seja específica e curta. Nunca declare a foto "aprovada para publicação": aprovação visual é de Eri.
