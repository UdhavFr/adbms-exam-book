# 11. Shadow Paging

Source: ADBMS_MasterNotes.docx — folder `u3ch11`

### 11. Shadow Paging
_(p. 19)_
Shadow paging maintains two page-table views: a stable shadow page table and a current page table. Modified pages are written to new locations rather than overwriting the old versions. At commit, the system switches the root pointer to the new page table.
Before update:
ROOT → SHADOW PAGE TABLE → old pages
             │
             └── stable

During update:
ROOT → CURRENT PAGE TABLE → new/modified pages
ROOT still preserves shadow mapping

COMMIT:
ROOT switches to CURRENT

CRASH BEFORE COMMIT:
Use SHADOW mapping
Shadow paging can simplify recovery because the old consistent mapping remains available, but it can suffer from fragmentation and copying/page-table management overhead.
