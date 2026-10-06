# MOCK EXAM 1 — Answer Key
Marking notes: 2-mark = definition (1) + clarifier (1). 5-mark = definition (1) + 3–4 correct points (3–4) + example (1).
10-mark = definition (1) + diagram (2) + components (5) + example/pro-con (1) + conclusion (1).
20-mark = stages as listed (14–15 marks) + diagram (3) + conclusion (2).

---

## Section A
**A1.** Database = an organized collection of logically related data representing information about an application/organization. DBMS = software that lets users/applications define, create, store, retrieve, update, protect and recover data; database + DBMS = database system.
**A2.** Schema = logical blueprint/structure of the database, relatively stable. Instance = the actual data stored at a particular point in time; it changes with every insert/update/delete.
**A3.** X → Y means whenever two tuples agree on all attributes of X they must also agree on all attributes of Y; X is the determinant, Y is functionally dependent on X.
**A4.** Every attribute contains atomic values, and there are no repeating groups or nested sets stored in a single field.
**A5.** Atomicity, Consistency, Isolation, Durability.
**A6.** A sequence of database operations that forms one logical unit of work and must preserve database correctness under concurrency or failure.
**A7.** When a distributed system experiences a network partition, it cannot simultaneously guarantee both strong consistency and availability for every request under the formal CAP definitions.
**A8.** Sharding is the horizontal distribution of records across multiple nodes, each shard storing a subset of the dataset.
**A9.** A numerical vector representation of an object produced by an embedding model (semantically similar objects are placed near each other in vector space).
**A10.** An auxiliary data structure/access path that improves lookup performance at the cost of storage and maintenance.

## Section B
**B1.** *Physical data independence* = change physical storage structures (files, indexes, pages) without changing the conceptual schema — example: replacing an index. *Logical data independence* = modify the conceptual schema without changing every external view/application as long as required external information can still be provided — example: splitting a table while keeping a compatible view. One mark each for definition, example, and the "which layer changes" distinction.
**B2.** Simple (not divisible — Age) · Composite (components — Address = Street/City/PIN) · Single-valued (one value per entity) · Multivalued (several values — phone numbers) · Derived (calculated — Age from DateOfBirth) · Key (uniquely identifies — StudentID).
**B3.** Super key = any attribute set that uniquely identifies a tuple; Candidate key = *minimal* super key; Primary key = the chosen candidate key; Alternate key = a candidate key not chosen; Foreign key = attribute(s) referencing a key in another relation (enforces referential integrity).
**B4.** Insertion anomaly: a fact cannot be inserted without also inserting an unrelated fact. Update anomaly: the same fact is repeated in many rows so one logical change requires multiple updates. Deletion anomaly: deleting one fact accidentally removes another fact that should be retained.
**B5.** DDL: CREATE, ALTER, DROP, TRUNCATE (define/modify structure) · DML: SELECT, INSERT, UPDATE, DELETE (retrieve/change data) · DCL: GRANT, REVOKE (privileges/security) · TCL: COMMIT, ROLLBACK, SAVEPOINT (transaction control).
**B6.** 3NF: for every non-trivial X → A, X is a super key **OR** A is prime (and 2NF, no transitive dependency). BCNF: for every non-trivial X → Y, X **must be** a super key — every determinant is a super key. BCNF is more restrictive; 3NF usually preserves dependencies while BCNF may lose dependency preservation. Every BCNF relation is in 3NF, not conversely. Memory: 3NF = OR, BCNF = ONLY.
**B7.** Deferred update: DB changes are written only after COMMIT (log records kept meanwhile); after a crash, committed transactions may need REDO and uncommitted ones normally need no UNDO. Immediate update: a modified page may be written before commit; after a crash, UNDO uncommitted changes and REDO committed changes that may not have reached disk.
**B8.** HBase: strong Hadoop ecosystem relationship · row key + column families · HBase APIs/shell · designed for large-scale sparse data with random read/write. Cassandra: independent distributed wide-column system · partition key + clustering columns · CQL · designed for high availability, horizontal scalability and high write throughput.

## Section C
**C1.** Definition of data abstraction; **diagram**: External → Conceptual → Internal → physical storage. External level: customised user views (student vs accounts views) — simplicity and security. Conceptual level: complete logical structure (entities, attributes, relationships, constraints) independent of physical storage. Internal level: physical representation — files, pages, record placement, indexes, access paths. Then physical independence (storage change, conceptual unchanged — change an index) vs logical independence (conceptual change, external views preserved — split a table with a compatible view). Conclusion: independent evolution reduces maintenance and protects applications.
**C2.** Transaction definition + bank transfer (debit A, credit B, all or nothing). **Atomicity**: all-or-nothing; failure ⇒ rollback (both debit and credit occur). **Consistency**: committed transactions preserve integrity constraints (no invalid account state). **Isolation**: intermediate effects controlled so execution is equivalent to an acceptable serial behaviour (nobody sees a half-transfer). **Durability**: committed effects survive subsequent failure, subject to DBMS guarantees (still there after restart). Isolation levels: Read Uncommitted → Read Committed → Repeatable Read → Serializable (with what each prevents).
**C3.** B+ tree: balanced multiway search tree; internal nodes = separator keys + child pointers; leaf nodes = search keys + record/data pointers, **linked**; search path root → compare → child → leaf → record; complexity O(log_f N); advantages: balanced height, high fan-out, linked leaves for range scans, dynamic updates, disk-page fit. **Diagram required.** Hash: key → hash function → bucket → records; collisions handled by overflow buckets/chaining/dynamic hashing; equality only, unordered. Comparison table: ordered/unordered, equality+range vs equality only, good/poor for ORDER BY. Range query ⇒ **B+ tree** (leaf chain), hash cannot support ordered traversal.

## Section D (20 marks) — marking stages
1. Define normalization + why redundancy is harmful (anomalies) — 2
2. Functional dependencies (definition, types) and candidate keys; attribute closure algorithm + example — 3
3. 1NF with atomic-value example (Phones → STUDENT_PHONE) — 2
4. 2NF: fully dependent on entire candidate key; ENROLL partial dependencies → STUDENT/COURSE/ENROLL — 3
5. 3NF: X super key OR A prime; EMPLOYEE transitive → DEPARTMENT — 3
6. BCNF: every determinant a super key — 2
7. MVD + 4NF with hobbies/languages — 2
8. Join dependency + 5NF — 2
9. Lossless join (definition + test) and dependency preservation (definition + independence of the two) — 3
10. Minimal cover steps (split/extraneous/redundant) — 1
11. Diagram of the ladder + conclusion on benefits — 3
*(Total capped at 20; partial credit per correct stage.)*
