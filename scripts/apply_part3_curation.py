"""
apply_part3_curation.py
Merge all 17 curated modules of Part 3 (Electrodynamics, 3.1 to 3.398, 398 problems)
into data/questions_seed.json, data/part3.json, and data/irodov.db.
"""

import json
import sqlite3
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

# Import all Part 3 curated modules
from part3_ch3_1a import CH3_1A_CURATED
from part3_ch3_1b import CH3_1B_CURATED
from part3_ch3_2a import CH3_2A_CURATED
from part3_ch3_2b import CH3_2B_CURATED
from part3_ch3_3a import CH3_3A_CURATED
from part3_ch3_3b import CH3_3B_CURATED
from part3_ch3_4a import CH3_4A_CURATED
from part3_ch3_4b import CH3_4B_CURATED
from part3_ch3_4c import CH3_4C_CURATED
from part3_ch3_5a import CH3_5A_CURATED
from part3_ch3_5b import CH3_5B_CURATED
from part3_ch3_5c import CH3_5C_CURATED
from part3_ch3_6a import CH3_6A_CURATED
from part3_ch3_6b import CH3_6B_CURATED
from part3_ch3_6c import CH3_6C_CURATED
from part3_ch3_6d import CH3_6D_CURATED
from part3_ch3_7 import CH3_7_CURATED

CHAPTER_METADATA = {
    "3.1": "Constant Electric Field in Vacuum",
    "3.2": "Conductors and Dielectrics in an Electric Field",
    "3.3": "Electric Capacitance. Energy of an Electric Field",
    "3.4": "Electric Current",
    "3.5": "Constant Magnetic Field. Magnetics",
    "3.6": "Electromagnetic Induction. Maxwell's Equations",
    "3.7": "Motion of Charged Particles in Electric and Magnetic Fields"
}

batches = [
    ("3.1", CH3_1A_CURATED),
    ("3.1", CH3_1B_CURATED),
    ("3.2", CH3_2A_CURATED),
    ("3.2", CH3_2B_CURATED),
    ("3.3", CH3_3A_CURATED),
    ("3.3", CH3_3B_CURATED),
    ("3.4", CH3_4A_CURATED),
    ("3.4", CH3_4B_CURATED),
    ("3.4", CH3_4C_CURATED),
    ("3.5", CH3_5A_CURATED),
    ("3.5", CH3_5B_CURATED),
    ("3.5", CH3_5C_CURATED),
    ("3.6", CH3_6A_CURATED),
    ("3.6", CH3_6B_CURATED),
    ("3.6", CH3_6C_CURATED),
    ("3.6", CH3_6D_CURATED),
    ("3.7", CH3_7_CURATED),
]

curated_map = {}
for ch_id, batch in batches:
    ch_title = CHAPTER_METADATA[ch_id]
    for item in batch:
        item['chapter_id'] = ch_id
        item['chapter_title'] = ch_title
        item['part_id'] = 3
        item['part_title'] = "Electrodynamics"
        curated_map[item['id']] = item

print(f"Total curated Part 3 problems loaded: {len(curated_map)} (expected 398)")
assert len(curated_map) == 398, f"Expected 398 problems, got {len(curated_map)}"

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
        q['question'] = c['question']
        q['difficulty'] = c.get('difficulty', q.get('difficulty', 2))
        q['hints'] = c.get('hints', [])
        q['answer'] = c['answer']
        q['final_answer'] = c['answer']
        q['solution'] = c['solution']
        q['tags'] = c.get('tags', q.get('tags', []))
        q['chapter_id'] = c['chapter_id']
        q['chapter_title'] = c['chapter_title']
        q['part_id'] = 3
        q['part_title'] = "Electrodynamics"
        updated_count += 1

print(f"Updated {updated_count} questions in questions_seed.json.")
with open(seed_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
print("Saved data/questions_seed.json.")

# 2. Update data/part3.json
part3_path = BASE_DIR / "data" / "part3.json"
part3_list = []
for i in range(1, 399):
    qid = f"3.{i}"
    c = curated_map[qid]
    part3_list.append({
        "id": qid,
        "title": c.get("title", f"Problem {qid}"),
        "part_id": 3,
        "part_title": "Electrodynamics",
        "chapter_id": c["chapter_id"],
        "chapter_title": c["chapter_title"],
        "statement": c["question"],
        "question": c["question"],
        "difficulty": c.get("difficulty", 2),
        "hints": c.get("hints", []),
        "answer": c["answer"],
        "final_answer": c["answer"],
        "solution": c["solution"],
        "tags": c.get("tags", [])
    })

with open(part3_path, "w", encoding="utf-8") as f:
    json.dump(part3_list, f, ensure_ascii=False, indent=2)
print(f"Wrote {len(part3_list)} questions to data/part3.json.")

# 3. Reseed SQLite database
db_path = BASE_DIR / "data" / "irodov.db"
conn = sqlite3.connect(str(db_path))
cursor = conn.cursor()

db_updated = 0
for qid, c in curated_map.items():
    cursor.execute("""
        UPDATE questions
        SET statement = ?,
            difficulty = ?,
            hints = ?,
            answer = ?,
            solution = ?,
            tags = ?,
            chapter_id = ?,
            chapter_title = ?,
            part_id = 3,
            part_title = 'Electrodynamics'
        WHERE id = ?
    """, (
        c["question"],
        c.get("difficulty", 2),
        json.dumps(c.get("hints", []), ensure_ascii=False),
        c["answer"],
        c["solution"],
        json.dumps(c.get("tags", []), ensure_ascii=False),
        c["chapter_id"],
        c["chapter_title"],
        qid
    ))
    db_updated += cursor.rowcount

conn.commit()
conn.close()
print(f"Updated {db_updated} rows in data/irodov.db.")
print("Part 3 curation applied successfully!")
