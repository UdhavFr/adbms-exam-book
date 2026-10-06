# likely-questions.md — Prioritised Question Shortlist

**Honesty note:** these are *derived from the source's own answer bank, structure and emphasis* — **not** actual
predictions of tomorrow's paper. The source contains five explicitly-built 20-mark answer plans; those anchor
the HIGH tier. Everything else is weighted by how centrally the topic sits in the notebook and how often such
topics appear in ADBMS-style papers generally.

Each entry: **question · estimated marks · why it matters · model answer skeleton · keywords · related concepts.**

---

# 🔴 HIGH PRIORITY (study these first — the source literally builds answers for them)

### H1. Explain normalization and all normal forms. — **20 marks**
- **Why:** it is Question 1 of the source's Master 20-Mark Answer Bank, and Unit 2 is the densest chapter group.
- **Skeleton:** define normalization & redundancy harm → FDs + keys + closure → 1NF (atomic example) → 2NF (partial, ENROLL) → 3NF (transitive, EMPLOYEE) → BCNF (determinant rule) → MVD/4NF (hobbies) → JD/5NF → lossless join + dependency preservation → minimal cover → conclusion (benefits).
- **Keywords:** atomic values, fully dependent on the entire candidate key, super key/prime, determinant, multivalued, join dependency, lossless, dependency preserving.
- **Related:** attribute closure, anomalies, comparison C9/C10.

### H2. Explain transaction processing, concurrency control and recovery. — **20 marks**
- **Why:** Question 2 of the source's answer bank — the longest single answer plan (15 stages).
- **Skeleton:** transaction + bank example → states → ACID → SQL transactions/isolation levels → schedules + anomalies → serializability + precedence graph → S/X locks → 2PL + strict 2PL → deadlock → timestamps → failures → deferred/immediate/shadow → log/WAL/checkpoint → UNDO/REDO → reliability conclusion.
- **Keywords:** all-or-nothing, lock point, conflict-serializable, write-ahead logging, checkpoint, undo, redo.
- **Related:** diagrams D5, D6, D7.

### H3. Explain distributed databases and the CAP theorem. — **20 marks**
- **Why:** Question 3 of the answer bank; CAP is flagged in the source as the most mis-stated topic.
- **Skeleton:** define DDB → architecture diagram → characteristics/types → fragmentation (H/V/Hybrid) → replication + allocation → distributed transactions → 2PC diagram → consistency models → CAP definition + C/A/P → behaviour during a partition → ACID vs BASE → sharding → trade-offs conclusion.
- **Keywords:** logically integrated, physically distributed, prepare/vote/commit, during a network partition, eventually consistent, horizontal partitioning.
- **Related:** D8, D9, D10, D12.

### H4. Explain NoSQL systems and MongoDB. — **20 marks**
- **Why:** Question 4 of the answer bank; covers Units 4–5 command content examiners can ask for concretely.
- **Skeleton:** define NoSQL + motivation → four models → compare models → CAP + BASE → sharding → MongoDB document model → relational→MongoDB mapping → CRUD commands → operators → aggregation pipeline diagram → applications → when document DBs are useful.
- **Keywords:** JSON/BSON, collection/document/field/_id, $match/$group/$project/$sort/$limit, eventual consistency.
- **Related:** D10, P20.

### H5. Explain indexing in relational and NoSQL databases. — **20 marks**
- **Why:** Question 5 of the answer bank; the source explicitly warns to compare all five systems, not one.
- **Skeleton:** define index + why → storage pages/I/O → B+ tree structure + operations + range search → hash + collisions → B+ tree vs hash table → MongoDB compound ordering → CouchDB Mango/views → Cassandra partition/clustering order → Neo4j property indexes → vector embeddings + vector indexes → HNSW/ANN → benefits + maintenance costs → query-driven conclusion.
- **Keywords:** auxiliary access path, linked leaves, partition key, clustering columns, HNSW, IVF, maintenance overhead.
- **Related:** D4, C13, C14, C36.

