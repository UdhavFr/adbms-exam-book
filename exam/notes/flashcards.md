# flashcards.md — Active-Recall Deck

Format: **Q → A**. Say your answer out loud *before* reading A. Mark each card:
`✓` got it · `~` partial · `✗` wrong. Any `✗` or `~` gets re-tested later (see `revision-plan.md` and `weakness-tracker.md`).

---

## Deck A — Exact definitions (Unit 1)

1. **Q:** Define a database. **A:** An organized collection of logically related data representing information about an application or organization.
2. **Q:** Define a DBMS (verbatim). **A:** Software that allows users and applications to define, create, store, retrieve, update, protect and recover data in a controlled manner; database + DBMS = database system.
3. **Q:** Name 3 problems of file systems DBMS cures. **A:** Redundancy, inconsistency, difficult sharing (also: security, concurrency, recovery, program-data dependence).
4. **Q:** Name the 9 DBMS functions. **A:** Data definition/schema · storage/retrieval · query processing/optimization · transactions · concurrency control · integrity · security · backup/recovery · metadata/catalog.
5. **Q:** Schema vs instance? **A:** Schema = logical blueprint (stable); instance = actual contents at a point in time (changes frequently).
6. **Q:** What changes when you INSERT a row? **A:** The instance only — not the schema.
7. **Q:** List the 3 levels of abstraction. **A:** External (user views) → Conceptual (complete logical schema) → Internal (files/pages/indexes/access paths) → physical storage.
8. **Q:** Physical data independence? **A:** Change physical storage structures without changing the conceptual schema (e.g. change an index).
9. **Q:** Logical data independence? **A:** Change the conceptual schema without changing every external view/application, when required external information can still be provided.
10. **Q:** Which independence = which layer? **A:** Physical = storage/internal layer; Logical = conceptual layer.
11. **Q:** 6 attribute types? **A:** Simple, composite, single-valued, multivalued, derived, key.
12. **Q:** Super vs candidate vs primary vs alternate vs foreign key? **A:** Any unique set / minimal unique set / chosen candidate / unchosen candidate / references another relation's key.
13. **Q:** Cardinality ratios in ER? **A:** 1:1, 1:N, M:N — anchors: Person–Passport, Department–Employee, Student–Course.
14. **Q:** Total vs partial participation? **A:** Total = every entity must participate (mandatory); partial = optional.
15. **Q:** Degree vs cardinality of a relation? **A:** Degree = number of attributes; cardinality = number of tuples.
16. **Q:** The three named integrity constraints? **A:** Domain, entity (PK not null + unique), referential (FK matches an existing key or NULL if allowed).
17. **Q:** Three modification anomalies? **A:** Insertion, update, deletion (I-U-D).
18. **Q:** σ and π? **A:** σ selection = rows; π projection = columns.
19. **Q:** SQL categories + commands? **A:** DDL: CREATE/ALTER/DROP/TRUNCATE · DML: SELECT/INSERT/UPDATE/DELETE · DCL: GRANT/REVOKE · TCL: COMMIT/ROLLBACK/SAVEPOINT.
20. **Q:** SQL processing order? **A:** FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT.

## Deck B — Normalization (Unit 2)

