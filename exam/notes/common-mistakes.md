# common-mistakes.md — What Costs Marks

Grouped by type. Each item: **the trap → the fix**. Items marked ⚠ come straight from the source's own warnings.

---

## A. Definition traps (exact-wording marks)

1. **CAP** — ⚠ never write *"you can pick any two at all times."*
   **Fix:** "During a network partition, a system cannot guarantee both strong consistency **and** availability for every request under the formal CAP definitions."
2. **3NF vs BCNF** — writing "3NF: X must be a super key".
   **Fix:** 3NF = **X is a super key OR A is prime**; BCNF = **only** super key.
4. **BCNF slogan** — forgetting the phrase *"every determinant must be a super key."*
5. **Durability** — "data can never be lost". **Fix:** "committed effects survive subsequent system failure, *subject to the DBMS's durability guarantees*."
6. **Isolation** — "transactions don't see each other". **Fix:** "intermediate effects are controlled so execution is equivalent to an acceptable serial behaviour."
7. **Index** — "index makes everything faster". **Fix:** name the cost — storage + write/maintenance overhead.
8. **Embedding/vector search** — describing vectors as "meaning". **Fix:** the vector has no human-readable meaning; usefulness depends on the embedding model and application.
9. **BASE** — "BASE means data is permanently wrong". **Fix:** temporary inconsistency accepted; eventual convergence expected.
10. **NoSQL** — "schemaless". **Fix:** flexible-schema family; **Cassandra still has an explicit table schema** (ALTER TABLE, cluster-wide metadata).

---

## B. Concept confusion — "don't confuse X with Y"

| X | Y | Difference you must state |
|---|---|---|
| Schema | Instance | blueprint vs current contents |
| Physical independence | Logical independence | storage changes vs conceptual-schema changes |
| Degree | Cardinality | #attributes vs #tuples (⚠ *cardinality also = 1:1/1:N/M:N in ER* — errata E1) |
| Super key | Candidate key | any unique set vs **minimal** unique set |
| Primary key | Foreign key | identifies this row vs references another relation's key |
| Selection σ | Projection π | **rows** vs **columns** |
| Partial dependency | Transitive dependency | depends on *part of a composite key* vs depends on *another non-key attribute* |
| 3NF | BCNF | OR rule vs ONLY rule |
| 4NF | 5NF | independent **multivalued** facts vs **join** dependency |
| Lossless join | Dependency preservation | reconstruct exactly vs enforce without joins |
| B+ tree | Hash index | ordered, range-capable vs equality-only |
| Serial | Serializable | no interleaving vs interleaved but equivalent |
| Lost update | Dirty read | write overwritten vs uncommitted data read |
| Non-repeatable read | Phantom | same **row** changed vs different **row set** returned |
| Deadlock | Starvation | cycle of waiting vs endless postponement (source covers cycle + timeout) |
| Strict 2PL | Rigorous 2PL | hold **X** locks till commit vs hold **S and X** till completion |
| Deferred update | Immediate update | write only after commit vs may write before commit |
| UNDO | REDO | reverse uncommitted work vs re-apply committed work |
| 2PL (locking) | 2PC (commit) | concurrency control within a DBMS vs atomic commit across sites (comparisons C28) |
| Fragmentation | Replication | split into parts vs copies of parts |
| Horizontal | Vertical fragmentation | rows vs columns |
| Sharding | Replication | partitioning the dataset across nodes vs duplicating data across nodes |
| Partition tolerance | High availability | surviving network failure vs answering every request |
| Cassandra partition key | Clustering column | **where** data lives vs **order** within partition |
| Traditional index | Vector index | exact/range on scalar keys vs similarity/nearest-neighbour on vectors |
| Cosine | Euclidean | angle vs straight-line distance |
| HNSW | IVF | navigable graph vs clusters |
| MongoDB `$match` | `$project` | filter documents vs shape/compute fields |

---

## C. Process-order mistakes

