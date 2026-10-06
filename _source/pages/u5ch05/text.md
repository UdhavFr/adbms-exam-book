# 5. Neo4j and Cypher

Source: ADBMS_MasterNotes.docx — folder `u5ch05`

### 5. Neo4j and Cypher
_(p. 29)_
Neo4j is a graph database that uses nodes, relationships, labels, and properties. Cypher is a declarative graph query language that represents graph patterns using ASCII-like syntax.
Create: CREATE (p:Person {name:'Alice', age:22});
Create relationship: MATCH (a:Person {name:'Alice'}), (b:Person {name:'Bob'}) CREATE (a)-[:FRIEND_OF]->(b);
Read: MATCH (p:Person)-[:FRIEND_OF]->(f:Person) RETURN p.name, f.name;
Filter: MATCH (p:Person) WHERE p.age > 20 RETURN p;
Update: MATCH (p:Person {name:'Alice'}) SET p.age=23 RETURN p;
Delete: MATCH (p:Person {name:'Alice'}) DETACH DELETE p;
#### Cypher pattern
_(p. 29)_
MATCH (person:Person)-[:FRIEND_OF]->(friend:Person)
      │                    │
    node                relationship
                              │
                         another node
             ↓
          RETURN person, friend
The strength of graph querying is its ability to express multi-hop patterns naturally, such as friends-of-friends, product recommendations, shortest paths, and dependency chains.
