# answer-bank.md — Model Answers at 2 / 5 / 10 / 20 Marks

**Depth guide (from the source):**
- **2 marks** = definition (+1 clarifying line). Do not write a paragraph.
- **5 marks** = definition → 3–5 structured points or a small table → one-line example/close.
- **10 marks** = definition → labelled diagram/flow → component headings → example → advantage/limitation → conclusion.
- **20 marks** = DEFINE → DRAW → EXPLAIN COMPONENTS → EXAMPLE → COMPARE/ADVANTAGES/LIMITATIONS → CONCLUDE (see `processes-and-algorithms.md` P23).

---

# 2-MARK ANSWERS (write these verbatim)

1. **DBMS** — Software that provides facilities for defining, storing, retrieving, updating, securing and recovering data in a database.
2. **Schema** — The overall logical description/blueprint of the database (structure, not contents).
3. **Instance** — The collection of actual data stored at a particular point in time.
4. **Foreign key** — Attribute(s) in one relation referencing a key in another relation, enforcing referential integrity.
5. **Entity integrity** — A primary key can never be NULL and must uniquely identify each tuple.
6. **Functional dependency** — X → Y means the value of X uniquely determines the value of Y.
7. **1NF** — Attributes contain atomic values; no repeating groups.
8. **3NF** — For every non-trivial X → A, X is a super key **or** A is a prime attribute.
9. **Lossless join** — Joining the decomposed relations reconstructs exactly the original relation, with no spurious tuples.
10. **Transaction** — A logical unit of database work that must preserve correctness under concurrency and failure.
11. **ACID** — Atomicity, Consistency, Isolation, Durability — the four guarantees every committed transaction must satisfy.
12. **Serializability** — A schedule whose effect is equivalent to some serial execution of its transactions.
13. **2PL** — A protocol with a growing phase (acquire locks, no releases) and a shrinking phase (release locks, no new acquisitions).
14. **WAL** — The log record must reach stable storage before the corresponding data page is written.
15. **Deadlock** — A cycle of transactions each waiting for a resource held by the next.
16. **Sharding** — Horizontal distribution of records across multiple nodes, each shard holding a subset of the dataset.
17. **CAP** — During a network partition, a distributed system cannot guarantee both strong consistency and availability for every request under the formal CAP definitions.
18. **NoSQL** — A broad family of non-relational database technologies designed for flexible data models and scalable/distributed workloads.
19. **Embedding** — A numerical vector representation of an object produced by an embedding model.
20. **Index** — An auxiliary access structure that improves lookup performance at the cost of storage and maintenance.
21. **Partition key (Cassandra)** — The attribute that determines which node/partition a row is stored in.
22. **Clustering column (Cassandra)** — The attribute that determines the order of rows within a partition.

---

# 5-MARK ANSWERS

## 5A. Schema vs Instance
"A **schema** is the overall logical description or blueprint of the database — relations, attributes, data types, keys, constraints and indexes — and is relatively stable. An **instance** is the collection of actual data stored at a particular point in time; inserts, updates and deletions change the instance without necessarily changing the schema. Example: schema `STUDENT(RollNo, Name, Course)`; instance `(101, Ravi, MCA)`. Analogy: the blueprint versus the current building."

## 5B. Physical vs Logical data independence
"**Physical data independence** is the ability to change physical storage structures without changing the conceptual schema — for example replacing an index without rewriting application queries. **Logical data independence** is the ability to modify the conceptual schema without changing every external view or application, provided the required external information can still be produced — for example splitting a table while keeping a compatible view. Physical independence protects the conceptual level from storage changes; logical independence protects user views from design changes."

## 5C. Keys
"A **super key** is any attribute set that uniquely identifies a tuple. A **candidate key** is a *minimal* super key. The **primary key** is the candidate key chosen as the main identifier; an **alternate key** is a candidate key not chosen. A **foreign key** references a key in another relation and enforces referential integrity. Memory: super → candidate → primary; unchosen candidate = alternate; foreign = points elsewhere."

## 5D. Modification anomalies
"Unnormalized designs cause three anomalies. **Insertion anomaly**: a fact cannot be inserted without also inserting an unrelated fact. **Update anomaly**: the same fact is repeated in many rows, so one logical change requires many updates. **Deletion anomaly**: deleting one fact accidentally removes another fact that should have been retained. Normalization is the standard cure because it removes the repetition that causes them."

