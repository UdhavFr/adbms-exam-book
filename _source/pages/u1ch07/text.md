# 7. SQL — DDL, DML, DCL and TCL

Source: ADBMS_MasterNotes.docx — folder `u1ch07`

### 7. SQL — DDL, DML, DCL and TCL
_(p. 7)_
SQL is the standard language used to define and manipulate relational databases. It is declarative: the user specifies what result is required while the DBMS determines an execution strategy.

| Category | Purpose | Commands |
|---|---|---|
| DDL | Define/modify structure | CREATE, ALTER, DROP, TRUNCATE |
| DML | Retrieve/change data | SELECT, INSERT, UPDATE, DELETE |
| DCL | Privileges/security | GRANT, REVOKE |
| TCL | Transaction control | COMMIT, ROLLBACK, SAVEPOINT |

Example DDL: CREATE TABLE Student(StudentID INT PRIMARY KEY, Name VARCHAR(50), CourseID INT, FOREIGN KEY(CourseID) REFERENCES Course(CourseID));
Example DML: SELECT CourseID, COUNT(*) FROM Student GROUP BY CourseID;
Example DML modification: UPDATE Student SET Name='Rahul' WHERE StudentID=101;
Example TCL: BEGIN; UPDATE Account SET Balance=Balance-500 WHERE AccountID=1; COMMIT;
Example DCL: GRANT SELECT ON Student TO user1;
#### Important SQL clauses
_(p. 7)_
WHERE filters rows before grouping. GROUP BY forms groups. HAVING filters groups. ORDER BY sorts the result. JOIN combines rows from multiple relations. Aggregate functions such as COUNT, SUM, AVG, MIN and MAX summarize data.
Typical execution idea: FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT, although the DBMS optimizer may transform the physical execution plan.
