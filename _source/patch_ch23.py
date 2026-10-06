import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')

s1 = "    (22, 'ch22/index.html', '▶ Narrated: 2PL + deadlock', '12 min'),\n]"
assert s1 in t
t = t.replace(s1, "    (22, 'ch22/index.html', '▶ Narrated: 2PL + deadlock', '12 min'),\n"
                  "    (23, 'ch23/index.html', '▶ Narrated: recovery', '12 min'),\n]", 1)

s2 = "[7, 8, 9, 20, 22, ('unit-3', 'Unit 3 notes', 'all 12 chapters, P0–P2 tagged')]"
assert s2 in t
t = t.replace(s2, "[7, 8, 9, 20, 22, 23, ('unit-3', 'Unit 3 notes', 'all 12 chapters, P0–P2 tagged')]", 1)

t = t.replace('initContents(22);initReveal();', 'initContents(23);initReveal();')
t = t.replace('initCover();initContents(22);initCountdown();initReveal();',
              'initCover();initContents(23);initCountdown();initReveal();')
p.write_text(t, encoding='utf-8')

for f, old, new in [
    ('site/adbms/ch19/index.html', 'initContents(22);initReveal();', 'initContents(23);initReveal();'),
    ('site/adbms/ch20/index.html', 'initContents(22);initReveal();', 'initContents(23);initReveal();'),
    ('site/adbms/ch21/index.html', 'initContents(22);initReveal();', 'initContents(23);initReveal();'),
    ('site/adbms/ch22/index.html', 'initContents(22);initReveal();', 'initContents(23);initReveal();'),
    ('books/adbms/chapters.md', '5 | Recovery: deferred/immediate/WAL/checkpoints | Unit 3 (ch23) | 12 | planned',
     '5 | Recovery: deferred/immediate/WAL/checkpoints | Unit 3 (ch23) | 12 | ready'),
    ('_source/qa_beats.py', "'site/adbms/ch22/index.html']",
     "'site/adbms/ch22/index.html', 'site/adbms/ch23/index.html']"),
    ('_source/qa_beats.py', "{'QAC1', 'QAC2', 'QAC3', 'QAC4'}", "{'QAC1', 'QAC2', 'QAC3', 'QAC4', 'QAC5', 'QAC6'}"),
    ('_source/qa_inline.py', "'site/adbms/ch22/index.html']",
     "'site/adbms/ch22/index.html', 'site/adbms/ch23/index.html']"),
    ('_source/qa_deep.py', "if totals and totals != {'22'}:", "if totals and totals != {'23'}:"),
    ('_source/qa_deep.py', '(expect 22)', '(expect 23)'),
]:
    fp = pathlib.Path(f)
    ft = fp.read_text(encoding='utf-8')
    assert old in ft, f'NOT FOUND in {f}: {old[:60]}'
    fp.write_text(ft.replace(old, new, 1), encoding='utf-8')
print('ch23 wired everywhere')
