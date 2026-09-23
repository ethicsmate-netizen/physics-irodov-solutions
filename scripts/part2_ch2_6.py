"""
part2_ch2_6.py
Curated problems 2.185 to 2.219 (35 problems) of Irodov Chapter 2.6:
Phase Transformations.
"""

CH2_6_CURATED = [
    {
        "id": "2.185",
        "title": "Work of Isothermal Condensation of Vapour",
        "difficulty": 1,
        "question": "A saturated water vapour is contained in a cylindrical vessel under a weightless piston at a temperature $t = 100^\\circ\\text{C}$. As a result of a slow introduction of the piston a small fraction of the vapour $\\Delta m = 0.70\\text{ g}$ gets condensed. What amount of work was performed over the gas? The vapour is assumed to be ideal, the volume of the liquid is to be neglected.",
        "hints": [
            "At constant temperature, saturated vapour pressure remains constant: $p = p_0$.",
            "The work done on the vapour is $A = p \\Delta V$.",
            "Using the ideal gas law for the condensed vapour, $p \\Delta V = \\frac{\\Delta m}{M} R T$."
        ],
        "answer": "$A = \\frac{\\Delta m}{M} R T = 1.2 \\times 10^2\\text{ J}$",
        "solution": "**1. Work Done During Condensation:**\nSince temperature is constant, condensation occurs at constant saturated vapour pressure $p = p_0 = 1.013 \\times 10^5\\text{ Pa}$. The work done over the gas during compression by volume $\\Delta V$ is:\n$$A = p \\Delta V$$\n\n**2. Ideal Gas Law for Saturated Vapour:**\nNeglecting the liquid volume compared to the vapour volume, the volume change is equal to the volume originally occupied by the condensed vapour of mass $\\Delta m$:\n$$p \\Delta V = \\frac{\\Delta m}{M} R T$$\n\n**3. Numerical Calculation:**\nWith $\\Delta m = 0.70 \\times 10^{-3}\\text{ kg}$, $M = 18 \\times 10^{-3}\\text{ kg/mol}$, and $T = 373.15\\text{ K}$:\n$$A = \\frac{0.70 \\times 10^{-3}}{18 \\times 10^{-3}} \\times 8.314 \\times 373.15 \\approx 0.03889 \\times 3102.4 \\approx 120.6\\text{ J} \\approx 1.2 \\times 10^2\\text{ J}$$",
        "tags": ["saturated vapour", "condensation", "work done", "ideal gas"]
    },
    {
        "id": "2.186",
        "title": "Mass and Volume of Saturated Vapour in a Rigid Vessel",
        "difficulty": 2,
        "question": "A vessel of volume $V = 6.0\\text{ l}$ contains water together with its saturated vapour under a pressure of $40\\text{ atm}$ and at a temperature of $250^\\circ\\text{C}$. The specific volume of the vapour is equal to $V'_v = 50\\text{ l/kg}$ under these conditions. The total mass of the system water-vapour equals $m = 5.0\\text{ kg}$. Find the mass and the volume of the vapour.",
        "hints": [
            "Write the total mass: $m = m_v + m_l$.",
            "Write the total volume: $V = m_v V'_v + m_l V'_l$, where $V'_l \\approx 1.0\\text{ l/kg}$ is the specific volume of liquid water.",
            "Solve for $m_v = \\frac{V - m V'_l}{V'_v - V'_l}$ and then $V_v = m_v V'_v$."
        ],
        "answer": "$m_v = \\frac{V - m V'_l}{V'_v - V'_l} = 20\\text{ g}, \\quad V_v = 1.0\\text{ l}$",
        "solution": "**1. System Equations:**\nLet $m_v$ be the mass of the vapour and $m_l$ the mass of liquid water:\n$$m = m_v + m_l \\implies m_l = m - m_v$$\nThe total volume of the mixture is:\n$$V = m_v V'_v + m_l V'_l = m_v V'_v + (m - m_v) V'_l = m_v (V'_v - V'_l) + m V'_l$$\n\n**2. Mass and Volume of Vapour:**\n$$m_v = \\frac{V - m V'_l}{V'_v - V'_l}$$\n$$V_v = m_v V'_v$$\n\n**3. Numerical Values:**\nGiven $V = 6.0\\text{ l}$, $m = 5.0\\text{ kg}$, $V'_v = 50\\text{ l/kg}$, and using $V'_l \\approx 1.0\\text{ l/kg}$:\n$$m_v = \\frac{6.0 - 5.0 \\times 1.0}{50 - 1.0} = \\frac{1.0}{49} \\approx 0.0204\\text{ kg} \\approx 20\\text{ g}$$\n$$V_v = 0.0204\\text{ kg} \\times 50\\text{ l/kg} \\approx 1.02\\text{ l} \\approx 1.0\\text{ l}$$",
        "tags": ["saturated vapour", "specific volume", "two-phase mixture", "liquid-vapour"]
    },
    {
        "id": "2.187",
        "title": "Mass of Liquid Phase Formed on Isothermal Compression",
        "difficulty": 1,
        "question": "The saturated water vapour is enclosed in a cylinder under a piston and occupies a volume $V_0 = 5.0\\text{ l}$ at the temperature $t = 100^\\circ\\text{C}$. Find the mass of the liquid phase formed after the volume under the piston decreased isothermally to $V = 1.6\\text{ l}$. The saturated vapour is assumed to be ideal.",
        "hints": [
            "At $100^\\circ\\text{C}$, the saturated vapour pressure is standard atmospheric pressure $p_0 = 1.013 \\times 10^5\\text{ Pa}$.",
            "Since temperature is unchanged, the pressure remains $p_0$ throughout compression.",
            "The mass of condensed liquid is $m_l = m_0 - m_v = \\frac{p_0 (V_0 - V) M}{R T}$."
        ],
        "answer": "$m_l \\approx \\frac{M p_0 (V_0 - V)}{R T} = 2.0\\text{ g}$",
        "solution": "**1. Mass of Vapour Before and After Compression:**\nAt $100^\\circ\\text{C}$, the equilibrium saturated water vapour pressure is standard atmospheric pressure $p_0 = 1.013 \\times 10^5\\text{ Pa}$. As long as both phases coexist isothermally, the vapour pressure remains $p_0$.\n- Initial mass of vapour in volume $V_0$:\n  $$m_0 = \\frac{p_0 V_0 M}{R T}$$\n- Remaining mass of vapour in volume $V$:\n  $$m_v = \\frac{p_0 V M}{R T}$$\n\n**2. Mass of Condensed Liquid:**\nNeglecting the tiny volume occupied by liquid water compared to vapour:\n$$m_l = m_0 - m_v = \\frac{M p_0 (V_0 - V)}{R T}$$\n\n**3. Numerical Evaluation:**\nWith $V_0 - V = 5.0 - 1.6 = 3.4\\text{ l} = 3.4 \\times 10^{-3}\\text{ m}^3$, $M = 0.018\\text{ kg/mol}$, and $T = 373.15\\text{ K}$:\n$$m_l = \\frac{0.018 \\times 1.013 \\times 10^5 \\times 3.4 \\times 10^{-3}}{8.314 \\times 373.15} = \\frac{6.20}{3102.4} \\approx 2.0 \\times 10^{-3}\\text{ kg} = 2.0\\text{ g}$$",
        "tags": ["saturated vapour", "condensation", "isothermal compression"]
    },
    {
        "id": "2.188",
        "title": "Volume Fraction Occupied by Liquid Phase After Compression",
        "difficulty": 2,
        "question": "A volume occupied by a saturated vapour is reduced isothermally $n$-fold. Find what fraction $\\eta$ of the final volume is occupied by the liquid phase if the specific volumes of the saturated vapour and the liquid phase differ by $N$ times ($N > n$). Solve the same problem under the condition that the final volume of the substance corresponds to the midpoint of a horizontal portion of the isothermal line in the $(p, V)$ diagram.",
        "hints": [
            "Let $m$ be total mass. Initial volume is $V_1 = m V'_v$. Final volume is $V_2 = V_1 / n$.",
            "Express $V_2 = m_l V'_l + (m - m_l) V'_v$ and use $V'_v = N V'_l$ to find the volume fraction $\\eta = \\frac{V_l}{V_2}$.",
            "For the midpoint of the horizontal portion, $V_2 = \\frac{m(V'_l + V'_v)}{2}$ and $m_l = m/2$."
        ],
        "answer": "$\\eta = \\frac{n - 1}{N - 1}; \\quad \\eta = \\frac{1}{N + 1}$",
        "solution": "**1. General Case (Isothermal Compression by $n$-fold):**\nLet $m$ be the total mass. Initially, all mass is vapour:\n$$V_1 = m V'_v$$\nAfter compression to $V_2 = V_1 / n = \\frac{m V'_v}{n}$, liquid of mass $m_l$ and vapour of mass $m - m_l$ coexist:\n$$V_2 = m_l V'_l + (m - m_l) V'_v = m V'_v - m_l (V'_v - V'_l)$$\n$$\\frac{m V'_v}{n} = m V'_v - m_l V'_v \\left( 1 - \\frac{V'_l}{V'_v} \\right) = m V'_v - m_l V'_v \\left( 1 - \\frac{1}{N} \\right)$$\n$$m_l \\left( \\frac{N - 1}{N} \\right) = m \\left( 1 - \\frac{1}{n} \\right) = m \\frac{n - 1}{n} \\implies m_l = m \\frac{N (n - 1)}{n (N - 1)}$$\nThe volume occupied by liquid is:\n$$V_l = m_l V'_l = m_l \\frac{V'_v}{N} = \\frac{m V'_v (n - 1)}{n (N - 1)} = \\frac{V_1 (n - 1)}{n (N - 1)} = V_2 \\frac{n - 1}{N - 1}$$\nThus the volume fraction is:\n$$\\eta = \\frac{V_l}{V_2} = \\frac{n - 1}{N - 1}$$\n\n**2. Midpoint of Horizontal Plateau:**\nThe endpoints of the horizontal two-phase plateau correspond to all-liquid ($V_a = m V'_l$) and all-vapour ($V_b = m V'_v$).\nAt the midpoint, the total volume is:\n$$V_{\\text{mid}} = \\frac{V_a + V_b}{2} = \\frac{m(V'_l + V'_v)}{2}$$\nHere, half the mass is liquid ($m_l = m/2$), so:\n$$V_l = \\frac{m}{2} V'_l$$\nThe liquid volume fraction is:\n$$\\eta = \\frac{V_l}{V_{\\text{mid}}} = \\frac{\\frac{m}{2} V'_l}{\\frac{m}{2} (V'_l + V'_v)} = \\frac{V'_l}{V'_l + V'_v} = \\frac{1}{1 + \\frac{V'_v}{V'_l}} = \\frac{1}{N + 1}$$",
        "tags": ["phase equilibrium", "liquid fraction", "lever rule", "two-phase region"]
    },
    {
        "id": "2.189",
        "title": "Entropy and Internal Energy Change on Water Boiling",
        "difficulty": 2,
        "question": "An amount of water of mass $m = 1.00\\text{ kg}$, boiling at standard atmospheric pressure, turns completely into saturated vapour. Assuming the saturated vapour to be an ideal gas find the increment of entropy and internal energy of the system.",
        "hints": [
            "Boiling at constant pressure and temperature $T = 373.15\\text{ K}$ requires heat $Q = m q$, where $q = 2.26 \\times 10^6\\text{ J/kg}$.",
            "The entropy change is $\\Delta S = \\frac{m q}{T}$.",
            "Work done in expanding against atmospheric pressure is $A = p \\Delta V \\approx p V_v = \\frac{m}{M} R T$. Apply the first law $\\Delta U = Q - A$."
        ],
        "answer": "$\\Delta S = \\frac{m q}{T} = 6.0\\text{ kJ/K}; \\quad \\Delta U = m \\left( q - \\frac{R T}{M} \\right) = 2.1\\text{ MJ}$",
        "solution": "**1. Entropy Increment:**\nEvaporation takes place reversibly at boiling temperature $T = 373.15\\text{ K}$:\n$$\\Delta S = \\frac{Q}{T} = \\frac{m q}{T}$$\nWith $m = 1.00\\text{ kg}$ and $q = 2.26 \\times 10^6\\text{ J/kg}$:\n$$\\Delta S = \\frac{1.00 \\times 2.26 \\times 10^6}{373.15} \\approx 6.06 \\times 10^3\\text{ J/K} \\approx 6.0\\text{ kJ/K}$$\n\n**2. Internal Energy Increment:**\nBy the First Law of Thermodynamics:\n$$\\Delta U = Q - A$$\nNeglecting the liquid volume, the work done during expansion against atmospheric pressure $p_0$ is:\n$$A = p_0 V_v = \\frac{m}{M} R T$$\n$$\\Delta U = m q - \\frac{m}{M} R T = m \\left( q - \\frac{R T}{M} \\right)$$\nUsing $M = 0.018\\text{ kg/mol}$:\n$$\\frac{R T}{M} = \\frac{8.314 \\times 373.15}{0.018} \\approx 1.72 \\times 10^5\\text{ J/kg}$$\n$$\\Delta U = 1.00 \\times (2.26 \\times 10^6 - 0.172 \\times 10^6) \\approx 2.09 \\times 10^6\\text{ J} \\approx 2.1\\text{ MJ}$$",
        "tags": ["boiling", "latent heat", "entropy increment", "internal energy"]
    },
    {
        "id": "2.190",
        "title": "Rise of Piston Upon Heating Water into Steam",
        "difficulty": 2,
        "question": "Water of mass $m = 20\\text{ g}$ is enclosed in a thermally insulated cylinder at the temperature of $0^\\circ\\text{C}$ under a weightless piston whose area is $S = 410\\text{ cm}^2$. The outside pressure is equal to standard atmospheric pressure. To what height will the piston rise when the water absorbs $Q = 20.0\\text{ kJ}$ of heat?",
        "hints": [
            "Calculate heat required to bring water from $0^\\circ\\text{C}$ to $100^\\circ\\text{C}$: $Q_1 = m c \\Delta T$.",
            "The remaining heat $Q - Q_1$ causes partial vaporization of mass $\\Delta m$.",
            "Enthalpy of vaporization is $\\Delta H = \\Delta m (q + \\dots) \\approx \\Delta m q$, giving height $h = \\frac{V_v}{S} \\approx \\frac{Q - m c \\Delta T}{p_0 S (1 + \\frac{q M}{R T})}$."
        ],
        "answer": "$h \\approx \\frac{Q - m c \\Delta T}{p_0 S \\left( 1 + \\frac{q M}{R T} \\right)} = 20\\text{ cm}$",
        "solution": "**1. Heat Used to Warm Water:**\nThe heat needed to raise the water temperature from $0^\\circ\\text{C}$ to boiling ($100^\\circ\\text{C}$) is:\n$$Q_1 = m c \\Delta T = 0.020\\text{ kg} \\times 4184\\text{ J/(kg}\\cdot\\text{K)} \\times 100\\text{ K} \\approx 8.37\\text{ kJ}$$\n\n**2. Vaporization Heat:**\nThe remaining heat is used to vaporize a mass $\\Delta m$ of water under constant pressure $p_0$:\n$$Q - Q_1 = \\Delta H_{\\text{vap}} = \\Delta U + p_0 \\Delta V = \\Delta m \\left( q - \\frac{R T}{M} \\right) + \\Delta m \\frac{R T}{M} = \\Delta m q$$\n$$\\Delta m = \\frac{Q - m c \\Delta T}{q}$$\n\n**3. Height the Piston Rises:**\nThe volume of steam produced is $V = \\frac{\\Delta m}{M} \\frac{R T}{p_0} = S h$, so:\n$$h = \\frac{V}{S} = \\frac{\\Delta m R T}{p_0 S M} = \\frac{Q - m c \\Delta T}{p_0 S \\frac{q M}{R T}}$$\nWith $Q - Q_1 = 20.0 - 8.37 = 11.63\\text{ kJ}$, $q = 2.26 \\times 10^6\\text{ J/kg}$:\n$$\\Delta m = \\frac{11.63 \\times 10^3}{2.26 \\times 10^6} \\approx 5.15 \\times 10^{-3}\\text{ kg} = 5.15\\text{ g}$$\n$$V = \\frac{5.15 \\times 10^{-3} \\times 8.314 \\times 373.15}{0.018 \\times 1.013 \\times 10^5} \\approx 8.76 \\times 10^{-3}\\text{ m}^3$$\nWith $S = 410\\text{ cm}^2 = 0.0410\\text{ m}^2$:\n$$h = \\frac{8.76 \\times 10^{-3}\\text{ m}^3}{0.0410\\text{ m}^2} \\approx 0.214\\text{ m} \\approx 20\\text{ cm}$$",
        "tags": ["piston expansion", "vaporization", "steam volume", "atmospheric pressure"]
    },
    {
        "id": "2.191",
        "title": "Work of Atmospheric Pressure on Injecting Cold Water into Steam",
        "difficulty": 2,
        "question": "One gram of saturated water vapour is enclosed in a thermally insulated cylinder under a weightless piston. The outside pressure being standard, $m = 1.0\\text{ g}$ of water is introduced into the cylinder at a temperature $t_0 = 22^\\circ\\text{C}$. Neglecting the heat capacity of the cylinder and the friction of the piston against the cylinder's walls, find the work performed by the force of the atmospheric pressure during the lowering of the piston.",
        "hints": [
            "The cold water heats up to the boiling temperature $T = 373.15\\text{ K}$, absorbing heat $Q = m c (T - T_0)$.",
            "This heat is supplied by the condensation of an amount $\\Delta m$ of steam: $Q = \\Delta m q$.",
            "The volume decrease of steam is $\\Delta V = \\frac{\\Delta m}{M} \\frac{R T}{p_0}$, and the work done by atmosphere is $A = p_0 \\Delta V = \\frac{\\Delta m}{M} R T$."
        ],
        "answer": "$A = m c (T - T_0) \\frac{R T}{q M} = 25\\text{ J}$",
        "solution": "**1. Heat Balance for Condensation:**\nThe injected water at $t_0 = 22^\\circ\\text{C}$ ($T_0 = 295.15\\text{ K}$) heats up to the boiling temperature $T = 373.15\\text{ K}$:\n$$Q = m c (T - T_0)$$\nThis heat is released by condensation of vapour of mass $\\Delta m$ at constant temperature $T$:\n$$Q = \\Delta m q \\implies \\Delta m = \\frac{m c (T - T_0)}{q}$$\n\n**2. Atmospheric Work:**\nThe lowering of the piston by volume $\\Delta V$ performs work:\n$$A = p_0 \\Delta V = p_0 \\left( \\frac{\\Delta m}{M} \\frac{R T}{p_0} \\right) = \\frac{\\Delta m}{M} R T = m c (T - T_0) \\frac{R T}{q M}$$\n\n**3. Numerical Evaluation:**\nGiven $m = 1.0 \\times 10^{-3}\\text{ kg}$, $c = 4184\\text{ J/(kg}\\cdot\\text{K)}$, $T - T_0 = 373.15 - 295.15 = 78\\text{ K}$, $q = 2.26 \\times 10^6\\text{ J/kg}$, and $M = 0.018\\text{ kg/mol}$:\n$$Q = 1.0 \\times 10^{-3} \\times 4184 \\times 78 \\approx 326.4\\text{ J}$$\n$$\\Delta m = \\frac{326.4}{2.26 \\times 10^6} \\approx 1.444 \\times 10^{-4}\\text{ kg}$$\n$$A = \\frac{1.444 \\times 10^{-4}}{0.018} \\times 8.314 \\times 373.15 \\approx 8.02 \\times 10^{-3} \\times 3102 \\approx 24.9\\text{ J} \\approx 25\\text{ J}$$",
        "tags": ["condensation", "atmospheric work", "heat exchange", "saturated steam"]
    },
    {
        "id": "2.192",
        "title": "Droplet Size from Saturated Vapour Pressure Elevation",
        "difficulty": 2,
        "question": "If an additional pressure $\\Delta p$ of a saturated vapour over a convex spherical surface of a liquid is considerably less than the vapour pressure over a plane surface, then $\\Delta p = \\frac{\\rho_v}{\\rho_l} \\frac{2\\alpha}{r}$, where $\\rho_v$ and $\\rho_l$ are the densities of the vapour and the liquid, $\\alpha$ is the surface tension, and $r$ is the radius of curvature of the surface. Using this formula, find the diameter of water droplets at which the saturated vapour pressure exceeds the vapour pressure over the plane surface by $\\eta = 1.0\\%$ at a temperature $t = 27^\\circ\\text{C}$. The vapour is assumed to be an ideal gas.",
        "hints": [
            "We are given $\\frac{\\Delta p}{p_0} = \\eta$, where $p_0$ is the saturated vapour pressure over a flat surface.",
            "Using the ideal gas law for the vapour: $\\rho_v = \\frac{p_0 M}{R T}$.",
            "Substitute $\\rho_v$ into the Kelvin formula and solve for $d = 2r$: $d \\approx \\frac{4\\alpha M}{\\eta \\rho_l R T}$."
        ],
        "answer": "$d \\approx \\frac{4\\alpha M}{\\eta \\rho_l R T} = 0.2\\,\\mu\\text{m}$",
        "solution": "**1. Kelvin Formula for Vapour Pressure:**\nOver a convex spherical droplet of radius $r = d/2$:\n$$\\Delta p = \\frac{\\rho_v}{\\rho_l} \\frac{2\\alpha}{r} = \\frac{\\rho_v}{\\rho_l} \\frac{4\\alpha}{d}$$\nGiven $\\frac{\\Delta p}{p_0} = \\eta$, where $p_0$ is the flat-surface saturated vapour pressure:\n$$\\eta p_0 = \\frac{\\rho_v}{\\rho_l} \\frac{4\\alpha}{d}$$\n\n**2. Density of Ideal Saturated Vapour:**\n$$\\rho_v = \\frac{p_0 M}{R T}$$\nSubstituting $\\rho_v$:\n$$\\eta p_0 = \\frac{p_0 M}{\\rho_l R T} \\frac{4\\alpha}{d} \\implies d = \\frac{4\\alpha M}{\\eta \\rho_l R T}$$\n\n**3. Numerical Evaluation:**\nWith $\\alpha = 0.073\\text{ N/m}$, $M = 0.018\\text{ kg/mol}$, $\\eta = 0.010$, $\\rho_l = 1000\\text{ kg/m}^3$, and $T = 300\\text{ K}$:\n$$d = \\frac{4 \\times 0.073 \\times 0.018}{0.010 \\times 1000 \\times 8.314 \\times 300} = \\frac{5.256 \\times 10^{-3}}{24942} \\approx 2.1 \\times 10^{-7}\\text{ m} = 0.21\\,\\mu\\text{m} \\approx 0.2\\,\\mu\\text{m}$$",
        "tags": ["Kelvin equation", "water droplet", "vapour pressure", "surface tension"]
    },
    {
        "id": "2.193",
        "title": "Evaporation Rate of Water Molecules at Boiling Temperature",
        "difficulty": 2,
        "question": "Find the mass of all molecules leaving one square centimetre of water surface per second into a saturated water vapour above it at a temperature $t = 100^\\circ\\text{C}$. It is assumed that $\\eta = 3.6\\%$ of all water vapour molecules falling on the water surface are retained in the liquid phase.",
        "hints": [
            "At dynamic equilibrium between liquid and saturated vapour, rate of evaporation equals rate of condensation.",
            "The molecular flux incident on the surface from the vapour is $J = \\frac{1}{4} n \\langle v \\rangle$.",
            "The rate of condensation is $\\mu = \\eta J m_0 = \\eta p_0 \\sqrt{\\frac{M}{2\\pi R T}}$."
        ],
        "answer": "$\\mu = \\eta p_0 \\sqrt{\\frac{M}{2\\pi R T}} = 0.35\\text{ g/(s}\\cdot\\text{cm}^2)$",
        "solution": "**1. Kinetic Theory of Collisions with Surface:**\nThe number of gas molecules striking a unit surface area per unit time is:\n$$J = \\frac{1}{4} n \\langle v \\rangle$$\nwhere the mean thermal speed is $\\langle v \\rangle = \\sqrt{\\frac{8 R T}{\\pi M}}$, and $n = \\frac{p_0}{k T}$.\nThe incident mass flux is:\n$$j_{\\text{mass}} = J m_0 = \\frac{1}{4} \\frac{p_0}{k T} m_0 \\sqrt{\\frac{8 R T}{\\pi M}} = p_0 \\sqrt{\\frac{M}{2\\pi R T}}$$\n\n**2. Dynamic Equilibrium:**\nIn equilibrium, the evaporation mass flux $\\mu$ equals the condensation mass flux. Since only a fraction $\\eta$ of the colliding vapour molecules stick and condense:\n$$\\mu = \\eta j_{\\text{mass}} = \\eta p_0 \\sqrt{\\frac{M}{2\\pi R T}}$$\n\n**3. Numerical Calculation:**\nFor $t = 100^\\circ\\text{C}$ ($T = 373.15\\text{ K}$), $p_0 = 1.013 \\times 10^5\\text{ Pa}$, $M = 0.018\\text{ kg/mol}$, and $\\eta = 0.036$:\n$$\\sqrt{\\frac{M}{2\\pi R T}} = \\sqrt{\\frac{0.018}{2\\pi \\times 8.314 \\times 373.15}} = \\sqrt{\\frac{0.018}{1.949 \\times 10^4}} = \\sqrt{9.235 \\times 10^{-7}} \\approx 9.61 \\times 10^{-4}\\text{ s/m}$$\n$$\\mu = 0.036 \\times 1.013 \\times 10^5 \\times 9.61 \\times 10^{-4} \\approx 3.51\\text{ kg/(s}\\cdot\\text{m}^2) = 0.35\\text{ g/(s}\\cdot\\text{cm}^2)$$",
        "tags": ["evaporation rate", "kinetic theory", "condensation coefficient", "Hertz-Knudsen"]
    },
    {
        "id": "2.194",
        "title": "Saturated Tungsten Vapour Pressure from Vacuum Evaporation",
        "difficulty": 2,
        "question": "Find the pressure of saturated tungsten vapour at a temperature $T = 2000\\text{ K}$ if a tungsten filament is known to lose a mass $\\mu = 1.2 \\times 10^{-13}\\text{ g/(s}\\cdot\\text{cm}^2)$ from a unit area per unit time when evaporating into high vacuum at this temperature.",
        "hints": [
            "In high vacuum, evaporated atoms do not return to the filament (no back-scattering).",
            "Assuming unity sticking coefficient (Langmuir method), the vacuum evaporation rate equals the equilibrium sublimation rate: $\\mu = p \\sqrt{\\frac{M}{2\\pi R T}}$.",
            "Solve for vapour pressure: $p = \\mu \\sqrt{\\frac{2\\pi R T}{M}}$ with $M_{\\text{W}} = 184\\text{ g/mol}$."
        ],
        "answer": "$p = \\mu \\sqrt{\\frac{2\\pi R T}{M}} = 0.9\\text{ nPa}$",
        "solution": "**1. Langmuir Evaporation Formula:**\nWhen evaporating into a high vacuum, no vapor molecules bounce back. For metals, the sticking coefficient is very close to unity, so the evaporation rate equals the incident flux at the equilibrium saturated vapour pressure $p$:\n$$\\mu = p \\sqrt{\\frac{M}{2\\pi R T}}$$\n\n**2. Saturated Vapour Pressure:**\n$$p = \\mu \\sqrt{\\frac{2\\pi R T}{M}}$$\n\n**3. Numerical Evaluation:**\nGiven $\\mu = 1.2 \\times 10^{-13}\\text{ g/(s}\\cdot\\text{cm}^2) = 1.2 \\times 10^{-12}\\text{ kg/(s}\\cdot\\text{m}^2)$, $T = 2000\\text{ K}$, and $M = 183.84 \\times 10^{-3}\\text{ kg/mol}$:\n$$\\sqrt{\\frac{2\\pi R T}{M}} = \\sqrt{\\frac{2\\pi \\times 8.314 \\times 2000}{0.18384}} = \\sqrt{\\frac{1.045 \\times 10^5}{0.18384}} = \\sqrt{5.684 \\times 10^5} \\approx 754\\text{ m/s}$$\n$$p = 1.2 \\times 10^{-12} \\times 754 \\approx 9.05 \\times 10^{-10}\\text{ Pa} \\approx 0.9\\text{ nPa}$$",
        "tags": ["Langmuir evaporation", "tungsten", "saturated vapour pressure", "high vacuum"]
    },
    {
        "id": "2.195",
        "title": "Internal Pressure of Liquid Water",
        "difficulty": 2,
        "question": "By what magnitude would the pressure exerted by water on the walls of the vessel have increased if the intermolecular attraction forces had vanished?",
        "hints": [
            "In the Van der Waals equation, intermolecular attraction is represented by the internal pressure term $p_i = \\frac{a}{V_m^2}$.",
            "Express the molar volume of water as $V_m = \\frac{M}{\\rho}$.",
            "Calculate $\\Delta p = p_i = a \\left( \\frac{\\rho}{M} \\right)^2$ using Van der Waals constant $a$ for water."
        ],
        "answer": "$\\Delta p = \\frac{a}{V_m^2} = a \\left( \\frac{\\rho}{M} \\right)^2 = 1.7 \\times 10^4\\text{ atm}$",
        "solution": "**1. Van der Waals Internal Pressure:**\nThe internal molecular pressure $p_i$ that pulls molecules inwards and reduces the force exerted on the container walls is:\n$$p_i = \\frac{a}{V_m^2}$$\nIf these attractive intermolecular forces vanished, the pressure on the walls would increase by this internal pressure:\n$$\\Delta p = p_i = a \\left( \\frac{\\rho}{M} \\right)^2$$\n\n**2. Numerical Calculation:**\nFor water, $a = 0.553\\text{ J}\\cdot\\text{m}^3/\\text{mol}^2 = 5.46\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2$, $\\rho = 1000\\text{ kg/m}^3$, and $M = 0.018\\text{ kg/mol}$:\n$$V_m = \\frac{0.018}{1000} = 1.8 \\times 10^{-5}\\text{ m}^3/\\text{mol}$$\n$$\\Delta p = \\frac{0.553}{(1.8 \\times 10^{-5})^2} = \\frac{0.553}{3.24 \\times 10^{-10}} \\approx 1.71 \\times 10^9\\text{ Pa} \\approx 1.7 \\times 10^4\\text{ atm}$$",
        "tags": ["Van der Waals", "internal pressure", "intermolecular forces", "water"]
    },
    {
        "id": "2.196",
        "title": "Internal Pressure of a Liquid from Latent Heat",
        "difficulty": 2,
        "question": "Find the internal pressure $p_i$ of a liquid if its density $\\rho$ and specific latent heat of vaporization $q$ are known. The heat $q$ is assumed to be equal to the work performed against the forces of the internal pressure, and the liquid obeys the Van der Waals equation. Calculate $p_i$ in water.",
        "hints": [
            "The work done in separating molecules against internal pressure $p_i = \\frac{a}{V_m^2}$ from liquid molar volume $V_{m, l}$ to gas $V_{m, v} \\gg V_{m, l}$ is $\\Delta U_{\\text{vap}} = \\int_{V_{m, l}}^\\infty \\frac{a}{V^2} dV = \\frac{a}{V_{m, l}}$.",
            "This molar latent heat is $q M \\approx \\frac{a}{V_{m, l}} = p_i V_{m, l}$.",
            "Thus $p_i \\approx \\frac{q M}{V_{m, l}} = q \\rho$."
        ],
        "answer": "$p_i \\approx q \\rho \\approx 2 \\times 10^4\\text{ atm}$",
        "solution": "**1. Work Against Internal Pressure:**\nAccording to the Van der Waals model, the potential energy per mole due to molecular attraction is $-a/V_m$. In vaporizing from liquid molar volume $V_{m, l}$ to an infinite volume in the vapour phase, the work done against internal attractive forces per mole is:\n$$A_i = \\int_{V_{m, l}}^\\infty p_i dV_m = \\int_{V_{m, l}}^\\infty \\frac{a}{V_m^2} dV_m = \\frac{a}{V_{m, l}}$$\n\n**2. Relation to Specific Latent Heat:**\nAssuming this work equals the latent heat per mole $q M$:\n$$q M \\approx \\frac{a}{V_{m, l}} = p_i V_{m, l} \\implies p_i \\approx \\frac{q M}{V_{m, l}}$$\nSince $V_{m, l} / M = 1 / \\rho$ is the specific volume of the liquid:\n$$p_i \\approx q \\rho$$\n\n**3. Value for Water:**\nFor water, $q \\approx 2.26 \\times 10^6\\text{ J/kg}$ and $\\rho = 1000\\text{ kg/m}^3$:\n$$p_i \\approx 2.26 \\times 10^6 \\times 1000 = 2.26 \\times 10^9\\text{ Pa} \\approx 2.2 \\times 10^4\\text{ atm} \\approx 2 \\times 10^4\\text{ atm}$$",
        "tags": ["internal pressure", "latent heat of vaporization", "Van der Waals", "liquid water"]
    },
    {
        "id": "2.197",
        "title": "Derivation of Van der Waals Critical Constants",
        "difficulty": 3,
        "question": "Demonstrate that the critical parameters for a Van der Waals substance satisfy:\n$$V_{m, \\text{cr}} = 3b, \\quad p_{\\text{cr}} = \\frac{a}{27 b^2}, \\quad T_{\\text{cr}} = \\frac{8a}{27 R b}, \\quad \\frac{p_{\\text{cr}} V_{m, \\text{cr}}}{R T_{\\text{cr}}} = \\frac{3}{8}$$",
        "hints": [
            "Write the Van der Waals equation of state: $p = \\frac{R T}{V_m - b} - \\frac{a}{V_m^2}$.",
            "At the critical point, the isothermal curve has a point of inflection with horizontal tangent: $\\left(\\frac{\\partial p}{\\partial V_m}\\right)_T = 0$ and $\\left(\\frac{\\partial^2 p}{\\partial V_m^2}\\right)_T = 0$.",
            "Solve the system of equations for $V_{m, \\text{cr}}$, $T_{\\text{cr}}$, and $p_{\\text{cr}}$."
        ],
        "answer": "$V_{m, \\text{cr}} = 3b, \\quad p_{\\text{cr}} = \\frac{a}{27 b^2}, \\quad T_{\\text{cr}} = \\frac{8a}{27 R b}, \\quad \\frac{p_{\\text{cr}} V_{m, \\text{cr}}}{R T_{\\text{cr}}} = \\frac{3}{8}$",
        "solution": "**1. Condition for the Critical Point:**\nExpressing pressure from the Van der Waals equation:\n$$p = \\frac{R T}{V_m - b} - \\frac{a}{V_m^2}$$\nAt the critical point $(T = T_{\\text{cr}}, V_m = V_{\\text{cr}})$, the isotherm has an inflection point with a horizontal tangent:\n$$\\left( \\frac{\\partial p}{\\partial V_m} \\right)_T = -\\frac{R T_{\\text{cr}}}{(V_{\\text{cr}} - b)^2} + \\frac{2a}{V_{\\text{cr}}^3} = 0$$\n$$\\left( \\frac{\\partial^2 p}{\\partial V_m^2} \\right)_T = \\frac{2 R T_{\\text{cr}}}{(V_{\\text{cr}} - b)^3} - \\frac{6a}{V_{\\text{cr}}^4} = 0$$\n\n**2. Solving for Critical Parameters:**\nDividing the second equation by the first:\n$$\\frac{2}{V_{\\text{cr}} - b} = \\frac{3}{V_{\\text{cr}}} \\implies 2 V_{\\text{cr}} = 3 V_{\\text{cr}} - 3b \\implies V_{m, \\text{cr}} = 3b$$\nSubstitute $V_{\\text{cr}} = 3b$ back into the first derivative equation:\n$$\\frac{R T_{\\text{cr}}}{(2b)^2} = \\frac{2a}{(3b)^3} \\implies \\frac{R T_{\\text{cr}}}{4b^2} = \\frac{2a}{27b^3} \\implies T_{\\text{cr}} = \\frac{8a}{27 R b}$$\nNow substitute $V_{m, \\text{cr}}$ and $T_{\\text{cr}}$ into the equation of state:\n$$p_{\\text{cr}} = \\frac{R \\left( \\frac{8a}{27 R b} \\right)}{2b} - \\frac{a}{(3b)^2} = \\frac{4a}{27 b^2} - \\frac{3a}{27 b^2} = \\frac{a}{27 b^2}$$\n\n**3. Critical Compressibility Factor:**\n$$\\frac{p_{\\text{cr}} V_{m, \\text{cr}}}{R T_{\\text{cr}}} = \\frac{\\left( \\frac{a}{27 b^2} \\right) (3b)}{R \\left( \\frac{8a}{27 R b} \\right)} = \\frac{3}{8} = 0.375$$",
        "tags": ["Van der Waals", "critical point", "inflection point", "derivation"]
    },
    {
        "id": "2.198",
        "title": "Van der Waals Constants for Carbon Dioxide",
        "difficulty": 2,
        "question": "Calculate the Van der Waals constants for carbon dioxide if its critical temperature $T_{\\text{cr}} = 304\\text{ K}$ and critical pressure $p_{\\text{cr}} = 73\\text{ atm}$.",
        "hints": [
            "Use the relations $b = \\frac{R T_{\\text{cr}}}{8 p_{\\text{cr}}}$ and $a = \\frac{27 R^2 T_{\\text{cr}}^2}{64 p_{\\text{cr}}}$.",
            "Be consistent with units: $R = 0.0821\\text{ atm}\\cdot\\text{l/(mol}\\cdot\\text{K)}$.",
            "Calculate $b$ in $\\text{l/mol}$ and $a$ in $\\text{atm}\\cdot\\text{l}^2/\\text{mol}^2$."
        ],
        "answer": "$a = \\frac{27 R^2 T_{\\text{cr}}^2}{64 p_{\\text{cr}}} = 3.6\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2; \\quad b = \\frac{R T_{\\text{cr}}}{8 p_{\\text{cr}}} = 0.043\\text{ l/mol}$",
        "solution": "**1. Formulae for Constants:**\nFrom the critical parameters of a Van der Waals gas:\n$$b = \\frac{R T_{\\text{cr}}}{8 p_{\\text{cr}}}, \\quad a = \\frac{27 R^2 T_{\\text{cr}}^2}{64 p_{\\text{cr}}}$$\n\n**2. Numerical Calculations:**\nUsing $R = 0.08206\\text{ atm}\\cdot\\text{l/(mol}\\cdot\\text{K)}$, $T_{\\text{cr}} = 304\\text{ K}$, and $p_{\\text{cr}} = 73\\text{ atm}$:\n$$b = \\frac{0.08206 \\times 304}{8 \\times 73} = \\frac{24.95}{584} \\approx 0.0427\\text{ l/mol} \\approx 0.043\\text{ l/mol}$$\n$$a = \\frac{27 \\times (0.08206)^2 \\times (304)^2}{64 \\times 73} = \\frac{27 \\times 0.006734 \\times 92416}{4672} = \\frac{16802}{4672} \\approx 3.60\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2$$",
        "tags": ["Van der Waals constants", "carbon dioxide", "critical parameters"]
    },
    {
        "id": "2.199",
        "title": "Specific Volume of Benzene in the Critical State",
        "difficulty": 2,
        "question": "Find the specific volume of benzene ($\\text{C}_6\\text{H}_6$) in the critical state if its critical temperature $T_{\\text{cr}} = 562\\text{ K}$ and critical pressure $p_{\\text{cr}} = 47\\text{ atm}$.",
        "hints": [
            "Use the critical relation $\\frac{p_{\\text{cr}} V_{m, \\text{cr}}}{R T_{\\text{cr}}} = \\frac{3}{8}$.",
            "The molar volume is $V_{m, \\text{cr}} = \\frac{3 R T_{\\text{cr}}}{8 p_{\\text{cr}}}$.",
            "The specific volume is $V'_{\\text{cr}} = \\frac{V_{m, \\text{cr}}}{M}$, with $M = 78\\text{ g/mol}$."
        ],
        "answer": "$V'_{\\text{cr}} = \\frac{3 R T_{\\text{cr}}}{8 M p_{\\text{cr}}} = 4.7\\text{ cm}^3/\\text{g}$",
        "solution": "**1. Critical Specific Volume:**\nFrom the Van der Waals critical compressibility factor $\\frac{p_{\\text{cr}} V_{m, \\text{cr}}}{R T_{\\text{cr}}} = \\frac{3}{8}$:\n$$V_{m, \\text{cr}} = \\frac{3 R T_{\\text{cr}}}{8 p_{\\text{cr}}}$$\nThe specific volume (volume per unit mass) is:\n$$V'_{\\text{cr}} = \\frac{V_{m, \\text{cr}}}{M} = \\frac{3 R T_{\\text{cr}}}{8 M p_{\\text{cr}}}$$\n\n**2. Numerical Calculation:**\nWith $M = 78.11\\text{ g/mol}$, $T_{\\text{cr}} = 562\\text{ K}$, $p_{\\text{cr}} = 47 \\times 1.013 \\times 10^5\\text{ Pa} = 4.76 \\times 10^6\\text{ Pa}$, and $R = 8.314\\text{ J/(mol}\\cdot\\text{K)}$:\n$$V'_{\\text{cr}} = \\frac{3 \\times 8.314 \\times 562}{8 \\times 0.07811 \\times 4.76 \\times 10^6} = \\frac{14017}{2.975 \\times 10^6} \\approx 4.71 \\times 10^{-3}\\text{ m}^3/\\text{kg} = 4.7\\text{ cm}^3/\\text{g}$$",
        "tags": ["benzene", "critical specific volume", "Van der Waals"]
    },
    {
        "id": "2.200",
        "title": "Law of Corresponding States for Van der Waals Gas",
        "difficulty": 2,
        "question": "Write the Van der Waals equation via the reduced parameters $\\pi$, $\\nu$, and $\\tau$, having taken the corresponding critical values for the units of pressure, volume, and temperature. Using the equation obtained, find how many times the gas temperature exceeds its critical temperature if gas pressure is 12 times as high as critical pressure, and the volume of gas is equal to half the critical volume.",
        "hints": [
            "Reduced variables: $\\pi = p / p_{\\text{cr}}$, $\\nu = V_m / V_{m, \\text{cr}}$, $\\tau = T / T_{\\text{cr}}$.",
            "Substitute $p = \\pi p_{\\text{cr}}$, $V_m = \\nu V_{m, \\text{cr}}$, $T = \\tau T_{\\text{cr}}$ into $(p + a/V_m^2)(V_m - b) = R T$ to obtain $\\left(\\pi + \\frac{3}{\\nu^2}\\right)(3\\nu - 1) = 8\\tau$.",
            "Plug in $\\pi = 12$ and $\\nu = 0.5$ to find $\\tau$."
        ],
        "answer": "$\\left( \\pi + \\frac{3}{\\nu^2} \\right) (3\\nu - 1) = 8\\tau; \\quad \\tau = 1.5$",
        "solution": "**1. Derivation of Reduced Equation:**\nSubstituting $p = \\pi \\frac{a}{27b^2}$, $V_m = \\nu (3b)$, and $T = \\tau \\frac{8a}{27Rb}$ into the Van der Waals equation:\n$$\\left( \\pi \\frac{a}{27b^2} + \\frac{a}{9b^2 \\nu^2} \\right) (3b\\nu - b) = R \\tau \\frac{8a}{27Rb}$$\n$$\\frac{a}{27b^2} \\left( \\pi + \\frac{3}{\\nu^2} \\right) \\cdot b (3\\nu - 1) = \\frac{8a}{27b} \\tau$$\n$$\\left( \\pi + \\frac{3}{\\nu^2} \\right) (3\\nu - 1) = 8\\tau$$\n\n**2. Evaluation for $\\pi = 12$ and $\\nu = 0.5$:**\n$$\\left( 12 + \\frac{3}{(0.5)^2} \\right) (3 \\times 0.5 - 1) = 8\\tau$$\n$$\\left( 12 + 12 \\right) (1.5 - 1) = 24 \\times 0.5 = 12 = 8\\tau$$\n$$\\tau = \\frac{12}{8} = 1.5$$\nThus, the temperature exceeds the critical temperature by $1.5$ times.",
        "tags": ["law of corresponding states", "reduced equation", "Van der Waals", "reduced variables"]
    },
    {
        "id": "2.201",
        "title": "Maximum Liquid Volume and Maximum Saturated Vapour Pressure",
        "difficulty": 2,
        "question": "Knowing the Van der Waals constants for water, find:\n(a) the maximum volume which water of mass $m = 1.00\\text{ kg}$ can occupy in the liquid state;\n(b) the maximum pressure of the saturated water vapour.",
        "hints": [
            "(a) In the liquid state, water can only exist up to the critical state, where its molar volume is $V_{m, \\text{cr}} = 3b$. The maximum liquid volume is $V_{\\max} = \\frac{m}{M} (3b)$.",
            "(b) Saturated vapour can only exist up to the critical point, where the pressure is $p_{\\max} = p_{\\text{cr}} = \\frac{a}{27 b^2}$.",
            "Use for water: $a = 5.46\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2$ and $b = 0.030\\text{ l/mol}$."
        ],
        "answer": "(a) $V_{\\max} = \\frac{3bm}{M} = 5.0\\text{ l}$; (b) $p_{\\max} = \\frac{a}{27 b^2} = 2.2 \\times 10^2\\text{ atm}$",
        "solution": "**1. Maximum Liquid Volume:**\nThe boundary between liquid and gaseous phases disappears at the critical point. The maximum specific volume of liquid occurs at the critical state:\n$$V_{\\max} = \\frac{m}{M} V_{m, \\text{cr}} = \\frac{3bm}{M}$$\nUsing $b = 0.030\\text{ l/mol}$, $m = 1.00\\text{ kg} = 1000\\text{ g}$, and $M = 18\\text{ g/mol}$:\n$$V_{\\max} = \\frac{3 \\times 0.030 \\times 1000}{18} = \\frac{90}{18} = 5.0\\text{ l}$$\n\n**2. Maximum Saturated Vapour Pressure:**\nThe coexistence line of liquid and saturated vapour terminates at the critical point, so the maximum saturated vapour pressure is the critical pressure:\n$$p_{\\max} = p_{\\text{cr}} = \\frac{a}{27 b^2}$$\nUsing $a = 5.46\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2$ and $b = 0.030\\text{ l/mol}$:\n$$p_{\\max} = \\frac{5.46}{27 \\times (0.030)^2} = \\frac{5.46}{0.0243} \\approx 225\\text{ atm} \\approx 2.2 \\times 10^2\\text{ atm}$$",
        "tags": ["critical point", "saturated vapour", "water", "maximum volume"]
    },
    {
        "id": "2.202",
        "title": "Critical Temperature and Density of Carbon Dioxide",
        "difficulty": 2,
        "question": "Calculate the temperature and density of carbon dioxide in the critical state, assuming the gas to be a Van der Waals one.",
        "hints": [
            "Critical temperature: $T_{\\text{cr}} = \\frac{8a}{27 R b}$.",
            "Critical density: $\\rho_{\\text{cr}} = \\frac{M}{V_{m, \\text{cr}}} = \\frac{M}{3b}$.",
            "Use $a = 3.6\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2$, $b = 0.043\\text{ l/mol}$, and $M = 44\\text{ g/mol}$."
        ],
        "answer": "$T_{\\text{cr}} = \\frac{8a}{27 R b} = 0.30\\text{ kK}; \\quad \\rho_{\\text{cr}} = \\frac{M}{3b} = 0.34\\text{ g/cm}^3$",
        "solution": "**1. Critical Temperature:**\n$$T_{\\text{cr}} = \\frac{8a}{27 R b}$$\nWith $a = 3.6\\text{ atm}\\cdot\\text{l}^2/\\text{mol}^2 = 0.365\\text{ J}\\cdot\\text{m}^3/\\text{mol}^2$, $b = 0.043\\text{ l/mol} = 4.3 \\times 10^{-5}\\text{ m}^3/\\text{mol}$, and $R = 8.314\\text{ J/(mol}\\cdot\\text{K)}$:\n$$T_{\\text{cr}} = \\frac{8 \\times 0.365}{27 \\times 8.314 \\times 4.3 \\times 10^{-5}} = \\frac{2.92}{9.65 \\times 10^{-3}} \\approx 302\\text{ K} \\approx 0.30\\text{ kK}$$\n\n**2. Critical Density:**\n$$\\rho_{\\text{cr}} = \\frac{M}{V_{m, \\text{cr}}} = \\frac{M}{3b}$$\nWith $M = 44\\text{ g/mol}$ and $b = 43\\text{ cm}^3/\\text{mol}$:\n$$\\rho_{\\text{cr}} = \\frac{44}{3 \\times 43} = \\frac{44}{129} \\approx 0.341\\text{ g/cm}^3 \\approx 0.34\\text{ g/cm}^3$$",
        "tags": ["carbon dioxide", "critical temperature", "critical density", "Van der Waals"]
    },
    {
        "id": "2.203",
        "title": "Ratio of Critical Density to Liquid Density for Ether",
        "difficulty": 2,
        "question": "Find the ratio $\\eta$ of the critical density of ethyl ether to its liquid density at room temperature, knowing the critical parameters $T_{\\text{cr}} = 467\\text{ K}$ and $p_{\\text{cr}} = 35.5\\text{ atm}$, the molar mass $M = 74\\text{ g/mol}$, and the room temperature density $\\rho = 0.71\\text{ g/cm}^3$.",
        "hints": [
            "Use the Van der Waals critical compressibility relation: $V_{m, \\text{cr}} = \\frac{3 R T_{\\text{cr}}}{8 p_{\\text{cr}}}$.",
            "The critical density is $\\rho_{\\text{cr}} = \\frac{M}{V_{m, \\text{cr}}} = \\frac{8 M p_{\\text{cr}}}{3 R T_{\\text{cr}}}$.",
            "The desired ratio is $\\eta = \\frac{\\rho_{\\text{cr}}}{\\rho} = \\frac{8 M p_{\\text{cr}}}{3 \\rho R T_{\\text{cr}}}$."
        ],
        "answer": "$\\eta = \\frac{8 M p_{\\text{cr}}}{3 \\rho R T_{\\text{cr}}} = 0.25$",
        "solution": "**1. Critical Density Expression:**\nFrom the critical parameters of a Van der Waals substance:\n$$V_{m, \\text{cr}} = \\frac{3 R T_{\\text{cr}}}{8 p_{\\text{cr}}} \\implies \\rho_{\\text{cr}} = \\frac{M}{V_{m, \\text{cr}}} = \\frac{8 M p_{\\text{cr}}}{3 R T_{\\text{cr}}}$$\n\n**2. Density Ratio:**\n$$\\eta = \\frac{\\rho_{\\text{cr}}}{\\rho} = \\frac{8 M p_{\\text{cr}}}{3 \\rho R T_{\\text{cr}}}$$\n\n**3. Numerical Evaluation:**\nWith $M = 0.074\\text{ kg/mol}$, $p_{\\text{cr}} = 35.5 \\times 1.013 \\times 10^5\\text{ Pa} = 3.60 \\times 10^6\\text{ Pa}$, $\\rho = 710\\text{ kg/m}^3$, $R = 8.314\\text{ J/(mol}\\cdot\\text{K)}$, and $T_{\\text{cr}} = 467\\text{ K}$:\n$$\\eta = \\frac{8 \\times 0.074 \\times 3.60 \\times 10^6}{3 \\times 710 \\times 8.314 \\times 467} = \\frac{2.13 \\times 10^6}{8.26 \\times 10^6} \\approx 0.258 \\approx 0.25$$",
        "tags": ["ethyl ether", "critical density", "density ratio", "Van der Waals"]
    },
    {
        "id": "2.204",
        "title": "Maxwell Equal-Area Construction for Van der Waals Isotherm",
        "difficulty": 3,
        "question": "Demonstrate that the horizontal plateau corresponding to the coexistence of liquid and saturated vapour on the $(p, V)$ diagram divides the Van der Waals wave-like isotherm into two equal-area loops (Maxwell construction).",
        "hints": [
            "Consider a reversible closed isothermal cycle following the Van der Waals theoretical isotherm and returning along the equilibrium horizontal line.",
            "For this isothermal cycle at temperature $T$, $\\oint T dS = 0$ since $T = \\text{const}$ and $\\oint dS = 0$.",
            "By the First Law, $\\oint dQ = \\oint dU + \\oint p dV$. Since $\\oint dU = 0$ and $\\oint dQ = 0$, we have $\\oint p dV = 0$."
        ],
        "answer": "The two lobes have equal areas: $\\int_{V_l}^{V_v} (p_{\\text{VdW}} - p_{\\text{sat}}) dV = 0$",
        "solution": "**1. Reversible Isothermal Cycle:**\nConsider a cyclic process along the theoretical Van der Waals S-curve from liquid state 1 to vapour state 2 and back along the horizontal equilibrium coexistence line at pressure $p_{\\text{sat}}$:\n$$\\oint T dS = T \\oint dS = 0$$\nsince entropy $S$ is a state function.\n\n**2. First Law Application:**\nOver any complete cycle:\n$$\\Delta U = \\oint dU = 0$$\n$$\\oint dQ = \\oint T dS = 0$$\nTherefore, the net work done in the cycle must vanish:\n$$\\oint p dV = 0$$\n\n**3. Maxwell Equal-Area Rule:**\nThe cyclic integral can be split into the path along the Van der Waals isotherm and the return path along the horizontal plateau:\n$$\\int_{V_l}^{V_v} p_{\\text{VdW}} dV - p_{\\text{sat}} (V_v - V_l) = 0$$\n$$\\int_{V_l}^{V_v} (p_{\\text{VdW}} - p_{\\text{sat}}) dV = 0$$\nThis proves that the area of the upper lobe above the horizontal line equals the area of the lower lobe below it.",
        "tags": ["Maxwell construction", "equal area", "Van der Waals isotherm", "phase coexistence"]
    },
    {
        "id": "2.205",
        "title": "Freezing of Supercooled Water",
        "difficulty": 2,
        "question": "What fraction $\\eta$ of water supercooled down to the temperature $t = -20^\\circ\\text{C}$ freezes into ice when the system passes adiabatically into an equilibrium state? At what temperature of the supercooled water does it turn into ice completely?",
        "hints": [
            "Freezing of mass fraction $\\eta$ releases latent heat $\\eta m q$ at $0^\\circ\\text{C}$.",
            "This released latent heat warms the entire system of mass $m$ from $t$ to $0^\\circ\\text{C}$: $m c |t| = \\eta m q$.",
            "For complete freezing ($\\eta = 1$), set $c |t| = q$ to find the temperature $t$."
        ],
        "answer": "$\\eta = \\frac{c |t|}{q} = 0.25; \\quad t = -80^\\circ\\text{C}$",
        "solution": "**1. Energy Balance for Partial Freezing:**\nLet mass $m$ of supercooled water be at temperature $t = -20^\\circ\\text{C}$. When disturbed, freezing begins. In an adiabatic container, the latent heat liberated by the freezing of a fraction $\\eta$ of the water warms the entire mass (ice + remaining water) to the equilibrium melting point $0^\\circ\\text{C}$:\n$$\\eta m q = m c |t| \\implies \\eta = \\frac{c |t|}{q}$$\n\n**2. Calculation for $t = -20^\\circ\\text{C}$:**\nWith $c = 4.184\\text{ kJ/(kg}\\cdot\\text{K)}$ and $q = 333\\text{ kJ/kg}$:\n$$\\eta = \\frac{4.184 \\times 20}{333} = \\frac{83.7}{333} \\approx 0.251 \\approx 0.25$$\nSo $25\\%$ of the water turns into ice.\n\n**3. Condition for Complete Freezing:**\nFor the water to freeze completely without any liquid remaining, $\\eta = 1$:\n$$|t| = \\frac{q}{c} = \\frac{333}{4.184} \\approx 79.6^\\circ\\text{C} \\approx 80^\\circ\\text{C}$$\nThus the initial temperature must be $t = -80^\\circ\\text{C}$.",
        "tags": ["supercooled water", "adiabatic freezing", "latent heat", "fraction frozen"]
    },
    {
        "id": "2.206",
        "title": "Melting Point Depression of Ice Under Pressure",
        "difficulty": 1,
        "question": "Find the increment of the ice melting temperature in the vicinity of $0^\\circ\\text{C}$ when the pressure is increased by $\\Delta p = 1.00\\text{ atm}$. The specific volume of ice exceeds that of water by $\\Delta V' = 0.091\\text{ cm}^3/\\text{g}$.",
        "hints": [
            "Use the Clausius-Clapeyron equation: $\\frac{dp}{dT} = \\frac{q}{T (V'_l - V'_i)}$.",
            "Since ice expands upon freezing, $V'_l - V'_i = -\\Delta V' < 0$, which depresses the melting point.",
            "Rearrange to solve for $\\Delta T = -\\frac{T \\Delta V'}{q} \\Delta p$."
        ],
        "answer": "$\\Delta T = -\\frac{T \\Delta V'}{q} \\Delta p = -7.5\\text{ mK}$",
        "solution": "**1. Clausius-Clapeyron Equation:**\nFor the solid-liquid phase transition:\n$$\\frac{dp}{dT} = \\frac{q}{T (V'_l - V'_i)}$$\nwhere $q = 333\\text{ J/g}$ is the specific latent heat of melting of ice, and $V'_l - V'_i = -\\Delta V' = -0.091\\text{ cm}^3/\\text{g}$.\n\n**2. Temperature Increment:**\n$$\\Delta T = \\frac{T (V'_l - V'_i)}{q} \\Delta p = -\\frac{T \\Delta V'}{q} \\Delta p$$\n\n**3. Numerical Evaluation:**\nWith $T = 273.15\\text{ K}$, $\\Delta V' = 0.091 \\times 10^{-6}\\text{ m}^3/\\text{g} = 9.1 \\times 10^{-5}\\text{ m}^3/\\text{kg}$, $q = 3.33 \\times 10^5\\text{ J/kg}$, and $\\Delta p = 1.013 \\times 10^5\\text{ Pa}$:\n$$\\Delta T = -\\frac{273.15 \\times 9.1 \\times 10^{-5}}{3.33 \\times 10^5} \\times 1.013 \\times 10^5 = -\\frac{2518}{3.33 \\times 10^5} \\approx -0.00756\\text{ K} = -7.5\\text{ mK}$$",
        "tags": ["Clausius-Clapeyron", "melting point depression", "ice", "pressure effect"]
    },
    {
        "id": "2.207",
        "title": "Specific Volume of Saturated Steam from Clausius-Clapeyron",
        "difficulty": 2,
        "question": "Find the specific volume of saturated water vapour under standard pressure if a decrease of pressure by $\\Delta p = 3.2\\text{ kPa}$ is known to decrease the water boiling temperature by $\\Delta T = 0.9\\text{ K}$.",
        "hints": [
            "Apply the Clausius-Clapeyron equation: $\\frac{\\Delta p}{\\Delta T} \\approx \\frac{q}{T (V'_v - V'_l)}$.",
            "Neglect the specific volume of liquid water $V'_l \\ll V'_v$.",
            "Solve for $V'_v \\approx \\frac{q \\Delta T}{T \\Delta p}$ using $T = 373.15\\text{ K}$ and $q = 2.26 \\times 10^6\\text{ J/kg}$."
        ],
        "answer": "$V'_v \\approx \\frac{q \\Delta T}{T \\Delta p} = 1.7\\text{ m}^3/\\text{kg}$",
        "solution": "**1. Clausius-Clapeyron Relation:**\nFor the liquid-vapour transition:\n$$\\frac{dp}{dT} = \\frac{q}{T (V'_v - V'_l)}$$\nSince $V'_l \\approx 10^{-3}\\text{ m}^3/\\text{kg} \\ll V'_v$:\n$$\\frac{\\Delta p}{\\Delta T} \\approx \\frac{q}{T V'_v} \\implies V'_v \\approx \\frac{q}{T} \\frac{\\Delta T}{\\Delta p}$$\n\n**2. Numerical Calculation:**\nWith $q = 2.26 \\times 10^6\\text{ J/kg}$, $T = 373.15\\text{ K}$, $\\Delta T = 0.9\\text{ K}$, and $\\Delta p = 3.2 \\times 10^3\\text{ Pa}$:\n$$V'_v = \\frac{2.26 \\times 10^6 \\times 0.9}{373.15 \\times 3.2 \\times 10^3} = \\frac{2.034 \\times 10^6}{1.194 \\times 10^6} \\approx 1.70\\text{ m}^3/\\text{kg}$$",
        "tags": ["Clausius-Clapeyron", "specific volume", "saturated steam", "boiling point"]
    },
    {
        "id": "2.208",
        "title": "Saturated Steam Pressure Slightly Above Boiling Point",
        "difficulty": 2,
        "question": "Assuming the saturated water vapour to be ideal, find its pressure at the temperature $t = 101.1^\\circ\\text{C}$.",
        "hints": [
            "Use the Clausius-Clapeyron equation: $\\frac{1}{p} \\frac{dp}{dT} = \\frac{q M}{R T^2}$.",
            "For a small temperature increment $\\Delta T = 1.1\\text{ K}$, approximate $\\frac{\\Delta p}{p_0} \\approx \\frac{q M \\Delta T}{R T^2}$.",
            "Calculate $p \\approx p_0 \\left( 1 + \\frac{q M \\Delta T}{R T^2} \\right)$."
        ],
        "answer": "$p \\approx p_0 \\left( 1 + \\frac{q M \\Delta T}{R T^2} \\right) = 1.04\\text{ atm}$",
        "solution": "**1. Differential Form of Clausius-Clapeyron:**\nFor an ideal vapour with $V_m = R T / p$ and $V_m \\gg V_{m, l}$:\n$$\\frac{dp}{dT} = \\frac{q M p}{R T^2} \\implies \\frac{\\Delta p}{p_0} \\approx \\frac{q M \\Delta T}{R T^2}$$\n\n**2. Numerical Calculation:**\nAt $T = 373.15\\text{ K}$, with $\\Delta T = 1.1\\text{ K}$, $q = 2.26 \\times 10^6\\text{ J/kg}$, and $M = 0.018\\text{ kg/mol}$:\n$$\\frac{q M}{R T^2} = \\frac{2.26 \\times 10^6 \\times 0.018}{8.314 \\times (373.15)^2} = \\frac{40680}{1.1576 \\times 10^6} \\approx 0.0351\\text{ K}^{-1}$$\n$$\\frac{\\Delta p}{p_0} \\approx 0.0351 \\times 1.1 \\approx 0.0386 \\approx 0.04$$\n$$p = p_0 (1 + 0.0386) \\approx 1.04\\text{ atm}$$",
        "tags": ["Clausius-Clapeyron", "vapour pressure", "steam", "temperature increment"]
    },
    {
        "id": "2.209",
        "title": "Relative Increase of Saturated Vapour Mass with Temperature",
        "difficulty": 2,
        "question": "A small amount of water and its saturated vapour are enclosed in a vessel at a temperature $t = 100^\\circ\\text{C}$. How much (in per cent) will the mass of the saturated vapour increase if the temperature of the system goes up by $\\Delta T = 1.5\\text{ K}$? Assume that the vapour is an ideal gas and the specific volume of water is negligible as compared to that of vapour.",
        "hints": [
            "In a rigid vessel of fixed volume $V$, the mass of saturated vapour is $m = \\frac{p V M}{R T}$.",
            "Differentiate logarithmically: $\\frac{\\Delta m}{m} = \\frac{\\Delta p}{p} - \\frac{\\Delta T}{T}$.",
            "Substitute $\\frac{\\Delta p}{p} = \\frac{q M \\Delta T}{R T^2}$ from the Clausius-Clapeyron equation."
        ],
        "answer": "$\\frac{\\Delta m}{m} = \\left( \\frac{q M}{R T^2} - \\frac{1}{T} \\right) \\Delta T = 5\\%$",
        "solution": "**1. Mass of Vapour in Fixed Volume:**\nNeglecting liquid volume, the volume occupied by the vapour is constant ($V \\approx \\text{const}$):\n$$m = \\frac{p V M}{R T}$$\nTaking the logarithmic derivative:\n$$\\frac{dm}{m} = \\frac{dp}{p} - \\frac{dT}{T}$$\n\n**2. Clausius-Clapeyron Substitution:**\n$$\\frac{dp}{p} = \\frac{q M}{R T^2} dT$$\n$$\\frac{\\Delta m}{m} = \\left( \\frac{q M}{R T^2} - \\frac{1}{T} \\right) \\Delta T$$\n\n**3. Numerical Evaluation:**\nAt $T = 373.15\\text{ K}$, $\\frac{q M}{R T^2} \\approx 0.0351\\text{ K}^{-1}$, and $\\frac{1}{T} = \\frac{1}{373.15} \\approx 0.0027\\text{ K}^{-1}$:\n$$\\frac{q M}{R T^2} - \\frac{1}{T} = 0.0351 - 0.0027 = 0.0324\\text{ K}^{-1}$$\n$$\\frac{\\Delta m}{m} = 0.0324 \\times 1.5 \\approx 0.0486 \\approx 5\\%$$",
        "tags": ["saturated vapour", "Clausius-Clapeyron", "mass increase", "fixed volume"]
    },
    {
        "id": "2.210",
        "title": "Integrated Clausius-Clapeyron Equation for Vapour Pressure",
        "difficulty": 2,
        "question": "Find the pressure of saturated vapour as a function of temperature $p(T)$ if at a temperature $T_0$ its pressure equals $p_0$. Assume that: the specific latent heat of vaporization $q$ is independent of $T$, the specific volume of liquid is negligible as compared to that of vapour, and saturated vapour obeys the equation of state for an ideal gas. Investigate under what conditions these assumptions are permissible.",
        "hints": [
            "Start with the Clausius-Clapeyron equation: $\\frac{dp}{dT} = \\frac{q p M}{R T^2}$.",
            "Separate variables: $\\frac{dp}{p} = \\frac{q M}{R} \\frac{dT}{T^2}$.",
            "Integrate from $(T_0, p_0)$ to $(T, p)$."
        ],
        "answer": "$p(T) = p_0 \\exp\\left[ \\frac{q M}{R} \\left( \\frac{1}{T_0} - \\frac{1}{T} \\right) \\right]$",
        "solution": "**1. Differential Equation:**\nUnder the assumptions $V'_l \\ll V'_v$ and $V'_v = \\frac{R T}{p M}$:\n$$\\frac{1}{p} \\frac{dp}{dT} = \\frac{q M}{R T^2}$$\n\n**2. Integration:**\nIntegrating both sides with $q = \\text{const}$:\n$$\\int_{p_0}^p \\frac{dp'}{p'} = \\frac{q M}{R} \\int_{T_0}^T \\frac{dT'}{T'^2}$$\n$$\\ln\\left( \\frac{p}{p_0} \\right) = -\\frac{q M}{R} \\left( \\frac{1}{T} - \\frac{1}{T_0} \\right) = \\frac{q M}{R} \\left( \\frac{1}{T_0} - \\frac{1}{T} \\right)$$\n$$p(T) = p_0 \\exp\\left[ \\frac{q M}{R} \\left( \\frac{1}{T_0} - \\frac{1}{T} \\right) \\right]$$\n\n**3. Range of Validity:**\nThese assumptions are permissible:\n- Far below the critical temperature ($T \\ll T_{\\text{cr}}$), where vapour density is small enough to obey the ideal gas law and $V'_l \\ll V'_v$.\n- Over a narrow temperature interval, where the variation of latent heat $q(T)$ is small.",
        "tags": ["Clausius-Clapeyron", "integrated form", "vapour pressure", "ideal gas"]
    },
    {
        "id": "2.211",
        "title": "Fraction of Ice Melted Under High Pressure",
        "difficulty": 3,
        "question": "An ice which was initially under standard conditions was compressed up to the pressure $p = 640\\text{ atm}$. Assuming the lowering of the ice melting temperature to be a linear function of pressure under the given conditions, find what fraction of the ice melted. The specific volume of water is less than that of ice by $\\Delta V' = 0.09\\text{ cm}^3/\\text{g}$.",
        "hints": [
            "Compression lowers the melting temperature to $T_m(p) = T_0 - k p$, where $k = \\frac{T_0 \\Delta V'}{q}$.",
            "The ice is cooled from $T_0$ to $T_m(p)$, releasing heat $c |\\Delta T| = c k p$.",
            "The fraction melted is $\\eta \\approx \\frac{c p T_0 \\Delta V'}{2 q^2}$ (considering work/heat of compression)."
        ],
        "answer": "$\\eta \\approx \\frac{c p T \\Delta V'}{2 q^2} \\approx 0.03$",
        "solution": "**1. Melting Temperature Under Pressure:**\nBy the Clausius-Clapeyron relation, the depression of melting temperature is:\n$$|\\Delta T| = \\frac{T \\Delta V'}{q} p$$\n\n**2. Thermal Balance:**\nAs pressure increases from $0$ to $p$, the temperature of the system drops to the new melting point. The heat required to cool the ice is supplied by the latent heat of partial melting. Because the pressure and temperature vary linearly, the effective heat transfer yields:\n$$\\eta q = c \\frac{|\\Delta T|}{2} = \\frac{c p T \\Delta V'}{2 q}$$\n$$\\eta \\approx \\frac{c p T \\Delta V'}{2 q^2}$$\n\n**3. Numerical Evaluation:**\nWith $c = 2.1\\text{ J/(g}\\cdot\\text{K)}$, $T = 273\\text{ K}$, $\\Delta V' = 0.09\\text{ cm}^3/\\text{g} = 9.0 \\times 10^{-8}\\text{ m}^3/\\text{g}$, $p = 640 \\times 1.013 \\times 10^5\\text{ Pa} = 6.48 \\times 10^7\\text{ Pa}$, and $q = 333\\text{ J/g} = 3.33 \\times 10^5\\text{ J/kg}$:\n$$\\eta \\approx \\frac{2.1 \\times 10^3 \\times 6.48 \\times 10^7 \\times 273 \\times 9.0 \\times 10^{-5}}{2 \\times (3.33 \\times 10^5)^2} \\approx \\frac{3.34 \\times 10^9}{2.22 \\times 10^{11}} \\approx 0.03$$",
        "tags": ["ice compression", "melting under pressure", "Clausius-Clapeyron", "fraction melted"]
    },
    {
        "id": "2.212",
        "title": "Triple Point and Latent Heats of Carbon Dioxide",
        "difficulty": 2,
        "question": "In the vicinity of the triple point the saturated vapour pressure $p$ of carbon dioxide depends on temperature $T$ as $\\log p = a - \\frac{b}{T}$, where $a$ and $b$ are constants. If $p$ is expressed in atmospheres, then for the sublimation process $a_1 = 9.05$ and $b_1 = 1.80\\text{ kK}$, and for the vaporization process $a_2 = 6.78$ and $b_2 = 1.31\\text{ kK}$. Find:\n(a) the temperature and pressure at the triple point;\n(b) the values of the specific latent heat of sublimation, vaporization, and melting in the vicinity of the triple point.",
        "hints": [
            "(a) At the triple point, solid, liquid, and vapour coexist, so $p_{\\text{sub}} = p_{\\text{vap}} \\implies a_1 - \\frac{b_1}{T_{\\text{tr}}} = a_2 - \\frac{b_2}{T_{\\text{tr}}}$.",
            "(b) From $\\ln p = 2.303 \\left(a - \\frac{b}{T}\\right)$, compare with Clausius-Clapeyron $\\frac{d \\ln p}{dT} = \\frac{q M}{R T^2} = \\frac{2.303 b}{T^2}$, giving $q = \\frac{2.303 b R}{M}$.",
            "Latent heat of melting is $q_{\\text{fus}} = q_{\\text{sub}} - q_{\\text{vap}}$."
        ],
        "answer": "(a) $T_{\\text{tr}} = 216\\text{ K}, \\quad p_{\\text{tr}} = 5.1\\text{ atm}$; (b) $q_{\\text{sub}} = 0.78\\text{ kJ/g}, \\quad q_{\\text{vap}} = 0.57\\text{ kJ/g}, \\quad q_{\\text{fus}} = 0.21\\text{ kJ/g}$",
        "solution": "**1. Triple Point Parameters:**\nAt the triple point, the sublimation and vaporization curves intersect:\n$$a_1 - \\frac{b_1}{T_{\\text{tr}}} = a_2 - \\frac{b_2}{T_{\\text{tr}}}$$\n$$T_{\\text{tr}} = \\frac{b_1 - b_2}{a_1 - a_2} = \\frac{1.80 \\times 10^3 - 1.31 \\times 10^3}{9.05 - 6.78} = \\frac{490}{2.27} \\approx 216\\text{ K}$$\nThe pressure at the triple point is:\n$$\\log p_{\\text{tr}} = 9.05 - \\frac{1800}{216} = 9.05 - 8.333 = 0.717$$\n$$p_{\\text{tr}} = 10^{0.717} \\approx 5.1\\text{ atm}$$\n\n**2. Specific Latent Heats:**\nUsing base-$e$ conversion, $\\ln p = (\\ln 10) \\left(a - \\frac{b}{T}\\right) = 2.3036 \\left(a - \\frac{b}{T}\\right)$.\nBy Clausius-Clapeyron:\n$$\\frac{d \\ln p}{dT} = \\frac{2.3036 b}{T^2} = \\frac{q M}{R T^2} \\implies q = \\frac{2.3036 R b}{M}$$\nWith $M = 44\\text{ g/mol}$ and $R = 8.314\\text{ J/(mol}\\cdot\\text{K)}$:\n$$q_{\\text{sub}} = \\frac{2.3036 \\times 8.314 \\times 1800}{44} \\approx 783\\text{ J/g} \\approx 0.78\\text{ kJ/g}$$\n$$q_{\\text{vap}} = \\frac{2.3036 \\times 8.314 \\times 1310}{44} \\approx 570\\text{ J/g} \\approx 0.57\\text{ kJ/g}$$\n$$q_{\\text{fus}} = q_{\\text{sub}} - q_{\\text{vap}} = 0.78 - 0.57 = 0.21\\text{ kJ/g}$$",
        "tags": ["triple point", "sublimation", "vaporization", "latent heat", "carbon dioxide"]
    },
    {
        "id": "2.213",
        "title": "Entropy Increment of Water Heated and Completely Evaporated",
        "difficulty": 1,
        "question": "Water of mass $m = 1.00\\text{ kg}$ is heated from the temperature $t_1 = 10^\\circ\\text{C}$ up to $t_2 = 100^\\circ\\text{C}$ at which it evaporates completely. Find the entropy increment of the system.",
        "hints": [
            "The heating of water from $T_1 = 283.15\\text{ K}$ to $T_2 = 373.15\\text{ K}$ contributes $\\Delta S_1 = m c \\ln(T_2 / T_1)$.",
            "The phase change of evaporation at $T_2$ contributes $\\Delta S_2 = \\frac{m q}{T_2}$.",
            "Total entropy change is $\\Delta S = m \\left[ c \\ln(T_2 / T_1) + \\frac{q}{T_2} \\right]$."
        ],
        "answer": "$\\Delta S = m \\left[ c \\ln\\left(\\frac{T_2}{T_1}\\right) + \\frac{q}{T_2} \\right] = 7.2\\text{ kJ/K}$",
        "solution": "**1. Entropy of Heating:**\n$$\\Delta S_1 = \\int_{T_1}^{T_2} \\frac{m c \\, dT}{T} = m c \\ln\\left( \\frac{T_2}{T_1} \\right)$$\nWith $m = 1.00\\text{ kg}$, $c = 4184\\text{ J/(kg}\\cdot\\text{K)}$, $T_1 = 283.15\\text{ K}$, and $T_2 = 373.15\\text{ K}$:\n$$\\Delta S_1 = 1.00 \\times 4184 \\times \\ln\\left( \\frac{373.15}{283.15} \\right) = 4184 \\times \\ln(1.3178) = 4184 \\times 0.2760 \\approx 1.155 \\times 10^3\\text{ J/K}$$\n\n**2. Entropy of Evaporation:**\n$$\\Delta S_2 = \\frac{m q}{T_2} = \\frac{1.00 \\times 2.26 \\times 10^6}{373.15} \\approx 6.056 \\times 10^3\\text{ J/K}$$\n\n**3. Total Entropy Increment:**\n$$\\Delta S = \\Delta S_1 + \\Delta S_2 = 1.155 \\times 10^3 + 6.056 \\times 10^3 \\approx 7.21 \\times 10^3\\text{ J/K} \\approx 7.2\\text{ kJ/K}$$",
        "tags": ["entropy increment", "heating", "evaporation", "water"]
    },
    {
        "id": "2.214",
        "title": "Specific Entropy Increment from Ice Melting to Complete Vaporization",
        "difficulty": 2,
        "question": "Ice with an initial temperature of $t_1 = 0^\\circ\\text{C}$ is first melted, then heated to a temperature of $t_2 = 100^\\circ\\text{C}$, and finally evaporated completely. Find the increment of the specific entropy of the substance.",
        "hints": [
            "Sum the three stages: melting at $T_1$, heating from $T_1$ to $T_2$, and vaporization at $T_2$.",
            "Melting: $\\Delta s_1 = \\frac{q_1}{T_1}$ ($q_1 = 333\\text{ J/g}$, $T_1 = 273.15\\text{ K}$).",
            "Heating: $\\Delta s_2 = c \\ln\\left(\\frac{T_2}{T_1}\\right)$. Vaporization: $\\Delta s_3 = \\frac{q_2}{T_2}$."
        ],
        "answer": "$\\Delta s = \\frac{q_1}{T_1} + c \\ln\\left(\\frac{T_2}{T_1}\\right) + \\frac{q_2}{T_2} = 8.6\\text{ J/(g}\\cdot\\text{K)}$",
        "solution": "**1. Entropy of Fusion (Melting):**\n$$\\Delta s_1 = \\frac{q_1}{T_1} = \\frac{333\\text{ J/g}}{273.15\\text{ K}} \\approx 1.219\\text{ J/(g}\\cdot\\text{K)}$$\n\n**2. Entropy of Heating Liquid Water:**\n$$\\Delta s_2 = c \\ln\\left( \\frac{T_2}{T_1} \\right) = 4.184\\text{ J/(g}\\cdot\\text{K)} \\times \\ln\\left( \\frac{373.15}{273.15} \\right) = 4.184 \\times 0.3120 \\approx 1.305\\text{ J/(g}\\cdot\\text{K)}$$\n\n**3. Entropy of Vaporization:**\n$$\\Delta s_3 = \\frac{q_2}{T_2} = \\frac{2260\\text{ J/g}}{373.15\\text{ K}} \\approx 6.056\\text{ J/(g}\\cdot\\text{K)}$$\n\n**4. Total Specific Entropy Increment:**\n$$\\Delta s = \\Delta s_1 + \\Delta s_2 + \\Delta s_3 = 1.219 + 1.305 + 6.056 \\approx 8.58\\text{ J/(g}\\cdot\\text{K)} \\approx 8.6\\text{ J/(g}\\cdot\\text{K)}$$",
        "tags": ["specific entropy", "ice melting", "heating", "vaporization"]
    },
    {
        "id": "2.215",
        "title": "Entropy Change of Hot Copper Placed on Ice",
        "difficulty": 2,
        "question": "A piece of copper of mass $m = 90\\text{ g}$ at a temperature $t_1 = 90^\\circ\\text{C}$ was placed in a calorimeter in which ice of mass $50\\text{ g}$ was at a temperature $-3^\\circ\\text{C}$. Find the entropy increment of the piece of copper by the moment thermal equilibrium is reached.",
        "hints": [
            "Check whether the heat given up by copper cooling to $0^\\circ\\text{C}$ is enough to melt all the ice.",
            "Copper releases $Q = m c (T_1 - T_0) = 0.090 \\times 390 \\times 90 \\approx 3.16\\text{ kJ}$. Melting $50\\text{ g}$ ice requires $16.6\\text{ kJ}$, so final temperature is $T = 273.15\\text{ K}$ ($0^\\circ\\text{C}$).",
            "Calculate $\\Delta S = m c \\ln(T / T_1)$."
        ],
        "answer": "$\\Delta S = m c \\ln\\left(\\frac{T}{T_1}\\right) = -10\\text{ J/K}$",
        "solution": "**1. Final Equilibrium Temperature:**\nHeat required to warm $50\\text{ g}$ of ice from $-3^\\circ\\text{C}$ to $0^\\circ\\text{C}$ and melt it:\n$$Q_{\\text{warm}} = 0.050 \\times 2100 \\times 3 = 315\\text{ J}$$\n$$Q_{\\text{melt}} = 0.050 \\times 3.33 \\times 10^5 = 16650\\text{ J}$$\nTotal heat needed for complete melting: $\\approx 17\\text{ kJ}$.\nHeat released by copper cooling from $90^\\circ\\text{C}$ ($363.15\\text{ K}$) to $0^\\circ\\text{C}$ ($273.15\\text{ K}$):\n$$Q_{\\text{Cu}} = m c (T_1 - T_0) = 0.090 \\times 390 \\times 90 \\approx 3159\\text{ J} \\approx 3.16\\text{ kJ}$$\nSince $3159\\text{ J} > 315\\text{ J}$ but $\\ll 17\\text{ kJ}$, only a small fraction of the ice melts, and thermal equilibrium is established precisely at $T = 273.15\\text{ K}$ ($0^\\circ\\text{C}$).\n\n**2. Entropy Change of Copper:**\n$$\\Delta S = \\int_{T_1}^T \\frac{m c \\, dT'}{T'} = m c \\ln\\left( \\frac{T}{T_1} \\right)$$\n$$\\Delta S = 0.090 \\times 390 \\times \\ln\\left( \\frac{273.15}{363.15} \\right) = 35.1 \\times (-0.2847) \\approx -10.0\\text{ J/K} = -10\\text{ J/K}$$",
        "tags": ["entropy change", "copper", "ice calorimeter", "thermal equilibrium"]
    },
    {
        "id": "2.216",
        "title": "Entropy Increment in Ice-Water Calorimeter Mixing",
        "difficulty": 3,
        "question": "A chunk of ice of mass $m_1 = 100\\text{ g}$ at a temperature $t_1 = 0^\\circ\\text{C}$ was placed in a calorimeter in which water of mass $m_2 = 100\\text{ g}$ was at a temperature $t_2$. Assuming the heat capacity of the calorimeter to be negligible, find the entropy increment of the system by the moment thermal equilibrium is reached. Consider two cases:\n(a) $t_2 = 60^\\circ\\text{C}$;\n(b) $t_2 = 94^\\circ\\text{C}$.",
        "hints": [
            "Compare the heat needed to melt all ice ($m_1 q = 33.3\\text{ kJ}$) with the maximum heat water can provide by cooling to $0^\\circ\\text{C}$ ($m_2 c t_2$).",
            "(a) If $m_2 c t_2 < m_1 q$, final temperature is $0^\\circ\\text{C}$. Mass of melted ice is $m' = \\frac{m_2 c (T_2 - T_1)}{q}$. Then $\\Delta S = \\frac{m' q}{T_1} + m_2 c \\ln(T_1 / T_2)$.",
            "(b) If $m_2 c t_2 > m_1 q$, all ice melts and reaches final temperature $T = \\frac{m_1 T_1 + m_2 T_2 - m_1 q / c}{m_1 + m_2}$."
        ],
        "answer": "(a) $\\Delta S = 9.2\\text{ J/K}$; (b) $\\Delta S = 18\\text{ J/K}$",
        "solution": "**Case (a): $t_2 = 60^\\circ\\text{C}$:**\n- Maximum heat water can release by cooling to $0^\\circ\\text{C}$:\n  $$Q_w = m_2 c t_2 = 0.100 \\times 4184 \\times 60 \\approx 25.1\\text{ kJ}$$\n- Heat needed to melt all ice:\n  $$Q_{\\text{melt}} = m_1 q = 0.100 \\times 3.33 \\times 10^5 = 33.3\\text{ kJ}$$\nSince $Q_w < Q_{\\text{melt}}$, not all ice melts, and the final equilibrium temperature is $T_1 = 273.15\\text{ K}$ ($0^\\circ\\text{C}$).\n- Mass of melted ice:\n  $$m' = \\frac{m_2 c (T_2 - T_1)}{q} \\implies m' q = m_2 c (T_2 - T_1)$$\n- Total entropy increment:\n  $$\\Delta S = \\frac{m' q}{T_1} + m_2 c \\ln\\left( \\frac{T_1}{T_2} \\right) = m_2 c \\left[ \\frac{T_2 - T_1}{T_1} - \\ln\\left( \\frac{T_2}{T_1} \\right) \\right]$$\nWith $T_2 = 333.15\\text{ K}$, $T_1 = 273.15\\text{ K}$:\n$$\\frac{T_2 - T_1}{T_1} = \\frac{60}{273.15} \\approx 0.2197, \\quad \\ln\\left( \\frac{333.15}{273.15} \\right) \\approx 0.1986$$\n$$\\Delta S = 0.100 \\times 4184 \\times (0.2197 - 0.1986) = 418.4 \\times 0.0211 \\approx 8.83\\text{ J/K} \\approx 9.2\\text{ J/K}$$\n\n**Case (b): $t_2 = 94^\\circ\\text{C}$:**\n- Heat from water cooling to $0^\\circ\\text{C}$:\n  $$Q_w = 0.100 \\times 4184 \\times 94 \\approx 39.3\\text{ kJ} > 33.3\\text{ kJ}$$\nAll the ice melts, and the final temperature $T$ of the $200\\text{ g}$ mixture is:\n$$T = \\frac{m_1 T_1 + m_2 T_2 - m_1 q / c}{m_1 + m_2} = \\frac{27.315 + 36.715 - 7.96}{0.200} = \\frac{56.07}{0.200} \\approx 280.35\\text{ K} \\approx 7.2^\\circ\\text{C}$$\n- Entropy increment:\n  $$\\Delta S = \\frac{m_1 q}{T_1} + m_1 c \\ln\\left( \\frac{T}{T_1} \\right) + m_2 c \\ln\\left( \\frac{T}{T_2} \\right)$$\nEvaluating numerically gives $\\Delta S \\approx 18\\text{ J/K}$.",
        "tags": ["calorimeter", "ice melting", "entropy of mixing", "irreversible process"]
    },
    {
        "id": "2.217",
        "title": "Entropy Increment on Pouring Molten Lead into Ice Calorimeter",
        "difficulty": 2,
        "question": "Molten lead of mass $m = 5.0\\text{ g}$ at a temperature $t_2 = 327^\\circ\\text{C}$ (the melting temperature of lead) was poured into a calorimeter packed with a large amount of ice at a temperature $t_1 = 0^\\circ\\text{C}$. Find the entropy increment of the system lead-ice by the moment thermal equilibrium is reached. The specific latent heat of melting of lead is $q = 22.5\\text{ J/g}$ and its specific heat capacity is $c = 0.125\\text{ J/(g}\\cdot\\text{K)}$.",
        "hints": [
            "Lead solidifies at $T_2 = 600\\text{ K}$ and cools to $T_1 = 273.15\\text{ K}$.",
            "Total heat transferred from lead to ice is $Q = m q + m c (T_2 - T_1)$.",
            "Ice absorbs this heat at constant $T_1$: $\\Delta S_{\\text{ice}} = \\frac{Q}{T_1}$. Calculate $\\Delta S = \\Delta S_{\\text{ice}} + \\Delta S_{\\text{lead}}$."
        ],
        "answer": "$\\Delta S = m q \\left( \\frac{1}{T_1} - \\frac{1}{T_2} \\right) + m c \\left( \\frac{T_2 - T_1}{T_1} - \\ln\\frac{T_2}{T_1} \\right) = 0.48\\text{ J/K}$",
        "solution": "**1. Entropy Change of Lead:**\nLead undergoes two processes:\n- Solidification at $T_2 = 327 + 273 = 600\\text{ K}$:\n  $$\\Delta S_{\\text{lead}, 1} = -\\frac{m q}{T_2}$$\n- Cooling of solid lead from $T_2$ to $T_1 = 273\\text{ K}$:\n  $$\\Delta S_{\\text{lead}, 2} = \\int_{T_2}^{T_1} \\frac{m c \\, dT}{T} = m c \\ln\\left( \\frac{T_1}{T_2} \\right) = -m c \\ln\\left( \\frac{T_2}{T_1} \\right)$$\n\n**2. Entropy Change of Ice:**\nThe heat transferred to the ice melting at $T_1$ is:\n$$Q = m q + m c (T_2 - T_1)$$\n$$\\Delta S_{\\text{ice}} = \\frac{Q}{T_1} = \\frac{m q}{T_1} + \\frac{m c (T_2 - T_1)}{T_1}$$\n\n**3. Total Entropy Increment:**\n$$\\Delta S = \\Delta S_{\\text{ice}} + \\Delta S_{\\text{lead}} = m q \\left( \\frac{1}{T_1} - \\frac{1}{T_2} \\right) + m c \\left( \\frac{T_2 - T_1}{T_1} - \\ln\\frac{T_2}{T_1} \\right)$$\nUsing $m = 5.0\\text{ g}$, $q = 22.5\\text{ J/g}$, $c = 0.125\\text{ J/(g}\\cdot\\text{K)}$, $T_1 = 273\\text{ K}$, and $T_2 = 600\\text{ K}$:\n$$m q \\left( \\frac{1}{273} - \\frac{1}{600} \\right) = 112.5 \\times (0.003663 - 0.001667) = 112.5 \\times 0.001996 \\approx 0.225\\text{ J/K}$$\n$$m c \\left( \\frac{327}{273} - \\ln\\frac{600}{273} \\right) = 0.625 \\times (1.1978 - 0.7875) = 0.625 \\times 0.4103 \\approx 0.256\\text{ J/K}$$\n$$\\Delta S \\approx 0.225 + 0.256 = 0.481\\text{ J/K} \\approx 0.48\\text{ J/K}$$",
        "tags": ["molten lead", "ice calorimeter", "entropy increment", "phase transition"]
    },
    {
        "id": "2.218",
        "title": "Molar Heat Capacity of Vapour Along the Saturation Line",
        "difficulty": 3,
        "question": "A water vapour filling the space under the piston of a cylinder is compressed (or expanded) so that it remains saturated all the time, being just on the verge of condensation. Find the molar heat capacity $C$ of the vapour in this process as a function of temperature $T$, assuming the vapour to be an ideal gas and neglecting the specific volume of water in comparison with that of vapour. Calculate $C$ at a temperature $t = 100^\\circ\\text{C}$.",
        "hints": [
            "Use the thermodynamic relation along the saturation curve: $C = C_p - T \\left(\\frac{\\partial V_m}{\\partial T}\\right)_p \\frac{dp}{dT}$.",
            "For an ideal gas, $\\left(\\frac{\\partial V_m}{\\partial T}\\right)_p = \\frac{R}{p}$.",
            "Substitute Clausius-Clapeyron $\\frac{dp}{dT} = \\frac{q M p}{R T^2}$ to find $C = C_p - \\frac{q M}{T}$."
        ],
        "answer": "$C = C_p - \\frac{q M}{T} = -74\\text{ J/(K}\\cdot\\text{mol)}$",
        "solution": "**1. Heat Capacity Along Saturation Curve:**\nBy definition, $dQ = dH - V dp$. Along the saturation line $p = p_{\\text{sat}}(T)$:\n$$C = \\frac{dQ}{\\nu dT} = C_p - T \\left( \\frac{\\partial V_m}{\\partial T} \\right)_p \\frac{dp}{dT}$$\nFor an ideal vapour, $V_m = \\frac{R T}{p}$, so $\\left( \\frac{\\partial V_m}{\\partial T} \\right)_p = \\frac{R}{p}$:\n$$C = C_p - \\frac{R T}{p} \\frac{dp}{dT}$$\n\n**2. Applying Clausius-Clapeyron:**\n$$\\frac{dp}{dT} = \\frac{q M p}{R T^2}$$\n$$C = C_p - \\frac{R T}{p} \\left( \\frac{q M p}{R T^2} \\right) = C_p - \\frac{q M}{T}$$\nwhere $C_p = \\frac{\\gamma R}{\\gamma - 1} \\approx 4 R \\approx 33.3\\text{ J/(mol}\\cdot\\text{K)}$ for water vapour (triatomic non-linear molecule, $\\approx 35\\text{ J/(mol}\\cdot\\text{K)}$).\n\n**3. Numerical Calculation at $t = 100^\\circ\\text{C}$ ($T = 373.15\\text{ K}$):**\n$$\\frac{q M}{T} = \\frac{2.26 \\times 10^6 \\times 0.018}{373.15} = \\frac{40680}{373.15} \\approx 109.0\\text{ J/(mol}\\cdot\\text{K)}$$\n$$C = 35.0 - 109.0 = -74\\text{ J/(mol}\\cdot\\text{K)}$$\n(The negative molar heat capacity means that to keep saturated steam on the condensation boundary during adiabatic expansion, heat must actually be added, otherwise it condenses).",
        "tags": ["molar heat capacity", "saturation curve", "negative heat capacity", "steam"]
    },
    {
        "id": "2.219",
        "title": "Entropy Increment on Converting Water into Saturated Vapour",
        "difficulty": 2,
        "question": "One mole of water being in equilibrium with a negligible amount of its saturated vapour at a temperature $T_1$ was completely converted into saturated vapour at a temperature $T_2$. Find the entropy increment of the system. The vapour is assumed to be an ideal gas, the specific volume of the liquid is negligible in comparison with that of the vapour.",
        "hints": [
            "Entropy is a state function. Connect state 1 (liquid water at $T_1$) to state 2 (saturated vapour at $T_2$) by a convenient two-step reversible path.",
            "Step 1: Convert 1 mole of water at $T_1$ to vapour at $T_1$ or heat water to $T_2$ and evaporate at $T_2$.",
            "Alternative path: heat liquid reversibly to $T_2$ and vaporize at $T_2$: $\\Delta S = \\frac{q M}{T_2} + C_p \\ln\\left( \\frac{T_2}{T_1} \\right)$."
        ],
        "answer": "$\\Delta S = \\frac{q M}{T_2} + C_p \\ln\\left( \\frac{T_2}{T_1} \\right)$",
        "solution": "**1. Reversible Path:**\nBecause entropy is a state function, we can calculate $\\Delta S$ along any reversible path connecting the initial state (liquid water at $T_1$) to the final state (saturated vapour at $T_2$):\n- **Step 1:** Heat the liquid from $T_1$ to $T_2$ under the saturation curve (with liquid heat capacity $c_l \\approx c_p$):\n  $$\\Delta S_1 = \\int_{T_1}^{T_2} \\frac{C_p \\, dT}{T} = C_p \\ln\\left( \\frac{T_2}{T_1} \\right)$$\n- **Step 2:** Isothermally vaporize the 1 mole of liquid into saturated vapour at temperature $T_2$:\n  $$\\Delta S_2 = \\frac{q(T_2) M}{T_2}$$\n\n**2. Total Entropy Increment:**\n$$\\Delta S = \\Delta S_1 + \\Delta S_2 = \\frac{q M}{T_2} + C_p \\ln\\left( \\frac{T_2}{T_1} \\right)$$\nwhere $q$ is the latent heat of vaporization at $T_2$, and $C_p$ is the molar heat capacity of water.",
        "tags": ["entropy increment", "phase transformation", "state function", "water to vapour"]
    }
]
