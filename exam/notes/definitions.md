# definitions.md — Exact Definitions to Reproduce in the Exam

How to use: **Memory line** = what you recall at the desk. **Exam-ready** = the sentence you write for marks
(write it almost word-for-word). **Plain** = the meaning, for understanding only — never write it as the definition.
Source refs use unit/section IDs from `structure.md`. Companion: `errata.md` E1–E7.

---

## UNIT 1 — Concepts & Conceptual Modeling

### Database
- **Memory:** organized collection of logically related data.
- **Exam-ready:** "A database is an organized collection of logically related data that represents information about a particular application or organization."
- **Plain:** one place where related facts live together.

### DBMS  ← *19-word exact definition, memorise verbatim*
- **Memory:** D-S-R-U-S-R: Define, Store, Retrieve, Update, Secure, Recover.
- **Exam-ready:** "A DBMS is software that allows users and applications to define, create, store, retrieve, update, protect and recover data in a controlled manner. The database together with the DBMS forms a database system."
- **Plain:** the program between you and the raw data.

### File-processing system (why DBMS is needed)
- **Memory:** redundancy → inconsistency → sharing/security/concurrency/recovery/program-data dependence.
- **Exam-ready:** "In a file-processing system the same data is duplicated across application files, so a change to one copy leaves the others inconsistent; sharing, security, backup, concurrent access and recovery are also difficult."
- **Plain:** each app owns its own files; nobody can trust any single copy.

### Data model
- **Memory:** vocabulary for describing structure + relationships + constraints (+ operations).
- **Exam-ready:** "A data model is a collection of concepts used to describe the structure of data, relationships among data items, constraints, and sometimes operations."
- **Plain:** the rules of the drawing you use to design a database.

### Schema
- **Memory:** blueprint.
- **Exam-ready:** "A schema is the overall logical description or blueprint of the database — relations, attributes, data types, keys, relationships, constraints and indexes. It is relatively stable compared with the actual data."
- **Plain:** the design, not the contents.

### Instance
- **Memory:** current contents at a moment in time.
- **Exam-ready:** "An instance is the collection of actual data stored in the database at a particular point in time; inserts, updates and deletions change the instance without necessarily changing the schema."
- **Plain:** what is actually in the building today.

### Data abstraction
- **Memory:** hide implementation detail.
- **Exam-ready:** "Data abstraction hides unnecessary implementation details from users by separating external views, the conceptual logical design, and the internal physical storage."
- **Plain:** you query *what*, not *where the bytes are*.

### Physical data independence
- **Memory:** P = Pages/physical — change storage without changing logical schema.
- **Exam-ready:** "Physical data independence is the ability to change physical storage structures without changing the conceptual schema — e.g. replacing an index without rewriting application queries."
- **Plain:** reorganise the warehouse, keep the catalogue.

### Logical data independence
- **Memory:** L = Logic — change conceptual schema without breaking external views/applications.
- **Exam-ready:** "Logical data independence is the ability to modify the conceptual schema without requiring changes to every external view or application, as long as the required external information can still be provided."
- **Plain:** redesign tables, keep the reports working.

### Entity / entity set
- **Memory:** entity = thing; entity set = collection of similar things.
- **Exam-ready:** "An entity is a distinguishable real-world object about which data is stored; an entity set is a collection of similar entities (e.g. STUDENT)."
- **Plain:** one student vs. the students table.

### Attribute types (six)
- **Memory:** Simple, Composite, Single-valued, Multivalued, Derived, Key.
- **Exam-ready:** "Simple attributes cannot be divided further; composite attributes have components (Address = Street, City, PIN); single-valued have one value per entity; multivalued have several (phone numbers); derived attributes are calculated from others (Age from DateOfBirth); a key attribute uniquely identifies an entity."
- **Plain:** six flavours of column.

### Super key / Candidate key / Primary key / Alternate key / Foreign key
- **Memory:** nested boxes: Super → Candidate (minimal) → Primary (chosen); unchosen Candidate = Alternate; Foreign points elsewhere.
- **Exam-ready:** "A super key is any attribute set that uniquely identifies a tuple; a candidate key is a *minimal* super key; the primary key is the candidate key selected as the main identifier; an alternate key is a candidate key not selected; a foreign key is an attribute(s) referencing a key in another relation."
- **Plain:** who can identify a row, and who points at whom.

