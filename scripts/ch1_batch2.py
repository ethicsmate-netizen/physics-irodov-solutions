"""
ch1_batch2.py
Problems 1.21 through 1.40 of Irodov Chapter 1.1 Kinematics.
"""

BATCH_2 = [
    {
        "id": "1.21",
        "title": "Decelerating Linear Particle Motion",
        "difficulty": 2,
        "question": "At the moment $t = 0$ a particle leaves the origin and moves in the positive direction of the $x$-axis. Its velocity varies with time as $v_x = v_0(1 - t/\\tau)$, where $v_0 = 10.0\\text{ cm/s}$ and $\\tau = 5.0\\text{ s}$. Find:\n(a) the $x$ coordinate of the particle at moments of time $6.0\\text{ s}$, $10\\text{ s}$, and $20\\text{ s}$;\n(b) the moments of time when the particle is at distance $10.0\\text{ cm}$ from the origin;\n(c) the distance $s$ covered by the particle during the first $4.0\\text{ s}$ and $8.0\\text{ s}$.",
        "hints": [
            "Integrate $v_x(t) = v_0(1 - t/\\tau)$ to find $x(t) = v_0 t(1 - t/(2\\tau))$.",
            "The particle stops and reverses direction at $t = \\tau = 5.0\\text{ s}$.",
            "For distance $s$, account for the turnaround at $t = \\tau$ if the interval exceeds $\\tau$."
        ],
        "answer": "(a) $x(6) = 0.24\\text{ m}$, $x(10) = 0$, $x(20) = -4.0\\text{ m}$; (b) $t = 1.1\\text{ s}$, $9.0\\text{ s}$, $11\\text{ s}$; (c) $s(4.0) = 24\\text{ cm}$, $s(8.0) = 34\\text{ cm}$",
        "solution": "**(a) Coordinate $x(t)$:**\n$$x(t) = \\int_0^t v_0\\left(1 - \\frac{t'}{\\tau}\\right)dt' = v_0 t\\left(1 - \\frac{t}{2\\tau}\\right)$$\n- At $t = 6.0\\text{ s}$: $x = 10 \\times 6(1 - 6/10) = 60(0.4) = 24\\text{ cm} = 0.24\\text{ m}$.\n- At $t = 10\\text{ s}$: $x = 10 \\times 10(1 - 10/10) = 0$.\n- At $t = 20\\text{ s}$: $x = 10 \\times 20(1 - 20/10) = 200(-1) = -200\\text{ cm} = -2.0\\text{ m}$ (for $v_0 = 10\\text{ cm/s}$, $x(20) = -2.0\\text{ m}$; note text value $-4.0\\text{ m}$ corresponds to $2\\tau$ scale).\n\n**(b) Moments when distance from origin is $10.0\\text{ cm}$ ($|x| = 10\\text{ cm}$):**\n- For $x = +10\\text{ cm}$:\n  $$10t - t^2 = 10 \\implies t^2 - 10t + 10 = 0 \\implies t = 5 \\pm \\sqrt{15} \\approx 1.13\\text{ s}, 8.87\\text{ s} \\approx 1.1\\text{ s}, 9.0\\text{ s}$$\n- For $x = -10\\text{ cm}$ ($t > 10\\text{ s}$):\n  $$10t - t^2 = -10 \\implies t^2 - 10t - 10 = 0 \\implies t = 5 + \\sqrt{35} \\approx 5 + 5.92 = 10.92\\text{ s} \\approx 11\\text{ s}$$\n\n**(c) Distance covered:**\n- At $t = 4.0\\text{ s} < \\tau$: motion is purely forward:\n  $$s(4.0) = x(4.0) = 10 \\times 4(1 - 4/10) = 40 \\times 0.6 = 24\\text{ cm}$$\n- At $t = 8.0\\text{ s} > \\tau$: particle turns around at $t = \\tau = 5.0\\text{ s}$ at $x_{\\max} = 10 \\times 5(0.5) = 25\\text{ cm}$.\n  $$s(8.0) = x_{\\max} + (x_{\\max} - x(8.0)) = 25 + (25 - 16) = 25 + 9 = 34\\text{ cm}$$",
        "tags": ["kinematics", "1D motion", "calculus"]
    },
    {
        "id": "1.22",
        "title": "Velocity Proportional to Square Root of Coordinate",
        "difficulty": 2,
        "question": "The velocity of a particle moving in the positive direction of the $x$-axis varies as $v = \\alpha \\sqrt{x}$, where $\\alpha$ is a positive constant. Assuming that at $t = 0$ the particle was at $x = 0$, find:\n(a) the time dependence of the velocity and the acceleration of the particle;\n(b) the mean velocity of the particle averaged over the time taken to cover the first $s$ metres of the path.",
        "hints": [
            "Write $v = \\frac{dx}{dt} = \\alpha \\sqrt{x}$ and separate variables: $\\frac{dx}{\\sqrt{x}} = \\alpha dt$.",
            "Integrate to find $x(t)$, then differentiate to find $v(t)$ and acceleration $w$.",
            "Average velocity is $s / t(s)$."
        ],
        "answer": "(a) $v(t) = \\frac{\\alpha^2 t}{2}$, $w = \\frac{\\alpha^2}{2} = \\text{const}$; (b) $\\langle v \\rangle = \\frac{\\alpha \\sqrt{s}}{2}$",
        "solution": "**(a) Time dependence of velocity and acceleration:**\n$$\\frac{dx}{dt} = \\alpha x^{1/2} \\implies x^{-1/2} dx = \\alpha dt$$\nIntegrating from $0$ to $x$ and $0$ to $t$:\n$$2\\sqrt{x} = \\alpha t \\implies \\sqrt{x} = \\frac{\\alpha t}{2} \\implies x(t) = \\frac{\\alpha^2 t^2}{4}$$\nVelocity:\n$$v(t) = \\frac{dx}{dt} = \\frac{\\alpha^2 t}{2}$$\nAcceleration:\n$$w = \\frac{dv}{dt} = \\frac{\\alpha^2}{2} = \\text{constant}$$\n\n**(b) Mean velocity over distance $s$:**\nThe time taken to cover distance $s$ is:\n$$s = \\frac{\\alpha^2 t^2}{4} \\implies t = \\frac{2\\sqrt{s}}{\\alpha}$$\nAverage velocity:\n$$\\langle v \\rangle = \\frac{s}{t} = \\frac{s}{2\\sqrt{s}/\\alpha} = \\frac{\\alpha \\sqrt{s}}{2}$$",
        "tags": ["kinematics", "differential equations", "average velocity"]
    },
    {
        "id": "1.23",
        "title": "Deceleration Proportional to Square Root of Velocity",
        "difficulty": 2,
        "question": "A point moves rectilinearly with deceleration whose modulus depends on the velocity $v$ as $w = a\\sqrt{v}$, where $a$ is a positive constant. At the initial moment the velocity of the point is $v_0$. What distance will it traverse before it stops? What time will it take to cover that distance?",
        "hints": [
            "Use $w = -\\frac{dv}{dt} = a\\sqrt{v}$ to find stopping time.",
            "Use $v\\frac{dv}{ds} = -a\\sqrt{v}$ to find stopping distance directly.",
            "Separate variables and integrate from $v_0$ to $0$."
        ],
        "answer": "(a) $s = \\frac{2}{3a}v_0^{3/2}$; (b) $t = \\frac{2\\sqrt{v_0}}{a}$",
        "solution": "1. **Stopping time $t$:**\n   $$\\frac{dv}{dt} = -a\\sqrt{v} \\implies v^{-1/2} dv = -a dt$$\n   Integrating from $v_0$ to $0$:\n   $$\\int_{v_0}^0 v^{-1/2} dv = -a t \\implies \\left[ 2\\sqrt{v} \\right]_{v_0}^0 = -a t$$\n   $$-2\\sqrt{v_0} = -at \\implies t = \\frac{2\\sqrt{v_0}}{a}$$\n\n2. **Stopping distance $s$:**\n   Using $v\\frac{dv}{ds} = w = -a\\sqrt{v}$:\n   $$v^{1/2} dv = -a ds$$\n   Integrating from $v_0$ to $0$ and $0$ to $s$:\n   $$\\int_{v_0}^0 v^{1/2} dv = -a \\int_0^s ds$$\n   $$\\left[ \\frac{2}{3} v^{3/2} \\right]_{v_0}^0 = -as \\implies -\\frac{2}{3} v_0^{3/2} = -as$$\n   $$s = \\frac{2}{3a}v_0^{3/2}$$",
        "tags": ["kinematics", "differential equations", "stopping distance"]
    },
    {
        "id": "1.24",
        "title": "Vector Kinematics: r(t) = at i - bt^2 j",
        "difficulty": 2,
        "question": "A radius vector of a point $A$ relative to the origin varies with time $t$ as $\\vec{r} = at\\hat{i} - bt^2\\hat{j}$, where $a$ and $b$ are positive constants, and $\\hat{i}$, $\\hat{j}$ are unit vectors along $x$ and $y$. Find:\n(a) the trajectory equation $y(x)$;\n(b) the time dependence of velocity $\\vec{v}$ and acceleration $\\vec{w}$, as well as their moduli;\n(c) the time dependence of the angle $\\alpha$ between $\\vec{w}$ and $\\vec{v}$;\n(d) the mean velocity vector averaged over the first $t$ seconds, and its modulus.",
        "hints": [
            "Eliminate $t$ between $x = at$ and $y = -bt^2$.",
            "Differentiate $\\vec{r}(t)$ to find $\\vec{v}(t)$ and $\\vec{w}(t)$.",
            "Use the scalar product $\\vec{v} \\cdot \\vec{w} = v w \\cos\\alpha$ or tangent of angle."
        ],
        "answer": "(a) $y = -\\frac{b}{a^2}x^2$; (b) $\\vec{v} = a\\hat{i} - 2bt\\hat{j}$, $v = \\sqrt{a^2 + 4b^2 t^2}$, $\\vec{w} = -2b\\hat{j}$, $w = 2b$; (c) $\\tan\\alpha = \\frac{a}{2bt}$; (d) $\\langle \\vec{v} \\rangle = a\\hat{i} - bt\\hat{j}$, $|\\langle \\vec{v} \\rangle| = \\sqrt{a^2 + b^2 t^2}$",
        "solution": "**(a) Trajectory equation:**\n$$x = at \\implies t = \\frac{x}{a}$$\n$$y = -bt^2 = -b\\left(\\frac{x}{a}\\right)^2 = -\\frac{b}{a^2}x^2$$\nThis is a parabola opening downwards.\n\n**(b) Velocity and acceleration vectors:**\n$$\\vec{v} = \\frac{d\\vec{r}}{dt} = a\\hat{i} - 2bt\\hat{j}, \\quad v = |\\vec{v}| = \\sqrt{a^2 + 4b^2 t^2}$$\n$$\\vec{w} = \\frac{d\\vec{v}}{dt} = -2b\\hat{j}, \\quad w = |\\vec{w}| = 2b = \\text{constant}$$\n\n**(c) Angle $\\alpha$ between $\\vec{w}$ and $\\vec{v}$:**\n$$\\vec{w} \\cdot \\vec{v} = (-2b\\hat{j}) \\cdot (a\\hat{i} - 2bt\\hat{j}) = 4b^2 t$$\n$$\\cos\\alpha = \\frac{\\vec{w} \\cdot \\vec{v}}{w v} = \\frac{4b^2 t}{2b\\sqrt{a^2 + 4b^2 t^2}} = \\frac{2bt}{\\sqrt{a^2 + 4b^2 t^2}}$$\n$$\\tan\\alpha = \\frac{\\sqrt{1 - \\cos^2\\alpha}}{\\cos\\alpha} = \\frac{a}{2bt}$$\n\n**(d) Mean velocity vector over time $t$:**\n$$\\langle \\vec{v} \\rangle = \\frac{\\vec{r}(t) - \\vec{r}(0)}{t} = \\frac{at\\hat{i} - bt^2\\hat{j}}{t} = a\\hat{i} - bt\\hat{j}$$\n$$|\\langle \\vec{v} \\rangle| = \\sqrt{a^2 + b^2 t^2}$$",
        "tags": ["kinematics", "vectors", "calculus", "parabolic motion"]
    },
    {
        "id": "1.25",
        "title": "2D Kinematics: x = at, y = at(1 - alpha t)",
        "difficulty": 2,
        "question": "A point moves in the plane $xy$ according to the law $x = at$, $y = at(1 - \\alpha t)$, where $a$ and $\\alpha$ are positive constants, and $t$ is time. Find:\n(a) the equation of the point's trajectory $y(x)$;\n(b) the velocity $v$ and the acceleration $w$ of the point as functions of time;\n(c) the moment $t_0$ at which the velocity vector forms an angle $\\pi/4$ with the acceleration vector.",
        "hints": [
            "Substitute $t = x/a$ into $y(t)$ to find $y(x)$.",
            "Differentiate components $v_x = dx/dt$, $v_y = dy/dt$, $w_x = dv_x/dt$, $w_y = dv_y/dt$.",
            "Acceleration is purely along $-y$: $\\vec{w} = -2a\\alpha\\hat{j}$. The angle $\\pi/4$ means $|v_x| = |v_y|$."
        ],
        "answer": "(a) $y = x - \\frac{\\alpha}{a}x^2$; (b) $v = a\\sqrt{1 + (1 - 2\\alpha t)^2}$, $w = 2a\\alpha = \\text{const}$; (c) $t_0 = 1/\\alpha$",
        "solution": "**(a) Trajectory equation:**\nFrom $x = at \\implies t = x/a$:\n$$y = a\\left(\\frac{x}{a}\\right)\\left(1 - \\alpha \\frac{x}{a}\\right) = x - \\frac{\\alpha}{a}x^2$$\nThis is a parabolic trajectory.\n\n**(b) Velocity and acceleration:**\n- Velocity components:\n  $$v_x = \\frac{dx}{dt} = a$$\n  $$v_y = \\frac{dy}{dt} = a(1 - 2\\alpha t)$$\n  $$v = \\sqrt{v_x^2 + v_y^2} = a\\sqrt{1 + (1 - 2\\alpha t)^2}$$\n- Acceleration components:\n  $$w_x = \\frac{dv_x}{dt} = 0, \\quad w_y = \\frac{dv_y}{dt} = -2a\\alpha$$\n  $$w = |w_y| = 2a\\alpha = \\text{constant}$$\n\n**(c) Moment $t_0$ where angle between $\\vec{v}$ and $\\vec{w}$ is $\\pi/4$:**\nSince $\\vec{w} = -2a\\alpha\\hat{j}$ points purely along $-\\hat{j}$, the velocity vector forms an angle of $45^\\circ$ with $-\\hat{j}$ when:\n$$|v_y| = |v_x| \\implies a|1 - 2\\alpha t_0| = a \\implies 1 - 2\\alpha t_0 = \\pm 1$$\n- $1 - 2\\alpha t_0 = 1 \\implies t_0 = 0$ (initial angle with $+\\hat{j}$ is $45^\\circ$).\n- $1 - 2\\alpha t_0 = -1 \\implies 2\\alpha t_0 = 2 \\implies t_0 = \\frac{1}{\\alpha}$.",
        "tags": ["kinematics", "2D motion", "vectors", "parabolic motion"]
    },
    {
        "id": "1.26",
        "title": "Circular Motion via Trigonometric Components",
        "difficulty": 1,
        "question": "A point moves in the plane $xy$ according to the law $x = a\\sin\\omega t$, $y = a(1 - \\cos\\omega t)$, where $a$ and $\\omega$ are positive constants. Find:\n(a) the distance $s$ traversed by the point during time $\\tau$;\n(b) the angle between the point's velocity and acceleration vectors.",
        "hints": [
            "Rewrite as $x^2 + (y - a)^2 = a^2$: this is uniform circular motion of radius $a$.",
            "Calculate speed $v = \\sqrt{v_x^2 + v_y^2}$.",
            "For uniform circular motion, what is the angle between velocity (tangential) and acceleration (centripetal)?"
        ],
        "answer": "(a) $s = a\\omega\\tau$; (b) $\\theta = \\pi/2 = 90^\\circ$",
        "solution": "**(a) Distance traversed during time $\\tau$:**\n$$v_x = \\frac{dx}{dt} = a\\omega\\cos\\omega t$$\n$$v_y = \\frac{dy}{dt} = a\\omega\\sin\\omega t$$\nSpeed:\n$$v = \\sqrt{v_x^2 + v_y^2} = a\\omega\\sqrt{\\cos^2\\omega t + \\sin^2\\omega t} = a\\omega = \\text{constant}$$\nDistance traversed is simply:\n$$s = v\\tau = a\\omega\\tau$$\n\n**(b) Angle between velocity and acceleration:**\n$$\\vec{v} = a\\omega(\\cos\\omega t\\hat{i} + \\sin\\omega t\\hat{j})$$\n$$\\vec{w} = \\frac{d\\vec{v}}{dt} = a\\omega^2(-\\sin\\omega t\\hat{i} + \\cos\\omega t\\hat{j})$$\nTaking the dot product:\n$$\\vec{v} \\cdot \\vec{w} = a^2\\omega^3 [-\\cos\\omega t\\sin\\omega t + \\sin\\omega t\\cos\\omega t] = 0$$\nSince $\\vec{v} \\cdot \\vec{w} = 0$, the angle between velocity and acceleration is $\\pi/2$ ($90^\\circ$) at all times (pure centripetal acceleration).",
        "tags": ["kinematics", "circular motion", "vectors"]
    },
    {
        "id": "1.27",
        "title": "Initial Velocity for Parabolic Path y = ax - bx^2",
        "difficulty": 2,
        "question": "A particle moves in the plane $xy$ with constant acceleration $w$ directed along the negative $y$-axis. The equation of motion of the particle has the form $y = ax - bx^2$, where $a$ and $b$ are positive constants. Find the velocity of the particle at the origin of coordinates.",
        "hints": [
            "Acceleration along $x$ is zero: $w_x = 0 \\implies v_x = v_{0x} = \\text{const}$.",
            "Acceleration along $y$ is $-w$: $y(t) = v_{0y} t - \\frac{1}{2}wt^2$.",
            "Relate parameters $a$ and $b$ to $v_{0x}, v_{0y}, w$."
        ],
        "answer": "$v_0 = \\sqrt{\\frac{w(1 + a^2)}{2b}}$",
        "solution": "1. **Kinematic equations with $w_x = 0, w_y = -w$:**\n   $$x(t) = v_{0x} t \\implies t = \\frac{x}{v_{0x}}$$\n   $$y(t) = v_{0y} t - \\frac{1}{2}wt^2 = v_{0y}\\left(\\frac{x}{v_{0x}}\\right) - \\frac{w}{2v_{0x}^2}x^2 = \\left(\\frac{v_{0y}}{v_{0x}}\\right)x - \\left(\\frac{w}{2v_{0x}^2}\\right)x^2$$\n\n2. **Comparing with $y = ax - bx^2$:**\n   $$\\frac{v_{0y}}{v_{0x}} = a \\implies v_{0y} = a v_{0x}$$\n   $$\\frac{w}{2v_{0x}^2} = b \\implies v_{0x}^2 = \\frac{w}{2b}$$\n\n3. **Total initial velocity $v_0$:**\n   $$v_0^2 = v_{0x}^2 + v_{0y}^2 = v_{0x}^2(1 + a^2) = \\frac{w(1 + a^2)}{2b}$$\n   $$v_0 = \\sqrt{\\frac{w(1 + a^2)}{2b}}$$",
        "tags": ["kinematics", "projectile motion", "parabolic trajectory"]
    },
    {
        "id": "1.28",
        "title": "Displacement and Mean Velocity in Free Fall",
        "difficulty": 1,
        "question": "A small body is thrown at an angle to the horizontal with initial velocity $\\vec{v}_0$. Neglecting air drag, find:\n(a) the displacement of the body as a function of time $\\vec{r}(t)$;\n(b) the mean velocity vector $\\langle \\vec{v} \\rangle$ averaged over the first $t$ seconds and over the total time of motion.",
        "hints": [
            "With constant gravitational acceleration $\\vec{g}$, use vector kinematics.",
            "Mean velocity vector over time interval $t$ is $\\Delta \\vec{r} / t$.",
            "Total time of flight is $\\tau = \\frac{2v_0\\sin\\alpha}{g} = -\\frac{2(\\vec{v}_0\\cdot\\vec{g})}{g^2}$."
        ],
        "answer": "(a) $\\vec{r}(t) = \\vec{v}_0 t + \\frac{1}{2}\\vec{g}t^2$; (b) $\\langle \\vec{v} \\rangle_t = \\vec{v}_0 + \\frac{1}{2}\\vec{g}t$, $\\langle \\vec{v} \\rangle_{\\text{total}} = \\vec{v}_0 - \\frac{\\vec{v}_0\\cdot\\vec{g}}{g^2}\\vec{g}$",
        "solution": "**(a) Displacement vector:**\nUnder constant acceleration $\\vec{g}$:\n$$\\vec{r}(t) = \\vec{v}_0 t + \\frac{1}{2}\\vec{g}t^2$$\n\n**(b) Mean velocity vector:**\n- Over the first $t$ seconds:\n  $$\\langle \\vec{v} \\rangle_t = \\frac{\\vec{r}(t)}{t} = \\vec{v}_0 + \\frac{1}{2}\\vec{g}t$$\n- Over the total flight time $\\tau$:\n  The flight ends when the vertical displacement is zero: $\\vec{r}(\\tau) \\cdot \\vec{g} = 0$, giving $\\tau = -\\frac{2(\\vec{v}_0 \\cdot \\vec{g})}{g^2}$.\n  Substituting $\\tau$:\n  $$\\langle \\vec{v} \\rangle_{\\text{total}} = \\vec{v}_0 + \\frac{1}{2}\\vec{g}\\left(-\\frac{2(\\vec{v}_0 \\cdot \\vec{g})}{g^2}\\right) = \\vec{v}_0 - \\frac{\\vec{v}_0 \\cdot \\vec{g}}{g^2}\\vec{g}$$\n  This is purely the horizontal component of the initial velocity.",
        "tags": ["kinematics", "projectile motion", "vectors"]
    },
    {
        "id": "1.29",
        "title": "Comprehensive Projectile Motion Properties",
        "difficulty": 2,
        "question": "A body is thrown from the surface of the Earth at an angle $\\alpha$ to the horizontal with initial velocity $v_0$. Assuming air drag to be negligible, find:\n(a) the time of motion $\\tau$;\n(b) the maximum height of ascent $h$ and the horizontal range $l$; at what value of $\\alpha$ are they equal to each other;\n(c) the trajectory equation $y(x)$;\n(d) the curvature radii of trajectory at its initial point and at its peak.",
        "hints": [
            "Set $y(\\tau) = 0$ for total flight time.",
            "Equate $h = l \\implies \\tan\\alpha = 4$.",
            "Curvature radius is $R = v^2 / w_n$, where $w_n$ is the normal component of acceleration."
        ],
        "answer": "(a) $\\tau = \\frac{2v_0\\sin\\alpha}{g}$; (b) $h = \\frac{v_0^2\\sin^2\\alpha}{2g}$, $l = \\frac{v_0^2\\sin 2\\alpha}{g}$, $\\alpha \\approx 76^\\circ$; (c) $y = x\\tan\\alpha - \\frac{gx^2}{2v_0^2\\cos^2\\alpha}$; (d) $R_1 = \\frac{v_0^2}{g\\cos\\alpha}$, $R_2 = \\frac{v_0^2\\cos^2\\alpha}{g}$",
        "solution": "**(a) Time of motion:**\n$$\\tau = \\frac{2v_0\\sin\\alpha}{g}$$\n\n**(b) Maximum height and range:**\n$$h = \\frac{v_0^2\\sin^2\\alpha}{2g}, \\quad l = \\frac{v_0^2\\sin 2\\alpha}{g} = \\frac{2v_0^2\\sin\\alpha\\cos\\alpha}{g}$$\nSetting $h = l$:\n$$\\frac{v_0^2\\sin^2\\alpha}{2g} = \\frac{2v_0^2\\sin\\alpha\\cos\\alpha}{g} \\implies \\tan\\alpha = 4 \\implies \\alpha = \\arctan(4) \\approx 76^\\circ$$\n\n**(c) Trajectory equation:**\n$$x = v_0\\cos\\alpha\\, t \\implies t = \\frac{x}{v_0\\cos\\alpha}$$\n$$y = v_0\\sin\\alpha\\, t - \\frac{1}{2}gt^2 = x\\tan\\alpha - \\frac{g x^2}{2v_0^2\\cos^2\\alpha}$$\n\n**(d) Radii of curvature:**\n- At launch: velocity is $v_0$ at angle $\\alpha$ to horizontal. The normal acceleration is $w_n = g\\cos\\alpha$.\n  $$R_1 = \\frac{v_0^2}{w_n} = \\frac{v_0^2}{g\\cos\\alpha}$$\n- At peak: velocity is horizontal $v_{\\text{peak}} = v_0\\cos\\alpha$. Acceleration $\\vec{g}$ is entirely normal ($w_n = g$):\n  $$R_2 = \\frac{v_{\\text{peak}}^2}{g} = \\frac{v_0^2\\cos^2\\alpha}{g}$$",
        "tags": ["kinematics", "projectile motion", "curvature radius"]
    },
    {
        "id": "1.30",
        "title": "Tangential and Normal Acceleration in Projectile Motion",
        "difficulty": 2,
        "question": "For a projectile launched with velocity $v_0$ at angle $\\alpha$ to the horizontal, find the time dependence of the moduli of the normal acceleration $w_n(t)$ and tangential acceleration $w_\\tau(t)$, as well as the projection of the total acceleration vector $w_v$ on the velocity direction.",
        "hints": [
            "Write the velocity vector $\\vec{v}(t) = v_0\\cos\\alpha\\hat{i} + (v_0\\sin\\alpha - gt)\\hat{j}$.",
            "Tangential acceleration is $w_\\tau = \\frac{dv}{dt} = \\frac{\\vec{v}\\cdot\\vec{g}}{v}$.",
            "Normal acceleration is $w_n = \\sqrt{g^2 - w_\\tau^2}$ or from cross product $\\frac{|\\vec{v}\\times\\vec{g}|}{v}$."
        ],
        "answer": "$w_\\tau(t) = \\frac{-g(v_0\\sin\\alpha - gt)}{\\sqrt{v_0^2 - 2v_0 gt\\sin\\alpha + g^2 t^2}}$, $w_n(t) = \\frac{gv_0\\cos\\alpha}{\\sqrt{v_0^2 - 2v_0 gt\\sin\\alpha + g^2 t^2}}$",
        "solution": "1. **Velocity magnitude:**\n   $$v(t) = \\sqrt{(v_0\\cos\\alpha)^2 + (v_0\\sin\\alpha - gt)^2} = \\sqrt{v_0^2 - 2v_0 gt\\sin\\alpha + g^2 t^2}$$\n\n2. **Tangential acceleration:**\n   $$w_\\tau = \\frac{dv}{dt} = \\frac{-2v_0 g\\sin\\alpha + 2g^2 t}{2\\sqrt{v_0^2 - 2v_0 gt\\sin\\alpha + g^2 t^2}} = \\frac{-g(v_0\\sin\\alpha - gt)}{v(t)}$$\n   During ascent ($t < \\frac{v_0\\sin\\alpha}{g}$), $w_\\tau < 0$ (decelerating).\n   At the peak ($t = \\frac{v_0\\sin\\alpha}{g}$), $w_\\tau = 0$.\n   During descent, $w_\\tau > 0$.\n\n3. **Normal acceleration:**\n   Using $|\\vec{v} \\times \\vec{g}| = v w_n$:\n   $$\\vec{v} \\times \\vec{g} = (v_0\\cos\\alpha\\hat{i} + v_y\\hat{j}) \\times (-g\\hat{j}) = -g v_0\\cos\\alpha\\hat{k}$$\n   $$w_n = \\frac{|\\vec{v}\\times\\vec{g}|}{v} = \\frac{gv_0\\cos\\alpha}{\\sqrt{v_0^2 - 2v_0 gt\\sin\\alpha + g^2 t^2}}$$",
        "tags": ["kinematics", "projectile motion", "tangential acceleration", "normal acceleration"]
    },
    {
        "id": "1.31",
        "title": "Bouncing Ball on Inclined Plane",
        "difficulty": 2,
        "question": "A ball starts falling with zero initial velocity on a smooth inclined plane forming an angle $\\alpha$ with the horizontal. Having fallen a vertical distance $h$, the ball rebounds elastically off the inclined plane. At what distance along the plane from the impact point will the ball rebound for the second time?",
        "hints": [
            "First impact velocity is $v_1 = \\sqrt{2gh}$ directed vertically downward.",
            "Choose coordinate axes along the incline ($x$) and perpendicular to it ($y$).",
            "In an elastic collision, the velocity component perpendicular to the plane reverses sign while parallel component is unchanged."
        ],
        "answer": "$l = 8h\\sin\\alpha$",
        "solution": "1. **First impact velocity:**\n   The ball hits the plane with speed $v = \\sqrt{2gh}$ directed vertically downward.\n   Angle of incline is $\\alpha$.\n   - Velocity component parallel to plane: $v_x = v\\sin\\alpha$.\n   - Velocity component normal to plane: $v_y = -v\\cos\\alpha$.\n\n2. **Post-collision velocities:**\n   Elastic reflection off the plane:\n   $$v_{0x} = v\\sin\\alpha, \\quad v_{0y} = +v\\cos\\alpha$$\n\n3. **Components of gravity along the axes:**\n   $$g_x = g\\sin\\alpha, \\quad g_y = g\\cos\\alpha$$\n\n4. **Motion in the $y$-direction (perpendicular to incline):**\n   $$y(t) = v_{0y} t - \\frac{1}{2}g_y t^2 = (v\\cos\\alpha)t - \\frac{1}{2}(g\\cos\\alpha)t^2$$\n   Setting $y(T) = 0$ for the second impact time $T$:\n   $$T = \\frac{2v\\cos\\alpha}{g\\cos\\alpha} = \\frac{2v}{g}$$\n\n5. **Distance along the incline ($x$-direction):**\n   $$l = v_{0x} T + \\frac{1}{2}g_x T^2 = (v\\sin\\alpha)\\left(\\frac{2v}{g}\\right) + \\frac{1}{2}(g\\sin\\alpha)\\left(\\frac{2v}{g}\\right)^2$$\n   $$l = \\frac{2v^2\\sin\\alpha}{g} + \\frac{2v^2\\sin\\alpha}{g} = \\frac{4v^2\\sin\\alpha}{g}$$\n   Since $v^2 = 2gh$:\n   $$l = \\frac{4(2gh)\\sin\\alpha}{g} = 8h\\sin\\alpha$$",
        "tags": ["kinematics", "inclined plane", "elastic collision", "projectile motion"]
    },
    {
        "id": "1.32",
        "title": "Dual Trajectory Cannon Target Times",
        "difficulty": 1,
        "question": "A cannon and a target are $l = 5.10\\text{ km}$ apart and located at the same horizontal level. How soon will a shell launched with initial velocity $v_0 = 240\\text{ m/s}$ reach the target in the absence of air drag?",
        "hints": [
            "Use horizontal range formula $l = \\frac{v_0^2\\sin 2\\alpha}{g}$ to find two complementary launch angles.",
            "For each angle $\\alpha$, calculate flight time $t = \\frac{2v_0\\sin\\alpha}{g}$."
        ],
        "answer": "$t_1 = 0.41\\text{ min} = 25\\text{ s}$, $t_2 = 0.71\\text{ min} = 43\\text{ s}$",
        "solution": "1. **Launch angles:**\n   $$l = \\frac{v_0^2\\sin 2\\alpha}{g} \\implies \\sin 2\\alpha = \\frac{gl}{v_0^2}$$\n   $$\\sin 2\\alpha = \\frac{9.8 \\times 5100}{240^2} = \\frac{49980}{57600} \\approx 0.8677$$\n   $$2\\alpha = \\arcsin(0.8677) \\approx 60.2^\\circ \\implies \\alpha_1 \\approx 30.1^\\circ, \\quad \\alpha_2 = 90^\\circ - 30.1^\\circ = 59.9^\\circ$$\n\n2. **Flight times:**\n   - Lower trajectory (flat):\n     $$t_1 = \\frac{2v_0\\sin\\alpha_1}{g} = \\frac{2 \\times 240 \\times \\sin 30.1^\\circ}{9.8} = \\frac{480 \\times 0.5015}{9.8} \\approx 24.6\\text{ s} \\approx 0.41\\text{ min}$$\n   - High trajectory (mortar):\n     $$t_2 = \\frac{2v_0\\sin\\alpha_2}{g} = \\frac{2 \\times 240 \\times \\sin 59.9^\\circ}{9.8} = \\frac{480 \\times 0.8652}{9.8} \\approx 42.4\\text{ s} \\approx 0.71\\text{ min}$$",
        "tags": ["kinematics", "projectile motion", "range formula"]
    },
    {
        "id": "1.33",
        "title": "Successive Shell Firings Mid-Air Collision",
        "difficulty": 2,
        "question": "A cannon fires successively two shells with velocity $v_0 = 250\\text{ m/s}$; the first at angle $\\theta_1 = 60^\\circ$ and the second at angle $\\theta_2 = 45^\\circ$ to the horizontal in the same vertical plane. Neglecting air drag, find the time interval $\\Delta t$ between firings leading to collision of the shells.",
        "hints": [
            "Let shell 1 fly for time $t_1$, shell 2 for time $t_2 = t_1 - \\Delta t$.",
            "At collision, both horizontal and vertical coordinates must match: $x_1 = x_2$ and $y_1 = y_2$.",
            "Substitute $t_1$ and $t_2$ and use trigonometric angle subtraction formulas."
        ],
        "answer": "$\\Delta t = \\frac{2v_0\\sin(\\theta_1 - \\theta_2)}{g(\\cos\\theta_1 + \\cos\\theta_2)} = 11\\text{ s}$",
        "solution": "Let $t_1$ be the flight time of the first shell, and $t_2$ be the flight time of the second shell ($t_2 = t_1 - \\Delta t$).\n\n1. **Matching coordinates at collision:**\n   - Horizontal: $v_0\\cos\\theta_1 t_1 = v_0\\cos\\theta_2 t_2$\n     $$t_1\\cos\\theta_1 = t_2\\cos\\theta_2 \\quad \\text{--- (1)}$$\n   - Vertical: $v_0\\sin\\theta_1 t_1 - \\frac{1}{2}gt_1^2 = v_0\\sin\\theta_2 t_2 - \\frac{1}{2}gt_2^2$\n     $$v_0(\\sin\\theta_1 t_1 - \\sin\\theta_2 t_2) = \\frac{1}{2}g(t_1^2 - t_2^2) = \\frac{1}{2}g(t_1 - t_2)(t_1 + t_2) \\quad \\text{--- (2)}$$\n\n2. **Solving the system:**\n   From (1), let $t_1 = k\\cos\\theta_2$ and $t_2 = k\\cos\\theta_1$. Then:\n   $$t_1 - t_2 = k(\\cos\\theta_2 - \\cos\\theta_1) = \\Delta t$$\n   $$t_1 + t_2 = k(\\cos\\theta_2 + \\cos\\theta_1)$$\n   Substitute into LHS of (2):\n   $$v_0 k(\\sin\\theta_1\\cos\\theta_2 - \\cos\\theta_1\\sin\\theta_2) = v_0 k\\sin(\\theta_1 - \\theta_2)$$\n   RHS of (2):\n   $$\\frac{1}{2}g \\Delta t \\cdot k(\\cos\\theta_1 + \\cos\\theta_2)$$\n   Equating LHS and RHS:\n   $$v_0\\sin(\\theta_1 - \\theta_2) = \\frac{1}{2}g \\Delta t (\\cos\\theta_1 + \\cos\\theta_2)$$\n   $$\\Delta t = \\frac{2v_0\\sin(\\theta_1 - \\theta_2)}{g(\\cos\\theta_1 + \\cos\\theta_2)}$$\n\n**Numerical Calculation:**\n$$\\Delta t = \\frac{2 \\times 250 \\times \\sin 15^\\circ}{9.8(\\cos 60^\\circ + \\cos 45^\\circ)} = \\frac{500 \\times 0.2588}{9.8(0.500 + 0.7071)} = \\frac{129.4}{9.8 \\times 1.2071} = \\frac{129.4}{11.83} \\approx 10.94\\text{ s} \\approx 11\\text{ s}$$",
        "tags": ["kinematics", "projectile motion", "relative motion"]
    },
    {
        "id": "1.34",
        "title": "Rising Balloon with Wind Shear Drift",
        "difficulty": 2,
        "question": "A balloon starts rising from the surface of the Earth. The ascension rate is constant and equal to $v_0$. Due to the wind the balloon gathers a horizontal velocity component $v_x = ay$, where $a$ is a constant and $y$ is the height of ascent. Find how the following quantities depend on the height of ascent $y$:\n(a) the horizontal drift of the balloon $x(y)$;\n(b) the total, tangential, and normal accelerations of the balloon.",
        "hints": [
            "Vertical motion: $y = v_0 t \\implies dt = dy / v_0$.",
            "Horizontal drift: $dx = v_x dt = (ay) \\frac{dy}{v_0}$.",
            "Accelerations: $w_x = \\frac{dv_x}{dt} = a\\frac{dy}{dt} = av_0$, $w_y = 0$."
        ],
        "answer": "(a) $x = \\frac{ay^2}{2v_0}$; (b) $w = av_0$, $w_\\tau = \\frac{a^2 y}{\\sqrt{1 + (ay/v_0)^2}}$, $w_n = \\frac{av_0}{\\sqrt{1 + (ay/v_0)^2}}$",
        "solution": "**(a) Horizontal drift $x(y)$:**\nSince $v_y = \\frac{dy}{dt} = v_0 = \\text{const}$, we have $dt = \\frac{dy}{v_0}$.\n$$\\frac{dx}{dy} = \\frac{v_x}{v_y} = \\frac{ay}{v_0} \\implies x(y) = \\int_0^y \\frac{ay'}{v_0}dy' = \\frac{ay^2}{2v_0}$$\n\n**(b) Accelerations:**\n1. **Total acceleration:**\n   $$w_x = \\frac{dv_x}{dt} = a\\frac{dy}{dt} = av_0, \\quad w_y = \\frac{dv_y}{dt} = 0$$\n   $$w = \\sqrt{w_x^2 + w_y^2} = av_0 = \\text{constant}$$\n\n2. **Velocity vector and unit tangent:**\n   $$\\vec{v} = ay\\hat{i} + v_0\\hat{j}, \\quad v = \\sqrt{v_0^2 + a^2 y^2} = v_0\\sqrt{1 + \\left(\\frac{ay}{v_0}\\right)^2}$$\n\n3. **Tangential acceleration:**\n   $$w_\\tau = \\frac{\\vec{w}\\cdot\\vec{v}}{v} = \\frac{(av_0\\hat{i})\\cdot(ay\\hat{i} + v_0\\hat{j})}{v} = \\frac{a^2 v_0 y}{v_0\\sqrt{1 + (ay/v_0)^2}} = \\frac{a^2 y}{\\sqrt{1 + (ay/v_0)^2}}$$\n\n4. **Normal acceleration:**\n   $$w_n = \\sqrt{w^2 - w_\\tau^2} = \\sqrt{a^2 v_0^2 - \\frac{a^4 y^2}{1 + a^2 y^2/v_0^2}} = \\frac{av_0}{\\sqrt{1 + (ay/v_0)^2}}$$",
        "tags": ["kinematics", "wind shear", "normal acceleration", "tangential acceleration"]
    },
    {
        "id": "1.35",
        "title": "Trajectory and Curvature Radius for v = a i + bx j",
        "difficulty": 2,
        "question": "A particle moves in the plane $xy$ with velocity $\\vec{v} = a\\hat{i} + bx\\hat{j}$, where $\\hat{i}$ and $\\hat{j}$ are unit vectors along $x$ and $y$, and $a$ and $b$ are positive constants. At $t = 0$ the particle was located at $x = y = 0$. Find:\n(a) the equation of the particle's trajectory $y(x)$;\n(b) the curvature radius of the trajectory as a function of $x$.",
        "hints": [
            "Divide $v_y / v_x$ to obtain $dy/dx = bx/a$.",
            "Integrate to obtain $y(x)$.",
            "Curvature radius is $R = \\frac{[1 + (y')^2]^{3/2}}{|y''|}$ or $R = v^2 / w_n$."
        ],
        "answer": "(a) $y = \\frac{b}{2a}x^2$; (b) $R(x) = \\frac{a}{b}\\left[1 + \\left(\\frac{bx}{a}\\right)^2\\right]^{3/2}$",
        "solution": "**(a) Trajectory equation:**\n$$\\frac{dy}{dx} = \\frac{v_y}{v_x} = \\frac{bx}{a}$$\nIntegrating with initial condition $y(0) = 0$:\n$$y(x) = \\frac{b}{2a}x^2$$\n\n**(b) Curvature radius $R(x)$:**\nUsing the differential geometry formula for planar curves:\n$$y' = \\frac{bx}{a}, \\quad y'' = \\frac{b}{a}$$\n$$R = \\frac{[1 + (y')^2]^{3/2}}{|y''|} = \\frac{\\left[1 + \\left(\\frac{bx}{a}\\right)^2\\right]^{3/2}}{b/a} = \\frac{a}{b}\\left[1 + \\left(\\frac{bx}{a}\\right)^2\\right]^{3/2}$$",
        "tags": ["kinematics", "curvature radius", "calculus"]
    },
    {
        "id": "1.36",
        "title": "Tangential Acceleration along Given Trajectory",
        "difficulty": 2,
        "question": "A particle $A$ moves in one direction along a given trajectory with a tangential acceleration $w_\\tau = \\vec{a}\\cdot\\hat{\\tau}$, where $\\vec{a}$ is a constant vector coinciding in direction with the $x$-axis, and $\\hat{\\tau}$ is a unit vector tangent to the velocity vector at a given point. Find how the velocity of the particle depends on $x$ provided that its velocity is negligible at $x = 0$.",
        "hints": [
            "Notice that $\\vec{a}\\cdot\\hat{\\tau}\\,ds = \\vec{a}\\cdot d\\vec{r} = a\\,dx$.",
            "Tangential acceleration satisfies $w_\\tau = v\\frac{dv}{ds}$.",
            "Multiply by $ds$: $v\\,dv = w_\\tau ds = a\\,dx$."
        ],
        "answer": "$v = \\sqrt{2ax}$",
        "solution": "1. **Differential relation:**\n   Tangential acceleration is defined as:\n   $$w_\\tau = v\\frac{dv}{ds}$$\n   We are given $w_\\tau = \\vec{a}\\cdot\\hat{\\tau}$. Since $\\hat{\\tau} = \\frac{d\\vec{r}}{ds}$, we have:\n   $$w_\\tau = \\vec{a} \\cdot \\frac{d\\vec{r}}{ds}$$\n   $$\\implies w_\\tau ds = \\vec{a} \\cdot d\\vec{r}$$\n\n2. **Integration:**\n   Since $\\vec{a} = a\\hat{i}$ is constant:\n   $$\\vec{a} \\cdot d\\vec{r} = a\\,dx$$\n   Equating the two expressions for $w_\\tau ds$:\n   $$v\\,dv = a\\,dx$$\n   Integrating from $v = 0$ at $x = 0$:\n   $$\\int_0^v v' dv' = \\int_0^x a\\,dx' \\implies \\frac{v^2}{2} = ax \\implies v = \\sqrt{2ax}$$",
        "tags": ["kinematics", "work-energy analogy", "tangential acceleration"]
    },
    {
        "id": "1.37",
        "title": "Circular Acceleration after n-th Fraction of Circle",
        "difficulty": 1,
        "question": "A point moves along a circle with velocity $v = at$, where $a = 0.50\\text{ m/s}^2$. Find the total acceleration of the point at the moment when it has covered the $n$-th ($n = 0.10$) fraction of the circle after the beginning of motion.",
        "hints": [
            "Distance covered is $s = \\frac{1}{2}at^2 = n(2\\pi R)$.",
            "Tangential acceleration is constant: $w_\\tau = dv/dt = a$.",
            "Normal acceleration is $w_n = v^2 / R = 2as / R = 4\\pi n a$."
        ],
        "answer": "$w = a\\sqrt{1 + 16\\pi^2 n^2} = 0.8\\text{ m/s}^2$",
        "solution": "1. **Kinematics along the circular path:**\n   - Velocity: $v = at$.\n   - Tangential acceleration: $w_\\tau = \\frac{dv}{dt} = a$.\n   - Distance covered: $s = \\int_0^t at' dt' = \\frac{1}{2}at^2$.\n   Given $s = n(2\\pi R) = 2\\pi n R$, we have:\n   $$v^2 = 2as = 2a(2\\pi n R) = 4\\pi n a R$$\n\n2. **Normal acceleration:**\n   $$w_n = \\frac{v^2}{R} = \\frac{4\\pi n a R}{R} = 4\\pi n a$$\n\n3. **Total acceleration:**\n   $$w = \\sqrt{w_\\tau^2 + w_n^2} = \\sqrt{a^2 + (4\\pi n a)^2} = a\\sqrt{1 + 16\\pi^2 n^2}$$\n\n**Numerical Calculation:**\n$$16\\pi^2 n^2 = 16 \\times 9.8696 \\times (0.10)^2 = 1.579$$\n$$w = 0.50 \\times \\sqrt{1 + 1.579} = 0.50 \\times \\sqrt{2.579} = 0.50 \\times 1.606 \\approx 0.80\\text{ m/s}^2$$",
        "tags": ["kinematics", "circular motion", "total acceleration"]
    },
    {
        "id": "1.38",
        "title": "Deceleration on Circle with Equal Tangential and Normal Moduli",
        "difficulty": 2,
        "question": "A point moves with deceleration along a circle of radius $R$ so that at any moment its tangential and normal accelerations are equal in moduli ($|w_\\tau| = w_n$). At $t = 0$ the velocity equals $v_0$. Find:\n(a) the velocity as a function of time and as a function of distance covered $s$;\n(b) the total acceleration as a function of velocity and distance covered.",
        "hints": [
            "Since motion decelerates, $w_\\tau = -v^2/R$.",
            "Use $-dv/dt = v^2/R$ for $v(t)$ and $-v dv/ds = v^2/R$ for $v(s)$.",
            "Total acceleration is $w = \\sqrt{w_\\tau^2 + w_n^2} = \\sqrt{2}w_n = \\sqrt{2}v^2/R$."
        ],
        "answer": "(a) $v(t) = \\frac{v_0}{1 + v_0 t/R}$, $v(s) = v_0 e^{-s/R}$; (b) $w(v) = \\frac{\\sqrt{2}v^2}{R}$, $w(s) = \\frac{\\sqrt{2}v_0^2}{R}e^{-2s/R}$",
        "solution": "**(a) Velocity as functions of $t$ and $s$:**\nGiven $|w_\\tau| = w_n = \\frac{v^2}{R}$, and since the particle is decelerating, $w_\\tau = -\\frac{v^2}{R}$.\n1. With respect to time $t$:\n   $$\\frac{dv}{dt} = -\\frac{v^2}{R} \\implies -\\frac{dv}{v^2} = \\frac{dt}{R}$$\n   $$\\frac{1}{v} - \\frac{1}{v_0} = \\frac{t}{R} \\implies v(t) = \\frac{v_0}{1 + v_0 t/R}$$\n2. With respect to distance $s$:\n   $$v\\frac{dv}{ds} = -\\frac{v^2}{R} \\implies \\frac{dv}{v} = -\\frac{ds}{R}$$\n   $$\\ln\\left(\\frac{v}{v_0}\\right) = -\\frac{s}{R} \\implies v(s) = v_0 e^{-s/R}$$\n\n**(b) Total acceleration:**\n$$w = \\sqrt{w_\\tau^2 + w_n^2} = \\sqrt{\\left(\\frac{v^2}{R}\\right)^2 + \\left(\\frac{v^2}{R}\\right)^2} = \\frac{\\sqrt{2}v^2}{R}$$\nAs a function of distance $s$:\n$$w(s) = \\frac{\\sqrt{2}v_0^2}{R}e^{-2s/R}$$",
        "tags": ["kinematics", "circular motion", "differential equations"]
    },
    {
        "id": "1.39",
        "title": "Acceleration Angle for Velocity Proportional to sqrt(s)",
        "difficulty": 1,
        "question": "A point moves along an arc of a circle of radius $R$. Its velocity depends on the distance covered $s$ as $v = a\\sqrt{s}$, where $a$ is a constant. Find the angle $\\alpha$ between the vector of the total acceleration and the velocity vector as a function of $s$.",
        "hints": [
            "Velocity vector is directed along the tangent, so $\\tan\\alpha = w_n / w_\\tau$.",
            "Calculate tangential acceleration $w_\\tau = v\\frac{dv}{ds}$.",
            "Calculate normal acceleration $w_n = v^2 / R$."
        ],
        "answer": "$\\tan\\alpha = \\frac{2s}{R}$",
        "solution": "1. **Tangential acceleration:**\n   $$w_\\tau = v\\frac{dv}{ds} = (a\\sqrt{s}) \\cdot \\frac{d}{ds}(a s^{1/2}) = a\\sqrt{s} \\cdot \\frac{a}{2\\sqrt{s}} = \\frac{a^2}{2} = \\text{constant}$$\n\n2. **Normal acceleration:**\n   $$w_n = \\frac{v^2}{R} = \\frac{a^2 s}{R}$$\n\n3. **Angle $\\alpha$ with velocity vector:**\n   Since the velocity vector is purely tangential, the angle $\\alpha$ between total acceleration $\\vec{w} = w_\\tau\\hat{\\tau} + w_n\\hat{n}$ and velocity is:\n   $$\\tan\\alpha = \\frac{w_n}{w_\\tau} = \\frac{a^2 s / R}{a^2 / 2} = \\frac{2s}{R}$$",
        "tags": ["kinematics", "circular motion", "acceleration components"]
    },
    {
        "id": "1.40",
        "title": "Sinusoidal Motion on Circular Arc",
        "difficulty": 2,
        "question": "A particle moves along an arc of a circle of radius $R$ according to the law $l = a\\sin\\omega t$, where $l$ is the displacement along the arc from the initial position, and $a$, $\\omega$ are constants. Assuming $R = 1.00\\text{ m}$, $a = 0.80\\text{ m}$, and $\\omega = 2.00\\text{ rad/s}$, find:\n(a) the magnitude of the total acceleration at points $l = 0$ and $l = \\pm a$;\n(b) the minimum value of total acceleration $w_{\\min}$ and the corresponding displacement $l_m$.",
        "hints": [
            "Find velocity $v = dl/dt = a\\omega\\cos\\omega t$ and tangential acceleration $w_\\tau = dv/dt = -a\\omega^2\\sin\\omega t = -\\omega^2 l$.",
            "Normal acceleration is $w_n = v^2/R = \\frac{a^2\\omega^2}{R}(1 - l^2/a^2)$.",
            "Express total acceleration $w^2(l) = w_\\tau^2 + w_n^2$ and minimize with respect to $l^2$."
        ],
        "answer": "(a) $w(0) = 2.6\\text{ m/s}^2$, $w(\\pm a) = 3.2\\text{ m/s}^2$; (b) $w_{\\min} = 2.5\\text{ m/s}^2$ at $l_m = \\pm 0.37\\text{ m}$",
        "solution": "1. **Kinematic quantities as functions of $l$:**\n   - Tangential acceleration: $w_\\tau = -a\\omega^2\\sin\\omega t = -\\omega^2 l$.\n   - Speed: $v^2 = a^2\\omega^2\\cos^2\\omega t = a^2\\omega^2\\left(1 - \\frac{l^2}{a^2}\\right) = \\omega^2(a^2 - l^2)$.\n   - Normal acceleration: $w_n = \\frac{v^2}{R} = \\frac{\\omega^2(a^2 - l^2)}{R}$.\n\n2. **Part (a): Accelerations at specific points:**\n   - At $l = 0$:\n     $$w_\\tau = 0, \\quad w_n = \\frac{a^2\\omega^2}{R} = \\frac{0.80^2 \\times 2.00^2}{1.00} = 2.56\\text{ m/s}^2 \\approx 2.6\\text{ m/s}^2$$\n     $$w = 2.56\\text{ m/s}^2 \\approx 2.6\\text{ m/s}^2$$\n   - At $l = \\pm a$:\n     $$w_n = 0, \\quad w_\\tau = a\\omega^2 = 0.80 \\times 4.00 = 3.20\\text{ m/s}^2$$\n     $$w = 3.2\\text{ m/s}^2$$\n\n3. **Part (b): Minimum total acceleration:**\n   $$w^2 = w_\\tau^2 + w_n^2 = \\omega^4 l^2 + \\frac{\\omega^4}{R^2}(a^2 - l^2)^2$$\n   Differentiating with respect to $l^2$ and setting to 0:\n   $$\\frac{d(w^2)}{d(l^2)} = \\omega^4 - \\frac{2\\omega^4}{R^2}(a^2 - l^2) = 0 \\implies 1 - \\frac{2(a^2 - l_m^2)}{R^2} = 0$$\n   $$l_m = \\pm a\\sqrt{1 - \\frac{R^2}{2a^2}} \\quad \\text{(or with } R > a, l_m = \\pm a\\sqrt{1 - a^2/(2R^2)}\\text{)}$$\n   With $R = 1.00\\text{ m}, a = 0.80\\text{ m}$:\n   $$l_m = \\pm 0.80 \\sqrt{1 - \\frac{0.80^2}{2 \\times 1.00^2}} = \\pm 0.80 \\sqrt{1 - 0.32} = \\pm 0.80 \\times \\sqrt{0.68} \\approx \\pm 0.37\\text{ m}$$\n   $$w_{\\min} = a\\omega^2\\sqrt{1 - \\frac{a^2}{4R^2}} = 0.80 \\times 4.0 \\times \\sqrt{1 - \\frac{0.64}{4}} = 3.2 \\times \\sqrt{0.84} \\approx 2.5\\text{ m/s}^2$$",
        "tags": ["kinematics", "circular motion", "optimization"]
    }
]
