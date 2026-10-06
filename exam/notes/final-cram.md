# final-cram.md — THE LAST-MINUTE SHEET
Read top to bottom. Everything here is P0 or essential P1. If you know every line, you can answer almost anything.
Source: `ADBMS_MasterNotes.docx` · exact wording: `definitions.md` · traps: `common-mistakes.md` · hooks: `memory-hooks.md`

---

# 0. THE SIX ANSWER MOVES (apply to every long question)
**DEFINE (source wording) → DRAW (labelled diagram) → COMPONENTS (headings) → EXAMPLE → ADVANTAGES/LIMITATIONS → CONCLUDE (correctness/performance/scalability/reliability).**
Marks by length: 2 = one definition line · 5 = def + 4 points + example · 10 = def + diagram + headings + example + pro/con + conclusion · 20 = full plan (25–30 min).

---

# 1. DEFINITIONS YOU MUST SAY VERBATIM
| Term | Sentence |
|---|---|
| **DBMS** | Software that provides facilities for defining, storing, retrieving, updating, securing and recovering data in a database. |
| **Schema** | Overall logical description/blueprint of the database; relatively stable. |
| **Instance** | Collection of actual data stored at a particular point in time. |
| **Data independence (physical)** | Change physical storage structures without changing the conceptual schema. |
| **Data independence (logical)** | Modify the conceptual schema without changing every external view/application, when required external information can still be provided. |
| **Functional dependency** | X → Y: whenever two tuples agree on all attributes of X they must also agree on all attributes of Y. |
| **1NF** | Each attribute contains atomic values; no repeating groups/nested sets. |
| **2NF** | In 1NF and every non-prime attribute is fully dependent on the entire candidate key. |
| **3NF** | In 2NF and for every non-trivial X → A, X is a super key **or** A is a prime attribute. |
| **BCNF** | For every non-trivial X → Y, X is a super key — every determinant is a super key. |
| **4NF** | Every non-trivial multivalued dependency has a super key determinant. |
| **5NF** | Every non-trivial join dependency is implied by candidate keys. |
| **Lossless join** | Joining the decomposed relations reconstructs exactly the original relation. |
| **Dependency preservation** | Original FDs enforceable on the parts individually, without joins. |
| **Transaction** | Logical unit of database work that must preserve correctness under concurrency and failure. |
| **Serializability** | A schedule whose effect is equivalent to some serial execution of its transactions. |
| **2PL** | Growing phase acquires locks (no releases); shrinking phase releases locks (no new acquisitions). |
| **WAL** | The log record must reach stable storage before the corresponding data page is written. |
| **Distributed database** | One logically integrated database physically distributed across network-connected sites. |
| **CAP** | During a network partition, a system cannot guarantee both strong consistency and availability for every request under the formal CAP definitions. |
| **Sharding** | Horizontal distribution of records across multiple nodes. |
| **NoSQL** | Non-relational database family for flexible data models and scalable/distributed workloads. |
| **Embedding** | Numerical vector representation of an object produced by an embedding model. |
| **Vector similarity search** | Retrieve stored vectors closest to a query vector using a chosen similarity/distance measure. |
| **Index** | Auxiliary access structure improving lookup performance at the cost of storage and maintenance. |

---

# 2. FORMULAS / RULES (trigger → result)
- **Closure:** loop adding RHS of FDs whose LHS ⊆ current set; **X⁺ = all attributes ⇒ super key**. Ex: {A→B,B→C,C→D} ⇒ A⁺ = {A,B,C,D}.
- **NF criteria:** 1 atomic · 2 no partial · 3 (X super key **or** A prime) · BC every determinant a super key · 4 MVD determinant a super key · 5 JD implied by keys.
- **Prime** = in some candidate key; **non-prime** = in none.
- **Lossless test:** (R1∩R2) → R1 **or** → R2. Ex: R(A,B,C)/R1(A,B)/R2(A,C): A→B or A→C.
- **Minimal cover:** Split RHS → Extraneous LHS → Remove redundant FDs (**S-E-R**) · F ≡ G iff F⁺ = G⁺.
- **B+ tree:** O(log_f N); internal = separators+pointers; leaves linked ⇒ **range scans**.
- **SQL order:** FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT.
- **Lock compatibility:** only **S + S** works; X conflicts with everything.
- **2PL:** GROWING → LOCK POINT → SHRINKING · strict = X until commit · rigorous = S+X until completion.
- **Recovery:** committed → **REDO** · uncommitted → **UNDO** · deferred ⇒ no UNDO of data pages · immediate ⇒ both.
- **2PC:** PREPARE → VOTE (YES/NO) → COMMIT if all YES else ABORT · can block.
- **CAP:** only meaningful **during a partition**.
- **Cassandra:** partition key = WHERE · clustering columns = ORDER.
- **Vector:** cosine = angle · Euclidean = distance · dot = alignment+magnitude · HNSW = graph · IVF = clusters.