### Relationship & cardinality ratio
- **Memory:** association; 1:1 | 1:N | M:N. Anchors: Person–Passport / Department–Employee / Student–Course.
- **Exam-ready:** "A relationship represents an association between entities; cardinality describes how many instances of one entity can participate — 1:1, 1:N or M:N."
- **Plain:** how many on each side.
- ⚠ **Do not confuse** with *cardinality of a relation = number of tuples* (errata E1).

### Participation constraint
- **Memory:** total = mandatory (double line), partial = optional (single line).
- **Exam-ready:** "Total participation means every entity must participate in the relationship; partial participation means participation is optional."
- **Plain:** must every student be enrolled, or only some?

### Three-level architecture (ANSI/SPARC)
- **Memory:** E-C-I: External → Conceptual → Internal → Physical.
- **Exam-ready:** "The external level describes customised user views; the conceptual level represents the complete logical structure independent of physical storage; the internal level describes physical representation — files, pages, indexes, access paths."
- **Plain:** view / logical design / storage layout.

### Relational model terms
- **Memory:** Relation=table, Tuple=row, Attribute=column, Domain=allowed values, Degree=#columns, Cardinality=#rows.
- **Exam-ready:** "A relation is a table of tuples; each attribute has a domain of permissible values; degree is the number of attributes and cardinality the number of tuples."
- **Plain:** table vocabulary.

### Integrity constraints (three + three)
- **Memory:** D-E-R (Domain, Entity, Referential) + U-C-N (UNIQUE, CHECK, NOT NULL).
- **Exam-ready:** "**Domain integrity**: values must satisfy the data type/domain. **Entity integrity**: primary key values cannot be NULL and must uniquely identify tuples. **Referential integrity**: a foreign key must refer to an existing referenced key, or be NULL where permitted."
- **Plain:** the DB refuses bad data itself.

### Modification anomalies
- **Memory:** I-U-D.
- **Exam-ready:** "**Insertion anomaly**: a fact cannot be inserted without also inserting an unrelated fact. **Update anomaly**: the same fact is repeated in many rows, so one logical change needs many updates. **Deletion anomaly**: deleting one fact accidentally removes another fact that should have been retained."
- **Plain:** bad design makes ordinary edits dangerous.

---

## UNIT 2 — Normalization, Storage & Indexing

### Functional dependency (FD)  ← *exact*
- **Memory:** X → Y = X determines Y; X is the determinant.
- **Exam-ready:** "A functional dependency X → Y means that whenever two tuples agree on all attributes of X, they must also agree on all attributes of Y. X is the determinant and Y is functionally dependent on X."
- **Plain:** knowing X pins down Y.

### Trivial / Non-trivial / Partial / Transitive / Full dependency
- **Memory:** Trivial Y⊆X · Non-trivial Y⊄X · Partial Y depends on part of a *composite* key · Transitive X→Y→Z ⇒ X→Z · Full Y needs *all* of X.
- **Exam-ready:** "A trivial FD has Y ⊆ X; a non-trivial FD does not. A partial dependency means Y depends on a proper subset of a composite key. A transitive dependency arises when X → Y and Y → Z imply X → Z."
- **Plain:** which slice of the key actually matters.

### Attribute closure X⁺
- **Memory:** start with X → keep adding RHS of FDs whose LHS is already inside → stop → superkey if it covers all attributes.
- **Exam-ready:** "The closure X⁺ is the set of all attributes functionally determined by X under a set of FDs. If X⁺ contains every attribute of the relation, X is a super key."
- **Plain:** everything X can unlock.

### Normalization
- **Memory:** organize by dependencies to kill redundancy/anomalies while preserving dependencies.
- **Exam-ready:** "Normalization is the systematic process of organizing relations using functional dependencies and decomposition so that redundancy and modification anomalies are reduced while important relationships and dependencies are preserved."
- **Plain:** split big tables so nothing is repeated.

### First Normal Form (1NF) ← *exact*
- **Memory:** atomic values; no repeating groups.
- **Exam-ready:** "A relation is in First Normal Form when each attribute contains atomic values and there are no repeating groups or nested sets stored inside a single field."
- **Plain:** one value per cell.

