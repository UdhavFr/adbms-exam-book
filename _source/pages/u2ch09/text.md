# 9. Lossless Join Decomposition

Source: ADBMS_MasterNotes.docx — folder `u2ch09`

### 9. Lossless Join Decomposition
_(p. 11)_
A decomposition is lossless if joining the decomposed relations produces exactly the original relation. It must neither lose valid information nor create spurious tuples.
For binary decomposition R into R1 and R2, a standard FD-based condition is that the common attributes functionally determine all attributes of at least one side, under the relevant dependency set.
Example: R(A,B,C), decomposed into R1(A,B) and R2(A,C). If A → B or A → C holds, the decomposition satisfies a common lossless-join criterion.
Original R(A,B,C)
       ↓ decomposition
 ┌────────────┐     ┌────────────┐
 │  R1(A,B)   │     │  R2(A,C)   │
 └──────┬─────┘     └──────┬─────┘
        └──────── JOIN ─────┘
                 ↓
          Original R recovered
