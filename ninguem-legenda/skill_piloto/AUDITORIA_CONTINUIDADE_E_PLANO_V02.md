# Continuidade da auditoria: encerramento técnico do piloto manual e plano da v0.2

Data: 29/10/2026. Complementa `AUDITORIA_FINAL_PILOTO.md`, que permanece como referência e não foi refeita. Nesta etapa não alterei a skill, não executei Crítico, não implementei a v0.2 e não toquei em n8n, grade, fila, contador real, lacres ou nas 72 avaliações. Não houve experimento novo nem consumo de crédito.

---

## I. Respostas às questões 3 a 12

**3. O Crítico v2.2 continua sendo a melhor referência consultiva?**
Sim, como a melhor referência documentada, e só como consultiva. Foi a única versão validada contra 24 itens inéditos com rótulos externos fixados antes, e na G3 reduzida (240 avaliações) foi mais estável que a v2.4-exp (divergiu entre execuções em 5 itens, contra 11). Ser a melhor disponível não a torna confiável como portão: ela aprova AMBÍGUA como se estivesse pronta. Por isso o papel correto segue sendo apontar problemas, nunca liberar peça.

**4. Há evidência para promover alguma versão experimental?**
Não. A v2.4-exp teve superioridade não demonstrada na G3 (perdeu BOA, criou erros novos, foi menos consistente). A v2.3 nunca foi promovida. A C1b está congelada e nunca foi executada. Menos aprovações, sozinho, não é melhoria editorial. Mantém-se a v2.2.

**5. Situação da C1b e da Emenda 2**

| Conceito | C1b | Emenda 2 |
|---|---|---|
| Congelamento | Sim, por hash (difere da v2.2 só nos 3 blocos declarados) | Sim, lacre de 14 arquivos, 0 divergências |
| Execução | Não. Zero arquivos de execução de Crítico | Não. Produção das 12 histórias feita e lacrada; as 72 avaliações não existem |
| Homologação | Não | Não. O desenho nunca promove a C1b automaticamente |
| Encerramento | Não decidido | Não decidido. Depende da escolha sobre L8CFD (parte III) |

**6. As pendências impedem o piloto manual ou só a homologação futura?**
Só a homologação futura do Crítico, da C1b e da autonomia. O piloto manual não depende do Crítico (consultivo) nem da classificação cega das 12, porque toda peça passa por aprovação humana. A ressalva é metodológica: a classificação provisória de L8CFD ("BOA, FUNCIONAL") não pode ser usada como validação.

**7. O mecanismo sustenta continuar produzindo peças-piloto supervisionadas?**
Sim. A evidência é suficiente para esse fim limitado: uma parcela relevante dos 60 itens da G1 recebeu rótulo BOA, e na arbitragem você decidiu 3 BOA, 3 AMBÍGUA e 0 RUIM entre os 6 itens revistos. Não é evidência de sustentabilidade em longo prazo (risco de repetir o truque, sem teste de volume) nem de qualidade sem supervisão. Regra a manter: se o estoque de boas histórias acabar, a produção para.

**8. O que bloqueia a próxima etapa de uso manual?**
Problemas técnicos e editoriais efetivos, todos pequenos e resolvíveis:
1. A skill v0.1.1 diverge de decisões já tomadas: imprime "Nº NNN" (a decisão é "001"); cita Gemini/Nano Banana como único gerador; não contém o padrão fotográfico nem o perfil de layout decidido.
2. A posição do número em relação a @surtodelucidez está indefinida, porque a composição aprovada visualmente não está no repositório (parte IV, conflito C1).
3. A aprovação visual da arte do LAB-001 está pendente (foto v10 tratada, B215, título sobre a ponteira, número sobre a janela, poça junto ao rótulo).
4. A política de rotulagem de conteúdo gerado por IA nas plataformas não foi verificada. Não bloqueia produzir manualmente, bloqueia publicar.
Não bloqueiam: homologação do Crítico, C1b, as 72 avaliações, L8CFD.

**9. O padrão fotográfico é verificável?**

