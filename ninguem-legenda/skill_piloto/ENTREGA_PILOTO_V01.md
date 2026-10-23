# O QUE NINGUÉM LEGENDA: PILOTO MANUAL v0.1 (entrega para conferência)

Data: 23/10/2026. Não é homologação do sistema, do layout nem do núcleo editorial.

## A. ZIP para a aba Habilidades
`skill_piloto/dist/o-que-ninguem-legenda-piloto-v0.1.zip` (22 arquivos, 0,7 MB, estrutura validada e extração testada). SHA-256 e hashes de cada arquivo em `REGISTRO_VERSAO_v0.1.json`. Gatilho provisório: `12!` ou o nome da série (ainda não usado pelas skills 1! a 11!; você pode trocar).

## B. Como a habilidade funciona e o que ela não faz
Fluxo manual em 8 passos, com portas suas:
1. Propõe uma história original (3 candidatas internas, filtros determinísticos, apresenta a melhor).
2. Crítico v2.2 consultivo (previsões cegas e avaliação em agentes isolados quando houver), com as limitações conhecidas declaradas.
3. Você decide: aprovar, revisar ou descartar. REVISAR nunca avança para imagem, máximo de 2 ciclos. AMBÍGUA nunca é apresentada como pronta.
4. Prompt fotográfico para Gemini/Nano Banana, em bloco de código, sem citar o FORA, conferido por script.
5. Você gera a foto manualmente.
6. Análise da foto: formato, fidelidade, ausência de antecipação, realismo, texto e marcas, composição para o texto. Resultado APTA, AJUSTAR ou REFAZER.
7. Composição do Story (script de layout provisório, 1080 x 1920).
8. Só depois da sua aprovação expressa a peça é considerada apta para publicação manual, feita por você.

Conteúdo: SKILL.md; referências (identidade editorial, Criador, operação do Crítico, Crítico v2.2 em cópia literal, prompt fotográfico, análise visual, assinatura e numeração, versão e limitações); scripts (filtros determinísticos, composição, medidas da foto, conferência de vazamento do prompt); fonte Inter (licença OFL); modelo de registro CSV.

Limitações: o Crítico v2.2 é provisório e pode aprovar o que você chamaria de AMBÍGUA; avaliadores são da mesma família de modelos; sem agentes disponíveis, as previsões perdem a condição de cegas (a skill avisa); a skill instalada não grava entre conversas, então o registro vive no CSV que você anexa e recebe de volta; layout, núcleo e numeração operacional não homologados. A C1b não está na skill. Os 12 textos do lote cego, os 60 da G1 e os 6 arbitrados não são usados como exemplo.

## C. Prompt fotográfico do guarda-chuva (L8CFD)
Arquivo `pilotos/LAB-001/prompt_gemini_L8CFD.txt` e bloco abaixo. Fiel ao conceito original, sem o vínculo familiar, sem o tempo, sem a devolução. A conferência de vazamento não encontrou palavra do FORA no prompt.

```
Fotografia realista de linguagem documental, formato vertical 9:16 (1080 x 1920).

Cena: um guarda-chuva preto grande, de cabo reto, aberto e em pé sobre o piso de porcelanato claro do corredor de um apartamento comum, com a copa levemente inclinada e encostada na parede lateral para secar. Gotas escorrem pelas varetas e pela borda do tecido, e uma pequena poça se forma sob ele. A porta de entrada do apartamento está entreaberta ao fundo, desfocada, deixando passar uma luz cinzenta de dia chuvoso.

Ambiente: corredor estreito e comum de apartamento, paredes lisas em tom claro, rodapé branco, piso de porcelanato bege acinzentado com reflexos suaves da água. Nada sobre o piso além do guarda-chuva e da poça.

Câmera: ponto de vista na altura do peito, levemente de frente e em ângulo suave, lente de 35 mm, profundidade de campo moderada (guarda-chuva nítido, fundo levemente desfocado).

Luz e cor: luz natural fria e difusa vinda da porta entreaberta, paleta contida em cinzas, bege frio e preto, sem cores saturadas.

Composição: guarda-chuva na metade superior e central do quadro, com ar ao redor; terço inferior do quadro mais calmo e escuro, apenas piso e reflexo suave, sem detalhes importantes nos 20% inferiores e nos 13% superiores.

Aparência: foto real, com aspecto de câmera de celular de boa qualidade, grão sutil, sem acabamento publicitário, sem aspecto de ilustração ou render.

Não incluir: nenhuma pessoa, mão ou rosto; nenhum texto, letra, número, logotipo, marca ou marca-d'água; nenhuma etiqueta, cartão, nome ou iniciais no guarda-chuva; nenhum segundo objeto além do guarda-chuva e do ambiente descrito.

Gere uma única imagem.
```

