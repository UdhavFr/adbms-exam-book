import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')
old = """    def rep(m):
        url = m.group(2)
        if url.startswith(('http', '#', '../', 'data:')):
            return m.group(0)"""
assert old in t, 'rebase rep not found'
new = """    def rep(m):
        url = m.group(2)
        if url.startswith(('http', '#', 'data:')):
            return m.group(0)
        if url.startswith('../'):
            return m.group(1) + '="' + base + url + '"'
"""
t = t.replace(old, new, 1)
p.write_text(t, encoding='utf-8')
print('rebase depth fixed')
