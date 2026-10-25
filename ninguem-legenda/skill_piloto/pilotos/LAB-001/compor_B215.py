#!/usr/bin/env python3
"""Composição de TESTE do perfil B com rótulos em 215/255 , degradê do topo reforçado (0,65 até y 480), número colado ao nome da série e assinatura menor (22 px) (a skill e o perfil B oficial NÃO são alterados).
Uso: compor_B215.py FOTO SAIDA [--guias]"""
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, "../../o-que-ninguem-legenda-piloto/scripts")
import compor_story as cs
cs.PERFIS["B215"] = dict(cs.PERFIS["B"], rotulo_alpha=215, grad_topo_max=0.65, grad_topo_fim=480, assinatura_px=22, assinatura_trk=4)
# Layout de teste pedido por Eri: o número da série fica colado ao nome da série (à direita dele, com um respiro), em vez de alinhado à margem direita.
GAP_NUMERO = 34
_orig = cs.texto_trk
_estado = {}
def _texto_trk(d, xy, txt, f, fill, trk=0, ancora="l"):
    if txt == "O QUE NINGUÉM LEGENDA":
        caixa = _orig(d, xy, txt, f, fill, trk, ancora); _estado["fim_titulo"] = caixa[2]; return caixa
    if txt.startswith("LAB") and ancora == "r":
        return _orig(d, (_estado["fim_titulo"] + GAP_NUMERO, xy[1]), txt, f, fill, trk, "l")
    return _orig(d, xy, txt, f, fill, trk, ancora)
cs.texto_trk = _texto_trk
NA_FOTO = "Um guarda-chuva aberto secando no corredor."
FORA = "Era do irmão e passou dois anos no armário dela. Hoje ela o devolveu e ficou para almoçar."
r = cs.compor(sys.argv[1], NA_FOTO, FORA, "LAB-001", sys.argv[2], perfil="B215", simulacao=True, guias="--guias" in sys.argv)
print(r if not isinstance(r, dict) else {k: r[k] for k in ("aprovacao_tecnica", "falhas", "texto_alterado") if k in r})
