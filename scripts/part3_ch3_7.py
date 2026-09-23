"""
part3_ch3_7.py
Curated problems 3.372 to 3.398 (27 problems) of Irodov Chapter 3.7:
Motion of Charged Particles in Electric and Magnetic Fields.
"""

CH3_7_CURATED = [
    {
        "id": "3.372",
        "title": "Electron Velocity in Linearly Ramp-Voltage Capacitor",
        "difficulty": 2,
        "question": "At the moment $t = 0$ an electron leaves one plate of a parallel-plate capacitor with negligible velocity. An accelerating voltage varying with time as $V(t) = a t$, where $a = 100\\text{ V/s}$, is applied between the plates. The separation between the plates is $l = 5.0\\text{ cm}$. What is the velocity of the electron at the moment it reaches the opposite plate?",
        "hints": [
            "The electric field between the plates is $E(t) = \\frac{V(t)}{l} = \\frac{a t}{l}$.",
            "Integrate the equation of motion $m \\ddot{x} = e E(t) = \\frac{e a t}{l}$ twice with initial conditions $x(0) = 0$ and $v(0) = 0$.",
            "Set $x(t_1) = l$ to find the transit time $t_1 = \\left(\\frac{6 m l^2}{e a}\\right)^{1/3}$, and substitute into $v(t_1) = \\frac{e a t_1^2}{2 m l} = \\left( \\frac{9 a l e}{2m} \\right)^{1/3}$."
        ],
        "answer": "$v = \\left( \\frac{9 a l e}{2m} \\right)^{1/3} \\approx 16\\text{ km/s}$",
        "solution": "**1. Electric Field and Equation of Motion:**\nThe electric field between the capacitor plates of separation $l$ is:\n$$E(t) = \\frac{V(t)}{l} = \\frac{a t}{l}$$\nThe equation of motion for an electron of mass $m$ and charge $-e$ moving toward the positive plate is:\n$$m \\frac{dv}{dt} = e E(t) = \\frac{e a t}{l}$$\n\n**2. Velocity and Displacement:**\nIntegrating from rest ($v(0) = 0$):\n$$v(t) = \\frac{e a}{2 m l} t^2$$\nIntegrating again for displacement ($x(0) = 0$):\n$$x(t) = \\frac{e a}{6 m l} t^3$$\n\n**3. Transit Time and Final Velocity:**\nWhen the electron reaches the opposite plate at $x = l$ at time $t_1$:\n$$l = \\frac{e a}{6 m l} t_1^3 \\implies t_1 = \\left( \\frac{6 m l^2}{e a} \\right)^{1/3}$$\nSubstituting $t_1$ into the velocity expression:\n$$v = \\frac{e a}{2 m l} \\left( \\frac{6 m l^2}{e a} \\right)^{2/3} = \\frac{1}{2} (6)^{2/3} \\left( \\frac{a l e}{m} \\right)^{1/3} = \\left( \\frac{9 a l e}{2m} \\right)^{1/3}$$\n\n**4. Numerical Evaluation:**\nGiven $a = 100\\text{ V/s}$, $l = 0.050\\text{ m}$, $e/m = 1.7588 \\times 10^{11}\\text{ C/kg}$:\n$$\\frac{9 a l e}{2m} = 4.5 \\times 100 \\times 0.050 \\times (1.7588 \\times 10^{11}) \\approx 3.957 \\times 10^{12}\\text{ m}^3\\text{/s}^3$$\n$$v = (3.957 \\times 10^{12})^{1/3} \\approx 1.58 \\times 10^4\\text{ m/s} \\approx 16\\text{ km/s}$$",
        "tags": ["time-varying electric field", "electron acceleration", "capacitor", "kinematics"]
    },
    {
        "id": "3.373",
        "title": "Deflection of Proton in Time-Varying Transverse Electric Field",
        "difficulty": 2,
        "question": "A proton accelerated by a potential difference $V$ enters the uniform electric field of a parallel-plate capacitor whose plates extend over a length $l$ in the motion direction. The field strength varies with time as $E(t) = a t$, where $a$ is a constant. Assuming the proton to be non-relativistic, find the angle between the motion directions of the proton before and after its flight through the capacitor; the proton enters the field at $t = 0$.",
        "hints": [
            "The initial horizontal velocity of the proton is $v_0 = \\sqrt{\\frac{2 e V}{m}}$.",
            "The transit time through plates of length $l$ is $\\tau = \\frac{l}{v_0}$.",
            "The vertical velocity acquired during transit is $v_y = \\int_0^\\tau \\frac{e a t}{m} \\, dt = \\frac{e a \\tau^2}{2m}$. Calculate $\\tan\\alpha = \\frac{v_y}{v_0} = \\frac{a l^2}{4} \\sqrt{\\frac{m}{2 e V^3}}$."
        ],
        "answer": "$\\tan\\alpha = \\frac{a l^2}{4} \\sqrt{\\frac{m}{2 e V^3}}$",
        "solution": "**1. Initial Velocity and Transit Time:**\nAccelerated from rest through potential difference $V$, the initial longitudinal velocity along the $x$-axis is:\n$$\\frac{1}{2} m v_0^2 = e V \\implies v_0 = \\sqrt{\\frac{2 e V}{m}}$$\nNeglecting fringe effects, the transit time through the capacitor of plate length $l$ is:\n$$\\tau = \\frac{l}{v_0}$$\n\n**2. Transverse Velocity Acquired:**\nThe transverse force is $F_y(t) = e E(t) = e a t$.\nIntegrating the transverse acceleration from $t = 0$ to $t = \\tau$:\n$$v_y = \\int_0^\\tau \\frac{e a t}{m} \\, dt = \\frac{e a \\tau^2}{2m} = \\frac{e a l^2}{2 m v_0^2}$$\nSubstituting $v_0^2 = \\frac{2 e V}{m}$:\n$$v_y = \\frac{e a l^2}{2 m \\left( \\frac{2 e V}{m} \\right)} = \\frac{a l^2}{4V}$$\n\n**3. Deflection Angle:**\nThe angle of deflection $\\alpha$ is given by:\n$$\\tan\\alpha = \\frac{v_y}{v_0} = \\frac{a l^2 / 4V}{\\sqrt{2 e V / m}} = \\frac{a l^2}{4} \\sqrt{\\frac{m}{2 e V^3}}$$",
        "tags": ["deflection angle", "time-dependent electric field", "proton beam", "capacitor transit"]
    },
    {
        "id": "3.374",
        "title": "Stopping Distance and Acceleration in Linearly Decreasing Electric Field",
        "difficulty": 2,
        "question": "A particle with specific charge $q/m$ moves rectilinearly due to an electric field $E(x) = E_0 - a x$, where $a$ is a positive constant, and $x$ is the distance from the point where the particle was initially at rest. Find:\n(a) the distance covered by the particle until it comes to a standstill;\n(b) the acceleration of the particle at that moment.",
        "hints": [
            "Use the work-energy theorem: $\\frac{1}{2} m v^2 = q \\int_0^x (E_0 - a x') \\, dx' = q \\left( E_0 x - \\frac{1}{2} a x^2 \\right)$.",
            "Set $v = 0$ to find the non-trivial turning point $x = \\frac{2 E_0}{a}$.",
            "The acceleration at that point is $w = \\frac{q}{m} E(x) = \\frac{q}{m} \\left( E_0 - a \\frac{2 E_0}{a} \\right) = -\\frac{q E_0}{m}$."
        ],
        "answer": "(a) $x = \\frac{2 E_0}{a}$; (b) $w = \\frac{q E_0}{m}$",
        "solution": "**(a) Distance Covered:**\nThe equation of motion is:\n$$m v \\frac{dv}{dx} = q E(x) = q (E_0 - a x)$$\nIntegrating from $x = 0$ with initial condition $v(0) = 0$:\n$$\\frac{1}{2} m v^2 = q \\int_0^x (E_0 - a x') \\, dx' = q \\left( E_0 x - \\frac{1}{2} a x^2 \\right)$$\nThe particle comes to a momentary standstill when $v = 0$:\n$$q x \\left( E_0 - \\frac{1}{2} a x \\right) = 0$$\nExcluding the initial point $x = 0$, the turning point is:\n$$x = \\frac{2 E_0}{a}$$\n\n**(b) Acceleration at Turning Point:**\nAt the position $x = \\frac{2 E_0}{a}$, the electric field is:\n$$E = E_0 - a \\left( \\frac{2 E_0}{a} \\right) = -E_0$$\nThe acceleration at this moment is:\n$$w = \\frac{q E}{m} = -\\frac{q E_0}{m}$$\nIts magnitude is:\n$$|w| = \\frac{q E_0}{m}$$",
        "tags": ["work-energy theorem", "inhomogeneous electric field", "turning point", "acceleration"]
    },
    {
        "id": "3.375",
        "title": "Time for Relativistic Electron Kinetic Energy to Equal Rest Energy",
        "difficulty": 2,
        "question": "An electron starts moving from rest in a uniform electric field of strength $E = 10\\text{ kV/cm}$. How soon after the start will the kinetic energy of the electron become equal to its rest energy?",
        "hints": [
            "When kinetic energy equals rest energy, $T = m_0 c^2$, so total energy is $E_{\\text{tot}} = T + m_0 c^2 = 2 m_0 c^2$.",
            "The relativistic momentum is $p = \\frac{1}{c}\\sqrt{E_{\\text{tot}}^2 - m_0^2 c^4} = \\sqrt{3} m_0 c$.",
            "From $\\frac{dp}{dt} = e E$, the elapsed time is $t = \\frac{p}{e E} = \\frac{\\sqrt{3} m_0 c}{e E}$."
        ],
        "answer": "$t = \\frac{\\sqrt{3} m_0 c}{e E} = 3.0\\text{ ns}$",
        "solution": "**1. Relativistic Energy and Momentum:**\nThe total energy of the electron is:\n$$E_{\\text{tot}} = T + m_0 c^2$$\nWhen $T = m_0 c^2$:\n$$E_{\\text{tot}} = 2 m_0 c^2$$\nFrom the relativistic energy-momentum invariant $E_{\\text{tot}}^2 = p^2 c^2 + m_0^2 c^4$:\n$$p = \\frac{1}{c} \\sqrt{(2 m_0 c^2)^2 - m_0^2 c^4} = \\sqrt{3} m_0 c$$\nIn general, for any kinetic energy $T$:\n$$p = \\frac{\\sqrt{T(T + 2 m_0 c^2)}}{c}$$\n\n**2. Time from Relativistic Equation of Motion:**\nUnder constant electric field $E$, the rate of change of momentum is:\n$$\\frac{dp}{dt} = e E \\implies p(t) = e E t$$\nSolving for time $t$:\n$$t = \\frac{p}{e E} = \\frac{\\sqrt{3} m_0 c}{e E}$$\n\n**3. Numerical Evaluation:**\nGiven $E = 10\\text{ kV/cm} = 1.0 \\times 10^6\\text{ V/m}$, $m_0 = 9.109 \\times 10^{-31}\\text{ kg}$, $c = 3.0 \\times 10^8\\text{ m/s}$, $e = 1.602 \\times 10^{-19}\\text{ C}$:\n$$t = \\frac{\\sqrt{3}(9.109 \\times 10^{-31}\\text{ kg})(3.0 \\times 10^8\\text{ m/s})}{(1.602 \\times 10^{-19}\\text{ C})(1.0 \\times 10^6\\text{ V/m})} = \\frac{4.733 \\times 10^{-22}}{1.602 \\times 10^{-13}} \\approx 2.95 \\times 10^{-9}\\text{ s} \\approx 3.0\\text{ ns}$$",
        "tags": ["relativistic dynamics", "kinetic energy", "rest energy", "uniform electric field"]
    },
    {
        "id": "3.376",
        "title": "Acceleration of Relativistic Electron in Uniform Electric Field",
        "difficulty": 2,
        "question": "Determine the acceleration of a relativistic electron moving along a uniform electric field of strength $E$ at the moment when its kinetic energy becomes equal to $T$.",
        "hints": [
            "For rectilinear motion along $\\mathbf{E}$, $\\frac{dp}{dt} = e E$, where $p = \\gamma m_0 v$.",
            "Differentiate $p$ with respect to time: $\\frac{dp}{dt} = m_0 \\gamma^3 w$, so acceleration is $w = \\frac{e E}{m_0 \\gamma^3}$.",
            "Express the Lorentz factor in terms of kinetic energy: $\\gamma = 1 + \\frac{T}{m_0 c^2}$, yielding $w = \\frac{e E}{m_0 \\left(1 + \\frac{T}{m_0 c^2}\\right)^3}$."
        ],
        "answer": "$w = \\frac{e E}{m_0 \\left( 1 + \\frac{T}{m_0 c^2} \\right)^3}$",
        "solution": "**1. Longitudinal Relativistic Acceleration:**\nFor 1D rectilinear motion along the electric field lines:\n$$\\frac{dp}{dt} = e E$$\nThe relativistic momentum is $p = \\frac{m_0 v}{\\sqrt{1 - v^2/c^2}} = m_0 \\gamma v$.\nDifferentiating with respect to time:\n$$\\frac{dp}{dt} = m_0 \\gamma \\frac{dv}{dt} + m_0 v \\frac{d\\gamma}{dt} = m_0 \\gamma w + m_0 v \\left( \\gamma^3 \\frac{v w}{c^2} \\right) = m_0 \\gamma^3 w \\left( \\frac{1}{\\gamma^2} + \\frac{v^2}{c^2} \\right) = m_0 \\gamma^3 w$$\nTherefore, the acceleration is:\n$$w = \\frac{e E}{m_0 \\gamma^3}$$\n\n**2. Relation to Kinetic Energy:**\nThe total energy is $E_{\\text{tot}} = \\gamma m_0 c^2 = T + m_0 c^2$, so:\n$$\\gamma = 1 + \\frac{T}{m_0 c^2}$$\nSubstituting $\\gamma$ into the acceleration expression:\n$$w = \\frac{e E}{m_0 \\left( 1 + \\frac{T}{m_0 c^2} \\right)^3}$$",
        "tags": ["relativistic acceleration", "longitudinal mass", "kinetic energy", "Lorentz factor"]
    },
    {
        "id": "3.377",
        "title": "Trajectory of Relativistic Proton in Transverse Electric Field",
        "difficulty": 3,
        "question": "At the moment $t = 0$ a relativistic proton flies with a velocity $\\mathbf{v}_0$ into the region where there is a uniform transverse electric field of strength $\\mathbf{E}$, with $\\mathbf{v}_0 \\perp \\mathbf{E}$. Find the time dependence of:\n(a) the angle $\\theta$ between the proton's velocity vector $\\mathbf{v}$ and the initial direction of motion;\n(b) the projection $v_x$ of the vector $\\mathbf{v}$ on the initial direction of motion.",
        "hints": [
            "Along the initial direction $x$, force is zero, so momentum $p_x = p_0 = \\gamma_0 m_0 v_0 = \\text{const}$.",
            "Transverse momentum grows linearly: $p_y(t) = e E t$. The angle satisfies $\\tan\\theta = \\frac{p_y}{p_x} = \\frac{e E t}{m_0 v_0} \\sqrt{1 - v_0^2/c^2}$.",
            "The velocity component is $v_x = \\frac{p_x c^2}{E_{\\text{tot}}(t)}$ with $E_{\\text{tot}}(t) = \\sqrt{p_0^2 c^2 + (e E t)^2 c^2 + m_0^2 c^4}$."
        ],
        "answer": "(a) $\\tan\\theta = \\frac{e E t}{m_0 v_0} \\sqrt{1 - \\frac{v_0^2}{c^2}}$; (b) $v_x(t) = \\frac{v_0}{\\sqrt{1 + \\left(1 - \\frac{v_0^2}{c^2}\\right) \\left( \\frac{e E t}{m_0 c} \\right)^2}}$",
        "solution": "**1. Momentum Components:**\nLet the proton initially move along the $x$-axis, and the electric field be directed along the $y$-axis.\nBecause $F_x = 0$:\n$$p_x(t) = p_0 = \\frac{m_0 v_0}{\\sqrt{1 - v_0^2/c^2}}$$\nAlong the $y$-axis, the equation of motion is $\\frac{dp_y}{dt} = e E$, giving:\n$$p_y(t) = e E t$$\n\n**(a) Angle of Motion $\\theta$:**\nThe direction of the velocity vector coincides with the direction of momentum:\n$$\\tan\\theta = \\frac{v_y}{v_x} = \\frac{p_y}{p_x} = \\frac{e E t}{p_0} = \\frac{e E t}{m_0 v_0} \\sqrt{1 - \\frac{v_0^2}{c^2}}$$\n\n**(b) Longitudinal Velocity Projection $v_x$:**\nIn relativistic dynamics, $\\mathbf{v} = \\frac{\\mathbf{p} c^2}{E_{\\text{tot}}}$, so:\n$$v_x(t) = \\frac{p_0 c^2}{\\sqrt{p_0^2 c^2 + p_y^2(t) c^2 + m_0^2 c^4}}$$\nSince $p_0^2 c^2 + m_0^2 c^4 = E_0^2 = \\frac{m_0^2 c^4}{1 - v_0^2/c^2}$:\n$$E_{\\text{tot}}(t) = \\sqrt{\\frac{m_0^2 c^4}{1 - v_0^2/c^2} + (e E t)^2 c^2} = \\frac{m_0 c^2}{\\sqrt{1 - v_0^2/c^2}} \\sqrt{1 + \\left( 1 - \\frac{v_0^2}{c^2} \\right) \\left( \\frac{e E t}{m_0 c} \\right)^2}$$\nSubstituting back:\n$$v_x(t) = \\frac{\\frac{m_0 v_0 c^2}{\\sqrt{1 - v_0^2/c^2}}}{E_{\\text{tot}}(t)} = \\frac{v_0}{\\sqrt{1 + \\left( 1 - \\frac{v_0^2}{c^2} \\right) \\left( \\frac{e E t}{m_0 c} \\right)^2}}$$",
        "tags": ["relativistic dynamics", "transverse electric field", "velocity projection", "Lorentz force"]
    },
    {
        "id": "3.378",
        "title": "Deflection of Accelerated Proton in Transverse Magnetic Field",
        "difficulty": 2,
        "question": "A proton accelerated by a potential difference $V' = 500\\text{ kV}$ flies through a uniform transverse magnetic field with induction $B = 0.51\\text{ T}$. The field occupies a region of space $d = 10\\text{ cm}$ in thickness. Find the angle $\\alpha$ through which the proton deviates from the initial direction of motion.",
        "hints": [
            "Check that the kinetic energy $e V' = 0.50\\text{ MeV} \\ll m_0 c^2 \\approx 938\\text{ MeV}$, so the proton is non-relativistic.",
            "The radius of the circular arc in the magnetic field is $R = \\frac{\\sqrt{2 m q V'}}{q B} = \\frac{1}{B}\\sqrt{\\frac{2 m V'}{q}}$.",
            "The geometry of deflection across thickness $d$ gives $\\sin\\alpha = \\frac{d}{R} = B d \\sqrt{\\frac{q}{2 m V'}}$."
        ],
        "answer": "$\\alpha = \\arcsin\\left( B d \\sqrt{\\frac{q}{2 m V'}} \\right) = 30^\\circ$",
        "solution": "**1. Radius of Curvature:**\nSince $V' = 500\\text{ kV}$, the kinetic energy is $0.50\\text{ MeV}$, which is much less than the proton rest energy ($938\\text{ MeV}$); non-relativistic formulas apply.\nThe velocity acquired from the accelerating potential is:\n$$v = \\sqrt{\\frac{2 q V'}{m}}$$\nIn the transverse magnetic field $B$, the proton executes circular motion with radius:\n$$R = \\frac{m v}{q B} = \\frac{m}{q B} \\sqrt{\\frac{2 q V'}{m}} = \\frac{1}{B} \\sqrt{\\frac{2 m V'}{q}}$$\n\n**2. Deflection Geometry:**\nPassing through a field layer of thickness $d$, the exit angle $\\alpha$ satisfies:\n$$\\sin\\alpha = \\frac{d}{R} = B d \\sqrt{\\frac{q}{2 m V'}}$$\n\n**3. Numerical Evaluation:**\nGiven $B = 0.51\\text{ T}$, $d = 0.10\\text{ m}$, $V' = 5.0 \\times 10^5\\text{ V}$, $q/m = 9.579 \\times 10^7\\text{ C/kg}$:\n$$\\sin\\alpha = (0.51)(0.10) \\sqrt{\\frac{9.579 \\times 10^7\\text{ C/kg}}{2(5.0 \\times 10^5\\text{ V})}} = 0.051 \\sqrt{95.79} = 0.051 \\times 9.787 \\approx 0.499 \\approx 0.50$$\n$$\\alpha = \\arcsin(0.50) = 30^\\circ$$",
        "tags": ["magnetic deflection", "cyclotron radius", "proton beam", "arcsin"]
    },
    {
        "id": "3.379",
        "title": "Velocity and Period of Charged Particles in Magnetic Field",
        "difficulty": 2,
        "question": "A charged particle moves along a circle of radius $r = 100\\text{ mm}$ in a uniform magnetic field with induction $B = 10.0\\text{ mT}$. Find its velocity and period of revolution if the particle is:\n(a) a non-relativistic proton;\n(b) a relativistic electron.",
        "hints": [
            "For the proton, use non-relativistic formulas: $v = \\frac{q B r}{m}$ and $T = \\frac{2\\pi m}{q B}$.",
            "For the electron, first calculate relativistic momentum $p = q B r$.",
            "Calculate total energy $E_{\\text{tot}} = \\sqrt{p^2 c^2 + m_0^2 c^4}$, velocity $v = \\frac{p c^2}{E_{\\text{tot}}}$, and period $T = \\frac{2\\pi r}{v}$."
        ],
        "answer": "(a) $v = 96\\text{ km/s} \\approx 100\\text{ km/s}$, $T = 6.5\\,\\mu\\text{s}$; (b) $v = 0.51 c$, $T = 4.1\\text{ ns}$",
        "solution": "**(a) Non-Relativistic Proton:**\n$$v = \\frac{q B r}{m_p} = \\frac{(1.602 \\times 10^{-19}\\text{ C})(0.010\\text{ T})(0.10\\text{ m})}{1.673 \\times 10^{-27}\\text{ kg}} = \\frac{1.602 \\times 10^{-22}}{1.673 \\times 10^{-27}} \\approx 9.58 \\times 10^4\\text{ m/s} \\approx 100\\text{ km/s}$$\nThe cyclotron period is:\n$$T = \\frac{2\\pi m_p}{q B} = \\frac{2\\pi (1.673 \\times 10^{-27})}{(1.602 \\times 10^{-19})(0.010)} \\approx 6.56 \\times 10^{-6}\\text{ s} = 6.5\\,\\mu\\text{s}$$\n\n**(b) Relativistic Electron:**\nThe momentum is given by:\n$$p = e B r = (1.602 \\times 10^{-19}\\text{ C})(0.010\\text{ T})(0.10\\text{ m}) = 1.602 \\times 10^{-22}\\text{ kg}\\cdot\\text{m/s}$$\nIn energy units:\n$$p c = (1.602 \\times 10^{-22})(3.0 \\times 10^8) = 4.806 \\times 10^{-14}\\text{ J} \\approx 0.300\\text{ MeV}$$\nThe electron rest energy is $m_0 c^2 \\approx 0.511\\text{ MeV}$.\nThe total energy is:\n$$E_{\\text{tot}} = \\sqrt{(p c)^2 + (m_0 c^2)^2} = \\sqrt{(0.300)^2 + (0.511)^2} = \\sqrt{0.3511} \\approx 0.593\\text{ MeV}$$\nThe velocity is:\n$$v = c \\frac{p c}{E_{\\text{tot}}} = c \\left( \\frac{0.300}{0.593} \\right) \\approx 0.51 c$$\nThe period of revolution is:\n$$T = \\frac{2\\pi r}{v} = \\frac{2\\pi (0.10\\text{ m})}{0.51(3.0 \\times 10^8\\text{ m/s})} \\approx 4.1 \\times 10^{-9}\\text{ s} = 4.1\\text{ ns}$$",
        "tags": ["cyclotron period", "relativistic electron", "proton motion", "magnetic radius"]
    },
    {
        "id": "3.380",
        "title": "Parameters of Relativistic Particle in Circular Magnetic Orbit",
        "difficulty": 2,
        "question": "A relativistic particle with charge $q$ and rest mass $m_0$ moves along a circle of radius $r$ in a uniform magnetic field of induction $B$. Find:\n(a) the modulus of the particle's momentum vector;\n(b) the kinetic energy of the particle;\n(c) the acceleration of the particle.",
        "hints": [
            "In a magnetic field, the Lorentz force provides the rate of change of momentum: $F = q v B = \\frac{v p}{r} \\implies p = q B r$.",
            "The kinetic energy is $T = E_{\\text{tot}} - m_0 c^2 = \\sqrt{p^2 c^2 + m_0^2 c^4} - m_0 c^2$.",
            "The centripetal acceleration is $w = \\frac{v^2}{r} = \\frac{p^2}{\\gamma^2 m_0^2 r} = \\frac{(q B r)^2}{r m_0^2 [1 + (q B r / m_0 c)^2]}$."
        ],
        "answer": "(a) $p = q B r$; (b) $T = m_0 c^2 \\left[ \\sqrt{1 + \\left( \\frac{q B r}{m_0 c} \\right)^2} - 1 \\right]$; (c) $w = \\frac{q^2 B^2 r}{m_0^2 \\left[ 1 + \\left( \\frac{q B r}{m_0 c} \\right)^2 \\right]}$",
        "solution": "**(a) Momentum:**\nThe equation of circular motion under the Lorentz force is:\n$$\\frac{dp}{dt} = p \\omega = p \\left( \\frac{v}{r} \\right) = q v B \\implies p = q B r$$\n\n**(b) Kinetic Energy:**\nThe total relativistic energy is:\n$$E_{\\text{tot}} = \\sqrt{p^2 c^2 + m_0^2 c^4} = \\sqrt{(q B r c)^2 + m_0^2 c^4} = m_0 c^2 \\sqrt{1 + \\left( \\frac{q B r}{m_0 c} \\right)^2}$$\nThe kinetic energy is:\n$$T = E_{\\text{tot}} - m_0 c^2 = m_0 c^2 \\left[ \\sqrt{1 + \\left( \\frac{q B r}{m_0 c} \\right)^2} - 1 \\right]$$\n\n**(c) Acceleration:**\nThe kinematic acceleration in circular motion is $w = \\frac{v^2}{r}$.\nSince $p = \\gamma m_0 v$, we have $v = \\frac{p}{\\gamma m_0}$, so:\n$$w = \\frac{p^2}{\\gamma^2 m_0^2 r}$$\nUsing $\\gamma^2 = 1 + \\left( \\frac{p}{m_0 c} \\right)^2 = 1 + \\left( \\frac{q B r}{m_0 c} \\right)^2$:\n$$w = \\frac{(q B r)^2}{m_0^2 r \\left[ 1 + \\left( \\frac{q B r}{m_0 c} \\right)^2 \\right]} = \\frac{q^2 B^2 r}{m_0^2 \\left[ 1 + \\left( \\frac{q B r}{m_0 c} \\right)^2 \\right]}$$",
        "tags": ["relativistic kinematics", "circular orbit", "magnetic field", "kinetic energy"]
    },
    {
        "id": "3.381",
        "title": "Kinetic Energy Limit for 1% Relativistic Period Deviation",
        "difficulty": 1,
        "question": "Up to what values of kinetic energy does the period of revolution of an electron and a proton in a uniform magnetic field exceed that at non-relativistic velocities by $\\eta = 1.0\\%$?",
        "hints": [
            "The relativistic period of revolution is $T = \\frac{2\\pi \\gamma m_0}{q B} = \\gamma T_0$.",
            "The condition $T = (1 + \\eta) T_0$ implies $\\gamma = 1 + \\eta$.",
            "The kinetic energy is $T = (\\gamma - 1) m_0 c^2 = \\eta m_0 c^2$. Calculate for electron and proton."
        ],
        "answer": "$T = \\eta m_0 c^2$; $5.1\\text{ keV}$ for electron, $9.4\\text{ MeV}$ for proton",
        "solution": "**1. Relativistic Period Dependency:**\nThe period of revolution of a charged particle in a magnetic field is:\n$$T = \\frac{2\\pi \\gamma m_0}{q B}$$\nAt non-relativistic speeds, $\\gamma \\to 1$ and $T_0 = \\frac{2\\pi m_0}{q B}$.\nThus:\n$$T = \\gamma T_0$$\n\n**2. Kinetic Energy Expression:**\nFor the period to exceed the classical value by a fraction $\\eta$:\n$$\\gamma = 1 + \\eta$$\nThe kinetic energy is:\n$$T_k = (\\gamma - 1) m_0 c^2 = \\eta m_0 c^2$$\n\n**3. Numerical Evaluation:**\n- For an electron ($m_0 c^2 = 0.511\\text{ MeV} = 511\\text{ keV}$):\n$$T_k = (0.010)(511\\text{ keV}) \\approx 5.1\\text{ keV}$$\n- For a proton ($m_0 c^2 = 938.3\\text{ MeV}$):\n$$T_k = (0.010)(938.3\\text{ MeV}) \\approx 9.4\\text{ MeV}$$",
        "tags": ["cyclotron resonance", "relativistic period", "kinetic energy limit", "Lorentz factor"]
    },
    {
        "id": "3.382",
        "title": "Pitch of Helical Electron Trajectory in Magnetic Field",
        "difficulty": 2,
        "question": "An electron accelerated by a potential difference $V = 1.0\\text{ kV}$ moves in a uniform magnetic field at an angle $\\alpha = 30^\\circ$ to the vector $\\mathbf{B}$ whose modulus is $B = 29\\text{ mT}$. Find the pitch of the helical trajectory of the electron.",
        "hints": [
            "The speed of the electron is $v = \\sqrt{\\frac{2 e V}{m}}$.",
            "The velocity component parallel to the magnetic field is $v_\\parallel = v \\cos\\alpha$.",
            "The period of revolution is $T = \\frac{2\\pi m}{e B}$. The pitch of the helix is $h = v_\\parallel T = \\frac{2\\pi \\cos\\alpha}{B} \\sqrt{\\frac{2 m V}{e}}$."
        ],
        "answer": "$h = \\frac{2\\pi \\cos\\alpha}{B} \\sqrt{\\frac{2 m V}{e}} = 2.0\\text{ cm}$",
        "solution": "**1. Velocity Components:**\nThe total speed of the accelerated electron is:\n$$v = \\sqrt{\\frac{2 e V}{m}}$$\nThe velocity parallel to the magnetic field $\\mathbf{B}$ is:\n$$v_\\parallel = v \\cos\\alpha = \\sqrt{\\frac{2 e V}{m}} \\cos\\alpha$$\n\n**2. Period of Revolution and Pitch:**\nThe period of circular motion in the transverse plane is:\n$$T = \\frac{2\\pi m}{e B}$$\nThe pitch $h$ of the helix (distance traveled along $\\mathbf{B}$ in one full revolution) is:\n$$h = v_\\parallel T = \\left( \\sqrt{\\frac{2 e V}{m}} \\cos\\alpha \\right) \\left( \\frac{2\\pi m}{e B} \\right) = \\frac{2\\pi \\cos\\alpha}{B} \\sqrt{\\frac{2 m V}{e}}$$\n\n**3. Numerical Evaluation:**\nGiven $V = 1000\\text{ V}$, $\\alpha = 30^\\circ$ ($\\cos 30^\\circ = \\frac{\\sqrt{3}}{2} \\approx 0.866$), $B = 0.029\\text{ T}$, $e/m = 1.7588 \\times 10^{11}\\text{ C/kg}$:\n$$v = \\sqrt{2(1.7588 \\times 10^{11})(1000)} = \\sqrt{3.518 \\times 10^{14}} \\approx 1.876 \\times 10^7\\text{ m/s}$$\n$$v_\\parallel = (1.876 \\times 10^7)(0.866) \\approx 1.624 \\times 10^7\\text{ m/s}$$\n$$T = \\frac{2\\pi}{(1.7588 \\times 10^{11})(0.029)} \\approx 1.232 \\times 10^{-9}\\text{ s}$$\n$$h = (1.624 \\times 10^7\\text{ m/s})(1.232 \\times 10^{-9}\\text{ s}) \\approx 0.020\\text{ m} = 2.0\\text{ cm}$$",
        "tags": ["helical motion", "helix pitch", "magnetic field", "cyclotron period"]
    },
    {
        "id": "3.383",
        "title": "Specific Charge from Magnetic Focusing of Charged Particle Beam",
        "difficulty": 2,
        "question": "A slightly divergent beam of non-relativistic charged particles accelerated by a potential difference $V$ propagates from point $A$ along the axis of a straight solenoid. The beam is brought into focus at a distance $l$ from point $A$ at two successive values of magnetic induction $B_1$ and $B_2$. Find the specific charge $q/m$ of the particles.",
        "hints": [
            "For small divergence angles, particles complete an integer number of cyclotron revolutions over length $l$: $l = k v_\\parallel T = k v \\frac{2\\pi m}{q B_k}$.",
            "For two successive focal states ($k$ and $k+1$), the difference in field is $B_2 - B_1 = \\frac{2\\pi m v}{q l}$.",
            "Substitute $v = \\sqrt{\\frac{2 q V}{m}}$ and solve for $q/m = \\frac{8\\pi^2 V}{l^2 (B_2 - B_1)^2}$."
        ],
        "answer": "$\\frac{q}{m} = \\frac{8\\pi^2 V}{l^2 (B_2 - B_1)^2}$",
        "solution": "**1. Focusing Condition in Axial Magnetic Field:**\nParticles leaving point $A$ at small angles $\\alpha \\ll 1$ have axial velocity $v_\\parallel = v \\cos\\alpha \\approx v$.\nAll particles return to the axis (focusing) after completing integer $k$ cyclotron revolutions:\n$$l = k v T_k = k v \\left( \\frac{2\\pi m}{q B_k} \\right)$$\n$$B_k = k \\frac{2\\pi m v}{q l}$$\n\n**2. Successive Values of Magnetic Induction:**\nFor two consecutive focusing states ($k$ and $k+1$):\n$$\\Delta B = B_2 - B_1 = \\frac{2\\pi m v}{q l}$$\n\n**3. Determining Specific Charge:**\nUsing $v = \\sqrt{\\frac{2 q V}{m}}$:\n$$\\Delta B = \\frac{2\\pi m}{q l} \\sqrt{\\frac{2 q V}{m}} = \\frac{2\\pi}{l} \\sqrt{\\frac{2 m V}{q}}$$\nSquaring both sides:\n$$(\\Delta B)^2 = \\frac{8\\pi^2 V}{l^2 (q/m)}$$\n$$\\frac{q}{m} = \\frac{8\\pi^2 V}{l^2 (B_2 - B_1)^2}$$",
        "tags": ["magnetic lens", "beam focusing", "specific charge", "solenoid"]
    },
    {
        "id": "3.384",
        "title": "Impact Radius of Electron on Transverse Screen in Solenoid Field",
        "difficulty": 2,
        "question": "A non-relativistic electron originates at a point $A$ lying on the axis of a straight solenoid and moves with velocity $v$ at an angle $\\alpha$ to the axis. The magnetic induction is $B$. Find the distance $r$ from the axis to the point on the screen that the electron strikes. The screen is perpendicular to the axis and located at a distance $l$ from point $A$.",
        "hints": [
            "The electron executes helical motion with transverse radius $\\rho = \\frac{m v \\sin\\alpha}{e B}$ and axial velocity $v_\\parallel = v \\cos\\alpha$.",
            "The time taken to reach the screen is $t = \\frac{l}{v \\cos\\alpha}$, during which it rotates by angle $\\varphi = \\omega t = \\frac{e B l}{m v \\cos\\alpha}$.",
            "The distance from the starting point on the axis to the point on the transverse circle after rotating through angle $\\varphi$ is $r = 2\\rho |\\sin(\\varphi/2)|$."
        ],
        "answer": "$r = 2\\rho \\left| \\sin\\left( \\frac{\\varphi}{2} \\right) \\right|$, where $\\rho = \\frac{m v \\sin\\alpha}{e B}$ and $\\varphi = \\frac{e B l}{m v \\cos\\alpha}$",
        "solution": "**1. Kinematics in Axial Magnetic Field:**\nChoosing the $z$-axis along the solenoid axis:\n$$v_z = v \\cos\\alpha, \\quad v_\\perp = v \\sin\\alpha$$\nIn the transverse plane, the electron moves on a circle of radius:\n$$\\rho = \\frac{m v_\\perp}{e B} = \\frac{m v \\sin\\alpha}{e B}$$\npassing through the origin (the axis point $A$).\n\n**2. Transit Time and Phase Angle:**\nThe screen is situated at $z = l$. The transit time is:\n$$t = \\frac{l}{v_z} = \\frac{l}{v \\cos\\alpha}$$\nThe angle traversed along the cyclotron circle during this time is:\n$$\\varphi = \\omega_c t = \\left( \\frac{e B}{m} \\right) \\left( \\frac{l}{v \\cos\\alpha} \\right) = \\frac{e B l}{m v \\cos\\alpha}$$\n\n**3. Distance from the Axis:**\nThe distance from the origin to a point on a circle of radius $\\rho$ that passes through the origin after traversing an angle $\\varphi$ subtended at the center is:\n$$r = 2\\rho \\left| \\sin\\left( \\frac{\\varphi}{2} \\right) \\right|$$",
        "tags": ["helical motion", "solenoid axis", "cyclotron rotation", "chord length"]
    },
    {
        "id": "3.385",
        "title": "Maximum Distance of Escaping Electron from Current-Carrying Wire",
        "difficulty": 3,
        "question": "From the surface of a round wire of radius $a$ carrying a direct current $I$, an electron escapes with a velocity $v_0$ perpendicular to the surface. Find the maximum distance of the electron from the axis of the wire before it turns back due to the action of the magnetic field generated by the current.",
        "hints": [
            "Outside the wire ($r > a$), the magnetic field is azimuthal: $B(r) = \\frac{\\mu_0 I}{2\\pi r}$.",
            "The equation of motion along the wire axis $z$ gives $m \\frac{dv_z}{dt} = e v_r B(r) = e \\frac{dr}{dt} \\frac{\\mu_0 I}{2\\pi r}$.",
            "Integrate to find $v_z(r) = \\frac{e \\mu_0 I}{2\\pi m} \\ln(r/a)$. At maximum radius, $v_r = 0$, so $v_z = v_0$, yielding $r_{\\max} = a e^{v_0 / b}$ with $b = \\frac{\\mu_0 e I}{2\\pi m}$."
        ],
        "answer": "$r_{\\max} = a e^{v_0 / b}$, where $b = \\frac{\\mu_0 e I}{2\\pi m}$",
        "solution": "**1. Magnetic Field and Equations of Motion:**\nOutside the wire of radius $a$, the magnetic field is purely azimuthal:\n$$B_\\theta(r) = \\frac{\\mu_0 I}{2\\pi r}$$\nThe Lorentz force on the electron (charge $-e$) is $\\mathbf{F} = -e [\\mathbf{v} \\times \\mathbf{B}]$.\nIn cylindrical coordinates $(r, \\theta, z)$:\n$$F_z = e v_r B_\\theta(r) = e \\frac{dr}{dt} \\left( \\frac{\\mu_0 I}{2\\pi r} \\right)$$\n$$m \\frac{dv_z}{dt} = \\frac{\\mu_0 e I}{2\\pi r} \\frac{dr}{dt}$$\n\n**2. Integrating Longitudinal Velocity:**\nIntegrating from the initial release at $r = a$ where $v_z(a) = 0$:\n$$m v_z(r) = \\frac{\\mu_0 e I}{2\\pi} \\int_a^r \\frac{dr'}{r'} = \\frac{\\mu_0 e I}{2\\pi} \\ln\\left( \\frac{r}{a} \\right)$$\n$$v_z(r) = b \\ln\\left( \\frac{r}{a} \\right), \\quad \\text{where } b = \\frac{\\mu_0 e I}{2\\pi m}$$\n\n**3. Maximum Radial Distance:**\nBecause the magnetic force does no work, the electron speed is strictly conserved:\n$$v_r^2(r) + v_z^2(r) = v_0^2$$\nAt the turning point ($r = r_{\\max}$), the radial velocity vanishes ($v_r = 0$), so $v_z = v_0$:\n$$b \\ln\\left( \\frac{r_{\\max}}{a} \\right) = v_0 \\implies \\ln\\left( \\frac{r_{\\max}}{a} \\right) = \\frac{v_0}{b}$$\n$$r_{\\max} = a e^{v_0 / b}$$",
        "tags": ["magnetic deflection", "wire magnetic field", "turning point", "conservation of energy"]
    },
    {
        "id": "3.386",
        "title": "Velocity and Specific Charge in Cylindrical Capacitor and Transverse B",
        "difficulty": 2,
        "question": "A non-relativistic charged particle flies through the electric field of a cylindrical capacitor and gets into a uniform transverse magnetic field with induction $B$. In the capacitor the particle moves along a circular arc, and in the magnetic field along a semi-circle of radius $r$. The potential difference applied to the capacitor is $V$, and the electrode radii are $a$ and $b$ ($a < b$). Find the velocity of the particle and its specific charge $q/m$.",
        "hints": [
            "In the cylindrical capacitor, the electric field is $E(R) = \\frac{V}{R \\ln(b/a)}$.",
            "The centripetal force condition gives $\\frac{m v^2}{R} = q E(R) = \\frac{q V}{R \\ln(b/a)} \\implies m v^2 = \\frac{q V}{\\ln(b/a)}$.",
            "In the magnetic field, $r = \\frac{m v}{q B} \\implies m v = q B r$. Combine both relations to find $v$ and $q/m$."
        ],
        "answer": "$v = \\frac{V}{B r \\ln(b/a)}, \\quad \\frac{q}{m} = \\frac{V}{B^2 r^2 \\ln(b/a)}$",
        "solution": "**1. Motion in Cylindrical Capacitor:**\nBetween cylindrical plates with radii $a$ and $b$ holding potential difference $V$, the radial electric field at radius $R$ is:\n$$E(R) = \\frac{V}{R \\ln(b/a)}$$\nFor the particle to move along a concentric circular arc of radius $R$, the electrostatic force must provide the centripetal acceleration:\n$$\\frac{m v^2}{R} = q E(R) = \\frac{q V}{R \\ln(b/a)} \\implies m v^2 = \\frac{q V}{\\ln(b/a)}$$\n\n**2. Motion in Transverse Magnetic Field:**\nUpon entering the uniform magnetic field $B$, the particle traces a semicircle of radius $r$:\n$$r = \\frac{m v}{q B} \\implies m v = q B r$$\n\n**3. Determining Velocity and Specific Charge:**\nDividing the two equations:\n$$\\frac{m v^2}{m v} = \\frac{\\frac{q V}{\\ln(b/a)}}{q B r} \\implies v = \\frac{V}{B r \\ln(b/a)}$$\nNow substituting $v$ back into $q B r = m v$:\n$$\\frac{q}{m} = \\frac{v}{B r} = \\frac{V}{B^2 r^2 \\ln(b/a)}$$",
        "tags": ["cylindrical capacitor", "velocity selector", "mass spectrometry", "specific charge"]
    },
    {
        "id": "3.387",
        "title": "Crossing Coordinates in Parallel Electric and Magnetic Fields",
        "difficulty": 2,
        "question": "Uniform electric and magnetic fields with strength $E$ and induction $B$ respectively are both directed along the $y$-axis. A particle with specific charge $q/m$ leaves the origin $O$ in the direction of the $x$-axis with an initial non-relativistic velocity $v_0$. Find:\n(a) the coordinate $y_n$ of the particle when it crosses the $y$-axis for the $n$-th time;\n(b) the angle $\\alpha$ between the particle's velocity vector and the $y$-axis at that moment.",
        "hints": [
            "In the $x$-$z$ plane, the particle undergoes circular motion with period $T = \\frac{2\\pi m}{q B}$, returning to the $y$-axis at times $t_n = n T$.",
            "Along the $y$-axis, the particle undergoes uniform acceleration $a_y = \\frac{q E}{m}$: $y(t) = \\frac{1}{2} a_y t^2$.",
            "Calculate $y_n = y(t_n) = \\frac{2\\pi^2 n^2 m E}{q B^2}$, and $\\tan\\alpha = \\frac{v_0}{v_y(t_n)} = \\frac{v_0 B}{2\\pi n E}$."
        ],
        "answer": "(a) $y_n = \\frac{2\\pi^2 n^2 m E}{q B^2}$; (b) $\\tan\\alpha = \\frac{v_0 B}{2\\pi n E}$",
        "solution": "**1. Transverse Circular Motion:**\nThe magnetic field along the $y$-axis acts only on velocity components in the $x$-$z$ plane.\nWith initial velocity $v_0$ along $x$, the motion in the $x$-$z$ plane is circular with cyclotron frequency $\\omega = \\frac{q B}{m}$ and period:\n$$T = \\frac{2\\pi}{\\omega} = \\frac{2\\pi m}{q B}$$\nThe particle returns to the $y$-axis ($x = 0, z = 0$) whenever $\\omega t = 2\\pi n$, so:\n$$t_n = n T = \\frac{2\\pi n m}{q B}$$\n\n**(a) Coordinate $y_n$:**\nAlong the $y$-axis, the electric field causes constant acceleration:\n$$a_y = \\frac{q E}{m}$$\nStarting from rest at $y = 0$, the $y$-coordinate at time $t_n$ is:\n$$y_n = \\frac{1}{2} a_y t_n^2 = \\frac{1}{2} \\left( \\frac{q E}{m} \\right) \\left( \\frac{2\\pi n m}{q B} \\right)^2 = \\frac{2\\pi^2 n^2 m E}{q B^2}$$\n\n**(b) Angle $\\alpha$ with the $y$-axis:**\nAt time $t_n$, the velocity components are:\n- Transverse speed in the $x$-$z$ plane: $v_\\perp = v_0$.\n- Longitudinal velocity along $y$: $v_y = a_y t_n = \\left( \\frac{q E}{m} \\right) \\left( \\frac{2\\pi n m}{q B} \\right) = \\frac{2\\pi n E}{B}$.\nThe angle $\\alpha$ with the $y$-axis satisfies:\n$$\\tan\\alpha = \\frac{v_\\perp}{v_y} = \\frac{v_0}{2\\pi n E / B} = \\frac{v_0 B}{2\\pi n E}$$",
        "tags": ["parallel E and B", "helical trajectory", "cyclotron period", "velocity angle"]
    },
    {
        "id": "3.388",
        "title": "Parabolic Trace in Thomson Mass Spectrograph",
        "difficulty": 2,
        "question": "A narrow beam of identical ions with specific charge $q/m$, possessing different velocities, enters along the $x$-axis into a region of space with uniform parallel electric and magnetic fields $E$ and $B$ (both along the $y$-axis). A plane screen at right angles to the $x$-axis is located at distance $l$ from the entry point. Find the equation of the trace that the ions leave on the screen. Demonstrate that for small deflections this is a parabola.",
        "hints": [
            "For small deflections, transit time is $t \\approx \\frac{l}{v_x}$.",
            "The electric deflection along $y$ is $y = \\frac{1}{2}\\frac{q E}{m} t^2 = \\frac{q E l^2}{2 m v_x^2}$.",
            "The magnetic deflection along $z$ is $z = \\frac{1}{2}\\frac{q B}{m} v_x t^2 = \\frac{q B l^2}{2 m v_x}$. Eliminate $v_x$ to find $y(z)$."
        ],
        "answer": "$z = \\frac{l q B}{m E} \\tan\\left( \\frac{m E y}{q B^2} \\right)$; for $z \\ll l$ this reduces to the parabola $y = \\frac{2 m E}{q l^2 B^2} z^2$",
        "solution": "**1. Equations of Deflection:**\nIons enter along the $x$-axis with speed $v_x$.\nFor small angles of deflection over flight distance $l$, the transit time is:\n$$t = \\frac{l}{v_x}$$\n- The electric field along $y$ produces acceleration $a_y = \\frac{q E}{m}$, yielding deflection:\n$$y = \\frac{1}{2} a_y t^2 = \\frac{q E l^2}{2 m v_x^2}$$\n- The magnetic field along $y$ produces Lorentz force along $z$ with acceleration $a_z = \\frac{q v_x B}{m}$, giving deflection:\n$$z = \\frac{1}{2} a_z t^2 = \\frac{1}{2} \\left( \\frac{q v_x B}{m} \\right) \\left( \\frac{l}{v_x} \\right)^2 = \\frac{q B l^2}{2 m v_x}$$\n\n**2. Eliminating Velocity:**\nFrom the magnetic deflection equation, express $v_x$ as:\n$$v_x = \\frac{q B l^2}{2 m z}$$\nSubstituting $v_x$ into the electric deflection equation:\n$$y = \\frac{q E l^2}{2 m} \\frac{1}{\\left( \\frac{q B l^2}{2 m z} \\right)^2} = \\frac{q E l^2}{2 m} \\frac{4 m^2 z^2}{q^2 B^2 l^4} = \\frac{2 m E}{q l^2 B^2} z^2$$\n\n**3. Conclusion:**\nThis is precisely the equation of a parabola $y = k z^2$, where the curvature $k = \\frac{2 m E}{q l^2 B^2}$ depends uniquely on the specific charge $q/m$ of the ions, demonstrating the operating principle of J.J. Thomson's parabola mass spectrograph.",
        "tags": ["Thomson mass spectrograph", "parabolic trace", "crossed fields", "isotope separation"]
    },
    {
        "id": "3.389",
        "title": "Force on Target from Undeviated Proton Beam",
        "difficulty": 2,
        "question": "A non-relativistic proton beam passes without deviation through a region of space with uniform transverse mutually perpendicular electric and magnetic fields with $E = 120\\text{ kV/m}$ and $B = 50\\text{ mT}$. Then the beam strikes a grounded target. Find the force with which the beam acts on the target if the beam current is $I = 0.80\\text{ mA}$.",
        "hints": [
            "Undeviated passage through crossed fields (velocity filter) requires $v = \\frac{E}{B}$.",
            "The proton flow rate is $\\frac{dN}{dt} = \\frac{I}{e}$.",
            "The force exerted on the absorbing target is the rate of momentum delivery: $F = \\frac{dp}{dt} = \\frac{dN}{dt} (m v) = \\frac{m E I}{e B}$."
        ],
        "answer": "$F = \\frac{m E I}{e B} = 20\\,\\mu\\text{N}$",
        "solution": "**1. Beam Velocity:**\nFor a beam to pass through crossed electric and magnetic fields without deflection, the electric and magnetic forces must balance exactly:\n$$e E = e v B \\implies v = \\frac{E}{B}$$\n\n**2. Force on the Target:**\nWhen the beam is completely absorbed by the target, the force is equal to the momentum transferred per unit time:\n$$F = \\frac{dp}{dt} = \\left( \\frac{dN}{dt} \\right) m v$$\nSince the beam current is $I = e \\frac{dN}{dt}$, the arrival rate is $\\frac{dN}{dt} = \\frac{I}{e}$:\n$$F = \\frac{I}{e} m v = \\frac{m E I}{e B}$$\n\n**3. Numerical Evaluation:**\nGiven $E = 1.20 \\times 10^5\\text{ V/m}$, $B = 0.050\\text{ T}$, $I = 0.80 \\times 10^{-3}\\text{ A}$, $m/e = 1.044 \\times 10^{-8}\\text{ kg/C}$:\n$$v = \\frac{1.20 \\times 10^5}{0.050} = 2.40 \\times 10^6\\text{ m/s}$$\n$$F = (1.044 \\times 10^{-8}\\text{ kg/C})(2.40 \\times 10^6\\text{ m/s})(0.80 \\times 10^{-3}\\text{ A}) \\approx 2.0 \\times 10^{-5}\\text{ N} = 20\\,\\mu\\text{N}$$",
        "tags": ["velocity selector", "crossed fields", "beam force", "momentum transfer"]
    },
    {
        "id": "3.390",
        "title": "Helix Pitch After Switching Off Crossed Electric Field",
        "difficulty": 2,
        "question": "Non-relativistic protons move rectilinearly in a region of space with uniform mutually perpendicular fields $E = 4.0\\text{ kV/m}$ and $B = 50\\text{ mT}$. The trajectory lies in the $x$-$z$ plane and forms an angle $\\varphi = 30^\\circ$ with the $x$-axis. Find the pitch of the helical trajectory along which the protons will move after the electric field is switched off.",
        "hints": [
            "In crossed fields, rectilinear motion requires balance of forces, relating velocity $v$ to $E$ and $B$: $v_\\perp = v \\sin\\varphi = \\frac{E}{B}$.",
            "The parallel velocity along $\\mathbf{B}$ is $v_\\parallel = v \\cos\\varphi = \\frac{E}{B} \\cot\\varphi$.",
            "After $\\mathbf{E}$ is switched off, the protons execute helical motion around $\\mathbf{B}$ with pitch $\\Delta l = v_\\parallel T = \\frac{2\\pi m E}{e B^2} \\cot\\varphi$."
        ],
        "answer": "$\\Delta l = \\frac{2\\pi m E}{e B^2} \\cot\\varphi = 6.2\\text{ cm}$",
        "solution": "**1. Initial Velocity from Crossed Fields:**\nIn crossed fields, the electric field $\\mathbf{E}$ is along the $y$-axis and the magnetic field $\\mathbf{B}$ is in the $x$-$z$ plane.\nFor rectilinear motion, the Lorentz force must vanish:\n$$e E = e v_\\perp B \\implies v_\\perp = \\frac{E}{B}$$\nWith the trajectory forming an angle $\\varphi = 30^\\circ$ with the field direction (or perpendicular axis), the velocity component along the magnetic field is:\n$$v_\\parallel = \\frac{E}{B} \\cot\\varphi$$\n\n**2. Pitch of Helix in Magnetic Field:**\nWhen $\\mathbf{E}$ is removed, the protons move solely under magnetic field $\\mathbf{B}$.\nThe period of cyclotron revolution is:\n$$T = \\frac{2\\pi m}{e B}$$\nThe pitch of the helical trajectory is:\n$$\\Delta l = v_\\parallel T = \\left( \\frac{E}{B} \\cot\\varphi \\right) \\left( \\frac{2\\pi m}{e B} \\right) = \\frac{2\\pi m E}{e B^2} \\cot\\varphi$$\n\n**3. Numerical Evaluation:**\nGiven $E = 4.0 \\times 10^3\\text{ V/m}$, $B = 0.050\\text{ T}$, $\\varphi = 30^\\circ$ ($\\cot 30^\\circ = \\sqrt{3} \\approx 1.732$), $e/m = 9.579 \\times 10^7\\text{ C/kg}$:\n$$\\Delta l = \\frac{2\\pi (4000)(1.732)}{(9.579 \\times 10^7)(0.050)^2} = \\frac{43530}{239475} \\approx 0.062\\text{ m} = 6.2\\text{ cm}$$",
        "tags": ["crossed fields", "helical trajectory", "pitch of helix", "proton motion"]
    },
    {
        "id": "3.391",
        "title": "Specific Charge from Beam Deflection Shift",
        "difficulty": 2,
        "question": "A beam of non-relativistic charged particles moves without deviation through a region $A$ of length $a$ where there are transverse mutually perpendicular fields $E$ and $B$. When the magnetic field is switched off, the trace of the beam on a screen $S$ at distance $b$ from the region shifts by $\\Delta x$. Find the specific charge $q/m$ of the particles.",
        "hints": [
            "With both fields on, $v = \\frac{E}{B}$.",
            "When $B$ is turned off, the particle is accelerated transversely by $E$ over distance $a$, acquiring transverse velocity $v_x = \\frac{q E a}{m v}$ and exit deflection $x_1 = \\frac{q E a^2}{2 m v^2}$.",
            "Drift over distance $b$ adds deflection $x_2 = v_x \\frac{b}{v} = \\frac{q E a b}{m v^2}$. Total shift is $\\Delta x = x_1 + x_2 = \\frac{q E a}{m v^2}\\left(\\frac{a}{2} + b\\right)$. Substitute $v = E/B$."
        ],
        "answer": "$\\frac{q}{m} = \\frac{2 E \\Delta x}{B^2 a (a + 2b)}$",
        "solution": "**1. Velocity Selection:**\nWith both fields active, the beam passes without deviation, so:\n$$v = \\frac{E}{B}$$\n\n**2. Deflection Without Magnetic Field:**\nWhen the magnetic field is turned off, the particle experiences transverse acceleration $w = \\frac{q E}{m}$ within region $A$ of length $a$.\nThe transit time through region $A$ is $t_1 = \\frac{a}{v}$.\nAt the exit of region $A$:\n- Transverse velocity: $v_x = w t_1 = \\frac{q E a}{m v}$.\n- Transverse displacement: $x_1 = \\frac{1}{2} w t_1^2 = \\frac{q E a^2}{2 m v^2}$.\n\n**3. Drift to the Screen:**\nOver the drift distance $b$ to the screen, time of flight is $t_2 = \\frac{b}{v}$, contributing an additional shift:\n$$x_2 = v_x t_2 = \\frac{q E a b}{m v^2}$$\nThe total shift observed on the screen is:\n$$\\Delta x = x_1 + x_2 = \\frac{q E a}{m v^2} \\left( \\frac{a}{2} + b \\right) = \\frac{q E a (a + 2b)}{2 m v^2}$$\n\n**4. Solving for Specific Charge:**\nSubstituting $v = \\frac{E}{B}$:\n$$\\Delta x = \\frac{q E a (a + 2b)}{2 m (E/B)^2} = \\frac{q B^2 a (a + 2b)}{2 m E}$$\n$$\\frac{q}{m} = \\frac{2 E \\Delta x}{B^2 a (a + 2b)}$$",
        "tags": ["specific charge", "velocity selector", "beam shift", "transverse deflection"]
    },
    {
        "id": "3.392",
        "title": "Cycloidal Motion of Charged Particle in Crossed Fields",
        "difficulty": 3,
        "question": "A particle with specific charge $q/m$ moves in the region of space where there are uniform mutually perpendicular fields $E$ (along $y$) and $B$ (along $z$). At $t = 0$ the particle was at the origin $O$ with zero velocity. For the non-relativistic case, find:\n(a) the law of motion $x(t)$ and $y(t)$, and the shape of the trajectory;\n(b) the length $s$ of the trajectory segment between two nearest cusps;\n(c) the mean drift velocity along the $x$-axis.",
        "hints": [
            "Write the Lorentz force equations: $m \\ddot{x} = q B \\dot{y}$ and $m \\ddot{y} = q E - q B \\dot{x}$.",
            "Integrating with $x(0) = y(0) = 0$ and $\\dot{x}(0) = \\dot{y}(0) = 0$ yields a cycloid: $x(t) = a(\\omega t - \\sin\\omega t)$ and $y(t) = a(1 - \\cos\\omega t)$ with $a = \\frac{m E}{q B^2}$ and $\\omega = \\frac{q B}{m}$.",
            "Calculate path length: $s = \\int_0^{2\\pi/\\omega} \\sqrt{\\dot{x}^2 + \\dot{y}^2} \\, dt = 8a = \\frac{8 m E}{q B^2}$. Drift velocity is $v_d = \\frac{E}{B}$."
        ],
        "answer": "(a) $x(t) = a(\\omega t - \\sin\\omega t), \\; y(t) = a(1 - \\cos\\omega t)$, cycloid with $a = \\frac{m E}{q B^2}, \\omega = \\frac{q B}{m}$; (b) $s = \\frac{8 m E}{q B^2}$; (c) $v_{\\text{drift}} = \\frac{E}{B}$",
        "solution": "**(a) Laws of Motion:**\nWith $\\mathbf{E} = E \\hat{\\mathbf{j}}$ and $\\mathbf{B} = B \\hat{\\mathbf{k}}$, Newton's second law is:\n$$m \\ddot{x} = q B \\dot{y}, \\quad m \\ddot{y} = q E - q B \\dot{x}$$\nDefining $\\omega = \\frac{q B}{m}$:\n$$\\ddot{x} = \\omega \\dot{y}, \\quad \\ddot{y} = \\frac{q E}{m} - \\omega \\dot{x}$$\nIntegrating the first equation with $\\dot{x}(0) = 0, y(0) = 0$:\n$$\\dot{x} = \\omega y$$\nSubstituting into the second equation:\n$$\\ddot{y} + \\omega^2 y = \\frac{q E}{m}$$\nWith initial conditions $y(0) = 0, \\dot{y}(0) = 0$, the solution is:\n$$y(t) = \\frac{q E}{m \\omega^2} (1 - \\cos\\omega t) = a (1 - \\cos\\omega t)$$\nwhere $a = \\frac{m E}{q B^2}$.\nThen:\n$$\\dot{x}(t) = \\omega a (1 - \\cos\\omega t) \\implies x(t) = a(\\omega t - \\sin\\omega t)$$\nThis describes a **cycloid**, generated by the rim of a circle of radius $a$ rolling along the $x$-axis.\n\n**(b) Arc Length of One Cycloid Arch:**\nThe velocity components are:\n$$\\dot{x} = a \\omega (1 - \\cos\\omega t), \\quad \\dot{y} = a \\omega \\sin\\omega t$$\n$$v(t) = \\sqrt{\\dot{x}^2 + \\dot{y}^2} = a \\omega \\sqrt{(1 - \\cos\\omega t)^2 + \\sin^2\\omega t} = a \\omega \\sqrt{2(1 - \\cos\\omega t)} = 2 a \\omega \\sin\\left( \\frac{\\omega t}{2} \\right)$$\nIntegrating over one period $T = \\frac{2\\pi}{\\omega}$:\n$$s = \\int_0^{2\\pi/\\omega} 2 a \\omega \\sin\\left( \\frac{\\omega t}{2} \\right) dt = 2 a \\omega \\left[ -\\frac{2}{\\omega} \\cos\\left( \\frac{\\omega t}{2} \\right) \\right]_0^{2\\pi/\\omega} = 8a = \\frac{8 m E}{q B^2}$$\n\n**(c) Mean Drift Velocity:**\nOver one period $T = \\frac{2\\pi}{\\omega}$, the displacement along $x$ is $\\Delta x = 2\\pi a$.\nThe mean velocity is:\n$$v_{\\text{drift}} = \\frac{\\Delta x}{T} = \\frac{2\\pi a}{2\\pi / \\omega} = a \\omega = \\left( \\frac{m E}{q B^2} \\right) \\left( \\frac{q B}{m} \\right) = \\frac{E}{B}$$",
        "tags": ["crossed fields", "cycloid", "drift velocity", "arc length"]
    },
    {
        "id": "3.393",
        "title": "Cutoff Voltage for Cylindrical Diode with Axial Heating Current",
        "difficulty": 3,
        "question": "A system consists of a long cylindrical anode of radius $a$ and a coaxial cylindrical cathode of radius $b$ ($b < a$). A filament located along the axis carries a heating current $I$ producing an azimuthal magnetic field. Find the least potential difference $V$ between cathode and anode at which thermal electrons leaving the cathode without initial velocity start reaching the anode.",
        "hints": [
            "The magnetic field produced by current $I$ is $B_\\theta(r) = \\frac{\\mu_0 I}{2\\pi r}$.",
            "The axial equation of motion is $m \\frac{dv_z}{dt} = e v_r B_\\theta(r) = e \\frac{\\mu_0 I}{2\\pi r} \\frac{dr}{dt}$, which integrates to $m v_z = \\frac{e \\mu_0 I}{2\\pi} \\ln(a/b)$.",
            "At cutoff, the radial velocity at $r = a$ is zero ($v_r = 0$), so all kinetic energy is in axial motion: $e V = \\frac{1}{2} m v_z^2 = \\frac{e^2}{2m} \\left( \\frac{\\mu_0 I}{2\\pi} \\ln\\frac{a}{b} \\right)^2$."
        ],
        "answer": "$V = \\frac{e}{2m} \\left( \\frac{\\mu_0 I}{2\\pi} \\ln\\frac{a}{b} \\right)^2$",
        "solution": "**1. Axial Equation of Motion:**\nThe heating current $I$ along the axis creates a magnetic field:\n$$B_\\theta(r) = \\frac{\\mu_0 I}{2\\pi r}$$\nAs electrons travel radially from cathode $b$ to anode $a$, the Lorentz force deflects them along the $z$-axis:\n$$F_z = e v_r B_\\theta(r) = e \\left( \\frac{dr}{dt} \\right) \\left( \\frac{\\mu_0 I}{2\\pi r} \\right)$$\n$$m \\frac{dv_z}{dt} = \\frac{\\mu_0 e I}{2\\pi r} \\frac{dr}{dt}$$\n\n**2. Axial Velocity at Anode:**\nIntegrating from the cathode ($r = b, v_z = 0$) to the anode ($r = a$):\n$$m v_z = \\frac{\\mu_0 e I}{2\\pi} \\int_b^a \\frac{dr}{r} = \\frac{\\mu_0 e I}{2\\pi} \\ln\\left( \\frac{a}{b} \\right)$$\n$$v_z = \\frac{\\mu_0 e I}{2\\pi m} \\ln\\left( \\frac{a}{b} \\right)$$\n\n**3. Cutoff Condition:**\nElectrons just reach the anode grazing its surface, meaning their radial velocity vanishes at $r = a$ ($v_r = 0$).\nBy energy conservation, the work done by the potential difference $V$ equals the kinetic energy:\n$$e V = \\frac{1}{2} m v_z^2 = \\frac{1}{2} m \\left[ \\frac{\\mu_0 e I}{2\\pi m} \\ln\\left( \\frac{a}{b} \\right) \\right]^2$$\n$$V = \\frac{e}{2m} \\left[ \\frac{\\mu_0 I}{2\\pi} \\ln\\left( \\frac{a}{b} \\right) \\right]^2$$",
        "tags": ["magnetron cutoff", "cylindrical diode", "heating current", "critical potential"]
    },
    {
        "id": "3.394",
        "title": "Hull Cutoff Condition for Cylindrical Magnetron",
        "difficulty": 3,
        "question": "A magnetron consists of a central filament cathode of radius $a$ and a coaxial cylindrical anode of radius $b$ located in a uniform axial magnetic field $B$. An accelerating potential difference $V$ is applied between the filament and the anode. Find the condition on magnetic induction $B$ for which electrons leaving the filament with zero velocity reach the anode.",
        "hints": [
            "In cylindrical coordinates with axial $\\mathbf{B} = B \\hat{\\mathbf{z}}$, the canonical angular momentum gives Busch's theorem: $m r^2 \\dot{\\theta} - \\frac{1}{2} e B r^2 = \\text{const}$.",
            "With $v_\\theta(a) = 0$, the azimuthal velocity at radius $b$ is $v_\\theta = \\frac{e B}{2m} \\frac{b^2 - a^2}{b}$.",
            "For electrons to reach the anode, the total kinetic energy $\\frac{1}{2} m (v_r^2 + v_\\theta^2) = e V$ requires $v_\\theta^2 \\le \\frac{2 e V}{m}$, giving $B \\le \\frac{2 b}{b^2 - a^2} \\sqrt{\\frac{2 m V}{e}}$."
        ],
        "answer": "$B \\le \\frac{2 b}{b^2 - a^2} \\sqrt{\\frac{2 m V}{e}}$",
        "solution": "**1. Busch's Theorem (Angular Momentum Conservation):**\nIn an axisymmetric system with uniform axial magnetic field $\\mathbf{B} = B \\hat{\\mathbf{z}}$, the torque equation is:\n$$\\frac{d}{dt} (m r^2 \\dot{\\theta}) = -e r (v_r B) = -e B r \\frac{dr}{dt} = -\\frac{1}{2} e B \\frac{d}{dt} (r^2)$$\nIntegrating from the filament ($r = a, \\dot{\\theta} = 0$):\n$$m r^2 \\dot{\\theta} = \\frac{1}{2} e B (r^2 - a^2)$$\nAt the anode ($r = b$), the tangential velocity is:\n$$v_\\theta = b \\dot{\\theta} = \\frac{e B}{2m} \\left( \\frac{b^2 - a^2}{b} \\right)$$\n\n**2. Energy Conservation and Cutoff Condition:**\nThe total kinetic energy at the anode is supplied by the potential difference $V$:\n$$\\frac{1}{2} m (v_r^2 + v_\\theta^2) = e V$$\nFor electrons to strike the anode, their radial velocity must be real ($v_r^2 \\ge 0$):\n$$v_\\theta^2 \\le \\frac{2 e V}{m}$$\n$$\\left[ \\frac{e B}{2m} \\left( \\frac{b^2 - a^2}{b} \\right) \\right]^2 \\le \\frac{2 e V}{m}$$\nSolving for $B$:\n$$B \\le \\frac{2 b}{b^2 - a^2} \\sqrt{\\frac{2 m V}{e}}$$\n(This is Hull's celebrated magnetron cutoff criterion).",
        "tags": ["magnetron", "Hull cutoff", "Busch's theorem", "angular momentum"]
    },
    {
        "id": "3.395",
        "title": "Unwinding Spiral Trajectory in Resonant AC Electric and DC Magnetic Fields",
        "difficulty": 3,
        "question": "A charged particle with specific charge $q/m$ starts from rest at the origin $O$ in uniform crossed fields: a constant magnetic field $B$ (along $z$) and a time-varying electric field $E(t) = E_m \\cos(\\omega t)$ (along $y$), where $\\omega = \\frac{q B}{m}$. Find the non-relativistic law of motion $x(t)$ and $y(t)$, and determine the trajectory shape.",
        "hints": [
            "Write the equations of motion: $\\ddot{x} = \\omega \\dot{y}$ and $\\ddot{y} = \\frac{q E_m}{m} \\cos(\\omega t) - \\omega \\dot{x}$.",
            "Integrate $\\dot{x} = \\omega y$. Then $\\ddot{y} + \\omega^2 y = \\frac{q E_m}{m} \\cos(\\omega t)$, which is an undamped harmonic oscillator driven at resonance.",
            "The resonant solution with $y(0) = \\dot{y}(0) = 0$ is $y(t) = \\frac{q E_m}{2 m \\omega} t \\sin(\\omega t)$. Integrate for $x(t)$ to obtain an unwinding spiral."
        ],
        "answer": "$x(t) = a [\\sin(\\omega t) - \\omega t \\cos(\\omega t)], \\quad y(t) = a \\omega t \\sin(\\omega t)$, where $a = \\frac{q E_m}{2 m \\omega^2}$; the trajectory is an unwinding spiral",
        "solution": "**1. Equations of Motion:**\nWith $\\mathbf{E}(t) = E_m \\cos(\\omega t) \\hat{\\mathbf{j}}$ and $\\mathbf{B} = B \\hat{\\mathbf{k}}$ with $\\omega = \\frac{q B}{m}$:\n$$m \\ddot{x} = q B \\dot{y} \\implies \\ddot{x} = \\omega \\dot{y}$$\n$$m \\ddot{y} = q E_m \\cos(\\omega t) - q B \\dot{x} \\implies \\ddot{y} = \\frac{q E_m}{m} \\cos(\\omega t) - \\omega \\dot{x}$$\n\n**2. Resonant Differential Equation:**\nIntegrating the first equation with initial conditions $x(0) = 0, \\dot{x}(0) = 0, y(0) = 0$:\n$$\\dot{x} = \\omega y$$\nSubstituting into the second equation:\n$$\\ddot{y} + \\omega^2 y = \\frac{q E_m}{m} \\cos(\\omega t)$$\nThis represents an oscillator driven at its exact natural frequency $\\omega$ (resonance).\nThe particular solution with zero initial position and velocity is:\n$$y(t) = \\frac{q E_m}{2 m \\omega} t \\sin(\\omega t)$$\n\n**3. Law of Motion along $x$:**\n$$\\dot{x}(t) = \\omega y(t) = \\frac{q E_m}{2 m} t \\sin(\\omega t)$$\nIntegrating by parts with $x(0) = 0$:\n$$x(t) = \\frac{q E_m}{2 m \\omega^2} [\\sin(\\omega t) - \\omega t \\cos(\\omega t)]$$\nDefining $a = \\frac{q E_m}{2 m \\omega^2}$:\n$$x(t) = a [\\sin(\\omega t) - \\omega t \\cos(\\omega t)], \\quad y(t) = a \\omega t \\sin(\\omega t)$$\n\n**4. Trajectory Shape:**\nThe distance from the origin grows linearly with time: $r(t) = \\sqrt{x^2 + y^2} \\approx a \\omega t$. The path forms an **unwinding spiral**.",
        "tags": ["cyclotron resonance", "driven oscillator", "unwinding spiral", "resonant acceleration"]
    },
    {
        "id": "3.396",
        "title": "Effective Accelerating Voltage in Cyclotron",
        "difficulty": 2,
        "question": "The cyclotron oscillator frequency is $\\nu = 10\\text{ MHz}$. Find the effective accelerating voltage applied across the dees of the cyclotron if the distance between neighboring proton trajectories is not less than $\\Delta r = 1.0\\text{ cm}$ at a trajectory radius $r = 0.50\\text{ m}$.",
        "hints": [
            "The orbital speed is related to frequency: $v = 2\\pi \\nu r$.",
            "The kinetic energy at radius $r$ is $T = \\frac{1}{2} m v^2 = 2\\pi^2 m \\nu^2 r^2$.",
            "In one full revolution, the particle crosses the accelerating gap twice, gaining energy $\\Delta T = 2 e V = \\frac{dT}{dr} \\Delta r = 4\\pi^2 m \\nu^2 r \\Delta r$. Solve for $V = \\frac{2\\pi^2 m \\nu^2 r \\Delta r}{e}$."
        ],
        "answer": "$V \\ge \\frac{2\\pi^2 m \\nu^2 r \\Delta r}{e} = 0.10\\text{ MV} = 100\\text{ kV}$",
        "solution": "**1. Kinetic Energy as a Function of Radius:**\nIn a cyclotron, the orbital frequency $\\nu$ is constant in the non-relativistic regime.\nThe velocity of a proton at orbit radius $r$ is:\n$$v = 2\\pi \\nu r$$\nThe kinetic energy is:\n$$T(r) = \\frac{1}{2} m v^2 = 2\\pi^2 m \\nu^2 r^2$$\n\n**2. Energy Gain per Turn:**\nIn each complete turn, the proton passes through the accelerating gap between the dees twice, acquiring energy:\n$$\\Delta T = 2 e V$$\nThe energy increment can also be expressed differentially in terms of the radial separation $\\Delta r$:\n$$\\Delta T = \\frac{dT}{dr} \\Delta r = 4\\pi^2 m \\nu^2 r \\Delta r$$\n\n**3. Accelerating Voltage:**\nEquating the two expressions:\n$$2 e V = 4\\pi^2 m \\nu^2 r \\Delta r \\implies V = \\frac{2\\pi^2 m \\nu^2 r \\Delta r}{e}$$\n\n**4. Numerical Evaluation:**\nGiven $\\nu = 10\\text{ MHz} = 1.0 \\times 10^7\\text{ s}^{-1}$, $r = 0.50\\text{ m}$, $\\Delta r = 0.010\\text{ m}$, $m/e = 1.044 \\times 10^{-8}\\text{ kg/C}$:\n$$V = 2\\pi^2 (1.044 \\times 10^{-8}\\text{ kg/C})(1.0 \\times 10^7\\text{ s}^{-1})^2 (0.50\\text{ m})(0.010\\text{ m})$$\n$$V = 2\\pi^2 (1.044 \\times 10^{-8})(10^{14})(0.0050) = 2\\pi^2 (1.044 \\times 10^6)(0.0050) \\approx 1.03 \\times 10^5\\text{ V} \\approx 0.10\\text{ MV}$$",
        "tags": ["cyclotron", "accelerating voltage", "orbit separation", "dee voltage"]
    },
    {
        "id": "3.397",
        "title": "Cyclotron Energy and Minimum Oscillator Frequency",
        "difficulty": 2,
        "question": "Protons are accelerated in a cyclotron so that the maximum curvature radius of their trajectory is $r = 50\\text{ cm}$. Find:\n(a) the kinetic energy of the protons when acceleration is completed if the magnetic induction is $B = 1.0\\text{ T}$;\n(b) the minimum frequency of the cyclotron oscillator at which the final kinetic energy amounts to $T = 20\\text{ MeV}$.",
        "hints": [
            "Final momentum is $p = q B r$, so non-relativistic kinetic energy is $T = \\frac{p^2}{2m} = \\frac{q^2 B^2 r^2}{2m}$.",
            "The orbital speed corresponding to kinetic energy $T$ is $v = \\sqrt{\\frac{2T}{m}}$.",
            "The cyclotron oscillator frequency must match the orbital frequency: $\\nu = \\frac{v}{2\\pi r} = \\frac{\\sqrt{2T/m}}{2\\pi r}$."
        ],
        "answer": "(a) $T = \\frac{e^2 B^2 r^2}{2m} = 12\\text{ MeV}$; (b) $\\nu_{\\min} = \\frac{\\sqrt{2T/m}}{2\\pi r} = 20\\text{ MHz}$",
        "solution": "**(a) Kinetic Energy:**\nAt the maximum orbital radius $r$, the momentum of the proton is:\n$$p = e B r$$\nThe kinetic energy (non-relativistic since $T \\ll m_0 c^2 \\approx 938\\text{ MeV}$) is:\n$$T = \\frac{p^2}{2m} = \\frac{e^2 B^2 r^2}{2m}$$\nNumerical evaluation with $e = 1.602 \\times 10^{-19}\\text{ C}$, $B = 1.0\\text{ T}$, $r = 0.50\\text{ m}$, $m = 1.673 \\times 10^{-27}\\text{ kg}$:\n$$T = \\frac{(1.602 \\times 10^{-19})^2 (1.0)^2 (0.50)^2}{2(1.673 \\times 10^{-27})} = \\frac{6.416 \\times 10^{-39}}{3.346 \\times 10^{-27}} \\approx 1.917 \\times 10^{-12}\\text{ J}$$\nIn MeV:\n$$T = \\frac{1.917 \\times 10^{-12}\\text{ J}}{1.602 \\times 10^{-13}\\text{ J/MeV}} \\approx 12\\text{ MeV}$$\n\n**(b) Minimum Oscillator Frequency:**\nFor final kinetic energy $T = 20\\text{ MeV} = 3.204 \\times 10^{-12}\\text{ J}$:\n$$v = \\sqrt{\\frac{2T}{m}} = \\sqrt{\\frac{2(3.204 \\times 10^{-12})}{1.673 \\times 10^{-27}}} = \\sqrt{3.83 \\times 10^{15}} \\approx 6.19 \\times 10^7\\text{ m/s}$$\nThe required oscillator frequency is:\n$$\\nu = \\frac{v}{2\\pi r} = \\frac{6.19 \\times 10^7\\text{ m/s}}{2\\pi (0.50\\text{ m})} = \\frac{6.19 \\times 10^7}{\\pi} \\approx 1.97 \\times 10^7\\text{ Hz} \\approx 20\\text{ MHz}$$",
        "tags": ["cyclotron", "maximum kinetic energy", "oscillator frequency", "resonance condition"]
    },
    {
        "id": "3.398",
        "title": "Acceleration Time and Path Length of Helium Ion in Cyclotron",
        "difficulty": 2,
        "question": "Singly charged ions $\\text{He}^+$ are accelerated in a cyclotron so that their maximum orbital radius is $r = 60\\text{ cm}$. The frequency of the cyclotron oscillator is $\\nu = 10.0\\text{ MHz}$, and the effective accelerating voltage across the dees is $V = 50\\text{ kV}$. Neglecting the gap between the dees, find:\n(a) the total time of acceleration of the ion;\n(b) the approximate distance covered by the ion in the process of its acceleration.",
        "hints": [
            "The final kinetic energy of the ion is $T = \\frac{1}{2} m v^2 = 2\\pi^2 m \\nu^2 r^2$.",
            "The number of accelerating gap crossings is $N = \\frac{T}{e V}$, so total revolutions is $n = N/2$. The acceleration time is $t = \\frac{n}{\\nu} = \\frac{\\pi^2 m \\nu r^2}{e V}$.",
            "The path length is $s = \\sum_{k=1}^n 2\\pi r_k \\approx \\int_0^n 2\\pi r(n') \\, dn'$. Since $r \\propto \\sqrt{n'}$, $s \\approx \\frac{4}{3} \\pi r n = \\frac{4}{3} \\frac{\\pi^3 m \\nu^2 r^3}{e V} \\approx 0.74\\text{ km}$."
        ],
        "answer": "(a) $t = \\frac{\\pi^2 m \\nu r^2}{e V} = 17\\,\\mu\\text{s}$; (b) $s \\approx \\frac{4}{3} \\frac{\\pi^3 m \\nu^2 r^3}{e V} = 0.74\\text{ km}$",
        "solution": "**1. Final Energy and Number of Revolutions:**\nFor a helium ion $\\text{He}^+$ of mass $m \\approx 4 \\times 1.673 \\times 10^{-27}\\text{ kg} = 6.69 \\times 10^{-27}\\text{ kg}$ and charge $e$, the final velocity at radius $r$ is $v = 2\\pi \\nu r$.\nThe final kinetic energy is:\n$$T = \\frac{1}{2} m (2\\pi \\nu r)^2 = 2\\pi^2 m \\nu^2 r^2$$\nIn each revolution, the ion crosses the accelerating gap twice, gaining energy $2 e V$.\nThe total number of revolutions to reach radius $r$ is:\n$$n = \\frac{T}{2 e V} = \\frac{\\pi^2 m \\nu^2 r^2}{e V}$$\n\n**(a) Total Acceleration Time:**\nSince each revolution takes a period $\\tau = \\frac{1}{\\nu}$, the total acceleration time is:\n$$t = n \\tau = \\frac{n}{\\nu} = \\frac{\\pi^2 m \\nu r^2}{e V}$$\nEvaluating numerically with $\\nu = 1.0 \\times 10^7\\text{ Hz}$, $r = 0.60\\text{ m}$, $V = 5.0 \\times 10^4\\text{ V}$:\n$$t = \\frac{\\pi^2 (6.69 \\times 10^{-27}\\text{ kg})(1.0 \\times 10^7\\text{ s}^{-1})(0.60\\text{ m})^2}{(1.602 \\times 10^{-19}\\text{ C})(5.0 \\times 10^4\\text{ V})} = \\frac{2.378 \\times 10^{-19}}{8.01 \\times 10^{-15}} \\approx 1.73 \\times 10^{-5}\\text{ s} = 17\\,\\mu\\text{s}$$\n\n**(b) Distance Covered:**\nThe radius at the $k$-th turn scales as $r_k = r \\sqrt{\\frac{k}{n}}$.\nThe total distance covered is the sum of circumferences:\n$$s = \\sum_{k=1}^n 2\\pi r_k \\approx 2\\pi r \\int_0^n \\sqrt{\\frac{k}{n}} \\, dk = 2\\pi r \\left[ \\frac{2}{3} \\frac{k^{3/2}}{\\sqrt{n}} \\right]_0^n = \\frac{4}{3} \\pi r n$$\nSubstituting $n = \\frac{\\pi^2 m \\nu^2 r^2}{e V}$:\n$$s = \\frac{4}{3} \\frac{\\pi^3 m \\nu^2 r^3}{e V}$$\nEvaluating numerically:\n$$s = \\frac{4}{3} \\pi (0.60\\text{ m}) n$$\nWith $n = \\nu t = (10^7\\text{ s}^{-1})(1.73 \\times 10^{-5}\\text{ s}) \\approx 173$ revolutions:\n$$s = \\frac{4}{3} \\pi (0.60)(173) \\approx 2.513 \\times 295.2 \\approx 742\\text{ m} \\approx 0.74\\text{ km}$$",
        "tags": ["cyclotron", "total acceleration time", "distance covered", "helium ion"]
    }
]
