import json
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CATALOG = {
    "parts": [
        {
            "id": 1,
            "title": "Physical Fundamentals of Mechanics",
            "total_questions": 388,
            "chapters": [
                {"id": "1.1", "title": "Kinematics", "range": "1.1 - 1.58", "count": 58, "start": 1, "end": 58},
                {"id": "1.2", "title": "The Fundamental Equation of Dynamics", "range": "1.59 - 1.117", "count": 59, "start": 59, "end": 117},
                {"id": "1.3", "title": "Laws of Conservation of Energy, Momentum, and Angular Momentum", "range": "1.118 - 1.199", "count": 82, "start": 118, "end": 199},
                {"id": "1.4", "title": "Universal Gravitation", "range": "1.200 - 1.233", "count": 34, "start": 200, "end": 233},
                {"id": "1.5", "title": "Dynamics of a Solid Body", "range": "1.234 - 1.289", "count": 56, "start": 234, "end": 289},
                {"id": "1.6", "title": "Elastic Deformations of a Solid Body", "range": "1.290 - 1.314", "count": 25, "start": 290, "end": 314},
                {"id": "1.7", "title": "Hydrodynamics", "range": "1.315 - 1.339", "count": 25, "start": 315, "end": 339},
                {"id": "1.8", "title": "Relativistic Mechanics", "range": "1.340 - 1.388", "count": 49, "start": 340, "end": 388}
            ]
        },
        {
            "id": 2,
            "title": "Thermodynamics and Molecular Physics",
            "total_questions": 257,
            "chapters": [
                {"id": "2.1", "title": "Equation of the Gas State. Processes", "range": "2.1 - 2.25", "count": 25, "start": 1, "end": 25},
                {"id": "2.2", "title": "The First Law of Thermodynamics. Heat Capacity", "range": "2.26 - 2.61", "count": 36, "start": 26, "end": 61},
                {"id": "2.3", "title": "Kinetic Theory of Gases. Boltzmann's Law and Maxwell's Distribution", "range": "2.62 - 2.112", "count": 51, "start": 62, "end": 112},
                {"id": "2.4", "title": "The Second Law of Thermodynamics. Entropy", "range": "2.113 - 2.159", "count": 47, "start": 113, "end": 159},
                {"id": "2.5", "title": "Liquids. Capillary Effects", "range": "2.160 - 2.184", "count": 25, "start": 160, "end": 184},
                {"id": "2.6", "title": "Phase Transformations", "range": "2.185 - 2.219", "count": 35, "start": 185, "end": 219},
                {"id": "2.7", "title": "Transport Phenomena", "range": "2.220 - 2.257", "count": 38, "start": 220, "end": 257}
            ]
        },
        {
            "id": 3,
            "title": "Electrodynamics",
            "total_questions": 398,
            "chapters": [
                {"id": "3.1", "title": "Constant Electric Field in Vacuum", "range": "3.1 - 3.53", "count": 53, "start": 1, "end": 53},
                {"id": "3.2", "title": "Conductors and Dielectrics in an Electric Field", "range": "3.54 - 3.100", "count": 47, "start": 54, "end": 100},
                {"id": "3.3", "title": "Electric Capacitance. Energy of an Electric Field", "range": "3.101 - 3.146", "count": 46, "start": 101, "end": 146},
                {"id": "3.4", "title": "Electric Current", "range": "3.147 - 3.218", "count": 72, "start": 147, "end": 218},
                {"id": "3.5", "title": "Constant Magnetic Field. Magnetics", "range": "3.219 - 3.287", "count": 69, "start": 219, "end": 287},
                {"id": "3.6", "title": "Electromagnetic Induction. Maxwell's Equations", "range": "3.288 - 3.371", "count": 84, "start": 288, "end": 371},
                {"id": "3.7", "title": "Motion of Charged Particles in Electric and Magnetic Fields", "range": "3.372 - 3.398", "count": 27, "start": 372, "end": 398}
            ]
        },
        {
            "id": 4,
            "title": "Oscillations and Waves",
            "total_questions": 238,
            "chapters": [
                {"id": "4.1", "title": "Mechanical Oscillations", "range": "4.1 - 4.93", "count": 93, "start": 1, "end": 93},
                {"id": "4.2", "title": "Electric Oscillations", "range": "4.94 - 4.149", "count": 56, "start": 94, "end": 149},
                {"id": "4.3", "title": "Elastic Waves. Acoustics", "range": "4.150 - 4.188", "count": 39, "start": 150, "end": 188},
                {"id": "4.4", "title": "Electromagnetic Waves. Radiation", "range": "4.189 - 4.238", "count": 50, "start": 189, "end": 238}
            ]
        },
        {
            "id": 5,
            "title": "Optics",
            "total_questions": 275,
            "chapters": [
                {"id": "5.1", "title": "Photometry and Geometrical Optics", "range": "5.1 - 5.63", "count": 63, "start": 1, "end": 63},
                {"id": "5.2", "title": "Interference of Light", "range": "5.64 - 5.96", "count": 33, "start": 64, "end": 96},
                {"id": "5.3", "title": "Diffraction of Light", "range": "5.97 - 5.156", "count": 60, "start": 97, "end": 156},
                {"id": "5.4", "title": "Polarization of Light", "range": "5.157 - 5.199", "count": 43, "start": 157, "end": 199},
                {"id": "5.5", "title": "Dispersion and Absorption of Light", "range": "5.200 - 5.223", "count": 24, "start": 200, "end": 223},
                {"id": "5.6", "title": "Optics of Moving Sources", "range": "5.224 - 5.245", "count": 22, "start": 224, "end": 245},
                {"id": "5.7", "title": "Thermal Radiation. Quantum Nature of Light", "range": "5.246 - 5.275", "count": 30, "start": 246, "end": 275}
            ]
        },
        {
            "id": 6,
            "title": "Atomic and Nuclear Physics",
            "total_questions": 310,
            "chapters": [
                {"id": "6.1", "title": "Scattering of Particles. Rutherford-Bohr Atom", "range": "6.1 - 6.48", "count": 48, "start": 1, "end": 48},
                {"id": "6.2", "title": "Wave Properties of Particles. Schrodinger Equation", "range": "6.49 - 6.96", "count": 48, "start": 49, "end": 96},
                {"id": "6.3", "title": "Properties of Atoms. Spectra", "range": "6.97 - 6.166", "count": 70, "start": 97, "end": 166},
                {"id": "6.4", "title": "Molecules and Crystals", "range": "6.167 - 6.213", "count": 47, "start": 167, "end": 213},
                {"id": "6.5", "title": "Radioactivity", "range": "6.214 - 6.248", "count": 35, "start": 214, "end": 248},
                {"id": "6.6", "title": "Nuclear Reactions", "range": "6.249 - 6.290", "count": 42, "start": 249, "end": 290},
                {"id": "6.7", "title": "Elementary Particles", "range": "6.291 - 6.310", "count": 20, "start": 291, "end": 310}
            ]
        }
    ]
}

total_probs = 0
total_chapters = 0
for part in CATALOG["parts"]:
    p_sum = 0
    total_chapters += len(part["chapters"])
    for ch in part["chapters"]:
        expected_count = ch["end"] - ch["start"] + 1
        assert ch["count"] == expected_count, f"Mismatch in {ch['id']}: count {ch['count']} vs {expected_count}"
        p_sum += ch["count"]
    assert p_sum == part["total_questions"], f"Part {part['id']} sum {p_sum} != {part['total_questions']}"
    total_probs += p_sum
    print(f"Part {part['id']}: {part['title']} -> {len(part['chapters'])} chapters, {p_sum} problems")

print(f"\nAll assertions passed! Total Chapters: {total_chapters}, Total Problems: {total_probs}")
