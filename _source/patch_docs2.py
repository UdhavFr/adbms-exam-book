import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')

# STE metric store (place near STE_SWAPS)
anchor = 'STE_PROT = '
assert anchor in t
t = t.replace(anchor, 'STE_PAIRS = []  # (before, after) html samples for the compliance metric\n' + anchor, 1)

old_loop = "html_body = '<div class=\"content\">\\n' + unstash(blocks(lesson_refs(body).splitlines())) + '\\n</div>'"
assert old_loop in t, 'lesson loop not found'
new_loop = ("_raw = '<div class=\"content\">\\n' + unstash(blocks(lesson_refs(body).splitlines())) + '\\n</div>'\n"
            "    STE_PAIRS.append([_raw, None])\n"
            "    html_body = ste_page(_raw)\n"
            "    STE_PAIRS[-1][1] = html_body")
t = t.replace(old_loop, new_loop, 1)
p.write_text(t, encoding='utf-8')
print('lesson loop wired')
