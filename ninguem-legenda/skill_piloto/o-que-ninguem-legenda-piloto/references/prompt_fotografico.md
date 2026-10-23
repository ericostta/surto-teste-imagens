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

## Conferência antes de entregar (duas camadas, a semântica é obrigatória)
1. ANÁLISE SEMÂNTICA, feita por você e mostrada a Eri em poucas linhas antes do bloco: liste cada elemento do prompt e sua origem (conceito_foto ou NA FOTO). Para cada elemento, pergunte: sugere uma relação (família, casal, trabalho), um tempo transcorrido, um motivo, um antes ou depois, um segundo personagem ou objeto simbólico, um sentimento? Pergunte também: um leitor que visse só esta foto, sabendo só o NA FOTO, já inferiria algo do FORA? Qualquer elemento que antecipe a revelação sai ou é reformulado. Elementos neutros que o modelo costuma inventar (segundo guarda-chuva, bilhete, porta-retrato, sapatos de outra pessoa, objetos "de contexto") entram na lista de exclusões.
2. CONFERÊNCIA LEXICAL AUXILIAR: `python3 scripts/checar_prompt.py --fora "<texto do FORA>" --na-foto "<texto do NA FOTO>" --prompt-arquivo prompt.txt`. Ela acusa palavras de conteúdo do FORA e termos de vínculo. É apenas apoio: sinônimos, pistas visuais e relações implícitas passam por ela. Ausência de alerta NÃO garante que o prompt não antecipa a revelação.
Só entregue o bloco depois das duas camadas.

## Depois da geração
Eri anexa a imagem e a skill segue o procedimento de references/analise_visual.md. Máximo de 2 gerações por história no piloto; depois, decisão de Eri.
