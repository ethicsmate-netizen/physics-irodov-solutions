import sys
from pathlib import Path
import pypdf

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent
reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

# Inspect text on PDF page 277 (Book page 271)
page = reader.pages[276] # 0-indexed 276 is page 277

words = []
def visitor_body(text, cm, tm, fontDict, fontSize):
    if text.strip():
        # tm is [a, b, c, d, e, f] where e is x, f is y
        x = tm[4]
        y = tm[5]
        words.append((y, x, text, fontSize))

page.extract_text(visitor_text=visitor_body)

# Sort primarily by y (descending: top to bottom), secondarily by x (ascending: left to right)
# Round y to nearest 3 points to group into lines
lines = {}
for y, x, text, size in words:
    line_y = round(y / 4.0) * 4.0
    if line_y not in lines:
        lines[line_y] = []
    lines[line_y].append((x, text))

print(f"Total lines extracted by spatial visitor on PDF Page 277: {len(lines)}")
sorted_y = sorted(lines.keys(), reverse=True)
for y in sorted_y[:40]:
    line_parts = sorted(lines[y], key=lambda item: item[0])
    line_str = "".join([t for _, t in line_parts])
    print(f"y={y:5.1f} | {line_str}")
