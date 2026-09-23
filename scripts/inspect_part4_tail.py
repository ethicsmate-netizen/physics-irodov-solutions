import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/questions_seed.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

for q in qs:
    if q['id'].startswith('4.') and 214 <= int(q['id'].split('.')[1]) <= 224:
        print(f"*** {q['id']} ***")
        print("Statement:", q['statement'])
        print("Answer:", q.get('answer'))
        print()
