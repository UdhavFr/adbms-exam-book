# 7. CAP Theorem

Source: ADBMS_MasterNotes.docx — folder `u4ch07`

### 7. CAP Theorem
_(p. 23)_
CAP theorem states that when a distributed system experiences a network partition, it cannot simultaneously guarantee both strong consistency and availability for every request under the formal CAP definitions.
                 CONSISTENCY (C)
                       /\
                      /  \
                     /    \
                    /      \
                   /        \
                  /          \
     AVAILABILITY (A) ------ PARTITION (P)

During a partition, a system must make a design trade-off
between consistency and availability.
#### Consistency
_(p. 23)_
A read observes the most recent write according to the system's formal consistency guarantee, or an error.
#### Availability
_(p. 23)_
Every request to a non-failing node receives a non-error response, though the response need not contain the latest value.
#### Partition tolerance
_(p. 23)_
The system continues to operate despite network failures that prevent some nodes from communicating.
EXAM-READY POINT: Do not write 'you can simply pick any two out of three at all times.' CAP is specifically about behavior when a network partition occurs.
