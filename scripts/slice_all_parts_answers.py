import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

# Read raw answers dumped from pages 274 to 355
import pypdf
reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

all_answers_text = []
for p in range(274, 355):
    txt = reader.pages[p].extract_text() or ''
    all_answers_text.append(f"\n--- PDF Page {p+1} (Book p.{p+1-6}) ---\n" + txt)

full_answers = "\n".join(all_answers_text)

# We know the headings:
# Part 1: Physical Fundamentals of Mechanics
# Part 2: Thermodynamics and Molecular Physics
# Part 3: Electrodynamics
# Part 4: Oscillations and Waves
# Part 5: Optics
# Part 6: Atomic and Nuclear Physics

# Let's find their occurrences in full_answers
headings = [
    (1, "Physical Fundamentals of Mechanics"),
    (2, "Thermodynamics and Molecular Physics"),
    (3, "Electrodynamics"),
    (4, "Oscillations and Waves"),
    (5, "Optics"),
    (6, "Atomic and Nuclear Physics")
]

def make_fuzzy_regex(h):
    words = h.split()
    return r'[\s\u25a0-\u25ff\W]*'.join(re.escape(w) for w in words)

matches = []
for p_num, h in headings:
    pattern = make_fuzzy_regex(h)
    m = list(re.finditer(pattern, full_answers, re.IGNORECASE))
    if m:
        # find the occurrence that is after page 274
        print(f"Heading Part {p_num} '{h}': found {len(m)} occurrences at {[match.start() for match in m]}")
        # Take the most relevant one in the answers section
        matches.append((p_num, h, m[0].start(), m[0].end()))
    else:
        print(f"FAILED to find heading Part {p_num}: {h}")

matches.sort(key=lambda x: x[2])

# Now slice cleanly!
for idx, (p_num, h, start, end) in enumerate(matches):
    next_start = matches[idx+1][2] if idx+1 < len(matches) else len(full_answers)
    part_slice = full_answers[end:next_start].strip()
    out_file = BASE_DIR / "data" / f"clean_raw_answers_part{p_num}.txt"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(part_slice)
    print(f"Part {p_num}: saved {out_file.name} ({len(part_slice)} chars)")

print("\nClean sliced answer files created for all parts!")
