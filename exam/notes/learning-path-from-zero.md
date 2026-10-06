# learning-path-from-zero.md — "I know nothing" 12-lesson path

*For a student starting from zero with the ADBMS exam tomorrow. Merges three sources:*
- *`ADBMS_MasterNotes.docx` — the authoritative syllabus notes (36 pp., 5 units, 61 sections)*
- *`chatgpt/adbms-papermorph/` — its 11-lesson teaching order, 50 memory hooks, traps (verified against source)*
- *`claude/ADBMS Boss Rush.html` — its 32-question MCQ drill bank (verified; now Section H of the question bank)*

**How to use:** work top to bottom. Each lesson = read → say the hooks out loud → answer the checkpoint MCQs in
`question-bank.md` (don't peek) → mark ✗ on anything you miss. One lesson ≈ 20–25 minutes. Total ≈ 4–5 hours,
then switch to `revision-plan.md` + mocks.

**Exam output rule (from the source, applies to every 10/20-mark answer):**
*Define (5–7 lines) → draw the diagram/flow → explain each component under its own heading → give an example →
comparison/pros-cons → 3–4 line conclusion.* Every answer you practice must follow this shape.

---

## UNIT 1 — Foundations (Lessons 1–3) — 55 min

### Lesson 1 · What databases are, why DBMS exist, and the three-level map
**Read:** `chapter-notes/unit-1.md` U1-1→U1-3 · **Hooks file:** `memory-hooks.md` §3
**You must be able to produce:** the three-level architecture diagram with labels + physical vs logical independence examples.

| Concept | Plain meaning |
|---|---|
| Database | Organized collection of logically related data |
| DBMS | Software that defines, creates, stores, retrieves, updates, protects, recovers the data |
| File system pain | Redundancy → inconsistency; no sharing/security/concurrency/recovery control; program-data dependence |
| External level | What each user group sees (views) |
| Conceptual level | The logical blueprint of everything |
| Internal level | How it's physically stored (files, pages, indexes) |
| Physical independence | Change storage/index without changing the logical schema |
| Logical independence | Change the conceptual schema without breaking user views |
| Schema | The blueprint (stable) · **Instance** | The current data values (changes constantly) |

**Hooks:** DBMS = *define, store, retrieve, update, protect, recover* · External = what user sees, Conceptual = blueprint,
Internal = storage · Physical = storage changes, Logical = schema changes.
**Trap:** never swap conceptual ↔ internal; never say "schema = SQL".

**Checkpoint →** `question-bank.md` **Q1, Q3, Q4, Q5** + MCQ **Q121, Q122, Q89**
**Wrap (3 steps):** 1) DBMS = define, store, retrieve, update, protect, recover. 2) External=user views, Conceptual=blueprint, Internal=storage. 3) Physical independence = storage changes; logical = schema changes; schema=blueprint, instance=data now.

### Lesson 2 · ER modeling and mapping to tables
**Read:** U1-4→U1-5 · **Hooks:** `memory-hooks.md` §3, `diagrams-and-mental-models.md` D2
**You must be able to produce:** an ER diagram from a scenario, then the relational schema with all 7 mapping rules.

| Concept | Plain meaning |
|---|---|
| Entity / attribute / relationship | The thing / its detail / the association between things |
| Derived attribute | Computable (age from DOB) |
| Composite attribute | Splittable (address = street + city) |
| Multivalued attribute | More than one value (phones) → needs its own table |
| Super / candidate / primary / alternate / foreign key | All possible keys / minimal unique / the chosen one / candidate-not-chosen / points to another table's key |
| Cardinality vs participation | How many (1:1, 1:N, M:N) vs mandatory-or-optional |
| 1:N mapping | The 1-side's key becomes a foreign key in the **N-side** |
| M:N mapping | Always a **new junction table** holding both keys |

**Hooks:** Thing = entity, detail = attribute, association = relationship · Many gets the key (FK on N side) ·
M:N needs a middleman table.
**Trap:** cardinality ≠ participation; FK goes on the **many** side, always.

