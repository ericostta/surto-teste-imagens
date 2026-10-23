#!/usr/bin/env python3
"""Regressão das falhas da v0.1 apontadas na auditoria de 23/10/2026.
Extrai o filtros.py do ZIP v0.1 (preservado) e do código v0.1.1 e compara o comportamento com o mesmo registro.
Execução: python3 skill_piloto/testes_regressao/test_falhas_v01.py (a partir de ninguem-legenda/)."""
import csv, importlib.util, json, sys, tempfile, unittest, zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
ZIP_V01 = BASE / "dist" / "o-que-ninguem-legenda-piloto-v0.1.zip"
V011 = BASE / "o-que-ninguem-legenda-piloto" / "scripts"
CAMPOS = "id,numero,data,estado,tema,situacao,mecanismo,emocao,tipo_contraste,abertura_fora,na_foto,fora_do_enquadramento,conceito_foto,rosto,avaliacao,justificativa_rejeicao,status_publicacao".split(",")
NA = "Um relógio parado na parede da sala."
FORA = "Parou no minuto em que o último morador se mudou, e ninguém teve coragem de trocar a pilha."


def carregar(dir_scripts):
    sys.path.insert(0, str(dir_scripts))
    for m in ("filtros",): sys.modules.pop(m, None)
    spec = importlib.util.spec_from_file_location("filtros", Path(dir_scripts) / "filtros.py")
    mod = importlib.util.module_from_spec(spec); sys.modules["filtros"] = mod; spec.loader.exec_module(mod)
    sys.path.pop(0); return mod


def registro(estado, d):
    p = Path(d) / "registro_piloto.csv"
    with open(p, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS, lineterminator="\n"); w.writeheader()
        w.writerow({c: "" for c in CAMPOS} | dict(id="LAB-001", estado=estado, mecanismo="M03", emocao="cotidiano", abertura_fora="parou no minuto", na_foto=NA, fora_do_enquadramento=FORA, rosto="false"))
    return p


def candidata():
    return dict(id="LAB-900", tema="x", situacao="y", mecanismo="M05", emocao="afeto", tipo_contraste="cena_vs_autor_da_cena", na_foto=NA, fora=FORA, conceito_foto="Relógio parado.", rosto=False)


def n_historico(mod, p):
    mod.REGISTRO = p
    return len(mod.carregar_historico())


class Regressao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp()
        with zipfile.ZipFile(ZIP_V01) as z:
            z.extractall(cls.tmp)
        achados = list(Path(cls.tmp).rglob("scripts/filtros.py"))
        assert achados, "filtros.py não encontrado no ZIP v0.1"
        cls.v01 = carregar(achados[0].parent)
        cls.v011 = carregar(V011)

    def test_v01_ignorava_publicado(self):
        p = registro("PUBLICADO", tempfile.mkdtemp())
        self.assertEqual(n_historico(self.v01, p), 0, "falha da v0.1 não reproduzida: PUBLICADO deveria ser ignorado")

    def test_v011_carrega_publicado(self):
        p = registro("PUBLICADO", tempfile.mkdtemp())
        self.assertEqual(n_historico(self.v011, p), 1)

    def test_v01_aceitava_publicada_e_v011_tambem(self):
        p = registro("PUBLICADA", tempfile.mkdtemp())
        self.assertEqual(n_historico(self.v01, p), 1); self.assertEqual(n_historico(self.v011, p), 1)

    def test_repeticao_de_publicado_passava_na_v01_e_e_barrada_na_v011(self):
        p = registro("PUBLICADO", tempfile.mkdtemp())
        self.v01.REGISTRO = p; self.v011.REGISTRO = p
        r01 = self.v01.avaliar(candidata(), self.v01.carregar_historico(), [candidata()])
        r011 = self.v011.avaliar(candidata(), self.v011.carregar_historico(), [candidata()])
        self.assertFalse(any("quase repetição" in f for f in r01["falhas"]), "v0.1 deveria deixar passar")
        self.assertTrue(any("quase repetição" in f for f in r011["falhas"]), "v0.1.1 deveria barrar")


if __name__ == "__main__":
    unittest.main(verbosity=2)