### Second Normal Form (2NF) ← *exact*
- **Memory:** 1NF + no partial dependency.
- **Exam-ready:** "A relation is in 2NF if it is already in 1NF and every non-prime attribute is fully functionally dependent on the entire candidate key."
- **Plain:** every non-key column needs the *whole* key.

### Third Normal Form (3NF) ← *exact*
- **Memory:** 2NF + no transitive dependency; **OR** rule.
- **Exam-ready:** "A relation is in 3NF if it is in 2NF and contains no undesirable transitive dependency of non-prime attributes on a key: for every non-trivial FD X → A, X is a super key **or** A is a prime attribute."
- **Plain:** non-key columns depend on the key, nothing but the key.

### Boyce–Codd Normal Form (BCNF) ← *exact*
- **Memory:** every determinant is a super key; **ONLY** rule.
- **Exam-ready:** "A relation is in BCNF if for every non-trivial functional dependency X → Y, X is a super key. Every determinant must be a super key."
- **Plain:** stricter than 3NF — no exceptions for prime attributes.

### Multivalued dependency (MVD) & 4NF
- **Memory:** two *independent* multivalued facts ⇒ 4NF splits them.
- **Exam-ready:** "A multivalued dependency X ↠ Y occurs when, for each value of X, the set of Y values is independent of the remaining attributes. 4NF requires every non-trivial MVD X ↠ Y to have X as a super key."
- **Plain:** hobbies don't depend on languages.

### Join dependency (JD) & 5NF
- **Memory:** reconstruct by joining projections; JD implied by candidate keys.
- **Exam-ready:** "A join dependency states that a relation can be reconstructed by joining several projections. A relation is in 5NF when every non-trivial join dependency is implied by candidate keys."
- **Plain:** splitting further never loses or fakes rows.

### Lossless join decomposition
- **Memory:** pieces rebuild the exact picture — no lost, no spurious tuples.
- **Exam-ready:** "A decomposition is lossless if joining the decomposed relations produces exactly the original relation — it neither loses valid information nor creates spurious tuples."
- **Plain:** tear it apart, tape it back, identical.

### Dependency preservation
- **Memory:** rules checkable locally, without joins.
- **Exam-ready:** "A decomposition is dependency preserving if the original functional dependencies can be enforced by enforcing dependencies on the decomposed relations individually, without requiring joins."
- **Plain:** you can still validate every rule from the split tables.

### Minimal (canonical) cover
- **Memory:** S-E-R: Split RHS → Extraneous LHS → Remove redundant FDs.
- **Exam-ready:** "A minimal cover is an equivalent, simplified set of functional dependencies with no extraneous attributes and no redundant dependencies; two sets F and G are equivalent when F⁺ = G⁺."
- **Plain:** the same rules, shortest form.

### B+ tree index
- **Memory:** internal = separators + child pointers; leaves = keys + record pointers, **linked**.
- **Exam-ready:** "A B+ tree is a balanced multiway search tree whose internal nodes contain separator keys and child pointers, and whose leaf nodes contain search keys and record/data references; leaves are linked, which makes range scanning efficient."
- **Plain:** a directory whose last page points to the next page.

### Hash index / collision
- **Memory:** key → hash → bucket → records; collision = same bucket.
- **Exam-ready:** "A hash index applies a hash function to a search key and maps it to a bucket; if two keys map to the same bucket a collision occurs, handled by overflow buckets, chaining or dynamic hashing."
- **Plain:** exact-address lookup, no order.

### Buffer pool / page (block)
- **Memory:** I/O moves pages, not records.
- **Exam-ready:** "Data is transferred between secondary storage and memory in pages or blocks; the buffer manager brings pages into memory and writes modified pages back, so reducing page I/O is a major optimization objective."
- **Plain:** the unit of disk traffic is the page.

---

## UNIT 3 — Transactions, Concurrency & Recovery

### Transaction ← *exact*
- **Memory:** logical unit of work that must preserve correctness; bank transfer anchor.
- **Exam-ready:** "A transaction is a sequence of database operations that forms one logical unit of work and must preserve database correctness even under concurrency or failure. A ₹500 transfer must either fully debit A and credit B, or have no effect at all."
- **Plain:** all-or-nothing unit of work.

