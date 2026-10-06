import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')

old = 'units_html.append(lib_section)'
assert old in t
t = t.replace(old, 'LIB_SECTION = lib_section', 1)

anchor = 'intro_html = blocks(intro_md.splitlines())'
assert anchor in t
t = t.replace(anchor, 'units_html.append(LIB_SECTION)\n' + anchor, 1)
p.write_text(t, encoding='utf-8')
print('lib ordering fixed')
