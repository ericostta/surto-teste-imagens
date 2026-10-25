# Auditoria da foto v4 alinhada (copa e haste) de L8CFD

Data: 24/10/2026. Origem: `foto_real_L8CFD_chatgpt_v4_tratada.png` (sha256 ba2e0b73d8cd3f64382a5e82412c26e299b28141541488f4542251014beb37fc), que veio do original v4 (892198e6...). Todos preservados.
Resultado: `foto_real_L8CFD_chatgpt_v4_alinhada.png` (sha256 1bae7605e8b8bce497c607c7ffab0f1c175ce2c4622faa9d9373c4cd54cad69d). Script: `alinhar_copa.py ENTRADA SAIDA 20 30`.

## O que foi feito (divulgação obrigatória)
Edição estrutural, mais invasiva que o tratamento de piso: a copa foi recortada, girada 20 graus no sentido horário em torno do cubo (607,225) com deslocamento de 30 px, a haste original foi recolada e o fundo descoberto foi RECONSTRUÍDO por interpolação, com textura de reboco copiada de outro trecho da parede. Há pixels inventados na parede à direita e na porta à esquerda.

## Constatações
- Eixo da copa e haste agora coerentes (desalinhamento de cerca de 22 graus eliminado, avaliação visual; medição numérica final não refeita).
- Haste continua inclinada 7,4 graus em direção à parede, borda da copa encosta na parede: sustentação plausível.
- Artefatos residuais em zoom: remendo claro pequeno sob a borda da copa junto à haste; trecho de parede liso e fosco no canto superior direito da copa; leve borrão na área da porta. Em tamanho de Story são pouco perceptíveis, mas existem.
- Título e número LAB-001 caem sobre a copa (legíveis, contraste sobre fundo escuro); a faixa vermelha de simulação cobre parte da copa só na simulação.
- NA FOTO: rótulo pequeno ainda fraco (contraste estimado cerca de 3:1); calibração do perfil B segue pendente.
- Aprovação técnica do script: SIM. Aprovação visual e decisão de aceitar edição com pixels reconstruídos: de Eri.
- Política de rotulagem de conteúdo de IA das plataformas: não verificada.
