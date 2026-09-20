import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

qs = json.load(open(BASE_DIR / "data" / "questions_seed.json", encoding="utf-8"))

with_dollar = [q for q in qs if '$' in q.get('statement', '') or '$' in q.get('answer', '') or '$' in q.get('solution', '')]
with_backslash = [q for q in qs if '\\' in q.get('statement', '') or '\\' in q.get('answer', '') or '\\' in q.get('solution', '')]

print(f"Total questions with '$': {len(with_dollar)}")
print(f"Total questions with '\\': {len(with_backslash)}")

# Print sample of questions with '$'
print("\nSamples of questions with '$':")
for q in with_dollar[:10]:
    print(f"[{q['id']}] statement has $: {'$' in q['statement']}, solution has $: {'$' in q['solution']}")

# Print sample of questions without '$'
print("\nSamples of questions WITHOUT '$':")
no_dollar = [q for q in qs if '$' not in q.get('statement', '') and '$' not in q.get('solution', '')]
print(f"Total questions WITHOUT '$': {len(no_dollar)}")
for q in no_dollar[:5]:
    print(f"[{q['id']}] {q['statement'][:80]}")
