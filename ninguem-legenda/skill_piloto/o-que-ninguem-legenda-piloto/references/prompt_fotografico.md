# Prompt fotográfico para Gemini / Nano Banana (piloto v0.1)

Eri gera a imagem manualmente. Nada de geração automática nem serviço pago.

## Entrega
Sempre em BLOCO DE CÓDIGO, pronto para copiar inteiro (preferência fixa de Eri). Um bloco por prompt. Antes do bloco, no máximo duas linhas dizendo o que ele gera e o que conferir. Português do Brasil, a menos que Eri peça inglês.

## Princípio central
O prompt descreve o que a FOTO mostra (conceito_foto e NA FOTO) com especificidade. Ele NUNCA menciona, sugere ou desenha o conteúdo do FORA DO ENQUADRAMENTO. A imagem não pode antecipar a revelação (relações familiares, histórias, motivos, tempo transcorrido, o que aconteceu antes ou depois). Não é preciso representar o que está fora do enquadramento.

Armadilhas:
- Citar a revelação no prompt faz o modelo tentar desenhá-la. Nunca cite o FORA.
- Objetos "para dar contexto" (etiqueta com nome, segundo objeto simbólico, embalagem, bilhete, fotos de família) costumam antecipar a revelação. Só entra o que o conceito_foto pede.
- Pedir "emocionante", "nostálgico", "simbólico" gera cena de banco de imagens. Descreva luz, material e estado dos objetos, não sentimentos.

## Estrutura do prompt
1. Tipo e formato: fotografia realista, linguagem documental, vertical 9:16 (1080 x 1920 ou maior, mesma proporção).
2. Cena: sujeito principal, estado (novo, gasto, molhado, aberto), posição e relação com o ambiente. Fiel ao conceito_foto.
3. Ambiente: tipo de lugar, materiais, o que aparece ao fundo e fora de foco.
4. Câmera: altura do ponto de vista, distância, lente aproximada (por exemplo 35 mm), profundidade de campo.
5. Luz e cor: fonte, direção, temperatura, paleta contida.
6. Composição para o texto: sujeito na metade superior e central; terço inferior mais calmo, escuro ou desfocado, sem detalhes importantes nos 20% inferiores e nos 13% superiores (a interface do Instagram cobre as bordas e o texto ocupa a parte baixa). Valores provisórios.
7. Autenticidade: aspecto de foto real, grão sutil, sem acabamento publicitário, sem aspecto de ilustração ou render.
8. Exclusões: nenhum texto, letra, número, logotipo, marca, marca-d'água; nenhuma pessoa nem rosto (padrão da série), salvo decisão expressa; nenhum objeto além dos descritos.
9. Saída: uma única imagem.

## Conferência antes de entregar
- Rode `python3 scripts/checar_prompt.py --fora "<texto do FORA>" --prompt-arquivo prompt.txt`. Ele acusa palavras de conteúdo do FORA que aparecem no prompt. Ocorrência não é prova de erro, mas exige justificativa (por exemplo, um objeto que já está no NA FOTO).
- Releia: o prompt contém algo que Eri só entenderia depois de ler o FORA? Se sim, retire.
- Cada elemento do prompt está no conceito_foto ou no NA FOTO?

## Depois da geração
Eri anexa a imagem e a skill segue o procedimento de references/analise_visual.md. Máximo de 2 gerações por história no piloto; depois, decisão de Eri.
