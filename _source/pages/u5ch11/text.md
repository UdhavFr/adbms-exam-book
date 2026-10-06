# 11. Cassandra Indexing and Ordering

Source: ADBMS_MasterNotes.docx — folder `u5ch11`

### 11. Cassandra Indexing and Ordering
_(p. 31)_
Cassandra relies heavily on primary-key design. The partition key decides the node/partition location, while clustering columns define the order of rows within a partition.
Example: CREATE TABLE results (course text, year int, student_id int, name text, PRIMARY KEY ((course), year, student_id));
Here, course is the partition key. Within a course partition, rows are ordered by year and then student_id according to clustering rules.
Cassandra supports secondary indexing mechanisms, but arbitrary indexing is not a substitute for good partition design. Query-driven data modeling is central.
Partition key → determines WHERE data lives
       ↓
Clustering columns → determine row ORDER within partition
       ↓
Efficient partition-local query
