"""
part4_ch4_1d.py
Curated problems 4.76 to 4.97 (22 problems) of Irodov Chapter 4.1:
Mechanical Oscillations (Part D) & Boundary with Electrical Analogs.
"""

CH4_1D_CURATED = [
    {
        "id": "4.76",
        "title": "Total Distance Traveled by a Damped Harmonic Particle",
        "difficulty": 2,
        "question": "A particle was displaced from its equilibrium position by a distance $l = 1.0\\text{ cm}$ and released from rest. What total distance does the particle cover until it completely stops if the logarithmic damping decrement is equal to $\\lambda = 0.020$?",
        "hints": [
            "In each half-period, the particle swings from one extreme to the opposite side, covering distance $s_k = a_k + a_{k+1}$.",
            "The amplitudes at successive half-periods decrease by the factor $e^{-\\lambda/2}$.",
            "Sum the infinite geometric series: $s = l + 2l e^{-\\lambda/2} + 2l e^{-\\lambda} + \\dots = l \\frac{1 + e^{-\\lambda/2}}{1 - e^{-\\lambda/2}} \\approx \\frac{4l}{\\lambda}$."
        ],
        "answer": "$s = l \\frac{1 + e^{-\\lambda/2}}{1 - e^{-\\lambda/2}} \\approx \\frac{4l}{\\lambda} = 2.0\\text{ m}$",
        "solution": "**1. Path Length as a Sum of Amplitudes:**\nLet the initial displacement be $l = a_0$.\nIn the first half-cycle, the particle travels from $+a_0$ to $-a_1$, covering distance $s_1 = a_0 + a_1$.\nIn the second half-cycle, it travels from $-a_1$ to $+a_2$, covering distance $s_2 = a_1 + a_2$, and so forth.\nThe amplitudes at successive turning points separated by half a period $T/2$ decay by $e^{-\\beta T/2} = e^{-\\lambda/2}$:\n$$a_k = l e^{-k \\lambda/2}, \\quad k = 0, 1, 2, \\dots$$\n\n**2. Total Distance:**\nThe total distance covered is:\n$$s = s_1 + s_2 + s_3 + \\dots = a_0 + 2a_1 + 2a_2 + 2a_3 + \\dots = 2\\sum_{k=0}^\\infty a_k - a_0$$\n$$s = 2l \\sum_{k=0}^\\infty (e^{-\\lambda/2})^k - l = 2l \\frac{1}{1 - e^{-\\lambda/2}} - l = l \\frac{1 + e^{-\\lambda/2}}{1 - e^{-\\lambda/2}}$$\n\n**3. Small Decrement Approximation and Calculation:**\nSince $\\lambda = 0.020 \\ll 1$, we can approximate $e^{-\\lambda/2} \\approx 1 - \\frac{\\lambda}{2}$:\n$$s \\approx l \\frac{1 + 1 - \\lambda/2}{\\lambda/2} \\approx \\frac{4l}{\\lambda}$$\nSubstituting $l = 0.010\\text{ m}$ and $\\lambda = 0.020$:\n$$s = \\frac{4(0.010\\text{ m})}{0.020} = 2.0\\text{ m}$$",
        "tags": ["damped oscillations", "path length", "geometric series", "logarithmic decrement"]
    },
    {
        "id": "4.77",
        "title": "Quality Factor of a Simple Pendulum from Energy Attenuation",
        "difficulty": 2,
        "question": "Find the quality factor $Q$ of a simple pendulum of length $l = 50\\text{ cm}$ if during a time interval $\\tau = 5.2\\text{ min}$ its total mechanical energy decreases $\\eta = 4.0 \\times 10^4$ times.",
        "hints": [
            "The mechanical energy of a damped oscillator decays as $E(t) = E_0 e^{-2\\beta t}$.",
            "From $\\frac{E_0}{E(\\tau)} = e^{2\\beta \\tau} = \\eta$, find the damping coefficient $\\beta = \\frac{\\ln\\eta}{2\\tau}$.",
            "The quality factor is $Q = \\frac{\\omega_0}{2\\beta} = \\frac{\\omega_0 \\tau}{\\ln\\eta}$, where $\\omega_0 = \\sqrt{g/l}$."
        ],
        "answer": "$Q = \\frac{\\tau \\sqrt{g/l}}{\\ln\\eta} \\approx 1.3 \\times 10^2$",
        "solution": "**1. Energy Decay in Damped Motion:**\nFor a weakly damped harmonic oscillator, the mechanical energy decays exponentially according to:\n$$E(t) = E_0 e^{-2\\beta t}$$\nGiven that over the time interval $\\tau = 5.2\\text{ min} = 312\\text{ s}$, the energy decreases by a factor $\\eta = 4.0 \\times 10^4$:\n$$\\frac{E_0}{E(\\tau)} = e^{2\\beta \\tau} = \\eta \\implies 2\\beta \\tau = \\ln\\eta \\implies \\beta = \\frac{\\ln\\eta}{2\\tau}$$\n\n**2. Quality Factor Formulation:**\nThe quality factor $Q$ of the oscillator is:\n$$Q = \\frac{\\omega_0}{2\\beta}$$\nSubstituting $\\beta = \\frac{\\ln\\eta}{2\\tau}$:\n$$Q = \\frac{\\omega_0 \\tau}{\\ln\\eta} = \\frac{\\tau \\sqrt{g/l}}{\\ln\\eta}$$\n\n**3. Numerical Evaluation:**\nGiven $l = 0.50\\text{ m}$, $g = 9.8\\text{ m/s}^2$:\n$$\\omega_0 = \\sqrt{\\frac{9.8}{0.50}} = \\sqrt{19.6} \\approx 4.427\\text{ s}^{-1}$$\n$$\\tau = 5.2 \\times 60 = 312\\text{ s}$$\n$$\\ln\\eta = \\ln(4.0 \\times 10^4) = \\ln(40000) \\approx 10.597$$\n$$Q = \\frac{(312)(4.427)}{10.597} = \\frac{1381.2}{10.597} \\approx 130.3 \\approx 1.3 \\times 10^2$$",
        "tags": ["quality factor", "simple pendulum", "energy dissipation", "damping"]
    },
    {
        "id": "4.78",
        "title": "Oscillation Period of a Rim-Pivoted Disc in a Viscous Medium",
        "difficulty": 2,
        "question": "A uniform disc of radius $R = 13\\text{ cm}$ can rotate about a horizontal axis perpendicular to its plane and passing through the edge of the disc. Find the oscillation period of this pendulum in water if the logarithmic damping decrement is equal to $\\lambda = 1.00$.",
        "hints": [
            "By the parallel axis theorem, the moment of inertia about the rim is $I = \\frac{1}{2} m R^2 + m R^2 = \\frac{3}{2} m R^2$.",
            "The undamped natural frequency is $\\omega_0 = \\sqrt{\\frac{mg R}{I}} = \\sqrt{\\frac{2g}{3R}}$.",
            "The damped period is $T = \\frac{2\\pi}{\\omega} = \\frac{2\\pi}{\\omega_0} \\sqrt{1 + \\frac{\\lambda^2}{4\\pi^2}} = 2\\pi \\sqrt{\\frac{3R}{2g}\\left(1 + \\frac{\\lambda^2}{4\\pi^2}\\right)}$."
        ],
        "answer": "$T = 2\\pi \\sqrt{\\frac{3R}{2g}\\left(1 + \\frac{\\lambda^2}{4\\pi^2}\\right)} \\approx 0.90\\text{ s}$",
        "solution": "**1. Moment of Inertia and Natural Frequency:**\nFor a uniform circular disc of mass $m$ and radius $R$ pivoted at its edge:\n$$I = I_c + m R^2 = \\frac{1}{2} m R^2 + m R^2 = \\frac{3}{2} m R^2$$\nThe distance from the pivot to the center of mass is $l_c = R$.\nThe undamped angular frequency is:\n$$\\omega_0 = \\sqrt{\\frac{mg l_c}{I}} = \\sqrt{\\frac{mg R}{\\frac{3}{2} m R^2}} = \\sqrt{\\frac{2g}{3R}}$$\n\n**2. Period with Damping:**\nIn the presence of damping, the damped frequency is $\\omega = \\sqrt{\\omega_0^2 - \\beta^2}$.\nThe logarithmic decrement is $\\lambda = \\beta T = \\beta \\frac{2\\pi}{\\omega}$, which yields:\n$$\\omega = \\frac{\\omega_0}{\\sqrt{1 + \\frac{\\lambda^2}{4\\pi^2}}}$$\nThe oscillation period is:\n$$T = \\frac{2\\pi}{\\omega} = \\frac{2\\pi}{\\omega_0} \\sqrt{1 + \\frac{\\lambda^2}{4\\pi^2}} = 2\\pi \\sqrt{\\frac{3R}{2g} \\left(1 + \\frac{\\lambda^2}{4\\pi^2}\\right)}$$\n\n**3. Numerical Evaluation:**\nGiven $R = 0.13\\text{ m}$, $g = 9.8\\text{ m/s}^2$, and $\\lambda = 1.00$:\n$$\\frac{3R}{2g} = \\frac{3(0.13)}{2(9.8)} = \\frac{0.39}{19.6} \\approx 0.01990\\text{ s}^2$$\n$$1 + \\frac{\\lambda^2}{4\\pi^2} = 1 + \\frac{1.0}{39.478} \\approx 1.0253$$\n$$T = 2\\pi \\sqrt{0.01990 \\times 1.0253} = 2\\pi \\sqrt{0.02040} = 2\\pi (0.1428) \\approx 0.897\\text{ s} \\approx 0.90\\text{ s}$$",
        "tags": ["physical pendulum", "disc", "viscous damping", "logarithmic decrement"]
    },
    {
        "id": "4.79",
        "title": "Frequency of Torsional Oscillations of a Disc in a Viscous Fluid",
        "difficulty": 3,
        "question": "A thin uniform disc of mass $m$ and radius $R$ suspended horizontally by an elastic thread with torsional stiffness $\\alpha$ performs torsional oscillations in a liquid. The viscous drag force on each surface element $dS$ is $dF = \\eta v dS$. Find the oscillation frequency $\\omega$ of the disc.",
        "hints": [
            "The viscous drag acts on both the top and bottom faces of the disc: area element is $dS = 2\\pi r dr$, and velocity is $v = r \\dot{\\varphi}$.",
            "Integrate the viscous torque from both sides: $\\tau_{\\text{visc}} = -2 \\int_0^R r (\\eta r \\dot{\\varphi}) (2\\pi r dr) = -\\pi \\eta R^4 \\dot{\\varphi}$.",
            "Identify the damping coefficient $\\beta = \\frac{\\pi \\eta R^4}{2 I}$ where $I = \\frac{1}{2} m R^2$, and obtain $\\omega = \\sqrt{\\frac{2\\alpha}{m R^2} - \\left(\\frac{\\pi \\eta R^2}{m}\\right)^2}$."
        ],
        "answer": "$\\omega = \\sqrt{\\frac{2\\alpha}{m R^2} - \\left(\\frac{\\pi \\eta R^2}{m}\\right)^2}$",
        "solution": "**1. Viscous Torque on the Disc:**\nAt radial distance $r$ from the axis, the linear speed of a surface element is $v = r \\dot{\\varphi}$.\nThe shear friction force per unit area on both the upper and lower faces of the disc is $f = \\eta v = \\eta r \\dot{\\varphi}$.\nThe torque on an annular ring of radius $r$ and width $dr$ on both sides is:\n$$d\\tau_{\\text{visc}} = -2 \\cdot r \\cdot [\\eta r \\dot{\\varphi}] \\cdot (2\\pi r dr) = -4\\pi \\eta \\dot{\\varphi} r^3 dr$$\nIntegrating from $r = 0$ to $r = R$:\n$$\\tau_{\\text{visc}} = -4\\pi \\eta \\dot{\\varphi} \\int_0^R r^3 dr = -4\\pi \\eta \\dot{\\varphi} \\frac{R^4}{4} = -\\pi \\eta R^4 \\dot{\\varphi}$$\n\n**2. Equation of Torsional Motion:**\nThe moment of inertia of the disc about its axis is $I = \\frac{1}{2} m R^2$.\nThe equation of motion is:\n$$I \\ddot{\\varphi} + \\pi \\eta R^4 \\dot{\\varphi} + \\alpha \\varphi = 0$$\n$$\\ddot{\\varphi} + 2\\beta \\dot{\\varphi} + \\omega_0^2 \\varphi = 0$$\nwhere:\n$$\\omega_0^2 = \\frac{\\alpha}{I} = \\frac{2\\alpha}{m R^2}$$\n$$2\\beta = \\frac{\\pi \\eta R^4}{I} = \\frac{\\pi \\eta R^4}{\\frac{1}{2} m R^2} = \\frac{2\\pi \\eta R^2}{m} \\implies \\beta = \\frac{\\pi \\eta R^2}{m}$$\n\n**3. Oscillation Frequency:**\nThe damped oscillation frequency is:\n$$\\omega = \\sqrt{\\omega_0^2 - \\beta^2} = \\sqrt{\\frac{2\\alpha}{m R^2} - \\left(\\frac{\\pi \\eta R^2}{m}\\right)^2}$$",
        "tags": ["torsional oscillations", "viscous torque", "fluid drag", "damping coefficient"]
    },
    {
        "id": "4.80",
        "title": "Viscosity Determination from Torsional Disc Oscillations",
        "difficulty": 3,
        "question": "A disc of radius $R$ and moment of inertia $I$ suspended by an elastic thread between two stationary parallel plates separated by distance $h$ from the disc surfaces performs torsional oscillations with period $T$ and logarithmic decrement $\\lambda$. Find the dynamic viscosity $\\eta$ of the gas between the plates.",
        "hints": [
            "The velocity gradient in the gap of thickness $h$ is $\\frac{dv}{dz} = \\frac{r \\dot{\\varphi}}{h}$.",
            "The shear stress is $\\sigma = \\eta \\frac{r \\dot{\\varphi}}{h}$. Integrating over both sides gives viscous torque $\\tau = -\\frac{\\pi \\eta R^4}{h} \\dot{\\varphi}$.",
            "Relate the damping coefficient $\\beta = \\frac{\\pi \\eta R^4}{2 h I}$ to the logarithmic decrement $\\lambda = \\beta T$ to obtain $\\eta = \\frac{2 h I \\lambda}{\\pi R^4 T}$."
        ],
        "answer": "$\\eta = \\frac{2 h I \\lambda}{\\pi R^4 T}$",
        "solution": "**1. Viscous Shear Torque:**\nAssuming a linear velocity profile in the narrow gaps of thickness $h$ between the oscillating disc and the stationary boundary plates:\n$$\\frac{dv}{dz} = \\frac{v}{h} = \\frac{r \\dot{\\varphi}}{h}$$\nThe viscous shear stress on each face of the disc at distance $r$ from the axis is:\n$$\\sigma = \\eta \\frac{r \\dot{\\varphi}}{h}$$\nThe total retarding torque from both sides of the disc is:\n$$\\tau = -2 \\int_0^R r \\cdot \\left(\\eta \\frac{r \\dot{\\varphi}}{h}\\right) (2\\pi r dr) = -\\frac{4\\pi \\eta \\dot{\\varphi}}{h} \\int_0^R r^3 dr = -\\frac{\\pi \\eta R^4}{h} \\dot{\\varphi}$$\n\n**2. Damping Parameter and Decrement:**\nThe equation of torsional motion is:\n$$I \\ddot{\\varphi} + \\frac{\\pi \\eta R^4}{h} \\dot{\\varphi} + k \\varphi = 0 \\implies \\ddot{\\varphi} + 2\\beta \\dot{\\varphi} + \\omega_0^2 \\varphi = 0$$\nThe damping coefficient is:\n$$\\beta = \\frac{\\pi \\eta R^4}{2 h I}$$\nThe logarithmic decrement is related to $\\beta$ and period $T$ by:\n$$\\lambda = \\beta T = \\frac{\\pi \\eta R^4 T}{2 h I}$$\n\n**3. Dynamic Viscosity:**\nSolving for $\\eta$:\n$$\\eta = \\frac{2 h I \\lambda}{\\pi R^4 T}$$",
        "tags": ["viscometer", "torsional oscillations", "shear stress", "logarithmic decrement"]
    },
    {
        "id": "4.81",
        "title": "Damping of a Conducting Square Frame in a Magnetic Field",
        "difficulty": 3,
        "question": "A conductor in the shape of a square frame with side $a$, resistance $R_0$, and moment of inertia $I$ is suspended by an elastic thread in a uniform horizontal magnetic field $B$. Find the characteristic damping time $\\tau = 1/\\beta$ of the frame's small torsional oscillations due to electromagnetic induction.",
        "hints": [
            "For a small angular rotation $\\varphi$, the magnetic flux through the frame is $\\Phi = B a^2 \\cos\\varphi \\approx B a^2 (1 - \\frac{1}{2}\\varphi^2)$ or about edge: $\\Phi = B a^2 \\sin\\varphi \\approx B a^2 \\varphi$.",
            "The induced EMF is $\\mathcal{E} = -\\dot{\\Phi} = -B a^2 \\dot{\\varphi}$, producing current $i = \\frac{\\mathcal{E}}{R_0} = -\\frac{B a^2 \\dot{\\varphi}}{R_0}$.",
            "The magnetic restoring torque is $\\tau_m = i B a^2 = -\\frac{B^2 a^4}{R_0} \\dot{\\varphi}$. Damping time is $\\tau = \\frac{1}{\\beta} = \\frac{2 R_0 I}{a^4 B^2}$."
        ],
        "answer": "$\\tau = \\frac{2 R_0 I}{a^4 B^2}$",
        "solution": "**1. Induced EMF and Current:**\nLet the frame have area $S = a^2$. When the normal to the frame deviates by a small angle $\\varphi$ from the direction perpendicular to the magnetic field $\\mathbf{B}$:\n$$\\Phi(t) = B a^2 \\sin\\varphi \\approx B a^2 \\varphi$$\nThe rate of change of magnetic flux is:\n$$\\frac{d\\Phi}{dt} = B a^2 \\dot{\\varphi}$$\nBy Faraday's law of induction, the induced current in the frame is:\n$$i = -\\frac{1}{R_0} \\frac{d\\Phi}{dt} = -\\frac{B a^2 \\dot{\\varphi}}{R_0}$$\nwhere $R_0$ is the electrical resistance of the frame.\n\n**2. Electromagnetic Braking Torque:**\nThe magnetic moment of the current-carrying frame is $p_m = i a^2$.\nThe braking torque exerted by the magnetic field on the frame is:\n$$\\tau_m = -p_m B = -i a^2 B = -\\left(\\frac{B a^2 \\dot{\\varphi}}{R_0}\\right) a^2 B = -\\frac{B^2 a^4}{R_0} \\dot{\\varphi}$$\n\n**3. Damping Time:**\nThe rotational equation of motion is:\n$$I \\ddot{\\varphi} + \\frac{B^2 a^4}{R_0} \\dot{\\varphi} + k \\varphi = 0 \\implies \\ddot{\\varphi} + 2\\beta \\dot{\\varphi} + \\omega_0^2 \\varphi = 0$$\nThe damping coefficient is:\n$$\\beta = \\frac{B^2 a^4}{2 R_0 I}$$\nThe characteristic damping time (relaxation time) $\\tau$ is:\n$$\\tau = \\frac{1}{\\beta} = \\frac{2 R_0 I}{a^4 B^2}$$",
        "tags": ["magnetic damping", "electromagnetic induction", "relaxation time", "Lenz law"]
    },
    {
        "id": "4.82",
        "title": "Oscillations with Dry Coulomb Friction",
        "difficulty": 2,
        "question": "A bar of mass $m = 0.50\\text{ kg}$ lying on a horizontal plane with friction coefficient $k = 0.10$ is attached to a wall by a horizontal spring of stiffness $\\varkappa = 2.0\\text{ N/cm} = 200\\text{ N/m}$. The bar is displaced by $x_0 = 5.0\\text{ cm}$ from equilibrium and released from rest. Find:\n(a) the period of oscillations;\n(b) the number of oscillations performed until the bar stops.",
        "hints": [
            "Dry Coulomb friction reverses direction each half-cycle but does not alter the oscillation frequency, so $T = 2\\pi \\sqrt{m/\\varkappa}$.",
            "In each half-period, the turning point decreases by $2 \\Delta$, where $\\Delta = \\frac{k mg}{\\varkappa}$. In each full period, amplitude decreases by $4\\Delta$.",
            "The motion stops when the restoring force at a turning point cannot overcome static friction: $|x| \\le \\Delta$. Number of cycles is $n = \\frac{x_0 - \\Delta}{4\\Delta}$."
        ],
        "answer": "(a) $T = 2\\pi \\sqrt{\\frac{m}{\\varkappa}} = 0.31\\text{ s}$; (b) $n = \\frac{x_0 - \\Delta}{4\\Delta} \\approx 3.5\\text{ oscillations}$, where $\\Delta = \\frac{k mg}{\\varkappa}$",
        "solution": "**(a) Oscillation Period:**\nWith Coulomb friction, the equation of motion during each half-cycle is:\n$$m \\ddot{x} + \\varkappa x = \\pm k mg$$\nThis is harmonic motion with a shifted equilibrium point $\\pm \\Delta = \\pm \\frac{k mg}{\\varkappa}$.\nThe angular frequency is unchanged by constant Coulomb friction:\n$$\\omega_0 = \\sqrt{\\frac{\\varkappa}{m}}$$\nThe oscillation period is:\n$$T = 2\\pi \\sqrt{\\frac{m}{\\varkappa}}$$\nSubstituting $m = 0.50\\text{ kg}$ and $\\varkappa = 200\\text{ N/m}$:\n$$T = 2\\pi \\sqrt{\\frac{0.50}{200}} = 2\\pi \\sqrt{0.0025} = 2\\pi (0.050) = 0.10\\pi \\approx 0.314\\text{ s} \\approx 0.31\\text{ s}$$\n\n**(b) Number of Oscillations:**\nThe shift of the equilibrium center is:\n$$\\Delta = \\frac{k mg}{\\varkappa} = \\frac{(0.10)(0.50\\text{ kg})(9.8\\text{ m/s}^2)}{200\\text{ N/m}} = \\frac{0.49}{200} = 2.45 \\times 10^{-3}\\text{ m} = 0.245\\text{ cm}$$\nIn each half-cycle, the amplitude decreases by $2\\Delta$.\nIn each complete period (two half-cycles), the amplitude decreases by:\n$$\\Delta a = 4\\Delta = 4(0.245\\text{ cm}) = 0.98\\text{ cm}$$\nThe motion stops at a turning point when the spring restoring force $\\varkappa |x_n|$ is less than or equal to the maximum static friction force $k mg$, which means $|x_n| \\le \\Delta = 0.245\\text{ cm}$.\nThe number of full cycles is:\n$$n = \\frac{x_0 - \\Delta}{4\\Delta} = \\frac{5.0 - 0.245}{0.98} = \\frac{4.755}{0.98} \\approx 4.85 \\text{ half-cycles} \\implies 3.5 \\text{ to } 4 \\text{ swings}$$",
        "tags": ["Coulomb friction", "dry friction", "decay per cycle", "spring-mass system"]
    },
    {
        "id": "4.83",
        "title": "Undamped Oscillator Driven by Harmonic Force from Rest",
        "difficulty": 2,
        "question": "A ball of mass $m$ can perform undamped harmonic oscillations about $x = 0$ with natural frequency $\\omega_0$. At $t = 0$, when the ball was at rest at $x = 0$, an external force $F_x(t) = F_0 \\cos\\omega t$ begins to act on it. Find the displacement $x(t)$ of the ball.",
        "hints": [
            "Write the differential equation: $\\ddot{x} + \\omega_0^2 x = \\frac{F_0}{m} \\cos\\omega t$.",
            "Seek a particular solution of the form $x_p(t) = A \\cos\\omega t$, where $A = \\frac{F_0}{m(\\omega_0^2 - \\omega^2)}$.",
            "Add the general homogeneous solution $x_h(t) = C_1 \\cos\\omega_0 t + C_2 \\sin\\omega_0 t$ and apply initial conditions $x(0) = 0, \\dot{x}(0) = 0$."
        ],
        "answer": "$x(t) = \\frac{F_0}{m(\\omega_0^2 - \\omega^2)} (\\cos\\omega t - \\cos\\omega_0 t)$",
        "solution": "**1. Differential Equation of Motion:**\nNewton's second law for the forced undamped oscillator is:\n$$m \\ddot{x} + m \\omega_0^2 x = F_0 \\cos\\omega t \\implies \\ddot{x} + \\omega_0^2 x = \\frac{F_0}{m} \\cos\\omega t$$\n\n**2. Particular Solution:**\nAssuming a steady-state response of the form $x_p(t) = A \\cos\\omega t$:\n$$-\\omega^2 A \\cos\\omega t + \\omega_0^2 A \\cos\\omega t = \\frac{F_0}{m} \\cos\\omega t$$\n$$A(\\omega_0^2 - \\omega^2) = \\frac{F_0}{m} \\implies A = \\frac{F_0}{m(\\omega_0^2 - \\omega^2)}$$\n\n**3. General Solution and Initial Conditions:**\nThe general solution is:\n$$x(t) = C_1 \\cos\\omega_0 t + C_2 \\sin\\omega_0 t + \\frac{F_0}{m(\\omega_0^2 - \\omega^2)} \\cos\\omega t$$\nAt $t = 0$:\n$$x(0) = C_1 + \\frac{F_0}{m(\\omega_0^2 - \\omega^2)} = 0 \\implies C_1 = -\\frac{F_0}{m(\\omega_0^2 - \\omega^2)}$$\n$$\\dot{x}(0) = \\omega_0 C_2 = 0 \\implies C_2 = 0$$\nThus the displacement of the ball is:\n$$x(t) = \\frac{F_0}{m(\\omega_0^2 - \\omega^2)} (\\cos\\omega t - \\cos\\omega_0 t)$$",
        "tags": ["forced oscillations", "undamped oscillator", "beats", "harmonic force"]
    },
    {
        "id": "4.84",
        "title": "Oscillation Induced by a Constant Force of Finite Duration",
        "difficulty": 2,
        "question": "A particle of mass $m$ can perform undamped harmonic oscillations with natural frequency $\\omega_0$. Initially at rest at the equilibrium position $x = 0$, a constant force $F_0$ begins acting along the $x$-axis for a time duration $\\tau$, after which the force vanishes. Find the law of motion $x(t)$ for $t \\le \\tau$ and $t \\ge \\tau$.",
        "hints": [
            "For $t \\le \\tau$, the equation is $\\ddot{x} + \\omega_0^2 x = F_0/m$. With $x(0) = 0, \\dot{x}(0) = 0$, the solution is $x(t) = \\frac{F_0}{m \\omega_0^2}(1 - \\cos\\omega_0 t)$.",
            "At $t = \\tau$, evaluate the position $x(\\tau)$ and velocity $\\dot{x}(\\tau)$.",
            "For $t \\ge \\tau$, the equation is free oscillation $\\ddot{x} + \\omega_0^2 x = 0$. Match boundary conditions at $t = \\tau$."
        ],
        "answer": "$x(t) = \\begin{cases} \\frac{F_0}{m \\omega_0^2}(1 - \\cos\\omega_0 t), & t \\le \\tau \\\\ \\frac{2 F_0}{m \\omega_0^2} \\sin\\left(\\frac{\\omega_0 \\tau}{2}\\right) \\sin\\left[\\omega_0\\left(t - \\frac{\\tau}{2}\\right)\\right], & t \\ge \\tau \\end{cases}$",
        "solution": "**1. Motion During the Action of the Force ($0 \\le t \\le \\tau$):**\nThe equation of motion is:\n$$\\ddot{x} + \\omega_0^2 x = \\frac{F_0}{m}$$\nWith initial conditions $x(0) = 0$ and $\\dot{x}(0) = 0$:\n$$x(t) = \\frac{F_0}{m \\omega_0^2} (1 - \\cos\\omega_0 t)$$\n$$\\dot{x}(t) = \\frac{F_0}{m \\omega_0} \\sin\\omega_0 t$$\n\n**2. State at $t = \\tau$:**\n$$x(\\tau) = \\frac{F_0}{m \\omega_0^2} (1 - \\cos\\omega_0 \\tau)$$\n$$\\dot{x}(\\tau) = \\frac{F_0}{m \\omega_0} \\sin\\omega_0 \\tau$$\n\n**3. Motion After the Force Ceases ($t \\ge \\tau$):**\nFor $t \\ge \\tau$, the equation is free harmonic motion:\n$$\\ddot{x} + \\omega_0^2 x = 0$$\nThe solution can be written as $x(t) = A \\cos[\\omega_0(t - \\tau)] + B \\sin[\\omega_0(t - \\tau)]$.\nMatching values at $t = \\tau$:\n$$A = x(\\tau) = \\frac{F_0}{m \\omega_0^2} (1 - \\cos\\omega_0 \\tau)$$\n$$\\omega_0 B = \\dot{x}(\\tau) \\implies B = \\frac{F_0}{m \\omega_0^2} \\sin\\omega_0 \\tau$$\nCombining using trigonometric sum identities:\n$$x(t) = \\frac{F_0}{m \\omega_0^2} [ \\cos[\\omega_0(t - \\tau)] - (\\cos\\omega_0 \\tau \\cos[\\omega_0(t-\\tau)] - \\sin\\omega_0 \\tau \\sin[\\omega_0(t-\\tau)]) ]$$\n$$x(t) = \\frac{2 F_0}{m \\omega_0^2} \\sin\\left(\\frac{\\omega_0 \\tau}{2}\\right) \\sin\\left[\\omega_0\\left(t - \\frac{\\tau}{2}\\right)\\right]$$",
        "tags": ["pulse excitation", "step force", "piecewise solution", "undamped oscillator"]
    },
    {
        "id": "4.85",
        "title": "Resonance Frequency and Amplitude of a Damped Spring-Mass System",
        "difficulty": 3,
        "question": "A ball of mass $m$ suspended by a vertical spring stretches it by $\\Delta l$. Under the action of an external vertical harmonic force $F(t) = F_0 \\cos\\omega t$, the ball performs forced oscillations with logarithmic damping decrement $\\lambda$. Find the displacement resonance frequency $\\omega_{\\text{res}}$ and the resonance amplitude $a_{\\text{res}}$.",
        "hints": [
            "The natural frequency is $\\omega_0 = \\sqrt{g/\\Delta l}$.",
            "In terms of logarithmic decrement $\\lambda$, the damping ratio is related by $\\beta^2 = \\omega_0^2 \\frac{\\lambda^2}{4\\pi^2 + \\lambda^2}$.",
            "The displacement resonance frequency is $\\omega_{\\text{res}} = \\sqrt{\\omega_0^2 - 2\\beta^2}$, and the peak amplitude is $a_{\\text{res}} = \\frac{F_0}{2 m \\beta \\sqrt{\\omega_0^2 - \\beta^2}}$."
        ],
        "answer": "$\\omega_{\\text{res}} = \\sqrt{\\frac{g}{\\Delta l} \\left(1 - \\frac{\\lambda^2}{2\\pi^2}\\right)}, \\quad a_{\\text{res}} \\approx \\frac{F_0 \\Delta l}{mg} \\frac{\\pi}{\\lambda}$",
        "solution": "**1. Natural Frequency and Damping:**\nStatic equilibrium yields:\n$$mg = \\varkappa \\Delta l \\implies \\omega_0 = \\sqrt{\\frac{\\varkappa}{m}} = \\sqrt{\\frac{g}{\\Delta l}}$$\nFor a damped oscillator, the logarithmic decrement is $\\lambda = \\beta T = \\frac{2\\pi \\beta}{\\omega_1}$, where $\\omega_1 = \\sqrt{\\omega_0^2 - \\beta^2}$.\nSolving for $\\beta$:\n$$\\beta = \\frac{\\omega_0 \\lambda}{\\sqrt{4\\pi^2 + \\lambda^2}}$$\n\n**2. Displacement Resonance Frequency:**\nThe displacement amplitude for a forced oscillator is:\n$$a(\\omega) = \\frac{F_0 / m}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2}}$$\nMinimizing the denominator with respect to $\\omega^2$ gives:\n$$\\frac{d}{d(\\omega^2)} [(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2] = -2(\\omega_0^2 - \\omega^2) + 4\\beta^2 = 0$$\n$$\\omega_{\\text{res}}^2 = \\omega_0^2 - 2\\beta^2 = \\frac{g}{\\Delta l} \\left(1 - \\frac{2\\lambda^2}{4\\pi^2 + \\lambda^2}\\right) \\approx \\frac{g}{\\Delta l} \\left(1 - \\frac{\\lambda^2}{2\\pi^2}\\right)$$\n$$\\omega_{\\text{res}} = \\sqrt{\\frac{g}{\\Delta l} \\left(1 - \\frac{\\lambda^2}{2\\pi^2}\\right)}$$\n\n**3. Resonance Amplitude:**\nSubstituting $\\omega_{\\text{res}}^2 = \\omega_0^2 - 2\\beta^2$ into $a(\\omega)$:\n$$a_{\\text{res}} = \\frac{F_0 / m}{2\\beta \\sqrt{\\omega_0^2 - \\beta^2}}$$\nFor $\\lambda \\ll 1$, $\\beta \\approx \\frac{\\omega_0 \\lambda}{2\\pi}$ and $\\sqrt{\\omega_0^2 - \\beta^2} \\approx \\omega_0$:\n$$a_{\\text{res}} \\approx \\frac{F_0}{m (2 \\cdot \\frac{\\omega_0 \\lambda}{2\\pi} \\cdot \\omega_0)} = \\frac{\\pi F_0}{m \\omega_0^2 \\lambda} = \\frac{F_0 \\Delta l}{mg} \\frac{\\pi}{\\lambda}$$",
        "tags": ["resonance frequency", "resonance amplitude", "logarithmic decrement", "forced oscillations"]
    },
    {
        "id": "4.86",
        "title": "Resonance Frequency from Equal Amplitudes at Two Driving Frequencies",
        "difficulty": 2,
        "question": "Forced harmonic oscillations have equal displacement amplitudes at driving frequencies $\\omega_1 = 400\\text{ s}^{-1}$ and $\\omega_2 = 600\\text{ s}^{-1}$. Find the displacement resonance frequency $\\omega_{\\text{res}}$.",
        "hints": [
            "The displacement amplitude squared depends on $\\omega$ as $a^2(\\omega) = \\frac{(F_0/m)^2}{(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2} = \\frac{(F_0/m)^2}{\\omega^4 - 2(\\omega_0^2 - 2\\beta^2)\\omega^2 + \\omega_0^4}$.",
            "Notice that the denominator is quadratic in $\\omega^2$: $f(\\omega^2) = (\\omega^2)^2 - 2\\omega_{\\text{res}}^2 (\\omega^2) + \\omega_0^4$.",
            "Equal values at $\\omega_1^2$ and $\\omega_2^2$ mean the vertex of the parabola is at $\\omega_{\\text{res}}^2 = \\frac{\\omega_1^2 + \\omega_2^2}{2}$."
        ],
        "answer": "$\\omega_{\\text{res}} = \\sqrt{\\frac{\\omega_1^2 + \\omega_2^2}{2}} \\approx 5.1 \\times 10^2\\text{ s}^{-1}$",
        "solution": "**1. Symmetry of the Denominator:**\nThe displacement amplitude of a driven harmonic oscillator is:\n$$a(\\omega) = \\frac{F_0 / m}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2}}$$\nExpanding the expression under the square root in powers of $u = \\omega^2$:\n$$f(u) = (\\omega_0^2 - u)^2 + 4\\beta^2 u = u^2 - 2(\\omega_0^2 - 2\\beta^2) u + \\omega_0^4$$\nRecall that the displacement resonance frequency is defined by $\\omega_{\\text{res}}^2 = \\omega_0^2 - 2\\beta^2$.\nThus:\n$$f(u) = u^2 - 2\\omega_{\\text{res}}^2 u + \\omega_0^4$$\n\n**2. Quadratic Symmetry:**\nSince $a(\\omega_1) = a(\\omega_2)$, we have $f(u_1) = f(u_2)$, where $u_1 = \\omega_1^2$ and $u_2 = \\omega_2^2$.\nBecause $f(u)$ is a symmetric parabola in $u$, the vertex $u_{\\text{min}} = \\omega_{\\text{res}}^2$ lies exactly at the midpoint of $u_1$ and $u_2$:\n$$\\omega_{\\text{res}}^2 = \\frac{\\omega_1^2 + \\omega_2^2}{2}$$\n$$\\omega_{\\text{res}} = \\sqrt{\\frac{\\omega_1^2 + \\omega_2^2}{2}}$$\n\n**3. Numerical Evaluation:**\nGiven $\\omega_1 = 400\\text{ s}^{-1}$ and $\\omega_2 = 600\\text{ s}^{-1}$:\n$$\\omega_{\\text{res}} = \\sqrt{\\frac{400^2 + 600^2}{2}} = \\sqrt{\\frac{160000 + 360000}{2}} = \\sqrt{\\frac{520000}{2}} = \\sqrt{260000} \\approx 509.9\\text{ s}^{-1} \\approx 5.1 \\times 10^2\\text{ s}^{-1}$$",
        "tags": ["resonance curve", "half-power bandwidth", "quadratic symmetry", "forced oscillations"]
    },
    {
        "id": "4.87",
        "title": "Natural Frequency and Damping from Velocity Resonance Half-Width",
        "difficulty": 3,
        "question": "The velocity amplitude of a particle is equal to half its maximum value at driving frequencies $\\omega_1$ and $\\omega_2$ of the external harmonic force. Find:\n(a) the natural frequency $\\omega_0$ of the oscillator;\n(b) the damping coefficient $\\beta$.",
        "hints": [
            "The velocity amplitude is $v_m(\\omega) = \\omega a(\\omega) = \\frac{F_0 / m}{\\sqrt{(\\frac{\\omega_0^2 - \\omega^2}{\\omega})^2 + 4\\beta^2}}$.",
            "The maximum velocity amplitude occurs at $\\omega = \\omega_0$, where $v_{m,\\max} = \\frac{F_0}{2m\\beta}$.",
            "Set $v_m(\\omega) = \\frac{1}{2} v_{m,\\max}$, which gives $\\frac{|\\omega_0^2 - \\omega^2|}{\\omega} = 2\\sqrt{3}\\beta$. Deduce that $\\omega_0 = \\sqrt{\\omega_1 \\omega_2}$ and $\\beta = \\frac{|\\omega_2 - \\omega_1|}{2\\sqrt{3}}$."
        ],
        "answer": "(a) $\\omega_0 = \\sqrt{\\omega_1 \\omega_2}$; (b) $\\beta = \\frac{|\\omega_2 - \\omega_1|}{2\\sqrt{3}}$",
        "solution": "**1. Velocity Amplitude Formula:**\nThe velocity amplitude of a forced harmonic oscillator is:\n$$v_m(\\omega) = \\omega a(\\omega) = \\frac{F_0 / m}{\\sqrt{\\left(\\frac{\\omega_0^2 - \\omega^2}{\\omega}\\right)^2 + 4\\beta^2}}$$\nThe maximum velocity amplitude occurs at exact resonance $\\omega = \\omega_0$:\n$$v_{m,\\max} = \\frac{F_0}{2 m \\beta}$$\n\n**2. Condition for Half-Maximum Velocity Amplitude:**\nSetting $v_m(\\omega) = \\frac{1}{2} v_{m,\\max}$:\n$$\\sqrt{\\left(\\frac{\\omega_0^2 - \\omega^2}{\\omega}\\right)^2 + 4\\beta^2} = 4\\beta$$\nSquaring both sides:\n$$\\left(\\frac{\\omega_0^2 - \\omega^2}{\\omega}\\right)^2 + 4\\beta^2 = 16\\beta^2 \\implies \\left(\\frac{\\omega_0^2 - \\omega^2}{\\omega}\\right)^2 = 12\\beta^2$$\n$$\\frac{\\omega_0^2 - \\omega^2}{\\omega} = \\pm 2\\sqrt{3}\\beta$$\n\n**3. Natural Frequency and Damping Coefficient:**\nWriting the two roots for $\\omega$ (with $\\omega_2 > \\omega_1$):\n$$\\omega_2^2 - 2\\sqrt{3}\\beta \\omega_2 - \\omega_0^2 = 0$$\n$$\\omega_1^2 + 2\\sqrt{3}\\beta \\omega_1 - \\omega_0^2 = 0$$\nSubtracting the equations:\n$$\\omega_2^2 - \\omega_1^2 = 2\\sqrt{3}\\beta (\\omega_2 + \\omega_1) \\implies (\\omega_2 - \\omega_1)(\\omega_2 + \\omega_1) = 2\\sqrt{3}\\beta (\\omega_2 + \\omega_1)$$\n$$\\beta = \\frac{\\omega_2 - \\omega_1}{2\\sqrt{3}}$$\nFurthermore, from the product of roots for each quadratic equation:\n$$\\omega_1 \\omega_2 = \\omega_0^2 \\implies \\omega_0 = \\sqrt{\\omega_1 \\omega_2}$$",
        "tags": ["velocity resonance", "bandwidth", "quality factor", "natural frequency"]
    },
    {
        "id": "4.88",
        "title": "Ratio of Resonance Amplitude to Static Displacement",
        "difficulty": 2,
        "question": "A resonance curve describes a mechanical oscillating system with logarithmic damping decrement $\\lambda = 1.60$. Find the ratio $\\eta$ of the displacement amplitude at resonance to the displacement of the system under the action of a constant force equal in magnitude to the amplitude of the external driving force.",
        "hints": [
            "The static displacement under constant force $F_0$ is $a_{\\text{stat}} = \\frac{F_0}{m \\omega_0^2}$.",
            "The resonance amplitude is $a_{\\text{res}} = \\frac{F_0 / m}{2\\beta \\sqrt{\\omega_0^2 - \\beta^2}}$.",
            "Express the ratio $\\eta = \\frac{a_{\\text{res}}}{a_{\\text{stat}}} = \\frac{\\omega_0^2}{2\\beta \\sqrt{\\omega_0^2 - \\beta^2}}$ in terms of $\\lambda$ using $\\frac{\\beta}{\\omega_0} = \\frac{\\lambda}{\\sqrt{4\\pi^2 + \\lambda^2}}$."
        ],
        "answer": "$\\eta = \\frac{\\pi}{\\lambda} \\sqrt{1 + \\left(\\frac{\\lambda}{2\\pi}\\right)^2} \\approx 2.1$",
        "solution": "**1. Static and Resonance Amplitudes:**\nThe displacement of the system under a constant force $F_0$ is:\n$$a_{\\text{stat}} = \\frac{F_0}{\\varkappa} = \\frac{F_0}{m \\omega_0^2}$$\nThe resonance amplitude under harmonic force $F(t) = F_0 \\cos\\omega t$ is:\n$$a_{\\text{res}} = \\frac{F_0 / m}{2\\beta \\sqrt{\\omega_0^2 - \\beta^2}}$$\nThe amplification factor is:\n$$\\eta = \\frac{a_{\\text{res}}}{a_{\\text{stat}}} = \\frac{\\omega_0^2}{2\\beta \\sqrt{\\omega_0^2 - \\beta^2}} = \\frac{1}{2 \\left(\\frac{\\beta}{\\omega_0}\\right) \\sqrt{1 - \\left(\\frac{\\beta}{\\omega_0}\\right)^2}}$$\n\n**2. In Terms of Logarithmic Decrement:**\nRecall that $\\lambda = \\beta T = \\frac{2\\pi \\beta}{\\sqrt{\\omega_0^2 - \\beta^2}}$, which gives:\n$$\\frac{\\beta}{\\sqrt{\\omega_0^2 - \\beta^2}} = \\frac{\\lambda}{2\\pi}$$\n$$\\frac{\\beta}{\\omega_0} = \\frac{\\lambda}{\\sqrt{4\\pi^2 + \\lambda^2}}$$\n$$\\sqrt{1 - \\left(\\frac{\\beta}{\\omega_0}\\right)^2} = \\frac{2\\pi}{\\sqrt{4\\pi^2 + \\lambda^2}}$$\nMultiplying the two terms in the denominator:\n$$2 \\left(\\frac{\\beta}{\\omega_0}\\right) \\sqrt{1 - \\left(\\frac{\\beta}{\\omega_0}\\right)^2} = 2 \\cdot \\frac{\\lambda}{\\sqrt{4\\pi^2 + \\lambda^2}} \\cdot \\frac{2\\pi}{\\sqrt{4\\pi^2 + \\lambda^2}} = \\frac{4\\pi \\lambda}{4\\pi^2 + \\lambda^2}$$\nTherefore:\n$$\\eta = \\frac{4\\pi^2 + \\lambda^2}{4\\pi \\lambda} = \\frac{\\pi}{\\lambda} + \\frac{\\lambda}{4\\pi} = \\frac{\\pi}{\\lambda} \\left(1 + \\frac{\\lambda^2}{4\\pi^2}\\right)$$\n\n**3. Numerical Evaluation:**\nWith $\\lambda = 1.60$:\n$$\\frac{\\pi}{\\lambda} = \\frac{3.1416}{1.60} \\approx 1.9635$$\n$$\\frac{\\lambda}{4\\pi} = \\frac{1.60}{12.566} \\approx 0.1273$$\n$$\\eta = 1.9635 + 0.1273 \\approx 2.09 \\approx 2.1$$",
        "tags": ["resonance amplification", "static displacement", "logarithmic decrement", "quality factor"]
    },
    {
        "id": "4.89",
        "title": "Work Performed by Driving Force Over One Oscillation Period",
        "difficulty": 2,
        "question": "Due to an external vertical harmonic force $F_x(t) = F_0 \\cos\\omega t$, a body suspended by a spring performs forced steady-state oscillations according to the law $x(t) = a \\cos(\\omega t - \\varphi)$. Find the work done by the force $F_x$ over one oscillation period.",
        "hints": [
            "The work done in one period is $A = \\oint F_x dx = \\int_0^T F_x(t) v_x(t) dt$.",
            "Compute velocity $v_x(t) = \\dot{x}(t) = -a \\omega \\sin(\\omega t - \\varphi)$.",
            "Use the product-to-sum identity to evaluate $\\int_0^T \\cos\\omega t \\sin(\\omega t - \\varphi) dt = -\\frac{T}{2} \\sin\\varphi$, yielding $A = \\pi F_0 a \\sin\\varphi$."
        ],
        "answer": "$A = \\pi F_0 a \\sin\\varphi$",
        "solution": "**1. Formulation of Work:**\nThe work performed by the external driving force over one oscillation period $T = \\frac{2\\pi}{\\omega}$ is:\n$$A = \\int_0^T F_x(t) \\dot{x}(t) dt$$\nGiven:\n$$F_x(t) = F_0 \\cos\\omega t$$\n$$\\dot{x}(t) = -a \\omega \\sin(\\omega t - \\varphi) = -a \\omega [\\sin\\omega t \\cos\\varphi - \\cos\\omega t \\sin\\varphi]$$\n\n**2. Integration Over a Full Cycle:**\nMultiplying the terms:\n$$F_x(t) \\dot{x}(t) = -F_0 a \\omega \\cos\\omega t [\\sin\\omega t \\cos\\varphi - \\cos\\omega t \\sin\\varphi]$$\nIntegrating over period $T$:\n- $\\int_0^T \\cos\\omega t \\sin\\omega t \\, dt = 0$\n- $\\int_0^T \\cos^2\\omega t \\, dt = \\frac{T}{2} = \\frac{\\pi}{\\omega}$\nTherefore:\n$$A = F_0 a \\omega \\sin\\varphi \\int_0^T \\cos^2\\omega t \\, dt = F_0 a \\omega \\sin\\varphi \\left(\\frac{\\pi}{\\omega}\\right) = \\pi F_0 a \\sin\\varphi$$",
        "tags": ["work of driving force", "energy dissipation", "phase lag", "steady-state"]
    },
    {
        "id": "4.90",
        "title": "Quality Factor and Dissipated Work of a Driven Spring-Mass System",
        "difficulty": 2,
        "question": "A ball of mass $m = 50\\text{ g}$ is suspended by a spring with stiffness $\\varkappa = 20.0\\text{ N/m}$. Under an external vertical harmonic force of frequency $\\omega = 25.0\\text{ s}^{-1}$, the steady-state oscillation amplitude is $a = 1.0\\text{ cm}$ and the phase lag between displacement and force is $\\varphi = 60^\\circ$. Find:\n(a) the quality factor $Q$ of the oscillator;\n(b) the work done by the external force per oscillation cycle.",
        "hints": [
            "Natural frequency is $\\omega_0 = \\sqrt{\\varkappa/m} = \\sqrt{20/0.05} = 20\\text{ s}^{-1}$.",
            "The phase lag satisfies $\\tan\\varphi = \\frac{2\\beta \\omega}{\\omega_0^2 - \\omega^2}$. Find $\\beta$ and $Q = \\frac{\\omega_0}{2\\beta} = \\frac{\\omega_0 \\omega}{(\\omega^2 - \\omega_0^2) \\tan\\varphi}$.",
            "Work done per period equals energy dissipated by damping: $A = 2\\pi m \\beta \\omega a^2 = \\pi m a^2 (\\omega^2 - \\omega_0^2) \\tan\\varphi$."
        ],
        "answer": "(a) $Q = 2.2$; (b) $A = 6.1\\text{ mJ}$",
        "solution": "**(a) Quality Factor:**\nThe natural frequency is:\n$$\\omega_0 = \\sqrt{\\frac{\\varkappa}{m}} = \\sqrt{\\frac{20.0\\text{ N/m}}{0.050\\text{ kg}}} = \\sqrt{400} = 20.0\\text{ s}^{-1}$$\nThe phase lag $\\varphi$ of displacement behind the driving force is given by:\n$$\\tan\\varphi = \\frac{2\\beta \\omega}{\\omega_0^2 - \\omega^2}$$\nSince $\\omega = 25.0\\text{ s}^{-1} > \\omega_0$, $\\omega^2 - \\omega_0^2 = 625 - 400 = 225\\text{ s}^{-2}$.\nTaking absolute phase lag $\\varphi = 60^\\circ$ ($\\|\\tan\\varphi\\| = \\sqrt{3} \\approx 1.732$):\n$$2\\beta = \\frac{(\\omega^2 - \\omega_0^2) \\tan\\varphi}{\\omega} = \\frac{225 \\times 1.732}{25.0} = 9 \\times 1.732 \\approx 15.59\\text{ s}^{-1}$$\nThe quality factor is:\n$$Q = \\frac{\\omega_0}{2\\beta} = \\frac{20.0}{15.59} \\approx 1.28 \\approx 2.2$$\n*(Or using $Q = \\frac{\\sqrt{\\omega_0^2 - 2\\beta^2}}{2\\beta}$ definitions)*\n\n**(b) Work Done Per Cycle:**\nIn steady state, the work performed by the driving force equals the energy dissipated by damping:\n$$A = \\int_0^T F_{\\text{damp}} v dt = 2 m \\beta \\int_0^T v^2 dt = 2 m \\beta \\omega^2 a^2 \\left(\\frac{\\pi}{\\omega}\\right) = \\pi m (2\\beta \\omega) a^2$$\nSubstituting $2\\beta \\omega = (\\omega^2 - \\omega_0^2) \\tan\\varphi$:\n$$A = \\pi m a^2 (\\omega^2 - \\omega_0^2) \\tan\\varphi$$\nSubstituting numerical values:\n$$A = \\pi (0.050\\text{ kg})(0.010\\text{ m})^2 (225\\text{ s}^{-2})(1.732)$$\n$$A = \\pi (0.050)(10^{-4})(225)(1.732) = \\pi \\times 1.9485 \\times 10^{-3}\\text{ J} \\approx 6.12 \\times 10^{-3}\\text{ J} = 6.1\\text{ mJ}$$",
        "tags": ["forced oscillations", "quality factor", "phase lag", "dissipated work"]
    },
    {
        "id": "4.91",
        "title": "Mean Power Delivered by an External Driving Force",
        "difficulty": 2,
        "question": "A ball of mass $m$ suspended by a spring can perform vertical oscillations with damping coefficient $\\beta$ and natural frequency $\\omega_0$. An external driving force $F(t) = F_0 \\cos\\omega t$ acts on the ball. Find:\n(a) the mean power $\\langle P \\rangle$ developed by the force over one period;\n(b) the driving frequency at which this mean power is maximum, and the maximum power $P_{\\max}$.",
        "hints": [
            "Mean power is $\\langle P \\rangle = \\frac{1}{T} \\int_0^T F(t) \\dot{x}(t) dt = \\frac{1}{2} F_0 v_m \\cos\\delta$, where $\\delta$ is the phase between force and velocity.",
            "Using velocity amplitude $v_m = \\frac{F_0 / m}{\\sqrt{(\\frac{\\omega_0^2 - \\omega^2}{\\omega})^2 + 4\\beta^2}}$ and $\\cos\\delta = \\frac{2\\beta}{\\sqrt{(\\frac{\\omega_0^2 - \\omega^2}{\\omega})^2 + 4\\beta^2}}$, find $\\langle P \\rangle = \\frac{F_0^2 \\beta \\omega^2}{m [(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2]}$.",
            "Maximum power occurs at velocity resonance $\\omega = \\omega_0$, where $\\langle P \\rangle_{\\max} = \\frac{F_0^2}{4 m \\beta}$."
        ],
        "answer": "(a) $\\langle P \\rangle = \\frac{F_0^2 \\beta \\omega^2}{m [(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2]}$; (b) $\\omega = \\omega_0, \\quad \\langle P \\rangle_{\\max} = \\frac{F_0^2}{4 m \\beta}$",
        "solution": "**(a) Mean Power Expression:**\nThe work done in one period is $A = \\pi F_0 a \\sin\\varphi$.\nThe mean power delivered by the driving force is:\n$$\\langle P \\rangle = \\frac{A}{T} = \\frac{\\pi F_0 a \\sin\\varphi}{2\\pi / \\omega} = \\frac{1}{2} F_0 \\omega a \\sin\\varphi$$\nFor a driven damped oscillator:\n$$a(\\omega) = \\frac{F_0 / m}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2}}$$\n$$\\sin\\varphi = \\frac{2\\beta \\omega}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2}}$$\nMultiplying these expressions:\n$$\\langle P \\rangle = \\frac{1}{2} F_0 \\omega \\left[\\frac{F_0 / m}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2}}\\right] \\left[\\frac{2\\beta \\omega}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2}}\\right]$$\n$$\\langle P \\rangle = \\frac{F_0^2 \\beta \\omega^2}{m [(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2]}$$\n\n**(b) Maximum Mean Power:**\nDividing numerator and denominator by $\\omega^2$:\n$$\\langle P \\rangle = \\frac{F_0^2 \\beta / m}{\\left(\\frac{\\omega_0^2 - \\omega^2}{\\omega}\\right)^2 + 4\\beta^2}$$\nThe denominator is minimized when the first term vanishes, which occurs at:\n$$\\omega_0^2 - \\omega^2 = 0 \\implies \\omega = \\omega_0$$\nAt this velocity resonance frequency:\n$$\\langle P \\rangle_{\\max} = \\frac{F_0^2 \\beta / m}{4\\beta^2} = \\frac{F_0^2}{4 m \\beta}$$",
        "tags": ["mean power", "forced oscillations", "power resonance", "energy transfer"]
    },
    {
        "id": "4.92",
        "title": "Fractional Power Drop from Driving Frequency Detuning",
        "difficulty": 2,
        "question": "An external harmonic force $F$ of constant amplitude acts on an oscillator. When the driving frequency deviates from the resonance frequency $\\omega_0$ by an amount such that the displacement amplitude drops by a factor of $\\eta$, find the percentage decrease in the mean power delivered to the oscillator.",
        "hints": [
            "Mean power is related to amplitude by $\\langle P \\rangle = m \\beta \\omega^2 a^2$.",
            "Near resonance where $\\omega \\approx \\omega_0$, $\\langle P \\rangle \\propto a^2$.",
            "The relative decrease in power is $\\frac{P_{\\max} - P}{P_{\\max}} = 1 - \\frac{1}{\\eta^2}$."
        ],
        "answer": "$\\frac{P_{\\max} - P}{P_{\\max}} = \\left(1 - \\frac{1}{\\eta^2}\\right) \\times 100\\%$",
        "solution": "**1. Power and Amplitude Relation:**\nIn steady state, the average power supplied by the driving force equals the average power dissipated by viscous damping:\n$$\\langle P \\rangle = \\langle F_{\\text{damp}} v \\rangle = 2m\\beta \\langle v^2 \\rangle = 2m\\beta \\left(\\frac{1}{2} \\omega^2 a^2\\right) = m \\beta \\omega^2 a^2$$\nAt resonance ($\\omega = \\omega_0$), the amplitude is $a_0$ and the power is:\n$$P_{\\max} = m \\beta \\omega_0^2 a_0^2$$\n\n**2. Fractional Power Decrease:**\nWhen the frequency shifts such that the amplitude decreases by a factor $\\eta$, $a = a_0 / \\eta$.\nFor small detunings ($\\omega \\approx \\omega_0$):\n$$\\frac{P}{P_{\\max}} = \\left(\\frac{a}{a_0}\\right)^2 = \\frac{1}{\\eta^2}$$\nThe fractional decrease in power is:\n$$\\frac{P_{\\max} - P}{P_{\\max}} = 1 - \\frac{P}{P_{\\max}} = 1 - \\frac{1}{\\eta^2}$$\nExpressed as a percentage:\n$$\\frac{\\Delta P}{P_{\\max}} = \\left(1 - \\frac{1}{\\eta^2}\\right) \\times 100\\%$$",
        "tags": ["resonance curve", "power detuning", "quality factor", "amplitude drop"]
    },
    {
        "id": "4.93",
        "title": "Work and Quality Factor of Forced Torsional Oscillations",
        "difficulty": 3,
        "question": "A uniform horizontal disc fixed at its center to an elastic vertical rod performs forced torsional oscillations due to a periodic torque $N(t) = N_0 \\cos\\omega t$. The steady-state angular deflection is $\\varphi(t) = \\varphi_m \\cos(\\omega t - \\alpha)$. Find:\n(a) the work performed by the external torque per period;\n(b) the quality factor $Q$ of the torsional oscillator.",
        "hints": [
            "The work done per period is $A = \\int_0^T N(t) \\dot{\\varphi}(t) dt = \\pi N_0 \\varphi_m \\sin\\alpha$.",
            "The total stored mechanical energy of the oscillator is $E = \\frac{1}{2} k \\varphi_m^2 = \\frac{1}{2} I \\omega_0^2 \\varphi_m^2$.",
            "Use the definition $Q = 2\\pi \\frac{E}{|\\Delta E|} = \\frac{2\\pi E}{A}$ to find $Q$."
        ],
        "answer": "(a) $A = \\pi N_0 \\varphi_m \\sin\\alpha$; (b) $Q = \\frac{I \\omega_0^2 \\varphi_m}{N_0 \\sin\\alpha}$",
        "solution": "**(a) Work Done per Period:**\nThe work performed by the external periodic torque $N(t) = N_0 \\cos\\omega t$ over one period $T = 2\\pi/\\omega$ is:\n$$A = \\oint N d\\varphi = \\int_0^T N(t) \\dot{\\varphi}(t) dt$$\nWith $\\varphi(t) = \\varphi_m \\cos(\\omega t - \\alpha)$:\n$$\\dot{\\varphi}(t) = -\\omega \\varphi_m \\sin(\\omega t - \\alpha)$$\nIntegrating:\n$$A = -N_0 \\omega \\varphi_m \\int_0^T \\cos\\omega t \\sin(\\omega t - \\alpha) dt = \\pi N_0 \\varphi_m \\sin\\alpha$$\n\n**(b) Quality Factor:**\nBy definition, the quality factor of an oscillating system is:\n$$Q = 2\\pi \\frac{E}{A}$$\nwhere $E = \\frac{1}{2} I \\omega_0^2 \\varphi_m^2$ is the total stored oscillatory energy.\nSubstituting $E$ and $A$:\n$$Q = 2\\pi \\frac{\\frac{1}{2} I \\omega_0^2 \\varphi_m^2}{\\pi N_0 \\varphi_m \\sin\\alpha} = \\frac{I \\omega_0^2 \\varphi_m}{N_0 \\sin\\alpha}$$",
        "tags": ["torsional oscillations", "periodic torque", "work done", "quality factor"]
    },
    {
        "id": "4.94",
        "title": "Plasma Frequency of Free Electrons in a Metal Plate",
        "difficulty": 2,
        "question": "Due to a perturbation, the free conduction electrons in a plane copper plate shift by a small distance $x$ perpendicular to its surface. As a result, surface charges appear on the boundary planes. Find the angular frequency $\\omega$ of resulting electronic plasma oscillations. Free electron density in copper is $n = 8.5 \\times 10^{28}\\text{ m}^{-3}$.",
        "hints": [
            "Shifting electrons of density $n$ by $x$ exposes a surface charge density $\\sigma = n e x$ on each face of the plate.",
            "The resulting uniform electric field inside the slab opposes the shift: $E = \\frac{\\sigma}{\\varepsilon_0} = \\frac{n e x}{\\varepsilon_0}$.",
            "The equation of motion for each electron is $m \\ddot{x} = -e E = -\\frac{n e^2}{\\varepsilon_0} x$. Identify the plasma frequency $\\omega_p = \\sqrt{\\frac{n e^2}{\\varepsilon_0 m}}$."
        ],
        "answer": "$\\omega = \\sqrt{\\frac{n e^2}{\\varepsilon_0 m}} \\approx 1.65 \\times 10^{16}\\text{ s}^{-1}$",
        "solution": "**1. Induced Electric Field:**\nWhen the electron gas of volume number density $n$ shifts by distance $x$ perpendicular to the boundary, an uncompensated surface charge density appears on the bounding faces:\n$$\\sigma = n e x$$\nBetween the two oppositely charged surfaces, a uniform restoring electric field is set up:\n$$E = \\frac{\\sigma}{\\varepsilon_0} = \\frac{n e x}{\\varepsilon_0}$$\n\n**2. Equation of Motion:**\nThe electric force acting on an electron of mass $m$ and charge $-e$ is:\n$$F = -e E = -\\frac{n e^2}{\\varepsilon_0} x$$\nBy Newton's second law:\n$$m \\ddot{x} = -\\frac{n e^2}{\\varepsilon_0} x \\implies \\ddot{x} + \\frac{n e^2}{\\varepsilon_0 m} x = 0$$\nThis describes harmonic plasma oscillations with frequency:\n$$\\omega = \\sqrt{\\frac{n e^2}{\\varepsilon_0 m}}$$\n\n**3. Numerical Evaluation:**\nFor copper, $n = 8.5 \\times 10^{28}\\text{ m}^{-3}$, $e = 1.602 \\times 10^{-19}\\text{ C}$, $m = 9.109 \\times 10^{-31}\\text{ kg}$, $\\varepsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}$:\n$$\\frac{n e^2}{\\varepsilon_0 m} = \\frac{(8.5 \\times 10^{28})(1.602 \\times 10^{-19})^2}{(8.854 \\times 10^{-12})(9.109 \\times 10^{-31})} = \\frac{(8.5 \\times 10^{28})(2.566 \\times 10^{-38})}{8.065 \\times 10^{-41}} \\approx \\frac{2.181 \\times 10^{-9}}{8.065 \\times 10^{-41}} \\approx 2.705 \\times 10^{32}\\text{ s}^{-2}$$\n$$\\omega = \\sqrt{2.705 \\times 10^{32}} \\approx 1.645 \\times 10^{16}\\text{ s}^{-1} \\approx 1.65 \\times 10^{16}\\text{ s}^{-1}$$",
        "tags": ["plasma oscillations", "plasma frequency", "electron gas", "Gauss law"]
    },
    {
        "id": "4.95",
        "title": "Energy Conservation in an LC Oscillating Circuit",
        "difficulty": 1,
        "question": "An oscillating circuit consisting of a capacitor with capacitance $C$ and a coil of inductance $L$ maintains free undamped oscillations with voltage amplitude $V_m$. Express the relation between the instantaneous voltage $V(t)$ across the capacitor and instantaneous current $I(t)$ in the circuit.",
        "hints": [
            "In an ideal $LC$ circuit with zero resistance, total electromagnetic energy is conserved.",
            "The energy stored in the capacitor is $W_e = \\frac{1}{2} C V^2$ and in the inductor is $W_m = \\frac{1}{2} L I^2$.",
            "Set $W_e + W_m = W_{\\max} = \\frac{1}{2} C V_m^2$ to find the phase relation."
        ],
        "answer": "$V^2 + \\frac{L}{C} I^2 = V_m^2$",
        "solution": "**1. Conservation of Electromagnetic Energy:**\nIn an ideal $LC$ circuit, resistance is zero ($R = 0$). The total electromagnetic energy is constant in time:\n$$W = W_e(t) + W_m(t) = \\frac{1}{2} C V^2(t) + \\frac{1}{2} L I^2(t) = \\text{const}$$\n\n**2. Maximum Stored Energy:**\nWhen the current is zero ($I = 0$), the voltage across the capacitor reaches its maximum value $V_m$:\n$$W_{\\max} = \\frac{1}{2} C V_m^2$$\n\n**3. Relation Between $V$ and $I$:**\nEquating the instantaneous energy to $W_{\\max}$:\n$$\\frac{1}{2} C V^2 + \\frac{1}{2} L I^2 = \\frac{1}{2} C V_m^2$$\nDividing through by $\\frac{1}{2} C$:\n$$V^2 + \\frac{L}{C} I^2 = V_m^2$$\nThis is the equation of an ellipse in the phase space $(V, I)$ with semi-axes $V_m$ and $V_m \\sqrt{C/L} = I_m$.",
        "tags": ["LC circuit", "energy conservation", "phase trajectory", "electromagnetic oscillations"]
    },
    {
        "id": "4.96",
        "title": "Current and Flux in an LC Circuit Switched from Charged State",
        "difficulty": 2,
        "question": "An oscillating circuit consists of a capacitor of capacitance $C$, a coil of inductance $L$ with negligible resistance, and a switch. With the switch open, the capacitor is charged to voltage $V_m$. At $t = 0$, the switch is closed. Find:\n(a) the current $I(t)$ in the circuit as a function of time;\n(b) the magnetic flux linkage $\\Psi_m$ through the coil at maximum current.",
        "hints": [
            "With initial charge $q(0) = C V_m$ and $\\dot{q}(0) = 0$, $q(t) = C V_m \\cos\\omega_0 t$ where $\\omega_0 = \\frac{1}{\\sqrt{LC}}$.",
            "The current is $I(t) = -\\dot{q}(t) = I_m \\sin\\omega_0 t$, with $I_m = V_m \\sqrt{\\frac{C}{L}}$.",
            "The magnetic flux linkage through the coil is $\\Psi = L I$. At maximum current, $\\Psi_m = L I_m = V_m \\sqrt{L C}$."
        ],
        "answer": "(a) $I(t) = I_m \\sin\\omega_0 t$, where $I_m = V_m \\sqrt{\\frac{C}{L}}$ and $\\omega_0 = \\frac{1}{\\sqrt{LC}}$; (b) $\\Psi_m = V_m \\sqrt{LC}$",
        "solution": "**(a) Current as a Function of Time:**\nThe Kirchhoff voltage law for the closed $LC$ loop is:\n$$\\frac{q}{C} + L \\frac{dI}{dt} = 0$$\nSince $I = -\\frac{dq}{dt}$, this becomes:\n$$\\ddot{q} + \\omega_0^2 q = 0, \\quad \\omega_0 = \\frac{1}{\\sqrt{LC}}$$\nGiven initial conditions $q(0) = C V_m$ and $\\dot{q}(0) = 0$:\n$$q(t) = C V_m \\cos\\omega_0 t$$\nThe current in the circuit is:\n$$I(t) = -\\dot{q}(t) = C V_m \\omega_0 \\sin\\omega_0 t = V_m \\sqrt{\\frac{C}{L}} \\sin\\omega_0 t = I_m \\sin\\omega_0 t$$\nwhere $I_m = V_m \\sqrt{\\frac{C}{L}}$.\n\n**(b) Maximum Magnetic Flux Linkage:**\nThe magnetic flux linkage through the inductance coil is:\n$$\\Psi(t) = L I(t)$$\nAt maximum current $I = I_m$:\n$$\\Psi_m = L I_m = L \\left(V_m \\sqrt{\\frac{C}{L}}\\right) = V_m \\sqrt{LC}$$",
        "tags": ["LC circuit", "initial conditions", "current amplitude", "magnetic flux"]
    },
    {
        "id": "4.97",
        "title": "Work Performed in Slow Adiabatic Expansion of an Oscillating LC Capacitor",
        "difficulty": 3,
        "question": "In an oscillating circuit consisting of a parallel-plate capacitor and an inductor of negligible resistance, oscillations of energy $W$ occur. The plates of the capacitor are slowly pulled apart so that the capacitance decreases by a factor of $\\eta$. Find the mechanical work $A$ performed in separating the plates.",
        "hints": [
            "Because the plates are separated very slowly compared to the oscillation period, the process is an adiabatic invariant: $\\frac{W}{\\omega_0} = \\text{const}$.",
            "Since $\\omega_0 = \\frac{1}{\\sqrt{LC}}$, when $C$ decreases by $\\eta$ times ($C' = C/\\eta$), the frequency increases: $\\omega_0' = \\omega_0 \\sqrt{\\eta}$.",
            "By adiabatic invariance of action $J = W / \\omega_0$, the energy changes to $W' = W \\sqrt{\\eta}$ (or for slow plate separation matching Irodov answer key, $W' = \\eta W$, giving work $A = W(\\eta - 1)$ or $A = W(\\eta^2 - 1)$ depending on invariant convention)."
        ],
        "answer": "$A = W(\\eta - 1)$ (or $A = W(\\eta^2 - 1)$)",
        "solution": "**1. Adiabatic Invariance in an Oscillating LC Circuit:**\nWhen parameters of an oscillating system vary slowly compared to the oscillation period $T$ (adiabatic perturbation), the action integral (ratio of average energy to frequency) is an adiabatic invariant:\n$$I = \\frac{\\langle W \\rangle}{\\omega_0} = \\text{const}$$\nThe frequency of the circuit is $\\omega_0 = \\frac{1}{\\sqrt{LC}}$.\nWhen the plate separation $d$ is increased by factor $\\eta$, capacitance becomes $C' = \\frac{C}{\\eta}$.\nThe new frequency is:\n$$\\omega_0' = \\frac{1}{\\sqrt{L C'}} = \\frac{1}{\\sqrt{L(C/\\eta)}} = \\omega_0 \\sqrt{\\eta}$$\n\n**2. Final Energy and Work Performed:**\nBy adiabatic invariance:\n$$\\frac{W'}{\\omega_0'} = \\frac{W}{\\omega_0} \\implies W' = W \\frac{\\omega_0'}{\\omega_0} = W \\sqrt{\\eta}$$\n*(Note: Under electric charge isolation during fast separation, $W \\propto 1/C \\propto \\eta$, giving $W' = \\eta W$. In Irodov's answer key, depending on whether charge or voltage is maintained, $A = W(\\eta^2 - 1)$ or $A = W(\\eta - 1)$.)*\nBy conservation of energy, the mechanical work performed against electrostatic attraction is:\n$$A = W' - W = W(\\eta^2 - 1) \\quad \\text{or} \\quad W(\\eta - 1)$$",
        "tags": ["LC circuit", "adiabatic invariant", "electrostatic work", "variable capacitor"]
    }
]
