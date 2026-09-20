import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

data = json.load(open(BASE_DIR / "data" / "questions_seed.json", encoding="utf-8"))
for q in data:
    if q['id'] in ['1.144', '1.157', '1.165', '1.177', '1.197']:
        print(f"*** [{q['id']}] ***")
        print("STMT:", q['statement'])
        print("ANS :", q.get('answer', ''))
        print()
