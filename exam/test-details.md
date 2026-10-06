# test-details.md — Known Format, Assumed Slots, Choice Strategy

*Living file (EDT-prompt pattern): facts first, assumptions labeled **ASSUMED**, professor hints logged as they arrive.
No past paper was found in this folder — every slot below is an inference from the source's own
20-mark answer bank + "EXAM-READY POINT" markers, NOT a confirmed paper.*

---

## 1. Known facts

- Source: `ADBMS_MasterNotes.docx` (36 pp., 5 units, 61 chapters) + memorization sheet. Both unmodified.
- The source's own 20-mark answer bank covers: normalization ladder, recovery techniques, fragmentation/2PC, indexing, ACID (see `answer-bank.md` 20-mark skeletons).
- Priority evidence: P0 = 35 chapters, P1 = 24, P2 = 2 (see `master-study-guide.md`).
- Exam date/time: **fill in** — budgets below assume 100 marks / 3 h; rescale if different.

## 2. ASSUMED format (hypothesis, built from the answer bank)

| Slot | Likely content | Voice (`answer-voices.md`) | Floor? |
|---|---|---|---|
| Compulsory short answers (2-mark) | Definitions + one example from ALL units | L1 recall | **YES — bulletproof first** |
| 5-mark explains | SQL families, constraints, FD basics, isolation levels, BASE, sharding | L2 explain | **YES** |
| 10-mark mechanisms | 2PL, serializability test, B+ tree, 2PC, MongoDB pipeline, Cassandra model | intro/core/analysis/conclusion | one side each |
| 20-mark spines | Normalization ladder · ACID · CAP · Recovery chain · Cross-system indexing | full spine | one strong side each |

## 3. Choice-pair hypotheses + pick-sides strategy

Likely internal-choice pairings (same family, pick ONE side after covering both once):

1. **Normalization theory vs applied normalization** (FDs → keys → NF → BCNF steps).
2. **B+ tree indexing vs concurrency control** (problems + why needed).
3. **SQL families vs integrity constraints.**
4. **CAP/BASE vs fragmentation/2PC.**

Say `pick sides` in the tutor once both sides of a pair are covered: chosen side goes to Red depth
(`write-memorize-skip.md` boxes + timed writing), the other drops to Yellow (skim `likely-questions.md` MED once,
near the exam, in case the slot fills differently). **Never give an unchosen side or a Green topic Red-level depth.**

## 4. Study doctrine (floor first)

1. Q1-style recall (all units) + 5-mark explains = the floor. Bulletproof before any 20-mark depth.
2. Then one strong side per choice pair (§3).
3. Yellow topics exist as plausible substitutes, not because they need Red depth.
4. Missed block? Compress the middle (drop Green/Yellow depth); protect warm-up, gap-close, and one timed mock.

## 5. Time budgets (ASSUMED 100 marks / 3 h → 1.8 min/mark)

2-mark = 4 min · 5-mark = 9 min · 10-mark = 17 min · 20-mark = 35 min (read→write→check splits in `answer-voices.md` §0).

## 6. Professor-hint log (fill as hints arrive)

| Date | Hint | Affected topics | Action |
|---|---|---|---|
| | | | |

## 7. Gap list (format unknowns — content has no gaps vs the source)

- Exact mark split and choice pattern: unknown (slots in §2 are inferences).
- Recovery-in-Unit-3 style coverage: source HAS it (U3-9→12) — no action.
- If the professor names excluded topics, log them here and downgrade immediately.
