import pathlib, re
for n in [1, 4, 7, 12]:
    t = pathlib.Path(f'site/adbms/ch{n:02d}.html').read_text(encoding='utf-8')
    has_box = 'Memory device' in t
    has_link = 'href="mem.html"' in t
    has_narr = ('ch19' in t) if n == 4 else ('ch20' in t if n == 7 else True)
    print(n, 'box:', has_box, 'memlink:', has_link, 'narrlink:', has_narr)
