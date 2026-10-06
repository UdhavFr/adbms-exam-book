# MOCK EXAM 2 — Application & Comparison (difficulty 2/3)
**Time:** 100 minutes · **Total:** 110 marks · Closed book. Write everything before checking `mock-exam-2-key.md`.

---

## Section A — Short answer (5 × 4 = 20)

**A1. (4)** Explain *entity integrity* and *referential integrity*, and give one SQL statement that enforces each.
**A2. (4)** A relation has attributes (StudentID, CourseID, StudentName, Grade) with key (StudentID, CourseID). Which normal form is violated and why? Show the decomposition.
**A3. (4)** List the four failure types a recovery manager must handle, with one cause each.
**A4. (4)** What is the difference between a *replica* and a *fragment*?
**A5. (4)** Give the MongoDB command families for CRUD and one example of a query using `$gt`.

## Section B — 5-mark questions (8 × 5 = 40)

**B1.** List the ER → relational mapping rules for: composite attribute, multivalued attribute, 1:1, 1:N, M:N and weak entity.
**B2.** Explain the three levels of the normalization ladder (1NF, 2NF, 3NF) using the *same* example relation if possible.
**B3.** Explain what a precedence graph is and state the condition for conflict serializability.
**B4.** Explain two-phase locking including the lock point, and distinguish strict from rigorous 2PL.
**B5.** Compare replication benefits with replication costs, and state what allocation means.
**B6.** Compare ACID and BASE.
**B7.** Explain the four sharding strategies with one strength each.
**B8.** Compare the four NoSQL data models on representation and typical application.

## Section C — 10-mark questions (3 × 10 = 30)

**C1.** Given R(A, B, C, D) with functional dependencies F = {A → B, B → C, C → D}: compute A⁺, identify whether A is a key, find a candidate key if A is not, and state which normal form the relation violates (assume all attributes are in R and A is the only determinant candidate besides combinations you test).
**C2.** Explain the log-based recovery mechanism: log record contents, the write-ahead logging rule, checkpoints, and what recovery does after a crash when T1 committed and T2 did not. Include a diagram.
**C3.** Explain the MongoDB aggregation pipeline with a worked example that computes total sales per product for paid orders, sorted descending. Then state two situations where an index would (and would not) help.

## Section D — 20-mark question (1 × 20 = 20)

**D1.** Explain distributed database fragmentation, replication, two-phase commit, CAP and sharding, and relate CAP to the ACID/BASE trade-off. Include diagrams where appropriate.

---
## Optional bonus (not counted): 
Write a 10-mark answer: "Explain vector embeddings, similarity measures and approximate nearest-neighbour search."
