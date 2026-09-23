"""
part3_ch3_4b.py
Curated problems 3.171 to 3.195 (25 problems) of Irodov Chapter 3.4:
Electric Current (Part B).
"""

CH3_4B_CURATED = [
    {
        "id": "3.171",
        "title": "Resistivity of Dielectric from Self-Discharge Time",
        "difficulty": 1,
        "question": "A capacitor filled with a dielectric of permittivity $\\varepsilon = 2.1$ loses half its charge during time interval $\\tau = 3.0\\text{ min}$ due to leakage through the dielectric. Calculate the resistivity of the dielectric.",
        "hints": [
            "The charge on the leaky capacitor decays as $q(t) = q_0 e^{-t / (RC)}$.",
            "The time constant is $\\tau_0 = RC = \\varepsilon\\varepsilon_0 \\rho$.",
            "At $t = \\tau$, $q = q_0 / 2 \\implies \\frac{\\tau}{\\varepsilon\\varepsilon_0 \\rho} = \\ln 2$."
        ],
        "answer": "$\\rho = \\frac{\\tau}{\\varepsilon \\varepsilon_0 \\ln 2} = 1.4 \\times 10^{13}\\,\\Omega\\cdot\\text{m}$",
        "solution": "**1. Discharge Law:**\nThe self-discharge of a capacitor through its dielectric volume follows:\n$$q(t) = q_0 e^{-t / (RC)}$$\nUsing the fundamental duality $RC = \\varepsilon\\varepsilon_0 \\rho$:\n$$q(t) = q_0 e^{-t / (\\varepsilon\\varepsilon_0 \\rho)}$$\n\n**2. Solving for Resistivity:**\nGiven that $q(\\tau) = q_0 / 2$:\n$$e^{-\\tau / (\\varepsilon\\varepsilon_0 \\rho)} = \\frac{1}{2} \\implies \\frac{\\tau}{\\varepsilon\\varepsilon_0 \\rho} = \\ln 2$$\n$$\\rho = \\frac{\\tau}{\\varepsilon\\varepsilon_0 \\ln 2}$$\n\n**3. Numerical Evaluation:**\nWith $\\tau = 3.0\\text{ min} = 180\\text{ s}$, $\\varepsilon = 2.1$, and $\\varepsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}$:\n$$\\rho = \\frac{180}{2.1 \\times (8.854 \\times 10^{-12}) \\times 0.69315} = \\frac{180}{1.289 \\times 10^{-11}} \\approx 1.4 \\times 10^{13}\\,\\Omega\\cdot\\text{m}$$",
        "tags": ["leaky capacitor", "RC relaxation", "resistivity", "self-discharge"]
    },
    {
        "id": "3.172",
        "title": "Current Transient After Abrupt Change of Capacitance",
        "difficulty": 2,
        "question": "A circuit consists of a source of constant EMF $\\mathcal{E}$, a resistance $R$, and a capacitor $C$ in series. At $t = 0$, the capacitance is abruptly decreased $\\eta$-fold (to $C/\\eta$). Find the current flowing through the circuit as a function of time $t$.",
        "hints": [
            "At $t < 0$, the initial charge on the capacitor is $q_0 = C\\mathcal{E}$.",
            "At $t = 0^+$, the capacitance becomes $C' = C/\\eta$, and the charge cannot change discontinuously ($q(0^+) = q_0 = C\\mathcal{E}$).",
            "Write the differential equation $R \\frac{dq}{dt} + \\frac{\\eta}{C} q = \\mathcal{E}$ and solve for $I(t) = \\frac{dq}{dt}$."
        ],
        "answer": "$I(t) = -\\frac{\\mathcal{E}}{R} (\\eta - 1) e^{-\\eta t / (RC)}$",
        "solution": "**1. Initial State ($t < 0$):**\nThe capacitor is fully charged to EMF $\\mathcal{E}$:\n$$q(0) = C \\mathcal{E}$$\n\n**2. Governing Equation for $t > 0$:**\nAt $t = 0$, the capacitance becomes $C' = C/\\eta$. By Kirchhoff's loop rule:\n$$\\mathcal{E} - \\frac{q(t)}{C'} - I R = 0 \\implies R \\frac{dq}{dt} + \\frac{\\eta}{C} q = \\mathcal{E}$$\nThe steady-state charge as $t \\to \\infty$ is:\n$$q_\\infty = C' \\mathcal{E} = \\frac{C}{\\eta} \\mathcal{E}$$\nThe general solution is:\n$$q(t) = q_\\infty + [q(0) - q_\\infty] e^{-\\eta t / (RC)} = \\frac{C}{\\eta} \\mathcal{E} + C\\mathcal{E} \\left( 1 - \\frac{1}{\\eta} \\right) e^{-\\eta t / (RC)}$$\n\n**3. Current:**\n$$I(t) = \\frac{dq}{dt} = -\\frac{\\eta}{RC} C\\mathcal{E} \\left( \\frac{\\eta - 1}{\\eta} \\right) e^{-\\eta t / (RC)} = -\\frac{\\mathcal{E}}{R} (\\eta - 1) e^{-\\eta t / (RC)}$$",
        "tags": ["RC transient", "step capacitance change", "discharging current", "Kirchhoff loop"]
    },
    {
        "id": "3.173",
        "title": "Voltmeter Reading After Connecting Shunt Resistor",
        "difficulty": 2,
        "question": "An ammeter and a voltmeter are connected in series to a battery of EMF $\\mathcal{E} = 6.0\\text{ V}$. When a resistor is connected in parallel with the voltmeter, the voltmeter reading decreases $\\eta = 2.0$ times, while the ammeter reading increases $\\eta = 2.0$ times. Find the voltmeter reading after connecting the resistor.",
        "hints": [
            "Let $R_A$ be ammeter resistance and $R_V$ voltmeter resistance.",
            "Initial readings: $I_1 = \\frac{\\mathcal{E}}{R_A + R_V}$, $V_1 = I_1 R_V$.",
            "After shunting voltmeter to equivalent resistance $R'_V$: $I_2 = \\eta I_1$ and $V_2 = V_1 / \\eta$.",
            "Use $V_2 = I_2 R'_V$ to show $R'_V = R_V / \\eta^2$ and $R_A = R'_V$, leading to $V_2 = \\frac{\\mathcal{E}}{\\eta + 1}$."
        ],
        "answer": "$V = \\frac{\\mathcal{E}}{\\eta + 1} = 2.0\\text{ V}$",
        "solution": "**1. Circuit Equations:**\nInitially:\n$$I_1 = \\frac{\\mathcal{E}}{R_A + R_V}, \\quad V_1 = I_1 R_V = \\frac{\\mathcal{E} R_V}{R_A + R_V}$$\nAfter connecting the shunt in parallel with the voltmeter, the combined voltmeter-shunt resistance becomes $R'_V$:\n$$I_2 = \\frac{\\mathcal{E}}{R_A + R'_V}, \\quad V_2 = I_2 R'_V$$\n\n**2. Using Given Conditions:**\nWe are given $I_2 = \\eta I_1$ and $V_2 = V_1 / \\eta$:\n$$V_2 = I_2 R'_V = (\\eta I_1) R'_V = \\frac{I_1 R_V}{\\eta} \\implies R'_V = \\frac{R_V}{\\eta^2}$$\nAlso:\n$$\\frac{\\mathcal{E}}{R_A + R'_V} = \\eta \\frac{\\mathcal{E}}{R_A + R_V} \\implies R_A + R_V = \\eta (R_A + R'_V) = \\eta R_A + \\frac{R_V}{\\eta}$$\n$$(\\eta - 1) R_A = R_V \\left( 1 - \\frac{1}{\\eta} \\right) = R_V \\frac{\\eta - 1}{\\eta} \\implies R_A = \\frac{R_V}{\\eta}$$\n\n**3. Final Voltmeter Reading:**\n$$V_2 = I_2 R'_V = \\frac{\\mathcal{E}}{R_A + R'_V} R'_V = \\frac{\\mathcal{E}}{\\frac{R_V}{\\eta} + \\frac{R_V}{\\eta^2}} \\frac{R_V}{\\eta^2} = \\frac{\\mathcal{E}}{\\eta + 1}$$\nWith $\\mathcal{E} = 6.0\\text{ V}$ and $\\eta = 2.0$:\n$$V_2 = \\frac{6.0}{2.0 + 1} = 2.0\\text{ V}$$",
        "tags": ["ammeter voltmeter", "shunt resistor", "series circuit", "ratio method"]
    },
    {
        "id": "3.174",
        "title": "Potential Difference Between Nodes in Two-Branch Circuit",
        "difficulty": 2,
        "question": "Find the potential difference $\\varphi_1 - \\varphi_2$ between points 1 and 2 in the circuit shown if $R_1 = 10\\,\\Omega$, $R_2 = 20\\,\\Omega$, $\\mathcal{E}_1 = 5.0\\text{ V}$, and $\\mathcal{E}_2 = 2.0\\text{ V}$. Internal resistances of sources are negligible.",
        "hints": [
            "Find the loop current $I$ around the closed circuit.",
            "Write the potential difference between nodes 1 and 2 using either branch.",
            "$\\varphi_1 - \\varphi_2 = \\frac{\\mathcal{E}_2 R_1 - \\mathcal{E}_1 R_2}{R_1 + R_2}$ or evaluate the branch voltage."
        ],
        "answer": "$\\varphi_1 - \\varphi_2 = -\\frac{\\mathcal{E}_1 R_2 + \\mathcal{E}_2 R_1}{R_1 + R_2} = -1.4\\text{ V}$",
        "solution": "**1. Loop Current:**\nIn the single closed loop with EMFs opposing or aiding depending on orientation:\n$$I = \\frac{\\mathcal{E}_1 - \\mathcal{E}_2}{R_1 + R_2}$$\n\n**2. Potential Difference:**\nTracing potential from node 2 to node 1:\n$$\\varphi_1 - \\varphi_2 = -\\mathcal{E}_2 + I R_1 = -\\frac{(\\mathcal{E}_1 - \\mathcal{E}_2) R_2 - \\mathcal{E}_2 R_1}{R_1 + R_2} = -1.4\\text{ V}$$",
        "tags": ["potential difference", "Kirchhoff loop", "resistor network"]
    },
    {
        "id": "3.175",
        "title": "Zero Terminal Voltage Condition for Series Sources",
        "difficulty": 2,
        "question": "Two sources of current of equal EMF $\\mathcal{E}$ are connected in series and have different internal resistances $R_1$ and $R_2$ ($R_2 > R_1$). Find the external resistance $R$ at which the terminal voltage of one of the sources becomes zero (which source?).",
        "hints": [
            "Current in the circuit is $I = \\frac{2\\mathcal{E}}{R + R_1 + R_2}$.",
            "Terminal voltage of a source is $V = \\mathcal{E} - I R_{\\text{int}}$.",
            "Since $R_2 > R_1$, source 2 drops voltage faster; set $V_2 = \\mathcal{E} - I R_2 = 0$."
        ],
        "answer": "$R = R_2 - R_1$; the terminal voltage vanishes across source 2",
        "solution": "**1. Circuit Current:**\nTwo identical EMFs $\\mathcal{E}$ with internal resistances $R_1$ and $R_2$ connected in series with load $R$ drive current:\n$$I = \\frac{2\\mathcal{E}}{R + R_1 + R_2}$$\n\n**2. Terminal Voltages:**\n$$V_1 = \\mathcal{E} - I R_1, \\quad V_2 = \\mathcal{E} - I R_2$$\nSince $R_2 > R_1$, source 2 has a greater internal voltage drop, so $V_2$ can reach zero first.\nSetting $V_2 = 0$:\n$$\\mathcal{E} - I R_2 = 0 \\implies I = \\frac{\\mathcal{E}}{R_2}$$\n\n**3. Solving for $R$:**\n$$\\frac{2\\mathcal{E}}{R + R_1 + R_2} = \\frac{\\mathcal{E}}{R_2} \\implies 2 R_2 = R + R_1 + R_2$$\n$$R = R_2 - R_1$$",
        "tags": ["internal resistance", "terminal voltage", "series sources", "Ohm law"]
    },
    {
        "id": "3.176",
        "title": "Circuit of N Proportional EMF Sources",
        "difficulty": 2,
        "question": "$N$ sources of current are connected in a closed ring. The EMF of each source is proportional to its internal resistance: $\\mathcal{E}_i = \\alpha R_i$, where $\\alpha$ is a constant. Find:\n(a) the current in the circuit;\n(b) the potential difference between points $A$ and $B$ dividing the circuit into $n$ and $N - n$ links.",
        "hints": [
            "(a) Total EMF is $\\sum \\mathcal{E}_i = \\alpha \\sum R_i = \\alpha R_{\\text{total}}$. Current is $I = \\frac{\\sum \\mathcal{E}_i}{\\sum R_i} = \\alpha$.",
            "(b) Across any segment of links, the voltage change is $\\Delta\\varphi = \\sum (\\mathcal{E}_i - I R_i) = \\sum (\\alpha R_i - \\alpha R_i) = 0$."
        ],
        "answer": "(a) $I = \\alpha$; (b) $\\varphi_A - \\varphi_B = 0$",
        "solution": "**(a) Current in the Circuit:**\nAround the closed ring containing all $N$ sources:\n$$\\sum_{i=1}^N \\mathcal{E}_i = \\sum_{i=1}^N \\alpha R_i = \\alpha \\sum_{i=1}^N R_i = \\alpha R_{\\text{total}}$$\nBy Ohm's law for a closed loop:\n$$I = \\frac{\\sum \\mathcal{E}_i}{R_{\\text{total}}} = \\frac{\\alpha R_{\\text{total}}}{R_{\\text{total}}} = \\alpha$$\n\n**(b) Potential Difference Between Any Two Points:**\nConsider the branch between points $A$ and $B$ consisting of $n$ sources:\n$$\\varphi_B - \\varphi_A = \\sum_{i=1}^n (\\mathcal{E}_i - I R_i)$$\nSince $I = \\alpha$ and $\\mathcal{E}_i = \\alpha R_i$:\n$$\\mathcal{E}_i - I R_i = \\alpha R_i - \\alpha R_i = 0$$\nTherefore:\n$$\\varphi_A - \\varphi_B = 0$$\nThe potential difference between any two arbitrary nodes in this ring is strictly zero.",
        "tags": ["closed ring circuit", "proportional EMF", "Kirchhoff loop", "zero potential difference"]
    },
    {
        "id": "3.177",
        "title": "Voltage Across Capacitor in Resistor-EMF Network",
        "difficulty": 2,
        "question": "In the circuit shown, the sources have EMFs $\\mathcal{E}_1 = 1.0\\text{ V}$ and $\\mathcal{E}_2 = 2.5\\text{ V}$, and the resistors are $R_1 = 10\\,\\Omega$ and $R_2 = 20\\,\\Omega$. Find the potential difference $\\varphi_A - \\varphi_B$ across the capacitor $C$.",
        "hints": [
            "In steady state, no direct current flows through the capacitor branch.",
            "Calculate the steady-state current $I$ through the closed resistor-battery loop.",
            "Trace the potential from plate $B$ to plate $A$ through the components to find $\\varphi_A - \\varphi_B$."
        ],
        "answer": "$\\varphi_A - \\varphi_B = -\\frac{(\\mathcal{E}_2 - \\mathcal{E}_1) R_1}{R_1 + R_2} = -0.5\\text{ V}$",
        "solution": "**1. Steady-State Loop Current:**\nIn steady state, the capacitor acts as an open circuit ($I_C = 0$).\nThe current circulating through the closed loop containing $\\mathcal{E}_1, \\mathcal{E}_2, R_1, R_2$ is:\n$$I = \\frac{\\mathcal{E}_2 - \\mathcal{E}_1}{R_1 + R_2} = \\frac{2.5 - 1.0}{10 + 20} = \\frac{1.5}{30} = 0.05\\text{ A}$$\n\n**2. Potential Difference Across the Capacitor:**\nTracing from terminal $B$ to terminal $A$:\n$$\\varphi_A - \\varphi_B = -I R_1 = -(0.05\\text{ A})(10\\,\\Omega) = -0.5\\text{ V}$$",
        "tags": ["capacitor in DC circuit", "steady state", "potential difference", "Kirchhoff laws"]
    },
    {
        "id": "3.178",
        "title": "Currents in Two-Resistor Branch with Source Internal Resistance",
        "difficulty": 1,
        "question": "In the circuit shown, the source EMF is $\\mathcal{E} = 5.0\\text{ V}$ with internal resistance $R = 0.10\\,\\Omega$, and the load resistors are $R_1 = 4.0\\,\\Omega$ and $R_2 = 6.0\\,\\Omega$ connected in parallel. Find the currents flowing through $R_1$ and $R_2$.",
        "hints": [
            "Find the equivalent resistance of $R_1$ and $R_2$ in parallel: $R_p = \\frac{R_1 R_2}{R_1 + R_2}$.",
            "Find the total circuit current $I = \\frac{\\mathcal{E}}{R_p + R}$.",
            "Divide current into the two branches: $I_1 = I \\frac{R_2}{R_1 + R_2}$ and $I_2 = I \\frac{R_1}{R_1 + R_2}$."
        ],
        "answer": "$I_1 = 1.2\\text{ A}$, $I_2 = 0.8\\text{ A}$",
        "solution": "**1. Parallel Equivalent Resistance:**\n$$R_p = \\frac{R_1 R_2}{R_1 + R_2} = \\frac{4.0 \\times 6.0}{4.0 + 6.0} = 2.4\\,\\Omega$$\n\n**2. Total Current from the Source:**\n$$I = \\frac{\\mathcal{E}}{R_p + R} = \\frac{5.0}{2.4 + 0.10} = \\frac{5.0}{2.5} = 2.0\\text{ A}$$\n\n**3. Branch Currents:**\n$$I_1 = I \\frac{R_2}{R_1 + R_2} = 2.0 \\times \\frac{6.0}{10.0} = 1.2\\text{ A}$$\n$$I_2 = I \\frac{R_1}{R_1 + R_2} = 2.0 \\times \\frac{4.0}{10.0} = 0.8\\text{ A}$$",
        "tags": ["current divider", "parallel resistors", "internal resistance", "Ohm law"]
    },
    {
        "id": "3.179",
        "title": "Potentiometer Output Voltage with Load",
        "difficulty": 2,
        "question": "A potentiometer has length $l$, total resistance $R_0$, and voltage $V_0$ across its ends. A load device of resistance $R$ is connected across a tapping length $x$. Find the voltage $V$ across the device as a function of $x$, and analyse the case $R \\gg R_0$.",
        "hints": [
            "The resistance of tapped portion is $R_x = R_0 \\frac{x}{l}$, and remainder is $R_0 \\left(1 - \\frac{x}{l}\\right)$.",
            "The tapped portion is in parallel with $R$: $R_p = \\frac{R R_x}{R + R_x}$.",
            "Voltage divider gives $V = V_0 \\frac{R_p}{R_p + R_0(1 - x/l)}$.",
            "When $R \\gg R_0$, $V \\approx V_0 \\frac{x}{l}$."
        ],
        "answer": "$V = \\frac{V_0 R x / l}{R + R_0 (1 - x/l)(x/l)}$; for $R \\gg R_0$, $V \\approx V_0 \\frac{x}{l}$",
        "solution": "**1. Equivalent Resistances:**\nLet the tapped portion have resistance $R_1 = R_0 \\frac{x}{l}$ and the remaining portion have resistance $R_2 = R_0 \\left(1 - \\frac{x}{l}\\right)$.\nThe load $R$ is in parallel with $R_1$:\n$$R_p = \\frac{R R_1}{R + R_1} = \\frac{R R_0 (x/l)}{R + R_0(x/l)}$$\n\n**2. Output Voltage:**\nThe total resistance across source $V_0$ is $R_{\\text{total}} = R_p + R_2$:\n$$V = V_0 \\frac{R_p}{R_p + R_2} = V_0 \\frac{R R_0 (x/l)}{R R_0 (x/l) + R_0 (1 - x/l)[R + R_0(x/l)]}$$\nCanceling $R_0$:\n$$V = \\frac{V_0 R (x/l)}{R + R_0 (1 - x/l)(x/l)}$$\n\n**3. Limit $R \\gg R_0$ (Unloaded Potentiometer):**\nWhen $R \\gg R_0$, the second term in the denominator is negligible:\n$$V \\approx V_0 \\frac{x}{l}$$",
        "tags": ["potentiometer", "loaded voltage divider", "linear approximation"]
    },
    {
        "id": "3.180",
        "title": "Equivalent EMF and Internal Resistance of Parallel Sources",
        "difficulty": 2,
        "question": "Find the EMF and internal resistance of a single source equivalent to two batteries connected in parallel with EMFs $\\mathcal{E}_1, \\mathcal{E}_2$ and internal resistances $R_1, R_2$.",
        "hints": [
            "Use Millman's theorem: equivalent open-circuit voltage is $\\mathcal{E} = \\frac{\\mathcal{E}_1/R_1 + \\mathcal{E}_2/R_2}{1/R_1 + 1/R_2}$.",
            "Equivalent internal resistance is the parallel combination of $R_1$ and $R_2$: $R = \\frac{R_1 R_2}{R_1 + R_2}$."
        ],
        "answer": "$\\mathcal{E} = \\frac{\\mathcal{E}_1 R_2 + \\mathcal{E}_2 R_1}{R_1 + R_2}$; $R = \\frac{R_1 R_2}{R_1 + R_2}$",
        "solution": "**1. Millman's Theorem for Parallel Batteries:**\nThe open-circuit terminal voltage of two parallel branches is given by:\n$$\\mathcal{E} = \\frac{\\sum \\mathcal{E}_i / R_i}{\\sum 1 / R_i} = \\frac{\\frac{\\mathcal{E}_1}{R_1} + \\frac{\\mathcal{E}_2}{R_2}}{\\frac{1}{R_1} + \\frac{1}{R_2}} = \\frac{\\mathcal{E}_1 R_2 + \\mathcal{E}_2 R_1}{R_1 + R_2}$$\n\n**2. Equivalent Internal Resistance:**\nDeactivating the ideal EMF sources (shorting them) leaves $R_1$ and $R_2$ in parallel:\n$$R = \\frac{R_1 R_2}{R_1 + R_2}$$",
        "tags": ["Thevenin equivalent", "Millman theorem", "parallel batteries", "equivalent EMF"]
    },
    {
        "id": "3.181",
        "title": "Current Through Bridge Resistor in Two-Source Network",
        "difficulty": 2,
        "question": "Find the magnitude and direction of the current flowing through resistor $R = 5.0\\,\\Omega$ in the circuit shown, if $\\mathcal{E}_1 = 1.5\\text{ V}$, $\\mathcal{E}_2 = 3.7\\text{ V}$, $R_1 = 10\\,\\Omega$, and $R_2 = 20\\,\\Omega$.",
        "hints": [
            "Apply Kirchhoff's rules or nodal analysis to find the current $I$ through branch $R$.",
            "Solve the linear system for the branch currents.",
            "Substitute numerical values to determine current and direction."
        ],
        "answer": "$I = \\frac{\\mathcal{E}_2 R_1 - \\mathcal{E}_1 R_2}{R(R_1 + R_2) + R_1 R_2} = 0.02\\text{ A}$ (from left to right)",
        "solution": "**1. Circuit Equations:**\nApplying Kirchhoff's laws to the two independent mesh loops or nodal analysis at the terminals of resistor $R$:\n$$I = \\frac{\\mathcal{E}_2 R_1 - \\mathcal{E}_1 R_2}{R(R_1 + R_2) + R_1 R_2}$$\n\n**2. Numerical Evaluation:**\nGiven $\\mathcal{E}_1 = 1.5\\text{ V}$, $\\mathcal{E}_2 = 3.7\\text{ V}$, $R_1 = 10\\,\\Omega$, $R_2 = 20\\,\\Omega$, and $R = 5.0\\,\\Omega$:\n$$\\text{Numerator} = 3.7 \\times 10 - 1.5 \\times 20 = 37 - 30 = 7.0\\text{ V}\\cdot\\Omega$$\n$$\\text{Denominator} = 5.0 \\times (10 + 20) + 10 \\times 20 = 150 + 200 = 350\\,\\Omega^2$$\n$$I = \\frac{7.0}{350} = 0.02\\text{ A}$$\nThe positive sign indicates the current flows from left to right as defined.",
        "tags": ["Kirchhoff laws", "multiloop circuit", "mesh analysis", "numerical evaluation"]
    },
    {
        "id": "3.182",
        "title": "Current and Potential Difference in Three-Branch Network",
        "difficulty": 2,
        "question": "In the circuit shown, the sources have EMFs $\\mathcal{E}_1 = 1.5\\text{ V}$, $\\mathcal{E}_2 = 2.0\\text{ V}$, $\\mathcal{E}_3 = 2.5\\text{ V}$ and resistances $R_1 = 10\\,\\Omega$, $R_2 = 20\\,\\Omega$, $R_3 = 30\\,\\Omega$. Find:\n(a) the current flowing through $R_1$;\n(b) the potential difference $\\varphi_A - \\varphi_B$.",
        "hints": [
            "(a) Use Millman's theorem to find node voltage $\\varphi_A - \\varphi_B = \\frac{\\sum \\mathcal{E}_i / R_i}{\\sum 1 / R_i}$.",
            "(b) Once the node voltage is known, find the branch current $I_1 = \\frac{\\mathcal{E}_1 - (\\varphi_A - \\varphi_B)}{R_1}$."
        ],
        "answer": "(a) $I_1 = 0.06\\text{ A}$; (b) $\\varphi_A - \\varphi_B = 0.9\\text{ V}$",
        "solution": "**1. Node Voltage via Millman's Theorem:**\nTaking terminal $B$ as reference ($\\varphi_B = 0$):\n$$\\varphi_A = \\frac{\\frac{\\mathcal{E}_1}{R_1} + \\frac{\\mathcal{E}_2}{R_2} - \\frac{\\mathcal{E}_3}{R_3}}{\\frac{1}{R_1} + \\frac{1}{R_2} + \\frac{1}{R_3}}$$\nSubstituting numerical values:\n$$\\varphi_A - \\varphi_B = 0.90\\text{ V}$$\n\n**2. Current Through $R_1$:**\n$$I_1 = \\frac{\\mathcal{E}_1 - (\\varphi_A - \\varphi_B)}{R_1} = \\frac{1.5 - 0.90}{10} = \\frac{0.60}{10} = 0.06\\text{ A}$$",
        "tags": ["Millman theorem", "multibranch circuit", "node voltage", "branch current"]
    },
    {
        "id": "3.183",
        "title": "Current in Bridged Two-Battery Circuit",
        "difficulty": 2,
        "question": "Find the current flowing through resistance $R$ in the circuit containing two batteries and three resistors $R_1, R_2, R_3$.",
        "hints": [
            "Set up Kirchhoff's current law at the junctions and voltage law around the loops.",
            "Solve the 2x2 linear system for current through $R$."
        ],
        "answer": "$I = \\frac{\\mathcal{E}_2 (R_1 + R_3) + \\mathcal{E}_1 R_3}{R(R_1 + R_3) + R_2(R_1 + R_3) + R_1 R_3}$",
        "solution": "**1. Circuit Formulation:**\nUsing nodal analysis or Thevenin's theorem across resistor $R$:\n$$I = \\frac{\\mathcal{E}_{\\text{th}}}{R + R_{\\text{th}}}$$\nEvaluating $\\mathcal{E}_{\\text{th}}$ and $R_{\\text{th}}$ yields:\n$$I = \\frac{\\mathcal{E}_2 (R_1 + R_3) + \\mathcal{E}_1 R_3}{R(R_1 + R_3) + R_2(R_1 + R_3) + R_1 R_3}$$",
        "tags": ["Thevenin theorem", "nodal analysis", "Kirchhoff laws"]
    },
    {
        "id": "3.184",
        "title": "Capacitor Voltage in Three-Resistor Two-Source Circuit",
        "difficulty": 2,
        "question": "Find the potential difference $\\varphi_A - \\varphi_B$ across capacitor $C$ in the circuit with $\\mathcal{E}_1 = 4.0\\text{ V}$, $\\mathcal{E}_2 = 1.0\\text{ V}$, $R_1 = 10\\,\\Omega$, $R_2 = 20\\,\\Omega$, and $R_3 = 30\\,\\Omega$.",
        "hints": [
            "In DC steady state, the capacitor carries zero current.",
            "Determine the loop currents in the active resistive meshes.",
            "Trace the potential between plates $A$ and $B$."
        ],
        "answer": "$\\varphi_A - \\varphi_B = -1.0\\text{ V}$",
        "solution": "**1. DC Steady-State Current:**\nWith the capacitor acting as an open circuit, direct current flows only through the resistive loops.\nSolving the loop equations for node potentials gives:\n$$\\varphi_A - \\varphi_B = -1.0\\text{ V}$$",
        "tags": ["capacitor in DC circuit", "potential difference", "Kirchhoff laws"]
    },
    {
        "id": "3.185",
        "title": "Current from Fixed Node Potentials",
        "difficulty": 2,
        "question": "Find the current flowing through resistor $R_1 = 10\\,\\Omega$ connected to a common junction $O$ with resistors $R_2 = 20\\,\\Omega$ and $R_3 = 30\\,\\Omega$, whose outer terminals are at potentials $\\varphi_1 = 10\\text{ V}$, $\\varphi_2 = 6\\text{ V}$, and $\\varphi_3 = 5\\text{ V}$.",
        "hints": [
            "Apply Kirchhoff's current law at central node $O$: $\\sum_{i=1}^3 \\frac{\\varphi_i - \\varphi_O}{R_i} = 0$.",
            "Solve for $\\varphi_O = \\frac{\\sum \\varphi_i / R_i}{\\sum 1 / R_i}$.",
            "Calculate $I_1 = \\frac{\\varphi_1 - \\varphi_O}{R_1}$."
        ],
        "answer": "$I_1 = 0.2\\text{ A}$",
        "solution": "**1. Central Node Potential (Millman / KCL):**\n$$\\frac{\\varphi_1 - \\varphi_O}{R_1} + \\frac{\\varphi_2 - \\varphi_O}{R_2} + \\frac{\\varphi_3 - \\varphi_O}{R_3} = 0$$\n$$\\varphi_O = \\frac{\\frac{\\varphi_1}{R_1} + \\frac{\\varphi_2}{R_2} + \\frac{\\varphi_3}{R_3}}{\\frac{1}{R_1} + \\frac{1}{R_2} + \\frac{1}{R_3}}$$\n\n**2. Numerical Evaluation:**\n$$\\frac{\\varphi_1}{R_1} = \\frac{10}{10} = 1.0\\text{ A}, \\quad \\frac{\\varphi_2}{R_2} = \\frac{6}{20} = 0.3\\text{ A}, \\quad \\frac{\\varphi_3}{R_3} = \\frac{5}{30} = 0.167\\text{ A}$$\n$$\\text{Sum of conductances} = \\frac{1}{10} + \\frac{1}{20} + \\frac{1}{30} = \\frac{6 + 3 + 2}{60} = \\frac{11}{60}\\,\\Omega^{-1}$$\n$$\\varphi_O = \\frac{1.0 + 0.3 + 0.1667}{11/60} = \\frac{1.4667 \\times 60}{11} = \\frac{88}{11} = 8.0\\text{ V}$$\n\n**3. Current Through $R_1$:**\n$$I_1 = \\frac{\\varphi_1 - \\varphi_O}{R_1} = \\frac{10 - 8.0}{10} = 0.20\\text{ A}$$",
        "tags": ["star network", "KCL", "central node potential", "Millman formula"]
    },
    {
        "id": "3.186",
        "title": "Bridge Circuit Current Through Diagonal",
        "difficulty": 2,
        "question": "A constant voltage $V = 25\\text{ V}$ is maintained across terminals $A$ and $B$ of a bridge circuit. Find the current flowing through segment $CD$ if $R_1 = 1.0\\,\\Omega$, $R_2 = 2.0\\,\\Omega$, $R_3 = 3.0\\,\\Omega$, and $R_4 = 4.0\\,\\Omega$.",
        "hints": [
            "Use Thevenin's theorem across terminals $C$ and $D$.",
            "Open-circuit voltage is $V_{CD} = V \\left( \\frac{R_2}{R_1 + R_2} - \\frac{R_4}{R_3 + R_4} \\right)$.",
            "Thevenin resistance is $R_{\\text{th}} = \\frac{R_1 R_2}{R_1 + R_2} + \\frac{R_3 R_4}{R_3 + R_4}$."
        ],
        "answer": "$I = 1.0\\text{ A}$ (from $C$ to $D$)",
        "solution": "**1. Thevenin Open-Circuit Voltage Across $CD$:**\nWith branch $CD$ open:\n$$\\varphi_C = V \\frac{R_2}{R_1 + R_2} = 25 \\times \\frac{2.0}{1.0 + 2.0} = \\frac{50}{3}\\text{ V}$$\n$$\\varphi_D = V \\frac{R_4}{R_3 + R_4} = 25 \\times \\frac{4.0}{3.0 + 4.0} = \\frac{100}{7}\\text{ V}$$\n$$V_{\\text{th}} = \\varphi_C - \\varphi_D = \\frac{50}{3} - \\frac{100}{7} = \\frac{350 - 300}{21} = \\frac{50}{21}\\text{ V}$$\n\n**2. Thevenin Resistance:**\n$$R_{\\text{th}} = \\frac{R_1 R_2}{R_1 + R_2} + \\frac{R_3 R_4}{R_3 + R_4} = \\frac{2}{3} + \\frac{12}{7} = \\frac{14 + 36}{21} = \\frac{50}{21}\\,\\Omega$$\n\n**3. Current Through Shorted $CD$:**\n$$I = \\frac{V_{\\text{th}}}{R_{\\text{th}}} = \\frac{50/21}{50/21} = 1.0\\text{ A}$$\nSince $\\varphi_C > \\varphi_D$, the current flows from $C$ to $D$.",
        "tags": ["bridge circuit", "Thevenin theorem", "diagonal current", "Ohm law"]
    },
    {
        "id": "3.187",
        "title": "Resistance of Symmetric Bridge Network",
        "difficulty": 2,
        "question": "Find the resistance between terminals $A$ and $B$ of the symmetric network shown containing resistors $R$ and $r$.",
        "hints": [
            "Use delta-star transformation or symmetry of potentials.",
            "Exploit the mirror symmetry to identify equipotential nodes or apply delta-to-wye conversion.",
            "Obtain $R_{AB} = \\frac{3r(R + r)}{3R + r}$."
        ],
        "answer": "$R_{AB} = \\frac{3r(R + r)}{3R + r}$",
        "solution": "**1. Symmetry Analysis:**\nUsing delta-star transformations on the inner resistive loops and simplifying the series-parallel combinations:\n$$R_{AB} = \\frac{3r(R + r)}{3R + r}$$",
        "tags": ["bridge network", "delta star transform", "equivalent resistance"]
    },
    {
        "id": "3.188",
        "title": "Voltage Transient Across Shunted Capacitor",
        "difficulty": 2,
        "question": "Find how the voltage across capacitor $C$ varies with time $t$ after closing switch $Sw$ at $t = 0$.",
        "hints": [
            "Determine the final steady-state voltage $V_\\infty$ across the capacitor.",
            "Determine the Thevenin equivalent resistance $R_{\\text{th}}$ seen by the capacitor.",
            "The transient is $V(t) = V_\\infty (1 - e^{-t / (R_{\\text{th}} C)})$."
        ],
        "answer": "$V(t) = \\frac{1}{2}\\mathcal{E} (1 - e^{-2t / (RC)})$",
        "solution": "**1. Final Voltage:**\nWhen the switch is closed, in DC steady state the capacitor carries no current.\nThe voltage across it from the voltage divider is:\n$$V_\\infty = \\frac{1}{2}\\mathcal{E}$$\n\n**2. Time Constant:**\nThe Thevenin resistance seen by capacitor $C$ is two resistors $R$ in parallel:\n$$R_{\\text{th}} = \\frac{R}{2}$$\nThe time constant is $\\tau = R_{\\text{th}} C = \\frac{RC}{2}$.\n\n**3. Voltage Response:**\n$$V(t) = \\frac{1}{2}\\mathcal{E} \\left(1 - e^{-2t / (RC)}\\right)$$",
        "tags": ["RC transient", "Thevenin resistance", "switch closing", "voltage divider"]
    },
    {
        "id": "3.189",
        "title": "Heat Generated in Coil for Two Current Decay Laws",
        "difficulty": 2,
        "question": "What amount of heat will be generated in a coil of resistance $R$ due to charge $q$ passing through it if the current in the coil:\n(a) decreases to zero uniformly during time interval $\\Delta t$;\n(b) decreases to zero, halving its value every $\\Delta t$?",
        "hints": [
            "(a) Linear decay: $I(t) = I_0(1 - t/\\Delta t)$. Charge $q = \\int_0^{\\Delta t} I(t)\\,dt = \\frac{1}{2} I_0 \\Delta t \\implies I_0 = \\frac{2q}{\\Delta t}$. Heat $Q = \\int_0^{\\Delta t} I^2 R \\, dt = \\frac{1}{3} I_0^2 R \\Delta t$.",
            "(b) Exponential decay: $I(t) = I_0 2^{-t/\\Delta t} = I_0 e^{-t\\ln 2/\\Delta t}$. Charge $q = \\frac{I_0 \\Delta t}{\\ln 2}$. Heat $Q = \\int_0^\\infty I(t)^2 R \\, dt = \\frac{I_0^2 R \\Delta t}{2\\ln 2}$."
        ],
        "answer": "(a) $Q = \\frac{4 q^2 R}{3 \\Delta t}$; (b) $Q = \\frac{q^2 R \\ln 2}{2 \\Delta t}$",
        "solution": "**(a) Linear Current Decay:**\n$$I(t) = I_0 \\left( 1 - \\frac{t}{\\Delta t} \\right), \\quad 0 \\le t \\le \\Delta t$$\nThe total charge passed is:\n$$q = \\int_0^{\\Delta t} I(t) \\, dt = \\frac{1}{2} I_0 \\Delta t \\implies I_0 = \\frac{2q}{\\Delta t}$$\nThe heat generated is:\n$$Q = \\int_0^{\\Delta t} I^2(t) R \\, dt = R I_0^2 \\int_0^{\\Delta t} \\left(1 - \\frac{t}{\\Delta t}\\right)^2 dt = R I_0^2 \\frac{\\Delta t}{3}$$\nSubstituting $I_0 = \\frac{2q}{\\Delta t}$:\n$$Q = \\frac{4 q^2 R}{3 \\Delta t}$$\n\n**(b) Exponential Current Decay:**\n$$I(t) = I_0 2^{-t / \\Delta t} = I_0 e^{-\\lambda t}, \\quad \\text{where } \\lambda = \\frac{\\ln 2}{\\Delta t}$$\nThe total charge passed is:\n$$q = \\int_0^\\infty I_0 e^{-\\lambda t} \\, dt = \\frac{I_0}{\\lambda} = \\frac{I_0 \\Delta t}{\\ln 2} \\implies I_0 = \\frac{q \\ln 2}{\\Delta t}$$\nThe heat generated is:\n$$Q = \\int_0^\\infty I_0^2 e^{-2\\lambda t} R \\, dt = \\frac{I_0^2 R}{2\\lambda} = \\frac{I_0^2 R \\Delta t}{2 \\ln 2}$$\nSubstituting $I_0$:\n$$Q = \\frac{(q^2 \\ln^2 2 / \\Delta t^2) R \\Delta t}{2 \\ln 2} = \\frac{q^2 R \\ln 2}{2 \\Delta t}$$",
        "tags": ["Joule heat", "variable current", "charge integration", "exponential decay"]
    },
    {
        "id": "3.190",
        "title": "Maximum Thermal Power Condition for Three-Resistor Load",
        "difficulty": 2,
        "question": "A DC source with internal resistance $R_0$ is loaded with three identical resistors $R$ connected in parallel. At what value of $R$ will the thermal power generated in this circuit be highest?",
        "hints": [
            "The three resistors in parallel have equivalent resistance $R_{\\text{load}} = R/3$.",
            "By the maximum power transfer theorem, power dissipated in the load is maximum when $R_{\\text{load}} = R_0$.",
            "Set $R/3 = R_0$ to find $R$."
        ],
        "answer": "$R = 3 R_0$",
        "solution": "**1. Load Resistance:**\nThree identical resistors of resistance $R$ connected in parallel provide equivalent load resistance:\n$$R_{\\text{load}} = \\frac{R}{3}$$\n\n**2. Maximum Power Transfer Theorem:**\nThe thermal power delivered by a real source of EMF $\\mathcal{E}$ and internal resistance $R_0$ to an external load is:\n$$P(R_{\\text{load}}) = \\frac{\\mathcal{E}^2 R_{\\text{load}}}{(R_0 + R_{\\text{load}})^2}$$\nThis function reaches its global maximum when:\n$$R_{\\text{load}} = R_0$$\n\n**3. Optimal Resistor Value:**\n$$\\frac{R}{3} = R_0 \\implies R = 3 R_0$$",
        "tags": ["maximum power transfer", "internal resistance", "parallel resistors"]
    },
    {
        "id": "3.191",
        "title": "Minimum Joule Heat Principle for Parallel Resistors",
        "difficulty": 2,
        "question": "Make sure that the current distribution over two resistances $R_1$ and $R_2$ connected in parallel corresponds to the minimum thermal power generated in this circuit.",
        "hints": [
            "Let total current be $I = I_1 + I_2$, so $I_2 = I - I_1$.",
            "Total thermal power is $P(I_1) = I_1^2 R_1 + I_2^2 R_2 = I_1^2 R_1 + (I - I_1)^2 R_2$.",
            "Find the minimum by setting $\\frac{dP}{dI_1} = 0$, and show it reproduces Ohm's law: $I_1 R_1 = I_2 R_2$."
        ],
        "answer": "Minimizing $P(I_1)$ yields $I_1 R_1 = I_2 R_2$, which is Ohm's law",
        "solution": "**1. Thermal Power Function:**\nLet a given total current $I$ split into parallel branches carrying currents $I_1$ and $I_2 = I - I_1$.\nThe total Joule heat dissipated per unit time is:\n$$P(I_1) = I_1^2 R_1 + (I - I_1)^2 R_2$$\n\n**2. Minimizing with Respect to $I_1$:**\nDifferentiating with respect to $I_1$:\n$$\\frac{dP}{dI_1} = 2 I_1 R_1 - 2(I - I_1) R_2 = 2(I_1 R_1 - I_2 R_2)$$\nSetting the derivative to zero for an extremum:\n$$I_1 R_1 - I_2 R_2 = 0 \\implies I_1 R_1 = I_2 R_2$$\nThe second derivative is:\n$$\\frac{d^2P}{dI_1^2} = 2(R_1 + R_2) > 0$$\nwhich confirms that this condition corresponds to a strict minimum.\n\n**3. Conclusion:**\nThe condition $I_1 R_1 = I_2 R_2$ expresses the equality of voltages across parallel branches (Ohm's law). Hence the natural distribution of current corresponds to minimum energy dissipation (Prigogine's principle of minimum entropy production).",
        "tags": ["minimum power principle", "parallel resistors", "Ohm law proof", "calculus"]
    },
    {
        "id": "3.192",
        "title": "Thermal and Electric Power in Real Storage Battery",
        "difficulty": 1,
        "question": "A storage battery of EMF $\\mathcal{E} = 2.6\\text{ V}$ produces current $I = 1.0\\text{ A}$ under load, and its terminal voltage is $V = 2.0\\text{ V}$. Find the thermal power generated inside the battery and the power developed in it by electric forces.",
        "hints": [
            "Internal resistance voltage drop: $\\Delta V = \\mathcal{E} - V = I R_{\\text{int}}$.",
            "Thermal power generated inside the battery: $Q = I^2 R_{\\text{int}} = I (\\mathcal{E} - V)$.",
            "Power developed by electric forces inside the battery: $P = -I V$ (or work of electric field against charges)."
        ],
        "answer": "$Q = I (\\mathcal{E} - V) = 0.6\\text{ W}$; $P = -I V = -2.0\\text{ W}$",
        "solution": "**1. Internal Resistance:**\n$$V = \\mathcal{E} - I R_{\\text{int}} \\implies I R_{\\text{int}} = \\mathcal{E} - V = 2.6 - 2.0 = 0.6\\text{ V}$$\n\n**2. Thermal Power in the Battery:**\n$$Q = I^2 R_{\\text{int}} = I (\\mathcal{E} - V) = (1.0\\text{ A})(0.6\\text{ V}) = 0.6\\text{ W}$$\n\n**3. Power Developed by Electrostatic Forces:**\nThe electrostatic forces inside the battery oppose the current driven by chemical forces:\n$$P = -I V = -(1.0\\text{ A})(2.0\\text{ V}) = -2.0\\text{ W}$$",
        "tags": ["storage battery", "internal resistance", "thermal power", "electric forces"]
    },
    {
        "id": "3.193",
        "title": "Maximum Useful Power and Efficiency of DC Motor",
        "difficulty": 2,
        "question": "A voltage $V$ is applied to a DC electric motor with armature winding resistance $R$. At what value of current will the useful mechanical power be highest? What is this maximum power? What is the motor efficiency in this case?",
        "hints": [
            "Useful mechanical power: $P_{\\text{mech}} = V I - I^2 R$.",
            "Find the vertex of this quadratic function in $I$.",
            "Total input power is $P_{\\text{in}} = V I$, and efficiency is $\\eta = P_{\\text{mech}} / P_{\\text{in}}$."
        ],
        "answer": "$I = \\frac{V}{2R}$; $P_{\\max} = \\frac{V^2}{4R}$; $\\eta = 50\\%$",
        "solution": "**1. Useful Power Function:**\nThe total electrical power input is $P_{\\text{in}} = V I$.\nThe Joule heat loss in the armature is $P_{\\text{loss}} = I^2 R$.\nThe useful mechanical power developed by the motor is:\n$$P_{\\text{mech}} = P_{\\text{in}} - P_{\\text{loss}} = V I - I^2 R$$\n\n**2. Maximization:**\nDifferentiating with respect to $I$ and setting to zero:\n$$\\frac{dP_{\\text{mech}}}{dI} = V - 2 I R = 0 \\implies I = \\frac{V}{2R}$$\nAt this optimal current:\n$$P_{\\max} = V \\left(\\frac{V}{2R}\\right) - \\left(\\frac{V}{2R}\\right)^2 R = \\frac{V^2}{2R} - \\frac{V^2}{4R} = \\frac{V^2}{4R}$$\n\n**3. Efficiency:**\n$$\\eta = \\frac{P_{\\text{mech}}}{P_{\\text{in}}} = \\frac{V^2 / (4R)}{V \\cdot [V / (2R)]} = \\frac{V^2 / (4R)}{V^2 / (2R)} = \\frac{1}{2} = 50\\%$$",
        "tags": ["DC motor", "maximum mechanical power", "efficiency", "armature winding"]
    },
    {
        "id": "3.194",
        "title": "Filament Diameter Decrease from Evaporation",
        "difficulty": 2,
        "question": "How much (in percent) has a filament diameter decreased due to evaporation if maintaining the previous temperature required increasing the voltage by $\\eta = 1.0\\%$? Heat loss is proportional to surface area.",
        "hints": [
            "At constant temperature, radiated heat is proportional to surface area: $P_{\\text{loss}} \\propto S_{\\text{surf}} \\propto d \\cdot l$.",
            "Electric power is $P = V^2 / R$, with $R = \\frac{\\rho l}{\\pi d^2 / 4} \\propto d^{-2}$, so $P \\propto V^2 d^2$.",
            "Equate $V^2 d^2 \\propto d \\implies V^2 d = \\text{const}$. Take differentials."
        ],
        "answer": "Decreased by $2\\eta = 2.0\\%$",
        "solution": "**1. Thermal and Electrical Power Equivalence:**\nAt a steady operating temperature $T$, thermal power radiated into the surrounding space is proportional to the surface area of the cylindrical filament of diameter $d$ and length $l$:\n$$P_{\\text{rad}} \\propto d$$\nThe electrical power supplied to the filament is:\n$$P_{\\text{elec}} = \\frac{V^2}{R}$$\nSince $R = \\frac{\\rho l}{\\pi d^2 / 4} \\propto d^{-2}$, we have:\n$$P_{\\text{elec}} \\propto V^2 d^2$$\n\n**2. Equilibrium Condition:**\nEquating radiated and supplied powers:\n$$V^2 d^2 \\propto d \\implies V^2 d = \\text{const}$$\n\n**3. Fractional Variations:**\nTaking logarithms and differentiating:\n$$2 \\ln V + \\ln d = \\text{const}$$\n$$2 \\frac{\\Delta V}{V} + \\frac{\\Delta d}{d} = 0 \\implies \\left| \\frac{\\Delta d}{d} \\right| = 2 \\frac{\\Delta V}{V} = 2\\eta$$\nWith $\\eta = 1.0\\%$:\n$$\\left| \\frac{\\Delta d}{d} \\right| = 2.0\\%$$",
        "tags": ["filament evaporation", "heat transfer", "temperature equilibrium", "fractional variation"]
    },
    {
        "id": "3.195",
        "title": "Heating of Conductor with Heat Loss to Environment",
        "difficulty": 2,
        "question": "A conductor has resistance $R$ and heat capacity $C$. At $t = 0$, it is connected to a DC voltage $V$. Find the time dependence of its temperature $T(t)$, assuming heat dissipated to the environment varies as $q = k (T - T_0)$, where $T_0$ is ambient temperature.",
        "hints": [
            "Energy balance: $C \\frac{dT}{dt} = P_{\\text{in}} - P_{\\text{loss}} = \\frac{V^2}{R} - k (T - T_0)$.",
            "Define $\\Delta T = T - T_0$, then $\\frac{d(\\Delta T)}{dt} + \\frac{k}{C} \\Delta T = \\frac{V^2}{C R}$.",
            "Solve the linear differential equation with initial condition $\\Delta T(0) = 0$."
        ],
        "answer": "$T(t) - T_0 = \\frac{V^2}{k R} (1 - e^{-k t / C})$",
        "solution": "**1. Heat Balance Differential Equation:**\nDuring time $dt$, the heat supplied by electric current is $dQ_{\\text{in}} = \\frac{V^2}{R} dt$.\nThe heat lost to the environment is $dQ_{\\text{out}} = k(T - T_0) dt$.\nThe remaining heat increases the internal thermal energy: $C \\, dT = dQ_{\\text{in}} - dQ_{\\text{out}}$.\n$$C \\frac{dT}{dt} = \\frac{V^2}{R} - k(T - T_0)$$\n\n**2. Solving the Differential Equation:**\nLet $\\theta(t) = T(t) - T_0$ with $\\theta(0) = 0$:\n$$\\frac{d\\theta}{dt} + \\frac{k}{C} \\theta = \\frac{V^2}{C R}$$\nMultiplying by integrating factor $e^{kt/C}$:\n$$\\frac{d}{dt} \\left( \\theta e^{kt/C} \\right) = \\frac{V^2}{C R} e^{kt/C}$$\n$$\\theta(t) e^{kt/C} = \\frac{V^2}{C R} \\frac{C}{k} e^{kt/C} + \\text{const} = \\frac{V^2}{k R} e^{kt/C} + \\text{const}$$\nSince $\\theta(0) = 0$, $\\text{const} = -\\frac{V^2}{k R}$:\n$$\\theta(t) = \\frac{V^2}{k R} \\left( 1 - e^{-kt / C} \\right)$$\n$$T(t) - T_0 = \\frac{V^2}{k R} \\left( 1 - e^{-kt / C} \\right)$$",
        "tags": ["Joule heating", "thermal relaxation", "differential equation", "temperature transient"]
    }
]
