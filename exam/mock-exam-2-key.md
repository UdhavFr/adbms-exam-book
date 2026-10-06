# MOCK EXAM 2 — Answer Key

## Section A
**A1.** *Entity integrity*: a primary key cannot be NULL and must uniquely identify each tuple — e.g. `StudentID INT PRIMARY KEY`. *Referential integrity*: a foreign key must refer to an existing referenced key, or be NULL where permitted — e.g. `FOREIGN KEY(CourseID) REFERENCES Course(CourseID)`. Mentioning UNIQUE/CHECK/NOT NULL as extras is fine.
**A2.** **2NF** is violated: the key is composite (StudentID, CourseID) and StudentName depends only on StudentID — a partial dependency. Decomposition: `STUDENT(StudentID, StudentName)`, `COURSE(CourseID, …)` (if CourseName exists), `ENROLL(StudentID, CourseID, Grade)`.
**A3.** Transaction failure (logical error, constraint violation, deadlock victim, explicit abort) · System crash (power/OS/DBMS process failure — loses volatile memory) · Media failure (disk damage — loses persistent data) · Communication failure (link/message failure, important in distributed databases).
**A4.** A **fragment** is a *part* of a relation (horizontal = rows, vertical = columns + repeated key). A **replica** is a *copy* of a fragment/relation held at another site. Fragmentation = split; replication = duplicate.
**A5.** Create: `insertOne()`/`insertMany()`; Read: `find()`/`findOne()`; Update: `updateOne()`/`updateMany()`; Delete: `deleteOne()`/`deleteMany()`. Example: `db.students.find({age:{$gt:21}})`.

## Section B
**B1.** Composite attribute → store individual components, not the composite. Multivalued attribute → separate relation containing the owner's PK and the multivalued value. 1:1 → PK of one side as FK in the other (preferably the total-participation side), relationship attributes may go there. 1:N → PK of the 1-side becomes FK on the **N-side**. M:N → new relation containing both PKs (usually a composite PK). Weak entity → relation with its attributes plus the owner's PK (owner key + partial key identifies it).
**B2.** Use ENROLL(StudentID, CourseID, StudentName, CourseName, Grade): **1NF** removes any non-atomic/repeating values (atomic cells). **2NF** removes partial dependencies — StudentName ∤ (StudentID,CourseID) fully → split STUDENT/COURSE/ENROLL. **3NF** removes transitive dependencies (if the relation had EmpID→DeptID→DeptName) — non-prime attributes depend only on the key. Definitions should be quoted exactly: atomic · fully dependent on the entire candidate key · X super key OR A prime.
**B3.** A precedence (serialization) graph has one node per transaction. For every pair of conflicting operations — same data item, at least one a write, different transactions — where Ti's operation occurs before Tj's, add edge Ti → Tj. If the graph is **acyclic**, the schedule is conflict-serializable (a topological order gives an equivalent serial order); if it contains a **cycle**, it is not.
**B4.** Locks: S = shared/read (compatible with S), X = exclusive/write (conflicts with S and X). 2PL: **growing** phase acquires locks and releases none; the **lock point** is the last acquisition; **shrinking** phase releases locks and acquires none. Basic 2PL guarantees conflict serializability. **Strict 2PL** holds X locks until commit/abort (reduces cascading rollbacks). **Rigorous 2PL** holds both S and X locks until completion.
**B5.** Benefits: higher availability, faster local reads, failure tolerance, reduced remote access. Costs: more storage, update coordination, consistency management, network/control overhead. Allocation = deciding which site stores which fragment/replica, based on query frequency, data locality, communication cost, storage capacity and reliability.
**B6.** ACID = Atomicity, Consistency, Isolation, Durability — strong transaction-oriented guarantees, typical of relational transaction systems; commit aims at a durable consistent state. BASE = Basically Available, Soft state, Eventual consistency — availability and flexible consistency emphasis, common in distributed NoSQL; state may change as replicas converge. BASE does not mean permanently wrong data — temporary inconsistency is accepted with eventual convergence.
**B7.** **Range**: key ranges assigned to shards — good for range queries, risk of hotspots. **Hash**: hash(shard key) chooses the shard — even distribution, weakens range locality. **Directory**: a mapping service tells the system where each key lives — flexible, adds a lookup service. **Geographic**: records assigned by region — locality/compliance, uneven volumes. Plus: a good shard key distributes data/traffic evenly, supports common queries, avoids oversized partitions/hotspots.
**B8.** Document (JSON/BSON documents — catalogs, content, profiles) · Key-value (key → value — cache, sessions, simple lookups) · Column-family (partitioned rows + flexible columns — large-scale distributed workloads) · Graph (nodes + relationships + properties — social networks, recommendations, fraud).

