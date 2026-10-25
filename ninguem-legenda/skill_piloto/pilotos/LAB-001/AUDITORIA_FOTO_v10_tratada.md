# Auditoria da foto v10 tratada (brilho do piso) de L8CFD
Data: 24/10/2026. Origem: `foto_real_L8CFD_chatgpt_v10_original.png` (preservada, sha256 45807c64...). Resultado: `foto_real_L8CFD_chatgpt_v10_tratada.png`; parâmetros em `tratamento_v10.json` (ganho de baixa frequência só na máscara do piso, força 1,0, percentil 10, raio 12; protege cabo, poça, anéis e reflexo). É ajuste de TOM: não inventa pixels, preserva textura e geometria. Script `tratar_piso.py` (fora da skill).

## Contraste efetivo (perfil B, render sem texto, `medir_contraste.py`; limites provisórios: blocos média 4,5 e pior decil 3,0; título e número média 3,0)
| Elemento | Original | Tratada |
|---|---|---|
| Título | 14,7 / 4,6 | 14,7 / 4,6 |
| Número LAB-001 | 5,5 / 2,0 | 5,5 / 2,0 |
| Rótulo NA FOTO | 4,0 / 2,7 | 4,1 / 3,3 |
| NA FOTO texto | 5,5 / 4,4 | 5,6 / 4,6 |
| Rótulo FORA | 5,1 / 4,6 | 5,2 / 4,9 |
| FORA texto | 10,6 / 7,3 | 12,3 / 10,9 |
| Assinatura | 6,2 / 5,8 | 6,4 / 6,3 |
(média / pior decil)
Único item abaixo do limite provisório: rótulo NA FOTO, média 4,1 (mínimo 4,5). Causa: transparência de 170/255 do rótulo no perfil B. Teste em memória (sem alterar o script): transparência 215 dá média 5,5 e pior decil 4,2. Alteração de perfil NÃO feita; depende de decisão de Eri (calibração do perfil B não homologada).

## Observações
- A ponteira do guarda-chuva passa sob "LEGENDA" do título (texto branco sobre ponteira escura, legível; sobreposição ao elemento central).
- Anéis da poça e reflexo sob o cabo ficam no limite do rótulo NA FOTO.
- Divulgar na publicação, se houver: tratamento de tom aplicado ao piso.

## Composição de teste com rótulos em 215/255 (autorizada por Eri, 24/10/2026 23:45)
`compor_B215.py` (fora da skill) cria o perfil de teste B215 = perfil B com rotulo_alpha 215; perfil B oficial e skill intactos. Saída: `LAB-001_B215_foto_v10_tratada.png` (+ `_guias`). Aprovação técnica do script: SIM, texto não alterado. Rótulo NA FOTO: média 5,5 e pior decil 4,2 (limite provisório 4,5 e 3,0 para média e decil: média passa; decil passa). Observação visual: o número LAB-001 sobre a janela clara continua o elemento de menor contraste (pior decil 2,0; média 5,5, acima do mínimo de 3,0 para título e número). Aprovação visual: pendente de Eri.

## Ajuste do degradê do topo no perfil de teste (Eri: "ajuste o que for necessário", 24/10/2026 23:47)
Perfil de teste B215 agora também com degradê do topo reforçado (grad_topo_max 0,65 até y 480; perfil B oficial: 0,34 até y 420). Efeito medido sem a sombra do texto: número LAB-001 média 4,6 para 5,1 e pior decil 1,9 para 2,3; título média 14,7 para 15,2 e pior decil 4,6 para 5,5. Melhora modesta; o número sobre a janela clara segue o elemento de menor contraste, legível (limite provisório de média 3,0 atendido; a sombra do texto, não medida, ajuda). Alternativa que eliminaria a questão: nova geração com a janela menos clara atrás do título. Aprovação técnica SIM; visual pendente de Eri.

## Ajustes de layout pedidos por Eri (24/10/2026 23:50), só no perfil de teste B215
1. Número da série (LAB-001) colado ao nome da série: fica à direita de "O QUE NINGUÉM LEGENDA" com respiro de 34 px, em vez de alinhado à margem direita. Implementado em `compor_B215.py` por substituição da função de texto em tempo de execução; `compor_story.py` e o perfil B oficial NÃO foram alterados.
2. "@surtodelucidez" (assinatura) menor: 27 px para 22 px (espaçamento 5 para 4). Interpretação: o pedido se referiu à assinatura; se Eri se referia a outro elemento, ajustar.
Aprovação técnica do script: SIM. O número agora cai sobre a parte esquerda da janela clara (conferir contraste no celular; não medido nesta posição). Perfil B continua sem homologação; estes ajustes entram na lista de decisões para a v0.2 (posição do número, tamanho da assinatura, rótulo 215, degradê do topo).
