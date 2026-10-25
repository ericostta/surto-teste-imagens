# Auditoria da fotografia v3 de L8CFD (ChatGPT, segunda tentativa de correção) e composição B

Data: 24/10/2026. Aplicação do padrão PROPOSTO (ainda não aprovado nem incorporado à skill). Foto preservada: `foto_real_L8CFD_chatgpt_v3_original.png` (SHA-256 889d3b4cd69e8f59b1fa397c60d4211552a3c16754ac6a2df8602b7761f3dbce). Fora do material de avaliação cega. Nada publicado, nenhum número real consumido, skill intacta.

Histórico: imagem original (Gemini, 572 x 1024), correção 1 (ChatGPT v2), correção 2 (esta). Pelo limite proposto, a skill para aqui e entrega diagnóstico para decisão humana.

## Etapa 1: fotografia
Arquivo PNG 941 x 1672, 2.168.863 bytes, proporção 0,5628, ampliação 1,148x. Faixa de atenção do critério I6 (810 a 1079 px), sem artefato de compressão visível.

| Critério | Constatação | Veredito |
|---|---|---|
| I4, I5 | guarda-chuva aberto secando em corredor; sem pessoa, etiqueta, nome ou segundo objeto | Passa |
| Realismo de materiais | gotas no tecido e na borda, parede rugosa com respingos, poça pequena com anéis em volta do cabo, gota se desprendendo da ponta do cabo, reflexos suaves no piso | Passa |
| Linguagem documental | muito mais natural que a v2: luz plana, sem contraste dramático, sem janela estourada, piso apenas brilhante | Melhorou, passa |
| **I1 sustentação** | **A haste inclina 12,4 graus com o topo para a esquerda, e a copa encosta na parede da direita (ver `AUDITORIA_v3_inclinacao.png`). O topo está longe da parede que supostamente sustenta o objeto, e a parede só pode empurrar: sem equilíbrio, o guarda-chuva tombaria para a esquerda. O prompt pedia a inclinação para a parede e o gerador fez o contrário, de modo mais acentuado que na v2 (8,1 graus).** | **Defeito provável, impeditivo para APTA** |
| I9 composição pedida | guarda-chuva na metade superior (copa de 8% a 34%, cabo toca o piso a 49% da altura), 50% inferiores só piso calmo: **cumprido**, salvo a copa começar a 8% e não a 18% | Quase cumprido |
| I9 câmera | câmera ao nível do piso, não na altura do peito | Desvio, sem prejuízo narrativo |

Limite do achado I1: baseia-se na geometria do plano da imagem; inclinação em profundidade não aparece e não posso excluí-la. Se o seu olho não percebe a anomalia, aceitar é decisão sua.

**Decisão da skill (proposta): AJUSTAR.**

## Etapa 2: arte no perfil B (LAB-001, simulação)
Arquivos: `LAB-001_B_foto_v3.png` e `_guias.png`. Aprovação técnica do script: SIM (texto cabe, zonas 250/340 px respeitadas, texto não alterado). Aprovação visual: pendente de Eri.

Contraste do branco sobre o fundo sem texto (limiares provisórios):

| Elemento | Média | Pior decil | Resultado |
|---|---|---|---|
| Título | 7,1:1 | 2,7:1 | média passa; trecho sobre a janela e a borda da copa é o mais fraco |
| Número LAB-001 | 19,4:1 | 19,2:1 | passa |
| NA FOTO | 4,2:1 | 1,9:1 | média ligeiramente abaixo de 4,5:1; o rótulo "NA FOTO" fica lavado sobre uma faixa brilhante do piso |
| FORA | 10,3:1 | 7,9:1 | passa |
| Assinatura | 10,5:1 | 9,6:1 | passa |

Sobreposição com o elemento central: NA FOTO e FORA ficam inteiros sobre piso calmo, sem cruzar a haste nem o cabo (melhora decisiva em relação à v2). Título e número agora cruzam a copa e a janela ao fundo. O contato do cabo com o piso fica logo acima do rótulo NA FOTO, sem encostar. (A faixa vermelha de simulação cobre parte da copa, e isso é só da simulação.)

**Decisão da skill (proposta): AJUSTAR** na arte, por contraste do rótulo NA FOTO e do título em trechos, e por título e número sobre a copa. A hierarquia entre foto e revelação funciona bem.

## Diagnóstico e opções para sua decisão
O padrão proposto manda parar após duas correções e perguntar: continuar, substituir a fotografia ou interromper.

1. **Aceitar a v3 como está**, se o seu olho tolerar a inclinação. É a melhor foto até agora em composição, naturalidade e uso do espaço do texto. Os ajustes de arte (rótulo e título) ficariam para decidir depois.
2. **Autorizar uma terceira correção**, excedendo o limite proposto, por edição da própria v3 pedindo apenas a inclinação da haste para a parede e preservando o resto. Risco: o gerador já ignorou esse pedido duas vezes.
3. **Mudar o arranjo físico da cena**, mantendo NA FOTO e FORA: por exemplo, o guarda-chuva aberto deitado de lado no piso, que é estável e comum, ou em pé sobre o cabo sem apoio na parede, com a haste vertical. Muda o conceito fotográfico e exige sua aprovação.
4. Interromper ou substituir a fotografia.

Minha recomendação: opção 2, com a edição pedida em uma frase curta, porque a composição já está certa e só a inclinação falha. Se falhar de novo, opção 3.
