import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

qs = json.load(open(BASE_DIR / "data" / "questions_seed.json", encoding="utf-8"))

print("Testing Chapter 1.1 questions (1.1 to 1.58):")
for q in qs[:58]:
    # Check if there are any issues in question, answer, solution
    pass

# Print a few random questions from 1.1 to 1.58
for i in [5, 12, 25, 35, 45, 55]:
    q = qs[i]
    print(f"\n--- [{q['id']}] {q['title']} ---")
    print("STMT:", q['statement'][:150])
    print("ANS: ", q['answer'])
