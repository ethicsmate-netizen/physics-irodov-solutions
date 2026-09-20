import json
import re
import sys
from pathlib import Path
import pypdf

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))
qs = json.load(open(BASE_DIR / "data" / "questions_seed.json", encoding="utf-8"))

# Extract raw text for Chapter 1.1 (PDF pages 7 to 16)
raw_p1 = ""
for p in range(6, 16):
    raw_p1 += "\n" + reader.pages[p].extract_text()

q_pattern = re.compile(r'(?:^|\n)\s*(\d{1,3})\.\s+')
matches = list(q_pattern.finditer(raw_p1))
pdf_dict = {}
for i in range(len(matches)):
    num = int(matches[i].group(1))
    if 1 <= num <= 58:
        start = matches[i].end()
        end = matches[i+1].start() if i+1 < len(matches) else len(raw_p1)
        pdf_dict[num] = raw_p1[start:end].strip().replace('\n', ' ')

print("Comparing curated statements with raw PDF text for first 20 questions:")
for i in range(1, 21):
    q = qs[i-1]
    curated = q['statement']
    raw = pdf_dict.get(i, 'NOT FOUND')
    print(f"\n[{q['id']}]")
    print(f"  PDF RAW:  {raw[:140]}")
    print(f"  CURATED:  {curated[:140]}")
    print(f"  ANS CUR:  {q['answer']}")
