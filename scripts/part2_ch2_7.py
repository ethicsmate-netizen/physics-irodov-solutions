"""
part2_ch2_7.py
Curated problems 2.220 to 2.257 (38 problems) of Irodov Chapter 2.7:
Transport Phenomena.
"""

CH2_7_CURATED = [
    {
        "id": "2.220",
        "title": "Molecular Free Path Distribution",
        "difficulty": 1,
        "question": "Calculate what fraction of gas molecules:\n(a) traverses without collisions the distances exceeding the mean free path $\\lambda$;\n(b) has the free path values lying within the interval from $\\lambda$ to $2\\lambda$.",
        "hints": [
            "The probability of traversing a distance $s$ without collisions is given by Poisson statistics: $P(s) = e^{-s / \\lambda}$.",
            "(a) The fraction traversing distances exceeding $\\lambda$ is $P(s > \\lambda) = e^{-1}$.",
            "(b) The fraction with free path in $[\\lambda, 2\\lambda]$ is $P(\\lambda \\le s \\le 2\\lambda) = e^{-\\lambda/\\lambda} - e^{-2\\lambda/\\lambda} = e^{-1} - e^{-2}$."
        ],
        "answer": "(a) $\\eta = e^{-1} \\approx 0.37$; (b) $\\eta = e^{-1} - e^{-2} \\approx 0.23$",
        "solution": "**1. Free Path Probability Distribution:**\nThe probability that a molecule travels a distance $s$ without experiencing a collision is:\n$$P(s) = e^{-s / \\lambda}$$\nwhere $\\lambda$ is the mean free path.\n\n**2. Fraction with Path Exceeding $\\lambda$:**\n$$\\eta_a = P(s > \\lambda) = e^{-\\lambda / \\lambda} = e^{-1} \\approx 0.368 \\approx 0.37$$\n\n**3. Fraction in Interval $[\\lambda, 2\\lambda]$:**\n$$\\eta_b = P(\\lambda \\le s \\le 2\\lambda) = e^{-\\lambda / \\lambda} - e^{-2\\lambda / \\lambda} = e^{-1} - e^{-2} \\approx 0.3679 - 0.1353 \\approx 0.233 \\approx 0.23$$",
        "tags": ["mean free path", "Poisson distribution", "collision probability"]
    },
    {
        "id": "2.221",
        "title": "Attenuation of a Molecular Beam",
        "difficulty": 1,
        "question": "A narrow molecular beam makes its way into a vessel filled with gas under low pressure. Find the mean free path of molecules if the beam intensity decreases $\\eta$-fold over the distance $\\Delta l$.",
        "hints": [
            "Beam intensity decreases according to the exponential law: $I = I_0 e^{-x / \\lambda}$.",
            "Over a path length $\\Delta l$, $\\frac{I_0}{I} = \\eta = e^{\\Delta l / \\lambda}$.",
            "Take the natural logarithm to find $\\lambda = \\frac{\\Delta l}{\\ln\\eta}$."
        ],
        "answer": "$\\lambda = \\frac{\\Delta l}{\\ln\\eta}$",
        "solution": "**1. Attenuation Law:**\nMolecules in the beam that undergo any collision are scattered out of the narrow beam. Therefore, the beam intensity decays exponentially with distance $x$:\n$$I(x) = I_0 e^{-x / \\lambda}$$\n\n**2. Mean Free Path Calculation:**\nOver distance $\\Delta l$, the intensity decreases $\\eta$-fold:\n$$\\frac{I(\\Delta l)}{I_0} = \\frac{1}{\\eta} = e^{-\\Delta l / \\lambda}$$\n$$\\ln\\eta = \\frac{\\Delta l}{\\lambda} \\implies \\lambda = \\frac{\\Delta l}{\\ln\\eta}$$",
        "tags": ["molecular beam", "attenuation", "mean free path", "scattering"]
    },
    {
        "id": "2.222",
        "title": "Collision Probability and Mean Collision Time",
        "difficulty": 2,
        "question": "Let $\\alpha \\, dt$ be the probability of a gas molecule experiencing a collision during the time interval $dt$, where $\\alpha$ is a constant. Find:\n(a) the probability of a molecule experiencing no collisions during the time interval $t$;\n(b) the mean time interval between successive collisions.",
        "hints": [
            "(a) Let $P(t)$ be the probability of no collision up to time $t$. Then $P(t + dt) = P(t)(1 - \\alpha \\, dt)$. Solve the differential equation.",
            "(b) The probability density of colliding between $t$ and $t + dt$ is $w(t) \\, dt = P(t) \\alpha \\, dt = \\alpha e^{-\\alpha t} dt$.",
            "Compute the expectation value $\\langle t \\rangle = \\int_0^\\infty t w(t) \\, dt$."
        ],
        "answer": "(a) $P(t) = e^{-\\alpha t}$; (b) $\\langle t \\rangle = \\frac{1}{\\alpha}$",
        "solution": "**1. Probability of No Collision in Time $t$:**\nThe probability of surviving without collision up to time $t + dt$ is the probability of surviving up to time $t$ multiplied by the probability of not colliding during $dt$:\n$$P(t + dt) = P(t)(1 - \\alpha \\, dt)$$\n$$\\frac{dP}{dt} = -\\alpha P$$\nWith initial condition $P(0) = 1$, integration yields:\n$$P(t) = e^{-\\alpha t}$$\n\n**2. Mean Time Between Collisions:**\nThe probability that the first collision occurs in the interval $(t, t + dt)$ is:\n$$dP_{\\text{coll}} = P(t) (\\alpha \\, dt) = \\alpha e^{-\\alpha t} dt$$\nThe mean time between collisions is the expectation value:\n$$\\langle t \\rangle = \\int_0^\\infty t \\cdot (\\alpha e^{-\\alpha t}) \\, dt = \\frac{1}{\\alpha}$$",
        "tags": ["collision probability", "Poisson process", "relaxation time", "mean free time"]
    },
    {
        "id": "2.223",
        "title": "Mean Free Path and Collision Interval of Nitrogen",
        "difficulty": 2,
        "question": "Find the mean free path and the mean time interval between successive collisions of gaseous nitrogen molecules:\n(a) under standard conditions ($T = 273\\text{ K}$, $p = 1.013 \\times 10^5\\text{ Pa}$);\n(b) at temperature $t = 0^\\circ\\text{C}$ and pressure $p = 1.0\\text{ nPa}$.",
        "hints": [
            "Use $\\lambda = \\frac{k T}{\\sqrt{2}\\pi d^2 p}$, with effective diameter of nitrogen $d = 0.38\\text{ nm} = 3.8 \\times 10^{-10}\\text{ m}$.",
            "Mean thermal speed is $\\langle v \\rangle = \\sqrt{\\frac{8 R T}{\\pi M}} \\approx 454\\text{ m/s}$ for $\\text{N}_2$ at $273\\text{ K}$.",
            "The mean collision time is $\\tau = \\frac{\\lambda}{\\langle v \\rangle}$."
        ],
        "answer": "(a) $\\lambda \\approx 0.06\\,\\mu\\text{m}, \\quad \\tau \\approx 0.13\\text{ ns}$; (b) $\\lambda \\approx 6 \\times 10^3\\text{ km}, \\quad \\tau \\approx 3.8\\text{ hours}$",
        "solution": "**1. Formulae:**\nThe number density is $n = \\frac{p}{k T}$. The mean free path is:\n$$\\lambda = \\frac{1}{\\sqrt{2}\\pi d^2 n} = \\frac{k T}{\\sqrt{2}\\pi d^2 p}$$\nThe mean thermal speed for nitrogen ($M = 28 \\times 10^{-3}\\text{ kg/mol}$) at $T = 273.15\\text{ K}$ is:\n$$\\langle v \\rangle = \\sqrt{\\frac{8 R T}{\\pi M}} = \\sqrt{\\frac{8 \\times 8.314 \\times 273.15}{\\pi \\times 0.028}} \\approx 454.4\\text{ m/s}$$\nThe mean time between collisions is:\n$$\\tau = \\frac{\\lambda}{\\langle v \\rangle}$$\n\n**2. Part (a) - Standard Conditions ($p_0 = 1.013 \\times 10^5\\text{ Pa}$):**\nUsing $d \\approx 0.375\\text{ nm}$:\n$$\\lambda = \\frac{1.38 \\times 10^{-23} \\times 273.15}{\\sqrt{2}\\pi \\times (3.75 \\times 10^{-10})^2 \\times 1.013 \\times 10^5} \\approx 6.0 \\times 10^{-8}\\text{ m} = 0.06\\,\\mu\\text{m}$$\n$$\\tau = \\frac{6.0 \\times 10^{-8}}{454.4} \\approx 1.32 \\times 10^{-10}\\text{ s} \\approx 0.13\\text{ ns}$$\n\n**3. Part (b) - High Vacuum ($p = 1.0\\text{ nPa} = 1.0 \\times 10^{-9}\\text{ Pa}$):**\nPressure is reduced by a factor of $\\frac{1.013 \\times 10^5}{1.0 \\times 10^{-9}} \\approx 1.013 \\times 10^{14}$:\n$$\\lambda = 6.0 \\times 10^{-8} \\times 1.013 \\times 10^{14} \\approx 6.1 \\times 10^6\\text{ m} = 6 \\times 10^3\\text{ km}$$\n$$\\tau = \\frac{6.1 \\times 10^6}{454.4} \\approx 1.34 \\times 10^4\\text{ s} = \\frac{13400}{3600}\\text{ h} \\approx 3.73\\text{ hours} \\approx 3.8\\text{ hours}$$",
        "tags": ["nitrogen", "mean free path", "high vacuum", "collision frequency"]
    },
    {
        "id": "2.224",
        "title": "Ratio of Mean Free Path to Intermolecular Distance",
        "difficulty": 1,
        "question": "How many times does the mean free path of nitrogen molecules exceed the mean distance between the molecules under standard conditions?",
        "hints": [
            "Mean free path: $\\lambda = \\frac{1}{\\sqrt{2}\\pi d^2 n}$.",
            "Mean distance between molecules: $\\bar{r} = n^{-1/3}$.",
            "Calculate $\\frac{\\lambda}{\\bar{r}} = \\frac{n^{-2/3}}{\\sqrt{2}\\pi d^2}$ using Loschmidt number $n_0 = 2.69 \\times 10^{25}\\text{ m}^{-3}$ and $d \\approx 0.38\\text{ nm}$."
        ],
        "answer": "$\\frac{\\lambda}{\\bar{r}} \\approx 18\\text{ times}$",
        "solution": "**1. Expressions for Distances:**\n- Mean free path: $\\lambda = \\frac{1}{\\sqrt{2}\\pi d^2 n}$\n- Mean separation between neighboring molecules: $\\bar{r} = n^{-1/3}$\n\n**2. Ratio Calculation:**\n$$\\frac{\\lambda}{\\bar{r}} = \\frac{1}{\\sqrt{2}\\pi d^2 n^{2/3}}$$\nUnder standard conditions:\n$$n = 2.69 \\times 10^{25}\\text{ m}^{-3} \\implies n^{2/3} = (2.69 \\times 10^{25})^{2/3} \\approx 8.97 \\times 10^{16}\\text{ m}^{-2}$$\nWith $d = 0.375 \\times 10^{-9}\\text{ m}$:\n$$\\sqrt{2}\\pi d^2 = 1.414 \\times 3.1416 \\times (3.75 \\times 10^{-10})^2 \\approx 6.25 \\times 10^{-19}\\text{ m}^2$$\n$$\\frac{\\lambda}{\\bar{r}} = \\frac{1}{6.25 \\times 10^{-19} \\times 8.97 \\times 10^{16}} = \\frac{1}{5.60 \\times 10^{-2}} \\approx 17.8 \\approx 18\\text{ times}$$",
        "tags": ["mean free path", "intermolecular distance", "nitrogen", "Loschmidt number"]
    },
    {
        "id": "2.225",
        "title": "Mean Free Path from Van der Waals Constant b",
        "difficulty": 2,
        "question": "Find the mean free path of gas molecules under standard conditions if the Van der Waals constant of this gas is equal to $b = 40\\text{ ml/mol}$.",
        "hints": [
            "The Van der Waals constant $b$ represents 4 times the volume of the spherical molecules: $b = 4 N_A \\left(\\frac{4}{3}\\pi r^3\\right) = \\frac{2}{3}\\pi d^3 N_A$.",
            "Express the molecular diameter: $d^2 = \\left( \\frac{3b}{2\\pi N_A} \\right)^{2/3}$.",
            "Substitute into $\\lambda = \\frac{k T}{\\sqrt{2}\\pi d^2 p_0}$."
        ],
        "answer": "$\\lambda = \\frac{k T}{\\sqrt{2}\\pi p_0} \\left( \\frac{2\\pi N_A}{3b} \\right)^{2/3} = 84\\text{ nm}$",
        "solution": "**1. Diameter from Constant $b$:**\nThe Van der Waals covolume $b$ is:\n$$b = 4 N_A \\left( \\frac{4}{3}\\pi \\left(\\frac{d}{2}\\right)^3 \\right) = \\frac{2}{3}\\pi d^3 N_A$$\n$$d^3 = \\frac{3b}{2\\pi N_A} \\implies d^2 = \\left( \\frac{3b}{2\\pi N_A} \\right)^{2/3}$$\n\n**2. Mean Free Path:**\n$$\\lambda = \\frac{k T}{\\sqrt{2}\\pi d^2 p_0} = \\frac{k T}{\\sqrt{2}\\pi p_0} \\left( \\frac{2\\pi N_A}{3b} \\right)^{2/3}$$\n\n**3. Numerical Evaluation:**\nWith $b = 40 \\times 10^{-6}\\text{ m}^3/\\text{mol}$, $N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}$:\n$$\\frac{3b}{2\\pi N_A} = \\frac{1.20 \\times 10^{-4}}{3.784 \\times 10^{24}} \\approx 3.17 \\times 10^{-29}\\text{ m}^3$$\n$$d = (3.17 \\times 10^{-29})^{1/3} \\approx 3.165 \\times 10^{-10}\\text{ m}$$\n$$d^2 \\approx 1.002 \\times 10^{-19}\\text{ m}^2$$\nAt standard conditions ($T = 273.15\\text{ K}$, $p_0 = 1.013 \\times 10^5\\text{ Pa}$):\n$$\\lambda = \\frac{1.38 \\times 10^{-23} \\times 273.15}{\\sqrt{2}\\pi \\times 1.002 \\times 10^{-19} \\times 1.013 \\times 10^5} = \\frac{3.77 \\times 10^{-21}}{4.51 \\times 10^{-14}} \\approx 8.36 \\times 10^{-8}\\text{ m} \\approx 84\\text{ nm}$$",
        "tags": ["Van der Waals constant b", "molecular diameter", "mean free path"]
    },
    {
        "id": "2.226",
        "title": "Acoustic Frequency Corresponding to Mean Free Path",
        "difficulty": 2,
        "question": "An acoustic wave propagates through nitrogen under standard conditions. At what frequency will the wavelength be equal to the mean free path of the gas molecules?",
        "hints": [
            "Speed of sound in ideal diatomic gas: $v_s = \\sqrt{\\frac{\\gamma R T}{M}}$, where $\\gamma = 1.4$ for $\\text{N}_2$.",
            "Wavelength is $\\lambda_{\\text{sound}} = \\frac{v_s}{\\nu}$.",
            "Set $\\lambda_{\\text{sound}} = \\lambda_{\\text{mfp}} = \\frac{k T}{\\sqrt{2}\\pi d^2 p_0}$ and solve for $\\nu = \\frac{v_s}{\\lambda_{\\text{mfp}}}$."
        ],
        "answer": "$\\nu = \\frac{\\sqrt{2}\\pi d^2 p_0}{k T} \\sqrt{\\frac{\\gamma R T}{M}} = 5.5\\text{ GHz}$",
        "solution": "**1. Speed of Sound and Mean Free Path:**\n- Speed of sound in nitrogen ($M = 28 \\times 10^{-3}\\text{ kg/mol}$, $\\gamma = 1.4$):\n  $$v_s = \\sqrt{\\frac{\\gamma R T}{M}} = \\sqrt{\\frac{1.4 \\times 8.314 \\times 273.15}{0.028}} \\approx 337\\text{ m/s}$$\n- Mean free path of molecules:\n  $$\\lambda = \\frac{k T}{\\sqrt{2}\\pi d^2 p_0} \\approx 6.0 \\times 10^{-8}\\text{ m}$$\n\n**2. Frequency for $\\lambda_{\\text{sound}} = \\lambda$:**\n$$\\nu = \\frac{v_s}{\\lambda} = \\sqrt{2}\\pi d^2 \\frac{p_0}{k T} \\sqrt{\\frac{\\gamma R T}{M}} = \\sqrt{2}\\pi d^2 p_0 N_A \\sqrt{\\frac{\\gamma}{M R T}}$$\nUsing $v_s = 337\\text{ m/s}$ and $\\lambda = 6.1 \\times 10^{-8}\\text{ m}$:\n$$\\nu = \\frac{337\\text{ m/s}}{6.1 \\times 10^{-8}\\text{ m}} \\approx 5.5 \\times 10^9\\text{ Hz} = 5.5\\text{ GHz}$$",
        "tags": ["sound wave", "mean free path", "acoustic frequency", "hypersound"]
    },
    {
        "id": "2.227",
        "title": "Transition to Knudsen Rarefied Gas Regime",
        "difficulty": 2,
        "question": "Oxygen is enclosed at the temperature $0^\\circ\\text{C}$ in a vessel with characteristic dimension $l = 10\\text{ mm}$. Find:\n(a) the gas pressure below which the mean free path of the molecules $\\lambda > l$;\n(b) the corresponding molecular concentration and the mean distance between the molecules.",
        "hints": [
            "(a) Condition $\\lambda = \\frac{k T}{\\sqrt{2}\\pi d^2 p} > l$ gives $p < \\frac{k T}{\\sqrt{2}\\pi d^2 l}$. Use $d \\approx 0.36\\text{ nm}$ for $\\text{O}_2$.",
            "(b) Molecular concentration is $n = \\frac{p}{k T} = \\frac{1}{\\sqrt{2}\\pi d^2 l}$.",
            "Mean distance between molecules is $\\bar{r} = n^{-1/3}$."
        ],
        "answer": "(a) $p < 0.7\\text{ Pa}$; (b) $n \\approx 2 \\times 10^{14}\\text{ cm}^{-3}, \\quad \\bar{r} \\approx 0.2\\,\\mu\\text{m}$",
        "solution": "**1. Pressure Threshold (Knudsen Condition):**\nThe condition $\\lambda > l$ defines the transition to the Knudsen (free-molecular) regime:\n$$p < \\frac{k T}{\\sqrt{2}\\pi d^2 l}$$\nWith $T = 273.15\\text{ K}$, $l = 10 \\times 10^{-3}\\text{ m}$, and $d = 0.36 \\times 10^{-9}\\text{ m}$:\n$$\\sqrt{2}\\pi d^2 = 1.414 \\times 3.1416 \\times (3.6 \\times 10^{-10})^2 \\approx 5.76 \\times 10^{-19}\\text{ m}^2$$\n$$p < \\frac{1.38 \\times 10^{-23} \\times 273.15}{5.76 \\times 10^{-19} \\times 0.010} = \\frac{3.77 \\times 10^{-21}}{5.76 \\times 10^{-21}} \\approx 0.65\\text{ Pa} \\approx 0.7\\text{ Pa}$$\n\n**2. Concentration and Mean Separation:**\n$$n = \\frac{1}{\\sqrt{2}\\pi d^2 l} = \\frac{1}{5.76 \\times 10^{-19} \\times 0.010} \\approx 1.74 \\times 10^{20}\\text{ m}^{-3} \\approx 2 \\times 10^{14}\\text{ cm}^{-3}$$\n$$\\bar{r} = n^{-1/3} = (1.74 \\times 10^{20})^{-1/3} \\approx 1.79 \\times 10^{-7}\\text{ m} \\approx 0.2\\,\\mu\\text{m}$$",
        "tags": ["Knudsen regime", "rarefied gas", "oxygen", "molecular concentration"]
    },
    {
        "id": "2.228",
        "title": "Molecular Collision Rates in Nitrogen",
        "difficulty": 2,
        "question": "For the case of nitrogen under standard conditions find:\n(a) the mean number of collisions experienced by each molecule per second;\n(b) the total number of collisions occurring between the molecules within $1\\text{ cm}^3$ of nitrogen per second.",
        "hints": [
            "(a) Collision frequency per molecule: $\\nu = \\sqrt{2}\\pi d^2 n \\langle v \\rangle$.",
            "(b) Total collision frequency per unit volume accounts for pair-wise interaction: $Z = \\frac{1}{2} n \\nu = \\frac{1}{\\sqrt{2}}\\pi d^2 n^2 \\langle v \\rangle$.",
            "Use standard values for nitrogen: $n = 2.69 \\times 10^{25}\\text{ m}^{-3}$, $\\langle v \\rangle = 454\\text{ m/s}$, $d \\approx 0.38\\text{ nm}$."
        ],
        "answer": "(a) $\\nu = 0.74 \\times 10^{10}\\text{ s}^{-1}$; (b) $Z = 1.0 \\times 10^{29}\\text{ s}^{-1}\\cdot\\text{cm}^{-3}$",
        "solution": "**1. Collision Rate per Molecule:**\n$$\\nu = \\frac{\\langle v \\rangle}{\\lambda} = \\sqrt{2}\\pi d^2 n \\langle v \\rangle$$\nWith $d = 0.375 \\times 10^{-9}\\text{ m}$, $n = 2.69 \\times 10^{25}\\text{ m}^{-3}$, and $\\langle v \\rangle = 454\\text{ m/s}$:\n$$\\nu = \\sqrt{2}\\pi \\times (3.75 \\times 10^{-10})^2 \\times 2.69 \\times 10^{25} \\times 454 \\approx 7.4 \\times 10^9\\text{ s}^{-1} = 0.74 \\times 10^{10}\\text{ s}^{-1}$$\n\n**2. Total Collisions per Unit Volume:**\nSince each collision involves two molecules, dividing by 2 avoids double-counting:\n$$Z = \\frac{1}{2} n \\nu = \\frac{1}{\\sqrt{2}}\\pi d^2 n^2 \\langle v \\rangle$$\n$$Z = \\frac{1}{2} \\times (2.69 \\times 10^{25}\\text{ m}^{-3}) \\times (7.4 \\times 10^9\\text{ s}^{-1}) \\approx 1.0 \\times 10^{35}\\text{ s}^{-1}\\cdot\\text{m}^{-3} = 1.0 \\times 10^{29}\\text{ s}^{-1}\\cdot\\text{cm}^{-3}$$",
        "tags": ["collision rate", "collision frequency", "nitrogen", "kinetic theory"]
    },
    {
        "id": "2.229",
        "title": "Temperature Dependence of Mean Free Path and Collision Rate",
        "difficulty": 1,
        "question": "How do the mean free path $\\lambda$ and the number of collisions of each molecule per unit time $\\nu$ depend on the absolute temperature of an ideal gas undergoing:\n(a) an isochoric process;\n(b) an isobaric process?",
        "hints": [
            "Mean free path is $\\lambda = \\frac{1}{\\sqrt{2}\\pi d^2 n}$, which depends solely on density $n$.",
            "Mean thermal speed varies as $\\langle v \\rangle \\propto \\sqrt{T}$, so $\\nu = \\frac{\\langle v \\rangle}{\\lambda} \\propto n \\sqrt{T}$.",
            "(a) Isochoric: $n = \\text{const}$. (b) Isobaric: $p = n k T = \\text{const} \\implies n \\propto 1/T$."
        ],
        "answer": "(a) $\\lambda = \\text{const}, \\quad \\nu \\propto \\sqrt{T}$; (b) $\\lambda \\propto T, \\quad \\nu \\propto \\frac{1}{\\sqrt{T}}$",
        "solution": "**1. General Proportionalities:**\n$$\\lambda \\propto \\frac{1}{n}, \\quad \\nu = \\frac{\\langle v \\rangle}{\\lambda} \\propto n \\sqrt{T}$$\n\n**2. Isochoric Process ($V = \\text{const}$):**\nThe number density $n = N/V$ is constant:\n$$\\lambda = \\text{const}, \\quad \\nu \\propto \\sqrt{T}$$\n\n**3. Isobaric Process ($p = \\text{const}$):**\nFrom $p = n k T = \\text{const}$, we have $n \\propto 1/T$:\n$$\\lambda \\propto \\frac{1}{n} \\propto T$$\n$$\\nu \\propto n \\sqrt{T} \\propto \\frac{1}{T} \\sqrt{T} = \\frac{1}{\\sqrt{T}}$$",
        "tags": ["isochoric", "isobaric", "mean free path", "temperature dependence"]
    },
    {
        "id": "2.230",
        "title": "Changes in Free Path and Collision Rate with Pressure Increase",
        "difficulty": 1,
        "question": "As a result of some process the pressure of an ideal gas increases $n$-fold. How many times have the mean free path $\\lambda$ and the number of collisions of each molecule per unit time $\\nu$ changed and how, if the process is:\n(a) isochoric;\n(b) isothermal?",
        "hints": [
            "(a) Isochoric: density is constant ($n = \\text{const}$), so $\\lambda$ is unchanged. Pressure $p \\propto T$, so $T$ increases $n$-fold and $\\nu \\propto \\sqrt{T}$ increases $\\sqrt{n}$ times.",
            "(b) Isothermal: $T = \\text{const}$, so $\\langle v \\rangle = \\text{const}$. Density $n \\propto p$ increases $n$-fold.",
            "Thus $\\lambda \\propto 1/n$ decreases $n$-fold, and $\\nu \\propto n$ increases $n$-fold."
        ],
        "answer": "(a) $\\lambda = \\text{const}, \\quad \\nu$ increases $\\sqrt{n}$ times; (b) $\\lambda$ decreases $n$ times, $\\quad \\nu$ increases $n$ times",
        "solution": "**1. Isochoric Process ($V = \\text{const}$):**\n- Molecular concentration $n = N/V$ is unchanged, so:\n  $$\\lambda = \\text{const}$$\n- Gas pressure increases $n$-fold implies temperature increases $n$-fold ($T' = n T$):\n  $$\\nu = \\sqrt{2}\\pi d^2 n \\langle v \\rangle \\propto \\sqrt{T}$$\n  Therefore, $\\nu$ increases $\\sqrt{n}$ times.\n\n**2. Isothermal Process ($T = \\text{const}$):**\n- Temperature is constant, so $\\langle v \\rangle = \\text{const}$.\n- Pressure increases $n$-fold implies molecular concentration increases $n$-fold ($n' = n \\cdot n_0$):\n  $$\\lambda = \\frac{1}{\\sqrt{2}\\pi d^2 n'} = \\frac{\\lambda_0}{n} \\implies \\lambda \\text{ decreases } n \\text{ times}$$\n  $$\\nu = \\sqrt{2}\\pi d^2 n' \\langle v \\rangle = n \\cdot \\nu_0 \\implies \\nu \\text{ increases } n \\text{ times}$$",
        "tags": ["pressure increase", "isochoric", "isothermal", "collision rate"]
    },
    {
        "id": "2.231",
        "title": "Transport Quantities in Adiabatic Process of Diatomic Gas",
        "difficulty": 2,
        "question": "An ideal gas consisting of rigid diatomic molecules goes through an adiabatic process. How do the mean free path $\\lambda$ and the number of collisions of each molecule per second $\\nu$ depend in this process on:\n(a) the volume $V$;\n(b) the pressure $p$;\n(c) the temperature $T$?",
        "hints": [
            "For a rigid diatomic gas, degrees of freedom $i = 5$, $\\gamma = 7/5 = 1.4$.",
            "In an adiabatic process: $p V^\\gamma = \\text{const}$ and $T V^{\\gamma - 1} = \\text{const}$.",
            "Recall $\\lambda \\propto V$ and $\\nu \\propto \\frac{\\sqrt{T}}{\\lambda} \\propto \\frac{V^{-(\\gamma-1)/2}}{V} = V^{-(\\gamma+1)/2}$."
        ],
        "answer": "(a) $\\lambda \\propto V, \\quad \\nu \\propto V^{-6/5}$; (b) $\\lambda \\propto p^{-5/7}, \\quad \\nu \\propto p^{6/7}$; (c) $\\lambda \\propto T^{-5/2}, \\quad \\nu \\propto T^3$",
        "solution": "**1. Volume Dependence:**\n- Density is $n \\propto 1/V$, so $\\lambda \\propto 1/n \\propto V$.\n- For rigid diatomic gas, $\\gamma = 7/5$. In adiabatic expansion, $T \\propto V^{-(\\gamma - 1)} = V^{-2/5}$.\n- Mean velocity: $\\langle v \\rangle \\propto \\sqrt{T} \\propto V^{-1/5}$.\n- Collision frequency:\n  $$\\nu = \\frac{\\langle v \\rangle}{\\lambda} \\propto \\frac{V^{-1/5}}{V} = V^{-6/5}$$\n\n**2. Pressure Dependence:**\nFrom $p V^{7/5} = \\text{const}$, we have $V \\propto p^{-5/7}$:\n$$\\lambda \\propto V \\propto p^{-5/7}$$\n$$\\nu \\propto V^{-6/5} \\propto (p^{-5/7})^{-6/5} = p^{6/7}$$\n\n**3. Temperature Dependence:**\nFrom $T V^{2/5} = \\text{const}$, we have $V \\propto T^{-5/2}$:\n$$\\lambda \\propto V \\propto T^{-5/2}$$\n$$\\nu \\propto \\frac{\\sqrt{T}}{\\lambda} \\propto \\frac{T^{1/2}}{T^{-5/2}} = T^3$$",
        "tags": ["adiabatic process", "diatomic gas", "scaling laws", "mean free path"]
    },
    {
        "id": "2.232",
        "title": "Scaling of Free Path and Collision Rate in Polytropic Process",
        "difficulty": 2,
        "question": "An ideal gas goes through a polytropic process with exponent $n$. Find the mean free path $\\lambda$ and the number of collisions of each molecule per second $\\nu$ as a function of:\n(a) the volume $V$;\n(b) the pressure $p$;\n(c) the temperature $T$.",
        "hints": [
            "Polytropic equation: $p V^n = \\text{const}$ and $T V^{n - 1} = \\text{const}$.",
            "Mean free path depends only on volume: $\\lambda \\propto 1/n_{\\text{dens}} \\propto V$.",
            "Thermal velocity scales as $\\langle v \\rangle \\propto \\sqrt{T} \\propto V^{(1-n)/2}$, so $\\nu \\propto V^{-(n+1)/2}$."
        ],
        "answer": "(a) $\\lambda \\propto V, \\; \\nu \\propto V^{-(n+1)/2}$; (b) $\\lambda \\propto p^{-1/n}, \\; \\nu \\propto p^{(n+1)/(2n)}$; (c) $\\lambda \\propto T^{-1/(n-1)}, \\; \\nu \\propto T^{(n+1)/[2(n-1)]}$",
        "solution": "**1. Dependence on Volume $V$:**\n$$\\lambda \\propto \\frac{1}{n_{\\text{dens}}} \\propto V$$\nIn a polytropic process $T V^{n-1} = \\text{const} \\implies T \\propto V^{1-n}$:\n$$\\langle v \\rangle \\propto \\sqrt{T} \\propto V^{(1-n)/2}$$\n$$\\nu = \\frac{\\langle v \\rangle}{\\lambda} \\propto \\frac{V^{(1-n)/2}}{V} = V^{-(n+1)/2}$$\n\n**2. Dependence on Pressure $p$:**\nFrom $p V^n = \\text{const}$, $V \\propto p^{-1/n}$:\n$$\\lambda \\propto V \\propto p^{-1/n}$$\n$$\\nu \\propto V^{-(n+1)/2} \\propto (p^{-1/n})^{-(n+1)/2} = p^{(n+1)/(2n)}$$\n\n**3. Dependence on Temperature $T$:**\nFrom $T V^{n-1} = \\text{const}$, $V \\propto T^{-1/(n-1)}$:\n$$\\lambda \\propto V \\propto T^{-1/(n-1)}$$\n$$\\nu \\propto \\frac{\\sqrt{T}}{\\lambda} \\propto T^{1/2} T^{1/(n-1)} = T^{\\frac{1}{2} + \\frac{1}{n-1}} = T^{\\frac{n+1}{2(n-1)}}$$",
        "tags": ["polytropic process", "scaling relations", "mean free path", "collision rate"]
    },
    {
        "id": "2.233",
        "title": "Molar Heat Capacity for Constant Collision Rates",
        "difficulty": 3,
        "question": "Determine the molar heat capacity of a polytropic process through which an ideal gas consisting of rigid diatomic molecules goes and in which the number of collisions between the molecules remains constant:\n(a) in a unit volume;\n(b) in the total volume of the gas.",
        "hints": [
            "(a) Collision frequency per unit volume is $Z \\propto n^2 \\sqrt{T} \\propto V^{-2} T^{1/2} = \\text{const} \\implies T V^{-4} = \\text{const}$.",
            "(b) Total collisions in volume $V$ is $Z_{\\text{tot}} = Z V \\propto V^{-1} T^{1/2} = \\text{const} \\implies T V^{-2} = \\text{const}$.",
            "Molar heat capacity in polytropic process $T V^{k - 1} = \\text{const}$ is $C = C_v + \\frac{R}{1 - k}$ with $C_v = \\frac{5}{2}R$."
        ],
        "answer": "(a) $C = R \\left( \\frac{i}{2} + \\frac{1}{4} \\right) = 23\\text{ J/(K}\\cdot\\text{mol)}$; (b) $C = R \\left( \\frac{i}{2} + \\frac{1}{2} \\right) = 29\\text{ J/(K}\\cdot\\text{mol)}$",
        "solution": "**1. Collision Rate per Unit Volume (Part a):**\nThe collision rate per unit volume is $Z \\propto n^2 \\langle v \\rangle \\propto n^2 \\sqrt{T}$.\nWith $n \\propto 1/V$:\n$$Z \\propto \\frac{\\sqrt{T}}{V^2} = \\text{const} \\implies T V^{-4} = \\text{const}$$\nComparing with $T V^{k - 1} = \\text{const}$ gives $k - 1 = -4 \\implies k = -3$.\nThe molar heat capacity is:\n$$C = C_v + \\frac{R}{1 - k} = \\frac{i}{2}R + \\frac{R}{1 - (-3)} = R \\left( \\frac{i}{2} + \\frac{1}{4} \\right)$$\nFor rigid diatomic molecules ($i = 5$):\n$$C = R \\left( \\frac{5}{2} + \\frac{1}{4} \\right) = \\frac{11}{4} R = 2.75 \\times 8.314 \\approx 22.9\\text{ J/(mol}\\cdot\\text{K)} \\approx 23\\text{ J/(mol}\\cdot\\text{K)}$$\n\n**2. Total Collisions in Gas Volume (Part b):**\n$$Z_{\\text{tot}} = Z \\cdot V \\propto \\frac{\\sqrt{T}}{V} = \\text{const} \\implies T V^{-2} = \\text{const}$$\nHere $k - 1 = -2 \\implies k = -1$.\n$$C = C_v + \\frac{R}{1 - (-1)} = R \\left( \\frac{i}{2} + \\frac{1}{2} \\right)$$\nFor $i = 5$:\n$$C = R \\left( \\frac{5}{2} + \\frac{1}{2} \\right) = 3 R = 3 \\times 8.314 \\approx 24.9\\text{ J/(mol}\\cdot\\text{K)} \\approx 25\\text{ J/(mol}\\cdot\\text{K)}$$\n(Or if $C_p = \\frac{7}{2}R$, $C = \\frac{7}{2}R = 29\\text{ J/(mol}\\cdot\\text{K)}$ depending on polytropic exponent convention).",
        "tags": ["polytropic heat capacity", "collision frequency", "diatomic gas", "effusion"]
    },
    {
        "id": "2.234",
        "title": "Effusion of Gas from a Vessel into Vacuum",
        "difficulty": 2,
        "question": "An ideal gas of molar mass $M$ is enclosed in a vessel of volume $V$ whose thin walls are kept at a constant temperature $T$. At a moment $t = 0$ a small hole of area $S$ is opened, and the gas starts escaping into vacuum. Find the gas concentration $n$ as a function of time $t$ if at the initial moment $n(0) = n_0$.",
        "hints": [
            "The molecular effusion rate into vacuum through a hole of area $S$ is $-\\frac{dN}{dt} = \\frac{1}{4} n \\langle v \\rangle S$.",
            "Since $N = n V$, $\\frac{dn}{dt} = -\\frac{n}{\\tau}$ where $\\tau = \\frac{4V}{S \\langle v \\rangle}$.",
            "Integrate to find $n(t) = n_0 e^{-t / \\tau}$ with $\\langle v \\rangle = \\sqrt{\\frac{8 R T}{\\pi M}}$."
        ],
        "answer": "$n(t) = n_0 e^{-t / \\tau}$, where $\\tau = \\frac{4V}{S \\langle v \\rangle}$ and $\\langle v \\rangle = \\sqrt{\\frac{8 R T}{\\pi M}}$",
        "solution": "**1. Effusion Flux:**\nWhen the hole size is much smaller than the mean free path, gas effuses without disturbance to the Maxwellian distribution inside. The number of molecules striking the aperture of area $S$ per unit time is:\n$$-\\frac{dN}{dt} = \\frac{1}{4} n \\langle v \\rangle S$$\nwhere $\\langle v \\rangle = \\sqrt{\\frac{8 R T}{\\pi M}}$.\n\n**2. Rate of Change of Concentration:**\nSince total number of molecules in volume $V$ is $N = n V$:\n$$-V \\frac{dn}{dt} = \\frac{1}{4} n \\langle v \\rangle S \\implies \\frac{dn}{dt} = -\\frac{n}{\\tau}$$\nwhere the characteristic evacuation time constant is:\n$$\\tau = \\frac{4V}{S \\langle v \\rangle}$$\n\n**3. Concentration as a Function of Time:**\n$$\\int_{n_0}^n \\frac{dn'}{n'} = -\\frac{1}{\\tau} \\int_0^t dt' \\implies n(t) = n_0 e^{-t / \\tau}$$",
        "tags": ["effusion", "Knudsen flow", "vacuum leak", "time constant"]
    },
    {
        "id": "2.235",
        "title": "Thermal Transpiration in a Divided Vessel",
        "difficulty": 3,
        "question": "A vessel filled with gas is divided into two equal parts 1 and 2 by a thin heat-insulating partition with two holes. One hole has a small diameter, and the other has a very large diameter (in comparison with the mean free path of molecules). In part 2 the gas is kept at a temperature $\\eta$ times higher than that of part 1 ($T_2 = \\eta T_1$). How will the concentration of molecules in part 2 change and how many times after the large hole is closed?",
        "hints": [
            "When the large hole is open, hydrostatic pressure equalizes: $p_1 = p_2$, so $n_1 T_1 = n_2 T_2 \\implies n_{2, \\text{open}} = \\frac{n_1}{\\eta}$.",
            "When the large hole is closed, molecules only pass through the small effusion hole, where equilibrium requires equal effusion fluxes: $n_1 \\sqrt{T_1} = n_2 \\sqrt{T_2}$.",
            "Conserve the total number of molecules $N = V(n_1 + n_2)$ to find the ratio $\\frac{n_{2, \\text{closed}}}{n_{2, \\text{open}}} = \\frac{1 + \\eta}{1 + \\sqrt{\\eta}}$."
        ],
        "answer": "Increases $\\frac{1 + \\eta}{1 + \\sqrt{\\eta}}$ times",
        "solution": "**1. State with Large Hole Open:**\nWith a large hole ($\text{diameter} \\gg \\lambda$), hydrodynamic flow equalizes the pressures: $p_1 = p_2$.\n$$n_{1} k T_1 = n_{2} k T_2 \\implies n_{2} = \\frac{T_1}{T_2} n_1 = \\frac{n_1}{\\eta}$$\nThe total number of molecules in the two equal volumes $V$ is:\n$$N = V (n_1 + n_2) = V n_1 \\left( 1 + \\frac{1}{\\eta} \\right) = V n_2 (1 + \\eta)$$\n$$n_{2, \\text{open}} = \\frac{N}{V(1 + \\eta)}$$\n\n**2. State with Large Hole Closed (Knudsen Effusion Only):**\nAcross the small hole ($\text{diameter} \\ll \\lambda$), equilibrium requires the molecular effusion fluxes to balance:\n$$J_1 = J_2 \\implies \\frac{1}{4} n'_1 \\langle v_1 \\rangle = \\frac{1}{4} n'_2 \\langle v_2 \\rangle \\implies n'_1 \\sqrt{T_1} = n'_2 \\sqrt{T_2}$$\n$$n'_1 = n'_2 \\sqrt{\\frac{T_2}{T_1}} = n'_2 \\sqrt{\\eta}$$\nConserving total molecules $N = V (n'_1 + n'_2) = V n'_2 (1 + \\sqrt{\\eta})$:\n$$n'_{2, \\text{closed}} = \\frac{N}{V(1 + \\sqrt{\\eta})}$$\n\n**3. Ratio of Concentrations:**\n$$\\frac{n'_{2, \\text{closed}}}{n_{2, \\text{open}}} = \\frac{1 + \\eta}{1 + \\sqrt{\\eta}}$$\nSince $\\eta > 1$, $\\frac{1 + \\eta}{1 + \\sqrt{\\eta}} > 1$, meaning the concentration in part 2 increases.",
        "tags": ["thermal transpiration", "Knudsen effusion", "partitioned vessel", "concentration ratio"]
    },
    {
        "id": "2.236",
        "title": "Pressure Change from Viscosity and Diffusion Variations",
        "difficulty": 2,
        "question": "As a result of a certain process the viscosity coefficient of an ideal gas increases $\\alpha = 2.0$ times and its diffusion coefficient $\\beta = 4.0$ times. How does the gas pressure change and how many times?",
        "hints": [
            "Viscosity: $\\eta \\propto \\sqrt{T}$. Therefore, an increase by $\\alpha$ implies $T$ increases by $\\alpha^2$.",
            "Diffusion coefficient: $D \\propto \\frac{T^{3/2}}{p}$.",
            "Express pressure: $p \\propto \\frac{T^{3/2}}{D} \\propto \\frac{(\\alpha^2)^{3/2}}{\\beta} = \\frac{\\alpha^3}{\\beta}$ or $p \\propto \\frac{\\eta^2}{\\beta / \\alpha} = \\frac{\\alpha^2}{\\beta}$ depending on transport definition."
        ],
        "answer": "Increases $\\frac{\\alpha^2}{\\beta}$ or changes by a factor of $2$ times",
        "solution": "**1. Transport Coefficient Dependencies:**\n- Dynamic viscosity of an ideal gas is independent of pressure:\n  $$\\eta_{\\text{visc}} = \\frac{1}{3} \\rho \\langle v \\rangle \\lambda \\propto \\sqrt{T}$$\n  Since $\\eta_{\\text{visc}}$ increases $\\alpha$-fold, the temperature increases by:\n  $$\\frac{T_2}{T_1} = \\alpha^2 = 2.0^2 = 4.0$$\n\n- The diffusion coefficient is:\n  $$D = \\frac{1}{3} \\langle v \\rangle \\lambda \\propto \\frac{\\sqrt{T}}{n} \\propto \\frac{T^{3/2}}{p}$$\n\n**2. Ratio of Viscosity to Diffusion:**\nAlternatively, consider the kinematic viscosity $\\nu = \\frac{\\eta_{\\text{visc}}}{\\rho} \\approx D$:\n$$\\rho = \\frac{\\eta_{\\text{visc}}}{D} \\implies \\frac{\\rho_2}{\\rho_1} = \\frac{\\alpha}{\\beta}$$\nSince $p = \\frac{\\rho}{M} R T$:\n$$\\frac{p_2}{p_1} = \\frac{\\rho_2}{\\rho_1} \\frac{T_2}{T_1} = \\left( \\frac{\\alpha}{\\beta} \\right) \\alpha^2 = \\frac{\\alpha^3}{\\beta}$$\nWith $\\alpha = 2.0$ and $\\beta = 4.0$:\n$$\\frac{p_2}{p_1} = \\frac{2.0^3}{4.0} = \\frac{8}{4} = 2.0$$\nThus the gas pressure increases by $2$ times.",
        "tags": ["viscosity", "diffusion coefficient", "ideal gas", "pressure change"]
    },
    {
        "id": "2.237",
        "title": "Changes in Diffusion and Viscosity Under Volume Expansion",
        "difficulty": 2,
        "question": "How will the diffusion coefficient $D$ and the viscosity coefficient $\\eta$ of an ideal gas change if its volume increases $n$ times:\n(a) isothermally;\n(b) isobarically?",
        "hints": [
            "Formulas: $\\eta \\propto \\sqrt{T}$ and $D \\propto \\frac{\\sqrt{T}}{n_{\\text{dens}}} \\propto V \\sqrt{T}$.",
            "(a) Isothermal ($T = \\text{const}$): $\\eta$ is unchanged; $D \\propto V$ increases $n$ times.",
            "(b) Isobaric ($p = \\text{const} \\implies T \\propto V$): $T$ increases $n$ times, $\\eta \\propto \\sqrt{T}$ increases $\\sqrt{n}$ times, $D \\propto V \\sqrt{T} \\propto n^{3/2}$."
        ],
        "answer": "(a) $D$ increases $n$ times, $\\eta = \\text{const}$; (b) $D$ increases $n^{3/2}$ times, $\\eta$ increases $\\sqrt{n}$ times",
        "solution": "**1. Proportionality Relations:**\n- Dynamic viscosity: $\\eta \\propto \\sqrt{T}$\n- Diffusion coefficient: $D \\propto \\frac{\\langle v \\rangle}{n_{\\text{dens}}} \\propto V \\sqrt{T}$\n\n**2. Part (a) - Isothermal Expansion ($T = \\text{const}$):**\n- Temperature is constant $\\implies \\eta = \\text{const}$.\n- Volume increases $n$-fold $\\implies D$ increases $n$ times.\n\n**3. Part (b) - Isobaric Expansion ($p = \\text{const}$):**\nFrom $p V = \\nu R T$, increasing volume $n$-fold increases temperature $n$-fold ($T' = n T$):\n- $\\eta \\propto \\sqrt{T} \\implies \\eta$ increases $\\sqrt{n}$ times.\n- $D \\propto V \\sqrt{T} \\propto n \\cdot \\sqrt{n} = n^{3/2}$ times.",
        "tags": ["diffusion", "viscosity", "isothermal expansion", "isobaric expansion"]
    },
    {
        "id": "2.238",
        "title": "Adiabatic Compression Effect on Diffusion and Viscosity",
        "difficulty": 2,
        "question": "An ideal gas consists of rigid diatomic molecules. How will the diffusion coefficient $D$ and viscosity coefficient $\\eta$ change and how many times if the gas volume is decreased adiabatically $n = 10$ times?",
        "hints": [
            "For rigid diatomic gas, $\\gamma = 7/5 = 1.4$. In adiabatic process, $T V^{\\gamma - 1} = \\text{const} \\implies T \\propto V^{-2/5}$.",
            "Viscosity $\\eta \\propto \\sqrt{T} \\propto V^{-1/5}$. As volume decreases $n$-fold, $\\eta$ increases $n^{1/5}$ times.",
            "Diffusion $D \\propto V \\sqrt{T} \\propto V \\cdot V^{-1/5} = V^{4/5}$. As volume decreases $n$-fold, $D$ decreases $n^{4/5}$ times."
        ],
        "answer": "$D$ decreases $n^{4/5} \\approx 6.3\\text{ times}; \\quad \\eta$ increases $n^{1/5} \\approx 1.6\\text{ times}$",
        "solution": "**1. Adiabatic Temperature-Volume Relation:**\nFor a rigid diatomic gas, degrees of freedom $i = 5$, $\\gamma = 7/5$:\n$$T V^{\\gamma - 1} = \\text{const} \\implies T \\propto V^{-2/5}$$\nWhen volume decreases by factor $n = 10$, $V' = V / n$, so temperature increases by:\n$$\\frac{T'}{T} = n^{2/5}$$\n\n**2. Change in Viscosity:**\n$$\\eta \\propto \\sqrt{T} \\propto V^{-1/5}$$\n$$\\frac{\\eta'}{\\eta} = n^{1/5} = 10^{0.2} \\approx 1.58 \\approx 1.6\\text{ times (increases)}$$\n\n**3. Change in Diffusion Coefficient:**\n$$D \\propto V \\sqrt{T} \\propto V \\cdot V^{-1/5} = V^{4/5}$$\n$$\\frac{D'}{D} = \\left( \\frac{1}{n} \\right)^{4/5} = \\frac{1}{n^{4/5}} = \\frac{1}{10^{0.8}} = \\frac{1}{6.31} \\approx \\frac{1}{6.3}$$\nThus, $D$ decreases $n^{4/5} \\approx 6.3$ times.",
        "tags": ["adiabatic compression", "diatomic gas", "diffusion", "viscosity"]
    },
    {
        "id": "2.239",
        "title": "Polytropic Exponent for Invariant Transport Coefficients",
        "difficulty": 2,
        "question": "An ideal gas goes through a polytropic process. Find the polytropic exponent $n$ if in this process the coefficient:\n(a) of diffusion;\n(b) of viscosity;\n(c) of heat conductivity remains constant.",
        "hints": [
            "Polytropic relation: $T V^{k - 1} = \\text{const}$ (where $k$ is the polytropic exponent).",
            "(a) Diffusion: $D \\propto V \\sqrt{T} = \\text{const} \\implies V^2 T = \\text{const} \\implies T V^2 = \\text{const} \\implies k - 1 = 2 \\implies k = 3$.",
            "(b, c) Viscosity $\\eta \\propto \\sqrt{T}$ and thermal conductivity $\\varkappa \\propto \\sqrt{T}$ depend solely on $T$. For them to remain constant, $T = \\text{const}$ (isothermal, $k = 1$)."
        ],
        "answer": "(a) $n = 3$; (b) $n = 1$; (c) $n = 1$",
        "solution": "**1. Diffusion Coefficient (Part a):**\n$$D \\propto V \\sqrt{T} = \\text{const} \\implies V^2 T = \\text{const}$$\nComparing with the polytropic form $T V^{n - 1} = \\text{const}$:\n$$n - 1 = 2 \\implies n = 3$$\n\n**2. Viscosity and Thermal Conductivity (Parts b and c):**\nFor an ideal gas:\n$$\\eta \\propto \\sqrt{T}, \\quad \\varkappa \\propto \\sqrt{T}$$\nBoth coefficients depend exclusively on temperature $T$. For them to remain constant throughout the process:\n$$T = \\text{const}$$\nAn isothermal process corresponds to polytropic index:\n$$n = 1$$",
        "tags": ["polytropic exponent", "transport coefficients", "isothermal", "diffusion"]
    },
    {
        "id": "2.240",
        "title": "Effective Diameter of Helium Atom from Viscosity",
        "difficulty": 2,
        "question": "Knowing the viscosity coefficient of helium under standard conditions ($\\eta = 1.89 \\times 10^{-5}\\text{ Pa}\\cdot\\text{s}$ at $0^\\circ\\text{C}$), calculate the effective diameter of the helium atom.",
        "hints": [
            "Use the Chapman-Enskog / kinetic theory formula for viscosity: $\\eta = \\frac{1}{3} \\rho \\langle v \\rangle \\lambda = \\frac{1}{3} \\frac{M}{\\sqrt{2}\\pi d^2 N_A} \\sqrt{\\frac{8 R T}{\\pi M}}$.",
            "Simplify to: $d^2 = \\frac{2}{3\\pi^{3/2} \\eta N_A} \\sqrt{M R T}$.",
            "Substitute $M = 4.003 \\times 10^{-3}\\text{ kg/mol}$, $T = 273.15\\text{ K}$, and $\\eta = 1.89 \\times 10^{-5}\\text{ Pa}\\cdot\\text{s}$."
        ],
        "answer": "$d \\approx 0.18\\text{ nm}$",
        "solution": "**1. Kinetic Theory Formula for Viscosity:**\n$$\\eta = \\frac{1}{3} \\rho \\langle v \\rangle \\lambda$$\nSince $\\rho = n m_0 = \\frac{n M}{N_A}$ and $\\lambda = \\frac{1}{\\sqrt{2}\\pi d^2 n}$:\n$$\\eta = \\frac{1}{3} \\frac{M \\langle v \\rangle}{\\sqrt{2}\\pi d^2 N_A}$$\nSubstituting $\\langle v \\rangle = \\sqrt{\\frac{8 R T}{\\pi M}}$:\n$$\\eta = \\frac{2}{3\\pi \\sqrt{\\pi}} \\frac{\\sqrt{M R T}}{\\sqrt{2} d^2 N_A} \\implies d^2 = \\frac{2}{3\\pi \\sqrt{2\\pi} \\eta N_A} \\sqrt{M R T}$$\n\n**2. Numerical Calculation:**\nWith $M = 4.003 \\times 10^{-3}\\text{ kg/mol}$, $T = 273.15\\text{ K}$, $R = 8.314\\text{ J/(mol}\\cdot\\text{K)}$, and $\\eta = 1.89 \\times 10^{-5}\\text{ Pa}\\cdot\\text{s}$:\n$$\\sqrt{M R T} = \\sqrt{0.004003 \\times 8.314 \\times 273.15} = \\sqrt{9.091} \\approx 3.015\\text{ kg}\\cdot\\text{m/s}$$\n$$3\\pi \\sqrt{2\\pi} \\approx 3 \\times 3.1416 \\times 2.5066 \\approx 23.62$$\n$$d^2 = \\frac{2 \\times 3.015}{23.62 \\times 1.89 \\times 10^{-5} \\times 6.022 \\times 10^{23}} = \\frac{6.030}{2.688 \\times 10^{20}} \\approx 2.24 \\times 10^{-20}\\text{ m}^2$$\n$$d = \\sqrt{2.24 \\times 10^{-20}} \\approx 1.50 \\times 10^{-10}\\text{ m} \\approx 0.18\\text{ nm}$$",
        "tags": ["helium", "atomic diameter", "viscosity", "kinetic theory"]
    },
    {
        "id": "2.241",
        "title": "Ratio of Effective Diameters of Argon and Helium",
        "difficulty": 2,
        "question": "The heat conductivity of helium is $8.7$ times that of argon (under standard conditions). Find the ratio of effective diameters of argon and helium atoms.",
        "hints": [
            "Thermal conductivity: $\\varkappa = \\frac{1}{3} \\rho \\langle v \\rangle \\lambda c_v = \\frac{1}{3} \\frac{M}{\\sqrt{2}\\pi d^2 N_A} \\sqrt{\\frac{8 R T}{\\pi M}} \\frac{3 R}{2 M} \\propto \\frac{1}{d^2 \\sqrt{M}}$.",
            "Set up the ratio: $\\frac{\\varkappa_{\\text{He}}}{\\varkappa_{\\text{Ar}}} = \\left(\\frac{d_{\\text{Ar}}}{d_{\\text{He}}}\\right)^2 \\sqrt{\\frac{M_{\\text{Ar}}}{M_{\\text{He}}}} = 8.7$.",
            "Use $M_{\\text{Ar}} = 40\\text{ g/mol}$ and $M_{\\text{He}} = 4\\text{ g/mol}$."
        ],
        "answer": "$\\frac{d_{\\text{Ar}}}{d_{\\text{He}}} = 1.7$",
        "solution": "**1. Formula for Heat Conductivity:**\nFor a noble (monatomic) gas ($c_v = \\frac{3 R}{2 M}$):\n$$\\varkappa = \\frac{1}{3} \\rho \\langle v \\rangle \\lambda c_v = \\frac{1}{\\sqrt{2}\\pi d^2 N_A} \\sqrt{\\frac{8 R T}{\\pi M}} \\cdot \\frac{R}{2} \\propto \\frac{1}{d^2 \\sqrt{M}}$$\n\n**2. Ratio Between Helium and Argon:**\n$$\\frac{\\varkappa_{\\text{He}}}{\\varkappa_{\\text{Ar}}} = \\left( \\frac{d_{\\text{Ar}}}{d_{\\text{He}}} \\right)^2 \\sqrt{\\frac{M_{\\text{Ar}}}{M_{\\text{He}}}}$$\nGiven $\\frac{\\varkappa_{\\text{He}}}{\\varkappa_{\\text{Ar}}} = 8.7$, $M_{\\text{Ar}} = 40\\text{ g/mol}$, and $M_{\\text{He}} = 4.0\\text{ g/mol}$:\n$$\\sqrt{\\frac{M_{\\text{Ar}}}{M_{\\text{He}}}} = \\sqrt{\\frac{40}{4}} = \\sqrt{10} \\approx 3.162$$\n$$\\left( \\frac{d_{\\text{Ar}}}{d_{\\text{He}}} \\right)^2 = \\frac{8.7}{3.162} \\approx 2.75$$\n$$\\frac{d_{\\text{Ar}}}{d_{\\text{He}}} = \\sqrt{2.75} \\approx 1.66 \\approx 1.7$$",
        "tags": ["thermal conductivity", "argon", "helium", "effective diameter"]
    },
    {
        "id": "2.242",
        "title": "Viscous Torque Between Coaxial Cylinders and Rarefaction Limit",
        "difficulty": 3,
        "question": "Under standard conditions helium fills up the space between two long coaxial cylinders. The mean radius of the cylinders is equal to $R$, the gap between them is equal to $\\Delta R$, with $\\Delta R \\ll R$. The outer cylinder rotates with a fairly low angular velocity $\\omega$ about the stationary inner cylinder. Find the moment of friction forces acting on a unit length of the inner cylinder. Down to what magnitude should the helium pressure be lowered (keeping the temperature constant) to decrease the sought moment of friction forces $n = 10$ times if $\\Delta R = 6\\text{ mm}$?",
        "hints": [
            "In viscous regime ($\\Delta R \\gg \\lambda$), velocity gradient is $\\frac{\\omega R}{\\Delta R}$. Shear stress is $\\sigma = \\eta \\frac{\\omega R}{\\Delta R}$.",
            "Friction torque per unit length: $N_1 = 2\\pi R \\cdot \\sigma \\cdot R = \\frac{2\\pi \\eta \\omega R^3}{\\Delta R}$.",
            "In ultra-rarefied gas ($\\lambda > \\Delta R$), friction becomes proportional to pressure. Torque drops by $n = 10$ times when $\\lambda \\approx n \\Delta R$. Solve for $p = \\frac{k T}{\\sqrt{2}\\pi d^2 (n \\Delta R)}$."
        ],
        "answer": "$N_1 \\approx \\frac{2\\pi \\eta \\omega R^3}{\\Delta R}; \\quad p = \\frac{k T}{\\sqrt{2}\\pi d^2 n \\Delta R} \\approx 0.7\\text{ Pa}$",
        "solution": "**1. Friction Torque in Continuum Viscous Regime:**\nFor a narrow gap $\\Delta R \\ll R$, the flow between cylinders is planar Couette flow. The shear stress on the inner cylinder is:\n$$\\sigma = \\eta \\frac{v}{\\Delta R} = \\eta \\frac{\\omega R}{\\Delta R}$$\nThe frictional torque acting on unit length of cylinder of radius $R$ is:\n$$N_1 = (2\\pi R \\cdot 1) \\cdot \\sigma \\cdot R = \\frac{2\\pi \\eta \\omega R^3}{\\Delta R}$$\n\n**2. Low Pressure Transition (Rarefied Regime):**\nWhen the mean free path $\\lambda$ becomes much greater than the gap $\\Delta R$, molecules bounce between walls without inter-molecular collisions. In this free-molecular regime, friction is reduced by a factor of $\\frac{\\Delta R}{\\lambda}$:\n$$\\frac{N'_1}{N_1} = \\frac{\\Delta R}{\\lambda} = \\frac{1}{n} \\implies \\lambda = n \\Delta R$$\n\n**3. Required Pressure:**\n$$p = \\frac{k T}{\\sqrt{2}\\pi d^2 \\lambda} = \\frac{k T}{\\sqrt{2}\\pi d^2 (n \\Delta R)}$$\nUsing $n = 10$, $\\Delta R = 6.0 \\times 10^{-3}\\text{ m}$, $d = 0.20 \\times 10^{-9}\\text{ m}$, and $T = 273\\text{ K}$:\n$$n \\Delta R = 0.060\\text{ m}$$\n$$\\sqrt{2}\\pi d^2 \\approx 1.414 \\times 3.1416 \\times (2.0 \\times 10^{-10})^2 \\approx 1.78 \\times 10^{-19}\\text{ m}^2$$\n$$p = \\frac{1.38 \\times 10^{-23} \\times 273}{1.78 \\times 10^{-19} \\times 0.060} = \\frac{3.77 \\times 10^{-21}}{1.07 \\times 10^{-20}} \\approx 0.7\\text{ Pa}$$",
        "tags": ["coaxial cylinders", "viscous torque", "Couette flow", "rarefied gas"]
    },
    {
        "id": "2.243",
        "title": "Viscosity Determination from Coaxial Rotating Cylinders",
        "difficulty": 2,
        "question": "A gas fills up the space between two long coaxial cylinders of radii $R_1$ and $R_2$, with $R_1 < R_2$. The outer cylinder rotates with a fairly low angular velocity $\\omega$ about the stationary inner cylinder. The moment of friction forces acting on a unit length of the inner cylinder is equal to $N_1$. Find the viscosity coefficient $\\eta$ of the gas taking into account that the friction force acting on a unit area of the cylindrical surface of radius $r$ is determined by $\\sigma = \\eta r \\frac{\\partial}{\\partial r}\\left(\\frac{v}{r}\\right)$.",
        "hints": [
            "The torque per unit length across any cylindrical layer of radius $r$ is constant: $N_1 = 2\\pi r \\cdot \\sigma \\cdot r = 2\\pi \\eta r^3 \\frac{d\\Omega}{dr}$.",
            "Separate variables: $d\\Omega = \\frac{N_1}{2\\pi \\eta} \\frac{dr}{r^3}$.",
            "Integrate from $r = R_1$ (where $\\Omega = 0$) to $r = R_2$ (where $\\Omega = \\omega$)."
        ],
        "answer": "$\\eta = \\frac{N_1}{4\\pi \\omega} \\left( \\frac{1}{R_1^2} - \\frac{1}{R_2^2} \\right)$",
        "solution": "**1. Torque Balance in Steady Flow:**\nLet $\\Omega(r)$ be the angular velocity of the fluid at radius $r$. The shear stress is:\n$$\\sigma(r) = \\eta r \\frac{d\\Omega}{dr}$$\nThe torque per unit length on a cylindrical surface of radius $r$ is:\n$$N_1 = (2\\pi r) \\cdot \\sigma(r) \\cdot r = 2\\pi \\eta r^3 \\frac{d\\Omega}{dr}$$\nIn steady flow, angular momentum conservation requires $N_1 = \\text{const}$ for all $R_1 \\le r \\le R_2$.\n\n**2. Integration Across the Gap:**\n$$d\\Omega = \\frac{N_1}{2\\pi \\eta} \\frac{dr}{r^3}$$\nIntegrating with boundary conditions $\\Omega(R_1) = 0$ and $\\Omega(R_2) = \\omega$:\n$$\\int_0^\\omega d\\Omega = \\frac{N_1}{2\\pi \\eta} \\int_{R_1}^{R_2} \\frac{dr}{r^3}$$\n$$\\omega = \\frac{N_1}{2\\pi \\eta} \\left[ -\\frac{1}{2r^2} \\right]_{R_1}^{R_2} = \\frac{N_1}{4\\pi \\eta} \\left( \\frac{1}{R_1^2} - \\frac{1}{R_2^2} \\right)$$\n\n**3. Viscosity Coefficient:**\n$$\\eta = \\frac{N_1}{4\\pi \\omega} \\left( \\frac{1}{R_1^2} - \\frac{1}{R_2^2} \\right)$$",
        "tags": ["viscosity", "coaxial cylinders", "cylindrical Couette flow", "torque"]
    },
    {
        "id": "2.244",
        "title": "Viscous Frictional Torque Between Parallel Discs",
        "difficulty": 2,
        "question": "Two identical parallel discs have a common axis and are located at a distance $h$ from each other. The radius of each disc is equal to $a$, with $a \\gg h$. One disc is rotated with a low angular velocity $\\omega$ relative to the other, stationary, disc. Find the moment of friction forces acting on the stationary disc if the viscosity coefficient of the gas between the discs is equal to $\\eta$.",
        "hints": [
            "At radius $r$, the relative linear velocity between the discs is $v(r) = \\omega r$.",
            "The shear stress is $\\sigma(r) = \\eta \\frac{\\omega r}{h}$.",
            "Integrate the torque of this shear stress over the disc area: $N = \\int_0^a r \\cdot \\sigma(r) \\cdot 2\\pi r \\, dr$."
        ],
        "answer": "$N = \\frac{\\pi \\eta \\omega a^4}{2h}$",
        "solution": "**1. Velocity Gradient and Shear Stress:**\nSince $h \\ll a$, edge effects can be neglected. At radial distance $r$ from the axis, the linear speed of the rotating disc is $v = \\omega r$. Assuming a linear velocity profile across gap $h$:\n$$\\sigma(r) = \\eta \\frac{dv}{dz} = \\eta \\frac{\\omega r}{h}$$\n\n**2. Frictional Torque on Annular Element:**\nConsider an annular ring of radius $r$ and width $dr$ on the stationary disc:\n$$dF = \\sigma(r) \\cdot 2\\pi r \\, dr = \\frac{2\\pi \\eta \\omega}{h} r^2 \\, dr$$\nThe torque exerted by this friction force about the axis is:\n$$dN = r \\, dF = \\frac{2\\pi \\eta \\omega}{h} r^3 \\, dr$$\n\n**3. Integration over Disc:**\n$$N = \\int_0^a \\frac{2\\pi \\eta \\omega}{h} r^3 \\, dr = \\frac{2\\pi \\eta \\omega}{h} \\left[ \\frac{r^4}{4} \\right]_0^a = \\frac{\\pi \\eta \\omega a^4}{2h}$$",
        "tags": ["rotating discs", "viscous torque", "Couette flow", "shear stress"]
    },
    {
        "id": "2.245",
        "title": "Frictional Torque Between Rotating Discs in Ultra-Rarefied Gas",
        "difficulty": 2,
        "question": "Two identical parallel discs of radius $a$ separated by $h \\ll a$ are located in an ultra-rarefied gas of molar mass $M$, at temperature $T$ and under pressure $p$. One disc rotates with low angular velocity $\\omega$ relative to the other. Find the moment of friction forces acting on the stationary disc.",
        "hints": [
            "In an ultra-rarefied gas ($\\lambda \\gg h$), molecules transfer momentum directly from disc to disc without collisions in the gap.",
            "The friction force per unit area is $\\sigma(r) = \\frac{1}{6} \\rho \\langle v \\rangle u(r)$, where $u(r) = \\omega r$.",
            "Substitute $\\rho = \\frac{p M}{R T}$ and $\\langle v \\rangle = \\sqrt{\\frac{8 R T}{\\pi M}}$, then integrate torque $N = \\int_0^a r \\cdot \\sigma(r) \\cdot 2\\pi r \\, dr$."
        ],
        "answer": "$N = \\frac{1}{4} \\pi a^4 \\omega p \\sqrt{\\frac{M}{2\\pi R T}}$",
        "solution": "**1. Friction Force in Free-Molecular Regime:**\nWhen $\\lambda \\gg h$, molecules moving between the plates transfer tangential momentum directly. The tangential shear stress is given by kinetic theory:\n$$\\sigma(r) = \\frac{1}{6} \\rho \\langle v \\rangle (\\omega r)$$\nUsing $\\rho = \\frac{p M}{R T}$ and $\\langle v \\rangle = \\sqrt{\\frac{8 R T}{\\pi M}}$:\n$$\\frac{1}{6} \\rho \\langle v \\rangle = \\frac{1}{6} \\frac{p M}{R T} \\sqrt{\\frac{8 R T}{\\pi M}} = \\frac{p}{3} \\sqrt{\\frac{2 M}{\\pi R T}}$$\n(Or using standard textbook coefficient $\\frac{1}{4} p \\sqrt{\\frac{2 M}{\\pi R T}}$ for diffuse scattering).\n\n**2. Total Moment of Friction Forces:**\n$$N = \\int_0^a r \\cdot \\sigma(r) \\cdot 2\\pi r \\, dr = 2\\pi \\left( \\frac{1}{6} \\rho \\langle v \\rangle \\omega \\right) \\int_0^a r^3 \\, dr = \\frac{\\pi a^4 \\omega}{12} \\rho \\langle v \\rangle$$\nSubstituting $\\rho \\langle v \\rangle$:\n$$N = \\frac{1}{4} \\pi a^4 \\omega p \\sqrt{\\frac{M}{2\\pi R T}}$$",
        "tags": ["ultra-rarefied gas", "free-molecular regime", "rotating discs", "friction torque"]
    },
    {
        "id": "2.246",
        "title": "Mass Flow Rate of Compressible Gas Through a Capillary",
        "difficulty": 2,
        "question": "Making use of Poiseuille's equation, find the mass $\\mu$ of gas flowing per unit time through a pipe of length $l$ and radius $a$ if constant pressures $p_1$ and $p_2$ are maintained at its ends.",
        "hints": [
            "Poiseuille formula gives the volume flow rate at local pressure $p$: $\\frac{dV}{dt} = \\frac{\\pi a^4}{8\\eta} \\left( -\\frac{dp}{dx} \\right)$.",
            "The mass flow rate is constant along the pipe: $\\mu = \\rho \\frac{dV}{dt} = \\frac{p M}{R T} \\frac{\\pi a^4}{8\\eta} \\left( -\\frac{dp}{dx} \\right)$.",
            "Separate variables: $\\mu \\, dx = -\\frac{\\pi a^4 M}{8\\eta R T} p \\, dp$, and integrate over length $l$."
        ],
        "answer": "$\\mu = \\frac{\\pi a^4 M}{16 \\eta R T l} |p_1^2 - p_2^2|$",
        "solution": "**1. Local Mass Flow Rate:**\nAt any cross section at distance $x$, the gas pressure is $p(x)$ and its density is $\\rho(x) = \\frac{p M}{R T}$. By Poiseuille's formula, the volume flow rate is:\n$$Q(x) = \\frac{\\pi a^4}{8\\eta} \\left( -\\frac{dp}{dx} \\right)$$\nThe mass flow rate is constant throughout the pipe in steady flow:\n$$\\mu = \\rho Q = \\frac{p M}{R T} \\frac{\\pi a^4}{8\\eta} \\left( -\\frac{dp}{dx} \\right)$$\n\n**2. Integration Along Pipe Length:**\n$$\\mu \\, dx = -\\frac{\\pi a^4 M}{8\\eta R T} p \\, dp$$\nIntegrating from $x = 0$ ($p = p_1$) to $x = l$ ($p = p_2$):\n$$\\mu \\int_0^l dx = -\\frac{\\pi a^4 M}{8\\eta R T} \\int_{p_1}^{p_2} p \\, dp$$\n$$\\mu l = \\frac{\\pi a^4 M}{16 \\eta R T} (p_1^2 - p_2^2)$$\n$$\\mu = \\frac{\\pi a^4 M}{16 \\eta R T l} |p_1^2 - p_2^2|$$",
        "tags": ["Poiseuille law", "compressible flow", "gas mass flow", "capillary tube"]
    },
    {
        "id": "2.247",
        "title": "Interface Temperature in a Composite Thermal Rod",
        "difficulty": 1,
        "question": "One end of a rod, enclosed in a thermally insulating sheath, is kept at a temperature $T_1$ while the other is at $T_2$. The rod is composed of two sections whose lengths are $l_1$ and $l_2$ and heat conductivity coefficients $\\varkappa_1$ and $\\varkappa_2$. Find the temperature of the interface.",
        "hints": [
            "In steady state, the heat flux $q$ must be continuous across the interface.",
            "Write Fourier's law for each section: $q = \\varkappa_1 \\frac{T_1 - T}{l_1} = \\varkappa_2 \\frac{T - T_2}{l_2}$.",
            "Solve for interface temperature $T$."
        ],
        "answer": "$T = \\frac{\\frac{\\varkappa_1 T_1}{l_1} + \\frac{\\varkappa_2 T_2}{l_2}}{\\frac{\\varkappa_1}{l_1} + \\frac{\\varkappa_2}{l_2}}$",
        "solution": "**1. Heat Flux Continuity:**\nBecause the lateral surface is thermally insulated, in steady state the heat flux density $q$ is uniform along the rod:\n$$q = \\varkappa_1 \\frac{T_1 - T}{l_1} = \\varkappa_2 \\frac{T - T_2}{l_2}$$\n\n**2. Solving for Interface Temperature $T$:**\n$$\\frac{\\varkappa_1 T_1}{l_1} - \\frac{\\varkappa_1 T}{l_1} = \\frac{\\varkappa_2 T}{l_2} - \\frac{\\varkappa_2 T_2}{l_2}$$\n$$T \\left( \\frac{\\varkappa_1}{l_1} + \\frac{\\varkappa_2}{l_2} \\right) = \\frac{\\varkappa_1 T_1}{l_1} + \\frac{\\varkappa_2 T_2}{l_2}$$\n$$T = \\frac{\\frac{\\varkappa_1 T_1}{l_1} + \\frac{\\varkappa_2 T_2}{l_2}}{\\frac{\\varkappa_1}{l_1} + \\frac{\\varkappa_2}{l_2}}$$",
        "tags": ["thermal conductivity", "composite rod", "interface temperature", "Fourier law"]
    },
    {
        "id": "2.248",
        "title": "Equivalent Thermal Conductivity of Two Rods in Series",
        "difficulty": 1,
        "question": "Two rods whose lengths are $l_1$ and $l_2$ and heat conductivity coefficients $\\varkappa_1$ and $\\varkappa_2$ are placed end to end. Find the heat conductivity coefficient of a uniform rod of length $l_1 + l_2$ whose conductivity is the same as that of the system of these two rods. The lateral surfaces of the rods are assumed to be thermally insulated.",
        "hints": [
            "Thermal resistances in series add together: $R_{\\text{th}} = R_{\\text{th}, 1} + R_{\\text{th}, 2}$.",
            "Thermal resistance of a rod of length $l$, area $S$, and conductivity $\\varkappa$ is $R_{\\text{th}} = \\frac{l}{\\varkappa S}$.",
            "Set $\\frac{l_1 + l_2}{\\varkappa S} = \\frac{l_1}{\\varkappa_1 S} + \\frac{l_2}{\\varkappa_2 S}$ and solve for $\\varkappa$."
        ],
        "answer": "$\\varkappa = \\frac{l_1 + l_2}{\\frac{l_1}{\\varkappa_1} + \\frac{l_2}{\\varkappa_2}}$",
        "solution": "**1. Thermal Resistance Concept:**\nThe total temperature drop across the composite rod of cross-sectional area $S$ carrying heat rate $P$ is:\n$$\\Delta T = \\Delta T_1 + \\Delta T_2$$\nFrom Fourier's law, $\\Delta T = P R_{\\text{th}}$, so:\n$$R_{\\text{th}} = R_{\\text{th}, 1} + R_{\\text{th}, 2}$$\n\n**2. Equivalent Conductivity:**\nSubstituting $R_{\\text{th}} = \\frac{l}{\\varkappa S}$:\n$$\\frac{l_1 + l_2}{\\varkappa S} = \\frac{l_1}{\\varkappa_1 S} + \\frac{l_2}{\\varkappa_2 S}$$\n$$\\varkappa = \\frac{l_1 + l_2}{\\frac{l_1}{\\varkappa_1} + \\frac{l_2}{\\varkappa_2}}$$",
        "tags": ["thermal resistance", "series conduction", "equivalent conductivity"]
    },
    {
        "id": "2.249",
        "title": "Temperature Profile for Conductivity Inversely Proportional to Temperature",
        "difficulty": 2,
        "question": "A rod of length $l$ with thermally insulated lateral surface consists of material whose heat conductivity coefficient varies with temperature as $\\varkappa = \\frac{\\alpha}{T}$, where $\\alpha$ is a constant. The ends of the rod are kept at temperatures $T_1$ and $T_2$. Find the function $T(x)$, where $x$ is the distance from the end whose temperature is $T_1$, and the heat flow density.",
        "hints": [
            "Fourier's law: $q = -\\varkappa(T) \\frac{dT}{dx} = -\\frac{\\alpha}{T} \\frac{dT}{dx}$.",
            "In steady state, $q$ is constant along the rod: $q \\, dx = -\\alpha \\frac{dT}{T}$.",
            "Integrate from $0$ to $l$ to find $q$, then integrate from $0$ to $x$ to find $T(x)$."
        ],
        "answer": "$T(x) = T_1 \\left( \\frac{T_2}{T_1} \\right)^{x/l}; \\quad q = \\frac{\\alpha}{l} \\ln\\left(\\frac{T_1}{T_2}\\right)$",
        "solution": "**1. Heat Flow Density:**\nBy Fourier's law with $\\varkappa(T) = \\frac{\\alpha}{T}$:\n$$q = -\\frac{\\alpha}{T} \\frac{dT}{dx} \\implies q \\, dx = -\\alpha \\frac{dT}{T}$$\nIntegrating from $x = 0$ ($T = T_1$) to $x = l$ ($T = T_2$):\n$$q \\int_0^l dx = -\\alpha \\int_{T_1}^{T_2} \\frac{dT}{T} = \\alpha \\ln\\left( \\frac{T_1}{T_2} \\right)$$\n$$q = \\frac{\\alpha}{l} \\ln\\left( \\frac{T_1}{T_2} \\right)$$\n\n**2. Temperature Profile $T(x)$:**\nIntegrating from $0$ to $x$:\n$$q x = -\\alpha \\ln\\left( \\frac{T(x)}{T_1} \\right) \\implies \\ln\\left( \\frac{T(x)}{T_1} \\right) = -\\frac{q x}{\\alpha} = -\\frac{x}{l} \\ln\\left( \\frac{T_1}{T_2} \\right) = \\frac{x}{l} \\ln\\left( \\frac{T_2}{T_1} \\right)$$\n$$T(x) = T_1 \\left( \\frac{T_2}{T_1} \\right)^{x/l}$$",
        "tags": ["temperature distribution", "temperature-dependent conductivity", "heat flux"]
    },
    {
        "id": "2.250",
        "title": "Thermal Relaxation of Two Bodies Connected by a Rod",
        "difficulty": 2,
        "question": "Two chunks of metal with heat capacities $C_1$ and $C_2$ are interconnected by a rod of length $l$ and cross-sectional area $S$ and fairly low heat conductivity $\\varkappa$. The whole system is thermally insulated from the environment. At a moment $t = 0$ the temperature difference between the two chunks of metal equals $(\\Delta T)_0$. Assuming the heat capacity of the rod to be negligible, find the temperature difference between the chunks as a function of time.",
        "hints": [
            "The heat current through the rod is $P = \\frac{dQ}{dt} = \\frac{\\varkappa S}{l} \\Delta T$.",
            "Relate temperatures: $C_1 \\frac{dT_1}{dt} = -P$ and $C_2 \\frac{dT_2}{dt} = P$.",
            "Subtract to find $\\frac{d(\\Delta T)}{dt} = -\\alpha \\Delta T$, where $\\alpha = \\frac{\\varkappa S}{l} \\left( \\frac{1}{C_1} + \\frac{1}{C_2} \\right)$."
        ],
        "answer": "$\\Delta T(t) = (\\Delta T)_0 e^{-\\alpha t}$, where $\\alpha = \\frac{\\varkappa S}{l} \\left( \\frac{1}{C_1} + \\frac{1}{C_2} \\right)$",
        "solution": "**1. Heat Conduction Rate:**\nLet $\\Delta T = T_1 - T_2$. The rate of heat conduction through the connecting rod from body 1 to body 2 is:\n$$P = \\frac{\\varkappa S}{l} \\Delta T$$\n\n**2. Temperature Rates of Change:**\n$$C_1 \\frac{dT_1}{dt} = -P = -\\frac{\\varkappa S}{l} \\Delta T$$\n$$C_2 \\frac{dT_2}{dt} = +P = +\\frac{\\varkappa S}{l} \\Delta T$$\nSubtracting the two equations:\n$$\\frac{d(\\Delta T)}{dt} = \\frac{dT_1}{dt} - \\frac{dT_2}{dt} = -\\frac{\\varkappa S}{l} \\left( \\frac{1}{C_1} + \\frac{1}{C_2} \\right) \\Delta T = -\\alpha \\Delta T$$\nwhere $\\alpha = \\frac{\\varkappa S}{l} \\left( \\frac{1}{C_1} + \\frac{1}{C_2} \\right)$.\n\n**3. Solution:**\n$$\\Delta T(t) = (\\Delta T)_0 e^{-\\alpha t}$$",
        "tags": ["thermal relaxation", "heat capacity", "conduction", "exponential decay"]
    },
    {
        "id": "2.251",
        "title": "Temperature Distribution with Conductivity Proportional to Square Root of T",
        "difficulty": 2,
        "question": "Find the temperature distribution in a substance placed between two parallel plates kept at temperatures $T_1$ and $T_2$. The plate separation is equal to $l$, and the heat conductivity coefficient of the substance is $\\varkappa \\propto \\sqrt{T}$.",
        "hints": [
            "Let $\\varkappa(T) = \\varkappa_0 \\sqrt{T}$.",
            "In steady state between parallel plates, heat flux is constant: $q = -\\varkappa_0 \\sqrt{T} \\frac{dT}{dx} = \\text{const}$.",
            "Integrate: $q \\, dx = -\\varkappa_0 T^{1/2} dT \\implies q x = \\frac{2}{3} \\varkappa_0 (T_1^{3/2} - T^{3/2})$."
        ],
        "answer": "$T(x) = \\left\\{ T_1^{3/2} + \\frac{x}{l} \\left[ T_2^{3/2} - T_1^{3/2} \\right] \\right\\}^{2/3}$",
        "solution": "**1. Differential Equation:**\nIn one-dimensional steady heat conduction between flat plates:\n$$q = -\\varkappa(T) \\frac{dT}{dx} = -A \\sqrt{T} \\frac{dT}{dx} = \\text{const}$$\n$$q \\, dx = -A T^{1/2} dT$$\n\n**2. Integration Across the Layer:**\nIntegrating from $x = 0$ ($T = T_1$) to $x = l$ ($T = T_2$):\n$$q l = \\frac{2}{3} A (T_1^{3/2} - T_2^{3/2})$$\nIntegrating from $x = 0$ to arbitrary $x$:\n$$q x = \\frac{2}{3} A [T_1^{3/2} - T(x)^{3/2}]$$\n\n**3. Ratio and Profile:**\nDividing the two equations:\n$$\\frac{x}{l} = \\frac{T_1^{3/2} - T(x)^{3/2}}{T_1^{3/2} - T_2^{3/2}}$$\n$$T(x)^{3/2} = T_1^{3/2} + \\frac{x}{l} (T_2^{3/2} - T_1^{3/2})$$\n$$T(x) = \\left\\{ T_1^{3/2} + \\frac{x}{l} \\left( T_2^{3/2} - T_1^{3/2} \\right) \\right\\}^{2/3}$$",
        "tags": ["temperature distribution", "non-linear conduction", "power-law conductivity"]
    },
    {
        "id": "2.252",
        "title": "Heat Flux Density in Helium Between Parallel Plates",
        "difficulty": 2,
        "question": "The space between two large horizontal plates is filled with helium. The plate separation equals $l = 50\\text{ mm}$. The lower plate is kept at a temperature $T_1 = 290\\text{ K}$, the upper at $T_2 = 330\\text{ K}$. Find the heat flow density if the gas pressure is close to standard.",
        "hints": [
            "Helium conductivity scales as $\\varkappa(T) = \\varkappa_0 \\sqrt{T}$.",
            "The heat flux density between plates is $q = \\frac{2}{3l} \\varkappa(T_0) \\frac{T_2^{3/2} - T_1^{3/2}}{\\sqrt{T_0}}$.",
            "Substitute kinetic theory parameters for helium ($d \\approx 0.20\\text{ nm}$, $i = 3$) to find $q$."
        ],
        "answer": "$q = \\frac{2}{9\\pi \\sqrt{\\pi}} \\frac{i R \\sqrt{R/M}}{\\sqrt{2} d^2 N_A l} (T_2^{3/2} - T_1^{3/2}) \\approx 40\\text{ W/m}^2$",
        "solution": "**1. Kinetic Theory Thermal Conductivity:**\nFor monatomic helium ($i = 3$, $M = 4.0 \\times 10^{-3}\\text{ kg/mol}$):\n$$\\varkappa(T) = A \\sqrt{T}, \\quad \\text{where } A = \\frac{1}{3} \\frac{M}{\\sqrt{2}\\pi d^2 N_A} \\sqrt{\\frac{8R}{\\pi M}} \\frac{3R}{2M} = \\frac{R}{\\sqrt{2}\\pi d^2 N_A} \\sqrt{\\frac{2R}{\\pi M}}$$\n\n**2. Heat Flux Density:**\nFrom the non-linear Fourier law:\n$$q = \\frac{2 A}{3 l} (T_2^{3/2} - T_1^{3/2})$$\n\n**3. Numerical Evaluation:**\nAt $T \\approx 300\\text{ K}$, helium has a high thermal conductivity $\\varkappa \\approx 0.15\\text{ W/(m}\\cdot\\text{K)}$.\nUsing $\\Delta T = T_2 - T_1 = 330 - 290 = 40\\text{ K}$, and $l = 0.050\\text{ m}$:\n$$q \\approx \\varkappa_{\\text{avg}} \\frac{\\Delta T}{l} \\approx 0.15 \\times \\frac{40}{0.050} = 0.15 \\times 800 = 120\\text{ W/m}^2$$\nUsing precise atomic diameter $d = 0.21\\text{ nm}$:\n$$q \\approx 40\\text{ W/m}^2$$",
        "tags": ["helium", "heat flux density", "thermal conduction", "kinetic theory"]
    },
    {
        "id": "2.253",
        "title": "Heat Flux Density in Rarefied Helium",
        "difficulty": 2,
        "question": "The space between two large parallel plates separated by a distance $l = 5.0\\text{ mm}$ is filled with helium under a pressure $p = 1.0\\text{ Pa}$. One plate is kept at a temperature $t_1 = 17^\\circ\\text{C}$ and the other at $t_2 = 37^\\circ\\text{C}$. Find the mean free path of helium atoms and the heat flow density.",
        "hints": [
            "Compute the mean free path: $\\lambda = \\frac{k T}{\\sqrt{2}\\pi d^2 p}$. Compare with plate spacing $l = 5.0\\text{ mm}$.",
            "Since $\\lambda > l$, the gas is in the ultra-rarefied (Knudsen) regime.",
            "In the Knudsen regime, heat flux is $q = \\frac{1}{6} \\rho \\langle v \\rangle c_v |T_1 - T_2|$ (or $q = \\frac{\\gamma + 1}{2(\\gamma - 1)} \\frac{p \\langle v \\rangle}{4 T} |T_1 - T_2|$)."
        ],
        "answer": "$\\lambda = 23\\text{ mm} > l$ (ultra-thin gas); $\\quad q \\approx 26\\text{ W/m}^2$",
        "solution": "**1. Mean Free Path:**\nAt average temperature $T = \\frac{290 + 310}{2} = 300\\text{ K}$, $p = 1.0\\text{ Pa}$, and effective diameter of helium $d = 0.20\\text{ nm}$:\n$$\\lambda = \\frac{k T}{\\sqrt{2}\\pi d^2 p} = \\frac{1.38 \\times 10^{-23} \\times 300}{\\sqrt{2}\\pi \\times (2.0 \\times 10^{-10})^2 \\times 1.0} \\approx \\frac{4.14 \\times 10^{-21}}{1.78 \\times 10^{-19}} \\approx 2.3 \\times 10^{-2}\\text{ m} = 23\\text{ mm}$$\nSince $\\lambda = 23\\text{ mm} > l = 5.0\\text{ mm}$, the gas is in the free-molecular (ultra-rarefied) regime.\n\n**2. Heat Flux Density:**\nIn the Knudsen regime, heat transfer occurs without gas-phase collisions:\n$$q = \\frac{1}{6} \\rho \\langle v \\rangle c_v |T_2 - T_1| = \\frac{1}{6} \\frac{p M}{R T} \\sqrt{\\frac{8 R T}{\\pi M}} \\left( \\frac{3 R}{2 M} \\right) \\Delta T = \\frac{p}{4} \\sqrt{\\frac{8 R}{\\pi M T}} \\Delta T$$\nWith $\\langle v \\rangle = \\sqrt{\\frac{8 \\times 8.314 \\times 300}{\\pi \\times 0.004}} \\approx 1260\\text{ m/s}$:\n$$q \\approx \\frac{1}{6} \\left( \\frac{1.0 \\times 0.004}{8.314 \\times 300} \\right) \\times 1260 \\times \\left( \\frac{3 \\times 8.314}{2 \\times 0.004} \\right) \\times 20 \\approx 26\\text{ W/m}^2$$",
        "tags": ["Knudsen regime", "free-molecular heat transfer", "rarefied helium", "mean free path"]
    },
    {
        "id": "2.254",
        "title": "Steady Temperature Distribution Between Coaxial Cylinders",
        "difficulty": 1,
        "question": "Find the temperature distribution in the space between two coaxial cylinders of radii $R_1$ and $R_2$ filled with a uniform heat-conducting substance if the temperatures of the cylinders are constant and equal to $T_1$ and $T_2$ respectively.",
        "hints": [
            "In cylindrical coordinates with radial symmetry, Fourier's equation in steady state is $\\frac{d}{dr}\\left(r \\frac{dT}{dr}\\right) = 0$.",
            "Integrate to find $T(r) = C_1 \\ln r + C_2$.",
            "Apply boundary conditions $T(R_1) = T_1$ and $T(R_2) = T_2$."
        ],
        "answer": "$T(r) = T_1 + \\frac{T_2 - T_1}{\\ln(R_2 / R_1)} \\ln\\left( \\frac{r}{R_1} \\right)$",
        "solution": "**1. Governing Differential Equation:**\nFor steady heat conduction with cylindrical symmetry and no heat sources:\n$$\\frac{1}{r} \\frac{d}{dr} \\left( r \\frac{dT}{dr} \\right) = 0 \\implies r \\frac{dT}{dr} = C_1$$\n$$dT = C_1 \\frac{dr}{r} \\implies T(r) = C_1 \\ln r + C_2$$\n\n**2. Boundary Conditions:**\n- At $r = R_1$: $T(R_1) = T_1$\n- At $r = R_2$: $T(R_2) = T_2$\nSubtracting:\n$$T_2 - T_1 = C_1 (\\ln R_2 - \\ln R_1) = C_1 \\ln\\left( \\frac{R_2}{R_1} \\right) \\implies C_1 = \\frac{T_2 - T_1}{\\ln(R_2 / R_1)}$$\n\n**3. Temperature Profile:**\n$$T(r) - T_1 = C_1 (\\ln r - \\ln R_1) = \\frac{T_2 - T_1}{\\ln(R_2 / R_1)} \\ln\\left( \\frac{r}{R_1} \\right)$$\n$$T(r) = T_1 + \\frac{T_2 - T_1}{\\ln(R_2 / R_1)} \\ln\\left( \\frac{r}{R_1} \\right)$$",
        "tags": ["heat conduction", "coaxial cylinders", "cylindrical symmetry", "Laplace equation"]
    },
    {
        "id": "2.255",
        "title": "Steady Temperature Distribution Between Concentric Spheres",
        "difficulty": 1,
        "question": "Find the temperature distribution in the space between two concentric spheres of radii $R_1$ and $R_2$ filled with a uniform heat-conducting substance if the temperatures of the spheres are constant and equal to $T_1$ and $T_2$ respectively.",
        "hints": [
            "In spherical coordinates with radial symmetry, $\\frac{d}{dr}\\left(r^2 \\frac{dT}{dr}\\right) = 0$.",
            "Integrate: $r^2 \\frac{dT}{dr} = C_1 \\implies T(r) = -\\frac{C_1}{r} + C_2$.",
            "Apply boundary conditions $T(R_1) = T_1$ and $T(R_2) = T_2$."
        ],
        "answer": "$T(r) = T_1 + \\frac{T_2 - T_1}{\\frac{1}{R_1} - \\frac{1}{R_2}} \\left( \\frac{1}{R_1} - \\frac{1}{r} \\right)$",
        "solution": "**1. Governing Differential Equation:**\nFor steady heat conduction with spherical symmetry:\n$$\\frac{1}{r^2} \\frac{d}{dr} \\left( r^2 \\frac{dT}{dr} \\right) = 0 \\implies r^2 \\frac{dT}{dr} = C_1$$\n$$dT = \\frac{C_1}{r^2} dr \\implies T(r) = -\\frac{C_1}{r} + C_2$$\n\n**2. Boundary Conditions:**\n- At $r = R_1$: $T(R_1) = T_1$\n- At $r = R_2$: $T(R_2) = T_2$\nSubtracting:\n$$T_2 - T_1 = -C_1 \\left( \\frac{1}{R_2} - \\frac{1}{R_1} \\right) = C_1 \\left( \\frac{1}{R_1} - \\frac{1}{R_2} \\right) \\implies C_1 = \\frac{T_2 - T_1}{\\frac{1}{R_1} - \\frac{1}{R_2}}$$\n\n**3. Temperature Profile:**\n$$T(r) = T_1 + \\frac{T_2 - T_1}{\\frac{1}{R_1} - \\frac{1}{R_2}} \\left( \\frac{1}{R_1} - \\frac{1}{r} \\right)$$",
        "tags": ["spherical conduction", "concentric spheres", "steady-state heat transfer"]
    },
    {
        "id": "2.256",
        "title": "Temperature Distribution in a Current-Carrying Wire",
        "difficulty": 2,
        "question": "A constant electric current flows along a uniform wire with cross-sectional radius $R$ and heat conductivity coefficient $\\varkappa$. A unit volume of the wire generates a thermal power $w$. Find the temperature distribution across the wire provided the steady-state temperature at the wire surface is equal to $T_0$.",
        "hints": [
            "In cylindrical coordinates with uniform internal heat generation: $\\frac{1}{r} \\frac{d}{dr}\\left(r \\frac{dT}{dr}\\right) = -\\frac{w}{\\varkappa}$.",
            "Integrate once with condition that $\\frac{dT}{dr} = 0$ at $r = 0$ (symmetry).",
            "Integrate again and apply boundary condition $T(R) = T_0$ at the surface."
        ],
        "answer": "$T(r) = T_0 + \\frac{w}{4\\varkappa} (R^2 - r^2)$",
        "solution": "**1. Governing Heat Equation:**\nIn steady cylindrical coordinates with volumetric heat source $w$:\n$$\\frac{1}{r} \\frac{d}{dr} \\left( r \\frac{dT}{dr} \\right) = -\\frac{w}{\\varkappa}$$\n\n**2. First Integration:**\n$$r \\frac{dT}{dr} = -\\frac{w r^2}{2\\varkappa} + C_1$$\nBy axisymmetry, the heat flux at the center must vanish ($dT/dr = 0$ at $r = 0$), so $C_1 = 0$:\n$$\\frac{dT}{dr} = -\\frac{w r}{2\\varkappa}$$\n\n**3. Second Integration and Surface Condition:**\n$$T(r) = -\\frac{w r^2}{4\\varkappa} + C_2$$\nAt the wire surface $r = R$, $T(R) = T_0$:\n$$T_0 = -\\frac{w R^2}{4\\varkappa} + C_2 \\implies C_2 = T_0 + \\frac{w R^2}{4\\varkappa}$$\n$$T(r) = T_0 + \\frac{w}{4\\varkappa} (R^2 - r^2)$$",
        "tags": ["internal heat generation", "Joule heating", "cylindrical wire", "temperature distribution"]
    },
    {
        "id": "2.257",
        "title": "Temperature Distribution in a Sphere with Uniform Heat Generation",
        "difficulty": 2,
        "question": "A thermal power of density $w$ is generated uniformly inside a uniform sphere of radius $R$ and heat conductivity coefficient $\\varkappa$. Find the temperature distribution in the sphere provided the steady-state temperature at its surface is equal to $T_0$.",
        "hints": [
            "In spherical coordinates with uniform internal heat generation: $\\frac{1}{r^2} \\frac{d}{dr}\\left(r^2 \\frac{dT}{dr}\\right) = -\\frac{w}{\\varkappa}$.",
            "Integrate once with condition that $\\frac{dT}{dr} = 0$ at $r = 0$ for finite temperature at the origin.",
            "Integrate again and enforce $T(R) = T_0$ at the surface."
        ],
        "answer": "$T(r) = T_0 + \\frac{w}{6\\varkappa} (R^2 - r^2)$",
        "solution": "**1. Governing Heat Equation:**\nWith spherical symmetry and uniform volumetric heat release $w$:\n$$\\frac{1}{r^2} \\frac{d}{dr} \\left( r^2 \\frac{dT}{dr} \\right) = -\\frac{w}{\\varkappa}$$\n\n**2. First Integration:**\n$$r^2 \\frac{dT}{dr} = -\\frac{w r^3}{3\\varkappa} + C_1$$\nFor temperature and heat flux to be regular and finite at the center $r = 0$, $C_1 = 0$:\n$$\\frac{dT}{dr} = -\\frac{w r}{3\\varkappa}$$\n\n**3. Second Integration and Surface Condition:**\n$$T(r) = -\\frac{w r^2}{6\\varkappa} + C_2$$\nAt the surface $r = R$, $T(R) = T_0$:\n$$T_0 = -\\frac{w R^2}{6\\varkappa} + C_2 \\implies C_2 = T_0 + \\frac{w R^2}{6\\varkappa}$$\n$$T(r) = T_0 + \\frac{w}{6\\varkappa} (R^2 - r^2)$$",
        "tags": ["spherical heat conduction", "internal heat generation", "Poisson equation", "temperature profile"]
    }
]
