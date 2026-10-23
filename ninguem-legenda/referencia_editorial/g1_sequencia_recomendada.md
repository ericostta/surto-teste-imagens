# G1: ordem recomendada entre congelamento da candidata e geração da validação

Data: 22/10/2026, cerca de 23h45. Fase A. Documento de recomendação. Nada foi implementado: não há sorteio, geração, prompt novo, execução, imagem ou alteração de grade, n8n, fila, publicadas ou skills.

## 1. Decisões de Eri de 23h42 registradas

- Lista de 60 conceitos aprovada preliminarmente, sem substituição por expectativa de qualidade.
- Sorteio determinístico por SHA-256 aprovado em princípio. Não executar agora. A frase-semente só será fornecida depois de satisfeitas as condições metodológicas anteriores.
- A proteção por ordem, hashes, registro de acessos e uso único é alternativa operacional razoável, mas não é isolamento técnico efetivo. Fica proibido afirmar que o conjunto esteve inacessível ao redator ou que os mecanismos impedem qualquer vazamento. Eles demonstram integridade documental e permitem auditoria parcial, e não provam ausência de acesso.
- Incompatibilidade a resolver: a candidata ainda não existe, e o protocolo exige candidata e protocolo de análise congelados antes dos itens. Não se pode gerar os 60 itens e depois desenvolver a candidata avaliada neles.
- Alternativas admissíveis: A, congelar a candidata antes da geração; B, lote de desenvolvimento separado e lote de validação produzido só depois do congelamento. Exemplos de desenvolvimento nunca contam como validação independente.

## 2. Recomendação: alternativa A

Definir e congelar a candidata antes de qualquer item de validação existir, desenvolvendo-a apenas com o material já queimado.

Por que A e não B:
- O material de desenvolvimento já existe e já está queimado para validação: W01 a W30 com seus rótulos, os conjuntos anteriores de calibração, as arbitragens de W05, W15 e W19 e a referência editorial. Um lote novo de desenvolvimento não acrescentaria independência, e custaria geração, rotulagem pelo ChatGPT e tempo de Eri.
- A mantém um único lote novo, que nasce inédito depois do congelamento.
- B só se justifica se Eri considerar o material queimado insuficiente para escrever a candidata. Nesse caso B vale, nas condições da seção 5.

O que A não resolve, e deve ser dito no relatório: a candidata será escrita por mim, que conheço o material queimado e a lista dos 60 conceitos. A lista é conhecida, mas o sorteio só ocorre depois do congelamento, então eu não saberei quais 30 conceitos compõem o fluxo.

## 3. Sequência de eventos

| Marco | Evento | Condição para passar |
|---|---|---|
| M0 | Eri aprova esta ordem e o hash definitivo da lista de 60 conceitos é registrado | autorização escrita de Eri |
| G0 | Desenvolvimento da candidata e dos instrumentos, só com material queimado | autorização expressa de Eri, separada de G1 |
| M1 | Congelamento: candidata, controles, instrumentos e protocolo de análise travados por hash e publicados; declaração de que o desenvolvimento terminou | revisão e autorização de Eri |
| M2 | Frase-semente de Eri e sorteio dos 30 conceitos do fluxo | M1 concluído |
| G1 | Geração dos itens por subagentes do Criador, manifesto por hash, varredura de vazamento | autorização expressa de Eri |
| G2 | Triagem lacrada, rótulos do ChatGPT lacrados, classificação humana às cegas, confronto | autorização expressa de Eri |
| G3 | Execuções dos Críticos e do julgador, auditoria, resultados lacrados, lote queimado | autorização expressa de Eri |

Regras de ordem: o sorteio vem depois do congelamento, para que quem desenvolve a candidata não conheça os conceitos do fluxo. Nenhum item existe antes de M1. Depois de M1, qualquer alteração de candidata, controle, instrumento ou protocolo queima o lote para a versão alterada e exige outro lote. Eu não escrevo nem edito os itens: eles são produzidos por subagentes que usam o `prompts/criador.md` atual e não recebem nenhum texto da candidata.

## 4. Arquivos e registros a criar (nenhum foi criado)

Em G0, sob autorização:
- prompt da candidata (nome a definir na autorização, por exemplo em `prompts/`) e, se necessário, prompt e procedimento do julgador de motivos, já aprovados em conceito;
- `g0_materiais_desenvolvimento.json`: lista fechada dos arquivos usados como material de desenvolvimento, com hash de cada um, todos marcados como queimados para validação;
- ajustes do validador e dos scripts de montagem de pacote, se precisarem existir, também congelados.

Em M1:
- `protocolo_analise_g1.md` e seu SHA-256: dimensões, tabela pareada, camadas de gravidade, critérios de melhora, igual, piora e inconclusivo, limiares para a decisão B, auditoria do julgador, cláusula de inferência;
- `marco_congelamento_g1.json`: hash de cada versão do teste (candidata, v2.2 como controle principal, v2.3-exp como controle secundário, e só enquanto não for ela a candidata), do protocolo, dos instrumentos e do hash da lista de 60 conceitos, mais a lista exata de arquivos da pasta no momento do marco (prova de que `validacao_g1/` ainda não existe);
- evidência externa de data: o horário do push no GitHub, que Eri pode conferir no histórico do repositório;
- `declaracao_fim_desenvolvimento.md`, assinada por Eri na autorização.

Em M2 e G1 (como já descrito em `g1_procedimento_sorteio.md` e `g1_protecao_conjunto_validacao.md`):
- registro da frase-semente e `sorteio_g1_resultado.json`;
- `validacao_g1/` com manifesto de hashes, `USO.json`, `registro_acessos_g1.jsonl` e o relatório da varredura de vazamento.

## 5. Se Eri preferir a alternativa B

- O lote de desenvolvimento é gerado em G0, com a mesma lista de procedimentos de rotulagem, mas com marca permanente "desenvolvimento, queimado": nunca entra na validação, nunca é apresentado como independente.
- Os 60 conceitos da validação permanecem fora do desenvolvimento: os conceitos do lote de desenvolvimento devem ser outros e não repetir nenhum deles.
- O lote de validação só é produzido depois de M1, com tudo o mais igual.
- O custo adicional é um lote a mais de itens, rótulos e triagem. O ganho é material de desenvolvimento novo e menos enviesado pelo que já foi visto.

## 6. Limitação que continua valendo

Esta sequência dá integridade documental e auditoria parcial. Não prova que a candidata não teve acesso, direto ou indireto, ao conjunto de validação, e o relatório final não poderá dizer que o conjunto esteve inacessível. Pode dizer que a ordem dos eventos, os hashes e os registros permitem verificar que a candidata foi congelada antes de os itens existirem.

## 7. O que preciso de Eri

1. Escolher A (recomendada) ou B.
2. Dizer se a candidata será uma versão nova, o que exige a autorização G0, ou se o teste se limitará às versões já existentes (v2.2 contra v2.3-exp), caso em que M1 é imediato mas o experimento não testa a referência editorial nova.
3. Autorizar a atualização de `g1_condicoes_documentais.md` e `g1_protecao_conjunto_validacao.md` para esta ordem, o que não envolve nenhuma geração.
