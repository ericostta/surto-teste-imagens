# Relatório da G1 (geração e congelamento)

Data: 23/10/2026. Autorização de Eri: 23/10/2026 00h13, limitada à geração dos 60 candidatos e ao congelamento. Nenhum Crítico, preditor ou julgador foi executado; nenhum rótulo, triagem ou avaliação existe; nenhuma imagem foi gerada.

- Itens incluídos: 30 de fluxo e 30 de desafio.
- Hash do conjunto incluído: `0222c881921bcccc0175e6005abb2f047a037b0201f902beda90a1c46491c081`.
- Exclusões técnicas (5, todas por duplicata de conceito fotográfico, com substituição): G1-D12, G1-D14, G1-D22, G1-D26, G1-D27. Detalhes em `geracao/log_exclusoes_tecnicas.json`. Os itens excluídos continuam preservados.
- Ocorrência mantida sem exclusão: G1-F08 (falha do filtro lexical "destino", sentido literal), levada ao conhecimento de Eri.

## Método

Um subagente Criador por item, em contexto próprio, recebendo só o prompt do item e instruído a ler apenas `prompts/criador.md`, `registro.csv` e `taxonomia.json`. Uma candidata por item (o ciclo normal entrega três por rodada). Fluxo: conceito fotográfico sorteado no M2, em ordem. Desafio: o Criador cria a foto, com uma intenção de geração por célula (briefings em `geracao/prompts/`) e um ambiente designado em rodízio. O `registro.csv` não foi atualizado com os itens. Sem triagem por qualidade e sem rótulos. A isolação entre subagentes é a do ambiente (mesmo sistema de arquivos, mesma família de modelo); a proteção é documental.

## Identificação dos 60 itens e conceitos fotográficos

