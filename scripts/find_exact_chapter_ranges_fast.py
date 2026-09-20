"""
find_exact_chapter_ranges_fast.py
Optimized scanner to pinpoint the exact problem boundaries for all 37 chapters.
"""

import re
import sys
from pathlib import Path
import pypdf

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = Path(__file__).resolve().parent.parent
pdf_path = BASE_DIR / "ARIHANT IE IRODOV NEW EDITION.pdf"
reader = pypdf.PdfReader(str(pdf_path))

# TOC Chapters with Book Pages (Book page + 6 = PDF page)
TOC_ITEMS = [
    # Part 1
    {"part": 1, "id": "1.1", "title": "Kinematics", "book_page": 1},
    {"part": 1, "id": "1.2", "title": "The Fundamental Equation of Dynamics", "book_page": 10},
    {"part": 1, "id": "1.3", "title": "Laws of Conservation of Energy, Momentum, and Angular Momentum", "book_page": 19},
    {"part": 1, "id": "1.4", "title": "Universal Gravitation", "book_page": 33},
    {"part": 1, "id": "1.5", "title": "Dynamics of a Solid Body", "book_page": 36},
    {"part": 1, "id": "1.6", "title": "Elastic Deformations of a Solid Body", "book_page": 47},
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

# For each chapter, book_page + 6 is the estimated PDF page (0-indexed: book_page + 5)
results = []
for idx, ch in enumerate(TOC_ITEMS):
    est_p = ch["book_page"] + 5 # 0-based
    # Search within [est_p - 1, est_p + 2]
    found_page = None
    first_prob = None
    
    # We want to find the heading and the first problem following it
    for p in range(max(0, est_p - 2), min(len(reader.pages), est_p + 3)):
        txt = (reader.pages[p].extract_text() or '').replace('□', ' ')
        # look for heading like "1.2." or "1.2 "
        pattern = r'(?:^|\n)\s*' + re.escape(ch["id"]) + r'[\.\s]+'
        m = re.search(pattern, txt)
        if m:
            found_page = p
            after_heading = txt[m.end():]
            # find first problem after heading e.g. "1.59." or "59."
            # In Irodov, questions under chapter 1.2 start either with "1.59." or "59."
            # Let's search for the first number starting a paragraph/line
            # Part number is ch["part"]
            part_num = ch["part"]
            prob_match = re.search(r'(?:^|\n)\s*(?:' + str(part_num) + r'\.)?(\d{1,4})\.\s+', after_heading)
            if prob_match:
                first_prob = int(prob_match.group(1))
            else:
                # maybe on the next page?
                next_txt = (reader.pages[p+1].extract_text() or '').replace('□', ' ')
                pm2 = re.search(r'(?:^|\n)\s*(?:' + str(part_num) + r'\.)?(\d{1,4})\.\s+', next_txt)
                if pm2:
                    first_prob = int(pm2.group(1))
            break
            
    ch["pdf_page_0"] = found_page
    ch["first_prob"] = first_prob
    print(f"Ch {ch['id']:4s} | Book p.{ch['book_page']:3d} | Found PDF p.{found_page+1 if found_page is not None else -1:3d} | First prob: {ch['part']}.{first_prob if first_prob else '?'}")

