# G1: proteção do conjunto de validação

Data: 22/10/2026. Fase A. Procedimento documental. Nada foi gerado nem executado. Atende à decisão 5 de Eri (23h34): o conjunto de validação não pode influenciar, direta ou indiretamente, a elaboração ou o ajuste da versão candidata.

## 1. Limitação do ambiente, declarada antes da geração

Neste ambiente não existe isolamento confiável por processo ou por acesso. Em concreto:
- uma única sessão (a minha) orquestra tudo: redige prompts, cria pacotes, lança subagentes, recebe os resultados e recebe, pelo chat, os rótulos que Eri traz do ChatGPT;
- os subagentes compartilham o mesmo sistema de arquivos e a mesma família de modelo do Criador, do Crítico, dos preditores e do julgador;
- o repositório é acessível por qualquer sessão futura, e não há custódia criptográfica com chave em poder de Eri;
- eu não consigo provar a ausência de acesso, só registrar os acessos que declaro. O registro é autodeclarado.

Por isso, simples embaralhamento de códigos não é tratado como garantia de independência (ele só evita viés de ordem). A proteção abaixo se apoia em quatro mecanismos que não dependem de eu me comportar bem: ordem dos eventos, prova por hash e por registro externo ao ambiente, verificação mecânica de vazamento e uso único. O que sobra de risco está na seção 5.

## 2. Procedimento, correspondendo aos seis pontos de Eri

### Ponto 1. O redator da versão candidata não terá acesso aos 60 itens

Mecanismo: congelar antes de existir. O conjunto de versões sob teste (candidata e controles) é declarado e congelado antes de qualquer item de validação existir. Quem redige a candidata não pode ter visto o que ainda não foi produzido.
- Se a candidata for uma versão já existente (v2.2, v2.3-exp ou outra), ela já está congelada por hash (9910c786…, 468fd382…, 74bc6f3a…) e o ponto está satisfeito por construção.
- Se Eri autorizar uma candidata nova, ela é redigida, travada por hash e publicada ANTES da autorização da G1. A G1 só começa depois do marco de congelamento (seção 3).
- Depois do marco, nenhuma versão do conjunto declarado pode ser criada nem alterada para este lote. Alterar qualquer uma queima o lote para a versão alterada, e o novo teste exige outro lote.
- Reforço opcional, que só Eri pode providenciar: redigir a candidata numa conversa separada, sem acesso a esta pasta. Eu não posso impor isso.

### Ponto 2. Os itens não entram em prompts, exemplos, históricos nem materiais de calibração

- Os itens ficam numa pasta própria, `validacao_g1/`, fora de `prompts/`, `calibracao/` e `lote/`, com um aviso de leitura restrita e um manifesto com SHA-256 de cada item.
- O gerador dos itens (subagentes do Criador, usando o `prompts/criador.md` atual e sem alteração) recebe somente o conceito fotográfico e o prompt do Criador. Não recebe texto de nenhuma versão candidata, critério do Crítico, rótulo, exemplo da referência editorial nem item de outro conjunto.
- Verificação mecânica de vazamento, a ser implementada na G1 e rodada em dois momentos (antes do marco de congelamento das versões e antes da G3): varredura de `prompts/`, `calibracao/`, `lote/`, `referencia_editorial/` e `README.md` procurando o texto de qualquer item (frase por frase, normalizado) e os hashes do manifesto. Qualquer ocorrência bloqueia a etapa e é registrada como possível contaminação.
- Os itens de validação não entram no registro de memória editorial usado pelo Criador (`registro.csv`) até a conclusão da comparação, para não influenciar gerações futuras.

### Ponto 3. A candidata é congelada antes de os responsáveis acessarem os itens

- Marco de congelamento: um arquivo `marco_congelamento_g1.json` com o hash de cada versão do conjunto, o hash do protocolo de análise e a data, commitado e publicado antes de a pasta `validacao_g1/` existir.
- Evidência independente do meu relógio: o horário de recebimento do push no GitHub (eventos do repositório) comparado com o do commit dos itens. Eri pode conferir pelo histórico do repositório. A ordem exigida é: marco de congelamento, depois lista sorteada, depois itens.
- Os hashes são recalculados e comparados com o marco no início da G3. Divergência invalida o lote.

### Ponto 4. A rotulagem externa não expõe rótulos aos Críticos nem ao desenvolvimento