| Código | Origem | Conceito fotográfico |
|---|---|---|
| G1-F01 | sorteio K38 | Goteira no telhado de zinco durante chuva forte, panela no chão aparando a água. |
| G1-F02 | sorteio K18 | Pescador de costas lançando uma rede num lago ao amanhecer, neblina baixa. |
| G1-F03 | sorteio K01 | Bancada de cozinha com tábua de madeira, uma cebola cortada ao meio e uma faca, luz da manhã. |
| G1-F04 | sorteio K41 | Mesa de sinuca com bolas dispostas e o taco encostado na borda. |
| G1-F05 | sorteio K23 | Árvore grande no centro de uma praça, folhas amarelas espalhadas pelo chão. |
| G1-F06 | sorteio K33 | Ônibus escolar amarelo parado numa estrada rural, poeira no ar. |
| G1-F07 | sorteio K20 | Sofá de sala com almofadas desalinhadas e um controle remoto no braço, televisão desligada. |
| G1-F08 | sorteio K55 | Rodoviária à noite com bancos de plástico e um funcionário de costas varrendo o chão. |
| G1-F09 | sorteio K13 | Bandeirinhas coloridas penduradas entre postes numa rua de bairro, céu de fim de tarde. |
| G1-F10 | sorteio K12 | Tesoura e mechas de cabelo no chão de uma barbearia, cadeira giratória ao fundo. |
| G1-F11 | sorteio K34 | Máquina de costura com tecido estampado sob a agulha, mão guiando o pano. |
| G1-F12 | sorteio K50 | Mão segurando um molho de chaves diante de uma porta de madeira. |
| G1-F13 | sorteio K42 | Aparelho de ar-condicionado pingando na fachada de um prédio, mancha escura na parede abaixo. |
| G1-F14 | sorteio K39 | Contêineres coloridos de coleta seletiva alinhados na calçada, dia de recolhimento. |
| G1-F15 | sorteio K03 | Mãos descascando uma laranja sobre uma pia de aço inox. |
| G1-F16 | sorteio K29 | Pegadas pequenas de pés descalços na areia molhada, uma onda chegando. |
| G1-F17 | sorteio K51 | Cortina de janela balançando com o vento, luz de fim de tarde atravessando o tecido. |
| G1-F18 | sorteio K40 | Campo de futebol de várzea com gramado irregular, gol de madeira e nuvens carregadas. |
| G1-F19 | sorteio K06 | Quadra de futsal de bairro com traves enferrujadas e uma bola parada no meio, fim de tarde. |
| G1-F20 | sorteio K30 | Bandejas de salgados sob a vitrine iluminada de uma lanchonete, balcão de inox. |
| G1-F21 | sorteio K52 | Estante de livros com lombadas desalinhadas e uma escada de madeira encostada. |
| G1-F22 | sorteio K26 | Capacete de obra e botas de segurança sobre um andaime ao fim do dia. |
| G1-F23 | sorteio K10 | Bicicleta presa a um poste por uma corrente grossa, rua de bairro ao entardecer. |
| G1-F24 | sorteio K08 | Pessoa de costas sentada na ponta de um píer, pés pendurados sobre a água calma. |
| G1-F25 | sorteio K44 | Mão de criança segurando a mão de um adulto numa faixa de pedestres. |
| G1-F26 | sorteio K58 | Máquina de lavar roupa com a porta aberta e peças amontoadas dentro. |
| G1-F27 | sorteio K57 | Toalha estendida sobre a areia de uma praia, sol alto e pegadas ao redor. |
| G1-F28 | sorteio K35 | Prato de arroz, feijão e ovo frito sobre toalha xadrez, garfo ao lado. |
| G1-F29 | sorteio K07 | Balança de pratos com pesos de metal sobre o balcão de uma mercearia. |
| G1-F30 | sorteio K02 | Lençóis brancos balançando num varal de quintal, céu azul e muro baixo ao fundo. |
| G1-D01 | desafio (casa) | Mesa de cozinha de toalha de plástico xadrez desbotada, vista de cima e levemente de lado. Caderno de caligrafia de capa mole aberto, com linhas pautadas preenchidas por fileiras de traços e laçadas repetidas, nenhuma palavra legível. Lápis curto apontado a faca e borracha gasta ao lado. Uma xícara de café pela metade. Luz de manhã entrando por janela lateral, fogão e panela esmaltada desfocados ao fundo. Sem rosto, sem mãos, sem texto legível, sem marca. |
| G1-D02 | desafio (rua) | Banquinho dobrável de madeira, aberto, encostado a um portão de ferro pintado de verde, numa calçada de bairro residencial. Muro baixo com trepadeira ao lado, ao fundo uma rua de paralelepípedos com carros estacionados desfocados. Luz dourada de fim de tarde. Nenhuma pessoa. Sem placa, número legível, marca ou logotipo. |
| G1-D03 | desafio (comercio) | Balcão de madeira gasto de um mercadinho de bairro, visto de cima em ângulo baixo. Caderno de capa dura aberto, páginas com colunas de nomes e valores em caneta azul, ilegíveis, várias linhas cortadas por um traço único. Lápis, calculadora pequena e um pote de balas ao lado. Prateleiras desfocadas ao fundo. Luz de tarde entrando pela porta. Nenhuma pessoa. |
| G1-D04 | desafio (cozinha) | Cozinha comum de apartamento, vista de frente para o fogão de quatro bocas: panela de alumínio grande com tampa entreaberta soltando vapor e uma colher de pau apoiada ao lado. Azulejo claro ao fundo, pano de prato dobrado na bancada. Luz morna de fim de tarde vinda da janela lateral. Nenhuma pessoa, sem prato ou talher posto, sem texto, marca ou logotipo. |
| G1-D05 | desafio (lazer_esporte) | Bicicleta infantil de quadro claro, sem rodinhas, encostada numa grade baixa de praça pública, com um pé de apoio lateral. Chão de terra batida e grama rala ao redor, banco de concreto desfocado ao fundo. Luz rasante de fim de tarde. Nenhuma pessoa, nenhuma bicicleta de adulto, sem texto, marca ou logotipo. |
| G1-D06 | desafio (natureza) | Morro de capim alto e dourado visto de baixo para cima, com uma trilha estreita de terra batida subindo em leve curva até se perder atrás da crista. Algumas árvores baixas e pedras esparsas ao redor. Céu limpo, luz suave de fim de tarde. Nenhuma pessoa, nenhuma construção, nenhuma placa, sem sinal de água ou fonte no quadro. |
| G1-D07 | desafio (transporte) | Interior de ônibus urbano lotado no fim da tarde. Plano fechado em um colo de mulher sentada, corpo cortado abaixo do peito, sem rosto. Duas mãos seguram uma sacola de papel pardo lisa, dobrada no topo, sem estampa nem texto. Ao fundo, desfocados, barras de apoio metálicas e passageiros em pé de costas. Luz dourada entrando pela janela lateral. |
| G1-D08 | desafio (trabalho) | Mesa de escritório de baixo para cima em ângulo levemente elevado: tampo de laminado claro, monitor desligado, teclado alinhado, um mouse e um telefone fixo cinza. Gaveta inferior fechada, sem alça chamativa. Nenhum objeto pessoal, nenhuma caixa à vista. Cadeira ergonômica preta empurrada para dentro. Baias vazias desfocadas ao fundo, luz fria de lâmpadas de teto no fim do expediente. Nenhuma pessoa, sem texto legível, sem marca nem logotipo. |
| G1-D09 | desafio (festa) | Par de sapatos sociais pretos de homem, bem engraxados, lado a lado sobre o piso de um salão de festa, parcialmente sob uma mesa com toalha branca que cai até perto do chão. Ao fundo, desfocados, outras mesas postas, cadeiras com capas claras e luzes quentes de festa. Nenhuma pessoa, nenhum vestido ou véu visível, sem texto nem marca legível. |
| G1-D10 | desafio (escola) | Sala de aula de escola pública ainda vazia, vista de cima e de lado sobre uma carteira de madeira clara. Estojo de tecido liso aberto, com doze lápis de cor alinhados e de pontas afiadas, sem marca e sem texto legível. Cadernos fechados ao lado, sem nome. Luz suave de manhã entrando por janela lateral, outras carteiras desfocadas ao fundo. Nenhuma pessoa. |
| G1-D11 | desafio (casa) | Sala de apartamento alugado, parede branca lisa em close médio, com um único prego com a cabeça aparente a meia altura, sem quadro, sem marca de quadro anterior. Ao fundo, desfocado, o braço de um sofá cinza e uma caixa de papelão fechada no chão. Luz lateral suave de fim de manhã. Nenhuma pessoa, sem texto, sem marca, sem logotipo. |
| G1-D13 | desafio (comercio) | Balcão de madeira gasta de uma quitanda de bairro com balança de prato metálica. Saco de papel pardo aberto sobre o prato, laranjas aparecendo na boca do saco, o ponteiro do mostrador sem números legíveis. Ao lado, caixotes de frutas desfocados e uma mão masculina apoiada na borda do balcão, sem rosto. Luz lateral de manhã vinda da porta aberta. Sem texto, sem marca, sem etiqueta de preço legível. |
| G1-D15 | desafio (lazer_esporte) | Bicicleta infantil rosa encostada no tronco de uma árvore em gramado de parque, guidão com fitas curtas nas pontas. No chão, junto à roda traseira, duas pequenas rodinhas de apoio soltas na grama e uma chave de boca. Ao fundo, trilha de terra batida vazia e campo de futebol desfocado. Luz dourada de fim de tarde. Nenhuma pessoa, sem texto, sem marca, sem logotipo. |
| G1-D16 | desafio (natureza) | Árvore isolada de copa larga no centro de um pasto aberto, grama baixa e seca ao redor, sombra circular no chão. Céu limpo de fim de tarde, luz lateral dourada. Sem trator, sem cerca, sem construções e sem pessoas. Nenhum texto, marca ou logotipo. |
| G1-D17 | desafio (transporte) | Interior de um ônibus urbano à noite, visto da parte de trás do corredor. Um passageiro de jaqueta escura dorme no último banco, cabeça encostada na janela, visto de costas e levemente de lado, sem rosto visível. Bolsa de lona no colo, alça enrolada na mão. Bancos vazios à frente, barras de apoio cromadas, luz amarelada de teto e reflexos de postes na janela. Motorista fora do quadro, sem espelho retrovisor mostrando alguém. Sem marcas, sem logotipos, sem letreiros ou qualquer escrita visível. |
| G1-D18 | desafio (trabalho) | Caneca de cerâmica branca com a borda lascada e uma marca de café seco no fundo, sobre a mesa de um escritório, ao lado de um teclado cinza e um mouse. Monitor desligado ao fundo, desfocado, e divisória baixa de baia. Luz fria de lâmpadas de teto misturada à luz lateral de uma janela. Nenhuma pessoa, sem logotipo e sem nada legível na caneca ou na mesa. |
| G1-D19 | desafio (festa) | Mesa de festa infantil em salão de condomínio, coberta por toalha branca lisa: centenas de brigadeiros em forminhas alinhadas em bandejas, torre de copos descartáveis, cacho de balões amarelos e azuis preso à parede ao fundo. Luz clara de tarde vinda de janela lateral. Nenhuma pessoa, nenhum texto legível, sem marca, sem faixa ou cartaz com nome. |
| G1-D20 | desafio (escola) | Toco de giz branco, gasto e pequeno, na calha de metal de um quadro-negro limpo, sem nada escrito. Pó de giz fino na calha. Sala de aula vazia ao fundo, desfocada, com carteiras de madeira alinhadas e janelas altas. Luz oblíqua de fim de manhã. Nenhuma pessoa, sem texto legível, sem marca. |
| G1-D21 | desafio (casa) | Corredor estreito de casa em plena madrugada, visto do fundo. Uma única luminária pequena de parede acesa, luz âmbar suave sobre o piso de madeira e o rodapé. Uma porta de quarto entreaberta ao fundo, escura por dentro. Paredes lisas em tom neutro, um tapete simples. Sem objetos infantis, sem texto, sem marca. Nenhuma pessoa. |
| G1-D23 | desafio (comercio) | Balcão de madeira de uma mercearia de bairro, em primeiro plano um pote de vidro de tampa metálica cheio de balas coloridas embaladas, ao lado de uma caixa registradora antiga de teclas, sem visor legível. Prateleiras desfocadas ao fundo com latas e sacos sem rótulo visível. Luz morna de fim de tarde entrando pela porta. Nenhuma pessoa, sem texto, sem marca, sem logotipo. |
| G1-D24 | desafio (cozinha) | Close na boca de um fogão de cozinha doméstica: frigideira de ferro bem grande, escurecida pelo uso, com um único ovo frito no centro e bastante área vazia ao redor. Cabo de madeira gasto, espátula apoiada na borda. Bancada de azulejo claro ao fundo, desfocada, sem outros utensílios em destaque. Luz de manhã vinda de janela lateral. Nenhuma pessoa, sem texto, sem marca, sem logotipo. |
| G1-D25 | desafio (lazer_esporte) | Par de luvas de goleiro infantis, de tecido gasto e dedos um pouco sujos de terra, apoiado sobre uma bola de futebol desbotada, no gramado irregular de um campinho de bairro. Trave simples e sem rede desfocada ao fundo. Luz baixa e dourada de fim de tarde. Nenhuma pessoa, sem marca, sem logotipo, sem texto. |
| G1-D28 | desafio (trabalho) | Capacete de obra amarelo, riscado e salpicado de cimento seco, pendurado num prego de um tapume de madeira num canteiro de obras. Visto de frente e por fora, com o interior totalmente oculto. Ao fundo, desfocados, andaime e sacos de cimento empilhados. Luz seca de fim de manhã. Nenhuma pessoa, sem texto, sem marca, sem logotipo. |
| G1-D29 | desafio (festa) | Salão de festa infantil já quase vazio, visto de perto: um balão azul comum, um pouco murcho, amarrado com fita ao encosto de uma cadeira de plástico branca à cabeceira de uma mesa com restos de docinhos em forminhas e copos descartáveis. Outros balões coloridos, mais cheios e brilhantes, ao fundo e desfocados, em arco desbotado. Serpentinas no chão. Luz quente de fim de tarde entrando por uma janela lateral. Nenhuma pessoa, sem texto, sem marca, sem logotipo. |
| G1-D30 | desafio (escola) | Close em uma carteira escolar de madeira clara, com marcas leves de uso. Sobre ela, um lápis amarelo reduzido a um toco de poucos centímetros, ponta recém-apontada, ao lado de um estojo de tecido aberto onde aparecem lápis novos e inteiros. Sala de aula desfocada ao fundo, janelas e fileiras de carteiras vazias. Luz natural suave de manhã. Sem texto legível, sem marca, sem logotipo. Nenhuma pessoa. |
| G1-D31 | desafio (lazer_esporte), substitui G1-D12 | Bola de tênis de feltro desbotado e quase sem pelo, parada junto ao alambrado, no canto de uma quadra pública de saibro. Linhas de cal apagadas, sombra comprida do alambrado. Luz baixa de fim de tarde. Nenhuma pessoa, nenhuma raquete no quadro, sem texto nem marca. |
| G1-D32 | desafio (trabalho), substitui G1-D22 | Suculenta pequena em vaso de barro simples sobre uma mesa de escritório, ao lado de um teclado cinza e um mouse. Plano fechado, com o resto do escritório desfocado ao fundo, sem outras plantas visíveis. Luz fria e uniforme de lâmpadas de teto. Nenhuma pessoa. Sem texto legível, marca ou logotipo. |
| G1-D33 | desafio (festa), substitui G1-D26 | Cerca de uma dúzia de balões de látex coloridos (vermelho, amarelo, azul, verde), sem estampa, amarrados no portão de ferro de um salão de festas comunitário, com a porta aberta ao fundo e mesas com toalhas de plástico desfocadas. Luz de fim de manhã, céu claro. Nenhuma pessoa, sem texto, sem marca, sem logotipo. |
| G1-D34 | desafio (escola), substitui G1-D27 | Estojo de tecido em cores vivas, zíper fechado, sobre uma carteira escolar de madeira clara com tampo levemente riscado, numa sala de aula vazia no fim da tarde. Caderno fechado ao lado, quadro verde apagado ao fundo, desfocado. Luz dourada entrando por janela lateral. Nenhuma pessoa, sem texto legível, sem marca nem logotipo. |
| G1-D35 | desafio (natureza), substitui G1-D14 | Rede de algodão cru armada entre dois troncos de árvores à beira de um riacho raso, mata fechada ao redor. Rede vazia, levemente curvada, sem objetos pessoais por perto. Luz coada de fim de tarde entre as folhas. Nenhuma pessoa, sem texto, sem marca, sem logotipo. |

As células de intenção do desafio estão só no mapa privado (`mapa_privado.json`), que não entra em pacote de avaliação.

## Limitações

- O orquestrador (Claude) viu os textos gerados ao recebê-los; não os alterou nem filtrou. Registrado em `registro_acessos_g1.jsonl`.
- O critério de duplicata envolveu julgamento do orquestrador sobre o que é "mesma cena" (critério e pares mantidos no log). Dois turnos de substituição ocorreram antes de qualquer rótulo.
- O rodízio de ambientes do desafio (ciclo de 10) causou as colisões de cena que geraram as exclusões; os substitutos receberam outros ambientes.
- Os itens de desafio refletem a intenção pedida ao Criador e podem não corresponder à classe real.
