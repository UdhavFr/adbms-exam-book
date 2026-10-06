# 4. Graph Databases and Graph Data Model

Source: ADBMS_MasterNotes.docx — folder `u5ch04`

### 4. Graph Databases and Graph Data Model
_(p. 28)_
Graph databases represent data as a network. Nodes represent entities, relationships represent connections, and properties store attributes. Graph databases are especially suitable when queries depend on traversing relationships.
        (Alice)
          │
       FRIEND_OF
          ↓
         (Bob)
          │
       PURCHASED
          ↓
       (Product)

Nodes = entities
Edges = relationships
Properties = attributes
Example applications include social networks, recommendation systems, fraud detection, knowledge graphs, network management, and dependency analysis.
