import json
from pathlib import Path
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

qs = json.load(open(BASE_DIR / "data" / "questions_seed.json", encoding="utf-8"))

control_chars = [('\x0c', 'FORMFEED \\f'), ('\x08', 'BACKSPACE \\b'), ('\x07', 'BELL \\a'), ('\x0b', 'VTAB \\v')]

found = 0
for q in qs:
    for name in ['statement', 'answer', 'solution']:
        text = q.get(name, '')
        for char, desc in control_chars:
            if char in text:
                found += 1
                print(f"[{q['id']}] Found {desc} in {name}!")
                idx = text.find(char)
                print(f"   Snippet: {repr(text[max(0, idx-15):min(len(text), idx+15)])}")

print(f"\nTotal control character occurrences found: {found}")
