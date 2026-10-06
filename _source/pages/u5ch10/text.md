# 10. CouchDB Indexing and Ordering

Source: ADBMS_MasterNotes.docx — folder `u5ch10`

### 10. CouchDB Indexing and Ordering
_(p. 31)_
CouchDB is a document database that exposes an HTTP/REST-oriented interface. It supports Mango indexes for selector queries and map/reduce views for indexed query patterns.
A Mango index can be created on fields such as course or age and then used by a selector query. Views can generate indexed key/value structures, where key ordering can be used for efficient range-style access.
The important exam point is that indexes in CouchDB avoid repeatedly scanning all documents and make predictable query patterns much more efficient.
