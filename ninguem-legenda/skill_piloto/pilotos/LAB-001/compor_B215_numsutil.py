#!/usr/bin/env python3
"""PROPOSTA VISUAL (NAO fixa coordenadas). Numero "001" sutil sob @surtodelucidez, a partir do feedback de Eri (29/10, 23:56).
Variante A: assinatura no lugar atual (esquerda, 22 px); 001 com 14 px (altura do digito proxima do x-height da assinatura), alfa baixo.
Variante B: formato do Circulo Tipografico transposto: assinatura centralizada, 001 centralizado, proporcao 9/26 (35%) -> 8 px, cinza #8A8A8A.
Variante C: igual a A, mas 001 em 8 px (proporcao 9/26 do Circulo Tipografico), alinhado a esquerda, cinza #8A8A8A.
Uso: compor_B215_numsutil.py FOTO SAIDA A|B|C"""
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, "../../o-que-ninguem-legenda-piloto/scripts")
import compor_story as cs
VAR = sys.argv[3]
NUM_PX = {"A": 14, "B": 8, "C": 8}[VAR]
cs.PERFIS["S"] = dict(cs.PERFIS["B"], rotulo_alpha=215, grad_topo_max=0.65, grad_topo_fim=480, assinatura_px=22, assinatura_trk=4, numero_px=NUM_PX)
L = cs.PERFIS["S"]
_o = cs.texto_trk
_s = {}
def _t(d, xy, txt, f, fill, trk=0, ancora="l"):
    W = 1080
    if txt == "@surtodelucidez":
        if VAR == "B":
            w = cs.largura(d, txt, f, trk); _s["cx"] = W / 2
            return _o(d, (W / 2 + w / 2, xy[1]), txt, f, fill, trk, "r")
        _s["cx"] = None
        return _o(d, xy, txt, f, fill, trk, ancora)
    if txt.startswith("LAB") and ancora == "r":
        y = L["assinatura_y"] + L["assinatura_px"] + (8 if VAR == "A" else 6)
        fill = (255, 255, 255, 150 if VAR == "A" else 138)
        if VAR == "B":
            w = cs.largura(d, "001", f, 1)
            return _o(d, (W / 2 + w / 2, y), "001", f, fill, 1, "r")
        return _o(d, (L["margem"], y), "001", f, fill, 3, "l")
    return _o(d, xy, txt, f, fill, trk, ancora)
cs.texto_trk = _t
NA_FOTO = "Um guarda-chuva aberto secando no corredor."
FORA = "Era do irmão e passou dois anos no armário dela. Hoje ela o devolveu e ficou para almoçar."
# assinatura e numero sao desenhados em ordem fixa pela skill; o numero vem antes da assinatura
r = cs.compor(sys.argv[1], NA_FOTO, FORA, "LAB-001", sys.argv[2], perfil="S", simulacao=True)
print(VAR, {k: r[k] for k in ("aprovacao_tecnica", "falhas") if k in r} if isinstance(r, dict) else r)
