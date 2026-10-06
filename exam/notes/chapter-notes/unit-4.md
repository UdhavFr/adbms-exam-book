# UNIT 4 — Distributed Databases and NoSQL Systems
Source: `ADBMS_MasterNotes.docx` Unit 4, pp. 22–24 · structure `u4ch01`–`u4ch12`
Two of the source's five 20-mark questions live here (Question 3: distributed+CAP · Question 4: NoSQL+MongoDB).

---

## U4-1 Introduction to Distributed Databases — **P1** (p. 22)
- **WHAT:** one **logically integrated** database whose data is **physically distributed** across network-connected sites; a DDBMS coordinates them and gives unified access.
- **CHARACTERISTICS:** physical distribution · network communication · transparent fragments/replicas · distributed query & transaction processing · tolerates communication/node failures · better availability/local performance · new consistency & coordination challenges.
- **TYPES:** homogeneous (similar DBMS tech) · heterogeneous (different tech/schemas) · federated (independent DBs cooperate through integration).
- **MISTAKE:** defining it as "several databases" — the point is *logically one*.

## U4-2 Data Fragmentation — **P0** (p. 22)
- **WHAT:** divide a relation into fragments stored near their users → lower communication cost, better local performance.
- **Horizontal:** split **rows** by predicate (`CUSTOMER_NORTH` / `CUSTOMER_SOUTH`).
- **Vertical:** split **columns**; **repeat the primary key** in each fragment so the relation is reconstructible by a join.
- **Hybrid:** horizontal then vertical.
- **PROPERTIES:** completeness, reconstruction, disjointness where the strategy requires them.
- **MISTAKE:** Horizontal=Columns (fix: *horizontal = rows*).

## U4-3 Replication and Allocation — **P1** (p. 23)
- **REPLICATION:** multiple copies at different sites — **full** (many/all sites) or **partial** (selected sites).
  Benefits: availability, faster local reads, failure tolerance, less remote access · Costs: storage, update coordination, consistency management, network/control overhead.
- **ALLOCATION:** which site stores which fragment/replica — decided by query frequency, data locality, communication cost, storage capacity, reliability.
- **MISTAKE:** confusing replication (copies) with fragmentation (parts).

## U4-4 Distributed Transactions and Two-Phase Commit — **P0** (p. 23)
- **WHY:** a distributed transaction may touch many sites; **atomicity must hold globally** — no commit at one site with abort at another.
- **2PC FLOW:** coordinator sends **PREPARE** → each participant records a prepared state and votes **YES/NO** → all required YES ⇒ **COMMIT**, else **ABORT** → participants record and execute the decision.
- **LIMITATION:** a prepared participant can **block** when it cannot learn the coordinator's final decision after a failure.
- **MEMORY:** **ASK → VOTE → DECIDE.**
- **MISTAKE:** calling 2PC a locking protocol (it is a **commit** protocol — see comparison C28).

## U4-5 Distributed Consistency Models — **P1** (p. 24)
- **MODELS:** strong/linearizable (single real-time-respecting order) · eventual (replicas temporarily disagree, converge if updates stop) · causal (causal order preserved) · session (read-your-writes, monotonic reads).
- **TRADE-OFF:** stronger consistency ⇒ more coordination ⇒ higher latency/lower availability during failures.
- **MISTAKE:** writing "eventual consistency is broken data" — it is a deliberate design choice.

## U4-6 NoSQL Systems — Types — **P0** (p. 24)
- **WHAT:** non-relational systems for flexible schemas, massive scale, high throughput, distributed availability, or relationship patterns that differ from tables.
- **FOUR MODELS:** Document (JSON/BSON — catalogs, content, profiles) · Key-value (cache, sessions, lookups) · Column-family (partitioned rows + flexible columns — large distributed workloads) · Graph (nodes+relationships+properties — social, recommendations, fraud).
- **MISTAKE:** "NoSQL = no schema" (Cassandra has explicit schemas).

