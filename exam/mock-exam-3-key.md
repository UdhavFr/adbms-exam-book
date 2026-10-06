# MOCK EXAM 3 — Answer Key

## Section A — True/False (2 marks each: 1 for verdict, 1 for the correction)

**A1. FALSE.** BCNF is *stricter* than 3NF: a BCNF relation has no non-super-key determinants, so it cannot contain a transitive dependency of a non-prime attribute (that requires a non-key determinant). *(The statement confuses 3NF — which may still allow some redundancy — with BCNF.)*

**A2. FALSE.** Serializable ≠ serial. A **serial** schedule runs transactions one after another; a **serializable** schedule may interleave operations but its effect is equivalent to *some* serial schedule.

**A3. FALSE.** In the SQL standard, Repeatable Read does **not** guarantee phantom protection — only **Serializable** does. Some DBMSs (e.g. PostgreSQL, MySQL/InnoDB) block phantoms at Repeatable Read, which is why the source hedges "exact phantom behaviour varies by DBMS" (errata E3).

**A4. FALSE.** CAP is specifically about behaviour **during a network partition**: under the formal definitions, strong consistency and availability cannot both be guaranteed for every request. "Choose any two at all times" is the classic wrong answer the source warns against.

**A5. TRUE.** Losslessness and dependency preservation are independent properties; good design seeks both when possible.

**A6. FALSE.** Under deferred update the changes were never written to the database before commit, so uncommitted transactions normally require **no database UNDO** (committed ones may need REDO).

**A7. FALSE.** WAL requires the **log record to reach stable storage before the data page** is written; otherwise recovery lacks the information to undo/redo.

**A8. FALSE.** Hash indexes are unordered and poorly suited to range conditions; use an ordered structure such as a B+ tree.

**A9. FALSE.** The **partition key** decides where the row is stored; clustering columns determine the **order of rows within a partition**.

**A10. FALSE.** Cosine similarity compares only the **angle/direction** between vectors; magnitude does not affect it (Euclidean distance and dot product do involve magnitude).

---

## Section B — Problems

### B1 (10)
**(a) (AB)⁺:** start {A,B} → AB→C ⇒ {A,B,C} → C→D ⇒ {A,B,C,D} → D→E ⇒ **{A,B,C,D,E}**.
**(b)** (AB)⁺ = all attributes ⇒ AB is a super key; removing either A or B breaks this (A⁺ = {A}, B⁺ = {B}) ⇒ **AB is the (minimal) candidate key**.
**(c)** Prime: **A, B**. Non-prime: **C, D, E**.
**(d) Highest normal form = 2NF.**
 - 1NF ✓ (atomic assumed).
 - 2NF ✓ — the only FD with a proper subset of the key on the left is none (A and B determine nothing), so there is no partial dependency.
 - 3NF ✗ — **C → D**: C is not a super key (C⁺ = {C,D,E}) and D is not prime ⇒ transitive dependency AB → C → D (same for D → E).
**(e)** Decomposition: **R1(AB, C)**, **R2(C, D)**, **R3(D, E)** — this satisfies BCNF (each determinant is a key of its relation) and is dependency preserving (each original FD lives in one part).
**Lossless verification:** R1 ∩ R2 = {C} and **C → D** determines R2 ⇒ lossless for that split; R2 ∩ R3 = {D} and **D → E** determines R3 ⇒ lossless. Joining all three reconstructs R exactly (no spurious tuples).

### B2 (10)
**(a) Conflicting pairs** (same item, ≥1 write, different transactions) in schedule order:
1. T1 R(X) … T2 W(X) → **T1 → T2**
2. T2 R(X) … T1 W(X) → **T2 → T1**
3. T2 W(X) … T1 W(X) → **T2 → T1**
4. T2 R(Y) … T1 W(Y) → **T2 → T1**
**(b) Graph:** nodes T1, T2 with edges **T1 → T2** and **T2 → T1**.
**(c)** The graph contains a **cycle** ⇒ **S is NOT conflict-serializable** (its result depends on the interleaving, not on either serial order).
**(d)** **Two-phase locking** (strict 2PL) or **timestamp ordering** would enforce a serializable outcome; the T2 R(X)/T1 W(X) interleaving would have been blocked by an X lock or a timestamp violation.

