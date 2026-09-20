import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

qs = json.load(open(BASE_DIR / "data" / "questions_seed.json", encoding="utf-8"))

odd_count = 0
for q in qs:
    for name in ['statement', 'answer', 'solution']:
        text = q.get(name, '')
        # Count non-escaped $
        # In MathRenderer, block math is $$...$$, inline math is $...$
        # Let's count $
        c = text.count('$')
        if c % 2 != 0:
            odd_count += 1
            if odd_count <= 20:
                print(f"[{q['id']}] ODD '$' in {name}: count={c}")
                print(f"   TEXT: {repr(text[:150])}")

print(f"\nTotal questions with odd '$': {odd_count}")
