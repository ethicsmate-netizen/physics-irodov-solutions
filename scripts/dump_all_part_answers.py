"""
dump_all_part_answers.py
Extract raw answer pages from the PDF for Parts 2, 3, 4, 5, 6 into data/ files.
"""

import sys
from pathlib import Path
import pypdf
import re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

pdf_path = BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"
reader = pypdf.PdfReader(str(pdf_path))

part_headers = {
    1: "Physical Fundamentals of Mechanics",
    2: "Thermodynamics and Molecular Physics",
    3: "Electrodynamics",
    4: "Oscillations and Waves",
    5: "Optics",
    6: "Atomic and Nuclear Physics"
}

# Scan pages 274 to 360 to find exact page start for each part's answers
part_starts = {}
for p in range(274, min(360, len(reader.pages))):
    txt = reader.pages[p].extract_text() or ''
    for part_num, header in part_headers.items():
        if header.lower() in txt.lower():
            if part_num not in part_starts:
                part_starts[part_num] = p
                print(f"Part {part_num} answers start around PDF page {p+1} (0-indexed {p})")

print("Part answer starts:", part_starts)

# Extract each part's answer pages
sorted_parts = sorted(part_starts.items(), key=lambda x: x[1])
for idx, (p_num, p_start) in enumerate(sorted_parts):
    p_end = sorted_parts[idx + 1][1] if idx + 1 < len(sorted_parts) else 355
    print(f"Extracting Part {p_num} answers: pages {p_start+1} to {p_end}")
    
    lines = []
    for p in range(p_start, p_end):
        txt = reader.pages[p].extract_text() or ''
        lines.append(f"\n--- Page {p+1} ---\n")
        lines.append(txt)
    
    out_file = BASE_DIR / "data" / f"raw_answers_part{p_num}.txt"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Saved {out_file.name} ({len(lines)} chunks)")

print("All raw answers extracted successfully!")
