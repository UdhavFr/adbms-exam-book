# 6. Overview of Relational Model

Source: ADBMS_MasterNotes.docx — folder `u1ch06`

### 6. Overview of Relational Model
_(p. 6)_
The relational model represents data as relations. A relation is usually visualized as a table containing tuples (rows) and attributes (columns). Each attribute has a domain defining permissible values.
#### Important terms
_(p. 6)_
- Relation = table
- Tuple = row
- Attribute = column
- Domain = permitted set/type of values
- Degree = number of attributes
- Cardinality = number of tuples
- Primary key = unique identifier
- Foreign key = reference to another relation
A relational database is governed by integrity rules so that invalid data cannot be introduced. The relational model also provides operations such as selection, projection, union, intersection, difference, Cartesian product, and join through relational algebra, while SQL provides a practical declarative language.
#### Relational algebra operations
_(p. 7)_

| Operation | Purpose |
|---|---|
| Selection σ | Selects rows satisfying a condition. |
| Projection π | Selects required columns. |
| Union ∪ | Combines compatible relations. |
| Difference − | Returns tuples in one relation but not the other. |
| Cartesian product × | Combines every tuple of one relation with every tuple of another. |
| Join ⋈ | Combines related tuples using a condition. |