| Critério | Estado |
|---|---|
| Verticalidade da haste (ajuste de reta aos pixels escuros) | Demonstrado em 10 versões (7,4° a 0,3°). Ferramenta externa à skill |
| Contraste efetivo do texto (alfa real sobre fundo com degradê, luminância WCAG) | Demonstrado como medição; limiares 4,5 (média dos blocos), 3,0 (pior decil e título/número) são provisórios; não inclui a sombra do texto |
| Formato 9:16 e resolução | Verificável por código; a faixa de atenção 810 a 1079 px é provisória |
| Tratamento de brilho do piso | Demonstrado, só ajuste de tom |
| Realismo, artefatos de IA, coerência física geral, correspondência com NA FOTO, não antecipar o FORA | Julgamento humano com apoio semântico; não verificável por código |
| Reprodutibilidade entre episódios | Não demonstrada: uma única cena foi calibrada |
| Limite de duas correções | Adequado como padrão; o LAB-001 usou dez versões por autorizações suas dadas na conversa, sem registro formal |

**10. O que falta, estritamente, para a skill ser tecnicamente consolidada como piloto manual?**
(a) Implementar a v0.2 versionada sem alterar a v0.1.1; (b) número real no formato "001"; (c) texto neutro quanto ao gerador de imagem; (d) padrão fotográfico incorporado como critério, com os limiares marcados como provisórios; (e) registro formal de exceções ao limite de correções; (f) a especificação do número e da assinatura, que depende de você enviar a imagem ou as medidas (não invento coordenadas); (g) testes atualizados e conferidor de integridade verde; (h) fechamento do LAB-001 com sua aprovação visual.

**11. Decisões que exigem aprovação humana expressa**
Especificação final do número e da assinatura; qualquer homologação de layout, fonte, margens e zonas de segurança; aprovação do padrão fotográfico e dos limiares; aprovação visual da foto e da arte de cada peça; exceções ao limite de correções; escolha sobre L8CFD; retomada ou encerramento da verificação C1b; início de implementação da v0.2; qualquer publicação; qualquer contato com n8n, grade, fila ou contador real; política de rotulagem de IA.

**12. Podemos encerrar o desenvolvimento técnico do piloto?**
Sim, sem impedimento crítico, depois das alterações obrigatórias da v0.2. Três coisas distintas:
- **Desenvolvimento técnico concluído:** alcançável com a v0.2 e seus testes. Não exige experimento novo.
- **Homologação editorial:** não existe e não decorre disso. Nenhum item (Crítico, C1b, layout, fonte, padrão fotográfico) está homologado.
- **Autorização operacional:** não existe. Publicação, n8n, fila e contador real seguem fora de escopo.

---

## II. Matriz de decisões

| Item | Confirmado | Provisório | Pendente |
|---|---|---|---|
| Uso | Piloto manual supervisionado; nada de n8n, fila, grade, publicação ou contador real | | |
| Número real | Formato "001", "002"... (decisão sua, 24/10); LAB- só em teste | | |
| Elemento 20% menor | É o número "001", abaixo de @surtodelucidez; assinatura não será reduzida de novo | | Base do cálculo (parte IV, C2) |
| Posição relativa assinatura e 001 | Aprovada visualmente por você em composição posterior | | Imagem ou medidas; não está no repositório |
| Layout B215 inteiro | | Perfil de teste (alfa 215, degradê topo reforçado) | Aprovação |
| Perfil B | | Base provisória | Homologação |
| Zonas de segurança 250/340 px, fonte Inter | | Provisórias | Homologação |
| Crítico v2.2 | Mantido consultivo | Referência provisória | Nenhuma promoção |
| C1b, Emenda 2 | | Congeladas | Decisão sobre L8CFD; sem homologação |
| 72 avaliações | Suspensas | | Retomada ou encerramento |
| Gerador de imagem | Não exclusivo | | Texto da skill a corrigir |
| Padrão fotográfico | "Mesmo padrão de excelência", sem afrouxar | Limiares | Aprovação |
| Limite de correções | Padrão de duas, com exceções humanas documentadas | | Modelo de registro |
| Foto LAB-001 (v10 tratada) | Segue como base | | Aprovação visual e editorial |
| Rotulagem de IA | | | Verificar |
| Séries irmãs | | | Documentos para a comparação (não bloqueia) |

---

## III. Parecer sobre L8CFD

Fatos: L8CFD é uma das 12 histórias inéditas do lote cego; foi avaliada por você fora do procedimento ("BOA, FUNCIONAL", provisória) e originou prompt e composição do piloto. Emenda 2: 18 itens x 2 execuções x 2 versões = 72. O registro de circunstância já proíbe mudar a participação de L8CFD sem autorização expressa sua.

