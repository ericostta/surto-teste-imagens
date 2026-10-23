# Protocolo de análise da comparação G3 (PROPOSTA para revisão de Eri)

Data: 22/10/2026. Etapa G0. Rascunho. Não está lacrado nem congelado: só será lacrado por hash no marco M1, com autorização expressa de Eri. Nada foi executado. Os números abaixo são propostas a decidir por Eri, e estão marcados como tal.

## 1. Escopo e condições

Versões comparadas: v2.4-exp (candidata), v2.2 (controle principal), v2.3-exp (controle secundário, só enquanto não for a candidata). Prompts, registros e resultados históricos das duas últimas permanecem inalterados. Mesmos 60 itens inéditos (30 de fluxo e 30 de desafio, analisados separadamente), mesmo pacote (instrumentos_g1/montar_pacotes.py), mesmo modelo e configuração, três execuções por versão, códigos e ordem embaralhados de forma independente por execução e por versão, contextos isolados, execuções das três versões feitas juntas e não reaproveitadas de experimentos anteriores. Falha técnica (formato inválido, truncamento) pode ser reexecutada uma vez, com o mesmo prompt e o motivo registrado. Todas as execuções entram na análise.

Referência: rótulos do ChatGPT para os 60 itens, itens com conflito de triagem e amostra de controle (20% dos sem conflito, mínimo de 10) classificados por Eri às cegas e confrontados, divergências examinadas por Eri conforme a seção 2.3 do plano rev2. A referência não é verdade absoluta. Itens em divergência legítima formam a zona contestada e nunca entram como consenso. Correspondência: BOA, APROVADA; AMBÍGUA, REVISAR; RUIM, REPROVADA, em princípio.

## 2. Definições para evitar ambiguidade

- Aprovação automática: veredicto APROVADA sem divergência legítima material declarada. Nas versões v2.2 e v2.3-exp, que não têm o campo, toda APROVADA é aprovação automática. Para a candidata, os resultados são sempre reportados em duas leituras: por veredicto e por aprovação automática. A taxa de divergência material declarada por estrato é acompanhada, para detectar uso como escudo (proposta de alarme: declarada em mais de 20% dos itens, ou concentrada num estrato, a ser discutido por Eri).
- Execução: uma rodada completa dos 30 itens do estrato por uma versão. Item e execução são os eventos analisados. Três execuções de 30 itens não são 90 itens independentes.
- Evento grave: aprovação automática de item de referência RUIM sem contestação (camada 1).

## 3. Camadas de erro, reportadas separadamente (sem índice global)

1. Aprovar automaticamente item de referência RUIM não contestado.
2. Aprovar automaticamente item de referência AMBÍGUA, ou item contestado sem reconhecer a contestação.
3. Reprovar ou inventar defeito em item BOA (reprovação indevida de história excelente).
4. Confundir REVISAR e REPROVADA.
5. Veredicto correto com motivo errado.

A ordem é prioridade inicial de análise, não medida absoluta de gravidade. Cada camada é reportada por versão, por execução, por estrato (fluxo e desafio; e, dentro do desafio, por célula de intenção e pela classe real) e por item. Contagens com intervalos, nunca só percentuais. Não se combina fluxo e desafio num número único.

## 4. Dimensões e resultado de cada uma

Dimensões (as oito já aprovadas como dimensões, não como condições absolutas): (1) camada 1; (2) camada 2; (3) retenção das BOA e defeitos inventados; (4) trocas entre aprovar e não aprovar entre execuções do mesmo item; (5) motivo correto; (6) controles especiais; (7) estrato de sentimentalismo implícito; (8) sem piora onde o controle já acertava.

A dimensão 6 depende dos controles especiais, que não fazem parte da G1 e dependem de autorização posterior. Sem eles, a dimensão 6 é "não avaliada", e a conclusão B fica indisponível (no máximo A, com indicação a confirmar). Peço decisão de Eri sobre isso na seção 9.

Resultado por dimensão e por controle, com o mesmo critério simétrico:
- Melhora: nas três execuções, o número de erros da candidata na camada é menor que o do controle na mesma execução; e, no pareamento por item, os itens corrigidos pela candidata (resultado correto em pelo menos duas das três execuções, contra errado no controle) superam os itens piorados; e a diferença é maior que a oscilação entre execuções da mesma versão observada neste experimento (maior diferença entre duas execuções da própria candidata e do próprio controle).
- Piora: a mesma regra no sentido inverso.
- Sem diferença distinguível: o que não cumprir nenhuma das duas. É o resultado padrão.
- Inconclusivo: falha metodológica (julgador, pacote incompleto, rótulos comprometidos, execução inválida). Nunca é evidência de qualidade.

A faixa histórica de variação da v2.2 não é critério. O ruído relevante é o deste experimento.