21. **Q:** Define functional dependency. **A:** X → Y: whenever two tuples agree on all attributes of X they must agree on all attributes of Y; X is the determinant.
22. **Q:** Trivial FD? **A:** Y ⊆ X.
23. **Q:** Partial vs transitive dependency? **A:** Partial = Y depends on part of a composite key; transitive = X→Y and Y→Z imply X→Z.
24. **Q:** Compute A⁺ for F = {A→B, B→C, C→D}. **A:** {A,B,C,D} ⇒ A is a key.
25. **Q:** When is X a super key (via closure)? **A:** When X⁺ contains every attribute of the relation.
26. **Q:** Ladder order? **A:** UNF → 1NF → 2NF → 3NF → BCNF → 4NF → 5NF.
27. **Q:** What does each NF fix (one word each)? **A:** 1=atomic values · 2=partial dependency · 3=transitive dependency · BC=determinant must be super key · 4=MVD · 5=join dependency.
28. **Q:** 1NF exact? **A:** Each attribute holds atomic values; no repeating groups or nested sets in a field.
29. **Q:** 2NF exact? **A:** In 1NF and every non-prime attribute is fully dependent on the entire candidate key.
30. **Q:** 3NF exact? **A:** In 2NF and for every non-trivial X→A, X is a super key or A is prime (no transitive dependency of non-prime on a key).
31. **Q:** BCNF exact? **A:** For every non-trivial X→Y, X is a super key — every determinant must be a super key.
32. **Q:** 4NF exact? **A:** Every non-trivial multivalued dependency has a super key determinant.
33. **Q:** 5NF exact? **A:** Every non-trivial join dependency is implied by candidate keys.
34. **Q:** 3NF vs BCNF in one line? **A:** 3NF = OR (super key *or* prime); BCNF = ONLY super key — BCNF stricter, may lose dependency preservation.
35. **Q:** 2NF example relation? **A:** ENROLL(StudentID, CourseID, StudentName, CourseName, Grade) — key (StudentID, CourseID); split into STUDENT/COURSE/ENROLL.
36. **Q:** 3NF example relation? **A:** EMPLOYEE(EmpID, DeptID, DeptName): EmpID→DeptID→DeptName transitive → DEPARTMENT(DeptID, DeptName).
37. **Q:** 4NF example? **A:** STUDENT with independent hobbies and languages → STUDENT_HOBBY + STUDENT_LANGUAGE.
38. **Q:** Lossless join definition? **A:** Joining decomposed relations gives exactly the original — no lost or spurious tuples.
39. **Q:** Binary lossless test? **A:** (R1 ∩ R2) → R1 or (R1 ∩ R2) → R2 under F.
40. **Q:** Dependency preservation? **A:** Original FDs enforceable on the parts individually, without joins.
41. **Q:** Do losslessness and preservation imply each other? **A:** No — independent properties.
42. **Q:** Minimal cover steps? **A:** Split RHS (one attribute) → remove extraneous LHS attributes → remove redundant FDs.
43. **Q:** FD sets equivalent when? **A:** F⁺ = G⁺.
44. **Q:** Prime vs non-prime attribute? **A:** Prime = belongs to some candidate key; non-prime = in no candidate key.
45. **Q:** B+ tree internal vs leaf nodes? **A:** Internal: separator keys + child pointers; leaves: search keys + record/data pointers, **linked**.
46. **Q:** B+ tree complexity? **A:** O(log_f N) node visits, f = fan-out.
47. **Q:** Hash index flow? **A:** key → hash function → bucket → records/pointers; collision = two keys in one bucket.
48. **Q:** B+ tree vs hash? **A:** Ordered, equality + range, good ORDER BY vs unordered, equality only, poor ranges.
49. **Q:** Which file organization for equality lookups? **A:** Hash. For ordered/range processing? Sequential/sorted. For frequent inserts? Heap. For related records together? Clustered.
50. **Q:** Why do DBs transfer data in pages? **A:** I/O cost: the buffer manager moves pages/blocks, so reducing page I/O is a major optimization goal.

## Deck C — Transactions (Unit 3)

51. **Q:** Define transaction. **A:** A sequence of database operations forming one logical unit of work that must preserve correctness under concurrency and failure.
52. **Q:** Transaction states in order? **A:** Active → Partially committed → Committed; failure → Failed → Aborted (restart/terminate).
53. **Q:** What does "partially committed" mean? **A:** The final statement has executed but durability/commit completion is not yet done.
54. **Q:** ACID — one line each? **A:** Atomicity = all-or-nothing · Consistency = committed transactions preserve integrity rules · Isolation = intermediate effects controlled so execution is serial-equivalent · Durability = committed effects survive failure.
55. **Q:** Bank example for each ACID letter? **A:** Both debit+credit · no invalid state · nobody sees half a transfer · still there after restart.
56. **Q:** SQL transaction flow? **A:** BEGIN/START TRANSACTION → operations → COMMIT (success) or ROLLBACK (error); SAVEPOINT for partial rollback.
57. **Q:** Isolation levels in order? **A:** Read Uncommitted → Read Committed → Repeatable Read → Serializable.
58. **Q:** Dirty read? **A:** Reading a value written by a transaction that has not committed.
59. **Q:** Lost update? **A:** A later write overwrites an earlier write from another transaction.
60. **Q:** Non-repeatable read vs phantom? **A:** Same row read twice gives different committed values vs same predicate returns a different set of rows.
61. **Q:** Serial vs serializable? **A:** Serial = transactions one after another; serializable = interleaved but equivalent to some serial schedule.
62. **Q:** Conflict serializability test? **A:** Build precedence graph (edge Ti→Tj for conflicting ops of Ti before Tj); acyclic = conflict-serializable, cycle = not.
63. **Q:** What is a conflict? **A:** Same data item, at least one write, different transactions.
64. **Q:** S vs X locks? **A:** S = shared/read, compatible with S; X = exclusive/write, conflicts with S and X.
65. **Q:** 2PL phases? **A:** Growing (acquire, no release) → lock point → shrinking (release, no new acquisition).
66. **Q:** What does basic 2PL guarantee? **A:** Conflict serializability.
67. **Q:** Strict 2PL? Rigorous 2PL? **A:** Hold X locks until commit/abort · hold S and X locks until completion.
68. **Q:** Deadlock + the 4 handling strategies? **A:** Cycle of mutual waits; PADT = Prevention, Avoidance, Detection (wait-for graph), Timeout.
69. **Q:** Timestamp ordering pro/con? **A:** No lock waiting ⇒ no lock-based deadlock; repeated aborts waste work.
70. **Q:** Read_TS / Write_TS? **A:** Largest timestamp of a transaction that successfully read / wrote X.
71. **Q:** Four failure types? **A:** Transaction failure, system crash, media failure, communication failure.
72. **Q:** Deferred update flow? **A:** Log records → no DB write → COMMIT → REDO/apply; uncommitted normally needs no UNDO.
73. **Q:** Immediate update flow? **A:** Log + page may be written pre-commit → on crash UNDO uncommitted and REDO committed if needed.
74. **Q:** Shadow paging? **A:** Stable shadow table + current table; modified pages written to new locations; COMMIT switches root; crash before commit uses the shadow mapping.
75. **Q:** WAL? **A:** The log record must reach stable storage before the corresponding data page is written.
76. **Q:** Checkpoint? **A:** A recorded recovery point so recovery starts there instead of scanning the whole log.
77. **Q:** The single recovery rule? **A:** Committed → REDO as needed; uncommitted → UNDO as needed.

