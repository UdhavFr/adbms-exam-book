# comparisons.md — Contrast Pairs (Tables = Marks)

Examiners award marks per correct *row*. Memorise the **contrast**, not the paragraph.
Rows marked **derived** are assembled from source facts (not new material).

---

## C1. File system vs DBMS

| Feature | File-processing system | DBMS |
|---|---|---|
| Redundancy | duplicated across app files | centralized/shared design reduces it |
| Inconsistency | copies drift apart | constraints + controlled updates |
| Sharing | hard (app-owned files) | multiple users/applications share one DB |
| Security | ad hoc per app | authentication + authorization |
| Concurrent access | uncoordinated | concurrency-control mechanisms |
| Recovery | manual/limited | logging, checkpoints, restore |
| Program-data dependence | data embedded in programs | data abstraction + data independence |

---

## C2. Schema vs Instance

| Aspect | Schema | Instance |
|---|---|---|
| Meaning | design / logical structure | actual contents at a moment |
| Change frequency | relatively infrequent | changes frequently |
| Example | `STUDENT(RollNo, Name, Course)` | `(101, Ravi, MCA)` |
| Analogy | blueprint | current building |

---

## C3. Physical vs Logical data independence

| Type | What can change | What must NOT change | Example |
|---|---|---|---|
| Physical | storage structures (files, indexes, pages) | conceptual schema | add/change an index |
| Logical | conceptual schema | required external views/apps | split a table, keep a compatible view |

---

## C4. Keys

| Key | Definition | Test |
|---|---|---|
| Super key | any attribute set that uniquely identifies a tuple | uniqueness only |
| Candidate key | **minimal** super key | remove any attribute ⇒ uniqueness breaks |
| Primary key | the chosen candidate key | one per relation |
| Alternate key | a candidate key not chosen | still valid identifier |
| Foreign key | attribute(s) referencing a key in another relation | must match a referenced key (or NULL if allowed) |

---

## C5. Cardinality ratios (ER) — plus the terminology trap

| Ratio | Meaning | Anchor example |
|---|---|---|
| 1:1 | one entity ↔ at most one on the other side | Person–Passport |
| 1:N | one ↔ many | Department–Employee |
| M:N | many ↔ many | Student–Course |

⚠ **Cardinality of a relation = number of tuples** (different meaning — errata E1). Degree = number of attributes.

---

## C6. Participation

| | Total | Partial |
|---|---|---|
| Meaning | every entity participates | participation optional |
| Drawing | double line | single line |
| Example | each student must enrol somewhere | some employees are not on a project |

---

## C7. SQL sub-languages

| Category | Purpose | Commands |
|---|---|---|
| DDL | define/modify structure | CREATE, ALTER, DROP, TRUNCATE |
| DML | retrieve/change data | SELECT, INSERT, UPDATE, DELETE |
| DCL | privileges/security | GRANT, REVOKE |
| TCL | transaction control | COMMIT, ROLLBACK, SAVEPOINT |

**Hook:** DDL=Design · DML=Manipulate · DCL=Control access · TCL=Transaction.

---

## C8. Modification anomalies

| Anomaly | One line |
|---|---|
| Insertion | cannot insert a fact without an unrelated fact |
| Update | one logical change requires many updates |
| Deletion | deleting a fact accidentally deletes another fact |

---

## C9. The normal-form ladder (the single most examinable table)

| NF | Fixed by | Defining rule | Canonical example |
|---|---|---|---|
| 1NF | atomic values | no repeating groups / nested sets | STUDENT(…, Phones) → STUDENT_PHONE |
| 2NF | remove **partial** dependency | non-prime depends on the **whole** key | ENROLL(StudentID, CourseID, StudentName, CourseName, Grade) |
| 3NF | remove **transitive** dependency | X→A allowed if **X super key OR A prime** | EMPLOYEE(EmpID, DeptID, DeptName) |
| BCNF | remove non-key determinants | **every determinant is a super key** | stricter than 3NF |
| 4NF | remove independent MVDs | non-trivial MVD ⇒ determinant is a super key | STUDENT(Student, Hobby, Language) |
| 5NF | remove join-dependency redundancy | non-trivial JD implied by candidate keys | lossless reconstruction by projections |

