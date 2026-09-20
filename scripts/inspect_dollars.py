import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

qs = json.load(open(BASE_DIR / "data" / "questions_seed.json", encoding="utf-8"))

for q in qs[58:70]:
    print(f"[{q['id']}]")
    if '$' in q['statement']:
        print("  STATEMENT $ matches:", re.findall(r'\$[^\$]+\$', q['statement']))
    if '$' in q['solution']:
        print("  SOLUTION $ matches:", re.findall(r'\$[^\$]+\$', q['solution']))
    if '$' in q['answer']:
        print("  ANSWER $ matches:", re.findall(r'\$[^\$]+\$', q['answer']))
