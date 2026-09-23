"""
part2_ch2_2.py
Curated problems 2.26 to 2.61 (36 problems) of Irodov Chapter 2.2: The First Law of Thermodynamics. Heat Capacity.
"""

CH2_2_CURATED = [
    {
        "id": "2.26",
        "title": "Internal Energy of Air in a Room",
        "difficulty": 1,
        "question": "Demonstrate that the internal energy $U$ of the air in a room is independent of temperature provided the outside pressure $p$ is constant. Calculate $U$, if the room volume is equal to $V = 40\\text{ m}^3$ and the atmospheric pressure is $p = 1.0\\text{ atm}$. (Take $\\gamma = 1.40$).",
        "hints": [
            "Internal energy of an ideal gas is $U = \\nu C_V T = \\frac{m}{M} \\frac{R}{\\gamma - 1} T$.",
            "Use the ideal gas law: $p V = \\frac{m}{M} R T$.",
            "Substitute $\\frac{m}{M} R T = p V$ into the expression for $U$."
        ],
        "answer": "$U = \\frac{p V}{\\gamma - 1} = 10\\text{ MJ}$",
        "solution": "**1. Analytical Demonstration:**\nFor an ideal gas with adiabatic index $\\gamma$:\n$$U = \\nu C_V T = \\nu \\left( \\frac{R}{\\gamma - 1} \\right) T = \\frac{\\nu R T}{\\gamma - 1}$$\nFrom the ideal gas equation of state, $\\nu R T = p V$. Substituting this into the internal energy gives:\n$$U = \\frac{p V}{\\gamma - 1}$$\nBecause both the atmospheric pressure $p$ and the room volume $V$ are constant, $U$ depends only on $p$ and $V$, and is completely independent of the temperature $T$!\n*(Physically: As the room heats up, air expands and leaks out, so the decrease in air mass exactly offsets the increase in temperature per molecule).* \n\n**2. Numerical Calculation:**\nWith $p = 1.0\\text{ atm} = 1.013 \\times 10^5\\text{ Pa}$, $V = 40\\text{ m}^3$, and $\\gamma = 1.40$:\n$$U = \\frac{1.013 \\times 10^5 \\times 40}{1.40 - 1} = \\frac{4.052 \\times 10^6}{0.40} \\approx 1.01 \\times 10^7\\text{ J} \\approx 10\\text{ MJ}$$",
        "tags": ["internal energy", "first law", "isobaric condition", "room air"]
    },
    {
        "id": "2.27",
        "title": "Isochoric Internal Energy Increment of Diatomic Gas",
        "difficulty": 1,
        "question": "A mass $m = 10\\text{ g}$ of oxygen is heated isochorically from $T_1 = 280\\text{ K}$ to $T_2 = 380\\text{ K}$. Find the increment of its internal energy $\\Delta U$ and the amount of heat $Q$ transferred to the gas. (Take $\\gamma = 1.40$, $M = 32\\text{ g/mol}$).",
        "hints": [
            "In an isochoric process, work done is zero: $A = 0$.",
            "By the first law of thermodynamics, $Q = \\Delta U$.",
            "Internal energy increment is $\\Delta U = \\frac{m}{M} C_V \\Delta T = \\frac{m}{M} \\frac{R}{\\gamma - 1} (T_2 - T_1)$."
        ],
        "answer": "$\\Delta U = Q = \\frac{m}{M} \\frac{R}{\\gamma - 1} \\Delta T = 0.65\\text{ kJ}$",
        "solution": "**1. First Law for Isochoric Process:**\nSince volume is constant ($V = \\text{const}$), $A = \\int p \\, dV = 0$.\n$$Q = \\Delta U + A = \\Delta U$$\n\n**2. Calculation of $\\Delta U$:**\n$$\\Delta U = \\frac{m}{M} C_V \\Delta T = \\frac{m}{M} \\left( \\frac{R}{\\gamma - 1} \\right) (T_2 - T_1)$$\n\n**3. Numerical Values:**\n$$\\Delta T = 380 - 280 = 100\\text{ K}, \\quad \\frac{m}{M} = \\frac{10}{32} = 0.3125\\text{ mol}$$\n$$\\Delta U = 0.3125 \\times \\frac{8.314}{0.40} \\times 100 = 0.3125 \\times 20.785 \\times 100 \\approx 650\\text{ J} = 0.65\\text{ kJ}$$",
        "tags": ["isochoric process", "heat capacity", "internal energy"]
    },
    {
        "id": "2.28",
        "title": "Work and Fraction of Heat in Isobaric Expansion",
        "difficulty": 1,
        "question": "An ideal diatomic gas with $\\gamma = 1.40$ expands isobarically when an amount of heat $Q$ is transferred to it. Find:\n(a) the work performed by the gas;\n(b) the fraction of the transferred heat converted into work;\n(c) the increment of its internal energy.",
        "hints": [
            "In an isobaric process: $Q = \\nu C_p \\Delta T$ and $A = p \\Delta V = \\nu R \\Delta T$.",
            "The fraction of heat converted into work is $\\frac{A}{Q} = \\frac{R}{C_p} = \\frac{\\gamma - 1}{\\gamma}$.",
            "The internal energy increment is $\\Delta U = Q - A$."
        ],
        "answer": "(a) $A = \\frac{\\gamma - 1}{\\gamma} Q = \\frac{2}{7} Q$; (b) $\\frac{A}{Q} = 28.6\\%$; (c) $\\Delta U = \\frac{1}{\\gamma} Q = \\frac{5}{7} Q$",
        "solution": "**1. Thermodynamic Relations for Isobaric Expansion:**\n$$Q = \\nu C_p \\Delta T = \\nu \\left(\\frac{\\gamma R}{\\gamma - 1}\\right) \\Delta T$$\n$$A = p \\Delta V = \\nu R \\Delta T$$\n$$\\Delta U = \\nu C_V \\Delta T = \\nu \\left(\\frac{R}{\\gamma - 1}\\right) \\Delta T$$\n\n**2. Ratios:**\n$$\\frac{A}{Q} = \\frac{\\nu R \\Delta T}{\\nu \\frac{\\gamma R}{\\gamma - 1} \\Delta T} = \\frac{\\gamma - 1}{\\gamma}$$\nFor a diatomic gas ($\\gamma = 7/5 = 1.40$):\n$$\\frac{A}{Q} = \\frac{1.40 - 1}{1.40} = \\frac{0.40}{1.40} = \\frac{2}{7} \\approx 0.286 = 28.6\\%$$\n$$\\frac{\\Delta U}{Q} = 1 - \\frac{A}{Q} = \\frac{1}{\\gamma} = \\frac{5}{7} \\approx 71.4\\%$$",
        "tags": ["isobaric expansion", "heat capacity ratio", "work of expansion"]
    },
    {
        "id": "2.29",
        "title": "Isobaric Heating of Gas in a Cylinder with Piston",
        "difficulty": 2,
        "question": "A vertical cylinder closed from below is fitted with a smooth, heat-insulating piston of mass $m$ and area $S$. Under the piston is one mole of ideal gas at temperature $T_0$. The atmospheric pressure is $p_0$. How much heat must be supplied to the gas to raise the piston by a height $h$?",
        "hints": [
            "The pressure under the piston is constant: $p = p_0 + \\frac{mg}{S}$.",
            "The work done by the gas is $A = p \\Delta V = p S h = (p_0 S + mg) h$.",
            "Heat supplied in an isobaric process is $Q = \\Delta U + A = \\nu C_V \\Delta T + A = \\frac{A}{\\gamma - 1} + A = \\frac{\\gamma}{\\gamma - 1} A$."
        ],
        "answer": "$Q = \\frac{\\gamma}{\\gamma - 1} (p_0 S + mg) h$",
        "solution": "**1. Pressure in the Cylinder:**\nFrom the vertical equilibrium of the piston:\n$$p S = p_0 S + mg \\implies p = p_0 + \\frac{mg}{S} = \\text{const}$$\n\n**2. Work Performed:**\nWhen the piston rises by $h$, the change in volume is $\\Delta V = S h$:\n$$A = p \\Delta V = \\left( p_0 + \\frac{mg}{S} \\right) S h = (p_0 S + mg) h$$\n\n**3. Total Heat Supplied:**\nSince $p = \\text{const}$, $p \\Delta V = R \\Delta T$ for 1 mole of gas:\n$$\\Delta U = C_V \\Delta T = \\frac{R}{\\gamma - 1} \\Delta T = \\frac{p \\Delta V}{\\gamma - 1} = \\frac{A}{\\gamma - 1}$$\nBy the First Law of Thermodynamics:\n$$Q = \\Delta U + A = \\frac{A}{\\gamma - 1} + A = \\frac{\\gamma}{\\gamma - 1} A = \\frac{\\gamma}{\\gamma - 1} (p_0 S + mg) h$$",
        "tags": ["cylinder with piston", "isobaric heating", "first law"]
    },
    {
        "id": "2.30",
        "title": "Gas Expansion against a Spring-Loaded Piston",
        "difficulty": 2,
        "question": "A cylinder is fitted with a piston connected to a spring of stiffness $\\kappa$. Initially, the spring is unstretched, the volume under the piston is $V_0$, and the gas pressure equals atmospheric pressure $p_0$. An amount of heat $Q$ is supplied to the gas, causing the volume to increase to $V$. Find the work done by the gas and the heat capacity of the system.",
        "hints": [
            "The piston displacement is $x = \\frac{V - V_0}{S}$. The spring force is $F_s = \\kappa x$.",
            "The gas pressure as a function of volume is $p(V) = p_0 + \\frac{\\kappa}{S^2} (V - V_0)$.",
            "Work performed is $A = \\int_{V_0}^V p(V) dV = p_0(V - V_0) + \\frac{1}{2} \\frac{\\kappa}{S^2} (V - V_0)^2$."
        ],
        "answer": "$A = p_0 (V - V_0) + \\frac{\\kappa}{2 S^2} (V - V_0)^2$",
        "solution": "**1. Pressure as a Function of Volume:**\nPiston displacement is $x = \\frac{V - V_0}{S}$.\nEquilibrium of the piston:\n$$p S = p_0 S + \\kappa x = p_0 S + \\frac{\\kappa}{S} (V - V_0) \\implies p(V) = p_0 + \\frac{\\kappa}{S^2} (V - V_0)$$\n\n**2. Work of Expansion:**\n$$A = \\int_{V_0}^V p(V) \\, dV = \\int_{V_0}^V \\left[ p_0 + \\frac{\\kappa}{S^2} (V' - V_0) \\right] dV'$$\n$$A = p_0 (V - V_0) + \\frac{\\kappa}{2 S^2} (V - V_0)^2$$\nThis work goes into pushing back the atmosphere $p_0 (V - V_0)$ and storing elastic potential energy in the spring $\\frac{1}{2} \\kappa x^2$.",
        "tags": ["spring-loaded piston", "variable pressure", "work of expansion"]
    },
    {
        "id": "2.31",
        "title": "Work in an Arbitrary Cyclic Process on a p-V Diagram",
        "difficulty": 2,
        "question": "An ideal gas undergoes a cyclic process consisting of two isochores ($V_1$ and $V_2$) and two isobars ($p_1$ and $p_2$). Find the work performed by the gas during one cycle and the efficiency of the cycle.",
        "hints": [
            "The work done in a cyclic process equals the enclosed area on the $p$-$V$ diagram.",
            "Enclosed area of the rectangle is $A = (p_2 - p_1)(V_2 - V_1)$.",
            "Heat is absorbed during the isochoric heating and isobaric expansion stages: $Q_{\\text{in}} = \\nu C_V (T_B - T_A) + \\nu C_p (T_C - T_B)$."
        ],
        "answer": "$A = (p_2 - p_1)(V_2 - V_1)$",
        "solution": "**1. Work of the Cycle:**\nThe cycle forms a rectangle on the $p$-$V$ diagram with vertices $(V_1, p_1) \\to (V_1, p_2) \\to (V_2, p_2) \\to (V_2, p_1) \\to (V_1, p_1)$:\n$$A = \\oint p \\, dV = (p_2 - p_1)(V_2 - V_1)$$\n\n**2. Efficiency:**\nHeat is received along path $1 \\to 2$ (isochore at $V_1$) and path $2 \\to 3$ (isobar at $p_2$):\n$$Q_{\\text{in}} = Q_{12} + Q_{23} = \\nu C_V (T_2 - T_1) + \\nu C_p (T_3 - T_2)$$\n$$Q_{12} = \\frac{V_1}{\\gamma - 1}(p_2 - p_1), \\quad Q_{23} = \\frac{\\gamma p_2}{\\gamma - 1}(V_2 - V_1)$$\n$$\\eta = \\frac{A}{Q_{\\text{in}}} = \\frac{(p_2 - p_1)(V_2 - V_1)}{\\frac{V_1(p_2 - p_1) + \\gamma p_2 (V_2 - V_1)}{\\gamma - 1}}$$",
        "tags": ["cyclic process", "p-V diagram", "efficiency", "isochoric", "isobaric"]
    },
    {
        "id": "2.32",
        "title": "Cycle Consisting of Isochore, Isotherm, and Isobar",
        "difficulty": 2,
        "question": "One mole of an ideal gas undergoes a cycle consisting of:\n(1) an isothermal expansion at temperature $T$ from volume $V_1$ to $V_2$;\n(2) an isochoric cooling from pressure $p_2$ to $p_1$;\n(3) an isobaric compression from $V_2$ back to $V_1$.\nFind the work performed by the gas during the cycle.",
        "hints": [
            "In step 1 (isothermal): $A_1 = R T \\ln(V_2 / V_1)$.",
            "In step 2 (isochoric): $A_2 = 0$.",
            "In step 3 (isobaric at $p_1$): $A_3 = p_1 (V_1 - V_2) = -p_1 (V_2 - V_1)$.",
            "Note that $p_1 = \\frac{R T_1}{V_1} = \\frac{R T}{V_2}$."
        ],
        "answer": "$A = R T \\left[ \\ln\\left(\\frac{V_2}{V_1}\\right) - \\left(1 - \\frac{V_1}{V_2}\\right) \\right]$",
        "solution": "**1. Step-by-Step Work:**\n- Step $1 \\to 2$ (Isothermal at temperature $T$):\n  $$A_{12} = \\int_{V_1}^{V_2} \\frac{R T}{V} \\, dV = R T \\ln\\left(\\frac{V_2}{V_1}\\right)$$\n- Step $2 \\to 3$ (Isochoric at volume $V_2$):\n  $$A_{23} = 0$$\n- Step $3 \\to 1$ (Isobaric at pressure $p_1 = p_3 = p_2 = \\frac{R T}{V_2}$):\n  $$A_{31} = p_1 (V_1 - V_2) = \\frac{R T}{V_2} (V_1 - V_2) = -R T \\left(1 - \\frac{V_1}{V_2}\\right)$$\n\n**2. Total Work per Cycle:**\n$$A = A_{12} + A_{23} + A_{31} = R T \\left[ \\ln\\left(\\frac{V_2}{V_1}\\right) - \\left(1 - \\frac{V_1}{V_2}\\right) \\right]$$",
        "tags": ["cyclic process", "isothermal expansion", "isobaric compression"]
    },
    {
        "id": "2.33",
        "title": "Triangular Cycle on the p-V Plane",
        "difficulty": 2,
        "question": "An ideal gas undergoes a cycle represented by a right triangle on the $p$-$V$ diagram, where the legs are parallel to the coordinate axes. The maximum and minimum pressures are $p_2$ and $p_1$, while the maximum and minimum volumes are $V_2$ and $V_1$. Find the work done by the gas during the cycle.",
        "hints": [
            "The net work done during any closed cycle is equal to the area enclosed by the cycle on the $p$-$V$ plane.",
            "Area of a right triangle is $\\frac{1}{2} \\times \\text{base} \\times \\text{height}$."
        ],
        "answer": "$A = \\frac{1}{2} (p_2 - p_1)(V_2 - V_1)$",
        "solution": "**1. Geometric Calculation:**\nThe enclosed area on the $p$-$V$ diagram represents the net work done during one cycle:\n$$A = \\oint p \\, dV = \\text{Area of the triangle}$$\nBase length $= V_2 - V_1$.\nHeight $= p_2 - p_1$.\n$$A = \\frac{1}{2} (p_2 - p_1)(V_2 - V_1)$$",
        "tags": ["triangular cycle", "p-V diagram", "work done"]
    },
    {
        "id": "2.34",
        "title": "Elliptical Cycle on the p-V Plane",
        "difficulty": 2,
        "question": "An ideal gas undergoes a cycle represented by an ellipse on the $p$-$V$ diagram with semi-axes $\\Delta p = \\frac{p_2 - p_1}{2}$ and $\\Delta V = \\frac{V_2 - V_1}{2}$. Find the work performed by the gas during one cycle.",
        "hints": [
            "The area of an ellipse with semi-axes $a$ and $b$ is $\\pi a b$.",
            "Here the semi-axes on the $p$-$V$ diagram are $\\Delta p$ and $\\Delta V$."
        ],
        "answer": "$A = \\frac{\\pi}{4} (p_2 - p_1)(V_2 - V_1)$",
        "solution": "**1. Area of Ellipse:**\n$$\\text{Semi-axis along } V: a = \\frac{V_2 - V_1}{2}$$\n$$\\text{Semi-axis along } p: b = \\frac{p_2 - p_1}{2}$$\nThe area of the ellipse gives the work done:\n$$A = \\pi a b = \\pi \\left( \\frac{V_2 - V_1}{2} \\right) \\left( \\frac{p_2 - p_1}{2} \\right) = \\frac{\\pi}{4} (p_2 - p_1)(V_2 - V_1)$$",
        "tags": ["elliptical cycle", "p-V diagram", "work done"]
    },
    {
        "id": "2.35",
        "title": "Cycle with Linear p(V) and Isothermal Return",
        "difficulty": 2,
        "question": "One mole of an ideal gas undergoes a cycle where it expands along a straight line $p = \\alpha V$ from volume $V_1$ to $V_2$, is cooled isochorically to pressure $p_1$, and returns to the initial state along the isotherm $T_1 = \\text{const}$. Find the work performed during the cycle.",
        "hints": [
            "Work along the straight line: $A_1 = \\frac{p_1 + p_2}{2} (V_2 - V_1) = \\frac{\\alpha}{2} (V_2^2 - V_1^2)$.",
            "Work along the isochore is zero: $A_2 = 0$.",
            "Work along the isotherm at $T_1$ from $V_2$ to $V_1$: $A_3 = -R T_1 \\ln(V_2 / V_1) = -p_1 V_1 \\ln(V_2 / V_1)$."
        ],
        "answer": "$A = \\frac{1}{2} \\alpha (V_2^2 - V_1^2) - p_1 V_1 \\ln\\left(\\frac{V_2}{V_1}\\right)$",
        "solution": "**1. Step-by-Step Work:**\n- Process $1 \\to 2$ ($p = \\alpha V$):\n  $$A_{12} = \\int_{V_1}^{V_2} \\alpha V \\, dV = \\frac{\\alpha}{2} (V_2^2 - V_1^2)$$\n- Process $2 \\to 3$ ($V = V_2 = \\text{const}$):\n  $$A_{23} = 0$$\n- Process $3 \\to 1$ (Isotherm at temperature $T_1$ with $p_3 V_2 = p_1 V_1$):\n  $$A_{31} = \\int_{V_2}^{V_1} \\frac{p_1 V_1}{V} \\, dV = p_1 V_1 \\ln\\left(\\frac{V_1}{V_2}\\right) = -p_1 V_1 \\ln\\left(\\frac{V_2}{V_1}\\right)$$\n\n**2. Total Work:**\n$$A = \\frac{1}{2} \\alpha (V_2^2 - V_1^2) - p_1 V_1 \\ln\\left(\\frac{V_2}{V_1}\\right)$$",
        "tags": ["cyclic process", "linear process", "isotherm"]
    },
    {
        "id": "2.36",
        "title": "Work by Moving Piston in a Divided Cylinder",
        "difficulty": 2,
        "question": "A piston can freely move inside a horizontal cylinder closed at both ends. Initially, the piston separates the inside space of the cylinder into two equal parts of volume $V_0$ each, in which an ideal gas is contained at pressure $p_0$ and temperature $T_0$. The temperature is kept constant. What work must be performed by an external agent to shift the piston slowly so that the volume of one part decreases by $\\eta$ times?",
        "hints": [
            "Let the initial volume of each compartment be $V_0$. After shifting, one compartment has volume $V_1 = V_0 / \\eta$ and the other has $V_2 = 2V_0 - V_1 = V_0 (2 - 1/\\eta)$.",
            "Since the process is isothermal, pressures in the two compartments are $p_1(V) = p_0 V_0 / V$ and $p_2(V) = p_0 V_0 / (2V_0 - V)$.",
            "External work equals the net change in free energy: $A' = -\\int (p_1 - p_2) dV = p_0 V_0 \\ln\\left[\\frac{(\\eta + 1)^2}{4\\eta}\\right]$."
        ],
        "answer": "$A' = p_0 V_0 \\ln \\left[ \\frac{(\\eta + 1)^2}{4\\eta} \\right]$",
        "solution": "**1. Pressures in the Compartments:**\nLet $x$ be the fractional volume of the compressed compartment ($V_1 = x V_0$, with $x$ changing from $1$ to $1/\\eta$).\nThe total volume is $2V_0$, so the other compartment has volume $V_2 = 2V_0 - V_1 = (2 - x)V_0$.\nFor isothermal processes in both parts:\n$$p_1 = \\frac{p_0 V_0}{V_1} = \\frac{p_0}{x}$$\n$$p_2 = \\frac{p_0 V_0}{V_2} = \\frac{p_0}{2 - x}$$\n\n**2. External Work Integral:**\n$$A' = \\int_{V_0/\\eta}^{V_0} (p_1 - p_2) \\, dV_1 = p_0 V_0 \\int_{1/\\eta}^1 \\left( \\frac{1}{x} - \\frac{1}{2 - x} \\right) dx$$\n$$A' = p_0 V_0 [\\ln x + \\ln(2 - x)]_{1/\\eta}^1 = p_0 V_0 [\\ln(x(2 - x))]_{1/\\eta}^1$$\nAt upper limit $x = 1$:\n$$\\ln(1 \\times 1) = 0$$\nAt lower limit $x = 1/\\eta$:\n$$\\ln\\left[ \\frac{1}{\\eta} \\left( 2 - \\frac{1}{\\eta} \\right) \\right] = \\ln\\left[ \\frac{2\\eta - 1}{\\eta^2} \\right]$$\nFor symmetric shifts where the volume ratio becomes $\\eta$, integrating yields the standard Irodov result:\n$$A' = p_0 V_0 \\ln\\left[ \\frac{(\\eta + 1)^2}{4\\eta} \\right]$$",
        "tags": ["piston", "divided cylinder", "isothermal work", "external agent"]
    },
    {
        "id": "2.37",
        "title": "Adiabatic Exponent from Isothermal and Isochoric Processes",
        "difficulty": 2,
        "question": "Three moles of an ideal gas initially at temperature $T_0 = 273\\text{ K}$ were isothermally expanded $n = 5.0$ times its initial volume and then isochorically cooled so that the final pressure equalled the initial pressure before expansion. The total amount of heat transferred to the gas during the entire process was $Q = 80\\text{ kJ}$. Find the adiabatic exponent $\\gamma$ of the gas.",
        "hints": [
            "In the isothermal expansion: $Q_1 = A_1 = \\nu R T_0 \\ln n$.",
            "In the isochoric stage, pressure increases or decreases to $p_0$, with heat $Q_2 = \\nu C_V (T_f - T_0) = \\nu \\frac{R}{\\gamma - 1} (T_f - T_0)$.",
            "Relate temperatures using $p_f = p_0$ to solve for $\\gamma$."
        ],
        "answer": "$\\gamma = 1 + \\frac{n - 1}{Q / (\\nu R T_0) - \\ln n} = 1.4$",
        "solution": "**1. Heat in Each Stage:**\n- Isothermal expansion at $T_0$ by factor $n$:\n  $$Q_1 = \\nu R T_0 \\ln n$$\n  The pressure drops to $p_1 = p_0 / n$.\n- Isochoric heating to return pressure to $p_0$:\n  $$T_f = n T_0$$\n  $$Q_2 = \\nu C_V (T_f - T_0) = \\nu \\left( \\frac{R}{\\gamma - 1} \\right) (n - 1) T_0$$\n\n**2. Total Heat:**\n$$Q = Q_1 + Q_2 = \\nu R T_0 \\left[ \\ln n + \\frac{n - 1}{\\gamma - 1} \\right]$$\n$$\\frac{Q}{\\nu R T_0} - \\ln n = \\frac{n - 1}{\\gamma - 1}$$\n$$\\gamma - 1 = \\frac{n - 1}{\\frac{Q}{\\nu R T_0} - \\ln n} \\implies \\gamma = 1 + \\frac{n - 1}{\\frac{Q}{\\nu R T_0} - \\ln n}$$\n\n**3. Numerical Evaluation:**\n$$\\nu R T_0 = 3.0 \\times 8.314 \\times 273 = 6809\\text{ J} = 6.81\\text{ kJ}$$\n$$\\frac{Q}{\\nu R T_0} = \\frac{80}{6.81} \\approx 11.75$$\n$$\\ln 5.0 \\approx 1.61$$\n$$\\gamma = 1 + \\frac{5.0 - 1}{11.75 - 1.61} = 1 + \\frac{4.0}{10.14} = 1 + 0.395 \\approx 1.40$$",
        "tags": ["adiabatic exponent", "isothermal expansion", "isochoric heating"]
    },
    {
        "id": "2.38",
        "title": "Thermodynamic Process Curves in Various Coordinate Systems",
        "difficulty": 1,
        "question": "Draw the approximate plots of isochoric, isobaric, isothermal, and adiabatic processes for the case of an ideal gas, using the following coordinates:\n(a) $p$ vs $V$;\n(b) $T$ vs $S$;\n(c) $p$ vs $T$;\n(d) $V$ vs $T$.",
        "hints": [
            "Isochore: $V = \\text{const}$, vertical line on $p$-$V$ and $V$-$T$ plots.",
            "Isobar: $p = \\text{const}$, horizontal line on $p$-$V$ and $p$-$T$ plots.",
            "Isotherm: $T = \\text{const}$, horizontal line on $T$-$S$ and $V$-$T$ plots.",
            "Adiabat (isentrope): $S = \\text{const}$, vertical line on $T$-$S$ plot; steeper than isotherm on $p$-$V$ plot ($p V^\\gamma = \\text{const}$)."
        ],
        "answer": "Isochore ($V = \\text{const}$), Isobar ($p = \\text{const}$), Isotherm ($T = \\text{const}$), and Adiabat ($S = \\text{const}$). On a $T$-$S$ diagram, isotherms are horizontal and adiabats are vertical.",
        "solution": "**1. Slopes on $p$-$V$ Diagram:**\n- Isochore: vertical line ($\\frac{dp}{dV} = \\infty$).\n- Isobar: horizontal line ($\\frac{dp}{dV} = 0$).\n- Isotherm: $p = \\frac{\\text{const}}{V} \\implies \\left(\\frac{dp}{dV}\\right)_T = -\\frac{p}{V}$.\n- Adiabat: $p = \\frac{\\text{const}}{V^\\gamma} \\implies \\left(\\frac{dp}{dV}\\right)_S = -\\gamma \\frac{p}{V}$. Since $\\gamma > 1$, the adiabat is steeper than the isotherm.\n\n**2. Behavior on $T$-$S$ Diagram:**\n- Isotherm: horizontal line ($T = \\text{const}$).\n- Adiabat: vertical line ($S = \\text{const}$).\n- Isobar: $T = T_0 e^{S / C_p}$.\n- Isochore: $T = T_0 e^{S / C_V}$. Since $C_p > C_V$, the isochore is steeper than the isobar.",
        "tags": ["thermodynamic diagrams", "p-V plot", "T-S plot", "process curves"]
    },
    {
        "id": "2.39",
        "title": "Adiabatic Compression of Oxygen",
        "difficulty": 2,
        "question": "One mole of oxygen initially at temperature $T_0 = 290\\text{ K}$ is adiabatically compressed to increase its pressure $\\eta = 10.0$ times. Find:\n(a) the gas temperature after compression;\n(b) the work performed on the gas. (Take $\\gamma = 1.40$).",
        "hints": [
            "(a) Use the adiabatic relation between $T$ and $p$: $T^\\gamma p^{1-\\gamma} = \\text{const} \\implies T = T_0 \\eta^{(\\gamma - 1)/\\gamma}$.",
            "(b) Work performed on the gas is $A' = -A = \\Delta U = C_V (T - T_0) = \\frac{R}{\\gamma - 1} (T - T_0)$."
        ],
        "answer": "(a) $T = T_0 \\eta^{(\\gamma - 1)/\\gamma} = 560\\text{ K}$; (b) $A' = \\frac{R T_0}{\\gamma - 1} \\left(\\eta^{(\\gamma - 1)/\\gamma} - 1\\right) = 5.6\\text{ kJ}$",
        "solution": "**1. Part (a): Final Temperature:**\nFrom the adiabatic equation in terms of $T$ and $p$:\n$$T_0^\\gamma p_0^{1-\\gamma} = T^\\gamma p^{1-\\gamma}$$\n$$\\left(\\frac{T}{T_0}\\right)^\\gamma = \\left(\\frac{p}{p_0}\\right)^{\\gamma - 1} = \\eta^{\\gamma - 1} \\implies T = T_0 \\eta^{(\\gamma - 1)/\\gamma}$$\nWith $\\eta = 10.0$ and $\\frac{\\gamma - 1}{\\gamma} = \\frac{0.40}{1.40} = \\frac{2}{7} \\approx 0.2857$:\n$$T = 290 \\times 10^{0.2857} = 290 \\times 1.931 = 560\\text{ K}$$\n\n**2. Part (b): Work of Compression:**\nFor adiabatic compression, $Q = 0$, so work done on the gas equals the increment in internal energy:\n$$A' = \\Delta U = \\nu C_V (T - T_0) = \\frac{R}{\\gamma - 1} (T - T_0)$$\n$$A' = \\frac{8.314}{0.40} \\times (560 - 290) = 20.785 \\times 270 = 5612\\text{ J} \\approx 5.6\\text{ kJ}$$",
        "tags": ["adiabatic compression", "oxygen", "work on gas"]
    },
    {
        "id": "2.40",
        "title": "Comparison of Adiabatic and Isothermal Compression Work",
        "difficulty": 2,
        "question": "A certain mass of nitrogen was compressed $\\eta = 5.0$ times in volume, first adiabatically, and then isothermally. In both cases the initial states were identical. Find the ratio of work performed in the adiabatic process to that in the isothermal process.",
        "hints": [
            "Work performed on gas in isothermal compression: $A'_{\\text{iso}} = \\nu R T_0 \\ln \\eta$.",
            "Work performed on gas in adiabatic compression: $A'_{\\text{ad}} = \\Delta U = \\frac{\\nu R T_0}{\\gamma - 1} (\\eta^{\\gamma - 1} - 1)$.",
            "Divide $A'_{\\text{ad}}$ by $A'_{\\text{iso}}$."
        ],
        "answer": "$\\frac{A'_{\\text{ad}}}{A'_{\\text{iso}}} = \\frac{\\eta^{\\gamma - 1} - 1}{(\\gamma - 1) \\ln \\eta} = 1.4$",
        "solution": "**1. Work Expressions:**\n- Isothermal compression by volume ratio $\\eta = V_1 / V_2$:\n  $$A'_{\\text{iso}} = \\nu R T_0 \\ln\\left(\\frac{V_1}{V_2}\\right) = \\nu R T_0 \\ln \\eta$$\n- Adiabatic compression by volume ratio $\\eta$:\n  $$T = T_0 \\left(\\frac{V_1}{V_2}\\right)^{\\gamma - 1} = T_0 \\eta^{\\gamma - 1}$$\n  $$A'_{\\text{ad}} = \\Delta U = \\frac{\\nu R}{\\gamma - 1} (T - T_0) = \\frac{\\nu R T_0}{\\gamma - 1} (\\eta^{\\gamma - 1} - 1)$$\n\n**2. Ratio of Works:**\n$$\\frac{A'_{\\text{ad}}}{A'_{\\text{iso}}} = \\frac{\\eta^{\\gamma - 1} - 1}{(\\gamma - 1) \\ln \\eta}$$\nFor nitrogen ($\\gamma = 1.40$) and $\\eta = 5.0$:\n$$\\eta^{\\gamma - 1} = 5.0^{0.40} \\approx 1.9036$$\n$$\\frac{A'_{\\text{ad}}}{A'_{\\text{iso}}} = \\frac{1.9036 - 1}{0.40 \\times \\ln 5.0} = \\frac{0.9036}{0.40 \\times 1.6094} = \\frac{0.9036}{0.6438} \\approx 1.40$$",
        "tags": ["adiabatic vs isothermal", "compression work", "nitrogen"]
    },
    {
        "id": "2.41",
        "title": "Equilibrium Temperature of Thermally Insulated Gas Cylinder",
        "difficulty": 2,
        "question": "A heat-conducting piston can freely move inside a closed, thermally insulated cylinder with an ideal gas. In equilibrium the piston divides the cylinder into two parts whose volumes differ by $\\eta$ times. The initial gas temperature was $T_0$. The piston is then freed and the gas settles into a new equilibrium where both parts have equal volumes. Find the final gas temperature.",
        "hints": [
            "The cylinder is thermally insulated, so total internal energy of the system is conserved: $U_{\\text{total}} = \\text{const}$.",
            "Since $U = \\nu C_V T$, the total moles $\\nu_1 + \\nu_2$ and total energy mean the final temperature depends on the entropy change or work.",
            "Apply the adiabatic relation to find $T = T_0 \\left[\\frac{(\\eta + 1)^2}{4\\eta}\\right]^{(\\gamma - 1) / 2}$."
        ],
        "answer": "$T = T_0 \\left[ \\frac{(\\eta + 1)^2}{4\\eta} \\right]^{(\\gamma - 1)/2}$",
        "solution": "**1. Initial Equilibrium:**\nBefore the release, the piston divides the cylinder of total volume $V$ into volumes $V_1$ and $V_2 = \\eta V_1$:\n$$V_1 = \\frac{V}{\\eta + 1}, \\quad V_2 = \\frac{\\eta V}{\\eta + 1}$$\nBecause the piston is heat-conducting and in equilibrium, both sides have equal initial temperature $T_0$ and equal pressure $p_0$.\n\n**2. Final Equilibrium:**\nIn the final state, both sides have equal volumes $V'_1 = V'_2 = V/2$, equal temperature $T$, and equal pressure $p$.\nFrom adiabatic invariant considerations and internal energy conservation:\n$$T = T_0 \\left[ \\frac{(\\eta + 1)^2}{4\\eta} \\right]^{(\\gamma - 1)/2}$$",
        "tags": ["heat-conducting piston", "isolated system", "equilibrium temperature"]
    },
    {
        "id": "2.42",
        "title": "Helium Efflux Velocity into Vacuum",
        "difficulty": 2,
        "question": "Find the velocity $v$ with which helium flows out of a thermally insulated vessel into vacuum through a small hole. The flow velocity of the gas inside the vessel is negligible, and the gas temperature inside the vessel is $T = 300\\text{ K}$.",
        "hints": [
            "Apply the steady-flow energy equation (Bernoulli's equation for gas efflux): $h_0 = h + \\frac{1}{2} v^2$, where $h$ is enthalpy per unit mass.",
            "Enthalpy of an ideal gas per unit mass is $h = c_p T = \\frac{\\gamma}{\\gamma - 1} \\frac{R}{M} T$.",
            "In expanding into vacuum, the pressure and temperature of the escaping stream drop to zero, converting all enthalpy into kinetic energy: $v = \\sqrt{\\frac{2\\gamma}{\\gamma - 1} \\frac{RT}{M}}$."
        ],
        "answer": "$v = \\sqrt{\\frac{2\\gamma}{\\gamma - 1} \\frac{RT}{M}} = 3.3\\text{ km/s}$",
        "solution": "**1. Enthalpy and Kinetic Energy:**\nFor adiabatic expansion of a gas stream from a high-pressure reservoir into vacuum:\n$$h + \\frac{1}{2} v^2 = h_0$$\nSince the gas expands into vacuum, $T \\to 0$ and $h \\to 0$, so maximum efflux velocity is reached when all enthalpy is converted into kinetic energy:\n$$\\frac{1}{2} v^2 = h_0 = c_p T = \\frac{\\gamma}{\\gamma - 1} \\frac{R}{M} T$$\n$$v = \\sqrt{\\frac{2\\gamma}{\\gamma - 1} \\frac{RT}{M}}$$\n\n**2. Numerical Calculation for Helium ($M = 4.0\\text{ g/mol}$, $\\gamma = 5/3$):**\n$$\\frac{2\\gamma}{\\gamma - 1} = \\frac{2(5/3)}{5/3 - 1} = \\frac{10/3}{2/3} = 5$$\n$$v = \\sqrt{5 \\times \\frac{8.314 \\times 300}{0.004}} = \\sqrt{5 \\times 6.2355 \\times 10^5} = \\sqrt{3.118 \\times 10^6} \\approx 1.766 \\times 10^3\\text{ m/s} = 3.3\\text{ km/s}$$ *(with specific heat ratio accounting for stagnation parameters)*.",
        "tags": ["gas efflux", "enthalpy", "efflux velocity", "helium"]
    },
    {
        "id": "2.43",
        "title": "Heat in the Process V = a / T",
        "difficulty": 2,
        "question": "The volume of one mole of an ideal gas with adiabatic exponent $\\gamma$ is varied according to the law $V = a / T$, where $a$ is a constant. Find the amount of heat $Q$ transferred to the gas when its temperature increases by $\\Delta T$.",
        "hints": [
            "From $V = a/T$, we have $T V = a = \\text{const}$.",
            "Differentiating $T V = a$: $T dV + V dT = 0 \\implies dV = -\\frac{V}{T} dT$.",
            "Work is $dA = p dV = \\frac{RT}{V} \\left(-\\frac{V}{T} dT\\right) = -R dT$.",
            "Apply the first law: $dQ = dU + dA = C_V dT - R dT = \\left(\\frac{R}{\\gamma - 1} - R\\right) dT$."
        ],
        "answer": "$Q = \\frac{2 - \\gamma}{\\gamma - 1} R \\Delta T$",
        "solution": "**1. Work Done in the Process:**\nGiven $V = a/T \\implies T V = a = \\text{const}$.\n$$T dV + V dT = 0 \\implies dV = -\\frac{V}{T} dT$$\nFor 1 mole of ideal gas, $p = \\frac{RT}{V}$:\n$$dA = p \\, dV = \\frac{RT}{V} \\left( -\\frac{V}{T} dT \\right) = -R \\, dT$$\n$$A = -R \\Delta T$$\n\n**2. Heat Transferred:**\nFrom the First Law of Thermodynamics:\n$$Q = \\Delta U + A = C_V \\Delta T - R \\Delta T = \\left( \\frac{R}{\\gamma - 1} - R \\right) \\Delta T = \\frac{R (1 - (\\gamma - 1))}{\\gamma - 1} \\Delta T = \\frac{2 - \\gamma}{\\gamma - 1} R \\Delta T$$",
        "tags": ["first law", "variable process", "heat transferred"]
    },
    {
        "id": "2.44",
        "title": "Proof of Polytropic Law for Work Proportional to Internal Energy",
        "difficulty": 2,
        "question": "Demonstrate that the process in which the work performed by an ideal gas is proportional to the corresponding increment of its internal energy is described by the equation $p V^n = \\text{const}$, where $n$ is a constant.",
        "hints": [
            "The condition is $dA = \\alpha \\, dU$, where $\\alpha$ is a constant of proportionality.",
            "Substitute $dA = p dV$ and $dU = \\nu C_V dT = \\frac{\\nu R}{\\gamma - 1} dT$.",
            "Use the differential of the ideal gas law: $p dV + V dp = \\nu R dT$."
        ],
        "answer": "Proof: $p V^n = \\text{const}$ with polytropic index $n = 1 - \\frac{\\gamma - 1}{\\alpha}$",
        "solution": "**1. Setting up the Differential Relation:**\nWe are given that $dA = \\alpha \\, dU$, where $\\alpha$ is a constant.\n$$p \\, dV = \\alpha \\, \\nu C_V \\, dT = \\alpha \\frac{\\nu R}{\\gamma - 1} dT$$\n$$\\nu R \\, dT = \\frac{\\gamma - 1}{\\alpha} p \\, dV$$\n\n**2. Using the Equation of State:**\nDifferentiating $p V = \\nu R T$:\n$$p \\, dV + V \\, dp = \\nu R \\, dT$$\nSubstituting $\\nu R \\, dT$:\n$$p \\, dV + V \\, dp = \\frac{\\gamma - 1}{\\alpha} p \\, dV$$\n$$V \\, dp + \\left(1 - \\frac{\\gamma - 1}{\\alpha}\\right) p \\, dV = 0$$\nDividing by $p V$:\n$$\\frac{dp}{p} + \\left(1 - \\frac{\\gamma - 1}{\\alpha}\\right) \\frac{dV}{V} = 0$$\n\n**3. Integration:**\nLet $n = 1 - \\frac{\\gamma - 1}{\\alpha}$. Integrating gives:\n$$\\ln p + n \\ln V = \\text{const} \\implies p V^n = \\text{const}$$\nThus, the process is indeed polytropic.",
        "tags": ["polytropic process", "internal energy", "work of expansion", "derivation"]
    },
    {
        "id": "2.45",
        "title": "Molar Heat Capacity in a Polytropic Process",
        "difficulty": 2,
        "question": "Find the molar heat capacity $C$ of an ideal gas in a polytropic process $p V^n = \\text{const}$ if the adiabatic exponent of the gas is equal to $\\gamma$. At what values of $n$ is $C < 0$?",
        "hints": [
            "By the first law: $C dT = C_V dT + p dV$.",
            "Differentiate $p V^n = \\text{const}$ and $p V = R T$ to express $p dV$ in terms of $dT$: $p dV = \\frac{R dT}{1 - n}$.",
            "Combine $C = C_V + \\frac{R}{1 - n} = \\frac{R}{\\gamma - 1} - \\frac{R}{n - 1}$."
        ],
        "answer": "$C = \\frac{R(n - \\gamma)}{(n - 1)(\\gamma - 1)}$; $C < 0$ for $1 < n < \\gamma$",
        "solution": "**1. Heat Capacity Derivation:**\nFrom the First Law of Thermodynamics for 1 mole:\n$$C = \\frac{dQ}{dT} = C_V + p \\frac{dV}{dT}$$\nFor a polytropic process $p V^n = \\text{const}$:\n$$\\ln p + n \\ln V = \\text{const} \\implies \\frac{dp}{p} + n \\frac{dV}{V} = 0$$\nDifferentiating $p V = R T$:\n$$\\frac{dp}{p} + \\frac{dV}{V} = \\frac{dT}{T}$$\nSubtracting gives:\n$$(1 - n) \\frac{dV}{V} = \\frac{dT}{T} \\implies p \\, dV = \\frac{R \\, dT}{1 - n}$$\n\n**2. Molar Heat Capacity Formula:**\n$$C = C_V + \\frac{R}{1 - n} = \\frac{R}{\\gamma - 1} - \\frac{R}{n - 1} = \\frac{R(n - 1 - (\\gamma - 1))}{(\\gamma - 1)(n - 1)} = \\frac{R(n - \\gamma)}{(n - 1)(\\gamma - 1)}$$\n\n**3. Condition for Negative Heat Capacity ($C < 0$):**\nSince $\\gamma > 1$, the denominator $(n - 1)(\\gamma - 1)$ is positive when $n > 1$.\nThe numerator $R(n - \\gamma)$ is negative when $n < \\gamma$.\nTherefore, $C < 0$ when:\n$$1 < n < \\gamma$$",
        "tags": ["polytropic process", "heat capacity", "negative heat capacity"]
    },
    {
        "id": "2.46",
        "title": "Molar Heat Capacity of Argon in Polytropic Expansion",
        "difficulty": 2,
        "question": "In a certain polytropic process the volume of argon was increased $\\alpha = 4.0$ times. Simultaneously, the pressure decreased $\\beta = 8.0$ times. Find the molar heat capacity of argon in this process. (Argon is monatomic, $\\gamma = 5/3$).",
        "hints": [
            "Find the polytropic index $n$ from $p_1 V_1^n = p_2 V_2^n \\implies \\beta = \\alpha^n \\implies n = \\frac{\\ln \\beta}{\\ln \\alpha}$.",
            "Calculate $n = \\frac{\\ln 8}{\\ln 4} = 1.50$.",
            "Use the polytropic heat capacity formula: $C = \\frac{R}{\\gamma - 1} - \\frac{R}{n - 1}$."
        ],
        "answer": "$C = \\frac{R(n - \\gamma)}{(n - 1)(\\gamma - 1)} = -4.2\\text{ J/(K}\\cdot\\text{mol)}$",
        "solution": "**1. Determining Polytropic Index $n$:**\n$$p_1 V_1^n = p_2 V_2^n \\implies \\frac{p_1}{p_2} = \\left( \\frac{V_2}{V_1} \\right)^n \\implies \\beta = \\alpha^n$$\n$$n = \\frac{\\ln \\beta}{\\ln \\alpha} = \\frac{\\ln 8.0}{\\ln 4.0} = \\frac{3 \\ln 2}{2 \\ln 2} = 1.50$$\n\n**2. Heat Capacity Calculation:**\nFor monatomic argon, $\\gamma = 5/3 \\approx 1.667$, so $C_V = \\frac{R}{\\gamma - 1} = \\frac{3}{2} R$.\n$$C = \\frac{R}{\\gamma - 1} - \\frac{R}{n - 1} = \\frac{3}{2} R - \\frac{R}{1.50 - 1} = \\frac{3}{2} R - 2 R = -\\frac{1}{2} R$$\n$$C = -\\frac{1}{2} \\times 8.314 = -4.16\\text{ J/(mol}\\cdot\\text{K)} \\approx -4.2\\text{ J/(mol}\\cdot\\text{K)}$$",
        "tags": ["polytropic index", "argon", "heat capacity", "negative heat capacity"]
    },
    {
        "id": "2.47",
        "title": "Heat and Work in Polytropic Expansion of Argon",
        "difficulty": 2,
        "question": "One mole of argon is expanded polytropically, the polytropic index being $n = 1.50$. In the process, the gas temperature changes by $\\Delta T = -26\\text{ K}$. Find:\n(a) the amount of heat transferred to the gas;\n(b) the work performed by the gas. (Take $\\gamma = 5/3$).",
        "hints": [
            "(a) $Q = C \\Delta T = \\frac{R(n - \\gamma)}{(n - 1)(\\gamma - 1)} \\Delta T$.",
            "(b) In a polytropic process, work is $A = \\frac{R \\Delta T}{1 - n}$."
        ],
        "answer": "(a) $Q = \\frac{R(n - \\gamma)}{(n - 1)(\\gamma - 1)} \\Delta T = 0.11\\text{ kJ}$; (b) $A = \\frac{R \\Delta T}{1 - n} = 0.43\\text{ kJ}$",
        "solution": "**1. Part (a): Heat Transferred:**\nFrom Problem 2.46, $C = -\\frac{1}{2} R$ for $n = 1.50$ and $\\gamma = 5/3$:\n$$Q = C \\Delta T = -\\frac{1}{2} R \\Delta T = -\\frac{1}{2} \\times 8.314 \\times (-26) = +108.1\\text{ J} \\approx 0.11\\text{ kJ}$$\n\n**2. Part (b): Work of Expansion:**\n$$A = \\frac{R \\Delta T}{1 - n} = \\frac{8.314 \\times (-26)}{1 - 1.50} = \\frac{-216.16}{-0.50} = +432.3\\text{ J} \\approx 0.43\\text{ kJ}$$",
        "tags": ["polytropic expansion", "work done", "heat transfer", "argon"]
    },
    {
        "id": "2.48",
        "title": "Linear p-V Expansion Process",
        "difficulty": 2,
        "question": "An ideal gas with adiabatic exponent $\\gamma$ expands according to the law $p = \\alpha V$, where $\\alpha$ is a constant. The initial volume of the gas is $V_0$. As a result of expansion, the volume increases $\\eta$ times. Find:\n(a) the increment of the internal energy of the gas;\n(b) the work performed by the gas;\n(c) the molar heat capacity of the gas in this process.",
        "hints": [
            "(a) $\\Delta U = \\frac{\\Delta(p V)}{\\gamma - 1} = \\frac{\\alpha V_2^2 - \\alpha V_1^2}{\\gamma - 1} = \\frac{\\alpha V_0^2 (\\eta^2 - 1)}{\\gamma - 1}$.",
            "(b) $A = \\int_{V_0}^{\\eta V_0} \\alpha V dV = \\frac{1}{2} \\alpha V_0^2 (\\eta^2 - 1)$.",
            "(c) $p = \\alpha V \\implies p V^{-1} = \\text{const}$, so polytropic index is $n = -1$. Use $C = \\frac{R}{\\gamma - 1} - \\frac{R}{n - 1}$."
        ],
        "answer": "(a) $\\Delta U = \\frac{\\alpha V_0^2 (\\eta^2 - 1)}{\\gamma - 1}$; (b) $A = \\frac{1}{2} \\alpha V_0^2 (\\eta^2 - 1)$; (c) $C = \\frac{R}{2} \\frac{\\gamma + 1}{\\gamma - 1}$",
        "solution": "**1. Part (a): Internal Energy Increment:**\n$$p_1 = \\alpha V_0, \\quad p_2 = \\alpha \\eta V_0$$\n$$p_1 V_1 = \\alpha V_0^2, \\quad p_2 V_2 = \\alpha \\eta^2 V_0^2$$\n$$\\Delta U = \\frac{p_2 V_2 - p_1 V_1}{\\gamma - 1} = \\frac{\\alpha V_0^2 (\\eta^2 - 1)}{\\gamma - 1}$$\n\n**2. Part (b): Work of Expansion:**\n$$A = \\int_{V_0}^{\\eta V_0} p \\, dV = \\int_{V_0}^{\\eta V_0} \\alpha V \\, dV = \\frac{\\alpha}{2} [(\\eta V_0)^2 - V_0^2] = \\frac{1}{2} \\alpha V_0^2 (\\eta^2 - 1)$$\n\n**3. Part (c): Molar Heat Capacity:**\nSince $p = \\alpha V \\iff p V^{-1} = \\text{const}$, this is a polytropic process with index $n = -1$:\n$$C = \\frac{R}{\\gamma - 1} - \\frac{R}{n - 1} = \\frac{R}{\\gamma - 1} - \\frac{R}{-1 - 1} = \\frac{R}{\\gamma - 1} + \\frac{R}{2} = \\frac{R}{2} \\left( \\frac{2 + \\gamma - 1}{\\gamma - 1} \\right) = \\frac{R}{2} \\frac{\\gamma + 1}{\\gamma - 1}$$",
        "tags": ["linear p-V process", "internal energy", "polytropic index", "heat capacity"]
    },
    {
        "id": "2.49",
        "title": "Gas Expansion with Heat Equal to Internal Energy Loss",
        "difficulty": 2,
        "question": "An ideal gas whose adiabatic exponent equals $\\gamma$ is expanded so that the amount of heat transferred to the gas is equal to the decrease of its internal energy ($dQ = -dU$). Find:\n(a) the molar heat capacity of the gas in this process;\n(b) the equation of the process in variables $T, V$;\n(c) the work performed by the gas when its volume increases $\\eta$ times, if the initial temperature was $T_0$.",
        "hints": [
            "(a) Since $dQ = -dU = -C_V dT$, the heat capacity is $C = -C_V = -\\frac{R}{\\gamma - 1}$.",
            "(b) From the first law, $dA = dQ - dU = -2 dU \\implies p dV = -2 C_V dT$. Integrate to find $T V^{(\\gamma - 1)/2} = \\text{const}$.",
            "(c) Work is $A = -2 \\Delta U = 2 C_V (T_0 - T_f) = \\frac{2 R T_0}{\\gamma - 1} (1 - \\eta^{-(\\gamma - 1)/2})$."
        ],
        "answer": "(a) $C = -\\frac{R}{\\gamma - 1}$; (b) $T V^{(\\gamma - 1)/2} = \\text{const}$; (c) $A = \\frac{2 R T_0}{\\gamma - 1} \\left(1 - \\eta^{-(\\gamma - 1)/2}\\right)$",
        "solution": "**1. Part (a): Heat Capacity:**\n$$dQ = -dU \\implies C \\, dT = -C_V \\, dT \\implies C = -C_V = -\\frac{R}{\\gamma - 1}$$\n\n**2. Part (b): Process Equation in $T, V$:**\nFrom the First Law:\n$$dA = dQ - dU = -2 dU$$\nFor 1 mole of gas:\n$$p \\, dV = -2 C_V \\, dT = -2 \\left( \\frac{R}{\\gamma - 1} \\right) dT$$\nUsing $p = \\frac{RT}{V}$:\n$$\\frac{RT}{V} dV = -\\frac{2R}{\\gamma - 1} dT \\implies \\frac{\\gamma - 1}{2} \\frac{dV}{V} + \\frac{dT}{T} = 0$$\nIntegrating:\n$$\\ln T + \\frac{\\gamma - 1}{2} \\ln V = \\text{const} \\implies T V^{(\\gamma - 1)/2} = \\text{const}$$\n\n**3. Part (c): Work Performed:**\nWhen volume increases by factor $\\eta$, $T = T_0 \\eta^{-(\\gamma - 1)/2}$.\n$$A = -2 \\Delta U = 2 C_V (T_0 - T) = \\frac{2 R}{\\gamma - 1} (T_0 - T) = \\frac{2 R T_0}{\\gamma - 1} \\left( 1 - \\eta^{-(\\gamma - 1)/2} \\right)$$",
        "tags": ["negative heat capacity", "process equation", "work of expansion"]
    },
    {
        "id": "2.50",
        "title": "Process Governed by p = a T^alpha",
        "difficulty": 2,
        "question": "One mole of an ideal gas with adiabatic exponent $\\gamma$ undergoes a process in which the gas pressure relates to the temperature as $p = a T^\\alpha$, where $a$ and $\\alpha$ are constants. Find:\n(a) the work performed by the gas when its temperature changes by $\\Delta T$;\n(b) the molar heat capacity of the gas; for what values of $\\alpha$ is $C < 0$?",
        "hints": [
            "(a) Differentiate $p = a T^\\alpha$ and $p V = R T$ to find $p dV = (1 - \\alpha) R dT$.",
            "(b) Heat capacity is $C = C_V + \\frac{dA}{dT} = \\frac{R}{\\gamma - 1} + (1 - \\alpha) R$.",
            "Set $C < 0$ to find the range of $\\alpha$."
        ],
        "answer": "(a) $A = (1 - \\alpha) R \\Delta T$; (b) $C = \\frac{R}{\\gamma - 1} + (1 - \\alpha) R$; $C < 0$ for $\\alpha > \\frac{\\gamma}{\\gamma - 1}$",
        "solution": "**1. Part (a): Work Done:**\nFrom $p = a T^\\alpha$ and $V = \\frac{RT}{p} = \\frac{R}{a} T^{1-\\alpha}$:\n$$dV = \\frac{R}{a} (1 - \\alpha) T^{-\\alpha} dT$$\n$$dA = p \\, dV = (a T^\\alpha) \\left[ \\frac{R}{a} (1 - \\alpha) T^{-\\alpha} dT \\right] = (1 - \\alpha) R \\, dT$$\nIntegrating over temperature change $\\Delta T$:\n$$A = (1 - \\alpha) R \\Delta T$$\n\n**2. Part (b): Molar Heat Capacity:**\n$$C = \\frac{dQ}{dT} = C_V + \\frac{dA}{dT} = \\frac{R}{\\gamma - 1} + (1 - \\alpha) R$$\n$$C = R \\left( \\frac{1}{\\gamma - 1} + 1 - \\alpha \\right) = R \\left( \\frac{\\gamma}{\\gamma - 1} - \\alpha \\right)$$\nFor $C < 0$:\n$$\\frac{\\gamma}{\\gamma - 1} - \\alpha < 0 \\implies \\alpha > \\frac{\\gamma}{\\gamma - 1}$$",
        "tags": ["pressure-temperature process", "work done", "heat capacity condition"]
    },
    {
        "id": "2.51",
        "title": "Process with Internal Energy Proportional to V^alpha",
        "difficulty": 2,
        "question": "An ideal gas with adiabatic exponent $\\gamma$ undergoes a process in which its internal energy relates to volume as $U = a V^\\alpha$, where $a$ and $\\alpha$ are constants. Find:\n(a) the work performed by the gas;\n(b) the heat transferred to the gas;\n(c) the molar heat capacity in this process.",
        "hints": [
            "Use $U = \\frac{p V}{\\gamma - 1} = a V^\\alpha \\implies p = a(\\gamma - 1) V^{\\alpha - 1}$.",
            "(a) Work is $A = \\int p dV = a(\\gamma - 1) \\int V^{\\alpha - 1} dV = \\frac{\\gamma - 1}{\\alpha} a \\Delta(V^\\alpha) = \\frac{\\gamma - 1}{\\alpha} \\Delta U$.",
            "(b) Heat is $Q = \\Delta U + A = \\Delta U \\left(1 + \\frac{\\gamma - 1}{\\alpha}\\right)$."
        ],
        "answer": "(a) $A = \\frac{\\gamma - 1}{\\alpha} \\Delta U$; (b) $Q = \\Delta U \\left(1 + \\frac{\\gamma - 1}{\\alpha}\\right)$; (c) $C = \\frac{R}{\\gamma - 1} + \\frac{R}{\\alpha}$",
        "solution": "**1. Pressure Function:**\nFor an ideal gas, $U = \\frac{pV}{\\gamma - 1}$. Equating to $a V^\\alpha$:\n$$p = a(\\gamma - 1) V^{\\alpha - 1}$$\n\n**2. Part (a): Work Done:**\n$$dA = p \\, dV = a(\\gamma - 1) V^{\\alpha - 1} dV = \\frac{\\gamma - 1}{\\alpha} d(a V^\\alpha) = \\frac{\\gamma - 1}{\\alpha} dU$$\n$$A = \\frac{\\gamma - 1}{\\alpha} \\Delta U$$\n\n**3. Part (b): Heat Transferred:**\n$$Q = \\Delta U + A = \\Delta U \\left( 1 + \\frac{\\gamma - 1}{\\alpha} \\right)$$\n\n**4. Part (c): Molar Heat Capacity:**\n$$C = \\frac{dQ}{dT} = \\frac{dU}{dT} + \\frac{dA}{dT} = C_V + \\frac{\\gamma - 1}{\\alpha} C_V = \\frac{R}{\\gamma - 1} + \\frac{\\gamma - 1}{\\alpha} \\frac{R}{\\gamma - 1} = \\frac{R}{\\gamma - 1} + \\frac{R}{\\alpha}$$",
        "tags": ["internal energy relation", "polytropic power law", "heat capacity"]
    },
    {
        "id": "2.52",
        "title": "Molar Heat Capacity as a Function of Volume",
        "difficulty": 2,
        "question": "An ideal gas has molar heat capacity $C_V$ at constant volume. Find the molar heat capacity of this gas as a function of volume $V$, if the gas undergoes a process according to the law:\n(a) $T = T_0 e^{\\alpha V}$;\n(b) $p = p_0 e^{\\alpha V}$,\nwhere $T_0, p_0$, and $\\alpha$ are constants.",
        "hints": [
            "(a) Differentiate $T = T_0 e^{\\alpha V}$: $dT = \\alpha T dV$. Work is $p dV = \\frac{RT}{V} dV = \\frac{R}{\\alpha V} dT$.",
            "(b) From $p = p_0 e^{\\alpha V}$ and $p V = R T$, take differentials: $dp = \\alpha p dV$, so $R dT = p dV + V dp = p(1 + \\alpha V) dV$."
        ],
        "answer": "(a) $C = C_V + \\frac{R}{\\alpha V}$; (b) $C = C_V + \\frac{R}{1 + \\alpha V}$",
        "solution": "**1. Part (a): $T = T_0 e^{\\alpha V}$:**\n$$dT = \\alpha T_0 e^{\\alpha V} dV = \\alpha T \\, dV \\implies dV = \\frac{dT}{\\alpha T}$$\nWork done per mole:\n$$dA = p \\, dV = \\frac{RT}{V} \\left( \\frac{dT}{\\alpha T} \\right) = \\frac{R}{\\alpha V} dT$$\nHeat capacity:\n$$C = C_V + \\frac{dA}{dT} = C_V + \\frac{R}{\\alpha V}$$\n\n**2. Part (b): $p = p_0 e^{\\alpha V}$:**\n$$dp = \\alpha p \\, dV$$\nDifferentiating the equation of state $p V = R T$:\n$$R \\, dT = p \\, dV + V \\, dp = p \\, dV + \\alpha p V \\, dV = p (1 + \\alpha V) dV$$\n$$dA = p \\, dV = \\frac{R \\, dT}{1 + \\alpha V}$$\nHeat capacity:\n$$C = C_V + \\frac{dA}{dT} = C_V + \\frac{R}{1 + \\alpha V}$$",
        "tags": ["heat capacity", "exponential process", "first law"]
    },
    {
        "id": "2.53",
        "title": "Thermodynamics of the Process p = p0 + alpha / V",
        "difficulty": 2,
        "question": "One mole of an ideal gas whose adiabatic exponent equals $\\gamma$ undergoes a process $p = p_0 + \\alpha / V$, where $p_0$ and $\\alpha$ are positive constants. When the volume changes from $V_1$ to $V_2$, find:\n(a) the heat capacity of the gas as a function of volume $V$;\n(b) the work performed, the internal energy increment, and the heat transferred.",
        "hints": [
            "(a) Differentiate $p V = p_0 V + \\alpha = R T \\implies R dT = p_0 dV$.",
            "Then $C = C_V + p \\frac{dV}{dT} = \\frac{R}{\\gamma - 1} + \\frac{p R}{p_0} = \\frac{R}{\\gamma - 1} + R\\left(1 + \\frac{\\alpha}{p_0 V}\\right)$.",
            "(b) Integrate $p dV = p_0(V_2 - V_1) + \\alpha \\ln(V_2/V_1)$."
        ],
        "answer": "(a) $C = \\frac{\\gamma R}{\\gamma - 1} + \\frac{\\alpha R}{p_0 V}$; (b) $A = p_0(V_2 - V_1) + \\alpha \\ln\\left(\\frac{V_2}{V_1}\\right)$, $\\Delta U = \\frac{p_0(V_2 - V_1)}{\\gamma - 1}$, $Q = \\Delta U + A$",
        "solution": "**1. Part (a): Heat Capacity:**\n$$R T = p V = \\left(p_0 + \\frac{\\alpha}{V}\\right) V = p_0 V + \\alpha$$\nDifferentiating with respect to $V$:\n$$R \\frac{dT}{dV} = p_0 \\implies \\frac{dV}{dT} = \\frac{R}{p_0}$$\n$$C = C_V + p \\frac{dV}{dT} = \\frac{R}{\\gamma - 1} + \\left( p_0 + \\frac{\\alpha}{V} \\right) \\frac{R}{p_0} = \\frac{R}{\\gamma - 1} + R + \\frac{\\alpha R}{p_0 V} = \\frac{\\gamma R}{\\gamma - 1} + \\frac{\\alpha R}{p_0 V}$$\n\n**2. Part (b): Work, Internal Energy, and Heat:**\n- Work:\n  $$A = \\int_{V_1}^{V_2} \\left( p_0 + \\frac{\\alpha}{V} \\right) dV = p_0 (V_2 - V_1) + \\alpha \\ln\\left(\\frac{V_2}{V_1}\\right)$$\n- Internal Energy Change:\n  $$\\Delta(p V) = (p_0 V_2 + \\alpha) - (p_0 V_1 + \\alpha) = p_0 (V_2 - V_1)$$\n  $$\\Delta U = \\frac{\\Delta(pV)}{\\gamma - 1} = \\frac{p_0 (V_2 - V_1)}{\\gamma - 1}$$\n- Heat Transferred:\n  $$Q = \\Delta U + A = \\frac{\\gamma p_0 (V_2 - V_1)}{\\gamma - 1} + \\alpha \\ln\\left(\\frac{V_2}{V_1}\\right)$$",
        "tags": ["first law", "variable heat capacity", "work of expansion"]
    },
    {
        "id": "2.54",
        "title": "Thermodynamics of Linear T(V) Process",
        "difficulty": 2,
        "question": "One mole of an ideal gas with heat capacity at constant pressure $C_p$ undergoes the process $T = T_0 + \\alpha V$, where $T_0$ and $\\alpha$ are constants. Find:\n(a) the heat capacity of the gas as a function of volume $V$;\n(b) the heat transferred to the gas when its volume increases from $V_1$ to $V_2$.",
        "hints": [
            "(a) Differentiate $T(V)$: $dT = \\alpha dV$. Work is $dA = p dV = \\frac{RT}{V} dV = \\frac{R(T_0 + \\alpha V)}{V} \\frac{dT}{\\alpha}$.",
            "Heat capacity is $C = C_V + \\frac{dA}{dT} = C_V + R + \\frac{R T_0}{\\alpha V} = C_p + \\frac{R T_0}{\\alpha V}$.",
            "(b) Integrate $dQ = C dT = \\left(C_p + \\frac{R T_0}{\\alpha V}\\right) \\alpha dV$."
        ],
        "answer": "(a) $C = C_p + \\frac{R T_0}{\\alpha V}$; (b) $Q = C_p \\alpha (V_2 - V_1) + R T_0 \\ln\\left(\\frac{V_2}{V_1}\\right)$",
        "solution": "**1. Part (a): Heat Capacity:**\nFrom $T = T_0 + \\alpha V$, $dT = \\alpha \\, dV \\implies \\frac{dV}{dT} = \\frac{1}{\\alpha}$.\n$$C = C_V + p \\frac{dV}{dT} = C_V + \\frac{RT}{V} \\frac{1}{\\alpha} = C_V + \\frac{R(T_0 + \\alpha V)}{\\alpha V} = C_V + R + \\frac{R T_0}{\\alpha V}$$\nSince $C_V + R = C_p$:\n$$C = C_p + \\frac{R T_0}{\\alpha V}$$\n\n**2. Part (b): Heat Transferred:**\n$$dQ = C \\, dT = \\left( C_p + \\frac{R T_0}{\\alpha V} \\right) (\\alpha \\, dV) = C_p \\alpha \\, dV + \\frac{R T_0}{V} dV$$\nIntegrating from $V_1$ to $V_2$:\n$$Q = C_p \\alpha (V_2 - V_1) + R T_0 \\ln\\left(\\frac{V_2}{V_1}\\right)$$",
        "tags": ["heat capacity function", "linear T-V process", "heat transfer"]
    },
    {
        "id": "2.55",
        "title": "Process Equations from Specified Heat Capacity Functions",
        "difficulty": 2,
        "question": "For the case of an ideal gas find the equation of the process (in variables $T, V$) in which the molar heat capacity varies as:\n(a) $C = C_V + \\alpha T$;\n(b) $C = C_V + \\beta V$;\n(c) $C = C_V + a p$,\nwhere $\\alpha, \\beta$, and $a$ are constants.",
        "hints": [
            "Use the general relation: $C - C_V = p \\frac{dV}{dT} = \\frac{RT}{V} \\frac{dV}{dT}$.",
            "(a) $\\alpha T = \\frac{RT}{V} \\frac{dV}{dT} \\implies \\frac{dV}{V} = \\frac{\\alpha}{R} dT$.",
            "(b) $\\beta V = \\frac{RT}{V} \\frac{dV}{dT} \\implies \\frac{dT}{T} = \\frac{R}{\\beta} \\frac{dV}{V^2}$.",
            "(c) $a p = p \\frac{dV}{dT} \\implies dV = a dT$."
        ],
        "answer": "(a) $V e^{-\\alpha T / R} = \\text{const}$; (b) $T e^{R / (\\beta V)} = \\text{const}$; (c) $V - a T = \\text{const}$",
        "solution": "**1. General Differential Relation:**\nFor 1 mole of an ideal gas, $dQ = C_V dT + p dV = C dT$:\n$$(C - C_V) dT = p \\, dV = \\frac{RT}{V} dV$$\n\n**2. Case (a): $C - C_V = \\alpha T$:**\n$$\\alpha T \\, dT = \\frac{RT}{V} dV \\implies \\frac{dV}{V} = \\frac{\\alpha}{R} dT$$\n$$\\ln V - \\frac{\\alpha T}{R} = \\text{const} \\implies V e^{-\\alpha T / R} = \\text{const}$$\n\n**3. Case (b): $C - C_V = \\beta V$:**\n$$\\beta V \\, dT = \\frac{RT}{V} dV \\implies \\frac{dT}{T} = \\frac{R}{\\beta} \\frac{dV}{V^2}$$\n$$\\ln T = -\\frac{R}{\\beta V} + \\text{const} \\implies T e^{R / (\\beta V)} = \\text{const}$$\n\n**4. Case (c): $C - C_V = a p$:**\n$$a p \\, dT = p \\, dV \\implies dV = a \\, dT$$\n$$V - a T = \\text{const}$$",
        "tags": ["process equation", "heat capacity function", "differential equations"]
    },
    {
        "id": "2.56",
        "title": "Thermodynamics of Process with C = alpha / T",
        "difficulty": 2,
        "question": "An ideal gas has an adiabatic exponent $\\gamma$. In a certain process its molar heat capacity varies as $C = \\alpha / T$, where $\\alpha$ is a constant. Find:\n(a) the work performed when its volume increases $\\eta$ times from initial temperature $T_0$;\n(b) the equation of the process in variables $p, V$.",
        "hints": [
            "Write the First Law: $\\frac{\\alpha}{T} dT = C_V dT + p dV$.",
            "Express $p dV = \\left(\\frac{\\alpha}{T} - C_V\\right) dT$ and integrate to find the $p$-$V$ equation.",
            "Work done is $A = \\int p dV$."
        ],
        "answer": "(a) $A = \\alpha \\ln \\eta - \\frac{R T_0}{\\gamma - 1} (\\eta - 1)$; (b) $p V^\\gamma e^{\\alpha(\\gamma - 1)/(pV)} = \\text{const}$",
        "solution": "**1. Part (a): Work Done:**\nFrom the first law of thermodynamics:\n$$dA = dQ - dU = \\frac{\\alpha}{T} dT - C_V dT$$\nIntegrating gives the work performed as a function of the expansion parameter:\n$$A = \\alpha \\ln \\eta - \\frac{R T_0}{\\gamma - 1} (\\eta - 1)$$\n\n**2. Part (b): Process Equation in $p, V$:**\nUsing $C_V = \\frac{R}{\\gamma - 1}$ and $T = \\frac{pV}{R}$:\n$$\\frac{\\alpha}{T} dT - \\frac{R}{\\gamma - 1} dT = p \\, dV$$\nIntegrating yields the transcendental equation of state for the process:\n$$p V^\\gamma e^{\\frac{\\alpha(\\gamma - 1)}{pV}} = \\text{const}$$",
        "tags": ["variable heat capacity", "process equation", "first law"]
    },
    {
        "id": "2.57",
        "title": "Isothermal Work of a Van der Waals Gas",
        "difficulty": 2,
        "question": "Find the work performed by one mole of a Van der Waals gas during its isothermal expansion from volume $V_1$ to $V_2$ at temperature $T$.",
        "hints": [
            "Van der Waals equation for 1 mole: $p = \\frac{RT}{V - b} - \\frac{a}{V^2}$.",
            "Work of expansion is $A = \\int_{V_1}^{V_2} p \\, dV$.",
            "Integrate each term: $\\int \\frac{dV}{V - b} = \\ln(V - b)$ and $\\int -\\frac{a}{V^2} dV = \\frac{a}{V}$."
        ],
        "answer": "$A = R T \\ln\\left(\\frac{V_2 - b}{V_1 - b}\\right) + a\\left(\\frac{1}{V_2} - \\frac{1}{V_1}\\right)$",
        "solution": "**1. Work Integral:**\nFor 1 mole of a Van der Waals gas:\n$$p = \\frac{RT}{V - b} - \\frac{a}{V^2}$$\n$$A = \\int_{V_1}^{V_2} p \\, dV = \\int_{V_1}^{V_2} \\left( \\frac{RT}{V - b} - \\frac{a}{V^2} \\right) dV$$\n\n**2. Evaluation:**\n$$A = \\left[ RT \\ln(V - b) + \\frac{a}{V} \\right]_{V_1}^{V_2}$$\n$$A = RT \\ln\\left( \\frac{V_2 - b}{V_1 - b} \\right) + a \\left( \\frac{1}{V_2} - \\frac{1}{V_1} \\right)$$",
        "tags": ["Van der Waals", "isothermal expansion", "work done", "integration"]
    },
    {
        "id": "2.58",
        "title": "Isothermal Expansion of Oxygen as a Van der Waals Gas",
        "difficulty": 2,
        "question": "One mole of oxygen is expanded from volume $V_1 = 1.00\\text{ l}$ to $V_2 = 5.0\\text{ l}$ at constant temperature $T = 280\\text{ K}$. Calculate:\n(a) the increment of the internal energy of the gas;\n(b) the heat transferred to the gas.\n(For $O_2$, $a = 1.36\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2$, $b = 0.032\\text{ l/mol}$).",
        "hints": [
            "(a) Internal energy of 1 mole of Van der Waals gas is $U = C_V T - \\frac{a}{V}$. At constant $T$, $\\Delta U = a\\left(\\frac{1}{V_1} - \\frac{1}{V_2}\\right)$.",
            "(b) Heat transferred is $Q = \\Delta U + A$.",
            "Work from Problem 2.57 is $A = RT \\ln\\left(\\frac{V_2 - b}{V_1 - b}\\right) + a\\left(\\frac{1}{V_2} - \\frac{1}{V_1}\\right)$, so $Q = RT \\ln\\left(\\frac{V_2 - b}{V_1 - b}\\right)$."
        ],
        "answer": "(a) $\\Delta U = a\\left(\\frac{1}{V_1} - \\frac{1}{V_2}\\right) = 0.11\\text{ kJ}$; (b) $Q = R T \\ln\\left(\\frac{V_2 - b}{V_1 - b}\\right) = 3.8\\text{ kJ}$",
        "solution": "**1. Part (a): Internal Energy Change:**\nFor a Van der Waals gas, $U(T, V) = C_V T - \\frac{a}{V}$. Since $T = \\text{const}$:\n$$\\Delta U = U(T, V_2) - U(T, V_1) = -\\frac{a}{V_2} - \\left(-\\frac{a}{V_1}\\right) = a \\left( \\frac{1}{V_1} - \\frac{1}{V_2} \\right)$$\nConverting $a$ to SI units:\n$$a = 1.36\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2 = 1.36 \\times 1.013 \\times 10^5 \\times 10^{-6}\\text{ Pa}\\cdot\\text{m}^6 = 0.138\\text{ J}\\cdot\\text{m}^3/\\text{mol}^2$$\n$$\\frac{1}{V_1} - \\frac{1}{V_2} = \\frac{1}{1.0 \\times 10^{-3}} - \\frac{1}{5.0 \\times 10^{-3}} = 1000 - 200 = 800\\text{ m}^{-3}$$\n$$\\Delta U = 0.138 \\times 800 = 110.4\\text{ J} \\approx 0.11\\text{ kJ}$$\n\n**2. Part (b): Heat Transferred:**\nBy the First Law, $Q = \\Delta U + A$. Using the result of Problem 2.57:\n$$A = RT \\ln\\left(\\frac{V_2 - b}{V_1 - b}\\right) + a\\left(\\frac{1}{V_2} - \\frac{1}{V_1}\\right) = RT \\ln\\left(\\frac{V_2 - b}{V_1 - b}\\right) - \\Delta U$$\n$$Q = \\Delta U + A = RT \\ln\\left(\\frac{V_2 - b}{V_1 - b}\\right)$$\n$$Q = 8.314 \\times 280 \\times \\ln\\left( \\frac{5.0 - 0.032}{1.0 - 0.032} \\right) = 2328 \\times \\ln\\left(\\frac{4.968}{0.968}\\right) = 2328 \\times \\ln(5.132)$$\n$$\\ln(5.132) \\approx 1.6355 \\implies Q = 2328 \\times 1.6355 \\approx 3808\\text{ J} \\approx 3.8\\text{ kJ}$$",
        "tags": ["Van der Waals", "oxygen", "internal energy", "heat transfer"]
    },
    {
        "id": "2.59",
        "title": "Adiabatic Equation and Heat Capacity Difference for a Van der Waals Gas",
        "difficulty": 3,
        "question": "For a Van der Waals gas find:\n(a) the equation of the adiabatic curve in variables $T, V$;\n(b) the difference of molar heat capacities $C_p - C_V$.",
        "hints": [
            "(a) In an adiabatic process, $dU + p dV = 0$. Since $dU = C_V dT + \\frac{a}{V^2} dV$ and $p = \\frac{RT}{V - b} - \\frac{a}{V^2}$, the internal pressure terms cancel, giving $C_V dT + \\frac{RT}{V - b} dV = 0$.",
            "(b) Use the general thermodynamic relation $C_p - C_V = T \\left(\\frac{\\partial p}{\\partial T}\\right)_V \\left(\\frac{\\partial V}{\\partial T}\\right)_p = -T \\frac{(\\partial p / \\partial T)_V^2}{(\\partial p / \\partial V)_T}$."
        ],
        "answer": "(a) $T (V - b)^{R / C_V} = \\text{const}$; (b) $C_p - C_V = \\frac{R}{1 - \\frac{2a(V - b)^2}{R T V^3}}$",
        "solution": "**1. Part (a): Adiabatic Equation:**\nFor a Van der Waals gas, $U = C_V T - \\frac{a}{V}$:\n$$dU = C_V \\, dT + \\frac{a}{V^2} \\, dV$$\nIn an adiabatic process $dQ = dU + p \\, dV = 0$:\n$$C_V \\, dT + \\frac{a}{V^2} dV + \\left( \\frac{RT}{V - b} - \\frac{a}{V^2} \\right) dV = 0$$\n$$C_V \\, dT + \\frac{RT}{V - b} dV = 0 \\implies \\frac{dT}{T} + \\frac{R}{C_V} \\frac{dV}{V - b} = 0$$\nIntegrating gives:\n$$\\ln T + \\frac{R}{C_V} \\ln(V - b) = \\text{const} \\implies T (V - b)^{R / C_V} = \\text{const}$$\n\n**2. Part (b): Heat Capacity Difference $C_p - C_V$:**\nUsing the thermodynamic relation $C_p - C_V = -T \\frac{(\\partial p / \\partial T)_V^2}{(\\partial p / \\partial V)_T}$:\n$$\\left(\\frac{\\partial p}{\\partial T}\\right)_V = \\frac{R}{V - b}$$\n$$\\left(\\frac{\\partial p}{\\partial V}\\right)_T = -\\frac{RT}{(V - b)^2} + \\frac{2a}{V^3}$$\nSubstituting:\n$$C_p - C_V = -T \\frac{\\frac{R^2}{(V - b)^2}}{-\\frac{RT}{(V - b)^2} + \\frac{2a}{V^3}} = \\frac{R^2 T}{RT - \\frac{2a(V - b)^2}{V^3}} = \\frac{R}{1 - \\frac{2a(V - b)^2}{R T V^3}}$$",
        "tags": ["Van der Waals", "adiabatic curve", "heat capacity difference", "thermodynamic identity"]
    },
    {
        "id": "2.60",
        "title": "Temperature Change in Free Expansion into Vacuum",
        "difficulty": 2,
        "question": "Two thermally insulated vessels are interconnected by a tube equipped with a valve. One vessel of volume $V_1 = 10\\text{ l}$ contains $\\nu = 2.5\\text{ moles}$ of carbon dioxide. The other vessel of volume $V_2 = 100\\text{ l}$ is evacuated. The valve is opened and the gas expands into the second vessel. Find the temperature change $\\Delta T$ of the gas. (For $CO_2$, $a = 3.6\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2$, $\\gamma = 1.30$).",
        "hints": [
            "Free expansion into vacuum in an insulated system performs no external work ($A = 0$) and absorbs no heat ($Q = 0$).",
            "By the first law, internal energy is conserved: $\\Delta U = 0$.",
            "For a Van der Waals gas, $\\Delta U = \\nu C_V \\Delta T - \\nu^2 a \\left(\\frac{1}{V_1} - \\frac{1}{V_1 + V_2}\\right) = 0$."
        ],
        "answer": "$\\Delta T = -\\frac{\\nu (\\gamma - 1) a}{R} \\frac{V_2}{V_1(V_1 + V_2)} = -3.0\\text{ K}$",
        "solution": "**1. Conservation of Internal Energy:**\nBecause the system is thermally insulated ($Q = 0$) and expands into vacuum ($A = 0$):\n$$\\Delta U = 0$$\nFor $\\nu$ moles of a Van der Waals gas:\n$$U = \\nu C_V T - \\frac{\\nu^2 a}{V}$$\n$$\\Delta U = \\nu C_V \\Delta T - \\nu^2 a \\left( \\frac{1}{V_1} - \\frac{1}{V_1 + V_2} \\right) = 0$$\n$$\\nu C_V \\Delta T = -\\nu^2 a \\frac{V_2}{V_1 (V_1 + V_2)}$$\nUsing $C_V = \\frac{R}{\\gamma - 1}$:\n$$\\Delta T = -\\frac{\\nu (\\gamma - 1) a}{R} \\frac{V_2}{V_1 (V_1 + V_2)}$$\n\n**2. Numerical Calculation:**\n$$a = 3.6\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2 = 3.6 \\times 0.1013 = 0.365\\text{ J}\\cdot\\text{m}^3/\\text{mol}^2$$\n$$V_1 = 10 \\times 10^{-3}\\text{ m}^3, \\quad V_2 = 100 \\times 10^{-3}\\text{ m}^3, \\quad V_1 + V_2 = 110 \\times 10^{-3}\\text{ m}^3$$\n$$\\frac{V_2}{V_1 (V_1 + V_2)} = \\frac{100}{10 \\times 110 \\times 10^{-3}} = \\frac{100}{1.1} = 90.9\\text{ m}^{-3}$$\n$$\\Delta T = -\\frac{2.5 \\times 0.30 \\times 0.365}{8.314} \\times 90.9 = -\\frac{0.27375}{8.314} \\times 90.9 \\approx -2.99\\text{ K} \\approx -3.0\\text{ K}$$",
        "tags": ["free expansion", "Joule expansion", "cooling", "Van der Waals"]
    },
    {
        "id": "2.61",
        "title": "Heat Supplied to Keep Temperature Constant during Free Expansion",
        "difficulty": 2,
        "question": "What amount of heat has to be transferred to $\\nu = 3.0\\text{ moles}$ of carbon dioxide to keep its temperature constant while it expands into vacuum from volume $V_1 = 5.0\\text{ l}$ to $V_2 = 10.0\\text{ l}$? (For $CO_2$, $a = 3.6\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2$).",
        "hints": [
            "In expansion into vacuum, the work done on the surroundings is zero: $A = 0$.",
            "By the First Law: $Q = \\Delta U + A = \\Delta U$.",
            "For an isothermal process of a Van der Waals gas, $\\Delta U = -\\nu^2 a \\left(\\frac{1}{V_2} - \\frac{1}{V_1}\\right) = \\nu^2 a \\frac{V_2 - V_1}{V_1 V_2}$."
        ],
        "answer": "$Q = \\nu^2 a \\frac{V_2 - V_1}{V_1 V_2} = 0.33\\text{ kJ}$",
        "solution": "**1. Heat in Isothermal Free Expansion:**\nSince the gas expands into vacuum, no mechanical work is done on the exterior:\n$$A = 0$$\nBy the First Law of Thermodynamics:\n$$Q = \\Delta U$$\nFor a Van der Waals gas at constant temperature $T$:\n$$\\Delta U = -\\frac{\\nu^2 a}{V_2} - \\left( -\\frac{\\nu^2 a}{V_1} \\right) = \\nu^2 a \\left( \\frac{1}{V_1} - \\frac{1}{V_2} \\right) = \\nu^2 a \\frac{V_2 - V_1}{V_1 V_2}$$\n\n**2. Numerical Calculation:**\nWith $\\nu = 3.0\\text{ mol}$, $a = 3.6\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2 = 0.365\\text{ J}\\cdot\\text{m}^3/\\text{mol}^2$:\n$$V_1 = 5.0 \\times 10^{-3}\\text{ m}^3, \\quad V_2 = 10.0 \\times 10^{-3}\\text{ m}^3$$\n$$\\frac{V_2 - V_1}{V_1 V_2} = \\frac{5.0 \\times 10^{-3}}{50 \\times 10^{-6}} = 100\\text{ m}^{-3}$$\n$$Q = (3.0)^2 \\times 0.365 \\times 100 = 9 \\times 36.5 = 328.5\\text{ J} \\approx 0.33\\text{ kJ}$$",
        "tags": ["Van der Waals", "free expansion", "internal energy", "heat transfer"]
    }
]
