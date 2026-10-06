# examples.md — The Canonical Examples (Bring These to the Exam)

One worked example per concept. Examiners give marks for **applying** a rule, not restating it.
All examples below are the source's own (or faithful restatements of them).

---

## E-1. Why DBMS (U1 §1)
Banking, railway/airline reservation, e-commerce, hospitals, universities, libraries, social networks, financial systems.
Relational examples: PostgreSQL, MySQL. NoSQL examples: MongoDB, Cassandra, Redis, Neo4j.

## E-2. Schema vs instance (U1 §2)
- Schema: `STUDENT(RollNo, Name, Course)`
- Instance: `(101, Ravi, MCA)` — inserts/updates change the instance, not the schema.

## E-3. Three-level views (U1 §3)
A student sees courses and marks; an accounts employee sees fees and payments — same database, different **external views**.
Changing an index = **physical** change with no conceptual edit. Splitting a table while keeping a compatible view = **logical** change.

## E-4. ER example (U1 §4)
- Entities: STUDENT, COURSE, EMPLOYEE, DEPARTMENT.
- Composite: `Address = Street, City, PIN`. Derived: `Age` from `DateOfBirth`. Multivalued: multiple phone numbers.
- Cardinalities: Person–Passport (1:1), Department–Employee (1:N), Student–Course (M:N).
- Relationship attribute: `EnrollmentDate` on ENROLLS (describes the event).

## E-5. ER → relational (U1 §5)
```
STUDENT(StudentID, Name)
COURSE(CourseID, Title)
ENROLLS(StudentID, CourseID, EnrollDate)     ← M:N junction, composite key
```
`StudentID` and `CourseID` are foreign keys referencing their parent relations.

## E-6. SQL by category (U1 §7)
```sql
-- DDL
CREATE TABLE Student(StudentID INT PRIMARY KEY, Name VARCHAR(50), CourseID INT,
                     FOREIGN KEY(CourseID) REFERENCES Course(CourseID));
-- DML (query + aggregate)
SELECT CourseID, COUNT(*) FROM Student GROUP BY CourseID;
-- DML (modification)
UPDATE Student SET Name='Rahul' WHERE StudentID=101;
-- TCL
BEGIN; UPDATE Account SET Balance=Balance-500 WHERE AccountID=1; COMMIT;
-- DCL
GRANT SELECT ON Student TO user1;
```

## E-7. Integrity (U1 §8)
```sql
FOREIGN KEY(CourseID) REFERENCES Course(CourseID)   -- cannot reference a missing course
CHECK (Salary > 0)      UNIQUE(email)   NOT NULL(Name)
Referential actions: CASCADE | SET NULL | SET DEFAULT | RESTRICT / NO ACTION
```

## E-8. Functional dependency (U2 §1)
`StudentID → StudentName`: if StudentID 101 is Ravi, every occurrence of 101 must be Ravi.

## E-9. Attribute closure (U2 §1)
F = {A→B, B→C, C→D}: A⁺ = {A} → {A,B} → {A,B,C} → **{A,B,C,D}** ⇒ A is a key.

## E-10. 1NF violation (U2 §3)
```
STUDENT(StudentID, Name, Phones)  with Phones = '9876,8765'   ✗ non-atomic
→ STUDENT(StudentID, Name)  +  STUDENT_PHONE(StudentID, Phone)  ✓ 1NF
```

## E-11. 2NF violation (U2 §4) ← *the standard answer example*
```
ENROLL(StudentID, CourseID, StudentName, CourseName, Grade)
key = (StudentID, CourseID)
StudentID  → StudentName   (partial: only part of the key)
CourseID   → CourseName    (partial: only part of the key)
↓ decompose
STUDENT(StudentID, StudentName)
COURSE(CourseID, CourseName)
ENROLL(StudentID, CourseID, Grade)     ← Grade fully depends on the whole key
```

