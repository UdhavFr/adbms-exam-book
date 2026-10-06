# formulas.md — Rules, Criteria and "Formula-Like" Content

ADBMS is a theory subject: there are **no numerical problems to compute**, but there *are* rigid
**rule-formulas** (normal-form criteria, closure, decomposition tests, complexity) that are marked
word-for-word. Treat each box below as a formula: trigger → result.

Anything marked **[EXTERNAL]** is standard knowledge added because the source names the concept
without printing the expression. Everything else is verbatim/faithful to the source.

---

## 1. Attribute closure (the one real algorithmic "formula")

**X⁺ = { all attributes functionally determined by X under F }**

Algorithm (memorise as a loop):
```
C := X
repeat
   if some FD (W → Z) in F has W ⊆ C, then C := C ∪ Z
until C stops growing
```
- **When to use:** find candidate keys, test whether an FD follows from F, test implication/equivalence.
- **Key result:** if **X⁺ = all attributes of R**, then **X is a super key**. A minimal such X is a candidate key.
- **Worked example (source):** F = {A→B, B→C, C→D}; A⁺ starts {A} → {A,B} → {A,B,C} → **{A,B,C,D}** ⇒ A is a key.
- **Common mistake:** forgetting to re-check FDs whose left side became part of the closure *after* an earlier step (you must loop until nothing new appears).

## 2. The normal-form criteria (write these exactly)

| NF | Criterion (exam-ready) | What it kills |
|---|---|---|
| 1NF | every attribute holds **atomic** values; no repeating groups / nested sets | non-atomic values |
| 2NF | 1NF **and** every non-prime attribute is **fully** dependent on the **entire** candidate key | **partial** dependency |
| 3NF | 2NF **and** for every non-trivial FD X → A: **X is a super key OR A is prime** | **transitive** dependency |
| BCNF | for every non-trivial FD X → Y: **X is a super key** (every determinant is a super key) | any non-key determinant |
| 4NF | every non-trivial **MVD** X ↠ Y has **X as a super key** | independent multivalued facts |
| 5NF | every non-trivial **join dependency** is implied by **candidate keys** | complex join redundancy |

- **Memory:** 1 = Atomic · 2 = Partial · 3 = Transitive · BC = Determinant · 4 = MVD · 5 = Join
- **Trap:** **3NF = OR** (super key *or* prime) · **BCNF = ONLY** (super key).

## 3. Prime vs non-prime (needed before you can apply 3NF/BCNF)

- **Prime attribute** = any attribute that belongs to *some* candidate key.
- **Non-prime attribute** = in no candidate key.
- **Common mistake:** calling a foreign key "prime" — a FK is prime only if it is part of a candidate key of *this* relation.

## 4. Lossless join test (binary decomposition)

R decomposed into R₁, R₂ is **lossless** iff, for the intersection of their attribute sets:

```
(R1 ∩ R2) → R1     OR     (R1 ∩ R2) → R2      (derived using F⁺)
```
- **Source example:** R(A,B,C) → R₁(A,B), R₂(A,C); intersection = {A}; so if **A → B** or **A → C** holds, the decomposition is lossless.
- **Common mistake:** testing with an attribute that is *not* in the intersection, or using only the FDs as written instead of their closure.

## 5. Dependency preservation test (conceptual)

A decomposition {R₁…Rₙ} is dependency preserving iff every FD in F can be checked using only the
projections F₁ ∪ … ∪ Fₙ — i.e. **F is contained in the union of the projections** (each projected FD is
checked locally, no join needed).
- **Memory:** Lossless = picture rebuilds exactly · Preserving = rules checkable without joining.
- **Common mistake:** assuming they come together — a decomposition can be lossless but *not* preserving.

## 6. Minimal cover steps (ordered — marks are for the order)

```
1. Split every FD so the RHS has exactly ONE attribute
2. Remove extraneous attributes from left sides (test each)
3. Remove redundant FDs (those derivable from the rest)
→ canonical cover
```
- **Equivalence:** F ≡ G iff **F⁺ = G⁺** (test with attribute closure).
- **Memory:** **S-E-R** = Split → Extraneous → Remove.

## 7. Complexity / performance expressions

| Expression | Meaning | Source |
|---|---|---|
| **O(log_f N)** | B+ tree node visits for a search, f = fan-out, N = entries | U2 §13 |
| Page I/O is the dominant cost | data moves in **pages/blocks**, not records | U2 §12 |
| Brute-force vector search = **O(N·d)** per query (N vectors, d dims) | why ANN exists | [EXTERNAL] — source says only "expensive as the number of vectors grows" |

