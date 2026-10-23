# Diagnóstico qualitativo das falhas do Crítico (v2.2 e v2.3-exp), Fase A

Data: 22/10/2026. Análise feita exclusivamente sobre registros já existentes (conjunto/resultados/ e rótulos externos). Nenhum Crítico foi reexecutado, nenhum prompt, rótulo ou item foi alterado, nenhuma alternativa foi implementada e nenhuma v2.4 é proposta. Decisões de Eri registradas (22/10/2026): não homologar nenhuma versão; suspender novas versões, camadas de agentes e sistemas de pontuação; autorizar apenas este diagnóstico; não reexecutar o julgador de motivos.

## 0. Ressalvas de leitura

- Limitação do julgador de motivos, registrada expressamente: o julgador isolado recebeu o NA FOTO, o FORA e o motivo externo, mas não a descrição da foto nem os textos anteriores. As contagens de defeitos "inventados" ou "não verificáveis" que ele produziu não são medidas confiáveis e não são usadas neste diagnóstico. Suas classificações de correspondência (coincide, em parte, não coincide) são usadas só de forma descritiva.
- Procedimento aberto agora: o mapa de origens (O1, O2, O3) foi aberto depois dos resultados, para esta análise. Isso não altera nenhum veredicto.
- Quem analisa é o mesmo modelo que gerou itens e Críticos. Isso é uma fonte de viés possível, especialmente na hipótese E.
- Tudo abaixo é descritivo e conta com 30 itens, 4 AMBÍGUA, 2 execuções por versão e um único avaliador externo.

## 1. Onde as falhas estão (achado central)

Os Críticos reprovam com segurança texto fraco, aprovam com segurança texto bom e falham numa zona estreita.

| Origem dos itens | Rótulos externos | RUIM aprovada (execuções) |
|---|---|---|
| O1, Criador do projeto | 9 BOA, 1 RUIM | 0 de 4 |
| O3, rascunhos rápidos | 9 RUIM, 1 AMBÍGUA | 2 de 36 (W16, W25) |
| O2, cronista livre | 1 BOA, 6 RUIM, 3 AMBÍGUA | 12 de 24 |

12 das 14 aprovações indevidas de RUIM vêm de O2: textos fluentes, plausíveis, com detalhe concreto, quase todos sobre ausência ou saudade ligada a um objeto (W08, W11, W15, W17, W19, W21). Nenhuma BOA do Criador do projeto foi ameaçada, e rascunhos fracos foram rejeitados. A dificuldade real é distinguir excelência de uma aparência de profundidade bem escrita, que é o que Eri descreveu.

Cautela: a boa concordância em O1 pode refletir que o Criador e o Crítico foram escritos sob as mesmas regras, não que o Crítico seja bom em geral.

## 2. Padrões de erro pedidos

### 2.1 Sentimentalismo confundido com profundidade
Evidência: o campo nomeia_emocao_sem_fato foi verdadeiro em 15 de 27 reprovações de RUIM e em 0 dos 14 RUIM aprovados e em 0 dos 40 BOA aprovados. O Crítico opera "sentimentalismo" como emoção nomeada ("A saudade senta ali"), não como construção sentimental convencional por objeto. W15 (luz acesa para o filho que não volta), W19 (guarda-chuva do marido), W17 (cadeira reservada), W21 (carregador ligado) passam porque a emoção fica implícita num objeto. A avaliação externa os reprova como sentimentalismo convencional. W16 (v2.2 e1) aprovou "É o único abraço que coube antes do portão" registrando só que é "figurado", em observação descartada, enquanto o motivo externo é justamente "sentimentalismo metafórico".

### 2.2 Complementação de contexto confundida com segunda leitura
Evidência: o campo elemento_que_muda do Crítico fixa uma "leitura inicial" que não coincide com a que os leitores cegos formaram. Em W15, os três leitores previram "luz acesa esperando um filho que não voltou" (captura 3 de 3). O Crítico descreve a leitura inicial como "quarto ocupado" (v2.3 e2) ou "esquecimento comum" (v2.2 e1) e conta como transformação o que o FORA acrescenta. Padrão idêntico em W19 ("objeto esquecido"), W21 ("objeto esquecido") e W17. A transformação real em relação ao que o leitor já inferiu é só o detalhe adicional ("diz que esqueceu", "se molha"), isto é, complemento de contexto. A previsão cega foi corretamente rebaixada de gatilho de REVISAR, mas deixou de ser a âncora empírica de "leitura inicial", e nenhum mecanismo ocupou esse lugar.

