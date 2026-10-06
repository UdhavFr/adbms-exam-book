# 2. Data Models, Schemas and Instances

Source: ADBMS_MasterNotes.docx — folder `u1ch02`

### 2. Data Models, Schemas and Instances
_(p. 3)_
A data model is a collection of concepts used to describe the structure of data, relationships among data items, constraints, and sometimes operations. It provides a vocabulary for designing and communicating a database.
#### Types of data models
_(p. 3)_
- Hierarchical model: organizes records in a tree-like parent-child structure.
- Network model: represents records connected through network-like relationships.
- Relational model: represents data as relations/tables.
- Entity–Relationship model: conceptual model based on entities, attributes and relationships.
- Object-oriented model: represents objects, classes, inheritance and methods.
- Document model: stores semi-structured documents such as JSON/BSON.
- Key-value model: stores data as key-value pairs.
- Column-family model: organizes distributed data into rows and column families.
- Graph model: represents nodes, edges and properties.
#### Schema
_(p. 3)_
A schema is the overall logical description or blueprint of the database. It specifies relations, attributes, data types, keys, relationships, constraints, indexes, views and other database objects. The schema is relatively stable compared with the actual data.
#### Instance
_(p. 3)_
An instance is the collection of actual data stored in the database at a particular point in time. Insertions, updates, and deletions change the instance without necessarily changing the schema.

| Aspect | Schema | Instance |
|---|---|---|
| Meaning | Database design/structure | Actual database contents |
| Change frequency | Relatively infrequent | Changes frequently |
| Example | STUDENT(RollNo, Name, Course) | (101, Ravi, MCA) |
| Analogy | Blueprint | Current building |

EXAM-READY POINT: Always remember: schema describes the structure; instance describes the state of the data at a particular moment.
