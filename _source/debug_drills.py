import re, pathlib
dt = pathlib.Path('exam/notes/classification-drills.md').read_text(encoding='utf-8')
dparts = re.split(r'(?m)^## Drill (\d+)', dt)
for i in range(1, len(dparts), 2):
    dn = int(dparts[i]); sec = dparts[i + 1]
    lines = sec.splitlines()
    rows = [ln for ln in lines if ln.lstrip().startswith('|') and not re.match(r'^\s*\|[\s:\-|]*\|\s*$', ln)]
    ans_m = re.search(r'\*\*Answers:\*\*\s*(.+)', sec)
    print('drill', dn, 'table-lines:', len(rows), 'has-answers:', bool(ans_m))
    if ans_m:
        print('   ans:', ans_m.group(1)[:100])