**One-line memory:** 1=Atomic · 2=Partial · 3=Transitive · BC=Determinant · 4=MVD · 5=Join.

---

## C10. 3NF vs BCNF ← *classic 5/10-mark question*

| Feature | 3NF | BCNF |
|---|---|---|
| Condition for X → A | X is a super key **OR** A is prime | X **must be** a super key |
| Restrictive? | less restrictive | more restrictive |
| Dependency preservation | usually preserved (a lossless, dependency-preserving decomposition always exists) | may be lost |
| Practical role | common compromise | used when stronger redundancy removal is needed |
| Memory | **OR** | **ONLY** |

---

## C11. Lossless join vs Dependency preservation

| Property | Question it answers |
|---|---|
| Lossless join | Can I reconstruct the original relation **exactly**, with no spurious tuples? |
| Dependency preservation | Can I enforce the original dependencies **without joining**? |

**Puzzle memory:** lossless = pieces rebuild the exact picture · preserved = rules checked locally.
They are independent: one can hold without the other.

---

## C12. File organizations

| Organization | Description | Best for |
|---|---|---|
| Heap | unordered records | frequent inserts, full scans |
| Sequential/sorted | key order | ordered processing, range access |
| Hash | key → bucket via hash function | equality lookups |
| Clustered | related records close together | queries accessing related records together |

---

## C13. B+ tree vs Hash index ← *very frequently asked*

| Feature | B+ tree | Hash index |
|---|---|---|
| Structure | balanced ordered tree | unordered buckets |
| Workload | equality **+ range** | equality only |
| ORDER BY / range scan | good (linked leaves) | poor |
| Lookup path | root → internal → leaf → record | key → hash → bucket → records |
| Complexity | O(log_f N) | ~O(1) average for equality |
| Memory | "broad access" | "hit the exact key" |

---

## C14. Index: benefits vs costs

| Benefits | Costs |
|---|---|
| avoids full table/collection scans | extra storage |
| lower latency | write overhead (index maintenance) |
| supports selective filtering | memory/cache pressure |
| ordered index supports range + sorting | useless if the query doesn't match its shape |
| nearest-neighbour retrieval in vector systems | too many indexes slow write-heavy systems |
| reduces CPU/memory/disk I/O/network work | needs partition-aware design when distributed |

---

## C15. Transaction states

| State | Meaning |
|---|---|
| Active | executing |
| Partially committed | last statement executed; durability not yet final |
| Committed | completed successfully; effects durable |
| Failed | cannot continue |
| Aborted | effects rolled back → restart or terminate |

---

## C16. ACID ← *highest-value Unit 3 table*

| Property | Detailed meaning | Banking example |
|---|---|---|
| Atomicity | all-or-nothing; rollback if an essential operation fails | debit **and** credit both happen |
| Consistency | committed transactions preserve integrity rules | no invalid account state |
| Isolation | intermediate effects of concurrent transactions controlled ⇒ equivalent to acceptable serial behaviour | nobody sees a half-completed transfer |
| Durability | committed effects survive later system failure | transfer still there after restart |

---

## C17. Isolation levels + which anomaly each stops

| Level | Dirty read | Non-repeatable read | Phantom |
|---|---|---|---|
| Read Uncommitted | possible | possible | possible |
| Read Committed | prevented | possible | possible |
| Repeatable Read | prevented | prevented | DBMS-dependent (SQL standard: possible) |
| Serializable | prevented | prevented | prevented |

*(Source gives the "general idea" rows; matrix form per errata E4.)*

---

## C18. Concurrency anomalies

| Anomaly | One-line trigger | Story |
|---|---|---|
| Lost update | later write overwrites an earlier write | "my write vanished" |
| Dirty read | read a value written by an uncommitted transaction | "I read dirty data" |
| Non-repeatable read | same row read twice gives different committed values | "the row changed under me" |
| Phantom read | repeated predicate query returns a different row **set** | "new rows appeared" |

---

## C19. Serial vs Serializable · and 2PL variants

| | Meaning |
|---|---|
| Serial schedule | transactions run one after another |
| Serializable schedule | may interleave, but equivalent to **some** serial schedule |

