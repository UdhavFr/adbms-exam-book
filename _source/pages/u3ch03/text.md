# 3. ACID Properties

Source: ADBMS_MasterNotes.docx — folder `u3ch03`

### 3. ACID Properties
_(p. 15)_

| Property | Detailed meaning | Banking example |
|---|---|---|
| Atomicity | Transaction is all-or-nothing. If one essential operation fails, the whole transaction can be rolled back. | Debit and credit must both occur. |
| Consistency | Every committed transaction preserves integrity constraints and valid database rules. | No invalid account state after transfer. |
| Isolation | Intermediate effects of concurrent transactions are controlled so that execution is equivalent to an acceptable serial behavior under the isolation guarantee. | Another transaction should not see an invalid intermediate transfer state. |
| Durability | After commit, effects survive subsequent system failure subject to the DBMS's durability guarantees. | Committed transfer remains after restart. |

EXAM-READY POINT: ACID is one of the highest-value topics. Explain each property with a definition plus the bank-transfer example.
