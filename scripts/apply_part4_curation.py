"""
apply_part4_curation.py
Merge all 10 curated modules of Part 4 (Oscillations and Waves, 4.1 to 4.238, 238 problems)
into data/questions_seed.json, data/part4.json, and data/irodov.db.
"""

import json
import sqlite3
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

# Import all Part 4 curated modules
from part4_ch4_1a import CH4_1A_CURATED
from part4_ch4_1b import CH4_1B_CURATED
from part4_ch4_1c import CH4_1C_CURATED
from part4_ch4_1d import CH4_1D_CURATED
from part4_ch4_2a import CH4_2A_CURATED
from part4_ch4_2b import CH4_2B_CURATED
from part4_ch4_3a import CH4_3A_CURATED
from part4_ch4_3b import CH4_3B_CURATED
from part4_ch4_4a import CH4_4A_CURATED
from part4_ch4_4b import CH4_4B_CURATED

CHAPTER_METADATA = {
    "4.1": "Mechanical Oscillations",
    "4.2": "Electric Oscillations",
    "4.3": "Elastic Waves. Acoustics",
    "4.4": "Electromagnetic Waves. Radiation"
}

all_batches = [
    CH4_1A_CURATED,
    CH4_1B_CURATED,
    CH4_1C_CURATED,
    CH4_1D_CURATED,
    CH4_2A_CURATED,
    CH4_2B_CURATED,
    CH4_3A_CURATED,
    CH4_3B_CURATED,
    CH4_4A_CURATED,
    CH4_4B_CURATED,
]

curated_map = {}
for batch in all_batches:
    for item in batch:
        qid = item['id']
        num = int(qid.split('.')[1])
        if 1 <= num <= 93:
            ch_id = "4.1"
        elif 94 <= num <= 149:
            ch_id = "4.2"
        elif 150 <= num <= 188:
            ch_id = "4.3"
        elif 189 <= num <= 238:
            ch_id = "4.4"
        else:
            raise ValueError(f"Unexpected question id {qid}")

        item['chapter_id'] = ch_id
        item['chapter_title'] = CHAPTER_METADATA[ch_id]
        item['part_id'] = 4
        item['part_title'] = "Oscillations and Waves"
        curated_map[qid] = item

print(f"Total curated Part 4 problems loaded: {len(curated_map)} (expected 238)")
assert len(curated_map) == 238, f"Expected 238 problems, got {len(curated_map)}"

# Verify all contiguous from 4.1 to 4.238
for i in range(1, 239):
    qid = f"4.{i}"
    assert qid in curated_map, f"Missing {qid} in curated map"
print("Contiguity check passed for all 238 Part 4 problems!")

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
        q['part_id'] = 4
        q['part_title'] = "Oscillations and Waves"
        updated_count += 1

print(f"Updated {updated_count} questions in questions_seed.json.")
assert updated_count == 238, f"Expected 238 questions updated in seed, got {updated_count}"
with open(seed_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
print("Saved data/questions_seed.json.")

# 2. Update data/part4.json
part4_path = BASE_DIR / "data" / "part4.json"
part4_list = []
for i in range(1, 239):
    qid = f"4.{i}"
    c = curated_map[qid]
    part4_list.append({
        "id": qid,
        "title": c.get("title", f"Problem {qid}"),
        "part_id": 4,
        "part_title": "Oscillations and Waves",
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

with open(part4_path, "w", encoding="utf-8") as f:
    json.dump(part4_list, f, ensure_ascii=False, indent=2)
print(f"Wrote {len(part4_list)} questions to data/part4.json.")

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
            part_id = 4,
            part_title = 'Oscillations and Waves'
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
assert db_updated == 238, f"Expected 238 db rows updated, got {db_updated}"
print("Part 4 curation applied successfully to all 238 problems!")
