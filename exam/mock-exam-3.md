# MOCK EXAM 3 — Hard / Trap-Heavy (difficulty 3/3)
**Time:** 90 minutes · **Total:** 100 marks · Closed book, exam conditions (no notes, no peeks, one attempt).
This paper deliberately contains **distractor wording**, cross-unit confusion and multi-step problems.
Answers: `mock-exam-3-key.md`.

---

## Section A — True or false? Correct the false statements (10 × 2 = 20)

**A1.** "A relation that is in BCNF may still contain transitive dependencies of non-prime attributes."
**A2.** "Serializable means transactions are executed one after another."
**A3.** "In the SQL standard, Repeatable Read guarantees that phantoms cannot occur."
**A4.** "CAP tells a designer that any distributed system can choose exactly two of consistency, availability and partition tolerance at all times."
**A5.** "A decomposition can be lossless but not dependency preserving."
**A6.** "Deferred update requires UNDO of uncommitted data pages after a crash."
**A7.** "The write-ahead logging rule requires data pages to be flushed before their log records."
**A8.** "A hash index is a good choice for a BETWEEN query."
**A9.** "In Cassandra, the clustering columns determine which node stores the row."
**A10.** "Cosine similarity is affected by the magnitude of the vectors."

## Section B — Problems (4 × 10 = 40)

**B1. (10)** R(A, B, C, D, E) with F = {AB → C, C → D, D → E}.
 (a) Compute (AB)⁺. (b) Identify the candidate key. (c) Classify prime/non-prime attributes.
 (d) State the highest normal form achieved and justify. (e) Give a decomposition to the highest normal form and verify the lossless-join condition for one split.

**B2. (10)** Schedule S: T1: R(X), W(X) … T2: R(X), W(X), R(Y) … T1: W(Y), COMMIT … T2: COMMIT (operations interleaved as: T1 R(X); T2 R(X); T1 W(X); T2 W(X); T2 R(Y); T1 W(Y); T1 COMMIT; T2 COMMIT).
 (a) List all conflicting pairs. (b) Draw the precedence graph. (c) State whether S is conflict-serializable and why. (d) Name a protocol that would have produced a correct schedule.

**B3. (10)** A system crashes mid-transaction. Given the log: `<START T1> <T1, A, 100, 50> <START T2> <T2, B, 200, 180> <COMMIT T1>` with **no checkpoint recorded**:
 (a) What does recovery do with T1 and T2, and why? (b) Which update technique is this consistent with — deferred or immediate update? Justify. (c) State the WAL rule and explain what would be impossible without it. (d) Explain how a checkpoint would have changed this recovery.

**B4. (10)** Design task: you must support the query `SELECT * FROM results WHERE course='MCA' ORDER BY year` in Cassandra.
 (a) Give a `CREATE TABLE` with a suitable primary key. (b) Identify the partition key and clustering columns and justify each. (c) Explain what happens to rows within the partition. (d) State how this differs from a normalized relational design.

## Section C — 10-mark conceptual (2 × 10 = 20)

**C1.** Explain the vector similarity-search pipeline end to end, compare brute force with ANN, and contrast HNSW with IVF. Include a diagram and name the three similarity measures.
**C2.** "Indexes improve reads but introduce costs." Explain this statement for (a) a relational B+ tree index, (b) a MongoDB compound index, (c) a Cassandra table design, and (d) a vector index. Conclude with the design principle the source recommends.

## Section D — 20-mark question (1 × 20 = 20)

**D1.** Explain transaction processing, concurrency control and recovery, covering: transaction states, ACID, isolation levels, concurrency anomalies, serializability and the precedence graph, locks and 2PL, deadlocks, timestamp ordering, failure types, deferred/immediate update, shadow paging, logging, WAL, checkpoints and UNDO/REDO. Include labelled diagrams.

---
*After marking: record every miss in `weakness-tracker.md` and re-attempt only the missed items after 30 minutes.*
