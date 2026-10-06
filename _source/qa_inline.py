import re, pathlib, subprocess, tempfile, os
for page in ['site/adbms/ch19/index.html', 'site/adbms/ch20/index.html', 'site/adbms/ch21/index.html', 'site/adbms/ch22/index.html', 'site/adbms/ch23/index.html', 'site/adbms/ch24/index.html', 'site/adbms/ch25/index.html']:
    h = pathlib.Path(page).read_text(encoding='utf-8')
    scripts = re.findall(r'<script>(.*?)</script>', h, re.S)
    hit = False
    for s in scripts:
        if 'BEATS' not in s or 'Narrate.init' not in s:
            continue
        hit = True
    # stub browser/engine globals so we canaje parse only: use node --check
    with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
        f.write(s)
        name = f.name
    r = subprocess.run(['node', '--check', name], capture_output=True, text=True)
    print(page, 'BEATS script syntax:', 'OK' if r.returncode == 0 else 'FAIL\n' + r.stderr)
    os.unlink(name)
    if not hit:
        print(page, 'NO BEATS SCRIPT FOUND')
