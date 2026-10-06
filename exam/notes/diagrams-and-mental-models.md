# diagrams-and-mental-models.md — Draw These Blind

Examiner signal: a labelled diagram = instant structure marks. Practise each one **on blank paper, timed (90 seconds)**.
Source: Diagram Practice Sheet (11 required) + architecture flows inside the notebook.

---

## D1. Three-level architecture ← *required*

```
        EXTERNAL / VIEW LEVEL
   ┌──────────┬──────────┬──────────┐
   │ Student  │ Faculty  │ Accounts │   ← customised user views
   │  view    │  view    │  view    │      (simplicity + security)
   └────┬─────┴────┬─────┴────┬─────┘
        └──────────┼──────────┘
                   ↓
          CONCEPTUAL LEVEL      ← complete logical schema:
                                   entities + relationships + constraints
                   ↓               (independent of physical storage)
           INTERNAL LEVEL        ← files + pages + indexes + access paths
                   ↓
         PHYSICAL STORAGE       ← disks/blocks
```
**Labels you must write:** external = *user views*, conceptual = *logical design*, internal = *physical layout*.
**Add the two arrows of independence:** physical (internal ↔ conceptual), logical (conceptual ↔ external).

---

## D2. ER diagram (the standard one) ← *required*

```
  ┌──────────┐                       ┌──────────┐
  │ STUDENT  │                       │  COURSE  │
  │──────────│                       │──────────│
  │ StudentID│                       │ CourseID │
  │ Name     │        ENROLLS        │ Title    │
  └────┬─────┘        ◇              └────┬─────┘
       │              │                   │
       │           M       N              │
       │                                  │
       └──────────────┴───────────────────┘
              EnrollmentDate  (relationship attribute)
```
**Explain every symbol:** rectangle = entity, oval = attribute, diamond = relationship, M:N = cardinality,
`EnrollmentDate` belongs to the *event*, not to one entity. Add a double diamond for a weak entity,
double ellipse for a multivalued attribute, dashed ellipse for a derived attribute.

---

## D3. The normalization ladder ← *required*

```
UNNORMALIZED
   ↓ remove repeating groups / non-atomic values
 1NF   (atomic values)
   ↓ remove partial dependencies
 2NF   (whole-key dependence)
   ↓ remove transitive dependencies
 3NF   (no non-key determinants)
   ↓ every determinant must be a super key
 BCNF
   ↓ remove non-key multivalued dependencies
 4NF
   ↓ remove problematic join dependencies
 5NF / PJNF
```
**Write under it:** 1=Atomic · 2=Partial · 3=Transitive · BC=Determinant · 4=MVD · 5=Join.

---

## D4. B+ tree ← *required*

```
                  [ 30 | 60 ]
              /        |        \
       [10|20]      [40|50]    [70|80|90]     ← internal: separators + child pointers
        / | \        / | \       / | \
      leaves (search keys + record/data pointers)
              ↕         ↕         ↕           ← LEAVES ARE LINKED
       [10,20]  ↔  [40,50]  ↔  [70,80,90]     ← range scan walks this chain
```
**Caption to write:** "internal nodes: separator keys + child pointers; leaf nodes: keys + record pointers, linked for range queries; balanced ⇒ O(log_f N)."

---

## D5. Transaction state machine ← *required*

```
              ACTIVE
                 │ last statement
                 ↓
        PARTIALLY COMMITTED
            │            │
     commit succeeds   failure
            ↓            ↓
       COMMITTED       FAILED
                          │ ROLLBACK
                          ↓
                       ABORTED
                          │
                  restart / terminate
```

---

## D6. Two-phase locking ← *required*

```
TIME →
┌────────────────────────┬────────────────────────┐
│ GROWING PHASE          │ SHRINKING PHASE        │
│ acquire S/X locks      │ release locks          │
│ NO releases            │ NO new acquisitions    │
└────────────────────────┴────────────────────────┘
              ▲
        LOCK POINT (last acquisition)
```

---

## D7. Recovery / log flow ← *required*

```
LOG:  <START T1> <T1, A, old, new> <START T2> <T2, B, old, new> <COMMIT T1>
                          ↓ CRASH
              ┌──── CHECKPOINT (recent start point) ────┐
              ↓                                         ↓
       T1 committed → REDO if required      T2 uncommitted → UNDO
              ↓
      CONSISTENT DATABASE
```
**Caption:** "WAL: the log record must reach stable storage **before** the data page is written."

---

## D8. Distributed database architecture ← *required*

```
            DISTRIBUTED DATABASE
                    │
      ┌─────────────┼─────────────┐
      ↓             ↓             ↓
   SITE A        SITE B        SITE C
  Data A1       Data B1       Data C1
  Replica A2    Replica B2    Replica C2
      \             │             /
       └───────── NETWORK ────────┘
```
**Add:** fragments (horizontal/vertical) and replicas at each site, plus a COORDINATOR node for 2PC.

