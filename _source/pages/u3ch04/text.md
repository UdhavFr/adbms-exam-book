# 4. Transaction Support in SQL

Source: ADBMS_MasterNotes.docx — folder `u3ch04`

### 4. Transaction Support in SQL
_(p. 16)_
SQL transaction control allows multiple statements to be grouped into a transaction.
BEGIN / START TRANSACTION
          ↓
     SQL operations
          ↓
     ┌────┴────┐
     │         │
  success    error
     │         │
   COMMIT   ROLLBACK
     │         │
 durable    undo uncommitted work
Example:
BEGIN;
UPDATE Account SET Balance = Balance - 500 WHERE AccountID = 1;
UPDATE Account SET Balance = Balance + 500 WHERE AccountID = 2;
COMMIT;
If an error occurs, ROLLBACK can undo uncommitted changes. SAVEPOINT creates an intermediate point to which a transaction can roll back.
#### Isolation levels
_(p. 16)_

| Isolation level | General idea |
|---|---|
| Read Uncommitted | May permit reading uncommitted changes; weakest common level. |
| Read Committed | Prevents ordinary dirty reads; behavior for repeated reads depends on DBMS. |
| Repeatable Read | Provides stronger repeat-read guarantees; exact phantom behavior varies by DBMS. |
| Serializable | Strongest standard isolation level; aims for serial-equivalent behavior. |

