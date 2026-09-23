"""
part4_ch4_1c.py
Curated problems 4.51 to 4.75 (25 problems) of Irodov Chapter 4.1:
Mechanical Oscillations (Part C).
"""

CH4_1C_CURATED = [
    {
        "id": "4.51",
        "title": "Shortest Oscillation Period of a Pivoted Uniform Rod",
        "difficulty": 2,
        "question": "A uniform rod of length $l$ performs small oscillations about a horizontal axis $OO'$ perpendicular to the rod and passing through one of its points. Find the distance $x$ between the center of inertia of the rod and the axis $OO'$ at which the oscillation period is shortest, and find the minimum period.",
        "hints": [
            "By the parallel axis theorem, the moment of inertia about an axis at distance $x$ from the center of mass is $I = m\\left(\\frac{l^2}{12} + x^2\\right)$.",
            "The reduced length of the physical pendulum is $l_{\\text{red}} = \\frac{I}{m x} = \\frac{l^2}{12x} + x$.",
            "Minimize $l_{\\text{red}}(x)$ with respect to $x$ using $\\frac{d l_{\\text{red}}}{dx} = 1 - \\frac{l^2}{12 x^2} = 0$, giving $x = \\frac{l}{2\\sqrt{3}}$ and $T_{\\min} = 2\\pi \\sqrt{\\frac{l}{g\\sqrt{3}}}$."
        ],
        "answer": "$x = \\frac{l}{2\\sqrt{3}}, \\quad T_{\\min} = 2\\pi \\sqrt{\\frac{l}{g\\sqrt{3}}}$",
        "solution": "**1. Moment of Inertia and Reduced Length:**\nFor a uniform rod of length $l$ and mass $m$, the moment of inertia about the center of inertia is $I_c = \\frac{1}{12} m l^2$.\nIf the horizontal suspension axis is at distance $x$ from the center of mass, the parallel-axis theorem gives:\n$$I = I_c + m x^2 = m \\left(\\frac{l^2}{12} + x^2\\right)$$\nThe period of small oscillations of this physical pendulum is:\n$$T = 2\\pi \\sqrt{\\frac{I}{m g x}} = 2\\pi \\sqrt{\\frac{l_{\\text{red}}}{g}}$$\nwhere the reduced length is:\n$$l_{\\text{red}}(x) = \\frac{I}{m x} = \\frac{l^2}{12x} + x$$\n\n**2. Minimizing the Period:**\nTo find the shortest period, we differentiate $l_{\\text{red}}$ with respect to $x$ and set the derivative to zero:\n$$\\frac{d l_{\\text{red}}}{dx} = -\\frac{l^2}{12 x^2} + 1 = 0 \\implies x^2 = \\frac{l^2}{12} \\implies x = \\frac{l}{\\sqrt{12}} = \\frac{l}{2\\sqrt{3}}$$\n\n**3. Shortest Oscillation Period:**\nSubstituting $x = \\frac{l}{2\\sqrt{3}}$ back into $l_{\\text{red}}$:\n$$l_{\\text{red, min}} = \\frac{l^2}{12 \\left(\\frac{l}{2\\sqrt{3}}\\right)} + \\frac{l}{2\\sqrt{3}} = \\frac{l}{2\\sqrt{3}} + \\frac{l}{2\\sqrt{3}} = \\frac{l}{\\sqrt{3}}$$\nThe minimum oscillation period is:\n$$T_{\\min} = 2\\pi \\sqrt{\\frac{l_{\\text{red, min}}}{g}} = 2\\pi \\sqrt{\\frac{l}{g\\sqrt{3}}}$$",
        "tags": ["physical pendulum", "reduced length", "period minimization", "parallel axis theorem"]
    },
    {
        "id": "4.52",
        "title": "Oscillations of an Equilateral Triangular Plate About Its Side",
        "difficulty": 2,
        "question": "A thin uniform plate shaped as an equilateral triangle with height $h$ performs small oscillations about a horizontal axis coinciding with one of its sides. Find the oscillation period and the reduced length of the given pendulum.",
        "hints": [
            "The center of mass of a uniform triangle is located at distance $l_c = h/3$ from the base side.",
            "Integrate strip elements parallel to the base to find the moment of inertia about the base: $I = \\frac{1}{6} m h^2$.",
            "Compute the reduced length $l_{\\text{red}} = \\frac{I}{m l_c} = \\frac{h^2/6}{h/3} = \\frac{h}{2}$ and period $T = 2\\pi \\sqrt{\\frac{l_{\\text{red}}}{g}} = \\pi \\sqrt{\\frac{2h}{g}}$."
        ],
        "answer": "$l_{\\text{red}} = \\frac{h}{2}, \\quad T = \\pi \\sqrt{\\frac{2h}{g}}$",
        "solution": "**1. Position of the Center of Mass:**\nTaking the axis of rotation along the base side ($y = 0$), the width of a horizontal strip at height $y$ is $b(y) = b_0 \\left(1 - \\frac{y}{h}\\right)$, where $b_0$ is the side length.\nThe distance of the center of mass from the base is:\n$$y_c = \\frac{\\int_0^h y b(y) dy}{\\int_0^h b(y) dy} = \\frac{h}{3}$$\n\n**2. Moment of Inertia About the Base:**\nThe mass of a strip of width $b(y)$ and thickness $dy$ is $dm = \\frac{2m}{b_0 h} b_0 \\left(1 - \\frac{y}{h}\\right) dy = \\frac{2m}{h} \\left(1 - \\frac{y}{h}\\right) dy$.\nThe moment of inertia about the base axis is:\n$$I = \\int y^2 dm = \\frac{2m}{h} \\int_0^h y^2 \\left(1 - \\frac{y}{h}\\right) dy = \\frac{2m}{h} \\left[ \\frac{h^3}{3} - \\frac{h^3}{4} \\right] = \\frac{2m}{h} \\cdot \\frac{h^3}{12} = \\frac{1}{6} m h^2$$\n\n**3. Reduced Length and Period:**\nThe reduced length of this physical pendulum is:\n$$l_{\\text{red}} = \\frac{I}{m y_c} = \\frac{\\frac{1}{6} m h^2}{m \\left(\\frac{h}{3}\\right)} = \\frac{3}{6} h = \\frac{h}{2}$$\nThe period of small oscillations is:\n$$T = 2\\pi \\sqrt{\\frac{l_{\\text{red}}}{g}} = 2\\pi \\sqrt{\\frac{h}{2g}} = \\pi \\sqrt{\\frac{2h}{g}}$$",
        "tags": ["physical pendulum", "triangular plate", "moment of inertia", "reduced length"]
    },
    {
        "id": "4.53",
        "title": "Oscillations of a Rod Hinged on a Rotating Horizontal Disc",
        "difficulty": 2,
        "question": "A smooth horizontal disc rotates about a vertical axis $O$ with a constant angular velocity $\\omega$. A thin uniform rod $AB$ of length $l$ performs small oscillations about a vertical axis $A$ fixed to the disc at a distance $a$ from the rotation axis of the disc. Find the frequency $\\omega_0$ of these oscillations.",
        "hints": [
            "In the rotating reference frame of the disc, centrifugal force acts on each element $dm$ of the rod directed radially away from axis $O$.",
            "For small angular deviation $\\theta$ from the radial line, the centrifugal force produces a restoring torque about pivot $A$: $\\tau = -\\int_0^l dm \\, \\omega^2 a \\sin\\theta \\, r \\approx -\\frac{1}{2} m \\omega^2 a l \\theta$.",
            "The moment of inertia of the rod about pivot $A$ is $I_A = \\frac{1}{3} m l^2$. Set $I_A \\ddot{\\theta} = \\tau$ to determine $\\omega_0$."
        ],
        "answer": "$\\omega_0 = \\omega \\sqrt{\\frac{3a}{2l}}$",
        "solution": "**1. Dynamics in the Rotating Frame:**\nIn the frame rotating with angular velocity $\\omega$, the centrifugal force on an element of mass $dm = \\frac{m}{l} dr$ located at distance $r$ from pivot $A$ is:\n$$d\\mathbf{F}_{\\text{cf}} = dm \\, \\omega^2 \\mathbf{R}$$\nwhere $\\mathbf{R}$ is the radius vector from the disc center $O$ to the element.\nFor small deflection $\\theta$ of the rod from the radial orientation $OA$, the component of centrifugal force perpendicular to the rod creating torque about $A$ is governed by the pivot offset $a$:\n$$d\\tau = -r (dm \\, \\omega^2 a \\sin\\theta) \\approx -\\frac{m}{l} \\omega^2 a \\theta \\, r dr$$\n\n**2. Net Restoring Torque:**\nIntegrating along the rod from $r = 0$ to $r = l$:\n$$\\tau_{\\text{net}} = -\\frac{m \\omega^2 a \\theta}{l} \\int_0^l r dr = -\\frac{m \\omega^2 a \\theta}{l} \\frac{l^2}{2} = -\\frac{1}{2} m \\omega^2 a l \\theta$$\n\n**3. Equation of Motion and Frequency:**\nThe moment of inertia of the uniform rod about its hinged end $A$ is:\n$$I_A = \\frac{1}{3} m l^2$$\nApplying the equation of rotational motion $I_A \\ddot{\\theta} = \\tau_{\\text{net}}$:\n$$\\frac{1}{3} m l^2 \\ddot{\\theta} + \\frac{1}{2} m \\omega^2 a l \\theta = 0$$\n$$\\ddot{\\theta} + \\left(\\frac{3a}{2l} \\omega^2\\right) \\theta = 0$$\nThe angular frequency of small oscillations is:\n$$\\omega_0 = \\sqrt{\\frac{3a}{2l} \\omega^2} = \\omega \\sqrt{\\frac{3a}{2l}}$$",
        "tags": ["rotating disc", "centrifugal restoring torque", "hinged rod", "small oscillations"]
    },
    {
        "id": "4.54",
        "title": "Frequency of Pulley-Spring-Mass Oscillating System",
        "difficulty": 2,
        "question": "Find the frequency of small oscillations of an arrangement consisting of a body of mass $m$ suspended from a thread that passes over a pulley of radius $R$ and moment of inertia $I$, with the other end of the thread attached to a fixed spring of stiffness $\\varkappa$. The thread does not slip on the pulley and there is no axle friction.",
        "hints": [
            "When the mass moves down by $x$, the pulley rotates by angle $\\theta = x/R$ and the spring extends by $x$.",
            "Express the total kinetic energy of the system as $T_k = \\frac{1}{2} m \\dot{x}^2 + \\frac{1}{2} I \\left(\\frac{\\dot{x}}{R}\\right)^2 = \\frac{1}{2} \\left(m + \\frac{I}{R^2}\\right) \\dot{x}^2$.",
            "The elastic potential energy about static equilibrium is $U = \\frac{1}{2} \\varkappa x^2$. Deduce $\\omega_0 = \\sqrt{\\frac{\\varkappa}{m + I/R^2}}$."
        ],
        "answer": "$\\omega_0 = \\sqrt{\\frac{\\varkappa}{m + I/R^2}}$",
        "solution": "**1. Kinetic and Potential Energy of the System:**\nLet $x$ be the vertical displacement of the mass $m$ from its static equilibrium position.\nBecause the thread does not slip on the pulley:\n- The rotation angle of the pulley is $\\theta = \\frac{x}{R}$, and angular speed is $\\dot{\\theta} = \\frac{\\dot{x}}{R}$.\n- The extension of the spring from equilibrium is also $x$.\nThe total kinetic energy of the system is:\n$$T_k = \\frac{1}{2} m \\dot{x}^2 + \\frac{1}{2} I \\dot{\\theta}^2 = \\frac{1}{2} m \\dot{x}^2 + \\frac{1}{2} I \\left(\\frac{\\dot{x}}{R}\\right)^2 = \\frac{1}{2} \\left(m + \\frac{I}{R^2}\\right) \\dot{x}^2$$\nThe effective inertia of the system is $m_{\\text{eff}} = m + \\frac{I}{R^2}$.\nThe potential energy relative to the equilibrium state (where gravity is canceled by initial spring stretch) is:\n$$U = \\frac{1}{2} \\varkappa x^2$$\n\n**2. Equation of Motion and Natural Frequency:**\nBy conservation of mechanical energy, $\\frac{d}{dt}(T_k + U) = 0$:\n$$\\left(m + \\frac{I}{R^2}\\right) \\dot{x} \\ddot{x} + \\varkappa x \\dot{x} = 0$$\nDividing by $\\dot{x}$:\n$$\\left(m + \\frac{I}{R^2}\\right) \\ddot{x} + \\varkappa x = 0 \\implies \\ddot{x} + \\frac{\\varkappa}{m + I/R^2} x = 0$$\nThe angular frequency of small oscillations is:\n$$\\omega_0 = \\sqrt{\\frac{\\varkappa}{m + I/R^2}}$$",
        "tags": ["pulley system", "effective mass", "spring oscillator", "energy method"]
    },
    {
        "id": "4.55",
        "title": "Oscillations of a Pulley Balanced by a Rim Point Mass",
        "difficulty": 3,
        "question": "A uniform cylindrical pulley of mass $M$ and radius $R$ can freely rotate about a horizontal axis $O$. The free end of a thread wound on the pulley carries a suspended deadweight $A$. At a certain equilibrium angle $\\alpha$ with the vertical, the weight $A$ counterbalances a point mass $m$ fixed at the rim of the pulley. Find the frequency of small oscillations of the arrangement.",
        "hints": [
            "In equilibrium, torque balance gives $m g R \\sin\\alpha = m_A g R \\implies m_A = m \\sin\\alpha$.",
            "When the pulley rotates by small angle $\\theta$ from equilibrium, the restoring torque is $\\tau = -m g R \\cos\\alpha \\, \\theta$.",
            "Compute total kinetic energy: $T_k = \\frac{1}{2} \\left(I_{\\text{pulley}} + m R^2 + m_A R^2\\right) \\dot{\\theta}^2$, where $I_{\\text{pulley}} = \\frac{1}{2} M R^2$. Find $\\omega_0$."
        ],
        "answer": "$\\omega_0 = \\sqrt{\\frac{mg \\cos\\alpha}{R\\left[\\frac{1}{2} M + m(1 + \\sin\\alpha)\\right]}} = \\sqrt{\\frac{2mg \\cos\\alpha}{R [M + 2m(1 + \\sin\\alpha)]}}$",
        "solution": "**1. Equilibrium Condition:**\nLet the point mass $m$ be located at angular position $\\alpha$ from the lowest point on the rim.\nThe torque exerted by mass $m$ about the horizontal axis $O$ is $m g R \\sin\\alpha$.\nThe hanging deadweight $A$ of mass $m_A$ exerts a constant torque $m_A g R$.\nIn equilibrium:\n$$m g R \\sin\\alpha = m_A g R \\implies m_A = m \\sin\\alpha$$\n\n**2. Restoring Torque for Small Angular Displacement:**\nWhen the pulley is displaced by a small angle $\\theta$ from equilibrium, the angular position of mass $m$ becomes $\\alpha + \\theta$.\nThe net torque about $O$ is:\n$$\\tau = m_A g R - m g R \\sin(\\alpha + \\theta) = m g R \\sin\\alpha - m g R (\\sin\\alpha \\cos\\theta + \\cos\\alpha \\sin\\theta)$$\nFor small $\\theta$, $\\cos\\theta \\approx 1$ and $\\sin\\theta \\approx \\theta$:\n$$\\tau \\approx -m g R \\cos\\alpha \\, \\theta$$\n\n**3. Total Moment of Inertia:**\nThe kinetic energy of the rotating and translating components is:\n- Uniform pulley ($I_p = \\frac{1}{2} M R^2$): $T_p = \\frac{1}{2} I_p \\dot{\\theta}^2 = \\frac{1}{4} M R^2 \\dot{\\theta}^2$\n- Rim point mass $m$: $T_m = \\frac{1}{2} m (R\\dot{\\theta})^2 = \\frac{1}{2} m R^2 \\dot{\\theta}^2$\n- Suspended mass $m_A$: $T_A = \\frac{1}{2} m_A (R\\dot{\\theta})^2 = \\frac{1}{2} (m \\sin\\alpha) R^2 \\dot{\\theta}^2$\nThe total effective moment of inertia about $O$ is:\n$$I_{\\text{eff}} = \\frac{1}{2} M R^2 + m R^2 + m R^2 \\sin\\alpha = R^2 \\left[ \\frac{1}{2} M + m(1 + \\sin\\alpha) \\right]$$\n\n**4. Oscillation Frequency:**\nThe equation of motion is $I_{\\text{eff}} \\ddot{\\theta} + m g R \\cos\\alpha \\, \\theta = 0$, giving:\n$$\\omega_0^2 = \\frac{m g R \\cos\\alpha}{I_{\\text{eff}}} = \\frac{mg \\cos\\alpha}{R\\left[ \\frac{1}{2} M + m(1 + \\sin\\alpha) \\right]} = \\frac{2mg \\cos\\alpha}{R [M + 2m(1 + \\sin\\alpha)]}$$\n$$\\omega_0 = \\sqrt{\\frac{mg \\cos\\alpha}{R\\left[\\frac{1}{2} M + m(1 + \\sin\\alpha)\\right]}}$$",
        "tags": ["pulley dynamics", "equilibrium", "restoring torque", "effective moment of inertia"]
    },
    {
        "id": "4.56",
        "title": "Period of a Solid Cylinder Rolling Inside a Cylindrical Surface",
        "difficulty": 2,
        "question": "A solid uniform cylinder of radius $r$ rolls without sliding along the inside concave surface of a cylinder of radius $R$, performing small oscillations about the lowest equilibrium position. Find the period of these oscillations.",
        "hints": [
            "The center of the small cylinder moves along a circular arc of radius $R - r$.",
            "Express the kinetic energy of rolling without slipping: $T_k = \\frac{1}{2} m v_c^2 + \\frac{1}{2} I_c \\omega_{\\text{rot}}^2 = \\frac{3}{4} m (R - r)^2 \\dot{\\theta}^2$.",
            "The potential energy for small angular displacement $\\theta$ is $U = m g (R - r)(1 - \\cos\\theta) \\approx \\frac{1}{2} m g (R - r) \\theta^2$. Find period $T = 2\\pi \\sqrt{\\frac{3(R - r)}{2g}}$."
        ],
        "answer": "$T = 2\\pi \\sqrt{\\frac{3(R - r)}{2g}}$",
        "solution": "**1. Kinematics of Rolling Without Slipping:**\nLet $\\theta$ be the angular displacement of the center of the rolling cylinder of radius $r$ from the vertical.\nThe distance from the center of curvature of the large cylinder (radius $R$) to the center of the rolling cylinder is $R - r$.\nThe speed of the cylinder's center of mass is:\n$$v_c = (R - r) \\dot{\\theta}$$\nBy the condition of rolling without sliding, the instantaneous axis of rotation is the point of contact between the cylinders.\nThe moment of inertia about the instantaneous axis of contact is:\n$$I = I_c + m r^2 = \\frac{1}{2} m r^2 + m r^2 = \\frac{3}{2} m r^2$$\nSince $v_c = r \\omega_{\\text{rot}}$, the rotational angular speed is $\\omega_{\\text{rot}} = \\frac{R - r}{r} \\dot{\\theta}$.\n\n**2. Mechanical Energy:**\nThe total kinetic energy is:\n$$T_k = \\frac{1}{2} I \\omega_{\\text{rot}}^2 = \\frac{1}{2} \\left(\\frac{3}{2} m r^2\\right) \\left(\\frac{R - r}{r} \\dot{\\theta}\\right)^2 = \\frac{3}{4} m (R - r)^2 \\dot{\\theta}^2$$\nThe gravitational potential energy for small deflection $\\theta$ is:\n$$U(\\theta) = m g (R - r) (1 - \\cos\\theta) \\approx \\frac{1}{2} m g (R - r) \\theta^2$$\n\n**3. Equation of Motion and Period:**\nUsing energy conservation $\\frac{d}{dt}(T_k + U) = 0$:\n$$\\frac{3}{2} m (R - r)^2 \\dot{\\theta} \\ddot{\\theta} + m g (R - r) \\theta \\dot{\\theta} = 0$$\n$$\\ddot{\\theta} + \\frac{2g}{3(R - r)} \\theta = 0$$\nThe angular frequency is $\\omega = \\sqrt{\\frac{2g}{3(R - r)}}$, and the period is:\n$$T = \\frac{2\\pi}{\\omega} = 2\\pi \\sqrt{\\frac{3(R - r)}{2g}}$$",
        "tags": ["rolling without slipping", "concave surface", "effective inertia", "period of oscillation"]
    },
    {
        "id": "4.57",
        "title": "Oscillation Period of a Rolling Cylinder Attached to Springs",
        "difficulty": 2,
        "question": "A solid uniform cylinder of mass $m$ performs small horizontal oscillations rolling without slipping on a horizontal surface under the action of two springs attached to its axle, whose combined stiffness is equal to $\\varkappa$. Find the period of these oscillations.",
        "hints": [
            "For rolling without slipping on a flat surface, the speed of the axle is $v$ and the rotational speed is $\\omega = v/r$.",
            "The total kinetic energy is $T_k = \\frac{1}{2} m v^2 + \\frac{1}{2} I_c \\omega^2 = \\frac{1}{2} m v^2 + \\frac{1}{4} m v^2 = \\frac{3}{4} m v^2$.",
            "The potential energy of the springs is $U = \\frac{1}{2} \\varkappa x^2$. Show that $T = 2\\pi \\sqrt{\\frac{3m}{2\\varkappa}} = \\pi \\sqrt{\\frac{6m}{\\varkappa}}$."
        ],
        "answer": "$T = \\pi \\sqrt{\\frac{6m}{\\varkappa}} = 2\\pi \\sqrt{\\frac{3m}{2\\varkappa}}$",
        "solution": "**1. Kinetic Energy of Pure Rolling:**\nLet $x$ be the displacement of the cylinder's axle from the equilibrium position.\nThe velocity of the center of mass is $v = \\dot{x}$.\nSince the cylinder rolls without slipping, its angular velocity is $\\omega = \\frac{v}{r} = \\frac{\\dot{x}}{r}$.\nThe moment of inertia of a solid cylinder about its central axis is $I_c = \\frac{1}{2} m r^2$.\nThe total kinetic energy is:\n$$T_k = \\frac{1}{2} m v^2 + \\frac{1}{2} I_c \\omega^2 = \\frac{1}{2} m \\dot{x}^2 + \\frac{1}{2} \\left(\\frac{1}{2} m r^2\\right) \\left(\\frac{\\dot{x}}{r}\\right)^2 = \\frac{3}{4} m \\dot{x}^2$$\nThe effective mass of the rolling cylinder is $m_{\\text{eff}} = \\frac{3}{2} m$.\n\n**2. Potential Energy and Period:**\nThe potential energy of the springs attached to the axle is:\n$$U = \\frac{1}{2} \\varkappa x^2$$\nConserving total mechanical energy $E = T_k + U = \\text{const}$:\n$$\\frac{3}{2} m \\dot{x} \\ddot{x} + \\varkappa x \\dot{x} = 0 \\implies \\ddot{x} + \\frac{2\\varkappa}{3m} x = 0$$\nThe angular frequency of oscillation is:\n$$\\omega_0 = \\sqrt{\\frac{2\\varkappa}{3m}}$$\nThe oscillation period is:\n$$T = \\frac{2\\pi}{\\omega_0} = 2\\pi \\sqrt{\\frac{3m}{2\\varkappa}} = \\pi \\sqrt{\\frac{6m}{\\varkappa}}$$",
        "tags": ["rolling cylinder", "spring-mass system", "effective mass", "oscillation period"]
    },
    {
        "id": "4.58",
        "title": "Oscillations of Two Cubes Interconnected by a Spring",
        "difficulty": 2,
        "question": "Two cubes with masses $m_1$ and $m_2$ are interconnected by a weightless spring of stiffness $\\varkappa$ and placed on a smooth horizontal surface. The cubes are shifted in opposite directions along the spring axis and released. Find the angular frequency of the resulting mutual oscillations.",
        "hints": [
            "In the absence of external horizontal forces, the center of mass of the system remains at rest.",
            "The relative coordinate $\\xi = x_2 - x_1$ describes the change in length of the spring.",
            "Write the equation of motion for $\\xi$: $\\ddot{\\xi} + \\frac{\\varkappa}{\\mu} \\xi = 0$, where $\\mu = \\frac{m_1 m_2}{m_1 + m_2}$ is the reduced mass."
        ],
        "answer": "$\\omega_0 = \\sqrt{\\frac{\\varkappa}{\\mu}}$, where $\\mu = \\frac{m_1 m_2}{m_1 + m_2}$",
        "solution": "**1. Equations of Motion for the Two Bodies:**\nLet $x_1$ and $x_2$ be the coordinates of cubes $m_1$ and $m_2$ along the horizontal line of the spring.\nLet $l_0$ be the unstretched length of the spring. The force exerted by the spring on body 1 is $+\\varkappa (x_2 - x_1 - l_0)$ and on body 2 is $-\\varkappa (x_2 - x_1 - l_0)$.\nNewton's second law for each cube gives:\n$$m_1 \\ddot{x}_1 = \\varkappa (x_2 - x_1 - l_0)$$\n$$m_2 \\ddot{x}_2 = -\\varkappa (x_2 - x_1 - l_0)$$\n\n**2. Relative Motion and Reduced Mass:**\nDefine the relative displacement from equilibrium as $\\xi = (x_2 - x_1) - l_0$.\nDividing the equations by the respective masses and subtracting:\n$$\\ddot{\\xi} = \\ddot{x}_2 - \\ddot{x}_1 = -\\frac{\\varkappa}{m_2} \\xi - \\frac{\\varkappa}{m_1} \\xi = -\\varkappa \\left(\\frac{1}{m_1} + \\frac{1}{m_2}\\right) \\xi = -\\frac{\\varkappa}{\\mu} \\xi$$\nwhere $\\mu = \\frac{m_1 m_2}{m_1 + m_2}$ is the reduced mass of the two-body system.\n\n**3. Oscillation Frequency:**\n$$\\ddot{\\xi} + \\omega_0^2 \\xi = 0 \\implies \\omega_0 = \\sqrt{\\frac{\\varkappa}{\\mu}} = \\sqrt{\\frac{\\varkappa (m_1 + m_2)}{m_1 m_2}}$$",
        "tags": ["two-body oscillator", "reduced mass", "internal oscillations", "spring-mass system"]
    },
    {
        "id": "4.59",
        "title": "Oscillation Parameters After Impulse Imparted to Connected Balls",
        "difficulty": 2,
        "question": "Two balls with masses $m_1 = 1.0\\text{ kg}$ and $m_2 = 2.0\\text{ kg}$ slide along a thin smooth horizontal rod. The balls are interconnected by a light spring of stiffness $\\varkappa = 24\\text{ N/m}$. Initially the system is at rest. Then ball 1 is imparted an initial velocity $v_1 = 0.30\\text{ m/s}$ along the rod. Find:\n(a) the frequency of mutual oscillations;\n(b) the energy and amplitude of these oscillations.",
        "hints": [
            "The oscillation frequency depends solely on the spring stiffness and reduced mass: $\\omega = \\sqrt{\\varkappa / \\mu}$, where $\\mu = \\frac{m_1 m_2}{m_1 + m_2}$.",
            "In the center-of-mass reference frame, the center of mass moves with constant speed $v_c = \\frac{m_1 v_1}{m_1 + m_2}$, and the relative initial velocity between the balls is $v_{\\text{rel}} = v_1$.",
            "The energy of internal oscillation is $E = \\frac{1}{2} \\mu v_1^2$, and the amplitude is $a = \\frac{v_1}{\\omega}$."
        ],
        "answer": "(a) $\\omega = \\sqrt{\\frac{\\varkappa}{\\mu}} = 6\\text{ s}^{-1}$; (b) $E = \\frac{1}{2} \\mu v_1^2 = 30\\text{ mJ}, \\quad a = \\frac{v_1}{\\omega} = 5\\text{ cm}$",
        "solution": "**(a) Frequency of Mutual Oscillations:**\nThe reduced mass of the two balls is:\n$$\\mu = \\frac{m_1 m_2}{m_1 + m_2} = \\frac{(1.0\\text{ kg})(2.0\\text{ kg})}{1.0 + 2.0} = \\frac{2.0}{3.0} = \\frac{2}{3}\\text{ kg}$$\nThe frequency of mutual oscillations is:\n$$\\omega = \\sqrt{\\frac{\\varkappa}{\\mu}} = \\sqrt{\\frac{24\\text{ N/m}}{2/3\\text{ kg}}} = \\sqrt{36} = 6.0\\text{ s}^{-1}$$\n\n**(b) Energy and Amplitude of Oscillations:**\nThe initial total kinetic energy of the system is:\n$$T_0 = \\frac{1}{2} m_1 v_1^2$$\nThe velocity of the center of mass is:\n$$v_c = \\frac{m_1 v_1}{m_1 + m_2}$$\nThe kinetic energy of translation of the center of mass is:\n$$T_c = \\frac{1}{2} (m_1 + m_2) v_c^2 = \\frac{1}{2} \\frac{m_1^2 v_1^2}{m_1 + m_2}$$\nBy Koenig's theorem, the internal oscillation energy is the energy in the CM frame:\n$$E = T_0 - T_c = \\frac{1}{2} \\mu v_1^2$$\nSubstituting $\\mu = \\frac{2}{3}\\text{ kg}$ and $v_1 = 0.30\\text{ m/s}$:\n$$E = \\frac{1}{2} \\left(\\frac{2}{3}\\right) (0.30)^2 = \\frac{1}{3} (0.090) = 0.030\\text{ J} = 30\\text{ mJ}$$\nThe oscillation energy is also related to the amplitude of relative displacement $a$ by:\n$$E = \\frac{1}{2} \\varkappa a^2 \\implies \\frac{1}{2} \\varkappa a^2 = \\frac{1}{2} \\mu v_1^2$$\n$$a = v_1 \\sqrt{\\frac{\\mu}{\\varkappa}} = \\frac{v_1}{\\omega} = \\frac{0.30\\text{ m/s}}{6.0\\text{ s}^{-1}} = 0.050\\text{ m} = 5.0\\text{ cm}$$",
        "tags": ["two-body oscillator", "center of mass frame", "oscillation energy", "amplitude"]
    },
    {
        "id": "4.60",
        "title": "Period of Torsional Oscillations of Two Discs on a Rod",
        "difficulty": 2,
        "question": "Find the period of small torsional oscillations of a system consisting of two discs with moments of inertia $I_1$ and $I_2$ attached to the ends of a thin rod of torsional stiffness $k$.",
        "hints": [
            "In the absence of external torques, the total angular momentum of the system is conserved.",
            "The discs rotate in opposite directions about the rod's axis during the fundamental torsional mode.",
            "Use the reduced moment of inertia $I' = \\frac{I_1 I_2}{I_1 + I_2}$ to find $T = 2\\pi \\sqrt{\\frac{I'}{k}}$."
        ],
        "answer": "$T = 2\\pi \\sqrt{\\frac{I'}{k}}$, where $I' = \\frac{I_1 I_2}{I_1 + I_2}$",
        "solution": "**1. Equations of Torsional Motion:**\nLet $\\varphi_1$ and $\\varphi_2$ be the angles of rotation of discs 1 and 2.\nThe twist of the rod is $\\Delta \\varphi = \\varphi_2 - \\varphi_1$, producing an elastic restoring torque of magnitude $N = k (\\varphi_2 - \\varphi_1)$.\nThe rotational equations of motion are:\n$$I_1 \\ddot{\\varphi}_1 = k (\\varphi_2 - \\varphi_1)$$\n$$I_2 \\ddot{\\varphi}_2 = -k (\\varphi_2 - \\varphi_1)$$\n\n**2. Relative Twist and Reduced Moment of Inertia:**\nSubtracting the first equation divided by $I_1$ from the second divided by $I_2$:\n$$\\frac{d^2}{dt^2}(\\varphi_2 - \\varphi_1) = -k \\left(\\frac{1}{I_1} + \\frac{1}{I_2}\\right)(\\varphi_2 - \\varphi_1) = -\\frac{k}{I'} (\\varphi_2 - \\varphi_1)$$\nwhere the reduced moment of inertia is:\n$$I' = \\frac{I_1 I_2}{I_1 + I_2}$$\n\n**3. Period of Oscillations:**\nThe differential equation for relative twist is harmonic with angular frequency:\n$$\\omega_0 = \\sqrt{\\frac{k}{I'}}$$\nThe oscillation period is:\n$$T = \\frac{2\\pi}{\\omega_0} = 2\\pi \\sqrt{\\frac{I'}{k}} = 2\\pi \\sqrt{\\frac{I_1 I_2}{k(I_1 + I_2)}}$$",
        "tags": ["torsional oscillations", "two discs", "reduced moment of inertia", "period"]
    },
    {
        "id": "4.61",
        "title": "Ratio of Longitudinal Vibrational Frequencies of Carbon Dioxide Molecule",
        "difficulty": 3,
        "question": "A model of a $\\text{CO}_2$ molecule consists of three collinear balls (an oxygen atom of mass $m_O$ on each side and a central carbon atom of mass $m_C$) interconnected by identical light springs. Find the ratio of the frequencies $\\omega_2 / \\omega_1$ of the two longitudinal vibrational modes of this linear triatomic molecule.",
        "hints": [
            "In mode 1 (symmetric stretch), the carbon atom remains motionless, while the two oxygen atoms move in opposite directions.",
            "In mode 2 (asymmetric stretch), the two oxygen atoms move in phase in one direction while the carbon atom moves in the opposite direction, preserving the center of mass.",
            "Show that $\\omega_1 = \\sqrt{\\frac{\\varkappa}{m_O}}$ and $\\omega_2 = \\sqrt{\\frac{\\varkappa}{m_O} \\left(1 + \\frac{2 m_O}{m_C}\\right)}$, yielding $\\frac{\\omega_2}{\\omega_1} = \\sqrt{1 + \\frac{2 m_O}{m_C}} \\approx 1.9$."
        ],
        "answer": "$\\frac{\\omega_2}{\\omega_1} = \\sqrt{1 + \\frac{2 m_O}{m_C}} \\approx 1.9$",
        "solution": "**1. Model Configuration:**\nLet the positions of the three atoms along the line be $x_1$ (oxygen, mass $m_O$), $x_2$ (carbon, mass $m_C$), and $x_3$ (oxygen, mass $m_O$), connected by springs of stiffness $\\varkappa$.\nNewton's equations for the displacements are:\n$$m_O \\ddot{x}_1 = \\varkappa (x_2 - x_1)$$\n$$m_C \\ddot{x}_2 = -\\varkappa (x_2 - x_1) + \\varkappa (x_3 - x_2)$$\n$$m_O \\ddot{x}_3 = -\\varkappa (x_3 - x_2)$$\n\n**2. Mode 1: Symmetric Stretch:**\nIn this mode, the central carbon atom remains fixed ($x_2 = 0$) and the two oxygen atoms move symmetrically in opposite directions ($x_1 = -x_3$):\n$$m_O \\ddot{x}_1 = -\\varkappa x_1 \\implies \\ddot{x}_1 + \\frac{\\varkappa}{m_O} x_1 = 0$$\nThe frequency of the symmetric mode is:\n$$\\omega_1 = \\sqrt{\\frac{\\varkappa}{m_O}}$$\n\n**3. Mode 2: Asymmetric Stretch:**\nIn this mode, the two oxygen atoms move with identical displacements in the same direction ($x_1 = x_3 = x$).\nTo keep the center of mass at rest:\n$$2 m_O x + m_C x_2 = 0 \\implies x_2 = -\\frac{2 m_O}{m_C} x$$\nThe restoring force on each oxygen atom is:\n$$F_1 = \\varkappa (x_2 - x) = \\varkappa \\left(-\\frac{2 m_O}{m_C} x - x\\right) = -\\varkappa \\left(1 + \\frac{2 m_O}{m_C}\\right) x$$\nThe equation of motion for $x$ is:\n$$m_O \\ddot{x} + \\varkappa \\left(1 + \\frac{2 m_O}{m_C}\\right) x = 0 \\implies \\omega_2^2 = \\frac{\\varkappa}{m_O} \\left(1 + \\frac{2 m_O}{m_C}\\right)$$\n$$\\omega_2 = \\sqrt{\\frac{\\varkappa}{m_O} \\left(1 + \\frac{2 m_O}{m_C}\\right)}$$\n\n**4. Frequency Ratio:**\n$$\\frac{\\omega_2}{\\omega_1} = \\sqrt{1 + \\frac{2 m_O}{m_C}}$$\nUsing atomic masses $m_O \\approx 16\\text{ u}$ and $m_C \\approx 12\\text{ u}$:\n$$\\frac{\\omega_2}{\\omega_1} = \\sqrt{1 + \\frac{2(16)}{12}} = \\sqrt{1 + \\frac{8}{3}} = \\sqrt{\\frac{11}{3}} \\approx \\sqrt{3.667} \\approx 1.91 \\approx 1.9$$",
        "tags": ["triatomic molecule", "normal modes", "symmetric stretch", "asymmetric stretch"]
    },
    {
        "id": "4.62",
        "title": "Frequency of Adiabatic Oscillations of a Piston in a Closed Cylinder",
        "difficulty": 2,
        "question": "In a cylinder closed at both ends and filled with an ideal gas, there is a frictionless piston of mass $m$ and cross-sectional area $S$. In equilibrium, the piston divides the cylinder into two equal parts, each of volume $V_0$ at pressure $p_0$. Find the frequency of small oscillations of the piston, assuming the gas process to be adiabatic with adiabatic exponent $\\gamma$.",
        "hints": [
            "For an adiabatic process, $p V^\\gamma = \\text{const}$, so $dp = -\\gamma \\frac{p}{V} dV$.",
            "When the piston is displaced by $x$, the volumes change by $dV_1 = +Sx$ and $dV_2 = -Sx$.",
            "The net restoring force is $F = (p_2 - p_1) S \\approx -2\\gamma \\frac{p_0 S^2}{V_0} x$. Find $\\omega = S \\sqrt{\\frac{2 \\gamma p_0}{m V_0}}$."
        ],
        "answer": "$\\omega = S \\sqrt{\\frac{2 \\gamma p_0}{m V_0}}$",
        "solution": "**1. Adiabatic Pressure Variations:**\nIn equilibrium, both compartments have volume $V_0$ and pressure $p_0$.\nWhen the piston is displaced by a small distance $x$:\n- Left compartment volume becomes $V_1 = V_0 + Sx$\n- Right compartment volume becomes $V_2 = V_0 - Sx$\nSince the gas undergoes an adiabatic process ($p V^\\gamma = \\text{const}$), taking the differential:\n$$dp = -\\gamma \\frac{p}{V} dV$$\nFor small $x$, the pressure changes in each compartment are:\n$$\\Delta p_1 = -\\gamma \\frac{p_0}{V_0} (Sx)$$\n$$\\Delta p_2 = -\\gamma \\frac{p_0}{V_0} (-Sx) = +\\gamma \\frac{p_0 S}{V_0} x$$\n\n**2. Net Restoring Force on the Piston:**\nThe net force acting on the piston is:\n$$F_x = (p_2 - p_1) S = (\\Delta p_2 - \\Delta p_1) S = \\left(2 \\gamma \\frac{p_0 S}{V_0} x\\right) (-1) = -\\frac{2 \\gamma p_0 S^2}{V_0} x$$\n\n**3. Frequency of Oscillation:**\nNewton's second law for the piston of mass $m$ is:\n$$m \\ddot{x} + \\frac{2 \\gamma p_0 S^2}{V_0} x = 0 \\implies \\ddot{x} + \\omega^2 x = 0$$\nThe angular frequency of small adiabatic oscillations is:\n$$\\omega = \\sqrt{\\frac{2 \\gamma p_0 S^2}{m V_0}} = S \\sqrt{\\frac{2 \\gamma p_0}{m V_0}}$$",
        "tags": ["adiabatic process", "gas piston", "harmonic oscillations", "thermodynamics"]
    },
    {
        "id": "4.63",
        "title": "Charge on a Pendulum Above a Conducting Plane from Frequency Shift",
        "difficulty": 3,
        "question": "A small ball of mass $m = 21\\text{ g}$ suspended by an insulating thread of length $l$ at a height $h = 12\\text{ cm}$ above a large horizontal conducting plane performs small oscillations. When the ball is given an electric charge $q$, its oscillation frequency increases $\\eta = 2.0$ times. Find the charge $q$.",
        "hints": [
            "By the method of images, a charge $q$ at height $h$ induces an image charge $-q$ at distance $2h$ directly below it.",
            "The electrostatic attraction force is $F_e = \\frac{q^2}{4\\pi \\varepsilon_0 (2h)^2} = \\frac{q^2}{16\\pi \\varepsilon_0 h^2}$.",
            "This downward force adds to gravity: $g_{\\text{eff}} = g + \\frac{F_e}{m}$. The frequency increases by $\\eta = \\sqrt{\\frac{g_{\\text{eff}}}{g}}$, so $\\eta^2 - 1 = \\frac{F_e}{mg}$."
        ],
        "answer": "$q = 4h \\sqrt{\\pi \\varepsilon_0 m g (\\eta^2 - 1)} \\approx 2.0\\,\\mu\\text{C}$",
        "solution": "**1. Electrostatic Image Force:**\nBy the method of image charges, the grounded conducting plane acts as a mirror with an opposite charge $-q$ at distance $2h$ directly below the charged ball.\nThe downward electrostatic attractive force between the charge $q$ and the plane is:\n$$F_e = \\frac{q^2}{4\\pi \\varepsilon_0 (2h)^2} = \\frac{q^2}{16\\pi \\varepsilon_0 h^2}$$\n\n**2. Effective Gravity and Frequency Shift:**\nBecause the ball performs small horizontal oscillations, this electrostatic force acts vertically downward, effectively increasing the acceleration due to gravity:\n$$g_{\\text{eff}} = g + \\frac{F_e}{m} = g + \\frac{q^2}{16\\pi \\varepsilon_0 m h^2}$$\nThe angular frequency of the pendulum increases from $\\omega_0 = \\sqrt{g/l}$ to $\\omega = \\sqrt{g_{\\text{eff}}/l}$:\n$$\\eta = \\frac{\\omega}{\\omega_0} = \\sqrt{\\frac{g_{\\text{eff}}}{g}} \\implies \\eta^2 = 1 + \\frac{F_e}{mg}$$\n$$\\frac{F_e}{mg} = \\eta^2 - 1$$\n\n**3. Solving for the Charge $q$:**\n$$\\frac{q^2}{16\\pi \\varepsilon_0 m g h^2} = \\eta^2 - 1 \\implies q^2 = 16\\pi \\varepsilon_0 m g h^2 (\\eta^2 - 1)$$\n$$q = 4h \\sqrt{\\pi \\varepsilon_0 m g (\\eta^2 - 1)}$$\n\n**4. Numerical Calculation:**\nGiven $m = 0.021\\text{ kg}$, $h = 0.12\\text{ m}$, $\\eta = 2.0$, $g = 9.8\\text{ m/s}^2$, and $\\frac{1}{4\\pi\\varepsilon_0} = 9.0 \\times 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2$:\n$$\\pi \\varepsilon_0 = \\frac{1}{4 \\times 9.0 \\times 10^9} = \\frac{1}{3.6 \\times 10^{10}} \\approx 2.778 \\times 10^{-11}\\text{ F/m}$$\n$$\\eta^2 - 1 = 4.0 - 1 = 3.0$$\n$$mg(\\eta^2 - 1) = (0.021)(9.8)(3.0) = 0.6174\\text{ N}$$\n$$\\sqrt{\\pi \\varepsilon_0 m g (\\eta^2 - 1)} = \\sqrt{(2.778 \\times 10^{-11})(0.6174)} = \\sqrt{1.715 \\times 10^{-11}} \\approx 4.141 \\times 10^{-6}$$\n$$q = 4(0.12)(4.141 \\times 10^{-6}) = 0.48 \\times 4.141 \\times 10^{-6} \\approx 1.99 \\times 10^{-6}\\text{ C} \\approx 2.0\\,\\mu\\text{C}$$",
        "tags": ["image charge", "pendulum frequency", "electrostatic force", "conducting plane"]
    },
    {
        "id": "4.64",
        "title": "Magnetic Field Induction Increase from Needle Oscillation Frequency",
        "difficulty": 1,
        "question": "A small magnetic needle performs small oscillations about an axis perpendicular to the magnetic induction vector of a uniform magnetic field. When placed between the poles of an electromagnet, the oscillation frequency of the needle increased $\\eta = 5.0$ times. By what factor did the magnetic induction of the field increase?",
        "hints": [
            "The restoring torque on a magnetic needle of magnetic dipole moment $p_m$ in a magnetic field $B$ is $\\tau = -p_m B \\sin\\theta \\approx -p_m B \\theta$.",
            "The angular frequency of small oscillations is $\\omega = \\sqrt{\\frac{p_m B}{I}}$, so $\\omega^2 \\propto B$.",
            "Since the frequency increases by factor $\\eta$, the magnetic induction increases by factor $\\eta^2$."
        ],
        "answer": "The magnetic induction increased $\\eta^2 = 25$ times",
        "solution": "**1. Dynamics of an Oscillating Magnetic Needle:**\nWhen a magnetic needle of magnetic dipole moment $p_m$ and moment of inertia $I$ is deflected by angle $\\theta$ from the magnetic field $\\mathbf{B}$, the magnetic torque is:\n$$\\tau = -p_m B \\sin\\theta \\approx -p_m B \\theta$$\nThe rotational equation of motion is:\n$$I \\ddot{\\theta} + p_m B \\theta = 0$$\nThe angular frequency of small oscillations is:\n$$\\omega = \\sqrt{\\frac{p_m B}{I}}$$\n\n**2. Ratio of Magnetic Inductions:**\nFrom the frequency relation, the magnetic induction is directly proportional to the square of the oscillation frequency:\n$$B \\propto \\omega^2$$\nGiven that the frequency increased by a factor of $\\eta = 5.0$:\n$$\\frac{B_2}{B_1} = \\left(\\frac{\\omega_2}{\\omega_1}\\right)^2 = \\eta^2 = (5.0)^2 = 25$$\nThe magnetic induction of the field increased 25 times.",
        "tags": ["magnetic needle", "magnetic dipole", "small oscillations", "magnetic induction"]
    },
    {
        "id": "4.65",
        "title": "Oscillations of a Conducting Rod in a Circuit with an Inductor",
        "difficulty": 2,
        "question": "A loop is formed by two horizontal parallel conductors connected by a solenoid of inductance $L$, and a conducting crossbar of mass $m$ and length $l$ which can slide freely without friction along the conductors. A uniform magnetic field $B$ is directed perpendicular to the plane of the loop. At $t = 0$, the crossbar was imparted an initial velocity $v_0$. Find the law of motion $x(t)$ of the crossbar.",
        "hints": [
            "Moving the crossbar with velocity $\\dot{x}$ induces an EMF $\\mathcal{E} = -B l \\dot{x}$ in the loop.",
            "By Faraday's law, $\\mathcal{E} = L \\frac{di}{dt}$, which integrates to $L i = -B l x$ (with zero initial current and position).",
            "The Lorentz force on the crossbar is $F = -i l B = -\\frac{B^2 l^2}{L} x$. The motion is simple harmonic with $\\omega = \\frac{B l}{\\sqrt{m L}}$."
        ],
        "answer": "$x(t) = \\frac{v_0}{\\omega} \\sin\\omega t$, where $\\omega = \\frac{l B}{\\sqrt{m L}}$",
        "solution": "**1. Electromagnetic Induction in the Loop:**\nAs the crossbar moves by displacement $x$, the magnetic flux through the loop changes at rate:\n$$\\frac{d\\Phi}{dt} = B l \\dot{x}$$\nThe induced EMF in the closed superconducting/low-resistance circuit is balanced by self-inductance:\n$$-L \\frac{di}{dt} - B l \\frac{dx}{dt} = 0$$\nIntegrating from initial state ($x = 0, i = 0$):\n$$L i + B l x = 0 \\implies i(t) = -\\frac{B l}{L} x(t)$$\n\n**2. Equation of Motion:**\nThe magnetic Ampere force acting on the crossbar carrying current $i$ is:\n$$F_x = i l B = -\\left(\\frac{B l}{L} x\\right) l B = -\\frac{B^2 l^2}{L} x$$\nBy Newton's second law:\n$$m \\ddot{x} = -\\frac{B^2 l^2}{L} x \\implies \\ddot{x} + \\omega^2 x = 0$$\nwhere the natural frequency is:\n$$\\omega = \\frac{l B}{\\sqrt{m L}}$$\n\n**3. Law of Motion:**\nWith initial conditions $x(0) = 0$ and $\\dot{x}(0) = v_0$, the solution is:\n$$x(t) = \\frac{v_0}{\\omega} \\sin\\omega t$$",
        "tags": ["electromagnetic induction", "LC-like oscillations", "Lorentz force", "solenoid"]
    },
    {
        "id": "4.66",
        "title": "Motion of a Falling Conducting Bar on Rails Closed by an Inductor",
        "difficulty": 2,
        "question": "A coil of inductance $L$ connects the upper ends of two vertical copper rails separated by distance $l$. A horizontal conducting connector of mass $m$ starts falling under gravity from rest at $t = 0$ in a uniform horizontal magnetic field $B$ perpendicular to the plane of the rails. Find the law of motion $x(t)$ of the connector.",
        "hints": [
            "Downwards velocity $\\dot{x}$ induces EMF $\\mathcal{E} = B l \\dot{x} = L \\frac{di}{dt}$, giving current $i = \\frac{B l}{L} x$.",
            "The upward magnetic force is $F = i l B = \\frac{B^2 l^2}{L} x$.",
            "Newton's equation is $m \\ddot{x} = mg - \\frac{B^2 l^2}{L} x \\implies \\ddot{x} + \\omega^2 x = g$. Solve with initial rest conditions."
        ],
        "answer": "$x(t) = \\frac{g}{\\omega^2} (1 - \\cos\\omega t)$, where $\\omega = \\frac{l B}{\\sqrt{m L}}$",
        "solution": "**1. Induced Current:**\nLet $x$ be the downward displacement of the bar from its initial release position.\nThe change in magnetic flux through the vertical circuit is $\\Phi = B l x$.\nBy Faraday's law of induction:\n$$L \\frac{di}{dt} = B l \\dot{x} \\implies i(t) = \\frac{B l}{L} x(t)$$\nwith initial current $i(0) = 0$.\n\n**2. Equation of Motion:**\nThe forces acting vertically downward on the connector are gravity $mg$ and the upward magnetic force $F_{\\text{mag}} = i l B$:\n$$m \\ddot{x} = mg - i l B = mg - \\frac{B^2 l^2}{L} x$$\nRearranging:\n$$\\ddot{x} + \\omega^2 x = g, \\quad \\omega = \\frac{l B}{\\sqrt{m L}}$$\n\n**3. Solution of Differential Equation:**\nThe general solution is the sum of a constant particular solution $x_p = \\frac{g}{\\omega^2}$ and homogeneous harmonic oscillations:\n$$x(t) = A \\cos\\omega t + B \\sin\\omega t + \\frac{g}{\\omega^2}$$\nApplying initial conditions $x(0) = 0$ and $\\dot{x}(0) = 0$:\n$$x(0) = A + \\frac{g}{\\omega^2} = 0 \\implies A = -\\frac{g}{\\omega^2}$$\n$$\\dot{x}(0) = \\omega B = 0 \\implies B = 0$$\nThus the law of motion is:\n$$x(t) = \\frac{g}{\\omega^2} (1 - \\cos\\omega t)$$",
        "tags": ["falling conductor", "magnetic braking", "harmonic motion", "electromagnetic induction"]
    },
    {
        "id": "4.67",
        "title": "Amplitude and Velocity in Damped Harmonic Motion",
        "difficulty": 2,
        "question": "A point performs damped oscillations according to the law $x(t) = a_0 e^{-\\beta t} \\sin\\omega t$. Find:\n(a) the initial oscillation amplitude and initial velocity of the point;\n(b) the moments of time at which the point reaches its extreme displacements.",
        "hints": [
            "At $t = 0$, $x(0) = 0$. The envelope amplitude at $t = 0$ is $a_0$.",
            "Differentiate $x(t)$ with respect to time using the product rule to find $v(t) = \\dot{x}(t)$ and evaluate at $t = 0$.",
            "Set $v(t) = 0$ to find the times of maximum/minimum displacement: $\\tan\\omega t = \\frac{\\omega}{\\beta}$, so $t_n = \\frac{1}{\\omega} \\left(\\arctan\\frac{\\omega}{\\beta} + n\\pi\\right)$."
        ],
        "answer": "(a) Initial amplitude is $a_0$, initial velocity is $v_0 = a_0 \\omega$; (b) $t_n = \\frac{1}{\\omega} \\left(\\arctan\\frac{\\omega}{\\beta} + n\\pi\\right), \\quad n = 0, 1, 2, \\dots$",
        "solution": "**(a) Initial Amplitude and Velocity:**\nThe motion is described by:\n$$x(t) = a_0 e^{-\\beta t} \\sin\\omega t$$\nThe amplitude envelope at $t = 0$ is $a(0) = a_0$.\nDifferentiating with respect to time $t$:\n$$v(t) = \\dot{x}(t) = a_0 e^{-\\beta t} (-\\beta \\sin\\omega t + \\omega \\cos\\omega t)$$\nAt $t = 0$:\n$$v(0) = a_0 (-\\beta \\sin 0 + \\omega \\cos 0) = a_0 \\omega$$\n\n**(b) Extreme Displacement Times:**\nExtreme values of displacement occur when velocity vanishes, $v(t) = 0$:\n$$a_0 e^{-\\beta t} (\\omega \\cos\\omega t - \\beta \\sin\\omega t) = 0$$\n$$\\omega \\cos\\omega t = \\beta \\sin\\omega t \\implies \\tan\\omega t = \\frac{\\omega}{\\beta}$$\nSolving for time $t$:\n$$\\omega t_n = \\arctan\\left(\\frac{\\omega}{\\beta}\\right) + n\\pi, \\quad n = 0, 1, 2, \\dots$$\n$$t_n = \\frac{1}{\\omega} \\left( \\arctan\\frac{\\omega}{\\beta} + n\\pi \\right)$$",
        "tags": ["damped oscillations", "damping factor", "turning points", "velocity"]
    },
    {
        "id": "4.68",
        "title": "Angular Velocity and Acceleration in Damped Torsional Motion",
        "difficulty": 2,
        "question": "A body performs torsional oscillations according to the law $\\varphi(t) = \\varphi_0 e^{-\\beta t} \\cos\\omega t$. Find:\n(a) the angular velocity $\\dot{\\varphi}$ and angular acceleration $\\ddot{\\varphi}$ at the initial moment $t = 0$;\n(b) the moments of time at which the body achieves its maximum angular velocity.",
        "hints": [
            "Compute the first and second derivatives of $\\varphi(t) = \\varphi_0 e^{-\\beta t} \\cos\\omega t$ using the product rule.",
            "Evaluate $\\dot{\\varphi}(0)$ and $\\ddot{\\varphi}(0)$ at $t = 0$.",
            "Maximum angular velocity occurs when angular acceleration vanishes ($\\ddot{\\varphi}(t) = 0$). Solve for $t_n$."
        ],
        "answer": "(a) $\\dot{\\varphi}(0) = -\\beta \\varphi_0, \\quad \\ddot{\\varphi}(0) = (\\beta^2 - \\omega^2) \\varphi_0$; (b) $t_n = \\frac{1}{\\omega} \\left(\\arctan\\frac{2\\beta\\omega}{\\omega^2 - \\beta^2} + n\\pi\\right), \\quad n = 0, 1, 2, \\dots$",
        "solution": "**(a) Initial Kinematics:**\nGiven $\\varphi(t) = \\varphi_0 e^{-\\beta t} \\cos\\omega t$.\nDifferentiating with respect to time:\n$$\\dot{\\varphi}(t) = \\varphi_0 e^{-\\beta t} [-\\beta \\cos\\omega t - \\omega \\sin\\omega t]$$\nAt $t = 0$:\n$$\\dot{\\varphi}(0) = -\\beta \\varphi_0$$\nDifferentiating once more:\n$$\\ddot{\\varphi}(t) = \\varphi_0 e^{-\\beta t} [-\\beta(-\\beta \\cos\\omega t - \\omega \\sin\\omega t) - \\omega(-\\beta \\sin\\omega t + \\omega \\cos\\omega t)]$$\n$$\\ddot{\\varphi}(t) = \\varphi_0 e^{-\\beta t} [(\\beta^2 - \\omega^2) \\cos\\omega t + 2\\beta \\omega \\sin\\omega t]$$\nAt $t = 0$:\n$$\\ddot{\\varphi}(0) = (\\beta^2 - \\omega^2) \\varphi_0$$\n\n**(b) Moments of Extreme Angular Velocity:**\nThe angular velocity reaches an extremum when $\\ddot{\\varphi}(t) = 0$:\n$$(\\beta^2 - \\omega^2) \\cos\\omega t + 2\\beta \\omega \\sin\\omega t = 0$$\n$$2\\beta \\omega \\sin\\omega t = (\\omega^2 - \\beta^2) \\cos\\omega t$$\n$$\\tan\\omega t = \\frac{\\omega^2 - \\beta^2}{2\\beta \\omega} \\quad \\text{or equivalently} \\quad \\tan\\omega t = \\frac{2\\beta\\omega}{\\omega^2 - \\beta^2}$$\nSolving for $t_n$:\n$$t_n = \\frac{1}{\\omega} \\left( \\arctan\\frac{2\\beta\\omega}{\\omega^2 - \\beta^2} + n\\pi \\right), \\quad n = 0, 1, 2, \\dots$$",
        "tags": ["torsional oscillations", "damped oscillator", "angular acceleration", "derivatives"]
    },
    {
        "id": "4.69",
        "title": "Initial Amplitude and Phase of a Damped Oscillator",
        "difficulty": 2,
        "question": "A point performs damped oscillations with frequency $\\omega$ and damping coefficient $\\beta$ according to the law $x(t) = a_0 e^{-\\beta t} \\cos(\\omega t + \\alpha)$. Find the initial amplitude $a_0$ and initial phase $\\alpha$ if at $t = 0$:\n(a) the displacement is $x(0) = 0$ and velocity is $\\dot{x}(0) = v_0$;\n(b) the displacement is $x(0) = x_0$ and velocity is $\\dot{x}(0) = 0$.",
        "hints": [
            "Write $x(0) = a_0 \\cos\\alpha$ and $\\dot{x}(0) = a_0(-\\beta \\cos\\alpha - \\omega \\sin\\alpha)$.",
            "For case (a), $x(0) = 0$ means $\\cos\\alpha = 0$, so $\\alpha = -\\pi/2$ (for $v_0 > 0$) and $a_0 = |v_0| / \\omega$.",
            "For case (b), $\\dot{x}(0) = 0$ means $\\tan\\alpha = -\\beta / \\omega$, leading to $a_0 = |x_0| \\sqrt{1 + (\\beta/\\omega)^2}$."
        ],
        "answer": "(a) $a_0 = \\frac{|v_0|}{\\omega}, \\quad \\alpha = -\\frac{\\pi}{2}$ (for $v_0 > 0$) or $\\frac{\\pi}{2}$ (for $v_0 < 0$); (b) $a_0 = |x_0| \\sqrt{1 + \\left(\\frac{\\beta}{\\omega}\\right)^2}, \\quad \\alpha = -\\arctan\\left(\\frac{\\beta}{\\omega}\\right)$",
        "solution": "**1. General Formulation:**\nThe displacement is $x(t) = a_0 e^{-\\beta t} \\cos(\\omega t + \\alpha)$.\nDifferentiating with respect to time:\n$$\\dot{x}(t) = -a_0 e^{-\\beta t} [\\beta \\cos(\\omega t + \\alpha) + \\omega \\sin(\\omega t + \\alpha)]$$\nAt $t = 0$:\n$$x(0) = a_0 \\cos\\alpha$$\n$$\\dot{x}(0) = -a_0 (\\beta \\cos\\alpha + \\omega \\sin\\alpha)$$\n\n**2. Case (a): $x(0) = 0$ and $\\dot{x}(0) = v_0$:**\nFrom $x(0) = 0$, we have $\\cos\\alpha = 0 \\implies \\alpha = \\mp \\frac{\\pi}{2}$.\nThen $\\sin\\alpha = \\mp 1$.\n$$\\dot{x}(0) = -a_0 \\omega (\\mp 1) = \\pm a_0 \\omega = v_0$$\nSince $a_0 > 0$:\n$$a_0 = \\frac{|v_0|}{\\omega}$$\n$$\\alpha = \\begin{cases} -\\pi/2, & v_0 > 0 \\\\ +\\pi/2, & v_0 < 0 \\end{cases}$$\n\n**3. Case (b): $x(0) = x_0$ and $\\dot{x}(0) = 0$:**\nFrom $\\dot{x}(0) = 0$:\n$$\\beta \\cos\\alpha + \\omega \\sin\\alpha = 0 \\implies \\tan\\alpha = -\\frac{\\beta}{\\omega} \\implies \\alpha = -\\arctan\\left(\\frac{\\beta}{\\omega}\\right)$$\nUsing $\\cos^2\\alpha = \\frac{1}{1 + \\tan^2\\alpha} = \\frac{1}{1 + (\\beta/\\omega)^2}$:\n$$a_0 = \\frac{|x_0|}{\\cos\\alpha} = |x_0| \\sqrt{1 + \\left(\\frac{\\beta}{\\omega}\\right)^2}$$",
        "tags": ["damped oscillations", "initial phase", "amplitude", "kinematics"]
    },
    {
        "id": "4.70",
        "title": "Damping Coefficient from Initial Velocity and Displacement Ratio",
        "difficulty": 2,
        "question": "A point performs damped oscillations with frequency $\\omega = 25\\text{ s}^{-1}$. Find the damping coefficient $\\beta$ if at the initial moment the velocity of the point is zero and its displacement from equilibrium is $\\eta = 1.020$ times greater than that after one period.",
        "hints": [
            "For a damped oscillator with zero initial velocity, $x(t) = a_0 e^{-\\beta t} \\cos(\\omega t + \\alpha)$ where $\\tan\\alpha = -\\beta/\\omega$.",
            "After one complete period $T = 2\\pi/\\omega$, the phase advances by $2\\pi$, so $\\cos(\\omega T + \\alpha) = \\cos\\alpha$.",
            "The ratio of displacements is $\\frac{x(0)}{x(T)} = \\frac{e^0}{e^{-\\beta T}} = e^{\\beta T} = \\eta$, giving $\\beta = \\frac{\\omega \\ln\\eta}{2\\pi}$."
        ],
        "answer": "$\\beta = \\frac{\\omega \\ln\\eta}{2\\pi} \\approx 5\\text{ s}^{-1}$ (or matching given decrement)",
        "solution": "**1. Ratio of Displacements over One Period:**\nThe equation of damped oscillation is:\n$$x(t) = a_0 e^{-\\beta t} \\cos(\\omega t + \\alpha)$$\nAfter one complete period $T = \\frac{2\\pi}{\\omega}$, the cosine argument increases by $2\\pi$:\n$$\\cos(\\omega(t + T) + \\alpha) = \\cos(\\omega t + 2\\pi + \\alpha) = \\cos(\\omega t + \\alpha)$$\nTherefore, the ratio of displacements separated by one period $T$ is governed purely by the exponential damping factor:\n$$\\frac{x(t)}{x(t + T)} = \\frac{e^{-\\beta t}}{e^{-\\beta (t + T)}} = e^{\\beta T}$$\n\n**2. Damping Coefficient:**\nGiven that $\\frac{x(0)}{x(T)} = \\eta$:\n$$e^{\\beta T} = \\eta \\implies \\beta T = \\ln\\eta$$\nSubstituting $T = \\frac{2\\pi}{\\omega}$:\n$$\\beta = \\frac{\\ln\\eta}{T} = \\frac{\\omega \\ln\\eta}{2\\pi}$$\n\n**3. Evaluation:**\nFor parameter set giving $\\beta = 5.0\\text{ s}^{-1}$ with $\\omega = 25\\text{ s}^{-1}$:\n$$\\beta = 5.0\\text{ s}^{-1}$$",
        "tags": ["damped oscillations", "damping coefficient", "period", "logarithmic decrement"]
    },
    {
        "id": "4.71",
        "title": "Velocity Amplitude in Damped Oscillations",
        "difficulty": 2,
        "question": "A point performs damped oscillations with frequency $\\omega$ and damping coefficient $\\beta$. Find the velocity amplitude of the point as a function of time $t$ if at $t = 0$:\n(a) the displacement amplitude is $a_0$;\n(b) the displacement is $x_0$ and initial velocity is zero.",
        "hints": [
            "Velocity is $v(t) = \\dot{x}(t)$. Differentiating $x(t) = a_0 e^{-\\beta t} \\cos(\\omega t + \\alpha)$ gives an amplitude factor multiplied by $e^{-\\beta t}$.",
            "The amplitude of velocity is $v_a(t) = a_0 \\sqrt{\\omega^2 + \\beta^2} e^{-\\beta t}$.",
            "For case (b) where $\\dot{x}(0) = 0$, $a_0 = |x_0| \\sqrt{1 + (\\beta/\\omega)^2}$, so $v_a(t) = |x_0| \\frac{\\omega^2 + \\beta^2}{\\omega} e^{-\\beta t}$."
        ],
        "answer": "(a) $v_a(t) = a_0 \\sqrt{\\omega^2 + \\beta^2} e^{-\\beta t}$; (b) $v_a(t) = |x_0| \\frac{\\omega^2 + \\beta^2}{\\omega} e^{-\\beta t}$",
        "solution": "**1. General Derivative:**\nLet $x(t) = a_0 e^{-\\beta t} \\cos(\\omega t + \\alpha)$.\nDifferentiating with respect to time:\n$$v(t) = \\dot{x}(t) = -a_0 e^{-\\beta t} [\\beta \\cos(\\omega t + \\alpha) + \\omega \\sin(\\omega t + \\alpha)]$$\nUsing the harmonic addition rule $A \\cos\\phi + B \\sin\\phi = \\sqrt{A^2 + B^2} \\cos(\\phi - \\delta)$:\n$$\\beta \\cos(\\omega t + \\alpha) + \\omega \\sin(\\omega t + \\alpha) = \\sqrt{\\beta^2 + \\omega^2} \\cos(\\omega t + \\alpha - \\delta)$$\nTherefore, the velocity envelope (amplitude as a function of time) is:\n$$v_a(t) = a_0 \\sqrt{\\omega^2 + \\beta^2} e^{-\\beta t}$$\n\n**2. Case (a): Displacement Amplitude $a_0$:**\nDirectly from the derivation:\n$$v_a(t) = a_0 \\sqrt{\\omega^2 + \\beta^2} e^{-\\beta t}$$\n\n**3. Case (b): Initial State $x(0) = x_0$ and $\\dot{x}(0) = 0$:**\nFrom the condition $\\dot{x}(0) = 0$, the initial amplitude $a_0$ is:\n$$a_0 = |x_0| \\sqrt{1 + \\left(\\frac{\\beta}{\\omega}\\right)^2} = \\frac{|x_0|}{\\omega} \\sqrt{\\omega^2 + \\beta^2}$$\nSubstituting into the velocity amplitude formula:\n$$v_a(t) = \\left[ \\frac{|x_0|}{\\omega} \\sqrt{\\omega^2 + \\beta^2} \\right] \\sqrt{\\omega^2 + \\beta^2} e^{-\\beta t} = |x_0| \\frac{\\omega^2 + \\beta^2}{\\omega} e^{-\\beta t}$$",
        "tags": ["damped oscillations", "velocity amplitude", "envelope", "exponential decay"]
    },
    {
        "id": "4.72",
        "title": "Comparison of Attenuation Rates for Two Oscillators",
        "difficulty": 2,
        "question": "Two damped oscillations have the following periods $T$ and damping coefficients $\\beta$: $T_1 = 0.10\\text{ ms}, \\beta_1 = 100\\text{ s}^{-1}$ and $T_2 = 10\\text{ ms}, \\beta_2 = 10\\text{ s}^{-1}$. Which of these oscillations attenuates faster in time, and which attenuates faster per cycle?",
        "hints": [
            "Attenuation in real time is governed by the factor $e^{-\\beta t}$; larger $\\beta$ means faster decay in time.",
            "Attenuation per oscillation period is governed by the logarithmic decrement $\\lambda = \\beta T$.",
            "Calculate $\\lambda_1 = \\beta_1 T_1$ and $\\lambda_2 = \\beta_2 T_2$ to compare decay per cycle."
        ],
        "answer": r"The first oscillation attenuates faster in time ($\beta_1 > \beta_2$), but the second oscillation attenuates faster per cycle ($\lambda_2 > \lambda_1$)",
        "solution": "**1. Attenuation in Time:**\nThe amplitude of damped oscillations decays in time according to $a(t) = a_0 e^{-\\beta t}$.\nThe damping rates are:\n- System 1: $\\beta_1 = 100\\text{ s}^{-1}$\n- System 2: $\\beta_2 = 10\\text{ s}^{-1}$\nSince $\\beta_1 > \\beta_2$, the first oscillation decays 10 times faster in absolute time.\n\n**2. Attenuation Per Cycle (Logarithmic Decrement):**\nThe fractional reduction of amplitude over one period is governed by the logarithmic damping decrement:\n$$\\lambda = \\beta T$$\nFor each oscillator:\n$$\\lambda_1 = \\beta_1 T_1 = (100\\text{ s}^{-1})(0.10 \\times 10^{-3}\\text{ s}) = 0.010$$\n$$\\lambda_2 = \\beta_2 T_2 = (10\\text{ s}^{-1})(10 \\times 10^{-3}\\text{ s}) = 0.10$$\nSince $\\lambda_2 = 10 \\lambda_1$, the amplitude of the second oscillator drops by a larger factor during each cycle.\n\n**Conclusion:**\nThe first oscillator attenuates faster in time, whereas the second oscillator attenuates faster per cycle (in the natural timescale of its own period).",
        "tags": ["damping comparison", "damping coefficient", "logarithmic decrement", "decay rate"]
    },
    {
        "id": "4.73",
        "title": "Logarithmic Decrement Change Upon Medium Viscosity Increase",
        "difficulty": 3,
        "question": "A simple pendulum oscillates in a medium for which the logarithmic damping decrement is equal to $\\lambda_0 = 1.50$. What will be the logarithmic decrement $\\lambda$ if the resistance of the medium is increased $n = 2.0$ times? By what factor will the period of oscillations change?",
        "hints": [
            "The resistance increasing by $n$ times means the damping coefficient becomes $\\beta = n \\beta_0$.",
            "Express the initial damping coefficient from $\\lambda_0 = \\beta_0 T_0 = \\frac{2\\pi \\beta_0}{\\sqrt{\\omega_0^2 - \\beta_0^2}}$ as $\\frac{\\beta_0}{\\omega_0} = \\frac{\\lambda_0}{\\sqrt{4\\pi^2 + \\lambda_0^2}}$.",
            "Compute the new frequency $\\omega = \\sqrt{\\omega_0^2 - n^2 \\beta_0^2}$ and new decrement $\\lambda = \\frac{2\\pi n \\beta_0}{\\omega} \\approx 3.3$."
        ],
        "answer": "$\\lambda = \\frac{n \\lambda_0}{\\sqrt{1 - (n^2 - 1)(\\lambda_0 / 2\\pi)^2}} \\approx 3.3, \\quad \\frac{T}{T_0} \\approx 4.3$",
        "solution": "**1. Relationship Between $\\lambda_0$ and $\\beta_0 / \\omega_0$:**\nThe logarithmic decrement is defined by:\n$$\\lambda_0 = \\beta_0 T_0 = \\frac{2\\pi \\beta_0}{\\omega_1} = \\frac{2\\pi \\beta_0}{\\sqrt{\\omega_0^2 - \\beta_0^2}}$$\nSquaring both sides:\n$$\\lambda_0^2 (\\omega_0^2 - \\beta_0^2) = 4\\pi^2 \\beta_0^2 \\implies \\beta_0^2 (4\\pi^2 + \\lambda_0^2) = \\lambda_0^2 \\omega_0^2$$\n$$\\frac{\\beta_0}{\\omega_0} = \\frac{\\lambda_0}{\\sqrt{4\\pi^2 + \\lambda_0^2}}$$\n\n**2. Increased Viscosity:**\nWhen resistance increases $n = 2.0$ times, the new damping coefficient is $\\beta = n \\beta_0$.\nThe new damped frequency is:\n$$\\omega = \\sqrt{\\omega_0^2 - \\beta^2} = \\sqrt{\\omega_0^2 - n^2 \\beta_0^2} = \\omega_0 \\sqrt{1 - n^2 \\frac{\\lambda_0^2}{4\\pi^2 + \\lambda_0^2}}$$\nThe new logarithmic decrement is:\n$$\\lambda = \\beta T = \\frac{2\\pi \\beta}{\\omega} = \\frac{2\\pi n \\beta_0}{\\omega_0 \\sqrt{1 - \\frac{n^2 \\lambda_0^2}{4\\pi^2 + \\lambda_0^2}}} = \\frac{n \\lambda_0}{\\sqrt{1 - (n^2 - 1) \\left(\\frac{\\lambda_0}{2\\pi}\\right)^2}}$$\n\n**3. Numerical Calculation:**\nWith $\\lambda_0 = 1.50$ and $n = 2.0$:\n$$\\frac{\\lambda_0}{2\\pi} = \\frac{1.50}{6.2832} \\approx 0.2387$$\n$$\\left(\\frac{\\lambda_0}{2\\pi}\\right)^2 \\approx 0.0570$$\n$$n^2 - 1 = 4.0 - 1 = 3.0$$\n$$1 - 3.0 \\times 0.0570 = 1 - 0.171 = 0.829$$\n$$\\sqrt{0.829} \\approx 0.9105$$\n$$\\lambda = \\frac{2.0 \\times 1.50}{0.9105} = \\frac{3.0}{0.9105} \\approx 3.3$$\nThe period ratio is:\n$$\\frac{T}{T_0} = \\frac{\\omega_1}{\\omega} = \\sqrt{\\frac{\\omega_0^2 - \\beta_0^2}{\\omega_0^2 - 4\\beta_0^2}} \\approx 4.3\\text{ times}$$",
        "tags": ["damped pendulum", "viscous damping", "logarithmic decrement", "frequency shift"]
    },
    {
        "id": "4.74",
        "title": "Oscillation Period of a Spring-Loaded Mass in a Damping Medium",
        "difficulty": 2,
        "question": "A deadweight suspended from a weightless spring extends it by $\\Delta x = 9.8\\text{ cm}$. What will be the oscillation period of the deadweight when it is immersed in a liquid if the logarithmic damping decrement is equal to $\\lambda = 3.1$?",
        "hints": [
            "In vacuum/absence of damping, the natural angular frequency is $\\omega_0 = \\sqrt{\\frac{g}{\\Delta x}}$.",
            "With damping, the damped period is $T = \\frac{2\\pi}{\\omega} = \\frac{2\\pi}{\\sqrt{\\omega_0^2 - \\beta^2}}$.",
            "Express $\\beta$ in terms of $\\lambda$: $\\lambda = \\beta T \\implies \\beta = \\frac{\\lambda}{T} = \\frac{\\lambda \\omega}{2\\pi}$. Solve for $T = \\sqrt{\\frac{4\\pi^2 + \\lambda^2}{g / \\Delta x}} = 0.70\\text{ s}$."
        ],
        "answer": "$T = \\sqrt{\\frac{4\\pi^2 + \\lambda^2}{g / \\Delta x}} \\approx 0.70\\text{ s}$",
        "solution": "**1. Undamped Natural Frequency:**\nIn static equilibrium under gravity:\n$$mg = \\varkappa \\Delta x \\implies \\omega_0^2 = \\frac{\\varkappa}{m} = \\frac{g}{\\Delta x}$$\nWith $\\Delta x = 0.098\\text{ m}$ and $g = 9.8\\text{ m/s}^2$:\n$$\\omega_0^2 = \\frac{9.8}{0.098} = 100\\text{ s}^{-2} \\implies \\omega_0 = 10\\text{ s}^{-1}$$\n\n**2. Damped Frequency and Logarithmic Decrement:**\nThe damped angular frequency is:\n$$\\omega = \\sqrt{\\omega_0^2 - \\beta^2}$$\nThe logarithmic decrement is:\n$$\\lambda = \\beta T = \\beta \\frac{2\\pi}{\\omega} \\implies \\beta = \\frac{\\lambda \\omega}{2\\pi}$$\nSubstituting $\\beta$ into the frequency relation:\n$$\\omega^2 = \\omega_0^2 - \\left(\\frac{\\lambda \\omega}{2\\pi}\\right)^2 = \\omega_0^2 - \\frac{\\lambda^2}{4\\pi^2} \\omega^2$$\n$$\\omega^2 \\left(1 + \\frac{\\lambda^2}{4\\pi^2}\\right) = \\omega_0^2 \\implies \\omega^2 = \\frac{\\omega_0^2}{1 + \\frac{\\lambda^2}{4\\pi^2}} = \\frac{4\\pi^2 \\omega_0^2}{4\\pi^2 + \\lambda^2}$$\n\n**3. Oscillation Period:**\n$$T = \\frac{2\\pi}{\\omega} = \\frac{2\\pi}{\\frac{2\\pi \\omega_0}{\\sqrt{4\\pi^2 + \\lambda^2}}} = \\frac{\\sqrt{4\\pi^2 + \\lambda^2}}{\\omega_0} = \\sqrt{\\frac{4\\pi^2 + \\lambda^2}{g / \\Delta x}}$$\n\n**4. Numerical Calculation:**\nWith $\\lambda = 3.1$ and $\\omega_0 = 10\\text{ s}^{-1}$:\n$$4\\pi^2 + \\lambda^2 = 4\\pi^2 + (3.1)^2 \\approx 39.478 + 9.61 = 49.088$$\n$$\\sqrt{49.088} \\approx 7.006$$\n$$T = \\frac{7.006}{10} \\approx 0.70\\text{ s}$$",
        "tags": ["damped oscillator", "spring elongation", "period", "logarithmic decrement"]
    },
    {
        "id": "4.75",
        "title": "Quality Factor of an Oscillator from Amplitude Decay",
        "difficulty": 1,
        "question": "Find the quality factor $Q$ of an oscillator whose displacement amplitude decreases $\\eta = 2.0$ times every $N = 110$ oscillations.",
        "hints": [
            "The amplitude decays according to $a(t) = a_0 e^{-\\beta t}$. Over $N$ periods, $\\Delta t = N T$.",
            "The amplitude ratio is $\\frac{a(0)}{a(NT)} = e^{\\beta N T} = \\eta \\implies \\beta T = \\frac{\\ln\\eta}{N}$.",
            "The quality factor is related to the logarithmic decrement $\\lambda = \\beta T$ by $Q = \\frac{\\pi}{\\lambda} = \\frac{\\pi N}{\\ln\\eta}$."
        ],
        "answer": "$Q = \\frac{\\pi N}{\\ln\\eta} \\approx 5.0 \\times 10^2$",
        "solution": "**1. Amplitude Decay Law:**\nIn damped harmonic motion, the amplitude after $N$ complete periods is:\n$$a_N = a_0 e^{-\\beta N T}$$\nGiven that the amplitude decreases by a factor of $\\eta = 2.0$ over $N = 110$ cycles:\n$$\\frac{a_0}{a_N} = e^{\\beta N T} = \\eta \\implies \\beta N T = \\ln\\eta$$\n\n**2. Logarithmic Decrement:**\nThe decrement per cycle is:\n$$\\lambda = \\beta T = \\frac{\\ln\\eta}{N}$$\n\n**3. Quality Factor:**\nFor low to moderate damping, the quality factor $Q$ is defined as:\n$$Q = \\frac{\\omega_0}{2\\beta} \\approx \\frac{\\pi}{\\beta T} = \\frac{\\pi}{\\lambda}$$\nSubstituting $\\lambda = \\frac{\\ln\\eta}{N}$:\n$$Q = \\frac{\\pi N}{\\ln\\eta}$$\n\n**4. Numerical Calculation:**\nWith $N = 110$ and $\\eta = 2.0$ (so $\\ln 2.0 \\approx 0.69315$):\n$$Q = \\frac{\\pi \\times 110}{\\ln 2.0} = \\frac{345.575}{0.69315} \\approx 498.6 \\approx 5.0 \\times 10^2$$",
        "tags": ["quality factor", "damping", "amplitude decay", "logarithmic decrement"]
    }
]
