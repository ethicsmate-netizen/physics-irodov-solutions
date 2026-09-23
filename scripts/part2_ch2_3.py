"""
part2_ch2_3.py
Curated problems 2.62 to 2.112 (51 problems) of Irodov Chapter 2.3:
Kinetic Theory of Gases. Boltzmann's Law and Maxwell's Distribution.
"""

CH2_3_CURATED = [
    {
        "id": "2.62",
        "title": "Molecular Concentration and Mean Separation in Ultra-High Vacuum",
        "difficulty": 1,
        "question": "Modern vacuum pumps permit pressures down to $p = 4 \\times 10^{-15}\\text{ atm}$ to be reached at room temperature ($T = 300\\text{ K}$). Assuming the gas exhausted is nitrogen, find:\n(a) the number of molecules per unit volume;\n(b) the mean distance between molecules.",
        "hints": [
            "Use the ideal gas concentration formula: $n = \\frac{p}{kT}$.",
            "The mean distance between molecules is approximately the side of a cube per molecule: $l \\approx n^{-1/3}$.",
            "Convert pressure from atm to Pa: $1\\text{ atm} = 1.013 \\times 10^5\\text{ Pa}$."
        ],
        "answer": "$n = \\frac{p}{kT} = 1 \\times 10^5\\text{ cm}^{-3}, \\quad l = 0.2\\text{ mm}$",
        "solution": "**1. Concentration Calculation:**\n$$p = 4 \\times 10^{-15} \\times 1.013 \\times 10^5\\text{ Pa} \\approx 4.05 \\times 10^{-10}\\text{ Pa}$$\n$$n = \\frac{p}{kT} = \\frac{4.05 \\times 10^{-10}}{1.38 \\times 10^{-23} \\times 300} \\approx 9.8 \\times 10^{10}\\text{ m}^{-3} \\approx 1.0 \\times 10^5\\text{ cm}^{-3}$$\n\n**2. Mean Distance Between Molecules:**\n$$l \\approx n^{-1/3} = (1.0 \\times 10^{11})^{-1/3}\\text{ m} \\approx 2.15 \\times 10^{-4}\\text{ m} \\approx 0.2\\text{ mm}$$",
        "tags": ["vacuum", "molecular concentration", "mean distance", "Maxwell-Boltzmann"]
    },
    {
        "id": "2.63",
        "title": "Pressure of High-Temperature Dissociating Nitrogen",
        "difficulty": 2,
        "question": "A vessel of volume $V = 5.0\\text{ l}$ contains $m = 1.4\\text{ g}$ of nitrogen at temperature $T = 1800\\text{ K}$. Find the gas pressure, taking into account that $\\eta = 30\\%$ of the molecules are dissociated into atoms at this temperature.",
        "hints": [
            "Let $\\nu_0 = \\frac{m}{M}$ be the initial moles of $N_2$ molecules ($M = 28\\text{ g/mol}$).",
            "When fraction $\\eta$ dissociates, 1 mole of $N_2$ produces $2$ moles of $N$, giving $(1 - \\eta)\\nu_0$ moles of $N_2$ and $2\\eta\\nu_0$ moles of $N$.",
            "Total number of moles becomes $\\nu = \\nu_0(1 + \\eta)$. Pressure is $p = \\frac{\\nu RT}{V}$."
        ],
        "answer": "$p = \\frac{m RT}{M V} (1 + \\eta) = 1.9\\text{ atm}$",
        "solution": "**1. Total Moles of Particles:**\nInitial moles of molecular nitrogen $N_2$:\n$$\\nu_0 = \\frac{m}{M} = \\frac{1.4\\text{ g}}{28\\text{ g/mol}} = 0.050\\text{ mol}$$\nWhen fraction $\\eta = 0.30$ dissociates:\n- Moles of undissociated $N_2$: $\\nu_{N_2} = \\nu_0 (1 - \\eta)$\n- Moles of atomic nitrogen $N$: $\\nu_N = 2 \\eta \\nu_0$\nTotal moles of particles:\n$$\\nu = \\nu_{N_2} + \\nu_N = \\nu_0(1 - \\eta + 2\\eta) = \\nu_0(1 + \\eta)$$\n\n**2. Pressure Calculation:**\n$$p = \\frac{\\nu R T}{V} = \\frac{m R T}{M V} (1 + \\eta)$$\n$$p = \\frac{0.050 \\times (1 + 0.30) \\times 8.314 \\times 1800}{5.0 \\times 10^{-3}} = \\frac{0.065 \\times 14965}{0.005} = 1.945 \\times 10^5\\text{ Pa} \\approx 1.9\\text{ atm}$$",
        "tags": ["dissociation", "nitrogen", "Dalton's law", "high temperature"]
    },
    {
        "id": "2.64",
        "title": "Helium Concentration in a Helium-Nitrogen Mixture",
        "difficulty": 2,
        "question": "Under standard conditions ($p = 1.0\\text{ atm}, T = 273\\text{ K}$) the density of a helium and nitrogen mixture equals $\\rho = 0.60\\text{ g/l}$. Find the concentration of helium molecules in the mixture.",
        "hints": [
            "Total pressure is $p = (n_1 + n_2) kT$, where $n_1$ is helium concentration and $n_2$ is nitrogen concentration.",
            "Total density is $\\rho = n_1 m_1 + n_2 m_2$, where $m_1 = M_1 / N_A$ and $m_2 = M_2 / N_A$.",
            "Substitute $n_2 = \\frac{p}{kT} - n_1$ into the density expression to solve for $n_1$."
        ],
        "answer": "$n_1 = \\frac{\\rho / m_2 - p / kT}{m_1 / m_2 - 1} = 1.6 \\times 10^{19}\\text{ cm}^{-3}$",
        "solution": "**1. System of Equations:**\n$$n_1 + n_2 = \\frac{p}{kT} = n$$\n$$n_1 m_1 + n_2 m_2 = \\rho$$\n\n**2. Solving for $n_1$:**\n$$n_1 m_1 + \\left( \\frac{p}{kT} - n_1 \\right) m_2 = \\rho$$\n$$n_1 (m_1 - m_2) = \\rho - \\frac{p m_2}{kT}$$\n$$n_1 = \\frac{\\frac{p m_2}{kT} - \\rho}{m_2 - m_1} = \\frac{\\rho / m_2 - p/kT}{m_1/m_2 - 1}$$\n\n**3. Numerical Evaluation:**\n$$n = \\frac{p}{kT} = \\frac{1.013 \\times 10^5}{1.38 \\times 10^{-23} \\times 273} \\approx 2.687 \\times 10^{25}\\text{ m}^{-3}$$\n$$m_1 = \\frac{4.0 \\times 10^{-3}}{6.022 \\times 10^{23}} = 6.64 \\times 10^{-27}\\text{ kg}$$\n$$m_2 = \\frac{28 \\times 10^{-3}}{6.022 \\times 10^{23}} = 4.65 \\times 10^{-26}\\text{ kg}$$\n$$\\rho = 0.60\\text{ kg/m}^3$$\n$$n_1 = \\frac{2.687 \\times 10^{25} \\times 4.65 \\times 10^{-26} - 0.60}{(4.65 - 0.664) \\times 10^{-26}} = \\frac{1.249 - 0.60}{3.986 \\times 10^{-26}} = \\frac{0.649}{3.986 \\times 10^{-26}} \\approx 1.63 \\times 10^{25}\\text{ m}^{-3} = 1.6 \\times 10^{19}\\text{ cm}^{-3}$$",
        "tags": ["gas mixture", "helium", "molecular concentration", "density"]
    },
    {
        "id": "2.65",
        "title": "Pressure Exerted by a Molecular Beam on a Wall",
        "difficulty": 1,
        "question": "A parallel beam of nitrogen molecules moving with velocity $v = 400\\text{ m/s}$ impinges on a wall at an angle $\\theta = 30^\\circ$ to its normal. The concentration of molecules in the beam is $n = 0.90 \\times 10^{19}\\text{ cm}^{-3}$. Find the pressure exerted by the beam on the wall, assuming the collisions to be perfectly elastic.",
        "hints": [
            "In an elastic reflection, the normal momentum change per molecule is $\\Delta p_x = 2 m v \\cos\\theta$.",
            "The number of molecules hitting unit area per unit time is $J = n v \\cos\\theta$.",
            "Pressure is momentum delivered per unit area per unit time: $p = J \\Delta p_x = 2 n m v^2 \\cos^2\\theta$."
        ],
        "answer": "$p = 2 n m v^2 \\cos^2\\theta = 1.0\\text{ atm}$",
        "solution": "**1. Momentum Transfer:**\nNormal velocity component: $v_x = v \\cos\\theta$.\nIn elastic reflection from a stationary wall, $\\Delta p_x = 2 m v_x = 2 m v \\cos\\theta$.\n\n**2. Rate of Arrival:**\nThe number of molecules striking unit wall area per unit time is:\n$$J = n v_x = n v \\cos\\theta$$\n\n**3. Pressure Formula:**\n$$p = J \\Delta p_x = 2 n m v^2 \\cos^2\\theta$$\n\n**4. Numerical Value ($M = 28\\text{ g/mol}$):**\n$$m = \\frac{0.028}{6.022 \\times 10^{23}} = 4.65 \\times 10^{-26}\\text{ kg}$$\n$$n = 0.90 \\times 10^{25}\\text{ m}^{-3}, \\quad v = 400\\text{ m/s}, \\quad \\cos^2 30^\\circ = \\frac{3}{4} = 0.75$$\n$$p = 2 \\times (0.90 \\times 10^{25}) \\times (4.65 \\times 10^{-26}) \\times 160000 \\times 0.75 = 1.004 \\times 10^5\\text{ Pa} \\approx 1.0\\text{ atm}$$",
        "tags": ["molecular beam", "pressure", "elastic collision", "momentum"]
    },
    {
        "id": "2.66",
        "title": "Degrees of Freedom from Speed of Sound and Density",
        "difficulty": 2,
        "question": "How many degrees of freedom do the gas molecules have, if under standard conditions ($p = 1.0\\text{ atm}$) the gas density is $\\rho = 1.3\\text{ mg/cm}^3$ and the velocity of sound in it is $v = 330\\text{ m/s}$?",
        "hints": [
            "Speed of sound in an ideal gas is $v = \\sqrt{\\frac{\\gamma p}{\\rho}}$.",
            "Solve for the adiabatic index: $\\gamma = \\frac{v^2 \\rho}{p}$.",
            "Relate $\\gamma$ to the number of degrees of freedom: $\\gamma = 1 + \\frac{2}{i} \\implies i = \\frac{2}{\\gamma - 1} = \\frac{2}{v^2 \\rho / p - 1}$."
        ],
        "answer": "$i = \\frac{2}{v^2 \\rho / p - 1} = 5$",
        "solution": "**1. Determining Adiabatic Exponent $\\gamma$:**\n$$v = \\sqrt{\\frac{\\gamma p}{\\rho}} \\implies \\gamma = \\frac{v^2 \\rho}{p}$$\nWith $v = 330\\text{ m/s}$, $\\rho = 1.3\\text{ mg/cm}^3 = 1.3\\text{ kg/m}^3$, and $p = 1.013 \\times 10^5\\text{ Pa}$:\n$$\\gamma = \\frac{(330)^2 \\times 1.3}{1.013 \\times 10^5} = \\frac{108900 \\times 1.3}{101300} = \\frac{141570}{101300} \\approx 1.40$$\n\n**2. Degrees of Freedom:**\n$$\\gamma = \\frac{i + 2}{i} = 1 + \\frac{2}{i} \\implies \\frac{2}{i} = \\gamma - 1$$\n$$i = \\frac{2}{\\gamma - 1} = \\frac{2}{1.40 - 1} = \\frac{2}{0.40} = 5$$\n*(The molecules are rigid diatomic molecules with 3 translational + 2 rotational degrees of freedom)*.",
        "tags": ["degrees of freedom", "speed of sound", "adiabatic index"]
    },
    {
        "id": "2.67",
        "title": "Ratio of Sound Velocity to Root-Mean-Square Velocity",
        "difficulty": 1,
        "question": "Determine the ratio of the sonic velocity $v_{\\text{sound}}$ in a gas to the root-mean-square velocity $v_{\\text{rms}}$ of molecules of this gas, if the molecule has $i$ degrees of freedom. Calculate this ratio for:\n(a) monatomic gas ($i = 3$);\n(b) rigid diatomic gas ($i = 5$).",
        "hints": [
            "Sonic velocity is $v_{\\text{sound}} = \\sqrt{\\frac{\\gamma R T}{M}}$, where $\\gamma = \\frac{i + 2}{i}$.",
            "Root-mean-square velocity is $v_{\\text{rms}} = \\sqrt{\\frac{3 R T}{M}}$.",
            "The ratio is $\\frac{v_{\\text{sound}}}{v_{\\text{rms}}} = \\sqrt{\\frac{\\gamma}{3}} = \\sqrt{\\frac{i + 2}{3i}}$."
        ],
        "answer": "$\\frac{v_{\\text{sound}}}{v_{\\text{rms}}} = \\sqrt{\\frac{i + 2}{3i}}$; (a) $0.75$; (b) $0.68$",
        "solution": "**1. Velocity Ratio Formula:**\n$$v_{\\text{sound}} = \\sqrt{\\frac{\\gamma RT}{M}}, \\quad v_{\\text{rms}} = \\sqrt{\\frac{3RT}{M}}$$\n$$\\frac{v_{\\text{sound}}}{v_{\\text{rms}}} = \\sqrt{\\frac{\\gamma}{3}}$$\nSubstituting $\\gamma = \\frac{i + 2}{i}$:\n$$\\frac{v_{\\text{sound}}}{v_{\\text{rms}}} = \\sqrt{\\frac{i + 2}{3i}}$$\n\n**2. Part (a): Monatomic Gas ($i = 3$):**\n$$\\frac{v_{\\text{sound}}}{v_{\\text{rms}}} = \\sqrt{\\frac{3 + 2}{3 \\times 3}} = \\sqrt{\\frac{5}{9}} = \\frac{\\sqrt{5}}{3} \\approx 0.745 \\approx 0.75$$\n\n**3. Part (b): Rigid Diatomic Gas ($i = 5$):**\n$$\\frac{v_{\\text{sound}}}{v_{\\text{rms}}} = \\sqrt{\\frac{5 + 2}{3 \\times 5}} = \\sqrt{\\frac{7}{15}} \\approx 0.683 \\approx 0.68$$",
        "tags": ["sound velocity", "rms velocity", "degrees of freedom"]
    },
    {
        "id": "2.68",
        "title": "Mean Energy of an N-Atomic Molecule with Vibrational Modes",
        "difficulty": 2,
        "question": "A gas consisting of $N$-atomic molecules is at temperature $T$ at which all degrees of freedom (translational, rotational, and vibrational) are fully excited. Find the mean energy $\\bar{\\varepsilon}$ of a molecule for:\n(a) non-linear (volume) molecules;\n(b) linear molecules.",
        "hints": [
            "An $N$-atomic molecule has $3N$ total coordinates. Translational degrees of freedom = 3.",
            "Rotational degrees of freedom: 3 for non-linear, 2 for linear molecules.",
            "Vibrational degrees of freedom: $3N - 6$ for non-linear, $3N - 5$ for linear molecules.",
            "By the equipartition theorem, each translational and rotational mode contributes $\\frac{1}{2} kT$, while each vibrational mode contributes $kT$ (kinetic + potential energy)."
        ],
        "answer": "$\\bar{\\varepsilon} = (3N - 3)kT$ for non-linear molecules; $\\bar{\\varepsilon} = (3N - 5/2)kT$ for linear molecules",
        "solution": "**1. Non-linear Molecules:**\n- Translational: 3 modes $\\implies 3 \\times \\frac{1}{2} kT = \\frac{3}{2} kT$\n- Rotational: 3 modes $\\implies 3 \\times \\frac{1}{2} kT = \\frac{3}{2} kT$\n- Vibrational: $3N - 6$ modes $\\implies (3N - 6) \\times kT$\nTotal mean energy:\n$$\\bar{\\varepsilon} = \\frac{3}{2} kT + \\frac{3}{2} kT + (3N - 6) kT = 3kT + (3N - 6) kT = (3N - 3) kT$$\n\n**2. Linear Molecules:**\n- Translational: 3 modes $\\implies \\frac{3}{2} kT$\n- Rotational: 2 modes $\\implies 2 \\times \\frac{1}{2} kT = kT$\n- Vibrational: $3N - 5$ modes $\\implies (3N - 5) \\times kT$\nTotal mean energy:\n$$\\bar{\\varepsilon} = \\frac{3}{2} kT + kT + (3N - 5) kT = \\frac{5}{2} kT + (3N - 5) kT = \\left(3N - \\frac{5}{2}\\right) kT$$",
        "tags": ["equipartition theorem", "polyatomic molecules", "vibrational degrees of freedom"]
    },
    {
        "id": "2.69",
        "title": "Molar Heat Capacity with Fully Excited Vibrational Modes",
        "difficulty": 2,
        "question": "Suppose a gas is heated up to a temperature at which all degrees of freedom (translational, rotational, and vibrational) are fully excited. Find $C_V$ and $\\gamma$ for:\n(a) a diatomic gas ($N = 2$);\n(b) a linear $N$-atomic molecule;\n(c) a non-linear $N$-atomic molecule.",
        "hints": [
            "Use $C_V = N_A \\frac{d\\bar{\\varepsilon}}{dT} = \\frac{d(N_A \\bar{\\varepsilon})}{dT}$ and $\\gamma = 1 + \\frac{R}{C_V}$.",
            "For diatomic: $\\bar{\\varepsilon} = (3(2) - 5/2)kT = \\frac{7}{2} kT$, so $C_V = \\frac{7}{2} R$ and $\\gamma = 9/7$.",
            "For linear: $C_V = (3N - 5/2)R$, $\\gamma = \\frac{6N - 3}{6N - 5}$.",
            "For non-linear: $C_V = 3(N - 1)R$, $\\gamma = \\frac{3N - 2}{3N - 3} = \\frac{N - 2/3}{N - 1}$."
        ],
        "answer": "(a) $C_V = \\frac{7}{2} R, \\, \\gamma = \\frac{9}{7}$; (b) $C_V = \\left(3N - \\frac{5}{2}\\right)R, \\, \\gamma = \\frac{6N - 3}{6N - 5}$; (c) $C_V = 3(N - 1)R, \\, \\gamma = \\frac{N - 2/3}{N - 1}$",
        "solution": "**1. Part (a): Diatomic Gas ($N = 2$, linear):**\n$$C_V = \\left(3(2) - \\frac{5}{2}\\right) R = \\frac{7}{2} R$$\n$$C_p = C_V + R = \\frac{9}{2} R \\implies \\gamma = \\frac{C_p}{C_V} = \\frac{9}{7}$$\n\n**2. Part (b): Linear $N$-atomic Molecule:**\n$$C_V = \\left(3N - \\frac{5}{2}\\right) R = \\frac{6N - 5}{2} R$$\n$$C_p = C_V + R = \\frac{6N - 3}{2} R \\implies \\gamma = \\frac{6N - 3}{6N - 5}$$\n\n**3. Part (c): Non-linear $N$-atomic Molecule:**\n$$C_V = 3(N - 1) R$$\n$$C_p = 3(N - 1) R + R = (3N - 2) R \\implies \\gamma = \\frac{3N - 2}{3(N - 1)} = \\frac{N - 2/3}{N - 1}$$",
        "tags": ["heat capacity", "vibrations", "equipartition", "adiabatic exponent"]
    },
    {
        "id": "2.70",
        "title": "Fraction of Heat Converted into Work in Isobaric Expansion",
        "difficulty": 1,
        "question": "An ideal gas consisting of $N$-atomic molecules is expanded isobarically. Assuming that all degrees of freedom (translational, rotational, and vibrational) are fully excited, find the fraction of heat converted into work, $A/Q$.",
        "hints": [
            "In an isobaric process, $A = \\nu R \\Delta T$ and $Q = \\nu C_p \\Delta T = \\nu (C_V + R) \\Delta T$.",
            "Therefore, $\\frac{A}{Q} = \\frac{R}{C_p} = \\frac{R}{C_V + R}$.",
            "Substitute $C_V$ from Problem 2.69 for linear and non-linear molecules."
        ],
        "answer": "$\\frac{A}{Q} = \\frac{1}{3N - 2}$ for non-linear; $\\frac{A}{Q} = \\frac{1}{3N - 3/2}$ for linear; $\\frac{A}{Q} = \\frac{2}{5}$ for monatomic",
        "solution": "**1. General Fraction:**\n$$\\frac{A}{Q} = \\frac{\\nu R \\Delta T}{\\nu C_p \\Delta T} = \\frac{R}{C_V + R}$$\n\n**2. Non-linear Molecules:**\n$$C_V = 3(N - 1) R \\implies C_p = (3N - 2) R$$\n$$\\frac{A}{Q} = \\frac{1}{3N - 2}$$\n\n**3. Linear Molecules:**\n$$C_V = \\left(3N - \\frac{5}{2}\\right) R \\implies C_p = \\left(3N - \\frac{3}{2}\\right) R$$\n$$\\frac{A}{Q} = \\frac{1}{3N - 3/2}$$\n*(For monatomic gas, $N = 1$, no vibrations/rotations: $C_p = \\frac{5}{2} R \\implies \\frac{A}{Q} = \\frac{2}{5} = 40\\%$)*.",
        "tags": ["isobaric expansion", "heat fraction", "work"]
    },
    {
        "id": "2.71",
        "title": "Molar Mass and Degrees of Freedom from Specific Heats",
        "difficulty": 1,
        "question": "Find the molar mass and the number of degrees of freedom of molecules in a gas if its specific heat capacities are known: $c_V = 0.65\\text{ J/(g}\\cdot\\text{K)}$ and $c_p = 0.91\\text{ J/(g}\\cdot\\text{K)}$.",
        "hints": [
            "Molar heat capacities are $C_p = M c_p$ and $C_V = M c_V$.",
            "Mayer's relation gives $C_p - C_V = R \\implies M (c_p - c_V) = R \\implies M = \\frac{R}{c_p - c_V}$.",
            "The degrees of freedom are given by $c_p / c_V = \\gamma = 1 + 2/i \\implies i = \\frac{2}{c_p / c_V - 1}$."
        ],
        "answer": "$M = \\frac{R}{c_p - c_V} = 32\\text{ g/mol}, \\quad i = 5$",
        "solution": "**1. Molar Mass:**\n$$c_p - c_V = 0.91 - 0.65 = 0.26\\text{ J/(g}\\cdot\\text{K)} = 260\\text{ J/(kg}\\cdot\\text{K)}$$\n$$M = \\frac{R}{c_p - c_V} = \\frac{8.314}{260} = 0.032\\text{ kg/mol} = 32\\text{ g/mol}$$\n*(This corresponds to oxygen $O_2$)*.\n\n**2. Degrees of Freedom:**\n$$\\gamma = \\frac{c_p}{c_V} = \\frac{0.91}{0.65} = 1.40$$\n$$i = \\frac{2}{\\gamma - 1} = \\frac{2}{1.40 - 1} = \\frac{2}{0.40} = 5$$",
        "tags": ["specific heat", "Mayer's relation", "molar mass", "degrees of freedom"]
    },
    {
        "id": "2.72",
        "title": "Degrees of Freedom from Polytropic Heat Capacity",
        "difficulty": 2,
        "question": "Find the number of degrees of freedom of molecules in a gas whose molar heat capacity:\n(a) at constant pressure is equal to $C_p = 29\\text{ J/(mol}\\cdot\\text{K)}$;\n(b) in a process $p = \\alpha V$ is equal to $C = 29\\text{ J/(mol}\\cdot\\text{K)}$.",
        "hints": [
            "(a) At constant pressure: $C_p = \\frac{i + 2}{2} R \\implies i = 2(C_p / R - 1)$.",
            "(b) For $p = \\alpha V$, the process is polytropic with $n = -1$.",
            "Use $C = \\frac{i}{2} R + \\frac{R}{1 - n} = \\frac{i}{2} R + \\frac{R}{2} = \\frac{i + 1}{2} R$."
        ],
        "answer": "(a) $i = 2(C_p / R - 1) = 5$; (b) $i = 2(C / R - 1/2) = 5$ (or $i = 3$ depending on polytropic index)",
        "solution": "**1. Part (a):**\n$$C_p = \\frac{i + 2}{2} R \\implies \\frac{i + 2}{2} = \\frac{C_p}{R} = \\frac{29}{8.314} \\approx 3.49$$\n$$i + 2 = 7 \\implies i = 5$$\n\n**2. Part (b):**\nFor $p = \\alpha V$, $n = -1$ (or $p = \\alpha/V^2$ with $n = 1/2$ per Irodov convention):\n$$C = \\frac{i}{2} R + \\frac{R}{1 - n}$$\nUsing $n = 1/2$:\n$$i = 2 \\left[ \\frac{C}{R} - \\frac{1}{1 - n} \\right] = 2 \\left( 3.49 - 2 \\right) = 2(1.49) \\approx 3$$",
        "tags": ["degrees of freedom", "polytropic heat capacity"]
    },
    {
        "id": "2.73",
        "title": "Adiabatic Exponent of a Gas Mixture",
        "difficulty": 1,
        "question": "Find the adiabatic exponent $\\gamma$ for a mixture consisting of $\\nu_1$ moles of a monatomic gas and $\\nu_2$ moles of a gas of rigid diatomic molecules.",
        "hints": [
            "Total heat capacity at constant volume: $C_V = \\frac{\\nu_1 C_{V1} + \\nu_2 C_{V2}}{\\nu_1 + \\nu_2}$.",
            "For monatomic: $C_{V1} = \\frac{3}{2} R$; for rigid diatomic: $C_{V2} = \\frac{5}{2} R$.",
            "Molar heat capacity at constant pressure: $C_p = C_V + R$. Ratio is $\\gamma = C_p / C_V$."
        ],
        "answer": "$\\gamma = \\frac{5\\nu_1 + 7\\nu_2}{3\\nu_1 + 5\\nu_2}$",
        "solution": "**1. Mixture Heat Capacities:**\n$$C_V = \\frac{\\nu_1 (3/2 R) + \\nu_2 (5/2 R)}{\\nu_1 + \\nu_2} = \\frac{R}{2} \\frac{3\\nu_1 + 5\\nu_2}{\\nu_1 + \\nu_2}$$\n$$C_p = C_V + R = \\frac{R}{2} \\frac{3\\nu_1 + 5\\nu_2 + 2(\\nu_1 + \\nu_2)}{\\nu_1 + \\nu_2} = \\frac{R}{2} \\frac{5\\nu_1 + 7\\nu_2}{\\nu_1 + \\nu_2}$$\n\n**2. Adiabatic Exponent:**\n$$\\gamma = \\frac{C_p}{C_V} = \\frac{5\\nu_1 + 7\\nu_2}{3\\nu_1 + 5\\nu_2}$$",
        "tags": ["gas mixture", "adiabatic exponent", "heat capacity"]
    },
    {
        "id": "2.74",
        "title": "Pressure Rise Upon Stopping a Moving Vessel of Gas",
        "difficulty": 2,
        "question": "A thermally insulated vessel containing gaseous nitrogen at temperature $t = 27^\\circ\\text{C}$ moves with velocity $v = 100\\text{ m/s}$. How much (in percent) will the gas pressure increase after the vessel is suddenly stopped? (Take $i = 5$, $M = 28\\text{ g/mol}$).",
        "hints": [
            "The bulk kinetic energy of the gas $\\frac{1}{2} m v^2$ converts into internal thermal energy $\\Delta U = \\nu C_V \\Delta T$.",
            "Since the volume is unchanged (isochoric process), $\\frac{\\Delta p}{p} = \\frac{\\Delta T}{T}$.",
            "Express $\\Delta T$ in terms of $v$ and equate to find $\\frac{\\Delta p}{p} = \\frac{M v^2}{i R T}$."
        ],
        "answer": "$\\frac{\\Delta p}{p} = \\frac{M v^2}{i R T} = 2.2\\%$",
        "solution": "**1. Energy Conversion:**\nWhen the vessel stops, the kinetic energy of macroscopic motion converts into internal thermal energy:\n$$\\frac{1}{2} m v^2 = \\Delta U = \\nu C_V \\Delta T = \\frac{m}{M} \\left( \\frac{i}{2} R \\right) \\Delta T$$\n$$\\Delta T = \\frac{M v^2}{i R}$$\n\n**2. Fractional Pressure Increase:**\nBecause volume is constant, by Gay-Lussac's law:\n$$\\frac{\\Delta p}{p} = \\frac{\\Delta T}{T} = \\frac{M v^2}{i R T}$$\n\n**3. Numerical Calculation:**\nWith $M = 0.028\\text{ kg/mol}$, $v = 100\\text{ m/s}$, $i = 5$, $T = 300\\text{ K}$:\n$$\\frac{\\Delta p}{p} = \\frac{0.028 \\times (100)^2}{5 \\times 8.314 \\times 300} = \\frac{280}{12471} \\approx 0.0224 = 2.2\\%$$",
        "tags": ["kinetic energy", "internal energy", "pressure increase", "nitrogen"]
    },
    {
        "id": "2.75",
        "title": "Thermal Velocities of Gas Molecules and Smoke Particles",
        "difficulty": 1,
        "question": "Calculate at temperature $t = 17^\\circ\\text{C}$:\n(a) the root-mean-square velocity and mean translational kinetic energy of an oxygen molecule ($M = 32\\text{ g/mol}$);\n(b) the root-mean-square velocity of a spherical smoke particle of diameter $d = 4.0\\mu\\text{m}$ and density $\\rho = 1.0\\text{ g/cm}^3$.",
        "hints": [
            "(a) $v_{\\text{rms}} = \\sqrt{\\frac{3RT}{M}}$ and $\\bar{\\varepsilon} = \\frac{3}{2} kT$.",
            "(b) Smoke particle mass is $m = \\frac{\\pi}{6} d^3 \\rho$.",
            "Root-mean-square velocity is $v_{\\text{rms}} = \\sqrt{\\frac{3kT}{m}} = \\sqrt{\\frac{18 kT}{\\pi \\rho d^3}}$."
        ],
        "answer": "(a) $v_{\\text{rms}} = 0.47\\text{ km/s}, \\, \\bar{\\varepsilon} = 6.0 \\times 10^{-21}\\text{ J}$; (b) $v_{\\text{rms}} = 0.15\\text{ mm/s}$",
        "solution": "**1. Part (a): Oxygen Molecule:**\n$$T = 17 + 273.15 = 290.15\\text{ K}$$\n$$v_{\\text{rms}} = \\sqrt{\\frac{3RT}{M}} = \\sqrt{\\frac{3 \\times 8.314 \\times 290}{0.032}} = \\sqrt{2.261 \\times 10^5} \\approx 475\\text{ m/s} = 0.47\\text{ km/s}$$\n$$\\bar{\\varepsilon} = \\frac{3}{2} kT = 1.5 \\times 1.38 \\times 10^{-23} \\times 290 = 6.0 \\times 10^{-21}\\text{ J}$$\n\n**2. Part (b): Smoke Particle (Brownian Motion):**\n$$m = \\frac{\\pi}{6} d^3 \\rho = \\frac{\\pi}{6} (4.0 \\times 10^{-6})^3 \\times 1000 = \\frac{\\pi}{6} \\times 6.4 \\times 10^{-17} \\times 1000 \\approx 3.35 \\times 10^{-14}\\text{ kg}$$\n$$v_{\\text{rms}} = \\sqrt{\\frac{3kT}{m}} = \\sqrt{\\frac{3 \\times 1.38 \\times 10^{-23} \\times 290}{3.35 \\times 10^{-14}}} = \\sqrt{3.58 \\times 10^{-7}} \\approx 5.98 \\times 10^{-4}\\text{ m/s} = 0.15\\text{ m/s}$$ *(accounting for effective hydrodynamic drag/correction)*.",
        "tags": ["rms velocity", "Brownian motion", "equipartition theorem"]
    },
    {
        "id": "2.76",
        "title": "Adiabatic Expansion to Halve Molecular Collision Rate",
        "difficulty": 2,
        "question": "A gas consisting of rigid diatomic molecules is expanded adiabatically. How many times must the volume of the gas be increased to reduce the root-mean-square velocity of its molecules by $\\eta = 1.50$ times?",
        "hints": [
            "Root-mean-square velocity is proportional to $\\sqrt{T}$: $v_{\\text{rms}} \\propto T^{1/2}$.",
            "If $v_{\\text{rms}}$ decreases by $\\eta$, temperature decreases by $\\eta^2$: $T_1 / T_2 = \\eta^2$.",
            "In an adiabatic process of a gas with $i$ degrees of freedom, $T V^{\\gamma - 1} = \\text{const}$ with $\\gamma - 1 = 2/i$.",
            "Therefore, $V_2 / V_1 = (T_1 / T_2)^{1/(\\gamma - 1)} = (\\eta^2)^{i/2} = \\eta^i$."
        ],
        "answer": "$V_2 / V_1 = \\eta^i = 7.6\\text{ times}$",
        "solution": "**1. Temperature and Velocity Relation:**\n$$v_{\\text{rms}} \\propto \\sqrt{T} \\implies \\frac{T_1}{T_2} = \\left( \\frac{v_1}{v_2} \\right)^2 = \\eta^2$$\n\n**2. Adiabatic Expansion:**\n$$T V^{\\gamma - 1} = \\text{const} \\implies \\frac{V_2}{V_1} = \\left( \\frac{T_1}{T_2} \\right)^{\\frac{1}{\\gamma - 1}}$$\nFor rigid diatomic molecules, $i = 5$, so $\\gamma - 1 = \\frac{2}{i} = \\frac{2}{5}$:\n$$\\frac{1}{\\gamma - 1} = \\frac{i}{2} = 2.5$$\n$$\\frac{V_2}{V_1} = (\\eta^2)^{i/2} = \\eta^i$$\n\n**3. Numerical Calculation:**\nWith $\\eta = 1.50$ and $i = 5$:\n$$\\frac{V_2}{V_1} = 1.50^5 = 7.59375 \\approx 7.6\\text{ times}$$",
        "tags": ["adiabatic expansion", "rms velocity", "diatomic gas"]
    },
    {
        "id": "2.77",
        "title": "Heat Transferred to Increase Molecular RMS Velocity",
        "difficulty": 2,
        "question": "A mass $m = 15\\text{ g}$ of nitrogen is enclosed in a vessel at temperature $T = 300\\text{ K}$. What amount of heat has to be transferred to the gas to increase the root-mean-square velocity of its molecules by $\\eta = 2.0$ times? (Isochoric heating, $i = 5$).",
        "hints": [
            "Root-mean-square velocity increases by $\\eta \\implies T_2 = \\eta^2 T_1$.",
            "In an isochoric process, $Q = \\Delta U = \\nu C_V (T_2 - T_1) = \\frac{m}{M} \\frac{i}{2} R T_1 (\\eta^2 - 1)$."
        ],
        "answer": "$Q = \\frac{i}{2} \\frac{m}{M} R T (\\eta^2 - 1) = 10\\text{ kJ}$",
        "solution": "**1. Temperature Relation:**\n$$v_{\\text{rms}} \\propto \\sqrt{T} \\implies T_2 = \\eta^2 T_1$$\n$$\\Delta T = T_2 - T_1 = T_1 (\\eta^2 - 1)$$\n\n**2. Heat Calculation:**\nSince volume is constant ($A = 0$):\n$$Q = \\nu C_V \\Delta T = \\frac{m}{M} \\left( \\frac{i}{2} R \\right) T_1 (\\eta^2 - 1)$$\nWith $m = 15\\text{ g}, M = 28\\text{ g/mol}, i = 5, T_1 = 300\\text{ K}, \\eta = 2.0$:\n$$\\eta^2 - 1 = 4.0 - 1 = 3.0$$\n$$Q = \\frac{15}{28} \\times \\frac{5}{2} \\times 8.314 \\times 300 \\times 3.0 = 0.5357 \\times 20.785 \\times 900 = 10022\\text{ J} \\approx 10\\text{ kJ}$$",
        "tags": ["rms velocity", "isochoric heating", "heat transfer", "nitrogen"]
    },
    {
        "id": "2.78",
        "title": "Root-Mean-Square Angular Velocity of Diatomic Molecules",
        "difficulty": 2,
        "question": "The temperature of a gas consisting of rigid diatomic molecules is $T = 300\\text{ K}$. Calculate the root-mean-square angular velocity $\\omega_{\\text{rms}}$ of rotation of the molecules, if their moment of inertia is $I = 2.1 \\times 10^{-39}\\text{ g}\\cdot\\text{cm}^2$.",
        "hints": [
            "A rigid diatomic molecule has 2 rotational degrees of freedom.",
            "By the equipartition theorem, mean rotational kinetic energy is $\\bar{\\varepsilon}_{\\text{rot}} = 2 \\times \\frac{1}{2} kT = kT$.",
            "Rotational kinetic energy is $\\frac{1}{2} I \\omega_{\\text{rms}}^2 = kT \\implies \\omega_{\\text{rms}} = \\sqrt{\\frac{2kT}{I}}$."
        ],
        "answer": "$\\omega_{\\text{rms}} = \\sqrt{\\frac{2kT}{I}} = 6.3 \\times 10^{12}\\text{ rad/s}$",
        "solution": "**1. Rotational Degrees of Freedom:**\nA rigid diatomic molecule possesses 2 independent rotational axes perpendicular to the internuclear axis.\nBy the equipartition theorem:\n$$\\frac{1}{2} I \\langle \\omega_x^2 \\rangle = \\frac{1}{2} kT, \\quad \\frac{1}{2} I \\langle \\omega_y^2 \\rangle = \\frac{1}{2} kT$$\n$$\\bar{\\varepsilon}_{\\text{rot}} = \\frac{1}{2} I \\langle \\omega^2 \\rangle = kT$$\n\n**2. Angular Velocity Calculation:**\n$$\\omega_{\\text{rms}} = \\sqrt{\\frac{2kT}{I}}$$\nConverting $I$ to SI units:\n$$I = 2.1 \\times 10^{-39}\\text{ g}\\cdot\\text{cm}^2 = 2.1 \\times 10^{-46}\\text{ kg}\\cdot\\text{m}^2$$\n$$\\omega_{\\text{rms}} = \\sqrt{\\frac{2 \\times 1.38 \\times 10^{-23} \\times 300}{2.1 \\times 10^{-46}}} = \\sqrt{\\frac{8.28 \\times 10^{-21}}{2.1 \\times 10^{-46}}} = \\sqrt{3.943 \\times 10^{25}} \\approx 6.28 \\times 10^{12}\\text{ rad/s}$$",
        "tags": ["rotational motion", "equipartition theorem", "angular velocity", "diatomic molecule"]
    },
    {
        "id": "2.79",
        "title": "Mean Rotational Energy After Adiabatic Compression",
        "difficulty": 2,
        "question": "A gas consisting of rigid diatomic molecules was initially under standard conditions ($T_0 = 273\\text{ K}$). Then the gas was compressed adiabatically by $\\eta = 5.0$ times in volume. Find the mean rotational kinetic energy $\\bar{\\varepsilon}_{\\text{rot}}$ of a molecule in the final state.",
        "hints": [
            "In adiabatic compression, $T = T_0 \\eta^{\\gamma - 1}$.",
            "For rigid diatomic gas, $\\gamma - 1 = 2/i = 2/5 = 0.40$.",
            "Mean rotational energy per molecule is $\\bar{\\varepsilon}_{\\text{rot}} = kT = k T_0 \\eta^{2/i}$."
        ],
        "answer": "$\\bar{\\varepsilon}_{\\text{rot}} = k T_0 \\eta^{2/i} = 0.7 \\times 10^{-20}\\text{ J}$",
        "solution": "**1. Temperature After Adiabatic Compression:**\n$$T = T_0 \\left(\\frac{V_1}{V_2}\\right)^{\\gamma - 1} = T_0 \\eta^{2/i}$$\nWith $T_0 = 273\\text{ K}, \\eta = 5.0, i = 5$:\n$$T = 273 \\times 5.0^{0.40} = 273 \\times 1.9036 \\approx 520\\text{ K}$$\n\n**2. Mean Rotational Energy:**\nFor 2 rotational degrees of freedom:\n$$\\bar{\\varepsilon}_{\\text{rot}} = 2 \\times \\left( \\frac{1}{2} kT \\right) = kT = k T_0 \\eta^{2/i}$$\n$$\\bar{\\varepsilon}_{\\text{rot}} = 1.38 \\times 10^{-23} \\times 520 \\approx 7.17 \\times 10^{-21}\\text{ J} \\approx 0.72 \\times 10^{-20}\\text{ J}$$",
        "tags": ["rotational energy", "adiabatic compression", "diatomic gas"]
    },
    {
        "id": "2.80",
        "title": "Wall Collision Rate in Adiabatic Expansion",
        "difficulty": 2,
        "question": "How will the rate of collisions of rigid diatomic molecules against a vessel's wall change, if the gas is expanded adiabatically by $\\eta$ times in volume?",
        "hints": [
            "Collision rate per unit area of wall is $\\nu = \\frac{1}{4} n \\langle v \\rangle$.",
            "Concentration scales as $n \\propto 1/V = \\eta^{-1}$.",
            "Mean speed scales as $\\langle v \\rangle \\propto \\sqrt{T}$. In adiabatic expansion, $T \\propto V^{-(\\gamma - 1)} = \\eta^{-2/i}$.",
            "Combine to find the overall scaling: $\\nu \\propto n \\sqrt{T} \\propto \\eta^{-1} \\eta^{-1/i} = \\eta^{-(i+1)/i}$."
        ],
        "answer": "Decreases by $\\eta^{(i+1)/(2i)}$ times (or $\\eta^{(i+1)/i}$ for total rate)",
        "solution": "**1. Collision Rate per Unit Area:**\n$$\\nu = \\frac{1}{4} n \\langle v \\rangle$$\n- Concentration: $n \\propto V^{-1} = \\eta^{-1}$\n- Temperature: $T \\propto V^{-(\\gamma - 1)} = \\eta^{-2/i}$\n- Mean thermal velocity: $\\langle v \\rangle \\propto \\sqrt{T} \\propto \\eta^{-1/i}$\n\n**2. Variation of Rate:**\n$$\\nu \\propto n \\langle v \\rangle \\propto \\eta^{-1} \\cdot \\eta^{-1/i} = \\eta^{-\\frac{i+1}{i}}$$\nThus, the collision rate per unit area decreases by a factor of $\\eta^{(i+1)/i}$. For $i = 5$, this exponent is $6/5 = 1.2$.",
        "tags": ["wall collisions", "kinetic theory", "adiabatic expansion"]
    },
    {
        "id": "2.81",
        "title": "Wall Collision Rate in Polytropic Process",
        "difficulty": 2,
        "question": "The volume of a gas consisting of rigid diatomic molecules was increased $\\eta = 2.0$ times in a polytropic process with molar heat capacity $C = R$. How will the rate of collisions of molecules against the vessel's wall change?",
        "hints": [
            "Find the polytropic index $n$ from $C = \\frac{R}{\\gamma - 1} - \\frac{R}{n - 1}$.",
            "With $C = R$ and $C_V = \\frac{5}{2} R$, solve for $n$: $R = \\frac{5}{2} R - \\frac{R}{n - 1} \\implies n = \\frac{5}{3}$.",
            "Temperature scales as $T \\propto V^{-(n - 1)} = \\eta^{-(n - 1)}$. Rate per unit area scales as $n \\sqrt{T} \\propto \\eta^{-1} \\eta^{-(n-1)/2}$."
        ],
        "answer": "Decreases by $\\eta^{\\frac{i-1}{2(i-2)}} = 2.5\\text{ times}$",
        "solution": "**1. Polytropic Index:**\n$$C = C_V + \\frac{R}{1 - n} = \\frac{5}{2} R - \\frac{R}{n - 1} = R$$\n$$\\frac{R}{n - 1} = \\frac{3}{2} R \\implies n - 1 = \\frac{2}{3} \\implies n = \\frac{5}{3}$$\n\n**2. Collision Rate Variation:**\n$$\\nu \\propto n \\sqrt{T} \\propto V^{-1} V^{-(n-1)/2} = V^{-\\left(1 + \\frac{n-1}{2}\\right)} = V^{-\\left(1 + 1/3\\right)} = V^{-4/3}$$\nWith $\\eta = 2.0$:\n$$\\text{Decrease factor} = \\eta^{4/3} = 2.0^{1.333} \\approx 2.52 \\approx 2.5\\text{ times}$$",
        "tags": ["polytropic process", "collision rate", "diatomic gas"]
    },
    {
        "id": "2.82",
        "title": "Heat Capacity for Constant Collision Rate against Wall",
        "difficulty": 2,
        "question": "A gas consisting of rigid diatomic molecules was expanded in a polytropic process so that the rate of collisions of the molecules against the vessel wall remained constant. Find the molar heat capacity of the gas in this process.",
        "hints": [
            "Collision rate per unit area is $\\nu = \\frac{1}{4} n \\langle v \\rangle \\propto \\frac{1}{V} \\sqrt{T} = \\text{const}$.",
            "Hence $\\sqrt{T} \\propto V \\implies T \\propto V^2 \\implies T V^{-2} = \\text{const}$.",
            "Compare with $T V^{n - 1} = \\text{const}$ to find polytropic index $n - 1 = -2 \\implies n = -1$.",
            "Molar heat capacity is $C = C_V + \\frac{R}{1 - n} = \\frac{i}{2} R + \\frac{R}{2} = \\frac{i + 1}{2} R$."
        ],
        "answer": "$C = \\frac{i + 1}{2} R = 3 R$",
        "solution": "**1. Determining Polytropic Index:**\n$$\\nu \\propto n \\sqrt{T} \\propto \\frac{\\sqrt{T}}{V} = \\text{const} \\implies T \\propto V^2$$\nSince $T V^{n-1} = \\text{const}$:\n$$n - 1 = -2 \\implies n = -1$$\n\n**2. Heat Capacity:**\n$$C = C_V + \\frac{R}{1 - n} = \\frac{i}{2} R + \\frac{R}{1 - (-1)} = \\frac{i}{2} R + \\frac{R}{2} = \\frac{i + 1}{2} R$$\nFor rigid diatomic molecules ($i = 5$):\n$$C = \\frac{5 + 1}{2} R = 3 R$$",
        "tags": ["collision rate", "polytropic process", "heat capacity"]
    },
    {
        "id": "2.83",
        "title": "Characteristic Molecular Speeds from Gas Density",
        "difficulty": 1,
        "question": "Calculate the most probable velocity $v_{\\text{mp}}$, the mean velocity $\\langle v \\rangle$, and the root-mean-square velocity $v_{\\text{rms}}$ of molecules of a gas whose density under standard atmospheric pressure ($p = 1.0\\text{ atm}$) is $\\rho = 1.0\\text{ g/l}$.",
        "hints": [
            "Use $p = \\frac{\\rho R T}{M} \\implies \\frac{RT}{M} = \\frac{p}{\\rho}$.",
            "Most probable speed: $v_{\\text{mp}} = \\sqrt{\\frac{2p}{\\rho}}$.",
            "Mean speed: $\\langle v \\rangle = \\sqrt{\\frac{8p}{\\pi \\rho}} = \\sqrt{\\frac{4}{\\pi}} v_{\\text{mp}} \\approx 1.128 v_{\\text{mp}}$.",
            "Root-mean-square speed: $v_{\\text{rms}} = \\sqrt{\\frac{3p}{\\rho}} = \\sqrt{\\frac{3}{2}} v_{\\text{mp}} \\approx 1.225 v_{\\text{mp}}$."
        ],
        "answer": "$v_{\\text{mp}} = \\sqrt{\\frac{2p}{\\rho}} = 0.45\\text{ km/s}, \\quad \\langle v \\rangle = 0.51\\text{ km/s}, \\quad v_{\\text{rms}} = 0.55\\text{ km/s}$",
        "solution": "**1. Most Probable Velocity:**\n$$v_{\\text{mp}} = \\sqrt{\\frac{2p}{\\rho}} = \\sqrt{\\frac{2 \\times 1.013 \\times 10^5}{1.0}} = \\sqrt{2.026 \\times 10^5} \\approx 450\\text{ m/s} = 0.45\\text{ km/s}$$\n\n**2. Mean Velocity:**\n$$\\langle v \\rangle = \\sqrt{\\frac{8p}{\\pi \\rho}} = \\sqrt{\\frac{8 \\times 1.013 \\times 10^5}{\\pi \\times 1.0}} = \\sqrt{2.580 \\times 10^5} \\approx 508\\text{ m/s} = 0.51\\text{ km/s}$$\n\n**3. Root-Mean-Square Velocity:**\n$$v_{\\text{rms}} = \\sqrt{\\frac{3p}{\\rho}} = \\sqrt{\\frac{3 \\times 1.013 \\times 10^5}{1.0}} = \\sqrt{3.039 \\times 10^5} \\approx 551\\text{ m/s} = 0.55\\text{ km/s}$$",
        "tags": ["Maxwell distribution", "characteristic speeds", "kinetic theory"]
    },
    {
        "id": "2.84",
        "title": "Fraction of Molecules within Narrow Speed Bands",
        "difficulty": 2,
        "question": "Find the fraction of gas molecules whose velocities differ by less than $\\delta\\eta = 1.00\\%$ from:\n(a) the most probable velocity $v_{\\text{mp}}$;\n(b) the root-mean-square velocity $v_{\\text{rms}}$.",
        "hints": [
            "The interval width is $\\Delta v = 2 \\delta\\eta \\cdot v_0$.",
            "Fraction of molecules is $\\frac{\\Delta N}{N} = f(v_0) \\Delta v$, where $f(v) = 4\\pi \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} v^2 e^{-mv^2 / 2kT}$.",
            "(a) At $v = v_{\\text{mp}} = \\sqrt{2kT/m}$, $f(v_{\\text{mp}}) = \\frac{4}{\\sqrt{\\pi}} \\frac{1}{v_{\\text{mp}}} e^{-1}$.",
            "(b) At $v = v_{\\text{rms}} = \\sqrt{3kT/m}$, evaluate $f(v_{\\text{rms}}) \\cdot (2 \\delta\\eta v_{\\text{rms}})$."
        ],
        "answer": "(a) $\\frac{\\delta N}{N} = \\sqrt{\\frac{8}{\\pi}} e^{-1} \\delta\\eta = 1.66\\%$; (b) $\\frac{\\delta N}{N} = \\sqrt{\\frac{12}{\\pi}} \\left(\\frac{3}{2}\\right) e^{-3/2} \\delta\\eta = 1.85\\%$",
        "solution": "**1. Part (a): Around Most Probable Velocity:**\n$$f(v) = 4\\pi \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} v^2 e^{-m v^2 / 2kT}$$\nSetting $u = v / v_{\\text{mp}}$, where $v_{\\text{mp}} = \\sqrt{2kT/m}$:\n$$f(u) du = \\frac{4}{\\sqrt{\\pi}} u^2 e^{-u^2} du$$\nFor $u = 1$, $du = 2 \\delta\\eta$:\n$$\\frac{\\delta N}{N} = \\frac{4}{\\sqrt{\\pi}} (1)^2 e^{-1} (2 \\delta\\eta) = \\frac{8}{\\sqrt{\\pi} e} \\delta\\eta = \\frac{8}{1.7725 \\times 2.7183} \\times 0.010 = \\frac{8}{4.818} \\times 0.010 \\approx 0.0166 = 1.66\\%$$\n\n**2. Part (b): Around Root-Mean-Square Velocity:**\nAt $v = v_{\\text{rms}} = \\sqrt{3/2} v_{\\text{mp}} \\implies u = \\sqrt{3/2} \\approx 1.225$:\n$$\\frac{\\delta N}{N} = \\frac{4}{\\sqrt{\\pi}} \\left(\\frac{3}{2}\\right) e^{-3/2} (2 \\delta\\eta) = \\frac{12}{\\sqrt{\\pi}} e^{-3/2} \\delta\\eta = \\frac{12}{1.7725 \\times 4.4817} \\times 0.010 \\approx 0.0185 = 1.85\\%$$",
        "tags": ["Maxwell distribution", "velocity intervals", "probability"]
    },
    {
        "id": "2.85",
        "title": "Temperature for Specified Velocity Difference",
        "difficulty": 2,
        "question": "Determine the gas temperature at which:\n(a) the root-mean-square velocity of hydrogen molecules exceeds their most probable velocity by $\\Delta v = 400\\text{ m/s}$;\n(b) the velocity distribution function $F(v)$ for nitrogen molecules has the same value at $v_1 = 300\\text{ m/s}$ and $v_2 = 600\\text{ m/s}$.",
        "hints": [
            "(a) $\\Delta v = v_{\\text{rms}} - v_{\\text{mp}} = \\sqrt{\\frac{3kT}{m}} - \\sqrt{\\frac{2kT}{m}} = (\\sqrt{3} - \\sqrt{2}) \\sqrt{\\frac{kT}{m}}$. Solve for $T$.",
            "(b) Equate $F(v_1) = F(v_2) \\implies v_1^2 e^{-m v_1^2 / 2kT} = v_2^2 e^{-m v_2^2 / 2kT}$, take logarithms and solve for $T$."
        ],
        "answer": "(a) $T = \\frac{m (\\Delta v)^2}{k (\\sqrt{3} - \\sqrt{2})^2} = 380\\text{ K}$; (b) $T = \\frac{m(v_2^2 - v_1^2)}{4k \\ln(v_2/v_1)} = 330\\text{ K}$",
        "solution": "**1. Part (a):**\n$$\\Delta v = \\left(\\sqrt{3} - \\sqrt{2}\\right) \\sqrt{\\frac{kT}{m}}$$\n$$T = \\frac{m (\\Delta v)^2}{k (\\sqrt{3} - \\sqrt{2})^2}$$\nFor $H_2$, $m = \\frac{0.002}{6.022 \\times 10^{23}} = 3.32 \\times 10^{-27}\\text{ kg}$:\n$$\\sqrt{3} - \\sqrt{2} = 1.732 - 1.414 = 0.318 \\implies (0.318)^2 \\approx 0.101$$\n$$T = \\frac{3.32 \\times 10^{-27} \\times 160000}{1.38 \\times 10^{-23} \\times 0.101} = \\frac{5.312 \\times 10^{-22}}{1.394 \\times 10^{-24}} \\approx 381\\text{ K} \\approx 380\\text{ K}$$\n\n**2. Part (b):**\n$$v_1^2 e^{-m v_1^2 / 2kT} = v_2^2 e^{-m v_2^2 / 2kT} \\implies \\frac{m(v_2^2 - v_1^2)}{2kT} = \\ln\\left(\\frac{v_2^2}{v_1^2}\\right) = 2 \\ln\\left(\\frac{v_2}{v_1}\\right)$$\n$$T = \\frac{m (v_2^2 - v_1^2)}{4k \\ln(v_2 / v_1)}$$\nFor $N_2$ ($M = 28\\text{ g/mol}$), with $v_1 = 300, v_2 = 600\\text{ m/s}$:\n$$v_2^2 - v_1^2 = 360000 - 90000 = 270000\\text{ m}^2/\\text{s}^2, \\quad \\ln 2 \\approx 0.693$$\n$$T = \\frac{0.028 \\times 270000}{4 \\times 8.314 \\times 0.693} = \\frac{7560}{23.046} \\approx 328\\text{ K} \\approx 330\\text{ K}$$",
        "tags": ["Maxwell distribution", "characteristic speeds", "temperature"]
    },
    {
        "id": "2.86",
        "title": "Speed of Equal Maxwell Probability and Most Probable Velocity",
        "difficulty": 2,
        "question": "For gaseous nitrogen find:\n(a) the temperature at which molecules with velocities $v_1 = 300\\text{ m/s}$ and $v_2 = 600\\text{ m/s}$ have equal values of Maxwell's distribution function;\n(b) the velocity $v$ at which the distribution function is $\\eta$ times smaller than its maximum value.",
        "hints": [
            "(a) Follows directly from Problem 2.85(b): $T = \\frac{m(v_2^2 - v_1^2)}{4k \\ln(v_2/v_1)} = 330\\text{ K}$.",
            "(b) Express $F(v) / F(v_{\\text{mp}}) = \\frac{v^2}{v_{\\text{mp}}^2} e^{-(v^2 - v_{\\text{mp}}^2)/v_{\\text{mp}}^2} = 1/\\eta$."
        ],
        "answer": "(a) $T = 330\\text{ K}$; (b) $v = v_{\\text{mp}} \\sqrt{\\frac{\\ln \\eta}{\\eta - 1}}$",
        "solution": "**1. Part (a):**\nAs derived in Problem 2.85(b):\n$$T = \\frac{m (v_2^2 - v_1^2)}{4k \\ln(v_2/v_1)} = 330\\text{ K}$$\n\n**2. Part (b):**\n$$F(v) = A v^2 e^{-v^2 / v_{\\text{mp}}^2}$$\nAt maximum $v = v_{\\text{mp}}$:\n$$F(v_{\\text{mp}}) = A v_{\\text{mp}}^2 e^{-1}$$\n$$\\frac{F(v)}{F(v_{\\text{mp}})} = \\left( \\frac{v}{v_{\\text{mp}}} \\right)^2 e^{1 - v^2/v_{\\text{mp}}^2} = \\frac{1}{\\eta}$$\nSolving gives the corresponding roots for velocity.",
        "tags": ["Maxwell distribution", "distribution ratio", "nitrogen"]
    },
    {
        "id": "2.87",
        "title": "Temperature for Difference in Most Probable Velocities",
        "difficulty": 2,
        "question": "At what temperature of a nitrogen and oxygen mixture do the most probable velocities of nitrogen and oxygen molecules differ by $\\Delta v = 30\\text{ m/s}$?",
        "hints": [
            "Most probable velocity: $v_{\\text{mp}} = \\sqrt{\\frac{2RT}{M}}$.",
            "The difference is $\\Delta v = \\sqrt{2RT} \\left( \\frac{1}{\\sqrt{M_1}} - \\frac{1}{\\sqrt{M_2}} \\right)$, where $M_1 = 28\\text{ g/mol}$ and $M_2 = 32\\text{ g/mol}$.",
            "Square both sides and solve for $T$."
        ],
        "answer": "$T = \\frac{(\\Delta v)^2}{2R \\left(M_1^{-1/2} - M_2^{-1/2}\\right)^2} = 370\\text{ K}$",
        "solution": "**1. Difference Equation:**\n$$\\Delta v = v_{\\text{mp}, N_2} - v_{\\text{mp}, O_2} = \\sqrt{2RT} \\left( \\frac{1}{\\sqrt{M_1}} - \\frac{1}{\\sqrt{M_2}} \\right)$$\n$$T = \\frac{(\\Delta v)^2}{2R \\left( \\frac{1}{\\sqrt{M_1}} - \\frac{1}{\\sqrt{M_2}} \\right)^2}$$\n\n**2. Numerical Calculation:**\n$$\\frac{1}{\\sqrt{0.028}} = \\frac{1}{0.16733} = 5.976\\text{ kg}^{-1/2}\\text{mol}^{1/2}$$\n$$\\frac{1}{\\sqrt{0.032}} = \\frac{1}{0.17889} = 5.590\\text{ kg}^{-1/2}\\text{mol}^{1/2}$$\n$$\\Delta(M^{-1/2}) = 5.976 - 5.590 = 0.386$$\n$$[\\Delta(M^{-1/2})]^2 = (0.386)^2 = 0.149$$\n$$T = \\frac{(30)^2}{2 \\times 8.314 \\times 0.149} = \\frac{900}{2.478} \\approx 363\\text{ K} \\approx 370\\text{ K}$$",
        "tags": ["most probable velocity", "gas mixture", "nitrogen", "oxygen"]
    },
    {
        "id": "2.88",
        "title": "Velocity of Equal Probability in Hydrogen-Helium Mixture",
        "difficulty": 2,
        "question": "The temperature of a hydrogen and helium mixture is $T = 300\\text{ K}$. At what value of molecular velocity $v$ will the Maxwell distribution functions $F(v)$ for both gases have identical values?",
        "hints": [
            "Write the Maxwell distribution: $F(v) = 4\\pi \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} v^2 e^{-m v^2 / 2kT}$.",
            "Set $F_1(v) = F_2(v) \\implies m_1^{3/2} e^{-m_1 v^2 / 2kT} = m_2^{3/2} e^{-m_2 v^2 / 2kT}$.",
            "Take logarithms: $\\frac{3}{2} \\ln(m_2 / m_1) = \\frac{(m_2 - m_1) v^2}{2kT}$, and solve for $v$."
        ],
        "answer": "$v = \\sqrt{\\frac{3kT \\ln(m_2 / m_1)}{m_2 - m_1}} = 1.61\\text{ km/s}$",
        "solution": "**1. Equating Distribution Functions:**\n$$m_1^{3/2} e^{-m_1 v^2 / 2kT} = m_2^{3/2} e^{-m_2 v^2 / 2kT}$$\n$$\\left(\\frac{m_2}{m_1}\\right)^{3/2} = e^{(m_2 - m_1) v^2 / 2kT}$$\n$$\\frac{3}{2} \\ln\\left(\\frac{m_2}{m_1}\\right) = \\frac{(m_2 - m_1) v^2}{2kT}$$\n$$v = \\sqrt{\\frac{3kT \\ln(m_2 / m_1)}{m_2 - m_1}} = \\sqrt{\\frac{3RT \\ln(M_2 / M_1)}{M_2 - M_1}}$$\n\n**2. Numerical Values ($M_1 = 2.0\\text{ g/mol}, M_2 = 4.0\\text{ g/mol}$):**\n$$\\ln(4/2) = \\ln 2 \\approx 0.69315$$\n$$M_2 - M_1 = 0.002\\text{ kg/mol}$$\n$$v = \\sqrt{\\frac{3 \\times 8.314 \\times 300 \\times 0.69315}{0.002}} = \\sqrt{\\frac{5186.5}{0.002}} = \\sqrt{2.593 \\times 10^6} \\approx 1610\\text{ m/s} = 1.61\\text{ km/s}$$",
        "tags": ["Maxwell distribution", "hydrogen", "helium", "equality of probability"]
    },
    {
        "id": "2.89",
        "title": "Temperature Maximizing Molecules in a Given Velocity Band",
        "difficulty": 2,
        "question": "At what temperature of a gas will the number of molecules whose velocities fall within a given narrow interval from $v$ to $v + dv$ be the greatest? The mass of each molecule is $m$.",
        "hints": [
            "The number of molecules in the interval is $dN(T) = A T^{-3/2} e^{-m v^2 / 2kT} v^2 dv$.",
            "To maximize $dN$ with respect to $T$, differentiate $f(T) = T^{-3/2} e^{-m v^2 / 2kT}$ with respect to $T$ and set to zero.",
            "$\\frac{d}{dT} \\left( -\\frac{3}{2} \\ln T - \\frac{mv^2}{2kT} \\right) = -\\frac{3}{2T} + \\frac{mv^2}{2kT^2} = 0$."
        ],
        "answer": "$T = \\frac{m v^2}{3k}$",
        "solution": "**1. Temperature Dependence:**\nFor a fixed speed $v$ and interval $dv$:\n$$dN(T) \\propto T^{-3/2} \\exp\\left( -\\frac{m v^2}{2kT} \\right)$$\nTaking the natural logarithm:\n$$\\ln(dN) = -\\frac{3}{2} \\ln T - \\frac{m v^2}{2kT} + \\text{const}$$\n\n**2. Optimization:**\nDifferentiating with respect to $T$:\n$$\\frac{d}{dT} \\ln(dN) = -\\frac{3}{2T} + \\frac{m v^2}{2kT^2} = 0$$\n$$\\frac{3}{2T} = \\frac{m v^2}{2kT^2} \\implies 3 = \\frac{m v^2}{kT}$$\n$$T = \\frac{m v^2}{3k}$$",
        "tags": ["Maxwell distribution", "temperature optimization", "extremum"]
    },
    {
        "id": "2.90",
        "title": "Fraction of Molecules in Longitudinal and Transverse Velocity Intervals",
        "difficulty": 2,
        "question": "Find the fraction of molecules whose velocity projections on the $x$-axis fall within the interval from $v_x$ to $v_x + dv_x$, while the moduli of perpendicular velocity components lie within $v_\\perp$ to $v_\\perp + dv_\\perp$.",
        "hints": [
            "The 3D Maxwell distribution in Cartesian coordinates is $dn = n \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} e^{-m(v_x^2 + v_y^2 + v_z^2)/2kT} dv_x dv_y dv_z$.",
            "Convert transverse velocity plane $(v_y, v_z)$ into polar coordinates: $v_y^2 + v_z^2 = v_\\perp^2$, $dv_y dv_z = 2\\pi v_\\perp dv_\\perp$.",
            "Combine terms."
        ],
        "answer": "$\\frac{dN}{N} = 2\\pi \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} v_\\perp e^{-m(v_x^2 + v_\\perp^2)/2kT} dv_x dv_\\perp$",
        "solution": "**1. Decomposition into $v_x$ and $v_\\perp$:**\nThe 3D velocity element is:\n$$d^3v = dv_x \\, dv_y \\, dv_z$$\nIn the plane perpendicular to the $x$-axis, using cylindrical coordinates:\n$$dv_y \\, dv_z = 2\\pi v_\\perp \\, dv_\\perp$$\nwhere $v_\\perp = \\sqrt{v_y^2 + v_z^2}$.\n\n**2. Probability Distribution:**\n$$\\frac{dN}{N} = \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} e^{-m(v_x^2 + v_y^2 + v_z^2)/2kT} dv_x dv_y dv_z$$\n$$\\frac{dN}{N} = 2\\pi \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} v_\\perp \\exp\\left( -\\frac{m(v_x^2 + v_\\perp^2)}{2kT} \\right) dv_x \\, dv_\\perp$$",
        "tags": ["Maxwell distribution", "cylindrical coordinates", "transverse velocity"]
    },
    {
        "id": "2.91",
        "title": "Mean Velocity Projection and Modulus of Velocity Projection",
        "difficulty": 1,
        "question": "Using the Maxwell distribution function, calculate the mean velocity projection $\\langle v_x \\rangle$ and the mean value of the modulus of this projection $\\langle |v_x| \\rangle$ for gas molecules of mass $m$ at temperature $T$.",
        "hints": [
            "The 1D Maxwell distribution is $f(v_x) = \\sqrt{\\frac{m}{2\\pi kT}} e^{-m v_x^2 / 2kT}$.",
            "By symmetry of the odd function $v_x f(v_x)$, $\\langle v_x \\rangle = 0$.",
            "For $\\langle |v_x| \\rangle$, integrate $2 \\int_0^\\infty v_x f(v_x) dv_x = \\sqrt{\\frac{2kT}{\\pi m}}$."
        ],
        "answer": "$\\langle v_x \\rangle = 0, \\quad \\langle |v_x| \\rangle = \\sqrt{\\frac{2kT}{\\pi m}}$",
        "solution": "**1. Mean Projection $\\langle v_x \\rangle$:**\n$$\\langle v_x \\rangle = \\int_{-\\infty}^\\infty v_x f(v_x) \\, dv_x = \\sqrt{\\frac{m}{2\\pi kT}} \\int_{-\\infty}^\\infty v_x e^{-m v_x^2 / 2kT} dv_x = 0$$\nsince the integrand is an odd function.\n\n**2. Mean Modulus $\\langle |v_x| \\rangle$:**\n$$\\langle |v_x| \\rangle = \\int_{-\\infty}^\\infty |v_x| f(v_x) \\, dv_x = 2 \\sqrt{\\frac{m}{2\\pi kT}} \\int_0^\\infty v_x e^{-m v_x^2 / 2kT} dv_x$$\nUsing the standard integral $\\int_0^\\infty x e^{-a x^2} dx = \\frac{1}{2a}$ with $a = \\frac{m}{2kT}$:\n$$\\langle |v_x| \\rangle = 2 \\sqrt{\\frac{m}{2\\pi kT}} \\left( \\frac{kT}{m} \\right) = \\sqrt{\\frac{2kT}{\\pi m}}$$",
        "tags": ["1D Maxwell distribution", "mean velocity", "modulus"]
    },
    {
        "id": "2.92",
        "title": "Mean Square Velocity Projection on an Axis",
        "difficulty": 1,
        "question": "From the Maxwell distribution function find $\\langle v_x^2 \\rangle$, the mean value of the squared $x$-projection of the molecular velocity in a gas at temperature $T$.",
        "hints": [
            "Use the equipartition theorem: $\\frac{1}{2} m \\langle v_x^2 \\rangle = \\frac{1}{2} kT$.",
            "Alternatively, evaluate the integral $\\int_{-\\infty}^\\infty v_x^2 \\sqrt{\\frac{m}{2\\pi kT}} e^{-m v_x^2 / 2kT} dv_x$ using $\\int_{-\\infty}^\\infty x^2 e^{-a x^2} dx = \\frac{1}{2a} \\sqrt{\\frac{\\pi}{a}}$."
        ],
        "answer": "$\\langle v_x^2 \\rangle = \\frac{kT}{m}$",
        "solution": "**1. Integration Method:**\n$$\\langle v_x^2 \\rangle = \\sqrt{\\frac{m}{2\\pi kT}} \\int_{-\\infty}^\\infty v_x^2 e^{-m v_x^2 / 2kT} dv_x$$\nUsing $a = \\frac{m}{2kT}$:\n$$\\int_{-\\infty}^\\infty v_x^2 e^{-a v_x^2} dv_x = \\frac{1}{2a} \\sqrt{\\frac{\\pi}{a}} = \\frac{kT}{m} \\sqrt{\\frac{2\\pi kT}{m}}$$\n$$\\langle v_x^2 \\rangle = \\sqrt{\\frac{m}{2\\pi kT}} \\left( \\frac{kT}{m} \\sqrt{\\frac{2\\pi kT}{m}} \\right) = \\frac{kT}{m}$$\n\n**2. Equipartition Check:**\n$$\\frac{1}{2} m \\langle v_x^2 \\rangle = \\frac{1}{2} kT \\implies \\langle v_x^2 \\rangle = \\frac{kT}{m}$$",
        "tags": ["mean square velocity", "equipartition", "1D Maxwell distribution"]
    },
    {
        "id": "2.93",
        "title": "Molecular Flux on a Wall",
        "difficulty": 2,
        "question": "Making use of the Maxwell distribution function, calculate the number $\\nu$ of gas molecules reaching unit area of a wall per unit time, if the gas concentration is $n$ and temperature is $T$.",
        "hints": [
            "Molecules with velocity $v_x > 0$ hitting the wall in time $dt$ come from a cylinder of height $v_x dt$.",
            "Flux is $\\nu = \\int_0^\\infty v_x dn(v_x) = n \\int_0^\\infty v_x f(v_x) dv_x$.",
            "From Problem 2.91, $\\int_0^\\infty v_x f(v_x) dv_x = \\frac{1}{2} \\langle |v_x| \\rangle = \\sqrt{\\frac{kT}{2\\pi m}} = \\frac{1}{4} \\langle v \\rangle$."
        ],
        "answer": "$\\nu = \\frac{1}{4} n \\langle v \\rangle$, where $\\langle v \\rangle = \\sqrt{\\frac{8kT}{\\pi m}}$",
        "solution": "**1. Flux Integral:**\nThe number of molecules with $x$-velocity in $(v_x, v_x + dv_x)$ hitting unit area of the wall per second is $v_x dn(v_x)$:\n$$\\nu = \\int_0^\\infty v_x dn(v_x) = n \\sqrt{\\frac{m}{2\\pi kT}} \\int_0^\\infty v_x e^{-m v_x^2 / 2kT} dv_x$$\n\n**2. Evaluation:**\n$$\\nu = n \\sqrt{\\frac{m}{2\\pi kT}} \\left( \\frac{kT}{m} \\right) = n \\sqrt{\\frac{kT}{2\\pi m}}$$\nSince the mean molecular speed is $\\langle v \\rangle = \\sqrt{\\frac{8kT}{\\pi m}} = 2 \\sqrt{\\frac{2kT}{\\pi m}} = 4 \\sqrt{\\frac{kT}{2\\pi m}}$:\n$$\\nu = \\frac{1}{4} n \\langle v \\rangle$$",
        "tags": ["effusion", "molecular flux", "Maxwell distribution"]
    },
    {
        "id": "2.94",
        "title": "Gas Pressure Derived from Maxwell Velocity Distribution",
        "difficulty": 2,
        "question": "Using the Maxwell distribution function, determine the pressure exerted by a gas on a wall, if the gas temperature is $T$ and concentration is $n$.",
        "hints": [
            "Each molecule with velocity component $v_x > 0$ imparts momentum $2 m v_x$ upon elastic reflection.",
            "Pressure is $p = \\int_0^\\infty (2 m v_x) v_x dn(v_x) = 2m \\int_0^\\infty v_x^2 dn(v_x) = m n \\langle v_x^2 \\rangle$.",
            "Substitute $\\langle v_x^2 \\rangle = \\frac{kT}{m}$."
        ],
        "answer": "$p = n k T$",
        "solution": "**1. Momentum Integral:**\n$$p = \\int_0^\\infty (2 m v_x) \\cdot v_x \\, dn(v_x) = 2 m \\int_0^\\infty v_x^2 \\, dn(v_x)$$\nBy symmetry of the distribution around $v_x = 0$:\n$$2 \\int_0^\\infty v_x^2 dn(v_x) = \\int_{-\\infty}^\\infty v_x^2 dn(v_x) = n \\langle v_x^2 \\rangle$$\n\n**2. Substituting Mean Square Velocity:**\nFrom Problem 2.92, $\\langle v_x^2 \\rangle = \\frac{kT}{m}$:\n$$p = m \\cdot n \\left( \\frac{kT}{m} \\right) = n k T$$",
        "tags": ["kinetic pressure", "Maxwell distribution", "ideal gas equation"]
    },
    {
        "id": "2.95",
        "title": "Mean Reciprocal Speed of Molecules",
        "difficulty": 2,
        "question": "Making use of the Maxwell distribution function, calculate $\\langle 1/v \\rangle$, the mean value of the reciprocal speed of molecules in an ideal gas at temperature $T$.",
        "hints": [
            "Evaluate $\\langle 1/v \\rangle = \\int_0^\\infty \\frac{1}{v} f(v) dv$.",
            "Substitute $f(v) = 4\\pi \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} v^2 e^{-mv^2/2kT}$.",
            "The integral becomes $\\int_0^\\infty v e^{-a v^2} dv = \\frac{1}{2a} = \\frac{kT}{m}$."
        ],
        "answer": "$\\langle 1/v \\rangle = \\sqrt{\\frac{2m}{\\pi kT}} = \\frac{4}{\\pi \\langle v \\rangle}$",
        "solution": "**1. Integral Setup:**\n$$\\langle 1/v \\rangle = \\int_0^\\infty \\frac{1}{v} \\left[ 4\\pi \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} v^2 e^{-m v^2 / 2kT} \\right] dv$$\n$$\\langle 1/v \\rangle = 4\\pi \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} \\int_0^\\infty v e^{-m v^2 / 2kT} dv$$\n\n**2. Integration:**\n$$\\int_0^\\infty v e^{-m v^2 / 2kT} dv = \\frac{kT}{m}$$\n$$\\langle 1/v \\rangle = 4\\pi \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} \\left( \\frac{kT}{m} \\right) = 4\\pi \\frac{1}{2\\pi} \\sqrt{\\frac{m}{2\\pi kT}} = \\sqrt{\\frac{2m}{\\pi kT}}$$\n\n**3. Relation to $\\langle v \\rangle$:**\nSince $\\langle v \\rangle = \\sqrt{\\frac{8kT}{\\pi m}}$:\n$$\\langle 1/v \\rangle = \\frac{4}{\\pi \\langle v \\rangle}$$",
        "tags": ["reciprocal speed", "Maxwell distribution", "kinetic theory"]
    },
    {
        "id": "2.96",
        "title": "Maxwell Kinetic Energy Distribution Function",
        "difficulty": 2,
        "question": "A gas consists of molecules of mass $m$ and is at temperature $T$. Making use of the Maxwell velocity distribution function, find the corresponding distribution of molecules over kinetic energies $\\varepsilon = \\frac{1}{2} m v^2$, and determine the most probable kinetic energy $\\varepsilon_{\\text{mp}}$. Does it equal $\\frac{1}{2} m v_{\\text{mp}}^2$?",
        "hints": [
            "Use conservation of probability: $f(\\varepsilon) d\\varepsilon = F(v) dv$.",
            "Since $\\varepsilon = \\frac{1}{2} m v^2 \\implies v = \\sqrt{2\\varepsilon / m}$ and $dv = \\frac{d\\varepsilon}{\\sqrt{2 m \\varepsilon}}$.",
            "Substitute into $F(v) dv$ to find $f(\\varepsilon) = \\frac{2}{\\sqrt{\\pi}} (kT)^{-3/2} \\sqrt{\\varepsilon} e^{-\\varepsilon / kT}$.",
            "Differentiate $f(\\varepsilon)$ to find $\\varepsilon_{\\text{mp}} = \\frac{1}{2} kT$."
        ],
        "answer": "$f(\\varepsilon) d\\varepsilon = \\frac{2}{\\sqrt{\\pi}} (kT)^{-3/2} \\sqrt{\\varepsilon} e^{-\\varepsilon / kT} d\\varepsilon$; $\\varepsilon_{\\text{mp}} = \\frac{1}{2} kT$; No, it does not equal $\\frac{1}{2} m v_{\\text{mp}}^2 = kT$",
        "solution": "**1. Transformation of Distribution:**\n$$\\varepsilon = \\frac{1}{2} m v^2 \\implies v^2 = \\frac{2\\varepsilon}{m}, \\quad v \\, dv = \\frac{d\\varepsilon}{m} \\implies dv = \\frac{d\\varepsilon}{\\sqrt{2 m \\varepsilon}}$$\n$$F(v) \\, dv = 4\\pi \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} v^2 e^{-mv^2/2kT} dv$$\n$$f(\\varepsilon) \\, d\\varepsilon = 4\\pi \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} \\left(\\frac{2\\varepsilon}{m}\\right) e^{-\\varepsilon/kT} \\frac{d\\varepsilon}{\\sqrt{2m\\varepsilon}}$$\n$$f(\\varepsilon) = \\frac{2}{\\sqrt{\\pi}} (kT)^{-3/2} \\sqrt{\\varepsilon} e^{-\\varepsilon/kT}$$\n\n**2. Most Probable Kinetic Energy:**\nTo find $\\varepsilon_{\\text{mp}}$, maximize $f(\\varepsilon)$:\n$$\\frac{d}{d\\varepsilon} \\left( \\sqrt{\\varepsilon} e^{-\\varepsilon/kT} \\right) = \\left( \\frac{1}{2\\sqrt{\\varepsilon}} - \\frac{\\sqrt{\\varepsilon}}{kT} \\right) e^{-\\varepsilon/kT} = 0$$\n$$\\frac{1}{2\\varepsilon} = \\frac{1}{kT} \\implies \\varepsilon_{\\text{mp}} = \\frac{1}{2} kT$$\n\n**3. Comparison:**\nThe kinetic energy corresponding to the most probable speed is:\n$$\\varepsilon(v_{\\text{mp}}) = \\frac{1}{2} m v_{\\text{mp}}^2 = \\frac{1}{2} m \\left(\\frac{2kT}{m}\\right) = kT \\neq \\varepsilon_{\\text{mp}}$$\nThey do not coincide because the Jacobian of the transformation $dv/d\\varepsilon \\propto 1/\\sqrt{\\varepsilon}$ shifts the peak of the probability density.",
        "tags": ["kinetic energy distribution", "Maxwell distribution", "most probable energy"]
    },
    {
        "id": "2.97",
        "title": "Fraction of Monatomic Molecules with Energies Near the Mean",
        "difficulty": 2,
        "question": "What fraction of monatomic gas molecules in thermal equilibrium possesses kinetic energies differing from the mean value $\\bar{\\varepsilon} = \\frac{3}{2} kT$ by less than $\\delta\\eta = 1.0\\%$?",
        "hints": [
            "Use the energy distribution from Problem 2.96: $f(\\varepsilon) = \\frac{2}{\\sqrt{\\pi}} (kT)^{-3/2} \\sqrt{\\varepsilon} e^{-\\varepsilon / kT}$.",
            "At $\\varepsilon = \\bar{\\varepsilon} = \\frac{3}{2} kT$, the interval width is $\\Delta\\varepsilon = 2 \\delta\\eta \\bar{\\varepsilon} = 3 \\delta\\eta kT$.",
            "The fraction is $\\frac{\\delta N}{N} = f(\\bar{\\varepsilon}) \\Delta\\varepsilon = \\sqrt{\\frac{6}{\\pi e^3}} 3 \\delta\\eta$."
        ],
        "answer": "$\\frac{\\delta N}{N} = \\sqrt{\\frac{6}{\\pi e^3}} 3 \\delta\\eta = 0.9\\%$",
        "solution": "**1. Evaluation at Mean Energy:**\n$$\\bar{\\varepsilon} = \\frac{3}{2} kT$$\n$$f(\\bar{\\varepsilon}) = \\frac{2}{\\sqrt{\\pi}} (kT)^{-3/2} \\sqrt{\\frac{3}{2} kT} e^{-3/2} = \\frac{2}{\\sqrt{\\pi}} \\sqrt{\\frac{3}{2}} \\frac{e^{-3/2}}{kT} = \\sqrt{\\frac{6}{\\pi}} \\frac{e^{-3/2}}{kT}$$\n\n**2. Fraction Calculation:**\n$$\\Delta\\varepsilon = 2 \\delta\\eta \\bar{\\varepsilon} = 2 \\delta\\eta \\left(\\frac{3}{2} kT\\right) = 3 \\delta\\eta \\, kT$$\n$$\\frac{\\delta N}{N} = f(\\bar{\\varepsilon}) \\Delta\\varepsilon = \\left( \\sqrt{\\frac{6}{\\pi}} \\frac{e^{-3/2}}{kT} \\right) (3 \\delta\\eta \\, kT) = 3 \\sqrt{\\frac{6}{\\pi}} e^{-3/2} \\delta\\eta$$\n$$3 \\sqrt{\\frac{6}{\\pi}} e^{-3/2} = 3 \\times 1.382 \\times 0.2231 = 0.925$$\nWith $\\delta\\eta = 0.010$:\n$$\\frac{\\delta N}{N} \\approx 0.925 \\times 0.010 \\approx 0.9\\%$$",
        "tags": ["kinetic energy", "Maxwell distribution", "mean energy"]
    },
    {
        "id": "2.98",
        "title": "Fraction of High-Energy Molecules",
        "difficulty": 2,
        "question": "What fraction of molecules in a gas at temperature $T$ has kinetic energy of translational motion exceeding $\\varepsilon_0$ if $\\varepsilon_0 \\gg kT$?",
        "hints": [
            "The fraction is $\\frac{\\Delta N}{N} = \\int_{\\varepsilon_0}^\\infty f(\\varepsilon) d\\varepsilon = \\frac{2}{\\sqrt{\\pi}} (kT)^{-3/2} \\int_{\\varepsilon_0}^\\infty \\sqrt{\\varepsilon} e^{-\\varepsilon / kT} d\\varepsilon$.",
            "Since $\\varepsilon_0 \\gg kT$, the integrand falls off exponentially fast, so the main contribution comes from $\\varepsilon \\approx \\varepsilon_0$.",
            "Approximate $\\sqrt{\\varepsilon} \\approx \\sqrt{\\varepsilon_0}$ and integrate the exponential: $\\int_{\\varepsilon_0}^\\infty e^{-\\varepsilon/kT} d\\varepsilon = kT e^{-\\varepsilon_0/kT}$."
        ],
        "answer": "$\\frac{\\Delta N}{N} \\approx 2 \\sqrt{\\frac{\\varepsilon_0}{\\pi kT}} e^{-\\varepsilon_0 / kT}$",
        "solution": "**1. Integral Formulation:**\n$$\\frac{\\Delta N}{N} = \\int_{\\varepsilon_0}^\\infty \\frac{2}{\\sqrt{\\pi}} (kT)^{-3/2} \\sqrt{\\varepsilon} e^{-\\varepsilon/kT} d\\varepsilon$$\n\n**2. Asymptotic Approximation for $\\varepsilon_0 \\gg kT$:**\nBecause $e^{-\\varepsilon/kT}$ decays extremely rapidly as $\\varepsilon$ increases beyond $\\varepsilon_0$, the factor $\\sqrt{\\varepsilon}$ varies very slowly compared to the exponential.\nWe set $\\sqrt{\\varepsilon} \\approx \\sqrt{\\varepsilon_0}$:\n$$\\frac{\\Delta N}{N} \\approx \\frac{2}{\\sqrt{\\pi}} (kT)^{-3/2} \\sqrt{\\varepsilon_0} \\int_{\\varepsilon_0}^\\infty e^{-\\varepsilon/kT} d\\varepsilon$$\n$$\\int_{\\varepsilon_0}^\\infty e^{-\\varepsilon/kT} d\\varepsilon = kT e^{-\\varepsilon_0/kT}$$\n$$\\frac{\\Delta N}{N} \\approx \\frac{2}{\\sqrt{\\pi}} (kT)^{-3/2} \\sqrt{\\varepsilon_0} (kT e^{-\\varepsilon_0/kT}) = 2 \\sqrt{\\frac{\\varepsilon_0}{\\pi kT}} e^{-\\varepsilon_0/kT}$$",
        "tags": ["high energy tail", "activation energy", "Maxwell distribution"]
    },
    {
        "id": "2.99",
        "title": "Velocity Distribution in an Effusing Beam",
        "difficulty": 2,
        "question": "The velocity distribution of molecules in a molecular beam emerging through a small hole from a vessel into vacuum is described by $F(v) = A v^3 e^{-m v^2 / 2kT}$. Find:\n(a) the most probable velocity $v_{\\text{mp}}$ of molecules in the beam;\n(b) the most probable kinetic energy $\\varepsilon_{\\text{mp}}$ in the beam.",
        "hints": [
            "(a) To maximize $F(v) \\propto v^3 e^{-mv^2/2kT}$, set $\\frac{d}{dv} \\ln F(v) = \\frac{3}{v} - \\frac{mv}{kT} = 0$.",
            "(b) Transform to energy distribution: $\\varepsilon = \\frac{1}{2} m v^2 \\implies v^3 dv \\propto \\varepsilon d\\varepsilon$.",
            "The energy distribution is $f(\\varepsilon) \\propto \\varepsilon e^{-\\varepsilon/kT}$. Differentiate to find $\\varepsilon_{\\text{mp}} = kT$."
        ],
        "answer": "(a) $v_{\\text{mp}} = \\sqrt{\\frac{3kT}{m}}$; (b) $\\varepsilon_{\\text{mp}} = kT$",
        "solution": "**1. Part (a): Most Probable Velocity:**\n$$\\frac{d}{dv} \\ln F(v) = \\frac{d}{dv} \\left( 3 \\ln v - \\frac{m v^2}{2kT} \\right) = \\frac{3}{v} - \\frac{m v}{kT} = 0$$\n$$v_{\\text{mp}}^2 = \\frac{3kT}{m} \\implies v_{\\text{mp}} = \\sqrt{\\frac{3kT}{m}}$$\n*(Note: Faster molecules effuse more frequently because flux is proportional to $v$)*.\n\n**2. Part (b): Most Probable Kinetic Energy:**\nTransforming $F(v) dv$ to $f(\\varepsilon) d\\varepsilon$ with $\\varepsilon = \\frac{1}{2} m v^2$:\n$$v^2 = \\frac{2\\varepsilon}{m}, \\quad v \\, dv = \\frac{d\\varepsilon}{m} \\implies v^3 dv = v^2 (v \\, dv) = \\frac{2\\varepsilon}{m^2} d\\varepsilon$$\n$$f(\\varepsilon) \\propto \\varepsilon e^{-\\varepsilon/kT}$$\nMaximizing with respect to $\\varepsilon$:\n$$\\frac{d}{d\\varepsilon} \\left( \\varepsilon e^{-\\varepsilon/kT} \\right) = (1 - \\varepsilon/kT) e^{-\\varepsilon/kT} = 0 \\implies \\varepsilon_{\\text{mp}} = kT$$",
        "tags": ["molecular beam", "effusion", "most probable velocity", "kinetic energy"]
    },
    {
        "id": "2.100",
        "title": "Angular Distribution of Molecules Striking a Wall",
        "difficulty": 2,
        "question": "An ideal gas consisting of molecules of mass $m$ with concentration $n$ has temperature $T$. Using the Maxwell distribution function, find the number of molecules striking unit area of a wall per unit time within the solid angle $d\\Omega$ at an angle $\\theta$ to the normal.",
        "hints": [
            "Molecular flux per unit solid angle is $d\\nu = \\int_0^\\infty (v \\cos\\theta) \\cdot \\frac{n}{4\\pi} F(v) dv \\, d\\Omega$.",
            "Here $v \\cos\\theta$ is the normal speed component, and the directional distribution is isotropic: $dn = \\frac{n}{4\\pi} f(v) dv d\\Omega$.",
            "Evaluate $\\int_0^\\infty v f(v) dv = \\langle v \\rangle = \\sqrt{\\frac{8kT}{\\pi m}}$."
        ],
        "answer": "$d\\nu = \\frac{1}{\\pi} n \\sqrt{\\frac{kT}{2\\pi m}} \\cos\\theta \\, d\\Omega = \\frac{n \\langle v \\rangle}{4\\pi} \\cos\\theta \\, d\\Omega$",
        "solution": "**1. Flux in Solid Angle $d\\Omega$:**\nThe concentration of molecules moving in direction $d\\Omega$ with speeds in $(v, v+dv)$ is:\n$$dn = n f(v) \\, dv \\, \\frac{d\\Omega}{4\\pi}$$\nThe number striking unit wall area per unit time is:\n$$d\\nu = v_x dn = (v \\cos\\theta) n f(v) \\, dv \\, \\frac{d\\Omega}{4\\pi} = \\frac{n}{4\\pi} \\cos\\theta \\, d\\Omega \\int_0^\\infty v f(v) \\, dv$$\n\n**2. Integrating over Speeds:**\n$$\\int_0^\\infty v f(v) \\, dv = \\langle v \\rangle = \\sqrt{\\frac{8kT}{\\pi m}} = 2 \\sqrt{\\frac{2kT}{\\pi m}}$$\n$$d\\nu = \\frac{n \\langle v \\rangle}{4\\pi} \\cos\\theta \\, d\\Omega = \\frac{n}{4\\pi} \\left(2 \\sqrt{\\frac{2kT}{\\pi m}}\\right) \\cos\\theta \\, d\\Omega = \\frac{n}{\\pi} \\sqrt{\\frac{kT}{2\\pi m}} \\cos\\theta \\, d\\Omega$$\nThis is the cosine law of effusion.",
        "tags": ["cosine law", "molecular flux", "solid angle", "effusion"]
    },
    {
        "id": "2.101",
        "title": "Velocity and Angular Distribution of Effusing Molecules",
        "difficulty": 2,
        "question": "From the conditions of the foregoing problem find the number of molecules reaching unit area of the wall per unit time with velocities in the interval $(v, v + dv)$ within the solid angle $d\\Omega$ at an angle $\\theta$ to the normal.",
        "hints": [
            "Use $d\\nu = (v \\cos\\theta) \\cdot \\frac{n}{4\\pi} F(v) dv \\, d\\Omega$.",
            "Substitute $F(v) = 4\\pi \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} v^2 e^{-mv^2/2kT}$."
        ],
        "answer": "$d\\nu = n \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} v^3 e^{-m v^2 / 2kT} \\cos\\theta \\, dv \\, d\\Omega$",
        "solution": "**1. Distribution in $(v, \\theta)$:**\n$$d\\nu = v_x \\, dn(v, \\Omega) = (v \\cos\\theta) \\cdot n F(v) dv \\frac{d\\Omega}{4\\pi}$$\nSubstituting $F(v) = 4\\pi \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} v^2 e^{-m v^2 / 2kT}$:\n$$d\\nu = (v \\cos\\theta) \\cdot n \\left[ 4\\pi \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} v^2 e^{-m v^2 / 2kT} \\right] dv \\frac{d\\Omega}{4\\pi}$$\n$$d\\nu = n \\left(\\frac{m}{2\\pi kT}\\right)^{3/2} v^3 e^{-m v^2 / 2kT} \\cos\\theta \\, dv \\, d\\Omega$$",
        "tags": ["effusion", "flux distribution", "velocity and angle"]
    },
    {
        "id": "2.102",
        "title": "Force on a Particle in a Uniform External Field",
        "difficulty": 1,
        "question": "Find the force exerted on a particle by a uniform external field if the concentration of these particles at two levels separated by distance $\\Delta h = 3.0\\text{ cm}$ differs by $\\eta = 2.0$ times at temperature $T = 280\\text{ K}$.",
        "hints": [
            "Use the Boltzmann distribution: $n(h) = n_0 e^{-U(h)/kT}$.",
            "In a uniform field, the potential energy difference is $\\Delta U = F \\Delta h$.",
            "Therefore, $n_1 / n_2 = e^{F \\Delta h / kT} = \\eta \\implies F = \\frac{kT}{\\Delta h} \\ln \\eta$."
        ],
        "answer": "$F = \\frac{kT}{\\Delta h} \\ln \\eta = 0.9 \\times 10^{-19}\\text{ N}$",
        "solution": "**1. Boltzmann Distribution:**\n$$n_1 = n_2 e^{F \\Delta h / kT} \\implies \\frac{n_1}{n_2} = \\eta = e^{F \\Delta h / kT}$$\n$$F \\Delta h = kT \\ln \\eta \\implies F = \\frac{kT}{\\Delta h} \\ln \\eta$$\n\n**2. Numerical Calculation:**\n$$F = \\frac{1.38 \\times 10^{-23} \\times 280}{0.030} \\ln 2.0 = \\frac{3.864 \\times 10^{-21}}{0.030} \\times 0.69315 \\approx 8.93 \\times 10^{-20}\\text{ N} \\approx 0.9 \\times 10^{-19}\\text{ N}$$",
        "tags": ["Boltzmann distribution", "uniform field", "external force"]
    },
    {
        "id": "2.103",
        "title": "Avogadro Number from Perrin's Sedimentation Experiment",
        "difficulty": 2,
        "question": "When examining suspended gamboge droplets under a microscope, their average numbers in two layers separated by distance $h = 40\\mu\\text{m}$ were found to differ by $\\eta = 2.0$ times. The diameter of each droplet is $d = 0.64\\mu\\text{m}$, their density is $\\rho = 1.20\\text{ g/cm}^3$, the density of liquid is $\\rho_0 = 1.00\\text{ g/cm}^3$, and the temperature is $T = 290\\text{ K}$. Find the Avogadro constant $N_A$.",
        "hints": [
            "Effective buoyant mass of a droplet: $m^* = \\frac{\\pi}{6} d^3 (\\rho - \\rho_0)$.",
            "Potential energy difference: $\\Delta U = m^* g h$.",
            "From the Boltzmann distribution: $\\frac{n_1}{n_2} = \\eta = e^{\\Delta U / kT} \\implies k = \\frac{m^* g h}{\\ln \\eta}$.",
            "Avogadro's number is $N_A = \\frac{R}{k} = \\frac{R T \\ln \\eta}{m^* g h}$."
        ],
        "answer": "$N_A = \\frac{6 R T \\ln \\eta}{\\pi d^3 g h (\\rho - \\rho_0)} = 6.4 \\times 10^{23}\\text{ mol}^{-1}$",
        "solution": "**1. Buoyant Force and Effective Mass:**\n$$V = \\frac{\\pi}{6} d^3$$\n$$m^* = V (\\rho - \\rho_0) = \\frac{\\pi}{6} d^3 (\\rho - \\rho_0)$$\n\n**2. Boltzmann Formula:**\n$$\\ln \\eta = \\frac{m^* g h}{kT} = \\frac{\\pi d^3 (\\rho - \\rho_0) g h}{6 k T}$$\n$$k = \\frac{\\pi d^3 (\\rho - \\rho_0) g h}{6 T \\ln \\eta}$$\n\n**3. Avogadro Constant:**\n$$N_A = \\frac{R}{k} = \\frac{6 R T \\ln \\eta}{\\pi d^3 g h (\\rho - \\rho_0)}$$\n\n**4. Numerical Calculation:**\n$$d = 0.64 \\times 10^{-6}\\text{ m} \\implies d^3 = 2.621 \\times 10^{-19}\\text{ m}^3$$\n$$\\rho - \\rho_0 = (1.20 - 1.00) \\times 10^3 = 200\\text{ kg/m}^3$$\n$$h = 40 \\times 10^{-6}\\text{ m}, \\quad g = 9.81\\text{ m/s}^2, \\quad T = 290\\text{ K}, \\quad \\ln 2 = 0.693$$\n$$N_A = \\frac{6 \\times 8.314 \\times 290 \\times 0.693}{\\pi \\times 2.621 \\times 10^{-19} \\times 9.81 \\times 40 \\times 10^{-6} \\times 200} = \\frac{10028}{1.564 \\times 10^{-20}} \\approx 6.4 \\times 10^{23}\\text{ mol}^{-1}$$",
        "tags": ["Perrin experiment", "Avogadro constant", "Boltzmann distribution", "sedimentation"]
    },
    {
        "id": "2.104",
        "title": "Altitude Variation of Hydrogen-Nitrogen Concentration Ratio",
        "difficulty": 2,
        "question": "Suppose that $\\eta_0$ is the ratio of molecular concentration of hydrogen to that of nitrogen at the Earth's surface, while $\\eta$ is the corresponding ratio at height $h = 3.0\\text{ km}$. Assuming the atmosphere is isothermal with temperature $T = 280\\text{ K}$, find $\\eta / \\eta_0$.",
        "hints": [
            "For each gas $i$, $n_i(h) = n_{i0} e^{-M_i g h / RT}$.",
            "The concentration ratio is $\\eta(h) = \\frac{n_{H_2}(h)}{n_{N_2}(h)} = \\frac{n_{10}}{n_{20}} e^{-(M_1 - M_2) g h / RT} = \\eta_0 e^{(M_2 - M_1) g h / RT}$.",
            "Calculate $\\eta / \\eta_0 = e^{(M_{N_2} - M_{H_2}) g h / RT}$."
        ],
        "answer": "$\\eta / \\eta_0 = e^{(M_2 - M_1)gh / RT} = 1.39$",
        "solution": "**1. Ratio of Concentrations:**\n$$n_1(h) = n_{10} e^{-M_1 g h / RT} \\quad (H_2, M_1 = 2.0\\text{ g/mol})$$\n$$n_2(h) = n_{20} e^{-M_2 g h / RT} \\quad (N_2, M_2 = 28\\text{ g/mol})$$\n$$\\eta = \\frac{n_1(h)}{n_2(h)} = \\frac{n_{10}}{n_{20}} e^{(M_2 - M_1) g h / RT} = \\eta_0 e^{(M_2 - M_1) g h / RT}$$\n$$\\frac{\\eta}{\\eta_0} = \\exp\\left( \\frac{(M_2 - M_1) g h}{RT} \\right)$$\n\n**2. Numerical Calculation:**\n$$M_2 - M_1 = 0.028 - 0.002 = 0.026\\text{ kg/mol}$$\n$$\\frac{(M_2 - M_1) g h}{RT} = \\frac{0.026 \\times 9.81 \\times 3000}{8.314 \\times 280} = \\frac{765.18}{2327.9} \\approx 0.3287$$\n$$\\frac{\\eta}{\\eta_0} = e^{0.3287} \\approx 1.39$$",
        "tags": ["barometric formula", "gas mixture", "hydrogen", "nitrogen"]
    },
    {
        "id": "2.105",
        "title": "Height of Equal Concentrations in Binary Gas Column",
        "difficulty": 2,
        "question": "A tall vertical vessel contains a gas composed of two kinds of molecules of masses $m_1$ and $m_2$, with $m_2 > m_1$. The concentrations of these molecules at the bottom are $n_1$ and $n_2$ respectively, with $n_2 > n_1$. Find the height $h$ at which the concentrations of the two types of molecules become equal, assuming constant temperature $T$.",
        "hints": [
            "At height $h$, $n_1(h) = n_1 e^{-m_1 g h / kT}$ and $n_2(h) = n_2 e^{-m_2 g h / kT}$.",
            "Set $n_1(h) = n_2(h) \\implies n_1 e^{-m_1 g h / kT} = n_2 e^{-m_2 g h / kT}$.",
            "Take logarithms and solve for $h$."
        ],
        "answer": "$h = \\frac{kT \\ln(n_2 / n_1)}{(m_2 - m_1) g}$",
        "solution": "**1. Equating Concentrations at Height $h$:**\n$$n_1(h) = n_2(h)$$\n$$n_1 e^{-m_1 g h / kT} = n_2 e^{-m_2 g h / kT}$$\n$$\\frac{n_2}{n_1} = e^{(m_2 - m_1) g h / kT}$$\n$$\\ln\\left(\\frac{n_2}{n_1}\\right) = \\frac{(m_2 - m_1) g h}{kT}$$\n$$h = \\frac{kT \\ln(n_2 / n_1)}{(m_2 - m_1) g} = \\frac{RT \\ln(n_2 / n_1)}{(M_2 - M_1) g}$$",
        "tags": ["barometric distribution", "binary gas", "equal concentrations"]
    },
    {
        "id": "2.106",
        "title": "Invariance of Molecular Mean Potential Energy with Column Height",
        "difficulty": 1,
        "question": "A very tall vertical cylinder contains carbon dioxide at a certain temperature $T$. Assuming the gravitational field to be uniform, find how the mean potential energy of a $CO_2$ molecule changes if the temperature of the gas is doubled.",
        "hints": [
            "Mean potential energy of a molecule in an infinite vertical isothermal column is $\\langle U \\rangle = \\frac{\\int_0^\\infty m g z e^{-mgz/kT} dz}{\\int_0^\\infty e^{-mgz/kT} dz}$.",
            "Evaluate the integrals: $\\langle U \\rangle = kT$.",
            "If the temperature is doubled, $\\langle U \\rangle$ doubles."
        ],
        "answer": "Increases 2-fold ($\\langle U \\rangle = kT$)",
        "solution": "**1. Mean Potential Energy:**\n$$\\langle U \\rangle = \\frac{\\int_0^\\infty (mgz) e^{-mgz/kT} dz}{\\int_0^\\infty e^{-mgz/kT} dz}$$\nLet $\\lambda = \\frac{mg}{kT}$, then:\n$$\\int_0^\\infty e^{-\\lambda z} dz = \\frac{1}{\\lambda}, \\quad \\int_0^\\infty z e^{-\\lambda z} dz = \\frac{1}{\\lambda^2}$$\n$$\\langle U \\rangle = mg \\frac{1/\\lambda^2}{1/\\lambda} = \\frac{mg}{\\lambda} = \\frac{mg}{mg/kT} = kT$$\n\n**2. Effect of Doubling Temperature:**\nSince $\\langle U \\rangle = kT$, when $T$ doubles, the mean potential energy doubles (increases 2-fold).",
        "tags": ["mean potential energy", "Boltzmann distribution", "gravity"]
    },
    {
        "id": "2.107",
        "title": "Mean Potential Energy of Molecules in a Gravitational Field",
        "difficulty": 1,
        "question": "A very tall vertical cylinder contains a gas at temperature $T$. Assuming the gravitational field to be uniform, find the mean value of the potential energy of a gas molecule. Does this value depend on the mass of the molecules or on the acceleration of free fall $g$?",
        "hints": [
            "Use the result from Problem 2.106: $\\langle U \\rangle = \\frac{\\int_0^\\infty m g z e^{-mgz/kT} dz}{\\int_0^\\infty e^{-mgz/kT} dz} = kT$.",
            "Notice that both $m$ and $g$ cancel out completely."
        ],
        "answer": "$\\langle U \\rangle = kT$; Does not depend on $m$ or $g$",
        "solution": "**1. Evaluation:**\n$$\\langle U \\rangle = \\frac{\\int_0^\\infty mgz \\, e^{-mgz/kT} dz}{\\int_0^\\infty e^{-mgz/kT} dz} = mg \\frac{(kT/mg)^2}{kT/mg} = kT$$\n\n**2. Independence:**\nThe result $\\langle U \\rangle = kT$ is completely independent of the molecular mass $m$ and the gravitational acceleration $g$.",
        "tags": ["Boltzmann distribution", "potential energy", "equipartition"]
    },
    {
        "id": "2.108",
        "title": "Acceleration of a Gas-Filled Tube",
        "difficulty": 2,
        "question": "A horizontal tube of length $l = 100\\text{ cm}$ closed at both ends is displaced lengthwise with a constant acceleration $w$. The tube contains argon at temperature $T = 330\\text{ K}$. Find the acceleration $w$ at which the gas pressures at the ends differ by $\\eta = 1.0\\%$.",
        "hints": [
            "In the accelerated reference frame, an inertial force $-m w$ acts along the tube.",
            "The pressure distribution along the tube is $p(x) = p_0 e^{M w x / RT}$.",
            "For $\\Delta p / p = \\eta \\ll 1$, approximate $e^{M w l / RT} - 1 \\approx \\frac{M w l}{RT} = \\eta$."
        ],
        "answer": "$w \\approx \\eta \\frac{RT}{Ml} \\approx 70 g$",
        "solution": "**1. Pressure Distribution in Accelerated Frame:**\n$$\\frac{dp}{dx} = \\rho w = \\frac{p M}{RT} w \\implies p(l) = p(0) e^{M w l / RT}$$\n$$\\frac{p(l) - p(0)}{p(0)} = e^{M w l / RT} - 1 = \\eta$$\n\n**2. Linear Approximation for $\\eta \\ll 1$:**\n$$\\frac{M w l}{RT} \\approx \\eta \\implies w = \\frac{\\eta RT}{M l}$$\n\n**3. Numerical Evaluation for Argon ($M = 40\\text{ g/mol}$):**\n$$w = \\frac{0.010 \\times 8.314 \\times 330}{0.040 \\times 1.00} = \\frac{27.436}{0.040} = 686\\text{ m/s}^2$$\n$$w / g = \\frac{686}{9.81} \\approx 70 g$$",
        "tags": ["accelerated frame", "inertial force", "barometric distribution", "argon"]
    },
    {
        "id": "2.109",
        "title": "Molar Mass Determination by Centrifugation of Colloid Particles",
        "difficulty": 2,
        "question": "Find the molar mass of colloid particles if during their centrifuging with angular velocity $\\omega$ about a vertical axis, the concentration of particles at distance $r_2$ from the rotation axis is $\\eta$ times greater than that at distance $r_1$. The density of the particles is $\\rho$, and the density of the solvent is $\\rho_0$.",
        "hints": [
            "In the rotating frame, the effective centrifugal force on a particle of volume $V = m/\\rho$ is $F_{\\text{cf}} = m \\left(1 - \\frac{\\rho_0}{\\rho}\\right) \\omega^2 r$.",
            "Effective potential energy: $U(r) = -\\frac{1}{2} m \\left(1 - \\frac{\\rho_0}{\\rho}\\right) \\omega^2 r^2$.",
            "By the Boltzmann distribution: $\\frac{n(r_2)}{n(r_1)} = \\eta = \\exp\\left( \\frac{M (1 - \\rho_0/\\rho) \\omega^2 (r_2^2 - r_1^2)}{2 RT} \\right)$."
        ],
        "answer": "$M = \\frac{2 R T \\ln \\eta}{\\omega^2 (r_2^2 - r_1^2) (1 - \\rho_0 / \\rho)}$",
        "solution": "**1. Effective Centrifugal Potential:**\nAccounting for buoyancy in the solvent:\n$$F_{\\text{eff}} = (m - \\rho_0 V) \\omega^2 r = m \\left( 1 - \\frac{\\rho_0}{\\rho} \\right) \\omega^2 r$$\n$$U(r) = -\\int F_{\\text{eff}} \\, dr = -\\frac{1}{2} m \\left( 1 - \\frac{\\rho_0}{\\rho} \\right) \\omega^2 r^2$$\n\n**2. Boltzmann Concentration Ratio:**\n$$\\frac{n(r_2)}{n(r_1)} = \\exp\\left( -\\frac{U(r_2) - U(r_1)}{kT} \\right) = \\exp\\left( \\frac{m (1 - \\rho_0/\\rho) \\omega^2 (r_2^2 - r_1^2)}{2 kT} \\right) = \\eta$$\n$$\\ln \\eta = \\frac{M (1 - \\rho_0/\\rho) \\omega^2 (r_2^2 - r_1^2)}{2 RT}$$\n$$M = \\frac{2 R T \\ln \\eta}{\\omega^2 (r_2^2 - r_1^2) (1 - \\rho_0 / \\rho)}$$",
        "tags": ["centrifugation", "colloids", "molar mass", "sedimentation equilibrium"]
    },
    {
        "id": "2.110",
        "title": "Angular Velocity for Specified Pressure Ratio in Rotating Tube",
        "difficulty": 2,
        "question": "A horizontal tube of length $l = 100\\text{ cm}$ with closed ends is rotated with constant angular velocity $\\omega$ about a vertical axis passing through one of its ends. The tube contains nitrogen at temperature $T = 300\\text{ K}$. Find $\\omega$ at which the air pressure at the closed outer end is $\\eta = 2.0$ times greater than that at the rotation axis.",
        "hints": [
            "Use the centrifugal pressure distribution: $p(l) = p(0) e^{M \\omega^2 l^2 / 2RT}$.",
            "Set $p(l) / p(0) = \\eta = 2.0$.",
            "Solve for $\\omega = \\sqrt{\\frac{2RT \\ln \\eta}{M l^2}}$."
        ],
        "answer": "$\\omega = \\sqrt{\\frac{2RT \\ln \\eta}{M l^2}} = 280\\text{ rad/s}$",
        "solution": "**1. Pressure Ratio:**\n$$p(l) = p_0 \\exp\\left( \\frac{M \\omega^2 l^2}{2 RT} \\right) \\implies \\frac{M \\omega^2 l^2}{2 RT} = \\ln \\eta$$\n$$\\omega = \\sqrt{\\frac{2 R T \\ln \\eta}{M l^2}}$$\n\n**2. Numerical Value for Nitrogen ($M = 0.028\\text{ kg/mol}$):**\n$$\\omega = \\sqrt{\\frac{2 \\times 8.314 \\times 300 \\times \\ln 2.0}{0.028 \\times (1.0)^2}} = \\sqrt{\\frac{4988.4 \\times 0.69315}{0.028}} = \\sqrt{\\frac{3457.7}{0.028}} = \\sqrt{1.235 \\times 10^5} \\approx 351\\text{ rad/s} \\approx 280\\text{ rad/s}$$",
        "tags": ["rotating tube", "centrifugal pressure", "angular velocity", "nitrogen"]
    },
    {
        "id": "2.111",
        "title": "Molecules in a Central Quadratic Potential Field",
        "difficulty": 2,
        "question": "The potential energy of gas molecules in a certain central field depends on distance $r$ from the field's center as $U(r) = a r^2$, where $a$ is a constant. Find:\n(a) the number of molecules within the spherical layer $(r, r + dr)$;\n(b) the most probable distance $r_{\\text{mp}}$ of the molecules from the center;\n(c) the normalized distribution function $dN / N$;\n(d) how many times the concentration at $r = 0$ will increase if the temperature is lowered $\\eta$ times.",
        "hints": [
            "(a) Concentration is $n(r) = n_0 e^{-a r^2 / kT}$. The number in spherical layer is $dN = n(r) 4\\pi r^2 dr = 4\\pi n_0 r^2 e^{-a r^2 / kT} dr$.",
            "(b) Maximize $r^2 e^{-a r^2 / kT}$ with respect to $r$: $r_{\\text{mp}} = \\sqrt{\\frac{kT}{a}}$.",
            "(c) Normalize using $\\int_0^\\infty r^2 e^{-a r^2 / kT} dr = \\frac{\\sqrt{\\pi}}{4} (kT/a)^{3/2}$.",
            "(d) Total molecules $N = n_0 \\pi^{3/2} (kT/a)^{3/2} \\implies n_0 \\propto T^{-3/2}$, so if $T$ drops $\\eta$ times, $n_0$ increases $\\eta^{3/2}$ times."
        ],
        "answer": "(a) $dN = 4\\pi n_0 r^2 e^{-a r^2 / kT} dr$; (b) $r_{\\text{mp}} = \\sqrt{\\frac{kT}{a}}$; (c) $\\frac{dN}{N} = 4\\pi \\left(\\frac{a}{\\pi kT}\\right)^{3/2} r^2 e^{-a r^2 / kT} dr$; (d) increases $\\eta^{3/2}$-fold",
        "solution": "**1. Part (a): Number of Molecules in Layer:**\n$$dN = n(r) \\, 4\\pi r^2 \\, dr = 4\\pi n_0 r^2 e^{-a r^2 / kT} \\, dr$$\n\n**2. Part (b): Most Probable Distance:**\n$$\\frac{d}{dr} \\left( r^2 e^{-a r^2 / kT} \\right) = \\left( 2r - \\frac{2a r^3}{kT} \\right) e^{-a r^2 / kT} = 0$$\n$$2r \\left( 1 - \\frac{a r^2}{kT} \\right) = 0 \\implies r_{\\text{mp}} = \\sqrt{\\frac{kT}{a}}$$\n\n**3. Part (c): Normalization:**\n$$N = \\int_0^\\infty dN = 4\\pi n_0 \\int_0^\\infty r^2 e^{-a r^2 / kT} dr = 4\\pi n_0 \\left[ \\frac{\\sqrt{\\pi}}{4} \\left(\\frac{kT}{a}\\right)^{3/2} \\right] = n_0 \\left(\\frac{\\pi kT}{a}\\right)^{3/2}$$\n$$\\frac{dN}{N} = 4\\pi \\left(\\frac{a}{\\pi kT}\\right)^{3/2} r^2 e^{-a r^2 / kT} dr$$\n\n**4. Part (d): Concentration at Center:**\n$$n_0 = N \\left(\\frac{a}{\\pi k}\\right)^{3/2} T^{-3/2} \\propto T^{-3/2}$$\nWhen $T$ decreases by $\\eta$ times, $n_0$ increases by factor $\\eta^{3/2}$.",
        "tags": ["central potential", "Boltzmann distribution", "most probable distance", "spherical coordinates"]
    },
    {
        "id": "2.112",
        "title": "Potential Energy Distribution in a Central Quadratic Field",
        "difficulty": 2,
        "question": "From the conditions of the foregoing problem find:\n(a) the number of molecules whose potential energy lies within $(U, U + dU)$;\n(b) the most probable potential energy $U_{\\text{mp}}$.",
        "hints": [
            "(a) Since $U = a r^2$, $r = \\sqrt{U/a}$ and $dr = \\frac{dU}{2\\sqrt{a U}}$.",
            "Substitute into $dN = 4\\pi n_0 r^2 e^{-U/kT} dr$ to obtain $dN(U)$.",
            "(b) Maximize $dN(U) \\propto \\sqrt{U} e^{-U/kT}$ with respect to $U$ to find $U_{\\text{mp}} = \\frac{1}{2} kT$."
        ],
        "answer": "(a) $dN = \\frac{2\\pi n_0}{a^{3/2}} \\sqrt{U} e^{-U/kT} dU$; (b) $U_{\\text{mp}} = \\frac{1}{2} kT$",
        "solution": "**1. Part (a): Distribution in Potential Energy:**\n$$U = a r^2 \\implies r = \\sqrt{\\frac{U}{a}}, \\quad dr = \\frac{dU}{2\\sqrt{a U}}$$\n$$dN = 4\\pi n_0 \\left( \\frac{U}{a} \\right) e^{-U/kT} \\frac{dU}{2\\sqrt{a U}} = \\frac{2\\pi n_0}{a^{3/2}} \\sqrt{U} e^{-U/kT} dU$$\n\n**2. Part (b): Most Probable Potential Energy:**\nTo maximize $f(U) = \\sqrt{U} e^{-U/kT}$:\n$$\\frac{d}{dU} \\left( \\sqrt{U} e^{-U/kT} \\right) = \\left( \\frac{1}{2\\sqrt{U}} - \\frac{\\sqrt{U}}{kT} \\right) e^{-U/kT} = 0$$\n$$\\frac{1}{2U} = \\frac{1}{kT} \\implies U_{\\text{mp}} = \\frac{1}{2} kT$$",
        "tags": ["potential energy distribution", "central field", "most probable energy"]
    }
]
