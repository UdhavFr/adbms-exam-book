import re, pathlib
t = pathlib.Path('site/adbms/index.html').read_text(encoding='utf-8')
for m in re.finditer(r'<h2><span class="n">([^<]+)</span>([^<]+)</h2>', t):
    cards = re.findall(r'id="(ch\d+)"', t[m.start():m.start() + 4000].split('</section>')[0])
    print(m.group(1), '|', m.group(2), '| cards:', cards)