## Section C
**C1.**
1. Closure: A⁺ starts {A}; A→B ⇒ {A,B}; B→C ⇒ {A,B,C}; C→D ⇒ **{A,B,C,D}**.
2. A⁺ = all attributes ⇒ **A is a super key**; A alone is minimal ⇒ **A is the candidate key**.
3. Prime attribute: A. Non-prime: B, C, D.
4. **1NF** ✓ (atomic assumed) and **2NF** ✓ (single-attribute key ⇒ no partial dependency possible).
5. **3NF violated**: B → C is a non-trivial FD where B is not a super key (B⁺ = {B,C,D}) and C is not prime ⇒ transitive dependency A → C (and A → D). Likewise C → D.
6. **BCNF also violated** for the same reason (every determinant must be a super key; B and C are not).
7. Lossless decomposition (chain): R1(A,B), R2(B,C), R3(C,D) — each intersection (B, then C) determines one side.

**C2.**
- **Log**: sequential record on stable storage containing transaction ID, data item, old value, new value — e.g. `<T1 START> <T1, A, 100, 50> <T1 COMMIT>`.
- **WAL**: the relevant log record must be written to stable storage **before** the corresponding data page is written, guaranteeing recovery has the information to undo or redo.
- **Checkpoint**: recovery information recorded at intervals so recovery starts from the recent checkpoint instead of scanning the entire log (shorter recovery time).
- **After a crash**: start from the last checkpoint → T1 committed ⇒ **REDO** its updates if they did not reach disk → T2 uncommitted ⇒ **UNDO** any of its changes that did → database consistent.
- **Diagram**: LOG → CHECKPOINT → CRASH → (REDO committed / UNDO uncommitted).

**C3.**
```js
db.sales.aggregate([
  {$match:{status:'paid'}},                       // filter first
  {$group:{_id:'$product', total:{$sum:'$amount'}}},
  {$sort:{total:-1}}
])
```
Explanation: filters paid sales, groups by product, sums the amount, sorts by total descending. Stages: $match filter · $group aggregate · $project shape fields · $sort order · $limit restrict (also $skip, $unwind, $lookup).
**Index helps**: equality/filter fields used repeatedly (`status`, `product`), sort fields (compound index with matching order), high-volume collections avoiding full scans.
**Index does not help**: write-heavy workloads where maintenance cost dominates; queries whose predicate/sort doesn't match the index structure (compound field order matters); low-selectivity predicates returning most documents; and indexes don't apply to aggregation stages that must process every document anyway (e.g. certain $group computations).

## Section D (20 marks) — marking stages
1. Define distributed database/DDBMS (logically integrated, physically distributed) — 2
2. **Fragmentation**: horizontal (rows/predicates), vertical (columns + PK repeated), hybrid; completeness/reconstruction/disjointness — 3
3. **Replication** benefits vs costs + allocation definition/criteria — 3
4. **2PC**: coordinator PREPARE → participants vote YES/NO → COMMIT/ABORT; diagram; blocking limitation — 3
5. **CAP**: exact statement + C/A/P definitions + "during a partition" framing (never "any two at all times") — 4
6. **Sharding**: horizontal distribution + four strategies with trade-offs — 2
7. **ACID vs BASE** relation to CAP: strong consistency costs availability/latency during partitions — 2
8. Diagrams (architecture/2PC/CAP) + conclusion on design trade-offs — 1
*(Capped at 20.)*

**Bonus (vector):** embedding definition → pipeline (data → model → vector → vector DB → similarity index) → cosine/Euclidean/dot → similarity search flow → brute force vs ANN → HNSW (graph) and IVF (clusters) → recall/latency trade-off.
