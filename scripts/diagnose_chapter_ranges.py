"""
diagnose_chapter_ranges.py
Finds the exact first problem number for every chapter directly from
ARIHANT IE IRODOV NEW EDITION.pdf by locating each chapter header
and searching forward for the first numbered problem.
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
reader = pypdf.PdfReader(str(BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"))

# Chapter header regex: "1.2 The Fundamental Equation..."
ch_re = re.compile(r'(?:^|\n)\s*([1-6]\.[1-8])\s+([A-Z][^\n]+)')

headers_found = []
for p in range(6, 274):
    txt = (reader.pages[p].extract_text() or '').replace('□', ' ')
    for m in ch_re.finditer(txt):
        ch_id = m.group(1)
        ch_title = m.group(2).strip()
        # Clean title
        ch_title = re.sub(r'●.*', '', ch_title).strip()
        headers_found.append({
            "page": p + 1,
            "page_idx": p,
            "pos": m.end(),
            "ch_id": ch_id,
            "title": ch_title
        })

print(f"Total headers located: {len(headers_found)}")

# Sort by page and position
headers_found.sort(key=lambda x: (x["page_idx"], x["pos"]))

# Dedup if same ch_id appears on same page
unique_headers = []
for h in headers_found:
    if not unique_headers or unique_headers[-1]["ch_id"] != h["ch_id"]:
        unique_headers.append(h)

print(f"Unique chapters located: {len(unique_headers)}\n")

# For each chapter, extract text up to next chapter (or 5 pages forward)
for i in range(len(unique_headers)):
    h = unique_headers[i]
    next_h = unique_headers[i+1] if i + 1 < len(unique_headers) else None
    
    start_p = h["page_idx"]
    end_p = min(next_h["page_idx"] + 1 if next_h else 274, start_p + 15)
    
    text_chunk = ""
    for p in range(start_p, end_p):
        txt = (reader.pages[p].extract_text() or '').replace('□', ' ')
        if p == start_p:
            txt = txt[h["pos"]:]
        text_chunk += "\n" + txt
        
    if next_h and next_h["ch_id"] in text_chunk:
        text_chunk = text_chunk.split(next_h["ch_id"])[0]
        
    # Find all problem numbers
    probs = [int(x) for x in re.findall(r'(?:^|\n)\s*(\d{1,4})\.\s+', text_chunk)]
    first_p = probs[0] if probs else None
    last_p = probs[-1] if probs else None
    count = len(probs)
    print(f"Chapter {h['ch_id']:5s} (p.{h['page']:3d}): {first_p} .. {last_p} (found {count:3d}) | Title: {h['title'][:45]}")
