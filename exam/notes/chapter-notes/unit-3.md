# UNIT 3 — Transaction Processing, Concurrency Control and Recovery
Source: `ADBMS_MasterNotes.docx` Unit 3, pp. 15–21 · structure `u3ch01`–`u3ch12`
The source's **Question 2** (20 marks) spans this entire unit — it is the longest single answer in the exam.

---

## U3-1 Concept of a Transaction — **P0** (p. 15)
- **WHAT:** a sequence of database operations forming **one logical unit of work** (read/write/insert/update/delete/control) that must preserve correctness under concurrency and failure.
- **ANCHOR:** bank transfer — debit A ₹500, credit B ₹500; crash in between ⇒ wrong DB unless atomicity holds.
- **FLOW:** BEGIN → READ/WRITE A → READ/WRITE B → COMMIT (permanent) | failure → ROLLBACK/RECOVERY.
- **MISTAKE:** defining a transaction as "a single query" — it is a *unit of work*, possibly many statements.

## U3-2 Transaction States and System Concepts — **P1** (p. 15)
- **STATES:** ACTIVE → (last statement) → PARTIALLY COMMITTED → (success) COMMITTED; failure → FAILED → ROLLBACK → ABORTED → restart/terminate.
- **COMPONENTS:** transaction manager coordinates; concurrency-control and recovery components guarantee correct behaviour.
- **MISTAKE:** skipping PARTIALLY COMMITTED (it is in the source diagram and named in answers).

## U3-3 ACID Properties — **P0** (p. 16) ← *highest-value Unit 3 topic*
- **A — Atomicity:** all-or-nothing; failure of an essential operation ⇒ roll back the whole transaction. *Bank: debit **and** credit both occur.*
- **C — Consistency:** every committed transaction preserves integrity constraints and valid rules. *No invalid account state.*
- **I — Isolation:** intermediate effects of concurrent transactions are controlled so execution is equivalent to an acceptable serial behaviour. *Nobody sees a half-completed transfer.*
- **D — Durability:** after commit, effects survive subsequent system failure, subject to the DBMS's durability guarantees. *Still there after restart.*
- **EXAM WRITE:** one definition line + one bank example line **per property** (that is how the source says to answer).
- **MISTAKE:** writing ACID as four words with no explanation; or "durability = nothing is ever lost" (unqualified).

## U3-4 Transaction Support in SQL + Isolation Levels — **P1** (p. 16)
- **FLOW:** BEGIN/START TRANSACTION → operations → COMMIT (success) / ROLLBACK (error); SAVEPOINT = intermediate rollback point.
- **LEVELS:** Read Uncommitted → Read Committed → Repeatable Read → Serializable (increasing strength; phantom behaviour at RR varies by DBMS — errata E3/E4).
- **MISTAKE:** claiming SQL is *written* in the FROM-first order; forgetting SAVEPOINT.

## U3-5 Concurrency Control and Serializability — **P0** (pp. 17–18)
- **WHY:** interleaving can produce incorrect results even when each transaction alone is correct.
- **ANOMALIES:** lost update (later write overwrites) · dirty read (read uncommitted) · non-repeatable read (same row, two reads, different committed values) · phantom (same predicate, different row set).
- **SERIAL vs SERIALIZABLE:** serial = one after another; serializable = interleaved but equivalent to *some* serial schedule.
- **CONFLICT SERIALIZABILITY ALGORITHM:** node per transaction → edge Ti→Tj for conflicting ops (same item, ≥1 write) with Ti first → **acyclic = conflict-serializable**, cycle = not.
- **EXAM WRITE:** anomalies table → definitions → the 4-step graph algorithm with a small schedule example.
- **MISTAKE:** drawing an edge for a read–read pair (not a conflict).