1. **Normalization ladder out of order** (e.g. 3NF before 2NF). Fix: UNF → 1NF → 2NF → 3NF → BCNF → 4NF → 5NF, with the *reason* for each step.
2. **Minimal cover order** (removing redundant FDs first). Fix: **Split RHS → remove extraneous LHS → remove redundant FDs** (S-E-R).
3. **Attribute closure run only once.** Fix: loop until no new attribute appears.
4. **2PL described as "lock at start, unlock at end".** Fix: the rule is the *phase boundary* — no releases while still acquiring.
5. **Conflict graph edges drawn for read–read pairs.** Fix: conflict requires same item **and at least one write**.
6. **2PC described as "coordinator locks everything".** Fix: PREPARE → vote → COMMIT/ABORT.
7. **WAL reversed** ("data first, then log"). Fix: **log record reaches stable storage BEFORE the data page is written**.
8. **Recovery start point**: scanning the whole log. Fix: start from the **checkpoint**.
9. **SQL clause order**: claiming SQL is *written* FROM-first. Fix: FROM-first is **processing order** (errata E2).
10. **Aggregation pipeline out of order.** Fix: $match → $group → $project → $sort → $limit.
11. **ER→relational for 1:N**: putting the FK on the 1-side. Fix: FK goes on the **N**-side.
12. **Lossless test direction**: testing R1 → (R1∩R2) instead of **(R1∩R2) → R1 or → R2**.

---

## D. Diagram mistakes

1. Drawing boxes with **no labels** — label every node/arrow and add a one-line caption.
2. Three-level architecture without the **independence arrows**.
3. B+ tree drawn **without linked leaves** (loses the range-query point).
4. CAP drawn as a plain triangle with **no "during a partition" caption**.
5. Transaction state diagram missing **PARTIALLY COMMITTED**, or missing the ROLLBACK path.
6. 2PL diagram missing the **LOCK POINT**.
7. Recovery diagram missing **WAL** or **checkpoint**.

---

## E. Answer-structure mistakes (this is where 20-mark answers die)

1. Starting with background fluff instead of a **definition**.
2. One giant paragraph instead of **headings per component**.
3. No **diagram** on a topic that has an architecture/process/hierarchy.
4. No **example** (relation, transaction, query, scenario).
5. Listing **advantages only** — the source repeatedly asks for advantages **and** limitations.
6. Stopping after 2–3 pages of substance for a 20-mark question (the source explicitly warns against this).
7. No **conclusion** linking to correctness / performance / scalability / reliability.
8. For MongoDB/Cassandra/Redis/Neo4j: writing prose but **no commands**.
9. For indexing: quoting benefits but not **maintenance cost**.
10. For normalization: stating the NF without showing **FDs → key → violation → decomposition**.

---

## F. Calculation/technical slips

1. Calling a foreign key "prime" when it is not part of any candidate key of *this* relation.
2. Forgetting that a **candidate key must be minimal** (removing any attribute breaks uniqueness).
3. Assuming a decomposition is lossless because "it looks natural" — you must test the intersection rule.
4. Assuming dependency preservation comes free with losslessness (they are independent).
5. Using a **hash index** for `BETWEEN`/`ORDER BY` questions.
6. Suggesting an index for a write-heavy workload without mentioning write overhead.
7. Embedding a query with a different model than the stored vectors (similarity space must match) — practical point, [EXTERNAL].
8. Saying HBase is "Cassandra on Hadoop": HBase has a **strong Hadoop ecosystem relationship**; Cassandra is an **independent** wide-column system.

---

## G. Traps built into true/false and MCQ-style questions

| Statement | Verdict | Why |
|---|---|---|
| "A relation in 2NF may still have transitive dependencies" | **TRUE** | that's what 3NF removes |
| "BCNF is less restrictive than 3NF" | **FALSE** | BCNF is stricter |
| "Every 3NF relation is in BCNF" | **FALSE** | reverse: BCNF ⇒ 3NF |
| "A lossless decomposition is always dependency preserving" | **FALSE** | independent properties |
| "Serializable means transactions never interleave" | **FALSE** | that's *serial* |
| "Read Committed prevents dirty reads" | **TRUE** | |
| "Serializable prevents phantoms" | **TRUE** (standard) | RR's phantom behaviour is DBMS-dependent (E3/E4) |
| "Timestamp ordering can deadlock on locks" | **FALSE** | no lock waits ⇒ no lock deadlock |
| "Deferred update may need UNDO for uncommitted data changes" | **FALSE** | changes weren't written |
| "CAP says choose 2 of 3 always" | **FALSE** | only meaningful during a partition |
| "Cassandra tables must be modelled around entities like SQL" | **FALSE** | model around **query patterns**; duplication is normal |
| "Hash indexes support efficient range queries" | **FALSE** | unordered |
| "In a compound index, field order does not matter" | **FALSE** | order decides supported query/sort patterns |
| "2PC prevents all blocking" | **FALSE** | prepared participants can block |
| "Total participation means every entity must participate" | **TRUE** | |
