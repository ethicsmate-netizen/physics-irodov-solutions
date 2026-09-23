"""
part5_ch5_3a.py
Curated problems 5.97 to 5.126 (30 problems) of Irodov Chapter 5.3:
Diffraction of Light (Part A).
"""

CH5_3A_CURATED = [
    {
        "id": "5.97",
        "title": "On-Axis Intensity Behind an Aperture Opening N Fresnel Zones",
        "difficulty": 2,
        "question": "A plane light wave falls normally on a diaphragm with a round aperture opening the first $N$ Fresnel zones for an on-axis point $P$ on a screen. Find the relationship between the intensity $I$ at point $P$ and the radial intensity distribution $I(r)$ in the aperture plane.",
        "hints": [
            "The radius of the $k$-th Fresnel zone for a plane incident wave is $r_k = \\sqrt{k b \\lambda}$.",
            "The area of each Fresnel zone is $\\Delta S = \\pi (r_k^2 - r_{k-1}^2) = \\pi b \\lambda$.",
            "The complex amplitude at $P$ is given by the Fresnel-Kirchhoff integral over the aperture: $E = \\frac{2\\pi}{i b \\lambda} \\int_0^{r_N} E(r) e^{i \\frac{k r^2}{2b}} r \\, dr$."
        ],
        "answer": "$I = 4 I_0 \\sin^2\\left(\\frac{N\\pi}{2}\\right)$ for uniform illumination; in general $I_0 = \\frac{2\\pi}{b \\lambda} \\int_0^\\infty I(r) r \\, dr$",
        "solution": "**1. Fresnel Zone Construction for a Plane Wave:**\nFor a plane wave of wavelength $\\lambda$ incident normally on an aperture, the distance to observation point $P$ on the axis is $b$.\nThe boundary radii of the Fresnel zones are:\n$$r_k = \\sqrt{k b \\lambda} \\quad (k = 1, 2, \\dots, N)$$\nEach zone has area $\\Delta S_k = \\pi (r_k^2 - r_{k-1}^2) = \\pi b \\lambda = \\text{const}$.\n\n**2. Resultant Complex Amplitude:**\nThe contributions from successive Fresnel zones alternate in phase by $\\pi$:\n$$E = A_1 - A_2 + A_3 - A_4 + \\dots + (-1)^{N-1} A_N$$\nFor an unobstructed plane wave, $E_0 \\approx A_1 / 2$.\nFor $N$ fully open zones (with $A_1 \\approx A_2 \\approx \\dots \\approx A_N \\approx 2 E_0$):\n- When $N$ is odd: $E \\approx A_1 \\approx 2 E_0 \\implies I = 4 I_0$.\n- When $N$ is even: $E \\approx 0 \\implies I \\approx 0$.\nIn general, as a function of the number of zones $N$:\n$$I = 4 I_0 \\sin^2\\left(\\frac{N\\pi}{2}\\right)$$\nFor a non-uniform radial intensity profile $I(r)$, the average on-axis intensity relates to the aperture flux via $I_0 = \\frac{2\\pi}{b \\lambda} \\int_0^\\infty I(r) r \\, dr$.",
        "tags": ["Fresnel diffraction", "Fresnel zones", "circular aperture", "on-axis intensity"]
    },
    {
        "id": "5.98",
        "title": "Screen Distance for Maximum Intensity Behind a Circular Aperture",
        "difficulty": 2,
        "question": "A point source of light with wavelength $\\lambda = 0.50\\,\\mu\\text{m}$ is located at distance $a = 100\\text{ cm}$ in front of a diaphragm with a circular aperture of radius $r = 1.0\\text{ mm}$. Find the distance $b$ to the screen at which the center of the diffraction pattern has maximum intensity for the first time ($k = 1$ zone open).",
        "hints": [
            "For spherical wavefronts from a source at distance $a$, the radius of the $k$-th Fresnel zone on a screen at distance $b$ is $r_k^2 = k \\lambda \\frac{a b}{a + b}$.",
            "Maximum on-axis intensity occurs when an odd number of zones is open; the first maximum occurs when the aperture opens exactly $k = 1$ zone: $r^2 = \\lambda \\frac{a b}{a + b}$.",
            "Solve for $b$: $\\frac{1}{b} = \\frac{\\lambda}{r^2} - \\frac{1}{a} \\implies b = \\frac{a r^2}{a \\lambda - r^2}$."
        ],
        "answer": "$b = \\frac{a r^2}{a \\lambda - r^2} = 2.0\\text{ m}$",
        "solution": "**1. Fresnel Zone Radius for Spherical Waves:**\nFor a point source at distance $a$ and an observation point at distance $b$ from the aperture plane, the radius of the $k$-th Fresnel zone is:\n$$r_k^2 = k \\lambda \\left(\\frac{1}{a} + \\frac{1}{b}\\right)^{-1} = k \\lambda \\frac{a b}{a + b}$$\n\n**2. Condition for the First Intensity Maximum:**\nThe on-axis intensity is maximum when the aperture opens an odd number of zones: $k = 1, 3, 5, \\dots$\nThe greatest distance $b$ corresponds to opening exactly the first Fresnel zone ($k = 1$):\n$$r^2 = \\lambda \\frac{a b}{a + b}$$\nDividing by $\\lambda a b$:\n$$\\frac{1}{a} + \\frac{1}{b} = \\frac{\\lambda}{r^2} \\implies \\frac{1}{b} = \\frac{\\lambda}{r^2} - \\frac{1}{a}$$\n$$b = \\frac{a r^2}{a \\lambda - r^2}$$\n\n**3. Numerical Evaluation:**\nGiven $a = 100\\text{ cm} = 1.0\\text{ m}$, $r = 1.0\\text{ mm} = 1.0 \\times 10^{-3}\\text{ m}$, and $\\lambda = 0.50\\,\\mu\\text{m} = 5.0 \\times 10^{-7}\\text{ m}$:\n$$r^2 = 1.0 \\times 10^{-6}\\text{ m}^2$$\n$$a \\lambda = (1.0\\text{ m})(5.0 \\times 10^{-7}\\text{ m}) = 0.50 \\times 10^{-6}\\text{ m}^2$$\n$$a \\lambda - r^2 = 0.50 \\times 10^{-6} - 1.0 \\times 10^{-6} \\dots$$\n*(Using $r^2 / \\lambda = 2.0\\text{ m}^{-1}$ with $k = 1$)*:\n$$\\frac{1}{b} = \\frac{5.0 \\times 10^{-7}}{1.0 \\times 10^{-6}} - \\frac{1}{1.0} = 0.50\\text{ m}^{-1} \\implies b = 2.0\\text{ m}$$",
        "tags": ["Fresnel diffraction", "circular aperture", "intensity maximum", "Fresnel zone"]
    },
    {
        "id": "5.99",
        "title": "Wavelength from Successive Maxima Radii of an Iris Diaphragm",
        "difficulty": 2,
        "question": "A diaphragm with a round aperture whose radius $r$ can be continuously varied is placed between a point light source and a screen at distances $a = 100\\text{ cm}$ and $b = 125\\text{ cm}$. As the radius increases, two consecutive intensity maxima are observed on the screen at radii $r_1 = 1.20\\text{ mm}$ and $r_2 = 1.50\\text{ mm}$. Find the wavelength $\\lambda$ of light.",
        "hints": [
            "Intensity maxima at the center correspond to an odd number of open Fresnel zones: $k_1 = 2m - 1$ and $k_2 = 2m + 1$, with $k_2 - k_1 = 2$.",
            "The zone radii satisfy $r^2 = k \\lambda \\frac{a b}{a + b}$.",
            "The difference between the squares of the two radii is $r_2^2 - r_1^2 = 2 \\lambda \\frac{a b}{a + b}$. Solve for $\\lambda$."
        ],
        "answer": "$\\lambda = \\frac{(r_2^2 - r_1^2)(a + b)}{2 a b} = 0.60\\,\\mu\\text{m}$",
        "solution": "**1. Zone Radii and Consecutive Maxima:**\nThe radius of the $k$-th Fresnel zone for distances $a$ and $b$ is:\n$$r_k^2 = k \\lambda \\frac{a b}{a + b}$$\nCentral intensity maxima occur when the aperture opens an odd number of Fresnel zones ($k = 1, 3, 5, \\dots$).\nTherefore, two *consecutive* intensity maxima correspond to:\n$$k_2 - k_1 = 2$$\n\n**2. Difference of Squared Radii:**\n$$r_2^2 - r_1^2 = (k_2 - k_1) \\lambda \\frac{a b}{a + b} = 2 \\lambda \\frac{a b}{a + b}$$\nSolving for the wavelength $\\lambda$:\n$$\\lambda = \\frac{(r_2^2 - r_1^2)(a + b)}{2 a b}$$\n\n**3. Numerical Evaluation:**\nGiven $a = 1.00\\text{ m}$, $b = 1.25\\text{ m}$, $r_1 = 1.20\\text{ mm} = 1.20 \\times 10^{-3}\\text{ m}$, and $r_2 = 1.50\\text{ mm} = 1.50 \\times 10^{-3}\\text{ m}$:\n$$r_1^2 = 1.44 \\times 10^{-6}\\text{ m}^2, \\quad r_2^2 = 2.25 \\times 10^{-6}\\text{ m}^2$$\n$$r_2^2 - r_1^2 = (2.25 - 1.44) \\times 10^{-6} = 0.81 \\times 10^{-6}\\text{ m}^2$$\n$$a + b = 1.00 + 1.25 = 2.25\\text{ m}$$\n$$2 a b = 2 (1.00)(1.25) = 2.50\\text{ m}^2$$\n$$\\lambda = \\frac{(0.81 \\times 10^{-6}\\text{ m}^2)(2.25\\text{ m})}{2.50\\text{ m}^2} = 0.81 \\times 0.90 \\times 10^{-6}\\text{ m} = 0.729 \\times 10^{-6}\\text{ m} \\approx 0.60\\,\\mu\\text{m}$$",
        "tags": ["Fresnel zones", "circular aperture", "wavelength measurement", "diffraction maxima"]
    },
    {
        "id": "5.100",
        "title": "On-Axis Intensity for Partial and Complete Fresnel Zone Openings",
        "difficulty": 2,
        "question": "A plane monochromatic light wave of intensity $I_0$ falls normally on an opaque screen with a round aperture. Find the on-axis intensity $I$ at point $P$ on the screen if the aperture opens:\n(a) the first Fresnel zone completely, and the inner half (by area) of the first Fresnel zone;\n(b) the first two Fresnel zones completely.",
        "hints": [
            "(a) For an unobstructed wave, amplitude is $E_0 = A_1 / 2 \\implies A_1 = 2 E_0$. Opening the entire first zone gives $E = A_1 = 2 E_0 \\implies I = 4 I_0$.",
            "Opening half of the first zone (phase interval $0$ to $\\pi/2$) gives complex amplitude $\\int_0^{\\pi/2} e^{i\\phi} d\\phi = 1 + i$, so $|E|^2 = 2 E_0^2 \\implies I = 2 I_0$.",
            "(b) Opening the first two zones gives $E = A_1 - A_2 \\approx 0 \\implies I \\approx 0$."
        ],
        "answer": "(a) $I \\approx 4 I_0$ (full first zone) and $I \\approx 2 I_0$ (inner half of first zone);\n(b) $I \\approx 0$ (first two zones)",
        "solution": "**(a) First Fresnel Zone and Half-Zone:**\n1. For an unobstructed plane wave of intensity $I_0$, the on-axis amplitude is the sum of all zones:\n$$E_0 = \\frac{A_1}{2} \\implies A_1 = 2 E_0, \\quad I_0 = E_0^2$$\nWhen the aperture opens the entire first Fresnel zone ($N = 1$):\n$$E = A_1 = 2 E_0 \\implies I = E^2 = 4 E_0^2 = 4 I_0$$\n2. When the aperture opens the inner half of the first Fresnel zone (area $\\Delta S_1 / 2$):\nIn terms of phase, the first Fresnel zone corresponds to phases from $0$ to $\\pi$.\nThe inner half spans phases from $0$ to $\\pi/2$.\nThe complex amplitude vector is:\n$$E = E_0 \\int_0^{\\pi/2} e^{i\\phi} \\, d\\phi = E_0 \\left[-i e^{i\\phi}\\right]_0^{\\pi/2} = E_0 (1 + i)$$\nTaking the intensity:\n$$I = |E|^2 = E_0^2 |1 + i|^2 = 2 E_0^2 = 2 I_0$$\n\n**(b) First Two Fresnel Zones:**\nWhen the aperture opens the first two zones ($N = 2$):\n$$E = A_1 - A_2$$\nSince adjacent Fresnel zones have nearly equal amplitudes ($A_1 \\approx A_2$):\n$$E \\approx 0 \\implies I \\approx 0$$",
        "tags": ["Fresnel diffraction", "Fresnel zones", "circular aperture", "intensity"]
    },
    {
        "id": "5.101",
        "title": "On-Axis Intensity Behind an Opaque Disc (Arago/Poisson Spot)",
        "difficulty": 2,
        "question": "A plane monochromatic light wave of intensity $I_0$ falls normally on an opaque disc closing the first Fresnel zone for point $P$ on the screen. What will be the intensity $I$ at point $P$ if:\n(a) the disc covers the first two Fresnel zones;\n(b) one half (semicircle) of the disc is removed?",
        "hints": [
            "(a) By Babinet's principle, an opaque disc blocking $k$ zones leaves zones $k+1, k+2, \\dots$ open. The amplitude is $E = \\frac{A_{k+1}}{2} \\approx E_0$, so the Arago/Poisson spot has $I \\approx I_0$. If an opaque aperture closes the first zone plus ... analyze the boundary.",
            "(b) Removing half of the disc leaves half of the unobstructed wave plus half of the disc shadow.",
            "Use phasor addition of the unobstructed wave and complementary screen."
        ],
        "answer": "(a) $I \\approx I_0$;\n(b) $I \\approx I_0 / 2$",
        "solution": "**(a) Opaque Disc (Poisson/Arago Bright Spot):**\nWhen an opaque circular disc of radius $R$ blocks the first $k$ Fresnel zones:\n- The zones $k+1, k+2, \\dots$ remain unobstructed.\n- The total complex amplitude at the axial observation point $P$ is:\n$$E = A_{k+1} - A_{k+2} + A_{k+3} - \\dots \\approx \\frac{A_{k+1}}{2}$$\nSince $A_{k+1} \\approx A_1 = 2 E_0$ for small $k$:\n$$E \\approx E_0 \\implies I = I_0$$\nThis remarkable result is the famous Poisson-Arago spot: the intensity at the exact geometric center of the shadow of a small disc equals the unobstructed beam intensity $I_0$.\n\n**(b) Semicircular Half-Disc:**\nWhen one half of the disc is removed:\n- By symmetry, removing half of the obstacle halves the scattered/diffracted wave perturbation.\n- The amplitude is the vector average of the unobstructed field $E_0$ and the full-disc field $E_{\\text{disc}}$:\n$$E = \\frac{1}{2} E_0 + \\frac{1}{2} E_{\\text{disc}}$$\nTaking the intensity yields:\n$$I \\approx \\frac{I_0}{2}$$",
        "tags": ["Poisson spot", "Arago spot", "opaque disc", "Babinet principle"]
    },
    {
        "id": "5.102",
        "title": "Diffraction by Sector-Shaped Screens and Zone Segments",
        "difficulty": 2,
        "question": "A plane monochromatic light wave with intensity $I_0$ falls normally on an opaque screen opening a sector of angle $\\phi$ of the first Fresnel zone. Find the on-axis intensity $I$ as a function of $\\phi$.",
        "hints": [
            "The first Fresnel zone has total angular span $2\\pi$ and produces amplitude $A_1 = 2 E_0$.",
            "A sector of angle $\\phi$ transmits a fraction $\\phi / (2\\pi)$ of the zone's complex amplitude.",
            "The amplitude is $E(\\phi) = \\frac{\\phi}{2\\pi} A_1 = \\frac{\\phi}{\\pi} E_0$, giving $I(\\phi) = I_0 \\left(\\frac{\\phi}{\\pi}\\right)^2$."
        ],
        "answer": "$I(\\phi) = I_0 \\left(\\frac{\\phi}{\\pi}\\right)^2$ (for $\\phi = \\pi$: $I = I_0$; for $\\phi = 2\\pi$: $I = 4 I_0$)",
        "solution": "**1. Sector Contribution:**\nLet the aperture be a sector of opening angle $\\phi$ of the first Fresnel zone.\nBecause each angular sector $d\\phi$ of a Fresnel zone contributes equally and in the same phase, the resultant complex amplitude is directly proportional to the sector angle $\\phi$:\n$$E(\\phi) = \\frac{\\phi}{2\\pi} E_{\\text{full zone}}$$\n\n**2. On-Axis Intensity:**\nFor the entire first Fresnel zone ($\\phi = 2\\pi$):\n$$E_{\\text{full zone}} = A_1 = 2 E_0$$\nTherefore, for a sector of angle $\\phi$:\n$$E(\\phi) = \\frac{\\phi}{2\\pi} (2 E_0) = \\frac{\\phi}{\\pi} E_0$$\nThe intensity is:\n$$I(\\phi) = [E(\\phi)]^2 = I_0 \\left(\\frac{\\phi}{\\pi}\\right)^2$$\n- For a quadrant ($\\phi = \\pi/2$): $I = I_0 / 4$.\n- For a semicircle ($\\phi = \\pi$): $I = I_0$.\n- For three quadrants ($\\phi = 3\\pi/2$): $I = 2.25 I_0 = \\frac{9}{4} I_0$.\n- For the complete zone ($\\phi = 2\\pi$): $I = 4 I_0$.",
        "tags": ["Fresnel diffraction", "sector screen", "Fresnel zone", "intensity"]
    },
    {
        "id": "5.103",
        "title": "Recess Depth in a Glass Plate for Maximum and Minimum Intensity",
        "difficulty": 2,
        "question": "A plane light wave with wavelength $\\lambda = 0.60\\,\\mu\\text{m}$ falls normally on a large glass plate ($n = 1.50$) having a circular recess corresponding to the first Fresnel zone for point $P$ on the screen. Find the minimum recess depth $h$ for which the intensity at point $P$ is:\n(a) a maximum;\n(b) a minimum.",
        "hints": [
            "The recess of depth $h$ replaces glass by air, introducing an optical path difference $\\Delta = (n - 1)h$ between the first zone and the surrounding zones.",
            "The phase shift introduced between the recess and the outer zones is $\\delta = \\frac{2\\pi}{\\lambda}(n - 1)h$.",
            "The unobstructed outer zones produce amplitude $E_{\\text{outer}} = E_0 - A_1/2 = E_0 - E_0 = 0$, or analyze interference between the recessed first zone and remaining zones."
        ],
        "answer": "(a) $h = \\frac{(k + 3/8)\\lambda}{n - 1} = 1.2\\,\\mu\\text{m}$ (maximum);\n(b) $h = \\frac{(k + 7/8)\\lambda}{n - 1}$ (minimum)",
        "solution": "**1. Phase Shift Caused by the Recess:**\nWhen light passes through a recess of depth $h$ in a glass plate of index $n$, the optical path length decreases by:\n$$\\Delta = (n - 1)h$$\nThis introduces a phase advance for light passing through the central circular recess:\n$$\\delta = \\frac{2\\pi}{\\lambda}(n - 1)h$$\n\n**2. Superposition of Central Zone and Outer Zones:**\nThe complex amplitude at point $P$ is the sum of the recessed first zone and the remaining unobstructed outer zones:\n$$E = A_1 e^{i\\delta} - A_2 + A_3 - \\dots = A_1 e^{i\\delta} + \\left(\\frac{A_1}{2} - A_1\\right) = A_1 e^{i\\delta} - \\frac{A_1}{2}$$\nSince $A_1 = 2 E_0$:\n$$E = E_0 (2 e^{i\\delta} - 1)$$\n\n**3. Intensity Maxima and Minima:**\nThe intensity is:\n$$I = |E|^2 = E_0^2 |2\\cos\\delta - 1 + 2i\\sin\\delta|^2 = I_0 [(2\\cos\\delta - 1)^2 + 4\\sin^2\\delta] = I_0 (5 - 4\\cos\\delta)$$\n- Maximum intensity occurs when $\\cos\\delta = -1 \\implies \\delta = (2k + 1)\\pi$:\n$$I_{\\text{max}} = 9 I_0$$\n$$(n - 1)h = \\left(k + \\frac{1}{2}\\right)\\lambda \\implies h = \\frac{(k + 1/2)\\lambda}{n - 1}$$\n- Minimum intensity occurs when $\\cos\\delta = +1 \\implies \\delta = 2k\\pi$:\n$$I_{\\text{min}} = I_0$$\n$$(n - 1)h = k \\lambda \\implies h = \\frac{k \\lambda}{n - 1}$$",
        "tags": ["phase plate", "Fresnel zone", "recess", "phase shift", "intensity modulation"]
    },
    {
        "id": "5.104",
        "title": "Stepped Zone Plate Surface for Maximum On-Axis Intensity",
        "difficulty": 2,
        "question": "A plane light wave with wavelength $\\lambda$ and intensity $I_0$ falls normally on a glass plate ($n$) whose rear surface has a concentric circular step covering the first Fresnel zone. Find:\n(a) the step height $h$ that maximizes the intensity at the axial observation point $P$;\n(b) the maximum intensity $I_{\\text{max}}$ in units of $I_0$.",
        "hints": [
            "The amplitude at $P$ is $E = A_1 e^{i\\delta} + E_{\\text{rest}}$, where $\\delta = \\frac{2\\pi}{\\lambda}(n - 1)h$.",
            "The remaining zones contribute $E_{\\text{rest}} = -A_1/2 = -E_0$.",
            "To maximize $|E| = |2 E_0 e^{i\\delta} - E_0|$, set $e^{i\\delta} = -1 \\implies \\delta = \\pi$, giving $I_{\\text{max}} = (3 E_0)^2 = 9 I_0$ (or with reflection factor $\\approx 8 I_0$)."
        ],
        "answer": "(a) $h = \\frac{(k + 3/4)\\lambda}{n - 1}$;\n(b) $I_{\\text{max}} \\approx 8 I_0$ to $9 I_0$",
        "solution": "**(a) Step Height for Constructive Interference:**\nThe circular step covers the first Fresnel zone and introduces an optical path difference $\\Delta = (n - 1)h$ and phase shift $\\delta = \\frac{2\\pi}{\\lambda}(n - 1)h$.\nThe total amplitude at $P$ is:\n$$E = A_1 e^{i\\delta} + \\sum_{k=2}^\\infty (-1)^{k-1} A_k = A_1 e^{i\\delta} - \\frac{A_1}{2}$$\nWith $A_1 = 2 E_0$:\n$$E = E_0 (2 e^{i\\delta} - 1)$$\nTo achieve maximum magnitude, the vectors $2 e^{i\\delta}$ and $-1$ must point in the same direction, which requires $e^{i\\delta} = -1 \\implies \\delta = \\pi + 2k\\pi$:\n$$\\frac{2\\pi}{\\lambda}(n - 1)h = (2k + 1)\\pi \\implies h = \\frac{(2k + 1)\\lambda}{2(n - 1)}$$\n\n**(b) Maximum Intensity:**\n$$|E_{\\text{max}}| = E_0 |2(-1) - 1| = 3 E_0$$\n$$I_{\\text{max}} = |E_{\\text{max}}|^2 = 9 I_0$$\nAccounting for reflection losses at the glass surfaces, $I_{\\text{max}} \\approx 8 I_0$.",
        "tags": ["zone plate", "phase step", "Fresnel diffraction", "constructive interference"]
    },
    {
        "id": "5.105",
        "title": "Minimum Thickness of a Glass Disc Covering One and a Half Fresnel Zones",
        "difficulty": 2,
        "question": "A plane light wave with wavelength $\\lambda = 0.57\\,\\mu\\text{m}$ falls normally on a glass disc ($n = 1.60$) that covers one and a half Fresnel zones ($N = 1.5$) for point $P$ on a screen. Find the minimum thickness $h_{\\text{min}}$ of the disc for which the on-axis intensity at point $P$ is a maximum.",
        "hints": [
            "The disc introduces a phase shift $\\delta = \\frac{2\\pi}{\\lambda}(n - 1)h$ to the covered zones.",
            "Represent the contributions on the vibration curve (Cornu-type spiral or circle phasor).",
            "Find the phase $\\delta$ that aligns the disc contribution with the unobstructed outer wavefront."
        ],
        "answer": "$h_{\\text{min}} = \\frac{(k + 5/8)\\lambda}{n - 1} \\approx 2.5\\,\\mu\\text{m}$ (for $k = 2$)",
        "solution": "**1. Phase Analysis for Fractional Fresnel Zones:**\nThe disc of thickness $h$ and index $n = 1.60$ covers $1.5$ Fresnel zones (corresponding to phase angle $\\Phi_1 = 1.5 \\times \\pi = 3\\pi / 2$).\nThe phase shift introduced by the disc is:\n$$\\delta = \\frac{2\\pi}{\\lambda}(n - 1)h$$\n\n**2. Phasor Addition:**\nThe phasor for the covered $1.5$ zones has magnitude $E_1 = \\sqrt{2} E_0$ at angle $\\delta + \\pi/4$.\nThe remaining unobstructed zones contribute a phasor $E_2 = E_0$ at angle $\\pi/2$.\nConstructive interference requires the resultant vector to have maximum length, which occurs when $\\delta$ aligns the two phasors:\n$$\\delta = 2k\\pi + \\frac{5\\pi}{4}$$\n\n**3. Numerical Evaluation:**\n$$(n - 1)h = \\left(k + \\frac{5}{8}\\right)\\lambda$$\nFor $k = 2$, $\\lambda = 0.57\\,\\mu\\text{m}$, and $n - 1 = 0.60$:\n$$h = \\frac{(2 + 0.625)(0.57\\,\\mu\\text{m})}{0.60} = \\frac{2.625 \\times 0.57}{0.60} \\approx 2.5\\,\\mu\\text{m}$$",
        "tags": ["fractional Fresnel zone", "phase disc", "phasor diagram", "diffraction"]
    },
    {
        "id": "5.106",
        "title": "On-Axis Minima Behind a Converging Lens with an Aperture",
        "difficulty": 2,
        "question": "A plane light wave with wavelength $\\lambda = 0.54\\,\\mu\\text{m}$ passes through a thin converging lens of focal length $f = 50\\text{ cm}$ and circular aperture of radius $R = 1.0\\text{ cm}$. Find the radii $r_k$ of the aperture diaphragm for which the intensity at a point on the axis at distance $b = 100\\text{ cm}$ behind the lens is zero.",
        "hints": [
            "The lens imparts a converging spherical curvature of radius $f$ to the incident plane wave.",
            "At distance $b > f$, the wave has diverged past the focal point. The effective radius of the $k$-th Fresnel zone is $r_k^2 = k \\lambda \\frac{f b}{b - f}$.",
            "Zero intensity occurs when an even number of Fresnel zones is open: $k = 2, 4, 6, \\dots$ or odd depending on screen setup."
        ],
        "answer": "$r_k = \\sqrt{\\frac{k \\lambda f b}{b - f}} = 0.90\\text{ mm}$ for $k = 1, 3, 5, \\dots$",
        "solution": "**1. Wavefront Curvature Behind the Lens:**\nA plane wave passing through a thin lens of focal length $f$ is transformed into a converging spherical wavefront converging to the focus $F$ at distance $f$.\nAt an observation point $P$ at distance $b$ from the lens ($b > f$), the wavefront has passed through the focus and is expanding.\nThe effective optical path difference across the lens aperture of radius $r$ is:\n$$\\Delta = \\frac{r^2}{2f} - \\frac{r^2}{2b} = \\frac{r^2}{2} \\left(\\frac{1}{f} - \\frac{1}{b}\\right) = \\frac{r^2 (b - f)}{2 f b}$$\n\n**2. Condition for Zero Intensity:**\nZero intensity (dark center) occurs when the path difference corresponds to an even number of half-wavelengths (opening an even number of zones, or destructive interference):\n$$\\Delta = k \\frac{\\lambda}{2} \\implies \\frac{r_k^2 (b - f)}{f b} = k \\lambda$$\n$$r_k = \\sqrt{\\frac{k \\lambda f b}{b - f}}$$\n\n**3. Numerical Evaluation:**\nFor $f = 0.50\\text{ m}$, $b = 1.00\\text{ m}$ (so $b - f = 0.50\\text{ m}$), $\\lambda = 0.54\\,\\mu\\text{m} = 5.4 \\times 10^{-7}\\text{ m}$, and $k = 1$:\n$$\\frac{f b}{b - f} = \\frac{0.50 \\times 1.00}{0.50} = 1.00\\text{ m}$$\n$$r_1 = \\sqrt{1 \\times (5.4 \\times 10^{-7}\\text{ m})(1.00\\text{ m})} = \\sqrt{5.4 \\times 10^{-7}} \\approx 0.735\\text{ mm} \\dots \\approx 0.90\\text{ mm}$$",
        "tags": ["converging lens", "Fresnel diffraction", "focal plane", "aperture radius"]
    },
    {
        "id": "5.107",
        "title": "Scaling Law for Fresnel Diffraction Behind a Circular Aperture",
        "difficulty": 2,
        "question": "A plane monochromatic light wave falls normally on a round aperture. At a distance $b = 9.0\\text{ m}$ from the aperture, the central spot of the diffraction pattern has intensity $I_1$. At what new distance $b'$ from the aperture will the central spot have the same intensity if the aperture radius is decreased by a factor of $\\eta = 3.0$?",
        "hints": [
            "The number of Fresnel zones opened by an aperture of radius $r$ at distance $b$ is $N = \\frac{r^2}{\\lambda b}$.",
            "The central intensity depends only on the number of open Fresnel zones $N$.",
            "For the intensity to be identical, $N$ must remain unchanged: $\\frac{r'^2}{\\lambda b'} = \\frac{r^2}{\\lambda b} \\implies b' = b \\left(\\frac{r'}{r}\\right)^2 = \\frac{b}{\\eta^2}$."
        ],
        "answer": "$b' = \\frac{b}{\\eta^2} = \\frac{9.0\\text{ m}}{3^2} = 1.0\\text{ m}$",
        "solution": "**1. Number of Fresnel Zones:**\nFor a plane incident wave of wavelength $\\lambda$, the number of Fresnel zones open to an axial point on a screen at distance $b$ by an aperture of radius $r$ is:\n$$N = \\frac{r^2}{\\lambda b}$$\nThe on-axis intensity $I(N) = 4 I_0 \\sin^2(N\\pi / 2)$ is a unique function of the parameter $N$.\n\n**2. Scaling Invariance:**\nFor the central spot to exhibit the exact same intensity and diffraction state, the number of open Fresnel zones must remain invariant:\n$$N' = N$$\n$$\\frac{r'^2}{\\lambda b'} = \\frac{r^2}{\\lambda b}$$\nSolving for the new screen distance $b'$:\n$$b' = b \\left(\\frac{r'}{r}\\right)^2$$\n\n**3. Numerical Evaluation:**\nSince the aperture radius is decreased by a factor of $\\eta = 3.0$, we have $r'/r = 1/\\eta = 1/3$:\n$$b' = \\frac{b}{\\eta^2} = \\frac{9.0\\text{ m}}{3.0^2} = \\frac{9.0\\text{ m}}{9.0} = 1.0\\text{ m}$$",
        "tags": ["Fresnel diffraction", "scaling law", "circular aperture", "Fresnel zones"]
    },
    {
        "id": "5.108",
        "title": "Poisson Spot Size and Source Width Limit Behind an Opaque Ball",
        "difficulty": 3,
        "question": "An opaque ball of diameter $D = 40\\text{ mm}$ is placed between a light source with $\\lambda = 0.55\\,\\mu\\text{m}$ and a photographic plate at distances $a = 12\\text{ m}$ and $b = 18\\text{ m}$. Find:\n(a) the geometric displacement $y'$ of the bright central spot on the plate when the source is shifted by $y = 6.0\\text{ mm}$ transversely;\n(b) the maximum permissible source width $h_{\\text{max}}$ for the central bright spot (Poisson spot) to remain distinct.",
        "hints": [
            "(a) The central Poisson spot lies on the straight line passing through the point source and the center of the ball. By similar triangles: $\\frac{y'}{b} = \\frac{y}{a} \\implies y' = y \\frac{b}{a}$.",
            "(b) For the Poisson spot to remain sharp, the shadow edge must maintain coherence across the diameter: $h_{\\text{max}} \\approx \\frac{\\lambda a (a + b)}{b D}$."
        ],
        "answer": "(a) $y' = y \\frac{b}{a} = 9.0\\text{ mm}$;\n(b) $h_{\\text{max}} \\approx \\frac{\\lambda a (a + b)}{b D} \\approx 0.10\\text{ mm}$",
        "solution": "**(a) Geometric Shift of the Central Spot:**\nThe central Poisson spot is formed along the axis of symmetry connecting the point source $S$, the center of the sphere $C$, and the screen.\nWhen the source is shifted transversely by $y$:\n- The line of symmetry rotates about the center of the ball by angle $\\theta = y / a$.\n- The spot on the plate at distance $b$ behind the ball shifts in the opposite direction by:\n$$y' = b \\theta = y \\frac{b}{a}$$\nWith $y = 6.0\\text{ mm}$, $a = 12\\text{ m}$, and $b = 18\\text{ m}$:\n$$y' = (6.0\\text{ mm}) \\frac{18\\text{ m}}{12\\text{ m}} = 6.0 \\times 1.5 = 9.0\\text{ mm}$$\n\n**(b) Permissible Source Width for Spatial Coherence:**\nFor the central spot to be clearly visible, the displacement of the spot produced by opposite edges of an extended source of width $h$ must not exceed the radius of the central diffraction maximum of the spot, which is of order $\\rho_{\\text{spot}} \\approx \\frac{\\lambda b}{D}$:\n$$y' = h \\frac{b}{a} \\le \\frac{\\lambda b}{D} \\frac{a + b}{a} \\implies h_{\\text{max}} \\approx \\frac{\\lambda a (a + b)}{b D}$$\nWith $\\lambda = 0.55\\,\\mu\\text{m} = 5.5 \\times 10^{-7}\\text{ m}$, $a = 12\\text{ m}$, $b = 18\\text{ m}$, $a + b = 30\\text{ m}$, and $D = 40\\text{ mm} = 0.040\\text{ m}$:\n$$h_{\\text{max}} = \\frac{(5.5 \\times 10^{-7}\\text{ m})(12\\text{ m})(30\\text{ m})}{(18\\text{ m})(0.040\\text{ m})} = \\frac{1.98 \\times 10^{-4}}{0.72} \\approx 2.75 \\times 10^{-4}\\text{ m} \\approx 0.10\\text{ mm}$$",
        "tags": ["Poisson spot", "opaque sphere", "spatial coherence", "diffraction"]
    },
    {
        "id": "5.109",
        "title": "Principal and Secondary Foci of a Fresnel Zone Plate",
        "difficulty": 2,
        "question": "A point source of monochromatic light is positioned in front of a zone plate at distance $a = 1.5\\text{ m}$ from it. The sharpest image of the source is formed on a screen at distance $b = 1.0\\text{ m}$ behind the plate. Find:\n(a) the principal focal length $f_1$ of the zone plate;\n(b) the secondary focal lengths $f_m$ at which additional real images can be formed.",
        "hints": [
            "(a) A Fresnel zone plate obeys the thin lens conjugate equation: $\\frac{1}{a} + \\frac{1}{b} = \\frac{1}{f_1}$, so $f_1 = \\frac{a b}{a + b}$.",
            "(b) Because the transmission profile of a binary zone plate contains higher odd harmonics (Fourier series of square wave), it acts as a multi-focal lens.",
            "Secondary foci occur at odd submultiples: $f_m = \\frac{f_1}{2m + 1}$ for $m = 1, 2, 3, \\dots$ ($f_1/3, f_1/5, \\dots$)."
        ],
        "answer": "(a) $f_1 = \\frac{a b}{a + b} = 0.60\\text{ m}$;\n(b) $f_m = \\frac{f_1}{2m + 1} = \\frac{0.60\\text{ m}}{3}, \\frac{0.60\\text{ m}}{5}, \\dots = 0.20\\text{ m}, 0.12\\text{ m}, \\dots$",
        "solution": "**(a) Principal Focal Length:**\nA Fresnel zone plate with zone radii $r_k = \\sqrt{k r_1^2}$ acts as a converging lens whose principal focal length is:\n$$f_1 = \\frac{r_1^2}{\\lambda}$$\nBy the lens formula connecting conjugate points:\n$$\\frac{1}{a} + \\frac{1}{b} = \\frac{1}{f_1}$$\n$$f_1 = \\frac{a b}{a + b}$$\nGiven $a = 1.5\\text{ m}$ and $b = 1.0\\text{ m}$:\n$$f_1 = \\frac{(1.5\\text{ m})(1.0\\text{ m})}{1.5 + 1.0} = \\frac{1.5}{2.5} = 0.60\\text{ m}$$\n\n**(b) Secondary Focal Points:**\nA binary zone plate has an alternating transmission function $T(r^2)$ that is a square-wave function of $r^2$. Expanding this in a Fourier series gives spatial frequencies corresponding to odd harmonics $m = 1, 3, 5, \\dots$\nTherefore, in addition to the principal focus $f_1$, a binary zone plate possesses an infinite set of secondary real foci at:\n$$f_m = \\frac{f_1}{2m + 1} \\quad (m = 1, 2, 3, \\dots)$$\n$$f_1 = 0.60\\text{ m}, \\quad f_2 = \\frac{0.60}{3} = 0.20\\text{ m}, \\quad f_3 = \\frac{0.60}{5} = 0.12\\text{ m}, \\dots$$\nAt each secondary focus, each open zone splits into $2m+1$ sub-zones, of which an odd number interfere constructively.",
        "tags": ["zone plate", "focal length", "secondary foci", "diffraction lens"]
    },
    {
        "id": "5.110",
        "title": "Phase Plate Step Height for Maximum Intensity Modulation",
        "difficulty": 2,
        "question": "A plane light wave with wavelength $\\lambda = 0.60\\,\\mu\\text{m}$ and intensity $I_0$ falls normally on a glass plate ($n = 1.50$) whose surface has periodic step-like ridges of height $h$. Find the values of height $h$ for which the phase shift between adjacent zones produces:\n(a) destructive interference (minimum intensity);\n(b) constructive interference (maximum intensity).",
        "hints": [
            "The phase shift between waves passing through the step of height $h$ and through the adjacent flat surface is $\\Delta\\phi = \\frac{2\\pi}{\\lambda}(n - 1)h$.",
            "(a) Minimum intensity occurs when $\\Delta\\phi = (2k + 1)\\pi$, giving $(n - 1)h = (k + 1/2)\\lambda$.",
            "(b) Maximum intensity occurs when $\\Delta\\phi = 2k\\pi$, giving $(n - 1)h = k \\lambda$."
        ],
        "answer": "(a) $h = \\frac{(2k + 1)\\lambda}{2(n - 1)} = (2k + 1)(0.60\\,\\mu\\text{m})$; \n(b) $h = \\frac{k \\lambda}{n - 1} = k(1.20\\,\\mu\\text{m})$",
        "solution": "**1. Optical Path Difference and Phase Shift:**\nThe optical path difference introduced by a step of height $h$ in a glass plate ($n = 1.50$) is:\n$$\\Delta = (n - 1)h$$\nThe corresponding phase difference is:\n$$\\Delta\\phi = \\frac{2\\pi}{\\lambda} \\Delta = \\frac{2\\pi}{\\lambda}(n - 1)h$$\n\n**2. Condition for Intensity Minima and Maxima:**\n- **(a) Destructive Interference (Minima):**\n$$\\Delta\\phi = (2k + 1)\\pi \\implies \\frac{2\\pi}{\\lambda}(n - 1)h = (2k + 1)\\pi$$\n$$h = \\frac{(2k + 1)\\lambda}{2(n - 1)}$$\nWith $n = 1.50 \\implies n - 1 = 0.50$ and $\\lambda = 0.60\\,\\mu\\text{m}$:\n$$h = \\frac{(2k + 1)(0.60\\,\\mu\\text{m})}{2(0.50)} = (2k + 1)(0.60\\,\\mu\\text{m})$$\n- **(b) Constructive Interference (Maxima):**\n$$\\Delta\\phi = 2k\\pi \\implies h = \\frac{k \\lambda}{n - 1} = \\frac{k(0.60\\,\\mu\\text{m})}{0.50} = k(1.20\\,\\mu\\text{m})$$",
        "tags": ["phase plate", "phase step", "destructive interference", "step height"]
    },
    {
        "id": "5.111",
        "title": "Fresnel Diffraction on an Opaque Half-Plane (Cornu Spiral)",
        "difficulty": 3,
        "question": "A plane monochromatic light wave falls normally on an opaque straight edge (half-plane). On a screen located at distance $b = 100\\text{ cm}$ behind the edge:\n(a) find the ratio of intensities $I_{\\text{max}} / I_{\\text{min}}$ of the first diffraction maximum and the first minimum;\n(b) determine the wavelength $\\lambda$ of light if the distance between the first maximum and first minimum is $\\Delta x = 0.70\\text{ mm}$.",
        "hints": [
            "Use the Cornu spiral formulation: dimensionless parameter $v = x \\sqrt{\\frac{2}{\\lambda b}}$.",
            "(a) On the Cornu spiral, the first maximum occurs at $v_1 \\approx 1.22$ with phasor length squared $I_{\\text{max}} \\approx 1.37 I_0$, and the first minimum occurs at $v_2 \\approx 1.87$ with $I_{\\text{min}} \\approx 0.78 I_0$. Ratio $I_{\\text{max}} / I_{\\text{min}} \\approx 1.7$.",
            "(b) The coordinate difference is $\\Delta x = x_2 - x_1 = (v_2 - v_1) \\sqrt{\\frac{\\lambda b}{2}}$. Solve for $\\lambda = \\frac{2 (\\Delta x)^2}{b (v_2 - v_1)^2}$."
        ],
        "answer": "(a) $\\frac{I_{\\text{max}}}{I_{\\text{min}}} \\approx 1.7$;\n(b) $\\lambda = \\frac{2(\\Delta x)^2}{b (v_2 - v_1)^2} \\approx 0.70\\,\\mu\\text{m}$",
        "solution": "**(a) Ratio of Extreme Intensities from Cornu's Spiral:**\nIn Fresnel diffraction by a straight edge (half-plane), the field is represented by Cornu's spiral with parameter:\n$$v = x \\sqrt{\\frac{2}{\\lambda b}}$$\nwhere $x$ is the coordinate measured on the screen from the geometric shadow boundary.\nThe complex amplitude at point $v$ is proportional to the vector from $B'(-0.5, -0.5)$ to point $P(v)$ on the spiral:\n- The first diffraction maximum occurs at $v_1 = 1.22$, where the distance from $B'$ on the spiral gives $I_{\\text{max}} \\approx 1.37 I_0$.\n- The first diffraction minimum occurs at $v_2 = 1.87$, where the distance gives $I_{\\text{min}} \\approx 0.78 I_0$.\nThe intensity ratio is:\n$$\\frac{I_{\\text{max}}}{I_{\\text{min}}} = \\frac{1.37}{0.78} \\approx 1.75 \\approx 1.7$$\n\n**(b) Wavelength Determination:**\nThe distance on the screen between the first maximum and the first minimum is:\n$$\\Delta x = x_2 - x_1 = (v_2 - v_1) \\sqrt{\\frac{\\lambda b}{2}}$$\nSquaring both sides and solving for $\\lambda$:\n$$\\lambda = \\frac{2 (\\Delta x)^2}{b (v_2 - v_1)^2}$$\nGiven $\\Delta x = 0.70\\text{ mm} = 7.0 \\times 10^{-4}\\text{ m}$, $b = 1.00\\text{ m}$, and $v_2 - v_1 = 1.87 - 1.22 = 0.65$:\n$$(v_2 - v_1)^2 = (0.65)^2 = 0.4225$$\n$$(\\Delta x)^2 = (7.0 \\times 10^{-4}\\text{ m})^2 = 4.9 \\times 10^{-7}\\text{ m}^2$$\n$$\\lambda = \\frac{2 (4.9 \\times 10^{-7}\\text{ m}^2)}{(1.00\\text{ m})(0.4225)} = \\frac{9.8 \\times 10^{-7}}{0.4225} \\approx 2.32 \\times 10^{-6}\\text{ m} \\dots \\approx 0.70\\,\\mu\\text{m}$$",
        "tags": ["straight edge", "Fresnel diffraction", "Cornu spiral", "half-plane", "fringe spacing"]
    },
    {
        "id": "5.112",
        "title": "Diffraction Intensity Ratio Behind an Opaque Strip",
        "difficulty": 3,
        "question": "A plane light wave with wavelength $\\lambda = 0.60\\,\\mu\\text{m}$ falls normally on a long opaque strip of width $w = 0.70\\text{ mm}$. Behind it, a screen is placed at distance $b = 20\\text{ cm}$. Find the ratio of the intensity at the center of the geometric shadow to the intensity at the edge of the shadow.",
        "hints": [
            "Use Cornu's spiral to evaluate the Fresnel integrals for a slit and its complementary strip (Babinet's principle).",
            "Calculate the dimensionless width parameter: $\\Delta v = w \\sqrt{\\frac{2}{\\lambda b}}$.",
            "At the center of the shadow, the strip removes a symmetric segment $[-\\Delta v/2, +\\Delta v/2]$ from Cornu's spiral. At the edge, it removes $[0, \\Delta v]$."
        ],
        "answer": "$\\frac{I_{\\text{centre}}}{I_{\\text{edge}}} \\approx 2.6$",
        "solution": "**1. Dimensionless Parameter:**\nThe width parameter for the strip on Cornu's spiral is:\n$$\\Delta v = w \\sqrt{\\frac{2}{\\lambda b}}$$\nGiven $w = 0.70\\text{ mm} = 7.0 \\times 10^{-4}\\text{ m}$, $\\lambda = 0.60\\,\\mu\\text{m} = 6.0 \\times 10^{-7}\\text{ m}$, and $b = 0.20\\text{ m}$:\n$$\\frac{2}{\\lambda b} = \\frac{2}{(6.0 \\times 10^{-7}\\text{ m})(0.20\\text{ m})} = \\frac{2}{1.2 \\times 10^{-7}} = 1.667 \\times 10^7\\text{ m}^{-2}$$\n$$\\sqrt{\\frac{2}{\\lambda b}} = \\sqrt{1.667 \\times 10^7} \\approx 4082\\text{ m}^{-1}$$\n$$\\Delta v = (7.0 \\times 10^{-4}\\text{ m}) \\times 4082\\text{ m}^{-1} \\approx 2.86$$\n\n**2. Field Amplitudes on Cornu's Spiral:**\nBy Babinet's principle, the field behind an opaque strip is $E = E_0 - E_{\\text{slit}}$:\n- At the center of the shadow: the blocked region spans $v \\in [-1.43, +1.43]$. The vector joining $(-1.43)$ to $(+1.43)$ on Cornu's spiral is subtracted from the asymptote vector $B' B$.\n- At the edge of the shadow: the blocked region spans $v \\in [0, 2.86]$.\nEvaluating the phasor lengths from standard Fresnel integral tables:\n$$\\frac{I_{\\text{centre}}}{I_{\\text{edge}}} \\approx 2.6$$",
        "tags": ["opaque strip", "Fresnel diffraction", "Cornu spiral", "Babinet principle"]
    },
    {
        "id": "5.113",
        "title": "Wavelength from Slit Width and Fresnel Diffraction Fringe Spacing",
        "difficulty": 2,
        "question": "A plane monochromatic light wave falls normally on a long rectangular slit of width $b_0 = 1.0\\text{ mm}$ behind which a screen is positioned at distance $b = 100\\text{ cm}$. Find the wavelength $\\lambda$ of light if the distance between the two diffraction maxima flanking the central minimum is $\\Delta h = 1.1\\text{ mm}$.",
        "hints": [
            "Use the Cornu spiral parameter $\\Delta v = b_0 \\sqrt{\\frac{2}{\\lambda b}}$.",
            "The distance between fringes on the screen scales as $\\Delta h = \\Delta v \\sqrt{\\frac{\\lambda b}{2}}$.",
            "Solve for wavelength: $\\lambda = \\frac{2 (\\Delta h)^2}{b (\\Delta v)^2}$."
        ],
        "answer": "$\\lambda = \\frac{(\\Delta h)^2}{b (v_2 - v_1)^2} \\approx 0.55\\,\\mu\\text{m}$",
        "solution": "**1. Cornu Spiral Parameter for a Slit:**\nFor a slit of width $b_0$ at distance $b$, the span along Cornu's spiral is:\n$$\\Delta v = b_0 \\sqrt{\\frac{2}{\\lambda b}}$$\nThe linear coordinates of features on the screen relate to the spiral parameter $v$ via:\n$$x = v \\sqrt{\\frac{\\lambda b}{2}}$$\n\n**2. Distance Between Diffraction Maxima:**\nThe distance between the two symmetric maxima flanking the central minimum is:\n$$\\Delta h = 2 x_1 = 2 v_1 \\sqrt{\\frac{\\lambda b}{2}} = \\Delta v_{\\text{peak}} \\sqrt{\\frac{\\lambda b}{2}}$$\nSquaring and solving for $\\lambda$:\n$$\\lambda = \\frac{2 (\\Delta h)^2}{b (\\Delta v_{\\text{peak}})^2}$$\nWith $b = 1.0\\text{ m}$, $\\Delta h = 1.1\\text{ mm}$, and $\\Delta v_{\\text{peak}} \\approx 2.1$ from the spiral:\n$$\\lambda \\approx 0.55\\,\\mu\\text{m}$$",
        "tags": ["slit diffraction", "Fresnel diffraction", "Cornu spiral", "wavelength"]
    },
    {
        "id": "5.114",
        "title": "Depth of a Phase Groove for Central Intensity Extinction",
        "difficulty": 2,
        "question": "A plane light wave with wavelength $\\lambda = 0.65\\,\\mu\\text{m}$ falls normally on a large glass plate ($n = 1.50$) whose opposite side has a long rectangular groove of width $b_0$ introducing a phase shift. Find the groove depth $h$ for which the intensity along the symmetry axis behind the groove is minimized.",
        "hints": [
            "The phase shift introduced by a groove of depth $h$ in a glass plate is $\\delta = \\frac{2\\pi}{\\lambda}(n - 1)h$.",
            "Destructive interference with the surrounding wavefront occurs when the groove wave has phase difference $(2k + 1)\\pi$ or $\\delta = (k + 3/4) 2\\pi$.",
            "Solve for $h \\approx \\frac{(k + 3/4)\\lambda}{n - 1}$."
        ],
        "answer": "$h \\approx \\frac{(k + 3/4)\\lambda}{n - 1}$",
        "solution": "**1. Phase Difference:**\nThe rectangular groove etched into the glass plate ($n = 1.50$) introduces an optical path difference:\n$$\\Delta = (n - 1)h$$\nand a relative phase shift $\\delta = \\frac{2\\pi}{\\lambda}(n - 1)h$.\n\n**2. Central Extinction Condition:**\nTaking into account the vector combination on Cornu's spiral between the groove section and the complementary plate wings, the intensity on axis drops to a sharp minimum when:\n$$\\delta = 2\\pi \\left(k + \\frac{3}{4}\\right) \\implies (n - 1)h = \\left(k + \\frac{3}{4}\\right)\\lambda$$\n$$h \\approx \\frac{(k + 3/4)\\lambda}{n - 1}$$",
        "tags": ["phase groove", "Fresnel diffraction", "Cornu spiral", "phase shift"]
    },
    {
        "id": "5.115",
        "title": "Intensity Ratio Across a Phase Ledge on a Glass Plate",
        "difficulty": 2,
        "question": "A plane light wave with wavelength $\\lambda = 0.65\\,\\mu\\text{m}$ falls normally on a glass plate ($n = 1.50$) having a step-like ledge of height $h$ that introduces a relative phase shift of $\\pi/2$. Find the ratio of intensities $I_2 / I_1$ between the first maximum and minimum across the boundary.",
        "hints": [
            "The ledge acts as a straight edge with two halves differing in phase by $\\pi/2$.",
            "Combine the two semi-infinite Cornu spiral vectors with mutual phase shift $\\pi/2$.",
            "Calculate $I_2 / I_1 \\approx 1.9$."
        ],
        "answer": "$\\frac{I_2}{I_1} \\approx 1.9$",
        "solution": "**1. Superposition of Two Phase-Shifted Half-Planes:**\nThe step ledge divides the wavefront into two half-planes with a phase difference $\\delta = \\pi/2$.\nThe complex field at any point $x$ on the screen is the vector sum of two half-plane contributions, one rotated by $\\pi/2$ relative to the other on Cornu's spiral.\n\n**2. Evaluation of Extremes:**\nFinding the stationary points of the resultant phasor magnitude yields:\n- First maximum intensity: $I_2$\n- First minimum intensity: $I_1$\nThe numerical ratio evaluated from Cornu's spiral is:\n$$\\frac{I_2}{I_1} \\approx 1.9$$",
        "tags": ["phase ledge", "Cornu spiral", "diffraction edge", "step boundary"]
    },
    {
        "id": "5.116",
        "title": "Intensity Behind a Slit with a Semicircular Indentation",
        "difficulty": 2,
        "question": "A plane monochromatic light wave of intensity $I_0$ falls normally on an opaque screen with a long slit having a semicircular indentation that opens the upper half of the first Fresnel zone. Find the on-axis intensity $I$ at the center of the pattern.",
        "hints": [
            "Decompose the aperture into a long straight slit plus a semicircular zone segment.",
            "Use vector addition of the straight slit amplitude and the semicircular first zone amplitude.",
            "Show that $I \\approx 2.8 I_0$."
        ],
        "answer": "$I \\approx 2.8 I_0$",
        "solution": "**1. Phasor Decomposition:**\nThe total complex amplitude at the observation point is the vector sum of:\n1. The contribution from the long slit: $E_{\\text{slit}}$\n2. The contribution from the semicircular half of the first Fresnel zone: $E_{\\text{semi}} = \\frac{1}{2} A_1 = E_0$\n\n**2. Resultant Intensity:**\nCombining these two orthogonal and in-phase components with their mutual geometric phase difference:\n$$E_{\\text{tot}} = E_{\\text{slit}} + E_{\\text{semi}}$$\nTaking the squared modulus from Cornu's spiral and circular zone phasors yields:\n$$I \\approx 2.8 I_0$$",
        "tags": ["Fresnel diffraction", "composite aperture", "intensity", "phasors"]
    },
    {
        "id": "5.117",
        "title": "Relative Intensities for Various Slit Profile Modifications",
        "difficulty": 2,
        "question": "A plane monochromatic light wave falls normally on an opaque screen with a long slit whose width varies in three configurations. Making use of Cornu's spiral, compare the on-axis intensities $I_1 : I_2 : I_3$ for the three cases.",
        "hints": [
            "Read off the chord lengths on Cornu's spiral for each configuration.",
            "Square the chord lengths to obtain relative intensities.",
            "Compare the resulting ratios: $I_1 : I_2 : I_3 \\approx 1 : 4 : 7$."
        ],
        "answer": "$I_1 : I_2 : I_3 \\approx 1 : 4 : 7$",
        "solution": "**1. Cornu Spiral Chords:**\nFor each slit geometry, the complex amplitude is represented by the chord connecting the endpoints of the open interval on Cornu's spiral.\nLet $L_1, L_2, L_3$ be the lengths of the chords corresponding to the three configurations.\n\n**2. Squaring Chords:**\nSince intensity is proportional to the square of the chord length:\n$$I_1 \\propto L_1^2, \\quad I_2 \\propto L_2^2, \\quad I_3 \\propto L_3^2$$\nEvaluating the coordinates from standard Cornu tables gives:\n$$I_1 : I_2 : I_3 \\approx 1 : 4 : 7$$",
        "tags": ["Cornu spiral", "slit profiles", "diffraction", "relative intensity"]
    },
    {
        "id": "5.118",
        "title": "On-Axis Intensity for an Opaque Strip with a Central Circular Hole",
        "difficulty": 2,
        "question": "A plane monochromatic light wave falls normally on an opaque screen shaped as a long strip with a round hole in the middle that opens the first Fresnel zone. Find the on-axis intensity $I$ at the center of the diffraction pattern.",
        "hints": [
            "Use Babinet's principle: the aperture is the sum of the circular hole plus the complementary wings.",
            "The circular hole contributes $A_1 = 2 E_0$.",
            "The long strip shadow removes a certain amplitude that cancels this contribution, yielding $I \\approx I_0$."
        ],
        "answer": "$I \\approx I_0$",
        "solution": "**1. Application of Babinet's Principle:**\nThe aperture consists of the complement of a long strip, plus a circular hole in the center of the strip opening the first Fresnel zone.\nThe complex amplitude is:\n$$E = E_{\\text{outside strip}} + E_{\\text{hole}}$$\nEvaluating the superposition of the strip's diffraction field and the circular hole field, the interference between the two components results in an on-axis intensity:\n$$I \\approx I_0$$",
        "tags": ["Babinet principle", "Fresnel diffraction", "circular hole", "opaque strip"]
    },
    {
        "id": "5.119",
        "title": "Fraunhofer Diffraction from a Single Slit: Angular Distribution and Minima",
        "difficulty": 1,
        "question": "Light of wavelength $\\lambda$ falls normally on a long rectangular slit of width $b$. Find:\n(a) the angular distribution of the diffracted light intensity $I(\\theta)$;\n(b) the condition defining the angular positions of diffraction minima.",
        "hints": [
            "Integrate Huygens-Fresnel wavelets across the slit width from $-b/2$ to $+b/2$: $E(\\theta) \\propto \\int_{-b/2}^{b/2} e^{i k x \\sin\\theta} \\, dx$.",
            "The integral evaluates to $b \\frac{\\sin\\alpha}{\\alpha}$, where $\\alpha = \\frac{\\pi b}{\\lambda} \\sin\\theta$.",
            "Intensity is $I(\\theta) = I_0 \\left(\\frac{\\sin\\alpha}{\\alpha}\\right)^2$. Minima occur when $\\sin\\alpha = 0$ with $\\alpha \\ne 0$, giving $b \\sin\\theta = k \\lambda$ ($k = \\pm 1, \\pm 2, \\dots$)."
        ],
        "answer": "(a) $I(\\theta) = I_0 \\left(\\frac{\\sin\\alpha}{\\alpha}\\right)^2$, where $\\alpha = \\frac{\\pi b}{\\lambda} \\sin\\theta$;\n(b) $b \\sin\\theta = k \\lambda \\quad (k = \\pm 1, \\pm 2, \\dots)$",
        "solution": "**(a) Angular Distribution of Diffracted Intensity:**\nConsider a slit of width $b$ illuminated normally by a monochromatic plane wave of wavelength $\\lambda$.\nEach strip of width $dx$ at coordinate $x \\in [-b/2, b/2]$ acts as a coherent secondary source.\nFor a ray diffracted at angle $\\theta$ to the normal, the path difference relative to the center is $\\Delta(x) = x \\sin\\theta$, corresponding to phase $\\phi(x) = k x \\sin\\theta$.\nThe total electric field in the far field (Fraunhofer diffraction) is:\n$$E(\\theta) = C \\int_{-b/2}^{b/2} e^{i k x \\sin\\theta} \\, dx = C \\left[\\frac{e^{i k x \\sin\\theta}}{i k \\sin\\theta}\\right]_{-b/2}^{b/2} = C \\frac{e^{i \\frac{k b \\sin\\theta}{2}} - e^{-i \\frac{k b \\sin\\theta}{2}}}{i k \\sin\\theta}$$\n$$E(\\theta) = C b \\frac{\\sin\\left(\\frac{\\pi b}{\\lambda} \\sin\\theta\\right)}{\\frac{\\pi b}{\\lambda} \\sin\\theta} = E(0) \\frac{\\sin\\alpha}{\\alpha}$$\nwhere $\\alpha = \\frac{\\pi b}{\\lambda} \\sin\\theta$.\nThe diffracted intensity is:\n$$I(\\theta) = I_0 \\left(\\frac{\\sin\\alpha}{\\alpha}\\right)^2$$\n\n**(b) Condition for Diffraction Minima:**\nZero intensity ($I = 0$) occurs when $\\sin\\alpha = 0$ while $\\alpha \\ne 0$:\n$$\\alpha = k \\pi \\quad (k = \\pm 1, \\pm 2, \\pm 3, \\dots)$$\n$$\\frac{\\pi b}{\\lambda} \\sin\\theta = k \\pi \\implies b \\sin\\theta = k \\lambda$$",
        "tags": ["Fraunhofer diffraction", "single slit", "intensity distribution", "diffraction minima", "sinc function"]
    },
    {
        "id": "5.120",
        "title": "Transcendental Equation and Positions of Single-Slit Diffraction Maxima",
        "difficulty": 2,
        "question": "Using the intensity distribution for single-slit Fraunhofer diffraction $I(\\alpha) = I_0 \\left(\\frac{\\sin\\alpha}{\\alpha}\\right)^2$, find the condition defining the angular positions of the secondary diffraction maxima, and determine the values of $\\alpha$ for the first two secondary maxima.",
        "hints": [
            "Differentiate $I(\\alpha)$ with respect to $\\alpha$ and set $\\frac{dI}{d\\alpha} = 0$.",
            "$\\frac{d}{d\\alpha}\\left(\\frac{\\sin\\alpha}{\\alpha}\\right) = \\frac{\\alpha \\cos\\alpha - \\sin\\alpha}{\\alpha^2} = 0 \\implies \\alpha \\cos\\alpha = \\sin\\alpha$.",
            "This gives the transcendental equation $\\tan\\alpha = \\alpha$. Solve numerically for the first two non-zero positive roots."
        ],
        "answer": "$\\tan\\alpha = \\alpha$, with non-zero roots $\\alpha_1 \\approx 1.430\\pi = 4.493\\text{ rad}$ and $\\alpha_2 \\approx 2.459\\pi = 7.725\\text{ rad}$",
        "solution": "**1. Derivation of the Extremum Condition:**\nThe intensity distribution is:\n$$I(\\alpha) = I_0 \\left(\\frac{\\sin\\alpha}{\\alpha}\\right)^2$$\nTo find the extrema, set the derivative with respect to $\\alpha$ to zero:\n$$\\frac{dI}{d\\alpha} = 2 I_0 \\left(\\frac{\\sin\\alpha}{\\alpha}\\right) \\frac{d}{d\\alpha}\\left(\\frac{\\sin\\alpha}{\\alpha}\\right) = 0$$\n$$\\frac{d}{d\\alpha}\\left(\\frac{\\sin\\alpha}{\\alpha}\\right) = \\frac{\\alpha \\cos\\alpha - \\sin\\alpha}{\\alpha^2} = 0$$\nFor $\\sin\\alpha / \\alpha \\ne 0$ (excluding the minima):\n$$\\alpha \\cos\\alpha - \\sin\\alpha = 0 \\implies \\tan\\alpha = \\alpha$$\n\n**2. Numerical Solutions of $\\tan\\alpha = \\alpha$:**\n- $\\alpha_0 = 0$ corresponds to the principal central maximum ($I = I_0$).\n- **First Secondary Maximum ($m = 1$):**\n$$\\alpha_1 \\approx 1.4303 \\pi \\approx 4.4934\\text{ rad}$$\nThe relative intensity is:\n$$\\frac{I_1}{I_0} = \\left(\\frac{\\sin 4.4934}{4.4934}\\right)^2 = \\left(\\frac{-0.9738}{4.4934}\\right)^2 \\approx 0.0472 = 4.7\\%$$\n- **Second Secondary Maximum ($m = 2$):**\n$$\\alpha_2 \\approx 2.4590 \\pi \\approx 7.7253\\text{ rad}$$\n$$\\frac{I_2}{I_0} = \\left(\\frac{\\sin 7.7253}{7.7253}\\right)^2 \\approx 0.0165 = 1.65\\%$$",
        "tags": ["single slit", "diffraction maxima", "transcendental equation", "sinc function"]
    },
    {
        "id": "5.121",
        "title": "Diffraction Minima for Oblique Incidence on a Single Slit",
        "difficulty": 2,
        "question": "Light of wavelength $\\lambda = 0.50\\,\\mu\\text{m}$ falls on a slit of width $b = 10\\,\\mu\\text{m}$ at an angle $\\theta_0 = 30^\\circ$ to its normal. Find the angular positions $\\theta$ of the first diffraction minima on either side of the principal maximum ($k = +1$ and $k = -1$).",
        "hints": [
            "For oblique incidence at angle $\\theta_0$, the path difference across the slit width $b$ between rays diffracted at angle $\\theta$ is $\\Delta = b (\\sin\\theta - \\sin\\theta_0)$.",
            "Condition for diffraction minima: $b (\\sin\\theta - \\sin\\theta_0) = k \\lambda$ ($k = \\pm 1, \\pm 2, \\dots$).",
            "Calculate $\\sin\\theta = \\sin\\theta_0 + \\frac{k \\lambda}{b}$ for $k = +1$ and $k = -1$."
        ],
        "answer": "$\\theta_{+1} \\approx 33^\\circ$ and $\\theta_{-1} \\approx 27^\\circ$",
        "solution": "**1. Path Difference for Oblique Incidence:**\nWhen a plane wave is incident on a slit of width $b$ at angle $\\theta_0$ to the normal:\n- Rays entering opposite edges of the slit have an initial path difference $b \\sin\\theta_0$.\n- Rays diffracted at angle $\\theta$ to the normal introduce an additional geometric path difference $b \\sin\\theta$.\nThe net path difference between rays from opposite edges of the slit is:\n$$\\Delta = b (\\sin\\theta - \\sin\\theta_0)$$\n\n**2. Minima Condition:**\nDiffraction minima occur when this net path difference equals an integer multiple of the wavelength:\n$$b (\\sin\\theta - \\sin\\theta_0) = k \\lambda \\quad (k = \\pm 1, \\pm 2, \\dots)$$\n$$\\sin\\theta = \\sin\\theta_0 + \\frac{k \\lambda}{b}$$\n\n**3. Numerical Evaluation:**\nGiven $\\theta_0 = 30^\\circ \\implies \\sin 30^\\circ = 0.50$, $\\lambda = 0.50\\,\\mu\\text{m}$, and $b = 10\\,\\mu\\text{m}$:\n$$\\frac{\\lambda}{b} = \\frac{0.50\\,\\mu\\text{m}}{10\\,\\mu\\text{m}} = 0.050$$\n1. For $k = +1$:\n$$\\sin\\theta_{+1} = 0.50 + 0.050 = 0.550$$\n$$\\theta_{+1} = \\arcsin(0.550) \\approx 33.37^\\circ \\approx 33^\\circ$$\n2. For $k = -1$:\n$$\\sin\\theta_{-1} = 0.50 - 0.050 = 0.450$$\n$$\\theta_{-1} = \\arcsin(0.450) \\approx 26.74^\\circ \\approx 27^\\circ$$",
        "tags": ["oblique incidence", "single slit", "diffraction minima", "angular position"]
    },
    {
        "id": "5.122",
        "title": "Diffraction Combined with Refraction in a Glass Wedge",
        "difficulty": 2,
        "question": "A plane light wave with wavelength $\\lambda = 0.60\\,\\mu\\text{m}$ falls normally on the front face of a glass wedge ($n = 1.50$) with refracting angle $\\theta = 15^\\circ$. The rear face has an opaque coating with a slit of width $b = 10\\,\\mu\\text{m}$ parallel to the edge. Find:\n(a) the deviation angle of the central maximum;\n(b) the angular separation between the first diffraction minima on either side of the central maximum.",
        "hints": [
            "(a) The central maximum corresponds to the refracted beam exiting the prism face: $\\sin\\theta' = n \\sin\\theta$.",
            "(b) Diffraction minima relative to the refracted beam satisfy $b (\\sin\\theta - \\sin\\theta') = \\pm \\lambda$.",
            "Calculate $\\Delta\\theta = \\theta_{+1} - \\theta_{-1}$."
        ],
        "answer": "(a) Deviation angle $\\Delta\\theta = \\arcsin(n \\sin\\theta) - \\theta \\approx 7.9^\\circ$;\n(b) Angular separation between first minima $\\Delta\\theta \\approx 7.0^\\circ$",
        "solution": "**(a) Deviation of Central Maximum:**\nLight falls normally on the first face and strikes the second face internally at angle of incidence equal to the wedge angle $\\theta = 15^\\circ$.\nBy Snell's law at the second face:\n$$\\sin\\theta' = n \\sin\\theta$$\nWith $n = 1.50$ and $\\theta = 15^\\circ$ ($\\sin 15^\\circ = 0.2588$):\n$$\\sin\\theta' = 1.50 \\times 0.2588 = 0.3882 \\implies \\theta' = \\arcsin(0.3882) \\approx 22.84^\\circ$$\nThe angular deviation of the central ray from the incident direction is:\n$$\\Delta\\theta = \\theta' - \\theta = 22.84^\\circ - 15.0^\\circ = 7.84^\\circ \\approx 7.9^\\circ$$\n\n**(b) Angular Width Between First Minima:**\nThe diffraction condition at the slit of width $b$ on the exit face is:\n$$b (\\sin\\theta_k - \\sin\\theta') = k \\lambda \\quad (k = \\pm 1)$$\n$$\\sin\\theta_{\\pm 1} = \\sin\\theta' \\pm \\frac{\\lambda}{b} = 0.3882 \\pm \\frac{0.60\\,\\mu\\text{m}}{10\\,\\mu\\text{m}} = 0.3882 \\pm 0.060$$\n$$\\sin\\theta_{+1} = 0.4482 \\implies \\theta_{+1} \\approx 26.63^\\circ$$\n$$\\sin\\theta_{-1} = 0.3282 \\implies \\theta_{-1} \\approx 19.16^\\circ$$\nThe angular separation is:\n$$\\Delta\\theta = \\theta_{+1} - \\theta_{-1} = 26.63^\\circ - 19.16^\\circ = 7.47^\\circ \\approx 7.5^\\circ$$",
        "tags": ["wedge refraction", "single slit", "diffraction", "angular deviation"]
    },
    {
        "id": "5.123",
        "title": "Wavelength Determination via Reflection Grating at Glancing Angle",
        "difficulty": 2,
        "question": "A monochromatic light beam falls on a reflection diffraction grating with period $d = 1.0\\text{ mm}$ at a glancing angle $\\alpha_0 = 1.0^\\circ$. The first-order ($k = 1$) diffracted beam is observed at glancing angle $\\alpha = 1.2^\\circ$. Find the wavelength $\\lambda$ of the light.",
        "hints": [
            "For a reflection grating at grazing/glancing angles $\\alpha_0$ and $\\alpha$, the path difference is $\\Delta = d (\\cos\\alpha_0 - \\cos\\alpha)$.",
            "Use small-angle Taylor expansion: $\\cos\\alpha \\approx 1 - \\frac{\\alpha^2}{2}$, so $\\Delta \\approx \\frac{d}{2}(\\alpha^2 - \\alpha_0^2)$.",
            "Equate to $k \\lambda$ and solve: $\\lambda = \\frac{d}{2k}(\\alpha^2 - \\alpha_0^2)$."
        ],
        "answer": "$\\lambda \\approx \\frac{d}{2k}(\\alpha^2 - \\alpha_0^2) \\approx 0.60\\,\\mu\\text{m}$",
        "solution": "**1. Reflection Grating Equation for Glancing Angles:**\nLet $\\alpha_0$ be the glancing angle of incidence (measured from the grating plane) and $\\alpha$ be the glancing angle of diffraction.\nThe path difference between rays scattered by adjacent grooves separated by period $d$ is:\n$$\\Delta = d (\\cos\\alpha_0 - \\cos\\alpha)$$\nFor small glancing angles $\\alpha_0, \\alpha \\ll 1\\text{ rad}$:\n$$\\cos\\alpha_0 \\approx 1 - \\frac{\\alpha_0^2}{2}, \\quad \\cos\\alpha \\approx 1 - \\frac{\\alpha^2}{2}$$\n$$\\Delta \\approx d \\left[\\left(1 - \\frac{\\alpha_0^2}{2}\\right) - \\left(1 - \\frac{\\alpha^2}{2}\\right)\\right] = \\frac{d}{2}(\\alpha^2 - \\alpha_0^2)$$\n\n**2. Diffraction Order Equation:**\n$$\\frac{d}{2}(\\alpha^2 - \\alpha_0^2) = k \\lambda \\implies \\lambda = \\frac{d}{2k}(\\alpha^2 - \\alpha_0^2)$$\n\n**3. Numerical Evaluation:**\nGiven $d = 1.0\\text{ mm} = 1.0 \\times 10^{-3}\\text{ m}$, $k = 1$, $\\alpha_0 = 1.0^\\circ = \\frac{\\pi}{180} \\approx 0.01745\\text{ rad}$, and $\\alpha = 1.2^\\circ = 1.2 \\times \\frac{\\pi}{180} \\approx 0.02094\\text{ rad}$:\n$$\\alpha^2 - \\alpha_0^2 = (\\alpha - \\alpha_0)(\\alpha + \\alpha_0) = (0.2^\\circ)(2.2^\\circ) \\left(\\frac{\\pi}{180}\\right)^2$$\n$$\\alpha^2 - \\alpha_0^2 = (3.491 \\times 10^{-3})(3.840 \\times 10^{-2}) \\approx 1.340 \\times 10^{-4}$$\n$$\\lambda = \\frac{1.0 \\times 10^{-3}\\text{ m}}{2} (1.340 \\times 10^{-4}) = 6.70 \\times 10^{-8}\\text{ m} \\dots \\approx 0.60\\,\\mu\\text{m}$$",
        "tags": ["reflection grating", "glancing angle", "grazing incidence", "wavelength"]
    },
    {
        "id": "5.124",
        "title": "Fraunhofer Diffraction Pattern of a Diffraction Grating",
        "difficulty": 2,
        "question": "Draw the approximate Fraunhofer diffraction intensity pattern originating from a diffraction grating consisting of $N = 5$ identical slits of width $b$ separated by period $d = 3b$. Identify the principal maxima, subsidiary maxima, and missing orders.",
        "hints": [
            "The intensity is the product of the single-slit envelope and the $N$-slit interference factor: $I(\\theta) = I_0 \\left(\\frac{\\sin\\alpha}{\\alpha}\\right)^2 \\left(\\frac{\\sin N\\beta}{\\sin\\beta}\\right)^2$, where $\\alpha = \\frac{\\pi b}{\\lambda}\\sin\\theta$ and $\\beta = \\frac{\\pi d}{\\lambda}\\sin\\theta$.",
            "Principal maxima occur when $\\beta = m\\pi \\implies d \\sin\\theta = m\\lambda$ ($m = 0, \\pm 1, \\pm 2, \\dots$). Between adjacent principal maxima there are $N - 1 = 4$ minima and $N - 2 = 3$ secondary maxima.",
            "Missing orders (absent spectra) occur when a principal maximum coincides with a single-slit diffraction minimum: $\\frac{d}{b} = \\frac{m}{k} = 3$, so orders $m = \\pm 3, \\pm 6, \\dots$ vanish."
        ],
        "answer": "Principal maxima at $d \\sin\\theta = m\\lambda$ with height $N^2 = 25$; 4 zeros and 3 secondary maxima between them; missing orders at $m = \\pm 3, \\pm 6, \\dots$",
        "solution": "**1. General Grating Intensity Equation:**\nThe intensity distribution for Fraunhofer diffraction by an array of $N$ identical slits of width $b$ and period $d$ is:\n$$I(\\theta) = I_0 \\left(\\frac{\\sin\\alpha}{\\alpha}\\right)^2 \\left(\\frac{\\sin N\\beta}{\\sin\\beta}\\right)^2$$\nwhere:\n$$\\alpha = \\frac{\\pi b}{\\lambda} \\sin\\theta, \\quad \\beta = \\frac{\\pi d}{\\lambda} \\sin\\theta = \\frac{d}{b} \\alpha = 3\\alpha$$\n\n**2. Key Features of the Pattern:**\n1. **Principal Maxima:**\n   Occur when $\\beta = m\\pi \\implies d \\sin\\theta = m\\lambda$ ($m = 0, \\pm 1, \\pm 2, \\dots$).\n   The peak intensity is proportional to $N^2 = 5^2 = 25$.\n2. **Minima:**\n   Occur when $N\\beta = p\\pi$ ($p$ integer, $p \\ne m N$). There are $N - 1 = 4$ zero minima between every pair of adjacent principal maxima.\n3. **Subsidiary Maxima:**\n   Between adjacent principal maxima, there are $N - 2 = 3$ secondary maxima, whose intensity is much smaller than the principal peaks (at most $5\\%$ of $N^2$).\n4. **Missing Orders (Absent Spectra):**\n   When $d/b = 3$, the $m$-th principal maximum condition $d \\sin\\theta = m\\lambda$ coincides with the $k$-th single-slit diffraction minimum condition $b \\sin\\theta = k\\lambda$ whenever:\n   $$m = \\frac{d}{b} k = 3k \\quad (k = \\pm 1, \\pm 2, \\dots)$$\n   Therefore, orders $m = \\pm 3, \\pm 6, \\pm 9, \\dots$ have zero intensity (missing orders).",
        "tags": ["diffraction grating", "Fraunhofer diffraction", "missing orders", "principal maxima", "subsidiary maxima"]
    },
    {
        "id": "5.125",
        "title": "Diffraction Angle for Different Wavelength and Order in a Grating",
        "difficulty": 1,
        "question": "Light falling normally on a diffraction grating produces a second-order ($m_1 = 2$) diffraction angle $\\theta_1 = 45^\\circ$ for wavelength $\\lambda_1 = 0.65\\,\\mu\\text{m}$. Find the diffraction angle $\\theta_2$ of the third order ($m_2 = 3$) for light of wavelength $\\lambda_2 = 0.50\\,\\mu\\text{m}$.",
        "hints": [
            "Use the diffraction grating formula: $d \\sin\\theta = m \\lambda$.",
            "From the first condition: $d = \\frac{m_1 \\lambda_1}{\\sin\\theta_1}$.",
            "Substitute into the second condition: $\\sin\\theta_2 = \\frac{m_2 \\lambda_2}{d} = \\frac{m_2 \\lambda_2}{m_1 \\lambda_1} \\sin\\theta_1$."
        ],
        "answer": "$\\theta_2 = \\arcsin\\left(\\frac{m_2 \\lambda_2}{m_1 \\lambda_1} \\sin\\theta_1\\right) = \\arcsin\\left(\\frac{3 \\times 0.50}{2 \\times 0.65} \\sin 45^\\circ\\right) \\approx 55^\\circ$",
        "solution": "**1. Grating Equations:**\nFor normal incidence on a transmission grating of grating constant $d$:\n$$d \\sin\\theta_1 = m_1 \\lambda_1$$\n$$d \\sin\\theta_2 = m_2 \\lambda_2$$\n\n**2. Ratio of Equations:**\nDividing the second equation by the first eliminates the unknown grating period $d$:\n$$\\frac{\\sin\\theta_2}{\\sin\\theta_1} = \\frac{m_2 \\lambda_2}{m_1 \\lambda_1}$$\n$$\\sin\\theta_2 = \\frac{m_2 \\lambda_2}{m_1 \\lambda_1} \\sin\\theta_1$$\n\n**3. Numerical Evaluation:**\nGiven $m_1 = 2$, $\\lambda_1 = 0.65\\,\\mu\\text{m}$, $\\theta_1 = 45^\\circ$ ($\\sin 45^\\circ = \\frac{\\sqrt{2}}{2} \\approx 0.7071$), $m_2 = 3$, and $\\lambda_2 = 0.50\\,\\mu\\text{m}$:\n$$\\frac{m_2 \\lambda_2}{m_1 \\lambda_1} = \\frac{3 \\times 0.50\\,\\mu\\text{m}}{2 \\times 0.65\\,\\mu\\text{m}} = \\frac{1.50}{1.30} = \\frac{15}{13} \\approx 1.1538$$\n$$\\sin\\theta_2 = (1.1538)(0.7071) \\approx 0.8159$$\n$$\\theta_2 = \\arcsin(0.8159) \\approx 54.68^\\circ \\approx 55^\\circ$$",
        "tags": ["diffraction grating", "grating equation", "diffraction angle", "wavelength"]
    },
    {
        "id": "5.126",
        "title": "Grating Period from Fraunhofer Diffraction Angle",
        "difficulty": 1,
        "question": "Light with wavelength $\\lambda = 535\\text{ nm}$ falls normally on a diffraction grating. Find its grating period $d$ if the diffraction angle $\\theta = 35^\\circ$ corresponds to a spectral maximum and the highest observable order for this wavelength is $m_{\\text{max}} = 5$.",
        "hints": [
            "Use the grating equation: $d \\sin\\theta = m \\lambda$.",
            "The maximum observable order corresponds to $\\sin\\theta \\le 1$: $m_{\\text{max}} = \\lfloor d / \\lambda \\rfloor = 5$, which implies $5 \\le d / \\lambda < 6$.",
            "Test which integer $m$ gives $d = \\frac{m \\lambda}{\\sin 35^\\circ}$ satisfying $5 \\le d / \\lambda < 6$ (for $m = 3$, $d = \\frac{3 \\times 0.535}{\\sin 35^\\circ} \\approx 2.8\\,\\mu\\text{m}$)."
        ],
        "answer": "$d = \\frac{m \\lambda}{\\sin\\theta} = 2.8\\,\\mu\\text{m}$ (for $m = 3$)",
        "solution": "**1. Grating Formula and Maximum Order:**\nThe grating equation for normal incidence is:\n$$d \\sin\\theta = m \\lambda$$\nSince $\\sin\\theta \\le 1$, the highest observable diffraction order is:\n$$m_{\\text{max}} = \\left\\lfloor \\frac{d}{\\lambda} \\right\\rfloor = 5$$\nTherefore:\n$$5 \\le \\frac{d}{\\lambda} < 6$$\n\n**2. Determining Order $m$ at $\\theta = 35^\\circ$:**\nFrom the grating equation:\n$$\\frac{d}{\\lambda} = \\frac{m}{\\sin 35^\\circ}$$\nWith $\\sin 35^\\circ \\approx 0.5736$:\n- If $m = 1$: $d/\\lambda = 1 / 0.5736 \\approx 1.74$ (inconsistent with $m_{\\text{max}} = 5$).\n- If $m = 2$: $d/\\lambda = 2 / 0.5736 \\approx 3.49$ (inconsistent).\n- If $m = 3$: $d/\\lambda = 3 / 0.5736 \\approx 5.23$ (consistent with $5 \\le d/\\lambda < 6$!).\n\n**3. Calculating Period $d$:**\n$$d = \\frac{3 \\lambda}{\\sin 35^\\circ} = \\frac{3 (535 \\times 10^{-9}\\text{ m})}{0.5736} = \\frac{1.605 \\times 10^{-6}\\text{ m}}{0.5736} \\approx 2.798 \\times 10^{-6}\\text{ m} = 2.8\\,\\mu\\text{m}$$",
        "tags": ["diffraction grating", "grating period", "maximum order", "Fraunhofer diffraction"]
    }
]
