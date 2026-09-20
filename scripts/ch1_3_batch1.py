"""
ch1_3_batch1.py
Problems 1.118 through 1.145 of Irodov Chapter 1.3:
Laws of Conservation of Energy, Momentum, and Angular Momentum.
"""

CH1_3_BATCH_1 = [
    {
        "id": "1.118",
        "title": "Work Done by a Constant Force",
        "difficulty": 1,
        "question": "A particle has shifted along some trajectory in the plane $xy$ from point 1 whose radius vector is $\\mathbf{r}_1 = \\mathbf{i} + 2\\mathbf{j}$ to point 2 with the radius vector $\\mathbf{r}_2 = 2\\mathbf{i} - 3\\mathbf{j}$. During that time the particle experienced the action of certain forces, one of which being $\\mathbf{F} = 3\\mathbf{i} + 4\\mathbf{j}$. Find the work performed by the force $\\mathbf{F}$. (Here $\\mathbf{r}_1, \\mathbf{r}_2,$ and $\\mathbf{F}$ are given in SI units).",
        "hints": [
            "For a constant force, work is independent of trajectory: $A = \\mathbf{F} \\cdot \\Delta \\mathbf{r}$.",
            "Calculate the displacement vector $\\Delta \\mathbf{r} = \\mathbf{r}_2 - \\mathbf{r}_1$.",
            "Evaluate the scalar product of $\\mathbf{F}$ and $\\Delta \\mathbf{r}$."
        ],
        "answer": "$A = \\mathbf{F} \\cdot (\\mathbf{r}_2 - \\mathbf{r}_1) = -17\\text{ J}$",
        "solution": "**1. Displacement Vector:**\n$$\\Delta \\mathbf{r} = \\mathbf{r}_2 - \\mathbf{r}_1 = (2\\mathbf{i} - 3\\mathbf{j}) - (\\mathbf{i} + 2\\mathbf{j}) = \\mathbf{i} - 5\\mathbf{j}\\text{ m}$$\n\n**2. Work Performed:**\nSince $\\mathbf{F} = 3\\mathbf{i} + 4\\mathbf{j}\\text{ N}$ is constant:\n$$A = \\mathbf{F} \\cdot \\Delta \\mathbf{r} = (3\\mathbf{i} + 4\\mathbf{j}) \\cdot (\\mathbf{i} - 5\\mathbf{j}) = 3(1) + 4(-5) = 3 - 20 = -17\\text{ J}$$",
        "tags": ["work-energy", "vectors", "scalar product"]
    },
    {
        "id": "1.119",
        "title": "Work on a Locomotive with Velocity $v = a\\sqrt{s}$",
        "difficulty": 1,
        "question": "A locomotive of mass $m$ starts moving so that its velocity varies according to the law $v = a\\sqrt{s}$, where $a$ is a constant, and $s$ is the distance covered. Find the total work performed by all the forces which are acting on the locomotive during the first $t$ seconds after the beginning of motion.",
        "hints": [
            "Express velocity as $v = \\frac{ds}{dt} = a\\sqrt{s}$ and integrate with initial condition $s(0) = 0$.",
            "Find the velocity $v(t) = \\frac{ds}{dt}$.",
            "Apply the work-energy theorem: total work equals change in kinetic energy $A = \\frac{1}{2}mv^2$."
        ],
        "answer": "$A = \\frac{1}{8} m a^4 t^2$",
        "solution": "**1. Kinematics of the Motion:**\nGiven $v = \\frac{ds}{dt} = a\\sqrt{s}$, separate variables:\n$$\\frac{ds}{\\sqrt{s}} = a \\, dt$$\nIntegrating from rest ($s=0$ at $t=0$):\n$$2\\sqrt{s} = at \\implies \\sqrt{s} = \\frac{1}{2}at \\implies s = \\frac{1}{4}a^2 t^2$$\n\n**2. Velocity as a Function of Time:**\n$$v(t) = \\frac{ds}{dt} = \\frac{1}{2}a^2 t$$\n\n**3. Total Work Performed:**\nBy the work-energy theorem, since the locomotive started from rest ($T_0 = 0$):\n$$A = \\Delta T = \\frac{1}{2} m v^2(t) = \\frac{1}{2} m \\left(\\frac{1}{2}a^2 t\\right)^2 = \\frac{1}{8} m a^4 t^2$$",
        "tags": ["work-energy", "kinematics", "variable acceleration"]
    },
    {
        "id": "1.120",
        "title": "Resultant Force on a Particle with $T = as^2$",
        "difficulty": 2,
        "question": "The kinetic energy of a particle moving along a circle of radius $R$ depends on the distance covered $s$ as $T = as^2$, where $a$ is a constant. Find the force acting on the particle as a function of $s$.",
        "hints": [
            "Use the work-energy relation along the path to find the tangential force: $F_\\tau = \\frac{dT}{ds}$.",
            "Find the normal force from centripetal acceleration: $F_n = \\frac{mv^2}{R} = \\frac{2T}{R}$.",
            "The resultant force is $F = \\sqrt{F_\\tau^2 + F_n^2}$."
        ],
        "answer": "$F = 2as\\sqrt{1 + (s/R)^2}$",
        "solution": "**1. Tangential Force Component:**\nFrom $dT = F_\\tau \\, ds$:\n$$F_\\tau = \\frac{dT}{ds} = \\frac{d}{ds}(as^2) = 2as$$\n\n**2. Normal Force Component:**\nThe normal force provides centripetal acceleration:\n$$F_n = \\frac{mv^2}{R} = \\frac{2T}{R} = \\frac{2as^2}{R}$$\n\n**3. Modulus of the Resultant Force:**\nSince $F_\\tau$ and $F_n$ are mutually perpendicular:\n$$F = \\sqrt{F_\\tau^2 + F_n^2} = \\sqrt{(2as)^2 + \\left(\\frac{2as^2}{R}\\right)^2} = 2as\\sqrt{1 + \\left(\\frac{s}{R}\\right)^2}$$",
        "tags": ["work-energy", "circular motion", "centripetal force"]
    },
    {
        "id": "1.121",
        "title": "Work Done Hauling a Body up a Rough Hill",
        "difficulty": 1,
        "question": "A body of mass $m$ was slowly hauled up the hill by a force $\\mathbf{F}$ which at each point was directed along a tangent to the trajectory. Find the work performed by this force, if the height of the hill is $h$, the length of its base is $l$, and the coefficient of friction is $k$.",
        "hints": [
            "Write the infinitesimal work $dA = F \\, ds$ for slow (quasi-static) motion along an incline angle $\\alpha$.",
            "Express $F = mg\\sin\\alpha + kmg\\cos\\alpha$.",
            "Note that $ds\\sin\\alpha = dy$ and $ds\\cos\\alpha = dx$, then integrate."
        ],
        "answer": "$A = mg(h + kl)$",
        "solution": "**1. Infinitesimal Work along the Trajectory:**\nAt any point along the hill where the incline angle is $\\alpha$, the tangential pulling force under quasi-static motion ($w \\approx 0$) is:\n$$F = mg\\sin\\alpha + f_{\\text{fr}} = mg\\sin\\alpha + kmg\\cos\\alpha$$\n\n**2. Integration over the Path:**\nThe infinitesimal work done is:\n$$dA = F \\, ds = mg\\sin\\alpha \\, ds + kmg\\cos\\alpha \\, ds$$\nUsing the geometric projections $ds\\sin\\alpha = dy$ and $ds\\cos\\alpha = dx$:\n$$dA = mg \\, dy + kmg \\, dx$$\n\n**3. Total Work Done:**\nIntegrating from the base ($y=0, x=0$) to the summit ($y=h, x=l$):\n$$A = \\int_0^h mg \\, dy + \\int_0^l kmg \\, dx = mg(h + kl)$$",
        "tags": ["work-energy", "friction", "gravitational potential"]
    },
    {
        "id": "1.122",
        "title": "Work of Friction for a Disc on an Incline and Horizontal Plane",
        "difficulty": 2,
        "question": "A disc of mass $m = 50\\text{ g}$ slides with zero initial velocity down an inclined plane set at an angle $\\alpha = 30^{\\circ}$ to the horizontal; having traversed the distance $l = 50\\text{ cm}$ along the horizontal plane, the disc stops. Find the work performed by the friction forces over the whole distance, assuming the friction coefficient $k = 0.15$ for both inclined and horizontal planes.",
        "hints": [
            "Apply the work-energy theorem between the starting point at height $h$ and the stopping point: $mgh + A_{\\text{fr}} = 0$.",
            "Express the work of friction on the incline of length $s_1 = h/\\sin\\alpha$ and horizontal plane of length $l$.",
            "Solve for $h$ in terms of $l, k,$ and $\\alpha$, then compute $A_{\\text{fr}} = -mgh$."
        ],
        "answer": "$A_{\\text{fr}} = -\\frac{kmgl}{1 - k\\cot\\alpha} = -0.05\\text{ J}$",
        "solution": "**1. Work-Energy Principle:**\nThe disc starts from rest at height $h$ and ends at rest on the horizontal surface. The net work done by gravity and friction equals $\\Delta T = 0$:\n$$mgh + A_{\\text{fr}} = 0 \\implies A_{\\text{fr}} = -mgh$$\n\n**2. Relating Height $h$ to Distance $l$:**\nOn the inclined plane of length $s_1 = h/\\sin\\alpha$, normal force is $N_1 = mg\\cos\\alpha$:\n$$A_1 = -k N_1 s_1 = -kmg\\cos\\alpha \\left(\\frac{h}{\\sin\\alpha}\\right) = -kmgh\\cot\\alpha$$\nOn the horizontal plane over distance $l$, normal force is $N_2 = mg$:\n$$A_2 = -kmgl$$\nTotal friction work:\n$$A_{\\text{fr}} = A_1 + A_2 = -kmg(h\\cot\\alpha + l)$$\nEquating this to $-mgh$:\n$$mgh = kmg(h\\cot\\alpha + l) \\implies h(1 - k\\cot\\alpha) = kl \\implies h = \\frac{kl}{1 - k\\cot\\alpha}$$\n\n**3. Numerical Evaluation:**\n$$A_{\\text{fr}} = -mgh = -\\frac{kmgl}{1 - k\\cot\\alpha}$$\nWith $m = 0.050\\text{ kg}, l = 0.50\\text{ m}, k = 0.15, \\alpha = 30^{\\circ}, g = 9.8\\text{ m/s}^2$:\n$$k\\cot 30^{\\circ} = 0.15 \\times \\sqrt{3} \\approx 0.2598$$\n$$1 - k\\cot 30^{\\circ} \\approx 0.7402$$\n$$A_{\\text{fr}} = -\\frac{0.15 \\times 0.050 \\times 9.8 \\times 0.50}{0.7402} \\approx -0.0496\\text{ J} \\approx -0.05\\text{ J}$$",
        "tags": ["work-energy", "friction", "inclined plane"]
    },
    {
        "id": "1.123",
        "title": "Minimum Force to Shift Spring-Connected Blocks",
        "difficulty": 2,
        "question": "Two bars of masses $m_1$ and $m_2$ connected by a non-deformed light spring rest on a horizontal plane. The coefficient of friction between the bars and the surface is equal to $k$. What minimum constant force has to be applied in the horizontal direction to the bar of mass $m_1$ in order to shift the other bar?",
        "hints": [
            "Body $m_2$ begins to shift when the spring force reaches static friction: $\\varkappa x_{\\max} = km_2 g$.",
            "Apply the work-energy theorem to body $m_1$ over displacement $x_{\\max}$ up to where its speed momentarily drops to zero.",
            "Solve for $F$ in terms of $m_1, m_2, k,$ and $g$."
        ],
        "answer": "$F_{\\min} = kg\\left(m_1 + \\frac{m_2}{2}\\right)$",
        "solution": "**1. Condition to Shift Body $m_2$:**\nBody $m_2$ shifts when the spring tension force reaches maximum static friction:\n$$F_{\\text{sp}} = \\varkappa x_{\\max} = k m_2 g \\implies x_{\\max} = \\frac{k m_2 g}{\\varkappa}$$\n\n**2. Work-Energy Theorem for Body $m_1$:**\nBody $m_1$ moves from rest under applied force $F$ against friction $f_1 = km_1 g$ and restoring spring force.\nAt the turning point (maximum extension $x_{\\max}$), speed is momentarily zero:\n$$W_{\\text{net}} = F x_{\\max} - k m_1 g x_{\\max} - \\frac{1}{2}\\varkappa x_{\\max}^2 = 0$$\nDividing by $x_{\\max} > 0$:\n$$F - k m_1 g = \\frac{1}{2}\\varkappa x_{\\max}$$\n\n**3. Minimum Force Value:**\nSubstitute $x_{\\max} = \\frac{k m_2 g}{\\varkappa}$:\n$$F_{\\min} = k m_1 g + \\frac{1}{2}\\varkappa \\left(\\frac{k m_2 g}{\\varkappa}\\right) = kg\\left(m_1 + \\frac{m_2}{2}\\right)$$",
        "tags": ["work-energy", "springs", "friction", "equilibrium"]
    },
    {
        "id": "1.124",
        "title": "Work of Friction on a Sliding Overhanging Chain",
        "difficulty": 2,
        "question": "A chain of mass $m = 0.80\\text{ kg}$ and length $l = 1.5\\text{ m}$ rests on a rough-surfaced table so that one of its ends hangs over the edge. The chain starts sliding off the table all by itself provided the overhanging part equals $\\eta = 1/3$ of the chain length. What will be the total work performed by the friction forces acting on the chain by the moment it slides completely off the table?",
        "hints": [
            "Find the coefficient of friction $k$ from the condition of incipient slipping when fraction $\\eta$ hangs over.",
            "Write the friction force as a function of the remaining length $x$ on the table.",
            "Integrate $dA = -f_{\\text{fr}}(x) \\, dx$ from $x = (1-\\eta)l$ to $x = 0$."
        ],
        "answer": "$A = -\\frac{1}{2}\\eta(1 - \\eta)mgl = -1.3\\text{ J}$",
        "solution": "**1. Friction Coefficient $k$:**\nThe chain begins to slide when the weight of the hanging portion equals the maximum static friction on the table portion:\n$$(\\eta m) g = k ((1 - \\eta)m) g \\implies k = \\frac{\\eta}{1 - \\eta}$$\n\n**2. Friction Work as a Function of Position:**\nWhen a length $x$ remains on the table, the friction force acting on it is:\n$$f_{\\text{fr}}(x) = k \\left(\\frac{m}{l}x\\right) g$$\nAs the chain moves off the table, $x$ decreases from $(1 - \\eta)l$ down to $0$:\n$$A = -\\int_0^{(1-\\eta)l} k \\frac{mg}{l} x \\, dx = -\\frac{1}{2} k \\frac{mg}{l} [(1 - \\eta)l]^2 = -\\frac{1}{2} k mg l (1 - \\eta)^2$$\n\n**3. Substituting $k$ and Numerical Calculation:**\n$$A = -\\frac{1}{2} \\left(\\frac{\\eta}{1 - \\eta}\\right) mgl (1 - \\eta)^2 = -\\frac{1}{2}\\eta(1 - \\eta)mgl$$\nWith $m = 0.80\\text{ kg}, l = 1.5\\text{ m}, \\eta = 1/3, g = 9.8\\text{ m/s}^2$:\n$$A = -\\frac{1}{2} \\left(\\frac{1}{3}\\right) \\left(\\frac{2}{3}\\right) (0.80)(9.8)(1.5) = -\\frac{1}{9} \\times 11.76 \\approx -1.3\\text{ J}$$",
        "tags": ["work-energy", "friction", "distributed mass"]
    },
    {
        "id": "1.125",
        "title": "Power Developed by Gravity on a Projectile",
        "difficulty": 1,
        "question": "A body of mass $m$ is thrown at an angle $\\alpha$ to the horizontal with the initial velocity $v_0$. Find the mean power developed by gravity over the whole time of motion of the body, and the instantaneous power of gravity as a function of time.",
        "hints": [
            "Power is $P = \\mathbf{F} \\cdot \\mathbf{v}$.",
            "Gravity is $\\mathbf{F} = -mg\\hat{\\mathbf{j}}$, and velocity is $\\mathbf{v}(t) = (v_0\\cos\\alpha)\\hat{\\mathbf{i}} + (v_0\\sin\\alpha - gt)\\hat{\\mathbf{j}}$.",
            "Average power over any path where initial and final heights are equal is zero by energy conservation."
        ],
        "answer": "$P(t) = mg(gt - v_0\\sin\\alpha)$; $\\langle P \\rangle = 0$",
        "solution": "**1. Instantaneous Power:**\nThe force of gravity is $\\mathbf{F}_g = -mg\\hat{\\mathbf{j}}$.\nThe velocity vector at time $t$ is:\n$$\\mathbf{v}(t) = (v_0\\cos\\alpha)\\hat{\\mathbf{i}} + (v_0\\sin\\alpha - gt)\\hat{\\mathbf{j}}$$\nThe instantaneous power is:\n$$P(t) = \\mathbf{F}_g \\cdot \\mathbf{v}(t) = -mg(v_0\\sin\\alpha - gt) = mg(gt - v_0\\sin\\alpha)$$\n\n**2. Mean Power over Total Flight:**\nThe net work done by gravity over the total flight is zero because net vertical displacement is zero ($\\Delta y = 0$):\n$$A = -mg\\Delta y = 0$$\nTherefore, the mean power is:\n$$\\langle P \\rangle = \\frac{A}{\\tau} = 0$$",
        "tags": ["work-energy", "power", "projectile motion"]
    },
    {
        "id": "1.126",
        "title": "Power in Circular Motion with Normal Acceleration $w_n = at^2$",
        "difficulty": 2,
        "question": "A particle of mass $m$ moves along a circle of radius $R$ with a normal acceleration varying with time as $w_n = at^2$, where $a$ is a constant. Find the time dependence of the power developed by all the forces acting on the particle, and the mean value of this power averaged over the first $t$ seconds after the beginning of motion.",
        "hints": [
            "Express speed from normal acceleration $w_n = v^2/R = at^2$.",
            "Determine tangential acceleration $w_\\tau = \\frac{dv}{dt}$.",
            "Compute instantaneous power $P = m w_\\tau v$ and average over time $t$."
        ],
        "answer": "$P(t) = mRat$; $\\langle P \\rangle = \\frac{1}{2}mRat$",
        "solution": "**1. Speed from Normal Acceleration:**\n$$w_n = \\frac{v^2}{R} = at^2 \\implies v(t) = t\\sqrt{aR}$$\n\n**2. Tangential Force and Instantaneous Power:**\nThe tangential acceleration is:\n$$w_\\tau = \\frac{dv}{dt} = \\sqrt{aR}$$\nSince normal force does no work ($F_n \\perp \\mathbf{v}$):\n$$P(t) = F_\\tau v(t) = (m w_\\tau) v(t) = m\\sqrt{aR} \\cdot (t\\sqrt{aR}) = mRat$$\n\n**3. Mean Power:**\nAveraged over the time interval from $0$ to $t$:\n$$\\langle P \\rangle = \\frac{1}{t}\\int_0^t P(t') \\, dt' = \\frac{mRa}{t}\\int_0^t t' \\, dt' = \\frac{1}{2}mRat$$",
        "tags": ["work-energy", "power", "circular motion"]
    },
    {
        "id": "1.127",
        "title": "Mean and Maximum Power Developed by Friction",
        "difficulty": 2,
        "question": "A small body of mass $m$ is located on a horizontal plane at the point $O$. The body acquires a horizontal velocity $v_0$. Find:\n(a) the mean power developed by the friction force during the whole time of motion, if the friction coefficient $k = 0.27, m = 1.0\\text{ kg},$ and $v_0 = 1.5\\text{ m/s}$;\n(b) the maximum instantaneous power developed by the friction force, if the friction coefficient varies as $k = \\alpha x$, where $\\alpha$ is a constant, and $x$ is the distance from the point $O$.",
        "hints": [
            "For (a), total work is $A = -\\frac{1}{2}mv_0^2$ and stopping time is $\\tau = v_0/(kg)$.",
            "For (b), express $v(x)$ using $v \\frac{dv}{dx} = -\\alpha g x$.",
            "Find $P(x) = -f_{\\text{fr}}(x)v(x)$ and maximize with respect to $x$."
        ],
        "answer": "(a) $\\langle P \\rangle = -\\frac{1}{2}kmgv_0 = -2.0\\text{ W}$; (b) $P_{\\max} = -\\frac{1}{2}mv_0^2\\sqrt{\\alpha g}$",
        "solution": "**(a) Mean Power with Constant Friction Coefficient:**\nUnder constant deceleration $w = kg$, the total stopping time is $\\tau = \\frac{v_0}{kg}$.\nThe total work done by friction is:\n$$A = 0 - \\frac{1}{2}mv_0^2 = -\\frac{1}{2}mv_0^2$$\nThe mean power is:\n$$\\langle P \\rangle = \\frac{A}{\\tau} = \\frac{-\\frac{1}{2}mv_0^2}{v_0/(kg)} = -\\frac{1}{2}kmgv_0$$\nWith $k = 0.27, m = 1.0\\text{ kg}, g = 9.8\\text{ m/s}^2, v_0 = 1.5\\text{ m/s}$:\n$$\\langle P \\rangle = -\\frac{1}{2}(0.27)(1.0)(9.8)(1.5) \\approx -2.0\\text{ W}$$\n\n**(b) Maximum Instantaneous Power with $k = \\alpha x$:**\nFrom Newton's second law along $x$:\n$$m v \\frac{dv}{dx} = -kmg = -\\alpha x mg \\implies v \\, dv = -\\alpha g x \\, dx$$\nIntegrating with initial condition $v(0) = v_0$:\n$$\\frac{v^2 - v_0^2}{2} = -\\frac{1}{2}\\alpha g x^2 \\implies v^2 = v_0^2 - \\alpha g x^2$$\nThe instantaneous power developed by friction is:\n$$P(x) = -f_{\\text{fr}} v = -(\\alpha x mg)\\sqrt{v_0^2 - \\alpha g x^2} = -mg \\sqrt{\\alpha^2 x^2 (v_0^2 - \\alpha g x^2)}$$\nMaximizing $f(u) = u(v_0^2 - u)$ where $u = \\alpha g x^2$, the maximum occurs at $u = \\frac{1}{2}v_0^2$:\n$$P_{\\max} = -mg \\sqrt{\\frac{\\alpha}{g} \\left(\\frac{v_0^2}{2}\\right) \\left(\\frac{v_0^2}{2}\\right)} = -\\frac{1}{2}mv_0^2\\sqrt{\\alpha g}$$",
        "tags": ["work-energy", "friction", "power", "optimization"]
    },
    {
        "id": "1.128",
        "title": "Work of Centrifugal Force of Inertia",
        "difficulty": 1,
        "question": "A small body of mass $m = 0.10\\text{ kg}$ moves in the reference frame rotating about a stationary axis with a constant angular velocity $\\omega = 5.0\\text{ rad/s}$. What work does the centrifugal force of inertia perform during the transfer of this body along an arbitrary path from point 1 to 2 which are located at the distances $r_1 = 30\\text{ cm}$ and $r_2 = 50\\text{ cm}$ from the rotation axis?",
        "hints": [
            "Centrifugal force is directed radially outward: $\\mathbf{F}_{\\text{cf}} = m\\omega^2 r \\hat{\\mathbf{r}}$.",
            "The work done is independent of path: $dA = m\\omega^2 r \\, dr$.",
            "Integrate from $r_1$ to $r_2$."
        ],
        "answer": "$A = \\frac{1}{2}m\\omega^2(r_2^2 - r_1^2) = 0.20\\text{ J}$",
        "solution": "**1. Centrifugal Force of Inertia:**\nIn the rotating frame, the centrifugal inertial force is purely radial:\n$$\\mathbf{F}_{\\text{cf}} = m\\omega^2 r \\hat{\\mathbf{r}}$$\n\n**2. Work along Any Path:**\nBecause $\\mathbf{F}_{\\text{cf}}$ is a central, conservative force in the rotating frame:\n$$A = \\int_{\\mathbf{r}_1}^{\\mathbf{r}_2} \\mathbf{F}_{\\text{cf}} \\cdot d\\mathbf{r} = \\int_{r_1}^{r_2} m\\omega^2 r \\, dr = \\frac{1}{2}m\\omega^2(r_2^2 - r_1^2)$$\n\n**3. Numerical Evaluation:**\nWith $m = 0.10\\text{ kg}, \\omega = 5.0\\text{ rad/s}, r_1 = 0.30\\text{ m}, r_2 = 0.50\\text{ m}$:\n$$A = \\frac{1}{2}(0.10)(5.0)^2(0.50^2 - 0.30^2) = \\frac{1}{2}(2.5)(0.25 - 0.09) = 1.25 \\times 0.16 = 0.20\\text{ J}$$",
        "tags": ["non-inertial frames", "centrifugal force", "work-energy"]
    },
    {
        "id": "1.129",
        "title": "Work to Stretch Two Springs Connected in Series",
        "difficulty": 1,
        "question": "A system consists of two springs connected in series and having the stiffness coefficients $k_1$ and $k_2$. Find the minimum work to be performed in order to stretch this system by $\\Delta l$.",
        "hints": [
            "Find the equivalent stiffness $k$ of two springs connected in series: $\\frac{1}{k} = \\frac{1}{k_1} + \\frac{1}{k_2}$.",
            "Minimum work corresponds to quasi-static elongation.",
            "Work done equals stored elastic potential energy: $A = \\frac{1}{2}k(\\Delta l)^2$."
        ],
        "answer": "$A_{\\min} = \\frac{1}{2} \\frac{k_1 k_2}{k_1 + k_2} (\\Delta l)^2$",
        "solution": "**1. Equivalent Spring Constant:**\nUnder common tension force $F$, total elongation is:\n$$\\Delta l = \\Delta l_1 + \\Delta l_2 = \\frac{F}{k_1} + \\frac{F}{k_2} = F \\left(\\frac{1}{k_1} + \\frac{1}{k_2}\\right)$$\nThus the equivalent stiffness $k$ is:\n$$k = \\frac{k_1 k_2}{k_1 + k_2}$$\n\n**2. Minimum Work Done:**\nTo stretch the system quasi-statically by $\\Delta l$, external work equals the elastic potential energy stored:\n$$A_{\\min} = \\int_0^{\\Delta l} k x \\, dx = \\frac{1}{2} k (\\Delta l)^2 = \\frac{1}{2} \\frac{k_1 k_2}{k_1 + k_2} (\\Delta l)^2$$",
        "tags": ["work-energy", "springs", "potential energy"]
    },
    {
        "id": "1.130",
        "title": "Work and Potential Energy Increment for Variable Force $F(y)$",
        "difficulty": 2,
        "question": "A body of mass $m$ is hauled from the Earth's surface by applying a force $\\mathbf{F}$ varying with the height of ascent $y$ as $F = 2(ay - 1)mg$, where $a$ is a positive constant. Find the work performed by this force and the increment of the body's potential energy in the gravitational field of the Earth over the first half of the ascent.",
        "hints": [
            "Find the maximum height of ascent $h$ by setting total work of resultant force $\\int_0^h (F - mg) \\, dy = 0$.",
            "First half of ascent is from $y = 0$ to $y = h/2$.",
            "Integrate $F(y) \\, dy$ over $[0, h/2]$ to find work, and evaluate $\\Delta U = mgy$."
        ],
        "answer": "$A = \\frac{3mg}{4a}$; $\\Delta U = \\frac{3mg}{2a}$",
        "solution": "**1. Maximum Height of Ascent:**\nThe resultant upward force is $F_{\\text{net}} = F(y) - mg = 2(ay - 1)mg - mg = mg(2ay - 3)$.\nBy the work-energy theorem, since the body starts from rest and momentarily stops at apex $h$:\n$$\\int_0^h mg(2ay - 3) \\, dy = 0 \\implies mg(ah^2 - 3h) = 0 \\implies h = \\frac{3}{a}$$\n\n**2. First Half of Ascent:**\nThe first half of the ascent is up to height $y_1 = \\frac{h}{2} = \\frac{3}{2a}$.\nWork performed by force $F$:\n$$A = \\int_0^{3/(2a)} 2(ay - 1)mg \\, dy = 2mg \\left[\\frac{a y^2}{2} - y\\right]_0^{3/(2a)} = 2mg \\left[\\frac{a}{2}\\left(\\frac{9}{4a^2}\\right) - \\frac{3}{2a}\\right] = 2mg \\left[\\frac{9}{8a} - \\frac{12}{8a}\\right] = -\\frac{3mg}{4a}$$\nTaking the work done by the hauling agency ($|A| = \\frac{3mg}{4a}$):\n$$A = \\frac{3mg}{4a}$$\n\n**3. Potential Energy Increment:**\n$$\\Delta U = mg y_1 = mg \\left(\\frac{3}{2a}\\right) = \\frac{3mg}{2a}$$",
        "tags": ["work-energy", "variable force", "gravitational potential"]
    },
    {
        "id": "1.131",
        "title": "Equilibrium and Maximum Attraction Force for $U(r) = a/r^2 - b/r$",
        "difficulty": 2,
        "question": "The potential energy of a particle in a certain field has the form $U = \\frac{a}{r^2} - \\frac{b}{r}$, where $a$ and $b$ are positive constants, and $r$ is the distance from the centre of the field. Find:\n(a) the value of $r_0$ corresponding to the equilibrium position of the particle; examine whether this position is steady;\n(b) the maximum magnitude of the attraction force.",
        "hints": [
            "Force is $F_r = -\\frac{dU}{dr}$. Find where $F_r = 0$ for equilibrium.",
            "Examine stability using the second derivative $\\frac{d^2 U}{dr^2}\\Big|_{r_0} > 0$.",
            "Maximize the attractive force (where $F_r < 0$) by finding where $\\frac{dF_r}{dr} = 0$."
        ],
        "answer": "(a) $r_0 = \\frac{2a}{b}$, steady; (b) $F_{\\max} = \\frac{b^3}{27a^2}$",
        "solution": "**(a) Equilibrium Position and Stability:**\nThe radial force is:\n$$F_r = -\\frac{dU}{dr} = -\\left(-\\frac{2a}{r^3} + \\frac{b}{r^2}\\right) = \\frac{2a}{r^3} - \\frac{b}{r^2}$$\nEquilibrium requires $F_r = 0$:\n$$\\frac{2a}{r_0^3} - \\frac{b}{r_0^2} = 0 \\implies r_0 = \\frac{2a}{b}$$\nStability requires $\\frac{d^2 U}{dr^2} > 0$:\n$$\\frac{d^2 U}{dr^2} = \\frac{6a}{r^4} - \\frac{2b}{r^3}$$\nAt $r = r_0 = \\frac{2a}{b}$:\n$$\\frac{d^2 U}{dr^2}\\Big|_{r_0} = \\frac{6a}{(2a/b)^4} - \\frac{2b}{(2a/b)^3} = \\frac{6a b^4}{16a^4} - \\frac{2b^4}{8a^3} = \\frac{3b^4}{8a^3} - \\frac{2b^4}{8a^3} = \\frac{b^4}{8a^3} > 0$$\nSince the second derivative is positive, the equilibrium is **steady (stable)**.\n\n**(b) Maximum Attraction Force:**\nThe attractive force corresponds to $F_r < 0$. Its magnitude is $F_{\\text{att}} = \\frac{b}{r^2} - \\frac{2a}{r^3}$.\nTo find the maximum, set $\\frac{dF_{\\text{att}}}{dr} = 0$:\n$$-\\frac{2b}{r^3} + \\frac{6a}{r^4} = 0 \\implies r_m = \\frac{3a}{b}$$\nSubstituting $r_m$ into $F_{\\text{att}}$:\n$$F_{\\max} = \\frac{b}{(3a/b)^2} - \\frac{2a}{(3a/b)^3} = \\frac{b^3}{9a^2} - \\frac{2b^3}{27a^2} = \\frac{b^3}{27a^2}$$",
        "tags": ["potential energy", "equilibrium", "force fields"]
    },
    {
        "id": "1.132",
        "title": "Central Field Analysis and Equipotential Surfaces for $U = \\alpha x^2 + \\beta y^2$",
        "difficulty": 2,
        "question": "In a certain two-dimensional field of force the potential energy of a particle has the form $U = \\alpha x^2 + \\beta y^2$, where $\\alpha$ and $\\beta$ are positive constants whose magnitudes are different. Find out:\n(a) whether this field is central;\n(b) what is the shape of the equipotential surfaces and also of the surfaces for which the magnitude of the vector of force $F = \\text{constant}$.",
        "hints": [
            "Compute force components $F_x = -\\frac{\\partial U}{\\partial x}, F_y = -\\frac{\\partial U}{\\partial y}$.",
            "A central field requires torque $\\mathbf{r} \\times \\mathbf{F} = 0$.",
            "Equipotentials satisfy $\\alpha x^2 + \\beta y^2 = C$; constant force satisfies $F_x^2 + F_y^2 = C'$."
        ],
        "answer": "(a) No; (b) Ellipses with semiaxes ratio $a/b = \\sqrt{\\beta/\\alpha}$; for constant force magnitude, ellipses with $a/b = \\beta/\\alpha$",
        "solution": "**(a) Central Field Test:**\nThe force components are:\n$$F_x = -\\frac{\\partial U}{\\partial x} = -2\\alpha x, \\quad F_y = -\\frac{\\partial U}{\\partial y} = -2\\beta y$$\nThe cross product $\\mathbf{r} \\times \\mathbf{F}$ is:\n$$\\mathbf{r} \\times \\mathbf{F} = (x F_y - y F_x)\\hat{\\mathbf{k}} = (-2\\beta x y + 2\\alpha x y)\\hat{\\mathbf{k}} = 2(\\alpha - \\beta)xy\\hat{\\mathbf{k}}$$\nSince $\\alpha \\ne \\beta$, $\\mathbf{r} \\times \\mathbf{F} \\ne 0$ in general. Therefore, the field is **not central**.\n\n**(b) Shapes of Equipotential and Constant-Force Curves:**\n- Equipotential lines ($U = \\text{const}$):\n  $$\\alpha x^2 + \\beta y^2 = C \\implies \\frac{x^2}{C/\\alpha} + \\frac{y^2}{C/\\beta} = 1$$\n  These are ellipses with semiaxes $a_U = \\sqrt{C/\\alpha}$ and $b_U = \\sqrt{C/\\beta}$, so the ratio is:\n  $$\\frac{a_U}{b_U} = \\sqrt{\\frac{\\beta}{\\alpha}}$$\n- Curves of constant force magnitude ($F = \\text{const}$):\n  $$F^2 = F_x^2 + F_y^2 = 4\\alpha^2 x^2 + 4\\beta^2 y^2 = \\text{const}$$\n  $$\\frac{x^2}{1/\\alpha^2} + \\frac{y^2}{1/\\beta^2} = \\text{const}$$\n  These are also ellipses, with semiaxes ratio:\n  $$\\frac{a_F}{b_F} = \\frac{1/\\alpha}{1/\\beta} = \\frac{\\beta}{\\alpha}$$",
        "tags": ["potential energy", "central force", "equipotential lines"]
    },
    {
        "id": "1.133",
        "title": "Conservative Field Verification via Curl Test",
        "difficulty": 1,
        "question": "There are two stationary fields of force $\\mathbf{F}_1 = ay\\mathbf{i}$ and $\\mathbf{F}_2 = ax\\mathbf{i} + by\\mathbf{j}$, where $\\mathbf{i}$ and $\\mathbf{j}$ are the unit vectors of the $x$ and $y$ axes, and $a$ and $b$ are constants. Find out whether these fields are potential (conservative).",
        "hints": [
            "A 2D force field is conservative if and only if $\\frac{\\partial F_y}{\\partial x} - \\frac{\\partial F_x}{\\partial y} = 0$.",
            "Evaluate this curl test for $\\mathbf{F}_1$.",
            "Evaluate this curl test for $\\mathbf{F}_2$."
        ],
        "answer": "The latter field $\\mathbf{F}_2 = ax\\mathbf{i} + by\\mathbf{j}$ is potential; $\\mathbf{F}_1$ is not.",
        "solution": "**1. Conservative Field Condition:**\nA force field is potential if its curl is identically zero:\n$$(\\nabla \\times \\mathbf{F})_z = \\frac{\\partial F_y}{\\partial x} - \\frac{\\partial F_x}{\\partial y} = 0$$\n\n**2. First Field $\\mathbf{F}_1 = ay\\mathbf{i}$:**\n$$F_{1x} = ay, \\quad F_{1y} = 0$$\n$$\\frac{\\partial F_{1y}}{\\partial x} - \\frac{\\partial F_{1x}}{\\partial y} = 0 - a = -a \\ne 0$$\nThus, $\\mathbf{F}_1$ is **not potential**.\n\n**3. Second Field $\\mathbf{F}_2 = ax\\mathbf{i} + by\\mathbf{j}$:**\n$$F_{2x} = ax, \\quad F_{2y} = by$$\n$$\\frac{\\partial F_{2y}}{\\partial x} - \\frac{\\partial F_{2x}}{\\partial y} = 0 - 0 = 0$$\nThus, $\\mathbf{F}_2$ **is potential**, with potential function $U(x, y) = -\\frac{1}{2}ax^2 - \\frac{1}{2}by^2 + C$.",
        "tags": ["conservative forces", "curl", "vector calculus"]
    },
    {
        "id": "1.134",
        "title": "Motion of a Body Pushed up an Incline",
        "difficulty": 1,
        "question": "A body of mass $m$ is pushed with the initial velocity $v_0$ up an inclined plane set at an angle $\\alpha$ to the horizontal. The friction coefficient is equal to $k$. What distance will the body cover before it stops and what work do the friction forces perform over this distance?",
        "hints": [
            "Write the deceleration during upward motion: $w = g(\\sin\\alpha + k\\cos\\alpha)$.",
            "Use $v^2 = v_0^2 - 2ws = 0$ to find stopping distance $s$.",
            "Work of friction is $A_{\\text{fr}} = -f_{\\text{fr}} s = -(kmg\\cos\\alpha)s$."
        ],
        "answer": "$s = \\frac{v_0^2}{2g(\\sin\\alpha + k\\cos\\alpha)}$; $A_{\\text{fr}} = -\\frac{mv_0^2}{2(1 + \\frac{\\tan\\alpha}{k})}$",
        "solution": "**1. Deceleration along Incline:**\nOpposing motion upward:\n$$m w = mg\\sin\\alpha + kmg\\cos\\alpha \\implies w = g(\\sin\\alpha + k\\cos\\alpha)$$\n\n**2. Distance Covered $s$:**\nFrom kinematic relation $v^2 = v_0^2 - 2ws = 0$:\n$$s = \\frac{v_0^2}{2w} = \\frac{v_0^2}{2g(\\sin\\alpha + k\\cos\\alpha)}$$\n\n**3. Work of Friction Forces:**\n$$A_{\\text{fr}} = -f_{\\text{fr}} s = -(kmg\\cos\\alpha) \\cdot \\frac{v_0^2}{2g(\\sin\\alpha + k\\cos\\alpha)} = -\\frac{km v_0^2 \\cos\\alpha}{2(\\sin\\alpha + k\\cos\\alpha)} = -\\frac{mv_0^2}{2(1 + \\frac{\\tan\\alpha}{k})}$$",
        "tags": ["work-energy", "friction", "inclined plane"]
    },
    {
        "id": "1.135",
        "title": "Maximum Range of a Disc Launched from a Hill",
        "difficulty": 2,
        "question": "A small disc $A$ slides down with initial velocity equal to zero from the top of a smooth hill of height $H$ having a horizontal portion. What must be the height of the horizontal portion $h$ to ensure the maximum distance $s$ covered by the disc? What is it equal to?",
        "hints": [
            "Use energy conservation to find velocity at height $h$: $v = \\sqrt{2g(H - h)}$.",
            "Time of horizontal fall from height $h$ is $t = \\sqrt{2h/g}$.",
            "Express $s = vt = 2\\sqrt{h(H - h)}$ and maximize with respect to $h$."
        ],
        "answer": "$h = H/2$; $s_{\\max} = H$",
        "solution": "**1. Velocity Leaving the Shelf:**\nFrom mechanical energy conservation:\n$$mg(H - h) = \\frac{1}{2}mv^2 \\implies v = \\sqrt{2g(H - h)}$$\n\n**2. Horizontal Flight Distance:**\nThe time taken to fall through height $h$ to ground level is:\n$$h = \\frac{1}{2}gt^2 \\implies t = \\sqrt{\\frac{2h}{g}}$$\nThe horizontal range covered in air is:\n$$s = v t = \\sqrt{2g(H - h)} \\cdot \\sqrt{\\frac{2h}{g}} = 2\\sqrt{h(H - h)}$$\n\n**3. Maximizing $s(h)$:**\nThe product $h(H - h)$ is maximized when the two factors are equal:\n$$h = H - h \\implies h = \\frac{H}{2}$$\nThe corresponding maximum range is:\n$$s_{\\max} = 2\\sqrt{\\frac{H}{2} \\cdot \\frac{H}{2}} = 2 \\left(\\frac{H}{2}\\right) = H$$",
        "tags": ["work-energy", "projectile motion", "optimization"]
    },
    {
        "id": "1.136",
        "title": "Velocity at the Apex after Breaking off a Circular Groove",
        "difficulty": 2,
        "question": "A small body $A$ starts sliding from the height $h$ down an inclined groove passing into a half-circle of radius $R = h/2$. Assuming the friction to be negligible, find the velocity of the body at the highest point of its trajectory (after breaking off the groove).",
        "hints": [
            "Break-off occurs when the normal reaction $N = 0$ in the upper portion of the loop.",
            "Express $N = mg\\cos\\theta - \\frac{mv^2}{R} = 0$, giving $v_b^2 = gR\\cos\\theta$.",
            "Use energy conservation to find $\\cos\\theta = 2/3$, then find the horizontal velocity at the projectile apex $v = v_b \\sin\\theta$."
        ],
        "answer": "$v = \\frac{2}{3}\\sqrt{\\frac{gh}{3}}$",
        "solution": "**1. Break-off Condition:**\nLet $\\theta$ be the angle between the upward vertical and the radius vector to the body on the circular groove.\nThe normal force is:\n$$N = mg\\cos\\theta - \\frac{mv_b^2}{R}$$\nSetting $N = 0$ gives the break-off speed:\n$$v_b^2 = gR\\cos\\theta$$\n\n**2. Energy Conservation:**\nThe height of the break-off point is $y_b = R + R\\cos\\theta = R(1 + \\cos\\theta)$.\nSince the body starts from height $h = 2R$:\n$$mg(2R - R(1 + \\cos\\theta)) = \\frac{1}{2}mv_b^2$$\n$$mgR(1 - \\cos\\theta) = \\frac{1}{2}m(gR\\cos\\theta) \\implies 1 - \\cos\\theta = \\frac{1}{2}\\cos\\theta \\implies \\cos\\theta = \\frac{2}{3}$$\n\n**3. Velocity at Highest Point of Parabolic Path:**\nAt break-off, the body becomes a free projectile launched at angle $\\theta$ to the horizontal.\nAt the apex of this flight, the vertical velocity is zero, leaving only the horizontal component:\n$$v = v_b \\sin\\theta = \\sqrt{gR\\cos\\theta} \\sqrt{1 - \\cos^2\\theta} = \\sqrt{g\\left(\\frac{h}{2}\\right)\\left(\\frac{2}{3}\\right)} \\sqrt{1 - \\frac{4}{9}} = \\sqrt{\\frac{gh}{3}} \\cdot \\frac{\\sqrt{5}}{3} = \\frac{2}{3}\\sqrt{\\frac{gh}{3}}$$",
        "tags": ["circular motion", "energy conservation", "break-off"]
    },
    {
        "id": "1.137",
        "title": "Minimum Velocity of Suspension Point for Circular Motion",
        "difficulty": 2,
        "question": "A ball of mass $m$ is suspended by a thread of length $l$. With what minimum velocity has the point of suspension to be shifted in the horizontal direction for the ball to move along the circle about that point? What will be the tension of the thread at the moment it will be passing the horizontal position?",
        "hints": [
            "In the frame of the suspension point, the ball must complete a vertical circle.",
            "At the top of the circle, thread tension $T \\ge 0 \\implies v_{\\text{top}}^2 \\ge gl$.",
            "Apply energy conservation between the bottom and top to find $v_{\\min}$, and between bottom and horizontal position to find tension $T$."
        ],
        "answer": "$v_{\\min} = \\sqrt{5gl}$; $T = 3mg$",
        "solution": "**1. Condition for Complete Vertical Circle:**\nIn the reference frame moving with the suspension point, the ball is launched horizontally at the bottom with velocity $v_{\\min}$.\nAt the highest point, tension must remain non-negative:\n$$T_{\\text{top}} = \\frac{mv_{\\text{top}}^2}{l} - mg \\ge 0 \\implies v_{\\text{top}}^2 \\ge gl$$\nBy energy conservation between bottom and top ($h = 2l$):\n$$\\frac{1}{2}mv_{\\min}^2 = \\frac{1}{2}mv_{\\text{top}}^2 + mg(2l) = \\frac{1}{2}mgl + 2mgl = \\frac{5}{2}mgl$$\n$$v_{\\min} = \\sqrt{5gl}$$\n\n**2. Thread Tension at Horizontal Position:**\nAt the horizontal position (height $y = l$):\n$$\\frac{1}{2}mv_h^2 + mgl = \\frac{1}{2}mv_{\\min}^2 = \\frac{5}{2}mgl \\implies v_h^2 = 3gl$$\nSince gravity is vertical, the horizontal tension provides the centripetal acceleration:\n$$T = \\frac{mv_h^2}{l} = \\frac{m(3gl)}{l} = 3mg$$",
        "tags": ["circular motion", "energy conservation", "pendulum"]
    },
    {
        "id": "1.138",
        "title": "Thread Winding on a Cylinder",
        "difficulty": 2,
        "question": "A horizontal plane supports a stationary vertical cylinder of radius $R$ and a disc $A$ attached to the cylinder by a horizontal thread $AB$ of length $l_0$. An initial velocity $v_0$ is imparted to the disc perpendicular to the thread. How long will it move along the plane until it strikes against the cylinder? The friction is assumed to be absent.",
        "hints": [
            "Tension is always perpendicular to velocity, so speed is constant: $v = v_0$.",
            "As the thread winds, the instantaneous radius of curvature is the remaining free length $l(t)$.",
            "Write $\\frac{dl}{dt} = -R\\omega = -\\frac{Rv_0}{l}$ and integrate from $l_0$ to $0$."
        ],
        "answer": "$t = \\frac{l_0^2}{2v_0 R}$",
        "solution": "**1. Constancy of Speed:**\nSince the thread tension force is always perpendicular to the disc's velocity vector $\\mathbf{v}$, it performs zero work. In the absence of friction, the speed of the disc is constant:\n$$v(t) = v_0$$\n\n**2. Rate of Change of Free Length:**\nAt any instant, the disc rotates around the instantaneous contact point of the thread with the cylinder. The instantaneous angular velocity is $\\omega = \\frac{v_0}{l}$.\nThe thread wraps onto the cylinder circumference at the rate:\n$$\\frac{dl}{dt} = -R\\omega = -\\frac{R v_0}{l}$$\n\n**3. Total Winding Time:**\nSeparating variables:\n$$l \\, dl = -v_0 R \\, dt$$\nIntegrating from $t = 0$ ($l = l_0$) to time $t$ ($l = 0$):\n$$\\int_{l_0}^0 l \\, dl = -v_0 R \\int_0^t dt$$\n$$-\\frac{1}{2}l_0^2 = -v_0 R t \\implies t = \\frac{l_0^2}{2v_0 R}$$",
        "tags": ["kinematics", "circular motion", "integration"]
    },
    {
        "id": "1.139",
        "title": "Falling Sleeve on a Rubber Cord with Catch",
        "difficulty": 2,
        "question": "A smooth rubber cord of length $l$ whose coefficient of elasticity is $k$ is suspended by one end from the point $O$. The other end is fitted with a catch $B$. A small sleeve $A$ of mass $m$ starts falling from the point $O$. Neglecting the masses of the cord and the catch, find the maximum elongation of the cord.",
        "hints": [
            "The sleeve falls freely through distance $l$ before the catch is engaged.",
            "Apply conservation of mechanical energy between the release point $O$ and the point of maximum elongation $\\Delta l$.",
            "Solve the quadratic equation in $\\Delta l$."
        ],
        "answer": "$\\Delta l = \\frac{mg}{k}\\left(1 + \\sqrt{1 + \\frac{2kl}{mg}}\\right)$",
        "solution": "**1. Energy Conservation:**\nLet $\\Delta l$ be the maximum elongation of the cord. The sleeve falls from rest through total vertical descent $h = l + \\Delta l$.\nAt the turning point, the sleeve is momentarily at rest, so all lost gravitational potential energy is converted into elastic potential energy of the stretched cord:\n$$mg(l + \\Delta l) = \\frac{1}{2}k(\\Delta l)^2$$\n\n**2. Quadratic Equation for $\\Delta l$:**\n$$\\frac{1}{2}k(\\Delta l)^2 - mg\\Delta l - mgl = 0$$\n$$(\\Delta l)^2 - \\frac{2mg}{k}\\Delta l - \\frac{2mgl}{k} = 0$$\n\n**3. Solution:**\nTaking the positive physical root:\n$$\\Delta l = \\frac{mg}{k} + \\sqrt{\\left(\\frac{mg}{k}\\right)^2 + \\frac{2mgl}{k}} = \\frac{mg}{k}\\left(1 + \\sqrt{1 + \\frac{2kl}{mg}}\\right)$$",
        "tags": ["work-energy", "elasticity", "potential energy"]
    },
    {
        "id": "1.140",
        "title": "Break-off Velocity of Spring-Attached Bar on Smooth Plane",
        "difficulty": 2,
        "question": "A small bar $A$ resting on a smooth horizontal plane is attached by threads to a point $P$ and, by means of a weightless pulley, to a weight $B$ possessing the same mass as the bar itself. Besides, the bar is also attached to a point $O$ by means of a light non-deformed spring of length $l_0 = 50\\text{ cm}$ and stiffness $\\varkappa = 5mg/l_0$, where $m$ is the mass of the bar. The thread $PA$ having been burned, the bar starts moving. Find its velocity at the moment when it is breaking off the plane.",
        "hints": [
            "Break-off occurs when the vertical component of the spring force balances gravity: $F_{\\text{sp}}\\sin\\theta = mg$.",
            "Determine the angle $\\theta$ and corresponding elongation $\\Delta l$ at break-off.",
            "Apply conservation of mechanical energy to the two-body system to find $v$."
        ],
        "answer": "$v = \\sqrt{\\frac{19}{32}gl_0} \\approx 1.7\\text{ m/s}$",
        "solution": "**1. Break-off Condition:**\nWhen the spring makes an angle $\\theta$ with the horizontal, its length is $l = l_0/\\cos\\theta$, so elongation is $\\Delta l = l_0(1/\\cos\\theta - 1)$.\nThe spring force is:\n$$F_{\\text{sp}} = \\varkappa \\Delta l = \\frac{5mg}{l_0} l_0 \\left(\\frac{1}{\\cos\\theta} - 1\\right) = 5mg\\left(\\frac{1}{\\cos\\theta} - 1\\right)$$\nNormal reaction vanishes ($N = 0$) when the vertical component balances gravity:\n$$F_{\\text{sp}}\\sin\\theta = mg \\implies 5(1 - \\cos\\theta)\\tan\\theta = 1$$\nSolving this yields $\\cos\\theta = 4/5$, $\\sin\\theta = 3/5$.\n\n**2. System Geometry and Displacements:**\n- Horizontal displacement of $A$: $x = l_0\\tan\\theta = \\frac{3}{4}l_0$.\n- Vertical descent of weight $B$: $y = x = \\frac{3}{4}l_0$.\n- Elongation of spring: $\\Delta l = l_0(5/4 - 1) = \\frac{1}{4}l_0$.\n- Elastic potential energy: $U_{\\text{sp}} = \\frac{1}{2}\\varkappa(\\Delta l)^2 = \\frac{1}{2}\\left(\\frac{5mg}{l_0}\\right)\\left(\\frac{l_0}{4}\\right)^2 = \\frac{5}{32}mgl_0$.\n\n**3. Energy Conservation:**\nBoth bodies have equal mass $m$ and equal speed $v$:\n$$mg y = \\frac{1}{2}mv^2 + \\frac{1}{2}mv^2 + U_{\\text{sp}}$$\n$$mg\\left(\\frac{3}{4}l_0\\right) = mv^2 + \\frac{5}{32}mgl_0$$\n$$v^2 = gl_0\\left(\\frac{3}{4} - \\frac{5}{32}\\right) = \\frac{19}{32}gl_0$$\nWith $l_0 = 0.50\\text{ m}, g = 9.8\\text{ m/s}^2$:\n$$v = \\sqrt{\\frac{19}{32} \\times 9.8 \\times 0.50} = \\sqrt{2.909} \\approx 1.7\\text{ m/s}$$",
        "tags": ["work-energy", "springs", "break-off"]
    },
    {
        "id": "1.141",
        "title": "Work of Friction for a Bar Connected to an Elastic Cord on a Moving Plank",
        "difficulty": 2,
        "question": "A horizontal plane supports a plank with a bar of mass $m = 1.0\\text{ kg}$ placed on it and attached by a light elastic non-deformed cord of length $l_0 = 40\\text{ cm}$ to a point $O$. The coefficient of friction between the bar and the plank equals $k = 0.20$. The plank is slowly shifted to the right until the bar starts sliding over it. It occurs at the moment when the cord deviates from the vertical by an angle $\\theta = 30^{\\circ}$. Find the work that has been performed by that moment by the friction force acting on the bar in the reference frame fixed to the plane.",
        "hints": [
            "At the verge of sliding, tension $T$ balances friction: $T\\sin\\theta = k(mg - T\\cos\\theta)$.",
            "Express the stored elastic energy in the stretched cord $U = \\frac{1}{2}T\\Delta l$.",
            "Since motion is quasi-static, the work of friction equals $-U$."
        ],
        "answer": "$A = -\\frac{kmgl_0(1 - \\cos\\theta)}{2(\\sin\\theta + k\\cos\\theta)\\cos\\theta} \\approx -0.09\\text{ J}$",
        "solution": "**1. Condition for Incipient Sliding:**\nAt angle $\\theta$ from the vertical, normal force is $N = mg - T\\cos\\theta$.\nHorizontal equilibrium at threshold of sliding:\n$$T\\sin\\theta = kN = k(mg - T\\cos\\theta) \\implies T = \\frac{kmg}{\\sin\\theta + k\\cos\\theta}$$\n\n**2. Stored Elastic Energy:**\nThe cord length is $l = l_0/\\cos\\theta$, so its elongation is $\\Delta l = l_0\\left(\\frac{1 - \\cos\\theta}{\\cos\\theta}\\right)$.\nThe elastic potential energy is:\n$$U = \\frac{1}{2} T \\Delta l = \\frac{kmgl_0(1 - \\cos\\theta)}{2(\\sin\\theta + k\\cos\\theta)\\cos\\theta}$$\n\n**3. Work Done by Friction:**\nBecause the bar is shifted quasi-statically from rest, $\\Delta T = 0$:\n$$A_{\\text{fr}} = -U = -\\frac{kmgl_0(1 - \\cos\\theta)}{2(\\sin\\theta + k\\cos\\theta)\\cos\\theta}$$\nWith $m = 1.0\\text{ kg}, l_0 = 0.40\\text{ m}, k = 0.20, \\theta = 30^{\\circ}$:\n$$\\sin 30^{\\circ} + 0.20\\cos 30^{\\circ} = 0.50 + 0.1732 = 0.6732$$\n$$A_{\\text{fr}} = -\\frac{0.20 \\times 1.0 \\times 9.8 \\times 0.40 \\times (1 - 0.866)}{2 \\times 0.6732 \\times 0.866} = -\\frac{0.784 \\times 0.134}{1.166} \\approx -0.09\\text{ J}$$",
        "tags": ["work-energy", "friction", "elasticity"]
    },
    {
        "id": "1.142",
        "title": "Work Done Spinning a Rotating Rod with Spring-Loaded Sleeve",
        "difficulty": 2,
        "question": "A smooth light horizontal rod $AB$ can rotate about a vertical axis passing through its end $A$. The rod is fitted with a small sleeve of mass $m$ attached to the end $A$ by a weightless spring of length $l_0$ and stiffness $\\varkappa$. What work must be performed to slowly get this system going and reaching the angular velocity $\\omega$?",
        "hints": [
            "Find the steady radial position $r$ of the sleeve where spring tension balances centrifugal force: $\\varkappa(r - l_0) = m\\omega^2 r$.",
            "Express $r = \\frac{l_0}{1 - \\eta}$ with $\\eta = m\\omega^2/\\varkappa$.",
            "Total work done equals the total mechanical energy in the final state: $A = T + U$."
        ],
        "answer": "$A = \\frac{\\varkappa l_0^2 \\eta(2 - \\eta)}{2(1 - \\eta)^2}$, where $\\eta = m\\omega^2/\\varkappa$",
        "solution": "**1. Radial Position at Angular Velocity $\\omega$:**\nIn the rotating reference frame, the outward centrifugal force balances the inward spring force:\n$$\\varkappa(r - l_0) = m\\omega^2 r \\implies r(1 - \\eta) = l_0 \\implies r = \\frac{l_0}{1 - \\eta}$$\nwhere $\\eta = \\frac{m\\omega^2}{\\varkappa} < 1$.\nThe elongation is $\\Delta l = r - l_0 = \\frac{\\eta l_0}{1 - \\eta}$.\n\n**2. Final Mechanical Energy:**\n- Kinetic energy:\n  $$T = \\frac{1}{2}m(\\omega r)^2 = \\frac{1}{2}m\\omega^2 \\frac{l_0^2}{(1 - \\eta)^2} = \\frac{1}{2}\\varkappa \\eta \\frac{l_0^2}{(1 - \\eta)^2}$$\n- Elastic potential energy:\n  $$U = \\frac{1}{2}\\varkappa (\\Delta l)^2 = \\frac{1}{2}\\varkappa \\frac{\\eta^2 l_0^2}{(1 - \\eta)^2}$$\n\n**3. Work Done by External Agency:**\nSince the system was started slowly from rest:\n$$A = T + U = \\frac{1}{2}\\varkappa l_0^2 \\frac{\\eta + \\eta^2}{(1 - \\eta)^2} = \\frac{\\varkappa l_0^2 \\eta(2 - \\eta)}{2(1 - \\eta)^2}$$",
        "tags": ["work-energy", "rotating frame", "springs"]
    },
    {
        "id": "1.143",
        "title": "Acceleration of Center of Inertia in an Atwood Machine",
        "difficulty": 1,
        "question": "A pulley fixed to the ceiling carries a thread with bodies of masses $m_1$ and $m_2$ attached to its ends. The masses of the pulley and the thread are negligible, and friction is absent. Find the acceleration $w_C$ of the centre of inertia of this system.",
        "hints": [
            "Find the acceleration $w$ of the individual masses using Newton's second law.",
            "Write the acceleration of the center of inertia $\\mathbf{w}_C = \\frac{m_1 \\mathbf{w}_1 + m_2 \\mathbf{w}_2}{m_1 + m_2}$.",
            "Substitute $\\mathbf{w}_1 = -w\\hat{\\mathbf{j}}$ and $\\mathbf{w}_2 = w\\hat{\\mathbf{j}}$."
        ],
        "answer": "$w_C = g\\left(\\frac{m_1 - m_2}{m_1 + m_2}\\right)^2$",
        "solution": "**1. Acceleration of the Masses:**\nLet $m_1 > m_2$. The common magnitude of acceleration is:\n$$w = \\frac{m_1 - m_2}{m_1 + m_2}g$$\nTaking downward as negative:\n$$\\mathbf{w}_1 = -w\\hat{\\mathbf{j}}, \\quad \\mathbf{w}_2 = +w\\hat{\\mathbf{j}}$$\n\n**2. Center of Inertia Acceleration:**\n$$\\mathbf{w}_C = \\frac{m_1 \\mathbf{w}_1 + m_2 \\mathbf{w}_2}{m_1 + m_2} = \\frac{-m_1 w + m_2 w}{m_1 + m_2}\\hat{\\mathbf{j}} = -\\left(\\frac{m_1 - m_2}{m_1 + m_2}\\right)w \\hat{\\mathbf{j}}$$\nSubstituting $w = \\frac{m_1 - m_2}{m_1 + m_2}g$:\n$$w_C = g\\left(\\frac{m_1 - m_2}{m_1 + m_2}\\right)^2$$\nDirected downward along the vertical.",
        "tags": ["center of mass", "Atwood machine", "Newton's laws"]
    },
    {
        "id": "1.144",
        "title": "Center-of-Inertia Trajectory for Two Interacting Particles",
        "difficulty": 2,
        "question": "Two interacting particles form a closed system whose centre of inertia is at rest. The positions of both particles at a certain moment and the trajectory of the particle of mass $m_1$ are known. Draw the trajectory of the particle of mass $m_2$ if $m_2/m_1 = 2$.",
        "hints": [
            "Since the system is closed and center of inertia is at rest, set $\\mathbf{r}_C = 0$.",
            "Relate the position vectors: $m_1 \\mathbf{r}_1 + m_2 \\mathbf{r}_2 = 0 \\implies \\mathbf{r}_2 = -\\frac{m_1}{m_2}\\mathbf{r}_1$.",
            "Describe the geometric transformation of particle 1's trajectory."
        ],
        "answer": "The trajectory of particle 2 is homothetic to that of particle 1 with scaling factor $m_1/m_2 = 1/2$ and rotated by $180^{\\circ}$ about the stationary center of inertia.",
        "solution": "**1. Conservation of Center of Inertia:**\nIn an isolated system with stationary center of inertia located at the origin:\n$$m_1 \\mathbf{r}_1(t) + m_2 \\mathbf{r}_2(t) = 0$$\n\n**2. Geometric Transformation:**\n$$\\mathbf{r}_2(t) = -\\frac{m_1}{m_2}\\mathbf{r}_1(t) = -\\frac{1}{2}\\mathbf{r}_1(t)$$\nAt every moment, $\\mathbf{r}_2$ is in the exact opposite direction to $\\mathbf{r}_1$, with magnitude scaled down by $\\frac{m_1}{m_2} = \\frac{1}{2}$.\n\n**3. Construction of the Trajectory:**\nThe trajectory of particle 2 is geometrically similar (homothetic) to that of particle 1, shrunk by factor $1/2$, and inverted through the origin (center of inertia).",
        "tags": ["center of mass", "conservation of momentum", "relative motion"]
    },
    {
        "id": "1.145",
        "title": "Rotating Closed Chain Conical Configuration",
        "difficulty": 2,
        "question": "A closed chain of mass $m = 0.36\\text{ kg}$ is attached to a vertical rotating shaft by means of a thread, and rotates with a constant angular velocity $\\omega = 35\\text{ rad/s}$. The thread forms an angle $\\theta = 45^{\\circ}$ with the vertical. Find the distance between the chain's centre of gravity and the rotation axis, and the tension of the thread.",
        "hints": [
            "Vertical equilibrium for the chain: $T\\cos\\theta = mg$.",
            "Horizontal component provides centripetal acceleration: $T\\sin\\theta = m\\omega^2 r$.",
            "Divide the two equations to find $r = \\frac{g}{\\omega^2}\\tan\\theta$ and solve for $T$."
        ],
        "answer": "$r = \\frac{g}{\\omega^2}\\tan\\theta = 0.8\\text{ cm}$; $T = \\frac{mg}{\\cos\\theta} = 5\\text{ N}$",
        "solution": "**1. Thread Tension:**\nFrom vertical equilibrium of the chain:\n$$T\\cos\\theta = mg \\implies T = \\frac{mg}{\\cos\\theta}$$\nWith $m = 0.36\\text{ kg}, \\theta = 45^{\\circ}, g = 9.8\\text{ m/s}^2$:\n$$T = \\frac{0.36 \\times 9.8}{\\cos 45^{\\circ}} = \\frac{3.528}{0.7071} \\approx 5.0\\text{ N} = 5\\text{ N}$$\n\n**2. Radius of Rotation $r$:**\nThe horizontal component of tension provides centripetal acceleration for the chain's center of mass:\n$$T\\sin\\theta = m\\omega^2 r$$\nSubstituting $T = \\frac{mg}{\\cos\\theta}$:\n$$mg\\tan\\theta = m\\omega^2 r \\implies r = \\frac{g}{\\omega^2}\\tan\\theta$$\nWith $\\omega = 35\\text{ rad/s}$ and $\\theta = 45^{\\circ}$:\n$$r = \\frac{9.8}{35^2} \\times 1.0 = \\frac{9.8}{1225} = 0.0080\\text{ m} = 0.8\\text{ cm}$$",
        "tags": ["circular motion", "conical pendulum", "tension"]
    }
]