### 2.3 Detalhe específico confundido com originalidade
Evidência: a cláusula "associação comum com perspectiva específica pode ser aprovada" foi satisfeita pelos dois tipos de caso com o mesmo raciocínio. W05 (BOA), W12 (BOA), W29 (BOA) e W15, W19, W08 (RUIM) foram aprovados por "a associação comum é transformada por um gesto concreto". Indicadores do próprio Crítico para W05 e W15: captura média 3,0 em ambos, associação comum "sim" nas 4 execuções em ambos, aprovados nas 4 em ambos. As justificativas citadas ("alisar para não apagar o formato dele"; "apagar todas as luzes menos essa e dizer que esqueceu") têm a mesma forma. Os indicadores que o Crítico produz não discriminam os dois. Isso também mostra uma tensão real: a cláusula que protege as BOA (W05, W12, W29) é a mesma que deixa passar W15 e W19. Apertá-la sem critério de qualidade do gesto tende a custar BOA.
Aviso sobre a referência: o motivo externo de W05 ("comportamento concreto") vale igualmente para W15 ("diz que esqueceu"). Os critérios declarados pelo avaliador externo não explicam a diferença; ela parece repousar em raridade do gesto, uma percepção holística. Isso pode ser um critério legítimo, mas também pode ser variação do avaliador. A decisão sobre qual das leituras vale é editorial e é de Eri.

### 2.4 Sutileza confundida com obscuridade (e o inverso)
Evidência: nos dois sentidos. (a) Omissões tratadas como sutileza onde a avaliação externa vê dependência de pressupostos: em W24 as duas execuções da v2.3-exp responderam à pergunta "o ausente é necessário?" com "Não." e "Não necessário.", sem demonstração; as duas versões tinham classificado o mesmo ("Não se diz se o pai morreu") como omissão legítima e aprovaram o item nas quatro execuções. (b) Em W27 (referente de "ela sobrou"), a avaliação externa aponta causalidade e formulação confusas; a v2.2 e1 reconheceu a ambiguidade de referência, mas a v2.3-exp e1 e a v2.2 e2 foram a clichê, e as quatro ficaram em REVISAR. O Teste de Integridade, quando preenchido, é respondido pelo próprio Crítico em linhas curtas e favoráveis, sem verificação.

### 2.5 Falhas centrais classificadas como periféricas
Evidência: seção 3 do relatório comparativo (W08 e1, W21 e1, W25 e1, W30 e1 e e2). O padrão existe também na v2.2, sob outro nome: observações descartadas. Em v2.2 e1 o Crítico registrou para W08 "lavar tira o cheiro dele", para W21 "esperando a bateria soa confuso", para W16 "é figurado", para W09 "param admite duas leituras", e aprovou. Ou seja: o Crítico VÊ o defeito e não o PESA. A regra de materialidade exige demonstrar a importância de um defeito que bloqueia; não exige justificar a dispensa de um defeito percebido. Em W25 a v2.3-exp e1 escreveu "sem peso para a leitura central" sobre o que era a revelação inteira.

### 2.6 Inconsistências entre avaliações do mesmo conteúdo
Evidência: a mesma observação é descartada numa execução e elevada a defeito noutra. v2.2: W16 ("é figurado" descartado em e1; perda_segunda_leitura sobre a mesma frase em e2); W17 ("tema recorrente" descartado em e1; redundância e clichê em e2); W21 ("esperando a bateria" descartado em e1; defeito em e2); W08 (tensão do cheiro descartada em e1; citada em e2). v2.3-exp: W25 (B em e1, clichê C em e2); W19 (C em e1, B em e2). Também há instabilidade de classe: W03, W10, W11 receberam C numa execução e D noutra para o mesmo texto. As instruções são as mesmas; o que muda é o peso dado a evidência idêntica.

## 3. Hipóteses de Eri (A a E), avaliadas sem presumir

A. Critérios insuficientemente definidos. Apoio forte. Sentimentalismo operacionalizado como emoção nomeada (2.1); "leitura inicial" sem âncora (2.2); "perspectiva específica" sem critério de qualidade do gesto (2.3); ausência de regra para justificar a dispensa de uma imperfeição percebida (2.5). Contra: a v2.3-exp acrescentou critérios e a instabilidade subiu.

B. Aplicação inconsistente de critérios adequados. Apoio forte para parte dos casos. Mesma evidência pesada de modos diferentes (2.6); classes C e D trocadas para o mesmo texto. Mas não explica os erros sistemáticos: W15 foi aprovado nas quatro execuções, ou seja, aplicado de forma consistente, e errado segundo a referência. A e B coexistem.

C. Tendência do modelo a valorizar sentimentalismo. Apoio parcial e ambíguo. Textos sentimentais explícitos (W01, W03, W04) foram reprovados; os que passam são os de sentimentalismo implícito num objeto. Isso é compatível com uma tendência a tratar o familiar como legítimo, mas também com a definição estreita de A. Registros não separam as duas. A concentração em O2 (12 de 14) sugere um ponto cego de gênero e não uma preferência por emoção em geral.

