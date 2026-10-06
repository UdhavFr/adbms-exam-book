# ultra-short-notes.md — Rapid Revision Only
One line per fact. If a line is unfamiliar, open the linked file for the full version.
Companion: `final-cram.md` (even tighter), `definitions.md` (exact wording), `errata.md` (source caveats).

---

## UNIT 1
- DB = organized collection of logically related data · DBMS = define, store, retrieve, update, secure, recover · DB + DBMS = database system.
- File-system cures: redundancy→centralized · inconsistency→constraints · sharing/security/concurrency/recovery→shared DB + auth + concurrency control + logging/checkpoints · program-data dependence→abstraction/independence.
- DBMS functions (9): schema · storage/retrieval · query/optimization · transactions · concurrency · integrity · security · backup/recovery · metadata.
- Data models: hierarchical, network, relational, ER, object-oriented, document, key-value, column-family, graph.
- Schema = blueprint (stable) · Instance = contents now (changes constantly).
- Levels: **External (views) → Conceptual (logical schema) → Internal (files/pages/indexes) → storage**.
- Physical independence = change storage, keep conceptual · Logical independence = change conceptual, keep views.
- Attributes: simple, composite, single-valued, multivalued, derived, key.
- Keys: super (any unique) → candidate (minimal) → primary (chosen) · alternate (unchosen) · foreign (points to another relation).
- ER: entity/attribute/relationship · cardinality 1:1, 1:N, M:N (Person–Passport / Dept–Employee / Student–Course) · total = mandatory, partial = optional.
- Mapping: strong→table · composite→components · multivalued→own table · 1:1→FK (prefer total side) · 1:N→**FK on N side** · M:N→new table (both PKs) · weak→owner key + partial key.
- Relational terms: relation/table · tuple/row · attribute/column · domain/permitted values · degree=#columns · cardinality=#rows · PK identifier · FK reference.
- Algebra: σ = rows, π = columns, ∪ − × ⋈.
- SQL: DDL CREATE/ALTER/DROP/TRUNCATE · DML SELECT/INSERT/UPDATE/DELETE · DCL GRANT/REVOKE · TCL COMMIT/ROLLBACK/SAVEPOINT.
- Processing order: FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT (WHERE = rows before grouping; HAVING = groups after).
- Integrity: domain (type) · entity (PK not null, unique) · referential (FK → existing key or NULL allowed) + UNIQUE/CHECK/NOT NULL · actions CASCADE/SET NULL/SET DEFAULT/RESTRICT.
- Anomalies: insertion · update · deletion.
- Design flow: requirements → ER → constraints → schema → normalization → SQL.

## UNIT 2
- FD: X→Y = agreement on X forces agreement on Y; X = determinant · trivial Y⊆X · partial = part of composite key · transitive X→Y→Z⇒X→Z.
- Closure X⁺: start with X, add RHS of any FD whose LHS is inside, loop; X⁺ = all attributes ⇒ super key.
- Ladder: UNF → 1NF(atomic) → 2NF(no partial) → 3NF(no transitive / X superkey **or** A prime) → BCNF(**every determinant is a super key**) → 4NF(no non-key MVD) → 5NF(JD implied by candidate keys).
- **3NF = OR · BCNF = ONLY.**
- 2NF example: ENROLL(StudentID, CourseID, StudentName, CourseName, Grade) → STUDENT / COURSE / ENROLL.
- 3NF example: EMPLOYEE(EmpID, DeptID, DeptName) → EMPLOYEE + DEPARTMENT.
- 4NF example: STUDENT hobby/language independence → STUDENT_HOBBY + STUDENT_LANGUAGE.
- Lossless: join = original exactly; test (R1∩R2)→R1 or →R2 · Preserving: FDs checkable without joins · independent properties.
- Minimal cover: Split RHS → Extraneous LHS → Remove redundant FDs · equivalent iff F⁺ = G⁺.
- Storage: pages/blocks, buffer manager, page I/O is the cost · heap (inserts) · sorted (range) · hash (equality) · clustered (related together).
- B+ tree: internal = separators + pointers, leaves = keys + record pointers **linked** · search Root→Compare→Child→Leaf→Record · O(log_f N) · linked leaves = range scans.
- Hash: key → hash → bucket → records · collision = same bucket (overflow/chaining/dynamic hashing) · equality only.