## U3-6 Lock-Based Concurrency Control and 2PL — **P0** (p. 18)
- **LOCKS:** S (shared, read, compatible with S) · X (exclusive, write, conflicts with S and X).
- **2PL:** GROWING (acquire, no release) → **LOCK POINT** → SHRINKING (release, no new acquisition).
- **VARIANTS:** basic ⇒ conflict serializability · strict ⇒ hold **X** until commit/abort (fewer cascading rollbacks) · rigorous ⇒ hold **S and X** until completion.
- **DEADLOCK:** T1 holds A waits B, T2 holds B waits A → cycle. Handling: **PADT** = Prevention, Avoidance, Detection (wait-for graph), Timeout.
- **MISTAKE:** describing 2PL as "lock everything at the start" instead of the phase rule; confusing strict vs rigorous.

## U3-7 Timestamp-Based Concurrency Control — **P1** (p. 18)
- **WHAT:** unique timestamp per transaction (older = smaller); per item X: Read_TS(X) = largest successful reader's timestamp, Write_TS(X) = largest successful writer's.
- **RULE:** a read/write that would violate timestamp order ⇒ reject/abort and restart.
- **PRO/CON:** no lock waiting ⇒ lock-based deadlock avoided · repeated aborts waste work.
- **MISTAKE:** saying timestamp ordering "eliminates all aborts".

## U3-8 Recovery and Types of Failures — **P1** (p. 19)
- **WHAT:** restoring the database to a consistent state after failure.
- **FAILURES:** transaction (logical error, constraint violation, deadlock victim, explicit abort) · system crash (loses volatile memory) · media failure (loses persistent data) · communication failure (critical in distributed DBs).
- **TOOLS:** logs, checkpoints, backups, shadow structures, undo/redo.
- **MISTAKE:** not distinguishing crash (volatile memory lost) from media failure (persistent data lost).

## U3-9 Deferred Update — **P0** (p. 19)
- **FLOW:** Transaction → write log records → continue execution (no DB write) → COMMIT → **REDO**/apply updates → durable DB.
- **AFTER CRASH:** committed may need REDO; uncommitted **normally need no DB UNDO** (changes were deferred).
- **HOOK:** *Deferred = delay the data.*

## U3-10 Immediate Update — **P0** (p. 20)
- **FLOW:** Transaction → log old/new values → data page may be written before commit → COMMIT? YES ⇒ REDO if needed · NO ⇒ **UNDO**.
- **AFTER CRASH:** UNDO uncommitted **and** REDO committed-that-may-not-have-reached-disk.
- **HOOK:** *Immediate = data may already be on disk.*

## U3-11 Shadow Paging — **P1** (p. 20)
- **FLOW:** stable SHADOW page table + current page table; modified pages go to new locations; **COMMIT: root switches to current**; **CRASH before commit: use the shadow mapping**.
- **TRADE-OFF:** simple recovery, consistent old version always available ↔ fragmentation and page-table management overhead.
- **MISTAKE:** saying the shadow table is updated during execution (it is *stable*; the current table changes).

## U3-12 Log-Based Recovery, WAL, Checkpoints — **P0** (pp. 20–21)
- **LOG:** sequential record on stable storage: transaction ID, data item, old value, new value. Example `<T1 START> <T1, A, 100, 50> <T1 COMMIT>`.
- **WAL:** the relevant log record must reach **stable storage before** the corresponding data page is written — otherwise recovery lacks the information to undo/redo.
- **CHECKPOINT:** recovery starts from a recent checkpoint instead of scanning the whole log.
- **MASTER RECOVERY FLOW:** DEFINE → FAILURES → DEFERRED → IMMEDIATE → SHADOW → LOG → WAL → CHECKPOINT → UNDO/REDO → CONCLUSION.
- **THE SINGLE RULE:** committed = REDO as needed · uncommitted = UNDO as needed.

---

### Unit 3 exam weighting
- **20-mark:** "Explain transaction processing, concurrency control and recovery" (source's Question 2 — 15 bullet stages).
- **10-mark:** ACID alone · 2PL + deadlock · conflict serializability · deferred vs immediate vs shadow paging.
- **5-mark:** transaction states · isolation levels · anomaly table · timestamp ordering pros/cons.
- **2-mark:** definitions (2PL, WAL, phantom, checkpoint…).
