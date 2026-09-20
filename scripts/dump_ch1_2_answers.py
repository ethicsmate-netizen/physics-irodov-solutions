import sys
from pathlib import Path
import pypdf

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

# Let's inspect answers for problems 59 to 117 (PDF pages 277-280)
raw_answers = ""
for p in range(276, 281): # 0-indexed 276-280 is pages 277-281
    raw_answers += f"\n--- PDF P.{p+1} ---\n" + reader.pages[p].extract_text()

with open("data/raw_answers_ch1_2.txt", "w", encoding="utf-8") as f:
    f.write(raw_answers)

print(f"Saved raw answers for 59-117 (length: {len(raw_answers)} chars)")
