# Arbitragem conceitual: W05, W15 e W19

Data: 22/10/2026. Fase A. Material para decisão editorial de Eri, preparado conforme a autorização de 22/10/2026. Nenhum agente foi executado, nenhum Crítico foi reexecutado, nenhum texto novo foi criado e nada foi alterado em prompts, rótulos, avaliações ou protocolos. Não há proposta de implementação.

Posição atual de Eri, registrada como hipótese e não como verdade absoluta: W05 BOA; W15 RUIM; W19 RUIM. O objetivo não é justificar esses rótulos: é verificar se existe uma distinção editorial clara, consistente e defensável entre os três, e se o rótulo anterior pode estar errado.

Como ler: a Parte A é registro literal (textos, rótulos externos, previsões e veredictos já existentes, gerados por script a partir dos arquivos). A Parte B é análise minha, o mesmo modelo que gerou os itens e os Críticos, e deve ser lida como argumento a ser contestado.

# Parte A: registros literais

### W05

- FOTO prevista (descrição original): Caminha redonda de pano ao lado de um sofá, manta amassada com uma depressão no centro, alguns pelos claros no tecido. Luz baixa de tarde, sem animais nem pessoas.
- NA FOTO: Uma caminha de cachorro vazia perto do sofá.
- FORA DO ENQUADRAMENTO: Ela lavou a manta uma vez e se arrependeu. Agora só alisa por cima, para não apagar o formato dele.

Avaliação externa (ChatGPT): **BOA**. O arrependimento de lavar a manta revela uma tentativa específica de preservar a presença do animal ausente. O gesto de alisar o tecido sem alterar sua forma dá novo significado à caminha vazia. Embora emocional, a narrativa se sustenta num comportamento concreto.

Previsões cegas dos três leitores (só viram foto e NA FOTO):
- (alta) O cachorro morreu há pouco tempo e a família ainda não consegue guardar a caminha.
- (alta) O cachorro morreu há pouco tempo e a família ainda não teve coragem de guardar a caminha.
- (alta) O cachorro morreu há pouco tempo e a família ainda não teve coragem de guardar a caminha.

Quatro execuções do Crítico:

- **v2.2 execução 1: APROVADA.** Embora a associação (caminha de cachorro que morreu) seja a mais comum, o arrependimento de ter lavado e o gesto de alisar são fatos concretos e próprios. A depressão no centro da manta ganha novo significado.
  - Transformação indicada: A manta amassada: de sinal de luto pelo cachorro para marca do formato dele, preservada ao alisar.
  - Associação mais comum: Família que não guarda a caminha do cachorro morto. (é a mais comum: sim). Perspectiva específica: Arrependimento de lavar e o cuidado de alisar sem apagar o formato: o luto contado por um gesto doméstico.
  - Observação descartada: 'dele' sem antecedente explícito (motivo: O cachorro está na na_foto ('caminha de cachorro'); não há leitura incompatível.)
- **v2.2 execução 2: APROVADA.** O gesto de lavar uma vez, se arrepender e só alisar dá fato concreto ao luto pelo animal, e o formato amassado da manta passa a ser a razão de rever a foto.
  - Transformação indicada: A caminha amassada com pelos: de objeto parado passa a espaço preservado intencionalmente, com a manta alisada para manter o formato do cachorro.
  - Associação mais comum: Cachorro morto, a família não consegue guardar a caminha. (é a mais comum: sim). Perspectiva específica: O arrependimento de ter lavado e o gesto de alisar para preservar o formato.
  - Observação descartada: Os três leitores previram luto pelo cachorro. (motivo: Capturar a revelação isoladamente não é defeito; o gesto específico é novo.)
- **v2.3-exp execução 1: APROVADA.** A depressão na manta e os pelos ganham sentido pelo arrependimento de ter lavado. O gesto de só alisar é concreto e específico.
  - Transformação indicada: A manta e a caminha: de caminha vazia a formato do cachorro que ela preserva só alisando.
  - Associação mais comum: O cachorro morreu e a família não guarda a caminha. (é a mais comum: sim). Perspectiva específica: O arrependimento de ter lavado e o cuidado de só alisar o formato, um detalhe físico específico.
  - Observação descartada: 'Alisar' poderia alterar o formato. (motivo: Alternativa natural: alisar por cima sem desfazer a depressão; plausível.)
