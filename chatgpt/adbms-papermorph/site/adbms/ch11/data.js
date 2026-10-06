const CHAPTER={
  "number": 11,
  "unit": "Final Boss",
  "title": "11. 20-Mark Answer Builder + Mixed Mock",
  "beats": [
    {
      "title": "THE 20-MARK FORMULA",
      "body": "The notebook’s universal answer shape: 5–7 line introduction → labelled diagram/flow → separate component headings → one practical example → advantages/limitations/applications/comparison → 3–4 line conclusion connecting to correctness, performance, scalability or reliability.",
      "purpose": "This is your “never leave the page blank” template.",
      "diagram": "flow",
      "memory": "D-D-E-E-C-C: Define, Diagram, Explain, Example, Compare, Conclude.",
      "trap": null,
      "items": [
        {
          "label": "DEFINE",
          "hot": true
        },
        {
          "label": "DIAGRAM"
        },
        {
          "label": "EXPLAIN"
        },
        {
          "label": "EXAMPLE"
        },
        {
          "label": "COMPARE"
        },
        {
          "label": "CONCLUDE"
        }
      ]
    },
    {
      "title": "NORMALIZATION BOSS",
      "body": "Prompt: “Explain normalization and all normal forms.” Your skeleton: definition + why redundancy hurts → FDs + candidate keys → 1NF → 2NF → 3NF → BCNF → 4NF → 5NF → lossless + dependency preservation → minimal cover/closure → conclusion.",
      "purpose": "Do not start writing prose until this skeleton exists.",
      "diagram": "norm",
      "memory": null,
      "trap": null
    },
    {
      "title": "TRANSACTION / RECOVERY BOSS",
      "body": "Prompt: “Explain transaction processing, concurrency control and recovery.” Skeleton: transaction + bank transfer → states → ACID → SQL transactions/isolation → anomalies → serializability/precedence graph → locks/2PL → deadlocks → timestamps → failures → deferred/immediate/shadow → log/WAL/checkpoint → UNDO/REDO → conclusion.",
      "purpose": "This is a full-mark road map.",
      "diagram": "recovery",
      "memory": null,
      "trap": null
    },
    {
      "title": "DISTRIBUTED / CAP BOSS",
      "body": "Prompt: “Explain distributed databases and CAP.” Skeleton: DDB definition → architecture → fragmentation → replication/allocation → distributed transactions → 2PC → consistency models → CAP + C/A/P → ACID vs BASE → sharding → design trade-offs.",
      "purpose": "Write the diagram before the paragraphs.",
      "diagram": "cap",
      "memory": null,
      "trap": null
    },
    {
      "title": "NOSQL / MONGO BOSS",
      "body": "Prompt: “Explain NoSQL systems and MongoDB.” Skeleton: NoSQL motivation → four models → compare them → CAP/BASE → sharding → MongoDB model → relational mapping → CRUD → operators → aggregation pipeline → applications → conclusion.",
      "purpose": "This can be answered almost as a checklist.",
      "diagram": "mongo",
      "memory": null,
      "trap": null
    },
    {
      "title": "INDEXING BOSS",
      "body": "Prompt: “Explain indexing in relational and NoSQL databases.” Skeleton: index purpose → pages/I/O → B+ tree + range → hash → compare → MongoDB indexes → CouchDB → Cassandra partition/clustering → Neo4j property index → vector embedding/ANN → benefits/costs → query-driven conclusion.",
      "purpose": "This is the notebook’s explicit 20-mark route.",
      "diagram": "index",
      "memory": null,
      "trap": null
    },
    {
      "title": "EXAM MORNING: WHAT TO MEMORIZE",
      "body": "Memorize definitions exactly where possible: DBMS, schema/instance, 3 levels, FD, 1NF/2NF/3NF/BCNF/4NF/5NF, ACID, serializable, 2PL, deadlock, recovery, distributed database, 2PC, CAP, BASE, sharding, MongoDB mapping, graph model, vector/ANN, B+ vs hash.",
      "purpose": "Everything else can be explained in your own words around the exact anchor terms.",
      "diagram": "flow",
      "memory": "Exact anchors + flexible explanation = safest exam strategy.",
      "trap": null,
      "items": [
        {
          "label": "DEFINITIONS",
          "hot": true
        },
        {
          "label": "DIAGRAMS"
        },
        {
          "label": "EXAMPLES"
        },
        {
          "label": "PRACTICE"
        }
      ]
    },
    {
      "title": "LAST 15-MINUTE LOOP",
      "body": "Close the notes. For each unit, say the 20-mark skeleton out loud. Draw: three-level architecture, ER M:N, normalization ladder, B+ tree, ACID, 2PL, recovery, distributed architecture, CAP, Mongo pipeline. Then answer one mixed question without looking.",
      "purpose": "This is active recall: force your brain to retrieve, not reread.",
      "diagram": "flow",
      "memory": null,
      "trap": null
    }
  ],
  "quiz": [
    {
      "q": "Which sentence is the safest opening for a 20-mark answer?",
      "opts": [
        "Jump straight to an example",
        "Define the concept and explain why it matters",
        "List 20 keywords only",
        "Start with the conclusion"
      ],
      "a": 1,
      "why": "The notebook explicitly recommends a 5–7 line definition + importance introduction.",
      "whyWrong": "A list alone does not show WHAT, WHY, HOW and WHERE."
    },
    {
      "q": "What should a strong 20-mark answer contain besides definitions?",
      "opts": [
        "Only code",
        "Diagram/flow, components, example, trade-offs and conclusion",
        "Only a comparison table",
        "Only advantages"
      ],
      "a": 1,
      "why": "That structure is the notebook’s exam-writing guidance.",
      "whyWrong": "Definitions alone are insufficient."
    },
    {
      "q": "Which pair is correctly matched?",
      "opts": [
        "4NF → join dependency",
        "5NF → multivalued dependency",
        "2NF → partial dependency",
        "BCNF → atomic values"
      ],
      "a": 2,
      "why": "2NF removes partial dependency.",
      "whyWrong": "4NF is MVD; 5NF is JD; 1NF is atomicity; BCNF is determinant super key."
    }
  ]
};