---

# 3. PROCESSES (chains — order = marks)
1. **ER→relational:** Entity→table · Composite→split · Multi→new table · 1:1→FK · **1:N→FK on N** · M:N→new table · Weak→owner+partial.
2. **Normalization problem:** FDs → candidate key (closure) → prime/non-prime → 1NF → 2NF → 3NF → BCNF → 4NF → 5NF → decompose → verify lossless (+preserving).
3. **Closure:** Start → Unlock → Add → Repeat → Complete.
4. **B+ search:** Root → Compare → Child → Leaf → Record (+ link-walk for ranges).
5. **Conflict serializability:** graph per txn → edges for conflicts (same item, ≥1 write, Ti first) → **acyclic = OK / cycle = NOT**.
6. **2PL:** acquire-all → lock point → release-all.
7. **Recovery:** log (log-before-data) → checkpoint → crash → undo uncommitted → redo committed.
8. **2PC:** ask → vote → decide.
9. **Fragmentation:** rows → columns (+key) → allocate → replicate.
10. **Aggregation:** $match → $group → $project → $sort → $limit.
11. **Vector search:** query → embed → index → top-k → results.
12. **20-mark writing:** define → draw → explain → example → compare → conclude.

---

# 4. COMPARISONS (one table = 5 marks)

| Pair | Left | Right |
|---|---|---|
| Schema / Instance | blueprint | contents now |
| Physical / Logical independence | storage changes | conceptual changes |
| 3NF / BCNF | **OR** (super key or prime) | **ONLY** (super key) |
| Lossless / Preserving | rebuilds exactly | enforceable without joins |
| B+ / Hash | ordered, equality+range, ORDER BY | unordered, equality only |
| Serial / Serializable | no interleave | interleaved but equivalent |
| 2PL / 2PC | locking (concurrency, one DBMS) | commit (atomicity, many sites) |
| Strict / Rigorous 2PL | X locks till commit | S and X till completion |
| Deferred / Immediate | write only after commit | may write before commit |
| Lost / Dirty | write overwritten | read uncommitted |
| Non-repeatable / Phantom | same row differs | row **set** differs |
| Fragment / Replica | a part | a copy |
| Horizontal / Vertical | rows | columns (+PK) |
| Sharding / Replication | split across nodes | copies across nodes |
| ACID / BASE | strong transactions | availability + eventual consistency |
| HBase / Cassandra | Hadoop ecosystem, row key+families, shell/API | independent, partition+clustering, CQL |
| Traditional / Vector index | exact/range on scalar keys | similarity/top-k on vectors |
| Cosine / Euclidean / Dot | angle | straight line / alignment+magnitude |

**Anomalies:** insertion (unrelated fact needed) · update (many rows to change) · deletion (loses another fact).
**Isolation levels:** RU (dirty possible) → RC (dirty prevented) → RR (repeatable; phantoms DBMS-dependent) → S (all prevented).
**Failure types:** transaction · crash (volatile lost) · media (persistent lost) · communication (distributed).

---

