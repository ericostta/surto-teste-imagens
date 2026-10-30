# Auditoria da foto v13 (ChatGPT), 30/10/2026

Arquivo: foto_real_L8CFD_chatgpt_v13.png, 940 x 1672 (proporção 0,5622, 9:16 dentro da tolerância), SHA-256 8ffdf53f1e106047686d03674118ddd646f1619dd479b80dc3779b04be11b41e. Resolução abaixo de 1080 x 1920 (aviso conhecido).

## Suporte físico (I1): atende
Ajuste de reta nos pixels escuros da haste (45 pontos): inclinação de 18,9 graus com o TOPO DA HASTE EM DIREÇÃO À PAREDE e a ponteira afastada, no piso, dentro da poça. O topo da copa encosta na parede. Configuração de escada apoiada, estável (a parede segura o topo; o atrito na ponteira segura a base). Corrige o defeito da v11 e da v12. Decisão visual e editorial continua com Eri.
Observação: a copa tem aparência levemente irregular (nervuras agrupadas do lado da parede). Não impede a leitura de guarda-chuva aberto, mas fica para o julgamento visual de Eri.

## Composição e legibilidade (I8): AJUSTAR (marginal)
A ponteira e a poça ficam na altura do rótulo NA FOTO, a cerca de 5 a 15 px acima do fim da primeira linha do texto na simulação, quase tocando o bloco. O título cruza a copa (texto claro sobre copa escura, legível).
Contraste efetivo (medir_contraste.py, layout com número no topo; ignorar o campo "numero"): título média 15,58, pior decil 3,62; rótulo NA FOTO média 2,89 (limite provisório 4,5), pior decil 2,55; texto NA FOTO 5,95 e 3,90; rótulo FORA 5,50 e 4,44; texto FORA 12,69 e 11,09; assinatura 6,48 e 6,15. Falha provisória: rótulo NA FOTO (sobre rodapé e parede claros). Limiares provisórios, não homologados.

## Opções
1. Aceitar a foto e tratar localmente só o tom atrás do rótulo NA FOTO (ajuste de luminância, sem alterar o objeto).
2. Uma correção ao gerador: subir o guarda-chuva cerca de 8% no quadro (ponteira acima de 52% da altura), o que afasta a poça do bloco de texto.
