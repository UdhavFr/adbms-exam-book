# 8. Join Dependencies and 5NF

Source: ADBMS_MasterNotes.docx — folder `u2ch08`

### 8. Join Dependencies and 5NF
_(p. 11)_
A join dependency states that a relation can be reconstructed by joining several projections. 5NF, or Project-Join Normal Form, addresses redundancy that remains because of complex join dependencies not captured adequately by functional and multivalued dependencies.
A relation is in 5NF when every non-trivial join dependency is implied by candidate keys. 5NF is relatively uncommon in routine application design but is important for understanding advanced relational decomposition.
Exam distinction: 4NF deals with independent multivalued facts; 5NF deals with complex join dependencies and lossless reconstruction through projections.
