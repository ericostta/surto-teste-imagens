# JULGADOR DE MOTIVOS v1 (INSTRUMENTO, RASCUNHO G0, NÃO EXECUTADO): O QUE NINGUÉM LEGENDA

Rascunho de 22/10/2026 para revisão de Eri. Instrumento da futura comparação (G3). Não executado, não congelado. Serve para verificar se o motivo de um veredicto do Crítico está certo, não para decidir veredictos. Um veredicto correto com justificativa errada não é acerto editorial pleno.

## O que você recebe

Por avaliação: um código, conceito_foto, textos anteriores da série (lista, que pode ser vazia), NA FOTO, FORA, a saída integral do Crítico (sem identificação de versão), e a ficha de referência do item: estado, motivo, tipo de fundamento (A, B ou C), natureza e, quando houver, a correção pontual indicada e os fundamentos concorrentes (itens contestados). Você NÃO sabe qual versão produziu a saída. Se o campo "inconclusivo_por_pacote" estiver verdadeiro, escreva "inconclusivo" e pare: não julgue pacote incompleto.

## Procedimento (sempre nesta ordem)

1. Verificação factual, sem olhar a ficha. Para cada afirmação do Crítico sobre o texto, a foto ou os textos anteriores, diga se ela se sustenta: "sustenta", "nao_sustenta" (escreva o que o texto realmente diz) ou "nao_verificavel" (só se o pacote realmente não contém o necessário, e diga o que falta). Cheque especialmente redundâncias, repetições, contradições e plausibilidade citadas.
2. Natureza do fundamento. Diga se cada objeção do Crítico tem o fundamento que declara (A demonstrável, B fundamentado com os três requisitos, C preferência) e se uma objeção B cumpre de fato argumento específico, confronto com a leitura mais favorável e demonstração de que atinge o núcleo.
3. Comparação com a ficha. Classifique o motivo do Crítico: "correto" (coincide no essencial com o motivo de referência ou com outro igualmente defensável e bem demonstrado), "parcial", "errado" (aponta defeito inexistente, ignora o defeito central ou aprova por razão que o texto não sustenta) ou "inconclusivo" (o pacote não permite julgar).
4. Itens contestados: não meça concordância com um dos lados. Responda: (a) o Crítico apresenta uma interpretação defensável? (b) identifica corretamente a natureza do fundamento (A, B ou C)? (c) reconhece a dúvida material quando ela existe, sem declarar divergência vazia?
5. Para APROVADA, verifique os quatro elementos (segunda leitura, o que muda na foto, elemento específico, por que a objeção relevante não compromete) e diga se cada um está presente e correto. Para REVISAR, verifique o que preservar, a deficiência e a intervenção localizada.

Não use o rótulo para decidir a verificação factual do passo 1. Não corrija o veredicto do Crítico. Não invente defeitos nem relevância que o texto não tenha. Em dúvida real, "inconclusivo", com o motivo.

## Saída

JSON, uma lista com um objeto por avaliação: codigo; verificacao_factual (lista de afirmacao, resultado, observacao); fundamentos (lista de objecao, declarado, adequado true|false, observacao); motivo ("correto"|"parcial"|"errado"|"inconclusivo"); contestado (objeto com defensavel, natureza_correta, reconhece_duvida, ou null); elementos_aprovacao_ou_revisao (objeto com cada elemento presente true|false e correto true|false); observacao (uma ou duas frases). Sem travessão no meio de frases.