### H6. Define and explain ACID properties with an example. — **5 or 10 marks**
- **Why:** the source calls ACID "one of the highest-value topics" with an explicit answer recipe (definition + bank example per property).
- **Skeleton:** one line + one bank example for Atomicity, Consistency, Isolation, Durability → why DBMSs need it.
- **Keywords:** all-or-nothing, integrity constraints, serial behaviour, survive failure.
- **Related:** transaction states, isolation levels.

### H7. What is an ER diagram? Map an ER diagram to a relational schema. — **10 or 20 marks**
- **Why:** Unit 1's core design competency; rules are listed as a numbered procedure (classic 10-mark material).
- **Skeleton:** ER definition → diagram with symbols → entities/attributes/keys/cardinality/participation → 7 mapping rules → worked STUDENT/COURSE/ENROLLS example → conclusion.
- **Keywords:** entity set, candidate key, M:N, foreign key, composite primary key, partial key.
- **Related:** D2, D14, P1.

### H8. Explain the three-level architecture and data independence. — **10 marks**
- **Why:** a stable, high-frequency short/long answer with a mandatory diagram; source devotes a full section + diagram.
- **Skeleton:** abstraction intro → diagram → external/conceptual/internal definitions → physical vs logical independence with examples → conclusion on maintainability.
- **Keywords:** user views, logical schema, access paths, storage structures, external views.
- **Related:** D1, comparisons C3.

### H9. What is conflict serializability? Test a schedule using a precedence graph. — **10 marks**
- **Why:** the only true *algorithm* in Unit 3 apart from closure; 10-mark problems are built from it.
- **Skeleton:** define conflict → serial vs serializable → 4-step algorithm → small worked schedule → conclusion (2PL/timestamps guarantee it).
- **Keywords:** same item, at least one write, edge Ti→Tj, acyclic.
- **Related:** D13, Q43.

### H10. Differentiate 3NF and BCNF (with an example). — **5 marks**
- **Why:** the "OR vs ONLY" contrast is the classic normalization discriminator and the source devotes a table to it.
- **Skeleton:** both definitions → restriction comparison → dependency preservation difference → note that BCNF ⇒ 3NF.
- **Keywords:** super key, prime attribute, determinant, dependency preservation.
- **Related:** C10, H1.

---

# 🟡 MEDIUM PRIORITY (very likely somewhere in the paper)

### M1. Explain deferred update, immediate update and shadow paging. — **10 marks**
- **Skeleton:** three sections with flows → crash behaviour table → which needs UNDO/REDO → trade-offs.
- **Keywords:** after commit, may be written before commit, stable shadow, root switch.

### M2. Explain log-based recovery, WAL and checkpoints. — **10 marks**
- **Skeleton:** log record fields + example → WAL statement → checkpoint purpose → UNDO/REDO rule → conclusion.
- **Keywords:** stable storage, old/new values, recent recovery point.

### M3. Explain two-phase commit with a diagram. — **10 marks**
- **Skeleton:** why distributed atomicity → prepare → vote → commit/abort → blocking limitation.
- **Keywords:** coordinator, participant, prepared state, blocking.

### M4. What is sharding? Compare sharding strategies. — **10 marks**
- **Skeleton:** definition + diagram → range/hash/directory/geographic with strength/weakness → good shard key criteria.
- **Keywords:** horizontal distribution, hotspots, hash of shard key, mapping service.

### M5. Compare ACID and BASE. — **5 marks**
- **Keywords:** transaction-oriented vs availability, soft state, eventual convergence.

### M6. Explain two-phase locking and how deadlocks are handled. — **10 marks**
- **Skeleton:** S/X compatibility table → 2PL diagram with lock point → strict/rigorous → deadlock example → PADT.
- **Keywords:** growing, shrinking, lock point, wait-for graph, timeout.

### M7. Explain functional dependency and attribute closure with an example. — **10 marks**
- **Skeleton:** FD definition + types → closure algorithm → worked example → use for candidate keys.
- **Keywords:** determinant, trivial, super key, loop until no growth.

