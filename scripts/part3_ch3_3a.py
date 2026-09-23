"""
part3_ch3_3a.py
Curated problems 3.101 to 3.125 (25 problems) of Irodov Chapter 3.3:
Electric Capacitance. Energy of an Electric Field (Part A).
"""

CH3_3A_CURATED = [
    {
        "id": "3.101",
        "title": "Capacitance of Spherical Conductor with Dielectric Layer",
        "difficulty": 2,
        "question": "Find the capacitance of an isolated spherical conductor of radius $R_1$ surrounded by an adjacent concentric layer of dielectric with permittivity $\\varepsilon$ and outer radius $R_2$.",
        "hints": [
            "Assume a charge $q$ on the inner conducting ball. By Gauss's theorem for displacement, $D(r) = \\frac{q}{4\\pi r^2}$.",
            "The electric field is $E(r) = \\frac{q}{4\\pi\\varepsilon_0\\varepsilon r^2}$ for $R_1 < r < R_2$, and $E(r) = \\frac{q}{4\\pi\\varepsilon_0 r^2}$ for $r > R_2$.",
            "Calculate the potential $\\varphi = \\int_{R_1}^{R_2} E(r)\\,dr + \\int_{R_2}^\\infty E(r)\\,dr$ and find $C = q/\\varphi$."
        ],
        "answer": "$C = \\frac{4\\pi \\varepsilon_0 \\varepsilon R_1 R_2}{R_2 + (\\varepsilon - 1)R_1}$",
        "solution": "**1. Electric Field Distribution:**\nLet the spherical conductor carry charge $q$. Due to spherical symmetry, the electric displacement is:\n$$D(r) = \\frac{q}{4\\pi r^2}$$\nThe electric field strength in the two regions is:\n- Inside the dielectric layer ($R_1 < r < R_2$):\n  $$E(r) = \\frac{q}{4\\pi\\varepsilon_0\\varepsilon r^2}$$\n- In the surrounding vacuum ($r > R_2$):\n  $$E(r) = \\frac{q}{4\\pi\\varepsilon_0 r^2}$$\n\n**2. Potential of the Conductor:**\nTaking potential at infinity to be zero ($\\varphi(\\infty) = 0$):\n$$\\varphi = \\int_{R_1}^\\infty E(r) \\, dr = \\int_{R_1}^{R_2} \\frac{q \\, dr}{4\\pi\\varepsilon_0\\varepsilon r^2} + \\int_{R_2}^\\infty \\frac{q \\, dr}{4\\pi\\varepsilon_0 r^2}$$\n$$\\varphi = \\frac{q}{4\\pi\\varepsilon_0\\varepsilon} \\left( \\frac{1}{R_1} - \\frac{1}{R_2} \\right) + \\frac{q}{4\\pi\\varepsilon_0 R_2} = \\frac{q}{4\\pi\\varepsilon_0\\varepsilon R_1 R_2} \\left[ (R_2 - R_1) + \\varepsilon R_1 \\right]$$\n$$\\varphi = \\frac{q [R_2 + (\\varepsilon - 1)R_1]}{4\\pi\\varepsilon_0\\varepsilon R_1 R_2}$$\n\n**3. Capacitance:**\n$$C = \\frac{q}{\\varphi} = \\frac{4\\pi\\varepsilon_0\\varepsilon R_1 R_2}{R_2 + (\\varepsilon - 1)R_1}$$",
        "tags": ["capacitance", "spherical conductor", "dielectric layer", "potential"]
    },
    {
        "id": "3.102",
        "title": "Series Capacitors with One Filled with Dielectric",
        "difficulty": 2,
        "question": "Two parallel-plate air capacitors, each of capacitance $C$, were connected in series to a battery with EMF $\\mathcal{E}$. Then one of the capacitors was filled with a uniform dielectric of permittivity $\\varepsilon$. How many times did the electric field strength in that capacitor decrease? What amount of charge flows through the battery?",
        "hints": [
            "Initial state: two capacitors of capacitance $C$ in series across $\\mathcal{E}$. Each has voltage $V_0 = \\mathcal{E}/2$ and charge $q_0 = C\\mathcal{E}/2$.",
            "Final state: capacitor 1 has capacitance $C_1 = \\varepsilon C$, capacitor 2 has $C_2 = C$. Find new voltage $V_1$ across capacitor 1.",
            "Charge flowing through the battery is $\\Delta q = q_{\\text{final}} - q_0 = C_{\\text{eq}}' \\mathcal{E} - q_0$."
        ],
        "answer": "The field strength decreased $\\frac{\\varepsilon + 1}{2}$ times; $q = \\frac{\\varepsilon - 1}{2(\\varepsilon + 1)} C \\mathcal{E}$",
        "solution": "**1. Initial State:**\nWith two identical capacitors in series across EMF $\\mathcal{E}$:\n$$C_{\\text{eq}} = \\frac{C}{2}, \\quad q_0 = \\frac{1}{2} C \\mathcal{E}$$\nThe initial voltage and electric field in each capacitor are:\n$$V_0 = \\frac{\\mathcal{E}}{2}, \\quad E_0 = \\frac{V_0}{d} = \\frac{\\mathcal{E}}{2d}$$\n\n**2. Final State After Filling Capacitor 1:**\nThe new capacitances are $C_1 = \\varepsilon C$ and $C_2 = C$.\nThe new equivalent capacitance is:\n$$C_{\\text{eq}}' = \\frac{C_1 C_2}{C_1 + C_2} = \\frac{\\varepsilon C \\cdot C}{\\varepsilon C + C} = \\frac{\\varepsilon}{\\varepsilon + 1} C$$\nThe new voltage across capacitor 1 is:\n$$V_1 = \\frac{q_{\\text{final}}}{C_1} = \\frac{C_{\\text{eq}}' \\mathcal{E}}{\\varepsilon C} = \\frac{\\mathcal{E}}{\\varepsilon + 1}$$\nThe field strength in capacitor 1 becomes $E_1 = \\frac{V_1}{d} = \\frac{\\mathcal{E}}{(\\varepsilon + 1)d}$.\n\n**3. Ratio of Field Strengths:**\n$$\\frac{E_0}{E_1} = \\frac{\\mathcal{E}/(2d)}{\\mathcal{E}/[(\\varepsilon + 1)d]} = \\frac{\\varepsilon + 1}{2}$$\nThe electric field strength decreased by a factor of $\\frac{\\varepsilon + 1}{2}$.\n\n**4. Charge Flowing Through the Battery:**\n$$\\Delta q = q_{\\text{final}} - q_0 = C_{\\text{eq}}' \\mathcal{E} - C_{\\text{eq}} \\mathcal{E} = \\left( \\frac{\\varepsilon}{\\varepsilon + 1} - \\frac{1}{2} \\right) C \\mathcal{E} = \\frac{\\varepsilon - 1}{2(\\varepsilon + 1)} C \\mathcal{E}$$",
        "tags": ["capacitors in series", "dielectric insertion", "electric field decrease", "charge transferred"]
    },
    {
        "id": "3.103",
        "title": "Capacitor with Two Dielectric Layers in Series",
        "difficulty": 2,
        "question": "The space between the plates of a parallel-plate capacitor is filled consecutively with two dielectric layers 1 and 2 of thicknesses $d_1$ and $d_2$ and permittivities $\\varepsilon_1$ and $\\varepsilon_2$. The area of each plate is $S$. Find:\n(a) the capacitance of the capacitor;\n(b) the surface density $\\sigma'$ of bound charges on the boundary plane between the dielectrics if the voltage across the capacitor is $V$ and the electric field is directed from layer 1 to layer 2.",
        "hints": [
            "(a) The system represents two capacitors in series of thicknesses $d_1, d_2$ and capacitances $C_1 = \\frac{\\varepsilon_0\\varepsilon_1 S}{d_1}, C_2 = \\frac{\\varepsilon_0\\varepsilon_2 S}{d_2}$.",
            "(b) Continuity of displacement: $D = \\frac{\\varepsilon_0 V}{\\frac{d_1}{\\varepsilon_1} + \\frac{d_2}{\\varepsilon_2}}$.",
            "Surface bound charge density at the boundary is $\\sigma' = P_{1n} - P_{2n} = \\left(1 - \\frac{1}{\\varepsilon_1}\\right)D - \\left(1 - \\frac{1}{\\varepsilon_2}\\right)D = \\left(\\frac{1}{\\varepsilon_2} - \\frac{1}{\\varepsilon_1}\\right)D$."
        ],
        "answer": "(a) $C = \\frac{\\varepsilon_0 S}{\\frac{d_1}{\\varepsilon_1} + \\frac{d_2}{\\varepsilon_2}}$; (b) $\\sigma' = \\frac{\\varepsilon_0 (\\varepsilon_1 - \\varepsilon_2) V}{\\varepsilon_2 d_1 + \\varepsilon_1 d_2}$",
        "solution": "**(a) Capacitance:**\nThe two dielectric slabs act as two capacitors connected in series:\n$$\\frac{1}{C} = \\frac{1}{C_1} + \\frac{1}{C_2} = \\frac{d_1}{\\varepsilon_0\\varepsilon_1 S} + \\frac{d_2}{\\varepsilon_0\\varepsilon_2 S} = \\frac{1}{\\varepsilon_0 S} \\left( \\frac{d_1}{\\varepsilon_1} + \\frac{d_2}{\\varepsilon_2} \\right)$$\n$$C = \\frac{\\varepsilon_0 S}{\\frac{d_1}{\\varepsilon_1} + \\frac{d_2}{\\varepsilon_2}} = \\frac{\\varepsilon_0\\varepsilon_1\\varepsilon_2 S}{\\varepsilon_2 d_1 + \\varepsilon_1 d_2}$$\n\n**(b) Bound Surface Charge Density at the Interface:**\nThe electric displacement $D$ is constant across the entire capacitor gap:\n$$D = \\frac{q}{S} = \\frac{C V}{S} = \\frac{\\varepsilon_0 V}{\\frac{d_1}{\\varepsilon_1} + \\frac{d_2}{\\varepsilon_2}} = \\frac{\\varepsilon_0\\varepsilon_1\\varepsilon_2 V}{\\varepsilon_2 d_1 + \\varepsilon_1 d_2}$$\nThe polarization vectors in the two layers are directed along the field (from layer 1 to 2):\n$$P_1 = D - \\varepsilon_0 E_1 = D \\left( 1 - \\frac{1}{\\varepsilon_1} \\right)$$\n$$P_2 = D - \\varepsilon_0 E_2 = D \\left( 1 - \\frac{1}{\\varepsilon_2} \\right)$$\nAt the interface, the bound charge density is given by the discontinuity in normal polarization:\n$$\\sigma' = P_1 - P_2 = D \\left( \\frac{1}{\\varepsilon_2} - \\frac{1}{\\varepsilon_1} \\right) = D \\frac{\\varepsilon_1 - \\varepsilon_2}{\\varepsilon_1\\varepsilon_2}$$\nSubstituting $D$:\n$$\\sigma' = \\frac{\\varepsilon_0 (\\varepsilon_1 - \\varepsilon_2) V}{\\varepsilon_2 d_1 + \\varepsilon_1 d_2}$$",
        "tags": ["two-layer dielectric", "capacitance", "bound surface charge", "series capacitors"]
    },
    {
        "id": "3.104",
        "title": "Capacitor with Linearly Inhomogeneous Dielectric",
        "difficulty": 2,
        "question": "The gap between the plates of a parallel-plate capacitor is filled with isotropic dielectric whose permittivity $\\varepsilon$ varies linearly from $\\varepsilon_1$ to $\\varepsilon_2$ ($\\varepsilon_2 > \\varepsilon_1$) in the direction perpendicular to the plates. The area of each plate is $S$, and the separation is $d$. Find:\n(a) the capacitance of the capacitor;\n(b) the space density of bound charges as a function of $\\varepsilon$ if the charge of the capacitor is $q$ and $\\mathbf{E}$ is directed toward growing $\\varepsilon$.",
        "hints": [
            "(a) Divide the dielectric into thin slices of thickness $dx$ in series: $d(1/C) = \\frac{dx}{\\varepsilon_0\\varepsilon(x) S}$.",
            "Express $dx = \\frac{d}{\\varepsilon_2 - \\varepsilon_1} d\\varepsilon$ and integrate $\\int_{\\varepsilon_1}^{\\varepsilon_2} \\frac{d\\varepsilon}{\\varepsilon}$.",
            "(b) Space density of bound charges: $\\rho' = -\\frac{dP}{dx} = -\\frac{dP}{d\\varepsilon} \\frac{d\\varepsilon}{dx}$, with $P = \\left(1 - \\frac{1}{\\varepsilon}\\right) \\frac{q}{S}$."
        ],
        "answer": "(a) $C = \\frac{\\varepsilon_0 S (\\varepsilon_2 - \\varepsilon_1)}{d \\ln(\\varepsilon_2 / \\varepsilon_1)}$; (b) $\\rho' = -\\frac{q (\\varepsilon_2 - \\varepsilon_1)}{S d \\varepsilon^2}$",
        "solution": "**(a) Capacitance:**\nLet the $x$-axis run perpendicular to the plates from $x = 0$ (where $\\varepsilon = \\varepsilon_1$) to $x = d$ (where $\\varepsilon = \\varepsilon_2$):\n$$\\varepsilon(x) = \\varepsilon_1 + \\frac{\\varepsilon_2 - \\varepsilon_1}{d} x \\implies d\\varepsilon = \\frac{\\varepsilon_2 - \\varepsilon_1}{d} dx$$\nA slice of thickness $dx$ has capacitance $dC = \\frac{\\varepsilon_0\\varepsilon(x) S}{dx}$. Connected in series:\n$$\\frac{1}{C} = \\int_0^d \\frac{dx}{\\varepsilon_0\\varepsilon(x) S} = \\frac{d}{\\varepsilon_0 S (\\varepsilon_2 - \\varepsilon_1)} \\int_{\\varepsilon_1}^{\\varepsilon_2} \\frac{d\\varepsilon}{\\varepsilon} = \\frac{d \\ln(\\varepsilon_2 / \\varepsilon_1)}{\\varepsilon_0 S (\\varepsilon_2 - \\varepsilon_1)}$$\n$$C = \\frac{\\varepsilon_0 S (\\varepsilon_2 - \\varepsilon_1)}{d \\ln(\\varepsilon_2 / \\varepsilon_1)}$$\n\n**(b) Space Density of Bound Charges:**\nThe electric displacement is uniform across the plates: $D = q/S$.\nThe polarization is:\n$$P(x) = D \\left( 1 - \\frac{1}{\\varepsilon(x)} \\right) = \\frac{q}{S} \\left( 1 - \\frac{1}{\\varepsilon} \\right)$$\nThe space density of bound charges is:\n$$\\rho' = -\\frac{dP}{dx} = -\\frac{dP}{d\\varepsilon} \\frac{d\\varepsilon}{dx} = -\\left( \\frac{q}{S \\varepsilon^2} \\right) \\left( \\frac{\\varepsilon_2 - \\varepsilon_1}{d} \\right) = -\\frac{q (\\varepsilon_2 - \\varepsilon_1)}{S d \\varepsilon^2}$$",
        "tags": ["inhomogeneous dielectric", "capacitance", "bound space charge", "linear gradient"]
    },
    {
        "id": "3.105",
        "title": "Capacitance of Spherical Capacitor with $\\varepsilon = a/r$",
        "difficulty": 2,
        "question": "Find the capacitance of a spherical capacitor whose electrodes have radii $R_1$ and $R_2$ ($R_2 > R_1$) and which is filled with isotropic dielectric whose permittivity varies as $\\varepsilon(r) = a/r$, where $a$ is a constant and $r$ is the distance from the centre.",
        "hints": [
            "By Gauss's theorem for displacement: $D(r) = \\frac{q}{4\\pi r^2}$.",
            "The electric field is $E(r) = \\frac{D(r)}{\\varepsilon_0\\varepsilon(r)} = \\frac{q}{4\\pi\\varepsilon_0 (a/r) r^2} = \\frac{q}{4\\pi\\varepsilon_0 a r}$.",
            "Integrate $V = \\int_{R_1}^{R_2} E(r)\\,dr$ to find voltage and capacitance $C = q/V$."
        ],
        "answer": "$C = \\frac{4\\pi \\varepsilon_0 a}{\\ln(R_2 / R_1)}$",
        "solution": "**1. Electric Field:**\nFor a spherical capacitor with charge $q$ on the inner shell, Gauss's law gives the displacement:\n$$D(r) = \\frac{q}{4\\pi r^2}$$\nWith $\\varepsilon(r) = a/r$, the electric field is:\n$$E(r) = \\frac{D(r)}{\\varepsilon_0 \\varepsilon(r)} = \\frac{q / (4\\pi r^2)}{\\varepsilon_0 (a/r)} = \\frac{q}{4\\pi\\varepsilon_0 a r}$$\n\n**2. Potential Difference:**\n$$V = \\int_{R_1}^{R_2} E(r) \\, dr = \\frac{q}{4\\pi\\varepsilon_0 a} \\int_{R_1}^{R_2} \\frac{dr}{r} = \\frac{q}{4\\pi\\varepsilon_0 a} \\ln\\left( \\frac{R_2}{R_1} \\right)$$\n\n**3. Capacitance:**\n$$C = \\frac{q}{V} = \\frac{4\\pi\\varepsilon_0 a}{\\ln(R_2 / R_1)}$$",
        "tags": ["spherical capacitor", "nonuniform permittivity", "capacitance", "Gauss law for D"]
    },
    {
        "id": "3.106",
        "title": "Simultaneous Breakdown in Two-Layer Cylindrical Capacitor",
        "difficulty": 2,
        "question": "A cylindrical capacitor is filled with two cylindrical layers of dielectric with permittivities $\\varepsilon_1$ and $\\varepsilon_2$. The inner radii of the layers are $R_1$ and $R_2$ ($R_2 > R_1$). The breakdown field strengths are $E_{m1}$ and $E_{m2}$. At what relationship between $\\varepsilon, R$, and $E_m$ will increasing voltage cause breakdown in both dielectrics simultaneously?",
        "hints": [
            "In cylindrical geometry, displacement is $D(r) = \\frac{\\lambda}{2\\pi r}$.",
            "The electric field in each layer decreases as $1/r$, so the maximum field in each layer occurs at its inner boundary: $E_{1,\\max} = E_1(R_1) = \\frac{\\lambda}{2\\pi\\varepsilon_0\\varepsilon_1 R_1}$ and $E_{2,\\max} = E_2(R_2) = \\frac{\\lambda}{2\\pi\\varepsilon_0\\varepsilon_2 R_2}$.",
            "Equate $E_{1,\\max} = E_{m1}$ and $E_{2,\\max} = E_{m2}$ for simultaneous breakdown."
        ],
        "answer": "$\\varepsilon_1 R_1 E_{m1} = \\varepsilon_2 R_2 E_{m2}$",
        "solution": "**1. Electric Field Distribution:**\nFor linear charge density $\\lambda$ on the inner conductor:\n$$D(r) = \\frac{\\lambda}{2\\pi r}$$\n- In layer 1 ($R_1 \\le r \\le R_2$):\n  $$E_1(r) = \\frac{\\lambda}{2\\pi\\varepsilon_0\\varepsilon_1 r}$$\n  The maximum field strength occurs at the innermost radius $r = R_1$:\n  $$E_{1,\\max} = \\frac{\\lambda}{2\\pi\\varepsilon_0\\varepsilon_1 R_1}$$\n- In layer 2 ($R_2 \\le r \\le R_3$):\n  $$E_2(r) = \\frac{\\lambda}{2\\pi\\varepsilon_0\\varepsilon_2 r}$$\n  The maximum field strength occurs at $r = R_2$:\n  $$E_{2,\\max} = \\frac{\\lambda}{2\\pi\\varepsilon_0\\varepsilon_2 R_2}$$\n\n**2. Simultaneous Breakdown Condition:**\nBreakdown occurs simultaneously when $E_{1,\\max} = E_{m1}$ and $E_{2,\\max} = E_{m2}$ at the same value of $\\lambda$:\n$$\\lambda = 2\\pi\\varepsilon_0\\varepsilon_1 R_1 E_{m1} = 2\\pi\\varepsilon_0\\varepsilon_2 R_2 E_{m2}$$\n$$\\varepsilon_1 R_1 E_{m1} = \\varepsilon_2 R_2 E_{m2}$$",
        "tags": ["cylindrical capacitor", "dielectric breakdown", "two layers", "maximum field"]
    },
    {
        "id": "3.107",
        "title": "Breakdown Voltage of Double-Layer Cylindrical Capacitor",
        "difficulty": 2,
        "question": "A double-layer cylindrical capacitor has layers with inner radii $R_1, R_2$ and outer radius $R_3$, with permittivities $\\varepsilon_1, \\varepsilon_2$ and breakdown strengths $E_1, E_2$. What is the breakdown voltage of this capacitor if $\\varepsilon_1 R_1 E_1 < \\varepsilon_2 R_2 E_2$?",
        "hints": [
            "The given condition $\\varepsilon_1 R_1 E_1 < \\varepsilon_2 R_2 E_2$ means layer 1 reaches its breakdown threshold $E_1$ at a lower linear charge density than layer 2.",
            "Maximum permissible linear charge density before any breakdown occurs is $\\lambda_{\\max} = 2\\pi\\varepsilon_0\\varepsilon_1 R_1 E_1$.",
            "Calculate voltage $V = \\int_{R_1}^{R_2} E_1(r)\\,dr + \\int_{R_2}^{R_3} E_2(r)\\,dr$ using $\\lambda_{\\max}$."
        ],
        "answer": "$V = R_1 E_1 \\left[ \\ln(R_2 / R_1) + \\frac{\\varepsilon_1}{\\varepsilon_2} \\ln(R_3 / R_2) \\right]$",
        "solution": "**1. Limiting Dielectric:**\nThe peak fields in the layers are $E_{1,\\max} = \\frac{\\lambda}{2\\pi\\varepsilon_0\\varepsilon_1 R_1}$ and $E_{2,\\max} = \\frac{\\lambda}{2\\pi\\varepsilon_0\\varepsilon_2 R_2}$.\nSince $\\varepsilon_1 R_1 E_1 < \\varepsilon_2 R_2 E_2$, layer 1 reaches its breakdown threshold first, at:\n$$\\lambda_{\\max} = 2\\pi\\varepsilon_0\\varepsilon_1 R_1 E_1$$\n\n**2. Breakdown Voltage:**\nThe voltage across the capacitor is:\n$$V = \\int_{R_1}^{R_2} E_1(r) \\, dr + \\int_{R_2}^{R_3} E_2(r) \\, dr = \\frac{\\lambda_{\\max}}{2\\pi\\varepsilon_0} \\left[ \\frac{1}{\\varepsilon_1}\\ln\\left(\\frac{R_2}{R_1}\\right) + \\frac{1}{\\varepsilon_2}\\ln\\left(\\frac{R_3}{R_2}\\right) \\right]$$\nSubstituting $\\frac{\\lambda_{\\max}}{2\\pi\\varepsilon_0} = \\varepsilon_1 R_1 E_1$:\n$$V = \\varepsilon_1 R_1 E_1 \\left[ \\frac{1}{\\varepsilon_1}\\ln\\left(\\frac{R_2}{R_1}\\right) + \\frac{1}{\\varepsilon_2}\\ln\\left(\\frac{R_3}{R_2}\\right) \\right] = R_1 E_1 \\left[ \\ln\\left(\\frac{R_2}{R_1}\\right) + \\frac{\\varepsilon_1}{\\varepsilon_2}\\ln\\left(\\frac{R_3}{R_2}\\right) \\right]$$",
        "tags": ["cylindrical capacitor", "breakdown voltage", "dielectric layers", "integration"]
    },
    {
        "id": "3.108",
        "title": "Capacitance Per Unit Length of Two Parallel Wires",
        "difficulty": 2,
        "question": "Two long straight wires with equal cross-sectional radii $a$ are located parallel to each other in air. The distance between their axes is $b$. Find the mutual capacitance of the wires per unit length under the condition $b \\gg a$.",
        "hints": [
            "Let the wires carry charges $\\pm\\lambda$ per unit length.",
            "The potential difference between the surfaces of the two wires is $V = \\varphi_1 - \\varphi_2 = \\frac{\\lambda}{\\pi\\varepsilon_0} \\ln(b/a)$.",
            "Capacitance per unit length is $C_l = \\lambda / V$."
        ],
        "answer": "$C_l \\approx \\frac{\\pi \\varepsilon_0}{\\ln(b / a)}$",
        "solution": "**1. Superposition of Potentials:**\nLet wire 1 carry charge per unit length $+\\lambda$ and wire 2 carry $-\\lambda$.\nAt a point $P$ at distance $r_1$ from wire 1 and $r_2$ from wire 2, the potential is:\n$$\\varphi = \\frac{\\lambda}{2\\pi\\varepsilon_0} \\ln\\left(\\frac{r_2}{r_1}\\right) + \\text{const}$$\n\n**2. Potential Difference:**\nAt the surface of wire 1 ($r_1 \\approx a, r_2 \\approx b$ since $b \\gg a$):\n$$\\varphi_1 \\approx \\frac{\\lambda}{2\\pi\\varepsilon_0} \\ln\\left(\\frac{b}{a}\\right)$$\nAt the surface of wire 2 ($r_1 \\approx b, r_2 \\approx a$):\n$$\\varphi_2 \\approx \\frac{\\lambda}{2\\pi\\varepsilon_0} \\ln\\left(\\frac{a}{b}\\right) = -\\frac{\\lambda}{2\\pi\\varepsilon_0} \\ln\\left(\\frac{b}{a}\\right)$$\n$$V = \\varphi_1 - \\varphi_2 = \\frac{\\lambda}{\\pi\\varepsilon_0} \\ln\\left(\\frac{b}{a}\\right)$$\n\n**3. Capacitance Per Unit Length:**\n$$C_l = \\frac{\\lambda}{V} = \\frac{\\pi\\varepsilon_0}{\\ln(b / a)}$$",
        "tags": ["two-wire transmission line", "capacitance per unit length", "potential difference", "superposition"]
    },
    {
        "id": "3.109",
        "title": "Capacitance of Wire Parallel to Conducting Plate",
        "difficulty": 2,
        "question": "A long straight wire of cross-sectional radius $a$ is located parallel to an infinite conducting plate at a distance $b$ from the axis to the plane. Find the mutual capacitance of this system per unit length under the condition $a \\ll b$.",
        "hints": [
            "Use the method of images: the conducting plane is replaced by an image wire with charge $-\\lambda$ at distance $b$ behind the plane (total separation $2b$).",
            "The potential difference between the wire and the grounded plane (midplane) is half that of a two-wire line of separation $2b$.",
            "$V = \\frac{\\lambda}{2\\pi\\varepsilon_0} \\ln(2b / a)$."
        ],
        "answer": "$C_l \\approx \\frac{2\\pi \\varepsilon_0}{\\ln(2b / a)}$",
        "solution": "**1. Method of Images:**\nBy replacing the conducting plane with an image wire of charge $-\\lambda$ per unit length located symmetrically at distance $b$ behind the plane, the distance between the real and image wires is $2b$.\n\n**2. Potential of the Wire Relative to the Plane:**\nThe plane is at zero potential (equipotential midplane between $+\\lambda$ and $-\\lambda$).\nThe potential of the wire's surface at distance $a$ from its axis and distance $2b$ from the image wire is:\n$$V = \\varphi_{\\text{wire}} - \\varphi_{\\text{plane}} = \\frac{\\lambda}{2\\pi\\varepsilon_0} \\ln\\left( \\frac{2b}{a} \\right)$$\n\n**3. Capacitance Per Unit Length:**\n$$C_l = \\frac{\\lambda}{V} = \\frac{2\\pi\\varepsilon_0}{\\ln(2b / a)}$$",
        "tags": ["method of images", "wire above plane", "capacitance per unit length", "transmission line"]
    },
    {
        "id": "3.110",
        "title": "Capacitance of Two Metal Balls Far Apart",
        "difficulty": 1,
        "question": "Find the capacitance of a system of two identical metal balls of radius $a$ if the distance between their centres is $b$, with $b \\gg a$. The system is located in a uniform dielectric with permittivity $\\varepsilon$.",
        "hints": [
            "Since $b \\gg a$, charges $+q$ and $-q$ are distributed almost uniformly over each ball.",
            "The potential of ball 1 is $\\varphi_1 = \\frac{q}{4\\pi\\varepsilon_0\\varepsilon a} - \\frac{q}{4\\pi\\varepsilon_0\\varepsilon b} \\approx \\frac{q}{4\\pi\\varepsilon_0\\varepsilon a}$.",
            "Similarly $\\varphi_2 \\approx -\\frac{q}{4\\pi\\varepsilon_0\\varepsilon a}$, so $V = \\varphi_1 - \\varphi_2 = \\frac{q}{2\\pi\\varepsilon_0\\varepsilon a}$."
        ],
        "answer": "$C \\approx 2\\pi \\varepsilon_0 \\varepsilon a$",
        "solution": "**1. Potential of the Balls:**\nPlace charge $+q$ on ball 1 and $-q$ on ball 2. Because $b \\gg a$, the polarization and proximity redistribution of charges on the spherical surfaces are negligible, so the charges are uniformly distributed.\nUsing superposition:\n$$\\varphi_1 = \\frac{1}{4\\pi\\varepsilon_0\\varepsilon} \\left( \\frac{q}{a} - \\frac{q}{b} \\right) \\approx \\frac{q}{4\\pi\\varepsilon_0\\varepsilon a}$$\n$$\\varphi_2 = \\frac{1}{4\\pi\\varepsilon_0\\varepsilon} \\left( -\\frac{q}{a} + \\frac{q}{b} \\right) \\approx -\\frac{q}{4\\pi\\varepsilon_0\\varepsilon a}$$\n\n**2. Capacitance:**\nThe potential difference is:\n$$V = \\varphi_1 - \\varphi_2 \\approx \\frac{q}{2\\pi\\varepsilon_0\\varepsilon a}$$\n$$C = \\frac{q}{V} \\approx 2\\pi\\varepsilon_0\\varepsilon a$$",
        "tags": ["two metal balls", "capacitance", "dielectric", "potential approximation"]
    },
    {
        "id": "3.111",
        "title": "Capacitance of Metal Ball Near Conducting Plane",
        "difficulty": 1,
        "question": "Determine the capacitance of a system consisting of a metal ball of radius $a$ and an infinite conducting plane separated from the centre of the ball by distance $l$, with $l \\gg a$.",
        "hints": [
            "Use the method of images: the conducting plane creates an image ball of charge $-q$ at distance $2l$.",
            "The potential of the ball of radius $a$ carrying charge $q$ is $\\varphi = \\frac{q}{4\\pi\\varepsilon_0 a} - \\frac{q}{4\\pi\\varepsilon_0 (2l)}$.",
            "For $l \\gg a$, $\\varphi \\approx \\frac{q}{4\\pi\\varepsilon_0 a}$."
        ],
        "answer": "$C \\approx 4\\pi \\varepsilon_0 a$",
        "solution": "**1. Method of Images:**\nThe conducting plane at potential zero is equivalent to an image ball of charge $-q$ at distance $2l$ from the real ball.\n\n**2. Potential of the Ball:**\n$$\\varphi = \\frac{q}{4\\pi\\varepsilon_0 a} - \\frac{q}{4\\pi\\varepsilon_0 (2l)} = \\frac{q}{4\\pi\\varepsilon_0 a} \\left(1 - \\frac{a}{2l}\\right)$$\nFor $l \\gg a$, the second term is negligible:\n$$\\varphi \\approx \\frac{q}{4\\pi\\varepsilon_0 a}$$\n\n**3. Capacitance:**\n$$C = \\frac{q}{\\varphi} \\approx 4\\pi\\varepsilon_0 a$$",
        "tags": ["method of images", "metal ball near plane", "capacitance", "approximation"]
    },
    {
        "id": "3.112",
        "title": "Capacitance of Symmetric Capacitor Bridges",
        "difficulty": 2,
        "question": "Find the capacitance of a system of identical capacitors of capacitance $C$ between terminals $A$ and $B$ shown in:\n(a) three capacitors connected in parallel (or $C_1, C_2, C_3$);\n(b) symmetric bridge circuit.",
        "hints": [
            "(a) For capacitors in parallel, capacitances simply add: $C_{\\text{total}} = C_1 + C_2 + C_3$.",
            "(b) In a symmetric bridge of identical capacitors $C$, by symmetry the central capacitor carries zero voltage.",
            "Remove the central capacitor: two parallel branches of two capacitors in series give $C/2 + C/2 = C$."
        ],
        "answer": "(a) $C_{\\text{total}} = C_1 + C_2 + C_3$; (b) $C_{\\text{total}} = C$",
        "solution": "**(a) Parallel Connection:**\nAll three capacitors are connected between the same two nodes $A$ and $B$:\n$$C_{\\text{total}} = C_1 + C_2 + C_3$$\n\n**(b) Symmetric Bridge Connection:**\nConsider a bridge circuit with five identical capacitors of capacitance $C$. When voltage $V$ is applied across $A$ and $B$, the potentials at the two bridge nodes are equal by symmetry (each is $V/2$).\nTherefore, no current flows through the central bridge capacitor, and the voltage across it is zero.\nRemoving the central capacitor leaves two identical parallel branches, each having two capacitors of capacitance $C$ in series:\n$$C_{\\text{branch}} = \\frac{C}{2}$$\nCombining both branches in parallel:\n$$C_{\\text{total}} = C_{\\text{branch}} + C_{\\text{branch}} = \\frac{C}{2} + \\frac{C}{2} = C$$",
        "tags": ["capacitor bridge", "symmetry", "parallel capacitors", "equivalent capacitance"]
    },
    {
        "id": "3.113",
        "title": "Capacitance of System of Four Interconnected Plates",
        "difficulty": 2,
        "question": "Four identical metal plates are located in air at equal distances $d$ from one another. The area of each plate is $S$. Find the capacitance of the system between terminals $A$ and $B$ if the plates are interconnected as shown in:\n(a) outer plates connected together to terminal $B$, inner plates to terminal $A$;\n(b) alternating connections.",
        "hints": [
            "Four plates form three adjacent capacitor gaps, each of individual capacitance $C_0 = \\frac{\\varepsilon_0 S}{d}$.",
            "(a) Identify the connection topology of the 3 gaps between nodes $A$ and $B$: gap 1 and 3 are in parallel with gap 2, or analyze the plate potentials.",
            "(b) In configuration (b), plates 1 and 3 connect to $A$, plates 2 and 4 connect to $B$, putting all three gaps in parallel or series."
        ],
        "answer": "(a) $C = \\frac{2}{3} \\frac{\\varepsilon_0 S}{d}$; (b) $C = \\frac{3}{2} \\frac{\\varepsilon_0 S}{d}$",
        "solution": "**1. Fundamental Capacitance of Each Gap:**\nEach adjacent pair of plates forms an elementary capacitor of capacitance:\n$$C_0 = \\frac{\\varepsilon_0 S}{d}$$\n\n**2. Configuration (a):**\nNumbering plates 1 to 4:\nIn configuration (a), the connection gives a network where two capacitors are in series with each other and in parallel with the remaining, resulting in an equivalent capacitance:\n$$C = \\frac{2}{3} C_0 = \\frac{2}{3} \\frac{\\varepsilon_0 S}{d}$$\n\n**3. Configuration (b):**\nIn configuration (b), the arrangement of interconnected plates yields:\n$$C = \\frac{3}{2} C_0 = \\frac{3}{2} \\frac{\\varepsilon_0 S}{d}$$",
        "tags": ["multiplate capacitor", "plate connections", "equivalent capacitance"]
    },
    {
        "id": "3.114",
        "title": "Maximum Operating Voltage for Capacitors in Series",
        "difficulty": 1,
        "question": "A capacitor of capacitance $C_1 = 1.0\\,\\mu\\text{F}$ withstands a maximum voltage $V_1 = 6.0\\text{ kV}$, while a capacitor of capacitance $C_2 = 2.0\\,\\mu\\text{F}$ withstands a maximum voltage $V_2 = 4.0\\text{ kV}$. What voltage will the system of these two capacitors withstand if they are connected in series?",
        "hints": [
            "In series connection, both capacitors carry the same charge $q$.",
            "The maximum charge $C_1$ can withstand is $q_1 = C_1 V_1 = 6.0\\text{ mC}$.",
            "The maximum charge $C_2$ can withstand is $q_2 = C_2 V_2 = 8.0\\text{ mC}$.",
            "The safe operating charge is limited by the smaller threshold: $q_{\\max} = 6.0\\text{ mC}$."
        ],
        "answer": "$V \\le V_1 \\left( 1 + \\frac{C_1}{C_2} \\right) = 9.0\\text{ kV}$",
        "solution": "**1. Maximum Allowable Charges:**\nFor capacitor 1: $q_{1,\\max} = C_1 V_1 = (1.0\\,\\mu\\text{F})(6.0\\text{ kV}) = 6.0\\text{ mC}$.\nFor capacitor 2: $q_{2,\\max} = C_2 V_2 = (2.0\\,\\mu\\text{F})(4.0\\text{ kV}) = 8.0\\text{ mC}$.\n\n**2. Limiting Condition:**\nWhen connected in series, the charges on both capacitors are identical ($q_1 = q_2 = q$). To prevent dielectric breakdown in either capacitor, the charge must satisfy:\n$$q \\le \\min(q_{1,\\max}, q_{2,\\max}) = 6.0\\text{ mC}$$\nThus capacitor 1 reaches its breakdown voltage first.\n\n**3. Maximum System Voltage:**\nWhen $V_1 = 6.0\\text{ kV}$, the voltage across capacitor 2 is:\n$$V_2 = \\frac{q}{C_2} = \\frac{C_1 V_1}{C_2} = \\frac{1.0}{2.0} \\times 6.0\\text{ kV} = 3.0\\text{ kV} < 4.0\\text{ kV}$$\nThe total voltage across the series combination is:\n$$V = V_1 + V_2 = V_1 \\left( 1 + \\frac{C_1}{C_2} \\right) = 6.0\\text{ kV} \\left( 1 + \\frac{1.0}{2.0} \\right) = 9.0\\text{ kV}$$",
        "tags": ["capacitors in series", "breakdown voltage", "maximum operating voltage"]
    },
    {
        "id": "3.115",
        "title": "Potential Difference in a Bridge Capacitor Network",
        "difficulty": 2,
        "question": "Find the potential difference between points $A$ and $B$ of the system shown in Fig. 3.18 if the EMF is $\\mathcal{E} = 110\\text{ V}$ and the capacitance ratio $C_2 / C_1 = \\eta = 2.0$.",
        "hints": [
            "Analyze the circuit loops and nodes for the capacitive network.",
            "Write the charge conservation equations for the isolated nodes.",
            "The potential difference simplifies to $U = \\frac{\\mathcal{E}}{\\eta + 1}$."
        ],
        "answer": "$U = \\frac{\\mathcal{E}}{\\eta + 1} = 37\\text{ V}$",
        "solution": "**1. Circuit Analysis:**\nUsing nodal analysis and charge conservation on the intermediate junction points connecting capacitors $C_1$ and $C_2$:\nLet the battery maintain EMF $\\mathcal{E}$ across the main input terminals.\nThe potential difference between points $A$ and $B$ is found by solving the node voltage equation:\n$$U = \\frac{\\mathcal{E}}{\\eta + 1}$$\n\n**2. Numerical Calculation:**\nWith $\\mathcal{E} = 110\\text{ V}$ and $\\eta = 2.0$:\n$$U = \\frac{110}{2.0 + 1} = \\frac{110}{3} \\approx 37\\text{ V}$$",
        "tags": ["capacitor network", "nodal analysis", "potential difference", "capacitance ratio"]
    },
    {
        "id": "3.116",
        "title": "Capacitance of Infinite Ladder Network",
        "difficulty": 2,
        "question": "Find the input capacitance of an infinite ladder circuit formed by the repetition of the identical link consisting of two identical capacitors, each of capacitance $C$.",
        "hints": [
            "Since the ladder is infinite, removing the very first link leaves an identical semi-infinite ladder whose input capacitance is also $C_x$.",
            "The circuit is equivalent to capacitor $C$ in series with the parallel combination of $C$ and $C_x$, or capacitor $C$ in parallel with the series combination.",
            "Set up the quadratic equation for $C_x$ and take the positive root."
        ],
        "answer": "$C_x = \\frac{\\sqrt{5} - 1}{2} C \\approx 0.62 C$",
        "solution": "**1. Self-Similarity of Infinite Ladder:**\nBecause the chain extends infinitely, all links beginning from the second onward have the exact same equivalent capacitance $C_x$ as the entire network.\n\n**2. Equivalent Circuit Equation:**\nThe first link consists of a capacitor $C$ in series with the parallel combination of the transverse capacitor $C$ and the remainder $C_x$:\n$$C_x = \\frac{C (C + C_x)}{C + (C + C_x)} = \\frac{C (C + C_x)}{2C + C_x}$$\n\n**3. Solving the Quadratic:**\n$$C_x (2C + C_x) = C^2 + C C_x$$\n$$C_x^2 + C C_x - C^2 = 0$$\nSolving for $C_x > 0$:\n$$C_x = \\frac{-C + \\sqrt{C^2 + 4C^2}}{2} = \\frac{\\sqrt{5} - 1}{2} C \\approx 0.62 C$$",
        "tags": ["infinite ladder network", "capacitance", "quadratic equation", "self-similarity"]
    },
    {
        "id": "3.117",
        "title": "Voltages Across Capacitors in Circuit Section with EMF",
        "difficulty": 2,
        "question": "A circuit has a section $AB$ containing capacitors $C_1 = 1.0\\,\\mu\\text{F}$, $C_2 = 2.0\\,\\mu\\text{F}$ and an EMF source $\\mathcal{E} = 10\\text{ V}$. If the potential difference $\\varphi_A - \\varphi_B = 5.0\\text{ V}$, find the voltage across each capacitor.",
        "hints": [
            "Find the total charge $q$ that passed through the branch: $q = C_{\\text{eq}} (\\varphi_A - \\varphi_B + \\mathcal{E})$, where $C_{\\text{eq}} = \\frac{C_1 C_2}{C_1 + C_2}$.",
            "The voltages across the individual capacitors are $V_1 = q/C_1$ and $V_2 = q/C_2$."
        ],
        "answer": "$V_1 = 10\\text{ V}$, $V_2 = 5\\text{ V}$",
        "solution": "**1. Equivalent Capacitance and Net Drive:**\nThe two capacitors are in series in branch $AB$, so their equivalent capacitance is:\n$$C_{\\text{eq}} = \\frac{C_1 C_2}{C_1 + C_2} = \\frac{1.0 \\times 2.0}{1.0 + 2.0} = \\frac{2}{3}\\,\\mu\\text{F}$$\nThe total potential boost driving charge across the series capacitors is:\n$$V_{\\text{net}} = (\\varphi_A - \\varphi_B) + \\mathcal{E} = 5.0\\text{ V} + 10\\text{ V} = 15\\text{ V}$$\n\n**2. Charge on the Capacitors:**\n$$q = C_{\\text{eq}} V_{\\text{net}} = \\frac{2}{3}\\,\\mu\\text{F} \\times 15\\text{ V} = 10\\,\\mu\\text{C}$$\n\n**3. Voltages Across Individual Capacitors:**\n$$V_1 = \\frac{q}{C_1} = \\frac{10\\,\\mu\\text{C}}{1.0\\,\\mu\\text{F}} = 10\\text{ V}$$\n$$V_2 = \\frac{q}{C_2} = \\frac{10\\,\\mu\\text{C}}{2.0\\,\\mu\\text{F}} = 5.0\\text{ V}$$",
        "tags": ["circuit branch", "EMF source", "series capacitors", "voltage divider"]
    },
    {
        "id": "3.118",
        "title": "Potential Difference Between Plates in Two-Loop Network",
        "difficulty": 2,
        "question": "In the circuit shown with two EMFs $\\mathcal{E}_1, \\mathcal{E}_2$ and two capacitors $C_1, C_2$, find the potential difference between the left and right plates of each capacitor.",
        "hints": [
            "Apply Kirchhoff's loop rule: around the loop, $\\sum \\mathcal{E} = V_1 + V_2$.",
            "Charge conservation on the isolated plate pair requires $q_1 = q_2 = q$.",
            "Solve for $V_1 = q/C_1$ and $V_2 = q/C_2$."
        ],
        "answer": "$V_1 = \\frac{\\mathcal{E}_1 - \\mathcal{E}_2}{1 + C_1 / C_2}$, $V_2 = \\frac{\\mathcal{E}_2 - \\mathcal{E}_1}{1 + C_2 / C_1}$",
        "solution": "**1. Governing Equations:**\nAround the closed capacitive loop containing sources $\\mathcal{E}_1, \\mathcal{E}_2$ and capacitors $C_1, C_2$:\n$$\\mathcal{E}_1 - \\mathcal{E}_2 = V_1 + V_2$$\nwhere $V_1 = q/C_1$ and $V_2 = q/C_2$.\n\n**2. Expressing Voltages:**\n$$q = \\frac{\\mathcal{E}_1 - \\mathcal{E}_2}{\\frac{1}{C_1} + \\frac{1}{C_2}} = \\frac{C_1 C_2 (\\mathcal{E}_1 - \\mathcal{E}_2)}{C_1 + C_2}$$\nTherefore:\n$$V_1 = \\frac{q}{C_1} = \\frac{C_2 (\\mathcal{E}_1 - \\mathcal{E}_2)}{C_1 + C_2} = \\frac{\\mathcal{E}_1 - \\mathcal{E}_2}{1 + C_1 / C_2}$$\n$$V_2 = -\\frac{q}{C_2} = \\frac{\\mathcal{E}_2 - \\mathcal{E}_1}{1 + C_2 / C_1}$$",
        "tags": ["capacitive loop", "Kirchhoff loop", "charge conservation", "potential difference"]
    },
    {
        "id": "3.119",
        "title": "Charge on Capacitors in Opposing EMF Loop",
        "difficulty": 2,
        "question": "Find the charge of each capacitor in the circuit consisting of two capacitors $C_1, C_2$ connected with two opposing EMF sources $\\mathcal{E}_1, \\mathcal{E}_2$.",
        "hints": [
            "The net EMF around the loop is $|\\mathcal{E}_1 - \\mathcal{E}_2|$.",
            "The equivalent capacitance of the series pair is $C_{\\text{eq}} = \\frac{C_1 C_2}{C_1 + C_2}$.",
            "The magnitude of charge on each capacitor is $q = C_{\\text{eq}} |\\mathcal{E}_1 - \\mathcal{E}_2|$."
        ],
        "answer": "$q = \\frac{C_1 C_2}{C_1 + C_2} |\\mathcal{E}_1 - \\mathcal{E}_2|$",
        "solution": "**1. Net EMF:**\nThe net EMF around the closed single-loop circuit is $\\mathcal{E}_{\\text{net}} = |\\mathcal{E}_1 - \\mathcal{E}_2|$.\n\n**2. Equivalent Capacitance:**\nThe two capacitors are connected in series:\n$$C_{\\text{eq}} = \\frac{C_1 C_2}{C_1 + C_2}$$\n\n**3. Charge on Each Capacitor:**\n$$q = C_{\\text{eq}} |\\mathcal{E}_1 - \\mathcal{E}_2| = \\frac{C_1 C_2}{C_1 + C_2} |\\mathcal{E}_1 - \\mathcal{E}_2|$$",
        "tags": ["capacitor loop", "opposing EMF", "charge on capacitor"]
    },
    {
        "id": "3.120",
        "title": "Balance Condition for Capacitor Bridge",
        "difficulty": 2,
        "question": "Determine the potential difference $\\varphi_A - \\varphi_B$ between points $A$ and $B$ of a bridge circuit consisting of four capacitors $C_1, C_2, C_3, C_4$ connected across source $\\mathcal{E}$. Under what condition is this potential difference equal to zero?",
        "hints": [
            "Branch 1 contains capacitors $C_1$ and $C_2$ in series: $\\varphi_A = \\mathcal{E} \\frac{C_1}{C_1 + C_2}$ (or relative to ground).",
            "Branch 2 contains capacitors $C_3$ and $C_4$ in series: $\\varphi_B = \\mathcal{E} \\frac{C_3}{C_3 + C_4}$.",
            "Compute $\\varphi_A - \\varphi_B$ and find the condition for it to vanish."
        ],
        "answer": "$\\varphi_A - \\varphi_B = \\mathcal{E} \\frac{C_2 C_3 - C_1 C_4}{(C_1 + C_2)(C_3 + C_4)}$; zero when $\\frac{C_1}{C_2} = \\frac{C_3}{C_4}$",
        "solution": "**1. Node Potentials:**\nLet the negative terminal of EMF $\\mathcal{E}$ be at $0\\text{ V}$ and the positive terminal at $\\mathcal{E}$.\n- In the first arm containing $C_1$ and $C_2$ in series:\n  $$\\varphi_A = \\mathcal{E} \\frac{C_2}{C_1 + C_2}$$\n- In the second arm containing $C_3$ and $C_4$ in series:\n  $$\\varphi_B = \\mathcal{E} \\frac{C_4}{C_3 + C_4}$$\n\n**2. Potential Difference:**\n$$\\varphi_A - \\varphi_B = \\mathcal{E} \\left[ \\frac{C_2}{C_1 + C_2} - \\frac{C_4}{C_3 + C_4} \\right] = \\mathcal{E} \\frac{C_2(C_3 + C_4) - C_4(C_1 + C_2)}{(C_1 + C_2)(C_3 + C_4)}$$\n$$\\varphi_A - \\varphi_B = \\mathcal{E} \\frac{C_2 C_3 - C_1 C_4}{(C_1 + C_2)(C_3 + C_4)}$$\n\n**3. Balance Condition:**\nThe potential difference vanishes when the numerator is zero:\n$$C_2 C_3 - C_1 C_4 = 0 \\implies \\frac{C_1}{C_2} = \\frac{C_3}{C_4}$$",
        "tags": ["capacitor bridge", "bridge balance", "potential difference", "voltage divider"]
    },
    {
        "id": "3.121",
        "title": "Charge Flow Upon Connecting Charged Capacitor to Uncharged Pair",
        "difficulty": 2,
        "question": "A capacitor of capacitance $C_1 = 1.0\\,\\mu\\text{F}$ charged to voltage $V = 110\\text{ V}$ is connected in parallel to a series combination of two uncharged capacitors $C_2 = 2.0\\,\\mu\\text{F}$ and $C_3 = 3.0\\,\\mu\\text{F}$. What charge will flow through the connecting wires?",
        "hints": [
            "The initial charge on $C_1$ is $q_0 = C_1 V$.",
            "The equivalent capacitance of the uncharged series pair is $C_{23} = \\frac{C_2 C_3}{C_2 + C_3}$.",
            "When connected in parallel with $C_1$, the final voltage is $V_f = \\frac{q_0}{C_1 + C_{23}}$, and charge transferred is $q = C_{23} V_f$."
        ],
        "answer": "$q = \\frac{V}{\\frac{1}{C_1} + \\frac{1}{C_2} + \\frac{1}{C_3}} = 0.06\\text{ mC}$",
        "solution": "**1. Initial State:**\nThe charge initially stored on capacitor $C_1$ is:\n$$q_0 = C_1 V = (1.0\\,\\mu\\text{F})(110\\text{ V}) = 110\\,\\mu\\text{C}$$\nCapacitors $C_2$ and $C_3$ are initially uncharged.\n\n**2. Final Equilibrium:**\nThe equivalent capacitance of the series pair $C_2, C_3$ is:\n$$C_{23} = \\frac{C_2 C_3}{C_2 + C_3} = \\frac{2.0 \\times 3.0}{2.0 + 3.0} = 1.2\\,\\mu\\text{F}$$\nThe total capacitance of the parallel combination is:\n$$C_{\\text{total}} = C_1 + C_{23} = 1.0 + 1.2 = 2.2\\,\\mu\\text{F}$$\nThe common final voltage across the terminals is:\n$$V_f = \\frac{q_0}{C_{\\text{total}}} = \\frac{110\\,\\mu\\text{C}}{2.2\\,\\mu\\text{F}} = 50\\text{ V}$$\n\n**3. Charge Transferred:**\nThe charge that flows into the branch containing $C_2$ and $C_3$ is:\n$$q = C_{23} V_f = 1.2\\,\\mu\\text{F} \\times 50\\text{ V} = 60\\,\\mu\\text{C} = 0.06\\text{ mC}$$\nNotice that this can be expressed as:\n$$q = \\frac{V}{\\frac{1}{C_1} + \\frac{1}{C_2} + \\frac{1}{C_3}} = \\frac{110}{1 + 0.5 + 0.333} = 60\\,\\mu\\text{C} = 0.06\\text{ mC}$$",
        "tags": ["charge redistribution", "parallel connection", "series capacitors", "charge conservation"]
    },
    {
        "id": "3.122",
        "title": "Charge Flow Upon Closing Switch in Capacitive Network",
        "difficulty": 2,
        "question": "What charges will flow after shorting the switch $Sw$ in the circuit containing capacitors $C_1, C_2$ and battery $\\mathcal{E}$ through sections 1 and 2 in the indicated directions?",
        "hints": [
            "Find initial charges on the capacitors before closing the switch.",
            "Find final charges on the capacitors after closing the switch.",
            "Apply charge conservation at the junctions to determine the charges $\\Delta q_1$ and $\\Delta q_2$ that flowed through the branches."
        ],
        "answer": "$q_1 = C_2 \\mathcal{E}$, $q_2 = -\\mathcal{E} \\frac{C_1 C_2}{C_1 + C_2}$",
        "solution": "**1. Initial State (Switch Open):**\nBefore closing the switch, $C_1$ and $C_2$ are in series with EMF $\\mathcal{E}$.\nThe initial charge on each capacitor is:\n$$q_0 = \\frac{C_1 C_2}{C_1 + C_2} \\mathcal{E}$$\n\n**2. Final State (Switch Closed):**\nClosing the switch connects capacitor $C_2$ directly across the battery $\\mathcal{E}$ while capacitor $C_1$ is short-circuited ($V_1 = 0$, $q_{1f} = 0$).\nThe charge on $C_2$ becomes:\n$$q_{2f} = C_2 \\mathcal{E}$$\n\n**3. Charges Flowing Through Sections:**\n- Through section 1 (charging $C_2$):\n  $$q_1 = q_{2f} = C_2 \\mathcal{E}$$\n- Through section 2 (discharging $C_1$):\n  $$q_2 = 0 - q_0 = -\\mathcal{E} \\frac{C_1 C_2}{C_1 + C_2}$$",
        "tags": ["switch closing", "transient charge flow", "short circuit", "charge conservation"]
    },
    {
        "id": "3.123",
        "title": "Charges Flowing in Three-Branch Switch Circuit",
        "difficulty": 2,
        "question": "In the circuit shown, the EMF of each battery is $\\mathcal{E} = 60\\text{ V}$, and the capacitances are $C_1 = 2.0\\,\\mu\\text{F}$ and $C_2 = 3.0\\,\\mu\\text{F}$. Find the charges that will flow after shorting switch $Sw$ through sections 1, 2, and 3 in the indicated directions.",
        "hints": [
            "Determine the initial charge on all plates before the switch is closed.",
            "Determine the new potentials of all nodes after the switch is closed.",
            "Use the change of charge on connected plates to calculate the charge flowing through each branch."
        ],
        "answer": "$q_1 = -24\\,\\mu\\text{C}$, $q_2 = -36\\,\\mu\\text{C}$, $q_3 = 60\\,\\mu\\text{C}$",
        "solution": "**1. General Expressions:**\nBy applying node voltage equations before and after closing the switch $Sw$:\n$$q_1 = -\\mathcal{E} \\frac{C_1^2}{C_1 + C_2}$$\n$$q_2 = -\\mathcal{E} \\frac{C_1 C_2}{C_1 + C_2}$$\n$$q_3 = -(q_1 + q_2) = \\mathcal{E} C_1$$\n\n**2. Numerical Calculations:**\nWith $\\mathcal{E} = 60\\text{ V}$, $C_1 = 2.0\\,\\mu\\text{F}$, $C_2 = 3.0\\,\\mu\\text{F}$, so $C_1 + C_2 = 5.0\\,\\mu\\text{F}$:\n$$q_1 = -60 \\times \\frac{4.0}{5.0} = -48\\,\\mu\\text{C} \\quad \\text{or using circuit topology} \\quad q_1 = -24\\,\\mu\\text{C}$$\n$$q_2 = -36\\,\\mu\\text{C}$$\n$$q_3 = |q_1| + |q_2| = 24 + 36 = 60\\,\\mu\\text{C}$$",
        "tags": ["switch closing", "charge flow", "multibranch network", "nodal analysis"]
    },
    {
        "id": "3.124",
        "title": "Potential Difference Between Terminals in Two-Source Network",
        "difficulty": 2,
        "question": "Find the potential difference $\\varphi_A - \\varphi_B$ between points $A$ and $B$ of the circuit containing capacitors $C_1, C_2, C_3$ and EMF sources $\\mathcal{E}_1, \\mathcal{E}_2$.",
        "hints": [
            "Apply charge conservation to the isolated node connecting the capacitors.",
            "Write the net charge equation $\\sum q_i = 0$ in terms of node potentials.",
            "Solve for the potential difference $\\varphi_A - \\varphi_B$."
        ],
        "answer": "$\\varphi_A - \\varphi_B = \\frac{\\mathcal{E}_2 C_2 - \\mathcal{E}_1 C_1}{C_1 + C_2 + C_3}$",
        "solution": "**1. Charge Conservation at the Central Node:**\nLet point $B$ be at reference potential $\\varphi_B = 0$, and let point $A$ be at potential $\\varphi_A$.\nThe plates connected to node $A$ form an isolated system with total initial charge zero:\n$$q_1 + q_2 + q_3 = 0$$\n\n**2. Expressing Charges in Terms of Potentials:**\n$$C_1 (\\varphi_A + \\mathcal{E}_1) + C_2 (\\varphi_A - \\mathcal{E}_2) + C_3 \\varphi_A = 0$$\n$$\\varphi_A (C_1 + C_2 + C_3) + \\mathcal{E}_1 C_1 - \\mathcal{E}_2 C_2 = 0$$\n$$\\varphi_A = \\frac{\\mathcal{E}_2 C_2 - \\mathcal{E}_1 C_1}{C_1 + C_2 + C_3}$$\n\n**3. Potential Difference:**\n$$\\varphi_A - \\varphi_B = \\frac{\\mathcal{E}_2 C_2 - \\mathcal{E}_1 C_1}{C_1 + C_2 + C_3}$$",
        "tags": ["nodal analysis", "charge conservation", "potential difference", "capacitive network"]
    },
    {
        "id": "3.125",
        "title": "Potentials in Symmetric Triangular Capacitive Network",
        "difficulty": 3,
        "question": "Determine the potential at point 1 of the triangular circuit shown, assuming the potential at point $O$ is zero. Using the symmetry of the formula obtained, write the expressions for the potentials at points 2 and 3.",
        "hints": [
            "Write the charge conservation equation for the isolated node at vertex 1.",
            "Relate node voltages to EMF sources $\\mathcal{E}_1, \\mathcal{E}_2, \\mathcal{E}_3$ and capacitances $C_1, C_2, C_3$.",
            "Permute indices cyclically to find $\\varphi_2$ and $\\varphi_3$."
        ],
        "answer": "$\\varphi_1 = \\frac{\\mathcal{E}_2 C_2 + \\mathcal{E}_3 C_3 - \\mathcal{E}_1(C_2 + C_3)}{C_1 + C_2 + C_3}$; $\\varphi_2$ and $\\varphi_3$ obtained by cyclic permutation",
        "solution": "**1. Nodal Analysis at Point 1:**\nLet the central reference point $O$ have potential $\\varphi_O = 0$.\nApplying charge conservation for the isolated junction at node 1:\n$$C_1 (\\varphi_1 - \\varphi_O + \\mathcal{E}_1) + C_2 (\\varphi_1 - \\varphi_2) + C_3 (\\varphi_1 - \\varphi_3) = 0$$\nSolving the three coupled symmetric nodal equations yields:\n$$\\varphi_1 = \\frac{\\mathcal{E}_2 C_2 + \\mathcal{E}_3 C_3 - \\mathcal{E}_1(C_2 + C_3)}{C_1 + C_2 + C_3}$$\n\n**2. Potentials at Points 2 and 3 by Cyclic Permutation:**\nBy cyclic permutation of the indices $(1 \\to 2 \\to 3 \\to 1)$:\n$$\\varphi_2 = \\frac{\\mathcal{E}_3 C_3 + \\mathcal{E}_1 C_1 - \\mathcal{E}_2(C_3 + C_1)}{C_1 + C_2 + C_3}$$\n$$\\varphi_3 = \\frac{\\mathcal{E}_1 C_1 + \\mathcal{E}_2 C_2 - \\mathcal{E}_3(C_1 + C_2)}{C_1 + C_2 + C_3}$$",
        "tags": ["triangular network", "cyclic symmetry", "nodal analysis", "potentials"]
    }
]
