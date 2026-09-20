import re
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

text = open(BASE_DIR / "data" / "raw_answers_part1.txt", encoding='utf-8').read()

pattern = re.compile(r'(\d+)\.\s+([\s\S]*?)(?=(?:\n\s*\d+\.|\n\s*Answers|\n--- Page|\Z))')
matches = pattern.findall(text)
answers = {}
for m in matches:
    num = m[0]
    ans = m[1].strip()
    if num not in answers:
        answers[num] = " ".join(ans.split())

# Check 1.200 to 1.289
with open(BASE_DIR / "data" / "ch1_4_5_raw_answers.txt", "w", encoding="utf-8") as f:
    for i in range(200, 290):
        ans = answers.get(str(i), "MISSING")
        f.write(f"[{i}]: {ans}\n")

print(f"Extracted raw answers for 1.200 to 1.289.")
