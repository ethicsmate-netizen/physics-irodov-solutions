import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/part5.json', 'r', encoding='utf-8') as f:
    p5 = json.load(f)

for p in p5[96:126]:
    print(f"*** {p['id']} ***")
    print("Statement:", repr(p.get('statement', ''))[:120])
    print("Answer:", repr(p.get('answer', ''))[:120])
    print()