## 5E. Isolation levels
"SQL defines increasing isolation: **Read Uncommitted** may read uncommitted changes (weakest); **Read Committed** prevents ordinary dirty reads; **Repeatable Read** adds repeat-read guarantees (phantom behaviour depends on the DBMS); **Serializable** is the strongest and aims for serial-equivalent behaviour. Higher isolation reduces anomalies — dirty read, non-repeatable read, phantom — at the cost of concurrency."

## 5F. Concurrency anomalies
"**Lost update**: a later write overwrites an earlier write from another transaction. **Dirty read**: a transaction reads a value written by one that has not committed. **Non-repeatable read**: the same row read twice returns different committed values because another transaction updated it between the reads. **Phantom read**: a repeated predicate query returns a different set of rows because of another transaction's inserts/deletes."

## 5G. Deferred vs Immediate update
"In **deferred update**, changes are not written to the database until commit, so after a crash committed transactions may need REDO while uncommitted ones normally need **no** UNDO. In **immediate update**, a modified page may be written before commit, so recovery must **UNDO** uncommitted changes and **REDO** committed ones that may not have reached disk. Deferred = delay the data; immediate = data may already be on disk."

## 5H. Replication benefits and costs
"Replication maintains multiple copies — **full** (all/many sites) or **partial** (selected sites). Benefits: higher availability, faster local reads, failure tolerance and reduced remote access. Costs: additional storage, update coordination, consistency management and network/control overhead. Allocation decides which site holds which fragment or replica, considering query frequency, locality, communication cost, storage capacity and reliability."

## 5I. NoSQL — four models
"**Document** stores JSON/BSON-like documents — catalogs, content, profiles. **Key-value** maps keys to values — caches, sessions, simple lookups. **Column-family** stores partitioned rows with flexible columns — large-scale distributed workloads. **Graph** stores nodes, relationships and properties — social networks, recommendations, fraud detection. The choice depends on access pattern: documents for flexible nested data, key-value for lookups, wide-column for scale, graph for relationship traversal."

## 5J. ACID (5-mark version)
"**Atomicity**: the transaction is all-or-nothing — if an essential operation fails the whole transaction rolls back (debit *and* credit both occur). **Consistency**: every committed transaction preserves integrity constraints and valid rules, so no invalid account state results. **Isolation**: intermediate effects of concurrent transactions are controlled so execution is equivalent to an acceptable serial behaviour — no transaction sees a half-completed transfer. **Durability**: once committed, effects survive subsequent system failure, subject to the DBMS's durability guarantees."

## 5K. Fragmentation types
"**Horizontal** fragmentation splits rows by predicates (e.g. `CUSTOMER_NORTH`). **Vertical** fragmentation splits columns and repeats the primary key in each fragment so the relation is reconstructed by a join. **Hybrid** combines both. A sound fragmentation satisfies completeness, reconstruction and — where required — disjointness."

## 5L. B+ tree vs Hash index
"A **B+ tree** is an ordered, balanced structure: internal nodes hold separator keys and child pointers, leaves hold keys plus record pointers and are linked, so equality, range, prefix and sorted retrieval all work (O(log_f N)). A **hash index** maps a key through a hash function to a bucket, giving fast equality lookups but no ordering, so range queries and ORDER BY are poor. Use B+ trees for range/ordered workloads and hash for exact-key lookups."

---

# 10-MARK ANSWERS

## 10A. Three-level architecture and data independence
**INTRODUCTION** — Database systems hide implementation details through data abstraction; the classic three-level architecture separates user views, logical organization and physical storage.
**DIAGRAM** — draw D1 (External → Conceptual → Internal → Physical).
**COMPONENTS**
1. **External level** — customised views (student sees courses/marks; accounts sees fees/payments); improves simplicity and security.
2. **Conceptual level** — complete logical structure independent of physical storage: entities, attributes, relationships, constraints.
3. **Internal level** — physical representation: files, pages, record placement, indexes, access paths.
**DATA INDEPENDENCE** — physical: change storage without changing the conceptual schema (change an index). Logical: change the conceptual schema without changing every external view/application, when required external information can still be provided.
**EXAMPLE** — replacing an index = physical; splitting a table with a compatible view = logical.
**CONCLUSION** — independence lets the design and technology evolve independently, reducing maintenance cost and protecting applications.

