# 3. Redis — Key-Value Store

Source: ADBMS_MasterNotes.docx — folder `u5ch03`

### 3. Redis — Key-Value Store
_(p. 28)_
Redis is an in-memory data store that supports key-value access and richer data structures. It is commonly used for caching, sessions, counters, queues, leaderboards, and fast temporary state.
#### Common commands
_(p. 28)_

| Command | Purpose |
|---|---|
| SET key value | Stores a string value. |
| GET key | Retrieves a value. |
| DEL key | Deletes a key. |
| EXISTS key | Checks whether a key exists. |
| HSET key field value | Sets a field in a hash. |
| HGET key field | Reads a hash field. |
| EXPIRE key seconds | Sets a time-to-live. |
| INCR key | Atomically increments a numeric value. |

Example: SET user:101 'Ravi' → GET user:101 returns Ravi. HSET user:101 name 'Ravi' course 'MCA' stores multiple fields under one key.
