import sys
import json
from pathlib import Path
from test_sequential_parser import parsed

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "data" / "part2.json", "r", encoding="utf-8") as f:
    p2 = json.load(f)

p2_map = {q["id"]: q for q in p2}

for n in range(26, 62):
    qid = f"2.{n}"
    q = p2_map.get(qid, {})
    ans = parsed.get(n, "MISSING")
    print(f"\n==================== Problem {qid} ====================")
    print("STMT:", q.get("statement")[:150].replace('\n', ' '))
    print("RAW ANS:", repr(ans))
