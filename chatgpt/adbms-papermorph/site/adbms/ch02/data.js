const CHAPTER={
  "number": 2,
  "unit": "Unit 1 · Foundations",
  "title": "2. ER Modeling & Relational Design",
  "beats": [
    {
      "title": "ENTITY, ATTRIBUTE, RELATIONSHIP",
      "body": "An entity is a distinguishable real-world object. Attributes describe entities. A relationship represents an association between entities.",
      "purpose": "Start conceptual modeling here.",
      "diagram": "er",
      "memory": "Thing = entity. Detail = attribute. Association = relationship.",
      "trap": null
    },
    {
      "title": "ATTRIBUTES: SPOT THE TYPE",
      "body": "Simple: cannot be meaningfully divided. Composite: has components. Single-valued: one value. Multivalued: several values. Derived: calculated from other data. Key attribute: uniquely identifies an entity.",
      "purpose": "These make easy 2–4 mark pickups inside a larger answer.",
      "diagram": "flow",
      "memory": "Age from DOB = derived. Address split into city/street = composite.",
      "trap": null,
      "items": [
        {
          "label": "SIMPLE",
          "hot": true
        },
        {
          "label": "COMPOSITE"
        },
        {
          "label": "MULTIVALUED"
        },
        {
          "label": "DERIVED"
        }
      ]
    },
    {
      "title": "KEYS: BUILD THE LADDER",
      "body": "Super key uniquely identifies. Candidate key is a minimal super key. Primary key is the chosen candidate key. Alternate key is an unchosen candidate key. Foreign key references a key in another relation.",
      "purpose": "Memorize the nesting: super ⊃ candidate → one candidate becomes primary.",
      "diagram": "flow",
      "memory": "Primary is chosen; alternate is candidate-but-not-chosen.",
      "trap": null,
      "items": [
        {
          "label": "SUPER KEY",
          "hot": true
        },
        {
          "label": "CANDIDATE"
        },
        {
          "label": "PRIMARY"
        }
      ]
    },
    {
      "title": "CARDINALITY + PARTICIPATION",
      "body": "Cardinality can be 1:1, 1:N or M:N. Total participation is mandatory; partial participation is optional.",
      "purpose": "A diagram + one sentence per constraint is high-value exam writing.",
      "diagram": "er",
      "memory": null,
      "trap": "Do not confuse cardinality (how many) with participation (mandatory or optional)."
    },
    {
      "title": "M:N MAPPING",
      "body": "For an M:N relationship, create a separate relation containing the primary keys of both entities, usually as a composite primary key. Relationship attributes such as EnrollmentDate live there too.",
      "purpose": "This is a classic mapping question.",
      "diagram": "flow",
      "memory": "M:N → junction table.",
      "trap": null,
      "items": [
        {
          "label": "STUDENT"
        },
        {
          "label": "ENROLLS",
          "hot": true
        },
        {
          "label": "COURSE"
        },
        {
          "label": "ENROLLMENT TABLE"
        }
      ]
    },
    {
      "title": "RELATIONAL CORE",
      "body": "Relation = table, tuple = row, attribute = column, domain = permitted values, degree = number of attributes, cardinality = number of tuples.",
      "purpose": "Fast vocabulary = fast marks.",
      "diagram": "flow",
      "memory": null,
      "trap": null
    },
    {
      "title": "EXAM ATTACK: ER → TABLES",
      "body": "Strong entity → relation. Composite attribute → store components. Multivalued attribute → separate relation. 1:1 → FK on one side, preferably total participation side. 1:N → 1-side key goes into N-side. M:N → separate relation. Weak entity → owner key + partial key.",
      "purpose": "Use this as a mechanical checklist.",
      "diagram": "flow",
      "memory": null,
      "trap": null
    }
  ],
  "quiz": [
    {
      "q": "For a 1:N relationship, where does the 1-side primary key usually go?",
      "opts": [
        "Into the 1-side as a duplicate",
        "As a foreign key in the N-side relation",
        "Into a brand-new relation always",
        "It is discarded"
      ],
      "a": 1,
      "why": "The 1-side key becomes a foreign key in the N-side.",
      "whyWrong": "A new table is specifically typical for M:N, not ordinary 1:N."
    },
    {
      "q": "A multivalued attribute is usually mapped by…",
      "opts": [
        "Repeating columns",
        "One big text field",
        "A separate relation with owner key + value",
        "Deleting the attribute"
      ],
      "a": 2,
      "why": "That keeps values addressable and relationally structured.",
      "whyWrong": "Repeating columns destroy the clean relational design."
    }
  ]
};