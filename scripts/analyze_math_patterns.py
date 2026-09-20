import json
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

qs = json.load(open(BASE_DIR / "data" / "questions_seed.json", encoding="utf-8"))

print(f"Total questions: {len(qs)}")

# Sample questions with numbers, formulas, equals signs
math_statements = []
for q in qs[58:]:
    stmt = q['statement']
    if any(sym in stmt for sym in ['=', '≈', '∆', 'µ', 'α', 'β', 'γ', 'ω', 'λ', 'ρ', 'σ', 'τ', 'φ', 'θ', 'π', 'ε', 'η', 'ν', '^', '°']):
        math_statements.append(q)

print(f"Total questions outside Ch 1.1 containing math symbols: {len(math_statements)} out of {len(qs)-58}")

print("\nSample 25 math statements and their answers:")
for q in math_statements[::len(math_statements)//25][:25]:
    print(f"--- [{q['id']}] ---")
    print("STMT:", q['statement'][:160])
    print("ANS: ", q['answer'][:120])
