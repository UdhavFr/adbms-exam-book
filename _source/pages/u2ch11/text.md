# 11. Minimal Cover and Equivalence of FDs

Source: ADBMS_MasterNotes.docx — folder `u2ch11`

### 11. Minimal Cover and Equivalence of FDs
_(p. 12)_
A minimal cover is an equivalent, simplified set of functional dependencies with no unnecessary attributes or dependencies.
#### Steps
_(p. 12)_
- Split every FD so the right side contains a single attribute.
- Remove extraneous attributes from left sides by testing whether they are unnecessary.
- Remove redundant FDs if they can be derived from the remaining dependencies.
- The resulting set is a minimal/canonical cover.
Two sets F and G are equivalent when F+ = G+, meaning they imply exactly the same functional dependencies. Attribute closure is used to test implication.
EXAM-READY POINT: For numerical normalization questions, show every dependency, identify the candidate key, state the current normal form, identify the violation, decompose, and state why the new relations satisfy the target normal form.
