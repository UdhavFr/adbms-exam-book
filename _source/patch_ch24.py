import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')

s1 = "    (23, 'ch23/index.html', '▶ Narrated: recovery', '12 min'),\n]"
assert s1 in t
t = t.replace(s1, "    (23, 'ch23/index.html', '▶ Narrated: recovery', '12 min'),\n"
                  "    (24, 'ch24/index.html', '▶ Narrated: B+ tree indexing', '12 min'),\n]", 1)

s2 = "[4, 5, 6, 19, ('unit-2', 'Unit 2 notes', 'all 14 chapters, P0–P2 tagged')]"
assert s2 in t
t = t.replace(s2, "[4, 5, 6, 19, 24, ('unit-2', 'Unit 2 notes', 'all 14 chapters, P0–P2 tagged')]", 1)

t = t.replace('initContents(23);initReveal();', 'initContents(24);initReveal();')
t = t.replace('initCover();initContents(23);initCountdown();initReveal();',
              'initCover();initContents(24);initCountdown();initReveal();')
p.write_text(t, encoding='utf-8')

for f, old, new in [
    ('site/adbms/ch19/index.html', 'initContents(23);initReveal();', 'initContents(24);initReveal();'),
    ('site/adbms/ch20/index.html', 'initContents(23);initReveal();', 'initContents(24);initReveal();'),
    ('site/adbms/ch21/index.html', 'initContents(23);initReveal();', 'initContents(24);initReveal();'),
    ('site/adbms/ch22/index.html', 'initContents(23);initReveal();', 'initContents(24);initReveal();'),
    ('site/adbms/ch23/index.html', 'initContents(23);initReveal();', 'initContents(24);initReveal();'),
    ('books/adbms/chapters.md', '6 | B+ tree indexing | Unit 2 (ch24) | 12 | planned',
     '6 | B+ tree indexing | Unit 2 (ch24) | 12 | ready'),
    ('_source/qa_beats.py', "'site/adbms/ch23/index.html']",
     "'site/adbms/ch23/index.html', 'site/adbms/ch24/index.html']"),
    ('_source/qa_beats.py', "{'QAC1', 'QAC2', 'QAC3', 'QAC4', 'QAC5', 'QAC6'}",
     "{'QAC1', 'QAC2', 'QAC3', 'QAC4', 'QAC5', 'QAC6', 'QAC7'}"),
    ('_source/qa_inline.py', "'site/adbms/ch23/index.html']",
     "'site/adbms/ch23/index.html', 'site/adbms/ch24/index.html']"),
    ('_source/qa_deep.py', "if totals and totals != {'23'}:", "if totals and totals != {'24'}:"),
    ('_source/qa_deep.py', '(expect 23)', '(expect 24)'),
]:
    fp = pathlib.Path(f)
    ft = fp.read_text(encoding='utf-8')
    assert old in ft, f'NOT FOUND in {f}: {old[:60]}'
    fp.write_text(ft.replace(old, new, 1), encoding='utf-8')
print('ch24 wired everywhere')
