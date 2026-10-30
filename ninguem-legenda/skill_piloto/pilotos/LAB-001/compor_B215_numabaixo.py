#!/usr/bin/env python3
"""PROPOSTA VISUAL para Eri (NAO fixa coordenadas): perfil B215 com o numero "001" abaixo de @surtodelucidez, alinhado a esquerda da assinatura, 20% menor que o tamanho anterior (30 px -> 24 px). Assinatura mantida em 22 px (ultima composicao vista). A skill nao e alterada.
Uso: compor_B215_numabaixo.py FOTO SAIDA [--guias]"""
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, "../../o-que-ninguem-legenda-piloto/scripts")
import compor_story as cs
cs.PERFIS["B215N"] = dict(cs.PERFIS["B"], rotulo_alpha=215, grad_topo_max=0.65, grad_topo_fim=480, assinatura_px=22, assinatura_trk=4, numero_px=24)
GAP = 12
_orig = cs.texto_trk
def _t(d, xy, txt, f, fill, trk=0, ancora="l"):
    if txt.startswith("LAB") and ancora == "r":
        L = cs.PERFIS["B215N"]
        return _orig(d, (L["margem"], L["assinatura_y"] + L["assinatura_px"] + GAP), "001", f, fill, trk, "l")
    return _orig(d, xy, txt, f, fill, trk, ancora)
cs.texto_trk = _t
NA_FOTO = "Um guarda-chuva aberto secando no corredor."
FORA = "Era do irmão e passou dois anos no armário dela. Hoje ela o devolveu e ficou para almoçar."
r = cs.compor(sys.argv[1], NA_FOTO, FORA, "LAB-001", sys.argv[2], perfil="B215N", simulacao=True, guias="--guias" in sys.argv)
print(r if not isinstance(r, dict) else {k: r[k] for k in ("aprovacao_tecnica", "falhas", "texto_alterado") if k in r})
