# 8. BASE vs ACID

Source: ADBMS_MasterNotes.docx — folder `u4ch08`

### 8. BASE vs ACID
_(p. 24)_

| ACID | BASE |
|---|---|
| Atomicity, Consistency, Isolation, Durability. | Basically Available, Soft state, Eventual consistency. |
| Strong transaction-oriented guarantees. | Availability and flexible consistency emphasis. |
| Common in traditional relational transaction systems. | Common in many distributed NoSQL architectures/use cases. |
| Commit aims at durable consistent state. | State may change as replicas converge. |

BASE does not mean data is permanently wrong. It means the system may accept temporary inconsistency while providing high availability and eventual convergence under suitable conditions.
