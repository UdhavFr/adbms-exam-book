# 7. Similarity Search

Source: ADBMS_MasterNotes.docx — folder `u5ch07`

### 7. Similarity Search
_(p. 30)_
Similarity search retrieves the items whose embeddings are closest to a query embedding according to a chosen metric.
USER QUERY
   ↓
EMBED QUERY
   ↓
QUERY VECTOR
   ↓
VECTOR INDEX
   ↓
Nearest neighbors / Top-k
   ↓
Metadata + original documents
   ↓
FINAL RESULTS
A brute-force method compares the query vector with every stored vector. This becomes expensive as the number of vectors grows. Approximate nearest-neighbor (ANN) indexes search a smaller, promising region of the vector space to achieve much lower latency.
#### HNSW
_(p. 30)_
Hierarchical Navigable Small World (HNSW) is a graph-based ANN technique. It creates a navigable graph in which search moves through increasingly close candidates. It is widely used because it offers a practical balance between search speed, memory usage, and recall.
#### IVF-style indexing
_(p. 30)_
Inverted-file methods partition vectors into groups or clusters and search only relevant groups. This reduces the number of vectors examined during a query.
