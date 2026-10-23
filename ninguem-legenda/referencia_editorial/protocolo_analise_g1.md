# Protocolo de análise da comparação G3, revisão 1 (PROPOSTA para nova revisão de Eri)

Data: 22/10/2026. Etapa G0, revisão conforme as decisões de Eri de 23h55. Não está lacrado nem congelado: só será lacrado por hash no marco M1, com autorização expressa. Nada foi executado. Os números marcados como proposta dependem de decisão de Eri.

## 1. Escopo e condições

Versões comparadas: v2.4-exp (candidata), v2.2 (controle principal), v2.3-exp (controle secundário, só enquanto não for a candidata), com prompts, registros e resultados históricos dos controles inalterados. Mesmos 60 itens inéditos (30 de fluxo e 30 de desafio, sempre analisados separadamente), mesmo pacote (instrumentos_g1/montar_pacotes.py), mesmo modelo e configuração, três execuções por versão, códigos e ordem embaralhados de forma independente por execução e por versão, contextos isolados, execuções das três versões feitas juntas e não reaproveitadas de experimentos anteriores. Falha técnica (formato inválido, truncamento) pode ser reexecutada uma vez, com o mesmo prompt e o motivo registrado. Todas as execuções entram na análise. Nenhuma execução favorável é selecionada retrospectivamente.

Referência: rótulos do ChatGPT para os 60 itens; itens com conflito de triagem e amostra de controle (20% dos sem conflito, mínimo de 10) classificados por Eri às cegas e confrontados; divergências examinadas por Eri conforme a seção 2.3 do plano rev2. A referência não é verdade absoluta. Itens em divergência legítima formam a zona contestada e nunca entram como consenso. Correspondência: BOA, APROVADA; AMBÍGUA, REVISAR; RUIM, REPROVADA, em princípio.

## 2. Dois registros por avaliação (decisão 3)

A. Veredicto bruto: APROVADA, REVISAR ou REPROVADA.
B. Elegibilidade automática: APROVADA sem divergência material declarada. Nas versões v2.2 e v2.3-exp, que não têm o campo, toda APROVADA é elegível automaticamente. Na candidata, o campo elegibilidade_automatica é verificado pelo validador contra o veredicto e a divergência.

O relatório mostra sempre os dois, por camada de erro, por versão, por execução e por estrato. Nenhuma versão pode ser apresentada como superior apenas porque classificou aprovações duvidosas como divergência legítima: uma melhora que apareça só na elegibilidade automática, e não no veredicto bruto, é descrita como "melhora condicionada a divergências declaradas" e não sustenta a conclusão B.

Controle das divergências declaradas:
- O alarme exploratório de 20% de itens com divergência material declarada não é limite seguro nem autoriza declarar divergências até esse percentual.
- Toda divergência declarada é fundamentada (duas interpretações, cada uma com trecho) e verificada pelo julgador de motivos quanto a serem realmente defensáveis e materiais (APROVADA contra outro estado).
- Avaliação qualitativa, caso a caso: o relatório apresenta todos os itens em que a candidata alterou a elegibilidade automática em relação ao próprio veredicto bruto (APROVADA bruta com elegibilidade negada), com o texto da divergência, o estado de referência e o parecer do julgador.
- Monitoramento particular das declarações concentradas em itens de referência RUIM, em sentimentalismo implícito e em propostas sem segunda leitura, informando contagem e identidade dos itens.
- Objeções "nao_demonstrada" (falha que o Crítico não conseguiu demonstrar) são reportadas à parte, item a item, com o parecer do julgador sobre se a falha alegada é sustentada pelo texto. Não são tratadas como preferência.

## 3. Camadas de erro, reportadas separadamente, sem índice global

1. Aprovar (veredicto bruto e elegibilidade automática) item de referência RUIM não contestado.
2. Aprovar item de referência AMBÍGUA, ou item contestado sem reconhecer a contestação.
3. Reprovar ou inventar defeito em item BOA.
4. Confundir REVISAR e REPROVADA.
5. Veredicto correto com motivo errado.

As camadas 1 e 3 são ambas relevantes para a confiabilidade editorial: não são idênticas, mas são preservadas separadamente, sem compensação matemática entre elas. Cada camada é reportada por versão, por execução, por estrato (fluxo e desafio, e no desafio por célula de intenção e por classe real) e por item. Contagens com intervalos, nunca só percentuais. Fluxo e desafio nunca entram num número único.

