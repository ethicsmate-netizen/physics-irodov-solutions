"""
apply_part5_curation.py
Merge all 11 curated modules of Part 5 (Optics, 5.1 to 5.275, 275 problems)
into data/questions_seed.json, data/part5.json, and data/irodov.db.
"""

import json
import sqlite3
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

# Import all Part 5 curated modules
from part5_ch5_1a import CH5_1A_CURATED
from part5_ch5_1b import CH5_1B_CURATED
from part5_ch5_2a import CH5_2A_CURATED
from part5_ch5_2b import CH5_2B_CURATED
from part5_ch5_3a import CH5_3A_CURATED
from part5_ch5_3b import CH5_3B_CURATED
from part5_ch5_4a import CH5_4A_CURATED
from part5_ch5_4b import CH5_4B_CURATED
from part5_ch5_5 import CH5_5_CURATED
from part5_ch5_6 import CH5_6_CURATED
from part5_ch5_7 import CH5_7_CURATED

CHAPTER_METADATA = {
    "5.1": "Photometry and Geometrical Optics",
    "5.2": "Interference of Light",
    "5.3": "Diffraction of Light",
    "5.4": "Polarization of Light",
    "5.5": "Dispersion and Absorption of Light",
    "5.6": "Optics of Moving Sources",
    "5.7": "Thermal Radiation. Quantum Nature of Light"
}

all_batches = [
    CH5_1A_CURATED,
    CH5_1B_CURATED,
    CH5_2A_CURATED,
    CH5_2B_CURATED,
    CH5_3A_CURATED,
    CH5_3B_CURATED,
    CH5_4A_CURATED,
    CH5_4B_CURATED,
    CH5_5_CURATED,
    CH5_6_CURATED,
    CH5_7_CURATED,
]

curated_map = {}
for batch in all_batches:
    for item in batch:
        qid = item['id']
        num = int(qid.split('.')[1])
        if 1 <= num <= 63:
            ch_id = "5.1"
        elif 64 <= num <= 96:
            ch_id = "5.2"
        elif 97 <= num <= 156:
            ch_id = "5.3"
        elif 157 <= num <= 199:
            ch_id = "5.4"
        elif 200 <= num <= 223:
            ch_id = "5.5"
        elif 224 <= num <= 245:
            ch_id = "5.6"
        elif 246 <= num <= 275:
            ch_id = "5.7"
        else:
            raise ValueError(f"Unexpected question id {qid}")

        item['chapter_id'] = ch_id
        item['chapter_title'] = CHAPTER_METADATA[ch_id]
        item['part_id'] = 5
        item['part_title'] = "Optics"
        curated_map[qid] = item

print(f"Total curated Part 5 problems loaded: {len(curated_map)} (expected 275)")
assert len(curated_map) == 275, f"Expected 275 problems, got {len(curated_map)}"

# Verify all contiguous from 5.1 to 5.275
for i in range(1, 276):
    qid = f"5.{i}"
    assert qid in curated_map, f"Missing {qid} in curated map"
print("Contiguity check passed for all 275 Part 5 problems!")

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
        q['part_id'] = 5
        q['part_title'] = "Optics"
        updated_count += 1

print(f"Updated {updated_count} questions in questions_seed.json.")
assert updated_count == 275, f"Expected 275 questions updated in seed, got {updated_count}"
with open(seed_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
print("Saved data/questions_seed.json.")

# 2. Update data/part5.json
part5_path = BASE_DIR / "data" / "part5.json"
part5_list = []
for i in range(1, 276):
    qid = f"5.{i}"
    c = curated_map[qid]
    part5_list.append({
        "id": qid,
        "title": c.get("title", f"Problem {qid}"),
        "part_id": 5,
        "part_title": "Optics",
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

with open(part5_path, "w", encoding="utf-8") as f:
    json.dump(part5_list, f, ensure_ascii=False, indent=2)
print(f"Wrote {len(part5_list)} questions to data/part5.json.")

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
            part_id = 5,
            part_title = 'Optics'
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
assert db_updated == 275, f"Expected 275 db rows updated, got {db_updated}"
print("Part 5 curation applied successfully to all 275 problems!")
