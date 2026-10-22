"""Extrai páginas oficiais e confere a aritmética do material didático.

Executar com PYTHONPATH apontando para .tools (pypdf instalado localmente).
Não acessa rede nem modifica o PDF original.
"""
from pathlib import Path
import csv
import hashlib
import json
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dados"
original = DATA / "petrobras_2024.pdf"
reader = PdfReader(original)
writer = PdfWriter()
texts = []
for printed, page in [("F-3", 344), ("F-4", 345), ("F-6", 347)]:
    writer.add_page(reader.pages[page - 1])
    texts.append(f"PÁGINA IMPRESSA {printed} / PÁGINA PDF ORIGINAL {page}\n"
                 + reader.pages[page - 1].extract_text())
with (DATA / "petrobras_2024_demonstracoes.pdf").open("wb") as handle:
    writer.write(handle)
(DATA / "petrobras_2024_demonstracoes.txt").write_text("\n\n".join(texts), encoding="utf-8")
rows = list(csv.DictReader((DATA / "petrobras_2024_recorte.csv").open(encoding="utf-8")))
values = {row["conta"]: {year: int(row[year]) for year in ["2024", "2023"]} for row in rows}
for year in ["2024", "2023"]:
    initial = values["Caixa e equivalentes de caixa no início do exercício"][year]
    op = values["Recursos líquidos gerados pelas atividades operacionais"][year]
    inv = values["Recursos líquidos gerados (utilizados) nas atividades de investimentos"][year]
    fin = values["Recursos líquidos utilizados nas atividades de financiamentos"][year]
    fx = values["Efeito de variação cambial sobre caixa e equivalentes de caixa"][year]
    final = values["Caixa e equivalentes de caixa no fim do exercício"][year]
    assert initial + op + inv + fin + fx == final, year
    assert final == values["Caixa e equivalentes de caixa"][year], year
result = {
    "fonte": "Petrobras, Form 20-F 2024, tradução livre, US$ milhões, consolidado",
    "consulta": "2026-10-14",
    "pdf_sha256": hashlib.sha256(original.read_bytes()).hexdigest(),
    "paginas_pdf": [344, 345, 347],
    "liquidez_2024": values["Ativo circulante"]["2024"] / values["Passivo circulante"]["2024"],
    "liquidez_2023": values["Ativo circulante"]["2023"] / values["Passivo circulante"]["2023"],
    "margem_pct_2024": values["Lucro líquido do exercício"]["2024"] / values["Receita de vendas"]["2024"] * 100,
    "margem_pct_2023": values["Lucro líquido do exercício"]["2023"] / values["Receita de vendas"]["2023"] * 100,
    "variacao_receita_pct": (values["Receita de vendas"]["2024"] / values["Receita de vendas"]["2023"] - 1) * 100,
    "conciliacao_caixa_2024": "OK",
    "conciliacao_caixa_2023": "OK",
}
(ROOT / "verificacao" / "calculos.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