**Checkpoint →** **Q6–Q12** + MCQ **Q117 (M:N), Q123, Q124, Q120 (entity integrity)**
**Wrap (3 steps):** 1) Thing=entity, detail=attribute, association=relationship. 2) 1:N → FK on N side; M:N → junction table. 3) Cardinality=how many; participation=mandatory-or-optional — never swap them.

### Lesson 3 · Relational model, SQL, integrity
**Read:** U1-6→U1-9 · **Hooks:** `memory-hooks.md` §3, `formulas.md` σ/π
**You must be able to produce:** the SQL command-family table + integrity-constraints table + one worked query.

- **Relational algebra:** σ = select **rows** (a condition), π = **columns** (project), JOIN = combine on a key.
- **SQL families:** DDL *defines* (CREATE/ALTER/DROP) · DML *manipulates* (SELECT/INSERT/UPDATE/DELETE) ·
  DCL *controls access* (GRANT/REVOKE) · TCL *tames transactions* (COMMIT/ROLLBACK).
- **Integrity:** entity = PK unique & NOT NULL · referential = FK must match a real PK · domain = values legal.
- **SQL clauses order:** FROM → WHERE (rows) → GROUP BY → HAVING (groups) → SELECT → ORDER BY.

**Hooks:** DDL Defines, DML Manipulates, DCL Controls, TCL Tames · WHERE filters rows, HAVING filters groups.
**Trap:** WHERE before GROUP BY, never after; PK can never be NULL.

**Checkpoint →** **Q13–Q18** + MCQ **Q119 (HAVING), Q118 (PK), Q120**
**Wrap (3 steps):** 1) σ=rows, π=columns. 2) DDL Defines, DML Manipulates, DCL Controls, TCL Tames. 3) WHERE filters rows → GROUP BY → HAVING filters groups; PK can never be NULL.

---

## UNIT 2 — Normalization & Storage (Lessons 4–6) — 60 min

### Lesson 4 · Functional dependencies and the normalization ladder 1NF→5NF
**Read:** `chapter-notes/unit-2.md` U2-1→U2-11 · **Hooks:** `memory-hooks.md` §4 — *the money hooks* ·
`comparisons.md` C1–C13 · **Practice on paper:** Q21, Q25, Q26, Q87
**You must be able to produce:** given F and a relation, find the key via closure, name the violated NF, decompose.

- **FD X→Y:** knowing X fixes Y. **Closure X⁺:** keep applying FDs until nothing new.
- **Key:** smallest set whose closure = all attributes.
- **The ladder (memorize verbatim):**
  - **1NF** — atomic cells, no repeating groups · **2NF** — 1NF + no *partial* dependency (non-key depends on the **whole** key)
  - **3NF** — no *transitive* dependency (non-key must not determine non-key) — test: **X→A holds if X is a super key OR A is prime**
  - **BCNF** — **every** determinant is a super key — test: **ONLY** X is a super key
  - **4NF** — no bad multivalued dependency · **5NF** — no join dependency not implied by keys
- **Decomposition tests:** *lossless* = intersection is a super key of at least one piece ·
  *dependency-preserving* = original FDs still checkable without joins.
- **Minimal cover:** split RHS → remove extraneous LHS → remove redundant FDs.

**Hooks:** *The key (1NF), the WHOLE key (2NF), nothing but the key (3NF), so help me Codd (BCNF)* ·
Lossless = reconstruct, preservation = enforce.
**Trap:** 3NF is **OR** (super key *or* prime attribute); BCNF is **ONLY** (super key, full stop).

**Checkpoint →** **Q21–Q34, Q87** + MCQ **Q91–Q95, Q127, Q128, Q141**
**Wrap (3 steps):** 1) Closure X⁺ → key = smallest set reaching everything. 2) Ladder: atomic (1NF) → whole-key (2NF) → no transitive (3NF=OR) → determinant-superkey (BCNF=ONLY). 3) Lossless = intersection is a super key of one part; preservation = FDs checkable without joins.

### Lesson 5 · Storage, B+ trees and hashing
**Read:** U2-12→U2-14 · **Hooks:** `memory-hooks.md` §4 · `diagrams-and-mental-models.md` B+ tree
**You must be able to produce:** a B+ tree insert/search drawing + B+ vs hash comparison table.

