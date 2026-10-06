# question-bank.md — Active-Recall Question Bank (Phase 7)

Metadata per question: `topic` (unit/chapter ID) · `P0–P3` priority · `difficulty 1–3` ·
**expected answer** · **essential keywords** (the marks) · **common incorrect answer** (what examiners deduct for).
Question types are tagged: **DEF** definition · **EXP** explain · **WHY** · **HOW** process · **CMP** compare ·
**CALC** computation · **APP** application · **TF** true/false trap · **MIS** misconception · **DIA** diagram ·
**SEQ** sequence order · **FILL** missing step.

Use with `weakness-tracker.md`: log `✗` answers as W-entries and re-test them.

---

## UNIT 1

**Q1** [DEF · U1-1 · P0 · 1] Define "database" and "DBMS" and state how they relate.
- Expected: database = organized collection of logically related data; DBMS = software to define, create, store, retrieve, update, protect, recover data; database + DBMS = database system.
- Keywords: organized collection, logically related, define/store/retrieve/update/protect/recover, database system.
- Common wrong: "DBMS is just storage" / describing a DBMS as the hardware.

**Q2** [EXP · U1-1 · P1 · 2] Explain three problems of file-processing systems and how a DBMS cures them.
- Expected: redundancy→centralized design; inconsistency→constraints + controlled updates; sharing/security/concurrency/recovery→shared DB, auth, concurrency control, logging/checkpoints; program-data dependence→abstraction/independence.
- Keywords: duplication, inconsistency, constraints, concurrency control, logging, checkpoints, data independence.
- Common wrong: only naming problems without cures (half marks).

**Q3** [DIA · U1-3 · P0 · 2] Draw the three-level architecture and label what each level contains.
- Expected: External (views) → Conceptual (logical schema) → Internal (files/pages/indexes) → physical storage, with independence arrows.
- Keywords: external views, conceptual logical, internal storage, data independence.
- Common wrong: reversing conceptual/internal; missing labels/caption.

**Q4** [CMP · U1-3 · P0 · 2] Physical vs logical data independence — one example each.
- Expected: physical = change storage without changing conceptual schema (change an index); logical = change conceptual schema while external views still work (split table with compatible view).
- Keywords: storage structures, conceptual schema, external views, index example.
- Common wrong: swapping the two.

**Q5** [CMP · U1-2 · P1 · 1] Schema vs instance with an example.
- Expected: schema = blueprint (STUDENT(RollNo,Name,Course)); instance = contents now ((101,Ravi,MCA)); schema stable, instance changes.
- Keywords: blueprint, point in time, changes frequently.
- Common wrong: "schema = SQL" or "instance = one row".

**Q6** [CMP · U1-4 · P0 · 2] Super key, candidate key, primary key, alternate key, foreign key.
- Expected: any unique set / minimal unique set / chosen candidate / unchosen candidate / references another relation's key.
- Keywords: uniquely identifies, minimal, chosen, references.
- Common wrong: "candidate key = primary key" (candidate keys may be several).

**Q7** [EXP · U1-4 · P0 · 2] Explain attribute types with one example each.
- Expected: simple (Age), composite (Address = Street/City/PIN), single-valued, multivalued (phones), derived (Age from DOB), key (StudentID).
- Keywords: atomic, components, several values, calculated, uniquely identifies.
- Common wrong: forgetting *derived*; calling an ID "composite".

**Q8** [DIA · U1-4 · P0 · 2] Draw an ER diagram for a student enrolling in a course, with a relationship attribute.
- Expected: STUDENT and COURSE rectangles, ENROLLS diamond, M and N labels, EnrollmentDate attribute on the relationship; explain symbols.
- Keywords: entity, relationship, cardinality M:N, relationship attribute.
- Common wrong: putting EnrollmentDate on STUDENT only.

**Q9** [HOW · U1-5 · P0 · 3] State the ER→relational mapping rules for 1:1, 1:N, M:N and weak entities.
- Expected: 1:1 → PK of one side as FK (prefer total participation side); 1:N → 1-side PK as FK on N-side; M:N → new relation with both PKs (composite); weak → attributes + owner PK (owner key + partial key).
- Keywords: foreign key, N-side, composite primary key, partial key.
- Common wrong: FK on the 1-side for 1:N.

