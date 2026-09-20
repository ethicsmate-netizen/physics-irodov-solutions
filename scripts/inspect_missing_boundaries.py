import sys
from pathlib import Path
import pypdf
import re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent
reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

def inspect_pages(title, start_p, end_p):
    print(f"\n=================== {title} (Pages {start_p}-{end_p}) ===================")
    for p in range(start_p - 1, end_p):
        txt = (reader.pages[p].extract_text() or '').replace('□', ' ')
        print(f"--- PDF Page {p+1} ---")
        lines = txt.split('\n')
        # print first 15 lines of each page
        for line in lines[:20]:
            if line.strip():
                print("  ", line.strip())

# Ch 1.3
inspect_pages("Ch 1.3 Check", 24, 27)

# Ch 5.1 & 5.3
inspect_pages("Ch 5.1 Check", 191, 194)
inspect_pages("Ch 5.3 Check", 207, 210)

# Ch 6.3 & end of Part 6
inspect_pages("Ch 6.3 Check", 248, 251)
inspect_pages("Part 6 End Check", 270, 275)