| | **A. Manter e registrar a limitação** | **B. Excluir** | **C. Substituir** | **D. Encerrar sem executar** |
|---|---|---|---|---|
| Vantagens | Protocolo, contagem (72) e lacre intactos; é a opção mais fiel ao pré-registro | Remove o item contaminado; resultado mais limpo para o que sobrar | Mantém 18 itens e o número de avaliações | Elimina o risco metodológico e o custo; preserva tudo |
| Riscos | Um item com sua leitura prévia pode inflar ou distorcer a concordância; a conclusão precisa de análise com e sem L8CFD | Só 11 inéditas; poder estatístico menor; cada item pesa ainda mais | Exige nova história cega, já depois de conhecer o desenho; risco de viés de seleção; é, na prática, trabalho novo | A C1b nunca é testada; não há caminho para a promoção do Crítico; o ganho esperado da C1b fica sem resposta |
| Mudanças documentais | Registro de limitação anexo; plano de análise (com e sem L8CFD) declarado antes de executar | Emenda 3 (17 itens, 68 avaliações), novo lacre | Emenda 3, produção cega nova, novo lacre, nova previsão cega | Registro de encerramento; nenhum arquivo apagado |
| O que permanece válido | Tudo | As 11 inéditas e as 6 arbitradas; hashes; produção das outras 11 | Lacre das outras 11; a nova seria sujeita ao novo lacre | Todos os registros, lacres, G1 a G3, arbitragem, congelamentos |

Observação do auditor, sem escolher por você: as alternativas B e C alteram o protocolo lacrado e por isso exigem emenda; A e D não. Qualquer resultado de A ou B continua sem valor de validação independente, por causa dos riscos da parte 4 da auditoria anterior. A decisão D é a única que também fecha o desenvolvimento do piloto sem depender de nova produção; A, B e C mantêm a verificação aberta e adiam a homologação do Crítico, não o piloto manual.

---

## IV. Plano técnico mínimo da v0.2 (sem execução)

**Princípio:** nova pasta `o-que-ninguem-legenda-piloto-v0.2`, copiada da v0.1.1. A v0.1.1 e seu ZIP ficam byte a byte intactos (verificação por hash antes e depois). Nenhuma dependência nova.

**Conflitos entre decisões recentes e especificações antigas (identificados, nenhum resolvido por mim):**
- **C1. Posição do número.** v0.1.1: número no topo, alinhado à direita. Teste B215 (sua instrução de 24/10): número colado ao nome da série, no topo. Instrução nova: "001" abaixo de @surtodelucidez. A composição aprovada não está no repositório. Preciso da imagem ou das medidas.
- **C2. Base do "20% menor".** Hoje o número tem 30 px; a assinatura, 27 px (v0.1.1) ou 22 px (teste B215). "20% menor" pode significar 24 px (do número atual), cerca de 17,6 px (do tamanho da assinatura de 22) ou cerca de 21,6 px (da de 27). O texto recebido usa as duas leituras. Não escolho.
- **C3. Assinatura.** "Não reduzir novamente" não diz se os 22 px do teste já contam como a redução aprovada ou se a assinatura volta aos 27 px.
- **C4. Formato do número.** O código imprime "Nº NNN"; a decisão é "001".
- **C5. Gerador.** SKILL.md, prompt_fotografico.md e versao_limitacoes.md citam Gemini/Nano Banana; a decisão é não impor gerador.
- **C6. Limite de correções.** `max_geracoes_imagem_por_texto: 2` no config; o LAB-001 usou dez versões por exceções dadas na conversa, sem registro formal.
- **C7. Registro de decisões.** `pilotos/LAB-001/DECISOES_EDITORIAIS_LAB-001.md` registra "número colado ao nome da série"; precisa ser atualizado quando C1 for resolvida.

**Alterações propostas, cada uma com justificativa:**

