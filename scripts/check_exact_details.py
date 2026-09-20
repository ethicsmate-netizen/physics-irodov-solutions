import sys
from pathlib import Path
import pypdf
import re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent
reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

def print_section(p_num, title):
    print(f"\n=================== {title} (PDF Page {p_num}) ===================")
    txt = (reader.pages[p_num - 1].extract_text() or '').replace('□', ' ')
    lines = txt.split('\n')
    for idx, l in enumerate(lines):
        if any(w in l for w in ['1.3', '1.11', '1.12', '5.1', '5.2', '5.3', '5.6', '5.7', '6.3', '6.7', 'Laws', 'Diffraction', 'Photometry', 'Elementary']):
            print(f"Line {idx}: {l}")
            # print surrounding lines
            start = max(0, idx - 2)
            end = min(len(lines), idx + 8)
            for j in range(start, end):
                print(f"   [{j}] {lines[j]}")
            print("-----------------")

print_section(25, "PDF P.25 (Ch 1.3 area)")
print_section(26, "PDF P.26 (Ch 1.3 area)")
print_section(192, "PDF P.192 (Ch 5.1 area)")
print_section(193, "PDF P.193 (Ch 5.1 area)")
print_section(208, "PDF P.208 (Ch 5.3 area)")
print_section(209, "PDF P.209 (Ch 5.3 area)")
print_section(273, "PDF P.273 (Ch 6.7 end area)")
print_section(274, "PDF P.274 (Ch 6.7 end area)")
