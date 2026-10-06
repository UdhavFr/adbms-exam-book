# answer-voices.md — Voice, Verbs & Time per Mark Level

*Doctrines stolen from two previous exam builds (EDT mid-sem, Blockchain end-sem)
and adapted to ADBMS. Rule zero from both: **wrong voice loses marks even with correct facts**.*

---

## 0. Timing doctrine (ASSUMED — no past paper found in this folder)

Assume the standard end-sem shape **100 marks / 3 h ≈ 1.8 min per mark** until told otherwise.
Mock exams in this folder deliberately run at compressed drill pace; the table below is for the real paper.

| Marks | Budget | Split (read → write → check) | Shape |
|---|---|---|---|
| 2 | 4 min | 1 → 2 → 1 | define + one example, 3–4 lines |
| 5 | 9 min | 2 → 6 → 1 | define + mechanism/diagram + example |
| 10 | 17 min | 3 → 12 → 2 | intro / core / analysis / conclusion (1+4+3+1+1) |
| 20 | 35 min | 5 → 27 → 3 | full spine (2+3+8+4+3, see §3) |

If the paper's totals differ, rescale linearly — the *ratios* are what matter.

---

## 1. Voice by mark level

- **2-mark (L1 recall):** define, list, name. One term, plain English, one example. **No justification, no diagram, no trade-offs** — they earn zero here and eat the 4-minute budget.
- **5-mark (L2 explain):** define + mechanism or labelled diagram + example. One contrast sentence if the question says "differentiate".
- **10-mark (L2/L3):** intro (notes' definition, quoted) → core (one bold sub-heading per scoring point, 2–3 lines each, notes' keywords) → analysis (cause-effect chain, table, or criteria verdict ending "Therefore…") → conclusion (2 lines reusing the question's keywords).
- **20-mark (L2–L4):** the full spine from `learning-path-from-zero.md` Lesson 12: Define (5–7 lines) → diagram → components under own headings → example → pros/cons/comparison → 3–4 line conclusion on correctness/speed/reliability.

---

## 2. Verb engines (obey the question's verb, not the topic's habit)

Multi-verb question → **one sub-heading per verb, echoing the question's words, in the order asked.**

- **Define / List:** term in source wording + one example. Stop.
- **Explain / Describe:** definition → mechanism/steps → example → why it matters (one line).
- **Differentiate / Compare:** **table first** (4+ parameters), then one verdict line for the scenario. Never two separate essays.
- **Apply / Work out (normalization, closure, schedules):** restate given data → numbered steps showing every intermediate result → boxed final answer → one-line benefit/meaning. Examiners award method marks per visible step.
- **Analyze:** break into components → relationships/cause-effect → verdict starting "Therefore…".
- **Evaluate / Justify:** criteria → strengths vs weaknesses → verdict **on the exact point asked**. Justify must argue the point, not survey the topic.
- **Write queries / commands / pipelines:** purpose (one line) → syntax → concrete example → what each clause does. `$match` first; WHERE before GROUP BY.

---

## 3. Mark chunking (suggested splits for task questions)

Show every intermediate step — method marks live there.

- **Applied normalization (FDs → keys → NF → BCNF):** data+closures **2** · key proof **2** · NF tests in ladder order **4** · decomposition + lossless/preservation check **2**. (= 10)
- **Normalization theory:** ladder definitions **3** · worked violation→fix **8** · lossless vs preservation table **4** · anomalies cured **3** · intro/conclusion **2**. (= 20)
- **CAP / ACID theory:** exact-statement intro **2** · each property/letter under own heading **8** · scenario application **4** · comparison (BASE / isolation levels) **3** · conclusion **3**. (= 20)
- **Recovery comparison:** failure types **2** · deferred vs immediate vs shadow table **8** · WAL + checkpoint chain **4** · which needs UNDO/REDO and why **4** · conclusion **2**. (= 20)

---

## 4. How marks are lost (each failed in previous exams)

1. No diagram where one exists (processes, hierarchies, algorithms — always draw).
2. No intro or no conclusion (the key expects both; 1 mark each).
3. Ignored verb (explained when asked to compare; listed when asked to evaluate).
4. Generic text without the notes' keywords (examiners grep for terms — see `final-cram.md` §7).
5. Writing the standard-textbook version where the notes differ (see `errata.md` E3/E4) — **answer with the notes' version only**; keep conflict flags (`CONFLICT: notes say X; standard texts say Y`) in your study margin, never in the answer.
6. Model answers are plain text: no LaTeX, no emoji, no `[tags]`; diagrams as labeled boxes; tables max 5×5; writable inside the §0 budget.
