import re, pathlib
d = pathlib.Path('site/adbms')
for f in ['index.html', 'ch19/index.html', 'ch20/index.html']:
    t = (d / f).read_text(encoding='utf-8')
    for m in re.finditer(r'&(?!amp;|lt;|gt;|quot;|#\d+;|#[xX][0-9a-fA-F]+;|nbsp;)[\s<]', t):
        s = max(0, m.start() - 60)
        print(f, '->', repr(t[s:m.start() + 10]))
print('---- markDone refs ----')
n = (d / 'narrate.js').read_text(encoding='utf-8')
for m in re.finditer(r'markDone\(\d+\)', n):
    print(m.group(0))
