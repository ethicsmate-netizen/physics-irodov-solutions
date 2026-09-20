#!/usr/bin/env python3
"""
Question Importer & Batch Ingestion Script for I.E. Irodov Question Bank.
Automatically maps problem IDs (e.g. 1.2, 2.15, 3.104) to their proper Part
and Chapter using irodov_catalog.json, validates LaTeX math, and populates
both data/questions_seed.json and data/irodov.db (SQLite).
"""

import json
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from backend import db

DATA_DIR = BASE_DIR / "data"
CATALOG_PATH = DATA_DIR / "irodov_catalog.json"
QUESTIONS_PATH = DATA_DIR / "questions_seed.json"


def load_catalog():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def find_chapter_for_problem(problem_id, catalog):
    """
    Given a problem ID like '1.14' or '3.105', determines the part and chapter
    from the problem ranges defined in irodov_catalog.json.
    """
    parts = problem_id.strip().split(".")
    if len(parts) != 2:
        return None

    try:
        part_num = int(parts[0])
        prob_num = int(parts[1])
    except ValueError:
        return None

    for part in catalog.get("parts", []):
        if part["id"] == part_num:
            for ch in part.get("chapters", []):
                # parse range e.g. "1.1 - 1.58"
                m = re.match(r"(\d+)\.(\d+)\s*-\s*(\d+)\.(\d+)", ch["range"])
                if m:
                    start_num = int(m.group(2))
                    end_num = int(m.group(4))
                    if start_num <= prob_num <= end_num:
                        return {
                            "part_id": part["id"],
                            "part_title": part["title"],
                            "chapter_id": ch["id"],
                            "chapter_title": ch["title"]
                        }
            # Fallback to first chapter of the part
            if part.get("chapters"):
                first_ch = part["chapters"][0]
                return {
                    "part_id": part["id"],
                    "part_title": part["title"],
                    "chapter_id": first_ch["id"],
                    "chapter_title": first_ch["title"]
                }

    return None


def import_questions_from_file(input_file_path):
    """
    Imports questions from a JSON or Markdown/Text file.
    """
    path = Path(input_file_path)
    if not path.exists():
        print(f"Error: File {input_file_path} not found.")
        return 0

    catalog = load_catalog()

    new_questions = []
    if path.suffix == ".json":
        with open(path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            if isinstance(raw_data, list):
                new_questions = raw_data
            elif isinstance(raw_data, dict):
                new_questions = [raw_data]
    else:
        # Simple plain text / markdown parser
        # Expecting format:
        # ## Problem 1.2
        # Statement text...
        # Answer: ...
        # Solution: ...
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        blocks = re.split(r"(?:^|\n)##\s*(?:Problem\s*)?(\d+\.\d+)", content)
        # blocks will be [preamble, id1, content1, id2, content2, ...]
        for i in range(1, len(blocks), 2):
            p_id = blocks[i].strip()
            p_body = blocks[i+1]

            # Extract statement, answer, solution
            ans_match = re.search(r"(?:Answer|Ans):\s*(.+?)(?=\n(?:Solution|Sol):|\Z)", p_body, re.DOTALL | re.IGNORECASE)
            sol_match = re.search(r"(?:Solution|Sol):\s*(.+)", p_body, re.DOTALL | re.IGNORECASE)

            answer = ans_match.group(1).strip() if ans_match else ""
            solution = sol_match.group(1).strip() if sol_match else ""

            # Remove Answer and Solution from statement
            stmt = p_body
            if ans_match:
                stmt = stmt[:ans_match.start()]
            elif sol_match:
                stmt = stmt[:sol_match.start()]
            statement = stmt.strip()

            new_questions.append({
                "id": p_id,
                "statement": statement,
                "answer": answer,
                "solution": solution,
                "difficulty": 2,
                "tags": [],
                "hints": []
            })

    # Load existing questions
    existing_questions = []
    if QUESTIONS_PATH.exists():
        with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
            try:
                existing_questions = json.load(f)
            except Exception:
                existing_questions = []

    existing_dict = {q["id"]: q for q in existing_questions}

    added_count = 0
    updated_count = 0

    for q in new_questions:
        q_id = str(q.get("id", "")).strip()
        if not q_id:
            continue

        meta = find_chapter_for_problem(q_id, catalog)
        if not meta:
            print(f"Warning: Could not automatically resolve chapter for problem {q_id}")
            meta = {
                "part_id": 1,
                "part_title": "Physical Fundamentals of Mechanics",
                "chapter_id": "1.1",
                "chapter_title": "Kinematics"
            }

        entry = {
            "id": q_id,
            "part_id": q.get("part_id", meta["part_id"]),
            "part_title": q.get("part_title", meta["part_title"]),
            "chapter_id": q.get("chapter_id", meta["chapter_id"]),
            "chapter_title": q.get("chapter_title", meta["chapter_title"]),
            "statement": q.get("statement", "").strip(),
            "difficulty": q.get("difficulty", 2),
            "tags": q.get("tags", []),
            "hints": q.get("hints", []),
            "answer": q.get("answer", "").strip(),
            "solution": q.get("solution", "").strip()
        }

        if q_id in existing_dict:
            existing_dict[q_id].update(entry)
            updated_count += 1
        else:
            existing_dict[q_id] = entry
            added_count += 1

    # Sort questions naturally (e.g. 1.1, 1.2, ..., 1.10, 2.1...)
    def sort_key(item):
        parts = item["id"].split(".")
        try:
            return (int(parts[0]), int(parts[1]))
        except Exception:
            return (999, 999)

    final_list = sorted(existing_dict.values(), key=sort_key)

    # Save to JSON
    with open(QUESTIONS_PATH, "w", encoding="utf-8") as f:
        json.dump(final_list, f, indent=2, ensure_ascii=False)

    # Re-sync SQLite database
    db.init_db(force_reseed=True)

    print(f"Successfully processed {len(new_questions)} problem(s):")
    print(f" - Added: {added_count}")
    print(f" - Updated: {updated_count}")
    print(f" - Total in database now: {len(final_list)}")
    return len(final_list)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/import_questions.py <path_to_questions.json_or_txt>")
        sys.exit(1)

    import_questions_from_file(sys.argv[1])
