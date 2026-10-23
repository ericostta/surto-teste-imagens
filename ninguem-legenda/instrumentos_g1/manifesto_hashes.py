#!/usr/bin/env python3
"""Manifesto de hashes SHA-256 (instrumento). Subcomandos:
  gerar ARQ... --saida manifesto.json    calcula e grava os hashes
  verificar manifesto.json               recalcula e compara; saída 1 se algum arquivo mudou ou sumiu
Usado para a lista de materiais de desenvolvimento (G0) e, só com autorização de Eri, para o marco M1."""
import hashlib, json, os, sys


def sha_arquivo(p: str) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def gerar(arquivos):
    return {os.path.relpath(a): sha_arquivo(a) for a in sorted(arquivos)}


def verificar(manifesto: dict):
    diffs = []
    for a, h in manifesto.items():
        if not os.path.exists(a):
            diffs.append((a, "ausente"))
        elif sha_arquivo(a) != h:
            diffs.append((a, "hash diferente"))
    return diffs


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    if sys.argv[1] == "gerar":
        args = sys.argv[2:]
        k = args.index("--saida")
        m = gerar(args[:k])
        json.dump(m, open(args[k + 1], "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print(f"{len(m)} arquivos")
    elif sys.argv[1] == "verificar":
        m = json.load(open(sys.argv[2], encoding="utf-8"))
        d = verificar(m)
        for a, motivo in d:
            print(f"{motivo}: {a}")
        print("íntegro" if not d else f"{len(d)} divergências")
        sys.exit(1 if d else 0)

if __name__ == "__main__":
    main()
