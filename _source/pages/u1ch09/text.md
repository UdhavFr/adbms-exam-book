# 9. Guidelines for Relational Schema Design

Source: ADBMS_MasterNotes.docx — folder `u1ch09`

### 9. Guidelines for Relational Schema Design
_(p. 8)_
- Each relation should have a clear and understandable meaning.
- Avoid unnecessary redundancy.
- Minimize NULL values where possible.
- Use appropriate primary and candidate keys.
- Represent relationships using foreign keys.
- Normalize relations to reduce anomalies.
- Choose appropriate data types and domains.
- Enforce business-critical integrity rules at the database level.
- Consider query performance and indexing after establishing a sound logical design.
- Use controlled denormalization only when there is a justified performance or reporting requirement.
#### Modification anomalies
_(p. 8)_

| Anomaly | Explanation |
|---|---|
| Insertion anomaly | A fact cannot be inserted without also inserting an unrelated fact. |
| Update anomaly | The same fact is repeated in many rows, so one logical change requires multiple updates. |
| Deletion anomaly | Deleting one fact accidentally removes another fact that should have been retained. |

EXAM-READY POINT: End Unit 1 by remembering the flow: requirements → conceptual ER model → constraints → relational schema → normalization/design → SQL implementation.
## UNIT 2 — NORMALIZATION, DATA STORAGE AND INDEXING
_(p. 9)_
