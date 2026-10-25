# Auditoria da fotografia v2 de L8CFD (gerada no ChatGPT) e composição B

Data: 24/10/2026. Aplicação do padrão PROPOSTO em `PROPOSTA_PADRAO_EXCELENCIA_FOTOGRAFICA.md` (ainda não aprovado nem incorporado à skill). Foto original preservada: `foto_real_L8CFD_chatgpt_v2_original.png` (SHA-256 aa8ea77123e75ba472ea83dcb582141f7c9a05f3837b69e8ba13217d85a51c94). Fora do material de avaliação cega. Nada publicado, nenhum número real consumido, skill intacta.

Histórico de tentativas: imagem original (Gemini, 572 x 1024) e tentativa de correção 1 (esta, ChatGPT). Resta uma tentativa de correção antes da decisão humana, se o limite proposto de duas correções for aprovado.

## Etapa 1: fotografia

Arquivo: PNG 941 x 1672, 1.934.210 bytes, proporção 0,5628 (9:16 = 0,5625), ampliação de 1,148x até 1080 x 1920. Parâmetros do gerador: ChatGPT (modelo de imagem não informado); a resolução máxima disponível lá não foi verificada.

| Critério | Constatação | Veredito |
|---|---|---|
| I6 resolução | 941 px de largura, na faixa de atenção (810 a 1079), mas sem artefato de compressão visível; muito melhor que a v1 | Atenção, aceitável |
| I7 arquivo e proporção | íntegro, 9:16 | Passa |
| I5 antecipação do FORA | sem pessoa, etiqueta, nome ou segundo objeto | Passa |
| I4 coerência com o NA FOTO | guarda-chuva aberto secando em corredor | Passa |
| Realismo de materiais | tecido molhado com gotas e escorrimentos, anéis de água, reflexos no piso, rugosidade da parede: convincentes e detalhados | Passa |
| Contato do cabo com o piso | cabo reto com ponteira esférica, anéis concêntricos centrados e reflexo vertical sob ele | Passa |
| Contato da copa com a parede | a ponteira da vareta toca a parede com pequena sombra; contato crível | Passa |
| **I1 sustentação (inclinação)** | **A haste inclina cerca de 8,1 graus para a direita, isto é, para longe da parede à esquerda que a copa toca (ver `AUDITORIA_v2_inclinacao.png`). Com o topo deslocado para longe da parede e a parede só podendo empurrar, o objeto não teria equilíbrio e tombaria para a direita. Na foto v1 a inclinação era em direção à parede, o que sustentava.** | **Defeito provável, impeditivo para APTA** |
| Geometria da copa | vê-se o interior da copa e, acima, o dorso do tecido; a leitura espacial é difícil, mas não consegui demonstrar impossibilidade | Observação |
| Linguagem documental (D) | aparência mais cinematográfica que documental: contraste alto, simetria do corredor com ponto de fuga e luz da porta, piso muito molhado e brilhante, sem grão. O prompt pedia aspecto de celular e piso apenas levemente úmido | Desvio (I9), preferência a decidir por você |
| Composição pedida (I9) | o prompt pedia o objeto entre 18% e 52% da altura; copa vai de 28% a 55% e a haste até cerca de 68% | Desvio |

**Limite do achado I1:** baseia-se na geometria no plano da imagem; uma inclinação em profundidade (para a câmera ou para o fundo) não aparece e não posso excluí-la. Se o seu olho não percebe a anomalia, a decisão de aceitar é sua. O padrão proposto diz que anomalia perceptível que comprometa a credibilidade impede aprovação.

**Decisão da skill (proposta): AJUSTAR** (nova geração orientada, sem alterar a ideia). Pontos fortes a preservar: materiais, água, reflexos, luz fria, ausência de antecipação.

## Etapa 2: arte no perfil B (LAB-001, simulação)

Arquivos: `LAB-001_B_foto_v2.png` e `LAB-001_B_foto_v2_guias.png`. Aprovação técnica do script: SIM (texto cabe, zonas de segurança 250/340 px respeitadas, travessão ausente, texto não alterado). Aprovação visual: pendente de Eri.

Contraste do branco sobre o fundo sem texto (com degradê), limiares provisórios do padrão proposto:

