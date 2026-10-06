import pathlib
p = pathlib.Path('_source/qa_coverage.py')
t = p.read_text(encoding='utf-8')

s1 = "'notes/learning-path-from-zero.md': ['ch01', 'docs/path.html'],"
assert s1 in t
t = t.replace(s1, "'notes/learning-path-from-zero.md': ['ch01.html', 'docs/path.html'],", 1)

s2 = "n_html = len(re.findall(r'<h[12][ >]', html))"
assert s2 in t
t = t.replace(s2, "n_html = len(re.findall(r'<h[1-4][ >]', html))", 1)

s3 = "check('written bank complete', n_written == 88 + 8, f'{n_written}/96 cards')"
assert s3 in t
t = t.replace(s3, "check('written bank complete', n_written == 88 + 8 + 5, f'{n_written}/101 cards')", 1)

lines = t.splitlines()
idx = next(i for i, ln in enumerate(lines) if ln.startswith('qtopics = '))
old_block = lines[idx]
assert 'MCQ' not in old_block, 'already patched?'
new_block = ("qtopics_w = re.findall(r'^\\*\\*Q\\d+\\*\\* \\[([A-Z]+) · ([^·\\]]+) ·', qb, re.M)\n"
             "qtopics_m = re.findall(r'^\\*\\*Q\\d+\\*\\* \\[MCQ A·\\s*([^A][^·]*?)\\s*A·', qb, re.M)\n"
             "qtopics = [(a, b) for a, b in qtopics_w]\n"
             "covered = set(b.strip() for a, b in qtopics_w) | set(x.strip() for x in qtopics_m)")
lines[idx] = new_block
# downstream uses: covered = set(t[1].strip() for t in qtopics) -> replace
old_cov = 'covered = set(t[1].strip() for t in qtopics)'
assert old_cov in '\n'.join(lines)
t = '\n'.join(lines).replace(old_cov, 'covered = set(b.strip() for a, b in qtopics_w) | set(x.strip() for x in qtopics_m)', 1)
p.write_text(t, encoding='utf-8')
print('qa_coverage patched')
