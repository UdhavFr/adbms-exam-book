# 3. First Normal Form (1NF)

Source: ADBMS_MasterNotes.docx — folder `u2ch03`

### 3. First Normal Form (1NF)
_(p. 10)_
A relation is in First Normal Form when each attribute contains atomic values and there are no repeating groups or nested sets stored inside a single relational field.
Non-1NF example: STUDENT(StudentID, Name, Phones) where Phones contains '9876,8765'. A relational design stores one phone value per row in a separate relation.
Decomposition: STUDENT(StudentID, Name) and STUDENT_PHONE(StudentID, Phone).
#### Benefits of 1NF
_(p. 10)_
- Makes individual values addressable.
- Simplifies searching and updating.
- Removes repeating groups.
- Provides a foundation for higher normal forms.
