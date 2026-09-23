"""
part3_ch3_6c.py
Curated problems 3.331 to 3.350 (20 problems) of Irodov Chapter 3.6:
Electromagnetic Induction. Maxwell's Equations (Part C).
"""

CH3_6C_CURATED = [
    {
        "id": "3.331",
        "title": "Mutual Inductance of Concentric Coplanar Circular Loops",
        "difficulty": 2,
        "question": "Two thin concentric wires shaped as circles with radii $a$ and $b$ lie in the same plane, with $a \\ll b$. Find:\n(a) their mutual inductance $L_{12}$;\n(b) the magnetic flux through the surface enclosed by the outside wire when the inside wire carries a current $I$.",
        "hints": [
            "Use the reciprocity theorem: $L_{12} = L_{21}$. It is simpler to find the flux through loop $a$ when current $I$ flows in loop $b$.",
            "The magnetic field produced by current $I$ in loop $b$ at its centre is $B = \\frac{\\mu_0 I}{2b}$, practically uniform across loop $a$.",
            "The flux through loop $a$ is $\\Phi = B (\\pi a^2) = \\frac{\\mu_0 \\pi a^2 I}{2b}$, so $L_{12} = \\frac{\\mu_0 \\pi a^2}{2b}$."
        ],
        "answer": "(a) $L_{12} \\approx \\frac{\\mu_0 \\pi a^2}{2b}$; (b) $\\Phi_{21} = \\frac{\\mu_0 \\pi a^2 I}{2b}$",
        "solution": "**(a) Mutual Inductance:**\nBy the reciprocity of mutual inductance, $L_{12} = L_{21}$.\nSuppose a current $I$ flows through the larger outer loop of radius $b$.\nThe magnetic induction at its centre is:\n$$B = \\frac{\\mu_0 I}{2b}$$\nBecause $a \\ll b$, this magnetic field is practically uniform over the entire area of the smaller concentric inner loop $S_a = \\pi a^2$.\nThe magnetic flux linked with the inner loop is:\n$$\\Phi_{12} = B S_a = \\left( \\frac{\\mu_0 I}{2b} \\right) (\\pi a^2) = \\frac{\\mu_0 \\pi a^2 I}{2b}$$\nThe mutual inductance is:\n$$L_{12} = \\frac{\\Phi_{12}}{I} = \\frac{\\mu_0 \\pi a^2}{2b}$$\n\n**(b) Magnetic Flux Through Outer Wire:**\nWhen the inner wire of radius $a$ carries current $I$, the magnetic flux through the outer loop of radius $b$ is, by reciprocity:\n$$\\Phi_{21} = L_{21} I = L_{12} I = \\frac{\\mu_0 \\pi a^2 I}{2b}$$",
        "tags": ["mutual inductance", "reciprocity theorem", "concentric loops", "magnetic flux"]
    },
    {
        "id": "3.332",
        "title": "Magnetic Moment of Magnet from Ballistic Galvanometer",
        "difficulty": 2,
        "question": "A small cylindrical magnet $M$ is placed at the centre of a thin coil of radius $a$ consisting of $N$ turns. The coil is connected to a ballistic galvanometer, and the active resistance of the whole circuit is $R$. Find the magnetic moment of the magnet if its removal from the coil results in a charge $q$ flowing through the galvanometer.",
        "hints": [
            "Use the reciprocity relation: the interaction energy between a magnetic dipole $\\mathbf{p}_m$ and a current-carrying coil is $W = -\\mathbf{p}_m \\cdot \\mathbf{B}_{\\text{coil}} = -I \\Psi$.",
            "The field at the centre of an $N$-turn coil carrying fictitious current $I$ is $B = \\frac{\\mu_0 N I}{2a}$.",
            "The flux linkage is $\\Psi = \\frac{\\mu_0 N p_m}{2a}$. Charge is $q = \\frac{\\Psi}{R}$, yielding $p_m = \\frac{2 a R q}{\\mu_0 N}$."
        ],
        "answer": "$p_m = \\frac{2 a R q}{\\mu_0 N}$",
        "solution": "**1. Reciprocal Calculation of Flux Linkage:**\nThe magnetic flux linkage $\\Psi$ established in the $N$-turn coil of radius $a$ by a small magnetic dipole $\\mathbf{p}_m$ located at its centre can be determined by reciprocity.\nIf a current $I$ were passed through the coil, it would produce a central magnetic induction:\n$$B = \\frac{\\mu_0 N I}{2a}$$\nThe interaction energy is:\n$$W = -\\mathbf{p}_m \\cdot \\mathbf{B} = -p_m \\left( \\frac{\\mu_0 N I}{2a} \\right)$$\nEquating this to $-I \\Psi$, we find the flux linkage:\n$$\\Psi = \\frac{\\mu_0 N p_m}{2a}$$\n\n**2. Ballistic Charge Measurement:**\nWhen the magnet is removed to infinity, the flux linkage drops from $\\Psi$ to $0$, so $\\Delta\\Psi = \\Psi$.\nThe charge measured by the ballistic galvanometer is:\n$$q = \\frac{\\Delta\\Psi}{R} = \\frac{\\mu_0 N p_m}{2 a R}$$\n\n**3. Magnetic Moment:**\n$$p_m = \\frac{2 a R q}{\\mu_0 N}$$",
        "tags": ["magnetic moment", "ballistic galvanometer", "reciprocity theorem", "flux linkage"]
    },
    {
        "id": "3.333",
        "title": "Mutual Inductance of Distant Coaxial Circular Loops",
        "difficulty": 2,
        "question": "Find the approximate formula expressing the mutual inductance of two thin coaxial loops of the same radius $a$ if their centres are separated by a distance $l$, with $l \\gg a$.",
        "hints": [
            "Since $l \\gg a$, each loop can be treated as a magnetic dipole of moment $p_m = I (\\pi a^2)$.",
            "The on-axis magnetic field of a magnetic dipole at distance $l$ is $B = \\frac{\\mu_0 (2 p_m)}{4\\pi l^3} = \\frac{\\mu_0 I a^2}{2 l^3}$.",
            "The magnetic flux through the second loop of area $\\pi a^2$ is $\\Phi = B (\\pi a^2)$, yielding $L_{12} = \\frac{\\Phi}{I} = \\frac{\\mu_0 \\pi a^4}{2 l^3}$."
        ],
        "answer": "$L_{12} \\approx \\frac{\\mu_0 \\pi a^4}{2 l^3}$",
        "solution": "**1. Magnetic Dipole Approximation:**\nWhen a current $I$ flows through the first circular loop of radius $a$, it acts at large distances ($l \\gg a$) as a magnetic dipole with magnetic moment:\n$$p_m = I (\\pi a^2)$$\n\n**2. On-Axis Magnetic Field:**\nAlong the dipole axis at distance $l$, the magnetic induction is:\n$$B(l) = \\frac{\\mu_0}{4\\pi} \\frac{2 p_m}{l^3} = \\frac{\\mu_0}{4\\pi} \\frac{2 I (\\pi a^2)}{l^3} = \\frac{\\mu_0 I a^2}{2 l^3}$$\n\n**3. Flux Linkage and Mutual Inductance:**\nBecause $l \\gg a$, the field is nearly uniform across the second coaxial loop of area $S = \\pi a^2$.\nThe magnetic flux through the second loop is:\n$$\\Phi = B(l) S = \\left( \\frac{\\mu_0 I a^2}{2 l^3} \\right) (\\pi a^2) = \\frac{\\mu_0 \\pi a^4 I}{2 l^3}$$\nTherefore, the mutual inductance is:\n$$L_{12} = \\frac{\\Phi}{I} = \\frac{\\mu_0 \\pi a^4}{2 l^3}$$",
        "tags": ["mutual inductance", "dipole approximation", "coaxial loops", "Biot-Savart law"]
    },
    {
        "id": "3.334",
        "title": "Current in Coupled Secondary Loop with Linearly Increasing Primary Current",
        "difficulty": 2,
        "question": "There are two stationary loops with mutual inductance $L_{12}$. The current in one of the loops starts to vary as $I_1(t) = \\alpha t$, where $\\alpha$ is a constant. Find the time dependence $I_2(t)$ of the current in the other loop, whose self-inductance is $L_2$ and resistance is $R$.",
        "hints": [
            "The electromotive force induced in the second loop by the changing current $I_1$ is $\\mathcal{E}_{21} = -L_{12} \\frac{dI_1}{dt} = -\\alpha L_{12}$.",
            "The differential equation for the secondary circuit is $L_2 \\frac{dI_2}{dt} + R I_2 = \\alpha L_{12}$.",
            "Solve the linear ODE with initial condition $I_2(0) = 0$ to get $I_2(t) = \\frac{\\alpha L_{12}}{R} (1 - e^{-R t / L_2})$."
        ],
        "answer": "$I_2(t) = \\frac{\\alpha L_{12}}{R} \\left( 1 - e^{-\\frac{R t}{L_2}} \\right)$",
        "solution": "**1. Differential Equation for Secondary Loop:**\nThe rate of change of primary current is $\\frac{dI_1}{dt} = \\alpha$.\nThe mutual induction emf acting in the second loop is:\n$$\\mathcal{E}_{21} = -L_{12} \\frac{dI_1}{dt} = -\\alpha L_{12}$$\nTaking the direction of induced current, the circuit equation for the secondary loop with self-inductance $L_2$ and resistance $R$ is:\n$$L_2 \\frac{dI_2}{dt} + R I_2 = \\alpha L_{12}$$\n\n**2. Solution of the ODE:**\nThis is a standard first-order non-homogeneous linear differential equation:\n$$\\frac{dI_2}{dt} + \\frac{R}{L_2} I_2 = \\frac{\\alpha L_{12}}{L_2}$$\nThe general solution is:\n$$I_2(t) = \\frac{\\alpha L_{12}}{R} + C e^{-R t / L_2}$$\n\n**3. Applying Initial Conditions:**\nAt $t = 0$, $I_2(0) = 0$, which gives $C = -\\frac{\\alpha L_{12}}{R}$.\nTherefore:\n$$I_2(t) = \\frac{\\alpha L_{12}}{R} \\left( 1 - e^{-\\frac{R t}{L_2}} \\right)$$",
        "tags": ["mutual induction", "RL transient", "differential equation", "Faraday's law"]
    },
    {
        "id": "3.335",
        "title": "Heat Generated in Coil After Disconnecting Source",
        "difficulty": 2,
        "question": "A coil of inductance $L = 2.0\\,\\mu\\text{H}$ and resistance $R = 1.0\\,\\Omega$ is connected to a source of constant emf $\\mathcal{E} = 3.0\\text{ V}$. A resistance $R_0 = 2.0\\,\\Omega$ is connected in parallel with the coil. Find the amount of heat generated in the coil after the switch disconnecting the source is opened. The internal resistance of the source is negligible.",
        "hints": [
            "Before the switch opens, the steady-state current in the inductor is $I_0 = \\frac{\\mathcal{E}}{R}$.",
            "The stored magnetic energy in the coil is $W_m = \\frac{1}{2} L I_0^2$.",
            "After disconnection, the coil discharges through a closed loop formed by $R$ and $R_0$ in series. The fraction of total energy dissipated in resistor $R$ is $\\frac{R}{R + R_0}$."
        ],
        "answer": "$Q = \\frac{L \\mathcal{E}^2}{2 R (R + R_0)} = 3.0\\,\\mu\\text{J}$",
        "solution": "**1. Initial Current and Stored Magnetic Energy:**\nIn steady state before the switch is opened, the current through the inductor branch of resistance $R$ is:\n$$I_0 = \\frac{\\mathcal{E}}{R}$$\nThe magnetic energy stored in the inductor is:\n$$W_m = \\frac{1}{2} L I_0^2 = \\frac{1}{2} L \\left( \\frac{\\mathcal{E}}{R} \\right)^2 = \\frac{L \\mathcal{E}^2}{2 R^2}$$\n\n**2. Distribution of Dissipated Heat:**\nWhen the source is disconnected, the current from the inductor circulates through a series loop containing resistors $R$ and $R_0$.\nAt any instant, the current $I(t)$ flows identically through both resistors.\nThe instantaneous powers dissipated are:\n$$P_{\\text{coil}}(t) = I^2(t) R, \\quad P_0(t) = I^2(t) R_0$$\nThe total heat generated in the coil is proportional to its resistance:\n$$Q = W_m \\frac{R}{R + R_0} = \\left( \\frac{L \\mathcal{E}^2}{2 R^2} \\right) \\frac{R}{R + R_0} = \\frac{L \\mathcal{E}^2}{2 R (R + R_0)}$$\n\n**3. Numerical Evaluation:**\nGiven $L = 2.0 \\times 10^{-6}\\text{ H}$, $\\mathcal{E} = 3.0\\text{ V}$, $R = 1.0\\,\\Omega$, $R_0 = 2.0\\,\\Omega$:\n$$Q = \\frac{(2.0 \\times 10^{-6})(3.0)^2}{2(1.0)(1.0 + 2.0)} = \\frac{1.80 \\times 10^{-5}}{6.0} = 3.0 \\times 10^{-6}\\text{ J} = 3.0\\,\\mu\\text{J}$$",
        "tags": ["magnetic energy", "energy dissipation", "RL circuit", "Joule heat"]
    },
    {
        "id": "3.336",
        "title": "Magnetic Energy of an Iron Toroid",
        "difficulty": 1,
        "question": "An iron toroid supports $N = 500$ turns. Find the magnetic field energy if a current $I = 2.0\\text{ A}$ produces a magnetic flux across the toroid cross-section equal to $\\Phi = 1.0\\text{ mWb}$.",
        "hints": [
            "The total magnetic flux linkage of the $N$ turns is $\\Psi = N \\Phi$.",
            "For a linear magnetic circuit, the magnetic field energy is $W = \\frac{1}{2} \\Psi I = \\frac{1}{2} N \\Phi I$.",
            "Substitute the given numerical values."
        ],
        "answer": "$W = \\frac{1}{2} N I \\Phi = 0.50\\text{ J}$",
        "solution": "**1. Magnetic Energy from Flux Linkage:**\nFor an iron toroid with $N$ turns, each carrying current $I$ and enclosing magnetic flux $\\Phi$, the total magnetic flux linkage is:\n$$\\Psi = N \\Phi$$\nThe magnetic field energy stored in the toroid is:\n$$W = \\frac{1}{2} \\Psi I = \\frac{1}{2} N I \\Phi$$\n\n**2. Numerical Evaluation:**\nGiven $N = 500$, $I = 2.0\\text{ A}$, $\\Phi = 1.0\\text{ mWb} = 1.0 \\times 10^{-3}\\text{ Wb}$:\n$$W = \\frac{1}{2} (500)(2.0\\text{ A})(1.0 \\times 10^{-3}\\text{ Wb}) = 0.50\\text{ J}$$",
        "tags": ["magnetic energy", "flux linkage", "toroid", "inductance"]
    },
    {
        "id": "3.337",
        "title": "Magnetic Energy of Iron Doughnut Core",
        "difficulty": 2,
        "question": "An iron core shaped as a doughnut with round cross-section of radius $a = 3.0\\text{ cm}$ carries a winding of $N = 1000$ turns through which a current $I = 1.0\\text{ A}$ flows. The mean radius of the doughnut is $b = 32\\text{ cm}$. Find the magnetic energy stored in the core, assuming the magnetic field strength $H$ is uniform throughout the cross-section and equal to its value at the mean radius.",
        "hints": [
            "The magnetic field strength along the mean circle of radius $b$ is $H = \\frac{N I}{2\\pi b}$.",
            "The volume of the doughnut core is $V = (2\\pi b)(\\pi a^2) = 2\\pi^2 a^2 b$.",
            "From the magnetization curve of iron, determine induction $B$ for the calculated $H$, and find the energy $W = \\frac{1}{2} B H V = \\pi^2 a^2 b B H$."
        ],
        "answer": "$W = \\pi^2 a^2 b B H \\approx 2.0\\text{ J}$, where $H = \\frac{N I}{2\\pi b} \\approx 500\\text{ A/m}$",
        "solution": "**1. Magnetic Field Strength:**\nAlong the circular centerline of radius $b$, Ampère's circuital law gives:\n$$H \\cdot (2\\pi b) = N I \\implies H = \\frac{N I}{2\\pi b}$$\nWith $N = 1000$, $I = 1.0\\text{ A}$, $b = 0.32\\text{ m}$:\n$$H = \\frac{1000 \\times 1.0}{2\\pi (0.32)} \\approx 497\\text{ A/m} \\approx 500\\text{ A/m}$$\n\n**2. Core Volume and Induction:**\nThe cross-sectional area is $S = \\pi a^2$.\nThe volume of the toroidal core is:\n$$V = 2\\pi b \\cdot \\pi a^2 = 2\\pi^2 a^2 b$$\nFrom the magnetization curve of transformer iron, at $H \\approx 500\\text{ A/m}$, the magnetic induction is approximately $B \\approx 1.0\\text{ T}$.\n\n**3. Stored Magnetic Energy:**\n$$W = \\frac{1}{2} B H V = \\frac{1}{2} B H (2\\pi^2 a^2 b) = \\pi^2 a^2 b B H$$\nEvaluating numerically:\n$$W = \\pi^2 (0.030)^2 (0.32)(1.0)(497) \\approx (9.8696)(9.0 \\times 10^{-4})(0.32)(497) \\approx 2.0 \\times 10^0\\text{ J} = 2.0\\text{ J}$$",
        "tags": ["magnetic energy", "toroid", "magnetization curve", "core volume"]
    },
    {
        "id": "3.338",
        "title": "Magnetic Energy and Inductance of Ring with Air Gap",
        "difficulty": 2,
        "question": "A thin ring made of magnetic material has a mean diameter $d = 30\\text{ cm}$ and supports a winding of $N = 800$ turns. The cross-sectional area of the ring is $S = 5.0\\text{ cm}^2$. The ring has a cross-cut air gap of width $b = 2.0\\text{ mm}$. When the winding carries a current, the permeability of the magnetic material is $\\mu = 1400$. Neglecting flux fringing at the gap edges, find:\n(a) the ratio of magnetic energies in the gap and in the magnetic material;\n(b) the inductance of the system using flux linkage and magnetic energy.",
        "hints": [
            "Because flux is continuous across the gap, $B$ is identical in the core and in the gap.",
            "Energy densities are $w_{\\text{gap}} = \\frac{B^2}{2\\mu_0}$ and $w_m = \\frac{B^2}{2\\mu_0 \\mu}$. The ratio of energies is $\\frac{W_{\\text{gap}}}{W_m} = \\frac{w_{\\text{gap}} S b}{w_m S (\\pi d - b)} \\approx \\frac{\\mu b}{\\pi d}$.",
            "Use Ampère's law to find $B = \\frac{\\mu_0 N I}{b + \\pi d / \\mu}$, then find inductance $L = \\frac{N B S}{I} = \\frac{\\mu_0 N^2 S}{b + \\pi d / \\mu}$."
        ],
        "answer": "(a) $\\frac{W_{\\text{gap}}}{W_m} \\approx \\frac{\\mu b}{\\pi d} \\approx 3.0$; (b) $L = \\frac{\\mu_0 N^2 S}{b + \\frac{\\pi d}{\\mu}} \\approx 0.15\\text{ H}$",
        "solution": "**(a) Ratio of Magnetic Energies:**\nNeglecting fringing, the magnetic induction $B$ is uniform throughout both the magnetic core and the air gap.\nThe volume energy densities are:\n$$w_{\\text{gap}} = \\frac{B^2}{2\\mu_0}, \\quad w_m = \\frac{B^2}{2\\mu_0 \\mu}$$\nThe respective volumes are $V_{\\text{gap}} = S b$ and $V_m = S l_m \\approx S \\pi d$.\nThe ratio of energies stored in the gap and the magnetic is:\n$$\\frac{W_{\\text{gap}}}{W_m} = \\frac{w_{\\text{gap}} V_{\\text{gap}}}{w_m V_m} = \\frac{\\frac{B^2}{2\\mu_0} S b}{\\frac{B^2}{2\\mu_0 \\mu} S \\pi d} = \\frac{\\mu b}{\\pi d}$$\nEvaluating numerically:\n$$\\frac{W_{\\text{gap}}}{W_m} = \\frac{(1400)(2.0 \\times 10^{-3}\\text{ m})}{\\pi (0.30\\text{ m})} = \\frac{2.80}{0.9425} \\approx 2.97 \\approx 3.0$$\n\n**(b) Inductance of the System:**\nBy Ampère's circuital law along the mean circumference:\n$$H_m l_m + H_{\\text{gap}} b = N I \\implies \\frac{B}{\\mu_0 \\mu} \\pi d + \\frac{B}{\\mu_0} b = N I$$\n$$B = \\frac{\\mu_0 N I}{b + \\frac{\\pi d}{\\mu}}$$\nThe total flux linkage is $\\Psi = N \\Phi = N B S$:\n$$\\Psi = \\frac{\\mu_0 N^2 S I}{b + \\frac{\\pi d}{\\mu}}$$\nThus the inductance is:\n$$L = \\frac{\\Psi}{I} = \\frac{\\mu_0 N^2 S}{b + \\frac{\\pi d}{\\mu}}$$\nEvaluating numerically:\n$$b + \\frac{\\pi d}{\\mu} = 0.0020 + \\frac{0.9425}{1400} = 0.0020 + 0.000673 = 0.002673\\text{ m}$$\n$$L = \\frac{(4\\pi \\times 10^{-7})(800)^2(5.0 \\times 10^{-4})}{0.002673} = \\frac{4.021 \\times 10^{-4}}{2.673 \\times 10^{-3}} \\approx 0.15\\text{ H}$$",
        "tags": ["magnetic circuit", "air gap", "inductance", "energy ratio"]
    },
    {
        "id": "3.339",
        "title": "Magnetic Energy per Unit Length of Rotating Charged Cylinder",
        "difficulty": 2,
        "question": "A long cylinder of radius $a$ carrying a uniform surface charge rotates about its axis with an angular velocity $\\omega$. Find the magnetic field energy per unit length of the cylinder if the linear charge density equals $\\lambda$ and $\\mu = 1$.",
        "hints": [
            "The surface charge density is $\\sigma = \\frac{\\lambda}{2\\pi a}$.",
            "The rotation creates a surface current density $j = \\sigma v = \\sigma (\\omega a) = \\frac{\\lambda \\omega}{2\\pi}$.",
            "Inside the cylinder, the magnetic field is uniform: $B = \\mu_0 j = \\frac{\\mu_0 \\lambda \\omega}{2\\pi}$, and outside $B = 0$. Integrate $W_1 = \\frac{B^2}{2\\mu_0} (\\pi a^2)$."
        ],
        "answer": "$W_1 = \\frac{\\mu_0 \\lambda^2 \\omega^2 a^2}{8\\pi}$",
        "solution": "**1. Surface Current Density:**\nThe charge per unit length is $\\lambda$, distributed uniformly over the cylindrical surface of radius $a$, so:\n$$\\sigma = \\frac{\\lambda}{2\\pi a}$$\nAs the cylinder rotates with angular velocity $\\omega$, the linear velocity of the surface is $v = \\omega a$.\nThe resulting azimuthal surface current density is:\n$$j = \\sigma v = \\left( \\frac{\\lambda}{2\\pi a} \\right) (\\omega a) = \\frac{\\lambda \\omega}{2\\pi}$$\n\n**2. Magnetic Field Inside and Outside:**\nBy analogy with an ideal solenoid, the magnetic field outside the long cylinder is zero, while inside it is uniform and axially directed:\n$$B = \\mu_0 j = \\frac{\\mu_0 \\lambda \\omega}{2\\pi}$$\n\n**3. Magnetic Energy per Unit Length:**\nThe volume of a section of length $1\\text{ m}$ inside the cylinder is $V_1 = \\pi a^2$.\nThe magnetic energy stored per unit length is:\n$$W_1 = \\frac{B^2}{2\\mu_0} V_1 = \\frac{1}{2\\mu_0} \\left( \\frac{\\mu_0 \\lambda \\omega}{2\\pi} \\right)^2 (\\pi a^2) = \\frac{\\mu_0 \\lambda^2 \\omega^2 a^2}{8\\pi}$$",
        "tags": ["rotating cylinder", "magnetic energy per unit length", "surface current", "solenoid analogy"]
    },
    {
        "id": "3.340",
        "title": "Electric Field with Same Energy Density as 1 T Magnetic Field",
        "difficulty": 1,
        "question": "At what magnitude of the electric field strength in vacuum is the volume energy density of this field the same as that of a magnetic field with induction $B = 1.0\\text{ T}$ (also in vacuum)?",
        "hints": [
            "The electric field energy density is $w_e = \\frac{1}{2}\\varepsilon_0 E^2$.",
            "The magnetic field energy density is $w_m = \\frac{B^2}{2\\mu_0}$.",
            "Equate $w_e = w_m$ to find $E = \\frac{B}{\\sqrt{\\varepsilon_0 \\mu_0}} = c B$."
        ],
        "answer": "$E = \\frac{B}{\\sqrt{\\varepsilon_0 \\mu_0}} = c B = 3.0 \\times 10^8\\text{ V/m}$",
        "solution": "**1. Energy Density Equality:**\nThe volume energy densities of electric and magnetic fields in vacuum are:\n$$w_e = \\frac{1}{2} \\varepsilon_0 E^2, \\quad w_m = \\frac{B^2}{2\\mu_0}$$\nEquating $w_e = w_m$:\n$$\\frac{1}{2} \\varepsilon_0 E^2 = \\frac{B^2}{2\\mu_0} \\implies E^2 = \\frac{B^2}{\\varepsilon_0 \\mu_0}$$\nSince the speed of light in vacuum is $c = \\frac{1}{\\sqrt{\\varepsilon_0 \\mu_0}}$:\n$$E = \\frac{B}{\\sqrt{\\varepsilon_0 \\mu_0}} = c B$$\n\n**2. Numerical Evaluation:**\nGiven $B = 1.0\\text{ T}$ and $c = 3.0 \\times 10^8\\text{ m/s}$:\n$$E = (3.0 \\times 10^8\\text{ m/s})(1.0\\text{ T}) = 3.0 \\times 10^8\\text{ V/m}$$",
        "tags": ["energy density", "electric vs magnetic", "speed of light", "electromagnetism"]
    },
    {
        "id": "3.341",
        "title": "Ratio of Magnetic to Electric Energy Densities on Axis of Rotating Ring",
        "difficulty": 2,
        "question": "A thin uniformly charged ring of radius $a = 10\\text{ cm}$ rotates about its axis with an angular velocity $\\omega = 100\\text{ rad/s}$. Find the ratio of volume energy densities of the magnetic and electric fields on the axis of the ring at a point removed from its centre by a distance $l = a$.",
        "hints": [
            "For total charge $q$, the electric field on the axis at $l = a$ is $E = \\frac{q a}{4\\pi \\varepsilon_0 (2a^2)^{3/2}}$.",
            "The rotation constitutes a loop current $I = \\frac{q \\omega}{2\\pi}$, producing magnetic field $B = \\frac{\\mu_0 I a^2}{2(2a^2)^{3/2}}$.",
            "Calculate $\\frac{w_m}{w_e} = \\frac{B^2 / (2\\mu_0)}{\\frac{1}{2}\\varepsilon_0 E^2} = \\frac{1}{\\varepsilon_0 \\mu_0} \\left( \\frac{B}{E} \\right)^2 = \\varepsilon_0 \\mu_0 \\omega^2 a^2 = \\left(\\frac{\\omega a}{c}\\right)^2$."
        ],
        "answer": "$\\frac{w_m}{w_e} = \\varepsilon_0 \\mu_0 \\omega^2 a^2 = \\left( \\frac{\\omega a}{c} \\right)^2 = 1.1 \\times 10^{-15}$",
        "solution": "**1. Electric Field on Axis:**\nLet the total charge on the ring be $q$.\nAt an axial distance $l = a$, the electric field is:\n$$E = \\frac{1}{4\\pi \\varepsilon_0} \\frac{q l}{(a^2 + l^2)^{3/2}} = \\frac{q a}{4\\pi \\varepsilon_0 (2a^2)^{3/2}} = \\frac{q}{4\\pi \\varepsilon_0 2\\sqrt{2} a^2}$$\n\n**2. Magnetic Field on Axis:**\nThe rotating ring constitutes an electric current:\n$$I = \\frac{q}{T} = \\frac{q \\omega}{2\\pi}$$\nThe on-axis magnetic field at distance $l = a$ is:\n$$B = \\frac{\\mu_0 I a^2}{2(a^2 + l^2)^{3/2}} = \\frac{\\mu_0 (\\frac{q\\omega}{2\\pi}) a^2}{2(2a^2)^{3/2}} = \\frac{\\mu_0 q \\omega}{4\\pi 2\\sqrt{2} a}$$\n\n**3. Ratio of Energy Densities:**\n$$w_m = \\frac{B^2}{2\\mu_0}, \\quad w_e = \\frac{1}{2} \\varepsilon_0 E^2$$\n$$\\frac{w_m}{w_e} = \\frac{B^2}{\\mu_0 \\varepsilon_0 E^2} = \\frac{1}{\\varepsilon_0 \\mu_0} \\left( \\frac{B}{E} \\right)^2$$\nNotice the ratio of $B$ to $E$:\n$$\\frac{B}{E} = \\frac{\\frac{\\mu_0 q \\omega}{4\\pi 2\\sqrt{2} a}}{\\frac{q}{4\\pi \\varepsilon_0 2\\sqrt{2} a^2}} = \\mu_0 \\varepsilon_0 \\omega a$$\nSubstituting into the energy density ratio:\n$$\\frac{w_m}{w_e} = \\frac{1}{\\varepsilon_0 \\mu_0} (\\mu_0 \\varepsilon_0 \\omega a)^2 = \\varepsilon_0 \\mu_0 \\omega^2 a^2 = \\left( \\frac{\\omega a}{c} \\right)^2$$\n\n**4. Numerical Evaluation:**\nGiven $a = 0.10\\text{ m}$, $\\omega = 100\\text{ rad/s}$, $c = 3.0 \\times 10^8\\text{ m/s}$:\n$$\\frac{w_m}{w_e} = \\left( \\frac{100 \\times 0.10}{3.0 \\times 10^8} \\right)^2 = \\left( \\frac{10}{3.0 \\times 10^8} \\right)^2 = \\left( \\frac{1}{3} \\times 10^{-7} \\right)^2 \\approx 1.1 \\times 10^{-15}$$",
        "tags": ["rotating charged ring", "energy density ratio", "electromagnetic fields", "relativistic factor"]
    },
    {
        "id": "3.342",
        "title": "Work of Magnetization per Unit Volume",
        "difficulty": 2,
        "question": "Using the expression for the volume density of magnetic energy, demonstrate that the amount of work contributed to the magnetization of a unit volume of a para- or diamagnetic material is equal to $A = -\\frac{1}{2} J B$.",
        "hints": [
            "The volume density of magnetic energy is $w = \\frac{1}{2} \\mathbf{B} \\cdot \\mathbf{H}$.",
            "Express the magnetic field strength in terms of magnetization: $\\mathbf{H} = \\frac{\\mathbf{B}}{\\mu_0} - \\mathbf{J}$.",
            "Substitute $\\mathbf{H}$ into $w$ to separate the vacuum field energy from the magnetization contribution: $w = \\frac{B^2}{2\\mu_0} - \\frac{1}{2} J B$."
        ],
        "answer": "$A = -\\frac{1}{2} J B$",
        "solution": "**1. Volume Density of Total Magnetic Energy:**\nIn a linear magnetic medium (para- or diamagnetic), the volume density of magnetic energy is:\n$$w = \\frac{1}{2} \\mathbf{B} \\cdot \\mathbf{H}$$\n\n**2. Relation to Magnetization:**\nThe magnetic field intensity $\\mathbf{H}$ is related to induction $\\mathbf{B}$ and magnetization $\\mathbf{J}$ by:\n$$\\mathbf{H} = \\frac{\\mathbf{B}}{\\mu_0} - \\mathbf{J}$$\nSubstituting this into the energy density expression:\n$$w = \\frac{1}{2} \\mathbf{B} \\cdot \\left( \\frac{\\mathbf{B}}{\\mu_0} - \\mathbf{J} \\right) = \\frac{B^2}{2\\mu_0} - \\frac{1}{2} \\mathbf{J} \\cdot \\mathbf{B}$$\n\n**3. Physical Interpretation of Terms:**\n- The first term $w_0 = \\frac{B^2}{2\\mu_0}$ represents the energy density required to establish the magnetic induction $\\mathbf{B}$ in empty space (vacuum).\n- The difference $A = w - w_0 = -\\frac{1}{2} \\mathbf{J} \\cdot \\mathbf{B} = -\\frac{1}{2} J B$ represents the work done in magnetizing the substance per unit volume.",
        "tags": ["magnetization work", "energy density", "paramagnetic", "diamagnetic"]
    },
    {
        "id": "3.343",
        "title": "Inductance of Series and Parallel Connected Coils",
        "difficulty": 1,
        "question": "Two identical coils, each of inductance $L$, are interconnected:\n(a) in series;\n(b) in parallel.\nAssuming the mutual inductance between the coils to be negligible, find the total inductance of the system in both cases.",
        "hints": [
            "In series, total emf is the sum of individual emfs: $\\mathcal{E} = -(L_1 + L_2)\\frac{dI}{dt}$.",
            "In parallel, voltage across both is identical and currents sum: $I = I_1 + I_2$, leading to $\\frac{1}{L_{\\text{total}}} = \\frac{1}{L_1} + \\frac{1}{L_2}$.",
            "Substitute $L_1 = L_2 = L$."
        ],
        "answer": "(a) $L_{\\text{total}} = 2L$; (b) $L_{\\text{total}} = \\frac{L}{2}$",
        "solution": "**(a) Series Connection:**\nWhen two uncoupled coils of inductance $L_1 = L$ and $L_2 = L$ are connected in series, the same current $I$ flows through both.\nThe total induced electromotive force is the sum of individual emfs:\n$$\\mathcal{E} = \\mathcal{E}_1 + \\mathcal{E}_2 = -L \\frac{dI}{dt} - L \\frac{dI}{dt} = -2L \\frac{dI}{dt}$$\nBy definition of equivalent inductance $\\mathcal{E} = -L_{\\text{total}} \\frac{dI}{dt}$, we have:\n$$L_{\\text{total}} = 2L$$\n\n**(b) Parallel Connection:**\nWhen connected in parallel, the same potential difference $V$ appears across both coils:\n$$V = L \\frac{dI_1}{dt} = L \\frac{dI_2}{dt}$$\nThe total current delivered to the parallel combination is $I = I_1 + I_2$:\n$$\\frac{dI}{dt} = \\frac{dI_1}{dt} + \\frac{dI_2}{dt} = \\frac{V}{L} + \\frac{V}{L} = \\frac{2V}{L}$$\nComparing with $V = L_{\\text{total}} \\frac{dI}{dt}$:\n$$L_{\\text{total}} = \\frac{L}{2}$$",
        "tags": ["equivalent inductance", "series inductors", "parallel inductors", "circuit rules"]
    },
    {
        "id": "3.344",
        "title": "Mutual Inductance of Fully Coaxial Nested Solenoids",
        "difficulty": 2,
        "question": "Two solenoids of equal length and almost equal cross-sectional area are fully inserted into one another. Find their mutual inductance if their individual inductances are equal to $L_1$ and $L_2$.",
        "hints": [
            "Write the formula for solenoid inductances: $L_1 = \\mu_0 \\frac{N_1^2 S}{l}$ and $L_2 = \\mu_0 \\frac{N_2^2 S}{l}$.",
            "Because they share the exact same volume and cross-section, all magnetic flux produced by one links all turns of the other.",
            "The mutual inductance is $L_{12} = \\mu_0 \\frac{N_1 N_2 S}{l} = \\sqrt{L_1 L_2}$."
        ],
        "answer": "$L_{12} = \\sqrt{L_1 L_2}$",
        "solution": "**1. Inductances of the Individual Solenoids:**\nFor two solenoids of length $l$ and common cross-sectional area $S$ with turns $N_1$ and $N_2$:\n$$L_1 = \\mu_0 \\frac{N_1^2 S}{l}$$\n$$L_2 = \\mu_0 \\frac{N_2^2 S}{l}$$\n\n**2. Mutual Inductance Expression:**\nSince the solenoids are coextensive and nested with identical cross-section, the magnetic flux linkage with solenoid 2 produced by current $I_1$ in solenoid 1 is:\n$$\\Psi_{21} = N_2 B_1 S = N_2 \\left( \\mu_0 \\frac{N_1 I_1}{l} \\right) S = \\mu_0 \\frac{N_1 N_2 S}{l} I_1$$\nTherefore, the mutual inductance is:\n$$L_{12} = \\frac{\\Psi_{21}}{I_1} = \\mu_0 \\frac{N_1 N_2 S}{l}$$\n\n**3. Relation to Self-Inductances:**\nMultiplying $L_1$ and $L_2$:\n$$L_1 L_2 = \\left( \\mu_0 \\frac{N_1^2 S}{l} \\right) \\left( \\mu_0 \\frac{N_2^2 S}{l} \\right) = \\left( \\mu_0 \\frac{N_1 N_2 S}{l} \\right)^2 = L_{12}^2$$\n$$L_{12} = \\sqrt{L_1 L_2}$$\n(This corresponds to ideal unity coupling coefficient $k = 1$).",
        "tags": ["nested solenoids", "mutual inductance", "coupling coefficient", "unity coupling"]
    },
    {
        "id": "3.345",
        "title": "Magnetic Interaction Energy in Terms of Field Inductions",
        "difficulty": 2,
        "question": "Demonstrate that the magnetic energy of interaction of two current-carrying loops located in vacuum can be represented as $W_{12} = \\frac{1}{\\mu_0} \\int \\mathbf{B}_1 \\cdot \\mathbf{B}_2 \\, dV$, where $\\mathbf{B}_1$ and $\\mathbf{B}_2$ are the magnetic inductions within a volume element $dV$, produced individually by the currents of the first and second loops respectively.",
        "hints": [
            "The total magnetic field at any point in space is $\\mathbf{B} = \\mathbf{B}_1 + \\mathbf{B}_2$ by the principle of superposition.",
            "Write the total magnetic energy: $W = \\frac{1}{2\\mu_0} \\int B^2 \\, dV = \\frac{1}{2\\mu_0} \\int (\\mathbf{B}_1 + \\mathbf{B}_2)^2 \\, dV$.",
            "Expand the integrand to identify self-energies $W_1$ and $W_2$, leaving the cross-term as the mutual interaction energy."
        ],
        "answer": "$W_{12} = \\frac{1}{\\mu_0} \\int \\mathbf{B}_1 \\cdot \\mathbf{B}_2 \\, dV$",
        "solution": "**1. Superposition of Magnetic Fields:**\nIn vacuum, the total magnetic induction at any point in space is the vector sum of fields produced by loop 1 and loop 2:\n$$\\mathbf{B} = \\mathbf{B}_1 + \\mathbf{B}_2$$\n\n**2. Total Magnetic Field Energy:**\nThe total energy of the magnetic field over all space is:\n$$W = \\frac{1}{2\\mu_0} \\int \\mathbf{B}^2 \\, dV = \\frac{1}{2\\mu_0} \\int (\\mathbf{B}_1 + \\mathbf{B}_2)^2 \\, dV$$\nExpanding the squared magnitude:\n$$W = \\frac{1}{2\\mu_0} \\int B_1^2 \\, dV + \\frac{1}{2\\mu_0} \\int B_2^2 \\, dV + \\frac{1}{\\mu_0} \\int \\mathbf{B}_1 \\cdot \\mathbf{B}_2 \\, dV$$\n\n**3. Identification of Interaction Energy:**\n- The first term $W_1 = \\frac{1}{2\\mu_0} \\int B_1^2 \\, dV = \\frac{1}{2} L_1 I_1^2$ is the intrinsic self-energy of loop 1.\n- The second term $W_2 = \\frac{1}{2\\mu_0} \\int B_2^2 \\, dV = \\frac{1}{2} L_2 I_2^2$ is the intrinsic self-energy of loop 2.\n- The cross-term represents the interaction energy between the two current-carrying loops:\n$$W_{12} = \\frac{1}{\\mu_0} \\int \\mathbf{B}_1 \\cdot \\mathbf{B}_2 \\, dV = L_{12} I_1 I_2$$",
        "tags": ["interaction energy", "field energy integral", "superposition", "mutual inductance"]
    },
    {
        "id": "3.346",
        "title": "Interaction Energy of Two Concentric Inclined Circular Loops",
        "difficulty": 2,
        "question": "Find the interaction energy of two loops carrying currents $I_1$ and $I_2$ if both loops are shaped as circles of radii $a$ and $b$, with $a \\ll b$. The loop centres are located at the same point and their planes form an angle $\\theta$ between them.",
        "hints": [
            "Treat the small inner loop of radius $a$ as a magnetic dipole with moment $\\mathbf{p}_{m1} = I_1 (\\pi a^2) \\hat{\\mathbf{n}}_1$.",
            "The larger loop of radius $b$ produces a uniform magnetic field at its centre: $\\mathbf{B}_2 = \\frac{\\mu_0 I_2}{2b} \\hat{\\mathbf{n}}_2$.",
            "The interaction energy is $W_{12} = -\\mathbf{p}_{m1} \\cdot \\mathbf{B}_2$ or $W_{12} = L_{12} I_1 I_2 = \\frac{\\mu_0 \\pi a^2}{2b} I_1 I_2 \\cos\\theta$."
        ],
        "answer": "$W_{12} = \\frac{\\mu_0 \\pi a^2}{2b} I_1 I_2 \\cos\\theta$",
        "solution": "**1. Magnetic Dipole Representation:**\nBecause $a \\ll b$, the inner loop of radius $a$ can be treated as a point magnetic dipole at the centre of the outer loop.\nIts magnetic dipole moment is:\n$$\\mathbf{p}_{m1} = I_1 (\\pi a^2) \\hat{\\mathbf{n}}_1$$\n\n**2. Magnetic Field of the Outer Loop:**\nThe outer loop of radius $b$ produces a magnetic field at the centre:\n$$\\mathbf{B}_2 = \\frac{\\mu_0 I_2}{2b} \\hat{\\mathbf{n}}_2$$\nwhere $\\hat{\\mathbf{n}}_2$ is the unit normal to the plane of the outer loop.\n\n**3. Mutual Inductance and Interaction Energy:**\nThe angle between normal vectors $\\hat{\\mathbf{n}}_1$ and $\\hat{\\mathbf{n}}_2$ is $\\theta$.\nThe magnetic flux through loop 1 due to current $I_2$ in loop 2 is:\n$$\\Phi_{12} = \\mathbf{B}_2 \\cdot (\\pi a^2 \\hat{\\mathbf{n}}_1) = \\left( \\frac{\\mu_0 I_2}{2b} \\right) (\\pi a^2) \\cos\\theta$$\nThe mutual inductance is:\n$$L_{12} = \\frac{\\Phi_{12}}{I_2} = \\frac{\\mu_0 \\pi a^2}{2b} \\cos\\theta$$\nThe interaction energy of the two current loops is:\n$$W_{12} = L_{12} I_1 I_2 = \\frac{\\mu_0 \\pi a^2}{2b} I_1 I_2 \\cos\\theta$$",
        "tags": ["magnetic interaction energy", "dipole in magnetic field", "inclined loops", "mutual inductance"]
    },
    {
        "id": "3.347",
        "title": "Displacement Current in Poorly Conducting Medium Between Spheres",
        "difficulty": 2,
        "question": "The space between two concentric metallic spheres is filled with a uniform poorly conducting medium of resistivity $\\rho$ and permittivity $\\varepsilon$. At $t = 0$ the inside sphere obtains a certain charge. Find:\n(a) the relation between the vectors of displacement current density $\\mathbf{j}_d$ and conduction current density $\\mathbf{j}$ at an arbitrary point of the medium;\n(b) the displacement current across an arbitrary closed surface enclosing the internal sphere, if at the given moment the charge of that sphere is $q$.",
        "hints": [
            "Conduction current density is $\\mathbf{j} = \\frac{1}{\\rho}\\mathbf{E}$.",
            "Displacement current density is $\\mathbf{j}_d = \\frac{\\partial \\mathbf{D}}{\\partial t} = \\varepsilon_0 \\varepsilon \\frac{\\partial \\mathbf{E}}{\\partial t}$.",
            "Charge relaxation follows $\\nabla \\cdot \\mathbf{j} = -\\frac{\\partial \\rho_{\\text{free}}}{\\partial t} \\implies \\frac{\\partial \\mathbf{E}}{\\partial t} = -\\frac{1}{\\varepsilon_0 \\varepsilon \\rho}\\mathbf{E}$, giving $\\mathbf{j}_d = -\\mathbf{j}$."
        ],
        "answer": "(a) $\\mathbf{j}_d = -\\mathbf{j}$; (b) $I_d = -\\frac{q}{\\varepsilon_0 \\varepsilon \\rho}$",
        "solution": "**(a) Relation Between Current Densities:**\nIn the conducting medium, Ohm's law relates conduction current density to electric field:\n$$\\mathbf{j} = \\sigma \\mathbf{E} = \\frac{1}{\\rho} \\mathbf{E}$$\nThe displacement current density is defined as:\n$$\\mathbf{j}_d = \\frac{\\partial \\mathbf{D}}{\\partial t} = \\varepsilon_0 \\varepsilon \\frac{\\partial \\mathbf{E}}{\\partial t}$$\nFrom the continuity equation for charge and Gauss's law:\n$$\\nabla \\cdot \\mathbf{j} + \\frac{\\partial \\rho_{\\text{free}}}{\\partial t} = 0 \\implies \\frac{1}{\\rho} \\nabla \\cdot \\mathbf{E} + \\frac{\\partial}{\\partial t} (\\varepsilon_0 \\varepsilon \\nabla \\cdot \\mathbf{E}) = 0$$\n$$\\frac{\\partial \\mathbf{E}}{\\partial t} = -\\frac{1}{\\varepsilon_0 \\varepsilon \\rho} \\mathbf{E}$$\nSubstituting into $\\mathbf{j}_d$:\n$$\\mathbf{j}_d = \\varepsilon_0 \\varepsilon \\left( -\\frac{1}{\\varepsilon_0 \\varepsilon \\rho} \\mathbf{E} \\right) = -\\frac{1}{\\rho} \\mathbf{E} = -\\mathbf{j}$$\n\n**(b) Total Displacement Current:**\nThe total displacement current across any closed surface $S$ enclosing the inner sphere is:\n$$I_d = \\oint_S \\mathbf{j}_d \\cdot d\\mathbf{S} = -\\oint_S \\mathbf{j} \\cdot d\\mathbf{S} = -I_{\\text{cond}}$$\nBy Gauss's law, the electric flux through $S$ is $\\oint_S \\mathbf{E} \\cdot d\\mathbf{S} = \\frac{q}{\\varepsilon_0 \\varepsilon}$.\nTherefore the conduction current is:\n$$I_{\\text{cond}} = \\frac{1}{\\rho} \\oint_S \\mathbf{E} \\cdot d\\mathbf{S} = \\frac{q}{\\varepsilon_0 \\varepsilon \\rho}$$\nHence the displacement current is:\n$$I_d = -I_{\\text{cond}} = -\\frac{q}{\\varepsilon_0 \\varepsilon \\rho}$$",
        "tags": ["displacement current", "Maxwell-Ampere law", "charge relaxation", "concentric spheres"]
    },
    {
        "id": "3.348",
        "title": "Absence of Magnetic Field in Discharging Parallel-Plate Capacitor",
        "difficulty": 2,
        "question": "A parallel-plate capacitor is formed by two discs with a uniform poorly conducting medium between them. The capacitor was initially charged and then disconnected from a voltage source. Neglecting edge effects, show that there is no magnetic field between the capacitor plates.",
        "hints": [
            "Apply the Maxwell-Ampère circuital law: $\\oint \\mathbf{B} \\cdot d\\mathbf{r} = \\mu_0 \\int (\\mathbf{j} + \\mathbf{j}_d) \\cdot d\\mathbf{S}$.",
            "Recall from problem 3.347 that in a uniform conducting medium undergoing free discharge, $\\mathbf{j}_d = -\\mathbf{j}$.",
            "The total current density vanishes everywhere inside the dielectric gap: $\\mathbf{j}_{\\text{total}} = \\mathbf{j} + \\mathbf{j}_d = 0$, implying $\\mathbf{B} = 0$."
        ],
        "answer": "The magnetic field is identically zero because the displacement current density cancels the conduction current density everywhere ($\\mathbf{j} + \\mathbf{j}_d = 0$)",
        "solution": "**1. Maxwell-Ampère Law:**\nThe magnetic field in the region between the capacitor plates is governed by the fourth Maxwell equation:\n$$\\oint \\mathbf{B} \\cdot d\\mathbf{r} = \\mu_0 \\int_S (\\mathbf{j} + \\mathbf{j}_d) \\cdot d\\mathbf{S}$$\nwhere $\\mathbf{j}$ is the conduction current density and $\\mathbf{j}_d = \\frac{\\partial \\mathbf{D}}{\\partial t}$ is the displacement current density.\n\n**2. Current Density Cancellation:**\nDuring discharge after disconnection, the electric field between the plates decays exponentially with the relaxation time $\\tau = \\varepsilon_0 \\varepsilon \\rho$:\n$$E(t) = E_0 e^{-t/\\tau}$$\nThe conduction current density is:\n$$\\mathbf{j} = \\sigma \\mathbf{E} = \\frac{1}{\\rho} \\mathbf{E}$$\nThe displacement current density is:\n$$\\mathbf{j}_d = \\varepsilon_0 \\varepsilon \\frac{\\partial \\mathbf{E}}{\\partial t} = \\varepsilon_0 \\varepsilon \\left( -\\frac{1}{\\varepsilon_0 \\varepsilon \\rho} \\mathbf{E} \\right) = -\\frac{1}{\\rho} \\mathbf{E} = -\\mathbf{j}$$\n\n**3. Resulting Magnetic Field:**\nThe net effective current density driving the magnetic field is:\n$$\\mathbf{j}_{\\text{total}} = \\mathbf{j} + \\mathbf{j}_d = \\mathbf{j} - \\mathbf{j} = 0$$\nBy axial symmetry, around any circular loop of radius $r$ centered on the capacitor axis:\n$$B(r) \\cdot 2\\pi r = \\mu_0 \\int_0^r (\\mathbf{j} + \\mathbf{j}_d) \\cdot d\\mathbf{S} = 0 \\implies B(r) = 0$$\nThus, there is no magnetic field between the plates.",
        "tags": ["displacement current", "capacitor discharge", "Maxwell-Ampere law", "zero magnetic field"]
    },
    {
        "id": "3.349",
        "title": "Electric Field Amplitude in AC Air Capacitor",
        "difficulty": 2,
        "question": "A parallel-plate air condenser whose plates each have an area $S = 100\\text{ cm}^2$ is connected in series to an AC circuit. Find the electric field strength amplitude in the capacitor if the sinusoidal current amplitude in the lead wires is $I_m = 1.0\\text{ mA}$ and the angular frequency is $\\omega = 1.6 \\times 10^7\\text{ s}^{-1}$.",
        "hints": [
            "The current in the lead wires equals the total displacement current through the capacitor dielectric: $I(t) = I_d(t) = \\varepsilon_0 S \\frac{dE}{dt}$.",
            "For a sinusoidal electric field $E(t) = E_m \\sin(\\omega t)$, the displacement current amplitude is $I_m = \\varepsilon_0 S \\omega E_m$.",
            "Solve for $E_m = \\frac{I_m}{\\varepsilon_0 \\omega S}$."
        ],
        "answer": "$E_m = \\frac{I_m}{\\varepsilon_0 \\omega S} \\approx 7.0\\text{ V/cm}$",
        "solution": "**1. Displacement Current and Electric Field:**\nIn an air capacitor ($\\varepsilon = 1$), there is no conduction current between the plates.\nBy the continuity of total current, the current in the connecting wires equals the displacement current in the gap:\n$$I(t) = \\int_S \\mathbf{j}_d \\cdot d\\mathbf{S} = \\varepsilon_0 S \\frac{dE}{dt}$$\n\n**2. Amplitude Relation:**\nAssuming a harmonic time dependence $E(t) = E_m \\sin(\\omega t)$:\n$$\\frac{dE}{dt} = \\omega E_m \\cos(\\omega t)$$\nThe amplitude of the displacement current is:\n$$I_m = \\varepsilon_0 S \\omega E_m$$\nSolving for the electric field amplitude:\n$$E_m = \\frac{I_m}{\\varepsilon_0 \\omega S}$$\n\n**3. Numerical Evaluation:**\nGiven $I_m = 1.0\\text{ mA} = 1.0 \\times 10^{-3}\\text{ A}$, $\\omega = 1.6 \\times 10^7\\text{ s}^{-1}$, $S = 100\\text{ cm}^2 = 0.010\\text{ m}^2$, $\\varepsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}$:\n$$E_m = \\frac{1.0 \\times 10^{-3}}{(8.854 \\times 10^{-12})(1.6 \\times 10^7)(0.010)} = \\frac{1.0 \\times 10^{-3}}{1.417 \\times 10^{-6}} \\approx 706\\text{ V/m} \\approx 7.0\\text{ V/cm}$$",
        "tags": ["displacement current", "AC capacitor", "electric field amplitude", "Maxwell equations"]
    },
    {
        "id": "3.350",
        "title": "Magnetic Field Between Capacitor Plates with Lossy Dielectric",
        "difficulty": 3,
        "question": "The space between the electrodes of a parallel-plate capacitor is filled with a uniform poorly conducting medium of conductivity $\\sigma$ and permittivity $\\varepsilon$. The capacitor plates are circular discs separated by a distance $d$. Neglecting edge effects, find the magnetic field strength $H(r, t)$ between the plates at distance $r$ from their axis if an AC voltage $V(t) = V_m \\cos(\\omega t)$ is applied.",
        "hints": [
            "The electric field between the plates is $E(t) = \\frac{V_m}{d} \\cos(\\omega t)$.",
            "The total current density is the sum of conduction and displacement current densities: $j_{\\text{total}} = \\sigma E + \\varepsilon_0 \\varepsilon \\frac{\\partial E}{\\partial t} = \\frac{V_m}{d}[\\sigma \\cos(\\omega t) - \\varepsilon_0 \\varepsilon \\omega \\sin(\\omega t)]$.",
            "Apply Ampère's circuital law around a circle of radius $r$: $H(r) \\cdot 2\\pi r = j_{\\text{total}} \\cdot \\pi r^2 \\implies H = \\frac{1}{2} r j_{\\text{total}} = H_m \\cos(\\omega t + \\alpha)$."
        ],
        "answer": "$H(r, t) = H_m \\cos(\\omega t + \\alpha)$, where $H_m = \\frac{r V_m}{2d} \\sqrt{\\sigma^2 + (\\varepsilon_0 \\varepsilon \\omega)^2}$ and $\\tan\\alpha = \\frac{\\varepsilon_0 \\varepsilon \\omega}{\\sigma}$",
        "solution": "**1. Conduction and Displacement Current Densities:**\nThe electric field between the plates is:\n$$E(t) = \\frac{V(t)}{d} = \\frac{V_m}{d} \\cos(\\omega t)$$\nThe conduction current density is:\n$$j_c(t) = \\sigma E(t) = \\frac{\\sigma V_m}{d} \\cos(\\omega t)$$\nThe displacement current density is:\n$$j_d(t) = \\varepsilon_0 \\varepsilon \\frac{\\partial E}{\\partial t} = -\\frac{\\varepsilon_0 \\varepsilon \\omega V_m}{d} \\sin(\\omega t)$$\n\n**2. Total Current Density:**\nThe total current density is:\n$$j_{\\text{total}}(t) = j_c(t) + j_d(t) = \\frac{V_m}{d} \\left[ \\sigma \\cos(\\omega t) - \\varepsilon_0 \\varepsilon \\omega \\sin(\\omega t) \\right]$$\nCombining into a single harmonic function:\n$$j_{\\text{total}}(t) = j_m \\cos(\\omega t + \\alpha)$$\nwhere:\n$$j_m = \\frac{V_m}{d} \\sqrt{\\sigma^2 + (\\varepsilon_0 \\varepsilon \\omega)^2}, \\quad \\tan\\alpha = \\frac{\\varepsilon_0 \\varepsilon \\omega}{\\sigma}$$\n\n**3. Magnetic Field from Maxwell-Ampère Law:**\nApplying Ampère's law around a circular contour of radius $r$ centered on the capacitor axis:\n$$\\oint \\mathbf{H} \\cdot d\\mathbf{r} = H(r, t) \\cdot (2\\pi r) = j_{\\text{total}}(t) \\cdot (\\pi r^2)$$\n$$H(r, t) = \\frac{1}{2} r j_{\\text{total}}(t) = H_m \\cos(\\omega t + \\alpha)$$\nwhere the amplitude of the magnetic field strength is:\n$$H_m = \\frac{1}{2} r j_m = \\frac{r V_m}{2d} \\sqrt{\\sigma^2 + (\\varepsilon_0 \\varepsilon \\omega)^2}$$",
        "tags": ["Maxwell-Ampere law", "lossy dielectric", "displacement current", "magnetic field in capacitor"]
    }
]