### ACID ← *exact, one line each*
- **Memory:** Atomicity = both or neither · Consistency = valid state · Isolation = no half-visible transfers · Durability = survives restart.
- **Exam-ready:** "**Atomicity**: a transaction is all-or-nothing; if an essential operation fails the whole transaction is rolled back. **Consistency**: every committed transaction preserves integrity constraints and valid database rules. **Isolation**: intermediate effects of concurrent transactions are controlled so execution is equivalent to an acceptable serial behaviour. **Durability**: after commit, effects survive subsequent system failure, subject to the DBMS's durability guarantees."
- **Plain:** the four promises every transaction makes.

### Schedule / serial / serializable
- **Memory:** serial = one after another; serializable = interleaved but equivalent to *some* serial order.
- **Exam-ready:** "A serial schedule executes transactions one after another; a serializable schedule may interleave operations but produces an effect equivalent to some serial schedule."
- **Plain:** concurrency without changing the outcome.

### Conflict serializability
- **Memory:** build precedence graph → cycle ⇒ not serializable.
- **Exam-ready:** "Two operations conflict if they access the same item and at least one is a write. Add an edge Ti → Tj when a conflicting operation of Ti precedes that of Tj; if the precedence graph is acyclic the schedule is conflict-serializable."
- **Plain:** draw arrows, look for a loop.

### Deadlock
- **Memory:** T1 holds A waits B; T2 holds B waits A — cycle.
- **Exam-ready:** "Deadlock occurs when transactions wait in a cycle, each holding a resource the next one needs; it is handled by prevention, avoidance, detection (wait-for graph) or timeout."
- **Plain:** mutual waiting forever.

### Two-Phase Locking (2PL) ← *exact*
- **Memory:** GROWING → LOCK POINT → SHRINKING.
- **Exam-ready:** "Two-phase locking divides a transaction into a growing phase in which locks may be acquired but not released, and a shrinking phase in which locks may be released but no new locks acquired; basic 2PL guarantees conflict serializability."
- **Plain:** take all locks first, then let go.

### Strict 2PL / Rigorous 2PL
- **Memory:** Strict = hold **X** till commit/abort; Rigorous = hold **S and X** till completion.
- **Exam-ready:** "Strict 2PL holds exclusive locks until commit or abort, which reduces cascading rollbacks; rigorous 2PL holds both shared and exclusive locks until completion."
- **Plain:** never let go early.

### Timestamp ordering
- **Memory:** older = smaller timestamp; Read_TS / Write_TS; violation ⇒ abort+restart; no lock waits.
- **Exam-ready:** "Each transaction receives a unique timestamp; Read_TS(X) is the largest timestamp of a transaction that read X and Write_TS(X) the largest that wrote X. A read/write that would violate timestamp order causes the transaction to be rejected and restarted, so lock-based deadlock is avoided at the cost of wasted work."
- **Plain:** order by birth certificate instead of locks.

### Failure types
- **Memory:** Transaction · System crash · Media · Communication.
- **Exam-ready:** "Transaction failures (logical error, constraint violation, deadlock victim, explicit abort), system crashes (power/OS/DBMS process failure losing volatile memory), media failures (disk damage losing persistent data) and communication failures (important in distributed databases)."
- **Plain:** four ways it goes wrong.

### Deferred update
- **Memory:** delay data — nothing hits disk before COMMIT; crash ⇒ REDO committed only.
- **Exam-ready:** "In deferred update, database changes are not written until the transaction commits; log records allow committed changes to be reconstructed, so after a crash committed transactions may need REDO while uncommitted ones normally need no UNDO."
- **Plain:** buffer it all, write on commit.

### Immediate update
- **Memory:** data may already be on disk ⇒ UNDO uncommitted + REDO committed.
- **Exam-ready:** "In immediate update a modified page may be written before commit, so after a crash the system must UNDO changes of uncommitted transactions and REDO changes of committed transactions that may not have reached disk."
- **Plain:** write as you go, clean up afterwards.

### Shadow paging
- **Memory:** old safe book / new working book; COMMIT switches ROOT; crash ⇒ use SHADOW.
- **Exam-ready:** "Shadow paging maintains a stable shadow page table and a current page table; modified pages are written to new locations, and at commit the root pointer switches to the current table — a crash before commit simply reuses the shadow mapping."
- **Plain:** never overwrite the last good copy.

