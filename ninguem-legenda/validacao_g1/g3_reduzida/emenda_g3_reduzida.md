# Emenda 1 ao protocolo de análise G3: G3 reduzida

Data: 23/10/2026. Autorização expressa de Eri (23/10, mensagem "Decisão sobre o plano revisado e autorização da G3 reduzida"). Esta emenda é um documento separado. O protocolo de análise original (referencia_editorial/protocolo_analise_g1.md, congelado no M1, commit 3dd05e5) permanece intacto, e nenhum arquivo do M1 é modificado. Esta emenda é registrada e publicada ANTES da primeira execução.

## 1. Natureza do experimento reduzido

Comparação entre o Crítico v2.2 (controle principal) e o Crítico v2.4-exp (candidato experimental), duas execuções por versão, sobre os mesmos 60 itens congelados da AMOSTRA DE FLUXO EXPERIMENTAL SIMPLIFICADO (30 de fluxo, 30 de desafio), totalizando quatro avaliações por item. Não é a G3 do protocolo original e não pode sustentar a conclusão de superioridade plena nem a homologação de autonomia previstas nele. Nenhuma versão é homologada por este experimento. Nenhuma promoção da v2.4-exp é automática.

## 2. Diferenças em relação ao protocolo original (M1)

1. Execuções por versão: duas, em vez de três.
2. Controle secundário v2.3-exp: não executado.
3. Julgador de motivos: não executado. A dimensão 5 (qualidade das justificativas) não é avaliada por julgador. Justificativas são apenas descritas, sem percentual de motivos corretos, sem limiar de 80%.
4. Controles especiais: não produzidos. A dimensão 6 não é avaliada.
5. Previsões cegas: reutilizadas as três previsões lacradas na G2 (commit c028472), fornecidas sem edição, na mesma ordem, às duas versões, em todas as execuções. Constituem uma entrada experimental comum, não três avaliações humanas independentes. No protocolo original, as previsões eram produzidas dentro de cada execução.
6. textos_anteriores: lista vazia em todos os pacotes, como no pacote externo da G2 (a amostra não tem edições anteriores).
7. Cada execução é dividida em duas partes consecutivas de 30 itens (ordem já embaralhada), cada parte avaliada por um agente isolado, por limite prático de tamanho da saída. O mesmo particionamento é usado nas quatro execuções.
8. Referência: os 60 rótulos externos do ChatGPT (lacrados no commit fad0b7f). A conferência humana de Eri (conflitos de triagem e controle) NÃO foi realizada. A segunda leitura de 27 itens (commit 937f93a) é não independente e não é usada como gabarito nem como confirmação.
9. Conclusões possíveis: as quatro desta emenda (seção 6), e não A/B/C do protocolo original.

## 3. Entradas e condições de execução

- Instrumento de pacote: instrumentos_g1/montar_pacotes.pacote_critico, congelado, sem alteração. Montagem em validacao_g1/g3_reduzida/montar_g3.py.
- Pacote por item: codigo, conceito_foto, na_foto, fora, previsoes_cegas (3), textos_anteriores (vazio). Sem id, rótulo, origem, versão, célula, mapa.
- Códigos e ordem embaralhados de forma independente por execução e por versão (sementes distintas por execução). Quatro execuções: v22_e1, v22_e2, v24_e1, v24_e2.
- Prompts: critico_v2_2.md e critico_v2_4_exp.md, sem alteração, conferidos por hash contra o M1. Mesmo modelo e configuração em todas as execuções, registrados depois a partir dos registros dos agentes.
- Cada parte é avaliada por um agente novo, em contexto isolado, instruído a ler apenas o prompt e o arquivo da parte. O isolamento é documental, não técnico, e o avaliador é o mesmo modelo que gerou os itens (limitação declarada).
- As quatro execuções são feitas juntas. Falha técnica (formato inválido, truncamento) pode ser reexecutada UMA vez, com o mesmo prompt e o motivo registrado. Todas as execuções entram na análise. Nenhuma execução favorável é selecionada retrospectivamente.
- Saídas guardadas literalmente, validadas por validar_avaliacao.py (inalterado) e lacradas com SHA-256 em commit ANTES de abrir os rótulos ou decodificar.
- Se a disponibilidade de recursos interromper as execuções, o planejamento é preservado e retomado, sem escolher execuções.

