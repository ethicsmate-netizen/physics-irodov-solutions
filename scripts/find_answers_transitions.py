import sys
from pathlib import Path
import pypdf
import re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent
reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

# In answers, let's search for Part headings:
headers = [
    "Thermodynamics and Molecular Physics",
    "Electrodynamics",
    "Oscillations and Waves",
    "Optics",
    "Atomic and Nuclear Physics"
]

for p in range(274, 355):
    txt = reader.pages[p].extract_text() or ''
    for h in headers:
        if h.lower() in txt.lower():
            print(f"\n>>> Header '{h}' found on PDF P.{p+1} (Book p.{p+1-6}):")
            # print what came just before it
            prev_txt = reader.pages[p-1].extract_text() or ''
            prev_lines = [l.strip() for l in prev_txt.split('\n') if l.strip()]
            print("Previous page bottom:")
            for l in prev_lines[-6:]:
                print("   ", l)
            curr_lines = [l.strip() for l in txt.split('\n') if l.strip()]
            print("Current page top:")
            for l in curr_lines[:6]:
                print("   ", l)

