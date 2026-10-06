# 6. Lock-Based Concurrency Control and 2PL

Source: ADBMS_MasterNotes.docx — folder `u3ch06`

### 6. Lock-Based Concurrency Control and 2PL
_(p. 17)_
A lock is a concurrency-control mechanism that controls access to a data item. A shared lock S is used for reading and can be compatible with other shared locks. An exclusive lock X is used for writing and conflicts with both S and X locks.

| Held/requested | S | X |
|---|---|---|
| S | Compatible | Not compatible |
| X | Not compatible | Not compatible |

#### Two-Phase Locking
_(p. 18)_
Two-phase locking divides a transaction into a growing phase and shrinking phase. During the growing phase, the transaction may acquire locks but cannot release them. During the shrinking phase, it may release locks but cannot acquire new locks.
TIME →
┌──────────────────────┬─────────────────────┐
│ GROWING PHASE        │ SHRINKING PHASE     │
│ acquire locks        │ release locks       │
│ no releases          │ no new acquisitions │
└──────────────────────┴─────────────────────┘
            LOCK POINT
       (last lock acquisition)
Basic 2PL guarantees conflict serializability. Strict 2PL holds exclusive locks until commit/abort, reducing cascading rollback problems. Rigorous 2PL can hold both shared and exclusive locks until completion.
#### Deadlock
_(p. 18)_
Deadlock occurs when transactions wait in a cycle. Example: T1 holds A and waits for B, while T2 holds B and waits for A.
T1 holds A → waits for B
      ↑             ↓
T2 waits for A ← holds B
            CYCLE = DEADLOCK
- Prevention: impose rules that prevent circular wait.
- Avoidance: grant requests only when safe under the chosen protocol.
- Detection: construct a wait-for graph and detect cycles.
- Timeout: abort a transaction that waits too long.
