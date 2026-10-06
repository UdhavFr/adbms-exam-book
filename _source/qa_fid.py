import re, pathlib
d = pathlib.Path('site/adbms')
for page, md in [('docs/diagrams.html', 'exam/notes/diagrams-and-mental-models.md'),
                 ('docs/definitions.html', 'exam/notes/definitions.md'),
                 ('docs/likely.html', 'exam/notes/likely-questions.md'),
                 ('docs/guide.html', 'exam/notes/master-study-guide.md')]:
    src = pathlib.Path(md).read_text(encoding='utf-8')
    html = (d / page).read_text(encoding='utf-8')
    n_md = len(re.findall(r'(?m)^#{1,4} ', src))
    n_h = len(re.findall(r'<h[1-4][ >]', html))
    print(page, 'md-headings:', n_md, 'h1-h4:', n_h, '-> complete:', n_h >= n_md)
