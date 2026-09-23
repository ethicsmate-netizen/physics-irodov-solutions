"""
part3_ch3_5b.py
Curated problems 3.243 to 3.265 (23 problems) of Irodov Chapter 3.5:
Constant Magnetic Field. Magnetics (Part B).
"""

CH3_5B_CURATED = [
    {
        "id": "3.243",
        "title": "Magnetic Moment of Circular Current Loop",
        "difficulty": 1,
        "question": "Find the magnetic moment of a thin circular loop with current if its radius is $R = 100\\text{ mm}$ and the magnetic induction at its centre is $B = 6.0\\,\\mu\\text{T}$.",
        "hints": [
            "The magnetic induction at the centre of a circular loop is $B = \\frac{\\mu_0 I}{2R}$, so $I = \\frac{2RB}{\\mu_0}$.",
            "The magnetic moment is $p_m = I S = I (\\pi R^2)$.",
            "Substitute $I$ to get $p_m = \\frac{2\\pi R^3 B}{\\mu_0}$."
        ],
        "answer": "$p_m = \\frac{2\\pi R^3 B}{\\mu_0} = 30\\text{ mA}\\cdot\\text{m}^2$",
        "solution": "**1. Current in the Loop:**\nFrom the formula for the magnetic induction at the centre of a circular loop:\n$$B = \\frac{\\mu_0 I}{2R} \\implies I = \\frac{2 R B}{\\mu_0}$$\n\n**2. Magnetic Moment:**\n$$p_m = I S = I (\\pi R^2) = \\left( \\frac{2 R B}{\\mu_0} \\right) (\\pi R^2) = \\frac{2\\pi R^3 B}{\\mu_0}$$\n\n**3. Numerical Evaluation:**\nWith $R = 0.100\\text{ m}$, $B = 6.0 \\times 10^{-6}\\text{ T}$, and $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ H/m}$:\n$$p_m = \\frac{2\\pi (0.100)^3 (6.0 \\times 10^{-6})}{4\\pi \\times 10^{-7}} = \\frac{1.2 \\times 10^{-8}}{4 \\times 10^{-7}} = 0.030\\text{ A}\\cdot\\text{m}^2 = 30\\text{ mA}\\cdot\\text{m}^2$$",
        "tags": ["magnetic moment", "circular loop", "centre field", "Biot Savart law"]
    },
    {
        "id": "3.244",
        "title": "Magnetic Moment of Semicircular Toroidal Winding",
        "difficulty": 2,
        "question": "Calculate the magnetic moment of a thin wire carrying current $I = 0.8\\text{ A}$ wound tightly on half a torus of cross-sectional diameter $d = 5.0\\text{ cm}$ with $N = 500$ turns.",
        "hints": [
            "Each circular turn has cross-sectional area $S = \\frac{\\pi d^2}{4}$ and magnetic moment $p_1 = I S$.",
            "The magnetic moment vectors $\\mathbf{p}_1$ point tangentially along the semicircular centerline of the torus.",
            "Integrate the vector sum of moments over the semicircle of angle $\\pi$: $p_m = \\int_0^\\pi p_1 \\frac{N}{\\pi} \\sin\\theta \\, d\\theta = \\frac{2 N I S}{\\pi} = \\frac{1}{2} N I d^2$."
        ],
        "answer": "$p_m = \\frac{1}{2} N I d^2 = 0.5\\text{ A}\\cdot\\text{m}^2$",
        "solution": "**1. Elementary Magnetic Moments:**\nEach turn of the winding has cross-sectional area $S = \\frac{\\pi d^2}{4}$ and carries current $I$.\nIts magnetic moment vector has magnitude $dp_m = I S \\left( \\frac{N}{\\pi} d\\theta \\right)$ directed tangentially along the torus centerline.\n\n**2. Vector Integration:**\nAligning the symmetry axis along the $y$-direction:\n$$p_m = \\int_0^\\pi (I S) \\frac{N}{\\pi} \\sin\\theta \\, d\\theta = \\frac{N I S}{\\pi} [-\\cos\\theta]_0^\\pi = \\frac{2 N I S}{\\pi}$$\nSubstituting $S = \\frac{\\pi d^2}{4}$:\n$$p_m = \\frac{2 N I}{\\pi} \\left( \\frac{\\pi d^2}{4} \\right) = \\frac{1}{2} N I d^2$$\n\n**3. Numerical Evaluation:**\n$$p_m = \\frac{1}{2} \\times 500 \\times 0.8 \\times (0.050)^2 = 200 \\times 0.0025 = 0.50\\text{ A}\\cdot\\text{m}^2$$",
        "tags": ["magnetic moment", "semitorus", "vector integration", "distributed winding"]
    },
    {
        "id": "3.245",
        "title": "Field and Magnetic Moment of Flat Spiral Coil",
        "difficulty": 2,
        "question": "A thin wire forms a plane spiral of $N = 100$ tight turns carrying current $I = 8\\text{ mA}$. The inner and outer radii are $a = 50\\text{ mm}$ and $b = 100\\text{ mm}$. Find:\n(a) the magnetic induction at the centre of the spiral;\n(b) the magnetic moment of the spiral.",
        "hints": [
            "The turn density is $n = \\frac{N}{b - a}$. A ring of radius $r$ has $dn = n \\, dr$ turns.",
            "(a) Magnetic field at centre: $B = \\int_a^b \\frac{\\mu_0 I (n \\, dr)}{2r} = \\frac{\\mu_0 N I}{2(b - a)} \\ln\\left(\\frac{b}{a}\\right)$.",
            "(b) Magnetic moment: $p_m = \\int_a^b I (\\pi r^2) (n \\, dr) = \\frac{\\pi N I}{3(b - a)} (b^3 - a^3) = \\frac{1}{3} \\pi N I (a^2 + ab + b^2)$."
        ],
        "answer": "(a) $B = \\frac{\\mu_0 N I}{2(b - a)} \\ln\\left(\\frac{b}{a}\\right) = 7.0\\,\\mu\\text{T}$; (b) $p_m = \\frac{1}{3}\\pi N I (a^2 + ab + b^2) = 15\\text{ mA}\\cdot\\text{m}^2$",
        "solution": "**(a) Magnetic Induction at the Centre:**\nNumber of turns in radial interval $dr$ is $dN = \\frac{N}{b - a} dr$.\nEach turn contributes $dB = \\frac{\\mu_0 I}{2r} dN$:\n$$B = \\int_a^b \\frac{\\mu_0 I N}{2(b - a)} \\frac{dr}{r} = \\frac{\\mu_0 N I}{2(b - a)} \\ln\\left(\\frac{b}{a}\\right)$$\nWith $N = 100$, $I = 8.0 \\times 10^{-3}\\text{ A}$, $a = 0.050\\text{ m}$, $b = 0.100\\text{ m}$:\n$$B = \\frac{(4\\pi \\times 10^{-7}) \\times 100 \\times 0.008}{2(0.050)} \\ln 2 = \\frac{3.2\\pi \\times 10^{-6}}{0.10} \\times 0.693 \\approx 7.0\\,\\mu\\text{T}$$\n\n**(b) Magnetic Moment:**\n$$p_m = \\int_a^b I (\\pi r^2) dN = \\frac{\\pi N I}{b - a} \\int_a^b r^2 \\, dr = \\frac{\\pi N I}{3(b - a)} (b^3 - a^3) = \\frac{1}{3}\\pi N I (a^2 + ab + b^2)$$\nEvaluating numerically:\n$$a^2 + ab + b^2 = 0.0025 + 0.0050 + 0.0100 = 0.0175\\text{ m}^2$$\n$$p_m = \\frac{\\pi \\times 100 \\times 0.008 \\times 0.0175}{3} \\approx 15\\text{ mA}\\cdot\\text{m}^2$$",
        "tags": ["flat spiral", "Biot Savart law", "magnetic moment", "radial integration"]
    },
    {
        "id": "3.246",
        "title": "Magnetic Field and Moment of Rotating Charged Disc",
        "difficulty": 2,
        "question": "A non-conducting thin disc of radius $R$ charged uniformly on one side with surface density $\\sigma$ rotates about its axis with angular velocity $\\omega$. Find:\n(a) the magnetic induction at the centre of the disc;\n(b) the magnetic moment of the disc.",
        "hints": [
            "A ring of radius $r$ and width $dr$ carries charge $dq = \\sigma (2\\pi r \\, dr)$.",
            "The circulating current is $dI = \\frac{\\omega}{2\\pi} dq = \\sigma \\omega r \\, dr$.",
            "(a) $B = \\int_0^R \\frac{\\mu_0 dI}{2r} = \\frac{1}{2} \\mu_0 \\sigma \\omega R$.",
            "(b) $p_m = \\int_0^R dI (\\pi r^2) = \\frac{1}{4} \\pi \\sigma \\omega R^4$."
        ],
        "answer": "(a) $B = \\frac{1}{2} \\mu_0 \\sigma \\omega R$; (b) $p_m = \\frac{1}{4} \\pi \\sigma \\omega R^4$",
        "solution": "**1. Elementary Circular Current:**\nA ring of radius $r$ and width $dr$ carries charge $dq = 2\\pi \\sigma r \\, dr$.\nThe rotation at frequency $f = \\frac{\\omega}{2\\pi}$ creates current:\n$$dI = \\frac{\\omega}{2\\pi} dq = \\sigma \\omega r \\, dr$$\n\n**2. Magnetic Field at the Centre (Part a):**\n$$B = \\int_0^R \\frac{\\mu_0 dI}{2r} = \\frac{\\mu_0 \\sigma \\omega}{2} \\int_0^R dr = \\frac{1}{2} \\mu_0 \\sigma \\omega R$$\n\n**3. Magnetic Moment (Part b):**\n$$p_m = \\int_0^R (\\pi r^2) dI = \\pi \\sigma \\omega \\int_0^R r^3 \\, dr = \\frac{1}{4} \\pi \\sigma \\omega R^4$$",
        "tags": ["rotating charged disc", "convection current", "magnetic moment", "centre field"]
    },
    {
        "id": "3.247",
        "title": "Magnetic Field at Centre of Rotating Charged Sphere",
        "difficulty": 2,
        "question": "A non-conducting sphere of radius $R = 50\\text{ mm}$ charged uniformly with surface density $\\sigma = 10.0\\,\\mu\\text{C/m}^2$ rotates with angular velocity $\\omega = 70\\text{ rad/s}$ about a central axis. Find the magnetic induction at the centre of the sphere.",
        "hints": [
            "Divide the spherical surface into rings of colatitude $\\theta$ and angular width $d\\theta$.",
            "Radius of ring is $r = R \\sin\\theta$, width is $R d\\theta$, area is $2\\pi R^2 \\sin\\theta d\\theta$.",
            "Circulating current: $dI = \\frac{\\omega}{2\\pi} dq = \\sigma \\omega R^2 \\sin\\theta d\\theta$.",
            "Field at centre from ring: $dB = \\frac{\\mu_0 dI (R \\sin\\theta)^2}{2 R^3} = \\frac{1}{2} \\mu_0 \\sigma \\omega R \\sin^3\\theta d\\theta$. Integrate over $\\theta \\in [0, \\pi]$."
        ],
        "answer": "$B = \\frac{2}{3} \\mu_0 \\sigma \\omega R = 29\\text{ pT}$",
        "solution": "**1. Elementary Surface Ring:**\nA zonal band between $\\theta$ and $\\theta + d\\theta$ has radius $r = R \\sin\\theta$, area $dA = 2\\pi R^2 \\sin\\theta d\\theta$, and carries current:\n$$dI = \\frac{\\omega}{2\\pi} \\sigma dA = \\sigma \\omega R^2 \\sin\\theta \\, d\\theta$$\n\n**2. Field at the Centre:**\nBy the Biot-Savart formula for a circular ring:\n$$dB = \\frac{\\mu_0 dI r^2}{2 R^3} = \\frac{\\mu_0 (\\sigma \\omega R^2 \\sin\\theta \\, d\\theta)(R^2 \\sin^2\\theta)}{2 R^3} = \\frac{1}{2} \\mu_0 \\sigma \\omega R \\sin^3\\theta \\, d\\theta$$\n\n**3. Integration:**\n$$B = \\frac{1}{2} \\mu_0 \\sigma \\omega R \\int_0^\\pi \\sin^3\\theta \\, d\\theta = \\frac{1}{2} \\mu_0 \\sigma \\omega R \\left[ \\frac{4}{3} \\right] = \\frac{2}{3} \\mu_0 \\sigma \\omega R$$\n\n**4. Numerical Evaluation:**\n$$B = \\frac{2}{3} (4\\pi \\times 10^{-7})(1.0 \\times 10^{-5})(70)(0.050) \\approx 2.9 \\times 10^{-11}\\text{ T} = 29\\text{ pT}$$",
        "tags": ["rotating charged sphere", "surface current", "centre magnetic field", "integration"]
    },
    {
        "id": "3.248",
        "title": "Magnetic Moment and Gyromagnetic Ratio of Rotating Charged Ball",
        "difficulty": 2,
        "question": "A charge $q$ is uniformly distributed over the volume of a ball of mass $m$ and radius $R$ rotating with angular velocity $\\omega$ about its diameter. Find its magnetic moment $p_m$ and the ratio $p_m / M$, where $M$ is the angular momentum.",
        "hints": [
            "Divide the sphere into concentric shells of radius $r$ carrying charge $dq = \\frac{3q r^2 dr}{R^3}$.",
            "Each spherical shell has magnetic moment $dp_m = \\frac{1}{3} dq \\, \\omega r^2$.",
            "Integrate to find $p_m = \\frac{1}{5} q R^2 \\omega$.",
            "Compare with angular momentum $M = \\frac{2}{5} m R^2 \\omega$ to find $p_m / M = \\frac{q}{2m}$."
        ],
        "answer": "$p_m = \\frac{1}{5} q R^2 \\omega$; $\\frac{p_m}{M} = \\frac{q}{2m}$",
        "solution": "**1. Gyromagnetic Ratio for Uniform Distribution:**\nFor any volume element $dV$ with uniform mass density $\\rho_m = \\frac{m}{V}$ and charge density $\\rho_q = \\frac{q}{V}$:\n$$\\frac{dq}{dm} = \\frac{q}{m} = \\text{const}$$\nThe elemental magnetic moment and angular momentum are:\n$$d\\mathbf{p}_m = \\frac{1}{2} \\int [\\mathbf{r} \\times \\mathbf{j}_q] dV = \\frac{1}{2} \\frac{q}{m} \\int [\\mathbf{r} \\times \\mathbf{j}_m] dV = \\frac{q}{2m} d\\mathbf{M}$$\nSince the ratio is constant for all volume elements:\n$$\\frac{p_m}{M} = \\frac{q}{2m}$$\n\n**2. Magnetic Moment:**\nThe moment of inertia of a solid sphere is $I = \\frac{2}{5} m R^2$, so the angular momentum is:\n$$M = \\frac{2}{5} m R^2 \\omega$$\nTherefore:\n$$p_m = \\frac{q}{2m} M = \\frac{q}{2m} \\left( \\frac{2}{5} m R^2 \\omega \\right) = \\frac{1}{5} q R^2 \\omega$$",
        "tags": ["gyromagnetic ratio", "rotating charged ball", "angular momentum", "magnetic moment"]
    },
    {
        "id": "3.249",
        "title": "Magnetic Field of Rotating Statically Polarized Cylinder",
        "difficulty": 2,
        "question": "A long dielectric cylinder of radius $R$ is statically polarized with $\\mathbf{P}(r) = \\alpha \\mathbf{r}$. The cylinder rotates about its axis with angular velocity $\\omega$. Find the magnetic induction $B$ at the centre/axis of the cylinder.",
        "hints": [
            "Find the bound volume charge density: $\\rho' = -\\nabla \\cdot \\mathbf{P} = -2\\alpha$.",
            "Find the bound surface charge density: $\\sigma' = P(R) = \\alpha R$.",
            "Rotation creates a volume current density $j(r) = \\rho' \\omega r = -2\\alpha \\omega r$ and a surface current sheet $i = \\sigma' \\omega R = \\alpha \\omega R^2$.",
            "Sum the axial magnetic fields from volume and surface currents."
        ],
        "answer": "$B = 0$",
        "solution": "**1. Bound Charges:**\nInside the cylinder with radial polarization $\\mathbf{P}(r) = \\alpha r \\hat{\\mathbf{r}}$:\n$$\\rho' = -\\nabla \\cdot \\mathbf{P} = -\\frac{1}{r} \\frac{d}{dr}(r \\cdot \\alpha r) = -2\\alpha$$\nOn the cylindrical boundary $r = R$:\n$$\\sigma' = P_r(R) = \\alpha R$$\n\n**2. Current Densities from Rotation:**\n- Volume current density: $j_\\theta(r) = \\rho' \\omega r = -2\\alpha \\omega r$\n- Surface current density: $i_\\theta = \\sigma' \\omega R = \\alpha \\omega R^2$\n\n**3. Resultant Magnetic Induction on the Axis:**\nBy Ampere's circuital law for a solenoid:\n- Volume current contributes: $B_{\\text{vol}} = \\mu_0 \\int_0^R j_\\theta(r) \\, dr = \\mu_0 \\int_0^R (-2\\alpha \\omega r) \\, dr = -\\mu_0 \\alpha \\omega R^2$\n- Surface current sheet contributes: $B_{\\text{surf}} = \\mu_0 i_\\theta = \\mu_0 \\alpha \\omega R^2$\n\n$$B = B_{\\text{vol}} + B_{\\text{surf}} = -\\mu_0 \\alpha \\omega R^2 + \\mu_0 \\alpha \\omega R^2 = 0$$",
        "tags": ["polarized rotating cylinder", "bound current", "cancellation", "solenoid field"]
    },
    {
        "id": "3.250",
        "title": "Ratio of Magnetic to Electric Force Between Moving Charges",
        "difficulty": 1,
        "question": "Two protons move parallel to each other with equal velocity $v = 300\\text{ km/s}$. Find the ratio of the magnetic to electrical interaction forces between the protons.",
        "hints": [
            "Coulomb repulsion: $F_e = \\frac{e^2}{4\\pi\\varepsilon_0 r^2}$.",
            "Magnetic attraction: $F_m = \\frac{\\mu_0 e^2 v^2}{4\\pi r^2}$.",
            "Ratio is $\\frac{F_m}{F_e} = \\varepsilon_0 \\mu_0 v^2 = \\frac{v^2}{c^2}$."
        ],
        "answer": "$\\frac{F_m}{F_e} = \\frac{v^2}{c^2} = 1.00 \\times 10^{-6}$",
        "solution": "**1. Interaction Forces:**\nFor two charges $e$ moving with parallel velocity $v$ separated by distance $r$:\n- Electrostatic repulsion: $F_e = \\frac{1}{4\\pi\\varepsilon_0} \\frac{e^2}{r^2}$\n- Magnetic Lorentz attraction: $F_m = e v B = e v \\left( \\frac{\\mu_0 e v}{4\\pi r^2} \\right) = \\frac{\\mu_0}{4\\pi} \\frac{e^2 v^2}{r^2}$\n\n**2. Force Ratio:**\n$$\\frac{F_m}{F_e} = \\varepsilon_0 \\mu_0 v^2 = \\frac{v^2}{c^2}$$\n\n**3. Numerical Evaluation:**\nWith $v = 300\\text{ km/s} = 3.0 \\times 10^5\\text{ m/s}$ and $c = 3.0 \\times 10^8\\text{ m/s}$:\n$$\\frac{F_m}{F_e} = \\left( \\frac{3.0 \\times 10^5}{3.0 \\times 10^8} \\right)^2 = (1.0 \\times 10^{-3})^2 = 1.00 \\times 10^{-6}$$",
        "tags": ["relativistic ratio", "Lorentz force", "Coulomb force", "moving charges"]
    },
    {
        "id": "3.251",
        "title": "Ampere Force on Bent Current-Carrying Wire",
        "difficulty": 2,
        "question": "Find the force per unit length acting on a thin wire carrying current $I = 8.0\\text{ A}$ at point $O$ if the wire is bent as shown in:\n(a) a semicircle of radius $R = 10\\text{ cm}$;\n(b) two parallel long wires separated by $l = 20\\text{ cm}$.",
        "hints": [
            "(a) Force per unit length: $F_1 = \\frac{\\mu_0 I^2}{4R} = 0.20\\text{ mN/m}$.",
            "(b) Force per unit length: $F_1 = \\frac{\\mu_0 I^2}{\\pi l} = 0.13\\text{ mN/m}$."
        ],
        "answer": "(a) $F_1 = \\frac{\\mu_0 I^2}{4R} = 0.20\\text{ mN/m}$; (b) $F_1 = \\frac{\\mu_0 I^2}{\\pi l} = 0.13\\text{ mN/m}$",
        "solution": "**(a) Curved Loop (Semicircle):**\n$$F_1 = \\frac{\\mu_0 I^2}{4R}$$\n$$F_1 = \\frac{(4\\pi \\times 10^{-7})(8.0)^2}{4(0.10)} = \\frac{2.56\\pi \\times 10^{-5}}{0.40} \\approx 0.20\\text{ mN/m}$$\n\n**(b) Parallel Long Wires:**\n$$F_1 = \\frac{\\mu_0 I^2}{\\pi l}$$\n$$F_1 = \\frac{(4\\pi \\times 10^{-7})(8.0)^2}{\\pi (0.20)} = \\frac{2.56 \\times 10^{-5}}{0.20} \\approx 0.13\\text{ mN/m}$$",
        "tags": ["Ampere force", "force per unit length", "parallel wires", "numerical calculation"]
    },
    {
        "id": "3.252",
        "title": "Rupturing Magnetic Field of Current-Carrying Coil",
        "difficulty": 2,
        "question": "A coil carrying current $I = 10\\text{ mA}$ has single-layer winding of copper wire of diameter $d = 0.10\\text{ mm}$ and turn radius $R = 30\\text{ mm}$, placed in an axial external magnetic field $B$. At what value of $B$ will the winding rupture if copper tensile strength is $\\sigma_m = 2.5 \\times 10^8\\text{ Pa}$?",
        "hints": [
            "The radial magnetic force per unit length on a turn is $f = I B$.",
            "This produces hoop tension in the wire: $T = f R = I B R$.",
            "The tensile stress is $\\sigma = \\frac{T}{\\pi d^2 / 4} = \\frac{4 I B R}{\\pi d^2}$.",
            "Set $\\sigma = \\sigma_m$ and solve for $B = \\frac{\\pi d^2 \\sigma_m}{4 I R}$."
        ],
        "answer": "$B = \\frac{\\pi d^2 \\sigma_m}{4 I R} = 8\\text{ kT}$",
        "solution": "**1. Hoop Tension in Circular Turn:**\nThe outward radial magnetic force on an arc $d\\theta$ of radius $R$ is $dF = I B (R d\\theta)$.\nEquating to hoop tension components: $2 T \\sin(d\\theta / 2) \\approx T d\\theta = I B R d\\theta$:\n$$T = I B R$$\n\n**2. Tensile Stress in the Wire:**\nFor a wire of circular cross-section of diameter $d$ ($A = \\pi d^2 / 4$):\n$$\\sigma = \\frac{T}{A} = \\frac{4 I B R}{\\pi d^2}$$\n\n**3. Rupturing Field:**\nRupture occurs when $\\sigma = \\sigma_m$:\n$$B = \\frac{\\pi d^2 \\sigma_m}{4 I R}$$\nWith $d = 1.0 \\times 10^{-4}\\text{ m}$, $\\sigma_m = 2.5 \\times 10^8\\text{ N/m}^2$, $I = 0.010\\text{ A}$, $R = 0.030\\text{ m}$:\n$$B = \\frac{\\pi (1.0 \\times 10^{-8})(2.5 \\times 10^8)}{4(0.010)(0.030)} = \\frac{2.5\\pi}{0.0012} \\approx 8.0 \\times 10^3\\text{ T} = 8\\text{ kT}$$",
        "tags": ["magnetic hoop stress", "rupture threshold", "tensile strength", "coil mechanics"]
    },
    {
        "id": "3.253",
        "title": "Magnetic Induction from Deflection of Suspended U-Frame",
        "difficulty": 2,
        "question": "A copper wire of cross-section $S = 2.5\\text{ mm}^2$ bent into three sides of a square can rotate about horizontal axis $OO'$. In a vertical magnetic field $B$, a current $I = 16\\text{ A}$ deflects the frame by $\\theta = 20^\\circ$. Find $B$ (copper density $\\rho = 8.9\\text{ g/cm}^3$).",
        "hints": [
            "Let the square side be $a$. The bottom horizontal wire carries current $I$ and experiences horizontal Ampere force $F = I a B$.",
            "Torque of Ampere force about $OO'$: $N_B = F a \\cos\\theta = I a^2 B \\cos\\theta$.",
            "Gravity torque of the three sides: $N_g = (2m_{\\text{side}} g \\frac{a}{2} + m_{\\text{side}} g a) \\sin\\theta = 2 m a g \\sin\\theta = 2 (\\rho S a) a g \\sin\\theta$.",
            "Equating torques: $B = \\frac{2\\rho g S}{I} \\tan\\theta$."
        ],
        "answer": "$B = \\frac{2\\rho g S}{I} \\tan\\theta = 10\\text{ mT}$",
        "solution": "**1. Torque of Ampere Force:**\nThe vertical side segments experience horizontal forces parallel to axis $OO'$ producing no torque.\nThe bottom horizontal segment of length $a$ experiences horizontal force $F = I a B$.\nIts torque about axis $OO'$ is:\n$$N_B = F \\cdot (a \\cos\\theta) = I a^2 B \\cos\\theta$$\n\n**2. Torque of Gravity:**\nEach side has mass $m = \\rho S a$.\n- Two vertical sides have centers of mass at distance $a/2$ from $OO'$, contributing $2 \\times (m g \\frac{a}{2} \\sin\\theta) = m g a \\sin\\theta$.\n- Bottom side has centre of mass at distance $a$, contributing $m g a \\sin\\theta$.\n$$N_g = 2 m g a \\sin\\theta = 2 (\\rho S a) g a \\sin\\theta = 2 \\rho g S a^2 \\sin\\theta$$\n\n**3. Equilibrium:**\nEquating $N_B = N_g$:\n$$I a^2 B \\cos\\theta = 2 \\rho g S a^2 \\sin\\theta \\implies B = \\frac{2\\rho g S}{I} \\tan\\theta$$\nWith $\\rho = 8.9 \\times 10^3\\text{ kg/m}^3$, $g = 9.8\\text{ m/s}^2$, $S = 2.5 \\times 10^{-6}\\text{ m}^2$, $I = 16\\text{ A}$, $\\theta = 20^\\circ$:\n$$B = \\frac{2(8.9 \\times 10^3)(9.8)(2.5 \\times 10^{-6})}{16} \\tan 20^\\circ \\approx 10\\text{ mT}$$",
        "tags": ["magnetic torque", "gravity balance", "deflection angle", "Ampere force"]
    },
    {
        "id": "3.254",
        "title": "Magnetic Field Measurement with Current Balance",
        "difficulty": 2,
        "question": "A small coil with $N = 200$ turns of area $S = 1.0\\text{ cm}^2$ is mounted on a balance arm of length $l = 30\\text{ cm}$. With current $I = 22\\text{ mA}$, balance equilibrium is restored by adding mass $\\Delta m = 60\\text{ mg}$. Find the magnetic induction $B$.",
        "hints": [
            "Magnetic dipole moment of the coil: $p_m = N I S$.",
            "The torque exerted by the magnetic field on the dipole is $N_B = p_m B = N I S B$.",
            "Equate to counterweight torque: $N I S B = \\Delta m g l \\implies B = \\frac{\\Delta m g l}{N I S}$."
        ],
        "answer": "$B = \\frac{\\Delta m g l}{N I S} = 0.40\\text{ T}$",
        "solution": "**1. Torque Balance Equation:**\nThe magnetic torque on the small coil is:\n$$\\tau_m = p_m B = N I S B$$\nThe mechanical restoring torque provided by counterweight $\\Delta m$ on arm $l$ is:\n$$\\tau_g = \\Delta m g l$$\n\n**2. Solving for Magnetic Induction:**\n$$N I S B = \\Delta m g l \\implies B = \\frac{\\Delta m g l}{N I S}$$\n\n**3. Numerical Evaluation:**\nGiven $\\Delta m = 60 \\times 10^{-6}\\text{ kg}$, $g = 9.8\\text{ m/s}^2$, $l = 0.30\\text{ m}$, $N = 200$, $I = 0.022\\text{ A}$, $S = 1.0 \\times 10^{-4}\\text{ m}^2$:\n$$B = \\frac{(6.0 \\times 10^{-5})(9.8)(0.30)}{200 \\times 0.022 \\times 1.0 \\times 10^{-4}} = \\frac{1.764 \\times 10^{-4}}{4.4 \\times 10^{-4}} = 0.40\\text{ T}$$",
        "tags": ["current balance", "magnetic torque", "magnetic dipole", "field measurement"]
    },
    {
        "id": "3.255",
        "title": "Ampere Force and Rotation Work on Square Frame Near Long Wire",
        "difficulty": 2,
        "question": "A square frame with side $a = 8.0\\text{ cm}$ carrying current $I = 0.90\\text{ A}$ lies in the plane of a long straight wire carrying current $I_0 = 5.0\\text{ A}$ at distance $\\eta a = 1.5 a$ to its centre. Find:\n(a) the net Ampere force acting on the frame;\n(b) the mechanical work required to rotate the frame through $180^\\circ$ about its parallel axis.",
        "hints": [
            "(a) The two sides perpendicular to the wire experience forces that cancel each other. The near side is at $r_1 = \\eta a - a/2$, far side is at $r_2 = \\eta a + a/2$. Net force is $F = \\frac{\\mu_0 I_0 I a}{2\\pi} \\left( \\frac{1}{r_1} - \\frac{1}{r_2} \\right)$.",
            "(b) Work done to flip the frame: $A = 2 I \\Phi = \\frac{\\mu_0 I_0 I a}{\\pi} \\ln\\left(\\frac{\\eta + 0.5}{\\eta - 0.5}\\right)$."
        ],
        "answer": "(a) $F = \\frac{\\mu_0 I_0 I}{2\\pi (\\eta^2 - 1/4)} = 0.40\\,\\mu\\text{N}$; (b) $A = \\frac{\\mu_0 I_0 I a}{\\pi} \\ln\\left(\\frac{\\eta + 0.5}{\\eta - 0.5}\\right) = 0.10\\,\\mu\\text{J}$",
        "solution": "**(a) Net Ampere Force:**\nDistances to near and far sides:\n$$r_1 = a(\\eta - 0.5), \\quad r_2 = a(\\eta + 0.5)$$\nForces on sides perpendicular to the straight wire cancel by symmetry.\n$$F = F_1 - F_2 = \\frac{\\mu_0 I_0 I a}{2\\pi} \\left( \\frac{1}{r_1} - \\frac{1}{r_2} \\right) = \\frac{\\mu_0 I_0 I a}{2\\pi} \\frac{a}{a^2(\\eta^2 - 0.25)} = \\frac{\\mu_0 I_0 I}{2\\pi (\\eta^2 - 0.25)}$$\nWith $\\eta = 1.5$ (so $\\eta^2 - 0.25 = 2.0$):\n$$F = \\frac{(4\\pi \\times 10^{-7})(5.0)(0.90)}{2\\pi \\times 2.0} = 4.5 \\times 10^{-7}\\text{ N} \\approx 0.40\\,\\mu\\text{N}$$\n\n**(b) Work of Rotation by $180^\\circ$:**\n$$\\Phi = \\int_{r_1}^{r_2} \\frac{\\mu_0 I_0}{2\\pi r} (a \\, dr) = \\frac{\\mu_0 I_0 a}{2\\pi} \\ln\\left( \\frac{\\eta + 0.5}{\\eta - 0.5} \\right)$$\n$$A = 2 I \\Phi = \\frac{\\mu_0 I_0 I a}{\\pi} \\ln\\left( \\frac{2.0}{1.0} \\right) = \\frac{(4\\pi \\times 10^{-7})(5.0)(0.90)(0.080)}{\\pi} \\ln 2 \\approx 0.10\\,\\mu\\text{J}$$",
        "tags": ["square frame", "Ampere force", "magnetic flux", "rotation work"]
    },
    {
        "id": "3.256",
        "title": "Zero Net Force Between Two Parallel Wires",
        "difficulty": 2,
        "question": "Two long parallel wires are connected at one end to resistor $R$ and at the other end to a DC source $V$. Separation between wire axes is $\\eta = 20$ times their radius $a$. At what value of $R$ does the resultant force of interaction between the wires vanish?",
        "hints": [
            "Magnetic force per unit length is attractive: $F_m = \\frac{\\mu_0 I^2}{2\\pi d}$.",
            "Electrostatic force per unit length is repulsive: $F_e = \\frac{\\lambda^2}{2\\pi\\varepsilon_0 d}$.",
            "Equate $F_m = F_e \\implies I = c \\lambda$. Express $V = \\frac{\\lambda}{\\pi\\varepsilon_0} \\ln\\eta$ and $I = V/R$ to find $R = \\frac{\\ln\\eta}{\\pi} \\sqrt{\\frac{\\mu_0}{\\varepsilon_0}}$."
        ],
        "answer": "$R \\approx \\frac{\\ln\\eta}{\\pi} \\sqrt{\\frac{\\mu_0}{\\varepsilon_0}} = 0.36\\text{ k}\\Omega$",
        "solution": "**1. Balance Between Magnetic and Electric Forces:**\nPer unit length, the electrostatic repulsive force and magnetic attractive force are:\n$$F_e = \\frac{\\lambda^2}{2\\pi\\varepsilon_0 d}, \\quad F_m = \\frac{\\mu_0 I^2}{2\\pi d}$$\nFor the net force to vanish ($F_e = F_m$):\n$$\\frac{\\lambda^2}{\\varepsilon_0} = \\mu_0 I^2 \\implies I = \\frac{\\lambda}{\\sqrt{\\varepsilon_0\\mu_0}} = c \\lambda$$\n\n**2. Potential Difference and Resistance:**\nThe voltage between the two wires of radius $a$ and separation $d = \\eta a$ is:\n$$V = \\frac{\\lambda}{\\pi\\varepsilon_0} \\ln\\eta$$\nOhm's law gives:\n$$R = \\frac{V}{I} = \\frac{\\frac{\\lambda}{\\pi\\varepsilon_0} \\ln\\eta}{c \\lambda} = \\frac{\\ln\\eta}{\\pi \\varepsilon_0 c} = \\frac{\\ln\\eta}{\\pi} \\sqrt{\\frac{\\mu_0}{\\varepsilon_0}}$$\n\n**3. Numerical Evaluation:**\nWith $\\sqrt{\\frac{\\mu_0}{\\varepsilon_0}} = 377\\,\\Omega$ and $\\eta = 20$:\n$$R = \\frac{\\ln 20}{\\pi} \\times 377 \\approx \\frac{2.996}{3.1416} \\times 377 \\approx 360\\,\\Omega = 0.36\\text{ k}\\Omega$$",
        "tags": ["force balance", "parallel transmission line", "wave impedance", "electrostatic and magnetic"]
    },
    {
        "id": "3.257",
        "title": "Interaction Force Between Half-Cylindrical Shell and Axial Wire",
        "difficulty": 2,
        "question": "A direct current $I$ flows in a long straight conductor shaped as a thin half-ring of radius $R$. The same current flows in the opposite direction along an axial wire. Find the magnetic interaction force per unit length between them.",
        "hints": [
            "From Problem 3.225, the magnetic field produced by the half-cylindrical current sheet at its axis is $B = \\frac{\\mu_0 I}{\\pi^2 R}$.",
            "By Newton's third law, the force per unit length on the axial wire is $F_1 = I B$.",
            "$F_1 = \\frac{\\mu_0 I^2}{\\pi^2 R}$."
        ],
        "answer": "$F_1 = \\frac{\\mu_0 I^2}{\\pi^2 R}$",
        "solution": "**1. Magnetic Field at the Axis:**\nFrom the solution of Problem 3.225, the half-cylindrical conductor carrying current $I$ creates at its axis $O$ a magnetic field of induction:\n$$B = \\frac{\\mu_0 I}{\\pi^2 R}$$\n\n**2. Force on Axial Wire:**\nThe axial wire carries current $I$ immersed in this field $B$. The Ampere force per unit length acting on the axial wire is:\n$$F_1 = I B = \\frac{\\mu_0 I^2}{\\pi^2 R}$$\nBy Newton's third law, the force on the half-cylindrical shell is equal in magnitude and opposite in direction.",
        "tags": ["Ampere force", "half-cylindrical shell", "axial conductor", "Newton third law"]
    },
    {
        "id": "3.258",
        "title": "Interaction Force Between Wire and Coplanar Strip",
        "difficulty": 2,
        "question": "Two long thin parallel conductors lie in the same plane: a straight wire carrying current $I_1$ and a flat strip of width $b$ carrying current $I_2$, separated by distance $a$. Find the magnetic interaction force per unit length.",
        "hints": [
            "Divide the strip into filaments of width $dx$ at distance $x$ from the wire ($a \\le x \\le a + b$).",
            "Current in filament: $dI_2 = I_2 \\frac{dx}{b}$.",
            "Force on filament: $dF_1 = \\frac{\\mu_0 I_1 dI_2}{2\\pi x} = \\frac{\\mu_0 I_1 I_2 dx}{2\\pi b x}$.",
            "Integrate $\\int_a^{a+b} \\frac{dx}{x} = \\ln\\left(1 + \\frac{b}{a}\\right)$."
        ],
        "answer": "$F_1 = \\frac{\\mu_0 I_1 I_2}{2\\pi b} \\ln\\left(1 + \\frac{b}{a}\\right)$",
        "solution": "**1. Elementary Current Filament:**\nThe current per unit width of the flat strip is $i = I_2 / b$.\nA filament of width $dx$ at distance $x$ from the straight wire carries current $dI = \\frac{I_2}{b} dx$.\n\n**2. Force Per Unit Length:**\nThe magnetic field produced by wire 1 at distance $x$ is $B_1(x) = \\frac{\\mu_0 I_1}{2\\pi x}$.\nThe Ampere force on the filament per unit length is:\n$$dF_1 = B_1(x) dI = \\frac{\\mu_0 I_1 I_2}{2\\pi b} \\frac{dx}{x}$$\n\n**3. Integrating Over the Strip:**\n$$F_1 = \\frac{\\mu_0 I_1 I_2}{2\\pi b} \\int_a^{a+b} \\frac{dx}{x} = \\frac{\\mu_0 I_1 I_2}{2\\pi b} \\ln\\left(\\frac{a + b}{a}\\right) = \\frac{\\mu_0 I_1 I_2}{2\\pi b} \\ln\\left(1 + \\frac{b}{a}\\right)$$",
        "tags": ["Ampere force", "coplanar strip", "logarithmic integration", "magnetic interaction"]
    },
    {
        "id": "3.259",
        "title": "Magnetic Pressure Between Two Current-Carrying Planes",
        "difficulty": 1,
        "question": "A system consists of two parallel planes carrying currents producing a uniform magnetic field $B$ between them and zero outside. Find the magnetic force per unit area of each plane.",
        "hints": [
            "The magnetic energy density between the planes is $w_m = \\frac{B^2}{2\\mu_0}$.",
            "By the virtual work principle, magnetic pressure equals the energy density: $p = w_m = \\frac{B^2}{2\\mu_0}$."
        ],
        "answer": "$F_1 = \\frac{B^2}{2\\mu_0}$",
        "solution": "**1. Magnetic Energy and Virtual Work:**\nThe magnetic field is $B$ between the planes and $0$ outside.\nThe magnetic energy per unit area for plane separation $x$ is:\n$$W_1 = \\frac{B^2}{2\\mu_0} x$$\n\n**2. Magnetic Force Per Unit Area:**\n$$F_1 = -\\frac{dW_1}{dx} = \\frac{B^2}{2\\mu_0}$$\nAlternatively, each plane carries surface current $i = B / \\mu_0$ experiencing the average field $B_{\\text{avg}} = B/2$, yielding force per unit area:\n$$F_1 = i B_{\\text{avg}} = \\left(\\frac{B}{\\mu_0}\\right) \\left(\\frac{B}{2}\\right) = \\frac{B^2}{2\\mu_0}$$",
        "tags": ["magnetic pressure", "current sheets", "virtual work", "magnetic energy density"]
    },
    {
        "id": "3.260",
        "title": "Magnetic Force on Plane with Unequal Surrounding Fields",
        "difficulty": 2,
        "question": "A conducting sheet carrying current is placed in an external magnetic field so that the magnetic inductions on its two sides are $B_1$ and $B_2$. Find the magnetic force per unit area acting on the plane.",
        "hints": [
            "Surface current density from boundary condition: $i = \\frac{|B_1 - B_2|}{\\mu_0}$ (or vector difference).",
            "The effective field acting on this surface current is the average of the fields on either side: $B_{\\text{avg}} = \\frac{B_1 + B_2}{2}$.",
            "Force per unit area is $F_1 = i B_{\\text{avg}} = \\frac{|B_1^2 - B_2^2|}{2\\mu_0}$."
        ],
        "answer": "$F_1 = \\frac{|B_1^2 - B_2^2|}{2\\mu_0}$",
        "solution": "**1. Surface Current Density:**\nBy Ampere's circuital law across the current sheet:\n$$B_1 - B_2 = \\mu_0 i \\implies i = \\frac{B_1 - B_2}{\\mu_0}$$\n\n**2. Effective Field and Force:**\nThe self-field of the sheet jumps by $\\pm \\mu_0 i / 2$. The external field driving the force is the average:\n$$B_{\\text{avg}} = \\frac{B_1 + B_2}{2}$$\nThe magnetic force per unit area is:\n$$F_1 = i B_{\\text{avg}} = \\left( \\frac{B_1 - B_2}{\\mu_0} \\right) \\left( \\frac{B_1 + B_2}{2} \\right) = \\frac{B_1^2 - B_2^2}{2\\mu_0}$$\nTaking the magnitude: $F_1 = \\frac{|B_1^2 - B_2^2|}{2\\mu_0}$.",
        "tags": ["magnetic pressure difference", "current sheet", "Maxwell stress", "boundary conditions"]
    },
    {
        "id": "3.261",
        "title": "Pressure Produced by Electromagnetic Pump",
        "difficulty": 1,
        "question": "In an electromagnetic pump transferring molten metal, a pipe section of width $a = 2.0\\text{ cm}$ is placed in a uniform magnetic field $B = 0.10\\text{ T}$. A transverse current $I = 100\\text{ A}$ flows across this section. Find the gauge pressure produced by the pump.",
        "hints": [
            "Ampere force on the fluid section: $F = I a B$ (or $F = I B a$).",
            "The cross-sectional area perpendicular to flow is $S = a b$, so pressure is $\\Delta p = F / S = \\frac{I B}{a}$."
        ],
        "answer": "$\\Delta p = \\frac{I B}{a} = 0.5\\text{ kPa}$",
        "solution": "**1. Pumping Force:**\nA current $I$ passing across distance $a$ perpendicular to magnetic field $B$ experiences an electromagnetic Ampere force:\n$$F = I B a$$\n\n**2. Pressure Output:**\nIf the fluid duct has cross-sectional area $A = a \\cdot h$, where $h$ is the pipe depth along $B$, and current flows along $a$:\n$$\\Delta p = \\frac{F}{A} = \\frac{I B a}{a h} = \\frac{I B}{h} \\implies \\Delta p = \\frac{I B}{a}$$\n\n**3. Numerical Evaluation:**\n$$\\Delta p = \\frac{(100\\text{ A})(0.10\\text{ T})}{0.020\\text{ m}} = \\frac{10}{0.020} = 500\\text{ Pa} = 0.50\\text{ kPa}$$",
        "tags": ["electromagnetic pump", "Ampere force", "MHD pressure", "numerical evaluation"]
    },
    {
        "id": "3.262",
        "title": "Magnetic Pinch Pressure in Thin-Walled Cylinder",
        "difficulty": 2,
        "question": "A current $I$ flows in a long thin-walled cylinder of radius $R$. What magnetic pressure do the walls of the cylinder experience?",
        "hints": [
            "Inside the cylinder, $B_{\\text{in}} = 0$. Outside the cylinder, $B_{\\text{out}} = \\frac{\\mu_0 I}{2\\pi R}$.",
            "The magnetic pressure pushing inward is $p = \\frac{B_{\\text{out}}^2}{2\\mu_0}$."
        ],
        "answer": "$p = \\frac{\\mu_0 I^2}{8\\pi^2 R^2}$",
        "solution": "**1. Magnetic Field Discontinuity:**\n- Inside the thin-walled cylinder: $B = 0$\n- Just outside the surface: $B = \\frac{\\mu_0 I}{2\\pi R}$\n\n**2. Magnetic Inward Pinch Pressure:**\nBy the Maxwell magnetic stress tensor across the boundary:\n$$p = \\frac{B^2}{2\\mu_0} = \\frac{1}{2\\mu_0} \\left( \\frac{\\mu_0 I}{2\\pi R} \\right)^2 = \\frac{\\mu_0 I^2}{8\\pi^2 R^2}$$\nThis pressure is directed radially inward (pinch effect).",
        "tags": ["magnetic pinch", "thin cylinder", "Maxwell stress", "magnetic pressure"]
    },
    {
        "id": "3.263",
        "title": "Magnetic Pressure on Solenoid Lateral Surface",
        "difficulty": 1,
        "question": "What pressure does the lateral surface of a long straight solenoid with $n$ turns per unit length experience when a current $I$ flows through it?",
        "hints": [
            "Inside the solenoid, the field is $B = \\mu_0 n I$. Outside, $B = 0$.",
            "Magnetic pressure acting outward on the winding is $p = \\frac{B^2}{2\\mu_0}$."
        ],
        "answer": "$p = \\frac{1}{2} \\mu_0 n^2 I^2$",
        "solution": "**1. Field Discontinuity Across Winding:**\n- Inside: $B = \\mu_0 n I$\n- Outside: $B = 0$\n\n**2. Magnetic Outward Pressure:**\nThe magnetic energy density inside is $w_m = \\frac{B^2}{2\\mu_0}$.\nBy the principle of virtual work, expanding the radius increases magnetic volume, exerting outward pressure:\n$$p = \\frac{B^2}{2\\mu_0} = \\frac{(\\mu_0 n I)^2}{2\\mu_0} = \\frac{1}{2} \\mu_0 n^2 I^2$$",
        "tags": ["solenoid pressure", "magnetic expansion", "Maxwell stress", "magnetic energy"]
    },
    {
        "id": "3.264",
        "title": "Limiting Current for Solenoid Winding Rupture",
        "difficulty": 2,
        "question": "A current $I$ flows in a long single-layer solenoid of radius $R$ and $n$ turns per unit length. Find the limiting current $I_{\\text{lim}}$ at which the winding ruptures if the tensile strength of the wire is $F_{\\text{lim}}$.",
        "hints": [
            "Outward magnetic pressure on the solenoid surface is $p = \\frac{1}{2} \\mu_0 n^2 I^2$.",
            "In length $\\Delta l = 1/n$ containing 1 turn, the outward force on a half-turn is $F = p (2R \\cdot \\Delta l) = p \\frac{2R}{n} = \\mu_0 n R I^2$.",
            "This force is held by two cross-sections of the turn: $2 T = F \\implies T = \\frac{1}{2} \\mu_0 n R I^2$.",
            "Set $T = F_{\\text{lim}}$ and solve for $I_{\\text{lim}}$."
        ],
        "answer": "$I_{\\text{lim}} = \\sqrt{\\frac{2 F_{\\text{lim}}}{\\mu_0 n R}}$",
        "solution": "**1. Hoop Tension in Solenoid Turns:**\nThe outward magnetic pressure on the solenoid walls is:\n$$p = \\frac{1}{2} \\mu_0 n^2 I^2$$\nConsider one turn occupying axial length $\\Delta l = 1/n$.\nThe outward bursting force on a semicircular half-turn is:\n$$F_{\\text{burst}} = p \\cdot (2R) \\cdot \\Delta l = \\left( \\frac{1}{2} \\mu_0 n^2 I^2 \\right) (2R) \\left(\\frac{1}{n}\\right) = \\mu_0 n R I^2$$\nThis force is balanced by tensile forces at the two cuts of the turn ($2 T = F_{\\text{burst}}$):\n$$T = \\frac{1}{2} \\mu_0 n R I^2$$\n\n**2. Limiting Current:**\nSetting $T = F_{\\text{lim}}$:\n$$F_{\\text{lim}} = \\frac{1}{2} \\mu_0 n R I_{\\text{lim}}^2 \\implies I_{\\text{lim}} = \\sqrt{\\frac{2 F_{\\text{lim}}}{\\mu_0 n R}}$$",
        "tags": ["solenoid rupture", "hoop tension", "limiting current", "magnetic pressure"]
    },
    {
        "id": "3.265",
        "title": "Power and Optimal Matching of MHD Generator",
        "difficulty": 2,
        "question": "A parallel-plate capacitor with plate area $S$ and gap $d$ is immersed in a stream of conducting liquid of resistivity $\\rho$ moving with velocity $v$ perpendicular to magnetic field $B$. An external load $R$ is connected across the plates. Find the power dissipated in $R$, the optimal load $R$ for maximum power, and this maximum power $P_{\\max}$.",
        "hints": [
            "Induced EMF in the moving liquid: $\\mathcal{E} = v B d$.",
            "Internal resistance of liquid between plates: $R_i = \\frac{\\rho d}{S}$.",
            "Power dissipated in load $R$: $P(R) = I^2 R = \\frac{(v B d)^2 R}{(R + \\rho d / S)^2}$.",
            "By maximum power transfer theorem, maximum occurs when $R = R_i = \\frac{\\rho d}{S}$, giving $P_{\\max} = \\frac{v^2 B^2 d S}{4\\rho}$."
        ],
        "answer": "$P = \\frac{v^2 B^2 d^2 R}{(R + \\rho d / S)^2}$; $P_{\\max} = \\frac{v^2 B^2 d S}{4\\rho}$ when $R = \\frac{\\rho d}{S}$",
        "solution": "**1. Induced EMF (Faraday / Lorentz):**\nThe charges in the fluid moving at velocity $v$ across magnetic field $B$ experience transverse Lorentz force $F = q v B$, producing an effective internal electric field $E^* = v B$.\nThe induced EMF across plate separation $d$ is:\n$$\\mathcal{E} = E^* d = v B d$$\n\n**2. Internal Resistance of the Generator:**\nThe resistance of the conducting liquid column of length $d$ and cross-section $S$ is:\n$$R_i = \\frac{\\rho d}{S}$$\n\n**3. Power in the External Load:**\n$$I = \\frac{\\mathcal{E}}{R + R_i} = \\frac{v B d}{R + \\frac{\\rho d}{S}}$$\n$$P = I^2 R = \\frac{v^2 B^2 d^2 R}{\\left( R + \\frac{\\rho d}{S} \\right)^2}$$\n\n**4. Maximum Power Matching:**\nBy the maximum power transfer theorem, $P(R)$ is maximized when the load resistance equals the internal resistance:\n$$R = R_i = \\frac{\\rho d}{S}$$\nThe maximum delivered power is:\n$$P_{\\max} = \\frac{\\mathcal{E}^2}{4 R_i} = \\frac{v^2 B^2 d^2}{4 \\left( \\frac{\\rho d}{S} \\right)} = \\frac{v^2 B^2 d S}{4\\rho}$$",
        "tags": ["MHD generator", "Lorentz force", "maximum power transfer", "internal resistance"]
    }
]
