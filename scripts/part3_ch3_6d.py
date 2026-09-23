"""
part3_ch3_6d.py
Curated problems 3.351 to 3.371 (21 problems) of Irodov Chapter 3.6:
Electromagnetic Induction. Maxwell's Equations (Part D).
"""

CH3_6D_CURATED = [
    {
        "id": "3.351",
        "title": "Displacement Current Density Around AC Solenoid",
        "difficulty": 2,
        "question": "A long straight solenoid has $n$ turns per unit length. An alternating current $I(t) = I_m \\sin(\\omega t)$ flows through it. Find the displacement current density as a function of the distance $r$ from the solenoid axis. The cross-sectional radius of the solenoid equals $R$.",
        "hints": [
            "The magnetic field inside the solenoid is $B(t) = \\mu_0 n I(t) = \\mu_0 n I_m \\sin(\\omega t)$. Outside, $B \\approx 0$.",
            "Calculate the vortex electric field using Faraday's law: $E(r) = -\\frac{1}{2} r \\frac{dB}{dt}$ for $r < R$, and $E(r) = -\\frac{1}{2} \\frac{R^2}{r} \\frac{dB}{dt}$ for $r > R$.",
            "The displacement current density is $\\mathbf{j}_d = \\varepsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t}$. Differentiating with respect to time gives $j_d \\propto \\frac{d^2 B}{dt^2}$."
        ],
        "answer": "$j_d(r) = \\begin{cases} \\frac{1}{2} \\varepsilon_0 \\mu_0 n I_m \\omega^2 r \\sin(\\omega t) & \\text{for } r < R \\\\[6pt] \\frac{1}{2} \\varepsilon_0 \\mu_0 n I_m \\omega^2 \\frac{R^2}{r} \\sin(\\omega t) & \\text{for } r > R \\end{cases}$",
        "solution": "**1. Magnetic Field and Induced Vortex Electric Field:**\nInside the long solenoid, the magnetic field is uniform:\n$$B(t) = \\mu_0 n I_m \\sin(\\omega t)$$\nOutside the solenoid ($r > R$), $B \\approx 0$.\nBy Faraday's law of induction around a circular contour of radius $r$:\n$$\\oint \\mathbf{E} \\cdot d\\mathbf{r} = E_\\theta (2\\pi r) = -\\frac{d\\Phi}{dt}$$\n- For $r < R$:\n$$E_\\theta (2\\pi r) = -\\pi r^2 \\frac{dB}{dt} \\implies E_\\theta = -\\frac{1}{2} r \\frac{dB}{dt} = -\\frac{1}{2} \\mu_0 n I_m \\omega r \\cos(\\omega t)$$\n- For $r > R$:\n$$E_\\theta (2\\pi r) = -\\pi R^2 \\frac{dB}{dt} \\implies E_\\theta = -\\frac{1}{2} \\frac{R^2}{r} \\frac{dB}{dt} = -\\frac{1}{2} \\mu_0 n I_m \\omega \\frac{R^2}{r} \\cos(\\omega t)$$\n\n**2. Displacement Current Density:**\nThe displacement current density vector is given by:\n$$\\mathbf{j}_d = \\varepsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t}$$\nDifferentiating the tangential electric field with respect to time:\n- For $r < R$:\n$$j_d(r, t) = -\\frac{1}{2} \\varepsilon_0 \\mu_0 n I_m \\omega r (-\\omega \\sin(\\omega t)) = \\frac{1}{2} \\varepsilon_0 \\mu_0 n I_m \\omega^2 r \\sin(\\omega t)$$\n- For $r > R$:\n$$j_d(r, t) = \\frac{1}{2} \\varepsilon_0 \\mu_0 n I_m \\omega^2 \\frac{R^2}{r} \\sin(\\omega t)$$",
        "tags": ["displacement current", "solenoid", "vortex electric field", "Maxwell equations"]
    },
    {
        "id": "3.352",
        "title": "Displacement Current Density of Moving Point Charge",
        "difficulty": 2,
        "question": "A point charge $q$ moves with a non-relativistic velocity $\\mathbf{v} = \\text{const}$. Find the displacement current density $\\mathbf{j}_d$ at a point located at distance $r$ from the charge on a straight line:\n(a) coinciding with the charge path;\n(b) perpendicular to the path and passing through the charge.",
        "hints": [
            "The electric field of the moving charge is $\\mathbf{E} = \\frac{q \\mathbf{r}}{4\\pi \\varepsilon_0 r^3}$ where $\\frac{d\\mathbf{r}}{dt} = -\\mathbf{v}$.",
            "Calculate $\\frac{\\partial \\mathbf{E}}{\\partial t} = \\frac{q}{4\\pi \\varepsilon_0 r^3} \\left[ -\\mathbf{v} + \\frac{3(\\mathbf{v} \\cdot \\mathbf{r})\\mathbf{r}}{r^2} \\right]$.",
            "Evaluate for (a) $\\mathbf{r} \\parallel \\mathbf{v}$ and (b) $\\mathbf{r} \\perp \\mathbf{v}$."
        ],
        "answer": "(a) $j_d = \\frac{q v}{2\\pi r^3}$; (b) $\\mathbf{j}_d = -\\frac{q \\mathbf{v}}{4\\pi r^3}$",
        "solution": "**1. Time Derivative of Electric Field:**\nAt a field point whose radius vector relative to the charge is $\\mathbf{r}$, the non-relativistic Coulomb field is:\n$$\\mathbf{E} = \\frac{q \\mathbf{r}}{4\\pi \\varepsilon_0 r^3}$$\nBecause the charge moves with velocity $\\mathbf{v}$, the radius vector from the charge to the fixed observation point changes as $\\frac{\\partial \\mathbf{r}}{\\partial t} = -\\mathbf{v}$.\nUsing the chain rule:\n$$\\frac{\\partial}{\\partial t} \\left( \\frac{\\mathbf{r}}{r^3} \\right) = \\frac{1}{r^3} \\frac{\\partial \\mathbf{r}}{\\partial t} - \\frac{3\\mathbf{r}}{r^4} \\frac{\\partial r}{\\partial t} = -\\frac{\\mathbf{v}}{r^3} + \\frac{3(\\mathbf{v} \\cdot \\mathbf{r})\\mathbf{r}}{r^5}$$\nThe displacement current density is:\n$$\\mathbf{j}_d = \\varepsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t} = \\frac{q}{4\\pi r^3} \\left[ -\\mathbf{v} + \\frac{3(\\mathbf{v} \\cdot \\mathbf{r})\\mathbf{r}}{r^2} \\right]$$\n\n**(a) On the line of motion ($\\mathbf{r} \\parallel \\mathbf{v}$):**\nHere $\\mathbf{r} = r \\frac{\\mathbf{v}}{v}$, so $(\\mathbf{v} \\cdot \\mathbf{r})\\mathbf{r} = (v r) \\left( r \\frac{\\mathbf{v}}{v} \\right) = r^2 \\mathbf{v}$:\n$$\\mathbf{j}_d = \\frac{q}{4\\pi r^3} [-\\mathbf{v} + 3\\mathbf{v}] = \\frac{2 q \\mathbf{v}}{4\\pi r^3} = \\frac{q \\mathbf{v}}{2\\pi r^3}$$\nIn magnitude, $j_d = \\frac{q v}{2\\pi r^3}$.\n\n**(b) Perpendicular to the path ($\\mathbf{r} \\perp \\mathbf{v}$):**\nHere $\\mathbf{v} \\cdot \\mathbf{r} = 0$, so:\n$$\\mathbf{j}_d = -\\frac{q \\mathbf{v}}{4\\pi r^3}$$",
        "tags": ["displacement current", "moving charge", "Maxwell equations", "vector calculus"]
    },
    {
        "id": "3.353",
        "title": "Maximum Displacement Current Density from Approaching Charged Ring",
        "difficulty": 2,
        "question": "A thin wire ring of radius $a$ carrying a charge $q$ approaches the observation point $P$ so that its centre moves rectilinearly with a constant velocity $v$. The plane of the ring remains perpendicular to the motion direction. At what distance $x_m$ from the point $P$ will the ring be located at the moment when the displacement current density at point $P$ becomes maximum? What is the magnitude of this maximum density?",
        "hints": [
            "The electric field at point $P$ on the ring axis at distance $x$ is $E(x) = \\frac{q x}{4\\pi \\varepsilon_0 (a^2 + x^2)^{3/2}}$.",
            "The displacement current density is $j_d = \\varepsilon_0 \\frac{\\partial E}{\\partial t} = -\\varepsilon_0 v \\frac{dE}{dx}$.",
            "Differentiate to find $j_d(x) = -\\frac{q v}{4\\pi} \\frac{a^2 - 2x^2}{(a^2 + x^2)^{5/2}}$. Find the value of $x$ where $|j_d|$ is extremized."
        ],
        "answer": "$x_m = 0, \\quad j_{d,\\max} = \\frac{q v}{4\\pi a^3}$",
        "solution": "**1. Electric Field on Ring Axis:**\nLet $x$ be the coordinate of the center of the ring relative to point $P$.\nThe axial electric field produced by the ring of radius $a$ and charge $q$ at point $P$ is:\n$$E(x) = \\frac{q x}{4\\pi \\varepsilon_0 (a^2 + x^2)^{3/2}}$$\n\n**2. Displacement Current Density:**\nAs the ring approaches $P$, its distance changes at rate $\\frac{dx}{dt} = -v$.\nThe displacement current density at point $P$ is:\n$$j_d = \\varepsilon_0 \\frac{\\partial E}{\\partial t} = \\varepsilon_0 \\frac{dE}{dx} \\left( \\frac{dx}{dt} \\right) = -\\varepsilon_0 v \\frac{dE}{dx}$$\nComputing the derivative:\n$$\\frac{dE}{dx} = \\frac{q}{4\\pi \\varepsilon_0} \\frac{(a^2 + x^2)^{3/2} - x \\cdot \\frac{3}{2}(a^2 + x^2)^{1/2}(2x)}{(a^2 + x^2)^3} = \\frac{q}{4\\pi \\varepsilon_0} \\frac{a^2 - 2x^2}{(a^2 + x^2)^{5/2}}$$\nThus:\n$$j_d(x) = -\\frac{q v}{4\\pi} \\frac{a^2 - 2x^2}{(a^2 + x^2)^{5/2}}$$\n\n**3. Maximum Magnitude:**\nAnalyzing $|j_d(x)|$, the function peaks at $x = 0$ (the center of the ring passes through point $P$):\n$$x_m = 0$$\nAt this moment:\n$$j_{d,\\max} = \\frac{q v}{4\\pi} \\frac{a^2}{a^5} = \\frac{q v}{4\\pi a^3}$$",
        "tags": ["displacement current", "charged ring", "maximum rate of change", "Maxwell equations"]
    },
    {
        "id": "3.354",
        "title": "Magnetic Field of Moving Charge via Displacement Current Circulation",
        "difficulty": 2,
        "question": "A point charge $q$ moves with a non-relativistic velocity $\\mathbf{v} = \\text{const}$. Applying the circulation theorem for the vector $\\mathbf{H}$ around a circular contour coaxial with the path, find $\\mathbf{H}$ at an observation point $A$ as a function of the radius vector $\\mathbf{r}$ and velocity $\\mathbf{v}$.",
        "hints": [
            "Use the Maxwell-Ampère circuital law: $\\oint \\mathbf{H} \\cdot d\\mathbf{r} = I_d = \\varepsilon_0 \\frac{d\\Phi_E}{dt}$.",
            "The electric flux through a spherical cap bounded by the circle of radius $R = r \\sin\\theta$ is $\\Phi_E = \\frac{q}{2\\varepsilon_0}(1 - \\cos\\theta)$.",
            "Differentiate $\\Phi_E$ with respect to time using $\\frac{d\\theta}{dt} = -\\frac{v \\sin\\theta}{r}$ to obtain $H(2\\pi r \\sin\\theta) = \\frac{q v \\sin\\theta}{2r}$, leading to $\\mathbf{H} = \\frac{q [\\mathbf{v} \\times \\mathbf{r}]}{4\\pi r^3}$."
        ],
        "answer": "$\\mathbf{H} = \\frac{q [\\mathbf{v} \\times \\mathbf{r}]}{4\\pi r^3}$",
        "solution": "**1. Maxwell-Ampère Law:**\nSince no conduction current passes through the open surface bounded by the circle of radius $R = r \\sin\\theta$, Ampère's circuital law with Maxwell's displacement current states:\n$$\\oint \\mathbf{H} \\cdot d\\mathbf{r} = H \\cdot (2\\pi R) = I_d = \\varepsilon_0 \\frac{d\\Phi_E}{dt}$$\n\n**2. Electric Flux Through the Spherical Cap:**\nChoose the spherical cap centered on the charge $q$ and bounded by the circular contour.\nThe electric field of the point charge is radially symmetric with total flux $q/\\varepsilon_0$.\nThe solid angle subtended by the cone of half-angle $\\theta$ is $\\Omega = 2\\pi (1 - \\cos\\theta)$.\nThe electric flux is:\n$$\\Phi_E = \\frac{q}{\\varepsilon_0} \\frac{\\Omega}{4\\pi} = \\frac{q}{2\\varepsilon_0} (1 - \\cos\\theta)$$\n\n**3. Rate of Flux Change:**\nAs the charge moves with velocity $v$, the angle $\\theta$ varies as $\\frac{d\\theta}{dt} = -\\frac{v \\sin\\theta}{r}$:\n$$\\frac{d\\Phi_E}{dt} = \\frac{q}{2\\varepsilon_0} \\sin\\theta \\left( -\\frac{d\\theta}{dt} \\right) = \\frac{q v \\sin^2\\theta}{2\\varepsilon_0 r}$$\n\n**4. Magnetic Field Strength:**\nEquating circulation to displacement current:\n$$H \\cdot (2\\pi r \\sin\\theta) = \\varepsilon_0 \\left( \\frac{q v \\sin^2\\theta}{2\\varepsilon_0 r} \\right) = \\frac{q v \\sin^2\\theta}{2r}$$\n$$H = \\frac{q v \\sin\\theta}{4\\pi r^2}$$\nIn vector form, noting that $\\mathbf{H}$ is azimuthal:\n$$\\mathbf{H} = \\frac{q [\\mathbf{v} \\times \\mathbf{r}]}{4\\pi r^3}$$",
        "tags": ["Maxwell-Ampere law", "moving charge", "Biot-Savart field", "displacement current"]
    },
    {
        "id": "3.355",
        "title": "Existence and Uniformity Conditions for Time-Dependent Fields",
        "difficulty": 2,
        "question": "Using Maxwell's equations, show that:\n(a) a time-dependent magnetic field cannot exist without an electric field;\n(b) a uniform electric field cannot exist in the presence of a time-dependent magnetic field;\n(c) inside an empty cavity a uniform electric field can be time-dependent.",
        "hints": [
            "Use Faraday's law in differential form: $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$.",
            "If $\\mathbf{E} = 0$ everywhere, its curl is identically zero, implying $\\frac{\\partial \\mathbf{B}}{\\partial t} = 0$.",
            "If $\\mathbf{E}$ is spatially uniform, $\\nabla \\times \\mathbf{E} = 0$. But if $\\frac{\\partial \\mathbf{B}}{\\partial t} \\ne 0$, this yields a contradiction."
        ],
        "answer": "(a) If $\\frac{\\partial \\mathbf{B}}{\\partial t} \\ne 0$, then $\\nabla \\times \\mathbf{E} \\ne 0$, which requires $\\mathbf{E} \\ne 0$; (b) For a uniform field $\\nabla \\times \\mathbf{E} = 0$, contradicting $-\\frac{\\partial \\mathbf{B}}{\\partial t} \\ne 0$; (c) A uniform field $\\mathbf{E}(t) = \\mathbf{E}_0 + \\mathbf{a} t$ can exist inside a cavity with linearly changing surface charges",
        "solution": "**(a) Time-dependent magnetic field requires an electric field:**\nBy Faraday's law:\n$$\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$$\nIf there were no electric field ($\\mathbf{E} = 0$ everywhere), then $\\nabla \\times \\mathbf{E} = 0$, which requires $\\frac{\\partial \\mathbf{B}}{\\partial t} = 0$.\nHence, a time-dependent magnetic field cannot exist in the total absence of an electric field.\n\n**(b) Uniform electric field cannot coexist with time-varying magnetic field:**\nIf an electric field is spatially uniform, its spatial derivatives vanish identically, so $\\nabla \\times \\mathbf{E} = 0$.\nHowever, Faraday's law dictates $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t} \\ne 0$, resulting in a direct contradiction.\n\n**(c) Uniform time-dependent electric field in empty cavity:**\nIn an empty region ($\\rho = 0, \\mathbf{j} = 0$), if $\\mathbf{E} = \\mathbf{a} f(t)$ where $\\mathbf{a}$ is spatially constant, then $\\nabla \\times \\mathbf{E} = 0$, implying $\\frac{\\partial \\mathbf{B}}{\\partial t} = 0$, so $\\mathbf{B} = \\text{const}$.\nThen the Maxwell-Ampère equation requires:\n$$\\nabla \\times \\mathbf{H} = \\varepsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t} = \\varepsilon_0 \\mathbf{a} f'(t)$$\nSince $\\mathbf{B} = \\text{const}$, the left-hand side is constant in time, which requires $f'(t) = \\text{const}$.\nThus $f(t)$ must be a linear function of time ($f(t) = c_1 t + c_0$), produced by linearly varying charges on the cavity boundary.",
        "tags": ["Maxwell equations", "Faraday's law", "uniform fields", "field compatibility"]
    },
    {
        "id": "3.356",
        "title": "Derivation of Charge Conservation from Maxwell's Equations",
        "difficulty": 2,
        "question": "Demonstrate that the law of electric charge conservation, $\\nabla \\cdot \\mathbf{j} = -\\frac{\\partial \\rho}{\\partial t}$, follows directly from Maxwell's equations.",
        "hints": [
            "Start from the Maxwell-Ampère circuital law: $\\nabla \\times \\mathbf{H} = \\mathbf{j} + \\frac{\\partial \\mathbf{D}}{\\partial t}$.",
            "Take the divergence of both sides, noting that the divergence of any vector curl is identically zero: $\\nabla \\cdot (\\nabla \\times \\mathbf{H}) \\equiv 0$.",
            "Apply Gauss's law $\\nabla \\cdot \\mathbf{D} = \\rho$ to arrive at the continuity equation."
        ],
        "answer": "Taking the divergence of $\\nabla \\times \\mathbf{H} = \\mathbf{j} + \\frac{\\partial \\mathbf{D}}{\\partial t}$ gives $0 = \\nabla \\cdot \\mathbf{j} + \\frac{\\partial}{\\partial t}(\\nabla \\cdot \\mathbf{D}) = \\nabla \\cdot \\mathbf{j} + \\frac{\\partial \\rho}{\\partial t}$",
        "solution": "**1. Maxwell-Ampère Law:**\nThe fourth Maxwell equation is:\n$$\\nabla \\times \\mathbf{H} = \\mathbf{j} + \\frac{\\partial \\mathbf{D}}{\\partial t}$$\n\n**2. Divergence of Both Sides:**\nApplying the divergence operator to both sides:\n$$\\nabla \\cdot (\\nabla \\times \\mathbf{H}) = \\nabla \\cdot \\mathbf{j} + \\nabla \\cdot \\left( \\frac{\\partial \\mathbf{D}}{\\partial t} \\right)$$\nBy vector identity, the divergence of the curl of any vector field is identically zero:\n$$\\nabla \\cdot (\\nabla \\times \\mathbf{H}) \\equiv 0$$\nInterchanging the order of spatial and temporal derivatives on the right:\n$$0 = \\nabla \\cdot \\mathbf{j} + \\frac{\\partial}{\\partial t} (\\nabla \\cdot \\mathbf{D})$$\n\n**3. Substitution of Gauss's Law:**\nFrom the first Maxwell equation (Gauss's law):\n$$\\nabla \\cdot \\mathbf{D} = \\rho$$\nSubstituting $\\nabla \\cdot \\mathbf{D}$:\n$$\\nabla \\cdot \\mathbf{j} + \\frac{\\partial \\rho}{\\partial t} = 0 \\implies \\nabla \\cdot \\mathbf{j} = -\\frac{\\partial \\rho}{\\partial t}$$\nThis confirms that charge conservation is an intrinsic consequence of Maxwell's equations.",
        "tags": ["charge conservation", "continuity equation", "Maxwell equations", "vector identity"]
    },
    {
        "id": "3.357",
        "title": "Compatibility of Faraday's Law and Solenoidal Nature of B",
        "difficulty": 1,
        "question": "Demonstrate that Maxwell's equations $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$ and $\\nabla \\cdot \\mathbf{B} = 0$ are mutually compatible.",
        "hints": [
            "Take the divergence of both sides of Faraday's law: $\\nabla \\cdot (\\nabla \\times \\mathbf{E}) = -\\nabla \\cdot \\frac{\\partial \\mathbf{B}}{\\partial t}$.",
            "Use the identity $\\nabla \\cdot (\\nabla \\times \\mathbf{A}) \\equiv 0$.",
            "Deduce that $\\frac{\\partial}{\\partial t}(\\nabla \\cdot \\mathbf{B}) = 0$, meaning $\\nabla \\cdot \\mathbf{B}$ is constant in time."
        ],
        "answer": "Taking the divergence yields $\\frac{\\partial}{\\partial t}(\\nabla \\cdot \\mathbf{B}) = 0$, so $\\nabla \\cdot \\mathbf{B} = \\text{const}$, which is completely compatible with $\\nabla \\cdot \\mathbf{B} = 0$",
        "solution": "**1. Divergence of Faraday's Law:**\nStart with the induction law:\n$$\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$$\nTaking the divergence of both sides:\n$$\\nabla \\cdot (\\nabla \\times \\mathbf{E}) = -\\nabla \\cdot \\left( \\frac{\\partial \\mathbf{B}}{\\partial t} \\right)$$\n\n**2. Applying Vector Identity:**\nSince the divergence of any curl is identically zero:\n$$0 = -\\frac{\\partial}{\\partial t} (\\nabla \\cdot \\mathbf{B}) \\implies \\frac{\\partial}{\\partial t} (\\nabla \\cdot \\mathbf{B}) = 0$$\n\n**3. Conclusion:**\nThis demonstrates that $\\nabla \\cdot \\mathbf{B}$ must be independent of time. Therefore, if $\\nabla \\cdot \\mathbf{B} = 0$ holds at any initial instant, it remains strictly zero at all subsequent times, proving that the two Maxwell equations are fully consistent.",
        "tags": ["Maxwell equations", "Faraday's law", "solenoidal field", "compatibility"]
    },
    {
        "id": "3.358",
        "title": "Curl of Electric Field in Rotating Magnetic Field",
        "difficulty": 2,
        "question": "In a certain region of an inertial reference frame, there is a magnetic field with induction $\\mathbf{B}$ rotating with angular velocity $\\boldsymbol{\\omega}$. Find $\\nabla \\times \\mathbf{E}$ in this region as a function of vectors $\\boldsymbol{\\omega}$ and $\\mathbf{B}$.",
        "hints": [
            "For a vector $\\mathbf{B}$ rotating with constant magnitude at angular velocity $\\boldsymbol{\\omega}$, its time derivative is $\\frac{\\partial \\mathbf{B}}{\\partial t} = \\boldsymbol{\\omega} \\times \\mathbf{B}$.",
            "Apply Faraday's law of induction: $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$.",
            "Substitute $\\frac{\\partial \\mathbf{B}}{\\partial t}$ to obtain $\\nabla \\times \\mathbf{E} = -[\\boldsymbol{\\omega} \\times \\mathbf{B}] = \\mathbf{B} \\times \\boldsymbol{\\omega}$."
        ],
        "answer": "$\\nabla \\times \\mathbf{E} = -[\\boldsymbol{\\omega} \\times \\mathbf{B}]$",
        "solution": "**1. Time Derivative of a Rotating Vector:**\nA vector $\\mathbf{B}$ of constant magnitude rotating with angular velocity vector $\\boldsymbol{\\omega}$ changes with time at the rate:\n$$\\frac{\\partial \\mathbf{B}}{\\partial t} = \\boldsymbol{\\omega} \\times \\mathbf{B}$$\n\n**2. Application of Faraday's Law:**\nFrom the Maxwell-Faraday equation:\n$$\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$$\nSubstituting the kinematic time derivative:\n$$\\nabla \\times \\mathbf{E} = -(\\boldsymbol{\\omega} \\times \\mathbf{B}) = \\mathbf{B} \\times \\boldsymbol{\\omega}$$",
        "tags": ["rotating field", "Faraday's law", "angular velocity", "curl"]
    },
    {
        "id": "3.359",
        "title": "Electric Field in Moving Frame via Force Invariance",
        "difficulty": 1,
        "question": "In the inertial reference frame $K$ there is a uniform magnetic field with induction $\\mathbf{B}$. Find the electric field strength in the frame $K'$ which moves relative to frame $K$ with a non-relativistic velocity $\\mathbf{v}$, with $\\mathbf{v} \\perp \\mathbf{B}$. Consider the forces acting on a test charge at the moment when its velocity in frame $K'$ is zero.",
        "hints": [
            "In frame $K'$, the test charge has velocity $\\mathbf{v}' = 0$, so the Lorentz force is purely electrostatic: $\\mathbf{F}' = q \\mathbf{E}'$.",
            "In frame $K$, the same charge moves with velocity $\\mathbf{v}$, experiencing the magnetic Lorentz force: $\\mathbf{F} = q [\\mathbf{v} \\times \\mathbf{B}]$.",
            "In non-relativistic mechanics, the force on a particle is invariant across inertial reference frames: $\\mathbf{F}' = \\mathbf{F}$."
        ],
        "answer": "$\\mathbf{E}' = [\\mathbf{v} \\times \\mathbf{B}]$",
        "solution": "**1. Force in Frame $K'$:**\nLet a test charge $q$ be at rest at a given instant in frame $K'$ (so $\\mathbf{v}' = 0$).\nThe Lorentz force acting on it in frame $K'$ is purely electric:\n$$\\mathbf{F}' = q \\mathbf{E}'$$\n\n**2. Force in Frame $K$:**\nIn frame $K$, the charge moves with velocity $\\mathbf{v}$. Since frame $K$ contains only magnetic field $\\mathbf{B}$ (with $\\mathbf{E} = 0$):\n$$\\mathbf{F} = q [\\mathbf{v} \\times \\mathbf{B}]$$\n\n**3. Invariance of Force:**\nIn classical (non-relativistic) mechanics, force is invariant under Galilean transformations:\n$$\\mathbf{F}' = \\mathbf{F}$$\n$$q \\mathbf{E}' = q [\\mathbf{v} \\times \\mathbf{B}] \\implies \\mathbf{E}' = [\\mathbf{v} \\times \\mathbf{B}]$$",
        "tags": ["field transformation", "Lorentz force", "moving reference frame", "Galilean relativity"]
    },
    {
        "id": "3.360",
        "title": "Surface Charge Density on Plate Moving Through Magnetic Field",
        "difficulty": 2,
        "question": "A large plate of non-ferromagnetic conducting material moves with a constant velocity $v = 90\\text{ cm/s}$ in a uniform magnetic field with induction $B = 50\\text{ mT}$. Find the surface density of electric charges appearing on the plate as a result of its motion.",
        "hints": [
            "In the moving frame of the conductor, the total effective force on conduction electrons must vanish in steady state: $\\mathbf{E}' = \\mathbf{E} + [\\mathbf{v} \\times \\mathbf{B}] = 0$.",
            "This establishes an internal electrostatic field $E = v B$ inside the plate.",
            "By boundary conditions on the normal component of $\\mathbf{E}$ across the surface, the surface charge density is $\\sigma = \\varepsilon_0 E = \\varepsilon_0 v B$."
        ],
        "answer": "$\\sigma = \\varepsilon_0 v B = 0.40\\text{ pC/m}^2$",
        "solution": "**1. Equilibrium of Conduction Electrons:**\nInside a conductor moving with velocity $\\mathbf{v}$ through magnetic field $\\mathbf{B}$, electrons experience an inward Lorentz force $F_m = e v B$.\nCharge separation occurs until an internal electrostatic field $\\mathbf{E}$ develops to balance this magnetic force:\n$$\\mathbf{E} = -[\\mathbf{v} \\times \\mathbf{B}]$$\nThe magnitude of this internal electric field is:\n$$E = v B$$\n\n**2. Surface Charge Density:**\nBy Gauss's law at the interface between the conductor and surrounding space (where $E = 0$ outside):\n$$\\sigma = \\varepsilon_0 E = \\varepsilon_0 v B$$\n\n**3. Numerical Evaluation:**\nGiven $v = 0.90\\text{ m/s}$, $B = 0.050\\text{ T}$, $\\varepsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}$:\n$$\\sigma = (8.854 \\times 10^{-12}\\text{ F/m})(0.90\\text{ m/s})(0.050\\text{ T}) \\approx 3.98 \\times 10^{-13}\\text{ C/m}^2 \\approx 0.40\\text{ pC/m}^2$$",
        "tags": ["motional induction", "surface charge", "Lorentz force", "conductor"]
    },
    {
        "id": "3.361",
        "title": "Space and Surface Charges in Rotating Aluminium Cylinder",
        "difficulty": 2,
        "question": "A long solid aluminium cylinder of radius $a = 5.0\\text{ cm}$ rotates about its axis in a uniform magnetic field with induction $B = 10\\text{ mT}$. The angular velocity of rotation is $\\omega = 45\\text{ rad/s}$, with $\\boldsymbol{\\omega} \\uparrow\\uparrow \\mathbf{B}$. Neglecting the magnetic field of appearing charges, find their space density $\\rho$ and surface density $\\sigma$.",
        "hints": [
            "Conduction electrons at radius $r$ rotate at velocity $v = \\omega r$, experiencing radial Lorentz force $F_m = e v B = e \\omega r B$.",
            "In steady state, the electric field balances the Lorentz force: $e E(r) = e \\omega r B \\implies E(r) = \\omega B r$.",
            "Use Gauss's law in cylindrical coordinates: $\\rho = \\varepsilon_0 \\frac{1}{r}\\frac{d}{dr}(r E) = 2 \\varepsilon_0 \\omega B$ (with negative sign for electrons). Surface charge follows from neutrality: $\\sigma = -\\frac{a \\rho}{2} = \\varepsilon_0 \\omega a B$."
        ],
        "answer": "$\\rho = -2 \\varepsilon_0 \\omega B = -0.080\\text{ nC/m}^3, \\quad \\sigma = \\varepsilon_0 \\omega a B = 2.0\\text{ pC/m}^2$",
        "solution": "**1. Equilibrium Radial Electric Field:**\nInside the rotating cylinder, electrons move with tangential velocity $v(r) = \\omega r$.\nThe magnetic Lorentz force pulls electrons radially inward:\n$$F_m = e v B = e \\omega r B$$\nIn steady-state rotation, an internal radial electric field $E(r)$ develops such that the net radial force on conduction electrons vanishes:\n$$e E(r) - e \\omega r B = 0 \\implies E(r) = \\omega B r$$\n(directed radially outward).\n\n**2. Volume Space Charge Density:**\nFrom Maxwell's first equation $\\nabla \\cdot \\mathbf{E} = \\frac{\\rho}{\\varepsilon_0}$ in cylindrical coordinates:\n$$\\rho = \\varepsilon_0 \\frac{1}{r} \\frac{d}{dr} [r E(r)] = \\varepsilon_0 \\frac{1}{r} \\frac{d}{dr} [\\omega B r^2] = 2 \\varepsilon_0 \\omega B$$\nBecause the field is produced by an excess of electrons displaced toward the axis, the bulk charge density is negative:\n$$\\rho = -2 \\varepsilon_0 \\omega B$$\n\n**3. Surface Charge Density:**\nSince the cylinder as a whole is electrically neutral, the total charge per unit length must be zero:\n$$\\int_0^a \\rho (2\\pi r \\, dr) + \\sigma (2\\pi a) = 0$$\n$$\\rho (\\pi a^2) + 2\\pi a \\sigma = 0 \\implies \\sigma = -\\frac{a \\rho}{2} = \\varepsilon_0 \\omega a B$$\n\n**4. Numerical Evaluation:**\nGiven $a = 0.050\\text{ m}$, $\\omega = 45\\text{ rad/s}$, $B = 0.010\\text{ T}$, $\\varepsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}$:\n$$\\rho = -2(8.854 \\times 10^{-12})(45)(0.010) = -7.97 \\times 10^{-11}\\text{ C/m}^3 \\approx -0.080\\text{ nC/m}^3$$\n$$\\sigma = (8.854 \\times 10^{-12})(45)(0.050)(0.010) \\approx 1.99 \\times 10^{-12}\\text{ C/m}^2 \\approx 2.0\\text{ pC/m}^2$$",
        "tags": ["rotating cylinder", "space charge", "surface charge", "Lorentz force"]
    },
    {
        "id": "3.362",
        "title": "Magnetic Field of Non-Relativistic Moving Charge",
        "difficulty": 2,
        "question": "A non-relativistic point charge $q$ moves with a constant velocity $\\mathbf{v}$. Using the field transformation formulas, find the magnetic induction $\\mathbf{B}$ produced by this charge at a point whose position relative to the charge is determined by the radius vector $\\mathbf{r}$.",
        "hints": [
            "In the rest frame $K_0$ of the charge, the field is purely electrostatic: $\\mathbf{E}_0 = \\frac{q \\mathbf{r}}{4\\pi \\varepsilon_0 r^3}$ and $\\mathbf{B}_0 = 0$.",
            "Use the non-relativistic field transformation formula for the laboratory frame $K$ where the charge moves with velocity $\\mathbf{v}$: $\\mathbf{B} = \\frac{1}{c^2}[\\mathbf{v} \\times \\mathbf{E}]$.",
            "Substitute $\\mathbf{E}_0$ and $c^2 = \\frac{1}{\\varepsilon_0 \\mu_0}$ to get $\\mathbf{B} = \\frac{\\mu_0 q [\\mathbf{v} \\times \\mathbf{r}]}{4\\pi r^3}$."
        ],
        "answer": "$\\mathbf{B} = \\frac{\\mu_0 q [\\mathbf{v} \\times \\mathbf{r}]}{4\\pi r^3}$",
        "solution": "**1. Fields in the Rest Frame $K_0$:**\nIn the rest frame of the charge, there is only a Coulomb electrostatic field:\n$$\\mathbf{E}_0 = \\frac{q \\mathbf{r}}{4\\pi \\varepsilon_0 r^3}, \\quad \\mathbf{B}_0 = 0$$\n\n**2. Transformation to Laboratory Frame $K$:**\nThe laboratory frame $K$ observes the charge moving with velocity $\\mathbf{v}$.\nUsing the field transformation for $v \\ll c$:\n$$\\mathbf{B} = \\mathbf{B}_0 + \\frac{1}{c^2} [\\mathbf{v} \\times \\mathbf{E}_0] = \\frac{1}{c^2} [\\mathbf{v} \\times \\mathbf{E}_0]$$\n\n**3. Evaluation:**\nSubstituting $\\mathbf{E}_0$ and using $c^2 = \\frac{1}{\\varepsilon_0 \\mu_0}$:\n$$\\mathbf{B} = \\frac{1}{c^2} \\left[ \\mathbf{v} \\times \\left( \\frac{q \\mathbf{r}}{4\\pi \\varepsilon_0 r^3} \\right) \\right] = \\frac{\\mu_0 \\varepsilon_0 q [\\mathbf{v} \\times \\mathbf{r}]}{4\\pi \\varepsilon_0 r^3} = \\frac{\\mu_0 q [\\mathbf{v} \\times \\mathbf{r}]}{4\\pi r^3}$$\nThis reproduces the Biot-Savart law for a moving point charge.",
        "tags": ["Biot-Savart law", "field transformation", "moving charge", "Maxwell equations"]
    },
    {
        "id": "3.363",
        "title": "Coexistence and Perpendicularity of Transformed E and B Fields",
        "difficulty": 2,
        "question": "Using the non-relativistic transformation formulas $\\mathbf{E}' = \\mathbf{E} + [\\mathbf{v} \\times \\mathbf{B}]$ and $\\mathbf{B}' = \\mathbf{B} - \\frac{1}{c^2}[\\mathbf{v} \\times \\mathbf{E}]$, demonstrate that if in the inertial frame $K$ there is only an electric or only a magnetic field, then in the frame $K'$ moving relative to $K$ both fields coexist simultaneously, and $\\mathbf{E}' \\perp \\mathbf{B}'$.",
        "hints": [
            "Consider Case 1: $\\mathbf{B} = 0$ in frame $K$. Find $\\mathbf{E}'$ and $\\mathbf{B}'$ and compute their scalar product $\\mathbf{E}' \\cdot \\mathbf{B}'$.",
            "Consider Case 2: $\\mathbf{E} = 0$ in frame $K$. Find $\\mathbf{E}'$ and $\\mathbf{B}'$ and compute $\\mathbf{E}' \\cdot \\mathbf{B}'$.",
            "Use the vector identity $\\mathbf{A} \\cdot [\\mathbf{v} \\times \\mathbf{A}] = 0$."
        ],
        "answer": "In both cases, $\\mathbf{E}' \\cdot \\mathbf{B}' = 0$, confirming that both fields coexist and are mutually perpendicular ($\\mathbf{E}' \\perp \\mathbf{B}'$)",
        "solution": "**Case 1: Pure electric field in frame $K$ ($\\mathbf{B} = 0$):**\nApplying the transformation formulas with $\\mathbf{B} = 0$:\n$$\\mathbf{E}' = \\mathbf{E}$$\n$$\\mathbf{B}' = -\\frac{1}{c^2} [\\mathbf{v} \\times \\mathbf{E}]$$\nSince $\\mathbf{v} \\ne 0$ and $\\mathbf{v} \\nparallel \\mathbf{E}$, a non-zero magnetic field $\\mathbf{B}'$ appears alongside $\\mathbf{E}'$.\nTaking the dot product:\n$$\\mathbf{E}' \\cdot \\mathbf{B}' = \\mathbf{E} \\cdot \\left( -\\frac{1}{c^2} [\\mathbf{v} \\times \\mathbf{E}] \\right) = -\\frac{1}{c^2} [\\mathbf{v} \\times \\mathbf{E}] \\cdot \\mathbf{E} = 0$$\nThus $\\mathbf{E}' \\perp \\mathbf{B}'$.\n\n**Case 2: Pure magnetic field in frame $K$ ($\\mathbf{E} = 0$):**\nApplying the transformation formulas with $\\mathbf{E} = 0$:\n$$\\mathbf{E}' = [\\mathbf{v} \\times \\mathbf{B}]$$\n$$\\mathbf{B}' = \\mathbf{B}$$\nTaking the dot product:\n$$\\mathbf{E}' \\cdot \\mathbf{B}' = [\\mathbf{v} \\times \\mathbf{B}] \\cdot \\mathbf{B} = 0$$\nThus $\\mathbf{E}' \\perp \\mathbf{B}'$ in this case as well.",
        "tags": ["field transformations", "Lorentz invariants", "orthogonality", "special relativity"]
    },
    {
        "id": "3.364",
        "title": "Electric Field Transformed from Vortex Magnetic Field",
        "difficulty": 2,
        "question": "In an inertial reference frame $K$ there is only a magnetic field with induction $\\mathbf{B} = \\frac{b(-y \\hat{\\mathbf{i}} + x \\hat{\\mathbf{j}})}{x^2 + y^2}$, where $b$ is a constant. Find the electric field strength $\\mathbf{E}'$ in the frame $K'$ moving relative to frame $K$ with a constant non-relativistic velocity $\\mathbf{v} = v \\hat{\\mathbf{k}}$. What is the shape of field $\\mathbf{E}'$?",
        "hints": [
            "Use the field transformation $\\mathbf{E}' = [\\mathbf{v} \\times \\mathbf{B}]$ since $\\mathbf{E} = 0$ in frame $K$.",
            "Compute the vector cross product $v \\hat{\\mathbf{k}} \\times (-y \\hat{\\mathbf{i}} + x \\hat{\\mathbf{j}})$.",
            "Express the result in terms of planar radius vector $\\mathbf{r}_\\perp = x \\hat{\\mathbf{i}} + y \\hat{\\mathbf{j}}$ and distance $r = \\sqrt{x^2 + y^2}$."
        ],
        "answer": "$\\mathbf{E}' = -\\frac{v b \\mathbf{r}_\\perp}{r^2}$; the field has radial cylindrical symmetry with magnitude $E' = \\frac{v b}{r}$",
        "solution": "**1. Field Transformation:**\nIn frame $K$, $\\mathbf{E} = 0$. In frame $K'$ moving with velocity $\\mathbf{v} = v \\hat{\\mathbf{k}}$, the transformed electric field is:\n$$\\mathbf{E}' = [\\mathbf{v} \\times \\mathbf{B}]$$\n\n**2. Cross Product Calculation:**\nGiven $\\mathbf{B} = \\frac{b}{x^2 + y^2} (-y \\hat{\\mathbf{i}} + x \\hat{\\mathbf{j}})$:\n$$\\mathbf{v} \\times \\mathbf{B} = (v \\hat{\\mathbf{k}}) \\times \\left[ \\frac{b}{x^2 + y^2} (-y \\hat{\\mathbf{i}} + x \\hat{\\mathbf{j}}) \\right]$$\nUsing the standard unit vector cross products $\\hat{\\mathbf{k}} \\times \\hat{\\mathbf{i}} = \\hat{\\mathbf{j}}$ and $\\hat{\\mathbf{k}} \\times \\hat{\\mathbf{j}} = -\\hat{\\mathbf{i}}$:\n$$\\mathbf{v} \\times \\mathbf{B} = \\frac{v b}{x^2 + y^2} \\left[ -y \\hat{\\mathbf{j}} - x \\hat{\\mathbf{i}} \\right] = -\\frac{v b (x \\hat{\\mathbf{i}} + y \\hat{\\mathbf{j}})}{x^2 + y^2}$$\n\n**3. Field Configuration:**\nLetting $\\mathbf{r}_\\perp = x \\hat{\\mathbf{i}} + y \\hat{\\mathbf{j}}$ with $r = |\\mathbf{r}_\\perp| = \\sqrt{x^2 + y^2}$:\n$$\\mathbf{E}' = -\\frac{v b}{r^2} \\mathbf{r}_\\perp = -\\frac{v b}{r} \\hat{\\mathbf{r}}_\\perp$$\nThe magnitude is $E' = \\frac{v b}{r}$. This corresponds to a radially symmetric cylindrical field directed toward the $z'$-axis, identical in form to the electrostatic field of a uniformly charged straight wire.",
        "tags": ["field transformation", "radial field", "cylindrical symmetry", "cross product"]
    },
    {
        "id": "3.365",
        "title": "Magnetic Field Transformed from Radial Electric Field",
        "difficulty": 2,
        "question": "In an inertial reference frame $K$ there is only an electric field of strength $\\mathbf{E} = \\frac{a(x \\hat{\\mathbf{i}} + y \\hat{\\mathbf{j}})}{x^2 + y^2}$, where $a$ is a constant. Find the magnetic induction $\\mathbf{B}'$ in frame $K'$ moving relative to frame $K$ with a constant non-relativistic velocity $\\mathbf{v} = v \\hat{\\mathbf{k}}$. What is the shape of field $\\mathbf{B}'$?",
        "hints": [
            "Use the field transformation $\\mathbf{B}' = -\\frac{1}{c^2}[\\mathbf{v} \\times \\mathbf{E}]$ since $\\mathbf{B} = 0$ in frame $K$.",
            "Evaluate $(v \\hat{\\mathbf{k}}) \\times (x \\hat{\\mathbf{i}} + y \\hat{\\mathbf{j}})$.",
            "Express the result in cylindrical coordinates and analyze the field lines."
        ],
        "answer": "$\\mathbf{B}' = \\frac{a v (y \\hat{\\mathbf{i}} - x \\hat{\\mathbf{j}})}{c^2 r^2}$; the field lines are concentric circles around the $z'$-axis with magnitude $B' = \\frac{a v}{c^2 r}$",
        "solution": "**1. Field Transformation:**\nWith $\\mathbf{B} = 0$ in frame $K$, the transformed magnetic field in frame $K'$ is:\n$$\\mathbf{B}' = -\\frac{1}{c^2} [\\mathbf{v} \\times \\mathbf{E}]$$\n\n**2. Cross Product Calculation:**\nWith $\\mathbf{v} = v \\hat{\\mathbf{k}}$ and $\\mathbf{E} = \\frac{a}{x^2 + y^2} (x \\hat{\\mathbf{i}} + y \\hat{\\mathbf{j}})$:\n$$\\mathbf{v} \\times \\mathbf{E} = (v \\hat{\\mathbf{k}}) \\times \\left[ \\frac{a}{x^2 + y^2} (x \\hat{\\mathbf{i}} + y \\hat{\\mathbf{j}}) \\right] = \\frac{a v}{x^2 + y^2} (x \\hat{\\mathbf{j}} - y \\hat{\\mathbf{i}})$$\nTherefore:\n$$\\mathbf{B}' = -\\frac{a v}{c^2 (x^2 + y^2)} (x \\hat{\\mathbf{j}} - y \\hat{\\mathbf{i}}) = \\frac{a v (y \\hat{\\mathbf{i}} - x \\hat{\\mathbf{j}})}{c^2 r^2}$$\n\n**3. Field Line Geometry:**\nIn cylindrical polar coordinates, the unit azimuthal vector is $\\hat{\\boldsymbol{\\theta}} = -\\sin\\theta \\hat{\\mathbf{i}} + \\cos\\theta \\hat{\\mathbf{j}} = \\frac{-y \\hat{\\mathbf{i}} + x \\hat{\\mathbf{j}}}{r}$.\nThus:\n$$\\mathbf{B}' = -\\frac{a v}{c^2 r} \\hat{\\boldsymbol{\\theta}}$$\nThe magnitude is $B' = \\frac{a v}{c^2 r}$. The field lines are concentric circles centered on the $z'$-axis, identical to the magnetic field of a straight line current.",
        "tags": ["field transformation", "circular magnetic field", "vortex field", "special relativity"]
    },
    {
        "id": "3.366",
        "title": "Low-Velocity Limit of Relativistic Field Transformations",
        "difficulty": 2,
        "question": "Demonstrate that the non-relativistic field transformation formulas follow from the exact relativistic Lorentz field transformation formulas in the limit $v \\ll c$.",
        "hints": [
            "Recall the exact relativistic transformations: $E'_\\parallel = E_\\parallel$, $\\mathbf{E}'_\\perp = \\gamma (\\mathbf{E}_\\perp + [\\mathbf{v} \\times \\mathbf{B}])$, with $\\gamma = \\frac{1}{\\sqrt{1 - v^2/c^2}}$.",
            "For $v \\ll c$, expand the Lorentz factor to first order: $\\gamma \\approx 1$.",
            "Combine parallel and perpendicular components to reconstruct full vectors $\\mathbf{E}'$ and $\\mathbf{B}'$."
        ],
        "answer": "At $v \\ll c$, $\\gamma \\to 1$, directly yielding $\\mathbf{E}' = \\mathbf{E} + [\\mathbf{v} \\times \\mathbf{B}]$ and $\\mathbf{B}' = \\mathbf{B} - \\frac{1}{c^2}[\\mathbf{v} \\times \\mathbf{E}]$",
        "solution": "**1. Exact Relativistic Transformations:**\nThe Lorentz transformations for electromagnetic field components parallel and perpendicular to relative velocity $\\mathbf{v}$ are:\n$$E'_\\parallel = E_\\parallel, \\quad \\mathbf{E}'_\\perp = \\gamma (\\mathbf{E}_\\perp + [\\mathbf{v} \\times \\mathbf{B}])$$\n$$B'_\\parallel = B_\\parallel, \\quad \\mathbf{B}'_\\perp = \\gamma \\left( \\mathbf{B}_\\perp - \\frac{1}{c^2} [\\mathbf{v} \\times \\mathbf{E}] \\right)$$\nwhere $\\gamma = \\frac{1}{\\sqrt{1 - v^2/c^2}}$.\n\n**2. Low-Velocity Approximation ($v \\ll c$):**\nWhen $v / c \\to 0$, the Lorentz factor simplifies to:\n$$\\gamma = \\left( 1 - \\frac{v^2}{c^2} \\right)^{-1/2} \\approx 1$$\nSubstituting $\\gamma \\approx 1$ into the perpendicular components:\n$$\\mathbf{E}'_\\perp \\approx \\mathbf{E}_\\perp + [\\mathbf{v} \\times \\mathbf{B}]$$\n$$\\mathbf{B}'_\\perp \\approx \\mathbf{B}_\\perp - \\frac{1}{c^2} [\\mathbf{v} \\times \\mathbf{E}]$$\n\n**3. Reconstituting Total Vector Fields:**\nSince $[\\mathbf{v} \\times \\mathbf{B}]$ and $[\\mathbf{v} \\times \\mathbf{E}]$ are strictly perpendicular to $\\mathbf{v}$, we can add the parallel and perpendicular parts:\n$$\\mathbf{E}' = E'_\\parallel \\hat{\\mathbf{v}} + \\mathbf{E}'_\\perp = E_\\parallel \\hat{\\mathbf{v}} + \\mathbf{E}_\\perp + [\\mathbf{v} \\times \\mathbf{B}] = \\mathbf{E} + [\\mathbf{v} \\times \\mathbf{B}]$$\n$$\\mathbf{B}' = B'_\\parallel \\hat{\\mathbf{v}} + \\mathbf{B}'_\\perp = B_\\parallel \\hat{\\mathbf{v}} + \\mathbf{B}_\\perp - \\frac{1}{c^2} [\\mathbf{v} \\times \\mathbf{E}] = \\mathbf{B} - \\frac{1}{c^2} [\\mathbf{v} \\times \\mathbf{E}]$$\nThis completes the demonstration.",
        "tags": ["Lorentz transformation", "field transformation", "non-relativistic limit", "special relativity"]
    },
    {
        "id": "3.367",
        "title": "Relativistic Transformation of Pure Electric Field",
        "difficulty": 3,
        "question": "In an inertial reference frame $K$ there is only a uniform electric field $E = 8.0\\text{ kV/m}$. Find the modulus and direction:\n(a) of the vector $\\mathbf{E}'$;\n(b) of the vector $\\mathbf{B}'$\nin an inertial reference frame $K'$ moving with constant velocity $v$ relative to frame $K$ at an angle $\\alpha = 45^\\circ$ to the vector $\\mathbf{E}$. The velocity of frame $K'$ is $\\beta = 0.60$ ($v = \\beta c$).",
        "hints": [
            "Decompose $\\mathbf{E}$ into components parallel and perpendicular to $\\mathbf{v}$: $E_\\parallel = E \\cos\\alpha$, $E_\\perp = E \\sin\\alpha$.",
            "In frame $K'$: $E'_\\parallel = E_\\parallel$ and $E'_\\perp = \\gamma E_\\perp$, giving $E' = E \\sqrt{\\frac{1 - \\beta^2 \\cos^2\\alpha}{1 - \\beta^2}}$.",
            "The magnetic induction is $B' = \\frac{\\gamma v E \\sin\\alpha}{c^2} = \\frac{\\beta E \\sin\\alpha}{c \\sqrt{1 - \\beta^2}}$."
        ],
        "answer": "(a) $E' = 9.1\\text{ kV/m}$, $\\alpha' \\approx 51^\\circ$; (b) $B' = 14\\,\\mu\\text{T}$",
        "solution": "**(a) Transformed Electric Field $\\mathbf{E}'$:**\nDecompose $\\mathbf{E}$ relative to $\\mathbf{v}$:\n$$E_\\parallel = E \\cos\\alpha, \\quad E_\\perp = E \\sin\\alpha$$\nIn frame $K'$:\n$$E'_\\parallel = E_\\parallel = E \\cos\\alpha$$\n$$E'_\\perp = \\gamma E_\\perp = \\frac{E \\sin\\alpha}{\\sqrt{1 - \\beta^2}}$$\nThe magnitude of $\\mathbf{E}'$ is:\n$$E' = \\sqrt{(E'_\\parallel)^2 + (E'_\\perp)^2} = E \\sqrt{\\cos^2\\alpha + \\frac{\\sin^2\\alpha}{1 - \\beta^2}} = E \\sqrt{\\frac{1 - \\beta^2 \\cos^2\\alpha}{1 - \\beta^2}}$$\nWith $\\beta = 0.60$, $\\sqrt{1 - \\beta^2} = 0.80$, $\\alpha = 45^\\circ$ (so $\\cos^2 45^\\circ = 0.5$):\n$$E' = 8.0 \\sqrt{\\frac{1 - 0.36(0.5)}{0.64}} = 8.0 \\sqrt{\\frac{0.82}{0.64}} = \\frac{8.0}{0.80} \\sqrt{0.82} = 10 \\times 0.9055 \\approx 9.1\\text{ kV/m}$$\nThe angle $\\alpha'$ between $\\mathbf{E}'$ and $\\mathbf{v}$ satisfies:\n$$\\tan\\alpha' = \\frac{E'_\\perp}{E'_\\parallel} = \\frac{\\gamma E \\sin\\alpha}{E \\cos\\alpha} = \\gamma \\tan\\alpha = \\frac{\\tan 45^\\circ}{0.80} = 1.25 \\implies \\alpha' \\approx 51^\\circ$$\n\n**(b) Transformed Magnetic Field $\\mathbf{B}'$:**\nSince $\\mathbf{B} = 0$ in frame $K$, the magnetic induction in $K'$ is purely transverse:\n$$\\mathbf{B}' = -\\frac{\\gamma}{c^2} [\\mathbf{v} \\times \\mathbf{E}]$$\n$$B' = \\frac{\\gamma v E \\sin\\alpha}{c^2} = \\frac{\\beta E \\sin\\alpha}{c \\sqrt{1 - \\beta^2}}$$\nNumerical evaluation:\n$$B' = \\frac{(0.60)(8000\\text{ V/m}) \\sin 45^\\circ}{(3.0 \\times 10^8\\text{ m/s})(0.80)} = \\frac{3394.1}{2.4 \\times 10^8} \\approx 1.41 \\times 10^{-5}\\text{ T} = 14\\,\\mu\\text{T}$$",
        "tags": ["relativistic transformation", "electric field", "Lorentz boost", "magnetic induction"]
    },
    {
        "id": "3.368",
        "title": "Relativistic Transformation of Pure Magnetic Field",
        "difficulty": 3,
        "question": "Solve the problem differing from the foregoing one by a uniform magnetic field with induction $B = 0.80\\text{ T}$ replacing the electric field ($E = 0$ in frame $K$). Find $E'$ and $B'$ in frame $K'$ moving at angle $\\alpha = 45^\\circ$ to $\\mathbf{B}$ with $\\beta = 0.60$.",
        "hints": [
            "Decompose $\\mathbf{B}$ into $B_\\parallel = B \\cos\\alpha$ and $B_\\perp = B \\sin\\alpha$.",
            "The transformed electric field is purely transverse: $E' = \\gamma v B \\sin\\alpha = \\frac{\\beta c B \\sin\\alpha}{\\sqrt{1 - \\beta^2}}$.",
            "The transformed magnetic field has components $B'_\\parallel = B \\cos\\alpha$ and $B'_\\perp = \\gamma B \\sin\\alpha$."
        ],
        "answer": "(a) $E' = 0.13\\text{ GV/m}$; (b) $B' = 0.91\\text{ T}$, $\\alpha' \\approx 51^\\circ$",
        "solution": "**(a) Transformed Electric Field $\\mathbf{E}'$:**\nIn frame $K$, $\\mathbf{E} = 0$ and $\\mathbf{B}$ is at angle $\\alpha = 45^\\circ$ to $\\mathbf{v}$.\nThe transformed electric field in $K'$ is:\n$$\\mathbf{E}' = \\gamma [\\mathbf{v} \\times \\mathbf{B}]$$\nIts magnitude is:\n$$E' = \\gamma v B \\sin\\alpha = \\frac{\\beta c B \\sin\\alpha}{\\sqrt{1 - \\beta^2}}$$\nNumerical evaluation with $\\beta = 0.60$, $\\sqrt{1 - \\beta^2} = 0.80$, $B = 0.80\\text{ T}$:\n$$E' = \\frac{(0.60)(3.0 \\times 10^8\\text{ m/s})(0.80\\text{ T}) \\sin 45^\\circ}{0.80} = 1.8 \\times 10^8 \\times 0.7071 \\approx 1.27 \\times 10^8\\text{ V/m} \\approx 0.13\\text{ GV/m}$$\n\n**(b) Transformed Magnetic Field $\\mathbf{B}'$:**\nThe magnetic field components in $K'$ are:\n$$B'_\\parallel = B_\\parallel = B \\cos\\alpha$$\n$$B'_\\perp = \\gamma B_\\perp = \\frac{B \\sin\\alpha}{\\sqrt{1 - \\beta^2}}$$\n$$B' = B \\sqrt{\\frac{1 - \\beta^2 \\cos^2\\alpha}{1 - \\beta^2}}$$\nNumerical evaluation:\n$$B' = 0.80 \\sqrt{\\frac{1 - 0.36(0.5)}{0.64}} = 0.80 \\frac{\\sqrt{0.82}}{0.80} = \\sqrt{0.82} \\approx 0.906\\text{ T} \\approx 0.91\\text{ T}$$\nThe angle $\\alpha'$ with $\\mathbf{v}$ satisfies $\\tan\\alpha' = \\gamma \\tan\\alpha = 1.25 \\implies \\alpha' \\approx 51^\\circ$.",
        "tags": ["relativistic transformation", "magnetic field", "Lorentz boost", "electric field generation"]
    },
    {
        "id": "3.369",
        "title": "Relativistic Invariants of the Electromagnetic Field",
        "difficulty": 3,
        "question": "The electromagnetic field has two relativistic invariant quantities. Using the field transformation formulas, demonstrate that these quantities are:\n(a) $I_1 = \\mathbf{E} \\cdot \\mathbf{B}$;\n(b) $I_2 = E^2 - c^2 B^2$.",
        "hints": [
            "Align the $x$-axis along the boost velocity $\\mathbf{v}$. Then components transform as: $E'_x = E_x$, $E'_y = \\gamma(E_y - v B_z)$, $E'_z = \\gamma(E_z + v B_y)$, and similarly for $\\mathbf{B}'$.",
            "Substitute into $\\mathbf{E}' \\cdot \\mathbf{B}' = E'_x B'_x + E'_y B'_y + E'_z B'_z$ and use $\\gamma^2(1 - v^2/c^2) = 1$.",
            "Similarly compute $(E')^2 - c^2 (B')^2$ and verify that all cross-terms cancel."
        ],
        "answer": "(a) $\\mathbf{E}' \\cdot \\mathbf{B}' = \\mathbf{E} \\cdot \\mathbf{B}$; (b) $(E')^2 - c^2 (B')^2 = E^2 - c^2 B^2$",
        "solution": "**1. Lorentz Field Transformations:**\nFor a boost along the $x$-axis with speed $v = \\beta c$ and $\\gamma = (1 - \\beta^2)^{-1/2}$:\n$$E'_x = E_x, \\quad E'_y = \\gamma(E_y - v B_z), \\quad E'_z = \\gamma(E_z + v B_y)$$\n$$B'_x = B_x, \\quad B'_y = \\gamma\\left( B_y + \\frac{v}{c^2} E_z \\right), \\quad B'_z = \\gamma\\left( B_z - \\frac{v}{c^2} E_y \\right)$$\n\n**(a) First Invariant $\\mathbf{E} \\cdot \\mathbf{B}$:**\n$$\\mathbf{E}' \\cdot \\mathbf{B}' = E'_x B'_x + E'_y B'_y + E'_z B'_z$$\n$$E'_y B'_y + E'_z B'_z = \\gamma^2 \\left[ (E_y - v B_z)\\left( B_y + \\frac{v}{c^2} E_z \\right) + (E_z + v B_y)\\left( B_z - \\frac{v}{c^2} E_y \\right) \\right]$$\nExpanding terms:\n$$= \\gamma^2 \\left[ E_y B_y + \\frac{v}{c^2} E_y E_z - v B_y B_z - \\frac{v^2}{c^2} E_z B_z + E_z B_z - \\frac{v}{c^2} E_y E_z + v B_y B_z - \\frac{v^2}{c^2} E_y B_y \\right]$$\nThe cross-terms $\\pm \\frac{v}{c^2} E_y E_z$ and $\\mp v B_y B_z$ cancel identically:\n$$= \\gamma^2 \\left( 1 - \\frac{v^2}{c^2} \\right) (E_y B_y + E_z B_z) = E_y B_y + E_z B_z$$\nAdding $E'_x B'_x = E_x B_x$:\n$$\\mathbf{E}' \\cdot \\mathbf{B}' = \\mathbf{E} \\cdot \\mathbf{B}$$\n\n**(b) Second Invariant $E^2 - c^2 B^2$:**\nComputing $(E')^2 - c^2 (B')^2$:\n$$(E'_y)^2 + (E'_z)^2 - c^2 [(B'_y)^2 + (B'_z)^2]$$\n$$= \\gamma^2 \\left[ (E_y - v B_z)^2 + (E_z + v B_y)^2 - c^2 \\left( B_y + \\frac{v}{c^2} E_z \\right)^2 - c^2 \\left( B_z - \\frac{v}{c^2} E_y \\right)^2 \\right]$$\nExpanding and canceling the $2 v (\\dots)$ cross-terms:\n$$= \\gamma^2 \\left( 1 - \\frac{v^2}{c^2} \\right) \\left[ E_y^2 + E_z^2 - c^2(B_y^2 + B_z^2) \\right] = E_y^2 + E_z^2 - c^2(B_y^2 + B_z^2)$$\nAdding $E_x^2 - c^2 B_x^2$ confirms:\n$$(E')^2 - c^2 (B')^2 = E^2 - c^2 B^2$$",
        "tags": ["relativistic invariants", "Lorentz invariants", "electromagnetic field tensor", "special relativity"]
    },
    {
        "id": "3.370",
        "title": "Single-Field Reference Frame for Perpendicular E and B",
        "difficulty": 3,
        "question": "In an inertial reference frame $K$ there are two uniform mutually perpendicular fields: an electric field $E = 40\\text{ kV/m}$ and a magnetic field $B = 0.20\\text{ mT}$. Find the electric field strength $E'$ (or magnetic induction $B'$) in the reference frame $K'$ where only one field, electric or magnetic, is observed.",
        "hints": [
            "Use the field invariants from problem 3.369: $I_1 = \\mathbf{E} \\cdot \\mathbf{B} = 0$ (since $\\mathbf{E} \\perp \\mathbf{B}$), and $I_2 = E^2 - c^2 B^2$.",
            "Calculate $c B = (3.0 \\times 10^8)(0.20 \\times 10^{-3}) = 60\\text{ kV/m}$. Since $c B > E$, $I_2 < 0$, so a frame $K'$ exists where $E' = 0$ and only $B'$ is observed.",
            "Use the invariant: $-(c B')^2 = E^2 - c^2 B^2 \\implies B' = \\sqrt{B^2 - (E/c)^2} = B \\sqrt{1 - (E/cB)^2}$."
        ],
        "answer": "$B' = B \\sqrt{1 - \\left(\\frac{E}{cB}\\right)^2} \\approx 0.15\\text{ mT}$ (pure magnetic field)",
        "solution": "**1. Determining Which Field Can Be Eliminated:**\nThe two fields are mutually perpendicular, so the first invariant vanishes:\n$$I_1 = \\mathbf{E} \\cdot \\mathbf{B} = 0$$\nNow evaluate the second invariant:\n$$I_2 = E^2 - c^2 B^2$$\nGiven $E = 40\\text{ kV/m} = 4.0 \\times 10^4\\text{ V/m}$ and $B = 0.20\\text{ mT} = 2.0 \\times 10^{-4}\\text{ T}$:\n$$c B = (3.0 \\times 10^8\\text{ m/s})(2.0 \\times 10^{-4}\\text{ T}) = 6.0 \\times 10^4\\text{ V/m} = 60\\text{ kV/m}$$\nSince $c B > E$, the second invariant is negative:\n$$I_2 = (40)^2 - (60)^2 = 1600 - 3600 = -2000\\text{ (kV/m)}^2 < 0$$\nBecause $I_2 < 0$, there exists a frame $K'$ where the electric field is completely transformed away ($E' = 0$), leaving only a pure magnetic field $B'$.\n\n**2. Calculation of Transformed Magnetic Field $B'$:**\nUsing the invariance of $I_2$ between frames $K$ and $K'$:\n$$(E')^2 - c^2 (B')^2 = E^2 - c^2 B^2$$\nSetting $E' = 0$:\n$$-c^2 (B')^2 = E^2 - c^2 B^2 \\implies (B')^2 = B^2 - \\frac{E^2}{c^2} = B^2 \\left[ 1 - \\left( \\frac{E}{c B} \\right)^2 \\right]$$\n$$B' = B \\sqrt{1 - \\left( \\frac{E}{c B} \\right)^2}$$\n\n**3. Numerical Evaluation:**\n$$B' = (0.20\\text{ mT}) \\sqrt{1 - \\left( \\frac{40}{60} \\right)^2} = (0.20\\text{ mT}) \\sqrt{1 - \\frac{4}{9}} = 0.20 \\sqrt{\\frac{5}{9}} = \\frac{0.20 \\sqrt{5}}{3} \\approx 0.149\\text{ mT} \\approx 0.15\\text{ mT}$$",
        "tags": ["field invariants", "crossed fields", "frame transformation", "special relativity"]
    },
    {
        "id": "3.371",
        "title": "Electric Field of Uniformly Moving Relativistic Charge",
        "difficulty": 3,
        "question": "A point charge $q$ moves uniformly and rectilinearly with a relativistic velocity equal to a $\\beta$ fraction of the velocity of light ($v = \\beta c$). Find the electric field strength $\\mathbf{E}$ produced by the charge at a point whose radius vector relative to the charge is equal to $\\mathbf{r}$ and forms an angle $\\theta$ with its velocity vector.",
        "hints": [
            "In the rest frame $K'$ of the charge, the field is Coulombian: $\\mathbf{E}' = \\frac{q \\mathbf{r}'}{4\\pi \\varepsilon_0 (r')^3}$.",
            "Transform coordinates and fields back to frame $K$ using $x' = \\gamma x$, $y' = y$, and $E_x = E'_x$, $E_y = \\gamma E'_y$.",
            "Show that $(r')^2 = \\gamma^2 r^2 (1 - \\beta^2 \\sin^2\\theta)$, and that $\\mathbf{E}$ remains strictly collinear with $\\mathbf{r}$."
        ],
        "answer": "$\\mathbf{E} = \\frac{q \\mathbf{r} (1 - \\beta^2)}{4\\pi \\varepsilon_0 r^3 (1 - \\beta^2 \\sin^2\\theta)^{3/2}}$",
        "solution": "**1. Field in the Rest Frame $K'$:**\nLet the charge move along the $x$-axis with speed $v$. In its rest frame $K'$, the charge is located at the origin.\nThe electrostatic field is:\n$$\\mathbf{E}' = \\frac{q \\mathbf{r}'}{4\\pi \\varepsilon_0 (r')^3}$$\nIts components are $E'_x = \\frac{q x'}{4\\pi \\varepsilon_0 (r')^3}$ and $E'_y = \\frac{q y'}{4\\pi \\varepsilon_0 (r')^3}$.\n\n**2. Coordinate Transformation:**\nAt the instant $t = 0$ when the charge passes through the origin of the laboratory frame $K$, the coordinates of the field point transform as:\n$$x' = \\gamma x = \\frac{x}{\\sqrt{1 - \\beta^2}}, \\quad y' = y$$\nThe distance $r'$ in frame $K'$ is:\n$$(r')^2 = (x')^2 + (y')^2 = \\frac{x^2}{1 - \\beta^2} + y^2 = \\frac{x^2 + y^2 - \\beta^2 y^2}{1 - \\beta^2}$$\nWith $x = r \\cos\\theta$ and $y = r \\sin\\theta$, this simplifies to:\n$$(r')^2 = \\frac{r^2 (1 - \\beta^2 \\sin^2\\theta)}{1 - \\beta^2} = \\gamma^2 r^2 (1 - \\beta^2 \\sin^2\\theta)$$\n$$(r')^3 = \\gamma^3 r^3 (1 - \\beta^2 \\sin^2\\theta)^{3/2}$$\n\n**3. Field Transformations to Frame $K$:**\nFrom the relativistic field transformations with $\\mathbf{B}' = 0$:\n$$E_x = E'_x = \\frac{q x'}{4\\pi \\varepsilon_0 (r')^3} = \\frac{q (\\gamma x)}{4\\pi \\varepsilon_0 \\gamma^3 r^3 (1 - \\beta^2 \\sin^2\\theta)^{3/2}} = \\frac{q x (1 - \\beta^2)}{4\\pi \\varepsilon_0 r^3 (1 - \\beta^2 \\sin^2\\theta)^{3/2}}$$\n$$E_y = \\gamma E'_y = \\gamma \\frac{q y'}{4\\pi \\varepsilon_0 (r')^3} = \\gamma \\frac{q y}{4\\pi \\varepsilon_0 \\gamma^3 r^3 (1 - \\beta^2 \\sin^2\\theta)^{3/2}} = \\frac{q y (1 - \\beta^2)}{4\\pi \\varepsilon_0 r^3 (1 - \\beta^2 \\sin^2\\theta)^{3/2}}$$\n\n**4. Vector Field Result:**\nCombining $E_x \\hat{\\mathbf{i}} + E_y \\hat{\\mathbf{j}}$:\n$$\\mathbf{E} = \\frac{q \\mathbf{r} (1 - \\beta^2)}{4\\pi \\varepsilon_0 r^3 (1 - \\beta^2 \\sin^2\\theta)^{3/2}}$$\nNotice that the vector $\\mathbf{E}$ is directed along the radius vector $\\mathbf{r}$ pointing directly away from the instantaneous position of the charge!",
        "tags": ["relativistic charge", "relativistic electric field", "Heaviside field", "Lorentz contraction"]
    }
]
