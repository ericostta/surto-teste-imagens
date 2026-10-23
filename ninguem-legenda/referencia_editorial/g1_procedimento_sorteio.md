# G1: procedimento de seleção e sorteio dos conceitos do fluxo

Data: 22/10/2026. Fase A. Documento de procedimento. O sorteio NÃO foi executado. A implementação de referência (`sorteio_g1.py`) foi testada somente com uma lista sintética, sem relação com a lista real, e não foi rodada sobre `g1_conceitos_candidatos.json`.

## 1. Ordem dos passos (cada um só depois do anterior)

1. Eri revisa e aprova a lista de conceitos. Alterações, se houver, são registradas.
2. Calcula-se o hash canônico da lista aprovada (SHA-256), registra-se no documento de aprovação e o registro é commitado e publicado.
3. Eri fornece a frase-semente. A frase é escolhida por ela depois do passo 2, não por mim, e é registrada por extenso no mesmo documento antes do cálculo. Eu não sugiro nem prevejo a frase.
4. Executa-se o sorteio com `sorteio_g1.py`, uma única vez, com o sal "g1-fluxo" e N igual a 30.
5. Registra-se a saída completa (hash da lista, sal, N, ordem dos selecionados, ordem das reservas) em arquivo, e esse arquivo é commitado e publicado antes de qualquer texto ser gerado.
6. Só então, com autorização expressa de Eri para gerar, começa a produção dos textos pelos 30 conceitos selecionados, na ordem do sorteio.

## 2. Algoritmo

pontuação(id) = SHA-256( frase_semente | hash_da_lista | sal | id ). Ordenam-se os ids pela pontuação, do menor para o maior. Os 30 primeiros formam a amostra de fluxo, e a ordem do sorteio é a ordem de produção. Os seguintes formam a fila de reservas.

Propriedades que Eri ou qualquer pessoa pode conferir: determinístico (mesma entrada, mesma saída); independe da ordem em que a lista foi escrita; qualquer alteração na lista muda o hash e portanto o resultado; a frase é de Eri, e o sal impede que o mesmo sorteio seja reutilizado para outro fim. O arquivo `sorteio_g1.py` tem cerca de 40 linhas e usa só a biblioteca padrão do Python. Qualquer ferramenta que calcule SHA-256 reproduz o resultado.

## 3. Reservas e exclusões

- Um conceito sorteado só pode ser substituído por exclusão técnica constatada antes da escrita de qualquer texto: violação das regras de foto (rosto identificável, texto legível, marca, tema vetado) descoberta depois da aprovação, ou duplicidade com um conceito da amostra de desafio. Substitui-se pelo próximo da fila de reservas, na ordem do sorteio.
- Cada substituição entra no log de exclusões com o conceito, o motivo, quem decidiu e quando.
- É proibido excluir ou substituir por expectativa de qualidade, por tipo de história esperado ou por qualquer rótulo. Não há novo sorteio.
- Se faltarem reservas, o fluxo fica com menos de 30 itens e isso é declarado, sem completar à mão.

## 4. Outros sorteios previstos, mesma regra

Cada um usa um sal próprio, é registrado antes de ser executado e nunca é refeito: controle humano de 20% dos itens sem conflito de triagem (mínimo de 10; sal "g2-controle-humano") e amostra de auditoria do julgador (mínimo de 20% e de 10, mais cobertura dos principais tipos de veredicto; sal "g3-auditoria-julgador"). Para esses, a frase-semente também é de Eri, e a lista de ids sorteáveis é lacrada por hash antes.

## 5. O que o sorteio não garante

Selecionar conceitos de modo imparcial não garante que os textos produzidos sejam representativos do processo normal: isso depende de a produção seguir o processo normal sem triagem (g1_condicoes_documentais.md, seção 2.2). Trinta itens são uma amostra pequena, e as contagens serão lidas com intervalos.
