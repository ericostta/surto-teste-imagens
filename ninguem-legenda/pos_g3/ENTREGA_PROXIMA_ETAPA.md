# Entrega: intervenção mínima, assinatura e contador, avanço paralelo e sequência até a implantação controlada

Data: 23/10/2026. Nada foi executado, publicado, comprado ou homologado. Nenhum prompt congelado, registro de M1, G1, G2 ou G3, n8n, grade, fila ou skill foi alterado.

---

## A. Intervenção editorial mínima e verificação limitada

### A.1 O problema que ela ataca

Segundo a sua arbitragem, o Crítico v2.2 aprova histórias de grau AMBÍGUA (D04, F22, D32 nas quatro execuções). Os padrões observados nos textos (hipóteses, não provas): a particularização por número, idade ou quantidade; a transformação que desfaz só a leitura que os previsores fizeram, e não algo que o NA FOTO afirma; mérito apenas sugerido, não demonstrado.

### A.2 A mudança: candidata C1, três inserções, nenhuma reconstrução

Arquivos: `pos_g3/intervencao/critico_v2_2_c1.md` e `diff_v2_2_para_c1.diff` (o diff mostra tudo o que mudou; a v2.2 em `prompts/` permanece intacta). A saída mantém `versao_criterio: "v2.2"` para usar o validador congelado, e a identidade da execução fica registrada fora da saída.

1. **E1 (transformação).** A transformação deve ser demonstrada sobre o que a foto e o NA FOTO mostram ou afirmam. Desfazer só a leitura dos previsores, quando o NA FOTO não a afirma, não conta.
2. **E5 (teste de remoção).** Reescrever o FORA mentalmente sem números, idades e quantidades. Se a transformação some, o detalhe era ornamento e o mérito não está demonstrado.
3. **Salvaguarda de abertura interpretativa.** Mais de uma leitura legítima não é defeito. Se a transformação está demonstrada em qualquer leitura plausível, aprova-se. Os reforços não podem exigir moral explícita, literalidade, motivo declarado ou explicação fechada, nem punir polissemia, implícito ou emoção não nomeada.

Risco declarado: o teste de remoção pode bloquear uma história boa cujo número é essencial (por exemplo, a contagem que sustenta o contraste). A verificação inclui itens desse tipo para medir isso.

### A.3 Desenho da verificação limitada (um único ciclo, registrado antes de executar)

**Material.** Doze histórias inéditas, sem usar os 60 itens da G1 como validação. Produzidas pelo Criador existente, em agentes novos, com três previsões cegas frescas por item, e quatro grupos de três: (i) produção normal; (ii) com particularização por número ou idade; (iii) com motivo declarado na última oração; (iv) deliberadamente abertas a mais de uma leitura forte. Os grupos ii a iv são estresse e ficam declarados como tal.

**Referência.** Você classifica as doze (BOA, AMBÍGUA, RUIM) em um único lote cego, antes de qualquer Crítico rodar, e as decisões são lacradas com SHA-256. Referência sua, não independente, e todos os avaliadores são da mesma família de modelos: o resultado não constitui confirmação editorial independente.

**Execuções.** v2.2 e C1, duas execuções cada, mesmos pacotes e mesmas previsões, em agentes isolados. Duas execuções, e não uma, porque a v2.2 virou o veredicto em 5 de 60 itens entre execuções e uma só leitura confundiria efeito com ruído. Cerca de 60 avaliações (48 nas inéditas e 12 na regressão, onde a v2.2 já tem dados da G3), contra 240 na G3.

**Regressão conhecida (não é teste inédito).** C1 sobre os seis itens arbitrados: D31 e F26 (BOA) devem continuar aprovados; D04, F22, D32 (AMBÍGUA) são os que se espera deixar de ser aprovados; D15 (BOA) é observação.

**Regra de decisão fixada antes de executar.** "Benefício claro" exige todas as condições:
- nas doze inéditas, C1 deixa de aprovar pelo menos dois itens que você classificou como AMBÍGUA e que a v2.2 aprovou, nas duas execuções;
- C1 não bloqueia nenhum item que você classificou como BOA e que a v2.2 aprovou, em nenhuma execução;
- na regressão, pelo menos dois dos três AMBÍGUA deixam de ser aprovados e D31 e F26 seguem aprovados.

Sem as três condições, o resultado é "sem benefício claro": a linha experimental é encerrada, a v2.2 segue inalterada e nenhum novo ajuste é feito. Com as três, C1 vira apenas proposta para você decidir, sem promoção automática nem homologação. Os resultados trazem listas de itens, nunca taxas, e o confronto com os rótulos históricos não recalcula a G3.

**Formalização.** Antes de executar: uma Emenda 2 documental com esta regra, os hashes de C1, da v2.2, dos pacotes e das decisões, publicada e verificada mecanicamente, no mesmo padrão da Emenda 1.

---

## B. Especificação recuperada: assinatura e contador

### B.1 Elementos (decisões conceituais recuperadas)

