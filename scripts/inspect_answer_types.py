import json
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE_DIR = Path(__file__).resolve().parent.parent

qs = json.load(open(BASE_DIR / "data" / "questions_seed.json", encoding="utf-8"))

text_answers = []
multiline_answers = []
for q in qs:
    ans = q.get('answer', '')
    if '\n' in ans:
        multiline_answers.append(q['id'])
    # check if answer starts with a word like "See", "When", "The", "Will", "Let", "If", "Refer"
    first_word = ans.split()[0] if ans.split() else ''
    first_word_clean = re.sub(r'[^a-zA-Z]', '', first_word)
    if first_word_clean in ['See', 'When', 'The', 'Will', 'Let', 'If', 'Refer', 'In', 'At', 'For', 'From', 'On', 'Due', 'To', 'As', 'By', 'It', 'Here', 'Where']:
        text_answers.append((q['id'], first_word_clean, ans[:80]))

print(f"Total answers with newlines: {len(multiline_answers)}")
print(f"Total answers starting with English text: {len(text_answers)}")
print("\nSample 15 text answers:")
for item in text_answers[:15]:
    print(f"[{item[0]}] ({item[1]}): {item[2]}")
