# I.E. Irodov - Problems in General Physics Question Bank & Solver

A modern, high-performance question bank, interactive solver, and practice testing suite built around I.E. Irodov's classic physics treatise: **"Problems in General Physics"** (1,877 problems across 6 parts and 36 chapters).

Designed for advanced physics students, competitive exam candidates (JEE Advanced, Physics Olympiad / IPhO, GRE Physics), and educators.

---

## Features

- **Authoritative Book Catalog**:
  - Full structure of all 6 parts and 36 chapters covering all 1,877 problems.
  - Part 1: Physical Fundamentals of Mechanics (Kinematics, Dynamics, Conservation Laws, Gravitation, Solid Body, Elasticity, Hydrodynamics, Relativistic Mechanics)
  - Part 2: Thermodynamics and Molecular Physics (Gas Equations, 1st Law, Kinetic Theory, 2nd Law & Entropy, Liquids & Capillarity, Phase Transitions, Transport)
  - Part 3: Electrodynamics (Electric Field in Vacuum, Dielectrics, Capacitance, Electric Current, Magnetic Field, Induction & Maxwell's Equations, Charged Particles)
  - Part 4: Oscillations and Waves (Mechanical Oscillations, Electric Oscillations, Elastic Waves & Acoustics, Electromagnetic Waves)
  - Part 5: Optics (Geometrical Optics, Interference, Diffraction, Polarization, Dispersion & Absorption, Moving Sources)
  - Part 6: Atomic and Nuclear Physics (Rutherford-Bohr Atom, Schrödinger Equation, Atomic Spectra, Radioactivity, Nuclear Reactions, Elementary Particles)

- **Rich Mathematical Typography**:
  - Full KaTeX LaTeX rendering for complex integrals, vector algebra, differential equations, and scientific units.

- **Progressive Disclosure & Solver**:
  - **💡 Progressive Hints**: Step-by-step conceptual hints without spoiling the answer.
  - **🎯 Final Answer**: Exact symbolic formula and numerical answer.
  - **📝 Detailed Step-by-Step Solution**: Rigorous analytical derivations and calculations.
  - **🤖 AI Solver Prompt Generator**: One-click copy of precision prompts for LLM physics solvers.

- **Timed Practice & Test Simulator**:
  - Configurable exams by Part, number of questions (3, 5, 8, 12), and timer duration.
  - Scratchpad for writing formulas and self-assessment scoring.

- **Interactive Formula Reference Sheet**:
  - Searchable collection of essential formulas, moments of inertia, boundary conditions, and physical constants with copyable LaTeX.

- **Progress Tracking & Scratchpad**:
  - Mark questions as Solved (🟢), In Progress (🟡), Starred (⭐), or Unsolved.
  - Built-in personal scratchpad notes saved locally in your browser.

- **Python CLI & SQLite Database**:
  - Standalone SQLite database (`data/irodov.db`) and command-line tool (`irodov_cli.py`).
  - Search, view solutions, pick random practice problems, and export printable Markdown worksheets.

---

## Quick Start

### 1. Interactive Web Application

Start the local development server:
```bash
npm run dev
```
Or build and preview the production application:
```bash
npm run build
npm run preview
```
Open your browser at `http://localhost:5173` (or the port displayed in your terminal).

---

### 2. Python CLI Tool

The CLI tool allows you to interact with the question bank directly from your terminal:

```bash
# View book table of contents and question distribution
python irodov_cli.py list

# View problem 1.13 with hints and full step-by-step solution
python irodov_cli.py get 1.13 --all

# View problem 1.100 with only hints
python irodov_cli.py get 1.100 --hint

# Search questions by keyword or tag (e.g. 'cylinder', 'entropy', 'relative-velocity')
python irodov_cli.py search "cylinder"

# Get a random practice problem from Mechanics
python irodov_cli.py random --part 1 --quiz

# Mark a problem as solved or starred
python irodov_cli.py status 1.13 solved --notes "Solved using parametric differentiation"
python irodov_cli.py status 1.100 starred

# View your overall progress and completion statistics
python irodov_cli.py stats

# Export a customized Markdown practice worksheet / test paper
python irodov_cli.py export --part 1 --count 5 --out mechanics_test.md --include-hints --include-solutions
```

---

## Project Structure

```
├── backend/
│   └── db.py                 # SQLite database layer and schema
├── data/
│   ├── irodov.db             # Pre-seeded SQLite database
│   ├── irodov_catalog.json   # Full syllabus structure (6 parts, 36 chapters)
│   └── questions_seed.json   # Seed bank of hallmark problems with LaTeX
├── src/
│   ├── components/
│   │   ├── FormulaSheet.jsx  # High-yield physics formula reference modal
│   │   ├── MathRenderer.jsx  # KaTeX LaTeX formula rendering component
│   │   ├── Navbar.jsx        # Top navigation, search, and theme switcher
│   │   ├── PracticeMode.jsx  # Timed quiz & practice exam simulator
│   │   ├── QuestionCard.jsx  # Interactive question card with hints & solutions
│   │   ├── Sidebar.jsx       # Syllabus explorer and filter tree
│   │   └── StatsModal.jsx    # Progress analytics modal
│   ├── App.jsx               # Main React application
│   ├── index.css             # Tailwind styling and custom scrollbars
│   └── main.jsx              # Application entry point
├── dist/                     # Optimized production bundle
├── irodov_cli.py             # Python command-line utility
├── package.json              # Web app dependencies and scripts
└── vite.config.js            # Vite build configuration
```
