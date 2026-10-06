# 9. MongoDB Indexing and Ordering

Source: ADBMS_MasterNotes.docx — folder `u5ch09`

### 9. MongoDB Indexing and Ordering
_(p. 30)_
MongoDB indexes allow queries to avoid scanning every document. Indexes may be single-field, compound, multikey, text, geospatial, unique, or other specialized types depending on the database version and use case.
Single-field: db.students.createIndex({age:1})
Compound: db.students.createIndex({course:1, age:-1})
Unique: db.users.createIndex({email:1}, {unique:true})
Sort: db.students.find().sort({age:1})
The order of fields in a compound index matters because it determines which query and sort patterns the index can support efficiently. Query plans can be inspected using explain().
