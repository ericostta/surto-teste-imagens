#!/usr/bin/env python3
"""Reserva e confirmação de números públicos no REGISTRO DO PILOTO (arquivo CSV). PILOTO MANUAL v0.1.1.
NÃO é o contador real do sistema de publicação e nunca o toca: só lê e escreve o CSV indicado em --registro.
Recusa o arquivo registro.csv do laboratório.

  reservar  --registro ARQ --id LAB-001            reserva o menor número livre (RESERVADO); antes da composição
  confirmar --registro ARQ --id LAB-001 [--data D] RESERVADO -> PUBLICADO; só depois que Eri confirmar a publicação manual
  liberar   --registro ARQ --id LAB-001 [--motivo] RESERVADO -> LIBERADO; falha ou cancelamento; o número volta a ficar livre
  listar    --registro ARQ
  verificar --registro ARQ                         duplicidades, formato e imutabilidade dos números confirmados

Números confirmados ficam também em um arquivo ao lado (<registro>.confirmados.jsonl, só acrescenta). `verificar` falha se um
número confirmado sumir, mudar de história ou for atribuído a outra. Testes e simulações usam LAB-: nunca consomem número.
"""
import argparse, csv, datetime, json, os, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from filtros import normalizar_estado  # fonte única dos estados

CAMPOS_PADRAO = "id,numero,data,estado,tema,situacao,mecanismo,emocao,tipo_contraste,abertura_fora,na_foto,fora_do_enquadramento,conceito_foto,rosto,avaliacao,justificativa_rejeicao,status_publicacao".split(",")
PODEM_RESERVAR = ("TEXTO_APROVADO", "FOTO_APROVADA", "ARTE_APROVADA")


class Erro(Exception):
    pass


def ler(caminho):
    with open(caminho, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r), r.fieldnames or CAMPOS_PADRAO


def gravar(caminho, linhas, campos):
    tmp = f"{caminho}.tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, lineterminator="\n")
        w.writeheader(); w.writerows(linhas)
    if os.path.exists(caminho):
        os.replace(caminho, f"{caminho}.bak")
    os.replace(tmp, caminho)


def sidecar(caminho):
    return f"{caminho}.confirmados.jsonl"


def confirmados_registrados(caminho):
    p = sidecar(caminho)
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def numeros_em_uso(linhas):
    """Números mantidos por RESERVADO ou PUBLICADO. LIBERADO libera o número."""
    return {int(l["numero"]) for l in linhas if normalizar_estado(l.get("estado")) in ("RESERVADO", "PUBLICADO") and str(l.get("numero", "")).strip().isdigit()}


def menor_livre(linhas, caminho):
    usados = numeros_em_uso(linhas) | {int(c["numero"]) for c in confirmados_registrados(caminho)}  # confirmado nunca volta
    n = 1
    while n in usados:
        n += 1
    return n


def achar(linhas, id_):
    for l in linhas:
        if l["id"] == id_:
            return l
    raise Erro(f"história {id_} não está no registro")


def verificar(caminho):
    linhas, _ = ler(caminho)
    falhas = []
    vistos = {}
    for l in linhas:
        e = normalizar_estado(l.get("estado")); n = str(l.get("numero", "")).strip()
        if e in ("RESERVADO", "PUBLICADO"):
            if not n.isdigit():
                falhas.append(f"{l['id']}: {e} sem número válido ('{n}')")
            elif int(n) in vistos:
                falhas.append(f"número {n} duplicado: {vistos[int(n)]} e {l['id']}")
            else:
                vistos[int(n)] = l["id"]
        elif n and e != "LIBERADO" and not l["id"].startswith("LAB-"):
            falhas.append(f"{l['id']}: número {n} em estado {e}")
    for c in confirmados_registrados(caminho):
        linha = next((l for l in linhas if l["id"] == c["id"]), None)
        if not linha or normalizar_estado(linha.get("estado")) != "PUBLICADO" or str(linha.get("numero", "")).strip() != c["numero"]:
            falhas.append(f"número confirmado {c['numero']} ({c['id']}) foi alterado ou removido")
        outro = next((l for l in linhas if l["id"] != c["id"] and str(l.get("numero", "")).strip() == c["numero"] and normalizar_estado(l.get("estado")) in ("RESERVADO", "PUBLICADO")), None)
        if outro:
            falhas.append(f"número confirmado {c['numero']} reutilizado por {outro['id']}")
    return falhas


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["reservar", "confirmar", "liberar", "listar", "verificar"])
    ap.add_argument("--registro", required=True); ap.add_argument("--id"); ap.add_argument("--data"); ap.add_argument("--motivo", default="")
    a = ap.parse_args(argv)
    if Path(a.registro).name == "registro.csv":
        raise Erro("recusado: registro.csv é o histórico do laboratório; use o registro do piloto (registro_piloto.csv)")
    if a.cmd == "verificar":
        f = verificar(a.registro)
        print("FALHAS:" if f else "registro do piloto consistente", *f, sep="\n")
        return 1 if f else 0
    linhas, campos = ler(a.registro)
    if a.cmd == "listar":
        for l in linhas:
            print(l["id"], normalizar_estado(l.get("estado")), l.get("numero") or "-", l.get("status_publicacao") or "")
        return 0
    if not a.id:
        raise Erro("--id obrigatório")
    problemas = verificar(a.registro)
    if problemas:
        raise Erro("registro inconsistente, corrija antes: " + "; ".join(problemas))
    l = achar(linhas, a.id); e = normalizar_estado(l.get("estado"))
    if a.cmd == "reservar":
        if e not in PODEM_RESERVAR:
            raise Erro(f"{a.id} está em {e}; só histórias aprovadas ({', '.join(PODEM_RESERVAR)}) recebem número")
        if str(l.get("numero", "")).strip():
            raise Erro(f"{a.id} já tem o número {l['numero']}")
        n = menor_livre(linhas, a.registro)
        l["numero"] = f"{n:03d}"; l["estado"] = "RESERVADO"; l["status_publicacao"] = "reservado"
        gravar(a.registro, linhas, campos)
        print(f"{a.id}: número {l['numero']} RESERVADO (ainda não consumido)")
    elif a.cmd == "confirmar":
        if e != "RESERVADO":
            raise Erro(f"{a.id} está em {e}; só RESERVADO pode ser confirmado")
        l["estado"] = "PUBLICADO"; l["status_publicacao"] = "publicado"
        l["data"] = a.data or datetime.date.today().isoformat()
        gravar(a.registro, linhas, campos)
        with open(sidecar(a.registro), "a", encoding="utf-8") as f:
            f.write(json.dumps({"id": a.id, "numero": l["numero"], "quando": datetime.datetime.now(datetime.timezone.utc).isoformat()}) + "\n")
        print(f"{a.id}: número {l['numero']} CONSUMIDO (publicação confirmada por Eri)")
    elif a.cmd == "liberar":
        if e != "RESERVADO":
            raise Erro(f"{a.id} está em {e}; só RESERVADO pode ser liberado (PUBLICADO nunca é liberado)")
        n = l["numero"]; l["numero"] = ""; l["estado"] = "LIBERADO"; l["status_publicacao"] = f"liberado:{n}" + (f" ({a.motivo})" if a.motivo else "")
        gravar(a.registro, linhas, campos)
        print(f"{a.id}: número {n} LIBERADO e disponível de novo")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Erro as e:
        print("ERRO:", e, file=sys.stderr); sys.exit(2)
