# 3. Levels of Data Abstraction

Source: ADBMS_MasterNotes.docx — folder `u1ch03`

### 3. Levels of Data Abstraction
_(p. 4)_
Database systems hide unnecessary implementation details from users through data abstraction. The classic three-level architecture separates user views, logical organization, and physical storage.
          EXTERNAL LEVEL / VIEW LEVEL
       ┌─────────┬─────────┬─────────┐
       │ Student │ Faculty │Accounts │
       │  View   │  View   │  View   │
       └────┬────┴────┬────┴────┬────┘
            └─────────┼─────────┘
                      ↓
              CONCEPTUAL LEVEL
        Complete logical database schema
        Entities + relationships + constraints
                      ↓
                INTERNAL LEVEL
       Files + pages + indexes + storage layout
                      ↓
                PHYSICAL STORAGE
#### External level
_(p. 4)_
The external level describes customized views for different users. A student may see courses and marks while an accounts employee sees fees and payments. Views improve simplicity and security.
#### Conceptual level
_(p. 4)_
The conceptual level represents the complete logical structure independent of physical storage. It describes entities, attributes, relationships, constraints, and the logical organization of data.
#### Internal level
_(p. 4)_
The internal level explains how data is physically represented, including files, pages, record placement, indexes, access paths, and storage structures.
#### Data independence
_(p. 4)_
Physical data independence is the ability to change physical storage structures without changing the conceptual schema. For example, replacing one index structure with another should not require rewriting application queries.
Logical data independence is the ability to modify the conceptual schema without requiring changes to every external view or application, as long as the required external information can still be provided.

| Type | Meaning | Example |
|---|---|---|
| Physical data independence | Physical storage can change without changing logical schema. | Add/change an index. |
| Logical data independence | Logical schema can evolve while preserving required external views. | Split a table while maintaining a compatible view. |

