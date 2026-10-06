# 1. Introduction to Database Systems

Source: ADBMS_MasterNotes.docx — folder `u1ch01`

### 1. Introduction to Database Systems
_(p. 2)_
A database is an organized collection of logically related data that represents information about a particular application or organization. A Database Management System (DBMS) is software that allows users and applications to define, create, store, retrieve, update, protect, and recover data in a controlled manner. The database together with the DBMS forms a database system.
Examples of database applications include banking, railway and airline reservation, e-commerce, hospitals, universities, libraries, social networks, and financial systems. Modern systems may use relational DBMSs such as PostgreSQL and MySQL or NoSQL systems such as MongoDB, Cassandra, Redis, and Neo4j.
#### Why DBMS is needed
_(p. 2)_
A traditional file-processing system stores information in separate application files. When the same customer information is stored in many files, duplication occurs. If one copy is changed and another is not, inconsistency appears. File systems also make sharing, security, backup, concurrent access, and recovery difficult.

| Problem in file systems | How DBMS addresses it |
|---|---|
| Data redundancy | Centralized/shared database design reduces unnecessary duplication. |
| Data inconsistency | Constraints and controlled updates keep related data consistent. |
| Difficult data sharing | Multiple users/applications can access a common database. |
| Security problems | Authentication and authorization mechanisms control access. |
| Concurrent access | Concurrency-control mechanisms coordinate simultaneous transactions. |
| Failure recovery | Logging, checkpoints and recovery mechanisms restore consistency. |
| Program-data dependence | Data abstraction and data independence reduce application dependence on physical storage. |

#### Main functions of a DBMS
_(p. 2)_
- Data definition and schema management
- Data storage and efficient retrieval
- Query processing and optimization
- Transaction processing
- Concurrency control
- Integrity constraint enforcement
- Security and authorization
- Backup and recovery
- Metadata/catalog management
                 DATABASE SYSTEM
                       │
          ┌────────────┴────────────┐
          │                         │
      USERS / APPS                 DBMS
                                    │
       ┌──────────────┬─────────────┼──────────────┐
       │              │             │              │
   Query Manager  Transaction   Storage        Recovery
                  Manager       Manager         Manager
       │              │             │              │
       └──────────────┴─────────────┴──────────────┘
                              │
                           DATABASE
Conclusion: A DBMS provides a systematic environment in which data can be stored and manipulated while preserving security, integrity, concurrency, and recoverability.
EXAM-READY POINT: If asked 'Explain database systems', define database and DBMS, discuss limitations of file systems, functions of DBMS, architecture, advantages, and conclude with the role of DBMS in reliable information management.
