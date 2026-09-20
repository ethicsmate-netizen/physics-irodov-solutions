import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

text = open(BASE_DIR / "data" / "raw_answers_part1.txt", encoding='utf-8').read()

# Regex to find numbered answers
pattern = re.compile(r'(\d+)\.\s+([\s\S]*?)(?=(?:\n\s*\d+\.|\n\s*Answers|\n--- Page|\Z))')
matches = pattern.findall(text)
answers = {}
for m in matches:
    num = m[0]
    ans = m[1].strip()
    if num not in answers:
        answers[num] = ans

print(f"Total numbered answers extracted: {len(answers)}")

with open(BASE_DIR / "data" / "ch1_3_clean_raw_answers.txt", "w", encoding="utf-8") as f:
    for i in range(118, 200):
        ans = answers.get(str(i), "MISSING")
        ans_one_line = " ".join(ans.split())
        f.write(f"[{i}]: {ans_one_line}\n")
        print(f"[{i}]: {ans_one_line[:90]}")
