"""
find_exact_chapter_ranges.py
Calculates the exact problem ranges for all 37 chapters of Irodov
by reading the text between each chapter's starting page and the next chapter's starting page.
"""

import json
import logging
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

# TOC Chapters with Book Pages
TOC_ITEMS = [
    # Part 1
    {"part": 1, "id": "1.1", "title": "Kinematics", "book_page": 1},
    {"part": 1, "id": "1.2", "title": "The Fundamental Equation of Dynamics", "book_page": 10},
    {"part": 1, "id": "1.3", "title": "Laws of Conservation of Energy, Momentum, and Angular Momentum", "book_page": 19},
    {"part": 1, "id": "1.4", "title": "Universal Gravitation", "book_page": 33},
    {"part": 1, "id": "1.5", "title": "Dynamics of a Solid Body", "book_page": 36},
    {"part": 1, "id": "1.6", "title": "Elastic Deformations of a Solid Body", "book_page": 47}, # let's verify page
    {"part": 1, "id": "1.7", "title": "Hydrodynamics", "book_page": 50},
    {"part": 1, "id": "1.8", "title": "Relativistic Mechanics", "book_page": 55},
    # Part 2
    {"part": 2, "id": "2.1", "title": "Equation of the Gas State. Processes", "book_page": 62},
    {"part": 2, "id": "2.2", "title": "The First Law of Thermodynamics. Heat Capacity", "book_page": 65},
    {"part": 2, "id": "2.3", "title": "Kinetic Theory of Gases. Boltzmann's Law and Maxwell's Distribution", "book_page": 69},
    {"part": 2, "id": "2.4", "title": "The Second Law of Thermodynamics. Entropy", "book_page": 75},
    {"part": 2, "id": "2.5", "title": "Liquids. Capillary Effects", "book_page": 81},
    {"part": 2, "id": "2.6", "title": "Phase Transformations", "book_page": 83},
    {"part": 2, "id": "2.7", "title": "Transport Phenomena", "book_page": 87},
    # Part 3
    {"part": 3, "id": "3.1", "title": "Constant Electric Field in Vacuum", "book_page": 92},
    {"part": 3, "id": "3.2", "title": "Conductors and Dielectrics in an Electric Field", "book_page": 98},
    {"part": 3, "id": "3.3", "title": "Electric Capacitance. Energy of an Electric Field", "book_page": 105},
    {"part": 3, "id": "3.4", "title": "Electric Current", "book_page": 112},
    {"part": 3, "id": "3.5", "title": "Constant Magnetic Field. Magnetics", "book_page": 123},
    {"part": 3, "id": "3.6", "title": "Electromagnetic Induction. Maxwell's Equations", "book_page": 134},
    {"part": 3, "id": "3.7", "title": "Motion of Charged Particles in Electric and Magnetic Fields", "book_page": 147},
    # Part 4
    {"part": 4, "id": "4.1", "title": "Mechanical Oscillations", "book_page": 153},
    {"part": 4, "id": "4.2", "title": "Electric Oscillations", "book_page": 167},
    {"part": 4, "id": "4.3", "title": "Elastic Waves. Acoustics", "book_page": 175},
    {"part": 4, "id": "4.4", "title": "Electromagnetic Waves. Radiation", "book_page": 180},
    # Part 5
    {"part": 5, "id": "5.1", "title": "Photometry and Geometrical Optics", "book_page": 186},
    {"part": 5, "id": "5.2", "title": "Interference of Light", "book_page": 197},
    {"part": 5, "id": "5.3", "title": "Diffraction of Light", "book_page": 202},
    {"part": 5, "id": "5.4", "title": "Polarization of Light", "book_page": 213},
    {"part": 5, "id": "5.5", "title": "Dispersion and Absorption of Light", "book_page": 220},
    {"part": 5, "id": "5.6", "title": "Optics of Moving Sources", "book_page": 223},
    {"part": 5, "id": "5.7", "title": "Thermal Radiation. Quantum Nature of Light", "book_page": 226},
    # Part 6
    {"part": 6, "id": "6.1", "title": "Scattering of Particles. Rutherford-Bohr Atom", "book_page": 232},
    {"part": 6, "id": "6.2", "title": "Wave Properties of Particles. Schrodinger Equation", "book_page": 237},
    {"part": 6, "id": "6.3", "title": "Properties of Atoms. Spectra", "book_page": 243},
    {"part": 6, "id": "6.4", "title": "Molecules and Crystals", "book_page": 250},
    {"part": 6, "id": "6.5", "title": "Radioactivity", "book_page": 256},
    {"part": 6, "id": "6.6", "title": "Nuclear Reactions", "book_page": 260},
    {"part": 6, "id": "6.7", "title": "Elementary Particles", "book_page": 265}
]

# We need to find for each chapter:
# 1. Where in the PDF does this chapter actually appear (search for ch_id + title)
# 2. What is the FIRST problem number and LAST problem number under it!

print("Scanning for exact chapter headings in PDF...")
for item in TOC_ITEMS:
    cid = item["id"]
    part = item["part"]
    
    # Search around estimated page
    found_page = None
    for p in range(6, 274):
        txt = (reader.pages[p].extract_text() or '').replace('□', ' ')
        # Match chapter number e.g. "1.2 " or "1.2."
        if re.search(r'(?:^|\n)\s*' + re.escape(cid) + r'[\.\s]+', txt):
            found_page = p + 1
            break
    item["pdf_page"] = found_page

for item in TOC_ITEMS:
    print(f"Chapter {item['id']:5s} | Book p.{item['book_page']:3d} | Found at PDF p.{item['pdf_page']}")
