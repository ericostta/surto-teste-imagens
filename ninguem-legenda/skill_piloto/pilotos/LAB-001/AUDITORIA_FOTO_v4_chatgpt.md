# Auditoria da fotografia v4 de L8CFD (ChatGPT, edição da v3, terceira correção) e composição B

Data: 24/10/2026. Aplicação do padrão PROPOSTO (ainda não aprovado nem incorporado à skill). Foto preservada: `foto_real_L8CFD_chatgpt_v4_original.png` (SHA-256 892198e648bcf4e37361a6d81d6260553441c7fc127ba5a484abaa29a25d12b9). Terceira correção, autorizada por Eri acima do limite proposto de duas. Fora do material de avaliação cega. Nada publicado, nenhum número real consumido, skill intacta.

## Etapa 1: fotografia
PNG 941 x 1672, 2.089.751 bytes, proporção 0,5628, ampliação 1,148x (faixa de atenção do I6, sem artefato visível).

| Critério | Constatação | Veredito |
|---|---|---|
| Preservação da v3 | fundo, porta, luz, parede e piso mantidos (diferença média de 1,5 a 4 níveis em faixas sem o guarda-chuva, compatível com ruído de regeneração); poça menor com anéis; gota no cabo | Preservada |
| I4, I5 | sem pessoa, etiqueta, nome ou segundo objeto; NA FOTO e FORA intactos | Passa |
| **I1 sustentação (inclinação da haste)** | **Corrigida: a haste visível inclina 7,4 graus com o topo PARA a parede, e a copa encosta nela (`AUDITORIA_v4_inclinacao.png`). A medição foi feita por ajuste de reta aos pixels da haste e reproduz a medida da v3 (12,2 graus medidos contra 12,4 marcados à mão).** | **Resolvido** |
| Realismo e documental | luz plana, materiais convincentes, composição natural | Passa |
| Composição pedida | guarda-chuva na metade superior, cabo no piso a cerca de 49% da altura, metade inferior só piso calmo | Cumprida (copa começa a cerca de 8%) |
| **Coerência geométrica copa e haste (observação nova)** | **O aro da copa sobe para a direita cerca de 15 graus (da ponta esquerda à parede), o que implica um eixo da copa inclinado cerca de 15 graus para a esquerda, enquanto a haste visível inclina 7,4 graus para a direita: uma diferença de cerca de 22 graus entre o eixo da copa e o da haste. Na v3, os dois coincidiam (12,8 e 12,4 graus). Parece que a edição girou a haste e não a copa.** | **Observação medida; impacto perceptível incerto** |

Limites do achado novo: o raciocínio usa o contorno do aro como elipse e ignora perspectiva forte e deformação da copa; é uma estimativa, não uma prova. Em tamanho de celular o efeito pode passar despercebido. A decisão sobre perceptibilidade é do seu olho.

**Decisão da skill (proposta): APTA, condicionada à sua confirmação visual do ponto copa e haste.** Se você achar o encaixe da haste na copa estranho, a decisão passa a AJUSTAR.

## Etapa 2: arte no perfil B (LAB-001, simulação)
Arquivos: `LAB-001_B_foto_v4.png` e `_guias.png`. Aprovação técnica do script: SIM (texto cabe, zonas 250/340 px, sem travessão, texto não alterado). Aprovação visual: pendente de Eri.

| Elemento | Média | Pior decil | Resultado |
|---|---|---|---|
| Título | 5,9:1 | 2,5:1 | média passa; trecho sobre a janela e a borda da copa é o mais fraco; 36% da faixa do título sobre a copa |
| Número LAB-001 | 19,6:1 | 18,9:1 | legível, mas 98% da faixa dele está sobre a copa junto à parede |
| NA FOTO | 4,1:1 | 1,9:1 | média ligeiramente abaixo de 4,5:1; o rótulo "NA FOTO" fica lavado sobre uma faixa brilhante do piso |
| FORA | 10,2:1 | 7,7:1 | passa |
| Assinatura | 10,4:1 | 9,4:1 | passa |

NA FOTO e FORA ficam inteiros sobre piso calmo, sem cruzar o guarda-chuva (0% de sobreposição, confirmado na imagem). O contato do cabo com o piso fica logo acima do rótulo NA FOTO, sem encostar. A faixa vermelha cobre a copa só na simulação.

**Causa do rótulo lavado:** no perfil B o degradê da base começa em y=1010 e o rótulo NA FOTO fica em y=953, na parte mais clara. É um parâmetro do perfil, não da foto. **Decisão da skill (proposta): AJUSTAR a arte**, por uma calibração pequena do perfil B (por exemplo, começar o degradê mais acima) que só será feita com sua aprovação, porque layout não está homologado. Título e número sobre a copa são escolha de composição para você julgar.
