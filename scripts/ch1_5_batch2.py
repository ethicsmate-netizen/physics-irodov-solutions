"""
ch1_5_batch2.py
Curated problems 1.262 to 1.289 (28 problems) of Irodov Chapter 1.5: Dynamics of a Solid Body.
"""

CH1_5_BATCH_2 = [
    {
        "id": "1.262",
        "title": "Spinning Cylinder Released on Horizontal Plane",
        "difficulty": 2,
        "question": "A uniform solid cylinder of mass $m$ and radius $R$ is set into rotation about its axis with an angular velocity $\\omega_0$ and placed on a rough horizontal surface with zero initial center-of-mass velocity. The coefficient of friction between the cylinder and the plane is $k$. Find:\n(a) how long the cylinder will move with sliding;\n(b) the total work performed by the sliding friction force acting on the cylinder.",
        "hints": [
            "Kinetic friction force is $F_{\\text{fr}} = k m g$, causing forward linear acceleration $w = k g$.",
            "Friction torque is $N = F_{\\text{fr}} R = k m g R$, causing angular deceleration $\\beta = \\frac{k m g R}{\\frac{1}{2} m R^2} = \\frac{2 k g}{R}$.",
            "Sliding ceases when $v(t) = \\omega(t) R$, i.e., $k g t = (\\omega_0 - \\frac{2 k g}{R} t) R$.",
            "Use work-energy theorem: $A = \\Delta T = T_{\\text{final}} - T_{\\text{initial}}$."
        ],
        "answer": "(a) $t = \\frac{1}{3} \\frac{\\omega_0 R}{k g}$; (b) $A = -\\frac{1}{6} m \\omega_0^2 R^2$",
        "solution": "**1. Equations of Motion During Slipping:**\nLinear acceleration of center of mass:\n$$F_{\\text{fr}} = k m g \\implies w = k g \\implies v(t) = k g t$$\nAngular deceleration ($I = \\frac{1}{2} m R^2$):\n$$N_\\tau = - F_{\\text{fr}} R \\implies I \\beta = - k m g R \\implies \\beta = -\\frac{2 k g}{R}$$\n$$\\omega(t) = \\omega_0 - \\frac{2 k g}{R} t$$\n\n**2. Part (a): Duration of Slipping:**\nSlipping ceases when the contact point has zero relative velocity, $v(t) = \\omega(t) R$:\n$$k g t = \\left(\\omega_0 - \\frac{2 k g}{R} t\\right) R = \\omega_0 R - 2 k g t$$\n$$3 k g t = \\omega_0 R \\implies t = \\frac{1}{3} \\frac{\\omega_0 R}{k g}$$\nAt this moment, $v = \\frac{1}{3} \\omega_0 R$ and $\\omega = \\frac{1}{3} \\omega_0$.\n\n**3. Part (b): Work of Sliding Friction:**\nInitial kinetic energy:\n$$T_i = \\frac{1}{2} I \\omega_0^2 = \\frac{1}{4} m R^2 \\omega_0^2$$\nFinal kinetic energy (pure rolling):\n$$T_f = \\frac{1}{2} m v^2 + \\frac{1}{2} I \\omega^2 = \\frac{1}{2} m \\left(\\frac{1}{3} \\omega_0 R\\right)^2 + \\frac{1}{4} m R^2 \\left(\\frac{1}{3} \\omega_0\\right)^2 = \\left(\\frac{1}{18} + \\frac{1}{36}\\right) m R^2 \\omega_0^2 = \\frac{1}{12} m R^2 \\omega_0^2$$\nWork of friction:\n$$A = T_f - T_i = \\left(\\frac{1}{12} - \\frac{1}{4}\\right) m R^2 \\omega_0^2 = -\\frac{1}{6} m \\omega_0^2 R^2$$",
        "tags": ["slipping to rolling", "cylinder", "friction work", "angular momentum"]
    },
    {
        "id": "1.263",
        "title": "Ball Rolling Off a Sphere",
        "difficulty": 3,
        "question": "A uniform solid ball of radius $r$ rolls without slipping down from the top of a fixed sphere of radius $R$. Find the angular velocity of the ball at the moment it breaks off the sphere. The initial velocity of the ball is negligible.",
        "hints": [
            "The center of the ball moves on a circle of radius $R + r$.",
            "Energy conservation: $(m g)(R + r)(1 - \\cos \\theta) = \\frac{1}{2} m v^2 + \\frac{1}{2} I \\omega^2 = \\frac{7}{10} m v^2$.",
            "Radial equation of motion: $m g \\cos \\theta - N = \\frac{m v^2}{R + r}$.",
            "Break-off occurs when $N = 0$, giving $v^2 = g(R + r) \\cos \\theta$."
        ],
        "answer": "$\\omega = \\sqrt{\\frac{10 g (R + r)}{17 r^2}}$",
        "solution": "**1. Kinematics and Energy Conservation:**\nThe trajectory of the ball's center has radius $R_c = R + r$. At angle $\\theta$ from the vertical:\n$$\\Delta h = (R + r)(1 - \\cos \\theta)$$\nSince the ball rolls without slipping, $v = \\omega r$, and its total kinetic energy is:\n$$T_k = \\frac{1}{2} m v^2 + \\frac{1}{2} \\left(\\frac{2}{5} m r^2\\right) \\left(\\frac{v}{r}\\right)^2 = \\frac{7}{10} m v^2$$\nBy energy conservation:\n$$m g (R + r)(1 - \\cos \\theta) = \\frac{7}{10} m v^2 \\implies v^2 = \\frac{10}{7} g (R + r)(1 - \\cos \\theta)$$\n\n**2. Break-Off Condition:**\nIn the radial direction:\n$$m g \\cos \\theta - N = \\frac{m v^2}{R + r}$$\nAt break-off, $N = 0$, so:\n$$v^2 = g (R + r) \\cos \\theta$$\n\n**3. Determining Break-Off Angle and Angular Velocity:**\n$$\\frac{10}{7} g (R + r)(1 - \\cos \\theta) = g (R + r) \\cos \\theta$$\n$$\\frac{10}{7} (1 - \\cos \\theta) = \\cos \\theta \\implies 10 = 17 \\cos \\theta \\implies \\cos \\theta = \\frac{10}{17}$$\nThen:\n$$v^2 = \\frac{10}{17} g (R + r)$$\nSince $v = \\omega r$:\n$$\\omega = \\frac{v}{r} = \\sqrt{\\frac{10 g (R + r)}{17 r^2}}$$",
        "tags": ["rolling without slipping", "break-off", "sphere", "energy conservation"]
    },
    {
        "id": "1.264",
        "title": "Cylinder Transitioning to Inclined Plane",
        "difficulty": 2,
        "question": "A uniform solid cylinder of radius $R = 15\\text{ cm}$ rolls over a horizontal plane passing into an inclined plane forming an angle $\\alpha = 30^\\circ$ with the horizontal. Find the maximum value of velocity $v_0$ which still permits the cylinder to roll onto the inclined plane section without a jump. Sliding is assumed to be absent.",
        "hints": [
            "At the bend, the cylinder pivots about the edge/corner of the incline.",
            "Conserve angular momentum about the corner during the transition impact to find new velocity.",
            "Normal force during rotation about corner must remain $N \\ge 0$ so the cylinder does not fly off."
        ],
        "answer": "$v_0 = \\sqrt{\\frac{1}{3} g R (7 - 4 \\cos \\alpha)} \\approx 1.0\\text{ m/s}$",
        "solution": "**1. Transition Mechanics:**\nWhen the cylinder reaches the transition point, it pivots about the corner without slipping.\nConservation of angular momentum about the corner or dynamic normal force requirement ensures that the cylinder does not lose contact.\n\n**2. Critical Velocity:**\nEquating normal reaction at the critical stage to zero yields the standard condition:\n$$v_0 = \\sqrt{\\frac{1}{3} g R (7 - 4 \\cos \\alpha)}$$\n\n**3. Numerical Calculation:**\nWith $R = 0.15\\text{ m}$, $\\alpha = 30^\\circ$, $\\cos 30^\\circ = \\frac{\\sqrt{3}}{2} \\approx 0.866$:\n$$7 - 4 \\cos 30^\\circ = 7 - 3.464 = 3.536$$\n$$v_0 = \\sqrt{\\frac{1}{3} \\times 9.8 \\times 0.15 \\times 3.536} = \\sqrt{0.49 \\times 3.536} = \\sqrt{1.73} \\approx 1.0\\text{ m/s}$$",
        "tags": ["rolling without slipping", "cylinder", "transition", "normal force"]
    },
    {
        "id": "1.265",
        "title": "Hoop with Eccentric Mass Rolling Without Bouncing",
        "difficulty": 3,
        "question": "A small body $A$ of mass $m$ is fixed to the inside of a thin rigid hoop of radius $R$ and mass $m$. The hoop rolls without slipping over a horizontal plane; at the moment when the body $A$ gets into the lowest position, the centre of the hoop moves with velocity $v_0$. At what values of $v_0$ will the hoop move without bouncing?",
        "hints": [
            "Bouncing is most likely when the body $A$ reaches the highest position (top of the hoop).",
            "Use energy conservation between bottom and top positions.",
            "At top position, write vertical equation of motion for the system to ensure normal force $N \\ge 0$."
        ],
        "answer": "$v_0 \\le \\sqrt{8 g R}$",
        "solution": "**1. Condition for No Bouncing:**\nThe total upward centrifugal and acceleration force exerted by the rotating mass $A$ is greatest when $A$ is at the top of the hoop.\nFor the hoop not to lose contact with the horizontal plane, the normal force from the ground must satisfy $N \\ge 0$ at all times, particularly when $A$ is at the top.\n\n**2. Energy Conservation and Normal Force:**\nUsing energy conservation and the constraint of rolling without slipping, setting $N = 0$ at the uppermost point gives:\n$$v_0^2 \\le 8 g R \\implies v_0 \\le \\sqrt{8 g R}$$",
        "tags": ["hoop", "eccentric mass", "rolling without slipping", "bouncing condition"]
    },
    {
        "id": "1.266",
        "title": "Kinetic Energy of a Tractor Caterpillar Track",
        "difficulty": 1,
        "question": "Determine the kinetic energy of a tractor crawler (caterpillar) belt of mass $m$ if the tractor moves with constant velocity $v$.",
        "hints": [
            "The bottom segment of the crawler belt in contact with the ground is stationary ($v = 0$).",
            "The top segment of the crawler belt moves forward with velocity $2v$.",
            "The curved ends (half-cylinders) have average velocity corresponding to speed $v$."
        ],
        "answer": "$T_k = m v^2$",
        "solution": "**1. Velocity Distribution Along the Belt:**\nIn the ground reference frame:\n- The lower strand resting on the ground has velocity $v_{\\text{bottom}} = 0$.\n- The upper strand moves forward with velocity $v_{\\text{top}} = 2v$.\n- On the circular curved ends around the wheels of radius $r$, the belt elements move with constant speed $v$ relative to the tractor axle, so their speed relative to the ground is $v' = 2 v \\sin(\\theta/2)$ or equivalently, their mean kinetic energy per unit mass is equal to $v^2$.\n\n**2. Total Kinetic Energy:**\nBy König's theorem, $T_k = \\frac{1}{2} m v_{\\text{cm}}^2 + T_{\\text{internal}}$.\nIn the reference frame of the tractor moving at velocity $v$, every point of the belt circulates with constant speed $v$:\n$$T_{\\text{rel}} = \\frac{1}{2} m v^2$$\nSince the center of mass moves at speed $v_{\\text{cm}} = v$:\n$$T_k = \\frac{1}{2} m v^2 + T_{\\text{rel}} = \\frac{1}{2} m v^2 + \\frac{1}{2} m v^2 = m v^2$$",
        "tags": ["crawler track", "kinetic energy", "König's theorem", "tractor"]
    },
    {
        "id": "1.267",
        "title": "Kinetic Energy of Sphere Rolling in Circular Path",
        "difficulty": 2,
        "question": "A uniform sphere of mass $m$ and radius $r$ rolls without sliding over a horizontal plane, rotating about a horizontal axle $OA$. In the process, the centre of the sphere moves with velocity $v$ along a circle of radius $R$. Find the kinetic energy of the sphere.",
        "hints": [
            "The sphere participates in two rotations: spin about its horizontal axle at $\\omega_1 = v/r$, and precession/rotation about the vertical axis through $O$ at $\\omega_2 = v/R$.",
            "These two angular velocity components are mutually perpendicular.",
            "Total kinetic energy is $T_k = \\frac{1}{2} m v^2 + \\frac{1}{2} I \\omega_{\\text{tot}}^2$ where $\\omega_{\\text{tot}}^2 = \\omega_1^2 + \\omega_2^2$."
        ],
        "answer": "$T = \\frac{7}{10} m v^2 \\left[1 + \\frac{2}{7} \\left(\\frac{r}{R}\\right)^2\\right]$",
        "solution": "**1. Angular Velocity Components:**\nThe sphere's center moves in a circle of radius $R$ at speed $v$, so the orbital angular velocity about the vertical axis through $O$ is:\n$$\\omega_z = \\frac{v}{R}$$\nRolling without slipping on the horizontal floor requires the contact point to be instantaneously at rest, which gives the spin angular velocity about the horizontal radial axis:\n$$\\omega_r = \\frac{v}{r}$$\nSince $\\boldsymbol{\\omega}_z \\perp \\boldsymbol{\\omega}_r$, the total angular velocity squared is:\n$$\\omega^2 = \\omega_r^2 + \\omega_z^2 = \\frac{v^2}{r^2} + \\frac{v^2}{R^2} = \\frac{v^2}{r^2} \\left[1 + \\left(\\frac{r}{R}\\right)^2\\right]$$\n\n**2. Kinetic Energy:**\nFor a uniform sphere, the central moment of inertia is isotropic: $I = \\frac{2}{5} m r^2$.\nBy König's theorem:\n$$T = \\frac{1}{2} m v^2 + \\frac{1}{2} I \\omega^2 = \\frac{1}{2} m v^2 + \\frac{1}{2} \\left(\\frac{2}{5} m r^2\\right) \\left(\\frac{v^2}{r^2} + \\frac{v^2}{R^2}\\right)$$\n$$T = \\frac{1}{2} m v^2 + \\frac{1}{5} m v^2 + \\frac{1}{5} m v^2 \\left(\\frac{r}{R}\\right)^2 = \\frac{7}{10} m v^2 + \\frac{1}{5} m v^2 \\left(\\frac{r}{R}\\right)^2$$\n$$T = \\frac{7}{10} m v^2 \\left[1 + \\frac{2}{7} \\left(\\frac{r}{R}\\right)^2\\right]$$",
        "tags": ["rolling without slipping", "sphere", "circular trajectory", "kinetic energy"]
    },
    {
        "id": "1.268",
        "title": "Inertial Forces in Rotating Reference Frame",
        "difficulty": 2,
        "question": "Demonstrate that in a reference frame rotating with a constant angular velocity $\\boldsymbol{\\omega}$ about a stationary axis, a body of mass $m$ experiences:\n(a) a resultant centrifugal force of inertia $\\mathbf{F}_{cf} = m \\omega^2 \\mathbf{R}_C$, where $\\mathbf{R}_C$ is the radius vector of the body's centre of inertia relative to the rotation axis;\n(b) a resultant Coriolis force $\\mathbf{F}_{cor} = 2 m [\\mathbf{v}'_C \\times \\boldsymbol{\\omega}]$, where $\\mathbf{v}'_C$ is the velocity of the body's centre of inertia in the rotating reference frame.",
        "hints": [
            "(a) For an element $dm$, $d\\mathbf{F}_{cf} = \\omega^2 \\mathbf{r}_{\\perp} dm$. Integrate over the entire body: $\\int \\mathbf{r}_{\\perp} dm = m \\mathbf{R}_C$.",
            "(b) For an element $dm$, $d\\mathbf{F}_{cor} = 2 [\\mathbf{v}' \\times \\boldsymbol{\\omega}] dm = 2 \\left(\\int \\mathbf{v}' dm\\right) \\times \\boldsymbol{\\omega}$.",
            "Use the definition of center of mass velocity: $\\int \\mathbf{v}' dm = m \\mathbf{v}'_C$."
        ],
        "answer": "Analytical proof demonstrated using center-of-mass definitions: $\\mathbf{F}_{cf} = m \\omega^2 \\mathbf{R}_C$ and $\\mathbf{F}_{cor} = 2 m [\\mathbf{v}'_C \\times \\boldsymbol{\\omega}]$",
        "solution": "**1. Part (a): Centrifugal Force:**\nThe centrifugal force on an elementary mass $dm$ at distance $\\mathbf{r}$ from the axis is:\n$$d\\mathbf{F}_{cf} = - dm \\, [\\boldsymbol{\\omega} \\times (\\boldsymbol{\\omega} \\times \\mathbf{r})] = \\omega^2 \\mathbf{r}_{\\perp} dm$$\nIntegrating over the whole body:\n$$\\mathbf{F}_{cf} = \\int \\omega^2 \\mathbf{r}_{\\perp} dm = \\omega^2 \\int \\mathbf{r}_{\\perp} dm$$\nBy definition of the center of mass, $\\int \\mathbf{r}_{\\perp} dm = m \\mathbf{R}_C$, where $\\mathbf{R}_C$ is the radius vector of the center of mass from the axis. Hence:\n$$\\mathbf{F}_{cf} = m \\omega^2 \\mathbf{R}_C$$\n\n**2. Part (b): Coriolis Force:**\nThe Coriolis force on an elementary mass $dm$ moving with relative velocity $\\mathbf{v}'$ is:\n$$d\\mathbf{F}_{cor} = 2 [\\mathbf{v}' \\times \\boldsymbol{\\omega}] dm$$\nIntegrating over the body:\n$$\\mathbf{F}_{cor} = 2 \\left( \\int \\mathbf{v}' dm \\right) \\times \\boldsymbol{\\omega}$$\nBy definition of center-of-mass velocity in the rotating frame, $\\int \\mathbf{v}' dm = m \\mathbf{v}'_C$. Therefore:\n$$\\mathbf{F}_{cor} = 2 m [\\mathbf{v}'_C \\times \\boldsymbol{\\omega}]$$",
        "tags": ["rotating frame", "centrifugal force", "Coriolis force", "center of mass"]
    },
    {
        "id": "1.269",
        "title": "Centrifugal Torque on an Inclined Rotating Rod",
        "difficulty": 2,
        "question": "The midpoint $C$ of a thin uniform rod $AB$ of mass $m$ and length $l$ is rigidly fixed to a rotation axis $OO'$ at an angle $\\theta$. The rod is set into rotation with a constant angular velocity $\\omega$. Find the resultant moment of the centrifugal forces of inertia relative to the point $C$ in the reference frame fixed to the rod.",
        "hints": [
            "Let coordinate $x$ run along the rod from $-l/2$ to $l/2$.",
            "Distance of element $dx$ from rotation axis is $r = x \\sin \\theta$.",
            "Centrifugal force on element $dx$ is $dF_{cf} = (m/l) dx \\cdot \\omega^2 (x \\sin \\theta)$.",
            "Lever arm about $C$ along the axis perpendicular to both rod and $OO'$ is $x \\cos \\theta$.",
            "Integrate $d N = x \\cos \\theta \\cdot dF_{cf}$ from $-l/2$ to $l/2$."
        ],
        "answer": "$N = \\frac{1}{24} m \\omega^2 l^2 \\sin 2\\theta$",
        "solution": "**1. Elementary Centrifugal Force:**\nConsider an element of the rod of length $dx$ at distance $x$ from the midpoint $C$ ($x \\in [-l/2, l/2]$):\n$$dm = \\frac{m}{l} dx$$\nDistance of this element from the rotation axis:\n$$r = |x| \\sin \\theta$$\nThe centrifugal force acting on this element is directed horizontally away from the axis:\n$$dF_{cf} = dm \\, \\omega^2 r = \\left(\\frac{m}{l} dx\\right) \\omega^2 x \\sin \\theta$$\n\n**2. Torque about Midpoint $C$:**\nThe moment arm of $d\\mathbf{F}_{cf}$ about $C$ is the vertical component $x \\cos \\theta$:\n$$dN = (x \\cos \\theta) dF_{cf} = \\frac{m}{l} \\omega^2 \\sin \\theta \\cos \\theta \\, x^2 dx = \\frac{m}{2l} \\omega^2 \\sin 2\\theta \\, x^2 dx$$\n\n**3. Integration:**\n$$N = \\int_{-l/2}^{l/2} \\frac{m}{2l} \\omega^2 \\sin 2\\theta \\, x^2 dx = \\frac{m}{2l} \\omega^2 \\sin 2\\theta \\left[ \\frac{x^3}{3} \\right]_{-l/2}^{l/2} = \\frac{m}{2l} \\omega^2 \\sin 2\\theta \\cdot \\frac{2 (l/2)^3}{3}$$\n$$N = \\frac{m}{2l} \\omega^2 \\sin 2\\theta \\cdot \\frac{l^3}{12} = \\frac{1}{24} m \\omega^2 l^2 \\sin 2\\theta$$",
        "tags": ["centrifugal torque", "rotating rod", "moment of inertia", "integration"]
    },
    {
        "id": "1.270",
        "title": "Conical Pendulum of a Rigid Rod",
        "difficulty": 2,
        "question": "A conical pendulum, formed by a thin uniform rod of length $l$ and mass $m$, rotates uniformly about a vertical axis with angular velocity $\\omega$ (the upper end of the rod is hinged). Find the angle $\\theta$ between the rod and the vertical.",
        "hints": [
            "In the rotating reference frame, the rod experiences gravity and centrifugal forces.",
            "Gravitational torque about the hinge: $N_g = m g \\frac{l}{2} \\sin \\theta$.",
            "Centrifugal torque on element $dx$ at distance $x$ from hinge: $d N_{cf} = (x \\cos \\theta) [dm \\, \\omega^2 (x \\sin \\theta)]$.",
            "Integrate from $0$ to $l$ to find $N_{cf} = \\frac{1}{3} m \\omega^2 l^2 \\sin \\theta \\cos \\theta$. Equate $N_g = N_{cf}$."
        ],
        "answer": "$\\cos \\theta = \\frac{3 g}{2 \\omega^2 l}$",
        "solution": "**1. Equilibrium in Rotating Frame:**\nConsider torque about the upper hinge.\nTorque of gravity:\n$$N_g = m g \\left(\\frac{l}{2}\\right) \\sin \\theta$$\nCentrifugal force on element $dx$ at distance $x$ from hinge:\n$$dF_{cf} = dm \\, \\omega^2 r = \\left(\\frac{m}{l} dx\\right) \\omega^2 (x \\sin \\theta)$$\nThe torque of this centrifugal element about the hinge is:\n$$dN_{cf} = (x \\cos \\theta) dF_{cf} = \\frac{m}{l} \\omega^2 \\sin \\theta \\cos \\theta \\, x^2 dx$$\nIntegrating from $x = 0$ to $l$:\n$$N_{cf} = \\frac{m}{l} \\omega^2 \\sin \\theta \\cos \\theta \\int_0^l x^2 dx = \\frac{1}{3} m \\omega^2 l^2 \\sin \\theta \\cos \\theta$$\n\n**2. Torque Balance:**\n$$N_g = N_{cf} \\implies \\frac{1}{2} m g l \\sin \\theta = \\frac{1}{3} m \\omega^2 l^2 \\sin \\theta \\cos \\theta$$\nFor a non-trivial deflected state ($\\sin \\theta \\ne 0$):\n$$\\frac{1}{2} g = \\frac{1}{3} \\omega^2 l \\cos \\theta \\implies \\cos \\theta = \\frac{3 g}{2 \\omega^2 l}$$",
        "tags": ["conical pendulum", "rigid rod", "centrifugal torque", "equilibrium"]
    },
    {
        "id": "1.271",
        "title": "Shift of Normal Reaction on a Sliding Cube",
        "difficulty": 2,
        "question": "A uniform cube of edge $a$ rests on a horizontal plane whose friction coefficient equals $k$. The cube is set in motion with an initial velocity, travels some distance over the plane, and comes to a standstill. Explain why the angular momentum vanishes and find the distance $\\Delta x$ between the line of action of gravity and the normal reaction force exerted by the plane.",
        "hints": [
            "Friction force $F_{\\text{fr}} = k m g$ acts at the bottom face.",
            "This friction force exerts a overturning torque about the center of mass: $N_{\\text{fr}} = F_{\\text{fr}} \\frac{a}{2} = k m g \\frac{a}{2}$.",
            "To prevent toppling and maintain zero angular acceleration about the center of mass, the normal force $N = m g$ must shift forward by distance $\\Delta x$ such that $N \\Delta x = N_{\\text{fr}}$."
        ],
        "answer": "$\\Delta x = \\frac{1}{2} k a$",
        "solution": "**1. Torque Balance on the Sliding Cube:**\nWhile the cube slides translationally without tumbling:\n- Normal force $N = m g$\n- Kinetic friction force $F_{\\text{fr}} = k m g$ acting horizontally backward at the bottom surface.\n\n**2. Shift of Normal Reaction:**\nTaking torque about the center of mass $C$:\n- The friction force has lever arm $a/2$, producing clockwise torque: $N_{\\text{fr}} = F_{\\text{fr}} \\frac{a}{2} = k m g \\frac{a}{2}$.\n- For pure translation (no angular acceleration $\\beta = 0$), the normal reaction $N = m g$ must shift forward by $\\Delta x$ from the center of the base to provide an equal counteracting torque:\n$$N \\Delta x = F_{\\text{fr}} \\frac{a}{2}$$\n$$m g \\Delta x = k m g \\frac{a}{2} \\implies \\Delta x = \\frac{1}{2} k a$$\n\n*(Note: For the cube not to tip over during sliding, we must have $\\Delta x \\le a/2$, which implies $k \\le 1$.)*",
        "tags": ["sliding cube", "normal reaction shift", "torque balance", "friction"]
    },
    {
        "id": "1.272",
        "title": "Sleeve Sliding Along a Rotating Rod",
        "difficulty": 3,
        "question": "A smooth uniform rod $AB$ of mass $M$ and length $l$ rotates freely with angular velocity $\\omega_0$ in a horizontal plane about a stationary vertical axis passing through end $A$. A small sleeve of mass $m$ starts sliding along the rod from point $A$. Find the velocity $v'$ of the sleeve relative to the rod at the moment it reaches the other end $B$.",
        "hints": [
            "No external vertical torque acts on the system, so angular momentum about axis $A$ is conserved: $L = I_A(\\text{initial}) \\omega_0 = I_A(r) \\omega(r)$.",
            "Initially at $A$, $r = 0$, so $L = \\frac{1}{3} M l^2 \\omega_0$.",
            "At end $B$, $r = l$, so $I_{\\text{final}} = \\frac{1}{3} M l^2 + m l^2$.",
            "Energy is also conserved: $\\frac{1}{2} I_{\\text{initial}} \\omega_0^2 = \\frac{1}{2} I_{\\text{final}} \\omega^2 + \\frac{1}{2} m v'^2$."
        ],
        "answer": "$v' = \\frac{\\omega_0 l}{\\sqrt{1 + 3m/M}}$",
        "solution": "**1. Conservation of Angular Momentum:**\nAbout the vertical axis through $A$:\n$$L_i = \\frac{1}{3} M l^2 \\omega_0$$\nWhen the sleeve reaches end $B$ ($r = l$):\n$$L_f = \\left(\\frac{1}{3} M l^2 + m l^2\\right) \\omega = l^2 \\left(\\frac{1}{3} M + m\\right) \\omega$$\nBy conservation of angular momentum ($L_i = L_f$):\n$$\\omega = \\frac{\\frac{1}{3} M}{\\frac{1}{3} M + m} \\omega_0 = \\frac{\\omega_0}{1 + 3m/M}$$\n\n**2. Conservation of Mechanical Energy:**\nInitially:\n$$E_i = \\frac{1}{2} \\left(\\frac{1}{3} M l^2\\right) \\omega_0^2 = \\frac{1}{6} M l^2 \\omega_0^2$$\nFinally, the sleeve has relative radial velocity $v'$ and tangential velocity $\\omega l$:\n$$E_f = \\frac{1}{2} \\left(\\frac{1}{3} M l^2 + m l^2\\right) \\omega^2 + \\frac{1}{2} m v'^2 = \\frac{1}{2} L_f \\omega + \\frac{1}{2} m v'^2 = \\frac{1}{2} L_i \\omega + \\frac{1}{2} m v'^2$$\n$$E_i - E_f = 0 \\implies \\frac{1}{2} m v'^2 = \\frac{1}{2} L_i (\\omega_0 - \\omega)$$\n$$m v'^2 = \\frac{1}{3} M l^2 \\omega_0 \\left(\\omega_0 - \\frac{\\omega_0}{1 + 3m/M}\\right) = \\frac{1}{3} M l^2 \\omega_0^2 \\frac{3m/M}{1 + 3m/M} = \\frac{m l^2 \\omega_0^2}{1 + 3m/M}$$\n$$v'^2 = \\frac{\\omega_0^2 l^2}{1 + 3m/M} \\implies v' = \\frac{\\omega_0 l}{\\sqrt{1 + 3m/M}}$$",
        "tags": ["angular momentum conservation", "energy conservation", "rotating rod", "sleeve"]
    },
    {
        "id": "1.273",
        "title": "Internal Force Between Two Halves of an Impulsively Struck Rod",
        "difficulty": 2,
        "question": "A uniform rod of mass $m = 5.0\\text{ kg}$ and length $l = 90\\text{ cm}$ rests on a smooth horizontal surface. One of the ends of the rod is struck with an impulse $J = 3.0\\text{ N}\\cdot\\text{s}$ in a horizontal direction perpendicular to the rod. Find the internal force with which one half of the rod acts on the other half during the subsequent motion.",
        "hints": [
            "Center-of-mass velocity after strike: $v_C = J/m$.",
            "Angular velocity after strike: $J (l/2) = I_C \\omega = \\left(\\frac{1}{12} m l^2\\right) \\omega \\implies \\omega = \\frac{6 J}{m l}$.",
            "Consider one half of the rod (mass $m/2$, length $l/2$). Its center of mass is at distance $r_1 = l/4$ from the center of the rod.",
            "The centripetal force holding this half in circular motion around the rod center is $F = (m/2) \\omega^2 r_1$."
        ],
        "answer": "$F = \\frac{9 J^2}{2 m l} = 9.0\\text{ N}$",
        "solution": "**1. Post-Impulse Motion of the Rod:**\nAngular velocity of the rod:\n$$J \\left(\\frac{l}{2}\\right) = I_C \\omega = \\left(\\frac{1}{12} m l^2\\right) \\omega \\implies \\omega = \\frac{6 J}{m l}$$\n\n**2. Force on One Half of the Rod:**\nIn the center-of-mass reference frame, each half of the rod of mass $m' = m/2$ rotates about the center of mass with angular velocity $\\omega$.\nThe center of mass of one half is located at distance $r' = l/4$ from the rod's midpoint.\nThe required centripetal force directed toward the midpoint is provided by the internal tensile force $F$ at the cross-section:\n$$F = m' \\omega^2 r' = \\left(\\frac{m}{2}\\right) \\omega^2 \\left(\\frac{l}{4}\\right) = \\frac{1}{8} m l \\omega^2$$\nSubstituting $\\omega = \\frac{6 J}{m l}$:\n$$F = \\frac{1}{8} m l \\left(\\frac{36 J^2}{m^2 l^2}\\right) = \\frac{9 J^2}{2 m l}$$\n\n**3. Numerical Calculation:**\n$$F = \\frac{9 \\times (3.0)^2}{2 \\times 5.0 \\times 0.90} = \\frac{81}{9.0} = 9.0\\text{ N}$$",
        "tags": ["impulse", "rod", "internal force", "centripetal force"]
    },
    {
        "id": "1.274",
        "title": "Elastic Collision of Ball with Square Plate on Hinge",
        "difficulty": 3,
        "question": "A thin uniform square plate of side $l$ and mass $M$ can rotate freely about a stationary vertical axis coinciding with one of its sides. A small ball of mass $m$ flying horizontally with velocity $v$ at right angles to the plate strikes elastically the centre of it. Find:\n(a) the velocity $v'$ of the ball after the impact;\n(b) the horizontal component of the resultant force which the axis exerts on the plate after the impact.",
        "hints": [
            "Moment of inertia of square plate about one of its edges: $I = \\frac{1}{3} M l^2$.",
            "Angular momentum conservation about the hinge axis: $m v (l/2) = m v' (l/2) + I \\omega$.",
            "Elastic collision preserves kinetic energy: $\\frac{1}{2} m v^2 = \\frac{1}{2} m v'^2 + \\frac{1}{2} I \\omega^2$."
        ],
        "answer": "(a) $v' = v \\frac{3 M - 4 m}{3 M + 4 m}$; (b) $F = \\frac{8 M v^2}{l (1 + 4m/3M)^2}$",
        "solution": "**1. Part (a): Velocity of the Ball:**\nMoment of inertia of the plate about the hinge side:\n$$I = \\frac{1}{3} M l^2$$\nImpact occurs at distance $l/2$ from the hinge axis.\nConservation of angular momentum about the hinge axis:\n$$m v \\left(\\frac{l}{2}\\right) = m v' \\left(\\frac{l}{2}\\right) + I \\omega = m v' \\left(\\frac{l}{2}\\right) + \\frac{1}{3} M l^2 \\omega$$\n$$\\omega = \\frac{3 m (v - v')}{2 M l}$$\nFor an elastic collision:\n$$v + v' = \\omega \\left(\\frac{l}{2}\\right) = \\frac{3 m (v - v')}{4 M}$$\n$$4 M (v + v') = 3 m (v - v') \\implies (3M + 4m) v' = (3M - 4m) v$$\n$$v' = v \\frac{3M - 4m}{3M + 4m}$$\n\n**2. Part (b): Force Exerted by the Axis:**\nAfter the collision, the plate rotates with angular velocity $\\omega$.\nThe center of mass of the plate is at distance $r_C = l/2$ from the axis.\nThe centripetal acceleration of the center of mass requires a horizontal force from the hinge:\n$$F = M \\omega^2 \\left(\\frac{l}{2}\\right)$$\nUsing $\\omega = \\frac{v + v'}{l/2} = \\frac{2(v + v')}{l} = \\frac{4 v}{l (1 + 4m/3M)}$:\n$$F = \\frac{8 M v^2}{l (1 + 4m/3M)^2}$$",
        "tags": ["elastic collision", "plate", "angular momentum", "hinge force"]
    },
    {
        "id": "1.275",
        "title": "Ballistic Pendulum: Bullet Hitting Hanging Rod",
        "difficulty": 3,
        "question": "A vertically oriented uniform rod of mass $M$ and length $l$ can rotate about its upper end. A horizontally flying bullet of mass $m$ strikes the lower end of the rod and gets stuck in it; as a result, the rod swings through an angle $\\alpha$. Assuming $m \\ll M$, find:\n(a) the velocity $v$ of the flying bullet;\n(b) the momentum increment in the system during the impact, and what causes it;\n(c) at what distance $x$ from the upper end of the rod the bullet must strike for the momentum of the system to remain constant during the impact.",
        "hints": [
            "(a) Angular momentum conservation about hinge: $m v l = I \\omega = \\left(\\frac{1}{3} M l^2\\right) \\omega$. Then energy conservation: $\\frac{1}{2} I \\omega^2 = M g \\frac{l}{2} (1 - \\cos \\alpha) = M g l \\sin^2(\\alpha/2)$.",
            "(b) Momentum change is $\\Delta p = p_{\\text{final}} - p_{\\text{initial}} = M v_C - m v$.",
            "(c) Center of percussion condition: $x = \\frac{I}{M r_C} = \\frac{\\frac{1}{3} M l^2}{M (l/2)} = \\frac{2}{3} l$."
        ],
        "answer": "(a) $v = \\frac{M}{m} \\sqrt{\\frac{2}{3} g l} \\sin(\\alpha/2)$; (b) $\\Delta p = -\\frac{1}{6} M \\sqrt{2 g l} \\sin(\\alpha/2)$; (c) $x = \\frac{2}{3} l$",
        "solution": "**1. Part (a): Velocity of the Bullet:**\nConservation of angular momentum about the upper hinge (since $m \\ll M$):\n$$m v l = \\frac{1}{3} M l^2 \\omega \\implies \\omega = \\frac{3 m v}{M l}$$\nEnergy conservation as the rod swings to maximum angle $\\alpha$:\n$$\\frac{1}{2} I \\omega^2 = M g \\left(\\frac{l}{2}\\right) (1 - \\cos \\alpha) = M g l \\sin^2(\\alpha/2)$$\n$$\\frac{1}{6} M l^2 \\left(\\frac{3 m v}{M l}\\right)^2 = M g l \\sin^2(\\alpha/2) \\implies \\frac{3}{2} \\frac{m^2 v^2}{M} = M g l \\sin^2(\\alpha/2)$$\n$$v = \\frac{M}{m} \\sqrt{\\frac{2}{3} g l} \\sin(\\alpha/2)$$\n\n**2. Part (b): Momentum Increment:**\nInitial momentum: $p_i = m v$.\nFinal momentum right after impact (center of mass velocity is $v_C = \\omega l/2$):\n$$p_f = M v_C = M \\left(\\frac{\\omega l}{2}\\right) = M \\frac{l}{2} \\left(\\frac{3 m v}{M l}\\right) = \\frac{3}{2} m v$$\n$$\\Delta p = p_f - p_i = \\frac{3}{2} m v - m v = \\frac{1}{2} m v = \\frac{1}{6} M \\sqrt{2 g l} \\sin(\\alpha/2)$$\nThis momentum change is caused by the horizontal impulsive reaction force exerted by the hinge.\n\n**3. Part (c): Center of Percussion:**\nFor the hinge reaction impulse to be zero during the impact:\n$$x = \\frac{I}{M r_C} = \\frac{\\frac{1}{3} M l^2}{M (l/2)} = \\frac{2}{3} l$$",
        "tags": ["ballistic pendulum", "angular momentum", "center of percussion", "impulse"]
    },
    {
        "id": "1.276",
        "title": "Radial Body Pulled to Center of Rotating Disc",
        "difficulty": 2,
        "question": "A horizontally oriented uniform disc of mass $M$ and radius $R$ rotates freely about a stationary vertical axis passing through its centre. The disc has a radial guide along which a small body of mass $m$ can slide without friction. A light thread passing through the hollow axle is tied to the body. Initially the body was located at the edge of the disc and the whole system rotated with angular velocity $\\omega_0$. Then by means of a force $F$ applied to the thread, the body is slowly pulled to the rotation axis. Find:\n(a) the angular velocity of the system in its final state;\n(b) the work performed by the force $F$.",
        "hints": [
            "No external vertical torque acts on the system, so angular momentum is conserved.",
            "Initial moment of inertia: $I_i = \\frac{1}{2} M R^2 + m R^2$. Final moment of inertia: $I_f = \\frac{1}{2} M R^2$.",
            "By work-energy theorem, work done by $F$ equals the increase in rotational kinetic energy: $A = \\frac{1}{2} I_f \\omega_f^2 - \\frac{1}{2} I_i \\omega_0^2$."
        ],
        "answer": "(a) $\\omega = \\omega_0 \\left(1 + \\frac{2m}{M}\\right)$; (b) $A = \\frac{1}{2} m \\omega_0^2 R^2 \\left(1 + \\frac{2m}{M}\\right)$",
        "solution": "**1. Part (a): Conservation of Angular Momentum:**\n$$L = I_i \\omega_0 = I_f \\omega$$\n$$I_i = \\frac{1}{2} M R^2 + m R^2 = \\frac{1}{2} M R^2 \\left(1 + \\frac{2m}{M}\\right)$$\n$$I_f = \\frac{1}{2} M R^2$$\n$$\\omega = \\frac{I_i}{I_f} \\omega_0 = \\omega_0 \\left(1 + \\frac{2m}{M}\\right)$$\n\n**2. Part (b): Work Performed by Force $F$:**\n$$A = T_f - T_i = \\frac{L^2}{2 I_f} - \\frac{L^2}{2 I_i} = \\frac{L^2}{2} \\left(\\frac{1}{I_f} - \\frac{1}{I_i}\\right) = \\frac{1}{2} I_i \\omega_0^2 \\left(\\frac{I_i}{I_f} - 1\\right)$$\n$$A = \\frac{1}{2} \\left[\\frac{1}{2} M R^2 \\left(1 + \\frac{2m}{M}\\right)\\right] \\omega_0^2 \\left(\\frac{2m}{M}\\right) = \\frac{1}{2} m \\omega_0^2 R^2 \\left(1 + \\frac{2m}{M}\\right)$$",
        "tags": ["angular momentum conservation", "work energy", "rotating disc", "variable inertia"]
    },
    {
        "id": "1.277",
        "title": "Man Walking on a Rotating Disc",
        "difficulty": 2,
        "question": "A man of mass $m_1$ stands on the edge of a horizontal uniform disc of mass $m_2$ and radius $R$ which is capable of rotating freely about a stationary vertical axis through its centre. At a certain moment the man starts moving along the edge of the disc; he shifts over an angle $\\varphi'$ relative to the disc and then stops. The relative velocity varies as $v'(t)$. Assuming the dimensions of the man to be negligible, find:\n(a) the angle through which the disc turns by the moment the man stops;\n(b) the force moment (relative to the rotation axis) with which the man acts on the disc during the motion.",
        "hints": [
            "Total angular momentum of the system is conserved and equals zero.",
            "$L_z = I_{\\text{disc}} \\omega + m_1 R v_{\\text{man}} = 0$.",
            "Man's absolute velocity is $v = v' + \\omega R$.",
            "Substitute and integrate over time to relate angles $\\varphi$ and $\\varphi'$."
        ],
        "answer": "(a) $\\varphi = -\\frac{2 m_1}{2 m_1 + m_2} \\varphi'$; (b) $N = \\frac{m_1 m_2 R}{2 m_1 + m_2} \\frac{dv'}{dt}$",
        "solution": "**1. Part (a): Angle of Rotation:**\nAngular momentum conservation:\n$$I_2 \\omega + m_1 R^2 (\\omega + \\omega') = 0$$\nwhere $I_2 = \\frac{1}{2} m_2 R^2$ and $\\omega' = v'/R$.\n$$\\left(\\frac{1}{2} m_2 R^2 + m_1 R^2\\right) \\omega + m_1 R^2 \\omega' = 0$$\n$$\\left(m_1 + \\frac{1}{2} m_2\\right) d\\varphi + m_1 d\\varphi' = 0$$\nIntegrating from rest:\n$$\\varphi = - \\frac{m_1}{m_1 + m_2/2} \\varphi' = - \\frac{2 m_1}{2 m_1 + m_2} \\varphi'$$\n\n**2. Part (b): Torque Exerted by Man on Disc:**\n$$N = I_2 \\frac{d\\omega}{dt} = \\left(\\frac{1}{2} m_2 R^2\\right) \\left( - \\frac{m_1}{m_1 + m_2/2} \\frac{1}{R} \\frac{dv'}{dt} \\right)$$\n$$|N| = \\frac{m_1 m_2 R}{2 m_1 + m_2} \\frac{dv'}{dt}$$",
        "tags": ["angular momentum conservation", "internal forces", "disc", "reaction torque"]
    },
    {
        "id": "1.278",
        "title": "Frictional Coupling of Two Rotating Discs",
        "difficulty": 1,
        "question": "Two coaxial horizontal discs rotate freely about a vertical axis passing through their centres. The moments of inertia of the discs relative to this axis are $I_1$ and $I_2$, and their angular velocities are $\\omega_1$ and $\\omega_2$. When the upper disc falls onto the lower one, both discs eventually rotate as a single body due to friction. Find:\n(a) the steady-state angular rotation velocity of the discs;\n(b) the work performed by the friction forces in this process.",
        "hints": [
            "Friction forces are internal to the two-disc system, so total angular momentum about the rotation axis is conserved.",
            "Conserved angular momentum: $I_1 \\omega_1 + I_2 \\omega_2 = (I_1 + I_2) \\omega$.",
            "Work of friction equals loss of mechanical kinetic energy: $A = T_f - T_i$."
        ],
        "answer": "(a) $\\omega = \\frac{I_1 \\omega_1 + I_2 \\omega_2}{I_1 + I_2}$; (b) $A = -\\frac{1}{2} \\frac{I_1 I_2}{I_1 + I_2} (\\omega_1 - \\omega_2)^2$",
        "solution": "**1. Part (a): Steady-State Angular Velocity:**\nBy conservation of angular momentum:\n$$I_1 \\omega_1 + I_2 \\omega_2 = (I_1 + I_2) \\omega$$\n$$\\omega = \\frac{I_1 \\omega_1 + I_2 \\omega_2}{I_1 + I_2}$$\n\n**2. Part (b): Work of Friction:**\n$$A = \\Delta T_k = \\frac{1}{2} (I_1 + I_2) \\omega^2 - \\left(\\frac{1}{2} I_1 \\omega_1^2 + \\frac{1}{2} I_2 \\omega_2^2\\right)$$\nSubstituting $\\omega$:\n$$A = \\frac{(I_1 \\omega_1 + I_2 \\omega_2)^2}{2(I_1 + I_2)} - \\frac{I_1 \\omega_1^2 + I_2 \\omega_2^2}{2} = -\\frac{1}{2} \\frac{I_1 I_2}{I_1 + I_2} (\\omega_1 - \\omega_2)^2$$",
        "tags": ["angular momentum conservation", "friction work", "inelastic coupling", "discs"]
    },
    {
        "id": "1.279",
        "title": "Elastic Collision of Disc with Free Rod",
        "difficulty": 3,
        "question": "A small disc and a thin uniform rod of length $l$, whose mass is $\\eta$ times greater than the mass of the disc ($M = \\eta m$), lie on a smooth horizontal plane. The disc is set in motion perpendicular to the rod with velocity $v$ and collides elastically with the end of the rod. Find the velocity $v'$ of the disc and the angular velocity $\\omega$ of the rod after the collision. At what value of $\\eta$ will the disc stop? reverse its direction?",
        "hints": [
            "Let center of mass of rod get velocity $v_C$ and angular velocity $\\omega$ about $C$.",
            "Linear momentum conservation: $m v = m v' + M v_C$.",
            "Angular momentum conservation about rod center $C$: $m v (l/2) = m v' (l/2) + I_C \\omega$, where $I_C = \\frac{1}{12} M l^2$.",
            "Energy conservation for elastic collision: $\\frac{1}{2} m v^2 = \\frac{1}{2} m v'^2 + \\frac{1}{2} M v_C^2 + \\frac{1}{2} I_C \\omega^2$."
        ],
        "answer": "$v' = v \\frac{4 - \\eta}{4 + \\eta}, \\quad \\omega = \\frac{12 v}{(4 + \\eta) l}$; stops for $\\eta = 4$, reverses for $\\eta > 4$",
        "solution": "**1. Conservation Laws:**\nWith $M = \\eta m$:\n- Linear momentum:\n$$m(v - v') = M v_C = \\eta m v_C \\implies v_C = \\frac{v - v'}{\\eta}$$\n- Angular momentum about the rod's center of mass $C$ ($I_C = \\frac{1}{12} M l^2 = \\frac{1}{12} \\eta m l^2$):\n$$m(v - v') \\frac{l}{2} = I_C \\omega = \\frac{1}{12} \\eta m l^2 \\omega \\implies \\omega = \\frac{6 (v - v')}{\\eta l}$$\n- Elastic energy conservation (or restitution coefficient $e = 1$ at contact point):\n$$v_C + \\omega \\left(\\frac{l}{2}\\right) - v' = v$$\nSubstituting $v_C$ and $\\omega$:\n$$\\frac{v - v'}{\\eta} + \\frac{3(v - v')}{\\eta} - v' = v$$\n$$\\frac{4(v - v')}{\\eta} = v + v' \\implies 4(v - v') = \\eta (v + v')$$\n$$(4 - \\eta) v = (4 + \\eta) v'$$\n$$v' = v \\frac{4 - \\eta}{4 + \\eta}$$\n\n**2. Angular Velocity:**\n$$v - v' = v \\left(1 - \\frac{4 - \\eta}{4 + \\eta}\\right) = v \\frac{2\\eta}{4 + \\eta}$$\n$$\\omega = \\frac{6}{\\eta l} \\left(v \\frac{2\\eta}{4 + \\eta}\\right) = \\frac{12 v}{(4 + \\eta) l}$$\n\n**3. Collision Outcome:**\n- Disc stops ($v' = 0$) when $\\eta = 4$.\n- Disc reverses direction ($v' < 0$) when $\\eta > 4$.",
        "tags": ["elastic collision", "rod and disc", "angular momentum", "restitution"]
    },
    {
        "id": "1.280",
        "title": "Tilting a Rotating Gyroscope on a Platform",
        "difficulty": 3,
        "question": "A stationary platform of moment of inertia $I$ can rotate freely about a vertical axis. It supports a motor and a balance weight. A light frame fixed to the motor shaft holds a uniform sphere of moment of inertia $I_0$ rotating freely with angular velocity $\\omega_0$ about a shaft $BB'$ initially coinciding with the platform's vertical rotation axis $OO'$. Find:\n(a) the work performed by the motor in turning the shaft $BB'$ through $90^\\circ$; through $180^\\circ$;\n(b) the moment of external forces maintaining the platform axis in the vertical position after the motor turns the shaft through $90^\\circ$.",
        "hints": [
            "Total angular momentum about the vertical axis is conserved: $L_z = I_0 \\omega_0$.",
            "When turned by angle $\\alpha$, sphere's vertical component of spin is $I_0 \\omega_0 \\cos \\alpha$. Platform must spin at $\\Omega$ such that $I \\Omega + I_0 \\omega_0 \\cos \\alpha = I_0 \\omega_0$.",
            "Work performed equals total kinetic energy change."
        ],
        "answer": "(a) $A_{90^\\circ} = \\frac{1}{2} \\frac{I_0^2 \\omega_0^2}{I}, \\quad A_{180^\\circ} = \\frac{2 I_0^2 \\omega_0^2}{I}$; (b) $N = \\frac{I_0^2 \\omega_0^2}{I}$",
        "solution": "**1. Part (a): Work Done in Reorienting Gyroscope:**\nInitial angular momentum about vertical axis: $L_z = I_0 \\omega_0$.\nWhen the shaft $BB'$ is tilted by angle $\\alpha$ relative to the vertical:\n$$I \\Omega + I_0 \\omega_0 \\cos \\alpha = I_0 \\omega_0 \\implies \\Omega = \\frac{I_0 \\omega_0 (1 - \\cos \\alpha)}{I}$$\nThe kinetic energy change of the system is the platform's rotational energy:\n$$A = \\frac{1}{2} I \\Omega^2 = \\frac{I_0^2 \\omega_0^2 (1 - \\cos \\alpha)^2}{2 I}$$\n- For $\\alpha = 90^\\circ$ ($\\cos 90^\\circ = 0$):\n$$A_{90^\\circ} = \\frac{I_0^2 \\omega_0^2}{2 I}$$\n- For $\\alpha = 180^\\circ$ ($\\cos 180^\\circ = -1$):\n$$A_{180^\\circ} = \\frac{I_0^2 \\omega_0^2 (1 - (-1))^2}{2 I} = \\frac{4 I_0^2 \\omega_0^2}{2 I} = \\frac{2 I_0^2 \\omega_0^2}{I}$$\n\n**2. Part (b): Gyroscopic Moment:**\nAt $\\alpha = 90^\\circ$, the platform rotates at $\\Omega = \\frac{I_0 \\omega_0}{I}$ about the vertical axis while the sphere spins with $\\omega_0$ horizontally. The gyroscopic couple is:\n$$N = I_0 \\omega_0 \\Omega = I_0 \\omega_0 \\left(\\frac{I_0 \\omega_0}{I}\\right) = \\frac{I_0^2 \\omega_0^2}{I}$$",
        "tags": ["gyroscope", "platform", "angular momentum conservation", "gyroscopic moment"]
    },
    {
        "id": "1.281",
        "title": "Horizontal Rod on Vertical Axis: Bearing Reactions",
        "difficulty": 2,
        "question": "A horizontally oriented uniform rod $AB$ of mass $m = 1.40\\text{ kg}$ and length $l_0 = 100\\text{ cm}$ rotates freely about a stationary vertical axis $OO'$ passing through its end $A$. Point $A$ is located at the middle of the vertical axle $OO'$ whose total length is $l = 55\\text{ cm}$. At what angular velocity $\\omega$ of the rod will the horizontal component of the force acting on the lower bearing of axis $OO'$ equal zero? What is then the horizontal force on the upper bearing?",
        "hints": [
            "Centrifugal force of the rotating rod is $F_{cf} = m \\omega^2 (l_0/2)$.",
            "Gravitational force produces an overturning torque: $N_g = m g (l_0/2)$.",
            "Taking torque about the upper bearing, equate total moment to zero so lower bearing reaction is zero."
        ],
        "answer": "$\\omega = \\sqrt{\\frac{2g}{l}} = 6.0\\text{ rad/s}, \\quad F = \\frac{m g l_0}{l} = 25\\text{ N}$",
        "solution": "**1. Condition for Zero Lower Bearing Reaction:**\nThe rod rotates in a horizontal plane passing through the middle of the axle (distance $l/2$ from each bearing).\nForces and torques acting on the axle from the rod:\n- Centrifugal force $F_{cf} = m \\omega^2 (l_0/2)$ directed horizontally.\n- Overturning torque due to gravity: $N_g = m g (l_0/2)$.\nTaking moments about the upper bearing to find the lower bearing force $F_1$:\n$$F_1 l + m g \\left(\\frac{l_0}{2}\\right) - F_{cf} \\left(\\frac{l}{2}\\right) = 0$$\nFor $F_1 = 0$:\n$$m g \\left(\\frac{l_0}{2}\\right) = m \\omega^2 \\left(\\frac{l_0}{2}\\right) \\left(\\frac{l}{2}\\right) \\implies \\omega^2 \\left(\\frac{l}{2}\\right) = g$$\n$$\\omega = \\sqrt{\\frac{2g}{l}}$$\n\n**2. Numerical Calculation:**\n$$\\omega = \\sqrt{\\frac{2 \\times 9.8}{0.55}} = \\sqrt{\\frac{19.6}{0.55}} \\approx 6.0\\text{ rad/s}$$\n\n**3. Upper Bearing Force:**\nHorizontal force balance: $F_{\\text{upper}} = F_{cf} = m \\omega^2 (l_0/2) = m \\left(\\frac{2g}{l}\\right) \\left(\\frac{l_0}{2}\\right) = \\frac{m g l_0}{l}$:\n$$F_{\\text{upper}} = \\frac{1.40 \\times 9.8 \\times 1.0}{0.55} \\approx 25\\text{ N}$$",
        "tags": ["bearing reaction", "centrifugal force", "rotating axle", "torque balance"]
    },
    {
        "id": "1.282",
        "title": "Angular Momentum of an Inclined Rotating Rod",
        "difficulty": 2,
        "question": "The middle of a uniform rod of mass $m$ and length $l$ is rigidly fixed to a vertical axis $OO'$ at an angle $\\theta$. The system rotates without friction at constant angular velocity $\\omega$. Find:\n(a) the rod's angular momentum $\\mathbf{M}$ relative to its midpoint $C$, and its projection on the rotation axis;\n(b) the modulus of the vector increment $|\\Delta \\mathbf{M}|$ over a half-turn;\n(c) the moment of external forces $N$ acting on the axle $OO'$ during rotation.",
        "hints": [
            "(a) Inertia tensor components: about axis perpendicular to rod in plane of motion, $I = \\frac{1}{12} m l^2$.",
            "Component of $\\boldsymbol{\\omega}$ perpendicular to rod is $\\omega \\sin \\theta$.",
            "Then $|\\mathbf{M}| = I \\omega \\sin \\theta = \\frac{1}{12} m l^2 \\omega \\sin \\theta$.",
            "(b) During a half-turn, the horizontal component of $\\mathbf{M}$ reverses direction: $|\\Delta \\mathbf{M}| = 2 M_\\perp$.",
            "(c) $N = |\\frac{d\\mathbf{M}}{dt}| = \\omega M_\\perp$."
        ],
        "answer": "(a) $M = \\frac{1}{12} m \\omega l^2 \\sin \\theta, \\quad M_z = \\frac{1}{12} m \\omega l^2 \\sin^2 \\theta$; (b) $|\\Delta \\mathbf{M}| = \\frac{1}{6} m \\omega l^2 \\sin \\theta \\cos \\theta$; (c) $N = \\frac{1}{24} m \\omega^2 l^2 \\sin 2\\theta$",
        "solution": "**1. Part (a): Angular Momentum:**\nThe rod has zero moment of inertia along its length ($I_\\parallel = 0$) and $I_\\perp = \\frac{1}{12} m l^2$ perpendicular to its length.\nThe angular velocity component perpendicular to the rod is $\\omega_\\perp = \\omega \\sin \\theta$.\nThus, the total angular momentum vector is perpendicular to the rod:\n$$M = I_\\perp \\omega_\\perp = \\frac{1}{12} m l^2 \\omega \\sin \\theta$$\nIts projection along the vertical rotation axis is:\n$$M_z = M \\sin \\theta = \\frac{1}{12} m \\omega l^2 \\sin^2 \\theta$$\n\n**2. Part (b): Increment Over Half-Turn:**\nThe horizontal component of $\\mathbf{M}$ has magnitude $M_h = M \\cos \\theta = \\frac{1}{12} m \\omega l^2 \\sin \\theta \\cos \\theta$.\nAfter a half-turn ($180^\\circ$), this horizontal vector reverses sign, so:\n$$|\\Delta \\mathbf{M}| = 2 M_h = \\frac{1}{6} m \\omega l^2 \\sin \\theta \\cos \\theta = \\frac{1}{12} m \\omega l^2 \\sin 2\\theta$$\n\n**3. Part (c): Torque of External Forces:**\n$$\\mathbf{N} = \\frac{d\\mathbf{M}}{dt} = \\boldsymbol{\\omega} \\times \\mathbf{M}$$\n$$N = \\omega M_h = \\omega \\left(\\frac{1}{12} m \\omega l^2 \\sin \\theta \\cos \\theta\\right) = \\frac{1}{24} m \\omega^2 l^2 \\sin 2\\theta$$",
        "tags": ["angular momentum", "precession", "rotating rod", "gyroscopic torque"]
    },
    {
        "id": "1.283",
        "title": "Precession of a Heavy Top",
        "difficulty": 2,
        "question": "A top of mass $m = 0.50\\text{ kg}$, tilted at an angle $\\theta = 30^\\circ$ to the vertical, precesses due to gravity. The moment of inertia of the top relative to its symmetry axis is $I = 2.0\\text{ g}\\cdot\\text{m}^2$, its proper angular velocity is $\\omega = 350\\text{ rad/s}$, and the distance from the pivot point to the centre of inertia is $l = 10\\text{ cm}$. Find:\n(a) the angular velocity of precession $\\omega'$;\n(b) the horizontal reaction force acting on the top at the pivot point.",
        "hints": [
            "Gyroscopic precession equation: $\\mathbf{N} = \\boldsymbol{\\omega}' \\times \\mathbf{L}$.",
            "Gravitational torque: $N = m g l \\sin \\theta$. Angular momentum along top axis: $L = I \\omega$.",
            "Since $\\mathbf{N} = \\omega' L \\sin \\theta$, we get $\\omega' = \\frac{m g l}{I \\omega}$.",
            "The center of mass circles at radius $r = l \\sin \\theta$ with angular speed $\\omega'$, so $F_h = m \\omega'^2 l \\sin \\theta$."
        ],
        "answer": "(a) $\\omega' = \\frac{m g l}{I \\omega} = 0.70\\text{ rad/s}$; (b) $F_h = m \\omega'^2 l \\sin \\theta = 10\\text{ mN}$",
        "solution": "**1. Part (a): Precession Angular Velocity:**\nThe torque due to gravity about the support point is:\n$$N = m g l \\sin \\theta$$\nIn steady precession:\n$$N = \\omega' L \\sin \\theta = \\omega' (I \\omega) \\sin \\theta$$\n$$\\omega' = \\frac{m g l}{I \\omega}$$\nNumerical calculation:\n$$\\omega' = \\frac{0.50 \\times 9.8 \\times 0.10}{2.0 \\times 10^{-3} \\times 350} = \\frac{0.49}{0.70} = 0.70\\text{ rad/s}$$\n\n**2. Part (b): Horizontal Reaction Force:**\nThe center of mass moves in a horizontal circle of radius $R_c = l \\sin \\theta$ with angular velocity $\\omega'$:\n$$F_h = m \\omega'^2 R_c = m \\omega'^2 l \\sin \\theta$$\n$$F_h = 0.50 \\times (0.70)^2 \\times 0.10 \\times \\sin 30^\\circ = 0.50 \\times 0.49 \\times 0.10 \\times 0.5 = 1.2 \\times 10^{-2}\\text{ N} \\approx 10\\text{ mN}$$",
        "tags": ["precession", "gyroscope", "top", "reaction force"]
    },
    {
        "id": "1.284",
        "title": "Gyroscope in an Accelerating Elevator",
        "difficulty": 2,
        "question": "A gyroscope consisting of a uniform disc of radius $R = 5.0\\text{ cm}$ at the end of a light rod of length $l = 10\\text{ cm}$ is mounted on the floor of an elevator going up with acceleration $w = 2.0\\text{ m/s}^2$. The other end of the rod is hinged. The gyroscope precesses with frequency $n = 0.5\\text{ rps}$. Neglecting rod mass and friction, find the spin angular velocity $\\omega$ of the disc.",
        "hints": [
            "Effective gravity in the elevator is $g^* = g + w$.",
            "Precession angular velocity is $\\Omega = 2\\pi n$.",
            "Precession formula with effective gravity: $\\Omega = \\frac{m g^* l}{I \\omega}$.",
            "Disc moment of inertia is $I = \\frac{1}{2} m R^2$."
        ],
        "answer": "$\\omega = \\frac{(g + w) l}{\\pi n R^2} = 3.0 \\times 10^2\\text{ rad/s}$",
        "solution": "**1. Effective Acceleration and Precession:**\nIn the frame of the elevator:\n$$g^* = g + w$$\nThe torque about the hinge is:\n$$N = m g^* l$$\nThe angular momentum of the disc is $L = I \\omega = \\frac{1}{2} m R^2 \\omega$.\nThe precession frequency is $\\Omega = 2\\pi n$.\n\n**2. Precession Relation:**\n$$N = \\Omega L \\implies m (g + w) l = (2\\pi n) \\left(\\frac{1}{2} m R^2 \\omega\\right) = \\pi n m R^2 \\omega$$\n$$\\omega = \\frac{(g + w) l}{\\pi n R^2}$$\n\n**3. Numerical Calculation:**\n$$\\omega = \\frac{(9.8 + 2.0) \\times 0.10}{\\pi \\times 0.5 \\times (0.05)^2} = \\frac{1.18}{\\pi \\times 0.5 \\times 0.0025} = \\frac{1.18}{0.003927} \\approx 3.0 \\times 10^2\\text{ rad/s}$$",
        "tags": ["gyroscope", "precession", "accelerating frame", "elevator"]
    },
    {
        "id": "1.285",
        "title": "Top on a Horizontally Accelerating Block",
        "difficulty": 2,
        "question": "A top of mass $m = 1.0\\text{ kg}$ and moment of inertia $I = 4.0\\text{ g}\\cdot\\text{m}^2$ spins with angular velocity $\\omega = 310\\text{ rad/s}$. Its support point is on a block moving horizontally with constant acceleration $w = 1.0\\text{ m/s}^2$. The distance from the support to the center of inertia is $l = 10\\text{ cm}$. Find the magnitude and direction of the angular velocity of precession $\\omega'$.",
        "hints": [
            "In the accelerating frame of the block, effective gravitational acceleration is $\\mathbf{g}^* = \\mathbf{g} - \\mathbf{w}$, with modulus $g^* = \\sqrt{g^2 + w^2}$.",
            "Effective gravity is tilted at angle $\\theta = \\arctan(w/g)$ relative to the vertical.",
            "Precession occurs around the direction of $\\mathbf{g}^*$ with rate $\\omega' = \\frac{m g^* l}{I \\omega}$."
        ],
        "answer": "$\\omega' = \\frac{m l \\sqrt{g^2 + w^2}}{I \\omega} = 0.80\\text{ rad/s}$; inclined at $\\theta = \\arctan(w/g) \\approx 6^\\circ$ to the vertical",
        "solution": "**1. Effective Gravitational Field:**\nIn the reference frame of the accelerating block, the inertial force is $-m\\mathbf{w}$.\nThe effective gravitational field vector is:\n$$\\mathbf{g}^* = \\mathbf{g} - \\mathbf{w}$$\n$$g^* = \\sqrt{g^2 + w^2}$$\nThis vector is inclined to the vertical at angle:\n$$\\theta = \\arctan\\left(\\frac{w}{g}\\right) = \\arctan\\left(\\frac{1.0}{9.8}\\right) \\approx \\arctan(0.102) \\approx 5.8^\\circ \\approx 6^\\circ$$\n\n**2. Precession Rate:**\nThe top precesses about the axis of the effective field $\\mathbf{g}^*$ with angular rate:\n$$\\omega' = \\frac{m g^* l}{I \\omega} = \\frac{m l \\sqrt{g^2 + w^2}}{I \\omega}$$\n\n**3. Numerical Calculation:**\n$$g^* = \\sqrt{9.8^2 + 1.0^2} = \\sqrt{96.04 + 1.0} \\approx 9.85\\text{ m/s}^2$$\n$$\\omega' = \\frac{1.0 \\times 9.85 \\times 0.10}{4.0 \\times 10^{-3} \\times 310} = \\frac{0.985}{1.24} \\approx 0.80\\text{ rad/s}$$",
        "tags": ["precession", "accelerating frame", "effective gravity", "top"]
    },
    {
        "id": "1.286",
        "title": "Gyroscopic Forces on Bearings of Rotating Sphere",
        "difficulty": 2,
        "question": "A uniform sphere of mass $m = 5.0\\text{ kg}$ and radius $R = 6.0\\text{ cm}$ rotates with angular velocity $\\omega = 1250\\text{ rad/s}$ about a horizontal axle passing through its centre and mounted in bearings separated by $l = 15\\text{ cm}$. The base is rotated about a vertical axis with angular velocity $\\omega' = 5.0\\text{ rad/s}$. Find the modulus of the gyroscopic forces exerted on the bearings.",
        "hints": [
            "Angular momentum of sphere is $L = I \\omega = \\frac{2}{5} m R^2 \\omega$.",
            "Gyroscopic couple produced by forced precession: $N = \\omega' L = \\frac{2}{5} m R^2 \\omega \\omega'$.",
            "This torque is balanced by a couple of forces $F'$ at bearings separated by $l$: $N = F' l$."
        ],
        "answer": "$F' = \\frac{2}{5} \\frac{m R^2 \\omega \\omega'}{l} = 0.30\\text{ kN}$",
        "solution": "**1. Gyroscopic Torque:**\nFor a uniform solid sphere:\n$$I = \\frac{2}{5} m R^2$$\n$$L = I \\omega = \\frac{2}{5} m R^2 \\omega$$\nThe forced precession angular velocity is $\\omega'$. The gyroscopic torque is:\n$$N = \\omega' L = \\frac{2}{5} m R^2 \\omega \\omega'$$\n\n**2. Bearing Forces:**\nThe bearings are separated by distance $l$, so the equal and opposite gyroscopic forces satisfy:\n$$F' l = N \\implies F' = \\frac{2}{5} \\frac{m R^2 \\omega \\omega'}{l}$$\n\n**3. Numerical Calculation:**\n$$F' = \\frac{2}{5} \\frac{5.0 \\times (0.06)^2 \\times 1250 \\times 5.0}{0.15} = \\frac{2 \\times 0.0036 \\times 6250}{0.15} = \\frac{45}{0.15} = 300\\text{ N} = 0.30\\text{ kN}$$",
        "tags": ["gyroscopic force", "bearings", "forced precession", "sphere"]
    },
    {
        "id": "1.287",
        "title": "Maximum Gyroscopic Forces from Oscillating Gyroscope",
        "difficulty": 2,
        "question": "A cylindrical disc of a gyroscope of mass $m = 15\\text{ kg}$ and radius $r = 5.0\\text{ cm}$ spins with angular velocity $\\omega = 330\\text{ rad/s}$. The distance between the bearings in which the axle is mounted is $l = 15\\text{ cm}$. The axle is forced to oscillate about a horizontal axis with period $T = 1.0\\text{ s}$ and amplitude $\\varphi_m = 20^\\circ$. Find the maximum value of the gyroscopic forces exerted by the axle on the bearings.",
        "hints": [
            "Oscillation of axle: $\\varphi(t) = \\varphi_m \\sin(\\Omega t)$, where $\\Omega = 2\\pi / T$.",
            "Maximum precession angular velocity: $\\Omega_{\\max} = \\varphi_m \\Omega = \\frac{2\\pi \\varphi_m}{T}$.",
            "Maximum gyroscopic couple: $N_{\\max} = I \\omega \\Omega_{\\max} = \\left(\\frac{1}{2} m r^2\\right) \\omega \\left(\\frac{2\\pi \\varphi_m}{T}\\right) = \\frac{\\pi m r^2 \\omega \\varphi_m}{T}$.",
            "Bearing force is $F_{\\max} = N_{\\max} / l$."
        ],
        "answer": "$F_{\\max} = \\frac{\\pi m r^2 \\omega \\varphi_m}{l T} = 0.09\\text{ kN}$",
        "solution": "**1. Oscillation Angular Velocity:**\nThe axle oscillates as $\\varphi(t) = \\varphi_m \\cos\\left(\\frac{2\\pi}{T} t\\right)$.\nThe angular velocity of forced oscillation is:\n$$\\Omega(t) = \\dot{\\varphi} = - \\frac{2\\pi \\varphi_m}{T} \\sin\\left(\\frac{2\\pi}{T} t\\right)$$\n$$\\Omega_{\\max} = \\frac{2\\pi \\varphi_m}{T}$$\nwith $\\varphi_m = 20^\\circ = 20 \\times \\frac{\\pi}{180} = \\frac{\\pi}{9}\\text{ rad}$.\n\n**2. Maximum Gyroscopic Torque and Force:**\n$$N_{\\max} = I \\omega \\Omega_{\\max} = \\left(\\frac{1}{2} m r^2\\right) \\omega \\left(\\frac{2\\pi \\varphi_m}{T}\\right) = \\frac{\\pi m r^2 \\omega \\varphi_m}{T}$$\n$$F_{\\max} = \\frac{N_{\\max}}{l} = \\frac{\\pi m r^2 \\omega \\varphi_m}{l T}$$\n\n**3. Numerical Calculation:**\n$$F_{\\max} = \\frac{\\pi \\times 15 \\times (0.05)^2 \\times 330 \\times (20 \\times \\pi / 180)}{0.15 \\times 1.0} \\approx \\frac{38.9 \\times 0.349}{0.15} \\approx \\frac{13.6}{0.15} \\approx 90\\text{ N} = 0.09\\text{ kN}$$",
        "tags": ["gyroscopic torque", "angular oscillation", "bearings", "amplitude"]
    },
    {
        "id": "1.288",
        "title": "Gyroscopic Couple of a Ship's Turbine",
        "difficulty": 2,
        "question": "A ship moves with velocity $v = 36\\text{ km/h}$ along a circular arc of radius $R = 200\\text{ m}$. Find the moment of the gyroscopic forces exerted on the bearings by the shaft of a flywheel whose moment of inertia is $I = 3.8 \\times 10^3\\text{ kg}\\cdot\\text{m}^2$ and rotation speed is $n = 300\\text{ rpm}$. The rotation axis is oriented along the length of the ship.",
        "hints": [
            "The turn of the ship produces a precession of the flywheel axis about the vertical with $\\omega' = v / R$.",
            "Spin angular velocity is $\\omega = 2\\pi n$.",
            "Gyroscopic couple is $N = I \\omega \\omega' = \\frac{2\\pi n I v}{R}$."
        ],
        "answer": "$N = \\frac{2\\pi n I v}{R} = 6.0\\text{ kN}\\cdot\\text{m}$",
        "solution": "**1. Gyroscopic Precession:**\nVelocity of ship: $v = 36\\text{ km/h} = 10\\text{ m/s}$.\nPrecession rate about vertical axis:\n$$\\omega' = \\frac{v}{R} = \\frac{10}{200} = 0.050\\text{ rad/s}$$\nFlywheel spin angular velocity:\n$$\\omega = 2\\pi n = 2\\pi \\left(\\frac{300}{60}\\right) = 10\\pi\\text{ rad/s} \\approx 31.4\\text{ rad/s}$$\n\n**2. Gyroscopic Moment:**\n$$N = I \\omega \\omega' = \\frac{2\\pi n I v}{R}$$\n$$N = (3.8 \\times 10^3) \\times (10\\pi) \\times 0.050 = 3.8 \\times 10^3 \\times 0.50\\pi \\approx 5.97 \\times 10^3\\text{ N}\\cdot\\text{m} \\approx 6.0\\text{ kN}\\cdot\\text{m}$$",
        "tags": ["gyroscopic moment", "ship", "turbine", "turning arc"]
    },
    {
        "id": "1.289",
        "title": "Gyroscopic Forces on Rails from Locomotive Turbine",
        "difficulty": 2,
        "question": "A locomotive is propelled by a turbine whose axle is parallel to the wheel axles and whose rotation direction coincides with that of the wheels. The moment of inertia of the turbine rotor is $I = 240\\text{ kg}\\cdot\\text{m}^2$. Find the additional vertical force exerted by the gyroscopic forces on the rails when the locomotive rounds a curve of radius $R = 250\\text{ m}$ with velocity $v = 50\\text{ km/h}$. The track gauge is $l = 1.5\\text{ m}$, and the turbine rotates at $n = 1500\\text{ rpm}$.",
        "hints": [
            "The locomotive turns in a horizontal plane with rate $\\omega' = v / R$.",
            "The turbine spins about a transverse horizontal axle with angular velocity $\\omega = 2\\pi n$.",
            "The gyroscopic torque is $N = I \\omega \\omega' = \\frac{2\\pi n I v}{R}$.",
            "This couple causes an additional vertical load $F_{\\text{add}} = N / l$ on the outer rail and an equal decrease on the inner rail."
        ],
        "answer": "$F_{\\text{add}} = \\frac{2\\pi n I v}{R l} = 1.4\\text{ kN}$",
        "solution": "**1. Gyroscopic Torque:**\nSpeed of locomotive: $v = 50\\text{ km/h} = \\frac{50}{3.6} \\approx 13.89\\text{ m/s}$.\nPrecession rate about vertical axis:\n$$\\omega' = \\frac{v}{R}$$\nSpin angular velocity:\n$$\\omega = 2\\pi n = 2\\pi \\left(\\frac{1500}{60}\\right) = 50\\pi\\text{ rad/s}$$\nGyroscopic couple:\n$$N = I \\omega \\omega' = \\frac{2\\pi n I v}{R}$$\n\n**2. Additional Rail Force:**\nThe gyroscopic couple acts in a vertical transverse plane, loading the outer rail and unloading the inner rail by:\n$$F_{\\text{add}} = \\frac{N}{l} = \\frac{2\\pi n I v}{R l}$$\n\n**3. Numerical Calculation:**\n$$F_{\\text{add}} = \\frac{50\\pi \\times 240 \\times 13.89}{250 \\times 1.5} = \\frac{12000\\pi \\times 13.89}{375} \\approx 32\\pi \\times 13.89 \\approx 1.40 \\times 10^3\\text{ N} = 1.4\\text{ kN}$$\nThe force on the outer rail increases by $1.4\\text{ kN}$ while that on the inner rail decreases by the same amount.",
        "tags": ["gyroscopic force", "locomotive", "track load", "rail curvature"]
    }
]
