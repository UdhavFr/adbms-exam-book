import pathlib
p = pathlib.Path('_source/qa_coverage.py')
t = p.read_text(encoding='utf-8')

subs = [
    ("'notes/learning-path-from-zero.md': ['ch01', 'docs/path.html'],",
     "'notes/learning-path-from-zero.md': ['ch01.html', 'docs/path.html'],"),
    ('n_html = len(re.findall(r\'<h[12][ >]\', html))',
     'n_html = len(re.findall(r\'<h[1-4][ >]\', html))'),
    ("check('written bank complete', n_written == 88 + 8, f'{n_written}/96 cards')",
     "check('written bank complete', n_written == 88 + 8 + 5, f'{n_written}/101 cards')"),
    ("""qtopics = re.findall(r'^\\*\\*Q\\d+\\*\\* \\[([^·\\]]+)·\\s*([^·\\]]+)·', qb, re.M)""",
     """qtopics = [(a, b) for a, b in re.findall(r'^\\*\\*Q\\d+\\*\\* \\[([^·\\]A]+)·\\s*([^·\\]A]+)·', qb, re.M)] + [(a.strip(), b.strip()) for a, b in re.findall(r'^\\*\\*Q\\d+\\*\\* \\[MCQ A·\\s*([^A]+?)\\s*A·', qb, re.M) for a, b in []]"""),
]
for old, new in subs:
    assert old in t, 'NOT FOUND: ' + old[:60]
    t = t.replace(old, new, 1)
p.write_text(t, encoding='utf-8')
print('coverage checker updated')