## 4. Critério de melhoria e de piora (refinado)

Princípio: comparação pareada dos mesmos itens. A decisão não usa a maior oscilação entre execuções como limiar estatístico universal, que pode ser conservadora demais num caso e enganosa noutro. A oscilação interna de cada versão é reportada como evidência de instabilidade, e não é convertida automaticamente em prova nem em refutação de superioridade.

Ordem de prioridade da leitura:
1. comparação dos mesmos itens entre candidata e controles;
2. quantidade e identidade dos itens corrigidos;
3. quantidade e identidade dos itens piorados;
4. gravidade editorial dessas mudanças (camadas da seção 3);
5. comportamento nas três execuções (padrões 3 de 3 e 2 de 3 por item);
6. consistência das justificativas (motivos CORRETO, PARCIAL, ERRADO);
7. análise separada de fluxo e desafio.

Item corrigido: o controle erra e a candidata acerta com motivo CORRETO em pelo menos duas das três execuções. Item piorado: o inverso. Correção com motivo ERRADO ou PARCIAL é registrada, mas não conta como correção plena. Classificação de cada dimensão: "melhora" quando, nas três execuções, os itens corrigidos superam os piorados na camada considerada, as correções e as pioras estão identificadas uma a uma, e o conjunto de pioras não é mais grave que o de correções; "piora" é a regra simétrica; "sem diferença distinguível" quando o quadro é misto ou pequeno; "inconclusivo" quando há falha metodológica. Diferença que dependa de um único item é descrita como tal. A classificação final de cada dimensão é registrada com a lista de itens e submetida a Eri. Mesmos critérios, em sentido simétrico, para melhoria e piora. Nenhum índice global.

Piora grave nas camadas 1 e 3 (proposta, Eri ajusta): pelo menos um item dessas camadas que o controle acertava em duas ou mais execuções e que a candidata erra em duas ou mais, ou aumento líquido de erros na camada em todas as execuções. Piora grave em qualquer das duas camadas impede a conclusão B, com o mesmo peso.

## 5. Dimensões

(1) camada 1; (2) camada 2; (3) camada 3 e defeitos inventados em BOA; (4) trocas entre aprovar e não aprovar entre execuções do mesmo item; (5) qualidade das justificativas; (6) controles especiais; (7) estrato de sentimentalismo implícito; (8) sem piora onde o controle já acertava. As dimensões não são oito condições absolutas: são lidas uma a uma.

### 5.1 Qualidade das justificativas (dimensão 5)

Quatro categorias do julgador, sempre separadas: CORRETO, PARCIAL, ERRADO, INCONCLUSIVO. PARCIAL não vale como CORRETO e é informado à parte, sem completar o percentual de acertos. Limiar operacional inicial para a conclusão B: pelo menos 80% de CORRETO entre as avaliações conclusivas (excluídas as INCONCLUSIVO), nas duas amostras examinadas separadamente. É uma exigência editorial prévia, não demonstração estatística de segurança. A conclusão B também exige comparação com o controle: não basta alcançar 80% se a candidata não melhora efetivamente em relação a ele. Definição de cálculo (proposta): por amostra, sobre as avaliações das três execuções reunidas, com o percentual de cada execução também apresentado e qualquer execução muito abaixo sinalizada. Aprovações indevidas sustentadas por justificativas claramente falsas recebem destaque próprio, item a item, independentemente do percentual agregado.

Julgador: prompts/julgador_motivos_v1_rascunho.md (verificação factual antes da ficha; não considera correta uma justificativa por usar termos da referência; verifica as afirmações contra a fotografia prevista e o texto). Auditoria humana de pelo menos 20% das avaliações, mínimo de 10, com seleção definida antes: sorteio por semente de Eri (sal "g3-auditoria-julgador") mais cobertura de cada combinação de versão e veredicto e dos motivos ERRADO e INCONCLUSIVO quando existirem. Se a confiabilidade do julgador não for demonstrada na auditoria (erro sistemático), a dimensão 5 é INCONCLUSIVA. O limite de 15% de avaliações INCONCLUSIVAS é alarme metodológico, não tolerância: concentração numa categoria, origem ou tipo de defeito pode invalidar a conclusão correspondente mesmo abaixo de 15%.

