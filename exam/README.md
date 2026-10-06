# exam/ — ADBMS Exam Preparation System
**Source of truth:** `ADBMS_MasterNotes.docx` (36 pp., 5 units, 61 chapters) — unmodified.
Secondary source: `ADBMS_MemorizationSheet.docx` (derived high-value index, used to cross-check priorities).

> **Interactive website (new):** open `site/adbms/index.html` — or serve from the project root with
> `python -m http.server 8765` → http://localhost:8765/site/adbms/ (root serving keeps the
> `.md` source links working) —
> for the Papermorph-styled book: cover + contents, all 12 lessons with quick
> checks, graded sorter drills, the 54-MCQ arena, mocks with keys, cram sheet.
> Plus a Library of every source note as readable pages, a 96-Q written bank and a
> 140-card flip deck (both self-marking), 3 narrated lessons, and plain-language text.
> Progress saves in the browser; first tries count.

## Start here
- **Full guide + priority map:** [`notes/master-study-guide.md`](notes/master-study-guide.md)
- **Learn the subject:** [`notes/chapter-notes/unit-1..5.md`](notes/chapter-notes/) (every chapter, P0–P2 tagged)
- **Cram:** [`notes/final-cram.md`](notes/final-cram.md) · [`notes/ultra-short-notes.md`](notes/ultra-short-notes.md)
- **Plan your remaining time:** [`revision-plan.md`](revision-plan.md) (30 min / 1 h / 2 h / 4 h / final-30 / final-10)
- **Practise:** [`mock-exam-1.md`](mock-exam-1.md) → [`mock-exam-2.md`](mock-exam-2.md) → [`mock-exam-3.md`](mock-exam-3.md)
  (keys: `mock-exam-N-key.md`)
- **Track your errors:** [`weakness-tracker.md`](weakness-tracker.md)
- **Quality report:** [`completion-audit.md`](completion-audit.md)

## All note files (`notes/`)
`master-study-guide.md` · `definitions.md` · `formulas.md` · `processes-and-algorithms.md` ·
`comparisons.md` · `diagrams-and-mental-models.md` · `examples.md` · `common-mistakes.md` ·
`memory-hooks.md` · `flashcards.md` · `question-bank.md` (156 questions incl. 54 verified MCQs + 8 cross-unit combined + 6 gap-close) · `likely-questions.md` ·
`learning-path-from-zero.md` (12-lesson teach-from-scratch path merging all three artifact sets) ·
`classification-drills.md` (10 Papermorph-style sorter/multi-select drills with answer keys) ·
`answer-voices.md` (voice/verb/time doctrine per mark level) ·
`write-memorize-skip.md` (Tier-S top-10 WRITE|MEMORIZE|SKIP boxes with mark chunking) ·
`memorization-techniques.md` (apt device per topic: acronym/story/loci/discriminator + drill protocols) ·
`answer-bank.md` · `ultra-short-notes.md` · `final-cram.md` · `errata.md` · `chapter-notes/unit-1..5.md`

## Ingestion artifacts (Papermorph-style)
- `sections.json` — section map (folder, title, unit, start/end page, topics)
- `structure.md` — UNIT → CHAPTER → TOPIC tree with page references
- `../_source/pages/<folder>/text.md` — chapter-level extracted text, page-anchored
- `../_source/build_sections.py`, `extract_pages.py`, `audit.py` — reproducible pipeline + audit
