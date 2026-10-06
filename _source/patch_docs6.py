import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')
old = '    return f"""<!doctype html>'
assert old in t
t = t.replace(old, '    page = f"""<!doctype html>', 1)
p.write_text(t, encoding='utf-8')
print('chrome return fixed')
