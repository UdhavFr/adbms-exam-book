# 10. Immediate Update

Source: ADBMS_MasterNotes.docx — folder `u3ch10`

### 10. Immediate Update
_(p. 19)_
In immediate update, a modified database page may be written before the transaction commits. Therefore, after a crash, the system may need to undo changes of uncommitted transactions and redo changes of committed transactions that may not have reached disk.
Transaction → log old/new values → data page may be written
                         ↓
                      COMMIT?
                    /         \
                  YES         NO
                   ↓           ↓
              REDO if needed  UNDO
