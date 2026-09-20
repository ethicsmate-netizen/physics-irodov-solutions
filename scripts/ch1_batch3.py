"""
ch1_batch3.py
Problems 1.41 through 1.58 of Irodov Chapter 1.1 Kinematics.
"""

BATCH_3 = [
    {
        "id": "1.41",
        "title": "Curvature Radius from Tangential and Normal Acceleration",
        "difficulty": 2,
        "question": "A point moves in the plane so that its tangential acceleration is $w_\\tau = a$, and its normal acceleration is $w_n = bt^4$, where $a$ and $b$ are positive constants, and $t$ is time. At $t = 0$ the point was at rest. Find how the curvature radius $R$ of the point's trajectory and the total acceleration $w$ depend on the distance covered $s$.",
        "hints": [
            "With constant $w_\\tau = a$, distance covered is $s = \\frac{1}{2}at^2 \\implies t^2 = 2s/a$.",
            "Speed is $v = at \\implies v^2 = 2as$.",
            "Normal acceleration is $w_n = v^2/R = bt^4 \\implies R = v^2 / (bt^4)$."
        ],
        "answer": "$R(s) = \\frac{a^3}{2bs}$, $w(s) = a\\sqrt{1 + \\left(\\frac{4bs^2}{a^3}\\right)^2}$",
        "solution": "1. **Kinematic relationships with constant $w_\\tau = a$:**\n   - Velocity: $v = at$.\n   - Distance covered: $s = \\frac{1}{2}at^2 \\implies t^2 = \\frac{2s}{a}$, $t^4 = \\frac{4s^2}{a^2}$.\n   - Velocity squared: $v^2 = a^2 t^2 = 2as$.\n\n2. **Curvature radius $R(s)$:**\n   $$w_n = \\frac{v^2}{R} = bt^4$$\n   $$R = \\frac{v^2}{bt^4} = \\frac{2as}{b \\cdot (4s^2 / a^2)} = \\frac{2as}{\\frac{4bs^2}{a^2}} = \\frac{a^3}{2bs}$$\n\n3. **Total acceleration $w(s)$:**\n   $$w_n = b t^4 = b\\left(\\frac{4s^2}{a^2}\\right) = \\frac{4bs^2}{a^2}$$\n   $$w = \\sqrt{w_\\tau^2 + w_n^2} = \\sqrt{a^2 + \\left(\\frac{4bs^2}{a^2}\\right)^2} = a\\sqrt{1 + \\left(\\frac{4bs^2}{a^3}\\right)^2}$$",
        "tags": ["kinematics", "curvature radius", "normal acceleration", "tangential acceleration"]
    },
    {
        "id": "1.42",
        "title": "Curvature Radius and Acceleration on Parabola and Ellipse",
        "difficulty": 2,
        "question": "A particle moves along a plane trajectory $y(x)$ with velocity $v$ whose modulus is constant. Find the acceleration of the particle at the point $x = 0$ and the curvature radius of the trajectory at that point if the trajectory has the form:\n(a) of a parabola $y = ax^2$;\n(b) of an ellipse $(x/a)^2 + (y/b)^2 = 1$ ($a$ and $b$ are positive constants).",
        "hints": [
            "At constant speed $v$, tangential acceleration is zero: $w_\\tau = 0$, so total acceleration is purely normal: $w = w_n = v^2 / R$.",
            "Use the curvature formula $R = \\frac{[1 + (y')^2]^{3/2}}{|y''|}$ at $x = 0$."
        ],
        "answer": "(a) $w = 2av^2$, $R = \\frac{1}{2a}$; (b) $w = \\frac{bv^2}{a^2}$, $R = \\frac{a^2}{b}$",
        "solution": "Since speed $v$ is constant, $w_\\tau = 0$, so the acceleration is purely normal:\n$$w = w_n = \\frac{v^2}{R}$$\nwhere the radius of curvature is $R = \\frac{[1 + (y')^2]^{3/2}}{|y''|}$.\n\n**(a) Parabola $y = ax^2$:**\n- $y' = 2ax \\implies y'(0) = 0$.\n- $y'' = 2a$.\n- At $x = 0$:\n  $$R = \\frac{[1 + 0]^{3/2}}{2a} = \\frac{1}{2a}$$\n  $$w = \\frac{v^2}{R} = 2av^2$$\n\n**(b) Ellipse $(x/a)^2 + (y/b)^2 = 1$:**\nAt $x = 0$, $y = b$. Differentiating implicitly:\n$$\\frac{2x}{a^2} + \\frac{2y y'}{b^2} = 0 \\implies y' = -\\frac{b^2 x}{a^2 y}$$\nAt $x = 0, y = b$: $y'(0) = 0$.\nDifferentiating again:\n$$\\frac{1}{a^2} + \\frac{(y')^2 + y y''}{b^2} = 0$$\nAt $x = 0, y = b, y' = 0$:\n$$\\frac{1}{a^2} + \\frac{b y''}{b^2} = 0 \\implies y'' = -\\frac{b}{a^2}$$\nRadius of curvature:\n$$R = \\frac{1}{|y''|} = \\frac{a^2}{b}$$\nAcceleration:\n$$w = \\frac{v^2}{R} = \\frac{bv^2}{a^2}$$",
        "tags": ["kinematics", "curvature radius", "calculus", "conic sections"]
    },
    {
        "id": "1.43",
        "title": "Rotating Chords and Inscribed Angle Velocity",
        "difficulty": 2,
        "question": "A particle $A$ moves along a circle of radius $R = 50\\text{ cm}$ so that its radius vector $\\vec{r}$ relative to a point $O$ on the circle rotates with constant angular velocity $\\omega = 0.40\\text{ rad/s}$. Find the modulus of the velocity of the particle, and the modulus and direction of its total acceleration.",
        "hints": [
            "Recall that the central angle is twice the inscribed angle: $\\theta_{\\text{center}} = 2\\varphi$, so angular velocity about center is $\\omega_{\\text{center}} = 2\\omega$.",
            "Linear speed along the circle is $v = \\omega_{\\text{center}} R = 2\\omega R$.",
            "Since $\\omega_{\\text{center}}$ is constant, motion is uniform circular motion with purely centripetal acceleration."
        ],
        "answer": "$v = 2\\omega R = 0.40\\text{ m/s}$, $w = 4\\omega^2 R = 0.32\\text{ m/s}^2$ permanently directed to the circle center.",
        "solution": "1. **Relation between inscribed angle and central angle:**\n   Let $C$ be the center of the circle of radius $R$. The angle of the chord $OA$ with respect to the initial axis is $\\varphi$, which increases at rate $\\dot{\\varphi} = \\omega$.\n   In a circle, the central angle subtending the arc $OA$ is $\\theta = 2\\varphi$.\n   Therefore, the angular velocity of point $A$ about the center $C$ is:\n   $$\\omega_C = \\frac{d\\theta}{dt} = 2\\frac{d\\varphi}{dt} = 2\\omega$$\n\n2. **Velocity:**\n   $$v = \\omega_C R = 2\\omega R = 2(0.40)(0.50) = 0.40\\text{ m/s}$$\n\n3. **Total acceleration:**\n   Since $\\omega = \\text{const}$, the angular acceleration $\\beta = 0$, so $w_\\tau = 0$.\n   The acceleration is entirely normal (centripetal), directed toward the center $C$:\n   $$w = w_n = \\omega_C^2 R = (2\\omega)^2 R = 4\\omega^2 R$$\n   $$w = 4(0.40)^2(0.50) = 4(0.16)(0.50) = 0.32\\text{ m/s}^2$$",
        "tags": ["kinematics", "circular motion", "inscribed angle"]
    },
    {
        "id": "1.44",
        "title": "Total Acceleration on Rim with Quadratic Angle Law",
        "difficulty": 2,
        "question": "A wheel rotates around a stationary axis so that the rotation angle $\\varphi$ varies with time as $\\varphi = at^2$, where $a = 0.20\\text{ rad/s}^2$. Find the total acceleration $w$ of point $A$ on the rim at $t = 2.5\\text{ s}$ if the linear velocity of point $A$ at this moment is $v = 0.65\\text{ m/s}$.",
        "hints": [
            "Angular velocity is $\\omega = \\dot{\\varphi} = 2at$, and angular acceleration is $\\beta = \\ddot{\\varphi} = 2a$.",
            "Linear speed is $v = \\omega R = 2at R \\implies R = \\frac{v}{2at}$.",
            "Tangential and normal accelerations: $w_\\tau = \\beta R$, $w_n = \\omega^2 R$."
        ],
        "answer": "$w = \\frac{v}{t}\\sqrt{1 + 4a^2 t^4} = 0.70\\text{ m/s}^2$",
        "solution": "1. **Angular kinematics:**\n   $$\\varphi = at^2 \\implies \\omega = \\frac{d\\varphi}{dt} = 2at, \\quad \\beta = \\frac{d\\omega}{dt} = 2a$$\n\n2. **Radius of the wheel:**\n   Given linear velocity $v = \\omega R = (2at)R$:\n   $$R = \\frac{v}{2at}$$\n\n3. **Acceleration components:**\n   - Tangential acceleration:\n     $$w_\\tau = \\beta R = 2a \\left(\\frac{v}{2at}\\right) = \\frac{v}{t}$$\n   - Normal acceleration:\n     $$w_n = \\omega^2 R = (2at)^2 \\left(\\frac{v}{2at}\\right) = 2at v$$\n\n4. **Total acceleration:**\n   $$w = \\sqrt{w_\\tau^2 + w_n^2} = \\sqrt{\\left(\\frac{v}{t}\\right)^2 + (2at v)^2} = \\frac{v}{t}\\sqrt{1 + 4a^2 t^4}$$\n\n**Numerical Calculation:**\nAt $t = 2.5\\text{ s}$, $v = 0.65\\text{ m/s}$, $a = 0.20\\text{ rad/s}^2$:\n$$4a^2 t^4 = 4(0.20)^2 (2.5)^4 = 4(0.04)(39.0625) = 0.16 \\times 39.0625 = 6.25$$\n$$\\sqrt{1 + 6.25} = \\sqrt{7.25} \\approx 2.6926$$\n$$w = \\frac{0.65}{2.5} \\times 2.6926 = 0.26 \\times 2.6926 \\approx 0.70\\text{ m/s}^2$$",
        "tags": ["kinematics", "rotational kinematics", "total acceleration"]
    },
    {
        "id": "1.45",
        "title": "Axial Rotation of Shell Leaving Rifled Barrel",
        "difficulty": 1,
        "question": "A shell acquires initial velocity $v = 320\\text{ m/s}$, having made $n = 2.0$ turns inside a barrel whose length is $l = 2.0\\text{ m}$. Assuming that the shell moves inside the barrel with uniform acceleration, find the angular velocity of its axial rotation at the moment when the shell escapes the barrel.",
        "hints": [
            "Total angle of axial rotation inside barrel is $\\Phi = 2\\pi n$.",
            "Since rifling pitch is constant, axial rotation angle is proportional to translation distance: $\\varphi(x) = \\frac{2\\pi n}{l} x$.",
            "Differentiating with respect to time: $\\omega = \\frac{d\\varphi}{dt} = \\frac{2\\pi n}{l}\\frac{dx}{dt} = \\frac{2\\pi n}{l}v$."
        ],
        "answer": "$\\omega = \\frac{2\\pi n v}{l} = 2.0\\times 10^3\\text{ rad/s}$",
        "solution": "1. **Rifling constraint:**\n   The rifling grooves inside the barrel force the shell to rotate proportionally to its linear displacement $x$ along the barrel:\n   $$\\varphi = k x$$\n   Since the shell makes $n$ complete turns over barrel length $l$:\n   $$\\Phi = 2\\pi n = k l \\implies k = \\frac{2\\pi n}{l}$$\n\n2. **Angular velocity:**\n   Differentiating the rotation angle with respect to time:\n   $$\\omega = \\frac{d\\varphi}{dt} = k \\frac{dx}{dt} = \\frac{2\\pi n}{l} v$$\n   This relation holds at every instant, including the exit moment where translation velocity is $v$.\n\n**Numerical Calculation:**\n$$\\omega = \\frac{2\\pi \\times 2.0 \\times 320}{2.0} = 2\\pi \\times 320 \\approx 2010.6\\text{ rad/s} \\approx 2.0 \\times 10^3\\text{ rad/s}$$",
        "tags": ["kinematics", "rotational kinematics", "rigid body"]
    },
    {
        "id": "1.46",
        "title": "Cubic Deceleration Law of Rotation",
        "difficulty": 2,
        "question": "A solid body rotates about a stationary axis according to the law $\\varphi = at - bt^3$, where $a = 6.0\\text{ rad/s}$ and $b = 2.0\\text{ rad/s}^3$. Find:\n(a) the mean values of angular velocity $\\langle \\omega \\rangle$ and angular acceleration $\\langle \\beta \\rangle$ averaged over the time interval between $t = 0$ and the complete stop;\n(b) the angular acceleration at the moment when the body stops.",
        "hints": [
            "Differentiate to find angular velocity $\\omega(t) = a - 3bt^2$ and angular acceleration $\\beta(t) = -6bt$.",
            "Body stops when $\\omega(t) = 0 \\implies t_0 = \\sqrt{a / (3b)}$.",
            "Mean angular velocity is $\\Delta \\varphi / t_0$; mean angular acceleration is $(\\omega(t_0) - \\omega(0))/t_0$."
        ],
        "answer": "(a) $\\langle \\omega \\rangle = \\frac{2}{3}a = 4.0\\text{ rad/s}$, $|\\langle \\beta \\rangle| = \\sqrt{3ab} = 6.0\\text{ rad/s}^2$; (b) $\\beta(t_0) = 2\\sqrt{3ab} = 12\\text{ rad/s}^2$",
        "solution": "1. **Angular velocity and acceleration:**\n   $$\\omega(t) = \\frac{d\\varphi}{dt} = a - 3bt^2$$\n   $$\\beta(t) = \\frac{d\\omega}{dt} = -6bt$$\n\n2. **Time to stop ($t_0$):**\n   $$\\omega(t_0) = 0 \\implies a - 3bt_0^2 = 0 \\implies t_0 = \\sqrt{\\frac{a}{3b}}$$\n   With $a = 6.0, b = 2.0$:\n   $$t_0 = \\sqrt{\\frac{6.0}{6.0}} = 1.0\\text{ s}$$\n\n3. **Part (a): Mean quantities over $[0, t_0]$:**\n   - Angle rotated: $\\varphi(t_0) = a t_0 - b t_0^3 = t_0(a - b t_0^2) = t_0\\left(a - \\frac{a}{3}\\right) = \\frac{2}{3}a t_0$.\n   - Mean angular velocity:\n     $$\\langle \\omega \\rangle = \\frac{\\varphi(t_0)}{t_0} = \\frac{2}{3}a = \\frac{2}{3}(6.0) = 4.0\\text{ rad/s}$$\n   - Mean angular acceleration modulus:\n     $$|\\langle \\beta \\rangle| = \\frac{|\\omega(t_0) - \\omega(0)|}{t_0} = \\frac{a}{t_0} = \\frac{a}{\\sqrt{a/(3b)}} = \\sqrt{3ab} = \\sqrt{3(6)(2)} = 6.0\\text{ rad/s}^2$$\n\n4. **Part (b): Angular acceleration at stop:**\n   $$|\\beta(t_0)| = 6b t_0 = 6b \\sqrt{\\frac{a}{3b}} = 2\\sqrt{3ab} = 2 \\times 6.0 = 12\\text{ rad/s}^2$$",
        "tags": ["kinematics", "rotational kinematics", "calculus", "average values"]
    },
    {
        "id": "1.47",
        "title": "Time for Acceleration Angle in Rotation beta = at",
        "difficulty": 2,
        "question": "A solid body starts rotating about a stationary axis with an angular acceleration $\\beta = at$, where $a = 2.0\\times 10^{-2}\\text{ rad/s}^3$. How soon after the beginning of rotation will the total acceleration vector of an arbitrary point of the body form an angle $\\alpha = 60^\\circ$ with its velocity vector?",
        "hints": [
            "Integrate $\\beta(t)$ from rest: $\\omega(t) = \\int_0^t at' dt' = \\frac{1}{2}at^2$.",
            "The angle between total acceleration and velocity is given by $\\tan\\alpha = w_n / w_\\tau$.",
            "Since $w_n = \\omega^2 R$ and $w_\\tau = \\beta R$, the radius $R$ cancels out: $\\tan\\alpha = \\omega^2 / \\beta$."
        ],
        "answer": "$t = \\sqrt[3]{\\frac{4\\tan\\alpha}{a}} \\approx 7.0\\text{ s}$",
        "solution": "1. **Angular kinematics:**\n   $$\\beta(t) = at$$\n   $$\\omega(t) = \\int_0^t at' dt' = \\frac{1}{2}at^2$$\n\n2. **Linear acceleration components of a point at distance $R$:**\n   - Tangential acceleration: $w_\\tau = \\beta R = at R$.\n   - Normal acceleration: $w_n = \\omega^2 R = \\left(\\frac{1}{2}at^2\\right)^2 R = \\frac{1}{4}a^2 t^4 R$.\n\n3. **Angle $\\alpha$ with velocity vector:**\n   Because the velocity is purely tangential:\n   $$\\tan\\alpha = \\frac{w_n}{w_\\tau} = \\frac{\\frac{1}{4}a^2 t^4 R}{at R} = \\frac{1}{4}at^3$$\n   $$t^3 = \\frac{4\\tan\\alpha}{a} \\implies t = \\left(\\frac{4\\tan\\alpha}{a}\\right)^{1/3}$$\n\n**Numerical Calculation:**\nFor $\\alpha = 60^\\circ$, $\\tan 60^\\circ = \\sqrt{3} \\approx 1.732$, $a = 0.020\\text{ rad/s}^3$:\n$$t^3 = \\frac{4 \\times 1.732}{0.020} = \\frac{6.928}{0.020} = 346.4$$\n$$t = (346.4)^{1/3} \\approx 7.02\\text{ s} \\approx 7.0\\text{ s}$$",
        "tags": ["kinematics", "rotational kinematics", "acceleration components"]
    },
    {
        "id": "1.48",
        "title": "Mean Angular Velocity under Deceleration beta proportional to sqrt(omega)",
        "difficulty": 2,
        "question": "A solid body rotates with deceleration about a stationary axis with an angular deceleration $\\beta \\propto \\sqrt{\\omega}$, where $\\omega$ is its angular velocity. Find the mean angular velocity of the body averaged over the whole time of rotation if at the initial moment its angular velocity was $\\omega_0$.",
        "hints": [
            "Write $\\frac{d\\omega}{dt} = -k\\sqrt{\\omega}$ and integrate to find stopping time $T$.",
            "Express total angle rotated $\\Delta \\varphi = \\int_0^T \\omega(t)\\,dt$ or use $\\omega\\frac{d\\omega}{d\\varphi} = -k\\sqrt{\\omega}$.",
            "Mean angular velocity is $\\langle \\omega \\rangle = \\Delta \\varphi / T$."
        ],
        "answer": "$\\langle \\omega \\rangle = \\frac{\\omega_0}{3}$",
        "solution": "1. **Differential equation for $\\omega(t)$:**\n   $$\\frac{d\\omega}{dt} = -k\\omega^{1/2} \\implies \\omega^{-1/2} d\\omega = -k dt$$\n   Integrating from $\\omega_0$ to $\\omega(t)$:\n   $$2\\sqrt{\\omega} - 2\\sqrt{\\omega_0} = -kt \\implies \\sqrt{\\omega(t)} = \\sqrt{\\omega_0} - \\frac{kt}{2}$$\n   The body stops ($\\omega = 0$) at time:\n   $$T = \\frac{2\\sqrt{\\omega_0}}{k}$$\n\n2. **Angular velocity as function of time:**\n   $$\\omega(t) = \\left(\\sqrt{\\omega_0} - \\frac{kt}{2}\\right)^2 = \\omega_0 \\left(1 - \\frac{t}{T}\\right)^2$$\n\n3. **Mean angular velocity:**\n   $$\\langle \\omega \\rangle = \\frac{1}{T}\\int_0^T \\omega(t)\\,dt = \\frac{\\omega_0}{T}\\int_0^T \\left(1 - \\frac{t}{T}\\right)^2 dt$$\n   Let $u = 1 - t/T$, then $dt = -T du$:\n   $$\\langle \\omega \\rangle = \\omega_0 \\int_0^1 u^2 du = \\frac{\\omega_0}{3}$$",
        "tags": ["kinematics", "rotational kinematics", "differential equations", "average velocity"]
    },
    {
        "id": "1.49",
        "title": "Angular Velocity Dependent on Rotation Angle: omega = omega_0 - a phi",
        "difficulty": 2,
        "question": "A solid body rotates about a stationary axis so that its angular velocity depends on the rotation angle $\\varphi$ as $\\omega = \\omega_0 - a\\varphi$, where $\\omega_0$ and $a$ are positive constants. At $t = 0$, $\\varphi = 0$. Find the time dependence of:\n(a) the rotation angle $\\varphi(t)$;\n(b) the angular velocity $\\omega(t)$.",
        "hints": [
            "Use definition $\\omega = \\frac{d\\varphi}{dt} = \\omega_0 - a\\varphi$.",
            "Separate variables: $\\frac{d\\varphi}{\\omega_0 - a\\varphi} = dt$.",
            "Integrate with initial condition $\\varphi(0) = 0$."
        ],
        "answer": "(a) $\\varphi(t) = \\frac{\\omega_0}{a}(1 - e^{-at})$; (b) $\\omega(t) = \\omega_0 e^{-at}$",
        "solution": "**(a) Rotation angle $\\varphi(t)$:**\n$$\\frac{d\\varphi}{dt} = \\omega_0 - a\\varphi \\implies \\frac{d\\varphi}{\\omega_0 - a\\varphi} = dt$$\nIntegrating both sides with $\\varphi(0) = 0$:\n$$-\\frac{1}{a}\\ln\\left(\\frac{\\omega_0 - a\\varphi}{\\omega_0}\\right) = t$$\n$$\\ln\\left(1 - \\frac{a}{\\omega_0}\\varphi\\right) = -at \\implies 1 - \\frac{a}{\\omega_0}\\varphi = e^{-at}$$\n$$\\varphi(t) = \\frac{\\omega_0}{a}(1 - e^{-at})$$\n\n**(b) Angular velocity $\\omega(t)$:**\n$$\\omega(t) = \\frac{d\\varphi}{dt} = \\omega_0 e^{-at}$$",
        "tags": ["kinematics", "rotational kinematics", "differential equations"]
    },
    {
        "id": "1.50",
        "title": "Harmonic Angular Acceleration: beta = beta_0 cos(phi)",
        "difficulty": 2,
        "question": "A solid body starts rotating about a stationary axis with angular acceleration $\\beta_z = \\beta_0\\cos\\varphi$, where $\\beta_0$ is a constant and $\\varphi$ is the angle of rotation from the initial position (with $\\omega_z = 0$ at $\\varphi = 0$). Find the angular velocity of the body as a function of the angle $\\varphi$.",
        "hints": [
            "Use the chain rule for angular acceleration: $\\beta_z = \\omega_z \\frac{d\\omega_z}{d\\varphi}$.",
            "Separate variables: $\\omega_z d\\omega_z = \\beta_0 \\cos\\varphi\\, d\\varphi$.",
            "Integrate from $\\omega_z = 0, \\varphi = 0$."
        ],
        "answer": "$\\omega_z = \\pm\\sqrt{2\\beta_0\\sin\\varphi}$",
        "solution": "1. **Angular differential relation:**\n   $$\\beta_z = \\frac{d\\omega_z}{dt} = \\frac{d\\omega_z}{d\\varphi}\\frac{d\\varphi}{dt} = \\omega_z \\frac{d\\omega_z}{d\\varphi}$$\n\n2. **Separation of variables and integration:**\n   $$\\omega_z d\\omega_z = \\beta_0\\cos\\varphi\\, d\\varphi$$\n   Integrating with initial condition $\\omega_z = 0$ at $\\varphi = 0$:\n   $$\\int_0^{\\omega_z} \\omega' d\\omega' = \\beta_0 \\int_0^\\varphi \\cos\\varphi' d\\varphi'$$\n   $$\\frac{\\omega_z^2}{2} = \\beta_0\\sin\\varphi$$\n   $$\\omega_z(\\varphi) = \\pm\\sqrt{2\\beta_0\\sin\\varphi}$$",
        "tags": ["kinematics", "rotational kinematics", "calculus"]
    },
    {
        "id": "1.51",
        "title": "Locus of Instantaneous Axis of Rotation for Rolling Disc",
        "difficulty": 2,
        "question": "A rotating disc moves in the positive direction of the $x$-axis. Find the equation $y(x)$ describing the position of the instantaneous axis of rotation, if at the initial moment the axis $C$ of the disc was located at the origin $O$, after which it moved:\n(a) with constant velocity $v$, while the disc started rotating counterclockwise with constant angular acceleration $\\beta$ (initial angular velocity zero);\n(b) with constant acceleration $w$ (zero initial velocity), while the disc rotates counterclockwise with constant angular velocity $\\omega$.",
        "hints": [
            "The instantaneous axis of rotation is at distance $y = v_C / \\omega$ from the center along the perpendicular to $\\vec{v}_C$.",
            "For case (a): center coordinate is $x = vt$, angular velocity is $\\omega = \\beta t$.",
            "For case (b): center coordinate is $x = \\frac{1}{2}wt^2$, center velocity is $v_C = wt$, angular velocity is constant $\\omega$."
        ],
        "answer": "(a) $y = \\frac{v^2}{\\beta x}$ (hyperbola); (b) $y = \\frac{\\sqrt{2wx}}{\\omega}$ (or $y^2 = \\frac{2wx}{\\omega^2}$, parabola)",
        "solution": "The instantaneous axis of rotation $I$ has zero velocity: $\\vec{v}_I = \\vec{v}_C + \\vec{\\omega} \\times \\vec{r}_{IC} = 0$.\nSince $\\vec{v}_C = v_C\\hat{i}$ and $\\vec{\\omega} = \\omega\\hat{k}$, the instantaneous center lies at height $y = v_C / \\omega$ above or below the center line.\n\n**(a) Uniform translation ($v_C = v$) and angular acceleration $\\beta$:**\n- Center position: $x = vt \\implies t = x/v$.\n- Angular velocity: $\\omega = \\beta t = \\beta\\left(\\frac{x}{v}\\right)$.\n- Instantaneous axis position:\n  $$y = \\frac{v_C}{\\omega} = \\frac{v}{\\beta x / v} = \\frac{v^2}{\\beta x}$$\n  This is a hyperbola.\n\n**(b) Accelerated translation ($w$) and constant angular velocity $\\omega$:**\n- Center velocity: $v_C = wt$.\n- Center position: $x = \\frac{1}{2}wt^2 \\implies t = \\sqrt{\\frac{2x}{w}}$.\n- Instantaneous axis position:\n  $$y = \\frac{v_C}{\\omega} = \\frac{w t}{\\omega} = \\frac{w}{\\omega}\\sqrt{\\frac{2x}{w}} = \\frac{\\sqrt{2wx}}{\\omega}$$\n  Squaring gives $y^2 = \\frac{2w}{\\omega^2} x$, which is a parabola.",
        "tags": ["kinematics", "rigid body", "instantaneous axis of rotation"]
    },
    {
        "id": "1.52",
        "title": "Cycloid Arc Length and Acceleration of Wheel Rim Point",
        "difficulty": 2,
        "question": "A point $A$ is located on the rim of a wheel of radius $R = 0.50\\text{ m}$ which rolls without slipping along a horizontal surface with constant velocity $v = 1.00\\text{ m/s}$. Find:\n(a) the modulus and direction of the acceleration vector of point $A$;\n(b) the total distance $s$ traversed by point $A$ between two successive moments at which it touches the surface.",
        "hints": [
            "In rolling without slipping at constant speed, center acceleration is zero, so the acceleration of any rim point is purely centripetal relative to the center: $w = v^2/R$.",
            "The trajectory of point $A$ is a cycloid: $x = R(\\omega t - \\sin\\omega t)$, $y = R(1 - \\cos\\omega t)$.",
            "The speed of point $A$ is $v_A = 2v\\sin(\\omega t/2)$. Integrate from $0$ to $T = 2\\pi/\\omega$ to find cycloid arc length $8R$."
        ],
        "answer": "(a) $w_A = \\frac{v^2}{R} = 2.0\\text{ m/s}^2$ permanently directed to the wheel center; (b) $s = 8R = 4.0\\text{ m}$",
        "solution": "**(a) Acceleration vector of rim point $A$:**\nFor rolling without slipping at constant linear speed $v$, the center has zero acceleration: $\\vec{w}_C = 0$.\nThe angular velocity is $\\omega = v/R = \\text{const}$, so angular acceleration is $\\beta = 0$.\nThe acceleration of point $A$ in the Earth frame equals its acceleration relative to the center $C$, which is purely centripetal:\n$$w_A = \\omega^2 R = \\frac{v^2}{R}$$\n$$w_A = \\frac{1.00^2}{0.50} = 2.0\\text{ m/s}^2$$\nThe vector $\\vec{w}_A$ is permanently directed towards the center of the wheel $C$.\n\n**(b) Total distance traversed between successive contacts (cycloid arc length):**\nThe velocity of point $A$ relative to the instantaneous center of rotation (contact point) is:\n$$v_A = \\omega r_{\\text{inst}} = \\omega \\cdot 2R\\sin\\left(\\frac{\\omega t}{2}\\right)$$\nThe total distance traversed in one full revolution ($T = 2\\pi/\\omega$) is:\n$$s = \\int_0^T v_A\\,dt = \\int_0^{2\\pi/\\omega} 2R\\omega \\sin\\left(\\frac{\\omega t}{2}\\right) dt = 2R \\left[ -2\\cos\\left(\\frac{\\omega t}{2}\\right) \\right]_0^{2\\pi/\\omega} = 8R$$\n$$s = 8 \\times 0.50\\text{ m} = 4.0\\text{ m}$$",
        "tags": ["kinematics", "rigid body", "rolling without slipping", "cycloid"]
    },
    {
        "id": "1.53",
        "title": "Velocities and Accelerations of Points on Rolling Ball",
        "difficulty": 2,
        "question": "A ball of radius $R = 10.0\\text{ cm}$ rolls without slipping down an inclined plane so that its centre moves with constant acceleration $w = 2.50\\text{ cm/s}^2$; $t = 2.00\\text{ s}$ after the beginning of motion find:\n(a) the velocities of the points $A$ (highest point), $B$ (side point at center height), and $O$ (contact point);\n(b) the accelerations of these points.",
        "hints": [
            "Use instantaneous center of rotation $O$ (contact point): $v = \\omega r_O$, where $\\omega = v_C / R = wt / R$.",
            "Point $O$ has zero velocity: $v_O = 0$. Point $A$ is at distance $2R$, point $B$ is at distance $\\sqrt{2}R$.",
            "Accelerations combine center acceleration $\\vec{w}_C$ and rotational accelerations (tangential and centripetal)."
        ],
        "answer": "(a) $v_A = 2wt = 10.0\\text{ cm/s}$, $v_B = \\sqrt{2}wt = 7.1\\text{ cm/s}$, $v_O = 0$; (b) $w_A = 2w\\sqrt{1 + (wt^2/2R)^2} = 5.6\\text{ cm/s}^2$, $w_B = w\\sqrt{1 + (1 - wt^2/R)^2} \\approx 2.5\\text{ cm/s}^2$, $w_O = \\frac{w^2 t^2}{R} = 2.5\\text{ cm/s}^2$",
        "solution": "1. **Velocities at $t = 2.00\\text{ s}$:**\n   Center velocity: $v_C = wt = 2.50 \\times 2.00 = 5.00\\text{ cm/s}$.\n   Angular velocity: $\\omega = v_C / R = 5.00 / 10.0 = 0.50\\text{ rad/s}$.\n   - Point $O$ (contact with plane): $v_O = 0$.\n   - Point $A$ (top of ball, distance $2R$ from $O$):\n     $$v_A = 2v_C = 2wt = 2(5.00) = 10.0\\text{ cm/s}$$\n   - Point $B$ (side of ball, distance $\\sqrt{2}R$ from $O$):\n     $$v_B = \\sqrt{2}v_C = \\sqrt{2}wt = 1.414 \\times 5.00 = 7.07\\text{ cm/s} \\approx 7.1\\text{ cm/s}$$\n\n2. **Accelerations at $t = 2.00\\text{ s}$:**\n   Center acceleration: $w_C = w = 2.50\\text{ cm/s}^2$ down the plane.\n   Angular acceleration: $\\beta = w/R = 2.50 / 10.0 = 0.25\\text{ rad/s}^2$.\n   Centripetal acceleration of rim points relative to center: $w_n = \\omega^2 R = (0.50)^2(10.0) = 2.50\\text{ cm/s}^2$.\n   Tangential acceleration of rim points relative to center: $w_\\tau = \\beta R = w = 2.50\\text{ cm/s}^2$.\n   - Contact point $O$:\n     Linear translation $w$ and tangential $\\beta R = w$ cancel along the plane: $w_{Ox} = w - \\beta R = 0$.\n     Normal centripetal component remains directed toward center: $w_O = w_n = \\frac{w^2 t^2}{R} = 2.50\\text{ cm/s}^2$.\n   - Top point $A$:\n     Parallel: $w_{Ax} = w + \\beta R = 2w = 5.0\\text{ cm/s}^2$.\n     Perpendicular: $w_{Ay} = w_n = 2.50\\text{ cm/s}^2$.\n     $$w_A = \\sqrt{(2w)^2 + w_n^2} = \\sqrt{5.0^2 + 2.5^2} = \\sqrt{25 + 6.25} = \\sqrt{31.25} \\approx 5.59\\text{ cm/s}^2 \\approx 5.6\\text{ cm/s}^2$$\n   - Side point $B$:\n     Combining translation $w$, rotational tangential $\\beta R = w$, and centripetal $w_n$:\n     $$w_B \\approx 2.5\\text{ cm/s}^2$$",
        "tags": ["kinematics", "rigid body", "rolling without slipping", "acceleration"]
    },
    {
        "id": "1.54",
        "title": "Curvature Radii of Cycloid on Rolling Cylinder",
        "difficulty": 2,
        "question": "A cylinder rolls without slipping over a horizontal plane. The radius of the cylinder is equal to $r$. Find the curvature radii of trajectories traced out by points $A$ (highest point of rim) and $B$ (side rim point at center height).",
        "hints": [
            "Use the physical formula for curvature radius $R = v^2 / w_n$.",
            "At point $A$, velocity is $v_A = 2v_C$, and its acceleration is $w_A = v_C^2 / r$ directed vertically downward (perpendicular to velocity).",
            "At point $B$, find the component of acceleration normal to its instantaneous velocity."
        ],
        "answer": "$R_A = 4r$, $R_B = 2\\sqrt{2}r$",
        "solution": "1. **Point $A$ (top of cylinder):**\n   - Velocity: point $A$ is at distance $2r$ from the instantaneous center of rotation $O$ (bottom contact point), so:\n     $$v_A = 2\\omega r = 2v_C$$\n   - Acceleration: for steady rolling, $\\vec{w}_A$ is directed purely vertically downward toward the center $C$, with modulus:\n     $$w_A = \\frac{v_C^2}{r}$$\n   Since $\\vec{v}_A$ is horizontal, $\\vec{w}_A$ is perpendicular to $\\vec{v}_A$, so $w_{n,A} = w_A = \\frac{v_C^2}{r}$.\n   - Curvature radius:\n     $$R_A = \\frac{v_A^2}{w_{n,A}} = \\frac{(2v_C)^2}{v_C^2 / r} = 4r$$\n\n2. **Point $B$ (equator of rim at center level):**\n   - Distance from instantaneous center $O$ to $B$ is $\\sqrt{r^2 + r^2} = \\sqrt{2}r$.\n   - Velocity: $v_B = \\omega (\\sqrt{2}r) = \\sqrt{2}v_C$, directed at $45^\\circ$ to the horizontal.\n   - Acceleration: $\\vec{w}_B$ is directed horizontally toward center $C$ with modulus $w_B = v_C^2 / r$.\n   - Normal acceleration: component of $\\vec{w}_B$ perpendicular to $\\vec{v}_B$ is:\n     $$w_{n,B} = w_B\\sin 45^\\circ = \\frac{v_C^2}{r\\sqrt{2}}$$\n   - Curvature radius:\n     $$R_B = \\frac{v_B^2}{w_{n,B}} = \\frac{(\\sqrt{2}v_C)^2}{v_C^2 / (r\\sqrt{2})} = 2\\sqrt{2}r$$",
        "tags": ["kinematics", "curvature radius", "rolling without slipping", "cycloid"]
    },
    {
        "id": "1.55",
        "title": "Relative Angular Velocity and Acceleration of Perpendicular Rotators",
        "difficulty": 2,
        "question": "Two solid bodies rotate about stationary mutually perpendicular intersecting axes with constant angular velocities $\\omega_1 = 3.0\\text{ rad/s}$ and $\\omega_2 = 4.0\\text{ rad/s}$. Find the angular velocity and angular acceleration of one body relative to the other.",
        "hints": [
            "Relative angular velocity is the vector difference: $\\vec{\\omega}_{\\text{rel}} = \\vec{\\omega}_1 - \\vec{\\omega}_2$.",
            "In the reference frame of body 2, the axis of body 1 rotates with angular velocity $-\\vec{\\omega}_2$.",
            "The relative angular acceleration is $\\vec{\\beta}_{\\text{rel}} = \\frac{d\\vec{\\omega}_{\\text{rel}}}{dt} = \\vec{\\omega}_1 \\times \\vec{\\omega}_2$."
        ],
        "answer": "$\\omega_{\\text{rel}} = \\sqrt{\\omega_1^2 + \\omega_2^2} = 5.0\\text{ rad/s}$, $\\beta_{\\text{rel}} = \\omega_1 \\omega_2 = 12\\text{ rad/s}^2$",
        "solution": "1. **Relative angular velocity:**\n   Let the rotation axes be along orthogonal unit vectors $\\hat{i}$ and $\\hat{j}$:\n   $$\\vec{\\omega}_1 = \\omega_1\\hat{i}, \\quad \\vec{\\omega}_2 = \\omega_2\\hat{j}$$\n   The relative angular velocity vector is:\n   $$\\vec{\\omega}_{\\text{rel}} = \\vec{\\omega}_1 - \\vec{\\omega}_2$$\n   Since the axes are mutually perpendicular:\n   $$\\omega_{\\text{rel}} = \\sqrt{\\omega_1^2 + \\omega_2^2} = \\sqrt{3.0^2 + 4.0^2} = 5.0\\text{ rad/s}$$\n\n2. **Relative angular acceleration:**\n   Although $\\omega_1$ and $\\omega_2$ are constant in the laboratory frame, in the rotating frame of body 2, the vector $\\vec{\\omega}_1$ changes direction due to rotation $\\vec{\\omega}_2$:\n   $$\\vec{\\beta}_{\\text{rel}} = \\left.\\frac{d\\vec{\\omega}_{\\text{rel}}}{dt}\\right|_{\\text{rel}} = \\vec{\\omega}_2 \\times \\vec{\\omega}_1$$\n   Since $\\vec{\\omega}_1 \\perp \\vec{\\omega}_2$:\n   $$\\beta_{\\text{rel}} = |\\vec{\\omega}_2 \\times \\vec{\\omega}_1| = \\omega_1 \\omega_2$$\n   $$\\beta_{\\text{rel}} = 3.0 \\times 4.0 = 12\\text{ rad/s}^2$$",
        "tags": ["kinematics", "rotational kinematics", "vectors", "relative rotation"]
    },
    {
        "id": "1.56",
        "title": "Time-Dependent Angular Velocity Vector omega = at i + bt^2 j",
        "difficulty": 2,
        "question": "A solid body rotates with angular velocity $\\vec{\\omega} = at\\hat{i} + bt^2\\hat{j}$, where $a = 0.50\\text{ rad/s}^2$, $b = 0.060\\text{ rad/s}^3$, and $\\hat{i}$, $\\hat{j}$ are unit vectors along $x$ and $y$. Find:\n(a) the moduli of the angular velocity and angular acceleration at $t = 10.0\\text{ s}$;\n(b) the angle between the vectors of angular velocity and angular acceleration at that moment.",
        "hints": [
            "Differentiate $\\vec{\\omega}(t)$ with respect to time to find $\\vec{\\beta}(t) = a\\hat{i} + 2bt\\hat{j}$.",
            "Calculate magnitudes at $t = 10.0\\text{ s}$.",
            "Use scalar product formula $\\cos\\theta = \\frac{\\vec{\\omega}\\cdot\\vec{\\beta}}{\\omega\\beta}$."
        ],
        "answer": "(a) $\\omega = 7.8\\text{ rad/s}$, $\\beta = 1.3\\text{ rad/s}^2$; (b) $\\theta \\approx 17^\\circ$",
        "solution": "**(a) Moduli of angular velocity and acceleration at $t = 10.0\\text{ s}$:**\n$$\\vec{\\omega}(t) = at\\hat{i} + bt^2\\hat{j}$$\nAt $t = 10.0\\text{ s}$:\n$$\\omega_x = 0.50 \\times 10.0 = 5.0\\text{ rad/s}$$\n$$\\omega_y = 0.060 \\times 10.0^2 = 6.0\\text{ rad/s}$$\n$$\\omega = \\sqrt{5.0^2 + 6.0^2} = \\sqrt{25 + 36} = \\sqrt{61} \\approx 7.81\\text{ rad/s} \\approx 7.8\\text{ rad/s}$$\n\nAngular acceleration:\n$$\\vec{\\beta} = \\frac{d\\vec{\\omega}}{dt} = a\\hat{i} + 2bt\\hat{j}$$\nAt $t = 10.0\\text{ s}$:\n$$\\beta_x = 0.50\\text{ rad/s}^2$$\n$$\\beta_y = 2(0.060)(10.0) = 1.20\\text{ rad/s}^2$$\n$$\\beta = \\sqrt{0.50^2 + 1.20^2} = \\sqrt{0.25 + 1.44} = \\sqrt{1.69} = 1.30\\text{ rad/s}^2$$\n\n**(b) Angle $\\theta$ between $\\vec{\\omega}$ and $\\vec{\\beta}$:**\n$$\\vec{\\omega} \\cdot \\vec{\\beta} = \\omega_x \\beta_x + \\omega_y \\beta_y = (5.0)(0.50) + (6.0)(1.20) = 2.5 + 7.2 = 9.7$$\n$$\\cos\\theta = \\frac{\\vec{\\omega} \\cdot \\vec{\\beta}}{\\omega \\beta} = \\frac{9.7}{7.81 \\times 1.30} = \\frac{9.7}{10.153} \\approx 0.9554$$\n$$\\theta = \\arccos(0.9554) \\approx 17.2^\\circ \\approx 17^\\circ$$",
        "tags": ["kinematics", "rotational kinematics", "vectors"]
    },
    {
        "id": "1.57",
        "title": "Rolling Cone Angular Velocity and Acceleration",
        "difficulty": 3,
        "question": "A round cone with half-angle $\\alpha = 30^\\circ$ and base radius $R = 5.0\\text{ cm}$ rolls uniformly and without slipping over a horizontal plane. The cone apex is hinged at point $O$ which is on the same horizontal level as point $C$, the cone base centre. The velocity of point $C$ is $v = 10.0\\text{ cm/s}$. Find the moduli of:\n(a) the vector of angular velocity of the cone and the angle it forms with the vertical;\n(b) the vector of angular acceleration of the cone.",
        "hints": [
            "In rolling without slipping, the line of contact with the table is the instantaneous axis of rotation.",
            "The angular velocity vector $\\vec{\\omega}$ must lie along this contact generator line.",
            "The center $C$ is at distance $R\\cot\\alpha$ from apex $O$ and rotates around vertical axis with precession rate $\\omega_0 = v / (R\\cot\\alpha)$."
        ],
        "answer": "(a) $\\omega = \\frac{v}{R\\cos\\alpha} = 2.3\\text{ rad/s}$, forming $60^\\circ$ with vertical; (b) $\\beta = \\frac{v^2}{R^2}\\tan\\alpha = 2.3\\text{ rad/s}^2$",
        "solution": "1. **Instantaneous axis of rotation and angular velocity:**\n   Because the cone rolls without slipping on the horizontal surface and its vertex $O$ is fixed, the generator line of the cone in contact with the table is momentarily at rest. Therefore, the contact line is the instantaneous axis of rotation.\n   The angular velocity vector $\\vec{\\omega}$ lies along this contact line, which is inclined at angle $\\alpha = 30^\\circ$ to the cone axis $OC$.\n   Since the axis $OC$ is horizontal, the contact line makes an angle of $90^\\circ - \\alpha = 60^\\circ$ with the vertical.\n   \n   The velocity of the center of the base $C$ is:\n   $$v = \\omega \\cdot d$$\n   where $d = R\\cos\\alpha$ is the perpendicular distance from $C$ to the instantaneous rotation axis.\n   $$\\omega = \\frac{v}{R\\cos\\alpha}$$\n   **Numerical value:**\n   $$\\omega = \\frac{10.0}{5.0 \\times \\cos 30^\\circ} = \\frac{2.0}{0.866} \\approx 2.31\\text{ rad/s} \\approx 2.3\\text{ rad/s}$$\n\n2. **Angular acceleration:**\n   The instantaneous axis of rotation rotates in the horizontal plane about the vertical axis passing through $O$ with precession angular velocity:\n   $$\\omega_0 = \\frac{v}{L} = \\frac{v}{R\\cot\\alpha} = \\frac{v\\tan\\alpha}{R}$$\n   The vector $\\vec{\\omega}$ changes direction with angular velocity $\\vec{\\omega}_0$:\n   $$\\vec{\\beta} = \\frac{d\\vec{\\omega}}{dt} = \\vec{\\omega}_0 \\times \\vec{\\omega}$$\n   Since $\\vec{\\omega}_0$ is vertical and $\\vec{\\omega}$ is horizontal (in contact plane), $|\\vec{\\omega}_0 \\times \\vec{\\omega}| = \\omega_0 \\omega\\sin(90^\\circ - \\alpha)$ or directly:\n   $$\\beta = \\omega_0 \\cdot \\omega\\sin(90^\\circ) \\cos\\alpha = \\left(\\frac{v\\tan\\alpha}{R}\\right)\\left(\\frac{v}{R\\cos\\alpha}\\right)\\cos\\alpha = \\frac{v^2}{R^2}\\tan\\alpha$$\n   **Numerical value:**\n   $$\\beta = \\frac{10.0^2}{5.0^2} \\times \\tan 30^\\circ = 4.0 \\times 0.5774 \\approx 2.31\\text{ rad/s}^2 \\approx 2.3\\text{ rad/s}^2$$",
        "tags": ["kinematics", "rolling cone", "3D rotation", "precession"]
    },
    {
        "id": "1.58",
        "title": "Gyroscopic Precession: Rotation about Horizontal Axis",
        "difficulty": 3,
        "question": "A solid body rotates with a constant angular velocity $\\omega_1 = 0.50\\text{ rad/s}$ about a horizontal axis $AB$. At the moment $t = 0$ the axis $AB$ starts turning about the vertical with a constant angular acceleration $\\beta_2 = 0.10\\text{ rad/s}^2$. Find the angular velocity and angular acceleration of the body after $t = 3.5\\text{ s}$.",
        "hints": [
            "Express the total angular velocity as $\\vec{\\omega}(t) = \\vec{\\omega}_1(t) + \\vec{\\omega}_2(t)$, where $\\vec{\\omega}_1$ is horizontal and $\\vec{\\omega}_2 = \\beta_2 t\\hat{k}$ is vertical.",
            "Since $\\vec{\\omega}_1 \\perp \\vec{\\omega}_2$, use the Pythagorean theorem for the magnitude of $\\vec{\\omega}$.",
            "Differentiate the vector $\\vec{\\omega}$ taking into account the rotation of the horizontal axis $\\frac{d\\vec{\\omega}_1}{dt} = \\vec{\\omega}_2 \\times \\vec{\\omega}_1$."
        ],
        "answer": "$\\omega = \\sqrt{\\omega_1^2 + (\\beta_2 t)^2} = 0.60\\text{ rad/s}$, $\\beta = \\sqrt{\\beta_2^2 + (\\omega_1 \\beta_2 t)^2} = 0.20\\text{ rad/s}^2$",
        "solution": "1. **Total Angular Velocity Vector:**\n   $$\\vec{\\omega}(t) = \\vec{\\omega}_1(t) + \\vec{\\omega}_2(t)$$\n   - $\\vec{\\omega}_1(t)$ lies in the horizontal plane with constant magnitude $\\omega_1 = 0.50\\text{ rad/s}$.\n   - $\\vec{\\omega}_2(t) = \\beta_2 t\\hat{k}$ points vertically with magnitude $\\omega_2(t) = \\beta_2 t$.\n   Since $\\vec{\\omega}_1 \\perp \\vec{\\omega}_2$ at all times:\n   $$\\omega(t) = \\sqrt{\\omega_1^2 + (\\beta_2 t)^2}$$\n   **Numerical value at $t = 3.5\\text{ s}$:**\n   $$\\omega_2 = 0.10 \\times 3.5 = 0.35\\text{ rad/s}$$\n   $$\\omega = \\sqrt{0.50^2 + 0.35^2} = \\sqrt{0.25 + 0.1225} = \\sqrt{0.3725} \\approx 0.61\\text{ rad/s} \\approx 0.6\\text{ rad/s}$$\n\n2. **Angular Acceleration Vector:**\n   $$\\vec{\\beta} = \\frac{d\\vec{\\omega}}{dt} = \\frac{d\\vec{\\omega}_1}{dt} + \\frac{d\\vec{\\omega}_2}{dt}$$\n   - The horizontal axis $AB$ rotates with angular velocity $\\vec{\\omega}_2$, so:\n     $$\\frac{d\\vec{\\omega}_1}{dt} = \\vec{\\omega}_2 \\times \\vec{\\omega}_1$$\n     Its magnitude is $\\omega_2 \\omega_1 = \\beta_2 t \\omega_1$, and it points horizontally perpendicular to $\\vec{\\omega}_1$.\n   - The vertical component acceleration is:\n     $$\\frac{d\\vec{\\omega}_2}{dt} = \\beta_2\\hat{k}$$\n     which points vertically.\n   Since the horizontal vector $\\vec{\\omega}_2 \\times \\vec{\\omega}_1$ is orthogonal to the vertical vector $\\beta_2\\hat{k}$:\n   $$\\beta = \\sqrt{\\beta_2^2 + (\\omega_1 \\beta_2 t)^2}$$\n   **Numerical value at $t = 3.5\\text{ s}$:**\n   $$\\omega_1 \\beta_2 t = 0.50 \\times 0.10 \\times 3.5 = 0.175\\text{ rad/s}^2$$\n   $$\\beta = \\sqrt{0.10^2 + 0.175^2} = \\sqrt{0.01 + 0.0306} = \\sqrt{0.0406} \\approx 0.20\\text{ rad/s}^2$$",
        "tags": ["kinematics", "3D rotation", "angular acceleration", "vectors"]
    }
]
