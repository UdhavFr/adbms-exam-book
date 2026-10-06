import re, pathlib
t = pathlib.Path('site/adbms/written.html').read_text(encoding='utf-8')
cards = re.findall(r'<div class="qcard written" id="(Q\d+)"', t)
print('cards:', len(cards))
print('Q84 present:', 'id="Q84"' in t, '| Q85 present:', 'id="Q85"' in t,
      '| Q88 present:', 'id="Q88"' in t, '| Q143 present:', 'id="Q143"' in t,
      '| Q150 present:', 'id="Q150"' in t)
i = t.find('id="Q84"')
print(t[i:i + 500].replace('\n', ' | '))
# lesson linkify check
l4 = pathlib.Path('site/adbms/ch04.html').read_text(encoding='utf-8')
print('ch04 written links:', len(re.findall(r'href="written\.html#Q\d+"', l4)),
      '| arena links:', len(re.findall(r'href="quiz\.html"', l4)))
