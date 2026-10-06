# revision-plan.md — Time-Boxed Study Plans
Every plan states **what** to open and **in what order**. High-yield first, always.
File paths are relative to `exam/`.

## Session rules (apply to every plan below)

- **Warm-up first (10 min, never skipped):** 3 questions from yesterday's Red topics + 2 older ones
  (tutor: say `quiz me` over the ✗ pile; solo: `question-bank.md` Section H/I misses). Missed items return
  later the same session after 3 other items. Correct in 2 separate sessions = SOLID.
- **Missed block? Compress the middle, protect the edges:** drop Green/Yellow depth first; never skip
  warm-up, gap-close (`weakness-tracker.md` queue), or one timed mock.
- **Floor first** (`test-details.md` §4): 2-mark recall + 5-mark explains across all units before any 20-mark depth.
- Say **sure / unsure / guess** before checking any answer (tutor asks automatically).

---

## 🚨 30-MINUTE EMERGENCY PLAN (nothing studied yet)

| Min | Action | File |
|---|---|---|
| 0–8 | Read the whole cram sheet **twice** — definitions, rules, chains, traps | `notes/final-cram.md` |
| 8–13 | The five 20-mark spines: read section 8 and say each spine aloud from memory | `notes/final-cram.md` §8 |
| 13–18 | The 11 diagrams: cover and redraw (three-level, ER, ladder, B+ tree, states, 2PL, recovery, distributed, CAP, sharding, vector) | `notes/diagrams-and-mental-models.md` |
| 18–23 | Comparisons tables: ACID/BASE, 3NF/BCNF, B+/hash, deferred/immediate, horizontal/vertical, traditional/vector index | `notes/comparisons.md` C9, C10, C13, C23, C26, C36 |
| 23–27 | Trap list (18 items) — read aloud; they are free marks | `notes/final-cram.md` §5 |
| 27–30 | Answer checklist + the 6 answer moves | `notes/final-cram.md` §0, §9 |

**If 30 minutes is really all you have:** `notes/final-cram.md` §1 (definitions), §2 (rules), §5 (traps), §8 (spines).

---

## ⏱ 1-HOUR PLAN

| Min | Action |
|---|---|
| 0–10 | `notes/final-cram.md` end-to-end (definitions → rules → chains → traps → hooks) |
| 10–25 | **P0 spines** in order: ACID + 2PL + recovery (`chapter-notes/unit-3.md`), normalization (`unit-2.md`) |
| 25–35 | CAP + 2PC + fragmentation + sharding (`unit-4.md`), indexing/Cassandra/vector (`unit-5.md`) |
| 35–45 | `notes/ultra-short-notes.md` — read every line; flag anything unfamiliar |
| 45–52 | `notes/answer-bank.md`: memorise the **2-mark list** and skim the 5-mark answers |
| 52–60 | Draw all 11 diagrams from memory; re-check only the ones you missed |

## ⏱ 2-HOUR PLAN

| Min | Action |
|---|---|
| 0–20 | `chapter-notes/unit-1.md` + `unit-2.md` (P0 chapters only) with `notes/definitions.md` open for exact wording |
| 20–45 | `chapter-notes/unit-3.md` (every P0) + `notes/processes-and-algorithms.md` P8–P16 |
| 45–65 | `chapter-notes/unit-4.md` + `unit-5.md` (P0 chapters) |
| 65–75 | `notes/comparisons.md` — all 🔴 tables (C9, C10, C13, C16, C17, C23, C30, C31, C35, C36) |
| 75–90 | `notes/question-bank.md` — answer the P0 questions aloud (Q19–Q33, Q40–Q54, Q60–Q69, Q73–Q80); mark ✗ |
| 90–100 | Speed drill: `question-bank.md` Section H+I MCQs (Q89–Q142) — 30 s each, no working; log every ✗ in `weakness-tracker.md`, re-read only those topics |
| 100–112 | `notes/flashcards.md` decks A–E (speed round: skip ✓ cards) |
| 112–120 | `notes/final-cram.md` §5 traps + §6 hooks + diagram redraw |

## ⏱ 4-HOUR PLAN (real preparation)

