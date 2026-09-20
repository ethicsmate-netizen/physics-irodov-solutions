import sys
from pathlib import Path
import pypdf
import re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent
reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

for p in [272, 273]: # 0-indexed 272 is PDF P.273, 273 is PDF P.274
    txt = (reader.pages[p].extract_text() or '').replace('□', ' ')
    print(f"=== PDF Page {p+1} ===")
    matches = re.findall(r'(?:^|\n)\s*(\d{1,4})\.\s+([^\n]+)', txt)
    for m in matches:
        print(f"   {m[0]}. {m[1][:80]}")

