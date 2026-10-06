# 6. Boyce-Codd Normal Form (BCNF)

Source: ADBMS_MasterNotes.docx — folder `u2ch06`

### 6. Boyce-Codd Normal Form (BCNF)
_(p. 11)_
A relation is in BCNF if for every non-trivial functional dependency X → Y, X is a super key. BCNF is stricter than 3NF and removes certain redundancy that 3NF can allow.
The key phrase to memorize is: 'Every determinant must be a super key.'

| 3NF | BCNF |
|---|---|
| X→A allowed if X is super key OR A is prime. | X→Y allowed only if X is super key. |
| Less restrictive. | More restrictive. |
| Usually easier to preserve dependencies. | Dependency preservation may be lost. |
| Often practical compromise. | Used when stronger redundancy removal is required. |

