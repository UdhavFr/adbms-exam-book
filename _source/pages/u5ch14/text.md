# 14. Importance of Indexes for NoSQL Query Performance

Source: ADBMS_MasterNotes.docx — folder `u5ch14`

### 14. Importance of Indexes for NoSQL Query Performance
_(p. 32)_
Indexes are important because NoSQL systems can contain millions or billions of records distributed across many machines. Without an appropriate access path, a query may scan large amounts of data, increasing latency and resource consumption.
#### Benefits
_(p. 32)_
- Reduce full collection/table scans.
- Lower query latency.
- Support selective filtering.
- Support sorting/range access where the index is ordered.
- Enable efficient nearest-neighbor retrieval in vector systems.
- Can reduce CPU, memory, disk I/O, and network work.
#### Costs and limitations
_(p. 32)_
- Additional storage.
- Write overhead because index entries must be maintained.
- Memory/cache pressure.
- An index may be ineffective if the query does not match its structure.
- Too many indexes can make write-heavy systems slower.
- Distributed databases may require careful partition-aware design.
EXAM-READY POINT: For a NoSQL indexing 20-mark answer, compare MongoDB, CouchDB, Cassandra, Neo4j, and vector indexes rather than explaining only one database.
