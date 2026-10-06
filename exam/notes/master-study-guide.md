# master-study-guide.md — ADBMS Exam System Index & Priority Map

**Source of truth:** `ADBMS_MasterNotes.docx` (36 pp., 5 units, 61 chapters) — corroborated by
`ADBMS_MemorizationSheet.docx`. Neither file was modified.
**Structure:** `exam/sections.json` (machine-readable map) · `exam/structure.md` (UNIT→CHAPTER→TOPIC with page refs).
**Papermorph role:** cloned to `_papermorph/`; its `outline.py`/`split_pages.py` pipeline was adapted for a
DOCX source (heading tree → sections → per-section text with page anchors) because this material is a DOCX,
not a PDF with bookmarks (`_source/build_sections.py`, `_source/extract_pages.py`).

---

## 1. What was processed

| Item | Count |
|---|---|
| Units | **5** |
| Chapters (Heading-2 sections) | **61** (+ 5 back-matter blocks: answer bank, diagram sheet, final revision, checklist, intro) |
| Topics/subtopics (Heading-3) | **61** |
| Tables extracted | **25** (master) + 24 (memorisation sheet) |
| Diagrams catalogued | **20** (11 required + 9 supporting) |
| Priority P0 chapters | **35** · P1 = 24 · P2 = 2 · P3 = 0 |

---

## 2. Priority map — every chapter

### UNIT 1 — Database System Concepts & Conceptual Modeling (pp. 2–8)
| # | Chapter | Page | P | Why |
|---|---|---|---|---|
| 1 | Introduction to Database Systems | 2 | P1 | definitions + problem/cure table = easy 5-marks |
| 2 | Data Models, Schemas and Instances | 3 | P1 | schema vs instance is a standard 2/5-mark |
| 3 | Levels of Data Abstraction | 4 | **P0** | 3-level diagram + two independences = near-certain question |
| 4 | Conceptual Modeling (ER) | 5 | **P0** | ER diagram questions; keys/cardinality/participation |
| 5 | Mapping ER → Relational | 6 | **P0** | 7 numbered rules = classic 10-mark |
| 6 | Overview of Relational Model | 6–7 | P1 | vocabulary + algebra (σ/π trap) |
| 7 | SQL — DDL/DML/DCL/TCL | 7 | **P0** | command categories + clause order, guaranteed marks |
| 8 | Integrity & Referential Constraints | 7 | **P0** | 3 named constraints + SQL, common 5-mark |
| 9 | Schema Design Guidelines & Anomalies | 8 | P1 | anomalies → bridge into normalization |

### UNIT 2 — Normalization, Data Storage & Indexing (pp. 9–14)
| # | Chapter | Page | P | Why |
|---|---|---|---|---|
| 1 | Functional Dependencies | 9 | **P0** | closure is a computational 10-mark |
| 2 | Normalization — Need & Goals | 10 | **P0** | the ladder diagram |
| 3 | 1NF | 10 | **P0** | definition + atomic example |
| 4 | 2NF | 10 | **P0** | ENROLL worked example (canonical) |
| 5 | 3NF | 11 | **P0** | EMPLOYEE worked example (canonical) |
| 6 | BCNF | 11 | **P0** | "every determinant is a super key" |
| 7 | MVD & 4NF | 11 | P1 | part of the 20-mark normalization answer |
| 8 | Join Dependencies & 5NF | 12 | P1 | 4NF vs 5NF distinction |
| 9 | Lossless Join Decomposition | 12 | **P0** | testable rule, common 5/10-mark |
| 10 | Dependency Preservation | 12 | P1 | the "independent properties" trap |
| 11 | Minimal Cover & FD Equivalence | 12 | P1 | ordered 4-step algorithm |
| 12 | Data Storage, Disk, Blocks | 12 | P2 | background for indexing answers |
| 13 | B+ Tree Indexing | 13 | **P0** | diagram + complexity + range scans |
| 14 | Hash-Based Indexing | 14 | P1 | comparison partner of B+ tree |

### UNIT 3 — Transactions, Concurrency & Recovery (pp. 15–21)
| # | Chapter | Page | P | Why |
|---|---|---|---|---|
| 1 | Concept of a Transaction | 15 | **P0** | opens the biggest 20-mark answer |
| 2 | Transaction States | 15 | P1 | state diagram component |
| 3 | ACID | 16 | **P0** | source: "one of the highest-value topics" |
| 4 | SQL Transaction Support & Isolation Levels | 16 | P1 | commands + level table |
| 5 | Concurrency Control & Serializability | 17–18 | **P0** | anomalies + precedence-graph algorithm |
| 6 | Lock-Based Control & 2PL | 18 | **P0** | 2PL diagram + deadlock handling |
| 7 | Timestamp-Based Control | 18 | P1 | pro/con short answer |
| 8 | Recovery & Failure Types | 19 | P1 | classification for the recovery answer |
| 9 | Deferred Update | 19 | **P0** | UNDO/REDO logic |
| 10 | Immediate Update | 20 | **P0** | contrast with deferred |
| 11 | Shadow Paging | 20 | P1 | third recovery technique |
| 12 | Log-Based Recovery, WAL, Checkpoint | 20–21 | **P0** | WAL rule is a must-quote |

