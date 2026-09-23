"""
part3_ch3_1a.py
Curated problems 3.1 to 3.25 (25 problems) of Irodov Chapter 3.1:
Constant Electric Field in Vacuum (Part A).
"""

CH3_1A_CURATED = [
    {
        "id": "3.1",
        "title": "Ratio of Electrostatic to Gravitational Forces",
        "difficulty": 1,
        "question": "Calculate the ratio of the electrostatic to gravitational interaction forces between two electrons and two protons. At what specific charge $q/m$ of a particle would these two forces balance each other?",
        "hints": [
            "Coulomb's law gives $F_e = \\frac{1}{4\\pi\\varepsilon_0} \\frac{e^2}{r^2}$; Newton's law gives $F_g = G \\frac{m^2}{r^2}$.",
            "The ratio is $\\frac{F_e}{F_g} = \\frac{e^2}{4\\pi\\varepsilon_0 G m^2}$. Calculate this for electrons ($m_e = 9.11 \\times 10^{-31}\\text{ kg}$) and protons ($m_p = 1.67 \\times 10^{-27}\\text{ kg}$).",
            "For force balance $F_e = F_g$, set $\\frac{q^2}{4\\pi\\varepsilon_0 r^2} = \\frac{G m^2}{r^2} \\implies \\frac{q}{m} = \\sqrt{4\\pi\\varepsilon_0 G}$."
        ],
        "answer": "$\\frac{F_e}{F_g} \\approx 4 \\times 10^{42}$ (electrons), $\\approx 1 \\times 10^{36}$ (protons); $\\quad \\frac{q}{m} = \\sqrt{4\\pi\\varepsilon_0 G} = 0.86 \\times 10^{-10}\\text{ C/kg}$",
        "solution": "**1. Ratio of Electrostatic to Gravitational Forces:**\nBoth forces obey the inverse-square law, so the distance $r$ cancels out:\n$$\\frac{F_e}{F_g} = \\frac{\\frac{e^2}{4\\pi\\varepsilon_0 r^2}}{\\frac{G m^2}{r^2}} = \\frac{e^2}{4\\pi\\varepsilon_0 G m^2}$$\n- For two electrons ($m_e = 9.109 \\times 10^{-31}\\text{ kg}$):\n  $$\\frac{F_e}{F_g} = \\frac{(1.602 \\times 10^{-19})^2 \\times 8.988 \\times 10^9}{6.674 \\times 10^{-11} \\times (9.109 \\times 10^{-31})^2} \\approx 4.17 \\times 10^{42} \\approx 4 \\times 10^{42}$$\n- For two protons ($m_p = 1.673 \\times 10^{-27}\\text{ kg}$):\n  $$\\frac{F_e}{F_g} = \\frac{(1.602 \\times 10^{-19})^2 \\times 8.988 \\times 10^9}{6.674 \\times 10^{-11} \\times (1.673 \\times 10^{-27})^2} \\approx 1.24 \\times 10^{36} \\approx 1 \\times 10^{36}$$\n\n**2. Specific Charge for Force Balance:**\nSetting $F_e = F_g$:\n$$\\frac{1}{4\\pi\\varepsilon_0} \\frac{q^2}{r^2} = G \\frac{m^2}{r^2} \\implies \\left(\\frac{q}{m}\\right)^2 = 4\\pi\\varepsilon_0 G$$\n$$\\frac{q}{m} = \\sqrt{4\\pi\\varepsilon_0 G} = \\sqrt{\\frac{6.674 \\times 10^{-11}}{8.988 \\times 10^9}} = \\sqrt{7.426 \\times 10^{-21}} \\approx 0.86 \\times 10^{-10}\\text{ C/kg}$$",
        "tags": ["Coulomb law", "gravitational force", "specific charge", "fundamental forces"]
    },
    {
        "id": "3.2",
        "title": "Coulomb Force from Fractional Charge Imbalance",
        "difficulty": 2,
        "question": "What would be the interaction force between two copper spheres, each of mass $m = 1.0\\text{ g}$, separated by a distance $r = 1.0\\text{ m}$, if the total electronic charge in them differed from the total nuclear charge by $1\\%$?",
        "hints": [
            "Find the number of copper atoms in $m = 1.0\\text{ g}$: $N = \\frac{m}{M} N_A$, with $M = 63.55\\text{ g/mol}$.",
            "Each copper atom has atomic number $Z = 29$, so total electronic charge is $Q = Z e N$.",
            "A $1\\%$ charge difference gives net charge $q = 0.01 Q$. Calculate $F = \\frac{q^2}{4\\pi\\varepsilon_0 r^2}$."
        ],
        "answer": "$F \\approx 2 \\times 10^{15}\\text{ N}$",
        "solution": "**1. Total Electronic Charge:**\nFor copper, atomic number $Z = 29$ and molar mass $M = 63.55\\text{ g/mol}$:\n$$N = \\frac{m}{M} N_A = \\frac{1.0\\text{ g}}{63.55\\text{ g/mol}} \\times 6.022 \\times 10^{23}\\text{ mol}^{-1} \\approx 9.476 \\times 10^{21}\\text{ atoms}$$\nThe total magnitude of electronic charge in each sphere is:\n$$Q = Z e N = 29 \\times (1.602 \\times 10^{-19}\\text{ C}) \\times 9.476 \\times 10^{21} \\approx 4.40 \\times 10^4\\text{ C}$$\n\n**2. Net Charge and Interaction Force:**\nA $1\\%$ imbalance produces an uncompensated charge:\n$$q = 0.01 Q = 4.40 \\times 10^2\\text{ C}$$\nThe repulsive Coulomb force at distance $r = 1.0\\text{ m}$ is:\n$$F = \\frac{1}{4\\pi\\varepsilon_0} \\frac{q^2}{r^2} = (8.988 \\times 10^9) \\times \\frac{(440)^2}{1.0^2} \\approx 1.74 \\times 10^{15}\\text{ N} \\approx 2 \\times 10^{15}\\text{ N}$$\n(This astronomical force illustrates why matter must be electrically neutral to an extraordinary degree of precision).",
        "tags": ["charge imbalance", "Coulomb force", "atomic structure", "copper"]
    },
    {
        "id": "3.3",
        "title": "Rate of Charge Leakage from Repelling Spheres",
        "difficulty": 2,
        "question": "Two small equally charged spheres, each of mass $m$, are suspended from the same point by silk threads of length $l$. The distance between the spheres $x \\ll l$. As a result of the leaking of the charge from both spheres with a constant rate, the spheres approach each other with velocity $v = a / \\sqrt{x}$, where $a$ is a constant. Find the rate of charge leakage $\\frac{dq}{dt}$.",
        "hints": [
            "At small separation $x \\ll l$, the angle of deflection is small: $\\tan\\theta \\approx \\frac{x}{2l} = \\frac{F_e}{mg}$.",
            "Substitute Coulomb's force $F_e = \\frac{q^2}{4\\pi\\varepsilon_0 x^2}$ to find $q(x) = x^{3/2} \\sqrt{\\frac{2\\pi\\varepsilon_0 mg}{l}}$.",
            "Differentiate with respect to time: $\\frac{dq}{dt} = \\frac{3}{2} x^{1/2} \\frac{dx}{dt} \\sqrt{\\dots}$, and use $\\frac{dx}{dt} = -v = -\\frac{a}{\\sqrt{x}}$."
        ],
        "answer": "$\\frac{dq}{dt} = \\frac{3}{2} a \\sqrt{\\frac{2\\pi\\varepsilon_0 mg}{l}}$",
        "solution": "**1. Equilibrium Condition:**\nEach sphere experiences three forces: tension $T$, gravity $mg$, and electrostatic repulsion $F_e$. For small deflection angles $\\theta$:\n$$\\tan\\theta \\approx \\sin\\theta = \\frac{x/2}{l} = \\frac{x}{2l}$$\nFrom force balance:\n$$\\tan\\theta = \\frac{F_e}{mg} = \\frac{q^2}{4\\pi\\varepsilon_0 mg x^2}$$\n$$\\frac{x}{2l} = \\frac{q^2}{4\\pi\\varepsilon_0 mg x^2} \\implies q^2 = \\frac{2\\pi\\varepsilon_0 mg}{l} x^3$$\n$$q = \\sqrt{\\frac{2\\pi\\varepsilon_0 mg}{l}} x^{3/2}$$\n\n**2. Rate of Charge Leakage:**\nDifferentiating both sides with respect to time $t$:\n$$\\frac{dq}{dt} = \\frac{3}{2} \\sqrt{\\frac{2\\pi\\varepsilon_0 mg}{l}} x^{1/2} \\frac{dx}{dt}$$\nSince the spheres approach each other with speed $v = -\\frac{dx}{dt} = \\frac{a}{\\sqrt{x}}$, we have $x^{1/2} \\left(-\\frac{dx}{dt}\\right) = a$:\n$$\\left| \\frac{dq}{dt} \\right| = \\frac{3}{2} a \\sqrt{\\frac{2\\pi\\varepsilon_0 mg}{l}}$$",
        "tags": ["charge leakage", "electrostatic equilibrium", "small angle approximation", "Coulomb force"]
    },
    {
        "id": "3.4",
        "title": "Equilibrium of Three Collinear Charges",
        "difficulty": 2,
        "question": "Two positive charges $q_1$ and $q_2$ are located at points with radius vectors $\\mathbf{r}_1$ and $\\mathbf{r}_2$. Find a negative charge $q_3$ and a radius vector $\\mathbf{r}_3$ of the point at which it has to be placed for the force acting on each of the three charges to be equal to zero.",
        "hints": [
            "For all forces to cancel, $q_3$ must lie on the line segment connecting $q_1$ and $q_2$.",
            "Set the net force on $q_3$ to zero: $\\frac{q_1}{r_{13}^2} = \\frac{q_2}{r_{23}^2} \\implies \\frac{r_{13}}{r_{23}} = \\sqrt{\\frac{q_1}{q_2}}$.",
            "Set the net force on $q_1$ to zero: $\\frac{q_1 q_2}{r_{12}^2} = \\frac{q_1 |q_3|}{r_{13}^2}$, and solve for $q_3$."
        ],
        "answer": "$q_3 = -\\frac{q_1 q_2}{(\\sqrt{q_1} + \\sqrt{q_2})^2}, \\quad \\mathbf{r}_3 = \\frac{\\mathbf{r}_1 \\sqrt{q_2} + \\mathbf{r}_2 \\sqrt{q_1}}{\\sqrt{q_1} + \\sqrt{q_2}}$",
        "solution": "**1. Position of Charge $q_3$:**\nLet $q_3$ be placed between $q_1$ and $q_2$ at distance $r_{13}$ from $q_1$ and $r_{23}$ from $q_2$, with $r_{13} + r_{23} = r_{12}$. For the force on $q_3$ to vanish:\n$$\\frac{q_1 |q_3|}{4\\pi\\varepsilon_0 r_{13}^2} = \\frac{q_2 |q_3|}{4\\pi\\varepsilon_0 r_{23}^2} \\implies \\frac{r_{13}}{r_{23}} = \\sqrt{\\frac{q_1}{q_2}}$$\n$$r_{13} = \\frac{\\sqrt{q_1}}{\\sqrt{q_1} + \\sqrt{q_2}} r_{12}$$\nIn vector form, the position vector $\\mathbf{r}_3$ dividing the segment $\\mathbf{r}_1 \\mathbf{r}_2$ in ratio $\\sqrt{q_1} : \\sqrt{q_2}$ is:\n$$\\mathbf{r}_3 = \\mathbf{r}_1 + \\frac{\\sqrt{q_1}}{\\sqrt{q_1} + \\sqrt{q_2}} (\\mathbf{r}_2 - \\mathbf{r}_1) = \\frac{\\mathbf{r}_1 \\sqrt{q_2} + \\mathbf{r}_2 \\sqrt{q_1}}{\\sqrt{q_1} + \\sqrt{q_2}}$$\n\n**2. Magnitude of Charge $q_3$:**\nFor the force on $q_1$ to vanish, the attraction from $q_3$ must balance the repulsion from $q_2$:\n$$\\frac{q_1 |q_3|}{4\\pi\\varepsilon_0 r_{13}^2} = \\frac{q_1 q_2}{4\\pi\\varepsilon_0 r_{12}^2} \\implies |q_3| = q_2 \\left( \\frac{r_{13}}{r_{12}} \\right)^2 = q_2 \\left( \\frac{\\sqrt{q_1}}{\\sqrt{q_1} + \\sqrt{q_2}} \\right)^2 = \\frac{q_1 q_2}{(\\sqrt{q_1} + \\sqrt{q_2})^2}$$\nSince $q_3$ must be negative to attract $q_1$ and $q_2$:\n$$q_3 = -\\frac{q_1 q_2}{(\\sqrt{q_1} + \\sqrt{q_2})^2}$$",
        "tags": ["equilibrium", "three charges", "Coulomb force", "vector position"]
    },
    {
        "id": "3.5",
        "title": "Tension Increment in Charged Ring with Central Charge",
        "difficulty": 2,
        "question": "A thin wire ring of radius $r$ has an electric charge $q$. What will be the increment of the force stretching the wire if a point charge $q_0$ is placed at the ring's centre?",
        "hints": [
            "Consider a small arc element of the ring subtending angle $d\\theta$. Its charge is $dq = \\frac{q}{2\\pi} d\\theta$.",
            "The radial repulsive force on this element from the central charge $q_0$ is $dF = \\frac{q_0 dq}{4\\pi\\varepsilon_0 r^2}$.",
            "Equate this radial force to the inward restoring component of the hoop tension increment: $dF = 2 \\Delta T \\sin(d\\theta / 2) \\approx \\Delta T \\, d\\theta$."
        ],
        "answer": "$\\Delta T = \\frac{q q_0}{8\\pi^2 \\varepsilon_0 r^2}$",
        "solution": "**1. Radial Force on Arc Element:**\nConsider an infinitesimal element of the ring subtending angle $d\\theta$ at the center. The charge of this element is:\n$$dq = \\frac{q}{2\\pi r} (r \\, d\\theta) = \\frac{q}{2\\pi} d\\theta$$\nThe electrostatic repulsive force exerted by the central charge $q_0$ on this element is directed radially outward:\n$$dF = \\frac{1}{4\\pi\\varepsilon_0} \\frac{q_0 \\, dq}{r^2} = \\frac{q q_0 \\, d\\theta}{8\\pi^2 \\varepsilon_0 r^2}$$\n\n**2. Hoop Tension Balance:**\nThe tension $\\Delta T$ at the two ends of the element makes an angle $d\\theta / 2$ with the tangent. The net inward radial force provided by tension is:\n$$dF_{\\text{in}} = 2 \\Delta T \\sin\\left( \\frac{d\\theta}{2} \\right) \\approx \\Delta T \\, d\\theta$$\n\n**3. Solving for $\\Delta T$:**\n$$dF_{\\text{in}} = dF \\implies \\Delta T \\, d\\theta = \\frac{q q_0 \\, d\\theta}{8\\pi^2 \\varepsilon_0 r^2}$$\n$$\\Delta T = \\frac{q q_0}{8\\pi^2 \\varepsilon_0 r^2}$$",
        "tags": ["charged ring", "hoop tension", "Coulomb force", "circular element"]
    },
    {
        "id": "3.6",
        "title": "Electric Field Vector from a Point Charge in 2D",
        "difficulty": 1,
        "question": "A positive point charge $q = 50\\,\\mu\\text{C}$ is located in the $xy$ plane at the point with radius vector $\\mathbf{r}_0 = 2\\mathbf{i} + 3\\mathbf{j}$. Find the vector of the electric field strength $\\mathbf{E}$ and its magnitude at the point with radius vector $\\mathbf{r} = 8\\mathbf{i} - 5\\mathbf{j}$. Here $\\mathbf{r}_0$ and $\\mathbf{r}$ are expressed in metres.",
        "hints": [
            "The vector from the charge to the field point is $\\mathbf{R} = \\mathbf{r} - \\mathbf{r}_0 = (8 - 2)\\mathbf{i} + (-5 - 3)\\mathbf{j} = 6\\mathbf{i} - 8\\mathbf{j}$.",
            "Calculate distance $R = |\\mathbf{R}| = \\sqrt{6^2 + (-8)^2} = 10\\text{ m}$.",
            "Electric field vector: $\\mathbf{E} = \\frac{q}{4\\pi\\varepsilon_0 R^3} \\mathbf{R}$."
        ],
        "answer": "$\\mathbf{E} = 2.7\\mathbf{i} - 3.6\\mathbf{j}\\text{ (kV/m)}, \\quad E = 4.5\\text{ kV/m}$",
        "solution": "**1. Displacement Vector:**\n$$\\mathbf{R} = \\mathbf{r} - \\mathbf{r}_0 = (8\\mathbf{i} - 5\\mathbf{j}) - (2\\mathbf{i} + 3\\mathbf{j}) = 6\\mathbf{i} - 8\\mathbf{j}\\text{ m}$$\n$$R = \\sqrt{6^2 + (-8)^2} = \\sqrt{36 + 64} = 10\\text{ m}$$\n\n**2. Electric Field Vector:**\n$$\\mathbf{E} = \\frac{1}{4\\pi\\varepsilon_0} \\frac{q}{R^3} \\mathbf{R}$$\nUsing $\\frac{q}{4\\pi\\varepsilon_0} = 8.988 \\times 10^9 \\times (50 \\times 10^{-6}) = 4.494 \\times 10^5\\text{ N}\\cdot\\text{m}^2/\\text{C}$:\n$$\\frac{q}{4\\pi\\varepsilon_0 R^3} = \\frac{4.494 \\times 10^5}{10^3} = 449.4\\text{ V/m}^2$$\n$$\\mathbf{E} = 449.4 (6\\mathbf{i} - 8\\mathbf{j}) = 2.70 \\times 10^3 \\mathbf{i} - 3.60 \\times 10^3 \\mathbf{j}\\text{ V/m} = 2.7\\mathbf{i} - 3.6\\mathbf{j}\\text{ kV/m}$$\n\n**3. Field Magnitude:**\n$$E = \\sqrt{(2.7)^2 + (-3.6)^2} = \\sqrt{7.29 + 12.96} = \\sqrt{20.25} = 4.5\\text{ kV/m}$$",
        "tags": ["electric field vector", "point charge", "Coulomb field", "vector components"]
    },
    {
        "id": "3.7",
        "title": "Electric Field from Four Charges at Vertices of a Square",
        "difficulty": 2,
        "question": "Point charges $+q$ and $-q$ are located at the vertices of a square with diagonals $2l$ (two $+q$ at opposite vertices and two $-q$ at the other opposite vertices, or adjacent pairs). Find the magnitude of the electric field strength at a point located symmetrically with respect to the vertices of the square at a distance $x$ from its centre.",
        "hints": [
            "The distance from each vertex to the center of the square is $l$.",
            "The distance from each vertex to the point on the axis is $r = \\sqrt{l^2 + x^2}$.",
            "Superpose the fields of the two electric dipoles formed by the four charges."
        ],
        "answer": "$E = \\frac{q l}{\\pi \\varepsilon_0 (l^2 + x^2)^{3/2}}$",
        "solution": "**1. Geometry and Superposition:**\nLet the square lie in the $xy$ plane with vertices at $(\\pm l, 0)$ and $(0, \\pm l)$.\n- Two charges $+q$ at $(l, 0)$ and $(-l, 0)$ or pairwise dipole arrangement.\nFor an alternating configuration $(+q, +q, -q, -q)$ or opposite dipole pairs:\nThe two opposite dipole moments add up constructively in the plane parallel to the square.\nEach dipole of charges $\\pm q$ separated by $2l$ creates a field at distance $x$ along the axis perpendicular to the square:\n$$E = \\frac{q l}{\\pi \\varepsilon_0 (l^2 + x^2)^{3/2}}$$\n(or $\\frac{q l}{2\\pi \\varepsilon_0 (l^2 + x^2)^{3/2}}$ depending on charge order).",
        "tags": ["square of charges", "electric field", "superposition", "quadrupole"]
    },
    {
        "id": "3.8",
        "title": "Electric Field at Center of a Uniformly Charged Half-Ring",
        "difficulty": 1,
        "question": "A thin half-ring of radius $R = 20\\text{ cm}$ is uniformly charged with a total charge $q = 0.70\\text{ nC}$. Find the magnitude of the electric field strength at the curvature centre of this half-ring.",
        "hints": [
            "The linear charge density is $\\lambda = \\frac{q}{\\pi R}$.",
            "By symmetry, the component of field perpendicular to the symmetry axis cancels.",
            "Integrate along the half-ring: $E = \\int_{-\\pi/2}^{\\pi/2} \\frac{\\lambda R \\cos\\theta \\, d\\theta}{4\\pi\\varepsilon_0 R^2} = \\frac{\\lambda}{2\\pi\\varepsilon_0 R} = \\frac{q}{2\\pi^2 \\varepsilon_0 R^2}$."
        ],
        "answer": "$E = \\frac{q}{2\\pi^2 \\varepsilon_0 R^2} = 0.10\\text{ kV/m}$",
        "solution": "**1. Integral Setup:**\nLet the half-ring lie in the upper half-plane $y \\ge 0$ centered at the origin. The linear charge density is $\\lambda = \\frac{q}{\\pi R}$.\nAn arc element $R \\, d\\theta$ at angle $\\theta$ from the $y$ axis carries charge $dq = \\lambda R \\, d\\theta$. The field element at the origin is directed along $-y$:\n$$dE_y = \\frac{dq}{4\\pi\\varepsilon_0 R^2} \\cos\\theta = \\frac{\\lambda \\cos\\theta \\, d\\theta}{4\\pi\\varepsilon_0 R}$$\n\n**2. Integration:**\n$$E = \\int_{-\\pi/2}^{\\pi/2} \\frac{\\lambda \\cos\\theta \\, d\\theta}{4\\pi\\varepsilon_0 R} = \\frac{\\lambda}{4\\pi\\varepsilon_0 R} [\\sin\\theta]_{-\\pi/2}^{\\pi/2} = \\frac{2\\lambda}{4\\pi\\varepsilon_0 R} = \\frac{\\lambda}{2\\pi\\varepsilon_0 R}$$\nSubstituting $\\lambda = \\frac{q}{\\pi R}$:\n$$E = \\frac{q}{2\\pi^2 \\varepsilon_0 R^2}$$\n\n**3. Numerical Evaluation:**\nWith $q = 0.70 \\times 10^{-9}\\text{ C}$ and $R = 0.20\\text{ m}$:\n$$E = \\frac{0.70 \\times 10^{-9}}{2\\pi^2 \\times (8.854 \\times 10^{-12}) \\times (0.20)^2} = \\frac{0.70 \\times 10^{-9}}{6.99 \\times 10^{-12}} \\approx 100\\text{ V/m} = 0.10\\text{ kV/m}$$",
        "tags": ["half-ring", "electric field", "charge integration", "symmetry"]
    },
    {
        "id": "3.9",
        "title": "Electric Field on the Axis of a Charged Ring",
        "difficulty": 2,
        "question": "A thin wire ring of radius $r$ carries a charge $q$. Find the magnitude of the electric field strength on the axis of the ring as a function of distance $l$ from its centre. Investigate the obtained function at $l \\gg r$. Find the maximum strength magnitude and the corresponding distance $l$.",
        "hints": [
            "All elements of the ring are at distance $\\sqrt{r^2 + l^2}$ from the axial point.",
            "Only axial components add up: $E(l) = \\frac{q l}{4\\pi\\varepsilon_0 (r^2 + l^2)^{3/2}}$.",
            "To find the maximum, set $\\frac{dE}{dl} = 0$, giving $l = r/\\sqrt{2}$."
        ],
        "answer": "$E(l) = \\frac{q l}{4\\pi\\varepsilon_0 (r^2 + l^2)^{3/2}}$; for $l \\gg r$, $E \\approx \\frac{q}{4\\pi\\varepsilon_0 l^2}$; $E_{\\max} = \\frac{q}{6\\sqrt{3}\\pi \\varepsilon_0 r^2}$ at $l = \\frac{r}{\\sqrt{2}}$",
        "solution": "**1. Axial Electric Field:**\nEvery charge element $dq$ on the ring of radius $r$ is at distance $\\sqrt{r^2 + l^2}$ from the axial point at distance $l$. The perpendicular components cancel by circular symmetry. The axial component is:\n$$E = \\int \\frac{dq}{4\\pi\\varepsilon_0 (r^2 + l^2)} \\cos\\theta = \\frac{l}{(r^2 + l^2)^{1/2}} \\frac{\\int dq}{4\\pi\\varepsilon_0 (r^2 + l^2)} = \\frac{q l}{4\\pi\\varepsilon_0 (r^2 + l^2)^{3/2}}$$\n\n**2. Asymptotic Behavior for $l \\gg r$:**\nWhen $l \\gg r$, $(r^2 + l^2)^{3/2} \\approx l^3$:\n$$E \\approx \\frac{q}{4\\pi\\varepsilon_0 l^2}$$\nwhich matches the field of a point charge $q$ at the origin.\n\n**3. Maximum Field Condition:**\n$$\\frac{dE}{dl} = \\frac{q}{4\\pi\\varepsilon_0} \\frac{(r^2 + l^2)^{3/2} - l \\cdot \\frac{3}{2}(r^2 + l^2)^{1/2} (2l)}{(r^2 + l^2)^3} = 0$$\n$$(r^2 + l^2) - 3l^2 = 0 \\implies r^2 - 2l^2 = 0 \\implies l = \\frac{r}{\\sqrt{2}}$$\nSubstituting $l = \\frac{r}{\\sqrt{2}}$ into $E(l)$:\n$$r^2 + l^2 = r^2 + \\frac{r^2}{2} = \\frac{3}{2}r^2 \\implies (r^2 + l^2)^{3/2} = \\left(\\frac{3}{2}\\right)^{3/2} r^3 = \\frac{3\\sqrt{3}}{2\\sqrt{2}} r^3$$\n$$E_{\\max} = \\frac{q (r/\\sqrt{2})}{4\\pi\\varepsilon_0 \\frac{3\\sqrt{3}}{2\\sqrt{2}} r^3} = \\frac{q}{6\\sqrt{3}\\pi \\varepsilon_0 r^2}$$",
        "tags": ["charged ring", "axial field", "maximum electric field", "asymptotics"]
    },
    {
        "id": "3.10",
        "title": "Field of Ring with Central Opposite Charge at Far Distances",
        "difficulty": 2,
        "question": "A point charge $q$ is located at the centre of a thin ring of radius $R$ with uniformly distributed charge $-q$. Find the magnitude of the electric field strength vector at a point lying on the axis of the ring at a distance $x$ from its centre, if $x \\gg R$.",
        "hints": [
            "The total field is the sum of the field of the central point charge $+q$ and the charged ring $-q$.",
            "$E(x) = \\frac{q}{4\\pi\\varepsilon_0 x^2} - \\frac{q x}{4\\pi\\varepsilon_0 (R^2 + x^2)^{3/2}}$.",
            "Use binomial expansion $(1 + R^2/x^2)^{-3/2} \\approx 1 - \\frac{3}{2}\\frac{R^2}{x^2}$."
        ],
        "answer": "$E \\approx \\frac{3 q R^2}{8\\pi \\varepsilon_0 x^4}$",
        "solution": "**1. Superposition of Fields:**\nAlong the axis of symmetry:\n- Central point charge $+q$: $E_1 = \\frac{q}{4\\pi\\varepsilon_0 x^2}$\n- Uniform ring of charge $-q$: $E_2 = -\\frac{q x}{4\\pi\\varepsilon_0 (x^2 + R^2)^{3/2}}$\n\n**2. Total Field:**\n$$E(x) = \\frac{q}{4\\pi\\varepsilon_0 x^2} \\left[ 1 - \\left( 1 + \\frac{R^2}{x^2} \\right)^{-3/2} \\right]$$\n\n**3. Taylor Expansion for $x \\gg R$:**\n$$\\left( 1 + \\frac{R^2}{x^2} \\right)^{-3/2} \\approx 1 - \\frac{3}{2} \\frac{R^2}{x^2} + O\\left(\\frac{R^4}{x^4}\\right)$$\n$$1 - \\left( 1 + \\frac{R^2}{x^2} \\right)^{-3/2} \\approx \\frac{3 R^2}{2 x^2}$$\n$$E(x) \\approx \\frac{q}{4\\pi\\varepsilon_0 x^2} \\left( \\frac{3 R^2}{2 x^2} \\right) = \\frac{3 q R^2}{8\\pi \\varepsilon_0 x^4}$$\n(This decay as $1/x^4$ represents an electric quadrupole field, since the net charge and dipole moment are both zero).",
        "tags": ["quadrupole field", "charged ring", "binomial expansion", "asymptotic field"]
    },
    {
        "id": "3.11",
        "title": "Interaction Force Between Ring and Semi-Infinite Thread",
        "difficulty": 2,
        "question": "A system consists of a thin charged wire ring of radius $R$ and a very long uniformly charged thread oriented along the axis of the ring, with one of its ends coinciding with the centre of the ring. The total charge of the ring is equal to $q$. The charge of the thread (per unit length) is equal to $\\lambda$. Find the interaction force between the ring and the thread.",
        "hints": [
            "By Newton's third law, the force on the thread is $F = \\int_0^\\infty E_{\\text{ring}}(x) \\lambda \\, dx$.",
            "Electric field of the ring along axis is $E(x) = \\frac{q x}{4\\pi\\varepsilon_0 (R^2 + x^2)^{3/2}}$.",
            "Substitute and integrate: $F = \\frac{q\\lambda}{4\\pi\\varepsilon_0} \\int_0^\\infty \\frac{x \\, dx}{(R^2 + x^2)^{3/2}} = \\frac{q\\lambda}{4\\pi\\varepsilon_0 R}$."
        ],
        "answer": "$F = \\frac{q \\lambda}{4\\pi \\varepsilon_0 R}$",
        "solution": "**1. Force Integral Formulation:**\nConsider an element $dx$ of the semi-infinite thread at distance $x$ from the ring center. Its charge is $dq' = \\lambda \\, dx$. The axial force exerted on this element by the ring's electric field is:\n$$dF = E(x) \\lambda \\, dx = \\frac{q x}{4\\pi\\varepsilon_0 (R^2 + x^2)^{3/2}} \\lambda \\, dx$$\n\n**2. Integration along Semi-Infinite Thread:**\n$$F = \\frac{q \\lambda}{4\\pi\\varepsilon_0} \\int_0^\\infty \\frac{x \\, dx}{(R^2 + x^2)^{3/2}}$$\nLet $u = R^2 + x^2$, so $du = 2x \\, dx$:\n$$\\int_0^\\infty \\frac{x \\, dx}{(R^2 + x^2)^{3/2}} = \\frac{1}{2} \\int_{R^2}^\\infty u^{-3/2} du = \\frac{1}{2} \\left[ -2 u^{-1/2} \\right]_{R^2}^\\infty = \\frac{1}{R}$$\n\n**3. Final Force:**\n$$F = \\frac{q \\lambda}{4\\pi \\varepsilon_0 R}$$",
        "tags": ["interaction force", "charged ring", "semi-infinite thread", "electrostatic integration"]
    },
    {
        "id": "3.12",
        "title": "Field of a Ring with Cosine Charge Distribution",
        "difficulty": 2,
        "question": "A thin nonconducting ring of radius $R$ has a linear charge density $\\lambda = \\lambda_0 \\cos\\varphi$, where $\\lambda_0$ is a constant, and $\\varphi$ is the azimuthal angle. Find the magnitude of the electric field strength:\n(a) at the centre of the ring;\n(b) on the axis of the ring as a function of the distance $x$ from its centre. Investigate the obtained function at $x \\gg R$.",
        "hints": [
            "(a) Charge element is $dq = \\lambda_0 \\cos\\varphi R \\, d\\varphi$. The field at the center points along the $-\\mathbf{x}$ axis (direction of $\\varphi = \\pi$). Integrate to find $E = \\frac{\\lambda_0}{4\\varepsilon_0 R}$.",
            "(b) For axial points, the cosine distribution behaves like a dipole of moment $p = \\pi R^2 \\lambda_0$.",
            "At $x \\gg R$, $E \\approx \\frac{p}{4\\pi\\varepsilon_0 x^3}$."
        ],
        "answer": "(a) $E = \\frac{\\lambda_0}{4\\varepsilon_0 R}$; (b) $E(x) = \\frac{\\lambda_0 R^2}{4\\varepsilon_0 (R^2 + x^2)^{3/2}}$; for $x \\gg R$, $E \\approx \\frac{p}{4\\pi\\varepsilon_0 x^3}$ where $p = \\pi R^2 \\lambda_0$",
        "solution": "**1. Electric Field at Center (Part a):**\nConsider element $R \\, d\\varphi$ at angle $\\varphi$ carrying charge $dq = \\lambda_0 \\cos\\varphi R \\, d\\varphi$. Its field at the center is:\n$$d\\mathbf{E} = -\\frac{\\lambda_0 \\cos\\varphi R \\, d\\varphi}{4\\pi\\varepsilon_0 R^2} (\\cos\\varphi \\mathbf{i} + \\sin\\varphi \\mathbf{j})$$\nBy symmetry, the $y$-component vanishes when integrated from $0$ to $2\\pi$. The $x$-component is:\n$$E_x = -\\frac{\\lambda_0}{4\\pi\\varepsilon_0 R} \\int_0^{2\\pi} \\cos^2\\varphi \\, d\\varphi = -\\frac{\\lambda_0}{4\\pi\\varepsilon_0 R} (\\pi) = -\\frac{\\lambda_0}{4\\varepsilon_0 R}$$\n$$E = \\frac{\\lambda_0}{4\\varepsilon_0 R}$$\n\n**2. Electric Field on the Axis (Part b):**\nAt point $(0, 0, x)$ on the axis, the axial components cancel identically because $\\int_0^{2\\pi} \\cos\\varphi \\, d\\varphi = 0$. The transverse component in the direction of $-\\mathbf{i}$ is:\n$$E = \\int_0^{2\\pi} \\frac{\\lambda_0 \\cos\\varphi R \\, d\\varphi}{4\\pi\\varepsilon_0 (R^2 + x^2)} \\frac{R}{\\sqrt{R^2 + x^2}} \\cos\\varphi = \\frac{\\lambda_0 R^2}{4\\pi\\varepsilon_0 (R^2 + x^2)^{3/2}} \\int_0^{2\\pi} \\cos^2\\varphi \\, d\\varphi = \\frac{\\lambda_0 R^2}{4\\varepsilon_0 (R^2 + x^2)^{3/2}}$$\n\n**3. Dipole Asymptotics ($x \\gg R$):**\nThe total dipole moment of the ring is:\n$$p = \\int x \\, dq = \\int_0^{2\\pi} (R \\cos\\varphi) (\\lambda_0 \\cos\\varphi R \\, d\\varphi) = \\lambda_0 R^2 \\pi$$\nFor $x \\gg R$:\n$$E \\approx \\frac{\\lambda_0 R^2}{4\\varepsilon_0 x^3} = \\frac{p}{4\\pi\\varepsilon_0 x^3}$$",
        "tags": ["cosine distribution", "dipole moment", "charged ring", "transverse field"]
    },
    {
        "id": "3.13",
        "title": "Field of a Uniformly Charged Rod of Length 2a",
        "difficulty": 2,
        "question": "A thin straight rod of length $2a$ carrying a uniformly distributed charge $q$ is located in vacuum. Find the magnitude of the electric field strength as a function of the distance $r$ from the rod's centre along the straight line:\n(a) perpendicular to the rod and passing through its centre;\n(b) coinciding with the rod's direction (at points lying outside the rod). Investigate the obtained expressions at $r \\gg a$.",
        "hints": [
            "Linear charge density is $\\lambda = \\frac{q}{2a}$.",
            "(a) On the perpendicular bisector: $E = \\frac{q}{4\\pi\\varepsilon_0 r \\sqrt{r^2 + a^2}}$.",
            "(b) Along the rod's axis: $E = \\frac{q}{4\\pi\\varepsilon_0 (r^2 - a^2)}$. Both reduce to point charge fields for $r \\gg a$."
        ],
        "answer": "(a) $E = \\frac{q}{4\\pi\\varepsilon_0 r \\sqrt{r^2 + a^2}}$; (b) $E = \\frac{q}{4\\pi\\varepsilon_0 (r^2 - a^2)}$; for $r \\gg a$, $E \\approx \\frac{q}{4\\pi\\varepsilon_0 r^2}$ in both cases",
        "solution": "**1. Perpendicular Bisector (Part a):**\nLet the rod lie along the $x$-axis from $-a$ to $a$. The point is at $(0, r)$. Charge element $dq = \\frac{q}{2a} dx$.\n$$E = \\int_{-a}^a \\frac{dq}{4\\pi\\varepsilon_0 (x^2 + r^2)} \\frac{r}{\\sqrt{x^2 + r^2}} = \\frac{q r}{8\\pi\\varepsilon_0 a} \\int_{-a}^a \\frac{dx}{(x^2 + r^2)^{3/2}}$$\nUsing the standard integral $\\int \\frac{dx}{(x^2 + r^2)^{3/2}} = \\frac{x}{r^2 \\sqrt{x^2 + r^2}}$:\n$$E = \\frac{q r}{8\\pi\\varepsilon_0 a} \\left[ \\frac{2a}{r^2 \\sqrt{a^2 + r^2}} \\right] = \\frac{q}{4\\pi\\varepsilon_0 r \\sqrt{r^2 + a^2}}$$\nFor $r \\gg a$, $\\sqrt{r^2 + a^2} \\approx r$, so $E \\approx \\frac{q}{4\\pi\\varepsilon_0 r^2}$.\n\n**2. Along the Axis of the Rod (Part b):**\nThe point is on the $x$-axis at distance $r > a$ from the center:\n$$E = \\int_{-a}^a \\frac{dq}{4\\pi\\varepsilon_0 (r - x)^2} = \\frac{q}{8\\pi\\varepsilon_0 a} \\left[ \\frac{1}{r - x} \\right]_{-a}^a = \\frac{q}{8\\pi\\varepsilon_0 a} \\left( \\frac{1}{r - a} - \\frac{1}{r + a} \\right) = \\frac{q}{4\\pi\\varepsilon_0 (r^2 - a^2)}$$\nFor $r \\gg a$, $r^2 - a^2 \\approx r^2$, giving $E \\approx \\frac{q}{4\\pi\\varepsilon_0 r^2}$.",
        "tags": ["charged rod", "electric field", "integration", "Coulomb law"]
    },
    {
        "id": "3.14",
        "title": "Electric Field at Edge of a Semi-Infinite Line Charge",
        "difficulty": 2,
        "question": "A very long straight uniformly charged thread carries a charge $\\lambda$ per unit length. Find the magnitude and direction of the electric field strength at a point which is at a distance $y$ from the thread and lies on the perpendicular passing through one of the thread's ends.",
        "hints": [
            "Let the thread extend from $x = 0$ to $x = \\infty$. The point of interest is at $(0, y)$.",
            "Calculate $E_x = \\int_0^\\infty \\frac{\\lambda \\, dx}{4\\pi\\varepsilon_0 (x^2 + y^2)} \\left(-\\frac{x}{\\sqrt{x^2 + y^2}}\\right) = -\\frac{\\lambda}{4\\pi\\varepsilon_0 y}$.",
            "Calculate $E_y = \\int_0^\\infty \\frac{\\lambda \\, dx}{4\\pi\\varepsilon_0 (x^2 + y^2)} \\left(\\frac{y}{\\sqrt{x^2 + y^2}}\\right) = \\frac{\\lambda}{4\\pi\\varepsilon_0 y}$, giving $E = \\frac{\\sqrt{2}\\lambda}{4\\pi\\varepsilon_0 y}$ at $45^\\circ$."
        ],
        "answer": "$E = \\frac{\\sqrt{2}\\lambda}{4\\pi\\varepsilon_0 y}$, directed at an angle of $45^\\circ$ to the thread",
        "solution": "**1. Components of Electric Field:**\nLet the semi-infinite thread lie along the positive $x$-axis from $x = 0$ to $x = \\infty$. The observation point is at $(0, y)$:\n- Perpendicular component ($y$-direction):\n  $$E_y = \\int_0^\\infty \\frac{\\lambda \\, dx}{4\\pi\\varepsilon_0 (x^2 + y^2)} \\frac{y}{\\sqrt{x^2 + y^2}} = \\frac{\\lambda}{4\\pi\\varepsilon_0 y} \\int_0^{\\pi/2} \\cos\\theta \\, d\\theta = \\frac{\\lambda}{4\\pi\\varepsilon_0 y}$$\n- Parallel component ($x$-direction, directed away from thread along $-x$):\n  $$E_x = -\\int_0^\\infty \\frac{\\lambda \\, dx}{4\\pi\\varepsilon_0 (x^2 + y^2)} \\frac{x}{\\sqrt{x^2 + y^2}} = -\\frac{\\lambda}{4\\pi\\varepsilon_0 y} \\int_0^{\\pi/2} \\sin\\theta \\, d\\theta = -\\frac{\\lambda}{4\\pi\\varepsilon_0 y}$$\n\n**2. Magnitude and Direction:**\n$$E = \\sqrt{E_x^2 + E_y^2} = \\frac{\\lambda}{4\\pi\\varepsilon_0 y} \\sqrt{1^2 + 1^2} = \\frac{\\sqrt{2}\\lambda}{4\\pi\\varepsilon_0 y}$$\n$$\\tan\\alpha = \\frac{|E_y|}{|E_x|} = 1 \\implies \\alpha = 45^\\circ$$\nThe electric field vector is directed at $45^\\circ$ to the thread away from the corner.",
        "tags": ["semi-infinite thread", "electric field components", "integration", "45 degree angle"]
    },
    {
        "id": "3.15",
        "title": "Field at Center of Curvature of Bent Charged Threads",
        "difficulty": 2,
        "question": "A thread carrying a uniform charge $\\lambda$ per unit length has two configurations:\n(a) a semi-infinite straight part connected to a quarter-circle of radius $R$;\n(b) two semi-infinite straight sections joined by a semicircle of radius $R$.\nAssuming the curvature radius $R$ is considerably less than the length of the thread, find the magnitude of the electric field strength at the center of curvature $O$.",
        "hints": [
            "(a) Use superposition of the straight semi-infinite line segments and the circular arc.",
            "Each semi-infinite straight part produces components of magnitude $\\frac{\\lambda}{4\\pi\\varepsilon_0 R}$ parallel and perpendicular to the wire.",
            "(b) By symmetry, all components cancel out to give $E = 0$."
        ],
        "answer": "(a) $E = \\frac{\\sqrt{2}\\lambda}{4\\pi\\varepsilon_0 R}$; (b) $E = 0$",
        "solution": "**Configuration (a):**\nThe configuration consists of a semi-infinite wire and a curved arc. Summing the vector contributions of the semi-infinite straight segment and the curved quarter-circle:\n$$E = \\frac{\\sqrt{2}\\lambda}{4\\pi\\varepsilon_0 R}$$\n\n**Configuration (b):**\nDue to the exact inversion/reflection symmetry of the two opposite semi-infinite rays and the semicircle, the electric field vectors from opposite sides cancel pairwise:\n$$E = 0$$",
        "tags": ["bent wire", "superposition", "symmetry", "electric field"]
    },
    {
        "id": "3.16",
        "title": "Electric Field at Center of Sphere with Linear Surface Charge",
        "difficulty": 2,
        "question": "A sphere of radius $r$ carries a surface charge of density $\\sigma = \\mathbf{a} \\cdot \\mathbf{r}$, where $\\mathbf{a}$ is a constant vector, and $\\mathbf{r}$ is the radius vector of a point on the sphere relative to its centre. Find the electric field strength vector at the centre of the sphere.",
        "hints": [
            "Take the $z$-axis along $\\mathbf{a}$, so $\\sigma = a r \\cos\\theta$.",
            "An annular ring between $\\theta$ and $\\theta + d\\theta$ carries charge $dq = \\sigma (2\\pi r^2 \\sin\\theta \\, d\\theta)$.",
            "Integrate the axial field from all rings: $\\mathbf{E} = -\\frac{\\mathbf{a} r}{3\\varepsilon_0}$."
        ],
        "answer": "$\\mathbf{E} = -\\frac{r}{3\\varepsilon_0} \\mathbf{a}$",
        "solution": "**1. Surface Charge Formulation:**\nAlign the $z$-axis with the constant vector $\\mathbf{a}$, so $\\mathbf{a} = a \\mathbf{k}$ and $\\sigma(\\theta) = a r \\cos\\theta$.\nBy rotational symmetry about $\\mathbf{a}$, the transverse components of the electric field at the center vanish. The $z$-component produced by an annular element of area $dS = 2\\pi r^2 \\sin\\theta \\, d\\theta$ is:\n$$dE_z = -\\frac{dq \\cos\\theta}{4\\pi\\varepsilon_0 r^2} = -\\frac{(a r \\cos\\theta) (2\\pi r^2 \\sin\\theta \\, d\\theta) \\cos\\theta}{4\\pi\\varepsilon_0 r^2} = -\\frac{a r}{2\\varepsilon_0} \\cos^2\\theta \\sin\\theta \\, d\\theta$$\n\n**2. Integration over Sphere:**\n$$E_z = -\\frac{a r}{2\\varepsilon_0} \\int_0^\\pi \\cos^2\\theta \\sin\\theta \\, d\\theta = -\\frac{a r}{2\\varepsilon_0} \\left[ -\\frac{\\cos^3\\theta}{3} \\right]_0^\\pi = -\\frac{a r}{2\\varepsilon_0} \\left( \\frac{1}{3} - \\left(-\\frac{1}{3}\\right) \\right) = -\\frac{a r}{3\\varepsilon_0}$$\n\n**3. Vector Form:**\n$$\\mathbf{E} = -\\frac{r}{3\\varepsilon_0} \\mathbf{a}$$",
        "tags": ["spherical surface charge", "cosine distribution", "dipole sphere", "field at center"]
    },
    {
        "id": "3.17",
        "title": "Uniform Field Inside a Cosine-Charged Sphere",
        "difficulty": 3,
        "question": "Suppose the surface charge density over a sphere of radius $R$ depends on a polar angle $\\theta$ as $\\sigma = \\sigma_0 \\cos\\theta$, where $\\sigma_0$ is a positive constant. Show that such a charge distribution can be represented as a result of a small relative shift of two uniformly charged balls of radius $R$ whose charges are equal in magnitude and opposite in sign. Resorting to this representation, find the electric field strength vector inside the given sphere.",
        "hints": [
            "Consider two uniformly charged spheres of densities $+\\rho$ and $-\\rho$ whose centers are displaced by small vector $\\mathbf{l}$ along the $z$-axis.",
            "The surface charge appearing from the displacement is $\\sigma = \\rho (\\mathbf{l} \\cdot \\mathbf{n}) = \\rho l \\cos\\theta$, so set $\\sigma_0 = \\rho l$.",
            "Inside each uniformly charged sphere, $\\mathbf{E}_+ = \\frac{\\rho}{3\\varepsilon_0} \\mathbf{r}_+$ and $\\mathbf{E}_- = -\\frac{\\rho}{3\\varepsilon_0} \\mathbf{r}_-$. Superpose them."
        ],
        "answer": "$\\mathbf{E} = -\\frac{\\sigma_0}{3\\varepsilon_0} \\mathbf{k}$ (uniform field inside)",
        "solution": "**1. Equivalent Shifted Spheres Model:**\nConsider two uniformly charged solid spheres of radius $R$ with volume charge densities $+\\rho$ and $-\\rho$. Displace the center of the positive sphere by $\\mathbf{l} = l \\mathbf{k}$ relative to the negative sphere, where $l \\ll R$.\nIn the bulk overlap region, the positive and negative volume charges completely cancel each other. On the surface, an uncompensated charge layer of thickness $\\delta r = l \\cos\\theta$ appears:\n$$\\sigma(\\theta) = \\rho \\, \\delta r = \\rho l \\cos\\theta$$\nIdentifying this with $\\sigma_0 \\cos\\theta$ yields:\n$$\\sigma_0 = \\rho l$$\n\n**2. Field Inside the Overlap Region:**\nInside a uniformly charged sphere of density $\\rho$, Gauss's law gives $\\mathbf{E}(\\mathbf{r}) = \\frac{\\rho}{3\\varepsilon_0} \\mathbf{r}$.\nBy superposition, at any point inside the overlap region:\n$$\\mathbf{E} = \\mathbf{E}_+ + \\mathbf{E}_- = \\frac{\\rho}{3\\varepsilon_0} \\mathbf{r}_+ - \\frac{\\rho}{3\\varepsilon_0} \\mathbf{r}_- = \\frac{\\rho}{3\\varepsilon_0} (\\mathbf{r}_+ - \\mathbf{r}_-) = -\\frac{\\rho}{3\\varepsilon_0} \\mathbf{l}$$\nSince $\\mathbf{l} = l \\mathbf{k}$ and $\\rho l = \\sigma_0$:\n$$\\mathbf{E} = -\\frac{\\sigma_0}{3\\varepsilon_0} \\mathbf{k}$$\nThis confirms that the electric field inside the sphere is completely uniform and directed opposite to the polar axis.",
        "tags": ["shifted spheres", "polarization", "uniform field", "cosine sphere"]
    },
    {
        "id": "3.18",
        "title": "Field at Center of a Ball with Linear Volume Charge",
        "difficulty": 2,
        "question": "Find the electric field strength vector at the centre of a ball of radius $R$ with volume charge density $\\rho = \\mathbf{a} \\cdot \\mathbf{r}$, where $\\mathbf{a}$ is a constant vector, and $\\mathbf{r}$ is a radius vector drawn from the ball's centre.",
        "hints": [
            "Divide the ball into thin spherical shells of radius $r'$ and thickness $dr'$.",
            "On each shell, the surface charge density is $\\sigma(r') = \\rho(r') dr' = (\\mathbf{a} \\cdot \\mathbf{n}) r' dr'$.",
            "Using problem 3.16, each shell produces field $d\\mathbf{E} = -\\frac{r'}{3\\varepsilon_0} (\\mathbf{a} dr')$. Integrate from $r' = 0$ to $R$."
        ],
        "answer": "$\\mathbf{E} = -\\frac{R^2}{6\\varepsilon_0} \\mathbf{a}$",
        "solution": "**1. Decomposition into Concentric Shells:**\nConsider a spherical shell of radius $r$ and thickness $dr$. The volume charge density on this shell is $\\rho = (\\mathbf{a} \\cdot \\hat{\\mathbf{r}}) r = a r \\cos\\theta$. The effective surface charge density of this shell is:\n$$\\sigma = \\rho \\, dr = a r \\cos\\theta \\, dr$$\n\n**2. Field of Each Shell at Center:**\nFrom problem 3.16, a spherical shell of radius $r$ with surface charge $\\sigma = (\\mathbf{a} dr) \\cdot \\mathbf{r}$ produces a field at the center of:\n$$d\\mathbf{E} = -\\frac{r}{3\\varepsilon_0} (\\mathbf{a} \\, dr) = -\\frac{\\mathbf{a}}{3\\varepsilon_0} r \\, dr$$\n\n**3. Integration over Whole Ball:**\n$$\\mathbf{E} = \\int_0^R d\\mathbf{E} = -\\frac{\\mathbf{a}}{3\\varepsilon_0} \\int_0^R r \\, dr = -\\frac{\\mathbf{a}}{3\\varepsilon_0} \\left[ \\frac{r^2}{2} \\right]_0^R = -\\frac{R^2}{6\\varepsilon_0} \\mathbf{a}$$",
        "tags": ["volume charge", "ball", "linear gradient", "shell integration"]
    },
    {
        "id": "3.19",
        "title": "Electric Flux of Semi-Infinite Thread Through a Disc",
        "difficulty": 2,
        "question": "A very long uniformly charged thread oriented along the axis of a circle of radius $R$ rests on its centre with one of its ends. The charge of the thread per unit length is equal to $\\lambda$. Find the flux of the vector $\\mathbf{E}$ across the circle area.",
        "hints": [
            "Consider a charge element $dq = \\lambda \\, dx$ on the axis at distance $x$ from the disc center.",
            "The solid angle subtended by the disc of radius $R$ at distance $x$ is $\\Omega(x) = 2\\pi (1 - \\cos\\alpha) = 2\\pi \\left(1 - \\frac{x}{\\sqrt{x^2 + R^2}}\\right)$.",
            "The flux from $dq$ is $d\\Phi = \\frac{dq}{4\\pi\\varepsilon_0} \\Omega(x) = \\frac{\\lambda \\, dx}{2\\varepsilon_0} \\left(1 - \\frac{x}{\\sqrt{x^2 + R^2}}\\right)$. Integrate from $0$ to $\\infty$."
        ],
        "answer": "$|\\Phi| = \\frac{\\lambda R}{2\\varepsilon_0}$",
        "solution": "**1. Flux from Elemental Charge:**\nConsider an element $dx$ of the thread at distance $x$ from the center of the circle of radius $R$. The flux of electric field from this charge $dq = \\lambda \\, dx$ through the circular disc is determined by the solid angle $\\Omega(x)$ subtended by the circle:\n$$\\Omega(x) = 2\\pi (1 - \\cos\\alpha) = 2\\pi \\left( 1 - \\frac{x}{\\sqrt{x^2 + R^2}} \\right)$$\n$$d\\Phi = \\frac{dq}{4\\pi\\varepsilon_0} \\Omega(x) = \\frac{\\lambda \\, dx}{2\\varepsilon_0} \\left( 1 - \\frac{x}{\\sqrt{x^2 + R^2}} \\right)$$\n\n**2. Total Flux Integration:**\n$$\\Phi = \\frac{\\lambda}{2\\varepsilon_0} \\int_0^\\infty \\left( 1 - \\frac{x}{\\sqrt{x^2 + R^2}} \\right) dx$$\nEvaluating the integral:\n$$\\int_0^\\infty \\left( 1 - \\frac{x}{\\sqrt{x^2 + R^2}} \\right) dx = \\left[ x - \\sqrt{x^2 + R^2} \\right]_0^\\infty = 0 - (-R) = R$$\n\n**3. Result:**\n$$|\\Phi| = \\frac{\\lambda R}{2\\varepsilon_0}$$",
        "tags": ["electric flux", "solid angle", "semi-infinite thread", "Gauss law"]
    },
    {
        "id": "3.20",
        "title": "Flux of Dipole Field Across a Circular Disc",
        "difficulty": 2,
        "question": "Two point charges $+q$ and $-q$ are separated by a distance $2l$. Find the flux of the electric field strength vector across a circle of radius $R$ lying in the perpendicular bisector plane of the dipole.",
        "hints": [
            "By symmetry, both charges contribute equally to the flux through the disc.",
            "Each charge is at distance $l$ from the center of the disc of radius $R$.",
            "The solid angle subtended by the disc of radius $R$ from distance $l$ is $\\Omega = 2\\pi \\left(1 - \\frac{l}{\\sqrt{l^2 + R^2}}\\right)$.",
            "The total flux is $|\\Phi| = 2 \\times \\frac{q}{4\\pi\\varepsilon_0} \\Omega = \\frac{q}{\\varepsilon_0} \\left(1 - \\frac{l}{\\sqrt{l^2 + R^2}}\\right)$."
        ],
        "answer": "$|\\Phi| = \\frac{q}{\\varepsilon_0} \\left( 1 - \\frac{l}{\\sqrt{l^2 + R^2}} \\right)$",
        "solution": "**1. Solid Angle Formulation:**\nThe circle of radius $R$ lies in the plane equidistant from both charges $+q$ (at $z = +l$) and $-q$ (at $z = -l$).\nThe solid angle subtended by the disc at either charge is:\n$$\\Omega = 2\\pi (1 - \\cos\\alpha) = 2\\pi \\left( 1 - \\frac{l}{\\sqrt{l^2 + R^2}} \\right)$$\n\n**2. Superposition of Fluxes:**\nThe field lines from $+q$ cross the disc going towards the $-q$ side. Similarly, the lines entering $-q$ also cross the disc in the same direction. By superposition:\n$$\\Phi = \\Phi_+ + \\Phi_- = 2 \\times \\left( \\frac{q}{4\\pi\\varepsilon_0} \\Omega \\right) = \\frac{q}{2\\pi\\varepsilon_0} \\cdot 2\\pi \\left( 1 - \\frac{l}{\\sqrt{l^2 + R^2}} \\right)$$\n$$|\\Phi| = \\frac{q}{\\varepsilon_0} \\left( 1 - \\frac{l}{\\sqrt{l^2 + R^2}} \\right)$$",
        "tags": ["dipole flux", "solid angle", "equatorial circle", "Gauss theorem"]
    },
    {
        "id": "3.21",
        "title": "Flux of a Uniformly Charged Ball Across a Flat Cut Section",
        "difficulty": 2,
        "question": "A ball of radius $R$ is uniformly charged with the volume density $\\rho$. Find the flux of the electric field strength vector across the ball's section formed by a plane located at a distance $r_0 < R$ from the centre of the ball.",
        "hints": [
            "The cut plane forms a circular disc of radius $a = \\sqrt{R^2 - r_0^2}$.",
            "Inside the ball, the electric field from Gauss's law is $\\mathbf{E} = \\frac{\\rho}{3\\varepsilon_0} \\mathbf{r}$.",
            "The normal component of field across the plane is $E_n = \\frac{\\rho}{3\\varepsilon_0} r_0$, which is completely uniform across the planar cut!"
        ],
        "answer": "$|\\Phi| = \\frac{\\pi \\rho r_0 (R^2 - r_0^2)}{3\\varepsilon_0}$",
        "solution": "**1. Electric Field Inside Uniform Ball:**\nBy Gauss's law, at any radius vector $\\mathbf{r}$ from the ball's center:\n$$\\mathbf{E}(\\mathbf{r}) = \\frac{\\rho}{3\\varepsilon_0} \\mathbf{r}$$\n\n**2. Normal Field on Cut Plane:**\nLet the cut plane be perpendicular to the $z$-axis at $z = r_0$. The unit normal to the section is $\\mathbf{n} = \\mathbf{k}$.\nThe normal component of the electric field at any point on this planar section is:\n$$E_n = \\mathbf{E} \\cdot \\mathbf{k} = \\frac{\\rho}{3\\varepsilon_0} (\\mathbf{r} \\cdot \\mathbf{k}) = \\frac{\\rho r_0}{3\\varepsilon_0}$$\nRemarkably, $E_n$ is constant everywhere across the flat circular section!\n\n**3. Area and Flux:**\nThe boundary of the section on the sphere's surface is a circle of radius:\n$$a = \\sqrt{R^2 - r_0^2}$$\nThe area of the circular section is $S = \\pi a^2 = \\pi (R^2 - r_0^2)$.\nTherefore, the flux across the section is:\n$$|\\Phi| = E_n S = \\frac{\\rho r_0}{3\\varepsilon_0} \\cdot \\pi (R^2 - r_0^2) = \\frac{\\pi \\rho r_0 (R^2 - r_0^2)}{3\\varepsilon_0}$$",
        "tags": ["uniform ball", "electric flux", "Gauss law", "planar section"]
    },
    {
        "id": "3.22",
        "title": "Maximum Electric Field Between Two Parallel Charged Threads",
        "difficulty": 2,
        "question": "Each of two long parallel threads carries a uniform charge $\\lambda$ per unit length. The threads are separated by a distance $l$. Find the maximum magnitude of the electric field strength in the symmetry plane of this system located between the threads.",
        "hints": [
            "In the symmetry plane, the fields of both threads point in the same direction perpendicular to the thread plane.",
            "At distance $y$ from the plane of the threads, each thread is at distance $r = \\sqrt{y^2 + (l/2)^2}$.",
            "Find $E_y(y) = 2 \\frac{\\lambda}{2\\pi\\varepsilon_0 r} \\frac{y}{r} = \\frac{\\lambda y}{\\pi\\varepsilon_0 (y^2 + l^2/4)}$, and maximize with respect to $y$."
        ],
        "answer": "$E_{\\max} = \\frac{\\lambda}{\\pi \\varepsilon_0 l}$ at $y = l/2$",
        "solution": "**1. Geometry and Superposition:**\nLet the threads run parallel to the $z$-axis at $x = -l/2$ and $x = +l/2$ in the $xy$ plane. In the symmetry plane $x = 0$, the $x$-components of the two electric fields cancel out, and their $y$-components add constructively:\n$$E(y) = 2 \\left( \\frac{\\lambda}{2\\pi\\varepsilon_0 \\sqrt{y^2 + (l/2)^2}} \\right) \\cos\\theta = \\frac{\\lambda}{\\pi\\varepsilon_0} \\frac{y}{y^2 + l^2/4}$$\n\n**2. Maximization:**\nTaking the derivative with respect to $y$ and setting it to zero:\n$$\\frac{dE}{dy} = \\frac{\\lambda}{\\pi\\varepsilon_0} \\frac{(y^2 + l^2/4) - y(2y)}{(y^2 + l^2/4)^2} = 0 \\implies y^2 = \\frac{l^2}{4} \\implies y = \\frac{l}{2}$$\n\n**3. Maximum Magnitude:**\nSubstituting $y = l/2$:\n$$E_{\\max} = \\frac{\\lambda}{\\pi\\varepsilon_0} \\frac{l/2}{(l/2)^2 + (l/2)^2} = \\frac{\\lambda}{\\pi\\varepsilon_0} \\frac{l/2}{l^2/2} = \\frac{\\lambda}{\\pi\\varepsilon_0 l}$$",
        "tags": ["parallel threads", "symmetry plane", "maximum electric field", "line charges"]
    },
    {
        "id": "3.23",
        "title": "Field on the Axis of a Cosine-Charged Cylindrical Surface",
        "difficulty": 2,
        "question": "An infinitely long cylindrical surface of circular cross-section is uniformly charged lengthwise with the surface density $\\sigma = \\sigma_0 \\cos\\varphi$, where $\\varphi$ is the polar angle of the cylindrical coordinate system whose $z$-axis coincides with the axis of the given surface. Find the magnitude and direction of the electric field strength vector on the $z$-axis.",
        "hints": [
            "Consider a longitudinal strip of width $R \\, d\\varphi$ on the cylinder of radius $R$.",
            "The linear charge density of this strip is $d\\lambda = \\sigma_0 \\cos\\varphi R \\, d\\varphi$.",
            "Each strip produces field $dE = \\frac{d\\lambda}{2\\pi\\varepsilon_0 R} = \\frac{\\sigma_0 \\cos\\varphi \\, d\\varphi}{2\\pi\\varepsilon_0}$. Integrate over $\\varphi$."
        ],
        "answer": "$E = \\frac{\\sigma_0}{2\\varepsilon_0}$, directed along the angle $\\varphi = \\pi$",
        "solution": "**1. Elemental Line Charge:**\nConsider an axial strip of width $R \\, d\\varphi$ at angle $\\varphi$. It acts as an infinite line charge of linear density:\n$$d\\lambda = \\sigma R \\, d\\varphi = \\sigma_0 \\cos\\varphi R \\, d\\varphi$$\n\n**2. Field on the Axis:**\nThe electric field produced by this line charge at the axis (distance $R$) is directed radially inward/outward:\n$$d\\mathbf{E} = -\\frac{d\\lambda}{2\\pi\\varepsilon_0 R} (\\cos\\varphi \\mathbf{i} + \\sin\\varphi \\mathbf{j}) = -\\frac{\\sigma_0 \\cos\\varphi \\, d\\varphi}{2\\pi\\varepsilon_0} (\\cos\\varphi \\mathbf{i} + \\sin\\varphi \\mathbf{j})$$\n\n**3. Integration:**\nThe $y$-component vanishes by symmetry upon integrating $\\cos\\varphi \\sin\\varphi$. The $x$-component is:\n$$E_x = -\\frac{\\sigma_0}{2\\pi\\varepsilon_0} \\int_0^{2\\pi} \\cos^2\\varphi \\, d\\varphi = -\\frac{\\sigma_0}{2\\pi\\varepsilon_0} (\\pi) = -\\frac{\\sigma_0}{2\\varepsilon_0}$$\nThus, the magnitude is $E = \\frac{\\sigma_0}{2\\varepsilon_0}$, and the vector points in the direction $\\varphi = \\pi$ (negative $x$-axis).",
        "tags": ["cylindrical surface", "cosine charge", "electric field on axis", "line charge integration"]
    },
    {
        "id": "3.24",
        "title": "Flux of an In-Plane Radial Field Through a Sphere",
        "difficulty": 2,
        "question": "The electric field strength depends only on the $x$ and $y$ coordinates according to the law $\\mathbf{E} = a \\frac{x\\mathbf{i} + y\\mathbf{j}}{x^2 + y^2}$, where $a$ is a constant. Find the flux of the vector $\\mathbf{E}$ through a sphere of radius $R$ with its centre at the origin of coordinates.",
        "hints": [
            "Use spherical coordinates: $x = R \\sin\\theta \\cos\\varphi$, $y = R \\sin\\theta \\sin\\varphi$, $z = R \\cos\\theta$.",
            "In cylindrical coordinates, $\\mathbf{E} = \\frac{a}{\\rho} \\hat{\\boldsymbol{\\rho}}$, pointing radially outward in the $xy$ plane.",
            "Compute $\\Phi = \\oint \\mathbf{E} \\cdot d\\mathbf{S} = \\int_0^\\pi \\int_0^{2\\pi} E_r R^2 \\sin\\theta \\, d\\theta \\, d\\varphi$, where $E_r = \\mathbf{E} \\cdot \\hat{\\mathbf{r}} = \\frac{a}{R \\sin\\theta} \\sin\\theta = \\frac{a}{R}$."
        ],
        "answer": "$\\Phi = 4\\pi R a$",
        "solution": "**1. Radial Component on Sphere Surface:**\nThe unit outward normal to the sphere of radius $R$ is $\\hat{\\mathbf{r}} = \\frac{x\\mathbf{i} + y\\mathbf{j} + z\\mathbf{k}}{R}$.\nThe electric field vector is:\n$$\\mathbf{E} = a \\frac{x\\mathbf{i} + y\\mathbf{j}}{x^2 + y^2}$$\nThe normal component of $\\mathbf{E}$ at any point on the sphere surface is:\n$$E_n = \\mathbf{E} \\cdot \\hat{\\mathbf{r}} = a \\frac{x^2 + y^2}{(x^2 + y^2) R} = \\frac{a}{R}$$\nRemarkably, $E_n = \\frac{a}{R}$ is constant over the entire surface of the sphere!\n\n**2. Flux Through the Sphere:**\n$$\\Phi = \\oint_{S} E_n \\, dS = \\frac{a}{R} \\oint_S dS = \\frac{a}{R} (4\\pi R^2) = 4\\pi R a$$",
        "tags": ["electric flux", "divergence theorem", "spherical surface", "radial field"]
    },
    {
        "id": "3.25",
        "title": "Field of a Ball with Linearly Decreasing Charge Density",
        "difficulty": 2,
        "question": "A ball of radius $R$ carries a positive charge whose volume density depends only on separation $r$ from the ball's centre as $\\rho(r) = \\rho_0 \\left(1 - \\frac{r}{R}\\right)$, where $\\rho_0$ is a constant. Assuming the permittivities of the ball and the environment to be equal to unity, find:\n(a) the magnitude of the electric field strength as a function of the distance $r$ both inside and outside the ball;\n(b) the maximum intensity $E_{\\max}$ and the corresponding distance $r_m$.",
        "hints": [
            "Apply Gauss's law: $4\\pi r^2 E(r) = \\frac{q(r)}{\\varepsilon_0}$.",
            "Inside ($r \\le R$): $q(r) = 4\\pi \\int_0^r \\rho_0 (1 - r'/R) r'^2 dr' = 4\\pi \\rho_0 \\left(\\frac{r^3}{3} - \\frac{r^4}{4R}\\right)$.",
            "Differentiate $E(r)$ to find maximum at $r_m = \\frac{2}{3} R$."
        ],
        "answer": "(a) $E(r) = \\frac{\\rho_0 r}{3\\varepsilon_0} \\left(1 - \\frac{3r}{4R}\\right)$ for $r \\le R$, and $E(r) = \\frac{\\rho_0 R^3}{12\\varepsilon_0 r^2}$ for $r \\ge R$; (b) $E_{\\max} = \\frac{\\rho_0 R}{12\\varepsilon_0}$ at $r_m = \\frac{2}{3}R$",
        "solution": "**1. Charge Enclosed as a Function of $r$:**\nFor $r \\le R$:\n$$q(r) = \\int_0^r \\rho(r') 4\\pi r'^2 dr' = 4\\pi \\rho_0 \\int_0^r \\left( r'^2 - \\frac{r'^3}{R} \\right) dr' = 4\\pi \\rho_0 \\left( \\frac{r^3}{3} - \\frac{r^4}{4R} \\right)$$\n\n**2. Electric Field Inside ($r \\le R$):**\nBy Gauss's law:\n$$4\\pi r^2 E(r) = \\frac{q(r)}{\\varepsilon_0} \\implies E(r) = \\frac{\\rho_0 r}{3\\varepsilon_0} \\left( 1 - \\frac{3r}{4R} \\right)$$\n\n**3. Electric Field Outside ($r \\ge R$):**\nThe total charge of the ball is $q(R) = 4\\pi \\rho_0 \\left( \\frac{R^3}{3} - \\frac{R^3}{4} \\right) = \\frac{\\pi \\rho_0 R^3}{3}$:\n$$E(r) = \\frac{q(R)}{4\\pi\\varepsilon_0 r^2} = \\frac{\\rho_0 R^3}{12\\varepsilon_0 r^2}$$\n\n**4. Maximum Electric Field:**\nSetting $\\frac{dE}{dr} = 0$ for $r \\le R$:\n$$\\frac{d}{dr} \\left( r - \\frac{3r^2}{4R} \\right) = 1 - \\frac{6r}{4R} = 1 - \\frac{3r}{2R} = 0 \\implies r_m = \\frac{2}{3} R$$\nSubstituting $r_m = \\frac{2}{3}R$ into $E(r)$:\n$$E_{\\max} = \\frac{\\rho_0 (2R/3)}{3\\varepsilon_0} \\left( 1 - \\frac{3(2R/3)}{4R} \\right) = \\frac{2\\rho_0 R}{9\\varepsilon_0} \\left( 1 - \\frac{1}{2} \\right) = \\frac{\\rho_0 R}{9\\varepsilon_0} \\times \\frac{1}{2} = \\frac{\\rho_0 R}{12\\varepsilon_0}$$",
        "tags": ["Gauss law", "spherical charge", "variable density", "maximum field"]
    }
]
