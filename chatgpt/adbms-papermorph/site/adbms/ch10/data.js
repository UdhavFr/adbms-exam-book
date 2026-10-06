const CHAPTER={
  "number": 10,
  "unit": "Unit 5 · NoSQL & Modern Stores",
  "title": "10. Cassandra, Redis, Graphs, Vectors & Indexing",
  "beats": [
    {
      "title": "COLUMN-FAMILY / WIDE-COLUMN",
      "body": "HBase and Cassandra are designed for huge datasets, horizontal scaling and high-throughput distributed workloads. HBase is associated with Hadoop and uses row keys + column families. Cassandra uses partition keys + clustering columns.",
      "purpose": "Know the structural distinction.",
      "diagram": "flow",
      "memory": "Cassandra: partition key = where; clustering = order within partition.",
      "trap": null,
      "items": [
        {
          "label": "HBASE\nROW KEY + CF",
          "hot": true
        },
        {
          "label": "CASSANDRA\nPARTITION + CLUSTERING"
        }
      ]
    },
    {
      "title": "CASSANDRA QUERY-DRIVEN DESIGN",
      "body": "CQL resembles SQL syntactically, but the data model and query restrictions differ. Cassandra tables are commonly modeled around query patterns; deliberately duplicated data can avoid expensive joins.",
      "purpose": "The mental model is “design for the query”.",
      "diagram": "flow",
      "memory": "Cassandra ≠ normalized relational modeling; duplicate when it serves the query.",
      "trap": null,
      "items": [
        {
          "label": "QUERY PATTERN",
          "hot": true
        },
        {
          "label": "PARTITION KEY"
        },
        {
          "label": "CLUSTERING ORDER"
        }
      ]
    },
    {
      "title": "REDIS = FAST KEY-VALUE",
      "body": "Redis is an in-memory data store used for caching, sessions, counters, queues, leaderboards and fast temporary state. Key commands: SET, GET, DEL, EXISTS, HSET, HGET, EXPIRE, INCR.",
      "purpose": "The use-case list is more important than memorizing prose.",
      "diagram": "flow",
      "memory": "Redis = fast temporary state.",
      "trap": null,
      "items": [
        {
          "label": "SET / GET",
          "hot": true
        },
        {
          "label": "CACHE"
        },
        {
          "label": "SESSION"
        },
        {
          "label": "COUNTER"
        }
      ]
    },
    {
      "title": "GRAPH DATA MODEL",
      "body": "Nodes are entities, relationships are connections, properties are attributes. Graph databases are suited to relationship-heavy queries such as social networks, recommendations, fraud detection, knowledge graphs, dependency analysis.",
      "purpose": "The graph picture itself is the explanation.",
      "diagram": "graph",
      "memory": "Node = thing. Edge = relationship. Property = detail.",
      "trap": null
    },
    {
      "title": "NEO4J + CYPHER",
      "body": "Neo4j uses nodes, relationships, labels and properties. Cypher represents graph patterns with ASCII-like syntax. Core operations in the notes: CREATE node, MATCH + CREATE relationship, MATCH + RETURN, WHERE filter, SET update, DETACH DELETE.",
      "purpose": "Pattern syntax is more memorable than definitions alone.",
      "diagram": "graph",
      "memory": "MATCH finds patterns. CREATE adds. SET changes. DELETE removes.",
      "trap": null
    },
    {
      "title": "VECTOR EMBEDDINGS",
      "body": "An embedding maps text/image/audio/product information into a numerical vector. Semantically similar items are intended to be near each other in vector space. Similarity measures: cosine similarity, Euclidean distance, dot product.",
      "purpose": "Understand the pipeline, not the buzzword.",
      "diagram": "vector",
      "memory": "Data → embedding → vector → nearest-neighbor search.",
      "trap": null
    },
    {
      "title": "SIMILARITY SEARCH + ANN",
      "body": "Similarity search embeds the query, searches an index, returns nearest neighbors/top-k plus metadata/original documents. Brute force compares against every vector; ANN searches a promising subset for lower latency. HNSW is graph-based ANN. IVF-style methods partition vectors into groups and search relevant groups.",
      "purpose": "HNSW and IVF are the two named ideas in the notes.",
      "diagram": "vector",
      "memory": "ANN trades exact exhaustiveness for speed.",
      "trap": null
    },
    {
      "title": "NOSQL INDEXING",
      "body": "Indexes reduce scans and latency, support selective filtering and may support sorting/range or nearest-neighbor retrieval. Costs: storage, write maintenance, memory/cache pressure, possible ineffectiveness and distributed-design complexity. MongoDB supports single-field, compound, multikey, text, geospatial and unique indexes.",
      "purpose": "Index the query pattern, not everything.",
      "diagram": "index",
      "memory": "Index = faster reads + maintenance cost.",
      "trap": null
    },
    {
      "title": "CASSANDRA / NEO4J / VECTOR INDEXING",
      "body": "Cassandra: partition key determines where data lives; clustering columns determine row order within the partition. Neo4j: property indexes help locate starting nodes before traversal; Cypher ORDER BY expresses ordering. Vector indexes such as HNSW/IVF target similarity/nearest-neighbor search rather than scalar equality/range.",
      "purpose": "This is the final cross-model comparison.",
      "diagram": "flow",
      "memory": "Scalar access ≠ similarity access.",
      "trap": null,
      "items": [
        {
          "label": "CASSANDRA\nPARTITION",
          "hot": true
        },
        {
          "label": "NEO4J\nPROPERTY"
        },
        {
          "label": "VECTOR\nHNSW / IVF"
        }
      ]
    },
    {
      "title": "FINAL EXAM ATTACK",
      "body": "For a NoSQL indexing 20-marker: define index → explain why → relational/B+ vs hash → MongoDB → CouchDB → Cassandra primary-key design → Neo4j property indexes → vector indexes → benefits/costs → query-driven conclusion.",
      "purpose": "This is explicitly the notebook’s exam-ready route.",
      "diagram": "index",
      "memory": null,
      "trap": null
    }
  ],
  "quiz": [
    {
      "q": "In Cassandra, the partition key primarily determines…",
      "opts": [
        "The graph traversal",
        "Where the data/partition lives",
        "The JSON field name",
        "The vector embedding"
      ],
      "a": 1,
      "why": "Partition key chooses the partition/location.",
      "whyWrong": "Clustering columns govern order within a partition."
    },
    {
      "q": "HNSW is best described as…",
      "opts": [
        "A graph-based ANN technique",
        "A SQL isolation level",
        "A hash collision strategy",
        "A MongoDB CRUD command"
      ],
      "a": 0,
      "why": "HNSW is a graph-based approximate nearest-neighbor technique.",
      "whyWrong": "The other options belong to unrelated topics."
    }
  ]
};