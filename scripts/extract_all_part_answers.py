import sys
from pathlib import Path
import pypdf

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent
reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

# Precise page boundaries (0-indexed):
# Part 1: 274 to 289
# Part 2: 289 to 298
# Part 3: 298 to 316
# Part 4: 316 to 328
# Part 5: 328 to 342
# Part 6: 342 to 355

part_ranges = {
    1: (274, 290),
    2: (289, 299),
    3: (298, 317),
    4: (316, 329),
    5: (328, 343),
    6: (342, 355)
}

for part_num, (p_start, p_end) in part_ranges.items():
    out_file = BASE_DIR / "data" / f"raw_answers_part{part_num}.txt"
    chunks = []
    for p in range(p_start, p_end):
        txt = reader.pages[p].extract_text() or ''
        chunks.append(f"\n--- PDF Page {p+1} (Book p.{p+1-6}) ---\n")
        chunks.append(txt)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(chunks))
    print(f"Part {part_num}: extracted PDF pages {p_start+1} to {p_end} -> {out_file.name} ({len(chunks)} chunks, {out_file.stat().st_size} bytes)")

print("\nAll 6 parts raw answers extracted cleanly!")
