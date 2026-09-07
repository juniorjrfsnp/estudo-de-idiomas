#!/usr/bin/env python3
"""Merge phrase JSON files into index.html, programa.html and markdown."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
LANG_MD = [
    ("en", "Inglês"),
    ("es", "Espanhol"),
    ("fr", "Francês"),
    ("de", "Alemão"),
    ("ru", "Russo"),
    ("he", "Hebraico"),
    ("ar", "Árabe"),
    ("hi", "Hindi"),
    ("zh", "Chinês Mandarim"),
    ("no", "Norueguês"),
]
KEYS = ["num", "module", "pt", "en", "es", "fr", "de", "ru", "he", "ar", "hi", "zh", "no"]

NEW_MODULES = [
    {"id": "m13", "icon": "🏨", "title": "Hotel & Acomodação", "range": "201–220"},
    {"id": "m14", "icon": "✈️", "title": "Viagem & Transporte", "range": "221–240"},
    {"id": "m15", "icon": "🍽️", "title": "Restaurante & Pedidos", "range": "241–260"},
    {"id": "m16", "icon": "👕", "title": "Compras & Roupas", "range": "261–280"},
    {"id": "m17", "icon": "🏦", "title": "Banco & Documentos", "range": "281–300"},
    {"id": "m18", "icon": "📚", "title": "Estudo & Aprendizado", "range": "301–320"},
    {"id": "m19", "icon": "🏡", "title": "Casa & Conveniências", "range": "321–340"},
    {"id": "m20", "icon": "🩺", "title": "Saúde & Corpo", "range": "341–360"},
    {"id": "m21", "icon": "🎬", "title": "Lazer & Hobbies", "range": "361–380"},
    {"id": "m22", "icon": "🌿", "title": "Natureza & Ar Livre", "range": "381–400"},
    {"id": "m23", "icon": "☕", "title": "Convites & Relacionamentos", "range": "401–420"},
    {"id": "m24", "icon": "📞", "title": "Telefone & Chamadas", "range": "421–440"},
    {"id": "m25", "icon": "🔧", "title": "Problemas do Dia a Dia", "range": "441–460"},
    {"id": "m26", "icon": "⚖️", "title": "Preferências & Comparações", "range": "461–480"},
    {"id": "m27", "icon": "🗺️", "title": "Planos & Futuro", "range": "481–500"},
]

MODULE_MD_TITLES = {
    "m13": "## 🏨 Módulo 13: Hotel & Acomodação (Frases 201 a 220)",
    "m14": "## ✈️ Módulo 14: Viagem & Transporte (Frases 221 a 240)",
    "m15": "## 🍽️ Módulo 15: Restaurante & Pedidos (Frases 241 a 260)",
    "m16": "## 👕 Módulo 16: Compras & Roupas (Frases 261 a 280)",
    "m17": "## 🏦 Módulo 17: Banco & Documentos (Frases 281 a 300)",
    "m18": "## 📚 Módulo 18: Estudo & Aprendizado (Frases 301 a 320)",
    "m19": "## 🏡 Módulo 19: Casa & Conveniências (Frases 321 a 340)",
    "m20": "## 🩺 Módulo 20: Saúde & Corpo (Frases 341 a 360)",
    "m21": "## 🎬 Módulo 21: Lazer & Hobbies (Frases 361 a 380)",
    "m22": "## 🌿 Módulo 22: Natureza & Ar Livre (Frases 381 a 400)",
    "m23": "## ☕ Módulo 23: Convites & Relacionamentos (Frases 401 a 420)",
    "m24": "## 📞 Módulo 24: Telefone & Chamadas (Frases 421 a 440)",
    "m25": "## 🔧 Módulo 25: Problemas do Dia a Dia (Frases 441 a 460)",
    "m26": "## ⚖️ Módulo 26: Preferências & Comparações (Frases 461 a 480)",
    "m27": "## 🗺️ Módulo 27: Planos & Futuro (Frases 481 a 500)",
}


def load_extra() -> list[dict]:
    phrases = []
    for path in sorted(DATA_DIR.glob("extra_*.json")):
        chunk = json.loads(path.read_text(encoding="utf-8"))
        phrases.extend(chunk)
    phrases.sort(key=lambda p: p["num"])
    nums = [p["num"] for p in phrases]
    if nums != list(range(201, 501)):
        missing = sorted(set(range(201, 501)) - set(nums))
        extra = sorted(set(nums) - set(range(201, 501)))
        dups = sorted({n for n in nums if nums.count(n) > 1})
        raise SystemExit(f"Bad extra nums missing={missing} extra={extra} dups={dups} count={len(phrases)}")
    for p in phrases:
        for k in KEYS:
            if k not in p or p[k] in (None, ""):
                raise SystemExit(f"Missing {k} on phrase {p.get('num')}")
    return phrases


def replace_data(html: str, data_json: str) -> str:
    pattern = re.compile(r"const DATA = \{.*?\};\n\nconst LANG_LABELS", re.S)
    if not pattern.search(html):
        raise SystemExit("DATA block not found")
    return pattern.sub("const DATA = " + data_json + ";\n\nconst LANG_LABELS", html, count=1)


def update_html_copy(html: str) -> str:
    repls = [
        ("200 Frases Essenciais", "500 Frases Essenciais"),
        ("As 200 frases mais úteis", "As 500 frases mais úteis"),
        ("200 frases que abrem", "500 frases que abrem"),
        (">200</b><span>frases", ">500</b><span>frases"),
        (">12</b><span>módulos temáticos", ">27</b><span>módulos temáticos"),
        (">2.200</b><span>traduções", ">5.500</b><span>traduções"),
    ]
    for old, new in repls:
        html = html.replace(old, new)
    return html


def phrase_md(p: dict) -> str:
    lines = [f"### Frase {p['num']}: {p['pt']}"]
    for key, label in LANG_MD:
        lines.append(f"* **{label}:** {p[key]}")
    return "\n".join(lines) + "\n"


def extra_markdown(phrases: list[dict]) -> str:
    parts = ["\n---\n"]
    current = None
    for p in phrases:
        if p["module"] != current:
            current = p["module"]
            parts.append(MODULE_MD_TITLES[current] + "\n")
        parts.append(phrase_md(p))
    return "\n".join(parts)


def update_md_header(text: str) -> str:
    text = text.replace(
        "As 200 Frases Mais Usadas no Mundo",
        "As 500 Frases Mais Usadas no Mundo",
        1,
    )
    text = text.replace(
        "as 200 frases e expressões mais utilizadas no mundo",
        "as 500 frases e expressões mais utilizadas no mundo",
        1,
    )
    return text


def main() -> None:
    extra = load_extra()
    base = json.loads((DATA_DIR / "phrases_200.json").read_text(encoding="utf-8"))
    data = {
        "modules": base["modules"] + NEW_MODULES,
        "phrases": base["phrases"] + extra,
    }
    assert len(data["phrases"]) == 500, len(data["phrases"])
    compact = json.dumps(data, ensure_ascii=False, separators=(",", ":"))

    for name in ("index.html", "programa.html"):
        path = ROOT / name
        html = path.read_text(encoding="utf-8")
        html = replace_data(html, compact)
        html = update_html_copy(html)
        path.write_text(html, encoding="utf-8")
        print("updated", name)

    template = ROOT / "template.html"
    tpl = template.read_text(encoding="utf-8")
    tpl = update_html_copy(tpl)
    template.write_text(tpl, encoding="utf-8")
    print("updated template.html copy")

    md_path = ROOT / "Programa_de_Estudos_200_Frases_Multilingue.md"
    md = md_path.read_text(encoding="utf-8")
    md = update_md_header(md)
    # Insert extra modules before the tips section
    marker = "\n---\n\n## 💡 Dicas Especiais"
    if marker not in md:
        raise SystemExit("markdown marker not found")
    md = md.replace(marker, extra_markdown(extra) + marker, 1)
    out_md = ROOT / "Programa_de_Estudos_500_Frases_Multilingue.md"
    out_md.write_text(md, encoding="utf-8")
    md_path.write_text(md, encoding="utf-8")
    print("updated markdown", out_md.name, "and original file")

    (DATA_DIR / "phrases_500.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("wrote data/phrases_500.json")


if __name__ == "__main__":
    main()
