import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')

s1 = "    (24, 'ch24/index.html', '▶ Narrated: B+ tree indexing', '12 min'),\n]"
assert s1 in t
t = t.replace(s1, "    (24, 'ch24/index.html', '▶ Narrated: B+ tree indexing', '12 min'),\n"
                  "    (25, 'ch25/index.html', '▶ Narrated: 2PC + fragmentation', '12 min'),\n]", 1)

s2 = "[10, 21, ('unit-4', 'Unit 4 notes', 'all 12 chapters, P0–P2 tagged')]"
assert s2 in t
t = t.replace(s2, "[10, 21, 25, ('unit-4', 'Unit 4 notes', 'all 12 chapters, P0–P2 tagged')]", 1)

t = t.replace('initContents(24);initReveal();', 'initContents(25);initReveal();')
t = t.replace('initCover();initContents(24);initCountdown();initReveal();',
              'initCover();initContents(25);initCountdown();initReveal();')
p.write_text(t, encoding='utf-8')

for f, old, new in [
    ('site/adbms/ch19/index.html', 'initContents(24);initReveal();', 'initContents(25);initReveal();'),
    ('site/adbms/ch20/index.html', 'initContents(24);initReveal();', 'initContents(25);initReveal();'),
    ('site/adbms/ch21/index.html', 'initContents(24);initReveal();', 'initContents(25);initReveal();'),
    ('site/adbms/ch22/index.html', 'initContents(24);initReveal();', 'initContents(25);initReveal();'),
    ('site/adbms/ch23/index.html', 'initContents(24);initReveal();', 'initContents(25);initReveal();'),
    ('site/adbms/ch24/index.html', 'initContents(24);initReveal();', 'initContents(25);initReveal();'),
    ('books/adbms/chapters.md', '7 | 2PC rounds + fragmentation rebuild | Unit 4 (ch25) | 12 | planned',
     '7 | 2PC rounds + fragmentation rebuild | Unit 4 (ch25) | 12 | ready'),
    ('_source/qa_beats.py', "'site/adbms/ch24/index.html']",
     "'site/adbms/ch24/index.html', 'site/adbms/ch25/index.html']"),
    ('_source/qa_beats.py', "{'QAC1', 'QAC2', 'QAC3', 'QAC4', 'QAC5', 'QAC6', 'QAC7'}",
     "{'QAC1', 'QAC2', 'QAC3', 'QAC4', 'QAC5', 'QAC6', 'QAC7', 'QAC8'}"),
    ('_source/qa_inline.py', "'site/adbms/ch24/index.html']",
     "'site/adbms/ch24/index.html', 'site/adbms/ch25/index.html']"),
    ('_source/qa_deep.py', "if totals and totals != {'24'}:", "if totals and totals != {'25'}:"),
    ('_source/qa_deep.py', '(expect 24)', '(expect 25)'),
]:
    fp = pathlib.Path(f)
    ft = fp.read_text(encoding='utf-8')
    assert old in ft, f'NOT FOUND in {f}: {old[:60]}'
    fp.write_text(ft.replace(old, new, 1), encoding='utf-8')
print('ch25 wired everywhere')
