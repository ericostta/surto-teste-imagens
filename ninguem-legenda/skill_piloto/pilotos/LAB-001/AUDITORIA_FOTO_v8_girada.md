# Auditoria da foto v8 girada (rotação do guarda-chuva) de L8CFD

Data: 24/10/2026. Origem: `foto_real_L8CFD_chatgpt_v8_original.png` (sha256 3c5f4074c56003cd2f90f5dc1ac6601e3fb0e57a2c9d4f9a04d18f033a29dd49), preservada. Resultado: `foto_real_L8CFD_chatgpt_v8_girada.png` (sha256 f452fb53e06cd9f03d8f36aa3d0d15c0d39bf68434d7304227ef8cda9bcf11de). Script: `girar_guarda_chuva.py SAIDA 17.7` (autorizado por Eri). Nada publicado.

## O que foi feito (divulgação obrigatória)
Giro rígido de 17,7 graus no sentido horário do guarda-chuva inteiro em torno do cubo da copa; cabo e poça acompanham o objeto (novo pé em torno de x 449, y 832). O fundo descoberto foi RECONSTRUÍDO: pequenas partes copiadas de v6 (abaixo da copa) e o restante por inpaint suavizado com grão. É uma edição estrutural com muitos pixels inventados (porta, janela e fim do corredor atrás da copa antiga, parede ao lado da borda).

## Medição
- Haste: inclinação de 8,1 graus com o topo PARA A PAREDE (medida por ajuste de reta nos centros da faixa escura, y 520 a 680). Antes: 9,7 graus para longe. I1 corrigido.
- Copa e haste continuam coerentes (giro rígido).

## Defeitos residuais (I3, artefatos)
- Janela e porta à esquerda da copa: borrão em forma de bolha, perda das bordas do batente.
- Abaixo da borda da copa, entre a porta e a haste: neblina lisa e pequenos fragmentos claros.
- Parede ao lado da borda direita: trecho liso sem a textura do reboco.
Visíveis em Story. Pelo padrão proposto, a foto NÃO é APTA enquanto esses artefatos existirem; a decisão final é de Eri.

## Conclusão
A rotação corrige a física, mas o fundo atrás da copa antiga não existe em nenhuma versão (v6, v7 e v8 o escondem), então não há como reconstruí-lo de forma fotograficamente convincente só com recursos locais. Caminhos: refazer o fundo em outro gerador, ou nova cena sem esse problema.
