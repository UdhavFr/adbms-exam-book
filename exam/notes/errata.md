# errata.md — Source Validation Log

Source of truth: `ADBMS_MasterNotes.docx` (36 pp.) + corroborating `ADBMS_MemorizationSheet.docx`.
Validation method: every definition, rule, algorithm, ordered process, command and example in the notes
was re-read against the extracted source text (`_source/pages/*/text.md`) before being written into
`exam/notes/*`. Entries below are the only places where the source is ambiguous, internally inconsistent,
or where outside knowledge was needed.

**Overall finding: no hard factual error was found in the source.** The notebook is unusually careful
(it deliberately hedges where textbooks disagree). All entries below are AMBIGUITY / TERMINOLOGY /
CLARIFICATION issues — exactly the kind of thing that costs marks when a student "fixes" the professor.

---

## E1 — "Cardinality" means two different things in this same notebook

- **Source statement (U1 §4, p.5):** "Cardinality describes how many instances can participate" → 1:1, 1:N, M:N.
- **Source statement (U1 §6, p.6):** "Cardinality = number of tuples" (relational vocabulary list).
- **Suspected issue:** Same word, two standard meanings, used ~1 page apart. A student who writes
  "cardinality = number of rows" in an ER question (or "cardinality = M:N" in a relational-algebra question)
  looks wrong even though both come from the source.
- **Resolution to use in the exam:**
  - ER / relationships context → **cardinality ratio** = 1:1, 1:N, M:N (how entities participate).
  - Relation / table context → **cardinality of a relation** = number of tuples (rows).
  - Pair it with *degree* = number of attributes (columns), which is unambiguous.
- **Reason:** Both usages are standard in the literature; the source uses both correctly *in context*.
- **Confidence:** High.

## E2 — SQL clause order: processing order vs. syntax order

- **Source statement (U1 §7, p.7):** "Typical execution idea: FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT".
- **Suspected issue:** The source states this as *execution/logical* order (and explicitly hedges that the
  optimizer may transform it). Students may be marked down if they claim SQL is *written* in that order.
- **Clarified version:**
  - **Logical/processing order:** FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT/OFFSET.
  - **Written (syntax) order:** SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT.
  - Memorise the source's chain for "in what order are rows filtered/grouped/sorted"; use syntax order when writing SQL.
- **Reason:** Both orders are standard; the source's chain is the examinable one for "order of evaluation".
- **Confidence:** High.

## E3 — Repeatable Read and phantoms

- **Source statement (U3 §4, p.17):** "Repeatable Read | Provides stronger repeat-read guarantees; exact phantom behavior varies by DBMS."
- **Suspected issue:** The hedge is correct but a student may be asked "does RR prevent phantoms?" and need a crisp answer.
- **Clarified version:** In the **SQL standard**, Repeatable Read does **not** guarantee phantom protection —
  only **Serializable** does. Several real DBMSs (e.g. PostgreSQL, MySQL/InnoDB) *do* block phantoms at
  Repeatable Read, which is why the source says behaviour varies.
- **Label:** [EXTERNAL] — added to make the source's hedge answerable, not to replace it.
- **Reason:** Standard SQL:1999/SQL:2011 isolation hierarchy; the source's wording stays compatible with it.
- **Confidence:** High (external), and consistent with the source.

## E4 — Isolation-level anomaly table is intentionally *not* a strict matrix

- **Source statement (U3 §4, p.17):** the four levels are given as "general idea" rows, not as
  dirty-read / lost-update / phantom columns.
- **Suspected issue:** Students often reproduce the classic textbook anomaly matrix from memory and
  contradict the source's hedge.
- **Clarified version (safe to write):**

  | Level | Dirty read | Lost/non-repeatable read | Phantom |
  |---|---|---|---|
  | Read Uncommitted | possible | possible | possible |
  | Read Committed | prevented | possible | possible |
  | Repeatable Read | prevented | prevented | DBMS-dependent (standard: possible) |
  | Serializable | prevented | prevented | prevented |

- **Confidence:** High — this is a superset of the source table, not a contradiction.

## E5 — Structural inconsistency in the memorisation sheet's unit labels

- **Source statement:** `ADBMS_MemorizationSheet.docx` has two sections both titled "UNIT 1"
  ("UNIT 1 — WHAT THE DATABASE IS" and "UNIT 1 — EXAM RULES & SQL"), and one titled "UNIT 4/5".
- **Suspected issue:** Cosmetic only. Section numbering inside it restarts (…9, then 10, 11, 12 …).
- **Resolution:** The **Master Notes'** unit boundaries (5 units, 61 chapters) are authoritative and are
  what `exam/sections.json` / `exam/structure.md` encode. The memorisation sheet is treated as a
  *derived high-value index*, not as a structural source.
- **Confidence:** High.

## E6 — "Cardinality" answer trap in the relational-algebra table

- **Source statement (U1 §6, p.6–7):** relational algebra table lists σ, π, ∪, −, ×, ⋈.
- **Suspected issue:** None in the source; flagged because students commonly write σ = columns / π = rows.
- **Clarified version:** σ (selection) = **rows**; π (projection) = **columns**. Union/difference/product
  require **union compatibility** (same attribute names, same domains, same order) for ∪ and −.
- **Note:** "union compatibility" is standard terminology the source implies ("combines compatible relations")
  but does not spell out. [EXTERNAL] label applies to the phrase only.
- **Confidence:** High.

## E7 — No page numbers exist in the DOCX itself

- **Issue:** The source is a `.docx`, not a PDF, so it has no fixed PDF page objects and no bookmarks.
- **Resolution (not a source error):** page references throughout `exam/` use **Word's own pagination** of
  the unmodified file (36 pages), captured in `_source/heading_pages.json` by reading each heading's
  `Range.Information(wdActiveEndPageNumber)`. Section boundaries are in `exam/sections.json`.
  The original DOCX files were **not modified** (opened read-only; no PDF re-save was written over them).
- **Confidence:** High.

---

### What was checked and found *correct* (spot-check log)

| Claim | Where | Verdict |
|---|---|---|
| 3NF formal rule "X is super key OR A is prime" | U2 §5, p.11 | Correct |
| BCNF "every determinant is a super key" | U2 §6, p.11 | Correct |
| Lossless binary test: R1∩R2 → R1 or → R2 (example A→B or A→C) | U2 §9, p.12 | Correct |
| Attribute closure example F={A→B,B→C,C→D}, A⁺={A,B,C,D} | U2 §1, p.9 | Correct |
| 2NF example ENROLL with key (StudentID, CourseID) | U2 §4, p.10 | Correct |
| 3NF example EmpID→DeptID→DeptName (transitive) | U2 §5, p.11 | Correct |
| Minimal cover order: split RHS → remove extraneous LHS → remove redundant FDs | U2 §11, p.12 | Correct |
| Deferred update ⇒ no DB UNDO needed for uncommitted work | U3 §9, p.19 | Correct |
| WAL: log record to stable storage before data page | U3 §12, p.20 | Correct |
| 2PC: PREPARE → vote → COMMIT/ABORT; blocking risk | U4 §4, p.24 | Correct |
| CAP stated as partition-scenario trade-off (not "pick any 2") | U4 §7, p.25 | Correct |
| Cassandra `PRIMARY KEY ((course), year, student_id)` ⇒ partition key + clustering order | U5 §11, p.32 | Correct |
| B+ tree complexity O(log_f N), leaves linked for range scan | U2 §13, p.13 | Correct |
| MongoDB aggregate pipeline `$match → $group → $project → $sort → $limit` | U4 §12, p.23 | Correct |
