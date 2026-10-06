# 13. B+ Tree Indexing

Source: ADBMS_MasterNotes.docx — folder `u2ch13`

### 13. B+ Tree Indexing
_(p. 13)_
A B+ tree is a balanced multiway search tree widely used for database indexing. Internal nodes contain separator keys and child pointers. Leaf nodes contain search keys and references to records/data pages. Leaf nodes are linked, which makes range scanning efficient.
                         [ 30 | 60 ]
                        /     |      \
                       /      |       \
              [10|20]      [40|50]    [70|80|90]
              / |  \        / | \       /  |  \
             ... ... ...    ... ... ... ... ... ...

Leaf level: [10,20] ↔ [40,50] ↔ [70,80,90]
                  linked for range traversal
#### Search process
_(p. 13)_
- Start at root.
- Compare search key with separator keys.
- Follow the correct child pointer.
- Continue until a leaf node is reached.
- Search the leaf and follow the record/data pointer.
#### Why B+ trees are efficient
_(p. 13)_
- Balanced height keeps search predictable.
- High fan-out reduces tree height.
- Linked leaves support efficient range queries.
- Dynamic insertion/deletion maintains the tree structure.
- Works well with disk pages because nodes can be sized to storage blocks.
Complexity is typically O(log_f N) node visits where f is the fan-out, with the actual cost depending on page size, tree height, caching, and implementation.