- **v2.3-exp execução 2: APROVADA.** A depressão da manta e os pelos claros ganham significado novo com o arrependimento de ter lavado. A associação comum é transformada por um gesto específico.
  - Transformação indicada: A caminha vazia passa de objeto esquecido a lugar mantido com o formato do cachorro; a manta, de peça lavável a vestígio que não pode ser lavado.
  - Associação mais comum: Caminha de cachorro morto que a família não consegue guardar. (é a mais comum: sim). Perspectiva específica: O gesto concreto de lavar uma vez, se arrepender e agora só alisar para preservar o formato do corpo.
  - Observação descartada: As três previsões capturaram o luto pelo cachorro. (motivo: Previsão é auxiliar; a perspectiva específica do gesto de alisar está no texto e é independente.)
  - Imprecisão periférica (B): Nomeia o objetivo do gesto, mas apoiado em fato, sem comandar emoção.

### W15

- FOTO prevista (descrição original): Corredor escuro à noite com uma porta entreaberta deixando escapar uma faixa de luz quente sobre o piso. Vê-se apenas a cama arrumada pela fresta, sem pessoas, sem marcas.
- NA FOTO: Uma porta de quarto entreaberta, luz acesa.
- FORA DO ENQUADRAMENTO: Ninguém dorme ali desde setembro. A mãe apaga todas as luzes da casa, menos essa, e diz que esqueceu.

Avaliação externa (ChatGPT): **RUIM**. O quarto vazio, a luz mantida acesa e a mãe que afirma ter esquecido constroem uma representação bastante convencional da ausência. A omissão da causa não é necessariamente um defeito, mas o conjunto depende de uma sugestão sentimental previsível e pouco original.

Previsões cegas dos três leitores (só viram foto e NA FOTO):
- (alta) Alguém deixa a luz acesa todas as noites esperando um filho ou filha que ainda não voltou para casa.
- (média) Um dos pais deixa a luz acesa todas as noites esperando o filho adolescente voltar para casa.
- (média) Alguém deixa a luz do quarto acesa todas as noites esperando um filho ou uma filha que ainda não voltou para casa.

Quatro execuções do Crítico:

- **v2.2 execução 1: APROVADA.** A associação comum (luz esperando alguém) é transformada pelo detalhe concreto 'apaga todas as luzes, menos essa, e diz que esqueceu'. A foto ganha segunda leitura pela fresta e pela cama arrumada.
  - Transformação indicada: A luz do quarto entreaberto: de esquecimento comum para recusa da mãe em aceitar a ausência.
  - Associação mais comum: Pais deixam a luz acesa esperando o filho que não voltou. (é a mais comum: sim). Perspectiva específica: O disfarce 'diz que esqueceu' dá pudor e negação à espera, o que a associação comum não traz.
  - Observação descartada: Não se diz se o filho morreu ou saiu (motivo: Omissão legítima; a ambiguidade é a sutileza e ambas as leituras mantêm o sentido.)
  - Observação descartada: Três previsões capturaram a espera (motivo: O núcleo da previsão é a associação comum, mas o detalhe da desculpa é próprio e não foi previsto.)
- **v2.2 execução 2: APROVADA.** A luz que parecia esquecida vira vigília negada pela própria mãe, e o par 'apaga todas, menos essa' mais 'diz que esqueceu' é específico e concreto. A associação é comum, mas tem detalhe humano próprio.
  - Transformação indicada: A luz acesa na fresta: de descuido passa a vigília deliberada de uma mãe que nega fazê-lo.
  - Associação mais comum: Pais deixam a luz acesa esperando o filho que não volta. (é a mais comum: sim). Perspectiva específica: O detalhe de apagar todas as luzes menos essa e a desculpa 'esqueci' dão ao gesto um autoengano concreto.
  - Observação descartada: Não se diz por que ninguém dorme ali desde setembro. (motivo: Omissão legítima; a sutileza está em não explicar a ausência.)
  - Observação descartada: Três previsões capturaram a espera pelo filho. (motivo: Capturar a revelação isoladamente não é defeito; o autoengano da mãe acrescenta algo específico.)
