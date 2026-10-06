# 8. Integrity and Referential Constraints

Source: ADBMS_MasterNotes.docx — folder `u1ch08`

### 8. Integrity and Referential Constraints
_(p. 7)_
Integrity constraints are rules that preserve correctness and consistency of database values.
- Domain integrity: values must satisfy the data type/domain.
- Entity integrity: primary-key values cannot be NULL and must uniquely identify tuples.
- Referential integrity: a foreign key must refer to an existing referenced key or be NULL where permitted.
- UNIQUE: prevents duplicate values in a constrained column/set.
- CHECK: enforces a Boolean condition such as Salary > 0.
- NOT NULL: prevents missing values where a value is mandatory.
Example: FOREIGN KEY(CourseID) REFERENCES Course(CourseID) ensures that a student cannot reference a course that does not exist. Referential actions may include CASCADE, SET NULL, SET DEFAULT, or RESTRICT/NO ACTION depending on the DBMS and design.
#### Why constraints matter
_(p. 8)_
Without constraints, invalid values can enter the database and cause application errors, inconsistent reports, broken relationships, and incorrect business decisions. Constraints move part of the correctness responsibility into the database itself.