## Deck D — Distributed & NoSQL (Unit 4)

78. **Q:** Define distributed database. **A:** One logically integrated database physically distributed across network-connected sites; DDBMS gives unified access.
79. **Q:** Homogeneous / heterogeneous / federated? **A:** Same DBMS tech / different tech or schemas / independent DBs cooperating via integration.
80. **Q:** Horizontal vs vertical fragmentation? **A:** Split rows by predicates / split columns with PK repeated in each fragment.
81. **Q:** Why repeat the key in vertical fragments? **A:** So the original relation can be reconstructed by a join.
82. **Q:** Fragmentation properties? **A:** Completeness, reconstruction, disjointness where required.
83. **Q:** Replication full vs partial? **A:** Copies at many/all sites vs at selected sites.
84. **Q:** Replication benefits/costs? **A:** Availability, local reads, failure tolerance, less remote access ↔ storage, update coordination, consistency management, network overhead.
85. **Q:** 2PC phases? **A:** Coordinator PREPARE → participants vote YES/NO → all YES = COMMIT, else ABORT → participants execute the decision.
86. **Q:** 2PC weakness? **A:** A prepared participant can block if it cannot learn the coordinator's decision.
87. **Q:** CAP exact statement? **A:** During a network partition, a system cannot guarantee both strong consistency and availability for every request under the formal CAP definitions.
88. **Q:** C, A, P individually? **A:** Read sees most recent write (or error) / every request to a non-failing node gets a non-error response / continues despite network failures.
89. **Q:** What must you never write about CAP? **A:** "You can pick any two out of three at all times."
90. **Q:** BASE? **A:** Basically Available, Soft state, Eventual consistency.
91. **Q:** ACID vs BASE in one line each? **A:** Strong transaction-oriented guarantees vs availability with flexible consistency and eventual convergence.
92. **Q:** Sharding definition? **A:** Horizontal distribution of records across multiple nodes; each shard holds a subset.
93. **Q:** 4 sharding strategies? **A:** Range, hash, directory, geographic.
94. **Q:** Good shard key criteria? **A:** Even data/traffic distribution, supports common queries, avoids hotspots/oversized partitions.
95. **Q:** Consistency models? **A:** Strong/linearizable, eventual, causal, session (read-your-writes, monotonic reads).
96. **Q:** Relational → MongoDB mapping? **A:** Table→Collection, Row→Document, Column→Field, PK→`_id`.
97. **Q:** MongoDB CRUD families? **A:** insertOne/insertMany, find/findOne, updateOne/updateMany, deleteOne/deleteMany.
98. **Q:** MongoDB operator groups? **A:** Comparison `$gt $gte $lt $lte $eq $ne`; membership `$in $nin`; logical `$and $or $not $nor`; update `$set $unset $inc $push $pull`.
99. **Q:** Aggregation pipeline order? **A:** $match → $group → $project → $sort → $limit (+ $skip, $unwind, $lookup).

