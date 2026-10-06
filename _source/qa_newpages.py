import pathlib
t = pathlib.Path('site/adbms/index.html').read_text(encoding='utf-8')
for f in ['voices.html', 'wms.html', 'test.html', 'plan.html']:
    print(f, 'linked:', f'href="{f}"' in t)
for f in ['voices.html', 'wms.html', 'test.html']:
    h = pathlib.Path('site/adbms/' + f).read_text(encoding='utf-8')
    print(f, 'bytes:', len(h), '| has content:', 'class="content"' in h)
