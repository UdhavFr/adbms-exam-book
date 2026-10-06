# memory-hooks.md — Mnemonics, Chains, Anchors

> Companion: [`memorization-techniques.md`](memorization-techniques.md) assigns the apt device
> per topic (acronym / story / loci / discriminator), with fully-worked devices and drill protocols.
> Hooks below are the raw material; the techniques file says how to encode each one.

Only hooks that actually help are listed — each is paired with the fact it unlocks.
Priority order: **lists → sequences → protocols → classifications → differences → terminology.**

---

## 1. Whole-subject skeleton (4 chains) ← *learn this first*

```
DESIGN:       ER → RELATIONAL → FD → NORMALIZATION → INDEXING → QUERY PERFORMANCE
RELIABILITY:  TRANSACTION → ACID → CONCURRENCY → SERIALIZABILITY → LOCKS/2PL → RECOVERY
DISTRIBUTION: DISTRIBUTED DB → FRAGMENT/REPLICATE → 2PC → CAP → NoSQL → SHARDING
NoSQL:        MongoDB / Cassandra / Redis / Neo4j / VECTOR DB → specialised access patterns
```
If you forget where a topic lives, place it in one of these four chains.

---

## 2. Definitions worth a word-chain

| Fact | Hook |
|---|---|
| DBMS functions | **D-S-R-U-S-R** = Define, Store, Retrieve, Update, Secure, Recover |
| 9 DBMS functions (expanded) | *Loci:* Door = schema · warehouse = storage · search desk = query · cashier = transaction · traffic police = concurrency · rule checker = integrity · guard = security · emergency room = recovery · catalogue = metadata |
| Three-level architecture | **E-C-I** = External → Conceptual → Internal |
| Data independence | **P** = Pages/physical · **L** = Logic/logical |
| Data models list | *Chunk:* old structural = Hierarchical/Network/Relational · conceptual/object = ER/Object-oriented · modern NoSQL = Document/Key-value/Column-family/Graph |
| Keys | **Nested boxes:** Super → Candidate (minimal) → Primary (chosen); unchosen candidate = Alternate; **Foreign = points elsewhere** |
| Schema vs instance | **BLUEPRINT = schema · CURRENT BUILDING = instance** |
| Cardinality anchors | Person–Passport = 1:1 · Department–Employee = 1:N · Student–Course = M:N |
| Participation | **Total = mandatory · Partial = optional** |

---

## 3. Unit 1 processing hooks

| Fact | Hook |
|---|---|
| ER→relational (7 rules) | **Entity→table · Composite→split · Multi→new table · 1:1→FK · 1:N→FK on N · M:N→new table · Weak→owner key + partial key** |
| Relational vocabulary | Relation=table, Tuple=row, Attribute=column, Domain=permitted values, Degree=#columns, Cardinality=#rows |
| Relational algebra | **Selection selects RECORDS, Projection selects FIELDS** (S↔rows, P↔columns) |
| SQL categories | **DDL=Design · DML=Manipulate · DCL=Control access · TCL=Transaction** |
| SQL processing order | rhythm: **FROM – WHERE – GROUP – HAVING – SELECT – ORDER – LIMIT** |
| Integrity constraints | **D-E-R** (Domain, Entity, Referential) **+ U-C-N** (UNIQUE, CHECK, NOT NULL) |
| Anomalies | **I-U-D** = Insertion / Update / Deletion |
| Unit-1 exam flow | Requirements → ER → constraints → relational schema → normalization → SQL implementation |

---

## 4. Normalization hooks ← *the money hooks*

| Fact | Hook |
|---|---|
| Ladder | **UNF → 1NF → 2NF → 3NF → BCNF → 4NF → 5NF** |
| What each fixes | **1=Atomic · 2=Partial · 3=Transitive · BC=Determinant · 4=MVD · 5=Join** |
| Acronym for the six | **A-P-T-D-M-J** = Atomic, Partial, Transitive, Determinant, Multivalued, Join |
| 3NF vs BCNF | **3NF = OR · BCNF = ONLY** |
| Attribute closure | **Start → Unlock → Add → Repeat → Complete** |
| Minimal cover | **S-E-R** = Split RHS → Extraneous LHS → Remove redundant FDs |
| Lossless vs preservation | **Puzzle picture** (exact rebuild) vs **rules checked in each drawer** |
| Canonical examples | 2NF = ENROLL · 3NF = EMPLOYEE/DEPARTMENT · 4NF = HOBBIES+LANGUAGES |
| Solving NF questions | FDs → Key → Prime/Non-prime → test in ladder order → decompose → verify |

---

## 5. Transaction & recovery hooks

