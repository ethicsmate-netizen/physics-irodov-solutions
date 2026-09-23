import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

for i in range(1, 7):
    fn = BASE_DIR / "data" / (f"part{i}.json" if i > 1 else "part1_rest.json")
    try:
        with open(fn, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Part {i}: {len(data)} questions, first ID={data[0]['id']}, last ID={data[-1]['id']}")
    except Exception as e:
        print(f"Part {i}: {e}")

# Also check questions_seed.json
seed_fn = BASE_DIR / "data" / "questions_seed.json"
with open(seed_fn, 'r', encoding='utf-8') as f:
    seed = json.load(f)
print(f"\nTotal in questions_seed.json: {len(seed)} questions, first ID={seed[0]['id']}, last ID={seed[-1]['id']}")
