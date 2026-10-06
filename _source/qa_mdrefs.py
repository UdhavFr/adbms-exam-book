import re, pathlib
d = pathlib.Path('site/adbms')
for p in sorted(d.rglob('*.html')):
    t = p.read_text(encoding='utf-8')
    # strip script contents to avoid JS false positives
    t2 = re.sub(r'<script>.*?</script>', '', t, flags=re.S)
    refs = re.findall(r'[\w./-]*[\w-]+\.md(?:\s*[§#][\w.–-]+)?', t2)
    refs = [r for r in refs if 'href' not in r and '.md' in r]
    if refs:
        print(p.relative_to(d), '->', sorted(set(refs))[:12])
