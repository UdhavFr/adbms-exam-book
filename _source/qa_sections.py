import re, pathlib
files = ['exam/notes/memory-hooks.md', 'exam/notes/diagrams-and-mental-models.md',
         'exam/notes/final-cram.md', 'exam/notes/common-mistakes.md',
         'exam/notes/formulas.md', 'exam/notes/comparisons.md',
         'exam/notes/chapter-notes/unit-1.md']
for f in files:
    t = pathlib.Path(f).read_text(encoding='utf-8')
    heads = re.findall(r'^(#{1,3} .+)$', t, re.M)
    print('=====', f, len(t), 'bytes')
    for h in heads[:12]:
        print('   ', h[:70])