- **B+ tree:** sorted, all data in **leaf** nodes, leaves **linked** → range queries fly.
  *B for Between.* Order: log_F(N) levels; fanout F = pointer count.
- **Hash:** compute bucket from key → O(1) exact lookup. *H for Has-exactly.* Collisions → chaining / overflow.
- **Choose:** range/pattern → B+ tree; equality-only hot lookup → hash.

**Hooks:** B for Between (ranges), H for Has-exactly (equality) · index = faster reads + storage & write cost.
**Trap:** hash is bad at ranges; indexes slow **writes**.

**Checkpoint →** **Q35–Q40** + MCQ **Q109, Q110, Q129, Q130**
**Wrap (3 steps):** 1) B+ tree = sorted + linked leaves → ranges fast (B for Between). 2) Hash = bucket from key → equality fast (H for Has-exactly). 3) Indexes = faster reads, slower writes, extra storage.

### Lesson 6 · Anomalies and schema-design guidelines
**Read:** U1-9 revisit + `common-mistakes.md` §B · **Hooks:** `common-mistakes.md`
**You must be able to produce:** insert/update/delete anomaly examples on one relation + how normalization cures each.

- **Insert anomaly** — can't add a fact without unrelated data · **Update anomaly** — one fact in many places,
  change one copy → inconsistency · **Delete anomaly** — deleting a row destroys unrelated facts.

**Checkpoint →** **Q19, Q20** + MCQ **Q141 (NF matching)**
**Wrap (3 steps):** 1) Insert anomaly = can't add a fact without unrelated data. 2) Update anomaly = one fact in many places → inconsistency. 3) Delete anomaly = deleting a row destroys unrelated facts; normalization cures all three.

---

## UNIT 3 — Transactions & Recovery (Lessons 7–9) — 60 min

### Lesson 7 · Transactions, ACID, isolation levels
**Read:** `chapter-notes/unit-3.md` U3-1→U3-4 · **Hooks:** `memory-hooks.md` §5 · **Highest-value Unit 3 topic**
**You must be able to produce:** ACID with one worked bank-transfer example per property + the isolation-level table.

- **Transaction** = one logical unit (bank transfer: debit A + credit B must succeed or fail together).
- **States:** Active → Partially Committed → Committed; failure path → Failed → Aborted → restart.
- **ACID:** **A**ll-or-nothing (atomicity) · **C**orrect state kept (consistency) · **I**solated (concurrency control) ·
  **D**urable after commit (survives crashes).
- **Isolation levels** (weakest→strongest): Read Uncommitted (dirty reads) → Read Committed →
  Repeatable Read (no non-repeatable reads; phantoms may remain) → Serializable (full).

**Hooks:** A = all, C = correct, I = isolated, D = durable · recovery guards A & D, concurrency control guards I.
**Trap:** "durability" = survives **failure after commit**, not "data is fast"; Partially Committed ≠ Committed.

**Checkpoint →** **Q41–Q46** + MCQ **Q97, Q98, Q99, Q131**
**Wrap (3 steps):** 1) Transaction = one logical unit; states Active → Partially Committed → Committed. 2) A=all-or-nothing, C=correct state, I=isolated, D=durable after commit. 3) Isolation ladder weakest→strongest: Read Uncommitted → Read Committed → Repeatable Read → Serializable.

### Lesson 8 · Concurrency: anomalies, serializability, 2PL, deadlock
**Read:** U3-5→U3-7 · **Hooks:** `memory-hooks.md` §5 · `processes-and-algorithms.md` P8–P11
**You must be able to produce:** a precedence graph for a schedule + the 2PL growing/shrinking diagram.

- **Anomalies:** Lost update (overwrite) · Dirty read (see uncommitted) · Non-repeatable read (row changes mid-transaction) ·
  Phantom (new rows appear).
