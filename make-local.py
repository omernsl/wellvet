#!/usr/bin/env python3
"""index.html (artifact kaynagi) -> local.html + docs/ (GitHub Pages icin yayin klasoru)."""
import shutil, pathlib
root = pathlib.Path(__file__).parent
src = (root/'index.html').read_text(encoding='utf-8')
head, body = src.split('</style>', 1)
doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head}</style>
</head>
<body>
{body.strip()}
</body>
</html>
"""
(root/'local.html').write_text(doc, encoding='utf-8')

# docs/: only what the public site needs — web previews, never originals
docs = root/'docs'
if docs.exists(): shutil.rmtree(docs)
(docs/'images'/'horse').mkdir(parents=True)
(docs/'index.html').write_text(doc, encoding='utf-8')
(docs/'.nojekyll').write_text('')
for f in (root/'images').glob('*.webp'):        shutil.copy2(f, docs/'images'/f.name)
for f in (root/'images'/'horse').glob('*.webp'): shutil.copy2(f, docs/'images'/'horse'/f.name)
(docs/'images'/'mockups').mkdir(parents=True)
for f in (root/'images'/'mockups').glob('*.webp'): shutil.copy2(f, docs/'images'/'mockups'/f.name)
n = sum(1 for _ in docs.rglob('*') if _.is_file())
print(f'local.html + docs/ yazildi ({len(doc)/1024:.0f} KB sayfa, docs icinde {n} dosya)')
