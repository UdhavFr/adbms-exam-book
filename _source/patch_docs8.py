import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')
subs = [
    ('concepts & modeling', 'concepts &amp; modeling'),
    ('normalization & storage', 'normalization &amp; storage'),
    ('transactions & recovery', 'transactions &amp; recovery'),
    ('distributed & NoSQL', 'distributed &amp; NoSQL'),
    ('stores & indexing', 'stores &amp; indexing'),
    ('rules & criteria', 'rules &amp; criteria'),
    ('traps & clarif', 'traps &amp; clarif'),
]
n = 0
for old, new in subs:
    if old in t:
        t = t.replace(old, new)
        n += 1
p.write_text(t, encoding='utf-8')
print('escaped', n)
