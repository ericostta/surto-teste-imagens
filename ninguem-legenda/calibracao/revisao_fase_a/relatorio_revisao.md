# Relatório: mecanismo REVISAR, falso negativo J06 e auditoria das reprovações

Data: 22/10/2026. Fase A, só texto. Referência editorial provisória: avaliação independente 2 do ChatGPT. Crítico v2.1 inalterado (SHA-256 do prompt 9910c786...2c15, conferido antes de cada execução). Veredictos travados do v2 e do v2.1 intactos.

## 1. J15 (mesa organizada): recuperada em 1 ciclo

Original: "Ele guarda tudo no lugar às sextas porque, na segunda, nunca sabe se ainda terá a mesa."
Motivo do REVISAR (v2.1, nota 58): a razão da mesa vazia (medo do desligamento) foi o palpite das 3 leituras cegas; a foto sem objetos pessoais já sugere esvaziamento.
Alterações do Criador (só o fora; foto e NA FOTO idênticos, então as 3 previsões foram reaproveitadas): manteve o ritual das sextas e a ausência de objetos pessoais, trocou o que ele revela.
Revisado (r1): "Toda sexta devolve a mesa como a encontrou. Cobre a licença de um colega e teme parecer que se instalou."
Filtros: sem falhas; alerta de mecanismo M07 repetido (só sinaliza).
Novo veredicto (Crítico limpo, sem ver original nem instrução): APROVADA, nota 80, 0 de 3 previsões capturaram, E1 a E5, "é a associação mais comum" = falso.
Justificativa do Crítico: a perspectiva do substituto que apaga os próprios rastros não é o palpite da categoria; um leitor volta à foto para reler a caneta alinhada como gesto de quem não quer ficar.
Comparação qualitativa: segunda leitura mais forte (de medo genérico de demissão para um constrangimento específico), originalidade claramente melhor, precisão narrativa boa. Ressalvas minhas, que o Crítico não levantou: (a) o ritual "toda sexta" perde a lógica original (fechar a semana); um substituto com esse receio arrumaria todo dia, e o Crítico chegou a parafrasear "todo dia"; (b) a plausibilidade depende de leitor aceitar um temor sutil. A aprovação não é validação externa: ninguém fora do Crítico avaliou o r1.

## 2. J01 (homem no elevador): falhou em 2 ciclos, descartada

Original: "É o último dia dele ali, e ninguém sabe. Pela primeira vez, ele não está com pressa."
Motivo do REVISAR (nota 38): revelação igual ao palpite de todos (demissão ou notícia); "último dia" sem motivo gera dois tons incompatíveis.
Ciclo 1 (r1): "Pediu demissão na semana passada. Hoje deixou três elevadores passarem e descobriu que, em nove anos, nunca precisou correr para pegar um."
Veredicto: REVISAR, nota 52, 3 de 3 previsões capturaram. Falhas: (a) defeito introduzido por mim, a oração "nunca precisou correr" admite leitura contraditória; (b) a demissão continuou no centro, o primeiro palpite.
Ciclo 2 (r2): "Nove anos correndo para pegar o elevador e gastando os minutos ganhos no celular. Hoje fez a conta e ficou parado."
Veredicto: REVISAR, nota 66, previsão "previu parte" (E2 satisfeita). Falhas: o fecho "ficou parado" não prova mudança nem é ato verificável e vira a moral de desacelerar; "fez a conta" sem termos; a foto participa pouco.
Resultado: limite de 2 ciclos atingido, não APROVADA, descartada conforme a regra. Nenhum ciclo 3.
Comparação qualitativa: o r2 é melhor que o original e que o r1 (tirou a demissão, ganhou o detalhe irônico dos minutos no celular, sem ambiguidade lógica), mas ainda não vale publicação. A ironia dos minutos no celular é o ativo a preservar se a ideia for retomada em outra foto.

## 3. Análise do falso negativo J06 (cardápio), resultado original preservado

