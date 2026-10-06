# ADBMS Exam Book — animated track

Scope: narrated animated lessons for the Tier-S exam topics of `ADBMS_MasterNotes.docx`
(36 pp., 5 units, 61 chapters). Static reading companion lives in the same folder
(`ch01.html`…`plan.html`); animated lessons are `ch19+` (new unit "Narrated lessons").
Pilot: ch19 (normalization ladder). Max 6 animated chapters before the exam.

Readers: CHRIST BCA student, exam tomorrow, zero-to-passing. Plain warm English,
exam form always in sight. Primary language: en.

## Conventions

- Stage 1600×900 SVG + controls (skill engine copy in `site/adbms/lib/`).
- Beats: intro → ideas with one quick check between → wrap (3 takeaways) → chapter
  practice (3 sets) → finish card. Beat ids match `narration.en.json`.
- Colours: COL.task (amber) = the rule/keyword; COL.quiz (blue) = examples/data;
  COL.good (green) = correct/pass; COL.bad (red) = violation/wrong; COL.nat/whole/
  int/rat hues reused as rung colours on the ladder (same colour, same rung).
- Tables are drawn as text rows + highlight rects (no table helper in the engine).
- Arrows: text "→" in T(); drawn connectors via path+draw only for the closure walk.
- Every question: right → `why`; wrong → hint at that mistake; then Show answer.
  Ids: `c-…` quick checks, `p-…` practice.
- Voice: en-US-AndrewMultilingualNeural, rate -4%. Narration writes math in words.

## Helper index

- (none yet — pilot uses engine primitives only: G, T, path, draw, show, hide,
  tw, panel, pop, pulse, quiz, choice, finishCard)

## Errata / feedback

- Pilot ch19 delivered 2026-10-06 without Playwright review (no Chromium/uv on this
  machine): delivery pass done statically — inline script `node --check` clean,
  all mark→step wirings resolved, all ask IDs exist in `quizzes.js`, all links resolve,
  text ≥34px, question cards below stage, `prefers-reduced-motion` honored.
  Needs human eyes on pacing/voices once (open `site/adbms/ch19/` and press Play).
