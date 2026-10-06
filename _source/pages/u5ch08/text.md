# 8. Indexing and Ordering Data Sets

Source: ADBMS_MasterNotes.docx — folder `u5ch08`

### 8. Indexing and Ordering Data Sets
_(p. 30)_
An index is an auxiliary data structure that creates an efficient access path to data. Instead of scanning every record, the DBMS can use the index to locate likely matching records.
Without index:
Query → scan record 1 → record 2 → ... → record N

With index:
Query → INDEX → matching key/pointers → required records
Indexes improve reads but introduce costs. They consume storage and must be maintained when indexed data changes. Therefore, the goal is not to create the maximum number of indexes but to create useful indexes that match important query patterns.
#### Ordering
_(p. 30)_
Ordering arranges records or index keys according to a chosen criterion. Ordered structures such as B+ trees are useful for equality, range, prefix, and sorted retrieval. Hash indexes are not naturally ordered and therefore are poor for range queries.
