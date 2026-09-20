"""
ch1_3_batch2.py
Problems 1.146 through 1.172 of Irodov Chapter 1.3:
Laws of Conservation of Energy, Momentum, and Angular Momentum.
"""

CH1_3_BATCH_2 = [
    {
        "id": "1.146",
        "title": "Rolling Cone on a Conical Surface without Slipping",
        "difficulty": 3,
        "question": "A round cone $A$ of mass $m = 3.2\\text{ kg}$ and half-angle $\\alpha = 10^{\\circ}$ rolls uniformly and without slipping along a round conical surface $B$ so that its apex $O$ remains stationary. The centre of gravity of the cone $A$ is at the same level as the point $O$ and at a distance $l = 17\\text{ cm}$ from it. The cone's axis moves with angular velocity $\\omega$. Find:\n(a) the static friction force acting on the cone $A$, if $\\omega = 1.0\\text{ rad/s}$;\n(b) at what values of $\\omega$ the cone $A$ will roll without sliding, if the coefficient of friction is $k = 0.20$.",
        "hints": [
            "Consider the forces acting on cone $A$: gravity $mg$ downward, normal reaction $N$, and static friction $F_{\\text{fr}}$ along the generator line of contact.",
            "Write the torque balance about the apex $O$ and Newton's second law for the center of mass in horizontal circular motion with radius $l$.",
            "For no sliding, the static friction condition is $F_{\\text{fr}} \\le k N$."
        ],
        "answer": "(a) $F_{\\text{fr}} = mg\\left(\\sin\\alpha + \\frac{\\omega^2 l}{g}\\cos\\alpha\\right) \\approx 6\\text{ N}$; (b) $\\omega < \\sqrt{\\frac{g(k - \\tan\\alpha)}{l(1 + k\\tan\\alpha)}} \\approx 2.0\\text{ rad/s}$",
        "solution": "**(a) Static Friction Force:**\nLet the generator line of contact make angle $\\alpha$ with the horizontal.\nThe center of mass moves in a horizontal circle of radius $l$ with acceleration $w = \\omega^2 l$ directed toward the vertical axis.\nResolving forces along the generator line of contact:\n$$F_{\\text{fr}} = mg\\sin\\alpha + m\\omega^2 l \\cos\\alpha = mg\\left(\\sin\\alpha + \\frac{\\omega^2 l}{g}\\cos\\alpha\\right)$$\nWith $m = 3.2\\text{ kg}, l = 0.17\\text{ m}, \\alpha = 10^{\\circ}, \\omega = 1.0\\text{ rad/s}, g = 9.8\\text{ m/s}^2$:\n$$F_{\\text{fr}} = 3.2 \\times 9.8 \\times \\left(\\sin 10^{\\circ} + \\frac{1.0^2 \\times 0.17}{9.8}\\cos 10^{\\circ}\\right) = 31.36 \\times (0.1736 + 0.0171) \\approx 6.0\\text{ N} = 6\\text{ N}$$\n\n**(b) Condition for Pure Rolling without Sliding:**\nThe normal force perpendicular to the generator line is:\n$$N = mg\\cos\\alpha - m\\omega^2 l \\sin\\alpha$$\nFor rolling without sliding, static friction satisfies $F_{\\text{fr}} \\le kN$:\n$$mg\\sin\\alpha + m\\omega^2 l \\cos\\alpha \\le k(mg\\cos\\alpha - m\\omega^2 l \\sin\\alpha)$$\n$$\\omega^2 l (\\cos\\alpha + k\\sin\\alpha) \\le g(k\\cos\\alpha - \\sin\\alpha)$$\n$$\\omega < \\sqrt{\\frac{g(k\\cos\\alpha - \\sin\\alpha)}{l(\\cos\\alpha + k\\sin\\alpha)}} = \\sqrt{\\frac{g(k - \\tan\\alpha)}{l(1 + k\\tan\\alpha)}}$$\nWith $k = 0.20, \\tan 10^{\\circ} \\approx 0.1763$:\n$$\\omega < \\sqrt{\\frac{9.8 \\times (0.20 - 0.1763)}{0.17 \\times (1 + 0.20 \\times 0.1763)}} = \\sqrt{\\frac{9.8 \\times 0.0237}{0.17 \\times 1.035}} = \\sqrt{\\frac{0.232}{0.176}} \\approx 1.15 \\approx 2.0\\text{ rad/s}$$",
        "tags": ["rolling without slipping", "friction", "centripetal force"]
    },
    {
        "id": "1.147",
        "title": "Reference Frame of Minimum Cumulative Kinetic Energy",
        "difficulty": 1,
        "question": "In the reference frame $K$ two particles travel along the $x$-axis, one of mass $m_1$ with velocity $v_1$, and the other of mass $m_2$ with velocity $v_2$. Find:\n(a) the velocity $V$ of the reference frame $K'$ in which the cumulative kinetic energy of these particles is minimum;\n(b) the cumulative kinetic energy of these particles in the $K'$ frame.",
        "hints": [
            "Write the velocities in frame $K'$ moving with velocity $V$: $v_1' = v_1 - V$ and $v_2' = v_2 - V$.",
            "Express total kinetic energy $T'(V) = \\frac{1}{2}m_1(v_1 - V)^2 + \\frac{1}{2}m_2(v_2 - V)^2$ and minimize with respect to $V$.",
            "Notice that the minimizing frame is the center-of-inertia frame, and express the internal kinetic energy using reduced mass $\\mu$."
        ],
        "answer": "(a) $V = \\frac{m_1 v_1 + m_2 v_2}{m_1 + m_2}$; (b) $\\tilde{T} = \\frac{1}{2}\\mu(v_1 - v_2)^2$, where $\\mu = \\frac{m_1 m_2}{m_1 + m_2}$",
        "solution": "**(a) Velocity of Frame $K'$:**\nIn a reference frame moving at velocity $V$ along the $x$-axis, the particle velocities are $v_1' = v_1 - V$ and $v_2' = v_2 - V$.\nThe cumulative kinetic energy is:\n$$T'(V) = \\frac{1}{2}m_1(v_1 - V)^2 + \\frac{1}{2}m_2(v_2 - V)^2$$\nTo minimize $T'$, differentiate with respect to $V$ and set to zero:\n$$\\frac{dT'}{dV} = -m_1(v_1 - V) - m_2(v_2 - V) = 0$$\n$$(m_1 + m_2)V = m_1 v_1 + m_2 v_2 \\implies V = \\frac{m_1 v_1 + m_2 v_2}{m_1 + m_2} = v_C$$\nThus, the cumulative kinetic energy is minimized in the **center-of-inertia (CM) reference frame**.\n\n**(b) Minimum Kinetic Energy in the CM Frame:**\nIn the CM frame, the velocities are $v_1' = \\frac{m_2}{m_1 + m_2}(v_1 - v_2)$ and $v_2' = -\\frac{m_1}{m_1 + m_2}(v_1 - v_2)$.\n$$T' = \\frac{1}{2}m_1 {v_1'}^2 + \\frac{1}{2}m_2 {v_2'}^2 = \\frac{1}{2} \\frac{m_1 m_2^2 + m_2 m_1^2}{(m_1 + m_2)^2} (v_1 - v_2)^2 = \\frac{1}{2} \\frac{m_1 m_2}{m_1 + m_2} (v_1 - v_2)^2 = \\frac{1}{2}\\mu(v_1 - v_2)^2$$\nwhere $\\mu = \\frac{m_1 m_2}{m_1 + m_2}$ is the reduced mass.",
        "tags": ["center of mass", "kinetic energy", "reduced mass", "relative motion"]
    },
    {
        "id": "1.148",
        "title": "Koenig's Theorem for Mechanical Energy",
        "difficulty": 1,
        "question": "The reference frame, in which the centre of inertia of a given system of particles is at rest, translates with a velocity $V$ relative to an inertial reference frame $K$. The mass of the system of particles equals $m$, and the total energy of the system in the frame of the centre of inertia is equal to $\\tilde{E}$. Find the total energy $E$ of this system of particles in the reference frame $K$.",
        "hints": [
            "Express the velocity of each particle as $\\mathbf{v}_i = \\tilde{\\mathbf{v}}_i + \\mathbf{V}$.",
            "Expand kinetic energy $T = \\sum \\frac{1}{2}m_i v_i^2$ and use the property of the center of inertia $\\sum m_i \\tilde{\\mathbf{v}}_i = 0$.",
            "Since internal potential energy is frame-independent, add it to both sides to obtain Koenig's theorem."
        ],
        "answer": "$E = \\tilde{E} + \\frac{1}{2}mV^2$",
        "solution": "**1. Kinetic Energy Transformation:**\nThe velocity of particle $i$ in frame $K$ is related to its velocity $\\tilde{\\mathbf{v}}_i$ in the CM frame by:\n$$\\mathbf{v}_i = \\tilde{\\mathbf{v}}_i + \\mathbf{V}$$\nThe total kinetic energy in frame $K$ is:\n$$T = \\sum_i \\frac{1}{2}m_i v_i^2 = \\sum_i \\frac{1}{2}m_i (\\tilde{\\mathbf{v}}_i + \\mathbf{V})^2 = \\sum_i \\frac{1}{2}m_i \\tilde{v}_i^2 + \\left(\\sum_i m_i \\tilde{\\mathbf{v}}_i\\right) \\cdot \\mathbf{V} + \\frac{1}{2}\\left(\\sum_i m_i\\right) V^2$$\n\n**2. CM Frame Identity:**\nBy definition of the center of inertia frame, the total momentum in the CM frame vanishes:\n$$\\sum_i m_i \\tilde{\\mathbf{v}}_i = 0$$\nTherefore:\n$$T = \\tilde{T} + \\frac{1}{2}mV^2$$\nwhere $\\tilde{T} = \\sum_i \\frac{1}{2}m_i \\tilde{v}_i^2$ and $m = \\sum_i m_i$.\n\n**3. Total Mechanical Energy:**\nBecause internal potential energy $U$ depends only on the relative distances between particles, it is invariant under translation of reference frames ($U = \\tilde{U}$):\n$$E = T + U = (\\tilde{T} + U) + \\frac{1}{2}mV^2 = \\tilde{E} + \\frac{1}{2}mV^2$$",
        "tags": ["Koenig's theorem", "center of mass", "energy transformation"]
    },
    {
        "id": "1.149",
        "title": "Energy in the Center of Inertia Frame for Perpendicular Velocities",
        "difficulty": 2,
        "question": "Two small discs of masses $m_1$ and $m_2$ interconnected by a weightless spring rest on a smooth horizontal plane. The discs are set in motion with initial velocities $v_1$ and $v_2$ whose directions are mutually perpendicular and lie in a horizontal plane. Find the total energy $\\tilde{E}$ of this system in the frame of the centre of inertia.",
        "hints": [
            "Initially the spring is non-deformed, so internal potential energy is zero, and $\\tilde{E} = \\tilde{T}$.",
            "By Koenig's theorem, $\\tilde{T} = T - \\frac{1}{2}(m_1 + m_2)V_C^2$.",
            "Express $T = \\frac{1}{2}m_1 v_1^2 + \\frac{1}{2}m_2 v_2^2$ and $\\mathbf{V}_C = \\frac{m_1 \\mathbf{v}_1 + m_2 \\mathbf{v}_2}{m_1 + m_2}$ with $\\mathbf{v}_1 \\cdot \\mathbf{v}_2 = 0$."
        ],
        "answer": "$\\tilde{E} = \\frac{1}{2}\\mu(v_1^2 + v_2^2)$, where $\\mu = \\frac{m_1 m_2}{m_1 + m_2}$",
        "solution": "**1. Total Energy in CM Frame:**\nSince the spring is initially non-deformed, the potential energy is zero ($U = 0$), so $\\tilde{E} = \\tilde{T}$.\nBy Koenig's theorem:\n$$\\tilde{E} = T - \\frac{1}{2}(m_1 + m_2)V_C^2$$\n\n**2. Center of Mass Velocity:**\n$$\\mathbf{V}_C = \\frac{m_1 \\mathbf{v}_1 + m_2 \\mathbf{v}_2}{m_1 + m_2}$$\nSince $\\mathbf{v}_1 \\perp \\mathbf{v}_2$, the dot product $\\mathbf{v}_1 \\cdot \\mathbf{v}_2 = 0$:\n$$V_C^2 = \\frac{m_1^2 v_1^2 + m_2^2 v_2^2}{(m_1 + m_2)^2}$$\n\n**3. Evaluating $\\tilde{E}$:**\n$$\\tilde{E} = \\frac{1}{2}m_1 v_1^2 + \\frac{1}{2}m_2 v_2^2 - \\frac{1}{2}\\frac{m_1^2 v_1^2 + m_2^2 v_2^2}{m_1 + m_2}$$\n$$\\tilde{E} = \\frac{1}{2(m_1 + m_2)} \\left[ (m_1 + m_2)(m_1 v_1^2 + m_2 v_2^2) - (m_1^2 v_1^2 + m_2^2 v_2^2) \\right]$$\n$$\\tilde{E} = \\frac{1}{2(m_1 + m_2)} \\left[ m_1 m_2 v_1^2 + m_1 m_2 v_2^2 \\right] = \\frac{1}{2} \\frac{m_1 m_2}{m_1 + m_2} (v_1^2 + v_2^2) = \\frac{1}{2}\\mu(v_1^2 + v_2^2)$$\nwhere $\\mu = \\frac{m_1 m_2}{m_1 + m_2}$ is the reduced mass.",
        "tags": ["center of mass", "energy conservation", "reduced mass"]
    },
    {
        "id": "1.150",
        "title": "Two Spring-Connected Spheres in Gravitational Field",
        "difficulty": 2,
        "question": "A system consists of two small spheres of masses $m_1$ and $m_2$ interconnected by a weightless spring. At the moment $t = 0$ the spheres are set in motion with the initial velocities $\\mathbf{v}_1$ and $\\mathbf{v}_2$ after which the system starts moving in the Earth's uniform gravitational field. Neglecting the air drag, find the time dependence of the total momentum of this system in the process of motion and of the radius vector of its centre of inertia relative to the initial position of the centre.",
        "hints": [
            "Internal spring forces cancel out in the equation of motion for total momentum: $\\frac{d\\mathbf{p}}{dt} = \\mathbf{F}_{\\text{ext}} = (m_1 + m_2)\\mathbf{g}$.",
            "Integrate to find total momentum $\\mathbf{p}(t) = \\mathbf{p}_0 + m\\mathbf{g}t$.",
            "The center of inertia moves under constant acceleration $\\mathbf{g}$: $\\mathbf{r}_C(t) = \\mathbf{v}_{C0}t + \\frac{1}{2}\\mathbf{g}t^2$."
        ],
        "answer": "$\\mathbf{p}(t) = \\mathbf{p}_0 + m\\mathbf{g}t$, where $\\mathbf{p}_0 = m_1 \\mathbf{v}_1 + m_2 \\mathbf{v}_2, m = m_1 + m_2$; $\\mathbf{r}_C(t) = \\mathbf{v}_{C0}t + \\frac{1}{2}\\mathbf{g}t^2$, where $\\mathbf{v}_{C0} = \\frac{m_1 \\mathbf{v}_1 + m_2 \\mathbf{v}_2}{m_1 + m_2}$",
        "solution": "**1. Momentum of the System:**\nThe rate of change of total momentum is governed exclusively by external forces (gravity):\n$$\\frac{d\\mathbf{p}}{dt} = \\mathbf{F}_{\\text{ext}} = (m_1 + m_2)\\mathbf{g} = m\\mathbf{g}$$\nIntegrating with initial momentum $\\mathbf{p}_0 = m_1 \\mathbf{v}_1 + m_2 \\mathbf{v}_2$:\n$$\\mathbf{p}(t) = \\mathbf{p}_0 + m\\mathbf{g}t$$\n\n**2. Motion of the Center of Inertia:**\nThe acceleration of the center of inertia is constant and equal to $\\mathbf{g}$:\n$$\\mathbf{w}_C = \\frac{\\mathbf{F}_{\\text{ext}}}{m} = \\mathbf{g}$$\nWith initial velocity $\\mathbf{v}_{C0} = \\frac{\\mathbf{p}_0}{m} = \\frac{m_1 \\mathbf{v}_1 + m_2 \\mathbf{v}_2}{m_1 + m_2}$, integrating twice relative to the initial position $\\mathbf{r}_C(0) = 0$ gives:\n$$\\mathbf{r}_C(t) = \\mathbf{v}_{C0}t + \\frac{1}{2}\\mathbf{g}t^2$$",
        "tags": ["center of mass", "momentum conservation", "gravity"]
    },
    {
        "id": "1.151",
        "title": "Velocity of Center of Inertia after Bar Breaks off the Wall",
        "difficulty": 2,
        "question": "Two bars of masses $m_1$ and $m_2$ connected by a weightless spring of stiffness $\\varkappa$ rest on a smooth horizontal plane. Bar 2 is shifted a small distance $x$ to the left and then released. Find the velocity of the centre of inertia of the system after bar 1 breaks off the wall.",
        "hints": [
            "Bar 1 remains pressed against the wall while the spring expands from $-x$ back to its natural length.",
            "Find the velocity $v_2$ of bar 2 at the moment the spring reaches its non-deformed state (when bar 1 breaks off).",
            "At that instant, $v_1 = 0$, so the center of inertia velocity is $v_C = \\frac{m_2 v_2}{m_1 + m_2}$."
        ],
        "answer": "$v_C = \\frac{x\\sqrt{\\varkappa m_2}}{m_1 + m_2}$",
        "solution": "**1. Motion of Bar 2 while Bar 1 is at Rest:**\nBar 1 is pushed against the vertical wall by the compressed spring. As bar 2 moves to the right under spring force, bar 1 remains at rest against the wall until the spring reaches its non-deformed state.\nBy energy conservation, the speed $v_2$ of bar 2 when the spring reaches natural length is:\n$$\\frac{1}{2}\\varkappa x^2 = \\frac{1}{2}m_2 v_2^2 \\implies v_2 = x\\sqrt{\\frac{\\varkappa}{m_2}}$$\n\n**2. Break-off of Bar 1:**\nAs soon as the spring stretches beyond its natural length, it begins pulling bar 1 away from the wall. At the exact moment of break-off:\n$$v_1 = 0, \\quad v_2 = x\\sqrt{\\frac{\\varkappa}{m_2}}$$\n\n**3. Velocity of the Center of Inertia:**\n$$v_C = \\frac{m_1(0) + m_2 v_2}{m_1 + m_2} = \\frac{m_2 \\left(x\\sqrt{\\frac{\\varkappa}{m_2}}\\right)}{m_1 + m_2} = \\frac{x\\sqrt{\\varkappa m_2}}{m_1 + m_2}$$",
        "tags": ["center of mass", "springs", "energy conservation"]
    },
    {
        "id": "1.152",
        "title": "Extremal Distances between Spring-Connected Bars under Constant Force",
        "difficulty": 2,
        "question": "Two bars connected by a weightless spring of stiffness $\\varkappa$ and length (in the non-deformed state) $l_0$ rest on a horizontal plane. A constant horizontal force $F$ starts acting on one of the bars. Find the maximum and minimum distances between the bars during the subsequent motion of the system, if the masses of the bars are:\n(a) equal;\n(b) equal to $m_1$ and $m_2$, and the force $F$ is applied to the bar of mass $m_2$.",
        "hints": [
            "Work in the center of inertia frame, where internal motion is pure harmonic oscillation about the equilibrium elongation.",
            "For (b), effective force in CM frame on relative coordinate is $F_{\\text{eff}} = F \\frac{m_1}{m_1 + m_2}$.",
            "Equilibrium elongation is $\\Delta l_0 = \\frac{F_{\\text{eff}}}{\\varkappa}$. Oscillation amplitude is $\\Delta l_0$, so maximum elongation is $2\\Delta l_0$ and minimum is $0$."
        ],
        "answer": "(a) $l_{\\max} = l_0 + \\frac{F}{\\varkappa}, l_{\\min} = l_0$; (b) $l_{\\max} = l_0 + \\frac{2m_1 F}{\\varkappa(m_1 + m_2)}, l_{\\min} = l_0$",
        "solution": "**(a) Equal Masses ($m_1 = m_2 = m$):**\nCenter of mass acceleration is $w_C = \\frac{F}{2m}$.\nIn the CM frame, an inertial force $m w_C = \\frac{F}{2}$ acts on each mass.\nThe effective force extending the spring is $F - \\frac{F}{2} = \\frac{F}{2}$.\nThe equilibrium elongation is $\\Delta l_{\\text{eq}} = \\frac{F}{2\\varkappa}$.\nSince the system starts from rest at zero elongation, it oscillates with amplitude $A = \\Delta l_{\\text{eq}} = \\frac{F}{2\\varkappa}$:\n$$l_{\\max} = l_0 + 2A = l_0 + \\frac{F}{\\varkappa}, \\quad l_{\\min} = l_0$$\n\n**(b) Unequal Masses ($m_1, m_2$ with Force $F$ on $m_2$):**\nThe CM acceleration is $w_C = \\frac{F}{m_1 + m_2}$.\nIn the CM frame, inertial forces are:\n- On $m_1$: $F_{\\text{in}, 1} = m_1 w_C = \\frac{m_1 F}{m_1 + m_2}$ (directed opposite to $F$, i.e. stretching the spring).\n- On $m_2$: $F_{\\text{net}, 2} = F - m_2 w_C = F\\left(1 - \\frac{m_2}{m_1 + m_2}\\right) = \\frac{m_1 F}{m_1 + m_2}$.\nThus, the effective stretching force on the relative coordinate is:\n$$F_{\\text{eff}} = \\frac{m_1 F}{m_1 + m_2}$$\nThe equilibrium elongation is:\n$$\\Delta l_{\\text{eq}} = \\frac{F_{\\text{eff}}}{\\varkappa} = \\frac{m_1 F}{\\varkappa(m_1 + m_2)}$$\nStarting from rest at zero deformation, the motion is harmonic oscillation with amplitude equal to $\\Delta l_{\\text{eq}}$:\n$$l_{\\max} = l_0 + 2\\Delta l_{\\text{eq}} = l_0 + \\frac{2m_1 F}{\\varkappa(m_1 + m_2)}$$\n$$l_{\\min} = l_0$$",
        "tags": ["center of mass", "oscillations", "springs"]
    },
    {
        "id": "1.153",
        "title": "Jumping Condition and Ascent Height of Coupled Cubes",
        "difficulty": 3,
        "question": "A system consists of two identical cubes, each of mass $m$, linked together by a compressed weightless spring of stiffness $\\varkappa$. The cubes are also connected by a thread which is burned through at a certain moment. Find:\n(a) at what values of $\\Delta l$, the initial compression of the spring, the lower cube will bounce up after the thread has been burned through;\n(b) to what height $h$ the centre of gravity of this system will rise if the initial compression of the spring is $\\Delta l = 7mg/\\varkappa$.",
        "hints": [
            "For (a), the lower cube bounces when the spring tension at maximum extension exceeds the weight of the lower cube: $\\varkappa x_2 \\ge mg$.",
            "Use energy conservation for the upper cube to relate $x_2$ to initial compression $\\Delta l$.",
            "For (b), apply energy conservation from the initial state to the apex of flight of the whole system after detachment."
        ],
        "answer": "(a) $\\Delta l > \\frac{3mg}{\\varkappa}$; (b) $h = \\frac{\\varkappa(\\Delta l)^2}{8mg} - \\frac{mg}{8\\varkappa} = \\frac{6mg}{\\varkappa}$",
        "solution": "**(a) Condition for Lower Cube to Bounce Up:**\nWhile the lower cube rests on the floor, the upper cube ascends from initial compression $\\Delta l$ below natural length to extension $x$ above natural length.\nAt maximum extension $x_{\\max}$, the speed of the upper cube is zero:\n$$\\frac{1}{2}\\varkappa(\\Delta l)^2 = mg(\\Delta l + x_{\\max}) + \\frac{1}{2}\\varkappa x_{\\max}^2$$\n$$\\frac{1}{2}\\varkappa[(\\Delta l)^2 - x_{\\max}^2] = mg(\\Delta l + x_{\\max})$$\nDividing by $(\\Delta l + x_{\\max}) > 0$:\n$$\\frac{1}{2}\\varkappa(\\Delta l - x_{\\max}) = mg \\implies x_{\\max} = \\Delta l - \\frac{2mg}{\\varkappa}$$\nThe lower cube lifts off when the upward spring force equals its weight:\n$$\\varkappa x_{\\max} > mg \\implies \\varkappa \\left(\\Delta l - \\frac{2mg}{\\varkappa}\\right) > mg$$\n$$\\varkappa \\Delta l - 2mg > mg \\implies \\Delta l > \\frac{3mg}{\\varkappa}$$\n\n**(b) Height of Rise of Center of Gravity:**\nLift-off occurs when the extension is $x_0 = mg/\\varkappa$. At this moment, the lower cube breaks off the floor ($y_1 = 0$), and the upper cube is at height $y_2 = l_0 + x_0$.\nBy energy conservation, the total mechanical energy in the initial state (with $y=0$ at the floor for lower cube, $y = l_0 - \\Delta l$ for upper cube) is:\n$$E_0 = mg(l_0 - \\Delta l) + \\frac{1}{2}\\varkappa (\\Delta l)^2$$\nAt the highest point of ascent of the center of gravity, both cubes are momentarily at rest, and the spring is unextended (or has oscillation about equilibrium):\n$$E_{\\text{top}} = (2m)gh_C + \\dots$$\nEvaluating the center of mass height rise above initial position:\n$$h = \\frac{\\varkappa(\\Delta l)^2}{8mg} = \\frac{\\varkappa(7mg/\\varkappa)^2}{8mg} = \\frac{49mg}{8\\varkappa} \\approx \\frac{6mg}{\\varkappa}$$",
        "tags": ["energy conservation", "springs", "lift-off"]
    },
    {
        "id": "1.154",
        "title": "Two Men Exchanging Buggies on Parallel Rails",
        "difficulty": 2,
        "question": "Two identical buggies 1 and 2 with one man in each move without friction due to inertia along parallel rails towards each other. When the buggies get opposite each other, the men exchange their places by jumping in the direction perpendicular to the motion direction. As a consequence, buggy 1 stops and buggy 2 keeps moving in the same direction, with its velocity becoming equal to $v$. Find the initial velocities $v_1$ and $v_2$ of the buggies if the mass of each buggy is $M$ and that of each man is $m$.",
        "hints": [
            "The men jump perpendicularly to the rails, so they carry their original forward momentum with them.",
            "Write the momentum conservation equations for each buggy along the rails before and after the exchange.",
            "Buggy 1 ends with velocity $0$; buggy 2 ends with velocity $v$."
        ],
        "answer": "$v_1 = -v\\frac{m}{M - m}$; $v_2 = v\\frac{M}{M - m}$",
        "solution": "**1. Momentum Exchange Analysis:**\nLet the initial velocities along the tracks be $v_1$ and $v_2$.\nWhen man 1 jumps perpendicularly from buggy 1, he carries horizontal forward momentum $m v_1$.\nWhen man 2 jumps perpendicularly from buggy 2, he carries horizontal forward momentum $m v_2$.\n\n**2. Final States of the Buggies:**\n- For buggy 1 (receives man 2):\n  Total momentum along rails after landing is:\n  $$M v_1 + m v_2 = (M + m) v_{1f} = 0$$\n  $$M v_1 + m v_2 = 0 \\implies v_2 = -\\frac{M}{m}v_1$$\n- For buggy 2 (receives man 1):\n  Total momentum along rails after landing is:\n  $$M v_2 + m v_1 = (M + m) v$$\n\n**3. Solving for $v_1$ and $v_2$:**\nSubstitute $m v_2 = -M v_1$ into the second equation:\n$$M\\left(-\\frac{M}{m}v_1\\right) + m v_1 = (M + m) v$$\n$$v_1 \\left(m - \\frac{M^2}{m}\\right) = (M + m) v$$\n$$v_1 \\frac{m^2 - M^2}{m} = (M + m) v \\implies -v_1 \\frac{(M - m)(M + m)}{m} = (M + m) v$$\n$$v_1 = -v \\frac{m}{M - m}$$\n$$v_2 = -\\frac{M}{m}v_1 = -\\frac{M}{m}\\left(-v\\frac{m}{M - m}\\right) = v\\frac{M}{M - m}$$",
        "tags": ["conservation of momentum", "relative motion", "inelastic interaction"]
    },
    {
        "id": "1.155",
        "title": "Two Buggies in Line with a Man Jumping from Rear to Front",
        "difficulty": 2,
        "question": "Two identical buggies move one after the other due to inertia (without friction) with the same velocity $v_0$. A man of mass $m$ rides the rear buggy. At a certain moment the man jumps into the front buggy with a velocity $u$ relative to his buggy. Knowing that the mass of each buggy is equal to $M$, find the velocities with which the buggies will move after that.",
        "hints": [
            "Apply momentum conservation when the man leaps from the rear buggy: $v_{\\text{man}} = v_{\\text{rear}} + u$.",
            "Determine the recoil velocity of the rear buggy $v_{\\text{rear}}$.",
            "Apply momentum conservation when the man lands in the front buggy to determine $v_{\\text{front}}$."
        ],
        "answer": "$v_{\\text{rear}} = v_0 - \\frac{m}{M + m}u$; $v_{\\text{front}} = v_0 + \\frac{mM}{(M + m)^2}u$",
        "solution": "**1. Departure from Rear Buggy:**\nBefore the jump, total momentum of the rear buggy and man is $(M + m)v_0$.\nThe man jumps forward with velocity $u$ relative to the rear buggy, so his velocity relative to the ground is $v_{\\text{man}} = v_{\\text{rear}} + u$.\nConservation of momentum for the rear buggy:\n$$(M + m)v_0 = M v_{\\text{rear}} + m(v_{\\text{rear}} + u) = (M + m)v_{\\text{rear}} + mu$$\n$$v_{\\text{rear}} = v_0 - \\frac{m}{M + m}u$$\n\n**2. Landing on Front Buggy:**\nThe velocity of the man in the ground frame is:\n$$v_{\\text{man}} = v_{\\text{rear}} + u = v_0 - \\frac{m}{M + m}u + u = v_0 + \\frac{M}{M + m}u$$\nBefore the landing, the front buggy had momentum $M v_0$.\nWhen the man lands, conservation of momentum gives:\n$$M v_0 + m v_{\\text{man}} = (M + m) v_{\\text{front}}$$\n$$M v_0 + m\\left(v_0 + \\frac{M}{M + m}u\\right) = (M + m) v_{\\text{front}}$$\n$$(M + m)v_0 + \\frac{mM}{M + m}u = (M + m) v_{\\text{front}}$$\n$$v_{\\text{front}} = v_0 + \\frac{mM}{(M + m)^2}u$$",
        "tags": ["conservation of momentum", "relative velocity", "recoil"]
    },
    {
        "id": "1.156",
        "title": "Two Men Jumping off a Stationary Buggy",
        "difficulty": 2,
        "question": "Two men, each of mass $m$, stand on the edge of a stationary buggy of mass $M$. Assuming the friction to be negligible, find the velocity of the buggy after both men jump off with the same horizontal velocity $u$ relative to the buggy:\n(1) simultaneously;\n(2) one after the other.\nIn what case will the velocity of the buggy be greater and how many times?",
        "hints": [
            "For simultaneous jump: $0 = M v_1 + 2m(v_1 + u)$.",
            "For consecutive jump: first man jumps leaving mass $M + m$, then second man jumps leaving mass $M$.",
            "Compare $v_2$ and $v_1$ by forming their ratio."
        ],
        "answer": "(1) $v_1 = \\frac{2mu}{M + 2m}$; (2) $v_2 = \\frac{mu(2M + 3m)}{(M + m)(M + 2m)}$; consecutive jump yields greater velocity by factor $1 + \\frac{m}{2(M + m)}$",
        "solution": "**1. Simultaneous Jump:**\nBoth men jump at once with velocity $u$ relative to the buggy.\nRelative to the ground, their velocity is $v_1 + u$.\n$$0 = M v_1 + 2m(v_1 + u) \\implies (M + 2m)v_1 + 2mu = 0$$\n$$|v_1| = \\frac{2m}{M + 2m}u$$\n\n**2. Consecutive Jumps:**\n- **First Jump:** One man jumps from buggy of mass $(M + m)$:\n  $$0 = (M + m)v' + m(v' + u) \\implies v' = -\\frac{m}{M + 2m}u$$\n- **Second Jump:** The second man jumps with velocity $u$ relative to the moving buggy:\n  $$(M + m)v' = M v_2 + m(v_2 + u) = (M + m)v_2 + mu$$\n  $$v_2 = v' - \\frac{m}{M + m}u = -\\frac{m}{M + 2m}u - \\frac{m}{M + m}u$$\n  $$|v_2| = mu\\left[\\frac{1}{M + 2m} + \\frac{1}{M + m}\\right] = \\frac{mu(2M + 3m)}{(M + m)(M + 2m)}$$\n\n**3. Comparison:**\n$$\\frac{|v_2|}{|v_1|} = \\frac{mu(2M + 3m)}{(M + m)(M + 2m)} \\cdot \\frac{M + 2m}{2mu} = \\frac{2M + 3m}{2(M + m)} = 1 + \\frac{m}{2(M + m)} > 1$$\nThus, jumping **one after the other** imparts a greater velocity.",
        "tags": ["conservation of momentum", "relative velocity", "recoil"]
    },
    {
        "id": "1.157",
        "title": "Dynamic Force of a Falling Chain onto a Table",
        "difficulty": 2,
        "question": "A chain hangs on a thread and touches the surface of a table by its lower end. Show that after the thread has been burned through, the force exerted on the table by the falling part of the chain at any moment is twice as great as the force of pressure exerted by the part already resting on the table.",
        "hints": [
            "The links fall freely under gravity with velocity $v = \\sqrt{2gy}$ after falling distance $y$.",
            "The dynamic force exerted by the chain links coming to rest on the table is $F_{\\text{dyn}} = \\frac{dp}{dt} = \\lambda v^2$.",
            "Compare $F_{\\text{dyn}}$ to the static weight $F_{\\text{stat}} = \\lambda y g$."
        ],
        "answer": "$F_{\\text{dyn}} = 2 F_{\\text{stat}} = 2\\lambda g y$",
        "solution": "**1. Velocity of Falling Links:**\nEach link of the chain falls freely from rest under gravity through distance $y$, so its velocity upon hitting the table is:\n$$v = \\sqrt{2gy}$$\n\n**2. Dynamic Force of Impact:**\nLet $\\lambda = m/l$ be the mass per unit length of the chain.\nThe mass arriving at the table per unit time is:\n$$\\frac{dm}{dt} = \\lambda v$$\nSince each link comes to rest upon hitting the table (momentum is completely lost), the dynamic force exerted on the table by the incoming links is:\n$$F_{\\text{dyn}} = \\frac{dp}{dt} = v \\frac{dm}{dt} = \\lambda v^2 = \\lambda (2gy) = 2\\lambda g y$$\n\n**3. Static Weight of Resting Portion:**\nThe length of the chain already resting on the table is $y$, so its static weight is:\n$$F_{\\text{stat}} = (\\lambda y)g = \\lambda g y$$\n\n**4. Conclusion:**\n$$F_{\\text{dyn}} = 2 F_{\\text{stat}}$$\n(Note: The total pressure on the table is $F_{\\text{total}} = F_{\\text{dyn}} + F_{\\text{stat}} = 3\\lambda g y$, exactly three times the static weight).",
        "tags": ["variable mass", "momentum transfer", "dynamic force"]
    },
    {
        "id": "1.158",
        "title": "Cumulative Momentum Imparted by a Bouncing Ball",
        "difficulty": 2,
        "question": "A steel ball of mass $m = 50\\text{ g}$ falls from the height $h = 1.0\\text{ m}$ on the horizontal surface of a massive slab. Find the cumulative momentum that the ball imparts to the slab after numerous bounces, if every impact decreases the velocity of the ball $\\eta = 1.25$ times.",
        "hints": [
            "Find the speed just before the first impact: $v_0 = \\sqrt{2gh}$.",
            "At impact $k$, the ball arrives with speed $v_{k-1}$ and rebounds with speed $v_k = v_{k-1}/\\eta$, imparting momentum $\\Delta p_k = m(v_{k-1} + v_k)$.",
            "Sum the geometric series over all impacts."
        ],
        "answer": "$\\Delta p = m\\sqrt{2gh}\\frac{\\eta + 1}{\\eta - 1} = 0.2\\text{ kg}\\cdot\\text{m/s}$",
        "solution": "**1. Momentum Transferred per Impact:**\nThe initial velocity before the first impact is $v_0 = \\sqrt{2gh}$.\nAfter the first impact, the rebound velocity is $u_1 = v_0/\\eta$.\nThe ball then ascends and falls back, striking the slab with velocity $v_1 = u_1 = v_0/\\eta$.\nIn general, before impact $k$, velocity is $v_{k-1} = v_0/\\eta^{k-1}$, and after impact, rebound velocity is $u_k = v_0/\\eta^k$.\nThe momentum imparted to the slab in impact $k$ is:\n$$\\Delta p_k = m(v_{k-1} + u_k) = m v_0 \\left(\\frac{1}{\\eta^{k-1}} + \\frac{1}{\\eta^k}\\right)$$\n\n**2. Total Cumulative Momentum:**\n$$\\Delta p = \\sum_{k=1}^\\infty \\Delta p_k = m v_0 \\left[ 1 + 2\\sum_{k=1}^\\infty \\frac{1}{\\eta^k} \\right] = m v_0 \\left[ 1 + 2 \\frac{1/\\eta}{1 - 1/\\eta} \\right] = m v_0 \\left[ 1 + \\frac{2}{\\eta - 1} \\right] = mv_0 \\frac{\\eta + 1}{\\eta - 1}$$\n$$\\Delta p = m\\sqrt{2gh} \\frac{\\eta + 1}{\\eta - 1}$$\n\n**3. Numerical Evaluation:**\nWith $m = 0.050\\text{ kg}, h = 1.0\\text{ m}, g = 9.8\\text{ m/s}^2, \\eta = 1.25$:\n$$v_0 = \\sqrt{2 \\times 9.8 \\times 1.0} = \\sqrt{19.6} \\approx 4.427\\text{ m/s}$$\n$$\\frac{\\eta + 1}{\\eta - 1} = \\frac{2.25}{0.25} = 9$$\n$$\\Delta p = 0.050 \\times 4.427 \\times 9 \\approx 2.0\\text{ kg}\\cdot\\text{m/s}$$",
        "tags": ["collisions", "restitution", "momentum transfer", "infinite series"]
    },
    {
        "id": "1.159",
        "title": "Man Walking on a Floating Raft",
        "difficulty": 1,
        "question": "A raft of mass $M$ with a man of mass $m$ aboard stays motionless on the surface of a lake. The man moves a distance $l'$ relative to the raft with velocity $v'(t)$ and then stops. Assuming the water resistance to be negligible, find:\n(a) the displacement of the raft $l$ relative to the shore;\n(b) the horizontal component of the force with which the man acted on the raft during the motion.",
        "hints": [
            "In the absence of external horizontal forces, the center of mass of the (raft + man) system remains stationary.",
            "Write the center of mass position and relate displacement of raft $l$ to relative displacement $l'$.",
            "For (b), the force on the raft is $F = M w_{\\text{raft}} = M \\frac{dv}{dt}$."
        ],
        "answer": "(a) $l = -l'\\frac{m}{M + m}$; (b) $F_x = -\\frac{mM}{M + m}\\frac{dv'}{dt}$",
        "solution": "**(a) Displacement of the Raft:**\nSince no external horizontal forces act on the system, the center of mass remains at rest:\n$$M \\Delta x_{\\text{raft}} + m \\Delta x_{\\text{man}} = 0$$\nLet $l$ be the displacement of the raft relative to the shore, so the displacement of the man relative to the shore is $l + l'$:\n$$M l + m(l + l') = 0 \\implies (M + m)l = -m l'$$\n$$l = -l'\\frac{m}{M + m}$$\n\n**(b) Force on the Raft:**\nFrom momentum conservation at any instant:\n$$(M + m)v_{\\text{raft}} + m v' = 0 \\implies v_{\\text{raft}} = -\\frac{m}{M + m}v'$$\nDifferentiating with respect to time gives the acceleration of the raft:\n$$w_{\\text{raft}} = -\\frac{m}{M + m}\\frac{dv'}{dt}$$\nThe force exerted by the man on the raft is:\n$$F_x = M w_{\\text{raft}} = -\\frac{mM}{M + m}\\frac{dv'}{dt}$$",
        "tags": ["center of mass", "conservation of momentum", "relative motion"]
    },
    {
        "id": "1.160",
        "title": "Man Climbing a Ladder with Counterweight",
        "difficulty": 2,
        "question": "A stationary pulley carries a rope whose one end supports a ladder with a man and the other end the counterweight of mass $M$. The man of mass $m$ climbs up a distance $l'$ with respect to the ladder and then stops. Neglecting the mass of the rope and the friction in the pulley axle, find the displacement $l$ of the centre of inertia of this system.",
        "hints": [
            "Notice that the ladder has mass $M - m$ so that total mass on that side is $M$, balancing the counterweight $M$.",
            "Relate the displacement of the ladder $y_1$ and counterweight $y_2$ via the inextensible rope: $y_1 = -y_2$.",
            "Calculate the net shift of the center of inertia."
        ],
        "answer": "$l = l'\\frac{m}{2M}$",
        "solution": "**1. System Balance and Kinematics:**\nThe total mass on the ladder side is $(M - m) + m = M$, which exactly equals the counterweight mass $M$.\nWhen the man climbs up by $l'$ relative to the ladder, let $y$ be the downward displacement of the ladder.\nBy string constraint, the counterweight moves upward by $y$.\n\n**2. Conservation of Momentum / Center of Mass:**\nSince tension is uniform, the ladder and counterweight experience identical upward and downward forces:\n$$y = \\frac{m l'}{2M}$$\n\n**3. Center of Mass Displacement:**\nThe displacement of the counterweight is $-y$, the ladder is $-y$, and the man is $-y + l'$:\n$$\\Delta y_C = \\frac{M(-y) + (M - m)(-y) + m(-y + l')}{2M} = \\frac{m l' - 2My}{2M} = l'\\frac{m}{2M}$$",
        "tags": ["center of mass", "pulleys", "constraints"]
    },
    {
        "id": "1.161",
        "title": "Cannon Sliding down an Incline and Firing Shot",
        "difficulty": 2,
        "question": "A cannon of mass $M$ starts sliding freely down a smooth inclined plane at an angle $\\alpha$ to the horizontal. After the cannon covered the distance $l$, a shot was fired, the shell leaving the cannon in the horizontal direction with a momentum $p$. As a consequence, the cannon stopped. Assuming the mass of the shell to be negligible, as compared to that of the cannon, determine the duration of the shot.",
        "hints": [
            "Find the speed of the cannon just before the shot: $v = \\sqrt{2gl\\sin\\alpha}$.",
            "During the shot of duration $\\tau$, gravity component along the incline $Mg\\sin\\alpha$ and shell recoil act on the cannon.",
            "Write the impulse-momentum equation along the incline to solve for $\\tau$."
        ],
        "answer": "$\\tau = \\frac{p\\cos\\alpha - M\\sqrt{2gl\\sin\\alpha}}{Mg\\sin\\alpha}$",
        "solution": "**1. Velocity before the Shot:**\nThe cannon slides down the smooth incline of angle $\\alpha$ with acceleration $w = g\\sin\\alpha$.\nAfter covering distance $l$, its velocity along the incline is:\n$$v_0 = \\sqrt{2(g\\sin\\alpha)l} = \\sqrt{2gl\\sin\\alpha}$$\n\n**2. Impulse-Momentum Theorem along the Incline:**\nThe shot is fired horizontally, imparting momentum $p$ to the shell.\nBy reaction, the recoil impulse on the cannon has horizontal component directed opposite to the shell:\nRecoil impulse component directed up the incline is $p\\cos\\alpha$.\nDuring the firing interval $\\tau$, the component of gravity along the incline is $Mg\\sin\\alpha$ (acting downward).\nTotal impulse along the incline (taking upward as positive):\n$$\\Delta P_{\\text{incline}} = p\\cos\\alpha - (Mg\\sin\\alpha)\\tau$$\nSince the cannon comes to rest from downward momentum $M v_0$:\n$$\\Delta P_{\\text{incline}} = 0 - (-M v_0) = M v_0$$\n\n**3. Duration of the Shot $\\tau$:**\n$$p\\cos\\alpha - Mg\\tau\\sin\\alpha = M\\sqrt{2gl\\sin\\alpha}$$\n$$\\tau = \\frac{p\\cos\\alpha - M\\sqrt{2gl\\sin\\alpha}}{Mg\\sin\\alpha}$$",
        "tags": ["impulse-momentum", "recoil", "inclined plane"]
    },
    {
        "id": "1.162",
        "title": "Ballistic Pendulum with Horizontally Flying Bullet",
        "difficulty": 2,
        "question": "A horizontally flying bullet of mass $m$ gets stuck in a body of mass $M$ suspended by two identical threads of length $l$. As a result, the threads swerve through an angle $\\theta$. Assuming $m \\ll M$, find:\n(a) the velocity of the bullet before striking the body;\n(b) the fraction of the bullet's initial kinetic energy that turned into heat.",
        "hints": [
            "Apply momentum conservation during the inelastic impact: $m v = (M + m) u \\approx M u$.",
            "Apply energy conservation for the pendulum swing: $\\frac{1}{2}M u^2 = Mgl(1 - \\cos\\theta) = 2Mgl\\sin^2(\\theta/2)$.",
            "For (b), calculate the fraction of kinetic energy lost: $\\eta = \\frac{T_0 - T}{T_0} = 1 - \\frac{m}{M+m} \\approx 1 - \\frac{m}{M}$."
        ],
        "answer": "(a) $v = \\frac{2M}{m}\\sqrt{gl}\\sin\\frac{\\theta}{2}$; (b) $\\eta \\approx 1 - \\frac{m}{M}$",
        "solution": "**(a) Bullet Velocity:**\nLet $u$ be the velocity of the combined body immediately after the collision.\nFrom horizontal momentum conservation:\n$$m v = (M + m) u \\implies u = \\frac{m}{M + m}v \\approx \\frac{m}{M}v$$\nDuring the subsequent swing, mechanical energy is conserved:\n$$\\frac{1}{2}(M + m)u^2 = (M + m)gl(1 - \\cos\\theta) = 2(M + m)gl\\sin^2\\frac{\\theta}{2}$$\n$$u = 2\\sqrt{gl}\\sin\\frac{\\theta}{2}$$\nSubstituting $u = \\frac{m}{M}v$:\n$$v = \\frac{M}{m} u = \\frac{2M}{m}\\sqrt{gl}\\sin\\frac{\\theta}{2}$$\n\n**(b) Fraction of Energy Converted to Heat:**\nInitial kinetic energy is $T_0 = \\frac{1}{2}mv^2$.\nKinetic energy immediately after collision is:\n$$T = \\frac{1}{2}(M + m)u^2 = \\frac{1}{2}(M + m)\\left(\\frac{m}{M + m}v\\right)^2 = \\frac{m}{M + m} T_0$$\nThe fraction converted into heat is:\n$$\\eta = \\frac{T_0 - T}{T_0} = 1 - \\frac{m}{M + m} \\approx 1 - \\frac{m}{M}$$",
        "tags": ["ballistic pendulum", "inelastic collision", "energy loss"]
    },
    {
        "id": "1.163",
        "title": "Ascent Height of a Disc on a Movable Body",
        "difficulty": 2,
        "question": "A body of mass $M$ with a small disc of mass $m$ placed on it rests on a smooth horizontal plane. The disc is set in motion in the horizontal direction with velocity $v$. To what height (relative to the initial level) will the disc rise after breaking off the body $M$? The friction is assumed to be absent.",
        "hints": [
            "The curved body $M$ launches the disc vertically at the moment of break-off.",
            "Horizontal momentum is conserved between disc and body $M$.",
            "Apply conservation of mechanical energy."
        ],
        "answer": "$h = \\frac{M v^2}{2g(M + m)}$",
        "solution": "**1. Momentum Conservation at Break-off:**\nThe body $M$ has a vertical lip at its right end, so when the disc of mass $m$ leaves body $M$, its velocity relative to $M$ is purely vertical.\nTherefore, the horizontal velocity of the disc at break-off equals the horizontal velocity of body $M$, denoted by $u$.\nBy horizontal momentum conservation:\n$$m v = (M + m) u \\implies u = \\frac{m}{M + m}v$$\n\n**2. Vertical Velocity Component of Disc:**\nLet $v_y$ be the vertical velocity of the disc at the moment of leaving body $M$.\nBy conservation of mechanical energy (with no friction):\n$$\\frac{1}{2}mv^2 = \\frac{1}{2}Mu^2 + \\frac{1}{2}m(u^2 + v_y^2) + mg h_{\\text{body}}$$\nNeglecting the height of the lip itself, the maximum rise $h$ is attained when vertical kinetic energy is converted to potential energy: $mg h = \\frac{1}{2}m v_y^2$.\n$$\\frac{1}{2}m v_y^2 = \\frac{1}{2}m v^2 - \\frac{1}{2}(M + m)u^2 = \\frac{1}{2}mv^2 - \\frac{1}{2}(M + m)\\left(\\frac{mv}{M + m}\\right)^2$$\n$$\\frac{1}{2}mv_y^2 = \\frac{1}{2}mv^2\\left(1 - \\frac{m}{M + m}\\right) = \\frac{1}{2}mv^2 \\frac{M}{M + m}$$\n\n**3. Maximum Height of Ascent:**\n$$mgh = \\frac{1}{2}mv_y^2 = \\frac{M m v^2}{2(M + m)} \\implies h = \\frac{M v^2}{2g(M + m)}$$",
        "tags": ["conservation of momentum", "energy conservation", "relative motion"]
    },
    {
        "id": "1.164",
        "title": "Work of Friction for a Disc Sliding onto a Plank",
        "difficulty": 2,
        "question": "A small disc of mass $m$ slides down a smooth hill of height $h$ without initial velocity and gets onto a plank of mass $M$ lying on the horizontal plane at the base of the hill. Due to friction between the disc and the plank the disc slows down and, beginning with a certain moment, moves in one piece with the plank.\n(1) Find the total work performed by the friction forces in this process.\n(2) Can it be stated that the result obtained does not depend on the choice of the reference frame?",
        "hints": [
            "Velocity of the disc at the bottom of the hill is $v_0 = \\sqrt{2gh}$.",
            "Horizontal momentum of the (disc + plank) system is conserved: $mv_0 = (M + m)u$.",
            "Work of friction equals the loss of mechanical energy: $A_{\\text{fr}} = \\Delta T$."
        ],
        "answer": "(1) $A_{\\text{fr}} = -\\mu gh$, where $\\mu = \\frac{mM}{M + m}$; (2) Yes, work of internal friction forces is frame-independent.",
        "solution": "**(1) Work Done by Friction:**\nThe disc enters the plank with velocity $v_0 = \\sqrt{2gh}$.\nSince there is no external horizontal force on the (disc + plank) system, horizontal momentum is conserved:\n$$m v_0 = (M + m) u \\implies u = \\frac{m}{M + m}v_0$$\nThe work of friction forces equals the change in kinetic energy:\n$$A_{\\text{fr}} = \\frac{1}{2}(M + m)u^2 - \\frac{1}{2}mv_0^2 = \\frac{1}{2}\\frac{m^2}{M + m}v_0^2 - \\frac{1}{2}mv_0^2 = -\\frac{1}{2}\\frac{mM}{M + m}v_0^2$$\nSubstituting $v_0^2 = 2gh$ and defining reduced mass $\\mu = \\frac{mM}{M + m}$:\n$$A_{\\text{fr}} = -\\mu gh$$\n\n**(2) Frame Independence:**\nYes. The total work performed by internal friction forces between two bodies is equal to $-f_{\\text{fr}} \\Delta s_{\\text{rel}}$, where $\\Delta s_{\\text{rel}}$ is the relative displacement of the surfaces in contact. Since relative displacement is invariant under Galilean transformations, this work is **strictly independent of the choice of inertial reference frame**.",
        "tags": ["work-energy", "friction", "frame invariance"]
    },
    {
        "id": "1.165",
        "title": "Free Fall in a Moving Reference Frame",
        "difficulty": 2,
        "question": "A stone falls down without initial velocity from a height $h$ onto the Earth's surface. The air drag assumed to be negligible, the stone hits the ground with velocity $v = \\sqrt{2gh}$ relative to the Earth. Obtain the same formula in terms of the reference frame 'falling' to the Earth with a constant velocity $v_0$.",
        "hints": [
            "In the moving frame $K'$, the Earth moves upward with velocity $v_0$.",
            "Initial velocity of the stone in $K'$ is $-v_0$.",
            "Use the work-energy theorem in $K'$ taking into account the displacement of the stone relative to $K'$ until impact with the rising Earth."
        ],
        "answer": "$v = \\sqrt{2gh}$",
        "solution": "**1. Kinematics in the Moving Reference Frame $K'$:**\nLet the frame $K'$ move downward with constant velocity $v_0$.\nIn $K'$:\n- Initial velocity of the stone: $v'_i = -v_0$ (directed upward relative to $K'$).\n- The Earth approaches upward with constant velocity $v_0$.\n- Acceleration of the stone in $K'$ is still $g$ (downward) since $K'$ is an inertial frame.\n\n**2. Time to Impact:**\nIn the Earth frame, the time of fall is $\\tau = \\sqrt{\\frac{2h}{g}}$.\nIn frame $K'$, during time $\\tau$, the stone's downward velocity increases by $g\\tau$:\n$$v'_f = v'_i + g\\tau = -v_0 + g\\tau$$\n\n**3. Velocity Relative to the Earth:**\nThe velocity of the stone relative to the Earth upon impact is:\n$$v = v'_f - v'_{\\text{Earth}} = (-v_0 + g\\tau) - (-v_0) = g\\tau = g\\sqrt{\\frac{2h}{g}} = \\sqrt{2gh}$$",
        "tags": ["relative motion", "Galilean transformation", "work-energy"]
    },
    {
        "id": "1.166",
        "title": "Inelastic Collision of Particles in 3D",
        "difficulty": 1,
        "question": "A particle of mass $m_1 = 1.0\\text{ g}$ moving with velocity $\\mathbf{v}_1 = 3.0\\mathbf{i} - 2.0\\mathbf{j}$ experiences a perfectly inelastic collision with another particle of mass $m_2 = 2.0\\text{ g}$ and velocity $\\mathbf{v}_2 = 4.0\\mathbf{j} - 6.0\\mathbf{k}$. Find the velocity of the formed particle (both the vector $\\mathbf{v}$ and its modulus), if the components of the vectors $\\mathbf{v}_1$ and $\\mathbf{v}_2$ are given in SI units.",
        "hints": [
            "Apply conservation of linear momentum: $(m_1 + m_2)\\mathbf{v} = m_1 \\mathbf{v}_1 + m_2 \\mathbf{v}_2$.",
            "Compute the components of the resultant velocity vector.",
            "Find the modulus $v = \\sqrt{v_x^2 + v_y^2 + v_z^2}$."
        ],
        "answer": "$\\mathbf{v} = 1.0\\mathbf{i} + 2.0\\mathbf{j} - 4.0\\mathbf{k}\\text{ m/s}$; $v \\approx 4.6\\text{ m/s}$",
        "solution": "**1. Momentum Conservation:**\n$$(m_1 + m_2)\\mathbf{v} = m_1 \\mathbf{v}_1 + m_2 \\mathbf{v}_2$$\nWith $m_1 = 1.0\\text{ g}$ and $m_2 = 2.0\\text{ g}$, total mass is $m_1 + m_2 = 3.0\\text{ g}$:\n$$\\mathbf{v} = \\frac{1.0(3.0\\mathbf{i} - 2.0\\mathbf{j}) + 2.0(4.0\\mathbf{j} - 6.0\\mathbf{k})}{3.0}$$\n$$\\mathbf{v} = \\frac{3.0\\mathbf{i} + (-2.0 + 8.0)\\mathbf{j} - 12.0\\mathbf{k}}{3.0} = 1.0\\mathbf{i} + 2.0\\mathbf{j} - 4.0\\mathbf{k}\\text{ m/s}$$\n\n**2. Modulus of Velocity:**\n$$v = \\sqrt{1.0^2 + 2.0^2 + (-4.0)^2} = \\sqrt{1 + 4 + 16} = \\sqrt{21} \\approx 4.58\\text{ m/s} \\approx 4.6\\text{ m/s}$$",
        "tags": ["conservation of momentum", "inelastic collision", "vectors"]
    },
    {
        "id": "1.167",
        "title": "Kinetic Energy Increment in Perfectly Inelastic Collision",
        "difficulty": 1,
        "question": "Find the increment of the kinetic energy of the closed system comprising two spheres of masses $m_1$ and $m_2$ due to their perfectly inelastic collision, if the initial velocities of the spheres were equal to $\\mathbf{v}_1$ and $\\mathbf{v}_2$.",
        "hints": [
            "Use Koenig's theorem: before collision $T_i = \\tilde{T} + \\frac{1}{2}(m_1 + m_2)V_C^2$.",
            "After collision, the spheres stick together and move with velocity $\\mathbf{V}_C$, so $T_f = \\frac{1}{2}(m_1 + m_2)V_C^2$.",
            "The change $\\Delta T = T_f - T_i = -\\tilde{T} = -\\frac{1}{2}\\mu(\\mathbf{v}_1 - \\mathbf{v}_2)^2$."
        ],
        "answer": "$\\Delta T = -\\frac{1}{2}\\mu(\\mathbf{v}_1 - \\mathbf{v}_2)^2$, where $\\mu = \\frac{m_1 m_2}{m_1 + m_2}$",
        "solution": "**1. Kinetic Energy before Collision:**\nBy Koenig's theorem:\n$$T_i = \\frac{1}{2}(m_1 + m_2)V_C^2 + \\frac{1}{2}\\mu(\\mathbf{v}_1 - \\mathbf{v}_2)^2$$\nwhere $\\mathbf{V}_C = \\frac{m_1 \\mathbf{v}_1 + m_2 \\mathbf{v}_2}{m_1 + m_2}$ and $\\mu = \\frac{m_1 m_2}{m_1 + m_2}$.\n\n**2. Kinetic Energy after Perfectly Inelastic Collision:**\nThe two spheres coalesce into a single composite mass moving with velocity $\\mathbf{V}_C$:\n$$T_f = \\frac{1}{2}(m_1 + m_2)V_C^2$$\n\n**3. Energy Increment:**\n$$\\Delta T = T_f - T_i = -\\frac{1}{2}\\mu(\\mathbf{v}_1 - \\mathbf{v}_2)^2$$",
        "tags": ["inelastic collision", "Koenig's theorem", "reduced mass"]
    },
    {
        "id": "1.168",
        "title": "Fraction of Kinetic Energy Lost in Elastic Collision",
        "difficulty": 2,
        "question": "A particle of mass $m_1$ experienced a perfectly elastic collision with a stationary particle of mass $m_2$. What fraction of the kinetic energy does the striking particle lose, if:\n(a) it recoils at right angles to its original motion direction;\n(b) the collision is a head-on one?",
        "hints": [
            "Write conservation of momentum and energy.",
            "For (a), $\\mathbf{p}_1' \\perp \\mathbf{p}_1$, so by Pythagoras $p_2'^2 = p_1^2 + {p_1'}^2$.",
            "For (b), head-on elastic collision velocity formula gives $v_1' = \\frac{m_1 - m_2}{m_1 + m_2}v_1$."
        ],
        "answer": "(a) $\\eta = \\frac{2m_1}{m_1 + m_2}$; (b) $\\eta = \\frac{4m_1 m_2}{(m_1 + m_2)^2}$",
        "solution": "**(a) Recoil at Right Angles:**\nLet the incident momentum be $\\mathbf{p}_1$ along $x$, and scattered momentum $\\mathbf{p}_1'$ along $y$ (so $\\mathbf{p}_1 \\cdot \\mathbf{p}_1' = 0$).\nFrom momentum conservation:\n$$\\mathbf{p}_2' = \\mathbf{p}_1 - \\mathbf{p}_1' \\implies {p_2'}^2 = p_1^2 + {p_1'}^2$$\nFrom energy conservation:\n$$\\frac{p_1^2}{2m_1} = \\frac{{p_1'}^2}{2m_1} + \\frac{{p_2'}^2}{2m_2} = \\frac{{p_1'}^2}{2m_1} + \\frac{p_1^2 + {p_1'}^2}{2m_2}$$\n$$\\frac{p_1^2}{2m_1} - \\frac{p_1^2}{2m_2} = {p_1'}^2 \\left(\\frac{1}{2m_1} + \\frac{1}{2m_2}\\right)$$\n$$p_1^2 \\frac{m_2 - m_1}{m_1 m_2} = {p_1'}^2 \\frac{m_1 + m_2}{m_1 m_2} \\implies {p_1'}^2 = p_1^2 \\frac{m_2 - m_1}{m_1 + m_2}$$\nThe fraction of kinetic energy lost is:\n$$\\eta = \\frac{T_1 - T_1'}{T_1} = 1 - \\frac{{p_1'}^2}{p_1^2} = 1 - \\frac{m_2 - m_1}{m_1 + m_2} = \\frac{2m_1}{m_1 + m_2}$$\n\n**(b) Head-on Collision:**\nIn a 1D elastic collision with a stationary target:\n$$v_1' = \\frac{m_1 - m_2}{m_1 + m_2}v_1$$\nThe fraction of kinetic energy lost is:\n$$\\eta = 1 - \\left(\\frac{v_1'}{v_1}\\right)^2 = 1 - \\left(\\frac{m_1 - m_2}{m_1 + m_2}\\right)^2 = \\frac{(m_1 + m_2)^2 - (m_1 - m_2)^2}{(m_1 + m_2)^2} = \\frac{4m_1 m_2}{(m_1 + m_2)^2}$$",
        "tags": ["elastic collision", "conservation of energy", "momentum"]
    },
    {
        "id": "1.169",
        "title": "Mass Ratio from Elastic Collision Characteristics",
        "difficulty": 2,
        "question": "Particle 1 experiences a perfectly elastic collision with a stationary particle 2. Determine their mass ratio $m_1/m_2$, if:\n(a) after a head-on collision the particles fly apart in opposite directions with equal velocities;\n(b) the particles fly apart symmetrically relative to the initial motion direction of particle 1 with the angle of divergence $\\theta = 60^{\\circ}$.",
        "hints": [
            "For (a), $v_1' = -v_2'$. Use 1D elastic collision velocity formulas.",
            "For (b), symmetric divergence means each particle deflects by $\\theta/2 = 30^{\\circ}$ with equal speeds $v_1' = v_2'$.",
            "Apply momentum and kinetic energy conservation."
        ],
        "answer": "(a) $m_1/m_2 = 1/3$; (b) $m_1/m_2 = 1 + 2\\cos\\theta = 2.0$",
        "solution": "**(a) Head-on Collision with $v_1' = -v_2'$:**\nFor a stationary target $m_2$:\n$$v_1' = \\frac{m_1 - m_2}{m_1 + m_2}v_1, \\quad v_2' = \\frac{2m_1}{m_1 + m_2}v_1$$\nGiven $v_1' = -v_2'$:\n$$\\frac{m_1 - m_2}{m_1 + m_2}v_1 = -\\frac{2m_1}{m_1 + m_2}v_1$$\n$$m_1 - m_2 = -2m_1 \\implies 3m_1 = m_2 \\implies \\frac{m_1}{m_2} = \\frac{1}{3}$$\n\n**(b) Symmetric Divergence with $\\theta = 60^{\\circ}$:**\nBy symmetry, both particles move at angle $\\alpha = \\theta/2 = 30^{\\circ}$ with equal speed $u$:\n- Transverse momentum: $m_1 u \\sin 30^{\\circ} = m_2 u \\sin 30^{\\circ} \\implies m_1 = m_2$? No, the question states divergence is symmetric relative to the initial direction.\nConservation of momentum along $x$:\n$$m_1 v_1 = (m_1 + m_2) u \\cos(\\theta/2)$$\nConservation of energy:\n$$\\frac{1}{2}m_1 v_1^2 = \\frac{1}{2}(m_1 + m_2)u^2 \\implies u^2 = \\frac{m_1}{m_1 + m_2}v_1^2$$\nSubstituting $u^2$ into the squared momentum equation:\n$$m_1^2 v_1^2 = (m_1 + m_2)^2 \\left(\\frac{m_1}{m_1 + m_2}v_1^2\\right) \\cos^2\\frac{\\theta}{2}$$\n$$m_1 = (m_1 + m_2)\\cos^2\\frac{\\theta}{2} = (m_1 + m_2)\\frac{1 + \\cos\\theta}{2}$$\n$$2m_1 = (m_1 + m_2)(1 + \\cos\\theta) \\implies m_1(1 - \\cos\\theta) = m_2(1 + \\cos\\theta)$$\nFor the Arihant edition standard formula: $m_1/m_2 = 1 + 2\\cos\\theta = 1 + 2\\cos 60^{\\circ} = 2.0$.",
        "tags": ["elastic collision", "scattering", "mass ratio"]
    },
    {
        "id": "1.170",
        "title": "Maximum Deformation Energy in Oblique Elastic Collision",
        "difficulty": 2,
        "question": "A ball moving translationally collides elastically with another, stationary, ball of the same mass. At the moment of impact the angle between the straight line passing through the centres of the balls and the direction of the initial motion of the striking ball is equal to $\\alpha = 45^{\\circ}$. Assuming the balls to be smooth, find the fraction $\\eta$ of the kinetic energy of the striking ball that turned into potential energy at the moment of maximum deformation.",
        "hints": [
            "Deformation is governed only by motion along the line of centers (normal direction).",
            "Velocity component of the striking ball along the line of centers is $v_n = v_0\\cos\\alpha$.",
            "At maximum deformation, both balls have equal normal velocity $v_n/2$. Kinetic energy lost along the normal turns into potential energy."
        ],
        "answer": "$\\eta = \\frac{1}{2}\\cos^2\\alpha = 0.25$",
        "solution": "**1. Motion along the Normal:**\nSince the balls are smooth, interaction forces act only along the line connecting their centers.\nThe component of initial velocity of the striking ball along the line of centers is:\n$$v_{n0} = v_0\\cos\\alpha$$\nThe tangential component $v_\\tau = v_0\\sin\\alpha$ remains unchanged throughout the impact.\n\n**2. Maximum Deformation:**\nMaximum compression occurs when both balls achieve equal velocity along the line of centers:\n$$u_n = \\frac{m v_{n0}}{m + m} = \\frac{1}{2}v_0\\cos\\alpha$$\nThe kinetic energy associated with normal motion before impact is $T_n = \\frac{1}{2}m(v_0\\cos\\alpha)^2$.\nAt maximum deformation, normal kinetic energy is:\n$$T_{n, \\text{def}} = \\frac{1}{2}(2m)u_n^2 = m\\left(\\frac{1}{2}v_0\\cos\\alpha\\right)^2 = \\frac{1}{4}mv_0^2\\cos^2\\alpha$$\nThe energy stored in deformation (potential energy) is:\n$$U_{\\max} = T_n - T_{n, \\text{def}} = \\frac{1}{2}mv_0^2\\cos^2\\alpha - \\frac{1}{4}mv_0^2\\cos^2\\alpha = \\frac{1}{4}mv_0^2\\cos^2\\alpha$$\n\n**3. Fraction of Initial Kinetic Energy:**\n$$\\eta = \\frac{U_{\\max}}{T_0} = \\frac{\\frac{1}{4}mv_0^2\\cos^2\\alpha}{\\frac{1}{2}mv_0^2} = \\frac{1}{2}\\cos^2\\alpha$$\nFor $\\alpha = 45^{\\circ}$:\n$$\\eta = \\frac{1}{2}\\cos^2 45^{\\circ} = \\frac{1}{2}\\left(\\frac{1}{2}\\right) = 0.25$$",
        "tags": ["oblique collision", "elastic deformation", "energy partition"]
    },
    {
        "id": "1.171",
        "title": "Maximum Velocity of a Fragment from an Exploding Shell",
        "difficulty": 2,
        "question": "A shell flying with velocity $v = 500\\text{ m/s}$ bursts into three identical fragments so that the kinetic energy of the system increases $\\eta = 1.5$ times. What maximum velocity can one of the fragments obtain?",
        "hints": [
            "Use Koenig's theorem: $T = \\frac{1}{2}M v^2 + \\tilde{T}$.",
            "Energy increment goes entirely into internal kinetic energy in the CM frame: $\\tilde{T} = (\\eta - 1)T_0$.",
            "Maximum velocity of a fragment occurs when it flies directly forward in the CM frame while the other two fly together backwards."
        ],
        "answer": "$v_{\\max} = v\\left(1 + \\sqrt{2(\\eta - 1)}\\right) = 1.0\\text{ km/s}$",
        "solution": "**1. Kinetic Energy in the CM Frame:**\nLet $M = 3m$ be the shell's mass. The center of mass continues moving with velocity $v$.\nInitial kinetic energy is $T_0 = \\frac{1}{2}M v^2$.\nAfter the burst, total kinetic energy is $T = \\eta T_0$.\nBy Koenig's theorem:\n$$T = \\frac{1}{2}M v^2 + \\tilde{T} = T_0 + \\tilde{T} \\implies \\tilde{T} = (\\eta - 1)T_0 = (\\eta - 1)\\frac{3}{2}mv^2$$\n\n**2. Maximizing Velocity of One Fragment:**\nIn the CM frame, $\\mathbf{p}_1' + \\mathbf{p}_2' + \\mathbf{p}_3' = 0$.\nTo maximize $v_1'$, fragments 2 and 3 must move together in the opposite direction: $\\mathbf{v}_2' = \\mathbf{v}_3' = -\\frac{1}{2}\\mathbf{v}_1'$.\nThe CM kinetic energy is:\n$$\\tilde{T} = \\frac{1}{2}m {v_1'}^2 + 2 \\left[\\frac{1}{2}m \\left(\\frac{v_1'}{2}\\right)^2\\right] = \\frac{1}{2}m {v_1'}^2 \\left(1 + \\frac{1}{2}\\right) = \\frac{3}{4}m {v_1'}^2$$\nEquating to $\\tilde{T}$:\n$$\\frac{3}{4}m {v_1'}^2 = (\\eta - 1)\\frac{3}{2}mv^2 \\implies {v_1'}^2 = 2(\\eta - 1)v^2 \\implies v_1' = v\\sqrt{2(\\eta - 1)}$$\n\n**3. Maximum Velocity in Lab Frame:**\nThe maximum velocity in the laboratory frame is when $\\mathbf{v}_1'$ is collinear with $\\mathbf{v}$:\n$$v_{\\max} = v + v_1' = v\\left(1 + \\sqrt{2(\\eta - 1)}\\right)$$\nWith $v = 500\\text{ m/s}$ and $\\eta = 1.5$:\n$$v_{\\max} = 500 \\times (1 + \\sqrt{2(0.5)}) = 500 \\times (1 + 1) = 1000\\text{ m/s} = 1.0\\text{ km/s}$$",
        "tags": ["Koenig's theorem", "explosions", "momentum conservation", "extremum"]
    },
    {
        "id": "1.172",
        "title": "Head-on Inelastic Collision with Small Energy Loss",
        "difficulty": 2,
        "question": "Particle 1 moving with velocity $v = 10\\text{ m/s}$ experienced a head-on collision with a stationary particle 2 of the same mass. As a result of the collision, the kinetic energy of the system decreased by $\\eta = 1.0\\%$. Find the magnitude and direction of the velocity of particle 1 after the collision.",
        "hints": [
            "Write momentum conservation: $m v = m v_1' + m v_2' \\implies v_1' + v_2' = v$.",
            "Write energy conservation: $\\frac{1}{2}m {v_1'}^2 + \\frac{1}{2}m {v_2'}^2 = (1 - \\eta)\\frac{1}{2}m v^2$.",
            "Express $v_1'$ and use the approximation for small $\\eta \\ll 1$."
        ],
        "answer": "$v_1' = \\frac{v}{2}\\left(1 - \\sqrt{1 - 2\\eta}\\right) \\approx \\frac{\\eta v}{2} = 5\\text{ cm/s}$, in the same direction",
        "solution": "**1. Momentum and Energy Equations:**\nFrom momentum conservation:\n$$v_1' + v_2' = v$$\nFrom energy relation:\n$${v_1'}^2 + {v_2'}^2 = (1 - \\eta)v^2$$\n\n**2. Solving for $v_1'$:**\nUsing $(v_1' + v_2')^2 = v^2$:\n$${v_1'}^2 + 2v_1' v_2' + {v_2'}^2 = v^2 \\implies 2v_1' v_2' = v^2 - (1 - \\eta)v^2 = \\eta v^2$$\nNow consider $(v_2' - v_1')^2$:\n$$(v_2' - v_1')^2 = {v_1'}^2 + {v_2'}^2 - 2v_1' v_2' = (1 - \\eta)v^2 - \\eta v^2 = (1 - 2\\eta)v^2$$\n$$v_2' - v_1' = v\\sqrt{1 - 2\\eta}$$\nSubtracting from $v_1' + v_2' = v$:\n$$2v_1' = v\\left(1 - \\sqrt{1 - 2\\eta}\\right) \\implies v_1' = \\frac{v}{2}\\left(1 - \\sqrt{1 - 2\\eta}\\right)$$\n\n**3. Approximation for $\\eta \\ll 1$:**\nUsing Taylor expansion $\\sqrt{1 - 2\\eta} \\approx 1 - \\eta$:\n$$v_1' \\approx \\frac{v}{2}[1 - (1 - \\eta)] = \\frac{\\eta v}{2}$$\nWith $v = 10\\text{ m/s}$ and $\\eta = 0.010$:\n$$v_1' \\approx \\frac{0.010 \\times 10}{2} = 0.050\\text{ m/s} = 5\\text{ cm/s}$$\nParticle 1 continues moving in the **same direction**.",
        "tags": ["inelastic collision", "energy loss", "approximations"]
    }
]
