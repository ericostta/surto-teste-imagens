#!/usr/bin/env python3
"""Mede a inclinação de uma haste ou objeto linear escuro em uma foto (PILOTO v0.2; ferramenta de APOIO, não substitui a leitura da imagem).
Uso: python3 scripts/medir_inclinacao.py FOTO.png X_TOPO Y_TOPO X_BASE Y_BASE --parede esquerda|direita [--janela 14] [--escuro 60]
Informe dois pontos aproximados sobre a haste (em pixels da foto original). O script ajusta uma reta aos pixels escuros ao redor da linha
informada e devolve o ângulo com a vertical e se o TOPO está voltado para a parede ou afastado dela.
Leitura para o defeito I1 (suporte físico): topo em direção à parede = apoio plausível (escada apoiada); topo afastado da parede sem outro
apoio = tende a cair; praticamente vertical (até 3 graus) sem apoio visível = suspeito de não ter suporte. A conclusão é do julgamento humano."""
import argparse, json, math, sys
from PIL import Image


def medir(foto, xt, yt, xb, yb, parede, janela=14, escuro=60):
    im = Image.open(foto).convert("L"); px = im.load(); W, H = im.size
    if yb == yt:
        raise ValueError("Y_TOPO e Y_BASE precisam ser diferentes")
    pts = []
    for y in range(min(yt, yb), max(yt, yb) + 1, 4):
        x0 = xt + (y - yt) * (xb - xt) / (yb - yt)
        xs = [x for x in range(int(x0) - janela, int(x0) + janela + 1) if 0 <= x < W and 0 <= y < H and px[x, y] < escuro]
        if xs:
            pts.append((y, sum(xs) / len(xs)))
    if len(pts) < 8:
        raise ValueError(f"pixels escuros insuficientes ao longo da linha informada ({len(pts)} pontos); ajuste os pontos, a janela ou o limiar --escuro")
    n = len(pts); my = sum(p[0] for p in pts) / n; mx = sum(p[1] for p in pts) / n
    a = sum((y - my) * (x - mx) for y, x in pts) / sum((y - my) ** 2 for y, x in pts)  # dx/dy, y cresce para baixo
    graus = math.degrees(math.atan(a))
    topo_para_esquerda = a > 0  # x cresce com y: o topo (y menor) fica mais à esquerda
    em_direcao = topo_para_esquerda if parede == "esquerda" else not topo_para_esquerda
    if abs(graus) <= 3:
        sentido = "praticamente vertical"
    else:
        sentido = "topo em direção à parede" if em_direcao else "topo afastado da parede"
    return {"pontos": n, "graus_com_a_vertical": round(abs(graus), 1), "sentido": sentido, "parede": parede,
            "nota": "ferramenta de apoio; a decisão sobre I1 é humana"}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("foto"); ap.add_argument("x_topo", type=int); ap.add_argument("y_topo", type=int)
    ap.add_argument("x_base", type=int); ap.add_argument("y_base", type=int)
    ap.add_argument("--parede", choices=["esquerda", "direita"], required=True)
    ap.add_argument("--janela", type=int, default=14); ap.add_argument("--escuro", type=int, default=60)
    a = ap.parse_args()
    try:
        print(json.dumps(medir(a.foto, a.x_topo, a.y_topo, a.x_base, a.y_base, a.parede, a.janela, a.escuro), ensure_ascii=False, indent=1))
    except ValueError as e:
        sys.exit(f"erro: {e}")
