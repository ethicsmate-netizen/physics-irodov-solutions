import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "data" / "questions_seed.json", "r", encoding="utf-8") as f:
    seed = json.load(f)

# Sample questions from Part 2, Part 3, Part 4, Part 5, Part 6
sample_ids = ["2.1", "2.26", "2.62", "2.113", "3.1", "3.54", "4.1", "5.1", "6.1"]

for q in seed:
    if q["id"] in sample_ids:
        print(f"=== Problem {q['id']}: {q.get('title')} (Chapter: {q.get('chapter_id')} - {q.get('chapter_title')}) ===")
        print("Question statement (first 150 chars):")
        print("  ", q["statement"][:150].replace('\n', ' '))
        print("Raw Answer / Final Answer:")
        print("  ", repr(q.get("final_answer", "")))
        print("Hints count:", len(q.get("hints", [])))
        print("Solution steps count:", len(q.get("solution_steps", [])))
        if q.get("solution_steps"):
            print("First step:")
            print("  ", q["solution_steps"][0].get("title"), "->", repr(q["solution_steps"][0].get("content")[:100]))
        print()
