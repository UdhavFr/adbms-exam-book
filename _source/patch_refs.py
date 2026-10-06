import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')
subs = [
("""        if any(s is None for s in secs) or len(keys) > 5:
            return md_link(ref_file)""",
"""        if any(s is None for s in secs) or len(keys) > 5:
            return stash_inline(md_link(ref_file))"""),
("""        if len(html) > EMBED_LIMIT * len(keys):
            return md_link(ref_file)
        return refbox(""",
"""        if len(html) > EMBED_LIMIT * len(keys):
            return stash_inline(md_link(ref_file))
        return stash(refbox("""),
("""        if s is None:
            return md_link(ref_file)
        html = blocks(s.splitlines())
        if len(html) > EMBED_LIMIT:
            return md_link(ref_file)
        return refbox(""",
"""        if s is None:
            return stash_inline(md_link(ref_file))
        html = blocks(s.splitlines())
        if len(html) > EMBED_LIMIT:
            return stash_inline(md_link(ref_file))
        return stash(refbox("""),
("""        if one_:
            return chapters(m.group(1), one_.group(1), one_.group(2))
        return md_link(m.group(1))""",
"""        if one_:
            return chapters(m.group(1), one_.group(1), one_.group(2))
        return stash_inline(md_link(m.group(1)))"""),
("""        if any(s is None for s in secs):
            return md_link(ref_file)
        html = blocks('\\n'.join(secs).splitlines())
        if len(html) > EMBED_LIMIT:
            return md_link(ref_file)
        return refbox(""",
"""        if any(s is None for s in secs):
            return stash_inline(md_link(ref_file))
        html = blocks('\\n'.join(secs).splitlines())
        if len(html) > EMBED_LIMIT:
            return stash_inline(md_link(ref_file))
        return stash(refbox("""),
("""    text = re.sub(r'`(processes-and-algorithms\\.md)`\\s*(P\\d+)\\s*[→–-]\\s*P\\d+',
                  lambda m: md_link(m.group(1)), text)""",
"""    text = re.sub(r'`(processes-and-algorithms\\.md)`\\s*(P\\d+)\\s*[→–-]\\s*P\\d+',
                  lambda m: stash_inline(md_link(m.group(1))), text)"""),
]
for old, new in subs:
    assert old in t, 'NOT FOUND: ' + old[:60]
    t = t.replace(old, new)
p.write_text(t, encoding='utf-8')
print('patched all', len(subs))
