# 12. Log-Based Recovery

Source: ADBMS_MasterNotes.docx — folder `u3ch12`

### 12. Log-Based Recovery
_(p. 20)_
A log is a sequential record of transaction actions maintained on stable storage. A typical record may contain transaction ID, data item, old value, and new value.
Examples: <T1 START>, <T1, A, 100, 50>, <T1 COMMIT>.
#### Write-Ahead Logging
_(p. 20)_
The Write-Ahead Logging principle requires the relevant log record to be written to stable storage before the corresponding changed data page is written to persistent storage. This guarantees that recovery has enough information to undo or redo the operation.
#### Checkpointing
_(p. 20)_
A checkpoint records recovery information at intervals. During recovery, the system can begin from a recent checkpoint rather than scanning the entire history of the log, reducing recovery time.
LOG:
<START T1>
<T1, A, old, new>
<START T2>
<T2, B, old, new>
<COMMIT T1>
        ↓ CRASH
Recovery:
T1 committed → REDO if required
T2 uncommitted → UNDO
EXAM-READY POINT: Recovery answer formula: define recovery → failures → deferred update → immediate update → shadow paging → logging → WAL → checkpoint → UNDO/REDO → conclusion.
## UNIT 4 — DISTRIBUTED DATABASES AND NoSQL SYSTEMS
_(p. 21)_
