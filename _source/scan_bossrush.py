import re, pathlib
h = pathlib.Path(r'claude\ADBMS Boss Rush.html').read_text(encoding='utf-8', errors='replace')
mods = re.findall(r"n:'([^']+)'", h)
print('modules:', mods)
qitems = re.findall(r"\['([^']{5,200})',\s*\[", h)
print('questions found:', len(qitems))
for q in qitems:
    print(' -', q[:110])
