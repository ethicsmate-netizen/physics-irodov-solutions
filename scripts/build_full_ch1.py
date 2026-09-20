"""
build_full_ch1.py
Merges batches 1, 2, 3 into a complete 58-problem Chapter 1.1 suite,
updates data/questions_seed.json, and synchronizes SQLite data/irodov.db.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.abspath('.'))

from scripts.ch1_batch1 import BATCH_1
from scripts.ch1_batch2 import BATCH_2
from scripts.ch1_batch3 import BATCH_3

all_ch1 = BATCH_1 + BATCH_2 + BATCH_3
print(f"Loaded {len(all_ch1)} Chapter 1.1 problems.")

# Verify sequence 1.1 to 1.58
ids = [q['id'] for q in all_ch1]
expected_ids = [f"1.{i}" for i in range(1, 59)]
assert ids == expected_ids, f"ID mismatch! Missing or out of order: {set(expected_ids) - set(ids)}"
print("Assertion passed: Exactly 1.1 to 1.58 in strict order.")

# Enrich with standard metadata
for q in all_ch1:
    q['part_id'] = 1
    q['part_title'] = "Physical Fundamentals of Mechanics"
    q['chapter_id'] = "1.1"
    q['chapter_title'] = "Kinematics"
    stmt = q.get('statement') or q.get('question') or ''
    q['statement'] = stmt
    q['question'] = stmt

# Load existing seed to retain other chapters/parts
SEED_PATH = 'data/questions_seed.json'
with open(SEED_PATH, 'r', encoding='utf-8') as f:
    existing_seed = json.load(f)

# Non-Chapter 1.1 questions to preserve
other_questions = []
for q in existing_seed:
    qid = q.get('id', '')
    # Chapter 1.1 questions have ids 1.1 through 1.58
    if qid.startswith('1.'):
        try:
            num = int(qid.split('.')[1])
            if 1 <= num <= 58:
                continue # Replace with enriched full ch1
        except ValueError:
            pass
    other_questions.append(q)

print(f"Retaining {len(other_questions)} existing questions from other chapters.")

# Combine: Chapter 1.1 (58) + other questions
final_questions = all_ch1 + other_questions
print(f"Total question count: {len(final_questions)}")

with open(SEED_PATH, 'w', encoding='utf-8') as f:
    json.dump(final_questions, f, indent=2, ensure_ascii=False)

print(f"Successfully saved {SEED_PATH} with {len(final_questions)} questions.")

# Now sync with backend/db.py
from backend.db import init_db

init_db(force_reseed=True)
print("Successfully synced questions into SQLite database (data/irodov.db).")
