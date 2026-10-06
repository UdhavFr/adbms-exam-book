# processes-and-algorithms.md — Every Ordered Process, as Flows

Format: **INPUT → steps → OUTPUT**, then a **compressed chain** to memorise, then the
**exam-ready explanation** (the sentence to write). Marks for processes come from *order*, so never re-order the steps.

---

## P1. ER → Relational mapping (7 rules) — U1 §5 · P0

**INPUT:** an ER diagram with entities, attributes, relationships, weak entities.
**OUTPUT:** a set of relations with primary/foreign keys.

```
ER DIAGRAM
   ↓ strong entity            → one relation; entity PK becomes relation PK
   ↓ composite attribute      → store the components, not the composite
   ↓ multivalued attribute    → NEW relation (owner PK + the value)
   ↓ 1:1 relationship         → PK of one side as FK in the other (prefer total-participation side)
   ↓ 1:N relationship         → PK of the 1-side becomes FK in the N-side
   ↓ M:N relationship         → NEW relation with both PKs (usually a composite PK)
   ↓ weak entity              → its attributes + owner PK; owner key + partial key identifies it
RELATIONAL SCHEMA
```

**Chain:** *Entity→table · Composite→split · Multi→new table · 1:1→FK · 1:N→FK on N · M:N→new table · Weak→owner+partial.*
**Exam-ready:** "For a strong entity create a relation whose primary key is the entity's key; store composite components separately; give multivalued attributes their own relation; place the 1-side key as a foreign key on the N-side; for M:N create a junction relation containing both keys; a weak entity's relation carries its owner's key."
**Common mistake:** putting the FK on the 1-side for a 1:N relationship (it must go on the **N**-side).

---

## P2. Solving a normalization question (the full procedure) — U2 · P0

**INPUT:** a relation with attributes and a set of FDs (given or inferable).
**OUTPUT:** the current normal form, the violation, and the decomposed schema.

```
LIST THE FDs
   ↓
FIND THE CANDIDATE KEY(s)  (attribute closure of candidate combinations)
   ↓
CLASSIFY attributes: prime vs non-prime
   ↓
TEST 1NF  → atomic values / no repeating groups          (else fix first)
   ↓
TEST 2NF  → any non-prime depends on PART of a key?      → partial dependency
   ↓
TEST 3NF  → any non-prime depends on a non-key attribute? → transitive dependency
   ↓
TEST BCNF → any determinant that is not a super key?
   ↓
TEST 4NF  → any non-trivial MVD with non-super-key determinant?
   ↓
TEST 5NF  → any non-trivial JD not implied by candidate keys?
   ↓
DECOMPOSE the violating relation, then RE-VERIFY
   • lossless join  (R1∩R2 → R1 or R2)
   • dependency preservation where possible
RESULT
```

**Chain:** *FDs → Key → Prime/Non-prime → 1 → 2 → 3 → BC → 4 → 5 → Decompose → Verify.*
**Exam-ready template (write this for any "check/convert to 3NF" question):**
1. "The functional dependencies are…"
2. "The candidate key is …, computed by attribute closure…"
3. "The relation is in __NF because … / violates __NF because …"
4. "The violation is a partial/transitive dependency of … on …"
5. "Decomposition: …"
6. "The result is in the target normal form; the decomposition is lossless (because …) and dependency preserving (because …)."

---

## P3. Attribute closure X⁺ — U2 §1 · P0

**INPUT:** a set of FDs F, an attribute set X.
**OUTPUT:** all attributes determined by X (⇒ super key test).

```
START  C = {X}
   ↓
SCAN F: any FD W→Z with W ⊆ C ?   --no--> STOP (no growth)
   ↓ yes
ADD Z to C
   ↓
LOOP until no change
   ↓
IF C = all attributes → X is a SUPER KEY (minimal ⇒ candidate key)
```

**Chain:** *Start → Unlock → Add → Repeat → Complete.*
**Worked example:** F={A→B,B→C,C→D}: {A} → {A,B} → {A,B,C} → **{A,B,C,D}** ⇒ A is a key.
**Common mistake:** running the FD list only once instead of looping to a fixed point.

---

## P4. Minimal cover — U2 §11 · P1

