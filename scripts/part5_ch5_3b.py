"""
part5_ch5_3b.py
Curated problems 5.127 to 5.156 (30 problems) of Irodov Chapter 5.3:
Diffraction of Light (Part B: Diffraction Gratings, Resolving Power of Optical Instruments, X-Ray Diffraction).
"""

CH5_3B_CURATED = [
    {
        "id": "5.127",
        "title": "Wavelength of Light from Angular Separation Between Grating Maxima",
        "difficulty": 2,
        "question": "Find the wavelength $\\lambda$ of monochromatic light falling normally on a diffraction grating with period $d = 2.2\\,\\mu\\text{m}$ if the angle between the directions to the Fraunhofer maxima of the first and the second order is equal to $\\Delta\\theta = 15^\\circ$.",
        "hints": [
            "Write the diffraction grating condition for normal incidence for the first and second orders: $d \\sin\\theta_1 = \\lambda$ and $d \\sin\\theta_2 = 2\\lambda$.",
            "Use the angular separation relation $\\theta_2 = \\theta_1 + \\Delta\\theta$. Expand $\\sin(\\theta_1 + \\Delta\\theta) = 2 \\sin\\theta_1$ using angle addition.",
            "Express $\\tan\\theta_1$ in terms of $\\Delta\\theta$, then find $\\sin\\theta_1 = \\frac{\\sin\\Delta\\theta}{\\sqrt{5 - 4\\cos\\Delta\\theta}}$, giving $\\lambda = d \\sin\\theta_1$."
        ],
        "answer": "$\\lambda = \\frac{d \\sin\\Delta\\theta}{\\sqrt{5 - 4\\cos\\Delta\\theta}} = 0.54\\,\\mu\\text{m}$",
        "solution": "**1. Grating Equations for Orders 1 and 2:**\nFor normal incidence on a grating of period $d$:\n$$d \\sin\\theta_1 = \\lambda, \\quad d \\sin\\theta_2 = 2\\lambda$$\nTherefore:\n$$\\sin\\theta_2 = 2 \\sin\\theta_1$$\n\n**2. Trigonometric Relation:**\nGiven that $\\theta_2 - \\theta_1 = \\Delta\\theta$, we have $\\theta_2 = \\theta_1 + \\Delta\\theta$:\n$$\\sin(\\theta_1 + \\Delta\\theta) = \\sin\\theta_1 \\cos\\Delta\\theta + \\cos\\theta_1 \\sin\\Delta\\theta = 2 \\sin\\theta_1$$\nRearranging:\n$$\\cos\\theta_1 \\sin\\Delta\\theta = \\sin\\theta_1 (2 - \\cos\\Delta\\theta)$$\n$$\\tan\\theta_1 = \\frac{\\sin\\Delta\\theta}{2 - \\cos\\Delta\\theta}$$\nUsing $\\sin\\theta_1 = \\frac{\\tan\\theta_1}{\\sqrt{1 + \\tan^2\\theta_1}}$:\n$$\\sin\\theta_1 = \\frac{\\sin\\Delta\\theta}{\\sqrt{\\sin^2\\Delta\\theta + (2 - \\cos\\Delta\\theta)^2}} = \\frac{\\sin\\Delta\\theta}{\\sqrt{\\sin^2\\Delta\\theta + 4 - 4\\cos\\Delta\\theta + \\cos^2\\Delta\\theta}} = \\frac{\\sin\\Delta\\theta}{\\sqrt{5 - 4\\cos\\Delta\\theta}}$$\n\n**3. Expression for Wavelength:**\n$$\\lambda = d \\sin\\theta_1 = \\frac{d \\sin\\Delta\\theta}{\\sqrt{5 - 4\\cos\\Delta\\theta}}$$\n\n**4. Numerical Evaluation:**\nFor $d = 2.2\\,\\mu\\text{m}$ and $\\Delta\\theta = 15^\\circ$:\n$$\\sin 15^\\circ \\approx 0.2588, \\quad \\cos 15^\\circ \\approx 0.9659$$\n$$5 - 4\\cos 15^\\circ = 5 - 4(0.9659) = 5 - 3.8637 = 1.1363$$\n$$\\sqrt{1.1363} \\approx 1.0660$$\n$$\\sin\\theta_1 = \\frac{0.2588}{1.0660} \\approx 0.2428$$\n$$\\lambda = (2.2\\,\\mu\\text{m})(0.2428) \\approx 0.534\\,\\mu\\text{m} \\approx 0.54\\,\\mu\\text{m}$$",
        "tags": ["diffraction grating", "Fraunhofer diffraction", "diffraction angle", "wavelength"]
    },
    {
        "id": "5.128",
        "title": "Diffraction Angle of Highest Observable Order for Normal and Oblique Incidence",
        "difficulty": 2,
        "question": "Light with wavelength $\\lambda = 530\\text{ nm}$ falls on a transparent diffraction grating with period $d = 1.50\\,\\mu\\text{m}$. Find the angle, relative to the grating normal, at which the Fraunhofer maximum of highest order is observed provided the light falls on the grating:\n(a) at right angles;\n(b) at an angle $\\theta_0 = 60^\\circ$ to the normal.",
        "hints": [
            "(a) For normal incidence, $d \\sin\\theta = k \\lambda$. The condition $|\\sin\\theta| \\le 1$ determines the maximum order $k_{\\text{max}} = \\lfloor d/\\lambda \\rfloor$.",
            "(b) For oblique incidence, the path difference between adjacent slits is $d(\\sin\\theta - \\sin\\theta_0) = k \\lambda$.",
            "For highest order in (b), consider negative diffraction orders ($k < 0$) which deflect toward the opposite side: $\\sin\\theta = \\sin\\theta_0 + k \\frac{\\lambda}{d}$, with $\\sin\\theta \\ge -1$."
        ],
        "answer": "(a) $\\theta = 45^\\circ$;\n(b) $\\theta = -65^\\circ$",
        "solution": "**1. Part (a): Normal Incidence:**\nThe grating equation is:\n$$d \\sin\\theta = k \\lambda \\implies \\sin\\theta = \\frac{k \\lambda}{d}$$\nSince $|\\sin\\theta| \\le 1$, the maximum diffraction order is:\n$$k_{\\text{max}} = \\left\\lfloor \\frac{d}{\\lambda} \\right\\rfloor = \\left\\lfloor \\frac{1.50\\,\\mu\\text{m}}{0.530\\,\\mu\\text{m}} \\right\\rfloor = \\lfloor 2.83 \\rfloor = 2$$\nFor $k = 2$:\n$$\\sin\\theta = \\frac{2 \\times 0.530}{1.50} = \\frac{1.06}{1.50} \\approx 0.7067$$\n$$\\theta = \\arcsin(0.7067) \\approx 44.96^\\circ \\approx 45^\\circ$$\n\n**2. Part (b): Oblique Incidence at $\\theta_0 = 60^\\circ$:**\nThe path difference between rays from adjacent grooves is $d(\\sin\\theta - \\sin\\theta_0) = k \\lambda$, so:\n$$\\sin\\theta = \\sin\\theta_0 + k \\frac{\\lambda}{d}$$\nWith $\\sin 60^\\circ = \\frac{\\sqrt{3}}{2} \\approx 0.8660$ and $\\frac{\\lambda}{d} = \\frac{0.530}{1.50} \\approx 0.3533$:\n- For positive $k$: $k = +1 \\implies \\sin\\theta = 0.8660 + 0.3533 = 1.219 > 1$ (no positive order beyond $k=0$).\n- For negative $k$: $\\sin\\theta$ decreases.\n  - $k = -1$: $\\sin\\theta = 0.8660 - 0.3533 = 0.5127$\n  - $k = -2$: $\\sin\\theta = 0.8660 - 0.7067 = 0.1593$\n  - $k = -3$: $\\sin\\theta = 0.8660 - 1.0600 = -0.1940$\n  - $k = -4$: $\\sin\\theta = 0.8660 - 1.4133 = -0.5473$\n  - $k = -5$: $\\sin\\theta = 0.8660 - 1.7667 = -0.9007$\n  - $k = -6$: $\\sin\\theta = 0.8660 - 2.1200 = -1.254 < -1$ (not observable).\nThus the maximum order is $k = -5$:\n$$\\theta = \\arcsin(-0.9007) \\approx -64.25^\\circ \\approx -65^\\circ$$",
        "tags": ["diffraction grating", "oblique incidence", "highest order", "grating equation"]
    },
    {
        "id": "5.129",
        "title": "Principal Maxima Separation in the Focal Plane of a Cylindrical Lens Grating",
        "difficulty": 2,
        "question": "Light with wavelength $\\lambda = 0.60\\,\\mu\\text{m}$ falls normally on a diffraction grating inscribed on a plane surface of a plano-convex cylindrical glass lens with curvature radius $R = 20\\text{ cm}$ and refractive index $n = 1.50$. The period of the grating is $d = 6.0\\,\\mu\\text{m}$. Find the distance $x$ between the principal maxima of first order located symmetrically in the focal plane of that lens.",
        "hints": [
            "A plano-convex cylindrical lens focuses parallel rays into a focal line at focal distance $f = \\frac{R}{n - 1}$.",
            "The diffraction grating diffracts light into symmetrical first-order beams at angles given by $\\sin\\theta = \\pm \\frac{\\lambda}{d}$.",
            "In the focal plane of the lens, rays diffracted at angle $\\theta$ are focused at distance $y = f \\tan\\theta$. The separation between the two symmetric orders is $x = 2 f \\tan\\theta = \\frac{2 R}{n - 1} \\frac{\\lambda}{\\sqrt{d^2 - \\lambda^2}}$."
        ],
        "answer": "$x = \\frac{2 R}{n - 1} \\frac{\\lambda}{\\sqrt{d^2 - \\lambda^2}} = 8.0\\text{ cm}$",
        "solution": "**1. Focal Length of the Plano-Convex Lens:**\nThe focal length of a plano-convex thin lens with radius of curvature $R$ and refractive index $n$ is:\n$$f = \\frac{R}{n - 1}$$\nFor $R = 20\\text{ cm}$ and $n = 1.50$:\n$$f = \\frac{20\\text{ cm}}{1.50 - 1} = 40\\text{ cm}$$\n\n**2. First-Order Diffraction Angle:**\nFor normal incidence on a grating of period $d$:\n$$\\sin\\theta = \\frac{\\lambda}{d} = \\frac{0.60\\,\\mu\\text{m}}{6.0\\,\\mu\\text{m}} = 0.10$$\n$$\\tan\\theta = \\frac{\\sin\\theta}{\\sqrt{1 - \\sin^2\\theta}} = \\frac{\\lambda/d}{\\sqrt{1 - (\\lambda/d)^2}} = \\frac{\\lambda}{\\sqrt{d^2 - \\lambda^2}}$$\n$$\\tan\\theta = \\frac{0.10}{\\sqrt{1 - 0.01}} = \\frac{0.10}{\\sqrt{0.99}} \\approx 0.1005$$\n\n**3. Distance Between First-Order Maxima:**\nThe distance from the central axis to each first-order line in the focal plane is $y = f \\tan\\theta$.\nThe total separation between the two symmetric first-order maxima is:\n$$x = 2 y = 2 f \\tan\\theta = \\frac{2 R}{n - 1} \\frac{\\lambda}{\\sqrt{d^2 - \\lambda^2}}$$\nSubstituting numerical values:\n$$x = 2 (40\\text{ cm})(0.1005) \\approx 8.04\\text{ cm} \\approx 8.0\\text{ cm}$$",
        "tags": ["diffraction grating", "cylindrical lens", "focal plane", "Fraunhofer diffraction"]
    },
    {
        "id": "5.130",
        "title": "Diffraction Grating Inscribed on the Exit Face of a Glass Wedge",
        "difficulty": 3,
        "question": "A plane light wave with wavelength $\\lambda = 0.50\\,\\mu\\text{m}$ falls normally on the face of a glass wedge with refracting angle $\\theta_w = 30^\\circ$ and refractive index $n = 1.50$. On the opposite face of the wedge a transparent diffraction grating with period $d = 2.00\\,\\mu\\text{m}$ is inscribed, whose lines are parallel to the wedge's edge. Find the angles that the direction of incident light forms with the directions to the principal Fraunhofer maxima of the zero and the first order. What is the highest order of the spectrum, and at what angle to the incident beam is it observed?",
        "hints": [
            "Inside the wedge, the beam strikes the exit face at angle of incidence $\\theta_w = 30^\\circ$.",
            "The optical path difference between rays passing through adjacent slits separated by $d$ on the exit face is $\\Delta = d [n \\sin\\theta_w - \\sin\\theta'] = k \\lambda$, where $\\theta'$ is the angle in air relative to the grating normal.",
            "The angle between the diffracted beam and the original incident beam direction is $\\phi = \\theta' - \\theta_w$. Determine $\\phi$ for $k = 0$, $k = -1$, and find the maximum order $k$ for which $|\\sin\\theta'| \\le 1$."
        ],
        "answer": "$\\phi_0 = -18.5^\\circ$ ($k = 0$), $\\phi = 0^\\circ$ ($k = -1$), $k_{\\text{max}} = 6$ with $\\phi_{\\text{max}} = +78.5^\\circ$",
        "solution": "**1. Geometry and Grating Equation on the Exit Face:**\nThe light strikes the first face normally and travels undeviated inside the glass wedge of refractive index $n = 1.50$. At the second face, the angle of incidence is $\\theta_w = 30^\\circ$.\nLet $\\theta'$ be the angle of the diffracted beam in air relative to the normal of the exit face.\nThe path difference between adjacent slits of period $d$ is:\n$$\\Delta = d (n \\sin\\theta_w - \\sin\\theta') = k \\lambda$$\n$$\\sin\\theta' = n \\sin\\theta_w - k \\frac{\\lambda}{d}$$\nWith $n = 1.50$, $\\theta_w = 30^\\circ$, and $\\frac{\\lambda}{d} = \\frac{0.50\\,\\mu\\text{m}}{2.00\\,\\mu\\text{m}} = 0.25$:\n$$n \\sin\\theta_w = 1.50 \\sin 30^\\circ = 0.75$$\n$$\\sin\\theta' = 0.75 - 0.25 k$$\n\n**2. Angle with Respect to the Incident Beam:**\nThe normal to the exit face is tilted by $\\theta_w = 30^\\circ$ relative to the incident beam. The deviation angle $\\phi$ relative to the incident direction is:\n$$\\phi = -(\\theta' - \\theta_w)$$\n\n**3. Evaluation for Low Orders:**\n- **Zero order ($k = 0$):**\n  $$\\sin\\theta'_0 = 0.75 \\implies \\theta'_0 = \\arcsin(0.75) \\approx 48.59^\\circ$$\n  Deviation: $\\phi_0 = -(48.59^\\circ - 30^\\circ) = -18.59^\\circ \\approx -18.5^\\circ$ (refracted beam bent away from the apex).\n- **First order toward the apex ($k = -1$ in our equation, or $+1$ with reversed sign):**\n  $$\\sin\\theta' = 0.75 - 0.25(-1) = 0.75 + 0.25 = 1.00 \\dots$$\n  If $k = 1$:\n  $$\\sin\\theta'_1 = 0.75 - 0.25(1) = 0.50 \\implies \\theta'_1 = 30^\\circ$$\n  Deviation: $\\phi_1 = -(30^\\circ - 30^\\circ) = 0^\\circ$ (the diffracted beam continues straight along the original incident direction!).\n\n**4. Highest Observable Order:**\nFor diffracted light to emerge into air, $-1 \\le \\sin\\theta' \\le 1$:\n$$-1 \\le 0.75 - 0.25 k \\le 1$$\n$$-1.75 \\le -0.25 k \\implies k \\le 7$$\nFor $k = 7$: $\\sin\\theta' = 0.75 - 1.75 = -1.0 \\implies \\theta' = -90^\\circ$ (grazing along the exit face).\nThe highest non-grazing order is $k = 6$:\n$$\\sin\\theta'_6 = 0.75 - 0.25(6) = 0.75 - 1.50 = -0.75$$\n$$\\theta'_6 = \\arcsin(-0.75) \\approx -48.59^\\circ$$\nDeviation angle:\n$$\\phi_6 = -(-48.59^\\circ - 30^\\circ) = -(-78.59^\\circ) = +78.59^\\circ \\approx +78.5^\\circ$$",
        "tags": ["diffraction grating", "glass wedge", "oblique incidence", "refraction", "highest order"]
    },
    {
        "id": "5.131",
        "title": "Phase Diffraction Grating Condition for Zero Central Maximum",
        "difficulty": 2,
        "question": "A plane light wave with wavelength $\\lambda$ falls normally on a phase diffraction grating cut on a glass plate with refractive index $n$. The grating consists of alternate strips of width $a/2$ (period $a$) etched to depth $h$. Find the depth $h$ of the lines at which the intensity of the central Fraunhofer maximum is zero. What is in this case the diffraction angle corresponding to the first maximum?",
        "hints": [
            "Light traversing the etched grooves and the unetched plate experiences an optical path difference $\\Delta = (n - 1) h$.",
            "For the central maximum ($\theta = 0$), waves from the two equal halves of each period interfere destructively when their phase difference is an odd multiple of $\\pi$: $\\Delta\\Phi = \\frac{2\\pi}{\\lambda}(n - 1)h = (2k - 1)\\pi$.",
            "For the first diffraction maximum, the condition corresponds to $\\sin\\theta_1 = \\frac{\\lambda}{2a}$ or $\\sin\\theta_1 = \\frac{\\lambda}{a}$."
        ],
        "answer": "$h = \\frac{(k - 1/2)\\lambda}{n - 1}$ ($k = 1, 2, \\dots$), $\\sin\\theta_1 = \\frac{\\lambda}{2a}$",
        "solution": "**1. Phase Shift in a Phase Grating:**\nThe grating consists of periodic strips of width $a/2$ with groove depth $h$, cut in a dielectric substrate of refractive index $n$.\nThe optical path difference between light rays passing through an unetched strip and an etched groove is:\n$$\\Delta = (n - 1) h$$\nThe corresponding phase difference is:\n$$\\delta = \\frac{2\\pi}{\\lambda} (n - 1) h$$\n\n**2. Condition for Zero Central Maximum:**\nAt $\\theta = 0$, each period consists of two equal areas transmitting light with a relative phase shift $\\delta$.\nThe resultant amplitude for each period is:\n$$E(0) \\propto 1 + e^{i\\delta} = e^{i\\delta/2} \\cdot 2 \\cos\\left(\\frac{\\delta}{2}\\right)$$\nThe intensity vanishes when $\\cos(\\delta/2) = 0$, meaning:\n$$\\frac{\\delta}{2} = \\left(k - \\frac{1}{2}\\right)\\pi \\implies \\frac{\\pi}{\\lambda}(n - 1)h = \\left(k - \\frac{1}{2}\\right)\\pi$$\n$$h = \\frac{(k - 1/2)\\lambda}{n - 1} \\quad (k = 1, 2, 3, \\dots)$$\n\n**3. Angle of the First Diffraction Maximum:**\nWhen the zero order is cancelled by destructive interference, the principal energy is diffracted into the first-order sidebands. The path difference between adjacent steps of width $a$ gives the first maximum at:\n$$\\sin\\theta_1 = \\frac{\\lambda}{2a}$$",
        "tags": ["phase grating", "groove depth", "destructive interference", "Fraunhofer diffraction"]
    },
    {
        "id": "5.132",
        "title": "Ultrasonic Wave Velocity from Light Diffraction Pattern (Debye-Sears Effect)",
        "difficulty": 2,
        "question": "A plane light wave with wavelength $\\lambda = 0.55\\,\\mu\\text{m}$ passes through a water-filled tank in which a standing ultrasonic wave is sustained at frequency $\\nu = 4.7\\text{ MHz}$. In the focal plane of an objective with focal length $f = 35\\text{ cm}$, a diffraction spectrum is observed with separation between neighbouring maxima $\\Delta x = 0.60\\text{ mm}$. Find the propagation velocity $v$ of ultrasonic oscillations in water.",
        "hints": [
            "A standing acoustic wave produces periodic modulation of the refractive index in the liquid with spatial period equal to the acoustic wavelength $\\Lambda = \\lambda_s = v / \\nu$.",
            "This periodic structure acts as a phase transmission grating. The angular separation between neighbouring diffraction orders is $\\theta \\approx \\frac{\\lambda}{\\Lambda} = \\frac{\\lambda \\nu}{v}$.",
            "In the focal plane of the lens, the linear separation is $\\Delta x = f \\theta = \\frac{f \\lambda \\nu}{v}$. Solve for $v$."
        ],
        "answer": "$v = \\frac{f \\lambda \\nu}{\\Delta x} = 1.5\\text{ km/s}$",
        "solution": "**1. Ultrasonic Wave as a Diffraction Grating:**\nAn acoustic wave propagating in a medium causes periodic variations in density and refractive index. The spatial period of this phase grating is equal to the acoustic wavelength:\n$$\\Lambda = \\frac{v}{\\nu}$$\nwhere $v$ is the speed of sound and $\\nu$ is the acoustic frequency.\n\n**2. Diffraction Angle and Focal Plane Separation:**\nFor light of wavelength $\\lambda$, the angular separation between adjacent Fraunhofer maxima is:\n$$\\sin\\theta \\approx \\theta = \\frac{\\lambda}{\\Lambda} = \\frac{\\lambda \\nu}{v}$$\nIn the focal plane of an objective with focal length $f$, this angular separation corresponds to a linear separation:\n$$\\Delta x = f \\theta = \\frac{f \\lambda \\nu}{v}$$\n\n**3. Ultrasonic Propagation Velocity:**\n$$v = \\frac{f \\lambda \\nu}{\\Delta x}$$\n\n**4. Numerical Evaluation:**\nGiven $f = 35\\text{ cm} = 0.35\\text{ m}$, $\\lambda = 0.55\\,\\mu\\text{m} = 5.5 \\times 10^{-7}\\text{ m}$, $\\nu = 4.7\\text{ MHz} = 4.7 \\times 10^6\\text{ s}^{-1}$, and $\\Delta x = 0.60\\text{ mm} = 6.0 \\times 10^{-4}\\text{ m}$:\n$$v = \\frac{0.35 \\times (5.5 \\times 10^{-7}) \\times (4.7 \\times 10^6)}{6.0 \\times 10^{-4}}$$\n$$0.35 \\times 5.5 \\times 4.7 = 9.0475$$\n$$v = \\frac{9.0475 \\times 10^{-1}}{6.0 \\times 10^{-4}} = \\frac{0.90475}{6.0 \\times 10^{-4}} \\approx 1508\\text{ m/s} \\approx 1.5\\text{ km/s}$$",
        "tags": ["Debye-Sears effect", "acousto-optics", "ultrasonic wave", "diffraction grating", "speed of sound"]
    },
    {
        "id": "5.133",
        "title": "Angular Distance of a Double Star by Michelson Stellar Interferometer",
        "difficulty": 2,
        "question": "To measure the angular distance $\\psi$ between the components of a double star by Michelson's method, a diaphragm with two narrow parallel slits separated by an adjustable distance $d$ is placed in front of a telescope's objective. While decreasing $d$, the first smearing (loss of visibility) of the fringe pattern was observed in the focal plane of the objective at $d = 95\\text{ cm}$. Find $\\psi$, assuming the wavelength of light to be $\\lambda = 0.55\\,\\mu\\text{m}$.",
        "hints": [
            "Each star produces its own two-slit interference pattern in the focal plane of the objective, with angular fringe spacing $\\theta = \\lambda / d$.",
            "The two fringe systems are shifted angularly by $\\psi$ (the angular separation of the stars).",
            "The fringes vanish (first minimum of visibility) when the maxima of one system coincide with the minima of the other system: $\\psi = \\theta / 2 = \\lambda / (2d)$."
        ],
        "answer": "$\\psi = \\frac{\\lambda}{2d} \\approx 0.06''$",
        "solution": "**1. Fringe Systems from Two Incoherent Point Sources:**\nEach component of the double star forms an independent interference pattern in the focal plane of the objective with angular fringe spacing:\n$$\\theta = \\frac{\\lambda}{d}$$\nBecause the two stars are separated by angular distance $\\psi$, their central (zeroth-order) interference fringes are separated by the same angle $\\psi$.\n\n**2. Condition for Fringe Disappearance:**\nAs the slit separation $d$ is varied, the fringe period $\\theta$ changes.\nThe interference fringes completely wash out when the bright fringes produced by the first star coincide with the dark fringes produced by the second star:\n$$\\psi = \\frac{\\theta}{2} = \\frac{\\lambda}{2d}$$\n\n**3. Numerical Evaluation:**\nGiven $\\lambda = 0.55\\,\\mu\\text{m} = 5.5 \\times 10^{-7}\\text{ m}$ and $d = 95\\text{ cm} = 0.95\\text{ m}$:\n$$\\psi = \\frac{5.5 \\times 10^{-7}\\text{ m}}{2 \\times 0.95\\text{ m}} = \\frac{5.5 \\times 10^{-7}}{1.90} \\approx 2.895 \\times 10^{-7}\\text{ rad}$$\nConverting radians to arcseconds ($1\\text{ rad} = 206265''$):\n$$\\psi = 2.895 \\times 10^{-7} \\times 206265'' \\approx 0.0597'' \\approx 0.06''$$",
        "tags": ["Michelson stellar interferometer", "double star", "angular separation", "fringe visibility"]
    },
    {
        "id": "5.134",
        "title": "Angular Dispersion of a Grating at Normal and Oblique Incidence",
        "difficulty": 2,
        "question": "A transparent diffraction grating has a period $d = 1.50\\,\\mu\\text{m}$. Find the angular dispersion $D = d\\theta/d\\lambda$ (in angular minutes per nanometer) corresponding to the maximum of highest order for a spectral line of wavelength $\\lambda = 530\\text{ nm}$ falling on the grating:\n(a) at right angles;\n(b) at an angle $\\theta_0 = 45^\\circ$ to the normal.",
        "hints": [
            "(a) At normal incidence, $d \\sin\\theta = k \\lambda$. The angular dispersion is $D = \\frac{d\\theta}{d\\lambda} = \\frac{k}{d \\cos\\theta} = \\frac{k}{d \\sqrt{1 - (k\\lambda/d)^2}}$.",
            "(b) At oblique incidence, $d(\\sin\\theta - \\sin\\theta_0) = k \\lambda$, so $D = \\frac{k}{d \\cos\\theta} = \\frac{k}{d \\sqrt{1 - (\\sin\\theta_0 + k\\lambda/d)^2}}$.",
            "Convert radians per nanometer to angular minutes per nanometer: $1\\text{ rad} \\approx 3438\\text{ arcmin}$."
        ],
        "answer": "(a) $D = 6.5'\\text{/nm}$ (order $k = 2$);\n(b) $D = 13'\\text{/nm}$ (order $k = -4$)",
        "solution": "**1. Part (a): Normal Incidence:**\nThe grating equation is $d \\sin\\theta = k \\lambda$. Differentiating with respect to $\\lambda$:\n$$d \\cos\\theta \\frac{d\\theta}{d\\lambda} = k \\implies D = \\frac{d\\theta}{d\\lambda} = \\frac{k}{d \\cos\\theta} = \\frac{k}{d \\sqrt{1 - (k\\lambda/d)^2}}$$\nThe maximum observable order is:\n$$k_{\\text{max}} = \\left\\lfloor \\frac{d}{\\lambda} \\right\\rfloor = \\left\\lfloor \\frac{1.50}{0.530} \\right\\rfloor = 2$$\nFor $k = 2$:\n$$\\frac{k\\lambda}{d} = \\frac{2 \\times 0.530}{1.50} = 0.7067$$\n$$\\cos\\theta = \\sqrt{1 - 0.7067^2} = \\sqrt{1 - 0.4994} = 0.7075$$\n$$D = \\frac{2}{(1500\\text{ nm})(0.7075)} = \\frac{2}{1061.3}\\text{ rad/nm} \\approx 1.884 \\times 10^{-3}\\text{ rad/nm}$$\nConverting to arcmin/nm ($1\\text{ rad} = \\frac{180 \\times 60}{\\pi} \\approx 3437.75'$):\n$$D = (1.884 \\times 10^{-3})(3437.75) \\approx 6.48'\\text{/nm} \\approx 6.5'\\text{/nm}$$\n\n**2. Part (b): Oblique Incidence at $\\theta_0 = 45^\\circ$:**\nThe grating equation is $d(\\sin\\theta - \\sin\\theta_0) = k \\lambda$:\n$$\\sin\\theta = \\sin\\theta_0 + k \\frac{\\lambda}{d} = \\sin 45^\\circ + k \\left(\\frac{0.530}{1.50}\\right) = 0.7071 + 0.3533 k$$\nDifferentiating:\n$$D = \\frac{d\\theta}{d\\lambda} = \\frac{|k|}{d \\cos\\theta}$$\nFor the largest dispersion, we seek the maximum order with $\\cos\\theta$ closest to zero:\n- For negative $k$: $k = -4 \\implies \\sin\\theta = 0.7071 - 4(0.3533) = 0.7071 - 1.4133 = -0.7062$.\n  $$\\cos\\theta = \\sqrt{1 - (-0.7062)^2} = \\sqrt{1 - 0.4988} = 0.7080$$\n  $$D = \\frac{4}{(1500\\text{ nm})(0.7080)} = \\frac{4}{1062}\\text{ rad/nm} \\approx 3.766 \\times 10^{-3}\\text{ rad/nm}$$\n  In arcmin/nm:\n  $$D = (3.766 \\times 10^{-3})(3437.75) \\approx 12.95'\\text{/nm} \\approx 13'\\text{/nm}$$",
        "tags": ["angular dispersion", "diffraction grating", "highest order", "oblique incidence"]
    },
    {
        "id": "5.135",
        "title": "Angular Dispersion of a Grating as a Function of Diffraction Angle",
        "difficulty": 1,
        "question": "Light with wavelength $\\lambda$ falls on a diffraction grating at right angles. Find the angular dispersion $D = d\\theta/d\\lambda$ of the grating as a function of the diffraction angle $\\theta$.",
        "hints": [
            "Write the grating condition for normal incidence: $d \\sin\\theta = k \\lambda$.",
            "Differentiate both sides with respect to $\\lambda$ to obtain $d \\cos\\theta \\frac{d\\theta}{d\\lambda} = k$.",
            "Substitute $k = \\frac{d \\sin\\theta}{\\lambda}$ into the expression for $\\frac{d\\theta}{d\\lambda}$."
        ],
        "answer": "$D = \\frac{d\\theta}{d\\lambda} = \\frac{\\tan\\theta}{\\lambda}$",
        "solution": "**1. Derivation:**\nFor light falling normally on a grating of period $d$, the condition for the $k$-th diffraction maximum is:\n$$d \\sin\\theta = k \\lambda$$\nDifferentiating with respect to $\\lambda$:\n$$d \\cos\\theta \\, d\\theta = k \\, d\\lambda$$\nTherefore, the angular dispersion is:\n$$D = \\frac{d\\theta}{d\\lambda} = \\frac{k}{d \\cos\\theta}$$\n\n**2. Elimination of $k/d$:**\nFrom the grating equation, $\\frac{k}{d} = \\frac{\\sin\\theta}{\\lambda}$. Substituting this gives:\n$$D = \\frac{\\sin\\theta}{\\lambda \\cos\\theta} = \\frac{\\tan\\theta}{\\lambda}$$\nThis shows that the angular dispersion is solely a function of the diffraction angle $\\theta$ and the wavelength $\\lambda$, increasing rapidly as $\\theta \\to 90^\\circ$.",
        "tags": ["angular dispersion", "diffraction grating", "dispersion formula"]
    },
    {
        "id": "5.136",
        "title": "Angular Width of a Grating Principal Maximum",
        "difficulty": 2,
        "question": "Light with wavelength $\\lambda = 589.0\\text{ nm}$ falls normally on a diffraction grating with period $d = 2.5\\,\\mu\\text{m}$ comprising $N = 10000$ lines. Find the angular width $\\Delta\\theta$ of the diffraction maximum of second order ($k = 2$).",
        "hints": [
            "The angular half-width $\\delta\\theta$ of a principal maximum corresponds to the first zero of the $N$-slit interference factor: $N d \\cos\\theta \\, \\delta\\theta = \\lambda$.",
            "The total angular width between the first flanking minima is $\\Delta\\theta = 2 \\delta\\theta = \\frac{2\\lambda}{N d \\cos\\theta}$.",
            "Find $\\cos\\theta = \\sqrt{1 - (k\\lambda/d)^2}$ for $k = 2$, and convert $\\Delta\\theta$ from radians to arcseconds."
        ],
        "answer": "$\\Delta\\theta = \\frac{2\\lambda}{N d \\sqrt{1 - (k\\lambda/d)^2}} = 11''$",
        "solution": "**1. Angular Width Condition:**\nA principal maximum occurs at angle $\\theta$ where $d \\sin\\theta = k \\lambda$.\nThe first minimum on either side occurs at $\\theta \\pm \\delta\\theta$ such that:\n$$N d [\\sin(\\theta + \\delta\\theta) - \\sin\\theta] = \\lambda \\implies N d \\cos\\theta \\, \\delta\\theta = \\lambda$$\nThus, the total angular width of the principal peak between the first minima is:\n$$\\Delta\\theta = 2 \\delta\\theta = \\frac{2\\lambda}{N d \\cos\\theta}$$\n\n**2. Determining $\\cos\\theta$:**\nFor $k = 2$, $\\lambda = 0.589\\,\\mu\\text{m}$, and $d = 2.5\\,\\mu\\text{m}$:\n$$\\sin\\theta = \\frac{k\\lambda}{d} = \\frac{2 \\times 0.589}{2.5} = \\frac{1.178}{2.5} = 0.4712$$\n$$\\cos\\theta = \\sqrt{1 - \\sin^2\\theta} = \\sqrt{1 - (0.4712)^2} = \\sqrt{1 - 0.2220} = \\sqrt{0.7780} \\approx 0.8820$$\n\n**3. Numerical Evaluation:**\n$$N d = 10000 \\times (2.5 \\times 10^{-6}\\text{ m}) = 0.025\\text{ m}$$\n$$\\Delta\\theta = \\frac{2 (5.89 \\times 10^{-7}\\text{ m})}{(0.025\\text{ m})(0.8820)} = \\frac{1.178 \\times 10^{-6}}{0.02205} \\approx 5.342 \\times 10^{-5}\\text{ rad}$$\nConverting to arcseconds ($1\\text{ rad} = 206265''$):\n$$\\Delta\\theta = (5.342 \\times 10^{-5})(206265'') \\approx 11.02'' \\approx 11''$$",
        "tags": ["diffraction grating", "angular width", "resolving power", "Fraunhofer diffraction"]
    },
    {
        "id": "5.137",
        "title": "Upper Bound on Resolving Power of a Diffraction Grating",
        "difficulty": 2,
        "question": "Demonstrate that when light falls on a diffraction grating at right angles, the maximum resolving power of the grating cannot exceed the value $l / \\lambda$, where $l$ is the total width of the grating and $\\lambda$ is the wavelength of light.",
        "hints": [
            "The chromatic resolving power of a grating is defined as $R = \\frac{\\lambda}{\\delta\\lambda} = k N$, where $k$ is the diffraction order and $N$ is the total number of lines.",
            "From the grating condition for normal incidence, $d \\sin\\theta = k \\lambda$, with $|\\sin\\theta| \\le 1$, which gives $k \\le d / \\lambda$.",
            "Substitute $k \\le d / \\lambda$ into $R = k N$ and note that the total width of the grating is $l = N d$."
        ],
        "answer": "$R_{\\text{max}} = \\frac{l}{\\lambda}$",
        "solution": "**1. Definition of Resolving Power:**\nAccording to Rayleigh's criterion, the resolving power of a diffraction grating in the $k$-th order is:\n$$R = \\frac{\\lambda}{\\delta\\lambda} = k N$$\nwhere $N$ is the total number of slits (lines) illuminated.\n\n**2. Maximum Diffraction Order:**\nFor normal incidence, the diffraction angle $\\theta$ of order $k$ satisfies:\n$$d \\sin\\theta = k \\lambda \\implies k = \\frac{d \\sin\\theta}{\\lambda}$$\nSince the physical diffraction angle cannot exceed $90^\\circ$, we have $\\sin\\theta < 1$, which sets an upper bound on $k$:\n$$k < \\frac{d}{\\lambda}$$\n\n**3. Maximum Resolving Power:**\nSubstituting this inequality into the expression for resolving power:\n$$R = k N < \\left(\\frac{d}{\\lambda}\\right) N = \\frac{N d}{\\lambda}$$\nSince $N d = l$ is the total physical width of the ruling on the grating:\n$$R_{\\text{max}} \\le \\frac{l}{\\lambda}$$\nThus, the theoretical resolving power of any diffraction grating of width $l$ illuminated normally cannot exceed $l / \\lambda$.",
        "tags": ["diffraction grating", "resolving power", "theoretical limit", "Rayleigh criterion"]
    },
    {
        "id": "5.138",
        "title": "Resolving Power and Optical Path Difference / Wave Packet Duration",
        "difficulty": 2,
        "question": "Using a diffraction grating as an example, demonstrate that the frequency difference $\\delta\\nu$ of two spectral lines resolved according to Rayleigh's criterion is equal to the reciprocal of the propagation time difference $\\delta t$ of the extreme interfering oscillations: $\\delta\\nu = 1 / \\delta t$.",
        "hints": [
            "Express the resolving power $R = \\lambda / \\delta\\lambda$ in terms of frequency $\\nu = c / \\lambda$, using $\\delta\\nu / \\nu = \\delta\\lambda / \\lambda$.",
            "Calculate the maximum optical path difference $\\Delta$ between rays passing through the opposite extreme edges of the grating of total width $l = N d$ in order $k$: $\\Delta = l \\sin\\theta = k N \\lambda$.",
            "The difference in transit time between the extreme rays is $\\delta t = \\Delta / c$. Compare $\\delta t$ with $1 / \\delta\\nu$."
        ],
        "answer": "$\\delta\\nu = \\frac{1}{\\delta t}$",
        "solution": "**1. Relation Between Wavelength and Frequency Resolution:**\nThe frequency $\\nu$ and wavelength $\\lambda$ are related by $\\nu = c / \\lambda$. Differentiating:\n$$|\\delta\\nu| = \\frac{c}{\\lambda^2} \\delta\\lambda = \\nu \\frac{\\delta\\lambda}{\\lambda}$$\nTherefore, the resolving power is:\n$$R = \\frac{\\lambda}{\\delta\\lambda} = \\frac{\\nu}{\\delta\\nu} = k N$$\nSolving for the minimum resolved frequency difference:\n$$\\delta\\nu = \\frac{\\nu}{k N} = \\frac{c}{k N \\lambda}$$\n\n**2. Time Delay Between Extreme Interfering Rays:**\nConsider light diffracted at angle $\\theta$ corresponding to the $k$-th principal maximum ($d \\sin\\theta = k \\lambda$).\nThe path difference between rays originating from the two extreme edges of the grating of width $l = N d$ is:\n$$\\Delta = l \\sin\\theta = (N d) \\sin\\theta = N (d \\sin\\theta) = N (k \\lambda) = k N \\lambda$$\nThe difference in propagation time between these extreme rays is:\n$$\\delta t = \\frac{\\Delta}{c} = \\frac{k N \\lambda}{c}$$\n\n**3. Conclusion:**\nComparing the two expressions:\n$$\\delta\\nu = \\frac{c}{k N \\lambda} = \\frac{1}{\\delta t}$$\nThis fundamental relationship shows that the spectral resolution is governed by the time span over which interference takes place, completely analogous to the Fourier uncertainty principle $\\Delta\\nu \\,\\Delta t \\sim 1$.",
        "tags": ["diffraction grating", "Rayleigh criterion", "wave packet", "Fourier relation", "transit time"]
    },
    {
        "id": "5.139",
        "title": "Diffraction Angle for Resolving Close Spectral Lines",
        "difficulty": 2,
        "question": "Light composed of two spectral lines with wavelengths $\\lambda_1 = 600.000\\text{ nm}$ and $\\lambda_2 = 600.050\\text{ nm}$ falls normally on a diffraction grating of width $l = 10.0\\text{ mm}$. At a certain diffraction angle $\\theta$ these lines are close to being resolved according to Rayleigh's criterion. Find $\\theta$.",
        "hints": [
            "The required resolving power to separate $\\lambda_1$ and $\\lambda_2$ is $R = \\frac{\\lambda}{\\delta\\lambda}$.",
            "According to Rayleigh's criterion, $R = k N$. Multiply by $\\lambda$: $k N \\lambda = R \\lambda$.",
            "From the grating condition, $d \\sin\\theta = k \\lambda \\implies N d \\sin\\theta = k N \\lambda = l \\sin\\theta$. Thus, $\\sin\\theta = \\frac{R \\lambda}{l} = \\frac{\\lambda^2}{l \\,\\delta\\lambda}$."
        ],
        "answer": "$\\theta = \\arcsin\\left(\\frac{\\lambda^2}{l \\,\\delta\\lambda}\\right) \\approx 46^\\circ$",
        "solution": "**1. Required Resolving Power:**\nFor the two lines $\\lambda_1 = 600.000\\text{ nm}$ and $\\lambda_2 = 600.050\\text{ nm}$, the mean wavelength is $\\lambda \\approx 600.0\\text{ nm}$ and the wavelength separation is $\\delta\\lambda = 0.050\\text{ nm}$.\nThe required resolving power is:\n$$R = \\frac{\\lambda}{\\delta\\lambda} = \\frac{600.0\\text{ nm}}{0.050\\text{ nm}} = 12000$$\n\n**2. Relation to Diffraction Angle:**\nBy Rayleigh's criterion, the lines are just resolved when:\n$$k N = R$$\nFor normal incidence, the grating equation gives:\n$$d \\sin\\theta = k \\lambda$$\nMultiplying both sides by the total number of lines $N$:\n$$N d \\sin\\theta = k N \\lambda$$\nSince $N d = l$ is the width of the grating and $k N = R$:\n$$l \\sin\\theta = R \\lambda = \\frac{\\lambda^2}{\\delta\\lambda}$$\n$$\\sin\\theta = \\frac{R \\lambda}{l} = \\frac{\\lambda^2}{l \\,\\delta\\lambda}$$\n\n**3. Numerical Evaluation:**\nGiven $l = 10.0\\text{ mm} = 1.00 \\times 10^{-2}\\text{ m}$, $\\lambda = 6.00 \\times 10^{-7}\\text{ m}$, and $R = 12000$:\n$$\\sin\\theta = \\frac{12000 \\times (6.00 \\times 10^{-7}\\text{ m})}{1.00 \\times 10^{-2}\\text{ m}} = \\frac{7.20 \\times 10^{-3}}{1.00 \\times 10^{-2}} = 0.720$$\n$$\\theta = \\arcsin(0.720) \\approx 46.05^\\circ \\approx 46^\\circ$$",
        "tags": ["diffraction grating", "resolving power", "Rayleigh criterion", "diffraction angle"]
    },
    {
        "id": "5.140",
        "title": "Resolving Order and Minimum Resolvable Wavelength Difference",
        "difficulty": 2,
        "question": "Light falls normally on a transparent diffraction grating of width $l = 6.5\\text{ cm}$ with $n_0 = 200\\text{ lines/mm}$. The spectrum under investigation includes a spectral line with $\\lambda = 670.8\\text{ nm}$ consisting of two components differing by $\\delta\\lambda = 0.015\\text{ nm}$. Find:\n(a) in what order of the spectrum these components will be resolved;\n(b) the least difference of wavelengths $\\delta\\lambda_{\\text{min}}$ that can be resolved by this grating in the wavelength region $\\lambda \\approx 670\\text{ nm}$.",
        "hints": [
            "(a) Find the total number of lines $N = n_0 l$. The required resolving power is $R = \\lambda / \\delta\\lambda$. The minimum order is the smallest integer $k \\ge R / N$.",
            "(b) The theoretical maximum resolving power is $R_{\\text{max}} = l / \\lambda$ (or $k_{\\text{max}} N$ with $k_{\\text{max}} = \\lfloor d/\\lambda \\rfloor$).",
            "The least resolvable wavelength difference is $\\delta\\lambda_{\\text{min}} = \\frac{\\lambda}{R_{\\text{max}}} \\approx \\frac{\\lambda^2}{l}$."
        ],
        "answer": "(a) In the fourth order ($k = 4$);\n(b) $\\delta\\lambda_{\\text{min}} \\approx \\frac{\\lambda^2}{l} \\approx 7\\text{ pm}$",
        "solution": "**1. Part (a): Order of Spectrum to Resolve Components:**\nThe total number of lines on the grating is:\n$$N = n_0 l = (200\\text{ mm}^{-1})(65\\text{ mm}) = 13000$$\nThe required chromatic resolving power is:\n$$R = \\frac{\\lambda}{\\delta\\lambda} = \\frac{670.8\\text{ nm}}{0.015\\text{ nm}} = 44720$$\nAccording to Rayleigh's criterion, $R = k N$, so:\n$$k \\ge \\frac{R}{N} = \\frac{44720}{13000} \\approx 3.44$$\nSince the diffraction order $k$ must be an integer, the components will be resolved beginning in the fourth order ($k = 4$).\n\n**2. Part (b): Minimum Resolvable Wavelength Difference:**\nThe grating period is $d = 1 / n_0 = 1 / (200\\text{ mm}^{-1}) = 5.0\\,\\mu\\text{m}$.\nThe maximum observable diffraction order is:\n$$k_{\\text{max}} = \\left\\lfloor \\frac{d}{\\lambda} \\right\\rfloor = \\left\\lfloor \\frac{5.0\\,\\mu\\text{m}}{0.6708\\,\\mu\\text{m}} \\right\\rfloor = 7$$\nThe maximum theoretical resolving power is:\n$$R_{\\text{max}} \\approx \\frac{l}{\\lambda}$$\nThus, the least resolvable wavelength difference is:\n$$\\delta\\lambda_{\\text{min}} = \\frac{\\lambda}{R_{\\text{max}}} \\approx \\frac{\\lambda^2}{l}$$\nSubstituting numerical values:\n$$\\delta\\lambda_{\\text{min}} \\approx \\frac{(670.8 \\times 10^{-9}\\text{ m})^2}{0.065\\text{ m}} = \\frac{4.50 \\times 10^{-13}}{0.065} \\approx 6.92 \\times 10^{-12}\\text{ m} \\approx 7\\text{ pm}$$",
        "tags": ["diffraction grating", "resolving power", "spectral order", "picometers"]
    },
    {
        "id": "5.141",
        "title": "Period and Width of Grating from Sodium Doublet Resolution",
        "difficulty": 2,
        "question": "With light falling normally on a transparent diffraction grating $l_1 = 10\\text{ mm}$ wide, it was found that the components of the yellow line of sodium ($589.0$ and $589.6\\text{ nm}$) are resolved beginning with the fifth order of the spectrum ($k_1 = 5$). Evaluate:\n(a) the period $d$ of this grating;\n(b) what must be the width $l_2$ of the grating with the same period for a doublet $\\lambda = 460.0\\text{ nm}$ whose components differ by $\\delta\\lambda = 0.13\\text{ nm}$ to be resolved in the third order of the spectrum ($k_2 = 3$).",
        "hints": [
            "(a) For sodium yellow line, $\\lambda_1 \\approx 589.3\\text{ nm}$ and $\\delta\\lambda_1 = 0.6\\text{ nm}$. The resolving power is $R_1 = \\lambda_1 / \\delta\\lambda_1 = k_1 N_1$. Find $N_1$, then $d = l_1 / N_1$.",
            "(b) For the second doublet, required resolving power is $R_2 = \\lambda_2 / \\delta\\lambda_2 = k_2 N_2$. Find $N_2 = R_2 / k_2$.",
            "The required grating width is $l_2 = N_2 d$."
        ],
        "answer": "(a) $d \\approx 0.05\\text{ mm}$;\n(b) $l \\approx 6\\text{ cm}$",
        "solution": "**1. Part (a): Period of the Grating:**\nFor the sodium doublet:\n$$\\lambda_1 = 589.3\\text{ nm}, \\quad \\delta\\lambda_1 = 589.6 - 589.0 = 0.6\\text{ nm}$$\nThe required resolving power is:\n$$R_1 = \\frac{\\lambda_1}{\\delta\\lambda_1} = \\frac{589.3}{0.6} \\approx 982$$\nSince this doublet is resolved beginning in order $k_1 = 5$:\n$$k_1 N_1 = R_1 \\implies N_1 = \\frac{R_1}{k_1} = \\frac{982}{5} \\approx 196.4 \\approx 200\\text{ lines}$$\nThe period of the grating is:\n$$d = \\frac{l_1}{N_1} = \\frac{10\\text{ mm}}{200} = 0.05\\text{ mm}$$\n\n**2. Part (b): Width of Grating for the Second Doublet:**\nFor $\\lambda_2 = 460.0\\text{ nm}$ and $\\delta\\lambda_2 = 0.13\\text{ nm}$:\n$$R_2 = \\frac{\\lambda_2}{\\delta\\lambda_2} = \\frac{460.0}{0.13} \\approx 3538$$\nTo resolve this in the third order ($k_2 = 3$):\n$$N_2 = \\frac{R_2}{k_2} = \\frac{3538}{3} \\approx 1179 \\approx 1180\\text{ lines}$$\nThe required width of the grating is:\n$$l_2 = N_2 d = 1180 \\times 0.05\\text{ mm} = 59\\text{ mm} \\approx 6\\text{ cm}$$",
        "tags": ["diffraction grating", "resolving power", "sodium doublet", "grating period"]
    },
    {
        "id": "5.142",
        "title": "Doublet Separation and Resolution in a Quartz Spectrograph",
        "difficulty": 2,
        "question": "A transparent diffraction grating of a quartz spectrograph is $l = 25\\text{ mm}$ wide and has $n_0 = 250\\text{ lines/mm}$. The focal length of an objective in whose focal plane a photographic plate is located is $F = 80\\text{ cm}$. Light falls on the grating at right angles. The spectrum under investigation includes a doublet with components $\\lambda_1 = 310.154\\text{ nm}$ and $\\lambda_2 = 310.184\\text{ nm}$ ($\\delta\\lambda = 0.030\\text{ nm}$). Determine:\n(a) the distances on the photographic plate between the components of this doublet in the spectra of the first and the second order;\n(b) whether these components will be resolved in these orders of the spectrum.",
        "hints": [
            "(a) Linear dispersion is $\\frac{\\Delta x}{\\delta\\lambda} = F D = \\frac{F k}{d \\cos\\theta} \\approx \\frac{F k}{d}$ for small diffraction angles. Calculate $\\Delta x$ for $k = 1$ and $k = 2$.",
            "(b) Total number of lines is $N = n_0 l = 250 \\times 25 = 6250$.",
            "The required resolving power is $R = \\lambda / \\delta\\lambda$. Compare $R$ with $k N$ for $k = 1$ and $k = 2$."
        ],
        "answer": "(a) $6\\,\\mu\\text{m}$ (first order) and $12\\,\\mu\\text{m}$ (second order);\n(b) Not resolved in the first order, resolved in the second order",
        "solution": "**1. Grating Characteristics:**\nPeriod of grating: $d = \\frac{1}{n_0} = \\frac{1}{250\\text{ mm}^{-1}} = 4.0 \\times 10^{-3}\\text{ mm} = 4.0\\,\\mu\\text{m}$.\nTotal number of lines: $N = n_0 l = (250\\text{ mm}^{-1})(25\\text{ mm}) = 6250$.\nMean wavelength: $\\lambda \\approx 310.17\\text{ nm}$, difference $\\delta\\lambda = 0.030\\text{ nm}$.\n\n**2. Part (a): Linear Separation on the Photographic Plate:**\nThe angular dispersion for small diffraction angles is $D = \\frac{d\\theta}{d\\lambda} \\approx \\frac{k}{d}$.\nThe separation on the focal plane is:\n$$\\Delta x = F \\Delta\\theta = F D \\delta\\lambda = \\frac{F k \\delta\\lambda}{d}$$\n- **First order ($k = 1$):**\n  $$\\Delta x_1 = \\frac{(0.80\\text{ m})(1)(0.030 \\times 10^{-9}\\text{ m})}{4.0 \\times 10^{-6}\\text{ m}} = \\frac{2.40 \\times 10^{-11}}{4.0 \\times 10^{-6}} = 6.0 \\times 10^{-6}\\text{ m} = 6\\,\\mu\\text{m}$$\n- **Second order ($k = 2$):**\n  $$\\Delta x_2 = 2 \\Delta x_1 = 12\\,\\mu\\text{m}$$\n\n**3. Part (b): Resolving Power Check:**\nThe required resolving power is:\n$$R_{\\text{req}} = \\frac{\\lambda}{\\delta\\lambda} = \\frac{310.17\\text{ nm}}{0.030\\text{ nm}} \\approx 10339$$\nThe available resolving power in order $k$ is $R_k = k N$:\n- For $k = 1$: $R_1 = 1 \\times 6250 = 6250 < 10339$ (not resolved!).\n- For $k = 2$: $R_2 = 2 \\times 6250 = 12500 > 10339$ (resolved!).",
        "tags": ["quartz spectrograph", "linear dispersion", "resolving power", "diffraction grating"]
    },
    {
        "id": "5.143",
        "title": "Resolving Power of a Prism Spectrograph (Rayleigh Criterion Derivation)",
        "difficulty": 3,
        "question": "The ultimate resolving power $\\lambda / \\delta\\lambda$ of a spectrograph's trihedral prism is determined by diffraction of light at the prism edges. When the prism is oriented at the angle of minimum deviation, show that according to Rayleigh's criterion:\n$$R = \\frac{\\lambda}{\\delta\\lambda} = b \\left|\\frac{dn}{d\\lambda}\\right|$$\nwhere $b$ is the width of the prism's base, and $dn/d\\lambda$ is the dispersion of its material.",
        "hints": [
            "Consider two extreme rays: one passing through the prism's apex (zero path in glass) and one passing through its base (path length $b$ in glass of refractive index $n$).",
            "At the angle of minimum deviation, the wavefront remains planar, and the optical path difference between the extreme rays is zero for wavelength $\\lambda$.",
            "For a nearby wavelength $\\lambda + \\delta\\lambda$, the refractive index changes to $n + \\delta n$. According to Rayleigh's criterion, the first diffraction minimum occurs when the additional optical path difference between the extreme rays is equal to $\\lambda$: $b |\\delta n| = \\lambda$."
        ],
        "answer": "Derivation: $b |\\delta n| = \\lambda \\implies \\frac{\\lambda}{\\delta\\lambda} = b \\left|\\frac{dn}{d\\lambda}\\right|$",
        "solution": "**1. Wavefronts and Optical Paths at Minimum Deviation:**\nConsider a monochromatic plane wave of wavelength $\\lambda$ incident on a symmetric trihedral prism at the angle of minimum deviation.\nLet ray 1 pass through the apex of the prism (path in glass is zero, with air path $L_{\\text{air}}$), while ray 2 passes along the base of the prism (path length in glass is $b$, with zero air path between the same conjugate wavefronts).\nBecause all rays emerging from the prism form an unperturbed plane wavefront perpendicular to the emergent beam, Fermat's principle requires that the optical paths between conjugate wavefronts be equal:\n$$\\Phi(\\lambda) = n(\\lambda) b - L_{\\text{air}} = 0$$\n\n**2. Perturbation for Wavelength $\\lambda + \\delta\\lambda$:**\nFor a neighbouring spectral line with wavelength $\\lambda + \\delta\\lambda$, the refractive index of the prism is $n + \\delta n$, where $\\delta n = \\frac{dn}{d\\lambda} \\delta\\lambda$.\nThe optical path along the apex ray does not change (it travels in air), while the optical path along the base ray increases by:\n$$\\delta\\Phi = b \\,\\delta n = b \\left|\\frac{dn}{d\\lambda}\\right| \\delta\\lambda$$\nThis introduces a phase tilt across the emergent beam aperture.\n\n**3. Rayleigh Criterion:**\nBy Rayleigh's criterion, two spectral lines are resolved when the principal maximum of $\\lambda + \\delta\\lambda$ falls on the first diffraction minimum of the pattern of wavelength $\\lambda$.\nFor an aperture defined by the prism base, the first diffraction minimum occurs when the optical path difference between the extreme rays of the beam equals one wavelength:\n$$\\delta\\Phi = \\lambda$$\n$$b \\left|\\frac{dn}{d\\lambda}\\right| \\delta\\lambda = \\lambda$$\nDividing by $\\delta\\lambda$ gives the resolving power of the prism:\n$$R = \\frac{\\lambda}{\\delta\\lambda} = b \\left|\\frac{dn}{d\\lambda}\\right|$$\nThis fundamental formula shows that the resolving power of a prism depends only on the width of its base $b$ and the dispersion $|dn/d\\lambda|$ of the prism material, independent of the prism angle.",
        "tags": ["prism spectrograph", "resolving power", "Rayleigh criterion", "dispersion", "derivation"]
    },
    {
        "id": "5.144",
        "title": "Resolving Power of a Prism with Cauchy Dispersion",
        "difficulty": 2,
        "question": "A spectrograph's trihedral prism is manufactured from glass whose refractive index varies with wavelength as $n = A + B/\\lambda^2$, where $A$ and $B$ are constants with $B = 0.010\\,\\mu\\text{m}^2$.\n(a) Find how the resolving power depends on $\\lambda$, and calculate $\\lambda / \\delta\\lambda$ in the vicinity of $\\lambda_1 = 434\\text{ nm}$ and $\\lambda_2 = 656\\text{ nm}$ if the width of the prism's base is $b = 5.0\\text{ cm}$;\n(b) Find the width of the prism's base capable of resolving the yellow sodium doublet ($589.0$ and $589.6\\text{ nm}$).",
        "hints": [
            "(a) Compute the dispersion $|dn/d\\lambda| = \\frac{2B}{\\lambda^3}$. The resolving power is $R = b |dn/d\\lambda| = \\frac{2 b B}{\\lambda^3}$.",
            "Substitute $\\lambda_1 = 0.434\\,\\mu\\text{m}$ and $\\lambda_2 = 0.656\\,\\mu\\text{m}$ with $b = 5.0\\times 10^4\\,\\mu\\text{m}$.",
            "(b) For the sodium doublet, $R = \\lambda / \\delta\\lambda = 589.3 / 0.6 \\approx 982$. Solve for $b = \\frac{R \\lambda^3}{2 B}$."
        ],
        "answer": "(a) $R = \\frac{2 b B}{\\lambda^3}$; $R_1 = 1.2 \\times 10^4$ and $R_2 = 0.35 \\times 10^4$;\n(b) $b = 1.0\\text{ cm}$",
        "solution": "**1. Part (a): Resolving Power Formula and Calculations:**\nThe refractive index is given by Cauchy's formula:\n$$n(\\lambda) = A + \\frac{B}{\\lambda^2}$$\nDifferentiating with respect to $\\lambda$:\n$$\\left|\\frac{dn}{d\\lambda}\\right| = \\frac{2B}{\\lambda^3}$$\nUsing the prism resolving power formula $R = b |dn/d\\lambda|$:\n$$R = \\frac{\\lambda}{\\delta\\lambda} = \\frac{2 b B}{\\lambda^3}$$\nWith $b = 5.0\\text{ cm} = 5.0 \\times 10^4\\,\\mu\\text{m}$ and $B = 0.010\\,\\mu\\text{m}^2$:\n$$2 b B = 2 (5.0 \\times 10^4\\,\\mu\\text{m})(0.010\\,\\mu\\text{m}^2) = 1000\\,\\mu\\text{m}^3$$\n- For $\\lambda_1 = 434\\text{ nm} = 0.434\\,\\mu\\text{m}$:\n  $$\\lambda_1^3 = (0.434)^3 \\approx 0.0818\\,\\mu\\text{m}^3$$\n  $$R_1 = \\frac{1000}{0.0818} \\approx 12225 \\approx 1.2 \\times 10^4$$\n- For $\\lambda_2 = 656\\text{ nm} = 0.656\\,\\mu\\text{m}$:\n  $$\\lambda_2^3 = (0.656)^3 \\approx 0.2821\\,\\mu\\text{m}^3$$\n  $$R_2 = \\frac{1000}{0.2821} \\approx 3545 \\approx 0.35 \\times 10^4$$\n\n**2. Part (b): Prism Base Width for Sodium Doublet:**\nFor the sodium doublet ($\\lambda = 589.3\\text{ nm} = 0.5893\\,\\mu\\text{m}$, $\\delta\\lambda = 0.6\\text{ nm}$):\n$$R = \\frac{589.3}{0.6} \\approx 982$$\nSetting $R = \\frac{2 b B}{\\lambda^3}$ and solving for $b$:\n$$b = \\frac{R \\lambda^3}{2 B} = \\frac{982 \\times (0.5893\\,\\mu\\text{m})^3}{2 \\times 0.010\\,\\mu\\text{m}^2}$$\n$$(0.5893)^3 \\approx 0.2046$$\n$$b = \\frac{982 \\times 0.2046}{0.020} = \\frac{200.9}{0.020} \\approx 10045\\,\\mu\\text{m} \\approx 1.0\\text{ cm}$$",
        "tags": ["prism spectrograph", "resolving power", "Cauchy formula", "sodium doublet"]
    },
    {
        "id": "5.145",
        "title": "Base Width of a Prism Matching Grating Resolving Power",
        "difficulty": 2,
        "question": "How wide is the base $b$ of a trihedral prism which has the same resolving power as a diffraction grating with $N = 10000$ lines in the second order of the spectrum if $|dn/d\\lambda| = 0.10\\,\\mu\\text{m}^{-1}$?",
        "hints": [
            "The resolving power of the diffraction grating in the second order ($k = 2$) is $R = k N = 2 \\times 10000 = 20000$.",
            "The resolving power of a prism is $R = b |dn/d\\lambda|$.",
            "Equate the two resolving powers and solve for $b = R / |dn/d\\lambda|$."
        ],
        "answer": "$b = \\frac{k N}{|dn/d\\lambda|} = 20\\text{ cm}$",
        "solution": "**1. Resolving Power of the Grating:**\nFor a diffraction grating with $N = 10000$ lines operating in the second order ($k = 2$):\n$$R_{\\text{grating}} = k N = 2 \\times 10000 = 20000$$\n\n**2. Resolving Power of the Prism:**\nFor a prism with base width $b$ and dispersion $|dn/d\\lambda|$:\n$$R_{\\text{prism}} = b \\left|\\frac{dn}{d\\lambda}\\right|$$\n\n**3. Equating Resolving Powers:**\n$$b \\left|\\frac{dn}{d\\lambda}\\right| = k N \\implies b = \\frac{k N}{|dn/d\\lambda|}$$\nGiven $|dn/d\\lambda| = 0.10\\,\\mu\\text{m}^{-1} = 10^5\\text{ m}^{-1}$:\n$$b = \\frac{20000}{0.10\\,\\mu\\text{m}^{-1}} = 2.0 \\times 10^5\\,\\mu\\text{m} = 0.20\\text{ m} = 20\\text{ cm}$$",
        "tags": ["prism", "diffraction grating", "resolving power", "comparison"]
    },
    {
        "id": "5.146",
        "title": "Telescope Resolving Power and Ground Linear Resolution",
        "difficulty": 2,
        "question": "A telescope has an objective with diameter $D = 5.0\\text{ cm}$. Find the resolving power of the objective and the minimum separation $\\Delta y_{\\text{min}}$ between two points at distance $l = 3.0\\text{ km}$ from the telescope that it can resolve (assume $\\lambda = 0.55\\,\\mu\\text{m}$).",
        "hints": [
            "According to Rayleigh's criterion, the angular resolution limit of a circular objective is $\\delta\\psi = 1.22 \\frac{\\lambda}{D}$.",
            "The resolving power of the objective is defined as $R = \\frac{1}{\\delta\\psi} = \\frac{D}{1.22\\lambda}$.",
            "The minimum linear separation at distance $l$ is $\\Delta y_{\\text{min}} = l \\,\\delta\\psi = 1.22 \\frac{l \\lambda}{D}$."
        ],
        "answer": "$R \\approx 7 \\times 10^4$, $\\Delta y_{\\text{min}} \\approx 4\\text{ cm}$",
        "solution": "**1. Angular Resolution of Circular Objective:**\nDiffraction at a circular aperture of diameter $D$ yields an Airy disk whose first dark ring has angular radius given by Rayleigh's criterion:\n$$\\delta\\psi = 1.22 \\frac{\\lambda}{D}$$\n\n**2. Resolving Power of the Objective:**\nThe resolving power is defined as the reciprocal of the angular limit of resolution:\n$$R = \\frac{1}{\\delta\\psi} = \\frac{D}{1.22 \\lambda}$$\nSubstituting $D = 5.0\\text{ cm} = 0.050\\text{ m}$ and $\\lambda = 0.55\\,\\mu\\text{m} = 5.5 \\times 10^{-7}\\text{ m}$:\n$$R = \\frac{0.050}{1.22 \\times (5.5 \\times 10^{-7})} = \\frac{0.050}{6.71 \\times 10^{-7}} \\approx 7.45 \\times 10^4 \\approx 7 \\times 10^4$$\n\n**3. Minimum Linear Separation:**\nAt a distance $l = 3.0\\text{ km} = 3000\\text{ m}$:\n$$\\Delta y_{\\text{min}} = l \\,\\delta\\psi = \\frac{l}{R} = \\frac{3000\\text{ m}}{7.45 \\times 10^4} \\approx 0.040\\text{ m} = 4\\text{ cm}$$",
        "tags": ["telescope", "resolving power", "Rayleigh criterion", "Airy disk", "linear resolution"]
    },
    {
        "id": "5.147",
        "title": "Lunar Surface Resolution of a Reflecting Telescope",
        "difficulty": 2,
        "question": "Calculate the minimum separation $\\Delta x_{\\text{min}}$ between two points on the Moon which can be resolved by a reflecting telescope with mirror diameter $D = 5.0\\text{ m}$. Assume the wavelength of light is $\\lambda = 0.55\\,\\mu\\text{m}$, and the distance to the Moon is $L = 384000\\text{ km}$.",
        "hints": [
            "Use Rayleigh's criterion for a circular aperture: $\\delta\\psi = 1.22 \\frac{\\lambda}{D}$.",
            "The minimum resolvable linear distance on the Moon is $\\Delta x_{\\text{min}} = L \\,\\delta\\psi = 1.22 \\frac{L \\lambda}{D}$.",
            "Substitute $L = 3.84 \\times 10^8\\text{ m}$, $\\lambda = 5.5 \\times 10^{-7}\\text{ m}$, and $D = 5.0\\text{ m}$."
        ],
        "answer": "$\\Delta x_{\\text{min}} = 1.22 \\frac{L \\lambda}{D} \\approx 50\\text{ m}$",
        "solution": "**1. Angular Limit of Resolution:**\nAccording to Rayleigh's criterion for a circular aperture of diameter $D$:\n$$\\delta\\psi = 1.22 \\frac{\\lambda}{D}$$\n\n**2. Linear Resolution on the Lunar Surface:**\nFor a distance $L$ from Earth to the Moon:\n$$\\Delta x_{\\text{min}} = L \\,\\delta\\psi = 1.22 \\frac{L \\lambda}{D}$$\n\n**3. Numerical Evaluation:**\nGiven $D = 5.0\\text{ m}$, $\\lambda = 0.55\\,\\mu\\text{m} = 5.5 \\times 10^{-7}\\text{ m}$, and $L = 3.84 \\times 10^8\\text{ m}$:\n$$\\Delta x_{\\text{min}} = 1.22 \\times \\frac{(3.84 \\times 10^8\\text{ m})(5.5 \\times 10^{-7}\\text{ m})}{5.0\\text{ m}}$$\n$$(3.84 \\times 10^8)(5.5 \\times 10^{-7}) = 211.2\\text{ m}^2$$\n$$\\Delta x_{\\text{min}} = \\frac{1.22 \\times 211.2}{5.0} = \\frac{257.66}{5.0} \\approx 51.5\\text{ m} \\approx 50\\text{ m}$$",
        "tags": ["reflecting telescope", "Moon", "Rayleigh criterion", "linear resolution"]
    },
    {
        "id": "5.148",
        "title": "Minimum Useful Magnification of a Telescope",
        "difficulty": 2,
        "question": "Determine the minimum magnification $\\Gamma_{\\text{min}}$ of a telescope with objective diameter $D = 5.0\\text{ cm}$ with which the resolving power of the objective is totally employed, if the diameter of the eye's pupil is $d_0 = 4.0\\text{ mm}$.",
        "hints": [
            "The angular limit of resolution of the objective is $\\delta\\psi = 1.22 \\lambda / D$.",
            "The angular limit of resolution of the human eye with pupil diameter $d_0$ is $\\delta\\psi' = 1.22 \\lambda / d_0$.",
            "To fully utilize the objective's resolving power, the telescope magnification $\\Gamma$ must satisfy $\\Gamma \\,\\delta\\psi \\ge \\delta\\psi'$, giving $\\Gamma_{\\text{min}} = \\delta\\psi' / \\delta\\psi = D / d_0$."
        ],
        "answer": "$\\Gamma_{\\text{min}} = \\frac{D}{d_0} \\approx 13$",
        "solution": "**1. Resolving Limits of Telescope and Eye:**\n- Angular limit of resolution of the telescope objective:\n  $$\\delta\\psi = 1.22 \\frac{\\lambda}{D}$$\n- Angular limit of resolution of the observer's eye with pupil diameter $d_0$:\n  $$\\delta\\psi' = 1.22 \\frac{\\lambda}{d_0}$$\n\n**2. Condition for Full Utilization (Normal Magnification):**\nWhen looking through the telescope, two points separated by angular angle $\\delta\\psi$ subtend an angle $\\Gamma \\,\\delta\\psi$ at the observer's eye.\nFor the eye to resolve these two points, we require:\n$$\\Gamma \\,\\delta\\psi \\ge \\delta\\psi'$$\n$$\\Gamma_{\\text{min}} = \\frac{\\delta\\psi'}{\\delta\\psi} = \\frac{1.22 \\lambda / d_0}{1.22 \\lambda / D} = \\frac{D}{d_0}$$\n(This is also known as the normal magnification, at which the exit pupil of the telescope matches the entrance pupil of the eye).\n\n**3. Numerical Evaluation:**\nGiven $D = 5.0\\text{ cm} = 50\\text{ mm}$ and $d_0 = 4.0\\text{ mm}$:\n$$\\Gamma_{\\text{min}} = \\frac{50\\text{ mm}}{4.0\\text{ mm}} = 12.5 \\approx 13$$",
        "tags": ["telescope", "normal magnification", "useful magnification", "resolving power", "pupil diameter"]
    },
    {
        "id": "5.149",
        "title": "Microscope Resolution Limit from Numerical Aperture",
        "difficulty": 1,
        "question": "A microscope has an objective whose numerical aperture is $\\sin\\alpha = 0.24$, where $\\alpha$ is the half-angle subtended by the objective rim. Find the minimum separation $d_{\\text{min}}$ resolved by this microscope when an object is illuminated by light with wavelength $\\lambda = 0.55\\,\\mu\\text{m}$.",
        "hints": [
            "Recall Abbe's and Rayleigh's resolution criterion for a microscope objective: $d_{\\text{min}} = \\frac{0.61 \\lambda}{\\sin\\alpha}$ (or $\\frac{\\lambda}{2 \\sin\\alpha}$ for coherent illumination).",
            "Substitute $\\lambda = 0.55\\,\\mu\\text{m}$ and $\\sin\\alpha = 0.24$ directly into $d_{\\text{min}} = \\frac{0.61 \\lambda}{\\sin\\alpha}$."
        ],
        "answer": "$d_{\\text{min}} = \\frac{0.61 \\lambda}{\\sin\\alpha} = 1.4\\,\\mu\\text{m}$",
        "solution": "**1. Resolution Criterion for a Microscope:**\nAccording to the Abbe-Rayleigh criterion for an optical microscope, the minimum transverse distance between two self-luminous or incoherently illuminated object points that can be resolved is:\n$$d_{\\text{min}} = \\frac{0.61 \\lambda}{n \\sin\\alpha}$$\nFor an objective working in air ($n = 1$):\n$$d_{\\text{min}} = \\frac{0.61 \\lambda}{\\sin\\alpha}$$\nwhere $\\sin\\alpha$ is the numerical aperture of the objective.\n\n**2. Numerical Evaluation:**\nGiven $\\lambda = 0.55\\,\\mu\\text{m}$ and $\\sin\\alpha = 0.24$:\n$$d_{\\text{min}} = \\frac{0.61 \\times 0.55\\,\\mu\\text{m}}{0.24} = \\frac{0.3355}{0.24} \\approx 1.398\\,\\mu\\text{m} \\approx 1.4\\,\\mu\\text{m}$$",
        "tags": ["microscope", "resolving power", "numerical aperture", "Abbe criterion"]
    },
    {
        "id": "5.150",
        "title": "Minimum Useful Magnification of a Microscope",
        "difficulty": 2,
        "question": "Find the minimum magnification $\\Gamma_{\\text{min}}$ of a microscope whose objective numerical aperture is $\\sin\\alpha = 0.24$, at which the resolving power of the objective is totally employed if the diameter of the eye's pupil is $d_0 = 4.0\\text{ mm}$ and the distance of distinct vision is $l_0 = 25\\text{ cm}$.",
        "hints": [
            "The minimum distance resolved by the microscope objective is $d_{\\text{min}} = \\frac{0.61 \\lambda}{\\sin\\alpha}$.",
            "When viewed at the distance of most distinct vision $l_0$, this separation subtends an angular size $\\delta\\psi = \\frac{d_{\\text{min}}}{l_0}$.",
            "The angular limit of resolution of the human eye is $\\delta\\psi' = \\frac{1.22 \\lambda}{d_0}$. The required magnification is $\\Gamma_{\\text{min}} = \\frac{\\delta\\psi'}{\\delta\\psi} = \\frac{2 l_0 \\sin\\alpha}{d_0}$."
        ],
        "answer": "$\\Gamma_{\\text{min}} = \\frac{2 l_0 \\sin\\alpha}{d_0} = 30$",
        "solution": "**1. Angular Separation and Resolving Power:**\nThe minimum distance resolved by the microscope objective is:\n$$d_{\\text{min}} = \\frac{0.61 \\lambda}{\\sin\\alpha}$$\nWhen viewed by the unaided eye from the distance of most distinct vision $l_0 = 25\\text{ cm}$, two points separated by $d_{\\text{min}}$ would subtend an angular angle:\n$$\\delta\\psi = \\frac{d_{\\text{min}}}{l_0} = \\frac{0.61 \\lambda}{l_0 \\sin\\alpha}$$\n\n**2. Eye's Limit of Resolution:**\nThe angular resolution of the eye with pupil diameter $d_0$ is:\n$$\\delta\\psi' = 1.22 \\frac{\\lambda}{d_0}$$\n\n**3. Minimum Useful Magnification:**\nTo fully exploit the microscope's resolving power, the magnified image viewed at distance $l_0$ must satisfy $\\Gamma \\,\\delta\\psi \\ge \\delta\\psi'$:\n$$\\Gamma_{\\text{min}} = \\frac{\\delta\\psi'}{\\delta\\psi} = \\frac{1.22 \\lambda / d_0}{(0.61 \\lambda / \\sin\\alpha) / l_0} = \\frac{1.22}{0.61} \\frac{l_0 \\sin\\alpha}{d_0} = \\frac{2 l_0 \\sin\\alpha}{d_0}$$\nNotice that the wavelength $\\lambda$ cancels out!\n\n**4. Numerical Evaluation:**\nWith $l_0 = 25\\text{ cm} = 250\\text{ mm}$, $\\sin\\alpha = 0.24$, and $d_0 = 4.0\\text{ mm}$:\n$$\\Gamma_{\\text{min}} = \\frac{2 \\times (250\\text{ mm}) \\times 0.24}{4.0\\text{ mm}} = \\frac{120}{4.0} = 30$$",
        "tags": ["microscope", "useful magnification", "resolving power", "numerical aperture", "pupil diameter"]
    },
    {
        "id": "5.151",
        "title": "X-Ray Diffraction on a 1D Chain of Scattering Centres",
        "difficulty": 2,
        "question": "A beam of X-rays with wavelength $\\lambda$ falls at a glancing angle $\\alpha_0 = 60.0^\\circ$ on a linear chain of scattering centres with period $a$. Find the glancing angles $\\alpha$ corresponding to all diffraction maxima if $\\lambda = \\frac{2}{5}a$.",
        "hints": [
            "The path difference between rays scattered by adjacent centres along the chain is $\\Delta = a (\\cos\\alpha_0 - \\cos\\alpha)$ or $a(\\cos\\alpha - \\cos\\alpha_0)$.",
            "The condition for diffraction maxima is $a (\\cos\\alpha - \\cos\\alpha_0) = k \\lambda \\implies \\cos\\alpha = \\cos\\alpha_0 + k \\frac{\\lambda}{a}$.",
            "Substitute $\\cos 60.0^\\circ = 0.50$ and $\\frac{\\lambda}{a} = 0.40$, and find all integer orders $k$ for which $|\\cos\\alpha| \\le 1$."
        ],
        "answer": "$\\alpha = 26^\\circ, 60^\\circ, 84^\\circ, 107^\\circ, 134^\\circ$",
        "solution": "**1. Diffraction Condition for a Linear Chain:**\nLet a beam of X-rays fall on a linear chain of atoms of period $a$ at glancing angle $\\alpha_0$ (measured from the axis of the chain).\nThe condition for constructive interference of rays scattered at glancing angle $\\alpha$ is:\n$$a (\\cos\\alpha - \\cos\\alpha_0) = k \\lambda$$\n$$\\cos\\alpha = \\cos\\alpha_0 + k \\frac{\\lambda}{a}$$\nwhere $k$ is an integer.\n\n**2. Evaluation of Possible Orders:**\nGiven $\\alpha_0 = 60.0^\\circ$ ($\\cos\\alpha_0 = 0.50$) and $\\lambda / a = 2/5 = 0.40$:\n$$\\cos\\alpha = 0.50 + 0.40 k$$\nFor physical real angles, $-1 \\le \\cos\\alpha \\le 1$:\n- $k = +1$: $\\cos\\alpha = 0.50 + 0.40 = 0.90 \\implies \\alpha = \\arccos(0.90) \\approx 25.84^\\circ \\approx 26^\\circ$\n- $k = 0$: $\\cos\\alpha = 0.50 \\implies \\alpha = 60.0^\\circ = 60^\\circ$\n- $k = -1$: $\\cos\\alpha = 0.50 - 0.40 = 0.10 \\implies \\alpha = \\arccos(0.10) \\approx 84.26^\\circ \\approx 84^\\circ$\n- $k = -2$: $\\cos\\alpha = 0.50 - 0.80 = -0.30 \\implies \\alpha = \\arccos(-0.30) \\approx 107.46^\\circ \\approx 107^\\circ$\n- $k = -3$: $\\cos\\alpha = 0.50 - 1.20 = -0.70 \\implies \\alpha = \\arccos(-0.70) \\approx 134.43^\\circ \\approx 134^\\circ$\n- For $k = +2$: $\\cos\\alpha = 1.30 > 1$ (no solution).\n- For $k = -4$: $\\cos\\alpha = -1.10 < -1$ (no solution).\n\n**3. Result:**\nThe glancing angles corresponding to diffraction maxima are $26^\\circ, 60^\\circ, 84^\\circ, 107^\\circ$, and $134^\\circ$.",
        "tags": ["X-ray diffraction", "1D lattice", "scattering centres", "glancing angle"]
    },
    {
        "id": "5.152",
        "title": "Periods of a 2D Rectangular Array from X-Ray Diffraction",
        "difficulty": 2,
        "question": "A beam of X-rays with wavelength $\\lambda = 40\\text{ pm}$ falls normally on a plane rectangular array of scattering centres and produces a system of diffraction maxima on a plane screen at distance $l = 10\\text{ cm}$ from the array. Find the array periods $a$ and $b$ along the $x$ and $y$ axes if the distances between symmetrically located maxima of second order are $\\Delta x = 60\\text{ mm}$ (along the $x$ axis) and $\\Delta y = 40\\text{ mm}$ (along the $y$ axis).",
        "hints": [
            "For normal incidence on a 2D array, the diffraction conditions along $x$ and $y$ decouple: $a \\sin\\theta_x = k_x \\lambda$ and $b \\sin\\theta_y = k_y \\lambda$.",
            "The distance between symmetric $\\pm k$ maxima on the screen is $\\Delta x = 2 l \\tan\\theta_x$ and $\\Delta y = 2 l \\tan\\theta_y$.",
            "Find $\\tan\\theta = \\Delta / (2l)$, compute $\\sin\\theta = \\frac{\\tan\\theta}{\\sqrt{1 + \\tan^2\\theta}}$, and solve for $a = \\frac{2\\lambda}{\\sin\\theta_x}$ and $b = \\frac{2\\lambda}{\\sin\\theta_y}$ with $k = 2$."
        ],
        "answer": "$a = 0.28\\text{ nm}$, $b = 0.41\\text{ nm}$",
        "solution": "**1. Diffraction Conditions along Principal Axes:**\nFor normal incidence on a 2D rectangular array with lattice constants $a$ and $b$:\n$$a \\sin\\theta_x = k_x \\lambda, \\quad b \\sin\\theta_y = k_y \\lambda$$\nFor second-order maxima ($k_x = 2$, $k_y = 2$):\n$$a = \\frac{2\\lambda}{\\sin\\theta_x}, \\quad b = \\frac{2\\lambda}{\\sin\\theta_y}$$\n\n**2. Determining Angles from Screen Positions:**\nThe symmetrical maxima $\\pm 2$ are separated by $\\Delta x$ and $\\Delta y$ on the screen at distance $l = 10\\text{ cm} = 100\\text{ mm}$:\n$$\\tan\\theta_x = \\frac{\\Delta x}{2l} = \\frac{60\\text{ mm}}{200\\text{ mm}} = 0.30$$\n$$\\sin\\theta_x = \\frac{\\tan\\theta_x}{\\sqrt{1 + \\tan^2\\theta_x}} = \\frac{0.30}{\\sqrt{1 + 0.09}} = \\frac{0.30}{\\sqrt{1.09}} \\approx \\frac{0.30}{1.0440} \\approx 0.2874$$\n$$\\tan\\theta_y = \\frac{\\Delta y}{2l} = \\frac{40\\text{ mm}}{200\\text{ mm}} = 0.20$$\n$$\\sin\\theta_y = \\frac{\\tan\\theta_y}{\\sqrt{1 + \\tan^2\\theta_y}} = \\frac{0.20}{\\sqrt{1 + 0.04}} = \\frac{0.20}{\\sqrt{1.04}} \\approx \\frac{0.20}{1.0198} \\approx 0.1961$$\n\n**3. Calculating Periods $a$ and $b$:**\nGiven $\\lambda = 40\\text{ pm} = 0.040\\text{ nm}$:\n$$a = \\frac{2 \\times 0.040\\text{ nm}}{0.2874} \\approx 0.278\\text{ nm} \\approx 0.28\\text{ nm}$$\n$$b = \\frac{2 \\times 0.040\\text{ nm}}{0.1961} \\approx 0.408\\text{ nm} \\approx 0.41\\text{ nm}$$",
        "tags": ["X-ray diffraction", "2D lattice", "lattice constant", "Fraunhofer diffraction"]
    },
    {
        "id": "5.153",
        "title": "Diffraction Maxima and Wavelengths for a 3D Rectangular Array (Laue Equations)",
        "difficulty": 3,
        "question": "A beam of X-rays impinges on a three-dimensional rectangular array whose periods are $a$, $b$, and $c$. The direction of the incident beam coincides with the direction along which the array period is $a$. Find the directions to the diffraction maxima and the wavelengths at which these maxima will be observed.",
        "hints": [
            "Let the incident beam propagate along the $x$-axis (direction cosines $(1, 0, 0)$). The diffracted direction has direction cosines $(\\cos\\alpha, \\cos\\beta, \\cos\\gamma)$ satisfying $\\cos^2\\alpha + \\cos^2\\beta + \\cos^2\\gamma = 1$.",
            "Write the three Laue equations: $a(1 - \\cos\\alpha) = k_1 \\lambda$, $b \\cos\\beta = k_2 \\lambda$, $c \\cos\\gamma = k_3 \\lambda$.",
            "Express the direction cosines in terms of $\\lambda$, substitute into $\\cos^2\\alpha + \\cos^2\\beta + \\cos^2\\gamma = 1$, and solve for $\\lambda$."
        ],
        "answer": "$\\lambda = \\frac{2(k_1/a)}{(k_1/a)^2 + (k_2/b)^2 + (k_3/c)^2}$ with directions given by $\\cos\\alpha = 1 - \\frac{k_1\\lambda}{a}$, $\\cos\\beta = \\frac{k_2\\lambda}{b}$, $\\cos\\gamma = \\frac{k_3\\lambda}{c}$",
        "solution": "**1. Geometry and Laue Equations:**\nChoose the Cartesian axes along the principal crystallographic directions of the rectangular lattice with lattice constants $a$, $b$, and $c$.\nThe incident beam travels along the $x$-axis ($\\{1, 0, 0\\}$).\nLet the unit vector in the direction of a diffraction maximum have direction cosines $(\\cos\\alpha, \\cos\\beta, \\cos\\gamma)$, which must satisfy:\n$$\\cos^2\\alpha + \\cos^2\\beta + \\cos^2\\gamma = 1$$\nThe path differences along the three axes must be integer multiples of $\\lambda$:\n1. Along the $x$-axis (period $a$):\n   $$a(1 - \\cos\\alpha) = k_1 \\lambda \\implies \\cos\\alpha = 1 - \\frac{k_1 \\lambda}{a}$$\n2. Along the $y$-axis (period $b$):\n   $$b \\cos\\beta = k_2 \\lambda \\implies \\cos\\beta = \\frac{k_2 \\lambda}{b}$$\n3. Along the $z$-axis (period $c$):\n   $$c \\cos\\gamma = k_3 \\lambda \\implies \\cos\\gamma = \\frac{k_3 \\lambda}{c}$$\n\n**2. Wavelength Condition:**\nSubstituting these direction cosines into the identity $\\cos^2\\alpha + \\cos^2\\beta + \\cos^2\\gamma = 1$:\n$$\\left(1 - \\frac{k_1 \\lambda}{a}\\right)^2 + \\left(\\frac{k_2 \\lambda}{b}\\right)^2 + \\left(\\frac{k_3 \\lambda}{c}\\right)^2 = 1$$\nExpanding the first term:\n$$1 - 2 \\left(\\frac{k_1}{a}\\right) \\lambda + \\left(\\frac{k_1}{a}\\right)^2 \\lambda^2 + \\left(\\frac{k_2}{b}\\right)^2 \\lambda^2 + \\left(\\frac{k_3}{c}\\right)^2 \\lambda^2 = 1$$\nCancelling 1 from both sides and dividing by $\\lambda \\ne 0$:\n$$\\lambda \\left[\\left(\\frac{k_1}{a}\\right)^2 + \\left(\\frac{k_2}{b}\\right)^2 + \\left(\\frac{k_3}{c}\\right)^2\\right] = 2 \\left(\\frac{k_1}{a}\\right)$$\n$$\\lambda = \\frac{2 (k_1 / a)}{(k_1 / a)^2 + (k_2 / b)^2 + (k_3 / c)^2}$$\n\n**3. Diffracted Directions:**\nThe directions $(\\alpha, \\beta, \\gamma)$ are determined by substituting this value of $\\lambda$ back into the three Laue equations.",
        "tags": ["X-ray diffraction", "Laue equations", "3D crystal lattice", "direction cosines"]
    },
    {
        "id": "5.154",
        "title": "Wavelength of X-Rays from Bragg Reflection on NaCl Crystal",
        "difficulty": 2,
        "question": "A narrow beam of X-rays impinges on the natural facet of a NaCl single crystal, whose density is $\\rho = 2.16\\text{ g/cm}^3$, at a glancing angle $\\alpha = 60.0^\\circ$. The mirror reflection from this facet produces a maximum of second order ($k = 2$). Find the wavelength $\\lambda$ of radiation.",
        "hints": [
            "In a rock-salt (NaCl) face-centered cubic crystal, the mass of one formula unit is $m = M / N_A$. Each unit cell of volume $(2d)^3$ contains 4 formula units, so $\\rho = \\frac{m}{2d^3}$, where $d$ is the interplanar distance between adjacent (100) planes.",
            "Determine the lattice spacing $d = \\left(\\frac{m}{2\\rho}\\right)^{1/3}$.",
            "Use Bragg's law: $2 d \\sin\\alpha = k \\lambda \\implies \\lambda = \\frac{2 d \\sin\\alpha}{k}$."
        ],
        "answer": "$\\lambda = \\frac{2}{k}\\left(\\frac{m}{2\\rho}\\right)^{1/3} \\sin\\alpha = 244\\text{ pm}$",
        "solution": "**1. Interplanar Distance in NaCl:**\nNaCl forms a face-centered cubic lattice of alternating $\\text{Na}^+$ and $\\text{Cl}^-$ ions.\nLet $d$ be the distance between adjacent parallel lattice planes parallel to the natural cleavage facet.\nThe volume of a cube of edge $d$ contains on average $1/2$ molecule of NaCl.\nTherefore, the mass density is related to the molecular mass $m$ of NaCl by:\n$$\\rho = \\frac{m / 2}{d^3} = \\frac{m}{2 d^3} \\implies d = \\left(\\frac{m}{2\\rho}\\right)^{1/3}$$\nUsing $M_{\\text{NaCl}} = 58.44\\text{ g/mol}$ and $N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}$:\n$$m = \\frac{58.44 \\times 10^{-3}\\text{ kg/mol}}{6.022 \\times 10^{23}\\text{ mol}^{-1}} \\approx 9.704 \\times 10^{-26}\\text{ kg}$$\nWith $\\rho = 2.16\\text{ g/cm}^3 = 2160\\text{ kg/m}^3$:\n$$\\frac{m}{2\\rho} = \\frac{9.704 \\times 10^{-26}}{2 \\times 2160} = 2.246 \\times 10^{-29}\\text{ m}^3$$\n$$d = (22.46 \\times 10^{-30}\\text{ m}^3)^{1/3} \\approx 2.822 \\times 10^{-10}\\text{ m} = 282.2\\text{ pm}$$\n\n**2. Bragg's Law:**\nFor the $k$-th reflection order at glancing angle $\\alpha$:\n$$2 d \\sin\\alpha = k \\lambda \\implies \\lambda = \\frac{2 d \\sin\\alpha}{k}$$\nFor $k = 2$ and $\\alpha = 60.0^\\circ$:\n$$\\lambda = d \\sin 60.0^\\circ = (282.2\\text{ pm}) \\left(\\frac{\\sqrt{3}}{2}\\right) = (282.2)(0.8660) \\approx 244.4\\text{ pm} \\approx 244\\text{ pm}$$",
        "tags": ["Bragg reflection", "NaCl crystal", "X-ray diffraction", "lattice constant"]
    },
    {
        "id": "5.155",
        "title": "Interplanar Distance from Rotating Crystal Method",
        "difficulty": 3,
        "question": "A beam of X-rays with wavelength $\\lambda = 174\\text{ pm}$ falls on the surface of a single crystal rotating about an axis parallel to its surface and perpendicular to the direction of the incident beam. The directions to the maxima of second ($k_1 = 2$) and third ($k_2 = 3$) order from the system of planes parallel to the surface form an angle $\\alpha = 60.0^\\circ$ between them. Find the corresponding interplanar distance $d$.",
        "hints": [
            "Let $\\theta_1$ and $\\theta_2$ be the glancing angles satisfying Bragg's law: $\\sin\\theta_1 = \\frac{k_1 \\lambda}{2d}$ and $\\sin\\theta_2 = \\frac{k_2 \\lambda}{2d}$.",
            "The angle between the reflected beams is $2\\theta_2 - 2\\theta_1 = \\alpha$, so $\\theta_2 - \\theta_1 = \\alpha / 2$.",
            "Use the identity $\\sin^2(\\alpha/2) = \\left(\\frac{\\lambda}{2d}\\right)^2 [k_1^2 + k_2^2 - 2 k_1 k_2 \\cos(\\alpha/2)]$ to solve for $d$."
        ],
        "answer": "$d = \\frac{\\lambda}{2\\sin(\\alpha/2)} \\sqrt{k_1^2 + k_2^2 - 2 k_1 k_2 \\cos(\\alpha/2)} = 0.28\\text{ nm}$",
        "solution": "**1. Bragg Equations and Beam Geometry:**\nLet $\\theta_1$ and $\\theta_2$ be the glancing angles of incidence on the crystal planes for reflection orders $k_1 = 2$ and $k_2 = 3$:\n$$\\sin\\theta_1 = \\frac{k_1 \\lambda}{2d}, \\quad \\sin\\theta_2 = \\frac{k_2 \\lambda}{2d}$$\nEach reflected beam is deflected by angle $2\\theta$ relative to the incident direction. Therefore, the angle between the two reflected beams is:\n$$2\\theta_2 - 2\\theta_1 = \\alpha \\implies \\theta_2 - \\theta_1 = \\frac{\\alpha}{2}$$\n\n**2. Trigonometric Elimination:**\nUsing the angle addition formula:\n$$\\sin\\theta_2 = \\sin\\left(\\theta_1 + \\frac{\\alpha}{2}\\right) = \\sin\\theta_1 \\cos\\left(\\frac{\\alpha}{2}\\right) + \\cos\\theta_1 \\sin\\left(\\frac{\\alpha}{2}\\right)$$\nRearranging:\n$$\\cos\\theta_1 \\sin\\left(\\frac{\\alpha}{2}\\right) = \\sin\\theta_2 - \\sin\\theta_1 \\cos\\left(\\frac{\\alpha}{2}\\right) = \\frac{\\lambda}{2d} \\left[k_2 - k_1 \\cos\\left(\\frac{\\alpha}{2}\\right)\\right]$$\nAlso:\n$$\\sin\\theta_1 \\sin\\left(\\frac{\\alpha}{2}\\right) = \\frac{\\lambda}{2d} k_1 \\sin\\left(\\frac{\\alpha}{2}\\right)$$\nSquaring and adding both equations (since $\\cos^2\\theta_1 + \\sin^2\\theta_1 = 1$):\n$$\\sin^2\\left(\\frac{\\alpha}{2}\\right) = \\left(\\frac{\\lambda}{2d}\\right)^2 \\left\\{ \\left[k_2 - k_1 \\cos\\left(\\frac{\\alpha}{2}\\right)\\right]^2 + k_1^2 \\sin^2\\left(\\frac{\\alpha}{2}\\right) \\right\\}$$\n$$\\sin^2\\left(\\frac{\\alpha}{2}\\right) = \\left(\\frac{\\lambda}{2d}\\right)^2 \\left[k_1^2 + k_2^2 - 2 k_1 k_2 \\cos\\left(\\frac{\\alpha}{2}\\right)\\right]$$\nSolving for $d$:\n$$d = \\frac{\\lambda}{2\\sin(\\alpha/2)} \\sqrt{k_1^2 + k_2^2 - 2 k_1 k_2 \\cos(\\alpha/2)}$$\n\n**3. Numerical Evaluation:**\nGiven $\\lambda = 174\\text{ pm}$, $\\alpha = 60.0^\\circ$ (so $\\alpha/2 = 30.0^\\circ$), $k_1 = 2$, $k_2 = 3$:\n$$\\sin 30.0^\\circ = 0.50, \\quad \\cos 30.0^\\circ = \\frac{\\sqrt{3}}{2} \\approx 0.8660$$\n$$k_1^2 + k_2^2 - 2 k_1 k_2 \\cos 30.0^\\circ = 4 + 9 - 2(2)(3)(0.8660) = 13 - 10.392 = 2.608$$\n$$\\sqrt{2.608} \\approx 1.615$$\n$$d = \\frac{174\\text{ pm}}{2(0.50)} \\times 1.615 = (174\\text{ pm})(1.615) \\approx 281\\text{ pm} = 0.28\\text{ nm}$$",
        "tags": ["rotating crystal", "Bragg reflection", "interplanar distance", "X-ray diffraction"]
    },
    {
        "id": "5.156",
        "title": "Debye-Scherrer Diffraction Ring Radius",
        "difficulty": 2,
        "question": "On transmitting a beam of X-rays with wavelength $\\lambda = 17.8\\text{ pm}$ through a polycrystalline specimen, a system of diffraction rings is produced on a screen located at a distance $l = 15\\text{ cm}$ from the specimen. Determine the radius $r$ of the bright ring corresponding to second order of reflection ($k = 2$) from the system of planes with interplanar distance $d = 155\\text{ pm}$.",
        "hints": [
            "Use Bragg's condition to find the glancing angle $\\theta$: $2 d \\sin\\theta = k \\lambda$.",
            "In Debye-Scherrer powder diffraction, the diffracted rays form a cone of semi-vertex angle $2\\theta$ around the forward beam axis.",
            "The radius of the ring on a flat screen at distance $l$ is $r = l \\tan 2\\theta$."
        ],
        "answer": "$r = l \\tan 2\\theta = 3.5\\text{ cm}$, where $\\sin\\theta = \\frac{k \\lambda}{2d}$",
        "solution": "**1. Bragg Reflection Angle:**\nAccording to Bragg's law for the $k$-th order reflection from planes of interplanar spacing $d$:\n$$2 d \\sin\\theta = k \\lambda \\implies \\sin\\theta = \\frac{k \\lambda}{2d}$$\nFor $k = 2$, $\\lambda = 17.8\\text{ pm}$, and $d = 155\\text{ pm}$:\n$$\\sin\\theta = \\frac{2 \\times 17.8\\text{ pm}}{2 \\times 155\\text{ pm}} = \\frac{17.8}{155} \\approx 0.11484$$\n$$\\theta = \\arcsin(0.11484) \\approx 6.595^\\circ$$\n\n**2. Debye-Scherrer Ring Radius:**\nIn a polycrystalline sample, the myriad randomly oriented micro-crystallites have reciprocal lattice vectors oriented uniformly in all directions.\nThe rays diffracted by planes satisfying Bragg's law form a coaxial cone around the incident beam with half-opening angle $2\\theta$.\nOn a flat screen perpendicular to the beam located at distance $l$ from the sample, this cone intercepts a circle of radius:\n$$r = l \\tan 2\\theta$$\nWith $2\\theta = 2(6.595^\\circ) = 13.19^\\circ$:\n$$\\tan 2\\theta = \\tan(13.19^\\circ) \\approx 0.2344$$\n\n**3. Numerical Evaluation:**\nFor $l = 15\\text{ cm}$:\n$$r = (15\\text{ cm})(0.2344) \\approx 3.516\\text{ cm} \\approx 3.5\\text{ cm}$$",
        "tags": ["Debye-Scherrer method", "powder diffraction", "Bragg law", "diffraction ring", "X-ray"]
    }
]
