import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

qs = json.load(open(BASE_DIR / "data" / "questions_seed.json", encoding="utf-8"))

for q in qs[:58]:
    # check for any strange patterns or errors
    stmt = q['statement']
    sol = q['solution']
    ans = q['answer']
    # check for unmatched $
    for name, text in [('statement', stmt), ('solution', sol), ('answer', ans)]:
        # count $
        c = text.count('$')
        if c % 2 != 0:
            print(f"[{q['id']}] ODD number of $ in {name}: {c}")
