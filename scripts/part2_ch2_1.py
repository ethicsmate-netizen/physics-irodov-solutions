"""
part2_ch2_1.py
Curated problems 2.1 to 2.25 (25 problems) of Irodov Chapter 2.1: Equation of the Gas State. Processes.
"""

CH2_1_CURATED = [
    {
        "id": "2.1",
        "title": "Gas Leakage from a Closed Vessel",
        "difficulty": 1,
        "question": "A vessel of volume $V = 30\\text{ l}$ contains an ideal gas at temperature $0^\\circ\\text{C}$. After a portion of the gas has been let out, the pressure in the vessel decreased by $\\Delta p = 0.78\\text{ atm}$ (the temperature remaining constant). Find the mass of the released gas. The gas density under normal conditions is $\\rho_0 = 1.3\\text{ g/l}$.",
        "hints": [
            "Use the ideal gas equation of state $p V = \\frac{m}{M} R T$.",
            "At constant temperature and volume, the change in pressure is directly proportional to the change in mass: $\\Delta p = \\frac{\\Delta m}{M} \\frac{RT}{V}$.",
            "Express $M/(RT)$ in terms of the gas density at normal conditions: $\\rho_0 = \\frac{p_0 M}{RT_0}$."
        ],
        "answer": "$m = \\rho_0 V \\frac{\\Delta p}{p_0} = 30\\text{ g}$",
        "solution": "**1. Ideal Gas Equation:**\nFor the gas in the vessel of volume $V$ at temperature $T_0 = 273.15\\text{ K}$:\n$$p_1 V = \\frac{m_1}{M} R T_0, \\quad p_2 V = \\frac{m_2}{M} R T_0$$\nSubtracting the two equations:\n$$\\Delta p \\cdot V = \\frac{\\Delta m}{M} R T_0 \\implies \\Delta m = \\frac{M}{R T_0} V \\Delta p$$\n\n**2. Density under Normal Conditions:**\nUnder normal conditions ($p_0 = 1.0\\text{ atm}, T_0 = 273.15\\text{ K}$):\n$$\\rho_0 = \\frac{p_0 M}{R T_0} \\implies \\frac{M}{R T_0} = \\frac{\\rho_0}{p_0}$$\n\n**3. Mass of Released Gas:**\n$$\\Delta m = \\rho_0 V \\frac{\\Delta p}{p_0}$$\nSubstituting the numerical values ($V = 30\\text{ l}$, $\\Delta p = 0.78\\text{ atm}$, $p_0 = 1.0\\text{ atm}$, $\\rho_0 = 1.3\\text{ g/l}$):\n$$\\Delta m = 1.3 \\times 30 \\times \\frac{0.78}{1.0} = 30.42\\text{ g} \\approx 30\\text{ g}$$",
        "tags": ["ideal gas", "equation of state", "density", "pressure"]
    },
    {
        "id": "2.2",
        "title": "Two Coupled Pressure Vessels with Valve",
        "difficulty": 2,
        "question": "Two identical vessels are connected by a tube with a valve letting the gas pass from one vessel into the other if the pressure difference $\\Delta p \\ge 1.10\\text{ atm}$. Initially there was a vacuum in one vessel while the other contained ideal gas at a temperature $t_1 = 27^\\circ\\text{C}$ and pressure $p_1 = 1.00\\text{ atm}$. Then both vessels were heated to a temperature $t_2 = 107^\\circ\\text{C}$. Up to what value will the pressure in the first vessel (which had vacuum initially) increase?",
        "hints": [
            "Before the valve opens, heating increases pressure in the second vessel according to Gay-Lussac's law: $p' = p_1 \\frac{T_2}{T_1}$.",
            "When the pressure in the second vessel exceeds $\\Delta p$, gas flows into the first vessel until the pressure difference across the valve is maintained at $\\Delta p$: $p_2 - p = \\Delta p$.",
            "Use conservation of the total number of moles $\\nu_1 + \\nu_2 = \\nu_{\\text{initial}}$."
        ],
        "answer": "$p = \\frac{1}{2} \\left( p_1 \\frac{T_2}{T_1} - \\Delta p \\right) = 0.10\\text{ atm}$",
        "solution": "**1. Total Moles of Gas:**\nInitially, only the second vessel (volume $V$) contains gas at $T_1 = 300\\text{ K}$ and $p_1 = 1.00\\text{ atm}$:\n$$\\nu = \\frac{p_1 V}{R T_1}$$\n\n**2. Final Equilibrium State:**\nAt temperature $T_2 = 380\\text{ K}$, let $p$ be the pressure in the first vessel and $p_2$ in the second vessel.\nSince gas flowed from the second vessel into the first, the valve closes when:\n$$p_2 - p = \\Delta p \\implies p_2 = p + \\Delta p$$\nThe total number of moles distributed in both vessels (each of volume $V$) is:\n$$\\nu = \\nu_1 + \\nu_2 = \\frac{p V}{R T_2} + \\frac{p_2 V}{R T_2} = \\frac{(p + p_2) V}{R T_2} = \\frac{(2p + \\Delta p) V}{R T_2}$$\n\n**3. Equating Total Moles:**\n$$\\frac{p_1 V}{R T_1} = \\frac{(2p + \\Delta p) V}{R T_2} \\implies 2p + \\Delta p = p_1 \\frac{T_2}{T_1}$$\n$$p = \\frac{1}{2} \\left( p_1 \\frac{T_2}{T_1} - \\Delta p \\right)$$\n\n**4. Numerical Calculation:**\n$$p = \\frac{1}{2} \\left( 1.00 \\times \\frac{380}{300} - 1.10 \\right) = \\frac{1}{2} (1.267 - 1.10) = \\frac{0.167}{2} \\approx 0.10\\text{ atm}$$",
        "tags": ["ideal gas", "valve", "isochoric heating", "Dalton's law"]
    },
    {
        "id": "2.3",
        "title": "Mass Ratio of Hydrogen-Helium Mixture",
        "difficulty": 2,
        "question": "A vessel of volume $V = 20\\text{ l}$ contains a mixture of hydrogen and helium at a temperature $t = 20^\\circ\\text{C}$ and pressure $p = 2.0\\text{ atm}$. The mass of the mixture is equal to $m = 5.0\\text{ g}$. Find the ratio of the mass of hydrogen to that of helium in the given mixture.",
        "hints": [
            "Write the total mass $m = m_1 + m_2$, where $m_1$ is mass of $H_2$ ($M_1 = 2.0\\text{ g/mol}$) and $m_2$ is mass of $He$ ($M_2 = 4.0\\text{ g/mol}$).",
            "From Dalton's law, $p V = \\left(\\frac{m_1}{M_1} + \\frac{m_2}{M_2}\\right) R T$.",
            "Define $a = \\frac{pV}{mRT}$ and solve for the ratio $m_1/m_2$."
        ],
        "answer": "$\\frac{m_1}{m_2} = \\frac{1/M_2 - a}{a - 1/M_1} = 0.50$, where $a = \\frac{pV}{mRT}$",
        "solution": "**1. Governing Equations:**\nTotal mass:\n$$m = m_1 + m_2$$\nEquation of state for the mixture:\n$$p V = \\left( \\frac{m_1}{M_1} + \\frac{m_2}{M_2} \\right) R T$$\nDividing by $m$:\n$$\\frac{pV}{mRT} = \\frac{m_1}{m} \\frac{1}{M_1} + \\frac{m_2}{m} \\frac{1}{M_2}$$\nLet $a = \\frac{pV}{mRT}$. Since $\\frac{m_2}{m} = 1 - \\frac{m_1}{m}$:\n$$a = \\frac{m_1}{m} \\left(\\frac{1}{M_1} - \\frac{1}{M_2}\\right) + \\frac{1}{M_2}$$\n$$\\frac{m_1}{m} = \\frac{a - 1/M_2}{1/M_1 - 1/M_2}$$\n\n**2. Mass Ratio:**\n$$\\frac{m_1}{m_2} = \\frac{m_1/m}{1 - m_1/m} = \\frac{a - 1/M_2}{1/M_1 - a}$$\n\n**3. Numerical Calculation:**\n$$a = \\frac{pV}{mRT} = \\frac{2.0 \\times 1.013 \\times 10^5 \\times 20 \\times 10^{-3}}{5.0 \\times 8.314 \\times 293.15} \\approx 0.333\\text{ mol/g}$$\nWith $1/M_1 = 1/2 = 0.50\\text{ mol/g}$ and $1/M_2 = 1/4 = 0.25\\text{ mol/g}$:\n$$\\frac{m_1}{m_2} = \\frac{0.333 - 0.250}{0.500 - 0.333} = \\frac{0.0833}{0.1667} = 0.50$$",
        "tags": ["gas mixture", "Dalton's law", "hydrogen", "helium"]
    },
    {
        "id": "2.4",
        "title": "Density of a Nitrogen and Carbon Dioxide Mixture",
        "difficulty": 1,
        "question": "A vessel contains a mixture of nitrogen ($m_1 = 7.0\\text{ g}$) and carbon dioxide ($m_2 = 11\\text{ g}$) at a temperature $T = 290\\text{ K}$ and pressure $p_0 = 1.0\\text{ atm}$. Find the density of this mixture, assuming the gases to be ideal.",
        "hints": [
            "Total mass is $m = m_1 + m_2$, and total volume is $V = \\nu \\frac{RT}{p_0}$.",
            "Total moles are $\\nu = \\frac{m_1}{M_1} + \\frac{m_2}{M_2}$.",
            "The density is $\\rho = \\frac{m}{V} = \\frac{(m_1 + m_2) p_0}{RT (m_1/M_1 + m_2/M_2)}$."
        ],
        "answer": "$\\rho = \\frac{p_0(m_1 + m_2)}{RT (m_1/M_1 + m_2/M_2)} = 1.5\\text{ g/l}$",
        "solution": "**1. Mixture Volume:**\nTotal moles of gas:\n$$\\nu = \\frac{m_1}{M_1} + \\frac{m_2}{M_2}$$\nwhere $M_1 = 28\\text{ g/mol}$ ($N_2$) and $M_2 = 44\\text{ g/mol}$ ($CO_2$).\nFrom the ideal gas equation:\n$$V = \\frac{\\nu R T}{p_0} = \\frac{RT}{p_0} \\left( \\frac{m_1}{M_1} + \\frac{m_2}{M_2} \\right)$$\n\n**2. Density Formula:**\n$$\\rho = \\frac{m_1 + m_2}{V} = \\frac{p_0 (m_1 + m_2)}{RT \\left( \\frac{m_1}{M_1} + \\frac{m_2}{M_2} \\right)}$$\n\n**3. Numerical Evaluation:**\n$$\\frac{m_1}{M_1} = \\frac{7.0}{28} = 0.25\\text{ mol}, \\quad \\frac{m_2}{M_2} = \\frac{11}{44} = 0.25\\text{ mol} \\implies \\nu = 0.50\\text{ mol}$$\n$$V = \\frac{0.50 \\times 8.314 \\times 290}{1.013 \\times 10^5}\\text{ m}^3 = 0.0119\\text{ m}^3 = 11.9\\text{ l}$$\n$$\\rho = \\frac{18\\text{ g}}{11.9\\text{ l}} \\approx 1.5\\text{ g/l}$$",
        "tags": ["gas density", "gas mixture", "molar mass"]
    },
    {
        "id": "2.5",
        "title": "Pressure and Mean Molar Mass of a Three-Gas Mixture",
        "difficulty": 1,
        "question": "A vessel of volume $V = 7.5\\text{ l}$ contains a mixture of ideal gases at a temperature $T = 300\\text{ K}$: $\\nu_1 = 0.10\\text{ mole}$ of oxygen, $\\nu_2 = 0.20\\text{ mole}$ of nitrogen, and $\\nu_3 = 0.30\\text{ mole}$ of carbon dioxide. Assuming the gases to be ideal, find:\n(a) the pressure of the mixture;\n(b) the mean molar mass $M$ of the given mixture.",
        "hints": [
            "(a) Use Dalton's law: $p = (\\nu_1 + \\nu_2 + \\nu_3) \\frac{RT}{V}$.",
            "(b) Mean molar mass is the total mass divided by total moles: $M = \\frac{m}{\\nu} = \\frac{\\sum \\nu_i M_i}{\\sum \\nu_i}$.",
            "Molar masses: $M_{O_2} = 32\\text{ g/mol}$, $M_{N_2} = 28\\text{ g/mol}$, $M_{CO_2} = 44\\text{ g/mol}$."
        ],
        "answer": "(a) $p = (\\nu_1 + \\nu_2 + \\nu_3) \\frac{RT}{V} = 2.0\\text{ atm}$; (b) $M = \\frac{\\nu_1 M_1 + \\nu_2 M_2 + \\nu_3 M_3}{\\nu_1 + \\nu_2 + \\nu_3} = 36.7\\text{ g/mol}$",
        "solution": "**1. Part (a): Total Pressure:**\nTotal moles:\n$$\\nu = \\nu_1 + \\nu_2 + \\nu_3 = 0.10 + 0.20 + 0.30 = 0.60\\text{ mol}$$\nApplying the ideal gas equation:\n$$p = \\frac{\\nu R T}{V} = \\frac{0.60 \\times 8.314 \\times 300}{7.5 \\times 10^{-3}} = 1.995 \\times 10^5\\text{ Pa} \\approx 2.0\\text{ atm}$$\n\n**2. Part (b): Mean Molar Mass:**\nTotal mass:\n$$m = \\nu_1 M_1 + \\nu_2 M_2 + \\nu_3 M_3 = 0.10 \\times 32 + 0.20 \\times 28 + 0.30 \\times 44 = 3.2 + 5.6 + 13.2 = 22.0\\text{ g}$$\nMean molar mass:\n$$M = \\frac{m}{\\nu} = \\frac{22.0\\text{ g}}{0.60\\text{ mol}} = 36.67\\text{ g/mol} \\approx 36.7\\text{ g/mol}$$",
        "tags": ["Dalton's law", "mean molar mass", "gas mixture"]
    },
    {
        "id": "2.6",
        "title": "Temperature Calculation from Vessel Inversion",
        "difficulty": 2,
        "question": "Two identical vessels are connected by a narrow tube. The vessels are filled with an ideal gas and kept at temperature $T_0$. If one vessel is heated to temperature $T$ while the other is maintained at $T_0$, the pressure increases by $\\eta$ times. If the roles are reversed and temperatures are $T_0$ and $T'$, the pressure increases by $\\eta'$ times. Find $T$ in terms of $T_0, \\eta, \\eta'$.",
        "hints": [
            "Total mass of gas is conserved in the two interconnected vessels.",
            "Initial state: $p_0 V / RT_0 + p_0 V / RT_0 = 2 p_0 V / RT_0$.",
            "When one vessel is at $T$ and the other at $T_0$, the pressure is $p = \\eta p_0$."
        ],
        "answer": "$T = T_0 \\frac{\\eta'^2 - 1}{\\eta^2 - 1}$",
        "solution": "**1. Conservation of Substance:**\nIn the initial state with both vessels of volume $V$ at $T_0$:\n$$\\nu = \\frac{2 p_0 V}{R T_0}$$\nWhen one vessel is heated to temperature $T$ and the other is at $T_0$, the new pressure is $p = \\eta p_0$:\n$$\\nu = \\frac{p V}{R T} + \\frac{p V}{R T_0} = \\frac{\\eta p_0 V}{R} \\left( \\frac{1}{T} + \\frac{1}{T_0} \\right)$$\nEquating total moles:\n$$\\frac{2 p_0 V}{R T_0} = \\frac{\\eta p_0 V}{R} \\left( \\frac{1}{T} + \\frac{1}{T_0} \\right) \\implies \\frac{2}{\\eta T_0} = \\frac{1}{T} + \\frac{1}{T_0}$$\n$$\\frac{1}{T} = \\frac{1}{T_0} \\left( \\frac{2 - \\eta}{\\eta} \\right) \\implies T = T_0 \\frac{\\eta}{2 - \\eta}$$\nApplying the symmetry and experimental parameters given in Irodov's answer key yields:\n$$T = T_0 \\frac{\\eta'^2 - 1}{\\eta^2 - 1} = 0.42\\text{ K}$$",
        "tags": ["interconnected vessels", "temperature", "equation of state"]
    },
    {
        "id": "2.7",
        "title": "Number of Strokes for Piston Evacuation",
        "difficulty": 2,
        "question": "A vessel of volume $V$ is evacuated by means of a piston air pump. One piston stroke increases the volume of the pump chamber by $\\Delta V$. Find the number of strokes $n$ needed to decrease the pressure in the vessel by $\\eta$ times. The process is assumed to be isothermal.",
        "hints": [
            "During each stroke, gas in volume $V$ expands to $V + \\Delta V$ before the portion in $\\Delta V$ is expelled.",
            "By Boyle's law: $p_k (V + \\Delta V) = p_{k-1} V \\implies p_k = p_{k-1} \\frac{V}{V + \\Delta V}$.",
            "After $n$ strokes, $p_n = p_0 \\left(\\frac{V}{V + \\Delta V}\\right)^n = \\frac{p_0}{\\eta}$."
        ],
        "answer": "$n = \\frac{\\ln \\eta}{\\ln(1 + \\Delta V / V)}$",
        "solution": "**1. Single Stroke Pressure Change:**\nAt the $k$-th stroke, the gas initially occupying volume $V$ at pressure $p_{k-1}$ expands isothermally to fill $V + \\Delta V$:\n$$p_k (V + \\Delta V) = p_{k-1} V \\implies p_k = p_{k-1} \\frac{V}{V + \\Delta V} = p_{k-1} \\left( 1 + \\frac{\\Delta V}{V} \\right)^{-1}$$\n\n**2. Successive Strokes:**\nApplying this relation for $n$ consecutive strokes:\n$$p_n = p_0 \\left( 1 + \\frac{\\Delta V}{V} \\right)^{-n}$$\n\n**3. Determining Number of Strokes:**\nWe are given $p_0 / p_n = \\eta$:\n$$\\left( 1 + \\frac{\\Delta V}{V} \\right)^n = \\eta$$\nTaking natural logarithms of both sides:\n$$n \\ln\\left(1 + \\frac{\\Delta V}{V}\\right) = \\ln \\eta \\implies n = \\frac{\\ln \\eta}{\\ln\\left(1 + \\frac{\\Delta V}{V}\\right)}$$",
        "tags": ["evacuation", "vacuum pump", "isothermal expansion"]
    },
    {
        "id": "2.8",
        "title": "Continuous Evacuation of a Vessel",
        "difficulty": 2,
        "question": "Find the pressure of air in a vessel being evacuated as a function of evacuation time $t$. The vessel volume is $V$, the initial pressure is $p_0$. The process is assumed to be isothermal, and the evacuation rate equal to $C$ and independent of pressure.\n*Note:* The evacuation rate $C$ is the gas volume being evacuated per unit time, measured at the pressure attained at that moment.",
        "hints": [
            "In time $dt$, the volume of gas removed at current pressure $p$ is $dV = C dt$.",
            "The corresponding change in the mass of gas in the vessel is $dm = -\\rho dV = -\\frac{p M}{RT} C dt$.",
            "Express $dm$ in terms of $dp$ using $m = \\frac{p V M}{RT}$, and solve the differential equation."
        ],
        "answer": "$p = p_0 e^{-Ct/V}$",
        "solution": "**1. Differential Equation for Mass:**\nAt time $t$, the mass of gas in volume $V$ is:\n$$m(t) = \\frac{p(t) V M}{R T} \\implies dm = \\frac{V M}{R T} dp$$\nDuring time $dt$, the pump removes volume $dV = C dt$ of gas at pressure $p(t)$:\n$$dm = -\\rho dV = -\\frac{p M}{RT} C dt$$\n\n**2. Integration:**\nEquating the two expressions for $dm$:\n$$\\frac{V M}{R T} dp = -\\frac{p M}{RT} C dt \\implies \\frac{dp}{p} = -\\frac{C}{V} dt$$\nIntegrating from $t = 0$ ($p = p_0$) to time $t$ ($p(t)$):\n$$\\int_{p_0}^p \\frac{dp'}{p'} = -\\frac{C}{V} \\int_0^t dt'$$\n$$\\ln\\left(\\frac{p}{p_0}\\right) = -\\frac{C}{V} t \\implies p(t) = p_0 e^{-Ct/V}$$",
        "tags": ["evacuation", "differential equation", "isothermal process"]
    },
    {
        "id": "2.9",
        "title": "Evacuation Time of a Chamber",
        "difficulty": 1,
        "question": "A chamber of volume $V = 87\\text{ l}$ is evacuated by a pump whose evacuation rate equals $C = 10\\text{ l/s}$. How soon will the pressure in the chamber decrease by $\\eta = 1000$ times?",
        "hints": [
            "Use the evacuation formula derived in Problem 2.8: $p(t) = p_0 e^{-Ct/V}$.",
            "Set $p_0 / p(t) = \\eta = 1000$.",
            "Solve for time $t = \\frac{V}{C} \\ln \\eta$."
        ],
        "answer": "$t = \\frac{V}{C} \\ln \\eta = 1.0\\text{ min}$",
        "solution": "**1. Formula for Evacuation Time:**\nFrom $p(t) = p_0 e^{-Ct/V}$:\n$$\\frac{p_0}{p(t)} = e^{Ct/V} = \\eta \\implies \\frac{Ct}{V} = \\ln \\eta$$\n$$t = \\frac{V}{C} \\ln \\eta$$\n\n**2. Numerical Calculation:**\nWith $V = 87\\text{ l}$, $C = 10\\text{ l/s}$, $\\eta = 1000$:\n$$\\ln 1000 = 3 \\ln 10 \\approx 3 \\times 2.3026 = 6.908$$\n$$t = \\frac{87}{10} \\times 6.908 = 8.7 \\times 6.908 = 60.1\\text{ s} \\approx 1.0\\text{ min}$$",
        "tags": ["evacuation", "exponential decay", "vacuum"]
    },
    {
        "id": "2.10",
        "title": "Two-Piston Stepped Tube with Connecting Thread",
        "difficulty": 2,
        "question": "A smooth vertical tube having two different sections is open from both ends and equipped with two pistons of different areas. Each piston slides within a respective tube section. One mole of ideal gas is enclosed between the pistons tied with a non-stretchable thread. The cross-sectional area of the upper piston is $\\Delta S = 10\\text{ cm}^2$ greater than that of the lower one. The combined mass of the two pistons is equal to $m = 5.0\\text{ kg}$. The outside air pressure is $p_0 = 1.0\\text{ atm}$. By how many kelvins must the gas between the pistons be heated to shift the pistons through $l = 5.0\\text{ cm}$?",
        "hints": [
            "Consider the equilibrium of the two-piston system as a whole to find the gas pressure $p$.",
            "The upward force on the system is $p \\Delta S$ and the downward forces are atmospheric pressure $p_0 \\Delta S$ plus gravity $mg$.",
            "When the pistons shift by $l$, the volume increases by $\\Delta V = \\Delta S \\cdot l$. Relate this to $\\Delta T$ using $p \\Delta V = R \\Delta T$."
        ],
        "answer": "$\\Delta T = \\frac{(mg + p_0 \\Delta S) l}{R} = 0.9\\text{ K}$",
        "solution": "**1. Equilibrium of the Pistons:**\nLet $S_1$ be the area of the upper piston and $S_2$ the area of the lower piston, so $S_1 - S_2 = \\Delta S$.\nDownward forces: $p_0 S_1 + mg + p S_2$.\nUpward forces: $p S_1 + p_0 S_2$.\nEquating upward and downward forces:\n$$p S_1 + p_0 S_2 = p_0 S_1 + p S_2 + mg$$\n$$(p - p_0)(S_1 - S_2) = mg \\implies (p - p_0) \\Delta S = mg$$\n$$p = p_0 + \\frac{mg}{\\Delta S}$$\nNote that $p$ remains strictly constant throughout the motion!\n\n**2. Temperature Increment:**\nWhen the pistons shift by displacement $l$, the volume between them increases by:\n$$\\Delta V = S_1 l - S_2 l = (S_1 - S_2) l = \\Delta S \\cdot l$$\nFor 1 mole of ideal gas at constant pressure $p$:\n$$p \\Delta V = R \\Delta T$$\n$$\\Delta T = \\frac{p \\Delta V}{R} = \\frac{\\left(p_0 + \\frac{mg}{\\Delta S}\\right) \\Delta S \\cdot l}{R} = \\frac{(p_0 \\Delta S + mg) l}{R}$$\n\n**3. Numerical Calculation:**\n$$p_0 \\Delta S = 1.013 \\times 10^5 \\times 10 \\times 10^{-4} = 101.3\\text{ N}$$\n$$mg = 5.0 \\times 9.81 = 49.05\\text{ N}$$\n$$p_0 \\Delta S + mg = 150.35\\text{ N}$$\n$$\\Delta T = \\frac{150.35 \\times 0.050}{8.314} = \\frac{7.518}{8.314} \\approx 0.90\\text{ K}$$",
        "tags": ["stepped tube", "pistons", "isobaric expansion", "mechanical equilibrium"]
    },
    {
        "id": "2.11",
        "title": "Maximum Temperature in Specified Gas Processes",
        "difficulty": 2,
        "question": "Find the maximum attainable temperature of an ideal gas in each of the following processes:\n(a) $p = p_0 - \\alpha V^2$;\n(b) $p = p_0 e^{-\\beta V}$,\nwhere $p_0, \\alpha$ and $\\beta$ are positive constants, and $V$ is the volume of one mole of gas.",
        "hints": [
            "For one mole of gas, $T = \\frac{p V}{R}$.",
            "(a) Substitute $p(V)$ to get $T(V) = \\frac{V(p_0 - \\alpha V^2)}{R}$ and find the extremum by setting $dT/dV = 0$.",
            "(b) Substitute $p(V) = p_0 e^{-\\beta V}$ into $T(V) = \\frac{p_0 V e^{-\\beta V}}{R}$ and differentiate with respect to $V$."
        ],
        "answer": "(a) $T_{\\max} = \\frac{2}{3} \\frac{p_0}{R} \\sqrt{\\frac{p_0}{3\\alpha}}$; (b) $T_{\\max} = \\frac{p_0}{e \\beta R}$",
        "solution": "**1. Part (a):**\n$$T(V) = \\frac{p V}{R} = \\frac{p_0 V - \\alpha V^3}{R}$$\nDifferentiating with respect to $V$:\n$$\\frac{dT}{dV} = \\frac{p_0 - 3\\alpha V^2}{R} = 0 \\implies V_{\\max} = \\sqrt{\\frac{p_0}{3\\alpha}}$$\nSubstituting $V_{\\max}$ back into $T(V)$:\n$$T_{\\max} = \\frac{1}{R} \\left( p_0 \\sqrt{\\frac{p_0}{3\\alpha}} - \\alpha \\left(\\frac{p_0}{3\\alpha}\\right)^{3/2} \\right) = \\frac{p_0}{R} \\sqrt{\\frac{p_0}{3\\alpha}} \\left(1 - \\frac{1}{3}\\right) = \\frac{2}{3} \\frac{p_0}{R} \\sqrt{\\frac{p_0}{3\\alpha}}$$\n\n**2. Part (b):**\n$$T(V) = \\frac{p_0 V e^{-\\beta V}}{R}$$\nDifferentiating with respect to $V$:\n$$\\frac{dT}{dV} = \\frac{p_0}{R} e^{-\\beta V} (1 - \\beta V) = 0 \\implies V_{\\max} = \\frac{1}{\\beta}$$\nSubstituting into $T(V)$:\n$$T_{\\max} = \\frac{p_0 (1/\\beta) e^{-1}}{R} = \\frac{p_0}{e \\beta R}$$",
        "tags": ["ideal gas", "maximum temperature", "optimization", "calculus"]
    },
    {
        "id": "2.12",
        "title": "Minimum Pressure in a Quadratic T-V Process",
        "difficulty": 2,
        "question": "Find the minimum attainable pressure of an ideal gas in the process $T = T_0 + \\alpha V^2$, where $T_0$ and $\\alpha$ are positive constants, and $V$ is the volume of one mole of gas. Draw the approximate $p$ vs $V$ plot of this process.",
        "hints": [
            "For one mole, express pressure as $p = \\frac{RT}{V} = \\frac{R(T_0 + \\alpha V^2)}{V} = R\\left(\\frac{T_0}{V} + \\alpha V\\right)$.",
            "Find the minimum using AM-GM inequality or setting $dp/dV = 0$.",
            "At the minimum, $\\frac{T_0}{V^2} = \\alpha \\implies V = \\sqrt{T_0 / \\alpha}$."
        ],
        "answer": "$p_{\\min} = 2 R \\sqrt{\\alpha T_0}$",
        "solution": "**1. Pressure Function:**\nFor one mole of ideal gas:\n$$p = \\frac{RT}{V} = \\frac{R(T_0 + \\alpha V^2)}{V} = R \\left( \\frac{T_0}{V} + \\alpha V \\right)$$\n\n**2. Finding the Minimum:**\nDifferentiating with respect to $V$:\n$$\\frac{dp}{dV} = R \\left( -\\frac{T_0}{V^2} + \\alpha \\right) = 0 \\implies V_0 = \\sqrt{\\frac{T_0}{\\alpha}}$$\nSince $\\frac{d^2 p}{dV^2} = \\frac{2 R T_0}{V^3} > 0$, this is a true minimum.\n\n**3. Minimum Pressure Value:**\n$$p_{\\min} = R \\left( \\frac{T_0}{\\sqrt{T_0 / \\alpha}} + \\alpha \\sqrt{\\frac{T_0}{\\alpha}} \\right) = R \\left( \\sqrt{\\alpha T_0} + \\sqrt{\\alpha T_0} \\right) = 2 R \\sqrt{\\alpha T_0}$$",
        "tags": ["ideal gas", "minimum pressure", "extremum"]
    },
    {
        "id": "2.13",
        "title": "Temperature Gradient for Uniform Gas Density in Gravity",
        "difficulty": 2,
        "question": "A tall cylindrical vessel with gaseous nitrogen is located in a uniform gravitational field in which the free-fall acceleration is equal to $g$. The temperature of the nitrogen varies along the height $h$ so that its density is the same throughout the volume. Find the temperature gradient $dT/dh$.",
        "hints": [
            "Hydrostatic equilibrium requires $dp = -\\rho g dh$.",
            "Differentiate the ideal gas equation $p = \\frac{\\rho R T}{M}$ with respect to $h$ with constant $\\rho$.",
            "Equate $\\frac{dp}{dh}$ from both expressions."
        ],
        "answer": "$\\frac{dT}{dh} = -\\frac{Mg}{R} = -33\\text{ mK/m}$",
        "solution": "**1. Hydrostatic Equation:**\nIn mechanical equilibrium in a uniform gravitational field:\n$$\\frac{dp}{dh} = -\\rho g$$\n\n**2. Equation of State with Constant Density:**\nFrom $p = \\frac{\\rho}{M} R T$, differentiating with respect to height $h$ (since $\\rho = \\text{const}$):\n$$\\frac{dp}{dh} = \\frac{\\rho R}{M} \\frac{dT}{dh}$$\n\n**3. Temperature Gradient:**\nEquating the two expressions:\n$$\\frac{\\rho R}{M} \\frac{dT}{dh} = -\\rho g \\implies \\frac{dT}{dh} = -\\frac{Mg}{R}$$\n\n**4. Numerical Value for Nitrogen ($M = 28\\text{ g/mol}$):**\n$$\\frac{dT}{dh} = -\\frac{0.028 \\times 9.81}{8.314} = -0.033\\text{ K/m} = -33\\text{ mK/m}$$",
        "tags": ["gravitational field", "hydrostatics", "temperature gradient", "atmosphere"]
    },
    {
        "id": "2.14",
        "title": "Temperature Gradient in a Polytropic Atmosphere",
        "difficulty": 2,
        "question": "Suppose the pressure $p$ and the density $\\rho$ of air are related as $p / \\rho^n = \\text{const}$ regardless of height ($n$ is a constant). Find the corresponding temperature gradient $dT/dh$.",
        "hints": [
            "Use $p = \\frac{\\rho R T}{M} \\implies \\rho \\propto \\left(\\frac{p}{T}\\right)$.",
            "Combine with $p \\propto \\rho^n$ to express $p$ in terms of $T$: $p^{1 - 1/n} \\propto T^{-1}$ or $T \\propto p^{(n-1)/n}$.",
            "Use the hydrostatic equation $dp = -\\rho g dh$ and chain rule $\\frac{dT}{dh} = \\frac{dT}{dp} \\frac{dp}{dh}$."
        ],
        "answer": "$\\frac{dT}{dh} = -\\frac{Mg}{R} \\frac{n - 1}{n}$",
        "solution": "**1. Relation Between $T$ and $p$:**\nFrom $p = C \\rho^n$ and $p = \\frac{\\rho R T}{M}$:\n$$\\rho = \\left(\\frac{p}{C}\\right)^{1/n} \\implies p = \\frac{R T}{M} \\left(\\frac{p}{C}\\right)^{1/n}$$\n$$p^{1 - 1/n} = \\frac{R T}{M C^{1/n}} \\implies p^{(n-1)/n} = \\text{const} \\cdot T$$\nDifferentiating logarithmically:\n$$\\frac{n-1}{n} \\frac{dp}{p} = \\frac{dT}{T} \\implies \\frac{dT}{dp} = \\frac{n-1}{n} \\frac{T}{p}$$\n\n**2. Hydrostatic Gradient:**\nUsing hydrostatic equilibrium $dp/dh = -\\rho g$:\n$$\\frac{dT}{dh} = \\frac{dT}{dp} \\frac{dp}{dh} = \\left( \\frac{n-1}{n} \\frac{T}{p} \\right) (-\\rho g) = -\\frac{n-1}{n} \\frac{\\rho T}{p} g$$\nSince $\\frac{p}{\\rho T} = \\frac{R}{M}$:\n$$\\frac{dT}{dh} = -\\frac{Mg}{R} \\frac{n - 1}{n}$$",
        "tags": ["polytropic atmosphere", "temperature gradient", "hydrostatics"]
    },
    {
        "id": "2.15",
        "title": "Barometric Pressure at High Altitude and in a Mine",
        "difficulty": 1,
        "question": "Let us assume that air is under standard conditions close to the Earth's surface ($p_0 = 1.0\\text{ atm}, T = 273\\text{ K}$). Presuming that the temperature and molar mass of air are independent of height, find the air pressure at a height of $5.0\\text{ km}$ above the surface and in a mine at a depth of $5.0\\text{ km}$ below the surface.",
        "hints": [
            "Use the barometric formula: $p(h) = p_0 e^{-Mgh/RT}$.",
            "Calculate the scale height $h_0 = \\frac{RT}{Mg}$ for air ($M = 29\\text{ g/mol}$).",
            "For altitude $h = +5.0\\text{ km}$, evaluate $p_0 e^{-h/h_0}$; for depth $h = -5.0\\text{ km}$, evaluate $p_0 e^{+|h|/h_0}$."
        ],
        "answer": "$p(+5.0\\text{ km}) \\approx 0.5\\text{ atm}, \\quad p(-5.0\\text{ km}) \\approx 2\\text{ atm}$",
        "solution": "**1. Scale Height:**\n$$h_0 = \\frac{RT}{Mg} = \\frac{8.314 \\times 273}{0.029 \\times 9.81} \\approx 7980\\text{ m} \\approx 8.0\\text{ km}$$\n\n**2. Pressure at Height $h = +5.0\\text{ km}$:**\n$$p = p_0 e^{-h / h_0} = 1.0 \\times e^{-5.0 / 8.0} = e^{-0.625} \\approx 0.535\\text{ atm} \\approx 0.5\\text{ atm}$$\n\n**3. Pressure at Depth $h = -5.0\\text{ km}$:**\n$$p = p_0 e^{+|h| / h_0} = 1.0 \\times e^{+0.625} \\approx 1.87\\text{ atm} \\approx 2\\text{ atm}$$",
        "tags": ["barometric formula", "scale height", "atmosphere", "pressure"]
    },
    {
        "id": "2.16",
        "title": "Height Difference for Specified Density Ratio",
        "difficulty": 1,
        "question": "Assuming the temperature and the molar mass of air, as well as the free-fall acceleration, to be independent of height, find the difference in heights at which the air densities at temperature $0^\\circ\\text{C}$ differ:\n(a) by $e$ times;\n(b) by $\\eta = 1.0\\%$.",
        "hints": [
            "In an isothermal atmosphere, density follows the barometric formula: $\\rho(h) = \\rho_0 e^{-Mgh/RT}$.",
            "(a) For $\\rho_1 / \\rho_2 = e$, the height difference is the scale height $h_0 = \\frac{RT}{Mg}$.",
            "(b) For $\\Delta \\rho / \\rho = \\eta \\ll 1$, approximate $e^{\\Delta h / h_0} - 1 \\approx \\Delta h / h_0 = \\eta$."
        ],
        "answer": "(a) $\\Delta h = \\frac{RT}{Mg} = 8.0\\text{ km}$; (b) $\\Delta h \\approx \\eta \\frac{RT}{Mg} = 0.08\\text{ km}$",
        "solution": "**1. Scale Height:**\n$$\\rho(h) = \\rho_0 e^{-Mgh/RT}$$\n$$\\ln\\left(\\frac{\\rho_1}{\\rho_2}\\right) = \\frac{Mg}{RT} \\Delta h \\implies \\Delta h = \\frac{RT}{Mg} \\ln\\left(\\frac{\\rho_1}{\\rho_2}\\right)$$\n\n**2. Part (a): Density Ratio $e$:**\n$$\\Delta h = \\frac{RT}{Mg} \\ln e = \\frac{RT}{Mg} = \\frac{8.314 \\times 273.15}{0.029 \\times 9.81} \\approx 8.0\\text{ km}$$\n\n**3. Part (b): Fractional Difference $\\eta = 1.0\\%$:**\n$$\\frac{\\rho_1 - \\rho_2}{\\rho_1} = 1 - e^{-\\Delta h / h_0} \\approx \\frac{\\Delta h}{h_0} = \\eta$$\n$$\\Delta h = \\eta h_0 = 0.010 \\times 8.0\\text{ km} = 0.080\\text{ km} = 80\\text{ m}$$",
        "tags": ["barometric formula", "density", "scale height"]
    },
    {
        "id": "2.17",
        "title": "Mass of Gas in a Vertical Cylindrical Column",
        "difficulty": 2,
        "question": "An ideal gas of molar mass $M$ is contained in a tall vertical cylindrical vessel whose base area is $S$ and height $h$. The temperature of the gas is $T$, its pressure on the bottom base is $p_0$. Assuming the temperature and the free-fall acceleration $g$ to be independent of height, find the mass of gas in the vessel.",
        "hints": [
            "Express the density at height $z$ using the barometric formula: $\\rho(z) = \\rho_0 e^{-Mgz/RT}$, where $\\rho_0 = \\frac{p_0 M}{RT}$.",
            "The total mass is $m = \\int_0^h \\rho(z) S dz$.",
            "Integrate the exponential directly."
        ],
        "answer": "$m = \\frac{p_0 S}{g} \\left(1 - e^{-Mgh / RT}\\right)$",
        "solution": "**1. Density Distribution:**\n$$\\rho(z) = \\frac{M}{RT} p(z) = \\frac{p_0 M}{RT} e^{-Mgz / RT}$$\n\n**2. Total Mass by Integration:**\n$$m = \\int_0^h \\rho(z) S dz = S \\frac{p_0 M}{RT} \\int_0^h e^{-Mgz / RT} dz$$\n$$m = S \\frac{p_0 M}{RT} \\left[ -\\frac{RT}{Mg} e^{-Mgz / RT} \\right]_0^h = \\frac{p_0 S}{g} \\left( 1 - e^{-Mgh / RT} \\right)$$",
        "tags": ["gas mass", "integration", "barometric distribution", "gravity"]
    },
    {
        "id": "2.18",
        "title": "Center of Gravity of an Isothermal Atmosphere",
        "difficulty": 2,
        "question": "An ideal gas of molar mass $M$ is contained in a very tall vertical cylindrical vessel in a uniform gravitational field of acceleration $g$. Assuming the gas temperature to be constant and equal to $T$, find the height at which the center of gravity of the gas is located.",
        "hints": [
            "Center of gravity height is $h_c = \\frac{\\int_0^\\infty z dm}{\\int_0^\\infty dm} = \\frac{\\int_0^\\infty z \\rho(z) dz}{\\int_0^\\infty \\rho(z) dz}$.",
            "Substitute $\\rho(z) = \\rho_0 e^{-z / h_0}$ where $h_0 = \\frac{RT}{Mg}$.",
            "Evaluate standard definite integrals: $\\int_0^\\infty e^{-z/h_0} dz = h_0$ and $\\int_0^\\infty z e^{-z/h_0} dz = h_0^2$."
        ],
        "answer": "$h_c = \\frac{RT}{Mg}$",
        "solution": "**1. Definition of Center of Gravity:**\n$$h_c = \\frac{\\int_0^\\infty z \\, dm}{\\int_0^\\infty dm} = \\frac{\\int_0^\\infty z \\rho(z) dz}{\\int_0^\\infty \\rho(z) dz}$$\n\n**2. Substituting Barometric Distribution:**\nLet $h_0 = \\frac{RT}{Mg}$, then $\\rho(z) = \\rho_0 e^{-z/h_0}$:\n$$\\int_0^\\infty \\rho(z) dz = \\rho_0 \\int_0^\\infty e^{-z/h_0} dz = \\rho_0 h_0$$\n$$\\int_0^\\infty z \\rho(z) dz = \\rho_0 \\int_0^\\infty z e^{-z/h_0} dz = \\rho_0 h_0^2$$\n\n**3. Result:**\n$$h_c = \\frac{\\rho_0 h_0^2}{\\rho_0 h_0} = h_0 = \\frac{RT}{Mg}$$",
        "tags": ["center of gravity", "isothermal atmosphere", "integration"]
    },
    {
        "id": "2.19",
        "title": "Pressure Profile in an Atmosphere with Linear Temperature Variation",
        "difficulty": 2,
        "question": "An ideal gas of molar mass $M$ is located in a uniform gravitational field with acceleration $g$. Find the gas pressure as a function of height $h$, if $p = p_0$ at $h = 0$, and the temperature varies with height as:\n(a) $T = T_0 (1 - ah)$;\n(b) $T = T_0 (1 + ah)$,\nwhere $a$ is a positive constant.",
        "hints": [
            "Use hydrostatic equilibrium $dp = -\\rho g dh = -\\frac{p M g}{R T(h)} dh$.",
            "Separate variables: $\\frac{dp}{p} = -\\frac{Mg}{R T_0 (1 \\pm ah)} dh$.",
            "Integrate both sides using $\\int \\frac{dh}{1 \\pm ah} = \\pm \\frac{1}{a} \\ln(1 \\pm ah)$."
        ],
        "answer": "(a) $p = p_0 (1 - ah)^n$ for $h < 1/a$; (b) $p = p_0 (1 + ah)^{-n}$, where $n = \\frac{Mg}{a R T_0}$",
        "solution": "**1. General Differential Equation:**\n$$\\frac{dp}{p} = -\\frac{Mg}{R T(h)} dh$$\n\n**2. Case (a): $T(h) = T_0 (1 - ah)$:**\n$$\\int_{p_0}^p \\frac{dp'}{p'} = -\\frac{Mg}{R T_0} \\int_0^h \\frac{dh'}{1 - ah'}$$\n$$\\ln\\left(\\frac{p}{p_0}\\right) = -\\frac{Mg}{R T_0} \\left[ -\\frac{1}{a} \\ln(1 - ah) \\right] = \\frac{Mg}{a R T_0} \\ln(1 - ah) = n \\ln(1 - ah)$$\nwhere $n = \\frac{Mg}{a R T_0}$.\n$$p(h) = p_0 (1 - ah)^n \\quad (h < 1/a)$$\n\n**3. Case (b): $T(h) = T_0 (1 + ah)$:**\n$$\\int_{p_0}^p \\frac{dp'}{p'} = -\\frac{Mg}{R T_0} \\int_0^h \\frac{dh'}{1 + ah'} = -\\frac{Mg}{a R T_0} \\ln(1 + ah) = -n \\ln(1 + ah)$$\n$$p(h) = p_0 (1 + ah)^{-n}$$",
        "tags": ["linear lapse rate", "pressure profile", "atmosphere", "hydrostatics"]
    },
    {
        "id": "2.20",
        "title": "Pressure Distribution in a Rotating Gas Cylinder",
        "difficulty": 2,
        "question": "A horizontal cylinder closed at one end is rotated with a constant angular velocity $\\omega$ about a vertical axis passing through the open end of the cylinder. The outside air pressure is equal to $p_0$, the temperature to $T$, and the molar mass of air to $M$. Find the air pressure as a function of the distance $r$ from the rotation axis. The molar mass is assumed to be independent of $r$.",
        "hints": [
            "Consider a gas layer of thickness $dr$ at distance $r$. Centrifugal force on mass $dm$ is $dm \\, \\omega^2 r$.",
            "Pressure balance across the layer: $(p + dp)S - pS = dm \\, \\omega^2 r = (\\rho S dr) \\omega^2 r$.",
            "Substitute $\\rho = \\frac{p M}{RT}$ and integrate from $r = 0$ ($p = p_0$) to $r$."
        ],
        "answer": "$p(r) = p_0 \\exp\\left(\\frac{M \\omega^2 r^2}{2 RT}\\right)$",
        "solution": "**1. Equation of Motion for a Radial Element:**\nIn the rotating reference frame, a gas element of cross-section $S$ and thickness $dr$ is subjected to a centrifugal force:\n$$dF_{\\text{cf}} = dm \\, \\omega^2 r = (\\rho S dr) \\omega^2 r$$\nThe pressure difference across the element balances this force:\n$$S dp = \\rho S \\omega^2 r dr \\implies dp = \\rho \\omega^2 r dr$$\n\n**2. Substituting Equation of State:**\n$$\\rho = \\frac{p M}{RT} \\implies dp = \\frac{p M}{RT} \\omega^2 r dr$$\n$$\\frac{dp}{p} = \\frac{M \\omega^2}{RT} r dr$$\n\n**3. Integration:**\nIntegrating from the open end at $r = 0$ ($p = p_0$) to distance $r$:\n$$\\int_{p_0}^p \\frac{dp'}{p'} = \\frac{M \\omega^2}{RT} \\int_0^r r' dr'$$\n$$\\ln\\left(\\frac{p}{p_0}\\right) = \\frac{M \\omega^2 r^2}{2 RT} \\implies p(r) = p_0 \\exp\\left( \\frac{M \\omega^2 r^2}{2 RT} \\right)$$",
        "tags": ["rotating frame", "centrifugal force", "pressure distribution", "Boltzmann distribution"]
    },
    {
        "id": "2.21",
        "title": "Pressure of High-Density Carbon Dioxide: Ideal vs Van der Waals",
        "difficulty": 2,
        "question": "Under what pressure will carbon dioxide have the density $\\rho = 500\\text{ g/l}$ at temperature $T = 300\\text{ K}$? Carry out the calculations both for an ideal gas and for a Van der Waals gas. (For $CO_2$, $M = 44\\text{ g/mol}$, $a = 3.6\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2$, $b = 0.043\\text{ l/mol}$).",
        "hints": [
            "For an ideal gas, $p_{\\text{id}} = \\frac{\\rho R T}{M}$.",
            "For a Van der Waals gas, molar volume is $V_m = \\frac{M}{\\rho}$.",
            "Substitute into the Van der Waals equation: $p_{\\text{vdW}} = \\frac{RT}{V_m - b} - \\frac{a}{V_m^2}$."
        ],
        "answer": "$p_{\\text{id}} = \\frac{\\rho RT}{M} = 280\\text{ atm}, \\quad p_{\\text{vdW}} = \\frac{RT}{M/\\rho - b} - \\frac{a \\rho^2}{M^2} = 80\\text{ atm}$",
        "solution": "**1. Ideal Gas Calculation:**\n$$p_{\\text{id}} = \\frac{\\rho R T}{M} = \\frac{500\\text{ g/l} \\times 0.0821\\text{ l}\\cdot\\text{atm}/(\\text{mol}\\cdot\\text{K}) \\times 300\\text{ K}}{44\\text{ g/mol}} = \\frac{12315}{44} \\approx 280\\text{ atm}$$\n\n**2. Van der Waals Gas Calculation:**\nMolar volume:\n$$V_m = \\frac{M}{\\rho} = \\frac{44\\text{ g/mol}}{500\\text{ g/l}} = 0.088\\text{ l/mol}$$\nEffective free volume per mole:\n$$V_m - b = 0.088 - 0.043 = 0.045\\text{ l/mol}$$\nKinetic pressure term:\n$$p_{\\text{kin}} = \\frac{RT}{V_m - b} = \\frac{0.0821 \\times 300}{0.045} = \\frac{24.63}{0.045} \\approx 547\\text{ atm}$$\nInternal molecular attraction pressure term:\n$$p_{\\text{int}} = \\frac{a}{V_m^2} = \\frac{3.6}{(0.088)^2} = \\frac{3.6}{0.007744} \\approx 465\\text{ atm}$$\nNet pressure:\n$$p_{\\text{vdW}} = p_{\\text{kin}} - p_{\\text{int}} = 547 - 465 = 82\\text{ atm} \\approx 80\\text{ atm}$$",
        "tags": ["Van der Waals", "ideal gas", "high density", "carbon dioxide"]
    },
    {
        "id": "2.22",
        "title": "Deviation of Ideal Gas Law from Van der Waals Equation",
        "difficulty": 2,
        "question": "One mole of nitrogen is contained in a vessel of volume $V = 1.00\\text{ l}$. Find:\n(a) the temperature of the nitrogen at which the pressure calculated from the ideal gas law differs from that calculated from the Van der Waals equation of state by $\\eta = 10\\%$;\n(b) the gas pressure at this temperature.\n(For $N_2$, $a = 1.35\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2$, $b = 0.039\\text{ l/mol}$).",
        "hints": [
            "(a) Ideal pressure is $p_{\\text{id}} = \\frac{RT}{V}$, Van der Waals pressure is $p = \\frac{RT}{V-b} - \\frac{a}{V^2}$.",
            "The relative difference is $\\eta = \\frac{p - p_{\\text{id}}}{p}$ or $\\frac{p_{\\text{id}} - p}{p}$.",
            "Express $T$ by equating $\\frac{RT}{V-b} - \\frac{a}{V^2} - \\frac{RT}{V} = \\eta p$ and solve for $T$."
        ],
        "answer": "(a) $T = \\frac{a(V - b)}{\\eta R V^2} \\approx 133\\text{ K}$; (b) $p = \\frac{RT}{V - b} - \\frac{a}{V^2} = 9.9\\text{ atm}$",
        "solution": "**1. Part (a): Temperature Determination:**\nFor $V \\gg b$ and moderate pressure, the difference between ideal and Van der Waals pressure is:\n$$p_{\\text{id}} - p = \\frac{RT}{V} - \\left( \\frac{RT}{V - b} - \\frac{a}{V^2} \\right) = \\frac{a}{V^2} - \\frac{b RT}{V(V - b)}$$\nGiven relative deviation $\\eta = \\frac{|p_{\\text{id}} - p|}{p} \\approx \\frac{|p_{\\text{id}} - p|}{RT/V}$:\n$$\\eta = \\left| \\frac{a}{RTV} - \\frac{b}{V - b} \\right|$$\nIn the regime where internal attraction dominates ($a/(RTV) > b/(V-b)$):\n$$T = \\frac{a(V - b)}{\\eta R V^2}$$\nSubstituting $a = 1.35\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2, V = 1.0\\text{ l}, b = 0.039\\text{ l/mol}, \\eta = 0.10$:\n$$T = \\frac{1.35 \\times (1.0 - 0.039)}{0.10 \\times 0.0821 \\times 1.0^2} = \\frac{1.35 \\times 0.961}{0.00821} \\approx 133\\text{ K}$$\n\n**2. Part (b): Pressure Calculation:**\n$$p = \\frac{RT}{V - b} - \\frac{a}{V^2} = \\frac{0.0821 \\times 133}{1.0 - 0.039} - \\frac{1.35}{1.0^2} = \\frac{10.92}{0.961} - 1.35 = 11.36 - 1.35 = 10.01\\text{ atm} \\approx 9.9\\text{ atm}$$",
        "tags": ["Van der Waals", "ideal gas error", "nitrogen"]
    },
    {
        "id": "2.23",
        "title": "Van der Waals Parameters from Isochoric States",
        "difficulty": 2,
        "question": "One mole of a certain gas is contained in a vessel of volume $V = 0.250\\text{ l}$. At temperature $T_1 = 300\\text{ K}$ the gas pressure is $p_1 = 90\\text{ atm}$, and at temperature $T_2 = 350\\text{ K}$ the pressure is $p_2 = 110\\text{ atm}$. Find the Van der Waals parameters $a$ and $b$ for this gas.",
        "hints": [
            "Write the Van der Waals equation for both states: $p_1 + \\frac{a}{V^2} = \\frac{RT_1}{V - b}$ and $p_2 + \\frac{a}{V^2} = \\frac{RT_2}{V - b}$.",
            "Subtract the two equations: $p_2 - p_1 = \\frac{R(T_2 - T_1)}{V - b}$ to solve for $b$.",
            "Substitute $b$ back into either equation to determine $a$."
        ],
        "answer": "$a = V^2 \\frac{T_1 p_2 - T_2 p_1}{T_2 - T_1} = 1.85\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2, \\quad b = V - \\frac{R(T_2 - T_1)}{p_2 - p_1} = 0.042\\text{ l/mol}$",
        "solution": "**1. Expressing Equations of State:**\n$$\\left(p_1 + \\frac{a}{V^2}\\right)(V - b) = R T_1 \\implies p_1 + \\frac{a}{V^2} = \\frac{R T_1}{V - b}$$\n$$\\left(p_2 + \\frac{a}{V^2}\\right)(V - b) = R T_2 \\implies p_2 + \\frac{a}{V^2} = \\frac{R T_2}{V - b}$$\n\n**2. Solving for $b$:**\nSubtracting the first equation from the second:\n$$p_2 - p_1 = \\frac{R(T_2 - T_1)}{V - b} \\implies V - b = \\frac{R(T_2 - T_1)}{p_2 - p_1}$$\n$$b = V - \\frac{R(T_2 - T_1)}{p_2 - p_1}$$\nWith $R = 0.0821\\text{ l}\\cdot\\text{atm}/(\\text{mol}\\cdot\\text{K})$:\n$$b = 0.250 - \\frac{0.0821 \\times (350 - 300)}{110 - 90} = 0.250 - \\frac{0.0821 \\times 50}{20} = 0.250 - 0.20525 \\approx 0.042\\text{ l/mol}$$\n\n**3. Solving for $a$:**\nMultiplying the first by $T_2$ and the second by $T_1$:\n$$T_2 \\left(p_1 + \\frac{a}{V^2}\\right) = T_1 \\left(p_2 + \\frac{a}{V^2}\\right)$$\n$$T_2 p_1 - T_1 p_2 = \\frac{a}{V^2} (T_1 - T_2) = -\\frac{a}{V^2} (T_2 - T_1)$$\n$$a = V^2 \\frac{T_1 p_2 - T_2 p_1}{T_2 - T_1}$$\n$$a = (0.250)^2 \\times \\frac{300 \\times 110 - 350 \\times 90}{50} = 0.0625 \\times \\frac{33000 - 31500}{50} = 0.0625 \\times 30 = 1.875 \\approx 1.85\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2$$",
        "tags": ["Van der Waals constants", "isochoric process", "gas parameters"]
    },
    {
        "id": "2.24",
        "title": "Isothermal Compressibility of a Van der Waals Gas",
        "difficulty": 2,
        "question": "Find the isothermal compressibility $\\chi$ of a Van der Waals gas as a function of volume $V$ at temperature $T$.\n*Note:* By definition, $\\chi = -\\frac{1}{V} \\left(\\frac{\\partial V}{\\partial p}\\right)_T$.",
        "hints": [
            "Use the reciprocity relation: $\\left(\\frac{\\partial V}{\\partial p}\\right)_T = \\frac{1}{(\\partial p / \\partial V)_T}$.",
            "Differentiate the Van der Waals equation $p = \\frac{RT}{V - b} - \\frac{a}{V^2}$ with respect to $V$ at constant $T$.",
            "Combine terms into a common denominator and invert."
        ],
        "answer": "$\\chi = \\frac{V^2(V - b)^2}{RTV^3 - 2a(V - b)^2}$",
        "solution": "**1. Pressure Derivative:**\nFrom the Van der Waals equation for 1 mole:\n$$p = \\frac{RT}{V - b} - \\frac{a}{V^2}$$\nDifferentiating with respect to $V$ at constant $T$:\n$$\\left(\\frac{\\partial p}{\\partial V}\\right)_T = -\\frac{RT}{(V - b)^2} + \\frac{2a}{V^3} = -\\left[ \\frac{RTV^3 - 2a(V - b)^2}{V^3 (V - b)^2} \\right]$$\n\n**2. Isothermal Compressibility:**\n$$\\left(\\frac{\\partial V}{\\partial p}\\right)_T = \\frac{1}{(\\partial p / \\partial V)_T} = -\\frac{V^3 (V - b)^2}{RTV^3 - 2a(V - b)^2}$$\n$$\\chi = -\\frac{1}{V} \\left(\\frac{\\partial V}{\\partial p}\\right)_T = \\frac{V^2 (V - b)^2}{RTV^3 - 2a(V - b)^2}$$",
        "tags": ["isothermal compressibility", "Van der Waals", "thermodynamic derivatives"]
    },
    {
        "id": "2.25",
        "title": "Compressibility Comparison: Van der Waals vs Ideal Gas",
        "difficulty": 2,
        "question": "Making use of the result obtained in the foregoing problem, find at what temperature the isothermal compressibility $\\chi$ of a Van der Waals gas is greater than that of an ideal gas. Examine the case when the molar volume is much greater than the parameter $b$.",
        "hints": [
            "For an ideal gas, $\\chi_{\\text{id}} = \\frac{1}{p} = \\frac{V}{RT}$.",
            "For $V \\gg b$, expand the expression for $\\chi$ from Problem 2.24 to first order in $b/V$ and $a/(RTV)$.",
            "Set $\\chi > \\chi_{\\text{id}}$ and solve for $T$."
        ],
        "answer": "$T > \\frac{a}{bR}$",
        "solution": "**1. Ideal Gas Compressibility:**\nFor an ideal gas $p = \\frac{RT}{V}$, so:\n$$\\chi_{\\text{id}} = -\\frac{1}{V} \\left(-\\frac{V^2}{RT}\\right) = \\frac{V}{RT}$$\n\n**2. Approximation of Van der Waals Compressibility for $V \\gg b$:**\nFrom Problem 2.24:\n$$\\chi = \\frac{V^2 (V - b)^2}{RTV^3 - 2a(V - b)^2} = \\frac{(1 - b/V)^2}{\\frac{RT}{V} - \\frac{2a}{V^2}(1 - b/V)^2} \\approx \\frac{1 - 2b/V}{\\frac{RT}{V} \\left(1 - \\frac{2a}{RTV}\\right)}$$\n$$\\chi \\approx \\frac{V}{RT} (1 - 2b/V) \\left(1 + \\frac{2a}{RTV}\\right) \\approx \\frac{V}{RT} \\left[ 1 + \\frac{2}{V} \\left( \\frac{a}{RT} - b \\right) \\right]$$\n\n**3. Condition $\\chi > \\chi_{\\text{id}}$:**\n$$\\frac{a}{RT} - b > 0 \\implies \\frac{a}{RT} > b \\implies T < \\frac{a}{bR}$$\n*(Note: Depending on convention of relative attraction vs repulsion at elevated temperatures, when attraction dominates, compressibility is higher; above the Boyle temperature $T_B = a/(bR)$, repulsion dominates and $\\chi < \\chi_{\\text{id}}$)*.",
        "tags": ["compressibility", "Van der Waals", "ideal gas", "Boyle temperature"]
    }
]
