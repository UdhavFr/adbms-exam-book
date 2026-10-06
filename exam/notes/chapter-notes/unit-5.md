# UNIT 5 — NoSQL Stores, Indexing and Ordering Data Sets
Source: `ADBMS_MasterNotes.docx` Unit 5, pp. 28–33 · structure `u5ch01`–`u5ch14`
Feeds the source's **Question 5** (indexing across relational *and* NoSQL) — the recommended answer must compare systems, not describe one.

---

## U5-1 Column-Oriented Databases: HBase and Cassandra — **P0** (p. 28)
- **WHAT:** wide-column/column-family stores organized around **row keys and column families**, built for very large datasets, horizontal scaling and high throughput; columns within families are sparse/flexible.
- **HBase:** distributed, tied to the **Hadoop ecosystem**; row key + column families; large-scale sparse data with random read/write at scale; accessed via APIs/shell.
- **Cassandra:** independent distributed wide-column DB for **high availability, horizontal scalability, high write throughput**; **partition key** distributes rows, **clustering columns** order rows within a partition; queried with **CQL**.
- **MISTAKE:** saying HBase is not Hadoop-related (it has a *strong* relationship) or that Cassandra's model is row-key+column-family (it is partition key + clustering columns).

## U5-2 Cassandra Basic Operations — **P1** (p. 29)
- **CQL:** CREATE KEYSPACE (with replication strategy/factor) · CREATE TABLE · INSERT · SELECT · UPDATE · DELETE — SQL-like syntax, different data model/query restrictions.
- **SCHEMA EVOLUTION:** explicit table schema; `ALTER TABLE` adds/modifies; changes must be **planned** because metadata is cluster-wide.
- **DESIGN PRINCIPLE:** model tables **according to query patterns**; deliberate **duplication** is normal so queries avoid expensive joins.
- **MISTAKE:** applying normalization thinking to Cassandra (opposite philosophy — comparison C39).

## U5-3 Redis — Key-Value Store — **P1** (p. 29)
- **WHAT:** **in-memory** key-value store with richer data structures; used for caching, sessions, counters, queues, leaderboards, fast temporary state.
- **COMMANDS:** SET/GET/DEL/EXISTS · HSET/HGET (hash) · EXPIRE (TTL) · INCR (atomic counter).
- **EXAMPLE:** `SET user:101 'Ravi'` → `GET user:101` ⇒ Ravi; `HSET user:101 name 'Ravi' course 'MCA'`.

## U5-4 Graph Databases and the Graph Data Model — **P1** (p. 30)
- **WHAT:** network representation — **nodes = entities, edges = relationships, properties = attributes**; best when queries depend on **traversing relationships**.
- **APPLICATIONS:** social networks, recommendation systems, fraud detection, knowledge graphs, network management, dependency analysis.
- **MISTAKE:** describing a graph DB as "tables with joins".

## U5-5 Neo4j and Cypher — **P1** (p. 30)
- **WHAT:** Neo4j = graph DB with nodes, relationships, labels, properties; **Cypher** = declarative graph language using ASCII-like patterns.
- **COMMAND ORDER:** CREATE → MATCH → WHERE → SET → DELETE (`DETACH DELETE` removes node + relationships).
- **PATTERN:** `MATCH (person:Person)-[:FRIEND_OF]->(friend:Person) RETURN …` — round brackets = **node**, square brackets = **relationship**.
- **STRENGTH:** natural multi-hop patterns — friends-of-friends, recommendations, shortest paths, dependency chains.
- **ORDERING:** `ORDER BY p.age DESC`.

## U5-6 Vector Databases and Embeddings — **P0** (p. 31)
- **WHAT:** an **embedding** converts text/image/audio/product into a numerical vector; the model places semantically similar objects near each other in vector space.
- **PIPELINE:** original data → embedding model → `[0.12, -0.31, 0.77, …]` → vector database → similarity/nearest-neighbour index.
- **CAVEAT (source):** vectors contain no human-readable meaning; usefulness depends on the embedding model and application.
- **MEASURES:** cosine similarity (angle/direction — semantic text retrieval) · Euclidean distance (straight-line) · dot product (alignment + magnitude — retrieval systems).

