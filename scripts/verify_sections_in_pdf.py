"""
verify_sections_in_pdf.py
Scans ARIHANT IE IRODOV NEW EDITION.pdf to find the true first problem number
and last problem number under each chapter header.
Compares this with data/irodov_catalog.json.
"""

import json
import logging
import os
from pathlib import Path
import re
import sys
import warnings
import pypdf

warnings.filterwarnings("ignore")
logging.getLogger("pypdf").setLevel(logging.ERROR)
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = Path(__file__).resolve().parent.parent
with open(BASE_DIR / "data" / "irodov_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

# Extract all pages up to page 274 (questions section)
pages_text = []
for i in range(274):
    pages_text.append((reader.pages[i].extract_text() or '').replace('□', ' '))

print("=== Scanning Actual Chapter Boundaries in PDF ===")

# Chapter header regex: e.g. "1.2 The Fundamental Equation of Dynamics", "2.1 Equation of the Gas State..."
ch_header_re = re.compile(r'(?:^|\n)\s*([1-6]\.[1-8])\s+([A-Z][^\n]+)')

pdf_chapters = []
for p_idx, p_txt in enumerate(pages_text):
    for m in ch_header_re.finditer(p_txt):
        ch_id = m.group(1)
        ch_title = m.group(2).strip()
        # filter out stray matches (like table of contents on page 2-3)
        if p_idx >= 5:
            pdf_chapters.append({
                "page": p_idx + 1,
                "ch_id": ch_id,
                "title": ch_title
            })

print(f"Found {len(pdf_chapters)} chapter occurrences in PDF pages 6-274:")
for ch in pdf_chapters:
    print(f"  Page {ch['page']:3d}: Chapter {ch['ch_id']} - {ch['title'][:55]}")

print("\n=== Now Finding the Problem Numbers Under Each Chapter in PDF ===")
# For each detected chapter, find the problem numbers between its start and the next chapter's start
for i in range(len(pdf_chapters)):
    curr_ch = pdf_chapters[i]
    next_ch = pdf_chapters[i+1] if i + 1 < len(pdf_chapters) else None
    
    start_p = curr_ch["page"] - 1
    end_p = next_ch["page"] if next_ch else 274
    
    combined = ""
    for p in range(start_p, end_p):
        combined += "\n" + pages_text[p]
    
    # If next_ch is on the same or next page, truncate at next_ch title
    if next_ch:
        ch_marker = next_ch["ch_id"]
        if ch_marker in combined:
            combined = combined.split(ch_marker)[0]
            
    # Find all problem numbers in this section
    prob_nums = [int(x) for x in re.findall(r'(?:^|\n)\s*(\d{1,4})\.\s+', combined)]
    # Filter out potential spurious numbers
    if prob_nums:
        first_prob = prob_nums[0]
        last_prob = prob_nums[-1]
        print(f"Chapter {curr_ch['ch_id']:5s} (Page {curr_ch['page']:3d}): Problems {first_prob} .. {last_prob} (Count: {len(prob_nums)})")
    else:
        print(f"Chapter {curr_ch['ch_id']:5s} (Page {curr_ch['page']:3d}): No problems detected!")
