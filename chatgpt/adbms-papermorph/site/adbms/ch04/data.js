const CHAPTER={
  "number": 4,
  "unit": "Unit 2 · Normalization & Storage",
  "title": "4. Functional Dependencies & Normal Forms",
  "beats": [
    {
      "title": "FUNCTIONAL DEPENDENCY",
      "body": "X → Y means: if two tuples agree on X, they must agree on Y. X is the determinant and Y is functionally dependent on X. Example: StudentID → StudentName.",
      "purpose": "FDs are the grammar behind normalization.",
      "diagram": "flow",
      "memory": "Arrow means: same X forces same Y.",
      "trap": null,
      "items": [
        {
          "label": "DETERMINANT X",
          "hot": true
        },
        {
          "label": "→"
        },
        {
          "label": "DEPENDENT Y"
        }
      ]
    },
    {
      "title": "ATTRIBUTE CLOSURE",
      "body": "X+ is the set of attributes functionally determined by X. Start with X and repeatedly add attributes from applicable FDs. If X+ contains every attribute of the relation, X is a super key.",
      "purpose": "Very likely numerical/problem area.",
      "diagram": "flow",
      "memory": "Closure = “what can X reach?”",
      "trap": null,
      "items": [
        {
          "label": "START X",
          "hot": true
        },
        {
          "label": "APPLY FDs"
        },
        {
          "label": "X+"
        },
        {
          "label": "ALL ATTRS?"
        }
      ]
    },
    {
      "title": "THE NORMALIZATION LADDER",
      "body": "1NF removes repeating/non-atomic values. 2NF removes partial dependencies. 3NF removes undesirable transitive dependencies. BCNF requires every determinant to be a super key. 4NF handles non-trivial multivalued dependencies. 5NF handles problematic join dependencies.",
      "purpose": "Memorize the reason, not only the names.",
      "diagram": "norm",
      "memory": "Atomic → full key → no transitives → determinant=superkey → no bad MVD → no bad JD.",
      "trap": null,
      "stage": 0
    },
    {
      "title": "1NF",
      "body": "Every attribute contains atomic values; no repeating groups or nested sets in a field. Example: Phones stored as “9876,8765” violates the idea; split to STUDENT_PHONE(StudentID, Phone).",
      "purpose": "The “one cell, one atomic value” test.",
      "diagram": "norm",
      "memory": null,
      "trap": null,
      "stage": 1
    },
    {
      "title": "2NF",
      "body": "Relation must be in 1NF and every non-prime attribute must depend on the entire candidate key. Main enemy: partial dependency on part of a composite key. Example ENROLL(StudentID, CourseID, StudentName, CourseName, Grade).",
      "purpose": "Look for a composite key first.",
      "diagram": "norm",
      "memory": null,
      "trap": null,
      "stage": 2
    },
    {
      "title": "3NF",
      "body": "Relation must be in 2NF and avoid undesirable transitive dependency of non-prime attributes on a key. Example: EmpID → DeptID and DeptID → DeptName, so DeptName moves to DEPARTMENT.",
      "purpose": "Classic “employee → department → department name” pattern.",
      "diagram": "norm",
      "memory": null,
      "trap": null,
      "stage": 3
    },
    {
      "title": "BCNF, 4NF, 5NF",
      "body": "BCNF: every determinant is a super key. 4NF: every non-trivial MVD has a super-key determinant. 5NF: every non-trivial join dependency is implied by candidate keys.",
      "purpose": "These distinctions are easy marks when stated precisely.",
      "diagram": "norm",
      "memory": "BCNF = determinant. 4NF = MVD. 5NF = JD.",
      "trap": "Do not reduce CAP or normal forms to vague slogans; define the exact dependency being controlled.",
      "stage": 5
    },
    {
      "title": "LOSSLESS + DEPENDENCY PRESERVATION",
      "body": "Lossless decomposition recreates exactly the original relation and avoids spurious tuples. Dependency preservation means original important FDs can be enforced on decomposed relations without joins. They are different properties.",
      "purpose": "Say the question each property answers.",
      "diagram": "flow",
      "memory": "Lossless = reconstruct. Preservation = enforce.",
      "trap": null,
      "items": [
        {
          "label": "DECOMPOSE",
          "hot": true
        },
        {
          "label": "LOSSLESS?"
        },
        {
          "label": "DEPENDENCIES PRESERVED?"
        }
      ]
    },
    {
      "title": "MINIMAL COVER",
      "body": "Split RHS so each FD has one attribute. Remove extraneous attributes from LHS when unnecessary. Remove redundant FDs. Result = minimal/canonical cover.",
      "purpose": "A clean 3-step procedure earns method marks.",
      "diagram": "flow",
      "memory": null,
      "trap": null,
      "items": [
        {
          "label": "SPLIT RHS",
          "hot": true
        },
        {
          "label": "REMOVE EXTRANEOUS"
        },
        {
          "label": "REMOVE REDUNDANT"
        }
      ]
    }
  ],
  "quiz": [
    {
      "q": "What does 2NF mainly remove?",
      "opts": [
        "Non-atomic values",
        "Partial dependencies",
        "Transitive dependencies",
        "Join dependencies"
      ],
      "a": 1,
      "why": "2NF attacks partial dependency on part of a composite key.",
      "whyWrong": "3NF is the transitive-dependency stage."
    },
    {
      "q": "BCNF requires…",
      "opts": [
        "Every determinant is a super key",
        "Every table has two keys",
        "All attributes are atomic",
        "No foreign keys"
      ],
      "a": 0,
      "why": "That is the memorization sentence from the notes.",
      "whyWrong": "Atomicity is 1NF, not BCNF."
    }
  ]
};