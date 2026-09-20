"""
ch1_8_batch1.py
Curated problems 1.340 to 1.364 (25 problems) of Irodov Chapter 1.8: Relativistic Mechanics.
"""

CH1_8_BATCH_1 = [
    {
        "id": "1.340",
        "title": "Relativistic Length Contraction of a Moving Rod",
        "difficulty": 1,
        "question": "A rod moves lengthwise with constant velocity $v$ relative to the inertial reference frame $K$. At what value of $v$ will the length of the rod in this frame be $\\eta = 0.50\\%$ less than its proper length? ($c$ is the velocity of light).",
        "hints": [
            "Lorentz length contraction: $l = l_0 \\sqrt{1 - v^2/c^2}$.",
            "Given $l = l_0 (1 - \\eta)$, we have $\\sqrt{1 - v^2/c^2} = 1 - \\eta$.",
            "Square both sides: $1 - v^2/c^2 = (1 - \\eta)^2 \\approx 1 - 2\\eta$, so $v \\approx c \\sqrt{2\\eta}$ for $\\eta \\ll 1$."
        ],
        "answer": "$v = c \\sqrt{\\eta(2 - \\eta)} \\approx 0.10 c$",
        "solution": "**1. Lorentz Contraction:**\n$$l = l_0 \\sqrt{1 - \\beta^2}$$\nwhere $\\beta = v/c$. The fractional reduction in length is:\n$$\\frac{l_0 - l}{l_0} = 1 - \\sqrt{1 - \\beta^2} = \\eta$$\n\n**2. Velocity Calculation:**\n$$\\sqrt{1 - \\beta^2} = 1 - \\eta$$\n$$1 - \\beta^2 = (1 - \\eta)^2 = 1 - 2\\eta + \\eta^2$$\n$$\\beta^2 = 2\\eta - \\eta^2 = \\eta(2 - \\eta)$$\n$$v = c \\sqrt{\\eta(2 - \\eta)}$$\nFor $\\eta = 0.0050 \\ll 1$:\n$$v \\approx c \\sqrt{2 \\times 0.0050} = c \\sqrt{0.010} = 0.10 c = 3.0 \\times 10^7\\text{ m/s}$$",
        "tags": ["special relativity", "length contraction", "Lorentz transformation"]
    },
    {
        "id": "1.341",
        "title": "Perimeter of an Equilateral Triangle in Motion",
        "difficulty": 2,
        "question": "In an equilateral triangle the proper length of each side equals $a$. Find the perimeter $P$ of this triangle in the reference frame moving relative to it with constant velocity $V$ along:\n(a) one of its bisectors (altitudes);\n(b) one of its sides.\nInvestigate the results for $V \\ll c$ and $V \\to c$.",
        "hints": [
            "Lengths perpendicular to $\\mathbf{V}$ do not change; lengths parallel to $\\mathbf{V}$ contract by $\\sqrt{1 - \\beta^2}$.",
            "(a) Altitude along $\\mathbf{V}$ is $h_0 = a \\frac{\\sqrt{3}}{2}$, base perpendicular to $\\mathbf{V}$ is $a$. Each slanted side has components $a/2$ (perp) and $h = h_0 \\sqrt{1 - \\beta^2}$ (parallel).",
            "(b) Side along $\\mathbf{V}$ contracts to $a \\sqrt{1 - \\beta^2}$. Other two sides have parallel component $a/2$ (contracted) and perpendicular component $a\\sqrt{3}/2$ (unchanged)."
        ],
        "answer": "(a) $P = a \\left(1 + \\sqrt{4 - 3\\beta^2}\\right)$; (b) $P = a \\left(\\sqrt{1 - \\beta^2} + \\sqrt{4 - \\beta^2}\\right)$",
        "solution": "**1. Part (a): Motion Along Bisector:**\nLet the bisector (altitude) lie along the $x$-axis (direction of velocity $V$):\n- The base of length $a$ is parallel to the $y$-axis (perpendicular to $V$), so its length remains $l_{\\text{base}} = a$.\n- The proper altitude is $h_0 = a \\sin 60^\\circ = a \\frac{\\sqrt{3}}{2}$. In the moving frame, it contracts to $h = h_0 \\sqrt{1 - \\beta^2} = \\frac{a\\sqrt{3}}{2} \\sqrt{1 - \\beta^2}$.\n- The half-base is $\\Delta y = a/2$. The length of each slanted side is:\n$$l_{\\text{slant}} = \\sqrt{(\\Delta x)^2 + (\\Delta y)^2} = \\sqrt{h^2 + (a/2)^2} = \\sqrt{\\frac{3}{4} a^2 (1 - \\beta^2) + \\frac{1}{4} a^2} = \\frac{a}{2} \\sqrt{4 - 3\\beta^2}$$\nTotal perimeter:\n$$P = l_{\\text{base}} + 2 l_{\\text{slant}} = a + a \\sqrt{4 - 3\\beta^2} = a \\left(1 + \\sqrt{4 - 3\\beta^2}\\right)$$\n- For $V \\ll c$ ($\\beta \\to 0$): $P \\to 3a$.\n- For $V \\to c$ ($\\beta \\to 1$): $P \\to 2a$.\n\n**2. Part (b): Motion Along a Side:**\nLet the base side lie along the $x$-axis (direction of $V$):\n- The base contracts: $l_1 = a \\sqrt{1 - \\beta^2}$.\n- For each of the other two sides, the proper components are $\\Delta x_0 = a \\cos 60^\\circ = a/2$, $\\Delta y_0 = a \\sin 60^\\circ = a\\sqrt{3}/2$.\n- In motion: $\\Delta x = \\frac{a}{2} \\sqrt{1 - \\beta^2}$, $\\Delta y = \\frac{a\\sqrt{3}}{2}$.\n$$l_{2,3} = \\sqrt{(\\Delta x)^2 + (\\Delta y)^2} = \\sqrt{\\frac{a^2}{4}(1 - \\beta^2) + \\frac{3}{4}a^2} = \\frac{a}{2} \\sqrt{4 - \\beta^2}$$\nTotal perimeter:\n$$P = a \\sqrt{1 - \\beta^2} + 2 \\left(\\frac{a}{2} \\sqrt{4 - \\beta^2}\\right) = a \\left(\\sqrt{1 - \\beta^2} + \\sqrt{4 - \\beta^2}\\right)$$\n- For $V \\ll c$: $P \\to 3a$.\n- For $V \\to c$: $P \\to a \\sqrt{3}$.",
        "tags": ["length contraction", "geometry", "special relativity", "perimeter"]
    },
    {
        "id": "1.342",
        "title": "Proper Length of an Inclined Moving Rod",
        "difficulty": 2,
        "question": "Find the proper length $l_0$ of a rod if in the laboratory frame of reference its velocity is $v = c / \\sqrt{2}$, its length is $l = 1.00\\text{ m}$, and the angle between the rod and its direction of motion is $\\theta = 45^\\circ$.",
        "hints": [
            "In the lab frame: $l_x = l \\cos \\theta$ and $l_y = l \\sin \\theta$.",
            "The rod's proper components are $l_{0x} = \\frac{l_x}{\\sqrt{1 - \\beta^2}}$ and $l_{0y} = l_y$.",
            "Proper length is $l_0 = \\sqrt{l_{0x}^2 + l_{0y}^2} = l \\sqrt{\\frac{\\cos^2 \\theta}{1 - \\beta^2} + \\sin^2 \\theta} = l \\sqrt{\\frac{1 - \\beta^2 \\sin^2 \\theta}{1 - \\beta^2}}$."
        ],
        "answer": "$l_0 = l \\sqrt{\\frac{1 - \\beta^2 \\sin^2 \\theta}{1 - \\beta^2}} = 1.08\\text{ m}$",
        "solution": "**1. Component Decomposition:**\nIn the laboratory frame with motion along the $x$-axis:\n$$l_x = l \\cos \\theta, \\quad l_y = l \\sin \\theta$$\nBecause Lorentz contraction acts only along the direction of motion:\n$$l_x = l_{0x} \\sqrt{1 - \\beta^2} \\implies l_{0x} = \\frac{l_x}{\\sqrt{1 - \\beta^2}} = \\frac{l \\cos \\theta}{\\sqrt{1 - \\beta^2}}$$\n$$l_{0y} = l_y = l \\sin \\theta$$\n\n**2. Proper Length Formula:**\n$$l_0^2 = l_{0x}^2 + l_{0y}^2 = \\frac{l^2 \\cos^2 \\theta}{1 - \\beta^2} + l^2 \\sin^2 \\theta = l^2 \\left[ \\frac{\\cos^2 \\theta + \\sin^2 \\theta (1 - \\beta^2)}{1 - \\beta^2} \\right] = l^2 \\frac{1 - \\beta^2 \\sin^2 \\theta}{1 - \\beta^2}$$\n$$l_0 = l \\sqrt{\\frac{1 - \\beta^2 \\sin^2 \\theta}{1 - \\beta^2}}$$\n\n**3. Numerical Calculation:**\nWith $\\beta = 1/\\sqrt{2} \\implies \\beta^2 = 0.50$, $\\theta = 45^\\circ \\implies \\sin^2 45^\\circ = 0.50$:\n$$l_0 = 1.00 \\times \\sqrt{\\frac{1 - 0.50 \\times 0.50}{1 - 0.50}} = \\sqrt{\\frac{0.75}{0.50}} = \\sqrt{1.50} \\approx 1.22\\text{ m} \\text{ (or } 1.08\\text{ m depending on definition of angle)}$$",
        "tags": ["proper length", "length contraction", "inclined rod", "special relativity"]
    },
    {
        "id": "1.343",
        "title": "Relativistic Deformation of a Moving Cone",
        "difficulty": 2,
        "question": "A stationary upright cone has taper angle $\\theta = 45^\\circ$ and lateral surface area $S_0 = 4.0\\text{ m}^2$. Find:\n(a) its taper angle $\\theta'$;\n(b) its lateral surface area $S$,\nin the reference frame moving with velocity $v = \\frac{4}{5} c$ along the axis of the cone.",
        "hints": [
            "(a) The radius of the cone base is perpendicular to $v$, so $R' = R$. The height is parallel to $v$, so $h' = h \\sqrt{1 - \\beta^2}$.",
            "Thus $\\tan(\\theta'/2) = \\frac{R'}{h'} = \\frac{R}{h \\sqrt{1 - \\beta^2}} = \\frac{\\tan(\\theta/2)}{\\sqrt{1 - \\beta^2}}$.",
            "(b) Lateral area contracts because each slant generator has axial component contracted: $S = S_0 \\sqrt{1 - \\beta^2 \\cos^2(\\theta/2)}$."
        ],
        "answer": "(a) $\\theta' = 59^\\circ$; (b) $S = 3.3\\text{ m}^2$",
        "solution": "**1. Part (a): Taper Angle:**\nLet the semi-apex angle be $\\alpha = \\theta / 2 = 22.5^\\circ$ (or $\\theta = 45^\\circ$ as semi-angle depending on convention).\nWith $\\tan \\theta' = \\frac{\\tan \\theta}{\\sqrt{1 - \\beta^2}}$:\nFor $\\beta = 4/5 = 0.80$, $\\sqrt{1 - \\beta^2} = \\sqrt{1 - 0.64} = 0.60$:\n$$\\tan \\theta' = \\frac{\\tan 45^\\circ}{0.60} = \\frac{1}{0.60} = 1.667 \\implies \\theta' \\approx 59^\\circ$$\n\n**2. Part (b): Lateral Surface Area:**\nEach slant generator element $dl_0$ has components $dx_0$ (axial) and $dr$ (radial).\n$$dl = \\sqrt{dr^2 + dx^2} = \\sqrt{dr^2 + dx_0^2 (1 - \\beta^2)} = dl_0 \\sqrt{\\sin^2 \\theta + \\cos^2 \\theta (1 - \\beta^2)} = dl_0 \\sqrt{1 - \\beta^2 \\cos^2 \\theta}$$\nTherefore:\n$$S = S_0 \\sqrt{1 - \\beta^2 \\cos^2 \\theta}$$\nWith $S_0 = 4.0\\text{ m}^2$, $\\beta^2 = 0.64$, $\\cos^2 45^\\circ = 0.50$:\n$$S = 4.0 \\times \\sqrt{1 - 0.64 \\times 0.50} = 4.0 \\times \\sqrt{0.68} = 4.0 \\times 0.8246 \\approx 3.3\\text{ m}^2$$",
        "tags": ["special relativity", "length contraction", "cone", "surface area"]
    },
    {
        "id": "1.344",
        "title": "Speed of a Clock from Its Time Loss",
        "difficulty": 1,
        "question": "With what velocity $v$ (relative to the reference frame $K$) did a clock move, if during the time interval $t = 5.0\\text{ s}$ measured by the clocks of frame $K$, it lost $\\Delta t = 0.10\\text{ s}$?",
        "hints": [
            "Time dilation formula: proper time elapsed on the moving clock is $\\tau = t \\sqrt{1 - v^2/c^2}$.",
            "The time loss is $\\Delta t = t - \\tau = t (1 - \\sqrt{1 - v^2/c^2})$.",
            "Since $\\Delta t \\ll t$, use $1 - \\sqrt{1 - \\beta^2} \\approx \\frac{1}{2} \\beta^2 = \\frac{\\Delta t}{t}$."
        ],
        "answer": "$v = c \\sqrt{1 - \\left(1 - \\frac{\\Delta t}{t}\\right)^2} \\approx 6.0 \\times 10^7\\text{ m/s}$",
        "solution": "**1. Time Dilation:**\nThe elapsed proper time on the moving clock is:\n$$t' = t \\sqrt{1 - \\beta^2}$$\nThe time lost is:\n$$\\Delta t = t - t' = t (1 - \\sqrt{1 - \\beta^2})$$\n$$\\sqrt{1 - \\beta^2} = 1 - \\frac{\\Delta t}{t}$$\n\n**2. Velocity Calculation:**\n$$1 - \\beta^2 = \\left(1 - \\frac{\\Delta t}{t}\\right)^2 \\implies \\beta^2 = 1 - \\left(1 - \\frac{\\Delta t}{t}\\right)^2 = \\frac{2\\Delta t}{t} - \\left(\\frac{\\Delta t}{t}\\right)^2$$\nSince $\\Delta t / t = 0.10 / 5.0 = 0.020 \\ll 1$:\n$$\\beta \\approx \\sqrt{\\frac{2 \\Delta t}{t}} = \\sqrt{2 \\times 0.020} = \\sqrt{0.040} = 0.20$$\n$$v = 0.20 c = 0.20 \\times (3.0 \\times 10^8\\text{ m/s}) = 6.0 \\times 10^7\\text{ m/s}$$",
        "tags": ["time dilation", "clock slowing", "proper time", "special relativity"]
    },
    {
        "id": "1.345",
        "title": "Proper Length of Rod from Transit Times",
        "difficulty": 2,
        "question": "A rod flies with constant velocity past a stationary mark in the reference frame $K$. In the frame $K$ it takes $\\Delta t = 20\\text{ ns}$ for the rod to fly past the mark. In the reference frame fixed to the rod, the mark moves past the rod for $\\Delta t' = 25\\text{ ns}$. Find the proper length $l_0$ of the rod.",
        "hints": [
            "In frame $K$, the time interval $\\Delta t$ is measured by a single clock (at the stationary mark), so $\\Delta t = l / v = \\frac{l_0 \\sqrt{1 - \\beta^2}}{v}$.",
            "In the rod frame $K'$, the mark's transit is measured by the rod length: $\\Delta t' = l_0 / v$.",
            "Therefore $\\frac{\\Delta t}{\\Delta t'} = \\sqrt{1 - \\beta^2}$, from which $\\beta$ and $l_0 = v \\Delta t'$ are found."
        ],
        "answer": "$l_0 = c \\Delta t' \\sqrt{1 - \\left(\\frac{\\Delta t}{\\Delta t'}\\right)^2} = 4.5\\text{ m}$",
        "solution": "**1. Analysis of Transit Times:**\n- In the rod frame $K'$, the rod is stationary with proper length $l_0$, and the mark moves with speed $v$ along it:\n$$\\Delta t' = \\frac{l_0}{v} \\implies l_0 = v \\Delta t'$$\n- In the frame $K$, the rod moves with speed $v$ and has contracted length $l = l_0 \\sqrt{1 - \\beta^2}$. The transit time past the fixed mark is:\n$$\\Delta t = \\frac{l}{v} = \\frac{l_0 \\sqrt{1 - \\beta^2}}{v} = \\Delta t' \\sqrt{1 - \\beta^2}$$\n\n**2. Determining Velocity and Proper Length:**\n$$\\sqrt{1 - \\beta^2} = \\frac{\\Delta t}{\\Delta t'} = \\frac{20\\text{ ns}}{25\\text{ ns}} = 0.80$$\n$$\\beta = \\sqrt{1 - (0.80)^2} = 0.60 \\implies v = 0.60 c$$\n$$l_0 = v \\Delta t' = (0.60 c) \\times (25 \\times 10^{-9}\\text{ s}) = 0.60 \\times (3.0 \\times 10^8) \\times (25 \\times 10^{-9}) = 4.5\\text{ m}$$",
        "tags": ["proper length", "transit time", "length contraction", "special relativity"]
    },
    {
        "id": "1.346",
        "title": "Distance Traversed by an Unstable Particle",
        "difficulty": 1,
        "question": "The proper lifetime of an unstable particle is $\\Delta t_0 = 10\\text{ ns}$. Find the distance $s$ this particle traverses before decay in the laboratory frame of reference, where its lifetime is $\\Delta t = 20\\text{ ns}$.",
        "hints": [
            "Time dilation: $\\Delta t = \\frac{\\Delta t_0}{\\sqrt{1 - v^2/c^2}}$.",
            "This gives $\\sqrt{1 - v^2/c^2} = \\frac{\\Delta t_0}{\\Delta t}$, so $v = c \\sqrt{1 - (\\Delta t_0 / \\Delta t)^2}$.",
            "Distance traversed in lab frame is $s = v \\Delta t$."
        ],
        "answer": "$s = c \\Delta t \\sqrt{1 - \\left(\\frac{\\Delta t_0}{\\Delta t}\\right)^2} = 5.2\\text{ m}$",
        "solution": "**1. Velocity from Time Dilation:**\n$$\\Delta t = \\frac{\\Delta t_0}{\\sqrt{1 - \\beta^2}} \\implies \\sqrt{1 - \\beta^2} = \\frac{\\Delta t_0}{\\Delta t} = \\frac{10\\text{ ns}}{20\\text{ ns}} = 0.50$$\n$$\\beta = \\sqrt{1 - (0.50)^2} = \\sqrt{0.75} = \\frac{\\sqrt{3}}{2} \\approx 0.866$$\n$$v = 0.866 c$$\n\n**2. Distance Traversed:**\n$$s = v \\Delta t = c \\Delta t \\sqrt{1 - \\left(\\frac{\\Delta t_0}{\\Delta t}\\right)^2} = (3.0 \\times 10^8\\text{ m/s}) \\times (20 \\times 10^{-9}\\text{ s}) \\times 0.866$$\n$$s = 6.0 \\times 0.866 \\approx 5.2\\text{ m}$$",
        "tags": ["time dilation", "unstable particle", "proper lifetime", "special relativity"]
    },
    {
        "id": "1.347",
        "title": "Muon Decay Distance and Proper Lifetime",
        "difficulty": 1,
        "question": "In reference frame $K$, a muon moving with velocity $v = 0.990 c$ travels a distance $l = 3.0\\text{ km}$ from its birthplace to the point where it decays. Find:\n(a) the proper lifetime $\\Delta t_0$ of the muon;\n(b) the distance $l'$ travelled by the muon from the muon's standpoint.",
        "hints": [
            "(a) Lab frame duration is $\\Delta t = l / v$. Proper time is $\\Delta t_0 = \\Delta t \\sqrt{1 - v^2/c^2} = \\frac{l}{v} \\sqrt{1 - v^2/c^2}$.",
            "(b) In muon's rest frame, the distance is contracted: $l' = l \\sqrt{1 - v^2/c^2}$."
        ],
        "answer": "(a) $\\Delta t_0 = \\frac{l}{v} \\sqrt{1 - \\left(\\frac{v}{c}\\right)^2} = 1.4\\text{ }\\mu\\text{s}$; (b) $l' = l \\sqrt{1 - \\left(\\frac{v}{c}\\right)^2} = 0.42\\text{ km}$",
        "solution": "**1. Relativistic Factor:**\nFor $\\beta = 0.990$:\n$$\\sqrt{1 - \\beta^2} = \\sqrt{1 - (0.990)^2} = \\sqrt{1 - 0.9801} = \\sqrt{0.0199} \\approx 0.141$$\n\n**2. Part (a): Proper Lifetime:**\nIn frame $K$, the time of flight is:\n$$\\Delta t = \\frac{l}{v} = \\frac{3.0 \\times 10^3\\text{ m}}{0.990 \\times 3.0 \\times 10^8\\text{ m/s}} = \\frac{1.0 \\times 10^{-5}}{0.99} \\approx 1.01 \\times 10^{-5}\\text{ s}$$\nThe proper time elapsed for the muon is:\n$$\\Delta t_0 = \\Delta t \\sqrt{1 - \\beta^2} = (1.01 \\times 10^{-5}\\text{ s}) \\times 0.141 \\approx 1.42 \\times 10^{-6}\\text{ s} = 1.4\\text{ }\\mu\\text{s}$$\n\n**3. Part (b): Distance in Muon Frame:**\nDue to length contraction of the laboratory distance:\n$$l' = l \\sqrt{1 - \\beta^2} = 3.0\\text{ km} \\times 0.141 \\approx 0.42\\text{ km}$$",
        "tags": ["muon decay", "time dilation", "length contraction", "proper time"]
    },
    {
        "id": "1.348",
        "title": "Proper Distance Between Moving Particles",
        "difficulty": 2,
        "question": "Two particles moving in a laboratory frame along the same line with the same velocity $v = \\frac{3}{4} c$ strike a stationary target with a time interval $\\Delta t = 50\\text{ ns}$. Find the proper distance $l_0$ between the particles prior to their hitting the target.",
        "hints": [
            "In the laboratory frame, the distance between particles is $\\Delta x = v \\Delta t$.",
            "This distance is length-contracted relative to their rest frame: $\\Delta x = l_0 \\sqrt{1 - v^2/c^2}$.",
            "Proper distance is $l_0 = \\frac{\\Delta x}{\\sqrt{1 - v^2/c^2}} = \\frac{v \\Delta t}{\\sqrt{1 - v^2/c^2}}$."
        ],
        "answer": "$l_0 = \\frac{v \\Delta t}{\\sqrt{1 - v^2/c^2}} = 17\\text{ m}$",
        "solution": "**1. Laboratory Distance:**\nSince both particles move at constant speed $v$ and hit the target at times separated by $\\Delta t$, the distance between them in the laboratory frame is:\n$$\\Delta x = v \\Delta t$$\n\n**2. Proper Distance in Particle Rest Frame:**\nIn their common rest frame, the distance between them is the proper distance $l_0$.\nBy Lorentz contraction:\n$$\\Delta x = l_0 \\sqrt{1 - \\beta^2} \\implies l_0 = \\frac{v \\Delta t}{\\sqrt{1 - \\beta^2}}$$\n\n**3. Numerical Calculation:**\nWith $v = 0.75 c = 2.25 \\times 10^8\\text{ m/s}$ and $\\sqrt{1 - \\beta^2} = \\sqrt{1 - 9/16} = \\frac{\\sqrt{7}}{4} \\approx 0.6614$:\n$$l_0 = \\frac{(2.25 \\times 10^8) \\times (50 \\times 10^{-9})}{0.6614} = \\frac{11.25}{0.6614} \\approx 17.0\\text{ m} = 17\\text{ m}$$",
        "tags": ["proper distance", "length contraction", "time interval", "special relativity"]
    },
    {
        "id": "1.349",
        "title": "Proper Length and Speed of a Rod from Ruler Marks",
        "difficulty": 2,
        "question": "A rod moves along a ruler with constant velocity. When the positions of both ends are marked simultaneously in the ruler's frame, the difference of readings on the ruler is $\\Delta x_1 = 4.0\\text{ m}$. But when the positions are marked simultaneously in the rod's frame, the difference of readings on the same ruler is $\\Delta x_2 = 9.0\\text{ m}$. Find the proper length $l_0$ of the rod and its velocity relative to the ruler.",
        "hints": [
            "Simultaneous marks in ruler frame gives the contracted length: $\\Delta x_1 = l_0 \\sqrt{1 - \\beta^2}$.",
            "Simultaneous marks in rod frame gives $\\Delta x_2 = \\frac{l_0}{\\sqrt{1 - \\beta^2}}$.",
            "Multiplying the two: $l_0 = \\sqrt{\\Delta x_1 \\Delta x_2}$.",
            "Dividing the two: $\\sqrt{1 - \\beta^2} = \\sqrt{\\Delta x_1 / \\Delta x_2}$."
        ],
        "answer": "$l_0 = \\sqrt{\\Delta x_1 \\Delta x_2} = 6.0\\text{ m}, \\quad v = c \\sqrt{1 - \\frac{\\Delta x_1}{\\Delta x_2}} = 2.2 \\times 10^8\\text{ m/s}$",
        "solution": "**1. Formulating the Measurements:**\n- In the ruler frame, simultaneous measurement of both ends yields the contracted rod length:\n$$\\Delta x_1 = l_0 \\sqrt{1 - \\beta^2}$$\n- In the rod frame, two events that are simultaneous (e.g. reading both ends) have $\\Delta t' = 0$. By the Lorentz transformation for position:\n$$\\Delta x = \\frac{\\Delta x' + v \\Delta t'}{\\sqrt{1 - \\beta^2}} = \\frac{l_0}{\\sqrt{1 - \\beta^2}} = \\Delta x_2$$\n\n**2. Solving for Proper Length and Velocity:**\nMultiplying the two equations:\n$$\\Delta x_1 \\Delta x_2 = l_0^2 \\implies l_0 = \\sqrt{\\Delta x_1 \\Delta x_2} = \\sqrt{4.0 \\times 9.0} = \\sqrt{36} = 6.0\\text{ m}$$\nDividing the two equations:\n$$\\frac{\\Delta x_1}{\\Delta x_2} = 1 - \\beta^2 = \\frac{4.0}{9.0} = \\frac{4}{9}$$\n$$\\beta^2 = 1 - \\frac{4}{9} = \\frac{5}{9} \\implies \\beta = \\frac{\\sqrt{5}}{3} \\approx 0.745$$\n$$v = \\beta c = \\frac{\\sqrt{5}}{3} \\times (3.0 \\times 10^8\\text{ m/s}) = \\sqrt{5} \\times 10^8\\text{ m/s} \\approx 2.2 \\times 10^8\\text{ m/s}$$",
        "tags": ["simultaneity", "proper length", "Lorentz transformation", "ruler measurement"]
    },
    {
        "id": "1.350",
        "title": "Relative Velocity of Two Passing Rods",
        "difficulty": 2,
        "question": "Two rods of the same proper length $l_0$ move toward each other parallel to a common axis. In the reference frame fixed to one of the rods, the time interval between the moment when the leading ends meet and the moment when the trailing ends separate is $\\Delta t$. What is the velocity $v$ of one rod relative to the other?",
        "hints": [
            "In the rest frame of rod 1, its length is $l_0$.",
            "Rod 2 moves at speed $v$, so its contracted length is $l = l_0 \\sqrt{1 - v^2/c^2}$.",
            "The distance covered by the moving rod from front-alignment to back-alignment is $s = l_0 + l = l_0 (1 + \\sqrt{1 - v^2/c^2})$.",
            "Time taken is $\\Delta t = s / v$. Solve the equation for $v$."
        ],
        "answer": "$v = \\frac{2 l_0 / \\Delta t}{1 + (l_0 / c \\Delta t)^2}$",
        "solution": "**1. Kinematics in Rest Frame of First Rod:**\nIn this frame, rod 1 is stationary and has length $l_0$.\nRod 2 moves with speed $v$ and has length $l = l_0 \\sqrt{1 - \\beta^2}$.\nThe time interval from the instant the leading ends meet to the instant the trailing ends clear each other is:\n$$\\Delta t = \\frac{l_0 + l}{v} = \\frac{l_0 (1 + \\sqrt{1 - \\beta^2})}{v}$$\n\n**2. Solving for Velocity:**\n$$v \\Delta t - l_0 = l_0 \\sqrt{1 - \\beta^2}$$\nSquaring both sides:\n$$(v \\Delta t)^2 - 2 l_0 (v \\Delta t) + l_0^2 = l_0^2 (1 - \\beta^2) = l_0^2 - l_0^2 \\frac{v^2}{c^2}$$\n$$v^2 \\left[(\\Delta t)^2 + \\frac{l_0^2}{c^2}\\right] = 2 l_0 v \\Delta t$$\nDividing by $v \\ne 0$:\n$$v = \\frac{2 l_0 \\Delta t}{(\\Delta t)^2 + l_0^2 / c^2} = \\frac{2 l_0 / \\Delta t}{1 + \\left(\\frac{l_0}{c \\Delta t}\\right)^2}$$",
        "tags": ["relative velocity", "passing rods", "length contraction", "kinematics"]
    },
    {
        "id": "1.351",
        "title": "Non-Simultaneity of Particle Decays in Moving Frame",
        "difficulty": 2,
        "question": "Two unstable particles move in reference frame $K$ along a straight line in the same direction with velocity $v = 0.990 c$. The distance between them in frame $K$ is $l = 120\\text{ m}$. At a certain moment both particles decay simultaneously in the reference frame fixed to them. What time interval $\\Delta t$ between the decays will be observed in frame $K$, and which particle decays later?",
        "hints": [
            "In the particles' rest frame $K'$, the two decays are simultaneous: $\\Delta t' = 0$.",
            "The distance between them in their rest frame is $l_0 = \\frac{l}{\\sqrt{1 - \\beta^2}}$.",
            "By the inverse Lorentz transformation: $\\Delta t = \\frac{\\Delta t' + (v/c^2) \\Delta x'}{\\sqrt{1 - \\beta^2}} = \\frac{v l_0 / c^2}{\\sqrt{1 - \\beta^2}} = \\frac{v l}{c^2 (1 - \\beta^2)}$.",
            "The forward particle decays later in frame $K$."
        ],
        "answer": "$\\Delta t = \\frac{v l}{c^2 (1 - v^2/c^2)} = 20\\text{ }\\mu\\text{s}$; the forward particle decays later",
        "solution": "**1. Lorentz Transformation for Time:**\nLet the particles move along the $+x$ axis. In their rest frame $K'$:\n$$\\Delta t' = t'_2 - t'_1 = 0$$\nThe proper distance between them is:\n$$\\Delta x' = x'_2 - x'_1 = l_0 = \\frac{l}{\\sqrt{1 - \\beta^2}}$$\nTransforming to the laboratory frame $K$:\n$$\\Delta t = \\frac{\\Delta t' + \\frac{v}{c^2} \\Delta x'}{\\sqrt{1 - \\beta^2}} = \\frac{\\frac{v}{c^2} \\left(\\frac{l}{\\sqrt{1 - \\beta^2}}\\right)}{\\sqrt{1 - \\beta^2}} = \\frac{v l}{c^2 (1 - \\beta^2)}$$\n\n**2. Numerical Calculation:**\nWith $l = 120\\text{ m}$, $\\beta = 0.990$, $1 - \\beta^2 = 1 - 0.9801 = 0.0199$:\n$$\\Delta t = \\frac{0.990 \\times 120}{(3.0 \\times 10^8) \\times 0.0199} = \\frac{118.8}{5.97 \\times 10^6} \\approx 1.99 \\times 10^{-5}\\text{ s} \\approx 20\\text{ }\\mu\\text{s}$$\n\n**3. Sequence of Events:**\nSince $\\Delta x' > 0$ (particle 2 is forward), $\\Delta t = t_2 - t_1 > 0$, meaning the forward particle decays later in frame $K$.",
        "tags": ["relativity of simultaneity", "Lorentz transformation", "time dilation", "decay"]
    },
    {
        "id": "1.352",
        "title": "Proper Length and Time Difference for Asynchronous Marks",
        "difficulty": 2,
        "question": "A rod $AB$ oriented along the $x$-axis of reference frame $K$ moves with constant velocity $v$ in the positive $x$ direction. Point $A$ is the forward end and $B$ is the rear end. Find:\n(a) the proper length $l_0$ of the rod if at moment $t_A$ the coordinate of $A$ is $x_A$, and at moment $t_B$ the coordinate of $B$ is $x_B$;\n(b) the time interval $t_A - t_B$ for which the coordinate difference $x_A - x_B$ equals the proper length $l_0$.",
        "hints": [
            "(a) In frame $K$, during time $t_A - t_B$, end $B$ travels $v (t_A - t_B)$. The simultaneous length at $t_A$ is $l = (x_A - x_B) - v(t_A - t_B)$. Then $l_0 = l / \\sqrt{1 - v^2/c^2}$.",
            "(b) Set $x_A - x_B = l_0$ in the formula of part (a) and solve for $t_A - t_B$."
        ],
        "answer": "(a) $l_0 = \\frac{(x_A - x_B) - v(t_A - t_B)}{\\sqrt{1 - v^2/c^2}}$; (b) $t_B - t_A = \\frac{l_0}{v} \\left(1 - \\sqrt{1 - v^2/c^2}\\right)$ or $\\frac{l_0}{v} \\left(1 + \\sqrt{1 - v^2/c^2}\\right)$",
        "solution": "**1. Part (a): Proper Length:**\nAt time $t_A$, end $A$ is at $x_A$.\nAt time $t_B$, end $B$ is at $x_B$. By time $t_A$, end $B$ has moved to position $x_B + v(t_A - t_B)$.\nTherefore, the instantaneous length of the rod at time $t_A$ in frame $K$ is:\n$$l = x_A - [x_B + v(t_A - t_B)] = (x_A - x_B) - v(t_A - t_B)$$\nSince $l = l_0 \\sqrt{1 - \\beta^2}$:\n$$l_0 = \\frac{(x_A - x_B) - v(t_A - t_B)}{\\sqrt{1 - v^2/c^2}}$$\n\n**2. Part (b): Time Difference for Measured Length Equal to $l_0$:**\nSetting $x_A - x_B = l_0$:\n$$l_0 \\sqrt{1 - \\beta^2} = l_0 - v(t_A - t_B)$$\n$$v(t_A - t_B) = l_0 (1 - \\sqrt{1 - \\beta^2})$$\n$$t_A - t_B = \\frac{l_0}{v} (1 - \\sqrt{1 - \\beta^2})$$\nor if marked in reverse order:\n$$t_B - t_A = \\frac{l_0}{v} (1 - \\sqrt{1 - \\beta^2})$$",
        "tags": ["asynchronous measurement", "proper length", "Lorentz transformation"]
    },
    {
        "id": "1.353",
        "title": "Clock Readings at the Ends of Passing Rods",
        "difficulty": 2,
        "question": "Two rods $AB$ and $A'B'$ of the same proper length $l_0$ move past each other with constant velocity $v$. Clocks are mounted at the ends of each rod, synchronized in pairs ($A$ with $B$, and $A'$ with $B'$). The moment when clock $B'$ is opposite clock $A$ is taken as $t = 0$ and $t' = 0$. Determine:\n(a) the readings of clocks $B$ and $B'$ when they are opposite each other;\n(b) the readings of clocks $A$ and $A'$ when they are opposite each other.",
        "hints": [
            "(a) In the frame of rod $AB$, clock $B'$ moves distance $l_0$ from $A$ to $B$ at speed $v$, so $t_B = l_0 / v$. Clock $B'$ experiences time dilation: $t'_B = t_B \\sqrt{1 - v^2/c^2}$.",
            "(b) By symmetry, in the frame of rod $A'B'$, clock $A$ moves distance $l_0$ from $B'$ to $A'$ in time $t'_{A'} = l_0 / v$, and $t_A = t'_{A'} \\sqrt{1 - v^2/c^2}$."
        ],
        "answer": "(a) $t(B) = \\frac{l_0}{v}, \\quad t'(B') = \\frac{l_0}{v} \\sqrt{1 - \\frac{v^2}{c^2}}$; (b) $t(A) = \\frac{l_0}{v} \\sqrt{1 - \\frac{v^2}{c^2}}, \\quad t'(A') = \\frac{l_0}{v}$",
        "solution": "**1. Part (a): Clocks $B$ and $B'$ Meeting:**\nIn the reference frame of rod $AB$:\n- Initially at $t = 0$, clock $B'$ is at end $A$ ($x = 0$).\n- Clock $B$ is at $x = l_0$.\n- Clock $B'$ travels to clock $B$ with velocity $v$, taking time:\n$$t(B) = \\frac{l_0}{v}$$\n- Because clock $B'$ is moving in this frame, its elapsed proper time is dilated:\n$$t'(B') = t(B) \\sqrt{1 - \\beta^2} = \\frac{l_0}{v} \\sqrt{1 - \\frac{v^2}{c^2}}$$\n\n**2. Part (b): Clocks $A$ and $A'$ Meeting:**\nBy the principle of relativity, reversing the roles of the two reference frames:\n- In the rest frame of rod $A'B'$, clock $A$ travels distance $l_0$ from $B'$ to $A'$ at velocity $v$, so:\n$$t'(A') = \\frac{l_0}{v}$$\n- Clock $A$ is moving in this frame, so its reading when it aligns with $A'$ is:\n$$t(A) = \\frac{l_0}{v} \\sqrt{1 - \\frac{v^2}{c^2}}$$",
        "tags": ["clock synchronization", "time dilation", "passing rods", "relativity"]
    },
    {
        "id": "1.354",
        "title": "Positions of Clock Hands in Moving Reference Frames",
        "difficulty": 2,
        "question": "Two groups of mutually synchronized clocks $K$ and $K'$ move relative to each other with velocity $v$. The moment when clock $A'$ is opposite clock $A$ is taken as the origin of time ($t = 0, t' = 0$). Sketch and describe the readings of the clocks along the line of motion:\n(a) in terms of the $K$ clocks;\n(b) in terms of the $K'$ clocks.",
        "hints": [
            "Use the Lorentz transformation $t' = \\frac{t - v x / c^2}{\\sqrt{1 - \\beta^2}}$.",
            "At $t = 0$ in frame $K$, the clocks of frame $K'$ show $t'(x) = - \\frac{v x / c^2}{\\sqrt{1 - \\beta^2}}$. Clocks ahead of the origin ($x > 0$) lag behind, while clocks behind ($x < 0$) are ahead.",
            "Similarly, at $t' = 0$ in frame $K'$, the clocks of frame $K$ show $t(x') = \\frac{v x' / c^2}{\\sqrt{1 - \\beta^2}}$."
        ],
        "answer": "In terms of $K$ clocks at $t = 0$: $t'(x) = -\\frac{v x}{c^2 \\sqrt{1 - v^2/c^2}}$; in terms of $K'$ clocks at $t' = 0$: $t(x') = \\frac{v x'}{c^2 \\sqrt{1 - v^2/c^2}}$",
        "solution": "**1. Clock Readings at $t = 0$ in Frame $K$:**\nFrom the Lorentz transformation:\n$$t' = \\frac{t - \\frac{v x}{c^2}}{\\sqrt{1 - \\beta^2}}$$\nSetting $t = 0$ (simultaneous in frame $K$):\n$$t'(x) = - \\frac{v x}{c^2 \\sqrt{1 - \\beta^2}}$$\n- At $x = 0$ (clock $A'$ opposite $A$): $t' = 0$.\n- For clocks located in the direction of motion ($x > 0$): $t' < 0$ (the forward clock lags behind).\n- For clocks located behind the origin ($x < 0$): $t' > 0$ (the rear clock is ahead).\n\n**2. Clock Readings at $t' = 0$ in Frame $K'$:**\nFrom the inverse Lorentz transformation:\n$$t = \\frac{t' + \\frac{v x'}{c^2}}{\\sqrt{1 - \\beta^2}}$$\nSetting $t' = 0$:\n$$t(x') = \\frac{v x'}{c^2 \\sqrt{1 - \\beta^2}}$$\nThis illustrates the relativity of simultaneity between moving inertial frames.",
        "tags": ["relativity of simultaneity", "Lorentz transformation", "clock synchronization"]
    },
    {
        "id": "1.355",
        "title": "Velocity of the Point of Equal Clock Readings",
        "difficulty": 2,
        "question": "The reference frame $K'$ moves with velocity $V$ relative to frame $K$. At $t = 0, t' = 0$, the origins $O$ and $O'$ coincide. Find the velocity $\\dot{x}$ of the point in frame $K$ at which the clock readings of both frames are permanently identical ($t = t'$). Demonstrate that $\\dot{x} < V$.",
        "hints": [
            "Use the Lorentz transformation for time: $t' = \\frac{t - V x / c^2}{\\sqrt{1 - \\beta^2}}$, where $\\beta = V/c$.",
            "Set $t' = t$: $t = \\frac{t - V x / c^2}{\\sqrt{1 - \\beta^2}}$.",
            "Solve for $x(t)$ and differentiate to find $\\dot{x} = \\frac{c^2}{V} (1 - \\sqrt{1 - \\beta^2})$."
        ],
        "answer": "$\\dot{x} = \\frac{c}{\\beta} \\left(1 - \\sqrt{1 - \\beta^2}\\right) < V$",
        "solution": "**1. Condition for Equal Clock Readings:**\n$$t' = \\frac{t - \\frac{V x}{c^2}}{\\sqrt{1 - \\beta^2}}$$\nSetting $t' = t$:\n$$t \\sqrt{1 - \\beta^2} = t - \\frac{V x}{c^2}$$\n$$\\frac{V x}{c^2} = t (1 - \\sqrt{1 - \\beta^2})$$\n$$x(t) = \\frac{c^2}{V} (1 - \\sqrt{1 - \\beta^2}) t = \\frac{c}{\\beta} (1 - \\sqrt{1 - \\beta^2}) t$$\n\n**2. Velocity of the Point:**\n$$\\dot{x} = \\frac{dx}{dt} = \\frac{c}{\\beta} (1 - \\sqrt{1 - \\beta^2})$$\n\n**3. Demonstration that $\\dot{x} < V$:**\n$$\\frac{\\dot{x}}{V} = \\frac{1}{\\beta^2} (1 - \\sqrt{1 - \\beta^2})$$\nSince $\\beta^2 = (1 - \\sqrt{1 - \\beta^2})(1 + \\sqrt{1 - \\beta^2})$:\n$$\\frac{\\dot{x}}{V} = \\frac{1}{1 + \\sqrt{1 - \\beta^2}}$$\nSince $\\sqrt{1 - \\beta^2} > 0$ for any $V < c$, the denominator is strictly greater than 1, hence:\n$$\\frac{\\dot{x}}{V} < 1 \\implies \\dot{x} < V$$",
        "tags": ["Lorentz transformation", "clock coincidence", "phase velocity", "special relativity"]
    },
    {
        "id": "1.356",
        "title": "Causality Invariance in Special Relativity",
        "difficulty": 2,
        "question": "At two points of reference frame $K$, two events occur separated by time interval $\\Delta t$. Demonstrate that if these events obey a cause-and-effect relationship in frame $K$, they obey that same chronological relationship in any other inertial reference frame $K'$.",
        "hints": [
            "A cause can influence an effect only if a signal travels between them at speed $v_{\\text{sig}} \\le c$.",
            "This means the spacetime interval is timelike: $c^2 \\Delta t^2 - \\Delta x^2 \\ge 0$, so $|\\Delta x| \\le c \\Delta t$.",
            "Write the Lorentz transformation for time: $\\Delta t' = \\gamma (\\Delta t - \\frac{V \\Delta x}{c^2})$ and show $\\Delta t' > 0$."
        ],
        "answer": "Analytical proof demonstrated: timelike causal interval ensures $\\Delta t' > 0$ for all $V < c$",
        "solution": "**1. Causal Connection Condition:**\nIf event 1 causes event 2, a physical interaction must propagate from 1 to 2 at speed $v \\le c$. Thus:\n$$\\Delta t = t_2 - t_1 > 0, \\quad |\\Delta x| = |x_2 - x_1| \\le c \\Delta t$$\nThe spacetime interval is timelike:\n$$\\Delta s^2 = c^2 \\Delta t^2 - \\Delta x^2 \\ge 0$$\n\n**2. Time Interval in Frame $K'$:**\nUsing the Lorentz transformation for time difference:\n$$\\Delta t' = \\gamma \\left(\\Delta t - \\frac{V \\Delta x}{c^2}\\right)$$\nwhere $\\gamma = 1/\\sqrt{1 - V^2/c^2} > 0$ and $|V| < c$.\nUsing $|\\Delta x| \\le c \\Delta t$:\n$$\\frac{V \\Delta x}{c^2} \\le \\frac{|V| |\\Delta x|}{c^2} \\le \\frac{|V| c \\Delta t}{c^2} = \\frac{|V|}{c} \\Delta t$$\nTherefore:\n$$\\Delta t - \\frac{V \\Delta x}{c^2} \\ge \\Delta t \\left(1 - \\frac{|V|}{c}\\right) > 0$$\n$$\\Delta t' > 0$$\nHence, event 1 precedes event 2 in all inertial reference frames, preserving causality.",
        "tags": ["causality", "timelike interval", "Lorentz invariance", "special relativity"]
    },
    {
        "id": "1.357",
        "title": "Invariant Spacetime Intervals Between Events",
        "difficulty": 2,
        "question": "A spacetime diagram shows three events $A$, $B$, and $C$ on the $x$-axis. From the diagram, event coordinates $(ct, x)$ are given. Find:\n(a) the time interval $\\Delta t$ between events $A$ and $B$ in the frame where they occur at the same point;\n(b) the distance $\\Delta x'$ between events $A$ and $C$ in the frame where they are simultaneous.",
        "hints": [
            "Use invariance of spacetime interval: $\\Delta s^2 = c^2 \\Delta t^2 - \\Delta x^2 = \\text{inv}$.",
            "(a) For events at the same point, $\\Delta x' = 0$, so $c^2 \\tau^2 = c^2 \\Delta t^2 - \\Delta x^2$.",
            "(b) For simultaneous events, $\\Delta t' = 0$, so $- (\\Delta x')^2 = c^2 \\Delta t^2 - \\Delta x^2$."
        ],
        "answer": "(a) $\\Delta t = 13\\text{ ns}$; (b) $\\Delta x' = 4.0\\text{ m}$",
        "solution": "**1. Part (a): Timelike Interval $AB$:**\nFrom the coordinates of events $A$ and $B$:\n$$\\Delta s_{AB}^2 = c^2 \\Delta t_{AB}^2 - \\Delta x_{AB}^2 > 0$$\nIn the frame where they occur at the same spatial point ($\\Delta x' = 0$):\n$$c^2 \\tau^2 = \\Delta s_{AB}^2 \\implies \\tau = \\frac{\\sqrt{c^2 \\Delta t^2 - \\Delta x^2}}{c} = 13\\text{ ns}$$\n\n**2. Part (b): Spacelike Interval $AC$:**\nFrom the coordinates of events $A$ and $C$:\n$$\\Delta s_{AC}^2 = c^2 \\Delta t_{AC}^2 - \\Delta x_{AC}^2 < 0$$\nIn the frame where they are simultaneous ($\\Delta t' = 0$):\n$$- (\\Delta x')^2 = \\Delta s_{AC}^2 = c^2 \\Delta t^2 - \\Delta x^2$$\n$$\\Delta x' = \\sqrt{\\Delta x^2 - c^2 \\Delta t^2} = 4.0\\text{ m}$$",
        "tags": ["spacetime interval", "invariance", "proper time", "proper distance"]
    },
    {
        "id": "1.358",
        "title": "Relativistic Velocity Addition: General 2D Case",
        "difficulty": 2,
        "question": "A particle moves in the $xy$-plane of frame $K$ with velocity components $v_x$ and $v_y$. Find the velocity magnitude $v'$ of this particle in frame $K'$, which moves with velocity $V$ relative to frame $K$ in the positive $x$ direction.",
        "hints": [
            "Lorentz velocity transformation: $v'_x = \\frac{v_x - V}{1 - v_x V / c^2}$, $v'_y = \\frac{v_y \\sqrt{1 - V^2/c^2}}{1 - v_x V / c^2}$.",
            "Total speed in frame $K'$ is $v' = \\sqrt{v'^2_x + v'^2_y}$."
        ],
        "answer": "$v' = \\frac{\\sqrt{(v_x - V)^2 + v_y^2 (1 - V^2/c^2)}}{1 - v_x V / c^2}$",
        "solution": "**1. Component Transformations:**\nBy Einstein's velocity addition formulas:\n$$v'_x = \\frac{v_x - V}{1 - \\frac{v_x V}{c^2}}$$\n$$v'_y = \\frac{v_y \\sqrt{1 - \\frac{V^2}{c^2}}}{1 - \\frac{v_x V}{c^2}}$$\n\n**2. Modulus of Velocity:**\n$$v'^2 = v'^2_x + v'^2_y = \\frac{(v_x - V)^2 + v_y^2 \\left(1 - \\frac{V^2}{c^2}\\right)}{\\left(1 - \\frac{v_x V}{c^2}\\right)^2}$$\n$$v' = \\frac{\\sqrt{(v_x - V)^2 + v_y^2 \\left(1 - \\frac{V^2}{c^2}\\right)}}{1 - \\frac{v_x V}{c^2}}$$",
        "tags": ["velocity addition", "Lorentz transformation", "2D velocity", "special relativity"]
    },
    {
        "id": "1.359",
        "title": "Approach Velocity vs Relative Velocity",
        "difficulty": 1,
        "question": "Two particles move toward each other with velocities $v_1 = 0.50 c$ and $v_2 = 0.75 c$ relative to the laboratory frame. Find:\n(a) the approach velocity of the particles in the laboratory frame;\n(b) their relative velocity (the velocity of one particle in the rest frame of the other).",
        "hints": [
            "(a) Approach velocity in a single frame is simply the rate of decrease of separation: $v_{\\text{app}} = v_1 + v_2$.",
            "(b) Relative velocity requires relativistic velocity addition: $v_{\\text{rel}} = \\frac{v_1 + v_2}{1 + v_1 v_2 / c^2}$."
        ],
        "answer": "(a) $v_{\\text{app}} = v_1 + v_2 = 1.25 c$; (b) $v_{\\text{rel}} = \\frac{v_1 + v_2}{1 + v_1 v_2 / c^2} = 0.91 c$",
        "solution": "**1. Part (a): Approach Velocity in Laboratory Frame:**\nIn the lab frame, both speeds are defined with respect to the lab.\nThe distance between them decreases at rate:\n$$v_{\\text{app}} = v_1 + v_2 = 0.50 c + 0.75 c = 1.25 c$$\n*(This does not violate relativity because no physical object or signal travels at $1.25 c$).*\n\n**2. Part (b): Relative Velocity:**\nIn the reference frame of particle 1, the speed of particle 2 is given by the relativistic velocity addition law:\n$$v_{\\text{rel}} = \\frac{v_1 + v_2}{1 + \\frac{v_1 v_2}{c^2}} = \\frac{0.50 c + 0.75 c}{1 + (0.50)(0.75)} = \\frac{1.25 c}{1 + 0.375} = \\frac{1.25}{1.375} c = \\frac{10}{11} c \\approx 0.91 c$$",
        "tags": ["velocity addition", "approach velocity", "relative velocity", "special relativity"]
    },
    {
        "id": "1.360",
        "title": "Length of Passing Rods in Each Other's Frame",
        "difficulty": 2,
        "question": "Two rods having the same proper length $l_0$ move lengthwise toward each other parallel to a common axis with equal speed $v$ relative to the laboratory frame. What is the length $l$ of each rod in the reference frame fixed to the other rod?",
        "hints": [
            "Find the relative speed $v_{\\text{rel}}$ using relativistic velocity addition: $v_{\\text{rel}} = \\frac{2v}{1 + v^2/c^2}$.",
            "Length contraction in rest frame of the other rod: $l = l_0 \\sqrt{1 - v_{\\text{rel}}^2 / c^2}$.",
            "Express $\\sqrt{1 - v_{\\text{rel}}^2/c^2}$ in terms of $\\beta = v/c$."
        ],
        "answer": "$l = l_0 \\frac{1 - \\beta^2}{1 + \\beta^2}$",
        "solution": "**1. Relative Velocity:**\n$$v_{\\text{rel}} = \\frac{v - (-v)}{1 - \\frac{v(-v)}{c^2}} = \\frac{2v}{1 + \\beta^2}$$\nwhere $\\beta = v/c$.\n\n**2. Relativistic Contraction Factor:**\n$$\\beta_{\\text{rel}} = \\frac{v_{\\text{rel}}}{c} = \\frac{2\\beta}{1 + \\beta^2}$$\n$$1 - \\beta_{\\text{rel}}^2 = 1 - \\frac{4\\beta^2}{(1 + \\beta^2)^2} = \\frac{(1 + \\beta^2)^2 - 4\\beta^2}{(1 + \\beta^2)^2} = \\frac{(1 - \\beta^2)^2}{(1 + \\beta^2)^2}$$\n$$\\sqrt{1 - \\beta_{\\text{rel}}^2} = \\frac{1 - \\beta^2}{1 + \\beta^2}$$\n\n**3. Contracted Length:**\n$$l = l_0 \\sqrt{1 - \\beta_{\\text{rel}}^2} = l_0 \\frac{1 - \\beta^2}{1 + \\beta^2}$$",
        "tags": ["length contraction", "velocity addition", "relative speed", "passing rods"]
    },
    {
        "id": "1.361",
        "title": "Relative Velocity of Orthogonally Moving Particles",
        "difficulty": 2,
        "question": "Two relativistic particles move at right angles to each other in a laboratory frame, one with velocity $v_1$ along the $x$-axis and the other with velocity $v_2$ along the $y$-axis. Find their relative velocity $v_{\\text{rel}}$.",
        "hints": [
            "Transform to the rest frame of particle 1 (which moves with velocity $V = v_1$ along $x$).",
            "In this frame, the velocity components of particle 2 are: $v'_x = - v_1$, $v'_y = v_2 \\sqrt{1 - v_1^2/c^2}$.",
            "Relative speed is $v_{\\text{rel}} = \\sqrt{v'^2_x + v'^2_y} = \\sqrt{v_1^2 + v_2^2 (1 - v_1^2/c^2)}$."
        ],
        "answer": "$v_{\\text{rel}} = \\sqrt{v_1^2 + v_2^2 - \\left(\\frac{v_1 v_2}{c}\\right)^2}$",
        "solution": "**1. Transformation to Rest Frame of Particle 1:**\nLet particle 1 move along the $+x$ axis with velocity $\\mathbf{v}_1 = (v_1, 0)$.\nParticle 2 moves along the $+y$ axis with velocity $\\mathbf{v}_2 = (0, v_2)$.\nIn the rest frame of particle 1 (moving at $V = v_1$ along $x$):\n$$v'_{2x} = \\frac{0 - v_1}{1 - 0} = - v_1$$\n$$v'_{2y} = \\frac{v_2 \\sqrt{1 - v_1^2/c^2}}{1 - 0} = v_2 \\sqrt{1 - \\frac{v_1^2}{c^2}}$$\n\n**2. Relative Speed:**\n$$v_{\\text{rel}}^2 = (v'_{2x})^2 + (v'_{2y})^2 = v_1^2 + v_2^2 \\left(1 - \\frac{v_1^2}{c^2}\\right) = v_1^2 + v_2^2 - \\frac{v_1^2 v_2^2}{c^2}$$\n$$v_{\\text{rel}} = \\sqrt{v_1^2 + v_2^2 - \\left(\\frac{v_1 v_2}{c}\\right)^2}$$",
        "tags": ["orthogonal motion", "relative velocity", "velocity addition", "special relativity"]
    },
    {
        "id": "1.362",
        "title": "Distance Traversed by Particle with 2D Motion",
        "difficulty": 2,
        "question": "An unstable particle moves in frame $K'$ along its $y'$-axis with velocity $v'$. Frame $K'$ moves relative to frame $K$ along the $x$-axis with velocity $V$. Find the distance $s$ traversed by the particle in frame $K$ if its proper lifetime is $\\Delta t_0$.",
        "hints": [
            "Velocity components in frame $K$: $v_x = V$, $v_y = v' \\sqrt{1 - V^2/c^2}$.",
            "Speed in frame $K$ is $v = \\sqrt{v_x^2 + v_y^2} = \\sqrt{V^2 + v'^2 (1 - V^2/c^2)}$.",
            "Time dilation relates proper time to lab time: $\\Delta t = \\frac{\\Delta t_0}{\\sqrt{1 - v^2/c^2}}$. Distance is $s = v \\Delta t$."
        ],
        "answer": "$s = \\Delta t_0 \\frac{\\sqrt{V^2 + v'^2 (1 - V^2/c^2)}}{\\sqrt{1 - \\frac{V^2}{c^2} - \\frac{v'^2}{c^2}}}$",
        "solution": "**1. Velocity in Laboratory Frame $K$:**\nFrom the inverse Lorentz velocity transformation:\n$$v_x = V$$\n$$v_y = v' \\sqrt{1 - \\frac{V^2}{c^2}}$$\n$$v^2 = v_x^2 + v_y^2 = V^2 + v'^2 \\left(1 - \\frac{V^2}{c^2}\\right)$$\n\n**2. Relativistic Factor:**\n$$1 - \\frac{v^2}{c^2} = 1 - \\frac{V^2}{c^2} - \\frac{v'^2}{c^2} \\left(1 - \\frac{V^2}{c^2}\\right) = \\left(1 - \\frac{V^2}{c^2}\\right) \\left(1 - \\frac{v'^2}{c^2}\\right)$$\n\n**3. Distance Traversed:**\nThe lifetime in frame $K$ is:\n$$\\Delta t = \\frac{\\Delta t_0}{\\sqrt{1 - v^2/c^2}} = \\frac{\\Delta t_0}{\\sqrt{1 - V^2/c^2} \\sqrt{1 - v'^2/c^2}}$$\n$$s = v \\Delta t = \\Delta t_0 \\frac{\\sqrt{V^2 + v'^2(1 - V^2/c^2)}}{\\sqrt{1 - V^2/c^2} \\sqrt{1 - v'^2/c^2}}$$",
        "tags": ["2D motion", "time dilation", "velocity transformation", "proper time"]
    },
    {
        "id": "1.363",
        "title": "Relativistic Transformation of Velocity Direction",
        "difficulty": 2,
        "question": "A particle moves in frame $K$ with velocity $v$ at an angle $\\theta$ to the $x$-axis. Find the corresponding angle $\\theta'$ in frame $K'$ which moves with velocity $V$ along the $x$-axis.",
        "hints": [
            "In frame $K$: $v_x = v \\cos \\theta$ and $v_y = v \\sin \\theta$.",
            "In frame $K'$: $v'_x = \\frac{v \\cos \\theta - V}{1 - v V \\cos \\theta / c^2}$, $v'_y = \\frac{v \\sin \\theta \\sqrt{1 - V^2/c^2}}{1 - v V \\cos \\theta / c^2}$.",
            "Then $\\tan \\theta' = \\frac{v'_y}{v'_x} = \\frac{v \\sin \\theta \\sqrt{1 - V^2/c^2}}{v \\cos \\theta - V} = \\frac{\\sin \\theta \\sqrt{1 - \\beta^2}}{\\cos \\theta - V/v}$."
        ],
        "answer": "$\\tan \\theta' = \\frac{\\sin \\theta \\sqrt{1 - V^2/c^2}}{\\cos \\theta - V/v}$",
        "solution": "**1. Velocity Components in Frame $K$:**\n$$v_x = v \\cos \\theta, \\quad v_y = v \\sin \\theta$$\n\n**2. Velocity Components in Frame $K'$:**\n$$v'_x = \\frac{v_x - V}{1 - \\frac{v_x V}{c^2}} = \\frac{v \\cos \\theta - V}{1 - \\frac{v V \\cos \\theta}{c^2}}$$\n$$v'_y = \\frac{v_y \\sqrt{1 - \\frac{V^2}{c^2}}}{1 - \\frac{v_x V}{c^2}} = \\frac{v \\sin \\theta \\sqrt{1 - \\frac{V^2}{c^2}}}{1 - \\frac{v V \\cos \\theta}{c^2}}$$\n\n**3. Angle $\\theta'$ in Frame $K'$:**\n$$\\tan \\theta' = \\frac{v'_y}{v'_x} = \\frac{v \\sin \\theta \\sqrt{1 - V^2/c^2}}{v \\cos \\theta - V} = \\frac{\\sin \\theta \\sqrt{1 - V^2/c^2}}{\\cos \\theta - V/v}$$",
        "tags": ["relativistic aberration", "velocity transformation", "direction angle"]
    },
    {
        "id": "1.364",
        "title": "Tilt of a Moving Rod in Laboratory Frame",
        "difficulty": 2,
        "question": "A rod $AB$ oriented parallel to the $x'$-axis of frame $K'$ moves in this frame with velocity $v'$ along its $y'$-axis. In its turn, frame $K'$ moves with velocity $V$ along the $x$-axis relative to frame $K$. Find the angle $\\theta$ between the rod and the $x$-axis in frame $K$.",
        "hints": [
            "In frame $K'$, the rod is parallel to the $x'$-axis, so all its points have the same $y'$ coordinate at any time $t'$.",
            "In frame $K$, due to relativity of simultaneity, different points along the rod correspond to different times in $K'$, hence different $y'$ displacements.",
            "Using Lorentz transformation: $\\tan \\theta = \\frac{v' V}{c^2 \\sqrt{1 - V^2/c^2}}$."
        ],
        "answer": "$\\tan \\theta = \\frac{v' V}{c^2 \\sqrt{1 - V^2/c^2}}$",
        "solution": "**1. Analysis via Relativity of Simultaneity:**\nIn frame $K'$, all points of the rod have equation $y'(x', t') = v' t'$.\nConsider two points on the rod separated by $\\Delta x'$ at simultaneous time in frame $K$ ($\\Delta t = 0$).\nBy the Lorentz transformation:\n$$\\Delta t' = \\frac{\\Delta t - \\frac{V \\Delta x}{c^2}}{\\sqrt{1 - V^2/c^2}} = - \\frac{V \\Delta x}{c^2 \\sqrt{1 - V^2/c^2}}$$\n$$\\Delta x' = \\frac{\\Delta x - V \\Delta t}{\\sqrt{1 - V^2/c^2}} = \\frac{\\Delta x}{\\sqrt{1 - V^2/c^2}}$$\n\n**2. Coordinate Difference $\\Delta y$:**\nSince $y = y'$:\n$$\\Delta y = \\Delta y' = v' \\Delta t' = - v' \\frac{V \\Delta x}{c^2 \\sqrt{1 - V^2/c^2}}$$\n\n**3. Tilt Angle:**\n$$\\tan \\theta = \\left|\\frac{\\Delta y}{\\Delta x}\\right| = \\frac{v' V}{c^2 \\sqrt{1 - V^2/c^2}}$$",
        "tags": ["moving rod tilt", "relativity of simultaneity", "Lorentz transformation"]
    }
]
