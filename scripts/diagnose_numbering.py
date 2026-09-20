import pypdf
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
reader = pypdf.PdfReader("ARIHANT IE IRODOV NEW EDITION.pdf")

# Check pages 7 to 20 for problem number patterns
print("Checking problem headers on pages 7 to 15:")
for p in range(6, 15):
    txt = reader.pages[p].extract_text() or ""
    # Find lines starting with numbers like "1.", "10.", "58."
    matches = re.findall(r"(?:^|\n)\s*(\d{1,4})\.\s+([A-Z][^\n]{10,80})", txt)
    if matches:
        print(f"\n--- Page {p+1} ---")
        for num, title in matches[:4]:
            print(f"  [{num}] {title[:60]}")

# Also check how parts are titled
for p in range(5, 50):
    txt = reader.pages[p].extract_text() or ""
    if "PART" in txt.upper():
        for line in txt.split("\n"):
            if "PART" in line.upper():
                print(f"Part header on page {p+1}: {line.strip()}")
