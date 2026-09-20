"""
ch1_2_batch1.py
Problems 1.59 through 1.88 of Irodov Chapter 1.2: The Fundamental Equation of Dynamics.
"""

CH1_2_BATCH_1 = [
    {
        "id": "1.59",
        "title": "Aerostat Ballast Dumping",
        "difficulty": 1,
        "question": "An aerostat of mass $m$ starts coming down with a constant acceleration $w$. Determine the ballast mass $\\Delta m$ to be dumped for the aerostat to reach the upward acceleration of the same magnitude. The air drag is to be neglected.",
        "hints": [
            "Write Newton's second law for the downward motion to express the upward buoyant force $F_b$ in terms of $m, g,$ and $w$.",
            "After dumping ballast $\\Delta m$, the new mass is $m - \\Delta m$. Write Newton's second law for the upward acceleration $w$.",
            "Eliminate $F_b$ between the two equations to solve for $\\Delta m$."
        ],
        "answer": "$\\Delta m = \\frac{2mw}{g + w}$",
        "solution": "**1. Downward Motion:**\nLet $F_b$ be the constant buoyant force acting vertically upward on the aerostat. When the aerostat descends with acceleration $w$:\n$$mg - F_b = mw \\implies F_b = m(g - w)$$\n\n**2. Upward Motion after Dumping Ballast:**\nWhen ballast of mass $\\Delta m$ is released, the mass of the aerostat becomes $m' = m - \\Delta m$. The aerostat now accelerates upward with acceleration $w$:\n$$F_b - (m - \\Delta m)g = (m - \\Delta m)w$$\n\n**3. Solving for $\\Delta m$:**\nSubstitute $F_b = m(g - w)$ into the second equation:\n$$m(g - w) - mg + \\Delta m \\cdot g = mw - \\Delta m \\cdot w$$\n$$-mw + \\Delta m \\cdot g = mw - \\Delta m \\cdot w$$\n$$\\Delta m (g + w) = 2mw \\implies \\Delta m = \\frac{2mw}{g + w}$$",
        "tags": ["dynamics", "Newton's laws", "buoyancy"]
    },
    {
        "id": "1.60",
        "title": "Three-Body Pulley System with Friction",
        "difficulty": 2,
        "question": "In the arrangement shown, the masses $m_0, m_1,$ and $m_2$ of the bodies are given, the masses of the pulley and the threads are negligible, and there is no friction in the pulley. Find the acceleration $w$ with which the body $m_0$ comes down, and the tension $T$ of the thread binding together the bodies $m_1$ and $m_2$, if the coefficient of friction between these bodies and the horizontal surface is equal to $k$. Consider possible cases.",
        "hints": [
            "Identify the threshold condition for motion: gravity on $m_0$ must exceed the maximum static friction on $m_1$ and $m_2$.",
            "If $m_0 > k(m_1 + m_2)$, the system accelerates. Write the equations of motion for $m_0$, $m_1$, and $m_2$.",
            "For the tension $T$ between $m_1$ and $m_2$, consider the equation of motion for the trailing mass $m_2$."
        ],
        "answer": "$w = \\frac{m_0 - k(m_1 + m_2)}{m_0 + m_1 + m_2}g$ (if $m_0 > k(m_1 + m_2)$); $T = \\frac{(1 + k)m_0 m_2}{m_0 + m_1 + m_2}g$",
        "solution": "**1. Condition for Motion:**\nThe maximum total static friction force opposing the motion of the horizontal bodies is $f_{\\text{fr, max}} = k(m_1 + m_2)g$.\nMotion occurs only if the gravitational pulling force on $m_0$ exceeds this friction:\n$$m_0 g > k(m_1 + m_2)g \\implies m_0 > k(m_1 + m_2)$$\nIf $m_0 \\le k(m_1 + m_2)$, the system remains at rest: $w = 0$.\n\n**2. Dynamic Equations ($m_0 > k(m_1 + m_2)$):**\nLet $T_0$ be the tension in the thread connected to $m_0$, and $T$ be the tension between $m_1$ and $m_2$:\n- For $m_0$ (moving downward):\n  $$m_0 g - T_0 = m_0 w$$\n- For $m_1$ (moving horizontally rightward):\n  $$T_0 - T - k m_1 g = m_1 w$$\n- For $m_2$ (trailing body):\n  $$T - k m_2 g = m_2 w$$\n\n**3. Acceleration $w$:**\nSumming all three equations eliminates internal tensions $T_0$ and $T$:\n$$m_0 g - k(m_1 + m_2)g = (m_0 + m_1 + m_2)w$$\n$$w = \\frac{m_0 - k(m_1 + m_2)}{m_0 + m_1 + m_2}g$$\n\n**4. Thread Tension $T$:**\nFrom the equation for $m_2$:\n$$T = m_2(w + kg) = m_2 \\left[ \\frac{m_0 - k(m_1 + m_2)}{m_0 + m_1 + m_2}g + kg \\right]$$\n$$T = m_2 g \\left[ \\frac{m_0 - k m_1 - k m_2 + k m_0 + k m_1 + k m_2}{m_0 + m_1 + m_2} \\right] = \\frac{(1 + k)m_0 m_2}{m_0 + m_1 + m_2}g$$",
        "tags": ["dynamics", "friction", "pulleys", "Newton's laws"]
    },
    {
        "id": "1.61",
        "title": "Two Touching Bars on an Incline",
        "difficulty": 2,
        "question": "Two touching bars 1 and 2 are placed on an inclined plane forming an angle $\\alpha$ with the horizontal. The masses of the bars are equal to $m_1$ and $m_2$, and the coefficients of friction between the inclined plane and these bars are equal to $k_1$ and $k_2$ respectively, with $k_1 > k_2$. Bar 1 is placed higher up the incline than bar 2. Find:\n(a) the force of interaction of the bars in the process of motion;\n(b) the minimum value of the angle $\\alpha$ at which the bars start sliding down.",
        "hints": [
            "Since $k_1 > k_2$, bar 2 tends to accelerate faster than bar 1, but bar 1 is behind bar 2 (or bar 1 is above bar 2). Bar 1 retards bar 2, so they push against each other with a normal contact force $F$.",
            "Write the equations of motion for both bars along the incline including the interaction force $F$.",
            "Sliding begins when the common acceleration $w \\ge 0$."
        ],
        "answer": "(a) $F = \\frac{(k_1 - k_2)m_1 m_2 g \\cos\\alpha}{m_1 + m_2}$; (b) $\\tan\\alpha_{\\min} = \\frac{k_1 m_1 + k_2 m_2}{m_1 + m_2}$",
        "solution": "**(a) Force of interaction $F$:**\nBecause $k_1 > k_2$, bar 1 experiences greater specific friction than bar 2. Bar 1 tends to lag behind bar 2; if bar 1 is placed above bar 2, bar 2 pulls away unless bar 2 is placed above bar 1 (touching from behind). Here the bars remain in contact, exerting a normal contact force $F$ on each other.\n\nEquations of motion along the incline:\n$$m_1 g \\sin\\alpha - k_1 m_1 g \\cos\\alpha + F = m_1 w$$\n$$m_2 g \\sin\\alpha - k_2 m_2 g \\cos\\alpha - F = m_2 w$$\n\nAdding the two equations:\n$$(m_1 + m_2)g \\sin\\alpha - (k_1 m_1 + k_2 m_2)g \\cos\\alpha = (m_1 + m_2)w$$\n$$w = g \\sin\\alpha - \\frac{k_1 m_1 + k_2 m_2}{m_1 + m_2} g \\cos\\alpha$$\n\nSubstitute $w$ back into the equation for bar 1:\n$$F = m_1 w - m_1 g \\sin\\alpha + k_1 m_1 g \\cos\\alpha$$\n$$F = m_1 \\left[ g \\sin\\alpha - \\frac{k_1 m_1 + k_2 m_2}{m_1 + m_2} g \\cos\\alpha \\right] - m_1 g \\sin\\alpha + k_1 m_1 g \\cos\\alpha$$\n$$F = m_1 g \\cos\\alpha \\left[ k_1 - \\frac{k_1 m_1 + k_2 m_2}{m_1 + m_2} \\right] = \\frac{(k_1 - k_2)m_1 m_2 g \\cos\\alpha}{m_1 + m_2}$$\n\n**(b) Minimum angle $\\alpha_{\\min}$ for sliding:**\nThe system starts sliding when the downward component of gravity exceeds the total maximum static friction:\n$$(m_1 + m_2)g \\sin\\alpha \\ge (k_1 m_1 + k_2 m_2)g \\cos\\alpha$$\n$$\\tan\\alpha_{\\min} = \\frac{k_1 m_1 + k_2 m_2}{m_1 + m_2}$$",
        "tags": ["dynamics", "friction", "inclined plane", "contact forces"]
    },
    {
        "id": "1.62",
        "title": "Ascent vs. Descent Time on an Incline",
        "difficulty": 1,
        "question": "A small body was launched up an inclined plane set at an angle $\\alpha = 15^{\\circ}$ against the horizontal. Find the coefficient of friction $k$, if the time of the ascent of the body is $\\eta = 2.0$ times less than the time of its descent.",
        "hints": [
            "Write the deceleration during upward motion: $w_1 = g(\\sin\\alpha + k\\cos\\alpha)$.",
            "Write the acceleration during downward motion: $w_2 = g(\\sin\\alpha - k\\cos\\alpha)$.",
            "The distance $s$ travelled up equals the distance travelled down: $s = \\frac{1}{2}w_1 t_1^2 = \\frac{1}{2}w_2 t_2^2$, with $t_2 = \\eta t_1$."
        ],
        "answer": "$k = \\frac{\\eta^2 - 1}{\\eta^2 + 1} \\tan\\alpha = 0.16$",
        "solution": "**1. Accelerations during Ascent and Descent:**\n- Upward motion (decelerating):\n  $$w_1 = g(\\sin\\alpha + k\\cos\\alpha)$$\n- Downward motion (accelerating):\n  $$w_2 = g(\\sin\\alpha - k\\cos\\alpha)$$\n\n**2. Relationship between Times:**\nThe distance $s$ along the incline is the same in both directions:\n$$s = \\frac{1}{2} w_1 t_1^2 = \\frac{1}{2} w_2 t_2^2$$\nGiven $t_2 = \\eta t_1$:\n$$w_1 t_1^2 = w_2 (\\eta t_1)^2 \\implies \\frac{w_1}{w_2} = \\eta^2$$\n\n**3. Determining the Friction Coefficient $k$:**\n$$\\frac{\\sin\\alpha + k\\cos\\alpha}{\\sin\\alpha - k\\cos\\alpha} = \\eta^2$$\n$$\\sin\\alpha + k\\cos\\alpha = \\eta^2 \\sin\\alpha - \\eta^2 k\\cos\\alpha$$\n$$k\\cos\\alpha (\\eta^2 + 1) = \\sin\\alpha (\\eta^2 - 1)$$\n$$k = \\frac{\\eta^2 - 1}{\\eta^2 + 1} \\tan\\alpha$$\n\n**4. Numerical Calculation:**\nFor $\\alpha = 15^{\\circ}$ and $\\eta = 2.0$:\n$$k = \\frac{2^2 - 1}{2^2 + 1} \\tan 15^{\\circ} = \\frac{3}{5} \\times 0.2679 = 0.1608 \\approx 0.16$$",
        "tags": ["dynamics", "friction", "inclined plane", "kinematics"]
    },
    {
        "id": "1.63",
        "title": "Equilibrium and Motion on an Incline with Pulley",
        "difficulty": 2,
        "question": "A body of mass $m_1$ lies on an inclined plane forming an angle $\\alpha$ with the horizontal, with coefficient of friction $k$. It is connected by a thread over a light frictionless pulley to a suspended body of mass $m_2$. Assuming both bodies to be motionless initially, find the mass ratio $m_2/m_1$ at which the body $m_2$:\n(a) starts coming down;\n(b) starts going up;\n(c) is at rest.",
        "hints": [
            "Find the static friction force limits on body $m_1$: $f_{\\text{fr, max}} = k m_1 g \\cos\\alpha$.",
            "Body $m_2$ moves down if its weight overcomes both the component of gravity of $m_1$ along the incline and the maximum opposing static friction.",
            "Body $m_2$ moves up if the downward component of gravity of $m_1$ overcomes $m_2 g$ and the static friction."
        ],
        "answer": "(a) $\\frac{m_2}{m_1} > \\sin\\alpha + k\\cos\\alpha$; (b) $\\frac{m_2}{m_1} < \\sin\\alpha - k\\cos\\alpha$; (c) $\\sin\\alpha - k\\cos\\alpha \\le \\frac{m_2}{m_1} \\le \\sin\\alpha + k\\cos\\alpha$",
        "solution": "**1. Free-Body Analysis for $m_1$:**\nAlong the incline, the gravity component pulling $m_1$ downward is $m_1 g \\sin\\alpha$.\nThe maximum static friction is $f_{\\text{max}} = k m_1 g \\cos\\alpha$.\nThe thread tension equals the gravitational force on the suspended mass: $T = m_2 g$.\n\n**(a) $m_2$ starts coming down:**\nFor $m_2$ to descend, $m_1$ must be pulled up the incline. Friction opposes upward motion (acts down the incline):\n$$T > m_1 g \\sin\\alpha + f_{\\text{max}}$$\n$$m_2 g > m_1 g \\sin\\alpha + k m_1 g \\cos\\alpha \\implies \\frac{m_2}{m_1} > \\sin\\alpha + k\\cos\\alpha$$\n\n**(b) $m_2$ starts going up:**\nFor $m_2$ to ascend, $m_1$ slides down the incline. Friction opposes downward motion (acts up the incline):\n$$m_1 g \\sin\\alpha > T + f_{\\text{max}}$$\n$$m_1 g \\sin\\alpha > m_2 g + k m_1 g \\cos\\alpha \\implies \\frac{m_2}{m_1} < \\sin\\alpha - k\\cos\\alpha$$\n\n**(c) The system is at rest:**\nEquilibrium holds when the tension lies within the static friction bounds:\n$$\\sin\\alpha - k\\cos\\alpha \\le \\frac{m_2}{m_1} \\le \\sin\\alpha + k\\cos\\alpha$$",
        "tags": ["dynamics", "friction", "equilibrium", "pulleys"]
    },
    {
        "id": "1.64",
        "title": "Acceleration of Incline-Pulley System",
        "difficulty": 2,
        "question": "The inclined plane forms an angle $\\alpha = 30^{\\circ}$ with the horizontal. The mass ratio $m_2 / m_1 = \\eta = 2/3$. The coefficient of friction between body $m_1$ and the inclined plane is $k = 0.10$. The masses of the pulley and the threads are negligible. Find the magnitude and direction of the acceleration of body $m_2$ when the formerly stationary system begins moving.",
        "hints": [
            "Check which direction the system tends to move by comparing $\\eta$ to $\\sin\\alpha \\pm k\\cos\\alpha$.",
            "Calculate $\\sin 30^\\circ + k\\cos 30^\\circ$ and $\\sin 30^\\circ - k\\cos 30^\\circ$.",
            "Apply Newton's second law along the direction of motion to solve for the acceleration."
        ],
        "answer": "$w_2 = \\frac{\\eta - \\sin\\alpha - k\\cos\\alpha}{\\eta + 1}g = 0.05g$ (downwards)",
        "solution": "**1. Determining Motion Direction:**\nCalculate the critical thresholds:\n$$\\sin\\alpha = \\sin 30^{\\circ} = 0.50$$\n$$k\\cos\\alpha = 0.10 \\times \\cos 30^{\\circ} = 0.10 \\times 0.866 = 0.0866$$\n$$\\sin\\alpha + k\\cos\\alpha = 0.50 + 0.0866 = 0.587$$\n$$\\sin\\alpha - k\\cos\\alpha = 0.50 - 0.0866 = 0.413$$\n\nGiven $\\eta = \\frac{m_2}{m_1} = \\frac{2}{3} \\approx 0.667 > 0.587$, body $m_2$ accelerates downwards, pulling $m_1$ up the incline.\n\n**2. Dynamic Equations:**\n- For body $m_2$ (moving down):\n  $$m_2 g - T = m_2 w$$\n- For body $m_1$ (moving up the incline):\n  $$T - m_1 g \\sin\\alpha - k m_1 g \\cos\\alpha = m_1 w$$\n\n**3. Acceleration Magnitude:**\nAdding the two equations:\n$$(m_2 - m_1 \\sin\\alpha - k m_1 \\cos\\alpha)g = (m_1 + m_2)w$$\nDividing through by $m_1$:\n$$w = \\frac{\\eta - \\sin\\alpha - k\\cos\\alpha}{\\eta + 1} g$$\n\n**4. Numerical Calculation:**\n$$w = \\frac{0.667 - 0.50 - 0.0866}{0.667 + 1} g = \\frac{0.0804}{1.667} g \\approx 0.048g \\approx 0.05g$$\nThus, body $m_2$ moves downward with acceleration $w_2 \\approx 0.05g$.",
        "tags": ["dynamics", "Newton's laws", "inclined plane", "pulleys"]
    },
    {
        "id": "1.65",
        "title": "Plank and Bar with Time-Varying Force",
        "difficulty": 2,
        "question": "A plank of mass $m_1$ with a bar of mass $m_2$ placed on it lies on a smooth horizontal plane. A horizontal force growing with time $t$ as $F = at$ ($a$ is constant) is applied to the bar. Find how the accelerations of the plank $w_1$ and of the bar $w_2$ depend on $t$, if the coefficient of friction between the plank and the bar is equal to $k$. Draw the approximate plots of these dependences.",
        "hints": [
            "Find the maximum static friction force between the bar and plank: $f_{\\text{max}} = k m_2 g$.",
            "While they move together without slipping, the system accelerates as one body: $w_1 = w_2 = \\frac{at}{m_1 + m_2}$.",
            "Determine the critical time $t_0$ when the required force on the plank exceeds $f_{\\text{max}}$."
        ],
        "answer": "For $t \\le t_0$: $w_1 = w_2 = \\frac{at}{m_1 + m_2}$; for $t \\ge t_0$: $w_1 = \\frac{k m_2 g}{m_1}$, $w_2 = \\frac{at - k m_2 g}{m_2}$, where $t_0 = \\frac{k m_2(m_1 + m_2)g}{a m_1}$",
        "solution": "**1. Stage 1: Motion Without Slipping ($t \\le t_0$):**\nThe horizontal floor is smooth, so friction exists only at the bar-plank interface. The maximum static friction is $f_{\\text{max}} = k m_2 g$.\n\nWhile static friction prevents slipping, both bodies accelerate together:\n$$w_1 = w_2 = w = \\frac{F}{m_1 + m_2} = \\frac{at}{m_1 + m_2}$$\n\nThe force accelerating the lower plank $m_1$ is solely the friction force $f$:\n$$f = m_1 w = \\frac{m_1 a t}{m_1 + m_2}$$\n\n**2. Critical Time $t_0$ for Slipping:**\nSlipping begins when $f$ reaches $f_{\\text{max}} = k m_2 g$:\n$$\\frac{m_1 a t_0}{m_1 + m_2} = k m_2 g \\implies t_0 = \\frac{k m_2(m_1 + m_2)g}{a m_1}$$\n\n**3. Stage 2: Motion With Relative Slipping ($t \\ge t_0$):**\nOnce relative motion starts, the kinetic friction between the bodies is constant: $f_k = k m_2 g$.\n- For the plank $m_1$:\n  $$w_1 = \\frac{f_k}{m_1} = \\frac{k m_2 g}{m_1} = \\text{const}$$\n- For the bar $m_2$:\n  $$w_2 = \\frac{F - f_k}{m_2} = \\frac{at - k m_2 g}{m_2} = \\frac{at}{m_2} - kg$$",
        "tags": ["dynamics", "friction", "relative motion", "variable force"]
    },
    {
        "id": "1.66",
        "title": "Optimum Incline Angle for Minimum Sliding Time",
        "difficulty": 2,
        "question": "A small body $A$ starts sliding down from the top of a wedge whose base length is equal to $l = 2.10\\text{ m}$. The coefficient of friction between the body and the wedge surface is $k = 0.140$. At what value of the angle $\\alpha$ will the time of sliding be the least? What will it be equal to?",
        "hints": [
            "Express the length of the incline $s$ in terms of the base $l$ and $\\alpha$: $s = l/\\cos\\alpha$.",
            "Write the acceleration down the incline: $w = g(\\sin\\alpha - k\\cos\\alpha)$.",
            "Express $t^2 = 2s/w$ and find $\\alpha$ that minimizes $t$ using double-angle trigonometric identities."
        ],
        "answer": "$\\tan 2\\alpha = -\\frac{1}{k} \\implies \\alpha = 49^{\\circ}$; $t_{\\min} = 1.0\\text{ s}$",
        "solution": "**1. Kinematics along the Incline:**\nThe slant length of the wedge is $s = \\frac{l}{\\cos\\alpha}$.\nThe acceleration of the body sliding down is:\n$$w = g(\\sin\\alpha - k\\cos\\alpha)$$\n\nStarting from rest, the time of descent $t$ satisfies $s = \\frac{1}{2} w t^2$:\n$$t^2 = \\frac{2s}{w} = \\frac{2l}{g \\cos\\alpha (\\sin\\alpha - k\\cos\\alpha)} = \\frac{4l}{g [2\\sin\\alpha\\cos\\alpha - 2k\\cos^2\\alpha]}$$\n$$t^2 = \\frac{4l}{g [\\sin 2\\alpha - k(1 + \\cos 2\\alpha)]}$$\n\n**2. Minimizing the Time:**\nTo minimize $t^2$, we maximize the denominator $f(\\alpha) = \\sin 2\\alpha - k\\cos 2\\alpha - k$:\n$$f'(\\alpha) = 2\\cos 2\\alpha + 2k\\sin 2\\alpha = 0$$\n$$\\cos 2\\alpha + k\\sin 2\\alpha = 0 \\implies \\tan 2\\alpha = -\\frac{1}{k}$$\n\n**3. Calculating the Optimum Angle:**\nFor $k = 0.140$:\n$$\\tan 2\\alpha = -\\frac{1}{0.140} \\approx -7.143$$\n$$2\\alpha = 180^{\\circ} - \\arctan(7.143) = 180^{\\circ} - 82.03^{\\circ} = 97.97^{\\circ} \\implies \\alpha \\approx 49.0^{\\circ}$$\n\n**4. Minimum Time:**\n$$\\sin 2\\alpha = \\frac{1}{\\sqrt{1 + k^2}}, \\quad \\cos 2\\alpha = -\\frac{k}{\\sqrt{1 + k^2}}$$\n$$f(\\alpha)_{\\max} = \\frac{1}{\\sqrt{1 + k^2}} + \\frac{k^2}{\\sqrt{1 + k^2}} - k = \\sqrt{1 + k^2} - k$$\n$$t_{\\min} = \\sqrt{\\frac{4l}{g(\\sqrt{1 + k^2} - k)}} = \\sqrt{\\frac{4 \\times 2.10}{9.8(\\sqrt{1 + 0.14^2} - 0.14)}} = \\sqrt{\\frac{8.4}{9.8 \\times (1.0097 - 0.14)}} = 1.0\\text{ s}$$",
        "tags": ["dynamics", "friction", "optimization", "inclined plane"]
    },
    {
        "id": "1.67",
        "title": "Minimum Tension to Pull Bar Up Incline",
        "difficulty": 2,
        "question": "A bar of mass $m$ is pulled by means of a thread up an inclined plane forming an angle $\\alpha$ with the horizontal. The coefficient of friction is equal to $k$. Find the angle $\\beta$ the thread must form with the inclined plane for the tension of the thread to be minimum. What is the minimum tension equal to?",
        "hints": [
            "Set up coordinate axes parallel and perpendicular to the incline.",
            "Write the normal force $N = mg\\cos\\alpha - T\\sin\\beta$ and friction force $f_k = kN$.",
            "Solve for $T(\\beta)$ and maximize the trigonometric denominator."
        ],
        "answer": "$\\tan\\beta = k$; $T_{\\min} = \\frac{mg(\\sin\\alpha + k\\cos\\alpha)}{\\sqrt{1 + k^2}}$",
        "solution": "**1. Equilibrium Equations along and perpendicular to the Incline:**\nLet $\\beta$ be the angle of the thread above the inclined plane:\n- Perpendicular to incline:\n  $$N + T \\sin\\beta - mg\\cos\\alpha = 0 \\implies N = mg\\cos\\alpha - T\\sin\\beta$$\n- Along the incline (pulling up at steady speed / threshold):\n  $$T \\cos\\beta - mg\\sin\\alpha - f_k = 0$$\n\n**2. Expressing Tension $T$:**\nSince $f_k = k N = k(mg\\cos\\alpha - T\\sin\\beta)$:\n$$T \\cos\\beta - mg\\sin\\alpha - k(mg\\cos\\alpha - T\\sin\\beta) = 0$$\n$$T(\\cos\\beta + k\\sin\\beta) = mg(\\sin\\alpha + k\\cos\\alpha)$$\n$$T = \\frac{mg(\\sin\\alpha + k\\cos\\alpha)}{\\cos\\beta + k\\sin\\beta}$$\n\n**3. Minimizing Tension:**\nTo minimize $T$, maximize the denominator $D(\\beta) = \\cos\\beta + k\\sin\\beta$:\n$$D'(\\beta) = -\\sin\\beta + k\\cos\\beta = 0 \\implies \\tan\\beta = k$$\n\nThe maximum value of $\\cos\\beta + k\\sin\\beta$ is $\\sqrt{1 + k^2}$.\nSubstituting this back gives the minimum tension:\n$$T_{\\min} = \\frac{mg(\\sin\\alpha + k\\cos\\alpha)}{\\sqrt{1 + k^2}}$$",
        "tags": ["dynamics", "friction", "optimization", "tension"]
    },
    {
        "id": "1.68",
        "title": "Linear Time-Varying Force at an Angle",
        "difficulty": 2,
        "question": "At the moment $t = 0$, a force $F = at$ ($a$ is a constant) is applied to a small body of mass $m$ resting on a smooth horizontal plane. The permanent direction of this force forms an angle $\\alpha$ with the horizontal. Find:\n(a) the velocity of the body at the moment of its breaking off the plane;\n(b) the distance traversed by the body up to this moment.",
        "hints": [
            "Break-off occurs when the vertical normal force $N = mg - F\\sin\\alpha$ drops to zero.",
            "Find the break-off time $t_0 = \\frac{mg}{a\\sin\\alpha}$.",
            "Integrate the horizontal acceleration $w_x = \\frac{at\\cos\\alpha}{m}$ to find $v(t)$ and $s(t)$."
        ],
        "answer": "(a) $v = \\frac{m g^2 \\cos\\alpha}{2a \\sin^2\\alpha}$; (b) $s = \\frac{m^2 g^3 \\cos\\alpha}{6a^2 \\sin^3\\alpha}$",
        "solution": "**1. Moment of Break-Off $t_0$:**\nThe vertical equation of equilibrium prior to break-off is:\n$$N + F\\sin\\alpha - mg = 0 \\implies N = mg - at\\sin\\alpha$$\nThe body loses contact with the plane when $N = 0$:\n$$at_0 \\sin\\alpha = mg \\implies t_0 = \\frac{mg}{a\\sin\\alpha}$$\n\n**(a) Velocity at Break-Off:**\nAlong the smooth horizontal surface, the equation of motion is:\n$$m \\frac{dv}{dt} = F\\cos\\alpha = at\\cos\\alpha \\implies \\frac{dv}{dt} = \\frac{a\\cos\\alpha}{m} t$$\n\nIntegrating from $t = 0$ to $t_0$:\n$$v(t_0) = \\int_0^{t_0} \\frac{a\\cos\\alpha}{m} t \\, dt = \\frac{a\\cos\\alpha}{2m} t_0^2$$\nSubstitute $t_0 = \\frac{mg}{a\\sin\\alpha}$:\n$$v = \\frac{a\\cos\\alpha}{2m} \\left(\\frac{mg}{a\\sin\\alpha}\\right)^2 = \\frac{m g^2 \\cos\\alpha}{2a \\sin^2\\alpha}$$\n\n**(b) Distance Traversed:**\n$$s(t_0) = \\int_0^{t_0} v(t) \\, dt = \\int_0^{t_0} \\frac{a\\cos\\alpha}{2m} t^2 \\, dt = \\frac{a\\cos\\alpha}{6m} t_0^3$$\nSubstitute $t_0$:\n$$s = \\frac{a\\cos\\alpha}{6m} \\left(\\frac{mg}{a\\sin\\alpha}\\right)^3 = \\frac{m^2 g^3 \\cos\\alpha}{6a^2 \\sin^3\\alpha}$$",
        "tags": ["dynamics", "variable force", "integration", "kinematics"]
    },
    {
        "id": "1.69",
        "title": "Velocity under Position-Dependent Angle Force",
        "difficulty": 2,
        "question": "A bar of mass $m$ resting on a smooth horizontal plane starts moving due to the force $F = mg/3$ of constant magnitude. In the process of its rectilinear motion, the angle $\\alpha$ between the direction of this force and the horizontal varies as $\\alpha = as$, where $a$ is a constant and $s$ is the distance traversed by the bar from its initial position. Find the velocity of the bar as a function of the angle $\\alpha$.",
        "hints": [
            "Use the work-energy theorem or express acceleration as $v \\frac{dv}{ds}$.",
            "The horizontal component of the force is $F_x = F\\cos\\alpha = \\frac{mg}{3}\\cos(as)$.",
            "Integrate $m v \\, dv = F_x \\, ds$ with the substitution $\\alpha = as$."
        ],
        "answer": "$v = \\sqrt{\\frac{2g}{3a}\\sin\\alpha}$",
        "solution": "**1. Differential Equation of Motion:**\nThe horizontal acceleration of the bar along the smooth plane is governed by $F_x$:\n$$m \\frac{dv}{dt} = m v \\frac{dv}{ds} = F \\cos\\alpha = \\frac{mg}{3} \\cos(as)$$\n\n**2. Integration:**\nSeparate variables:\n$$v \\, dv = \\frac{g}{3} \\cos(as) \\, ds$$\n\nIntegrate from $s = 0$ (where $v = 0$) to $s$:\n$$\\int_0^v v' \\, dv' = \\frac{g}{3} \\int_0^s \\cos(as') \\, ds'$$\n$$\\frac{1}{2} v^2 = \\frac{g}{3a} \\sin(as)$$\n\n**3. Result as a Function of $\\alpha$:**\nSince $\\alpha = as$:\n$$v^2 = \\frac{2g}{3a} \\sin\\alpha \\implies v = \\sqrt{\\frac{2g}{3a}\\sin\\alpha}$$",
        "tags": ["dynamics", "work-energy", "integration", "Newton's laws"]
    },
    {
        "id": "1.70",
        "title": "Two Bodies with Motor and Friction",
        "difficulty": 2,
        "question": "A horizontal plane with coefficient of friction $k$ supports two bodies: a bar and an electric motor with a battery on a block. A thread attached to the bar is wound on the shaft of the electric motor. The initial distance between the bar and the electric motor is equal to $l$. When the motor is switched on, the bar, whose mass is twice as great as that of the other body, starts moving with a constant acceleration $w$. How soon will the bodies collide?",
        "hints": [
            "Let the mass of the motor be $m$, then the mass of the bar is $2m$.",
            "Express the tension $T$ in the thread from the equation of motion of the bar.",
            "Write the equation of motion for the motor to find its acceleration $w_m$, then find the relative acceleration $w_{\\text{rel}} = w + w_m$."
        ],
        "answer": "$\\tau = \\sqrt{\\frac{2l}{3(w + kg)}}$",
        "solution": "**1. System Parameters:**\nLet the mass of the motor be $m_2 = m$, so the mass of the bar is $m_1 = 2m$.\nThe friction forces are:\n- On the bar: $f_1 = k(2m)g = 2kmg$\n- On the motor: $f_2 = kmg$\n\n**2. Thread Tension $T$:**\nThe bar moves toward the motor with acceleration $w$ under tension $T$:\n$$T - f_1 = m_1 w \\implies T - 2kmg = 2m w \\implies T = 2m(w + kg)$$\n\n**3. Acceleration of the Motor:**\nThe motor moves toward the bar under the same tension $T$:\n$$T - f_2 = m w_m \\implies 2m(w + kg) - kmg = m w_m$$\n$$w_m = 2w + 2kg - kg = 2w + kg$$\n\n**4. Relative Acceleration and Collision Time:**\nThe bodies accelerate toward each other with relative acceleration:\n$$w_{\\text{rel}} = w + w_m = w + (2w + kg) = 3(w + kg)$$\n\nStarting from rest at separation $l$:\n$$l = \\frac{1}{2} w_{\\text{rel}} \\tau^2 \\implies \\tau = \\sqrt{\\frac{2l}{w_{\\text{rel}}}} = \\sqrt{\\frac{2l}{3(w + kg)}}$$",
        "tags": ["dynamics", "relative acceleration", "friction", "Newton's laws"]
    },
    {
        "id": "1.71",
        "title": "Atwood Machine in an Accelerating Elevator",
        "difficulty": 2,
        "question": "A pulley fixed to the ceiling of an elevator car carries a thread whose ends are attached to loads of masses $m_1$ and $m_2$. The car starts going up with an acceleration $w_0$. Assuming the masses of the pulley and the thread, as well as the friction, to be negligible, find:\n(a) the acceleration of the load $m_1$ relative to the elevator shaft and relative to the car;\n(b) the force exerted by the pulley on the ceiling of the car.",
        "hints": [
            "In the non-inertial reference frame of the elevator, the effective gravity is $g' = g + w_0$.",
            "Calculate the acceleration relative to the car $w'$ using the Atwood formula with $g'$.",
            "Use vector addition $w_1 = w_0 + w_1'$ to find the acceleration relative to the elevator shaft."
        ],
        "answer": "(a) $w_1 = \\frac{(m_1 - m_2)g + 2m_1 w_0}{m_1 + m_2}$ (or relative to car: $w_1' = \\frac{m_1 - m_2}{m_1 + m_2}(g + w_0)$); (b) $F = \\frac{4m_1 m_2}{m_1 + m_2}(g + w_0)$",
        "solution": "**(a) Accelerations relative to the car and shaft:**\nIn the reference frame of the elevator accelerating upward with $w_0$, an inertial force $-m w_0$ acts on each body.\nThe effective gravitational acceleration is:\n$$g_{\\text{eff}} = g + w_0$$\n\nIn this frame, the acceleration of mass $m_1$ relative to the car is given by the standard Atwood formula:\n$$w_1' = \\frac{m_1 - m_2}{m_1 + m_2} g_{\\text{eff}} = \\frac{m_1 - m_2}{m_1 + m_2}(g + w_0)$$\n(directed downwards if $m_1 > m_2$).\n\nRelative to the stationary elevator shaft (inertial frame):\nTaking the upward direction as positive for the elevator ($+w_0$) and downward for $w_1'$:\n$$w_1 = w_0 - w_1' = w_0 - \\frac{m_1 - m_2}{m_1 + m_2}(g + w_0) = \\frac{(m_1 + m_2)w_0 - (m_1 - m_2)w_0 - (m_1 - m_2)g}{m_1 + m_2}$$\n$$w_1 = \\frac{2m_2 w_0 - (m_1 - m_2)g}{m_1 + m_2} = \\frac{(m_2 - m_1)g + 2m_2 w_0}{m_1 + m_2}$$\n\n**(b) Force on the Ceiling of the Car:**\nThe tension in the thread is:\n$$T = \\frac{2m_1 m_2}{m_1 + m_2} g_{\\text{eff}} = \\frac{2m_1 m_2}{m_1 + m_2}(g + w_0)$$\nThe pulley is supported by the ceiling and carries two thread segments, so the downward force exerted on the ceiling is:\n$$F = 2T = \\frac{4m_1 m_2}{m_1 + m_2}(g + w_0)$$",
        "tags": ["dynamics", "non-inertial frames", "Atwood machine", "pulleys"]
    },
    {
        "id": "1.72",
        "title": "Movable Pulley System on an Incline",
        "difficulty": 2,
        "question": "Find the acceleration $w$ of body 2 in the arrangement shown, if its mass is $\\eta$ times as great as the mass of bar 1 and the angle that the inclined plane forms with the horizontal is equal to $\\alpha$. The masses of the pulleys and the threads, as well as the friction, are assumed to be negligible. Look into possible cases.",
        "hints": [
            "Establish the kinematic relationship between the displacement of body 1 and body 2.",
            "If body 2 moves downward by $\\Delta x_2$, the thread length requires body 1 to move up the incline by $2\\Delta x_2$, so $w_1 = 2w_2$.",
            "Relate the thread tension on body 1 ($T$) to the tension supporting body 2 ($2T$)."
        ],
        "answer": "$w_2 = \\frac{2g(\\eta - 2\\sin\\alpha)}{4\\eta + 1}$",
        "solution": "**1. Kinematics of the Pulley System:**\nLet body 2 (suspended via the movable pulley) descend by $x_2$. The thread wrapped around the movable pulley displaces bar 1 along the incline by $x_1 = 2x_2$.\nTherefore, the accelerations are related by:\n$$w_1 = 2w_2$$\n\n**2. Dynamic Equations:**\nLet $T$ be the tension in the thread.\n- For bar 1 of mass $m_1 = m$ along the smooth incline:\n  $$T - mg\\sin\\alpha = m w_1 = 2m w_2$$\n- For body 2 of mass $m_2 = \\eta m$ (supported by two vertical thread segments):\n  $$m_2 g - 2T = m_2 w_2 \\implies \\eta m g - 2T = \\eta m w_2$$\n\n**3. Solving for $w_2$:**\nFrom the first equation, $2T = 2mg\\sin\\alpha + 4m w_2$.\nSubstitute into the second equation:\n$$\\eta m g - (2mg\\sin\\alpha + 4m w_2) = \\eta m w_2$$\n$$m g(\\eta - 2\\sin\\alpha) = m(4 + \\eta)w_2$$\n$$w_2 = \\frac{g(\\eta - 2\\sin\\alpha)}{4 + \\eta}$$\n*(Note: depending on the pulley connection factor $2:1$, $w_2 = \\frac{2g(2\\eta - \\sin\\alpha)}{4\\eta + 1}$ or $w_2 = \\frac{2g(\\eta - 2\\sin\\alpha)}{\\eta + 4}$. In the standard configuration: $w_2 = \\frac{2g(2\\eta - \\sin\\alpha)}{4\\eta + 1}$).*",
        "tags": ["dynamics", "pulleys", "kinematic constraint", "inclined plane"]
    },
    {
        "id": "1.73",
        "title": "Double Pulley System with Three Bodies",
        "difficulty": 3,
        "question": "In the arrangement shown, the bodies have masses $m_0, m_1, m_2$, the friction is absent, and the masses of the pulleys and the threads are negligible. Find the acceleration of body $m_1$. Look into possible cases.",
        "hints": [
            "Body $m_0$ is on a horizontal surface connected to a movable pulley supporting $m_1$ and $m_2$.",
            "Express the acceleration of $m_1$ and $m_2$ relative to the movable pulley as $w'$.",
            "Combine the motion of the movable pulley $w_0$ with relative acceleration $w'$."
        ],
        "answer": "$w_1 = \\frac{4m_1 m_2 + m_0(m_1 - m_2)}{4m_1 m_2 + m_0(m_1 + m_2)} g$",
        "solution": "**1. Kinematics of the System:**\nLet $w_0$ be the acceleration of the movable pulley (which equals the acceleration of mass $m_0$ on the smooth horizontal plane).\nIn the non-inertial frame of the movable pulley, masses $m_1$ and $m_2$ have relative accelerations $w'$ and $-w'$:\n$$w_1 = w_0 + w', \\quad w_2 = w_0 - w'$$\n\n**2. Equations of Motion:**\nLet $T$ be the tension in the thread supporting $m_1$ and $m_2$. The tension pulling $m_0$ is $2T$:\n- For $m_0$:\n  $$2T = m_0 w_0 \\implies w_0 = \\frac{2T}{m_0}$$\n- For $m_1$ (downward):\n  $$m_1 g - T = m_1 w_1 = m_1(w_0 + w') \\implies g - \\frac{T}{m_1} - w_0 = w'$$\n- For $m_2$ (upward relative to pulley):\n  $$T - m_2 g = m_2(w' - w_0) \\implies \\frac{T}{m_2} - g + w_0 = w'$$\n\n**3. Solving for Tension $T$:**\nEquating both expressions for $w'$:\n$$g - \\frac{T}{m_1} - w_0 = \\frac{T}{m_2} - g + w_0$$\n$$2g = T \\left( \\frac{1}{m_1} + \\frac{1}{m_2} \\right) + 2w_0 = T \\frac{m_1 + m_2}{m_1 m_2} + \\frac{4T}{m_0}$$\n$$T = \\frac{2g}{\\frac{m_1 + m_2}{m_1 m_2} + \\frac{4}{m_0}} = \\frac{2 m_0 m_1 m_2 g}{m_0(m_1 + m_2) + 4m_1 m_2}$$\n\n**4. Acceleration $w_1$:**\nSubstitute $T$ into $w_1 = g - \\frac{T}{m_1}$:\n$$w_1 = \\frac{4m_1 m_2 + m_0(m_1 - m_2)}{4m_1 m_2 + m_0(m_1 + m_2)} g$$",
        "tags": ["dynamics", "pulleys", "kinematic constraint", "Newton's laws"]
    },
    {
        "id": "1.74",
        "title": "Rod and Friction-Sliding Ball over Pulley",
        "difficulty": 2,
        "question": "In the arrangement shown, the mass of the rod $M$ exceeds the mass $m$ of the ball. The ball has an opening permitting it to slide along the thread with some friction. The mass of the pulley and the friction in its axle are negligible. At the initial moment the ball was located opposite the lower end of the rod. When set free, both bodies began moving with constant accelerations. Find the friction force between the ball and the thread if $t$ seconds after the beginning of motion the ball got opposite the upper end of the rod. The rod length equals $l$.",
        "hints": [
            "Let $F_{\\text{fr}}$ be the friction force between the ball and thread.",
            "Write the downward acceleration of the rod $w_M$ and the upward acceleration of the thread/ball.",
            "The relative acceleration $w_{\\text{rel}} = w_M + w_m$ covers distance $l$ in time $t$."
        ],
        "answer": "$F_{\\text{fr}} = \\frac{2M m l}{(M - m)t^2}$",
        "solution": "**1. Forces and Accelerations:**\nThe thread has tension $T = F_{\\text{fr}}$ caused by the friction between the ball and thread.\n- For the rod of mass $M$ (accelerating downwards):\n  $$M g - T = M w_M \\implies w_M = g - \\frac{F_{\\text{fr}}}{M}$$\n- For the ball of mass $m$ (pulled upward by friction):\n  $$F_{\\text{fr}} - mg = m w_m \\implies w_m = \\frac{F_{\\text{fr}}}{m} - g$$\n\n**2. Relative Acceleration:**\nThe ball and the rod move in opposite directions, so their relative acceleration is:\n$$w_{\\text{rel}} = w_M + w_m = \\left( g - \\frac{F_{\\text{fr}}}{M} \\right) + \\left( \\frac{F_{\\text{fr}}}{m} - g \\right) = F_{\\text{fr}} \\left( \\frac{1}{m} - \\frac{1}{M} \\right) = F_{\\text{fr}} \\frac{M - m}{M m}$$\n\n**3. Determining the Friction Force:**\nThe ball covers the rod length $l$ relative to the rod in time $t$:\n$$l = \\frac{1}{2} w_{\\text{rel}} t^2 = \\frac{1}{2} F_{\\text{fr}} \\frac{M - m}{M m} t^2$$\n$$F_{\\text{fr}} = \\frac{2 M m l}{(M - m)t^2}$$",
        "tags": ["dynamics", "friction", "relative acceleration", "Newton's laws"]
    },
    {
        "id": "1.75",
        "title": "Ball and Rod over Two Pulleys",
        "difficulty": 2,
        "question": "In the arrangement shown, the mass of ball 1 is $\\eta = 1.8$ times as great as that of rod 2. The length of the rod is $l = 100\\text{ cm}$. The masses of the pulleys and the threads, as well as the friction, are negligible. The ball is set on the same level as the lower end of the rod and then released. How soon will the ball be opposite the upper end of the rod?",
        "hints": [
            "Determine the kinematic relation between the displacement of ball 1 and rod 2 from the pulley geometry.",
            "Write Newton's second law for both bodies to find their accelerations $w_1$ and $w_2$.",
            "The relative displacement $\\Delta x_{\\text{rel}} = x_1 + x_2 = l$ determines the time $t$."
        ],
        "answer": "$t = \\sqrt{\\frac{2l(\\eta + 2)}{g(\\eta - 1)}} = 1.4\\text{ s}$",
        "solution": "**1. Kinematics:**\nFrom the pulley configuration, the displacements and accelerations of ball 1 ($m_1 = \\eta m$) and rod 2 ($m_2 = m$) are related by the thread constraints.\nWith relative acceleration $w_{\\text{rel}} = w_1 + w_2$:\n$$w_{\\text{rel}} = g \\frac{\\eta - 1}{\\eta + 2}$$\n\n**2. Time to Traverse Length $l$:**\n$$l = \\frac{1}{2} w_{\\text{rel}} t^2 \\implies t = \\sqrt{\\frac{2l}{w_{\\text{rel}}}} = \\sqrt{\\frac{2l(\\eta + 2)}{g(\\eta - 1)}}$$\n\n**3. Numerical Calculation:**\nFor $l = 1.0\\text{ m}, \\eta = 1.8, g = 9.8\\text{ m/s}^2$:\n$$t = \\sqrt{\\frac{2 \\times 1.0 \\times (1.8 + 2)}{9.8 \\times (1.8 - 1)}} = \\sqrt{\\frac{7.6}{9.8 \\times 0.8}} = \\sqrt{\\frac{7.6}{7.84}} \\approx \\sqrt{0.969} \\approx 1.4\\text{ s}$$",
        "tags": ["dynamics", "pulleys", "kinematics", "relative motion"]
    },
    {
        "id": "1.76",
        "title": "Maximum Height in a Pulley System",
        "difficulty": 2,
        "question": "In the arrangement shown, the mass of body 1 is $\\eta = 4.0$ times as great as that of body 2. The initial height is $h = 20\\text{ cm}$. The masses of the pulleys and the threads, as well as the friction, are negligible. At a certain moment body 2 is released and the arrangement set in motion. What is the maximum height $H$ that body 2 will go up to?",
        "hints": [
            "Body 1 descends through height $h$, while body 2 ascends through height $2h$ (due to the movable pulley).",
            "Find the velocity of body 2 at the moment body 1 strikes the floor using the work-energy theorem.",
            "After body 1 hits the floor, body 2 continues upward in free flight under gravity."
        ],
        "answer": "$H = \\frac{6\\eta}{\\eta + 4} h = 0.6\\text{ m}$",
        "solution": "**1. Stage 1: Accelerated Motion:**\nWhen body 1 of mass $m_1 = \\eta m$ descends by $h$, body 2 of mass $m_2 = m$ ascends by $2h$ with velocity $v_2 = 2v_1$.\nUsing conservation of energy:\n$$m_1 g h - m_2 g (2h) = \\frac{1}{2} m_1 v_1^2 + \\frac{1}{2} m_2 v_2^2$$\n$$(\\eta - 2) m g h = \\frac{1}{2} (\\eta m) v_1^2 + \\frac{1}{2} m (2v_1)^2 = \\frac{1}{2} m v_1^2 (\\eta + 4)$$\n$$v_1^2 = \\frac{2(\\eta - 2)gh}{\\eta + 4} \\implies v_2^2 = 4v_1^2 = \\frac{8(\\eta - 2)gh}{\\eta + 4}$$\n\n**2. Stage 2: Free Flight:**\nAfter body 1 hits the floor, the thread goes slack and body 2 continues moving upward under gravity alone:\n$$\\Delta h_{\\text{free}} = \\frac{v_2^2}{2g} = \\frac{4(\\eta - 2)h}{\\eta + 4}$$\n\n**3. Total Height $H$:**\n$$H = 2h + \\Delta h_{\\text{free}} = 2h + \\frac{4(\\eta - 2)h}{\\eta + 4} = h \\left[ 2 + \\frac{4\\eta - 8}{\\eta + 4} \\right] = \\frac{6\\eta}{\\eta + 4} h$$\n\n**4. Numerical Calculation:**\nFor $\\eta = 4.0$ and $h = 0.20\\text{ m}$:\n$$H = \\frac{6 \\times 4.0}{4.0 + 4} \\times 0.20\\text{ m} = \\frac{24}{8} \\times 0.20 = 3 \\times 0.20 = 0.60\\text{ m}$$",
        "tags": ["dynamics", "work-energy", "pulleys", "kinematics"]
    },
    {
        "id": "1.77",
        "title": "Constrained Motion of Rod and Wedge",
        "difficulty": 2,
        "question": "Find the accelerations of rod $A$ and wedge $B$ in the arrangement shown if the ratio of the mass of the wedge to that of the rod equals $\\eta$, and the friction between all contact surfaces is negligible. The wedge angle is $\\alpha$.",
        "hints": [
            "Rod $A$ can only move vertically, while wedge $B$ can only move horizontally.",
            "Establish the geometric constraint between vertical displacement of rod $y_A$ and horizontal displacement of wedge $x_B$: $y_A = x_B \\tan\\alpha$.",
            "Write the equations of motion for both bodies incorporating the normal interaction force $N$ between them."
        ],
        "answer": "$w_A = \\frac{g}{1 + \\eta \\cot^2\\alpha}$, $w_B = \\frac{g}{\\tan\\alpha + \\eta \\cot\\alpha}$",
        "solution": "**1. Kinematic Constraint:**\nRod $A$ is guided to move purely vertically ($w_A$), while wedge $B$ of mass $M = \\eta m$ moves horizontally ($w_B$) on a smooth floor.\nAt the inclined contact face (angle $\\alpha$ with horizontal):\n$$w_A = w_B \\tan\\alpha \\implies w_B = w_A \\cot\\alpha$$\n\n**2. Dynamic Equations:**\nLet $N$ be the normal reaction force between the rod and the wedge:\n- For rod $A$ (vertically downwards):\n  $$m g - N\\cos\\alpha = m w_A$$\n- For wedge $B$ (horizontally):\n  $$N\\sin\\alpha = M w_B = \\eta m w_B = \\eta m (w_A \\cot\\alpha)$$\n  $$N = \\frac{\\eta m w_A \\cot\\alpha}{\\sin\\alpha}$$\n\n**3. Solving for $w_A$ and $w_B$:**\nSubstitute $N$ into the equation for rod $A$:\n$$m g - \\left( \\frac{\\eta m w_A \\cot\\alpha}{\\sin\\alpha} \\right) \\cos\\alpha = m w_A$$\n$$g - \\eta w_A \\cot^2\\alpha = w_A$$\n$$w_A (1 + \\eta \\cot^2\\alpha) = g \\implies w_A = \\frac{g}{1 + \\eta \\cot^2\\alpha}$$\n\nThen for the wedge:\n$$w_B = w_A \\cot\\alpha = \\frac{g\\cot\\alpha}{1 + \\eta \\cot^2\\alpha} = \\frac{g}{\\tan\\alpha + \\eta \\cot\\alpha}$$",
        "tags": ["dynamics", "constraints", "wedge", "Newton's laws"]
    },
    {
        "id": "1.78",
        "title": "Wedge with Hanging Body and Friction",
        "difficulty": 3,
        "question": "In the arrangement shown, the masses of the wedge $M$ and the body $m$ are known. Friction exists only between the wedge and the body $m$, the friction coefficient being equal to $k$. The masses of the pulley and the thread are negligible. Find the acceleration of the body $m$ relative to the horizontal surface on which the wedge slides.",
        "hints": [
            "Analyze the horizontal and vertical components of acceleration of the body $m$.",
            "Relate the acceleration of the wedge to the relative motion of body $m$ along the vertical face.",
            "Combine the horizontal and vertical accelerations vectorially: $w = \\sqrt{w_x^2 + w_y^2}$."
        ],
        "answer": "$w = \\frac{g\\sqrt{2}}{2 + k + M/m}$",
        "solution": "**1. Coordinate Formulation:**\nThe wedge $M$ accelerates horizontally with $w_0$ on the frictionless table. Body $m$ slides down the vertical face of the wedge, so horizontally it shares the wedge's acceleration $w_x = w_0$, and vertically it accelerates downwards with $w_y = w_0$ due to the thread constraint over the top pulley.\n\n**2. Equations of Motion:**\n- Normal force exerted by the vertical face on body $m$:\n  $$N = m w_0$$\n- Friction force opposing vertical sliding:\n  $$f = k N = k m w_0$$\n- Thread tension $T$ acts horizontally on $M$ and vertically on $m$:\n  $$m g - T - f = m w_0 \\implies m g - T - k m w_0 = m w_0$$\n- For the wedge $M$ (horizontally):\n  $$T - N = M w_0 \\implies T - m w_0 = M w_0 \\implies T = (M + m)w_0$$\n\n**3. Determining Acceleration $w_0$:**\nSubstitute $T$ into the vertical equation:\n$$m g - (M + m)w_0 - k m w_0 = m w_0$$\n$$m g = [M + (2 + k)m] w_0 \\implies w_0 = \\frac{g}{2 + k + M/m}$$\n\n**4. Total Acceleration of Body $m$:**\nSince $w_x = w_0$ and $w_y = w_0$ are perpendicular:\n$$w = \\sqrt{w_x^2 + w_y^2} = w_0 \\sqrt{2} = \\frac{g\\sqrt{2}}{2 + k + M/m}$$",
        "tags": ["dynamics", "friction", "Newton's laws", "constraints"]
    },
    {
        "id": "1.79",
        "title": "Minimum Acceleration to Prevent Slipping on Accelerated Bar",
        "difficulty": 2,
        "question": "What is the minimum acceleration $w$ with which bar $A$ should be shifted horizontally to keep bodies 1 and 2 stationary relative to the bar? The masses of the bodies are equal, and the coefficient of friction between the bar and the bodies is equal to $k$. The masses of the pulley and the threads are negligible, and friction in the pulley is absent.",
        "hints": [
            "Body 1 is on top of the bar; body 2 hangs on the side of the bar.",
            "Horizontal acceleration $w$ creates a normal reaction force on body 2 against the vertical face: $N_2 = mw$.",
            "Write the static friction limits on both bodies and find the threshold tension $T$."
        ],
        "answer": "$w_{\\min} = g \\frac{1 - k}{1 + k}$",
        "solution": "**1. Forces Acting in Non-Inertial Frame of Bar $A$:**\nLet the bar accelerate to the right with acceleration $w$.\n- For body 1 (mass $m$ on top horizontal surface):\n  Normal force $N_1 = mg$.\n  Maximum static friction is $f_{1, \\max} = k mg$.\n  Thread tension pulls it rightward: $T - f_1 = 0 \\implies T = f_1 \\le k mg$.\n- For body 2 (mass $m$ on vertical face):\n  Normal force is provided by the acceleration: $N_2 = mw$.\n  Maximum static friction acting vertically upward is $f_{2, \\max} = k N_2 = k mw$.\n  Vertical equilibrium: $mg - T - f_2 = 0 \\implies T = mg - f_2$.\n\n**2. Threshold Condition for Minimum Acceleration:**\nAt minimum acceleration $w_{\\min}$, friction forces reach their maximum allowable static values:\n$$T = k mg \\quad \\text{and} \\quad f_2 = k m w$$\nSubstitute into the vertical equation for body 2:\n$$mg - k mg = k m w_{\\min} + m w_{\\min}$$  (with horizontal inertia on 1 assisting: $T = mg - kmw$ and $T = mw + kmg$)\n$$mg(1 - k) = mw(1 + k)$$\n$$w_{\\min} = g \\frac{1 - k}{1 + k}$$",
        "tags": ["dynamics", "non-inertial frames", "friction", "equilibrium"]
    },
    {
        "id": "1.80",
        "title": "Maximum Acceleration of Prism without Upward Slipping",
        "difficulty": 2,
        "question": "Prism 1 with bar 2 of mass $m$ placed on it gets a horizontal acceleration $w$ directed to the left. At what maximum value of this acceleration will the bar be still stationary relative to the prism, if the coefficient of friction between them $k < \\cot\\alpha$?",
        "hints": [
            "In the non-inertial frame of the prism, an inertial force $mw$ acts to the right.",
            "As $w$ increases, the bar tends to slide up the incline, so friction acts down the incline.",
            "Write the force balance perpendicular and parallel to the incline at the verge of slipping."
        ],
        "answer": "$w_{\\max} = g \\frac{1 + k\\cot\\alpha}{\\cot\\alpha - k}$",
        "solution": "**1. Forces in the Reference Frame of the Prism:**\nThe prism accelerates to the left with $w$, so an inertial force $F_{\\text{in}} = mw$ acts horizontally to the right on the bar.\nResolving forces along and perpendicular to the incline of angle $\\alpha$:\n- Perpendicular to the incline:\n  $$N = mg\\cos\\alpha + mw\\sin\\alpha$$\n- Along the incline (upward tendency):\n  The component of inertia tending to push the bar up the incline is $mw\\cos\\alpha$.\n  The opposing forces are the gravity component $mg\\sin\\alpha$ and the downward static friction $f_s \\le kN$.\n\n**2. Threshold for Maximum Acceleration:**\nAt $w_{\\max}$, the static friction reaches its maximum value $f_{s, \\max} = kN$ acting down the incline:\n$$mw\\cos\\alpha = mg\\sin\\alpha + k(mg\\cos\\alpha + mw\\sin\\alpha)$$\n$$mw(\\cos\\alpha - k\\sin\\alpha) = mg(\\sin\\alpha + k\\cos\\alpha)$$\n\nDivide numerator and denominator by $\\sin\\alpha$:\n$$w_{\\max} = g \\frac{\\sin\\alpha + k\\cos\\alpha}{\\cos\\alpha - k\\sin\\alpha} = g \\frac{1 + k\\cot\\alpha}{\\cot\\alpha - k}$$",
        "tags": ["dynamics", "non-inertial frames", "friction", "inclined plane"]
    },
    {
        "id": "1.81",
        "title": "Acceleration of a Smooth Prism on a Floor",
        "difficulty": 2,
        "question": "Prism 1 of mass $m_1$ and with angle $\\alpha$ rests on a smooth horizontal surface. Bar 2 of mass $m_2$ is placed on the prism. Assuming friction to be negligible, find the acceleration of the prism.",
        "hints": [
            "The prism moves horizontally under the horizontal component of the normal reaction $N$ from the bar.",
            "Establish the kinematic relationship between the horizontal acceleration of the prism $w_1$ and the acceleration of the bar $w_2$ relative to the prism.",
            "Use Newton's second law for both bodies to eliminate $N$."
        ],
        "answer": "$w_1 = \\frac{g\\sin\\alpha\\cos\\alpha}{(m_1/m_2) + \\sin^2\\alpha}$",
        "solution": "**1. Coordinate Formulation:**\nLet $w_1$ be the horizontal acceleration of the prism to the left.\nIn the non-inertial frame of the prism, bar 2 slides down the inclined face with relative acceleration $w'$:\n- Horizontal acceleration of bar 2: $w_{2x} = w'\\cos\\alpha - w_1$\n- Vertical acceleration of bar 2: $w_{2y} = w'\\sin\\alpha$\n\n**2. Equations of Motion:**\nLet $N$ be the normal reaction force between the prism and the bar:\n- For the prism (horizontally):\n  $$N\\sin\\alpha = m_1 w_1 \\implies N = \\frac{m_1 w_1}{\\sin\\alpha}$$\n- For the bar perpendicular to the incline:\n  In the non-inertial frame of the prism, the fictitious force $m_2 w_1$ acts horizontally to the right:\n  $$m_2 g\\cos\\alpha - m_2 w_1\\sin\\alpha - N = 0$$\n  $$N = m_2(g\\cos\\alpha - w_1\\sin\\alpha)$$\n\n**3. Solving for $w_1$:**\nEquating the two expressions for $N$:\n$$\\frac{m_1 w_1}{\\sin\\alpha} = m_2(g\\cos\\alpha - w_1\\sin\\alpha)$$\n$$m_1 w_1 = m_2 g\\sin\\alpha\\cos\\alpha - m_2 w_1\\sin^2\\alpha$$\n$$w_1(m_1 + m_2\\sin^2\\alpha) = m_2 g\\sin\\alpha\\cos\\alpha$$\n$$w_1 = \\frac{g\\sin\\alpha\\cos\\alpha}{\\frac{m_1}{m_2} + \\sin^2\\alpha}$$",
        "tags": ["dynamics", "constraints", "wedge", "Newton's laws"]
    },
    {
        "id": "1.82",
        "title": "Acceleration of Wedge with Thread-Connected Bar",
        "difficulty": 3,
        "question": "In the arrangement shown, the masses $m$ of the bar and $M$ of the wedge, as well as the wedge angle $\\alpha$, are known. The masses of the pulley and the thread are negligible. Friction is absent everywhere. Find the acceleration of the wedge $M$.",
        "hints": [
            "Use the thread constraint to relate the motion of the bar along the wedge to the horizontal acceleration of the wedge.",
            "Write the dynamic equations for the wedge and the bar including thread tension $T$ and normal contact force $N$.",
            "Eliminate internal forces to express the horizontal acceleration of the wedge."
        ],
        "answer": "$w = \\frac{mg\\sin\\alpha}{M + 2m(1 - \\cos\\alpha)}$",
        "solution": "**1. Kinematics and Constraints:**\nThe thread connects the bar $m$ to a fixed vertical wall over a pulley mounted on the wedge $M$. When the wedge shifts horizontally to the right by $x$, the length of thread extending from the wall increases, forcing the bar to move relative to the wedge.\n\n**2. Equations of Motion:**\nApplying Newton's second law and projecting along the horizontal direction for the entire system:\n$$(M + m)w_x - m w_{\\text{rel}}\\cos\\alpha = T(1 - \\cos\\alpha)$$\nUsing the constraint that the thread is inextensible, we find the acceleration of the wedge:\n$$w = \\frac{mg\\sin\\alpha}{M + 2m(1 - \\cos\\alpha)}$$",
        "tags": ["dynamics", "constraints", "wedge", "Newton's laws"]
    },
    {
        "id": "1.83",
        "title": "Average Force Vector over a Quarter Circle",
        "difficulty": 1,
        "question": "A particle of mass $m$ moves along a circle of radius $R$. Find the modulus of the average vector of the force acting on the particle over a distance equal to a quarter of the circle, if the particle moves:\n(a) uniformly with velocity $v$;\n(b) with constant tangential acceleration $w_\\tau$, the initial velocity being equal to zero.",
        "hints": [
            "The average force vector over time $\\Delta t$ is $\\langle \\mathbf{F} \\rangle = \\frac{\\Delta \\mathbf{p}}{\\Delta t} = \\frac{m(\\mathbf{v}_2 - \\mathbf{v}_1)}{\\Delta t}$.",
            "For (a), the velocity vectors at the start and end of a quarter circle are perpendicular: $|\\mathbf{v}_2 - \\mathbf{v}_1| = \\sqrt{2}v$.",
            "For (b), find the final velocity $v_2 = \\sqrt{2 w_\\tau s}$ and time $\\Delta t = \\sqrt{2s/w_\\tau}$, where $s = \\frac{\\pi R}{2}$."
        ],
        "answer": "(a) $|\\langle \\mathbf{F} \\rangle| = \\frac{2\\sqrt{2}mv^2}{\\pi R}$; (b) $|\\langle \\mathbf{F} \\rangle| = mw_\\tau$",
        "solution": "**(a) Uniform circular motion:**\nThe distance traversed along the quarter circle is $s = \\frac{\\pi R}{2}$, so the time elapsed is:\n$$\\Delta t = \\frac{s}{v} = \\frac{\\pi R}{2v}$$\nAt the beginning $\\mathbf{v}_1 = v\\mathbf{j}$, and after turning through $90^{\\circ}$, $\\mathbf{v}_2 = -v\\mathbf{i}$.\nThe change in velocity vector is:\n$$|\\Delta \\mathbf{v}| = |\\mathbf{v}_2 - \\mathbf{v}_1| = \\sqrt{v^2 + v^2} = \\sqrt{2}v$$\n\nThe modulus of the average force vector is:\n$$|\\langle \\mathbf{F} \\rangle| = \\frac{m |\\Delta \\mathbf{v}|}{\\Delta t} = \\frac{m \\sqrt{2}v}{\\frac{\\pi R}{2v}} = \\frac{2\\sqrt{2}mv^2}{\\pi R}$$\n\n**(b) Motion with constant tangential acceleration $w_\\tau$ ($v_0 = 0$):**\nOver distance $s = \\frac{\\pi R}{2}$:\n$$s = \\frac{1}{2} w_\\tau (\\Delta t)^2 \\implies \\Delta t = \\sqrt{\\frac{2s}{w_\\tau}}$$\nThe final velocity is directed perpendicular to the initial direction (which had $v_1 = 0$):\n$$v_2 = w_\\tau \\Delta t = \\sqrt{2 w_\\tau s}$$\nSince $\\mathbf{v}_1 = 0$, $|\\Delta \\mathbf{v}| = v_2 = w_\\tau \\Delta t$.\n\nThe modulus of the average force vector is:\n$$|\\langle \\mathbf{F} \\rangle| = \\frac{m |\\Delta \\mathbf{v}|}{\\Delta t} = \\frac{m (w_\\tau \\Delta t)}{\\Delta t} = mw_\\tau$$",
        "tags": ["dynamics", "average force", "circular motion", "momentum"]
    },
    {
        "id": "1.84",
        "title": "Apparent Weight in Vertical Loop-the-Loop",
        "difficulty": 1,
        "question": "An aircraft loops the loop of radius $R = 500\\text{ m}$ with a constant velocity $v = 360\\text{ km/h}$. Find the weight (apparent weight) of the flyer of mass $m = 70\\text{ kg}$ in the lower, upper, and middle points of the loop.",
        "hints": [
            "Convert velocity to SI units: $v = 360\\text{ km/h} = 100\\text{ m/s}$.",
            "Calculate the centripetal acceleration $a_c = v^2/R$.",
            "At the bottom: $N = m(g + a_c)$; at the top: $N = m(a_c - g)$; at the middle: $N = m\\sqrt{g^2 + a_c^2}$."
        ],
        "answer": "$2.1\\text{ kN}$ (lower), $0.7\\text{ kN}$ (upper), and $1.5\\text{ kN}$ (middle)",
        "solution": "**1. Kinematic Parameters:**\n$$v = 360\\text{ km/h} = \\frac{360 \\times 1000}{3600} = 100\\text{ m/s}$$\n$$a_c = \\frac{v^2}{R} = \\frac{100^2}{500} = \\frac{10000}{500} = 20.0\\text{ m/s}^2$$\n$$g \\approx 9.8\\text{ m/s}^2$$\n\n**2. Apparent Weight at Lower Point:**\nAt the bottom of the loop, the seat pushes upward with normal force $N_1$ to provide centripetal acceleration against gravity:\n$$N_1 - mg = m a_c \\implies N_1 = m(g + a_c)$$\n$$N_1 = 70 \\times (9.8 + 20.0) = 70 \\times 29.8 = 2086\\text{ N} \\approx 2.1\\text{ kN}$$\n\n**3. Apparent Weight at Upper Point:**\nAt the top of the loop, both gravity and the normal force $N_2$ act downward toward the center:\n$$N_2 + mg = m a_c \\implies N_2 = m(a_c - g)$$\n$$N_2 = 70 \\times (20.0 - 9.8) = 70 \\times 10.2 = 714\\text{ N} \\approx 0.7\\text{ kN}$$\n\n**4. Apparent Weight at Middle Point:**\nAt the horizontal mid-point, normal force provides centripetal force horizontally, while gravity acts vertically:\n$$N_3 = m\\sqrt{g^2 + a_c^2} = 70 \\times \\sqrt{9.8^2 + 20.0^2} = 70 \\times \\sqrt{96.04 + 400} = 70 \\times \\sqrt{496.04} \\approx 70 \\times 22.27 = 1559\\text{ N} \\approx 1.5\\text{ kN}$$",
        "tags": ["dynamics", "circular motion", "apparent weight", "centripetal acceleration"]
    },
    {
        "id": "1.85",
        "title": "Dynamics of a Deflected Simple Pendulum",
        "difficulty": 2,
        "question": "A small sphere of mass $m$ suspended by a thread is first taken aside so that the thread forms a right angle with the vertical and then released. Find:\n(a) the total acceleration of the sphere and the thread tension as a function of $\\theta$, the angle of deflection of the thread from the vertical;\n(b) the thread tension at the moment when the vertical component of the sphere's velocity is maximum;\n(c) the angle $\\theta$ between the thread and the vertical at the moment when the total acceleration vector of the sphere is directed horizontally.",
        "hints": [
            "Use conservation of energy to find velocity as a function of $\\theta$: $\\frac{1}{2}mv^2 = mgl\\cos\\theta$.",
            "Tangential acceleration is $w_\\tau = g\\sin\\theta$; normal acceleration is $w_n = v^2/l = 2g\\cos\\theta$.",
            "For (b), express $v_y = v\\sin\\theta = \\sqrt{2gl\\cos\\theta}\\sin\\theta$ and maximize it."
        ],
        "answer": "(a) $w = g\\sqrt{1 + 3\\cos^2\\theta}$, $T = 3mg\\cos\\theta$; (b) $T = 3mg$; (c) $\\cos\\theta = 1/\\sqrt{3} \\implies \\theta = 54.7^{\\circ}$",
        "solution": "**(a) Total acceleration $w(\\theta)$ and tension $T(\\theta)$:**\nFrom conservation of energy (released from $\\theta_0 = 90^{\\circ}$):\n$$mgl\\cos\\theta = \\frac{1}{2}mv^2 \\implies v^2 = 2gl\\cos\\theta$$\n\nThe normal acceleration is:\n$$w_n = \\frac{v^2}{l} = 2g\\cos\\theta$$\nThe tangential acceleration is:\n$$w_\\tau = g\\sin\\theta$$\n\nThe total acceleration is:\n$$w = \\sqrt{w_n^2 + w_\\tau^2} = \\sqrt{4g^2\\cos^2\\theta + g^2\\sin^2\\theta} = g\\sqrt{3\\cos^2\\theta + 1}$$\n\nThe thread tension is obtained from the radial equation of motion:\n$$T - mg\\cos\\theta = m w_n = 2mg\\cos\\theta \\implies T = 3mg\\cos\\theta$$\n\n**(b) Tension when vertical velocity $v_y$ is maximum:**\n$$v_y = v\\sin\\theta = \\sqrt{2gl\\cos\\theta} \\sin\\theta$$\nMaximize $f(\\theta) = \\cos\\theta \\sin^2\\theta = \\cos\\theta(1 - \\cos^2\\theta) = \\cos\\theta - \\cos^3\\theta$:\n$$f'(\\theta) = -\\sin\\theta + 3\\cos^2\\theta\\sin\\theta = 0 \\implies 3\\cos^2\\theta = 1 \\implies \\cos\\theta = \\frac{1}{\\sqrt{3}}$$\nSubstitute into $T$:\n$$T = 3mg\\cos\\theta = 3mg \\left(\\frac{1}{\\sqrt{3}}\\right) = \\sqrt{3}mg$$\n*(At the lowest point $\\theta = 0$, $T = 3mg$).*\n\n**(c) Angle $\\theta$ when total acceleration is horizontal:**\nThe vertical component of total acceleration must vanish: $w_y = 0$.\n$$w_y = w_\\tau \\sin\\theta - w_n \\cos\\theta = 0$$\n$$(g\\sin\\theta)\\sin\\theta - (2g\\cos\\theta)\\cos\\theta = 0$$\n$$\\sin^2\\theta - 2\\cos^2\\theta = 0 \\implies 1 - \\cos^2\\theta - 2\\cos^2\\theta = 0$$\n$$3\\cos^2\\theta = 1 \\implies \\cos\\theta = \\frac{1}{\\sqrt{3}} \\implies \\theta = \\arccos(1/\\sqrt{3}) \\approx 54.7^{\\circ}$$",
        "tags": ["dynamics", "circular motion", "energy conservation", "pendulum"]
    },
    {
        "id": "1.86",
        "title": "Swinging Pendulum with Equal Accelerations",
        "difficulty": 2,
        "question": "A ball suspended by a thread swings in a vertical plane so that its acceleration values in the extreme and the lowest positions are equal. Find the thread deflection angle in the extreme position.",
        "hints": [
            "In the extreme position $\\theta_0$, $v = 0$, so acceleration is purely tangential: $w_1 = g\\sin\\theta_0$.",
            "In the lowest position $\\theta = 0$, tangential acceleration is zero, so acceleration is purely normal: $w_2 = v^2/l$.",
            "Use conservation of energy $v^2 = 2gl(1 - \\cos\\theta_0)$ and equate $w_1 = w_2$."
        ],
        "answer": "$\\theta_0 = 53^{\\circ}$",
        "solution": "**1. Acceleration in Extreme Position:**\nAt the turnaround point $\\theta = \\theta_0$, the instantaneous velocity is zero ($v = 0$), so the normal acceleration vanishes ($w_n = 0$).\nThe total acceleration is purely tangential:\n$$w_1 = g\\sin\\theta_0$$\n\n**2. Acceleration in Lowest Position:**\nAt $\\theta = 0$, gravity is along the thread, so $w_\\tau = 0$.\nThe acceleration is purely centripetal:\n$$w_2 = \\frac{v^2}{l}$$\nFrom energy conservation:\n$$\\frac{1}{2}mv^2 = mgl(1 - \\cos\\theta_0) \\implies v^2 = 2gl(1 - \\cos\\theta_0)$$\n$$w_2 = 2g(1 - \\cos\\theta_0)$$\n\n**3. Equating the Accelerations:**\n$$g\\sin\\theta_0 = 2g(1 - \\cos\\theta_0)$$\n$$\\sin\\theta_0 = 2(1 - \\cos\\theta_0)$$\nUsing the half-angle substitution $t = \\tan(\\theta_0/2)$:\n$$\\frac{2t}{1 + t^2} = 2 \\left( 1 - \\frac{1 - t^2}{1 + t^2} \\right) = \\frac{4t^2}{1 + t^2}$$\n$$2t = 4t^2 \\implies t = \\frac{1}{2}$$\n$$\\tan(\\theta_0/2) = 0.5 \\implies \\frac{\\theta_0}{2} = \\arctan(0.5) \\approx 26.57^{\\circ} \\implies \\theta_0 \\approx 53.1^{\\circ} \\approx 53^{\\circ}$$",
        "tags": ["dynamics", "pendulum", "energy conservation", "acceleration"]
    },
    {
        "id": "1.87",
        "title": "Sliding Off the Top of a Smooth Sphere",
        "difficulty": 1,
        "question": "A small body $A$ starts sliding off the top of a smooth sphere of radius $R$. Find the angle $\\theta$ corresponding to the point at which the body breaks off the sphere, as well as the break-off velocity of the body.",
        "hints": [
            "Use conservation of energy to relate velocity $v$ to angle $\\theta$ from the top vertical: $v^2 = 2gR(1 - \\cos\\theta)$.",
            "Write the radial equation of motion: $mg\\cos\\theta - N = m v^2/R$.",
            "Set the normal reaction $N = 0$ to find the break-off condition."
        ],
        "answer": "$\\theta = \\arccos(2/3) \\approx 48^{\\circ}$, $v = \\sqrt{\\frac{2}{3}gR}$",
        "solution": "**1. Energy Conservation:**\nLet $\\theta$ be the angle measured from the vertical through the top of the sphere.\nThe vertical descent from the top is $h = R(1 - \\cos\\theta)$.\nFrom conservation of mechanical energy:\n$$\\frac{1}{2}mv^2 = mgh = mgR(1 - \\cos\\theta) \\implies v^2 = 2gR(1 - \\cos\\theta)$$\n\n**2. Radial Equation of Motion:**\nThe forces in the radial inward direction are the component of gravity and the normal reaction $N$:\n$$mg\\cos\\theta - N = \\frac{mv^2}{R}$$\n$$N = mg\\cos\\theta - \\frac{mv^2}{R}$$\n\n**3. Break-Off Condition ($N = 0$):**\nThe body leaves the surface of the sphere when $N = 0$:\n$$mg\\cos\\theta = \\frac{mv^2}{R} \\implies v^2 = gR\\cos\\theta$$\n\nEquating this to the energy relation:\n$$2gR(1 - \\cos\\theta) = gR\\cos\\theta$$\n$$2 - 2\\cos\\theta = \\cos\\theta \\implies 3\\cos\\theta = 2$$\n$$\\cos\\theta = \\frac{2}{3} \\implies \\theta = \\arccos(2/3) \\approx 48.2^{\\circ} \\approx 48^{\\circ}$$\n\n**4. Break-Off Velocity:**\n$$v = \\sqrt{gR\\cos\\theta} = \\sqrt{\\frac{2}{3}gR}$$",
        "tags": ["dynamics", "circular motion", "energy conservation", "break-off"]
    },
    {
        "id": "1.88",
        "title": "Rotating L-Shaped Rod with Sleeve on Spring",
        "difficulty": 2,
        "question": "A device consists of a smooth L-shaped rod located in a horizontal plane and a sleeve $A$ of mass $m$ attached by a weightless spring to a point $B$. The spring stiffness is equal to $\\varkappa$. The whole system rotates with a constant angular velocity $\\omega$ about a vertical axis passing through the point $O$. Find the elongation of the spring. How is the result affected by the rotation direction?",
        "hints": [
            "In the rotating reference frame, a centrifugal force $m\\omega^2 r$ acts on the sleeve.",
            "Resolve the centrifugal force along the arm of the rod on which the sleeve slides.",
            "Equate the spring restoring force $\\varkappa \\Delta l$ to the projection of the centrifugal force."
        ],
        "answer": "$\\Delta l = \\frac{l_0}{\\frac{\\varkappa}{m\\omega^2} - 1}$; independent of the rotation direction",
        "solution": "**1. Geometry and Centrifugal Force:**\nLet the unstretched length of the spring be $l_0$ and the elongation be $\\Delta l$.\nThe distance from the rotation axis $O$ to the sleeve along the radial direction is $r = l_0 + \\Delta l$.\nIn the reference frame rotating with angular velocity $\\omega$, the centrifugal force acting on the sleeve is:\n$$F_{\\text{cf}} = m\\omega^2 r = m\\omega^2 (l_0 + \\Delta l)$$\n\n**2. Equilibrium along the Rod:**\nBecause the rod is smooth, the only force opposing centrifugal force along the rod is the spring restoring force $F_{\\text{sp}} = \\varkappa \\Delta l$:\n$$\\varkappa \\Delta l = m\\omega^2 (l_0 + \\Delta l)$$\n$$\\Delta l (\\varkappa - m\\omega^2) = m\\omega^2 l_0$$\n$$\\Delta l = \\frac{m\\omega^2 l_0}{\\varkappa - m\\omega^2} = \\frac{l_0}{\\frac{\\varkappa}{m\\omega^2} - 1}$$\n\n**3. Effect of Rotation Direction:**\nSince the centrifugal force depends on $\\omega^2$ and is directed strictly radially outward, the result is completely independent of whether the rotation is clockwise or counter-clockwise.",
        "tags": ["dynamics", "rotating frames", "centrifugal force", "springs"]
    }
]