| Fact | Hook |
|---|---|
| ACID story | Atomicity = both debit **and** credit · Consistency = valid account state · Isolation = nobody sees a half-transfer · Durability = still there after restart |
| Transaction states | **Active → Partially committed → Committed**; failure branch **Failed → Aborted** |
| Isolation levels | **RU → RC → RR → S** (increasing strength) |
| Anomaly stories | *"My write vanished"* (lost update) · *"I read dirty data"* (dirty read) · *"Same row changed"* (non-repeatable) · *"New matching rows appeared"* (phantom) |
| Locks | **S = Shares · X = eXcludes** (only S+S compatible) |
| 2PL phases | **GROWING → LOCK POINT → SHRINKING** |
| Deadlock handling | **PADT** = Prevention, Avoidance, Detection, Timeout |
| Failure types | *Loci:* transaction room → server/power room → disk room → network room |
| Deferred vs immediate | **Deferred = delay the data · Immediate = data may already be on disk** |
| Shadow paging | **old safe book / new working book** |
| WAL | **LOG FIRST, DATA SECOND** |
| Recovery master flow | DEFINE → FAILURES → DEFERRED → IMMEDIATE → SHADOW → LOG → WAL → CHECKPOINT → UNDO/REDO → CONCLUSION |
| The single recovery rule | **Committed = REDO as needed · Uncommitted = UNDO as needed** |

---

## 6. Distributed hooks

| Fact | Hook |
|---|---|
| Architecture | SITE A ↔ NETWORK ↔ SITE B ↔ NETWORK ↔ SITE C |
| Fragmentation | **Horizontal = Rows · Vertical = Columns** (+ PK repeated) |
| 2PC | **ASK → VOTE → DECIDE** (PREPARE → YES/NO → COMMIT/ABORT) |
| CAP | **C-A-P, only meaningful DURING a partition**; *never* "any two all the time" |
| Consistency models | strong → eventual → causal → session (read-your-writes, monotonic reads) |
| Sharding strategies | **Range · Hash · Directory · Geographic** ("R-H-D-G") |
| Good shard key | even spread · supports common queries · no hotspots |
| System types | Homogeneous = **same** tech · Heterogeneous = **different** · Federated = **independent but cooperating** |

---

## 7. NoSQL / store hooks

| Fact | Hook |
|---|---|
| Four models | **D-K-C-G** = Document, Key-value, Column-family, Graph (anchor uses: catalog · cache · big distributed · social) |
| Relational → MongoDB | **Database→Database, Table→Collection, Row→Document, Column→Field, PK→_id** |
| MongoDB CRUD | every action has **ONE / MANY** (insertOne/insertMany, find/findOne, updateOne/updateMany, deleteOne/deleteMany) |
| MongoDB operators | comparison `$gt $gte $lt $lte $eq $ne` · membership `$in $nin` · logical `$and $or $not $nor` · update `$set $unset $inc $push $pull` |
| Aggregation | **$match → $group → $project → $sort → $limit** (*also $skip, $unwind, $lookup*) |
| Cypher order | **CREATE → MATCH → WHERE → SET → DELETE** ("Create → Find → Filter → Modify → Destroy") |
| Cypher pattern | `MATCH (node)-[:REL]->(node) RETURN …` — **round = node, bracket = relationship** |
| Cassandra | **Partition = Place · Clustering = Order** |
| Redis | basic key → hash → time → counter (**SET/GET · HSET/HGET · EXPIRE · INCR**) |
| Graph model | **Nodes = entities · Edges = relationships · Properties = attributes** |
| Vector pipeline | **Query → Embedding → Index → Top-K** |
| Similarity metrics | **Cosine = angle · Euclidean = distance · Dot = alignment + magnitude** |
| ANN structures | **HNSW = GRAPH navigation · IVF = CLUSTERS** |
| Index trade-off | **faster reads ↔ storage + maintenance cost** |
| HBase vs Cassandra | HBase = **H**adoop-bound, row key + families, shell/API · Cassandra = **independent**, partition+clustering, CQL |

---

## 8. Contrast pairs to recite (30 seconds each)

```
schema ↔ instance          physical ↔ logical independence      degree ↔ cardinality
super ↔ candidate key      selection ↔ projection               partial ↔ transitive
3NF OR ↔ BCNF ONLY         4NF ↔ 5NF                            lossless ↔ preserving
B+ ↔ hash                  serial ↔ serializable               S ↔ X
basic ↔ strict ↔ rigorous  deferred ↔ immediate ↔ shadow        undo ↔ redo
2PL ↔ 2PC                  horizontal ↔ vertical               fragmentation ↔ replication
CAP ↔ BASE                 sharding ↔ replication              partition key ↔ clustering column
traditional ↔ vector index cosine ↔ euclidean ↔ dot            HNSW ↔ IVF
```

---

## 9. Diagram-flash method (draw from memory, 90 s each)

1. Three-level architecture · 2. ER (STUDENT ◇ ENROLLS ◇ COURSE, M:N) · 3. Normalization ladder ·
4. B+ tree with linked leaves · 5. Transaction states · 6. 2PL with LOCK POINT ·
7. LOG → CHECKPOINT → UNDO/REDO · 8. Distributed sites ↔ network · 9. CAP triangle ·
10. Sharding split · 11. Vector search pipeline.

**Routine:** cover the page → draw all 11 → check → redraw only the ones you missed (max 2 rounds).