| Min | Block |
|---|---|
| 0–40 | **Unit 1**: read `chapter-notes/unit-1.md` fully; test with flashcards Deck A; write one ER diagram + one mapping answer from memory |
| 40–95 | **Unit 2**: `chapter-notes/unit-2.md` + `notes/processes-and-algorithms.md` P2–P7; solve a normalization problem from `question-bank.md` Q21/Q25/Q26/Q87 on paper |
| 95–150 | **Unit 3**: `chapter-notes/unit-3.md` + P8–P16; draw state/2PL/recovery diagrams; answer Q40–Q54 |
| 150–195 | **Unit 4**: `chapter-notes/unit-4.md`; write the CAP answer verbatim twice; 2PC diagram; Mongo commands from `examples.md` E-28/E-29 |
| 195–235 | **Unit 5**: `chapter-notes/unit-5.md`; Cassandra partition/clustering example; index comparison table |
| 235–260 | **Cross-unit**: `notes/comparisons.md` (all tables) + `notes/common-mistakes.md` sections A–C |
| 260–285 | **Mock 1, timed, closed book** → `mock-exam-1.md` |
| 285–300 | **Mark** with `mock-exam-1-key.md`; log every miss in `weakness-tracker.md` |
| 300–330 | **Fix phase**: re-study only the missed topics (`chapter-notes`, `definitions.md`), then re-answer the same questions |
| 330–345 | `notes/likely-questions.md` HIGH tier — say each skeleton aloud |
| 345–360 | `notes/final-cram.md` + diagram redraw |

*(If you have 4 hours and Mock 1 is already done, swap 260–345 for `mock-exam-2.md` + marking + fix.)*

---

## 🕒 FINAL 30 MINUTES BEFORE THE EXAM

| Order | Content | File |
|---|---|---|
| 1 (6 min) | Five 20-mark spines said aloud, in order | `notes/final-cram.md` §8 |
| 2 (5 min) | All exact definitions table (read twice) | `notes/final-cram.md` §1 |
| 3 (4 min) | Formulas/rules (closure, NF criteria, lossless, WAL, 2PC, CAP, partition/clustering) | `notes/final-cram.md` §2 |
| 4 (5 min) | Comparisons table (the one-page version) | `notes/final-cram.md` §4 |
| 5 (4 min) | Process chains 1–12 | `notes/final-cram.md` §3 |
| 6 (4 min) | Memory hooks blast | `notes/final-cram.md` §6 |
| 7 (2 min) | Traps + keywords + pre-answer checklist | `notes/final-cram.md` §5, §7, §9 |

## 🕙 FINAL 10 MINUTES BEFORE THE EXAM

1. **(3 min)** Say the four subject chains: DESIGN · RELIABILITY · DISTRIBUTION · NoSQL.
2. **(2 min)** Normalization one-liner: *1=Atomic, 2=Partial, 3=Transitive, BC=Determinant, 4=MVD, 5=Join* + "3NF = OR, BCNF = ONLY".
3. **(1 min)** ACID one line each with the bank story.
4. **(1 min)** 2PL: *growing → lock point → shrinking*; locks: *S shares, X excludes*; recovery: *committed=REDO, uncommitted=UNDO; LOG BEFORE DATA*.
5. **(1 min)** CAP exact sentence (partition wording!) + 2PC *ask → vote → decide*.
6. **(1 min)** Cassandra *partition = place, clustering = order* · vector *query → embedding → index → top-k · HNSW=graph, IVF=clusters*.
7. **(1 min)** Remind yourself of the 4 structural rules: definition first · diagram · headings · example · conclusion; and never write the CAP slogan.

---

## Recommended sequence for the remaining time (assuming you start now)
1. `notes/final-cram.md` (twice) — 15 min
2. P0 chapter-notes units 3 → 2 → 4 → 5 → 1 — 90 min
3. `mock-exam-1.md` timed + mark + fix — 60 min
4. `weakness-tracker.md` re-test loop — 30 min
5. `notes/likely-questions.md` HIGH skeletons aloud — 20 min
6. `mock-exam-2.md` if time remains — 90 min
7. Final-30 plan, then final-10 plan, then sleep.
