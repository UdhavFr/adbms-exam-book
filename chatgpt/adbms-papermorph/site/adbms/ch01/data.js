const CHAPTER={
  "number": 1,
  "unit": "Unit 1 · Foundations",
  "title": "1. Database Systems & Three-Level Architecture",
  "beats": [
    {
      "title": "DATABASE SYSTEM = DATA + DBMS",
      "body": "A database is an organized collection of logically related data. A DBMS defines, stores, retrieves, updates, protects and recovers that data. The database together with the DBMS forms a database system.",
      "purpose": "Lock this definition first: it is the opening sentence for many 20-mark answers.",
      "diagram": "flow",
      "memory": "DBMS = define + store + retrieve + update + protect + recover",
      "trap": "Do not jump straight to features. Start with a clean definition and why the system is needed.",
      "items": [
        {
          "label": "USERS / APPS",
          "hot": true
        },
        {
          "label": "DBMS"
        },
        {
          "label": "DATABASE"
        }
      ]
    },
    {
      "title": "WHY FILE SYSTEMS HURT",
      "body": "Repeated copies create redundancy; changing one copy but not another creates inconsistency. File systems also make sharing, security, concurrent access and failure recovery difficult.",
      "purpose": "Examiners love “problem → DBMS solution” because it proves why DBMS exists.",
      "diagram": "flow",
      "memory": "Redundancy → inconsistency → DBMS controls the mess.",
      "trap": null,
      "items": [
        {
          "label": "FILE PROBLEMS",
          "hot": true
        },
        {
          "label": "DBMS CONTROLS"
        },
        {
          "label": "RELIABLE DATA"
        }
      ]
    },
    {
      "title": "THE THREE-LEVEL MAP",
      "body": "External level gives user-specific views. Conceptual level describes the complete logical database. Internal level describes files, pages, record placement, indexes and access paths.",
      "purpose": "Draw this almost automatically in the exam.",
      "diagram": "levels",
      "memory": "External = what user sees; Conceptual = logical blueprint; Internal = storage details.",
      "trap": "Do not swap conceptual and internal."
    },
    {
      "title": "DATA INDEPENDENCE",
      "body": "Physical data independence: change storage structures without changing the conceptual schema. Logical data independence: change the conceptual schema without forcing every external view/application to change when the required information can still be provided.",
      "purpose": "A two-row comparison is enough for a strong sub-answer.",
      "diagram": "flow",
      "memory": "Physical = storage changes. Logical = schema changes.",
      "trap": null,
      "items": [
        {
          "label": "PHYSICAL CHANGE",
          "hot": true
        },
        {
          "label": "LOGICAL SCHEMA"
        },
        {
          "label": "APP STAYS"
        }
      ]
    },
    {
      "title": "SCHEMA vs INSTANCE",
      "body": "Schema is the database design/structure: relations, attributes, keys, constraints, indexes, views and other objects. Instance is the actual data at a particular moment.",
      "purpose": "Use the blueprint analogy when stuck.",
      "diagram": "flow",
      "memory": "Schema = structure. Instance = state.",
      "trap": null,
      "items": [
        {
          "label": "SCHEMA\nBLUEPRINT",
          "hot": true
        },
        {
          "label": "INSTANCE\nCURRENT STATE"
        }
      ]
    },
    {
      "title": "EXAM ATTACK: Q1",
      "body": "If asked “Explain database systems”, build: definition → file-system problems → DBMS functions → three-level architecture → data independence → example → advantages → conclusion.",
      "purpose": "This is the source notebook’s answer-writing template turned into a recall route.",
      "diagram": "flow",
      "memory": null,
      "trap": null
    }
  ],
  "quiz": [
    {
      "q": "Which level hides physical storage details from end users?",
      "opts": [
        "External",
        "Conceptual",
        "Internal",
        "Storage device"
      ],
      "a": 0,
      "why": "External level provides customized user views.",
      "whyWrong": "Internal level is where physical representation is described."
    },
    {
      "q": "Schema means…",
      "opts": [
        "Current data values",
        "Database blueprint/structure",
        "Only indexes",
        "Only user views"
      ],
      "a": 1,
      "why": "Schema is the relatively stable logical design.",
      "whyWrong": "Current values are the instance."
    }
  ]
};