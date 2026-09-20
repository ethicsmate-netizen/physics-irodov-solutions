import sys
from pathlib import Path
import pypdf

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent
reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

for p in range(23, 28):
    txt = (reader.pages[p].extract_text() or '').replace('□', ' ')
    print(f"=== PDF Page {p+1} ===")
    lines = [l.strip() for l in txt.split('\n') if l.strip()]
    print("First 5 lines:", lines[:5])
    print("Last 5 lines:", lines[-5:])
    for l in lines:
        if '1.' in l or 'Conservation' in l or 'Dynamics' in l:
            print("   ->", l)