- A reprovação não decorreu da previsibilidade isoladamente. A regra E2 só impede APROVADA; a REPROVADA veio de três eliminatórias: foto que entrega a revelação, redundância com a foto e clichê sem perspectiva específica.
- A evidência da previsibilidade é empírica: as três leituras cegas, todas com confiança alta, escreveram a ideia quase com as mesmas palavras, e uma delas até com o fingimento. Não é um artefato de penalização.
- Falha editorial concreta, minha como Criador: a descrição da foto traz "um dedo pousado na coluna da direita" e o fora diz "lê da direita para a esquerda", repetindo o gesto que a foto já mostra. O ChatGPT viu essa mesma foto e classificou BOA, descrevendo a situação como "não evidente na fotografia". Há divergência de critério sobre quanto o dedo entrega, e as leituras cegas sustentam o Crítico.
- Onde o v2.1 pode ser severo demais: "foto que entrega a revelação" está na lista fechada de REPROVADA, mas a descrição da foto é uma saída do Criador, barata de corrigir. O auditor independente concorda que a reprovação foi indevida (confiança média) e aponta a correção: tirar o dedo da coluna e deslocar o fora para o fingimento (o prato mais barato apresentado como o preferido).
- Conclusão: J06 é caso de fronteira da regra, não falha de previsibilidade. Hipótese não testada: uma versão com foto corrigida passaria. Nada foi alterado no Crítico; a decisão sobre permitir revisão da foto é de Eri e do ChatGPT.

## 4. Auditoria das reprovações

Auditoria cega por subagente independente (viu só foto, NA FOTO e fora, sem veredicto), régua dos critérios do Crítico, instruído a ser tão exigente quanto ele. Foram auditadas as 15 reprovações do v2.1, as 9 do conjunto 2 e as 6 do conjunto 1, não uma amostra.

- Justificadas: 13. Duvidosa: 1 (J17, mesa posta para quatro, confiança baixa; núcleo possível: ritual semanal de pôr a mesa para quatro e pacto de silêncio, com pronomes e "coragem" a corrigir). Indevida: 1 (J06).
- Cruzamento com rótulos externos: 14 das 15 eram RUIM (6 de Eri, 8 do ChatGPT); a única BOA é J06, a mesma que o auditor sinalizou. J17 é RUIM para o ChatGPT, então a dúvida do auditor não tem apoio externo.
- Nenhuma outra ideia promissora descartada indevidamente. Limite: auditor e Crítico são o mesmo tipo de modelo.

## 5. Diagnóstico sobre a eficácia do mecanismo de revisão

- Esta rodada: 1 de 2 recuperada (J15). Somada ao teste anterior (3 de 7 válidas), 4 de 9.
- O mecanismo funciona quando o defeito está no fora e a foto deixa espaço (J15). Falha quando a previsibilidade nasce da foto (J01 e, em outro grau, J06): revisar só o texto não tira o palpite que a foto já impõe.
- Dois modos de falha do Criador: introduzir defeito novo (J01 r1; antes LAB-005 e LAB-009) e cair em moral ao deslocar a revelação (J01 r2).
- Os critérios de aprovação foram demonstrados pelos campos do Crítico (elemento que muda, perspectiva específica, E1 a E5), mas o mesmo Crítico avalia o que o mesmo modelo revisou, sem checagem externa. Nenhuma revisão foi validada por outro avaliador.
- Confiável para o que se pede, recuperar ideias sem aprovar fracas: sim no sentido de não ter aprovado nada fraco (J01 foi barrada duas vezes). Confiável como máquina de recuperação: ainda não, a amostra é pequena e a taxa é metade.

Decisões que cabem a Eri e ao ChatGPT: (1) avaliar às cegas J15-r1 e J01-r2 como verificação externa; (2) decidir se a revisão pode alterar a descrição da foto e o NA FOTO (exigiria novas previsões cegas) e se "foto que entrega" deve virar REVISAR; (3) se vale um teste de J06 com foto corrigida.
