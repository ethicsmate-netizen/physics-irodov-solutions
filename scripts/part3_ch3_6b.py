"""
part3_ch3_6b.py
Curated problems 3.311 to 3.330 (20 problems) of Irodov Chapter 3.6:
Electromagnetic Induction. Maxwell's Equations (Part B).
"""

CH3_6B_CURATED = [
    {
        "id": "3.311",
        "title": "Angular Velocity of Charged Ring in Increasing Magnetic Field",
        "difficulty": 2,
        "question": "A thin non-conducting ring of mass $m$ carrying a uniformly distributed charge $q$ can freely rotate about its axis. At the initial moment the ring was at rest and no magnetic field was present. Then a practically uniform magnetic field was switched on, which was perpendicular to the plane of the ring and increased with time according to a certain law $B(t)$. Find the angular velocity $\\omega$ of the ring as a function of the induction $B(t)$.",
        "hints": [
            "The time-varying magnetic field induces a vortex electric field whose circulation around a circle of radius $r$ is $\\oint \\mathbf{E} \\cdot d\\mathbf{r} = -\\frac{d\\Phi}{dt} = -\\pi r^2 \\frac{dB}{dt}$.",
            "This gives tangential field $E_\\theta = -\\frac{r}{2} \\frac{dB}{dt}$, exerting a torque $N_z = q r E_\\theta = -\\frac{1}{2} q r^2 \\frac{dB}{dt}$.",
            "Relate torque to angular acceleration using moment of inertia $J = m r^2$: $m r^2 \\frac{d\\omega}{dt} = -\\frac{1}{2} q r^2 \\frac{dB}{dt}$, showing $r$ cancels out."
        ],
        "answer": "$\\omega = -\\frac{q B(t)}{2m}$",
        "solution": "**1. Induced Vortex Electric Field:**\nBy Faraday's law of induction in axisymmetric geometry, the induced electric field along the circumference of the ring of radius $r$ satisfies:\n$$\\oint \\mathbf{E} \\cdot d\\mathbf{r} = E_\\theta (2\\pi r) = -\\frac{d\\Phi}{dt} = -\\pi r^2 \\frac{dB}{dt}$$\n$$E_\\theta = -\\frac{1}{2} r \\frac{dB}{dt}$$\n\n**2. Torque on the Ring:**\nThe total electric force on the uniformly distributed charge $q$ acts tangentially, producing a torque about the axis of rotation:\n$$N_z = r (q E_\\theta) = -\\frac{1}{2} q r^2 \\frac{dB}{dt}$$\n\n**3. Rotational Dynamics:**\nThe moment of inertia of the thin ring is $J = m r^2$.\nApplying the rotational equation of motion:\n$$J \\frac{d\\omega}{dt} = N_z \\implies m r^2 \\frac{d\\omega}{dt} = -\\frac{1}{2} q r^2 \\frac{dB}{dt}$$\nThe radius $r$ cancels completely:\n$$\\frac{d\\omega}{dt} = -\\frac{q}{2m} \\frac{dB}{dt}$$\nIntegrating from the initial state where $B(0) = 0$ and $\\omega(0) = 0$:\n$$\\omega(t) = -\\frac{q B(t)}{2m}$$",
        "tags": ["Betatron effect", "vortex electric field", "Faraday's law", "rotational dynamics"]
    },
    {
        "id": "3.312",
        "title": "Maximum Radial Force on Ring Inside Energized Solenoid",
        "difficulty": 3,
        "question": "A thin wire ring of radius $a$ and resistance $r$ is located inside a long solenoid so that their axes coincide. The length of the solenoid is equal to $l$, its cross-sectional radius is $b$, and its total number of turns is $N$. At a certain moment the solenoid was connected to a source of constant voltage $V$. The total resistance of the solenoid circuit is equal to $R$. Assuming the self-inductance of the ring to be negligible, find the maximum value of the radial force acting per unit length of the ring.",
        "hints": [
            "Current in the solenoid builds up as $I(t) = \\frac{V}{R}(1 - e^{-t/\\tau})$ with $\\tau = \\frac{L}{R}$ and $L = \\frac{\\mu_0 N^2 \\pi b^2}{l}$.",
            "The induced current in the ring is $I_{\\text{ring}} = \\frac{\\mathcal{E}_i}{r} = \\frac{\\pi a^2}{r} \\frac{dB}{dt} = \\frac{\\pi a^2}{r} \\left( \\frac{\\mu_0 N}{l} \\right) \\frac{dI}{dt}$.",
            "The radial force per unit length is $f_r(t) = I_{\\text{ring}}(t) B(t) \\propto I(t) \\frac{dI}{dt}$, which reaches its maximum when $e^{-t/\\tau} = \\frac{1}{2}$."
        ],
        "answer": "$f_{r,\\max} = \\frac{\\mu_0 a^2 V^2}{4 r R l b^2}$",
        "solution": "**1. Solenoid Current Transient:**\nThe inductance of a long solenoid of length $l$, radius $b$, and $N$ turns is:\n$$L = \\mu_0 \\frac{N^2}{l} \\pi b^2$$\nWhen connected to a source of voltage $V$ with circuit resistance $R$, the current rises according to:\n$$I(t) = \\frac{V}{R} \\left( 1 - e^{-t/\\tau} \\right), \\quad \\text{where } \\tau = \\frac{L}{R}$$\nThe rate of current change is:\n$$\\frac{dI}{dt} = \\frac{V}{L} e^{-t/\\tau}$$\n\n**2. Magnetic Field and Ring Current:**\nThe magnetic field inside the solenoid is:\n$$B(t) = \\mu_0 \\frac{N}{l} I(t)$$\nThe emf induced in the coaxial ring of radius $a$ is:\n$$\\mathcal{E}_i(t) = \\pi a^2 \\frac{dB}{dt} = \\pi a^2 \\left( \\mu_0 \\frac{N}{l} \\right) \\frac{dI}{dt}$$\nThe current in the ring (resistance $r$) is:\n$$I_{\\text{ring}}(t) = \\frac{\\mathcal{E}_i(t)}{r} = \\frac{\\pi a^2}{r} \\left( \\mu_0 \\frac{N}{l} \\right) \\frac{dI}{dt}$$\n\n**3. Radial Force per Unit Length:**\nThe radial magnetic force on an element $dl$ of the ring is $dF = I_{\\text{ring}} B \\, dl$.\nThus the force per unit length is:\n$$f_r(t) = I_{\\text{ring}}(t) B(t) = \\frac{\\pi a^2}{r} \\left( \\frac{\\mu_0 N}{l} \\right)^2 I(t) \\frac{dI}{dt}$$\nSubstituting $I(t)$ and $\\frac{dI}{dt}$:\n$$I(t) \\frac{dI}{dt} = \\frac{V^2}{R L} e^{-t/\\tau} (1 - e^{-t/\\tau})$$\nSetting $u = e^{-t/\\tau}$, the product $u(1 - u)$ reaches its maximum value of $\\frac{1}{4}$ at $u = \\frac{1}{2}$:\n$$\\left[ I(t) \\frac{dI}{dt} \\right]_{\\max} = \\frac{V^2}{4 R L}$$\n\n**4. Maximum Radial Force:**\n$$f_{r,\\max} = \\frac{\\pi a^2}{r} \\left( \\frac{\\mu_0 N}{l} \\right)^2 \\frac{V^2}{4 R L} = \\frac{\\pi a^2}{r} \\frac{\\mu_0^2 N^2}{l^2} \\frac{V^2}{4 R \\left( \\mu_0 \\frac{N^2}{l} \\pi b^2 \\right)} = \\frac{\\mu_0 a^2 V^2}{4 r R l b^2}$$",
        "tags": ["solenoid inductance", "transient current", "radial force", "Faraday's law"]
    },
    {
        "id": "3.313",
        "title": "Heat Dissipated by Parabolic Flux Variation",
        "difficulty": 2,
        "question": "The magnetic flux through a stationary loop with resistance $R$ varies during the time interval $\\tau$ as $\\Phi(t) = a t (\\tau - t)$. Find the amount of heat generated in the loop during that time. The inductance of the loop is to be neglected.",
        "hints": [
            "The induced emf is $\\mathcal{E}_i(t) = -\\frac{d\\Phi}{dt} = -a(\\tau - 2t)$.",
            "The instantaneous Joule heat power is $P(t) = \\frac{\\mathcal{E}_i^2(t)}{R}$.",
            "Integrate $Q = \\int_0^\\tau \\frac{a^2 (\\tau - 2t)^2}{R} \\, dt$ to obtain $Q = \\frac{a^2 \\tau^3}{3R}$."
        ],
        "answer": "$Q = \\frac{a^2 \\tau^3}{3R}$",
        "solution": "**1. Induced Electromotive Force:**\nGiven magnetic flux $\\Phi(t) = a t (\\tau - t) = a \\tau t - a t^2$.\nBy Faraday's law:\n$$\\mathcal{E}_i(t) = -\\frac{d\\Phi}{dt} = -a (\\tau - 2t)$$\n\n**2. Joule Heat Generation:**\nThe rate of heat dissipation in the loop of resistance $R$ is:\n$$P(t) = \\frac{\\mathcal{E}_i^2(t)}{R} = \\frac{a^2}{R} (\\tau - 2t)^2$$\nIntegrating from $t = 0$ to $t = \\tau$:\n$$Q = \\int_0^\\tau P(t) \\, dt = \\frac{a^2}{R} \\int_0^\\tau (\\tau - 2t)^2 \\, dt$$\nUsing the substitution $u = \\tau - 2t$, $du = -2 \\, dt$:\n$$Q = \\frac{a^2}{R} \\left[ -\\frac{(\\tau - 2t)^3}{6} \\right]_0^\\tau = \\frac{a^2}{R} \\left( -\\frac{(-\\tau)^3}{6} + \\frac{\\tau^3}{6} \\right) = \\frac{a^2 \\tau^3}{3R}$$",
        "tags": ["Joule heating", "Faraday's law", "time-dependent flux", "definite integration"]
    },
    {
        "id": "3.314",
        "title": "Induced Current in Thick Conducting Ring Inside Solenoid",
        "difficulty": 2,
        "question": "In the middle of a long solenoid there is a coaxial ring of square cross-section, made of conducting material with resistivity $\\rho$. The thickness (axial height) of the ring is equal to $h$, and its inside and outside radii are equal to $a$ and $b$ respectively. Find the current induced in the ring if the magnetic induction produced by the solenoid varies with time as $B = \\beta t$, where $\\beta$ is a constant. Neglect the inductance of the ring.",
        "hints": [
            "Divide the ring into thin coaxial cylindrical shells of radius $r$, thickness $dr$, and height $h$.",
            "The emf around a shell of radius $r$ is $\\mathcal{E}(r) = \\pi r^2 \\frac{dB}{dt} = \\pi r^2 \\beta$.",
            "The resistance of this shell is $dR = \\rho \\frac{2\\pi r}{h \\, dr}$. Find $dI = \\frac{\\mathcal{E}(r)}{dR}$ and integrate from $a$ to $b$."
        ],
        "answer": "$I = \\frac{1}{4} \\frac{(b^2 - a^2) h \\beta}{\\rho}$",
        "solution": "**1. Elementary Current Shell:**\nConsider an elementary cylindrical shell inside the ring of radius $r$, radial thickness $dr$, and axial height $h$.\nThe magnetic flux enclosed by this circle is $\\Phi(r) = \\pi r^2 B(t)$.\nThe induced electromotive force along this circular loop is:\n$$\\mathcal{E}(r) = \\frac{d\\Phi}{dt} = \\pi r^2 \\beta$$\n\n**2. Resistance of the Elementary Shell:**\nThe length of the circular current path is $2\\pi r$ and the cross-sectional area through which this azimuthal current flows is $dA = h \\, dr$.\nThe electrical resistance of the shell is:\n$$dR = \\rho \\frac{2\\pi r}{h \\, dr}$$\n\n**3. Elementary and Total Induced Current:**\nThe current circulating in the shell is:\n$$dI = \\frac{\\mathcal{E}(r)}{dR} = \\frac{\\pi r^2 \\beta}{\\rho \\frac{2\\pi r}{h \\, dr}} = \\frac{\\beta h}{2\\rho} r \\, dr$$\nIntegrating across the full radial extent from $r = a$ to $r = b$:\n$$I = \\int_a^b dI = \\frac{\\beta h}{2\\rho} \\int_a^b r \\, dr = \\frac{\\beta h}{2\\rho} \\left[ \\frac{b^2 - a^2}{2} \\right] = \\frac{1}{4} \\frac{(b^2 - a^2) h \\beta}{\\rho}$$",
        "tags": ["Faraday's law", "eddy currents", "cylindrical shell integration", "solenoid"]
    },
    {
        "id": "3.315",
        "title": "Wire Length for Solenoid of Given Inductance",
        "difficulty": 2,
        "question": "How many metres of a thin wire are required to manufacture a solenoid of length $l_0 = 100\\text{ cm}$ and inductance $L = 1.0\\text{ mH}$ if the solenoid's cross-sectional diameter is considerably less than its length?",
        "hints": [
            "The inductance of a long solenoid is $L = \\mu_0 n^2 V = \\frac{\\mu_0 N^2 (\\pi r^2)}{l_0}$.",
            "The total length of the wound wire is $l = N (2\\pi r)$, so $r = \\frac{l}{2\\pi N}$ and the cross-sectional area is $\\pi r^2 = \\frac{l^2}{4\\pi N^2}$.",
            "Substitute into the inductance formula: $L = \\frac{\\mu_0 l^2}{4\\pi l_0}$ and solve for $l = \\sqrt{\\frac{4\\pi l_0 L}{\\mu_0}}$."
        ],
        "answer": "$l = \\sqrt{\\frac{4\\pi l_0 L}{\\mu_0}} = 100\\text{ m} = 0.10\\text{ km}$",
        "solution": "**1. Inductance Formula in Terms of Wire Length:**\nFor a long solenoid of length $l_0$, radius $r$, and $N$ turns, the inductance is:\n$$L = \\frac{\\mu_0 N^2 S}{l_0} = \\frac{\\mu_0 N^2 (\\pi r^2)}{l_0}$$\nThe total length $l$ of the wire wound into $N$ circular turns of radius $r$ is:\n$$l = N (2\\pi r) \\implies 2\\pi r = \\frac{l}{N}$$\nThe cross-sectional area can be rewritten as:\n$$S = \\pi r^2 = \\frac{(2\\pi r)^2}{4\\pi} = \\frac{l^2}{4\\pi N^2}$$\nSubstituting $S$ into the inductance expression:\n$$L = \\frac{\\mu_0 N^2}{l_0} \\left( \\frac{l^2}{4\\pi N^2} \\right) = \\frac{\\mu_0 l^2}{4\\pi l_0}$$\nNotice that the number of turns $N$ and radius $r$ cancel out completely!\n\n**2. Solving for Wire Length:**\n$$l = \\sqrt{\\frac{4\\pi l_0 L}{\\mu_0}}$$\nGiven $l_0 = 1.0\\text{ m}$, $L = 1.0 \\times 10^{-3}\\text{ H}$, $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ H/m}$:\n$$l = \\sqrt{\\frac{4\\pi (1.0)(1.0 \\times 10^{-3})}{4\\pi \\times 10^{-7}}} = \\sqrt{10^4} = 100\\text{ m} = 0.10\\text{ km}$$",
        "tags": ["solenoid inductance", "wire length", "magnetic flux", "geometry"]
    },
    {
        "id": "3.316",
        "title": "Inductance of Solenoid from Wire Mass and Resistance",
        "difficulty": 2,
        "question": "Find the inductance of a solenoid of length $l$ whose winding is made of copper wire of mass $m$. The winding resistance is equal to $R$. The solenoid diameter is considerably less than its length. (Resistivity $\\rho$, density $\\rho_0$).",
        "hints": [
            "Express the mass of the wire as $m = \\rho_0 l_w S_w$ and its resistance as $R = \\rho \\frac{l_w}{S_w}$.",
            "Eliminate the wire cross-section $S_w$ to find $l_w^2 = \\frac{m R}{\\rho \\rho_0}$.",
            "Use the solenoid relation from the previous problem $L = \\frac{\\mu_0 l_w^2}{4\\pi l}$ to express $L$ in terms of $m, R, \\rho, \\rho_0, l$."
        ],
        "answer": "$L = \\frac{\\mu_0 m R}{4\\pi \\rho \\rho_0 l}$",
        "solution": "**1. Length of Winding Wire:**\nLet the total wire length be $l_w$ and its cross-sectional area be $S_w$.\nThe mass of the wire is:\n$$m = \\rho_0 l_w S_w \\implies S_w = \\frac{m}{\\rho_0 l_w}$$\nThe electrical resistance of the wire is:\n$$R = \\rho \\frac{l_w}{S_w} = \\rho \\frac{l_w}{m / (\\rho_0 l_w)} = \\frac{\\rho \\rho_0 l_w^2}{m}$$\nSolving for $l_w^2$:\n$$l_w^2 = \\frac{m R}{\\rho \\rho_0}$$\n\n**2. Inductance of the Solenoid:**\nFrom the relation between solenoid inductance and total winding length (established in problem 3.315):\n$$L = \\frac{\\mu_0 l_w^2}{4\\pi l}$$\nSubstituting $l_w^2$:\n$$L = \\frac{\\mu_0 m R}{4\\pi \\rho \\rho_0 l}$$",
        "tags": ["solenoid inductance", "wire mass", "copper resistivity", "scaling relations"]
    },
    {
        "id": "3.317",
        "title": "Current Rise Time in an RL Circuit",
        "difficulty": 1,
        "question": "A coil of inductance $L = 300\\text{ mH}$ and resistance $R = 140\\text{ m}\\Omega$ is connected to a constant voltage source. How soon will the coil current reach $\\eta = 50\\%$ of the steady-state value?",
        "hints": [
            "In an RL circuit connected to a constant voltage source, current rises as $I(t) = I_0(1 - e^{-t/\\tau})$ where $\\tau = \\frac{L}{R}$.",
            "Set $1 - e^{-t/\\tau} = \\eta \\implies e^{-t/\\tau} = 1 - \\eta$.",
            "Solve for time: $t = \\frac{L}{R} \\ln\\left( \\frac{1}{1 - \\eta} \\right)$."
        ],
        "answer": "$t = \\frac{L}{R} \\ln\\left( \\frac{1}{1 - \\eta} \\right) = 1.5\\text{ s}$",
        "solution": "**1. RL Transient Response:**\nWhen an inductor $L$ with series resistance $R$ is connected to a DC source $V$, the differential equation is:\n$$L \\frac{dI}{dt} + R I = V$$\nWith initial condition $I(0) = 0$, the solution is:\n$$I(t) = \\frac{V}{R} \\left( 1 - e^{-R t / L} \\right) = I_0 \\left( 1 - e^{-t/\\tau} \\right)$$\nwhere $\\tau = \\frac{L}{R}$ is the circuit inductive time constant.\n\n**2. Finding the Time $t$:**\nSetting $I(t) = \\eta I_0$:\n$$1 - e^{-t/\\tau} = \\eta \\implies e^{-t/\\tau} = 1 - \\eta \\implies t = \\tau \\ln\\left( \\frac{1}{1 - \\eta} \\right) = \\frac{L}{R} \\ln\\left( \\frac{1}{1 - \\eta} \\right)$$\n\n**3. Numerical Evaluation:**\nGiven $L = 0.300\\text{ H}$, $R = 0.140\\,\\Omega$, $\\eta = 0.50$:\n$$\\tau = \\frac{0.300}{0.140} \\approx 2.143\\text{ s}$$\n$$t = 2.143 \\ln(2) = 2.143 \\times 0.69315 \\approx 1.49\\text{ s} \\approx 1.5\\text{ s}$$",
        "tags": ["RL circuit", "time constant", "transient response", "exponential growth"]
    },
    {
        "id": "3.318",
        "title": "Time Constant of a Solenoid",
        "difficulty": 2,
        "question": "Calculate the time constant $\\tau$ of a straight solenoid of length $l = 1.0\\text{ m}$ having a single-layer winding of copper wire whose total mass is $m = 1.0\\text{ kg}$. The cross-sectional diameter of the solenoid is assumed to be considerably less than its length. (Copper density $\\rho_0 = 8.9 \\times 10^3\\text{ kg/m}^3$, resistivity $\\rho = 1.7 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}$).",
        "hints": [
            "The time constant is defined as $\\tau = \\frac{L}{R}$.",
            "Recall from problem 3.316 that $L = \\frac{\\mu_0 m R}{4\\pi \\rho \\rho_0 l}$.",
            "Dividing by $R$ gives $\\tau = \\frac{\\mu_0 m}{4\\pi \\rho \\rho_0 l}$. Evaluate numerically."
        ],
        "answer": "$\\tau = \\frac{\\mu_0 m}{4\\pi \\rho \\rho_0 l} = 0.66\\text{ ms}$",
        "solution": "**1. Expression for the Time Constant:**\nUsing the relation derived in problem 3.316:\n$$L = \\frac{\\mu_0 m R}{4\\pi \\rho \\rho_0 l}$$\nThe time constant $\\tau$ of the solenoid is defined as:\n$$\\tau = \\frac{L}{R} = \\frac{\\mu_0 m}{4\\pi \\rho \\rho_0 l}$$\n\n**2. Numerical Evaluation:**\nGiven $m = 1.0\\text{ kg}$, $l = 1.0\\text{ m}$, $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ H/m}$, $\\rho = 1.7 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}$, $\\rho_0 = 8.9 \\times 10^3\\text{ kg/m}^3$:\n$$\\tau = \\frac{(4\\pi \\times 10^{-7})(1.0)}{4\\pi (1.7 \\times 10^{-8})(8.9 \\times 10^3)(1.0)} = \\frac{10^{-7}}{1.513 \\times 10^{-4}} \\approx 6.6 \\times 10^{-4}\\text{ s} = 0.66\\text{ ms}$$",
        "tags": ["time constant", "solenoid", "inductance", "copper properties"]
    },
    {
        "id": "3.319",
        "title": "Inductance per Unit Length of Coaxial Cable",
        "difficulty": 2,
        "question": "Find the inductance of a unit length of a cable consisting of two thin-walled coaxial metallic cylinders if the radius of the outside cylinder is $\\eta = 3.6$ times that of the inside one. The permeability of the medium between the cylinders is equal to unity.",
        "hints": [
            "Between the cylinders ($a < r < b$), the magnetic field produced by current $I$ is $B(r) = \\frac{\\mu_0 I}{2\\pi r}$.",
            "The magnetic energy per unit length is $W_1 = \\int_a^b \\frac{B^2}{2\\mu_0} 2\\pi r \\, dr = \\frac{\\mu_0 I^2}{4\\pi} \\ln\\left(\\frac{b}{a}\\right)$.",
            "Equate to $W_1 = \\frac{1}{2} L_1 I^2$ to find $L_1 = \\frac{\\mu_0}{2\\pi} \\ln\\eta$."
        ],
        "answer": "$L_1 = \\frac{\\mu_0}{2\\pi} \\ln\\eta = 0.26\\,\\mu\\text{H/m}$",
        "solution": "**1. Magnetic Field Between Cylinders:**\nBy Ampère's circuital law, for $a < r < b$:\n$$B(r) = \\frac{\\mu_0 I}{2\\pi r}$$\nFor thin-walled cylinders, magnetic fields inside the inner cylinder and outside the outer cylinder are zero.\n\n**2. Magnetic Energy per Unit Length:**\nThe magnetic energy stored per unit length of the coaxial cable is:\n$$W_1 = \\int_a^b \\frac{B^2(r)}{2\\mu_0} (2\\pi r \\, dr) = \\frac{\\mu_0 I^2}{4\\pi} \\int_a^b \\frac{dr}{r} = \\frac{\\mu_0 I^2}{4\\pi} \\ln\\left( \\frac{b}{a} \\right)$$\nWith $\\eta = b/a$:\n$$W_1 = \\frac{\\mu_0 I^2}{4\\pi} \\ln\\eta$$\n\n**3. Inductance per Unit Length:**\nSince $W_1 = \\frac{1}{2} L_1 I^2$:\n$$L_1 = \\frac{\\mu_0}{2\\pi} \\ln\\eta$$\n\n**4. Numerical Evaluation:**\n$$\\mu_0 = 4\\pi \\times 10^{-7}\\text{ H/m}, \\quad \\eta = 3.6$$\n$$L_1 = \\frac{4\\pi \\times 10^{-7}}{2\\pi} \\ln(3.6) = 2 \\times 10^{-7} \\times 1.2809 \\approx 2.56 \\times 10^{-7}\\text{ H/m} \\approx 0.26\\,\\mu\\text{H/m}$$",
        "tags": ["coaxial cable", "inductance per unit length", "magnetic energy", "Ampere's law"]
    },
    {
        "id": "3.320",
        "title": "Inductance of Toroidal Solenoid with Square Cross-Section",
        "difficulty": 2,
        "question": "Calculate the inductance of a doughnut solenoid (toroid) whose inside radius is equal to $b$ and cross-section has the form of a square with side $a$. The solenoid winding consists of $N$ turns. The space inside the solenoid is filled with a uniform paramagnetic material having permeability $\\mu$.",
        "hints": [
            "At radius $r$ inside the toroid ($b \\le r \\le b+a$), Ampère's law gives $B(r) = \\frac{\\mu_0 \\mu N I}{2\\pi r}$.",
            "The magnetic flux through a single square turn of height $a$ is $\\Phi = \\int_b^{b+a} B(r) a \\, dr = \\frac{\\mu_0 \\mu N I a}{2\\pi} \\ln\\left(1 + \\frac{a}{b}\\right)$.",
            "The total flux linkage is $\\Psi = N \\Phi$, yielding inductance $L = \\frac{\\Psi}{I} = \\frac{\\mu_0 \\mu N^2 a}{2\\pi} \\ln\\left(1 + \\frac{a}{b}\\right)$."
        ],
        "answer": "$L = \\frac{\\mu_0 \\mu N^2 a}{2\\pi} \\ln\\left(1 + \\frac{a}{b}\\right)$",
        "solution": "**1. Magnetic Field Inside Toroid:**\nUsing Ampère's circuital law along a concentric circular path of radius $r$ ($b \\le r \\le b + a$):\n$$\\oint \\mathbf{B} \\cdot d\\mathbf{r} = B(r) \\cdot 2\\pi r = \\mu_0 \\mu N I \\implies B(r) = \\frac{\\mu_0 \\mu N I}{2\\pi r}$$\n\n**2. Magnetic Flux Through One Turn:**\nEach turn has square dimensions $a \\times a$ with radial width $a$ and vertical height $a$.\nThe flux through one turn is:\n$$\\Phi = \\int_b^{b+a} B(r) (a \\, dr) = \\frac{\\mu_0 \\mu N I a}{2\\pi} \\int_b^{b+a} \\frac{dr}{r} = \\frac{\\mu_0 \\mu N I a}{2\\pi} \\ln\\left( \\frac{b+a}{b} \\right) = \\frac{\\mu_0 \\mu N I a}{2\\pi} \\ln\\left( 1 + \\frac{a}{b} \\right)$$\n\n**3. Inductance:**\nThe total flux linkage of the $N$ turns is $\\Psi = N \\Phi$.\nTherefore, the inductance is:\n$$L = \\frac{\\Psi}{I} = \\frac{\\mu_0 \\mu N^2 a}{2\\pi} \\ln\\left( 1 + \\frac{a}{b} \\right)$$",
        "tags": ["toroidal coil", "inductance", "magnetic flux", "Ampere's law"]
    },
    {
        "id": "3.321",
        "title": "Inductance per Unit Length of Double Tape Line",
        "difficulty": 2,
        "question": "Calculate the inductance of a unit length of a double tape line if the parallel tapes are separated by a distance $h$ which is considerably less than their width $b$, namely $b/h = 50$.",
        "hints": [
            "With $b \\gg h$, edge effects can be neglected. The surface current density on each tape is $j = I/b$.",
            "The uniform magnetic field between the tapes is $B = \\mu_0 j = \\frac{\\mu_0 I}{b}$.",
            "The magnetic energy per unit length is $W_1 = \\frac{B^2}{2\\mu_0} (b h) = \\frac{\\mu_0 I^2 h}{2b}$, giving $L_1 = \\frac{\\mu_0 h}{b}$."
        ],
        "answer": "$L_1 = \\frac{\\mu_0 h}{b} = 25\\text{ nH/m}$",
        "solution": "**1. Magnetic Field Between the Tapes:**\nSince $b \\gg h$, the magnetic field between the parallel conductive tapes is approximately uniform, while outside the gap it vanishes.\nThe surface current density across the width $b$ is:\n$$j = \\frac{I}{b}$$\nBy Ampère's circuital law, the magnetic field in the gap is:\n$$B = \\mu_0 j = \\frac{\\mu_0 I}{b}$$\n\n**2. Inductance from Magnetic Flux or Energy:**\nThe magnetic flux per unit length through the gap of height $h$ is:\n$$\\Phi_1 = B \\cdot (h \\cdot 1) = \\frac{\\mu_0 I h}{b}$$\nThe inductance per unit length is:\n$$L_1 = \\frac{\\Phi_1}{I} = \\frac{\\mu_0 h}{b}$$\n\n**3. Numerical Evaluation:**\nGiven $b/h = 50$ and $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ H/m}$:\n$$L_1 = \\frac{4\\pi \\times 10^{-7}}{50} \\approx 2.51 \\times 10^{-8}\\text{ H/m} \\approx 25\\text{ nH/m}$$",
        "tags": ["transmission line", "inductance per unit length", "parallel tapes", "Ampere's law"]
    },
    {
        "id": "3.322",
        "title": "Inductance per Unit Length of Two-Wire Transmission Line",
        "difficulty": 2,
        "question": "Find the inductance of a unit length of a two-wire line if the radius of each wire is $\\eta$ times less than the distance between the axes of the wires. Neglect the internal magnetic field inside the wires, assume permeability $\\mu = 1$ throughout, and $\\eta \\gg 1$.",
        "hints": [
            "Let wire radius be $r_0$ and axis separation be $d = \\eta r_0$.",
            "Between the wires, the magnetic field from current $+I$ and $-I$ is $B(x) = \\frac{\\mu_0 I}{2\\pi x} + \\frac{\\mu_0 I}{2\\pi(d - x)}$.",
            "Integrate from $x = r_0$ to $x = d - r_0$ to find the external flux per unit length $\\Phi_1 = \\frac{\\mu_0 I}{\\pi} \\ln\\left(\\frac{d - r_0}{r_0}\\right) \\approx \\frac{\\mu_0 I}{\\pi} \\ln\\eta$."
        ],
        "answer": "$L_1 \\approx \\frac{\\mu_0}{\\pi} \\ln\\eta$",
        "solution": "**1. Magnetic Field Between Two Parallel Wires:**\nLet the wire radius be $r_0$ and the center-to-center distance be $d = \\eta r_0$ with $\\eta \\gg 1$.\nAlong the line connecting the wire centres, the total magnetic field due to the forward and return currents is:\n$$B(x) = \\frac{\\mu_0 I}{2\\pi x} + \\frac{\\mu_0 I}{2\\pi (d - x)}$$\nwhere $x$ is measured from the axis of the first wire.\n\n**2. Magnetic Flux per Unit Length:**\nThe external magnetic flux passing between the surfaces of the two wires per unit length is:\n$$\\Phi_1 = \\int_{r_0}^{d - r_0} B(x) \\, dx = \\frac{\\mu_0 I}{2\\pi} \\left[ \\ln x - \\ln(d - x) \\right]_{r_0}^{d - r_0} = \\frac{\\mu_0 I}{\\pi} \\ln\\left( \\frac{d - r_0}{r_0} \\right)$$\nFor $\\eta = d/r_0 \\gg 1$:\n$$\\ln\\left( \\frac{d - r_0}{r_0} \\right) = \\ln(\\eta - 1) \\approx \\ln\\eta$$\n\n**3. Inductance per Unit Length:**\n$$L_1 = \\frac{\\Phi_1}{I} \\approx \\frac{\\mu_0}{\\pi} \\ln\\eta$$",
        "tags": ["two-wire line", "inductance per unit length", "transmission line", "magnetic flux"]
    },
    {
        "id": "3.323",
        "title": "Superconducting Ring Turned in Magnetic Field",
        "difficulty": 2,
        "question": "A superconducting round ring of radius $a$ and inductance $L$ was located in a uniform magnetic field of induction $B$. The ring plane was initially parallel to the vector $\\mathbf{B}$, and the current in the ring was equal to zero. Then the ring was turned through $90^\\circ$ so that its plane became perpendicular to the field. Find:\n(a) the current induced in the ring after the turn;\n(b) the work performed during the turn.",
        "hints": [
            "In a superconductor, electrical resistance is zero, so total magnetic flux through the closed loop is strictly conserved: $\\Phi_{\\text{total}} = \\text{const}$.",
            "Initially $\\Phi_{\\text{total}} = 0$. After turning, external flux is $\\Phi_{\\text{ext}} = \\pi a^2 B$, so $\\pi a^2 B + L I = 0 \\implies I = -\\frac{\\pi a^2 B}{L}$.",
            "The external mechanical work performed equals the increase in stored magnetic energy: $A = \\frac{1}{2} L I^2$."
        ],
        "answer": "(a) $I = \\frac{\\pi a^2 B}{L}$; (b) $A = \\frac{(\\pi a^2 B)^2}{2L}$",
        "solution": "**(a) Induced Current:**\nFor a superconducting loop, $R = 0$, so by Faraday's law:\n$$\\mathcal{E}_i = -\\frac{d\\Phi_{\\text{total}}}{dt} = 0 \\implies \\Phi_{\\text{total}} = \\Phi_{\\text{ext}} + L I = \\text{constant}$$\nInitially, the ring is parallel to $\\mathbf{B}$ and carries no current, so:\n$$\\Phi_{\\text{total}} = 0$$\nWhen rotated by $90^\\circ$, the external flux through the ring becomes $\\Phi_{\\text{ext}} = \\pi a^2 B$.\nBy flux conservation:\n$$\\pi a^2 B + L I = 0 \\implies I = -\\frac{\\pi a^2 B}{L}$$\nThe magnitude of the induced current is:\n$$I = \\frac{\\pi a^2 B}{L}$$\n\n**(b) Work Performed:**\nBecause no energy is dissipated in a superconductor ($R = 0$), the external mechanical work $A$ performed during the turn is entirely converted into the magnetic energy of the system:\n$$A = \\Delta W_m = \\frac{1}{2} L I^2 = \\frac{1}{2} L \\left( \\frac{\\pi a^2 B}{L} \\right)^2 = \\frac{(\\pi a^2 B)^2}{2L}$$",
        "tags": ["superconductivity", "flux conservation", "magnetic energy", "work in magnetic field"]
    },
    {
        "id": "3.324",
        "title": "Current in Stretched Superconducting Solenoid",
        "difficulty": 2,
        "question": "A current $I_0 = 1.9\\text{ A}$ flows in a long closed solenoid. The wire it is wound of is in a superconducting state. Find the current flowing in the solenoid when the length of the solenoid is increased by $\\eta = 5\\%$.",
        "hints": [
            "In a superconducting solenoid, total magnetic flux linkage $\\Psi$ is conserved.",
            "The flux linkage is $\\Psi = N \\Phi = N (B S) = N \\left( \\mu_0 \\frac{N}{l} I S \\right) = \\frac{\\mu_0 N^2 S}{l} I$.",
            "Since $N$ and $S$ remain constant while length increases to $l' = l(1 + \\eta)$, conservation of $\\Psi$ requires $\\frac{I'}{l'} = \\frac{I_0}{l}$."
        ],
        "answer": "$I = I_0 (1 + \\eta) = 2.0\\text{ A}$",
        "solution": "**1. Flux Linkage Conservation in Superconducting Solenoid:**\nBecause the solenoid wire is superconducting, resistance is zero, and the total magnetic flux linkage $\\Psi$ through the $N$ turns cannot change:\n$$\\Psi = \\text{constant}$$\n\n**2. Flux Linkage Expression:**\nFor a long solenoid of length $l$, cross-sectional area $S$, and total turns $N$, the magnetic field inside is:\n$$B = \\mu_0 \\frac{N}{l} I$$\nThe total flux linkage is:\n$$\\Psi = N B S = \\frac{\\mu_0 N^2 S}{l} I$$\nSince the number of turns $N$ and cross-section $S$ do not change when the solenoid is stretched axially:\n$$\\frac{I}{l} = \\text{constant}$$\n\n**3. Current After Stretching:**\nWhen the length increases from $l$ to $l' = l(1 + \\eta)$:\n$$\\frac{I'}{l(1 + \\eta)} = \\frac{I_0}{l} \\implies I' = I_0 (1 + \\eta)$$\n\n**4. Numerical Evaluation:**\n$$I' = (1.9\\text{ A})(1 + 0.05) = 1.9 \\times 1.05 = 1.995\\text{ A} \\approx 2.0\\text{ A}$$",
        "tags": ["superconducting solenoid", "flux conservation", "stretching solenoid", "inductance"]
    },
    {
        "id": "3.325",
        "title": "Persistent Current in Cooled Superconducting Ring",
        "difficulty": 2,
        "question": "A ring of radius $a = 50\\text{ mm}$ made of thin wire of radius $b = 1.0\\text{ mm}$ was located in a uniform magnetic field with induction $B = 0.50\\text{ mT}$ so that the ring plane was perpendicular to $\\mathbf{B}$. Then the ring was cooled down to a superconducting state, and the magnetic field was switched off. Find the ring current after that. (The inductance of the thin ring is $L = \\mu_0 a \\left[ \\ln(8a/b) - 2 \\right]$).",
        "hints": [
            "At the transition to the superconducting state, the external magnetic flux through the ring is frozen in: $\\Phi_0 = \\pi a^2 B$.",
            "When the external field is removed, persistent current $I$ arises to maintain the trapped flux: $L I = \\Phi_0 = \\pi a^2 B$.",
            "Calculate $I = \\frac{\\pi a^2 B}{L} = \\frac{\\pi a B}{\\mu_0 [\\ln(8a/b) - 2]}$."
        ],
        "answer": "$I = \\frac{\\pi a B}{\\mu_0 \\left[ \\ln(8a/b) - 2 \\right]} \\approx 16\\text{ A}$",
        "solution": "**1. Trapped Magnetic Flux:**\nWhen the ring is cooled below its critical temperature in the magnetic field $B$, it transitions to the superconducting state without any screening currents initially, enclosing external flux:\n$$\\Phi_0 = \\pi a^2 B$$\n\n**2. Persistent Current Generation:**\nWhen the external field is turned off, the total flux through the superconducting ring must remain constant:\n$$\\Phi_{\\text{total}} = \\Phi_{\\text{ext}} + L I = \\Phi_0$$\nSince $\\Phi_{\\text{ext}} \\to 0$:\n$$L I = \\pi a^2 B \\implies I = \\frac{\\pi a^2 B}{L}$$\n\n**3. Expression and Calculation:**\nUsing the given formula for ring inductance $L = \\mu_0 a \\left[ \\ln(8a/b) - 2 \\right]$:\n$$I = \\frac{\\pi a^2 B}{\\mu_0 a \\left[ \\ln(8a/b) - 2 \\right]} = \\frac{\\pi a B}{\\mu_0 \\left[ \\ln(8a/b) - 2 \\right]}$$\nGiven $a = 5.0 \\times 10^{-2}\\text{ m}$, $b = 1.0 \\times 10^{-3}\\text{ m}$, $B = 5.0 \\times 10^{-4}\\text{ T}$:\n$$\\frac{8a}{b} = \\frac{8 \\times 50}{1.0} = 400$$\n$$\\ln(400) - 2 \\approx 5.991 - 2 = 3.991$$\n$$I = \\frac{\\pi (0.050)(5.0 \\times 10^{-4})}{(4\\pi \\times 10^{-7})(3.991)} = \\frac{2.5 \\times 10^{-5}}{4 \\times 10^{-7} \\times 3.991} = \\frac{25}{1.596} \\approx 15.7\\text{ A} \\approx 16\\text{ A}$$",
        "tags": ["persistent current", "superconducting ring", "trapped flux", "ring inductance"]
    },
    {
        "id": "3.326",
        "title": "Current Transient After Abrupt Inductance Decrease",
        "difficulty": 2,
        "question": "A closed circuit consists of a source of constant emf $\\mathcal{E}$ and a choke coil of inductance $L$ connected in series. The active resistance of the whole circuit is equal to $R$. At the moment $t = 0$ the choke coil inductance was decreased abruptly $\\eta$ times. Find the current in the circuit as a function of time $t$. (During a stepwise change of inductance the total magnetic flux linkage remains constant).",
        "hints": [
            "Before $t = 0$, the steady-state current is $I_0 = \\mathcal{E}/R$, with flux linkage $\\Psi_0 = L I_0$.",
            "At $t = 0^+$, inductance drops to $L' = L/\\eta$. Flux conservation $\\Psi(0^+) = \\Psi(0^-)$ gives $L' I(0^+) = L I_0 \\implies I(0^+) = \\eta I_0 = \\eta \\frac{\\mathcal{E}}{R}$.",
            "For $t > 0$, the circuit evolves as $L' \\frac{dI}{dt} + R I = \\mathcal{E}$ with initial value $I(0^+) = \\eta \\frac{\\mathcal{E}}{R}$."
        ],
        "answer": "$I(t) = \\frac{\\mathcal{E}}{R} \\left[ 1 + (\\eta - 1) e^{-\\frac{\\eta R t}{L}} \\right]$",
        "solution": "**1. Initial State and Abrupt Transition:**\nPrior to $t = 0$, the steady-state current is:\n$$I_0 = \\frac{\\mathcal{E}}{R}$$\nThe magnetic flux linkage in the coil is $\\Psi(0^-) = L I_0 = \\frac{L \\mathcal{E}}{R}$.\nAt $t = 0$, the inductance changes instantaneously to $L' = L/\\eta$.\nBecause the flux linkage cannot change discontinuously during an instantaneous transition:\n$$\\Psi(0^+) = \\Psi(0^-) \\implies L' I(0^+) = L I_0 \\implies \\frac{L}{\\eta} I(0^+) = L I_0$$\n$$I(0^+) = \\eta I_0 = \\eta \\frac{\\mathcal{E}}{R}$$\n\n**2. Differential Equation for $t > 0$:**\nFor $t > 0$, the circuit equation with new inductance $L' = L/\\eta$ is:\n$$L' \\frac{dI}{dt} + R I = \\mathcal{E}$$\nThe general solution is:\n$$I(t) = \\frac{\\mathcal{E}}{R} + C e^{-R t / L'} = \\frac{\\mathcal{E}}{R} + C e^{-\\eta R t / L}$$\n\n**3. Applying Initial Condition:**\nAt $t = 0^+$:\n$$I(0^+) = \\frac{\\mathcal{E}}{R} + C = \\eta \\frac{\\mathcal{E}}{R} \\implies C = (\\eta - 1) \\frac{\\mathcal{E}}{R}$$\nThus the current as a function of time is:\n$$I(t) = \\frac{\\mathcal{E}}{R} \\left[ 1 + (\\eta - 1) e^{-\\frac{\\eta R t}{L}} \\right]$$",
        "tags": ["RL transient", "flux linkage conservation", "stepwise inductance change", "exponential decay"]
    },
    {
        "id": "3.327",
        "title": "Inductor Current Transient After Switch Closure",
        "difficulty": 2,
        "question": "Find the time dependence of the current flowing through the inductance $L$ of a bridge circuit after the switch $Sw$ is shorted at the moment $t = 0$. The circuit consists of source $\\mathcal{E}$, two resistors $R$ in parallel branches, and the inductor branch across the nodes.",
        "hints": [
            "Use Thévenin's theorem for the network connected across the inductor $L$.",
            "The open-circuit voltage across the inductor nodes is $V_{\\text{th}} = \\frac{\\mathcal{E}}{2}$, and the Thévenin equivalent resistance is $R_{\\text{th}} = \\frac{R}{2}$.",
            "The inductor current responds as $I(t) = \\frac{V_{\\text{th}}}{R_{\\text{th}}} (1 - e^{-t/\\tau})$ where $\\tau = \\frac{L}{R_{\\text{th}}} = \\frac{2L}{R}$."
        ],
        "answer": "$I(t) = \\frac{\\mathcal{E}}{R} \\left( 1 - e^{-\\frac{R t}{2L}} \\right)$",
        "solution": "**1. Thévenin Equivalent Circuit:**\nViewing the circuit from the terminals of the inductor $L$:\n- The open-circuit voltage across the inductor terminals (with $L$ disconnected) is:\n$$V_{\\text{th}} = \\frac{\\mathcal{E}}{2}$$\n- The equivalent resistance with the independent voltage source replaced by a short circuit is the parallel combination of the two resistances $R$:\n$$R_{\\text{th}} = \\frac{R \\cdot R}{R + R} = \\frac{R}{2}$$\n\n**2. Differential Equation for Inductor Current:**\nThe simplified equivalent circuit consists of source $V_{\\text{th}}$, resistor $R_{\\text{th}}$, and inductor $L$ in series:\n$$L \\frac{dI}{dt} + R_{\\text{th}} I = V_{\\text{th}}$$\n$$L \\frac{dI}{dt} + \\frac{R}{2} I = \\frac{\\mathcal{E}}{2}$$\n\n**3. Transient Solution:**\nWith initial condition $I(0) = 0$:\n$$I(t) = \\frac{V_{\\text{th}}}{R_{\\text{th}}} \\left( 1 - e^{-R_{\\text{th}} t / L} \\right) = \\frac{\\mathcal{E}/2}{R/2} \\left( 1 - e^{-\\frac{R t}{2L}} \\right) = \\frac{\\mathcal{E}}{R} \\left( 1 - e^{-\\frac{R t}{2L}} \\right)$$",
        "tags": ["Thevenin equivalent", "RL transient", "switch closing", "inductor current"]
    },
    {
        "id": "3.328",
        "title": "Steady-State Currents in Parallel Inductors",
        "difficulty": 2,
        "question": "In a circuit containing an emf $\\mathcal{E}$, a series resistance $R$, and two parallel lossless inductors $L_1$ and $L_2$, find the steady-state currents in the coils after the switch is closed. The source internal resistance and coil resistances are negligible.",
        "hints": [
            "Because the inductors are connected in parallel, the instantaneous voltage across them is identical: $V(t) = L_1 \\frac{dI_1}{dt} = L_2 \\frac{dI_2}{dt}$.",
            "Integrating from $t = 0$ (where $I_1(0) = I_2(0) = 0$) gives $L_1 I_1(t) = L_2 I_2(t)$.",
            "In steady state, the total current is $I_1 + I_2 = \\frac{\\mathcal{E}}{R}$. Combine with the flux relation to find $I_1$ and $I_2$."
        ],
        "answer": "$I_1 = \\frac{\\mathcal{E}}{R} \\frac{L_2}{L_1 + L_2}, \\quad I_2 = \\frac{\\mathcal{E}}{R} \\frac{L_1}{L_1 + L_2}$",
        "solution": "**1. Voltage Equality Across Parallel Inductors:**\nSince ideal coils $L_1$ and $L_2$ are connected in parallel, the potential difference across them is identical at every instant:\n$$V_L(t) = L_1 \\frac{dI_1}{dt} = L_2 \\frac{dI_2}{dt}$$\nIntegrating with respect to time from $t = 0$ where $I_1(0) = I_2(0) = 0$:\n$$L_1 I_1(t) = L_2 I_2(t) \\implies I_2(t) = \\frac{L_1}{L_2} I_1(t)$$\n\n**2. Steady-State Total Current:**\nIn the steady state ($t \\to \\infty$), the inductors act as short circuits (zero voltage drop across them), so the total current delivered by the source of emf $\\mathcal{E}$ through resistor $R$ is:\n$$I_{\\text{total}} = I_1 + I_2 = \\frac{\\mathcal{E}}{R}$$\n\n**3. Determining Individual Currents:**\nSubstituting $I_2 = \\frac{L_1}{L_2} I_1$ into the sum:\n$$I_1 \\left( 1 + \\frac{L_1}{L_2} \\right) = \\frac{\\mathcal{E}}{R} \\implies I_1 \\left( \\frac{L_1 + L_2}{L_2} \\right) = \\frac{\\mathcal{E}}{R}$$\n$$I_1 = \\frac{\\mathcal{E}}{R} \\frac{L_2}{L_1 + L_2}$$\nBy symmetry:\n$$I_2 = \\frac{\\mathcal{E}}{R} \\frac{L_1}{L_1 + L_2}$$",
        "tags": ["parallel inductors", "flux linkage", "current division", "steady state"]
    },
    {
        "id": "3.329",
        "title": "Mutual Inductance of Straight Wire and Rectangular Frame",
        "difficulty": 2,
        "question": "Calculate the mutual inductance of a long straight wire and a coplanar rectangular frame with sides $a$ and $b$. The side of length $b$ is closest to the wire, oriented parallel to it, and separated from it by a distance $l$.",
        "hints": [
            "The magnetic field produced by current $I$ in the long wire at distance $r$ is $B(r) = \\frac{\\mu_0 I}{2\\pi r}$.",
            "An element of area in the frame parallel to the wire is $dA = b \\, dr$, where $r$ varies from $l$ to $l + a$.",
            "Integrate $\\Phi = \\int_l^{l+a} B(r) b \\, dr$ and calculate $L_{12} = \\frac{\\Phi}{I}$."
        ],
        "answer": "$L_{12} = \\frac{\\mu_0 b}{2\\pi} \\ln\\left(1 + \\frac{a}{l}\\right)$",
        "solution": "**1. Magnetic Field of the Straight Wire:**\nWhen current $I$ flows through the long straight wire, the magnetic field at distance $r$ in the plane of the frame is:\n$$B(r) = \\frac{\\mu_0 I}{2\\pi r}$$\n\n**2. Magnetic Flux Through the Frame:**\nThe frame has length $b$ parallel to the wire and width $a$ perpendicular to the wire.\nThe distance from the wire to points within the frame ranges from $r = l$ to $r = l + a$.\nThe magnetic flux through an area strip $dA = b \\, dr$ is:\n$$\\Phi = \\int_l^{l+a} B(r) b \\, dr = \\frac{\\mu_0 I b}{2\\pi} \\int_l^{l+a} \\frac{dr}{r} = \\frac{\\mu_0 b I}{2\\pi} \\ln\\left( \\frac{l + a}{l} \\right) = \\frac{\\mu_0 b I}{2\\pi} \\ln\\left( 1 + \\frac{a}{l} \\right)$$\n\n**3. Mutual Inductance:**\nBy definition, the mutual inductance is:\n$$L_{12} = \\frac{\\Phi}{I} = \\frac{\\mu_0 b}{2\\pi} \\ln\\left( 1 + \\frac{a}{l} \\right)$$",
        "tags": ["mutual inductance", "Biot-Savart law", "rectangular frame", "magnetic flux"]
    },
    {
        "id": "3.330",
        "title": "Mutual Inductance of Toroid and Axial Straight Wire",
        "difficulty": 2,
        "question": "Determine the mutual inductance of a doughnut coil (toroid) and an infinite straight wire passing along its axis. The coil has a rectangular cross-section, inside radius $a$, outside radius $b$, axial height $h$, and $N$ turns. The system is located in a uniform medium with magnetic permeability $\\mu$.",
        "hints": [
            "Current $I$ along the axial wire produces a circular magnetic field $B(r) = \\frac{\\mu_0 \\mu I}{2\\pi r}$.",
            "The magnetic flux through a single rectangular turn of height $h$ and radial width $b - a$ is $\\Phi_1 = \\int_a^b B(r) h \\, dr = \\frac{\\mu_0 \\mu I h}{2\\pi} \\ln(b/a)$.",
            "The total flux linkage across all $N$ turns is $\\Psi = N \\Phi_1$. Divide by $I$ to find $L_{12}$."
        ],
        "answer": "$L_{12} = \\frac{\\mu_0 \\mu N h}{2\\pi} \\ln\\left(\\frac{b}{a}\\right)$",
        "solution": "**1. Magnetic Field Produced by Axial Current:**\nA current $I$ flowing along the infinite straight wire on the symmetry axis produces an azimuthal magnetic field:\n$$B(r) = \\frac{\\mu_0 \\mu I}{2\\pi r}$$\nThis field is everywhere perpendicular to the cross-sectional area of the toroidal coil turns.\n\n**2. Flux Linkage with the Toroid:**\nEach of the $N$ turns of the toroid has height $h$ parallel to the axis and spans from radius $a$ to $b$.\nThe magnetic flux through one turn is:\n$$\\Phi_1 = \\int_a^b B(r) (h \\, dr) = \\frac{\\mu_0 \\mu I h}{2\\pi} \\int_a^b \\frac{dr}{r} = \\frac{\\mu_0 \\mu I h}{2\\pi} \\ln\\left( \\frac{b}{a} \\right)$$\nThe total flux linked with all $N$ turns is:\n$$\\Psi = N \\Phi_1 = \\frac{\\mu_0 \\mu N I h}{2\\pi} \\ln\\left( \\frac{b}{a} \\right)$$\n\n**3. Mutual Inductance:**\nBy definition:\n$$L_{12} = \\frac{\\Psi}{I} = \\frac{\\mu_0 \\mu N h}{2\\pi} \\ln\\left( \\frac{b}{a} \\right)$$",
        "tags": ["mutual inductance", "toroidal coil", "axial wire", "magnetic flux linkage"]
    }
]
