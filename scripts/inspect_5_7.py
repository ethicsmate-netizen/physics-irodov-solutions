import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/part5.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

p5_7 = [q for q in data if any(q['id'] == f'5.{i}' for i in range(246, 276))]
with open('scripts/inspect_5_7.txt', 'w', encoding='utf-8') as out:
    out.write(f'Found {len(p5_7)} problems\n')
    for q in p5_7:
        out.write(f'=== {q["id"]} ===\n')
        out.write(f'Q: {q["question"]}\n')
        out.write(f'A: {q["answer"]}\n\n')
