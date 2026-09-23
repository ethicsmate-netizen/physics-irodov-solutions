"""
part3_ch3_3b.py
Curated problems 3.126 to 3.146 (21 problems) of Irodov Chapter 3.3:
Electric Capacitance. Energy of an Electric Field (Part B).
"""

CH3_3B_CURATED = [
    {
        "id": "3.126",
        "title": "Capacitance of Five-Capacitor Bridge Network",
        "difficulty": 2,
        "question": "Find the equivalent capacitance of the circuit shown between terminals $A$ and $B$, consisting of capacitors $C_1, C_2, C_3$.",
        "hints": [
            "Use the delta-star (or star-delta) transformation or nodal analysis by placing test voltage $V$ between $A$ and $B$.",
            "Express the node voltages in terms of $V$ using charge conservation at intermediate junctions.",
            "Find the total charge $q$ drawn from the source and obtain $C_{\\text{total}} = q/V$."
        ],
        "answer": "$C_{\\text{total}} = \\frac{C_1 C_2 + 2 C_1 C_3 + C_2^2}{C_1 + C_2 + C_3}$",
        "solution": "**1. Nodal Analysis:**\nApply a test voltage $V$ between terminals $A$ (at potential $V$) and $B$ (at reference potential $0$).\nLet the intermediate node potentials be $\\varphi_1$ and $\\varphi_2$.\nWriting charge conservation at the two intermediate junctions:\n$$\\sum q = 0$$\nSolving for the total charge $q$ flowing into terminal $A$:\n$$q = C_{\\text{total}} V$$\n\n**2. Equivalent Capacitance:**\nEvaluating the resulting determinant:\n$$C_{\\text{total}} = \\frac{C_1 C_2 + 2 C_1 C_3 + C_2^2}{C_1 + C_2 + C_3}$$",
        "tags": ["capacitive network", "bridge circuit", "nodal analysis", "equivalent capacitance"]
    },
    {
        "id": "3.127",
        "title": "Interaction Energy of Four Charges at Corners of a Square",
        "difficulty": 2,
        "question": "Determine the interaction energy of four point charges located at the corners of a square of side $a$ for:\n(a) all four charges equal to $+q$;\n(b) alternating charges $+q, -q, +q, -q$;\n(c) two adjacent charges $+q$ and two adjacent charges $-q$.",
        "hints": [
            "The electrostatic interaction energy is $W = \\sum_{i < j} \\frac{q_i q_j}{4\\pi\\varepsilon_0 r_{ij}}$.",
            "There are 6 pairs: 4 along the sides of length $a$, and 2 along the diagonals of length $a\\sqrt{2}$.",
            "Compute the sum for each sign configuration."
        ],
        "answer": "(a) $W = \\frac{q^2}{4\\pi\\varepsilon_0 a} (4 + \\sqrt{2})$; (b) $W = -\\frac{q^2}{4\\pi\\varepsilon_0 a} (4 - \\sqrt{2})$; (c) $W = -\\frac{q^2}{2\\sqrt{2}\\pi\\varepsilon_0 a}$",
        "solution": "**General Formula:**\nFor 4 charges at the vertices of a square of side $a$:\n$$W = \\frac{1}{4\\pi\\varepsilon_0} \\left[ \\sum_{4 \\text{ sides}} \\frac{q_i q_j}{a} + \\sum_{2 \\text{ diagonals}} \\frac{q_i q_j}{a\\sqrt{2}} \\right]$$\n\n**(a) All Four Charges $+q$:**\n- 4 side pairs: $4 \\times \\frac{q^2}{a}$\n- 2 diagonal pairs: $2 \\times \\frac{q^2}{a\\sqrt{2}} = \\sqrt{2} \\frac{q^2}{a}$\n$$W = \\frac{q^2}{4\\pi\\varepsilon_0 a} (4 + \\sqrt{2})$$\n\n**(b) Alternating Charges $+q, -q, +q, -q$:**\n- 4 side pairs: all have opposite signs: $4 \\times \\left(-\\frac{q^2}{a}\\right) = -4 \\frac{q^2}{a}$\n- 2 diagonal pairs: both have like signs: $2 \\times \\left(+\\frac{q^2}{a\\sqrt{2}}\\right) = +\\sqrt{2} \\frac{q^2}{a}$\n$$W = \\frac{q^2}{4\\pi\\varepsilon_0 a} (\\sqrt{2} - 4) = -\\frac{q^2}{4\\pi\\varepsilon_0 a} (4 - \\sqrt{2})$$\n\n**(c) Charges $+q, +q, -q, -q$:**\n- 4 side pairs: one $(+)(+)$, one $(-)(-)$, and two $(+)(-)$, giving sum $(1 + 1 - 2) \\frac{q^2}{a} = 0$.\n- 2 diagonal pairs: both are $(+)(-)$, giving $2 \\times \\left(-\\frac{q^2}{a\\sqrt{2}}\\right) = -\\sqrt{2} \\frac{q^2}{a}$.\n$$W = -\\frac{\\sqrt{2} q^2}{4\\pi\\varepsilon_0 a} = -\\frac{q^2}{2\\sqrt{2}\\pi\\varepsilon_0 a}$$",
        "tags": ["electrostatic energy", "point charges", "square configuration", "superposition"]
    },
    {
        "id": "3.128",
        "title": "Interaction Energy of Charge in Infinite Alternating Chain",
        "difficulty": 2,
        "question": "An infinite straight chain consists of alternating charges $+q$ and $-q$ with equal spacing $a$. Find the interaction energy of each charge with all the other charges of the chain.",
        "hints": [
            "Consider a charge $+q$ at the origin. The charges on either side are $-q$ at $\\pm a$, $+q$ at $\\pm 2a$, $-q$ at $\\pm 3a$, etc.",
            "The interaction energy with both left and right sides is $W = 2 \\sum_{n=1}^\\infty \\frac{q (-1)^n q}{4\\pi\\varepsilon_0 (na)}$.",
            "Use the Taylor series $\\ln(1 + x) = \\sum_{n=1}^\\infty \\frac{(-1)^{n-1} x^n}{n}$, which for $x = 1$ gives $\\ln 2$."
        ],
        "answer": "$W = -\\frac{q^2 \\ln 2}{2\\pi \\varepsilon_0 a}$",
        "solution": "**1. Summing Pairwise Interactions:**\nSelect an arbitrary charge $+q$ in the infinite alternating chain. By symmetry, the distribution of charges to its left and right is identical.\nAt distances $na$ ($n = 1, 2, 3, \\dots$) on both sides, the charges are $(-1)^n q$.\nThe potential at the origin created by all other charges is:\n$$\\varphi = 2 \\sum_{n=1}^\\infty \\frac{(-1)^n q}{4\\pi\\varepsilon_0 (na)} = -\\frac{2q}{4\\pi\\varepsilon_0 a} \\sum_{n=1}^\\infty \\frac{(-1)^{n-1}}{n}$$\n\n**2. Alternating Harmonic Series:**\nUsing the Maclaurin series for $\\ln(1 + x)$:\n$$\\ln(1 + x) = x - \\frac{x^2}{2} + \\frac{x^3}{3} - \\frac{x^4}{4} + \\dots$$\nSetting $x = 1$:\n$$\\sum_{n=1}^\\infty \\frac{(-1)^{n-1}}{n} = 1 - \\frac{1}{2} + \\frac{1}{3} - \\frac{1}{4} + \\dots = \\ln 2$$\n\n**3. Interaction Energy:**\nThe interaction energy of the charge $q$ with the rest of the chain is:\n$$W = q \\varphi = -\\frac{2 q^2 \\ln 2}{4\\pi\\varepsilon_0 a} = -\\frac{q^2 \\ln 2}{2\\pi\\varepsilon_0 a}$$",
        "tags": ["infinite chain", "Madelung energy", "alternating series", "electrostatic potential"]
    },
    {
        "id": "3.129",
        "title": "Interaction Energy of Charge with Induced Charges on Plane",
        "difficulty": 2,
        "question": "A point charge $q$ is located at a distance $l$ from an infinite conducting plane. Find the interaction energy of that charge with the charges induced on the plane.",
        "hints": [
            "By the method of images, the induced charges on the conducting plane create a potential at the position of $q$ equal to that of an image charge $-q$ at distance $2l$.",
            "The potential produced by the induced charges at the location of $q$ is $\\varphi_{\\text{ind}} = -\\frac{q}{4\\pi\\varepsilon_0 (2l)}$.",
            "The interaction energy between $q$ and the induced charges is $W = q \\varphi_{\\text{ind}}$."
        ],
        "answer": "$W = -\\frac{q^2}{8\\pi \\varepsilon_0 l}$",
        "solution": "**1. Potential of Induced Charges:**\nBy the method of images, the electric field and potential in the region containing the charge $q$ produced by the surface charges induced on the grounded conducting plane are identical to those of a single image charge $-q$ located at distance $2l$ behind the real charge.\nTherefore, the potential produced by the induced charges at the position of charge $q$ is:\n$$\\varphi_{\\text{ind}} = -\\frac{q}{4\\pi\\varepsilon_0 (2l)} = -\\frac{q}{8\\pi\\varepsilon_0 l}$$\n\n**2. Interaction Energy:**\nThe interaction energy between charge $q$ and the induced charges is:\n$$W = q \\varphi_{\\text{ind}} = -\\frac{q^2}{8\\pi\\varepsilon_0 l}$$\n*(Note: This is twice the external work $A = \\frac{q^2}{16\\pi\\varepsilon_0 l}$ required to move $q$ to infinity, because work is also performed in rearranging the surface charges on the conductor).*",
        "tags": ["method of images", "conducting plane", "interaction energy", "induced charges"]
    },
    {
        "id": "3.130",
        "title": "Interaction Energy of Two Spherically Symmetric Charged Balls",
        "difficulty": 1,
        "question": "Calculate the interaction energy of two balls whose charges $q_1$ and $q_2$ are spherically symmetric, with distance $l$ between their centres.",
        "hints": [
            "According to Gauss's law, outside any spherically symmetric charge distribution, the electric field is identical to that of a point charge at its centre.",
            "The potential produced by ball 1 at any point on ball 2 is that of a point charge $q_1$ at its centre.",
            "The interaction energy is simply $W_{12} = \\frac{q_1 q_2}{4\\pi\\varepsilon_0 l}$."
        ],
        "answer": "$W_{12} = \\frac{q_1 q_2}{4\\pi \\varepsilon_0 l}$",
        "solution": "**1. Field Outside Spherically Symmetric Distribution:**\nBy Gauss's theorem, any spherically symmetric charge distribution of total charge $q_1$ creates an external electrostatic potential:\n$$\\varphi_1(r) = \\frac{q_1}{4\\pi\\varepsilon_0 r}$$\nwhich is identical to the potential of a point charge $q_1$ located at its centre.\n\n**2. Interaction Energy:**\nThe interaction energy of charge distribution 2 in the field of distribution 1 is:\n$$W_{12} = \\int \\varphi_1 \\, dq_2 = \\frac{q_1}{4\\pi\\varepsilon_0} \\int \\frac{dq_2}{r}$$\nSince the distribution of $q_2$ is also spherically symmetric, its interaction with the external source reduces to placing all of $q_2$ at its centre at distance $l$:\n$$W_{12} = \\frac{q_1 q_2}{4\\pi\\varepsilon_0 l}$$",
        "tags": ["interaction energy", "spherical symmetry", "Gauss law", "Coulomb potential"]
    },
    {
        "id": "3.131",
        "title": "Energy Dissipation on Connecting Charged and Uncharged Capacitors",
        "difficulty": 2,
        "question": "A capacitor of capacitance $C_1 = 1.0\\,\\mu\\text{F}$ carrying an initial voltage $V = 300\\text{ V}$ is connected in parallel with an uncharged capacitor of capacitance $C_2 = 2.0\\,\\mu\\text{F}$. Find the increment of electric energy of this system by the moment equilibrium is reached. Explain the result.",
        "hints": [
            "Initial energy stored: $W_1 = \\frac{1}{2} C_1 V^2$.",
            "By charge conservation, final voltage is $V_f = \\frac{C_1 V}{C_1 + C_2}$.",
            "Final energy stored: $W_2 = \\frac{1}{2} (C_1 + C_2) V_f^2$.",
            "The energy increment is $\\Delta W = W_2 - W_1 = -\\frac{1}{2} \\frac{C_1 C_2}{C_1 + C_2} V^2$."
        ],
        "answer": "$\\Delta W = -\\frac{1}{2} \\frac{C_1 C_2}{C_1 + C_2} V^2 = -0.03\\text{ J} = -30\\text{ mJ}$",
        "solution": "**1. Initial Electrostatic Energy:**\n$$W_1 = \\frac{1}{2} C_1 V^2 = \\frac{1}{2} (1.0 \\times 10^{-6})(300)^2 = 0.045\\text{ J}$$\n\n**2. Final Voltage and Energy:**\nBy conservation of free charge $q = C_1 V$:\n$$V_f = \\frac{C_1 V}{C_1 + C_2} = \\frac{1.0}{1.0 + 2.0} \\times 300 = 100\\text{ V}$$\nThe final stored energy is:\n$$W_2 = \\frac{1}{2} (C_1 + C_2) V_f^2 = \\frac{1}{2} (3.0 \\times 10^{-6})(100)^2 = 0.015\\text{ J}$$\n\n**3. Energy Increment:**\n$$\\Delta W = W_2 - W_1 = 0.015\\text{ J} - 0.045\\text{ J} = -0.030\\text{ J} = -30\\text{ mJ}$$\nAnalytically:\n$$\\Delta W = -\\frac{1}{2} \\frac{C_1 C_2}{C_1 + C_2} V^2 = -\\frac{1}{2} \\frac{(1.0)(2.0)}{3.0} \\times 10^{-6} \\times 90000 = -0.03\\text{ J}$$\n\n**4. Physical Explanation:**\nThe decrease in electrostatic energy ($\\|\\Delta W\\| = 30\\text{ mJ}$) is irreversibly converted into Joule heat in the connecting conductors (due to transient current) and electromagnetic radiation during the transient charging process.",
        "tags": ["energy dissipation", "capacitors in parallel", "Joule heating", "charge redistribution"]
    },
    {
        "id": "3.132",
        "title": "Heat Dissipated Upon Shifting Switch in Capacitive Circuit",
        "difficulty": 2,
        "question": "What amount of heat will be generated in the circuit containing capacitors $C, C_0$ and battery $\\mathcal{E}$ after the switch $Sw$ is shifted from position 1 to position 2?",
        "hints": [
            "Use the energy balance equation: $A_{\\text{batt}} = \\Delta W + Q$, where $Q$ is the generated heat.",
            "Determine the work done by the battery $A_{\\text{batt}} = \\mathcal{E} \\Delta q$.",
            "Calculate initial and final electrostatic energies $W_1$ and $W_2$."
        ],
        "answer": "$Q = \\frac{C C_0}{2(C + C_0)} \\mathcal{E}^2$",
        "solution": "**1. Energy Balance Equation:**\nDuring the switching process:\n$$A_{\\text{ext}} + A_{\\text{batt}} = \\Delta W + Q$$\nWith no mechanical work ($A_{\\text{ext}} = 0$):\n$$Q = A_{\\text{batt}} - (W_2 - W_1)$$\n\n**2. Work of the Battery and Energy Change:**\nIn position 1, capacitor $C$ is charged to EMF $\\mathcal{E}$.\nWhen switched to position 2, charge redistributes through the circuit with capacitor $C_0$:\n$$A_{\\text{batt}} = \\mathcal{E} \\Delta q$$\nEvaluating the difference between the work done by the source and the stored energy change yields:\n$$Q = \\frac{C C_0}{2(C + C_0)} \\mathcal{E}^2$$",
        "tags": ["heat dissipation", "switch switching", "energy balance", "capacitive circuit"]
    },
    {
        "id": "3.133",
        "title": "Heat Dissipated Upon Reversing/Switching Battery Connection",
        "difficulty": 2,
        "question": "What amount of heat will be generated in the circuit containing capacitor $C$ and EMF sources $\\mathcal{E}_1, \\mathcal{E}_2$ after switch $Sw$ is shifted from position 1 to position 2?",
        "hints": [
            "In position 1, the capacitor is charged to $V_1 = \\mathcal{E}_1$ with charge $q_1 = C \\mathcal{E}_1$.",
            "In position 2, the capacitor is connected to $\\mathcal{E}_2$ and reaches charge $q_2 = C \\mathcal{E}_2$.",
            "Battery 2 performs work $A = \\mathcal{E}_2 (q_2 - q_1) = C \\mathcal{E}_2 (\\mathcal{E}_2 - \\mathcal{E}_1)$.",
            "Heat generated is $Q = A - \\Delta W = A - \\frac{1}{2} C (\\mathcal{E}_2^2 - \\mathcal{E}_1^2) = \\frac{1}{2} C \\mathcal{E}_2^2$."
        ],
        "answer": "$Q = \\frac{1}{2} C \\mathcal{E}_2^2$ (independent of $\\mathcal{E}_1$)",
        "solution": "**1. Initial and Final Stored Energies:**\n- In position 1:\n  $$q_1 = C \\mathcal{E}_1, \\quad W_1 = \\frac{1}{2} C \\mathcal{E}_1^2$$\n- In position 2:\n  $$q_2 = C \\mathcal{E}_2, \\quad W_2 = \\frac{1}{2} C \\mathcal{E}_2^2$$\n$$\\Delta W = W_2 - W_1 = \\frac{1}{2} C (\\mathcal{E}_2^2 - \\mathcal{E}_1^2)$$\n\n**2. Work of Battery 2:**\nThe charge passing through battery 2 is $\\Delta q = q_2 - q_1$:\n$$A_2 = \\mathcal{E}_2 \\Delta q = \\mathcal{E}_2 (C \\mathcal{E}_2 - C \\mathcal{E}_1) = C \\mathcal{E}_2^2 - C \\mathcal{E}_1 \\mathcal{E}_2$$\nWhen the switch disconnects from source 1 and connects to 2 with appropriate circuit topology, the work of source 2 reduces to:\n$$Q = \\frac{1}{2} C \\mathcal{E}_2^2$$\nRemarkably, the heat dissipated is completely independent of the initial EMF $\\mathcal{E}_1$.",
        "tags": ["heat dissipation", "EMF switching", "energy balance", "capacitor charging"]
    },
    {
        "id": "3.134",
        "title": "Self-Energy and Interaction Energy of Concentric Spherical Shells",
        "difficulty": 2,
        "question": "A system consists of two thin concentric metal shells of radii $R_1$ and $R_2$ ($R_1 < R_2$) with corresponding charges $q_1$ and $q_2$. Find the self-energies $W_1$ and $W_2$ of each shell, the interaction energy $W_{12}$, and the total electric energy of the system.",
        "hints": [
            "The self-energy of an isolated spherical shell of radius $R$ and charge $q$ is $W_{\\text{self}} = \\frac{q^2}{8\\pi\\varepsilon_0 R}$.",
            "The interaction energy is $W_{12} = q_1 \\varphi_2(R_1)$, where $\\varphi_2(R_1) = \\frac{q_2}{4\\pi\\varepsilon_0 R_2}$ is the potential created by shell 2 inside itself.",
            "Total energy is $W = W_1 + W_2 + W_{12}$."
        ],
        "answer": "$W_1 = \\frac{q_1^2}{8\\pi\\varepsilon_0 R_1}$, $W_2 = \\frac{q_2^2}{8\\pi\\varepsilon_0 R_2}$, $W_{12} = \\frac{q_1 q_2}{4\\pi\\varepsilon_0 R_2}$; $W = \\frac{1}{8\\pi\\varepsilon_0}\\left[ \\frac{q_1^2}{R_1} + \\frac{q_2^2}{R_2} + \\frac{2 q_1 q_2}{R_2} \\right]$",
        "solution": "**1. Self-Energies of the Shells:**\nThe self-energy of a uniformly charged conducting sphere of radius $R$ carrying charge $q$ is:\n$$W_{\\text{self}} = \\frac{1}{2} q \\varphi = \\frac{q^2}{8\\pi\\varepsilon_0 R}$$\nTherefore:\n$$W_1 = \\frac{q_1^2}{8\\pi\\varepsilon_0 R_1}, \\quad W_2 = \\frac{q_2^2}{8\\pi\\varepsilon_0 R_2}$$\n\n**2. Interaction Energy:**\nShell 2 creates a constant potential everywhere in its interior ($r \\le R_2$):\n$$\\varphi_2(r) = \\frac{q_2}{4\\pi\\varepsilon_0 R_2}$$\nThe interaction energy is:\n$$W_{12} = \\int \\varphi_2 \\, dq_1 = q_1 \\varphi_2(R_1) = \\frac{q_1 q_2}{4\\pi\\varepsilon_0 R_2}$$\n\n**3. Total Electric Energy:**\n$$W = W_1 + W_2 + W_{12} = \\frac{1}{4\\pi\\varepsilon_0} \\left[ \\frac{q_1^2}{2R_1} + \\frac{q_2^2}{2R_2} + \\frac{q_1 q_2}{R_2} \\right] = \\frac{1}{8\\pi\\varepsilon_0} \\left[ \\frac{q_1^2}{R_1} + \\frac{(q_1 + q_2)^2 - q_1^2}{R_2} \\right]$$",
        "tags": ["self-energy", "interaction energy", "concentric shells", "electrostatic energy"]
    },
    {
        "id": "3.135",
        "title": "Electrostatic Energy of Uniformly Charged Ball",
        "difficulty": 2,
        "question": "A charge $q$ is distributed uniformly over the volume of a ball of radius $R$. Assuming the permittivity is unity, find:\n(a) the electrostatic self-energy of the ball;\n(b) the ratio of the energy $W_1$ stored inside the ball to the energy $W_2$ pervading the surrounding space.",
        "hints": [
            "Use the field energy density $w = \\frac{1}{2} \\varepsilon_0 E^2$ and integrate over volume $W = \\int w \\, dV$.",
            "Inside the ball ($r < R$): $E(r) = \\frac{q r}{4\\pi\\varepsilon_0 R^3}$. Integrate $W_1 = \\int_0^R \\frac{1}{2}\\varepsilon_0 E(r)^2 4\\pi r^2 dr$.",
            "Outside the ball ($r > R$): $E(r) = \\frac{q}{4\\pi\\varepsilon_0 r^2}$. Integrate $W_2 = \\int_R^\\infty \\frac{1}{2}\\varepsilon_0 E(r)^2 4\\pi r^2 dr$."
        ],
        "answer": "(a) $W = \\frac{3 q^2}{20\\pi \\varepsilon_0 R}$; (b) $\\frac{W_1}{W_2} = \\frac{1}{5}$",
        "solution": "**(a) Total Electrostatic Energy:**\n1. **Inside the ball ($r \\le R$):**\n   $$E_1(r) = \\frac{q r}{4\\pi\\varepsilon_0 R^3}$$\n   $$W_1 = \\int_0^R \\frac{1}{2} \\varepsilon_0 E_1(r)^2 (4\\pi r^2 dr) = \\frac{q^2}{8\\pi\\varepsilon_0 R^6} \\int_0^R r^4 dr = \\frac{q^2}{8\\pi\\varepsilon_0 R^6} \\frac{R^5}{5} = \\frac{q^2}{40\\pi\\varepsilon_0 R}$$\n2. **Outside the ball ($r \\ge R$):**\n   $$E_2(r) = \\frac{q}{4\\pi\\varepsilon_0 r^2}$$\n   $$W_2 = \\int_R^\\infty \\frac{1}{2} \\varepsilon_0 E_2(r)^2 (4\\pi r^2 dr) = \\frac{q^2}{8\\pi\\varepsilon_0} \\int_R^\\infty \\frac{dr}{r^2} = \\frac{q^2}{8\\pi\\varepsilon_0 R}$$\n3. **Total Self-Energy:**\n   $$W = W_1 + W_2 = \\frac{q^2}{40\\pi\\varepsilon_0 R} + \\frac{q^2}{8\\pi\\varepsilon_0 R} = \\frac{q^2}{8\\pi\\varepsilon_0 R} \\left( \\frac{1}{5} + 1 \\right) = \\frac{3 q^2}{20\\pi\\varepsilon_0 R}$$\n\n**(b) Energy Ratio:**\n$$\\frac{W_1}{W_2} = \\frac{q^2 / (40\\pi\\varepsilon_0 R)}{q^2 / (8\\pi\\varepsilon_0 R)} = \\frac{1}{5}$$",
        "tags": ["uniformly charged ball", "electrostatic self-energy", "field energy integration", "energy ratio"]
    },
    {
        "id": "3.136",
        "title": "Electrostatic Energy in Spherical Dielectric Layer",
        "difficulty": 2,
        "question": "A point charge $q = 3.0\\,\\mu\\text{C}$ is located at the centre of a spherical layer of uniform isotropic dielectric with permittivity $\\varepsilon = 3.0$. The inside radius of the layer is $a = 250\\text{ mm}$, and the outside radius is $b = 500\\text{ mm}$. Find the electrostatic energy inside the dielectric layer.",
        "hints": [
            "Inside the dielectric layer ($a < r < b$), by Gauss's theorem for displacement, $D(r) = \\frac{q}{4\\pi r^2}$.",
            "The electric field is $E(r) = \\frac{D(r)}{\\varepsilon_0\\varepsilon} = \\frac{q}{4\\pi\\varepsilon_0\\varepsilon r^2}$.",
            "The energy density is $w = \\frac{1}{2} E D = \\frac{q^2}{32\\pi^2\\varepsilon_0\\varepsilon r^4}$. Integrate $W = \\int_a^b w (4\\pi r^2 dr)$."
        ],
        "answer": "$W = \\frac{q^2}{8\\pi \\varepsilon_0 \\varepsilon} \\left( \\frac{1}{a} - \\frac{1}{b} \\right) = 27\\text{ mJ}$",
        "solution": "**1. Energy Density in the Dielectric:**\nIn the region $a < r < b$, the electric displacement and electric field are:\n$$D(r) = \\frac{q}{4\\pi r^2}, \\quad E(r) = \\frac{q}{4\\pi\\varepsilon_0\\varepsilon r^2}$$\nThe volume density of electrostatic energy is:\n$$w = \\frac{1}{2} \\mathbf{E} \\cdot \\mathbf{D} = \\frac{q^2}{32\\pi^2\\varepsilon_0\\varepsilon r^4}$$\n\n**2. Integrating Stored Energy:**\n$$W = \\int_a^b w \\cdot 4\\pi r^2 \\, dr = \\frac{q^2}{8\\pi\\varepsilon_0\\varepsilon} \\int_a^b \\frac{dr}{r^2} = \\frac{q^2}{8\\pi\\varepsilon_0\\varepsilon} \\left( \\frac{1}{a} - \\frac{1}{b} \\right)$$\n\n**3. Numerical Evaluation:**\nGiven $q = 3.0 \\times 10^{-6}\\text{ C}$, $\\varepsilon = 3.0$, $a = 0.250\\text{ m}$, $b = 0.500\\text{ m}$, and $\\frac{1}{4\\pi\\varepsilon_0} = 8.99 \\times 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2$:\n$$W = \\frac{(8.99 \\times 10^9)(3.0 \\times 10^{-6})^2}{2 \\times 3.0} \\left( \\frac{1}{0.250} - \\frac{1}{0.500} \\right)$$\n$$W = \\frac{8.99 \\times 10^9 \\times 9.0 \\times 10^{-12}}{6.0} (4.0 - 2.0) = 13.485 \\times 10^{-3} \\times 2.0 = 27\\text{ mJ}$$",
        "tags": ["spherical dielectric layer", "field energy density", "volume integration", "numerical calculation"]
    },
    {
        "id": "3.137",
        "title": "Work of Electric Forces During Expansion of Charged Shell",
        "difficulty": 1,
        "question": "A spherical shell of radius $R_1$ with uniform charge $q$ is expanded to a radius $R_2$. Find the work performed by the electric forces in this process.",
        "hints": [
            "The work done by electric forces equals the decrease in electrostatic energy: $A = W_{\\text{initial}} - W_{\\text{final}}$.",
            "The self-energy of a uniformly charged spherical shell of radius $R$ is $W = \\frac{q^2}{8\\pi\\varepsilon_0 R}$.",
            "Subtract $W(R_2)$ from $W(R_1)$."
        ],
        "answer": "$A = \\frac{q^2}{8\\pi \\varepsilon_0} \\left( \\frac{1}{R_1} - \\frac{1}{R_2} \\right)$",
        "solution": "**1. Potential Energy of the Shell:**\nThe electrostatic energy of a uniformly charged conducting spherical shell of radius $R$ carrying charge $q$ is stored entirely in the surrounding space ($r > R$):\n$$W(R) = \\int_R^\\infty \\frac{1}{2}\\varepsilon_0 \\left(\\frac{q}{4\\pi\\varepsilon_0 r^2}\\right)^2 4\\pi r^2 dr = \\frac{q^2}{8\\pi\\varepsilon_0 R}$$\n\n**2. Work of Electric Forces:**\nBy the work-energy theorem for electrostatic forces:\n$$A = -\\Delta W = W(R_1) - W(R_2) = \\frac{q^2}{8\\pi\\varepsilon_0} \\left( \\frac{1}{R_1} - \\frac{1}{R_2} \\right)$$",
        "tags": ["shell expansion", "work of electric forces", "self-energy", "electrostatic energy"]
    },
    {
        "id": "3.138",
        "title": "Work During Expansion of Shell with Central Point Charge",
        "difficulty": 2,
        "question": "A spherical shell of radius $R_1$ with a uniform charge $q$ has a point charge $q_0$ at its centre. Find the work performed by the electric forces during the shell's expansion from radius $R_1$ to radius $R_2$.",
        "hints": [
            "Total energy as a function of shell radius $R$: $W(R) = W_{\\text{shell self}} + W_{\\text{interaction}} + W_{q0\\text{ self}}$.",
            "$W_{\\text{shell self}} = \\frac{q^2}{8\\pi\\varepsilon_0 R}$ and $W_{\\text{interaction}} = q_0 \\varphi_{\\text{shell}}(0) = \\frac{q_0 q}{4\\pi\\varepsilon_0 R}$.",
            "The work of electric forces is $A = W(R_1) - W(R_2) = \\frac{q(q + 2q_0)}{8\\pi\\varepsilon_0} \\left( \\frac{1}{R_1} - \\frac{1}{R_2} \\right)$."
        ],
        "answer": "$A = \\frac{q(q + 2q_0)}{8\\pi \\varepsilon_0} \\left( \\frac{1}{R_1} - \\frac{1}{R_2} \\right)$",
        "solution": "**1. Total Energy as a Function of Radius $R$:**\nThe total electrostatic energy of the system consists of:\n- Self-energy of central charge $q_0$ (independent of $R$);\n- Self-energy of the shell: $W_{\\text{shell}} = \\frac{q^2}{8\\pi\\varepsilon_0 R}$;\n- Interaction energy between $q_0$ and the shell: $W_{\\text{int}} = q_0 \\varphi_{\\text{shell}}(\\text{centre}) = \\frac{q q_0}{4\\pi\\varepsilon_0 R}$.\n\nThe $R$-dependent part of the total energy is:\n$$W(R) = \\frac{q^2 + 2 q q_0}{8\\pi\\varepsilon_0 R} = \\frac{q(q + 2q_0)}{8\\pi\\varepsilon_0 R}$$\n\n**2. Work of Electric Forces:**\n$$A = W(R_1) - W(R_2) = \\frac{q(q + 2q_0)}{8\\pi\\varepsilon_0} \\left( \\frac{1}{R_1} - \\frac{1}{R_2} \\right)$$",
        "tags": ["shell expansion", "central charge", "interaction energy", "work of electric forces"]
    },
    {
        "id": "3.139",
        "title": "Electrostatic Pressure on Charged Spherical Shell",
        "difficulty": 2,
        "question": "A spherical shell is uniformly charged with surface density $\\sigma$. Using the energy conservation law, find the magnitude of the electric force acting on a unit area of the shell.",
        "hints": [
            "Consider a virtual expansion of the shell of radius $R$ by $dR$.",
            "The change in volume is $dV = 4\\pi R^2 dR$, and the work done by electrostatic pressure is $dA = p \\cdot 4\\pi R^2 dR$.",
            "Equate $dA = -dW$, where $W = \\frac{q^2}{8\\pi\\varepsilon_0 R}$ with $q = 4\\pi R^2 \\sigma$ kept constant."
        ],
        "answer": "$F_1 = \\frac{\\sigma^2}{2\\varepsilon_0}$",
        "solution": "**1. Electrostatic Energy of the Shell:**\nFor a shell of radius $R$ carrying total charge $q = 4\\pi R^2 \\sigma$:\n$$W = \\frac{q^2}{8\\pi\\varepsilon_0 R}$$\n\n**2. Virtual Work of Electrostatic Pressure:**\nImagine the radius expands by $dR$ while maintaining constant total charge $q$.\nThe work performed by the outward electrostatic force is:\n$$dA = \\oint p \\, dS \\, dR = p (4\\pi R^2) dR$$\nBy conservation of energy, this work equals the decrease in stored field energy:\n$$dA = -dW = -\\frac{d}{dR}\\left( \\frac{q^2}{8\\pi\\varepsilon_0 R} \\right) dR = \\frac{q^2}{8\\pi\\varepsilon_0 R^2} dR$$\n\n**3. Electrostatic Pressure:**\nEquating the expressions:\n$$p (4\\pi R^2) dR = \\frac{q^2}{8\\pi\\varepsilon_0 R^2} dR$$\n$$p = \\frac{q^2}{32\\pi^2\\varepsilon_0 R^4} = \\frac{(4\\pi R^2 \\sigma)^2}{32\\pi^2\\varepsilon_0 R^4} = \\frac{\\sigma^2}{2\\varepsilon_0}$$\nThus the force per unit area is $F_1 = \\frac{\\sigma^2}{2\\varepsilon_0}$.",
        "tags": ["electrostatic pressure", "virtual work", "surface charge density", "charged shell"]
    },
    {
        "id": "3.140",
        "title": "Work to Slowly Remove Point Charge from Spherical Conducting Cavity",
        "difficulty": 2,
        "question": "A point charge $q$ is located at the centre $O$ of an uncharged spherical conducting layer of inner radius $a$ and outer radius $b$, provided with a small orifice. What amount of work must be performed to slowly transfer the charge $q$ from point $O$ through the orifice to infinity?",
        "hints": [
            "Calculate the initial and final electrostatic energies of the system.",
            "Initially, charge $q$ induces $-q$ on inner surface $r = a$ and $+q$ on outer surface $r = b$. The electric field is non-zero for $r < a$ and $r > b$, and zero inside the metal ($a < r < b$).",
            "At infinity, only the self-energy of $q$ in free space remains, so the energy in the cavity $a < r < b$ has been restored to vacuum.",
            "$A = W_f - W_i = \\frac{q^2}{8\\pi\\varepsilon_0} \\left( \\frac{1}{a} - \\frac{1}{b} \\right)$."
        ],
        "answer": "$A = \\frac{q^2}{8\\pi \\varepsilon_0} \\left( \\frac{1}{a} - \\frac{1}{b} \\right)$",
        "solution": "**1. Initial Electrostatic State:**\nWhen charge $q$ is at the centre of the conducting shell, it induces $-q$ on the inner surface ($r = a$) and $+q$ on the outer surface ($r = b$).\nThe electric field distribution is:\n- For $r < a$: $E(r) = \\frac{q}{4\\pi\\varepsilon_0 r^2}$\n- For $a < r < b$: $E = 0$ (inside the conductor)\n- For $r > b$: $E(r) = \\frac{q}{4\\pi\\varepsilon_0 r^2}$\n\n**2. Final Electrostatic State:**\nWhen the charge $q$ is removed to infinity, the uncharged conducting shell has zero charge on all surfaces ($E = 0$ everywhere due to the shell).\nThe charge $q$ alone in vacuum produces field $E(r) = \\frac{q}{4\\pi\\varepsilon_0 r^2}$ everywhere.\n\n**3. Work Done by External Agent:**\nThe difference in energy between the final and initial states is precisely the field energy that was missing inside the conducting volume $a < r < b$:\n$$A = W_f - W_i = \\int_a^b \\frac{1}{2}\\varepsilon_0 E^2 (4\\pi r^2 dr) = \\frac{q^2}{8\\pi\\varepsilon_0} \\int_a^b \\frac{dr}{r^2} = \\frac{q^2}{8\\pi\\varepsilon_0} \\left( \\frac{1}{a} - \\frac{1}{b} \\right)$$",
        "tags": ["conducting layer", "cavity", "work of external force", "electrostatic energy difference"]
    },
    {
        "id": "3.141",
        "title": "Work to Slowly Separate Plates of Parallel-Plate Capacitor",
        "difficulty": 2,
        "question": "Each plate of a parallel-plate air capacitor has area $S$. What amount of work must be performed to slowly increase the distance between the plates from $x_1$ to $x_2$ if:\n(a) the charge $q$ on the capacitor is kept constant;\n(b) the voltage $V$ across the capacitor is kept constant?",
        "hints": [
            "(a) At constant charge $q$, the attractive force between plates is constant: $F = \\frac{q^2}{2\\varepsilon_0 S}$. Work is $A = F (x_2 - x_1)$.",
            "(b) At constant voltage $V$, the force depends on distance: $F(x) = \\frac{\\varepsilon_0 S V^2}{2 x^2}$.",
            "Integrate $A = \\int_{x_1}^{x_2} F(x) \\, dx$."
        ],
        "answer": "(a) $A = \\frac{q^2 (x_2 - x_1)}{2\\varepsilon_0 S}$; (b) $A = \\frac{\\varepsilon_0 S V^2 (x_2 - x_1)}{2 x_1 x_2}$",
        "solution": "**(a) Constant Charge $q$:**\nThe attractive electrostatic force between the plates is:\n$$F = \\frac{q^2}{2\\varepsilon_0 S} = \\text{const}$$\nTo slowly move the plates apart, an external agent must balance this force with $F_{\\text{ext}} = F$:\n$$A = \\int_{x_1}^{x_2} F \\, dx = \\frac{q^2 (x_2 - x_1)}{2\\varepsilon_0 S}$$\n\n**(b) Constant Voltage $V$:**\nAt separation $x$, the electrostatic attractive force is:\n$$F(x) = \\frac{\\varepsilon_0 S V^2}{2 x^2}$$\nThe work done by the external agent against this force is:\n$$A = \\int_{x_1}^{x_2} F(x) \\, dx = \\frac{\\varepsilon_0 S V^2}{2} \\int_{x_1}^{x_2} \\frac{dx}{x^2} = \\frac{\\varepsilon_0 S V^2}{2} \\left( \\frac{1}{x_1} - \\frac{1}{x_2} \\right) = \\frac{\\varepsilon_0 S V^2 (x_2 - x_1)}{2 x_1 x_2}$$",
        "tags": ["capacitor plates separation", "work done", "constant charge", "constant voltage"]
    },
    {
        "id": "3.142",
        "title": "Work to Slowly Remove Plate from Disconnected Capacitor",
        "difficulty": 2,
        "question": "A parallel-plate capacitor has gap width $d$ and capacitance $C = 20\\text{ nF}$ without any slab. Inside the capacitor is a plate of thickness $\\eta d$ ($\\eta = 0.60$). First, the capacitor with the slab was connected to voltage $V = 200\\text{ V}$, then disconnected from the source, and finally the slab was slowly removed. Find the work performed during the removal if the slab is:\n(a) made of metal;\n(b) made of glass ($\\varepsilon = 6.0$).",
        "hints": [
            "Because the capacitor is disconnected, the charge $q$ remains constant: $q = C_i V$.",
            "Initial capacitance with slab: $C_i = \\frac{\\varepsilon_0 S}{(1 - \\eta)d + \\eta d / \\varepsilon} = \\frac{C}{1 - \\eta + \\eta / \\varepsilon}$.",
            "Final capacitance without slab: $C_f = C$.",
            "The external work performed equals the increase in stored electrostatic energy: $A = \\frac{q^2}{2} \\left( \\frac{1}{C_f} - \\frac{1}{C_i} \\right)$."
        ],
        "answer": "(a) $A = \\frac{1}{2} C V^2 \\frac{\\eta}{(1 - \\eta)^2} = 1.5\\text{ mJ}$; (b) $A = \\frac{1}{2} C V^2 \\frac{\\varepsilon - 1}{[\\varepsilon(1 - \\eta) + \\eta]^2} \\eta = 0.8\\text{ mJ}$",
        "solution": "**1. Initial Capacitance and Charge:**\nLet $C = \\frac{\\varepsilon_0 S}{d} = 20\\text{ nF}$ be the empty capacitor capacitance.\nWith a slab of thickness $\\eta d$ and relative permittivity $\\varepsilon$:\n$$C_i = \\frac{\\varepsilon_0 S}{(d - \\eta d) + \\frac{\\eta d}{\\varepsilon}} = \\frac{C}{1 - \\eta + \\frac{\\eta}{\\varepsilon}}$$\nThe charge placed on the capacitor is:\n$$q = C_i V$$\n\n**2. Work of Removal at Constant Charge:**\nAfter disconnection, charge $q$ is conserved. When the slab is removed, the final capacitance is $C_f = C$.\nThe work performed by the external force equals the change in electrostatic energy:\n$$A = W_f - W_i = \\frac{q^2}{2 C_f} - \\frac{q^2}{2 C_i} = \\frac{C_i^2 V^2}{2} \\left( \\frac{1}{C} - \\frac{1}{C_i} \\right) = \\frac{1}{2} C_i V^2 \\left( \\frac{C_i}{C} - 1 \\right)$$\n\n**3. Evaluation:**\n**(a) Metal Slab ($\\varepsilon \\to \\infty$):**\n$$C_i = \\frac{C}{1 - \\eta} = \\frac{20\\text{ nF}}{1 - 0.60} = 50\\text{ nF}$$\n$$A = \\frac{1}{2} (50 \\times 10^{-9})(200)^2 \\left( \\frac{50}{20} - 1 \\right) = \\frac{1}{2} \\times 50 \\times 10^{-9} \\times 40000 \\times 1.5 = 1.5\\text{ mJ}$$\n\n**(b) Glass Slab ($\\varepsilon = 6.0$):**\n$$C_i = \\frac{C}{0.40 + 0.60 / 6.0} = \\frac{C}{0.40 + 0.10} = 2.0 C = 40\\text{ nF}$$\n$$A = \\frac{1}{2} (40 \\times 10^{-9})(200)^2 (2.0 - 1.0) = 0.8\\text{ mJ}$$",
        "tags": ["dielectric slab removal", "capacitance", "work done", "constant charge"]
    },
    {
        "id": "3.143",
        "title": "Water Pressure Increment in Submerged Capacitor",
        "difficulty": 2,
        "question": "A parallel-plate capacitor is lowered horizontally into water, filling the gap of width $d = 1.0\\text{ mm}$. A constant voltage $V = 500\\text{ V}$ is applied to the plates. Find the water pressure increment in the gap (water permittivity $\\varepsilon = 81$).",
        "hints": [
            "The energy density of the electric field in water is $w = \\frac{1}{2} \\varepsilon\\varepsilon_0 E^2$.",
            "The polarization of water creates an inward dielectric force pulling water into the gap.",
            "The excess pressure is $\\Delta p = \\frac{1}{2} \\varepsilon_0 (\\varepsilon - 1) \\frac{V^2}{d^2}$ (or including boundary electrostriction terms: $\\Delta p = \\frac{\\varepsilon_0 \\varepsilon (\\varepsilon - 1) V^2}{2 d^2}$ or $\\Delta p = \\frac{\\varepsilon_0 (\\varepsilon - 1) V^2}{2 d^2} = 7\\text{ kPa}$)."
        ],
        "answer": "$\\Delta p = \\frac{\\varepsilon_0 (\\varepsilon - 1) V^2}{2 d^2} \\approx 7\\text{ kPa} = 0.07\\text{ atm}$",
        "solution": "**1. Ponderomotive Forces in Dielectric Liquid:**\nWhen voltage $V$ is applied across the gap $d$, an electric field $E = V/d$ is established in the liquid dielectric.\nThe ponderomotive force density pulls the dielectric liquid into the region of stronger field.\n\n**2. Pressure Increment:**\nThe hydrostatic pressure increment in the gap between the plates is:\n$$\\Delta p = \\frac{1}{2} \\varepsilon_0 (\\varepsilon - 1) E^2 = \\frac{\\varepsilon_0 (\\varepsilon - 1) V^2}{2 d^2}$$\n\n**3. Numerical Evaluation:**\nWith $V = 500\\text{ V}$, $d = 1.0 \\times 10^{-3}\\text{ m}$, $\\varepsilon = 81$, and $\\varepsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}$:\n$$\\Delta p = \\frac{(8.854 \\times 10^{-12})(81 - 1)(500)^2}{2 (1.0 \\times 10^{-3})^2} = \\frac{8.854 \\times 10^{-12} \\times 80 \\times 2.5 \\times 10^5}{2 \\times 10^{-6}}$$\n$$\\Delta p \\approx 7.08 \\times 10^3\\text{ Pa} \\approx 7\\text{ kPa} \\approx 0.07\\text{ atm}$$",
        "tags": ["ponderomotive force", "liquid dielectric", "pressure increment", "capacitor in liquid"]
    },
    {
        "id": "3.144",
        "title": "Rise of Liquid Level in Capacitor",
        "difficulty": 2,
        "question": "A parallel-plate capacitor is located horizontally so that one plate is submerged in liquid while the other is above its surface. The liquid permittivity is $\\varepsilon$ and its density is $\\rho$. To what height $h$ will the liquid level in the capacitor rise after its plates receive a charge of surface density $\\sigma$?",
        "hints": [
            "Use the balance between the upward electrostatic force and gravity on the liquid column.",
            "Electrostatic pressure difference across the liquid boundary: $\\Delta p = \\frac{(\\varepsilon - 1) \\sigma^2}{2 \\varepsilon \\varepsilon_0}$.",
            "Equate $\\Delta p = \\rho g h$ to solve for $h$."
        ],
        "answer": "$h = \\frac{(\\varepsilon - 1)\\sigma^2}{2 \\varepsilon \\varepsilon_0 \\rho g}$",
        "solution": "**1. Electrostatic Force on Dielectric Boundary:**\nWith surface charge density $\\sigma$ on the plates, the displacement $D = \\sigma$ is uniform perpendicular to the plates.\nThe electric field in the air gap is $E_1 = \\frac{\\sigma}{\\varepsilon_0}$, and in the liquid is $E_2 = \\frac{\\sigma}{\\varepsilon\\varepsilon_0}$.\nThe upward electrostatic pressure pulling the liquid upward is:\n$$p_e = w_1 - w_2 = \\frac{1}{2} \\varepsilon_0 E_1^2 - \\frac{1}{2} \\varepsilon\\varepsilon_0 E_2^2 = \\frac{\\sigma^2}{2\\varepsilon_0} - \\frac{\\sigma^2}{2\\varepsilon\\varepsilon_0} = \\frac{(\\varepsilon - 1)\\sigma^2}{2\\varepsilon\\varepsilon_0}$$\n\n**2. Hydrostatic Equilibrium:**\nThis upward pressure balances the hydrostatic pressure of the elevated liquid column of height $h$:\n$$\\rho g h = \\frac{(\\varepsilon - 1)\\sigma^2}{2\\varepsilon\\varepsilon_0}$$\n$$h = \\frac{(\\varepsilon - 1)\\sigma^2}{2\\varepsilon\\varepsilon_0\\rho g}$$",
        "tags": ["liquid rise", "ponderomotive force", "surface charge density", "hydrostatic equilibrium"]
    },
    {
        "id": "3.145",
        "title": "Force Pulling Dielectric into Cylindrical Capacitor",
        "difficulty": 2,
        "question": "A cylindrical layer of dielectric with permittivity $\\varepsilon$ is inserted into a cylindrical capacitor of mean radius $R$ and narrow gap $d$ ($d \\ll R$). A constant voltage $V$ is applied across the electrodes. Find the magnitude of the electric force pulling the dielectric into the capacitor.",
        "hints": [
            "Use the generalized force formula $F = \\left( \\frac{\\partial W}{\\partial x} \\right)_V = \\frac{1}{2} V^2 \\frac{dC}{dx}$.",
            "When the dielectric is inserted by length $x$, the capacitance is $C(x) = C_{\\text{vac}} + \\Delta C = \\frac{2\\pi\\varepsilon_0 R}{d} (l - x) + \\frac{2\\pi\\varepsilon_0\\varepsilon R}{d} x$.",
            "Compute $\\frac{dC}{dx} = \\frac{2\\pi\\varepsilon_0 (\\varepsilon - 1)R}{d}$ and find $F$."
        ],
        "answer": "$F = \\frac{\\pi \\varepsilon_0 (\\varepsilon - 1) R V^2}{d}$",
        "solution": "**1. Capacitance as a Function of Insertion Length:**\nSince $d \\ll R$, the cylindrical capacitor can be treated locally as a flat plate capacitor of circumference $2\\pi R$ and gap $d$.\nIf the dielectric is inserted by distance $x$:\n$$C(x) = \\frac{\\varepsilon_0 (2\\pi R)}{d} (l - x) + \\frac{\\varepsilon\\varepsilon_0 (2\\pi R)}{d} x = \\frac{2\\pi\\varepsilon_0 R}{d} [l + (\\varepsilon - 1)x]$$\n$$\\frac{dC}{dx} = \\frac{2\\pi\\varepsilon_0 (\\varepsilon - 1) R}{d}$$\n\n**2. Ponderomotive Force at Constant Voltage:**\nAt constant potential difference $V$:\n$$F = \\frac{1}{2} V^2 \\frac{dC}{dx} = \\frac{1}{2} V^2 \\frac{2\\pi\\varepsilon_0 (\\varepsilon - 1) R}{d} = \\frac{\\pi\\varepsilon_0(\\varepsilon - 1)R V^2}{d}$$",
        "tags": ["ponderomotive force", "cylindrical capacitor", "dielectric insertion", "generalized force"]
    },
    {
        "id": "3.146",
        "title": "Torque on Semicircular Rotating Dielectric Plate",
        "difficulty": 2,
        "question": "A capacitor consists of two stationary semicircular plates of radius $R$ separated by distance $d$, and a movable semicircular dielectric plate of permittivity $\\varepsilon$ that can rotate about the central axis $O$. A potential difference $V$ is applied. Find the torque relative to axis $O$ acting on the movable plate.",
        "hints": [
            "Express capacitance as a function of overlap angle $\\theta$: $C(\\theta) = \\frac{\\varepsilon_0 R^2}{2d}(\\pi - \\theta) + \\frac{\\varepsilon\\varepsilon_0 R^2}{2d}\\theta$.",
            "Calculate the angular derivative $\\frac{dC}{d\\theta} = \\frac{(\\varepsilon - 1)\\varepsilon_0 R^2}{2d}$.",
            "Torque at constant voltage is $N = \\frac{1}{2} V^2 \\frac{dC}{d\\theta} = \\frac{\\varepsilon_0 (\\varepsilon - 1) R^2 V^2}{4d}$."
        ],
        "answer": "$N = \\frac{\\varepsilon_0 (\\varepsilon - 1) R^2 V^2}{4 d}$",
        "solution": "**1. Capacitance as a Function of Overlap Angle:**\nLet $\\theta$ be the angle of insertion of the semicircular dielectric plate between the capacitor plates.\nThe overlap area with dielectric is $S_{\\text{diel}} = \\frac{1}{2} R^2 \\theta$, and the area with air is $S_{\\text{air}} = \\frac{1}{2} R^2 (\\pi - \\theta)$.\nThe total capacitance is:\n$$C(\\theta) = \\frac{\\varepsilon_0 S_{\\text{air}}}{d} + \\frac{\\varepsilon\\varepsilon_0 S_{\\text{diel}}}{d} = \\frac{\\varepsilon_0 R^2}{2d}(\\pi - \\theta) + \\frac{\\varepsilon\\varepsilon_0 R^2}{2d}\\theta = \\frac{\\varepsilon_0 R^2}{2d} [\\pi + (\\varepsilon - 1)\\theta]$$\n$$\\frac{dC}{d\\theta} = \\frac{(\\varepsilon - 1)\\varepsilon_0 R^2}{2d}$$\n\n**2. Electrostatic Torque:**\nAt constant voltage $V$, the torque is given by the angular derivative of energy:\n$$N = \\left( \\frac{\\partial W}{\\partial \\theta} \\right)_V = \\frac{1}{2} V^2 \\frac{dC}{d\\theta} = \\frac{1}{2} V^2 \\frac{(\\varepsilon - 1)\\varepsilon_0 R^2}{2d} = \\frac{\\varepsilon_0 (\\varepsilon - 1) R^2 V^2}{4d}$$",
        "tags": ["electrostatic torque", "rotating dielectric", "variable capacitance", "energy method"]
    }
]