### UNIT 4 — Distributed Databases & NoSQL (pp. 22–27)
| # | Chapter | Page | P | Why |
|---|---|---|---|---|
| 1 | Introduction to Distributed Databases | 22 | P1 | definition + characteristics + types |
| 2 | Data Fragmentation | 22 | **P0** | horizontal/vertical/hybrid + example |
| 3 | Replication and Allocation | 23 | P1 | benefits/costs table = 5 marks |
| 4 | Distributed Transactions / 2PC | 23 | **P0** | ordered protocol + diagram |
| 5 | Consistency Models | 24 | P1 | strong/eventual/causal/session |
| 6 | NoSQL Systems — Types | 24 | **P0** | four models table = frequent 5-mark |
| 7 | CAP Theorem | 25 | **P0** | highest-trap topic; exact wording required |
| 8 | BASE vs ACID | 25 | **P0** | classic comparison |
| 9 | Sharding & Partitioning | 26 | **P0** | strategies + shard-key criteria |
| 10 | MongoDB Data Model | 26 | P1 | mapping table |
| 11 | MongoDB CRUD | 26–27 | **P0** | commands examiners can demand |
| 12 | MongoDB Aggregation | 27 | **P0** | pipeline order + worked example |

### UNIT 5 — NoSQL Stores, Indexing & Ordering (pp. 28–33)
| # | Chapter | Page | P | Why |
|---|---|---|---|---|
| 1 | Column-Oriented: HBase & Cassandra | 28 | **P0** | comparison table + data model |
| 2 | Cassandra Basic Operations | 29 | P1 | CQL + query-pattern design principle |
| 3 | Redis | 29 | P1 | command recall (2/5-mark) |
| 4 | Graph Databases & Graph Model | 30 | P1 | nodes/edges/properties + use cases |
| 5 | Neo4j & Cypher | 30 | P1 | command patterns + multi-hop strength |
| 6 | Vector Databases & Embeddings | 31 | **P0** | modern topic, definitional marks |
| 7 | Similarity Search | 31 | **P0** | pipeline + ANN vs brute force |
| 8 | Indexing & Ordering Data Sets | 32 | **P0** | the index trade-off principle |
| 9 | MongoDB Indexing | 32 | **P0** | compound-order rule + explain() |
| 10 | CouchDB Indexing | 32 | P2 | Mango/views (one comparison row) |
| 11 | Cassandra Indexing & Ordering | 33 | **P0** | partition vs clustering (high-frequency) |
| 12 | Neo4j Indexing | 33 | P1 | starting-node index idea |
| 13 | Vector Store Indexing | 33 | **P0** | traditional vs vector table |
| 14 | Importance of Indexes for NoSQL | 33 | P1 | benefits/costs + the "compare all five" rule |

### 🔴 Tier-S — if you can only study 10 topics
1. ACID (U3-3) · 2. Normalization ladder 1NF→5NF (U2-2…8) · 3. CAP (U4-7) · 4. 2PL (U3-6) ·
5. Recovery: deferred/immediate/shadow/log/WAL (U3-9…12) · 6. Conflict serializability (U3-5) ·
7. B+ tree (U2-13) · 8. ER→relational mapping (U1-5) · 9. 2PC + fragmentation (U4-2,4) ·
10. Indexing across MongoDB/Cassandra/Neo4j/vector (U5-9,11,13).

---

## 3. File map — what to open, when

| Need | Open |
|---|---|
| Last 10 minutes before the exam | `notes/final-cram.md` |
| Last 30 minutes (rapid but complete) | `notes/ultra-short-notes.md` |
| Exact wording of a definition | `notes/definitions.md` |
| A rule, test or criterion | `notes/formulas.md` |
| "How do I answer a process question?" | `notes/processes-and-algorithms.md` |
| Comparison question prep | `notes/comparisons.md` |
| Diagram practice | `notes/diagrams-and-mental-models.md` |
| Worked examples & real commands | `notes/examples.md` |
| Avoiding lost marks | `notes/common-mistakes.md` |
| Mnemonics & chains | `notes/memory-hooks.md` |
| Self-testing (quick) | `notes/flashcards.md` |
| Self-testing (deep, with metadata) | `notes/question-bank.md` |
| What to study first | `notes/likely-questions.md` |
| Model answers by mark count | `notes/answer-bank.md` |
| Detailed per-unit notes | `notes/chapter-notes/unit-1..5.md` |
| Timed practice | `mock-exam-1..3.md` + `-key` files |
| Study schedules | `revision-plan.md` |
| Tracking your errors | `weakness-tracker.md` |
| Source caveats | `notes/errata.md` |
| What was/wasn't processed | `completion-audit.md` |

---

## 4. The study loop (3 rounds)

1. **Learn** — read a unit's `chapter-notes/unit-N.md` with `final-cram.md` beside it (20–30 min/unit).
2. **Test** — `flashcards.md` deck for that unit + 5 questions from `question-bank.md`; mark ✓/~/✗.
3. **Fix** — log every ✗ in `weakness-tracker.md`; re-read only the linked source lines; re-test after 30 min
   (spaced repetition inside the session), then again before the mock.

Then: `mock-exam-1` → mark → fix → `mock-exam-2` → mark → fix → `mock-exam-3`.
Final pass: `final-cram.md` + `revision-plan.md` (final-30 / final-10 plans).

---

## 5. Source page quick index
U1 pp.2–8 · U2 pp.9–14 · U3 pp.15–21 · U4 pp.22–27 · U5 pp.28–33 · back matter pp.34–36
(answer bank, diagram sheet, memorise-word-for-word table, checklist).
Full heading→page table: `_source/heading_pages.json`.
