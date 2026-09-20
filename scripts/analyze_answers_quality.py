import json
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

qs = json.load(open(BASE_DIR / "data" / "questions_seed.json", encoding="utf-8"))

placeholders = []
clean_curated = []
mangled_ocr = []

for q in qs:
    ans = q.get('answer', '')
    if any(p in ans.lower() for p in ['refer to', 'see analytical', 'analytical derivation']):
        placeholders.append(q['id'])
    elif q['id'].startswith('1.') and int(q['id'].split('.')[1]) <= 58:
        clean_curated.append(q['id'])
    else:
        mangled_ocr.append(q['id'])

print(f"Total problems: {len(qs)}")
print(f"Clean curated answers (1.1 - 1.58): {len(clean_curated)}")
print(f"Placeholder answers: {len(placeholders)}")
print(f"Mangled OCR answers: {len(mangled_ocr)}")

print("\nSample 10 mangled OCR answers:")
for qid in mangled_ocr[::len(mangled_ocr)//10][:10]:
    q = next(item for item in qs if item['id'] == qid)
    print(f"[{qid}] {repr(q['answer'])}")
