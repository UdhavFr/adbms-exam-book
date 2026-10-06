import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')
i = t.find('_approximat')
print('found at', i)
print(repr(t[i - 30:i + 40]))
