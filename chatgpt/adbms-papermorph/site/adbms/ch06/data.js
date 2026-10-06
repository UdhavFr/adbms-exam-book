const CHAPTER={
  "number": 6,
  "unit": "Unit 3 · Transactions & Recovery",
  "title": "6. Transactions, ACID & Isolation",
  "beats": [
    {
      "title": "TRANSACTION = ONE LOGICAL UNIT",
      "body": "A transaction is a sequence of database operations forming one logical unit of work. Bank transfer is the classic example: debit A and credit B must behave together.",
      "purpose": "Lead with this when asked about transactions.",
      "diagram": "flow",
      "memory": "Transaction = all operations needed for one logical job.",
      "trap": null,
      "items": [
        {
          "label": "BEGIN",
          "hot": true
        },
        {
          "label": "READ/WRITE A"
        },
        {
          "label": "READ/WRITE B"
        },
        {
          "label": "COMMIT / ROLLBACK"
        }
      ]
    },
    {
      "title": "TRANSACTION STATES",
      "body": "Active → Partially committed → Committed. Failure path: Failed → Aborted → restart/terminate.",
      "purpose": "Draw this flow for transaction-state questions.",
      "diagram": "flow",
      "memory": null,
      "trap": "Partially committed means the final statement ran, but durability is not necessarily completed yet.",
      "items": [
        {
          "label": "ACTIVE",
          "hot": true
        },
        {
          "label": "PARTIALLY COMMITTED"
        },
        {
          "label": "COMMITTED"
        }
      ]
    },
    {
      "title": "ACID: THE BIG FOUR",
      "body": "Atomicity = all-or-nothing. Consistency = integrity rules remain valid. Isolation = concurrent transactions behave under the chosen isolation guarantee. Durability = committed effects survive later failure subject to the DBMS guarantee.",
      "purpose": "Explain every property with the bank transfer.",
      "diagram": "acid",
      "memory": "A = all, C = correct, I = isolated, D = durable.",
      "trap": null
    },
    {
      "title": "SQL TRANSACTIONS",
      "body": "BEGIN/START TRANSACTION groups statements. COMMIT makes them durable. ROLLBACK undoes uncommitted work. SAVEPOINT creates an intermediate rollback point.",
      "purpose": "Know the command flow, not isolated commands.",
      "diagram": "flow",
      "memory": null,
      "trap": null,
      "items": [
        {
          "label": "BEGIN",
          "hot": true
        },
        {
          "label": "SQL WORK"
        },
        {
          "label": "COMMIT"
        },
        {
          "label": "ROLLBACK"
        }
      ]
    },
    {
      "title": "ISOLATION LEVELS",
      "body": "Read Uncommitted may permit dirty reads. Read Committed prevents ordinary dirty reads. Repeatable Read gives stronger repeated-read guarantees; phantom behavior varies by DBMS. Serializable is the strongest standard level and aims for serial-equivalent behavior.",
      "purpose": "Use careful wording: exact behavior can vary by DBMS.",
      "diagram": "flow",
      "memory": "Strength rises → concurrency freedom generally falls.",
      "trap": null,
      "items": [
        {
          "label": "READ\nUNCOMMITTED"
        },
        {
          "label": "READ\nCOMMITTED"
        },
        {
          "label": "REPEATABLE\nREAD"
        },
        {
          "label": "SERIALIZABLE",
          "hot": true
        }
      ]
    },
    {
      "title": "EXAM ATTACK: ACID ANSWER",
      "body": "Definition → bank transfer → four properties with one line + example each → SQL transaction support → isolation levels → conclude with reliability and correctness.",
      "purpose": "This is one of the highest-value answers in the notebook.",
      "diagram": "acid",
      "memory": null,
      "trap": null
    }
  ],
  "quiz": [
    {
      "q": "Which ACID property says a transaction is all-or-nothing?",
      "opts": [
        "Consistency",
        "Atomicity",
        "Isolation",
        "Durability"
      ],
      "a": 1,
      "why": "Atomicity is the all-or-nothing property.",
      "whyWrong": "Consistency is about valid state and constraints."
    }
  ]
};