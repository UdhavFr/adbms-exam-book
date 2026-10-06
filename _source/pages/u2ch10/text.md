# 10. Dependency Preservation

Source: ADBMS_MasterNotes.docx — folder `u2ch10`

### 10. Dependency Preservation
_(p. 12)_
A decomposition is dependency preserving if the important original functional dependencies can be enforced by enforcing dependencies on the decomposed relations individually, without requiring joins.
Losslessness and dependency preservation are different properties. A decomposition may be lossless but not dependency preserving, or dependency preserving but not lossless. Good database design seeks both when possible.

| Property | Question it answers |
|---|---|
| Lossless join | Can I reconstruct the original relation exactly? |
| Dependency preservation | Can I enforce the original dependencies without joining decomposed relations? |

