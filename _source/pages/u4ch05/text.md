# 5. Distributed Consistency Models

Source: ADBMS_MasterNotes.docx — folder `u4ch05`

### 5. Distributed Consistency Models
_(p. 22)_
A consistency model defines what values and ordering guarantees clients can observe when data is replicated or distributed.
- Strong/linearizable-style consistency: operations appear to take effect in a single real-time-respecting order under the model.
- Eventual consistency: replicas may temporarily disagree but converge if updates stop.
- Causal consistency: causally related operations preserve their causal order.
- Session-oriented guarantees may provide read-your-writes or monotonic-read behavior.
Consistency is a design choice. Stronger consistency can require more coordination and may affect latency and availability during failures.
