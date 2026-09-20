import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

qs = json.load(open(BASE_DIR / "data" / "questions_seed.json", encoding="utf-8"))

samples = ["1.1", "1.10", "1.58", "1.59", "1.118", "2.1", "2.26", "3.1", "3.54", "4.1", "4.94", "5.1", "5.64", "6.1", "6.49", "6.167"]

for q in qs:
    if q["id"] in samples:
        print(f"================== {q['id']} ({q['chapter_title']}) ==================")
        print("STATEMENT:")
        print(q["statement"])
        print("\nANSWER:")
        print(q["answer"])
        print("\nSOLUTION (first 200 chars):")
        print(q["solution"][:200])
        print()
