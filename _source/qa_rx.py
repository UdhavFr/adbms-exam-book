import re
line = '**Read:** `chapter-notes/unit-1.md` U1-1→U1-3 · **Hooks file:** `memory-hooks.md` §3'
m1 = re.search(r'`(chapter-notes/unit-\d\.md)`\s*(U\d+-\d+(?:\s*[→–-]\s*U\d+-\d+)?)?', line)
print('ch:', m1.groups() if m1 else None)
m2 = re.search(r'`((?:memory-hooks|diagrams-and-mental-models|final-cram|common-mistakes|formulas|processes-and-algorithms)\.md)`\s*[§#]([A-Za-z0-9]+)', line)
print('sec:', m2.groups() if m2 else None)
