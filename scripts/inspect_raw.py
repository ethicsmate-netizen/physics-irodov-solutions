import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('../data/questions_seed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

lines = []
for q in data:
    qid = q['id']
    if qid.startswith('5.'):
        num = int(qid.split('.')[1])
        if 224 <= num <= 245:
            lines.append(f"=== {qid} ===")
            lines.append(f"T: {q.get('title', '')}")
            lines.append(f"Q: {q['question']}")
            lines.append(f"A: {q.get('answer', '')}")
            lines.append("")

with open('inspect_out_ch5_6.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

