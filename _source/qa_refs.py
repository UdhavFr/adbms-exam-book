import re, pathlib
d = pathlib.Path('site/adbms')
n_embeds = n_mdlinks = 0
for p in sorted(d.rglob('*.html')):
    t = p.read_text(encoding='utf-8')
    e = len(re.findall(r'<details class="ref">', t))
    m = len(re.findall(r'href="\.\./\.\./exam/[^"]+\.md"', t))
    left = re.findall(r'@@REF(BOX|IN)\d+@@', t) + re.findall(r'&lt;details', t)
    if e or m:
        print(p.relative_to(d), 'embeds:', e, 'md-links:', m)
    if left:
        print('  LEFTOVER:', p.relative_to(d), left[:3])
    n_embeds += e
    n_mdlinks += m
print('TOTAL embeds:', n_embeds, '| md-links:', n_mdlinks)
# verify every md href target exists
missing = set()
for p in d.rglob('*.html'):
    t = p.read_text(encoding='utf-8')
    for h in re.findall(r'href="(\.\./\.\./exam/[^"]+)"', t):
        target = (p.parent / h).resolve()
        if not target.is_file():
            missing.add((p.relative_to(d).as_posix(), h))
print('missing md targets:', missing or 'NONE')
