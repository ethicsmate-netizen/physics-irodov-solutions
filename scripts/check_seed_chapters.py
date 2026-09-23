import json
from pathlib import Path
from verify_all_37_chapters import CATALOG

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "data" / "questions_seed.json", "r", encoding="utf-8") as f:
    seed = json.load(f)

# Build a lookup from problem ID to expected part, chapter_id, chapter_title
lookup = {}
for part in CATALOG["parts"]:
    for ch in part["chapters"]:
        for num in range(ch["start"], ch["end"] + 1):
            pid = f"{part['id']}.{num}"
            lookup[pid] = {
                "part_id": part["id"],
                "part_title": part["title"],
                "chapter_id": ch["id"],
                "chapter_title": ch["title"]
            }

mismatches = []
for q in seed:
    pid = q["id"]
    if pid not in lookup:
        mismatches.append(f"Unknown ID in seed: {pid}")
        continue
    exp = lookup[pid]
    ch_id = q.get("chapter_id")
    ch_title = q.get("chapter_title")
    part_id = q.get("part_id")
    if str(ch_id) != str(exp["chapter_id"]) or ch_title != exp["chapter_title"] or str(part_id) != str(exp["part_id"]):
        mismatches.append(f"{pid}: current ({part_id}, {ch_id}, '{ch_title}') vs expected ({exp['part_id']}, {exp['chapter_id']}, '{exp['chapter_title']}')")

print(f"Total questions checked: {len(seed)}")
print(f"Mismatches found: {len(mismatches)}")
if mismatches:
    print("First 20 mismatches:")
    for m in mismatches[:20]:
        print("  ", m)
