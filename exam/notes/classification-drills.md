# classification-drills.md — Sorter & Multi-Select Drills (Papermorph format)

*Stolen from Papermorph's chapter-practice design: their strongest question types are (a) **sorters** —
assign each item to a category — and (b) **multi-select grids** — "choose every statement that is true".
Both beat plain MCQ because there's no guessing from options: you must hold the whole category map in your head.
All items verified against `ADBMS_MasterNotes.docx`. Answers + why at the bottom of each drill — **cover them first**.*

Scoring (first attempts only, per `weakness-tracker.md`): each item = 1 point. **≤60% on any drill → that
category map is WEAK** → re-read the named section, then redo the drill tomorrow morning.

---

## Drill 1 · NORMALIZATION SORTER (Unit 2 — the money drill)

**Sort each situation into its bucket:** `1NF-violation` · `partial-dependency (2NF)` · `transitive-dependency (3NF)` · `BCNF-violation` · `already-fine`

| # | Situation | Your bucket |
|---|---|---|
| 1 | Cell contains "Cheese, Olives" in one field | |
| 2 | Key is AB; FD B→C exists | |
| 3 | Key is ID; FDs ID→Dept and Dept→DeptHead | |
| 4 | Key is AB; FD AB→C exists, nothing else | |
| 5 | FD D→B where D is not a super key and B is not prime | |
| 6 | Repeating group of phone numbers stored as Phone1, Phone2, Phone3 columns | |
| 7 | Key AB; FDs AB→C and A→D (A not a super key) | |
| 8 | Single-column key, no FDs except key→attributes | |

**Answers:** 1→1NF · 2→partial (B is part of composite key AB) · 3→transitive · 4→fine (AB is super key) ·
5→BCNF-violation (determinant D not a super key) · 6→1NF (repeating groups) · 7→partial (A part of AB) ·
8→fine. **Why:** bucket by *which rule breaks*: atomicity (1NF) → whole-key dependence (2NF) →
non-key→non-key (3NF) → determinant-not-superkey (BCNF).

---

## Drill 2 · NORMAL FORMS MULTI-SELECT (Unit 2)

**Choose EVERY statement that is true** (each is T/F — state why for each):

1. Every BCNF relation is in 3NF.
2. 3NF requires that every determinant is a super key.
3. 2NF only matters when the key is composite.
4. A decomposition can be lossless but not dependency-preserving.
5. BCNF decomposition always preserves all FDs.
6. 4NF deals with multivalued dependencies.
7. The test for 3NF is: X→A holds only if X is a super key or A is prime.
8. Minimal cover = split RHS, remove extraneous LHS, remove redundant FDs.

