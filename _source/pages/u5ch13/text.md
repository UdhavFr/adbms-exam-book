# 13. Vector Store Indexing

Source: ADBMS_MasterNotes.docx — folder `u5ch13`

### 13. Vector Store Indexing
_(p. 31)_
Vector indexes are designed for nearest-neighbor search. Unlike a B+ tree that searches ordered scalar keys, a vector index organizes high-dimensional vectors so that similar vectors can be located efficiently.

| Traditional database index | Vector index |
|---|---|
| Exact/range-oriented access. | Similarity/nearest-neighbor access. |
| B+ tree or hash. | HNSW, IVF and related ANN structures. |
| Query: age = 22, price BETWEEN 100 AND 200. | Query: top-k vectors closest to query embedding. |
| Uses ordered keys or buckets. | Uses geometric/graph/cluster structure. |

