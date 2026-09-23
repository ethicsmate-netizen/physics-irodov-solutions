import sys
from pathlib import Path
import pypdf
import re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

pdf_path = BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"
reader = pypdf.PdfReader(str(pdf_path))

for p in range(274, 356):
    txt = reader.pages[p].extract_text() or ''
    first_few = [l.strip() for l in txt.split('\n') if l.strip()][:5]
    # Check if there's any header or 1.1, 2.1, 3.1, 4.1, 5.1, 6.1
    has_target = any(
        re.search(r'\b(?:PART|part)\b|\b1\.1\b|\b2\.1\b|\b3\.1\b|\b4\.1\b|\b5\.1\b|\b6\.1\b', l)
        for l in first_few
    )
    # Check for keywords
    keywords = ["thermodynamics", "electrodynamics", "oscillations", "optics", "atomic", "nuclear"]
    matched_kw = [kw for kw in keywords if kw in txt.lower()]
    print(f"P.{p+1}: {' | '.join(first_few[:2])} (kw: {matched_kw})")