## UNIT 3
- Transaction = logical unit of work preserving correctness · bank: debit A + credit B or neither.
- States: ACTIVE → PARTIALLY COMMITTED → COMMITTED · FAILED → ABORTED.
- ACID: atomic (all-or-nothing) · consistent (constraints hold) · isolated (serial-equivalent, no half-transfers visible) · durable (survives failure).
- SQL: BEGIN → ops → COMMIT | ROLLBACK · SAVEPOINT = partial rollback · RU → RC → RR → S.
- Anomalies: lost update (write overwrites write) · dirty read (uncommitted read) · non-repeatable (same row twice differs) · phantom (predicate returns different set).
- Serial = no interleave · Serializable = interleave but equivalent to some serial order.
- Conflict serializability: conflicts = same item + ≥1 write; edge Ti→Tj when Ti first; **acyclic ⇒ serializable, cycle ⇒ not**.
- Locks: S=read (S+S ok) · X=write (conflicts with S and X).
- 2PL: GROWING (acquire only) → LOCK POINT → SHRINKING (release only) · basic ⇒ conflict serializable · strict ⇒ X until commit · rigorous ⇒ S+X until completion.
- Deadlock: cycle of waits · PADT = prevention, avoidance, detection (wait-for graph), timeout.
- Timestamps: older = smaller · Read_TS/Write_TS per item · violation ⇒ abort/restart · no lock-wait deadlock, but wasted work.
- Failures: transaction · system crash (volatile lost) · media (persistent lost) · communication (distributed).
- Deferred update = write only after commit (REDO committed; no UNDO for uncommitted) · Immediate = may write before commit (UNDO uncommitted + REDO committed).
- Shadow paging: stable shadow table + current table · commit switches root · crash → use shadow.
- Log: <TID, item, old, new> on stable storage · **WAL: log before data page** · checkpoint = recovery start point.
- Rule: **committed → REDO · uncommitted → UNDO.**

## UNIT 4
- Distributed DB = logically integrated, physically distributed across networked sites · homogeneous / heterogeneous / federated.
- Fragmentation: horizontal = rows (predicates) · vertical = columns (+ PK repeated) · hybrid = both · properties: completeness, reconstruction, disjointness.
- Replication: full/partial copies · benefits = availability, local reads, failure tolerance, less remote access · costs = storage, update coordination, consistency, overhead · allocation = which site stores what.
- 2PC: coordinator PREPARE → votes YES/NO → COMMIT if all YES else ABORT · can block.
- Consistency models: strong/linearizable · eventual · causal · session (read-your-writes, monotonic reads).
- **CAP: during a network partition, cannot guarantee both strong consistency and availability for every request (formal definitions).** Never say "any two at all times."
- C = read sees latest write or error · A = non-failing node answers (may be stale) · P = survives network failure.
- BASE = Basically Available · Soft state · Eventual consistency (temporary inconsistency accepted, converges).
- Sharding = horizontal split across nodes · range (hotspots) / hash (even, no ranges) / directory (mapping service) / geographic (region) · good key = even spread, query-friendly, no hotspots.
- MongoDB: database → collection → document → field · PK = `_id` · BSON, nested docs/arrays.
- CRUD: insertOne/insertMany · find/findOne · updateOne/updateMany · deleteOne/deleteMany.
- Operators: `$gt $gte $lt $lte $eq $ne` · `$in $nin` · `$and $or $not $nor` · `$set $unset $inc $push $pull`.
- Pipeline: **$match → $group → $project → $sort → $limit** (+$skip $unwind $lookup) · example: paid sales by product sorted desc.

## UNIT 5
- Wide-column: row keys/column families, huge scale · HBase = Hadoop ecosystem, row key + families, APIs/shell · Cassandra = independent, **partition key + clustering columns**, CQL, availability/scale/write throughput.
- Cassandra: model tables around **query patterns**; duplicate deliberately to avoid joins; explicit schema (ALTER TABLE, cluster-wide).
- `PRIMARY KEY ((course), year, student_id)` → course = partition (location), year & student_id = clustering (order).
- Redis: in-memory key-value · SET/GET/DEL/EXISTS · HSET/HGET · EXPIRE · INCR · caching, sessions, counters, queues, leaderboards.
- Graph: nodes = entities, edges = relationships, properties = attributes · social/recommendation/fraud/knowledge/dependency.
- Neo4j/Cypher: `CREATE (p:Person {..})` · `MATCH (a)-[:REL]->(b) RETURN …` · WHERE · SET · DETACH DELETE · ORDER BY · multi-hop patterns.
- Embedding = numerical vector from an embedding model; similar objects near each other.
- Search: query → embed → vector index → top-k → metadata → results · brute force = all vectors · ANN = promising region.
- Similarity: cosine = angle · Euclidean = straight line · dot = alignment + magnitude.
- HNSW = graph navigation · IVF = clusters.
- Index = auxiliary access path; faster reads ↔ storage + maintenance; too many indexes slow writes; useless if the query doesn't match.
- MongoDB indexes: single-field, compound (field **order** matters), multikey, text, geospatial, unique · `explain()`.
- CouchDB: Mango indexes (selector) + map/reduce views (ordered keys, ranges).
- Neo4j: property index finds **starting node**, then traversal.
- Traditional index (B+ tree/hash, exact/range) vs vector index (HNSW/IVF, similarity/top-k).
- 20-mark indexing answer = compare MongoDB, CouchDB, Cassandra, Neo4j, vector indexes + benefits/costs + query-driven conclusion.

---

## Ten diagrams (draw blind)
1 External→Conceptual→Internal→storage · 2 STUDENT◇ENROLLS◇COURSE (M:N) · 3 normalization ladder · 4 B+ tree linked leaves ·
5 transaction states · 6 growing/lock point/shrinking · 7 log→checkpoint→undo/redo · 8 sites↔network · 9 CAP triangle ·
10 data→shards · (11 vector pipeline).

## Answers that are always worth marks
Definition first · labelled diagram · headings · one worked example · advantages **and** limitations · actual commands for MongoDB/Cassandra/Redis/Neo4j · conclusion (correctness/performance/scalability/reliability).
