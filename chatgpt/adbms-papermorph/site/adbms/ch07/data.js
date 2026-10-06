const CHAPTER={
  "number": 7,
  "unit": "Unit 3 · Transactions & Recovery",
  "title": "7. Concurrency, Locks, Deadlocks & Recovery",
  "beats": [
    {
      "title": "WHY CONCURRENCY CONTROL?",
      "body": "Interleaving can produce incorrect results even when each transaction is correct by itself. Common anomalies: lost update, dirty read, non-repeatable read, phantom read.",
      "purpose": "Memorize anomaly → meaning pairs.",
      "diagram": "flow",
      "memory": "Lost = overwrite. Dirty = uncommitted. Non-repeatable = same row, different value. Phantom = different set of rows.",
      "trap": null,
      "items": [
        {
          "label": "LOST UPDATE",
          "hot": true
        },
        {
          "label": "DIRTY READ"
        },
        {
          "label": "NON-REPEATABLE"
        },
        {
          "label": "PHANTOM"
        }
      ]
    },
    {
      "title": "SERIALIZABILITY",
      "body": "A serial schedule runs transactions one after another. A serializable schedule may interleave but has an effect equivalent to some serial schedule.",
      "purpose": "Serializability = correctness with concurrency.",
      "diagram": "flow",
      "memory": null,
      "trap": null,
      "items": [
        {
          "label": "INTERLEAVE",
          "hot": true
        },
        {
          "label": "PRECEDENCE GRAPH"
        },
        {
          "label": "ACYCLIC?"
        }
      ]
    },
    {
      "title": "PRECEDENCE GRAPH",
      "body": "Create one node per transaction. For conflicting operations on the same item where at least one is a write, add Ti → Tj if Ti occurs first. Acyclic graph = conflict-serializable; cycle = not conflict-serializable.",
      "purpose": "This is a procedure—write the steps.",
      "diagram": "flow",
      "memory": "Cycle = trouble.",
      "trap": null,
      "items": [
        {
          "label": "NODES",
          "hot": true
        },
        {
          "label": "CONFLICT EDGE"
        },
        {
          "label": "CHECK CYCLE"
        }
      ]
    },
    {
      "title": "LOCKS: S vs X",
      "body": "Shared (S) lock is for reading and can coexist with other S locks. Exclusive (X) lock is for writing and conflicts with S and X.",
      "purpose": "The 2×2 compatibility table is easy marks.",
      "diagram": "flow",
      "memory": null,
      "trap": null,
      "items": [
        {
          "label": "S + S ✓",
          "hot": true
        },
        {
          "label": "S + X ✗"
        },
        {
          "label": "X + X ✗"
        }
      ]
    },
    {
      "title": "TWO-PHASE LOCKING",
      "body": "Growing phase: acquire locks, no releases. Shrinking phase: release locks, no new acquisitions. Basic 2PL guarantees conflict serializability. Strict 2PL keeps exclusive locks until commit/abort, reducing cascading rollback problems.",
      "purpose": "Draw the phases + lock point.",
      "diagram": "2pl",
      "memory": "Grow = grab. Shrink = surrender.",
      "trap": null
    },
    {
      "title": "DEADLOCK",
      "body": "Deadlock occurs when transactions wait in a cycle. Example: T1 holds A and waits for B; T2 holds B and waits for A. Handling: prevention, avoidance, detection with wait-for graph, timeout.",
      "purpose": "The word “cycle” should immediately trigger deadlock.",
      "diagram": "flow",
      "memory": "Deadlock = circular waiting.",
      "trap": null,
      "items": [
        {
          "label": "T1 holds A",
          "hot": true
        },
        {
          "label": "waits B"
        },
        {
          "label": "T2 holds B"
        },
        {
          "label": "waits A"
        }
      ]
    },
    {
      "title": "TIMESTAMP ORDERING",
      "body": "Each transaction gets a unique timestamp. Read_TS(X) records the largest timestamp that successfully read X; Write_TS(X) records the largest timestamp that successfully wrote X. Violations may abort/restart the transaction. Advantage: no lock-waiting deadlock; disadvantage: repeated aborts can waste work.",
      "purpose": "Good comparison against 2PL.",
      "diagram": "flow",
      "memory": null,
      "trap": null,
      "items": [
        {
          "label": "TIMESTAMP",
          "hot": true
        },
        {
          "label": "READ_TS / WRITE_TS"
        },
        {
          "label": "ORDER CHECK"
        },
        {
          "label": "ABORT / RESTART"
        }
      ]
    },
    {
      "title": "RECOVERY: FAILURE TYPES",
      "body": "Transaction failure: logical error, constraint violation, deadlock victim, explicit abort. System crash: volatile memory lost. Media failure: persistent storage damaged. Communication failure matters especially in distributed DBs.",
      "purpose": "Always enumerate the failure types before explaining recovery methods.",
      "diagram": "flow",
      "memory": null,
      "trap": null,
      "items": [
        {
          "label": "TX FAILURE"
        },
        {
          "label": "SYSTEM CRASH"
        },
        {
          "label": "MEDIA",
          "hot": true
        },
        {
          "label": "COMMUNICATION"
        }
      ]
    },
    {
      "title": "RECOVERY METHODS",
      "body": "Deferred update: database changes delayed until commit; committed work may need REDO. Immediate update: data may be written before commit; recovery may need UNDO + REDO. Shadow paging keeps stable shadow mapping until root switches at commit. Log-based recovery uses sequential logs. WAL requires the log record to reach stable storage before the changed data page. Checkpoints reduce recovery work.",
      "purpose": "This sequence itself is an exam answer plan.",
      "diagram": "recovery",
      "memory": "Deferred → mostly REDO. Immediate → UNDO + REDO. Shadow → switch root at commit.",
      "trap": null
    },
    {
      "title": "EXAM ATTACK: RECOVERY ANSWER",
      "body": "Define recovery → failure types → deferred update → immediate update → shadow paging → log + WAL → checkpoint → UNDO/REDO → conclusion.",
      "purpose": "Memorize this order.",
      "diagram": "recovery",
      "memory": null,
      "trap": null
    }
  ],
  "quiz": [
    {
      "q": "Which 2PL phase forbids acquiring new locks?",
      "opts": [
        "Growing",
        "Shrinking",
        "Lock point",
        "Commit"
      ],
      "a": 1,
      "why": "Shrinking phase releases locks and acquires no new locks.",
      "whyWrong": "Growing phase is the acquisition phase."
    },
    {
      "q": "WAL requires…",
      "opts": [
        "Data page first, log later",
        "Log record first, then changed data page",
        "No log",
        "Only checkpoints"
      ],
      "a": 1,
      "why": "Write-Ahead Logging writes the log to stable storage before the corresponding changed page.",
      "whyWrong": "That is the core WAL guarantee."
    }
  ]
};