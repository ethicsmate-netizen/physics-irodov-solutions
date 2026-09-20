import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
p6_path = BASE_DIR / "data" / "part6.json"

with open(p6_path, "r", encoding="utf-8") as f:
    p6_data = json.load(f)

print(f"Original part6.json count: {len(p6_data)}")
# Keep only up to 6.310
filtered = [q for q in p6_data if int(q["id"].split(".")[1]) <= 310]
print(f"Trimmed part6.json count: {len(filtered)}")
print(f"Last problem is: {filtered[-1]['id']}: {filtered[-1]['question'][:60]}")

with open(p6_path, "w", encoding="utf-8") as f:
    json.dump(filtered, f, indent=2, ensure_ascii=False)

print("Saved clean part6.json!")
