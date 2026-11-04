#!/usr/bin/env python3
# Checks that PlantUML preview images match the PlantUML text in index.html.
# Usage: python3 check-puml-preview.py [--update]
import hashlib, html, pathlib, re, sys
src = pathlib.Path('index.html').read_text(encoding='utf-8')
sha = lambda b: hashlib.sha256(b).hexdigest()
lock = {}
lp = pathlib.Path('puml-preview.lock')
if lp.exists():
    for line in lp.read_text().split('\n'):
        if line.strip():
            d, ph, ih = line.split()
            lock[d] = (ph, ih)
bad = 0
for dom, code_id, img in [('forest', 'puml-src', 'puml-forest.svg'), ('bank', 'puml-src-bank', 'puml-bank.svg')]:
    m = re.search(r'<code id="%s"[^>]*>(.*?)</code>' % code_id, src, re.S)
    ph = sha(html.unescape(m.group(1)).encode())
    ip = pathlib.Path(img)
    ih = sha(ip.read_bytes()) if ip.exists() else '-'
    old = lock.get(dom)
    if old is None:
        print(f'{dom}: немає запису в lock'); bad += 1
    elif ph != old[0] and ih == old[1]:
        print(f'{dom}: STALE, текст PlantUML змінився, картинку не перегенеровано'); bad += 1
    elif ph == old[0] and ih != old[1]:
        print(f'{dom}: УВАГА, картинка змінилась без зміни тексту'); bad += 1
    elif ph != old[0] and ih != old[1]:
        print(f'{dom}: перерендерено, оновіть lock (--update)')
        bad += 1
    else:
        print(f'{dom}: ok')
    lock[dom] = (ph, ih)
if '--update' in sys.argv:
    lp.write_text(''.join(f'{d} {v[0]} {v[1]}\n' for d, v in lock.items()))
    print('lock оновлено')
sys.exit(1 if bad and '--update' not in sys.argv else 0)
