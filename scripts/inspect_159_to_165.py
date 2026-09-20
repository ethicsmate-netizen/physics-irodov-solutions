import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

qs = json.load(open(BASE_DIR / "data" / "questions_seed.json", encoding="utf-8"))

for q in qs[58:65]:
    print(f"==================== [{q['id']}] ====================")
    print("STMT:", q['statement'])
    print("ANS: ", q['answer'])
    print("SOL: ", q['solution'])
    print()
