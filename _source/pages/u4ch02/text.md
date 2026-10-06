# 2. Data Fragmentation

Source: ADBMS_MasterNotes.docx — folder `u4ch02`

### 2. Data Fragmentation
_(p. 21)_
Fragmentation divides a relation into smaller fragments that can be stored close to the applications that use them. It can reduce communication cost and improve local performance.
#### Horizontal fragmentation
_(p. 21)_
Rows are divided according to predicates. Example: CUSTOMER_NORTH contains customers from northern regions and CUSTOMER_SOUTH contains customers from southern regions.
#### Vertical fragmentation
_(p. 21)_
Columns are divided. The primary key is normally repeated in each fragment so the original relation can be reconstructed through a join.
#### Hybrid fragmentation
_(p. 21)_
Combines horizontal and vertical fragmentation.
RELATION R
   │
   ├── Horizontal → rows A | rows B
   │
   ├── Vertical   → columns A | columns B + key
   │
   └── Hybrid      → rows first, then columns
A correct fragmentation should satisfy completeness, reconstruction, and disjointness where required by the strategy.
