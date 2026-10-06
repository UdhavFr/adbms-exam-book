# weakness-tracker.md — Weakness Detection & Adaptive Testing System
The point of this file: **stop reviewing what you already know; attack what you keep getting wrong.**

---

## 1. How to log (takes 10 seconds per error)

After any flashcard, question-bank item, mock exam or tutor question, record failures only:

```
| Date/Time | ID (Q#/flashcard#/topic) | Unit-Chapter | Error type | Your wrong answer (1 line) | Correct answer (1 line) | Severity | Next test |
```

**Error types (pick one):**
- `DEF` forgotten/inaccurate definition
- `CONF` confused concepts (X vs Y)
- `ORDER` process/sequence mistake
- `CALC` closure/computation mistake
- `KEY` missing exam keyword (right idea, no mark-earning words)
- `DIAG` diagram missing/incorrect
- `CMD` command/syntax error (SQL/Mongo/CQL/Cypher)
- `TRAP` fell for a known distractor (CAP slogan, σ/π swap, etc.)

**Severity:** `1` = slipped · `2` = partially correct · `3` = completely wrong / didn't know.

---

## 2. The scoring rules (which topics get quizzed again)

**First-attempt rule (stolen from Papermorph's engine):** only your **first try** at a question counts toward
the diagnostic score. If you retry the same question and get it right, that proves *learning*, not *knowing* —
log the retry as a separate `RETEST` row with its own result, and never let it overwrite the first attempt.
The first-try number is the one that decides what you're weak on.

Per chapter keep a rolling score (first attempts only):

```
Chapter score = (correct first-tries) − (errors × severity)
```

- **Score ≤ 0 or any severity-3 error** → the chapter is **WEAK**: re-quiz **in 10 minutes**, then **in 30 minutes**, then at the end of the session (3 re-tests minimum).
- **Score 1–3** → **SHAKY**: re-quiz once later in the session (different question ID — never the same wording).
- **Score ≥ 4 with no severity-3 errors** → **STRONG**: do **not** re-quiz unless spaced repetition is due
  (re-test a STRONG topic only: once at the start of the next study block, and once before the exam).
- Any `TRAP` error → always re-test with a **differently worded** version of the same trap.

**Re-test rule:** each re-test must be a *different* question over the *same* concept (see `question-bank.md`
for alternates; if none exist, change the mark count — 2-mark recall → 5-mark explain → 10-mark apply).

---

## 3. Bias rules (what to spend time on)

1. **P0 topics get 60% of quiz time**, P1 30%, P2 10% — *unless* a P1 topic is repeatedly failing, in which
   case it temporarily outranks a P0 you already know.
2. Never quiz a STRONG topic twice in a row without a spaced gap.
3. Prefer **weak × high-priority** combinations: e.g. if CAP (P0) is a `TRAP` error, it becomes the very next
   question, then again in 10 minutes, then again in the final cram.
4. If two consecutive errors are the same **error type** (e.g. `KEY` twice), stop answering content and fix the
   *answer structure* instead (use `common-mistakes.md` §E).
5. If a **process** topic fails twice (`ORDER`), switch to drawing the flow diagram (`diagrams-and-mental-models.md`).

---

## 4. Master tracking table (copy rows as needed)

| ID | Topic | Unit-Chapter | Type | Sev | Tests | Status |
|---|---|---|---|---|---|---|
| W-001 | | | | | | |
| W-002 | | | | | | |
| W-003 | | | | | | |
| W-004 | | | | | | |
| W-005 | | | | | | |

**Status values:** `OPEN` → `RETEST#1 DUE` → `RETEST#2 DUE` → `HEALED` (two clean re-tests) / `PERSISTENT`
(fails 3 re-tests → downgrade to "read + write + teach aloud" mode).

---

## 5. Chapter strength board (update after each mock)

| Unit-Chapter | Topic | 1st score | Mock1 | Mock2 | Mock3 | Final status |
|---|---|---|---|---|---|---|
| U1-3 | Abstraction & independence | | | | | |
| U1-4 | ER modeling | | | | | |
| U1-5 | ER → relational | | | | | |
| U1-7 | SQL categories/order | | | | | |
| U1-8 | Integrity constraints | | | | | |
| U2-1 | FD & closure | | | | | |
| U2-3→8 | Normal forms 1→5 | | | | | |
| U2-9/10 | Lossless / preservation | | | | | |
| U2-13/14 | B+ tree / hash | | | | | |
| U3-3 | ACID | | | | | |
| U3-5 | Serializability | | | | | |
| U3-6 | Locks & 2PL | | | | | |
| U3-9→12 | Recovery techniques | | | | | |
| U4-2 | Fragmentation | | | | | |
| U4-4 | 2PC | | | | | |
| U4-7 | CAP | | | | | |
| U4-8/9 | BASE, sharding | | | | | |
| U4-11/12 | MongoDB CRUD/pipeline | | | | | |
| U5-1/11 | Cassandra model & ordering | | | | | |
| U5-6/7 | Embeddings & search | | | | | |
| U5-8/9/13 | Indexing systems | | | | | |

Legend for Final status: 🟢 strong · 🟡 shaky · 🔴 weak.

---

## 6. Automatic re-test queue (fill as you go)

**Due in 10 min:** __________________________________________
**Due in 30 min:** __________________________________________
**Due at session end:** _____________________________________
**Due before the exam (final-30 plan):** ______________________

---

## 7. How the tutor (me) uses this file

When you answer me interactively I will:
1. start with **P0** recall, mix understanding questions, and increase difficulty gradually;
2. **offer a hint on request** — say "hint" and I give the minimum keyword scaffold (like Papermorph's "Keys:"
   line) *before* you answer; a hint-assisted answer is logged as severity-2, a clean first try as 0-error;
3. never reveal the answer before you've tried — even a wrong attempt teaches more than a peek;
4. mark partial answers by naming **exactly what's missing** (keyword-level), teach only that, then return to testing;
5. after every 3 answered questions, give a **3-step wrap** (numbered recipe, Papermorph-style) of whatever
   we just covered, so the session leaves a compressed takeaway, not scattered facts;
6. skip anything you've answered correctly twice, unless a spaced re-test is due;
7. push failed items into the queue above with an error type and severity;
8. switch into timed exam simulation once the P0 board is mostly 🟢.
9. **teach in L1→L2→L3 gates** (Blockchain pattern): one layer per reply — L1 MAP (what + why in your words),
   L2 mechanism/diagram, L3 timed exam answer — ending each reply with that layer's gate question ONLY.
   I never show the next layer, a model answer, or a conflict box before you pass the gate. No L3 without the
   L1 gate; if you force it I flag "shallow: risk". Fail a gate → I pinpoint the divergence and re-explain
   differently; pass → I raise difficulty (scenario, extra verb, combined topic).
10. **confidence-first:** before I grade, you say **sure / unsure / guess**. Sure-but-wrong jumps to the front
    of the re-test queue; guess-and-right still gets one re-test (luck is not knowledge).

**Tutor modes (say the word):** `check me` (one retrieval Q) · `quiz me` (graded set, confidence asked, marks per line)
· `cram me` (Red topics, no gates) · `full [topic]` (slow L1→L3) · `ELI5 [topic]` (L1 only) · `exam-ready [topic]`
(straight to L3) · `pick sides` (commit a choice-pair side per `test-details.md` §3) · `connect me [topic]`
(cross-unit chain + one Section-J style question) · `memorize me [topic]` (assign the apt device
from `memorization-techniques.md`, then drill it retrieve-before-reveal) · `simulate` (timed mock) · `NORMAL [question]` (bypass protocol once).
