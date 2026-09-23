import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

txt = (BASE_DIR / "data" / "clean_raw_answers_part2.txt").read_text(encoding="utf-8")

lines = txt.split('\n')
parsed = {}
cur_lines = []
active_num = None

for line in lines:
    # Match any line starting with a number followed by '.'
    m = re.match(r'^\s*(\d{1,3})\.\s*(.*)', line)
    if m:
        num = int(m.group(1))
        # Ensure it's a valid sequential progression (between 1 and 257)
        if 1 <= num <= 257 and (active_num is None or 0 < num - active_num <= 4):
            if active_num is not None:
                parsed[active_num] = '\n'.join(cur_lines).strip()
            active_num = num
            cur_lines = [m.group(2)]
            continue
    if active_num is not None:
        cur_lines.append(line)

if active_num is not None:
    parsed[active_num] = '\n'.join(cur_lines).strip()

print(f"Sequentially parsed: {len(parsed)} questions")
for i in range(1, 15):
    print(f"{i}: {repr(parsed.get(i, 'MISSING')[:70])}")

missing = [n for n in range(1, 258) if n not in parsed]
print(f"Missing numbers in Part 2: {missing}")