### B3 (10)
**(a)** Start from the beginning of the log (no checkpoint). **T1 committed ⇒ REDO** its update to A (100→50) if the change did not reach disk. **T2 has no COMMIT ⇒ UNDO** its update to B (200→180) if it was written.
**(b)** **Immediate update** — an uncommitted transaction's change may already be on disk, so UNDO is required. Under deferred update, T2's changes would never have reached the database and only REDO of T1 would be needed.
**(c)** WAL: the log record must be written to **stable storage before** the corresponding data page. Without it, a page could be flushed while the log still lacks old/new values — recovery could neither undo the uncommitted change nor redo the committed one (and could not know the page's pre-change state).
**(d)** A checkpoint records recovery information at intervals: recovery could **start at the checkpoint** instead of scanning the whole log, reducing recovery time, and (in typical implementations) dirty pages of already-committed transactions would already be flushed, shrinking the REDO set.

### B4 (10)
**(a)**
```sql
CREATE TABLE results (
  course text, year int, student_id int, name text,
  PRIMARY KEY ((course), year, student_id)
);
```
**(b)** **Partition key = `course`** — it answers WHERE the data lives, so `WHERE course='MCA'` targets exactly one partition (no cluster-wide scan). **Clustering columns = `year` (then `student_id`)** — they define the ORDER of rows inside the partition, so rows come back already ordered by `year`, satisfying `ORDER BY year` with no extra sort step.
**(c)** Rows within a `course` partition are physically ordered by `year` ascending, ties broken by `student_id`; reads are partition-local and cheap.
**(d)** A normalized relational design would split data (e.g. by course/year) and use **JOINs** and an index+sort at query time; Cassandra's design is **query-first with deliberate duplication** so the query is served from a single partition — schema changes must be planned because metadata is cluster-wide.

---

## Section C

**C1 (10)** — Mark for: embedding definition (numerical vector, similar objects near each other) · pipeline diagram `QUERY → EMBED → QUERY VECTOR → VECTOR INDEX → TOP-K → METADATA/DOCS → RESULTS` · the three measures (cosine = angle, Euclidean = straight-line, dot = alignment+magnitude) · brute force compares every stored vector, exact but expensive as N grows · ANN searches a smaller promising region for much lower latency with a small recall trade-off · **HNSW** = Hierarchical Navigable Small World, graph-based navigation through increasingly close candidates · **IVF** = inverted-file, partitions vectors into clusters and searches only relevant groups · note that query and stored vectors must come from the same embedding model (practical, [EXTERNAL]).

**C2 (10)** — Mark for:
- **(a) Relational B+ tree:** fewer page scans, O(log_f N), supports range/ORDER BY; costs = extra storage, index maintenance on inserts/updates/deletes, cache pressure.
- **(b) MongoDB compound index:** field order decides which query/sort patterns are served; `explain()` to verify; a mis-ordered index is ineffective; write overhead on indexed fields.
- **(c) Cassandra:** performance comes primarily from **partition/clustering design**, not from adding indexes — a secondary index is no substitute for a good partition key; wrong design ⇒ full/ scatter-gather scans.
- **(d) Vector index:** nearest-neighbour access (HNSW/IVF) replaces scanning all vectors; costs memory and build time, approximate results (recall trade-off), maintenance as vectors change.
- **Conclusion (the source's principle):** indexes must be **query-driven** — create useful indexes matching important query patterns, not the maximum number of indexes; too many indexes slow write-heavy systems.

---

## Section D (20 marks) — marking stages (1 mark each, capped at 20)
1. Transaction definition + bank example · 2. State diagram (Active → Partially committed → Committed; Failed → Aborted) ·
3. ACID, one line **+ bank example per property** · 4. Isolation levels with what each prevents ·
5. Four anomalies (lost update, dirty, non-repeatable, phantom) · 6. Serial vs serializable ·
7. Precedence-graph algorithm + cycle test · 8. S/X compatibility table ·
9. 2PL diagram with lock point · 10. Strict vs rigorous 2PL ·
11. Deadlock + PADT handling · 12. Timestamp ordering (Read_TS/Write_TS, abort, no lock deadlock, wasted work) ·
13. Failure types (transaction/crash/media/communication) · 14. Deferred update flow ·
15. Immediate update flow · 16. Shadow paging (shadow/current tables, root switch) ·
17. Log record contents + example · 18. WAL rule ·
19. Checkpoint purpose · 20. UNDO/REDO rule + conclusion on reliability.
**Diagram credit:** transaction states, 2PL, recovery chain (up to 3 extra marks, then cap at 20).
