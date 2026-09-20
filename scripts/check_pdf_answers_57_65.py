import sys
from pathlib import Path
import pypdf

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

# Let's search pages 276-282 for Problem 59 to 65 answers
for p in range(275, 282):
    txt = (reader.pages[p].extract_text() or '')
    if '59.' in txt or '60.' in txt:
        print(f"=== PDF Page {p+1} (Book page {p+1-6}) ===")
        lines = txt.split('\n')
        for idx, l in enumerate(lines):
            if any(l.strip().startswith(f"{n}.") for n in range(57, 66)):
                print(f"L{idx:3d}: {l}")
                for j in range(idx+1, min(len(lines), idx+4)):
                    if any(lines[j].strip().startswith(f"{n}.") for n in range(50, 70)):
                        break
                    print(f"     {lines[j]}")
