# Auditoria da fotografia v4 tratada (L8CFD) e composição B

Data: 24/10/2026. Tratamento LIMITADO feito por Claude sobre uma CÓPIA da v4, a pedido de Eri ("calibrar a foto até dar certo"). O original (`foto_real_L8CFD_chatgpt_v4_original.png`, SHA-256 892198e648bcf4e37361a6d81d6260553441c7fc127ba5a484abaa29a25d12b9) permanece intacto. Nada publicado, nenhum número real consumido, skill intacta.

## O que foi feito
Script `tratar_piso.py` (fora da skill), parâmetros registrados em `tratamento_v4.json`: ganho suave de baixa frequência aplicado só ao piso (máscara com borda suavizada), que reduz reflexos claros e preserva a textura fina; cabo, poça, anéis e o reflexo logo sob o cabo ficam protegidos. Força 1,0, percentil-alvo 10, raio 12. Saída: `foto_real_L8CFD_chatgpt_v4_tratada.png` (SHA-256 ba2e0b73d8cd3f64382a5e82412c26e299b28141541488f4542251014beb37fc). Nada foi desenhado nem inventado: só a luminosidade do piso foi redistribuída. Mudou o piso, não o guarda-chuva, a haste, a copa ou a cena.

Iterações: quatro configurações testadas (força 0,8 a 1,0; percentil 10 a 50; raio 8 a 35). Em todas o contraste efetivo melhorou; a escolhida equilibra efeito e naturalidade, sem halos nem faixas visíveis na ampliação.

## Resultado (contraste efetivo com o alfa real do texto, média / pior decil)
| Elemento | v4 original | v4 tratada | v5 |
|---|---|---|---|
| Rótulo NA FOTO | 2,3 / 1,1 | 3,3 / 2,9 | 4,0 / 3,5 |
| Texto NA FOTO | 3,6 / 1,5 | 4,6 / 4,0 | 4,9 / 3,3 |
| Rótulo FORA | 4,2 / 2,5 | 4,9 / 4,4 | 4,9 / 4,0 |
| FORA | 11,0 / 9,1 | 11,6 / 9,8 | 12,2 / 10,4 |
| Assinatura | 8,8 / 8,0 | 10,4 / 10,0 | 10,6 / 10,3 |
| Título | 10,2 / 2,4 | 10,2 / 2,4 | 12,2 / 2,3 |

Pelos limiares provisórios (blocos de texto: média de pelo menos 4,5:1 e pior decil de pelo menos 3:1), o texto NA FOTO e o FORA agora passam; o rótulo NA FOTO é pequeno e fica em 3,3:1, legível mas o ponto mais fraco.

## O que continua pendente (não resolvível por tratamento)
1. **Copa e haste:** a v4 mantém o desalinhamento estimado de cerca de 22 graus entre o eixo da copa e o da haste; a haste inclina 7,4 graus para a parede. A decisão sobre perceptibilidade é do olho de Eri.
2. **Título e número sobre a copa:** o título cruza a copa e a janela (pior decil de 2,4:1, trecho sobre a janela) e o número LAB-001 fica sobre a borda da copa junto à parede. Escolha de composição de Eri; uma calibração do perfil B (por exemplo, gradiente superior mais forte) é possível, mas depende de aprovação.
3. **Transparência:** a imagem tratada deixa de ser a saída pura do gerador; o registro acima documenta o tratamento. Antes de publicar, vale conferir a política da plataforma sobre conteúdo gerado ou editado por IA.

Decisão da skill (proposta): foto v4 tratada APTA, condicionada à confirmação visual do ponto copa e haste; arte AJUSTAR apenas se Eri considerar inaceitável o título e o número sobre a copa.
