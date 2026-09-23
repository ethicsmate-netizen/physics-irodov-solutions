import sys
from pathlib import Path
import pypdf

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent
reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

print("Scanning pages 270 to 355 for Part transitions:")
for p in range(270, 355):
    txt = reader.pages[p].extract_text() or ''
    lines = [line.strip() for line in txt.split('\n') if line.strip()]
    for i, line in enumerate(lines):
        if any(w in line.upper() for w in ['PART ONE', 'PART TWO', 'PART THREE', 'PART FOUR', 'PART FIVE', 'PART SIX', 'PART 1', 'PART 2', 'PART 3', 'PART 4', 'PART 5', 'PART 6']):
            print(f"P.{p+1} (Book p.{p+1-6}): line: {line}")
            for ctx in lines[max(0, i-2):min(len(lines), i+3)]:
                print(f"    {ctx}")
