import sys
from pathlib import Path
import pypdf
import re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent
reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

# Look at the end of the PDF to see the answers for Part 6
print(f"Total PDF pages: {len(reader.pages)}")

# Search backward from the end for Part 6 answers
for p in range(len(reader.pages) - 1, 270, -1):
    txt = (reader.pages[p].extract_text() or '')
    if '6.7' in txt or '6.300' in txt or '6.310' in txt or 'Atomic and Nuclear' in txt or '6.29' in txt:
        print(f"Found on PDF page {p+1}:")
        for line in txt.split('\n')[-30:]:
            if line.strip():
                print("  ", line.strip()[:80])
        break
