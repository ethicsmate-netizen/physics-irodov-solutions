import sys
from pathlib import Path
import pypdf
import re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent
reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

# Answers section is from PDF page 275 (Book page 269) to PDF page 355 (Book page 351).
# Let's find each part header in the answers section!
part_answers = {}
for p in range(274, len(reader.pages)):
    txt = (reader.pages[p].extract_text() or '')
    for part_num, name in [
        (1, "Physical Fundamentals of Mechanics"),
        (2, "Thermodynamics and Molecular Physics"),
        (3, "Electrodynamics"),
        (4, "Oscillations and Waves"),
        (5, "Optics"),
        (6, "Atomic and Nuclear Physics")
    ]:
        if name.lower() in txt.lower():
            print(f"Found '{name}' (Part {part_num}) answers header around PDF page {p+1} (Book p.{p+1-6})")

