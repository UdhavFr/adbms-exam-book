# 10. MongoDB Data Model

Source: ADBMS_MasterNotes.docx — folder `u4ch10`

### 10. MongoDB Data Model
_(p. 24)_
MongoDB is a document-oriented NoSQL database. It stores BSON documents in collections. Documents can contain nested documents and arrays, allowing a representation close to application objects.
MONGODB
Database
  └── Collection: students
        ├── Document {_id:1, name:'Ravi', age:22}
        ├── Document {_id:2, name:'Asha', age:23}
        └── Document {_id:3, name:'John', age:21}

| Relational concept | MongoDB concept |
|---|---|
| Database | Database |
| Table | Collection |
| Row | Document |
| Column | Field |
| Primary key | _id |

