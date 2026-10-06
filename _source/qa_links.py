import re, pathlib
d = pathlib.Path('site/adbms').resolve()
root = d.parents[1]
pages = [p for p in d.rglob('*.html')]
files = set(p.relative_to(d).as_posix() for p in pages)
assets = {'quizzes.js', 'app.js', 'style.css', 'narrate.js'}
missing = set()
for p in pages:
    t = p.read_text(encoding='utf-8')
    refs = re.findall(r'href="([^"]+)"', t) + re.findall(r'src="([^"]+)"', t)
    for h in refs:
        if h.startswith(('http', '#', 'data:')):
            continue
        base = h.split('#')[0]
        if not base:
            continue
        # resolve relative to the page's directory; may land in exam/ (md links)
        try:
            rel = (p.parent / base).resolve().relative_to(d).as_posix()
        except ValueError:
            try:
                (p.parent / base).resolve().relative_to(root)
            except ValueError:
                missing.add((p.relative_to(d).as_posix(), h))
                continue
            if not (p.parent / base).resolve().is_file():
                missing.add((p.relative_to(d).as_posix(), h))
            continue
        if rel not in files and rel not in assets:
            missing.add((p.relative_to(d).as_posix(), h))
print('missing links:', missing or 'NONE')
