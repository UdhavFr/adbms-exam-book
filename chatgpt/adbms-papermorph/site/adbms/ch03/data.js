const CHAPTER={
  "number": 3,
  "unit": "Unit 1 · Foundations",
  "title": "3. Relational Algebra, SQL & Integrity",
  "beats": [
    {
      "title": "RELATIONAL ALGEBRA = OPERATORS",
      "body": "Selection σ filters rows. Projection π chooses columns. Union combines compatible relations. Difference finds tuples in one but not the other. Cartesian product pairs every tuple. Join combines related tuples using a condition.",
      "purpose": "Know the symbol + purpose pair.",
      "diagram": "flow",
      "memory": "σ = select rows. π = project columns.",
      "trap": null,
      "items": [
        {
          "label": "σ ROWS",
          "hot": true
        },
        {
          "label": "π COLUMNS"
        },
        {
          "label": "JOIN"
        },
        {
          "label": "∪ / − / ×"
        }
      ]
    },
    {
      "title": "SQL CATEGORIES",
      "body": "DDL defines/changes structure: CREATE, ALTER, DROP, TRUNCATE. DML retrieves/changes data: SELECT, INSERT, UPDATE, DELETE. DCL manages privileges: GRANT, REVOKE. TCL controls transactions: COMMIT, ROLLBACK, SAVEPOINT.",
      "purpose": "A table in the exam scores quickly and cleanly.",
      "diagram": "flow",
      "memory": "DDL = structure, DML = data, DCL = permissions, TCL = transactions.",
      "trap": null,
      "items": [
        {
          "label": "DDL"
        },
        {
          "label": "DML",
          "hot": true
        },
        {
          "label": "DCL"
        },
        {
          "label": "TCL"
        }
      ]
    },
    {
      "title": "SQL CLAUSE ORDER",
      "body": "Typical logical idea: FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT, although the optimizer may transform the physical plan.",
      "purpose": "Use this when explaining query processing or writing SQL.",
      "diagram": "flow",
      "memory": "WHERE filters rows; HAVING filters groups.",
      "trap": null,
      "items": [
        {
          "label": "FROM/JOIN",
          "hot": true
        },
        {
          "label": "WHERE"
        },
        {
          "label": "GROUP BY"
        },
        {
          "label": "HAVING"
        },
        {
          "label": "SELECT"
        },
        {
          "label": "ORDER BY"
        }
      ]
    },
    {
      "title": "INTEGRITY CONSTRAINTS",
      "body": "Domain integrity: valid data type/domain. Entity integrity: primary key is unique and not NULL. Referential integrity: foreign key refers to an existing referenced key or may be NULL where allowed. UNIQUE prevents duplicates. CHECK enforces a Boolean condition. NOT NULL makes a value mandatory.",
      "purpose": "These are database-enforced correctness rules.",
      "diagram": "flow",
      "memory": "PK = identity. FK = valid reference.",
      "trap": null,
      "items": [
        {
          "label": "DOMAIN"
        },
        {
          "label": "ENTITY",
          "hot": true
        },
        {
          "label": "REFERENTIAL"
        },
        {
          "label": "CHECK / UNIQUE"
        }
      ]
    },
    {
      "title": "ANOMALIES = DESIGN WARNING",
      "body": "Insertion anomaly: cannot add a fact without unrelated data. Update anomaly: same fact repeated, so one logical change needs many updates. Deletion anomaly: deleting one fact accidentally removes another.",
      "purpose": "This leads directly into normalization.",
      "diagram": "flow",
      "memory": "I-U-D: insert, update, delete anomalies.",
      "trap": null,
      "items": [
        {
          "label": "INSERTION"
        },
        {
          "label": "UPDATE",
          "hot": true
        },
        {
          "label": "DELETION"
        }
      ]
    },
    {
      "title": "EXAM ATTACK: SQL + INTEGRITY",
      "body": "Define SQL as declarative; classify commands; give one DDL + one DML + one TCL example; explain WHERE/GROUP BY/HAVING; finish with integrity constraints and why they matter.",
      "purpose": "This converts scattered facts into one 20-mark answer.",
      "diagram": "flow",
      "memory": null,
      "trap": null
    }
  ],
  "quiz": [
    {
      "q": "Which clause filters groups after GROUP BY?",
      "opts": [
        "WHERE",
        "HAVING",
        "ORDER BY",
        "LIMIT"
      ],
      "a": 1,
      "why": "HAVING filters groups.",
      "whyWrong": "WHERE filters rows before grouping."
    },
    {
      "q": "Entity integrity requires primary-key values to be…",
      "opts": [
        "Nullable and duplicated",
        "Unique and non-NULL",
        "Sorted",
        "Encrypted"
      ],
      "a": 1,
      "why": "A primary key identifies tuples and cannot be NULL.",
      "whyWrong": "Sorting/encryption are unrelated to entity integrity."
    }
  ]
};