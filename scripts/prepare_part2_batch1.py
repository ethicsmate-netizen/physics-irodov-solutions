import sys
import json
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "data" / "part2.json", "r", encoding="utf-8") as f:
    p2 = json.load(f)

p2_map = {q["id"]: q for q in p2}

raw_ans_txt = (BASE_DIR / "data" / "clean_raw_answers_part2.txt").read_text(encoding="utf-8")

# Parse raw answers
ans_blocks = re.split(r'(?:^|\n)\s*(\d+)\.\s*', raw_ans_txt)
answers = {}
for i in range(1, len(ans_blocks), 2):
    num = int(ans_blocks[i])
    content = ans_blocks[i+1].strip()
    # take up to next block boundary if any
    answers[num] = content.split('\n--- PDF Page')[0].strip()

print(f"Total answers extracted for Part 2: {len(answers)}")

# Inspect 2.1 to 2.61
batch1_info = []
for n in range(1, 62):
    qid = f"2.{n}"
    stmt = p2_map.get(qid, {}).get("statement", "")
    ans = answers.get(n, "NO_ANSWER_IN_PDF")
    batch1_info.append({
        "id": qid,
        "statement": stmt,
        "raw_answer": ans
    })

with open(BASE_DIR / "data" / "part2_batch1_raw.json", "w", encoding="utf-8") as f:
    json.dump(batch1_info, f, ensure_ascii=False, indent=2)

print(f"Saved {len(batch1_info)} questions to data/part2_batch1_raw.json")
for item in batch1_info[:5]:
    print(f"\n--- {item['id']} ---")
    print("STMT:", item["statement"])
    print("ANS:", item["raw_answer"])