### Log / Write-Ahead Logging (WAL) / checkpoint
- **Memory:** **LOG FIRST, DATA SECOND**; checkpoint = recovery starting point.
- **Exam-ready:** "A log is a sequential record of transaction actions on stable storage (transaction ID, data item, old value, new value). The Write-Ahead Logging principle requires the relevant log record to reach stable storage *before* the corresponding data page is written. A checkpoint records recovery information at intervals so recovery can start from a recent point instead of scanning the whole log."
- **Plain:** write the diary before you move the furniture.

### Recovery
- **Memory:** restore consistency after failure; UNDO uncommitted, REDO committed.
- **Exam-ready:** "Recovery is the process of restoring the database to a consistent state after failure, using logs, checkpoints, backups and undo/redo techniques."
- **Plain:** roll back the broken, replay the promised.

---

## UNIT 4 — Distributed Databases & NoSQL

### Distributed database / DDBMS
- **Memory:** one logical DB, physically spread over network-connected sites.
- **Exam-ready:** "A distributed database is a logically integrated database whose data is physically distributed across multiple network-connected sites; a DDBMS coordinates these sites and gives users unified access."
- **Plain:** one database, many machines.

### Horizontal / Vertical / Hybrid fragmentation
- **Memory:** Horizontal = **rows** (by predicate) · Vertical = **columns** (+ repeat the PK) · Hybrid = both.
- **Exam-ready:** "Horizontal fragmentation divides rows by predicates; vertical fragmentation divides columns and normally repeats the primary key in each fragment so the relation can be reconstructed by a join; hybrid fragmentation combines both."
- **Plain:** split by rows, by columns, or both.

### Replication / Allocation
- **Memory:** copies at sites; full = all sites, partial = some; allocation = which site holds what.
- **Exam-ready:** "Replication means maintaining multiple copies of data at different sites — full or partial — improving availability and local reads at the cost of storage, update coordination and consistency management. Allocation decides which site stores which fragment/replica based on query frequency, locality, communication cost, storage capacity and reliability."
- **Plain:** copy everything everywhere, or decide carefully.

### Two-Phase Commit (2PC) ← *ordered process*
- **Memory:** ASK → VOTE → DECIDE (PREPARE → YES/NO → COMMIT/ABORT).
- **Exam-ready:** "In 2PC the coordinator sends PREPARE to all participants; each records a prepared state and votes YES/NO; if all required votes are YES the coordinator sends COMMIT, otherwise ABORT; participants then record and execute the decision. It guarantees atomic commitment but can block when a prepared participant cannot learn the final decision."
- **Plain:** everyone agrees before anyone acts.

### Consistency model
- **Memory:** strong/linearizable · eventual · causal · session (read-your-writes, monotonic reads).
- **Exam-ready:** "A consistency model defines what values and ordering guarantees clients can observe when data is replicated or distributed: strong/linearizable consistency orders operations in real time, eventual consistency lets replicas temporarily disagree and converge if updates stop, causal consistency preserves causal order, and session guarantees provide read-your-writes or monotonic reads."
- **Plain:** what a reader is allowed to see.

### CAP theorem ← *exact wording matters*
- **Memory:** under a **partition**, you trade **C** vs **A**. Never write "any two at all times".
- **Exam-ready:** "The CAP theorem states that when a distributed system experiences a network partition, it cannot simultaneously guarantee both strong consistency and availability for every request under the formal CAP definitions."
- **Plain:** when the network splits, pick what to preserve.
- **C** = a read observes the most recent write per the formal guarantee, or an error.
  **A** = every request to a non-failing node gets a non-error response (value need not be latest).
  **P** = the system keeps operating despite network failures between nodes.

### BASE
- **Memory:** Basically Available · Soft state · Eventual consistency.
- **Exam-ready:** "BASE stands for Basically Available, Soft state, Eventual consistency: the system may accept temporary inconsistency while providing high availability and eventual convergence under suitable conditions."
- **Plain:** available now, consistent later.

