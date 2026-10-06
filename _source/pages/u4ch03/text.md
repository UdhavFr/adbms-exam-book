# 3. Replication and Allocation

Source: ADBMS_MasterNotes.docx — folder `u4ch03`

### 3. Replication and Allocation
_(p. 22)_
Replication means maintaining multiple copies of data at different sites. Full replication stores copies at many/all sites; partial replication stores copies at selected sites.

| Benefit | Cost |
|---|---|
| Higher availability | More storage |
| Faster local reads | Update coordination |
| Failure tolerance | Consistency management |
| Reduced remote access | Network/control overhead |

Allocation is the decision about which site stores which fragment or replica. It should consider query frequency, data locality, communication cost, storage capacity, and reliability requirements.
