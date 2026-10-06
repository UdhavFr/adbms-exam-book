import pathlib, re
t = pathlib.Path('site/adbms/drills.html').read_text(encoding='utf-8')
sels = re.findall(r'<select data-ans="([^"]+)"[^>]*>(.*?)</select>', t, re.S)
print('selects:', len(sels))
bad = 0
for ans, inner in sels:
    opts = re.findall(r'<option value="([^"]+)">', inner)[1:]
    if ans not in opts:
        bad += 1
        print('MISMATCH:', ans)
print('mismatches:', bad)
print('aria-labels:', len(re.findall(r'aria-label="Bucket', t)))
print('noscript:', '<noscript>' in t)