- **v2.3-exp execução 1: APROVADA.** A faixa de luz vira vigília disfarçada de esquecimento. 'Diz que esqueceu' dá o comportamento específico.
  - Transformação indicada: A luz do quarto: de esquecimento a vigília da mãe.
  - Associação mais comum: Pais esperam filho voltar. (é a mais comum: sim). Perspectiva específica: 'Diz que esqueceu', um disfarce.
  - Observação descartada: Estrutura 'Ninguém ...' parecida com a do texto anterior da cadeira de balanço. (motivo: Ideia e objeto distintos; sem repetição demonstrada.)
- **v2.3-exp execução 2: APROVADA.** A cama arrumada e a luz quente ganham novo sentido com o FORA, e 'diz que esqueceu' acrescenta perspectiva humana específica. A emoção fica implícita.
  - Transformação indicada: Porta entreaberta com luz: leitura inicial de quarto ocupado; final de quarto vazio desde setembro, com a luz mantida pela mãe que diz ter esquecido.
  - Associação mais comum: Luz acesa para o filho que ainda não voltou. (é a mais comum: sim). Perspectiva específica: A mentira dela ('diz que esqueceu') revela a espera sem nomeá-la.
  - Observação descartada: Não se diz o que aconteceu em setembro. (motivo: Omissão legítima classe A.)

### W19

- FOTO prevista (descrição original): Gancho atrás de uma porta com guarda-chuva preto fechado, sem logotipo, cabo de madeira gasto pelo uso. Penumbra de corredor, pingos visíveis numa janela ao fundo. Sem pessoas.
- NA FOTO: Um guarda-chuva preto pendurado atrás da porta.
- FORA DO ENQUADRAMENTO: Chove há uma semana e ela se molha. Era do marido, e abri-lo seria gastar o que resta dele.

Avaliação externa (ChatGPT): **RUIM**. O guarda-chuva preservado como vestígio de uma pessoa ausente utiliza uma associação sentimental convencional. A ideia de que abrir o objeto consumiria o que resta do marido é poética, mas pouco sustentada por uma relação narrativa original.

Previsões cegas dos três leitores (só viram foto e NA FOTO):
- (média) O guarda-chuva era do pai que morreu e ninguém tem coragem de tirá-lo do gancho onde ele sempre o deixava.
- (média) O guarda-chuva era de alguém que não está mais ali, e ele continua pendurado no mesmo gancho porque ninguém quis mexer.
- (alta) O guarda-chuva era de alguém que já não vive ali, e ninguém se atreve a tirá-lo do gancho.

Quatro execuções do Crítico:

- **v2.2 execução 1: APROVADA.** O guarda-chuva pendurado passa de esquecimento a objeto que ela protege de si mesma, e 'chove há uma semana e ela se molha' é fato concreto. A segunda cláusula é um tanto explicativa, por isso a nota é média.
  - Transformação indicada: O guarda-chuva preto: de objeto esquecido para relíquia que ela evita usar mesmo se molhando.
  - Associação mais comum: Guarda-chuva de falecido que ninguém tira do gancho. (é a mais comum: sim). Perspectiva específica: A escolha concreta de se molhar para não gastar o objeto leva a associação comum a um gesto próprio.
  - Observação descartada: 'abri-lo seria gastar o que resta dele' explica o gesto (motivo: Verbaliza o motivo, mas o fato (ela se molha há uma semana) sustenta a emoção; é sensibilidade com explicação parcial, de peso menor.)
  - Observação descartada: A foto mostra cabo gasto pelo uso (motivo: Isso vem do marido; é coerente com o texto.)