Sequência obrigatória: itens congelados por hash; predições cegas de triagem dos subagentes Claude, lacradas por hash; pacote cego para o ChatGPT (somente conceito, texto e contexto da série, códigos opacos); rótulos devolvidos por Eri e lacrados por hash no mesmo turno em que chegam; conflitos de triagem calculados; classificação humana; só então a execução dos Críticos.
- Subagentes Críticos, preditores e julgador recebem apenas o seu pacote por caminho de arquivo. Rótulos, predições alheias e mapas de procedência ficam em pastas que não constam de nenhum pacote.
- Os rótulos chegam à minha sessão porque Eri os cola no chat. É uma exposição inevitável neste ambiente. Ela não pode alimentar o desenvolvimento, porque as versões estão congeladas e o protocolo de análise está lacrado antes. Registra-se que o orquestrador viu os rótulos antes das execuções.
- A classificação humana ocorre sem conhecimento prévio de rótulos e de predições: Eri recebe os itens selecionados por conflito e os sorteados para controle num único pacote misturado, sem indicação de qual é qual e sem rótulo do ChatGPT nem predição. O confronto só vem depois que a classificação dela estiver lacrada.

### Ponto 5. Uso único

- `validacao_g1/USO.json` registra o estado do lote: reservado, congelado, rotulado, executado, queimado.
- A comparação autorizada (três execuções por versão do conjunto declarado, mais uma reexecução técnica por falha de formato, com o mesmo prompt e o motivo registrado) é feita uma única vez. Ao terminar, o lote passa a "queimado" e o hash dos resultados é lacrado.
- Qualquer execução adicional com os mesmos itens exige autorização nova, é rotulada como exploratória e não conta como validação. Uma candidata alterada depois dos resultados não pode usar este lote.

### Ponto 6. Acesso indevido é registrado e tratado como possível contaminação

- `registro_acessos_g1.jsonl` recebe uma linha para cada leitura dos itens ou dos rótulos: quem ou o que leu, quando, para qual passo declarado (montar pacote, lacrar, triagem, execução de Crítico por pacote, decodificação, auditoria). Os passos declarados são os do ponto 4.
- Qualquer leitura fora dos passos declarados, antes do marco de congelamento ou por quem redige versões, é anotada como possível contaminação, com a avaliação do efeito: se ocorreu antes do congelamento de uma versão, o lote fica queimado para essa versão; se depois, os itens afetados ficam marcados e a análise é refeita com e sem eles.
- O registro é autodeclarado. Seu valor está em permitir que Eri e qualquer leitor do histórico do repositório vejam o que foi feito, não em impedir o acesso.

## 3. Marcos e ordem de eventos

M0, aprovação de Eri da lista e do procedimento. M1, versões do conjunto declaradas e congeladas, protocolo de análise lacrado, marco publicado. M2, frase-semente de Eri e sorteio dos conceitos, registro publicado. M3, geração dos textos (G1), manifesto dos itens por hash. M4, varredura de vazamento limpa. M5, triagem lacrada, pacote cego ao ChatGPT, rótulos lacrados. M6, classificação humana lacrada e confronto. M7, execuções (G3). M8, lote queimado e resultados lacrados.
Cada passagem exige a autorização expressa de Eri que o plano já prevê, e nenhuma é iniciada por minha iniciativa.

## 4. Alternativa em caso de isolamento insuficiente

Esta é a alternativa, e é o que adotarei se Eri aprovar: a proteção por ordem, hash, varredura e uso único acima, com a limitação da seção 1 escrita no relatório final. Se Eri considerar insuficiente, as variantes mais fortes dependem de recursos que só ela controla: (a) candidata redigida em conversa separada sem acesso à pasta de validação; (b) cópia dos itens custodiada por Eri e entregue só no momento das execuções; (c) um segundo redator ou revisor humano que verifique o marco e o log. Nenhuma delas é pressuposta.

## 5. Riscos que permanecem, e como as conclusões devem tratá-los

- Eu conheço o material queimado anterior (W01 a W30, arbitragens, referência editorial). Isso já faz parte do desenvolvimento e não é contaminação do lote novo, mas significa que a candidata não é "cega" a este tipo de texto.
- O Criador, o Crítico, os preditores e o julgador são da mesma família. Erros correlacionados podem existir sem aparecer no isolamento formal.
- Um acesso não declarado não seria detectado. A verificação mecânica de vazamento só pega texto copiado, não influência indireta de memória.
- Depois de usado, o lote não valida mais nenhuma candidata desenvolvida com conhecimento dos seus resultados. Uma nova candidata exige novo lote.
O relatório final registrará essas limitações junto com a cláusula de inferência já adotada.
