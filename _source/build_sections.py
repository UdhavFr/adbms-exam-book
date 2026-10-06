"""Papermorph-style section map from the DOCX heading tree + Word page numbers.

Source: ADBMS_MasterNotes.docx (36 pages, Word pagination).
Output: exam/sections.json  (schema follows Papermorph outline.py: folder/title/start/end/unit/chapter_start)
        exam/structure.md   (UNIT -> CHAPTER -> TOPIC tree with page refs)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows = json.loads((Path(__file__).parent / "heading_pages.json").read_text(encoding="utf-8-sig"))

# Order of headings in the document is the reading order.
sections = []
current_unit = None
current_chapter = None
for r in rows:
    style, text, page = r["style"], r["text"].strip(), int(r["page"])
    if style == "Heading 1":
        m = re.match(r"UNIT\s+(\d+)\s*[—-]\s*(.+)", text)
        if m:
            current_unit = f"UNIT {m.group(1)} — {m.group(2).strip()}"
            current_chapter = None
        else:
            # back matter blocks (answer bank, diagram sheet, revision, checklist)
            current_unit = "APPENDIX"
            slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:40]
            current_chapter = {"folder": "app_" + slug, "title": text, "unit": current_unit,
                               "start": page, "chapter_start": page, "topics": []}
            sections.append(current_chapter)
    elif style == "Heading 2" and current_unit:
        m = re.match(r"(\d+)\.\s*(.+)", text)
        num, title = (m.group(1), m.group(2).strip()) if m else ("?", text)
        current_chapter = {
            "folder": f"u{current_unit.split()[1] if current_unit.startswith('UNIT') else 'x'}ch{int(num):02d}" if current_unit.startswith("UNIT") else f"app{len(sections):02d}",
            "title": f"{num}. {title}" if m else text,
            "unit": current_unit,
            "start": page,
            "chapter_start": page,
            "topics": [],
        }
        sections.append(current_chapter)
    elif style == "Heading 3" and current_chapter is not None:
        current_chapter["topics"].append({"title": text, "page": page})

# end page = next section's start page - 1 (last section ends on the final page)
for i, s in enumerate(sections):
    s["end"] = (sections[i + 1]["start"] - 1) if i + 1 < len(sections) else 36
    if s["end"] < s["start"]:
        s["end"] = s["start"]

out = []
for s in sections:
    out.append({k: s[k] for k in ("folder", "title", "unit", "start", "end", "chapter_start")} | {"topics": s["topics"]})

(ROOT / "exam").mkdir(exist_ok=True)
(ROOT / "exam" / "sections.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

lines = ["# ADBMS — Structure Map (UNIT → CHAPTER → TOPIC)", "",
         "Source: `ADBMS_MasterNotes.docx` (authoritative base material, 36 pp. by Word pagination).",
         "Page references come from Word's pagination of the original file; the DOCX has no fixed PDF pages,",
         "so these are the reproducible source anchors (`_source/heading_pages.json`).", ""]
for s in out:
    if not s["unit"].startswith("UNIT"):
        continue
    lines.append(f"## {s['unit']}  →  {s['title']}  (pp. {s['start']}–{s['end']})")
    lines.append(f"- folder: `{s['folder']}`")
    for t in s["topics"]:
        lines.append(f"  - {t['title']} (p. {t['page']})")
    lines.append("")
lines.append("## APPENDIX (answer bank / diagrams / final revision / checklist)")
for s in out:
    if s["unit"].startswith("UNIT"):
        continue
    lines.append(f"- {s['title']} (pp. {s['start']}–{s['end']}) — {len(s['topics'])} sub-sections")
(ROOT / "exam" / "structure.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

units = {}
for s in out:
    units.setdefault(s["unit"], []).append(s)
print(f"{len(out)} sections, {len([s for s in out if s['unit'].startswith('UNIT')])} chapters, "
      f"{sum(len(s['topics']) for s in out)} topics/subtopics across {len(units)} units")
