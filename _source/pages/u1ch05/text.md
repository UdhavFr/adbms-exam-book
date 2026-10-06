# 5. Mapping ER Diagrams to Relational Schemas

Source: ADBMS_MasterNotes.docx — folder `u1ch05`

### 5. Mapping ER Diagrams to Relational Schemas
_(p. 6)_
ER-to-relational mapping transforms the conceptual ER design into tables suitable for a relational DBMS.
- For each strong entity, create a relation containing its simple attributes. Select the entity's primary key as the relation's primary key.
- For a composite attribute, store its individual components rather than the composite attribute as one field.
- For a multivalued attribute, create a separate relation containing the owner's primary key and the multivalued value.
- For a 1:1 relationship, place the primary key of one entity as a foreign key in the other, preferably where participation is total. Relationship attributes may be included there.
- For a 1:N relationship, place the primary key of the 1-side as a foreign key in the N-side relation.
- For an M:N relationship, create a separate relation containing the primary keys of both entities. These normally form a composite primary key.
- For a weak entity, create a relation containing its attributes and the owner's primary key; the owner key plus the weak entity's partial key identifies the weak entity.
Example: STUDENT(StudentID, Name) and COURSE(CourseID, Title) with ENROLLS(StudentID, CourseID, EnrollDate) represents an M:N relationship. StudentID and CourseID are foreign keys referencing their parent relations.
ER MODEL                         RELATIONAL MODEL
STUDENT ─── ENROLLS ─── COURSE   STUDENT(StudentID, Name)
   M             N                COURSE(CourseID, Title)
                                  ENROLLS(StudentID, CourseID,
                                          EnrollDate)