## 4. Referência, tensões e rótulos contestáveis

- Distribuição dos rótulos externos: 33 BOA, 16 AMBÍGUA, 11 RUIM.
- Todos os 11 itens RUIM estão entre as 17 tensões exploratórias. Portanto, o grupo sem tensões não contém nenhum RUIM. É PROIBIDO apresentar taxa de aprovações indevidas de RUIM calculada sobre o grupo sem tensões, ou interpretar sua ausência como resultado favorável. As análises de sensibilidade respeitam a composição efetiva dos grupos.
- Os resultados são apresentados completos, com os itens em tensão identificados (tipos A e B). Itens em tensão são tratados como rótulos de menor confiabilidade, e o relatório mostra o que muda quando eles são tratados à parte, sem excluí-los do resultado principal.
- Limites de confiabilidade a declarar: rótulo de um único avaliador que é um modelo; ausência de validação humana independente; rótulos são referência experimental, não verdade editorial absoluta; a amostra é de fluxo simplificado, com M01 em 36 de 60 itens e pequeno_vs_grande em 42 de 60.
- Fluxo e desafio são sempre analisados separadamente. Nenhum índice global.

## 5. Medidas, definidas antes dos resultados

Correspondência de referência: BOA corresponde a APROVADA, AMBÍGUA a REVISAR, RUIM a REPROVADA, em princípio.

Por item e por execução, em tabela pareada (v2.2 contra v2.4-exp, execução 1 e 2):
1. Aprovações inadequadas de itens RUIM e de itens AMBÍGUA, relatadas separadamente, com listas de itens.
2. Preservação das BOA: BOA aprovada, BOA em REVISAR, BOA reprovada. Toda perda de aprovação de BOA é registrada, inclusive em uma só execução.
3. Casos corrigidos pela candidata: item cujo veredicto da v2.2 é erro (aprova RUIM ou AMBÍGUA, ou não aprova BOA) nas duas execuções e cujo veredicto da v2.4-exp é acerto nas duas. Correção em uma execução é registrada à parte como parcial.
4. Novos erros introduzidos pela candidata: o inverso.
5. Consistência entre execuções: itens com veredicto diferente entre as duas execuções da mesma versão.
6. Veredicto bruto e elegibilidade automática, sempre os dois (na v2.2, elegível é toda APROVADA; na v2.4-exp vale o campo elegibilidade_automatica).
7. Divergências editoriais materiais declaradas pela v2.4-exp, listadas item a item.
8. Dependência dos resultados de itens contestáveis (as tensões), respeitando a composição dos grupos.
9. Justificativas: apenas descrição qualitativa das aprovações inadequadas, sem julgador.

## 6. Critério de interpretação

As conclusões possíveis são quatro. Nenhuma depende apenas de diferença numérica pequena, e sobreposição de resultados não é prova de equivalência.

1. MELHORIA OPERACIONAL OBSERVADA, COM RESSALVAS. Exige, juntas:
   - ganhos identificáveis em mais de um item (pelo menos dois itens distintos, listados) nas aprovações inadequadas de RUIM e AMBÍGUA, no veredicto bruto, em pelo menos um estrato;
   - nenhuma piora grave ou sistemática em qualquer estrato (grave: BOA reprovada nas duas execuções ou RUIM aprovado nas duas execuções que a v2.2 não aprovava; sistemática: dois ou mais itens do mesmo tipo de piora no mesmo estrato);
   - nenhuma perda consistente (nas duas execuções) nem editorialmente relevante de BOA. Uma perda assim impede a conclusão 1, e a candidata não é promovida automaticamente;
   - ganhos que não dependam apenas de itens contestáveis, nem apenas da elegibilidade ou da declaração de divergência;
   - consistência entre execuções não pior que a da v2.2.
   Não se exige melhora numérica estrita em todos os estratos quando o controle não apresentou erros corrigíveis em algum deles.
