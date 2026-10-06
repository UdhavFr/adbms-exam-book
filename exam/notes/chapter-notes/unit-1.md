# UNIT 1 — Database System Concepts & Conceptual Modeling
Source: `ADBMS_MasterNotes.docx` Unit 1, pp. 2–8 · structure `u1ch01`–`u1ch09`
Priority legend: **P0** must-know · **P1** high-value · **P2** supporting · **P3** only if time remains

---

## U1-1 Introduction to Database Systems — **P1** (p. 2)
- **WHAT:** DB = organized collection of logically related data; DBMS = software to define/store/retrieve/update/protect/recover it.
- **WHY:** file systems give redundancy → inconsistency, and poor sharing/security/concurrency/recovery.
- **HOW:** DBMS centralizes data, adds constraints, concurrency control, logging/checkpoints, abstraction.
- **EXAM WRITE:** definition (D-S-R-U-S-R) → the 7-row problem/cure table → 9 functions → conclusion.
- **MISTAKE:** listing functions without the *problem→cure* table (that table is where the easy marks are).

## U1-2 Data Models, Schemas and Instances — **P1** (p. 3)
- **WHAT:** data model = concepts describing structure/relationships/constraints(+operations); schema = blueprint; instance = contents now.
- **EXAM WRITE:** definition → 9 model types in 3 chunks (old structural / conceptual-object / modern NoSQL) → schema-vs-instance table → blueprint analogy.
- **MISTAKE:** confusing schema and instance (blueprint vs current building), or forgetting that inserts change the *instance* only.

## U1-3 Levels of Data Abstraction & Data Independence — **P0** (p. 4)
- **WHAT:** three levels — **External** (customized user views) → **Conceptual** (complete logical schema, storage-independent) → **Internal** (files, pages, indexes, access paths) → physical storage.
- **WHY:** hides implementation detail; lets storage or logical design change without breaking users.
- **HOW:** physical independence = change storage without changing conceptual schema (change an index).
  Logical independence = change conceptual schema while required external views still work (split a table with a compatible view).
- **REMEMBER:** **E-C-I**; **P**=Pages/physical, **L**=Logic/logical.
- **EXAM WRITE:** diagram (D1) + one line per level + a two-row independence table with examples.
- **MISTAKE:** swapping the two independences. Fix: *which layer am I changing?* storage→physical, schema→logical.

## U1-4 Conceptual Modeling Using the ER Approach — **P0** (p. 5)
- **WHAT:** ER = high-level conceptual technique: entities, attributes, relationships, constraints — drawn *before* implementation.
- **WHY:** easy to understand by users and designers; captures structure without storage detail.
- **HOW:**
  - Entity / entity set (STUDENT, EMPLOYEE, PRODUCT, DEPARTMENT).
  - Attributes: simple, composite, single-valued, multivalued, derived, key.
  - Keys: super → candidate (minimal) → primary (chosen) · alternate (unchosen) · foreign (points elsewhere).
  - Relationships + cardinality **1:1 / 1:N / M:N** with anchors Person–Passport / Dept–Employee / Student–Course.
  - Participation: **total = mandatory (double line)**, **partial = optional (single line)**.
  - Relationship attribute: `EnrollmentDate` describes the *event*.
- **REMEMBER:** entity=thing · attribute=property · relationship=connection.
- **EXAM WRITE:** ER diagram (D2) + explain every symbol + the keys table + cardinality/participation table.
- **MISTAKE:** drawing an ER diagram with no labels; or calling `EnrollmentDate` a STUDENT attribute (errata E1 trap: cardinality means two things).

## U1-5 Mapping ER Diagrams to Relational Schemas — **P0** (p. 6)
- **WHAT:** transformation rules from conceptual ER design to tables.
- **HOW (7 rules, in order):** strong entity → relation with its PK · composite → store components ·
  multivalued → separate relation (owner PK + value) · 1:1 → PK of one side as FK (prefer total-participation side) ·
  1:N → **1-side PK becomes FK on the N-side** · M:N → new relation with both PKs (composite PK) ·
  weak entity → attributes + owner PK (owner key + partial key identifies it).
