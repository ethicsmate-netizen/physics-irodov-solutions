"""
apply_ch1_4_curation.py
Merge Chapter 1.4 curated batch (1.200 to 1.233) into data/questions_seed.json and data/irodov.db.
"""

import json
import sqlite3
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

# Import Chapter 1.4
from ch1_4_curated import CH1_4_CURATED

curated_map = {item['id']: item for item in CH1_4_CURATED}
print(f"Loaded {len(curated_map)} curated Chapter 1.4 questions (1.200 to 1.233).")

# 1. Update questions_seed.json
seed_path = BASE_DIR / "data" / "questions_seed.json"
with open(seed_path, "r", encoding="utf-8") as f:
    questions = json.load(f)

updated_count = 0
for q in questions:
    qid = q['id']
    if qid in curated_map:
        c = curated_map[qid]
        q['title'] = c.get('title', q.get('title', f"Problem {qid}"))
        q['statement'] = c['question']
        q['difficulty'] = c.get('difficulty', q.get('difficulty', 2))
        q['hints'] = c.get('hints', [])
        q['answer'] = c['answer']
        q['solution'] = c['solution']
        q['tags'] = c.get('tags', q.get('tags', []))
        updated_count += 1

print(f"Updated {updated_count} questions in questions_seed.json.")

with open(seed_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

# 2. Update part1_rest.json
part1_path = BASE_DIR / "data" / "part1_rest.json"
if part1_path.exists():
    with open(part1_path, "r", encoding="utf-8") as f:
        part1_data = json.load(f)
    p1_updated = 0
    for q in part1_data:
        qid = q['id']
        if qid in curated_map:
            c = curated_map[qid]
            q['title'] = c.get('title', q.get('title', f"Problem {qid}"))
            q['statement'] = c['question']
            q['difficulty'] = c.get('difficulty', q.get('difficulty', 2))
            q['hints'] = c.get('hints', [])
            q['answer'] = c['answer']
            q['solution'] = c['solution']
            q['tags'] = c.get('tags', q.get('tags', []))
            p1_updated += 1
    with open(part1_path, "w", encoding="utf-8") as f:
        json.dump(part1_data, f, ensure_ascii=False, indent=2)
    print(f"Updated {p1_updated} questions in part1_rest.json.")

# 3. Resync SQLite DB using backend.db.init_db
sys.path.insert(0, str(BASE_DIR))
from backend.db import init_db

init_db(force_reseed=True)
print("Resynced irodov.db via backend.db.init_db(force_reseed=True).")
print("Chapter 1.4 curation successfully applied!")
