# 2. Transaction States and System Concepts

Source: ADBMS_MasterNotes.docx — folder `u3ch02`

### 2. Transaction States and System Concepts
_(p. 15)_
                 ACTIVE
                   │
             last statement
                   ↓
           PARTIALLY COMMITTED
              │           │
       commit success     failure
              ↓           ↓
          COMMITTED      FAILED
                           │
                         ROLLBACK
                           ↓
                        ABORTED
                           │
                    restart / terminate
Active means the transaction is executing. Partially committed means the final statement has executed but durability has not necessarily been completed. Committed means the transaction completed successfully. Failed means it cannot continue. Aborted means its effects have been rolled back.
The DBMS transaction manager coordinates execution, while the concurrency-control and recovery components ensure correct behavior under concurrent access and failure.