| Elemento | Média | Pior decil | Resultado |
|---|---|---|---|
| Título | 4,2:1 | 1,8:1 (sobre a janela clara) | média passa (mínimo 3:1); trecho "LEGENDA" próximo da janela é o mais fraco |
| Número LAB-001 | 9,6:1 | 7,5:1 | passa |
| NA FOTO | 6,0:1 | 2,3:1 | média passa, pior decil abaixo de 3:1 |
| FORA | 10,8:1 | 6,3:1 | passa |
| Assinatura | 12,3:1 | 11,3:1 | passa |

Sobreposição com o elemento central (conferida na imagem): a haste atravessa o bloco NA FOTO ("corredor.") e o bloco FORA, a borda da copa encosta na linha "Um guarda-chuva aberto", e a ponteira do cabo fica atrás de "armário". O texto continua legível, mas passa sobre o elemento narrativo central, que era o ponto a conferir. **Observação sobre a metodologia:** o indicador automático de sobreposição que improvisei (pixels muito escuros) acusou só 2% e 1%, e errou; o julgamento visual é que valeu. Isso entra como limitação do verificador automático.

Fotografia bem melhor que a v1 (resolução, contraste, FORA sobre piso calmo), mas a composição ainda coloca o sujeito na zona de texto. **Decisão da skill (proposta): AJUSTAR.**

## Prompt revisado (tentativa de correção 2, a última antes da sua decisão)

Diferenças em relação ao prompt anterior: (1) inclinação explícita em direção à parede; (2) composição reforçada com ancoragem em partes da imagem, porque o gerador ignorou as porcentagens; (3) piso levemente úmido e luz mais plana, para reduzir o aspecto cinematográfico; (4) aspecto de foto de celular reforçado.

```
Fotografia realista de linguagem documental, formato vertical 9:16, na maior resolução disponível.

Cena: um guarda-chuva preto grande, de cabo reto, aberto e em pé sobre o cabo, no piso de um corredor comum de apartamento. IMPORTANTE para o equilíbrio: a haste inclina em direção à parede lateral, de modo que o topo da haste fique mais perto da parede do que o cabo, e a borda da copa encosta na parede, que sustenta o guarda-chuva. Gotas escorrem pelas varetas e pela borda do tecido. Uma poça pequena e bem delimitada, com poucos anéis de água, forma-se ao redor do cabo. O resto do piso está apenas levemente úmido, sem respingos espalhados e sem reflexos fortes. Ao fundo, a porta de entrada entreaberta e desfocada deixa passar luz cinzenta de dia chuvoso.

Ambiente: corredor estreito e comum, paredes lisas em tom claro, rodapé branco, piso de porcelanato bege acinzentado. Nada sobre o piso além do guarda-chuva e da água.

Câmera: foto de celular de boa qualidade, na altura do peito, levemente de frente, equivalente a lente de 35 mm, com a câmera mais afastada do que numa foto de detalhe, deixando ar ao redor do guarda-chuva. Profundidade de campo moderada.

Luz e cor: luz natural fria, difusa e mais plana, sem contraste dramático e sem efeito cinematográfico; paleta contida em cinzas, bege frio e preto. A parte superior do quadro (teto e paredes altas) em sombra suave e uniforme, mais escura que o resto, sem janela ou área clara atrás da faixa superior.

Composição, a regra mais importante: o guarda-chuva INTEIRO, da ponta da copa até a ponta do cabo no chão, ocupa somente os 45% SUPERIORES do quadro, com a copa começando a cerca de 18% da altura e o cabo tocando o piso a cerca de 45% da altura. Os 55% inferiores do quadro mostram apenas piso calmo, com reflexo suave, sem nenhum objeto. Nada importante nos 15% superiores.

Aparência: foto real de aspecto cotidiano, grão sutil, sem acabamento publicitário, sem aspecto de ilustração ou render.

Não incluir: nenhuma pessoa, mão ou rosto; nenhum texto, letra, número, logotipo, marca ou marca-d'água; nenhuma etiqueta, cartão, nome ou iniciais no guarda-chuva; nenhum segundo objeto além do guarda-chuva e do ambiente descrito.

Gere uma única imagem.
```

Observação de prudência: o bloco de texto do perfil B começa a cerca de 50% da altura, por isso o cabo foi pedido a 45%. A poça e o piso ficam sob o texto, o que é bom (piso calmo), mas confirme que o guarda-chuva não fique pequeno demais. Se o gerador não obedecer à composição, a alternativa é aceitar a v2 e rever a posição dos blocos num perfil novo, o que depende da sua decisão e não será feito sem ela.
