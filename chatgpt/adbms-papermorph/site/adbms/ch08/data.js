const CHAPTER={
  "number": 8,
  "unit": "Unit 4 · Distributed & NoSQL",
  "title": "8. Distributed DB, Fragmentation, Replication & 2PC",
  "beats": [
    {
      "title": "DISTRIBUTED DATABASE",
      "body": "A distributed database is logically integrated but physically distributed across network-connected sites. DDBMS coordinates the sites and offers a unified way to access data.",
      "purpose": "Think “one logical database, many physical sites.”",
      "diagram": "dist",
      "memory": "Logical unity, physical distribution.",
      "trap": null
    },
    {
      "title": "TYPES + TRADE-OFFS",
      "body": "Homogeneous systems use similar DBMS technology. Heterogeneous systems may combine technologies/schemas. Federated systems let independently managed databases cooperate.",
      "purpose": "Keep type definitions short and exact.",
      "diagram": "flow",
      "memory": null,
      "trap": null
    },
    {
      "title": "FRAGMENTATION",
      "body": "Horizontal fragmentation divides rows by predicates. Vertical fragmentation divides columns, usually repeating the key so the original relation can be reconstructed by join. Hybrid combines both. Correct fragmentation considers completeness, reconstruction and disjointness where required.",
      "purpose": "Draw row split vs column split.",
      "diagram": "flow",
      "memory": "Horizontal = rows. Vertical = columns.",
      "trap": null,
      "items": [
        {
          "label": "RELATION R",
          "hot": true
        },
        {
          "label": "HORIZONTAL\nROWS"
        },
        {
          "label": "VERTICAL\nCOLUMNS"
        },
        {
          "label": "HYBRID"
        }
      ]
    },
    {
      "title": "REPLICATION + ALLOCATION",
      "body": "Replication keeps multiple copies at sites. Full replication copies broadly; partial replication copies selectively. Benefits: availability, local reads, failure tolerance, less remote access. Costs: storage, update coordination, consistency management. Allocation decides where fragments/replicas live based on query frequency, locality, communication cost, capacity and reliability.",
      "purpose": "A benefits-vs-costs table is exam-friendly.",
      "diagram": "flow",
      "memory": null,
      "trap": null
    },
    {
      "title": "2PC: THE ATOMIC COMMIT PROTOCOL",
      "body": "Coordinator sends PREPARE. Participants check and vote YES/NO. If all required votes are YES, coordinator sends COMMIT; otherwise ABORT. Participants record and execute the decision. 2PC can block in some failures, especially after participants are prepared but before learning the coordinator’s final decision.",
      "purpose": "Draw the coordinator above participants.",
      "diagram": "flow",
      "memory": "2PC = ask → vote → decide → record.",
      "trap": null,
      "items": [
        {
          "label": "COORDINATOR",
          "hot": true
        },
        {
          "label": "PREPARE"
        },
        {
          "label": "VOTE YES/NO"
        },
        {
          "label": "COMMIT / ABORT"
        }
      ]
    },
    {
      "title": "CONSISTENCY MODELS",
      "body": "Strong/linearizable-style consistency gives a single real-time-respecting order under the model. Eventual consistency allows temporary disagreement but convergence if updates stop. Causal consistency preserves causal ordering. Session guarantees can include read-your-writes and monotonic reads.",
      "purpose": "Stronger consistency can require more coordination and affect latency/availability.",
      "diagram": "flow",
      "memory": null,
      "trap": null
    },
    {
      "title": "EXAM ATTACK: DISTRIBUTED DB",
      "body": "Definition → architecture → characteristics/types → fragmentation → replication/allocation → distributed transactions → 2PC diagram → consistency models → conclusion.",
      "purpose": "Do not skip the diagram.",
      "diagram": "dist",
      "memory": null,
      "trap": null
    }
  ],
  "quiz": [
    {
      "q": "Vertical fragmentation divides…",
      "opts": [
        "Rows",
        "Columns",
        "Databases",
        "Transactions"
      ],
      "a": 1,
      "why": "Vertical = columns, usually keeping the key for reconstruction.",
      "whyWrong": "Horizontal fragmentation divides rows."
    },
    {
      "q": "In 2PC, who sends PREPARE?",
      "opts": [
        "Each participant to coordinator",
        "Coordinator to participants",
        "The database user",
        "The storage manager"
      ],
      "a": 1,
      "why": "Coordinator starts the prepare round.",
      "whyWrong": "Participants answer the prepare request with votes."
    }
  ]
};