# UNIT 2 — Normalization, Data Storage and Indexing
Source: `ADBMS_MasterNotes.docx` Unit 2, pp. 9–14 · structure `u2ch01`–`u2ch14`
This unit contains the **#1 most examinable answer** in the subject (the full normalization answer).

---

## U2-1 Functional Dependencies — **P0** (p. 9)
- **WHAT:** X → Y means tuples agreeing on X must agree on Y; X = determinant, Y functionally dependent.
- **WHY:** FDs find candidate keys, expose redundancy, define partial/transitive dependencies, drive decomposition, prove constraint preservation.
- **TYPES:** trivial (Y ⊆ X) · non-trivial · full · partial (subset of a composite key) · transitive (X→Y, Y→Z ⇒ X→Z).
- **CLOSURE:** X⁺ = everything X determines; if X⁺ = all attributes ⇒ X is a super key. Loop until no growth.
- **EXAM WRITE:** definition → example `StudentID → StudentName` → why-FDs list → types list → closure algorithm with the {A,B,C,D} example.
- **MISTAKE:** stopping the closure loop early; calling Y⊆X non-trivial.

## U2-2 Normalization — Need and Goals — **P0** (p. 10)
- **WHAT:** systematic organization using dependencies and decomposition so redundancy and anomalies fall while dependencies are preserved.
- **WHY:** modification anomalies (I-U-D) and wasted storage in uncontrolled designs.
- **THE LADDER:** UNF →(atomic) 1NF →(no partial) 2NF →(no transitive) 3NF →(every determinant a super key) BCNF →(no non-key MVD) 4NF →(no problematic JD) 5NF.
- **WHY-NOT-BLINDLY:** balance correctness, maintainability, query performance, application needs.
- **EXAM WRITE:** definition → ladder diagram with the *reason arrow* on each step → one line on goals → transition sentence into 1NF.

## U2-3 First Normal Form — **P0** (p. 10)
- **WHAT:** every attribute atomic; no repeating groups/nested sets in one field.
- **EXAMPLE:** `STUDENT(…, Phones)` with `'9876,8765'` → `STUDENT(StudentID, Name)` + `STUDENT_PHONE(StudentID, Phone)`.
- **BENEFITS:** values addressable · easier search/update · removes repeating groups · foundation for higher NFs.
- **MISTAKE:** splitting a *composite* attribute (Address) and calling it an 1NF fix — composites are handled in ER mapping; 1NF is about **atomicity/repeating groups**.

## U2-4 Second Normal Form — **P0** (p. 10)
- **WHAT:** 1NF **and** every non-prime attribute fully dependent on the **entire** candidate key ⇒ removes **partial** dependency.
- **EXAMPLE (memorise):** `ENROLL(StudentID, CourseID, StudentName, CourseName, Grade)`, key `(StudentID, CourseID)`; `StudentID→StudentName`, `CourseID→CourseName` are partial → decompose to STUDENT / COURSE / ENROLL(…, Grade).
- **MISTAKE:** applying 2NF to a single-attribute key (there can be no partial dependency then).

