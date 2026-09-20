import sys
from pathlib import Path
import pypdf
import re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent
reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

def check_pages_range(start_p, end_p, label):
    print(f"\n=================== {label} (Pages {start_p}-{end_p}) ===================")
    for p in range(start_p - 1, end_p):
        txt = (reader.pages[p].extract_text() or '').replace('□', ' ')
        # Find lines starting with a number followed by dot
        probs = re.findall(r'(?:^|\n)\s*(\d{1,4})\.\s+([^\n]+)', txt)
        print(f"PDF P.{p+1} (Book p.{p+1-6}):")
        for num, text in probs[:5]:
            print(f"   Prob {num}: {text[:60]}")
        if len(probs) > 5:
            num, text = probs[-1]
            print(f"   ... last prob on page: {num}: {text[:60]}")

check_pages_range(192, 195, "Ch 5.1 Start Check")
check_pages_range(208, 211, "Ch 5.3 Start Check")
check_pages_range(231, 235, "Ch 5.7 & Part 5 End Check")
check_pages_range(271, 275, "Ch 6.7 & Part 6 End Check")
