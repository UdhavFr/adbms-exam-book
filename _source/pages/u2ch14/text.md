# 14. Hash-Based Indexing

Source: ADBMS_MasterNotes.docx — folder `u2ch14`

### 14. Hash-Based Indexing
_(p. 14)_
A hash index applies a hash function to a search key and maps the result to a bucket. It is particularly efficient for equality conditions such as StudentID = 101.
Search key: 101
     ↓
 hash(101)
     ↓
 bucket 5
     ↓
 records / pointers
If two keys map to the same bucket, a collision occurs. Overflow buckets, chaining, or dynamic hashing techniques can handle collisions.

| B+ Tree | Hash |
|---|---|
| Ordered structure. | Unordered bucket structure. |
| Excellent for equality + range queries. | Excellent for equality queries. |
| Supports ORDER BY/range traversal. | Poor for range traversal. |
| Balanced tree. | Hash function + buckets. |

## UNIT 3 — TRANSACTION PROCESSING, CONCURRENCY CONTROL AND RECOVERY
_(p. 15)_
