import pathlib, re
files = ['exam/notes/learning-path-from-zero.md','exam/notes/classification-drills.md',
         'exam/notes/final-cram.md','exam/notes/ultra-short-notes.md',
         'exam/mock-exam-1.md','exam/mock-exam-1-key.md',
         'exam/mock-exam-2.md','exam/mock-exam-3.md']
fence = re.compile(r'^```', re.M)
bq = re.compile(r'^>', re.M)
tbl = re.compile(r'^\|.*\|$', re.M)
h1 = re.compile(r'^# ', re.M)
lnk = re.compile(r'\[.+?\]\(.+?\)')
hr = re.compile(r'^---+$', re.M)
for f in files:
    t = pathlib.Path(f).read_text(encoding='utf-8')
    print(f, {'fences': len(fence.findall(t)), 'blockquote': len(bq.findall(t)),
              'tables': len(tbl.findall(t)), 'details': t.count('<details'),
              'h1': len(h1.findall(t)), 'links': len(lnk.findall(t)),
              'hr': len(hr.findall(t))})
