import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')
old = "    'Written answer bank (101)',"
assert old in t
t = t.replace(old, "    'Written answer bank (102)',", 1)
old2 = "check('written bank complete', n_written == 88 + 8 + 5, f'{n_written}/101 cards')"
p2 = pathlib.Path('_source/qa_coverage.py')
t2 = p2.read_text(encoding='utf-8')
assert old2 in t2
t2 = t2.replace(old2, "check('written bank complete', n_written == 88 + 8 + 6, f'{n_written}/102 cards')", 1)
p.write_text(t, encoding='utf-8')
p2.write_text(t2, encoding='utf-8')
print('counts updated')