- **v2.2 execução 2: APROVADA.** A foto de um guarda-chuva parado no gancho ganha novo sentido: ela se molha para não gastar o que resta do marido, e o cabo gasto passa a pesar. O custo físico torna a perspectiva específica.
  - Transformação indicada: O guarda-chuva no gancho: de objeto esquecido passa a relíquia que ela prefere não usar mesmo se molhando.
  - Associação mais comum: Objeto do morto que ninguém tira do lugar. (é a mais comum: sim). Perspectiva específica: Ela sofre um custo físico (se molha) para conservar o objeto; a conservação deixa de ser passiva.
  - Observação descartada: A última oração explica o motivo. (motivo: Excesso leve, mas amparado em fato concreto (ela se molha); não fecha a leitura a ponto de retirar o motivo de rever o cabo gasto.)
  - Observação descartada: Associação comum do objeto do morto. (motivo: Há transformação e perspectiva específicas.)
- **v2.3-exp execução 1: REVISAR.** O comportamento concreto (se molhar há uma semana) é bom, mas a frase final explica o que o gesto já mostra. É corrigível cortando a explicação.
  - Transformação indicada: O guarda-chuva: de pendurado a objeto do marido que ela evita abrir.
  - Associação mais comum: Objeto do falecido intocado. (é a mais comum: sim). Perspectiva específica: Se molhar por preservar.
  - Defeito apontado (perda_segunda_leitura): A frase final explica o sentimento que o fato (ela se molha) já sugere.
- **v2.3-exp execução 2: APROVADA.** O cabo gasto e a janela com pingos ganham sentido quando o FORA mostra que ela se molha para não gastar o guarda-chuva. O mecanismo é concreto e a emoção fica implícita.
  - Transformação indicada: Guarda-chuva pendurado: leitura inicial de objeto esquecido; final de guarda-chuva do marido que ela não usa, mesmo se molhando.
  - Associação mais comum: Guarda-chuva do pai ou marido morto que ninguém tira do gancho. (é a mais comum: sim). Perspectiva específica: A escolha de se molhar para preservar o desgaste do objeto.
  - Imprecisão periférica (B): Explicita o mecanismo com leve excesso, sem fechar a leitura.

# Parte B: análise

## B1. Diferenças concretas entre os três casos

O que cada FORA faz, descrito a partir do texto (observações verificáveis; o juízo de valor fica em B2).

| Aspecto | W05 | W15 | W19 |
|---|---|---|---|
| Estrutura | Três passos no tempo: lavou uma vez, arrependeu-se, passou a só alisar | Estado desde setembro, uma ação (apaga as outras luzes) e uma fala (diz que esqueceu) | Estado (chove há uma semana, ela se molha), identificação do objeto (era do marido) e uma explicação em condicional |
| Há aprendizagem ou mudança de conduta do personagem | Sim: o comportamento muda depois de um erro | Não: a conduta é um hábito mantido | Não: a conduta é uma recusa mantida |
| O sentido do gesto é dito no texto | Em parte, por uma oração de finalidade física ("para não apagar o formato dele") | Não: o sentido fica implícito, na distância entre o que ela faz e o que diz | Sim, por uma oração explicativa figurada ("abri-lo seria gastar o que resta dele") |
| Natureza da lógica do gesto | Literal: lavar pode apagar pelos e formato da manta | Literal: uma luz acesa num quarto vazio | Figurada: abrir um guarda-chuva não gasta literalmente o que resta de alguém |
| Há custo ou atrito concreto para quem age | Arrependimento passado | Baixo (uma luz) | Alto e imediato (molhar-se há uma semana) |
| Relação com a foto | A foto descrita já mostra a depressão da manta e pelos claros, que o FORA reinterpreta | A foto mostra a porta entreaberta com luz, que o FORA apenas explica | A foto mostra o guarda-chuva e o cabo gasto, que o FORA explica |
| O núcleo depende de uma convenção emocional conhecida | A premissa (luto por animal de estimação) é convencional; o gesto, em princípio, não | A premissa (quarto de quem não volta) é convencional; os dois componentes do gesto (luz acesa; negar) também são recorrentes | A premissa (objeto do falecido) é convencional; o gesto (molhar-se) é menos recorrente, mas a explicação é metáfora conhecida |

