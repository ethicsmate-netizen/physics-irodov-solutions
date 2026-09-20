import json
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

start = int(sys.argv[1])
end = int(sys.argv[2])

q = json.load(open('data/questions_seed.json', encoding='utf-8'))
qmap = {x['id']: x for x in q}

for i in range(start, end + 1):
    qid = f"1.{i}"
    if qid in qmap:
        item = qmap[qid]
        print(f"=== {qid} ===")
        print(f"Title: {item.get('title', '')}")
        print(f"Statement: {item['statement']}")
        print(f"Answer: {item['answer']}")
        print()