**Answers:** 1 T · 2 F (that's BCNF; 3NF allows prime A) · 3 T (single-attribute keys have no partial deps) ·
4 T · 5 F (BCNF may lose FDs; 3NF synthesis preserves) · 6 T · 7 T · 8 T.

---

## Drill 3 · RECOVERY SORTER (Unit 3)

**Match each scheme to what recovery needs after a crash:** `REDO-only` · `UNDO+REDO` · `neither (switch root)` · `log-first rule`

| # | Scheme / rule | Your bucket |
|---|---|---|
| 1 | Deferred update | |
| 2 | Immediate update | |
| 3 | Shadow paging | |
| 4 | Write-Ahead Logging | |
| 5 | Checkpoint | |

**Answers:** 1→REDO-only · 2→UNDO+REDO · 3→neither · 4→log-first rule · 5→neither itself — it *bounds*
where UNDO/REDO starts. **Why:** deferred = uncommitted never touched disk → nothing to undo; immediate =
uncommitted IS on disk → must undo; shadow = old pages intact → flip the root pointer; WAL = log record
reaches stable storage *before* the data page.

---

## Drill 4 · CONCURRENCY MULTI-SELECT (Unit 3)

**Choose EVERY true statement:**

1. A cycle in the precedence graph means the schedule IS conflict serializable.
2. In 2PL, once shrinking begins, no new locks may be acquired.
3. 2PL guarantees serializability but may deadlock.
4. Deadlock is detected with a wait-for graph.
5. Phantom reads disappear under Read Committed.
6. Serializable isolation prevents all four anomaly types.
7. X-locks conflict with S-locks and X-locks.
8. 2PC is a locking protocol.

**Answers:** 1 F (cycle = NOT serializable) · 2 T · 3 T · 4 T · 5 F (phantoms survive until Serializable;
Repeatable Read still allows them in SQL-standard terms — source hedges) · 6 T · 7 T ·
8 F (2PC = distributed agreement protocol; 2PL = locking discipline — the classic mix-up).

---

## Drill 5 · ACID SORTER (Unit 3)

**Each bank-transfer symptom → the ACID property at stake:**

| # | Symptom | Property |
|---|---|---|
| 1 | Debit applied, credit lost in a crash — money vanished | |
| 2 | Committed transfer gone after power cut | |
| 3 | Two transfers read the same balance and both withdrew | |
| 4 | Transfer left the account at a negative value violating the rule | |

**Answers:** 1→Atomicity · 2→Durability · 3→Isolation · 4→Consistency.

---

## Drill 6 · DISTRIBUTED SORTER (Unit 4)

**Bucket each fact:** `horizontal-fragment` · `vertical-fragment` · `2PC-phase` · `CAP-choice` · `sharding-strategy`

| # | Fact | Bucket |
|---|---|---|
| 1 | Split EMPLOYEES into rows by department | |
| 2 | Split EMPLOYEES into (ID,Name) and (ID,Salary) | |
| 3 | Rebuild fragment with JOIN on the key | |
| 4 | Coordinator sends "can you commit?" and waits for votes | |
| 5 | Any participant votes NO | |
| 6 | System keeps answering with stale data during a partition | |
| 7 | Range sharding for time-series logs | |
| 8 | Hash sharding for even key distribution | |

**Answers:** 1→horizontal (σ) · 2→vertical (π, key kept) · 3→vertical-rebuild · 4→2PC prepare phase ·
5→global abort · 6→AP choice · 7→range · 8→hash. **Why:** rows=σ=horizontal, columns=π=vertical;
prepare→vote→decision is the whole 2PC shape; CAP's trade-off only exists *during* a partition.

---

## Drill 7 · STORE MATCHER (Unit 5)

**Match each requirement to the best store:** `MongoDB` · `Cassandra` · `Redis` · `Neo4j` · `Vector store`

| # | Requirement | Store |
|---|---|---|
| 1 | Session tokens with 30-minute expiry | |
| 2 | Friend-of-friend traversal | |
| 3 | "Similar products" by embedding cosine angle | |
| 4 | Time-series write-heavy, query by partition+clustering key | |
| 5 | Flexible JSON product catalog with ad-hoc field queries | |

**Answers:** 1→Redis (TTL) · 2→Neo4j (graph) · 3→Vector store (cosine) · 4→Cassandra (partition=where,
clustering=order) · 5→MongoDB (documents).

---

## Drill 8 · INDEX MULTI-SELECT (Unit 5)

**Choose EVERY true statement:**

1. B+ tree suits range queries because leaves are linked and sorted.
2. Hash indexes make equality lookups O(1) but ranges slow.
3. HNSW is a graph-based approximate nearest-neighbour technique.
4. IVF clusters vectors then searches within clusters.
5. Cassandra clustering columns decide storage order inside a partition.
6. Indexes speed reads and slow writes.
7. Every NoSQL system uses the same indexing mechanism.
8. Aggregation pipelines should `$match` first to cut data early.

**Answers:** 1 T · 2 T · 3 T · 4 T · 5 T · 6 T · 7 F (the source explicitly warns against this) · 8 T.

---

## Drill 9 · ER MAPPING SORTER (Unit 1)

**Bucket each mapping rule:** `1:N` · `M:N` · `multivalued attribute` · `composite attribute` · `weak entity`

| # | Rule | Bucket |
|---|---|---|
| 1 | New junction table holding both keys | |
| 2 | 1-side's PK becomes FK in the N-side relation | |
| 3 | Separate relation: owner PK + the values | |
| 4 | Flatten into single columns (Street, City, Pin) | |
| 5 | Owner PK + discriminator, total participation noted | |

**Answers:** 1→M:N · 2→1:N · 3→multivalued · 4→composite · 5→weak entity.

---

## Drill 10 · SQL & ARCHITECTURE MULTI-SELECT (Unit 1)

**Choose EVERY true statement:**

1. External level hides physical storage from end users.
2. Physical data independence means the conceptual schema changes when storage changes.
3. GRANT/REVOKE are DCL.
4. Entity integrity = primary key NOT NULL and unique.
5. Schema is the blueprint; instance is the current data values.
6. WHERE filters groups after GROUP BY.
7. HAVING filters groups after GROUP BY.
8. A DBMS cures redundancy by centralizing design.

**Answers:** 1 T · 2 F (conceptual stays fixed — that's the point) · 3 T · 4 T · 5 T ·
6 F (WHERE filters rows *before* grouping) · 7 T · 8 T.

---

## Score log

| Drill | Date | First-try % | Re-try % | Verdict |
|---|---|---|---|---|
| 1 Normalization sorter | | | | |
| 2 NF multi-select | | | | |
| 3 Recovery sorter | | | | |
| 4 Concurrency multi-select | | | | |
| 5 ACID sorter | | | | |
| 6 Distributed sorter | | | | |
| 7 Store matcher | | | | |
| 8 Index multi-select | | | | |
| 9 ER mapping sorter | | | | |
| 10 SQL/arch multi-select | | | | |
