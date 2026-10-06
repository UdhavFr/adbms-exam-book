import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')

s1 = "    (21, 'ch21/index.html', '▶ Narrated: CAP, the precise claim', '12 min'),\n]"
assert s1 in t
t = t.replace(s1, "    (21, 'ch21/index.html', '▶ Narrated: CAP, the precise claim', '12 min'),\n"
                  "    (22, 'ch22/index.html', '▶ Narrated: 2PL + deadlock', '12 min'),\n]", 1)

s2 = "[7, 8, 9, 20, ('unit-3', 'Unit 3 notes', 'all 12 chapters, P0–P2 tagged')]"
assert s2 in t
t = t.replace(s2, "[7, 8, 9, 20, 22, ('unit-3', 'Unit 3 notes', 'all 12 chapters, P0–P2 tagged')]", 1)

t = t.replace('initContents(21);initReveal();', 'initContents(22);initReveal();')
t = t.replace('initCover();initContents(21);initCountdown();initReveal();',
              'initCover();initContents(22);initCountdown();initReveal();')
p.write_text(t, encoding='utf-8')

for f, old, new in [
    ('site/adbms/ch19/index.html', 'initContents(21);initReveal();', 'initContents(22);initReveal();'),
    ('site/adbms/ch20/index.html', 'initContents(21);initReveal();', 'initContents(22);initReveal();'),
    ('site/adbms/ch21/index.html', 'initContents(21);initReveal();', 'initContents(22);initReveal();'),
    ('books/adbms/chapters.md', '4 | 2PL + deadlock | Unit 3 (ch22) | 12 | planned',
     '4 | 2PL + deadlock | Unit 3 (ch22) | 12 | ready'),
    ('_source/qa_beats.py', "['site/adbms/ch19/index.html', 'site/adbms/ch20/index.html', 'site/adbms/ch21/index.html']",
     "['site/adbms/ch19/index.html', 'site/adbms/ch20/index.html', 'site/adbms/ch21/index.html', 'site/adbms/ch22/index.html']"),
    ('_source/qa_beats.py', "{'QAC1', 'QAC2', 'QAC3'}", "{'QAC1', 'QAC2', 'QAC3', 'QAC4'}"),
    ('_source/qa_inline.py', "['site/adbms/ch19/index.html', 'site/adbms/ch20/index.html', 'site/adbms/ch21/index.html']",
     "['site/adbms/ch19/index.html', 'site/adbms/ch20/index.html', 'site/adbms/ch21/index.html', 'site/adbms/ch22/index.html']"),
    ('_source/qa_deep.py', "if totals and totals != {'21'}:", "if totals and totals != {'22'}:"),
    ('_source/qa_deep.py', "issues.append(f'{rel}: initContents totals {totals} (expect 21)')",
     "issues.append(f'{rel}: initContents totals {totals} (expect 22)')"),
]:
    fp = pathlib.Path(f)
    ft = fp.read_text(encoding='utf-8')
    assert old in ft, f'NOT FOUND in {f}: {old[:60]}'
    fp.write_text(ft.replace(old, new, 1), encoding='utf-8')
print('ch22 wired everywhere')
