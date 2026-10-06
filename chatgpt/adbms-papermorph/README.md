# ADBMS Exam Quest — Papermorph-style interactive study book

Built from `ADBMS_MasterNotes.docx` using the Papermorph structure: 1600×900 SVG lesson stages, beat-based explanations, quick checks / mini-bosses, cover + contents, and local static delivery.

## Run

From this folder:

```bash
python3 -m http.server 8765 -d site
```

Open:

`http://localhost:8765/adbms/`

## Recommended exam-night path

1. Chapters 1–3: foundations / ER / SQL.
2. Chapters 4–5: normalization / indexing.
3. Chapters 6–7: ACID / concurrency / recovery.
4. Chapters 8–9: distributed DB / CAP / MongoDB.
5. Chapter 10: Cassandra / Redis / Neo4j / vectors / NoSQL indexing.
6. Chapter 11: 20-mark answer builder + mixed mock.

Use the arrow keys to move through beats, `Space` for browser narration, and the Mini-boss button for active recall.

## Source / fidelity

Content is a transformed, exam-oriented rendering of the supplied Advanced Database Systems study notebook. Definitions and terminology follow the source notebook; pedagogical memory hooks and interaction mechanics are added for retrieval practice.