**Q10** [HOW · U1-5 · P0 · 2] What do you do with a multivalued attribute during mapping?
- Expected: create a separate relation containing the owner's primary key and the multivalued value.
- Keywords: separate relation, owner PK, multivalued value.
- Common wrong: comma-separating values in one column (that's the 1NF error).

**Q11** [CALC · U1-6 · P1 · 1] Relation R has 5 attributes and 12 rows — its degree and cardinality?
- Expected: degree 5, cardinality 12.
- Keywords: degree = attributes, cardinality = tuples.
- Common wrong: swapping them.

**Q12** [MIS · U1-6 · P1 · 2] "σ selects columns and π selects rows." True or false?
- Expected: **False** — σ (selection) selects rows; π (projection) selects columns.
- Keywords: selection rows, projection columns.
- Common wrong: agreeing with the swap.

**Q13** [EXP · U1-7 · P0 · 2] Classify SQL commands into DDL, DML, DCL, TCL with examples.
- Expected: DDL CREATE/ALTER/DROP/TRUNCATE; DML SELECT/INSERT/UPDATE/DELETE; DCL GRANT/REVOKE; TCL COMMIT/ROLLBACK/SAVEPOINT.
- Keywords: structure, data, privileges, transaction.
- Common wrong: putting SELECT in DDL; putting GRANT in TCL.

**Q14** [SEQ · U1-7 · P0 · 2] In what order are SQL clauses *processed*?
- Expected: FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT.
- Keywords: WHERE before grouping, HAVING after grouping.
- Common wrong: giving the *syntax* order when asked for processing (E2).

**Q15** [MIS · U1-7 · P1 · 2] WHERE vs HAVING — which filters rows and which filters groups?
- Expected: WHERE filters rows **before** grouping; HAVING filters groups **after** grouping.
- Keywords: before grouping, after grouping.
- Common wrong: "HAVING is just a slower WHERE".

**Q16** [EXP · U1-8 · P0 · 2] Entity, domain and referential integrity.
- Expected: domain = values satisfy the type/domain; entity = PK not NULL and unique; referential = FK refers to an existing referenced key or NULL where permitted.
- Keywords: not null, unique, existing key, permitted NULL.
- Common wrong: "foreign keys can never be NULL".

**Q17** [WHY · U1-8 · P1 · 2] Why do integrity constraints matter?
- Expected: without them invalid values enter → application errors, inconsistent reports, broken relationships, wrong decisions; constraints move correctness responsibility into the database.
- Keywords: invalid values, consistency, database-level enforcement.
- Common wrong: "they make queries faster".

**Q18** [DEF · U1-9 · P1 · 1] Define insertion, update and deletion anomalies.
- Expected: insertion = can't add a fact without an unrelated fact; update = one logical change needs many updates; deletion = deleting one fact removes another that should stay.
- Keywords: unrelated fact, repeated, accidental removal.
- Common wrong: describing only redundancy, not the anomaly names.

---

## UNIT 2

**Q19** [DEF · U2-1 · P0 · 1] Define functional dependency.
- Expected: X → Y means whenever two tuples agree on all attributes of X they must also agree on all attributes of Y; X is the determinant.
- Keywords: agree on X, agree on Y, determinant.
- Common wrong: "X and Y are related" (vague = no marks).

**Q20** [CALC · U2-1 · P0 · 2] F = {A→B, B→C, C→D}; compute A⁺ and say what it proves.
- Expected: {A} → {A,B} → {A,B,C} → {A,B,C,D}; A⁺ = all attributes ⇒ A is a super key (candidate key if minimal).
- Keywords: closure, loop until no growth, super key.
- Common wrong: stopping after one FD.

**Q21** [CALC · U2-1 · P0 · 3] R(A,B,C,D) with F = {A→B, B→C, D→B}. Candidate key?
- Expected: A⁺ = {A,B,C} (no D) ✗; AD⁺ = {A,D,B,C} = all ⇒ **AD** is the candidate key.
- Keywords: closure includes all attributes.
- Common wrong: picking A because it "looks like the ID".

**Q22** [CALC · U2-1 · P2 · 3] Is C → A derivable from F = {A→B, B→C}?
- Expected: C⁺ = {C} — cannot reach A ⇒ no, C→A does not follow.
- Keywords: closure of the determinant, implication test.
- Common wrong: reading the arrow backwards (B→C does not give C→B).

**Q23** [EXP · U2-2 · P0 · 2] Draw the normalization ladder and say what each step removes.
- Expected: UNF →(atomic) 1NF →(partial) 2NF →(transitive) 3NF →(determinant is super key) BCNF →(MVD) 4NF →(JD) 5NF.
- Keywords: atomic, partial, transitive, determinant, multivalued, join.
- Common wrong: BCNF after 3NF *without* stating the determinant rule.

**Q24** [DEF · U2-3 · P0 · 1] Define 1NF.
- Expected: each attribute contains atomic values; no repeating groups or nested sets in a field.
- Keywords: atomic, repeating groups.
- Common wrong: "no NULLs" (not 1NF).

**Q25** [APP · U2-4 · P0 · 3] ENROLL(StudentID, CourseID, StudentName, CourseName, Grade): show it is not in 2NF and fix it.
- Expected: key (StudentID, CourseID); StudentName depends only on StudentID and CourseName only on CourseID ⇒ partial dependencies ⇒ decompose STUDENT / COURSE / ENROLL(…, Grade).
- Keywords: composite key, partial dependency, fully dependent, decomposition.
- Common wrong: calling it a transitive dependency (it's partial).

**Q26** [APP · U2-5 · P0 · 3] EMPLOYEE(EmpID, DeptID, DeptName): show the 3NF violation and fix it.
- Expected: EmpID→DeptID, DeptID→DeptName ⇒ transitive EmpID→DeptName ⇒ move to DEPARTMENT(DeptID, DeptName); remaining EMPLOYEE(EmpID, DeptID).
- Keywords: transitive dependency, non-prime attribute, separate relation.
- Common wrong: keeping DeptName because "it's convenient".

**Q27** [CMP · U2-6 · P0 · 2] 3NF vs BCNF.
- Expected: 3NF allows X→A if X is super key **or** A is prime; BCNF requires X super key **only**; BCNF stricter; 3NF usually preserves dependencies, BCNF may not.
- Keywords: OR vs ONLY, stricter, dependency preservation.
- Common wrong: "BCNF is the weaker form".

**Q28** [DEF · U2-7 · P0 · 1] Define multivalued dependency and 4NF.
- Expected: X ↠ Y when for each X value the set of Y values is independent of the remaining attributes; 4NF requires the determinant of every non-trivial MVD to be a super key.
- Keywords: independent, super key determinant.
- Common wrong: defining 4NF as "no repeating groups".

**Q29** [CMP · U2-8 · P1 · 2] 4NF vs 5NF.
- Expected: 4NF removes redundancy from independent multivalued facts; 5NF addresses complex join dependencies not captured by FDs/MVDs — lossless reconstruction through projections.
- Keywords: multivalued, join dependency, implied by candidate keys.
- Common wrong: "5NF = no redundancy at all".

**Q30** [FILL · U2-9 · P0 · 2] R(A,B,C) → R1(A,B), R2(A,C). Fill the missing test: ____ → R1 or ____ → R2.
- Expected: (R1 ∩ R2) = {A}; **A → B** (i.e. A→R1) or **A → C** (A→R2) makes it lossless.
- Keywords: intersection, functional determination of one side.
- Common wrong: testing B → A.

**Q31** [MIS · U2-10 · P1 · 2] "A lossless decomposition is always dependency preserving."
- Expected: False — the properties are independent; a decomposition may be lossless but not dependency preserving (and vice versa).
- Keywords: independent properties, enforce without joins.
- Common wrong: assuming they come together.

**Q32** [SEQ · U2-11 · P1 · 2] Order the minimal-cover steps.
- Expected: split RHS to single attributes → remove extraneous LHS attributes → remove redundant FDs → canonical cover.
- Keywords: split, extraneous, redundant.
- Common wrong: removing redundant FDs before extraneous attributes.

**Q33** [DIA · U2-13 · P0 · 2] Draw a B+ tree and explain why range queries are fast.
- Expected: internal separators + child pointers; leaves with keys + record pointers **linked**; range scan walks the leaf chain; O(log_f N) height.
- Keywords: linked leaves, fan-out, balanced, range scan.
- Common wrong: no leaf links drawn.

**Q34** [CMP · U2-14 · P0 · 2] B+ tree vs hash index.
- Expected: ordered vs unordered; equality+range vs equality only; good ORDER BY vs poor range; balanced tree vs buckets.
- Keywords: ordered, range, equality, bucket.
- Common wrong: "hash is better at everything".

**Q35** [WHY · U2-12 · P2 · 1] Why does a DBMS transfer data in pages rather than records?
- Expected: I/O cost — the buffer manager moves pages/blocks into memory and writes back; reducing page I/O is a major optimization objective.
- Keywords: pages, blocks, buffer manager, page I/O.
- Common wrong: "records are too small to find".

**Q36** [EXP · U2-12 · P2 · 1] Compare heap, sequential, hash and clustered file organizations.
- Expected: heap = unordered, frequent inserts/scans; sequential = key order, range; hash = equality; clustered = related records together.
- Keywords: unordered, key order, hash function, related records.
- Common wrong: saying heap is "sorted by insertion".

---

## UNIT 3

**Q37** [DEF · U3-1 · P0 · 1] Define transaction.
- Expected: a sequence of database operations forming one logical unit of work that must preserve correctness even under concurrency or failure.
- Keywords: logical unit of work, correctness, concurrency, failure.
- Common wrong: "a single SQL statement".

**Q38** [WHY · U3-1 · P0 · 2] Why is the bank transfer the classic transaction example?
- Expected: debit A and credit B must both happen or neither; a crash between them would otherwise leave the DB incorrect — atomicity/recovery make it all-or-nothing.
- Keywords: both or neither, crash, atomicity.
- Common wrong: only saying "money is important".

**Q39** [SEQ · U3-2 · P1 · 2] Order: ABORTED, ACTIVE, COMMITTED, FAILED, PARTIALLY COMMITTED.
- Expected: ACTIVE → PARTIALLY COMMITTED → COMMITTED; failure path: ACTIVE → FAILED → ABORTED (partially committed can also fail).
- Keywords: last statement, rollback.
- Common wrong: COMMITTED before PARTIALLY COMMITTED.

**Q40** [EXP · U3-3 · P0 · 3] Explain ACID with a bank-transfer example for each property.
- Expected: A all-or-nothing (both debit and credit); C committed state preserves constraints (no invalid account); I intermediate effects controlled ⇒ serial-equivalent (no half-transfer visible); D committed effects survive failure (still there after restart).
- Keywords: all-or-nothing, integrity constraints, serial behaviour, survive failure.
- Common wrong: giving ACID as four words only.

**Q41** [EXP · U3-4 · P1 · 2] The four isolation levels and what each prevents.
- Expected: RU may read uncommitted; RC prevents dirty reads; RR stronger repeat-read (phantoms DBMS-dependent); Serializable strongest, aims for serial equivalence.
- Keywords: dirty read, repeatable, phantom, serializable.
- Common wrong: claiming RR always prevents phantoms without a hedge (E3/E4).

**Q42** [CMP · U3-5 · P0 · 2] Non-repeatable read vs phantom read.
- Expected: same row read twice → different committed values vs same predicate → different **set** of rows (inserts/deletes).
- Keywords: same row vs row set, predicate.
- Common wrong: treating them as synonyms.

**Q43** [HOW · U3-5 · P0 · 3] Test a schedule for conflict serializability.
- Expected: nodes per transaction; edges for conflicts (same item, ≥1 write) with Ti before Tj; acyclic ⇒ conflict-serializable; cycle ⇒ not.
- Keywords: precedence graph, conflict, acyclic/cycle.
- Common wrong: drawing edges for read–read pairs.

**Q44** [DEF · U3-5 · P0 · 1] Serial vs serializable schedule.
- Expected: serial = transactions execute one after another; serializable = may interleave but the effect equals some serial schedule.
- Keywords: interleave, equivalent, serial execution.
- Common wrong: "serializable = serial".

**Q45** [DIA · U3-6 · P0 · 2] Draw the 2PL diagram with the lock point and name the phases' rules.
- Expected: growing = acquire only; lock point = last acquisition; shrinking = release only; no new acquisitions after shrinking.
- Keywords: growing, shrinking, lock point, no release while acquiring.
- Common wrong: "lock at start, unlock at end".

**Q46** [CMP · U3-6 · P0 · 2] Basic, strict and rigorous 2PL.
- Expected: basic → conflict serializability; strict → hold X locks until commit/abort (fewer cascading rollbacks); rigorous → hold S and X until completion.
- Keywords: growing/shrinking, X locks, commit/abort, cascading rollback.
- Common wrong: swapping strict and rigorous.

**Q47** [MIS · U3-6 · P1 · 2] Does 2PL prevent deadlock?
- Expected: No — two transactions can still hold one resource and wait for the other (cycle). Handle via prevention, avoidance, detection (wait-for graph), timeout.
- Keywords: cycle of waits, wait-for graph, timeout.
- Common wrong: "2PL eliminates deadlock".

**Q48** [EXP · U3-7 · P1 · 2] Timestamp ordering: rule, advantage, disadvantage.
- Expected: unique timestamps (older smaller); Read_TS/Write_TS per item; violating read/write order ⇒ abort and restart; advantage = no lock waiting ⇒ no lock-based deadlock; cost = repeated aborts waste work.
- Keywords: timestamp, abort, restart, no lock waits.
- Common wrong: "timestamps prevent all aborts".

**Q49** [EXP · U3-8 · P1 · 2] Classify failure types with one cause each.
- Expected: transaction (logical error, constraint violation, deadlock victim, abort); system crash (power/OS/DBMS process, loses volatile memory); media (disk damage, loses persistent data); communication (message/link failure, important in distributed DBs).
- Keywords: volatile vs persistent, distributed.
- Common wrong: not distinguishing crash from media failure.

**Q50** [CMP · U3-9/10 · P0 · 3] Deferred vs immediate update — write timing and recovery actions.
- Expected: deferred = DB written only after commit (REDO committed if needed; uncommitted normally no UNDO); immediate = page may be written before commit (UNDO uncommitted + REDO committed if needed).
- Keywords: after commit, before commit, undo, redo.
- Common wrong: saying deferred update needs both undo and redo.

**Q51** [HOW · U3-11 · P1 · 2] Explain shadow paging through commit and crash.
- Expected: stable shadow table + current table; updates go to new pages; commit switches root to current; crash before commit uses shadow mapping; trade-off = fragmentation/overhead.
- Keywords: stable shadow, new locations, root switch, old mapping.
- Common wrong: "shadow table is updated too".

**Q52** [FILL · U3-12 · P0 · 2] WAL: the ____ must reach ____ before the ____ is written.
- Expected: log record → stable storage → before the corresponding data page.
- Keywords: log before data, stable storage.
- Common wrong: reversing the order.

**Q53** [WHY · U3-12 · P1 · 2] Why checkpoints?
- Expected: recovery starts from a recent checkpoint instead of scanning the entire log, reducing recovery time.
- Keywords: recent point, log scanning, recovery time.
- Common wrong: "checkpoints back up the whole database".

**Q54** [HOW · U3-12 · P0 · 2] A crash occurs; T1 committed, T2 not. What does recovery do?
- Expected: start from last checkpoint; REDO T1's changes if needed; UNDO T2's changes; database consistent.
- Keywords: committed → redo, uncommitted → undo.
- Common wrong: undoing T1 or redoing T2.

---

## UNIT 4

**Q55** [DEF · U4-1 · P1 · 1] Define distributed database and DDBMS.
- Expected: one logically integrated database physically distributed across network-connected sites; DDBMS coordinates sites and gives unified access.
- Keywords: logically integrated, physically distributed, unified access.
- Common wrong: "several independent databases".

**Q56** [CMP · U4-1 · P2 · 1] Homogeneous, heterogeneous, federated.
- Expected: similar DBMS tech / different tech or schemas / independently managed DBs cooperating through integration mechanisms.
- Keywords: same tech, different tech, cooperating independent.
- Common wrong: confusing heterogeneous with federated.

**Q57** [CMP · U4-2 · P0 · 2] Horizontal vs vertical vs hybrid fragmentation.
- Expected: rows by predicate / columns with PK repeated / both combined; reconstruction by union or join.
- Keywords: rows, columns, primary key repeated, join.
- Common wrong: swapping horizontal and vertical (hook: horizontal = rows).

**Q58** [WHY · U4-2 · P1 · 2] Why repeat the primary key in a vertical fragment?
- Expected: so the original relation can be reconstructed by joining the fragments on the key.
- Keywords: reconstruction, join, key.
- Common wrong: "to save space".

**Q59** [EXP · U4-3 · P1 · 2] Benefits and costs of replication.
- Expected: benefits — availability, faster local reads, failure tolerance, less remote access; costs — storage, update coordination, consistency management, network/control overhead.
- Keywords: availability, updates coordination, consistency.
- Common wrong: listing only benefits.

**Q60** [HOW · U4-4 · P0 · 3] Explain 2PC with a diagram.
- Expected: coordinator PREPARE → participants record prepared and vote YES/NO → all YES ⇒ COMMIT else ABORT → participants record/execute; limitation = blocking when the decision is unreachable.
- Keywords: coordinator, prepare, vote, commit/abort, blocking.
- Common wrong: calling it a locking protocol.

**Q61** [EXP · U4-7 · P0 · 3] State CAP precisely and define C, A and P.
- Expected: during a network partition, cannot guarantee both strong consistency and availability for every request under the formal CAP definitions; C = read sees most recent write (or error); A = non-failing node responds non-error (not necessarily latest); P = continues despite network failures.
- Keywords: network partition, formal definitions, non-error response.
- Common wrong: "choose any two at all times" (explicitly penalised in the source).

**Q62** [CMP · U4-8 · P0 · 2] ACID vs BASE.
- Expected: ACID = atomicity/consistency/isolation/durability, strong transaction guarantees, relational systems; BASE = basically available, soft state, eventual consistency, availability/flexible consistency, distributed NoSQL.
- Keywords: transaction-oriented, eventual convergence, temporary inconsistency.
- Common wrong: "BASE means unreliable data".

**Q63** [EXP · U4-9 · P0 · 2] Sharding strategies with one strength/weakness each.
- Expected: range (good ranges/hotspots), hash (even load/no range locality), directory (flexible/extra service), geographic (locality/uneven volumes); good shard key = even spread, supports common queries, no hotspots.
- Keywords: hash of shard key, mapping service, hotspots.
- Common wrong: describing sharding as replication.

**Q64** [CMP · U4-10 · P1 · 1] Relational vs MongoDB terminology.
- Expected: table→collection, row→document, column→field, primary key→_id.
- Keywords: collection, document, field, _id.
- Common wrong: "MongoDB has no primary key".

**Q65** [APP · U4-11 · P0 · 2] Write MongoDB commands: insert two students; find those older than 21; add 1 year to all MCA students.
- Expected: insertMany([...]); find({age:{$gt:21}}); updateMany({course:'MCA'},{$inc:{age:1}}).
- Keywords: insertMany, $gt, $inc, updateMany.
- Common wrong: using SQL syntax (SELECT/UPDATE).

**Q66** [HOW · U4-12 · P0 · 2] Aggregation pipeline: total sales per product for paid orders, sorted descending.
- Expected: `{$match:{status:'paid'}}, {$group:{_id:'$product', total:{$sum:'$amount'}}}, {$sort:{total:-1}}`.
- Keywords: $match first, $group with $sum, $sort -1.
- Common wrong: putting $group before $match (performance/semantics point).

---

## UNIT 5

**Q67** [CMP · U5-1 · P0 · 2] HBase vs Cassandra (four contrasts).
- Expected: Hadoop ecosystem vs independent; row key + column families vs partition key + clustering columns; APIs/shell vs CQL; large-scale sparse data vs highly available distributed workloads.
- Keywords: Hadoop, CQL, partition key, clustering columns.
- Common wrong: "both are Hadoop databases".

**Q68** [EXP · U5-2 · P0 · 2] Cassandra's design principle and why duplication is acceptable.
- Expected: model tables around query patterns; deliberate duplication avoids expensive joins; explicit schema with ALTER TABLE must be planned cluster-wide.
- Keywords: query patterns, duplication, joins, schema metadata.
- Common wrong: applying normalization rules to Cassandra.

**Q69** [HOW · U5-11 · P0 · 3] For `PRIMARY KEY ((course), year, student_id)`, identify partition key, clustering columns and row order.
- Expected: `course` = partition key (location); `year`, `student_id` = clustering columns; rows ordered by year then student_id within each partition.
- Keywords: location vs order, within partition.
- Common wrong: treating year as a partition key (double parentheses mark the partition key).

**Q70** [APP · U5-3 · P1 · 1] Redis: store user 101 with name and course, set a TTL, increment a counter.
- Expected: HSET user:101 name 'Ravi' course 'MCA'; EXPIRE user:101 seconds; INCR counter (SET/GET for strings).
- Keywords: hash, TTL, atomic increment.
- Common wrong: using SQL INSERT.

**Q71** [EXP · U5-4 · P1 · 1] Graph data model trio + two use cases.
- Expected: nodes = entities, edges = relationships, properties = attributes; social networks/recommendations/fraud/knowledge graphs/dependency analysis.
- Keywords: nodes, edges, properties, traversal.
- Common wrong: describing tables with joins.

**Q72** [APP · U5-5 · P1 · 2] Write Cypher to create Alice, link her to Bob as FRIEND_OF, then list her friends.
- Expected: `CREATE (p:Person {name:'Alice', age:22});` … `MATCH (a:Person {name:'Alice'}), (b:Person {name:'Bob'}) CREATE (a)-[:FRIEND_OF]->(b);` … `MATCH (p:Person)-[:FRIEND_OF]->(f:Person) RETURN p.name, f.name;`
- Keywords: MATCH, square-bracket relationship, RETURN.
- Common wrong: SQL SELECT syntax.

**Q73** [DEF · U5-6 · P0 · 1] Define embedding.
- Expected: a numerical vector representation of an object produced by an embedding model; semantically similar objects are placed near each other in vector space.
- Keywords: numerical vector, embedding model, similar objects near each other.
- Common wrong: "embedding = a database".

**Q74** [CMP · U5-6 · P0 · 2] Cosine, Euclidean, dot product.
- Expected: cosine = angle/direction (semantic text retrieval); Euclidean = straight-line distance; dot = alignment + magnitude (retrieval systems).
- Keywords: angle, distance, alignment.
- Common wrong: saying cosine uses magnitude.

**Q75** [SEQ · U5-7 · P0 · 2] Order the similarity-search pipeline.
- Expected: user query → embed query → query vector → vector index → nearest neighbours/top-k → metadata + documents → results.
- Keywords: same embedding model, top-k, metadata.
- Common wrong: embedding the stored data at query time.

**Q76** [CMP · U5-7 · P0 · 2] HNSW vs IVF.
- Expected: HNSW = graph-based ANN navigating through increasingly close candidates; IVF = partitions vectors into clusters and searches only relevant groups.
- Keywords: navigable small world, graph, inverted file, clusters.
- Common wrong: swapping them.

**Q77** [EXP · U5-9 · P0 · 2] Why does compound-index field order matter? Give an example.
- Expected: order determines which query/sort patterns the index can support efficiently — e.g. index {course:1, age:-1} serves course-filtered queries and their sorts; inspect with explain().
- Keywords: query patterns, sort patterns, explain().
- Common wrong: "any order works".

**Q78** [CMP · U5-13 · P0 · 2] Traditional index vs vector index.
- Expected: exact/range access on scalar keys (B+ tree, hash; age=22, BETWEEN) vs similarity/top-k on high-dimensional vectors (HNSW, IVF).
- Keywords: nearest-neighbour, scalar keys, top-k.
- Common wrong: saying vector indexes are "B+ trees for vectors".

**Q79** [WHY · U5-14 · P1 · 2] Why do NoSQL systems need indexes, and what do they cost?
- Expected: millions/billions of records across machines ⇒ scans are expensive; indexes cut latency/CPU/memory/I/O/network; costs = storage, write overhead, cache pressure, useless if query mismatched, too many slow writes.
- Keywords: full scan, latency, write overhead, query-driven.
- Common wrong: "indexes are always free".

**Q80** [EXP · U5-8 · P1 · 2] What is ordering, and why is it relevant to index choice?
- Expected: ordering arranges records/keys by a criterion; ordered structures (B+ trees) support equality, range, prefix and sorted retrieval; hash indexes are unordered ⇒ poor for ranges.
- Keywords: ordered, range, prefix, ORDER BY.
- Common wrong: claiming hash supports ORDER BY.

---

## MIXED / CROSS-UNIT TRAPS

**Q81** [TF · mixed · P0 · 1] "CAP means you can have at most two of consistency, availability, partition tolerance." — verdict?
- Expected: **False as stated** — CAP is specifically about behaviour *during a network partition*, where strong consistency and availability cannot both be guaranteed for every request.
- Keywords: during partition, formal definitions.
- Common wrong: repeating the slogan.

**Q82** [MIS · U3/U4 · P0 · 2] 2PL vs 2PC — what does each do?
- Expected: 2PL = two-phase **locking**, concurrency control inside one DBMS (growing/shrinking); 2PC = two-phase **commit**, atomic commit across sites (prepare/commit).
- Keywords: locking vs commit, single site vs multiple sites.
- Common wrong: treating them as the same protocol.

**Q83** [CMP · U1/U5 · P0 · 2] Normalize (relational) vs deliberate duplication (Cassandra) — why the opposite advice?
- Expected: relational joins are cheap and redundancy causes anomalies; Cassandra queries must hit one partition, so tables are modelled around query patterns and duplication avoids costly distributed joins.
- Keywords: anomalies vs joins, query patterns, partition-local.
- Common wrong: "Cassandra is just badly designed".

**Q84** [TF · U2 · P1 · 1] "A candidate key must be minimal." — verdict? **True**; removing any attribute destroys uniqueness.

**Q85** [DIA · mixed · P0 · 2] Draw in 90 seconds: the recovery chain.
- Expected: LOG → CHECKPOINT → CRASH → UNDO uncommitted + REDO committed, with WAL noted as log-before-data.
- Keywords: checkpoint, undo, redo, WAL.
- Common wrong: missing checkpoint or WAL.

**Q86** [EXP · mixed · P0 · 3] "Explain how indexing improves NoSQL query performance."
- Expected: index = auxiliary access path (avoids full scans) → lower latency and resource use → per-system mechanisms: MongoDB compound indexes, CouchDB Mango/views, Cassandra partition+clustering design, Neo4j property indexes, vector HNSW/IVF → benefits + costs → query-driven conclusion.
- Keywords: auxiliary access path, per-system comparison, maintenance cost, query-driven.
- Common wrong: describing only one database (the source explicitly warns against this).

**Q87** [APP · U2 · P0 · 3] R(A,B,C,D), F = {AB→C, C→D, D→B}. Find the key and the normal form.
- Expected: (AB)⁺ = {A,B,C,D} ⇒ **AB** key; D→B is a transitive/non-prime dependency (D is non-prime, AB is the only key ⇒ C→D... D→B with D non-prime and B non-prime) ⇒ violates 3NF (and BCNF, since D is not a super key).
- Keywords: closure, prime/non-prime, transitive.
- Common wrong: declaring BCNF first without showing 3NF's failure.

**Q88** [EXP · U4 · P2 · 1] Eventual consistency: when is it acceptable?
- Expected: replicas may temporarily disagree but converge if updates stop; acceptable when availability matters more than immediate freshness (the trade-off requires more coordination for stronger consistency).
- Keywords: converge, temporary, availability trade-off.
- Common wrong: "eventual consistency = data loss".

---


## SECTION H — MCQ RAPID-FIRE (32 items, mixed units)

*External-source additions:* these 32 MCQs were recovered from `claude/ADBMS Boss Rush.html` (another AI artifact in this folder) and **verified item-by-item against `ADBMS_MasterNotes.docx`** — every answer key and explanation agrees with the master notes. Use for speed drills: answer in 30 seconds each, no working.

**Q89** [MCQ A· mixed A· P1 A· 2] Which step comes first in a 20-mark answer?
- A. Diagram
- B. Definition and intro **[KEY]**
- C. Conclusion
- D. Example
- Why: Start with a 5-7 line definition and why it matters.

**Q90** [MCQ A· mixed A· P1 A· 1] A topic has a process or architecture. What should you add?
- A. Nothing, text is enough
- B. A labelled diagram or flow **[KEY]**
- C. Only a table
- D. A longer conclusion
- Why: Diagrams are explicitly rewarded for processes, hierarchies and algorithms.

**Q91** [MCQ A· U2-4 A· P0 A· 1] R(A,B,C), key is AB, and B→C. Which normal form is violated first?
- A. 1NF
- B. 2NF **[KEY]**
- C. 3NF
- D. BCNF
- Why: C depends on only part of the key (B), which is a partial dependency, so 2NF fails.

**Q92** [MCQ A· U2-5 A· P0 A· 1] Student(ID, Dept, DeptHead) with ID→Dept and Dept→DeptHead. What is the problem?
- A. Partial dependency
- B. Transitive dependency **[KEY]**
- C. Not atomic
- D. Lossy join
- Why: ID→Dept→DeptHead is transitive, so 3NF fails.

**Q93** [MCQ A· U2-6 A· P0 A· 1] Which statement is true?
- A. Every 3NF relation is in BCNF
- B. Every BCNF relation is in 3NF **[KEY]**
- C. BCNF is weaker than 2NF
- D. 1NF allows repeating groups
- Why: BCNF is stricter than 3NF, so BCNF implies 3NF but not the reverse.

**Q94** [MCQ A· U2-1 A· P0 A· 1] R(A,B,C,D) with A→B and B→C. What is A+?
- A. {A}
- B. {A,B}
- C. {A,B,C} **[KEY]**
- D. {A,B,C,D}
- Why: A gives B, B gives C, and nothing gives D, so A+ is {A,B,C}.

**Q95** [MCQ A· U2-9 A· P1 A· 1] When is a binary decomposition R1, R2 lossless?
- A. Common attribute set is a key of R1 or R2 **[KEY]**
- B. R1 and R2 share no attributes
- C. Both are in 1NF
- D. It has fewer tables
- Why: Intersection must be a super key of at least one part.

**Q96** [MCQ A· U2-9 A· P1 A· 1] Which normal form decomposition always preserves dependencies AND is lossless?
- A. BCNF
- B. 3NF **[KEY]**
- C. 2NF
- D. 4NF
- Why: 3NF synthesis guarantees both; BCNF may lose dependencies.

**Q97** [MCQ A· U3-3 A· P0 A· 1] Power cut right after COMMIT, but the data is still there after restart. Which property?
- A. Atomicity
- B. Consistency
- C. Isolation
- D. Durability **[KEY]**
- Why: Committed changes surviving failure is durability.

**Q98** [MCQ A· U3-3 A· P0 A· 1] Debit succeeded, credit failed, so the debit is undone. Which property?
- A. Atomicity **[KEY]**
- B. Isolation
- C. Durability
- D. Consistency
- Why: All-or-nothing is atomicity.

**Q99** [MCQ A· U3-3 A· P0 A· 1] Which component mainly ensures Isolation?
- A. Recovery manager
- B. Concurrency control **[KEY]**
- C. Buffer manager
- D. Query optimizer
- Why: Locking or timestamps give isolation.

**Q100** [MCQ A· U3-5 A· P0 A· 1] A precedence graph contains a cycle. The schedule is...
- A. Conflict serializable
- B. Not conflict serializable **[KEY]**
- C. Always recoverable
- D. Serial
- Why: A cycle means no equivalent serial order exists.

**Q101** [MCQ A· U3-6 A· P0 A· 1] In 2PL, what is forbidden after the first unlock?
- A. Reading
- B. Acquiring new locks **[KEY]**
- C. Committing
- D. Unlocking
- Why: Once shrinking starts, no new locks.

**Q102** [MCQ A· U3-6 A· P1 A· 1] Deadlock is detected using...
- A. Precedence graph
- B. Wait-for graph **[KEY]**
- C. B+ tree
- D. Shadow table
- Why: A cycle in the wait-for graph means deadlock.

**Q103** [MCQ A· U4-7 A· P0 A· 1] During a partition, a system keeps answering with possibly stale data. It chose...
- A. CP
- B. AP **[KEY]**
- C. CA
- D. ACID
- Why: Availability over consistency is AP.

**Q104** [MCQ A· U4-8 A· P0 A· 1] What does the S in BASE stand for?
- A. Strong
- B. Soft state **[KEY]**
- C. Serializable
- D. Sharded
- Why: Soft state: data may change without input as replicas converge.

**Q105** [MCQ A· U4-9 A· P1 A· 1] Hash sharding mainly helps with...
- A. Range queries
- B. Even data distribution **[KEY]**
- C. Joins
- D. Foreign keys
- Why: Hashing spreads keys evenly, but range queries get harder.

**Q106** [MCQ A· U4-2 A· P0 A· 1] How is a vertically fragmented table rebuilt?
- A. UNION
- B. JOIN on the key **[KEY]**
- C. Intersection
- D. Cartesian product
- Why: Each fragment keeps the key so a join reconstructs the table.

**Q107** [MCQ A· U4-4 A· P0 A· 1] In 2PC, one participant votes NO. Result?
- A. Commit
- B. Global abort **[KEY]**
- C. Ignore it
- D. Retry later only for that site
- Why: Any NO vote forces a global abort.

**Q108** [MCQ A· U4-4 A· P1 A· 1] Main drawback of 2PC?
- A. No atomicity
- B. Blocking if coordinator fails **[KEY]**
- C. Too many tables
- D. No logging
- Why: Participants can be stuck waiting for the coordinator decision.

**Q109** [MCQ A· U2-13 A· P0 A· 1] Query: salary BETWEEN 30000 AND 50000. Best index?
- A. Hash
- B. B+ tree **[KEY]**
- C. No index
- D. Bitmap on name
- Why: Linked sorted leaves make ranges fast.

**Q110** [MCQ A· U2-13 A· P0 A· 1] Main downside of indexes?
- A. Slower reads
- B. Extra storage and write overhead **[KEY]**
- C. Data loss
- D. No ordering
- Why: Every write must also update the index.

**Q111** [MCQ A· U3-9 A· P0 A· 1] Which recovery scheme never needs UNDO?
- A. Deferred update **[KEY]**
- B. Immediate update
- C. Both
- D. Neither
- Why: Nothing uncommitted ever reaches the database.

**Q112** [MCQ A· U3-12 A· P0 A· 1] WAL means...
- A. Data page first, log later
- B. Log first, then data page **[KEY]**
- C. Lock then write
- D. Write all later
- Why: Log before data is what makes undo and redo possible.

**Q113** [MCQ A· U5-4 A· P1 A· 1] Best store for friend-of-friend recommendations?
- A. Redis
- B. Neo4j **[KEY]**
- C. Cassandra
- D. MongoDB
- Why: Relationship traversal is the graph database sweet spot.

**Q114** [MCQ A· U4-11 A· P0 A· 1] Which command finds docs with age over 20 in MongoDB?
- A. SELECT age>20
- B. db.users.find({age:{$gt:20}}) **[KEY]**
- C. GET age
- D. MATCH (age)
- Why: $gt is the MongoDB greater-than operator.

**Q115** [MCQ A· U4-12 A· P0 A· 1] Which stage should usually come first to cut data early?
- A. $sort
- B. $match **[KEY]**
- C. $group
- D. $limit after group
- Why: Filtering first shrinks the data every later stage touches.

**Q116** [MCQ A· U5-7 A· P0 A· 1] Which measure compares the angle between two vectors?
- A. Hamming
- B. Cosine similarity **[KEY]**
- C. Manhattan time
- D. Jaccard rows
- Why: Cosine similarity is based on the angle.

**Q117** [MCQ A· U5-6 A· P0 A· 1] HNSW is mainly used for...
- A. Exact joins
- B. Approximate nearest neighbour search **[KEY]**
- C. Locking
- D. Sharding
- Why: It is a graph index for fast approximate similarity search.

**Q118** [MCQ A· U1-5 A· P0 A· 1] How is an M:N relationship mapped?
- A. FK on either side
- B. Separate junction table **[KEY]**
- C. Merge the entities
- D. Ignore it
- Why: A new table holds the keys of both entities.

**Q119** [MCQ A· U1-7 A· P0 A· 1] GRANT and REVOKE belong to...
- A. DDL
- B. DML
- C. DCL **[KEY]**
- D. TCL
- Why: They control access, so Data Control Language.

**Q120** [MCQ A· U1-8 A· P0 A· 1] Entity integrity means...
- A. FK must match
- B. Primary key cannot be null **[KEY]**
- C. Values are unique across tables
- D. Every table has an index
- Why: No primary key attribute may be null.

---

## SECTION I — MCQ CROSS-CHECK SET (22 items)

*External-source additions:* these 22 MCQs were recovered from `chatgpt/adbms-papermorph/` (another AI artifact over the same source notes) and **verified item-by-item against `ADBMS_MasterNotes.docx`** — every answer key agrees with the source. Each carries the original `whyWrong` distractor explanation so you learn why the other options fail.

**Q121** [MCQ A· U1-3 A· P0 A· 1] Which level hides physical storage details from end users?
- A. External **[KEY]**
- B. Conceptual
- C. Internal
- D. Storage device
- Why: External level provides customized user views.
- Why not: Internal level is where physical representation is described.

**Q122** [MCQ A· U1-2 A· P1 A· 1] Schema means…
- A. Current data values
- B. Database blueprint/structure **[KEY]**
- C. Only indexes
- D. Only user views
- Why: Schema is the relatively stable logical design.
- Why not: Current values are the instance.

**Q123** [MCQ A· U1-5 A· P0 A· 1] For a 1:N relationship, where does the 1-side primary key usually go?
- A. Into the 1-side as a duplicate
- B. As a foreign key in the N-side relation **[KEY]**
- C. Into a brand-new relation always
- D. It is discarded
- Why: The 1-side key becomes a foreign key in the N-side.
- Why not: A new table is specifically typical for M:N, not ordinary 1:N.

**Q124** [MCQ A· U1-5 A· P1 A· 1] A multivalued attribute is usually mapped by…
- A. Repeating columns
- B. One big text field
- C. A separate relation with owner key + value **[KEY]**
- D. Deleting the attribute
- Why: That keeps values addressable and relationally structured.
- Why not: Repeating columns destroy the clean relational design.

**Q125** [MCQ A· U1-7 A· P0 A· 1] Which clause filters groups after GROUP BY?
- A. WHERE
- B. HAVING **[KEY]**
- C. ORDER BY
- D. LIMIT
- Why: HAVING filters groups.
- Why not: WHERE filters rows before grouping.

**Q126** [MCQ A· U1-8 A· P0 A· 1] Entity integrity requires primary-key values to be…
- A. Nullable and duplicated
- B. Unique and non-NULL **[KEY]**
- C. Sorted
- D. Encrypted
- Why: A primary key identifies tuples and cannot be NULL.
- Why not: Sorting/encryption are unrelated to entity integrity.

**Q127** [MCQ A· U2-4 A· P0 A· 1] What does 2NF mainly remove?
- A. Non-atomic values
- B. Partial dependencies **[KEY]**
- C. Transitive dependencies
- D. Join dependencies
- Why: 2NF attacks partial dependency on part of a composite key.
- Why not: 3NF is the transitive-dependency stage.

**Q128** [MCQ A· U2-6 A· P0 A· 1] BCNF requires…
- A. Every determinant is a super key **[KEY]**
- B. Every table has two keys
- C. All attributes are atomic
- D. No foreign keys
- Why: That is the memorization sentence from the notes.
- Why not: Atomicity is 1NF, not BCNF.

**Q129** [MCQ A· U2-13 A· P0 A· 1] Which index is naturally suited to a range query?
- A. Hash index
- B. B+ tree **[KEY]**
- C. No index ever
- D. Only a graph index
- Why: B+ trees maintain order and linked leaves.
- Why not: Hash buckets are not naturally ordered.

**Q130** [MCQ A· U2-14 A· P1 A· 1] A hash collision occurs when…
- A. A key is missing
- B. Two keys map to the same bucket **[KEY]**
- C. The tree becomes unbalanced
- D. A page is empty
- Why: Two different keys can map to the same bucket.
- Why not: Unbalanced trees are not the hash collision concept.

**Q131** [MCQ A· U3-3 A· P0 A· 1] Which ACID property says a transaction is all-or-nothing?
- A. Consistency
- B. Atomicity **[KEY]**
- C. Isolation
- D. Durability
- Why: Atomicity is the all-or-nothing property.
- Why not: Consistency is about valid state and constraints.

**Q132** [MCQ A· U3-6 A· P0 A· 1] Which 2PL phase forbids acquiring new locks?
- A. Growing
- B. Shrinking **[KEY]**
- C. Lock point
- D. Commit
- Why: Shrinking phase releases locks and acquires no new locks.
- Why not: Growing phase is the acquisition phase.

**Q133** [MCQ A· U3-12 A· P0 A· 1] WAL requires…
- A. Data page first, log later
- B. Log record first, then changed data page **[KEY]**
- C. No log
- D. Only checkpoints
- Why: Write-Ahead Logging writes the log to stable storage before the corresponding changed page.
- Why not: That is the core WAL guarantee.

**Q134** [MCQ A· U4-2 A· P0 A· 1] Vertical fragmentation divides…
- A. Rows
- B. Columns **[KEY]**
- C. Databases
- D. Transactions
- Why: Vertical = columns, usually keeping the key for reconstruction.
- Why not: Horizontal fragmentation divides rows.

**Q135** [MCQ A· U4-4 A· P0 A· 1] In 2PC, who sends PREPARE?
- A. Each participant to coordinator
- B. Coordinator to participants **[KEY]**
- C. The database user
- D. The storage manager
- Why: Coordinator starts the prepare round.
- Why not: Participants answer the prepare request with votes.

**Q136** [MCQ A· U4-7 A· P0 A· 1] CAP trade-off is specifically about…
- A. Normal operation only
- B. A network partition **[KEY]**
- C. Primary keys
- D. SQL joins
- Why: CAP concerns the trade-off during network partition.
- Why not: Partition is the condition that triggers the theorem’s trade-off.

**Q137** [MCQ A· U4-10 A· P1 A· 1] In MongoDB, a table maps most closely to…
- A. Document
- B. Field
- C. Collection **[KEY]**
- D. _id
- Why: Table → collection.
- Why not: Document maps to row.

**Q138** [MCQ A· U5-1 A· P0 A· 1] In Cassandra, the partition key primarily determines…
- A. The graph traversal
- B. Where the data/partition lives **[KEY]**
- C. The JSON field name
- D. The vector embedding
- Why: Partition key chooses the partition/location.
- Why not: Clustering columns govern order within a partition.

**Q139** [MCQ A· U5-6 A· P0 A· 1] HNSW is best described as…
- A. A graph-based ANN technique **[KEY]**
- B. A SQL isolation level
- C. A hash collision strategy
- D. A MongoDB CRUD command
- Why: HNSW is a graph-based approximate nearest-neighbor technique.
- Why not: The other options belong to unrelated topics.

**Q140** [MCQ A· mixed A· P1 A· 1] Which sentence is the safest opening for a 20-mark answer?
- A. Jump straight to an example
- B. Define the concept and explain why it matters **[KEY]**
- C. List 20 keywords only
- D. Start with the conclusion
- Why: The notebook explicitly recommends a 5–7 line definition + importance introduction.
- Why not: A list alone does not show WHAT, WHY, HOW and WHERE.

**Q141** [MCQ A· mixed A· P1 A· 1] What should a strong 20-mark answer contain besides definitions?
- A. Only code
- B. Diagram/flow, components, example, trade-offs and conclusion **[KEY]**
- C. Only a comparison table
- D. Only advantages
- Why: That structure is the notebook’s exam-writing guidance.
- Why not: Definitions alone are insufficient.

**Q142** [MCQ A· mixed A· P0 A· 1] Which pair is correctly matched?
- A. 4NF → join dependency
- B. 5NF → multivalued dependency
- C. 2NF → partial dependency **[KEY]**
- D. BCNF → atomic values
- Why: 2NF removes partial dependency.
- Why not: 4NF is MVD; 5NF is JD; 1NF is atomicity; BCNF is determinant super key.

---

## SECTION J — CROSS-UNIT COMBINED QUESTIONS (8 items, `connect me` set)

*Blockchain-prompt pattern: real 10-mark papers recombine topics across units. Each item forces two+
chapters in one answer. Answer with the 10-mark voice (`answer-voices.md` §1): intro → core (one
sub-heading per unit involved) → analysis → conclusion.*

**Q143** [EXP · U2+U5 · P0 · 3] "Indexing improves query performance" — prove it once for B+ trees and once for a NoSQL store, then state the common cost.
- Expected: B+ tree = sorted linked leaves → range without full scan · Cassandra/MongoDB = partition/clustering or compound index → same avoidance · common cost = storage + slower writes + maintenance.
- Keywords: auxiliary access path, full scan avoided, per-system mechanism, write overhead.
- Common wrong: describing only one system (the source explicitly warns against this).

**Q144** [EXP · U3+U4 · P0 · 3] A distributed transfer must be atomic AND durable. Combine 2PC with WAL to show how.
- Expected: 2PC prepare→vote→decision gives atomicity across sites (any NO → global abort) · WAL (log-before-data) at each participant gives durability across crashes · failure cases: coordinator death = blocking; participant crash = recover from log.
- Keywords: global abort, log-before-data, blocking drawback, per-site recovery.
- Common wrong: claiming 2PC alone survives crashes (it needs the log); mixing 2PL with 2PC.

**Q145** [APP · U1+U2 · P0 · 2] Map this scenario to tables, then normalize to BCNF: "A college (ID, name) has departments (dept code, head); each student (roll, name) belongs to one department and takes many courses (code, title)."
- Expected: entities + M:N student–course → junction table; 1:N dept FKs · FDs: roll→…, dept→head (transitive via student? show closure) → 3NF/BCNF decomposition with lossless check.
- Keywords: junction table, FK on N side, transitive dependency, lossless check.
- Common wrong: FK on the 1-side; stopping at 3NF without the BCNF determinant test.

**Q146** [EXP · U2+U3 · P1 · 3] Lossless-join decomposition vs serializable schedules: what is each "preserving", and what test decides each?
- Expected: lossless = no spurious tuples on reconstruct (intersection = super key of one part) · serializability = isolation/correctness under concurrency (precedence graph acyclic) · both are "does the decomposition/reordering preserve the original meaning" tests, one for data, one for execution.
- Keywords: spurious tuples, acyclic, reconstruct, equivalent serial order.
- Common wrong: calling a schedule "lossless" or a decomposition "serializable".

**Q147** [EXP · U3+U4 · P0 · 2] Isolation levels vs BASE/eventual consistency: when does each apply and what does each sacrifice?
- Expected: isolation levels = single-DB concurrency (sacrifice concurrency for correctness, up to Serializable) · BASE = distributed availability (sacrifice immediate consistency, converge later) · Serializable ≈ strongest single-node; AP ≈ availability-first distributed.
- Keywords: single-node vs distributed, converge, partition condition.
- Common wrong: "eventual consistency = data loss"; applying CAP to one machine.

**Q148** [APP · U4+U5 · P1 · 2] Choose stores for: (a) user sessions, (b) product catalog with flexible fields, (c) "similar items", (d) friend recommendations. One line of justification each.
- Expected: (a) Redis + TTL · (b) MongoDB documents · (c) vector store, cosine angle, HNSW/IVF · (d) Neo4j graph traversal.
- Keywords: TTL, flexible schema, embedding, traversal.
- Common wrong: one store for everything; Cassandra for (d).

**Q149** [EXP · U1+U3 · P1 · 2] Entity integrity + referential integrity vs ACID consistency: who enforces what, and when?
- Expected: integrity constraints = schema-level rules checked per statement (PK NOT NULL/unique; FK must match) · ACID consistency = transaction-level valid-state preservation (rules hold before AND after) · constraints are the mechanism, consistency is the guarantee; concurrency control + constraints together guard C.
- Keywords: per-statement vs per-transaction, mechanism vs guarantee.
- Common wrong: "consistency = uniform data"; confusing C with isolation.

**Q150** [EXP · U2+U4 · P1 · 3] Horizontal fragmentation cuts rows; 2NF removes partial dependencies. Explain why both are "put each fact where it belongs" operations — and how you rebuild what each splits.
- Expected: fragmentation = physical distribution (rows by predicate, UNION to rebuild) · normalization = logical design (facts depend on the whole key, JOIN to rebuild) · both eliminate redundancy/duplication of responsibility; rebuild operators differ (UNION vs JOIN-on-key).
- Keywords: physical vs logical, UNION, JOIN on key, redundancy.
- Common wrong: rebuilding fragments with JOIN on non-key columns; calling normalization "fragmentation".

---

## SECTION K — P0 GAP-CLOSE SET (5 items)

*Added by coverage audit: P0/P1 chapters with text + drill coverage but no direct written question.
Same format, same voices.*

**Q151** [EXP · U3-9 · P0 · 2] Deferred update: how does it work, and why is REDO enough after a crash?
- Expected: writes go to log records only; DB untouched until COMMIT, then REDO/applies updates → durable · crash: committed may need REDO; uncommitted need no DB UNDO (nothing uncommitted ever reached the disk).
- Keywords: log first, deferred, REDO-only, no UNDO.
- Common wrong: "deferred needs UNDO too" / skipping the log-then-commit order.

**Q152** [EXP · U3-10 · P0 · 2] Immediate update: what reaches the disk before commit, and what must recovery do?
- Expected: log old/new values; data page may be written before commit · crash: UNDO uncommitted AND REDO committed-that-may-not-have-reached-disk · WAL (log-before-data) is what makes both possible.
- Keywords: old/new values, UNDO + REDO, WAL.
- Common wrong: REDO-only (that's deferred); writing data before the log record.

**Q153** [EXP · U4-6 · P0 · 2] Name the four NoSQL models with one use-case each.
- Expected: Document = JSON/BSON (catalogs, content, profiles) · Key-value = cache/sessions/lookups · Column-family = partitioned rows + flexible columns (large distributed workloads) · Graph = nodes+relationships+properties (social, recommendations, fraud).
- Keywords: flexible schema, scale/throughput, one use-case per model.
- Common wrong: "NoSQL = no schema" (Cassandra has explicit schemas); one store for everything.

**Q154** [EXP · U4-5 · P1 · 2] Strong vs eventual consistency: what does each guarantee, and what does stronger cost?
- Expected: strong/linearizable = single real-time-respecting order · eventual = replicas may temporarily disagree but converge if updates stop · causal/session in between · stronger ⇒ more coordination ⇒ higher latency / lower availability during failures.
- Keywords: converge, coordination cost, availability trade-off.
- Common wrong: "eventual consistency = data loss/broken data" (it is deliberate).

**Q155** [EXP · U5-12 · P1 · 2] What are Neo4j indexes for, and when do they pay off?
- Expected: indexes on properties locate starting nodes fast (e.g. Person(name)); traversal then follows relationships instead of scanning · pay off when the initial lookup is selective · ordering via ORDER BY in Cypher.
- Keywords: starting nodes, traversal not scan, selective lookup.
- Common wrong: indexing every property blindly; confusing graph traversal with relational joins.

**Q156** [EXP · U5-10 · P2 · 1] CouchDB: what are Mango indexes and map/reduce views for?
- Expected: HTTP/REST document DB · Mango indexes serve selector queries · map/reduce views build indexed key/value structures where key ordering gives range-style access · point (source): indexes avoid repeatedly scanning all documents.
- Keywords: Mango, selector queries, key ordering, avoid full scans.
- Common wrong: confusing Mango with MongoDB aggregation; claiming CouchDB has no indexing.

---

## Answer-quality checklist (apply to every written answer)
- [ ] Definition first, in source wording
- [ ] Diagram or flow where one exists
- [ ] Headings per component
- [ ] A concrete example (relation / query / transaction / scenario)
- [ ] Advantages **and** limitations where relevant
- [ ] Commands quoted for MongoDB/Cassandra/Redis/Neo4j questions
- [ ] Conclusion tied to correctness / performance / scalability / reliability
