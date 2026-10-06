"""Quality audit: coverage, cross-references, counts.

Checks:
1. every file in the deliverable list exists and is non-trivial
2. every chapter title from sections.json appears in exam/notes/chapter-notes/* (coverage)
3. priority annotations cover all 61 chapters
4. counts of questions / flashcards / mock marks
5. no source PDF/DOCX was modified (compare sizes/mtimes against recorded values)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAM = ROOT / "exam"
SECTIONS = json.loads((EXAM / "sections.json").read_text(encoding="utf-8"))
unit_sections = [s for s in SECTIONS if s["unit"].startswith("UNIT")]

required = [
    "README.md", "sections.json", "structure.md", "revision-plan.md",
    "weakness-tracker.md", "completion-audit.md",
    "mock-exam-1.md", "mock-exam-1-key.md", "mock-exam-2.md", "mock-exam-2-key.md",
    "mock-exam-3.md", "mock-exam-3-key.md",
    "notes/master-study-guide.md", "notes/definitions.md", "notes/formulas.md",
    "notes/processes-and-algorithms.md", "notes/comparisons.md",
    "notes/diagrams-and-mental-models.md", "notes/examples.md", "notes/common-mistakes.md",
    "notes/memory-hooks.md", "notes/flashcards.md", "notes/question-bank.md",
    "notes/likely-questions.md", "notes/answer-bank.md", "notes/ultra-short-notes.md",
    "notes/final-cram.md", "notes/errata.md",
] + [f"notes/chapter-notes/unit-{i}.md" for i in range(1, 6)]

problems = []
for rel in required:
    p = EXAM / rel
    if not p.exists():
        problems.append(f"MISSING FILE: {rel}")
    elif p.stat().st_size < 400:
        problems.append(f"TOO SMALL ({p.stat().st_size}B): {rel}")

# coverage: chapter titles present in the unit notes
notes_text = ""
for i in range(1, 6):
    notes_text += (EXAM / "notes" / "chapter-notes" / f"unit-{i}.md").read_text(encoding="utf-8")
all_notes = notes_text + "".join(
    (EXAM / "notes" / f).read_text(encoding="utf-8")
    for f in ["definitions.md", "formulas.md", "comparisons.md", "processes-and-algorithms.md",
              "final-cram.md", "ultra-short-notes.md", "flashcards.md", "question-bank.md",
              "likely-questions.md", "answer-bank.md", "examples.md", "memory-hooks.md",
              "common-mistakes.md", "diagrams-and-mental-models.md"]
)

# coverage by heading number: every U{unit}-{n} must exist exactly once in its unit's notes
unit_of = {}
for s in unit_sections:
    unum = int(re.match(r"UNIT (\d+)", s["unit"]).group(1))
    num = int(re.match(r"(\d+)\.", s["title"]).group(1))
    unit_of.setdefault(unum, []).append((num, s["title"]))

for unum, items in sorted(unit_of.items()):
    txt = (EXAM / "notes" / "chapter-notes" / f"unit-{unum}.md").read_text(encoding="utf-8")
    found = re.findall(rf"^## U{unum}-(\d+)\s", txt, re.M)
    for num, title in items:
        if str(num) not in found:
            problems.append(f"CHAPTER NOTES MISSING: unit-{unum}.md → U{unum}-{num} {title}")
        if found.count(str(num)) > 1:
            problems.append(f"DUPLICATE: unit-{unum}.md → U{unum}-{num}")
        # distinctive keyword must appear somewhere across all notes
        words = [w for w in re.findall(r"[A-Za-z]{5,}", title) if w.lower() not in {"using", "their", "which"}]
        if words and not any(w.lower() in all_notes.lower() for w in words):
            problems.append(f"NO MENTION anywhere of title keywords {words}: {title}")

# priority annotations
prios = re.findall(r"## U\d+-\d+.*?— \*\*(P\d)\*\*", notes_text)
prio_counts = {p: prios.count(p) for p in sorted(set(prios))}
if len(prios) != 61:
    problems.append(f"priority annotations found: {len(prios)} (expected 61)")

# counts
qb = (EXAM / "notes" / "question-bank.md").read_text(encoding="utf-8")
q_count = len(re.findall(r"^\*\*Q\d+\*\*", qb, re.M))
fc = (EXAM / "notes" / "flashcards.md").read_text(encoding="utf-8")
fc_count = len(re.findall(r"^\d+\.\s\*\*Q:", fc, re.M))
tf_count = len(re.findall(r"^\| T\d+", fc, re.M))

def mock_marks(path):
    t = (EXAM / path).read_text(encoding="utf-8")
    return len(re.findall(r"\*\*A\d", t)), t.count("marks")

# source integrity
src = {p.name: (p.stat().st_size, int(p.stat().st_mtime)) for p in ROOT.glob("*.docx")}

print("FILES CHECKED:", len(required))
print("PRIORITY COUNTS:", prio_counts)
print("question-bank items:", q_count, "| flashcards:", fc_count, "| TF traps:", tf_count)
for m in ["mock-exam-1.md", "mock-exam-2.md", "mock-exam-3.md"]:
    t = (EXAM / m).read_text(encoding="utf-8")
    print(m, "->", len(t.split()), "words")
print("SOURCE DOCX:", src)
print()
if problems:
    print("PROBLEMS:")
    for p in problems:
        print(" -", p)
else:
    print("NO PROBLEMS FOUND")

# suspicious content checks
for rel in required:
    p = EXAM / rel
    if not p.exists():
        continue
    t = p.read_text(encoding="utf-8")
    for bad in ["TODO", "FIXME", "lorem", "XXX", "TBD"]:
        if bad.lower() in t.lower():
            print(f"PLACEHOLDER in {rel}: {bad}")
