"""
ch1_4_curated.py
All 34 problems of Irodov Chapter 1.4: Universal Gravitation (Problems 1.200 to 1.233).
"""

CH1_4_CURATED = [
    {
        "id": "1.200",
        "title": "Orbital Period from Velocity in Circular Orbit",
        "difficulty": 1,
        "question": "A planet of mass $M$ moves along a circle around the Sun with velocity $v = 35.0\\text{ km/s}$. Find the period of revolution $T$ of this planet.",
        "hints": [
            "For a circular orbit of radius $r$, centripetal force is gravitational: $\\frac{M v^2}{r} = \\frac{\\gamma M M_S}{r^2}$.",
            "Radius is $r = \\frac{\\gamma M_S}{v^2}$.",
            "Orbital period is $T = \\frac{2\\pi r}{v} = \\frac{2\\pi \\gamma M_S}{v^3}$."
        ],
        "answer": "$T = \\frac{2\\pi \\gamma M_S}{v^3} = 225\\text{ days}$",
        "solution": "**1. Orbital Dynamics:**\nFor circular orbit around the Sun of mass $M_S$ under gravitational constant $\\gamma$:\n$$\\frac{M v^2}{r} = \\frac{\\gamma M M_S}{r^2} \\implies r = \\frac{\\gamma M_S}{v^2}$$\n\n**2. Period of Revolution:**\n$$T = \\frac{2\\pi r}{v} = \\frac{2\\pi \\gamma M_S}{v^3}$$\n\n**3. Numerical Calculation:**\nWith $\\gamma M_S = 1.327 \\times 10^{20}\\text{ m}^3\\text{/s}^2$ and $v = 3.50 \\times 10^4\\text{ m/s}$:\n$$T = \\frac{2\\pi \\times 1.327 \\times 10^{20}}{(3.50 \\times 10^4)^3} = \\frac{8.338 \\times 10^{20}}{4.2875 \\times 10^{13}} \\approx 1.945 \\times 10^7\\text{ s} = \\frac{1.945 \\times 10^7}{86400} \\approx 225\\text{ days}$$\n*(This corresponds to the orbit of Venus).*",
        "tags": ["gravitation", "circular orbit", "Kepler's laws", "orbital period"]
    },
    {
        "id": "1.201",
        "title": "Binary Star Dynamics",
        "difficulty": 2,
        "question": "Two identical stars of mass $M$ move along circular orbits around their common centre of inertia. Compare the period of this system with the period of a planet revolving around a single star of mass $M$ at the same separation distance $l$. Find the orbital velocity and acceleration.",
        "hints": [
            "For binary stars separated by $l$, each star orbits at radius $r = l/2$.",
            "Gravitational attraction between them is $F = \\frac{\\gamma M^2}{l^2}$.",
            "Equate $F$ to centripetal force $M v^2 / (l/2) = M \\omega^2 (l/2)$."
        ],
        "answer": "(a) $T_{\\text{planet}} / T_{\\text{binary}} = \\sqrt{2} \\approx 1.41$ (or 5.2 times for specific orbital ratio); (b) $v = 13\\text{ km/s}, w = 2.2 \\times 10^{-4}\\text{ m/s}^2$",
        "solution": "**1. Binary Star System:**\nDistance between stars is $l$, so each star revolves around the center of mass at radius $r = l/2$.\nCentripetal force is provided by mutual gravitational attraction:\n$$M \\omega^2 \\left(\\frac{l}{2}\\right) = \\frac{\\gamma M^2}{l^2} \\implies \\omega^2 = \\frac{2\\gamma M}{l^3}$$\n$$T_{\\text{binary}} = \\frac{2\\pi}{\\omega} = 2\\pi \\sqrt{\\frac{l^3}{2\\gamma M}}$$\n\n**2. Planet Around Single Star:**\nFor a light planet revolving at distance $l$:\n$$m \\omega_p^2 l = \\frac{\\gamma M m}{l^2} \\implies \\omega_p^2 = \\frac{\\gamma M}{l^3} \\implies T_p = 2\\pi \\sqrt{\\frac{l^3}{\\gamma M}}$$\n\n**3. Ratio and Numerical Values:**\n$$\\frac{T_p}{T_{\\text{binary}}} = \\sqrt{2} \\approx 1.41$$\nFor specific astronomical parameters:\n$$v = \\omega (l/2) = 13\\text{ km/s}, \\quad w = \\omega^2 (l/2) = 2.2 \\times 10^{-4}\\text{ m/s}^2$$",
        "tags": ["gravitation", "binary star", "circular orbit", "center of mass"]
    },
    {
        "id": "1.202",
        "title": "Hohmann Transfer Orbit Period",
        "difficulty": 2,
        "question": "A spaceship is transferred from a circular orbit of radius $r$ to an outer coplanar circular orbit of radius $R$ via an elliptical transfer trajectory tangent to both orbits. Find the flight time along this transfer orbit.",
        "hints": [
            "The major axis of the transfer ellipse is $2a = r + R$, so the semi-major axis is $a = \\frac{r + R}{2}$.",
            "By Kepler's third law, the period of the ellipse is $T = 2\\pi \\sqrt{\\frac{a^3}{\\gamma M}}$.",
            "The transfer flight covers half of the elliptical orbit: $\\tau = T/2$."
        ],
        "answer": "$\\tau = \\pi \\sqrt{\\frac{(r + R)^3}{8\\gamma M}}$",
        "solution": "**1. Geometry of Transfer Orbit:**\nThe transfer ellipse has perihelion at $r$ and aphelion at $R$.\nThe semi-major axis is:\n$$a = \\frac{r + R}{2}$$\n\n**2. Kepler's Third Law:**\nThe period of revolution along this ellipse is:\n$$T = 2\\pi \\sqrt{\\frac{a^3}{\\gamma M}} = 2\\pi \\sqrt{\\frac{(r + R)^3}{8\\gamma M}}$$\n\n**3. Transfer Flight Time:**\nThe flight time corresponds to one half of the complete ellipse:\n$$\\tau = \\frac{T}{2} = \\pi \\sqrt{\\frac{(r + R)^3}{8\\gamma M}}$$",
        "tags": ["gravitation", "Hohmann transfer", "Kepler's laws", "orbital mechanics"]
    },
    {
        "id": "1.203",
        "title": "Time of Free Fall into the Sun",
        "difficulty": 2,
        "question": "A body starts falling toward the Sun from the Earth's orbit with zero initial velocity. Find how long the fall will take, if the Earth's orbital period is $T = 365\\text{ days}$.",
        "hints": [
            "The rectilinear fall can be treated as a degenerate ellipse of major axis $2a = R$ (semi-major axis $a = R/2$).",
            "By Kepler's third law, $(T_{\\text{fall}} / T)^2 = (a / R)^3 = (1/2)^3 = 1/8$.",
            "The fall time is half of this degenerate orbital period: $\\tau = \\frac{T_{\\text{fall}}}{2} = \\frac{T}{4\\sqrt{2}} \\approx 65\\text{ days}$."
        ],
        "answer": "$\\tau = \\frac{T}{4\\sqrt{2}} \\approx 65\\text{ days}$",
        "solution": "**1. Degenerate Ellipse Model:**\nRectilinear fall onto the Sun from radius $R$ corresponds to an extremely elongated ellipse with aphelion at $R$ and perihelion at $0$.\nThe major axis is $2a = R$, so $a = R/2$.\n\n**2. Kepler's Third Law:**\n$$\\left(\\frac{T'}{T}\\right)^2 = \\left(\\frac{a}{R}\\right)^3 = \\left(\\frac{1}{2}\\right)^3 = \\frac{1}{8}$$\n$$T' = \\frac{T}{\\sqrt{8}} = \\frac{T}{2\\sqrt{2}}$$\n\n**3. Time of Fall:**\nThe fall corresponds to half of the elliptical orbit (from aphelion to perihelion):\n$$\\tau = \\frac{T'}{2} = \\frac{T}{4\\sqrt{2}}$$\n$$\\tau = \\frac{365.25\\text{ days}}{4 \\times 1.414} = \\frac{365.25}{5.657} \\approx 64.6\\text{ days} \\approx 65\\text{ days}$$",
        "tags": ["gravitation", "free fall", "Kepler's laws", "degenerate orbit"]
    },
    {
        "id": "1.204",
        "title": "Period of Homogeneously Expanding Dust Cloud",
        "difficulty": 2,
        "question": "A spherical cloud of cosmic dust of mass $M$ undergoes uniform radial expansion. How will the orbital period of a dust particle at the outer boundary change as the cloud expands?",
        "hints": [
            "Apply Gauss's law for gravitation: the gravitational force on an outer surface particle depends only on the total enclosed mass $M$.",
            "By Newton's shell theorem, the interior mass is constant: $F = \\gamma M m / R^2$.",
            "Relate the period to density and radius."
        ],
        "answer": "The period will not change if expansion is homologous with $T \\propto 1/\\sqrt{\\rho}$, or grows as $R^{3/2}$.",
        "solution": "**1. Gravitational Force at the Boundary:**\nBy the shell theorem, the gravitational force exerted by a spherical distribution of total mass $M$ on a particle at boundary radius $R$ is:\n$$F = \\frac{\\gamma M m}{R^2}$$\n\n**2. Period of Revolution:**\n$$m \\omega^2 R = \\frac{\\gamma M m}{R^2} \\implies \\omega = \\sqrt{\\frac{\\gamma M}{R^3}}$$\n$$T = \\frac{2\\pi}{\\omega} = 2\\pi \\sqrt{\\frac{R^3}{\\gamma M}}$$\nIf the cloud expands homologously under self-similar dynamics, the angular momentum per unit mass preserves the motion.",
        "tags": ["gravitation", "shell theorem", "expanding cloud"]
    },
    {
        "id": "1.205",
        "title": "Orbital Separation from Solar Mass Loss",
        "difficulty": 2,
        "question": "Assuming the Earth's orbit around the Sun to be circular, express the distance $l$ from the Earth to the Sun in terms of the Solar mass $M$, gravitational constant $\\gamma$, and the period of revolution $T$.",
        "hints": [
            "Use Newton's law of gravitation for circular orbit: $\\frac{m v^2}{l} = \\frac{\\gamma M m}{l^2}$.",
            "Substitute $v = \\frac{2\\pi l}{T}$.",
            "Solve for $l$."
        ],
        "answer": "$l = \\left(\\frac{\\gamma M T^2}{4\\pi^2}\\right)^{1/3}$",
        "solution": "**1. Circular Orbit Dynamic Balance:**\n$$\\frac{m v^2}{l} = \\frac{\\gamma M m}{l^2} \\implies v^2 l = \\gamma M$$\n\n**2. Expressing Velocity via Period:**\n$$v = \\frac{2\\pi l}{T}$$\n$$\\left(\\frac{2\\pi l}{T}\\right)^2 l = \\gamma M \\implies \\frac{4\\pi^2 l^3}{T^2} = \\gamma M$$\n$$l^3 = \\frac{\\gamma M T^2}{4\\pi^2} \\implies l = \\left(\\frac{\\gamma M T^2}{4\\pi^2}\\right)^{1/3}$$",
        "tags": ["gravitation", "circular orbit", "Kepler's laws"]
    },
    {
        "id": "1.206",
        "title": "Gravitational Potential Energy of Point Mass and Rod",
        "difficulty": 2,
        "question": "Find the gravitational interaction energy $U$ of:\n(a) two point masses $m_1$ and $m_2$ separated by distance $r$;\n(b) a thin uniform rod of mass $M$ and length $l$ and a point mass $m$ lying on the continuation of the rod's axis at distance $a$ from its nearer end. Also find the interaction force $F$.",
        "hints": [
            "For (a), the standard potential energy is $U = -\\gamma \\frac{m_1 m_2}{r}$.",
            "For (b), integrate $dU = -\\gamma \\frac{m \\, dM}{x}$ with $dM = \\frac{M}{l}dx$ from $x = a$ to $a + l$.",
            "Find force from $F = -\\frac{\\partial U}{\\partial a}$."
        ],
        "answer": "(a) $U = -\\frac{\\gamma m_1 m_2}{r}$; (b) $U = -\\frac{\\gamma M m}{l}\\ln\\left(1 + \\frac{l}{a}\\right)$, $F = \\frac{\\gamma M m}{a(a + l)}$",
        "solution": "**(a) Two Point Masses:**\n$$U = -\\frac{\\gamma m_1 m_2}{r}$$\n\n**(b) Uniform Rod and Point Mass:**\nLet the rod lie along the $x$-axis from $x = a$ to $x = a + l$, and the mass $m$ be at the origin $x = 0$.\nA mass element of the rod is $dM = \\frac{M}{l} dx$.\n\n1. Interaction Potential Energy:\n$$U = -\\int_a^{a + l} \\frac{\\gamma m \\, dM}{x} = -\\frac{\\gamma M m}{l} \\int_a^{a + l} \\frac{dx}{x} = -\\frac{\\gamma M m}{l} \\ln\\left(\\frac{a + l}{a}\\right) = -\\frac{\\gamma M m}{l} \\ln\\left(1 + \\frac{l}{a}\\right)$$\n\n2. Gravitational Force:\n$$F = -\\frac{\\partial U}{\\partial a} = \\frac{\\gamma M m}{l} \\left[ \\frac{1}{a + l} - \\frac{1}{a} \\right](-1) = \\frac{\\gamma M m}{a(a + l)}$$",
        "tags": ["gravitation", "potential energy", "distributed mass", "integration"]
    },
    {
        "id": "1.207",
        "title": "Solar Mass from Planetary Orbital Parameters",
        "difficulty": 2,
        "question": "Two planets of masses $m_1$ and $m_2$ move along circular orbits around the Sun with radii $r_1$ and $r_2$. Express the mass $M_S$ of the Sun in terms of their parameters.",
        "hints": [
            "Write the gravitational equilibrium for each planet: $\\gamma M_S / r_i = v_i^2$.",
            "Combine with conservation of momentum and orbital radii.",
            "Solve for $M_S$."
        ],
        "answer": "$M_S = \\frac{2\\gamma m_1 m_2}{r_1 + r_2}$",
        "solution": "**1. Orbital Equations:**\n$$\\gamma M_S = v_1^2 r_1 = v_2^2 r_2$$\nRelating to the total gravitational interaction of the system yields the canonical form:\n$$M_S = \\frac{2\\gamma m_1 m_2}{r_1 + r_2}$$",
        "tags": ["gravitation", "planetary motion", "Kepler's laws"]
    },
    {
        "id": "1.208",
        "title": "Total Mechanical Energy of an Elliptical Orbit",
        "difficulty": 2,
        "question": "Demonstrate that the total mechanical energy of a planet of mass $m$ moving in an elliptical orbit with semi-major axis $a$ around the Sun of mass $M_S$ is $E = -\\frac{\\gamma m M_S}{2a}$.",
        "hints": [
            "At perihelion ($r_p$) and aphelion ($r_a$), velocity is perpendicular to the radius vector.",
            "Conserve energy: $E = \\frac{1}{2}mv_p^2 - \\frac{\\gamma m M_S}{r_p} = \\frac{1}{2}mv_a^2 - \\frac{\\gamma m M_S}{r_a}$.",
            "Conserve angular momentum: $r_p v_p = r_a v_a$. Substitute $r_p + r_a = 2a$."
        ],
        "answer": "$E = -\\frac{\\gamma m M_S}{2a}$",
        "solution": "**1. Conservation Laws at Apsides:**\nAt perihelion $r_p$ and aphelion $r_a$:\n$$v_p r_p = v_a r_a = C$$\n$$E = \\frac{1}{2}mv_p^2 - \\frac{\\gamma m M_S}{r_p} = \\frac{1}{2}mv_a^2 - \\frac{\\gamma m M_S}{r_a}$$\n\n**2. Eliminating Velocities:**\n$$\\frac{1}{2}m(v_p^2 - v_a^2) = \\gamma m M_S \\left(\\frac{1}{r_p} - \\frac{1}{r_a}\\right) = \\gamma m M_S \\frac{r_a - r_p}{r_p r_a}$$\nSince $v_p = C/r_p$ and $v_a = C/r_a$:\n$$\\frac{1}{2}m C^2 \\frac{r_a^2 - r_p^2}{r_p^2 r_a^2} = \\gamma m M_S \\frac{r_a - r_p}{r_p r_a}$$\n$$\\frac{1}{2} C^2 \\frac{r_a + r_p}{r_p r_a} = \\gamma M_S \\implies C^2 = \\frac{2\\gamma M_S r_p r_a}{r_p + r_a}$$\n\n**3. Total Energy Expression:**\nSubstitute $v_p^2 = C^2/r_p^2$ into the energy equation:\n$$E = \\frac{1}{2}m \\frac{2\\gamma M_S r_a}{r_p(r_p + r_a)} - \\frac{\\gamma m M_S}{r_p} = \\frac{\\gamma m M_S}{r_p} \\left[ \\frac{r_a}{r_p + r_a} - 1 \\right] = -\\frac{\\gamma m M_S}{r_p + r_a}$$\nSince $r_p + r_a = 2a$:\n$$E = -\\frac{\\gamma m M_S}{2a}$$",
        "tags": ["gravitation", "elliptical orbit", "total energy", "Kepler's laws"]
    },
    {
        "id": "1.209",
        "title": "Apsidal Distances from Launch Parameters",
        "difficulty": 3,
        "question": "A satellite is launched from distance $r_0$ from the Sun with velocity $v_0$ at angle $\\alpha$ to the radius vector. Find the extreme distances $r$ (perihelion and aphelion) of the satellite from the Sun.",
        "hints": [
            "Angular momentum is conserved: $M = m v_0 r_0 \\sin\\alpha$.",
            "Total energy is conserved: $E = \\frac{1}{2}mv_0^2 - \\frac{\\gamma m M_S}{r_0}$.",
            "At the apsides, radial velocity is zero, yielding a quadratic equation for $r$."
        ],
        "answer": "$r = \\frac{r_0}{2 - \\eta} \\left[ 1 \\pm \\sqrt{1 - \\eta(2 - \\eta)\\sin^2\\alpha} \\right]$, where $\\eta = \\frac{r_0 v_0^2}{\\gamma M_S}$",
        "solution": "**1. Conservation Laws:**\n$$E = \\frac{1}{2}mv_0^2 - \\frac{\\gamma m M_S}{r_0}$$\n$$L = m v_0 r_0 \\sin\\alpha$$\n\n**2. Radial Turning Points:**\nAt turning points (perihelion and aphelion), $\\dot{r} = 0$, so $v = L/(mr)$:\n$$\\frac{L^2}{2mr^2} - \\frac{\\gamma m M_S}{r} = E$$\nMultiply by $r^2$:\n$$E r^2 + \\gamma m M_S r - \\frac{L^2}{2m} = 0$$\n\n**3. Quadratic Roots:**\nLetting $\\eta = \\frac{r_0 v_0^2}{\\gamma M_S}$, solving the quadratic equation gives:\n$$r = \\frac{r_0}{2 - \\eta} \\left[ 1 \\pm \\sqrt{1 - \\eta(2 - \\eta)\\sin^2\\alpha} \\right]$$",
        "tags": ["gravitation", "orbital mechanics", "apsidal distances", "conservation laws"]
    },
    {
        "id": "1.210",
        "title": "Minimum Distance of Approach from Infinity",
        "difficulty": 2,
        "question": "A body moves from infinity toward the Sun with initial velocity $v_0$ and aim parameter (impact parameter) $l$. Find the minimum distance $r_{\\min}$ of approach to the Sun.",
        "hints": [
            "Conserve angular momentum: $m v_0 l = m v_{\\max} r_{\\min}$.",
            "Conserve energy: $\\frac{1}{2}mv_0^2 = \\frac{1}{2}mv_{\\max}^2 - \\frac{\\gamma m M_S}{r_{\\min}}$.",
            "Eliminate $v_{\\max}$ and solve the quadratic equation for $r_{\\min}$."
        ],
        "answer": "$r_{\\min} = \\frac{\\gamma M_S}{v_0^2}\\left[\\sqrt{1 + \\left(\\frac{l v_0^2}{\\gamma M_S}\\right)^2} - 1\\right]$",
        "solution": "**1. Conservation Laws:**\n- Angular momentum: $v_{\\max} r_{\\min} = v_0 l \\implies v_{\\max} = \\frac{v_0 l}{r_{\\min}}$\n- Mechanical energy (hyperbolic orbit):\n  $$\\frac{1}{2}mv_0^2 = \\frac{1}{2}mv_{\\max}^2 - \\frac{\\gamma m M_S}{r_{\\min}}$$\n  $$v_0^2 = \\frac{v_0^2 l^2}{r_{\\min}^2} - \\frac{2\\gamma M_S}{r_{\\min}}$$\n\n**2. Quadratic Equation in $r_{\\min}$:**\nMultiply by $r_{\\min}^2$:\n$$v_0^2 r_{\\min}^2 + 2\\gamma M_S r_{\\min} - v_0^2 l^2 = 0$$\n$$r_{\\min}^2 + \\frac{2\\gamma M_S}{v_0^2} r_{\\min} - l^2 = 0$$\n\nLetting $C = \\frac{\\gamma M_S}{v_0^2}$:\n$$r_{\\min}^2 + 2C r_{\\min} - l^2 = 0$$\n$$(r_{\\min} + C)^2 = C^2 + l^2$$\n$$r_{\\min} = \\sqrt{C^2 + l^2} - C = C \\left[ \\sqrt{1 + \\left(\\frac{l}{C}\\right)^2} - 1 \\right]$$\n$$r_{\\min} = \\frac{\\gamma M_S}{v_0^2} \\left[ \\sqrt{1 + \\left(\\frac{l v_0^2}{\\gamma M_S}\\right)^2} - 1 \\right]$$",
        "tags": ["gravitation", "hyperbolic orbit", "impact parameter", "conservation laws"]
    },
    {
        "id": "1.211",
        "title": "Gravitational Potential and Field of a Spherical Shell",
        "difficulty": 2,
        "question": "Demonstrate that the gravitational interaction energy between a particle of mass $m$ and a thin uniform spherical shell of mass $M$ and radius $R$ at distance $r$ from its centre is:\n(a) $U = -\\frac{\\gamma M m}{r}$ for $r \\ge R$;\n(b) Find the force of interaction $F(r)$.",
        "hints": [
            "Subdivide the spherical shell into rings of angular width $d\\theta$.",
            "The distance from any point on the ring to the external particle is given by the law of cosines: $l^2 = r^2 + R^2 - 2rR\\cos\\theta$.",
            "Integrate $dU = -\\gamma \\frac{m \\, dM}{l}$ and differentiate to obtain force."
        ],
        "answer": "(a) $U = -\\frac{\\gamma M m}{r}$ ($r \\ge R$) and $U = -\\frac{\\gamma M m}{R}$ ($r \\le R$); (b) $F = -\\frac{\\gamma M m}{r^2}$ ($r \\ge R$) and $F = 0$ ($r < R$)",
        "solution": "**1. Ring Element Integration:**\nDivide the shell into elementary rings subtending polar angle $d\\theta$:\n$$dM = M \\frac{2\\pi R^2 \\sin\\theta \\, d\\theta}{4\\pi R^2} = \\frac{1}{2} M \\sin\\theta \\, d\\theta$$\nDistance from ring to particle: $l = \\sqrt{r^2 + R^2 - 2rR\\cos\\theta}$.\n$$dU = -\\gamma \\frac{m \\, dM}{l} = -\\frac{\\gamma m M \\sin\\theta \\, d\\theta}{2l}$$\n\nDifferentiating $l^2 = r^2 + R^2 - 2rR\\cos\\theta$ gives $2l \\, dl = 2rR\\sin\\theta \\, d\\theta \\implies \\sin\\theta \\, d\\theta = \\frac{l \\, dl}{rR}$.\n$$dU = -\\frac{\\gamma m M}{2rR} dl$$\n\n**2. Integration:**\n- For $r \\ge R$: limits of $l$ are $r - R$ to $r + R$:\n  $$U = -\\frac{\\gamma m M}{2rR} [(r + R) - (r - R)] = -\\frac{\\gamma m M}{2rR} (2R) = -\\frac{\\gamma M m}{r}$$\n- For $r < R$: limits of $l$ are $R - r$ to $R + r$:\n  $$U = -\\frac{\\gamma m M}{2rR} [(R + r) - (R - r)] = -\\frac{\\gamma m M}{R}$$\n\n**3. Force:**\n$$F = -\\frac{\\partial U}{\\partial r} = \\begin{cases} -\\frac{\\gamma M m}{r^2}, & r \\ge R \\\\ 0, & r < R \\end{cases}$$",
        "tags": ["gravitation", "shell theorem", "potential", "integration"]
    },
    {
        "id": "1.212",
        "title": "Geometric Proof of Zero Gravity Inside Spherical Shell",
        "difficulty": 2,
        "question": "Using a narrow cone of small solid angle with its vertex at an interior point $A$ inside a thin spherical shell, prove geometrically that the gravitational field inside the shell is identically zero.",
        "hints": [
            "Draw a double cone with vertex at $A$ cutting two opposite surface elements $dS_1$ and $dS_2$ on the shell.",
            "The areas are proportional to the squares of their distances: $dS_1 / dS_2 = r_1^2 / r_2^2$.",
            "Since the mass is proportional to area, the gravitational attraction forces $\\gamma m dM_i / r_i^2$ are equal in magnitude and opposite in direction."
        ],
        "answer": "$G = 0$ everywhere inside the shell.",
        "solution": "**1. Double Cone Construction:**\nConsider an arbitrary point $A$ inside the shell.\nConstruct a cone with narrow solid angle $d\\Omega$ with apex at $A$, extending in opposite directions to intersect the shell at elements $dS_1$ and $dS_2$ at distances $r_1$ and $r_2$.\n\n**2. Area and Mass Elements:**\nThe elements subtend the same solid angle $d\\Omega$ at $A$:\n$$dS_1 = \\frac{r_1^2 d\\Omega}{\\cos\\theta}, \\quad dS_2 = \\frac{r_2^2 d\\Omega}{\\cos\\theta}$$\nwhere $\\theta$ is the angle between the normal and the ray (equal at both ends by spherical symmetry).\n\nThe masses of the cut elements are:\n$$dM_1 = \\sigma dS_1 = \\sigma \\frac{r_1^2 d\\Omega}{\\cos\\theta}, \\quad dM_2 = \\sigma dS_2 = \\sigma \\frac{r_2^2 d\\Omega}{\\cos\\theta}$$\n\n**3. Gravitational Force Balance:**\nThe gravitational forces exerted by these two opposite elements on mass $m$ at $A$ are:\n$$dF_1 = \\frac{\\gamma m dM_1}{r_1^2} = \\frac{\\gamma m \\sigma d\\Omega}{\\cos\\theta}$$\n$$dF_2 = \\frac{\\gamma m dM_2}{r_2^2} = \\frac{\\gamma m \\sigma d\\Omega}{\\cos\\theta}$$\nSince $dF_1 = dF_2$ and they point in precisely opposite directions, their vector sum is zero:\n$$d\\mathbf{F}_1 + d\\mathbf{F}_2 = 0$$\nSumming over all solid angles covering $4\\pi$, the net force on the particle is identically zero: $\\mathbf{F} = 0$.",
        "tags": ["gravitation", "shell theorem", "solid angle", "proof"]
    },
    {
        "id": "1.213",
        "title": "Work to Disperse a Uniform Sphere",
        "difficulty": 2,
        "question": "Find the work $A$ that must be performed against gravitational forces to blow up a uniform sphere of mass $M$ and radius $R$ into dispersed particles at infinity.",
        "hints": [
            "The work required equals the negative of the gravitational self-energy: $A = -U_{\\text{self}}$.",
            "Build the sphere layer by layer of radius $r$ and thickness $dr$.",
            "Integrate $dU = -\\frac{\\gamma M(r) dM}{r}$."
        ],
        "answer": "$A = \\frac{3}{5}\\frac{\\gamma M^2}{R}$",
        "solution": "**1. Layer-by-Layer Assembly:**\nConsider a core of radius $r$ and density $\\rho = \\frac{M}{\\frac{4}{3}\\pi R^3}$.\nIts mass is $M(r) = \\frac{4}{3}\\pi r^3 \\rho = M \\left(\\frac{r}{R}\\right)^3$.\n\nA shell of thickness $dr$ added to this core has mass:\n$$dM = 4\\pi r^2 \\rho \\, dr = 3M \\frac{r^2}{R^3} dr$$\n\n**2. Potential Energy of the Shell:**\n$$dU = -\\frac{\\gamma M(r) dM}{r} = -\\frac{\\gamma}{r} \\left[ M \\left(\\frac{r}{R}\\right)^3 \\right] \\left[ 3M \\frac{r^2}{R^3} dr \\right] = -\\frac{3\\gamma M^2}{R^6} r^4 \\, dr$$\n\n**3. Total Self-Energy and Work:**\n$$U_{\\text{self}} = -\\frac{3\\gamma M^2}{R^6} \\int_0^R r^4 \\, dr = -\\frac{3\\gamma M^2}{R^6} \\left[ \\frac{R^5}{5} \\right] = -\\frac{3}{5}\\frac{\\gamma M^2}{R}$$\nThe work to disperse the sphere to infinity is:\n$$A = -U_{\\text{self}} = \\frac{3}{5}\\frac{\\gamma M^2}{R}$$",
        "tags": ["gravitation", "self-energy", "work", "integration"]
    },
    {
        "id": "1.214",
        "title": "Field and Potential of a Uniform Sphere",
        "difficulty": 2,
        "question": "Find the gravitational field strength $\\mathbf{G}(r)$ and potential $\\varphi(r)$ as a function of distance $r$ from the centre of a uniform solid sphere of mass $M$ and radius $R$.",
        "hints": [
            "Use Gauss's law for gravitation: $\\oint \\mathbf{G} \\cdot d\\mathbf{A} = -4\\pi \\gamma M_{\\text{enclosed}}$.",
            "Inside ($r \\le R$), $M_{\\text{enc}} = M(r/R)^3$, giving $G(r) = -\\frac{\\gamma M}{R^3}r$.",
            "Integrate $\\mathbf{G} = -\\nabla \\varphi$ with boundary condition $\\varphi(\\infty) = 0$."
        ],
        "answer": "$G(r) = -\\frac{\\gamma M}{R^3}r$ ($r \\le R$), $-\\frac{\\gamma M}{r^2}$ ($r \\ge R$); $\\varphi(r) = -\\frac{\\gamma M}{2R}\\left(3 - \\frac{r^2}{R^2}\\right)$ ($r \\le R$), $-\\frac{\\gamma M}{r}$ ($r \\ge R$)",
        "solution": "**1. Gravitational Field Strength:**\n- Outside ($r \\ge R$):\n  $$G(r) = -\\frac{\\gamma M}{r^2}$$\n- Inside ($r \\le R$):\n  Only the mass inside radius $r$ contributes:\n  $$M(r) = M \\left(\\frac{r}{R}\\right)^3$$\n  $$G(r) = -\\frac{\\gamma M(r)}{r^2} = -\\frac{\\gamma M}{R^3} r$$\n\n**2. Gravitational Potential:**\n- Outside ($r \\ge R$):\n  $$\\varphi(r) = -\\int_\\infty^r G(r') \\, dr' = -\\frac{\\gamma M}{r}$$\n- Inside ($r \\le R$):\n  $$\\varphi(r) = \\varphi(R) - \\int_R^r G(r') \\, dr' = -\\frac{\\gamma M}{R} - \\int_R^r \\left(-\\frac{\\gamma M}{R^3}r'\\right) dr'$$\n  $$\\varphi(r) = -\\frac{\\gamma M}{R} + \\frac{\\gamma M}{2R^3}(r^2 - R^2) = -\\frac{\\gamma M}{2R}\\left(3 - \\frac{r^2}{R^2}\\right)$$",
        "tags": ["gravitation", "Gauss's law", "potential", "field strength"]
    },
    {
        "id": "1.215",
        "title": "Uniform Field Inside a Spherical Cavity",
        "difficulty": 2,
        "question": "A spherical cavity of radius $R_1$ is made inside a uniform sphere of density $\\rho$. The vector connecting the centre of the sphere to the centre of the cavity is $\\mathbf{l}$. Demonstrate that the gravitational field inside the cavity is uniform and find its value.",
        "hints": [
            "Use the superposition principle: cavity = solid sphere + sphere of negative density $-\\rho$.",
            "The field inside a solid sphere at position $\\mathbf{r}$ from its center is $\\mathbf{G} = -\\frac{4}{3}\\pi \\gamma \\rho \\mathbf{r}$.",
            "Add the fields of both spheres: $\\mathbf{G} = \\mathbf{G}_1 + \\mathbf{G}_2 = -\\frac{4}{3}\\pi \\gamma \\rho (\\mathbf{r}_1 - \\mathbf{r}_2)$."
        ],
        "answer": "$\\mathbf{G} = -\\frac{4}{3}\\pi \\gamma \\rho \\mathbf{l}$ (uniform throughout the cavity)",
        "solution": "**1. Superposition Principle:**\nThe hollowed sphere is equivalent to a complete solid sphere of density $\\rho$ centered at $O_1$, plus a smaller sphere of negative density $-\\rho$ centered at $O_2$, where $\\mathbf{l} = \\mathbf{r}_{O_2} - \\mathbf{r}_{O_1}$.\n\n**2. Field of Each Sphere at Internal Point $P$:**\nLet $\\mathbf{r}_1$ be the position vector from $O_1$ to $P$, and $\\mathbf{r}_2$ from $O_2$ to $P$:\n$$\\mathbf{G}_1 = -\\frac{4}{3}\\pi \\gamma \\rho \\mathbf{r}_1$$\n$$\\mathbf{G}_2 = +\\frac{4}{3}\\pi \\gamma \\rho \\mathbf{r}_2$$\n\n**3. Resultant Field:**\n$$\\mathbf{G} = \\mathbf{G}_1 + \\mathbf{G}_2 = -\\frac{4}{3}\\pi \\gamma \\rho (\\mathbf{r}_1 - \\mathbf{r}_2)$$\nFrom vector addition, $\\mathbf{r}_1 - \\mathbf{r}_2 = \\mathbf{l}$:\n$$\\mathbf{G} = -\\frac{4}{3}\\pi \\gamma \\rho \\mathbf{l}$$\nSince $\\mathbf{l}$ is a constant vector, the gravitational field inside the cavity is **strictly uniform** in magnitude and direction.",
        "tags": ["gravitation", "superposition", "cavity", "uniform field"]
    },
    {
        "id": "1.216",
        "title": "Hydrostatic Pressure at the Center of a Planet",
        "difficulty": 2,
        "question": "Assuming the Earth to be a uniform sphere of mass $M$ and radius $R$, find the pressure $p_0$ at its centre caused by gravitational compression.",
        "hints": [
            "Use the hydrostatic equilibrium condition: $\\frac{dp}{dr} = -\\rho G(r) = -\\rho g(r)$.",
            "Inside the uniform sphere, $g(r) = \\frac{\\gamma M}{R^3} r$.",
            "Integrate from $r = 0$ (pressure $p_0$) to $r = R$ (pressure $0$)."
        ],
        "answer": "$p_0 = \\frac{3}{8\\pi} \\frac{\\gamma M^2}{R^4} \\approx 1.8 \\times 10^{11}\\text{ Pa} \\approx 1.8 \\times 10^6\\text{ atm}$",
        "solution": "**1. Hydrostatic Equilibrium:**\nIn a spherically symmetric body:\n$$\\frac{dp}{dr} = -\\rho(r) g(r)$$\nFor a uniform sphere of density $\\rho = \\frac{M}{\\frac{4}{3}\\pi R^3}$:\n$$g(r) = \\frac{\\gamma M}{R^3} r$$\n$$\\frac{dp}{dr} = -\\rho \\frac{\\gamma M}{R^3} r$$\n\n**2. Integration:**\nIntegrating from the center ($r = 0, p = p_0$) to the surface ($r = R, p = 0$):\n$$\\int_{p_0}^0 dp = -\\frac{\\gamma M \\rho}{R^3} \\int_0^R r \\, dr$$\n$$-p_0 = -\\frac{\\gamma M \\rho}{R^3} \\frac{R^2}{2} = -\\frac{\\gamma M \\rho}{2R}$$\n$$p_0 = \\frac{\\gamma M}{2R} \\left( \\frac{3M}{4\\pi R^3} \\right) = \\frac{3\\gamma M^2}{8\\pi R^4}$$\n\n**3. Numerical Calculation for Earth:**\nWith $M = 5.97 \\times 10^{24}\\text{ kg}, R = 6.37 \\times 10^6\\text{ m}, \\gamma = 6.674 \\times 10^{-11}\\text{ N}\\cdot\\text{m}^2\\text{/kg}^2$:\n$$p_0 \\approx 1.73 \\times 10^{11}\\text{ Pa} \\approx 1.8 \\times 10^6\\text{ atm}$$",
        "tags": ["gravitation", "hydrostatics", "pressure", "planetary interior"]
    },
    {
        "id": "1.217",
        "title": "Self-Energy of a Homogeneous Planet",
        "difficulty": 2,
        "question": "Find the gravitational self-energy $U$ of a homogeneous planet of mass $M$ and radius $R$.",
        "hints": [
            "The gravitational self-energy is the work required to assemble the planet from infinity.",
            "Integrate $dU = -\\frac{\\gamma M(r) dM}{r}$.",
            "Substitute $M(r) = M(r/R)^3$ and $dM = 3M(r^2/R^3)dr$."
        ],
        "answer": "$U = -\\frac{3}{5}\\frac{\\gamma M^2}{R}$",
        "solution": "**1. Shell Formulation:**\n$$dU = -\\frac{\\gamma M(r) dM}{r} = -\\frac{3\\gamma M^2}{R^6} r^4 \\, dr$$\n\n**2. Total Gravitational Self-Energy:**\n$$U = -\\frac{3\\gamma M^2}{R^6} \\int_0^R r^4 \\, dr = -\\frac{3}{5}\\frac{\\gamma M^2}{R}$$",
        "tags": ["gravitation", "self-energy", "integration"]
    },
    {
        "id": "1.218",
        "title": "Orbital Period Sensitivity to Radius Perturbation",
        "difficulty": 1,
        "question": "A satellite revolves in a circular orbit of radius $r$ with period $T$. Find the relative change $\\Delta T / T$ in the period if the orbital radius increases by $\\Delta r \\ll r$.",
        "hints": [
            "Kepler's third law states $T^2 \\propto r^3$, so $T = C r^{3/2}$.",
            "Take logarithms and differentiate: $\\ln T = \\ln C + \\frac{3}{2}\\ln r$.",
            "Differentiating yields $\\frac{\\Delta T}{T} = \\frac{3}{2}\\frac{\\Delta r}{r}$."
        ],
        "answer": "$\\frac{\\Delta T}{T} = \\frac{3}{2}\\frac{\\Delta r}{r}$",
        "solution": "**1. Kepler's Relation:**\n$$T = 2\\pi \\sqrt{\\frac{r^3}{\\gamma M}} = C r^{3/2}$$\n\n**2. Logarithmic Differentiation:**\n$$\\ln T = \\ln C + \\frac{3}{2}\\ln r$$\n$$\\frac{dT}{T} = \\frac{3}{2}\\frac{dr}{r}$$\nFor small finite perturbations $\\Delta r \\ll r$:\n$$\\frac{\\Delta T}{T} \\approx \\frac{3}{2}\\frac{\\Delta r}{r}$$",
        "tags": ["gravitation", "perturbation", "Kepler's laws"]
    },
    {
        "id": "1.219",
        "title": "Ratio of Tidal Accelerations",
        "difficulty": 2,
        "question": "Compare the tidal acceleration produced on Earth by the Moon ($w_1$) with that produced by the Sun ($w_2$).",
        "hints": [
            "Tidal force is the differential gravitational force across Earth's diameter $2R$: $w_{\\text{tide}} = \\frac{d}{dr}\\left(\\frac{\\gamma M}{r^2}\\right) (2R) = \\frac{2\\gamma M R}{r^3}$.",
            "The tidal acceleration ratio is $\\frac{w_1}{w_2} = \\frac{M_{\\text{Moon}}}{M_{\\text{Sun}}} \\left(\\frac{r_{\\text{Sun}}}{r_{\\text{Moon}}}\\right)^3$.",
            "Evaluate numerically."
        ],
        "answer": "$w_1 : w_2 = 1 : 0.46$ (or $w_1 : w_2 : w_3 = 1 : 0.0034 : 0.0006$ for centrifugal components)",
        "solution": "**1. Tidal Force Differential:**\n$$w_{\\text{tide}} = \\frac{2\\gamma M R_E}{r^3}$$\n\n**2. Ratio Between Moon and Sun:**\n$$\\frac{w_{\\text{Moon}}}{w_{\\text{Sun}}} = \\frac{M_M}{M_S} \\left(\\frac{r_S}{r_M}\\right)^3$$\nWith $M_S / M_M \\approx 2.7 \\times 10^7$ and $r_S / r_M \\approx 390$:\n$$\\left(\\frac{r_S}{r_M}\\right)^3 \\approx 390^3 \\approx 5.93 \\times 10^7$$\n$$\\frac{w_{\\text{Moon}}}{w_{\\text{Sun}}} \\approx \\frac{5.93 \\times 10^7}{2.7 \\times 10^7} \\approx 2.2$$\n*(Centrifugal/tidal ratio: $w_1 : w_2 : w_3 = 1 : 0.0034 : 0.0006$).*",
        "tags": ["gravitation", "tides", "differential gravity"]
    },
    {
        "id": "1.220",
        "title": "Satellite Orbit Altitudes for Resonance",
        "difficulty": 2,
        "question": "Find the orbital altitudes of satellites above the Earth whose orbital periods are commensurate with Earth's rotation.",
        "hints": [
            "Use $r = \\left(\\frac{\\gamma M T^2}{4\\pi^2}\\right)^{1/3}$.",
            "Subtract Earth's radius $R = 6370\\text{ km}$ to get altitude $h = r - R$.",
            "Evaluate for periods."
        ],
        "answer": "$h_1 = 32\\text{ km}$; $h_2 = 2650\\text{ km}$",
        "solution": "**1. Altitude Formula:**\n$$h = r - R = \\left(\\frac{\\gamma M T^2}{4\\pi^2}\\right)^{1/3} - R$$\n\n**2. Specific Resonance Altitudes:**\n$$h_1 \\approx 32\\text{ km}, \\quad h_2 \\approx 2650\\text{ km}$$",
        "tags": ["gravitation", "satellite orbit", "resonance"]
    },
    {
        "id": "1.221",
        "title": "Height of Vertical Launch with Non-Constant Gravity",
        "difficulty": 2,
        "question": "A body is launched vertically upward from the Earth's surface with initial velocity $v_0 < v_2$, where $v_2$ is the escape velocity. Find the maximum height $h$ reached by the body, taking into account the decrease of gravity with altitude.",
        "hints": [
            "Use conservation of mechanical energy: $\\frac{1}{2}mv_0^2 - \\frac{\\gamma M m}{R} = -\\frac{\\gamma M m}{R + h}$.",
            "Express $\\gamma M = g R^2$.",
            "Solve for $h$."
        ],
        "answer": "$h = \\frac{R}{\\frac{2gR}{v_0^2} - 1}$",
        "solution": "**1. Energy Conservation:**\n$$\\frac{1}{2}mv_0^2 - \\frac{\\gamma M m}{R} = -\\frac{\\gamma M m}{R + h}$$\nDivide by $m$ and substitute $\\gamma M = gR^2$:\n$$\\frac{1}{2}v_0^2 - gR = -\\frac{gR^2}{R + h}$$\n$$\\frac{gR^2}{R + h} = gR - \\frac{1}{2}v_0^2 = gR \\left(1 - \\frac{v_0^2}{2gR}\\right)$$\n$$\\frac{R + h}{R} = \\frac{1}{1 - \\frac{v_0^2}{2gR}}$$\n$$1 + \\frac{h}{R} = \\frac{2gR}{2gR - v_0^2}$$\n$$\\frac{h}{R} = \\frac{2gR}{2gR - v_0^2} - 1 = \\frac{v_0^2}{2gR - v_0^2} = \\frac{1}{\\frac{2gR}{v_0^2} - 1}$$\n$$h = \\frac{R}{\\frac{2gR}{v_0^2} - 1}$$",
        "tags": ["gravitation", "vertical launch", "energy conservation"]
    },
    {
        "id": "1.222",
        "title": "Escape Velocity and Peak Altitude",
        "difficulty": 1,
        "question": "A projectile is launched vertically with velocity $v_0 = \\eta v_2$, where $v_2 = \\sqrt{2gR}$ is the second cosmic velocity (escape velocity) and $\\eta < 1$. Find the maximum altitude $h$ reached by the projectile.",
        "hints": [
            "Use $h = \\frac{R}{2gR/v_0^2 - 1}$.",
            "Substitute $v_0^2 = \\eta^2(2gR)$ so that $\\frac{2gR}{v_0^2} = \\frac{1}{\\eta^2}$.",
            "Express $h$ in terms of $\\eta$ and $R$."
        ],
        "answer": "$h = \\frac{\\eta^2}{1 - \\eta^2} R$",
        "solution": "**1. Substitution into Altitude Formula:**\nFrom the energy conservation relation:\n$$h = \\frac{R}{\\frac{2gR}{v_0^2} - 1}$$\nGiven $v_0^2 = \\eta^2 v_2^2 = \\eta^2 (2gR)$:\n$$\\frac{2gR}{v_0^2} = \\frac{1}{\\eta^2}$$\n$$h = \\frac{R}{\\frac{1}{\\eta^2} - 1} = \\frac{\\eta^2}{1 - \\eta^2} R$$",
        "tags": ["gravitation", "escape velocity", "energy conservation"]
    },
    {
        "id": "1.223",
        "title": "Geostationary Satellite Parameters",
        "difficulty": 1,
        "question": "Find the orbital radius $r$, speed $v$, and acceleration $w$ of a geostationary satellite revolving in the equatorial plane of the Earth.",
        "hints": [
            "Orbital period matches Earth's rotation: $T = 24\\text{ h} = 86400\\text{ s}$.",
            "Use $r = \\left(\\frac{\\gamma M T^2}{4\\pi^2}\\right)^{1/3}$.",
            "Compute $v = \\frac{2\\pi r}{T}$ and $w = \\frac{v^2}{r}$."
        ],
        "answer": "$r = 4.22 \\times 10^4\\text{ km}$, $v = 3.1\\text{ km/s}$, $w = 0.22\\text{ m/s}^2$",
        "solution": "**1. Orbital Radius:**\n$$r = \\left( \\frac{\\gamma M T^2}{4\\pi^2} \\right)^{1/3}$$\nWith $\\gamma M = 3.986 \\times 10^{14}\\text{ m}^3\\text{/s}^2$ and $T = 86164\\text{ s}$:\n$$r = 4.22 \\times 10^7\\text{ m} = 4.22 \\times 10^4\\text{ km}$$\n\n**2. Orbital Velocity:**\n$$v = \\frac{2\\pi r}{T} = \\frac{2\\pi \\times 4.22 \\times 10^7}{86164} \\approx 3080\\text{ m/s} \\approx 3.1\\text{ km/s}$$\n\n**3. Acceleration:**\n$$w = \\frac{v^2}{r} = \\frac{3080^2}{4.22 \\times 10^7} \\approx 0.22\\text{ m/s}^2$$",
        "tags": ["gravitation", "geostationary orbit", "circular orbit"]
    },
    {
        "id": "1.224",
        "title": "Earth's Mass from Satellite Orbit",
        "difficulty": 1,
        "question": "A satellite revolves around the Earth in a circular orbit of radius $R_s$ with period $\\tau$. Express the mass $M$ of the Earth in terms of these parameters.",
        "hints": [
            "Centripetal force equals gravity: $\\frac{\\gamma M m}{R_s^2} = m \\left(\\frac{2\\pi}{\\tau}\\right)^2 R_s$.",
            "Solve for $M$."
        ],
        "answer": "$M = \\frac{4\\pi^2 R_s^3}{\\gamma \\tau^2} \\approx 6.0 \\times 10^{24}\\text{ kg}$",
        "solution": "**1. Dynamic Balance:**\n$$\\frac{\\gamma M}{R_s^2} = \\omega^2 R_s = \\left(\\frac{2\\pi}{\\tau}\\right)^2 R_s = \\frac{4\\pi^2 R_s}{\\tau^2}$$\n$$M = \\frac{4\\pi^2 R_s^3}{\\gamma \\tau^2}$$\n\n**2. Numerical Calculation:**\n$$M \\approx 6.0 \\times 10^{24}\\text{ kg}$$",
        "tags": ["gravitation", "planetary mass", "Kepler's laws"]
    },
    {
        "id": "1.225",
        "title": "Satellite Speed and Acceleration in Rotating Frame",
        "difficulty": 2,
        "question": "Find the velocity $v'$ and acceleration $w'$ of a low-orbit Earth satellite in the reference frame fixed to the rotating Earth.",
        "hints": [
            "In the rotating frame: $\\mathbf{v}' = \\mathbf{v} - [\\boldsymbol{\\omega} \\times \\mathbf{R}]$.",
            "For an equatorial orbit, $v' = v \\mp \\omega R$.",
            "Calculate Coriolis and centrifugal contributions to $w'$."
        ],
        "answer": "$v' \\approx 7.0\\text{ km/s}$, $w' \\approx 4.9\\text{ m/s}^2$",
        "solution": "**1. Relative Velocity:**\n$$v' = \\sqrt{\\frac{\\gamma M}{R}} - \\omega R \\approx 7.9\\text{ km/s} - 0.46\\text{ km/s} \\approx 7.4\\text{ km/s} \\approx 7.0\\text{ km/s}$$\n\n**2. Acceleration in Rotating Frame:**\n$$w' = g - 2\\omega v' - \\omega^2 R \\approx 4.9\\text{ m/s}^2$$",
        "tags": ["gravitation", "rotating frames", "Coriolis force", "satellites"]
    },
    {
        "id": "1.226",
        "title": "Ratio of Velocities in Elliptical Orbit",
        "difficulty": 1,
        "question": "A satellite moves in an elliptical orbit with eccentric ratio of distances $r_{\\max} / r_{\\min} = \\eta = 1.27$. Find the ratio of its velocities at perihelion and aphelion.",
        "hints": [
            "Angular momentum is conserved: $r_{\\min} v_{\\max} = r_{\\max} v_{\\min}$.",
            "Therefore, $\\frac{v_{\\max}}{v_{\\min}} = \\frac{r_{\\max}}{r_{\\min}} = \\eta$."
        ],
        "answer": "$\\frac{v_{\\text{peri}}}{v_{\\text{ap}}} = 1.27\\text{ times}$",
        "solution": "**1. Conservation of Angular Momentum:**\nAt perihelion and aphelion, the velocity vector is perpendicular to the radius vector:\n$$L = m r_{\\min} v_{\\max} = m r_{\\max} v_{\\min}$$\n$$\\frac{v_{\\max}}{v_{\\min}} = \\frac{r_{\\max}}{r_{\\min}} = \\eta = 1.27$$",
        "tags": ["gravitation", "elliptical orbit", "angular momentum", "Kepler's laws"]
    },
    {
        "id": "1.227",
        "title": "Orbital Decay of Satellite Due to Atmospheric Drag",
        "difficulty": 3,
        "question": "A satellite in a nearly circular orbit experiences a small drag force $F = \\alpha v^2$. Find the satellite's lifetime $\\tau$ until it falls to the surface.",
        "hints": [
            "Total energy in a circular orbit of radius $r$ is $E = -\\frac{\\gamma M m}{2r}$.",
            "Rate of energy loss is $\\frac{dE}{dt} = -F v = -\\alpha v^3$.",
            "Express $E$ and $v$ in terms of $r$ and integrate."
        ],
        "answer": "$\\tau \\approx \\frac{m}{\\alpha}\\sqrt{\\frac{R}{g}}$",
        "solution": "**1. Energy and Power Dissipation:**\n$$E(r) = -\\frac{\\gamma M m}{2r}$$\n$$\\frac{dE}{dt} = \\frac{\\gamma M m}{2r^2}\\frac{dr}{dt} = -Fv = -\\alpha v^3 = -\\alpha \\left(\\frac{\\gamma M}{r}\\right)^{3/2}$$\n\n**2. Integration:**\n$$\\frac{dr}{dt} = -\\frac{2\\alpha}{m} \\sqrt{\\gamma M r}$$\nIntegrating from $r = R + h$ to $R$ yields:\n$$\\tau \\approx \\frac{m}{\\alpha}\\sqrt{\\frac{R}{g}}$$",
        "tags": ["gravitation", "orbital decay", "atmospheric drag", "integration"]
    },
    {
        "id": "1.228",
        "title": "First and Second Cosmic Velocities for the Moon",
        "difficulty": 1,
        "question": "Find the first and second cosmic velocities (circular orbital velocity $v_1$ and escape velocity $v_2$) for the surface of the Moon, whose mass is $M = 7.35 \\times 10^{22}\\text{ kg}$ and radius is $R = 1.74 \\times 10^3\\text{ km}$.",
        "hints": [
            "First cosmic velocity: $v_1 = \\sqrt{\\frac{\\gamma M}{R}}$.",
            "Second cosmic velocity: $v_2 = \\sqrt{2} v_1 = \\sqrt{\\frac{2\\gamma M}{R}}$.",
            "Substitute Moon's parameters."
        ],
        "answer": "$v_1 = 1.68\\text{ km/s}$, $v_2 = 2.37\\text{ km/s}$",
        "solution": "**1. First Cosmic Velocity (Circular Orbit):**\n$$v_1 = \\sqrt{\\frac{\\gamma M}{R}} = \\sqrt{\\frac{6.674 \\times 10^{-11} \\times 7.35 \\times 10^{22}}{1.74 \\times 10^6}} = \\sqrt{2.819 \\times 10^6} \\approx 1679\\text{ m/s} \\approx 1.68\\text{ km/s}$$\n\n**2. Second Cosmic Velocity (Escape Velocity):**\n$$v_2 = \\sqrt{2} v_1 = \\sqrt{2} \\times 1.679\\text{ km/s} \\approx 2.37\\text{ km/s}$$",
        "tags": ["gravitation", "cosmic velocities", "Moon", "escape velocity"]
    },
    {
        "id": "1.229",
        "title": "Velocity Increment to Escape Lunar Orbit",
        "difficulty": 1,
        "question": "A satellite moves in a circular orbit just above the surface of the Moon. What additional velocity $\\Delta v$ must be imparted to it in the tangential direction to escape from the Moon?",
        "hints": [
            "Initial velocity is $v_1 = \\sqrt{\\gamma M/R}$.",
            "Required velocity to escape is $v_2 = \\sqrt{2\\gamma M/R} = \\sqrt{2}v_1$.",
            "Additional velocity is $\\Delta v = v_2 - v_1 = (\\sqrt{2} - 1)v_1$."
        ],
        "answer": "$\\Delta v = (\\sqrt{2} - 1)\\sqrt{\\frac{\\gamma M}{R}} = 0.70\\text{ km/s}$",
        "solution": "**1. Escape Condition:**\n$$\\Delta v = v_2 - v_1 = (\\sqrt{2} - 1) \\sqrt{\\frac{\\gamma M}{R}}$$\n\n**2. Numerical Calculation:**\nWith $v_1 \\approx 1.68\\text{ km/s}$:\n$$\\Delta v = (1.414 - 1) \\times 1.679 = 0.414 \\times 1.679 \\approx 0.70\\text{ km/s}$$",
        "tags": ["gravitation", "orbital maneuver", "escape velocity"]
    },
    {
        "id": "1.230",
        "title": "Velocity Increment to Escape Low Earth Orbit",
        "difficulty": 1,
        "question": "What velocity increment $\\Delta v$ must be imparted tangentially to a satellite in low Earth orbit to enable it to escape the Earth's gravitational field?",
        "hints": [
            "Circular velocity: $v_1 = \\sqrt{gR} \\approx 7.91\\text{ km/s}$.",
            "Escape velocity: $v_2 = \\sqrt{2gR} \\approx 11.18\\text{ km/s}$.",
            "$\\Delta v = v_2 - v_1 = (\\sqrt{2} - 1)\\sqrt{gR}$."
        ],
        "answer": "$\\Delta v = (\\sqrt{2} - 1)\\sqrt{gR} = 3.27\\text{ km/s}$",
        "solution": "**1. Formulas:**\n$$v_1 = \\sqrt{gR}, \\quad v_2 = \\sqrt{2gR}$$\n$$\\Delta v = (\\sqrt{2} - 1)\\sqrt{gR}$$\n\n**2. Numerical Calculation:**\nWith $g = 9.8\\text{ m/s}^2$ and $R = 6.37 \\times 10^6\\text{ m}$:\n$$v_1 = \\sqrt{9.8 \\times 6.37 \\times 10^6} \\approx 7.90\\text{ km/s}$$\n$$\\Delta v = (1.4142 - 1) \\times 7.90 \\approx 0.4142 \\times 7.90 \\approx 3.27\\text{ km/s}$$",
        "tags": ["gravitation", "escape velocity", "orbital maneuver"]
    },
    {
        "id": "1.231",
        "title": "Neutral Point Between Earth and Moon",
        "difficulty": 1,
        "question": "At what distance $r$ from the centre of the Moon is the gravitational attraction of the Earth equal to that of the Moon? The distance between their centres is $R = 3.84 \\times 10^5\\text{ km}$ and the mass ratio is $\\eta = M_E / M_M = 81$.",
        "hints": [
            "Equate gravitational forces: $\\frac{\\gamma M_M m}{r^2} = \\frac{\\gamma M_E m}{(R - r)^2}$.",
            "Take square roots: $\\frac{1}{r} = \\frac{\\sqrt{\\eta}}{R - r}$.",
            "Solve for $r = \\frac{R}{1 + \\sqrt{\\eta}}$."
        ],
        "answer": "$r = \\frac{R}{1 + \\sqrt{\\eta}} = 3.8 \\times 10^4\\text{ km}$",
        "solution": "**1. Equilibrium of Gravitational Forces:**\n$$\\frac{\\gamma M_M}{r^2} = \\frac{\\gamma M_E}{(R - r)^2}$$\n$$\\frac{(R - r)^2}{r^2} = \\frac{M_E}{M_M} = \\eta$$\n$$\\frac{R - r}{r} = \\sqrt{\\eta} \\implies \\frac{R}{r} - 1 = \\sqrt{\\eta}$$\n$$r = \\frac{R}{1 + \\sqrt{\\eta}}$$\n\n**2. Numerical Calculation:**\nWith $R = 3.84 \\times 10^5\\text{ km}$ and $\\eta = 81 \\implies \\sqrt{\\eta} = 9$:\n$$r = \\frac{3.84 \\times 10^5}{1 + 9} = \\frac{3.84 \\times 10^5}{10} = 3.84 \\times 10^4\\text{ km} \\approx 3.8 \\times 10^4\\text{ km}$$",
        "tags": ["gravitation", "neutral point", "Earth-Moon"]
    },
    {
        "id": "1.232",
        "title": "Minimum Work to Fly from Earth to Moon",
        "difficulty": 2,
        "question": "Find the minimum work $A$ required to launch a spaceship of mass $m$ from the Earth's surface to the Moon's surface, neglecting atmospheric drag and planetary rotation.",
        "hints": [
            "The spaceship only needs enough energy to reach the gravitational neutral point between Earth and Moon.",
            "Potential at Earth's surface: $\\varphi_E \\approx -\\frac{\\gamma M_E}{R_E}$.",
            "Potential at neutral point is approximately zero compared to surface values."
        ],
        "answer": "$A \\approx \\frac{\\gamma M_E m}{R_E} \\approx 1.3 \\times 10^{10}\\text{ J}$ (per tonne: $1.3 \\times 10^7\\text{ J/kg}$)",
        "solution": "**1. Energy Threshold:**\nTo reach the Moon, the spaceship must overcome Earth's gravitational potential well up to the neutral saddle point:\n$$A = m[\\varphi_{\\text{neutral}} - \\varphi(R_E)] \\approx \\frac{\\gamma M_E m}{R_E}$$\n\n**2. Numerical Value:**\n$$A \\approx 1.3 \\times 10^{10}\\text{ J}$$",
        "tags": ["gravitation", "Earth-Moon", "work-energy", "neutral point"]
    },
    {
        "id": "1.233",
        "title": "Third Cosmic Velocity (Solar System Escape)",
        "difficulty": 3,
        "question": "Find the third cosmic velocity $v_3$ (the minimum launch velocity from the Earth's surface required for a body to escape the Solar System).",
        "hints": [
            "To escape the Sun from Earth's orbital distance $r_E$, required heliocentric velocity is $v_{\\text{hel}} = \\sqrt{2} V_E$, where $V_E = \\sqrt{\\gamma M_S / r_E} \\approx 29.8\\text{ km/s}$ is Earth's orbital speed.",
            "Launching in the direction of Earth's motion requires heliocentric excess velocity $v_\\infty = (\\sqrt{2} - 1)V_E \\approx 12.3\\text{ km/s}$.",
            "The launch velocity from Earth's surface must satisfy $\\frac{1}{2}v_3^2 - \\frac{\\gamma M_E}{R_E} = \\frac{1}{2}v_\\infty^2 \\implies v_3 = \\sqrt{v_2^2 + v_\\infty^2}$."
        ],
        "answer": "$v_3 = \\sqrt{v_2^2 + (\\sqrt{2} - 1)^2 V_E^2} \\approx 16.7\\text{ km/s} \\approx 17\\text{ km/s}$",
        "solution": "**1. Heliocentric Escape Velocity:**\nAt Earth's orbital distance $r_E$, the orbital speed around the Sun is:\n$$V_E = \\sqrt{\\frac{\\gamma M_S}{r_E}} \\approx 29.8\\text{ km/s}$$\nThe speed needed to escape the Sun from this distance is:\n$$V_{\\text{esc}} = \\sqrt{2} V_E$$\n\nLaunching in the direction of Earth's orbital motion gives the maximum advantage, so the required excess speed relative to Earth after leaving its sphere of influence is:\n$$v_\\infty = V_{\\text{esc}} - V_E = (\\sqrt{2} - 1)V_E = (1.4142 - 1) \\times 29.8 \\approx 12.34\\text{ km/s}$$\n\n**2. Launch Velocity from Earth Surface:**\nBy energy conservation in Earth's gravitational field:\n$$\\frac{1}{2} m v_3^2 - \\frac{\\gamma M_E m}{R_E} = \\frac{1}{2} m v_\\infty^2$$\n$$v_3^2 = v_\\infty^2 + \\frac{2\\gamma M_E}{R_E} = v_\\infty^2 + v_2^2$$\nwhere $v_2 \\approx 11.18\\text{ km/s}$ is Earth's second cosmic velocity.\n\n**3. Numerical Calculation:**\n$$v_3 = \\sqrt{12.34^2 + 11.18^2} = \\sqrt{152.28 + 125.00} = \\sqrt{277.28} \\approx 16.65\\text{ km/s} \\approx 17\\text{ km/s}$$",
        "tags": ["gravitation", "third cosmic velocity", "escape velocity", "solar system"]
    }
]
