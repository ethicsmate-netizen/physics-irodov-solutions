import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

part_counts = {
    1: 388,
    2: 257,
    3: 398,
    4: 238,
    5: 275,
    6: 310
}

def parse_part(part_num, total):
    fn = BASE_DIR / "data" / f"clean_raw_answers_part{part_num}.txt"
    txt = fn.read_text(encoding="utf-8")
    lines = txt.split('\n')
    parsed = {}
    cur_lines = []
    active_num = None

    for line in lines:
        m = re.match(r'^\s*(\d{1,3})\.\s*(.*)', line)
        if m:
            num = int(m.group(1))
            if 1 <= num <= total and (active_num is None or 0 < num - active_num <= 4):
                if active_num is not None:
                    parsed[active_num] = '\n'.join(cur_lines).strip()
                active_num = num
                cur_lines = [m.group(2)]
                continue
        if active_num is not None:
            cur_lines.append(line)

    if active_num is not None:
        parsed[active_num] = '\n'.join(cur_lines).strip()

    missing = [n for n in range(1, total + 1) if n not in parsed]
    print(f"Part {part_num} (expected {total}): parsed {len(parsed)}, missing {len(missing)} {missing[:10]}")
    return parsed

for p, tot in part_counts.items():
    parse_part(p, tot)