## E-12. 3NF violation (U2 §5) ← *the standard answer example*
```
EMPLOYEE(EmpID, DeptID, DeptName)
EmpID → DeptID ;  DeptID → DeptName  ⇒  EmpID → DeptName is TRANSITIVE
↓
EMPLOYEE(EmpID, DeptID)   DEPARTMENT(DeptID, DeptName)
```

## E-13. BCNF trigger (U2 §6)
Write the rule, not a new example: *X→Y is allowed only if X is a super key.* If a determinant such as
`DeptName` (not a super key) determines something, 3NF may still accept it (DeptName prime?) but **BCNF rejects it**.
(BCNF's own canonical case: a relation where a non-key attribute participates in determining the key.)

## E-14. 4NF violation (U2 §7)
```
STUDENT(Student, Hobby, Language)   hobbies independent of languages
→ STUDENT_HOBBY(Student, Hobby) + STUDENT_LANGUAGE(Student, Language)
```
Storing all combinations creates repeated, meaningless combinations.

## E-15. Lossless join (U2 §9)
R(A,B,C) → R1(A,B), R2(A,C): intersection = {A}; if **A→B** or **A→C** holds ⇒ lossless.

## E-16. Buffer/pages (U2 §12)
File → pages → buffer pool [P1, P7, P4, P9] → CPU. Page I/O, not record I/O, dominates cost.

## E-17. B+ tree (U2 §13)
```
root: [30 | 60]   → children [10|20], [40|50], [70|80|90]
leaves: [10,20] ↔ [40,50] ↔ [70,80,90]   (linked)
search 50: root → middle child → leaf [40,50] → record pointer
range 40..80: leaf [40,50] → follow link → leaf [70,80,90] → stop
```

## E-18. Hash index (U2 §14)
key 101 → hash(101) → bucket 5 → records/pointers. Two keys in one bucket = collision → overflow bucket/chaining/dynamic hashing.

## E-19. Bank transfer (U3 §1, ACID anchor)
Debit ₹500 from A, credit ₹500 to B. Crash after the debit ⇒ database incorrect unless the transaction is atomic:
either both become permanent or both are undone.

## E-20. SQL transactions (U3 §4)
```sql
BEGIN;
UPDATE Account SET Balance = Balance - 500 WHERE AccountID = 1;
UPDATE Account SET Balance = Balance + 500 WHERE AccountID = 2;
COMMIT;                     -- or ROLLBACK on error; SAVEPOINT for partial rollback
```

## E-21. Conflict serializability (U3 §5)
```
T1: R(X) … W(X) … COMMIT
T2:            R(X) … COMMIT
conflict on X (one is a write), T1 first ⇒ edge T1 → T2 ⇒ acyclic ⇒ conflict-serializable
```

## E-22. Deadlock (U3 §6)
T1 holds A, waits for B; T2 holds B, waits for A → cycle → deadlock.
Handling: prevention, avoidance, detection (wait-for graph), timeout.

## E-23. Log records (U3 §12)
```
<T1 START>  <T1, A, 100, 50>  <T1 COMMIT>
crash:  T1 committed → REDO if required ;  T2 uncommitted → UNDO
```

## E-24. Fragmentation (U4 §2)
- Horizontal: `CUSTOMER_NORTH` (customers from northern regions) vs `CUSTOMER_SOUTH`.
- Vertical: split columns; **repeat the primary key** in every fragment so a JOIN reconstructs the relation.

## E-25. 2PC (U4 §4)
Coordinator → PREPARE → P1/P2/P3 vote YES/NO → all YES ⇒ COMMIT, else ABORT.

## E-26. Sharding (U4 §9)
Dataset split as SHARD 1 (IDs 1–100), SHARD 2 (101–200), SHARD 3 (201–300).

## E-27. MongoDB model (U4 §10)
```
Database → collection 'students' → documents {_id:1, name:'Ravi', age:22}, ...
Table→Collection, Row→Document, Column→Field, PK→_id
```

## E-28. MongoDB CRUD (U4 §11)
```js
db.students.insertOne({name:'Ravi', age:22, course:'MCA'})
db.students.insertMany([{name:'Asha',age:23},{name:'John',age:21}])
db.students.find({age:{$gt:21}})
db.students.findOne({name:'Ravi'})
db.students.updateOne({name:'Ravi'}, {$set:{age:23}})
db.students.updateMany({course:'MCA'}, {$inc:{age:1}})
db.students.deleteOne({name:'Ravi'})
db.students.deleteMany({course:'MCA'})
```
Operators: `$gt $gte $lt $lte $eq $ne` · `$in $nin` · `$and $or $not $nor` · `$set $unset $inc $push $pull`

## E-29. MongoDB aggregation (U4 §12)
```js
db.sales.aggregate([
  {$match:{status:'paid'}},
  {$group:{_id:'$product', total:{$sum:'$amount'}}},
  {$sort:{total:-1}}
])
```
= filter paid sales → group by product → sum amount → sort by total descending.

## E-30. Cassandra CQL (U5 §2)
```sql
CREATE KEYSPACE college WITH replication = {'class':'SimpleStrategy','replication_factor':3};
CREATE TABLE student (id int PRIMARY KEY, name text, course text);
INSERT INTO student (id,name,course) VALUES (1,'Ravi','MCA');
SELECT * FROM student;   UPDATE student SET course='MTech' WHERE id=1;   DELETE FROM student WHERE id=1;
```
Schema evolution via `ALTER TABLE` — metadata is cluster-wide, so plan changes.

## E-31. Cassandra ordering (U5 §11) ← *favourite small question*
```sql
CREATE TABLE results (course text, year int, student_id int, name text,
                      PRIMARY KEY ((course), year, student_id));
```
`course` = **partition key** (where the data lives); `year`, `student_id` = **clustering columns**
(order of rows inside a partition).

## E-32. Redis (U5 §3)
```redis
SET user:101 'Ravi'      GET user:101        DEL key        EXISTS key
HSET user:101 name 'Ravi' course 'MCA'       HGET user:101 name
EXPIRE user:101 3600     INCR counter
```

## E-33. Cypher / Neo4j (U5 §5)
```cypher
CREATE (p:Person {name:'Alice', age:22});
MATCH (a:Person {name:'Alice'}), (b:Person {name:'Bob'}) CREATE (a)-[:FRIEND_OF]->(b);
MATCH (p:Person)-[:FRIEND_OF]->(f:Person) RETURN p.name, f.name;
MATCH (p:Person) WHERE p.age > 20 RETURN p;
MATCH (p:Person {name:'Alice'}) SET p.age=23 RETURN p;
MATCH (p:Person {name:'Alice'}) DETACH DELETE p;
MATCH (p:Person) RETURN p.name, p.age ORDER BY p.age DESC;
```
Pattern: `MATCH (node)-[:RELATIONSHIP]->(node) RETURN …`

## E-34. Vector embeddings (U5 §6)
Text/image/audio → embedding model → `[0.12, -0.31, 0.77, …]` → vector DB → similarity/nearest-neighbour index.
Two semantically related sentences ⇒ high cosine similarity.

## E-35. Similarity search (U5 §7)
Query → embed → vector index → top-k → metadata + original documents → results.
Brute force compares all vectors; ANN (HNSW graph, IVF clusters) searches a promising region.

## E-36. Index creation across systems (U5 §9–13)
```js
db.students.createIndex({age:1})                              // single-field
db.students.createIndex({course:1, age:-1})                   // compound — order matters
db.users.createIndex({email:1}, {unique:true})                // unique
db.students.find().sort({age:1})                              // sort uses the index
db.students.find().explain()                                  // inspect the query plan
```
- **CouchDB:** Mango indexes for selector queries; map/reduce views give ordered keys for range access.
- **Neo4j:** property index on `Person(name)` finds the *starting node* fast; traversal then follows relationships.