# 5. TRAPS THAT LOSE MARKS
1. **CAP** — never "pick any two at all times" → say **"during a network partition…"**.
2. **3NF/BCNF** — 3NF = OR, BCNF = ONLY.
3. **σ/π** — selection = rows, projection = columns.
4. **1:N mapping** — FK on the **N-side**.
5. **WAL** — **log before data**.
6. **Lossless test** — direction (intersection → one side).
7. **Deferred update** — uncommitted work needs **no UNDO**.
8. **Serializable ≠ serial**.
9. **Deadlock** — 2PL does *not* prevent it (PADT).
10. **RR & phantoms** — say "varies by DBMS; standard guarantees it only at Serializable".
11. **Cardinality** — ER ratio (1:1/1:N/M:N) vs relation rows (errata E1): say which you mean.
12. **Cassandra** — partition = location, clustering = order; duplication is *intentional*.
13. **Compound index** — field order matters; check with `explain()`.
14. **Hash** — never recommend for range/ORDER BY.
15. **HNSW vs IVF** — graph vs clusters (don't swap).
16. **NoSQL = schemaless?** No — Cassandra has explicit schemas.
17. **Index question** — always state the **cost** (storage + write maintenance).
18. **20-mark answers** — no diagram, no example, no conclusion = lost marks.

---

# 6. MEMORY HOOKS (5-minute blast)
- Whole subject: **DESIGN** (ER→relational→FD→normalization→indexing) · **RELIABILITY** (transaction→ACID→concurrency→serializability→2PL→recovery) · **DISTRIBUTION** (fragment/replicate→2PC→CAP→NoSQL→sharding) · **NoSQL stores**.
- DBMS functions = **D-S-R-U-S-R** · Levels = **E-C-I** · Independence = **P**hysical/Pages, **L**ogical.
- Normalization = **A-P-T-D-M-J** (Atomic, Partial, Transitive, Determinant, Multivalued, Join).
- Minimal cover = **S-E-R** · Deadlock = **PADT** · 2PC = **ASK→VOTE→DECIDE**.
- Locks: **S = Shares, X = eXcludes** · Integrity: **D-E-R + U-C-N** · Anomalies: **I-U-D**.
- Cassandra: **Partition = Place, Clustering = Order** · Graph: **Nodes/Edges/Properties = entities/relationships/attributes**.
- Redis: key → hash → time → counter · Pipeline: **match-group-project-sort-limit** · Cypher: **Create→Find→Filter→Modify→Destroy**.
- Vector: **Query→Embedding→Index→Top-K** · ANN: **HNSW = graph, IVF = clusters**.
- Bank story for ACID: both-or-neither · valid state · no half-transfer seen · still there after restart.
- Shadow paging = **old safe book / new working book** · WAL = **diary before moving furniture**.

---

# 7. MUST-USE EXAM KEYWORDS (sprinkle these; examiners grep for them)
`atomic values` · `non-prime attribute` · `candidate key` · `determinant` · `super key` · `partial dependency` · `transitive dependency` · `multivalued dependency` · `join dependency` · `lossless join` · `dependency preservation` · `attribute closure` · `page I/O` · `linked leaves` · `fan-out` · `all-or-nothing` · `integrity constraints` · `serial-equivalent` · `precedence graph` · `lock point` · `cascading rollback` · `wait-for graph` · `stable storage` · `checkpoint` · `UNDO/REDO` · `logically integrated / physically distributed` · `atomic commitment` · `blocking` · `eventual convergence` · `partition key` · `clustering columns` · `query patterns` · `top-k` · `approximate nearest neighbour` · `write overhead` · `query-driven indexing` · `explain()`.

---

# 8. THE FIVE 20-MARK SPINES (one glance each)
1. **NORMALIZATION:** FDs/keys/closure → 1NF → 2NF → 3NF → BCNF → 4NF → 5NF → lossless → preservation → minimal cover → benefits.
2. **TRANSACTIONS:** transaction+example → states → ACID → SQL/isolation → anomalies → serializability+graph → locks → 2PL → deadlock → timestamps → failures → deferred/immediate/shadow → log/WAL/checkpoint → undo/redo → reliability.
3. **DISTRIBUTED:** definition → architecture → characteristics/types → fragmentation → replication/allocation → 2PC → consistency models → CAP (C/A/P, during partition) → ACID vs BASE → sharding → trade-offs.
4. **NOSQL/MONGO:** NoSQL definition → 4 models → compare → CAP/BASE → sharding → Mongo model → mapping → CRUD → operators → aggregation → applications → when to use.
5. **INDEXING:** index + I/O → B+ tree (+range) → hash (+collisions) → compare → MongoDB → CouchDB → Cassandra → Neo4j → vector/HNSW → benefits/costs → query-driven conclusion.

---

# 9. FINAL 60-SECOND CHECKLIST BEFORE YOU WRITE
[ ] Did I define it in source wording? [ ] Diagram with labels + caption? [ ] Headings per component?
[ ] A concrete example? [ ] Advantages **and** limitations? [ ] Commands for NoSQL questions?
[ ] CAP/3NF/BCNF traps avoided? [ ] Conclusion tying to correctness/performance/scalability/reliability?
