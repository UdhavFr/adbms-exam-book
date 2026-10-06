import re, pathlib
t = pathlib.Path('site/adbms/ch01.html').read_text(encoding='utf-8')
for m in re.finditer(r'<details class="ref">.*?</details>', t, re.S):
    s = m.group(0)
    print('SUMMARY:', re.search(r'<summary>(.*?)</summary>', s, re.S).group(1)[:110])
    print('  tables:', s.count('<table'), '| escaped tags:', s.count('&lt;'), '| chars:', len(s))
t4 = pathlib.Path('site/adbms/ch04.html').read_text(encoding='utf-8')
for m in re.finditer(r'<details class="ref">.*?</details>', t4, re.S):
    s = m.group(0)
    print('CH04 SUMMARY:', re.search(r'<summary>(.*?)</summary>', s, re.S).group(1)[:110])