### M8. Explain 1NF, 2NF, 3NF with examples. — **10 marks**
- **Skeleton:** three definitions + three relations + decompositions.
- **Keywords:** atomic, partial, transitive.

### M9. Explain horizontal and vertical fragmentation with an example. — **5 or 10 marks**
- **Keywords:** predicates, columns, primary key repeated, reconstruction.

### M10. Explain MongoDB aggregation pipeline with an example. — **10 marks**
- **Skeleton:** pipeline concept → stage order diagram → worked sales example → stage meanings.
- **Keywords:** $match, $group, $sum, $sort, pipeline stages.

### M11. Explain the Cassandra data model: partition keys and clustering columns. — **10 marks**
- **Skeleton:** wide-column concept → partition/clustering rules → `PRIMARY KEY ((course), year, student_id)` analysis → query-pattern design principle.
- **Keywords:** where data lives, order within partition, duplication to avoid joins.

### M12. Explain vector databases, embeddings and similarity search. — **10 marks**
- **Skeleton:** embedding definition + pipeline → similarity measures → similarity search flow → brute force vs ANN → HNSW/IVF.
- **Keywords:** numerical vector, top-k, cosine, ANN, navigable small world.

### M13. Explain B+ tree indexing and compare it with hash indexing. — **10 marks**
- **Skeleton:** structure → search steps → why efficient (linked leaves) → complexity → hash flow + collisions → comparison table.
- **Keywords:** separators, fan-out, range scan, bucket, collision.

### M14. Explain SQL command categories and clause processing order. — **5 or 10 marks**
- **Keywords:** DDL/DML/DCL/TCL, WHERE vs HAVING, FROM→…→LIMIT.

### M15. Explain integrity constraints with examples. — **5 marks**
- **Keywords:** domain, entity, referential, UNIQUE, CHECK, NOT NULL, CASCADE.

### M16. What are modification anomalies? How does normalization remove them? — **5 or 10 marks**
- **Keywords:** insertion, update, deletion, redundancy, decomposition.

---

# 🟢 LOWER PRIORITY (short answers / fillers — still worth 10 minutes each)

- **L1.** Schema vs instance (2–5) · **L2.** Data models list & classification (2–5) ·
- **L3.** Relational algebra operations (5) · **L4.** File organizations comparison (5) ·
- **L5.** Transaction states diagram (5) · **L6.** Isolation levels comparison (5) ·
- **L7.** Concurrency anomaly definitions — lost/dirty/non-repeatable/phantom (5) ·
- **L8.** Timestamp ordering advantages/disadvantages (5) · **L9.** Failure types (5) ·
- **L10.** Replication benefits vs costs (5) · **L11.** Homogeneous/heterogeneous/federated (2–5) ·
- **L12.** Consistency models — strong/eventual/causal/session (5) · **L13.** NoSQL four models (5) ·
- **L14.** MongoDB CRUD command families (5) · **L15.** Redis commands and use cases (2–5) ·
- **L16.** Graph data model + use cases (2–5) · **L17.** Cypher command patterns (5) ·
- **L18.** HBase vs Cassandra (5) · **L19.** CouchDB Mango vs views (5) ·
- **L20.** Traditional vs vector index (5) · **L21.** Index benefits vs costs (5) ·
- **L22.** DBMS functions list (2–5) · **L23.** Keys — super/candidate/primary/alternate/foreign (5) ·
- **L24.** Minimal cover steps (5) · **L25.** Lossless vs dependency preservation (5).

---

## How to answer by mark count (quick rule)

| Marks | Structure | Time |
|---|---|---|
| 2 | 1 definition sentence (+1 clarifier) | 2 min |
| 5 | definition → 3–5 points/table → one example/close | 6 min |
| 10 | definition → diagram → component headings → example → pro/con → conclusion | 12 min |
| 20 | DEFINE → DRAW → COMPONENTS → EXAMPLE → COMPARE/ADVANTAGES → CONCLUDE (full answer plan) | 25–30 min |
