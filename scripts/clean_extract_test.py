import pypdf
import sys
import logging
import warnings

# Suppress warnings and logger
warnings.filterwarnings("ignore")
logging.getLogger("pypdf").setLevel(logging.ERROR)
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

reader = pypdf.PdfReader("ARIHANT IE IRODOV NEW EDITION.pdf")
text_p7 = reader.pages[6].extract_text()
text_p8 = reader.pages[7].extract_text()

print("Page 7 length:", len(text_p7))
print("Page 8 length:", len(text_p8))
print("\n--- Clean Page 8 Sample ---")
print(text_p8[:600])
