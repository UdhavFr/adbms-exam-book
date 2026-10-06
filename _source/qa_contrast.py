def lum(h):
    h = h.lstrip('#')
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def ratio(a, b):
    x, y = lum(a), lum(b)
    return (max(x, y) + 0.05) / (min(x, y) + 0.05)

board, panel = '#1d2b27', '#22322d'
for name, fg in [('chalk', '#ece8dc'), ('dim', '#9aaba3'), ('faint', '#5d7068'),
                 ('task', '#f0b45a'), ('quiz', '#86c9e8'), ('good', '#8fd6b0'), ('bad', '#f0979a')]:
    print(f'{name:6} on board: {ratio(fg, board):.2f} | on panel: {ratio(fg, panel):.2f}')