## 8. Relational algebra "symbols formula sheet"

| Op | Symbol | Result |
|---|---|---|
| Selection | **σ**_(cond)_ | rows satisfying condition (**records**) |
| Projection | **π**_(attrs)_ | required columns (**fields**) |
| Union | **∪** | tuples in either (union compatible) |
| Difference | **−** | in one, not the other |
| Cartesian product | **×** | every tuple × every tuple |
| Join | **⋈**_(cond)_ | related tuples combined |

- **Hook:** **S**election = **S**ubset of rows; **P**rojection = **P**ick columns. (Never swap them.)

## 9. SQL evaluation-order formula

```
FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```
- Written order is `SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT` (errata E2).
- **Meaning:** WHERE filters *rows before* grouping; HAVING filters *groups after* grouping.

## 10. Lock compatibility formula

| held \ requested | S | X |
|---|---|---|
| **S** | ✅ compatible | ❌ |
| **X** | ❌ | ❌ |

- **Hook:** S = **S**hares, X = e**X**cludes. Only S+S ever works.

## 11. 2PL formula

```
GROWING (acquire only) → LOCK POINT (last acquisition) → SHRINKING (release only)
```
- Basic 2PL ⇒ **conflict serializability**. Strict 2PL ⇒ hold **X** locks till commit/abort (fewer cascading rollbacks). Rigorous ⇒ hold **S and X** till completion.

## 12. Recovery decision formula

```
After crash:  COMMITTED  → REDO as needed
              UNCOMMITTED → UNDO as needed
```
- Deferred update ⇒ uncommitted work never reached the DB ⇒ normally **no UNDO**.
- Immediate update ⇒ both UNDO and REDO may be required.
- **WAL formula:** `log record → stable storage` **BEFORE** `data page → disk`.

## 13. ACID (the four-line formula)

```
A  Atomicity    all-or-nothing            (rollback on failure)
C  Consistency  committed state is valid  (constraints hold)
I  Isolation    no inappropriate intermediate effects (serial-equivalent)
D  Durability   committed effects survive failure
```

## 14. 2PC decision formula

```
Coordinator: PREPARE ──► participants vote YES/NO
             all YES → COMMIT
             any NO / coordinator decision → ABORT
```
- **Memory:** ASK → VOTE → DECIDE. **Limitation:** blocking.

## 15. CAP formula

```
During a network partition:  strong Consistency  ⊕  Availability   (choose the guarantee)
```
- **Never write:** "you can pick any two at all times."
- **C** = read sees latest write (or error) · **A** = non-failing node answers (maybe stale) · **P** = survives network failure.

## 16. Similarity formulas **[EXTERNAL]** — source names the measures, not the expressions

Let **q** = query vector, **v** = stored vector.

| Measure | Formula | Memory |
|---|---|---|
| Cosine similarity | cos θ = (q·v) / (‖q‖‖v‖) | **angle only** (ignores length) |
| Euclidean distance | ‖q − v‖₂ = √Σ(qᵢ−vᵢ)² | **straight-line** distance (smaller = closer) |
| Dot product | q·v = Σ qᵢvᵢ | **alignment + magnitude** (large = close & large vectors) |

- Higher cosine / dot ⇒ more similar; smaller Euclidean ⇒ more similar.

## 17. Cardinality / degree (relation vocabulary)

- **Degree(R)** = number of attributes (columns).
- **Cardinality(R)** = number of tuples (rows).
- ⚠ In the ER context *cardinality* = 1:1 / 1:N / M:N (errata E1). Say which one you mean.

## 18. MongoDB command "formula"

```
CRUD × ONE/MANY:  insertOne|insertMany · find|findOne · updateOne|updateMany · deleteOne|deleteMany
Pipeline:          $match → $group → $project → $sort → $limit   (+ $skip, $unwind, $lookup)
```

## 19. Cassandra placement "formula"

```
PRIMARY KEY ( (partition_key), clustering1, clustering2 )
   partition key   → WHERE the row lives (which node)
   clustering cols  → ORDER of rows inside the partition
```

## 20. Vector search pipeline

```
QUERY → EMBED → QUERY VECTOR → VECTOR INDEX → TOP-K neighbours → metadata/documents → RESULTS
```
