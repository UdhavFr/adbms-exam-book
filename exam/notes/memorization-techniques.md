# memorization-techniques.md — The Right Device per Topic

*Two inputs merged: Blockchain §6 memory rules + a research pass on mnemonic fit
(consensus: acronyms/acrostics for short ordered lists, keyword method for terms,
loci for long ordered sets, chaining for sequences — matched to material, never one-size-fits-all).
Rule zero (BC): a mnemonic must be faster than the plain list, and acronym letters must match
the notes' list exactly. Concepts use cause-effect chains; procedures use worked reps, not acronyms.*

---

## 0. Operating rules (non-negotiable)

1. **Retrieve before reveal:** cover the device, recite aloud, then check. Reading a mnemonic is not learning it.
2. **SOLID = correct in 2 separate sessions:** tonight's block + the morning block. Anything correct only once is re-tested, not trusted.
3. **Red topics get a redrawn diagram** (look → cover → draw → compare, 3 reps). Labels carry marks — label-first.
4. **40-min blocks, 5–10 min breaks.** No all-nighter; morning = light retrieval only.
5. Warm-up sets live in `revision-plan.md` session rules; confidence-first in `weakness-tracker.md` §7.

---

## 1. Technique catalog (codes used in §2–§3)

| Code | Technique | Wins when… |
|---|---|---|
| ACR | Acronym (letters = word) | unordered short sets (ACID, BASE) |
| RST | Acrostic sentence (first letters) | ordered lists ≤7 (SQL clause order, pipeline) |
| CHK | Chunking (groups ≤4) | 5–9 items (ER rules, sharding, cover steps) |
| KW | Keyword image | one abstract term (WAL, checkpoint, cosine) |
| STY | Story chain | sequences with cause-effect (2PC, anomalies) |
| LOC | Memory palace (one route, stations) | the 6-step 20-mark spine; isolation ladder pegs |
| DRW | Draw reps (look-cover-draw-compare ×3) | all 11 required diagrams |
| WRT | Write reps (×3 from memory) | commands, definitions' openers, formulas |
| CE | Cause-effect chain | concepts (why deferred needs no UNDO) |
| D1W | One-word discriminator | every confusable pair (§4) |
| REP | Worked reps (3 fresh problems) | procedures (closure, NF tests, graphs) — never acronyms |

---

## 2. Assignment map (Tier-S fully worked in §3; rest mapped here)

| Topic | Chapters | Device | Already-have pointer |
|---|---|---|---|
| Normalization ladder | U2-1→11 | STY (pizza sheet) + RST (ladder sentence) + REP | `memory-hooks.md` §4, ch19 narrated |
| ACID + states | U3-1→4 | ACR + STY (transfer) + DRW (states) | ch20 narrated |
| CAP/BASE | U4-7/8 | D1W ("during a partition") + ACR + KW triangle | `final-cram.md` §5 |
| 2PL + deadlock | U3-6 | KW (grow=grab) + CE + D1W (2PL≠2PC) | hooks §5 |
| Recovery chain | U3-9→12 | STY + CE (no log→no undo) + D1W per scheme | hooks §5 |
| Serializability | U3-5 | REP (graphs) + D1W (cycle=bad) | processes P8–P11 |
| B+ tree vs hash | U2-13/14 | KW (Between/Has-exactly) + DRW | hooks §4 |
| ER mapping (7 rules) | U1-4/5 | CHK 2-2-3 + D1W (cardinality≠participation) | hooks §3 |
| Fragmentation + 2PC + sharding | U4-2/4/9 | STY (planner) + CHK + RST | hooks §6 |
| Cross-system indexing | U5-8→14 | CE + KW per system + D1W (partition≠clustering, HNSW≠IVF) | hooks §7 |
| SQL families + clauses | U1-7 | RST (families + execution order) + WRT | hooks §3 |
| Integrity constraints | U1-8 | KW (PK carved, FK leash) + D1W | flashcards |
| Isolation levels | U3-4 | LOC pegs 1–4 + CE (each level kills one anomaly) | §3 |
| Minimal cover | U2-11 | ACR (SSS) + REP | §3 |
| MongoDB pipeline | U4-12 | RST (My Great Shoes) + CE (filter first) | hooks §7 |
| Vector search | U5-6/7/13 | KW (angle/ruler/shadow) + D1W | hooks §7 |
| Three-level architecture | U1-3 | LOC 3 stations (flat→blueprint→engine room) | diagrams D1 |
| Schema vs instance | U1-2 | D1W (blueprint vs photo) | flashcards |
| Lossless/preservation | U2-9/10 | D1W (reconstruct vs enforce) + anchor example | comparisons |
| Stores (4 + vector) | U4-6/10/11, U5-1→5 | ACR (Doctors…) + KW use-case each | hooks §7 |

---

## 3. Fully-worked devices (recite these, don't just read)

