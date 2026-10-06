# write-memorize-skip.md — Tier-S Top 10, per-Topic Boxes

*Format stolen from both previous builds: every Red topic gets three boxes.
**WRITE** = the minimal scoring skeleton + suggested chunking. **MEMORIZE** = the exact
words/labels/anchors. **SKIP** = what earns zero — never spend budget there.
Voices, verbs and budgets live in `answer-voices.md`; hooks in `memory-hooks.md`.*

---

## 1. ACID (U3-3)

- **WRITE:** opener "A transaction is one logical unit of work (e.g. bank transfer: debit A + credit B succeed or fail together)." → A/C/I/D each under own heading with one transfer example → isolation-level ladder → closer tying recovery (A,D) vs concurrency control (I). Chunk (20): 2+8+4+3+3.
- **MEMORIZE:** "All-or-nothing, correct state, isolated, durable after commit." States: Active → Partially Committed → Committed; Failed → Aborted. "Recovery guards A and D; concurrency control guards I."
- **SKIP:** histories of who invented ACID; engine internals beyond lock/log one-liners.

## 2. Normalization ladder 1NF→5NF (U2-1→11)

- **WRITE:** opener with X→Y + closure one-liner → ladder as numbered tests (atomic → whole-key → no-transitive → determinant-superkey → no-bad-MVD → no-JD) → one worked relation per violated level → lossless/preservation check → anomalies-cured closer. Chunk (20): 2+3+8+4+3.
- **MEMORIZE:** "The key (1NF), the WHOLE key (2NF), nothing but the key (3NF), so help me Codd (BCNF)." 3NF = super-key-OR-prime; BCNF = super-key-ONLY. Lossless test: intersection is a super key of one part. Minimal cover: split RHS → shrink LHS → shed redundant.
- **SKIP:** proving Armstrong axioms; 4NF/5NF beyond one line each (sample never passed BCNF in depth).

## 3. CAP theorem (U4-7)

- **WRITE:** opener with the EXACT condition ("during a network partition, at most two of three") → C/A/P each with the notes' guarantee (C: every read gets the latest write **or an error**) → CP-vs-AP with one scenario each → BASE bridge → closer. Chunk (20): 2+3+8+4+3.
- **MEMORIZE:** "P is not optional, so choose C or A." Never write "any two at all times" — the #1 wrong answer in the subject.
- **SKIP:** formal impossibility proof; PACELC extensions.

## 4. 2PL + locks + deadlock (U3-6)

- **WRITE:** S vs X lock table (X conflicts with everything) → growing/shrinking diagram → "guarantees serializability, may deadlock" → wait-for-graph detection + victim-abort cure → closer. Chunk (10): 1+4+3+1+1.
- **MEMORIZE:** "Grow = grab, shrink = surrender, never regrow." Cycle in wait-for graph = deadlock. **2PL ≠ 2PC.**
- **SKIP:** strict/rigorous 2PL variants beyond naming; timestamp-rule internals (one contrast line only).

## 5. Recovery chain (U3-9→12)

- **WRITE:** failure types (transaction / system / disk+communication) → deferred vs immediate vs shadow table → WAL rule + checkpoint bounding → UNDO/REDO decision per scheme → closer. Chunk (20): 2+8+4+4+2.
- **MEMORIZE:** "Deferred = Delay → REDO only. Immediate = I need both → UNDO + REDO." WAL = log record reaches stable storage BEFORE the data page. Checkpoint = recovery starts here, not at time zero.
- **SKIP:** ARIES internals; fuzzy-checkpoint algorithms.

## 6. Conflict serializability (U3-5)

- **WRITE:** conflicting-pair definition → build-the-graph steps on the given schedule → cycle verdict → equivalent serial order if acyclic → closer. Chunk (10): 1+4+3+1+1.
- **MEMORIZE:** "Cycle = not conflict serializable." Conflicts only on same item with at least one write.
- **SKIP:** view serializability beyond one contrast line; precedence of predicate locks.

## 7. B+ tree indexing (U2-13)

- **WRITE:** structure (sorted, data in linked leaves) → search/insert walk-through → why ranges fly → B+ vs hash table → index-cost closer. Chunk (10): 1+4+3+1+1.
- **MEMORIZE:** "B for Between (ranges); H for Has-exactly (equality)." Order/fanout one-liner. Indexes speed reads, slow writes.
- **SKIP:** B-tree vs B+ split algorithms in code-level detail; bulkload math.

## 8. ER → relational mapping (U1-4/5)

- **WRITE:** scenario → ER diagram (entities/attributes/keys/cardinality) → the 7 mapping rules applied one by one → final schema with PK/FK marked → closer. Chunk (10): 1+4+3+1+1.
- **MEMORIZE:** "Many gets the key (FK on the N side). M:N needs a middleman table." Cardinality = how many; participation = mandatory-or-optional.
- **SKIP:** EER (subclass/specialization) beyond recognition; min-max notation variants.

## 9. Fragmentation + 2PC + sharding (U4-2/4/9)

- **WRITE:** horizontal (σ rows) vs vertical (π columns, key kept) + rebuild (UNION / JOIN-on-key) → replication motive/cost → 2PC prepare→vote→decision with NO-means-abort → sharding strategies → blocking-drawback closer. Chunk (20): 2+3+8+4+3.
- **MEMORIZE:** "Hand out Rows; Vertical slices of Columns. 2PC = Prepare, then Commit." Any NO vote → global abort.
- **SKIP:** 3PC; replica-consistency protocols beyond naming.

## 10. Cross-system indexing (U5-8→14)

- **WRITE:** "index = auxiliary access path" opener → per-system mechanism (MongoDB compound, Cassandra partition+clustering, Neo4j property, vector HNSW/IVF) → benefits+costs → query-driven closer. Chunk (10): 1+4+3+1+1. (The source explicitly warns: never describe only one database.)
- **MEMORIZE:** "Partition = place, clustering = order. HNSW = graph, IVF = clusters. Cosine = angle." `$match` first.
- **SKIP:** CouchDB beyond one line (P2); HNSW layer math.
