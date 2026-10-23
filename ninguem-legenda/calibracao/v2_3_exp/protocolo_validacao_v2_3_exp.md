# Protocolo de validação independente da v2.3-exp (para registro antes de qualquer execução)

Data: 22/10/2026. NADA abaixo foi executado. A execução exige autorização expressa de Eri, depois da classificação externa. Os itens Q06, Q10 e Q22 e todo o material de v2_2/conjunto estão contaminados e não entram.

## 1. Conjunto
- 30 itens inéditos (W01 a W30), embaralhados e sem pistas de origem, em conjunto/candidatas.json. Todos passaram nos filtros determinísticos (resultado_filtros.json); um candidato bruto (O2-06) foi eliminado pelos filtros e o excesso foi sorteado com semente registrada.
- Três origens distintas, 10 itens de cada: O1 o Criador do projeto (prompts/criador.md, taxonomia, registro); O2 um cronista livre que recebeu só o formato e um exemplo, sem taxonomia nem Criador; O3 um redator de rascunhos rápidos, sem revisão. O mapa de origens é privado (gabarito_origens_privado.json, SHA-256 registrado) e só é aberto depois da execução, para análise por origem.
- Não há tipo pretendido por item. A diversidade de qualidade vem do processo de criação, não de categorias ilustradas à mão. Os nove perfis pedidos (BOA com implícito, BOA previsível, AMBÍGUA corrigível, imperfeição periférica, obscura, causalidade artificial, redundante, clichê sentimental, micro-história simples e original) serão verificados depois, pelo rótulo externo e pelo motivo, e a cobertura de cada perfil será declarada. Se algum perfil ficar sem exemplo, será dito, e não será forjado depois.
- Máxima semelhança textual do FORA com itens anteriores: 0,48 (O2-11 contra um item V22), abaixo de repetição evidente. Os itens históricos não entram.

## 2. Ordem de execução
1. Eri encaminha conjunto/para_externo_v23.md ao avaliador externo. Rótulos BOA, AMBÍGUA, RUIM, com motivo para AMBÍGUA e RUIM, sem ver nenhum veredicto. Commit dos rótulos com SHA-256 antes de qualquer execução.
2. Três previsões cegas independentes por item (leitores novos, só foto e NA FOTO).
3. Crítico v2.3-exp em duas execuções independentes e Crítico v2.2 em duas execuções independentes, sobre as mesmas previsões, ordens e códigos diferentes em cada uma, contexto limpo, sem filtros e sem acesso a rótulos, origens ou resultados anteriores.
4. validar_avaliacao.py em todas as saídas.
5. Decodificação das execuções por mapa privado, só depois de todas terminadas.
6. Nada é ajustado depois de ver os resultados: nem prompts, nem rótulos, nem itens.

## 3. Medidas (sem usar concordância global como prova)
1. Falsas aprovações: APROVADA em RUIM; e, à parte, em AMBÍGUA (aprovação contestável).
2. Falsas reprovações: REPROVADA em BOA.
3. Revisões desnecessárias: REVISAR em BOA.
4. Defeitos reais identificados: o defeito citado corresponde ao motivo externo.
5. Defeitos inventados: sem trecho, com demonstração hipotética, vaga ou contrariada pelo texto; inclui qualquer defeito C ou D em item BOA e correções de B tratados como bloqueio.
6. Consistência: veredicto e classe (A, B, C, D) entre as duas execuções de cada versão, com a lista dos itens divergentes e o motivo.
7. Correspondência veredicto e justificativa: cada veredicto coincidente com o rótulo é classificado como (a) acerto pleno, motivo coincide com o externo; (b) acerto pelo motivo errado, não contado como acerto editorial pleno; (c) acerto sem motivo comparável (BOA aprovada sem defeito externo a confrontar). A comparação de motivos usa regra escrita antes: o julgador (agente isolado que só recebe o motivo externo e o defeito citado, sem rótulo nem veredicto) responde "coincide / coincide em parte / não coincide".

## 4. Comparações
Separadas: v2.2 execução 1 e 2; v2.3-exp execução 1 e 2. Contagens por origem e por perfil. A v2.1 não entra, pois já foi medida no conjunto anterior e esta rodada não pretende reabrir a comparação.

## 5. Sinais de alerta pré-definidos
- Qualquer RUIM aprovada.
- Qualquer BOA reprovada ou com defeito C ou D demonstrado.
- Mais AMBÍGUAS aprovadas na v2.3-exp do que na v2.2 (a mudança não cumpriu seu propósito).
- Defeito com cliche_efetivo ou redundancia apoiado só na previsão (validador avisa).
- Defeito de contradição sem "Alternativa natural:".
- Aumento de BOA em REVISAR em relação à v2.2.
- Divergência de veredicto entre execuções da v2.3-exp maior que a da v2.2 no mesmo conjunto.
- Itens B que o avaliador externo considera centrais (sinal de permissividade na fronteira B/C).
Esses sinais não são limiares de homologação: a decisão de homologar permanece com Eri.

## 6. Limitações declaradas
As três origens são todas modelos Claude, com prompts diferentes, o que reduz mas não elimina a dependência dos padrões do Criador. O avaliador externo é um único modelo. Trinta itens ainda é pouco para tipos raros. A cobertura de perfis é verificada depois e pode falhar. A fronteira B/C depende do julgamento do Crítico. O julgador de motivos é um modelo. Por isso os resultados orientam, não homologam.
