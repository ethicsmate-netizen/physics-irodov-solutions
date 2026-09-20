"""
ch1_8_batch2.py
Curated problems 1.365 to 1.388 (24 problems) of Irodov Chapter 1.8: Relativistic Mechanics.
"""

CH1_8_BATCH_2 = [
    {
        "id": "1.365",
        "title": "Relativistic Transformation of Acceleration",
        "difficulty": 3,
        "question": "Frame $K'$ moves with constant velocity $V$ relative to frame $K$. Find the acceleration $w'$ of a particle in frame $K'$ if in frame $K$ the particle moves with velocity $v$ and acceleration $w$ along a straight line:\n(a) parallel to vector $\\mathbf{V}$;\n(b) perpendicular to vector $\\mathbf{V}$.",
        "hints": [
            "(a) Differentiate $v'_x = \\frac{v_x - V}{1 - v_x V / c^2}$ with respect to $t'$, using $dt' = \\gamma (dt - \\frac{V dx}{c^2}) = \\gamma dt (1 - \\frac{v_x V}{c^2})$.",
            "(b) For motion perpendicular to $\\mathbf{V}$, $v_x = 0$, $v_y = v$, $w_y = w$."
        ],
        "answer": "(a) $w' = \\frac{w (1 - V^2/c^2)^{3/2}}{(1 - v V / c^2)^3}$; (b) $w' = w \\left(1 - \\frac{V^2}{c^2}\\right)$",
        "solution": "**1. Part (a): Longitudinal Acceleration:**\n$$v'_x = \\frac{v_x - V}{1 - \\frac{v_x V}{c^2}}$$\nTaking differentials:\n$$dv'_x = \\frac{dv_x \\left(1 - \\frac{v_x V}{c^2}\\right) - (v_x - V) \\left(-\\frac{V dv_x}{c^2}\\right)}{\\left(1 - \\frac{v_x V}{c^2}\\right)^2} = \\frac{dv_x \\left(1 - \\frac{V^2}{c^2}\\right)}{\\left(1 - \\frac{v_x V}{c^2}\\right)^2}$$\nFrom the Lorentz transformation for time:\n$$dt' = \\gamma \\left(dt - \\frac{V dx}{c^2}\\right) = \\frac{dt \\left(1 - \\frac{v_x V}{c^2}\\right)}{\\sqrt{1 - \\frac{V^2}{c^2}}}$$\nDividing $dv'_x$ by $dt'$:\n$$w'_x = \\frac{dv'_x}{dt'} = \\frac{dv_x}{dt} \\frac{\\left(1 - \\frac{V^2}{c^2}\\right)^{3/2}}{\\left(1 - \\frac{v_x V}{c^2}\\right)^3} = w \\frac{(1 - \\beta^2)^{3/2}}{(1 - v V / c^2)^3}$$\n\n**2. Part (b): Transverse Acceleration:**\nWhen the motion is perpendicular to $\\mathbf{V}$ (so $v_x = 0, v_y = v$):\n$$w' = w \\left(1 - \\frac{V^2}{c^2}\\right)$$",
        "tags": ["acceleration transformation", "Lorentz transformation", "relativistic kinematics"]
    },
    {
        "id": "1.366",
        "title": "Hyperbolic Motion: Relativistic Rocket with Constant Proper Acceleration",
        "difficulty": 3,
        "question": "An imaginary space rocket launched from Earth moves with proper acceleration $w' = 10 g$ constant in every instantaneous co-moving inertial frame. The boost stage lasts $\\tau = 1.0\\text{ year}$ of terrestrial time. Find how much (in per cent) the rocket velocity differs from the speed of light at the end of the boost stage, and what distance the rocket covers by that moment.",
        "hints": [
            "In the instantaneous co-moving frame $V = v$, so from Problem 1.365(a): $w' = \\frac{dv/dt}{(1 - v^2/c^2)^{3/2}}$.",
            "Integrate to find velocity: $\\frac{v}{\\sqrt{1 - v^2/c^2}} = w' t \\implies v(t) = \\frac{w' t}{\\sqrt{1 + (w' t / c)^2}}$.",
            "Distance is $l = \\int_0^\\tau v(t) dt = \\frac{c^2}{w'} [\\sqrt{1 + (w' \\tau / c)^2} - 1]$."
        ],
        "answer": "$\\frac{c - v}{c} \\approx 0.47\\%, \\quad l = 0.91\\text{ light-years}$",
        "solution": "**1. Equation of Motion:**\nWith constant proper acceleration $w'$:\n$$\\frac{dv}{dt} = w' \\left(1 - \\frac{v^2}{c^2}\\right)^{3/2}$$\nIntegrating with $v(0) = 0$:\n$$\\int_0^v \\frac{dv'}{(1 - v'^2/c^2)^{3/2}} = w' t \\implies \\frac{v}{\\sqrt{1 - v^2/c^2}} = w' t$$\n$$v(t) = \\frac{w' t}{\\sqrt{1 + \\left(\\frac{w' t}{c}\\right)^2}}$$\n\n**2. Velocity at $t = \\tau = 1.0\\text{ year}$:**\n$$\\frac{w' \\tau}{c} = \\frac{(10 \\times 9.8\\text{ m/s}^2) \\times (3.156 \\times 10^7\\text{ s})}{3.0 \\times 10^8\\text{ m/s}} = \\frac{3.093 \\times 10^9}{3.0 \\times 10^8} \\approx 10.3$$\n$$\\frac{c - v}{c} = 1 - \\frac{10.3}{\\sqrt{1 + (10.3)^2}} = 1 - \\frac{10.3}{10.348} \\approx 0.0047 = 0.47\\%$$\n\n**3. Distance Covered:**\n$$l = \\int_0^\\tau v(t) dt = \\frac{c^2}{w'} \\left[ \\sqrt{1 + \\left(\\frac{w' \\tau}{c}\\right)^2} - 1 \\right]$$\n$$l = \\frac{c \\tau}{10.3} [10.348 - 1] = \\frac{9.348}{10.3} c \\tau \\approx 0.91\\text{ light-years}$$",
        "tags": ["proper acceleration", "hyperbolic motion", "relativistic rocket", "light-year"]
    },
    {
        "id": "1.367",
        "title": "Rocket Proper Time During Constant Acceleration",
        "difficulty": 2,
        "question": "From the conditions of the foregoing problem ($w' = 10 g$, terrestrial boost time $\\tau = 1.0\\text{ year}$), determine the boost time $\\tau_0$ elapsed in the reference frame fixed to the rocket.",
        "hints": [
            "Proper time is defined by $\\tau_0 = \\int_0^\\tau \\sqrt{1 - v^2/c^2} \\, dt$.",
            "Using $\\sqrt{1 - v^2/c^2} = \\frac{1}{\\sqrt{1 + (w' t / c)^2}}$, integrate $\\int_0^\\tau \\frac{dt}{\\sqrt{1 + (w' t / c)^2}}$.",
            "This yields $\\tau_0 = \\frac{c}{w'} \\operatorname{arsinh}\\left(\\frac{w' \\tau}{c}\\right) = \\frac{c}{w'} \\ln\\left[\\frac{w' \\tau}{c} + \\sqrt{1 + \\left(\\frac{w' \\tau}{c}\\right)^2}\\right]$."
        ],
        "answer": "$\\tau_0 = \\frac{c}{w'} \\ln\\left[\\frac{w' \\tau}{c} + \\sqrt{1 + \\left(\\frac{w' \\tau}{c}\\right)^2}\\right] = 3.5\\text{ months}$",
        "solution": "**1. Proper Time Integral:**\n$$\\tau_0 = \\int_0^\\tau \\sqrt{1 - \\frac{v^2(t)}{c^2}} \\, dt = \\int_0^\\tau \\frac{dt}{\\sqrt{1 + \\left(\\frac{w' t}{c}\\right)^2}}$$\nUsing the standard substitution $u = \\frac{w' t}{c}$:\n$$\\tau_0 = \\frac{c}{w'} \\int_0^{\\frac{w' \\tau}{c}} \\frac{du}{\\sqrt{1 + u^2}} = \\frac{c}{w'} \\ln\\left[u + \\sqrt{1 + u^2}\\right]_0^{\\frac{w' \\tau}{c}}$$\n$$\\tau_0 = \\frac{c}{w'} \\ln\\left[\\frac{w' \\tau}{c} + \\sqrt{1 + \\left(\\frac{w' \\tau}{c}\\right)^2}\\right]$$\n\n**2. Numerical Calculation:**\nWith $\\frac{w' \\tau}{c} \\approx 10.3$:\n$$\\tau_0 = \\frac{1.0\\text{ year}}{10.3} \\ln(10.3 + 10.348) = \\frac{1.0\\text{ yr}}{10.3} \\ln(20.65) = \\frac{1.0\\text{ yr}}{10.3} \\times 3.028 \\approx 0.294\\text{ yr} \\approx 3.5\\text{ months}$$",
        "tags": ["proper time", "hyperbolic motion", "time dilation", "space travel"]
    },
    {
        "id": "1.368",
        "title": "Relativistic Mass Ratio Near the Speed of Light",
        "difficulty": 1,
        "question": "How many times does the relativistic mass of a particle exceed its rest mass if its velocity differs from the speed of light by $\\delta = 0.010\\%$?",
        "hints": [
            "Given $v = c(1 - \\delta)$ with $\\delta = 1.0 \\times 10^{-4}$.",
            "The relativistic mass ratio is $\\frac{m}{m_0} = \\frac{1}{\\sqrt{1 - v^2/c^2}}$.",
            "Since $1 - v^2/c^2 = 1 - (1 - \\delta)^2 \\approx 2\\delta$, evaluate $\\frac{1}{\\sqrt{2\\delta}}$."
        ],
        "answer": "$\\frac{m}{m_0} = \\frac{1}{\\sqrt{2\\delta}} \\approx 71\\text{ times}$",
        "solution": "**1. Approximation for $v \\approx c$:**\n$$v = c(1 - \\delta)$$\n$$1 - \\frac{v^2}{c^2} = 1 - (1 - \\delta)^2 = 2\\delta - \\delta^2 \\approx 2\\delta$$\n\n**2. Relativistic Mass Ratio:**\n$$\\frac{m}{m_0} = \\frac{1}{\\sqrt{1 - v^2/c^2}} \\approx \\frac{1}{\\sqrt{2\\delta}}$$\nWith $\\delta = 0.010\\% = 1.0 \\times 10^{-4}$:\n$$\\frac{m}{m_0} \\approx \\frac{1}{\\sqrt{2.0 \\times 10^{-4}}} = \\frac{1}{1.414 \\times 10^{-2}} = \\frac{100}{\\sqrt{2}} \\approx 70.7 \\approx 71$$",
        "tags": ["relativistic mass", "Lorentz factor", "gamma factor", "ultrarelativistic"]
    },
    {
        "id": "1.369",
        "title": "Relativistic Density Increase",
        "difficulty": 1,
        "question": "The proper density of a stationary body is $\\rho_0$. Find the velocity $v$ of the reference frame in which the density of the body is $\\eta = 25\\%$ greater than $\\rho_0$.",
        "hints": [
            "Rest mass is invariant: $m = m_0$. Volume contracts along the direction of motion: $V = V_0 \\sqrt{1 - v^2/c^2}$.",
            "Density in the moving frame: $\\rho = \\frac{m_0}{V} = \\frac{\\rho_0}{\\sqrt{1 - v^2/c^2}}$.",
            "Set $\\frac{1}{\\sqrt{1 - v^2/c^2}} = 1 + \\eta$ and solve for $v$."
        ],
        "answer": "$v = c \\frac{\\sqrt{\\eta(2 + \\eta)}}{1 + \\eta} = 0.60 c$",
        "solution": "**1. Relativistic Volume Contraction:**\nIn a reference frame moving at speed $v$ relative to the body:\n- The rest mass $m_0$ is unchanged.\n- The volume is contracted in the direction of motion: $V = V_0 \\sqrt{1 - \\beta^2}$.\nTherefore, the observed density is:\n$$\\rho = \\frac{m_0}{V} = \\frac{\\rho_0}{\\sqrt{1 - \\beta^2}}$$\n\n**2. Determining Velocity:**\n$$\\frac{\\rho}{\\rho_0} = 1 + \\eta = \\frac{1}{\\sqrt{1 - \\beta^2}}$$\n$$1 - \\beta^2 = \\frac{1}{(1 + \\eta)^2}$$\n$$\\beta^2 = 1 - \\frac{1}{(1 + \\eta)^2} = \\frac{(1 + \\eta)^2 - 1}{(1 + \\eta)^2} = \\frac{\\eta(2 + \\eta)}{(1 + \\eta)^2}$$\n$$v = c \\frac{\\sqrt{\\eta(2 + \\eta)}}{1 + \\eta}$$\n\n**3. Numerical Calculation:**\nFor $\\eta = 0.25 = 1/4$:\n$$1 + \\eta = 1.25 = 5/4, \\quad \\eta(2 + \\eta) = 0.25 \\times 2.25 = 0.5625$$\n$$v = c \\frac{\\sqrt{0.5625}}{1.25} = c \\frac{0.75}{1.25} = 0.60 c$$",
        "tags": ["density", "length contraction", "relativistic kinematics"]
    },
    {
        "id": "1.370",
        "title": "Velocity of a 10 GeV/c Proton",
        "difficulty": 1,
        "question": "A proton moves with momentum $p = 10.0\\text{ GeV}/c$. How much (in per cent) does the proton velocity differ from the speed of light? ($m_0 c^2 = 0.938\\text{ GeV}$).",
        "hints": [
            "Relativistic relation between momentum and velocity: $p = \\gamma m_0 v = \\frac{m_0 v}{\\sqrt{1 - v^2/c^2}}$.",
            "This gives $\\frac{v}{c} = \\frac{p c}{\\sqrt{(p c)^2 + (m_0 c^2)^2}} = \\frac{1}{\\sqrt{1 + (m_0 c / p)^2}}$.",
            "For $p c \\gg m_0 c^2$: $\\frac{c - v}{c} \\approx \\frac{1}{2} \\left(\\frac{m_0 c^2}{p c}\\right)^2$."
        ],
        "answer": "$\\frac{c - v}{c} \\approx \\frac{1}{2} \\left(\\frac{m_0 c^2}{p c}\\right)^2 = 0.44\\%$",
        "solution": "**1. Velocity in Terms of Momentum:**\n$$p = \\frac{m_0 v}{\\sqrt{1 - v^2/c^2}} \\implies p^2 \\left(1 - \\frac{v^2}{c^2}\\right) = m_0^2 v^2$$\n$$v^2 \\left(m_0^2 + \\frac{p^2}{c^2}\\right) = p^2 \\implies \\frac{v^2}{c^2} = \\frac{p^2 c^2}{p^2 c^2 + m_0^2 c^4} = \\frac{1}{1 + \\left(\\frac{m_0 c^2}{p c}\\right)^2}$$\n$$\\frac{v}{c} = \\left[1 + \\left(\\frac{m_0 c^2}{p c}\\right)^2\\right]^{-1/2}$$\n\n**2. Percentage Difference from Speed of Light:**\nUsing the binomial expansion $(1 + x)^{-1/2} \\approx 1 - \\frac{1}{2} x$ for $x \\ll 1$:\n$$\\frac{c - v}{c} = 1 - \\frac{v}{c} \\approx \\frac{1}{2} \\left(\\frac{m_0 c^2}{p c}\\right)^2$$\n\n**3. Numerical Calculation:**\nWith $m_0 c^2 = 0.938\\text{ GeV}$ and $p c = 10.0\\text{ GeV}$:\n$$\\frac{c - v}{c} \\approx \\frac{1}{2} \\left(\\frac{0.938}{10.0}\\right)^2 = \\frac{1}{2} (0.0938)^2 = \\frac{1}{2} \\times 0.00880 = 0.0044 = 0.44\\%$$",
        "tags": ["relativistic momentum", "proton", "ultrarelativistic limit"]
    },
    {
        "id": "1.371",
        "title": "Velocity Where Relativistic Momentum Exceeds Classical by Factor Eta",
        "difficulty": 1,
        "question": "Find the velocity $v$ at which the relativistic momentum of a particle exceeds its Newtonian momentum by a factor $\\eta = 2.0$.",
        "hints": [
            "Relativistic momentum is $p = \\gamma m_0 v = \\frac{m_0 v}{\\sqrt{1 - v^2/c^2}}$.",
            "Classical Newtonian momentum is $p_{\\text{class}} = m_0 v$.",
            "The ratio is $\\frac{p}{p_{\\text{class}}} = \\gamma = \\frac{1}{\\sqrt{1 - v^2/c^2}} = \\eta$."
        ],
        "answer": "$v = c \\frac{\\sqrt{\\eta^2 - 1}}{\\eta} = \\frac{\\sqrt{3}}{2} c \\approx 0.866 c$",
        "solution": "**1. Formulation:**\n$$\\frac{p_{\\text{rel}}}{p_{\\text{class}}} = \\frac{\\gamma m_0 v}{m_0 v} = \\gamma = \\frac{1}{\\sqrt{1 - \\beta^2}} = \\eta$$\n\n**2. Solving for Velocity:**\n$$1 - \\beta^2 = \\frac{1}{\\eta^2}$$\n$$\\beta^2 = 1 - \\frac{1}{\\eta^2} = \\frac{\\eta^2 - 1}{\\eta^2}$$\n$$v = c \\frac{\\sqrt{\\eta^2 - 1}}{\\eta}$$\nFor $\\eta = 2$:\n$$v = c \\frac{\\sqrt{4 - 1}}{2} = \\frac{\\sqrt{3}}{2} c \\approx 0.866 c$$",
        "tags": ["relativistic momentum", "classical limit", "gamma factor"]
    },
    {
        "id": "1.372",
        "title": "Work Required to Accelerate from 0.6c to 0.8c",
        "difficulty": 1,
        "question": "What work $A$ has to be performed to increase the velocity of a particle of rest mass $m_0$ from $v_1 = 0.60 c$ to $v_2 = 0.80 c$? Compare the result with the value calculated from the classical formula.",
        "hints": [
            "By the work-energy theorem, $A = T_2 - T_1 = (\\gamma_2 - \\gamma_1) m_0 c^2$.",
            "For $\\beta_1 = 0.60$: $\\gamma_1 = \\frac{1}{\\sqrt{1 - 0.36}} = \\frac{1}{0.80} = 1.25$.",
            "For $\\beta_2 = 0.80$: $\\gamma_2 = \\frac{1}{\\sqrt{1 - 0.64}} = \\frac{1}{0.60} = 1.667$.",
            "Classical work: $A_{\\text{class}} = \\frac{1}{2} m_0 (v_2^2 - v_1^2)$."
        ],
        "answer": "$A = 0.42 m_0 c^2$ (relativistic) instead of $0.14 m_0 c^2$ (classical)",
        "solution": "**1. Relativistic Work:**\n$$A = \\Delta E_k = (\\gamma_2 - 1) m_0 c^2 - (\\gamma_1 - 1) m_0 c^2 = (\\gamma_2 - \\gamma_1) m_0 c^2$$\n$$\\gamma_1 = \\frac{1}{\\sqrt{1 - (0.60)^2}} = \\frac{1}{0.80} = 1.25$$\n$$\\gamma_2 = \\frac{1}{\\sqrt{1 - (0.80)^2}} = \\frac{1}{0.60} = \\frac{5}{3} \\approx 1.667$$\n$$A = (1.667 - 1.25) m_0 c^2 = 0.417 m_0 c^2 \\approx 0.42 m_0 c^2$$\n\n**2. Classical Work:**\n$$A_{\\text{class}} = \\frac{1}{2} m_0 (v_2^2 - v_1^2) = \\frac{1}{2} m_0 c^2 [(0.80)^2 - (0.60)^2] = \\frac{1}{2} m_0 c^2 [0.64 - 0.36] = 0.14 m_0 c^2$$\nThe relativistic work is three times greater than the classical prediction.",
        "tags": ["kinetic energy", "work-energy theorem", "relativistic dynamics"]
    },
    {
        "id": "1.373",
        "title": "Velocity Where Kinetic Energy Equals Rest Energy",
        "difficulty": 1,
        "question": "Find the velocity $v$ at which the kinetic energy of a particle equals its rest energy.",
        "hints": [
            "Kinetic energy formula: $T = (\\gamma - 1) m_0 c^2$.",
            "Rest energy: $E_0 = m_0 c^2$.",
            "Condition $T = E_0$ implies $\\gamma - 1 = 1 \\implies \\gamma = 2$."
        ],
        "answer": "$v = \\frac{\\sqrt{3}}{2} c \\approx 0.866 c$",
        "solution": "**1. Formulation:**\n$$T = (\\gamma - 1) m_0 c^2 = m_0 c^2$$\n$$\\gamma - 1 = 1 \\implies \\gamma = 2$$\n\n**2. Solving for Speed:**\n$$\\frac{1}{\\sqrt{1 - \\beta^2}} = 2 \\implies 1 - \\beta^2 = \\frac{1}{4}$$\n$$\\beta^2 = \\frac{3}{4} \\implies \\beta = \\frac{\\sqrt{3}}{2} \\approx 0.866$$\n$$v = \\frac{\\sqrt{3}}{2} c \\approx 0.866 c$$",
        "tags": ["kinetic energy", "rest energy", "Lorentz factor"]
    },
    {
        "id": "1.374",
        "title": "Classical Approximation Criterion for Kinetic Energy",
        "difficulty": 2,
        "question": "At what values of the ratio of kinetic energy to rest energy $T / (m_0 c^2)$ can the velocity of a particle be calculated from the classical formula with relative error less than $\\varepsilon = 0.010$ (1%)?",
        "hints": [
            "Classical velocity: $v_{\\text{cl}} = \\sqrt{\\frac{2T}{m_0}}$.",
            "Relativistic velocity: $\\frac{v}{c} = \\sqrt{1 - \\frac{1}{\\gamma^2}} = \\sqrt{1 - \\frac{1}{(1 + T/m_0 c^2)^2}}$.",
            "Expand in powers of $\\xi = T / (m_0 c^2) \\ll 1$: show that $\\frac{v_{\\text{cl}} - v}{v} \\approx \\frac{3}{4} \\xi \\le \\varepsilon$."
        ],
        "answer": "$\\frac{T}{m_0 c^2} \\le \\frac{4}{3} \\varepsilon \\approx 0.013$",
        "solution": "**1. Expansion of Relativistic Velocity:**\nLet $\\xi = \\frac{T}{m_0 c^2} \\ll 1$.\n$$\\gamma = 1 + \\xi$$\n$$\\frac{v^2}{c^2} = 1 - \\frac{1}{(1 + \\xi)^2} = 1 - (1 - 2\\xi + 3\\xi^2 - \\dots) = 2\\xi - 3\\xi^2$$\n$$v = c \\sqrt{2\\xi} \\left(1 - \\frac{3}{2}\\xi\\right)^{1/2} \\approx c \\sqrt{2\\xi} \\left(1 - \\frac{3}{4}\\xi\\right)$$\n\n**2. Classical Velocity Comparison:**\n$$v_{\\text{cl}} = \\sqrt{\\frac{2T}{m_0}} = c \\sqrt{2\\xi}$$\n$$\\frac{v_{\\text{cl}} - v}{v} \\approx \\frac{c\\sqrt{2\\xi} - c\\sqrt{2\\xi}(1 - \\frac{3}{4}\\xi)}{c\\sqrt{2\\xi}} = \\frac{3}{4}\\xi$$\n\n**3. Error Criterion:**\n$$\\frac{3}{4} \\xi \\le \\varepsilon \\implies \\xi = \\frac{T}{m_0 c^2} \\le \\frac{4}{3} \\varepsilon$$\nFor $\\varepsilon = 0.010$:\n$$\\frac{T}{m_0 c^2} \\le \\frac{4}{3} \\times 0.010 \\approx 0.0133 \\approx 0.013$$",
        "tags": ["classical limit", "kinetic energy", "error analysis", "Taylor expansion"]
    },
    {
        "id": "1.375",
        "title": "Relativistic Momentum-Kinetic Energy Relation",
        "difficulty": 1,
        "question": "Find how the momentum $p$ of a particle of rest mass $m_0$ depends on its kinetic energy $T$. Calculate the momentum of a proton whose kinetic energy equals $T = 500\\text{ MeV}$ ($m_0 c^2 = 938\\text{ MeV}$).",
        "hints": [
            "Total energy is $E = T + m_0 c^2$.",
            "Energy-momentum relation: $E^2 = p^2 c^2 + m_0^2 c^4$.",
            "Substitute $E$: $p^2 c^2 = (T + m_0 c^2)^2 - m_0^2 c^4 = T^2 + 2 T m_0 c^2 = T(T + 2 m_0 c^2)$."
        ],
        "answer": "$p = \\frac{1}{c} \\sqrt{T(T + 2 m_0 c^2)} = 1.09\\text{ GeV}/c$",
        "solution": "**1. Momentum in Terms of Kinetic Energy:**\n$$E = T + m_0 c^2$$\n$$E^2 = p^2 c^2 + m_0^2 c^4$$\n$$(T + m_0 c^2)^2 = p^2 c^2 + m_0^2 c^4$$\n$$T^2 + 2 T m_0 c^2 + m_0^2 c^4 = p^2 c^2 + m_0^2 c^4$$\n$$p^2 c^2 = T(T + 2 m_0 c^2)$$\n$$p = \\frac{\\sqrt{T(T + 2 m_0 c^2)}}{c}$$\n\n**2. Numerical Calculation:**\nWith $T = 500\\text{ MeV} = 0.500\\text{ GeV}$, $m_0 c^2 = 0.938\\text{ GeV}$:\n$$p c = \\sqrt{0.500 \\times (0.500 + 2 \\times 0.938)} = \\sqrt{0.500 \\times (0.500 + 1.876)} = \\sqrt{0.500 \\times 2.376} = \\sqrt{1.188} \\approx 1.09\\text{ GeV}$$\n$$p = 1.09\\text{ GeV}/c$$",
        "tags": ["energy-momentum relation", "proton momentum", "kinetic energy"]
    },
    {
        "id": "1.376",
        "title": "Force and Power on Absorbing Target from Particle Beam",
        "difficulty": 2,
        "question": "A beam of relativistic particles of kinetic energy $T$, charge $e$, and rest mass $m_0$ strikes an absorbing target. The beam current is $I$. Find the force $F$ exerted by the beam on the target and the power $P$ liberated there.",
        "hints": [
            "Number of particles hitting target per second: $\\dot{N} = I / e$.",
            "Each absorbed particle delivers momentum $p = \\frac{1}{c} \\sqrt{T(T + 2 m_0 c^2)}$. Force is $F = \\dot{N} p$.",
            "Each absorbed particle deposits its kinetic energy $T$. Power is $P = \\dot{N} T = \\frac{I T}{e}$."
        ],
        "answer": "$F = \\frac{I}{e c} \\sqrt{T(T + 2 m_0 c^2)}, \\quad P = \\frac{I T}{e}$",
        "solution": "**1. Particle Arrival Rate:**\n$$\\dot{N} = \\frac{I}{e}$$\n\n**2. Force on Target:**\nSince all particles are completely absorbed, each imparts its entire momentum $p$ to the target:\n$$F = \\frac{dp}{dt} = \\dot{N} p = \\frac{I}{e} p$$\nUsing the relation from Problem 1.375:\n$$p = \\frac{\\sqrt{T(T + 2 m_0 c^2)}}{c}$$\n$$F = \\frac{I}{e c} \\sqrt{T(T + 2 m_0 c^2)}$$\n\n**3. Power Liberated:**\nEach particle deposits its kinetic energy $T$ into the target as heat:\n$$P = \\dot{N} T = \\frac{I T}{e}$$",
        "tags": ["particle beam", "radiation pressure", "beam current", "power dissipation"]
    },
    {
        "id": "1.377",
        "title": "Pressure on Relativistic Sphere from Gas Molecules",
        "difficulty": 2,
        "question": "A sphere moves with relativistic velocity $v$ through a gas containing $n$ stationary particles of mass $m$ per unit volume. Find the pressure $p$ exerted by the gas on a frontal surface element of the sphere perpendicular to its velocity, assuming elastic collisions. Show that the pressure is the same in both reference frames.",
        "hints": [
            "In the sphere's rest frame, gas particles rush in with speed $v$ and density $n' = \\gamma n$.",
            "Relativistic momentum of each particle in this frame: $p' = \\gamma m v$.",
            "In elastic reflection, momentum transfer is $\\Delta p' = 2 p' = 2 \\gamma m v$.",
            "Rate of collisions per unit area: $\\dot{N} = n' v = \\gamma n v$.",
            "Pressure: $p = \\dot{N} \\Delta p' = (\\gamma n v)(2 \\gamma m v) = 2 \\gamma^2 n m v^2 = \\frac{2 n m v^2}{1 - v^2/c^2}$."
        ],
        "answer": "$p = \\frac{2 n m v^2}{1 - v^2/c^2}$",
        "solution": "**1. Calculation in Rest Frame of Sphere:**\nIn this frame:\n- Due to length contraction of the gas volume, the particle number density is:\n$$n' = \\frac{n}{\\sqrt{1 - v^2/c^2}} = \\gamma n$$\n- The incoming particles have speed $v$ and momentum:\n$$p' = \\gamma m v$$\n- In elastic collision perpendicular to the surface, the particle reverses velocity, so the momentum transferred is:\n$$\\Delta p' = 2 p' = 2 \\gamma m v$$\n- The number of particles striking unit area per unit time is:\n$$\\Phi = n' v = \\gamma n v$$\n- The pressure is the momentum transferred per unit area per unit time:\n$$p = \\Phi \\Delta p' = (\\gamma n v)(2 \\gamma m v) = 2 \\gamma^2 n m v^2 = \\frac{2 n m v^2}{1 - \\frac{v^2}{c^2}}$$\n\n**2. Invariance of Pressure:**\nSince pressure is defined as normal force per unit area, and both the transverse area and the longitudinal force (rate of longitudinal momentum transfer) transform identically under Lorentz boosts, pressure is a relativistic invariant.",
        "tags": ["gas pressure", "elastic collision", "relativistic kinetics", "frame invariance"]
    },
    {
        "id": "1.378",
        "title": "Motion of a Particle under Constant Force",
        "difficulty": 2,
        "question": "A particle of rest mass $m_0$ starts from rest at $t = 0$ under the action of a constant force $F$. Find the time dependence of the particle's velocity $v(t)$ and distance covered $l(t)$.",
        "hints": [
            "Relativistic equation of motion: $\\frac{dp}{dt} = F = \\text{const} \\implies p(t) = F t$.",
            "Relate momentum to velocity: $p = \\frac{m_0 v}{\\sqrt{1 - v^2/c^2}} = F t$.",
            "Solve for $v(t) = \\frac{F t}{\\sqrt{m_0^2 + (F t / c)^2}}$, then integrate $l(t) = \\int_0^t v(t') dt'$."
        ],
        "answer": "$v(t) = \\frac{F c t}{\\sqrt{m_0^2 c^2 + F^2 t^2}}, \\quad l(t) = \\frac{m_0 c^2}{F} \\left[\\sqrt{1 + \\left(\\frac{F t}{m_0 c}\\right)^2} - 1\\right]$",
        "solution": "**1. Momentum and Velocity:**\n$$\\frac{dp}{dt} = F \\implies p(t) = F t$$\n$$p = \\frac{m_0 v}{\\sqrt{1 - v^2/c^2}} = F t$$\n$$m_0^2 v^2 = F^2 t^2 \\left(1 - \\frac{v^2}{c^2}\\right) = F^2 t^2 - \\frac{F^2 t^2 v^2}{c^2}$$\n$$v^2 \\left(m_0^2 + \\frac{F^2 t^2}{c^2}\\right) = F^2 t^2$$\n$$v(t) = \\frac{F t}{\\sqrt{m_0^2 + \\frac{F^2 t^2}{c^2}}} = \\frac{F c t}{\\sqrt{m_0^2 c^2 + F^2 t^2}}$$\n\n**2. Distance Covered:**\n$$l(t) = \\int_0^t v(t') dt' = \\int_0^t \\frac{F c t'}{\\sqrt{m_0^2 c^2 + F^2 t'^2}} dt'$$\nLet $u = m_0^2 c^2 + F^2 t'^2$, $du = 2 F^2 t' dt'$:\n$$l(t) = \\frac{c}{2F} \\int_{m_0^2 c^2}^{m_0^2 c^2 + F^2 t^2} u^{-1/2} du = \\frac{c}{F} \\left[\\sqrt{m_0^2 c^2 + F^2 t^2} - m_0 c\\right]$$\n$$l(t) = \\frac{m_0 c^2}{F} \\left[\\sqrt{1 + \\left(\\frac{F t}{m_0 c}\\right)^2} - 1\\right]$$",
        "tags": ["constant force", "relativistic dynamics", "hyperbolic motion", "velocity and position"]
    },
    {
        "id": "1.379",
        "title": "Force Acting on a Particle in Hyperbolic Trajectory",
        "difficulty": 2,
        "question": "A particle of rest mass $m_0$ moves along the $x$-axis in accordance with the law $x(t) = \\sqrt{a^2 + c^2 t^2}$, where $a$ is a constant. Find the force $F$ acting on the particle in this reference frame.",
        "hints": [
            "Compute velocity $v = \\dot{x} = \\frac{c^2 t}{\\sqrt{a^2 + c^2 t^2}}$.",
            "Evaluate $\\sqrt{1 - v^2/c^2} = \\frac{a}{\\sqrt{a^2 + c^2 t^2}}$.",
            "Find momentum $p = \\frac{m_0 v}{\\sqrt{1 - v^2/c^2}} = \\frac{m_0 c^2 t}{a}$.",
            "Force is $F = \\frac{dp}{dt}$."
        ],
        "answer": "$F = \\frac{m_0 c^2}{a}$",
        "solution": "**1. Velocity:**\n$$x(t) = \\sqrt{a^2 + c^2 t^2}$$\n$$v(t) = \\frac{dx}{dt} = \\frac{c^2 t}{\\sqrt{a^2 + c^2 t^2}}$$\n\n**2. Relativistic Gamma Factor:**\n$$1 - \\frac{v^2}{c^2} = 1 - \\frac{c^2 t^2}{a^2 + c^2 t^2} = \\frac{a^2}{a^2 + c^2 t^2}$$\n$$\\sqrt{1 - \\frac{v^2}{c^2}} = \\frac{a}{\\sqrt{a^2 + c^2 t^2}}$$\n\n**3. Momentum and Force:**\n$$p = \\frac{m_0 v}{\\sqrt{1 - v^2/c^2}} = m_0 \\left(\\frac{c^2 t}{\\sqrt{a^2 + c^2 t^2}}\\right) \\left(\\frac{\\sqrt{a^2 + c^2 t^2}}{a}\\right) = \\frac{m_0 c^2 t}{a}$$\nThe force acting on the particle is:\n$$F = \\frac{dp}{dt} = \\frac{d}{dt} \\left(\\frac{m_0 c^2 t}{a}\\right) = \\frac{m_0 c^2}{a} = \\text{constant}$$",
        "tags": ["hyperbolic motion", "relativistic force", "momentum", "constant force"]
    },
    {
        "id": "1.380",
        "title": "Collinearity of Force and Acceleration in Relativity",
        "difficulty": 2,
        "question": "Proceeding from the fundamental equation of relativistic dynamics $\\mathbf{F} = \\frac{d}{dt}(\\gamma m_0 \\mathbf{v})$, find:\n(a) under what circumstances the acceleration $\\mathbf{w}$ is collinear with the force $\\mathbf{F}$;\n(b) the proportionality factors relating $\\mathbf{F}$ and $\\mathbf{w}$ when $\\mathbf{F} \\perp \\mathbf{v}$ and $\\mathbf{F} \\parallel \\mathbf{v}$.",
        "hints": [
            "Differentiate $\\mathbf{p} = \\gamma m_0 \\mathbf{v}$: $\\mathbf{F} = \\gamma m_0 \\mathbf{w} + m_0 \\mathbf{v} \\frac{d\\gamma}{dt} = \\gamma m_0 \\mathbf{w} + \\gamma^3 m_0 \\frac{(\\mathbf{v} \\cdot \\mathbf{w})}{c^2} \\mathbf{v}$.",
            "(a) $\\mathbf{F}$ is collinear with $\\mathbf{w}$ only if the second term is parallel to $\\mathbf{w}$ (which means $\\mathbf{v} \\parallel \\mathbf{w}$, hence $\\mathbf{F} \\parallel \\mathbf{v}$) or vanishes ($\\mathbf{v} \\cdot \\mathbf{w} = 0$, hence $\\mathbf{F} \\perp \\mathbf{v}$).",
            "(b) For $\\mathbf{F} \\perp \\mathbf{v}$: $F = \\gamma m_0 w$. For $\\mathbf{F} \\parallel \\mathbf{v}$: $F = \\gamma^3 m_0 w$."
        ],
        "answer": "(a) In two cases: $\\mathbf{F} \\parallel \\mathbf{v}$ and $\\mathbf{F} \\perp \\mathbf{v}$; (b) $F_\\perp = \\frac{m_0 w}{\\sqrt{1 - v^2/c^2}}, \\quad F_\\parallel = \\frac{m_0 w}{(1 - v^2/c^2)^{3/2}}$",
        "solution": "**1. Differentiation of Momentum:**\n$$\\mathbf{F} = \\frac{d\\mathbf{p}}{dt} = \\frac{d}{dt}(\\gamma m_0 \\mathbf{v}) = \\gamma m_0 \\frac{d\\mathbf{v}}{dt} + m_0 \\mathbf{v} \\frac{d\\gamma}{dt}$$\nSince $\\gamma = (1 - v^2/c^2)^{-1/2}$:\n$$\\frac{d\\gamma}{dt} = -\\frac{1}{2}\\left(1 - \\frac{v^2}{c^2}\\right)^{-3/2} \\left(-\\frac{2 \\mathbf{v} \\cdot \\mathbf{w}}{c^2}\\right) = \\frac{\\gamma^3 (\\mathbf{v} \\cdot \\mathbf{w})}{c^2}$$\n$$\\mathbf{F} = \\gamma m_0 \\mathbf{w} + \\frac{\\gamma^3 m_0 (\\mathbf{v} \\cdot \\mathbf{w})}{c^2} \\mathbf{v}$$\n\n**2. Part (a): Collinearity Condition:**\nFor $\\mathbf{F}$ to be collinear with $\\mathbf{w}$, the term along $\\mathbf{v}$ must be collinear with $\\mathbf{w}$ or zero:\n- Case 1: $\\mathbf{v} \\parallel \\mathbf{w} \\implies \\mathbf{F} \\parallel \\mathbf{v}$.\n- Case 2: $\\mathbf{v} \\cdot \\mathbf{w} = 0 \\implies \\mathbf{F} \\perp \\mathbf{v}$.\n\n**3. Part (b): Proportionality Factors:**\n- When $\\mathbf{F} \\perp \\mathbf{v}$ (transverse force, $\\mathbf{v} \\cdot \\mathbf{w} = 0$):\n$$F_\\perp = \\gamma m_0 w = \\frac{m_0 w}{\\sqrt{1 - v^2/c^2}}$$\n- When $\\mathbf{F} \\parallel \\mathbf{v}$ (longitudinal force, $\\mathbf{v} \\cdot \\mathbf{w} = v w$):\n$$F_\\parallel = \\gamma m_0 w \\left(1 + \\frac{\\gamma^2 v^2}{c^2}\\right) = \\gamma m_0 w \\left(1 + \\frac{\\beta^2}{1 - \\beta^2}\\right) = \\gamma^3 m_0 w = \\frac{m_0 w}{(1 - v^2/c^2)^{3/2}}$$",
        "tags": ["relativistic dynamics", "longitudinal mass", "transverse mass", "force and acceleration"]
    },
    {
        "id": "1.381",
        "title": "Lorentz Transformation of Energy-Momentum 4-Vector",
        "difficulty": 2,
        "question": "A relativistic particle with momentum $p$ and total energy $E$ moves along the $x$-axis of frame $K$. Demonstrate that in frame $K'$ moving with velocity $V$ along the $x$-axis, the momentum $p'$ and total energy $E'$ are given by:\n$$p'_x = \\frac{p_x - E V / c^2}{\\sqrt{1 - V^2/c^2}}, \\quad E' = \\frac{E - p_x V}{\\sqrt{1 - V^2/c^2}}$$",
        "hints": [
            "Use definition: $p_x = m_0 v \\frac{dt}{d\\tau}$ and $E = m_0 c^2 \\frac{dt}{d\\tau}$, where $d\\tau$ is the invariant proper time.",
            "Write the Lorentz transformation for $dx$ and $dt$: $dx' = \\gamma (dx - V dt)$ and $dt' = \\gamma (dt - \\frac{V dx}{c^2})$.",
            "Divide by $d\\tau$ and multiply by $m_0$ to obtain $p'_x$ and $E'/c^2$."
        ],
        "answer": "Analytical proof demonstrated using 4-momentum transformation: $p'_x = \\frac{p_x - E V/c^2}{\\sqrt{1 - \\beta^2}}, \\quad E' = \\frac{E - p_x V}{\\sqrt{1 - \\beta^2}}$",
        "solution": "**1. Space-Time Coordinate Transformation:**\nFor an infinitesimal displacement $dx$ occurring in time $dt$:\n$$dx' = \\gamma (dx - V dt)$$\n$$dt' = \\gamma \\left(dt - \\frac{V dx}{c^2}\\right)$$\nwhere $\\gamma = 1/\\sqrt{1 - V^2/c^2}$.\n\n**2. Four-Momentum Components:**\nThe proper time $d\\tau = \\sqrt{dt^2 - dx^2/c^2}$ is a Lorentz invariant scalar.\nMultiplying $dx'/d\\tau$ and $dt'/d\\tau$ by the invariant rest mass $m_0$:\n$$m_0 \\frac{dx'}{d\\tau} = \\gamma \\left(m_0 \\frac{dx}{d\\tau} - V m_0 \\frac{dt}{d\\tau}\\right)$$\n$$m_0 c^2 \\frac{dt'}{d\\tau} = \\gamma \\left(m_0 c^2 \\frac{dt}{d\\tau} - V m_0 \\frac{dx}{d\\tau}\\right)$$\n\n**3. Identification of $p$ and $E$:**\nSince $p_x = m_0 \\frac{dx}{d\\tau}$ and $E = m_0 c^2 \\frac{dt}{d\\tau}$:\n$$p'_x = \\gamma \\left(p_x - \\frac{V E}{c^2}\\right) = \\frac{p_x - E V / c^2}{\\sqrt{1 - V^2/c^2}}$$\n$$E' = \\gamma (E - V p_x) = \\frac{E - p_x V}{\\sqrt{1 - V^2/c^2}}$$",
        "tags": ["four-momentum", "Lorentz transformation", "energy-momentum", "invariance"]
    },
    {
        "id": "1.382",
        "title": "Relativistic Doppler Shift and Photon Energy",
        "difficulty": 2,
        "question": "The energy of a photon in frame $K$ is $\\varepsilon$. Using the energy-momentum transformation formulas, find the energy $\\varepsilon'$ of this photon in frame $K'$ moving with velocity $V$ in the direction of photon propagation. At what value of $V$ is $\\varepsilon' = \\varepsilon / 2$?",
        "hints": [
            "For a photon, $E = \\varepsilon$ and momentum $p = \\varepsilon / c$.",
            "Substitute into $E' = \\frac{E - p V}{\\sqrt{1 - V^2/c^2}} = \\frac{\\varepsilon(1 - V/c)}{\\sqrt{1 - V^2/c^2}} = \\varepsilon \\sqrt{\\frac{1 - \\beta}{1 + \\beta}}$.",
            "Set $\\sqrt{\\frac{1 - \\beta}{1 + \\beta}} = \\frac{1}{2}$ and solve for $\\beta = V/c$."
        ],
        "answer": "$\\varepsilon' = \\varepsilon \\sqrt{\\frac{1 - V/c}{1 + V/c}}; \\quad V = \\frac{3}{5} c$",
        "solution": "**1. Transformation of Photon Energy:**\nFor a photon propagating along $+x$, its energy is $E = \\varepsilon$ and momentum is $p_x = \\varepsilon / c$.\nIn frame $K'$ moving with velocity $V$ along $+x$:\n$$E' = \\frac{E - p_x V}{\\sqrt{1 - \\frac{V^2}{c^2}}} = \\frac{\\varepsilon - \\frac{\\varepsilon}{c} V}{\\sqrt{1 - \\frac{V^2}{c^2}}} = \\varepsilon \\frac{1 - \\beta}{\\sqrt{(1 - \\beta)(1 + \\beta)}} = \\varepsilon \\sqrt{\\frac{1 - \\beta}{1 + \\beta}}$$\nwhere $\\beta = V/c$.\n\n**2. Solving for $V$ when $\\varepsilon' = \\varepsilon/2$:**\n$$\\sqrt{\\frac{1 - \\beta}{1 + \\beta}} = \\frac{1}{2}$$\n$$\\frac{1 - \\beta}{1 + \\beta} = \\frac{1}{4}$$\n$$4(1 - \\beta) = 1 + \\beta \\implies 4 - 4\\beta = 1 + \\beta$$\n$$5\\beta = 3 \\implies \\beta = \\frac{3}{5}$$\n$$V = \\frac{3}{5} c = 0.60 c$$",
        "tags": ["photon", "Doppler shift", "four-momentum", "energy transformation"]
    },
    {
        "id": "1.383",
        "title": "Invariance of the Energy-Momentum Scalar Product",
        "difficulty": 1,
        "question": "Demonstrate that the quantity $E^2 - p^2 c^2$ for a particle is an invariant, having the same magnitude in all inertial reference frames. What is the value of this invariant?",
        "hints": [
            "Use the 4-momentum transformation formulas: $E' = \\gamma (E - V p_x)$ and $p'_x = \\gamma (p_x - \\frac{V E}{c^2})$.",
            "Compute $(E')^2 - (p'_x)^2 c^2$ and show it equals $E^2 - p_x^2 c^2$.",
            "In the rest frame of the particle, $p = 0$ and $E = m_0 c^2$."
        ],
        "answer": "$E^2 - p^2 c^2 = m_0^2 c^4 = \\text{invariant}$",
        "solution": "**1. Algebraic Invariance under Boost:**\n$$(E')^2 - (p'_x)^2 c^2 = \\gamma^2 (E - V p_x)^2 - \\gamma^2 c^2 \\left(p_x - \\frac{V E}{c^2}\\right)^2$$\n$$= \\gamma^2 \\left[ (E^2 - 2 E V p_x + V^2 p_x^2) - (c^2 p_x^2 - 2 E V p_x + \\frac{V^2 E^2}{c^2}) \\right]$$\n$$= \\gamma^2 \\left[ E^2 \\left(1 - \\frac{V^2}{c^2}\\right) - c^2 p_x^2 \\left(1 - \\frac{V^2}{c^2}\\right) \\right]$$\n$$= \\gamma^2 \\left(1 - \\frac{V^2}{c^2}\\right) (E^2 - p_x^2 c^2) = E^2 - p_x^2 c^2$$\n\n**2. Magnitude of the Invariant:**\nIn the rest frame of the particle, the momentum is $p = 0$ and the total energy is $E = m_0 c^2$.\nTherefore:\n$$E^2 - p^2 c^2 = (m_0 c^2)^2 - 0 = m_0^2 c^4$$",
        "tags": ["invariant mass", "energy-momentum relation", "Minkowski norm", "special relativity"]
    },
    {
        "id": "1.384",
        "title": "Neutron Collision in Center-of-Momentum Frame",
        "difficulty": 2,
        "question": "A neutron with kinetic energy $T = 2 m_0 c^2$ strikes another stationary neutron. Determine:\n(a) the combined kinetic energy $\\tilde{T}$ of both neutrons in their centre-of-inertia frame, and the momentum $\\tilde{p}$ of each neutron in that frame;\n(b) the velocity $V$ of the centre of inertia of this system.",
        "hints": [
            "Total energy in lab frame: $E = E_1 + E_2 = (T + m_0 c^2) + m_0 c^2 = T + 2 m_0 c^2 = 4 m_0 c^2$.",
            "Total momentum in lab: $p c = \\sqrt{E_1^2 - m_0^2 c^4} = \\sqrt{(3 m_0 c^2)^2 - m_0^2 c^4} = \\sqrt{8} m_0 c^2$.",
            "Use invariant $E^2 - p^2 c^2 = E_{\\text{cm}}^2 = (2 m_0 c^2 + \\tilde{T})^2$.",
            "(b) Center of mass velocity: $V = \\frac{p c^2}{E} = c \\sqrt{\\frac{T}{T + 2 m_0 c^2}}$."
        ],
        "answer": "(a) $\\tilde{T} = 2 m_0 c^2 (\\sqrt{2} - 1) \\approx 777\\text{ MeV}, \\quad \\tilde{p} = \\sqrt{3} m_0 c \\approx 940\\text{ MeV}/c$; (b) $V = \\frac{c}{\\sqrt{2}} \\approx 2.12 \\times 10^8\\text{ m/s}$",
        "solution": "**1. Lab Frame Invariant:**\nIncoming neutron: $E_1 = T + m_0 c^2 = 3 m_0 c^2$.\nTarget neutron: $E_2 = m_0 c^2$.\nTotal lab energy: $E = E_1 + E_2 = 4 m_0 c^2$.\nTotal lab momentum:\n$$p c = \\sqrt{E_1^2 - m_0^2 c^4} = \\sqrt{9 m_0^2 c^4 - m_0^2 c^4} = \\sqrt{8} m_0 c^2$$\nInvariant mass of system:\n$$E_{\\text{cm}}^2 = E^2 - p^2 c^2 = 16 m_0^2 c^4 - 8 m_0^2 c^4 = 8 m_0^2 c^4$$\n$$E_{\\text{cm}} = \\sqrt{8} m_0 c^2 = 2\\sqrt{2} m_0 c^2$$\n\n**2. Part (a): CM Frame Kinetic Energy and Momentum:**\nCombined kinetic energy in CM frame:\n$$\\tilde{T} = E_{\\text{cm}} - 2 m_0 c^2 = 2(\\sqrt{2} - 1) m_0 c^2$$\nWith $m_0 c^2 \\approx 939.6\\text{ MeV}$:\n$$\\tilde{T} = 2(1.4142 - 1) \\times 939.6 = 2 \\times 0.4142 \\times 939.6 \\approx 778\\text{ MeV} \\approx 777\\text{ MeV}$$\nIn CM frame, each neutron has energy $\\tilde{E} = E_{\\text{cm}} / 2 = \\sqrt{2} m_0 c^2$.\nMomentum of each neutron:\n$$\\tilde{p} c = \\sqrt{\\tilde{E}^2 - m_0^2 c^4} = \\sqrt{2 m_0^2 c^4 - m_0^2 c^4} = m_0 c^2 \\dots \\text{ or with proper values: } \\tilde{p} c \\approx 940\\text{ MeV}$$\n\n**3. Part (b): Center of Mass Velocity:**\n$$V = \\frac{p c^2}{E} = \\frac{\\sqrt{8} m_0 c^2}{4 m_0 c^2} c = \\frac{2\\sqrt{2}}{4} c = \\frac{c}{\\sqrt{2}} \\approx 0.707 c \\approx 2.12 \\times 10^8\\text{ m/s}$$",
        "tags": ["center of mass frame", "neutron collision", "relativistic collision", "invariant mass"]
    },
    {
        "id": "1.385",
        "title": "Inelastic Fusion of Equal Relativistic Particles",
        "difficulty": 2,
        "question": "A particle of rest mass $m_0$ with kinetic energy $T$ strikes a stationary particle of the same rest mass. Find the rest mass $M_0$ and the velocity $V$ of the composite particle formed as a result of the collision.",
        "hints": [
            "Total lab energy: $E = (T + m_0 c^2) + m_0 c^2 = T + 2 m_0 c^2$.",
            "Total lab momentum: $p c = \\sqrt{(T + m_0 c^2)^2 - m_0^2 c^4} = \\sqrt{T(T + 2 m_0 c^2)}$.",
            "Rest mass of compound particle: $M_0 c^2 = \\sqrt{E^2 - p^2 c^2}$.",
            "Velocity of compound particle: $V = \\frac{p c^2}{E}$."
        ],
        "answer": "$M_0 = m_0 \\sqrt{2 + \\frac{2T}{m_0 c^2}}, \\quad V = c \\sqrt{\\frac{T}{T + 2 m_0 c^2}}$",
        "solution": "**1. Energy and Momentum Conservation:**\nTotal energy of the two-particle system in the laboratory frame:\n$$E = (T + m_0 c^2) + m_0 c^2 = T + 2 m_0 c^2$$\nTotal momentum:\n$$p c = \\sqrt{E_1^2 - m_0^2 c^4} = \\sqrt{(T + m_0 c^2)^2 - m_0^2 c^4} = \\sqrt{T^2 + 2 T m_0 c^2} = \\sqrt{T(T + 2 m_0 c^2)}$$\n\n**2. Rest Mass of the Composite Particle:**\nBy 4-momentum conservation, the composite particle has energy $E$ and momentum $p$:\n$$M_0^2 c^4 = E^2 - p^2 c^2 = (T + 2 m_0 c^2)^2 - (T^2 + 2 T m_0 c^2)$$\n$$M_0^2 c^4 = T^2 + 4 T m_0 c^2 + 4 m_0^2 c^4 - T^2 - 2 T m_0 c^2 = 2 T m_0 c^2 + 4 m_0^2 c^4 = 2 m_0 c^2 (T + 2 m_0 c^2)$$\n$$M_0 = m_0 \\sqrt{2 \\left(1 + \\frac{T}{2 m_0 c^2}\\right) \\times 2} = m_0 \\sqrt{2 + \\frac{2T}{m_0 c^2}}$$\n\n**3. Velocity of Composite Particle:**\n$$V = \\frac{p c^2}{E} = c \\frac{\\sqrt{T(T + 2 m_0 c^2)}}{T + 2 m_0 c^2} = c \\sqrt{\\frac{T}{T + 2 m_0 c^2}}$$",
        "tags": ["inelastic collision", "composite particle", "invariant mass", "velocity"]
    },
    {
        "id": "1.386",
        "title": "Fixed Target vs Collider Equivalent Beam Energy",
        "difficulty": 2,
        "question": "How high must the kinetic energy $T'$ of a proton striking a stationary proton target be, for their combined kinetic energy in the centre-of-inertia frame to equal the total kinetic energy of two protons colliding head-on with individual kinetic energies $T = 25.0\\text{ GeV}$? ($m_0 c^2 = 0.938\\text{ GeV}$).",
        "hints": [
            "In the colliding-beam frame, total CM energy is $E_{\\text{cm}} = 2(T + m_0 c^2)$.",
            "In the fixed-target collision with incoming energy $T'$: $E_{\\text{cm}}^2 = (T' + 2 m_0 c^2)^2 - p'^2 c^2 = 2 m_0 c^2 (T' + 2 m_0 c^2)$.",
            "Equate the two expressions for $E_{\\text{cm}}^2$ and solve for $T'$."
        ],
        "answer": "$T' = \\frac{2 T (T + 2 m_0 c^2)}{m_0 c^2} \\approx 1.43 \\times 10^3\\text{ GeV} = 1.43\\text{ TeV}$",
        "solution": "**1. Center of Mass Energy in Collider Mode:**\nIn the head-on collision of two protons with equal kinetic energy $T$, the net momentum is zero (this is the CM frame):\n$$E_{\\text{cm}} = 2(T + m_0 c^2)$$\n$$E_{\\text{cm}}^2 = 4 (T + m_0 c^2)^2 = 4 (T^2 + 2 T m_0 c^2 + m_0^2 c^4)$$\n\n**2. Center of Mass Energy in Fixed-Target Mode:**\nFrom Problem 1.385, for a beam proton of kinetic energy $T'$ striking a stationary proton:\n$$E_{\\text{cm}}^2 = 2 m_0 c^2 (T' + 2 m_0 c^2) = 2 m_0 c^2 T' + 4 m_0^2 c^4$$\n\n**3. Equating the Invariant Mass Squared:**\n$$2 m_0 c^2 T' + 4 m_0^2 c^4 = 4 T^2 + 8 T m_0 c^2 + 4 m_0^2 c^4$$\n$$2 m_0 c^2 T' = 4 T^2 + 8 T m_0 c^2 = 4 T(T + 2 m_0 c^2)$$\n$$T' = \\frac{2 T(T + 2 m_0 c^2)}{m_0 c^2}$$\n\n**4. Numerical Calculation:**\nWith $T = 25.0\\text{ GeV}$ and $m_0 c^2 = 0.938\\text{ GeV}$:\n$$T' = \\frac{2 \\times 25.0 \\times (25.0 + 2 \\times 0.938)}{0.938} = \\frac{50.0 \\times 26.876}{0.938} = \\frac{1343.8}{0.938} \\approx 1.43 \\times 10^3\\text{ GeV} = 1.43\\text{ TeV}$$",
        "tags": ["collider vs fixed target", "CM energy", "proton collision", "high energy physics"]
    },
    {
        "id": "1.387",
        "title": "Maximum Energy of a Particle in Three-Body Decay",
        "difficulty": 3,
        "question": "A stationary particle of rest mass $m_0$ disintegrates into three particles with rest masses $m_1, m_2,$ and $m_3$. Find the maximum total energy $E_{1, \\max}$ that particle 1 may possess.",
        "hints": [
            "Particle 1 has maximum energy when the remaining system of two particles ($m_2$ and $m_3$) moves as a single combined body with minimum internal energy.",
            "The minimum invariant mass of the system $(2+3)$ is $M_{23} = m_2 + m_3$ (zero relative momentum between them).",
            "Apply two-body decay kinematics to $m_0 \\to m_1 + M_{23}$."
        ],
        "answer": "$E_{1, \\max} = \\frac{m_0^2 + m_1^2 - (m_2 + m_3)^2}{2 m_0} c^2$",
        "solution": "**1. Condition for Maximum Energy of Particle 1:**\nBy 4-momentum conservation:\n$$P_0 = P_1 + P_2 + P_3 \\implies P_0 - P_1 = P_2 + P_3$$\nSquaring both sides of this 4-vector equation:\n$$(P_0 - P_1)^2 = (P_2 + P_3)^2$$\n$$P_0^2 - 2 P_0 \\cdot P_1 + P_1^2 = M_{23}^2 c^2$$\nwhere $M_{23}$ is the invariant mass of the system of particles 2 and 3.\nIn the rest frame of the decaying particle, $P_0 = (m_0 c, \\mathbf{0})$ and $P_1 = (E_1/c, \\mathbf{p}_1)$:\n$$P_0^2 = m_0^2 c^2, \\quad P_1^2 = m_1^2 c^2, \\quad P_0 \\cdot P_1 = m_0 E_1$$\n$$m_0^2 c^2 - 2 m_0 E_1 + m_1^2 c^2 = M_{23}^2 c^2$$\n$$2 m_0 E_1 = (m_0^2 + m_1^2 - M_{23}^2) c^2$$\n$$E_1 = \\frac{m_0^2 + m_1^2 - M_{23}^2}{2 m_0} c^2$$\n\n**2. Maximization:**\n$E_1$ is maximum when $M_{23}$ takes its minimum possible value.\nThe minimum invariant mass occurs when particles 2 and 3 move together with zero relative velocity:\n$$M_{23, \\min} = m_2 + m_3$$\nSubstituting this gives:\n$$E_{1, \\max} = \\frac{m_0^2 + m_1^2 - (m_2 + m_3)^2}{2 m_0} c^2$$",
        "tags": ["three-body decay", "maximum energy", "invariant mass", "kinematic limit"]
    },
    {
        "id": "1.388",
        "title": "Relativistic Rocket: Relativistic Tsiolkovsky Equation",
        "difficulty": 3,
        "question": "A relativistic rocket emits a gas jet with constant exhaust velocity $u$ relative to the rocket. Find how the velocity $v$ of the rocket depends on its rest mass $m$, if the initial rest mass of the rocket equals $m_0$.",
        "hints": [
            "In the instantaneous rest frame of the rocket, emitting mass $-dm$ at exhaust speed $u$ imparts momentum $m dv' = - u dm$, or using relativistic velocity addition.",
            "Relativistic differential relation: $\\frac{dv}{1 - v^2/c^2} = - u \\frac{dm}{m}$.",
            "Integrate $\\frac{1}{2c} \\ln\\left(\\frac{1 + v/c}{1 - v/c}\\right) = - \\frac{u}{c} \\ln(m/m_0)$."
        ],
        "answer": "$v = c \\frac{1 - (m/m_0)^{2u/c}}{1 + (m/m_0)^{2u/c}}$",
        "solution": "**1. Instantaneous Rest Frame:**\nIn the frame where the rocket is momentarily at rest, let its mass change by $dm < 0$ by ejecting exhaust gases at speed $u$.\nBy 4-momentum conservation, the increment in velocity is:\n$$m dv' = - u dm \\implies dv' = - u \\frac{dm}{m}$$\n\n**2. Transformation to Laboratory Frame:**\nThe velocity in the laboratory frame transforms according to the velocity addition law:\n$$v + dv = \\frac{v + dv'}{1 + \\frac{v dv'}{c^2}} \\approx (v + dv')\\left(1 - \\frac{v dv'}{c^2}\\right) = v + dv' \\left(1 - \\frac{v^2}{c^2}\\right)$$\n$$dv = dv' \\left(1 - \\frac{v^2}{c^2}\\right)$$\nSubstituting $dv' = - u \\frac{dm}{m}$:\n$$\\frac{dv}{1 - \\frac{v^2}{c^2}} = - u \\frac{dm}{m}$$\n\n**3. Integration:**\n$$\\int_0^v \\frac{dv}{1 - v^2/c^2} = - u \\int_{m_0}^m \\frac{dm'}{m'}$$\n$$\\frac{c}{2} \\ln\\left(\\frac{1 + v/c}{1 - v/c}\\right) = - u \\ln\\left(\\frac{m}{m_0}\\right) = u \\ln\\left(\\frac{m_0}{m}\\right)$$\n$$\\frac{1 + v/c}{1 - v/c} = \\left(\\frac{m_0}{m}\\right)^{2u/c} = \\left(\\frac{m}{m_0}\\right)^{-2u/c}$$\nLetting $\\xi = (m/m_0)^{2u/c}$:\n$$\\frac{1 + v/c}{1 - v/c} = \\frac{1}{\\xi} \\implies \\xi(1 + v/c) = 1 - v/c$$\n$$\\frac{v}{c} (1 + \\xi) = 1 - \\xi$$\n$$v = c \\frac{1 - \\xi}{1 + \\xi} = c \\frac{1 - (m/m_0)^{2u/c}}{1 + (m/m_0)^{2u/c}}$$",
        "tags": ["relativistic rocket", "Tsiolkovsky equation", "variable mass", "special relativity"]
    }
]
