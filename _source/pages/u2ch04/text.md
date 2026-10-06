# 4. Second Normal Form (2NF)

Source: ADBMS_MasterNotes.docx — folder `u2ch04`

### 4. Second Normal Form (2NF)
_(p. 10)_
A relation is in 2NF if it is already in 1NF and every non-prime attribute is fully functionally dependent on the entire candidate key. Partial dependency is therefore the main problem addressed by 2NF.
Example: ENROLL(StudentID, CourseID, StudentName, CourseName, Grade). Candidate key = (StudentID, CourseID). StudentName depends only on StudentID and CourseName depends only on CourseID. Therefore these are partial dependencies.
ENROLL(StudentID, CourseID, StudentName, CourseName, Grade)
          │             │
          │             └── CourseID → CourseName
          └──────────────── StudentID → StudentName

Decompose:
STUDENT(StudentID, StudentName)
COURSE(CourseID, CourseName)
ENROLL(StudentID, CourseID, Grade)
The decomposition removes repeated student and course details and keeps Grade dependent on the complete enrollment key.
