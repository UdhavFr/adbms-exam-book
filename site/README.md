# ADBMS Exam Book — static site

Papermorph-styled, exam-optimized study site built from `exam/`.
Deliberate deviation from the full Papermorph pipeline (user request overrides
defaults): no TTS narration / animated SVG beats — the exam is tomorrow, so
every page is active-recall shaped instead (lessons + quick checks + graded
drills + mocks). Visual language (chalkboard theme, cover + contents, unit
cards, localStorage progress, first-attempt scoring) follows the Papermorph
book implementation in `_papermorph/site/elementary-algebra/`.

## Preview

Serve from the **project root** (so the site's links to `exam/*.md` source files resolve):

```sh
python -m http.server 8765
```

Open http://localhost:8765/site/adbms/ (cover → contents → chapters).
`file://` works too. Serving only `site/` (old instruction) breaks the `.md` source links.

## Contents

20 chapters in 6 units: 12 lessons (from `learning-path-from-zero.md`, each with its
apt memory-device box), 2 narrated lessons (ch19 ladder, ch20 ACID),
classification drills (interactive sorters + multi-select, first-attempt
graded), a 54-MCQ rapid-fire arena (verified imports from the two co-located
AI artifacts), 3 mocks with keys in `<details>`, the final cram sheet.
Plus `plan.html` (revision plans, unnumbered) and `voices.html`,
`wms.html`, `test.html` (answer voices, WMS boxes, test details).
`ch19/` is the narrated pilot (normalization ladder): skill-shaped beats +
browser speech synthesis, no MP3s (Edge TTS synthesis endpoint unreachable
from this network; `content/adbms/ch19/narration.en.json` + `_source/tts_local.py`
are ready for a real-audio port). Player: `narrate.js`.

## Rebuild

```sh
python _source/build_site.py
```

Sources: `exam/notes/learning-path-from-zero.md`,
`exam/notes/classification-drills.md`, `exam/mock-exam-*.md`,
`exam/notes/final-cram.md`, `exam/notes/ultra-short-notes.md`,
`exam/revision-plan.md`, `_source/bossrush_mcqs.json`,
`_source/chatgpt_quizzes.json`. Original DOCXs are never touched.
Validate with `python _source/qa_site.py`.
