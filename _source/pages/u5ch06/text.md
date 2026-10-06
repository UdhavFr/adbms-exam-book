# 6. Vector Databases and Embeddings

Source: ADBMS_MasterNotes.docx — folder `u5ch06`

### 6. Vector Databases and Embeddings
_(p. 29)_
A vector embedding converts an object such as text, image, audio, or product information into a numerical vector. An embedding model attempts to place semantically similar objects near each other in vector space.
ORIGINAL DATA
 Text / Image / Audio
        ↓
 EMBEDDING MODEL
        ↓
 [0.12, -0.31, 0.77, ...]
        ↓
 VECTOR DATABASE
        ↓
 similarity / nearest-neighbor index
For example, two semantically related sentences may produce vectors with high cosine similarity. The vectors themselves do not automatically contain human-readable meaning; their usefulness depends on the embedding model and application.
#### Similarity measures
_(p. 29)_

| Measure | Idea |
|---|---|
| Cosine similarity | Compares the angle/direction between vectors; widely used for semantic text retrieval. |
| Euclidean distance | Measures straight-line distance between points. |
| Dot product | Measures vector alignment and magnitude together; frequently used in retrieval systems. |