### 5.2 Itens contestados

Não se mede concordância com um dos lados. Segundo o julgador: o Crítico apresenta interpretação defensável? identifica a natureza do fundamento (A, B ou C)? reconhece a dúvida material quando existe, sem divergência vazia? Nas versões sem o campo de divergência, o reconhecimento só pode ser avaliado pelo texto da justificativa.

### 5.3 Controles especiais (dimensão 6)

Não se elimina a dimensão 6. Sem os controles especiais, o experimento fica limitado à conclusão A (continuar investigando), com no máximo indicação provisória de melhoria. Plano, sujeito a autorização específica posterior e sem geração agora:
- um pequeno lote independente de controles especiais, produzido depois do M1 e antes da G3;
- regras, categorias, critérios de inclusão e tratamento dos resultados congelados por hash antes da produção dos itens (marco próprio, a ser definido);
- os itens dos controles não podem ser conhecidos pelo redator da candidata antes do M1. Limitação declarada: o redator conhece o desenho conceitual dos cinco tipos (seção 11 do plano rev2), mas nenhum item existe;
- os controles não se misturam aos 30 itens de fluxo nem aos 30 de desafio e têm análise própria;
- passam pela mesma rotulagem independente e pelas mesmas condições de execução.

## 6. Decisões possíveis ao final (sem homologar)

- A, continuar investigando: evidência parcial, mecanismos de erro compreendidos, hipótese plausível, mesmo com dimensões inconclusivas ou não avaliadas. Pode vir com indicação provisória de melhoria.
- B, considerar a candidata superior. Exige, juntas: melhora relevante, consistente e fundamentada sobre o controle principal, lida nas duas amostras separadamente; nenhuma piora grave na camada 1 nem na camada 3, ambas com o mesmo peso e sem compensação entre si; pelo menos 80% de motivos CORRETOS entre as conclusivas em cada amostra, com melhora sobre o controle; dimensão 5 conclusiva (julgador auditado); dimensão 6 avaliada e sem queda; relatório dos dois registros (bruto e elegibilidade) sem melhora apenas por divergências declaradas.
- C, homologar para publicação autônoma: fora do alcance deste experimento.
Sinais de reconsideração (alertas diagnósticos, sem gatilho automático): melhora dentro do ruído; sentimentalismo continuando a passar; mérito mal demonstrado; trocas entre aprovar e não aprovar tão frequentes quanto antes; motivos majoritariamente errados com justificativas fluentes; Crítico seguindo um único avaliador; divergência usada como escudo; aprovação de itens limpos e vazios (quando os controles existirem). Qualquer alerta pede diagnóstico escrito e decisão de Eri, e pode apontar para mudar a estratégia, inclusive a geração dos candidatos, e não para uma v2.5.

O experimento deve mostrar melhora, igualdade e piora com a mesma clareza: os critérios acima são simétricos e a piora da candidata em qualquer camada tem o mesmo destaque que a melhora.

## 7. Comparabilidade com as versões anteriores (decisão 8)

A v2.4-exp não tem os campos evidencias_positivas, defeitos_demonstrados, eliminatorias e nota, e acrescenta leitura_inicial, merito, objecoes, nucleo, divergencia_legitima e elegibilidade_automatica. Os campos antigos e novos não são comparáveis diretamente. A comparação ocorre por veredictos brutos, decisões de elegibilidade e justificativas verificáveis (julgador e auditoria), nunca por contagem de defeitos nem por nota.

## 8. Cláusula de inferência para o relatório final, antes dos resultados

As amostras são pequenas; os resultados dependem dos modelos usados; a subjetividade editorial legítima não desaparece; avaliadores podem errar; as execuções repetidas são correlacionadas; consistência não é correção; concordância com o ChatGPT não é prova de qualidade; uma pequena redução percentual de erros não demonstra superioridade; três execuções não provam estabilidade; os 80% de motivos corretos são exigência editorial prévia, não demonstração estatística. O conjunto não pode ser descrito como inacessível ao redator: as proteções (ordem cronológica, hashes, registros de acesso e uso único) dão integridade documental e auditoria parcial, não prova de ausência de acesso.
