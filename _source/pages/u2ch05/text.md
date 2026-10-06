# 5. Third Normal Form (3NF)

Source: ADBMS_MasterNotes.docx — folder `u2ch05`

### 5. Third Normal Form (3NF)
_(p. 10)_
A relation is in 3NF if it is in 2NF and does not contain an undesirable transitive dependency of non-prime attributes on a key. Formally, for every non-trivial FD X → A, X is a super key or A is a prime attribute.
Example: EMPLOYEE(EmpID, DeptID, DeptName). EmpID → DeptID and DeptID → DeptName. Therefore EmpID → DeptName transitively. DeptName should be moved to DEPARTMENT.
EMPLOYEE(EmpID, DeptID, DeptName)
      │
      ├── EmpID → DeptID
      │
      └── DeptID → DeptName
              ↓
       TRANSITIVE DEPENDENCY

EMPLOYEE(EmpID, DeptID)
DEPARTMENT(DeptID, DeptName)
