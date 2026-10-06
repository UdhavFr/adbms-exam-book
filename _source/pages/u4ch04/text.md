# 4. Distributed Transaction Management

Source: ADBMS_MasterNotes.docx — folder `u4ch04`

### 4. Distributed Transaction Management
_(p. 22)_
A distributed transaction can access or update data at multiple sites. The system must maintain atomicity so that a transaction does not commit at one site and abort at another.
#### Two-Phase Commit (2PC)
_(p. 22)_
             COORDINATOR
                  │
             PREPARE?
        ┌─────────┼─────────┐
        ↓         ↓         ↓
       P1        P2        P3
        │         │         │
      YES        YES       YES
        └─────────┼─────────┘
                  ↓
          GLOBAL COMMIT
                  │
        ┌─────────┼─────────┐
        ↓         ↓         ↓
       P1        P2        P3
- Coordinator sends PREPARE to participants.
- Each participant checks whether it can commit and records a prepared state.
- Participants vote YES/NO.
- If all required votes are YES, coordinator sends COMMIT; otherwise it sends ABORT.
- Participants record and execute the decision.
2PC ensures atomic commitment but can block in some failure scenarios, especially when participants are prepared and cannot learn the coordinator's final decision.
