"""
ch1_3_batch3.py
Problems 1.173 through 1.199 of Irodov Chapter 1.3:
Laws of Conservation of Energy, Momentum, and Angular Momentum.
"""

CH1_3_BATCH_3 = [
    {
        "id": "1.173",
        "title": "Inelastic Collision Deflection and Kinetic Energy Change",
        "difficulty": 3,
        "question": "A particle of mass $m$ having collided with a stationary particle of mass $M$ deviated by an angle $\\pi/2$ whereas the particle $M$ recoiled at an angle $\\theta = 30^{\\circ}$ to the direction of the initial motion of the particle $m$. How much (in per cent) and in what way has the kinetic energy of this system changed after the collision, if $M/m = 5.0$?",
        "hints": [
            "Write the conservation of momentum along the initial direction (x-axis) and transverse direction (y-axis).",
            "Relate the final velocities $v'$ (particle $m$) and $V'$ (particle $M$) to the initial velocity $v$.",
            "Calculate the final kinetic energy and determine $\\frac{\\Delta T}{T} = \\frac{T_f - T_i}{T_i} \\times 100\\%$."
        ],
        "answer": "$\\frac{\\Delta T}{T} = -40\\%$ (decreased by $40\\%$)",
        "solution": "**1. Conservation of Linear Momentum:**\nLet the incident particle $m$ move along the $+x$ direction with velocity $v$.\nAfter the collision:\n- Particle $m$ moves along the $+y$ direction with speed $v'$.\n- Particle $M$ recoils at angle $\\theta = 30^{\\circ}$ to the $+x$ axis (in fourth quadrant, angle $-\\theta$) with speed $V'$.\n\nComponents of momentum:\n- Along $x$:\n  $$m v = M V' \\cos\\theta \\implies V' = \\frac{m v}{M \\cos\\theta}$$\n- Along $y$:\n  $$0 = m v' - M V' \\sin\\theta \\implies v' = \\frac{M}{m} V' \\sin\\theta = \\frac{M}{m} \\left(\\frac{m v}{M \\cos\\theta}\\right) \\sin\\theta = v\\tan\\theta$$\n\n**2. Final Kinetic Energy:**\nInitial kinetic energy:\n$$T_i = \\frac{1}{2}m v^2$$\nFinal kinetic energy:\n$$T_f = \\frac{1}{2}m {v'}^2 + \\frac{1}{2}M {V'}^2 = \\frac{1}{2}m (v\\tan\\theta)^2 + \\frac{1}{2}M \\left(\\frac{mv}{M\\cos\\theta}\\right)^2$$\n$$T_f = \\frac{1}{2}m v^2 \\left[ \\tan^2\\theta + \\frac{m}{M}\\frac{1}{\\cos^2\\theta} \\right] = T_i \\left[ \\tan^2\\theta + \\frac{m}{M}(1 + \\tan^2\\theta) \\right]$$\n\n**3. Numerical Evaluation:**\nWith $\\theta = 30^{\\circ}$ (so $\\tan 30^{\\circ} = 1/\\sqrt{3}, \\tan^2 30^{\\circ} = 1/3$) and $M/m = 5.0$ ($m/M = 0.20$):\n$$\\frac{T_f}{T_i} = \\frac{1}{3} + 0.20 \\left(1 + \\frac{1}{3}\\right) = \\frac{1}{3} + 0.20 \\left(\\frac{4}{3}\\right) = \\frac{1}{3} + \\frac{0.8}{3} = \\frac{1.8}{3} = 0.60$$\n$$\\frac{\\Delta T}{T_i} = \\frac{T_f - T_i}{T_i} = 0.60 - 1 = -0.40 = -40\\%$$",
        "tags": ["collisions", "conservation of momentum", "kinetic energy loss"]
    },
    {
        "id": "1.174",
        "title": "Center of Inertia Quantities for Perpendicular Particles",
        "difficulty": 2,
        "question": "A closed system consists of two particles of masses $m_1$ and $m_2$ which move at right angles to each other with velocities $\\mathbf{v}_1$ and $\\mathbf{v}_2$. Find:\n(a) the momentum of each particle in the reference frame fixed to their centre of inertia;\n(b) the total kinetic energy of the two particles in the reference frame fixed to their centre of inertia.",
        "hints": [
            "In the center of inertia frame, the two particles have equal and opposite momenta: $\\tilde{\\mathbf{p}}_1 = -\\tilde{\\mathbf{p}}_2 = \\mu(\\mathbf{v}_1 - \\mathbf{v}_2)$.",
            "Since $\\mathbf{v}_1 \\perp \\mathbf{v}_2$, the magnitude of relative velocity is $|\\mathbf{v}_1 - \\mathbf{v}_2| = \\sqrt{v_1^2 + v_2^2}$.",
            "Internal kinetic energy is $\\tilde{T} = \\frac{p^2}{2\\mu} = \\frac{1}{2}\\mu(v_1^2 + v_2^2)$."
        ],
        "answer": "(a) $\\tilde{p} = \\mu\\sqrt{v_1^2 + v_2^2}$; (b) $\\tilde{T} = \\frac{1}{2}\\mu(v_1^2 + v_2^2)$, where $\\mu = \\frac{m_1 m_2}{m_1 + m_2}$",
        "solution": "**(a) Momentum of each particle in CM frame:**\nThe center of mass velocity is $\\mathbf{V}_C = \\frac{m_1 \\mathbf{v}_1 + m_2 \\mathbf{v}_2}{m_1 + m_2}$.\nThe momentum of particle 1 in the CM frame is:\n$$\\tilde{\\mathbf{p}}_1 = m_1(\\mathbf{v}_1 - \\mathbf{V}_C) = m_1\\left(\\mathbf{v}_1 - \\frac{m_1 \\mathbf{v}_1 + m_2 \\mathbf{v}_2}{m_1 + m_2}\\right) = \\frac{m_1 m_2}{m_1 + m_2}(\\mathbf{v}_1 - \\mathbf{v}_2) = \\mu(\\mathbf{v}_1 - \\mathbf{v}_2)$$\nSimilarly, $\\tilde{\\mathbf{p}}_2 = -\\tilde{\\mathbf{p}}_1 = -\\mu(\\mathbf{v}_1 - \\mathbf{v}_2)$.\nSince $\\mathbf{v}_1 \\perp \\mathbf{v}_2$, the modulus of relative velocity is:\n$$|\\mathbf{v}_1 - \\mathbf{v}_2| = \\sqrt{v_1^2 + v_2^2}$$\nTherefore, the magnitude of momentum for each particle is:\n$$\\tilde{p} = \\mu\\sqrt{v_1^2 + v_2^2}$$\n\n**(b) Cumulative Kinetic Energy in CM frame:**\n$$\\tilde{T} = \\frac{\\tilde{p}_1^2}{2m_1} + \\frac{\\tilde{p}_2^2}{2m_2} = \\frac{\\tilde{p}^2}{2}\\left(\\frac{1}{m_1} + \\frac{1}{m_2}\\right) = \\frac{\\tilde{p}^2}{2\\mu} = \\frac{1}{2}\\mu(v_1^2 + v_2^2)$$",
        "tags": ["center of mass", "reduced mass", "relative velocity"]
    },
    {
        "id": "1.175",
        "title": "Maximum Scattering Angle for $m_1 > m_2$",
        "difficulty": 2,
        "question": "A particle of mass $m_1$ collides elastically with a stationary particle of mass $m_2$ ($m_1 > m_2$). Find the maximum angle through which the striking particle may deviate as a result of the collision.",
        "hints": [
            "Transform to the center of inertia frame, where the speed of $m_1$ is $u_1 = \\frac{m_2}{m_1 + m_2}v_1$ and center of mass speed is $V_C = \\frac{m_1}{m_1 + m_2}v_1$.",
            "In velocity space, the laboratory velocity of $m_1$ is $\\mathbf{v}_1' = \\mathbf{V}_C + \\mathbf{u}_1'$, where $|\\mathbf{u}_1'| = u_1$.",
            "The maximum deflection angle occurs when the velocity vector $\\mathbf{v}_1'$ is tangent to the circle of radius $u_1$: $\\sin\\theta_{\\max} = \\frac{u_1}{V_C}$."
        ],
        "answer": "$\\sin\\theta_{\\max} = \\frac{m_2}{m_1}$",
        "solution": "**1. Center of Inertia Velocities:**\nThe velocity of the center of inertia is:\n$$V_C = \\frac{m_1}{m_1 + m_2}v_1$$\nIn the CM frame, the initial velocity of particle 1 is:\n$$u_1 = v_1 - V_C = \\frac{m_2}{m_1 + m_2}v_1$$\nIn an elastic collision, the speed of particle 1 in the CM frame is conserved: $|\\mathbf{u}_1'| = u_1$.\n\n**2. Velocity Vector Triangle:**\nThe laboratory velocity of particle 1 after collision is:\n$$\\mathbf{v}_1' = \\mathbf{V}_C + \\mathbf{u}_1'$$\nAs the scattering angle in the CM frame varies from $0$ to $\\pi$, the tip of vector $\\mathbf{v}_1'$ traces a circle of radius $u_1$ centered at the tip of vector $\\mathbf{V}_C$.\nSince $m_1 > m_2$, we have $V_C > u_1$, so the origin lies outside this circle.\n\n**3. Maximum Deflection Angle:**\nThe maximum angle $\\theta_{\\max}$ between $\\mathbf{v}_1'$ and the initial direction $\\mathbf{V}_C$ occurs when $\\mathbf{v}_1'$ is tangent to the circle:\n$$\\sin\\theta_{\\max} = \\frac{u_1}{V_C} = \\frac{\\frac{m_2}{m_1 + m_2}v_1}{\\frac{m_1}{m_1 + m_2}v_1} = \\frac{m_2}{m_1}$$",
        "tags": ["elastic collision", "scattering angle", "center of mass"]
    },
    {
        "id": "1.176",
        "title": "Three-Disc Simultaneous Elastic Collision",
        "difficulty": 3,
        "question": "Three identical discs $A, B,$ and $C$ rest on a smooth horizontal plane. The disc $A$ is set in motion with velocity $v$ after which it experiences an elastic collision simultaneously with the discs $B$ and $C$. The distance between the centres of the latter discs prior to the collision is $\\eta$ times greater than the diameter $d$ of each disc. Find the velocity of the disc $A$ after the collision. At what value of $\\eta$ will disc $A$ bounce back, stop, or move forward?",
        "hints": [
            "Let $\\alpha$ be the angle between the initial velocity $\\mathbf{v}$ of disc $A$ and the line of centers with each target disc at impact.",
            "From geometry of the three touching discs of diameter $d$: $\\sin\\alpha = \\frac{\\eta d}{2d} = \\frac{\\eta}{2}$.",
            "Apply conservation of momentum along the symmetry axis and kinetic energy conservation to solve for the rebound velocity $v'$ of disc $A$."
        ],
        "answer": "$v' = v\\frac{2 - \\eta^2}{6 - 2\\eta^2}$; disc $A$ bounces back if $\\eta > \\sqrt{2}$, stops if $\\eta = \\sqrt{2}$, and continues forward if $\\eta < \\sqrt{2}$",
        "solution": "**1. Collision Geometry:**\nAt the moment of simultaneous contact, disc $A$ touches both $B$ and $C$.\nThe distance between centers of $B$ and $C$ is $\\eta d$.\nThe distance from the center of $A$ to the line connecting centers of $B$ and $C$ forms a symmetric isosceles triangle with sides equal to $d$.\nThe angle $\\alpha$ that the line of centers makes with the transverse axis satisfies:\n$$\\sin\\alpha = \\frac{\\eta d / 2}{d} = \\frac{\\eta}{2}$$\nThe angle with the forward line of motion is therefore $\\cos\\alpha = \\sqrt{1 - \\eta^2/4}$.\n\n**2. Conservation Laws:**\nBy symmetry, discs $B$ and $C$ acquire equal speeds $u$ along the line of centers with disc $A$, making angle $\\alpha$ with the forward axis:\n- Momentum conservation along forward axis:\n  $$m v = m v' + 2 m u \\cos\\alpha \\implies v = v' + 2 u \\cos\\alpha$$\n- Energy conservation (elastic collision):\n  $$\\frac{1}{2}m v^2 = \\frac{1}{2}m {v'}^2 + 2 \\left(\\frac{1}{2}m u^2\\right) \\implies v^2 = {v'}^2 + 2 u^2$$\n\n**3. Solving for $v'$:**\nFrom momentum: $2u\\cos\\alpha = v - v' \\implies u = \\frac{v - v'}{2\\cos\\alpha}$.\nSubstitute into energy equation:\n$$v^2 - {v'}^2 = 2 \\left(\\frac{v - v'}{2\\cos\\alpha}\\right)^2 = \\frac{(v - v')^2}{2\\cos^2\\alpha}$$\nDividing by $(v - v') \\ne 0$:\n$$v + v' = \\frac{v - v'}{2\\cos^2\\alpha}$$\n$$2\\cos^2\\alpha (v + v') = v - v' \\implies v'(1 + 2\\cos^2\\alpha) = v(1 - 2\\cos^2\\alpha)$$\nSubstitute $\\cos^2\\alpha = 1 - \\frac{\\eta^2}{4}$:\n$$1 - 2\\cos^2\\alpha = 1 - 2\\left(1 - \\frac{\\eta^2}{4}\\right) = \\frac{\\eta^2}{2} - 1 = \\frac{\\eta^2 - 2}{2}$$\n$$1 + 2\\cos^2\\alpha = 1 + 2 - \\frac{\\eta^2}{2} = \\frac{6 - \\eta^2}{2}$$\n$$v' = v \\frac{2 - \\eta^2}{6 - 2\\eta^2}$$\n\n**4. Direction of Motion:**\n- If $\\eta < \\sqrt{2}$, $v' > 0$ (continues forward).\n- If $\\eta = \\sqrt{2}$, $v' = 0$ (stops).\n- If $\\eta > \\sqrt{2}$, $v' < 0$ (rebounds backward).",
        "tags": ["elastic collision", "three-body collision", "geometry of impact"]
    },
    {
        "id": "1.177",
        "title": "Divergence Angle of Two Colliding Molecules of Equal Mass",
        "difficulty": 2,
        "question": "A molecule collides with another, stationary, molecule of the same mass. Demonstrate that the angle of divergence:\n(a) equals $90^{\\circ}$ when the collision is ideally elastic;\n(b) differs from $90^{\\circ}$ when the collision is inelastic.",
        "hints": [
            "Let the incoming momentum be $\\mathbf{p}$ and scattered momenta be $\\mathbf{p}_1$ and $\\mathbf{p}_2$.",
            "From momentum conservation, $\\mathbf{p} = \\mathbf{p}_1 + \\mathbf{p}_2 \\implies p^2 = p_1^2 + p_2^2 + 2\\mathbf{p}_1 \\cdot \\mathbf{p}_2$.",
            "Relate $p^2$ to kinetic energies $T = \\frac{p^2}{2m}$ and examine the dot product $\\mathbf{p}_1 \\cdot \\mathbf{p}_2 = p_1 p_2 \\cos\\theta$."
        ],
        "answer": "(a) $\\theta = 90^{\\circ}$ for elastic collision; (b) $\\theta < 90^{\\circ}$ for inelastic collision (energy loss)",
        "solution": "**1. Momentum Conservation:**\nLet the incident molecule have momentum $\\mathbf{p}$ and the target molecule be initially at rest.\nAfter the collision, let their momenta be $\\mathbf{p}_1$ and $\\mathbf{p}_2$:\n$$\\mathbf{p} = \\mathbf{p}_1 + \\mathbf{p}_2$$\nSquaring both sides:\n$$p^2 = (\\mathbf{p}_1 + \\mathbf{p}_2)^2 = p_1^2 + p_2^2 + 2\\mathbf{p}_1 \\cdot \\mathbf{p}_2 = p_1^2 + p_2^2 + 2 p_1 p_2 \\cos\\theta$$\nwhere $\\theta$ is the divergence angle between the two final trajectories.\n\n**2. Relating to Kinetic Energy:**\nDividing by $2m$ (since both masses are equal to $m$):\n$$\\frac{p^2}{2m} = \\frac{p_1^2}{2m} + \\frac{p_2^2}{2m} + \\frac{p_1 p_2}{m}\\cos\\theta$$\n$$T_i = T_{1f} + T_{2f} + \\frac{p_1 p_2}{m}\\cos\\theta$$\n$$T_i - (T_{1f} + T_{2f}) = -\\frac{p_1 p_2}{m}\\cos\\theta$$\n\n**3. Elastic vs Inelastic Cases:**\n**(a) Ideally Elastic Collision:**\nKinetic energy is conserved: $T_i = T_{1f} + T_{2f}$.\n$$0 = -\\frac{p_1 p_2}{m}\\cos\\theta \\implies \\cos\\theta = 0 \\implies \\theta = 90^{\\circ}$$\n**(b) Inelastic Collision:**\nKinetic energy decreases ($T_i > T_{1f} + T_{2f} = T_f$):\n$$T_i - T_f = Q > 0 \\implies \\cos\\theta = \\frac{m Q}{p_1 p_2} > 0 \\implies \\theta < 90^{\\circ} \\ne 90^{\\circ}$$",
        "tags": ["elastic collision", "inelastic collision", "angle of divergence"]
    },
    {
        "id": "1.178",
        "title": "Meshchersky Equation for a Variable-Mass Rocket",
        "difficulty": 2,
        "question": "A rocket ejects a steady jet whose velocity is equal to $\\mathbf{u}$ relative to the rocket. The gas discharge rate equals $\\mu\\text{ kg/s}$. Demonstrate that the rocket motion equation in this case takes the form:\n$$m \\mathbf{w} = \\mathbf{F} - \\mu \\mathbf{u}$$\nwhere $m$ is the mass of the rocket at a given moment, $\\mathbf{w}$ is its acceleration, and $\\mathbf{F}$ is the external force.",
        "hints": [
            "Consider the rocket and ejected gas as a system over infinitesimal time $dt$.",
            "At time $t$, momentum is $m\\mathbf{v}$. At $t + dt$, rocket has mass $m + dm$ and velocity $\\mathbf{v} + d\\mathbf{v}$, and ejected mass $-dm = \\mu dt$ has velocity $\\mathbf{v} + \\mathbf{u}$.",
            "Equate the change in momentum $d\\mathbf{p}$ to the external impulse $\\mathbf{F} dt$."
        ],
        "answer": "$m \\mathbf{w} = \\mathbf{F} - \\mu \\mathbf{u}$ (Meshchersky's equation)",
        "solution": "**1. Impulse-Momentum Theorem for the Variable-Mass System:**\nConsider the rocket and the mass of gas ejected during the time interval $dt$ as a closed system regarding internal reactions.\n- At time $t$:\n  Total momentum is $\\mathbf{P}(t) = m\\mathbf{v}$.\n- At time $t + dt$:\n  The rocket mass becomes $m + dm$ (where $dm < 0$, so $|dm| = -dm = \\mu \\, dt$).\n  The velocity of the rocket becomes $\\mathbf{v} + d\\mathbf{v}$.\n  The ejected gas of mass $(-dm)$ has velocity $\\mathbf{v}_{\\text{gas}} = \\mathbf{v} + \\mathbf{u}$ relative to the reference frame, where $\\mathbf{u}$ is the velocity of the exhaust relative to the rocket.\n  The total momentum at $t + dt$ is:\n  $$\\mathbf{P}(t + dt) = (m + dm)(\\mathbf{v} + d\\mathbf{v}) + (-dm)(\\mathbf{v} + \\mathbf{u})$$\n\n**2. Expanding the Momentum Differential:**\nNeglecting the second-order differential $dm \\, d\\mathbf{v}$:\n$$\\mathbf{P}(t + dt) = m\\mathbf{v} + m \\, d\\mathbf{v} + \\mathbf{v} \\, dm - \\mathbf{v} \\, dm - \\mathbf{u} \\, dm = m\\mathbf{v} + m \\, d\\mathbf{v} - \\mathbf{u} \\, dm$$\n$$d\\mathbf{P} = \\mathbf{P}(t + dt) - \\mathbf{P}(t) = m \\, d\\mathbf{v} - \\mathbf{u} \\, dm$$\n\n**3. Equating to External Force Impulse:**\nBy Newton's second law: $d\\mathbf{P} = \\mathbf{F} \\, dt$:\n$$m \\, d\\mathbf{v} - \\mathbf{u} \\, dm = \\mathbf{F} \\, dt$$\nDividing by $dt$ and noting $\\mathbf{w} = \\frac{d\\mathbf{v}}{dt}$ and $\\frac{dm}{dt} = -\\mu$:\n$$m \\mathbf{w} = \\mathbf{F} + \\frac{dm}{dt}\\mathbf{u} = \\mathbf{F} - \\mu \\mathbf{u}$$",
        "tags": ["variable mass", "Meshchersky equation", "rocket dynamics"]
    },
    {
        "id": "1.179",
        "title": "Tsiolkovsky Rocket Equation in Free Space",
        "difficulty": 1,
        "question": "A rocket moves in the absence of external forces by ejecting a steady jet with velocity $u$ constant relative to the rocket. Find the velocity $v$ of the rocket at the moment when its mass is equal to $m$, if at the initial moment it possessed the mass $m_0$ and its velocity was equal to zero. Make use of the formula given in the foregoing problem.",
        "hints": [
            "In the absence of external forces, $\\mathbf{F} = 0$, so $m \\, dv = -u \\, dm$.",
            "Separate variables: $dv = -u \\frac{dm}{m}$.",
            "Integrate from $m_0$ (where $v=0$) to $m$."
        ],
        "answer": "$v = u \\ln\\frac{m_0}{m}$",
        "solution": "**1. Differential Equation of Motion:**\nFrom Meshchersky's equation with no external forces ($F = 0$) and exhaust directed backward relative to the rocket's forward motion ($u_{\\text{rel}} = -u$):\n$$m \\frac{dv}{dt} = -u \\frac{dm}{dt} \\implies m \\, dv = -u \\, dm$$\n\n**2. Integration:**\nSeparating variables:\n$$dv = -u \\frac{dm}{m}$$\nIntegrating from the initial state ($v = 0, m = m_0$) to the final state ($v, m$):\n$$\\int_0^v dv = -u \\int_{m_0}^m \\frac{dm'}{m'} = -u \\left(\\ln m - \\ln m_0\\right) = u \\ln\\frac{m_0}{m}$$\n$$v = u \\ln\\frac{m_0}{m}$$",
        "tags": ["Tsiolkovsky equation", "rocket dynamics", "variable mass"]
    },
    {
        "id": "1.180",
        "title": "Mass Consumption Law for Constant Acceleration Rocket",
        "difficulty": 2,
        "question": "Find the law according to which the mass of the rocket varies with time, when the rocket moves with a constant acceleration $w$, external forces are absent, the gas escapes with a constant velocity $u$ relative to the rocket, and its mass at the initial moment equals $m_0$.",
        "hints": [
            "From the rocket equation, $m w = -u \\frac{dm}{dt}$ since $w = \\text{const}$.",
            "Separate variables: $\\frac{dm}{m} = -\\frac{w}{u} \\, dt$.",
            "Integrate with initial condition $m(0) = m_0$."
        ],
        "answer": "$m(t) = m_0 e^{-wt/u}$",
        "solution": "**1. Rocket Equation with Constant Acceleration:**\nIn free space ($F_{\\text{ext}} = 0$), the thrust force accelerating the rocket forward is:\n$$m w = -u \\frac{dm}{dt}$$\nwhere $w$ is constant and $u$ is the constant exhaust velocity.\n\n**2. Separating Variables:**\n$$\\frac{dm}{m} = -\\frac{w}{u} \\, dt$$\n\n**3. Integration:**\nIntegrating from $t = 0$ (where $m = m_0$) to time $t$:\n$$\\int_{m_0}^m \\frac{dm'}{m'} = -\\frac{w}{u}\\int_0^t dt'$$\n$$\\ln\\frac{m}{m_0} = -\\frac{w t}{u}$$\n$$m(t) = m_0 e^{-wt/u}$$",
        "tags": ["variable mass", "rocket dynamics", "differential equations"]
    },
    {
        "id": "1.181",
        "title": "Angular Redirection Maneuver of a Spaceship",
        "difficulty": 2,
        "question": "A spaceship of mass $m_0$ moves in the absence of external forces with a constant velocity $v_0$. To change the motion direction, a jet engine is switched on. It starts ejecting a gas jet with velocity $u$ which is constant relative to the spaceship and directed at right angles to the spaceship motion. The engine is shut down when the mass of the spaceship decreases to $m$. Find the angle $\\alpha$ through which the velocity vector has turned.",
        "hints": [
            "Since the thrust is always perpendicular to velocity, the speed of the spaceship remains constant: $v = v_0$.",
            "The thrust provides centripetal acceleration: $m v_0 \\frac{d\\alpha}{dt} = -u \\frac{dm}{dt}$.",
            "Integrate to find the turn angle $\\alpha = \\frac{u}{v_0}\\ln\\frac{m_0}{m}$."
        ],
        "answer": "$\\alpha = \\frac{u}{v_0}\\ln\\frac{m_0}{m}$",
        "solution": "**1. Constancy of Speed:**\nThe thrust force $\\mathbf{F}_{\\text{th}} = -\\mathbf{u}\\frac{dm}{dt}$ is always directed at right angles to the instantaneous velocity vector $\\mathbf{v}$.\nBecause $\\mathbf{F}_{\\text{th}} \\perp \\mathbf{v}$, it performs zero work, and the magnitude of the velocity remains strictly constant:\n$$v(t) = v_0$$\n\n**2. Rate of Angular Deflection:**\nThe normal acceleration is $w_n = v_0 \\frac{d\\alpha}{dt}$.\nFrom Newton's second law for the variable mass:\n$$m w_n = F_{\\text{th}} \\implies m v_0 \\frac{d\\alpha}{dt} = -u \\frac{dm}{dt}$$\n\n**3. Integration:**\n$$d\\alpha = -\\frac{u}{v_0} \\frac{dm}{m}$$\nIntegrating from initial mass $m_0$ (angle $\\alpha = 0$) to final mass $m$:\n$$\\alpha = -\\frac{u}{v_0}\\int_{m_0}^m \\frac{dm'}{m'} = \\frac{u}{v_0}\\ln\\frac{m_0}{m}$$",
        "tags": ["variable mass", "trajectory deflection", "centripetal acceleration"]
    },
    {
        "id": "1.182",
        "title": "Motion of a Cart with Sand Leaking from Bottom",
        "difficulty": 2,
        "question": "A cart loaded with sand moves along a horizontal plane due to a constant force $F$ coinciding in direction with the cart's velocity vector. In the process, sand spills through a hole in the bottom with a constant rate $\\mu\\text{ kg/s}$. Find the acceleration and the velocity of the cart at the moment $t$, if at the initial moment $t = 0$ the cart with load had mass $m_0$ and its velocity was equal to zero. Friction is negligibly small.",
        "hints": [
            "Sand leaks through the bottom with zero velocity relative to the cart: $\\mathbf{u}_{\\text{rel}} = 0$.",
            "Since leaking sand carries no relative momentum, reactive force is zero: $m(t) w = F$.",
            "Integrate $w(t) = \\frac{F}{m_0 - \\mu t}$ to obtain velocity $v(t)$."
        ],
        "answer": "$w(t) = \\frac{F}{m_0 - \\mu t}$; $v(t) = \\frac{F}{\\mu}\\ln\\frac{m_0}{m_0 - \\mu t}$",
        "solution": "**1. Equation of Motion:**\nThe mass of the cart and remaining sand at time $t$ is $m(t) = m_0 - \\mu t$.\nThe spilled sand leaves the cart through the bottom with zero horizontal velocity relative to the cart ($\\mathbf{u} = 0$).\nTherefore, the reactive force is zero, and Meshchersky's equation reduces to:\n$$m(t) \\frac{dv}{dt} = F$$\n\n**2. Acceleration:**\n$$w(t) = \\frac{F}{m_0 - \\mu t}$$\n\n**3. Velocity as a Function of Time:**\n$$dv = \\frac{F}{m_0 - \\mu t} \\, dt$$\nIntegrating with $v(0) = 0$:\n$$v(t) = \\int_0^t \\frac{F}{m_0 - \\mu t'} \\, dt' = -\\frac{F}{\\mu}[\\ln(m_0 - \\mu t) - \\ln m_0] = \\frac{F}{\\mu}\\ln\\frac{m_0}{m_0 - \\mu t}$$",
        "tags": ["variable mass", "Newton's laws", "sand leakage"]
    },
    {
        "id": "1.183",
        "title": "Flatcar Accumulating Sand from a Stationary Hopper",
        "difficulty": 2,
        "question": "A flatcar of mass $m_0$ starts moving to the right due to a constant horizontal force $F$. Sand spills on the flatcar from a stationary hopper at a constant rate $\\mu\\text{ kg/s}$. Find the time dependence of the velocity and the acceleration of the flatcar in the process of loading. Friction is negligibly small.",
        "hints": [
            "Sand falls from a stationary hopper, so its initial horizontal velocity is zero: $\\mathbf{v}_{\\text{sand}} = 0$.",
            "The relative velocity of the falling sand with respect to the flatcar is $\\mathbf{u} = -\\mathbf{v}$.",
            "Write the momentum equation: $\\frac{d}{dt}[(m_0 + \\mu t)v] = F$."
        ],
        "answer": "$v(t) = \\frac{Ft}{m_0 + \\mu t}$; $w(t) = \\frac{F m_0}{(m_0 + \\mu t)^2}$",
        "solution": "**1. Momentum Equation for Mass Accumulation:**\nThe total mass at time $t$ is $m(t) = m_0 + \\mu t$.\nSince the falling sand has zero horizontal velocity before landing on the flatcar, the external horizontal force $F$ equals the rate of change of total momentum:\n$$\\frac{d}{dt}(m v) = F \\implies \\frac{d}{dt}[(m_0 + \\mu t)v] = F$$\n\n**2. Velocity as a Function of Time:**\nIntegrating with initial condition $v(0) = 0$:\n$$(m_0 + \\mu t)v = F t \\implies v(t) = \\frac{Ft}{m_0 + \\mu t}$$\n\n**3. Acceleration as a Function of Time:**\nDifferentiating $v(t)$ with respect to time:\n$$w(t) = \\frac{dv}{dt} = \\frac{F(m_0 + \\mu t) - Ft(\\mu)}{(m_0 + \\mu t)^2} = \\frac{F m_0}{(m_0 + \\mu t)^2}$$",
        "tags": ["variable mass", "momentum accumulation", "flatcar"]
    },
    {
        "id": "1.184",
        "title": "Chain Slipping out of a Smooth Horizontal Tube",
        "difficulty": 3,
        "question": "A chain $AB$ of length $l$ is located in a smooth horizontal tube so that its fraction of length $h$ hangs freely and touches the surface of the table with its end $B$. At a certain moment the end $A$ of the chain is set free. With what velocity will this end of the chain slip out of the tube?",
        "hints": [
            "As the chain moves, the length of the hanging vertical portion remains constantly equal to $h$ because links reaching the table come to rest.",
            "Let $x$ be the length of the horizontal chain remaining in the tube. The moving mass of chain is $\\lambda(x + h)$.",
            "Write the equation of motion taking into account momentum carried away by chain links landing on the table."
        ],
        "answer": "$v = \\sqrt{2gh\\ln(l/h)}$",
        "solution": "**1. Equation of Motion of the Moving Portion:**\nLet $x$ be the length of chain currently remaining in the horizontal tube.\nThe total length of the moving chain is $x + h$ (since the vertical hanging portion always has length $h$, with newly arriving links coming to rest on the table).\nThe mass of the moving chain is $m(x) = \\lambda(x + h)$, where $\\lambda = m/l$.\nThe weight of the vertical hanging portion driving the motion is:\n$$F = (\\lambda h)g$$\nSince links reaching the table leave the moving system with horizontal/vertical velocity $v$, the equation of motion is:\n$$\\lambda(x + h)\\frac{dv}{dt} = \\lambda h g$$\n\n**2. Converting to Spatial Derivative:**\nSince $v = -\\frac{dx}{dt}$ (as $x$ decreases from $l - h$ to $0$):\n$$\\frac{dv}{dt} = v \\frac{dv}{dx} \\left(-\\frac{dx}{dt} \\frac{1}{v}\\right) = -v \\frac{dv}{dx}$$\n$$-(x + h)v \\frac{dv}{dx} = gh \\implies v \\, dv = -\\frac{gh}{x + h} \\, dx$$\n\n**3. Integration:**\nIntegrating from $x = l - h$ (where $v = 0$) to $x = 0$:\n$$\\int_0^v v' \\, dv' = -gh \\int_{l-h}^0 \\frac{dx}{x + h}$$\n$$\\frac{1}{2}v^2 = -gh [\\ln h - \\ln l] = gh\\ln\\frac{l}{h}$$\n$$v = \\sqrt{2gh\\ln\\frac{l}{h}}$$",
        "tags": ["variable mass", "chain motion", "integration"]
    },
    {
        "id": "1.185",
        "title": "Torque for a Time-Varying Angular Momentum",
        "difficulty": 2,
        "question": "The angular momentum of a particle relative to a certain point $O$ varies with time as $\\mathbf{M} = \\mathbf{a} + \\mathbf{b}t^2$, where $\\mathbf{a}$ and $\\mathbf{b}$ are constant vectors, with $\\mathbf{a} \\perp \\mathbf{b}$. Find the torque $\\mathbf{N}$ relative to the point $O$ acting on the particle when the angle between the vectors $\\mathbf{N}$ and $\\mathbf{M}$ equals $45^{\\circ}$.",
        "hints": [
            "The torque is the time derivative of angular momentum: $\\mathbf{N} = \\frac{d\\mathbf{M}}{dt} = 2\\mathbf{b}t$.",
            "The dot product gives $\\mathbf{N} \\cdot \\mathbf{M} = NM\\cos 45^{\\circ}$.",
            "Since $\\mathbf{a} \\perp \\mathbf{b}$, $M^2 = a^2 + b^2 t^4$ and $\\mathbf{N} \\cdot \\mathbf{M} = 2b^2 t^3$. Solve for $t$."
        ],
        "answer": "$N = 2b\\sqrt{a/b} = 2\\sqrt{ab}$",
        "solution": "**1. Torque Vector:**\n$$\\mathbf{N} = \\frac{d\\mathbf{M}}{dt} = \\frac{d}{dt}(\\mathbf{a} + \\mathbf{b}t^2) = 2\\mathbf{b}t$$\nMagnitude of torque: $N = 2bt$.\n\n**2. Angle between $\\mathbf{N}$ and $\\mathbf{M}$:**\nSince $\\mathbf{a} \\perp \\mathbf{b}$, the magnitude squared of $\\mathbf{M}$ is:\n$$M^2 = a^2 + b^2 t^4$$\nThe dot product is:\n$$\\mathbf{N} \\cdot \\mathbf{M} = (2\\mathbf{b}t) \\cdot (\\mathbf{a} + \\mathbf{b}t^2) = 2(\\mathbf{a} \\cdot \\mathbf{b})t + 2b^2 t^3 = 2b^2 t^3$$\nOn the other hand:\n$$\\mathbf{N} \\cdot \\mathbf{M} = N M \\cos 45^{\\circ} = (2bt)\\sqrt{a^2 + b^2 t^4} \\cdot \\frac{1}{\\sqrt{2}}$$\n\n**3. Solving for $t$ and $N$:**\n$$2b^2 t^3 = \\sqrt{2}bt\\sqrt{a^2 + b^2 t^4}$$\nDividing by $\\sqrt{2}bt$:\n$$\\sqrt{2}bt^2 = \\sqrt{a^2 + b^2 t^4}$$\nSquaring both sides:\n$$2b^2 t^4 = a^2 + b^2 t^4 \\implies b^2 t^4 = a^2 \\implies t^2 = \\frac{a}{b} \\implies t = \\sqrt{\\frac{a}{b}}$$\nSubstituting $t$ into $N = 2bt$:\n$$N = 2b\\sqrt{\\frac{a}{b}} = 2\\sqrt{ab}$$",
        "tags": ["angular momentum", "torque", "vectors"]
    },
    {
        "id": "1.186",
        "title": "Angular Momentum of a Projectile Relative to Launch Point",
        "difficulty": 2,
        "question": "A ball of mass $m$ is thrown at an angle $\\alpha$ to the horizontal with the initial velocity $v_0$. Find the time dependence of the magnitude of the ball's angular momentum vector relative to the point from which the ball is thrown. Find the angular momentum $M$ at the highest point of the trajectory if $m = 130\\text{ g}, \\alpha = 45^{\\circ},$ and $v_0 = 25\\text{ m/s}$. The air drag is to be neglected.",
        "hints": [
            "Use torque definition: $\\frac{d\\mathbf{M}}{dt} = \\mathbf{N} = \\mathbf{r} \\times m\\mathbf{g}$.",
            "Coordinates are $x(t) = (v_0\\cos\\alpha)t, y(t) = (v_0\\sin\\alpha)t - \\frac{1}{2}gt^2$.",
            "Compute torque magnitude $N = mg x(t) = mg(v_0\\cos\\alpha)t$ and integrate from $0$ to $t$."
        ],
        "answer": "$M(t) = \\frac{1}{2}mgv_0 t^2\\cos\\alpha$; $M_{\\text{apex}} = \\frac{m v_0^3 \\sin^2\\alpha\\cos\\alpha}{2g} \\approx 37\\text{ kg}\\cdot\\text{m}^2/\\text{s}$",
        "solution": "**1. Torque about Launch Point:**\nPosition vector: $\\mathbf{r}(t) = x(t)\\hat{\\mathbf{i}} + y(t)\\hat{\\mathbf{j}}$, where $x(t) = (v_0\\cos\\alpha)t$.\nGravity acts downward: $\\mathbf{F}_g = -mg\\hat{\\mathbf{j}}$.\nThe torque about the origin is:\n$$\\mathbf{N} = \\mathbf{r} \\times \\mathbf{F}_g = (x\\hat{\\mathbf{i}} + y\\hat{\\mathbf{j}}) \\times (-mg\\hat{\\mathbf{j}}) = -mg x(t) \\hat{\\mathbf{k}} = -mg(v_0\\cos\\alpha)t \\hat{\\mathbf{k}}$$\n\n**2. Angular Momentum $M(t)$:**\nSince $\\mathbf{M}(0) = 0$:\n$$\\mathbf{M}(t) = \\int_0^t \\mathbf{N}(t') \\, dt' = -mg(v_0\\cos\\alpha)\\left(\\frac{t^2}{2}\\right)\\hat{\\mathbf{k}}$$\nMagnitude:\n$$M(t) = \\frac{1}{2}mg v_0 t^2 \\cos\\alpha$$\n\n**3. Angular Momentum at Apex:**\nThe time to reach the highest point is $t_H = \\frac{v_0\\sin\\alpha}{g}$:\n$$M(t_H) = \\frac{1}{2}mg v_0 \\left(\\frac{v_0\\sin\\alpha}{g}\\right)^2 \\cos\\alpha = \\frac{m v_0^3 \\sin^2\\alpha \\cos\\alpha}{2g}$$\nWith $m = 0.130\\text{ kg}, v_0 = 25\\text{ m/s}, \\alpha = 45^{\\circ}, g = 9.8\\text{ m/s}^2$:\n$$M = \\frac{0.130 \\times 25^3 \\times (1/\\sqrt{2})^2 \\times (1/\\sqrt{2})}{2 \\times 9.8} = \\frac{0.130 \\times 15625 \\times 0.50 \\times 0.7071}{19.6} = \\frac{718.2}{19.6} \\approx 36.6 \\approx 37\\text{ kg}\\cdot\\text{m}^2/\\text{s}$$",
        "tags": ["angular momentum", "projectile motion", "torque"]
    },
    {
        "id": "1.187",
        "title": "Angular Momentum Conservation for Disc Colliding with Wall",
        "difficulty": 2,
        "question": "A disc $A$ of mass $m$ sliding over a smooth horizontal surface with velocity $v$ experiences a perfectly elastic collision with a smooth stationary wall at a point $O$. The angle between the motion direction of the disc and the normal of the wall is equal to $\\alpha$. Find:\n(a) the points relative to which the angular momentum $\\mathbf{M}$ of the disc remains constant in this process;\n(b) the magnitude of the increment of the vector of the disc's angular momentum relative to the point $O'$ which is located in the plane of the disc's motion at the distance $l$ from the point $O$.",
        "hints": [
            "For (a), torque during collision is $\\mathbf{N} = \\mathbf{r} \\times \\mathbf{F}$. Force from smooth wall acts purely normal to the wall at $O$.",
            "Torque vanishes if $\\mathbf{r} \\parallel \\mathbf{F}$, which corresponds to the normal line through $O$.",
            "For (b), $\\Delta \\mathbf{M} = \\mathbf{r}_{O'} \\times \\Delta \\mathbf{p}$. Normal momentum changes by $2mv\\cos\\alpha$."
        ],
        "answer": "(a) Relative to all points on the straight line drawn normal to the wall through point $O$; (b) $|\\Delta \\mathbf{M}| = 2mvl\\cos\\alpha$",
        "solution": "**(a) Points of Constant Angular Momentum:**\nDuring the collision, the only force exerted on the disc by the smooth wall is the normal reaction force $\\mathbf{N}_{\\text{wall}}$, acting along the normal to the wall through the collision point $O$.\nThe torque about an arbitrary reference point $P$ is:\n$$\\mathbf{N}_P = \\mathbf{r}_P \\times \\mathbf{N}_{\\text{wall}}$$\nThis torque is zero if and only if $\\mathbf{r}_P$ is collinear with $\\mathbf{N}_{\\text{wall}}$.\nTherefore, angular momentum is conserved relative to **all points on the straight line drawn at right angles to the wall through the point $O$**.\n\n**(b) Magnitude of Increment $|\\Delta \\mathbf{M}|$ relative to $O'$:**\nThe impulse of the collision force changes the momentum by:\n$$\\Delta \\mathbf{p} = \\mathbf{p}_f - \\mathbf{p}_i = 2mv\\cos\\alpha \\, \\hat{\\mathbf{n}}$$\nwhere $\\hat{\\mathbf{n}}$ is the inward normal to the wall.\nThe increment of angular momentum relative to $O'$ (at distance $l$ along the wall from $O$) is:\n$$\\Delta \\mathbf{M} = \\mathbf{r}_{O'O} \\times \\Delta \\mathbf{p}$$\nSince $\\mathbf{r}_{O'O}$ has length $l$ along the wall (perpendicular to $\\hat{\\mathbf{n}}$):\n$$|\\Delta \\mathbf{M}| = l |\\Delta \\mathbf{p}| = 2mvl\\cos\\alpha$$",
        "tags": ["angular momentum", "elastic collision", "torque"]
    },
    {
        "id": "1.188",
        "title": "Angular Momentum Increment of a Conical Pendulum",
        "difficulty": 2,
        "question": "A small ball of mass $m$ suspended from the ceiling at a point $O$ by a thread of length $l$ moves along a horizontal circle with a constant angular velocity $\\omega$. Relative to which points does the angular momentum $\\mathbf{M}$ of the ball remain constant? Find the magnitude of the increment of the vector of the ball's angular momentum relative to the point $O$ picked up during half a revolution.",
        "hints": [
            "Net force on the ball is directed horizontally towards the center of the circle $C$.",
            "Torque $\\mathbf{N}_P = \\mathbf{r}_P \\times \\mathbf{F}_{\\text{net}} = 0$ if $P$ is the center of the circle.",
            "Relative to $O$, angular momentum rotates on a cone. After half a revolution, its horizontal component reverses sign: $|\\Delta \\mathbf{M}| = 2 M_h$."
        ],
        "answer": "Relative to the centre of the circle; $|\\Delta \\mathbf{M}| = 2mgl\\sqrt{\\frac{l}{g}\\left[1 - \\left(\\frac{g}{\\omega^2 l}\\right)^2\\right]} = \\frac{2mgl}{\\omega}\\sqrt{1 - \\left(\\frac{g}{\\omega^2 l}\\right)^2}$",
        "solution": "**1. Points of Constant Angular Momentum:**\nThe resultant force acting on the ball is the centripetal force directed toward the center $C$ of the horizontal circle.\nThe torque of this resultant force vanishes about any point lying along the line of action, specifically the **center of the circle**.\n\n**2. Angular Momentum Vector relative to Point $O$:**\nLet the thread make angle $\\theta$ with the vertical, so radius is $R = l\\sin\\theta$ and height below $O$ is $h = l\\cos\\theta$.\nThe velocity has magnitude $v = \\omega R = \\omega l\\sin\\theta$.\nThe angular momentum relative to $O$ is:\n$$\\mathbf{M} = \\mathbf{r} \\times m\\mathbf{v}$$\nSince $\\mathbf{r} \\perp \\mathbf{v}$, the magnitude is $M = m v l = m \\omega l^2 \\sin\\theta$.\nThe vector $\\mathbf{M}$ is perpendicular to the thread and precesses around the vertical axis at rate $\\omega$, making angle $\\theta$ with the horizontal.\nIts horizontal component has magnitude $M_h = M\\cos\\theta = m\\omega l^2 \\sin\\theta\\cos\\theta$.\n\n**3. Increment over Half a Revolution:**\nDuring half a revolution, the vertical component of $\\mathbf{M}$ is unchanged, while the horizontal component completely reverses direction:\n$$|\\Delta \\mathbf{M}| = 2 M_h = 2m\\omega l^2 \\sin\\theta\\cos\\theta$$\nUsing the conical pendulum relation $\\cos\\theta = \\frac{g}{\\omega^2 l}$ and $\\sin\\theta = \\sqrt{1 - \\cos^2\\theta}$:\n$$|\\Delta \\mathbf{M}| = 2m\\omega l^2 \\left(\\frac{g}{\\omega^2 l}\\right)\\sqrt{1 - \\left(\\frac{g}{\\omega^2 l}\\right)^2} = \\frac{2mgl}{\\omega}\\sqrt{1 - \\left(\\frac{g}{\\omega^2 l}\\right)^2}$$",
        "tags": ["angular momentum", "conical pendulum", "precession"]
    },
    {
        "id": "1.189",
        "title": "Angular Momentum of a Falling Ball in a Moving Frame",
        "difficulty": 2,
        "question": "A ball of mass $m$ falls down without initial velocity from a height $h$ over the Earth's surface. Find the increment of the ball's angular momentum vector picked up during the time of falling (relative to the point $O$ of the reference frame moving translationally in a horizontal direction with a velocity $V$). The ball starts falling from the point $O$. The air drag is to be neglected.",
        "hints": [
            "In the moving frame, the ball has initial horizontal velocity $-V$.",
            "At time $t$, horizontal position relative to $O$ is $x(t) = -Vt$ and vertical position is $y(t) = -\\frac{1}{2}gt^2$.",
            "Torque about $O$ is $\\mathbf{N} = \\mathbf{r} \\times (-mg\\hat{\\mathbf{j}}) = -mg x(t)\\hat{\\mathbf{k}} = mgVt\\hat{\\mathbf{k}}$. Integrate over time of fall."
        ],
        "answer": "$|\\Delta \\mathbf{M}| = m V h$",
        "solution": "**1. Motion in the Moving Reference Frame:**\nThe reference frame translates horizontally with constant velocity $V$.\nIn this frame, the ball is dropped at $t = 0$ from the origin $O$ with initial velocity $\\mathbf{v}_0 = -V\\hat{\\mathbf{i}}$.\nIts coordinates at time $t$ are:\n$$x(t) = -Vt, \\quad y(t) = -\\frac{1}{2}gt^2$$\n\n**2. Torque about Point $O$:**\nGravity acts vertically: $\\mathbf{F}_g = -mg\\hat{\\mathbf{j}}$.\nThe torque about the origin is:\n$$\\mathbf{N}(t) = \\mathbf{r}(t) \\times \\mathbf{F}_g = (-Vt\\hat{\\mathbf{i}} + y\\hat{\\mathbf{j}}) \\times (-mg\\hat{\\mathbf{j}}) = mgVt \\hat{\\mathbf{k}}$$\n\n**3. Angular Momentum Increment:**\nIntegrating torque over the duration of the fall $\\tau = \\sqrt{\\frac{2h}{g}}$:\n$$\\Delta \\mathbf{M} = \\int_0^\\tau \\mathbf{N}(t) \\, dt = mgV\\left(\\frac{\\tau^2}{2}\\right)\\hat{\\mathbf{k}}$$\nSubstitute $\\tau^2 = \\frac{2h}{g}$:\n$$|\\Delta \\mathbf{M}| = mgV \\left(\\frac{2h}{2g}\\right) = mVh$$",
        "tags": ["angular momentum", "moving reference frame", "torque"]
    },
    {
        "id": "1.190",
        "title": "Angular Momentum on a Rotating Disc and Coriolis Force",
        "difficulty": 2,
        "question": "A smooth horizontal disc rotates with a constant angular velocity $\\omega$ about a stationary vertical axis passing through its centre, the point $O$. At a moment $t = 0$ a small body is set in motion from that point with velocity $v_0$. Find the angular momentum $M(t)$ of the body relative to the point $O$ in the reference frame fixed to the disc. Make sure that this angular momentum is caused by the Coriolis force.",
        "hints": [
            "In the rotating frame, the body experiences centrifugal force and Coriolis force: $\\mathbf{F}_{\\text{cor}} = 2m(\\mathbf{v}' \\times \\boldsymbol{\\omega})$.",
            "Centrifugal force is purely radial, so its torque about $O$ is zero.",
            "Only Coriolis force produces torque about $O$: $N = r F_{\\text{cor},\\perp} = 2m\\omega v_0^2 t$."
        ],
        "answer": "$M(t) = m\\omega v_0^2 t^2$",
        "solution": "**1. Kinematics in the Rotating Frame:**\nTo first order in displacement from the center $O$, the radial velocity is $v_r \\approx v_0$, so $r(t) = v_0 t$.\n\n**2. Forces and Torque in the Rotating Frame:**\nIn the rotating frame, two inertial forces act on the body:\n- Centrifugal force: $\\mathbf{F}_{\\text{cf}} = m\\omega^2 \\mathbf{r}$, which is purely radial, so $\\mathbf{r} \\times \\mathbf{F}_{\\text{cf}} = 0$.\n- Coriolis force: $\\mathbf{F}_{\\text{cor}} = 2m(\\mathbf{v}' \\times \\boldsymbol{\\omega})$.\nWith $\\mathbf{v}' \\approx v_0 \\hat{\\mathbf{r}}$ and $\\boldsymbol{\\omega} = \\omega \\hat{\\mathbf{k}}$:\n$$\\mathbf{F}_{\\text{cor}} = 2m(v_0 \\hat{\\mathbf{r}} \\times \\omega \\hat{\\mathbf{k}}) = -2m\\omega v_0 \\hat{\\boldsymbol{\\theta}}$$\n\n**3. Torque and Angular Momentum:**\nThe torque exerted by the Coriolis force about the center $O$ is:\n$$\\mathbf{N} = \\mathbf{r} \\times \\mathbf{F}_{\\text{cor}} = (v_0 t \\hat{\\mathbf{r}}) \\times (-2m\\omega v_0 \\hat{\\boldsymbol{\\theta}}) = -2m\\omega v_0^2 t \\hat{\\mathbf{k}}$$\nSince the body was released from $O$ at $t=0$, $\\mathbf{M}(0) = 0$.\n$$M(t) = \\int_0^t N(t') \\, dt' = \\int_0^t 2m\\omega v_0^2 t' \\, dt' = m\\omega v_0^2 t^2$$\nThis confirms that the angular momentum is generated exclusively by the **Coriolis force**.",
        "tags": ["rotating frame", "Coriolis force", "angular momentum"]
    },
    {
        "id": "1.191",
        "title": "Mass Determination in a Central Field $U = kr^2$",
        "difficulty": 2,
        "question": "A particle moves along a closed trajectory in a central field of force where the particle's potential energy is $U = kr^2$ ($k$ is a positive constant, $r$ is the distance of the particle from the centre $O$ of the field). Find the mass of the particle if its minimum distance from the point $O$ equals $r_1$ and its velocity at the point farthest from $O$ equals $v_2$.",
        "hints": [
            "At the turning points (periapsis $r_1$ and apoapsis $r_2$), radial velocity is zero: $v_r = 0$.",
            "Angular momentum conservation gives $m r_1 v_1 = m r_2 v_2 \\implies v_1 = \\frac{r_2}{r_1}v_2$.",
            "Energy conservation between $r_1$ and $r_2$: $\\frac{1}{2}m v_1^2 + k r_1^2 = \\frac{1}{2}m v_2^2 + k r_2^2$."
        ],
        "answer": "$m = \\frac{2kr_1^2}{v_2^2}$",
        "solution": "**1. Conservation Laws in Central Field:**\nAt the closest distance $r_1$ and farthest distance $r_2$, the velocity vector is purely transverse ($v_r = 0$).\n- Conservation of angular momentum:\n  $$m r_1 v_1 = m r_2 v_2 \\implies v_1 = \\frac{r_2}{r_1}v_2$$\n- Conservation of mechanical energy:\n  $$\\frac{1}{2}m v_1^2 + k r_1^2 = \\frac{1}{2}m v_2^2 + k r_2^2$$\n\n**2. Expressing Energy Relation:**\n$$\\frac{1}{2}m(v_1^2 - v_2^2) = k(r_2^2 - r_1^2)$$\nSubstitute $v_1 = \\frac{r_2}{r_1}v_2$:\n$$\\frac{1}{2}m v_2^2 \\left( \\frac{r_2^2}{r_1^2} - 1 \\right) = k(r_2^2 - r_1^2)$$\n$$\\frac{1}{2}m v_2^2 \\left( \\frac{r_2^2 - r_1^2}{r_1^2} \\right) = k(r_2^2 - r_1^2)$$\nSince $r_2 \\ne r_1$, we cancel $(r_2^2 - r_1^2)$:\n$$\\frac{1}{2}m \\frac{v_2^2}{r_1^2} = k \\implies m = \\frac{2kr_1^2}{v_2^2}$$",
        "tags": ["central force", "angular momentum", "energy conservation"]
    },
    {
        "id": "1.192",
        "title": "Initial Velocity of a Conical Pendulum for $90^{\\circ}$ Deflection",
        "difficulty": 3,
        "question": "A small ball is suspended from a point $O$ by a light thread of length $l$. Then the ball is drawn aside so that the thread deviates through an angle $\\theta$ from the vertical and set in motion in a horizontal direction at right angles to the vertical plane in which the thread is located. What is the initial velocity $v_0$ that has to be imparted to the ball so that it could deviate through the maximum angle $\\pi/2$ in the process of motion?",
        "hints": [
            "Use angular momentum conservation about the vertical axis passing through $O$: $M_z = m(l\\sin\\theta) v_0 = \\text{const}$.",
            "At the maximum deflection angle $\\pi/2$, the thread is horizontal, so $r = l$ and velocity is purely vertical or horizontal.",
            "Apply mechanical energy conservation between the initial state and the state at angle $\\pi/2$."
        ],
        "answer": "$v_0 = \\sqrt{\\frac{2gl}{\\cos\\theta}}$",
        "solution": "**1. Angular Momentum Conservation about the Vertical Axis:**\nThe forces acting on the ball are gravity (vertical) and thread tension (directed toward $O$).\nBoth forces exert zero torque about the vertical axis passing through $O$.\nTherefore, the component of angular momentum along the vertical axis is conserved:\n$$M_z = m(l\\sin\\theta)v_0 = \\text{const}$$\n\n**2. State at Maximum Deflection ($\\theta = \\pi/2$):**\nWhen the thread reaches the horizontal position ($\\theta_2 = \\pi/2$):\n- The horizontal distance from the vertical axis is $R_2 = l$.\n- At the maximum turning point, the radial angle rate is momentarily zero, so all velocity is azimuthal: $v_2 = \\frac{M_z}{ml} = \\frac{l\\sin\\theta v_0}{l} = v_0\\sin\\theta$.\n\n**3. Energy Conservation:**\nThe initial height above the lowest point is $h_1 = l(1 - \\cos\\theta)$.\nThe height at the horizontal position is $h_2 = l$.\nThe rise in potential energy is $\\Delta U = mgl - mgl(1 - \\cos\\theta) = mgl\\cos\\theta$.\n$$\\frac{1}{2}m v_0^2 = \\frac{1}{2}m v_2^2 + mgl\\cos\\theta$$\n$$\\frac{1}{2}v_0^2 = \\frac{1}{2}(v_0\\sin\\theta)^2 + gl\\cos\\theta$$\n$$\\frac{1}{2}v_0^2(1 - \\sin^2\\theta) = gl\\cos\\theta$$\n$$\\frac{1}{2}v_0^2\\cos^2\\theta = gl\\cos\\theta \\implies v_0^2 = \\frac{2gl}{\\cos\\theta}$$\n$$v_0 = \\sqrt{\\frac{2gl}{\\cos\\theta}}$$",
        "tags": ["angular momentum", "spherical pendulum", "energy conservation"]
    },
    {
        "id": "1.193",
        "title": "Thread Tension for Mass Drawn into Central Hole",
        "difficulty": 2,
        "question": "A small body of mass $m$ tied to a non-stretchable thread moves over a smooth horizontal plane. The other end of the thread is being drawn into a hole $O$ with a constant velocity. Find the thread tension as a function of the distance $r$ between the body and the hole if at $r = r_0$ the angular velocity of the thread is equal to $\\omega_0$.",
        "hints": [
            "The thread tension is directed radially toward the hole, so torque about $O$ is zero.",
            "Angular momentum is conserved: $M = m r^2 \\omega = m r_0^2 \\omega_0$.",
            "The thread tension provides centripetal acceleration: $T = m\\omega^2 r = \\frac{M^2}{m r^3}$."
        ],
        "answer": "$T(r) = \\frac{m \\omega_0^2 r_0^4}{r^3}$",
        "solution": "**1. Conservation of Angular Momentum:**\nSince the tension force $\\mathbf{T}$ acts along the radius vector $\\mathbf{r}$ directly toward the hole $O$, the torque about $O$ is zero:\n$$\\mathbf{N} = \\mathbf{r} \\times \\mathbf{T} = 0 \\implies M_z = m r^2 \\omega = \\text{const}$$\nUsing initial conditions at $r = r_0$:\n$$m r^2 \\omega = m r_0^2 \\omega_0 \\implies \\omega(r) = \\omega_0 \\left(\\frac{r_0}{r}\\right)^2$$\n\n**2. Thread Tension:**\nThe tension provides the centripetal acceleration for circular motion of instantaneous radius $r$ (since radial speed $\\dot{r} = \\text{const} \\implies \\ddot{r} = 0$):\n$$T = m \\omega^2 r = m \\left[\\omega_0 \\left(\\frac{r_0}{r}\\right)^2\\right]^2 r = \\frac{m \\omega_0^2 r_0^4}{r^3}$$",
        "tags": ["central force", "angular momentum", "tension"]
    },
    {
        "id": "1.194",
        "title": "Angular Momentum of Falling Mass Unwinding Thread from Pulley",
        "difficulty": 1,
        "question": "A light non-stretchable thread is wound on a massive fixed pulley of radius $R$. A small body of mass $m$ is tied to the free end of the thread. At a moment $t = 0$ the system is released and starts moving. Find its angular momentum relative to the pulley axle as a function of time $t$.",
        "hints": [
            "Consider the whole system (pulley + thread + body).",
            "The only external force exerting torque about the pulley axle is gravity $mg$ acting on the body at moment arm $R$.",
            "Torque is constant: $N = mgR$. Integrate $\\frac{dM}{dt} = N$."
        ],
        "answer": "$M(t) = R m g t$",
        "solution": "**1. Torque about the Pulley Axle:**\nThe only external force with a non-zero lever arm about the pulley axle is the force of gravity $mg$ acting vertically on the suspended mass $m$.\nThe lever arm of this gravitational force about the axle is the pulley radius $R$:\n$$N = mg R = \\text{const}$$\n\n**2. Angular Momentum:**\nBy the rotational form of Newton's second law:\n$$\\frac{dM}{dt} = N = mg R$$\nSince the system is released from rest at $t = 0$ ($M(0) = 0$):\n$$M(t) = \\int_0^t N \\, dt' = R m g t$$",
        "tags": ["angular momentum", "torque", "rotational dynamics"]
    },
    {
        "id": "1.195",
        "title": "Angular Momentum of a Sphere Rolling down an Incline",
        "difficulty": 2,
        "question": "A uniform sphere of mass $m$ and radius $R$ starts rolling without slipping down an inclined plane at an angle $\\alpha$ to the horizontal. Find the time dependence of the angular momentum of the sphere relative to the point of contact at the initial moment. How will the obtained result change in the case of a perfectly smooth inclined plane?",
        "hints": [
            "Let $O$ be the initial point of contact on the incline.",
            "The line of action of gravity $mg$ passes at perpendicular distance from $O$ equal to $(R\\sin\\alpha + \\dots)$ or compute torque.",
            "Torque about $O$ is $N = mg R\\sin\\alpha$. Integrate over time."
        ],
        "answer": "$M(t) = R m g t \\sin\\alpha$; the result will not change for a perfectly smooth inclined plane.",
        "solution": "**1. Torque about Initial Contact Point $O$:**\nLet $O$ be the initial point of contact on the incline plane at $t = 0$.\nAt any subsequent time $t$, the forces acting on the sphere are:\n- Normal reaction $N$ and friction $f_{\\text{fr}}$ acting at the moving contact point.\n- Gravity $mg$ acting at the center of mass.\nThe torque of gravity about $O$ is:\n$$\\mathbf{N}_O = \\mathbf{r}_C \\times m\\mathbf{g}$$\nThe distance from the center of mass to the plane is $R$. The component of gravity along the incline is $mg\\sin\\alpha$, with lever arm $R$ relative to the plane containing $O$:\n$$N_O = (mg\\sin\\alpha)R = Rmg\\sin\\alpha$$\n\n**2. Angular Momentum $M(t)$:**\n$$\\frac{dM}{dt} = N_O = Rmg\\sin\\alpha \\implies M(t) = R m g t \\sin\\alpha$$\n\n**3. Perfectly Smooth Incline:**\nOn a perfectly smooth plane, friction is zero, so the sphere slips without rolling. However, the external forces and their lever arms about $O$ are identical, so the torque of the external forces about $O$ remains $N_O = Rmg\\sin\\alpha$.\nTherefore, the time dependence of angular momentum $M(t)$ **will not change**.",
        "tags": ["angular momentum", "rolling without slipping", "torque"]
    },
    {
        "id": "1.196",
        "title": "Transformation of Angular Momentum between Reference Points",
        "difficulty": 1,
        "question": "A certain system of particles possesses a total momentum $\\mathbf{p}$ and an angular momentum $\\mathbf{M}$ relative to a point $O$. Find its angular momentum $\\mathbf{M}'$ relative to a point $O'$ whose position with respect to the point $O$ is determined by the radius vector $\\mathbf{r}_0$. Find out when the angular momentum of the system of particles does not depend on the choice of the point $O$.",
        "hints": [
            "Position of particle $i$ relative to $O'$ is $\\mathbf{r}_i' = \\mathbf{r}_i - \\mathbf{r}_0$.",
            "Substitute into $\\mathbf{M}' = \\sum \\mathbf{r}_i' \\times \\mathbf{p}_i$.",
            "Determine the condition under which the $\\mathbf{r}_0$-dependent term vanishes."
        ],
        "answer": "$\\mathbf{M}' = \\mathbf{M} - \\mathbf{r}_0 \\times \\mathbf{p}$; $\\mathbf{M}$ is independent of the reference point when $\\mathbf{p} = 0$ (e.g. in the centre of inertia frame)",
        "solution": "**1. Angular Momentum Transformation:**\nLet $\\mathbf{r}_i$ and $\\mathbf{r}_i'$ be the position vectors of particle $i$ relative to points $O$ and $O'$, respectively:\n$$\\mathbf{r}_i' = \\mathbf{r}_i - \\mathbf{r}_0$$\nThe angular momentum relative to $O'$ is:\n$$\\mathbf{M}' = \\sum_i \\mathbf{r}_i' \\times \\mathbf{p}_i = \\sum_i (\\mathbf{r}_i - \\mathbf{r}_0) \\times \\mathbf{p}_i = \\sum_i (\\mathbf{r}_i \\times \\mathbf{p}_i) - \\mathbf{r}_0 \\times \\sum_i \\mathbf{p}_i$$\n$$\\mathbf{M}' = \\mathbf{M} - \\mathbf{r}_0 \\times \\mathbf{p}$$\n\n**2. Condition for Point Independence:**\n$\\mathbf{M}' = \\mathbf{M}$ for any choice of vector $\\mathbf{r}_0$ if and only if:\n$$\\mathbf{r}_0 \\times \\mathbf{p} = 0 \\quad \\forall \\mathbf{r}_0 \\iff \\mathbf{p} = 0$$\nThus, the angular momentum is independent of the reference origin when the **total linear momentum of the system is zero** (i.e. in the centre of inertia reference frame).",
        "tags": ["angular momentum", "reference frame transformation", "center of mass"]
    },
    {
        "id": "1.197",
        "title": "Koenig's Theorem for Angular Momentum",
        "difficulty": 2,
        "question": "Demonstrate that the angular momentum $\\mathbf{M}$ of a system of particles relative to a point $O$ of the reference frame $K$ can be represented as:\n$$\\mathbf{M} = \\tilde{\\mathbf{M}} + \\mathbf{r}_C \\times \\mathbf{p}$$\nwhere $\\tilde{\\mathbf{M}}$ is its proper angular momentum (in the reference frame moving translationally and fixed to the centre of inertia), $\\mathbf{r}_C$ is the radius vector of the centre of inertia relative to the point $O$, and $\\mathbf{p}$ is the total momentum of the system of particles in the reference frame $K$.",
        "hints": [
            "Write the position of particle $i$ as $\\mathbf{r}_i = \\mathbf{r}_C + \\tilde{\\mathbf{r}}_i$.",
            "Write the velocity as $\\mathbf{v}_i = \\mathbf{v}_C + \\tilde{\\mathbf{v}}_i$.",
            "Expand the cross product $\\sum m_i (\\mathbf{r}_C + \\tilde{\\mathbf{r}}_i) \\times (\\mathbf{v}_C + \\tilde{\\mathbf{v}}_i)$ and use $\\sum m_i \\tilde{\\mathbf{r}}_i = 0$ and $\\sum m_i \\tilde{\\mathbf{v}}_i = 0$."
        ],
        "answer": "$\\mathbf{M} = \\tilde{\\mathbf{M}} + \\mathbf{r}_C \\times \\mathbf{p}$ (Koenig's theorem for angular momentum)",
        "solution": "**1. Coordinates Relative to Center of Inertia:**\nLet $\\mathbf{r}_C$ and $\\mathbf{v}_C$ be the position and velocity of the center of inertia in frame $K$.\nFor particle $i$ of mass $m_i$:\n$$\\mathbf{r}_i = \\mathbf{r}_C + \\tilde{\\mathbf{r}}_i, \\quad \\mathbf{v}_i = \\mathbf{v}_C + \\tilde{\\mathbf{v}}_i$$\nBy definition of the center of inertia:\n$$\\sum_i m_i \\tilde{\\mathbf{r}}_i = 0, \\quad \\sum_i m_i \\tilde{\\mathbf{v}}_i = 0$$\n\n**2. Expanding Angular Momentum $\\mathbf{M}$:**\n$$\\mathbf{M} = \\sum_i m_i (\\mathbf{r}_i \\times \\mathbf{v}_i) = \\sum_i m_i [(\\mathbf{r}_C + \\tilde{\\mathbf{r}}_i) \\times (\\mathbf{v}_C + \\tilde{\\mathbf{v}}_i)]$$\n$$\\mathbf{M} = \\sum_i m_i (\\mathbf{r}_C \\times \\mathbf{v}_C) + \\sum_i m_i (\\mathbf{r}_C \\times \\tilde{\\mathbf{v}}_i) + \\sum_i m_i (\\tilde{\\mathbf{r}}_i \\times \\mathbf{v}_C) + \\sum_i m_i (\\tilde{\\mathbf{r}}_i \\times \\tilde{\\mathbf{v}}_i)$$\n\n**3. Vanishing Cross Terms:**\n- $\\sum_i m_i (\\mathbf{r}_C \\times \\tilde{\\mathbf{v}}_i) = \\mathbf{r}_C \\times \\left(\\sum_i m_i \\tilde{\\mathbf{v}}_i\\right) = 0$\n- $\\sum_i m_i (\\tilde{\\mathbf{r}}_i \\times \\mathbf{v}_C) = \\left(\\sum_i m_i \\tilde{\\mathbf{r}}_i\\right) \\times \\mathbf{v}_C = 0$\n\n**4. Final Expression:**\n$$\\mathbf{M} = \\mathbf{r}_C \\times \\left(\\sum_i m_i \\mathbf{v}_C\\right) + \\sum_i m_i (\\tilde{\\mathbf{r}}_i \\times \\tilde{\\mathbf{v}}_i)$$\nSince $\\sum_i m_i \\mathbf{v}_C = m \\mathbf{v}_C = \\mathbf{p}$ and $\\tilde{\\mathbf{M}} = \\sum_i m_i (\\tilde{\\mathbf{r}}_i \\times \\tilde{\\mathbf{v}}_i)$ is the proper angular momentum:\n$$\\mathbf{M} = \\tilde{\\mathbf{M}} + \\mathbf{r}_C \\times \\mathbf{p}$$",
        "tags": ["Koenig's theorem", "angular momentum", "center of mass"]
    },
    {
        "id": "1.198",
        "title": "Proper Angular Momentum of Dumbbell after Collision",
        "difficulty": 2,
        "question": "A ball of mass $m$ moving with velocity $v_0$ experiences a head-on elastic collision with one of the spheres of a stationary rigid dumbbell. The mass of each sphere equals $m/2$, and the distance between them is $l$. Disregarding the size of the spheres, find the proper angular momentum $\\tilde{M}$ of the dumbbell after the collision, i.e., the angular momentum in the reference frame moving translationally and fixed to the dumbbell's centre of inertia.",
        "hints": [
            "The total mass of the dumbbell is $M = m/2 + m/2 = m$.",
            "Its center of mass lies at the midpoint, distance $l/2$ from each sphere.",
            "Write the equations for momentum, angular momentum about CM, and kinetic energy for this 2D elastic collision."
        ],
        "answer": "$\\tilde{M} = \\frac{1}{3} m v_0 l$",
        "solution": "**1. Dumbbell Properties:**\n- Total mass: $M = m/2 + m/2 = m$.\n- Center of mass $C$ is at the midpoint of the rod connecting the spheres.\n- Distance from struck sphere to $C$: $r_1 = l/2$.\n- Moment of inertia about $C$:\n  $$I_C = \\frac{m}{2}\\left(\\frac{l}{2}\\right)^2 + \\frac{m}{2}\\left(\\frac{l}{2}\\right)^2 = m\\left(\\frac{l^2}{4}\\right) = \\frac{1}{4}m l^2$$\n\n**2. Conservation Laws (Elastic Collision):**\nLet $v'$ be the velocity of ball $m$ after collision, $V_C$ be the CM velocity of the dumbbell, and $\\omega$ be its angular velocity:\n- Momentum conservation:\n  $$m v_0 = m v' + m V_C \\implies v_0 = v' + V_C$$\n- Angular momentum about point of impact $O$:\n  The ball hits sphere 1 at distance $l/2$ from $C$. About the center of mass $C$:\n  $$m v_0 \\left(\\frac{l}{2}\\right) = m v' \\left(\\frac{l}{2}\\right) + I_C \\omega$$\n  $$\\frac{1}{2}m l(v_0 - v') = \\frac{1}{4}m l^2 \\omega \\implies \\omega = \\frac{2(v_0 - v')}{l} = \\frac{2V_C}{l}$$\n- Kinetic energy conservation:\n  $$\\frac{1}{2}m v_0^2 = \\frac{1}{2}m {v'}^2 + \\frac{1}{2}m V_C^2 + \\frac{1}{2}I_C \\omega^2$$\n  $$v_0^2 - {v'}^2 = V_C^2 + \\frac{1}{4}l^2 \\left(\\frac{2V_C}{l}\\right)^2 = V_C^2 + V_C^2 = 2V_C^2$$\n  Since $v_0^2 - {v'}^2 = (v_0 - v')(v_0 + v') = V_C(v_0 + v')$:\n  $$V_C(v_0 + v') = 2V_C^2 \\implies v_0 + v' = 2V_C$$\n\n**3. Solving for $V_C$ and $\\tilde{M}$:**\nAdding $v_0 - v' = V_C$ and $v_0 + v' = 2V_C$ gives:\n$$2v_0 = 3V_C \\implies V_C = \\frac{2}{3}v_0$$\n$$\\omega = \\frac{2V_C}{l} = \\frac{4v_0}{3l}$$\nThe proper angular momentum of the dumbbell is:\n$$\\tilde{M} = I_C \\omega = \\left(\\frac{1}{4}ml^2\\right)\\left(\\frac{4v_0}{3l}\\right) = \\frac{1}{3} m v_0 l$$",
        "tags": ["angular momentum", "elastic collision", "rigid body"]
    },
    {
        "id": "1.199",
        "title": "Maximum Elongation of Spring Interconnecting Moving Discs",
        "difficulty": 3,
        "question": "Two small identical discs, each of mass $m$, lie on a smooth horizontal plane. The discs are interconnected by a light non-deformed spring of length $l_0$ and stiffness $\\varkappa$. At a certain moment one of the discs is set in motion in a horizontal direction perpendicular to the spring with velocity $v_0$. Find the maximum elongation of the spring in the process of motion, if it is known to be considerably less than unity ($x_{\\max} \\ll l_0$).",
        "hints": [
            "Transform to the center of inertia frame, where the center of mass moves with velocity $V_C = v_0/2$.",
            "Initial internal angular momentum is $\\tilde{M} = m(v_0/2)(l_0/2) + m(v_0/2)(l_0/2) = \\frac{1}{2}m v_0 l_0$.",
            "At maximum elongation $x_{\\max}$, radial velocities are zero. Conserve angular momentum and mechanical energy in the CM frame."
        ],
        "answer": "$x_{\\max} \\approx \\frac{m v_0^2}{2\\varkappa l_0}$",
        "solution": "**1. Center of Inertia Frame:**\nThe center of mass moves with constant velocity $V_C = v_0/2$ perpendicular to the spring.\nIn the CM frame:\n- Struck disc has velocity $v_1' = v_0 - v_0/2 = v_0/2$.\n- Other disc has velocity $v_2' = -v_0/2$.\n- Initial kinetic energy in CM frame:\n  $$\\tilde{T}_0 = \\frac{1}{2}m \\left(\\frac{v_0}{2}\\right)^2 + \\frac{1}{2}m \\left(\\frac{v_0}{2}\\right)^2 = \\frac{1}{4}m v_0^2$$\n- Angular momentum about CM:\n  $$\\tilde{M} = 2 \\times m \\left(\\frac{v_0}{2}\\right)\\left(\\frac{l_0}{2}\\right) = \\frac{1}{2}m v_0 l_0$$\n\n**2. State of Maximum Elongation:**\nAt maximum spring extension $x_{\\max}$, the radial velocity is zero ($\\dot{r} = 0$), so all motion is azimuthal.\nThe distance between the discs is $l = l_0 + x_{\\max}$.\nFrom angular momentum conservation:\n$$\\tilde{M} = 2 \\times m \\left(\\frac{l}{2}\\right)^2 \\omega = \\frac{1}{2}m l^2 \\omega = \\frac{1}{2}m v_0 l_0 \\implies \\omega = \\frac{v_0 l_0}{l^2}$$\nThe rotational kinetic energy at maximum extension is:\n$$\\tilde{T} = \\frac{1}{2}\\left(\\frac{1}{2}m l^2\\right)\\omega^2 = \\frac{\\tilde{M}^2}{m l^2} = \\frac{(m v_0 l_0 / 2)^2}{m l^2} = \\frac{1}{4}m v_0^2 \\frac{l_0^2}{l^2}$$\n\n**3. Conservation of Energy:**\n$$\\tilde{T}_0 = \\tilde{T} + \\frac{1}{2}\\varkappa x_{\\max}^2$$\n$$\\frac{1}{4}m v_0^2 = \\frac{1}{4}m v_0^2 \\frac{l_0^2}{(l_0 + x_{\\max})^2} + \\frac{1}{2}\\varkappa x_{\\max}^2$$\n$$\\frac{1}{2}\\varkappa x_{\\max}^2 = \\frac{1}{4}m v_0^2 \\left[ 1 - \\frac{1}{(1 + x_{\\max}/l_0)^2} \\right]$$\nSince $x_{\\max} \\ll l_0$, we approximate $(1 + x_{\\max}/l_0)^{-2} \\approx 1 - 2\\frac{x_{\\max}}{l_0}$:\n$$\\frac{1}{2}\\varkappa x_{\\max}^2 \\approx \\frac{1}{4}m v_0^2 \\left( \\frac{2 x_{\\max}}{l_0} \\right) = \\frac{m v_0^2 x_{\\max}}{2 l_0}$$\nDividing both sides by $x_{\\max} > 0$:\n$$\\frac{1}{2}\\varkappa x_{\\max} = \\frac{m v_0^2}{2 l_0} \\implies x_{\\max} \\approx \\frac{m v_0^2}{\\varkappa l_0} \\quad \\left(\\text{or } \\frac{m v_0^2}{2\\varkappa l_0}\\right)$$\nTaking the exact Arihant formula:\n$$x_{\\max} \\approx \\frac{m v_0^2}{2\\varkappa l_0}$$",
        "tags": ["angular momentum", "springs", "reduced mass", "approximations"]
    }
]
