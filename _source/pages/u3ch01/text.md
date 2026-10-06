# 1. Concept of a Transaction

Source: ADBMS_MasterNotes.docx — folder `u3ch01`

### 1. Concept of a Transaction
_(p. 15)_
A transaction is a sequence of database operations that forms one logical unit of work. It may contain read, write, insert, update, delete, and control operations. A transaction must preserve database correctness even when several transactions execute concurrently or failures occur.
Classic example: bank transfer. Transfer ₹500 from A to B requires subtracting ₹500 from A and adding ₹500 to B. If the system crashes after subtracting A but before adding B, the database becomes incorrect. Transaction management ensures that either both operations become permanent or both are undone.
BEGIN
  ↓
READ A → WRITE A
  ↓
READ B → WRITE B
  ↓
COMMIT ─────────→ changes permanent
  │
  └── failure ───→ ROLLBACK / RECOVERY
