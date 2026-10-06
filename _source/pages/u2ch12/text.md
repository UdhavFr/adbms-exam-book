# 12. Data Storage, Disk Structure and Blocks

Source: ADBMS_MasterNotes.docx — folder `u2ch12`

### 12. Data Storage, Disk Structure and Blocks
_(p. 12)_
Database storage is organized to minimize expensive input/output operations between secondary storage and main memory. Data is normally transferred in pages or blocks rather than one individual record at a time.
SECONDARY STORAGE
 ┌───────────────────────────────────┐
 │ File                              │
 │ ┌────┬────┬────┬────┬────┐       │
 │ │Page│Page│Page│Page│Page│ ...   │
 │ └────┴────┴────┴────┴────┘       │
 └────────────────┬──────────────────┘
                  │ I/O
                  ↓
              BUFFER POOL
         ┌────┬────┬────┬────┐
         │ P1 │ P7 │ P4 │ P9 │
         └────┴────┴────┴────┘
                  ↓
              CPU / DBMS
A page contains records. The buffer manager brings pages into memory, keeps frequently needed pages available, and writes modified pages back to storage. Reducing page I/O is a major objective of query and storage optimization.
#### File organizations
_(p. 13)_

| Organization | Description | Best suited for |
|---|---|---|
| Heap | Unordered records; insertion is simple. | Frequent inserts, scans. |
| Sequential/sorted | Records kept in key order. | Ordered processing, range access. |
| Hash | Hash function maps key to bucket. | Equality lookups. |
| Clustered | Related records placed close together. | Queries accessing related records together. |

