# 12. Neo4j Indexing and Ordering

Source: ADBMS_MasterNotes.docx — folder `u5ch12`

### 12. Neo4j Indexing and Ordering
_(p. 31)_
Neo4j indexes properties so that starting nodes can be located efficiently. For example, an index on Person(name) helps find the starting node for a query involving a person's name before graph traversal begins.
Ordering can be expressed in Cypher using ORDER BY: MATCH (p:Person) RETURN p.name, p.age ORDER BY p.age DESC.
Graph indexes are especially valuable when the initial lookup is selective. Once a starting node is found, graph traversal follows relationships rather than scanning unrelated records.
