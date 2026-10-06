# 1. Column-Oriented Databases: HBase and Cassandra

Source: ADBMS_MasterNotes.docx — folder `u5ch01`

### 1. Column-Oriented Databases: HBase and Cassandra
_(p. 27)_
Column-family or wide-column databases store data in a distributed structure organized around row keys and groups of columns. They are designed for very large datasets, horizontal scaling, and high-throughput distributed workloads.
#### HBase
_(p. 27)_
Apache HBase is a distributed, column-family database associated with the Hadoop ecosystem. A table has row keys and column families. Columns within families can be sparse and flexible. HBase is useful for large datasets requiring random read/write access at scale.
#### Cassandra
_(p. 27)_
Apache Cassandra is a distributed wide-column database designed for high availability, horizontal scalability, and high write throughput. It uses a partition key to distribute rows and clustering columns to order rows within each partition.
CASSANDRA TABLE
Partition key: course
        │
        ├── Partition: MCA
        │      ├── clustering row 1
        │      ├── clustering row 2
        │      └── clustering row 3
        │
        └── Partition: MBA
               ├── clustering row 1
               └── clustering row 2

| HBase | Cassandra |
|---|---|
| Strong Hadoop ecosystem relationship. | Independent distributed wide-column system. |
| Row key + column families. | Partition key + clustering columns. |
| HBase APIs/shell. | CQL. |
| Designed for large-scale sparse data. | Designed for highly available distributed workloads. |