## 5. Comparação pareada

Tabela por item e por execução: referência, veredicto e aprovação automática de cada versão, motivo julgado, flags. Para cada par (candidata contra principal, candidata contra secundária, e descritivamente secundária contra principal): itens iguais, itens corrigidos, itens piorados, por camada, e o padrão por item (3 de 3, 2 de 3). Testes pareados exatos (por exemplo de sinais) podem acompanhar como auxílio descritivo, com a ressalva de que o tamanho não sustenta inferência forte. O padrão por item não é convertido em decisão por maioria: em operação cada execução decide sozinha, e um erro grave em qualquer execução conta como evento.

## 6. Itens contestados

Não se mede concordância com um dos lados. Mede-se, segundo o julgador de motivos: se o Crítico apresenta interpretação defensável; se identifica corretamente a natureza do fundamento (A, B ou C); se reconhece a dúvida material quando existe, sem divergência vazia. Para as versões que não têm o campo de divergência, o reconhecimento só pode ser avaliado pelo texto da justificativa.

## 7. Julgador de motivos e auditoria

Instrumento: prompts/julgador_motivos_v1_rascunho.md, com pacote completo (foto, textos anteriores, texto, saída integral sem identificar a versão, ficha de referência, fundamentos concorrentes nos contestados), procedimento fixo e porta de completude. Pacote incompleto torna a avaliação do item inconclusiva. O limite de 15% de inconclusivas é alarme metodológico, não tolerância: se as inconclusivas se concentrarem numa categoria, origem ou tipo de defeito, a conclusão correspondente pode ser considerada inválida mesmo abaixo de 15%. Auditoria humana de pelo menos 20% das avaliações do julgador, mínimo de 10, com seleção definida antes: sorteio por semente de Eri (sal "g3-auditoria-julgador") mais cobertura obrigatória dos principais tipos de veredicto (pelo menos um caso por combinação de versão e veredicto, e por motivo "errado" e "inconclusivo" quando existirem). Erro sistemático encontrado inutiliza a contagem do julgador, e a dimensão 5 fica inconclusiva.

## 8. Decisões possíveis ao final (sem homologar)

- A, continuar investigando: evidência parcial, mecanismos de erro compreendidos, hipótese plausível.
- B, considerar a candidata superior: melhora relevante, consistente e fundamentada sobre o controle principal, nas duas amostras lidas separadamente, sem perdas graves nas camadas 1 e 3 (nenhuma piora), dimensão 5 conclusiva, dimensão 6 avaliada e sem queda. Limiares numéricos propostos para Eri decidir: melhora nas camadas 1 e 2 conforme a regra da seção 4 em ambas as amostras; nenhuma piora nas camadas 1 e 3; pelo menos 70% dos acertos de veredicto com motivo "correto" ou "parcial" (proposta); taxa de divergência material declarada abaixo do alarme.
- C, homologar para publicação autônoma: fora do alcance deste experimento. Exige validação muito maior e posterior.
Sinais de reconsideração (alertas diagnósticos, sem gatilho automático): melhora dentro do ruído do experimento; sentimentalismo continuando a passar; mérito mal demonstrado; trocas entre aprovar e não aprovar tão frequentes quanto antes; maioria de acertos por motivo errado; Crítico seguindo um único avaliador; divergência declarada como escudo; aprovação de itens limpos e vazios (quando os controles existirem). Qualquer alerta pede diagnóstico escrito e decisão de Eri, e pode apontar para mudar a estratégia, inclusive a geração dos candidatos, e não para a v2.5.

O experimento é capaz de mostrar melhora, igualdade e piora com a mesma clareza: a regra da seção 4 é simétrica, e a piora da candidata em qualquer camada é reportada com o mesmo destaque.

## 9. O que Eri precisa decidir sobre este protocolo

1. Aceitar que, sem os controles especiais, a conclusão B fique indisponível, ou autorizar a produção deles antes da G3.
2. Os limiares propostos (70% de motivos corretos ou parciais; alarme de 20% de divergência material declarada; regra de melhora da seção 4).
3. Se a camada 3 (reprovar história excelente) deve ter peso de decisão igual à camada 1 na conclusão B, ou só ser reportada ao lado.

## 10. Cláusula de inferência a constar no relatório final, antes dos resultados

As amostras são pequenas; os resultados dependem dos modelos usados; a subjetividade editorial legítima não desaparece; avaliadores podem errar; as execuções repetidas são correlacionadas; consistência não é correção; concordância com o ChatGPT não é prova de qualidade; uma pequena redução percentual de erros não demonstra superioridade; três execuções não provam estabilidade. O conjunto não pode ser descrito como inacessível ao redator. As proteções (ordem cronológica, hashes, registros de acesso e uso único) dão integridade documental e auditoria parcial, e não provam ausência de acesso.