D. Dificuldade em reconhecer transformações narrativas originais. Apoio plausível, não demonstrado. Todas as 10 BOA foram aprovadas, então originais evidentes são reconhecidos. O que o Crítico não faz é graduar a raridade do gesto (W05 contra W15). As previsões cegas capturam a premissa, não o gesto, e por isso não ajudam aqui. Dependência da referência: ver aviso em 2.3.

E. Limitações da arquitetura de autoavaliação. Apoio moderado, com cautela. O Crítico produz justificativas fluentes e internamente coerentes para aprovações que a referência rejeita (W15, W19), e o validador só verifica coerência interna, não verdade. O mesmo modelo que escreve os itens (O2) e os julga compartilha o repertório do que é "natural" e "familiar". A variação entre execuções idênticas (v2.2: 6 e 2 RUIM aprovadas) mostra um ruído de amostragem que nenhuma instrução elimina. Não posso testar isso sem uma referência independente adicional.

Síntese honesta: A e B são os mais bem sustentados e são, em princípio, corrigíveis por instruções. C e D não se distinguem de A com estes registros. E é plausível e estrutural. A tentativa mais recente de corrigir por instruções (v2.2 para v2.3-exp) não trouxe ganho medido, o que é um indício, não uma prova, de retornos decrescentes.

## 4. Casos prioritários como exemplos de falhas reais

- W15 e W19: aprovados com indicadores (captura 3, associação comum sim) idênticos aos de uma BOA (W05). A falha é de critério (2.3, 2.1, 2.2), não de omissão do Crítico: ele identificou corretamente a associação comum e a "transformou" por um detalhe.
- W08: o Crítico reconheceu a incompatibilidade (v2.3-exp e1: "lavar não preserva o cheiro dele") e a dispensou com "a leitura poética sustenta". O procedimento de contradição nunca foi acionado, porque a incompatibilidade foi enquadrada como imprecisão, não como contradição.
- W30: a v2.2 demonstrou o defeito ("uma casa sem ovos e café por meses é pouco plausível") nas duas execuções; a v2.3-exp registrou a mesma observação como B ("lê-se como itens da lista não repostos"), com a interpretação alternativa que o ajuste 2 manda procurar, mas aplicada a plausibilidade e não a contradição. Um possível efeito colateral do ajuste 2, não demonstrado: a busca por alternativa natural pode ter deslocado o Crítico para a leitura benigna em geral.

## 5. Alternativas possíveis para o próximo estágio (nenhuma implementada)

1. Corrigir por instruções, de forma estreita: definir sentimentalismo para além da emoção nomeada; exigir que a "leitura inicial" venha das previsões cegas; exigir justificativa para cada observação descartada. Prós: baixo custo. Contras: v2.2 para v2.3-exp já mostrou que mais critérios podem aumentar a variância; a tensão BOA contra RUIM na cláusula da associação comum permanece.
2. Reduzir a ambição do Crítico: usá-lo para reprovar com segurança (onde foi confiável) e para encaminhar à decisão humana tudo o que não for claramente excelente. Prós: usa o que funciona (10 de 10 BOA preservadas, rascunhos fracos rejeitados). Contras: a aprovação autônoma, objetivo da skill, deixa de existir.
3. Resolver a referência antes: pedir a Eri que decida, com suas próprias palavras, o que separa W05 de W15 e W19, ou obter um segundo avaliador independente. Sem esse critério editorial estável, qualquer ajuste treina o sistema para concordar com um único modelo, o que Eri quer evitar.
4. Quebrar a autoavaliação por um julgador de outra família de modelos ou por mais de uma amostra, apenas na decisão de aprovar. Prós: ataca E e o ruído. Contras: custo, complexidade, risco de nova camada que Eri quer evitar.
5. Atacar a geração em vez do julgamento: o Criador do projeto produziu 9 BOA em 10; investir em restrições na geração pode reduzir a dependência do Crítico. Contra: amostra pequena, e a vantagem de O1 pode vir da proximidade com as regras do Crítico.
6. Medir antes de mudar: repetir o conjunto com outras duas execuções por versão para estimar o ruído (esclarece B contra E). Contra: não resolve A.

Nenhuma delas é recomendada aqui. A pergunta aberta de Eri (problema corrigível por instruções ou reconsiderar a estratégia) parece ter resposta mista: parte corrigível (A, B), parte estrutural (E, e a dependência da referência).

## 6. Limitações da análise

Uma única referência externa, também um modelo, cujos rótulos de W15 e W19 repousam em convencionalidade e não em defeito textual objetivo; 4 AMBÍGUA; 2 execuções por versão; análise post hoc pelo mesmo modelo; mapa de origens aberto depois dos resultados; julgador de motivos com contexto incompleto; a concentração em O2 pode refletir o gênero que aquele processo de criação favorece (ausência com objeto), não uma propriedade geral do Crítico.