- **Conflict serializability:** build precedence graph on conflicting pairs; **cycle = not serializable**.
- **Locks:** **S**hared (read) vs e**X**clusive (write); X conflicts with everything.
- **2PL:** *Growing* — acquire locks, release none · *Shrinking* — release only, **acquire none**.
  Guarantees serializability; may deadlock.
- **Deadlock:** circular waiting; detect with **wait-for graph** cycle; cure by aborting a victim (or prevent with
  ordered lock acquisition).

**Hooks:** Grow = grab, shrink = surrender, never regrow · cycle in the graph = bad news ·
Lost = overwrite, Dirty = uncommitted, Non-repeatable = same row diff value, Phantom = new row.
**Trap:** **2PL ≠ 2PC** (2PL = locking discipline in one DB; 2PC = distributed agreement protocol).

**Checkpoint →** **Q47–Q56** + MCQ **Q100, Q101, Q102, Q132**
**Wrap (3 steps):** 1) Anomalies: Lost=overwrite, Dirty=uncommitted, Non-repeatable=same row new value, Phantom=new row. 2) Precedence graph: cycle = NOT serializable. 3) 2PL: grow=grab, shrink=surrender, never regrow; deadlock = circular wait, caught by wait-for graph.

### Lesson 9 · Recovery: failures, deferred/immediate, shadow paging, WAL, checkpoints
**Read:** U3-8→U3-12 · **Hooks:** `memory-hooks.md` §5 · `processes-and-algorithms.md` P12–P16
**You must be able to produce:** the recovery chain diagram (LOG → CHECKPOINT → CRASH → UNDO/REDO) + a
deferred vs immediate comparison row.

- **Failures:** transaction (logic/abort) · system (software) · **disk/communication** (torn page, head crash).
- **Deferred update:** uncommitted changes never touch the DB → **REDO only** after commit.
- **Immediate update:** DB written before commit → **UNDO uncommitted + REDO committed** on recovery.
- **Shadow paging:** keep old pages; switch root pointer at commit → old version stays valid (no UNDO).
- **WAL:** **log before data** — the log record must reach stable storage *before* the changed data page.
- **Checkpoint:** forces earlier log + dirty pages to disk → recovery starts from the checkpoint, not from time zero.

**Hooks:** Deferred = Delay → only REDO · Immediate = I need both → UNDO + REDO · WAL = log first, always.
**Trap:** WAL is **log-before-data**, never data-first; deferred update needs **no UNDO**.

**Checkpoint →** **Q57–Q68** + MCQ **Q103, Q104, Q134**
**Wrap (3 steps):** 1) Deferred = Delay → REDO only. 2) Immediate = I need both → UNDO+REDO. 3) WAL = log before data, always; checkpoint bounds where recovery starts; shadow paging = switch root pointer, no UNDO.

---

## UNIT 4 — Distributed & NoSQL core (Lessons 10–11) — 45 min

### Lesson 10 · Fragmentation, replication, 2PC, CAP/BASE, sharding
**Read:** `chapter-notes/unit-4.md` U4-1→U4-9 · **Hooks:** `memory-hooks.md` §6 · `comparisons.md` C23–C31
**You must be able to produce:** fragmentation types + 2PC two-round flow + the CAP paragraph (exact wording!).

- **Horizontal fragmentation** — split **rows** (selection σ) · **Vertical** — split **columns** (projection π, keep the key) ·
  Rebuild: horizontal → UNION, vertical → JOIN on the key.
- **Replication:** copies for availability/performance; cost = update coordination.
- **2PC:** *Prepare* (coordinator asks, participants **vote**) → *Commit/Abort* (any **NO** → global abort).
  Drawback: **blocking** if the coordinator dies mid-protocol.
- **CAP theorem (exact wording):** *During a network partition*, a distributed system can guarantee **at most two of three** —
  Consistency (every read gets the latest write **or an error**), Availability (every non-failing node answers),
  Partition tolerance (keeps working despite failures). **Never** write "any two at all times."
- **BASE:** **B**asically **A**vailable, **S**oft state, **E**ventual consistency — trade immediate consistency for availability.
- **Sharding:** Range (locality) · Hash (**balance**, ranges get hard) · Directory (lookup map) · Geographic (latency).

