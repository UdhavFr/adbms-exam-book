# 9. Sharding and Partitioning

Source: ADBMS_MasterNotes.docx — folder `u4ch09`

### 9. Sharding and Partitioning
_(p. 24)_
Sharding is horizontal distribution of records across multiple nodes. Each shard stores a subset of the dataset.
                    DATASET
                       │
              SHARDING / PARTITION
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       SHARD 1      SHARD 2      SHARD 3
       IDs 1–100    101–200      201–300
#### Strategies
_(p. 24)_
- Range-based: key ranges are assigned to shards; good for ranges but can create hotspots.
- Hash-based: a hash of the shard key chooses the shard; usually distributes load evenly but weakens range locality.
- Directory-based: a mapping service tells the system where each key is stored.
- Geographic: records are assigned by region, useful for locality and compliance requirements.
A good shard key should distribute data and traffic evenly, support common queries, and avoid oversized partitions or hotspots.
