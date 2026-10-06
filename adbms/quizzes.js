window.MCQS = [
 {
  "id": "Q89",
  "topic": "mixed",
  "unit": "mixed",
  "pri": "P1",
  "text": "Which step comes first in a 20-mark answer?",
  "opts": [
   "Diagram",
   "Definition and intro",
   "Conclusion",
   "Example"
  ],
  "ans": 1,
  "why": "Start with a 5-7 line definition and why it matters.",
  "whyNot": null,
  "hint": "Recall the mixed notes (priority P1) — answer from memory first."
 },
 {
  "id": "Q90",
  "topic": "mixed",
  "unit": "mixed",
  "pri": "P1",
  "text": "A topic has a process or architecture. What should you add?",
  "opts": [
   "Nothing, text is enough",
   "A labelled diagram or flow",
   "Only a table",
   "A longer conclusion"
  ],
  "ans": 1,
  "why": "Diagrams are explicitly rewarded for processes, hierarchies and algorithms.",
  "whyNot": null,
  "hint": "Recall the mixed notes (priority P1) — answer from memory first."
 },
 {
  "id": "Q91",
  "topic": "U2-4",
  "unit": "U2",
  "pri": "P0",
  "text": "R(A,B,C), key is AB, and B→C. Which normal form is violated first?",
  "opts": [
   "1NF",
   "2NF",
   "3NF",
   "BCNF"
  ],
  "ans": 1,
  "why": "C depends on only part of the key (B), which is a partial dependency, so 2NF fails.",
  "whyNot": null,
  "hint": "Recall the U2-4 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q92",
  "topic": "U2-5",
  "unit": "U2",
  "pri": "P0",
  "text": "Student(ID, Dept, DeptHead) with ID→Dept and Dept→DeptHead. What is the problem?",
  "opts": [
   "Partial dependency",
   "Transitive dependency",
   "Not atomic",
   "Lossy join"
  ],
  "ans": 1,
  "why": "ID→Dept→DeptHead is transitive, so 3NF fails.",
  "whyNot": null,
  "hint": "Recall the U2-5 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q93",
  "topic": "U2-6",
  "unit": "U2",
  "pri": "P0",
  "text": "Which statement is true?",
  "opts": [
   "Every 3NF relation is in BCNF",
   "Every BCNF relation is in 3NF",
   "BCNF is weaker than 2NF",
   "1NF allows repeating groups"
  ],
  "ans": 1,
  "why": "BCNF is stricter than 3NF, so BCNF implies 3NF but not the reverse.",
  "whyNot": null,
  "hint": "Recall the U2-6 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q94",
  "topic": "U2-1",
  "unit": "U2",
  "pri": "P0",
  "text": "R(A,B,C,D) with A→B and B→C. What is A+?",
  "opts": [
   "{A}",
   "{A,B}",
   "{A,B,C}",
   "{A,B,C,D}"
  ],
  "ans": 2,
  "why": "A gives B, B gives C, and nothing gives D, so A+ is {A,B,C}.",
  "whyNot": null,
  "hint": "Recall the U2-1 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q95",
  "topic": "U2-9",
  "unit": "U2",
  "pri": "P1",
  "text": "When is a binary decomposition R1, R2 lossless?",
  "opts": [
   "Common attribute set is a key of R1 or R2",
   "R1 and R2 share no attributes",
   "Both are in 1NF",
   "It has fewer tables"
  ],
  "ans": 0,
  "why": "Intersection must be a super key of at least one part.",
  "whyNot": null,
  "hint": "Recall the U2-9 notes (priority P1) — answer from memory first."
 },
 {
  "id": "Q96",
  "topic": "U2-9",
  "unit": "U2",
  "pri": "P1",
  "text": "Which normal form decomposition always preserves dependencies AND is lossless?",
  "opts": [
   "BCNF",
   "3NF",
   "2NF",
   "4NF"
  ],
  "ans": 1,
  "why": "3NF synthesis guarantees both; BCNF may lose dependencies.",
  "whyNot": null,
  "hint": "Recall the U2-9 notes (priority P1) — answer from memory first."
 },
 {
  "id": "Q97",
  "topic": "U3-3",
  "unit": "U3",
  "pri": "P0",
  "text": "Power cut right after COMMIT, but the data is still there after restart. Which property?",
  "opts": [
   "Atomicity",
   "Consistency",
   "Isolation",
   "Durability"
  ],
  "ans": 3,
  "why": "Committed changes surviving failure is durability.",
  "whyNot": null,
  "hint": "Recall the U3-3 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q98",
  "topic": "U3-3",
  "unit": "U3",
  "pri": "P0",
  "text": "Debit succeeded, credit failed, so the debit is undone. Which property?",
  "opts": [
   "Atomicity",
   "Isolation",
   "Durability",
   "Consistency"
  ],
  "ans": 0,
  "why": "All-or-nothing is atomicity.",
  "whyNot": null,
  "hint": "Recall the U3-3 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q99",
  "topic": "U3-3",
  "unit": "U3",
  "pri": "P0",
  "text": "Which component mainly ensures Isolation?",
  "opts": [
   "Recovery manager",
   "Concurrency control",
   "Buffer manager",
   "Query optimizer"
  ],
  "ans": 1,
  "why": "Locking or timestamps give isolation.",
  "whyNot": null,
  "hint": "Recall the U3-3 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q100",
  "topic": "U3-5",
  "unit": "U3",
  "pri": "P0",
  "text": "A precedence graph contains a cycle. The schedule is...",
  "opts": [
   "Conflict serializable",
   "Not conflict serializable",
   "Always recoverable",
   "Serial"
  ],
  "ans": 1,
  "why": "A cycle means no equivalent serial order exists.",
  "whyNot": null,
  "hint": "Recall the U3-5 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q101",
  "topic": "U3-6",
  "unit": "U3",
  "pri": "P0",
  "text": "In 2PL, what is forbidden after the first unlock?",
  "opts": [
   "Reading",
   "Acquiring new locks",
   "Committing",
   "Unlocking"
  ],
  "ans": 1,
  "why": "Once shrinking starts, no new locks.",
  "whyNot": null,
  "hint": "Recall the U3-6 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q102",
  "topic": "U3-6",
  "unit": "U3",
  "pri": "P1",
  "text": "Deadlock is detected using...",
  "opts": [
   "Precedence graph",
   "Wait-for graph",
   "B+ tree",
   "Shadow table"
  ],
  "ans": 1,
  "why": "A cycle in the wait-for graph means deadlock.",
  "whyNot": null,
  "hint": "Recall the U3-6 notes (priority P1) — answer from memory first."
 },
 {
  "id": "Q103",
  "topic": "U4-7",
  "unit": "U4",
  "pri": "P0",
  "text": "During a partition, a system keeps answering with possibly stale data. It chose...",
  "opts": [
   "CP",
   "AP",
   "CA",
   "ACID"
  ],
  "ans": 1,
  "why": "Availability over consistency is AP.",
  "whyNot": null,
  "hint": "Recall the U4-7 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q104",
  "topic": "U4-8",
  "unit": "U4",
  "pri": "P0",
  "text": "What does the S in BASE stand for?",
  "opts": [
   "Strong",
   "Soft state",
   "Serializable",
   "Sharded"
  ],
  "ans": 1,
  "why": "Soft state: data may change without input as replicas converge.",
  "whyNot": null,
  "hint": "Recall the U4-8 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q105",
  "topic": "U4-9",
  "unit": "U4",
  "pri": "P1",
  "text": "Hash sharding mainly helps with...",
  "opts": [
   "Range queries",
   "Even data distribution",
   "Joins",
   "Foreign keys"
  ],
  "ans": 1,
  "why": "Hashing spreads keys evenly, but range queries get harder.",
  "whyNot": null,
  "hint": "Recall the U4-9 notes (priority P1) — answer from memory first."
 },
 {
  "id": "Q106",
  "topic": "U4-2",
  "unit": "U4",
  "pri": "P0",
  "text": "How is a vertically fragmented table rebuilt?",
  "opts": [
   "UNION",
   "JOIN on the key",
   "Intersection",
   "Cartesian product"
  ],
  "ans": 1,
  "why": "Each fragment keeps the key so a join reconstructs the table.",
  "whyNot": null,
  "hint": "Recall the U4-2 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q107",
  "topic": "U4-4",
  "unit": "U4",
  "pri": "P0",
  "text": "In 2PC, one participant votes NO. Result?",
  "opts": [
   "Commit",
   "Global abort",
   "Ignore it",
   "Retry later only for that site"
  ],
  "ans": 1,
  "why": "Any NO vote forces a global abort.",
  "whyNot": null,
  "hint": "Recall the U4-4 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q108",
  "topic": "U4-4",
  "unit": "U4",
  "pri": "P1",
  "text": "Main drawback of 2PC?",
  "opts": [
   "No atomicity",
   "Blocking if coordinator fails",
   "Too many tables",
   "No logging"
  ],
  "ans": 1,
  "why": "Participants can be stuck waiting for the coordinator decision.",
  "whyNot": null,
  "hint": "Recall the U4-4 notes (priority P1) — answer from memory first."
 },
 {
  "id": "Q109",
  "topic": "U2-13",
  "unit": "U2",
  "pri": "P0",
  "text": "Query: salary BETWEEN 30000 AND 50000. Best index?",
  "opts": [
   "Hash",
   "B+ tree",
   "No index",
   "Bitmap on name"
  ],
  "ans": 1,
  "why": "Linked sorted leaves make ranges fast.",
  "whyNot": null,
  "hint": "Recall the U2-13 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q110",
  "topic": "U2-13",
  "unit": "U2",
  "pri": "P0",
  "text": "Main downside of indexes?",
  "opts": [
   "Slower reads",
   "Extra storage and write overhead",
   "Data loss",
   "No ordering"
  ],
  "ans": 1,
  "why": "Every write must also update the index.",
  "whyNot": null,
  "hint": "Recall the U2-13 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q111",
  "topic": "U3-9",
  "unit": "U3",
  "pri": "P0",
  "text": "Which recovery scheme never needs UNDO?",
  "opts": [
   "Deferred update",
   "Immediate update",
   "Both",
   "Neither"
  ],
  "ans": 0,
  "why": "Nothing uncommitted ever reaches the database.",
  "whyNot": null,
  "hint": "Recall the U3-9 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q112",
  "topic": "U3-12",
  "unit": "U3",
  "pri": "P0",
  "text": "WAL means...",
  "opts": [
   "Data page first, log later",
   "Log first, then data page",
   "Lock then write",
   "Write all later"
  ],
  "ans": 1,
  "why": "Log before data is what makes undo and redo possible.",
  "whyNot": null,
  "hint": "Recall the U3-12 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q113",
  "topic": "U5-4",
  "unit": "U5",
  "pri": "P1",
  "text": "Best store for friend-of-friend recommendations?",
  "opts": [
   "Redis",
   "Neo4j",
   "Cassandra",
   "MongoDB"
  ],
  "ans": 1,
  "why": "Relationship traversal is the graph database sweet spot.",
  "whyNot": null,
  "hint": "Recall the U5-4 notes (priority P1) — answer from memory first."
 },
 {
  "id": "Q114",
  "topic": "U4-11",
  "unit": "U4",
  "pri": "P0",
  "text": "Which command finds docs with age over 20 in MongoDB?",
  "opts": [
   "SELECT age>20",
   "db.users.find({age:{$gt:20}})",
   "GET age",
   "MATCH (age)"
  ],
  "ans": 1,
  "why": "$gt is the MongoDB greater-than operator.",
  "whyNot": null,
  "hint": "Recall the U4-11 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q115",
  "topic": "U4-12",
  "unit": "U4",
  "pri": "P0",
  "text": "Which stage should usually come first to cut data early?",
  "opts": [
   "$sort",
   "$match",
   "$group",
   "$limit after group"
  ],
  "ans": 1,
  "why": "Filtering first shrinks the data every later stage touches.",
  "whyNot": null,
  "hint": "Recall the U4-12 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q116",
  "topic": "U5-7",
  "unit": "U5",
  "pri": "P0",
  "text": "Which measure compares the angle between two vectors?",
  "opts": [
   "Hamming",
   "Cosine similarity",
   "Manhattan time",
   "Jaccard rows"
  ],
  "ans": 1,
  "why": "Cosine similarity is based on the angle.",
  "whyNot": null,
  "hint": "Recall the U5-7 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q117",
  "topic": "U5-6",
  "unit": "U5",
  "pri": "P0",
  "text": "HNSW is mainly used for...",
  "opts": [
   "Exact joins",
   "Approximate nearest neighbour search",
   "Locking",
   "Sharding"
  ],
  "ans": 1,
  "why": "It is a graph index for fast approximate similarity search.",
  "whyNot": null,
  "hint": "Recall the U5-6 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q118",
  "topic": "U1-5",
  "unit": "U1",
  "pri": "P0",
  "text": "How is an M:N relationship mapped?",
  "opts": [
   "FK on either side",
   "Separate junction table",
   "Merge the entities",
   "Ignore it"
  ],
  "ans": 1,
  "why": "A new table holds the keys of both entities.",
  "whyNot": null,
  "hint": "Recall the U1-5 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q119",
  "topic": "U1-7",
  "unit": "U1",
  "pri": "P0",
  "text": "GRANT and REVOKE belong to...",
  "opts": [
   "DDL",
   "DML",
   "DCL",
   "TCL"
  ],
  "ans": 2,
  "why": "They control access, so Data Control Language.",
  "whyNot": null,
  "hint": "Recall the U1-7 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q120",
  "topic": "U1-8",
  "unit": "U1",
  "pri": "P0",
  "text": "Entity integrity means...",
  "opts": [
   "FK must match",
   "Primary key cannot be null",
   "Values are unique across tables",
   "Every table has an index"
  ],
  "ans": 1,
  "why": "No primary key attribute may be null.",
  "whyNot": null,
  "hint": "Recall the U1-8 notes (priority P0) — answer from memory first."
 },
 {
  "id": "Q121",
  "topic": "U1-3",
  "unit": "U1",
  "pri": "P0",
  "text": "Which level hides physical storage details from end users?",
  "opts": [
   "External",
   "Conceptual",
   "Internal",
   "Storage device"
  ],
  "ans": 0,
  "why": "External level provides customized user views.",
  "whyNot": "Internal level is where physical representation is described.",
  "hint": "Not this: Internal level is where physical representation is described."
 },
 {
  "id": "Q122",
  "topic": "U1-2",
  "unit": "U1",
  "pri": "P1",
  "text": "Schema means…",
  "opts": [
   "Current data values",
   "Database blueprint/structure",
   "Only indexes",
   "Only user views"
  ],
  "ans": 1,
  "why": "Schema is the relatively stable logical design.",
  "whyNot": "Current values are the instance.",
  "hint": "Not this: Current values are the instance."
 },
 {
  "id": "Q123",
  "topic": "U1-5",
  "unit": "U1",
  "pri": "P0",
  "text": "For a 1:N relationship, where does the 1-side primary key usually go?",
  "opts": [
   "Into the 1-side as a duplicate",
   "As a foreign key in the N-side relation",
   "Into a brand-new relation always",
   "It is discarded"
  ],
  "ans": 1,
  "why": "The 1-side key becomes a foreign key in the N-side.",
  "whyNot": "A new table is specifically typical for M:N, not ordinary 1:N.",
  "hint": "Not this: A new table is specifically typical for M:N, not ordinary 1:N."
 },
 {
  "id": "Q124",
  "topic": "U1-5",
  "unit": "U1",
  "pri": "P1",
  "text": "A multivalued attribute is usually mapped by…",
  "opts": [
   "Repeating columns",
   "One big text field",
   "A separate relation with owner key + value",
   "Deleting the attribute"
  ],
  "ans": 2,
  "why": "That keeps values addressable and relationally structured.",
  "whyNot": "Repeating columns destroy the clean relational design.",
  "hint": "Not this: Repeating columns destroy the clean relational design."
 },
 {
  "id": "Q125",
  "topic": "U1-7",
  "unit": "U1",
  "pri": "P0",
  "text": "Which clause filters groups after GROUP BY?",
  "opts": [
   "WHERE",
   "HAVING",
   "ORDER BY",
   "LIMIT"
  ],
  "ans": 1,
  "why": "HAVING filters groups.",
  "whyNot": "WHERE filters rows before grouping.",
  "hint": "Not this: WHERE filters rows before grouping."
 },
 {
  "id": "Q126",
  "topic": "U1-8",
  "unit": "U1",
  "pri": "P0",
  "text": "Entity integrity requires primary-key values to be…",
  "opts": [
   "Nullable and duplicated",
   "Unique and non-NULL",
   "Sorted",
   "Encrypted"
  ],
  "ans": 1,
  "why": "A primary key identifies tuples and cannot be NULL.",
  "whyNot": "Sorting/encryption are unrelated to entity integrity.",
  "hint": "Not this: Sorting/encryption are unrelated to entity integrity."
 },
 {
  "id": "Q127",
  "topic": "U2-4",
  "unit": "U2",
  "pri": "P0",
  "text": "What does 2NF mainly remove?",
  "opts": [
   "Non-atomic values",
   "Partial dependencies",
   "Transitive dependencies",
   "Join dependencies"
  ],
  "ans": 1,
  "why": "2NF attacks partial dependency on part of a composite key.",
  "whyNot": "3NF is the transitive-dependency stage.",
  "hint": "Not this: 3NF is the transitive-dependency stage."
 },
 {
  "id": "Q128",
  "topic": "U2-6",
  "unit": "U2",
  "pri": "P0",
  "text": "BCNF requires…",
  "opts": [
   "Every determinant is a super key",
   "Every table has two keys",
   "All attributes are atomic",
   "No foreign keys"
  ],
  "ans": 0,
  "why": "That is the memorization sentence from the notes.",
  "whyNot": "Atomicity is 1NF, not BCNF.",
  "hint": "Not this: Atomicity is 1NF, not BCNF."
 },
 {
  "id": "Q129",
  "topic": "U2-13",
  "unit": "U2",
  "pri": "P0",
  "text": "Which index is naturally suited to a range query?",
  "opts": [
   "Hash index",
   "B+ tree",
   "No index ever",
   "Only a graph index"
  ],
  "ans": 1,
  "why": "B+ trees maintain order and linked leaves.",
  "whyNot": "Hash buckets are not naturally ordered.",
  "hint": "Not this: Hash buckets are not naturally ordered."
 },
 {
  "id": "Q130",
  "topic": "U2-14",
  "unit": "U2",
  "pri": "P1",
  "text": "A hash collision occurs when…",
  "opts": [
   "A key is missing",
   "Two keys map to the same bucket",
   "The tree becomes unbalanced",
   "A page is empty"
  ],
  "ans": 1,
  "why": "Two different keys can map to the same bucket.",
  "whyNot": "Unbalanced trees are not the hash collision concept.",
  "hint": "Not this: Unbalanced trees are not the hash collision concept."
 },
 {
  "id": "Q131",
  "topic": "U3-3",
  "unit": "U3",
  "pri": "P0",
  "text": "Which ACID property says a transaction is all-or-nothing?",
  "opts": [
   "Consistency",
   "Atomicity",
   "Isolation",
   "Durability"
  ],
  "ans": 1,
  "why": "Atomicity is the all-or-nothing property.",
  "whyNot": "Consistency is about valid state and constraints.",
  "hint": "Not this: Consistency is about valid state and constraints."
 },
 {
  "id": "Q132",
  "topic": "U3-6",
  "unit": "U3",
  "pri": "P0",
  "text": "Which 2PL phase forbids acquiring new locks?",
  "opts": [
   "Growing",
   "Shrinking",
   "Lock point",
   "Commit"
  ],
  "ans": 1,
  "why": "Shrinking phase releases locks and acquires no new locks.",
  "whyNot": "Growing phase is the acquisition phase.",
  "hint": "Not this: Growing phase is the acquisition phase."
 },
 {
  "id": "Q133",
  "topic": "U3-12",
  "unit": "U3",
  "pri": "P0",
  "text": "WAL requires…",
  "opts": [
   "Data page first, log later",
   "Log record first, then changed data page",
   "No log",
   "Only checkpoints"
  ],
  "ans": 1,
  "why": "Write-Ahead Logging writes the log to stable storage before the corresponding changed page.",
  "whyNot": "That is the core WAL guarantee.",
  "hint": "Not this: That is the core WAL guarantee."
 },
 {
  "id": "Q134",
  "topic": "U4-2",
  "unit": "U4",
  "pri": "P0",
  "text": "Vertical fragmentation divides…",
  "opts": [
   "Rows",
   "Columns",
   "Databases",
   "Transactions"
  ],
  "ans": 1,
  "why": "Vertical = columns, usually keeping the key for reconstruction.",
  "whyNot": "Horizontal fragmentation divides rows.",
  "hint": "Not this: Horizontal fragmentation divides rows."
 },
 {
  "id": "Q135",
  "topic": "U4-4",
  "unit": "U4",
  "pri": "P0",
  "text": "In 2PC, who sends PREPARE?",
  "opts": [
   "Each participant to coordinator",
   "Coordinator to participants",
   "The database user",
   "The storage manager"
  ],
  "ans": 1,
  "why": "Coordinator starts the prepare round.",
  "whyNot": "Participants answer the prepare request with votes.",
  "hint": "Not this: Participants answer the prepare request with votes."
 },
 {
  "id": "Q136",
  "topic": "U4-7",
  "unit": "U4",
  "pri": "P0",
  "text": "CAP trade-off is specifically about…",
  "opts": [
   "Normal operation only",
   "A network partition",
   "Primary keys",
   "SQL joins"
  ],
  "ans": 1,
  "why": "CAP concerns the trade-off during network partition.",
  "whyNot": "Partition is the condition that triggers the theorem’s trade-off.",
  "hint": "Not this: Partition is the condition that triggers the theorem’s trade-off."
 },
 {
  "id": "Q137",
  "topic": "U4-10",
  "unit": "U4",
  "pri": "P1",
  "text": "In MongoDB, a table maps most closely to…",
  "opts": [
   "Document",
   "Field",
   "Collection",
   "_id"
  ],
  "ans": 2,
  "why": "Table → collection.",
  "whyNot": "Document maps to row.",
  "hint": "Not this: Document maps to row."
 },
 {
  "id": "Q138",
  "topic": "U5-1",
  "unit": "U5",
  "pri": "P0",
  "text": "In Cassandra, the partition key primarily determines…",
  "opts": [
   "The graph traversal",
   "Where the data/partition lives",
   "The JSON field name",
   "The vector embedding"
  ],
  "ans": 1,
  "why": "Partition key chooses the partition/location.",
  "whyNot": "Clustering columns govern order within a partition.",
  "hint": "Not this: Clustering columns govern order within a partition."
 },
 {
  "id": "Q139",
  "topic": "U5-6",
  "unit": "U5",
  "pri": "P0",
  "text": "HNSW is best described as…",
  "opts": [
   "A graph-based ANN technique",
   "A SQL isolation level",
   "A hash collision strategy",
   "A MongoDB CRUD command"
  ],
  "ans": 0,
  "why": "HNSW is a graph-based approximate nearest-neighbor technique.",
  "whyNot": "The other options belong to unrelated topics.",
  "hint": "Not this: The other options belong to unrelated topics."
 },
 {
  "id": "Q140",
  "topic": "mixed",
  "unit": "mixed",
  "pri": "P1",
  "text": "Which sentence is the safest opening for a 20-mark answer?",
  "opts": [
   "Jump straight to an example",
   "Define the concept and explain why it matters",
   "List 20 keywords only",
   "Start with the conclusion"
  ],
  "ans": 1,
  "why": "The notebook explicitly recommends a 5–7 line definition + importance introduction.",
  "whyNot": "A list alone does not show WHAT, WHY, HOW and WHERE.",
  "hint": "Not this: A list alone does not show WHAT, WHY, HOW and WHERE."
 },
 {
  "id": "Q141",
  "topic": "mixed",
  "unit": "mixed",
  "pri": "P1",
  "text": "What should a strong 20-mark answer contain besides definitions?",
  "opts": [
   "Only code",
   "Diagram/flow, components, example, trade-offs and conclusion",
   "Only a comparison table",
   "Only advantages"
  ],
  "ans": 1,
  "why": "That structure is the notebook’s exam-writing guidance.",
  "whyNot": "Definitions alone are insufficient.",
  "hint": "Not this: Definitions alone are insufficient."
 },
 {
  "id": "Q142",
  "topic": "mixed",
  "unit": "mixed",
  "pri": "P0",
  "text": "Which pair is correctly matched?",
  "opts": [
   "4NF → join dependency",
   "5NF → multivalued dependency",
   "2NF → partial dependency",
   "BCNF → atomic values"
  ],
  "ans": 2,
  "why": "2NF removes partial dependency.",
  "whyNot": "4NF is MVD; 5NF is JD; 1NF is atomicity; BCNF is determinant super key.",
  "hint": "Not this: 4NF is MVD; 5NF is JD; 1NF is atomicity; BCNF is determinant super key."
 }
];
window.MCQ_BY_ID = {};
window.MCQS.forEach(q => window.MCQ_BY_ID[q.id] = q);
