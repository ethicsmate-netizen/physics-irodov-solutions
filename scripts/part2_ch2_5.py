"""
part2_ch2_5.py
Curated problems 2.160 to 2.184 (25 problems) of Irodov Chapter 2.5:
Liquids. Capillary Effects.
"""

CH2_5_CURATED = [
    {
        "id": "2.160",
        "title": "Capillary Pressure in Droplets and Bubbles",
        "difficulty": 1,
        "question": "Find the capillary pressure:\n(a) in mercury droplets of diameter $d = 1.5\\,\\mu\\text{m}$;\n(b) inside a soap bubble of diameter $d = 3.0\\text{ mm}$ if the surface tension of the soap-water solution is $\\alpha = 45\\text{ mN/m}$.",
        "hints": [
            "(a) For a spherical droplet with one surface, the Laplace excess pressure is $\\Delta p = \\frac{2\\alpha}{r} = \\frac{4\\alpha}{d}$.",
            "(b) A soap bubble has two spherical surfaces (inner and outer), so $\\Delta p = 2 \\times \\frac{2\\alpha}{r} = \\frac{8\\alpha}{d}$.",
            "Use $\\alpha_{\\text{Hg}} = 0.490\\text{ N/m}$ and convert the result to atmospheres ($1\\text{ atm} \\approx 1.013 \\times 10^5\\text{ Pa}$)."
        ],
        "answer": "(a) $\\Delta p = \\frac{4\\alpha}{d} = 13\\text{ atm}$; (b) $\\Delta p = \\frac{8\\alpha}{d} = 1.2 \\times 10^{-3}\\text{ atm}$",
        "solution": "**1. Droplet of Mercury:**\nA liquid droplet has a single spherical interface. The capillary Laplace pressure is:\n$$\\Delta p = \\frac{2\\alpha}{r} = \\frac{4\\alpha}{d}$$\nUsing $\\alpha_{\\text{Hg}} = 0.490\\text{ N/m}$ and $d = 1.5 \\times 10^{-6}\\text{ m}$:\n$$\\Delta p = \\frac{4 \\times 0.490}{1.5 \\times 10^{-6}} = 1.31 \\times 10^6\\text{ Pa} \\approx 13\\text{ atm}$$\n\n**2. Soap Bubble:**\nA bubble has two spherical interfaces (inside and outside of the thin liquid film):\n$$\\Delta p = \\frac{4\\alpha}{r} = \\frac{8\\alpha}{d}$$\nWith $\\alpha = 45 \\times 10^{-3}\\text{ N/m}$ and $d = 3.0 \\times 10^{-3}\\text{ m}$:\n$$\\Delta p = \\frac{8 \\times 0.045}{3.0 \\times 10^{-3}} = 120\\text{ Pa} \\approx 1.2 \\times 10^{-3}\\text{ atm}$$",
        "tags": ["surface tension", "Laplace pressure", "mercury droplet", "soap bubble"]
    },
    {
        "id": "2.161",
        "title": "Maximum Layer of Mercury Over a Round Hole",
        "difficulty": 1,
        "question": "In the bottom of a vessel with mercury there is a round hole of diameter $d = 70\\,\\mu\\text{m}$. At what maximum thickness of the mercury layer will the liquid still not flow out through this hole?",
        "hints": [
            "Mercury does not wet glass/container material (convex meniscus bulging downward).",
            "The maximum capillary pressure opposing liquid outflow occurs when the meniscus forms a hemisphere of radius $R = d/2$.",
            "Equate hydrostatic pressure $\\rho g h$ to maximum capillary Laplace pressure $\\Delta p = \\frac{4\\alpha}{d}$."
        ],
        "answer": "$h = \\frac{4\\alpha}{\\rho g d} = 21\\text{ cm}$",
        "solution": "**1. Condition of Equilibrium:**\nMercury is a non-wetting liquid. As the liquid tries to leak through the circular hole of diameter $d$, a convex meniscus bulges downwards at the bottom of the aperture. The maximum capillary back-pressure the meniscus can provide without bursting corresponds to a hemispherical shape with radius of curvature $R = d/2$:\n$$\\Delta p_{\\max} = \\frac{2\\alpha}{R} = \\frac{4\\alpha}{d}$$\n\n**2. Maximum Height of Liquid:**\nFor the liquid not to flow out, the hydrostatic pressure at the bottom must not exceed $\\Delta p_{\\max}$:\n$$\\rho g h \\le \\frac{4\\alpha}{d} \\implies h_{\\max} = \\frac{4\\alpha}{\\rho g d}$$\nUsing $\\alpha = 0.49\\text{ N/m}$, $\\rho = 13.6 \\times 10^3\\text{ kg/m}^3$, $g = 9.8\\text{ m/s}^2$, and $d = 70 \\times 10^{-6}\\text{ m}$:\n$$h = \\frac{4 \\times 0.49}{13.6 \\times 10^3 \\times 9.8 \\times 70 \\times 10^{-6}} = \\frac{1.96}{9.33} \\approx 0.21\\text{ m} = 21\\text{ cm}$$",
        "tags": ["capillary pressure", "surface tension", "hydrostatics", "non-wetting"]
    },
    {
        "id": "2.162",
        "title": "Surface Tension from Isothermal Bubble Expansion",
        "difficulty": 2,
        "question": "A vessel filled with air under pressure $p_0$ contains a soap bubble of diameter $d$. The air pressure having been reduced isothermally $n$-fold, the bubble diameter increased $\\eta$-fold. Find the surface tension of the soap-water solution.",
        "hints": [
            "Write the internal pressure of the bubble in terms of outside pressure: $p_{\\text{in}} = p_{\\text{out}} + \\frac{8\\alpha}{d}$.",
            "The volume of the bubble is $V = \\frac{\\pi}{6} d^3$.",
            "Apply Boyle's law for the isothermal expansion of the trapped gas inside the bubble: $p_{\\text{in}, 1} V_1 = p_{\\text{in}, 2} V_2$."
        ],
        "answer": "$\\alpha = \\frac{1}{8} p_0 d \\frac{1 - \\eta^3/n}{\\eta^2 - 1}$",
        "solution": "**1. Initial and Final States of the Bubble:**\n- Initial state: outside pressure is $p_0$, diameter is $d$.\n  The internal pressure is:\n  $$p_1 = p_0 + \\frac{8\\alpha}{d}, \\quad V_1 = \\frac{\\pi}{6} d^3$$\n- Final state: outside pressure is $p_0/n$, diameter is $\\eta d$.\n  The internal pressure is:\n  $$p_2 = \\frac{p_0}{n} + \\frac{8\\alpha}{\\eta d}, \\quad V_2 = \\frac{\\pi}{6} (\\eta d)^3 = \\eta^3 V_1$$\n\n**2. Isothermal Condition:**\nSince the gas inside expands isothermally at temperature $T$:\n$$p_1 V_1 = p_2 V_2 \\implies p_1 = \\eta^3 p_2$$\n$$\\left( p_0 + \\frac{8\\alpha}{d} \\right) = \\eta^3 \\left( \\frac{p_0}{n} + \\frac{8\\alpha}{\\eta d} \\right) = \\frac{\\eta^3}{n} p_0 + \\frac{8\\alpha \\eta^2}{d}$$\n\n**3. Solving for $\\alpha$:**\n$$\\frac{8\\alpha}{d} (\\eta^2 - 1) = p_0 \\left( 1 - \\frac{\\eta^3}{n} \\right)$$\n$$\\alpha = \\frac{1}{8} p_0 d \\frac{1 - \\eta^3/n}{\\eta^2 - 1}$$",
        "tags": ["soap bubble", "surface tension", "isothermal expansion", "Boyle's law"]
    },
    {
        "id": "2.163",
        "title": "Pressure Inside an Underwater Air Bubble",
        "difficulty": 1,
        "question": "Find the pressure in an air bubble of diameter $d = 4.0\\,\\mu\\text{m}$, located in water at a depth $h = 5.0\\text{ m}$. The atmospheric pressure has the standard value $p_0$.",
        "hints": [
            "The pressure in water at depth $h$ is $p_{\\text{w}} = p_0 + \\rho g h$.",
            "Across the spherical interface, surface tension adds Laplace excess pressure: $\\Delta p = \\frac{4\\alpha}{d}$.",
            "The internal pressure is $p = p_0 + \\rho g h + \\frac{4\\alpha}{d}$."
        ],
        "answer": "$p = p_0 + \\rho g h + \\frac{4\\alpha}{d} = 2.2\\text{ atm}$",
        "solution": "**1. Pressure Components:**\nThe pressure inside an air bubble underwater is balanced by:\n- Atmospheric pressure $p_0 = 1.013 \\times 10^5\\text{ Pa} \\approx 1.0\\text{ atm}$\n- Hydrostatic pressure of the water column: $p_{\\text{hydro}} = \\rho g h$\n- Laplace capillary pressure of the spherical bubble surface: $\\Delta p_{\\text{cap}} = \\frac{2\\alpha}{r} = \\frac{4\\alpha}{d}$\n\n**2. Total Pressure:**\n$$p = p_0 + \\rho g h + \\frac{4\\alpha}{d}$$\nUsing $\\rho = 1000\\text{ kg/m}^3$, $g = 9.8\\text{ m/s}^2$, $h = 5.0\\text{ m}$, $\\alpha = 0.073\\text{ N/m}$, and $d = 4.0 \\times 10^{-6}\\text{ m}$:\n$$p_{\\text{hydro}} = 1000 \\times 9.8 \\times 5.0 = 4.9 \\times 10^4\\text{ Pa} \\approx 0.48\\text{ atm}$$\n$$\\Delta p_{\\text{cap}} = \\frac{4 \\times 0.073}{4.0 \\times 10^{-6}} = 7.3 \\times 10^4\\text{ Pa} \\approx 0.72\\text{ atm}$$\n$$p = 1.013 \\times 10^5 + 4.9 \\times 10^4 + 7.3 \\times 10^4 = 2.23 \\times 10^5\\text{ Pa} \\approx 2.2\\text{ atm}$$",
        "tags": ["air bubble", "Laplace pressure", "hydrostatic pressure"]
    },
    {
        "id": "2.164",
        "title": "Depth of Pond from Rising Gas Bubble",
        "difficulty": 2,
        "question": "The diameter of a gas bubble formed at the bottom of a pond is $d = 4.0\\,\\mu\\text{m}$. When the bubble rises to the surface its diameter increases $\\eta = 1.1$ times. Find how deep is the pond at that spot. The atmospheric pressure is standard, the gas expansion is assumed to be isothermal.",
        "hints": [
            "At depth $h$, pressure is $p_1 = p_0 + \\rho g h + \\frac{4\\alpha}{d}$.",
            "At the surface, pressure is $p_2 = p_0 + \\frac{4\\alpha}{\\eta d}$.",
            "Isothermal condition gives $p_1 V_1 = p_2 V_2 \\implies p_1 = \\eta^3 p_2$."
        ],
        "answer": "$h = \\frac{1}{\\rho g} \\left[ p_0 (\\eta^3 - 1) + \\frac{4\\alpha}{d}(\\eta^2 - 1) \\right] = 5.0\\text{ m}$",
        "solution": "**1. Pressures and Volumes:**\n- At the bottom (depth $h$):\n  $$p_1 = p_0 + \\rho g h + \\frac{4\\alpha}{d}, \\quad V_1 = \\frac{\\pi}{6} d^3$$\n- At the surface:\n  $$p_2 = p_0 + \\frac{4\\alpha}{\\eta d}, \\quad V_2 = \\frac{\\pi}{6} (\\eta d)^3 = \\eta^3 V_1$$\n\n**2. Isothermal Expansion:**\n$$p_1 V_1 = p_2 V_2 \\implies p_1 = \\eta^3 p_2$$\n$$p_0 + \\rho g h + \\frac{4\\alpha}{d} = \\eta^3 \\left( p_0 + \\frac{4\\alpha}{\\eta d} \\right) = \\eta^3 p_0 + \\frac{4\\alpha \\eta^2}{d}$$\n\n**3. Depth $h$:**\n$$\\rho g h = p_0 (\\eta^3 - 1) + \\frac{4\\alpha}{d} (\\eta^2 - 1)$$\n$$h = \\frac{1}{\\rho g} \\left[ p_0 (\\eta^3 - 1) + \\frac{4\\alpha}{d} (\\eta^2 - 1) \\right]$$\nWith $\\eta = 1.1$, $\\eta^3 - 1 = 1.331 - 1 = 0.331$, $\\eta^2 - 1 = 1.21 - 1 = 0.21$:\n$$p_0 (\\eta^3 - 1) = 1.013 \\times 10^5 \\times 0.331 \\approx 3.35 \\times 10^4\\text{ Pa}$$\n$$\\frac{4\\alpha}{d} (\\eta^2 - 1) = \\frac{4 \\times 0.073}{4.0 \\times 10^{-6}} \\times 0.21 = 7.3 \\times 10^4 \\times 0.21 \\approx 1.53 \\times 10^4\\text{ Pa}$$\n$$h = \\frac{3.35 \\times 10^4 + 1.53 \\times 10^4}{1000 \\times 9.8} = \\frac{4.88 \\times 10^4}{9800} \\approx 5.0\\text{ m}$$",
        "tags": ["gas bubble", "pond depth", "surface tension", "Boyle's law"]
    },
    {
        "id": "2.165",
        "title": "Level Difference of Mercury in Two Communicating Capillaries",
        "difficulty": 1,
        "question": "Find the difference in height of mercury columns in two communicating vertical capillaries whose diameters are $d_1 = 0.50\\text{ mm}$ and $d_2 = 1.00\\text{ mm}$, if the contact angle $\\theta = 138^\\circ$.",
        "hints": [
            "In each capillary, the depression height is $h_i = \\frac{4\\alpha \\cos\\theta}{\\rho g d_i}$.",
            "Since $\\theta > 90^\\circ$, $\\cos\\theta < 0$, meaning the mercury level is depressed.",
            "The difference in height between the two columns is $\\Delta h = |h_1 - h_2| = \\frac{4\\alpha |\\cos\\theta|}{\\rho g} \\left(\\frac{1}{d_1} - \\frac{1}{d_2}\\right)$."
        ],
        "answer": "$\\Delta h = \\frac{4\\alpha |\\cos\\theta|}{\\rho g} \\left( \\frac{1}{d_1} - \\frac{1}{d_2} \\right) = 11\\text{ mm}$",
        "solution": "**1. Capillary Depression:**\nFor a non-wetting liquid ($\\theta = 138^\\circ$), the meniscus is convex and capillary depression occurs. The depth of depression in tube $i$ is:\n$$h_i = \\frac{4\\alpha |\\cos\\theta|}{\\rho g d_i}$$\n\n**2. Difference in Level:**\n$$\\Delta h = h_1 - h_2 = \\frac{4\\alpha |\\cos\\theta|}{\\rho g} \\left( \\frac{1}{d_1} - \\frac{1}{d_2} \\right)$$\nUsing $\\alpha = 0.49\\text{ N/m}$, $\\rho = 13.6 \\times 10^3\\text{ kg/m}^3$, $|\\cos 138^\\circ| \\approx 0.743$, $d_1 = 0.50 \\times 10^{-3}\\text{ m}$, $d_2 = 1.00 \\times 10^{-3}\\text{ m}$:\n$$\\frac{1}{d_1} - \\frac{1}{d_2} = 2000 - 1000 = 1000\\text{ m}^{-1}$$\n$$\\Delta h = \\frac{4 \\times 0.49 \\times 0.743}{13.6 \\times 10^3 \\times 9.8} \\times 1000 = \\frac{1.456}{133.28} \\approx 1.1 \\times 10^{-2}\\text{ m} = 11\\text{ mm}$$",
        "tags": ["communicating vessels", "capillary depression", "mercury", "contact angle"]
    },
    {
        "id": "2.166",
        "title": "Curvature Radius of Meniscus in an Insufficiently Long Capillary",
        "difficulty": 2,
        "question": "A vertical capillary with inside diameter $d = 0.50\\text{ mm}$ is submerged into water so that the length of its part protruding over the water surface is equal to $h = 25\\text{ mm}$. Find the curvature radius of the meniscus.",
        "hints": [
            "Check what the normal capillary rise $h_0 = \\frac{4\\alpha}{\\rho g d}$ would be for complete wetting.",
            "If $h < h_0$, water rises to the very top edge and the meniscus flattens to adjust its radius of curvature $R$.",
            "At equilibrium, hydrostatic head balances the capillary pressure: $\\rho g h = \\frac{2\\alpha}{R}$."
        ],
        "answer": "$R = \\frac{2\\alpha}{\\rho g h} = 0.6\\text{ mm}$",
        "solution": "**1. Normal Capillary Rise:**\nFor water with complete wetting ($\\theta = 0$):\n$$h_0 = \\frac{4\\alpha}{\\rho g d} = \\frac{4 \\times 0.073}{1000 \\times 9.8 \\times 0.50 \\times 10^{-3}} \\approx 0.060\\text{ m} = 60\\text{ mm}$$\n\n**2. Insufficient Height:**\nSince the protruding height $h = 25\\text{ mm} < h_0$, the liquid reaches the very top rim of the capillary tube without overflowing. The meniscus adjusts its curvature radius $R$ until the capillary pressure balances the hydrostatic column of height $h$:\n$$\\rho g h = \\frac{2\\alpha}{R} \\implies R = \\frac{2\\alpha}{\\rho g h}$$\n\n**3. Numerical Calculation:**\n$$R = \\frac{2 \\times 0.073}{1000 \\times 9.8 \\times 0.025} = \\frac{0.146}{245} \\approx 5.96 \\times 10^{-4}\\text{ m} \\approx 0.60\\text{ mm}$$",
        "tags": ["capillary rise", "curvature radius", "meniscus", "insufficient height"]
    },
    {
        "id": "2.167",
        "title": "Submersion Depth of Sealed Capillary for Equal Levels",
        "difficulty": 2,
        "question": "A glass capillary of length $l = 110\\text{ mm}$ and inside diameter $d = 20\\,\\mu\\text{m}$ is submerged vertically into water. The upper end of the capillary is sealed. The outside pressure is standard. To what length $x$ has the capillary to be submerged to make the water levels inside and outside the capillary coincide?",
        "hints": [
            "When the water levels inside and outside coincide, the meniscus is at depth $x$ below the water surface, so the water pressure at the meniscus is $p_0$.",
            "Across the concave meniscus (wetting), the trapped air pressure inside is higher: $p = p_0 + \\frac{4\\alpha}{d}$.",
            "Use Boyle's law for the trapped air of original length $l$ compressed to length $l - x$."
        ],
        "answer": "$x = \\frac{l}{1 + \\frac{p_0 d}{4\\alpha}} = 1.4\\text{ cm}$",
        "solution": "**1. Trapped Gas Pressure:**\nWhen the water levels inside and outside coincide, the liquid pressure just beneath the meniscus equals atmospheric pressure $p_0$. Because water wets glass completely, the meniscus is concave towards the trapped air, giving a capillary Laplace pressure drop:\n$$p_{\\text{water}} = p - \\frac{4\\alpha}{d} = p_0 \\implies p = p_0 + \\frac{4\\alpha}{d}$$\n\n**2. Boyle's Law:**\nThe original length of the air column was $l$ at pressure $p_0$. After submersion to depth $x$, the length of the air column is $l - x$ at pressure $p$:\n$$p_0 l = p (l - x) = \\left( p_0 + \\frac{4\\alpha}{d} \\right) (l - x)$$\n$$1 - \\frac{x}{l} = \\frac{p_0}{p_0 + \\frac{4\\alpha}{d}} \\implies \\frac{x}{l} = \\frac{\\frac{4\\alpha}{d}}{p_0 + \\frac{4\\alpha}{d}} = \\frac{1}{1 + \\frac{p_0 d}{4\\alpha}}$$\n$$x = \\frac{l}{1 + \\frac{p_0 d}{4\\alpha}}$$\n\n**3. Numerical Evaluation:**\n$$\\frac{p_0 d}{4\\alpha} = \\frac{1.013 \\times 10^5 \\times 20 \\times 10^{-6}}{4 \\times 0.073} = \\frac{2.026}{0.292} \\approx 6.94$$\n$$x = \\frac{110\\text{ mm}}{1 + 6.94} = \\frac{110}{7.94} \\approx 13.9\\text{ mm} \\approx 1.4\\text{ cm}$$",
        "tags": ["sealed capillary", "Boyle's law", "submersion", "Laplace pressure"]
    },
    {
        "id": "2.168",
        "title": "Surface Tension from Liquid Rise in a Sealed Capillary",
        "difficulty": 2,
        "question": "When a vertical capillary of length $l$ with the sealed upper end was brought in contact with the surface of a liquid, the level of this liquid rose to the height $h$. The liquid density is $\\rho$, the inside diameter of the capillary is $d$, the contact angle is $\\theta$, the atmospheric pressure is $p_0$. Find the surface tension of the liquid.",
        "hints": [
            "The trapped air column is compressed from initial length $l$ to final length $l - h$.",
            "The pressure of the compressed air is $p = p_0 \\frac{l}{l - h}$.",
            "The hydrostatic pressure balance at the meniscus is $p_0 - p_{\\text{liq}} = \\rho g h$, where $p_{\\text{liq}} = p - \\frac{4\\alpha \\cos\\theta}{d}$."
        ],
        "answer": "$\\alpha = \\frac{d}{4\\cos\\theta} \\left[ \\rho g h + p_0 \\frac{h}{l - h} \\right]$",
        "solution": "**1. Compressed Air Pressure:**\nAssuming isothermal compression of the trapped air column:\n$$p_0 (S l) = p S (l - h) \\implies p = p_0 \\frac{l}{l - h}$$\n\n**2. Pressure Balance at the Meniscus:**\nAt height $h$ above the free surface of the reservoir, the hydrostatic pressure in the liquid is:\n$$p_{\\text{liq}} = p_0 - \\rho g h$$\nAcross the curved meniscus, the pressure jump is given by the Laplace formula:\n$$p - p_{\\text{liq}} = \\frac{4\\alpha \\cos\\theta}{d}$$\nSubstituting $p$ and $p_{\\text{liq}}$:\n$$\\frac{4\\alpha \\cos\\theta}{d} = p_0 \\frac{l}{l - h} - (p_0 - \\rho g h) = \\rho g h + p_0 \\left( \\frac{l}{l - h} - 1 \\right) = \\rho g h + p_0 \\frac{h}{l - h}$$\n\n**3. Surface Tension:**\n$$\\alpha = \\frac{d}{4\\cos\\theta} \\left[ \\rho g h + p_0 \\frac{h}{l - h} \\right]$$",
        "tags": ["sealed capillary", "surface tension", "hydrostatic balance", "contact angle"]
    },
    {
        "id": "2.169",
        "title": "Capillary Rise in an Annular Gap",
        "difficulty": 2,
        "question": "A glass rod of diameter $d_1 = 1.5\\text{ mm}$ is inserted symmetrically into a glass capillary with inside diameter $d_2 = 2.0\\text{ mm}$. Then the whole arrangement is vertically oriented and brought in contact with the surface of water. To what height will the water rise in the capillary?",
        "hints": [
            "Identify the cross-sectional area of the annular gap: $S = \\frac{\\pi}{4} (d_2^2 - d_1^2)$.",
            "The total wetted perimeter consists of the inner capillary wall and the outer rod surface: $L = \\pi (d_1 + d_2)$.",
            "Equate the total upward capillary force $F = \\alpha L$ to the weight of the water column $W = \\rho g h S$."
        ],
        "answer": "$h = \\frac{4\\alpha}{\\rho g (d_2 - d_1)} = 6.0\\text{ cm}$",
        "solution": "**1. Capillary and Gravitational Forces:**\n- Upward surface tension force acting along both boundaries (rod surface and tube wall, complete wetting $\\theta = 0$):\n  $$F = \\alpha \\pi (d_1 + d_2)$$\n- Weight of the annular liquid column of height $h$:\n  $$W = \\rho g h \\cdot \\frac{\\pi}{4} (d_2^2 - d_1^2) = \\rho g h \\cdot \\frac{\\pi}{4} (d_2 - d_1)(d_2 + d_1)$$\n\n**2. Equilibrium Height:**\nEquating $F = W$:\n$$\\alpha \\pi (d_1 + d_2) = \\rho g h \\frac{\\pi}{4} (d_2 - d_1)(d_2 + d_1)$$\n$$h = \\frac{4\\alpha}{\\rho g (d_2 - d_1)}$$\n\n**3. Numerical Evaluation:**\nWith $\\alpha = 0.073\\text{ N/m}$, $\\rho = 1000\\text{ kg/m}^3$, $g = 9.8\\text{ m/s}^2$, and $d_2 - d_1 = 0.50 \\times 10^{-3}\\text{ m}$:\n$$h = \\frac{4 \\times 0.073}{1000 \\times 9.8 \\times 0.50 \\times 10^{-3}} = \\frac{0.292}{4.9} \\approx 0.060\\text{ m} = 6.0\\text{ cm}$$",
        "tags": ["annular capillary", "surface tension", "capillary rise", "water"]
    },
    {
        "id": "2.170",
        "title": "Liquid Rise Profile in a Vertical Wedge",
        "difficulty": 2,
        "question": "Two vertical plates submerged partially in a wetting liquid form a wedge with a very small angle $\\delta\\varphi$. The edge of this wedge is vertical. The density of the liquid is $\\rho$, its surface tension is $\\alpha$, the contact angle is $\\theta$. Find the height $h$, to which the liquid rises, as a function of the distance $x$ from the edge.",
        "hints": [
            "At distance $x$ from the edge, the gap distance between the plates is $d(x) = x \\delta\\varphi$.",
            "Consider a thin vertical column of liquid between $x$ and $x + dx$.",
            "Balance the upward capillary force $2 \\alpha dx \\cos\\theta$ with the weight of the column $\\rho g h(x) d(x) dx$."
        ],
        "answer": "$h(x) = \\frac{2\\alpha \\cos\\theta}{\\rho g x \\delta\\varphi}$",
        "solution": "**1. Geometry of the Wedge:**\nAt a distance $x$ from the vertical edge of the wedge, the separation between the plates is:\n$$d(x) = x \\delta\\varphi$$\n\n**2. Force Equilibrium on Column of Width $dx$:**\n- Upward capillary force on the two walls:\n  $$dF_{\\text{cap}} = 2 (\\alpha dx) \\cos\\theta$$\n- Weight of the liquid column of height $h(x)$, width $dx$, and thickness $d(x)$:\n  $$dW = \\rho g h(x) [x \\delta\\varphi \\, dx]$$\n\n**3. Equilibrium Profile:**\nEquating upward and downward forces:\n$$2 \\alpha \\cos\\theta \\, dx = \\rho g h(x) x \\delta\\varphi \\, dx$$\n$$h(x) = \\frac{2\\alpha \\cos\\theta}{\\rho g x \\delta\\varphi}$$\n(This shows that the profile of the meniscus is an equilateral hyperbola $h(x) \\propto 1/x$.)",
        "tags": ["wedge", "capillary rise", "hyperbolic profile", "surface tension"]
    },
    {
        "id": "2.171",
        "title": "Discharge Rate of an Accelerating Vertical Water Jet",
        "difficulty": 2,
        "question": "A vertical water jet flows out of a round hole. One of the horizontal sections of the jet has the diameter $d_1 = 2.0\\text{ mm}$ while the other section located $l = 20\\text{ mm}$ lower has the diameter which is $n = 1.5$ times less. Find the volume of the water flowing from the hole each second.",
        "hints": [
            "Use the continuity equation for incompressible flow: $V' = v_1 S_1 = v_2 S_2$.",
            "Relate diameters: $S_1 / S_2 = (d_1 / d_2)^2 = n^2$, so $v_2 = n^2 v_1$.",
            "Apply Torricelli / Bernoulli / free fall equation under gravity: $v_2^2 - v_1^2 = 2gl$."
        ],
        "answer": "$V' = \\frac{\\pi d_1^2}{4} \\sqrt{\\frac{2gl}{n^4 - 1}} = 0.96\\text{ cm}^3/\\text{s}$",
        "solution": "**1. Continuity Equation:**\nFor steady incompressible flow, the volume discharge rate $V'$ is constant along the jet:\n$$V' = v_1 \\frac{\\pi d_1^2}{4} = v_2 \\frac{\\pi d_2^2}{4}$$\nSince $d_2 = d_1 / n$, we have:\n$$v_2 = v_1 \\left( \\frac{d_1}{d_2} \\right)^2 = n^2 v_1$$\n\n**2. Velocity from Free Fall:**\nUnder gravity with negligible air drag:\n$$v_2^2 - v_1^2 = 2gl \\implies (n^4 - 1) v_1^2 = 2gl \\implies v_1 = \\sqrt{\\frac{2gl}{n^4 - 1}}$$\n\n**3. Volume Flow Rate:**\n$$V' = \\frac{\\pi d_1^2}{4} \\sqrt{\\frac{2gl}{n^4 - 1}}$$\nUsing $d_1 = 2.0 \\times 10^{-3}\\text{ m}$, $l = 20 \\times 10^{-3}\\text{ m}$, $n = 1.5$ ($n^4 = 5.0625$, $n^4 - 1 = 4.0625$), and $g = 9.8\\text{ m/s}^2$:\n$$v_1 = \\sqrt{\\frac{2 \\times 9.8 \\times 0.020}{4.0625}} = \\sqrt{\\frac{0.392}{4.0625}} \\approx 0.3106\\text{ m/s}$$\n$$V' = \\frac{\\pi}{4} (2.0 \\times 10^{-3})^2 \\times 0.3106 = 3.1416 \\times 10^{-6} \\times 0.3106 \\approx 0.976 \\times 10^{-6}\\text{ m}^3/\\text{s} \\approx 0.96\\text{ cm}^3/\\text{s}$$",
        "tags": ["hydrodynamics", "continuity equation", "falling jet", "discharge rate"]
    },
    {
        "id": "2.172",
        "title": "Curvature Difference of a Falling Raindrop",
        "difficulty": 2,
        "question": "A water drop falls in air with a uniform velocity. Find the difference between the curvature radii of the drop's surface at the upper and lower points of the drop separated by the distance $h = 2.3\\text{ mm}$.",
        "hints": [
            "Falling at uniform velocity implies that internal pressure gradient is purely hydrostatic: $p_2 - p_1 = \\rho g h$.",
            "At the lower point, capillary pressure is $2\\alpha / R_2$; at the upper point, it is $2\\alpha / R_1$.",
            "Assuming nearly spherical shape of radius $R \\approx h/2$, expand $2\\alpha(1/R_1 - 1/R_2) = \\rho g h$."
        ],
        "answer": "$R_2 - R_1 \\approx \\frac{1}{8} \\frac{\\rho g h^3}{\\alpha} = 0.20\\text{ mm}$",
        "solution": "**1. Pressure Difference in the Drop:**\nWhen falling at terminal (uniform) velocity, aerodynamic drag balances gravity over the drop as a whole. Inside the liquid, the pressure difference between the lower point (2) and upper point (1) separated by vertical height $h$ is hydrostatic:\n$$p_2 - p_1 = \\rho g h$$\n\n**2. Laplace Capillary Pressure:**\nSince outside air pressure variation over the drop height is negligible compared to water density:\n$$p_2 - p_1 = 2\\alpha \\left( \\frac{1}{R_1} - \\frac{1}{R_2} \\right) = 2\\alpha \\frac{R_2 - R_1}{R_1 R_2}$$\n\n**3. Approximation for Drop Radius:**\nFor a drop of diameter $h$, $R_1 R_2 \\approx R^2 \\approx (h/2)^2 = \\frac{h^2}{4}$:\n$$2\\alpha \\frac{R_2 - R_1}{h^2 / 4} = \\rho g h \\implies R_2 - R_1 \\approx \\frac{1}{8} \\frac{\\rho g h^3}{\\alpha}$$\n\n**4. Numerical Calculation:**\nUsing $\\rho = 1000\\text{ kg/m}^3$, $g = 9.8\\text{ m/s}^2$, $h = 2.3 \\times 10^{-3}\\text{ m}$, and $\\alpha = 0.073\\text{ N/m}$:\n$$R_2 - R_1 = \\frac{1000 \\times 9.8 \\times (2.3 \\times 10^{-3})^3}{8 \\times 0.073} = \\frac{9.8 \\times 1.2167 \\times 10^{-5}}{0.584} \\approx 2.04 \\times 10^{-4}\\text{ m} = 0.20\\text{ mm}$$",
        "tags": ["falling drop", "Laplace pressure", "terminal velocity", "curvature"]
    },
    {
        "id": "2.173",
        "title": "Compression of a Mercury Drop Tablet Between Plates",
        "difficulty": 3,
        "question": "A mercury drop shaped as a round tablet of radius $R$ and thickness $h$ is located between two horizontal glass plates. Assuming that $h \\ll R$, find the mass $m$ of a weight which has to be placed on the upper plate to diminish the distance between the plates $n$ times. The contact angle equals $\\theta$. Calculate $m$ if $R = 2.0\\text{ cm}$, $h = 0.38\\text{ mm}$, $n = 2.0$, and $\\theta = 135^\\circ$.",
        "hints": [
            "Because mercury is non-wetting ($\\theta = 135^\\circ > 90^\\circ$), the meniscus is convex and exerts an upward repulsive capillary force on the plates.",
            "The capillary pressure is $\\Delta p = \\frac{2\\alpha |\\cos\\theta|}{h}$.",
            "The volume of mercury $V = \\pi R^2 h$ is constant, so when $h' = h/n$, the radius becomes $R' = R \\sqrt{n}$.",
            "The added weight $mg$ must supply the force difference: $mg = \\Delta p' (\\pi R'^2) - \\Delta p (\\pi R^2)$."
        ],
        "answer": "$m \\approx \\frac{2\\pi \\alpha R^2 |\\cos\\theta|}{g h} (n^2 - 1) = 0.70\\text{ kg}$",
        "solution": "**1. Capillary Overpressure Inside Mercury:**\nMercury does not wet glass ($\\theta = 135^\\circ$). The principal radii of curvature of the rim meniscus are $R_1 \\approx h / (2 |\\cos\\theta|)$ in the vertical plane and $R_2 \\approx R$ in the horizontal plane. Since $h \\ll R$, $1/R_2 \\ll 1/R_1$, giving an internal overpressure:\n$$\\Delta p = \\frac{2\\alpha |\\cos\\theta|}{h}$$\n\n**2. Force on the Plate:**\nThe upward force exerted by the mercury tablet on the plate of contact area $S = \\pi R^2$ is:\n$$F = \\Delta p \\cdot \\pi R^2 = \\frac{2\\pi \\alpha R^2 |\\cos\\theta|}{h}$$\n\n**3. Compression to Thickness $h' = h/n$:**\nBy conservation of volume of mercury, $V = \\pi R^2 h = \\pi R'^2 h'$:\n$$R'^2 = n R^2$$\nThe new upward force is:\n$$F' = \\frac{2\\pi \\alpha R'^2 |\\cos\\theta|}{h'} = \\frac{2\\pi \\alpha (n R^2) |\\cos\\theta|}{h / n} = n^2 \\frac{2\\pi \\alpha R^2 |\\cos\\theta|}{h} = n^2 F$$\n\n**4. Mass of the Weight:**\nThe mass $m$ placed on the upper plate balances the increase in capillary force:\n$$m g = F' - F = F (n^2 - 1) = \\frac{2\\pi \\alpha R^2 |\\cos\\theta|}{h} (n^2 - 1)$$\n$$m = \\frac{2\\pi \\alpha R^2 |\\cos\\theta|}{g h} (n^2 - 1)$$\n\n**5. Numerical Calculation:**\nWith $\\alpha = 0.49\\text{ N/m}$, $R = 0.020\\text{ m}$, $|\\cos 135^\\circ| = \\frac{\\sqrt{2}}{2} \\approx 0.7071$, $h = 0.38 \\times 10^{-3}\\text{ m}$, $n = 2.0$ ($n^2 - 1 = 3$), and $g = 9.8\\text{ m/s}^2$:\n$$F = \\frac{2\\pi \\times 0.49 \\times (0.020)^2 \\times 0.7071}{0.38 \\times 10^{-3}} = \\frac{8.706 \\times 10^{-4}}{0.38 \\times 10^{-3}} \\approx 2.29\\text{ N}$$\n$$m = \\frac{2.29 \\times 3}{9.8} \\approx \\frac{6.87}{9.8} \\approx 0.70\\text{ kg}$$",
        "tags": ["mercury tablet", "capillary compression", "contact angle", "non-wetting"]
    },
    {
        "id": "2.174",
        "title": "Attraction Force Between Wet Glass Plates",
        "difficulty": 2,
        "question": "Find the attraction force between two parallel glass plates, separated by a distance $h = 0.10\\text{ mm}$, after a water drop of mass $m = 70\\text{ mg}$ was introduced between them. The wetting is assumed to be complete.",
        "hints": [
            "Water forms a thin circular disc of thickness $h$ and area $S = \\frac{V}{h} = \\frac{m}{\\rho h}$.",
            "Due to concave meniscus at the perimeter (complete wetting), the pressure inside the water film is reduced by $\\Delta p = \\frac{2\\alpha}{h}$.",
            "The attractive force is $F = \\Delta p \\cdot S = \\frac{2\\alpha m}{\\rho h^2}$."
        ],
        "answer": "$F \\approx \\frac{2\\alpha m}{\\rho h^2} = 1.0\\text{ N}$",
        "solution": "**1. Geometry of the Water Film:**\nThe mass of the water drop is $m$, so its volume is $V = m / \\rho$. Squeezed between plates at spacing $h$, it spreads over an area:\n$$S = \\frac{V}{h} = \\frac{m}{\\rho h}$$\n\n**2. Capillary Underpressure:**\nWith complete wetting ($\\theta = 0$), the meniscus at the perimeter is concave with radius $r = h/2$. The Laplace pressure deficit inside the liquid is:\n$$\\Delta p = \\frac{2\\alpha}{h}$$\n\n**3. Attractive Force:**\nThe atmospheric pressure on the outside exceeds the internal liquid pressure, pressing the plates together with force:\n$$F = \\Delta p \\cdot S = \\frac{2\\alpha}{h} \\cdot \\frac{m}{\\rho h} = \\frac{2\\alpha m}{\\rho h^2}$$\nUsing $\\alpha = 0.073\\text{ N/m}$, $m = 70 \\times 10^{-6}\\text{ kg}$, $\\rho = 1000\\text{ kg/m}^3$, and $h = 0.10 \\times 10^{-3}\\text{ m}$:\n$$F = \\frac{2 \\times 0.073 \\times 70 \\times 10^{-6}}{1000 \\times (1.0 \\times 10^{-4})^2} = \\frac{1.022 \\times 10^{-5}}{1.0 \\times 10^{-5}} \\approx 1.0\\text{ N}$$",
        "tags": ["wet glass plates", "capillary attraction", "Laplace underpressure"]
    },
    {
        "id": "2.175",
        "title": "Force to Separate Two Wet Glass Discs",
        "difficulty": 1,
        "question": "Two glass discs of radius $R = 5.0\\text{ cm}$ were wetted with water and put together so that the thickness of the water layer between them was $h = 1.9\\,\\mu\\text{m}$. Assuming the wetting to be complete, find the force that has to be applied at right angles to the plates in order to pull them apart.",
        "hints": [
            "The area of the discs is $S = \\pi R^2$.",
            "The capillary underpressure inside the water layer is $\\Delta p = \\frac{2\\alpha}{h}$.",
            "The separating force must overcome the underpressure: $F = \\Delta p \\cdot S = \\frac{2\\pi R^2 \\alpha}{h}$."
        ],
        "answer": "$F = \\frac{2\\pi R^2 \\alpha}{h} = 0.60\\text{ kN}$",
        "solution": "**1. Underpressure in Thin Water Film:**\nFor complete wetting ($\\theta = 0$), the meniscus along the circumference of the discs has curvature radius $r = h/2$, creating a negative gauge pressure inside the film:\n$$\\Delta p = \\frac{2\\alpha}{h}$$\n\n**2. Force Required to Separate:**\nThe force holding the discs together across area $S = \\pi R^2$ is:\n$$F = \\Delta p \\cdot S = \\frac{2\\pi R^2 \\alpha}{h}$$\nUsing $R = 0.050\\text{ m}$, $\\alpha = 0.073\\text{ N/m}$, and $h = 1.9 \\times 10^{-6}\\text{ m}$:\n$$F = \\frac{2\\pi \\times (0.050)^2 \\times 0.073}{1.9 \\times 10^{-6}} = \\frac{1.147 \\times 10^{-3}}{1.9 \\times 10^{-6}} \\approx 604\\text{ N} \\approx 0.60\\text{ kN}$$",
        "tags": ["glass discs", "adhesion", "capillary underpressure", "surface tension"]
    },
    {
        "id": "2.176",
        "title": "Attraction Between Partially Submerged Vertical Plates",
        "difficulty": 2,
        "question": "Two vertical parallel glass plates are partially submerged in water. The distance between the plates is $d = 0.10\\text{ mm}$, and their width is $l = 12\\text{ cm}$. Assuming that the water between the plates does not reach the upper edges of the plates and that the wetting is complete, find the force of their mutual attraction.",
        "hints": [
            "Water rises between the plates to a height $h = \\frac{2\\alpha}{\\rho g d}$.",
            "At height $z$ above the free surface, the pressure inside the water column is $p(z) = p_0 - \\rho g z$.",
            "Integrate the underpressure $\\Delta p(z) = \\rho g z$ over the height of the column: $F = \\int_0^h \\rho g z \\, l \\, dz$."
        ],
        "answer": "$F = \\frac{2\\alpha^2 l}{\\rho g d^2} = 13\\text{ N}$",
        "solution": "**1. Height of Capillary Rise:**\nBetween two parallel plates separated by distance $d$ with complete wetting:\n$$h = \\frac{2\\alpha}{\\rho g d}$$\n\n**2. Pressure Distribution:**\nAt a height $z$ above the reservoir surface ($0 \\le z \\le h$):\n$$p(z) = p_0 - \\rho g z$$\nThe net inward pressure pressing the plates together at height $z$ is:\n$$\\Delta p(z) = p_0 - p(z) = \\rho g z$$\n\n**3. Total Attractive Force:**\nIntegrating over the wetted area $l \\, dz$:\n$$F = \\int_0^h \\rho g z \\, l \\, dz = \\frac{1}{2} \\rho g l h^2$$\nSubstituting $h = \\frac{2\\alpha}{\\rho g d}$:\n$$F = \\frac{1}{2} \\rho g l \\left( \\frac{2\\alpha}{\\rho g d} \\right)^2 = \\frac{2\\alpha^2 l}{\\rho g d^2}$$\n\n**4. Numerical Evaluation:**\nWith $\\alpha = 0.073\\text{ N/m}$, $l = 0.12\\text{ m}$, $d = 0.10 \\times 10^{-3}\\text{ m}$, $\\rho = 1000\\text{ kg/m}^3$, and $g = 9.8\\text{ m/s}^2$:\n$$F = \\frac{2 \\times (0.073)^2 \\times 0.12}{1000 \\times 9.8 \\times (1.0 \\times 10^{-4})^2} = \\frac{1.279 \\times 10^{-3}}{9.8 \\times 10^{-5}} \\approx 13\\text{ N}$$",
        "tags": ["parallel plates", "capillary rise", "attractive force", "hydrostatics"]
    },
    {
        "id": "2.177",
        "title": "Lifetime of a Deflating Soap Bubble Through a Capillary",
        "difficulty": 2,
        "question": "Find the lifetime of a soap bubble of radius $R$ connected with the atmosphere through a capillary of length $l$ and inside radius $r$. The surface tension is $\\alpha$, the viscosity coefficient of the gas is $\\eta$.",
        "hints": [
            "The excess pressure driving the gas out of the bubble is $\\Delta p = \\frac{4\\alpha}{R'}$, where $R'$ is the instantaneous bubble radius.",
            "Use Poiseuille's formula for the volume flow rate: $-\\frac{dV}{dt} = \\frac{\\pi r^4}{8\\eta l} \\Delta p$.",
            "Express $V = \\frac{4}{3}\\pi R'^3$ so that $dV = 4\\pi R'^2 dR'$, and integrate from $R' = R$ to $R' = 0$."
        ],
        "answer": "$t = \\frac{2\\eta l R^4}{\\alpha r^4}$",
        "solution": "**1. Poiseuille Flow Rate:**\nThe excess Laplace pressure inside the soap bubble of instantaneous radius $R'$ is:\n$$\\Delta p = \\frac{4\\alpha}{R'}$$\nBy Poiseuille's formula, the volume of gas flowing out per unit time through the capillary of radius $r$ and length $l$ is:\n$$-\\frac{dV}{dt} = \\frac{\\pi r^4}{8\\eta l} \\Delta p = \\frac{\\pi r^4}{8\\eta l} \\cdot \\frac{4\\alpha}{R'} = \\frac{\\pi \\alpha r^4}{2\\eta l R'}$$\n\n**2. Differential Equation for $R'(t)$:**\nSince $V = \\frac{4}{3}\\pi R'^3$, we have $\\frac{dV}{dt} = 4\\pi R'^2 \\frac{dR'}{dt}$:\n$$-4\\pi R'^2 \\frac{dR'}{dt} = \\frac{\\pi \\alpha r^4}{2\\eta l R'} \\implies R'^3 dR' = -\\frac{\\alpha r^4}{8\\eta l} dt$$\n\n**3. Integration for Lifetime $t$:**\nIntegrating from $t = 0$ ($R' = R$) to $t$ ($R' = 0$):\n$$\\int_0^R R'^3 dR' = \\frac{R^4}{4} = \\frac{\\alpha r^4}{8\\eta l} t$$\n$$t = \\frac{2\\eta l R^4}{\\alpha r^4}$$",
        "tags": ["soap bubble", "Poiseuille formula", "viscosity", "lifetime"]
    },
    {
        "id": "2.178",
        "title": "Heat Liberated During Capillary Rise",
        "difficulty": 2,
        "question": "A vertical capillary is brought in contact with the water surface. What amount of heat is liberated while the water rises along the capillary? The wetting is assumed to be complete, the surface tension equals $\\alpha$.",
        "hints": [
            "Calculate the work done by surface tension forces during the rise of the liquid column: $A_{\\text{st}} = F_{\\text{st}} h = (2\\pi r \\alpha) h$.",
            "Calculate the gain in gravitational potential energy of the column: $\\Delta U_p = m g \\frac{h}{2}$.",
            "By conservation of energy, the dissipated energy appearing as heat is $Q = A_{\\text{st}} - \\Delta U_p$."
        ],
        "answer": "$Q = \\frac{2\\pi \\alpha^2}{\\rho g}$",
        "solution": "**1. Capillary Height:**\nFor a tube of radius $r$ with complete wetting:\n$$h = \\frac{2\\alpha}{\\rho g r}$$\n\n**2. Work of Surface Tension:**\nThe upward force of surface tension along the meniscus rim is $F_{\\text{st}} = 2\\pi r \\alpha$. It acts through distance $h$:\n$$A_{\\text{st}} = F_{\\text{st}} h = (2\\pi r \\alpha) \\left( \\frac{2\\alpha}{\\rho g r} \\right) = \\frac{4\\pi \\alpha^2}{\\rho g}$$\n\n**3. Gravitational Potential Energy Gain:**\nThe mass of the risen liquid is $m = \\rho \\pi r^2 h$. Its center of mass is raised by $h/2$:\n$$\\Delta U_p = m g \\frac{h}{2} = \\frac{1}{2} \\rho g \\pi r^2 h^2 = \\frac{1}{2} \\rho g \\pi r^2 \\left( \\frac{2\\alpha}{\\rho g r} \\right)^2 = \\frac{2\\pi \\alpha^2}{\\rho g}$$\n\n**4. Liberated Heat:**\nThe difference between the work done by surface tension and the potential energy stored is dissipated as heat by viscous damping:\n$$Q = A_{\\text{st}} - \\Delta U_p = \\frac{4\\pi \\alpha^2}{\\rho g} - \\frac{2\\pi \\alpha^2}{\\rho g} = \\frac{2\\pi \\alpha^2}{\\rho g}$$\n(Notice that $Q$ is completely independent of the capillary radius $r$.)",
        "tags": ["capillary rise", "energy conservation", "dissipated heat", "surface tension"]
    },
    {
        "id": "2.179",
        "title": "Surface Free Energy of Droplet and Bubble",
        "difficulty": 1,
        "question": "Find the free energy of the surface layer of:\n(a) a mercury droplet of diameter $d = 1.4\\text{ mm}$;\n(b) a soap bubble of diameter $d = 6.0\\text{ mm}$ if the surface tension of the soap-water solution is equal to $\\alpha = 45\\text{ mN/m}$.",
        "hints": [
            "The surface free energy is given by $F_s = \\alpha S$, where $S$ is the total area of interface.",
            "(a) A droplet has a single surface of area $S = \\pi d^2$.",
            "(b) A soap bubble has two surfaces (inner and outer), each of area $\\pi d^2$, so $S = 2\\pi d^2$."
        ],
        "answer": "(a) $F_s = \\pi \\alpha d^2 = 3.0\\,\\mu\\text{J}$; (b) $F_s = 2\\pi \\alpha d^2 = 10\\,\\mu\\text{J}$",
        "solution": "**1. Mercury Droplet:**\nA single spherical interface has area $S = 4\\pi (d/2)^2 = \\pi d^2$:\n$$F_s = \\alpha \\pi d^2$$\nUsing $\\alpha_{\\text{Hg}} = 0.490\\text{ N/m}$ and $d = 1.4 \\times 10^{-3}\\text{ m}$:\n$$F_s = 0.490 \\times \\pi \\times (1.4 \\times 10^{-3})^2 \\approx 3.02 \\times 10^{-6}\\text{ J} \\approx 3.0\\,\\mu\\text{J}$$\n\n**2. Soap Bubble:**\nA bubble film has both inner and outer surfaces, giving total area $S = 2 \\pi d^2$:\n$$F_s = 2\\pi \\alpha d^2$$\nUsing $\\alpha = 45 \\times 10^{-3}\\text{ N/m}$ and $d = 6.0 \\times 10^{-3}\\text{ m}$:\n$$F_s = 2\\pi \\times 0.045 \\times (6.0 \\times 10^{-3})^2 \\approx 1.02 \\times 10^{-5}\\text{ J} \\approx 10\\,\\mu\\text{J}$$",
        "tags": ["surface free energy", "mercury droplet", "soap bubble"]
    },
    {
        "id": "2.180",
        "title": "Change in Free Energy on Coalescence of Mercury Droplets",
        "difficulty": 2,
        "question": "Find the increment of the free energy of the surface layer when two identical mercury droplets, each of diameter $d = 1.5\\text{ mm}$, merge isothermally.",
        "hints": [
            "The initial surface free energy of the two droplets is $F_1 = 2 \\times (\\pi \\alpha d^2)$.",
            "By volume conservation, the merged droplet has diameter $D = 2^{1/3} d$.",
            "The final free energy is $F_2 = \\pi \\alpha D^2 = 2^{2/3} \\pi \\alpha d^2$. Calculate $\\Delta F = F_2 - F_1$."
        ],
        "answer": "$\\Delta F = -2\\pi \\alpha d^2 (1 - 2^{-1/3}) = -1.5\\,\\mu\\text{J}$",
        "solution": "**1. Initial Free Energy:**\nTwo droplets of diameter $d$ have total surface area $S_1 = 2 \\pi d^2$:\n$$F_1 = 2\\pi \\alpha d^2$$\n\n**2. Merged Droplet:**\nConserving total volume $V_2 = 2 V_1$:\n$$\\frac{\\pi}{6} D^3 = 2 \\left( \\frac{\\pi}{6} d^3 \\right) \\implies D = 2^{1/3} d$$\nThe new surface area is $S_2 = \\pi D^2 = 2^{2/3} \\pi d^2$, and the final free energy is:\n$$F_2 = 2^{2/3} \\pi \\alpha d^2$$\n\n**3. Free Energy Increment:**\n$$\\Delta F = F_2 - F_1 = \\pi \\alpha d^2 (2^{2/3} - 2) = -2\\pi \\alpha d^2 (1 - 2^{-1/3})$$\nUsing $\\alpha = 0.49\\text{ N/m}$, $d = 1.5 \\times 10^{-3}\\text{ m}$, and $1 - 2^{-1/3} = 1 - 0.7937 = 0.2063$:\n$$\\Delta F = -2\\pi \\times 0.49 \\times (1.5 \\times 10^{-3})^2 \\times 0.2063 \\approx -1.43 \\times 10^{-6}\\text{ J} \\approx -1.5\\,\\mu\\text{J}$$",
        "tags": ["droplet coalescence", "free energy increment", "surface tension"]
    },
    {
        "id": "2.181",
        "title": "Work Required to Blow a Soap Bubble",
        "difficulty": 2,
        "question": "Find the work to be performed in order to blow a soap bubble of radius $R$ if the outside air pressure is equal to $p_0$ and the surface tension of the soap-water solution is equal to $\\alpha$.",
        "hints": [
            "Blowing the bubble requires creating the two surface layers of total area $8\\pi R^2$, requiring surface energy $F = 8\\pi R^2 \\alpha$.",
            "In addition, the gas must be compressed isothermally from the external reservoir at $p_0$ to internal pressure $p = p_0 + \\frac{4\\alpha}{R}$.",
            "The work to deliver gas of volume $V$ into the bubble at pressure $p$ against $p_0$ is $p V \\ln(p/p_0)$."
        ],
        "answer": "$A' = 8\\pi R^2 \\alpha + p V \\ln(p/p_0)$, where $p = p_0 + \\frac{4\\alpha}{R}$ and $V = \\frac{4}{3}\\pi R^3$",
        "solution": "**1. Work of Surface Formation:**\nA soap bubble has two spherical interfaces of radius $R$. The free energy required to form these interfaces is:\n$$F = \\alpha \\cdot 2(4\\pi R^2) = 8\\pi R^2 \\alpha$$\n\n**2. Work of Gas Compression:**\nThe internal pressure inside the bubble is:\n$$p = p_0 + \\frac{4\\alpha}{R}$$\nTo introduce volume $V = \\frac{4}{3}\\pi R^3$ of gas into the bubble at pressure $p$ from an ambient atmosphere at $p_0$ isothermally, the work required from the external blower is:\n$$A_{\\text{gas}} = \\int_{p_0}^p V' dp' = p V \\ln\\left( \\frac{p}{p_0} \\right)$$\n\n**3. Total Work:**\n$$A' = F + p V \\ln\\left( \\frac{p}{p_0} \\right)$$\nwhere $F = 8\\pi R^2 \\alpha$, $p = p_0 + \\frac{4\\alpha}{R}$, and $V = \\frac{4}{3}\\pi R^3$.",
        "tags": ["soap bubble", "work done", "surface tension", "gas compression"]
    },
    {
        "id": "2.182",
        "title": "Heat Capacity Difference of Gas Inside a Soap Bubble",
        "difficulty": 3,
        "question": "A soap bubble of radius $r$ is inflated with an ideal gas. The atmospheric pressure is $p_0$, the surface tension of the soap-water solution is $\\alpha$. Find the difference between the molar heat capacity of the gas during its heating inside the bubble and the molar heat capacity of the gas under constant pressure, $C - C_p$.",
        "hints": [
            "Internal pressure is $p(r) = p_0 + \\frac{4\\alpha}{r}$.",
            "Use the ideal gas law $p V = \\nu R T$ to find $\\nu dT$ in terms of $r$ and $dr$.",
            "Apply the first law: $C = C_v + \\frac{p dV}{\\nu dT}$, and subtract $C_p = C_v + R$."
        ],
        "answer": "$C - C_p = -\\frac{R}{2} \\frac{1}{1 + \\frac{3}{8}\\frac{p_0 r}{\\alpha}}$",
        "solution": "**1. State Equation for Gas in Bubble:**\nThe pressure inside the bubble of radius $r$ is:\n$$p = p_0 + \\frac{4\\alpha}{r}$$\nThe volume is $V = \\frac{4}{3}\\pi r^3$. Therefore:\n$$\\nu R T = p V = \\left( p_0 + \\frac{4\\alpha}{r} \\right) \\left( \\frac{4}{3}\\pi r^3 \\right) = \\frac{4}{3}\\pi p_0 r^3 + \\frac{16}{3}\\pi \\alpha r^2$$\n\n**2. Relation Between $dT$ and $dr$:**\nDifferentiating both sides:\n$$\\nu R dT = \\left( 4\\pi p_0 r^2 + \\frac{32}{3}\\pi \\alpha r \\right) dr$$\n\n**3. Work Done and Heat Capacity:**\nThe work done by the gas in expanding by $dr$ is:\n$$dA = p dV = \\left( p_0 + \\frac{4\\alpha}{r} \\right) (4\\pi r^2 dr)$$\nBy the First Law, the molar heat capacity is:\n$$C = C_v + \\frac{dA}{\\nu dT} = C_v + R \\frac{\\left( p_0 + \\frac{4\\alpha}{r} \\right) 4\\pi r^2 dr}{\\left( 4\\pi p_0 r^2 + \\frac{32}{3}\\pi \\alpha r \\right) dr} = C_v + R \\frac{p_0 + \\frac{4\\alpha}{r}}{p_0 + \\frac{8\\alpha}{3r}}$$\n\n**4. Difference $C - C_p$:**\nSince $C_p = C_v + R$:\n$$C - C_p = R \\left( \\frac{p_0 + \\frac{4\\alpha}{r}}{p_0 + \\frac{8\\alpha}{3r}} - 1 \\right) = R \\frac{\\frac{4\\alpha}{3r}}{p_0 + \\frac{8\\alpha}{3r}} = \\frac{R}{2 + \\frac{3 p_0 r}{4\\alpha}} = -\\frac{R}{2} \\frac{1}{1 + \\frac{3}{8} \\frac{p_0 r}{\\alpha}}$$\n(Note: depending on sign convention of temperature change during expansion/heating, $C - C_p$ has magnitude $\\frac{R/2}{1 + \\frac{3 p_0 r}{8\\alpha}}$).",
        "tags": ["soap bubble", "molar heat capacity", "polytropic process", "ideal gas"]
    },
    {
        "id": "2.183",
        "title": "Carnot Cycle Applied to a Liquid Film",
        "difficulty": 3,
        "question": "Considering the Carnot cycle as applied to a liquid film, show that in an isothermal process the amount of heat required for the formation of a unit area of the surface layer is equal to $q = -T \\frac{d\\alpha}{dT}$, where $\\frac{d\\alpha}{dT}$ is the temperature derivative of the surface tension.",
        "hints": [
            "Construct an infinitesimal Carnot cycle with stretching $d\\sigma$ at temperature $T$, and contraction at $T - dT$.",
            "The work done during the cycle is $dA = -\\frac{d\\alpha}{dT} dT \\, d\\sigma$.",
            "The Carnot efficiency is $\\eta = \\frac{dA}{dQ} = \\frac{dT}{T}$. Solve for $q = \\frac{dQ}{d\\sigma}$."
        ],
        "answer": "$q = -T \\frac{d\\alpha}{dT}$",
        "solution": "**1. Infinitesimal Carnot Cycle:**\nConsider a liquid film of area $\\sigma$ undergoing a reversible Carnot cycle between temperatures $T$ and $T - dT$:\n- Isothermal stretching by $d\\sigma$ at temperature $T$: the work done on the film is $\\alpha(T) d\\sigma$, and heat $dQ = q \\, d\\sigma$ is absorbed.\n- Adiabatic cooling from $T$ to $T - dT$.\n- Isothermal contraction by $d\\sigma$ at $T - dT$: work returned is $\\alpha(T - dT) d\\sigma$.\n- Adiabatic heating back to $T$.\n\n**2. Net Work Performed:**\nThe net work performed during the cycle is:\n$$dA = [\\alpha(T) - \\alpha(T - dT)] d\\sigma = -\\frac{d\\alpha}{dT} dT \\, d\\sigma$$\n\n**3. Carnot Efficiency:**\nFor any Carnot cycle operating between $T$ and $T - dT$, the efficiency is:\n$$\\eta = \\frac{dA}{dQ} = \\frac{dT}{T}$$\nEquating expressions for $dA$:\n$$\\frac{dT}{T} dQ = -\\frac{d\\alpha}{dT} dT \\, d\\sigma \\implies dQ = -T \\frac{d\\alpha}{dT} d\\sigma$$\nTherefore, the heat required per unit area formed is:\n$$q = \\frac{dQ}{d\\sigma} = -T \\frac{d\\alpha}{dT}$$",
        "tags": ["liquid film", "Carnot cycle", "surface tension", "entropy of surface"]
    },
    {
        "id": "2.184",
        "title": "Entropy and Internal Energy Changes of a Soap Film",
        "difficulty": 2,
        "question": "The surface of a soap film was increased isothermally by $\\Delta \\sigma$ at a temperature $T$. Knowing the surface tension of the soap-water solution $\\alpha$ and the temperature coefficient $\\frac{d\\alpha}{dT}$, find the increment:\n(a) of the entropy of the film's surface layer;\n(b) of the internal energy of the surface layer.",
        "hints": [
            "A soap film has two surfaces, so the total increase in surface area is $2\\Delta\\sigma$.",
            "(a) From $q = -T \\frac{d\\alpha}{dT}$ per unit surface area, the heat absorbed is $\\Delta Q = 2 q \\Delta\\sigma$. The entropy change is $\\Delta S = \\frac{\\Delta Q}{T}$.",
            "(b) Apply the first law: $\\Delta U = \\Delta Q + A_{\\text{ext}}$, where $A_{\\text{ext}} = 2\\alpha \\Delta\\sigma$."
        ],
        "answer": "(a) $\\Delta S = -2 \\frac{d\\alpha}{dT} \\Delta\\sigma$; (b) $\\Delta U = 2 \\left( \\alpha - T \\frac{d\\alpha}{dT} \\right) \\Delta\\sigma$",
        "solution": "**1. Total Area Increase:**\nA soap film has two interfaces, so an increase in projected film area by $\\Delta\\sigma$ increases the total surface area by:\n$$\\Delta A = 2\\Delta\\sigma$$\n\n**2. Entropy Increment:**\nThe heat absorbed per unit area during isothermal stretching is $q = -T \\frac{d\\alpha}{dT}$. Thus the total heat absorbed is:\n$$\\Delta Q = 2 q \\Delta\\sigma = -2 T \\frac{d\\alpha}{dT} \\Delta\\sigma$$\nSince the process is isothermal, the entropy change is:\n$$\\Delta S = \\frac{\\Delta Q}{T} = -2 \\frac{d\\alpha}{dT} \\Delta\\sigma$$\n\n**3. Internal Energy Increment:**\nBy the First Law of Thermodynamics, $\\Delta U = \\Delta Q + A$, where the mechanical work done on the film to increase its surface area is $A = 2\\alpha \\Delta\\sigma$:\n$$\\Delta U = 2\\alpha \\Delta\\sigma + \\Delta Q = 2\\alpha \\Delta\\sigma - 2 T \\frac{d\\alpha}{dT} \\Delta\\sigma = 2 \\left( \\alpha - T \\frac{d\\alpha}{dT} \\right) \\Delta\\sigma$$",
        "tags": ["soap film", "surface entropy", "internal energy", "temperature coefficient"]
    }
]