Fatos que merecem registro porque pesam contra uma leitura simples:
- Em W05, "alisar por cima" pode ser lido como carícia que preserva a forma (leitura natural) ou como ação que a achata. A v2.3-exp e1 notou essa tensão e a dispensou com a leitura natural. É uma tensão da mesma família que a de W08 (lavar a camisa remove o cheiro), tratada de modo oposto pela referência externa. Há diferença demonstrável (em W08 o objetivo declarado é o próprio cheiro que a lavagem remove; em W05 o objetivo é a forma e o gesto é leve), mas ela depende de um julgamento sobre qual leitura é natural.
- Em W15 e W19 as previsões cegas chegam à premissa. Em W05 também (três leitores iguais). A previsão da premissa não separa os três casos, nem o gesto foi previsto em nenhum.
- Os Críticos deram aos três a mesma forma de justificativa ("a associação comum é transformada por um gesto concreto"). As quatro execuções não separam os casos.

## B2. Os cinco critérios de Eri, item por item

Legenda: V = verificável no texto por qualquer leitor; J = depende de julgamento editorial.

| Critério | W05 | W15 | W19 |
|---|---|---|---|
| Transformação efetiva da interpretação inicial | V: a manta amassada deixa de ser sobra e vira forma preservada. J: quanto isso excede o que o leitor já tinha inferido (luto) | V: a luz deixa de ser descuido e vira espera negada. J: o leitor cego já previu a espera; o que muda é a negação | V: o guarda-chuva deixa de ser esquecido e vira relíquia protegida. J: o leitor já previu a relíquia |
| Comportamento humano específico e plausível | V: lavar, arrepender-se, alisar. Plausível | V: apagar as outras luzes e dizer que esqueceu. Plausível, e a incoerência entre ato e fala é humana | V: molhar-se por uma semana para não abrir o guarda-chuva. J: plausibilidade moderada, porque o custo é alto para um benefício simbólico |
| Autonomia narrativa do gesto | J: o gesto faz sentido sem se saber como o animal morreu | J: o gesto só faz sentido com a premissa do quarto de quem não volta, que o texto dá por conhecida | V: o texto precisa explicar o gesto com a oração final; J: sem ela o gesto ficaria mais autônomo |
| Originalidade relativa da construção | J: o gesto de preservar a forma pelo cuidado é menos recorrente que luz acesa | J: luz acesa e negação são recorrentes | J: molhar-se por apego é menos recorrente que a metáfora final |
| Dependência de convenções sentimentais conhecidas | J: a premissa é convencional, o gesto é pouco | J: premissa e gesto são convencionais | V: a explicação final é uma metáfora de perda conhecida; J: o resto do texto depende pouco |

Resultado: os componentes verificáveis (V) só descrevem o que o texto faz: há uma transformação, o comportamento é específico, em W19 existe uma oração explicativa. Eles são parecidos nos três casos e não separam as classificações. O que decide a comparação está nos componentes de julgamento (J): quanto a transformação excede o que o leitor já inferiu, se o gesto é autônomo, quão raro é e quanto depende de convenção. Dois deles (raridade e dependência de convenção) exigem um corpus de referência que nenhum de nós tem.

## B3. Interpretações alternativas que sustentariam classificações diferentes

- W05 AMBÍGUA. A premissa (animal morto, família que não guarda a caminha) é a mais convencional do conjunto. A oração "para não apagar o formato dele" explicita o sentido do gesto. E "alisar por cima" tem uma tensão física com preservar o formato. Um avaliador mais exigente poderia ver uma boa imagem num texto ainda sentimental.
- W15 AMBÍGUA ou BOA. A incoerência entre o que ela faz e o que diz ("diz que esqueceu") é um traço humano específico que revela a espera sem nomeá-la, sem moralizar e sem explicar a causa. O próprio avaliador externo escreveu que "a omissão da causa não é necessariamente um defeito". O argumento de convencionalidade se apoia em recorrência (luz acesa para quem não volta), não em um defeito textual. Quatro execuções do Crítico aprovaram.
- W19 AMBÍGUA. O comportamento concreto (molhar-se por uma semana) é forte. O defeito localizável é a oração final, que explica o sentido com uma metáfora, e ela é separável do restante do texto. Isso é diferente de um item sem comportamento concreto. Um avaliador mais flexível trataria como correção pontual, não como falha estrutural.
- Em sentido contrário, uma leitura mais severa colocaria os três como RUIM ou AMBÍGUA, por dependerem da mesma premissa de luto, e a diferença entre eles seria só de execução.

