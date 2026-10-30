# Análise visual da fotografia gerada (piloto v0.2): Padrão de Excelência Fotográfica

STATUS: referência operacional PROVISÓRIA, proposta pela auditoria de 29/10/2026 e incorporada por decisão de Eri. Os limiares NÃO estão homologados e a reprodutibilidade entre episódios não foi demonstrada (uma única cena foi calibrada). Aprovação visual e editorial da foto é sempre de Eri; a skill nunca aprova.

Entrada: imagem anexada por Eri, mais a história aprovada (NA FOTO, FORA, conceito_foto). Abra a imagem de fato (Read com o caminho do arquivo anexado) e rode `python3 scripts/analisar_foto.py FOTO.png`. A análise tem três camadas: medições de apoio por código, leitura semântica da imagem e decisão humana. O código ajuda; ele não substitui a leitura.

## Defeitos impeditivos (qualquer um impede APTA)
- I1 Suporte físico: o objeto se sustenta de forma plausível? Um objeto equilibrado sem apoio, ou inclinado de modo que cairia, é defeito, ainda que a foto seja bonita. Exemplo do LAB-001: guarda-chuva aberto em pé sobre a ponteira (reprovado por Eri), e guarda-chuva inclinado com o topo afastado da parede (tende a cair). Estável: apoiado como uma escada, com o topo contra a parede e a base no piso.
- I2 Geometria: perspectiva, proporções, sombras e reflexos coerentes; sem objetos fundidos ou deformados.
- I3 Artefatos de IA: mãos, simetrias impossíveis, texturas cerosas, reflexos incoerentes, sombras sem fonte, brilho publicitário.
- I4 Contradiz o NA FOTO: sujeito, estado, posição ou ambiente não conferem com a história.
- I5 Antecipa o FORA: algo na imagem só faz sentido depois da revelação (segundo objeto simbólico, etiqueta, nome, vínculo, pista de quem ou porquê).
- I6 Resolução: ver limiares abaixo.
- I7 Integridade e formato: 9:16, sem texto, letras, números, logotipos ou marcas-d'água; sem rosto ou figura humana não prevista.
- I8 Composição e contraste: o sujeito não pode ficar sob os blocos de texto, e o texto precisa ser legível (limiares abaixo).
- I9 Desvio do prompt: elementos incluídos ou omitidos em relação ao que foi pedido.

## O que é verificável por código e o que não é
Por código (apoio, com limiares provisórios):
- Formato 9:16, dimensões e resolução (`scripts/analisar_foto.py`): abaixo de 810 px de largura é falha de resolução; de 810 a 1079 px é faixa de atenção; 1080 ou mais é adequada.
- Contraste efetivo do texto (`scripts/compor_story.py`, campo `contraste` do .checagem.json): relação de luminância do texto com a transparência real sobre a foto já com degradê, SEM a sombra do texto. Limites provisórios: blocos (rótulos e textos) média 4,5 e pior decil 3,0; elementos discretos (título, número, assinatura) média 3,0. Abaixo do limite gera AVISO, nunca bloqueio.
- Inclinação de haste ou objeto linear (`scripts/medir_inclinacao.py`): ângulo e se o topo está voltado para a parede ou afastado. Até 3 graus é praticamente vertical.
- Luminância por zona (`scripts/analisar_foto.py`).
Só por julgamento humano e leitura semântica: realismo documental, artefatos de IA, coerência física geral, fidelidade ao NA FOTO, não antecipação do FORA, protagonismo da foto sem o texto, aparência da copa e dos detalhes.

## Checagens adicionais herdadas
- Pessoas e rosto: padrão sem rosto.
- Composição para o texto: o sujeito escapa da área coberta pela interface (cerca de 13% no topo e 20% embaixo, valores provisórios) e não cruza os blocos de texto; o terço inferior fica calmo. Lição do LAB-001: um guarda-chuva grande no centro cruzou os blocos; menor e mais alto no quadro resolveu.
- Protagonismo: a foto sustenta a peça sozinha, sem o texto.

## Resultado
- APTA: pode ir para a composição.
- AJUSTAR: dá para corrigir com corte, ajuste de tom (por exemplo, escurecer um trecho atrás de um rótulo, sem tocar no objeto) ou uma única mudança pedida ao gerador; diga qual.
- REFAZER: nova geração com o prompt corrigido. Ajuste local de pixels que mova ou gire o objeto principal não é permitido como correção (deixa artefatos, porque o fundo atrás dele não existe).
Liste defeitos com o que se vê, onde e a gravidade. Seja específica e curta. Nunca declare a foto "aprovada para publicação".

## Limite de correções e exceções
Padrão: no máximo 2 correções ou gerações por história. Passar disso exige autorização expressa de Eri, registrada no registro da peça (quem autorizou, quando e o motivo). Sem autorização, a skill para e apresenta o impasse. Quando duas correções iguais falharem, não repita a instrução: mude o arranjo físico da cena ou peça uma única mudança por vez, descrita por pontos de contato.
