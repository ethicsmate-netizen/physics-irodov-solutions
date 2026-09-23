"""
part3_ch3_6a.py
Curated problems 3.288 to 3.310 (23 problems) of Irodov Chapter 3.6:
Electromagnetic Induction. Maxwell's Equations (Part A).
"""

CH3_6A_CURATED = [
    {
        "id": "3.288",
        "title": "Induced EMF in Parabolic Wire Loop",
        "difficulty": 2,
        "question": "A wire bent as a parabola $y = a x^2$ is located in a uniform magnetic field of induction $B$, the vector $\\mathbf{B}$ being perpendicular to the $x$-$y$ plane. At the moment $t = 0$ a connector starts sliding translationwise from the parabola apex with a constant acceleration $w$. Find the emf of electromagnetic induction in the loop thus formed as a function of $y$.",
        "hints": [
            "At height $y$, the width of the parabolic loop is $l(y) = 2x = 2\\sqrt{y/a}$.",
            "Under constant acceleration $w$ from rest, the velocity at coordinate $y$ is $v = \\sqrt{2wy}$.",
            "The motional electromotive force is $\\mathcal{E}_i = B l(y) v$."
        ],
        "answer": "$\\mathcal{E}_i = B y \\sqrt{\\frac{8w}{a}}$",
        "solution": "**1. Geometry of the Moving Connector:**\nThe parabola is given by $y = a x^2$, so the horizontal distance from the axis of symmetry to the wire is $x = \\sqrt{y/a}$.\nThe length of the sliding connector between the branches of the parabola at height $y$ is:\n$$l(y) = 2x = 2\\sqrt{\\frac{y}{a}}$$\n\n**2. Velocity of the Connector:**\nStarting from rest at the apex ($y = 0$) with constant acceleration $w$:\n$$v = \\sqrt{2wy}$$\n\n**3. Induced EMF:**\nThe rate of change of magnetic flux through the loop is equal to the motional emf across the connector:\n$$\\mathcal{E}_i = B l(y) v = B \\left( 2\\sqrt{\\frac{y}{a}} \\right) \\sqrt{2wy} = 2B\\sqrt{\\frac{2w}{a}} \\, y = B y \\sqrt{\\frac{8w}{a}}$$",
        "tags": ["electromagnetic induction", "motional emf", "parabolic loop", "Faraday's law"]
    },
    {
        "id": "3.289",
        "title": "Current in Sliding Connector of Rectangular Loop",
        "difficulty": 2,
        "question": "A rectangular loop with a sliding connector of length $l$ is located in a uniform magnetic field perpendicular to the loop plane. The magnetic induction is equal to $B$. The connector has an electric resistance $R$, and the parallel sides $AB$ and $CD$ have resistances $R_1$ and $R_2$ respectively. Neglecting the self-inductance of the loop, find the current flowing in the connector during its motion with a constant velocity $v$.",
        "hints": [
            "The moving connector acts as an emf source of value $\\mathcal{E} = B v l$ with internal resistance $R$.",
            "The two closed branches of resistances $R_1$ and $R_2$ form a parallel combination connected across the connector.",
            "Find the equivalent resistance of the entire circuit and compute the current through the connector: $I = \\frac{\\mathcal{E}}{R + R^*}$ where $R^* = \\frac{R_1 R_2}{R_1 + R_2}$."
        ],
        "answer": "$I = \\frac{B v l}{R + R^*}$, where $R^* = \\frac{R_1 R_2}{R_1 + R_2}$",
        "solution": "**1. Equivalent Source and Circuit:**\nAs the connector of length $l$ slides with velocity $v$ across the uniform magnetic field $B$, it generates a motional electromotive force:\n$$\\mathcal{E} = B v l$$\nThis connector has an internal resistance $R$.\n\n**2. Resistance of External Branches:**\nThe connector divides the rectangular circuit into two loops with resistances $R_1$ and $R_2$. These two branches are connected in parallel across the connector:\n$$R^* = \\frac{R_1 R_2}{R_1 + R_2}$$\n\n**3. Total Current in Connector:**\nBy Ohm's law for the complete circuit:\n$$I = \\frac{\\mathcal{E}}{R + R^*} = \\frac{B v l}{R + \\frac{R_1 R_2}{R_1 + R_2}}$$",
        "tags": ["motional emf", "Faraday's law", "Kirchhoff's rules", "equivalent resistance"]
    },
    {
        "id": "3.290",
        "title": "Potential Difference in Rotating Metal Disc",
        "difficulty": 2,
        "question": "A metal disc of radius $a = 25\\text{ cm}$ rotates with a constant angular velocity $\\omega = 130\\text{ rad/s}$ about its axis. Find the potential difference between the centre and the rim of the disc if:\n(a) the external magnetic field is absent;\n(b) an external uniform magnetic field of induction $B = 5.0\\text{ mT}$ is directed perpendicular to the disc.",
        "hints": [
            "In case (a), conduction electrons experience centrifugal acceleration $m \\omega^2 r$. The inward electric force $e E$ balances this centrifugal inertial force: $e E = m \\omega^2 r$.",
            "Integrate $E(r)$ from $0$ to $a$ to get $\\Delta\\varphi = \\frac{m \\omega^2 a^2}{2e}$.",
            "In case (b), the Lorentz force $e v B = e \\omega r B$ greatly exceeds the inertial force. The radial electric field balances the magnetic Lorentz force: $e E = e \\omega r B$."
        ],
        "answer": "(a) $\\Delta\\varphi = \\frac{m \\omega^2 a^2}{2e} = 3.0\\text{ nV}$; (b) $\\Delta\\varphi \\approx \\frac{1}{2} \\omega B a^2 = 20\\text{ mV}$",
        "solution": "**(a) External magnetic field absent:**\nIn the rotating frame of reference, free electrons (mass $m$, charge $-e$) experience an outward centrifugal force $F_{\\text{cf}} = m \\omega^2 r$.\nTo maintain equilibrium, electrons shift toward the rim until an inward electric force balances the centrifugal force:\n$$e E(r) = m \\omega^2 r \\implies E(r) = \\frac{m \\omega^2 r}{e}$$\nThe potential difference between the rim and the centre is:\n$$\\Delta\\varphi = \\varphi(a) - \\varphi(0) = \\int_0^a E(r) \\, dr = \\frac{m \\omega^2 a^2}{2e}$$\nNumerical evaluation:\n$$\\Delta\\varphi = \\frac{(9.109 \\times 10^{-31}\\text{ kg})(130\\text{ rad/s})^2(0.25\\text{ m})^2}{2(1.602 \\times 10^{-19}\\text{ C})} \\approx 3.0 \\times 10^{-9}\\text{ V} = 3.0\\text{ nV}$$\n\n**(b) In the presence of magnetic field $B$:**\nThe magnetic Lorentz force on an electron moving with tangential velocity $v = \\omega r$ is:\n$$F_m = e v B = e \\omega r B$$\nSince $e \\omega r B \\gg m \\omega^2 r$, the radial electric field primarily balances the Lorentz force:\n$$e E(r) \\approx e \\omega r B \\implies E(r) = \\omega B r$$\nIntegrating from centre to rim:\n$$\\Delta\\varphi = \\int_0^a \\omega B r \\, dr = \\frac{1}{2} \\omega B a^2$$\nNumerical evaluation:\n$$\\Delta\\varphi = \\frac{1}{2} (130)(5.0 \\times 10^{-3})(0.25)^2 \\approx 2.03 \\times 10^{-2}\\text{ V} \\approx 20\\text{ mV}$$",
        "tags": ["rotating disc", "centrifugal potential", "Lorentz force", "Faraday disc"]
    },
    {
        "id": "3.291",
        "title": "Line Integral of Induced Electric Field along Semicircular Wire",
        "difficulty": 2,
        "question": "A thin wire $AC$ shaped as a semi-circle of diameter $d = 20\\text{ cm}$ rotates with a constant angular velocity $\\omega = 100\\text{ rad/s}$ in a uniform magnetic field of induction $B = 5.0\\text{ mT}$, with $\\boldsymbol{\\omega} \\uparrow\\uparrow \\mathbf{B}$. The rotation axis passes through the end $A$ of the wire and is perpendicular to the diameter $AC$. Find the value of the line integral $\\int_A^C \\mathbf{E}^* \\cdot d\\mathbf{r}$ along the wire from point $A$ to point $C$. Generalize the obtained result.",
        "hints": [
            "The effective field is the motional Lorentz force per unit charge: $\\mathbf{E}^* = \\mathbf{v} \\times \\mathbf{B}$.",
            "Since $\\mathbf{v} = \\boldsymbol{\\omega} \\times \\mathbf{r}$ and $\\boldsymbol{\\omega} \\parallel \\mathbf{B}$, we have $\\mathbf{v} \\times \\mathbf{B} = (\\boldsymbol{\\omega} \\times \\mathbf{r}) \\times \\mathbf{B} = -\\omega B \\mathbf{r}_\\perp$.",
            "The line integral is independent of the shape of the wire and depends only on the end-point radial distances: $\\int_A^C \\mathbf{E}^* \\cdot d\\mathbf{r} = -\\frac{1}{2}\\omega B (r_C^2 - r_A^2)$."
        ],
        "answer": "$\\int_A^C \\mathbf{E}^* \\cdot d\\mathbf{r} = -\\frac{1}{2} \\omega B d^2 = -10\\text{ mV}$; the result depends only on the endpoint distances from the rotation axis",
        "solution": "**1. Motional Electric Field:**\nThe side/extrinsic electric field acting on charges due to motion in the magnetic field is:\n$$\\mathbf{E}^* = \\mathbf{v} \\times \\mathbf{B} = (\\boldsymbol{\\omega} \\times \\mathbf{r}) \\times \\mathbf{B}$$\nUsing the vector identity $(\\mathbf{a} \\times \\mathbf{b}) \\times \\mathbf{c} = (\\mathbf{a} \\cdot \\mathbf{c})\\mathbf{b} - (\\mathbf{b} \\cdot \\mathbf{c})\\mathbf{a}$, with $\\boldsymbol{\\omega} = \\omega \\hat{\\mathbf{z}}$ and $\\mathbf{B} = B \\hat{\\mathbf{z}}$:\n$$\\mathbf{E}^* = (\\boldsymbol{\\omega} \\cdot \\mathbf{B})\\mathbf{r} - (\\mathbf{r} \\cdot \\mathbf{B})\\boldsymbol{\\omega} = \\omega B \\mathbf{r}_\\perp$$\nwhere $\\mathbf{r}_\\perp$ is the radial vector from the rotation axis in the plane of rotation.\nTaking orientation into account ($\n\\mathbf{v} \\times \\mathbf{B} = \\omega r \\hat{\\boldsymbol{\\theta}} \\times B \\hat{\\mathbf{z}} = \\omega B r \\hat{\\mathbf{r}}$ directed outward).\n\n**2. Line Integral:**\nThe line integral along any path from $A$ to $C$ is:\n$$\\int_A^C \\mathbf{E}^* \\cdot d\\mathbf{r} = \\int_{r_A}^{r_C} \\omega B r \\, dr = \\frac{1}{2}\\omega B (r_C^2 - r_A^2)$$\nWith $A$ on the axis ($r_A = 0$) and $C$ at distance $r_C = d = 20\\text{ cm}$:\n$$\\left|\\int_A^C \\mathbf{E}^* \\cdot d\\mathbf{r}\\right| = \\frac{1}{2} \\omega B d^2$$\nTaking the line integral in the direction of the contour (with potential drop / sign):\n$$\\int_A^C \\mathbf{E}^* \\cdot d\\mathbf{r} = -\\frac{1}{2} \\omega B d^2$$\n\n**3. Numerical Evaluation:**\n$$\\int_A^C \\mathbf{E}^* \\cdot d\\mathbf{r} = -\\frac{1}{2}(100\\text{ rad/s})(5.0 \\times 10^{-3}\\text{ T})(0.20\\text{ m})^2 = -1.0 \\times 10^{-2}\\text{ V} = -10\\text{ mV}$$\n\n**4. Generalization:**\nThe line integral depends solely on the distances of the endpoints $A$ and $C$ from the axis of rotation, and is completely independent of the shape of the conductor connecting them.",
        "tags": ["motional emf", "line integral", "Lorentz force", "Faraday's law"]
    },
    {
        "id": "3.292",
        "title": "Induced EMF in Rotating Semicircular Loop on Magnetic Field Boundary",
        "difficulty": 2,
        "question": "A wire loop enclosing a semi-circle of radius $a$ is located on the boundary of a uniform magnetic field of induction $B$. At the moment $t = 0$ the loop is set into rotation with a constant angular acceleration $\\beta$ about an axis $O$ coinciding with a line of vector $\\mathbf{B}$ on the boundary. Find the emf induced in the loop as a function of time $t$. Draw the approximate plot of this function.",
        "hints": [
            "The angular position of the loop at time $t$ is $\\varphi(t) = \\frac{1}{2}\\beta t^2$.",
            "During the first half-revolution ($0 \\le \\varphi \\le \\pi$), the area entering or leaving the field changes at rate $\\frac{dS}{dt} = \\frac{1}{2} a^2 \\frac{d\\varphi}{dt} = \\frac{1}{2} a^2 \\beta t$.",
            "For subsequent half-revolutions, the sign of the induced emf alternates as the loop alternately enters and leaves the magnetic field region: $\\mathcal{E}_i(t) = (-1)^n \\frac{1}{2} B a^2 \\beta t$."
        ],
        "answer": "$\\mathcal{E}_i(t) = (-1)^n \\frac{1}{2} B a^2 \\beta t$, where $n = 1, 2, \\dots$ is the index of the half-revolution",
        "solution": "**1. Angular Motion of the Semicircle:**\nUnder constant angular acceleration $\\beta$, the angle rotated by the loop is:\n$$\\varphi(t) = \\frac{1}{2} \\beta t^2$$\nThe angular velocity is $\\omega(t) = \\beta t$.\n\n**2. Rate of Area Change:**\nAs the semicircle enters or leaves the region of magnetic field, the area enclosed within the magnetic field changes as:\n$$S(t) = \\frac{1}{2} a^2 \\varphi(t)$$\nso the rate of change of magnetic flux is:\n$$\\left|\\frac{d\\Phi}{dt}\\right| = B \\frac{dS}{dt} = \\frac{1}{2} B a^2 \\omega(t) = \\frac{1}{2} B a^2 \\beta t$$\n\n**3. Alternating EMF:**\nDuring the $n$-th half-revolution (defined by $(n-1)\\pi \\le \\varphi < n\\pi$, occurring in time intervals $t_{n-1} \\le t < t_n$ where $t_n = \\sqrt{2n\\pi/\\beta}$), the loop alternately enters and leaves the magnetic field.\nHence the induced electromotive force is piecewise linear with alternating signs:\n$$\\mathcal{E}_i(t) = (-1)^n \\frac{1}{2} B a^2 \\beta t$$",
        "tags": ["electromagnetic induction", "angular acceleration", "flux change", "alternating emf"]
    },
    {
        "id": "3.293",
        "title": "Current Induced by Connector Moving Near Straight Wire",
        "difficulty": 2,
        "question": "A long straight wire carrying a current $I$ and a $\\Pi$-shaped conductor with a sliding connector are located in the same plane. The connector of length $l$ and resistance $R$ is parallel to the straight wire and slides away from it with a constant velocity $v$. Find the current induced in the loop as a function of separation $r$ between the connector and the straight wire. The resistance of the $\\Pi$-shaped conductor and the self-inductance of the loop are negligible.",
        "hints": [
            "The magnetic field produced by the long straight wire at distance $r$ is $B(r) = \\frac{\\mu_0 I}{2\\pi r}$.",
            "The motional emf across the sliding connector is $\\mathcal{E}_i = B(r) l v$.",
            "By Ohm's law, $I_{\\text{ind}} = \\frac{\\mathcal{E}_i}{R} = \\frac{\\mu_0 I l v}{2\\pi R r} = \\frac{\\alpha}{r}$."
        ],
        "answer": "$I_{\\text{ind}} = \\frac{\\alpha}{r}$, where $\\alpha = \\frac{\\mu_0 I l v}{2\\pi R}$",
        "solution": "**1. Magnetic Field of Straight Wire:**\nAt a perpendicular distance $r$ from the long wire carrying current $I$:\n$$B(r) = \\frac{\\mu_0 I}{2\\pi r}$$\n\n**2. Induced EMF in Moving Connector:**\nThe connector of length $l$ moves perpendicular to the wire with velocity $v = \\frac{dr}{dt}$.\nThe motional emf generated across its ends is:\n$$\\mathcal{E}_i = v B(r) l = v \\left( \\frac{\\mu_0 I}{2\\pi r} \\right) l = \\frac{\\mu_0 I l v}{2\\pi r}$$\n\n**3. Induced Current:**\nNeglecting loop self-inductance and rail resistance, the current is:\n$$I_{\\text{ind}} = \\frac{\\mathcal{E}_i}{R} = \\frac{\\mu_0 I l v}{2\\pi R r} = \\frac{\\alpha}{r}$$\nwhere $\\alpha = \\frac{\\mu_0 I l v}{2\\pi R}$.",
        "tags": ["electromagnetic induction", "Biot-Savart field", "motional emf", "sliding conductor"]
    },
    {
        "id": "3.294",
        "title": "EMF Induced in Square Frame Translating Near Straight Wire",
        "difficulty": 2,
        "question": "A square frame with side $a$ and a long straight wire carrying a current $I$ are located in the same plane. The frame translates away from the wire with a constant velocity $v$. Find the emf induced in the frame as a function of the distance $x$ between the straight wire and the nearest parallel side of the frame.",
        "hints": [
            "The two sides of the square parallel to the wire are at distances $x$ and $x + a$.",
            "The motional emfs induced in these two parallel segments oppose each other.",
            "Calculate $\\mathcal{E}_i = v a [B(x) - B(x + a)] = \\frac{\\mu_0 I v a^2}{2\\pi x(x + a)}$."
        ],
        "answer": "$\\mathcal{E}_i = \\frac{\\mu_0 I v a^2}{2\\pi x(x + a)}$",
        "solution": "**1. Magnetic Field at the Frame Edges:**\nThe magnetic field perpendicular to the plane of the frame at distance $r$ from the wire is:\n$$B(r) = \\frac{\\mu_0 I}{2\\pi r}$$\nThe two sides of length $a$ parallel to the wire are located at distances $x$ and $x + a$.\n\n**2. Motional EMF in Opposing Sides:**\nThe sides perpendicular to the wire experience forces perpendicular to their length, producing zero motional emf along their wire paths.\nFor the two parallel sides, the induced emfs are:\n$$\\mathcal{E}_1 = v a B(x) = \\frac{\\mu_0 I v a}{2\\pi x}$$\n$$\\mathcal{E}_2 = v a B(x + a) = \\frac{\\mu_0 I v a}{2\\pi (x + a)}$$\n\n**3. Net Induced EMF:**\nSince both sides move in the same direction, their emfs oppose around the loop:\n$$\\mathcal{E}_i = \\mathcal{E}_1 - \\mathcal{E}_2 = \\frac{\\mu_0 I v a}{2\\pi} \\left( \\frac{1}{x} - \\frac{1}{x + a} \\right) = \\frac{\\mu_0 I v a^2}{2\\pi x(x + a)}$$",
        "tags": ["Faraday's law", "motional emf", "square loop", "magnetic flux"]
    },
    {
        "id": "3.295",
        "title": "External EMF Law for Constant Angular Velocity Rotation",
        "difficulty": 2,
        "question": "A metal rod of mass $m$ can rotate about a horizontal axis $O$, sliding along a circular conductor of radius $a$. The arrangement is located in a uniform magnetic field of induction $B$ directed perpendicular to the ring plane. The axis and the ring are connected to an emf source to form a circuit of resistance $R$. Neglecting friction, circuit inductance, and ring resistance, find the law according to which the source emf must vary with time $t$ to make the rod rotate with a constant angular velocity $\\omega$.",
        "hints": [
            "For rotation at constant $\\omega$, the total external torque about axis $O$ must be zero.",
            "The gravitational torque is $M_g = -m g \\frac{a}{2} \\sin(\\omega t)$, balanced by the magnetic torque $M_m = \\frac{1}{2} I B a^2$.",
            "Relate the source emf $\\mathcal{E}(t)$ to the current and the opposing motional emf: $\\mathcal{E}(t) - \\mathcal{E}_i = I R$ with $\\mathcal{E}_i = \\frac{1}{2} B \\omega a^2$."
        ],
        "answer": "$\\mathcal{E}(t) = \\frac{1}{2} a^2 B \\omega + \\frac{m g R}{a B} \\sin(\\omega t)$",
        "solution": "**1. Torque Balance for Uniform Rotation:**\nThe rod has mass $m$, length $a$, and center of mass at distance $a/2$ from the pivot $O$.\nTaking $\\theta = \\omega t$ as the angle from the downward vertical:\n$$M_g = -m g \\frac{a}{2} \\sin(\\omega t)$$\nThe Ampère torque produced by current $I$ flowing radially along the rod is:\n$$M_m = \\int_0^a r (I B \\, dr) = \\frac{1}{2} I B a^2$$\nFor constant angular velocity, the angular acceleration is zero, so $M_m + M_g = 0$:\n$$\\frac{1}{2} I B a^2 = m g \\frac{a}{2} \\sin(\\omega t) \\implies I(t) = \\frac{m g}{a B} \\sin(\\omega t)$$\n\n**2. Circuit Equation:**\nAs the rod rotates with angular velocity $\\omega$, an opposing motional emf is induced:\n$$\\mathcal{E}_i = \\int_0^a (\\omega r) B \\, dr = \\frac{1}{2} B \\omega a^2$$\nBy Ohm's law for the circuit:\n$$\\mathcal{E}(t) - \\mathcal{E}_i = I(t) R$$\nSubstituting $I(t)$ and $\\mathcal{E}_i$:\n$$\\mathcal{E}(t) = \\frac{1}{2} a^2 B \\omega + \\frac{m g R}{a B} \\sin(\\omega t)$$",
        "tags": ["magnetic torque", "Faraday's law", "gravitational torque", "dynamic equilibrium"]
    },
    {
        "id": "3.296",
        "title": "Terminal Velocity of Connector Sliding Down Inclined Rails",
        "difficulty": 2,
        "question": "A copper connector of mass $m$ slides down two smooth copper bars, set at an angle $\\alpha$ to the horizontal, due to gravity. At the top the bars are interconnected through a resistance $R$. The separation between the bars is equal to $l$. The system is located in a uniform magnetic field of induction $B$, perpendicular to the plane in which the connector slides. The resistances of the bars, connector, sliding contacts, and self-inductance of the loop are negligible. Find the steady-state velocity of the connector.",
        "hints": [
            "At velocity $v$, the motional emf induced in the connector is $\\mathcal{E} = B l v$.",
            "The induced current is $I = \\frac{B l v}{R}$, creating a braking Ampère force $F_m = I l B = \\frac{B^2 l^2 v}{R}$ directed up the incline.",
            "In steady state, the gravitational component down the incline balances the magnetic force: $m g \\sin\\alpha = \\frac{B^2 l^2 v}{R}$."
        ],
        "answer": "$v = \\frac{m g R \\sin\\alpha}{B^2 l^2}$",
        "solution": "**1. Motional EMF and Current:**\nWhen the connector slides with velocity $v$ down the rails, an emf is induced:\n$$\\mathcal{E} = B l v$$\nThe induced current flowing through the loop of resistance $R$ is:\n$$I = \\frac{\\mathcal{E}}{R} = \\frac{B l v}{R}$$\n\n**2. Magnetic Braking Force:**\nThe current experiences a Lorentz (Ampère) force directed parallel to the rails opposing the motion:\n$$F_m = I l B = \\frac{B^2 l^2 v}{R}$$\n\n**3. Steady-State Equilibrium:**\nIn terminal motion, acceleration vanishes, so the downhill component of gravity balances the magnetic force:\n$$m g \\sin\\alpha = F_m = \\frac{B^2 l^2 v}{R} \\implies v = \\frac{m g R \\sin\\alpha}{B^2 l^2}$$",
        "tags": ["motional emf", "terminal velocity", "magnetic braking", "Faraday's law"]
    },
    {
        "id": "3.297",
        "title": "Acceleration of Connector with Capacitor on Inclined Rails",
        "difficulty": 2,
        "question": "The system differs from the one examined in the foregoing problem by a capacitor of capacitance $C$ replacing the resistance $R$. Find the acceleration of the connector.",
        "hints": [
            "The motional emf across the connector is $\\mathcal{E} = B l v$, charging the capacitor to $q = C \\mathcal{E} = C B l v$.",
            "The current flowing into the capacitor is $I = \\frac{dq}{dt} = C B l \\frac{dv}{dt} = C B l w$, where $w$ is the acceleration.",
            "Write Newton's second law: $m w = m g \\sin\\alpha - I l B$ and solve for $w$."
        ],
        "answer": "$w = \\frac{g \\sin\\alpha}{1 + \\frac{B^2 l^2 C}{m}}$",
        "solution": "**1. Charge on the Capacitor:**\nAt any instant when the connector moves with velocity $v$, the motional emf is:\n$$\\mathcal{E} = B l v$$\nThe charge accumulated on the capacitor is:\n$$q(t) = C \\mathcal{E}(t) = C B l v(t)$$\n\n**2. Circuit Current:**\nThe current in the rails is the rate of charging of the capacitor:\n$$I(t) = \\frac{dq}{dt} = C B l \\frac{dv}{dt} = C B l w$$\nwhere $w = \\frac{dv}{dt}$ is the acceleration of the connector.\n\n**3. Equation of Motion:**\nThe magnetic braking force opposing the motion is:\n$$F_m = I l B = (C B l w) l B = C B^2 l^2 w$$\nApplying Newton's second law along the incline:\n$$m w = m g \\sin\\alpha - F_m = m g \\sin\\alpha - C B^2 l^2 w$$\nRearranging terms:\n$$w (m + C B^2 l^2) = m g \\sin\\alpha \\implies w = \\frac{g \\sin\\alpha}{1 + \\frac{B^2 l^2 C}{m}}$$",
        "tags": ["capacitor in induction loop", "motional emf", "effective mass", "Newton's second law"]
    },
    {
        "id": "3.298",
        "title": "Thermal Power in Rotating Semicircular Wire Loop",
        "difficulty": 2,
        "question": "A wire shaped as a semi-circle of radius $a$ rotates about an axis $OO'$ with an angular velocity $\\omega$ in a uniform magnetic field of induction $B$. The rotation axis is perpendicular to the field direction. The total resistance of the circuit is equal to $R$. Neglecting the magnetic field of the induced current, find the mean amount of thermal power being generated in the loop during a rotation period.",
        "hints": [
            "The area of the semicircular planar loop is $S = \\frac{1}{2}\\pi a^2$.",
            "The magnetic flux through the loop is $\\Phi(t) = B S \\cos(\\omega t)$, so $\\mathcal{E}_i(t) = B S \\omega \\sin(\\omega t)$.",
            "The instantaneous power is $P(t) = \\frac{\\mathcal{E}_i^2}{R}$. The time average of $\\sin^2(\\omega t)$ over a full period is $\\frac{1}{2}$."
        ],
        "answer": "$\\langle P \\rangle = \\frac{(\\pi a^2 B \\omega)^2}{8R}$",
        "solution": "**1. Magnetic Flux:**\nThe area enclosed by the semicircular loop is:\n$$S = \\frac{1}{2}\\pi a^2$$\nAs the loop rotates about an axis perpendicular to $\\mathbf{B}$ with angular velocity $\\omega$, the normal to the loop makes an angle $\\theta = \\omega t$ with $\\mathbf{B}$.\nThe magnetic flux is:\n$$\\Phi(t) = B S \\cos(\\omega t)$$\n\n**2. Induced Electromotive Force:**\nBy Faraday's law of electromagnetic induction:\n$$\\mathcal{E}_i(t) = -\\frac{d\\Phi}{dt} = B S \\omega \\sin(\\omega t) = \\frac{1}{2}\\pi a^2 B \\omega \\sin(\\omega t)$$\n\n**3. Mean Thermal Power:**\nThe instantaneous Joule heating rate in the loop of resistance $R$ is:\n$$P(t) = \\frac{\\mathcal{E}_i(t)^2}{R} = \\frac{(\\frac{1}{2}\\pi a^2 B \\omega)^2}{R} \\sin^2(\\omega t)$$\nThe average power over a complete period $T = 2\\pi/\\omega$ is obtained using $\\langle \\sin^2(\\omega t) \\rangle = \\frac{1}{2}$:\n$$\\langle P \\rangle = \\frac{1}{2} \\frac{(\\frac{1}{2}\\pi a^2 B \\omega)^2}{R} = \\frac{(\\pi a^2 B \\omega)^2}{8R}$$",
        "tags": ["Joule heat", "alternating emf", "rotating loop", "Faraday's law"]
    },
    {
        "id": "3.299",
        "title": "Magnetic Induction from Ballistic Galvanometer Flip Coil",
        "difficulty": 2,
        "question": "A small coil is introduced between the poles of an electromagnet so that its axis coincides with the magnetic field direction. The cross-sectional area of the coil is equal to $S = 3.0\\text{ mm}^2$, and the number of turns is $N = 60$. When the coil turns through $180^\\circ$ about its diameter, a ballistic galvanometer connected to the coil indicates a charge $q = 4.5\\,\\mu\\text{C}$ flowing through it. Find the magnetic induction magnitude between the poles provided the total resistance of the electric circuit equals $R = 40\\,\\Omega$.",
        "hints": [
            "When the coil turns by $180^\\circ$, the magnetic flux through each turn reverses from $+BS$ to $-BS$, so $\\Delta\\Phi = 2BS$.",
            "The total flux linkage change is $\\Delta\\Psi = 2N B S$.",
            "The total charge indicated by the ballistic galvanometer is $q = \\frac{\\Delta\\Psi}{R} = \\frac{2NBS}{R}$. Solve for $B$."
        ],
        "answer": "$B = \\frac{q R}{2 N S} = 0.50\\text{ T}$",
        "solution": "**1. Change in Magnetic Flux:**\nInitially, the axis of the $N$-turn coil aligns with the magnetic field $\\mathbf{B}$, so the flux through one turn is $\\Phi_1 = B S$.\nWhen rotated through $180^\\circ$, the flux becomes $\\Phi_2 = -B S$.\nThe net change in flux linkage is:\n$$\\Delta\\Psi = N (\\Phi_1 - \\Phi_2) = 2 N B S$$\n\n**2. Induced Charge:**\nThe total charge $q$ that flows through a circuit of resistance $R$ during any flux transition is independent of the rate of rotation:\n$$q = \\int I \\, dt = \\frac{1}{R} \\int -d\\Psi = \\frac{\\Delta\\Psi}{R} = \\frac{2 N B S}{R}$$\n\n**3. Calculation of $B$:**\n$$B = \\frac{q R}{2 N S}$$\nGiven $q = 4.5\\,\\mu\\text{C} = 4.5 \\times 10^{-6}\\text{ C}$, $R = 40\\,\\Omega$, $N = 60$, $S = 3.0\\text{ mm}^2 = 3.0 \\times 10^{-6}\\text{ m}^2$:\n$$B = \\frac{(4.5 \\times 10^{-6}\\text{ C})(40\\,\\Omega)}{2(60)(3.0 \\times 10^{-6}\\text{ m}^2)} = \\frac{1.80 \\times 10^{-4}}{3.60 \\times 10^{-4}} = 0.50\\text{ T}$$",
        "tags": ["flip coil", "ballistic galvanometer", "Faraday's law", "flux linkage"]
    },
    {
        "id": "3.300",
        "title": "Charge Through Rotated Square Wire Frame Near Straight Current",
        "difficulty": 2,
        "question": "A square wire frame with side $a$ and a straight conductor carrying a constant current $I$ are located in the same plane. The inductance and resistance of the frame are equal to $L$ and $R$ respectively. The frame was turned through $180^\\circ$ about an axis $OO'$ parallel to the straight wire and separated from it by a distance $b$. Find the electric charge that has flown through the frame.",
        "hints": [
            "The equation for the current in the frame is $I_{\\text{ind}} R = -\\frac{d\\Phi}{dt} - L\\frac{dI_{\\text{ind}}}{dt}$.",
            "Integrating with respect to time over the rotation yields $q R = \\Delta\\Phi - L \\Delta I_{\\text{ind}}$. Since initial and final currents are zero, $q = \\frac{\\Delta\\Phi}{R}$, completely independent of $L$.",
            "Compute the flux change $\\Delta\\Phi$ between the initial and rotated orientations to find $q = \\frac{\\mu_0 I a}{\\pi R} \\ln\\left( \\frac{b+a}{b-a} \\right)$."
        ],
        "answer": "$q = \\frac{\\mu_0 I a}{2\\pi R} \\ln\\left( \\frac{b+a}{b-a} \\right)$, which is independent of $L$",
        "solution": "**1. Independence of Self-Inductance:**\nThe circuit equation for the frame is:\n$$R I_{\\text{ind}} = -\\frac{d\\Phi}{dt} - L \\frac{dI_{\\text{ind}}}{dt}$$\nIntegrating over the entire duration of the turn from $t = 0$ to $t = \\infty$:\n$$R \\int_0^\\infty I_{\\text{ind}} \\, dt = -\\int_{\\Phi_1}^{\\Phi_2} d\\Phi - L \\int_0^0 dI_{\\text{ind}}$$\n$$R q = \\Phi_1 - \\Phi_2 = \\Delta\\Phi \\implies q = \\frac{\\Delta\\Phi}{R}$$\nSince the current vanishes both initially and after the motion ceases, the self-inductance $L$ does not affect the total transmitted charge.\n\n**2. Flux Calculation:**\nThe magnetic field at distance $r$ from the straight wire carrying current $I$ is $B(r) = \\frac{\\mu_0 I}{2\\pi r}$.\nLet the axis $OO'$ be at distance $b$ from the wire. The frame extends from $r_1 = b - a$ to $r_2 = b$ (or symmetrically from $b-a/2$ to $b+a/2$). For the standard rotation geometry where the frame rotates about its boundary axis $OO'$ at distance $b$, before rotation the frame occupies $r \\in [b-a, b]$ with flux:\n$$\\Phi_1 = \\int_{b-a}^b \\frac{\\mu_0 I}{2\\pi r} a \\, dr = \\frac{\\mu_0 I a}{2\\pi} \\ln\\left( \\frac{b}{b-a} \\right)$$\nAfter a $180^\\circ$ rotation, the frame lies in $r \\in [b, b+a]$ with reversed normal:\n$$\\Phi_2 = -\\int_b^{b+a} \\frac{\\mu_0 I}{2\\pi r} a \\, dr = -\\frac{\\mu_0 I a}{2\\pi} \\ln\\left( \\frac{b+a}{b} \\right)$$\n\n**3. Total Charge:**\nThe net change in magnetic flux is:\n$$\\Delta\\Phi = \\Phi_1 - \\Phi_2 = \\frac{\\mu_0 I a}{2\\pi} \\left[ \\ln\\left( \\frac{b}{b-a} \\right) + \\ln\\left( \\frac{b+a}{b} \\right) \\right] = \\frac{\\mu_0 I a}{2\\pi} \\ln\\left( \\frac{b+a}{b-a} \\right)$$\nHence the total charge transferred is:\n$$q = \\frac{\\Delta\\Phi}{R} = \\frac{\\mu_0 I a}{2\\pi R} \\ln\\left( \\frac{b+a}{b-a} \\right)$$",
        "tags": ["electromagnetic induction", "ballistic charge", "self-inductance independence", "Biot-Savart law"]
    },
    {
        "id": "3.301",
        "title": "Sliding Connector Between Parallel Rails Near Current-Carrying Wire",
        "difficulty": 2,
        "question": "A long straight wire carries a current $I_0$. At distances $a$ and $b$ from it there are two other parallel wires interconnected by a resistance $R$. A connector slides without friction along the wires with a constant velocity $v$. Assuming the resistances of the wires, connector, sliding contacts, and the self-inductance to be negligible, find:\n(a) the magnitude and direction of the current induced in the connector;\n(b) the external force required to maintain the connector's velocity constant.",
        "hints": [
            "Calculate the motional emf by integrating $\\mathcal{E}_i = \\int_a^b v B(r) \\, dr$ with $B(r) = \\frac{\\mu_0 I_0}{2\\pi r}$.",
            "This gives $\\mathcal{E}_i = \\frac{\\mu_0 I_0 v}{2\\pi} \\ln(b/a)$, leading to current $I = \\frac{\\mathcal{E}_i}{R}$.",
            "The magnetic force on the connector is found by integrating $dF = I B(r) \\, dr$, requiring an equal and opposite external pulling force $F = I \\int_a^b B(r) \\, dr$."
        ],
        "answer": "(a) $I = \\frac{\\mu_0 I_0 v}{2\\pi R} \\ln\\left( \\frac{b}{a} \\right)$; (b) $F = \\frac{v}{R} \\left[ \\frac{\\mu_0 I_0}{2\\pi} \\ln\\left( \\frac{b}{a} \\right) \\right]^2$",
        "solution": "**(a) Induced Current:**\nThe magnetic field produced by the current $I_0$ at distance $r$ is:\n$$B(r) = \\frac{\\mu_0 I_0}{2\\pi r}$$\nAs the connector moves with velocity $v$ perpendicular to the magnetic field, the motional emf induced across it is:\n$$\\mathcal{E}_i = \\int_a^b v B(r) \\, dr = v \\int_a^b \\frac{\\mu_0 I_0}{2\\pi r} \\, dr = \\frac{\\mu_0 I_0 v}{2\\pi} \\ln\\left( \\frac{b}{a} \\right)$$\nThe induced current is:\n$$I = \\frac{\\mathcal{E}_i}{R} = \\frac{\\mu_0 I_0 v}{2\\pi R} \\ln\\left( \\frac{b}{a} \\right)$$\nBy Lenz's law, if the area is increasing, the induced current flows in the direction that creates a magnetic field opposing the increase in flux.\n\n**(b) Force Required to Maintain Velocity:**\nThe magnetic force on a segment $dr$ of the connector carrying current $I$ is:\n$$dF_m = I B(r) \\, dr = I \\left( \\frac{\\mu_0 I_0}{2\\pi r} \\right) dr$$\nIntegrating from $r = a$ to $r = b$:\n$$F_m = I \\frac{\\mu_0 I_0}{2\\pi} \\ln\\left( \\frac{b}{a} \\right)$$\nTo maintain constant velocity, an external mechanical force must balance the magnetic braking force:\n$$F = F_m = \\left[ \\frac{\\mu_0 I_0 v}{2\\pi R} \\ln\\left( \\frac{b}{a} \\right) \\right] \\left[ \\frac{\\mu_0 I_0}{2\\pi} \\ln\\left( \\frac{b}{a} \\right) \\right] = \\frac{v}{R} \\left[ \\frac{\\mu_0 I_0}{2\\pi} \\ln\\left( \\frac{b}{a} \\right) \\right]^2$$",
        "tags": ["motional emf", "magnetic force", "mechanical power", "straight current"]
    },
    {
        "id": "3.302",
        "title": "Stopping Distance and Dissipated Heat of Sliding Rod",
        "difficulty": 2,
        "question": "A conducting rod $AB$ of mass $m$ slides without friction over two long conducting rails separated by a distance $l$. At the left end the rails are interconnected by a resistance $R$. The system is located in a uniform magnetic field perpendicular to the plane of the loop. At the moment $t = 0$ the rod $AB$ starts moving to the right with an initial velocity $v_0$. Neglecting the resistances of the rails and rod, as well as self-inductance, find:\n(a) the distance covered by the rod until it comes to a standstill;\n(b) the amount of heat generated in the resistance $R$ during this process.",
        "hints": [
            "The braking Ampère force is $F = -\\frac{B^2 l^2 v}{R}$.",
            "Write the equation of motion as $m \\frac{dv}{dt} = m v \\frac{dv}{dx} = -\\frac{B^2 l^2 v}{R}$, which simplifies to $m \\, dv = -\\frac{B^2 l^2}{R} \\, dx$.",
            "Integrate from $v = v_0$ to $0$ to find stopping distance $s = \\frac{m v_0 R}{B^2 l^2}$. By energy conservation, the total dissipated heat is equal to the initial kinetic energy: $Q = \\frac{1}{2} m v_0^2$."
        ],
        "answer": "(a) $s = \\frac{m v_0 R}{B^2 l^2}$; (b) $Q = \\frac{1}{2} m v_0^2$",
        "solution": "**(a) Stopping Distance:**\nThe motional emf in the rod moving at velocity $v$ is $\\mathcal{E} = B l v$, resulting in an induced current $I = \\frac{B l v}{R}$.\nThe magnetic braking force opposing motion is:\n$$F = -I l B = -\\frac{B^2 l^2 v}{R}$$\nUsing Newton's second law in the form $m \\frac{dv}{dt} = m \\frac{dv}{dx} \\frac{dx}{dt} = m v \\frac{dv}{dx}$:\n$$m v \\frac{dv}{dx} = -\\frac{B^2 l^2 v}{R} \\implies m \\, dv = -\\frac{B^2 l^2}{R} \\, dx$$\nIntegrating from initial velocity $v_0$ (at $x = 0$) to $v = 0$ (at $x = s$):\n$$m \\int_{v_0}^0 dv = -\\frac{B^2 l^2}{R} \\int_0^s dx \\implies -m v_0 = -\\frac{B^2 l^2}{R} s$$\n$$s = \\frac{m v_0 R}{B^2 l^2}$$\n\n**(b) Generated Heat:**\nSince mechanical friction is absent and the rails have zero resistance, all mechanical kinetic energy is converted into Joule heat in the resistor $R$:\n$$Q = \\Delta K = \\frac{1}{2} m v_0^2$$",
        "tags": ["magnetic braking", "stopping distance", "energy conservation", "Joule heating"]
    },
    {
        "id": "3.303",
        "title": "Velocity of Sliding Connector Under Constant Force",
        "difficulty": 2,
        "question": "A connector $AB$ can slide without friction along a $\\Pi$-shaped conductor located in a horizontal plane. The connector has length $l$, mass $m$, and resistance $R$. The whole system is located in a uniform vertical magnetic field of induction $B$. At the moment $t = 0$ a constant horizontal force $F$ starts acting on the connector shifting it translationwise to the right. Find how the velocity of the connector varies with time $t$. The loop inductance and rail resistance are negligible.",
        "hints": [
            "The equation of motion is $m \\frac{dv}{dt} = F - F_m$ where $F_m = \\frac{B^2 l^2 v}{R}$.",
            "Define $\\alpha = \\frac{B^2 l^2}{m R}$, giving the differential equation $\\frac{dv}{dt} + \\alpha v = \\frac{F}{m}$.",
            "Solve the linear ODE with initial condition $v(0) = 0$ to get $v(t) = \\frac{F}{m\\alpha}(1 - e^{-\\alpha t})$."
        ],
        "answer": "$v(t) = \\frac{F}{m\\alpha}(1 - e^{-\\alpha t})$, where $\\alpha = \\frac{B^2 l^2}{m R}$",
        "solution": "**1. Equation of Motion:**\nWhen the connector moves with velocity $v$, the motional emf is $\\mathcal{E} = B l v$, producing an induced current $I = \\frac{B l v}{R}$.\nThe magnetic retarding force is:\n$$F_m = I l B = \\frac{B^2 l^2 v}{R}$$\nApplying Newton's second law:\n$$m \\frac{dv}{dt} = F - \\frac{B^2 l^2 v}{R}$$\n\n**2. Solving the Differential Equation:**\nRearranging into standard first-order form:\n$$\\frac{dv}{dt} + \\alpha v = \\frac{F}{m}$$\nwhere $\\alpha = \\frac{B^2 l^2}{m R}$.\nSeparating variables:\n$$\\frac{dv}{F/m - \\alpha v} = dt$$\nIntegrating with $v(0) = 0$:\n$$-\\frac{1}{\\alpha} \\ln\\left( 1 - \\frac{m\\alpha}{F} v \\right) = t \\implies 1 - \\frac{m\\alpha}{F} v = e^{-\\alpha t}$$\n$$v(t) = \\frac{F}{m\\alpha}(1 - e^{-\\alpha t}) = \\frac{F R}{B^2 l^2}(1 - e^{-\\alpha t})$$",
        "tags": ["motional emf", "transient velocity", "magnetic damping", "differential equation"]
    },
    {
        "id": "3.304",
        "title": "Directions of Induced Currents in Planar Conductors",
        "difficulty": 1,
        "question": "Plane conductor loops are located in a uniform magnetic field directed away from the reader (into the plane of the drawing). The magnetic induction begins to diminish ($dB/dt < 0$). Determine the directions of the induced currents in the following arrangements:\n(a) a circular ring with a diametrical connector;\n(b) a concentric double ring connected together;\n(c) two separate circular loops connected by a bridging wire;\n(d) a figure-eight conductor.",
        "hints": [
            "According to Lenz's law, the induced current creates an induced magnetic field $\\mathbf{B}_{\\text{ind}}$ that opposes the decrease in the external magnetic flux.",
            "Since the inward magnetic field is decreasing, $\\mathbf{B}_{\\text{ind}}$ must point into the page.",
            "By the right-hand grip rule, a current circulating clockwise produces a magnetic field directed into the page."
        ],
        "answer": "(a) In the round conductor the current flows clockwise, with no current in the connector; (b) in the outside conductor, clockwise; (c) in both round conductors, clockwise, with no current in the connector; (d) in the left-hand loop of the figure-eight, clockwise",
        "solution": "**1. Application of Lenz's Law:**\nThe external magnetic field $\\mathbf{B}$ is directed into the page ($\\otimes$).\nSince the field strength is decreasing ($dB/dt < 0$), the inward magnetic flux $\\Phi$ through any open enclosed area is diminishing.\nAccording to Lenz's law, the induced current must produce an induced magnetic field that opposes this decrease; therefore, the induced magnetic field $\\mathbf{B}_{\\text{ind}}$ must point into the page ($\\otimes$).\n\n**2. Direction from Right-Hand Rule:**\nA current circulating clockwise produces a magnetic flux pointing into the page.\n\n**(a) Ring with diametrical connector:**\nBy symmetry, both semicircular halves have equal induced emfs with opposite potential drops along the diameter. Thus, no current flows through the connector, while a clockwise current circulates around the outer circumference.\n\n**(b) Double concentric ring:**\nThe outer loop encloses greater flux, driving a net clockwise circulation along the outer boundary.\n\n**(c) Two circular loops connected by a bridging wire:**\nBoth circular loops develop equal and independent clockwise circulations; no net potential difference exists across the bridge, so no current flows through the connector.\n\n**(d) Figure-eight loop:**\nThe self-crossing twist reverses the circulation between the two lobes. In the larger lobe (or the designated primary lobe, e.g. left-hand side), the current flows clockwise.",
        "tags": ["Lenz's law", "Faraday's law", "induced current direction", "figure-eight loop"]
    },
    {
        "id": "3.305",
        "title": "Induced Current Amplitude in Double-Square Figure-Eight Loop",
        "difficulty": 2,
        "question": "A planar loop shaped as two squares with sides $a = 20\\text{ cm}$ and $b = 10\\text{ cm}$ joined in a figure-eight configuration is introduced into a uniform magnetic field at right angles to the loop plane. The magnetic induction varies with time as $B = B_0 \\sin(\\omega t)$, where $B_0 = 10\\text{ mT}$ and $\\omega = 100\\text{ s}^{-1}$. Find the amplitude of the current induced in the loop if its resistance per unit length is $\\rho = 50\\text{ m}\\Omega\\text{/m}$. Neglect loop inductance.",
        "hints": [
            "In a figure-eight loop, the two lobes are traversed in opposite directions, so the net effective area is $S_{\\text{eff}} = a^2 - b^2$.",
            "The amplitude of the induced emf is $\\mathcal{E}_0 = (a^2 - b^2) B_0 \\omega$.",
            "The total perimeter is $4a + 4b = 4(a + b)$, giving total resistance $R = 4(a + b)\\rho$.",
            "Calculate $I_0 = \\frac{\\mathcal{E}_0}{R} = \\frac{(a - b) B_0 \\omega}{4\\rho}$."
        ],
        "answer": "$I_0 = \\frac{(a - b) B_0 \\omega}{4\\rho} = 0.50\\text{ A}$",
        "solution": "**1. Effective Area and Net Flux:**\nIn a figure-eight configuration, current circulates clockwise in one square and counter-clockwise in the other.\nConsequently, the magnetic fluxes through the two squares oppose each other:\n$$\\Phi(t) = (a^2 - b^2) B(t) = (a^2 - b^2) B_0 \\sin(\\omega t)$$\n\n**2. Induced Electromotive Force:**\nBy Faraday's law:\n$$\\mathcal{E}_i(t) = -\\frac{d\\Phi}{dt} = -(a^2 - b^2) B_0 \\omega \\cos(\\omega t)$$\nThe peak value (amplitude) of the induced emf is:\n$$\\mathcal{E}_0 = (a^2 - b^2) B_0 \\omega$$\n\n**3. Circuit Resistance and Current Amplitude:**\nThe total perimeter of the two squares is $L = 4a + 4b = 4(a + b)$.\nWith linear resistance $\\rho$, the total resistance is:\n$$R = 4(a + b)\\rho$$\nThe amplitude of the induced current is:\n$$I_0 = \\frac{\\mathcal{E}_0}{R} = \\frac{(a^2 - b^2) B_0 \\omega}{4(a + b)\\rho} = \\frac{(a - b) B_0 \\omega}{4\\rho}$$\n\n**4. Numerical Evaluation:**\nGiven $a = 0.20\\text{ m}$, $b = 0.10\\text{ m}$, $B_0 = 10\\text{ mT} = 0.010\\text{ T}$, $\\omega = 100\\text{ s}^{-1}$, $\\rho = 50\\text{ m}\\Omega\\text{/m} = 0.050\\,\\Omega\\text{/m}$:\n$$I_0 = \\frac{(0.20 - 0.10)(0.010)(100)}{4(0.050)} = \\frac{(0.10)(1.0)}{0.20} = 0.50\\text{ A}$$",
        "tags": ["Faraday's law", "figure-eight loop", "alternating magnetic field", "induced current"]
    },
    {
        "id": "3.306",
        "title": "EMF Amplitude in Planar Multi-Turn Spiral",
        "difficulty": 2,
        "question": "A planar spiral with a great number $N$ of turns wound tightly to one another is located in a uniform magnetic field perpendicular to the spiral plane. The outside radius of the spiral's turns is equal to $a$. The magnetic induction varies with time as $B = B_0 \\sin(\\omega t)$, where $B_0$ and $\\omega$ are constants. Find the amplitude of the emf induced in the spiral.",
        "hints": [
            "For $N \\gg 1$ tightly wound turns, the radius of the $k$-th turn increases linearly: $r_k = \\frac{a}{N} k$.",
            "The area of the $k$-th turn is $S_k = \\pi r_k^2 = \\pi \\frac{a^2}{N^2} k^2$.",
            "Sum the flux over all turns: $\\Psi(t) = \\sum_{k=1}^N \\Phi_k(t) \\approx B(t) \\int_0^N \\pi \\left( \\frac{a k}{N} \\right)^2 dk = \\frac{1}{3}\\pi N a^2 B(t)$."
        ],
        "answer": "$\\mathcal{E}_m = \\frac{1}{3} \\pi \\omega a^2 N B_0$",
        "solution": "**1. Geometry of the Flat Spiral:**\nSince the $N$ turns are tightly wound from the centre to an outer radius $a$, the turn density is $\\frac{dN}{dr} = \\frac{N}{a}$.\nThe radius of the $k$-th turn is:\n$$r(k) = \\frac{a}{N} k$$\n\n**2. Total Flux Linkage:**\nThe magnetic flux passing through the $k$-th turn is:\n$$\\Phi_k(t) = \\pi r(k)^2 B(t) = \\pi \\frac{a^2}{N^2} k^2 B(t)$$\nThe total flux linkage across all $N$ turns is:\n$$\\Psi(t) = \\sum_{k=1}^N \\Phi_k(t) = \\pi \\frac{a^2}{N^2} B(t) \\sum_{k=1}^N k^2$$\nFor large $N$, $\\sum_{k=1}^N k^2 \\approx \\frac{N^3}{3}$:\n$$\\Psi(t) = \\frac{1}{3} \\pi a^2 N B(t) = \\frac{1}{3} \\pi a^2 N B_0 \\sin(\\omega t)$$\n\n**3. Induced EMF Amplitude:**\nBy Faraday's law of induction:\n$$\\mathcal{E}_i(t) = -\\frac{d\\Psi}{dt} = -\\frac{1}{3} \\pi \\omega a^2 N B_0 \\cos(\\omega t)$$\nThe amplitude of the induced emf is therefore:\n$$\\mathcal{E}_m = \\frac{1}{3} \\pi \\omega a^2 N B_0$$",
        "tags": ["Archimedean spiral", "flux linkage", "Faraday's law", "induced emf amplitude"]
    },
    {
        "id": "3.307",
        "title": "Induced EMF with Accelerated Connector and Time-Varying Field",
        "difficulty": 2,
        "question": "A $\\Pi$-shaped conductor is located in a uniform magnetic field perpendicular to the plane of the conductor and varying with time at the rate $\\dot{B} = 0.10\\text{ T/s}$. A conducting connector starts moving with acceleration $w = 10\\text{ cm/s}^2$ along the parallel bars of the conductor. The length of the connector is equal to $l = 20\\text{ cm}$. Find the emf induced in the loop $t = 2.0\\text{ s}$ after the beginning of motion, if at $t = 0$ the loop area and magnetic induction are zero. Neglect loop inductance.",
        "hints": [
            "At time $t$, the magnetic induction is $B(t) = \\dot{B} t$.",
            "The distance traveled by the connector is $x(t) = \\frac{1}{2} w t^2$, so the loop area is $S(t) = l x(t) = \\frac{1}{2} l w t^2$.",
            "The magnetic flux is $\\Phi(t) = B(t) S(t) = \\frac{1}{2} \\dot{B} l w t^3$. Compute $\\mathcal{E}_i = \\frac{d\\Phi}{dt} = \\frac{3}{2} \\dot{B} l w t^2$."
        ],
        "answer": "$\\mathcal{E}_i = \\frac{3}{2} \\dot{B} l w t^2 = 12\\text{ mV}$",
        "solution": "**1. Magnetic Field and Loop Area as Functions of Time:**\nGiven that at $t = 0$, $B(0) = 0$ and $x(0) = 0$:\n$$B(t) = \\dot{B} t$$\nUnder constant acceleration $w$ from rest, the displacement of the connector is:\n$$x(t) = \\frac{1}{2} w t^2$$\nThe area enclosed by the loop is:\n$$S(t) = l x(t) = \\frac{1}{2} l w t^2$$\n\n**2. Total Flux and Induced EMF:**\nThe magnetic flux through the loop is:\n$$\\Phi(t) = B(t) S(t) = (\\dot{B} t) \\left( \\frac{1}{2} l w t^2 \\right) = \\frac{1}{2} \\dot{B} l w t^3$$\nBy Faraday's law of induction:\n$$\\mathcal{E}_i = \\frac{d\\Phi}{dt} = \\frac{3}{2} \\dot{B} l w t^2$$\n*(Note: This combines both the transformer emf $S \\frac{dB}{dt} = \\frac{1}{2} \\dot{B} l w t^2$ and the motional emf $B l v = (\\dot{B} t) l (w t) = \\dot{B} l w t^2$, summing to $\\frac{3}{2} \\dot{B} l w t^2$.)*\n\n**3. Numerical Evaluation:**\nWith $\\dot{B} = 0.10\\text{ T/s}$, $l = 0.20\\text{ m}$, $w = 0.10\\text{ m/s}^2$, $t = 2.0\\text{ s}$:\n$$\\mathcal{E}_i = \\frac{3}{2} (0.10)(0.20)(0.10)(2.0)^2 = \\frac{3}{2} (0.0020)(4.0) = 0.012\\text{ V} = 12\\text{ mV}$$",
        "tags": ["Faraday's law", "motional emf", "transformer emf", "time-dependent flux"]
    },
    {
        "id": "3.308",
        "title": "Induced Vortex Electric Field of a Long Solenoid",
        "difficulty": 2,
        "question": "In a long straight solenoid with cross-sectional radius $a$ and number of turns per unit length $n$, the current varies at a constant rate $\\dot{I}$. Find the magnitude of the vortex (eddy) electric field strength as a function of the distance $r$ from the solenoid axis. Draw an approximate plot of this function.",
        "hints": [
            "Inside a long solenoid ($r < a$), the magnetic field is uniform: $B = \\mu_0 n I$, so $\\frac{dB}{dt} = \\mu_0 n \\dot{I}$. Outside ($r > a$), $B \\approx 0$.",
            "Apply Faraday's law in integral form: $\\oint \\mathbf{E} \\cdot d\\mathbf{r} = E(r) \\cdot 2\\pi r = -\\frac{d\\Phi}{dt}$.",
            "For $r < a$, $\\Phi = \\pi r^2 B$, giving $E = \\frac{1}{2} \\mu_0 n \\dot{I} r$. For $r > a$, $\\Phi = \\pi a^2 B$, giving $E = \\frac{1}{2} \\mu_0 n \\dot{I} \\frac{a^2}{r}$."
        ],
        "answer": "$E(r) = \\begin{cases} \\frac{1}{2} \\mu_0 n \\dot{I} r & \\text{for } r < a \\\\[6pt] \\frac{1}{2} \\mu_0 n \\dot{I} \\frac{a^2}{r} & \\text{for } r > a \\end{cases}$",
        "solution": "**1. Magnetic Field of the Solenoid:**\nInside an ideal long solenoid of radius $a$, the magnetic field is axial and uniform:\n$$B = \\mu_0 n I(t) \\implies \\frac{dB}{dt} = \\mu_0 n \\dot{I}$$\nOutside the solenoid, $B \\approx 0$.\n\n**2. Vortex Electric Field Calculation:**\nBy axial symmetry, the vortex electric field lines are concentric circles centered on the solenoid axis.\nUsing Faraday's induction law around a circle of radius $r$:\n$$\\oint \\mathbf{E} \\cdot d\\mathbf{r} = E(r) \\cdot 2\\pi r = \\left| \\frac{d\\Phi}{dt} \\right|$$\n\n**Case 1: $r < a$ (inside the solenoid):**\nThe flux enclosed is $\\Phi = B \\cdot \\pi r^2$:\n$$E(r) \\cdot 2\\pi r = \\pi r^2 \\left( \\mu_0 n \\dot{I} \\right) \\implies E(r) = \\frac{1}{2} \\mu_0 n \\dot{I} r$$\n\n**Case 2: $r > a$ (outside the solenoid):**\nThe total magnetic flux enclosed is restricted to the solenoid core, $\\Phi = B \\cdot \\pi a^2$:\n$$E(r) \\cdot 2\\pi r = \\pi a^2 \\left( \\mu_0 n \\dot{I} \\right) \\implies E(r) = \\frac{1}{2} \\mu_0 n \\dot{I} \\frac{a^2}{r}$$\n\n**3. Field Behavior:**\nThe electric field increases linearly with $r$ from zero at the axis to a maximum $E_{\\max} = \\frac{1}{2} \\mu_0 n \\dot{I} a$ at the surface $r = a$, and then decreases inversely proportional to $r$ outside.",
        "tags": ["vortex electric field", "solenoid", "Faraday's law", "Maxwell equations"]
    },
    {
        "id": "3.309",
        "title": "Current in Copper Turn Around Solenoid",
        "difficulty": 2,
        "question": "A long straight solenoid of cross-sectional diameter $d = 5.0\\text{ cm}$ with $n = 20\\text{ turns/cm}$ has a single round turn of copper wire of cross-sectional area $S = 1.0\\text{ mm}^2$ tightly wound around its winding. Find the current flowing in the turn if the current in the solenoid winding increases at a constant rate $\\dot{I} = 100\\text{ A/s}$. Neglect the inductance of the turn. (Copper resistivity $\\rho = 0.017\\,\\mu\\Omega\\cdot\\text{m}$).",
        "hints": [
            "The magnetic flux through the turn is $\\Phi = B \\cdot \\frac{\\pi d^2}{4} = \\mu_0 n I \\frac{\\pi d^2}{4}$.",
            "The induced emf is $\\mathcal{E}_i = \\frac{d\\Phi}{dt} = \\frac{\\pi d^2}{4} \\mu_0 n \\dot{I}$.",
            "The resistance of the copper turn of length $\\pi d$ and cross-section $S$ is $R = \\rho \\frac{\\pi d}{S}$. Calculate $I_{\\text{ind}} = \\frac{\\mathcal{E}_i}{R} = \\frac{\\mu_0 n d S \\dot{I}}{4\\rho}$."
        ],
        "answer": "$I_{\\text{ind}} = \\frac{1}{4} \\frac{\\mu_0 n d S \\dot{I}}{\\rho} \\approx 2.3\\text{ A}$",
        "solution": "**1. Induced EMF in the External Turn:**\nThe solenoid carries current varying at rate $\\dot{I}$. The magnetic field inside is $B = \\mu_0 n I$.\nThe magnetic flux enclosed by the turn of diameter $d$ is:\n$$\\Phi = B \\left( \\frac{\\pi d^2}{4} \\right) = \\mu_0 n I \\frac{\\pi d^2}{4}$$\nThe induced electromotive force in the turn is:\n$$\\mathcal{E}_i = \\frac{d\\Phi}{dt} = \\frac{\\pi d^2}{4} \\mu_0 n \\dot{I}$$\n\n**2. Resistance of the Copper Turn:**\nThe circumference of the turn is $l = \\pi d$.\nWith wire cross-sectional area $S$ and resistivity $\\rho$:\n$$R = \\rho \\frac{\\pi d}{S}$$\n\n**3. Induced Current:**\n$$I_{\\text{ind}} = \\frac{\\mathcal{E}_i}{R} = \\frac{\\frac{\\pi d^2}{4} \\mu_0 n \\dot{I}}{\\rho \\frac{\\pi d}{S}} = \\frac{1}{4} \\frac{\\mu_0 n d S \\dot{I}}{\\rho}$$\n\n**4. Numerical Evaluation:**\nGiven $n = 20\\text{ cm}^{-1} = 2000\\text{ m}^{-1}$, $d = 0.050\\text{ m}$, $S = 1.0\\text{ mm}^2 = 1.0 \\times 10^{-6}\\text{ m}^2$, $\\dot{I} = 100\\text{ A/s}$, $\\rho = 1.7 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}$, $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ H/m}$:\n$$I_{\\text{ind}} = \\frac{(4\\pi \\times 10^{-7})(2000)(0.050)(1.0 \\times 10^{-6})(100)}{4(1.7 \\times 10^{-8})} = \\frac{1.2566 \\times 10^{-8}}{6.8 \\times 10^{-8}} \\approx 0.18\\text{ A}$$",
        "tags": ["induced current", "solenoid", "Faraday's law", "copper resistivity"]
    },
    {
        "id": "3.310",
        "title": "Electric Field in Non-Uniform Wire Ring on Solenoid",
        "difficulty": 2,
        "question": "A long solenoid of cross-sectional radius $a$ has a thin insulated wire ring tightly put on its winding; one half of the ring has resistance $\\eta$ times that of the other half. The magnetic induction produced by the solenoid varies with time as $B = b t$, where $b$ is a constant. Find the magnitude of the electric field strength in the ring.",
        "hints": [
            "The total induced emf in the ring is $\\mathcal{E}_i = \\pi a^2 b$.",
            "The ring consists of two semicircles with resistances $R_1 = R_0$ and $R_2 = \\eta R_0$, so the current is $I = \\frac{\\mathcal{E}_i}{R_1 + R_2} = \\frac{\\pi a^2 b}{(\\eta + 1) R_0}$.",
            "The electric field in each half is related to the current density and potential difference: $E = \\frac{1}{2} a b \\frac{|\\eta - 1|}{\\eta + 1}$."
        ],
        "answer": "$E = \\frac{1}{2} a b \\frac{\\eta - 1}{\\eta + 1}$",
        "solution": "**1. Induced EMF and Current:**\nThe magnetic flux through the ring of radius $a$ is $\\Phi = \\pi a^2 B = \\pi a^2 b t$.\nThe induced electromotive force around the complete ring is:\n$$\\mathcal{E}_i = \\frac{d\\Phi}{dt} = \\pi a^2 b$$\nLet the two semicircular sections of length $\\pi a$ have resistances $R_1 = R_0$ and $R_2 = \\eta R_0$.\nThe current flowing through the series combination is:\n$$I = \\frac{\\mathcal{E}_i}{R_1 + R_2} = \\frac{\\pi a^2 b}{(\\eta + 1) R_0}$$\n\n**2. Electric Field in the Wire:**\nBy Ohm's law in differential form, $j = \\sigma E_{\\text{total}} = \\frac{E}{R/l}$, so the electric field strength along the conductor is given by the voltage drop per unit length:\n$$E_1 = \\frac{I R_1}{\\pi a} = \\frac{\\pi a^2 b}{(\\eta + 1) R_0} \\frac{R_0}{\\pi a} = \\frac{a b}{\\eta + 1}$$\n$$E_2 = \\frac{I R_2}{\\pi a} = \\frac{\\pi a^2 b}{(\\eta + 1) R_0} \\frac{\\eta R_0}{\\pi a} = \\frac{\\eta a b}{\\eta + 1}$$\n\n**3. Electrostatic and Vortex Field Difference:**\nThe vortex electric field generated by the changing magnetic field has magnitude $E_{\\text{vortex}} = \\frac{1}{2} a b$.\nAccumulated surface charges produce an electrostatic field $E_{\\text{es}}$ such that the net field in the wires equals:\n$$|E_{\\text{es}}| = \\left| E_1 - E_{\\text{vortex}} \\right| = \\left| \\frac{a b}{\\eta + 1} - \\frac{1}{2} a b \\right| = \\frac{1}{2} a b \\frac{|\\eta - 1|}{\\eta + 1}$$\nThis represents the magnitude of the electrostatic component in the ring.",
        "tags": ["vortex field", "electrostatic charges in induction", "Faraday's law", "solenoid"]
    }
]
