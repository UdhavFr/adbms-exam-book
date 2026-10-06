# 1. Introduction to Distributed Databases

Source: ADBMS_MasterNotes.docx — folder `u4ch01`

### 1. Introduction to Distributed Databases
_(p. 21)_
A distributed database is a logically integrated database whose data is physically distributed across multiple network-connected sites. A Distributed Database Management System coordinates these sites and provides users with a unified way to access the distributed data.
                 DISTRIBUTED DATABASE
                        │
          ┌─────────────┼─────────────┐
          ↓             ↓             ↓
       SITE A         SITE B        SITE C
      Data A1        Data B1       Data C1
      Replica A2     Replica B2    Replica C2
          \             │             /
           └──────── NETWORK ─────────┘
#### Characteristics
_(p. 21)_
- Data physically distributed across sites.
- Sites communicate through a network.
- Fragments and replicas may be transparent to users.
- Supports distributed query and transaction processing.
- Must tolerate communication and node failures.
- Can improve availability and local performance.
- Introduces consistency and coordination challenges.
#### Types
_(p. 21)_
Homogeneous systems use similar DBMS technology across sites. Heterogeneous systems may combine different database technologies or schemas. Federated systems allow independently managed databases to cooperate through integration mechanisms.
