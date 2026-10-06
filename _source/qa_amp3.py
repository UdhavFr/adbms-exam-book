import re, pathlib
t = pathlib.Path('site/adbms/index.html').read_text(encoding='utf-8')
for m in re.finditer(r'&(?!amp;|lt;|gt;|quot;|#\d+;|#[xX][0-9a-fA-F]+;|nbsp;)[\s<]', t):
    s = max(0, m.start() - 50)
    print(repr(t[s:m.start() + 8]))