## D. Primeira proposta visual (SIMULAÇÃO, não é arte aprovada)
`pilotos/LAB-001/LAB-001_simulacao_visual.png` e `LAB-001_simulacao_guias.png` (com zonas de segurança). A foto é um marcador; o carimbo vermelho identifica a simulação.

| Critério | Proposta |
|---|---|
| Nome da série | Topo, esquerda, abaixo da zona de interface (y = 292 px), caixa alta, Inter SemiBold 30 px com espaçamento largo, branco 94%. Discreto, mas sempre no mesmo lugar |
| Número | Topo, direita, na mesma linha do nome, Inter Medium 30 px. LAB-001 no teste; 001, 002 quando público |
| Blocos | Parte inferior, sobre degradê escuro: NA FOTO primeiro (46 px, 88%), um filete curto, depois FORA DO ENQUADRAMENTO. O FORA é maior e mais pesado (56 px Medium, 100%) porque é a revelação |
| Rótulos | Os dois rótulos em caixa alta pequena (27 px, espaçados), para o texto ser o destaque |
| Assinatura | @surtodelucidez, 27 px, 65%, esquerda, abaixo do FORA e acima da zona inferior da interface. Sem competir |
| Fotografia | Cobre toda a tela 1080 x 1920. O degradê começa em 960 px; acima disso a foto fica limpa. Textos ocupam só a faixa 980 a 1480 px |
| Espaços | Margem lateral de 84 px, respiro de 58 px entre blocos, texto alinhado à esquerda |
| Celular | Texto principal de 46 a 56 px (cerca de 17 a 20 pt na tela); rótulos de 27 px são o limite inferior e devem ser testados no seu aparelho |
| Repetição | O script usa posições fixas e ajusta o corpo e as quebras de linha de forma equilibrada, avisando se o texto não cabe |

Pontos de atenção que precisam do seu olhar: a faixa inferior fica quase preta, o que pode pesar com fotos escuras; as zonas de 250 e 340 px são provisórias; a fonte Inter é escolha minha, não definida pela série.

## E. Decisões que dependem de você
1. Gatilho `12!` (ou outro).
2. Layout: posição, tamanho e peso do título; local e discrição da assinatura; posição e tamanho do número; ordem e hierarquia entre NA FOTO e FORA; força do degradê; fonte; margens.
3. Valores das zonas de segurança, a verificar no seu aparelho.
4. Confirmar L8CFD como BOA com detalhe FUNCIONAL no registro formal. Está registrada só como provisória, fora do lote cego lacrado.
5. Rotular imagens como geradas por IA (decisão ainda em aberto desde o início do projeto).
6. Posição da série na grade de dez publicações (decisão futura).
7. Homologar o núcleo editorial e o Crítico (pendentes).
8. Retomar ou não as 72 avaliações (suspensas, exigem nova confirmação sua; o lote cego das 12 segue aguardando seu registro).
9. Se L8CFD, por ser uma das 12 do lote cego, deve ficar fora de qualquer análise da C1b caso a verificação seja retomada, já que ela já recebeu atenção de produção. Minha sugestão: tratar como item de produção e registrar essa condição na análise.

## F. Registro da versão e integridade
PILOTO MANUAL v0.1, 23/10/2026. Verificação mecânica da Emenda 2 repetida (passou): v2.2, validador, M1, G1, G2 e G3 e a Emenda 2 sem alteração; `git diff` sem mudanças em prompts, instrumentos, referência editorial, validacao_g1, pos_g3 e verificacao_c1b. A skill foi construída em pasta própria (`skill_piloto/`). Não foram tocados: n8n (nunca acessado), grade, fila, publicadas, contador real, skills existentes (somente lidas como modelo de estrutura). Nenhuma imagem foi gerada, nada foi comprado e nada foi publicado. A verificação das 72 avaliações permanece suspensa e nenhum Crítico foi executado.
