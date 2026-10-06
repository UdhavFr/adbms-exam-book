# 5. Concurrency Control and Serializability

Source: ADBMS_MasterNotes.docx — folder `u3ch05`

### 5. Concurrency Control and Serializability
_(p. 17)_
Concurrency control is the set of techniques used to coordinate simultaneous transactions. It is necessary because interleaving operations can produce incorrect results even when each transaction is correct by itself.
#### Common anomalies
_(p. 17)_

| Anomaly | Meaning |
|---|---|
| Lost update | A later write overwrites an earlier write from another transaction. |
| Dirty read | A transaction reads a value written by another transaction that has not committed. |
| Non-repeatable read | A row read twice gives different committed values because another transaction updated it between reads. |
| Phantom read | A repeated predicate query returns a different set of rows due to another transaction's insert/delete/update affecting the predicate. |

#### Serial vs serializable
_(p. 17)_
A serial schedule executes transactions one after another. A serializable schedule may interleave operations but produces an effect equivalent to some serial schedule. Serializability provides correctness while allowing concurrency.
#### Conflict serializability
_(p. 17)_
Construct a precedence graph with one node per transaction. If two conflicting operations access the same item, at least one is a write, and Ti's operation occurs before Tj's operation, add Ti → Tj. If the graph is acyclic, the schedule is conflict-serializable. If it contains a cycle, it is not conflict-serializable.
T1                 T2
 |                  |
R(X)               
 |                  |
W(X) ───────────→ R(X)
 |                  |
COMMIT             COMMIT

Conflict creates edge T1 → T2.
Check graph for cycles.