## U4-7 CAP Theorem — **P0** (p. 25) ← *the most common wrong-answer trap in the subject*
- **EXACT STATEMENT:** "When a distributed system experiences a network partition, it cannot simultaneously guarantee both strong consistency and availability for every request under the formal CAP definitions."
- **C:** a read observes the most recent write according to the formal consistency guarantee, or an error.
- **A:** every request to a non-failing node gets a non-error response (the value need not be the latest).
- **P:** the system continues operating despite network failures preventing some nodes from communicating.
- **⚠ NEVER WRITE:** "you can simply pick any two out of three at all times."
- **EXAM WRITE:** triangle diagram + this caption + C/A/P definitions + one sentence on the design trade-off during a partition.

## U4-8 BASE vs ACID — **P0** (p. 25)
- **BASE = Basically Available, Soft state, Eventual consistency.**
- **ACID** = strong transaction-oriented guarantees for traditional relational systems; commit aims at a durable consistent state.
- **BASE** = availability and flexible consistency emphasis in distributed NoSQL use cases; state may change as replicas converge.
- **KEY LINE:** BASE does **not** mean data is permanently wrong — temporary inconsistency accepted, convergence expected.

## U4-9 Sharding and Partitioning — **P0** (p. 26)
- **WHAT:** **horizontal** distribution of records across multiple nodes; each shard holds a subset (SHARD 1: IDs 1–100 …).
- **STRATEGIES:** range (good ranges, hotspot risk) · hash (even load, weak range locality) · directory (mapping service) · geographic (by region; locality/compliance).
- **GOOD SHARD KEY:** distributes data and traffic evenly · supports common queries · avoids oversized partitions/hotspots.
- **MISTAKE:** confusing sharding (parts on different nodes) with replication (copies).

## U4-10 MongoDB Data Model — **P1** (p. 26)
- **WHAT:** document-oriented; **BSON documents in collections**; nested documents and arrays approximate application objects.
- **MAPPING:** Table→Collection · Row→Document · Column→Field · Primary key→`_id` · Database→Database.
- **MISTAKE:** "MongoDB has no primary key" (`_id` is the primary key).

## U4-11 MongoDB CRUD — **P0** (pp. 26–27)
- **COMMAND FAMILY:** insertOne/insertMany · find/findOne · updateOne/updateMany · deleteOne/deleteMany.
- **OPERATORS:** comparison `$gt $gte $lt $lte $eq $ne` · membership `$in $nin` · logical `$and $or $not $nor` · update `$set $unset $inc $push $pull`.
- **EXAMPLES:** `db.students.find({age:{$gt:21}})` · `db.students.updateOne({name:'Ravi'},{$set:{age:23}})` · `db.students.updateMany({course:'MCA'},{$inc:{age:1}})`.
- **MISTAKE:** giving prose instead of commands (the source requires actual command patterns).

## U4-12 MongoDB Aggregation — **P0** (p. 27)
- **WHAT:** a **pipeline** of stages; each stage transforms/filters/groups/sorts/joins.
- **ORDER:** `$match → $group → $project → $sort → $limit` (also `$skip`, `$unwind`, `$lookup`).
- **WORKED EXAMPLE:** `db.sales.aggregate([{$match:{status:'paid'}},{$group:{_id:'$product',total:{$sum:'$amount'}}},{$sort:{total:-1}}])` → *filter paid → group by product → sum amount → sort descending.*
- **MISTAKE:** forgetting that `$match` goes first (it prunes documents before expensive grouping).

---

### Unit 4 exam weighting
- **20-mark:** Question 3 (distributed + CAP) and Question 4 (NoSQL + MongoDB) — use the source's 13/11-bullet skeletons.
- **10-mark:** CAP with exact wording · 2PC with diagram · fragmentation types · ACID vs BASE · sharding strategies.
- **5-mark:** replication benefits/costs · consistency models · NoSQL four models · aggregation pipeline.
- **2-mark:** definitions (sharding, federated, eventual consistency…).
