# 7. Timestamp-Based Concurrency Control

Source: ADBMS_MasterNotes.docx — folder `u3ch07`

### 7. Timestamp-Based Concurrency Control
_(p. 18)_
Timestamp ordering assigns every transaction a unique timestamp. Older transactions have smaller timestamps. The protocol ensures conflicting operations occur in timestamp order.
For each data item X, Read_TS(X) stores the largest timestamp of a transaction that successfully read X, while Write_TS(X) stores the largest timestamp of a transaction that successfully wrote X.
If a requested read or write would violate the timestamp ordering rules, the transaction may be rejected/aborted and restarted. A major advantage is that transactions do not wait for locks, so deadlocks due to lock waiting are avoided. A disadvantage is that repeated aborts can waste work.
