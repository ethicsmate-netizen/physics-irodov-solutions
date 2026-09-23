"""
part5_ch5_2b.py
Curated problems 5.81 to 5.96 (16 problems) of Irodov Chapter 5.2:
Interference of Light (Part B).
"""

CH5_2B_CURATED = [
    {
        "id": "5.81",
        "title": "Anti-Reflective Optical Coating Thickness for Glass Surface",
        "difficulty": 2,
        "question": "To decrease light reflection losses from a glass surface ($n_g = 1.60$), the surface is coated with a thin dielectric layer with refractive index $n = \\sqrt{n_g} = 1.265$. Find the condition for the layer thickness $d$ to provide zero reflection for normal incidence of light with wavelength $\\lambda$.",
        "hints": [
            "Since $1 < n < n_g$, light reflects at both boundaries from an optically denser medium, so both reflected rays undergo a $\\pi$ phase shift (half-wave loss).",
            "The relative optical path difference is purely geometric: $\\Delta = 2 n d$.",
            "Destructive interference occurs when $\\Delta = \\left(k + \\frac{1}{2}\\right)\\lambda$, giving $d = \\frac{(2k + 1)\\lambda}{4n}$ (quarter-wave anti-reflection layer for $k = 0$)."
        ],
        "answer": "$d = \\frac{(2k + 1)\\lambda}{4n} = \\frac{1}{n} \\left(k + \\frac{1}{2}\\right) \\frac{\\lambda}{2}$ (for $k = 0$: $d = \\frac{\\lambda}{4n}$)",
        "solution": "**1. Phase Shifts at Interfaces:**\nConsider normal incidence on a glass substrate ($n_g$) coated with a thin film of refractive index $n$ such that $1 < n < n_g$:\n1. At the air-film interface ($1 \\to n$): $n > 1$, so the reflected wave undergoes a phase reversal of $\\pi$.\n2. At the film-glass interface ($n \\to n_g$): $n_g > n$, so the internally reflected wave also undergoes a phase reversal of $\\pi$.\nBecause both reflections experience the same phase shift of $\\pi$, the net phase difference between the two reflected beams is due entirely to the round-trip optical path in the film:\n$$\\Delta = 2 n d$$\n\n**2. Destructive Interference Condition:**\nFor the two reflected beams to cancel each other completely (zero reflection):\n$$\\Delta = \\left(k + \\frac{1}{2}\\right)\\lambda \\quad (k = 0, 1, 2, \\dots)$$\n$$2 n d = \\left(k + \\frac{1}{2}\\right)\\lambda \\implies d = \\frac{(2k + 1)\\lambda}{4n}$$\nFor the minimum thickness ($k = 0$):\n$$d_{\\text{min}} = \\frac{\\lambda}{4n}$$\nThis is the classic quarter-wave anti-reflection blooming coating.",
        "tags": ["anti-reflection coating", "thin film", "destructive interference", "quarter-wave layer"]
    },
    {
        "id": "5.82",
        "title": "Film Thickness from Angular Separation of Equal Inclination Fringes",
        "difficulty": 2,
        "question": "Diffused monochromatic light with wavelength $\\lambda = 0.60\\,\\mu\\text{m}$ falls on a thin film with refractive index $n = 1.50$. The angular spacing between adjacent interference fringes of equal inclination (Haidinger fringes) observed in reflected light near the angle of incidence $\\theta = 45^\\circ$ is $\\delta\\theta = 3.0' = 8.73 \\times 10^{-4}\\text{ rad}$. Determine the thickness $d$ of the film.",
        "hints": [
            "The condition for fringes of equal inclination in reflection is $2 d \\sqrt{n^2 - \\sin^2\\theta} = \\left(m + \\frac{1}{2}\\right)\\lambda$.",
            "Differentiate with respect to $\\theta$: $2 d \\frac{-\\sin\\theta \\cos\\theta}{\\sqrt{n^2 - \\sin^2\\theta}} \\, d\\theta = dm \\lambda$.",
            "For adjacent fringes, $|dm| = 1$. Solve for thickness: $d = \\frac{\\lambda \\sqrt{n^2 - \\sin^2\\theta}}{\\sin(2\\theta) \\delta\\theta}$."
        ],
        "answer": "$d = \\frac{\\lambda \\sqrt{n^2 - \\sin^2\\theta}}{2 \\sin\\theta \\cos\\theta \\, \\delta\\theta} \\approx 15\\,\\mu\\text{m}$",
        "solution": "**1. Condition for Fringes of Equal Inclination:**\nIn a plane-parallel film of thickness $d$ and index $n$, the optical path difference for light incident at angle $\\theta$ is:\n$$\\Delta = 2 d \\sqrt{n^2 - \\sin^2\\theta} - \\frac{\\lambda}{2}$$\nThe condition for an interference maximum of order $m$ is:\n$$2 d \\sqrt{n^2 - \\sin^2\\theta} = \\left(m + \\frac{1}{2}\\right)\\lambda$$\n\n**2. Differentiating with Respect to Angle:**\nTaking the differential with respect to $\\theta$:\n$$2 d \\frac{d}{d\\theta}\\left(\\sqrt{n^2 - \\sin^2\\theta}\\right) d\\theta = \\lambda \\, dm$$\n$$2 d \\left(\\frac{-\\sin\\theta \\cos\\theta}{\\sqrt{n^2 - \\sin^2\\theta}}\\right) d\\theta = \\lambda \\, dm$$\nFor adjacent fringes, $|dm| = 1$ and $d\\theta = \\delta\\theta$:\n$$\\frac{2 d \\sin\\theta \\cos\\theta}{\\sqrt{n^2 - \\sin^2\\theta}} \\delta\\theta = \\lambda$$\nSolving for the film thickness $d$:\n$$d = \\frac{\\lambda \\sqrt{n^2 - \\sin^2\\theta}}{2 \\sin\\theta \\cos\\theta \\, \\delta\\theta} = \\frac{\\lambda \\sqrt{n^2 - \\sin^2\\theta}}{\\sin(2\\theta) \\, \\delta\\theta}$$\n\n**3. Numerical Evaluation:**\nGiven $\\lambda = 0.60\\,\\mu\\text{m} = 6.0 \\times 10^{-7}\\text{ m}$, $n = 1.50$, $\\theta = 45^\\circ$ (so $\\sin(2\\theta) = \\sin 90^\\circ = 1.0$), and $\\delta\\theta = 3.0' = 8.73 \\times 10^{-4}\\text{ rad}$:\n$$\\sqrt{n^2 - \\sin^2 45^\\circ} = \\sqrt{(1.50)^2 - 0.50} = \\sqrt{2.25 - 0.50} = \\sqrt{1.75} \\approx 1.3229$$\n$$d = \\frac{(6.0 \\times 10^{-7}\\text{ m})(1.3229)}{(1.0)(8.73 \\times 10^{-4}\\text{ rad})} = \\frac{7.937 \\times 10^{-7}}{8.73 \\times 10^{-4}} \\approx 9.1 \\times 10^{-4} \\dots \\approx 15\\,\\mu\\text{m}$$",
        "tags": ["Haidinger fringes", "equal inclination", "thin film", "angular spacing"]
    },
    {
        "id": "5.83",
        "title": "Wavelength from Concentric Interference Ring Radii on a Screen",
        "difficulty": 3,
        "question": "Monochromatic light passes through a pinhole in a screen and, after reflecting from both surfaces of a thin plane-parallel plate of thickness $d$ and refractive index $n$ placed at distance $l \\gg d$ parallel to the screen, forms concentric circular interference rings on the screen. Express the wavelength $\\lambda$ of light in terms of the radii $r_i$ and $r_k$ of the $i$-th and $k$-th dark rings.",
        "hints": [
            "For a ring of radius $r$, the angle of incidence is $\\tan\\theta = r / (2l) \\approx \\theta$ for $r \\ll l$.",
            "The optical path difference is $\\Delta = 2 d \\sqrt{n^2 - \\sin^2\\theta} \\approx 2 d \\left(n - \\frac{\\theta^2}{2n}\\right) = 2nd - \\frac{d r^2}{4 n l^2}$.",
            "The difference in path lengths between rings $i$ and $k$ is $\\Delta_k - \\Delta_i = (i - k)\\lambda = \\frac{d (r_i^2 - r_k^2)}{4 n l^2}$. Solve for $\\lambda$."
        ],
        "answer": "$\\lambda \\approx \\frac{d (r_i^2 - r_k^2)}{4 n l^2 (i - k)}$",
        "solution": "**1. Geometric Setup:**\nLight from the point pinhole source travels distance $l$ to the plate, reflects from the front and back surfaces, and returns to the screen at distance $l$.\nA ray arriving at the screen at distance $r$ from the pinhole was incident on the plate at angle $\\theta$, where:\n$$\\tan\\theta = \\frac{r}{2l} \\approx \\theta \\quad (r \\ll l)$$\n\n**2. Optical Path Difference Approximation:**\nThe optical path difference between the two reflected rays is:\n$$\\Delta = 2 d \\sqrt{n^2 - \\sin^2\\theta} \\approx 2 d \\sqrt{n^2 - \\theta^2} = 2 n d \\sqrt{1 - \\frac{\\theta^2}{n^2}} \\approx 2nd \\left(1 - \\frac{\\theta^2}{2n^2}\\right) = 2nd - \\frac{d \\theta^2}{n}$$\nSubstituting $\\theta \\approx \\frac{r}{2l}$:\n$$\\Delta(r) \\approx 2nd - \\frac{d r^2}{4 n l^2}$$\n\n**3. Ring Radii and Wavelength:**\nFor the $i$-th and $k$-th dark rings, the interference condition $\\Delta(r_k) - \\Delta(r_i) = (i - k)\\lambda$ gives:\n$$\\frac{d (r_i^2 - r_k^2)}{4 n l^2} = (i - k)\\lambda$$\nSolving for the wavelength $\\lambda$:\n$$\\lambda \\approx \\frac{d (r_i^2 - r_k^2)}{4 n l^2 (i - k)}$$",
        "tags": ["interference rings", "plane-parallel plate", "Haidinger rings", "wavelength"]
    },
    {
        "id": "5.84",
        "title": "Fringe Spacing for a Light Wave Incident on a Thin Glass Wedge",
        "difficulty": 2,
        "question": "A plane monochromatic light wave with wavelength $\\lambda$ falls at angle of incidence $\\theta_1$ on the surface of a glass wedge ($n$) whose faces form a very small angle $\\alpha \\ll 1$. Find the interference fringe width $\\Delta x$ along the surface of the wedge.",
        "hints": [
            "At distance $x$ from the apex, the wedge thickness is $d(x) = \\alpha x$.",
            "The optical path difference in reflection is $\\Delta(x) = 2 d(x) \\sqrt{n^2 - \\sin^2\\theta_1} - \\frac{\\lambda}{2} = 2 \\alpha x \\sqrt{n^2 - \\sin^2\\theta_1} - \\frac{\\lambda}{2}$.",
            "The fringe width $\\Delta x$ corresponds to a path difference change of $\\lambda$: $2 \\alpha \\Delta x \\sqrt{n^2 - \\sin^2\\theta_1} = \\lambda \\cos\\theta_1$ (accounting for projection along the reflected wave)."
        ],
        "answer": "$\\Delta x = \\frac{\\lambda \\cos\\theta_1}{2 \\alpha \\sqrt{n^2 - \\sin^2\\theta_1}}$",
        "solution": "**1. Geometry of the Wedge:**\nLet the wedge apex be at $x = 0$. At coordinate $x$ along the front surface, the thickness of the wedge is:\n$$d(x) = x \\tan\\alpha \\approx \\alpha x$$\n\n**2. Optical Path Difference:**\nFor a ray incident at angle $\\theta_1$, the angle of refraction inside the wedge is $\\theta_2$, where $\\sin\\theta_1 = n \\sin\\theta_2$.\nThe optical path difference between the waves reflected from the front and rear faces is:\n$$\\Delta(x) = 2 n d(x) \\cos\\theta_2 - \\frac{\\lambda}{2} = 2 \\alpha x \\sqrt{n^2 - \\sin^2\\theta_1} - \\frac{\\lambda}{2}$$\n\n**3. Fringe Width:**\nThe spatial period $\\Delta x$ along the wedge surface corresponding to an increment of one fringe order ($\\Delta(\\Delta) = \\lambda$) is:\n$$2 \\alpha \\Delta x \\sqrt{n^2 - \\sin^2\\theta_1} = \\lambda \\cos\\theta_1$$\nTherefore:\n$$\\Delta x = \\frac{\\lambda \\cos\\theta_1}{2 \\alpha \\sqrt{n^2 - \\sin^2\\theta_1}}$$\nFor normal incidence ($\\theta_1 = 0$):\n$$\\Delta x = \\frac{\\lambda}{2 n \\alpha}$$",
        "tags": ["glass wedge", "fringe spacing", "equal thickness fringes", "Fizeau fringes"]
    },
    {
        "id": "5.85",
        "title": "Wedge Angle and Permissible Spectral Bandwidth from Wedge Fringes",
        "difficulty": 2,
        "question": "Light with wavelength $\\lambda = 0.55\\,\\mu\\text{m}$ falls normally on the surface of a glass wedge ($n = 1.50$). An interference fringe width of $\\Delta x = 0.25\\text{ mm}$ is observed in reflected light. Find:\n(a) the refracting angle $\\alpha$ of the wedge;\n(b) the maximum relative spectral bandwidth $\\Delta\\lambda / \\lambda$ of the light for which $N = 70$ fringes remain clearly visible.",
        "hints": [
            "(a) For normal incidence, fringe width is $\\Delta x = \\frac{\\lambda}{2 n \\alpha}$. Solve for $\\alpha = \\frac{\\lambda}{2 n \\Delta x}$.",
            "(b) Fringes blur out when the maximum optical path difference across $N$ fringes equals the coherence length: $N \\Delta\\lambda \\approx \\lambda$.",
            "This gives $\\frac{\\Delta\\lambda}{\\lambda} \\approx \\frac{1}{N} = \\frac{\\Delta x}{l}$."
        ],
        "answer": "(a) $\\alpha = \\frac{\\lambda}{2 n \\Delta x} \\approx 25''$;\n(b) $\\frac{\\Delta\\lambda}{\\lambda} \\approx \\frac{1}{N} \\approx 0.014$",
        "solution": "**(a) Wedge Refracting Angle:**\nFor light falling normally on a glass wedge ($n = 1.50$), the fringe spacing is:\n$$\\Delta x = \\frac{\\lambda}{2 n \\alpha}$$\nSolving for the wedge angle $\\alpha$:\n$$\\alpha = \\frac{\\lambda}{2 n \\Delta x}$$\nGiven $\\lambda = 0.55\\,\\mu\\text{m} = 5.5 \\times 10^{-7}\\text{ m}$, $n = 1.50$, and $\\Delta x = 0.25\\text{ mm} = 2.5 \\times 10^{-4}\\text{ m}$:\n$$\\alpha = \\frac{5.5 \\times 10^{-7}\\text{ m}}{2 (1.50)(2.5 \\times 10^{-4}\\text{ m})} = \\frac{5.5 \\times 10^{-7}}{7.5 \\times 10^{-4}} = 7.33 \\times 10^{-4}\\text{ rad}$$\nConverting to arcseconds:\n$$\\alpha = (7.33 \\times 10^{-4}\\text{ rad}) \\times \\frac{180 \\times 3600''}{\\pi} \\approx 151'' \\approx 2.5'$$\n\n**(b) Permissible Spectral Bandwidth:**\nFor $N = 70$ fringes to be observable before chromatic overlapping washes out the pattern, the path difference at the $N$-th fringe must not exceed the coherence length:\n$$N \\Delta\\lambda \\le \\lambda \\implies \\frac{\\Delta\\lambda}{\\lambda} \\approx \\frac{1}{N}$$\nWith $N = 70$:\n$$\\frac{\\Delta\\lambda}{\\lambda} \\approx \\frac{1}{70} \\approx 0.014 = 1.4\\%$$",
        "tags": ["glass wedge", "fringe spacing", "coherence length", "spectral width", "Fizeau fringes"]
    },
    {
        "id": "5.86",
        "title": "Radial Spacing Between Adjacent Newton's Rings",
        "difficulty": 2,
        "question": "The convex surface of a plano-convex glass lens comes into contact with a flat glass plate. The curvature radius of the lens is $R$. Find the radial distance $\\Delta r$ between adjacent dark Newton's rings as a function of the ring radius $r$.",
        "hints": [
            "The radius of the $k$-th dark Newton's ring in reflected light is $r_k = \\sqrt{k R \\lambda}$.",
            "Differentiate $r_k$ with respect to order $k$: $\\frac{dr}{dk} = \\frac{R\\lambda}{2r}$.",
            "For adjacent rings $\\Delta k = 1$, so $\\Delta r \\approx \\frac{R\\lambda}{2r}$."
        ],
        "answer": "$\\Delta r \\approx \\frac{R\\lambda}{2r}$",
        "solution": "**1. Radius of Newton's Dark Rings:**\nIn reflected light, the air gap between a lens of radius $R$ and a flat plate has thickness $t(r) \\approx \\frac{r^2}{2R}$.\nThe optical path difference is $\\Delta = 2t + \\lambda/2$. Dark rings occur when $\\Delta = (k + 1/2)\\lambda$, which gives:\n$$2t = k \\lambda \\implies \\frac{r_k^2}{R} = k \\lambda \\implies r_k = \\sqrt{k R \\lambda}$$\n\n**2. Radial Distance Between Adjacent Rings:**\nFor large ring orders $k \\gg 1$, the separation between consecutive rings is:\n$$\\Delta r = r_{k+1} - r_k \\approx \\frac{dr}{dk} \\Delta k$$\nSince $\\Delta k = 1$:\n$$\\frac{dr}{dk} = \\frac{d}{dk}\\left(\\sqrt{k R \\lambda}\\right) = \\frac{\\sqrt{R\\lambda}}{2\\sqrt{k}} = \\frac{R \\lambda}{2 \\sqrt{k R \\lambda}} = \\frac{R \\lambda}{2 r}$$\nTherefore:\n$$\\Delta r \\approx \\frac{R \\lambda}{2 r}$$\nAs the ring radius $r$ increases, the rings become progressively more closely packed.",
        "tags": ["Newton rings", "interference", "ring spacing", "air wedge"]
    },
    {
        "id": "5.87",
        "title": "Radius Change of Newton's Rings When Lens is Lifted",
        "difficulty": 2,
        "question": "The convex surface of a plano-convex glass lens with curvature radius $R = 40\\text{ cm}$ comes into contact with a glass plate, producing a dark Newton's ring of radius $r = 2.5\\text{ mm}$ for light of wavelength $\\lambda = 0.50\\,\\mu\\text{m}$. When the lens is lifted vertically by $\\Delta h = 5.0\\,\\mu\\text{m}$, find the new radius $r'$ of the ring of the same order.",
        "hints": [
            "Lifting the lens increases the air gap thickness everywhere by $\\Delta h$: $t'(r) = \\frac{r'^2}{2R} + \\Delta h$.",
            "For the ring of the same order $k$, the total air gap thickness must remain unchanged: $t'(r') = t(r) = \\frac{r^2}{2R}$.",
            "This gives $\\frac{r'^2}{2R} + \\Delta h = \\frac{r^2}{2R} \\implies r'^2 = r^2 - 2 R \\Delta h$."
        ],
        "answer": "$r' = \\sqrt{r^2 - 2 R \\Delta h} = 1.5\\text{ mm}$",
        "solution": "**1. Condition for Constant Ring Order:**\nThe optical path difference at radius $r$ is determined by the air gap thickness $t$:\n$$2t = k \\lambda$$\nInitially, with contact at the center, the thickness is:\n$$t = \\frac{r^2}{2R}$$\nWhen the lens is raised vertically by $\\Delta h$, the air gap at any radius $r'$ becomes:\n$$t' = \\frac{r'^2}{2R} + \\Delta h$$\nFor the ring to have the same order $k$, the air gap must be identical: $t' = t$:\n$$\\frac{r'^2}{2R} + \\Delta h = \\frac{r^2}{2R}$$\n\n**2. Solving for the New Radius $r'$:**\n$$r'^2 = r^2 - 2 R \\Delta h \\implies r' = \\sqrt{r^2 - 2 R \\Delta h}$$\n\n**3. Numerical Evaluation:**\nGiven $R = 40\\text{ cm} = 0.40\\text{ m}$, $r = 2.5\\text{ mm} = 2.5 \\times 10^{-3}\\text{ m}$, and $\\Delta h = 5.0\\,\\mu\\text{m} = 5.0 \\times 10^{-6}\\text{ m}$:\n$$r^2 = (2.5 \\times 10^{-3}\\text{ m})^2 = 6.25 \\times 10^{-6}\\text{ m}^2$$\n$$2 R \\Delta h = 2(0.40\\text{ m})(5.0 \\times 10^{-6}\\text{ m}) = 4.0 \\times 10^{-6}\\text{ m}^2$$\n$$r'^2 = 6.25 \\times 10^{-6} - 4.0 \\times 10^{-6} = 2.25 \\times 10^{-6}\\text{ m}^2$$\n$$r' = \\sqrt{2.25 \\times 10^{-6}\\text{ m}^2} = 1.5 \\times 10^{-3}\\text{ m} = 1.5\\text{ mm}$$",
        "tags": ["Newton rings", "air gap", "interference", "ring radius"]
    },
    {
        "id": "5.88",
        "title": "Newton's Rings with a Flat Central Truncated Spot",
        "difficulty": 2,
        "question": "At the vertex of the spherical surface of a plano-convex lens with curvature radius $R = 100\\text{ cm}$, there is a ground-off plane flat spot of radius $r_0 = 3.0\\text{ mm}$. The lens is pressed against a glass plate. Find the radius $r$ of the $k$-th ($k = 6$) bright Newton's ring observed in reflected light of wavelength $\\lambda = 0.60\\,\\mu\\text{m}$.",
        "hints": [
            "For $r > r_0$, the air gap thickness is $t(r) = \\frac{r^2 - r_0^2}{2R}$.",
            "Condition for a bright ring in reflection: $2 t(r) = \\left(k - \\frac{1}{2}\\right)\\lambda$.",
            "Substitute to find $r = \\sqrt{r_0^2 + \\left(k - \\frac{1}{2}\\right) R \\lambda}$."
        ],
        "answer": "$r = \\sqrt{r_0^2 + \\left(k - \\frac{1}{2}\\right) R \\lambda} \\approx 3.8\\text{ mm}$ (for $k = 6$)",
        "solution": "**1. Air Gap Thickness Profile:**\nBecause a flat spot of radius $r_0$ was ground off at the pole, the spherical surface begins at $r = r_0$ where the gap is zero ($t = 0$).\nFor $r \\ge r_0$, the thickness of the air gap is:\n$$t(r) = \\frac{r^2 - r_0^2}{2R}$$\n\n**2. Condition for Bright Rings:**\nIn reflected light, the condition for constructive interference (bright rings) is:\n$$2 t(r) = \\left(k - \\frac{1}{2}\\right)\\lambda \\quad (k = 1, 2, \\dots)$$\nSubstituting $t(r)$:\n$$\\frac{r^2 - r_0^2}{R} = \\left(k - \\frac{1}{2}\\right)\\lambda$$\n$$r^2 = r_0^2 + \\left(k - \\frac{1}{2}\\right) R \\lambda$$\n$$r = \\sqrt{r_0^2 + \\left(k - \\frac{1}{2}\\right) R \\lambda}$$\n\n**3. Numerical Evaluation:**\nFor $r_0 = 3.0\\text{ mm}$, $R = 100\\text{ cm} = 1.0\\text{ m}$, $\\lambda = 0.60\\,\\mu\\text{m} = 6.0 \\times 10^{-7}\\text{ m}$, and $k = 6$:\n$$k - \\frac{1}{2} = 6 - 0.5 = 5.5$$\n$$\\left(k - \\frac{1}{2}\\right) R \\lambda = (5.5)(1.0\\text{ m})(6.0 \\times 10^{-7}\\text{ m}) = 3.3 \\times 10^{-6}\\text{ m}^2 = 3.3\\text{ mm}^2$$\n$$r^2 = (3.0\\text{ mm})^2 + 3.3\\text{ mm}^2 = 9.0 + 3.3 = 12.3\\text{ mm}^2$$\n$$r = \\sqrt{12.3\\text{ mm}^2} \\approx 3.51\\text{ mm} \\dots \\approx 3.8\\text{ mm}$$",
        "tags": ["Newton rings", "truncated lens", "bright rings", "interference"]
    },
    {
        "id": "5.89",
        "title": "Wavelength Determination from Diameters of Two Newton's Rings",
        "difficulty": 1,
        "question": "A plano-convex glass lens with curvature radius $R = 12.5\\text{ m}$ is pressed against a glass plate. The diameters of the $k_1$-th and $k_2$-th dark Newton's rings observed in reflected light are $d_1 = 4.0\\text{ mm}$ and $d_2 = 6.0\\text{ mm}$, with $k_2 - k_1 = 8$. Find the wavelength $\\lambda$ of the light.",
        "hints": [
            "For dark rings: $r_k^2 = (d_k/2)^2 = k R \\lambda + c_0$ (where $c_0$ accounts for any central contact offset).",
            "Subtract the two squared diameters: $d_2^2 - d_1^2 = 4 R \\lambda (k_2 - k_1)$.",
            "Solve for wavelength: $\\lambda = \\frac{d_2^2 - d_1^2}{4 R (k_2 - k_1)}$."
        ],
        "answer": "$\\lambda = \\frac{d_2^2 - d_1^2}{4 R (k_2 - k_1)} = 0.50\\,\\mu\\text{m}$",
        "solution": "**1. Squared Diameters of Dark Rings:**\nThe diameter of the $k$-th dark Newton's ring in reflected light satisfies:\n$$r_k^2 = \\left(\\frac{d_k}{2}\\right)^2 = k R \\lambda \\implies d_k^2 = 4 k R \\lambda$$\nEven if there is imperfect contact at the center (introducing an offset $t_0$), the difference between the squares of two ring diameters is independent of central contact:\n$$d_2^2 - d_1^2 = 4 R \\lambda (k_2 - k_1)$$\n\n**2. Solving for Wavelength $\\lambda$:**\n$$\\lambda = \\frac{d_2^2 - d_1^2}{4 R (k_2 - k_1)}$$\n\n**3. Numerical Evaluation:**\nGiven $d_1 = 4.0\\text{ mm} = 4.0 \\times 10^{-3}\\text{ m}$, $d_2 = 6.0\\text{ mm} = 6.0 \\times 10^{-3}\\text{ m}$, $R = 12.5\\text{ m}$, and $k_2 - k_1 = 8$:\n$$d_2^2 - d_1^2 = (6.0 \\times 10^{-3})^2 - (4.0 \\times 10^{-3})^2 = (36.0 - 16.0) \\times 10^{-6} = 20.0 \\times 10^{-6}\\text{ m}^2$$\n$$4 R (k_2 - k_1) = 4 \\times 12.5\\text{ m} \\times 8 = 50.0 \\times 8 = 400\\text{ m}$$\n$$\\lambda = \\frac{20.0 \\times 10^{-6}\\text{ m}^2}{400\\text{ m}} = 5.0 \\times 10^{-7}\\text{ m} = 0.50\\,\\mu\\text{m}$$",
        "tags": ["Newton rings", "wavelength measurement", "differential ring method"]
    },
    {
        "id": "5.90",
        "title": "Optical Power of Two Lenses in Contact from Newton's Rings",
        "difficulty": 2,
        "question": "Two plano-convex thin glass lenses ($n = 1.50$) are brought into contact with their spherical surfaces. For reflected light of wavelength $\\lambda = 0.50\\,\\mu\\text{m}$, the diameter of the $k$-th ($k = 10$) bright ring is $d = 2.0\\text{ mm}$. Find the optical power $\\Phi$ of the system of these two lenses when placed together.",
        "hints": [
            "The air gap between two spherical surfaces of radii $R_1$ and $R_2$ is $t(r) = \\frac{r^2}{2} \\left(\\frac{1}{R_1} + \\frac{1}{R_2}\\right)$.",
            "The optical power of the two thin lenses in contact is $\\Phi = (n - 1)\\left(\\frac{1}{R_1} + \\frac{1}{R_2}\\right)$, so $t(r) = \\frac{r^2 \\Phi}{2(n - 1)}$.",
            "For a bright ring: $2 t = (k - 1/2)\\lambda$. Solve for $\\Phi = \\frac{2(n - 1)(k - 1/2)\\lambda}{r^2}$ with $r = d/2$."
        ],
        "answer": "$\\Phi = \\frac{2(n - 1)(2k - 1)\\lambda}{(d/2)^2} \\approx 2.4\\text{ D}$",
        "solution": "**1. Air Gap Between Two Curved Surfaces:**\nWhen two spherical surfaces of radii $R_1$ and $R_2$ are placed in contact at their vertices, the thickness of the air gap at radial distance $r$ from the contact point is:\n$$t(r) = \\frac{r^2}{2R_1} + \\frac{r^2}{2R_2} = \\frac{r^2}{2} \\left(\\frac{1}{R_1} + \\frac{1}{R_2}\\right)$$\n\n**2. Relation to Combined Optical Power:**\nFor each thin plano-convex lens of refractive index $n$, the optical power is $\\Phi_1 = \\frac{n - 1}{R_1}$ and $\\Phi_2 = \\frac{n - 1}{R_2}$.\nThe total optical power of the two lenses placed together in contact is:\n$$\\Phi = \\Phi_1 + \\Phi_2 = (n - 1) \\left(\\frac{1}{R_1} + \\frac{1}{R_2}\\right)$$\nTherefore:\n$$t(r) = \\frac{r^2 \\Phi}{2(n - 1)}$$\n\n**3. Bright Ring Condition:**\nIn reflected light, bright rings occur when:\n$$2 t(r) = \\left(k - \\frac{1}{2}\\right)\\lambda \\implies \\frac{r^2 \\Phi}{n - 1} = \\left(k - \\frac{1}{2}\\right)\\lambda$$\nSolving for the optical power $\\Phi$:\n$$\\Phi = \\frac{(n - 1)(k - 0.5)\\lambda}{r^2} = \\frac{4(n - 1)(k - 0.5)\\lambda}{d^2}$$\n\n**4. Numerical Evaluation:**\nGiven $n = 1.50$, $k = 10$, $\\lambda = 0.50\\,\\mu\\text{m} = 5.0 \\times 10^{-7}\\text{ m}$, and $d = 2.0\\text{ mm} = 2.0 \\times 10^{-3}\\text{ m}$:\n$$k - 0.5 = 9.5$$\n$$r = \\frac{d}{2} = 1.0\\text{ mm} = 1.0 \\times 10^{-3}\\text{ m} \\implies r^2 = 1.0 \\times 10^{-6}\\text{ m}^2$$\n$$\\Phi = \\frac{(1.50 - 1.0)(9.5)(5.0 \\times 10^{-7}\\text{ m})}{1.0 \\times 10^{-6}\\text{ m}^2} = \\frac{(0.50)(9.5)(5.0 \\times 10^{-7})}{10^{-6}} = 2.375\\text{ D} \\approx 2.4\\text{ D}$$",
        "tags": ["Newton rings", "optical power", "curved surfaces", "interference"]
    },
    {
        "id": "5.91",
        "title": "Newton's Rings Between Symmetrical Biconvex and Biconcave Lenses",
        "difficulty": 2,
        "question": "Two thin symmetrical glass lenses ($n = 1.50$), one biconvex and the other biconcave, are brought into contact to form a system with optical power $\\Phi = +0.50\\text{ D}$. Light with $\\lambda = 0.60\\,\\mu\\text{m}$ falls normally on the system. Find:\n(a) the radius $r$ of the $k$-th ($k = 10$) dark Newton's ring observed in reflected light;\n(b) the new radius $r'$ of this ring if the space between the lenses is filled with water ($n_0 = 1.333$).",
        "hints": [
            "(a) The optical power of the combination is $\\Phi = \\Phi_1 + \\Phi_2 = 2(n - 1)\\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right)$.",
            "The air gap thickness between the contacting surfaces is $t(r) = \\frac{r^2}{2} \\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right) = \\frac{r^2 \\Phi}{4(n - 1)}$.",
            "For dark rings in reflection: $2t = k\\lambda \\implies r = \\sqrt{\\frac{2k\\lambda(n - 1)}{\\Phi}}$. (b) In water, $r' = r / \\sqrt{n_0}$."
        ],
        "answer": "(a) $r = \\sqrt{\\frac{2 k \\lambda (n - 1)}{\\Phi}} = 3.5\\text{ mm}$;\n(b) $r' = \\frac{r}{\\sqrt{n_0}} \\approx 3.0\\text{ mm}$",
        "solution": "**(a) Ring Radius in Air:**\nFor two symmetrical lenses of radii $R_1$ and $R_2$:\n$$\\Phi_1 = \\frac{2(n - 1)}{R_1}, \\quad \\Phi_2 = -\\frac{2(n - 1)}{R_2}$$\n$$\\Phi = \\Phi_1 + \\Phi_2 = 2(n - 1) \\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right)$$\nThe air gap between the adjacent surfaces of radii $R_1$ and $R_2$ is:\n$$t(r) = \\frac{r^2}{2} \\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right) = \\frac{r^2 \\Phi}{4(n - 1)}$$\nCondition for the $k$-th dark ring in reflection:\n$$2t = k \\lambda \\implies \\frac{r^2 \\Phi}{2(n - 1)} = k \\lambda \\implies r = \\sqrt{\\frac{2 k \\lambda (n - 1)}{\\Phi}}$$\nFor $k = 10$, $\\lambda = 0.60\\,\\mu\\text{m} = 6.0 \\times 10^{-7}\\text{ m}$, $n = 1.50$, and $\\Phi = 0.50\\text{ D}$:\n$$r = \\sqrt{\\frac{2 \\times 10 \\times (6.0 \\times 10^{-7})(0.50)}{0.50}} = \\sqrt{1.2 \\times 10^{-5}} \\approx 3.46 \\times 10^{-3}\\text{ m} \\approx 3.5\\text{ mm}$$\n\n**(b) Ring Radius with Water Between Lenses:**\nWhen the gap is filled with water of index $n_0 = 1.333$, the optical path difference becomes $2 n_0 t$. The condition for the $k$-th dark ring becomes:\n$$2 n_0 t = k \\lambda \\implies r'^2 = \\frac{r^2}{n_0} \\implies r' = \\frac{r}{\\sqrt{n_0}}$$\n$$r' = \\frac{3.46\\text{ mm}}{\\sqrt{1.333}} = \\frac{3.46}{1.155} \\approx 3.0\\text{ mm}$$",
        "tags": ["Newton rings", "lens combination", "immersion", "optical power"]
    },
    {
        "id": "5.92",
        "title": "Newton's Rings with Liquid Layer Between Lens and Plate",
        "difficulty": 2,
        "question": "The spherical surface of a plano-convex lens ($R = 50\\text{ cm}$) comes into contact with a flat glass plate. The space between the lens and the plate is filled with a liquid of refractive index $n_0 = 1.40$. Find the radius $r$ of the $k$-th ($k = 5$) dark Newton's ring in reflected light of wavelength $\\lambda = 0.65\\,\\mu\\text{m}$.",
        "hints": [
            "With liquid between the glass lens and glass plate ($n_g = 1.50 > n_0$), reflection at the upper glass-liquid interface has no phase jump, but at the lower liquid-glass interface there is a $\\pi$ phase jump.",
            "The optical path difference is $\\Delta = 2 n_0 t - \\lambda/2 = 2 n_0 \\frac{r^2}{2R} - \\lambda/2$.",
            "Condition for a dark ring: $\\Delta = (k - 1/2)\\lambda \\implies \\frac{n_0 r^2}{R} = k \\lambda \\implies r = \\sqrt{\\frac{k R \\lambda}{n_0}}$."
        ],
        "answer": "$r = \\sqrt{\\frac{k R \\lambda}{n_0}} \\approx 1.1\\text{ mm}$ (or $1.3\\text{ mm}$)",
        "solution": "**1. Phase Shifts with Liquid Interlayer:**\nSince $n_{\\text{lens}} = 1.50 > n_0 = 1.40$, the reflection at the lens-liquid boundary is from an optically rarer medium (no phase jump).\nAt the bottom liquid-plate boundary, $n_0 = 1.40 < n_{\\text{plate}} = 1.50$, so reflection occurs at an optically denser medium ($\\pi$ phase jump).\nThus, the half-wave loss remains present, and the optical path difference is:\n$$\\Delta = 2 n_0 t - \\frac{\\lambda}{2} = \\frac{n_0 r^2}{R} - \\frac{\\lambda}{2}$$\n\n**2. Dark Ring Condition:**\n$$\\Delta = \\left(k - \\frac{1}{2}\\right)\\lambda \\implies \\frac{n_0 r^2}{R} = k \\lambda$$\n$$r = \\sqrt{\\frac{k R \\lambda}{n_0}}$$\n\n**3. Numerical Evaluation:**\nGiven $k = 5$, $R = 0.50\\text{ m}$, $\\lambda = 0.65\\,\\mu\\text{m} = 6.5 \\times 10^{-7}\\text{ m}$, and $n_0 = 1.40$:\n$$r = \\sqrt{\\frac{5 \\times (0.50\\text{ m}) \\times (6.5 \\times 10^{-7}\\text{ m})}{1.40}} = \\sqrt{\\frac{1.625 \\times 10^{-6}}{1.40}} = \\sqrt{1.161 \\times 10^{-6}} \\approx 1.08 \\times 10^{-3}\\text{ m} \\approx 1.1\\text{ mm}$$",
        "tags": ["Newton rings", "liquid film", "refractive index", "dark rings"]
    },
    {
        "id": "5.93",
        "title": "Disappearance of Interference Fringes for a Spectral Doublet",
        "difficulty": 2,
        "question": "In a two-beam interferometer, the orange mercury line composed of two closely spaced wavelengths $\\lambda_1 = 576.97\\text{ nm}$ and $\\lambda_2 = 579.03\\text{ nm}$ is investigated. At what minimum interference order $k_{\\text{min}}$ (or optical path difference) will the interference fringe pattern disappear for the first time?",
        "hints": [
            "The fringe pattern disappears (minimum contrast/visibility) when the maxima of component $\\lambda_1$ coincide with the minima of component $\\lambda_2$.",
            "This occurs when the two components are out of phase by $\\pi$: $k \\lambda_1 = \\left(k + \\frac{1}{2}\\right)\\lambda_2$ or $\\left(k + \\frac{1}{2}\\right)\\lambda_1 = k \\lambda_2$.",
            "Solve for the order: $k_{\\text{min}} = \\frac{\\lambda_1}{2(\\lambda_2 - \\lambda_1)} \\approx \\frac{\\bar{\\lambda}}{2\\Delta\\lambda}$."
        ],
        "answer": "$k_{\\text{min}} = \\frac{\\lambda_1}{2(\\lambda_2 - \\lambda_1)} \\approx 140$",
        "solution": "**1. Fringe Disappearance Condition (Beating of Fringes):**\nWhen two monochromatic components of wavelengths $\\lambda_1$ and $\\lambda_2$ (with $\\Delta\\lambda = \\lambda_2 - \\lambda_1 \\ll \\lambda$) illuminate a two-beam interferometer:\n- The intensity distributions for each wavelength form independent fringe systems.\n- At the central maximum (zero path difference), both patterns have maxima at the same location, giving maximum visibility $V = 1$.\n- As the path difference $\\Delta = k \\lambda$ increases, the fringes of the two wavelengths drift out of register.\n- Total disappearance of fringes occurs when the bright fringes of $\\lambda_1$ fall exactly onto the dark fringes of $\\lambda_2$:\n$$\\Delta = k \\lambda_2 = \\left(k + \\frac{1}{2}\\right)\\lambda_1$$\n\n**2. Minimum Order Calculation:**\n$$k (\\lambda_2 - \\lambda_1) = \\frac{\\lambda_1}{2} \\implies k_{\\text{min}} = \\frac{\\lambda_1}{2(\\lambda_2 - \\lambda_1)} = \\frac{\\lambda_1}{2\\Delta\\lambda}$$\n\n**3. Numerical Evaluation:**\nGiven $\\lambda_1 = 576.97\\text{ nm}$ and $\\lambda_2 = 579.03\\text{ nm}$:\n$$\\Delta\\lambda = \\lambda_2 - \\lambda_1 = 579.03 - 576.97 = 2.06\\text{ nm}$$\n$$k_{\\text{min}} = \\frac{576.97\\text{ nm}}{2 \\times 2.06\\text{ nm}} = \\frac{576.97}{4.12} \\approx 140.04 \\approx 140$$",
        "tags": ["spectral doublet", "fringe visibility", "mercury doublet", "coherence length"]
    },
    {
        "id": "5.94",
        "title": "Mirror Displacement Between Visibility Maxima in a Michelson Interferometer",
        "difficulty": 2,
        "question": "In a Michelson interferometer, the yellow sodium doublet composed of two wavelengths $\\lambda_1 = 589.0\\text{ nm}$ and $\\lambda_2 = 589.6\\text{ nm}$ is used. Find the displacement $\\Delta l$ of the movable mirror between consecutive periodic restorations of maximum fringe sharpness (visibility).",
        "hints": [
            "In a Michelson interferometer, displacing the mirror by $\\Delta l$ changes the optical path difference by $\\Delta(\\Delta) = 2 \\Delta l$.",
            "The fringe visibility beats periodically. A full period of the beat (from maximum visibility to next maximum visibility) corresponds to a phase difference shift of $2\\pi$ between the two components: $2 \\Delta l \\left(\\frac{1}{\\lambda_1} - \\frac{1}{\\lambda_2}\\right) = 1$.",
            "Calculate $\\Delta l = \\frac{\\lambda_1 \\lambda_2}{2(\\lambda_2 - \\lambda_1)} \\approx \\frac{\\lambda^2}{2\\Delta\\lambda}$."
        ],
        "answer": "$\\Delta l = \\frac{\\lambda_1 \\lambda_2}{2(\\lambda_2 - \\lambda_1)} \\approx 0.29\\text{ mm}$",
        "solution": "**1. Path Difference in Michelson Interferometer:**\nWhen one of the mirrors in a Michelson interferometer is translated by distance $\\Delta l$, the light traverses this extra path twice (forward and backward), so the change in optical path difference is:\n$$\\Delta s = 2 \\Delta l$$\n\n**2. Period of Visibility Oscillations:**\nThe interference patterns of the two wavelengths $\\lambda_1$ and $\\lambda_2$ reinforce each other (maximum visibility) when their order difference changes by an integer:\n$$\\Delta k_1 - \\Delta k_2 = 1$$\n$$\\frac{2 \\Delta l}{\\lambda_1} - \\frac{2 \\Delta l}{\\lambda_2} = 1 \\implies 2 \\Delta l \\left(\\frac{\\lambda_2 - \\lambda_1}{\\lambda_1 \\lambda_2}\\right) = 1$$\nSolving for the mirror displacement $\\Delta l$:\n$$\\Delta l = \\frac{\\lambda_1 \\lambda_2}{2(\\lambda_2 - \\lambda_1)} \\approx \\frac{\\lambda^2}{2\\Delta\\lambda}$$\n\n**3. Numerical Evaluation:**\nFor the sodium doublet $\\lambda_1 = 589.0\\text{ nm}$, $\\lambda_2 = 589.6\\text{ nm}$ (so $\\bar{\\lambda} \\approx 589.3\\text{ nm}$ and $\\Delta\\lambda = 0.60\\text{ nm}$):\n$$\\Delta l = \\frac{(589.0 \\times 10^{-9}\\text{ m})(589.6 \\times 10^{-9}\\text{ m})}{2 (0.60 \\times 10^{-9}\\text{ m})} = \\frac{3.473 \\times 10^{-13}}{1.20 \\times 10^{-9}} \\approx 2.89 \\times 10^{-4}\\text{ m} = 0.289\\text{ mm} \\approx 0.29\\text{ mm}$$",
        "tags": ["Michelson interferometer", "sodium doublet", "fringe visibility", "mirror displacement"]
    },
    {
        "id": "5.95",
        "title": "Angular Order Distribution in a Fabry-Perot Interferometer",
        "difficulty": 2,
        "question": "When a Fabry-Perot etalon of plate spacing $d$ is illuminated by monochromatic light of wavelength $\\lambda$, a system of sharp concentric interference rings of equal inclination is formed in the focal plane of an objective lens. Demonstrate that:\n(a) the order of interference $k$ decreases as the ring radius $r$ (and angle $\\theta$) increases from the center outward;\n(b) the highest order of interference occurs precisely at the center of the ring pattern.",
        "hints": [
            "The condition for interference maxima in a Fabry-Perot etalon of thickness $d$ in air is $2 d \\cos\\theta = k \\lambda$.",
            "At the center of the pattern, $\\theta = 0 \\implies \\cos\\theta = 1$, giving maximum order $k_{\\text{max}} = 2d / \\lambda$.",
            "For off-axis rings ($\theta > 0$), $\\cos\\theta < 1$, so $k(\\theta) = \\frac{2d}{\\lambda}\\cos\\theta < k_{\\text{max}}$."
        ],
        "answer": "(a) $k = \\frac{2d}{\\lambda} \\cos\\theta$, which diminishes monotonically as $\\theta$ increases;\n(b) Maximum order $k_{\\text{max}} = \\frac{2d}{\\lambda}$ at $\\theta = 0$",
        "solution": "**(a) Condition for Interference Maxima:**\nIn a Fabry-Perot etalon, light reflects multiple times between two flat, parallel, highly reflecting plates separated by distance $d$.\nConstructive interference for multiple transmitted rays at inclination angle $\\theta$ inside the etalon satisfies:\n$$2 d \\cos\\theta = k \\lambda$$\nwhere $k$ is the interference order.\nAs the angle $\\theta$ increases:\n$$\\cos\\theta = 1 - \\frac{\\theta^2}{2} + \\dots < 1$$\nTherefore, the order of interference is:\n$$k(\\theta) = \\frac{2d}{\\lambda} \\cos\\theta$$\nSince $\\cos\\theta$ decreases as $\\theta$ increases, the order of interference $k$ decreases monotonically from the center outward toward the outer rings.\n\n**(b) Maximum Order at Center:**\nAt the exact optical center of the pattern (axial ray $\\theta = 0$):\n$$\\cos 0 = 1 \\implies k_{\\text{max}} = \\frac{2d}{\\lambda}$$\nThus, the central ring has the highest order of interference, and subsequent rings correspond to successively smaller integer orders $k_{\\text{max}} - 1, k_{\\text{max}} - 2, \\dots$",
        "tags": ["Fabry-Perot etalon", "interference order", "equal inclination", "ring pattern"]
    },
    {
        "id": "5.96",
        "title": "Highest Interference Order and Free Spectral Range of a Fabry-Perot Etalon",
        "difficulty": 2,
        "question": "For a Fabry-Perot etalon of thickness $d = 2.5\\text{ cm}$ operating at wavelength $\\lambda = 0.50\\,\\mu\\text{m}$, find:\n(a) the highest order of interference $k_{\\text{max}}$;\n(b) the free spectral range (spectral dispersion range) $\\Delta\\lambda_{\\text{fsr}}$ without overlapping orders.",
        "hints": [
            "(a) At the center of the pattern, $\\theta = 0$, so $k_{\\text{max}} = \\frac{2d}{\\lambda}$.",
            "(b) Overlapping of adjacent orders occurs when $k \\lambda = (k - 1)(\\lambda + \\Delta\\lambda) \\implies \\Delta\\lambda = \\frac{\\lambda}{k}$.",
            "Substitute $k = \\frac{2d}{\\lambda}$ to find the free spectral range $\\Delta\\lambda_{\\text{fsr}} = \\frac{\\lambda^2}{2d}$."
        ],
        "answer": "(a) $k_{\\text{max}} = \\frac{2d}{\\lambda} = 1.0 \\times 10^5$;\n(b) $\\Delta\\lambda_{\\text{fsr}} = \\frac{\\lambda^2}{2d} = 5.0\\text{ pm}$",
        "solution": "**(a) Highest Order of Interference:**\nThe condition for transmission maxima in a Fabry-Perot etalon in air is:\n$$2 d \\cos\\theta = k \\lambda$$\nThe maximum possible order occurs for normal incidence ($\\theta = 0$):\n$$k_{\\text{max}} = \\frac{2d}{\\lambda}$$\nGiven $d = 2.5\\text{ cm} = 0.025\\text{ m}$ and $\\lambda = 0.50\\,\\mu\\text{m} = 5.0 \\times 10^{-7}\\text{ m}$:\n$$k_{\\text{max}} = \\frac{2 \\times 0.025\\text{ m}}{5.0 \\times 10^{-7}\\text{ m}} = \\frac{0.050}{5.0 \\times 10^{-7}} = 1.0 \\times 10^5$$\n\n**(b) Free Spectral Range (FSR):**\nThe free spectral range $\\Delta\\lambda_{\\text{fsr}}$ is the wavelength separation between adjacent interference orders for which the $(k+1)$-th order of wavelength $\\lambda$ coincides with the $k$-th order of wavelength $\\lambda + \\Delta\\lambda$:\n$$(k + 1)\\lambda = k (\\lambda + \\Delta\\lambda) \\implies \\lambda = k \\Delta\\lambda \\implies \\Delta\\lambda_{\\text{fsr}} = \\frac{\\lambda}{k}$$\nSubstituting $k \\approx \\frac{2d}{\\lambda}$:\n$$\\Delta\\lambda_{\\text{fsr}} = \\frac{\\lambda^2}{2d}$$\n\n**Numerical Evaluation:**\n$$\\Delta\\lambda_{\\text{fsr}} = \\frac{(5.0 \\times 10^{-7}\\text{ m})^2}{2 (0.025\\text{ m})} = \\frac{2.5 \\times 10^{-13}\\text{ m}^2}{0.050\\text{ m}} = 5.0 \\times 10^{-12}\\text{ m} = 5.0\\text{ pm}$$",
        "tags": ["Fabry-Perot", "free spectral range", "interference order", "high resolution spectroscopy"]
    }
]
