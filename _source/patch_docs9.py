import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')
old = "    'Written answer bank (96)',"
assert old in t, 'title anchor missing'
t = t.replace(old, "    'Written answer bank (101)',", 1)
p.write_text(t, encoding='utf-8')
print('title updated')