| Elemento | Especificação |
|---|---|
| Formato | Story 1080 x 1920, 9:16 |
| Identificação superior | O QUE NINGUÉM LEGENDA, com o número público da edição |
| Numeração | 001, 002, 003, exclusiva desta coleção |
| Assinatura inferior | @surtodelucidez apenas (a forma extensa SURTO DE LUCIDEZ @surtodelucidez ficou na versão anterior do DNA) |
| Tratamento | Assinatura, título e contador discretos, sem disputar atenção com a fotografia e a mensagem |
| Posições | Fixas entre edições, com margens de segurança da interface do Instagram |

### B.2 Proposta visual de posicionamento

`pos_g3/intervencao/wireframe_posicionamento.png`: wireframe com zonas de interface de 250 px no topo e 340 px no rodapé (valores usuais, a confirmar), identificação superior logo abaixo da zona de topo, fotografia, blocos NA FOTO e FORA, assinatura acima da zona de rodapé. É proposta de posição, não arte final, e o layout dos blocos de texto é hipótese minha porque a composição gráfica da série não está no repositório. Nada é homologado.

### B.3 Regra do contador e especificação técnica

**Regra.** O número só é consumido quando a publicação correspondente é confirmada. Histórias descartadas, revisões, testes com prefixo LAB-, simulações e tentativas malsucedidas não consomem número.

**Problema técnico central.** O número está impresso na imagem, então a imagem precisa de um número antes de existir confirmação. A solução é separar reserva de consumo.

**Livro-razão (ledger) append-only**, com estados por entrada:
- `reservado`: o próximo número livre é atribuído a uma tentativa, com chave de idempotência (hash do conteúdo mais janela da grade). Um bloqueio de escritor único impede duas reservas simultâneas.
- `confirmado`: só quando a plataforma devolve o identificador do story publicado. Aqui o número é consumido. Preferir o identificador da publicação, e não inferência por horário.
- `liberado`: falha comprovada de não publicação; o número volta a ser o próximo livre e o arquivo renderizado com ele é descartado.
- `inconclusivo`: resposta duvidosa ou tempo esgotado. O número fica retido, nada é publicado de novo, e uma conferência por identificador ou histórico decide entre `confirmado` e `liberado` antes de qualquer nova tentativa.

**Garantias.** Sem número duplicado (bloqueio e reserva única). Sem salto indevido (liberado reaproveita o número). Sem publicação duplicada (chave de idempotência e proibição de reenviar um `inconclusivo`). Auditoria completa (o ledger é histórico, nunca sobrescrito). Testes e simulações usam um contador separado com prefixo LAB-.

**Dependência a verificar.** Se o histórico de Stories da plataforma permite a conferência de um `inconclusivo` a tempo (os insights de Stories ficam cerca de 24 horas). Isto vai para o ensaio operacional.

---

## C. O que já pode avançar sem depender da conclusão editorial

| Frente | Pode avançar agora | Fica de fora |
|---|---|---|
| Núcleo de identidade | Documento formal pronto para a sua decisão: `pos_g3/NUCLEO_IDENTIDADE_PROPOSTA.md` (inclui a distinção BOA aberta contra AMBÍGUA insuficiente e o estoque que encolhe em vez de publicar fraco) | Homologação |
| Fase B visual | Especificação do Auditor Visual, com os critérios revisados (a foto não precisa mostrar o que o FORA revela, e antecipar a revelação é defeito), e plano de teste usando imagens geradas manualmente por você no Gemini, sem crédito. Cotação 9:16 pendente | Qualquer geração paga ou compra de créditos |
| Assinatura e contador | Especificação de B, com o wireframe | Alterar o contador ou o sistema de publicação |
| Ensaio operacional | Plano de falhas simuladas contra um publicador de mentira e um ledger local: erro no meio da publicação, resposta inconclusiva, duplicidade, fila vazia, estoque baixo, JSON do Crítico inválido, imagem reprovada, ordem de reserva em paralelo | Publicar de verdade, mexer no n8n |
| Estoque | Política de estoque: produção insuficiente reduz o disponível e nunca força publicação | Definir tamanho do estoque sem os dados da verificação |

Posso construir o publicador de mentira e o ledger local, com os testes, se você autorizar. Nada disso toca n8n, grade ou fila.

---

## D. Sequência curta e realista até a implantação controlada

1. **Decisões suas, em um lote:** aprovar ou ajustar o núcleo; autorizar a Emenda 2 e a verificação limitada de C1; escolher a posição na grade de dez postagens (substituir ou compartilhar uma janela existente, sem criar uma décima primeira).
2. **Verificação limitada de C1** (A.3), com decisão automática pela regra pré-registrada. Se "sem benefício claro", a v2.2 segue como está e a linha se encerra.
3. **Em paralelo, sem esperar o passo 2:** ledger local e ensaio de falhas simuladas; Auditor Visual e teste manual no Gemini; especificação final das assinaturas.
4. **Fase B:** cotação 9:16 real, decisão de modelo e orçamento, e as seis histórias aprovadas em um único lote de decisão.
5. **Ensaio operacional de ponta a ponta sem publicar**, com o contador LAB-, e relatório das falhas simuladas.
6. **Implantação controlada:** a v2.2 ou C1, conforme o passo 2, em baixo volume, com o contador real, estoque que encolhe em vez de forçar, e o Metricool só descritivo. Qualquer integração com o n8n e a primeira publicação real dependem de autorização específica sua.

Cada passo depende só dos anteriores indicados, e nenhum exige nova rodada de experimentos além da verificação do passo 2.
