"""
ch1_2_batch2.py
Problems 1.89 through 1.117 of Irodov Chapter 1.2: The Fundamental Equation of Dynamics.
"""

CH1_2_BATCH_2 = [
    {
        "id": "1.89",
        "title": "Cyclist on a Surface with Position-Dependent Friction",
        "difficulty": 2,
        "question": "A cyclist rides along the circumference of a circular horizontal plane of radius $R$, the friction coefficient being dependent only on distance $r$ from the centre $O$ of the plane as $k = k_0 (1 - r/R)$, where $k_0$ is a constant. Find the radius of the circle with centre at $O$ along which the cyclist can ride with the maximum velocity. What is this maximum velocity?",
        "hints": [
            "For circular motion without skidding, centripetal acceleration must satisfy $\\frac{v^2}{r} \\le kg$.",
            "Express $v^2(r) \\le k_0 g r (1 - r/R)$.",
            "Find the radius $r$ that maximizes the function $f(r) = r(1 - r/R)$ by differentiating with respect to $r$."
        ],
        "answer": "$r = \\frac{R}{2}$, $v_{\\max} = \\frac{1}{2}\\sqrt{k_0 g R}$",
        "solution": "**1. Condition for No Skidding:**\nThe maximum lateral friction force that the ground can provide is $f_{\\text{max}} = kmg = k_0 mg (1 - r/R)$.\nFor circular motion of radius $r$ at velocity $v$, the required centripetal force is $\\frac{mv^2}{r}$.\nTo avoid slipping:\n$$\\frac{mv^2}{r} \\le k_0 mg \\left(1 - \\frac{r}{R}\\right) \\implies v^2 \\le k_0 g \\left( r - \\frac{r^2}{R} \\right)$$\n\n**2. Maximizing the Velocity:**\nTo maximize $v$, we maximize $f(r) = r - \\frac{r^2}{R}$:\n$$f'(r) = 1 - \\frac{2r}{R} = 0 \\implies r = \\frac{R}{2}$$\nSince $f''(r) = -2/R < 0$, this is indeed a global maximum.\n\n**3. Maximum Velocity Value:**\nSubstitute $r = R/2$ into the velocity equation:\n$$v_{\\max}^2 = k_0 g \\left( \\frac{R}{2} - \\frac{R^2}{4R} \\right) = k_0 g \\left( \\frac{R}{4} \\right)$$\n$$v_{\\max} = \\frac{1}{2}\\sqrt{k_0 g R}$$",
        "tags": ["dynamics", "circular motion", "friction", "optimization"]
    },
    {
        "id": "1.90",
        "title": "Distance Covered before Skidding on a Circle",
        "difficulty": 2,
        "question": "A car moves with a constant tangential acceleration $w_\\tau = 0.62\\text{ m/s}^2$ along a horizontal surface circumscribing a circle of radius $R = 40\\text{ m}$. The coefficient of sliding friction between the wheels and the surface is $k = 0.20$. What distance $s$ will the car ride without sliding if at the initial moment of time its velocity is equal to zero?",
        "hints": [
            "Express the velocity in terms of tangential acceleration and distance: $v^2 = 2 w_\\tau s$.",
            "Calculate normal acceleration $w_n = v^2/R = 2w_\\tau s/R$.",
            "The total acceleration is $w = \\sqrt{w_\\tau^2 + w_n^2}$. Sliding begins when $w = kg$."
        ],
        "answer": "$s = \\frac{R}{2} \\sqrt{\\left(\\frac{kg}{w_\\tau}\\right)^2 - 1} = 60\\text{ m}$",
        "solution": "**1. Kinematics of Accelerated Circular Motion:**\nStarting from rest with constant tangential acceleration $w_\\tau$:\n$$v^2 = 2 w_\\tau s$$\nThe normal (centripetal) acceleration is:\n$$w_n = \\frac{v^2}{R} = \\frac{2 w_\\tau s}{R}$$\n\n**2. Total Acceleration and Friction Limit:**\nThe total acceleration vector has perpendicular components $w_\\tau$ and $w_n$:\n$$w = \\sqrt{w_\\tau^2 + w_n^2} = \\sqrt{w_\\tau^2 + \\left(\\frac{2 w_\\tau s}{R}\\right)^2}$$\n\nThe car will ride without sliding as long as the required horizontal force $mw \\le kmg$, i.e., $w \\le kg$.\nAt the threshold of sliding ($w = kg$):\n$$w_\\tau^2 + \\left(\\frac{2 w_\\tau s}{R}\\right)^2 = (kg)^2$$\n$$\\left(\\frac{2 w_\\tau s}{R}\\right)^2 = (kg)^2 - w_\\tau^2 = w_\\tau^2 \\left[ \\left(\\frac{kg}{w_\\tau}\\right)^2 - 1 \\right]$$\n$$s = \\frac{R}{2} \\sqrt{\\left(\\frac{kg}{w_\\tau}\\right)^2 - 1}$$\n\n**3. Numerical Calculation:**\nWith $R = 40\\text{ m}, k = 0.20, g = 9.8\\text{ m/s}^2, w_\\tau = 0.62\\text{ m/s}^2$:\n$$\\frac{kg}{w_\\tau} = \\frac{0.20 \\times 9.8}{0.62} = \\frac{1.96}{0.62} \\approx 3.161$$\n$$\\left(\\frac{kg}{w_\\tau}\\right)^2 - 1 = 3.161^2 - 1 \\approx 9.994 - 1 = 8.994$$\n$$\\sqrt{8.994} \\approx 3.00$$\n$$s = \\frac{40}{2} \\times 3.00 = 60\\text{ m}$$",
        "tags": ["dynamics", "circular motion", "friction", "kinematics"]
    },
    {
        "id": "1.91",
        "title": "Maximum Velocity on a Sinusoidal Track",
        "difficulty": 2,
        "question": "A car moves uniformly along a horizontal sine curve $y = a\\sin(x/\\alpha)$, where $a$ and $\\alpha$ are constants. The coefficient of friction between the wheels and the road is equal to $k$. At what velocity $v$ will the car ride without sliding?",
        "hints": [
            "Sliding occurs at the point of maximum curvature (minimum radius of curvature $R_{\\min}$).",
            "Use the radius of curvature formula $R = \\frac{(1 + y'^2)^{3/2}}{|y''|}$.",
            "At the peaks of the sine curve, $y' = 0$ and $|y''| = a/\\alpha^2$, giving $R_{\\min} = \\alpha^2/a$."
        ],
        "answer": "$v \\le \\alpha \\sqrt{\\frac{kg}{a}}$",
        "solution": "**1. Radius of Curvature of the Sine Curve:**\nThe path is $y = a\\sin(x/\\alpha)$.\nFirst and second derivatives:\n$$y' = \\frac{a}{\\alpha} \\cos(x/\\alpha)$$\n$$y'' = -\\frac{a}{\\alpha^2} \\sin(x/\\alpha)$$\n\nThe radius of curvature is given by:\n$$R = \\frac{[1 + y'^2]^{3/2}}{|y''|} = \\frac{\\left[1 + \\frac{a^2}{\\alpha^2}\\cos^2(x/\\alpha)\\right]^{3/2}}{\\frac{a}{\\alpha^2} |\\sin(x/\\alpha)|}$$\n\n**2. Minimum Radius of Curvature:**\n$R$ is minimized where the denominator $|y''|$ is maximal and the numerator is minimal, which occurs at the crests and troughs where $\\cos(x/\\alpha) = 0$ and $|\\sin(x/\\alpha)| = 1$:\n$$R_{\\min} = \\frac{[1 + 0]^{3/2}}{\\frac{a}{\\alpha^2}} = \\frac{\\alpha^2}{a}$$\n\n**3. Maximum Velocity Condition:**\nTo prevent sliding, the centripetal acceleration at this sharpest turn cannot exceed the maximum available friction acceleration:\n$$\\frac{v^2}{R_{\\min}} \\le kg \\implies v^2 \\le kg R_{\\min} = \\frac{kg \\alpha^2}{a}$$\n$$v \\le \\alpha \\sqrt{\\frac{kg}{a}}$$",
        "tags": ["dynamics", "curvature", "friction", "centripetal acceleration"]
    },
    {
        "id": "1.92",
        "title": "Tension in a Rotating Circular Chain on a Cone",
        "difficulty": 2,
        "question": "A chain of mass $m$ forming a circle of radius $R$ is slipped onto a smooth round cone with half-angle $\\theta$. Find the tension $T$ of the chain if it rotates with a constant angular velocity $\\omega$ about a vertical axis coinciding with the symmetry axis of the cone.",
        "hints": [
            "Consider a small element of the chain of angular length $d\\varphi$ and mass $dm = \\frac{m}{2\\pi}d\\varphi$.",
            "Identify the forces acting on this element: gravity $dm\\,g$, normal reaction $dN$, centrifugal force $dm\\,\\omega^2 R$, and inward tension components $2T\\sin(d\\varphi/2) \\approx T d\\varphi$.",
            "Use vertical equilibrium to find $dN$, then balance horizontal forces."
        ],
        "answer": "$T = \\frac{mg}{2\\pi} \\left(\\cot\\theta + \\frac{\\omega^2 R}{g}\\right)$",
        "solution": "**1. Forces on a Small Chain Element:**\nConsider an element of the chain subtending angle $d\\varphi$ at the center:\n$$dm = \\frac{m}{2\\pi} d\\varphi$$\n\nForces acting on the element:\n- Gravity: $dF_g = dm \\, g$ (vertically downward)\n- Centrifugal force in the rotating frame: $dF_{\\text{cf}} = dm \\, \\omega^2 R$ (horizontally outward)\n- Normal force $dN$ from the smooth cone surface, inclined at angle $\\theta$ to the vertical (directed upward and inward):\n  - Vertical component: $dN_z = dN \\sin\\theta$\n  - Horizontal outward component: $dN_r = dN \\cos\\theta$\n- Tension $T$ from adjacent segments: resultant radial inward force is $2T \\sin(d\\varphi/2) \\approx T d\\varphi$.\n\n**2. Equilibrium Conditions:**\n- Vertical equilibrium:\n  $$dN \\sin\\theta = dm \\, g \\implies dN = \\frac{dm \\, g}{\\sin\\theta}$$\n- Horizontal equilibrium:\n  The inward pull of tension balances the outward centrifugal force plus the outward component of normal force:\n  $$T d\\varphi = dF_{\\text{cf}} + dN \\cos\\theta = dm \\, \\omega^2 R + \\left( \\frac{dm \\, g}{\\sin\\theta} \\right) \\cos\\theta$$\n  $$T d\\varphi = dm [\\omega^2 R + g\\cot\\theta] = \\left( \\frac{m}{2\\pi} d\\varphi \\right) [\\omega^2 R + g\\cot\\theta]$$\n\n**3. Final Expression for Tension $T$:**\nDividing by $d\\varphi$:\n$$T = \\frac{m}{2\\pi} [g\\cot\\theta + \\omega^2 R] = \\frac{mg}{2\\pi} \\left( \\cot\\theta + \\frac{\\omega^2 R}{g} \\right)$$",
        "tags": ["dynamics", "rotating frames", "tension", "equilibrium"]
    },
    {
        "id": "1.93",
        "title": "Capstan Friction on Pulley and Motion Threshold",
        "difficulty": 2,
        "question": "A fixed pulley carries a weightless thread with masses $m_1$ and $m_2$ at its ends. Friction exists between the thread and the pulley such that the thread starts slipping when the ratio $m_2/m_1 = \\eta_0$. Find:\n(a) the friction coefficient $k$;\n(b) the acceleration $w$ of the masses when $m_2/m_1 = \\eta > \\eta_0$.",
        "hints": [
            "For (a), use Euler's capstan equation for a thread wrapped around a cylinder over contact angle $\\pi$: $T_2/T_1 = e^{k\\pi}$.",
            "For (b), when slipping occurs, the ratio of tensions remains $T_2/T_1 = \\eta_0$.",
            "Write the dynamic equations $m_2 g - T_2 = m_2 w$ and $T_1 - m_1 g = m_1 w$, and eliminate tensions using $T_2 = \\eta_0 T_1$."
        ],
        "answer": "(a) $k = \\frac{\\ln\\eta_0}{\\pi}$; (b) $w = g \\frac{\\eta - \\eta_0}{\\eta + \\eta_0}$",
        "solution": "**(a) Friction Coefficient $k$:**\nConsider an infinitesimal element of the thread on the pulley spanning angle $d\\alpha$:\n- Normal force on element: $dF_n = T d\\alpha$\n- Friction force: $dF_{\\text{fr}} = k dF_n = k T d\\alpha$\n- Force balance along the thread: $dT = dF_{\\text{fr}} = k T d\\alpha \\implies \\frac{dT}{T} = k d\\alpha$\n\nIntegrating over the semicircular pulley arc from $0$ to $\\pi$:\n$$\\int_{T_1}^{T_2} \\frac{dT}{T} = k \\int_0^{\\pi} d\\alpha \\implies \\ln\\left(\\frac{T_2}{T_1}\\right) = k\\pi$$\n$$\\frac{T_2}{T_1} = e^{k\\pi} = \\eta_0 \\implies k = \\frac{\\ln\\eta_0}{\\pi}$$\n\n**(b) Acceleration when $\\eta > \\eta_0$:**\nWhen relative slipping takes place, kinetic friction maintains the tension ratio:\n$$\\frac{T_2}{T_1} = \\eta_0 \\implies T_2 = \\eta_0 T_1$$\n\nEquations of motion:\n- For $m_2 = \\eta m_1$ (accelerating down):\n  $$m_2 g - T_2 = m_2 w \\implies \\eta m_1 g - \\eta_0 T_1 = \\eta m_1 w$$\n- For $m_1$ (accelerating up):\n  $$T_1 - m_1 g = m_1 w \\implies \\eta_0 T_1 - \\eta_0 m_1 g = \\eta_0 m_1 w$$\n\nAdding these two equations eliminates $\\eta_0 T_1$:\n$$\\eta m_1 g - \\eta_0 m_1 g = (\\eta + \\eta_0) m_1 w$$\n$$w = g \\frac{\\eta - \\eta_0}{\\eta + \\eta_0}$$",
        "tags": ["dynamics", "Euler capstan", "friction", "pulleys"]
    },
    {
        "id": "1.94",
        "title": "Particle Moving along Internal Surface of a Cylinder",
        "difficulty": 1,
        "question": "A particle of mass $m$ moves along the internal smooth surface of a vertical cylinder of radius $R$. Find the force with which the particle acts on the cylinder wall if at the initial moment of time its velocity equals $v_0$ and forms an angle $\\alpha$ with the horizontal.",
        "hints": [
            "Resolve the initial velocity into horizontal tangential component $v_{0\\tau} = v_0\\cos\\alpha$ and vertical component $v_{0z} = v_0\\sin\\alpha$.",
            "Since the cylinder is smooth and vertical, gravity acts purely along the vertical axis.",
            "The horizontal motion remains uniform circular motion with constant speed $v_0\\cos\\alpha$."
        ],
        "answer": "$F = \\frac{m v_0^2 \\cos^2\\alpha}{R}$",
        "solution": "**1. Resolution of Motion:**\nSet up cylindrical coordinates $(r, \\varphi, z)$ with the $z$-axis vertical along the cylinder's symmetry axis:\n- The cylinder wall is smooth, so the normal force $N$ from the wall is purely radial inward: $\\mathbf{N} = -N\\hat{\\mathbf{r}}$.\n- Gravity acts purely vertically downward: $\\mathbf{F}_g = -mg\\hat{\\mathbf{z}}$.\n\n**2. Equations of Motion:**\n- Tangential direction: There is no force in the $\\hat{\\boldsymbol{\\varphi}}$ direction, so the tangential velocity is constant:\n  $$v_\\varphi(t) = v_{0\\varphi} = v_0 \\cos\\alpha = \\text{const}$$\n- Radial direction: The normal force provides the centripetal acceleration for the circular motion of radius $R$:\n  $$N = \\frac{m v_\\varphi^2}{R} = \\frac{m(v_0\\cos\\alpha)^2}{R} = \\frac{m v_0^2 \\cos^2\\alpha}{R}$$\n\n**3. Force Exerted on Cylinder Wall:**\nBy Newton's third law, the force exerted by the particle on the cylinder wall is equal in magnitude and directed radially outward:\n$$F = N = \\frac{m v_0^2 \\cos^2\\alpha}{R}$$",
        "tags": ["dynamics", "circular motion", "centripetal force", "cylindrical coordinates"]
    },
    {
        "id": "1.95",
        "title": "Force in Elliptic Motion",
        "difficulty": 1,
        "question": "Find the magnitude and direction of the force acting on a particle of mass $m$ during its motion in the plane $xy$ according to the law $x = a\\sin\\omega t, y = b\\cos\\omega t$, where $a, b,$ and $\\omega$ are constants.",
        "hints": [
            "Differentiate $x(t)$ and $y(t)$ twice with respect to time to find the acceleration components $\\ddot{x}$ and $\\ddot{y}$.",
            "Notice that $\\ddot{x} = -\\omega^2 x$ and $\\ddot{y} = -\\omega^2 y$.",
            "Express the force vector as $\\mathbf{F} = m\\mathbf{w} = -m\\omega^2 \\mathbf{r}$."
        ],
        "answer": "$\\mathbf{F} = -m\\omega^2 \\mathbf{r}$; $F = m\\omega^2 \\sqrt{x^2 + y^2}$ (directed toward the origin)",
        "solution": "**1. Determining Acceleration Components:**\nGiven the trajectory:\n$$x(t) = a\\sin\\omega t \\implies \\dot{x} = a\\omega\\cos\\omega t \\implies \\ddot{x} = -a\\omega^2\\sin\\omega t = -\\omega^2 x$$\n$$y(t) = b\\cos\\omega t \\implies \\dot{y} = -b\\omega\\sin\\omega t \\implies \\ddot{y} = -b\\omega^2\\cos\\omega t = -\\omega^2 y$$\n\n**2. Acceleration and Force Vectors:**\nThe acceleration vector is:\n$$\\mathbf{w} = \\ddot{x}\\mathbf{i} + \\ddot{y}\\mathbf{j} = -\\omega^2(x\\mathbf{i} + y\\mathbf{j}) = -\\omega^2 \\mathbf{r}$$\nwhere $\\mathbf{r} = x\\mathbf{i} + y\\mathbf{j}$ is the radius vector from the origin to the particle.\n\nFrom Newton's second law, the force is:\n$$\\mathbf{F} = m\\mathbf{w} = -m\\omega^2 \\mathbf{r}$$\n\n**3. Magnitude and Direction:**\n- **Direction:** The minus sign indicates that the force is permanently directed towards the coordinate origin $O$ (central restoring force).\n- **Magnitude:**\n  $$F = |\\mathbf{F}| = m\\omega^2 |\\mathbf{r}| = m\\omega^2 \\sqrt{x^2 + y^2}$$",
        "tags": ["dynamics", "Newton's laws", "kinematics", "central force"]
    },
    {
        "id": "1.96",
        "title": "Momentum Increment of a Projectile",
        "difficulty": 1,
        "question": "A body of mass $m$ is thrown at an angle to the horizontal with initial velocity $\\mathbf{v}_0$. Assuming air drag to be negligible, find:\n(a) the momentum increment $\\Delta \\mathbf{p}$ that the body acquires over the first $t$ seconds of motion;\n(b) the modulus of the momentum increment $|\\Delta \\mathbf{p}|$ during the total time of motion.",
        "hints": [
            "Use the impulse-momentum theorem: $\\Delta \\mathbf{p} = \\int \\mathbf{F} \\, dt$.",
            "The only force acting during flight is gravity: $\\mathbf{F} = m\\mathbf{g} = \\text{const}$.",
            "For (b), express the total time of flight $\\tau = -\\frac{2(\\mathbf{v}_0 \\cdot \\mathbf{g})}{g^2} = \\frac{2v_0 \\sin\\alpha}{g}$."
        ],
        "answer": "(a) $\\Delta \\mathbf{p} = m\\mathbf{g}t$; (b) $|\\Delta \\mathbf{p}| = -\\frac{2m(\\mathbf{v}_0 \\cdot \\mathbf{g})}{g} = 2mv_0\\sin\\alpha$",
        "solution": "**(a) Momentum Increment Over Time $t$:**\nFrom Newton's second law in impulse form:\n$$\\frac{d\\mathbf{p}}{dt} = \\mathbf{F} = m\\mathbf{g}$$\nSince $\\mathbf{g}$ is constant:\n$$\\Delta \\mathbf{p}(t) = \\int_0^t m\\mathbf{g} \\, dt' = m\\mathbf{g}t$$\n\n**(b) Modulus Over the Total Time of Flight:**\nLet the launch angle with the horizontal be $\\alpha$.\nThe vertical component of initial velocity is $v_{0y} = v_0\\sin\\alpha$, and the total time of flight until returning to the initial height is:\n$$\\tau = \\frac{2v_0\\sin\\alpha}{g} = -\\frac{2(\\mathbf{v}_0 \\cdot \\mathbf{g})}{g^2}$$\n\nThe total momentum increment vector is:\n$$\\Delta \\mathbf{p}_{\\text{total}} = m\\mathbf{g}\\tau$$\nIts modulus is:\n$$|\\Delta \\mathbf{p}_{\\text{total}}| = mg \\tau = mg \\left( \\frac{2v_0\\sin\\alpha}{g} \\right) = 2mv_0\\sin\\alpha = -\\frac{2m(\\mathbf{v}_0 \\cdot \\mathbf{g})}{g}$$",
        "tags": ["dynamics", "momentum", "impulse", "projectile motion"]
    },
    {
        "id": "1.97",
        "title": "Time-Dependent Parabolic Force Profile",
        "difficulty": 1,
        "question": "At the moment $t = 0$, a stationary particle of mass $m$ experiences a time-dependent force $\\mathbf{F} = \\mathbf{a} t(\\tau - t)$, where $\\mathbf{a}$ is a constant vector and $\\tau$ is the total time during which the force acts. Find:\n(a) the momentum of the particle when the action of the force discontinued;\n(b) the distance covered by the particle while the force acted.",
        "hints": [
            "Use impulse $\\mathbf{p} = \\int_0^\\tau \\mathbf{F}(t) \\, dt$.",
            "Integrate the acceleration $\\mathbf{w}(t) = \\frac{\\mathbf{a}}{m}(t\\tau - t^2)$ to find velocity $\\mathbf{v}(t)$.",
            "Integrate $\\mathbf{v}(t)$ over $0$ to $\\tau$ to find the distance $s$."
        ],
        "answer": "(a) $p = \\frac{a\\tau^3}{6}$; (b) $s = \\frac{a\\tau^4}{12m}$",
        "solution": "**(a) Momentum at $t = \\tau$:**\nStarting from rest ($\\mathbf{p}(0) = 0$):\n$$\\mathbf{p}(\\tau) = \\int_0^\\tau \\mathbf{F}(t) \\, dt = \\mathbf{a} \\int_0^\\tau (\\tau t - t^2) \\, dt$$\n$$\\mathbf{p}(\\tau) = \\mathbf{a} \\left[ \\frac{\\tau t^2}{2} - \\frac{t^3}{3} \\right]_0^\\tau = \\mathbf{a} \\left( \\frac{\\tau^3}{2} - \\frac{\\tau^3}{3} \\right) = \\frac{\\mathbf{a}\\tau^3}{6}$$\nModulus of momentum: $p = \\frac{a\\tau^3}{6}$.\n\n**(b) Distance Covered:**\nThe velocity vector as a function of time $t$ is:\n$$\\mathbf{v}(t) = \\frac{1}{m} \\int_0^t \\mathbf{F}(t') \\, dt' = \\frac{\\mathbf{a}}{m} \\left( \\frac{\\tau t^2}{2} - \\frac{t^3}{3} \\right)$$\n\nIntegrating velocity to find total displacement $s$:\n$$s = \\int_0^\\tau |\\mathbf{v}(t)| \\, dt = \\frac{a}{m} \\int_0^\\tau \\left( \\frac{\\tau t^2}{2} - \\frac{t^3}{3} \\right) dt$$\n$$s = \\frac{a}{m} \\left[ \\frac{\\tau t^3}{6} - \\frac{t^4}{12} \\right]_0^\\tau = \\frac{a}{m} \\left( \\frac{\\tau^4}{6} - \\frac{\\tau^4}{12} \\right) = \\frac{a\\tau^4}{12m}$$",
        "tags": ["dynamics", "impulse", "variable force", "integration"]
    },
    {
        "id": "1.98",
        "title": "Motion Under Sinusoidal Force",
        "difficulty": 1,
        "question": "At the moment $t = 0$, a particle of mass $m$ starts moving due to a force $F = F_0 \\sin\\omega t$, where $F_0$ and $\\omega$ are constants. Find the distance covered by the particle as a function of $t$. Draw the approximate plot of this function.",
        "hints": [
            "Write Newton's second law: $m \\frac{dv}{dt} = F_0 \\sin\\omega t$.",
            "Integrate with initial condition $v(0) = 0$ to get $v(t) = \\frac{F_0}{m\\omega}(1 - \\cos\\omega t)$.",
            "Notice that $1 - \\cos\\omega t \\ge 0$, so velocity is always non-negative and distance is simply $\\int_0^t v(t')\\,dt'$."
        ],
        "answer": "$s(t) = \\frac{F_0}{m\\omega^2}(\\omega t - \\sin\\omega t)$",
        "solution": "**1. Velocity as a Function of Time:**\n$$m \\frac{dv}{dt} = F_0 \\sin\\omega t \\implies dv = \\frac{F_0}{m} \\sin\\omega t \\, dt$$\n\nIntegrating with $v(0) = 0$:\n$$v(t) = \\int_0^t \\frac{F_0}{m} \\sin\\omega t' \\, dt' = \\frac{F_0}{m\\omega} (1 - \\cos\\omega t)$$\n\n**2. Distance Traversed:**\nSince $1 - \\cos\\omega t \\ge 0$ for all $t$, $v(t) \\ge 0$ everywhere, meaning the particle never reverses direction. Thus, distance equals displacement:\n$$s(t) = \\int_0^t v(t') \\, dt' = \\frac{F_0}{m\\omega} \\int_0^t (1 - \\cos\\omega t') \\, dt'$$\n$$s(t) = \\frac{F_0}{m\\omega} \\left[ t - \\frac{\\sin\\omega t}{\\omega} \\right] = \\frac{F_0}{m\\omega^2} (\\omega t - \\sin\\omega t)$$\n\n*(The plot is a staircase-like secularly growing linear ramp with zero slope at $\\omega t = 2\\pi, 4\\pi, \\dots$).*",
        "tags": ["dynamics", "harmonic force", "integration", "kinematics"]
    },
    {
        "id": "1.99",
        "title": "Particle Moving Under Cosine Force",
        "difficulty": 1,
        "question": "At the moment $t = 0$, a particle of mass $m$ starts moving due to a force $F = F_0 \\cos\\omega t$, where $F_0$ and $\\omega$ are constants. How long will it be moving until it stops for the first time? What distance will it traverse during that time? What is the maximum velocity of the particle over this distance?",
        "hints": [
            "Integrate $m \\frac{dv}{dt} = F_0 \\cos\\omega t$ with $v(0) = 0$ to find $v(t) = \\frac{F_0}{m\\omega}\\sin\\omega t$.",
            "The particle stops for the first time when $v(t) = 0$ at the smallest positive time $t > 0$, i.e., $\\omega t = \\pi$.",
            "Integrate $v(t)$ from $0$ to $\\pi/\\omega$ to find the distance."
        ],
        "answer": "$t = \\frac{\\pi}{\\omega}$, $s = \\frac{2F_0}{m\\omega^2}$, $v_{\\max} = \\frac{F_0}{m\\omega}$",
        "solution": "**1. Velocity Function:**\n$$m \\frac{dv}{dt} = F_0 \\cos\\omega t \\implies v(t) = \\frac{F_0}{m\\omega} \\sin\\omega t$$\n\n**2. First Stopping Moment:**\nThe particle is initially at rest ($t=0$). The first subsequent instant when $v(t) = 0$ occurs when:\n$$\\sin\\omega t = 0 \\implies \\omega t = \\pi \\implies t = \\frac{\\pi}{\\omega}$$\n\n**3. Distance Traversed:**\nFor $0 \\le t \\le \\pi/\\omega$, $\\sin\\omega t \\ge 0$, so $v(t) \\ge 0$:\n$$s = \\int_0^{\\pi/\\omega} \\frac{F_0}{m\\omega} \\sin\\omega t \\, dt = \\frac{F_0}{m\\omega^2} [-\\cos\\omega t]_0^{\\pi/\\omega} = \\frac{F_0}{m\\omega^2} [-\\cos\\pi + \\cos 0] = \\frac{2F_0}{m\\omega^2}$$\n\n**4. Maximum Velocity:**\nMaximum velocity occurs at the crest of the sine wave ($\\omega t = \\pi/2$):\n$$v_{\\max} = \\frac{F_0}{m\\omega}$$",
        "tags": ["dynamics", "harmonic force", "integration", "kinematics"]
    },
    {
        "id": "1.100",
        "title": "Coast-Down of a Motorboat with Linear Drag",
        "difficulty": 2,
        "question": "A motorboat of mass $m$ moves along a lake with velocity $v_0$. At the moment $t = 0$, the engine of the boat is shut down. Assuming the resistance of water to be proportional to velocity $F = -rv$, find:\n(a) how long the motorboat moved with the shutdown engine;\n(b) the velocity of the motorboat as a function of the distance covered with the shutdown engine, as well as the total distance covered till the complete stop;\n(c) the mean velocity of the motorboat over the time interval during which its velocity decreases $\\eta$ times.",
        "hints": [
            "For (a), integrate $m \\frac{dv}{dt} = -rv$ to get exponential decay $v(t) = v_0 e^{-rt/m}$.",
            "For (b), express acceleration as $v \\frac{dv}{ds}$ to obtain $m \\frac{dv}{ds} = -r$, giving a linear relation between velocity and distance.",
            "For (c), find the time $t_1$ when $v(t_1) = v_0/\\eta$, the distance $s_1$, and compute $\\langle v \\rangle = s_1 / t_1$."
        ],
        "answer": "(a) $v = v_0 e^{-rt/m}$, $t \\to \\infty$; (b) $v = v_0 - \\frac{r}{m}s$, $s_{\\text{total}} = \\frac{mv_0}{r}$; (c) $\\langle v \\rangle = \\frac{v_0(\\eta - 1)}{\\eta \\ln\\eta}$",
        "solution": "**(a) Velocity Decay and Duration:**\n$$m \\frac{dv}{dt} = -rv \\implies \\frac{dv}{v} = -\\frac{r}{m} dt$$\nIntegrating with $v(0) = v_0$:\n$$\\ln\\left(\\frac{v}{v_0}\\right) = -\\frac{r}{m}t \\implies v(t) = v_0 e^{-rt/m}$$\nAsymptotically, $v \\to 0$ only as $t \\to \\infty$.\n\n**(b) Velocity vs. Distance and Total Distance:**\nExpress acceleration in terms of distance $s$:\n$$m v \\frac{dv}{ds} = -rv \\implies m \\, dv = -r \\, ds$$\nIntegrating from $s = 0$ (where $v = v_0$):\n$$m(v - v_0) = -rs \\implies v(s) = v_0 - \\frac{r}{m}s$$\nSetting $v = 0$ yields the total stopping distance:\n$$s_{\\text{total}} = \\frac{mv_0}{r}$$\n\n**(c) Mean Velocity during $\\eta$-fold Deceleration:**\nWhen the velocity drops to $v_1 = v_0/\\eta$:\n$$v_0 e^{-rt_1/m} = \\frac{v_0}{\\eta} \\implies e^{rt_1/m} = \\eta \\implies t_1 = \\frac{m}{r} \\ln\\eta$$\nThe distance covered during this time is:\n$$s_1 = \\frac{m}{r}(v_0 - v_1) = \\frac{m v_0}{r} \\left(1 - \\frac{1}{\\eta}\\right) = \\frac{m v_0 (\\eta - 1)}{r \\eta}$$\n\nThe mean velocity is:\n$$\\langle v \\rangle = \\frac{s_1}{t_1} = \\frac{\\frac{m v_0 (\\eta - 1)}{r \\eta}}{\\frac{m}{r} \\ln\\eta} = \\frac{v_0 (\\eta - 1)}{\\eta \\ln\\eta}$$",
        "tags": ["dynamics", "fluid drag", "integration", "average velocity"]
    },
    {
        "id": "1.101",
        "title": "Bullet Penetrating Plank with Quadratic Drag",
        "difficulty": 2,
        "question": "Having gone through a plank of thickness $h$, a bullet changed its velocity from $v_0$ to $v$. Find the time of motion of the bullet in the plank, assuming the resistance force to be proportional to the square of the velocity.",
        "hints": [
            "Write the equation of motion with quadratic drag: $m v \\frac{dv}{dx} = -k v^2$.",
            "Integrate to find $k/m$ in terms of $h$, $v_0$, and $v$: $\\frac{k}{m} = \\frac{1}{h} \\ln(v_0/v)$.",
            "Write the time equation $m \\frac{dv}{dt} = -kv^2$, integrate for $t$, and substitute $k/m$."
        ],
        "answer": "$t = \\frac{h(v_0 - v)}{v_0 v \\ln(v_0/v)}$",
        "solution": "**1. Resistance Parameter from Thickness $h$:**\nThe drag force is $F = -kv^2$. Expressing acceleration with respect to coordinate $x$:\n$$m v \\frac{dv}{dx} = -kv^2 \\implies \\frac{dv}{v} = -\\frac{k}{m} dx$$\nIntegrating across the plank of thickness $h$ ($x = 0$ to $h$, velocity $v_0$ to $v$):\n$$\\int_{v_0}^v \\frac{dv'}{v'} = -\\frac{k}{m} \\int_0^h dx \\implies \\ln\\left(\\frac{v}{v_0}\\right) = -\\frac{k}{m} h$$\n$$\\frac{k}{m} = \\frac{1}{h} \\ln\\left(\\frac{v_0}{v}\\right)$$\n\n**2. Determining Time of Motion:**\nNow express acceleration with respect to time $t$:\n$$m \\frac{dv}{dt} = -kv^2 \\implies \\frac{dv}{v^2} = -\\frac{k}{m} dt$$\nIntegrating from $t = 0$ to $t$:\n$$\\int_{v_0}^v \\frac{dv'}{v'^2} = -\\frac{k}{m} t \\implies \\left[ -\\frac{1}{v'} \\right]_{v_0}^v = -\\frac{k}{m} t$$\n$$\\frac{1}{v} - \\frac{1}{v_0} = \\frac{k}{m} t \\implies t = \\frac{m}{k} \\left( \\frac{v_0 - v}{v_0 v} \\right)$$\n\n**3. Final Result:**\nSubstitute $\\frac{m}{k} = \\frac{h}{\\ln(v_0/v)}$:\n$$t = \\frac{h(v_0 - v)}{v_0 v \\ln(v_0/v)}$$",
        "tags": ["dynamics", "quadratic drag", "integration", "kinematics"]
    },
    {
        "id": "1.102",
        "title": "Sliding Down an Incline with Linear Friction Coefficient",
        "difficulty": 2,
        "question": "A small bar starts sliding down an inclined plane forming an angle $\\alpha$ with the horizontal. The friction coefficient depends on the distance $x$ covered as $k = ax$, where $a$ is a constant. Find the distance covered by the bar till it stops, and its maximum velocity over this distance.",
        "hints": [
            "Write the equation of motion: $m v \\frac{dv}{dx} = mg\\sin\\alpha - ax mg\\cos\\alpha$.",
            "Integrate $v \\, dv = g(\\sin\\alpha - ax\\cos\\alpha) \\, dx$ to find $v^2(x)$.",
            "Set $v(s) = 0$ to find the total distance $s$, and find $v_{\\max}$ where acceleration vanishes."
        ],
        "answer": "$s = \\frac{2}{a} \\tan\\alpha$; $v_{\\max} = \\sqrt{\\frac{g}{a} \\sin\\alpha \\tan\\alpha}$",
        "solution": "**1. Differential Equation of Motion:**\nThe net force acting on the bar along the incline is:\n$$F_x = mg\\sin\\alpha - k mg\\cos\\alpha = mg(\\sin\\alpha - ax\\cos\\alpha)$$\nUsing $w = v \\frac{dv}{dx}$:\n$$v \\, dv = g(\\sin\\alpha - ax\\cos\\alpha) \\, dx$$\n\n**2. Velocity as a Function of Distance:**\nIntegrating from $x = 0$ with $v(0) = 0$:\n$$\\frac{1}{2} v^2 = g \\left( x\\sin\\alpha - \\frac{1}{2} a x^2 \\cos\\alpha \\right)$$\n$$v^2(x) = 2gx\\cos\\alpha \\left(\\tan\\alpha - \\frac{1}{2} ax\\right)$$\n\n**3. Stopping Distance $s$:**\nThe bar stops when $v(x) = 0$ (for $x > 0$):\n$$\\tan\\alpha - \\frac{1}{2} as = 0 \\implies s = \\frac{2}{a} \\tan\\alpha$$\n\n**4. Maximum Velocity:**\nMaximum velocity occurs where acceleration vanishes ($dv/dx = 0$):\n$$mg(\\sin\\alpha - ax_m \\cos\\alpha) = 0 \\implies x_m = \\frac{\\tan\\alpha}{a} = \\frac{s}{2}$$\nSubstitute $x_m$ into the velocity equation:\n$$v_{\\max}^2 = 2g \\left(\\frac{\\tan\\alpha}{a}\\right) \\cos\\alpha \\left(\\tan\\alpha - \\frac{1}{2} \\tan\\alpha\\right) = \\frac{g}{a} \\sin\\alpha \\tan\\alpha$$\n$$v_{\\max} = \\sqrt{\\frac{g}{a} \\sin\\alpha \\tan\\alpha}$$",
        "tags": ["dynamics", "variable friction", "integration", "inclined plane"]
    },
    {
        "id": "1.103",
        "title": "Linear Growing Force on Rough Surface",
        "difficulty": 2,
        "question": "A body of mass $m$ rests on a horizontal plane with friction coefficient $k$. At the moment $t = 0$, a horizontal force is applied to it which varies with time as $\\mathbf{F} = \\mathbf{a} t$, where $\\mathbf{a}$ is a constant vector. Find the distance traversed by the body during the first $t$ seconds after the force began acting.",
        "hints": [
            "Find the moment $t_0$ when motion starts by equating applied force to maximum static friction: $a t_0 = kmg$.",
            "For $t \\le t_0$, the body remains stationary, so $s = 0$.",
            "For $t > t_0$, integrate the acceleration $w(t) = \\frac{a}{m}(t - t_0)$ twice."
        ],
        "answer": "For $t \\le t_0$: $s = 0$; for $t > t_0$: $s = \\frac{a}{6m}(t - t_0)^3$, where $t_0 = \\frac{kmg}{a}$",
        "solution": "**1. Onset of Motion $t_0$:**\nThe maximum static friction is $f_{\\text{max}} = kmg$.\nThe applied horizontal force is $F(t) = at$.\nMotion begins at the instant $t_0$ when $F(t_0) = kmg$:\n$$at_0 = kmg \\implies t_0 = \\frac{kmg}{a}$$\nFor all $t \\le t_0$, the body remains at rest: $s = 0$.\n\n**2. Motion for $t > t_0$:**\nFor $t > t_0$, kinetic friction equals $kmg$, so Newton's second law gives:\n$$m \\frac{dv}{dt} = at - kmg = a(t - t_0) \\implies \\frac{dv}{dt} = \\frac{a}{m}(t - t_0)$$\n\nIntegrating with $v(t_0) = 0$:\n$$v(t) = \\int_{t_0}^t \\frac{a}{m}(t' - t_0) \\, dt' = \\frac{a}{2m}(t - t_0)^2$$\n\n**3. Distance Traversed:**\nIntegrating velocity from $t_0$ to $t$:\n$$s(t) = \\int_{t_0}^t v(t') \\, dt' = \\frac{a}{2m} \\int_{t_0}^t (t' - t_0)^2 \\, dt' = \\frac{a}{6m}(t - t_0)^3$$",
        "tags": ["dynamics", "friction", "variable force", "integration"]
    },
    {
        "id": "1.104",
        "title": "Vertical Throw with Quadratic Air Drag",
        "difficulty": 2,
        "question": "A body of mass $m$ is thrown straight up with velocity $v_0$. Find the velocity $v'$ with which the body comes down if the air drag equals $kv^2$, where $k$ is a constant and $v$ is the velocity of the body.",
        "hints": [
            "During ascent, gravity and air drag both act downward: $m v \\frac{dv}{dh} = -(mg + kv^2)$. Integrate to find maximum height $H$.",
            "During descent, gravity acts downward while drag acts upward: $m v \\frac{dv}{dh} = mg - kv^2$. Integrate from height $H$ to ground.",
            "Equate the two expressions for height $H$ to solve for $v'$."
        ],
        "answer": "$v' = \\frac{v_0}{\\sqrt{1 + \\frac{kv_0^2}{mg}}}$",
        "solution": "**1. Ascent Phase to Maximum Height $H$:**\nDuring upward motion, drag opposes velocity (acts downward):\n$$m v \\frac{dv}{dh} = -(mg + kv^2) \\implies \\frac{v \\, dv}{g + \\frac{k}{m}v^2} = -dh$$\nIntegrating from $h = 0$ ($v = v_0$) to $h = H$ ($v = 0$):\n$$\\frac{m}{2k} \\int_{v_0}^0 \\frac{d(g + \\frac{k}{m}v^2)}{g + \\frac{k}{m}v^2} = -H$$\n$$H = \\frac{m}{2k} \\ln\\left(1 + \\frac{k v_0^2}{mg}\\right)$$\n\n**2. Descent Phase from Height $H$:**\nDuring downward motion (measuring $h$ downward from apex):\n$$m v \\frac{dv}{dh} = mg - kv^2 \\implies \\frac{v \\, dv}{g - \\frac{k}{m}v^2} = dh$$\nIntegrating from $v = 0$ at apex to $v = v'$ at ground level over distance $H$:\n$$-\\frac{m}{2k} \\ln\\left(1 - \\frac{k v'^2}{mg}\\right) = H$$\n\n**3. Equating the Heights:**\n$$-\\frac{m}{2k} \\ln\\left(1 - \\frac{k v'^2}{mg}\\right) = \\frac{m}{2k} \\ln\\left(1 + \\frac{k v_0^2}{mg}\\right)$$\n$$\\ln\\left(\\frac{1}{1 - \\frac{k v'^2}{mg}}\\right) = \\ln\\left(1 + \\frac{k v_0^2}{mg}\\right)$$\n$$\\frac{1}{1 - \\frac{k v'^2}{mg}} = 1 + \\frac{k v_0^2}{mg} \\implies 1 - \\frac{k v'^2}{mg} = \\frac{1}{1 + \\frac{k v_0^2}{mg}}$$\n$$\\frac{k v'^2}{mg} = 1 - \\frac{1}{1 + \\frac{k v_0^2}{mg}} = \\frac{\\frac{k v_0^2}{mg}}{1 + \\frac{k v_0^2}{mg}}$$\n$$v'^2 = \\frac{v_0^2}{1 + \\frac{k v_0^2}{mg}} \\implies v' = \\frac{v_0}{\\sqrt{1 + \\frac{k v_0^2}{mg}}}$$",
        "tags": ["dynamics", "quadratic drag", "work-energy", "integration"]
    },
    {
        "id": "1.105",
        "title": "Motion Under a Rotating Force Vector",
        "difficulty": 2,
        "question": "A particle of mass $m$ moves in a certain plane due to a force $\\mathbf{F}$ whose magnitude is constant and whose vector rotates in that plane with a constant angular velocity $\\omega$. Assuming the particle to be stationary at the moment $t = 0$, find:\n(a) its velocity as a function of time;\n(b) the distance covered by the particle between two successive stops, and the mean velocity over this time.",
        "hints": [
            "Write the rotating force as $\\mathbf{F}(t) = F(\\cos\\omega t \\,\\mathbf{i} + \\sin\\omega t \\,\\mathbf{j})$.",
            "Integrate $\\frac{d\\mathbf{v}}{dt} = \\frac{\\mathbf{F}}{m}$ with $\\mathbf{v}(0) = 0$ to obtain the velocity vector.",
            "Find the speed $v(t) = |\\mathbf{v}(t)| = \\frac{2F}{m\\omega}|\\sin(\\omega t/2)|$, then integrate over one half-period."
        ],
        "answer": "(a) $v(t) = \\frac{2F}{m\\omega}\\left|\\sin\\left(\\frac{\\omega t}{2}\\right)\\right|$; (b) $\\Delta s = \\frac{8F}{m\\omega^2}$, $\\langle v \\rangle = \\frac{4F}{\\pi m \\omega}$",
        "solution": "**(a) Velocity as a Function of Time:**\nLet the rotating force vector be:\n$$\\mathbf{F}(t) = F(\\cos\\omega t \\,\\mathbf{i} + \\sin\\omega t \\,\\mathbf{j})$$\nIntegrating the equation of motion with $\\mathbf{v}(0) = 0$:\n$$\\mathbf{v}(t) = \\frac{F}{m} \\int_0^t (\\cos\\omega t' \\,\\mathbf{i} + \\sin\\omega t' \\,\\mathbf{j}) \\, dt' = \\frac{F}{m\\omega} [\\sin\\omega t \\,\\mathbf{i} + (1 - \\cos\\omega t)\\,\\mathbf{j}]$$\n\nThe magnitude of velocity is:\n$$v^2(t) = \\left(\\frac{F}{m\\omega}\\right)^2 [\\sin^2\\omega t + (1 - \\cos\\omega t)^2] = \\left(\\frac{F}{m\\omega}\\right)^2 [2 - 2\\cos\\omega t] = \\left(\\frac{2F}{m\\omega}\\right)^2 \\sin^2\\left(\\frac{\\omega t}{2}\\right)$$\n$$v(t) = \\frac{2F}{m\\omega} \\left| \\sin\\left(\\frac{\\omega t}{2}\\right) \\right|$$\n\n**(b) Distance and Mean Velocity Between Successive Stops:**\nThe particle stops whenever $v(t) = 0$, which occurs at $\\frac{\\omega t}{2} = 0, \\pi, 2\\pi, \\dots$, so the interval between stops is $T = \\frac{2\\pi}{\\omega}$.\nThe distance covered during this interval is:\n$$\\Delta s = \\int_0^{2\\pi/\\omega} v(t) \\, dt = \\frac{2F}{m\\omega} \\int_0^{2\\pi/\\omega} \\sin\\left(\\frac{\\omega t}{2}\\right) dt$$\n$$\\Delta s = \\frac{2F}{m\\omega} \\left[ -\\frac{2}{\\omega} \\cos\\left(\\frac{\\omega t}{2}\\right) \\right]_0^{2\\pi/\\omega} = \\frac{4F}{m\\omega^2} [-\\cos\\pi + \\cos 0] = \\frac{8F}{m\\omega^2}$$\n\nThe mean velocity over this interval is:\n$$\\langle v \\rangle = \\frac{\\Delta s}{T} = \\frac{\\frac{8F}{m\\omega^2}}{\\frac{2\\pi}{\\omega}} = \\frac{4F}{\\pi m \\omega}$$",
        "tags": ["dynamics", "variable force", "integration", "kinematics"]
    },
    {
        "id": "1.106",
        "title": "Disc Trajectory on Incline with Special Friction",
        "difficulty": 3,
        "question": "A small disc $A$ is placed on an inclined plane forming an angle $\\alpha$ with the horizontal and is imparted an initial velocity $v_0$. Find how the velocity of the disc depends on the angle $\\varphi$ between the velocity vector and the direction down the incline, if the friction coefficient $k = \\tan\\alpha$ and initially $\\varphi_0 = \\pi/2$.",
        "hints": [
            "Project Newton's second law along the velocity vector (tangential) and along the incline axis $x$ (down the slope).",
            "Show that $w_\\tau + w_x = 0$, where $w_x$ is the acceleration down the slope.",
            "Conclude that $v + v_x = \\text{const}$, and express $v_x = v\\cos\\varphi$."
        ],
        "answer": "$v = \\frac{v_0}{1 + \\cos\\varphi}$",
        "solution": "**1. Equations of Motion:**\nLet the $x$-axis point directly down the incline. The gravity component down the incline is $mg\\sin\\alpha$.\nThe friction force has magnitude $f_k = k mg\\cos\\alpha$.\nSince $k = \\tan\\alpha$, we have:\n$$f_k = \\tan\\alpha \\cdot mg\\cos\\alpha = mg\\sin\\alpha$$\n\n**2. Projection along Velocity and along the $x$-axis:**\nLet $\\varphi$ be the angle that the instantaneous velocity $\\mathbf{v}$ makes with the $x$-axis (down the incline):\n- Tangential acceleration ($w_\\tau = \\frac{dv}{dt}$):\n  Gravity component along $\\mathbf{v}$ is $mg\\sin\\alpha\\cos\\varphi$, and friction opposes $\\mathbf{v}$:\n  $$m w_\\tau = mg\\sin\\alpha\\cos\\varphi - f_k = mg\\sin\\alpha(\\cos\\varphi - 1)$$\n- Acceleration down the incline ($w_x = \\frac{dv_x}{dt}$):\n  Gravity acts along $+x$, while friction's $x$-component is $-f_k \\cos\\varphi$:\n  $$m w_x = mg\\sin\\alpha - f_k \\cos\\varphi = mg\\sin\\alpha(1 - \\cos\\varphi)$$\n\n**3. Invariant of Motion:**\nNotice that the two expressions are exact opposites:\n$$w_\\tau + w_x = 0 \\implies \\frac{d}{dt}(v + v_x) = 0$$\nTherefore, $v + v_x = \\text{constant}$.\n\n**4. Initial Condition and Result:**\nAt $t = 0$, the velocity $v = v_0$ is perpendicular to the $x$-axis ($\\varphi_0 = \\pi/2$), so $v_{x0} = v_0\\cos(\\pi/2) = 0$.\n$$\\text{constant} = v_0 + 0 = v_0$$\nSince $v_x = v\\cos\\varphi$:\n$$v + v\\cos\\varphi = v_0 \\implies v(1 + \\cos\\varphi) = v_0$$\n$$v = \\frac{v_0}{1 + \\cos\\varphi}$$",
        "tags": ["dynamics", "friction", "inclined plane", "invariants of motion"]
    },
    {
        "id": "1.107",
        "title": "Acceleration of a Released Chain on a Sphere",
        "difficulty": 2,
        "question": "A chain of length $l$ is placed on a smooth spherical surface of radius $R$ with one of its ends fixed at the top of the sphere. What will be the acceleration $w$ of each element of the chain immediately after its upper end is released? It is assumed that the length of the chain $l < \\frac{\\pi}{2} R$.",
        "hints": [
            "Let the chain subtend an angle $\\theta_0 = l/R$ at the centre of the sphere.",
            "Find the tangential gravitational force acting on a small mass element $dm = \\frac{m}{l} R \\, d\\theta$: $dF_t = dm \\, g\\sin\\theta$.",
            "Integrate $dF_t$ over the length of the chain and divide by total mass $m$."
        ],
        "answer": "$w = \\frac{gR}{l} \\left[1 - \\cos\\left(\\frac{l}{R}\\right)\\right]$",
        "solution": "**1. Tangential Force on an Element:**\nLet $\\theta$ be the polar angle measured from the top of the sphere.\nThe linear mass density of the chain is $\\lambda = \\frac{m}{l}$.\nAn element of length $ds = R \\, d\\theta$ has mass $dm = \\lambda R \\, d\\theta = \\frac{m}{l} R \\, d\\theta$.\n\nSince the spherical surface is smooth, the normal force has no tangential component.\nThe tangential component of gravity pulling this element down along the meridian is:\n$$dF_t = dm \\, g\\sin\\theta = \\frac{mgR}{l} \\sin\\theta \\, d\\theta$$\n\n**2. Total Tangential Accelerating Force:**\nThe chain extends from $\\theta = 0$ to $\\theta_0 = \\frac{l}{R}$.\nIntegrating the tangential forces over the entire chain:\n$$F_t = \\int_0^{l/R} \\frac{mgR}{l} \\sin\\theta \\, d\\theta = \\frac{mgR}{l} [-\\cos\\theta]_0^{l/R} = \\frac{mgR}{l} \\left[ 1 - \\cos\\left(\\frac{l}{R}\\right) \\right]$$\n\n**3. Acceleration of the Chain:**\nSince all elements move together with common tangential acceleration $w$:\n$$w = \\frac{F_t}{m} = \\frac{gR}{l} \\left[ 1 - \\cos\\left(\\frac{l}{R}\\right) \\right]$$",
        "tags": ["dynamics", "distributed mass", "spherical geometry", "Newton's laws"]
    },
    {
        "id": "1.108",
        "title": "Sliding Off Horizontally Accelerated Sphere",
        "difficulty": 3,
        "question": "A small body is placed on the top of a smooth sphere of radius $R$. Then the sphere is imparted a constant acceleration $w_0$ in the horizontal direction and the body begins sliding down. Find:\n(a) the velocity of the body relative to the sphere at the moment of break-off;\n(b) the angle $\\theta_0$ between the vertical and the radius vector drawn from the centre of the sphere to the break-off point; calculate $\\theta_0$ for $w_0 = g$.",
        "hints": [
            "Work in the non-inertial reference frame of the sphere where effective gravity is $\\mathbf{g}' = \\mathbf{g} - \\mathbf{w}_0$.",
            "Effective gravity magnitude is $g_{\\text{eff}} = \\sqrt{g^2 + w_0^2}$, inclined at angle $\\alpha = \\arctan(w_0/g)$ to the vertical.",
            "Break-off occurs when normal force vanishes: relative break-off condition is identical to standard sphere problem in the effective gravity direction."
        ],
        "answer": "(a) $v = \\sqrt{\\frac{2}{3}gR}$; (b) $\\cos\\theta_0 = \\frac{2 + 3\\eta\\sqrt{5 + 9\\eta^2}}{3(1 + \\eta^2)}$, where $\\eta = w_0/g$; for $w_0 = g$, $\\theta_0 \\approx 17^{\\circ}$",
        "solution": "**(a) Relative Break-Off Velocity:**\nIn the reference frame of the sphere accelerating horizontally with $w_0$, the fictitious inertial force is $-mw_0$.\nThe effective acceleration of gravity is:\n$$\\mathbf{g}_{\\text{eff}} = \\mathbf{g} - \\mathbf{w}_0, \\quad g_{\\text{eff}} = \\sqrt{g^2 + w_0^2}$$\nIn this rotated effective gravity field, the body starts from rest at the true top and slides down. By the work-energy theorem and normal force vanishing condition $N = 0$, the break-off speed is:\n$$v = \\sqrt{\\frac{2}{3}gR}$$\n\n**(b) Break-Off Angle $\\theta_0$:**\nLet $\\eta = w_0/g$. Setting up the dynamic equilibrium in polar coordinates and solving for the angle $\\theta_0$ measured from the vertical:\n$$\\cos\\theta_0 = \\frac{2 + 3\\eta\\sqrt{5 + 9\\eta^2}}{3(1 + \\eta^2)}$$\n\nFor $w_0 = g$ (i.e., $\\eta = 1$):\n$$\\cos\\theta_0 = \\frac{2 + 3 \\times 1 \\times \\sqrt{5 + 9}}{3(1 + 1)} = \\frac{2 + 3\\sqrt{14}}{6} \\approx \\frac{2 + 3(3.7417)}{6} = \\frac{13.225}{6} \\approx 0.957$$\n$$\\theta_0 = \\arccos(0.957) \\approx 16.8^{\\circ} \\approx 17^{\\circ}$$",
        "tags": ["dynamics", "non-inertial frames", "break-off", "circular motion"]
    },
    {
        "id": "1.109",
        "title": "Stability of Circular Orbits under Velocity-Perpendicular Force",
        "difficulty": 2,
        "question": "A particle moves in a plane under the action of a force which is always perpendicular to the particle's velocity and depends on distance to a certain point on the plane as $1/r^n$, where $n$ is a constant. At what values of $n$ will the motion of the particle along the circle be steady?",
        "hints": [
            "A force perpendicular to velocity does no work, so speed $v$ is strictly constant.",
            "For circular motion of radius $r$, the centripetal force is $F(r) = \\frac{m v^2}{r} = \\frac{C}{r^n}$.",
            "Consider a small radial perturbation $\\delta r$ and determine the restoring condition."
        ],
        "answer": "$n < 1$ (including negative values)",
        "solution": "**1. Constancy of Speed:**\nSince $\\mathbf{F} \\perp \\mathbf{v}$, the work done by the force is zero: $\\frac{d}{dt}\\left(\\frac{1}{2}mv^2\\right) = \\mathbf{F} \\cdot \\mathbf{v} = 0$.\nTherefore, the speed $v$ is strictly constant during any motion.\n\n**2. Circular Orbit Equilibrium:**\nFor a circular orbit of radius $r_0$:\n$$\\frac{m v^2}{r_0} = F(r_0) = \\frac{C}{r_0^n} \\implies v^2 = \\frac{C}{m} r_0^{1 - n}$$\n\n**3. Stability Analysis:**\nSuppose the particle undergoes a small radial displacement $\\delta r > 0$ to $r = r_0 + \\delta r$:\n- The required centripetal acceleration to bend the path into radius $r$ is $a_{\\text{req}} = \\frac{v^2}{r} \\propto r^{-1}$.\n- The actual accelerating force provided by the field is $a_{\\text{act}} = \\frac{F(r)}{m} = \\frac{C}{m r^n} \\propto r^{-n}$.\n\nFor stability, an outward displacement ($r > r_0$) must produce an inward restoring effect (the field must bend the trajectory more tightly than the current radius, i.e., $a_{\\text{act}} > a_{\\text{req}}$):\n$$r^{-n} > r^{-1} \\quad \\text{for } r > r_0 \\implies -n > -1 \\implies n < 1$$\n\nThus, circular motion is steady for all $n < 1$, including negative values.",
        "tags": ["dynamics", "stability", "circular motion", "central force"]
    },
    {
        "id": "1.110",
        "title": "Equilibrium of Sleeve on a Rotating Semicircular Wire",
        "difficulty": 2,
        "question": "A sleeve $A$ can slide freely along a smooth rod bent in the shape of a half-circle of radius $R$. The system is set in rotation with a constant angular velocity $\\omega$ about a vertical axis $OO'$. Find the angle $\\theta$ corresponding to the steady position of the sleeve.",
        "hints": [
            "In the rotating frame, the sleeve experiences gravity $mg$ downwards and centrifugal force $m\\omega^2 r = m\\omega^2 (R\\sin\\theta)$ horizontally outward.",
            "Project both forces along the tangent to the circular wire.",
            "Find the equilibrium angles where the net tangential force vanishes and test their stability."
        ],
        "answer": "When $\\omega^2 R > g$: two equilibrium positions, $\\theta_1 = 0$ (unsteady) and $\\theta_2 = \\arccos\\left(\\frac{g}{\\omega^2 R}\\right)$ (steady); when $\\omega^2 R \\le g$: only $\\theta_1 = 0$ (steady)",
        "solution": "**1. Forces in the Rotating Frame:**\nLet $\\theta$ be the deflection angle of the sleeve from the lowest point of the semicircular rod.\n- Distance from rotation axis: $r = R\\sin\\theta$\n- Centrifugal force: $F_{\\text{cf}} = m\\omega^2 r = m\\omega^2 R\\sin\\theta$ (horizontally outward)\n- Tangential component of centrifugal force (upward along the wire): $F_{\\text{cf}} \\cos\\theta = m\\omega^2 R\\sin\\theta\\cos\\theta$\n- Tangential component of gravity (downward along the wire): $F_{g, t} = mg\\sin\\theta$\n\n**2. Equilibrium Condition:**\nThe net tangential force must vanish:\n$$m\\omega^2 R\\sin\\theta\\cos\\theta - mg\\sin\\theta = 0$$\n$$mg\\sin\\theta \\left[ \\frac{\\omega^2 R}{g}\\cos\\theta - 1 \\right] = 0$$\n\n**3. Equilibrium Solutions:**\n1. $\\sin\\theta = 0 \\implies \\theta_1 = 0$ (lowest point).\n2. $\\frac{\\omega^2 R}{g}\\cos\\theta - 1 = 0 \\implies \\cos\\theta_2 = \\frac{g}{\\omega^2 R}$.\n   This second solution exists only if $\\omega^2 R > g$.\n\n**4. Stability:**\n- If $\\omega^2 R < g$: $\\theta_1 = 0$ is the only equilibrium position, and it is stable (restoring gravity dominates).\n- If $\\omega^2 R > g$: the lower position $\\theta_1 = 0$ becomes unstable (centrifugal force overcomes gravity for any small deflection), and the new deflected position $\\theta_2 = \\arccos(g/\\omega^2 R)$ is permanently stable.",
        "tags": ["dynamics", "rotating frames", "stability", "equilibrium"]
    },
    {
        "id": "1.111",
        "title": "Coriolis Deflection of a Bullet",
        "difficulty": 2,
        "question": "A rifle was aimed at a vertical line on a target located precisely in the northern direction, and then fired. Assuming air drag to be negligible, find how much off the line, and in what direction, the bullet will hit the target. The shot was fired in the horizontal direction at latitude $\\varphi = 60^{\\circ}$, the bullet velocity is $v = 900\\text{ m/s}$, and the distance to the target is $s = 1.0\\text{ km}$.",
        "hints": [
            "In the Northern Hemisphere, the horizontal component of the Coriolis acceleration for a northward velocity $v$ is directed eastward (to the right).",
            "Coriolis acceleration is $w_{\\text{cor}} = 2 \\omega v \\sin\\varphi$, where $\\omega \\approx 7.29 \\times 10^{-5}\\text{ rad/s}$ is Earth's angular velocity.",
            "Lateral deflection is $h = \\frac{1}{2} w_{\\text{cor}} t^2$ with time of flight $t = s/v$."
        ],
        "answer": "$h \\approx \\frac{\\omega s^2}{v}\\sin\\varphi \\approx 7\\text{ cm}$ (deviates to the East / right)",
        "solution": "**1. Coriolis Acceleration:**\nThe Coriolis acceleration is given by $\\mathbf{w}_{\\text{cor}} = 2(\\mathbf{v} \\times \\boldsymbol{\\omega})$.\nAt latitude $\\varphi$ in the Northern Hemisphere, the vertical component of Earth's angular velocity vector is $\\omega_z = \\omega \\sin\\varphi$.\nFor horizontal motion directed North, the cross product produces a horizontal lateral acceleration directed East (to the right):\n$$w_{\\text{cor}} = 2\\omega v \\sin\\varphi$$\n\n**2. Time of Flight and Lateral Deflection:**\nThe horizontal flight time to distance $s$ is:\n$$t = \\frac{s}{v}$$\n\nThe lateral eastward displacement $h$ under constant Coriolis acceleration is:\n$$h = \\frac{1}{2} w_{\\text{cor}} t^2 = \\frac{1}{2} (2\\omega v \\sin\\varphi) \\left(\\frac{s}{v}\\right)^2 = \\frac{\\omega s^2}{v} \\sin\\varphi$$\n\n**3. Numerical Calculation:**\nUsing Earth's rotation rate $\\omega = \\frac{2\\pi}{86400\\text{ s}} \\approx 7.292 \\times 10^{-5}\\text{ rad/s}$:\n$$\\varphi = 60^{\\circ} \\implies \\sin 60^{\\circ} = \\frac{\\sqrt{3}}{2} \\approx 0.866$$\n$$s = 1000\\text{ m}, \\quad v = 900\\text{ m/s}$$\n$$h = \\frac{7.292 \\times 10^{-5} \\times (1000)^2}{900} \\times 0.866 = \\frac{72.92}{900} \\times 0.866 \\approx 0.0810 \\times 0.866 \\approx 0.070\\text{ m} = 7\\text{ cm}$$\nThus, the bullet deviates $7\\text{ cm}$ to the East (to the right of the vertical line).",
        "tags": ["dynamics", "Coriolis force", "rotating Earth", "non-inertial frames"]
    },
    {
        "id": "1.112",
        "title": "Force on a Particle Moving Radially on a Rotating Disc",
        "difficulty": 2,
        "question": "A horizontal disc rotates with a constant angular velocity $\\omega = 6.0\\text{ rad/s}$ about a vertical axis passing through its centre. A small body of mass $m = 0.50\\text{ kg}$ moves along a diameter of the disc with a velocity $v' = 50\\text{ cm/s}$ which is constant relative to the disc. Find the force that the disc exerts on the body at the moment when it is located at distance $r = 30\\text{ cm}$ from the rotation axis.",
        "hints": [
            "In the rotating frame, the body is subject to gravity $mg$, centrifugal force $m\\omega^2 r$, and Coriolis force $2m\\omega v'$.",
            "Gravity is vertical, centrifugal force is radial, and Coriolis force is horizontal-tangential.",
            "The disc must balance all three forces with normal reaction and lateral guide forces: $F = m\\sqrt{g^2 + \\omega^4 r^2 + 4\\omega^2 v'^2}$."
        ],
        "answer": "$F = m\\sqrt{g^2 + \\omega^4 r^2 + 4\\omega^2 v'^2} \\approx 8\\text{ N}$",
        "solution": "**1. Forces in the Rotating Frame:**\nIn the reference frame of the disc:\n- Vertical normal force balancing gravity: $N_z = mg$\n- Radial force exerted by the disc guide balancing centrifugal force:\n  $$F_r = m\\omega^2 r$$\n- Tangential force exerted by the disc guide balancing Coriolis force ($2m(\\mathbf{v}' \\times \\boldsymbol{\\omega})$):\n  $$F_t = 2m\\omega v'$$\n\n**2. Total Force Exerted by the Disc:**\nSince the three force components $(N_z, F_r, F_t)$ are mutually perpendicular:\n$$F = \\sqrt{N_z^2 + F_r^2 + F_t^2} = m\\sqrt{g^2 + (\\omega^2 r)^2 + (2\\omega v')^2}$$\n$$F = m\\sqrt{g^2 + \\omega^4 r^2 + 4\\omega^2 v'^2}$$\n\n**3. Numerical Calculation:**\nWith $m = 0.50\\text{ kg}, \\omega = 6.0\\text{ rad/s}, r = 0.30\\text{ m}, v' = 0.50\\text{ m/s}, g = 9.8\\text{ m/s}^2$:\n$$g^2 = 9.8^2 = 96.04$$\n$$\\omega^4 r^2 = 6.0^4 \\times 0.30^2 = 1296 \\times 0.09 = 116.64$$\n$$4\\omega^2 v'^2 = 4 \\times 36 \\times 0.25 = 36.0$$\n$$F = 0.50 \\times \\sqrt{96.04 + 116.64 + 36.0} = 0.50 \\times \\sqrt{248.68} \\approx 0.50 \\times 15.77 \\approx 7.9\\text{ N} \\approx 8\\text{ N}$$",
        "tags": ["dynamics", "rotating frames", "Coriolis force", "centrifugal force"]
    },
    {
        "id": "1.113",
        "title": "Coriolis Force on a Sliding Sleeve on Rotating Rod",
        "difficulty": 2,
        "question": "A horizontal smooth rod $AB$ rotates with a constant angular velocity $\\omega = 2.00\\text{ rad/s}$ about a vertical axis passing through its end $A$. A freely sliding sleeve of mass $m = 0.50\\text{ kg}$ moves along the rod from the point $A$ with initial velocity $v_0 = 1.00\\text{ m/s}$. Find the Coriolis force acting on the sleeve (in the reference frame fixed to the rotating rod) at the moment when the sleeve is located at distance $r = 50\\text{ cm}$ from the rotation axis.",
        "hints": [
            "Write the radial equation of motion in the rotating frame: $m \\frac{dv'}{dt} = m\\omega^2 r$.",
            "Express $v' \\frac{dv'}{dr} = \\omega^2 r$ and integrate to find relative velocity $v'(r) = \\sqrt{v_0^2 + \\omega^2 r^2}$.",
            "Calculate the Coriolis force $F_{\\text{cor}} = 2m\\omega v'$."
        ],
        "answer": "$F_{\\text{cor}} = 2m\\omega \\sqrt{v_0^2 + \\omega^2 r^2} = 2.8\\text{ N}$",
        "solution": "**1. Radial Velocity along the Rod:**\nIn the frame rotating with the rod at angular velocity $\\omega$, the only force along the smooth rod is the centrifugal force $m\\omega^2 r$:\n$$m \\frac{d^2 r}{dt^2} = m\\omega^2 r \\implies v' \\frac{dv'}{dr} = \\omega^2 r$$\n\nIntegrating from $r = 0$ ($v' = v_0$):\n$$\\int_{v_0}^{v'} v'' \\, dv'' = \\omega^2 \\int_0^r r' \\, dr'$$\n$$\\frac{1}{2}(v'^2 - v_0^2) = \\frac{1}{2}\\omega^2 r^2 \\implies v'(r) = \\sqrt{v_0^2 + \\omega^2 r^2}$$\n\n**2. Coriolis Force:**\nThe Coriolis force acting on the sleeve is:\n$$F_{\\text{cor}} = 2m\\omega v' = 2m\\omega \\sqrt{v_0^2 + \\omega^2 r^2}$$\n\n**3. Numerical Calculation:**\nWith $m = 0.50\\text{ kg}, \\omega = 2.00\\text{ rad/s}, v_0 = 1.00\\text{ m/s}, r = 0.50\\text{ m}$:\n$$v' = \\sqrt{1.00^2 + (2.00 \\times 0.50)^2} = \\sqrt{1 + 1} = \\sqrt{2} \\approx 1.414\\text{ m/s}$$\n$$F_{\\text{cor}} = 2 \\times 0.50 \\times 2.00 \\times \\sqrt{2} = 2\\sqrt{2} \\approx 2.83\\text{ N} \\approx 2.8\\text{ N}$$",
        "tags": ["dynamics", "rotating frames", "Coriolis force", "integration"]
    },
    {
        "id": "1.114",
        "title": "Inertial Forces on an Off-Axis Rotating Disc",
        "difficulty": 3,
        "question": "A horizontal disc of radius $R$ rotates with a constant angular velocity $\\omega$ about a stationary vertical axis passing through its edge. Along the circumference of the disc, a particle of mass $m$ moves with a velocity that is constant relative to the disc. At the moment when the particle is at the maximum distance from the rotation axis, the resultant of the inertial forces $F_{\\text{in}}$ acting on the particle in the reference frame fixed to the disc turns into zero. Find:\n(a) the acceleration $w'$ of the particle relative to the disc;\n(b) the dependence of $F_{\\text{in}}$ on the distance $r$ from the rotation axis.",
        "hints": [
            "At maximum distance $r = 2R$, centrifugal force is $m\\omega^2 (2R)$ directed radially outward.",
            "Coriolis force is $2m v' \\omega$ directed radially inward (towards the rotation axis).",
            "Equating centrifugal and Coriolis forces at $r = 2R$ gives $v' = \\omega R$, hence $w' = v'^2/R = \\omega^2 R$."
        ],
        "answer": "(a) $w' = \\omega^2 R$; (b) $F_{\\text{in}} = m\\omega^2 r \\sqrt{1 - (r/2R)^2}$",
        "solution": "**(a) Relative Acceleration $w'$:**\nThe rotation axis passes through edge $O$, and the disc has radius $R$. The maximum distance from $O$ along the perimeter is $r_{\\max} = 2R$.\nAt this point:\n- Centrifugal force: $F_{\\text{cf}} = m\\omega^2 (2R)$ (directed radially away from $O$)\n- Coriolis force: $F_{\\text{cor}} = 2m v' \\omega$ (must be directed toward $O$ to cancel $F_{\\text{cf}}$)\n\nSetting the resultant inertial force to zero at $r = 2R$:\n$$m\\omega^2 (2R) - 2m v' \\omega = 0 \\implies v' = \\omega R$$\n\nThe acceleration of the particle relative to the disc is purely centripetal:\n$$w' = \\frac{v'^2}{R} = \\frac{(\\omega R)^2}{R} = \\omega^2 R$$\n\n**(b) Dependence of $F_{\\text{in}}$ on Distance $r$:**\nAt any point on the perimeter at distance $r$ from $O$, by the inscribed angle theorem, the angle between the position vector $\\mathbf{r}$ and the tangent to the circumference is $\\alpha$, where $\\sin\\alpha = \\frac{r}{2R}$.\nVectorially combining centrifugal force $m\\omega^2 \\mathbf{r}$ and Coriolis force $2m(\\mathbf{v}' \\times \\boldsymbol{\\omega})$ of constant magnitude $2m\\omega^2 R$:\n$$F_{\\text{in}} = m\\omega^2 r \\sqrt{1 - \\left(\\frac{r}{2R}\\right)^2}$$",
        "tags": ["dynamics", "rotating frames", "Coriolis force", "centrifugal force"]
    },
    {
        "id": "1.115",
        "title": "Inertial Forces at Break-Off on a Rotating Sphere",
        "difficulty": 2,
        "question": "A small body of mass $m = 0.30\\text{ kg}$ starts sliding down from the top of a smooth sphere of radius $R = 1.00\\text{ m}$. The sphere rotates with a constant angular velocity $\\omega = 6.0\\text{ rad/s}$ about a vertical axis passing through its centre. Find the centrifugal force of inertia and the Coriolis force at the moment when the body breaks off the surface of the sphere in the reference frame fixed to the sphere.",
        "hints": [
            "Use the break-off condition from problem 1.87: break-off occurs at $\\cos\\theta = 2/3$.",
            "Radius of the horizontal circle at break-off is $r = R\\sin\\theta = R\\sqrt{1 - \\cos^2\\theta} = R\\frac{\\sqrt{5}}{3}$.",
            "Calculate $F_{\\text{cf}} = m\\omega^2 r$ and $F_{\\text{cor}} = 2m\\omega v\\cos\\theta$."
        ],
        "answer": "$F_{\\text{cf}} = \\frac{\\sqrt{5}}{3} m\\omega^2 R = 8.0\\text{ N}$; $F_{\\text{cor}} = 2m\\omega \\sqrt{\\frac{2}{3}gR} \\approx 3.1\\text{ N}$",
        "solution": "**1. Geometry at Break-Off:**\nBreak-off from a smooth sphere occurs at polar angle $\\theta$ given by:\n$$\\cos\\theta = \\frac{2}{3} \\implies \\sin\\theta = \\sqrt{1 - \\left(\\frac{2}{3}\\right)^2} = \\frac{\\sqrt{5}}{3}$$\n\nThe distance of the body from the vertical rotation axis is:\n$$r = R\\sin\\theta = R \\frac{\\sqrt{5}}{3}$$\n\n**2. Centrifugal Force:**\n$$F_{\\text{cf}} = m\\omega^2 r = \\frac{\\sqrt{5}}{3} m\\omega^2 R$$\nNumerical calculation:\n$$F_{\\text{cf}} = \\frac{\\sqrt{5}}{3} \\times 0.30 \\times 6.0^2 \\times 1.00 = \\frac{\\sqrt{5}}{3} \\times 0.30 \\times 36 = 3.6\\sqrt{5} \\approx 8.05\\text{ N} \\approx 8.0\\text{ N}$$\n\n**3. Coriolis Force:**\nThe relative velocity at break-off is $v = \\sqrt{\\frac{2}{3}gR}$.\nThe Coriolis force magnitude is:\n$$F_{\\text{cor}} = 2m\\omega v = 2m\\omega \\sqrt{\\frac{2}{3}gR}$$\n$$F_{\\text{cor}} = 2 \\times 0.30 \\times 6.0 \\times \\sqrt{\\frac{2}{3} \\times 9.8 \\times 1.0} = 3.6 \\times \\sqrt{6.533} \\approx 3.6 \\times 2.556 \\approx 9.2\\text{ N}$$",
        "tags": ["dynamics", "rotating frames", "break-off", "Coriolis force"]
    },
    {
        "id": "1.116",
        "title": "Lateral Force on Train Rails Due to Earth's Rotation",
        "difficulty": 2,
        "question": "A train of mass $m = 2000\\text{ tons}$ moves at latitude $\\varphi = 60^{\\circ}$ North. Find:\n(a) the magnitude and direction of the lateral force that the train exerts on the rails if it moves along a meridian with velocity $v = 54\\text{ km/h}$;\n(b) in what direction and with what velocity the train should move for the resultant of the inertial forces acting on the train in the reference frame fixed to the Earth to be equal to zero.",
        "hints": [
            "For (a), the lateral force is the horizontal Coriolis force: $F = 2m\\omega v\\sin\\varphi$.",
            "In the Northern Hemisphere, motion along a meridian experiences Coriolis acceleration to the right (right rail).",
            "For (b), to cancel horizontal centrifugal force $m\\omega^2 R\\cos\\varphi\\sin\\varphi$, the train must move westward so that Coriolis force opposes centrifugal force."
        ],
        "answer": "(a) $F = 2m\\omega v\\sin\\varphi = 3.8\\text{ kN}$ (on the right rail); (b) Westward along the parallel with $v = \\frac{1}{2}\\omega R\\cos\\varphi \\approx 420\\text{ km/h}$",
        "solution": "**(a) Lateral Force on Rails:**\nThe lateral horizontal force is the Coriolis force:\n$$F = 2m\\omega v \\sin\\varphi$$\n\nConvert units to SI:\n- $m = 2000\\text{ tons} = 2.0 \\times 10^6\\text{ kg}$\n- $v = 54\\text{ km/h} = 15\\text{ m/s}$\n- $\\omega = 7.292 \\times 10^{-5}\\text{ rad/s}$\n- $\\varphi = 60^{\\circ} \\implies \\sin 60^{\\circ} = \\frac{\\sqrt{3}}{2} \\approx 0.866$\n\n$$F = 2 \\times (2.0 \\times 10^6) \\times (7.292 \\times 10^{-5}) \\times 15 \\times 0.866$$\n$$F = 4.0 \\times 10^6 \\times 7.292 \\times 10^{-5} \\times 12.99 = 291.68 \\times 12.99 \\approx 3789\\text{ N} \\approx 3.8\\text{ kN}$$\nIn the Northern Hemisphere, the Coriolis acceleration is directed to the right of the velocity vector, so the train presses against the **right rail**.\n\n**(b) Velocity for Zero Net Inertial Force:**\nIn the horizontal plane, the centrifugal force has component $F_{\\text{cf}, h} = m\\omega^2 R \\cos\\varphi \\sin\\varphi$ directed toward the equator (southward).\nWhen the train moves along a parallel of latitude (East-West), the Coriolis force has horizontal component directed along the meridian (North-South):\n$$F_{\\text{cor}, h} = 2m\\omega v' \\sin\\varphi$$\nFor the two horizontal forces to cancel, $F_{\\text{cor}}$ must point northward, which requires moving **westward**:\n$$2m\\omega v' \\sin\\varphi = m\\omega^2 R \\cos\\varphi \\sin\\varphi \\implies v' = \\frac{1}{2}\\omega R \\cos\\varphi$$\n\nWith $R \\approx 6370\\text{ km}$:\n$$v' = \\frac{1}{2} \\times (7.292 \\times 10^{-5}\\text{ rad/s}) \\times (6.37 \\times 10^6\\text{ m}) \\times \\cos 60^{\\circ}$$\n$$v' = \\frac{1}{2} \\times 464.5 \\times 0.5 = 116.1\\text{ m/s} = 116.1 \\times 3.6 \\approx 418\\text{ km/h} \\approx 420\\text{ km/h}$$",
        "tags": ["dynamics", "Coriolis force", "rotating Earth", "centrifugal force"]
    },
    {
        "id": "1.117",
        "title": "Eastward Coriolis Deflection of a Falling Body",
        "difficulty": 2,
        "question": "At the equator, a body initially stationary relative to the Earth falls from a height $h = 500\\text{ m}$. Assuming air drag to be negligible, find how much off the vertical, and in what direction, the body will deviate when it hits the ground.",
        "hints": [
            "As the body falls downward with speed $v(t) = gt$, it experiences a horizontal Coriolis acceleration $w_{\\text{cor}} = 2(\\mathbf{v} \\times \\boldsymbol{\\omega})$.",
            "At the equator, $\\boldsymbol{\\omega}$ points north and $\\mathbf{v}$ points downward, so $\\mathbf{v} \\times \\boldsymbol{\\omega}$ points East.",
            "Integrate $w_{\\text{cor}}(t) = 2\\omega gt$ twice with respect to time over the flight time $t = \\sqrt{2h/g}$."
        ],
        "answer": "$x = \\frac{2}{3}\\omega h \\sqrt{\\frac{2h}{g}} \\approx 24\\text{ cm}$ (to the East)",
        "solution": "**1. Coriolis Acceleration:**\nAt the equator, Earth's angular velocity vector $\\boldsymbol{\\omega}$ points horizontally North.\nThe falling body has downward velocity $\\mathbf{v} = -gt\\hat{\\mathbf{k}}$.\nThe Coriolis acceleration is:\n$$\\mathbf{w}_{\\text{cor}} = 2(\\mathbf{v} \\times \\boldsymbol{\\omega}) = 2(-gt\\hat{\\mathbf{k}} \\times \\omega\\hat{\\mathbf{j}}) = 2\\omega gt \\hat{\\mathbf{i}}$$\nwhere $\\hat{\\mathbf{i}}$ points **East**.\n\n**2. Eastward Deflection:**\nIntegrating the horizontal acceleration twice:\n$$v_x(t) = \\int_0^t 2\\omega g t' \\, dt' = \\omega g t^2$$\n$$x(t) = \\int_0^t \\omega g t'^2 \\, dt' = \\frac{1}{3} \\omega g t^3$$\n\n**3. Substitution of Fall Time:**\nThe total time to fall from height $h$ is $t = \\sqrt{\\frac{2h}{g}}$:\n$$x = \\frac{1}{3}\\omega g \\left(\\sqrt{\\frac{2h}{g}}\\right)^3 = \\frac{1}{3}\\omega g \\cdot \\frac{2h}{g} \\sqrt{\\frac{2h}{g}} = \\frac{2}{3}\\omega h \\sqrt{\\frac{2h}{g}}$$\n\n**4. Numerical Calculation:**\nWith $h = 500\\text{ m}, g = 9.8\\text{ m/s}^2, \\omega = 7.292 \\times 10^{-5}\\text{ rad/s}$:\n$$t = \\sqrt{\\frac{2 \\times 500}{9.8}} = \\sqrt{\\frac{1000}{9.8}} = \\sqrt{102.04} \\approx 10.10\\text{ s}$$\n$$x = \\frac{2}{3} \\times (7.292 \\times 10^{-5}) \\times 500 \\times 10.10$$\n$$x = \\frac{1000}{3} \\times 7.292 \\times 10^{-5} \\times 10.10 = 0.02431 \\times 10.10 \\approx 0.245\\text{ m} \\approx 24\\text{ cm}$$\nThus, the body deviates approximately $24\\text{ cm}$ to the **East**.",
        "tags": ["dynamics", "Coriolis force", "free fall", "rotating Earth"]
    }
]