## Deck E — Stores, indexing, vectors (Unit 5)

100. **Q:** Cassandra partition key vs clustering columns? **A:** Partition key = where the row lives; clustering columns = order of rows within the partition.
101. **Q:** Cassandra design philosophy? **A:** Model tables around query patterns; duplicate data deliberately to avoid joins.
102. **Q:** HBase vs Cassandra (4 contrasts)? **A:** Hadoop ecosystem vs independent · row key + families vs partition + clustering · APIs/shell vs CQL · sparse large data vs highly available write-heavy workloads.
103. **Q:** Redis used for? **A:** Caching, sessions, counters, queues, leaderboards, fast temporary state — in-memory.
104. **Q:** Redis command families? **A:** SET/GET/DEL/EXISTS · HSET/HGET · EXPIRE · INCR.
105. **Q:** Graph model trio? **A:** Nodes = entities, edges = relationships, properties = attributes.
106. **Q:** Cypher command order? **A:** CREATE → MATCH → WHERE → SET → DELETE.
107. **Q:** Cypher pattern syntax? **A:** `MATCH (node)-[:RELATIONSHIP]->(node) RETURN …` — round = node, square = relationship.
108. **Q:** Define embedding. **A:** A numerical vector representation of an object produced by an embedding model; similar objects are placed near each other in vector space.
109. **Q:** Vector search pipeline? **A:** Query → embed → query vector → vector index → top-k → metadata/documents → results.
110. **Q:** Cosine vs Euclidean vs dot? **A:** Angle/direction · straight-line distance · alignment + magnitude.
111. **Q:** Brute force vs ANN? **A:** Compare all vectors (exact, slow) vs search a promising region (approximate, low latency).
112. **Q:** HNSW vs IVF? **A:** Graph-based hierarchical navigable small world vs inverted-file clusters.
113. **Q:** Define index. **A:** An auxiliary access structure that improves lookup performance at the cost of storage and maintenance.
114. **Q:** Index benefits/costs? **A:** Fewer scans, lower latency, filtering/sorting/nearest-neighbour ↔ storage, write overhead, cache pressure, useless if mismatched.
115. **Q:** MongoDB index types? **A:** Single-field, compound, multikey, text, geospatial, unique.
116. **Q:** Why does compound-index field order matter? **A:** It determines which query and sort patterns the index can serve efficiently; check with explain().
117. **Q:** CouchDB indexes? **A:** Mango indexes for selector queries; map/reduce views give ordered keys for range-style access.
118. **Q:** Neo4j indexing? **A:** Property indexes locate starting nodes quickly; traversal then follows relationships.
119. **Q:** Traditional vs vector index? **A:** Exact/range on scalar keys (B+ tree, hash) vs similarity/top-k on vectors (HNSW, IVF).
120. **Q:** Ordered vs unordered index for range queries? **A:** B+ tree (ordered) supports ranges; hash (unordered) does not.

---

## Rapid-fire true/false (say T/F instantly)

| # | Statement | Answer |
|---|---|---|
| T1 | A relation in 2NF may contain transitive dependencies | **T** (that's 3NF's job) |
| T2 | BCNF is less restrictive than 3NF | **F** |
| T3 | Every relation in BCNF is in 3NF | **T** |
| T4 | Lossless decomposition ⇒ dependency preserving | **F** |
| T5 | Serializable means no interleaving | **F** (that's serial) |
| T6 | S and X locks are compatible | **F** |
| T7 | Strict 2PL holds X locks until commit/abort | **T** |
| T8 | Deferred update needs UNDO of uncommitted data pages | **F** (they were never written) |
| T9 | WAL means data page before log record | **F** (log first) |
| T10 | CAP applies equally when the network is healthy | **F** (only meaningful under partition) |
| T11 | Cassandra needs no schema | **F** (explicit schema, ALTER TABLE) |
| T12 | Hash indexes are ideal for range queries | **F** |
| T13 | Compound index field order is irrelevant | **F** |
| T14 | 2PC guarantees progress under all failures | **F** (can block) |
| T15 | Vertical fragments repeat the primary key | **T** |
| T16 | An index never slows writes down | **F** |
| T17 | Cosine similarity depends on vector magnitude | **F** (angle only) |
| T18 | IVF partitions vectors into clusters | **T** |
| T19 | Total participation is optional | **F** (mandatory) |
| T20 | A foreign key may be NULL where permitted | **T** |
