# Produção autônoma (v1.0): passo a passo da tarefa diária

Rodar dentro de /home/claude/surto-teste-imagens/ninguem-legenda/skill_piloto/v0.2.1/o-que-ninguem-legenda-piloto (scripts da skill) ou da pasta da skill instalada. REG = /home/claude/surto-teste-imagens/ninguem-legenda/producao/registro_producao.csv.

0. Pré-requisitos: repositório clonado com escrita (PASSO 0 da tarefa diária); Kairogen carregada via ToolSearch (generate_image, estimate_cost); `pip install pillow numpy opencv-python-headless --break-system-packages` se faltar.
1. Se fila/D_1800_ninguemlegenda.png já existir, não gerar de novo.
2. Confirmar números: `python3 scripts/registro_numeracao.py listar --registro REG`; para cada RESERVADO com arquivo em publicadas/ (nome AAAAMMDD_1800_ninguemlegenda.png), `confirmar --id NL-NNN --data AAAA-MM-DD`. `verificar` deve passar.
3. Criador e filtros: 3 candidatas em JSON; `python3 scripts/filtros.py candidatas.json --registro REG`. Não repetir tema/mecanismo/situação das linhas do REG. Escolha a melhor.
4. Crítico v2.2: referência references/critico_operacao.md e critico_v2_2_referencia.md. Precisa BOA. Até 2 ciclos de revisão; senão abortar o dia.
5. Prompt: references/prompt_fotografico.md; `python3 scripts/checar_prompt.py`. Termine o prompt com "Gere uma única imagem." e a lista "Não incluir" (pessoa, mão, rosto, texto legível, letra, número, logotipo, marca d'água). Composição: elemento principal na metade superior/central; 20% inferiores e 13% superiores sem detalhes importantes.
6. Foto: generate_image model gpt-image-2, aspect_ratio 9:16, extra_params {"resolution":"2k"}, expected_credits 5, wait_for_completion true. Baixar a imagem (curl/python; se o download pelo shell for recusado, usar o arquivo local indicado no resultado da ferramenta). Olhar a foto (Read). Rodar `python3 scripts/analisar_foto.py FOTO` e `medir_inclinacao.py` quando houver objeto apoiado. Até 3 gerações no total; passando disso, abortar o dia e avisar Eri.
7. Registrar a história no REG como ARTE_APROVADA (linha NL-NNN com na_foto, fora_do_enquadramento, tema, situacao, mecanismo, conceito_foto, rosto=false) e `reservar`.
8. Compor: `python3 scripts/compor_story.py --foto FOTO --na-foto "..." --fora "..." --numero NNN --registro REG --id NL-NNN --perfil D --saida fila/AAAAMMDD_1800_ninguemlegenda.png`. Abrir o PNG (Read) e conferir: 1080x1920, texto idêntico, "NNN" sob o S e o U, título legível, nada em zona de segurança. Salvar também o .checagem.json (mesma pasta, fora de fila/: em ninguem-legenda/producao/saidas/).
9. commit e push (git pull --rebase antes). Conferir com git ls-tree que o arquivo está em origin/main.
10. Push curto para Eri: número, NA FOTO, FORA, veredicto do Crítico, créditos gastos, o que falhou.
Falha em qualquer etapa: não enfileirar, liberar número reservado (se houver) e avisar.