### Sharding
- **Memory:** horizontal distribution across nodes; range | hash | directory | geographic.
- **Exam-ready:** "Sharding is the horizontal distribution of records across multiple nodes, where each shard stores a subset of the dataset; a good shard key distributes data and traffic evenly, supports common queries and avoids hotspots."
- **Plain:** one big table split into slices on different machines.

### NoSQL
- **Memory:** non-relational, flexible schema, scalable/distributed workloads.
- **Exam-ready:** "NoSQL is a broad family of non-relational database technologies designed for flexible data models and scalable/distributed workloads."
- **Plain:** not-your-SQL databases.

### The four NoSQL models
- **Memory:** Document / Key-value / Column-family / Graph.
- **Exam-ready:** "**Document** stores JSON/BSON-like documents (catalogs, content, profiles); **key-value** maps keys to values (cache, sessions, lookups); **column-family** stores partitioned rows with flexible columns (large-scale distributed workloads); **graph** stores nodes, relationships and properties (social networks, recommendations, fraud)."

### Aggregation pipeline (MongoDB)
- **Memory:** $match → $group → $project → $sort → $limit (+ $skip, $unwind, $lookup).
- **Exam-ready:** "The aggregation framework processes documents through a sequence of pipeline stages; each stage transforms, filters, groups, sorts or joins data — for example $match filters, $group aggregates, $project shapes fields, $sort orders and $limit restricts."

---

## UNIT 5 — NoSQL Stores, Indexing & Ordering

### Cassandra data model rules ← *highest-yield Unit 5 definitions*
- **Memory:** **Partition key = WHERE data lives · Clustering columns = ORDER within partition.**
- **Exam-ready:** "In Cassandra the partition key determines which node/partition a row is stored in, while clustering columns define the order of rows within each partition; tables should be modelled around query patterns and deliberate duplication is common so joins are avoided."

### HBase vs Cassandra
- **Memory:** HBase = Hadoop ecosystem, row key + column families, APIs/shell · Cassandra = independent, partition key + clustering, CQL, high availability/writes.

### Redis
- **Memory:** in-memory key-value; caching, sessions, counters, queues, leaderboards, TTL.
- **Exam-ready:** "Redis is an in-memory data store supporting key-value access and richer data structures, commonly used for caching, sessions, counters, queues, leaderboards and fast temporary state (SET/GET/DEL/EXISTS, HSET/HGET, EXPIRE, INCR)."

### Graph database
- **Memory:** Nodes = entities · Edges = relationships · Properties = attributes.
- **Exam-ready:** "A graph database represents data as a network of nodes (entities), relationships (edges) and properties (attributes), and is suitable when queries depend on traversing relationships."

### Vector embedding ← *exact*
- **Memory:** object → numerical vector; similar objects near each other.
- **Exam-ready:** "An embedding is a numerical vector representation of an object produced by an embedding model; the model attempts to place semantically similar objects near each other in vector space."
- **Plain:** meaning turned into coordinates.

### Vector similarity search ← *exact*
- **Memory:** query → embed → index → top-k → results.
- **Exam-ready:** "Vector similarity search retrieves the stored vectors closest to a query vector according to a chosen similarity or distance measure — cosine similarity (angle), Euclidean distance (straight line) or dot product (alignment and magnitude)."

### ANN / HNSW / IVF
- **Memory:** brute force = all vectors · ANN = promising region only · HNSW = **graph** · IVF = **clusters**.
- **Exam-ready:** "Approximate nearest-neighbour indexes trade a little recall for much lower latency: HNSW is a graph-based hierarchical navigable small-world structure that walks through increasingly close candidates, while IVF partitions vectors into clusters and searches only relevant groups."

### Index ← *exact*
- **Memory:** auxiliary access path; faster reads ↔ storage + maintenance cost.
- **Exam-ready:** "An index is an auxiliary data structure that creates an efficient access path to data, improving lookup performance at the cost of storage and maintenance."
- **Plain:** a lookup table for your table.

### Compound index field order
- **Memory:** order matters — it decides which query/sort patterns the index can serve.
- **Exam-ready:** "In a compound index the order of fields determines which query and sort patterns the index can support efficiently; query plans can be inspected with explain()."

### Ordering
- **Memory:** B+ tree = ordered (equality, range, prefix, sorted retrieval) · hash = unordered (poor for ranges).
