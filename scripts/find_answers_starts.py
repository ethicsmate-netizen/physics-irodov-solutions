import sys
from pathlib import Path
import pypdf
import re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent
reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

print("Searching for answer section headers or '1. ' starts...")
for p in range(273, 355):
    txt = reader.pages[p].extract_text() or ''
    # Look for lines that look like start of part or 1.
    lines = [l.strip() for l in txt.split('\n') if l.strip()]
    for i, l in enumerate(lines):
        if re.match(r'^1\.\s', l):
            print(f"Possible start at PDF P.{p+1} (Book p.{p+1-6}):")
            for ctx in lines[max(0, i-4):min(len(lines), i+3)]:
                print(f"   {ctx}")
            print("-" * 40)
