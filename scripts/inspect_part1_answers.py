import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

p1 = json.load(open(BASE_DIR / "data" / "part1_rest.json", encoding="utf-8"))
print(f"Total problems in part1_rest: {len(p1)}")
for q in p1[:10]:
    print(f"[{q['id']}] ANS: {repr(q.get('answer'))}")
