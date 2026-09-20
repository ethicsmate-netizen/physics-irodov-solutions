import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

questions = json.load(open('data/questions_seed.json', encoding='utf-8'))
qmap = {q['id']: q for q in questions}

print(f"Total questions in database: {len(questions)}")

missing_ids = []
low_hints = []
missing_answers = []
total_ch1 = 0

for i in range(1, 389):
    qid = f"1.{i}"
    if qid not in qmap:
        missing_ids.append(qid)
        continue
    total_ch1 += 1
    q = qmap[qid]
    if len(q.get('hints', [])) < 2:
        low_hints.append(qid)
    ans = q.get('answer', '')
    if not ans or 'MISSING' in ans or len(ans) < 3:
        missing_answers.append((qid, ans))

print(f"Chapter 1 problems found: {total_ch1} / 388")
print(f"Missing IDs: {len(missing_ids)}")
if missing_ids:
    print(missing_ids[:10])

print(f"Problems with fewer than 2 hints: {len(low_hints)}")
if low_hints:
    print(low_hints[:10])

print(f"Problems with missing/blank answers: {len(missing_answers)}")
if missing_answers:
    print(missing_answers[:10])

print("\nSample Chapter 1 problems verification:")
for check_id in ["1.1", "1.58", "1.59", "1.117", "1.118", "1.199", "1.200", "1.233", "1.234", "1.289", "1.290", "1.314", "1.315", "1.339", "1.340", "1.388"]:
    if check_id in qmap:
        q = qmap[check_id]
        print(f"[{check_id}] {q['title']}")
        print(f"   Answer: {q['answer'][:80]}")
        print(f"   Hints count: {len(q['hints'])}, Solution length: {len(q['solution'])} chars")
