# 1. Functional Dependencies

Source: ADBMS_MasterNotes.docx — folder `u2ch01`

### 1. Functional Dependencies
_(p. 9)_
A functional dependency (FD) describes a relationship between attributes in a relation. X → Y means that whenever two tuples agree on all attributes of X, they must also agree on all attributes of Y. X is called the determinant and Y is functionally dependent on X.
Example: StudentID → StudentName. If StudentID 101 identifies Ravi, every occurrence of StudentID 101 must have the same StudentName under this dependency.
#### Why FDs matter
_(p. 9)_
- Identify candidate keys.
- Detect redundancy.
- Identify partial and transitive dependencies.
- Guide normalization and decomposition.
- Help prove whether a decomposition preserves important constraints.
#### Important types
_(p. 9)_
- Trivial FD: Y ⊆ X.
- Non-trivial FD: Y is not a subset of X.
- Full dependency: Y depends on the whole determinant X.
- Partial dependency: Y depends on only a proper subset of a composite key.
- Transitive dependency: X → Y and Y → Z imply X → Z.
#### Attribute closure
_(p. 9)_
The closure X+ is the set of all attributes functionally determined by X using a set of FDs. To compute X+, start with X and repeatedly add attributes that can be obtained from FDs whose left side is already contained in the closure. If X+ contains every attribute of the relation, X is a super key.
Example: F = {A→B, B→C, C→D}. A+ starts as {A}; A→B gives B; B→C gives C; C→D gives D. Therefore A+ = {A,B,C,D}, so A is a key for this relation if these are all its attributes.
