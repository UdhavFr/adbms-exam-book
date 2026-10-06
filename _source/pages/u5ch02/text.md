# 2. Cassandra Basic Operations

Source: ADBMS_MasterNotes.docx — folder `u5ch02`

### 2. Cassandra Basic Operations
_(p. 27)_
Cassandra uses CQL (Cassandra Query Language), whose syntax resembles SQL but whose data model and query restrictions are different.
CREATE KEYSPACE college WITH replication = {'class':'SimpleStrategy','replication_factor':3};
CREATE TABLE student (id int PRIMARY KEY, name text, course text);
INSERT INTO student (id,name,course) VALUES (1,'Ravi','MCA');
SELECT * FROM student;
UPDATE student SET course='MTech' WHERE id=1;
DELETE FROM student WHERE id=1;
#### Schema evolution
_(p. 28)_
Cassandra has an explicit schema for tables and types even though NoSQL systems are often described as flexible-schema systems. ALTER TABLE can add or modify supported schema elements. Schema changes must be planned because schema metadata is shared across the cluster.
Important design principle: model Cassandra tables according to query patterns. Unlike a normalized relational design, it is common to duplicate data deliberately so required queries can be served efficiently without expensive joins.
