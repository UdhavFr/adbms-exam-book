# 2. Normalization — Need and Goals

Source: ADBMS_MasterNotes.docx — folder `u2ch02`

### 2. Normalization — Need and Goals
_(p. 9)_
Normalization is the systematic process of organizing relations using dependencies and decomposition so that redundancy and modification anomalies are reduced while important relationships and dependencies are preserved.
UNNORMALIZED DATA
      ↓ remove repeating groups / non-atomic values
1NF  ───────────────────────────────
      ↓ remove partial dependencies
2NF  ───────────────────────────────
      ↓ remove transitive dependencies
3NF  ───────────────────────────────
      ↓ every determinant must be a super key
BCNF ───────────────────────────────
      ↓ remove non-key multivalued dependencies
4NF  ───────────────────────────────
      ↓ remove problematic join dependencies
5NF / PJNF
The goal is not to normalize blindly. A good design balances correctness, maintainability, query performance, and application requirements.