---

## D9. CAP triangle ← *required*

```
            CONSISTENCY (C)
                 /\
                /  \
               /    \
              /      \
             /________\
   AVAILABILITY (A) —— PARTITION (P)

  During a partition: trade C against A.
```
**Caption under it (verbatim idea):** "During a network partition a system cannot guarantee both strong
consistency and availability for every request under the formal CAP definitions."

---

## D10. Sharding ← *required*

```
                DATASET
                   │
        SHARDING / PARTITION
     ┌─────────────┼─────────────┐
     ↓             ↓             ↓
  SHARD 1       SHARD 2       SHARD 3
  IDs 1–100     IDs 101–200   IDs 201–300
  (range strategy shown; hash/dir/geographic are alternatives)
```

---

## D11. Vector search pipeline ← *required*

```
  QUERY → EMBEDDING MODEL → QUERY VECTOR → VECTOR INDEX → TOP-K → METADATA/DOCS → RESULTS
```
Add side-notes: cosine = angle, Euclidean = distance, dot = alignment+magnitude; HNSW = graph, IVF = clusters.

---

## Extra diagrams worth drawing (strong answers, not on the required list)

### D12. 2PC message flow

```
COORDINATOR ─── PREPARE ───► P1, P2, P3
COORDINATOR ◄── YES/NO ──── P1, P2, P3
COORDINATOR ─── COMMIT ───►  (all YES)   |   ABORT (any NO)
     ⚠ prepared participant BLOCKS if coordinator's decision is unreachable
```

### D13. Concurrency: conflict → precedence graph

```
T1: R(X) … W(X) ────────► T2: R(X) … COMMIT

edge T1 → T2 (conflicting ops on X, T1 first) → graph acyclic ⇒ conflict-serializable
```

### D14. ER → relational mapping (before/after)

```
ER MODEL                              RELATIONAL MODEL
STUDENT ─── ENROLLS ─── COURSE   →    STUDENT(StudentID, Name)
   M            N                     COURSE(CourseID, Title)
                                      ENROLLS(StudentID, CourseID, EnrollDate)
```

### D15. Data flow: disk to CPU

```
SECONDARY STORAGE (File → Pages)  --I/O-->  BUFFER POOL [P1 P7 P4 P9]  -->  CPU / DBMS
   "DB I/O moves pages, not records"  →  reducing page I/O is the optimization goal
```

### D16. Normalization worked example (2NF)

```
ENROLL(StudentID, CourseID, StudentName, CourseName, Grade)
         │                │
   StudentID → StudentName   CourseID → CourseName     ← partial (key is composite)
         ↓
STUDENT(StudentID, StudentName)
COURSE(CourseID, CourseName)
ENROLL(StudentID, CourseID, Grade)      ← Grade depends on the FULL key
```

### D17. Transitive dependency (3NF)

```
EMPLOYEE(EmpID, DeptID, DeptName)
   EmpID → DeptID
             DeptID → DeptName   ⇒ transitive
        ↓
EMPLOYEE(EmpID, DeptID)   +   DEPARTMENT(DeptID, DeptName)
```

### D18. Independent multivalued facts (4NF)

```
STUDENT ──┬── HOBBIES      ┐ independent of each other
          └── LANGUAGES    ┘ ⇒ split:
        STUDENT_HOBBY(Student, Hobby)  +  STUDENT_LANGUAGE(Student, Language)
```

### D19. Cassandra partition layout

```
TABLE student   partition key = course
      ├── Partition MCA: clustering rows (ordered by clustering cols)
      └── Partition MBA: clustering rows
   partition key → WHERE the data lives   |   clustering columns → ORDER within partition
```

### D20. Deferred vs immediate update

```
DEFERRED:   Transaction → LOG only → COMMIT → REDO apply → DB
IMMEDIATE:  Transaction → LOG → page may hit disk → COMMIT?  YES: REDO if needed | NO: UNDO
```

---

## Mental models (one picture each)

| Concept | Picture to hold |
|---|---|
| Schema vs instance | blueprint vs the building today |
| Data independence | changing shelves (physical) vs changing the catalogue (logical) |
| Normalization | a messy drawer → labelled separate drawers |
| Lossless join | puzzle pieces that rebuild the exact picture |
| Dependency preservation | rules checked in each drawer without re-merging them |
| B+ tree | a book index whose last page points to the next page |
| Hash index | P.O. boxes: exact address, no ordering |
| 2PL | take every key you need, then hand them back — never halfway |
| ACID | four promises of a bank transfer |
| WAL | diary entry before moving the furniture |
| Shadow paging | never overwrite the last good manuscript |
| 2PC | everyone raises a hand before anyone acts |
| CAP | when the network splits, decide what you keep |
| Cassandra | the partition key is the address; clustering columns are the shelf order |
| Vector DB | meaning as coordinates; nearest = most similar |