## 10B. ER modeling (entities, attributes, keys, cardinality)
**INTRODUCTION** — The ER approach is a high-level conceptual technique used before implementation to describe entities, attributes, relationships and constraints in an understandable form.
**DIAGRAM** — draw D2 (STUDENT ◇ ENROLLS ◇ COURSE, M:N, EnrollmentDate).
**COMPONENTS** — *Entities* (STUDENT, EMPLOYEE) and entity sets. *Attributes*: simple, composite, single-valued, multivalued, derived, key. *Keys*: super → candidate → primary; alternate; foreign. *Relationships* and cardinality 1:1 / 1:N / M:N (Person–Passport, Department–Employee, Student–Course). *Participation*: total = mandatory, partial = optional.
**EXAMPLE** — `EnrollmentDate` is a relationship attribute because it describes the enrollment event.
**LIMITATION** — ER is conceptual: it must be mapped to a relational schema before implementation.
**CONCLUSION** — a clear ER model prevents structural errors early and communicates the design to examiners and users.

## 10C. ER → relational mapping
**INTRODUCTION** — mapping transforms the conceptual ER design into tables.
**RULES (numbered)** — strong entity → relation with its PK · composite → store components · multivalued → separate relation (owner PK + value) · 1:1 → PK of one side as FK (prefer total participation) · 1:N → 1-side PK as FK on the N-side · M:N → new relation with both PKs (composite key) · weak entity → attributes + owner key + partial key.
**EXAMPLE** — `STUDENT(StudentID, Name)`, `COURSE(CourseID, Title)`, `ENROLLS(StudentID, CourseID, EnrollDate)`.
**DIAGRAM** — before/after (D14).
**TRAPS** — FK on the N-side; M:N must create a new relation, not a column.
**CONCLUSION** — correct mapping preserves keys, relationships and integrity when the design is implemented.

## 10D. Conflict serializability and the precedence graph
**INTRODUCTION** — concurrency control coordinates simultaneous transactions because interleaving can break correctness.
**CONCEPTS** — conflict = same data item, at least one write, different transactions. Serial vs serializable (interleaved but equivalent to some serial schedule).
**ALGORITHM** — (1) node per transaction; (2) add edge Ti → Tj when a conflicting op of Ti precedes Tj's; (3) acyclic ⇒ conflict-serializable; (4) cycle ⇒ not conflict-serializable.
**EXAMPLE** — T1: R(X), W(X); T2: R(X) ⇒ edge T1 → T2 ⇒ acyclic.
**ALTERNATIVES** — locks (2PL) vs timestamps as ways to *produce* serializable schedules.
**CONCLUSION** — the graph is the test; 2PL and timestamp ordering are protocols that guarantee serializability.

## 10E. Two-phase locking (with deadlock)
**INTRODUCTION** — a lock controls access to a data item; S locks (read) are compatible with each other, X locks (write) conflict with everything.
**DIAGRAM** — D6: growing → lock point → shrinking.
**RULE** — growing: acquire only; shrinking: release only. Basic 2PL ⇒ conflict serializability. **Strict 2PL** holds X locks until commit/abort (reduces cascading rollbacks); **rigorous** holds S and X until completion.
**DEADLOCK** — cycle of waits (T1 holds A wants B; T2 holds B wants A) handled by prevention, avoidance, detection (wait-for graph) and timeout.
**EXAMPLE** — compatibility table (S/S compatible; everything else not).
**CONCLUSION** — 2PL buys correctness with reduced concurrency; strict variants trade more holding for fewer cascading aborts.

## 10F. Log-based recovery, WAL and checkpoints
**INTRODUCTION** — recovery restores a consistent state after failure.
**LOG** — sequential record on stable storage: transaction ID, data item, old value, new value (`<T1, A, 100, 50>`).
**WAL** — log record must reach stable storage **before** the corresponding data page is written, guaranteeing enough information to undo or redo.
**CHECKPOINT** — recovery starts from the recent checkpoint instead of scanning the entire log.
**UNDO/REDO** — committed → REDO as needed; uncommitted → UNDO as needed.
**DIAGRAM** — D7.
**EXAMPLE** — log with T1 committed, T2 uncommitted after a crash.
**CONCLUSION** — logging plus checkpoints makes recovery fast, complete and repeatable.

## 10G. CAP theorem (exact)
**INTRODUCTION** — distributed systems must reason about partition behaviour.
**DIAGRAM** — D9 triangle with the caption.
**DEFINITIONS** — C: read observes the most recent write per the formal guarantee, or an error. A: every request to a non-failing node gets a non-error response (not necessarily the latest value). P: the system continues despite network failures between nodes.
**THE STATEMENT** — during a network partition a system cannot guarantee both strong consistency and availability for every request under the formal CAP definitions.
**TRADE-OFF** — during a partition, choose what to preserve; stronger consistency needs more coordination and affects latency/availability. Relate to BASE: basically available, soft state, eventual consistency.
**⚠** — never write "pick any two at all times."
**CONCLUSION** — CAP is a design-choice framework for partition behaviour, not a slogan.

