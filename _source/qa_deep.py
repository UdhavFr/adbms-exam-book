import re, pathlib

d = pathlib.Path('site/adbms').resolve()
pages = [p for p in d.rglob('*.html')]
print('pages:', len(pages))
issues = []

for p in pages:
    rel = p.relative_to(d).as_posix()
    t = p.read_text(encoding='utf-8')
    # 1. progress total consistency
    totals = set(re.findall(r'initContents\((\d+)\)', t))
    if totals and totals != {'25'}:
        issues.append(f'{rel}: initContents totals {totals} (expect 25)')
    # 2. placeholders
    for bad in ['TODO', 'FIXME', 'lorem', 'XXX', 'TBD']:
        if bad.lower() in t.lower():
            issues.append(f'{rel}: placeholder {bad}')
    # 3. duplicate ids
    ids = re.findall(r'id="([^"]+)"', t)
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        issues.append(f'{rel}: duplicate ids {dupes}')
    # 4. raw & not an entity (heuristic: & followed by space or end, or &< )
    raws = re.findall(r'&(?!amp;|lt;|gt;|quot;|#\d+;|#[xX][0-9a-fA-F]+;|nbsp;|→|✗|✓|★|⚡|⏩|▶|⏸|←|→|✍|·)[\s<]', t)
    if raws:
        issues.append(f'{rel}: possible raw & ({len(raws)}x)')
    # 5. noscript fallback
    if '<noscript>' not in t:
        issues.append(f'{rel}: no <noscript> fallback')
    # 6. selects without accessible label
    for m in re.finditer(r'<select(?![^>]*aria-label)(?![^>]*id="voicelist")[^>]*>', t):
        issues.append(f'{rel}: select without aria-label')
    # 7. title present
    if '<title>' not in t:
        issues.append(f'{rel}: no <title>')

print('ISSUES:', len(issues))
for i in issues:
    print(' -', i)