2. SUPERIORIDADE NÃO DEMONSTRADA. Padrão quando a evidência não é suficientemente favorável à v2.4-exp. A v2.2 permanece como referência provisória para a próxima etapa de laboratório, sem declaração de superioridade ou homologação.
3. PIORA OBSERVADA. Regra espelhada: perdas ou novos erros identificáveis em mais de um item sem compensação, ou piora grave.
4. INCONCLUSIVO. Falha técnica não resolvida, melhora ou piora que dependa de um único item ou de itens contestáveis, ou impossibilidade de leitura por estrato.

Melhora obtida apenas pela declaração de divergência, sem melhora nos vereditos brutos, não comprova superioridade editorial.

## 7. Simulação do gate (sem novas avaliações)

Usa somente os resultados das quatro execuções. Três desenhos, sem homologação de nenhum:
- GATE 1: uma avaliação por item. Simulado duas vezes por versão (execução 1 como primeira avaliação e execução 2 como primeira avaliação).
- GATE 2: duas aprovações obrigatórias. APROVADA somente se as duas execuções da versão aprovam.
- GATE 3: segunda avaliação apenas com sinais de risco definidos antes dos resultados. Sinais:
  - S1: alerta de filtros.py (executado sem alteração sobre os 60 itens, resultado em privado/resultado_filtros.json);
  - S2: zona ausência ou saudade pelo cadastro do item: tipo_contraste igual a presenca_vs_ausencia ou emocao igual a melancolia;
  - S3: sinal da primeira avaliação do Crítico. Na v2.2: e_a_associacao_mais_comum verdadeiro ou previsoes_que_capturaram maior ou igual a 2. Na v2.4-exp: objecoes não vazia ou divergencia_legitima diferente de "nenhuma".
  Com algum sinal, o item só é aprovado se a segunda avaliação também aprovar. Sem sinal, vale a primeira.
Para cada desenho e versão, relatar: erros evitados (aprovações indevidas retidas), histórias BOA atrasadas (BOA aprovada que seria retida), erros que permaneceram, e a fração de segundas avaliações acionadas (custo). Aprovados indevidos sem nenhum sinal são listados: a ausência de alerta não é presumida como ausência de risco.

## 8. Ordem de trabalho

1. Verificação mecânica da emenda e dos instrumentos, e publicação desta emenda.
2. Execução das quatro execuções e validação.
3. Lacre das saídas brutas (SHA-256, commit, push).
4. Só então decodificação, abertura dos rótulos, análise, simulação e relatório.

## 9. Limitações declaradas

- Um único avaliador de referência, modelo de IA, sem validação humana independente e sem a conferência humana prevista no M1.
- Quatro avaliações por item, pelo mesmo modelo: repetições dos mesmos 60 itens, não amostras independentes.
- Com 11 itens RUIM, um item vale cerca de 9 pontos percentuais. Qualquer conclusão traz listas de itens.
- Amostra de fluxo simplificado, com concentração de M01 e pequeno_vs_grande, uma candidata por conceito, conceitos pré-definidos.
- Sem julgador de motivos e sem controles especiais: não se avalia a correção das justificativas nem a sensibilidade a defeitos fabricados.
- Isolamento dos agentes documental e mesmo modelo gerador e avaliador.
- Sinais de risco do gate definidos a partir de erros conhecidos: podem não cobrir erros novos.
- O resultado orienta a escolha de uma referência provisória e não homologa nada.

## 10. Fora do escopo

Nenhuma execução de v2.3-exp, julgador de motivos ou controles especiais. Nenhuma imagem, nenhum crédito visual, nenhuma publicação. Sem alteração de n8n, grade, fila, publicadas, skills, Metricool, prompts, itens, rótulos, previsões lacradas ou arquivos do M1.
