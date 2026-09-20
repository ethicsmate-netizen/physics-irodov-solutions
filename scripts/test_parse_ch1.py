import pypdf
import sys
import logging
import warnings
import re
import json

warnings.filterwarnings("ignore")
logging.getLogger("pypdf").setLevel(logging.ERROR)
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

reader = pypdf.PdfReader("ARIHANT IE IRODOV NEW EDITION.pdf")

# 1. Extract Questions 1-58 from pages 7-16 (indices 6-15)
raw_q_text = ""
for idx in range(6, 16):
    raw_q_text += "\n" + (reader.pages[idx].extract_text() or "").replace('□', ' ')

# Discard anything after 1.2 header
if "1.2 The Fundamental Equation of Dynamics" in raw_q_text:
    raw_q_text = raw_q_text.split("1.2 The Fundamental Equation of Dynamics")[0]

# Remove intro formula section before question 1
if "1. A motorboat" in raw_q_text:
    raw_q_text = "1. A motorboat" + raw_q_text.split("1. A motorboat", 1)[1]

# Split questions by number
q_matches = list(re.finditer(r'(?:^|\n)\s*(\d{1,2})\.\s+', raw_q_text))
questions = {}
for i in range(len(q_matches)):
    q_num = int(q_matches[i].group(1))
    if q_num > 58:
        continue
    start = q_matches[i].end()
    end = q_matches[i+1].start() if i + 1 < len(q_matches) else len(raw_q_text)
    txt = raw_q_text[start:end].strip()
    
    # Clean up watermarks, page footers, figure captions
    txt = re.sub(r'Telegram\s+@unacademyplusdiscounts', '', txt)
    txt = re.sub(r'\d+\s*\|\s*Physical Fundamentals of Mechanics', '', txt)
    txt = re.sub(r'Physical Fundamentals of Mechanics\s*\|\s*\d+', '', txt)
    txt = re.sub(r'Kinematics\s*\|\s*\d+', '', txt)
    txt = re.sub(r'\d+\s*\|\s*Kinematics', '', txt)
    txt = re.sub(r'Physical Fundamentals\s+of Mechanics', '', txt)
    txt = re.sub(r'Fig\.\s*1\.\d+', '', txt)
    # Clean multiple spaces/newlines
    lines = [l.strip() for l in txt.split('\n') if l.strip()]
    cleaned = ' '.join(lines)
    # Fix spacing around punctuation and subparts
    cleaned = re.sub(r'\s+([,.;:?!])', r'\1', cleaned)
    cleaned = re.sub(r'\(a\)', '\n(a)', cleaned)
    cleaned = re.sub(r'\(b\)', '\n(b)', cleaned)
    cleaned = re.sub(r'\(c\)', '\n(c)', cleaned)
    cleaned = re.sub(r'\(d\)', '\n(d)', cleaned)
    questions[q_num] = cleaned.strip()

# 2. Extract Answers 1-58 from pages 275-277 (indices 274, 275, 276)
raw_ans_text = ""
for idx in [274, 275, 276]:
    raw_ans_text += "\n" + (reader.pages[idx].extract_text() or "").replace('□', ' ')

# Stop before 59
ans_matches = list(re.finditer(r'(?:^|\n)\s*(\d{1,2})\.\s+', raw_ans_text))
answers = {}
for i in range(len(ans_matches)):
    a_num = int(ans_matches[i].group(1))
    if a_num > 58:
        continue
    start = ans_matches[i].end()
    end = ans_matches[i+1].start() if i + 1 < len(ans_matches) else len(raw_ans_text)
    txt = raw_ans_text[start:end].strip()
    
    txt = re.sub(r'Telegram\s+@unacademyplusdiscounts', '', txt)
    txt = re.sub(r'Physical Fundamentals of Mechanics', '', txt)
    txt = re.sub(r'Answers\s*\|\s*\d+', '', txt)
    txt = re.sub(r'\d+\s*\|\s*Answers', '', txt)
    lines = [l.strip() for l in txt.split('\n') if l.strip()]
    cleaned = ' '.join(lines)
    cleaned = re.sub(r'\s+([,.;:?!])', r'\1', cleaned)
    answers[a_num] = cleaned.strip()

print(f"Extracted {len(questions)} questions and {len(answers)} answers.")
for qn in [1, 2, 3, 10, 25, 45, 58]:
    print(f"\n--- [1.{qn}] ---")
    print(f"Q: {questions.get(qn)}")
    print(f"A: {answers.get(qn)}")
