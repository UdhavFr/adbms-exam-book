const CHAPTER={
  "number": 5,
  "unit": "Unit 2 · Normalization & Storage",
  "title": "5. Storage, B+ Trees & Hash Indexing",
  "beats": [
    {
      "title": "WHY PAGES EXIST",
      "body": "Database I/O is expensive, so data moves between secondary storage and memory in pages/blocks rather than one record at a time. The buffer manager brings pages into memory and writes modified pages back.",
      "purpose": "The optimization target is often fewer page I/Os.",
      "diagram": "flow",
      "memory": "Disk → pages → buffer pool → CPU.",
      "trap": null,
      "items": [
        {
          "label": "DISK PAGES",
          "hot": true
        },
        {
          "label": "BUFFER POOL"
        },
        {
          "label": "CPU / DBMS"
        }
      ]
    },
    {
      "title": "FILE ORGANIZATIONS",
      "body": "Heap: unordered, simple insertion, good for frequent inserts/scans. Sequential/sorted: key order, good for ordered/range access. Hash: bucket by hash function, good for equality. Clustered: related records placed close together.",
      "purpose": "Use “best suited for” wording in the exam.",
      "diagram": "flow",
      "memory": null,
      "trap": null,
      "items": [
        {
          "label": "HEAP"
        },
        {
          "label": "SORTED"
        },
        {
          "label": "HASH",
          "hot": true
        },
        {
          "label": "CLUSTERED"
        }
      ]
    },
    {
      "title": "B+ TREE: WHAT LIVES WHERE?",
      "body": "Internal nodes hold separator keys and child pointers. Leaf nodes hold search keys and record/data-page references. Leaves are linked, making range scans efficient.",
      "purpose": "The leaf linkage is a key differentiator.",
      "diagram": "btree",
      "memory": "B+ tree: balanced + high fan-out + linked leaves.",
      "trap": null
    },
    {
      "title": "B+ TREE SEARCH",
      "body": "Start at root → compare with separator keys → follow child pointer → repeat → reach leaf → follow record/data pointer.",
      "purpose": "Describe the journey, not only the definition.",
      "diagram": "flow",
      "memory": null,
      "trap": null,
      "items": [
        {
          "label": "ROOT",
          "hot": true
        },
        {
          "label": "CHILD"
        },
        {
          "label": "LEAF"
        },
        {
          "label": "RECORD"
        }
      ]
    },
    {
      "title": "HASH INDEX",
      "body": "Hash function maps a key to a bucket. Best for equality lookups such as StudentID = 101. Collisions require overflow buckets, chaining or dynamic hashing techniques.",
      "purpose": "The exam comparison is equality vs range.",
      "diagram": "flow",
      "memory": "Hash = equality. B+ tree = equality + range.",
      "trap": null,
      "items": [
        {
          "label": "KEY 101",
          "hot": true
        },
        {
          "label": "hash(101)"
        },
        {
          "label": "BUCKET"
        },
        {
          "label": "RECORD"
        }
      ]
    },
    {
      "title": "B+ TREE vs HASH",
      "body": "B+ tree is ordered, balanced and strong for equality + range + sorted traversal. Hash is bucket-based, unordered and strong for equality but poor for range traversal.",
      "purpose": "A 2-column comparison is a mark magnet.",
      "diagram": "flow",
      "memory": null,
      "trap": null,
      "items": [
        {
          "label": "B+ TREE",
          "hot": true
        },
        {
          "label": "VS"
        },
        {
          "label": "HASH"
        }
      ]
    },
    {
      "title": "EXAM ATTACK: INDEXING",
      "body": "Define index → explain pages/I/O → B+ tree structure + search + range → hash + collision → comparison → conclusion about query-driven indexing.",
      "purpose": "That is the full 20-mark route.",
      "diagram": "index",
      "memory": null,
      "trap": null
    }
  ],
  "quiz": [
    {
      "q": "Which index is naturally suited to a range query?",
      "opts": [
        "Hash index",
        "B+ tree",
        "No index ever",
        "Only a graph index"
      ],
      "a": 1,
      "why": "B+ trees maintain order and linked leaves.",
      "whyWrong": "Hash buckets are not naturally ordered."
    },
    {
      "q": "A hash collision occurs when…",
      "opts": [
        "A key is missing",
        "Two keys map to the same bucket",
        "The tree becomes unbalanced",
        "A page is empty"
      ],
      "a": 1,
      "why": "Two different keys can map to the same bucket.",
      "whyWrong": "Unbalanced trees are not the hash collision concept."
    }
  ]
};