## U2-5 Third Normal Form — **P0** (p. 11)
- **WHAT:** 2NF **and** no undesirable transitive dependency of non-prime attributes on a key. Formally: for every non-trivial X→A, **X is a super key OR A is prime**.
- **EXAMPLE:** `EMPLOYEE(EmpID, DeptID, DeptName)`; EmpID→DeptID, DeptID→DeptName ⇒ transitive → `EMPLOYEE(EmpID, DeptID)` + `DEPARTMENT(DeptID, DeptName)`.
- **REMEMBER:** 3NF = **OR**.
- **MISTAKE:** writing "3NF: determinant must be a super key" (that's BCNF).

## U2-6 Boyce–Codd Normal Form — **P0** (p. 11)
- **WHAT:** every non-trivial FD X → Y has **X as a super key** — slogan: *"every determinant must be a super key."*
- **vs 3NF:** stricter; may lose dependency preservation; 3NF is the practical compromise; BCNF when stronger redundancy removal is needed.
- **REMEMBER:** BCNF = **ONLY**.
- **MISTAKE:** claiming BCNF is easier to satisfy than 3NF.

## U2-7 Multivalued Dependencies and 4NF — **P1** (p. 11)
- **WHAT:** X ↠ Y when, for each X value, the set of Y values is independent of the remaining attributes — typically two independent multivalued facts about one entity.
- **EXAMPLE:** STUDENT with independent HOBBIES and LANGUAGES → `STUDENT_HOBBY` + `STUDENT_LANGUAGE`.
- **RULE:** 4NF = every non-trivial MVD has **X as a super key**.
- **MISTAKE:** describing 4NF as "no repeating groups" (that's 1NF).

## U2-8 Join Dependencies and 5NF — **P1** (p. 12)
- **WHAT:** a relation can be reconstructed by joining several projections; 5NF (PJNF) = every non-trivial JD is implied by candidate keys.
- **DISTINCTION (source):** *4NF deals with independent multivalued facts; 5NF deals with complex join dependencies and lossless reconstruction through projections.*
- **MISTAKE:** calling 5NF "the normal form with no redundancy at all" — it addresses redundancy from join dependencies not captured by FDs/MVDs.

## U2-9 Lossless Join Decomposition — **P0** (p. 12)
- **WHAT:** joining the decomposed relations yields *exactly* the original — no lost information, no spurious tuples.
- **TEST (binary):** for R1, R2: **(R1 ∩ R2) → R1** or **(R1 ∩ R2) → R2** under F.
- **EXAMPLE:** R(A,B,C) → R1(A,B), R2(A,C); if A→B or A→C ⇒ lossless.
- **MISTAKE:** reversing the implication direction; or asserting losslessness without testing.

## U2-10 Dependency Preservation — **P1** (p. 12)
- **WHAT:** original FDs enforceable on the decomposed relations *individually*, without joins.
- **KEY POINT:** losslessness and preservation are **independent**; a decomposition can be one without the other; design seeks both when possible.
- **MISTAKE:** assuming they come together.

## U2-11 Minimal Cover and FD Equivalence — **P1** (p. 12)
- **STEPS:** split RHS to single attributes → remove extraneous LHS attributes → remove redundant FDs → canonical cover.
- **EQUIVALENCE:** F ≡ G iff F⁺ = G⁺ (test with closure).
- **MISTAKE:** wrong order (redundancy removal before extraneous-attribute removal).

## U2-12 Data Storage, Disk Structure and Blocks — **P2** (p. 12)
- **WHAT:** data moves in **pages/blocks**, not records; buffer manager loads pages, keeps hot pages, writes back dirty pages; reducing page I/O is a core optimization goal.
- **FILE ORGANIZATIONS:** heap (inserts/scans) · sequential/sorted (ordered/range) · hash (equality) · clustered (related records together).
- **MISTAKE:** saying "the DB reads record by record".

## U2-13 B+ Tree Indexing — **P0** (p. 13)
- **WHAT:** balanced multiway search tree; internal = separator keys + child pointers; leaves = search keys + record/data pointers; **leaves linked**.
- **SEARCH:** root → compare → follow child → leaf → record pointer.
- **WHY FAST:** balanced height · high fan-out · linked leaves (range scans) · dynamic insert/delete · nodes sized to disk pages. Complexity **O(log_f N)**.
- **MISTAKE:** not mentioning linked leaves (the range-query reason).

## U2-14 Hash-Based Indexing — **P1** (p. 14)
- **WHAT:** key → hash function → bucket → records/pointers; great for equality (`StudentID = 101`).
- **COLLISION:** two keys → same bucket; handled by overflow buckets, chaining, dynamic hashing.
- **vs B+ TREE:** ordered vs unordered · equality+range vs equality only · good for ORDER BY vs poor range traversal.
- **MISTAKE:** recommending hash for range/ORDER BY questions.

---

### Unit 2 exam weighting
- **20-mark:** "Explain normalization and all normal forms" (source's Question 1) — FDs → keys → 1NF…5NF → lossless → preservation → minimal cover → conclusion.
- **10-mark:** a specific "convert R to 3NF/BCNF" problem · B+ tree vs hash comparison.
- **5-mark:** attribute closure computation · dependency preservation vs losslessness · file organizations.
- **2-mark:** NF definitions · FD types · collision.