**Hooks:** CAP is about behavior DURING a partition · CP = Careful & Patient, AP = Always Present ·
Hand out Rows (horizontal), Vertical slices of columns (vertical) · 2PC = Prepare, then Commit.
**Trap:** CAP's condition is **the partition itself** — "any two at all times" is the #1 wrong answer in the subject.

**Checkpoint →** **Q69–Q76** + MCQ **Q105–Q108, Q135, Q136**
**Wrap (3 steps):** 1) Horizontal=rows (σ), vertical=columns (π, key kept); rebuild: UNION / JOIN-on-key. 2) 2PC: Prepare→vote→Commit/Abort; any NO = global abort; blocking = its drawback. 3) CAP = at most two of C/A/P *during a partition* — never 'any two at all times'; BASE = Basically Available, Soft state, Eventual consistency.

### Lesson 11 · MongoDB + Cassandra + Redis + Neo4j + vector search
**Read:** U4-10→U4-12 + `chapter-notes/unit-5.md` U5-1→U5-7 · **Hooks:** `memory-hooks.md` §7 ·
`comparisons.md` C32–C39 · `processes-and-algorithms.md` P17–P23
**You must be able to produce:** the store-comparison table + real commands + the ANN explanation.

| Store | Model | Anchor fact |
|---|---|---|
| MongoDB | Document (JSON) | Table→**collection**, row→**document**, column→**field**; `db.x.find({age:{$gt:20}})`; pipeline `$match→$group→$sort` (filter first!) |
| Cassandra | Wide-column | **Partition key = where data lives**, **clustering = order within**; query-driven design, duplicate freely |
| Redis | Key-value | Fast temporary/session state; TTL expiry |
| Neo4j | Graph | Nodes/edges/properties; `MATCH (a)-[:FRIEND]->(b)`; friend-of-friend = its sweet spot |
| Vector DB | Embeddings | Data→embedding→vector→nearest-neighbour; **cosine = angle** similarity; **HNSW = graph** ANN, **IVF = clusters**; brute force O(N·d) |

**Hooks:** Doctors Keep Calm Gracefully = Document, Key-value, Column, Graph · My Great Shoes = Match, Group, Sort ·
partition = place, clustering = order · scalar access ≠ similarity access.
**Trap:** Cassandra partition ≠ clustering; HNSW ≠ IVF (graph vs clusters); aggregation `$match` first.

**Checkpoint →** **Q77–Q86, Q88** + MCQ **Q111–Q116, Q137–Q140**
**Wrap (3 steps):** 1) MongoDB: table→collection, row→document; pipeline $match first. 2) Cassandra: partition key=where, clustering=order. 3) Redis=key-value+TTL, Neo4j=graph traversal, vectors: cosine=angle, HNSW=graph, IVF=clusters.

---

## Lesson 12 · The 20-mark answer builder + mixed final drill
**Read:** `answer-bank.md` (all 20-mark skeletons) + `notes/final-cram.md` · **Hooks:** `memory-hooks.md` §1–2
**You must be able to produce:** any 20-mark answer in the fixed shape, from memory, in ~25 minutes.

**The formula (both artifacts agree — it's the source's own guidance):**
*Dogs Draw Elephants, Politely Concluding* → **D**efine (5–7 lines) · **D**iagram · **E**laborate each component
under its own heading · **E**xample (table/query/schedule) · **P**ros-cons-comparison · **C**onclusion (3–4 lines on
correctness/speed/reliability).

**Wrap (3 steps):** 1) Define 5–7 lines → 2) diagram + components under headings → 3) example, pros/cons,
3–4 line conclusion on correctness/speed/reliability.

**Final drill order (closed book):** `final-cram.md` §1–§6 → 20 flashcards from the ✗ pile →
3 one-page 20-mark answers (ACID, Normalization, CAP) timed at 25 min each → `mock-exam-3.md`.

---

## Progress log

| Lesson | Date/time | Checkpoint ✗ count | Notes |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| … | | | |

Log every ✗ in `weakness-tracker.md` — that file becomes your final-10-minutes reading list.
