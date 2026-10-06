# 8. Recovery and Types of Failures

Source: ADBMS_MasterNotes.docx — folder `u3ch08`

### 8. Recovery and Types of Failures
_(p. 18)_
Recovery is the process of restoring the database to a consistent state after failure.
- Transaction failure: logical error, constraint violation, deadlock victim, or explicit abort.
- System crash: power failure or operating-system/database process failure causing loss of volatile memory.
- Media failure: disk/storage damage causing loss of persistent data.
- Communication failure: especially important in distributed databases.
The recovery manager uses logs, checkpoints, backups, shadow structures, and undo/redo techniques depending on the DBMS.
