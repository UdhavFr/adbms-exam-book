# DIAGRAM PRACTICE SHEET

Source: ADBMS_MasterNotes.docx — folder `app_diagram-practice-sheet`

## DIAGRAM PRACTICE SHEET
_(p. 34)_
Practise drawing these diagrams from memory. They are deliberately simple enough to reproduce quickly in an exam.
1. THREE LEVEL ARCHITECTURE
External Views → Conceptual Schema → Internal Schema → Storage

2. ER MODEL
[STUDENT] ─── ◇ ENROLLS ◇ ─── [COURSE]
             M              N

3. NORMALIZATION
UNF → 1NF → 2NF → 3NF → BCNF → 4NF → 5NF

4. B+ TREE
          [30 | 60]
         /    |    \
      [10]  [40]  [70|80]
       ↔      ↔      ↔

5. TRANSACTION
ACTIVE → PARTIALLY COMMITTED → COMMITTED
   │
   └→ FAILED → ABORTED

6. 2PL
GROWING (acquire) → LOCK POINT → SHRINKING (release)

7. RECOVERY
LOG → CHECKPOINT → CRASH → UNDO uncommitted + REDO committed

8. DISTRIBUTED DB
SITE A ↔ NETWORK ↔ SITE B ↔ NETWORK ↔ SITE C

9. CAP
             C
            / \
           /   \
          A --- P

10. SHARDING
DATA → SHARD 1 | SHARD 2 | SHARD 3

11. VECTOR SEARCH
QUERY → EMBEDDING → VECTOR INDEX → TOP-K → RESULTS
