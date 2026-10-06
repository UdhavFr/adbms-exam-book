# | Title | Unit (per DOCX) | Minutes | Status
1 | The normalization ladder (1NF→BCNF) | Unit 2 (ch19) | 12 | ready
2 | ACID: the big four | Unit 3 (ch20) | 12 | ready
3 | CAP: the precise claim | Unit 4 (ch21) | 12 | ready
4 | 2PL + deadlock | Unit 3 (ch22) | 12 | ready
5 | Recovery: deferred/immediate/WAL/checkpoints | Unit 3 (ch23) | 12 | ready
6 | B+ tree indexing | Unit 2 (ch24) | 12 | ready
7 | 2PC rounds + fragmentation rebuild | Unit 4 (ch25) | 12 | ready

## Narration candidacy (grounded in the DOCX's own structure)

The DOCX's MASTER 20-MARK ANSWER BANK asks exactly 5 questions — each is a
natural narrated lesson: Q1 normalization (ch19 done), Q2 txn/concurrency/recovery
(ch20 covers ACID; ch22–23 complete it), Q3 distributed+CAP (ch21 done; ch25 completes
it), Q4 NoSQL+MongoDB (slideshow-style, lower animation value — text suffices),
Q5 indexing (ch24 planned).

- **Tier 1 — procedural, highly drawable (do next):** 2PL grow/shrink + wait-for
  cycle (U3-6) · deferred vs immediate + WAL-before-data + checkpoint bounding
  (U3-9/10/12) · B+ tree search walk + hash contrast (U2-13/14) · 2PC
  prepare→vote→decision + fragment rebuild UNION/JOIN (U4-2/4).
- **Tier 2 — drawable but thinner:** ER→tables mapping walk (U1-5) ·
  serializability graph test (U3-5) · MongoDB pipeline $match-first (U4-12) ·
  isolation ladder (already inside ch20).
- **Tier 3 — don't narrate (text wins):** definitions, disk/storage background,
  CouchDB, EER depth, proofs. Reading is faster than watching for facts.