| Arquivo (na pasta v0.2) | Alteração | Justificativa |
|---|---|---|
| `SKILL.md` | Versão 0.2; remover exclusividade do gerador; passo da foto passa a citar o padrão e a exceção documentada | C5, C6 |
| `references/versao_limitacoes.md`, `prompt_fotografico.md` | Texto neutro quanto ao gerador; lição de que instruções de geometria falham e a saída é mudar o arranjo físico da cena | C5; evidência do LAB-001 |
| `references/analise_visual.md` | Incorpora o padrão: critérios impeditivos I1 a I9, APTA/AJUSTAR/REFAZER, quais são verificáveis por código e quais exigem julgamento; limiares marcados provisórios | Item 9 |
| `references/assinatura_numeracao.md` | Número real "001"; LAB- só em teste; posição e tamanho do número conforme especificação que você enviar; marcado "visual aprovado, layout não homologado" | C1 a C4 |
| `scripts/config.json` | Novo perfil C derivado do B (alfa dos rótulos 215, degradê do topo reforçado, tamanhos da assinatura e do número só quando C2 e C3 forem respondidas); limiares de contraste; registro de exceção ao limite de correções | Decisões 24/10 |
| `scripts/compor_story.py` | Remove o prefixo "Nº" do número real; suporte ao perfil C; posição do número pela especificação; bloqueio se o número ficar fora da zona permitida | C1, C4 |
| `scripts/analisar_foto.py` | Adicionar medição de contraste efetivo e verificação de verticalidade, usando só as bibliotecas que o script já importa; se for necessária biblioteca nova, manter a ferramenta fora da skill e dizer isso | Item 9 |
| `scripts/registro_numeracao.py` | Aceitar e imprimir "001"; contador real continua não acessado | C4 |
| `scripts/verificar_skill.py` | Versão e manifesto de arquivos da v0.2 | Integridade |
| `testes/test_piloto.py` | Novos testes (abaixo) | Cobertura |
| `ENTREGA_PILOTO_V02.md`, `REGISTRO_VERSAO_v0.2.json`, ZIP em `dist/` | Registro, hashes, limitações declaradas | Rastreabilidade |
| `pilotos/LAB-001/DECISOES_EDITORIAIS_LAB-001.md` | Anexar as decisões novas; nada apagado | C7 |

Não alterados: Crítico v2.2 (`critico_v2_2_referencia.md`), preditor cego, criador, controles de repetição, taxonomia, lacres, C1b, Emenda 2, n8n.

**Testes necessários**
1. Os 23 testes atuais continuam passando na v0.2.
2. Hash da v0.1.1 e do seu ZIP idênticos antes e depois.
3. Número real formatado como "001", "012", "100"; sem "Nº"; LAB- só em modo simulação.
4. Número real nunca consome nem lê o contador real (teste de recusa).
5. Perfil C: número e assinatura dentro das zonas e sem sobreposição, nos tamanhos especificados.
6. Bloqueio quando texto não cabe ou elemento cai em zona de segurança.
7. Medição de contraste: caso aprovado, caso reprovado, e concordância com os valores já medidos do LAB-001 (v10 tratada).
8. Verticalidade: v10 (0,3°) aprovada, v8 (9,7°) reprovada.
9. Resolução e 9:16: aceita 1080x1920, reprova proporção errada.
10. Limite de correções: terceira geração exige exceção registrada.
11. Texto sem exclusividade de gerador (busca por "exclusiv").
12. `verificar_skill.py` verde e ZIP reproduzível.
13. Verificação de que nenhum script toca n8n, fila, grade, contador real ou `registro.csv` do laboratório.

**Dependência para implementar:** respostas de C1, C2 e C3. Sem elas, a v0.2 sai com o perfil C parcial e a posição do número marcada como pendente, nunca com coordenadas inventadas.

---

## V. Decisões que o proprietário precisa tomar

1. Enviar a imagem ou as medidas da composição com @surtodelucidez e "001" aprovada (C1).
2. Dizer a base do "20% menor": do número atual, ou da assinatura (C2).
3. Dizer se a assinatura fica em 22 px ou volta a 27 px (C3).
4. Escolher entre A, B, C ou D para L8CFD (parte III).
5. Aprovar, ajustar ou rejeitar o padrão fotográfico e seus limiares provisórios.
6. Autorizar a implementação da v0.2 conforme este plano.
7. Aprovar ou recusar visualmente a arte do LAB-001.
8. Antes de qualquer publicação: política de rotulagem de IA.
9. Opcional, não bloqueia: documentos das séries Cena Cortada, Nota Fiscal Emocional e Palavra em Julgamento.

---

## VI. Veredito

**AJUSTES OBRIGATÓRIOS.**

Não é revisão estrutural: o fluxo, os estados, a rejeição, a numeração, os controles de repetição e a separação entre manual e autônomo estão coerentes e íntegros. Não é ainda "piloto manual consolidado": a v0.1.1 diverge de decisões tomadas depois (formato do número, gerador, padrão fotográfico, layout), há três pontos de especificação visual que só você pode esclarecer e o LAB-001 espera sua aprovação. Resolvidos esses pontos pela v0.2, o desenvolvimento técnico pode ser considerado encerrado, sem homologação editorial e sem autorização operacional.
