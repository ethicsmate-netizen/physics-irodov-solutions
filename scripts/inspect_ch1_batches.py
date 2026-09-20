import json
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('data/ch1_extracted_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

def show_batch(start, end):
    for item in items[start:end]:
        print(f"=== Problem {item['id']} ===")
        print(f"Q: {item['q']}")
        print(f"A: {item['a']}")
        print("-" * 50)

if __name__ == '__main__':
    import sys
    s = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    e = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    show_batch(s, e)