| Variant | Rule | Guarantees |
|---|---|---|
| Basic 2PL | growing/shrinking phases | conflict serializability |
| Strict 2PL | hold **X** locks till commit/abort | fewer cascading rollbacks |
| Rigorous 2PL | hold **S and X** till completion | strongest lock holding |

---

## C20. Lock compatibility

| held \ req | S | X |
|---|---|---|
| S | ✅ | ❌ |
| X | ❌ | ❌ |

*S = Shares (read), X = eXcludes (write).*

---

## C21. Lock-based (2PL) vs Timestamp ordering

| Feature | 2PL | Timestamp ordering |
|---|---|---|
| Coordination | locks + phases | unique timestamps, order of operations |
| Waiting | may wait for locks | no waiting |
| Deadlock | possible (cycle) | lock-wait deadlock impossible |
| Cost | blocking / lower concurrency in contention | aborted work wasted on restarts |
| Correctness | conflict serializable | serializable by timestamp order |

---

## C22. Failure types

| Failure | Cause | What is lost |
|---|---|---|
| Transaction failure | logical error, constraint violation, deadlock victim, explicit abort | that transaction's progress |
| System crash | power / OS / DBMS process failure | volatile memory |
| Media failure | disk damage | persistent data on that media |
| Communication failure | network link failure (critical in distributed DBs) | messages between sites |

---

## C23. Deferred update vs Immediate update vs Shadow paging ← *favourite 10-marker*

| Feature | Deferred update | Immediate update | Shadow paging |
|---|---|---|---|
| When data pages are written | only **after** commit | may be written **before** commit | always to **new** pages |
| What the DB sees on crash | only committed changes | both committed & uncommitted changes | old consistent version |
| After crash | REDO committed if needed (normally **no UNDO**) | **UNDO** uncommitted + **REDO** committed | use SHADOW mapping |
| Extra structure | log records | log records | two page tables |
| Weakness | needs enough log to redo | needs undo/redo logic | fragmentation, page-table copy overhead |
| Memory | "delay the data" | "data may already be on disk" | "old safe book / new working book" |

---

## C24. Recovery mechanisms

| Mechanism | Idea |
|---|---|
| Logging | sequential record of actions: TID, item, old, new |
| WAL | log record to stable storage **before** the data page is written |
| Checkpoint | recovery starts from a recent point, not the whole log |
| Shadow paging | never overwrite the last consistent version |
| Undo/Redo | undo uncommitted, redo committed |

---

## C25. Homogeneous vs Heterogeneous vs Federated

| Type | Meaning |
|---|---|
| Homogeneous | similar DBMS technology across sites |
| Heterogeneous | different database technologies or schemas |
| Federated | independently managed databases cooperating through integration mechanisms |

---

## C26. Fragmentation types

| Type | Split | Reconstruction |
|---|---|---|
| Horizontal | **rows** by predicate | UNION of fragments |
| Vertical | **columns** (PK repeated in each) | JOIN on the key |
| Hybrid | horizontal then vertical | combination |

Properties: **completeness · reconstruction · disjointness** (where the strategy requires it).
**Hook:** Horizontal = Rows, Vertical = Columns.

---

## C27. Replication: benefits vs costs

| Benefits | Costs |
|---|---|
| higher availability | more storage |
| faster local reads | update coordination |
| failure tolerance | consistency management |
| reduced remote access | network/control overhead |

---

## C28. 2PL vs 2PC ← *derived (C) — do not confuse*

| Feature | 2PL (two-phase **locking**) | 2PC (two-phase **commit**) |
|---|---|---|
| Unit | a transaction inside **one** DBMS | a transaction across **multiple** sites |
| Purpose | concurrency control → serializability | atomic **commit** decision |
| Phases | growing / shrinking (locks) | prepare / commit-or-abort (votes) |
| Failure issue | deadlock | blocking when decision unreachable |
| Memory | *lock* phases | *vote* phases |

---

## C29. Consistency models

