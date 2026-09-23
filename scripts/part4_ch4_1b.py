"""
part4_ch4_1b.py
Curated problems 4.26 to 4.50 (25 problems) of Irodov Chapter 4.1:
Mechanical Oscillations (Part B).
"""

CH4_1B_CURATED = [
    {
        "id": "4.26",
        "title": "Transverse Oscillations of a Bead on a Stretched String",
        "difficulty": 2,
        "question": "A small body of mass $m$ is fixed to the middle of a stretched string of length $2l$. In the equilibrium position the string tension is equal to $T_0$. Find the angular frequency of small oscillations of the body in the transverse direction. The mass of the string is negligible and the gravitational field is absent.",
        "hints": [
            "For a small transverse displacement $y \\ll l$, each half of the string has length $\\sqrt{l^2 + y^2} \\approx l + \\frac{y^2}{2l}$, meaning change in length is second order and tension remains approximately constant at $T_0$.",
            "The restoring force from each half of the string along the transverse axis is $-T_0 \\sin\\theta \\approx -T_0 \\frac{y}{l}$.",
            "The total restoring force on mass $m$ is $F_y = -2 T_0 \\frac{y}{l}$. Formulate Newton's second law $m \\ddot{y} + \\frac{2T_0}{l} y = 0$ to find $\\omega$."
        ],
        "answer": "$\\omega = \\sqrt{\\frac{2 T_0}{m l}}$",
        "solution": "**1. Geometry and String Tension:**\nLet the transverse displacement of the bead from the straight configuration be $y$, where $y \\ll l$.\nThe length of each half of the string becomes:\n$$l' = \\sqrt{l^2 + y^2} = l \\sqrt{1 + \\left(\\frac{y}{l}\\right)^2} \\approx l \\left(1 + \\frac{y^2}{2l^2}\\right)$$\nThe elongation $\\Delta l = l' - l \\approx \\frac{y^2}{2l}$ is of the second order in $y/l$. Therefore, to the first order of smallness, the tension in the string remains constant and equal to $T_0$.\n\n**2. Equation of Motion:**\nEach half of the string pulls the body toward the equilibrium axis at an angle $\\theta \\approx \\frac{y}{l}$.\nThe net transverse restoring force acting on the body is:\n$$F_y = -2 T_0 \\sin\\theta \\approx -2 T_0 \\frac{y}{l}$$\nApplying Newton's second law:\n$$m \\ddot{y} = -\\frac{2 T_0}{l} y \\implies \\ddot{y} + \\frac{2 T_0}{m l} y = 0$$\n\n**3. Angular Frequency:**\nComparing with the standard harmonic oscillator equation $\\ddot{y} + \\omega^2 y = 0$:\n$$\\omega = \\sqrt{\\frac{2 T_0}{m l}}$$",
        "tags": ["transverse oscillations", "stretched string", "restoring force", "small oscillations"]
    },
    {
        "id": "4.27",
        "title": "Oscillation of Liquid in an Asymmetric U-Tube",
        "difficulty": 2,
        "question": "Determine the period of small oscillations of mercury of mass $m = 200\\text{ g}$ poured into a bent tube whose right arm forms an angle $\\theta = 30^\\circ$ with the vertical, while the left arm is vertical. The cross-sectional area of the tube is $S = 0.50\\text{ cm}^2$. The viscosity of mercury is to be neglected.",
        "hints": [
            "If the mercury column is displaced by a distance $x$ along the tube, the mercury surface in the vertical arm rises by $x$, and in the inclined arm drops by $x \\cos\\theta$ in vertical height.",
            "The difference in hydrostatic levels between the two free surfaces is $\\Delta h = x + x \\cos\\theta = x(1 + \\cos\\theta)$.",
            "The net restoring force is $F = -\\rho S g \\Delta h = -\\rho S g (1 + \\cos\\theta) x$. The total mass oscillating is $m$, so $T = 2\\pi \\sqrt{\\frac{m}{\\rho S g (1 + \\cos\\theta)}}$."
        ],
        "answer": "$T = 2\\pi \\sqrt{\\frac{m}{\\rho S g (1 + \\cos\\theta)}} \\approx 0.8\\text{ s}$",
        "solution": "**1. Hydrostatic Restoring Force:**\nLet $x$ be the displacement of the mercury column along the tube from its equilibrium position.\n- In the vertical left arm, the surface rises by vertical height $\\Delta h_1 = x$.\n- In the inclined right arm, the surface moves along the tube by $x$, which corresponds to a vertical height decrease of $\\Delta h_2 = x \\cos\\theta$.\nThe total difference in vertical levels between the two arms is:\n$$\\Delta h = \\Delta h_1 + \\Delta h_2 = x(1 + \\cos\\theta)$$\nThe resulting unbalanced hydrostatic restoring force acting on the entire liquid column is:\n$$F = -\\rho S g \\Delta h = -\\rho S g (1 + \\cos\\theta) x$$\nwhere $\\rho$ is the density of mercury and $S$ is the tube cross-section.\n\n**2. Equation of Motion and Period:**\nThe entire mass of mercury $m$ moves with acceleration $\\ddot{x}$:\n$$m \\ddot{x} + \\rho S g (1 + \\cos\\theta) x = 0$$\nThe angular frequency of harmonic oscillations is:\n$$\\omega = \\sqrt{\\frac{\\rho S g (1 + \\cos\\theta)}{m}}$$\nThe oscillation period is:\n$$T = \\frac{2\\pi}{\\omega} = 2\\pi \\sqrt{\\frac{m}{\\rho S g (1 + \\cos\\theta)}}$$\n\n**3. Numerical Calculation:**\nWith $m = 0.200\\text{ kg}$, $\\rho = 13.6 \\times 10^3\\text{ kg/m}^3$, $S = 0.50 \\times 10^{-4}\\text{ m}^2$, $g = 9.8\\text{ m/s}^2$, and $\\theta = 30^\\circ$ (so $\\cos 30^\\circ = \\frac{\\sqrt{3}}{2} \\approx 0.866$):\n$$\\rho S g (1 + \\cos\\theta) = (13600)(5.0 \\times 10^{-5})(9.8)(1 + 0.866) \\approx (0.68)(9.8)(1.866) \\approx 12.43\\text{ N/m}$$\n$$T = 2\\pi \\sqrt{\\frac{0.200}{12.43}} = 2\\pi \\sqrt{0.01609} = 2\\pi (0.1268) \\approx 0.80\\text{ s}$$",
        "tags": ["U-tube oscillations", "hydrostatics", "fluid mechanics", "harmonic motion"]
    },
    {
        "id": "4.28",
        "title": "Harmonic Oscillations of a Rod on Rotating Rollers",
        "difficulty": 2,
        "question": "A uniform rod is placed horizontally on two spinning wheels whose axes are separated by a distance $l = 20\\text{ cm}$. The wheels rotate in opposite directions towards each other. The coefficient of friction between the rod and the wheels is $k = 0.18$. Demonstrate that the rod performs harmonic oscillations and find the period of these oscillations.",
        "hints": [
            "Let the center of mass of the rod be displaced by distance $x$ from the midpoint between the rollers. Find normal forces $N_1$ and $N_2$ from torque equilibrium.",
            "Setting torques about the center of mass to zero: $N_1 (l/2 + x) = N_2 (l/2 - x)$, with $N_1 + N_2 = mg$.",
            "Because the rollers rotate inward, the sliding friction forces oppose displacement: $F_{\\text{net}} = k N_2 - k N_1 = -\\frac{2kmg}{l} x$. Show this leads to $T = \\pi \\sqrt{\\frac{2l}{kg}}$."
        ],
        "answer": "$T = \\pi \\sqrt{\\frac{2l}{k g}} \\approx 1.5\\text{ s}$",
        "solution": "**1. Normal Reactions on the Rod:**\nLet the midpoint between the two rotating wheels be the origin $x = 0$. Suppose the center of mass of the rod is displaced by $x$ to the right.\nThe distance of the center of mass to wheel 1 (left) is $\\frac{l}{2} + x$, and to wheel 2 (right) is $\\frac{l}{2} - x$.\nSince there is no vertical motion:\n$$N_1 + N_2 = mg$$\nTaking torques about the center of mass:\n$$N_1 \\left(\\frac{l}{2} + x\\right) = N_2 \\left(\\frac{l}{2} - x\\right)$$\nSolving for the normal reaction forces:\n$$N_1 = mg \\frac{l/2 - x}{l}, \\quad N_2 = mg \\frac{l/2 + x}{l}$$\n\n**2. Frictional Restoring Force:**\nThe wheels rotate inward toward the center. Hence:\n- Wheel 1 exerts a kinetic friction force to the right: $F_1 = k N_1$.\n- Wheel 2 exerts a kinetic friction force to the left: $F_2 = k N_2$.\nThe net horizontal force acting on the rod is:\n$$F_x = F_1 - F_2 = k (N_1 - N_2) = k \\left[ mg \\frac{l/2 - x}{l} - mg \\frac{l/2 + x}{l} \\right] = -\\frac{2 k mg}{l} x$$\n\n**3. Equation of Motion and Period:**\nBy Newton's second law:\n$$m \\ddot{x} = -\\frac{2 k mg}{l} x \\implies \\ddot{x} + \\frac{2 k g}{l} x = 0$$\nThis is the standard equation of simple harmonic motion with angular frequency:\n$$\\omega = \\sqrt{\\frac{2 k g}{l}}$$\nThe oscillation period is:\n$$T = \\frac{2\\pi}{\\omega} = 2\\pi \\sqrt{\\frac{l}{2kg}} = \\pi \\sqrt{\\frac{2l}{kg}}$$\n\n**4. Numerical Calculation:**\nWith $l = 0.20\\text{ m}$, $k = 0.18$, and $g = 9.8\\text{ m/s}^2$:\n$$T = \\pi \\sqrt{\\frac{2(0.20)}{(0.18)(9.8)}} = \\pi \\sqrt{\\frac{0.40}{1.764}} = \\pi \\sqrt{0.2268} = \\pi (0.4762) \\approx 1.50\\text{ s}$$",
        "tags": ["rotating rollers", "kinetic friction", "harmonic oscillator", "torque balance"]
    },
    {
        "id": "4.29",
        "title": "Oscillations Through an Earth Diameter Shaft",
        "difficulty": 2,
        "question": "Imagine a shaft going all the way through the Earth from pole to pole along its rotation axis. Assuming the Earth to be a homogeneous sphere of radius $R$ and neglecting air drag, find:\n(a) the equation of motion of a body falling down into the shaft;\n(b) how long does it take the body to reach the other end of the shaft;\n(c) the velocity of the body at the Earth's centre.",
        "hints": [
            "Inside a uniform spherical mass, the gravitational force at distance $x$ from the center is due only to the sphere of radius $x$: $F(x) = -\\frac{G M(x) m}{x^2} = -m \\frac{g}{R} x$.",
            "The equation of motion is $\\ddot{x} + \\frac{g}{R} x = 0$, representing simple harmonic motion with angular frequency $\\omega = \\sqrt{g/R}$.",
            "The transit time through the Earth is half a period: $\\tau = \\pi \\sqrt{R/g}$. The velocity at the center is the maximum oscillation velocity $v_{\\max} = \\omega R = \\sqrt{gR}$."
        ],
        "answer": "(a) $\\ddot{x} + \\frac{g}{R} x = 0$; (b) $\\tau = \\pi \\sqrt{\\frac{R}{g}} \\approx 42\\text{ min}$; (c) $v = \\sqrt{gR} \\approx 7.9\\text{ km/s}$",
        "solution": "**(a) Equation of Motion:**\nFor a homogeneous sphere of radius $R$ and total mass $M$, the mass enclosed within a concentric sphere of radius $x$ ($x \\le R$) is:\n$$M(x) = M \\left(\\frac{x}{R}\\right)^3$$\nBy Gauss's law for gravitation, the spherical shell outside radius $x$ exerts zero net force. The gravitational force on a body of mass $m$ at coordinate $x$ along the shaft is:\n$$F(x) = -\\frac{G M(x) m}{x^2} = -\\frac{G M m}{R^3} x = -m \\left(\\frac{g}{R}\\right) x$$\nwhere $g = \\frac{GM}{R^2}$ is the free-fall acceleration at the Earth's surface.\nNewton's second law gives:\n$$m \\ddot{x} = -m \\frac{g}{R} x \\implies \\ddot{x} + \\frac{g}{R} x = 0$$\n\n**(b) Time to Reach the Other End:**\nThe motion is simple harmonic with angular frequency $\\omega = \\sqrt{\\frac{g}{R}}$ and period $T = 2\\pi \\sqrt{\\frac{R}{g}}$.\nDropping the body from one pole ($x = R$) to the opposite pole ($x = -R$) corresponds to half an oscillation cycle:\n$$\\tau = \\frac{T}{2} = \\pi \\sqrt{\\frac{R}{g}}$$\nWith $R \\approx 6.37 \\times 10^6\\text{ m}$ and $g = 9.8\\text{ m/s}^2$:\n$$\\tau = \\pi \\sqrt{\\frac{6.37 \\times 10^6}{9.8}} \\approx \\pi \\times 806.2\\text{ s} \\approx 2533\\text{ s} \\approx 42.2\\text{ min} \\approx 42\\text{ min}$$\n\n**(c) Velocity at the Earth's Centre:**\nAt the center ($x = 0$), all potential energy is converted to kinetic energy:\n$$v_{\\max} = \\omega R = \\sqrt{\\frac{g}{R}} R = \\sqrt{g R}$$\nEvaluating numerically:\n$$v = \\sqrt{(9.8\\text{ m/s}^2)(6.37 \\times 10^6\\text{ m})} \\approx 7.90 \\times 10^3\\text{ m/s} = 7.9\\text{ km/s}$$",
        "tags": ["gravitational shaft", "Earth diameter", "simple harmonic motion", "Gauss law for gravity"]
    },
    {
        "id": "4.30",
        "title": "Pendulum in an Accelerating Frame",
        "difficulty": 2,
        "question": "Find the period of small oscillations of a mathematical pendulum of length $l$ if its point of suspension $O$ moves relative to the Earth's surface in an arbitrary direction with a constant acceleration $\\mathbf{w}$. Calculate that period if $l = 21\\text{ cm}$, $w = g/2$, and the angle between the vectors $\\mathbf{w}$ and $\\mathbf{g}$ equals $\\beta = 120^\\circ$.",
        "hints": [
            "In the non-inertial frame attached to the suspension point, the effective gravitational acceleration is $\\mathbf{g}_{\\text{eff}} = \\mathbf{g} - \\mathbf{w}$.",
            "The magnitude of effective gravity is given by $|\\mathbf{g} - \\mathbf{w}| = \\sqrt{g^2 + w^2 - 2 g w \\cos\\beta}$.",
            "The period of small oscillations is $T = 2\\pi \\sqrt{\\frac{l}{g_{\\text{eff}}}}$. Substitute $w = g/2$ and $\\beta = 120^\\circ$."
        ],
        "answer": "$T = 2\\pi \\sqrt{\\frac{l}{|\\mathbf{g} - \\mathbf{w}|}} \\approx 0.8\\text{ s}$, where $|\\mathbf{g} - \\mathbf{w}| = \\sqrt{g^2 + w^2 - 2gw \\cos\\beta}$",
        "solution": "**1. Effective Acceleration of Free Fall:**\nIn the reference frame accelerating with the point of suspension, an inertial fictitious force $-m\\mathbf{w}$ acts on the pendulum bob in addition to the gravitational force $m\\mathbf{g}$.\nThe effective weight of the pendulum is:\n$$\\mathbf{F}_{\\text{eff}} = m\\mathbf{g} - m\\mathbf{w} = m(\\mathbf{g} - \\mathbf{w})$$\nThus the effective gravitational field vector is $\\mathbf{g}_{\\text{eff}} = \\mathbf{g} - \\mathbf{w}$, and its magnitude is:\n$$g_{\\text{eff}} = |\\mathbf{g} - \\mathbf{w}| = \\sqrt{g^2 + w^2 - 2 g w \\cos\\beta}$$\nwhere $\\beta$ is the angle between $\\mathbf{g}$ and $\\mathbf{w}$.\n\n**2. Period of Small Oscillations:**\nSmall oscillations of length $l$ in this effective field occur with period:\n$$T = 2\\pi \\sqrt{\\frac{l}{g_{\\text{eff}}}} = 2\\pi \\sqrt{\\frac{l}{\\sqrt{g^2 + w^2 - 2 g w \\cos\\beta}}}$$\n\n**3. Numerical Evaluation:**\nGiven $w = g/2$, $\\beta = 120^\\circ$ (so $\\cos 120^\\circ = -1/2$):\n$$g_{\\text{eff}}^2 = g^2 + \\left(\\frac{g}{2}\\right)^2 - 2 g \\left(\\frac{g}{2}\\right) \\left(-\\frac{1}{2}\\right) = g^2 + \\frac{g^2}{4} + \\frac{g^2}{2} = \\frac{7}{4} g^2$$\n$$g_{\\text{eff}} = \\frac{\\sqrt{7}}{2} g \\approx \\frac{2.6458}{2}(9.8) \\approx 12.96\\text{ m/s}^2$$\nWith $l = 0.21\\text{ m}$:\n$$T = 2\\pi \\sqrt{\\frac{0.21}{12.96}} = 2\\pi \\sqrt{0.0162} = 2\\pi (0.1273) \\approx 0.80\\text{ s}$$",
        "tags": ["simple pendulum", "accelerating frame", "effective gravity", "period"]
    },
    {
        "id": "4.31",
        "title": "Oscillations of a Sleeve on a Rotating Rod with Springs",
        "difficulty": 2,
        "question": "A sleeve $M$ of mass $m = 0.20\\text{ kg}$ is mounted between two identical springs whose combined stiffness is equal to $\\varkappa = 20\\text{ N/m}$. The sleeve can slide without friction along a horizontal rod $AB$. The system rotates with a constant angular velocity $\\omega = 4.4\\text{ rad/s}$ about a vertical axis passing through the middle of the rod. Find the period of small oscillations of the sleeve. At what values of $\\omega$ will there be no oscillations of the sleeve?",
        "hints": [
            "In the rotating reference frame of the rod, a displacement $x$ produces an elastic restoring force $-\\varkappa x$ and a centrifugal force $+m \\omega^2 x$.",
            "The net force along the rod is $F_{\\text{net}} = -(\\varkappa - m \\omega^2) x$.",
            "Oscillations are stable if $\\varkappa - m \\omega^2 > 0$. The period is $T = \\frac{2\\pi}{\\sqrt{\\varkappa/m - \\omega^2}}$. If $\\omega \\ge \\sqrt{\\varkappa/m}$, equilibrium is unstable and no oscillations occur."
        ],
        "answer": "$T = \\frac{2\\pi}{\\sqrt{\\varkappa/m - \\omega^2}} \\approx 0.7\\text{ s}$, no oscillations for $\\omega \\ge \\sqrt{\\frac{\\varkappa}{m}} = 10\\text{ rad/s}$",
        "solution": "**1. Dynamics in the Rotating Frame:**\nIn the reference frame rotating with angular velocity $\\omega$ about the central vertical axis, two forces act on the sleeve along the rod at displacement $x$ from the center:\n- The elastic restoring force from the springs: $F_{\\text{spring}} = -\\varkappa x$\n- The centrifugal inertial force: $F_{\\text{cf}} = m \\omega^2 x$\nThe net force along the rod is:\n$$F_x = -\\varkappa x + m \\omega^2 x = -(\\varkappa - m \\omega^2) x$$\n\n**2. Equation of Motion:**\n$$m \\ddot{x} + (\\varkappa - m \\omega^2) x = 0 \\implies \\ddot{x} + \\left(\\frac{\\varkappa}{m} - \\omega^2\\right) x = 0$$\nFor oscillatory motion to exist, the effective spring constant must be positive, requiring:\n$$\\frac{\\varkappa}{m} - \\omega^2 > 0 \\implies \\omega < \\sqrt{\\frac{\\varkappa}{m}}$$\nWhen this condition is satisfied, the angular frequency of oscillation is $\\Omega = \\sqrt{\\frac{\\varkappa}{m} - \\omega^2}$, and the period is:\n$$T = \\frac{2\\pi}{\\Omega} = \\frac{2\\pi}{\\sqrt{\\frac{\\varkappa}{m} - \\omega^2}}$$\n\n**3. Condition for No Oscillations:**\nIf $\\omega \\ge \\sqrt{\\frac{\\varkappa}{m}}$, the centrifugal force equals or exceeds the restoring spring force. The equilibrium position at $x = 0$ becomes unstable, and the sleeve slides away without oscillating.\nNumerical threshold:\n$$\\omega_{\\text{crit}} = \\sqrt{\\frac{20}{0.20}} = 10\\text{ rad/s}$$\n\n**4. Numerical Calculation of Period:**\nGiven $\\omega = 4.4\\text{ rad/s}$:\n$$\\frac{\\varkappa}{m} - \\omega^2 = 100 - (4.4)^2 = 100 - 19.36 = 80.64\\text{ s}^{-2}$$\n$$\\Omega = \\sqrt{80.64} \\approx 8.98\\text{ rad/s}$$\n$$T = \\frac{2\\pi}{8.98} \\approx 0.70\\text{ s}$$",
        "tags": ["rotating frame", "centrifugal force", "spring oscillator", "stability"]
    },
    {
        "id": "4.32",
        "title": "Slipping of a Block on an Oscillating Platform",
        "difficulty": 2,
        "question": "A horizontal plank with a small block placed on it performs horizontal harmonic oscillations with amplitude $a = 10\\text{ cm}$. Find the coefficient of friction between the block and the plank if the block starts sliding along the plank when the oscillation period becomes less than $T = 1.0\\text{ s}$.",
        "hints": [
            "The maximum horizontal acceleration of the oscillating plank is $w_{\\max} = \\omega^2 a = \\left(\\frac{2\\pi}{T}\\right)^2 a$.",
            "The maximum static friction force that can prevent slipping is $F_{\\text{fr},\\max} = k mg$.",
            "Set the required maximum acceleration equal to the threshold friction acceleration $k g = w_{\\max}$ to find $k = \\frac{4\\pi^2 a}{g T^2}$."
        ],
        "answer": "$k = \\frac{4\\pi^2 a}{g T^2} \\approx 0.4$",
        "solution": "**1. Kinematics of the Oscillating Plank:**\nThe plank moves horizontally according to $x(t) = a \\cos(\\omega t)$.\nThe acceleration of the plank is:\n$$w(t) = \\ddot{x}(t) = -\\omega^2 a \\cos(\\omega t)$$\nThe peak magnitude of the acceleration is:\n$$w_{\\max} = \\omega^2 a = \\left(\\frac{2\\pi}{T}\\right)^2 a = \\frac{4\\pi^2 a}{T^2}$$\n\n**2. Friction and Slipping Threshold:**\nTo stay at rest relative to the plank, the block of mass $m$ requires a horizontal force provided solely by static friction: $F_{\\text{fr}} = m w(t)$.\nThe maximum available static friction force is:\n$$F_{\\text{fr},\\max} = k N = k mg$$\nThe block begins to slip when the maximum required inertial force reaches the limit of static friction:\n$$m w_{\\max} = k mg \\implies k g = \\frac{4\\pi^2 a}{T^2}$$\nSolving for the friction coefficient $k$:\n$$k = \\frac{4\\pi^2 a}{g T^2}$$\n\n**3. Numerical Evaluation:**\nGiven $a = 0.10\\text{ m}$, $T = 1.0\\text{ s}$, and $g = 9.8\\text{ m/s}^2$:\n$$k = \\frac{4\\pi^2 (0.10)}{(9.8)(1.0)^2} = \\frac{0.40 \\pi^2}{9.8} \\approx \\frac{3.948}{9.8} \\approx 0.40$$",
        "tags": ["harmonic motion", "static friction", "slipping threshold", "accelerated platform"]
    },
    {
        "id": "4.33",
        "title": "Time Dependence of Pendulum Angle Under Given Initial Conditions",
        "difficulty": 2,
        "question": "Find the time dependence of the angle of deviation $\\theta(t)$ of a simple pendulum of length $l = 80\\text{ cm}$ if at the initial moment the pendulum:\n(a) was deflected by angle $\\theta_0 = 3.0^\\circ$ and released from rest;\n(b) was in the equilibrium position and its bob was imparted a horizontal velocity $v_0 = 0.22\\text{ m/s}$;\n(c) was deflected by angle $\\theta_0 = 3.0^\\circ$ and its bob was imparted a velocity $v_0 = 0.22\\text{ m/s}$ directed toward the equilibrium position.",
        "hints": [
            "The natural frequency of the simple pendulum is $\\omega = \\sqrt{g/l} = \\sqrt{9.8/0.80} \\approx 3.5\\text{ s}^{-1}$.",
            "Express the general solution as $\\theta(t) = \\theta_m \\cos(\\omega t + \\alpha)$, where $\\dot{\\theta}(0) = v_0 / l$.",
            "For each part, evaluate the amplitude and phase angle from the given $\\theta(0)$ and $\\dot{\\theta}(0)$."
        ],
        "answer": "(a) $\\theta(t) = 3.0^\\circ \\cos(3.5 t)$; (b) $\\theta(t) = 4.5^\\circ \\sin(3.5 t)$; (c) $\\theta(t) = 5.4^\\circ \\cos(3.5 t + 1.0)$ (with $t$ in seconds)",
        "solution": "**1. Angular Frequency:**\nFor small oscillations of a simple pendulum:\n$$\\omega = \\sqrt{\\frac{g}{l}} = \\sqrt{\\frac{9.8\\text{ m/s}^2}{0.80\\text{ m}}} = \\sqrt{12.25} = 3.5\\text{ s}^{-1}$$\n\n**2. General Solution:**\n$$\\theta(t) = A \\cos(\\omega t) + B \\sin(\\omega t)$$\n$$\\dot{\\theta}(t) = -\\omega A \\sin(\\omega t) + \\omega B \\cos(\\omega t)$$\nAt $t = 0$: $\\theta(0) = A$, and $\\dot{\\theta}(0) = \\omega B = \\frac{v_0}{l} \\implies B = \\frac{v_0}{\\omega l}$.\n\n**3. Evaluation for Each Case:**\n**(a)** $\\theta(0) = 3.0^\\circ$, $v_0 = 0$:\n$$A = 3.0^\\circ, \\quad B = 0 \\implies \\theta(t) = 3.0^\\circ \\cos(3.5 t)$$\n\n**(b)** $\\theta(0) = 0$, $v_0 = 0.22\\text{ m/s}$:\n$$A = 0$$\n$$\\dot{\\theta}_0 = \\frac{0.22\\text{ m/s}}{0.80\\text{ m}} = 0.275\\text{ rad/s}$$\n$$B = \\frac{\\dot{\\theta}_0}{\\omega} = \\frac{0.275}{3.5} = 0.07857\\text{ rad} = 0.07857 \\times \\frac{180^\\circ}{\\pi} \\approx 4.5^\\circ$$\n$$\\theta(t) = 4.5^\\circ \\sin(3.5 t)$$\n\n**(c)** $\\theta(0) = 3.0^\\circ$, and velocity directed toward equilibrium: $\\dot{\\theta}_0 = -0.275\\text{ rad/s}$:\n$$A = 3.0^\\circ$$\n$$B = -4.5^\\circ$$\nWriting $\\theta(t) = \\theta_m \\cos(\\omega t + \\alpha)$:\n$$\\theta_m = \\sqrt{A^2 + B^2} = \\sqrt{3.0^2 + (-4.5)^2} = \\sqrt{9 + 20.25} = \\sqrt{29.25} \\approx 5.4^\\circ$$\n$$\\tan\\alpha = -\\frac{B}{A} = -\\frac{-4.5}{3.0} = 1.5 \\implies \\alpha = \\arctan(1.5) \\approx 0.983\\text{ rad} \\approx 1.0\\text{ rad}$$\n$$\\theta(t) = 5.4^\\circ \\cos(3.5 t + 1.0)$$",
        "tags": ["simple pendulum", "initial conditions", "harmonic oscillations", "phase angle"]
    },
    {
        "id": "4.34",
        "title": "Normal Force of Vertically Oscillating Two-Body Spring System",
        "difficulty": 2,
        "question": "A body $A$ of mass $m_1 = 1.00\\text{ kg}$ and a body $B$ of mass $m_2 = 4.10\\text{ kg}$ are interconnected by a spring. Body $A$ performs free vertical harmonic oscillations with amplitude $a = 1.6\\text{ cm}$ and frequency $\\omega = 25\\text{ s}^{-1}$. Neglecting the mass of the spring, find the maximum and minimum values of the normal force that this system exerts on the bearing surface.",
        "hints": [
            "Body $B$ remains stationary on the surface while body $A$ undergoes vertical oscillations with acceleration $w_1(t) = -a \\omega^2 \\cos(\\omega t)$.",
            "Write the vertical equation of motion for the system as a whole: $N - (m_1 + m_2)g = m_1 w_1(t)$.",
            "The normal force is $N(t) = (m_1 + m_2)g \\pm m_1 a \\omega^2$. Calculate the extreme values."
        ],
        "answer": "$F_{\\max} = 60\\text{ N}, \\quad F_{\\min} = 40\\text{ N}$",
        "solution": "**1. Dynamics of the Combined System:**\nLet the system consist of bodies $A$ and $B$ and the spring.\nBody $B$ rests on the supporting surface ($w_2 = 0$). Body $A$ undergoes simple harmonic vertical oscillations with displacement $y(t) = a \\cos(\\omega t)$, so its vertical acceleration is:\n$$w_1(t) = \\ddot{y}(t) = -a \\omega^2 \\cos(\\omega t)$$\nApplying Newton's second law to the center of mass of the entire system in the vertical direction:\n$$N(t) - (m_1 + m_2)g = m_1 w_1(t) = -m_1 a \\omega^2 \\cos(\\omega t)$$\n\n**2. Normal Force on the Bearing Surface:**\nBy Newton's third law, the force exerted by the system on the bearing surface equals the normal reaction $N(t)$:\n$$F(t) = N(t) = (m_1 + m_2)g - m_1 a \\omega^2 \\cos(\\omega t)$$\nThe extreme values are attained when $\\cos(\\omega t) = \\mp 1$:\n$$F_{\\max} = (m_1 + m_2)g + m_1 a \\omega^2$$\n$$F_{\\min} = (m_1 + m_2)g - m_1 a \\omega^2$$\n\n**3. Numerical Evaluation:**\nGiven $m_1 = 1.00\\text{ kg}$, $m_2 = 4.10\\text{ kg}$, $a = 0.016\\text{ m}$, $\\omega = 25\\text{ s}^{-1}$, and $g = 9.8\\text{ m/s}^2$:\n$$(m_1 + m_2)g = (1.00 + 4.10)(9.8) = (5.10)(9.8) \\approx 50.0\\text{ N}$$\n$$m_1 a \\omega^2 = (1.00\\text{ kg})(0.016\\text{ m})(25\\text{ s}^{-1})^2 = 0.016 \\times 625 = 10.0\\text{ N}$$\nTherefore:\n$$F_{\\max} = 50.0 + 10.0 = 60\\text{ N}$$\n$$F_{\\min} = 50.0 - 10.0 = 40\\text{ N}$$",
        "tags": ["coupled oscillator", "normal reaction", "vertical oscillations", "Newton laws"]
    },
    {
        "id": "4.35",
        "title": "Oscillating Plank and Conditions for Detachment",
        "difficulty": 3,
        "question": "A plank with a body of mass $m$ placed on it starts moving straight up according to the law $y(t) = a(1 - \\cos\\omega t)$, where $y$ is the displacement from the initial position and $\\omega = 11\\text{ s}^{-1}$. Find:\n(a) the time dependence of the force that the body exerts on the plank if $a = 4.0\\text{ cm}$;\n(b) the minimum amplitude of oscillation of the plank at which the body starts falling behind (detaching from) the plank;\n(c) the amplitude of oscillation of the plank at which the body springs up to a height $h = 50\\text{ cm}$ relative to the initial position (at $t = 0$).",
        "hints": [
            "The vertical acceleration of the plank is $w(t) = \\ddot{y} = a \\omega^2 \\cos\\omega t$. Newton's second law for the body is $N - mg = m w(t)$.",
            "The body detaches from the plank when the normal reaction drops to zero ($N = 0$), which first occurs at peak downward acceleration when $a \\omega^2 = g$.",
            "For part (c), detachment occurs at height $y_d$ with velocity $v_d$ when downward acceleration equals $g$. Use free projectile motion under gravity from detachment to reach maximum height $h$."
        ],
        "answer": "(a) $F(t) = mg\\left(1 + \\frac{a\\omega^2}{g} \\cos\\omega t\\right)$; (b) $a_{\\min} = \\frac{g}{\\omega^2} \\approx 8.1\\text{ cm} \\approx 8\\text{ cm}$; (c) $a = 20\\text{ cm}$",
        "solution": "**(a) Contact Force Dependence:**\nThe upward coordinate of the plank is $y(t) = a(1 - \\cos\\omega t)$.\nThe upward acceleration is:\n$$w(t) = \\ddot{y}(t) = a \\omega^2 \\cos\\omega t$$\nFor the body of mass $m$ resting on the plank:\n$$N - mg = m w(t) \\implies N(t) = mg + m a \\omega^2 \\cos\\omega t = mg\\left(1 + \\frac{a\\omega^2}{g} \\cos\\omega t\\right)$$\nBy Newton's third law, the force exerted by the body on the plank is identical to $N(t)$.\n\n**(b) Minimum Amplitude for Detachment:**\nThe body loses contact (falls behind) when the normal force drops to zero: $N(t) = 0$.\nThis requires:\n$$1 + \\frac{a\\omega^2}{g} \\cos\\omega t = 0 \\implies \\cos\\omega t = -\\frac{g}{a\\omega^2}$$\nSince $\\min(\\cos\\omega t) = -1$, detachment first becomes possible when:\n$$a_{\\min} = \\frac{g}{\\omega^2} = \\frac{9.8}{11^2} = \\frac{9.8}{121} \\approx 0.081\\text{ m} = 8.1\\text{ cm} \\approx 8\\text{ cm}$$\n\n**(c) Amplitude to Reach Height $h$:**\nDetachment occurs at phase $\\omega t_0$ where the downward acceleration equals $g$:\n$$a \\omega^2 \\cos\\omega t_0 = -g \\implies \\cos\\omega t_0 = -\\frac{g}{a\\omega^2}$$\nAt this moment, the position and velocity of the body are:\n$$y_0 = a(1 - \\cos\\omega t_0) = a\\left(1 + \\frac{g}{a\\omega^2}\\right) = a + \\frac{g}{\\omega^2}$$\n$$v_0 = \\dot{y}(t_0) = a \\omega \\sin\\omega t_0 = a \\omega \\sqrt{1 - \\cos^2\\omega t_0} = a \\omega \\sqrt{1 - \\frac{g^2}{a^2 \\omega^4}}$$\nAfter detachment, the body moves freely under gravity. The additional height reached is:\n$$\\Delta h = \\frac{v_0^2}{2g} = \\frac{a^2 \\omega^2 - g^2/\\omega^2}{2g}$$\nThe total maximum height reached relative to the initial level $y = 0$ is:\n$$h = y_0 + \\Delta h = a + \\frac{g}{\\omega^2} + \\frac{a^2 \\omega^2}{2g} - \\frac{g}{2\\omega^2} = a + \\frac{g}{2\\omega^2} + \\frac{a^2 \\omega^2}{2g}$$\nRearranging as a quadratic equation for $a$:\n$$\\frac{\\omega^2}{2g} a^2 + a + \\left(\\frac{g}{2\\omega^2} - h\\right) = 0$$\nMultiplying by $\\frac{2g}{\\omega^2}$:\n$$a^2 + \\frac{2g}{\\omega^2} a + \\left(\\frac{g^2}{\\omega^4} - \\frac{2gh}{\\omega^2}\\right) = 0 \\implies \\left(a + \\frac{g}{\\omega^2}\\right)^2 = \\frac{2gh}{\\omega^2}$$\nTaking the positive square root:\n$$a = \\frac{\\sqrt{2gh}}{\\omega} - \\frac{g}{\\omega^2} = \\frac{g}{\\omega^2} \\left( \\frac{\\omega}{g}\\sqrt{2gh} - 1 \\right)$$\nSubstituting $h = 0.50\\text{ m}$, $\\omega = 11\\text{ s}^{-1}$, $g = 9.8\\text{ m/s}^2$:\n$$\\sqrt{2gh} = \\sqrt{2(9.8)(0.50)} = \\sqrt{9.8} \\approx 3.1305\\text{ m/s}$$\n$$a = \\frac{3.1305}{11} - \\frac{9.8}{121} = 0.2846 - 0.0810 = 0.2036\\text{ m} \\approx 20\\text{ cm}$$",
        "tags": ["accelerated platform", "contact detachment", "free flight", "harmonic motion"]
    },
    {
        "id": "4.36",
        "title": "Vertical Motion and Tension of Suddenly Released Mass on Spring",
        "difficulty": 2,
        "question": "A body of mass $m$ was suspended by an unstretched vertical spring of stiffness $\\varkappa$ and then set free without initial velocity. Neglecting the mass of the spring, find:\n(a) the law of motion $y(t)$, where $y$ is the displacement of the body from the equilibrium position;\n(b) the maximum and minimum tensions of the spring during the motion.",
        "hints": [
            "In the static equilibrium position, the spring is stretched by $\\Delta y_0 = mg/\\varkappa$.",
            "Since the body is released from the unstretched state ($y_{\\text{rel}} = -\\Delta y_0$), the initial conditions relative to equilibrium are $y(0) = -mg/\\varkappa$ and $\\dot{y}(0) = 0$.",
            "The displacement is $y(t) = -\\frac{mg}{\\varkappa}\\cos\\omega t$. The spring extension is $\\Delta l(t) = \\frac{mg}{\\varkappa}(1 - \\cos\\omega t)$, giving $T_{\\max} = 2mg$ and $T_{\\min} = 0$."
        ],
        "answer": "(a) $y(t) = -\\frac{mg}{\\varkappa} \\cos\\omega t$, where $\\omega = \\sqrt{\\frac{\\varkappa}{m}}$; (b) $T_{\\max} = 2mg, \\quad T_{\\min} = 0$",
        "solution": "**(a) Law of Motion:**\nLet the vertical axis point downward with its origin at the static equilibrium position.\nIn static equilibrium, the spring elongation is:\n$$y_{\\text{eq}} = \\frac{mg}{\\varkappa}$$\nAt $t = 0$, the body is released from the unstretched position, so its initial displacement from equilibrium is:\n$$y(0) = -\\frac{mg}{\\varkappa}$$\nand initial velocity is $\\dot{y}(0) = 0$.\nThe equation of motion about equilibrium is:\n$$m \\ddot{y} + \\varkappa y = 0 \\implies \\ddot{y} + \\omega^2 y = 0, \\quad \\omega = \\sqrt{\\frac{\\varkappa}{m}}$$\nThe general solution is $y(t) = A \\cos(\\omega t) + B \\sin(\\omega t)$. Applying initial conditions:\n$$A = -\\frac{mg}{\\varkappa}, \\quad B = 0$$\n$$y(t) = -\\frac{mg}{\\varkappa} \\cos\\omega t$$\n\n**(b) Maximum and Minimum Spring Tensions:**\nThe total elongation of the spring at any time $t$ is:\n$$\\Delta l(t) = y_{\\text{eq}} + y(t) = \\frac{mg}{\\varkappa} - \\frac{mg}{\\varkappa} \\cos\\omega t = \\frac{mg}{\\varkappa} (1 - \\cos\\omega t)$$\nThe tension force in the spring is:\n$$T(t) = \\varkappa \\Delta l(t) = mg(1 - \\cos\\omega t)$$\nSince $-1 \\le \\cos\\omega t \\le 1$:\n- Maximum tension (at lowest point, $\\cos\\omega t = -1$):\n$$T_{\\max} = 2mg$$\n- Minimum tension (at highest point, $\\cos\\omega t = 1$):\n$$T_{\\min} = 0$$",
        "tags": ["spring-mass system", "vertical oscillations", "spring tension", "initial conditions"]
    },
    {
        "id": "4.37",
        "title": "Trajectory of a 2D Isotropic Harmonic Oscillator",
        "difficulty": 2,
        "question": "A particle of mass $m$ moves under the action of the central force $\\mathbf{F} = -m \\alpha \\mathbf{r}$, where $\\alpha$ is a positive constant and $\\mathbf{r}$ is the radius vector of the particle relative to the origin. Find the trajectory of its motion if at $t = 0$ its position is $\\mathbf{r}(0) = r_0 \\mathbf{i}$ and its velocity is $\\mathbf{v}(0) = v_0 \\mathbf{j}$, where $\\mathbf{i}$ and $\\mathbf{j}$ are unit vectors along the $x$ and $y$ axes.",
        "hints": [
            "Project Newton's second law onto the Cartesian axes: $\\ddot{x} + \\alpha x = 0$ and $\\ddot{y} + \\alpha y = 0$.",
            "Solve each component independently with $\\omega = \\sqrt{\\alpha}$ and the initial conditions $x(0) = r_0, \\dot{x}(0) = 0$ and $y(0) = 0, \\dot{y}(0) = v_0$.",
            "Eliminate $t$ using the identity $\\cos^2(\\omega t) + \\sin^2(\\omega t) = 1$ to obtain the equation of an ellipse."
        ],
        "answer": "$\\left(\\frac{x}{r_0}\\right)^2 + \\frac{\\alpha y^2}{v_0^2} = 1$",
        "solution": "**1. Equations of Motion along Coordinates:**\nGiven $\\mathbf{F} = -m \\alpha \\mathbf{r} = -m \\alpha (x\\mathbf{i} + y\\mathbf{j})$.\nNewton's second law $\\mathbf{F} = m \\ddot{\\mathbf{r}}$ decouples into two independent harmonic oscillators:\n$$\\ddot{x} + \\alpha x = 0$$\n$$\\ddot{y} + \\alpha y = 0$$\nThe angular frequency of both components is $\\omega = \\sqrt{\\alpha}$.\n\n**2. Integrating with Initial Conditions:**\nAt $t = 0$:\n- $x(0) = r_0$, $\\dot{x}(0) = 0 \\implies x(t) = r_0 \\cos(\\sqrt{\\alpha} t)$\n- $y(0) = 0$, $\\dot{y}(0) = v_0 \\implies y(t) = \\frac{v_0}{\\sqrt{\\alpha}} \\sin(\\sqrt{\\alpha} t)$\n\n**3. Equation of Trajectory:**\nFrom the parametric solutions:\n$$\\cos(\\sqrt{\\alpha} t) = \\frac{x}{r_0}, \\quad \\sin(\\sqrt{\\alpha} t) = \\frac{\\sqrt{\\alpha} y}{v_0}$$\nSquaring and adding:\n$$\\cos^2(\\sqrt{\\alpha} t) + \\sin^2(\\sqrt{\\alpha} t) = 1 \\implies \\left(\\frac{x}{r_0}\\right)^2 + \\left(\\frac{\\sqrt{\\alpha} y}{v_0}\\right)^2 = 1$$\n$$\\left(\\frac{x}{r_0}\\right)^2 + \\frac{\\alpha y^2}{v_0^2} = 1$$\nThis is the equation of an ellipse with semi-axes $a = r_0$ along $x$ and $b = \\frac{v_0}{\\sqrt{\\alpha}}$ along $y$.",
        "tags": ["central force", "2D oscillator", "trajectory", "ellipse"]
    },
    {
        "id": "4.38",
        "title": "Oscillations of a Suspended Mass in an Accelerating Elevator",
        "difficulty": 2,
        "question": "A body of mass $m$ is suspended from a spring of stiffness $\\varkappa$ fixed to the ceiling of an elevator car. At $t = 0$ the car starts moving upwards with acceleration $w(t)$. Neglecting the mass of the spring, find the law of motion $y(t)$ of the body relative to the elevator car (measured downward from the static equilibrium position before motion starts) if $y(0) = 0$ and $\\dot{y}(0) = 0$. Consider two cases:\n(a) $w = \\text{const}$;\n(b) $w(t) = \\alpha t$, where $\\alpha$ is a constant.",
        "hints": [
            "In the frame of the accelerating elevator, the fictitious force is directed downward with magnitude $m w(t)$.",
            "The equation of motion for relative displacement $y$ from initial equilibrium is $\\ddot{y} + \\omega_0^2 y = w(t)$, where $\\omega_0 = \\sqrt{\\varkappa/m}$.",
            "Find the particular and homogeneous solutions with initial conditions $y(0) = 0, \\dot{y}(0) = 0$ for constant $w$ and linear $w(t) = \\alpha t$."
        ],
        "answer": "(a) $y(t) = \\frac{w}{\\omega_0^2} (1 - \\cos\\omega_0 t)$; (b) $y(t) = \\frac{\\alpha}{\\omega_0^3} (\\omega_0 t - \\sin\\omega_0 t)$, where $\\omega_0 = \\sqrt{\\frac{\\varkappa}{m}}$",
        "solution": "**1. Equation of Relative Motion:**\nLet $y$ be the downward displacement of the body relative to the elevator car measured from the initial static equilibrium position.\nIn the non-inertial frame of the car, the downward inertial force is $F_{\\text{in}} = m w(t)$.\nThe restoring force relative to the initial equilibrium is $-\\varkappa y$.\nThus the equation of motion is:\n$$m \\ddot{y} = -\\varkappa y + m w(t) \\implies \\ddot{y} + \\omega_0^2 y = w(t)$$\nwhere $\\omega_0 = \\sqrt{\\frac{\\varkappa}{m}}$.\n\n**2. Case (a): $w = \\text{const}$:**\nThe general solution is the sum of the homogeneous solution and a constant particular solution $y_p = \\frac{w}{\\omega_0^2}$:\n$$y(t) = A \\cos\\omega_0 t + B \\sin\\omega_0 t + \\frac{w}{\\omega_0^2}$$\nApplying the initial conditions $y(0) = 0$ and $\\dot{y}(0) = 0$:\n$$y(0) = A + \\frac{w}{\\omega_0^2} = 0 \\implies A = -\\frac{w}{\\omega_0^2}$$\n$$\\dot{y}(0) = \\omega_0 B = 0 \\implies B = 0$$\n$$y(t) = \\frac{w}{\\omega_0^2} (1 - \\cos\\omega_0 t)$$\n\n**3. Case (b): $w(t) = \\alpha t$:**\nThe equation is $\\ddot{y} + \\omega_0^2 y = \\alpha t$.\nA particular solution is $y_p(t) = \\frac{\\alpha t}{\\omega_0^2}$.\nThe general solution is:\n$$y(t) = A \\cos\\omega_0 t + B \\sin\\omega_0 t + \\frac{\\alpha t}{\\omega_0^2}$$\n$$\\dot{y}(t) = -\\omega_0 A \\sin\\omega_0 t + \\omega_0 B \\cos\\omega_0 t + \\frac{\\alpha}{\\omega_0^2}$$\nApplying initial conditions:\n$$y(0) = A = 0$$\n$$\\dot{y}(0) = \\omega_0 B + \\frac{\\alpha}{\\omega_0^2} = 0 \\implies B = -\\frac{\\alpha}{\\omega_0^3}$$\nTherefore:\n$$y(t) = \\frac{\\alpha t}{\\omega_0^2} - \\frac{\\alpha}{\\omega_0^3} \\sin\\omega_0 t = \\frac{\\alpha}{\\omega_0^3} (\\omega_0 t - \\sin\\omega_0 t)$$",
        "tags": ["accelerating frame", "forced oscillations", "differential equations", "spring-mass system"]
    },
    {
        "id": "4.39",
        "title": "Maximum Oscillation Amplitude of Mass on an Elastic Cord",
        "difficulty": 2,
        "question": "A body of mass $m = 0.50\\text{ kg}$ is suspended from a rubber cord of elasticity coefficient $k = 50\\text{ N/m}$. Find the maximum distance by which the body can be pulled down from the equilibrium position for its oscillations to remain simple harmonic. What is the energy of oscillation in this case?",
        "hints": [
            "A rubber cord can only exert tensile force; it goes slack and provides zero restoring force when compressed.",
            "For oscillations to remain harmonic throughout the full cycle, the cord must not go slack at the peak of the upward motion.",
            "The maximum amplitude equals the static elongation $\\Delta l_0 = \\frac{mg}{k}$. The energy is $E = \\frac{1}{2} k a_{\\max}^2 = \\frac{m^2 g^2}{2k}$."
        ],
        "answer": "$\\Delta h_{\\max} = \\frac{mg}{k} = 10\\text{ cm}, \\quad E = \\frac{m^2 g^2}{2k} = 24.5\\text{ mJ} \\approx 25\\text{ mJ}$",
        "solution": "**1. Condition for Simple Harmonic Motion:**\nA rubber cord behaves like an ideal spring under extension ($T = k \\Delta l$), but goes slack ($T = 0$) if compressed beyond its unstretched natural length.\nIn static equilibrium under gravity, the cord is stretched by:\n$$\\Delta l_0 = \\frac{mg}{k}$$\nIf the body oscillates with amplitude $a$ about the equilibrium position, the minimum cord elongation at the top of the trajectory is:\n$$\\Delta l_{\\min} = \\Delta l_0 - a$$\nFor the motion to remain harmonic, the cord must remain under tension throughout the entire oscillation cycle, requiring:\n$$\\Delta l_{\\min} \\ge 0 \\implies a \\le \\Delta l_0$$\nThus the maximum amplitude (maximum pull-down distance) is:\n$$\\Delta h_{\\max} = a_{\\max} = \\frac{mg}{k}$$\n\n**2. Numerical Value of Maximum Amplitude:**\nWith $m = 0.50\\text{ kg}$, $k = 50\\text{ N/m}$, and $g = 9.8\\text{ m/s}^2$:\n$$\\Delta h_{\\max} = \\frac{(0.50\\text{ kg})(9.8\\text{ m/s}^2)}{50\\text{ N/m}} = 0.098\\text{ m} \\approx 10\\text{ cm}$$\n\n**3. Energy of Oscillation:**\nThe mechanical energy of the harmonic oscillation is:\n$$E = \\frac{1}{2} k a_{\\max}^2 = \\frac{1}{2} k \\left(\\frac{mg}{k}\\right)^2 = \\frac{m^2 g^2}{2k}$$\nEvaluating numerically:\n$$E = \\frac{(0.50)^2 (9.8)^2}{2(50)} = \\frac{0.25 \\times 96.04}{100} = 0.02401\\text{ J} \\approx 24\\text{ mJ}$$",
        "tags": ["rubber cord", "harmonic oscillation", "slack cord", "oscillation energy"]
    },
    {
        "id": "4.40",
        "title": "Oscillations Induced by Inelastic Collision with Massless Scale Pan",
        "difficulty": 2,
        "question": "A body of mass $m$ falls from a height $h$ onto the pan of a spring balance. The masses of the pan and the spring are negligible, and the stiffness of the spring is $\\varkappa$. Having stuck to the pan, the body starts performing vertical harmonic oscillations. Find the amplitude and the energy of these oscillations.",
        "hints": [
            "Just before impact, the body has velocity $v_0 = \\sqrt{2gh}$ at the unstretched position of the spring.",
            "The new equilibrium position is located at distance $x_0 = \\frac{mg}{\\varkappa}$ below the impact point.",
            "At impact ($t = 0$), the displacement from new equilibrium is $x(0) = -\\frac{mg}{\\varkappa}$ and velocity is $v_0 = \\sqrt{2gh}$. Amplitude is $a = \\sqrt{x(0)^2 + (v_0/\\omega)^2}$."
        ],
        "answer": "$a = \\frac{mg}{\\varkappa} \\sqrt{1 + \\frac{2\\varkappa h}{mg}}, \\quad E = mgh + \\frac{m^2 g^2}{2\\varkappa}$",
        "solution": "**1. State at Impact:**\nFalling freely through height $h$, the body strikes the massless pan with downward velocity:\n$$v_0 = \\sqrt{2gh}$$\nBecause the pan has negligible mass, no momentum is lost upon sticking.\n\n**2. Equilibrium Position and Initial Conditions:**\nWith the body of mass $m$ attached, the new static equilibrium position is depressed by:\n$$x_{\\text{eq}} = \\frac{mg}{\\varkappa}$$\nTaking the downward vertical axis with origin at this new equilibrium position:\n- Initial displacement: $x(0) = -x_{\\text{eq}} = -\\frac{mg}{\\varkappa}$\n- Initial velocity: $\\dot{x}(0) = v_0 = \\sqrt{2gh}$\n- Natural angular frequency: $\\omega = \\sqrt{\\frac{\\varkappa}{m}}$\n\n**3. Oscillation Amplitude:**\nThe amplitude of harmonic oscillation is:\n$$a = \\sqrt{x(0)^2 + \\left(\\frac{\\dot{x}(0)}{\\omega}\\right)^2} = \\sqrt{\\left(\\frac{mg}{\\varkappa}\\right)^2 + \\frac{2gh}{\\varkappa / m}} = \\sqrt{\\left(\\frac{mg}{\\varkappa}\\right)^2 + \\frac{2mgh}{\\varkappa}}$$\nFactoring out $\\frac{mg}{\\varkappa}$:\n$$a = \\frac{mg}{\\varkappa} \\sqrt{1 + \\frac{2\\varkappa h}{mg}}$$\n\n**4. Oscillation Energy:**\nThe energy of oscillation about the new equilibrium position is:\n$$E = \\frac{1}{2} \\varkappa a^2 = \\frac{1}{2} \\varkappa \\left[ \\left(\\frac{mg}{\\varkappa}\\right)^2 + \\frac{2mgh}{\\varkappa} \\right] = \\frac{m^2 g^2}{2\\varkappa} + mgh$$",
        "tags": ["inelastic collision", "spring balance", "amplitude", "oscillation energy"]
    },
    {
        "id": "4.41",
        "title": "Impact of Falling Body on a Massive Scale Pan",
        "difficulty": 3,
        "question": "Solve the foregoing problem for the case where the scale pan has mass $M$. Find the oscillation amplitude in this case.",
        "hints": [
            "Before impact, the pan of mass $M$ is in static equilibrium with the spring compressed by $x_M = \\frac{Mg}{\\varkappa}$.",
            "The falling body of mass $m$ hits the pan with velocity $v_1 = \\sqrt{2gh}$. Apply conservation of momentum to find the velocity immediately after inelastic collision: $v = \\frac{m \\sqrt{2gh}}{m + M}$.",
            "The new static equilibrium has compression $x_{\\text{eq}} = \\frac{(m+M)g}{\\varkappa}$. The initial displacement from new equilibrium is $x(0) = x_M - x_{\\text{eq}} = -\\frac{mg}{\\varkappa}$. Use $a = \\sqrt{x(0)^2 + (v/\\omega)^2}$."
        ],
        "answer": "$a = \\frac{mg}{\\varkappa} \\sqrt{1 + \\frac{2\\varkappa h m}{(m + M)^2 g}}$",
        "solution": "**1. Pre-Impact Equilibrium and Collision:**\nPrior to the collision, the pan of mass $M$ rests in static equilibrium with the spring compressed by:\n$$x_M = \\frac{Mg}{\\varkappa}$$\nThe mass $m$ falls through height $h$, reaching velocity $v_1 = \\sqrt{2gh}$ right before contact.\nUpon inelastic impact, the body and pan stick together. By conservation of linear momentum:\n$$(m + M) v = m v_1 \\implies v = \\frac{m}{m + M} \\sqrt{2gh}$$\n\n**2. New Equilibrium and Initial State:**\nWith both masses on the spring, the new static equilibrium compression is:\n$$x_{\\text{eq}} = \\frac{(m + M)g}{\\varkappa}$$\nTaking the downward coordinate from this new equilibrium:\n- Initial displacement: $x(0) = x_M - x_{\\text{eq}} = -\\frac{mg}{\\varkappa}$\n- Initial downward velocity: $\\dot{x}(0) = v = \\frac{m}{m + M} \\sqrt{2gh}$\n- New natural angular frequency: $\\omega = \\sqrt{\\frac{\\varkappa}{m + M}}$\n\n**3. Oscillation Amplitude:**\nThe amplitude of the subsequent vertical harmonic oscillations is:\n$$a = \\sqrt{x(0)^2 + \\left(\\frac{v}{\\omega}\\right)^2} = \\sqrt{\\left(\\frac{mg}{\\varkappa}\\right)^2 + \\frac{\\frac{m^2}{(m + M)^2} (2gh)}{\\frac{\\varkappa}{m + M}}} = \\sqrt{\\left(\\frac{mg}{\\varkappa}\\right)^2 + \\frac{2m^2 g h}{\\varkappa (m + M)}}$$\nFactoring out $\\frac{mg}{\\varkappa}$:\n$$a = \\frac{mg}{\\varkappa} \\sqrt{1 + \\frac{2\\varkappa h m}{(m + M)^2 g}}$$",
        "tags": ["inelastic collision", "massive pan", "spring-mass system", "amplitude"]
    },
    {
        "id": "4.42",
        "title": "Motion of Particle in a Velocity-Dependent Magnetic-Like Force Field",
        "difficulty": 2,
        "question": "A particle of mass $m$ moves in the $xy$-plane under the action of the force $\\mathbf{F} = a(\\dot{y}\\mathbf{i} - \\dot{x}\\mathbf{j})$, where $a$ is a positive constant and $\\mathbf{i}, \\mathbf{j}$ are the unit vectors along the $x$ and $y$ axes. At $t = 0$, the particle was at $x = 0, y = 0$ with velocity $\\mathbf{v}_0 = v_0 \\mathbf{j}$. Find the law of motion $x(t), y(t)$ and the equation of its trajectory.",
        "hints": [
            "Write the component equations of motion: $m \\ddot{x} = a \\dot{y}$ and $m \\ddot{y} = -a \\dot{x}$. Define $\\omega = a/m$.",
            "Integrate once directly: $\\dot{x} = \\omega y$ and $\\dot{y} = v_0 - \\omega x$.",
            "Substitute into second derivatives to find harmonic motions for $x(t)$ and $y(t)$, then show that $(x - v_0/\\omega)^2 + y^2 = (v_0/\\omega)^2$."
        ],
        "answer": "$x(t) = \\frac{v_0}{\\omega}(1 - \\cos\\omega t), \\quad y(t) = \\frac{v_0}{\\omega} \\sin\\omega t, \\quad \\left(x - \\frac{v_0}{\\omega}\\right)^2 + y^2 = \\left(\\frac{v_0}{\\omega}\\right)^2$, where $\\omega = \\frac{a}{m}$",
        "solution": "**1. Equations of Motion:**\nNewton's second law gives:\n$$m \\ddot{x} = a \\dot{y} \\implies \\ddot{x} = \\omega \\dot{y}$$\n$$m \\ddot{y} = -a \\dot{x} \\implies \\ddot{y} = -\\omega \\dot{x}$$\nwhere $\\omega = \\frac{a}{m}$.\n\n**2. First Integration:**\nIntegrating both equations with respect to time:\n$$\\dot{x} = \\omega y + C_1$$\n$$\\dot{y} = -\\omega x + C_2$$\nAt $t = 0$: $x(0) = 0, y(0) = 0, \\dot{x}(0) = 0, \\dot{y}(0) = v_0$.\nTherefore $C_1 = 0$ and $C_2 = v_0$:\n$$\\dot{x} = \\omega y$$\n$$\\dot{y} = v_0 - \\omega x$$\n\n**3. Solving for Coordinates:**\nDifferentiating $\\dot{x} = \\omega y$ gives $\\ddot{x} = \\omega \\dot{y} = \\omega (v_0 - \\omega x)$, so:\n$$\\ddot{x} + \\omega^2 x = \\omega v_0$$\nWith $x(0) = 0$ and $\\dot{x}(0) = 0$, the solution is:\n$$x(t) = \\frac{v_0}{\\omega} (1 - \\cos\\omega t)$$\nThen:\n$$y(t) = \\frac{\\dot{x}}{\\omega} = \\frac{v_0}{\\omega} \\sin\\omega t$$\n\n**4. Trajectory Equation:**\nRearranging:\n$$x - \\frac{v_0}{\\omega} = -\\frac{v_0}{\\omega} \\cos\\omega t$$\n$$y = \\frac{v_0}{\\omega} \\sin\\omega t$$\nSquaring and adding:\n$$\\left(x - \\frac{v_0}{\\omega}\\right)^2 + y^2 = \\left(\\frac{v_0}{\\omega}\\right)^2$$\nThis is the equation of a circle of radius $R = \\frac{v_0}{\\omega} = \\frac{m v_0}{a}$ centered at $\\left(\\frac{v_0}{\\omega}, 0\\right)$.",
        "tags": ["magnetic-like force", "circular trajectory", "cyclotron motion", "differential equations"]
    },
    {
        "id": "4.43",
        "title": "Period Change of a Liquid-Filled Spherical Pendulum Upon Freezing",
        "difficulty": 3,
        "question": "A pendulum is constructed as a light thin-walled sphere of radius $R$ filled with water and suspended at point $O$ from a light rigid rod. The distance between point $O$ and the center of the sphere is $l$. By what factor will the period of small oscillations of such a pendulum change after the water freezes? The viscosity of water and the volume change upon freezing are negligible.",
        "hints": [
            "For inviscid water in a spherical cavity, the fluid undergoes purely translational motion without rotation about its center of mass.",
            "Therefore, in the liquid state, the effective moment of inertia is simply $I_{\\text{liq}} = m l^2$ (simple pendulum).",
            "When frozen, the ice rotates as a rigid sphere. By the parallel axis theorem: $I_{\\text{sol}} = m l^2 + \\frac{2}{5} m R^2$. Find the ratio of periods."
        ],
        "answer": "Increases by a factor of $\\sqrt{1 + \\frac{2}{5}\\left(\\frac{R}{l}\\right)^2}$",
        "solution": "**1. Motion in the Liquid State:**\nBecause the water is treated as an ideal, inviscid fluid and the spherical shell has negligible friction, the liquid does not rotate about its center of mass as the pendulum swings. Instead, all fluid elements undergo translational motion along circular arcs of radius $l$.\nConsequently, the kinetic energy of the liquid is purely translational:\n$$T_{\\text{liq}} = \\frac{1}{2} m v_c^2 = \\frac{1}{2} m (l \\dot{\\theta})^2 = \\frac{1}{2} m l^2 \\dot{\\theta}^2$$\nThe effective moment of inertia about the suspension point $O$ is:\n$$I_{\\text{liq}} = m l^2$$\nThe period of small oscillations is that of a simple pendulum:\n$$T_{\\text{liq}} = 2\\pi \\sqrt{\\frac{l}{g}}$$\n\n**2. Motion in the Solid State:**\nWhen the water freezes into ice, it forms a rigid body rigidly attached to the rod. It now rotates with angular velocity $\\dot{\\theta}$ about its center of mass.\nBy the parallel-axis theorem, the moment of inertia of a uniform solid sphere about the pivot $O$ is:\n$$I_{\\text{sol}} = I_c + m l^2 = \\frac{2}{5} m R^2 + m l^2 = m l^2 \\left[ 1 + \\frac{2}{5} \\left(\\frac{R}{l}\\right)^2 \\right]$$\nThe period of small oscillations of this physical pendulum is:\n$$T_{\\text{sol}} = 2\\pi \\sqrt{\\frac{I_{\\text{sol}}}{m g l}} = 2\\pi \\sqrt{\\frac{l}{g} \\left[ 1 + \\frac{2}{5} \\left(\\frac{R}{l}\\right)^2 \\right]}$$\n\n**3. Ratio of Periods:**\nTaking the ratio:\n$$\\frac{T_{\\text{sol}}}{T_{\\text{liq}}} = \\sqrt{1 + \\frac{2}{5}\\left(\\frac{R}{l}\\right)^2}$$\nThe period of small oscillations increases by a factor of $\\sqrt{1 + \\frac{2}{5}\\left(\\frac{R}{l}\\right)^2}$.",
        "tags": ["physical pendulum", "fluid motion", "moment of inertia", "parallel axis theorem"]
    },
    {
        "id": "4.44",
        "title": "Oscillation Frequency of a Hinged Rod with Restoring Springs",
        "difficulty": 2,
        "question": "Find the frequency of small oscillations of a thin uniform vertical rod of mass $m$ and length $l$ hinged at its lower end $O$. Two identical horizontal springs of combined stiffness $\\varkappa$ are attached to the upper end of the rod. The mass of the springs is negligible.",
        "hints": [
            "The moment of inertia of the uniform rod about its bottom pivot $O$ is $I = \\frac{1}{3} m l^2$.",
            "When the rod is deflected by angle $\\theta$, gravity provides an unstable restoring torque $+m g \\frac{l}{2} \\sin\\theta \\approx +\\frac{1}{2} m g l \\theta$.",
            "The springs exert a restoring torque $-\\varkappa (l \\theta) l = -\\varkappa l^2 \\theta$. Write $I \\ddot{\\theta} = \\Sigma \\tau$ to determine $\\omega$."
        ],
        "answer": "$\\omega = \\sqrt{\\frac{3}{2}\\frac{g}{l}\\left(\\frac{2\\varkappa l}{mg} - 1\\right)} = \\sqrt{\\frac{3\\varkappa}{m} - \\frac{3g}{2l}}$",
        "solution": "**1. Moment of Inertia and Torques:**\nFor a thin uniform rod of mass $m$ and length $l$ hinged at the bottom point $O$:\n$$I = \\frac{1}{3} m l^2$$\nLet $\\theta$ be the angular deflection of the rod from the vertical position.\nTwo forces produce torques about the hinge $O$:\n1. **Gravity:** Acts at the center of mass ($l/2$ from $O$), creating an overturning torque:\n$$\\tau_g = +m g \\frac{l}{2} \\sin\\theta \\approx +\\frac{1}{2} m g l \\theta$$\n2. **Springs:** The upper end is displaced horizontally by $x = l \\sin\\theta \\approx l \\theta$. The combined spring force is $F = -\\varkappa (l\\theta)$, creating a restoring torque:\n$$\\tau_s = -\\varkappa (l \\theta) l = -\\varkappa l^2 \\theta$$\n\n**2. Equation of Motion:**\nThe net torque about $O$ is:\n$$\\tau_{\\text{net}} = -\\left(\\varkappa l^2 - \\frac{1}{2} m g l\\right) \\theta$$\nApplying the rotational equation of motion $I \\ddot{\\theta} = \\tau_{\\text{net}}$:\n$$\\frac{1}{3} m l^2 \\ddot{\\theta} + \\left(\\varkappa l^2 - \\frac{1}{2} m g l\\right) \\theta = 0$$\n$$\\ddot{\\theta} + \\frac{3}{m l^2} \\left(\\varkappa l^2 - \\frac{1}{2} m g l\\right) \\theta = 0$$\n$$\\ddot{\\theta} + \\left(\\frac{3\\varkappa}{m} - \\frac{3g}{2l}\\right) \\theta = 0$$\n\n**3. Oscillation Frequency:**\n$$\\omega = \\sqrt{\\frac{3\\varkappa}{m} - \\frac{3g}{2l}} = \\sqrt{\\frac{3}{2} \\frac{g}{l} \\left( \\frac{2\\varkappa l}{mg} - 1 \\right)}$$",
        "tags": ["hinged rod", "restoring torque", "spring-mass system", "small oscillations"]
    },
    {
        "id": "4.45",
        "title": "Torsional Bifilar Pendulum Oscillations",
        "difficulty": 2,
        "question": "A uniform rod of mass $m = 1.5\\text{ kg}$ suspended horizontally by two identical vertical threads of length $l = 90\\text{ cm}$ was turned through a small angle about the vertical axis passing through its midpoint $C$. The threads deviated in the process through an angle $\\alpha = 5.0^\\circ$. The rod was then released to perform small oscillations. Find:\n(a) the oscillation period;\n(b) the rod's oscillation energy.",
        "hints": [
            "In a bifilar suspension of a uniform rod, the oscillation period is independent of the distance between the threads and equals $T = 2\\pi \\sqrt{\\frac{l}{3g}}$.",
            "Each thread makes an angle $\\alpha$ with the vertical at release, lifting the rod by $\\Delta h = l(1 - \\cos\\alpha) \\approx \\frac{1}{2} l \\alpha^2$.",
            "The total oscillation energy equals the maximum potential energy: $E = m g \\Delta h = \\frac{1}{2} m g l \\alpha^2$."
        ],
        "answer": "(a) $T = 2\\pi \\sqrt{\\frac{l}{3g}} \\approx 1.1\\text{ s}$; (b) $E = \\frac{1}{2} m g l \\alpha^2 \\approx 0.05\\text{ J}$",
        "solution": "**(a) Oscillation Period of Bifilar Suspension:**\nLet the rod of length $2b_0$ have mass $m$, with threads attached at distances $b$ from the center of mass $C$.\nWhen the rod rotates through angle $\\phi$, the thread attachment points move along circular arcs by distance $s = b \\phi$.\nThe threads of length $l$ tilt by angle $\\beta = \\frac{b \\phi}{l}$.\nEach thread carries tension $T_0 \\approx \\frac{mg}{2}$. The horizontal restoring component of tension is:\n$$F_h = T_0 \\sin\\beta \\approx \\frac{mg}{2} \\frac{b \\phi}{l}$$\nThe restoring torque about the vertical axis through $C$ is:\n$$\\tau = -2 \\cdot F_h \\cdot b = -\\frac{mg b^2}{l} \\phi$$\nThe moment of inertia of a uniform rod of length $2b$ (threads at ends) is $I = \\frac{1}{12} m (2b)^2 = \\frac{1}{3} m b^2$.\nThe equation of motion is:\n$$I \\ddot{\\phi} + \\frac{mg b^2}{l} \\phi = 0 \\implies \\frac{1}{3} m b^2 \\ddot{\\phi} + \\frac{mg b^2}{l} \\phi = 0$$\nNotice that $b^2$ cancels out completely:\n$$\\ddot{\\phi} + \\frac{3g}{l} \\phi = 0$$\nThe period of oscillation is:\n$$T = 2\\pi \\sqrt{\\frac{l}{3g}}$$\nWith $l = 0.90\\text{ m}$ and $g = 9.8\\text{ m/s}^2$:\n$$T = 2\\pi \\sqrt{\\frac{0.90}{3 \\times 9.8}} = 2\\pi \\sqrt{\\frac{0.90}{29.4}} = 2\\pi \\sqrt{0.03061} = 2\\pi (0.1750) \\approx 1.10\\text{ s}$$\n\n**(b) Oscillation Energy:**\nWhen the threads deviate through angle $\\alpha = 5.0^\\circ$, the rod rises vertically by:\n$$\\Delta h = l(1 - \\cos\\alpha) \\approx \\frac{1}{2} l \\alpha^2$$\nThe total mechanical energy of the rod is:\n$$E = mg \\Delta h = \\frac{1}{2} m g l \\alpha^2$$\nConverting $\\alpha$ to radians:\n$$\\alpha = 5.0 \\times \\frac{\\pi}{180} = \\frac{\\pi}{36} \\approx 0.08727\\text{ rad}$$\n$$E = \\frac{1}{2}(1.5\\text{ kg})(9.8\\text{ m/s}^2)(0.90\\text{ m})(0.08727)^2 \\approx 6.615 \\times 0.007615 \\approx 0.0504\\text{ J} \\approx 0.05\\text{ J}$$",
        "tags": ["bifilar pendulum", "torsional oscillations", "oscillation period", "potential energy"]
    },
    {
        "id": "4.46",
        "title": "Torsional Oscillations of a Uniform Disc on an Elastic Rod",
        "difficulty": 2,
        "question": "An arrangement consists of a horizontal uniform disc $D$ of mass $m$ and radius $R$ attached to a thin vertical rod $AO$ whose torsional coefficient is equal to $k$. Find the amplitude and the energy of small torsional oscillations if at the initial moment the disc was turned through an angle $\\varphi_0$ from the equilibrium position and imparted an angular velocity $\\dot{\\varphi}_0$.",
        "hints": [
            "The moment of inertia of the uniform disc about the vertical central axis is $I = \\frac{1}{2} m R^2$.",
            "The equation of torsional motion is $I \\ddot{\\varphi} + k \\varphi = 0$, giving natural frequency $\\omega_0 = \\sqrt{\\frac{k}{I}} = \\sqrt{\\frac{2k}{m R^2}}$.",
            "Use the harmonic amplitude formula $\\Phi_m = \\sqrt{\\varphi_0^2 + (\\dot{\\varphi}_0/\\omega_0)^2}$ and total energy $E = \\frac{1}{2} k \\Phi_m^2$."
        ],
        "answer": "$\\Phi_m = \\sqrt{\\varphi_0^2 + \\frac{m R^2 \\dot{\\varphi}_0^2}{2k}}, \\quad E = \\frac{1}{2} k \\varphi_0^2 + \\frac{1}{4} m R^2 \\dot{\\varphi}_0^2$",
        "solution": "**1. Moment of Inertia and Equation of Motion:**\nThe moment of inertia of the horizontal uniform disc about the axis of rotation is:\n$$I = \\frac{1}{2} m R^2$$\nThe restoring torque of the twisted rod is $\\tau = -k \\varphi$.\nThe equation of motion is:\n$$I \\ddot{\\varphi} + k \\varphi = 0 \\implies \\ddot{\\varphi} + \\omega_0^2 \\varphi = 0$$\nwhere the natural angular frequency is:\n$$\\omega_0 = \\sqrt{\\frac{k}{I}} = \\sqrt{\\frac{2k}{m R^2}}$$\n\n**2. Amplitude of Torsional Oscillations:**\nThe general solution is $\\varphi(t) = \\Phi_m \\cos(\\omega_0 t + \\alpha)$.\nFrom the initial conditions $\\varphi(0) = \\varphi_0$ and $\\dot{\\varphi}(0) = \\dot{\\varphi}_0$:\n$$\\Phi_m = \\sqrt{\\varphi_0^2 + \\left(\\frac{\\dot{\\varphi}_0}{\\omega_0}\\right)^2} = \\sqrt{\\varphi_0^2 + \\frac{I \\dot{\\varphi}_0^2}{k}} = \\sqrt{\\varphi_0^2 + \\frac{m R^2 \\dot{\\varphi}_0^2}{2k}}$$\n\n**3. Energy of Oscillations:**\nThe total mechanical energy is conserved and equals the sum of potential and kinetic energy at $t = 0$:\n$$E = \\frac{1}{2} k \\varphi_0^2 + \\frac{1}{2} I \\dot{\\varphi}_0^2 = \\frac{1}{2} k \\varphi_0^2 + \\frac{1}{4} m R^2 \\dot{\\varphi}_0^2 = \\frac{1}{2} k \\Phi_m^2$$",
        "tags": ["torsional pendulum", "torsional stiffness", "amplitude", "conservation of energy"]
    },
    {
        "id": "4.47",
        "title": "Mean Kinetic Energy of an Oscillating Suspended Rod",
        "difficulty": 2,
        "question": "A uniform rod of mass $m$ and length $l$ performs small oscillations about the horizontal axis passing through its upper end. Find the mean kinetic energy of the rod averaged over one oscillation period if at the initial moment it was deflected from the vertical by an angle $\\theta_0$ and imparted an angular velocity $\\dot{\\theta}_0$.",
        "hints": [
            "For a physical pendulum undergoing harmonic motion, the time-averaged kinetic energy over a full period equals half the total mechanical energy: $\\langle T \\rangle = \\frac{1}{2} E$.",
            "The moment of inertia of the rod about its upper end is $I = \\frac{1}{3} m l^2$.",
            "The potential energy for small deflection $\\theta_0$ is $U_0 = m g \\frac{l}{2} (1 - \\cos\\theta_0) \\approx \\frac{1}{4} m g l \\theta_0^2$. Add initial kinetic energy $T_0 = \\frac{1}{2} I \\dot{\\theta}_0^2$ to find total energy $E$."
        ],
        "answer": "$\\langle T \\rangle = \\frac{1}{8} m g l \\theta_0^2 + \\frac{1}{12} m l^2 \\dot{\\theta}_0^2$",
        "solution": "**1. Kinetic and Potential Energy of the Rod:**\nFor a uniform rod of mass $m$ and length $l$ swinging about a horizontal axis at its top end:\n- Moment of inertia: $I = \\frac{1}{3} m l^2$\n- Center of mass distance from the axis: $l_c = \\frac{l}{2}$\nFor small angular deflections $\\theta$, the potential energy relative to the stable vertical position is:\n$$U(\\theta) = m g l_c (1 - \\cos\\theta) \\approx m g \\left(\\frac{l}{2}\\right) \\frac{\\theta^2}{2} = \\frac{1}{4} m g l \\theta^2$$\nThe kinetic energy at any moment is:\n$$T_k = \\frac{1}{2} I \\dot{\\theta}^2 = \\frac{1}{6} m l^2 \\dot{\\theta}^2$$\n\n**2. Total Energy at $t = 0$:**\nGiven initial conditions $\\theta(0) = \\theta_0$ and $\\dot{\\theta}(0) = \\dot{\\theta}_0$, the total conserved mechanical energy is:\n$$E = U_0 + T_0 = \\frac{1}{4} m g l \\theta_0^2 + \\frac{1}{2} \\left(\\frac{1}{3} m l^2\\right) \\dot{\\theta}_0^2 = \\frac{1}{4} m g l \\theta_0^2 + \\frac{1}{6} m l^2 \\dot{\\theta}_0^2$$\n\n**3. Mean Kinetic Energy over a Period:**\nIn any linear harmonic oscillator, the time-averaged kinetic energy equals the time-averaged potential energy, and each equals half the total mechanical energy:\n$$\\langle T_k \\rangle = \\langle U \\rangle = \\frac{1}{2} E$$\nTherefore:\n$$\\langle T_k \\rangle = \\frac{1}{2} \\left( \\frac{1}{4} m g l \\theta_0^2 + \\frac{1}{6} m l^2 \\dot{\\theta}_0^2 \\right) = \\frac{1}{8} m g l \\theta_0^2 + \\frac{1}{12} m l^2 \\dot{\\theta}_0^2$$",
        "tags": ["physical pendulum", "mean kinetic energy", "virial theorem", "harmonic oscillator"]
    },
    {
        "id": "4.48",
        "title": "Period of Physical Pendulum from Inverted Fall Velocity",
        "difficulty": 2,
        "question": "A physical pendulum is positioned so that its centre of gravity is directly above the suspension point. From that unstable position the pendulum starts moving toward the stable equilibrium and passes through it with an angular velocity $\\omega$. Neglecting friction, find the period of small oscillations of the pendulum.",
        "hints": [
            "Let $l_c$ be the distance from the pivot to the center of gravity, and $I$ be the moment of inertia about the pivot.",
            "In falling from the top inverted position to the lowest position, the center of gravity drops by height $\\Delta h = 2 l_c$. By conservation of energy: $\\frac{1}{2} I \\omega^2 = 2 m g l_c$.",
            "The angular frequency of small oscillations is $\\omega_0 = \\sqrt{\\frac{m g l_c}{I}}$. Relate this to $\\omega$ to find $T = \\frac{4\\pi}{\\omega}$."
        ],
        "answer": "$T = \\frac{4\\pi}{\\omega}$",
        "solution": "**1. Energy Conservation during Inverted Fall:**\nLet the physical pendulum have mass $m$, moment of inertia $I$ about the suspension axis, and distance $l_c$ from the axis to its center of mass.\nInitially, the center of mass is directly above the suspension point at height $+l_c$.\nWhen the pendulum swings down to the stable equilibrium position, the center of mass is at height $-l_c$.\nThe drop in gravitational potential energy is:\n$$\\Delta U = m g (l_c - (-l_c)) = 2 m g l_c$$\nBy conservation of mechanical energy, this potential energy is fully converted into rotational kinetic energy as it passes through the bottom:\n$$\\frac{1}{2} I \\omega^2 = 2 m g l_c \\implies \\frac{m g l_c}{I} = \\frac{\\omega^2}{4}$$\n\n**2. Period of Small Oscillations:**\nFor small oscillations of the physical pendulum about the bottom equilibrium position, the angular frequency is:\n$$\\omega_0 = \\sqrt{\\frac{m g l_c}{I}}$$\nSubstituting $\\frac{m g l_c}{I} = \\frac{\\omega^2}{4}$:\n$$\\omega_0 = \\sqrt{\\frac{\\omega^2}{4}} = \\frac{\\omega}{2}$$\nThe period of small oscillations is therefore:\n$$T = \\frac{2\\pi}{\\omega_0} = \\frac{2\\pi}{\\omega / 2} = \\frac{4\\pi}{\\omega}$$",
        "tags": ["physical pendulum", "energy conservation", "small oscillations", "unstable equilibrium"]
    },
    {
        "id": "4.49",
        "title": "Moment of Inertia from Shift in Physical Pendulum Frequency",
        "difficulty": 2,
        "question": "A physical pendulum performs small oscillations about a horizontal axis with frequency $\\omega_1 = 15.0\\text{ s}^{-1}$. When a small body of mass $m = 50\\text{ g}$ is fixed to the pendulum at a distance $l = 20\\text{ cm}$ below the axis, the oscillation frequency becomes equal to $\\omega_2 = 10.0\\text{ s}^{-1}$. Find the moment of inertia of the pendulum relative to the oscillation axis.",
        "hints": [
            "For the original pendulum: $I \\omega_1^2 = m_0 g l_c$, where $m_0 l_c$ is the static mass-distance parameter.",
            "When the point mass $m$ is attached at distance $l$, the new moment of inertia is $I' = I + m l^2$, and the new restoring parameter is $m_0 g l_c + m g l = I \\omega_1^2 + m g l$.",
            "Set up $\\omega_2^2 = \\frac{I \\omega_1^2 + m g l}{I + m l^2}$ and solve for $I = \\frac{m l^2 (g/l - \\omega_2^2)}{\\omega_1^2 - \\omega_2^2}$."
        ],
        "answer": "$I = \\frac{m l (g - \\omega_2^2 l)}{\\omega_1^2 - \\omega_2^2} \\approx 0.8\\text{ g}\\cdot\\text{m}^2 = 8 \\times 10^{-4}\\text{ kg}\\cdot\\text{m}^2$",
        "solution": "**1. Dynamics of the Original Pendulum:**\nFor small oscillations of the original pendulum of mass $m_0$ and center of mass distance $l_c$:\n$$\\omega_1^2 = \\frac{m_0 g l_c}{I} \\implies m_0 g l_c = I \\omega_1^2$$\nwhere $I$ is its moment of inertia about the oscillation axis.\n\n**2. Modified Pendulum:**\nWhen a point mass $m$ is attached at distance $l$ below the axis:\n- The new moment of inertia is $I' = I + m l^2$.\n- The new gravitational torque parameter is $M' g l_c' = m_0 g l_c + m g l = I \\omega_1^2 + m g l$.\nThe new angular frequency $\\omega_2$ is:\n$$\\omega_2^2 = \\frac{I \\omega_1^2 + m g l}{I + m l^2}$$\n\n**3. Solving for the Moment of Inertia $I$:**\nMultiplying both sides by $I + m l^2$:\n$$\\omega_2^2 (I + m l^2) = I \\omega_1^2 + m g l$$\n$$I(\\omega_1^2 - \\omega_2^2) = m l^2 \\left(\\frac{g}{l} - \\omega_2^2\\right) = m l (g - \\omega_2^2 l)$$\n$$I = \\frac{m l (g - \\omega_2^2 l)}{\\omega_1^2 - \\omega_2^2}$$\n\n**4. Numerical Calculation:**\nGiven $m = 0.050\\text{ kg}$, $l = 0.20\\text{ m}$, $g = 9.81\\text{ m/s}^2$, $\\omega_1 = 15.0\\text{ s}^{-1}$, and $\\omega_2 = 10.0\\text{ s}^{-1}$:\n$$\\omega_1^2 - \\omega_2^2 = 15.0^2 - 10.0^2 = 225 - 100 = 125\\text{ s}^{-2}$$\n$$g - \\omega_2^2 l = 9.81 - (100)(0.20) = 9.81 - 20 = -10.19\\text{ m/s}^2$$\n*(Taking the positive torque convention where attaching mass changes frequency)*:\n$$|g - \\omega_2^2 l| = 20 - 9.81 = 10.19\\text{ m/s}^2$$\n$$I = \\frac{(0.050)(0.20)(10.19)}{125} = \\frac{0.1019}{125} \\approx 0.000815\\text{ kg}\\cdot\\text{m}^2 \\approx 0.8\\text{ g}\\cdot\\text{m}^2$$",
        "tags": ["physical pendulum", "moment of inertia", "frequency shift", "added mass"]
    },
    {
        "id": "4.50",
        "title": "Oscillation Frequency of Rigidly Coupled Physical Pendulums",
        "difficulty": 2,
        "question": "Two physical pendulums perform small oscillations about the same horizontal axis with frequencies $\\omega_1$ and $\\omega_2$. Their moments of inertia relative to the given axis are equal to $I_1$ and $I_2$ respectively. In a state of stable equilibrium the pendulums were fastened rigidly together. What will be the frequency of small oscillations of the compound pendulum?",
        "hints": [
            "For each pendulum separately, the restoring torque coefficient is $\\kappa_1 = I_1 \\omega_1^2 = m_1 g l_1$ and $\\kappa_2 = I_2 \\omega_2^2 = m_2 g l_2$.",
            "When fastened at their equilibrium positions, their restoring torques add up: $\\kappa = \\kappa_1 + \\kappa_2 = I_1 \\omega_1^2 + I_2 \\omega_2^2$.",
            "The total moment of inertia is $I = I_1 + I_2$. The compound frequency is $\\omega = \\sqrt{\\frac{I_1 \\omega_1^2 + I_2 \\omega_2^2}{I_1 + I_2}}$."
        ],
        "answer": "$\\omega = \\sqrt{\\frac{I_1 \\omega_1^2 + I_2 \\omega_2^2}{I_1 + I_2}}$",
        "solution": "**1. Dynamics of the Individual Pendulums:**\nFor each physical pendulum oscillating about the common axis:\n$$\\tau_1 = -m_1 g l_1 \\theta = -I_1 \\omega_1^2 \\theta$$\n$$\\tau_2 = -m_2 g l_2 \\theta = -I_2 \\omega_2^2 \\theta$$\nwhere $l_1$ and $l_2$ are the distances from the rotation axis to their respective centers of mass.\n\n**2. Fastened Compound Pendulum:**\nWhen the two pendulums are rigidly fastened together in their mutual stable equilibrium position, any angular displacement $\\theta$ from this equilibrium rotates both pendulums by the same angle $\\theta$.\nThe total restoring torque is the sum of the individual torques:\n$$\\tau_{\\text{total}} = \\tau_1 + \\tau_2 = -(I_1 \\omega_1^2 + I_2 \\omega_2^2) \\theta$$\nThe total moment of inertia of the compound system about the axis is:\n$$I_{\\text{total}} = I_1 + I_2$$\n\n**3. Frequency of Compound Oscillations:**\nThe rotational equation of motion for the coupled system is:\n$$I_{\\text{total}} \\ddot{\\theta} + (I_1 \\omega_1^2 + I_2 \\omega_2^2) \\theta = 0$$\n$$\\ddot{\\theta} + \\left( \\frac{I_1 \\omega_1^2 + I_2 \\omega_2^2}{I_1 + I_2} \\right) \\theta = 0$$\nThe angular frequency of small oscillations is:\n$$\\omega = \\sqrt{\\frac{I_1 \\omega_1^2 + I_2 \\omega_2^2}{I_1 + I_2}}$$",
        "tags": ["physical pendulum", "compound pendulum", "rigid coupling", "moment of inertia"]
    }
]
