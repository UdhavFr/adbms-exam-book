# 7. Multivalued Dependencies and 4NF

Source: ADBMS_MasterNotes.docx — folder `u2ch07`

### 7. Multivalued Dependencies and 4NF
_(p. 11)_
A multivalued dependency X ↠ Y occurs when, for each value of X, the set of Y values is independent of the remaining attributes. It often arises when an entity has two independent multivalued properties.
Example: STUDENT(Student, Hobby, Language). If a student's hobbies are independent of the languages the student knows, storing all combinations creates repeated combinations.
             STUDENT
          /           \
       HOBBIES      LANGUAGES
         │              │
         └── independent ┘

Instead of one large relation:
STUDENT_HOBBY(Student, Hobby)
STUDENT_LANGUAGE(Student, Language)
4NF requires that every non-trivial multivalued dependency X ↠ Y has X as a super key.
