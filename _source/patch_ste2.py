import pathlib
p = pathlib.Path('_source/build_site.py')
lines = p.read_text(encoding='utf-8').splitlines(keepends=True)
for i, ln in enumerate(lines):
    if 'demonstrat' in ln and 'approximat' in ln and 'show' in ln:
        head = ln.split("'show'), ")[0] + "'show'),\n"
        lines[i] = head
        print('fixed line', i + 1, '->', repr(head[:80]))
        break
p.write_text(''.join(lines), encoding='utf-8')