## 10H. Indexing across relational and NoSQL systems
**INTRODUCTION** — an index is an auxiliary access path; without it a query scans records 1…N.
**STORAGE BASIS** — pages/blocks and the buffer manager: reducing page I/O is the objective.
**B+ TREE** — separators + pointers, linked leaves, O(log_f N), range queries. **HASH** — key → bucket, equality only, collisions via overflow/chaining/dynamic hashing. **Compare** (table).
**NoSQL** — *MongoDB*: single-field/compound/multikey/text/geospatial/unique; field order matters; `explain()`. *CouchDB*: Mango indexes + map/reduce views with ordered keys. *Cassandra*: partition key = location, clustering = order; secondary indexes don't replace partition design. *Neo4j*: property indexes find starting nodes, then traversal. *Vector*: HNSW (graph) and IVF (clusters) for top-k similarity.
**BENEFITS vs COSTS** — fewer scans, lower latency, filtering/sorting/nearest-neighbour ↔ storage, write overhead, cache pressure, useless indexes.
**CONCLUSION** — indexes must be **query-driven**; design for important query patterns, not maximum index count.

---

# 20-MARK SKELETONS (expand each bullet into a paragraph + diagram)

> Source: the notebook's "Master 20-Mark Answer Bank". These are **answer plans**, not predicted questions.

## Q1 — Explain normalization and all normal forms
1. Define normalization; why redundancy is harmful (anomalies).
2. Functional dependencies and candidate keys (closure).
3. 1NF with an atomic-value example (Phones → STUDENT_PHONE).
4. 2NF and partial dependency with a composite key (ENROLL).
5. 3NF and transitive dependency (EMPLOYEE/DEPARTMENT).
6. BCNF and the super-key determinant rule ("every determinant is a super key").
7. Multivalued dependency and 4NF (hobbies/languages).
8. Join dependency and 5NF.
9. Lossless join and dependency preservation (with the test).
10. Minimal cover and attribute closure.
11. Conclude: benefits of a properly normalized design.
**Draw:** the normalization ladder (D3) + the 2NF and 3NF decomposition diagrams (D16, D17).

## Q2 — Transaction processing, concurrency control and recovery
1. Transaction + bank-transfer example · 2. States · 3. ACID · 4. SQL transactions and isolation levels ·
5. Concurrent schedules and anomalies · 6. Serializability + precedence graph · 7. S/X locks ·
8. 2PL and strict 2PL · 9. Deadlock and handling · 10. Timestamp ordering · 11. Failure types ·
12. Deferred update, immediate update, shadow paging · 13. Log-based recovery, WAL, checkpoints ·
14. UNDO and REDO · 15. Conclude with the importance of reliability.
**Draw:** transaction states (D5), 2PL (D6), recovery/log (D7).

## Q3 — Distributed databases and CAP
1. Define distributed database/DDBMS · 2. Architecture diagram · 3. Characteristics and types (homogeneous/heterogeneous/federated) ·
4. Horizontal/vertical/hybrid fragmentation · 5. Replication and allocation · 6. Distributed transactions ·
7. 2PC with diagram · 8. Consistency models · 9. Define CAP accurately · 10. Explain C, A, P ·
11. Behaviour during a partition · 12. ACID vs BASE · 13. Sharding strategies · 14. Conclude with design trade-offs.
**Draw:** distributed architecture (D8), CAP (D9), 2PC (D12), sharding (D10).

## Q4 — NoSQL systems and MongoDB
1. Define NoSQL and its motivation · 2. The four models · 3. Compare the four models · 4. CAP and BASE ·
5. Sharding · 6. MongoDB document model · 7. Relational→MongoDB mapping · 8. CRUD with commands ·
9. Query operators · 10. Aggregation pipeline with diagram · 11. Applications and benefits ·
12. Conclude with when document databases are useful.
**Draw:** Mongo hierarchy (D27-style), aggregation flow (D20/P20).

## Q5 — Indexing in relational and NoSQL databases
1. Define index + why needed · 2. Storage pages and I/O · 3. B+ tree structure and operations · 4. B+ tree range search ·
5. Hash indexing and collisions · 6. Compare B+ tree vs hash · 7. MongoDB indexes and compound ordering ·
8. CouchDB Mango/view indexing · 9. Cassandra partition and clustering order · 10. Neo4j property indexes ·
11. Vector embeddings and vector indexes · 12. HNSW/ANN · 13. Benefits and index-maintenance costs ·
14. Conclude with query-driven indexing.
**Draw:** B+ tree (D4), with/without index flow, traditional vs vector index table (C36).
