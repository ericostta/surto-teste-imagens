#!/usr/bin/env python3
"""Medidas objetivas da foto gerada (PILOTO v0.1): dimensões, proporção e luminância por zona.
Uso: python3 analisar_foto.py FOTO.png
Não substitui a leitura da imagem: apoia a checagem de formato e de composição para o texto."""
import sys
from PIL import Image


def lum(im):
    g = im.convert("L")
    h = g.histogram(); n = sum(h)
    return sum(i * c for i, c in enumerate(h)) / n / 255


def main():
    im = Image.open(sys.argv[1]).convert("RGB")
    w, h = im.size
    prop = w / h
    print(f"dimensões: {w} x {h}  proporção: {prop:.4f} (9:16 = {9/16:.4f})")
    print("9:16:", "sim" if abs(prop - 9 / 16) < 0.01 else "NÃO (será cortado ao cobrir 1080 x 1920)")
    if w < 1080 or h < 1920: print("AVISO: resolução abaixo de 1080 x 1920")
    zonas = {"topo (0-13%)": (0, .13), "centro (13-50%)": (.13, .5), "faixa dos blocos (50-76%)": (.5, .76), "base (76-100%)": (.76, 1)}
    for nome, (a, b) in zonas.items():
        z = im.crop((0, int(h * a), w, int(h * b)))
        print(f"luminância média {nome}: {lum(z):.2f}")
    faixa = lum(im.crop((0, int(h * .5), w, int(h * .76))))
    print("faixa dos blocos:", "clara (o degradê escurece, mas confira o contraste)" if faixa > .6 else "adequada para texto claro com o degradê")


if __name__ == "__main__":
    main()
