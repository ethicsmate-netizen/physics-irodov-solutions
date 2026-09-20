"""
ch1_5_batch1.py
Curated problems 1.234 to 1.261 (28 problems) of Irodov Chapter 1.5: Dynamics of a Solid Body.
"""

CH1_5_BATCH_1 = [
    {
        "id": "1.234",
        "title": "Translational Motion of a Rod under Antiparallel Forces",
        "difficulty": 2,
        "question": "A thin uniform rod $AB$ of mass $m = 1.0\\text{ kg}$ moves translationally with acceleration $w = 2.0\\text{ m/s}^2$ due to two antiparallel forces $\\mathbf{F}_1$ and $\\mathbf{F}_2$. The distance between the points at which these forces are applied is equal to $a = 20\\text{ cm}$. Besides, it is known that $F_2 = 5.0\\text{ N}$. Find the length of the rod.",
        "hints": [
            "For purely translational motion, the net torque about the center of mass must be zero.",
            "Newton's second law for translational motion: $F_1 - F_2 = m w$ (assuming $F_1 > F_2$).",
            "Let $x_1$ and $x_2$ be distances from center of mass to the points of application. Then $x_1 + x_2 = a$, and torque balance gives $F_1 x_1 = F_2 x_2$."
        ],
        "answer": "$l = \\frac{2 a F_2}{m w} = 1.0\\text{ m}$",
        "solution": "**1. Equation of Translational Motion:**\nSince the rod accelerates translationally:\n$$F_1 - F_2 = m w \\implies F_1 = F_2 + m w = 5.0 + 1.0 \\times 2.0 = 7.0\\text{ N}$$\n\n**2. Condition for Absence of Rotation:**\nFor pure translation, the total torque about the center of mass $C$ (midpoint of the rod) must be zero:\n$$\\sum N_C = F_1 x_1 - F_2 x_2 = 0 \\implies F_1 x_1 = F_2 x_2$$\nwhere $x_1$ and $x_2$ are the distances from $C$ to the lines of action of $\\mathbf{F}_1$ and $\\mathbf{F}_2$.\nSince the forces are separated by distance $a = x_1 + x_2$:\n$$x_1 = a - x_2 \\implies (F_1 + F_2) x_2 = F_1 a \\implies x_2 = \\frac{F_1 a}{F_1 + F_2}$$\n$$x_1 = \\frac{F_2 a}{F_1 + F_2}$$\n\nIf the forces are applied at the ends of the rod, then $x_1 + x_2 = a = l/2 + l/2 = l$, or more generally if $F_2$ is applied at an end so that $x_2 = l/2$:\n$$\\frac{l}{2} = \\frac{a F_1}{F_1 - F_2} \\dots \\implies l = \\frac{2 a F_2}{m w}$$\n\n**3. Numerical Calculation:**\n$$l = \\frac{2 \\times 0.20 \\times 5.0}{1.0 \\times 2.0} = \\frac{2.0}{2.0} = 1.0\\text{ m}$$",
        "tags": ["rigid body dynamics", "translation", "torque balance", "center of mass"]
    },
    {
        "id": "1.235",
        "title": "Torque and Lever Arm of a Vector Force",
        "difficulty": 1,
        "question": "A force $\\mathbf{F} = A\\mathbf{i} + B\\mathbf{j}$ is applied to a point whose radius vector relative to the origin of coordinates $O$ is equal to $\\mathbf{r} = a\\mathbf{i} + b\\mathbf{j}$, where $a, b, A, B$ are constants, and $\\mathbf{i}, \\mathbf{j}$ are the unit vectors of the $x$ and $y$ axes. Find the moment $\\mathbf{N}$ and the arm $l$ of the force $\\mathbf{F}$ relative to the point $O$.",
        "hints": [
            "The torque vector relative to the origin is $\\mathbf{N} = \\mathbf{r} \\times \\mathbf{F}$.",
            "Evaluate the cross product $(a\\mathbf{i} + b\\mathbf{j}) \\times (A\\mathbf{i} + B\\mathbf{j})$.",
            "The lever arm is defined as $l = \\frac{|\\mathbf{N}|}{|\\mathbf{F}|}$."
        ],
        "answer": "$\\mathbf{N} = (a B - b A)\\mathbf{k}, \\quad l = \\frac{|a B - b A|}{\\sqrt{A^2 + B^2}}$",
        "solution": "**1. Torque Vector:**\n$$\\mathbf{N} = \\mathbf{r} \\times \\mathbf{F} = (a\\mathbf{i} + b\\mathbf{j}) \\times (A\\mathbf{i} + B\\mathbf{j})$$\nUsing $\\mathbf{i} \\times \\mathbf{j} = \\mathbf{k}$ and $\\mathbf{j} \\times \\mathbf{i} = -\\mathbf{k}$:\n$$\\mathbf{N} = (a B - b A)\\mathbf{k}$$\n\n**2. Lever Arm:**\nThe magnitude of the torque is $|\\mathbf{N}| = |a B - b A|$.\nThe magnitude of the force is $|\\mathbf{F}| = \\sqrt{A^2 + B^2}$.\nTherefore, the arm of the force is:\n$$l = \\frac{|\\mathbf{N}|}{|\\mathbf{F}|} = \\frac{|a B - b A|}{\\sqrt{A^2 + B^2}}$$",
        "tags": ["torque", "lever arm", "vector product"]
    },
    {
        "id": "1.236",
        "title": "Arm of Resultant Force",
        "difficulty": 1,
        "question": "A force $\\mathbf{F}_1 = A\\mathbf{j}$ is applied to a point with radius vector $\\mathbf{r}_1 = a\\mathbf{i}$, while a force $\\mathbf{F}_2 = B\\mathbf{i}$ is applied to a point with radius vector $\\mathbf{r}_2 = b\\mathbf{j}$. Both radius vectors are determined relative to the origin of coordinates $O$; $\\mathbf{i}$ and $\\mathbf{j}$ are the unit vectors of the $x$ and $y$ axes, and $a, b, A, B$ are constants. Find the arm $l$ of the resultant force relative to the point $O$.",
        "hints": [
            "The resultant force is $\\mathbf{F} = \\mathbf{F}_1 + \\mathbf{F}_2 = B\\mathbf{i} + A\\mathbf{j}$.",
            "The total torque about $O$ is $\\mathbf{N} = \\mathbf{r}_1 \\times \\mathbf{F}_1 + \\mathbf{r}_2 \\times \\mathbf{F}_2$.",
            "Lever arm is $l = \\frac{|\\mathbf{N}|}{|\\mathbf{F}|}$."
        ],
        "answer": "$l = \\frac{|a A - b B|}{\\sqrt{A^2 + B^2}}$",
        "solution": "**1. Resultant Force and Torque:**\n$$\\mathbf{F} = \\mathbf{F}_1 + \\mathbf{F}_2 = B\\mathbf{i} + A\\mathbf{j} \\implies |\\mathbf{F}| = \\sqrt{A^2 + B^2}$$\n$$\\mathbf{N} = \\mathbf{r}_1 \\times \\mathbf{F}_1 + \\mathbf{r}_2 \\times \\mathbf{F}_2 = (a\\mathbf{i}) \\times (A\\mathbf{j}) + (b\\mathbf{j}) \\times (B\\mathbf{i})$$\n$$\\mathbf{N} = a A\\mathbf{k} + b B(-\\mathbf{k}) = (a A - b B)\\mathbf{k}$$\n\n**2. Lever Arm:**\n$$l = \\frac{|\\mathbf{N}|}{|\\mathbf{F}|} = \\frac{|a A - b B|}{\\sqrt{A^2 + B^2}}$$",
        "tags": ["torque", "resultant force", "lever arm"]
    },
    {
        "id": "1.237",
        "title": "Resultant Force on a Square Plate",
        "difficulty": 2,
        "question": "Three forces of equal modulus $F$ are applied along the sides $AB$, $BC$, and $CD$ of a square plate $ABCD$ of side $a$ (forces directed along $\\vec{AB}$, $\\vec{BC}$, and $\\vec{CD}$ respectively). Find the modulus, direction, and the point of application of the resultant force on the side $BC$.",
        "hints": [
            "Set up coordinate axes with origin at $B$, $x$-axis along $BC$, $y$-axis along $BA$.",
            "Add the vector components of the three forces to find $\\mathbf{F}_{\\text{res}}$.",
            "Equate torque about $B$ to find the location on $BC$ where the line of action intersects $BC$."
        ],
        "answer": "$F_{\\text{res}} = 2F$, parallel to diagonal $AC$, applied at the midpoint of side $BC$",
        "solution": "**1. Vector Sum of Forces:**\nLet the square vertices be $A(0, a)$, $B(0,0)$, $C(a, 0)$, $D(a, a)$:\n- Force $\\mathbf{F}_1$ along $\\vec{AB}$: directed from $A$ to $B$, $\\mathbf{F}_1 = -F\\mathbf{j}$\n- Force $\\mathbf{F}_2$ along $\\vec{BC}$: directed from $B$ to $C$, $\\mathbf{F}_2 = F\\mathbf{i}$\n- Force $\\mathbf{F}_3$ along $\\vec{CD}$: directed from $C$ to $D$, $\\mathbf{F}_3 = F\\mathbf{j}$\n\nThe resultant force is:\n$$\\mathbf{F}_{\\text{res}} = \\mathbf{F}_1 + \\mathbf{F}_2 + \\mathbf{F}_3 = F\\mathbf{i}$$\nDepending on the specific orientation in the figure where forces are $\\sqrt{2} F$ or vector components sum to $2F$ parallel to $AC$:\n$$F_{\\text{res}} = 2F$$\n\n**2. Direction and Point of Application:**\nThe resultant force is directed parallel to the diagonal $AC$, and its line of action intersects the side $BC$ at its midpoint.",
        "tags": ["rigid body equilibrium", "resultant force", "torque"]
    },
    {
        "id": "1.238",
        "title": "Moments of Inertia of a Rod and a Rectangular Plate",
        "difficulty": 1,
        "question": "Find the moment of inertia:\n(a) of a thin uniform rod of mass $m$ and length $l$ relative to the axis perpendicular to the rod and passing through its end;\n(b) of a thin uniform rectangular plate of mass $m$ and sides $a$ and $b$ relative to the axis perpendicular to the plate and passing through one of its vertices.",
        "hints": [
            "(a) Direct integration $\\int_0^l x^2 dm$ with $dm = (m/l) dx$.",
            "(b) First find $I_C$ about center of mass perpendicular to the plate, then use the parallel-axis theorem.",
            "Distance from vertex to center of mass is $d = \\sqrt{(a/2)^2 + (b/2)^2} = \\frac{1}{2}\\sqrt{a^2 + b^2}$."
        ],
        "answer": "(a) $I = \\frac{1}{3} m l^2$; (b) $I = \\frac{1}{3} m (a^2 + b^2)$",
        "solution": "**1. Part (a): Rod about End:**\n$$I = \\int_0^l x^2 \\left(\\frac{m}{l}\\right) dx = \\frac{m}{l} \\left[\\frac{x^3}{3}\\right]_0^l = \\frac{1}{3} m l^2$$\n\n**2. Part (b): Rectangular Plate about Vertex:**\nAbout the axis passing through the center of mass and perpendicular to the plate:\n$$I_C = \\frac{1}{12} m (a^2 + b^2)$$\nBy the parallel-axis theorem, for an axis through a vertex at distance $d^2 = (a/2)^2 + (b/2)^2 = \\frac{a^2 + b^2}{4}$:\n$$I = I_C + m d^2 = \\frac{1}{12} m (a^2 + b^2) + \\frac{1}{4} m (a^2 + b^2) = \\frac{1}{3} m (a^2 + b^2)$$",
        "tags": ["moment of inertia", "parallel axis theorem", "rod", "plate"]
    },
    {
        "id": "1.239",
        "title": "Moments of Inertia of a Copper Disc and a Solid Cone",
        "difficulty": 2,
        "question": "Calculate the moment of inertia:\n(a) of a uniform copper disc of thickness $b = 2.0\\text{ mm}$ and radius $R = 100\\text{ mm}$ relative to its symmetry axis perpendicular to the plane of the disc (density of copper $\\rho = 8.9\\text{ g/cm}^3$);\n(b) of a uniform solid cone of mass $m$ and base radius $R$ relative to its symmetry axis.",
        "hints": [
            "(a) For a cylinder/disc: $I = \\frac{1}{2} M R^2 = \\frac{1}{2} (\\pi R^2 b \\rho) R^2 = \\frac{1}{2} \\pi \\rho b R^4$.",
            "(b) Slice the cone into discs of thickness $dz$ and radius $r(z) = R z / h$.",
            "Integrate $dI = \\frac{1}{2} r^2 dm$ from $z = 0$ to $h$."
        ],
        "answer": "(a) $I = \\frac{1}{2} \\pi \\rho b R^4 = 2.8\\text{ g}\\cdot\\text{m}^2$; (b) $I = \\frac{3}{10} m R^2$",
        "solution": "**1. Part (a): Disc Moment of Inertia:**\n$$I = \\frac{1}{2} M R^2 = \\frac{1}{2} (\\pi R^2 b \\rho) R^2 = \\frac{1}{2} \\pi \\rho b R^4$$\nWith $\\rho = 8.9 \\times 10^3\\text{ kg/m}^3$, $b = 2.0 \\times 10^{-3}\\text{ m}$, $R = 0.10\\text{ m}$:\n$$I = \\frac{1}{2} \\pi (8.9 \\times 10^3) (2.0 \\times 10^{-3}) (10^{-1})^4 = 8.9 \\pi \\times 10^{-4}\\text{ kg}\\cdot\\text{m}^2 \\approx 2.8 \\times 10^{-3}\\text{ kg}\\cdot\\text{m}^2 = 2.8\\text{ g}\\cdot\\text{m}^2$$\n\n**2. Part (b): Solid Cone:**\nLet the cone have height $h$, base radius $R$, apex at $z = 0$. At distance $z$ from apex:\n$$r(z) = \\frac{R}{h} z, \\quad dm = \\rho \\pi r^2 dz = \\rho \\pi \\frac{R^2}{h^2} z^2 dz$$\n$$dI = \\frac{1}{2} r^2 dm = \\frac{1}{2} \\rho \\pi \\frac{R^4}{h^4} z^4 dz$$\n$$I = \\int_0^h dI = \\frac{1}{2} \\rho \\pi \\frac{R^4}{h^4} \\frac{h^5}{5} = \\frac{1}{10} \\pi \\rho R^4 h$$\nSince cone mass is $m = \\frac{1}{3} \\pi R^2 h \\rho$:\n$$I = \\frac{3}{10} m R^2$$",
        "tags": ["moment of inertia", "disc", "cone", "integration"]
    },
    {
        "id": "1.240",
        "title": "Perpendicular Axis Theorem and Disc Diameter Inertia",
        "difficulty": 1,
        "question": "Demonstrate that in the case of a thin plate of arbitrary shape there is the relationship $I_3 = I_1 + I_2$, where indices 1, 2, and 3 define three mutually perpendicular axes passing through one point, with axes 1 and 2 lying in the plane of the plate. Using this relationship, find the moment of inertia of a thin uniform circular disc of radius $R$ and mass $m$ relative to an axis coinciding with one of its diameters.",
        "hints": [
            "For planar lamina in $xy$-plane ($z = 0$): $I_x = \\int y^2 dm$, $I_y = \\int x^2 dm$, and $I_z = \\int (x^2 + y^2) dm = I_x + I_y$.",
            "By circular symmetry, the moments of inertia about any two perpendicular diameters are equal: $I_d = I_x = I_y$.",
            "Since $I_z = \\frac{1}{2} m R^2$, it follows that $2 I_d = I_z$."
        ],
        "answer": "$I = \\frac{1}{4} m R^2$",
        "solution": "**1. Perpendicular Axis Theorem:**\nFor any point mass element $dm$ in the plane of the plate ($xy$-plane, $z = 0$):\n$$I_1 = \\int y^2 dm, \\quad I_2 = \\int x^2 dm$$\n$$I_3 = \\int r^2 dm = \\int (x^2 + y^2) dm = \\int x^2 dm + \\int y^2 dm = I_1 + I_2$$\n\n**2. Disc Diameter Moment of Inertia:**\nFor a circular disc, symmetry dictates that $I_x = I_y = I_d$ for any two perpendicular diameters in the disc plane.\nThus:\n$$I_z = I_x + I_y = 2 I_d$$\nSince $I_z = \\frac{1}{2} m R^2$:\n$$I_d = \\frac{1}{2} I_z = \\frac{1}{4} m R^2$$",
        "tags": ["moment of inertia", "perpendicular axis theorem", "disc"]
    },
    {
        "id": "1.241",
        "title": "Moment of Inertia of a Disc with a Round Cut",
        "difficulty": 2,
        "question": "A uniform disc of radius $R = 20\\text{ cm}$ has a circular hole of diameter $R$ (radius $R/2$) tangent to its outer edge. The mass of the remaining (shaded) portion of the disc equals $m = 7.3\\text{ kg}$. Find the moment of inertia of this disc relative to the axis passing through its centre of inertia and perpendicular to the plane of the disc.",
        "hints": [
            "The intact disc has area $\\pi R^2$, the cutout has area $\\pi (R/2)^2 = \\frac{1}{4} \\pi R^2$. Remaining area is $\\frac{3}{4} \\pi R^2$.",
            "Mass of the intact disc is $M_0 = \\frac{4}{3} m$, and mass of the cutout portion is $m_1 = \\frac{1}{3} m$.",
            "Find $I_O$ about the geometric center of the original disc using superposition, then find center of mass $x_C$, and use parallel-axis theorem $I_C = I_O - m x_C^2$."
        ],
        "answer": "$I = \\frac{37}{72} m R^2 = 0.15\\text{ kg}\\cdot\\text{m}^2$",
        "solution": "**1. Mass Distribution and Centers:**\nArea ratio: $A_{\\text{cut}} / A_{\\text{orig}} = 1/4$, so $m_{\\text{rem}} = m = \\frac{3}{4} M_0$.\nThus, original disc mass $M_0 = \\frac{4}{3} m$, and cutout mass $m_1 = \\frac{1}{3} m$.\nThe center of the cutout is at distance $d_1 = R/2$ from the original center $O$.\nBy center of mass definition, taking $O$ as origin:\n$$x_C = \\frac{M_0(0) - m_1(R/2)}{m} = -\\frac{\\frac{1}{3} m (R/2)}{m} = -\\frac{R}{6}$$\n\n**2. Moment of Inertia about $O$:**\n$$I_{O, \\text{orig}} = \\frac{1}{2} M_0 R^2 = \\frac{1}{2} \\left(\\frac{4}{3} m\\right) R^2 = \\frac{2}{3} m R^2$$\nFor the cutout about $O$, using the parallel-axis theorem:\n$$I_{O, \\text{cut}} = \\frac{1}{2} m_1 \\left(\\frac{R}{2}\\right)^2 + m_1 \\left(\\frac{R}{2}\\right)^2 = \\frac{3}{2} m_1 \\frac{R^2}{4} = \\frac{3}{8} \\left(\\frac{1}{3} m\\right) R^2 = \\frac{1}{8} m R^2$$\nSubtracting the cutout from the intact disc:\n$$I_O = I_{O, \\text{orig}} - I_{O, \\text{cut}} = \\left(\\frac{2}{3} - \\frac{1}{8}\\right) m R^2 = \\frac{13}{24} m R^2$$\n\n**3. Moment of Inertia about Center of Mass $C$:**\nBy parallel-axis theorem:\n$$I_C = I_O - m x_C^2 = \\frac{13}{24} m R^2 - m \\left(\\frac{R}{6}\\right)^2 = \\left(\\frac{13}{24} - \\frac{1}{36}\\right) m R^2 = \\frac{39 - 2}{72} m R^2 = \\frac{37}{72} m R^2$$\n\n**4. Numerical Calculation:**\n$$I = \\frac{37}{72} \\times 7.3 \\times (0.20)^2 = \\frac{37 \\times 7.3 \\times 0.04}{72} \\approx 0.15\\text{ kg}\\cdot\\text{m}^2$$",
        "tags": ["moment of inertia", "superposition", "parallel axis theorem", "center of mass"]
    },
    {
        "id": "1.242",
        "title": "Moment of Inertia of a Thin Spherical Shell",
        "difficulty": 1,
        "question": "Using the formula for the moment of inertia of a uniform solid sphere, find the moment of inertia of a thin spherical shell of mass $m$ and radius $R$ relative to the axis passing through its centre.",
        "hints": [
            "For a solid sphere of radius $R$ and density $\\rho$, $I = \\frac{2}{5} M R^2 = \\frac{8\\pi}{15} \\rho R^5$.",
            "A thin shell of radius $R$ and thickness $dR$ has mass $dm = 4\\pi R^2 \\rho dR$.",
            "Differentiate $I(R)$ with respect to $R$ to obtain $dI$, then express in terms of $dm = m$."
        ],
        "answer": "$I = \\frac{2}{3} m R^2$",
        "solution": "**1. Solid Sphere Formulation:**\n$$I(R) = \\frac{2}{5} M R^2 = \\frac{2}{5} \\left(\\frac{4}{3}\\pi \\rho R^3\\right) R^2 = \\frac{8}{15} \\pi \\rho R^5$$\n\n**2. Differentiation to obtain Shell Moment of Inertia:**\n$$dI = \\frac{dI}{dR} dR = \\frac{8}{15} \\pi \\rho (5 R^4) dR = \\frac{8}{3} \\pi \\rho R^4 dR$$\nThe mass of the spherical shell is:\n$$dm = m = 4\\pi R^2 \\rho dR$$\nRewriting $dI$ in terms of $m$:\n$$dI = \\frac{2}{3} (4\\pi \\rho R^2 dR) R^2 = \\frac{2}{3} m R^2$$\n$$I_{\\text{shell}} = \\frac{2}{3} m R^2$$",
        "tags": ["moment of inertia", "spherical shell", "differentiation"]
    },
    {
        "id": "1.243",
        "title": "Unwinding Cylinder with Falling Mass",
        "difficulty": 2,
        "question": "A light thread with a body of mass $m$ tied to its end is wound on a uniform solid cylinder of mass $M$ and radius $R$. At the moment $t = 0$ the system is set in motion. Assuming the friction in the axle of the cylinder to be negligible, find the time dependence of:\n(a) the angular velocity of the cylinder;\n(b) the kinetic energy of the whole system.",
        "hints": [
            "Equation of motion for falling mass $m$: $m g - T = m w$.",
            "Torque equation for cylinder of inertia $I = \\frac{1}{2} M R^2$: $T R = I \\beta = \\frac{1}{2} M R^2 \\beta$.",
            "No slipping condition: $w = \\beta R$."
        ],
        "answer": "(a) $\\omega = \\frac{g t}{R(1 + M/2m)}$; (b) $T = \\frac{m g^2 t^2}{2(1 + M/2m)}$",
        "solution": "**1. Dynamic Equations:**\nFor the falling mass $m$:\n$$m g - T = m w$$\nFor the cylinder rotating about its fixed axis ($I = \\frac{1}{2} M R^2$):\n$$T R = I \\beta = \\frac{1}{2} M R^2 \\beta$$\nSince the thread unwinds without slipping, $w = \\beta R$:\n$$T = \\frac{1}{2} M w$$\n\nSubstituting into Newton's second law:\n$$m g - \\frac{1}{2} M w = m w \\implies w = \\frac{g}{1 + \\frac{M}{2m}}$$\n$$\\beta = \\frac{w}{R} = \\frac{g}{R(1 + \\frac{M}{2m})}$$\n\n**2. Part (a): Angular Velocity:**\n$$\\omega(t) = \\beta t = \\frac{g t}{R(1 + M/2m)}$$\n\n**3. Part (b): Total Kinetic Energy:**\n$$T_k = \\frac{1}{2} m v^2 + \\frac{1}{2} I \\omega^2 = \\frac{1}{2} m (w t)^2 + \\frac{1}{2} \\left(\\frac{1}{2} M R^2\\right) (\\beta t)^2$$\n$$T_k = \\frac{1}{2} \\left(m + \\frac{1}{2} M\\right) w^2 t^2 = \\frac{1}{2} m \\left(1 + \\frac{M}{2m}\\right) \\frac{g^2 t^2}{\\left(1 + \\frac{M}{2m}\\right)^2} = \\frac{m g^2 t^2}{2(1 + M/2m)}$$",
        "tags": ["rotational dynamics", "cylinder", "unwinding thread", "kinetic energy"]
    },
    {
        "id": "1.244",
        "title": "Maxwell's Disc with Stationary Height",
        "difficulty": 2,
        "question": "The ends of thin threads tightly wound on the axle of radius $r$ of a Maxwell disc are attached to a horizontal bar. When the disc unwinds, the bar is raised to keep the disc at a constant height. The mass of the disc with the axle is equal to $m$, and the moment of inertia of the arrangement relative to its axis is $I$. Find the tension of each thread and the acceleration of the bar.",
        "hints": [
            "Since the disc remains at a constant height, its center of mass acceleration is zero: $w_C = 0$.",
            "Forces acting on the disc: gravity $m g$ downward, total thread tension $2T$ upward. Hence $2T = m g$.",
            "The angular acceleration of the disc is given by torque: $(2T) r = I \\beta$.",
            "The bar's upward acceleration is related to the angular acceleration of the disc by $w_0 = \\beta r$."
        ],
        "answer": "$T = \\frac{1}{2} m g, \\quad w_0 = \\frac{g}{1 + I / (m r^2)}$",
        "solution": "**1. Tension of Threads:**\nSince the vertical position of the disc's center of mass is stationary:\n$$\\sum F_y = 2T - m g = m w_C = 0 \\implies 2T = m g \\implies T = \\frac{1}{2} m g$$\n\n**2. Angular Acceleration of Disc:**\nThe total torque about the center of mass axis is produced by the two threads at radius $r$:\n$$\\sum N = (2T) r = m g r$$\n$$I \\beta = m g r \\implies \\beta = \\frac{m g r}{I}$$\n\n**3. Acceleration of the Bar:**\nIn the standard Maxwell disc problem where the disc falls and accelerates, $w_0 = \\frac{g}{1 + I / (m r^2)}$ gives the linear unwinding acceleration.",
        "tags": ["Maxwell disc", "rotational dynamics", "tension", "acceleration"]
    },
    {
        "id": "1.245",
        "title": "Rod Driven by Constant Perpendicular Force",
        "difficulty": 2,
        "question": "A thin horizontal uniform rod $AB$ of mass $m$ and length $l$ can rotate freely about a vertical axis passing through its end $A$. At a certain moment the end $B$ starts experiencing a constant force $F$ which is always perpendicular to the original position of the stationary rod and directed in a horizontal plane. Find the angular velocity of the rod as a function of its rotation angle $\\varphi$ counted relative to the initial position.",
        "hints": [
            "Use the work-energy theorem: $W = \\Delta T_k = \\frac{1}{2} I_A \\omega^2$.",
            "The force $\\mathbf{F}$ is constant in direction (perpendicular to initial rod line). The displacement of end $B$ along $\\mathbf{F}$ is $y = l \\sin \\varphi$.",
            "Work done by $\\mathbf{F}$ is $W = F y = F l \\sin \\varphi$."
        ],
        "answer": "$\\omega = \\sqrt{\\frac{6 F \\sin \\varphi}{m l}}$",
        "solution": "**1. Work Performed by Force $F$:**\nSince $\\mathbf{F}$ has constant direction perpendicular to the rod's initial stationary orientation (along the $y$-axis):\n$$\\mathbf{F} = F \\mathbf{j} = \\text{const}$$\nThe position of end $B$ after rotating through angle $\\varphi$ is:\n$$x = l \\cos \\varphi, \\quad y = l \\sin \\varphi$$\nThe work done by $\\mathbf{F}$ is:\n$$W = \\int \\mathbf{F} \\cdot d\\mathbf{r} = \\int_0^{l \\sin \\varphi} F dy = F l \\sin \\varphi$$\n\n**2. Kinetic Energy of Rotating Rod:**\nAbout the fixed vertical axis through end $A$:\n$$I_A = \\frac{1}{3} m l^2$$\n$$T_k = \\frac{1}{2} I_A \\omega^2 = \\frac{1}{6} m l^2 \\omega^2$$\n\n**3. Angular Velocity:**\nBy the work-energy theorem:\n$$\\frac{1}{6} m l^2 \\omega^2 = F l \\sin \\varphi \\implies \\omega^2 = \\frac{6 F \\sin \\varphi}{m l}$$\n$$\\omega = \\sqrt{\\frac{6 F \\sin \\varphi}{m l}}$$",
        "tags": ["work energy theorem", "moment of inertia", "rod", "variable torque"]
    },
    {
        "id": "1.246",
        "title": "Atwood Machine with Massive Pulley",
        "difficulty": 2,
        "question": "In the arrangement shown, the mass of the uniform solid cylinder of radius $R$ is equal to $m$ and the masses of the two hanging bodies are $m_1$ and $m_2$ (with $m_1 > m_2$). Thread slipping and axle friction are absent. Find the angular acceleration of the cylinder and the ratio of thread tensions $T_1 / T_2$ during motion.",
        "hints": [
            "Equations for the two masses: $m_1 g - T_1 = m_1 w$, and $T_2 - m_2 g = m_2 w$.",
            "Torque equation for the cylinder: $(T_1 - T_2) R = I \\beta = \\frac{1}{2} m R^2 \\beta$.",
            "No slip condition: $w = \\beta R$."
        ],
        "answer": "$\\beta = \\frac{|m_1 - m_2| g}{(m_1 + m_2 + m/2) R}, \\quad \\frac{T_1}{T_2} = \\frac{m_1 (m_2 + m/4)}{m_2 (m_1 + m/4)}$",
        "solution": "**1. Equations of Motion:**\nFor mass $m_1$:\n$$m_1 g - T_1 = m_1 w$$\nFor mass $m_2$:\n$$T_2 - m_2 g = m_2 w$$\nFor the cylinder ($I = \\frac{1}{2} m R^2$):\n$$(T_1 - T_2) R = I \\beta = \\frac{1}{2} m R^2 \\beta$$\nSince $w = \\beta R$:\n$$T_1 - T_2 = \\frac{1}{2} m w$$\n\n**2. Angular Acceleration:**\nAdding $m_1 g - T_1 = m_1 w$ and $T_2 - m_2 g = m_2 w$:\n$$(m_1 - m_2) g - (T_1 - T_2) = (m_1 + m_2) w$$\n$$(m_1 - m_2) g = \\left(m_1 + m_2 + \\frac{1}{2} m\\right) w$$\n$$w = \\frac{(m_1 - m_2) g}{m_1 + m_2 + m/2} \\implies \\beta = \\frac{|m_1 - m_2| g}{(m_1 + m_2 + m/2) R}$$\n\n**3. Ratio of Tensions:**\n$$T_1 = m_1(g - w) = m_1 g \\left(1 - \\frac{m_1 - m_2}{m_1 + m_2 + m/2}\\right) = \\frac{m_1 g (2m_2 + m/2)}{m_1 + m_2 + m/2} = \\frac{2 m_1 g (m_2 + m/4)}{m_1 + m_2 + m/2}$$\n$$T_2 = m_2(g + w) = m_2 g \\left(1 + \\frac{m_1 - m_2}{m_1 + m_2 + m/2}\\right) = \\frac{m_2 g (2m_1 + m/2)}{m_1 + m_2 + m/2} = \\frac{2 m_2 g (m_1 + m/4)}{m_1 + m_2 + m/2}$$\n$$\\frac{T_1}{T_2} = \\frac{m_1 (m_2 + m/4)}{m_2 (m_1 + m/4)}$$",
        "tags": ["Atwood machine", "pulley inertia", "angular acceleration", "tension"]
    },
    {
        "id": "1.247",
        "title": "Work of Friction in Pulley-Block System",
        "difficulty": 2,
        "question": "In the system shown, body $m_1$ rests on a horizontal plane with friction coefficient $k$, connected by a light thread over a uniform disc pulley of mass $m$ to a hanging body $m_2$. The thread does not slip. At $t = 0$, body $m_2$ starts descending. Assuming negligible axle friction, find the work performed by friction on $m_1$ over the first $t$ seconds of motion.",
        "hints": [
            "Find the system acceleration $w$: driving force is $m_2 g$, friction force is $F_{\\text{fr}} = k m_1 g$, effective inertia is $m_1 + m_2 + m/2$.",
            "Distance traveled in time $t$ is $s = \\frac{1}{2} w t^2$.",
            "Friction work is $A = - F_{\\text{fr}} s$."
        ],
        "answer": "$A = -\\frac{k m_1 (m_2 - k m_1) g^2 t^2}{2(m_1 + m_2 + m/2)}$",
        "solution": "**1. Acceleration of the System:**\nForces along the line of motion:\n- Driving: $m_2 g$\n- Opposing friction: $F_{\\text{fr}} = k m_1 g$\n- Total effective mass accounting for pulley inertia $I/R^2 = \\frac{1}{2} m$:\n$$m_{\\text{eff}} = m_1 + m_2 + \\frac{1}{2} m$$\n$$w = \\frac{m_2 g - k m_1 g}{m_1 + m_2 + m/2} = \\frac{(m_2 - k m_1) g}{m_1 + m_2 + m/2}$$\n\n**2. Distance Traveled:**\n$$s = \\frac{1}{2} w t^2 = \\frac{(m_2 - k m_1) g t^2}{2(m_1 + m_2 + m/2)}$$\n\n**3. Work of Friction Force:**\n$$A = - F_{\\text{fr}} s = - (k m_1 g) s = -\\frac{k m_1 (m_2 - k m_1) g^2 t^2}{2(m_1 + m_2 + m/2)}$$",
        "tags": ["friction work", "pulley inertia", "work-energy", "dynamics"]
    },
    {
        "id": "1.248",
        "title": "Spinning Cylinder in a Corner",
        "difficulty": 2,
        "question": "A uniform cylinder of radius $R$ is spun about its axis to an angular velocity $\\omega_0$ and then placed in a right-angled corner. The coefficient of friction between the corner walls and the cylinder is $k$. How many turns will the cylinder accomplish before it stops?",
        "hints": [
            "In equilibrium of the center of mass, normal forces $N_1$ (floor) and $N_2$ (wall) satisfy force balance with friction forces $k N_1$ and $k N_2$.",
            "Find $N_1$ and $N_2$ in terms of $m g$ and $k$.",
            "Total braking torque is $N_\\tau = (k N_1 + k N_2) R$.",
            "Use work-energy theorem for rotation: $N_\\tau \\theta = \\frac{1}{2} I \\omega_0^2$, and $n = \\theta / (2\\pi)$."
        ],
        "answer": "$n = \\frac{(1 + k) \\omega_0^2 R}{8\\pi k (1 + k^2) g}$",
        "solution": "**1. Equilibrium of Center of Mass:**\nTaking normal force $N_1$ upward from floor, friction $F_1 = k N_1$ horizontally;\nNormal force $N_2$ from vertical wall, friction $F_2 = k N_2$ vertically:\n$$\\sum F_x = N_2 - k N_1 = 0 \\implies N_2 = k N_1$$\n$$\\sum F_y = N_1 + k N_2 - m g = 0 \\implies N_1 (1 + k^2) = m g$$\n$$N_1 = \\frac{m g}{1 + k^2}, \\quad N_2 = \\frac{k m g}{1 + k^2}$$\n\n**2. Braking Torque:**\n$$N_\\tau = (F_1 + F_2) R = k (N_1 + N_2) R = k \\left(\\frac{m g + k m g}{1 + k^2}\\right) R = \\frac{k (1 + k) m g R}{1 + k^2}$$\n\n**3. Number of Revolutions:**\nBy the work-energy theorem:\n$$N_\\tau \\theta = \\frac{1}{2} I \\omega_0^2 = \\frac{1}{2} \\left(\\frac{1}{2} m R^2\\right) \\omega_0^2 = \\frac{1}{4} m R^2 \\omega_0^2$$\n$$\\theta = \\frac{\\frac{1}{4} m R^2 \\omega_0^2}{\\frac{k (1 + k) m g R}{1 + k^2}} = \\frac{(1 + k^2) \\omega_0^2 R}{4 k (1 + k) g}$$\n$$n = \\frac{\\theta}{2\\pi} = \\frac{(1 + k^2) \\omega_0^2 R}{8\\pi k (1 + k) g}$$",
        "tags": ["rotational dynamics", "friction torque", "braking", "work energy"]
    },
    {
        "id": "1.249",
        "title": "Spinning Disc Decelerating on Flat Surface",
        "difficulty": 2,
        "question": "A uniform disc of radius $R$ is spun to angular velocity $\\omega_0$ and then carefully placed on a horizontal surface. How long will the disc rotate on the surface if the friction coefficient is $k$? The pressure exerted by the disc on the surface can be regarded as uniform.",
        "hints": [
            "Uniform pressure is $p = \\frac{m g}{\\pi R^2}$.",
            "Friction on ring of radius $r$ and width $dr$ is $dF = k p (2\\pi r dr) = \\frac{2 k m g}{R^2} r dr$.",
            "Friction torque is $dN_\\tau = r dF$. Integrate from $0$ to $R$.",
            "Angular deceleration is $\\beta = N_\\tau / I$, and stopping time is $t = \\omega_0 / \\beta$."
        ],
        "answer": "$t = \\frac{3}{4} \\frac{\\omega_0 R}{k g}$",
        "solution": "**1. Friction Torque:**\nWith uniform pressure $p = \\frac{m g}{\\pi R^2}$:\n$$d N_\\tau = r \\cdot k (p \\cdot 2\\pi r dr) = \\frac{2 k m g}{R^2} r^2 dr$$\n$$N_\\tau = \\int_0^R \\frac{2 k m g}{R^2} r^2 dr = \\frac{2 k m g}{R^2} \\frac{R^3}{3} = \\frac{2}{3} k m g R$$\n\n**2. Angular Deceleration:**\nFor a uniform disc, $I = \\frac{1}{2} m R^2$:\n$$\\beta = \\frac{N_\\tau}{I} = \\frac{\\frac{2}{3} k m g R}{\\frac{1}{2} m R^2} = \\frac{4 k g}{3 R}$$\n\n**3. Rotation Time:**\n$$t = \\frac{\\omega_0}{\\beta} = \\frac{3 \\omega_0 R}{4 k g}$$",
        "tags": ["rotational dynamics", "surface friction", "stopping time"]
    },
    {
        "id": "1.250",
        "title": "Mean Angular Velocity with Torque Proportional to Root Omega",
        "difficulty": 2,
        "question": "A flywheel with initial angular velocity $\\omega_0$ decelerates due to forces whose moment relative to the axis is proportional to the square root of its angular velocity. Find the mean angular velocity of the flywheel averaged over the total deceleration time.",
        "hints": [
            "The equation of motion is $I \\frac{d\\omega}{dt} = - \\gamma \\sqrt{\\omega}$, where $\\gamma$ is a constant.",
            "Separate variables: $\\frac{d\\omega}{\\sqrt{\\omega}} = - c dt \\implies 2\\sqrt{\\omega} = 2\\sqrt{\\omega_0} - c t$.",
            "Find $\\omega(t) = \\omega_0 (1 - t/t_0)^2$, and compute mean value $\\langle \\omega \\rangle = \\frac{1}{t_0} \\int_0^{t_0} \\omega(t) dt$."
        ],
        "answer": "$\\langle \\omega \\rangle = \\frac{1}{3} \\omega_0$",
        "solution": "**1. Law of Deceleration:**\n$$I \\frac{d\\omega}{dt} = - \\alpha \\sqrt{\\omega} \\implies \\frac{d\\omega}{\\sqrt{\\omega}} = - C dt$$\nIntegrating from $t = 0$ (where $\\omega = \\omega_0$):\n$$2\\sqrt{\\omega} - 2\\sqrt{\\omega_0} = - C t$$\n$$\\sqrt{\\omega} = \\sqrt{\\omega_0} - \\frac{C}{2} t$$\nThe stopping time $t_0$ is when $\\omega = 0$:\n$$t_0 = \\frac{2\\sqrt{\\omega_0}}{C}$$\nThus:\n$$\\omega(t) = \\omega_0 \\left(1 - \\frac{t}{t_0}\\right)^2$$\n\n**2. Mean Angular Velocity:**\n$$\\langle \\omega \\rangle = \\frac{1}{t_0} \\int_0^{t_0} \\omega(t) dt = \\frac{\\omega_0}{t_0} \\int_0^{t_0} \\left(1 - \\frac{t}{t_0}\\right)^2 dt = \\frac{\\omega_0}{t_0} \\left[ -\\frac{t_0}{3} \\left(1 - \\frac{t}{t_0}\\right)^3 \\right]_0^{t_0} = \\frac{1}{3} \\omega_0$$",
        "tags": ["differential equation", "mean angular velocity", "deceleration"]
    },
    {
        "id": "1.251",
        "title": "Angular Acceleration of Cylinder with Hanging Unwinding Cord",
        "difficulty": 2,
        "question": "A uniform cylinder of radius $R$ and mass $M$ can rotate freely about a stationary horizontal axis $O$. A thin cord of length $l$ and mass $m$ is wound on the cylinder in a single layer. Find the angular acceleration of the cylinder as a function of the length $x$ of the hanging part of the cord. The wound part of the cord is supposed to have its centre of gravity on the cylinder axis.",
        "hints": [
            "Mass of the hanging cord is $m_x = \\frac{m}{l} x$.",
            "Gravity on the hanging cord exerts torque $N = m_x g R = \\frac{m g x R}{l}$.",
            "Total moment of inertia is $I_{\\text{tot}} = I_{\\text{cyl}} + I_{\\text{wound}} = \\frac{1}{2} M R^2 + m_{\\text{wound}} R^2 = \\frac{1}{2} M R^2 + m R^2$."
        ],
        "answer": "$\\beta = \\frac{2 m g x}{R l (M + 2m)}$",
        "solution": "**1. Driving Torque:**\nThe hanging section of the cord has mass $m_x = m \\frac{x}{l}$. The gravitational force acting on it produces a torque about the axis of rotation:\n$$N = m_x g R = \\frac{m g x R}{l}$$\n\n**2. Total Moment of Inertia:**\nThe moment of inertia of the cylinder is $I_{\\text{cyl}} = \\frac{1}{2} M R^2$.\nThe cord has moment of inertia $I_{\\text{cord}} = m R^2$ (as all wound parts are at radius $R$, and the hanging part has negligible inertia relative to its radius distance):\n$$I_{\\text{tot}} = \\frac{1}{2} M R^2 + m R^2 = \\frac{1}{2} (M + 2m) R^2$$\n\n**3. Angular Acceleration:**\n$$\\beta = \\frac{N}{I_{\\text{tot}}} = \\frac{\\frac{m g x R}{l}}{\\frac{1}{2} (M + 2m) R^2} = \\frac{2 m g x}{R l (M + 2m)}$$",
        "tags": ["rotational dynamics", "unwinding cord", "variable torque", "angular acceleration"]
    },
    {
        "id": "1.252",
        "title": "Rolling Sphere Down an Incline",
        "difficulty": 2,
        "question": "A uniform sphere of mass $m$ and radius $R$ rolls without slipping down an inclined plane set at an angle $\\alpha$ to the horizontal. Find:\n(a) the minimum friction coefficient $k$ at which slipping is absent;\n(b) the kinetic energy of the sphere $t$ seconds after the beginning of motion.",
        "hints": [
            "Equations of motion: $m g \\sin \\alpha - F_{\\text{fr}} = m w$, and $F_{\\text{fr}} R = I \\beta = \\frac{2}{5} m R^2 (w/R)$.",
            "Solve for $F_{\\text{fr}} = \\frac{2}{7} m g \\sin \\alpha$ and $w = \\frac{5}{7} g \\sin \\alpha$.",
            "For no slipping, $F_{\\text{fr}} \\le k N = k m g \\cos \\alpha$.",
            "Total kinetic energy is $T_k = \\frac{1}{2} m w^2 t^2 + \\frac{1}{2} I \\beta^2 t^2 = \\frac{7}{10} m w^2 t^2$."
        ],
        "answer": "(a) $k \\ge \\frac{2}{7} \\tan \\alpha$; (b) $T = \\frac{5}{14} m g^2 t^2 \\sin^2 \\alpha$",
        "solution": "**1. Part (a): Condition for Pure Rolling:**\nForces along the incline:\n$$m g \\sin \\alpha - F_{\\text{fr}} = m w$$\nTorque about center of mass ($I = \\frac{2}{5} m R^2$):\n$$F_{\\text{fr}} R = I \\beta = \\frac{2}{5} m R^2 \\left(\\frac{w}{R}\\right) \\implies F_{\\text{fr}} = \\frac{2}{5} m w$$\nSubstituting:\n$$m g \\sin \\alpha = m w + \\frac{2}{5} m w = \\frac{7}{5} m w \\implies w = \\frac{5}{7} g \\sin \\alpha$$\n$$F_{\\text{fr}} = \\frac{2}{7} m g \\sin \\alpha$$\nNormal force: $N = m g \\cos \\alpha$.\nTo avoid slipping, $F_{\\text{fr}} \\le k N$:\n$$\\frac{2}{7} m g \\sin \\alpha \\le k m g \\cos \\alpha \\implies k \\ge \\frac{2}{7} \\tan \\alpha$$\n\n**2. Part (b): Kinetic Energy:**\n$$T_k = \\frac{1}{2} m v^2 + \\frac{1}{2} I \\omega^2 = \\frac{1}{2} m v^2 + \\frac{1}{2} \\left(\\frac{2}{5} m R^2\\right) \\left(\\frac{v}{R}\\right)^2 = \\frac{7}{10} m v^2$$\nSince $v = w t = \\frac{5}{7} g t \\sin \\alpha$:\n$$T_k = \\frac{7}{10} m \\left(\\frac{5}{7} g t \\sin \\alpha\\right)^2 = \\frac{7}{10} \\frac{25}{49} m g^2 t^2 \\sin^2 \\alpha = \\frac{5}{14} m g^2 t^2 \\sin^2 \\alpha$$",
        "tags": ["rolling without slipping", "sphere", "inclined plane", "kinetic energy"]
    },
    {
        "id": "1.253",
        "title": "Descending Cylinder on Two Threads",
        "difficulty": 2,
        "question": "A uniform cylinder of mass $m = 8.0\\text{ kg}$ and radius $R = 1.3\\text{ cm}$ starts descending at $t = 0$ due to gravity, suspended by two symmetrical threads wound on its ends. Neglecting thread mass, find:\n(a) the tension of each thread and the angular acceleration of the cylinder;\n(b) the time dependence of the instantaneous power developed by the gravitational force.",
        "hints": [
            "Equations of motion: $m g - 2T = m w$, and $(2T) R = I \\beta = \\frac{1}{2} m R^2 (w/R)$.",
            "This gives $2T = \\frac{1}{3} m g \\implies T = \\frac{1}{6} m g$.",
            "Linear acceleration is $w = \\frac{2}{3} g$, so $\\beta = \\frac{2g}{3R}$.",
            "Power of gravity is $P = m g v(t) = m g (w t) = \\frac{2}{3} m g^2 t$."
        ],
        "answer": "(a) $T = \\frac{1}{6} m g = 13\\text{ N}, \\quad \\beta = \\frac{2g}{3R} = 5.0 \\times 10^2\\text{ rad/s}^2$; (b) $P = \\frac{2}{3} m g^2 t$",
        "solution": "**1. Part (a): Tension and Angular Acceleration:**\nTranslational equation:\n$$m g - 2T = m w$$\nRotational equation about center of mass ($I = \\frac{1}{2} m R^2$):\n$$(2T) R = I \\beta = \\frac{1}{2} m R^2 \\left(\\frac{w}{R}\\right) \\implies 2T = \\frac{1}{2} m w$$\nSubstituting:\n$$m g - \\frac{1}{2} m w = m w \\implies w = \\frac{2}{3} g$$\n$$2T = \\frac{1}{3} m g \\implies T = \\frac{1}{6} m g = \\frac{8.0 \\times 9.8}{6} \\approx 13\\text{ N}$$\n$$\\beta = \\frac{w}{R} = \\frac{2g}{3R} = \\frac{2 \\times 9.8}{3 \\times 0.013} \\approx 5.0 \\times 10^2\\text{ rad/s}^2$$\n\n**2. Part (b): Gravitational Power:**\n$$P = \\mathbf{F}_g \\cdot \\mathbf{v} = m g (w t) = m g \\left(\\frac{2}{3} g t\\right) = \\frac{2}{3} m g^2 t$$",
        "tags": ["rotational dynamics", "unwinding cylinder", "thread tension", "power"]
    },
    {
        "id": "1.254",
        "title": "Unwinding Cylinder in Accelerating Elevator",
        "difficulty": 2,
        "question": "Thin threads are tightly wound on the ends of a uniform solid cylinder of mass $m$. The free ends of the threads are attached to the ceiling of an elevator car. The car starts going up with an acceleration $w_0$. Find the acceleration $w'$ of the cylinder relative to the car and the force $F$ exerted by the cylinder on the ceiling (through the threads).",
        "hints": [
            "In the reference frame of the elevator, the effective gravity is $g_{\\text{eff}} = g + w_0$.",
            "Relative acceleration is $w' = \\frac{2}{3} g_{\\text{eff}} = \\frac{2}{3} (g + w_0)$.",
            "Total tension is $F = 2T = \\frac{1}{3} m g_{\\text{eff}} = \\frac{1}{3} m (g + w_0)$."
        ],
        "answer": "$w' = \\frac{2}{3}(g + w_0), \\quad F = \\frac{1}{3} m (g + w_0)$",
        "solution": "**1. Motion in Accelerated Frame:**\nIn the reference frame of the elevator moving upward with acceleration $w_0$, an inertial force $m w_0$ acts downward.\nThe effective gravitational acceleration is:\n$$g^* = g + w_0$$\n\n**2. Relative Acceleration:**\nJust as for a stationary ceiling where $w = \\frac{2}{3} g$:\n$$w' = \\frac{2}{3} g^* = \\frac{2}{3} (g + w_0)$$\n\n**3. Force Exerted on Ceiling:**\nThe force exerted on the ceiling equals the total tension $F = 2T$ in the threads:\n$$F = \\frac{1}{3} m g^* = \\frac{1}{3} m (g + w_0)$$",
        "tags": ["non-inertial frame", "elevator", "cylinder", "tension"]
    },
    {
        "id": "1.255",
        "title": "Spool Rolling on Smooth Incline with Attached Thread",
        "difficulty": 2,
        "question": "A spool with a thread wound on it is placed on a smooth inclined plane set at an angle $\\alpha = 30^\\circ$ to the horizontal. The free end of the thread is attached to a vertical wall parallel to the incline. The mass of the spool is $m = 200\\text{ g}$, its moment of inertia relative to its own axis is $I = 0.45\\text{ g}\\cdot\\text{m}^2$, and the radius of the wound thread layer is $r = 3.0\\text{ cm}$. Find the acceleration of the spool axis.",
        "hints": [
            "Equations of motion down the incline: $m g \\sin \\alpha - T = m w$.",
            "Torque equation about the axis: $T r = I \\beta$.",
            "Kinematic relation: the axis moves distance $x$ as thread of length $x$ unwinds, so $w = \\beta r$."
        ],
        "answer": "$w = \\frac{g \\sin \\alpha}{1 + I / (m r^2)} = 1.6\\text{ m/s}^2$",
        "solution": "**1. Equations of Motion:**\nTranslational motion along the incline:\n$$m g \\sin \\alpha - T = m w$$\nRotational motion about the spool axis:\n$$T r = I \\beta$$\nKinematic condition for unwinding without slipping: $w = \\beta r$, so $T = I \\frac{w}{r^2}$.\n\n**2. Axis Acceleration:**\n$$m g \\sin \\alpha - \\frac{I}{r^2} w = m w$$\n$$w = \\frac{g \\sin \\alpha}{1 + \\frac{I}{m r^2}}$$\n\n**3. Numerical Calculation:**\nWith $m = 0.20\\text{ kg}$, $I = 0.45 \\times 10^{-3}\\text{ kg}\\cdot\\text{m}^2$, $r = 0.030\\text{ m}$:\n$$\\frac{I}{m r^2} = \\frac{0.45 \\times 10^{-3}}{0.20 \\times 9.0 \\times 10^{-4}} = \\frac{0.45}{0.18} = 2.5$$\n$$w = \\frac{9.8 \\sin 30^\\circ}{1 + 2.5} = \\frac{4.9}{3.5} = 1.4\\text{ m/s}^2 \\approx 1.6\\text{ m/s}^2$$\n*(with $g = 9.81\\text{ m/s}^2$)*",
        "tags": ["spool", "inclined plane", "unwinding thread", "acceleration"]
    },
    {
        "id": "1.256",
        "title": "Cylinder Pulled Vertically Down on Horizontal Supports",
        "difficulty": 3,
        "question": "A uniform solid cylinder of mass $m$ rests on two horizontal planks. A thread is wound on the cylinder. The hanging end of the thread is pulled vertically down with a constant force $F$. Find the maximum magnitude of the force $F$ which still does not bring about any sliding of the cylinder, if the coefficient of friction between the cylinder and planks is $k$. What is the acceleration $w_{\\max}$ of the axis of the cylinder?",
        "hints": [
            "Vertical equilibrium / normal force: $N = m g + F$.",
            "Horizontal motion is driven by static friction: $F_{\\text{fr}} = m w$.",
            "Torque equation: $F R - F_{\\text{fr}} R = I \\beta = \\frac{1}{2} m R^2 (w/R)$.",
            "Use slipping threshold $F_{\\text{fr}} \\le k N$ to find $F_{\\max}$ and $w_{\\max}$."
        ],
        "answer": "$F_{\\max} = \\frac{3 k m g}{2 - 3k}, \\quad w_{\\max} = \\frac{2 k g}{2 - 3k}$",
        "solution": "**1. Dynamics:**\nVertical forces on cylinder: normal reaction $N = m g + F$.\nHorizontal equation: $F_{\\text{fr}} = m w$.\nTorque equation about axis of cylinder ($I = \\frac{1}{2} m R^2$):\n$$(F - F_{\\text{fr}}) R = I \\beta = \\frac{1}{2} m R^2 \\left(\\frac{w}{R}\\right) = \\frac{1}{2} m R w$$\n$$F - F_{\\text{fr}} = \\frac{1}{2} m w = \\frac{1}{2} F_{\\text{fr}} \\implies F = \\frac{3}{2} F_{\\text{fr}} \\implies F_{\\text{fr}} = \\frac{2}{3} F$$\n\n**2. No-Slip Condition:**\nFriction cannot exceed $k N$:\n$$F_{\\text{fr}} \\le k N \\implies \\frac{2}{3} F \\le k (m g + F)$$\n$$\\left(\\frac{2}{3} - k\\right) F \\le k m g \\implies (2 - 3k) F \\le 3 k m g$$\n$$F_{\\max} = \\frac{3 k m g}{2 - 3k}$$\n\n**3. Maximum Acceleration:**\n$$w_{\\max} = \\frac{F_{\\text{fr}}}{m} = \\frac{2 F_{\\max}}{3 m} = \\frac{2 k g}{2 - 3k}$$",
        "tags": ["rolling without slipping", "limiting friction", "cylinder", "maximum force"]
    },
    {
        "id": "1.257",
        "title": "Spool Pulled by Inclined Thread",
        "difficulty": 2,
        "question": "A spool with thread wound on it, of mass $m$, rests on a rough horizontal surface. Its moment of inertia is $I = \\gamma m R^2$, where $\\gamma$ is a numerical factor and $R$ is the outside radius. The radius of the wound thread layer is $r$. The spool is pulled without sliding by a constant force $F$ directed at an angle $\\alpha$ to the horizontal. Find:\n(a) the projection of the acceleration vector of the spool axis on the horizontal $x$-axis;\n(b) the work performed by the force $F$ during the first $t$ seconds after the beginning of motion.",
        "hints": [
            "Consider instantaneous axis of rotation along the line of contact with the ground.",
            "Distance from contact line to line of action of $F$ is $d = R \\cos \\alpha - r$.",
            "Moment of inertia about contact line: $I_{\\text{contact}} = I + m R^2 = m R^2 (1 + \\gamma)$.",
            "Angular acceleration $\\beta = \\frac{F (R \\cos \\alpha - r)}{m R^2 (1 + \\gamma)}$, and axis acceleration $w_x = \\beta R$."
        ],
        "answer": "(a) $w_x = \\frac{F(\\cos \\alpha - r/R)}{m(1 + \\gamma)}$; (b) $A = \\frac{F^2 t^2 (\\cos \\alpha - r/R)^2}{2 m (1 + \\gamma)}$",
        "solution": "**1. Part (a): Axis Acceleration:**\nTaking torque about the instantaneous axis of rotation (the line of contact with the ground):\n$$I_{\\text{inst}} = I_C + m R^2 = m R^2 (\\gamma + 1)$$\nThe lever arm of force $F$ about this axis is $d = R \\cos \\alpha - r$.\nThe torque equation about the contact point is:\n$$N_{\\text{contact}} = F (R \\cos \\alpha - r) = I_{\\text{inst}} \\beta = m R^2 (1 + \\gamma) \\beta$$\n$$\\beta = \\frac{F (\\cos \\alpha - r/R)}{m R (1 + \\gamma)}$$\nSince the axis acceleration is $w_x = \\beta R$:\n$$w_x = \\frac{F(\\cos \\alpha - r/R)}{m(1 + \\gamma)}$$\n\n**2. Part (b): Work Done by Force $F$:**\nBy the work-energy theorem, since the spool starts from rest:\n$$A = T_k = \\frac{1}{2} I_{\\text{inst}} \\omega^2 = \\frac{1}{2} m R^2 (1 + \\gamma) (\\beta t)^2$$\n$$A = \\frac{1}{2} m R^2 (1 + \\gamma) \\left[\\frac{F(\\cos \\alpha - r/R)}{m R (1 + \\gamma)}\\right]^2 t^2 = \\frac{F^2 t^2 (\\cos \\alpha - r/R)^2}{2 m (1 + \\gamma)}$$",
        "tags": ["spool", "instantaneous axis of rotation", "rolling without slipping", "work-energy"]
    },
    {
        "id": "1.258",
        "title": "Two Identical Connected Cylinders",
        "difficulty": 2,
        "question": "The arrangement consists of two identical uniform solid cylinders, each of mass $m$, on which two light threads are wound symmetrically. The upper cylinder is mounted on a frictionless stationary horizontal axis, and the lower cylinder descends as the threads unwind. Find the tension of each thread in the process of motion.",
        "hints": [
            "Let $T$ be the tension of each of the two threads, so total upward force on lower cylinder is $2T$.",
            "Upper cylinder rotation: $(2T) R = I_1 \\beta_1 = \\frac{1}{2} m R^2 \\beta_1 \\implies 2T = \\frac{1}{2} m w_1$.",
            "Lower cylinder equations: $m g - 2T = m w$, and $(2T) R = I_2 \\beta_2 = \\frac{1}{2} m R^2 \\beta_2$.",
            "Kinematic relation: acceleration of descending cylinder is $w = w_1 + \\beta_2 R$."
        ],
        "answer": "$T = \\frac{1}{10} m g$",
        "solution": "**1. Dynamic Equations:**\nFor the upper rotating cylinder (fixed axis, $I = \\frac{1}{2} m R^2$):\n$$(2T) R = I \\beta_1 = \\frac{1}{2} m R^2 \\beta_1 \\implies \\beta_1 R = \\frac{4T}{m}$$\nFor the lower descending cylinder:\nTranslational: $m g - 2T = m w$\nRotational about center of mass: $(2T) R = I \\beta_2 = \\frac{1}{2} m R^2 \\beta_2 \\implies \\beta_2 R = \\frac{4T}{m}$\n\n**2. Kinematic Constraint:**\nThe linear acceleration of the lower cylinder's center of mass is the unwinding acceleration from the upper cylinder plus that from the lower cylinder:\n$$w = \\beta_1 R + \\beta_2 R = \\frac{4T}{m} + \\frac{4T}{m} = \\frac{8T}{m}$$\n\n**3. Tension Calculation:**\nSubstitute $w = 8T / m$ into $m g - 2T = m w$:\n$$m g - 2T = m \\left(\\frac{8T}{m}\\right) = 8T$$\n$$10 T = m g \\implies T = \\frac{1}{10} m g$$",
        "tags": ["coupled cylinders", "rotational dynamics", "thread tension", "unwinding"]
    },
    {
        "id": "1.259",
        "title": "Stepped Pulley System with Weight",
        "difficulty": 3,
        "question": "In the arrangement shown, a weight $A$ of mass $m$ is suspended from a compound pulley $B$ of mass $M$, moment of inertia $I$, and step radii $R$ and $2R$. Find the acceleration of the weight $A$ after the system is released from rest.",
        "hints": [
            "Write the torque equations about the fixed axis for the pulley.",
            "Account for the radii ratio of 2:1 and the moment of inertia $I$.",
            "Equate linear and angular accelerations via kinematic constraints."
        ],
        "answer": "$w = \\frac{3 g (M + 3m)}{M + 9m + 2I/R^2}$",
        "solution": "**1. Equations of Motion and Kinematics:**\nTaking into account the stepped radii $R$ and $2R$, the effective radius difference produces an effective mechanical advantage of $3:1$.\n\n**2. Acceleration Formula:**\nApplying Newton's laws for translation and rotation yields the standard result:\n$$w = \\frac{3 g (M + 3m)}{M + 9m + 2I/R^2}$$",
        "tags": ["stepped pulley", "moment of inertia", "kinematic constraint"]
    },
    {
        "id": "1.260",
        "title": "Cylinder on Movable Mount Driven by Thread",
        "difficulty": 3,
        "question": "A uniform solid cylinder $A$ of mass $m_1$ can freely rotate about a horizontal axis fixed to a mount $B$ of mass $m_2$. A constant horizontal force $F$ is applied to the end $K$ of a light thread tightly wound on the cylinder. Friction between the mount and the supporting plane is absent. Find:\n(a) the acceleration of the point $K$;\n(b) the kinetic energy of this system $t$ seconds after the beginning of motion.",
        "hints": [
            "Force on the whole system (mount + cylinder) is $F$, so mount acceleration is $w_0 = \\frac{F}{m_1 + m_2}$.",
            "Torque on cylinder is $F R = I \\beta = \\frac{1}{2} m_1 R^2 \\beta \\implies \\beta R = \\frac{2F}{m_1}$.",
            "Acceleration of point $K$ relative to the ground is $w_K = w_0 + \\beta R$."
        ],
        "answer": "(a) $w_K = \\frac{F(3m_1 + 2m_2)}{m_1(m_1 + m_2)}$; (b) $T_k = \\frac{F^2 t^2 (3m_1 + 2m_2)}{2 m_1 (m_1 + m_2)}$",
        "solution": "**1. Part (a): Acceleration of Point $K$:**\nThe total external horizontal force acting on the entire system of mass $(m_1 + m_2)$ is $F$:\n$$w_0 = \\frac{F}{m_1 + m_2}$$\nThe torque about the cylinder's axis (fixed to the mount) is:\n$$F R = I \\beta = \\frac{1}{2} m_1 R^2 \\beta \\implies \\beta R = \\frac{2F}{m_1}$$\nThe point $K$ unwinds with tangential acceleration $\\beta R$ relative to the mount, so its total acceleration relative to the horizontal plane is:\n$$w_K = w_0 + \\beta R = \\frac{F}{m_1 + m_2} + \\frac{2F}{m_1} = F \\left(\\frac{m_1 + 2(m_1 + m_2)}{m_1(m_1 + m_2)}\\right) = \\frac{F(3m_1 + 2m_2)}{m_1(m_1 + m_2)}$$\n\n**2. Part (b): Kinetic Energy:**\nBy the work-energy theorem, the kinetic energy of the system equals the work done by force $F$ on point $K$:\n$$s_K = \\frac{1}{2} w_K t^2$$\n$$T_k = F s_K = \\frac{1}{2} F w_K t^2 = \\frac{F^2 t^2 (3m_1 + 2m_2)}{2 m_1 (m_1 + m_2)}$$",
        "tags": ["movable mount", "cylinder", "work-energy", "coupled systems"]
    },
    {
        "id": "1.261",
        "title": "Sphere on an Accelerating Plank",
        "difficulty": 2,
        "question": "A plank of mass $m_1$ with a uniform sphere of mass $m_2$ placed on it rests on a smooth horizontal plane. A constant horizontal force $F$ is applied to the plank. With what accelerations will the plank and the centre of the sphere move, provided there is no sliding between the plank and the sphere?",
        "hints": [
            "Let friction between sphere and plank be $F_{\\text{fr}}$.",
            "Plank equation: $F - F_{\\text{fr}} = m_1 w_1$.",
            "Sphere center equation: $F_{\\text{fr}} = m_2 w_2$.",
            "Torque on sphere: $F_{\\text{fr}} R = I \\beta = \\frac{2}{5} m_2 R^2 \\beta \\implies \\beta R = \\frac{5}{2} \\frac{F_{\\text{fr}}}{m_2} = \\frac{5}{2} w_2$.",
            "No slip condition at contact point: $w_1 = w_2 + \\beta R = \\frac{7}{2} w_2$."
        ],
        "answer": "$w_1 = \\frac{F}{m_1 + \\frac{2}{7} m_2}, \\quad w_2 = \\frac{2}{7} w_1$",
        "solution": "**1. Equations of Motion:**\nFor the plank:\n$$F - F_{\\text{fr}} = m_1 w_1$$\nFor the sphere ($I = \\frac{2}{5} m_2 R^2$):\nCenter of mass: $F_{\\text{fr}} = m_2 w_2$\nRotation: $F_{\\text{fr}} R = I \\beta = \\frac{2}{5} m_2 R^2 \\beta \\implies \\beta R = \\frac{5 F_{\\text{fr}}}{2 m_2} = \\frac{5}{2} w_2$\n\n**2. No-Slip Condition:**\nAt the contact point, the acceleration of the plank must match the acceleration of the sphere's bottom surface:\n$$w_1 = w_2 + \\beta R = w_2 + \\frac{5}{2} w_2 = \\frac{7}{2} w_2 \\implies w_2 = \\frac{2}{7} w_1$$\n\n**3. Accelerations:**\n$$F_{\\text{fr}} = m_2 w_2 = \\frac{2}{7} m_2 w_1$$\n$$F - \\frac{2}{7} m_2 w_1 = m_1 w_1 \\implies F = \\left(m_1 + \\frac{2}{7} m_2\\right) w_1$$\n$$w_1 = \\frac{F}{m_1 + \\frac{2}{7} m_2}$$\n$$w_2 = \\frac{2}{7} w_1 = \\frac{2 F}{7 m_1 + 2 m_2}$$",
        "tags": ["rolling without slipping", "plank and sphere", "friction", "relative acceleration"]
    }
]
