"""Extract chapter-level text (paragraphs + tables) per section of sections.json.

Output: _source/pages/<folder>/text.md, each block anchored to its source page.
Papermorph 'split_pages.py' equivalent for a DOCX source.
"""
import json
import re
from pathlib import Path

import docx
from docx.document import Document as Doc
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "ADBMS_MasterNotes.docx"
SECTIONS = json.loads((ROOT / "exam" / "sections.json").read_text(encoding="utf-8"))
PAGES = json.loads((Path(__file__).parent / "heading_pages.json").read_text(encoding="utf-8-sig"))

heading_page = {}
for r in PAGES:
    if r["style"].startswith("Heading") or r["style"] == "Title":
        heading_page.setdefault(r["text"].strip(), int(r["page"]))


def iter_blocks(parent):
    body = parent.element.body if isinstance(parent, Doc) else parent._element
    for child in body.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


doc = docx.Document(SRC)
blocks = list(iter_blocks(doc))

# Heading positions, and match them 1:1 in document order to sections.json
starts = []
for i, b in enumerate(blocks):
    if not isinstance(b, Paragraph):
        continue
    st, t = b.style.name, b.text.strip()
    if st == "Heading 1" and re.match(r"UNIT\s+\d+", t):
        continue  # unit banners are not sections in sections.json
    if st == "Heading 3":
        continue  # H3 = topic inside a section, not a section boundary
    if st.startswith("Heading"):
        starts.append((st, t, i))

assert len(starts) == len(SECTIONS), (len(starts), len(SECTIONS))
order = [(SECTIONS[n]["folder"], title, bi) for n, (st, title, bi) in enumerate(starts)]

out_root = ROOT / "_source" / "pages"
for n, (folder, title, bi) in enumerate(order):
    end = order[n + 1][2] if n + 1 < len(order) else len(blocks)
    lines = [f"# {title}", "", f"Source: ADBMS_MasterNotes.docx — folder `{folder}`", ""]
    page = None
    for b in blocks[bi:end]:
        if isinstance(b, Paragraph):
            t = b.text.rstrip()
            st = b.style.name
            if not t.strip():
                continue
            if st.startswith("Heading") or st == "Title":
                prefix = {"Title": "# ", "Heading 1": "## ", "Heading 2": "### ", "Heading 3": "#### "}.get(st, "#### ")
                lines.append(f"{prefix}{t.strip()}")
                if t.strip() in heading_page:
                    page = heading_page[t.strip()]
                    lines.append(f"_(p. {page})_")
            elif st.startswith("List"):
                lines.append(f"- {t.strip()}")
            else:
                lines.append(t)
        else:
            lines.append("")
            lines.append("| " + " | ".join(" ".join(c.text.split()) for c in b.rows[0].cells) + " |")
            lines.append("|" + "---|" * len(b.rows[0].cells))
            for row in b.rows[1:]:
                lines.append("| " + " | ".join(" ".join(c.text.split()) for c in row.cells) + " |")
            lines.append("")
    d = out_root / folder
    d.mkdir(parents=True, exist_ok=True)
    (d / "text.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

print(f"{len(order)} section text files -> {out_root}")