- **REMEMBER:** decision tree *Entity→table | Composite→split | Multi→new table | 1:1→FK | 1:N→FK on N | M:N→new table | Weak→owner+partial*.
- **EXAM WRITE:** rules list → worked example `STUDENT / COURSE / ENROLLS(StudentID, CourseID, EnrollDate)` → before/after diagram (D14).
- **MISTAKE:** FK on the wrong side of a 1:N relationship.

## U1-6 Overview of the Relational Model — **P1** (pp. 6–7)
- **WHAT:** relations = tables; tuples/attributes/domains; degree = #attributes, cardinality = #tuples; PK/FK; integrity rules; relational algebra.
- **ALGEBRA:** σ selection (rows) · π projection (columns) · ∪ union · − difference · × Cartesian product · ⋈ join.
- **EXAM WRITE:** vocabulary table + algebra table + one sentence: "SQL is the practical declarative language over this algebra."
- **MISTAKE:** σ/π swapped. **Hook:** Selection = records, Projection = fields.

## U1-7 SQL — DDL, DML, DCL, TCL — **P0** (p. 7)
- **WHAT:** declarative standard language — user states *what*, DBMS decides *how*.
- **HOW:**
  - DDL: CREATE, ALTER, DROP, TRUNCATE · DML: SELECT, INSERT, UPDATE, DELETE · DCL: GRANT, REVOKE · TCL: COMMIT, ROLLBACK, SAVEPOINT.
  - Clause roles: WHERE filters rows before grouping · GROUP BY forms groups · HAVING filters groups · ORDER BY sorts · JOIN combines relations · aggregates COUNT/SUM/AVG/MIN/MAX.
  - **Processing order:** FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT (errata E2: not the writing order).
- **REMEMBER:** DDL=Design, DML=Manipulate, DCL=Control access, TCL=Transaction.
- **EXAM WRITE:** the 4-category table → one real statement per category → the clause-order chain with a "why" line for WHERE vs HAVING.
- **MISTAKE:** using HAVING to filter individual rows, or WHERE to filter groups.

## U1-8 Integrity and Referential Constraints — **P0** (p. 7)
- **WHAT:** rules preserving correctness: **domain** (type/domain), **entity** (PK not NULL, unique), **referential** (FK points at an existing key or NULL if allowed), plus UNIQUE, CHECK, NOT NULL.
- **WHY:** without them, invalid values enter → bad reports, broken relationships, wrong decisions; constraints move correctness into the DB.
- **HOW:** `FOREIGN KEY(CourseID) REFERENCES Course(CourseID)`; referential actions CASCADE / SET NULL / SET DEFAULT / RESTRICT|NO ACTION.
- **REMEMBER:** **D-E-R + U-C-N**.
- **EXAM WRITE:** three named constraints (bold) + SQL sample + "why constraints matter" paragraph.
- **MISTAKE:** writing "foreign key must not be NULL" (NULL is permitted where the design allows).

## U1-9 Guidelines for Relational Schema Design & Anomalies — **P1** (p. 8)
- **WHAT:** 10 guidelines (clear meaning, avoid redundancy, minimize NULLs, proper keys, FKs for relationships, normalize, good data types, DB-level rules, performance/indexing after logical design, controlled denormalization only when justified).
- **ANOMALIES:** insertion (can't add a fact without an unrelated fact) · update (one logical change, many rows) · deletion (deleting a fact removes another).
- **EXAM WRITE:** anomalies table + 5–6 guidelines + the flow: requirements → ER → constraints → relational schema → normalization → SQL.
- **MISTAKE:** describing an anomaly without naming which one (I-U-D).

---

### Unit 1 exam weighting (evidence-based guess, not a prediction)
- **20-mark material:** ER + mapping + relational design as one combined question ("Design a database for…").
- **10-mark:** three-level architecture + data independence · SQL categories + clause order + constraints.
- **5-mark:** schema vs instance · anomalies · keys · relational algebra.
- **2-mark:** definitions (DBMS, tuple, domain, entity integrity…).