| Model | Guarantee |
|---|---|
| Strong / linearizable | operations appear in a single real-time-respecting order |
| Eventual | replicas may temporarily disagree, converge if updates stop |
| Causal | causally related operations keep their causal order |
| Session (read-your-writes, monotonic reads) | per-session sanity guarantees |

Trade-off: stronger consistency ⇒ more coordination ⇒ higher latency / lower availability during failures.

---

## C30. ACID vs BASE ← *very common 5-mark question*

| ACID | BASE |
|---|---|
| Atomicity, Consistency, Isolation, Durability | Basically Available, Soft state, Eventual consistency |
| strong transaction-oriented guarantees | availability + flexible consistency emphasis |
| traditional relational transaction systems | distributed NoSQL architectures/use cases |
| commit aims at durable consistent state | state may change as replicas converge |

BASE ≠ permanently wrong data: temporary inconsistency accepted, eventual convergence expected.

---

## C31. CAP — the exact framing

| Letter | Name | Meaning |
|---|---|---|
| C | Consistency | a read observes the most recent write **according to the formal guarantee**, or an error |
| A | Availability | every request to a non-failing node gets a non-error response (need not be the latest value) |
| P | Partition tolerance | the system continues despite network failures preventing node communication |

⚠ **During a network partition**, strong consistency and availability cannot both be guaranteed for every request.
**Never write:** "you can pick any two at all times."

---

## C32. Sharding strategies

| Strategy | Rule | Strength | Weakness |
|---|---|---|---|
| Range | key ranges → shards | good range queries | hotspots at the edge |
| Hash | hash(shard key) | even distribution | loses range locality |
| Directory | mapping service per key | flexible | extra lookup service |
| Geographic | assign by region | locality/compliance | uneven data volumes |

Good shard key: even data+traffic, supports common queries, no oversized partitions/hotspots.

---

## C33. NoSQL data models

| Type | Data representation | Typical applications |
|---|---|---|
| Document | JSON/BSON-like documents | catalogs, content, profiles |
| Key-value | key → value | cache, sessions, simple lookups |
| Column-family | partitioned rows + flexible columns | large-scale distributed workloads |
| Graph | nodes + relationships + properties | social networks, recommendations, fraud |

---

## C34. Relational vs MongoDB vocabulary

| Relational concept | MongoDB |
|---|---|
| Database | Database |
| Table | Collection |
| Row | Document |
| Column | Field |
| Primary key | `_id` |

---

## C35. HBase vs Cassandra ← *Unit 5 comparison table*

| HBase | Cassandra |
|---|---|
| strong Hadoop ecosystem relationship | independent distributed wide-column system |
| row key + column families | **partition key + clustering columns** |
| HBase APIs / shell | **CQL** (SQL-like) |
| large-scale sparse data, random read/write | high availability, horizontal scalability, high write throughput |

---

## C36. Traditional index vs Vector index

| Traditional database index | Vector index |
|---|---|
| exact / range-oriented access | similarity / nearest-neighbour access |
| B+ tree or hash | HNSW, IVF and related ANN structures |
| `age = 22`, `price BETWEEN 100 AND 200` | top-k vectors closest to a query embedding |
| ordered keys or buckets | geometric / graph / cluster structure |

---

## C37. Brute-force vs ANN search

| Brute force | ANN |
|---|---|
| compare query with **every** stored vector | search a smaller, promising region |
| exact | approximate (small recall trade-off) |
| cost grows linearly with N | much lower latency at scale |
| — | HNSW = navigable **graph**; IVF = **clusters** |

---

## C38. Cosine vs Euclidean vs Dot product

| Measure | Idea | Use when |
|---|---|---|
| Cosine similarity | angle/direction between vectors | semantic text retrieval (magnitude irrelevant) |
| Euclidean distance | straight-line distance between points | magnitude matters, geometric closeness |
| Dot product | alignment **and** magnitude | retrieval systems weighting vector length |

---

## C39. Relational design vs Cassandra design philosophy *(derived)*

| Relational | Cassandra |
|---|---|
| normalize to remove redundancy | deliberately **duplicate** to avoid joins |
| design tables around entities | design tables around **query patterns** |
| joins at query time | single-partition reads |
| secondary indexes freely | partition/clustering key design first; indexing secondary |
