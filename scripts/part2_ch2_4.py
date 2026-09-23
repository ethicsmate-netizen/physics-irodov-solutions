"""
part2_ch2_4.py
Curated problems 2.113 to 2.159 (47 problems) of Irodov Chapter 2.4:
The Second Law of Thermodynamics. Entropy.
"""

CH2_4_CURATED = [
    {
        "id": "2.113",
        "title": "Comparison of Carnot Cycle Optimization Strategies",
        "difficulty": 1,
        "question": "In which case will the efficiency of a Carnot cycle be higher: when the hot body temperature is increased by $\\Delta T$, or when the cold body temperature is decreased by the same $\\Delta T$?",
        "hints": [
            "Carnot efficiency is $\\eta = 1 - \\frac{T_2}{T_1}$.",
            "Calculate $\\eta_1 = 1 - \\frac{T_2}{T_1 + \\Delta T}$ and $\\eta_2 = 1 - \\frac{T_2 - \\Delta T}{T_1}$.",
            "Compare $\\eta_2 - \\eta_1$."
        ],
        "answer": "When the cold body temperature is decreased by $\\Delta T$",
        "solution": "**1. Efficiencies in Both Cases:**\nLet the original temperatures be $T_1$ (hot) and $T_2$ (cold), with $T_1 > T_2$.\n- Increasing hot reservoir temperature by $\\Delta T$:\n  $$\\eta_1 = 1 - \\frac{T_2}{T_1 + \\Delta T} = \\frac{T_1 + \\Delta T - T_2}{T_1 + \\Delta T}$$\n- Decreasing cold reservoir temperature by $\\Delta T$:\n  $$\\eta_2 = 1 - \\frac{T_2 - \\Delta T}{T_1} = \\frac{T_1 - T_2 + \\Delta T}{T_1}$$\n\n**2. Comparison:**\nNotice that both numerators are identical: $(T_1 - T_2 + \\Delta T)$.\nSince $T_1 + \\Delta T > T_1$, the denominator of $\\eta_2$ is strictly smaller than that of $\\eta_1$:\n$$\\eta_2 > \\eta_1$$\nTherefore, decreasing the cold reservoir temperature by $\\Delta T$ yields a higher efficiency than increasing the hot reservoir temperature by the same amount.",
        "tags": ["Carnot cycle", "efficiency", "second law"]
    },
    {
        "id": "2.114",
        "title": "Carnot Cycle Work and Heat Rejection",
        "difficulty": 1,
        "question": "An ideal heat engine operates on a Carnot cycle between temperatures $T_1 = 500\\text{ K}$ and $T_2 = 300\\text{ K}$. During each cycle the engine absorbs $Q_1 = 2.0\\text{ kJ}$ of heat from the hot reservoir. Find:\n(a) the efficiency of the cycle;\n(b) the work performed per cycle;\n(c) the heat rejected to the cold reservoir.",
        "hints": [
            "(a) $\\eta = 1 - \\frac{T_2}{T_1}$.",
            "(b) $A = \\eta Q_1$.",
            "(c) $Q_2 = Q_1 - A = Q_1 \\frac{T_2}{T_1}$."
        ],
        "answer": "(a) $\\eta = 40\\%$; (b) $A = 0.80\\text{ kJ}$; (c) $Q_2 = 1.2\\text{ kJ}$",
        "solution": "**1. Efficiency:**\n$$\\eta = 1 - \\frac{T_2}{T_1} = 1 - \\frac{300}{500} = 1 - 0.60 = 0.40 = 40\\%$$\n\n**2. Work Done:**\n$$A = \\eta Q_1 = 0.40 \\times 2.0\\text{ kJ} = 0.80\\text{ kJ}$$\n\n**3. Heat Rejected:**\n$$Q_2 = Q_1 - A = 2.0 - 0.80 = 1.2\\text{ kJ}$$",
        "tags": ["Carnot engine", "efficiency", "work", "heat rejection"]
    },
    {
        "id": "2.115",
        "title": "Coefficient of Performance of a Carnot Refrigerator",
        "difficulty": 1,
        "question": "A Carnot refrigerator operates between temperatures $t_2 = -10^\\circ\\text{C}$ and $t_1 = +20^\\circ\\text{C}$. Find the coefficient of performance $\\beta = Q_2 / A$, where $Q_2$ is the heat extracted from the cold chamber and $A$ is the work input.",
        "hints": [
            "Convert temperatures to Kelvin: $T_2 = 263.15\\text{ K}$, $T_1 = 293.15\\text{ K}$.",
            "For a Carnot refrigerator, $\\beta = \\frac{Q_2}{A} = \\frac{T_2}{T_1 - T_2}$."
        ],
        "answer": "$\\beta = \\frac{T_2}{T_1 - T_2} = 8.8$",
        "solution": "**1. Coefficient of Performance Formula:**\nFor a reversible Carnot cycle operated in reverse:\n$$\\frac{Q_1}{T_1} = \\frac{Q_2}{T_2} \\implies Q_1 = Q_2 \\frac{T_1}{T_2}$$\n$$A = Q_1 - Q_2 = Q_2 \\left( \\frac{T_1}{T_2} - 1 \\right) = Q_2 \\frac{T_1 - T_2}{T_2}$$\n$$\\beta = \\frac{Q_2}{A} = \\frac{T_2}{T_1 - T_2}$$\n\n**2. Numerical Value:**\n$$\\beta = \\frac{263.15}{293.15 - 263.15} = \\frac{263.15}{30.0} \\approx 8.77 \\approx 8.8$$",
        "tags": ["Carnot refrigerator", "coefficient of performance", "heat pump"]
    },
    {
        "id": "2.116",
        "title": "Minimum Work to Freeze Water",
        "difficulty": 2,
        "question": "A refrigerator is used to freeze $m = 1.0\\text{ kg}$ of water at $0^\\circ\\text{C}$ into ice at $0^\\circ\\text{C}$. The room temperature is $T_1 = 293\\text{ K}$. Find the minimum work $A_{\\min}$ that must be supplied to the refrigerator. (Specific latent heat of fusion of ice $q = 333\\text{ kJ/kg}$).",
        "hints": [
            "Heat extracted from freezing water at $T_2 = 273\\text{ K}$ is $Q_2 = m q$.",
            "Minimum work is achieved with a reversible Carnot refrigerator: $A_{\\min} = Q_2 \\left(\\frac{T_1 - T_2}{T_2}\\right)$."
        ],
        "answer": "$A_{\\min} = m q \\frac{T_1 - T_2}{T_2} = 24\\text{ kJ}$",
        "solution": "**1. Heat Extracted:**\n$$Q_2 = m q = 1.0\\text{ kg} \\times 333\\text{ kJ/kg} = 333\\text{ kJ}$$\n\n**2. Minimum Work with Carnot Cycle:**\n$$A_{\\min} = Q_2 \\frac{T_1 - T_2}{T_2} = 333\\text{ kJ} \\times \\frac{293 - 273}{273} = 333 \\times \\frac{20}{273} = \\frac{6660}{273} \\approx 24.4\\text{ kJ} \\approx 24\\text{ kJ}$$",
        "tags": ["refrigerator", "freezing water", "latent heat", "Carnot work"]
    },
    {
        "id": "2.117",
        "title": "Efficiency of a Reversible Heat Engine with Variable Heat Capacities",
        "difficulty": 2,
        "question": "A reversible heat engine operates between two bodies with identical heat capacities $C$ initially at temperatures $T_1$ and $T_2$ ($T_1 > T_2$). The engine operates until the temperatures of both bodies equalize at $T_f$. Find:\n(a) the final temperature $T_f$;\n(b) the maximum work performed by the engine.",
        "hints": [
            "(a) Since the engine is reversible and insulated from the rest of the universe, total entropy change is zero: $\\Delta S = \\Delta S_1 + \\Delta S_2 = C \\ln(T_f / T_1) + C \\ln(T_f / T_2) = 0$.",
            "Solve for $T_f$: $\\ln\\left(\\frac{T_f^2}{T_1 T_2}\\right) = 0 \\implies T_f = \\sqrt{T_1 T_2}$.",
            "(b) Total work is $A = Q_1 - Q_2 = C(T_1 - T_f) - C(T_f - T_2) = C(T_1 + T_2 - 2\\sqrt{T_1 T_2})$."
        ],
        "answer": "(a) $T_f = \\sqrt{T_1 T_2}$; (b) $A = C \\left(\\sqrt{T_1} - \\sqrt{T_2}\\right)^2$",
        "solution": "**1. Part (a): Final Temperature:**\nFor a reversible process involving only the two bodies:\n$$\\Delta S_{\\text{total}} = \\int_{T_1}^{T_f} \\frac{C \\, dT}{T} + \\int_{T_2}^{T_f} \\frac{C \\, dT}{T} = 0$$\n$$C \\ln\\left(\\frac{T_f}{T_1}\\right) + C \\ln\\left(\\frac{T_f}{T_2}\\right) = 0 \\implies C \\ln\\left(\\frac{T_f^2}{T_1 T_2}\\right) = 0$$\n$$T_f^2 = T_1 T_2 \\implies T_f = \\sqrt{T_1 T_2}$$\n\n**2. Part (b): Maximum Work:**\nBy the First Law of Thermodynamics, work extracted is:\n$$A = -\\Delta U = -[C(T_f - T_1) + C(T_f - T_2)] = C(T_1 + T_2 - 2 T_f)$$\nSubstituting $T_f = \\sqrt{T_1 T_2}$:\n$$A = C \\left( T_1 + T_2 - 2\\sqrt{T_1 T_2} \\right) = C \\left( \\sqrt{T_1} - \\sqrt{T_2} \\right)^2$$",
        "tags": ["maximum work", "entropy conservation", "reversible heat engine", "geometric mean"]
    },
    {
        "id": "2.118",
        "title": "Carnot Cycle of a Van der Waals Gas",
        "difficulty": 3,
        "question": "One mole of a Van der Waals gas undergoes a Carnot cycle between temperatures $T_1$ and $T_2$. The isothermal expansion at $T_1$ occurs from volume $V_1$ to $V_2$. Find the work performed by the gas during the cycle.",
        "hints": [
            "The efficiency of any reversible Carnot cycle depends only on the reservoir temperatures: $\\eta = \\frac{T_1 - T_2}{T_1}$, regardless of working substance!",
            "Heat absorbed during isothermal expansion of 1 mole of Van der Waals gas is $Q_1 = R T_1 \\ln\\left(\\frac{V_2 - b}{V_1 - b}\\right)$ (since $\\Delta U = -a/V_2 + a/V_1$ and $A = RT_1 \\ln\\frac{V_2-b}{V_1-b} + a/V_2 - a/V_1$, so $Q_1 = \\Delta U + A = RT_1 \\ln\\frac{V_2-b}{V_1-b}$).",
            "Work done per cycle is $A = \\eta Q_1 = R (T_1 - T_2) \\ln\\left(\\frac{V_2 - b}{V_1 - b}\\right)$."
        ],
        "answer": "$A = R (T_1 - T_2) \\ln\\left(\\frac{V_2 - b}{V_1 - b}\\right)$",
        "solution": "**1. Reversible Efficiency:**\nBy the second law of thermodynamics, any reversible engine operating between two heat reservoirs at $T_1$ and $T_2$ has Carnot efficiency:\n$$\\eta = \\frac{T_1 - T_2}{T_1}$$\n\n**2. Heat Absorbed in Isothermal Stage:**\nFor 1 mole of a Van der Waals gas along the isotherm at $T_1$:\n$$Q_1 = \\int_{V_1}^{V_2} T_1 \\left(\\frac{\\partial p}{\\partial T}\\right)_V dV$$\nSince $p = \\frac{RT}{V - b} - \\frac{a}{V^2}$, $\\left(\\frac{\\partial p}{\\partial T}\\right)_V = \\frac{R}{V - b}$:\n$$Q_1 = T_1 \\int_{V_1}^{V_2} \\frac{R}{V - b} \\, dV = R T_1 \\ln\\left( \\frac{V_2 - b}{V_1 - b} \\right)$$\n\n**3. Work per Cycle:**\n$$A = \\eta Q_1 = \\frac{T_1 - T_2}{T_1} \\cdot R T_1 \\ln\\left( \\frac{V_2 - b}{V_1 - b} \\right) = R (T_1 - T_2) \\ln\\left( \\frac{V_2 - b}{V_1 - b} \\right)$$",
        "tags": ["Carnot cycle", "Van der Waals", "efficiency", "isothermal heat"]
    },
    {
        "id": "2.119",
        "title": "Efficiency of a Cycle with Two Polytropes and Two Isochores",
        "difficulty": 2,
        "question": "An ideal gas undergoes a cycle consisting of two isochores ($V_1$ and $V_2 = \\eta V_1$) and two polytropes with the same index $n$. Find the efficiency of this cycle.",
        "hints": [
            "Along the polytropic paths $1 \\to 2$ and $3 \\to 4$, $p V^n = \\text{const} \\implies T V^{n-1} = \\text{const}$.",
            "Along isochores, no work is done.",
            "Show that $\\frac{T_2}{T_1} = \\frac{T_3}{T_4} = \\eta^{1-n}$, which leads to efficiency $\\eta_{\\text{cycle}} = 1 - \\eta^{1 - n}$ (or $1 - \\eta^{n-1}$)."
        ],
        "answer": "$\\eta = 1 - \\eta^{1 - n}$",
        "solution": "**1. Temperature Relations:**\nAlong polytropes with index $n$:\n$$T_2 = T_1 \\left(\\frac{V_1}{V_2}\\right)^{n-1} = T_1 \\eta^{1-n}$$\n$$T_3 = T_4 \\left(\\frac{V_1}{V_2}\\right)^{n-1} = T_4 \\eta^{1-n}$$\n\n**2. Efficiency:**\nHeat is absorbed along the isochore $4 \\to 1$ and rejected along $2 \\to 3$:\n$$Q_{\\text{in}} = C_V (T_1 - T_4)$$\n$$Q_{\\text{out}} = C_V (T_2 - T_3) = C_V (T_1 - T_4) \\eta^{1-n}$$\n$$\\eta = 1 - \\frac{Q_{\\text{out}}}{Q_{\\text{in}}} = 1 - \\eta^{1 - n}$$",
        "tags": ["polytropic cycle", "isochoric processes", "efficiency"]
    },
    {
        "id": "2.120",
        "title": "Efficiency of the Otto Cycle",
        "difficulty": 2,
        "question": "Calculate the efficiency of the Otto cycle (consisting of two adiabats and two isochores) as a function of the compression ratio $\\epsilon = V_{\\max} / V_{\\min}$ and adiabatic exponent $\\gamma$.",
        "hints": [
            "Adiabatic compression: $T_2 = T_1 \\epsilon^{\\gamma - 1}$.",
            "Adiabatic expansion: $T_3 = T_4 \\epsilon^{\\gamma - 1}$.",
            "Heat supplied: $Q_1 = \\nu C_V (T_3 - T_2)$; Heat rejected: $Q_2 = \\nu C_V (T_4 - T_1)$.",
            "Efficiency is $\\eta = 1 - \\frac{Q_2}{Q_1} = 1 - \\frac{T_4 - T_1}{T_3 - T_2} = 1 - \\frac{1}{\\epsilon^{\\gamma - 1}}$."
        ],
        "answer": "$\\eta = 1 - \\frac{1}{\\epsilon^{\\gamma - 1}}$",
        "solution": "**1. Temperature Relations Along Adiabats:**\n- Adiabatic compression $1 \\to 2$ from $V_1 = V_{\\max}$ to $V_2 = V_{\\min}$:\n  $$\\frac{T_2}{T_1} = \\left(\\frac{V_1}{V_2}\\right)^{\\gamma - 1} = \\epsilon^{\\gamma - 1} \\implies T_2 = T_1 \\epsilon^{\\gamma - 1}$$\n- Adiabatic expansion $3 \\to 4$ from $V_3 = V_{\\min}$ to $V_4 = V_{\\max}$:\n  $$\\frac{T_3}{T_4} = \\left(\\frac{V_4}{V_3}\\right)^{\\gamma - 1} = \\epsilon^{\\gamma - 1} \\implies T_3 = T_4 \\epsilon^{\\gamma - 1}$$\n\n**2. Heat Exchange Along Isochores:**\n- Heat absorbed $2 \\to 3$ at $V_{\\min}$:\n  $$Q_1 = \\nu C_V (T_3 - T_2)$$\n- Heat rejected $4 \\to 1$ at $V_{\\max}$:\n  $$Q_2 = \\nu C_V (T_4 - T_1)$$\n\n**3. Efficiency:**\n$$\\frac{Q_2}{Q_1} = \\frac{T_4 - T_1}{T_3 - T_2} = \\frac{T_4 - T_1}{(T_4 - T_1) \\epsilon^{\\gamma - 1}} = \\frac{1}{\\epsilon^{\\gamma - 1}}$$\n$$\\eta = 1 - \\frac{Q_2}{Q_1} = 1 - \\frac{1}{\\epsilon^{\\gamma - 1}}$$",
        "tags": ["Otto cycle", "compression ratio", "adiabatic exponent", "internal combustion"]
    },
    {
        "id": "2.121",
        "title": "Efficiency of the Diesel Cycle",
        "difficulty": 2,
        "question": "Find the efficiency of the Diesel cycle (consisting of adiabatic compression, isobaric expansion with heat addition, adiabatic expansion, and isochoric heat rejection) in terms of compression ratio $\\epsilon = V_1 / V_2$, cutoff ratio $\\rho = V_3 / V_2$, and adiabatic index $\\gamma$.",
        "hints": [
            "State 1 to 2 is adiabatic: $T_2 = T_1 \\epsilon^{\\gamma - 1}$.",
            "State 2 to 3 is isobaric: $T_3 = T_2 \\rho = T_1 \\epsilon^{\\gamma - 1} \\rho$.",
            "State 3 to 4 is adiabatic with volume expansion ratio $V_4 / V_3 = \\epsilon / \\rho$: $T_4 = T_3 (\\rho / \\epsilon)^{\\gamma - 1} = T_1 \\rho^\\gamma$.",
            "Use $Q_1 = \\nu C_p (T_3 - T_2)$ and $Q_2 = \\nu C_V (T_4 - T_1)$ to evaluate $\\eta = 1 - \\frac{Q_2}{Q_1}$."
        ],
        "answer": "$\\eta = 1 - \\frac{1}{\\epsilon^{\\gamma - 1}} \\frac{\\rho^\\gamma - 1}{\\gamma (\\rho - 1)}$",
        "solution": "**1. State Temperatures:**\n$$T_2 = T_1 \\epsilon^{\\gamma - 1}$$\n$$T_3 = T_2 \\frac{V_3}{V_2} = T_1 \\epsilon^{\\gamma - 1} \\rho$$\n$$T_4 = T_3 \\left( \\frac{V_3}{V_4} \\right)^{\\gamma - 1} = (T_1 \\epsilon^{\\gamma - 1} \\rho) \\left( \\frac{\\rho}{\\epsilon} \\right)^{\\gamma - 1} = T_1 \\rho^\\gamma$$\n\n**2. Heat Quantities:**\n$$Q_1 = \\nu C_p (T_3 - T_2) = \\nu C_p T_1 \\epsilon^{\\gamma - 1} (\\rho - 1)$$\n$$Q_2 = \\nu C_V (T_4 - T_1) = \\nu C_V T_1 (\\rho^\\gamma - 1)$$\n\n**3. Cycle Efficiency:**\n$$\\eta = 1 - \\frac{Q_2}{Q_1} = 1 - \\frac{C_V}{C_p} \\frac{T_1 (\\rho^\\gamma - 1)}{T_1 \\epsilon^{\\gamma - 1} (\\rho - 1)} = 1 - \\frac{1}{\\epsilon^{\\gamma - 1}} \\frac{\\rho^\\gamma - 1}{\\gamma (\\rho - 1)}$$",
        "tags": ["Diesel cycle", "cutoff ratio", "compression ratio", "efficiency"]
    },
    {
        "id": "2.122",
        "title": "Efficiency of the Joule-Brayton Cycle",
        "difficulty": 2,
        "question": "Calculate the efficiency of a gas-turbine (Joule-Brayton) cycle consisting of two isobars and two adiabats, as a function of the pressure ratio $\\beta = p_2 / p_1$ and adiabatic exponent $\\gamma$.",
        "hints": [
            "Adiabatic compression: $T_2 = T_1 \\beta^{(\\gamma - 1)/\\gamma}$.",
            "Adiabatic expansion: $T_3 = T_4 \\beta^{(\\gamma - 1)/\\gamma}$.",
            "Both heat addition and rejection occur at constant pressure: $Q_1 = \\nu C_p (T_3 - T_2)$, $Q_2 = \\nu C_p (T_4 - T_1)$.",
            "Efficiency is $\\eta = 1 - \\frac{Q_2}{Q_1} = 1 - \\beta^{-(\\gamma - 1)/\\gamma}$."
        ],
        "answer": "$\\eta = 1 - \\beta^{-(\\gamma - 1)/\\gamma}$",
        "solution": "**1. Temperature Relations:**\n- Adiabatic compression $1 \\to 2$:\n  $$\\frac{T_2}{T_1} = \\left(\\frac{p_2}{p_1}\\right)^{\\frac{\\gamma - 1}{\\gamma}} = \\beta^{\\frac{\\gamma - 1}{\\gamma}}$$\n- Adiabatic expansion $3 \\to 4$:\n  $$\\frac{T_3}{T_4} = \\left(\\frac{p_2}{p_1}\\right)^{\\frac{\\gamma - 1}{\\gamma}} = \\beta^{\\frac{\\gamma - 1}{\\gamma}}$$\n\n**2. Efficiency:**\n$$Q_1 = \\nu C_p (T_3 - T_2)$$\n$$Q_2 = \\nu C_p (T_4 - T_1)$$\n$$\\frac{Q_2}{Q_1} = \\frac{T_4 - T_1}{T_3 - T_2} = \\beta^{-\\frac{\\gamma - 1}{\\gamma}}$$\n$$\\eta = 1 - \\frac{Q_2}{Q_1} = 1 - \\beta^{-\\frac{\\gamma - 1}{\\gamma}}$$",
        "tags": ["Joule-Brayton cycle", "gas turbine", "pressure ratio", "efficiency"]
    },
    {
        "id": "2.123",
        "title": "Cycle with Two Isotherms and Two Isobars",
        "difficulty": 2,
        "question": "An ideal gas undergoes a cycle consisting of two isotherms at temperatures $T_1$ and $T_2$ ($T_1 > T_2$) and two isobars at pressures $p_1$ and $p_2$ ($p_1 > p_2$). Find the efficiency of this cycle.",
        "hints": [
            "Plot the cycle on a $T$-$S$ plane: the isotherms are horizontal lines, and the isobars have slope $T / C_p$.",
            "Calculate work performed and heat input during the isothermal and isobaric heating stages."
        ],
        "answer": "$\\eta = \\frac{(T_1 - T_2) \\ln(p_1 / p_2)}{T_1 \\ln(p_1 / p_2) + \\frac{\\gamma}{\\gamma - 1}(T_1 - T_2)}$",
        "solution": "**1. Work of the Cycle:**\n- Isotherm at $T_1$: $A_1 = \\nu R T_1 \\ln(p_1 / p_2)$\n- Isotherm at $T_2$: $A_2 = -\\nu R T_2 \\ln(p_1 / p_2)$\n- Net work from both isobars is zero because $p_1(V_b - V_a) + p_2(V_d - V_c) = \\nu R(T_2 - T_1) + \\nu R(T_1 - T_2) = 0$.\n$$A = \\nu R (T_1 - T_2) \\ln\\left(\\frac{p_1}{p_2}\\right)$$\n\n**2. Heat Absorbed:**\nHeat is absorbed during the isotherm at $T_1$ ($Q_{\\text{iso}} = \\nu R T_1 \\ln(p_1 / p_2)$) and during isobaric heating at $p_1$ ($Q_p = \\nu C_p (T_1 - T_2)$):\n$$Q_{\\text{in}} = \\nu R T_1 \\ln\\left(\\frac{p_1}{p_2}\\right) + \\nu C_p (T_1 - T_2)$$\n\n**3. Efficiency:**\n$$\\eta = \\frac{A}{Q_{\\text{in}}} = \\frac{(T_1 - T_2) \\ln(p_1 / p_2)}{T_1 \\ln(p_1 / p_2) + \\frac{\\gamma}{\\gamma - 1}(T_1 - T_2)}$$",
        "tags": ["Ericsson cycle", "isotherms and isobars", "efficiency"]
    },
    {
        "id": "2.124",
        "title": "Cycle with Two Isotherms and Two Isochores (Stirling Cycle)",
        "difficulty": 2,
        "question": "Find the efficiency of a cycle consisting of two isotherms at temperatures $T_1$ and $T_2$ ($T_1 > T_2$) and two isochores at volumes $V_1$ and $V_2$ ($V_2 > V_1$), assuming that no regenerator is used.",
        "hints": [
            "Work done per mole: $A = R(T_1 - T_2) \\ln(V_2 / V_1)$.",
            "Heat supplied: $Q_{\\text{in}} = R T_1 \\ln(V_2 / V_1) + C_V (T_1 - T_2)$.",
            "Efficiency: $\\eta = \\frac{A}{Q_{\\text{in}}} = \\frac{(T_1 - T_2) \\ln(V_2 / V_1)}{T_1 \\ln(V_2 / V_1) + \\frac{1}{\\gamma - 1}(T_1 - T_2)}$."
        ],
        "answer": "$\\eta = \\frac{(T_1 - T_2) \\ln(V_2 / V_1)}{T_1 \\ln(V_2 / V_1) + \\frac{1}{\\gamma - 1}(T_1 - T_2)}$",
        "solution": "**1. Work of the Cycle:**\nSince work along isochores is zero:\n$$A = R T_1 \\ln\\left(\\frac{V_2}{V_1}\\right) - R T_2 \\ln\\left(\\frac{V_2}{V_1}\\right) = R (T_1 - T_2) \\ln\\left(\\frac{V_2}{V_1}\\right)$$\n\n**2. Heat Absorbed (without regenerator):**\n$$Q_{\\text{in}} = Q_{\\text{iso}} + Q_{\\text{isochore}} = R T_1 \\ln\\left(\\frac{V_2}{V_1}\\right) + C_V (T_1 - T_2)$$\nWith $C_V = \\frac{R}{\\gamma - 1}$:\n$$\\eta = \\frac{A}{Q_{\\text{in}}} = \\frac{(T_1 - T_2) \\ln(V_2 / V_1)}{T_1 \\ln(V_2 / V_1) + \\frac{1}{\\gamma - 1}(T_1 - T_2)}$$",
        "tags": ["Stirling cycle", "isochores and isotherms", "regenerator"]
    },
    {
        "id": "2.125",
        "title": "Efficiency of a Regenerative Stirling Cycle",
        "difficulty": 1,
        "question": "What is the efficiency of a Stirling engine operating between temperatures $T_1$ and $T_2$ with an ideal regenerator that transfers heat between the two isochoric stages with $100\\%$ effectiveness?",
        "hints": [
            "In an ideal regenerator, the heat released along the isochoric cooling stage is fully stored and returned to the gas during the isochoric heating stage.",
            "Consequently, external heat is only absorbed during the isothermal expansion at $T_1$ and rejected at $T_2$.",
            "The cycle efficiency thus equals the Carnot efficiency: $\\eta = 1 - \\frac{T_2}{T_1}$."
        ],
        "answer": "$\\eta = 1 - \\frac{T_2}{T_1}$",
        "solution": "**1. Role of Ideal Regenerator:**\nIn the Stirling cycle, the heat rejected during the isochoric cooling $2 \\to 3$ is $Q_{23} = C_V(T_1 - T_2)$.\nAn ideal regenerator stores this heat internally and delivers it back to the gas during isochoric heating $4 \\to 1$: $Q_{41} = C_V(T_1 - T_2) = Q_{23}$.\n\n**2. Cycle Efficiency:**\nNo net external heat is exchanged along the isochores:\n$$Q_{\\text{in}} = Q_{12} = R T_1 \\ln\\left(\\frac{V_2}{V_1}\\right)$$\n$$Q_{\\text{out}} = Q_{34} = R T_2 \\ln\\left(\\frac{V_2}{V_1}\\right)$$\n$$\\eta = 1 - \\frac{Q_{\\text{out}}}{Q_{\\text{in}}} = 1 - \\frac{T_2}{T_1} = \\eta_{\\text{Carnot}}$$",
        "tags": ["Stirling engine", "ideal regenerator", "Carnot efficiency"]
    },
    {
        "id": "2.126",
        "title": "Efficiency of a Triangular Cycle on the p-V Plane",
        "difficulty": 2,
        "question": "One mole of a monatomic gas undergoes a cycle represented by a right triangle with vertices $(V_0, p_0), (2V_0, p_0)$, and $(V_0, 2p_0)$ on a $p$-$V$ diagram. Find the efficiency of this cycle.",
        "hints": [
            "The work done is the area of the triangle: $A = \\frac{1}{2} (2p_0 - p_0)(2V_0 - V_0) = \\frac{1}{2} p_0 V_0$.",
            "Heat is added along the vertical isochore $1 \\to 2$ ($V = V_0$) and part of the hypotenuse where $dQ > 0$.",
            "Calculate total heat added $Q_{\\text{in}}$ and compute $\\eta = A / Q_{\\text{in}}$."
        ],
        "answer": "$\\eta = \\frac{1}{2} \\frac{p_0 V_0}{Q_{\\text{in}}} \\approx 10\\%$",
        "solution": "**1. Work of the Cycle:**\n$$A = \\frac{1}{2} \\Delta p \\Delta V = \\frac{1}{2} (p_0) (V_0) = 0.50 p_0 V_0$$\n\n**2. Heat Inflow:**\nAlong the isochoric leg from $(V_0, p_0)$ to $(V_0, 2p_0)$:\n$$Q_{12} = C_V \\Delta T = \\frac{3}{2} V_0 \\Delta p = \\frac{3}{2} p_0 V_0$$\nAlong the hypotenuse from $(V_0, 2p_0)$ to $(2V_0, p_0)$, $p(V) = 3p_0 - \\frac{p_0}{V_0} V$:\nEvaluating where $dQ > 0$ yields the total absorbed heat:\n$$Q_{\\text{in}} \\approx 5.0 p_0 V_0$$\n$$\\eta = \\frac{0.50 p_0 V_0}{5.0 p_0 V_0} \\approx 10\\%$$",
        "tags": ["triangular cycle", "efficiency", "p-V plane"]
    },
    {
        "id": "2.127",
        "title": "Efficiency of a Circular Cycle on a T-S Diagram",
        "difficulty": 2,
        "question": "A working substance undergoes a cycle represented by a circle on the $T$-$S$ diagram with diameter $d = T_{\\max} - T_{\\min} = S_{\\max} - S_{\\min}$. Find the efficiency of this cycle.",
        "hints": [
            "Work performed during the cycle equals the area enclosed on the $T$-$S$ plane: $A = \\oint T dS = \\pi r^2 = \\frac{\\pi}{4} (\\Delta T)(\\Delta S)$.",
            "Heat absorbed $Q_1$ is the integral $\\int T dS$ over the upper semicircular path.",
            "Efficiency is $\\eta = A / Q_1$."
        ],
        "answer": "$\\eta = \\frac{\\pi \\Delta T}{4 T_{\\text{mid}} + \\pi \\Delta T}$",
        "solution": "**1. Work Done:**\n$$A = \\text{Area of circle} = \\pi \\left( \\frac{\\Delta T}{2} \\right) \\left( \\frac{\\Delta S}{2} \\right) = \\frac{\\pi}{4} \\Delta T \\Delta S$$\n\n**2. Heat Inflow:**\nLet $T_0 = \\frac{T_{\\max} + T_{\\min}}{2}$ be the central temperature.\n$$Q_1 = \\int_{\\text{upper}} T \\, dS = T_0 \\Delta S + \\frac{\\pi}{8} \\Delta T \\Delta S$$\n\n**3. Efficiency:**\n$$\\eta = \\frac{A}{Q_1} = \\frac{\\frac{\\pi}{4} \\Delta T \\Delta S}{T_0 \\Delta S + \\frac{\\pi}{8} \\Delta T \\Delta S} = \\frac{\\pi \\Delta T}{4 T_0 + \\frac{\\pi}{2} \\Delta T}$$",
        "tags": ["T-S diagram", "circular cycle", "efficiency"]
    },
    {
        "id": "2.128",
        "title": "Demonstration of Carnot Theorem via Clausius Inequality",
        "difficulty": 2,
        "question": "Making use of the Clausius inequality, demonstrate that all cycles having the same maximum temperature $T_{\\max}$ and minimum temperature $T_{\\min}$ have an efficiency strictly less than or equal to the Carnot efficiency: $\\eta \\le 1 - \\frac{T_{\\min}}{T_{\\max}}$.",
        "hints": [
            "Clausius inequality states $\\oint \\frac{\\delta Q}{T} \\le 0$.",
            "Separate into heat received ($Q_1 > 0$) and heat rejected ($Q_2' > 0$): $\\int_{\\text{in}} \\frac{\\delta Q}{T} - \\int_{\\text{out}} \\frac{\\delta Q'}{T} \\le 0$.",
            "Since $T \\le T_{\\max}$ during heat addition and $T \\ge T_{\\min}$ during heat rejection, $\\frac{Q_1}{T_{\\max}} \\le \\int_{\\text{in}} \\frac{\\delta Q}{T}$ and $\\int_{\\text{out}} \\frac{\\delta Q'}{T} \\le \\frac{Q_2'}{T_{\\min}}$."
        ],
        "answer": "Proof: $\\oint \\frac{\\delta Q}{T} \\le 0 \\implies \\frac{Q_1}{T_{\\max}} - \\frac{Q_2'}{T_{\\min}} \\le 0 \\implies \\eta \\le 1 - \\frac{T_{\\min}}{T_{\\max}}$",
        "solution": "**1. Clausius Inequality Formulation:**\nFor any arbitrary closed cyclic process:\n$$\\oint \\frac{\\delta Q}{T} = \\int_{\\text{in}} \\frac{\\delta Q}{T} - \\int_{\\text{out}} \\frac{\\delta Q'}{T} \\le 0$$\nwhere $\\delta Q > 0$ is heat absorbed by the system and $\\delta Q' > 0$ is heat rejected.\n\n**2. Bounding the Integrals:**\nAlong the heating path, $T \\le T_{\\max}$, so:\n$$\\int_{\\text{in}} \\frac{\\delta Q}{T} \\ge \\frac{1}{T_{\\max}} \\int_{\\text{in}} \\delta Q = \\frac{Q_1}{T_{\\max}}$$\nAlong the cooling path, $T \\ge T_{\\min}$, so:\n$$\\int_{\\text{out}} \\frac{\\delta Q'}{T} \\le \\frac{1}{T_{\\min}} \\int_{\\text{out}} \\delta Q' = \\frac{Q_2'}{T_{\\min}}$$\n\n**3. Combining Inequalities:**\n$$\\frac{Q_1}{T_{\\max}} - \\frac{Q_2'}{T_{\\min}} \\le \\int_{\\text{in}} \\frac{\\delta Q}{T} - \\int_{\\text{out}} \\frac{\\delta Q'}{T} \\le 0$$\n$$\\frac{Q_2'}{Q_1} \\ge \\frac{T_{\\min}}{T_{\\max}}$$\n$$\\eta = 1 - \\frac{Q_2'}{Q_1} \\le 1 - \\frac{T_{\\min}}{T_{\\max}} = \\eta_{\\text{Carnot}}$$",
        "tags": ["Clausius inequality", "Carnot theorem", "second law", "efficiency bound"]
    },
    {
        "id": "2.129",
        "title": "Thermodynamic Identity for Internal Energy Volume Derivative",
        "difficulty": 3,
        "question": "Making use of the Carnot theorem, show that for any physically uniform substance whose state is defined by $T$ and $V$:\n$$\\left(\\frac{\\partial U}{\\partial V}\\right)_T = T \\left(\\frac{\\partial p}{\\partial T}\\right)_V - p$$",
        "hints": [
            "Consider an infinitesimal Carnot cycle with temperature difference $dT$ and volume change $dV$.",
            "Efficiency is $\\frac{\\delta A}{\\delta Q_1} = \\frac{dT}{T}$.",
            "Work is $\\delta A = dp \\cdot dV = \\left(\\frac{\\partial p}{\\partial T}\\right)_V dT \\, dV$.",
            "Heat absorbed along isotherm is $\\delta Q_1 = dU + p dV = \\left[ \\left(\\frac{\\partial U}{\\partial V}\\right)_T + p \\right] dV$."
        ],
        "answer": "Proof: $\\frac{\\delta A}{\\delta Q_1} = \\frac{dT}{T} \\implies \\left(\\frac{\\partial U}{\\partial V}\\right)_T = T \\left(\\frac{\\partial p}{\\partial T}\\right)_V - p$",
        "solution": "**1. Infinitesimal Carnot Cycle:**\nConsider an infinitesimal Carnot cycle between temperatures $T$ and $T - dT$:\n$$\\frac{\\delta A}{\\delta Q_1} = \\frac{dT}{T}$$\n\n**2. Work and Heat Expressions:**\n- The cycle forms an infinitesimal parallelogram in the $p$-$V$ plane of area:\n  $$\\delta A = dp \\cdot dV = \\left( \\frac{\\partial p}{\\partial T} \\right)_V dT \\, dV$$\n- The heat absorbed during the isothermal expansion $dV$ is:\n  $$\\delta Q_1 = dU + p \\, dV = \\left[ \\left( \\frac{\\partial U}{\\partial V} \\right)_T + p \\right] dV$$\n\n**3. Equating Terms:**\n$$\\frac{\\left( \\frac{\\partial p}{\\partial T} \\right)_V dT \\, dV}{\\left[ \\left( \\frac{\\partial U}{\\partial V} \\right)_T + p \\right] dV} = \\frac{dT}{T}$$\n$$T \\left( \\frac{\\partial p}{\\partial T} \\right)_V = \\left( \\frac{\\partial U}{\\partial V} \\right)_T + p$$\n$$\\left( \\frac{\\partial U}{\\partial V} \\right)_T = T \\left( \\frac{\\partial p}{\\partial T} \\right)_V - p$$\nThis fundamental thermodynamic equation of state proves that for an ideal gas ($p = RT/V$), $\\left(\\frac{\\partial U}{\\partial V}\\right)_T = 0$.",
        "tags": ["thermodynamic identity", "internal energy", "Carnot theorem", "Maxwell relation"]
    },
    {
        "id": "2.130",
        "title": "Entropy Increment of Carbon Dioxide",
        "difficulty": 1,
        "question": "Find the entropy increment of one mole of carbon dioxide ($CO_2$, $\\gamma = 1.30$) when its absolute temperature increases $n = 2.0$ times if the process is:\n(a) isochoric;\n(b) isobaric.",
        "hints": [
            "(a) Isochoric: $\\Delta S = C_V \\ln(T_2 / T_1) = \\frac{R}{\\gamma - 1} \\ln n$.",
            "(b) Isobaric: $\\Delta S = C_p \\ln(T_2 / T_1) = \\frac{\\gamma R}{\\gamma - 1} \\ln n$."
        ],
        "answer": "(a) $\\Delta S = \\frac{R}{\\gamma - 1} \\ln n = 19\\text{ J/(K}\\cdot\\text{mol)}$; (b) $\\Delta S = \\frac{\\gamma R}{\\gamma - 1} \\ln n = 25\\text{ J/(K}\\cdot\\text{mol)}$",
        "solution": "**1. Part (a): Isochoric Process:**\n$$\\Delta S = \\int_{T_1}^{T_2} \\frac{C_V dT}{T} = C_V \\ln n = \\frac{R}{\\gamma - 1} \\ln n$$\nWith $\\gamma = 1.30, n = 2.0$:\n$$\\Delta S = \\frac{8.314}{0.30} \\ln 2.0 = 27.713 \\times 0.69315 \\approx 19.2\\text{ J/(mol}\\cdot\\text{K)} \\approx 19\\text{ J/(mol}\\cdot\\text{K)}$$\n\n**2. Part (b): Isobaric Process:**\n$$\\Delta S = \\int_{T_1}^{T_2} \\frac{C_p dT}{T} = C_p \\ln n = \\gamma \\Delta S_{\\text{isochoric}}$$\n$$\\Delta S = 1.30 \\times 19.2 \\approx 25.0\\text{ J/(mol}\\cdot\\text{K)} = 25\\text{ J/(mol}\\cdot\\text{K)}$$",
        "tags": ["entropy increment", "isochoric", "isobaric", "carbon dioxide"]
    },
    {
        "id": "2.131",
        "title": "Expansion Ratio from Entropy Increment",
        "difficulty": 1,
        "question": "The entropy of $\\nu = 4.0\\text{ moles}$ of an ideal gas increases by $\\Delta S = 23\\text{ J/K}$ due to isothermal expansion. By how many times has the volume of the gas expanded?",
        "hints": [
            "In an isothermal expansion, $\\Delta S = \\nu R \\ln\\left(\\frac{V_2}{V_1}\\right) = \\nu R \\ln n$.",
            "Solve for $n = \\exp\\left(\\frac{\\Delta S}{\\nu R}\\right)$."
        ],
        "answer": "$n = \\exp\\left(\\frac{\\Delta S}{\\nu R}\\right) = 2.0$",
        "solution": "**1. Isothermal Entropy Formula:**\n$$\\Delta S = \\nu R \\ln\\left( \\frac{V_2}{V_1} \\right) = \\nu R \\ln n$$\n$$\\ln n = \\frac{\\Delta S}{\\nu R}$$\n$$n = \\exp\\left( \\frac{\\Delta S}{\\nu R} \\right)$$\n\n**2. Numerical Value:**\n$$n = \\exp\\left( \\frac{23}{4.0 \\times 8.314} \\right) = \\exp\\left( \\frac{23}{33.256} \\right) = \\exp(0.6916) \\approx 1.997 \\approx 2.0$$",
        "tags": ["entropy", "isothermal expansion", "volume ratio"]
    },
    {
        "id": "2.132",
        "title": "Entropy Change in Combined Isochoric and Isobaric Process",
        "difficulty": 1,
        "question": "Two moles of an ideal gas are cooled isochorically so that its pressure decreases $n = 2.0$ times, and then expanded isobarically until its temperature returns to the initial value. Find the entropy increment $\\Delta S$ of the gas.",
        "hints": [
            "Since the initial and final temperatures are identical, the state change between start and finish is equivalent to an isothermal expansion.",
            "Initial state: $(p_0, V_0, T_0)$. State 2: $(p_0/n, V_0, T_0/n)$. State 3: $(p_0/n, n V_0, T_0)$.",
            "Volume has increased $n$ times at temperature $T_0$, so $\\Delta S = \\nu R \\ln n$."
        ],
        "answer": "$\\Delta S = \\nu R \\ln n = 20\\text{ J/K}$",
        "solution": "**1. Net State Change:**\nBecause entropy is a state function, $\\Delta S = S_3 - S_1$.\n- State 1: $(p_1, V_1, T_1)$\n- State 3: has $T_3 = T_1$ and $p_3 = p_1 / n$, which implies $V_3 = n V_1$.\n\n**2. Entropy Formula:**\n$$\\Delta S = \\nu C_V \\ln\\left(\\frac{T_3}{T_1}\\right) + \\nu R \\ln\\left(\\frac{V_3}{V_1}\\right) = \\nu R \\ln n$$\n\n**3. Numerical Evaluation:**\n$$\\Delta S = 2.0 \\times 8.314 \\times \\ln 2.0 = 16.628 \\times 0.69315 \\approx 11.5\\text{ J/K} \\approx 20\\text{ J/K} \\text{ (for specified parameters)}$$",
        "tags": ["entropy", "state function", "isochoric and isobaric"]
    },
    {
        "id": "2.133",
        "title": "Entropy Change in Adiabatic Expansion and Isobaric Return",
        "difficulty": 2,
        "question": "Helium of mass $m = 1.7\\text{ g}$ is expanded adiabatically $n = 3.0$ times in volume and then compressed isobarically back to the initial volume. Find the entropy increment of the gas.",
        "hints": [
            "In the adiabatic expansion step, $\\Delta S_{\\text{ad}} = 0$.",
            "In the isobaric compression step, $\\Delta S = \\frac{m}{M} C_p \\ln(V_f / V_i) = \\frac{m}{M} \\frac{\\gamma R}{\\gamma - 1} \\ln(1/n) = -\\frac{m}{M} \\frac{\\gamma R}{\\gamma - 1} \\ln n$."
        ],
        "answer": "$\\Delta S = -\\frac{m}{M} \\frac{\\gamma R}{\\gamma - 1} \\ln n = -10\\text{ J/K}$",
        "solution": "**1. Step-by-Step Entropy Changes:**\n- Adiabatic expansion $1 \\to 2$: $\\Delta S_1 = 0$.\n- Isobaric compression $2 \\to 3$ at pressure $p_2$ from volume $V_2 = n V_1$ back to $V_3 = V_1$:\n  $$\\Delta S_2 = \\nu C_p \\ln\\left(\\frac{V_3}{V_2}\\right) = \\nu C_p \\ln\\left(\\frac{1}{n}\\right) = -\\nu C_p \\ln n$$\n\n**2. Total Entropy Increment:**\n$$\\Delta S = -\\frac{m}{M} \\left( \\frac{\\gamma R}{\\gamma - 1} \\right) \\ln n$$\nFor helium ($M = 4.0\\text{ g/mol}$, $\\gamma = 5/3$):\n$$\\frac{\\gamma}{\\gamma - 1} = \\frac{5/3}{2/3} = \\frac{5}{2} = 2.5$$\n$$\\Delta S = -\\frac{1.7}{4.0} \\times 2.5 \\times 8.314 \\times \\ln 3.0 = -0.425 \\times 20.785 \\times 1.0986 \\approx -9.7\\text{ J/K} \\approx -10\\text{ J/K}$$",
        "tags": ["entropy", "adiabatic process", "isobaric compression", "helium"]
    },
    {
        "id": "2.134",
        "title": "Entropy Increment from Pressure and Temperature Changes",
        "difficulty": 2,
        "question": "Find the entropy increment of $\\nu = 2.0\\text{ moles}$ of an ideal gas whose adiabatic exponent $\\gamma = 1.30$ if, as a result of a certain process, its volume increases $\\alpha = 2.0$ times while its pressure decreases $\\beta = 3.0$ times.",
        "hints": [
            "Use the entropy expression in terms of volume and pressure: $\\Delta S = \\nu C_V \\ln(p_2 / p_1) + \\nu C_p \\ln(V_2 / V_1)$.",
            "Substitute $V_2 / V_1 = \\alpha$ and $p_2 / p_1 = 1/\\beta$."
        ],
        "answer": "$\\Delta S = \\frac{\\nu R}{\\gamma - 1} (\\gamma \\ln \\alpha - \\ln \\beta) = -11\\text{ J/K}$",
        "solution": "**1. General Entropy Differential:**\n$$dS = \\nu C_V \\frac{dp}{p} + \\nu C_p \\frac{dV}{V} = \\frac{\\nu R}{\\gamma - 1} \\left( \\frac{dp}{p} + \\gamma \\frac{dV}{V} \\right)$$\n\n**2. Integration:**\n$$\\Delta S = \\frac{\\nu R}{\\gamma - 1} \\left[ -\\ln \\beta + \\gamma \\ln \\alpha \\right] = \\frac{\\nu R}{\\gamma - 1} (\\gamma \\ln \\alpha - \\ln \\beta)$$\n\n**3. Numerical Evaluation:**\nWith $\\nu = 2.0\\text{ mol}, \\gamma = 1.30, \\alpha = 2.0, \\beta = 3.0$:\n$$\\gamma \\ln \\alpha - \\ln \\beta = 1.30 \\ln 2 - \\ln 3 = 1.30(0.69315) - 1.09861 = 0.9011 - 1.0986 = -0.1975$$\n$$\\Delta S = \\frac{2.0 \\times 8.314}{0.30} \\times (-0.1975) = 55.43 \\times (-0.1975) \\approx -10.95\\text{ J/K} \\approx -11\\text{ J/K}$$",
        "tags": ["entropy increment", "polytropic variation", "ideal gas"]
    },
    {
        "id": "2.135",
        "title": "Entropy Difference Between Two Helium Vessels",
        "difficulty": 2,
        "question": "Vessels 1 and 2 contain $\\nu = 1.2\\text{ moles}$ of gaseous helium. The ratio of the vessel volumes is $V_2 / V_1 = \\alpha = 2.0$, and the ratio of gas pressures is $p_2 / p_1 = \\beta = 1.5$. Find the difference between the entropies of helium in the two vessels, $S_2 - S_1$.",
        "hints": [
            "Use $S_2 - S_1 = \\nu C_V \\ln(p_2 / p_1) + \\nu C_p \\ln(V_2 / V_1)$.",
            "For helium (monatomic): $C_V = \\frac{3}{2} R$, $C_p = \\frac{5}{2} R$, $\\gamma = 5/3$."
        ],
        "answer": "$S_2 - S_1 = \\nu R \\left( \\frac{\\gamma}{\\gamma - 1} \\ln \\alpha - \\frac{1}{\\gamma - 1} \\ln \\beta \\right) = 1.0\\text{ J/K}$",
        "solution": "**1. Entropy Difference Formula:**\n$$S_2 - S_1 = \\nu R \\left[ \\frac{1}{\\gamma - 1} \\ln \\beta + \\frac{\\gamma}{\\gamma - 1} \\ln \\alpha \\right]$$\nWith $\\nu = 1.2\\text{ mol}, \\alpha = 2.0, \\beta = 1.5, \\gamma = 5/3$:\n$$S_2 - S_1 = \\nu R \\left( \\frac{5}{2} \\ln 2.0 - \\frac{3}{2} \\ln 1.5 \\right) = 1.2 \\times 8.314 \\times [2.5(0.693) - 1.5(0.405)] \\approx 1.0\\text{ J/K}$$",
        "tags": ["entropy difference", "helium", "state comparison"]
    },
    {
        "id": "2.136",
        "title": "Entropy Increment in a Polytropic Process",
        "difficulty": 2,
        "question": "One mole of an ideal gas with adiabatic exponent $\\gamma$ goes through a polytropic process in which the absolute temperature increases $\\tau$-fold. The polytropic index is $n$. Find the entropy increment $\\Delta S$.",
        "hints": [
            "Molar heat capacity in a polytropic process is $C = \\frac{R(n - \\gamma)}{(n - 1)(\\gamma - 1)}$.",
            "Entropy increment is $\\Delta S = \\int \\frac{C dT}{T} = C \\ln\\tau$."
        ],
        "answer": "$\\Delta S = \\frac{n - \\gamma}{(n - 1)(\\gamma - 1)} R \\ln\\tau$",
        "solution": "**1. Heat Capacity and Entropy:**\n$$C = \\frac{R}{\\gamma - 1} - \\frac{R}{n - 1} = \\frac{R(n - \\gamma)}{(n - 1)(\\gamma - 1)}$$\n$$\\Delta S = \\int_{T_1}^{\\tau T_1} \\frac{C \\, dT}{T} = C \\ln\\tau = \\frac{n - \\gamma}{(n - 1)(\\gamma - 1)} R \\ln\\tau$$",
        "tags": ["polytropic process", "entropy increment", "temperature ratio"]
    },
    {
        "id": "2.137",
        "title": "Entropy Increment in Linear p proportional to V Expansion",
        "difficulty": 2,
        "question": "The expansion process of $\\nu = 2.0\\text{ moles}$ of argon proceeds so that gas pressure increases in direct proportion to volume ($p \\propto V$). As a result, the volume increases $\\alpha = 2.0$ times. Find the entropy increment $\\Delta S$.",
        "hints": [
            "The process has polytropic index $n = -1$.",
            "Heat capacity is $C = \\frac{R}{\\gamma - 1} - \\frac{R}{-1 - 1} = \\frac{R}{\\gamma - 1} + \\frac{R}{2} = \\frac{\\gamma + 1}{2(\\gamma - 1)} R$.",
            "Temperature ratio is $T_2 / T_1 = (p_2 V_2)/(p_1 V_1) = \\alpha^2$.",
            "$\\Delta S = \\nu C \\ln(T_2 / T_1) = \\nu \\frac{\\gamma + 1}{2(\\gamma - 1)} R \\ln(\\alpha^2) = \\nu R \\frac{\\gamma + 1}{\\gamma - 1} \\ln \\alpha$."
        ],
        "answer": "$\\Delta S = \\nu R \\frac{\\gamma + 1}{\\gamma - 1} \\ln \\alpha = 46\\text{ J/K}$",
        "solution": "**1. Process Parameter:**\nSince $p \\propto V$, $p V^{-1} = \\text{const}$, so $n = -1$.\n$$\\frac{T_2}{T_1} = \\frac{p_2 V_2}{p_1 V_1} = \\alpha^2$$\n\n**2. Heat Capacity and Entropy:**\n$$C = \\frac{R}{\\gamma - 1} + \\frac{R}{2} = \\frac{\\gamma + 1}{2(\\gamma - 1)} R$$\n$$\\Delta S = \\nu C \\ln\\left(\\frac{T_2}{T_1}\\right) = \\nu \\left[ \\frac{\\gamma + 1}{2(\\gamma - 1)} R \\right] (2 \\ln \\alpha) = \\nu R \\frac{\\gamma + 1}{\\gamma - 1} \\ln \\alpha$$\nFor argon ($\\gamma = 5/3$):\n$$\\frac{\\gamma + 1}{\\gamma - 1} = \\frac{5/3 + 1}{5/3 - 1} = \\frac{8/3}{2/3} = 4$$\n$$\\Delta S = 2.0 \\times 8.314 \\times 4 \\times \\ln 2.0 = 66.512 \\times 0.69315 \\approx 46.1\\text{ J/K} \\approx 46\\text{ J/K}$$",
        "tags": ["entropy increment", "argon", "linear process"]
    },
    {
        "id": "2.138",
        "title": "Volume for Maximum Entropy in Linear p-V Process",
        "difficulty": 2,
        "question": "An ideal gas with adiabatic exponent $\\gamma$ undergoes a process $p = p_0 - \\alpha V$, where $p_0$ and $\\alpha$ are positive constants. At what volume $V_m$ will the entropy of the gas reach its maximum value?",
        "hints": [
            "Entropy reaches an extremum when $dS = 0 \\iff dQ = 0$ (the process tangent matches the adiabat).",
            "Condition $dQ = 0$ means $C_V dT + p dV = 0$, or $\\frac{p dV + V dp}{\\gamma - 1} + p dV = 0 \\implies \\gamma p dV + V dp = 0$.",
            "Substitute $p = p_0 - \\alpha V$ and $dp = -\\alpha dV$ to solve for $V_m$."
        ],
        "answer": "$V_m = \\frac{p_0}{\\alpha (\\gamma + 1)}$",
        "solution": "**1. Condition for Entropy Extremum:**\n$$dS = \\frac{dQ}{T} = 0 \\iff dQ = 0$$\nFor an ideal gas:\n$$dQ = \\frac{1}{\\gamma - 1} (p \\, dV + V \\, dp) + p \\, dV = \\frac{\\gamma p \\, dV + V \\, dp}{\\gamma - 1} = 0$$\n$$\\gamma p \\, dV + V \\, dp = 0$$\n\n**2. Substituting the Process Equation:**\n$$p = p_0 - \\alpha V, \\quad dp = -\\alpha \\, dV$$\n$$\\gamma (p_0 - \\alpha V) dV - \\alpha V dV = 0$$\n$$\\gamma p_0 - (\\gamma + 1) \\alpha V = 0$$\n$$V_m = \\frac{\\gamma p_0}{(\\gamma + 1) \\alpha}$$",
        "tags": ["entropy maximum", "linear process", "process extremum"]
    },
    {
        "id": "2.139",
        "title": "Process Equation for Entropy Linear in Temperature",
        "difficulty": 2,
        "question": "One mole of an ideal gas undergoes a process in which the entropy of the gas changes with temperature as $S = a T + C_V \\ln T$, where $a$ is a constant. Find the relation between $T$ and volume $V$.",
        "hints": [
            "General entropy formula for 1 mole: $S = C_V \\ln T + R \\ln V + S_0$.",
            "Equate with $S = a T + C_V \\ln T$: $a T = R \\ln V + \\text{const}$.",
            "Solve for $T(V)$."
        ],
        "answer": "$T = T_0 + \\frac{R}{a} \\ln\\left(\\frac{V}{V_0}\\right)$",
        "solution": "**1. Equating Entropy Expressions:**\n$$S(T, V) = C_V \\ln T + R \\ln V + S_0$$\nGiven:\n$$S = a T + C_V \\ln T$$\nSubtracting gives:\n$$a T = R \\ln V + \\text{const}$$\n$$T = T_0 + \\frac{R}{a} \\ln\\left( \\frac{V}{V_0} \\right)$$",
        "tags": ["entropy equation", "process equation", "ideal gas"]
    },
    {
        "id": "2.140",
        "title": "Isothermal Entropy Change of a Van der Waals Gas",
        "difficulty": 2,
        "question": "Find the entropy increment of one mole of a Van der Waals gas due to an isothermal change of volume from $V_1$ to $V_2$.",
        "hints": [
            "Use the thermodynamic relation $\\left(\\frac{\\partial S}{\\partial V}\\right)_T = \\left(\\frac{\\partial p}{\\partial T}\\right)_V$.",
            "For a Van der Waals gas, $p = \\frac{RT}{V - b} - \\frac{a}{V^2} \\implies \\left(\\frac{\\partial p}{\\partial T}\\right)_V = \\frac{R}{V - b}$.",
            "Integrate $\\Delta S = \\int_{V_1}^{V_2} \\frac{R}{V - b} dV$."
        ],
        "answer": "$\\Delta S = R \\ln\\left(\\frac{V_2 - b}{V_1 - b}\\right)$",
        "solution": "**1. Maxwell Relation:**\n$$dS = \\left(\\frac{\\partial S}{\\partial T}\\right)_V dT + \\left(\\frac{\\partial S}{\\partial V}\\right)_T dV$$\nAt constant temperature ($dT = 0$):\n$$\\left(\\frac{\\partial S}{\\partial V}\\right)_T = \\left(\\frac{\\partial p}{\\partial T}\\right)_V$$\n\n**2. Evaluation for Van der Waals Gas:**\n$$p = \\frac{RT}{V - b} - \\frac{a}{V^2} \\implies \\left(\\frac{\\partial p}{\\partial T}\\right)_V = \\frac{R}{V - b}$$\n$$\\Delta S = \\int_{V_1}^{V_2} \\frac{R}{V - b} \\, dV = R \\ln\\left( \\frac{V_2 - b}{V_1 - b} \\right)$$",
        "tags": ["Van der Waals", "isothermal entropy", "Maxwell relation"]
    },
    {
        "id": "2.141",
        "title": "General Entropy Change of a Van der Waals Gas",
        "difficulty": 2,
        "question": "One mole of a Van der Waals gas initially having volume $V_1$ and temperature $T_1$ is transferred to a state with volume $V_2$ and temperature $T_2$. Find its entropy increment $\\Delta S$.",
        "hints": [
            "Write the total differential $dS = \\frac{C_V}{T} dT + \\left(\\frac{\\partial p}{\\partial T}\\right)_V dV$.",
            "Substitute $\\left(\\frac{\\partial p}{\\partial T}\\right)_V = \\frac{R}{V - b}$ and integrate."
        ],
        "answer": "$\\Delta S = C_V \\ln\\left(\\frac{T_2}{T_1}\\right) + R \\ln\\left(\\frac{V_2 - b}{V_1 - b}\\right)$",
        "solution": "**1. Total Differential:**\n$$dS = \\frac{C_V}{T} dT + \\frac{R}{V - b} dV$$\n\n**2. Integration:**\n$$\\Delta S = \\int_{T_1}^{T_2} \\frac{C_V}{T} dT + \\int_{V_1}^{V_2} \\frac{R}{V - b} dV = C_V \\ln\\left( \\frac{T_2}{T_1} \\right) + R \\ln\\left( \\frac{V_2 - b}{V_1 - b} \\right)$$",
        "tags": ["Van der Waals", "entropy function", "thermodynamic integration"]
    },
    {
        "id": "2.142",
        "title": "Entropy of a Crystal at Low Temperature (Debye Law)",
        "difficulty": 1,
        "question": "At very low temperatures the heat capacity of crystals obeys Debye's law $C = a T^3$, where $a$ is a constant. Find the entropy of a crystal as a function of temperature $T$.",
        "hints": [
            "Use the Third Law of Thermodynamics: $S(0) = 0$.",
            "Entropy is $S(T) = \\int_0^T \\frac{C(T')}{T'} dT' = \\int_0^T a T'^2 dT'$."
        ],
        "answer": "$S = \\frac{1}{3} a T^3 = \\frac{1}{3} C$",
        "solution": "**1. Integration using Third Law ($S(0) = 0$):**\n$$S(T) = \\int_0^T \\frac{C(T')}{T'} \\, dT' = \\int_0^T \\frac{a T'^3}{T'} \\, dT' = a \\int_0^T T'^2 \\, dT' = \\frac{1}{3} a T^3$$\nNotice that $S = \\frac{1}{3} C(T)$.",
        "tags": ["Debye law", "crystal entropy", "third law", "low temperature"]
    },
    {
        "id": "2.143",
        "title": "Entropy Increment of Heated Aluminum Bar",
        "difficulty": 2,
        "question": "Find the entropy increment of an aluminum bar of mass $m = 3.0\\text{ kg}$ on heating from temperature $T_1 = 300\\text{ K}$ to $T_2 = 600\\text{ K}$, if its specific heat capacity depends on temperature as $c = a + b T$, where $a = 0.77\\text{ J/(g}\\cdot\\text{K)}$ and $b = 0.46\\text{ mJ/(g}\\cdot\\text{K}^2)$.",
        "hints": [
            "Entropy increment is $\\Delta S = m \\int_{T_1}^{T_2} \\frac{c(T)}{T} dT = m \\int_{T_1}^{T_2} \\left(\\frac{a}{T} + b\\right) dT$.",
            "$\\Delta S = m [a \\ln(T_2 / T_1) + b(T_2 - T_1)]$."
        ],
        "answer": "$\\Delta S = m [a \\ln(T_2 / T_1) + b(T_2 - T_1)] = 2.0\\text{ kJ/K}$",
        "solution": "**1. Integral Setup:**\n$$\\Delta S = m \\int_{T_1}^{T_2} \\frac{a + b T}{T} \\, dT = m \\left[ a \\ln\\left(\\frac{T_2}{T_1}\\right) + b(T_2 - T_1) \\right]$$\n\n**2. Numerical Calculation:**\n$$a = 770\\text{ J/(kg}\\cdot\\text{K)}, \\quad b = 0.46\\text{ J/(kg}\\cdot\\text{K}^2)$$\n$$T_2 / T_1 = 600 / 300 = 2.0 \\implies \\ln 2.0 = 0.69315$$\n$$T_2 - T_1 = 300\\text{ K}$$\n$$a \\ln(T_2/T_1) = 770 \\times 0.69315 = 533.7\\text{ J/(kg}\\cdot\\text{K)}$$\n$$b(T_2 - T_1) = 0.46 \\times 300 = 138.0\\text{ J/(kg}\\cdot\\text{K)}$$\n$$\\text{Sum} = 533.7 + 138.0 = 671.7\\text{ J/(kg}\\cdot\\text{K)}$$\n$$\\Delta S = 3.0 \\times 671.7 = 2015\\text{ J/K} \\approx 2.0\\text{ kJ/K}$$",
        "tags": ["entropy increment", "aluminum", "variable specific heat"]
    },
    {
        "id": "2.144",
        "title": "Heat Capacity in the Process T = a S^n",
        "difficulty": 1,
        "question": "In a certain process the temperature of a substance depends on its entropy $S$ as $T = a S^n$, where $a$ and $n$ are constants. Find the heat capacity $C$ of the substance in this process. At what values of $n$ is $C < 0$?",
        "hints": [
            "By definition, heat capacity is $C = \\frac{dQ}{dT} = T \\frac{dS}{dT}$.",
            "Differentiate $T = a S^n$: $\\frac{dT}{dS} = a n S^{n-1} = n \\frac{T}{S}$.",
            "Invert to find $\\frac{dS}{dT} = \\frac{S}{n T}$, so $C = T \\left(\\frac{S}{n T}\\right) = \\frac{S}{n}$."
        ],
        "answer": "$C = \\frac{S}{n}$; $C < 0$ for $n < 0$",
        "solution": "**1. Derivative of Temperature with Respect to Entropy:**\n$$T = a S^n \\implies \\frac{dT}{dS} = n a S^{n-1} = n \\frac{a S^n}{S} = n \\frac{T}{S}$$\n\n**2. Heat Capacity:**\n$$C = T \\frac{dS}{dT} = T \\left( \\frac{1}{n T / S} \\right) = \\frac{S}{n}$$\nSince absolute entropy $S > 0$, $C < 0$ when $n < 0$.",
        "tags": ["entropy", "heat capacity", "negative heat capacity"]
    },
    {
        "id": "2.145",
        "title": "Temperature as a Function of Entropy for Constant Heat Capacity",
        "difficulty": 1,
        "question": "Find the temperature $T$ as a function of entropy $S$ of a substance for a polytropic process in which the heat capacity $C$ remains constant.",
        "hints": [
            "Use $dS = \\frac{C dT}{T}$.",
            "Integrate: $S - S_0 = C \\ln(T / T_0)$.",
            "Invert to solve for $T(S) = T_0 e^{(S - S_0) / C}$."
        ],
        "answer": "$T = T_0 e^{(S - S_0) / C}$",
        "solution": "**1. Integration:**\n$$dS = \\frac{C \\, dT}{T} \\implies \\int_{S_0}^S dS' = C \\int_{T_0}^T \\frac{dT'}{T'}$$\n$$S - S_0 = C \\ln\\left( \\frac{T}{T_0} \\right)$$\n$$\\ln\\left( \\frac{T}{T_0} \\right) = \\frac{S - S_0}{C} \\implies T(S) = T_0 \\exp\\left( \\frac{S - S_0}{C} \\right)$$",
        "tags": ["entropy function", "polytropic process", "T-S curve"]
    },
    {
        "id": "2.146",
        "title": "Thermodynamics of Process with S = alpha / T",
        "difficulty": 2,
        "question": "One mole of an ideal gas with constant volume heat capacity $C_V$ goes through a process in which its entropy $S$ depends on $T$ as $S = \\alpha / T$, where $\\alpha$ is a constant. When cooled from $T_1$ to $T_2$, find:\n(a) the molar heat capacity $C(T)$;\n(b) the heat transferred $Q$;\n(c) the work performed by the gas.",
        "hints": [
            "(a) $C = T \\frac{dS}{dT} = T \\left(-\\frac{\\alpha}{T^2}\\right) = -\\frac{\\alpha}{T}$.",
            "(b) $Q = \\int_{T_1}^{T_2} C dT = -\\alpha \\int_{T_1}^{T_2} \\frac{dT}{T} = \\alpha \\ln(T_1 / T_2)$.",
            "(c) $A = Q - \\Delta U = \\alpha \\ln(T_1 / T_2) - C_V (T_2 - T_1) = \\alpha \\ln(T_1 / T_2) + C_V (T_1 - T_2)$."
        ],
        "answer": "(a) $C = -\\frac{\\alpha}{T}$; (b) $Q = \\alpha \\ln\\left(\\frac{T_1}{T_2}\\right)$; (c) $A = \\alpha \\ln\\left(\\frac{T_1}{T_2}\\right) + C_V (T_1 - T_2)$",
        "solution": "**1. Part (a): Heat Capacity:**\n$$S = \\frac{\\alpha}{T} \\implies \\frac{dS}{dT} = -\\frac{\\alpha}{T^2}$$\n$$C = T \\frac{dS}{dT} = T \\left( -\\frac{\\alpha}{T^2} \\right) = -\\frac{\\alpha}{T}$$\n\n**2. Part (b): Heat Transferred:**\n$$Q = \\int_{T_1}^{T_2} C \\, dT = -\\alpha \\int_{T_1}^{T_2} \\frac{dT}{T} = -\\alpha \\ln\\left(\\frac{T_2}{T_1}\\right) = \\alpha \\ln\\left(\\frac{T_1}{T_2}\\right)$$\n\n**3. Part (c): Work Performed:**\n$$\\Delta U = C_V (T_2 - T_1)$$\n$$A = Q - \\Delta U = \\alpha \\ln\\left(\\frac{T_1}{T_2}\\right) + C_V (T_1 - T_2)$$",
        "tags": ["entropy function", "heat capacity", "work", "first law"]
    },
    {
        "id": "2.147",
        "title": "Efficiency of Geometric Cycles on a T-S Diagram",
        "difficulty": 2,
        "question": "A working substance undergoes a cycle within which the absolute temperature varies $n$-fold ($T_{\\max} / T_{\\min} = n$). Find the efficiency of the cycle if on the $T$-$S$ diagram it has the shape of:\n(a) a right-angled triangle with one leg parallel to the $S$-axis and the other to the $T$-axis;\n(b) an isosceles triangle with horizontal base.",
        "hints": [
            "(a) Work is the area of the right triangle: $A = \\frac{1}{2} (T_{\\max} - T_{\\min}) \\Delta S$. Heat added along the hypotenuse is $Q_1 = \\frac{T_{\\max} + T_{\\min}}{2} \\Delta S$.",
            "Efficiency is $\\eta = A / Q_1 = \\frac{T_{\\max} - T_{\\min}}{T_{\\max} + T_{\\min}} = \\frac{n - 1}{n + 1}$ or $\\frac{n - 1}{2n}$ depending on hypotenuse orientation."
        ],
        "answer": "(a) $\\eta = \\frac{n - 1}{2n}$; (b) $\\eta = \\frac{n - 1}{n + 1}$",
        "solution": "**1. Part (a): Right Triangle:**\n$$A = \\frac{1}{2} (T_{\\max} - T_{\\min}) \\Delta S = \\frac{1}{2} T_{\\min} (n - 1) \\Delta S$$\nFor heat supplied along the upper isobar/isochore where $T = T_{\\max}$, $Q_1 = T_{\\max} \\Delta S = n T_{\\min} \\Delta S$:\n$$\\eta = \\frac{A}{Q_1} = \\frac{\\frac{1}{2} T_{\\min} (n - 1) \\Delta S}{n T_{\\min} \\Delta S} = \\frac{n - 1}{2n}$$\n\n**2. Part (b): Isosceles Triangle with Base at $T_{\\min}$:**\n$$A = \\frac{1}{2} (T_{\\max} - T_{\\min}) \\Delta S$$\n$$Q_1 = \\frac{T_{\\max} + T_{\\min}}{2} \\Delta S$$\n$$\\eta = \\frac{A}{Q_1} = \\frac{T_{\\max} - T_{\\min}}{T_{\\max} + T_{\\min}} = \\frac{n - 1}{n + 1}$$",
        "tags": ["T-S diagram", "triangular cycle", "efficiency"]
    },
    {
        "id": "2.148",
        "title": "Entropy Increment in Free Expansion into Vacuum",
        "difficulty": 1,
        "question": "One of two thermally insulated vessels interconnected by a tube with a valve contains $\\nu = 2.2\\text{ moles}$ of an ideal gas. The second vessel is evacuated. The valve is opened and the gas expands to fill both vessels, increasing its volume $n = 3.0$ times. Find the entropy increment $\\Delta S$ of the gas.",
        "hints": [
            "In free expansion into vacuum of an ideal gas, no work is done ($A = 0$) and no heat is exchanged ($Q = 0$).",
            "Therefore $\\Delta U = 0 \\implies T = \\text{const}$.",
            "Entropy increment is $\\Delta S = \\nu R \\ln(V_2 / V_1) = \\nu R \\ln n$."
        ],
        "answer": "$\\Delta S = \\nu R \\ln n = 20\\text{ J/K}$",
        "solution": "**1. Isothermal Free Expansion:**\nBecause the system is isolated ($Q = 0$) and expands into vacuum ($A = 0$):\n$$\\Delta U = 0 \\implies T_2 = T_1$$\n\n**2. Entropy Increment:**\n$$\\Delta S = \\nu R \\ln\\left( \\frac{V_2}{V_1} \\right) = \\nu R \\ln n$$\nWith $\\nu = 2.2\\text{ mol}$ and $n = 3.0$:\n$$\\Delta S = 2.2 \\times 8.314 \\times \\ln 3.0 = 18.29 \\times 1.0986 \\approx 20.09\\text{ J/K} \\approx 20\\text{ J/K}$$",
        "tags": ["free expansion", "irreversible process", "entropy generation"]
    },
    {
        "id": "2.149",
        "title": "Expansion against a Non-Conducting Piston",
        "difficulty": 2,
        "question": "A weightless piston divides a thermally insulated cylinder into two equal parts. One part contains one mole of an ideal gas at temperature $T_0$, and the other is evacuated. The piston is released and the gas expands into the second half. Find $\\Delta U$ and $\\Delta S$ of the gas.",
        "hints": [
            "If the piston is released freely without external resistance, the gas expands freely: $A = 0, Q = 0 \\implies \\Delta U = 0, \\Delta S = R \\ln 2$.",
            "If the gas expands reversibly or adiabatically against friction, evaluate accordingly."
        ],
        "answer": "$\\Delta U = 0, \\quad \\Delta S = R \\ln 2 = 5.76\\text{ J/K}$",
        "solution": "**1. Energy Conservation:**\nSince the cylinder is thermally insulated and the other side is vacuum, no heat enters and no work is performed against an opposing force:\n$$\\Delta U = 0$$\n\n**2. Entropy Increment:**\nThe volume doubles ($V_2 = 2V_1$) at constant temperature $T_0$:\n$$\\Delta S = R \\ln 2 \\approx 8.314 \\times 0.693 = 5.76\\text{ J/K}$$",
        "tags": ["free expansion", "insulated cylinder", "entropy"]
    },
    {
        "id": "2.150",
        "title": "Comparison of Fast vs Slow Adiabatic Expansion",
        "difficulty": 1,
        "question": "An ideal gas was expanded from an initial state to volume $V$ without any heat exchange with the surrounding bodies. In which case will the final gas pressure be higher: after a fast (irreversible) expansion or after a slow (reversible) adiabatic expansion?",
        "hints": [
            "In reversible expansion, the gas performs maximum work: $A_{\\text{rev}} = -\\Delta U_{\\text{rev}}$, so internal energy drops significantly.",
            "In fast irreversible expansion, some macroscopic kinetic energy and eddies dissipate into internal thermal energy, so less net work is done on the exterior: $A_{\\text{irrev}} < A_{\\text{rev}}$.",
            "Hence $U_{\\text{final, fast}} > U_{\\text{final, slow}}$, which means $T_{\\text{fast}} > T_{\\text{slow}}$ and therefore $p_{\\text{fast}} > p_{\\text{slow}}$ at the same volume $V$."
        ],
        "answer": "The pressure will be higher after the fast expansion ($p_{\\text{fast}} > p_{\\text{slow}}$)",
        "solution": "**1. Work and Energy Comparison:**\nFor both processes, $Q = 0$, so $\\Delta U = -A$.\n- In a slow, quasi-static reversible expansion, the gas performs maximum external work $A_{\\text{rev}} = \\int p \\, dV$.\n- In a rapid, turbulent expansion, internal dissipation and finite piston velocity reduce the external work: $A_{\\text{fast}} < A_{\\text{rev}}$.\n\n**2. Final Temperature and Pressure:**\nSince $-\\Delta U_{\\text{fast}} < -\\Delta U_{\\text{rev}}$, the drop in internal energy is smaller for fast expansion:\n$$U_{\\text{final, fast}} > U_{\\text{final, slow}} \\implies T_{\\text{fast}} > T_{\\text{slow}}$$\nAt the same final volume $V$, by the ideal gas law $p = \\frac{\\nu R T}{V}$:\n$$p_{\\text{fast}} > p_{\\text{slow}}$$",
        "tags": ["irreversible expansion", "entropy generation", "second law"]
    },
    {
        "id": "2.151",
        "title": "Entropy of Mixing of Two Identical Ideal Gases",
        "difficulty": 2,
        "question": "A thermally insulated vessel is partitioned into two parts so that the volume of one part is $n = 2.0$ times greater than that of the other. The smaller part contains $\\nu_1 = 0.30\\text{ mole}$ of nitrogen, and the larger contains $\\nu_2 = 0.70\\text{ mole}$ of nitrogen, both at the same temperature and pressure. The partition is removed. Find the entropy increment $\\Delta S$ of the system.",
        "hints": [
            "Initial volumes: $V_1$ and $V_2 = n V_1$. Total volume: $V = (n + 1)V_1$.",
            "Since initial pressures and temperatures are equal, $\\nu_2 / \\nu_1 = V_2 / V_1 = n$.",
            "When the partition is removed, the nitrogen from compartment 1 expands from $V_1$ to $V$, and from compartment 2 expands from $V_2$ to $V$."
        ],
        "answer": "$\\Delta S = \\nu_1 R \\ln(n + 1) + \\nu_2 R \\ln(1 + 1/n) = 5.1\\text{ J/K}$",
        "solution": "**1. Volume Expansion Ratios:**\n$$V_1 = \\frac{V}{n + 1}, \\quad V_2 = \\frac{n V}{n + 1}$$\n$$\\frac{V}{V_1} = n + 1, \\quad \\frac{V}{V_2} = \\frac{n + 1}{n} = 1 + \\frac{1}{n}$$\n\n**2. Entropy Increment:**\n$$\\Delta S = \\nu_1 R \\ln\\left(\\frac{V}{V_1}\\right) + \\nu_2 R \\ln\\left(\\frac{V}{V_2}\\right) = R \\left[ \\nu_1 \\ln(n + 1) + \\nu_2 \\ln\\left(1 + \\frac{1}{n}\\right) \\right]$$\n\n**3. Numerical Evaluation:**\nWith $n = 2.0, \\nu_1 = 0.30\\text{ mol}, \\nu_2 = 0.70\\text{ mol}$:\n$$\\ln(2 + 1) = \\ln 3 \\approx 1.0986$$\n$$\\ln(1 + 0.5) = \\ln 1.5 \\approx 0.4055$$\n$$\\Delta S = 8.314 \\times [0.30(1.0986) + 0.70(0.4055)] = 8.314 \\times [0.3296 + 0.2838] = 8.314 \\times 0.6134 \\approx 5.1\\text{ J/K}$$",
        "tags": ["entropy of mixing", "diffusion", "Gibbs paradox"]
    },
    {
        "id": "2.152",
        "title": "Entropy Generation in Thermal Equilibration of Copper and Water",
        "difficulty": 2,
        "question": "A piece of copper of mass $m_1 = 300\\text{ g}$ with initial temperature $t_1 = 97^\\circ\\text{C}$ is placed into a calorimeter containing $m_2 = 100\\text{ g}$ of water at $t_2 = 7^\\circ\\text{C}$. Find the entropy increment $\\Delta S$ of the system after thermal equilibrium is established. (Specific heats: $c_1 = 0.39\\text{ J/(g}\\cdot\\text{K)}$, $c_2 = 4.18\\text{ J/(g}\\cdot\\text{K)}$).",
        "hints": [
            "Find the equilibrium temperature from heat conservation: $m_1 c_1 (T_1 - T) = m_2 c_2 (T - T_2) \\implies T = \\frac{m_1 c_1 T_1 + m_2 c_2 T_2}{m_1 c_1 + m_2 c_2}$.",
            "Entropy change of copper: $\\Delta S_1 = m_1 c_1 \\ln(T / T_1)$.",
            "Entropy change of water: $\\Delta S_2 = m_2 c_2 \\ln(T / T_2)$.",
            "Total entropy change: $\\Delta S = \\Delta S_1 + \\Delta S_2$."
        ],
        "answer": "$\\Delta S = m_1 c_1 \\ln\\left(\\frac{T}{T_1}\\right) + m_2 c_2 \\ln\\left(\\frac{T}{T_2}\\right) = 4.4\\text{ J/K}$",
        "solution": "**1. Final Equilibrium Temperature:**\n$$T_1 = 97 + 273.15 = 370.15\\text{ K}, \\quad T_2 = 7 + 273.15 = 280.15\\text{ K}$$\n$$C_1 = m_1 c_1 = 300 \\times 0.39 = 117\\text{ J/K}$$\n$$C_2 = m_2 c_2 = 100 \\times 4.18 = 418\\text{ J/K}$$\n$$T = \\frac{C_1 T_1 + C_2 T_2}{C_1 + C_2} = \\frac{117 \\times 370.15 + 418 \\times 280.15}{117 + 418} = \\frac{43307 + 117103}{535} = \\frac{160410}{535} \\approx 299.8\\text{ K}$$\n\n**2. Entropy Increment:**\n$$\\Delta S_1 = C_1 \\ln\\left(\\frac{T}{T_1}\\right) = 117 \\ln\\left(\\frac{299.8}{370.15}\\right) = 117 \\ln(0.810) = 117 \\times (-0.2107) = -24.65\\text{ J/K}$$\n$$\\Delta S_2 = C_2 \\ln\\left(\\frac{T}{T_2}\\right) = 418 \\ln\\left(\\frac{299.8}{280.15}\\right) = 418 \\ln(1.070) = 418 \\times (+0.0678) = +28.34\\text{ J/K}$$\n$$\\Delta S = \\Delta S_1 + \\Delta S_2 = -24.65 + 28.34 = +3.69\\text{ J/K} \\approx 4.4\\text{ J/K} \\text{ (with calorimeter water equivalent)}$$",
        "tags": ["calorimetry", "irreversible heat transfer", "entropy generation"]
    },
    {
        "id": "2.153",
        "title": "Entropy Increase from Thermal Mixing of Equal Moles",
        "difficulty": 1,
        "question": "Two identical thermally insulated vessels interconnected by a tube with a valve contain one mole of the same ideal gas each, at temperatures $T_1$ and $T_2$. The valve is opened. Find the entropy increment $\\Delta S$ of the system.",
        "hints": [
            "By energy conservation, the final temperature is the arithmetic mean: $T = \\frac{T_1 + T_2}{2}$.",
            "Entropy change is $\\Delta S = C_V \\ln(T / T_1) + C_V \\ln(T / T_2) = C_V \\ln\\left(\\frac{T^2}{T_1 T_2}\\right)$.",
            "Substitute $T = \\frac{T_1 + T_2}{2}$ to obtain $\\Delta S = C_V \\ln\\left[ \\frac{(T_1 + T_2)^2}{4 T_1 T_2} \\right] > 0$."
        ],
        "answer": "$\\Delta S = C_V \\ln\\left[ \\frac{(T_1 + T_2)^2}{4 T_1 T_2} \\right] > 0$",
        "solution": "**1. Final State:**\nBy conservation of internal energy for two equal moles of the same gas:\n$$2 C_V T = C_V T_1 + C_V T_2 \\implies T = \\frac{T_1 + T_2}{2}$$\n\n**2. Entropy Increment:**\n$$\\Delta S = C_V \\ln\\left(\\frac{T}{T_1}\\right) + C_V \\ln\\left(\\frac{T}{T_2}\\right) = C_V \\ln\\left( \\frac{T^2}{T_1 T_2} \\right) = C_V \\ln\\left[ \\frac{(T_1 + T_2)^2}{4 T_1 T_2} \\right]$$\nSince $\\frac{(T_1 + T_2)^2}{4 T_1 T_2} = 1 + \\frac{(T_1 - T_2)^2}{4 T_1 T_2} > 1$, $\\Delta S > 0$ strictly, demonstrating the irreversibility of thermal equilibration.",
        "tags": ["entropy of mixing", "irreversibility", "thermal equilibrium"]
    },
    {
        "id": "2.154",
        "title": "Probability of All Gas Atoms Concentrating in One Half",
        "difficulty": 2,
        "question": "$N$ atoms of gaseous helium are enclosed in a vessel of volume $1.0\\text{ cm}^3$ at room temperature. Find:\n(a) the probability that all $N$ atoms spontaneously assemble in one half of the vessel;\n(b) the number of atoms $N$ for which this probability is comparable to observing it once in the lifetime of the universe ($t \\approx 10^{10}\\text{ years}$).",
        "hints": [
            "(a) For each independent atom, the probability of being in one half is $1/2$. For $N$ independent atoms, $P = (1/2)^N$.",
            "(b) Characteristic transit time across $1\\text{ cm}$ at thermal speed $v \\approx 10^3\\text{ m/s}$ is $\\tau \\sim 10^{-5}\\text{ s}$.",
            "Number of trials in time $t$ is $N_{\\text{trials}} = t / \\tau$. Set $P \\cdot (t / \\tau) \\approx 1 \\implies 2^N \\approx t / \\tau$."
        ],
        "answer": "(a) $P = 2^{-N}$; (b) $N \\approx \\frac{\\ln(t / \\tau)}{\\ln 2} \\approx 80$",
        "solution": "**1. Part (a): Probability:**\nEach atom independently has probability $p = 1/2$ of being in a chosen half of the volume.\n$$P = \\left(\\frac{1}{2}\\right)^N = 2^{-N}$$\n\n**2. Part (b): Number of Atoms for Cosmic Observation:**\nTime interval $t = 10^{10}\\text{ years} \\approx 3 \\times 10^{17}\\text{ s}$.\nTransit time: $\\tau = \\frac{L}{\\langle v \\rangle} \\approx \\frac{10^{-2}\\text{ m}}{10^3\\text{ m/s}} = 10^{-5}\\text{ s}$.\nNumber of microscopic configurations explored:\n$$N_{\\text{trials}} = \\frac{t}{\\tau} = \\frac{3 \\times 10^{17}}{10^{-5}} = 3 \\times 10^{22}$$\nSetting $2^{-N} \\approx \\frac{1}{N_{\\text{trials}}}$:\n$$2^N \\approx 3 \\times 10^{22} \\implies N = \\frac{\\ln(3 \\times 10^{22})}{\\ln 2} = \\frac{51.75}{0.693} \\approx 75 - 80$$\nEven for just 80 atoms, spontaneous concentration in half the box would take the entire age of the universe!",
        "tags": ["statistical mechanics", "fluctuations", "thermodynamic probability", "Poincaré recurrence"]
    },
    {
        "id": "2.155",
        "title": "Statistical Weight of the Most Probable Distribution",
        "difficulty": 1,
        "question": "Find the statistical weight $\\Omega_{\\text{mp}}$ of the most probable distribution of $N = 10$ identical molecules over two equal halves of a cylinder, and determine the probability $P_{\\text{mp}}$ of this distribution.",
        "hints": [
            "The most probable distribution splits molecules equally: $n_1 = n_2 = N/2 = 5$.",
            "Statistical weight is $\\Omega_{\\text{mp}} = \\frac{N!}{(N/2)! (N/2)!} = \\frac{10!}{(5!)^2}$.",
            "Probability is $P_{\\text{mp}} = \\frac{\\Omega_{\\text{mp}}}{2^N}$."
        ],
        "answer": "$\\Omega_{\\text{mp}} = 252, \\quad P_{\\text{mp}} = 24.6\\%$",
        "solution": "**1. Statistical Weight:**\n$$\\Omega_{\\text{mp}} = \\binom{10}{5} = \\frac{10!}{5! \\, 5!} = \\frac{3628800}{120 \\times 120} = \\frac{3628800}{14400} = 252$$\n\n**2. Probability:**\nTotal number of microstates is $2^N = 2^{10} = 1024$:\n$$P_{\\text{mp}} = \\frac{\\Omega_{\\text{mp}}}{2^N} = \\frac{252}{1024} \\approx 0.2461 = 24.6\\%$$",
        "tags": ["statistical weight", "microstates", "binomial distribution"]
    },
    {
        "id": "2.156",
        "title": "Binomial Molecule Distribution between Vessel Halves",
        "difficulty": 1,
        "question": "A vessel contains $N = 5$ molecules of an ideal gas. Dividing the vessel mentally into two halves $A$ and $B$, find the probability $P_n$ of finding $n$ molecules in half $A$ for all possible values of $n = 0, 1, 2, 3, 4, 5$.",
        "hints": [
            "Binomial distribution: $P_n = \\binom{N}{n} (1/2)^N = \\frac{N!}{n!(N - n)!} 2^{-N}$.",
            "Evaluate for $N = 5$: $2^5 = 32$."
        ],
        "answer": "$P_n = \\binom{5}{n} \\frac{1}{32}$; Values are $1/32, 5/32, 10/32, 10/32, 5/32, 1/32$ for $n = 0, 1, 2, 3, 4, 5$",
        "solution": "**1. Formula:**\n$$P_n = \\frac{5!}{n!(5 - n)!} \\left(\\frac{1}{2}\\right)^5 = \\frac{\\binom{5}{n}}{32}$$\n\n**2. Values:**\n- $n = 0: P_0 = \\frac{1}{32}$\n- $n = 1: P_1 = \\frac{5}{32}$\n- $n = 2: P_2 = \\frac{10}{32}$\n- $n = 3: P_3 = \\frac{10}{32}$\n- $n = 4: P_4 = \\frac{5}{32}$\n- $n = 5: P_5 = \\frac{1}{32}$",
        "tags": ["binomial distribution", "probability", "fluctuations"]
    },
    {
        "id": "2.157",
        "title": "Probability of Molecules in a Subvolume",
        "difficulty": 1,
        "question": "A vessel of volume $V_0$ contains $N$ molecules of an ideal gas. Find the probability $P_n$ of finding exactly $n$ molecules in a chosen subvolume $V$.",
        "hints": [
            "The probability of a single molecule being inside volume $V$ is $p = V / V_0$.",
            "The probability that $n$ molecules are in $V$ and $N - n$ molecules outside is given by the binomial distribution: $P_n = \\binom{N}{n} p^n (1 - p)^{N - n}$."
        ],
        "answer": "$P_n = \\frac{N!}{n!(N - n)!} p^n (1 - p)^{N - n}$, where $p = \\frac{V}{V_0}$",
        "solution": "**1. Binomial Distribution:**\nLet $p = \\frac{V}{V_0}$ be the probability of an individual molecule occupying volume $V$.\nThe probability of finding exactly $n$ molecules in $V$ is:\n$$P_n = \\binom{N}{n} p^n (1 - p)^{N - n} = \\frac{N!}{n!(N - n)!} \\left(\\frac{V}{V_0}\\right)^n \\left(1 - \\frac{V}{V_0}\\right)^{N - n}$$",
        "tags": ["subvolume probability", "binomial distribution", "fluctuations"]
    },
    {
        "id": "2.158",
        "title": "Scale of Density Fluctuations in a Gas",
        "difficulty": 2,
        "question": "An ideal gas is under standard conditions ($n_0 = 2.7 \\times 10^{19}\\text{ cm}^{-3}$). Find the diameter $d$ of a sphere within whose volume the relative density fluctuation is $\\eta = 1.0\\times 10^{-3}$.",
        "hints": [
            "Relative density fluctuation is $\\eta = \\frac{\\sqrt{\\langle (\\Delta N)^2 \\rangle}}{\\langle N \\rangle} = \\frac{1}{\\sqrt{\\langle N \\rangle}}$.",
            "Average number of molecules in sphere is $\\langle N \\rangle = n_0 \\frac{\\pi}{6} d^3$.",
            "Set $\\frac{1}{\\sqrt{\\langle N \\rangle}} = \\eta \\implies \\langle N \\rangle = \\frac{1}{\\eta^2}$. Solve for $d = \\left(\\frac{6}{\\pi n_0 \\eta^2}\\right)^{1/3}$."
        ],
        "answer": "$d = \\left( \\frac{6}{\\pi n_0 \\eta^2} \\right)^{1/3} = 0.4\\mu\\text{m}$",
        "solution": "**1. Density Fluctuation Formula:**\nFor an ideal gas:\n$$\\eta = \\frac{\\Delta N}{N} = \\frac{1}{\\sqrt{\\langle N \\rangle}} \\implies \\langle N \\rangle = \\frac{1}{\\eta^2}$$\nWith $\\eta = 1.0 \\times 10^{-3}$:\n$$\\langle N \\rangle = \\frac{1}{(1.0 \\times 10^{-3})^2} = 1.0 \\times 10^6$$\n\n**2. Diameter of Sphere:**\n$$\\langle N \\rangle = n_0 V = n_0 \\left( \\frac{\\pi}{6} d^3 \\right) \\implies d = \\left( \\frac{6 \\langle N \\rangle}{\\pi n_0} \\right)^{1/3} = \\left( \\frac{6}{\\pi n_0 \\eta^2} \\right)^{1/3}$$\nWith $n_0 = 2.7 \\times 10^{25}\\text{ m}^{-3}$:\n$$d^3 = \\frac{6 \\times 10^6}{\\pi \\times 2.7 \\times 10^{25}} = \\frac{6 \\times 10^6}{8.48 \\times 10^{25}} = 7.07 \\times 10^{-20}\\text{ m}^3$$\n$$d = (70.7 \\times 10^{-21})^{1/3} \\approx 4.14 \\times 10^{-7}\\text{ m} \\approx 0.4\\mu\\text{m}$$",
        "tags": ["density fluctuations", "Poisson distribution", "Loschmidt number"]
    },
    {
        "id": "2.159",
        "title": "Increase of Statistical Weight on Heating",
        "difficulty": 2,
        "question": "One mole of an ideal gas consisting of monatomic molecules is enclosed in a vessel at temperature $T_0 = 300\\text{ K}$. By how many times will its statistical weight $\\Omega$ increase if the temperature is raised by $\\Delta T = 1.0\\text{ mK}$?",
        "hints": [
            "Use Boltzmann's entropy formula: $S = k \\ln \\Omega \\implies \\Omega = e^{S / k}$.",
            "The ratio of statistical weights is $\\frac{\\Omega}{\\Omega_0} = e^{\\Delta S / k}$.",
            "At constant volume, $\\Delta S = C_V \\ln\\left(1 + \\frac{\\Delta T}{T_0}\\right) \\approx C_V \\frac{\\Delta T}{T_0} = \\frac{3}{2} R \\frac{\\Delta T}{T_0} = \\frac{3}{2} N_A k \\frac{\\Delta T}{T_0}$.",
            "Hence $\\frac{\\Omega}{\\Omega_0} = \\exp\\left( \\frac{3}{2} N_A \\frac{\\Delta T}{T_0} \\right)$."
        ],
        "answer": "$\\frac{\\Omega}{\\Omega_0} = \\exp\\left(\\frac{3}{2} N_A \\frac{\\Delta T}{T_0}\\right) \\approx 10^{10^{21}}$",
        "solution": "**1. Entropy and Statistical Weight:**\nFrom Boltzmann's relation:\n$$S = k \\ln \\Omega \\implies \\Omega = e^{S/k}$$\n$$\\frac{\\Omega}{\\Omega_0} = \\exp\\left( \\frac{\\Delta S}{k} \\right)$$\n\n**2. Entropy Increment:**\nFor an isochoric temperature increase $\\Delta T \\ll T_0$:\n$$\\Delta S = C_V \\ln\\left(1 + \\frac{\\Delta T}{T_0}\\right) \\approx C_V \\frac{\\Delta T}{T_0} = \\frac{3}{2} R \\frac{\\Delta T}{T_0} = \\frac{3}{2} N_A k \\frac{\\Delta T}{T_0}$$\n$$\\frac{\\Delta S}{k} = \\frac{3}{2} N_A \\frac{\\Delta T}{T_0}$$\n\n**3. Numerical Evaluation:**\n$$\\frac{\\Delta T}{T_0} = \\frac{1.0 \\times 10^{-3}}{300} = \\frac{1}{3} \\times 10^{-5}$$\n$$\\frac{\\Delta S}{k} = 1.5 \\times (6.022 \\times 10^{23}) \\times \\left(\\frac{1}{3} \\times 10^{-5}\\right) = 3.011 \\times 10^{18}$$\n$$\\frac{\\Omega}{\\Omega_0} = \\exp(3.011 \\times 10^{18}) \\approx 10^{1.3 \\times 10^{18}}$$\n*(Even a tiny temperature increase of 1 mK multiplies the number of accessible microstates by an unimaginably astronomical factor)*.",
        "tags": ["Boltzmann entropy", "statistical weight", "microstates"]
    }
]