**INPUT:** F.
**OUTPUT:** canonical cover G with F⁺ = G⁺.

```
SPLIT every FD so RHS = one attribute
   ↓
REMOVE extraneous attributes from each left side (re-test each removal)
   ↓
REMOVE redundant FDs (each must be re-checked against the rest)
   ↓
G is the MINIMAL COVER
```

**Chain:** **S-E-R** = Split → Extraneous → Remove.
**Common mistake:** skipping step 2 (extraneous LHS attributes) — that is what "minimal" mostly means.

---

## P5. Lossless-join verification — U2 §9 · P0

**INPUT:** R, F, a decomposition {R₁, R₂}.
**OUTPUT:** lossless or not.

```
COMPUTE  I = R1 ∩ R2
   ↓
TEST  I → R1   (using F⁺ / closure of I)
   ↓
OR     I → R2
   ↓
either holds → LOSSLESS (joining reproduces R exactly, no spurious tuples)
neither holds → NOT lossless
```

**Chain:** *Intersect → Determine one side → Confirm.*
**Common mistake:** testing R1 → I instead of I → one side (direction matters).

---

## P6. B+ tree search — U2 §13 · P0

**INPUT:** search key K.
**OUTPUT:** the record(s)/data page pointer.

```
START at ROOT (internal node)
   ↓
COMPARE K with the node's separator keys
   ↓
FOLLOW the correct child pointer
   ↓
DESCEND until a LEAF node is reached
   ↓
SEARCH the leaf's key array
   ↓
FOLLOW the record/data pointer → RECORD
   (range query: scan forward along the LINKED leaves)
```

**Chain:** *Root → Compare → Child → Leaf → Record.*
**Why fast:** balanced height · high fan-out (few levels) · linked leaves (range scans) · dynamic insert/delete · nodes sized to disk pages.
**Complexity:** O(log_f N) node visits.
**Common mistake:** forgetting that **leaves are linked** — that is the whole reason B+ trees beat other trees for range queries.

---

## P7. Hash lookup — U2 §14 · P1

**INPUT:** equality search key K.
**OUTPUT:** records in the bucket.

```
K → hash(K) → BUCKET id
   ↓
go to bucket → records/pointers
   ↓
two keys same bucket = COLLISION → overflow bucket / chaining / dynamic hashing
```

**Chain:** *Key → Hash → Bucket → Records.*
**Common mistake:** suggesting a hash index for a **range** query (poor fit — use B+ tree).

---

## P8. Conflict serializability test — U3 §5 · P0

**INPUT:** a schedule S of transactions.
**OUTPUT:** conflict-serializable? (and an equivalent serial order)

```
CREATE one node per transaction (T1, T2, …)
   ↓
FIND conflicting pairs: same data item, at least one a WRITE, different transactions
   ↓
for each pair where Ti's op comes FIRST → add edge Ti → Tj
   ↓
CHECK the graph
   ↓
ACYCLIC  → conflict-serializable (topological order = equivalent serial order)
CYCLE    → NOT conflict-serializable
```

**Chain:** *Build graph → Look for cycle.*
**Common mistake:** drawing an edge for a pair that is not a conflict (two reads never conflict).

---

## P9. Two-phase locking execution — U3 §6 · P0

**INPUT:** concurrent transactions.
**OUTPUT:** conflict-serializable execution.

```
GROWING PHASE: acquire S/X locks — NO releases
   ↓
LOCK POINT: last lock acquisition
   ↓
SHRINKING PHASE: release locks — NO new acquisitions
   ↓
(STRICT 2PL: hold X locks until COMMIT/ABORT → fewer cascading rollbacks)
```

**Chain:** *Acquire-all → Lock point → Release-all.*
**Deadlock handling chain:** **PADT** = Prevention · Avoidance · Detection (wait-for graph) · Timeout.
**Common mistake:** saying 2PL means "lock everything at once" — the real rule is the *no-release-while-acquiring* boundary.

---

## P10. Timestamp ordering rules — U3 §7 · P1

**INPUT:** each transaction Ti with timestamp TS(Ti); each item X with Read_TS(X), Write_TS(X).
**OUTPUT:** execute, or reject + restart.

