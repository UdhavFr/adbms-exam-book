import re, pathlib
t = pathlib.Path('exam/notes/question-bank.md').read_text(encoding='utf-8')
wblocks = re.split(r'(?m)^## (UNIT \d|MIXED / CROSS-UNIT TRAPS|SECTION J.*)$', t)
print('blocks:', len(wblocks))
found = []
pat = (r"^\*\*Q(\d+)\*\* \[([^·\]]+)·\s*([^·\]]+)·\s*([^·\]]+)·\s*([^\]]+)\]\s*(.+?)"
       r"\n- Expected:\s*(.+?)\n- Keywords:\s*(.+?)\n- Common wrong:\s*(.+?)(?=\n\n|\n\*\*Q|\Z)")
for i in range(1, len(wblocks), 2):
    sec = wblocks[i]
    ms = list(re.finditer(pat, wblocks[i + 1], re.M | re.S))
    ids = [int(m.group(1)) for m in ms]
    print(repr(sec[:40]), '->', len(ms), 'first:', ids[:2] if ids else None, 'last:', ids[-2:] if ids else None)
    found += ids
expect = set(list(range(1, 89)) + list(range(143, 151)))
print('MISSING:', sorted(expect - set(found)))
