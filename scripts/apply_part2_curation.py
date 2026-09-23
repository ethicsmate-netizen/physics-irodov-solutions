"""
apply_part2_curation.py
Merge all 7 curated chapters of Part 2 (Thermodynamics and Molecular Physics, 2.1 to 2.257, 257 problems)
into data/questions_seed.json, data/part2.json, and data/irodov.db.
"""

import json
import sqlite3
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

# Import all Part 2 curated chapters
from part2_ch2_1 import CH2_1_CURATED
from part2_ch2_2 import CH2_2_CURATED
from part2_ch2_3 import CH2_3_CURATED
from part2_ch2_4 import CH2_4_CURATED
from part2_ch2_5 import CH2_5_CURATED
from part2_ch2_6 import CH2_6_CURATED
from part2_ch2_7 import CH2_7_CURATED

CHAPTER_METADATA = {
    "2.1": "Equation of the Gas State. Processes",
    "2.2": "The First Law of Thermodynamics. Heat Capacity",
    "2.3": "Kinetic Theory of Gases. Boltzmann's Law and Maxwell's Distribution",
    "2.4": "The Second Law of Thermodynamics. Entropy",
    "2.5": "Liquids. Capillary Effects",
    "2.6": "Phase Transformations",
    "2.7": "Transport Phenomena"
}

batches = [
    ("2.1", CH2_1_CURATED),
    ("2.2", CH2_2_CURATED),
    ("2.3", CH2_3_CURATED),
    ("2.4", CH2_4_CURATED),
    ("2.5", CH2_5_CURATED),
    ("2.6", CH2_6_CURATED),
    ("2.7", CH2_7_CURATED),
]

curated_map = {}
for ch_id, batch in batches:
    ch_title = CHAPTER_METADATA[ch_id]
    for item in batch:
        item['chapter_id'] = ch_id
        item['chapter_title'] = ch_title
        item['part_id'] = 2
        item['part_title'] = "Thermodynamics and Molecular Physics"
        curated_map[item['id']] = item

print(f"Total curated Part 2 problems loaded: {len(curated_map)} (expected 257)")
assert len(curated_map) == 257, f"Expected 257 problems, got {len(curated_map)}"

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
        q['part_id'] = 2
        q['part_title'] = "Thermodynamics and Molecular Physics"
        updated_count += 1

print(f"Updated {updated_count} questions in questions_seed.json.")
assert updated_count == 257, f"Expected to update 257 questions in questions_seed.json, updated {updated_count}"

with open(seed_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

# 2. Update data/part2.json
part2_list = []
for i in range(1, 258):
    qid = f"2.{i}"
    c = curated_map[qid]
    part2_list.append({
        "id": qid,
        "title": c.get("title", f"Problem {qid}"),
        "statement": c["question"],
        "question": c["question"],
        "difficulty": c.get("difficulty", 2),
        "hints": c.get("hints", []),
        "answer": c["answer"],
        "final_answer": c["answer"],
        "solution": c["solution"],
        "tags": c.get("tags", []),
        "chapter_id": c["chapter_id"],
        "chapter_title": c["chapter_title"],
        "part_id": 2,
        "part_title": "Thermodynamics and Molecular Physics"
    })

part2_path = BASE_DIR / "data" / "part2.json"
with open(part2_path, "w", encoding="utf-8") as f:
    json.dump(part2_list, f, ensure_ascii=False, indent=2)
print(f"Wrote {len(part2_list)} questions to data/part2.json.")

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
            part_id = 2,
            part_title = 'Thermodynamics and Molecular Physics'
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
print("Part 2 curation applied successfully!")