## U5-7 Similarity Search — **P0** (p. 31)
- **FLOW:** user query → embed query → query vector → vector index → nearest neighbours / **top-k** → metadata + original documents → results.
- **BRUTE FORCE:** compare with every stored vector — expensive as N grows.
- **ANN:** search a smaller promising region for much lower latency.
  - **HNSW** (Hierarchical Navigable Small World): graph-based; walks through increasingly close candidates; balances speed, memory, recall.
  - **IVF** (inverted-file): partitions vectors into clusters; searches only relevant groups.
- **MISTAKE:** writing HNSW = clusters / IVF = graph (swap them and you lose the mark).

## U5-8 Indexing and Ordering Data Sets — **P0** (p. 32)
- **WHAT:** an index is an **auxiliary access path** — `Query → INDEX → keys/pointers → records` instead of scanning 1…N.
- **COSTS:** storage + maintenance on writes + cache pressure; too many indexes slow write-heavy systems; an index that doesn't match the query shape is useless.
- **ORDERING:** ordered structures (B+ trees) support equality, range, prefix and sorted retrieval; **hash indexes are not ordered** ⇒ poor for range queries.
- **MISTAKE:** "more indexes = better performance" without stating write cost.

## U5-9 MongoDB Indexing and Ordering — **P0** (p. 32)
- **TYPES:** single-field, compound, multikey, text, geospatial, unique (and others by version/use case).
- **COMMANDS:** `createIndex({age:1})` · `createIndex({course:1, age:-1})` · `createIndex({email:1},{unique:true})` · `find().sort({age:1})`.
- **KEY RULE:** **compound-index field order matters** — it determines which query and sort patterns the index serves efficiently; inspect plans with `explain()`.

## U5-10 CouchDB Indexing and Ordering — **P2** (p. 32)
- **WHAT:** HTTP/REST-oriented document DB; **Mango indexes** for selector queries; **map/reduce views** produce indexed key/value structures where **key ordering** gives range-style access.
- **EXAM POINT (source):** indexes avoid repeatedly scanning all documents and make predictable query patterns efficient.

## U5-11 Cassandra Indexing and Ordering — **P0** (p. 33)
- **RULE:** **partition key decides the node/partition location**; **clustering columns define row order within a partition**.
- **EXAMPLE:** `PRIMARY KEY ((course), year, student_id)` ⇒ `course` partitions; inside a partition rows ordered by `year`, then `student_id`.
- **SECONDARY INDEXES:** supported, but **not a substitute for good partition design** — query-driven modelling is central.
- **MEMORY:** **Partition = Place · Clustering = Order.**

## U5-12 Neo4j Indexing and Ordering — **P1** (p. 33)
- **WHAT:** indexes on properties locate **starting nodes** quickly (e.g. `Person(name)`); traversal then follows relationships instead of scanning.
- **WHEN VALUABLE:** when the initial lookup is selective; ordering via `ORDER BY` in Cypher.

## U5-13 Vector Store Indexing — **P0** (p. 33)
- **vs TRADITIONAL:** exact/range-oriented on scalar keys (B+ tree/hash; `age = 22`, `BETWEEN`) vs similarity/nearest-neighbour on high-dimensional vectors (HNSW, IVF; top-k by distance).
- **WHY DIFFERENT:** a vector index organizes geometry/graph/cluster structure, not ordered keys.

## U5-14 Importance of Indexes for NoSQL Query Performance — **P1** (p. 33)
- **WHY:** millions/billions of records across machines ⇒ without an access path a query scans huge volumes (latency + CPU + memory + I/O + network).
- **BENEFITS:** fewer full scans · lower latency · selective filtering · sorting/range (ordered index) · efficient nearest-neighbour · less CPU/memory/disk/network work.
- **COSTS:** storage · write overhead · memory/cache pressure · ineffective if query doesn't match · too many indexes slow writes · distributed designs need partition awareness.
- **⚠ EXAM-READY ADVICE (source):** for a 20-mark indexing answer, **compare MongoDB, CouchDB, Cassandra, Neo4j and vector indexes** rather than explaining only one database.

---

### Unit 5 exam weighting
- **20-mark:** Question 5 (indexing) — coverage across all five systems + benefits/costs + conclusion "query-driven indexing".
- **10-mark:** Cassandra partition/clustering design · HBase vs Cassandra · vector embeddings + similarity search + ANN.
- **5-mark:** Redis commands · Cypher pattern · graph data model · CouchDB Mango vs views · traditional vs vector index.
- **2-mark:** definitions (embedding, HNSW, partition key, index…).
