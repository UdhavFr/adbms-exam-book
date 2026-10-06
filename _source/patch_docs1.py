import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')

old_target = '''def md_target(ref):
    """Resolve a .md reference to a site-relative URL, or None if not found."""
    if re.fullmatch(r'mock-exam-(\\d)\\.md', ref):
        return f'mock{re.fullmatch(r"mock-exam-(\\d)\\.md", ref).group(1)}.html'
    cands = [EXAM / 'notes' / ref, EXAM / ref.lstrip('/')]
    if ref.startswith('notes/'):
        cands.insert(0, EXAM / ref)
    for p in cands:
        if p.is_file():
            return '../../exam/' + p.relative_to(EXAM).as_posix()
    return None'''

new_target = '''# .md reference -> nice site page (fall back to the raw .md file URL)
DOCS = {
    'memory-hooks.md': 'mem.html',
    'memorization-techniques.md': 'mem.html',
    'final-cram.md': 'cram.html',
    'ultra-short-notes.md': 'cram.html',
    'question-bank.md': 'written.html',
    'revision-plan.md': 'plan.html',
    'answer-voices.md': 'voices.html',
    'test-details.md': 'test.html',
    'write-memorize-skip.md': 'wms.html',
    'chapter-notes/unit-1.md': 'docs/unit-1.html',
    'chapter-notes/unit-2.md': 'docs/unit-2.html',
    'chapter-notes/unit-3.md': 'docs/unit-3.html',
    'chapter-notes/unit-4.md': 'docs/unit-4.html',
    'chapter-notes/unit-5.md': 'docs/unit-5.html',
    'diagrams-and-mental-models.md': 'docs/diagrams.html',
    'formulas.md': 'docs/formulas.html',
    'comparisons.md': 'docs/comparisons.html',
    'processes-and-algorithms.md': 'docs/processes.html',
    'common-mistakes.md': 'docs/mistakes.html',
    'definitions.md': 'docs/definitions.html',
    'answer-bank.md': 'docs/answers.html',
    'examples.md': 'docs/examples.html',
    'errata.md': 'docs/errata.html',
    'likely-questions.md': 'docs/likely.html',
    'flashcards.md': 'docs/cards.html',
    'weakness-tracker.md': 'docs/tracker.html',
    'master-study-guide.md': 'docs/guide.html',
    'learning-path-from-zero.md': 'docs/path.html',
}

def md_target(ref):
    """Resolve a .md reference to a site-relative URL (nice page preferred)."""
    m = re.fullmatch(r'mock-exam-(\\d)(?:-key)?\\.md', ref)
    if m:
        return f'mock{m.group(1)}.html'
    key = ref[6:] if ref.startswith('notes/') else ref
    if key in DOCS:
        return DOCS[key]
    cands = [EXAM / 'notes' / ref, EXAM / ref.lstrip('/')]
    if ref.startswith('notes/'):
        cands.insert(0, EXAM / ref)
    for p in cands:
        if p.is_file():
            return '../../exam/' + p.relative_to(EXAM).as_posix()
    return None'''

assert old_target in t, 'md_target block not found'
t = t.replace(old_target, new_target)
p.write_text(t, encoding='utf-8')
print('md_target rewired')