```
READ of X by Ti:
   TS(Ti) < Write_TS(X)  → too old, reads stale data → REJECT/ROLLBACK Ti
   else → allow; Read_TS(X) = max(Read_TS(X), TS(Ti))
WRITE of X by Ti:
   TS(Ti) < Read_TS(X)   → would overwrite newer read → REJECT/ROLLBACK Ti
   TS(Ti) < Write_TS(X)  → would overwrite newer write → REJECT/ROLLBACK Ti (or Thomas rule)
   else → allow; Write_TS(X) = max(Write_TS(X), TS(Ti))
```
**Exam-ready point:** no lock waiting ⇒ **lock-based deadlock is impossible**; cost = repeated aborts waste work.
(Detailed rule variants are [EXTERNAL] elaboration of the source's summary: "older = smaller timestamp; violation ⇒ abort and restart.")

---

## P11. Transaction state machine — U3 §2 · P1

```
ACTIVE
  ↓ last statement executes
PARTIALLY COMMITTED
  ↓ commit succeeds → COMMITTED
  ↓ failure        → FAILED → ROLLBACK → ABORTED → restart/terminate
```

**Chain:** *Active → Partially committed → Committed; fail anywhere → Failed → Aborted.*

---

## P12. SQL transaction flow — U3 §4 · P1

```
BEGIN / START TRANSACTION
   ↓
SQL operations (UPDATE …)
   ↓
  ┌──────┴──────┐
success        error
  ↓              ↓
COMMIT        ROLLBACK      (SAVEPOINT → partial rollback to a marked point)
  ↓              ↓
durable      uncommitted work undone
```

---

## P13. Deferred update (no-steal, redo-only flavour) — U3 §9 · P0

```
TRANSACTION
   ↓ write LOG records only
CONTINUE EXECUTION (no data page written)
   ↓ COMMIT
APPLY / REDO updates → durable database
   ↓ CRASH before commit
nothing reached the DB ⇒ normally NO UNDO needed
```

**Chain:** *Log → Commit → Redo.*
**Memory:** **Deferred = delay the data.**

---

## P14. Immediate update (steal flavour) — U3 §10 · P0

```
TRANSACTION → log old/new values → data page MAY be written before commit
   ↓ COMMIT?
  YES → REDO if the page never reached disk
   NO → UNDO the pages already written
```

**Chain:** *Log → Write early → Undo uncommitted + Redo committed.*

---

## P15. Shadow paging — U3 §11 · P1

```
BEFORE:   ROOT → SHADOW PAGE TABLE (old, stable) → old pages
UPDATE:   write modified pages to NEW locations; build CURRENT page table
COMMIT:   ROOT switches → CURRENT table     (old pages become garbage)
CRASH BEFORE COMMIT: keep using SHADOW → old consistent state restored
```

**Chain:** *Old book safe → new book working → commit flips the pointer → crash uses old book.*
**Trade-off:** simple recovery, but fragmentation + page-table copy overhead.

---

## P16. Log-based recovery with WAL + checkpoint — U3 §12 · P0

**INPUT:** a log on stable storage, a crash.
**OUTPUT:** consistent database.

```
NORMAL RUN: for every change, APPEND <TID, item, old, new> to the LOG
   ↓ WAL: log record reaches STABLE STORAGE before the data page is written
   ↓ periodically: CHECKPOINT (flush data, note active transactions)
   ↓ CRASH
RECOVERY:
   START from the last CHECKPOINT (no full log scan)
   for each transaction: COMMITTED → REDO as needed
                          UNCOMMITTED → UNDO as needed
   ↓
CONSISTENT DATABASE
```

**Chain:** *Log first → Checkpoint → Crash → Undo uncommitted → Redo committed.*
**Master recovery answer (source):** *DEFINE → FAILURES → DEFERRED → IMMEDIATE → SHADOW → LOG → WAL → CHECKPOINT → UNDO/REDO → CONCLUSION.*

---

## P17. Two-phase commit (2PC) — U4 §4 · P0

```
COORDINATOR                    PARTICIPANTS (P1, P2, P3)
   ↓ PREPARE ──────────────────►  record "prepared" state
   ◄──────────── YES / NO ─────  vote
   ↓
all YES → COMMIT ─────────────►  record + apply decision
any NO  → ABORT  ─────────────►  record + undo
```
**Chain:** **ASK → VOTE → DECIDE.**
**Exam-ready:** "2PC guarantees atomic commitment — no site commits unless all can — but a participant in the prepared state may *block* if the coordinator's decision cannot be learned after a failure."
**Common mistake:** calling 2PC a *locking* protocol — it is a **commit** protocol.

---

## P18. Fragmentation → allocation → replication (distributed design) — U4 §2–3 · P0/P1

```
RELATION R
   ↓ horizontal: split by predicate → R1(rows A), R2(rows B)         (completeness, reconstruction, disjointness)
   ↓ vertical:   split by columns  → R1(cols+PK), R2(cols+PK)        (PK repeated so a JOIN reconstructs R)
   ↓ hybrid:     horizontal then vertical
FRAGMENTS → ALLOCATION (which site: query frequency, locality, comm cost, storage, reliability)
   ↓ REPLICATION: full or partial copies
DISTRIBUTED STORAGE with higher availability / local reads, at the cost of update coordination
```

**Chain:** *Horizontal=Rows → Vertical=Columns → Allocate → Replicate.*

---

## P19. Sharding strategy selection — U4 §9 · P0

```
DATASET TOO LARGE FOR ONE NODE
   ↓
CHOOSE SHARD KEY (distributes data+traffic evenly, supports common queries, no hotspots)
   ↓
RANGE      → key ranges per shard (good ranges, risk of hotspots)
HASH       → hash(shard key) (even load, loses range locality)
DIRECTORY  → mapping service says where each key lives
GEOGRAPHIC → assign by region (locality/compliance)
   ↓
SHARD 1 | SHARD 2 | SHARD 3
```

---

## P20. MongoDB aggregation pipeline — U4 §12 · P0

```
COLLECTION
   ↓ $match   filter documents
   ↓ $group   aggregate (e.g. total per product)
   ↓ $project shape/compute fields
   ↓ $sort    order
   ↓ $limit   restrict (also $skip, $unwind, $lookup)
RESULT
```

**Worked example (source):** `db.sales.aggregate([{$match:{status:'paid'}}, {$group:{_id:'$product', total:{$sum:'$amount'}}}, {$sort:{total:-1}}])`
→ *filters paid sales → groups by product → sums amount → sorts by total descending.*
**Chain:** *Match → Group → Project → Sort → Limit.*

---

## P21. Vector similarity search — U5 §6–7 · P0

```
USER QUERY
   ↓ EMBED with the same embedding model → QUERY VECTOR
   ↓ VECTOR INDEX (brute force = compare all; ANN = HNSW graph / IVF clusters)
   ↓ TOP-K nearest neighbours (cosine / Euclidean / dot)
   ↓ attach metadata + original documents
FINAL RESULTS
```
**Chain:** *Query → Embedding → Index → Top-K → Results.*
**Common mistake:** embedding the query with a **different model** than the stored vectors — the space must be the same (practical point, [EXTERNAL]).

---

## P22. Query-driven Cassandra design — U5 §2, §11 · P0

```
START from the QUERY pattern
   ↓ choose PARTITION KEY  → answers "WHERE will this query look?"
   ↓ choose CLUSTERING COLS → answers "in what ORDER do rows come back?"
   ↓ duplication of data is ACCEPTABLE (joins are the thing to avoid)
TABLE + index design → efficient partition-local query
```

**Chain:** *Query → Partition key → Clustering order → Duplicate if needed.*

---

## P23. The 20-mark answer process (writing algorithm) — source intro · P0

```
READ the question twice → identify exactly what is asked
   ↓
INTRODUCTION: 5–7 lines — define + why it matters
   ↓
LABELLED DIAGRAM / FLOW (architecture, process, hierarchy, algorithm)
   ↓
COMPONENTS under separate headings (never one blob paragraph)
   ↓
PRACTICAL EXAMPLE (table, relation, transaction, query, scenario)
   ↓
ADVANTAGES / LIMITATIONS / COMPARISON
   ↓
CONCLUSION: 3–4 lines tying to correctness, performance, scalability or reliability
```
**Shape:** **DEFINE → DRAW → EXPLAIN COMPONENTS → EXAMPLE → COMPARE/ADVANTAGES → CONCLUDE.**
