"""
part3_ch3_5c.py
Curated problems 3.266 to 3.287 (22 problems) of Irodov Chapter 3.5:
Constant Magnetic Field. Magnetics (Part C).
"""

CH3_5C_CURATED = [
    {
        "id": "3.266",
        "title": "Radial Potential Difference Inside Current-Carrying Wire",
        "difficulty": 2,
        "question": "A straight round copper wire of radius $R = 5.0\\text{ mm}$ carries current $I = 50\\text{ A}$. Find the potential difference between the axis of the conductor and its surface (electron concentration $n = 0.9 \\times 10^{23}\\text{ cm}^{-3}$).",
        "hints": [
            "Conduction electrons moving at drift velocity $u = \\frac{I}{\\pi R^2 n e}$ experience inward magnetic Lorentz force $F_m = e u B(r) = e u \\left( \\frac{\\mu_0 I r}{2\\pi R^2} \\right)$.",
            "In equilibrium, this magnetic pinch force is balanced by an outward radial Hall electric field: $e E(r) = e u B(r)$.",
            "Integrate $U = \\int_0^R E(r) \\, dr = \\frac{\\mu_0 I^2}{4\\pi^2 R^2 n e}$."
        ],
        "answer": "$U = \\frac{\\mu_0 I^2}{4\\pi^2 R^2 n e} = 2.0\\text{ pV}$",
        "solution": "**1. Drift Velocity and Magnetic Field:**\nThe conduction electrons drift with mean velocity:\n$$u = \\frac{I}{\\pi R^2 n e}$$\nInside the conductor, the magnetic field is:\n$$B(r) = \\frac{\\mu_0 I r}{2\\pi R^2}$$\n\n**2. Equilibrium of Forces:**\nThe magnetic Lorentz force pulls electrons toward the wire axis:\n$$F_m(r) = e u B(r)$$\nIn steady state, charge redistributes radially until an outward electrostatic field $E(r)$ develops such that the net radial force vanishes:\n$$e E(r) = e u B(r) \\implies E(r) = u B(r) = \\left( \\frac{I}{\\pi R^2 n e} \\right) \\left( \\frac{\\mu_0 I r}{2\\pi R^2} \\right) = \\frac{\\mu_0 I^2 r}{2\\pi^2 R^4 n e}$$\n\n**3. Potential Difference:**\n$$U = \\varphi(0) - \\varphi(R) = \\int_0^R E(r) \\, dr = \\frac{\\mu_0 I^2}{2\\pi^2 R^4 n e} \\left[ \\frac{R^2}{2} \\right] = \\frac{\\mu_0 I^2}{4\\pi^2 R^2 n e}$$\n\n**4. Numerical Evaluation:**\nGiven $I = 50\\text{ A}$, $R = 0.0050\\text{ m}$, $n = 0.9 \\times 10^{29}\\text{ m}^{-3}$, $e = 1.602 \\times 10^{-19}\\text{ C}$, $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ H/m}$:\n$$U = \\frac{(4\\pi \\times 10^{-7})(2500)}{4\\pi^2 (2.5 \\times 10^{-5})(0.9 \\times 10^{29})(1.602 \\times 10^{-19})} \\approx 2.0 \\times 10^{-12}\\text{ V} = 2.0\\text{ pV}$$",
        "tags": ["magnetic pinch", "Hall effect in wire", "radial potential difference", "drift velocity"]
    },
    {
        "id": "3.267",
        "title": "Carrier Concentration from Hall Effect in Sodium",
        "difficulty": 2,
        "question": "In Hall effect measurements on a sodium conductor, the transverse electric field was $E = 5.0\\,\\mu\\text{V/cm}$ with current density $j = 200\\text{ A/cm}^2$ and magnetic induction $B = 1.00\\text{ T}$. Find the concentration of conduction electrons and its ratio to the total number of sodium atoms.",
        "hints": [
            "The Hall field balances the Lorentz force: $e E = e u B = e \\left(\\frac{j}{n e}\\right) B \\implies E = \\frac{j B}{n e}$.",
            "Solve for $n = \\frac{j B}{e E}$.",
            "Calculate atomic density $n_{\\text{atom}} = \\frac{\\rho_{\\text{Na}} N_A}{M_{\\text{Na}}}$ and compare."
        ],
        "answer": "$n = \\frac{j B}{e E} = 2.5 \\times 10^{28}\\text{ m}^{-3}$; ratio is approximately $1 : 1$",
        "solution": "**1. Hall Electric Field:**\nIn steady state, the transverse electric field balances the Lorentz force:\n$$e E = e u B = \\frac{j B}{n} \\implies n = \\frac{j B}{e E}$$\n\n**2. Numerical Evaluation of $n$:**\nGiven $j = 200\\text{ A/cm}^2 = 2.0 \\times 10^6\\text{ A/m}^2$, $B = 1.00\\text{ T}$, $E = 5.0\\,\\mu\\text{V/cm} = 5.0 \\times 10^{-4}\\text{ V/m}$:\n$$n = \\frac{(2.0 \\times 10^6)(1.00)}{(1.602 \\times 10^{-19})(5.0 \\times 10^{-4})} = \\frac{2.0 \\times 10^6}{8.01 \\times 10^{-23}} \\approx 2.5 \\times 10^{28}\\text{ m}^{-3}$$\n\n**3. Atomic Concentration:**\nFor sodium, mass density $\\rho \\approx 970\\text{ kg/m}^3$ and molar mass $M = 23.0\\text{ g/mol}$:\n$$n_{\\text{atom}} = \\frac{\\rho N_A}{M} = \\frac{(970)(6.022 \\times 10^{26})}{23} \\approx 2.54 \\times 10^{28}\\text{ m}^{-3}$$\nThus the ratio $n / n_{\\text{atom}} \\approx 1.0$, meaning each sodium atom contributes approximately one conduction electron.",
        "tags": ["Hall effect", "carrier concentration", "monovalent metal", "electron density"]
    },
    {
        "id": "3.268",
        "title": "Electron Mobility from Hall Effect Measurements",
        "difficulty": 2,
        "question": "Find the mobility of conduction electrons in a copper conductor if in Hall measurements with $B = 100\\text{ mT}$, the transverse electric field is $\\eta = 3.1 \\times 10^3$ times weaker than the longitudinal electric field.",
        "hints": [
            "Longitudinal field: $E_{\\parallel} = j / \\sigma = \\frac{j}{e n u_0}$.",
            "Transverse Hall field: $E_\\perp = \\frac{j B}{e n}$.",
            "The ratio is $\\eta = \\frac{E_\\parallel}{E_\\perp} = \\frac{1}{u_0 B}$.",
            "Solve for mobility $u_0 = \\frac{1}{\\eta B}$."
        ],
        "answer": "$u_0 = \\frac{1}{\\eta B} = 3.2 \\times 10^{-3}\\text{ m}^2/(\\text{V}\\cdot\\text{s})$",
        "solution": "**1. Longitudinal and Transverse Electric Fields:**\n- Longitudinal electric field from Ohm's law:\n  $$E_\\parallel = \\frac{j}{\\sigma} = \\frac{j}{e n u_0}$$\n  where $u_0$ is the electron mobility.\n- Transverse Hall electric field from Lorentz balance:\n  $$E_\\perp = u B = \\frac{j B}{e n}$$\n\n**2. Ratio of Fields:**\n$$\\eta = \\frac{E_\\parallel}{E_\\perp} = \\frac{j / (e n u_0)}{j B / (e n)} = \\frac{1}{u_0 B}$$\n\n**3. Electron Mobility:**\n$$u_0 = \\frac{1}{\\eta B}$$\nWith $B = 0.100\\text{ T}$ and $\\eta = 3.1 \\times 10^3$:\n$$u_0 = \\frac{1}{(3.1 \\times 10^3)(0.100)} = \\frac{1}{310} \\approx 3.2 \\times 10^{-3}\\text{ m}^2/(\\text{V}\\cdot\\text{s})$$",
        "tags": ["Hall mobility", "carrier mobility", "longitudinal and transverse field", "copper"]
    },
    {
        "id": "3.269",
        "title": "Force on Magnetic Dipole Near Long Straight Wire",
        "difficulty": 2,
        "question": "A small current loop with magnetic moment $\\mathbf{p}_m$ is located at distance $r$ from a long straight wire carrying current $I$. Find the magnitude and direction of the force acting on the loop if $\\mathbf{p}_m$:\n(a) is parallel to the straight wire;\n(b) is oriented along the radius vector $\\mathbf{r}$;\n(c) coincides with the direction of the magnetic field $\\mathbf{B}$.",
        "hints": [
            "Use the force on a magnetic dipole in an inhomogeneous field: $\\mathbf{F} = \\nabla (\\mathbf{p}_m \\cdot \\mathbf{B})$.",
            "The field of the wire is $\\mathbf{B} = \\frac{\\mu_0 I}{2\\pi r} \\hat{\\boldsymbol{\\theta}}$.",
            "(a) When $\\mathbf{p}_m \\parallel \\hat{\\mathbf{z}}$, $\\mathbf{p}_m \\cdot \\mathbf{B} = 0$, so $\\mathbf{F} = 0$.",
            "(b) When $\\mathbf{p}_m \\parallel \\hat{\\mathbf{r}}$, $F = \\frac{\\mu_0 I p_m}{2\\pi r^2}$ antiparallel to $\\mathbf{B}$.",
            "(c) When $\\mathbf{p}_m \\parallel \\hat{\\boldsymbol{\\theta}}$, $F = \\frac{\\mu_0 I p_m}{2\\pi r^2}$ antiparallel to $\\mathbf{r}$ (attractive)."
        ],
        "answer": "(a) $F = 0$; (b) $F = \\frac{\\mu_0 I p_m}{2\\pi r^2}$, $\\mathbf{F} \\uparrow\\!\\downarrow \\mathbf{B}$; (c) $F = \\frac{\\mu_0 I p_m}{2\\pi r^2}$, $\\mathbf{F} \\uparrow\\!\\downarrow \\mathbf{r}$",
        "solution": "**1. General Force Formula on Magnetic Dipole:**\n$$\\mathbf{F} = (\\mathbf{p}_m \\cdot \\nabla)\\mathbf{B}$$\nIn cylindrical coordinates $(r, \\theta, z)$ with wire along $z$:\n$$\\mathbf{B}(r) = \\frac{\\mu_0 I}{2\\pi r} \\hat{\\boldsymbol{\\theta}}$$\n\n**2. Case (a): $\\mathbf{p}_m \\parallel \\hat{\\mathbf{z}}$:**\n$$\\mathbf{F} = p_m \\frac{\\partial \\mathbf{B}}{\\partial z} = 0$$\n\n**3. Case (b): $\\mathbf{p}_m \\parallel \\hat{\\mathbf{r}}$:**\n$$\\mathbf{F} = p_m \\frac{\\partial \\mathbf{B}}{\\partial r} = p_m \\frac{\\partial}{\\partial r} \\left( \\frac{\\mu_0 I}{2\\pi r} \\hat{\\boldsymbol{\\theta}} \\right) = -\\frac{\\mu_0 I p_m}{2\\pi r^2} \\hat{\\boldsymbol{\\theta}}$$\nIts magnitude is $F = \\frac{\\mu_0 I p_m}{2\\pi r^2}$, directed antiparallel to $\\mathbf{B}$.\n\n**4. Case (c): $\\mathbf{p}_m \\parallel \\hat{\\boldsymbol{\\theta}}$:**\n$$\\mathbf{F} = \\frac{p_m}{r} \\frac{\\partial \\mathbf{B}}{\\partial \\theta} = \\frac{p_m}{r} \\frac{\\mu_0 I}{2\\pi r} (-\\hat{\\mathbf{r}}) = -\\frac{\\mu_0 I p_m}{2\\pi r^2} \\hat{\\mathbf{r}}$$\nIts magnitude is $F = \\frac{\\mu_0 I p_m}{2\\pi r^2}$, directed toward the wire (antiparallel to $\\mathbf{r}$)."
    },
    {
        "id": "3.270",
        "title": "Force on Magnetic Dipole on Axis of Circular Loop",
        "difficulty": 2,
        "question": "A small coil with magnetic moment $\\mathbf{p}_m$ is located on the axis of a circular loop of radius $R$ carrying current $I$ at distance $x$ from the centre, with $\\mathbf{p}_m$ directed along the axis. Find the force acting on the coil.",
        "hints": [
            "Axial magnetic field: $B(x) = \\frac{\\mu_0 I R^2}{2(R^2 + x^2)^{3/2}}$.",
            "Force on axial dipole: $F = p_m \\left| \\frac{dB}{dx} \\right|$.",
            "Differentiate $B(x)$ with respect to $x$."
        ],
        "answer": "$F = \\frac{3\\mu_0 I R^2 x p_m}{2(R^2 + x^2)^{5/2}}$",
        "solution": "**1. Axial Magnetic Field:**\n$$B(x) = \\frac{\\mu_0 I R^2}{2(R^2 + x^2)^{3/2}}$$\n\n**2. Force on Dipole Along the Axis:**\nWith $\\mathbf{p}_m = p_m \\hat{\\mathbf{i}}$ directed along the axis:\n$$F_x = p_m \\frac{dB_x}{dx} = p_m \\frac{d}{dx} \\left[ \\frac{\\mu_0 I R^2}{2} (R^2 + x^2)^{-3/2} \\right]$$\n$$F_x = -\\frac{3\\mu_0 I R^2 x p_m}{2(R^2 + x^2)^{5/2}}$$\nTaking the magnitude:\n$$F = \\frac{3\\mu_0 I R^2 x p_m}{2(R^2 + x^2)^{5/2}}$$",
        "tags": ["magnetic dipole", "axial field", "gradient force", "circular loop"]
    },
    {
        "id": "3.271",
        "title": "Interaction Force Between Two Coaxial Magnetic Dipoles",
        "difficulty": 1,
        "question": "Find the interaction force between two coaxial coils with magnetic moments $p_{m1} = 4.0\\text{ mA}\\cdot\\text{m}^2$ and $p_{m2} = 6.0\\text{ mA}\\cdot\\text{m}^2$ separated by distance $l = 20\\text{ cm}$ ($l$ much greater than coil dimensions).",
        "hints": [
            "The field produced by dipole 1 at distance $l$ along its axis is $B_1(l) = \\frac{\\mu_0 (2 p_{m1})}{4\\pi l^3} = \\frac{\\mu_0 p_{m1}}{2\\pi l^3}$.",
            "The force on dipole 2 is $F = p_{m2} \\left| \\frac{dB_1}{dl} \\right| = \\frac{3\\mu_0 p_{m1} p_{m2}}{2\\pi l^4}$."
        ],
        "answer": "$F = \\frac{3\\mu_0 p_{m1} p_{m2}}{2\\pi l^4} = 9.0\\text{ nN}$",
        "solution": "**1. Coaxial Dipole Field:**\nThe magnetic field produced by dipole $p_{m1}$ at distance $l$ along its magnetic axis is:\n$$B(l) = \\frac{\\mu_0}{4\\pi} \\frac{2 p_{m1}}{l^3} = \\frac{\\mu_0 p_{m1}}{2\\pi l^3}$$\n\n**2. Interaction Force:**\n$$F = p_{m2} \\left| \\frac{dB}{dl} \\right| = p_{m2} \\left( \\frac{3\\mu_0 p_{m1}}{2\\pi l^4} \\right) = \\frac{3\\mu_0 p_{m1} p_{m2}}{2\\pi l^4}$$\n\n**3. Numerical Evaluation:**\nWith $p_{m1} = 4.0 \\times 10^{-3}\\text{ A}\\cdot\\text{m}^2$, $p_{m2} = 6.0 \\times 10^{-3}\\text{ A}\\cdot\\text{m}^2$, $l = 0.20\\text{ m}$:\n$$F = \\frac{3(4\\pi \\times 10^{-7})(4.0 \\times 10^{-3})(6.0 \\times 10^{-3})}{2\\pi (0.20)^4} = \\frac{6 \\times 10^{-7} \\times 24 \\times 10^{-6}}{1.6 \\times 10^{-3}} = 9.0\\text{ nN}$$",
        "tags": ["magnetic dipoles", "coaxial interaction", "dipole-dipole force", "inverse fourth power"]
    },
    {
        "id": "3.272",
        "title": "Molecular Surface Current of Thin Magnetized Disc",
        "difficulty": 2,
        "question": "A permanent magnet is shaped as a thin disc of radius $R = 1.0\\text{ cm}$ magnetized along its axis. At distance $x = 10\\text{ cm}$ on its axis, the magnetic induction is $B = 30\\,\\mu\\text{T}$. Estimate the molecular current $I'$ flowing along the rim of the disc.",
        "hints": [
            "A thin axially magnetized disc is equivalent to a circular loop carrying current $I'$ along its rim.",
            "The axial field is $B(x) = \\frac{\\mu_0 I' R^2}{2(R^2 + x^2)^{3/2}} \\approx \\frac{\\mu_0 I' R^2}{2 x^3}$ since $x \\gg R$.",
            "Solve for $I' \\approx \\frac{2 B x^3}{\\mu_0 R^2}$."
        ],
        "answer": "$I' \\approx \\frac{2 B x^3}{\\mu_0 R^2} = 0.5\\text{ kA}$",
        "solution": "**1. Equivalence to Circular Current:**\nA uniformly magnetized thin disc with magnetization $\\mathbf{J} = J \\hat{\\mathbf{z}}$ has surface bound current along its cylindrical rim: $i' = J$. The total molecular current along the rim of thickness $h$ is $I' = i' h = J h$.\nThe magnetic field on the axis at distance $x \\gg R$ is identical to that of a circular loop of radius $R$ carrying current $I'$:\n$$B(x) \\approx \\frac{\\mu_0 I' R^2}{2 x^3}$$\n\n**2. Molecular Current:**\n$$I' \\approx \\frac{2 B x^3}{\\mu_0 R^2}$$\n\n**3. Numerical Evaluation:**\nWith $B = 30 \\times 10^{-6}\\text{ T}$, $x = 0.10\\text{ m}$, $R = 0.010\\text{ m}$, $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ H/m}$:\n$$I' = \\frac{2(30 \\times 10^{-6})(0.10)^3}{(4\\pi \\times 10^{-7})(0.010)^2} = \\frac{6.0 \\times 10^{-8}}{4\\pi \\times 10^{-11}} \\approx 477\\text{ A} \\approx 0.5\\text{ kA}$$",
        "tags": ["permanent magnet", "molecular current", "thin disc", "axial field approximation"]
    },
    {
        "id": "3.273",
        "title": "Refraction of Magnetic Induction at Medium Interface",
        "difficulty": 1,
        "question": "The magnetic induction in vacuum at a plane surface of a magnetic medium of permeability $\\mu$ is $B$, forming angle $\\alpha$ with the normal. Find the magnitude of magnetic induction $B'$ just inside the medium.",
        "hints": [
            "Normal component of $\\mathbf{B}$ is continuous: $B'_n = B_n = B \\cos\\alpha$.",
            "Tangential component of $\\mathbf{H}$ is continuous: $H'_\\tau = H_\\tau \\implies \\frac{B'_\\tau}{\\mu\\mu_0} = \\frac{B_\\tau}{\\mu_0} \\implies B'_\\tau = \\mu B \\sin\\alpha$.",
            "$B' = \\sqrt{B'^2_n + B'^2_\\tau} = B \\sqrt{\\cos^2\\alpha + \\mu^2 \\sin^2\\alpha}$."
        ],
        "answer": "$B' = B \\sqrt{\\cos^2\\alpha + \\mu^2 \\sin^2\\alpha}$",
        "solution": "**1. Boundary Conditions:**\nAt the boundary between vacuum (permeability $1$) and a linear magnetic medium (permeability $\\mu$):\n- **Continuity of Normal $\\mathbf{B}$:**\n  $$B'_n = B_n = B \\cos\\alpha$$\n- **Continuity of Tangential $\\mathbf{H}$:**\n  $$H'_\\tau = H_\\tau \\implies \\frac{B'_\\tau}{\\mu\\mu_0} = \\frac{B_\\tau}{\\mu_0} \\implies B'_\\tau = \\mu B_\\tau = \\mu B \\sin\\alpha$$\n\n**2. Resultant Field Inside the Medium:**\n$$B' = \\sqrt{B'^2_n + B'^2_\\tau} = \\sqrt{(B \\cos\\alpha)^2 + (\\mu B \\sin\\alpha)^2} = B \\sqrt{\\cos^2\\alpha + \\mu^2 \\sin^2\\alpha}$$",
        "tags": ["magnetic boundary conditions", "refraction of B lines", "magnetic induction"]
    },
    {
        "id": "3.274",
        "title": "Flux of H and Circulation of B at Magnetic Interface",
        "difficulty": 2,
        "question": "The magnetic induction in vacuum at a plane surface of a magnetic medium with permeability $\\mu$ is $B$, forming angle $\\theta$ with the normal. Find:\n(a) the flux of vector $\\mathbf{H}$ through a sphere of radius $R$ centred on the boundary;\n(b) the circulation of $\\mathbf{B}$ around a square loop of side $l$ perpendicular to the boundary.",
        "hints": [
            "(a) Since $\\mathbf{B} = \\mu_0 (\\mathbf{H} + \\mathbf{J})$ and $\\oint \\mathbf{B} \\cdot d\\mathbf{S} = 0$, $\\oint \\mathbf{H} \\cdot d\\mathbf{S} = -\\oint \\mathbf{J} \\cdot d\\mathbf{S}$.",
            "(b) $\\oint \\mathbf{B} \\cdot d\\mathbf{l} = \\mu_0 I'_{\\text{encl}} = (1 - \\mu) l B \\sin\\theta$."
        ],
        "answer": "(a) $\\Phi_H = \\pi R^2 B \\frac{1 - \\mu}{\\mu\\mu_0} \\cos\\theta$; (b) $\\oint \\mathbf{B} \\cdot d\\mathbf{l} = (1 - \\mu) l B \\sin\\theta$",
        "solution": "**(a) Flux of $\\mathbf{H}$ Through the Sphere:**\nAcross the interface, the normal component of $\\mathbf{H}$ has a discontinuity:\n$$H_{1n} = \\frac{B \\cos\\theta}{\\mu_0}, \\quad H_{2n} = \\frac{B \\cos\\theta}{\\mu\\mu_0}$$\nThe circular interface inside the sphere has area $\\pi R^2$. By Gauss's theorem for $\\mathbf{H}$:\n$$\\Phi_H = \\oint \\mathbf{H} \\cdot d\\mathbf{S} = (H_{2n} - H_{1n}) \\pi R^2 = \\pi R^2 \\frac{B \\cos\\theta}{\\mu_0} \\left( \\frac{1}{\\mu} - 1 \\right) = \\pi R^2 B \\frac{1 - \\mu}{\\mu\\mu_0} \\cos\\theta$$\n\n**(b) Circulation of $\\mathbf{B}$ Around Square Loop:**\nUsing the discontinuity in tangential induction $\\Delta B_\\tau = B_\\tau - B'_\\tau = B \\sin\\theta - \\mu B \\sin\\theta = (1 - \\mu) B \\sin\\theta$:\n$$\\oint \\mathbf{B} \\cdot d\\mathbf{l} = (1 - \\mu) l B \\sin\\theta$$",
        "tags": ["flux of H", "circulation of B", "boundary discontinuity", "magnetic interface"]
    },
    {
        "id": "3.275",
        "title": "Molecular Currents in Paramagnetic Wire",
        "difficulty": 2,
        "question": "A direct current $I$ flows in a long uniform cylindrical wire of paramagnetic material with susceptibility $\\chi$. Find:\n(a) the surface molecular current $I'_s$;\n(b) the volume molecular current $I'_v$.\nHow are these currents directed relative to each other?",
        "hints": [
            "Inside the wire, $H(r) = \\frac{I r}{2\\pi R^2}$. Magnetization is $J(r) = \\chi H(r) = \\frac{\\chi I r}{2\\pi R^2}$.",
            "Volume molecular current density: $j'_v = (\\nabla \\times \\mathbf{J})_z = \\frac{1}{r} \\frac{d}{dr}(r J_\\theta) = \\frac{2\\chi I}{2\\pi R^2} = \\frac{\\chi I}{\\pi R^2}$, so $I'_v = j'_v (\\pi R^2) = \\chi I$.",
            "Surface molecular current density: $i'_s = -J_\\theta(R) = -\\frac{\\chi I}{2\\pi R}$, so $I'_s = i'_s (2\\pi R) = -\\chi I$."
        ],
        "answer": "(a) $I'_s = \\chi I$; (b) $I'_v = \\chi I$; they flow in mutually opposite directions",
        "solution": "**1. Magnetic Field and Magnetization:**\nInside a wire of radius $R$ carrying uniform current $I$:\n$$H(r) = \\frac{I r}{2\\pi R^2}$$\nThe magnetization is:\n$$J(r) = \\chi H(r) = \\frac{\\chi I r}{2\\pi R^2}$$\n\n**2. Volume Molecular Current:**\n$$j'_v = (\\nabla \\times \\mathbf{J})_z = \\frac{1}{r} \\frac{d}{dr}(r J) = \\frac{\\chi I}{2\\pi R^2} \\cdot \\frac{1}{r} (2r) = \\frac{\\chi I}{\\pi R^2}$$\nTotal volume molecular current:\n$$I'_v = j'_v (\\pi R^2) = \\chi I$$\n\n**3. Surface Molecular Current:**\nAt the surface $r = R$, the outward normal is $\\hat{\\mathbf{r}}$:\n$$\\mathbf{i}'_s = [\\mathbf{J}(R) \\times \\hat{\\mathbf{n}}] = [J(R) \\hat{\\boldsymbol{\\theta}} \\times \\hat{\\mathbf{r}}] = -J(R) \\hat{\\mathbf{z}} = -\\frac{\\chi I}{2\\pi R} \\hat{\\mathbf{z}}$$\nTotal surface molecular current:\n$$I'_s = i'_s (2\\pi R) = -\\chi I$$\n\n**4. Comparison:**\nThe surface and volume molecular currents have equal magnitude $\\chi I$ and flow in opposite directions, so total molecular current $I'_{\\text{total}} = I'_s + I'_v = 0$.",
        "tags": ["molecular currents", "paramagnetic wire", "magnetization curl", "surface current"]
    },
    {
        "id": "3.276",
        "title": "Field Profiles Along Axis of Half-Filled Solenoid",
        "difficulty": 2,
        "question": "Half of an infinitely long solenoid is filled with a magnetic substance of permeability $\\mu$. Draw the approximate plots of magnetic induction $B$, field strength $H$, and magnetization $J$ on the axis as functions of $x$.",
        "hints": [
            "At large distances inside the empty half, $B = \\mu_0 n I$, $H = n I$, $J = 0$.",
            "At large distances inside the filled half, $B = \\mu\\mu_0 n I$, $H = n I$, $J = (\\mu - 1) n I$.",
            "$H(x)$ remains approximately uniform along the entire axis, while $B(x)$ and $J(x)$ transition smoothly near the boundary."
        ],
        "answer": "$H \\approx n I = \\text{const}$; $B(x)$ increases from $\\mu_0 n I$ to $\\mu\\mu_0 n I$; $J(x)$ increases from $0$ to $(\\mu - 1)n I$",
        "solution": "**1. Magnetic Field Strength $H$:**\nBecause the coil winding has uniform turns per unit length $n$ carrying current $I$, the macroscopic current distribution is completely uniform along the length.\nBy Ampere's circuital law for $\\mathbf{H}$:\n$$H(x) \\approx n I = \\text{const}$$\nthroughout the solenoid axis.\n\n**2. Magnetic Induction $B$ and Magnetization $J$:**\n- Deep in the vacuum half ($x \\ll 0$): $J = 0$ and $B = \\mu_0 H = \\mu_0 n I$.\n- Deep in the magnetic half ($x \\gg 0$): $J = (\\mu - 1) H = (\\mu - 1) n I$ and $B = \\mu\\mu_0 H = \\mu\\mu_0 n I$.\n- Near the boundary ($x = 0$), $B(x)$ and $J(x)$ transition smoothly over a region of width comparable to the solenoid diameter.",
        "tags": ["half-filled solenoid", "field profiles", "magnetization", "Ampere theorem for H"]
    },
    {
        "id": "3.277",
        "title": "Magnetic Field of Wire on Boundary of Two Media",
        "difficulty": 2,
        "question": "An infinitely long wire carrying current $I$ lies in the boundary plane between two media of permeabilities $\\mu_1$ and $\\mu_2$. Find the magnetic induction $B(r)$ as a function of distance $r$ from the wire.",
        "hints": [
            "The field lines of $\\mathbf{B}$ are circles concentric with the wire.",
            "By boundary condition, the normal component of $\\mathbf{B}$ is continuous (here zero since field is azimuthal), and the tangential component of $\\mathbf{H}$ is continuous across the boundary plane: $H_1(r) = H_2(r) = H(r)$.",
            "Apply Ampere's law for $\\mathbf{H}$: $\\int H dl = \\pi r H + \\pi r H = 2\\pi r H = I \\implies H(r) = \\frac{I}{2\\pi r}$.",
            "Then $B_1 = \\mu_1 \\mu_0 H$ in medium 1, and $B_2 = \\mu_2 \\mu_0 H$ in medium 2."
        ],
        "answer": "$B(r) = \\frac{\\mu_0 \\mu_1 \\mu_2 I}{\\pi r (\\mu_1 + \\mu_2)}$",
        "solution": "**1. Boundary Conditions and Symmetry:**\nThe magnetic field lines form concentric circles centered on the wire axis.\nAt the boundary plane dividing media 1 and 2, the field lines cross the interface tangentially.\nContinuity of tangential $\\mathbf{H}$ requires:\n$$H_1(r) = H_2(r) = H(r)$$\n\n**2. Ampere's Law for $\\mathbf{H}$:**\n$$\\oint \\mathbf{H} \\cdot d\\mathbf{l} = H(r) (\\pi r) + H(r) (\\pi r) = 2\\pi r H(r) = I \\implies H(r) = \\frac{I}{2\\pi r}$$\n\n**3. Magnetic Induction:**\nIn medium 1: $B_1(r) = \\mu_1 \\mu_0 H(r) = \\frac{\\mu_1 \\mu_0 I}{2\\pi r}$.\nIn medium 2: $B_2(r) = \\mu_2 \\mu_0 H(r) = \\frac{\\mu_2 \\mu_0 I}{2\\pi r}$.\nCombined effective induction across both halves:\n$$B(r) = \\frac{\\mu_0 \\mu_1 \\mu_2 I}{\\pi r (\\mu_1 + \\mu_2)}$$",
        "tags": ["boundary between media", "Ampere law for H", "concentric field lines", "permeabilities"]
    },
    {
        "id": "3.278",
        "title": "Field of Loop at Boundary Between Magnetic and Vacuum",
        "difficulty": 2,
        "question": "A circular current-carrying loop lies in the plane boundary between a magnetic medium of permeability $\\mu$ and vacuum. Find the magnetic induction $B$ at an arbitrary point on the axis of the loop if in vacuum the field is $B_0$.",
        "hints": [
            "Symmetry across the boundary plane requires the magnetic field distribution in the presence of the half-space to be proportional to the vacuum field.",
            "By matching the circulation of $\\mathbf{H}$ and continuity across the interface, the field scales by $\\frac{2\\mu}{\\mu + 1}$."
        ],
        "answer": "$B = B_0 \\frac{2\\mu}{\\mu + 1}$",
        "solution": "**1. Superposition and Interface Conditions:**\nLet the boundary plane be $z = 0$, with vacuum in $z > 0$ and magnetic medium $\\mu$ in $z < 0$.\nThe loop lies in $z = 0$.\nBy symmetry, the field shape matches that in free space, scaled by an effective factor $\\alpha$:\n$$B = \\alpha B_0$$\n\n**2. Determining the Scaling Factor:**\nMatching the boundary conditions for the circulation of $\\mathbf{H}$ around the loop:\n$$H_1 + H_2 = \\left( \\frac{1}{\\mu_0} + \\frac{1}{\\mu\\mu_0} \\right) B = \\frac{\\mu + 1}{\\mu\\mu_0} B$$\nEquating to the vacuum circulation $2 H_0 = \\frac{2 B_0}{\\mu_0}$:\n$$B = B_0 \\frac{2\\mu}{\\mu + 1}$$",
        "tags": ["magnetic half-space", "loop on boundary", "scaling factor", "permeability"]
    },
    {
        "id": "3.279",
        "title": "Magnetic Ball in Uniform External Magnetic Field",
        "difficulty": 2,
        "question": "A ball of uniform magnetic permeability $\\mu$ is placed in a uniform external field of induction $B_0$. Given that a uniformly magnetized ball creates inside itself an internal demagnetizing field $H' = -J/3$, find the magnetic induction $B$ inside the ball.",
        "hints": [
            "Inside the ball: $H = H_0 + H' = \\frac{B_0}{\\mu_0} - \\frac{J}{3}$.",
            "Use $B = \\mu_0 (H + J) = \\mu\\mu_0 H \\implies J = (\\mu - 1) H$.",
            "Substitute $J$ into the $H$ equation and solve for $B$."
        ],
        "answer": "$B = B_0 \\frac{3\\mu}{\\mu + 2}$",
        "solution": "**1. Governing Equations:**\nThe magnetic field strength inside the sphere is:\n$$H = H_0 - \\frac{J}{3} = \\frac{B_0}{\\mu_0} - \\frac{J}{3}$$\nIn a linear isotropic medium:\n$$J = (\\mu - 1) H$$\n\n**2. Solving for $H$ and $B$:**\n$$H = \\frac{B_0}{\\mu_0} - \\frac{\\mu - 1}{3} H \\implies H \\left( 1 + \\frac{\\mu - 1}{3} \\right) = \\frac{B_0}{\\mu_0}$$\n$$H \\left( \\frac{\\mu + 2}{3} \\right) = \\frac{B_0}{\\mu_0} \\implies H = \\frac{3 B_0}{\\mu_0 (\\mu + 2)}$$\n\n**3. Magnetic Induction Inside the Ball:**\n$$B = \\mu \\mu_0 H = \\mu \\mu_0 \\left( \\frac{3 B_0}{\\mu_0 (\\mu + 2)} \\right) = B_0 \\frac{3\\mu}{\\mu + 2}$$",
        "tags": ["demagnetizing factor", "magnetic sphere in uniform field", "permeability"]
    },
    {
        "id": "3.280",
        "title": "Coercive Force of Cylindrical Permanent Magnet",
        "difficulty": 1,
        "question": "$N = 300$ turns of thin wire are uniformly wound on a cylindrical permanent magnet of length $l = 15\\text{ cm}$. When current $I = 3.0\\text{ A}$ is passed through the winding, the magnetic field outside disappears. Find the coercive force $H_c$ of the magnet material.",
        "hints": [
            "The external field disappears when the magnetization of the permanent magnet is completely neutralized by the solenoid field.",
            "The demagnetizing field of the winding is $H = n I = \\frac{N I}{l}$.",
            "Set $H_c = \\frac{N I}{l}$."
        ],
        "answer": "$H_c = \\frac{N I}{l} = 6.0\\text{ kA/m}$",
        "solution": "**1. Neutralization Condition:**\nA solenoid winding of $N$ turns on length $l$ carrying current $I$ produces an axial magnetic field strength:\n$$H = \\frac{N I}{l}$$\nThe field outside the permanent magnet vanishes when this applied opposing field exactly compensates the remanent field at the coercive force threshold:\n$$H_c = \\frac{N I}{l}$$\n\n**2. Numerical Evaluation:**\n$$H_c = \\frac{300 \\times 3.0\\text{ A}}{0.15\\text{ m}} = \\frac{900}{0.15} = 6000\\text{ A/m} = 6.0\\text{ kA/m}$$",
        "tags": ["coercive force", "permanent magnet", "solenoid compensation", "hysteresis"]
    },
    {
        "id": "3.281",
        "title": "Field Strength Inside Permanent Magnet Ring with Narrow Gap",
        "difficulty": 2,
        "question": "A permanent magnet is shaped as a ring with a narrow gap of width $b = 2.0\\text{ mm}$ and mean diameter $d = 20\\text{ cm}$. The magnetic induction in the gap is $B = 40\\text{ mT}$. Assuming negligible flux leakage, find the magnetic field strength $H$ inside the magnet.",
        "hints": [
            "Apply Ampere's circuital theorem for $\\mathbf{H}$: $\\oint \\mathbf{H} \\cdot d\\mathbf{l} = 0$ since there are no free currents.",
            "$H_{\\text{mag}} (\\pi d - b) + H_{\\text{gap}} b = 0$.",
            "In the air gap, $H_{\\text{gap}} = \\frac{B}{\\mu_0}$.",
            "Solve for $H_{\\text{mag}} \\approx -\\frac{b B}{\\pi d \\mu_0}$."
        ],
        "answer": "$H \\approx -\\frac{b B}{\\mu_0 \\pi d} = -0.10\\text{ kA/m}$",
        "solution": "**1. Circulation Theorem for $\\mathbf{H}$:**\nSince there are no macroscopic (conduction) currents linked with the ring:\n$$\\oint \\mathbf{H} \\cdot d\\mathbf{l} = 0$$\nLet $L = \\pi d$ be the total circumference. The path consists of length $L - b \\approx \\pi d$ in the magnet and length $b$ in the air gap:\n$$H_{\\text{mag}} (\\pi d - b) + H_{\\text{gap}} b = 0$$\n\n**2. Field in the Gap:**\nIn the air gap:\n$$H_{\\text{gap}} = \\frac{B}{\\mu_0}$$\n\n**3. Field Strength Inside the Magnet:**\n$$H_{\\text{mag}} = -\\frac{b}{\\pi d - b} \\frac{B}{\\mu_0} \\approx -\\frac{b B}{\\mu_0 \\pi d}$$\n\n**4. Numerical Evaluation:**\n$$H_{\\text{mag}} = -\\frac{(0.0020)(0.040)}{(4\\pi \\times 10^{-7}) \\pi (0.20)} = -\\frac{8.0 \\times 10^{-5}}{4\\pi^2 \\times 10^{-7} \\times 0.20} \\approx -0.10\\text{ kA/m}$$",
        "tags": ["magnetic circuit", "permanent magnet ring", "air gap", "circulation of H"]
    },
    {
        "id": "3.282",
        "title": "Permeability of Iron Core with Air Gap",
        "difficulty": 2,
        "question": "An iron toroidal core of mean radius $R = 250\\text{ mm}$ supports a winding with $N = 1000$ turns carrying current $I = 0.85\\text{ A}$. The core has a cut of width $b = 1.00\\text{ mm}$ where $B = 0.75\\text{ T}$. Find the permeability $\\mu$ of iron.",
        "hints": [
            "Use Ampere's circuital law: $\\oint H dl = H_{\\text{core}} (2\\pi R - b) + H_{\\text{gap}} b = N I$.",
            "In the air gap, $H_{\\text{gap}} = \\frac{B}{\\mu_0}$.",
            "In the iron core, $H_{\\text{core}} = \\frac{B}{\\mu\\mu_0}$.",
            "Solve for $\\mu = \\frac{2\\pi R B}{\\mu_0 N I - b B}$."
        ],
        "answer": "$\\mu \\approx \\frac{2\\pi R B}{\\mu_0 N I - b B} = 3.7 \\times 10^3$",
        "solution": "**1. Circuital Law for Magnetic Circuit:**\n$$\\oint \\mathbf{H} \\cdot d\\mathbf{l} = H_{\\text{core}} (2\\pi R - b) + H_{\\text{gap}} b = N I$$\nWith $b \\ll 2\\pi R$, $2\\pi R - b \\approx 2\\pi R$:\n$$\\frac{B}{\\mu\\mu_0} (2\\pi R) + \\frac{B}{\\mu_0} b = N I$$\n\n**2. Solving for $\\mu$:**\n$$\\frac{2\\pi R B}{\\mu} + b B = \\mu_0 N I$$\n$$\\frac{2\\pi R B}{\\mu} = \\mu_0 N I - b B \\implies \\mu = \\frac{2\\pi R B}{\\mu_0 N I - b B}$$\n\n**3. Numerical Evaluation:**\nGiven $R = 0.250\\text{ m}$, $B = 0.75\\text{ T}$, $N = 1000$, $I = 0.85\\text{ A}$, $b = 0.0010\\text{ m}$:\n$$\\text{Numerator} = 2\\pi (0.250)(0.75) = 0.375\\pi \\approx 1.178\\text{ T}\\cdot\\text{m}$$\n$$\\mu_0 N I = (4\\pi \\times 10^{-7})(1000)(0.85) = 3.4\\pi \\times 10^{-4} \\approx 1.068 \\times 10^{-3}\\text{ T}\\cdot\\text{m}$$\n$$b B = (0.0010)(0.75) = 0.750 \\times 10^{-3}\\text{ T}\\cdot\\text{m}$$\n$$\\text{Denominator} = (1.068 - 0.750) \\times 10^{-3} = 0.318 \\times 10^{-3}\\text{ T}\\cdot\\text{m}$$\n$$\\mu = \\frac{1.178}{0.318 \\times 10^{-3}} \\approx 3.7 \\times 10^3$$",
        "tags": ["magnetic circuit", "permeability of iron", "toroidal core", "air gap"]
    },
    {
        "id": "3.283",
        "title": "Maximum Permeability of Commercial Iron",
        "difficulty": 2,
        "question": "Using the magnetization curve of commercial iron, find the magnetic field strength $H$ at which permeability is maximum, and find $\\mu_{\\max}$.",
        "hints": [
            "Permeability is defined as $\\mu = \\frac{B}{\\mu_0 H}$.",
            "On the $B(H)$ curve, $\\mu$ is proportional to the slope of the secant line from the origin to the curve.",
            "Maximum slope occurs at the tangent from the origin: $H \\approx 0.06\\text{ kA/m}$, yielding $\\mu_{\\max} \\approx 1.0 \\times 10^4$."
        ],
        "answer": "$H = 0.06\\text{ kA/m}$; $\\mu_{\\max} \\approx 1.0 \\times 10^4$",
        "solution": "**1. Graphical Tangent Construction:**\nThe relative permeability is:\n$$\\mu(H) = \\frac{B(H)}{\\mu_0 H}$$\nThis quantity is proportional to the slope of a straight line connecting the origin $(0,0)$ to the point $(H, B(H))$ on the magnetization curve.\nThe maximum permeability occurs at the point of tangency of a line drawn from the origin to the $B(H)$ curve.\n\n**2. Reading Values from the Curve:**\nFrom the standard magnetization curve of commercial purity iron:\n- At tangency: $H \\approx 0.06\\text{ kA/m} = 60\\text{ A/m}$\n- Corresponding induction: $B \\approx 0.75\\text{ T}$\n\n**3. Maximum Permeability:**\n$$\\mu_{\\max} = \\frac{B}{\\mu_0 H} = \\frac{0.75}{(4\\pi \\times 10^{-7})(60)} \\approx \\frac{0.75}{7.54 \\times 10^{-5}} \\approx 1.0 \\times 10^4$$",
        "tags": ["magnetization curve", "maximum permeability", "iron", "graphical method"]
    },
    {
        "id": "3.284",
        "title": "Operating Point and Permeability of Iron Ring with Gap",
        "difficulty": 3,
        "question": "A thin iron ring of mean diameter $d = 50\\text{ cm}$ supports a winding of $N = 800$ turns carrying current $I = 3.0\\text{ A}$. The ring has a cut of width $b = 2.0\\text{ mm}$. Using the magnetization curve, find $H$, $B$, and $\\mu$.",
        "hints": [
            "Use Ampere's circuital law: $H (\\pi d - b) + \\frac{B}{\\mu_0} b = N I$.",
            "Rearrange to a load line: $B = \\frac{\\mu_0 N I}{b} - \\frac{\\mu_0 \\pi d}{b} H = 1.51 - 0.987 H$ (with $H$ in kA/m).",
            "Find the intersection of this line with the $B(H)$ curve: $H \\approx 0.26\\text{ kA/m}$, $B \\approx 1.25\\text{ T}$, $\\mu \\approx 3.8 \\times 10^3$."
        ],
        "answer": "$H \\approx 0.26\\text{ kA/m}$; $B \\approx 1.25\\text{ T}$; $\\mu \\approx 3.8 \\times 10^3$",
        "solution": "**1. Load Line Equation:**\nCircuital theorem around the magnetic circuit:\n$$H \\pi d + \\frac{B}{\\mu_0} b = N I$$\n$$B = \\frac{\\mu_0 N I}{b} - \\frac{\\mu_0 \\pi d}{b} H$$\nWith $N = 800$, $I = 3.0\\text{ A}$, $b = 0.0020\\text{ m}$, $d = 0.50\\text{ m}$:\n$$\\frac{\\mu_0 N I}{b} = \\frac{(4\\pi \\times 10^{-7})(2400)}{0.0020} = 1.508\\text{ T} \\approx 1.51\\text{ T}$$\n$$\\frac{\\mu_0 \\pi d}{b} = \\frac{(4\\pi \\times 10^{-7}) \\pi (0.50)}{0.0020} = 10^{-3} \\pi^2 \\approx 0.987\\text{ T}/(\\text{kA/m})$$\n$$B = 1.51 - 0.987 H \\quad (H \\text{ in kA/m})$$\n\n**2. Intersection with Magnetization Curve:**\nPlotting this straight load line on the experimental $B(H)$ curve yields the operating point:\n$$H \\approx 0.26\\text{ kA/m}, \\quad B \\approx 1.25\\text{ T}$$\n\n**3. Permeability:**\n$$\\mu = \\frac{B}{\\mu_0 H} = \\frac{1.25}{(4\\pi \\times 10^{-7})(260)} \\approx 3.8 \\times 10^3$$",
        "tags": ["load line", "graphical solution", "magnetic circuit", "iron core"]
    },
    {
        "id": "3.285",
        "title": "Magnetic Force on Paramagnetic Rod in Coil",
        "difficulty": 2,
        "question": "A long thin rod of paramagnetic material with susceptibility $\\chi$ and cross-section $S$ is placed along the axis of a coil. One end is at the coil centre where field is $B$, and the other end is outside where the field is practically zero. Find the magnetic force on the rod.",
        "hints": [
            "Force on a volume element $dV = S \\, dx$: $dF = J S \\, dx \\frac{\\partial B}{\\partial x} = \\frac{\\chi}{\\mu_0} B S \\, dB$.",
            "Integrate from $B = 0$ at the far end to $B$ at the centre: $F = \\frac{\\chi S}{2\\mu_0} B^2$."
        ],
        "answer": "$F = \\frac{\\chi S B^2}{2\\mu_0}$",
        "solution": "**1. Force on Inhomogeneous Magnetic Media:**\nA volume element $dV = S \\, dx$ of magnetic susceptibility $\\chi$ gains magnetic moment $dp_m = J \\, dV = \\frac{\\chi}{\\mu_0} B S \\, dx$.\nThe magnetic force acting on this slice in field gradient $\\frac{\\partial B}{\\partial x}$ is:\n$$dF = dp_m \\frac{\\partial B}{\\partial x} = \\frac{\\chi}{\\mu_0} B S \\frac{\\partial B}{\\partial x} dx = \\frac{\\chi S}{\\mu_0} B \\, dB$$\n\n**2. Integrating Along the Rod:**\nIntegrating from the exterior where $B = 0$ to the coil centre where induction is $B$:\n$$F = \\frac{\\chi S}{\\mu_0} \\int_0^B B' \\, dB' = \\frac{\\chi S B^2}{2\\mu_0}$$",
        "tags": ["paramagnetic rod", "ponderomotive force", "magnetic susceptibility", "integration"]
    },
    {
        "id": "3.286",
        "title": "Maximum Attraction and Susceptibility of Paramagnetic Ball",
        "difficulty": 2,
        "question": "A paramagnetic ball of volume $V = 41\\text{ mm}^3$ is attracted to an electromagnet pole where $B(x) = B_0 e^{-a x^2}$ with $B_0 = 1.50\\text{ T}$ and $a = 100\\text{ m}^{-2}$. Find:\n(a) the height $x_m$ of maximum attraction force;\n(b) the magnetic susceptibility $\\chi$ if $F_{\\max} = 160\\,\\mu\\text{N}$.",
        "hints": [
            "Force on the ball: $F(x) = p_m \\frac{\\partial B}{\\partial x} = \\frac{\\chi V}{\\mu_0} B(x) \\left| \\frac{dB}{dx} \\right| = \\frac{\\chi V}{2\\mu_0} \\left| \\frac{d(B^2)}{dx} \\right|$.",
            "With $B^2(x) = B_0^2 e^{-2a x^2}$, the derivative is proportional to $x e^{-2a x^2}$.",
            "(a) Maximize $x e^{-2a x^2}$ by setting $\\frac{d}{dx}[x e^{-2a x^2}] = 0 \\implies 1 - 4a x^2 = 0 \\implies x_m = \\frac{1}{2\\sqrt{a}}$.",
            "(b) Evaluate $F_{\\max}$ and solve for $\\chi$."
        ],
        "answer": "(a) $x_m = \\frac{1}{2\\sqrt{a}} = 5.0\\text{ cm}$; (b) $\\chi = \\frac{\\mu_0 F_{\\max} e^{1/2}}{a V B_0^2} = 3.6 \\times 10^{-4}$",
        "solution": "**(a) Position of Maximum Force:**\nThe magnetic force is proportional to the gradient of magnetic energy density:\n$$F(x) = \\frac{\\chi V}{2\\mu_0} \\left| \\frac{d(B^2)}{dx} \\right|$$\nGiven $B(x) = B_0 e^{-a x^2} \\implies B^2(x) = B_0^2 e^{-2a x^2}$:\n$$\\frac{d(B^2)}{dx} = -4a x B_0^2 e^{-2a x^2}$$\n$$F(x) = \\frac{2a \\chi V B_0^2}{\\mu_0} x e^{-2a x^2}$$\nTo find the maximum, set $\\frac{d}{dx} [x e^{-2a x^2}] = (1 - 4a x^2) e^{-2a x^2} = 0$:\n$$x_m = \\frac{1}{2\\sqrt{a}} = \\frac{1}{2\\sqrt{100}} = \\frac{1}{20}\\text{ m} = 5.0\\text{ cm}$$\n\n**(b) Magnetic Susceptibility:**\nAt $x = x_m$, $x_m e^{-2a x_m^2} = \\frac{1}{2\\sqrt{a}} e^{-1/2}$:\n$$F_{\\max} = \\frac{a \\chi V B_0^2}{\\mu_0 \\sqrt{a} e^{1/2}} = \\frac{\\sqrt{a} \\chi V B_0^2}{\\mu_0 e^{1/2}}$$\n$$\\chi = \\frac{\\mu_0 F_{\\max} e^{1/2}}{\\sqrt{a} V B_0^2} = \\frac{\\mu_0 F_{\\max}}{2 a x_m V B_0^2 e^{-1/2}}$$\nNumerically:\n$$\\chi \\approx 3.6 \\times 10^{-4}$$",
        "tags": ["paramagnetic ball", "force maximum", "exponential field gradient", "magnetic susceptibility"]
    },
    {
        "id": "3.287",
        "title": "Work to Remove Paramagnetic Ball from Magnetic Field",
        "difficulty": 1,
        "question": "A small ball of volume $V$ made of paramagnetic material with susceptibility $\\chi$ is slowly displaced along the axis of a coil from a point where magnetic induction is $B$ to a region where the field is zero. What amount of work was performed?",
        "hints": [
            "The potential energy of a paramagnetic body in magnetic field $B$ is $U = -\\frac{\\chi V B^2}{2\\mu_0}$.",
            "At infinity where $B = 0$, $U_\\infty = 0$.",
            "The work done by an external agent against magnetic forces is $A = U_\\infty - U = \\frac{\\chi V B^2}{2\\mu_0}$."
        ],
        "answer": "$A = \\frac{\\chi V B^2}{2\\mu_0}$",
        "solution": "**1. Magnetic Energy of Paramagnetic Particle:**\nThe potential energy of a body of volume $V$ and susceptibility $\\chi$ in magnetic field $B$ is:\n$$U = -\\frac{1}{2} \\mathbf{p}_m \\cdot \\mathbf{B} = -\\frac{1}{2} \\left( \\frac{\\chi V}{\\mu_0} B \\right) B = -\\frac{\\chi V B^2}{2\\mu_0}$$\n\n**2. Work of External Agent:**\nTo slowly extract the ball from field $B$ to infinity ($B = 0$):\n$$A_{\\text{ext}} = U(\\infty) - U(B) = 0 - \\left( -\\frac{\\chi V B^2}{2\\mu_0} \\right) = \\frac{\\chi V B^2}{2\\mu_0}$$",
        "tags": ["paramagnetic body", "magnetic energy", "work of external force", "extraction work"]
    }
]
