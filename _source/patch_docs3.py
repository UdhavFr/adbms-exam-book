import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')

e1_old = """def chrome(title, body, ch=None):
    body = linkify_mdfiles(body)
    nav = ''"""
e1_new = """def rebase(html, base):
    if not base:
        return html
    def rep(m):
        url = m.group(2)
        if url.startswith(('http', '#', '../', 'data:')):
            return m.group(0)
        if url.startswith('docs/'):
            url = url[5:]
        else:
            url = '../' + url
        return m.group(1) + '="' + url + '"'
    return re.sub(r'(href|src)="([^"]+)"', rep, html)

def chrome(title, body, ch=None, base=''):
    body = linkify_mdfiles(body)
    body = add_ids_toc(body)
    nav = ''"""
assert e1_old in t, 'e1 anchor missing'
t = t.replace(e1_old, e1_new, 1)

e2_old = """<script src="app.js"></script>
<script>initContents(21);initReveal();</script>
</body>
</html>
\"\"\"
"""
e2_new = """<script src="app.js"></script>
<script>initContents(21);initReveal();</script>
</body>
</html>
\"\"\"
    return rebase(page, base) if base else page
"""
assert e2_old in t, 'e2 anchor missing'
t = t.replace(e2_old, e2_new, 1)
p.write_text(t, encoding='utf-8')
print('chrome wired')
