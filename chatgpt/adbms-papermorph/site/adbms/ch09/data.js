const CHAPTER={
  "number": 9,
  "unit": "Unit 4 · Distributed & NoSQL",
  "title": "9. CAP, BASE, Sharding & MongoDB",
  "beats": [
    {
      "title": "CAP: THE PRECISE CLAIM",
      "body": "When a distributed system experiences a network partition, it cannot simultaneously guarantee both strong consistency and availability for every request under the formal CAP definitions.",
      "purpose": "The partition condition matters.",
      "diagram": "cap",
      "memory": "CAP is about behavior DURING a partition.",
      "trap": "Do not write “pick any two of three at all times.”",
      "sel": 2
    },
    {
      "title": "C, A, P",
      "body": "Consistency: a read observes the most recent write according to the model or an error. Availability: every request to a non-failing node gets a non-error response, though not necessarily the latest value. Partition tolerance: the system continues despite network failures separating nodes.",
      "purpose": "Write one clean definition for each letter.",
      "diagram": "cap",
      "memory": null,
      "trap": null,
      "sel": 0
    },
    {
      "title": "ACID vs BASE",
      "body": "ACID emphasizes atomicity, consistency, isolation and durability with strong transaction guarantees. BASE = Basically Available, Soft state, Eventual consistency; many distributed NoSQL architectures emphasize availability and flexible consistency, accepting temporary inconsistency while replicas converge.",
      "purpose": "A direct comparison scores quickly.",
      "diagram": "flow",
      "memory": "ACID = correctness guarantees. BASE = availability + convergence trade-off.",
      "trap": null,
      "items": [
        {
          "label": "ACID",
          "hot": true
        },
        {
          "label": "VS"
        },
        {
          "label": "BASE"
        }
      ]
    },
    {
      "title": "SHARDING",
      "body": "Sharding horizontally distributes records across nodes. Range-based uses key ranges; hash-based uses a hash of the shard key; directory-based uses a mapping service; geographic assigns records by region. A good shard key spreads data and traffic and avoids hotspots/oversized partitions.",
      "purpose": "“Good shard key” is a common conceptual question.",
      "diagram": "flow",
      "memory": "Range = locality, Hash = balance, Directory = lookup map, Geographic = region.",
      "trap": null,
      "items": [
        {
          "label": "DATASET",
          "hot": true
        },
        {
          "label": "SHARD 1"
        },
        {
          "label": "SHARD 2"
        },
        {
          "label": "SHARD 3"
        }
      ]
    },
    {
      "title": "MONGODB DATA MODEL",
      "body": "MongoDB stores BSON documents in collections. Documents can contain nested documents and arrays. Mapping: relational database → database; table → collection; row → document; column → field; primary key → _id.",
      "purpose": "Think “document close to application object”.",
      "diagram": "mongo",
      "memory": "Table → collection. Row → document. Column → field.",
      "trap": null
    },
    {
      "title": "MONGODB CRUD",
      "body": "Create: insertOne/insertMany. Read: find/findOne. Update: updateOne/updateMany with operators such as $set and $inc. Delete: deleteOne/deleteMany. Common operators include comparison ($gt, $gte, $lt, $lte, $eq, $ne), membership ($in, $nin), logical ($and, $or, $not, $nor) and update operators ($set, $unset, $inc, $push, $pull).",
      "purpose": "Know the verb → method pairing.",
      "diagram": "flow",
      "memory": "CRUD = insert, find, update, delete.",
      "trap": null,
      "items": [
        {
          "label": "CREATE",
          "hot": true
        },
        {
          "label": "READ"
        },
        {
          "label": "UPDATE"
        },
        {
          "label": "DELETE"
        }
      ]
    },
    {
      "title": "MONGODB AGGREGATION PIPELINE",
      "body": "The pipeline transforms documents through stages. Typical flow: $match → $group → $project → $sort → $limit. Other stages include $skip, $unwind and $lookup.",
      "purpose": "Explain what each stage does.",
      "diagram": "mongo",
      "memory": "$match filters; $group aggregates; $project shapes; $sort orders; $limit restricts.",
      "trap": null
    },
    {
      "title": "EXAM ATTACK: CAP + MONGO",
      "body": "Define CAP precisely → C/A/P → ACID vs BASE → sharding strategies → MongoDB model + mapping → CRUD → aggregation pipeline → use cases/conclusion.",
      "purpose": "This combines two high-yield clusters.",
      "diagram": "cap",
      "memory": null,
      "trap": null
    }
  ],
  "quiz": [
    {
      "q": "CAP trade-off is specifically about…",
      "opts": [
        "Normal operation only",
        "A network partition",
        "Primary keys",
        "SQL joins"
      ],
      "a": 1,
      "why": "CAP concerns the trade-off during network partition.",
      "whyWrong": "Partition is the condition that triggers the theorem’s trade-off."
    },
    {
      "q": "In MongoDB, a table maps most closely to…",
      "opts": [
        "Document",
        "Field",
        "Collection",
        "_id"
      ],
      "a": 2,
      "why": "Table → collection.",
      "whyWrong": "Document maps to row."
    }
  ]
};