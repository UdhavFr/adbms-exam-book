# 9. Deferred Update

Source: ADBMS_MasterNotes.docx — folder `u3ch09`

### 9. Deferred Update
_(p. 19)_
In deferred update, database changes are not written to the database until the transaction reaches commit. Log records are generated so committed changes can be reconstructed.
Transaction
   ↓
Write log records
   ↓
Continue execution
   ↓
COMMIT
   ↓
Apply/REDO updates
   ↓
Durable database
After a crash, committed transactions may need REDO, while uncommitted transactions normally require no database UNDO because their changes were deferred.