## B4. A distinção resiste sem adjetivos subjetivos?

Em parte. Demonstráveis no texto: (1) W05 tem uma sequência com mudança de conduta depois de um erro, e W15 e W19 não; (2) a lógica do gesto de W05 é literal e a de W19 é figurada; (3) em W19 a oração final explica o sentido e é separável, em W15 o sentido fica implícito; (4) W19 e W05 têm atrito concreto, W15 menos.
Não demonstráveis sem preferência: a raridade do gesto (luz acesa contra alisar a manta contra molhar-se); se uma incoerência entre ato e fala em W15 é um traço humano específico ou outra convenção; se uma premissa convencional com gesto menos convencional basta para BOA.
Observação: o que é demonstrável favorece a distinção entre W05 e W19 (lógica literal contra figurada, oração explicativa) com mais clareza do que a distinção entre W05 e W15. Nesse par, o contraste demonstrável é a sequência com aprendizagem, e é fraco para sustentar RUIM sozinho.

## B5. O rótulo anterior pode ser discutível?

Sim, em graus diferentes.
- W15 é o mais discutível: a referência externa o reprova por convencionalidade, e a nota sobre omissão concede que ela não é defeito. O texto contém um traço (diz que esqueceu) que a avaliação externa não discute.
- W19 é discutível entre RUIM e AMBÍGUA, pela separabilidade da oração final.
- W05 é discutível entre BOA e AMBÍGUA, pelas razões de B3.
Isto é, a assimetria entre os três pode ser real, mas a evidência textual não a prova; ela se apoia em um critério de raridade que ainda não foi formulado.

## B6. Questões editoriais ainda não resolvidas

1. A convencionalidade da premissa (luto, ausência) deve pesar mais do que o gesto, ou o gesto decide?
2. Um comportamento concreto cuja explicação é uma metáfora de perda continua RUIM, ou vira AMBÍGUA (correção pontual) quando a metáfora é separável?
3. Ato desmentido por fala (W15) conta como detalhe específico e humano, ou é ele próprio uma convenção da ausência?
4. Quando um mecanismo físico tem tensão (lavar o cheiro, alisar a forma), o critério é a intenção declarada do personagem, ou a leitura mais natural? W08 e W05 recebem hoje tratamentos opostos.
5. A raridade do gesto pode ser um critério usado sem um corpus de referência? Quem é o árbitro: Eri, um segundo avaliador, ou a comparação com publicações já feitas?
6. AMBÍGUA permite publicação depois de ajuste mínimo, ou sempre exige nova avaliação completa?
7. Os três deveriam ser avaliados novamente por outro avaliador independente antes de qualquer decisão? (Pergunta de procedimento; não é solicitação de execução.)

## B7. Descoberta exploratória sobre origem (registro, decisão 6)

12 das 14 aprovações indevidas de RUIM ficaram concentradas nos itens do grupo do cronista livre (W08, W15, W17, W19, W21). A análise por origem foi feita depois dos resultados e a amostra é pequena (30 itens, 3 origens, 10 por origem). Não se conclui que esse processo de criação seja inferior nem que retirá-lo resolveria o problema. Os três itens deste documento pertencem a esse grupo (W05, W15, W19), o que reforça que a questão aqui é a mesma da concentração: a dificuldade se concentra em textos fluentes e plausíveis com premissa de ausência.

## B8. Limitações

Análise feita pelo mesmo modelo que gerou os itens e os Críticos; um único avaliador externo (ChatGPT) e a posição de Eri como segunda referência; sem corpus para medir raridade; três itens apenas; os registros dos Críticos são auto-justificativas e não medidas independentes; os juízos J acima são meus e podem ser contestados.
