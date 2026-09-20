import pypdf
import sys
import logging
import warnings
import re

warnings.filterwarnings("ignore")
logging.getLogger("pypdf").setLevel(logging.ERROR)
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

reader = pypdf.PdfReader("ARIHANT IE IRODOV NEW EDITION.pdf")

for idx in range(6, 30):
    txt = (reader.pages[idx].extract_text() or "").replace('□', ' ')
    if re.search(r'(?:^|\n)\s*58\.\s+', txt) or re.search(r'(?:^|\n)\s*59\.\s+', txt) or "1.2. The Fundamental Equation of Dynamics" in txt:
        print(f"Page {idx+1} contains transition to 1.2:")
        lines = txt.split("\n")
        for l in lines:
            if re.match(r'^\s*(?:57|58|59|60)\.\s+', l) or "Fundamental" in l:
                print("  ", l.strip()[:80])
