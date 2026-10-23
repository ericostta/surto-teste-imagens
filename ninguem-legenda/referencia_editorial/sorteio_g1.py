#!/usr/bin/env python3
"""Sorteio verificável da etapa G1 (implementação de referência do procedimento).

Estado: documentação. NÃO foi executado sobre a lista real. Só será executado depois que
Eri (1) aprovar a lista, (2) tiver o hash da lista registrado e (3) fornecer a frase-semente.

Algoritmo (determinístico, reprodutível por qualquer pessoa com sha256):
  hash_lista = SHA-256 do JSON canônico da lista de conceitos aprovada
  pontuacao(id) = SHA-256( frase_semente + "|" + hash_lista + "|" + sal + "|" + id )
  ordena-se os ids por pontuacao crescente; os N primeiros formam a seleção; os seguintes
  formam a fila de reservas, usada apenas para exclusão técnica registrada.
O sal separa sorteios distintos (ex.: "g1-fluxo", "g2-controle-humano", "g3-auditoria-julgador").
"""
import hashlib, json, sys

def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def hash_lista(conceitos: list) -> str:
    canon = json.dumps(sorted(conceitos, key=lambda c: c["id"]), ensure_ascii=False,
                       sort_keys=True, separators=(",", ":"))
    return sha(canon)

def sortear(ids: list, frase: str, hlista: str, sal: str, n: int):
    pont = {i: sha(f"{frase}|{hlista}|{sal}|{i}") for i in ids}
    ordem = sorted(ids, key=lambda i: pont[i])
    return ordem[:n], ordem[n:], pont

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("lista_json"); ap.add_argument("--frase", required=True)
    ap.add_argument("--sal", required=True); ap.add_argument("--n", type=int, required=True)
    a = ap.parse_args()
    d = json.load(open(a.lista_json, encoding="utf-8"))
    conc = d["conceitos"]; h = hash_lista(conc)
    sel, res, pont = sortear([c["id"] for c in conc], a.frase, h, a.sal, a.n)
    print(json.dumps({"hash_lista": h, "sal": a.sal, "n": a.n, "selecionados_em_ordem": sel,
                      "reservas_em_ordem": res}, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
