import sys
import json
from pathlib import Path
sys.path.insert(0, 'scripts')
from test_sequential_parser import parsed
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

with open('data/part2.json', 'r', encoding='utf-8') as f:
    p2 = json.load(f)
p2_map = {q['id']: q for q in p2}

print("=== Sample 2.160 to 2.184 (Liquids & Capillary) ===")
for n in range(160, 185):
    print(f"{n}: {p2_map[f'2.{n}']['statement'][:80].replace(chr(10), ' ')} -> {repr(parsed.get(n, 'MISSING'))}")

print("\n=== Sample 2.185 to 2.219 (Phase Transformations) ===")
for n in range(185, 220):
    print(f"{n}: {p2_map[f'2.{n}']['statement'][:80].replace(chr(10), ' ')} -> {repr(parsed.get(n, 'MISSING'))}")

print("\n=== Sample 2.220 to 2.257 (Transport Phenomena) ===")
for n in range(220, 258):
    print(f"{n}: {p2_map[f'2.{n}']['statement'][:80].replace(chr(10), ' ')} -> {repr(parsed.get(n, 'MISSING'))}")
