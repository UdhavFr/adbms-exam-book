# 4. Conceptual Modeling Using ER Approach

Source: ADBMS_MasterNotes.docx — folder `u1ch04`

### 4. Conceptual Modeling Using ER Approach
_(p. 5)_
The Entity–Relationship (ER) approach is a high-level conceptual modeling technique used before implementing the database. It describes entities, their attributes, relationships, and constraints in a form that is easy to understand.
#### Entities
_(p. 5)_
An entity is a distinguishable real-world object about which data is stored. Examples include STUDENT, EMPLOYEE, PRODUCT and DEPARTMENT. An entity set is a collection of similar entities.
#### Attributes
_(p. 5)_
- Simple attribute: cannot be meaningfully divided further, such as Age.
- Composite attribute: consists of components, such as Address containing Street, City and PIN.
- Single-valued attribute: has one value for each entity.
- Multivalued attribute: may contain several values, such as multiple phone numbers.
- Derived attribute: calculated from other data, such as Age derived from DateOfBirth.
- Key attribute: uniquely identifies an entity.
#### Keys
_(p. 5)_

| Key | Meaning |
|---|---|
| Super key | Any attribute set that uniquely identifies a tuple/entity. |
| Candidate key | Minimal super key. |
| Primary key | Candidate key selected as the main identifier. |
| Alternate key | Candidate key not selected as primary key. |
| Foreign key | Attribute(s) referencing a key in another relation. |

#### Relationships and cardinality
_(p. 5)_
A relationship represents an association between entities. Examples include STUDENT enrolls in COURSE, EMPLOYEE works for DEPARTMENT, and CUSTOMER places ORDER. Cardinality describes how many instances can participate.

| Cardinality | Meaning | Example |
|---|---|---|
| 1:1 | One entity is related to at most one entity on the other side. | Person–Passport |
| 1:N | One entity can relate to many entities. | Department–Employee |
| M:N | Many entities on both sides can be related. | Student–Course |

#### Participation constraints
_(p. 5)_
Total participation means every entity must participate in the relationship. Partial participation means participation is optional. Structural constraints therefore communicate both cardinality and whether participation is mandatory.
        ┌──────────┐        ┌──────────┐
        │ STUDENT  │        │  COURSE  │
        └────┬─────┘        └────┬─────┘
             │                    │
             │       ENROLLS      │
             └───────◇───────────┘
                  M        N
                 /            
          EnrollmentDate
In the diagram, STUDENT and COURSE are entities and ENROLLS is an M:N relationship. EnrollmentDate is a relationship attribute because it describes the enrollment event rather than only one entity.
EXAM-READY POINT: In the exam, draw at least one ER diagram and explain every symbol. A diagram plus explanation usually makes the answer substantially stronger.
