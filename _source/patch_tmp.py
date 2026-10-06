import pathlib
p = pathlib.Path('_source/qa_coverage.py')
t = p.read_text(encoding='utf-8')
i = t.find('qtopics = ')
j = t.find('\n', t.find("for a, b in []]") if "for a, b in []]" in t else i)
# find end of the (possibly already-patched) qtopics assignment: next line starting 'covered = '
k = t.find('\ncovered = ')
seg_start = t.find('qtopics = ')
print(repr(t[seg_start:k + 30]))
