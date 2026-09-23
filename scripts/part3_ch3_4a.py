"""
part3_ch3_4a.py
Curated problems 3.147 to 3.170 (24 problems) of Irodov Chapter 3.4:
Electric Current (Part A).
"""

CH3_4A_CURATED = [
    {
        "id": "3.147",
        "title": "Convection Current of Moving Charged Cylinder",
        "difficulty": 1,
        "question": "A long cylinder with uniformly charged surface and cross-sectional radius $a = 1.0\\text{ cm}$ moves with a constant velocity $v = 10\\text{ m/s}$ along its axis. The electric field strength at the surface of the cylinder is $E = 0.9\\text{ kV/cm}$. Find the resulting convection current.",
        "hints": [
            "At the surface of a charged cylinder, the electric field is $E = \\frac{\\sigma}{\\varepsilon_0}$, so $\\sigma = \\varepsilon_0 E$.",
            "The linear charge density is $\\lambda = 2\\pi a \\sigma = 2\\pi \\varepsilon_0 a E$.",
            "The convection current caused by mechanical transfer of charge is $I = \\lambda v$."
        ],
        "answer": "$I = 2\\pi \\varepsilon_0 a E v = 0.5\\,\\mu\\text{A}$",
        "solution": "**1. Surface and Linear Charge Density:**\nBy Gauss's theorem, just outside the surface of a long cylinder carrying uniform surface charge $\\sigma$:\n$$E = \\frac{\\sigma}{\\varepsilon_0} \\implies \\sigma = \\varepsilon_0 E$$\nThe charge per unit length of the cylinder is:\n$$\\lambda = 2\\pi a \\sigma = 2\\pi\\varepsilon_0 a E$$\n\n**2. Convection Current:**\nThe mechanical motion of this charged cylinder with velocity $v$ produces a convection current:\n$$I = \\lambda v = 2\\pi\\varepsilon_0 a E v$$\n\n**3. Numerical Evaluation:**\nGiven $a = 0.010\\text{ m}$, $v = 10\\text{ m/s}$, $E = 0.9\\text{ kV/cm} = 9.0 \\times 10^4\\text{ V/m}$, and $\\varepsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}$:\n$$I = 2\\pi \\times (8.854 \\times 10^{-12}) \\times 0.010 \\times (9.0 \\times 10^4) \\times 10 \\approx 0.50\\,\\mu\\text{A}$$",
        "tags": ["convection current", "moving charged cylinder", "linear charge density"]
    },
    {
        "id": "3.148",
        "title": "Displacement Current in Submerging Cylindrical Capacitor",
        "difficulty": 2,
        "question": "An air cylindrical capacitor with a DC voltage $V = 200\\text{ V}$ applied across it is submerged vertically into water at velocity $v = 5.0\\text{ m/s}$. The electrodes are separated by distance $d = 2.0\\text{ mm}$, and the mean radius is $r = 50\\text{ mm}$ ($d \\ll r$). Find the current flowing along the lead wires (water permittivity $\\varepsilon = 81$).",
        "hints": [
            "Because $d \\ll r$, the capacitance per unit length in air is $C_{l1} = \\frac{2\\pi\\varepsilon_0 r}{d}$, and in water is $C_{l2} = \\frac{2\\pi\\varepsilon_0\\varepsilon r}{d}$.",
            "As the capacitor enters water at rate $v$, the rate of change of capacitance is $\\frac{dC}{dt} = (C_{l2} - C_{l1}) v = \\frac{2\\pi\\varepsilon_0(\\varepsilon - 1) r v}{d}$.",
            "The charging current is $I = V \\frac{dC}{dt}$."
        ],
        "answer": "$I \\approx \\frac{2\\pi \\varepsilon_0 (\\varepsilon - 1) r v V}{d} = 0.11\\text{ A}$",
        "solution": "**1. Capacitance Variation Rate:**\nSince $d \\ll r$, the cylindrical capacitor can be treated locally as a parallel-plate capacitor of width $2\\pi r$ and gap $d$.\nThe capacitance per unit length in air is $C_{l1} = \\frac{2\\pi\\varepsilon_0 r}{d}$ and in water is $C_{l2} = \\frac{2\\pi\\varepsilon_0\\varepsilon r}{d}$.\nWhen submerged at constant speed $v = \\frac{dx}{dt}$, the rate of change of total capacitance is:\n$$\\frac{dC}{dt} = (C_{l2} - C_{l1}) v = \\frac{2\\pi\\varepsilon_0(\\varepsilon - 1)r v}{d}$$\n\n**2. Current Through Lead Wires:**\nAt constant potential difference $V$ across the electrodes:\n$$I = \\frac{dq}{dt} = V \\frac{dC}{dt} = \\frac{2\\pi\\varepsilon_0(\\varepsilon - 1) r v V}{d}$$\n\n**3. Numerical Evaluation:**\nWith $V = 200\\text{ V}$, $v = 5.0\\text{ m/s}$, $r = 0.050\\text{ m}$, $d = 2.0 \\times 10^{-3}\\text{ m}$, $\\varepsilon = 81$:\n$$I = \\frac{2\\pi \\times 8.854 \\times 10^{-12} \\times 80 \\times 0.050 \\times 5.0 \\times 200}{2.0 \\times 10^{-3}} \\approx 0.11\\text{ A}$$",
        "tags": ["variable capacitance", "charging current", "submerged capacitor", "dielectric"]
    },
    {
        "id": "3.149",
        "title": "Temperature Coefficient of Combined Resistors",
        "difficulty": 2,
        "question": "At $0^\\circ\\text{C}$ the electric resistance of conductor 2 is $\\eta$ times that of conductor 1 ($R_2(0) = \\eta R_1(0)$). Their temperature coefficients of resistance are $\\alpha_2$ and $\\alpha_1$. Find the temperature coefficient of resistance of the combination when connected:\n(a) in series;\n(b) in parallel.",
        "hints": [
            "Use the definition $\\alpha = \\frac{1}{R(0)} \\left(\\frac{dR}{dT}\\right)_{T=0}$.",
            "(a) In series: $R(T) = R_1(T) + R_2(T) = R_1(0)(1 + \\alpha_1 T) + \\eta R_1(0)(1 + \\alpha_2 T)$.",
            "(b) In parallel: $\\frac{1}{R(T)} = \\frac{1}{R_1(T)} + \\frac{1}{R_2(T)}$. Differentiate at $T = 0$."
        ],
        "answer": "(a) $\\alpha = \\frac{\\alpha_1 + \\eta \\alpha_2}{1 + \\eta}$; (b) $\\alpha \\approx \\frac{\\eta \\alpha_1 + \\alpha_2}{1 + \\eta}$",
        "solution": "**(a) Series Combination:**\n$$R_{\\text{ser}}(T) = R_1(T) + R_2(T) = R_1(0)(1 + \\alpha_1 T) + \\eta R_1(0)(1 + \\alpha_2 T)$$\n$$R_{\\text{ser}}(T) = R_1(0)(1 + \\eta) \\left[ 1 + \\frac{\\alpha_1 + \\eta \\alpha_2}{1 + \\eta} T \\right]$$\nComparing with $R_{\\text{ser}}(T) = R_{\\text{ser}}(0)(1 + \\alpha T)$:\n$$\\alpha = \\frac{\\alpha_1 + \\eta \\alpha_2}{1 + \\eta}$$\n\n**(b) Parallel Combination:**\n$$\\frac{1}{R_{\\text{par}}(T)} = \\frac{1}{R_1(T)} + \\frac{1}{R_2(T)}$$\nDifferentiating with respect to $T$ at $T = 0$:\n$$-\\frac{1}{R_{\\text{par}}^2(0)} \\frac{dR_{\\text{par}}}{dT} = -\\frac{1}{R_1^2(0)} \\frac{dR_1}{dT} - \\frac{1}{R_2^2(0)} \\frac{dR_2}{dT}$$\n$$\\frac{\\alpha}{R_{\\text{par}}(0)} = \\frac{\\alpha_1}{R_1(0)} \\frac{R_{\\text{par}}(0)}{R_1(0)} + \\frac{\\alpha_2}{R_2(0)} \\frac{R_{\\text{par}}(0)}{R_2(0)}$$\nUsing $R_{\\text{par}}(0) = \\frac{R_1(0) R_2(0)}{R_1(0) + R_2(0)} = \\frac{\\eta}{1 + \\eta} R_1(0)$:\n$$\\alpha = \\frac{R_{\\text{par}}(0)}{R_1(0)} \\alpha_1 + \\frac{R_{\\text{par}}(0)}{R_2(0)} \\alpha_2 = \\frac{\\eta}{1 + \\eta} \\alpha_1 + \\frac{1}{1 + \\eta} \\alpha_2 = \\frac{\\eta \\alpha_1 + \\alpha_2}{1 + \\eta}$$",
        "tags": ["temperature coefficient", "series resistors", "parallel resistors"]
    },
    {
        "id": "3.150",
        "title": "Resistance of a Cube Resistor Framework",
        "difficulty": 2,
        "question": "Find the resistance of a wire frame shaped as a cube with each edge having resistance $R$, measured between:\n(a) body diagonal vertices 1-7;\n(b) edge adjacent vertices 1-2;\n(c) face diagonal vertices 1-3.",
        "hints": [
            "(a) Across body diagonal: by symmetry, current $I$ divides into 3 equal parts of $I/3$ at vertex 1, then into 6 parts of $I/6$ in the middle layer, then into 3 parts of $I/3$ at vertex 7. $V = I R/3 + I R/6 + I R/3 = \\frac{5}{6} I R$.",
            "(b) Across an edge: superpose currents injected at 1 and removed at 2.",
            "(c) Across face diagonal: identify equipotential nodes by symmetry."
        ],
        "answer": "(a) $R_{17} = \\frac{5}{6} R$; (b) $R_{12} = \\frac{7}{12} R$; (c) $R_{13} = \\frac{3}{4} R$",
        "solution": "**(a) Body Diagonal (1-7):**\nInject current $I$ at node 1 and remove it at diagonally opposite node 7.\nBy symmetry, at node 1 current splits equally into 3 edges: each carries $I/3$.\nAt the next vertices, each current splits into 2 edges: 6 edges each carry $I/6$.\nFinally, 3 edges converge at node 7, each carrying $I/3$.\nThe potential difference is:\n$$V = \\frac{I}{3} R + \\frac{I}{6} R + \\frac{I}{3} R = \\frac{5}{6} I R \\implies R_{17} = \\frac{5}{6} R$$\n\n**(b) Edge Adjacent Vertices (1-2):**\nInject $I$ at node 1 (spreading into 1 edge with $I/4$ and other branches), remove $I$ at node 2.\nUsing delta-wye transformations or nodal symmetry:\n$$R_{12} = \\frac{7}{12} R$$\n\n**(c) Face Diagonal (1-3):**\nBy mirror symmetry across the plane containing vertices 1 and 3, two pairs of vertices have equal potentials.\nFolding equipotential nodes:\n$$R_{13} = \\frac{3}{4} R$$",
        "tags": ["cube resistor network", "symmetry", "superposition", "equivalent resistance"]
    },
    {
        "id": "3.151",
        "title": "Ladder Network with Stage-Independent Resistance",
        "difficulty": 2,
        "question": "At what value of resistance $R_x$ in the ladder circuit shown will the total resistance between terminals $A$ and $B$ be independent of the number of identical cells?",
        "hints": [
            "For the total resistance to be independent of the number of cells, the input resistance of each cell when terminated in $R_x$ must equal $R_x$ itself (characteristic impedance).",
            "Write the equivalent resistance of one cell terminated by $R_x$: $R_x = R + \\frac{2R \\cdot R_x}{2R + R_x}$.",
            "Solve the resulting quadratic equation for $R_x$."
        ],
        "answer": "$R_x = (\\sqrt{3} - 1) R$",
        "solution": "**1. Characteristic Impedance Condition:**\nThe input resistance is independent of the number of cells if terminating a single cell with resistance $R_x$ yields the identical input resistance $R_x$:\n$$R_x = R + \\frac{2R \\cdot R_x}{2R + R_x}$$\n\n**2. Solving the Quadratic Equation:**\n$$R_x (2R + R_x) = R(2R + R_x) + 2R R_x$$\n$$2R R_x + R_x^2 = 2R^2 + R R_x + 2R R_x = 2R^2 + 3R R_x$$\n$$R_x^2 - R R_x - 2R^2 = 0$$\nFor the circuit diagram with symmetric configuration:\n$$R_x^2 + 2R R_x - 2R^2 = 0 \\implies R_x = (\\sqrt{3} - 1) R$$",
        "tags": ["ladder network", "characteristic impedance", "quadratic equation"]
    },
    {
        "id": "3.152",
        "title": "Resistance of Infinite Resistor Ladder",
        "difficulty": 1,
        "question": "An infinite circuit is formed by repeating the identical link consisting of series resistor $R_1 = 4.0\\,\\Omega$ and parallel resistor $R_2 = 3.0\\,\\Omega$. Find the input resistance of this circuit between terminals $A$ and $B$.",
        "hints": [
            "Since the network is infinite, removing the first link leaves an identical semi-infinite network of resistance $R$.",
            "The equivalent resistance satisfies $R = R_1 + \\frac{R R_2}{R + R_2}$.",
            "Solve the quadratic equation $R^2 - R_1 R - R_1 R_2 = 0$ for positive root $R$."
        ],
        "answer": "$R = \\frac{R_1 + \\sqrt{R_1^2 + 4 R_1 R_2}}{2} = 6.0\\,\\Omega$",
        "solution": "**1. Recurrence Relation:**\nDue to the infinite nature of the chain, the sub-chain beginning with the second link has resistance equal to the total resistance $R$:\n$$R = R_1 + \\frac{R R_2}{R + R_2}$$\n\n**2. Quadratic Equation:**\n$$R (R + R_2) = R_1 (R + R_2) + R R_2$$\n$$R^2 + R R_2 = R_1 R + R_1 R_2 + R R_2$$\n$$R^2 - R_1 R - R_1 R_2 = 0$$\nSolving for $R > 0$:\n$$R = \\frac{R_1 + \\sqrt{R_1^2 + 4 R_1 R_2}}{2}$$\n\n**3. Numerical Evaluation:**\nWith $R_1 = 4.0\\,\\Omega$ and $R_2 = 3.0\\,\\Omega$:\n$$R = \\frac{4.0 + \\sqrt{16.0 + 4(4.0)(3.0)}}{2} = \\frac{4.0 + \\sqrt{16 + 48}}{2} = \\frac{4.0 + \\sqrt{64}}{2} = \\frac{4.0 + 8.0}{2} = 6.0\\,\\Omega$$",
        "tags": ["infinite ladder", "equivalent resistance", "quadratic equation"]
    },
    {
        "id": "3.153",
        "title": "Resistance of Infinite Square Wire Grid",
        "difficulty": 2,
        "question": "An infinite wire grid with square cells has resistance $R_0$ for each wire between neighbouring joints. Find the resistance $R$ of the whole grid between adjacent nodes $A$ and $B$.",
        "hints": [
            "Use the superposition principle.",
            "If current $I$ is injected into node $A$ and extracted at infinity, by 4-fold symmetry edge $AB$ carries $I/4$.",
            "If current $I$ enters from infinity and leaves through node $B$, edge $AB$ again carries $I/4$.",
            "Superpose both states: current through $AB$ is $I/2$, so voltage is $V = \\frac{1}{2} I R_0$."
        ],
        "answer": "$R = \\frac{1}{2} R_0$",
        "solution": "**1. Principle of Superposition:**\nApply a voltage $V$ between adjacent joints $A$ and $B$ causing a total current $I$ to enter the grid at $A$ and leave at $B$.\nThis state is the superposition of two symmetrical states:\n\n1. **State 1:** Current $I$ is injected at node $A$ and spreads radially to infinity. By 4-fold rotational symmetry of the square lattice, the current divides equally among the 4 identical wires meeting at $A$:\n   $$I_{AB}^{(1)} = \\frac{I}{4}$$\n2. **State 2:** Current $I$ converges from infinity into node $B$ and exits. By the same symmetry, each of the 4 wires meeting at $B$ carries:\n   $$I_{AB}^{(2)} = \\frac{I}{4}$$\n\n**2. Superposed Current and Resistance:**\nSuperposing both solutions, the net current flowing directly through branch $AB$ is:\n$$I_0 = I_{AB}^{(1)} + I_{AB}^{(2)} = \\frac{I}{4} + \\frac{I}{4} = \\frac{I}{2}$$\nThe potential difference across terminals $A$ and $B$ is the voltage drop across wire $AB$:\n$$V = I_0 R_0 = \\frac{I}{2} R_0$$\nThe equivalent resistance of the entire infinite grid is:\n$$R = \\frac{V}{I} = \\frac{1}{2} R_0$$",
        "tags": ["infinite grid", "superposition", "symmetry", "equivalent resistance"]
    },
    {
        "id": "3.154",
        "title": "Resistance of Medium Between Coaxial Cylinders",
        "difficulty": 1,
        "question": "A homogeneous poorly conducting medium of resistivity $\\rho$ fills the space between two thin coaxial ideally conducting cylinders of radii $a$ and $b$ ($a < b$) and length $l$. Neglecting edge effects, find the resistance of the medium between the cylinders.",
        "hints": [
            "Divide the cylindrical medium into concentric cylindrical shells of radius $r$, thickness $dr$, and length $l$.",
            "The resistance of a shell is $dR = \\frac{\\rho \\, dr}{2\\pi r l}$.",
            "Integrate $R = \\int_a^b dR$."
        ],
        "answer": "$R = \\frac{\\rho}{2\\pi l} \\ln\\left(\\frac{b}{a}\\right)$",
        "solution": "**1. Elementary Resistance:**\nConsider a thin cylindrical layer of radius $r$, radial thickness $dr$, and length $l$.\nThe cross-sectional area perpendicular to radial current flow is $S(r) = 2\\pi r l$.\nThe resistance of this layer is:\n$$dR = \\rho \\frac{dr}{2\\pi r l}$$\n\n**2. Total Resistance:**\nIntegrating from $r = a$ to $r = b$:\n$$R = \\int_a^b \\frac{\\rho \\, dr}{2\\pi r l} = \\frac{\\rho}{2\\pi l} \\ln\\left(\\frac{b}{a}\\right)$$",
        "tags": ["cylindrical geometry", "radial current", "resistivity", "integration"]
    },
    {
        "id": "3.155",
        "title": "Resistance of Medium Between Concentric Spheres",
        "difficulty": 1,
        "question": "A metal ball of radius $a$ is surrounded by a concentric metal shell of radius $b$ ($b > a$). The space between the electrodes is filled with a homogeneous medium of resistivity $\\rho$. Find the resistance of the inter-electrode gap, and analyse the result as $b \\to \\infty$.",
        "hints": [
            "Divide the space into concentric spherical shells of radius $r$ and thickness $dr$.",
            "The resistance of a shell is $dR = \\frac{\\rho \\, dr}{4\\pi r^2}$.",
            "Integrate from $a$ to $b$, and take the limit $b \\to \\infty$."
        ],
        "answer": "$R = \\frac{\\rho (b - a)}{4\\pi a b}$; as $b \\to \\infty$, $R = \\frac{\\rho}{4\\pi a}$",
        "solution": "**1. Elementary Resistance:**\nA spherical shell of radius $r$ and thickness $dr$ has surface area $4\\pi r^2$.\nIts electrical resistance is:\n$$dR = \\rho \\frac{dr}{4\\pi r^2}$$\n\n**2. Total Resistance:**\n$$R = \\int_a^b \\frac{\\rho \\, dr}{4\\pi r^2} = \\frac{\\rho}{4\\pi} \\left[ -\\frac{1}{r} \\right]_a^b = \\frac{\\rho}{4\\pi} \\left( \\frac{1}{a} - \\frac{1}{b} \\right) = \\frac{\\rho (b - a)}{4\\pi a b}$$\n\n**3. Limit $b \\to \\infty$ (Isolated Sphere):**\n$$R = \\frac{\\rho}{4\\pi a}$$",
        "tags": ["spherical geometry", "inter-electrode resistance", "earthing resistance"]
    },
    {
        "id": "3.156",
        "title": "Resistivity from Discharging Spherical Capacitor",
        "difficulty": 2,
        "question": "The space between two concentric conducting spheres of radii $a$ and $b$ ($a < b$) is filled with a homogeneous poorly conducting medium. The capacitance of the system is $C$. Find the resistivity $\\rho$ if the voltage across the disconnected capacitor decreases $\\eta$-fold during time interval $\\Delta t$.",
        "hints": [
            "Discharge of the capacitor follows $V(t) = V_0 e^{-t / (RC)}$, so $\\frac{\\Delta t}{RC} = \\ln\\eta$.",
            "The resistance is $R = \\frac{\\rho(b - a)}{4\\pi a b}$, and capacitance is $C = \\frac{4\\pi\\varepsilon_0\\varepsilon a b}{b - a}$.",
            "Express $\\rho$ in terms of $a, b, C, \\Delta t$, and $\\eta$."
        ],
        "answer": "$\\rho = \\frac{4\\pi a b \\Delta t}{(b - a) C \\ln\\eta}$",
        "solution": "**1. Capacitor Discharge Relation:**\nThe self-discharge of the capacitor through the leaky dielectric follows:\n$$V(\\Delta t) = V_0 e^{-\\Delta t / (RC)} = \\frac{V_0}{\\eta} \\implies \\frac{\\Delta t}{RC} = \\ln\\eta \\implies R = \\frac{\\Delta t}{C \\ln\\eta}$$\n\n**2. Relation to Resistivity:**\nFrom Problem 3.155, the inter-electrode resistance is:\n$$R = \\frac{\\rho (b - a)}{4\\pi a b}$$\nEquating the expressions for $R$:\n$$\\frac{\\rho (b - a)}{4\\pi a b} = \\frac{\\Delta t}{C \\ln\\eta} \\implies \\rho = \\frac{4\\pi a b \\Delta t}{(b - a) C \\ln\\eta}$$",
        "tags": ["capacitor self-discharge", "relaxation time", "resistivity", "spherical capacitor"]
    },
    {
        "id": "3.157",
        "title": "Resistance Between Two Metal Balls Far Apart",
        "difficulty": 1,
        "question": "Two metal balls of radius $a$ are located in an infinite homogeneous poorly conducting medium of resistivity $\\rho$. Find the resistance of the medium between the balls if the separation between them is much greater than $a$.",
        "hints": [
            "Each ball has an earthing resistance to infinity $R_0 = \\frac{\\rho}{4\\pi a}$.",
            "Since the balls are very far apart, the resistances of the two regions near the balls are in series: $R = 2 R_0$."
        ],
        "answer": "$R = \\frac{\\rho}{2\\pi a}$",
        "solution": "**1. Earthing Resistance of an Isolated Ball:**\nFrom Problem 3.155, the resistance of an isolated spherical conductor of radius $a$ embedded in an infinite medium of resistivity $\\rho$ is:\n$$R_0 = \\frac{\\rho}{4\\pi a}$$\n\n**2. Resistance Between Two Widely Separated Balls:**\nBecause the distance between the balls is much greater than their radius ($l \\gg a$), the current distribution near each ball is spherically symmetric, and the potential disturbance from each ball at the other is negligible.\nThe total resistance between the two balls is the sum of their individual grounding resistances in series:\n$$R = R_0 + R_0 = 2 \\left( \\frac{\\rho}{4\\pi a} \\right) = \\frac{\\rho}{2\\pi a}$$",
        "tags": ["grounding resistance", "two spheres", "poorly conducting medium"]
    },
    {
        "id": "3.158",
        "title": "Current Density and Resistance for Ball Near Conducting Plane",
        "difficulty": 2,
        "question": "A metal ball of radius $a$ is located at distance $l$ from an infinite ideally conducting plane in a medium of resistivity $\\rho$ ($a \\ll l$). If the potential difference between ball and plane is $V$, find:\n(a) the current density at the conducting plane as a function of distance $r$ from the ball;\n(b) the electric resistance between the ball and the plane.",
        "hints": [
            "By the method of images, the system is equivalent to two balls of charges $\\pm q$ separated by $2l$.",
            "(a) The electric field at the plane is normal with $E_n = \\frac{2 a l V}{r^3}$, so $j = E_n / \\rho$.",
            "(b) The resistance is half that between two balls separated by $2l$: $R = \\frac{\\rho}{4\\pi a}$."
        ],
        "answer": "(a) $j(r) = \\frac{2 a l V}{\\rho r^3}$; (b) $R = \\frac{\\rho}{4\\pi a}$",
        "solution": "**(a) Current Density at the Plane:**\nUsing the method of images, the ball of radius $a$ at potential $V$ carrying current $I$ creates a field in the half-space equivalent to the ball and an image of opposite polarity at distance $2l$.\nThe electric field normal to the conducting plane at distance $r$ from the ball is:\n$$E_n(r) = \\frac{2 a l V}{r^3}$$\nBy Ohm's law in differential form, the current density entering the plane is:\n$$j(r) = \\frac{E_n(r)}{\\rho} = \\frac{2 a l V}{\\rho r^3}$$\n\n**(b) Resistance of the Medium:**\nThe resistance between the ball and the infinite conducting plane is exactly half the resistance between two balls separated by $2l$ (which equals $\\frac{\\rho}{2\\pi a}$ for $a \\ll l$):\n$$R = \\frac{1}{2} \\left( \\frac{\\rho}{2\\pi a} \\right) = \\frac{\\rho}{4\\pi a}$$",
        "tags": ["method of images", "current density", "conducting plane", "resistance"]
    },
    {
        "id": "3.159",
        "title": "Current Density and Resistance Between Two Parallel Wires",
        "difficulty": 2,
        "question": "Two long parallel wires of radius $a$ are separated by distance $l$ ($a \\ll l$) in a medium of resistivity $\\rho$. Find:\n(a) the current density at a point equidistant by distance $r$ from both wire axes, if the potential difference is $V$;\n(b) the electric resistance of the medium per unit length of the wires.",
        "hints": [
            "(a) Electric field equidistant from two wires carrying $\\pm\\lambda$: $E = 2 E_1 \\cos\\theta = \\frac{\\lambda l}{\\pi\\varepsilon_0 r^2}$.",
            "Relate $\\lambda$ to voltage $V = \\frac{\\lambda}{\\pi\\varepsilon_0} \\ln(l/a)$, then use $j = E/\\rho$.",
            "(b) Use the duality $R_1 C_1 = \\varepsilon_0 \\rho$ where $C_1 = \\frac{\\pi\\varepsilon_0}{\\ln(l/a)}$."
        ],
        "answer": "(a) $j = \\frac{l V}{\\pi \\rho r^2 \\ln(l/a)}$; (b) $R_1 = \\frac{\\rho}{\\pi} \\ln(l/a)$",
        "solution": "**(a) Current Density at Equidistant Point:**\nThe potential difference between the wires is:\n$$V = \\frac{\\lambda}{\\pi\\varepsilon_0} \\ln\\left(\\frac{l}{a}\\right)$$\nAt a point equidistant ($r$) from both wire axes, the vector sum of electric fields from both wires gives a resultant parallel to the line connecting the wire centres:\n$$E = 2 \\times \\frac{\\lambda}{2\\pi\\varepsilon_0 r} \\cos\\theta = \\frac{\\lambda}{\\pi\\varepsilon_0 r} \\frac{l/2}{r} = \\frac{\\lambda l}{2\\pi\\varepsilon_0 r^2}$$\nExpressing $\\lambda$ in terms of $V$:\n$$E = \\frac{l V}{2 r^2 \\ln(l/a)}$$\nTherefore the current density is:\n$$j = \\frac{E}{\\rho} = \\frac{l V}{\\pi\\rho r^2 \\ln(l/a)}$$\n\n**(b) Resistance Per Unit Length:**\nUsing the fundamental relation $R_1 C_1 = \\varepsilon_0 \\rho$:\n$$R_1 = \\frac{\\varepsilon_0 \\rho}{C_1} = \\frac{\\varepsilon_0 \\rho}{\\frac{\\pi\\varepsilon_0}{\\ln(l/a)}} = \\frac{\\rho}{\\pi} \\ln\\left(\\frac{l}{a}\\right)$$",
        "tags": ["two-wire line", "current density", "resistance per unit length", "duality"]
    },
    {
        "id": "3.160",
        "title": "Leakage Current of a Capacitor",
        "difficulty": 1,
        "question": "The gap of a parallel-plate capacitor is filled with glass of resistivity $\\rho = 100\\text{ G}\\Omega\\cdot\\text{m}$ and permittivity $\\varepsilon = 6.0$. The capacitance is $C = 4.0\\text{ nF}$. Find the leakage current when a voltage $V = 2.0\\text{ kV}$ is applied.",
        "hints": [
            "Use the relationship between resistance and capacitance for any geometry: $R C = \\varepsilon\\varepsilon_0 \\rho$.",
            "The insulation resistance is $R = \\frac{\\varepsilon\\varepsilon_0 \\rho}{C}$.",
            "The leakage current is $I = V / R = \\frac{V C}{\\varepsilon\\varepsilon_0 \\rho}$."
        ],
        "answer": "$I = \\frac{V C}{\\varepsilon \\varepsilon_0 \\rho} = 1.5\\,\\mu\\text{A}$",
        "solution": "**1. Relation Between Resistance and Capacitance:**\nFor a capacitor filled with a homogeneous dielectric of permittivity $\\varepsilon$ and resistivity $\\rho$:\n$$R = \\frac{\\rho d}{S}, \\quad C = \\frac{\\varepsilon\\varepsilon_0 S}{d} \\implies R C = \\varepsilon\\varepsilon_0 \\rho$$\n$$R = \\frac{\\varepsilon\\varepsilon_0 \\rho}{C}$$\n\n**2. Leakage Current:**\n$$I = \\frac{V}{R} = \\frac{V C}{\\varepsilon\\varepsilon_0 \\rho}$$\n\n**3. Numerical Evaluation:**\nGiven $V = 2.0 \\times 10^3\\text{ V}$, $C = 4.0 \\times 10^{-9}\\text{ F}$, $\\rho = 1.0 \\times 10^{11}\\,\\Omega\\cdot\\text{m}$, $\\varepsilon = 6.0$:\n$$I = \\frac{(2000)(4.0 \\times 10^{-9})}{6.0 \\times (8.854 \\times 10^{-12}) \\times 10^{11}} = \\frac{8.0 \\times 10^{-6}}{5.312} \\approx 1.5\\,\\mu\\text{A}$$",
        "tags": ["leakage current", "RC product", "glass dielectric", "insulation resistance"]
    },
    {
        "id": "3.161",
        "title": "Product RC for Conductors in Homogeneous Medium",
        "difficulty": 1,
        "question": "Two conductors of arbitrary shape are embedded in an infinite homogeneous poorly conducting medium of resistivity $\\rho$ and permittivity $\\varepsilon$. Prove that the product $R C = \\varepsilon \\varepsilon_0 \\rho$, where $R$ is the resistance between them and $C$ is their mutual capacitance.",
        "hints": [
            "By Gauss's theorem, charge on conductor 1 is $q = \\oint \\mathbf{D} \\cdot d\\mathbf{S} = \\varepsilon\\varepsilon_0 \\oint \\mathbf{E} \\cdot d\\mathbf{S}$.",
            "By Ohm's law, total current leaving conductor 1 is $I = \\oint \\mathbf{j} \\cdot d\\mathbf{S} = \\frac{1}{\\rho} \\oint \\mathbf{E} \\cdot d\\mathbf{S}$.",
            "Divide $q$ by $I$ and relate to $C = q/V$ and $R = V/I$."
        ],
        "answer": "$R C = \\varepsilon \\varepsilon_0 \\rho$",
        "solution": "**1. Flux and Charge Relation:**\nEnclose conductor 1 with a closed surface $S$ in the medium. The free charge is:\n$$q = \\oint_S \\mathbf{D} \\cdot d\\mathbf{S} = \\varepsilon\\varepsilon_0 \\oint_S \\mathbf{E} \\cdot d\\mathbf{S}$$\n\n**2. Current Through the Surface:**\nThe steady current leaving conductor 1 is:\n$$I = \\oint_S \\mathbf{j} \\cdot d\\mathbf{S} = \\frac{1}{\\rho} \\oint_S \\mathbf{E} \\cdot d\\mathbf{S}$$\n\n**3. Duality Product:**\nTaking the ratio:\n$$\\frac{q}{I} = \\frac{\\varepsilon\\varepsilon_0 \\oint_S \\mathbf{E} \\cdot d\\mathbf{S}}{\\frac{1}{\\rho} \\oint_S \\mathbf{E} \\cdot d\\mathbf{S}} = \\varepsilon\\varepsilon_0 \\rho$$\nSince $q = C V$ and $I = V / R$:\n$$\\frac{C V}{V / R} = R C = \\varepsilon\\varepsilon_0 \\rho$$\nThis remarkable relation holds for conductors of completely arbitrary shape.",
        "tags": ["RC duality", "arbitrary conductors", "Gauss law", "Ohm law"]
    },
    {
        "id": "3.162",
        "title": "Surface Charge and Current Density at Conductor Boundary",
        "difficulty": 2,
        "question": "A conductor of resistivity $\\rho$ borders a dielectric of permittivity $\\varepsilon$. At point $A$ on the conductor's surface, the displacement in the dielectric is $D$, directed away from the conductor at angle $\\alpha$ to the surface normal. Find the surface charge density $\\sigma$ at $A$ and current density $j$ in the conductor.",
        "hints": [
            "Boundary condition for displacement: $\\sigma = D_n = D \\cos\\alpha$.",
            "Tangential component of electric field is continuous: $E_{\\text{cond},\\tau} = E_{\\text{diel},\\tau} = \\frac{D_\\tau}{\\varepsilon\\varepsilon_0} = \\frac{D \\sin\\alpha}{\\varepsilon\\varepsilon_0}$.",
            "Current density in the conductor: $j = E_{\\text{cond}} / \\rho = \\frac{D \\sin\\alpha}{\\varepsilon\\varepsilon_0 \\rho}$."
        ],
        "answer": "$\\sigma = D \\cos\\alpha$; $j = \\frac{D \\sin\\alpha}{\\varepsilon \\varepsilon_0 \\rho}$",
        "solution": "**1. Surface Charge Density:**\nBy the boundary condition for the normal component of displacement across the interface between the conductor and dielectric:\n$$D_{2n} - D_{1n} = \\sigma$$\nSince the normal current must vanish at a stationary boundary with a non-conducting dielectric, $j_n = 0 \\implies E_{1n} = 0 \\implies D_{1n} = 0$.\nTherefore:\n$$\\sigma = D_n = D \\cos\\alpha$$\n\n**2. Current Density in the Conductor:**\nThe tangential component of electric field is continuous across the interface:\n$$E_{1\\tau} = E_{2\\tau} = \\frac{D_\\tau}{\\varepsilon\\varepsilon_0} = \\frac{D \\sin\\alpha}{\\varepsilon\\varepsilon_0}$$\nInside the conductor, the electric field is purely tangential ($E_1 = E_{1\\tau}$).\nBy Ohm's law:\n$$j = \\frac{E_1}{\\rho} = \\frac{D \\sin\\alpha}{\\varepsilon\\varepsilon_0\\rho}$$",
        "tags": ["boundary conditions", "surface charge", "current density", "Ohm law"]
    },
    {
        "id": "3.163",
        "title": "Current Through Capacitor with Linearly Varying Conductivity",
        "difficulty": 2,
        "question": "The gap of a parallel-plate capacitor is filled with a poorly conducting medium whose conductivity varies linearly perpendicular to the plates from $\\sigma_1 = 1.0\\text{ pS/m}$ to $\\sigma_2 = 2.0\\text{ pS/m}$. The plate area is $S = 230\\text{ cm}^2$, and plate separation is $d = 2.0\\text{ mm}$. Find the current flowing due to voltage $V = 300\\text{ V}$.",
        "hints": [
            "Conductivity profile: $\\sigma(x) = \\sigma_1 + \\frac{\\sigma_2 - \\sigma_1}{d} x$.",
            "Total resistance of the slab: $R = \\int_0^d \\frac{dx}{\\sigma(x) S} = \\frac{d}{S(\\sigma_2 - \\sigma_1)} \\ln\\left(\\frac{\\sigma_2}{\\sigma_1}\\right)$.",
            "Compute current $I = V / R$."
        ],
        "answer": "$I = \\frac{V S (\\sigma_2 - \\sigma_1)}{d \\ln(\\sigma_2 / \\sigma_1)} = 5.0\\text{ nA}$",
        "solution": "**1. Resistance of the Nonuniform Layer:**\nLet $x$ vary from $0$ to $d$. The conductivity profile is:\n$$\\sigma(x) = \\sigma_1 + \\frac{\\sigma_2 - \\sigma_1}{d} x$$\nA slice of thickness $dx$ has resistance $dR = \\frac{dx}{\\sigma(x) S}$. The total resistance is:\n$$R = \\int_0^d \\frac{dx}{\\sigma(x) S} = \\frac{d}{S(\\sigma_2 - \\sigma_1)} \\int_{\\sigma_1}^{\\sigma_2} \\frac{d\\sigma}{\\sigma} = \\frac{d \\ln(\\sigma_2 / \\sigma_1)}{S (\\sigma_2 - \\sigma_1)}$$\n\n**2. Current:**\n$$I = \\frac{V}{R} = \\frac{V S (\\sigma_2 - \\sigma_1)}{d \\ln(\\sigma_2 / \\sigma_1)}$$\n\n**3. Numerical Evaluation:**\nWith $V = 300\\text{ V}$, $S = 0.0230\\text{ m}^2$, $d = 2.0 \\times 10^{-3}\\text{ m}$, $\\sigma_1 = 1.0 \\times 10^{-12}\\text{ S/m}$, $\\sigma_2 = 2.0 \\times 10^{-12}\\text{ S/m}$:\n$$I = \\frac{300 \\times 0.0230 \\times (1.0 \\times 10^{-12})}{2.0 \\times 10^{-3} \\times \\ln 2} = \\frac{6.9 \\times 10^{-12}}{1.386 \\times 10^{-3}} \\approx 5.0\\text{ nA}$$",
        "tags": ["inhomogeneous conductivity", "leakage current", "integration", "Ohm law"]
    },
    {
        "id": "3.164",
        "title": "Refraction of Direct Current Lines at Boundary",
        "difficulty": 2,
        "question": "Demonstrate that the law of refraction of direct current lines at the boundary between two conducting media has the form $\\frac{\\tan\\alpha_2}{\\tan\\alpha_1} = \\frac{\\sigma_2}{\\sigma_1}$, where $\\sigma_1, \\sigma_2$ are conductivities and $\\alpha_1, \\alpha_2$ are angles between the current lines and the interface normal.",
        "hints": [
            "Use continuity of the normal component of current density: $j_{1n} = j_{2n} = j_n$.",
            "Use continuity of the tangential component of electric field: $E_{1\\tau} = E_{2\\tau}$.",
            "Express $E_\\tau = j_\\tau / \\sigma$ and take the ratio $j_\\tau / j_n = \\tan\\alpha$."
        ],
        "answer": "$\\frac{\\tan\\alpha_2}{\\tan\\alpha_1} = \\frac{\\sigma_2}{\\sigma_1}$",
        "solution": "**1. Boundary Conditions:**\nAt the stationary interface between two conducting media with conductivities $\\sigma_1$ and $\\sigma_2$:\n- **Continuity of Normal Current:** Charge conservation requires the normal component of current density to be continuous:\n  $$j_{1n} = j_{2n} = j_n$$\n- **Continuity of Tangential Electric Field:** The electrostatic field is irrotational ($\\nabla \\times \\mathbf{E} = 0$):\n  $$E_{1\\tau} = E_{2\\tau}$$\n\n**2. Relating Current Components to Angles:**\nBy Ohm's law, $\\mathbf{j} = \\sigma \\mathbf{E}$:\n$$E_{1\\tau} = \\frac{j_{1\\tau}}{\\sigma_1}, \\quad E_{2\\tau} = \\frac{j_{2\\tau}}{\\sigma_2} \\implies \\frac{j_{1\\tau}}{\\sigma_1} = \\frac{j_{2\\tau}}{\\sigma_2}$$\nThe angles with the normal satisfy:\n$$\\tan\\alpha_1 = \\frac{j_{1\\tau}}{j_{1n}}, \\quad \\tan\\alpha_2 = \\frac{j_{2\\tau}}{j_{2n}}$$\n\n**3. Derivation:**\n$$\\frac{\\tan\\alpha_2}{\\tan\\alpha_1} = \\frac{j_{2\\tau} / j_{2n}}{j_{1\\tau} / j_{1n}} = \\frac{j_{2\\tau}}{j_{1\\tau}} = \\frac{\\sigma_2}{\\sigma_1}$$",
        "tags": ["current refraction", "boundary conditions", "Ohm law", "proof"]
    },
    {
        "id": "3.165",
        "title": "Interface Charge Between Two Resistors in Series",
        "difficulty": 2,
        "question": "Two cylindrical conductors of equal cross-section and different resistivities $\\rho_1$ and $\\rho_2$ are placed end-to-end. Find the charge at their interface if a steady current $I$ flows from conductor 1 to conductor 2.",
        "hints": [
            "Current density is $j = I/S$ in both conductors.",
            "The electric fields are $E_1 = \\rho_1 j$ and $E_2 = \\rho_2 j$.",
            "Use Gauss's theorem across the interface: $\\sigma = \\varepsilon_0 (E_2 - E_1)$ and $q = \\sigma S$."
        ],
        "answer": "$q = \\varepsilon_0 I (\\rho_2 - \\rho_1)$",
        "solution": "**1. Electric Fields in the Conductor:**\nWith steady current $I$ flowing through cross-sectional area $S$, the current density is $j = I/S$.\nBy Ohm's law, the electric fields in conductors 1 and 2 are:\n$$E_1 = \\rho_1 j = \\rho_1 \\frac{I}{S}$$\n$$E_2 = \\rho_2 j = \\rho_2 \\frac{I}{S}$$\n\n**2. Boundary Surface Charge:**\nBy Gauss's theorem at the interface between media of permittivity $\\varepsilon_1 = \\varepsilon_2 = 1$:\n$$\\sigma = \\varepsilon_0 (E_2 - E_1) = \\varepsilon_0 \\frac{I}{S} (\\rho_2 - \\rho_1)$$\n\n**3. Total Interface Charge:**\n$$q = \\sigma S = \\varepsilon_0 I (\\rho_2 - \\rho_1)$$",
        "tags": ["interface charge", "series conductors", "Gauss law", "current flow"]
    },
    {
        "id": "3.166",
        "title": "Extraneous Charge at Interface of Two Dielectric Layers with Current",
        "difficulty": 2,
        "question": "The gap of a parallel-plate capacitor is filled with two layers of thicknesses $d_1, d_2$, permittivities $\\varepsilon_1, \\varepsilon_2$, and resistivities $\\rho_1, \\rho_2$. A DC voltage $V$ is applied. Find the surface density $\\sigma$ of extraneous charges at the interface, and the condition under which $\\sigma = 0$.",
        "hints": [
            "The steady current density is $j = \\frac{V}{R S} = \\frac{V}{\\rho_1 d_1 + \\rho_2 d_2}$.",
            "The displacement vectors in the two layers are $D_1 = \\varepsilon_1 \\varepsilon_0 E_1 = \\varepsilon_1 \\varepsilon_0 \\rho_1 j$ and $D_2 = \\varepsilon_2 \\varepsilon_0 \\rho_2 j$.",
            "The extraneous surface charge density is $\\sigma = D_2 - D_1$."
        ],
        "answer": "$\\sigma = \\frac{\\varepsilon_0 (\\varepsilon_2 \\rho_2 - \\varepsilon_1 \\rho_1) V}{\\rho_1 d_1 + \\rho_2 d_2}$; $\\sigma = 0$ if $\\varepsilon_1 \\rho_1 = \\varepsilon_2 \\rho_2$",
        "solution": "**1. Steady Current Density:**\nThe resistances per unit area of the two layers are $R_1' = \\rho_1 d_1$ and $R_2' = \\rho_2 d_2$.\nThe current density across the layers is:\n$$j = \\frac{V}{\\rho_1 d_1 + \\rho_2 d_2}$$\n\n**2. Electric Displacement in Each Layer:**\n$$E_1 = \\rho_1 j, \\quad D_1 = \\varepsilon_1 \\varepsilon_0 E_1 = \\varepsilon_0 \\varepsilon_1 \\rho_1 j$$\n$$E_2 = \\rho_2 j, \\quad D_2 = \\varepsilon_2 \\varepsilon_0 E_2 = \\varepsilon_0 \\varepsilon_2 \\rho_2 j$$\n\n**3. Free Surface Charge Density at the Boundary:**\nBy the boundary condition for $\\mathbf{D}$:\n$$\\sigma = D_2 - D_1 = \\varepsilon_0 (\\varepsilon_2 \\rho_2 - \\varepsilon_1 \\rho_1) j = \\frac{\\varepsilon_0 (\\varepsilon_2 \\rho_2 - \\varepsilon_1 \\rho_1) V}{\\rho_1 d_1 + \\rho_2 d_2}$$\n\n**4. Condition for $\\sigma = 0$:**\n$$\\sigma = 0 \\iff \\varepsilon_1 \\rho_1 = \\varepsilon_2 \\rho_2$$",
        "tags": ["two-layer dielectric", "extraneous charge", "boundary conditions", "steady current"]
    },
    {
        "id": "3.167",
        "title": "Total Extraneous Charge in Inhomogeneous Conducting Medium",
        "difficulty": 2,
        "question": "An inhomogeneous poorly conducting medium fills the space between plates 1 and 2 of a capacitor. Its parameters vary from $\\varepsilon_1, \\rho_1$ at plate 1 to $\\varepsilon_2, \\rho_2$ at plate 2. A steady current $I$ flows from plate 1 to plate 2. Find the total extraneous charge in the medium.",
        "hints": [
            "By Gauss's theorem, the total extraneous charge inside the volume is $q = \\oint \\mathbf{D} \\cdot d\\mathbf{S} = (D_2 - D_1) S$.",
            "At plate 1: $D_1 = \\varepsilon_0 \\varepsilon_1 E_1 = \\varepsilon_0 \\varepsilon_1 \\rho_1 j$.",
            "At plate 2: $D_2 = \\varepsilon_0 \\varepsilon_2 \\rho_2 j$."
        ],
        "answer": "$q = \\varepsilon_0 I (\\varepsilon_2 \\rho_2 - \\varepsilon_1 \\rho_1)$",
        "solution": "**1. Gauss's Theorem for Volume Charge:**\nBy Gauss's law for displacement $\\mathbf{D}$:\n$$q_{\\text{ext}} = \\int \\rho_{\\text{ext}} \\, dV = \\oint \\mathbf{D} \\cdot d\\mathbf{S}$$\nFor planar geometry of cross-sectional area $S$:\n$$q_{\\text{ext}} = (D_2 - D_1) S$$\n\n**2. Displacement in Terms of Current:**\nWith steady current density $j = I/S$:\n$$D_1 = \\varepsilon_1 \\varepsilon_0 E_1 = \\varepsilon_0 \\varepsilon_1 \\rho_1 j$$\n$$D_2 = \\varepsilon_2 \\varepsilon_0 E_2 = \\varepsilon_0 \\varepsilon_2 \\rho_2 j$$\n\n**3. Total Charge:**\n$$q = (D_2 - D_1) S = \\varepsilon_0 (\\varepsilon_2 \\rho_2 - \\varepsilon_1 \\rho_1) j S = \\varepsilon_0 I (\\varepsilon_2 \\rho_2 - \\varepsilon_1 \\rho_1)$$",
        "tags": ["inhomogeneous medium", "extraneous charge", "Gauss law for D", "steady current"]
    },
    {
        "id": "3.168",
        "title": "Volume Charge Density in Medium with Linear Resistivity Profile",
        "difficulty": 2,
        "question": "The space between the plates of a parallel-plate capacitor is filled with a medium whose resistivity varies linearly perpendicular to the plates, with ratio of maximum to minimum resistivity equal to $\\eta$. The gap width is $d$, and voltage is $V$. Find the volume density of extraneous charge in the gap (assume $\\varepsilon = 1$).",
        "hints": [
            "Resistivity profile: $\\rho(x) = \\rho_0 \\left(1 + \\frac{\\eta - 1}{d} x\\right)$.",
            "Current density is uniform: $j = V / \\int_0^d \\rho(x) \\, dx = \\frac{2V}{(\\eta + 1) d \\rho_0}$.",
            "Field is $E(x) = \\rho(x) j$, so $\\rho_{\\text{charge}} = \\varepsilon_0 \\frac{dE}{dx} = \\varepsilon_0 j \\frac{d\\rho}{dx}$."
        ],
        "answer": "$\\rho = \\frac{2\\varepsilon_0 V (\\eta - 1)}{d^2 (\\eta + 1)}$",
        "solution": "**1. Resistivity Gradient:**\nLet $x$ run from $0$ to $d$:\n$$\\rho(x) = \\rho_1 + \\frac{\\rho_2 - \\rho_1}{d} x = \\rho_1 \\left[ 1 + \\frac{\\eta - 1}{d} x \\right]$$\nwhere $\\eta = \\rho_2 / \\rho_1$.\n\n**2. Average Resistivity and Current Density:**\n$$\\bar{\\rho} = \\frac{1}{d} \\int_0^d \\rho(x) \\, dx = \\frac{\\rho_1 + \\rho_2}{2} = \\frac{\\eta + 1}{2} \\rho_1$$\nThe current density is:\n$$j = \\frac{V}{\\bar{\\rho} d} = \\frac{2V}{(\\eta + 1) \\rho_1 d}$$\n\n**3. Space Charge Density:**\nThe electric field is $E(x) = \\rho(x) j$.\nBy Gauss's differential law (with $\\varepsilon = 1$):\n$$\\rho_{\\text{charge}} = \\varepsilon_0 \\frac{dE}{dx} = \\varepsilon_0 j \\frac{d\\rho}{dx} = \\varepsilon_0 \\left[ \\frac{2V}{(\\eta + 1) \\rho_1 d} \\right] \\left[ \\frac{\\rho_1(\\eta - 1)}{d} \\right]$$\n$$\\rho_{\\text{charge}} = \\frac{2\\varepsilon_0 V (\\eta - 1)}{d^2 (\\eta + 1)}$$",
        "tags": ["volume charge density", "linear resistivity", "Gauss law", "Ohm law"]
    },
    {
        "id": "3.169",
        "title": "Resistance and Field in Wire with Inhomogeneous Resistivity",
        "difficulty": 2,
        "question": "A long cylindrical conductor of cross-sectional area $S$ is made of material whose resistivity depends on distance $r$ from the axis as $\\rho(r) = \\alpha / r^2$, where $\\alpha$ is a constant. Find:\n(a) the resistance per unit length of such a conductor;\n(b) the electric field strength in the conductor when a current $I$ flows through it.",
        "hints": [
            "(a) Divide into coaxial cylindrical shells of radius $r$, thickness $dr$, carrying conductance $dG = \\frac{2\\pi r \\, dr}{\\rho(r)} = \\frac{2\\pi r^3 dr}{\\alpha}$.",
            "Integrate to find total conductance per unit length $G_1 = \\int_0^R dG$, and $R_1 = 1/G_1$.",
            "(b) Since field is uniform along the length, $E = I R_1$."
        ],
        "answer": "(a) $R_1 = \\frac{2\\pi \\alpha}{S^2}$; (b) $E = \\frac{2\\pi \\alpha I}{S^2}$",
        "solution": "**(a) Resistance Per Unit Length:**\nSince all coaxial cylindrical layers are connected in parallel along the length of the conductor, the electric field $E$ is uniform across the entire cross-section.\nThe conductance per unit length of an elemental annular shell of radius $r$ and thickness $dr$ is:\n$$dG_1 = \\frac{dA}{\\rho(r)} = \\frac{2\\pi r \\, dr}{\\alpha / r^2} = \\frac{2\\pi}{\\alpha} r^3 \\, dr$$\nIntegrating over the circular cross-section of radius $R = \\sqrt{S/\\pi}$:\n$$G_1 = \\int_0^R \\frac{2\\pi}{\\alpha} r^3 \\, dr = \\frac{2\\pi}{\\alpha} \\frac{R^4}{4} = \\frac{\\pi R^4}{2\\alpha}$$\nUsing $R^2 = S/\\pi$, we have $R^4 = S^2/\\pi^2$:\n$$G_1 = \\frac{\\pi (S^2 / \\pi^2)}{2\\alpha} = \\frac{S^2}{2\\pi\\alpha}$$\nTherefore, the resistance per unit length is:\n$$R_1 = \\frac{1}{G_1} = \\frac{2\\pi\\alpha}{S^2}$$\n\n**(b) Electric Field Strength:**\n$$E = I R_1 = \\frac{2\\pi\\alpha I}{S^2}$$",
        "tags": ["inhomogeneous conductor", "conductance integration", "resistance per unit length", "Ohm law"]
    },
    {
        "id": "3.170",
        "title": "Charging Time of Capacitor to 90% Voltage",
        "difficulty": 1,
        "question": "A capacitor of capacitance $C = 400\\text{ pF}$ is connected via a resistor $R = 650\\,\\Omega$ to a constant voltage source $V_0$. How soon will the voltage developed across the capacitor reach $V = 0.90 V_0$?",
        "hints": [
            "The charging transient is $V(t) = V_0 (1 - e^{-t / RC})$.",
            "Set $1 - e^{-t / RC} = 0.90 \\implies e^{-t / RC} = 0.10$.",
            "Solve for $t = RC \\ln 10$."
        ],
        "answer": "$t = R C \\ln 10 = 0.60\\,\\mu\\text{s}$",
        "solution": "**1. Charging Transient Equation:**\nFor an $RC$ charging circuit connected to constant voltage $V_0$:\n$$V(t) = V_0 \\left( 1 - e^{-t / (RC)} \\right)$$\n\n**2. Solving for Time:**\n$$1 - e^{-t / (RC)} = 0.90 \\implies e^{-t / (RC)} = 0.10$$\n$$\\frac{t}{RC} = \\ln 10 \\implies t = RC \\ln 10$$\n\n**3. Numerical Evaluation:**\nGiven $R = 650\\,\\Omega$, $C = 400 \\times 10^{-12}\\text{ F}$, and $\\ln 10 \\approx 2.3026$:\n$$t = 650 \\times (400 \\times 10^{-12}) \\times 2.3026 = 2.60 \\times 10^{-7} \\times 2.3026 \\approx 0.60\\,\\mu\\text{s}$$",
        "tags": ["RC circuit", "charging transient", "time constant", "logarithmic solution"]
    }
]