**Isolation ladder — LOC pegs (weakest→strongest):**
1. **Dirty glass** (Read Uncommitted — you drink unwashed data: dirty reads).
2. **Clean glass** (Read Committed — washed once: no dirty reads).
3. **Photocopier** (Repeatable Read — your copy can't change under you; new pages may still arrive = phantoms).
4. **Single-file queue** (Serializable — one after another, full isolation).
Chain: each level kills exactly one anomaly. Gate: recite 1→4 with the killed anomaly each.

**SQL execution order — RST:** FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY.
Sentence: "**F**at **W**orms **G**obble **H**ot **S**paghetti **O**ften." Letters match the notes' order exactly.
Corollary hook: WHERE filters rows (before), HAVING filters groups (after).

**SQL families — RST + verbs:** **D**DL *Defines*, D**M**L *Manipulates*, D**C**L *Controls access*, T**C**L *Tames transactions*.
Write-reps: CREATE/ALTER/DROP · SELECT/INSERT/UPDATE/DELETE · GRANT/REVOKE · COMMIT/ROLLBACK/SAVEPOINT (3× each from memory).

**Minimal cover — ACR:** **S**plit RHS → **S**hrink LHS → **S**hed redundant FDs. Then REP on two FD sets.

**MongoDB pipeline — RST + CE:** "**M**y **G**reat **S**hoes" ($match → $group → $sort; $project shapes, $limit caps).
CE: filter first = every later stage touches less data. Gate: reorder a shuffled pipeline.

**ER 7 rules — CHK 2-2-3:** [entity→table · attributes→columns] [1:N = FK on N · M:N = junction] [multivalued→own table · composite→flatten · weak→owner-key + discriminator].

**Sharding — CHK + images:** Range (library shelves in order — locality) · Hash (lottery balls — balance, ranges die) · Directory (librarian's index — lookup map) · Geographic (local branch — latency).

**WAL — KW + CE:** a **ship's log written before the cargo moves**. CE: no log-before-data → crash leaves changes with no undo/redo record → unrecoverable. Hence "log first, always".

**Checkpoint — KW:** a **bookmark jammed into the log**. Recovery starts at the bookmark, not page one.

**Locks — KW:** **S**hared = reading room (many readers, no pens). e**X**clusive = locked diary (one writer, nobody else).

**Cosine/Euclidean/dot — KW:** cosine = **angle between arrows** (direction, not length) · Euclidean = **ruler distance** · dot = **shadow length** (projection).

**20-mark spine — LOC palace (6 stations, reuse for every long answer):**
**Door** (Define 5–7 lines) → **Hallway picture** (Diagram) → **Rooms** (Elaborate, one room per component) →
**Kitchen demo** (Example you can touch) → **Scales** (Pros vs cons) → **Guestbook** (Conclusion 3–4 lines).
Walk it before every 20-mark answer; the examiner's key follows the same route.

---

## 4. One-word discriminators (the whole confusables list, one word each)

| Pair | Discriminator |
|---|---|
| 3NF vs BCNF | **OR** vs **ONLY** (prime allowed or not) |
| CAP phrasing | **partition** (only during one) |
| σ vs π | **rows** vs **columns** |
| FK placement | **N-side** (many gets the key) |
| WAL order | **log-first** (never data-first) |
| 2PL vs 2PC | **locking** vs **agreement** |
| Lossless vs preservation | **reconstruct** vs **enforce** |
| Deferred vs immediate | **REDO-only** vs **UNDO+REDO** |
| Horizontal vs vertical frag | **rows** vs **columns** (UNION vs JOIN-on-key) |
| B+ vs hash | **range** vs **equality** |
| Partition vs clustering key | **place** vs **order** |
| HNSW vs IVF | **graph** vs **clusters** |
| Repeatable Read vs Serializable | **phantoms** (survive vs die) |
| Schema vs instance | **blueprint** vs **photo** |
| Cardinality vs participation | **how-many** vs **mandatory** |
| Entity vs referential integrity | **PK-valid** vs **FK-matches** |
| Atomicity vs durability | **all-or-nothing** vs **survives-crash** |
| Consistency (ACID) vs isolation | **rules-hold** vs **separate-rooms** |
| Eventual consistency | **converge** (never "loss") |
| $match position | **first** (cut early) |

Drill: cover the right column, recite the word. One wrong word = one lost mark.

---

## 5. What NOT to memorize (derive, dedupe, or drop)

- Armstrong axioms (use reflexivity/augmentation/transitivity — never recite them).
- 4NF/5NF beyond one line each; B-tree split algorithms; CouchDB depth; EER depth (SKIP boxes agree).
- Full definitions past the opener: memorize the first 5–7 words verbatim (exam opener), reconstruct the rest from keywords.
- Any two mnemonics for the same list — one device per list, the §3 one wins.
