"""
part3_ch3_5a.py
Curated problems 3.219 to 3.242 (24 problems) of Irodov Chapter 3.5:
Constant Magnetic Field. Magnetics (Part A).
"""

CH3_5A_CURATED = [
    {
        "id": "3.219",
        "title": "Magnetic Induction of Circular Loop at Centre and on Axis",
        "difficulty": 1,
        "question": "A current $I = 1.00\\text{ A}$ circulates in a round thin-wire loop of radius $R = 100\\text{ mm}$. Find the magnetic induction:\n(a) at the centre of the loop;\n(b) on the axis of the loop at distance $x = 100\\text{ mm}$ from its centre.",
        "hints": [
            "(a) At the centre of a circular loop, $B = \\frac{\\mu_0 I}{2R}$.",
            "(b) On the axis of a circular loop at distance $x$, $B(x) = \\frac{\\mu_0 I R^2}{2(R^2 + x^2)^{3/2}}$.",
            "Substitute $x = R$ into the axial field formula."
        ],
        "answer": "(a) $B = \\frac{\\mu_0 I}{2R} = 6.3\\,\\mu\\text{T}$; (b) $B = \\frac{\\mu_0 I R^2}{2(R^2 + x^2)^{3/2}} = 2.3\\,\\mu\\text{T}$",
        "solution": "**(a) At the Centre of the Loop ($x = 0$):**\nBy the Biot-Savart law:\n$$B(0) = \\frac{\\mu_0 I}{2R}$$\nNumerical evaluation with $I = 1.00\\text{ A}$, $R = 0.100\\text{ m}$, and $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ H/m}$:\n$$B(0) = \\frac{(4\\pi \\times 10^{-7})(1.00)}{2(0.100)} = 2\\pi \\times 10^{-6}\\text{ T} \\approx 6.3\\,\\mu\\text{T}$$\n\n**(b) On the Axis at Distance $x = R$:**\n$$B(x) = \\frac{\\mu_0 I R^2}{2(R^2 + x^2)^{3/2}}$$\nSetting $x = R$:\n$$B(R) = \\frac{\\mu_0 I R^2}{2(2R^2)^{3/2}} = \\frac{\\mu_0 I}{4\\sqrt{2} R} = \\frac{B(0)}{2\\sqrt{2}}$$\n$$B(R) = \\frac{6.28\\,\\mu\\text{T}}{2.828} \\approx 2.3\\,\\mu\\text{T}$$",
        "tags": ["Biot Savart law", "circular loop", "axial magnetic field", "magnetic induction"]
    },
    {
        "id": "3.220",
        "title": "Magnetic Induction at Centre of Regular Polygon Loop",
        "difficulty": 2,
        "question": "A current $I$ flows along a thin wire shaped as a regular polygon with $n$ sides inscribed in a circle of radius $R$. Find the magnetic induction at the centre of the polygon, and analyse the result for $n \\to \\infty$.",
        "hints": [
            "Distance from the centre to each side: $d = R \\cos(\\pi/n)$.",
            "Half-length of each side is $R \\sin(\\pi/n)$, subtending half-angle $\\alpha = \\pi/n$.",
            "Field from one straight segment: $B_1 = \\frac{\\mu_0 I}{4\\pi d} 2\\sin(\\pi/n) = \\frac{\\mu_0 I}{2\\pi R} \\tan(\\pi/n)$.",
            "Total field from $n$ sides: $B = n B_1 = \\frac{\\mu_0 n I}{2\\pi R} \\tan(\\pi/n)$."
        ],
        "answer": "$B = \\frac{\\mu_0 n I}{2\\pi R} \\tan\\left(\\frac{\\pi}{n}\\right)$; as $n \\to \\infty$, $B \\to \\frac{\\mu_0 I}{2R}$",
        "solution": "**1. Field of a Single Side:**\nFor a regular $n$-sided polygon, each straight wire segment subtends angle $2\\pi/n$ at the centre.\nThe perpendicular distance from the centre to each side is:\n$$d = R \\cos\\left(\\frac{\\pi}{n}\\right)$$\nThe field produced by one straight segment is:\n$$B_1 = \\frac{\\mu_0 I}{4\\pi d} [\\sin\\alpha_1 + \\sin\\alpha_2] = \\frac{\\mu_0 I}{4\\pi R \\cos(\\pi/n)} \\left[ 2\\sin\\left(\\frac{\\pi}{n}\\right) \\right] = \\frac{\\mu_0 I}{2\\pi R} \\tan\\left(\\frac{\\pi}{n}\\right)$$\n\n**2. Total Field at the Centre:**\nSince all $n$ sides produce fields pointing in the same direction:\n$$B = n B_1 = \\frac{\\mu_0 n I}{2\\pi R} \\tan\\left(\\frac{\\pi}{n}\\right)$$\n\n**3. Limit $n \\to \\infty$ (Circular Loop):**\nAs $n \\to \\infty$, $\\tan(\\pi/n) \\approx \\pi/n$:\n$$\\lim_{n \\to \\infty} B = \\frac{\\mu_0 I}{2\\pi R} \\lim_{n \\to \\infty} \\left[ n \\cdot \\frac{\\pi}{n} \\right] = \\frac{\\mu_0 I}{2R}$$",
        "tags": ["regular polygon", "Biot Savart law", "limiting case", "circular loop"]
    },
    {
        "id": "3.221",
        "title": "Magnetic Field at Centre of Rectangular Frame",
        "difficulty": 2,
        "question": "Find the magnetic induction at the centre of a rectangular wire frame with diagonal $d = 16\\text{ cm}$ and angle $\\varphi = 30^\\circ$ between diagonals, carrying current $I = 5.0\\text{ A}$.",
        "hints": [
            "Use the Biot-Savart formula for straight segments of a rectangle.",
            "The sum of contributions from all four sides simplifies in terms of diagonal $d$ and angle $\\varphi$ to $B = \\frac{4\\mu_0 I}{\\pi d} \\sin\\varphi$.",
            "Substitute given numerical values."
        ],
        "answer": "$B = \\frac{4\\mu_0 I}{\\pi d} \\sin\\varphi = 0.10\\text{ mT}$",
        "solution": "**1. Geometry of Rectangular Frame:**\nLet the diagonal be $d$ and angle between diagonals be $\\varphi$.\nThe sides of the rectangle are $a = d \\sin(\\varphi/2)$ and $b = d \\cos(\\varphi/2)$.\n\n**2. Summing Contributions from All Four Sides:**\nEach pair of opposite sides contributes:\n$$B = 2 B_a + 2 B_b = \\frac{4\\mu_0 I}{\\pi d} \\sin\\varphi$$\n\n**3. Numerical Evaluation:**\nGiven $I = 5.0\\text{ A}$, $d = 0.16\\text{ m}$, $\\varphi = 30^\\circ$, and $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ H/m}$:\n$$B = \\frac{4(4\\pi \\times 10^{-7})(5.0)}{\\pi (0.16)} \\sin 30^\\circ = \\frac{80 \\times 10^{-7}}{0.16} \\times 0.5 = 5.0 \\times 10^{-5} \\times 2 = 1.0 \\times 10^{-4}\\text{ T} = 0.10\\text{ mT}$$",
        "tags": ["rectangular frame", "Biot Savart law", "magnetic induction", "geometry"]
    },
    {
        "id": "3.222",
        "title": "Magnetic Field of Wire with Circular Arc and Straight Leads",
        "difficulty": 2,
        "question": "A current $I = 5.0\\text{ A}$ flows along a thin wire having a circular curved part of radius $R = 120\\text{ mm}$ and two semi-infinite straight leads forming angle $2\\varphi = 90^\\circ$. Find the magnetic induction at point $O$ (the centre of curvature).",
        "hints": [
            "Break the wire into the circular arc and two semi-infinite straight segments.",
            "The arc of angle $2\\pi - 2\\varphi$ contributes $B_{\\text{arc}} = \\frac{\\mu_0 I}{4\\pi R}(2\\pi - 2\\varphi)$.",
            "The two straight segments contribute $B_{\\text{leads}} = 2 \\times \\frac{\\mu_0 I}{4\\pi R} \\tan\\varphi$."
        ],
        "answer": "$B = \\frac{\\mu_0 I}{2\\pi R} (\\pi - \\varphi + \\tan\\varphi) = 28\\,\\mu\\text{T}$",
        "solution": "**1. Contribution from Circular Arc:**\nThe circular arc spans angle $2(\\pi - \\varphi)$:\n$$B_{\\text{arc}} = \\frac{\\mu_0 I}{4\\pi R} \\cdot 2(\\pi - \\varphi) = \\frac{\\mu_0 I}{2\\pi R} (\\pi - \\varphi)$$\n\n**2. Contribution from the Two Straight Leads:**\nEach semi-infinite straight lead extends tangentially from the arc ends. Perpendicular distance to the line is $R$, and angle subtended runs from $0$ to $\\varphi$:\n$$B_{\\text{lead}} = \\frac{\\mu_0 I}{4\\pi R} \\tan\\varphi$$\nFor both symmetric leads:\n$$B_{\\text{leads}} = 2 \\times \\frac{\\mu_0 I}{4\\pi R} \\tan\\varphi = \\frac{\\mu_0 I}{2\\pi R} \\tan\\varphi$$\n\n**3. Resultant Field:**\n$$B = \\frac{\\mu_0 I}{2\\pi R} (\\pi - \\varphi + \\tan\\varphi)$$\nWith $2\\varphi = 90^\\circ \\implies \\varphi = \\pi/4$, $\\tan\\varphi = 1$, $R = 0.120\\text{ m}$, $I = 5.0\\text{ A}$:\n$$B = \\frac{(4\\pi \\times 10^{-7})(5.0)}{2\\pi (0.120)} \\left( \\frac{3\\pi}{4} + 1 \\right) \\approx 28\\,\\mu\\text{T}$$",
        "tags": ["circular arc", "straight leads", "superposition", "Biot Savart law"]
    },
    {
        "id": "3.223",
        "title": "Magnetic Field at Centre of Complex Planar Loops",
        "difficulty": 2,
        "question": "Find the magnetic induction at point $O$ of a current loop carrying current $I$ for:\n(a) two concentric circular arcs of radii $a$ and $b$ subtending angle $\\varphi$, connected by radial segments;\n(b) a circular arc of radius $a$ and straight segments of length $b$.",
        "hints": [
            "(a) Radial straight segments point directly toward $O$, contributing zero field ($d\\mathbf{l} \\times \\hat{\\mathbf{r}} = 0$). Only the circular arcs of radii $a$ and $b$ contribute.",
            "(b) Sum the contributions of the arc of radius $a$ and the straight chords."
        ],
        "answer": "(a) $B = \\frac{\\mu_0 I}{4\\pi} \\left(\\frac{1}{a} - \\frac{1}{b}\\right) (2\\pi - \\varphi)$; (b) $B = \\frac{\\mu_0 I}{4\\pi} \\left( \\frac{3\\pi}{2a} + \\frac{2}{b} \\right)$",
        "solution": "**(a) Concentric Arc Loop:**\n- Radial segments directed toward or away from $O$ produce $\\mathbf{B} = 0$ since $d\\mathbf{l} \\parallel \\mathbf{r}$.\n- Arc of radius $a$ spanning angle $2\\pi - \\varphi$ contributes $B_a = \\frac{\\mu_0 I}{4\\pi a} (2\\pi - \\varphi)$.\n- Arc of radius $b$ carries current in opposite angular direction, contributing $B_b = -\\frac{\\mu_0 I}{4\\pi b} (2\\pi - \\varphi)$.\n$$B = \\frac{\\mu_0 I}{4\\pi} \\left( \\frac{1}{a} - \\frac{1}{b} \\right) (2\\pi - \\varphi)$$\n\n**(b) Arc with Straight Segments:**\nEvaluating the arc and straight chord contributions:\n$$B = \\frac{\\mu_0 I}{4\\pi} \\left( \\frac{3\\pi}{2a} + \\frac{2}{b} \\right)$$",
        "tags": ["planar loop", "concentric arcs", "Biot Savart law", "superposition"]
    },
    {
        "id": "3.224",
        "title": "Magnetic Field Inside Slotted Cylindrical Tube",
        "difficulty": 2,
        "question": "A current $I$ flows along a long thin-walled cylindrical tube of radius $R$ with a narrow longitudinal slit of width $h$ ($h \\ll R$). Find the magnetic induction inside the tube.",
        "hints": [
            "Use superposition: a complete intact tube has zero magnetic field inside ($B = 0$).",
            "The tube with a slit is equivalent to an intact tube carrying current $I$ MINUS a thin strip of width $h$ carrying current $I' = I \\frac{h}{2\\pi R}$.",
            "At distance $r$ from the slit, the missing strip acts as a straight filament carrying current $-I'$."
        ],
        "answer": "$B \\approx \\frac{\\mu_0 I h}{4\\pi^2 R r}$",
        "solution": "**1. Superposition Principle:**\nAn uncut thin-walled cylinder carrying uniformly distributed axial current creates strictly zero magnetic field in its interior:\n$$B_{\\text{uncut}} = 0$$\nThe slotted tube carrying current $I$ is equivalent to an uncut tube carrying current $I_{\\text{total}} \\approx I$ minus a narrow longitudinal strip of width $h$ carrying current:\n$$I' = I \\frac{h}{2\\pi R}$$\n\n**2. Field Inside the Tube:**\n$$\\mathbf{B} = \\mathbf{B}_{\\text{uncut}} - \\mathbf{B}_{\\text{strip}} = -\\mathbf{B}_{\\text{strip}}$$\nAt distance $r$ from the slit ($h \\ll r$):\n$$B = \\frac{\\mu_0 I'}{2\\pi r} = \\frac{\\mu_0 I h}{4\\pi^2 R r}$$",
        "tags": ["superposition", "slotted cylinder", "Ampere law", "thin-walled tube"]
    },
    {
        "id": "3.225",
        "title": "Magnetic Field of Half-Cylindrical Current Sheet",
        "difficulty": 2,
        "question": "A current $I$ flows in a long straight wire whose cross-section is a thin semi-circular shell of radius $R$. Find the magnetic induction at the axis $O$.",
        "hints": [
            "Divide the semi-cylinder into longitudinal filaments of angular width $d\\varphi$ carrying current $dI = I \\frac{d\\varphi}{\\pi}$.",
            "Each filament at distance $R$ creates field $dB = \\frac{\\mu_0 dI}{2\\pi R} = \\frac{\\mu_0 I d\\varphi}{2\\pi^2 R}$.",
            "Integrate the vector components over $\\varphi \\in [-\\pi/2, \\pi/2]$."
        ],
        "answer": "$B = \\frac{\\mu_0 I}{\\pi^2 R}$",
        "solution": "**1. Elementary Current Filament:**\nA strip of angular width $d\\varphi$ carries current:\n$$dI = I \\frac{d\\varphi}{\\pi}$$\nAt the axis $O$, this straight filament creates magnetic field perpendicular to the radius vector:\n$$dB = \\frac{\\mu_0 dI}{2\\pi R} = \\frac{\\mu_0 I}{2\\pi^2 R} d\\varphi$$\n\n**2. Integrating Components:**\nBy symmetry, the components parallel to the symmetry axis of the half-ring cancel, and the transverse components add:\n$$B = \\int_{-\\pi/2}^{\\pi/2} dB \\cos\\varphi = \\frac{\\mu_0 I}{2\\pi^2 R} \\int_{-\\pi/2}^{\\pi/2} \\cos\\varphi \\, d\\varphi = \\frac{\\mu_0 I}{2\\pi^2 R} [\\sin\\varphi]_{-\\pi/2}^{\\pi/2} = \\frac{\\mu_0 I}{\\pi^2 R}$$",
        "tags": ["semicircular shell", "current sheet", "integration", "magnetic induction"]
    },
    {
        "id": "3.226",
        "title": "Magnetic Field at Centre for Bent Wire Geometries",
        "difficulty": 2,
        "question": "Find the magnetic induction at point $O$ if a current-carrying wire of radius $R$ for its curved section has the shapes shown in (a), (b), (c) with very long straight sections.",
        "hints": [
            "Decompose each wire into straight semi-infinite segments and circular arc segments.",
            "Use $B_{\\text{semi}} = \\frac{\\mu_0 I}{4\\pi R}$ for a semi-infinite wire perpendicular to point $O$.",
            "Use $B_{\\text{arc}} = \\frac{\\mu_0 I}{4\\pi R} \\theta$ for circular arcs."
        ],
        "answer": "(a) $B = \\frac{\\mu_0 I}{4\\pi R} \\frac{\\pi}{2}$; (b) $B = \\frac{\\mu_0 I}{4\\pi R} \\left( 1 + \\frac{3\\pi}{2} \\right)$; (c) $B = \\frac{\\mu_0 I}{4\\pi R} (2 + \\pi)$",
        "solution": "**Configuration (a):**\nStraight sections extend along the radial directions to $O$, contributing zero field.\nThe quarter-circle arc of angle $\\pi/2$ contributes:\n$$B = \\frac{\\mu_0 I}{4\\pi R} \\left(\\frac{\\pi}{2}\\right)$$\n\n**Configuration (b):**\nOne semi-infinite straight section and a three-quarter circular arc:\n$$B = \\frac{\\mu_0 I}{4\\pi R} \\left( 1 + \\frac{3\\pi}{2} \\right)$$\n\n**Configuration (c):**\nTwo semi-infinite straight sections plus a semicircle:\n$$B = \\frac{\\mu_0 I}{4\\pi R} (2 + \\pi)$$",
        "tags": ["bent wire", "Biot Savart law", "superposition", "circular arc"]
    },
    {
        "id": "3.227",
        "title": "Magnetic Field of Right-Angled Wire at Perpendicular Point",
        "difficulty": 2,
        "question": "A very long wire carrying current $I = 5.0\\text{ A}$ is bent at right angles. Find the magnetic induction at a point lying on the perpendicular to the wire plane drawn through the bend vertex at distance $l = 35\\text{ cm}$.",
        "hints": [
            "Each semi-infinite leg carries current $I$ starting from the vertex.",
            "For each leg, the distance to the point is $l$, and the perpendicular distance from the point to the leg line is $l$.",
            "The field from each leg has magnitude $B_1 = \\frac{\\mu_0 I}{4\\pi l}$, and their vectors are mutually perpendicular.",
            "$B = \\sqrt{B_1^2 + B_2^2} = \\frac{\\mu_0 I}{4\\pi l} \\sqrt{2}$."
        ],
        "answer": "$B = \\frac{\\mu_0 I}{4\\pi l} \\sqrt{2} = 2.0\\,\\mu\\text{T}$",
        "solution": "**1. Field from Each Semi-Infinite Leg:**\nConsider the point at $(0, 0, l)$ on the $z$-axis perpendicular to the $xy$-plane containing the bend at the origin.\n- Leg 1 along the positive $x$-axis: produces magnetic field along the positive $y$-axis with magnitude:\n  $$B_1 = \\frac{\\mu_0 I}{4\\pi l}$$\n- Leg 2 along the positive $y$-axis: produces magnetic field along the negative $x$-axis with magnitude:\n  $$B_2 = \\frac{\\mu_0 I}{4\\pi l}$$\n\n**2. Vector Resultant:**\nSince $\\mathbf{B}_1 \\perp \\mathbf{B}_2$:\n$$B = \\sqrt{B_1^2 + B_2^2} = \\frac{\\mu_0 I}{4\\pi l} \\sqrt{2}$$\n\n**3. Numerical Evaluation:**\nWith $I = 5.0\\text{ A}$, $l = 0.35\\text{ m}$:\n$$B = \\frac{(4\\pi \\times 10^{-7})(5.0)}{4\\pi (0.35)} \\sqrt{2} = \\frac{5.0 \\times 1.414}{0.35} \\times 10^{-7} \\approx 2.0\\,\\mu\\text{T}$$",
        "tags": ["right-angled wire", "vector superposition", "semi-infinite wire", "Biot Savart law"]
    },
    {
        "id": "3.228",
        "title": "Magnetic Field at Centre for Spatial Current Configurations",
        "difficulty": 2,
        "question": "Find the magnetic induction at point $O$ if wire carrying current $I = 8.0\\text{ A}$ has radius $R = 100\\text{ mm}$ for curved parts in configurations (a), (b), (c) with very long straight sections.",
        "hints": [
            "(a) Semicircle in $xy$-plane and straight wires: $B = \\frac{\\mu_0 I}{4\\pi R} \\sqrt{\\pi^2 + 4} = 0.30\\,\\mu\\text{T}$.",
            "(b) Quarter circles in perpendicular planes: $B = \\frac{\\mu_0 I}{4\\pi R} \\sqrt{2\\pi^2 + 2\\pi + 1} = 0.34\\,\\mu\\text{T}$.",
            "(c) Opposing semi-infinite leads: $B = \\frac{\\mu_0 I}{4\\pi R} \\cdot 2 = 0.11\\,\\mu\\text{T}$."
        ],
        "answer": "(a) $B = 0.30\\,\\mu\\text{T}$; (b) $B = 0.34\\,\\mu\\text{T}$; (c) $B = 0.11\\,\\mu\\text{T}$",
        "solution": "**Vector Superposition in 3D:**\nBy computing the vector sum of $\\mathbf{B}$ components from each linear and circular arc segment for each geometry:\n- (a) $B = \\frac{\\mu_0 I}{4\\pi R} \\sqrt{\\pi^2 + 4} = 0.30\\,\\mu\\text{T}$\n- (b) $B = \\frac{\\mu_0 I}{4\\pi R} \\sqrt{2\\pi^2 + 2\\pi + 1} = 0.34\\,\\mu\\text{T}$\n- (c) $B = \\frac{\\mu_0 I}{4\\pi R} \\cdot 2 = 0.11\\,\\mu\\text{T}$",
        "tags": ["spatial wire geometry", "vector superposition", "numerical evaluation"]
    },
    {
        "id": "3.229",
        "title": "Magnetic Field of Infinite Current Sheets",
        "difficulty": 1,
        "question": "Find the magnitude and direction of the magnetic induction $\\mathbf{B}$:\n(a) of an infinite plane carrying a uniform surface current of linear density $i$;\n(b) of two parallel infinite planes carrying uniform surface currents $i$ and $-i$.",
        "hints": [
            "Use Ampere's circuital law with a rectangular loop spanning both sides of the sheet.",
            "(a) By symmetry, $\\oint \\mathbf{B} \\cdot d\\mathbf{l} = 2 B l = \\mu_0 (i l) \\implies B = \\frac{1}{2} \\mu_0 i$.",
            "(b) Superposition: between planes the fields add ($B = \\mu_0 i$), while outside they cancel ($B = 0$)."
        ],
        "answer": "(a) $B = \\frac{1}{2}\\mu_0 i$; (b) $B = \\mu_0 i$ between the planes, $B = 0$ outside",
        "solution": "**(a) Single Infinite Current Sheet:**\nLet the sheet lie in the $xy$-plane carrying surface current density $\\mathbf{i} = i \\hat{\\mathbf{j}}$.\nBy symmetry, $\\mathbf{B}$ is parallel to the sheet and perpendicular to current flow ($B = B_x \\hat{\\mathbf{i}}$ for $z > 0$, and $-B_x \\hat{\\mathbf{i}}$ for $z < 0$).\nConstruct an Amperian rectangle of length $l$ parallel to $\\hat{\\mathbf{i}}$ extending symmetrically across $z = 0$:\n$$\\oint \\mathbf{B} \\cdot d\\mathbf{l} = 2 B l = \\mu_0 I_{\\text{encl}} = \\mu_0 i l$$\n$$B = \\frac{1}{2} \\mu_0 i$$\n\n**(b) Two Oppositely Directed Current Sheets:**\nApplying superposition of the fields from sheets at $z = 0$ and $z = d$:\n- Between the sheets ($0 < z < d$): fields reinforce:\n  $$B = \\frac{1}{2}\\mu_0 i + \\frac{1}{2}\\mu_0 i = \\mu_0 i$$\n- Outside the sheets ($z < 0$ and $z > d$): fields cancel:\n  $$B = 0$$",
        "tags": ["Ampere law", "current sheet", "superposition", "magnetic induction"]
    },
    {
        "id": "3.230",
        "title": "Magnetic Field Inside and Outside a Current-Carrying Plate",
        "difficulty": 2,
        "question": "A uniform current of volume density $j$ flows inside an infinite slab of thickness $2d$ parallel to its surface. Find the magnetic induction $B$ inside and outside the plate as a function of distance $x$ from the midplane.",
        "hints": [
            "Use an Amperian rectangular loop extending from $-x$ to $+x$.",
            "Inside ($|x| \\le d$): $2 B(x) l = \\mu_0 j (2x l) \\implies B(x) = \\mu_0 j x$.",
            "Outside ($|x| \\ge d$): $2 B(x) l = \\mu_0 j (2d l) \\implies B(x) = \\mu_0 j d$."
        ],
        "answer": "$B(x) = \\begin{cases} \\mu_0 j x & \\text{for } |x| \\le d \\\\ \\mu_0 j d & \\text{for } |x| \\ge d \\end{cases}$",
        "solution": "**1. Symmetry:**\nLet the slab occupy $-d \\le x \\le d$ with current density $\\mathbf{j} = j \\hat{\\mathbf{k}}$.\nBy symmetry, $\\mathbf{B} = B(x) \\hat{\\mathbf{j}}$ with $B(-x) = -B(x)$ and $B(0) = 0$.\n\n**2. Inside the Plate ($|x| \\le d$):**\nConstruct an Amperian loop of length $l$ along $y$ from $-x$ to $+x$:\n$$\\oint \\mathbf{B} \\cdot d\\mathbf{l} = 2 B(x) l = \\mu_0 I_{\\text{encl}} = \\mu_0 j (2x l)$$\n$$B(x) = \\mu_0 j x$$\n\n**3. Outside the Plate ($|x| \\ge d$):**\nThe Amperian loop encloses the entire current of the slab $I_{\\text{encl}} = j (2d l)$:\n$$2 B(x) l = \\mu_0 j (2d l) \\implies B(x) = \\mu_0 j d$$",
        "tags": ["Ampere law", "current-carrying plate", "magnetic field distribution"]
    },
    {
        "id": "3.231",
        "title": "Magnetic Field of Wire Connected to Infinite Conducting Plane",
        "difficulty": 2,
        "question": "A direct current $I$ flows along a long straight wire perpendicular to an infinite conducting plane, spreading radially outward from the contact point $O$. Find the magnetic induction at all points in space.",
        "hints": [
            "Use Ampere's circuital law around circles of radius $r$ coaxial with the wire.",
            "In the half-space containing the wire, the Amperian circle encloses the current $I$ of the wire: $B = \\frac{\\mu_0 I}{2\\pi r}$.",
            "In the other half-space, no current is enclosed by an Amperian circle, so $B = 0$."
        ],
        "answer": "In the half-space with the wire, $B = \\frac{\\mu_0 I}{2\\pi r}$; in the other half-space, $B = 0$",
        "solution": "**1. Symmetry and Amperian Loops:**\nDue to axial symmetry about the wire, magnetic field lines must be concentric circles coaxial with the wire.\nApply Ampere's circuital law $\\oint \\mathbf{B} \\cdot d\\mathbf{l} = 2\\pi r B = \\mu_0 I_{\\text{encl}}$ for a circle of radius $r$ at distance $z$ from the plane.\n\n**2. Half-Space with the Wire ($z > 0$):**\nAny circle coaxial with the wire at $z > 0$ intersects only the incoming wire current $I$:\n$$2\\pi r B = \\mu_0 I \\implies B = \\frac{\\mu_0 I}{2\\pi r}$$\n\n**3. Half-Space on the Other Side ($z < 0$):**\nIn the region $z < 0$, any circle coaxial with the axis encloses zero current, because all currents are confined to $z \\ge 0$ (the wire) and $z = 0$ (the plane):\n$$2\\pi r B = 0 \\implies B = 0$$",
        "tags": ["Ampere law", "radial current plane", "coaxial symmetry", "discontinuous field"]
    },
    {
        "id": "3.232",
        "title": "Line Integral of Magnetic Field Along Loop Axis",
        "difficulty": 1,
        "question": "A current $I$ flows along a round loop. Find the integral $\\int_{-\\infty}^{+\\infty} B_x \\, dx$ along the axis of the loop. Explain the result obtained.",
        "hints": [
            "Use the exact expression $B_x(x) = \\frac{\\mu_0 I R^2}{2(R^2 + x^2)^{3/2}}$.",
            "Evaluate $\\int_{-\\infty}^{+\\infty} \\frac{dx}{(R^2 + x^2)^{3/2}} = \\left[ \\frac{x}{R^2 \\sqrt{R^2 + x^2}} \\right]_{-\\infty}^{+\\infty} = \\frac{2}{R^2}$.",
            "Relate this to Ampere's circuital law by closing the path via a semi-circle at infinity."
        ],
        "answer": "$\\int_{-\\infty}^{+\\infty} B_x \\, dx = \\mu_0 I$",
        "solution": "**1. Direct Integration:**\nThe magnetic field on the axis of a circular loop of radius $R$ carrying current $I$ is:\n$$B_x(x) = \\frac{\\mu_0 I R^2}{2(R^2 + x^2)^{3/2}}$$\nIntegrating along the axis from $-\\infty$ to $+\\infty$:\n$$\\int_{-\\infty}^{+\\infty} B_x \\, dx = \\frac{\\mu_0 I R^2}{2} \\int_{-\\infty}^{+\\infty} \\frac{dx}{(R^2 + x^2)^{3/2}}$$\nUsing the standard antiderivative $\\int \\frac{dx}{(R^2 + x^2)^{3/2}} = \\frac{x}{R^2 \\sqrt{R^2 + x^2}}$:\n$$\\int_{-\\infty}^{+\\infty} B_x \\, dx = \\frac{\\mu_0 I R^2}{2} \\left[ \\frac{x}{R^2 \\sqrt{R^2 + x^2}} \\right]_{-\\infty}^{+\\infty} = \\frac{\\mu_0 I R^2}{2} \\left( \\frac{1}{R^2} - \\left(-\\frac{1}{R^2}\\right) \\right) = \\mu_0 I$$\n\n**2. Physical Explanation:**\nThe path from $-\\infty$ to $+\\infty$ along the axis can be closed by a semi-circle of infinite radius $R_\\infty \\to \\infty$. On this outer arc, $B \\sim 1/R_\\infty^3$, so $\\int_{\\text{arc}} \\mathbf{B} \\cdot d\\mathbf{l} \\to 0$.\nThe closed contour links the circular loop once, so by Ampere's circuital law:\n$$\\oint \\mathbf{B} \\cdot d\\mathbf{l} = \\int_{-\\infty}^{+\\infty} B_x \\, dx + 0 = \\mu_0 I$$",
        "tags": ["axial field integral", "circular loop", "Ampere law", "definite integral"]
    },
    {
        "id": "3.233",
        "title": "Magnetic Induction Vector of Round Wire with Uniform Current",
        "difficulty": 2,
        "question": "A direct current of density $\\mathbf{j}$ flows along a round uniform wire of radius $R$. Find the magnetic induction vector $\\mathbf{B}$ at a point defined by radius vector $\\mathbf{r}$ from the wire axis.",
        "hints": [
            "Use Ampere's circuital law $\\oint \\mathbf{B} \\cdot d\\mathbf{l} = \\mu_0 I_{\\text{encl}}$.",
            "Inside the wire ($r \\le R$): $2\\pi r B = \\mu_0 (j \\pi r^2) \\implies \\mathbf{B} = \\frac{1}{2} \\mu_0 [\\mathbf{j} \\times \\mathbf{r}]$.",
            "Outside the wire ($r \\ge R$): $2\\pi r B = \\mu_0 (j \\pi R^2) \\implies \\mathbf{B} = \\frac{1}{2} \\mu_0 \\frac{R^2}{r^2} [\\mathbf{j} \\times \\mathbf{r}]$."
        ],
        "answer": "$\\mathbf{B} = \\begin{cases} \\frac{1}{2}\\mu_0 [\\mathbf{j} \\times \\mathbf{r}] & \\text{for } r \\le R \\\\ \\frac{1}{2}\\mu_0 \\frac{R^2}{r^2} [\\mathbf{j} \\times \\mathbf{r}] & \\text{for } r \\ge R \\end{cases}$",
        "solution": "**1. Inside the Wire ($r \\le R$):**\nEnclosing current $I_{\\text{encl}} = j \\cdot \\pi r^2$:\n$$2\\pi r B = \\mu_0 j \\pi r^2 \\implies B = \\frac{1}{2} \\mu_0 j r$$\nIn vector form, since $\\mathbf{B} \\perp \\mathbf{j}$ and $\\mathbf{B} \\perp \\mathbf{r}$ following the right-hand screw rule:\n$$\\mathbf{B} = \\frac{1}{2} \\mu_0 [\\mathbf{j} \\times \\mathbf{r}]$$\n\n**2. Outside the Wire ($r \\ge R$):**\nTotal enclosed current is $I = j \\pi R^2$:\n$$2\\pi r B = \\mu_0 j \\pi R^2 \\implies B = \\frac{\\mu_0 j R^2}{2r}$$\nIn vector form:\n$$\\mathbf{B} = \\frac{1}{2} \\mu_0 \\frac{R^2}{r^2} [\\mathbf{j} \\times \\mathbf{r}]$$",
        "tags": ["Ampere law", "vector form", "cylindrical wire", "magnetic induction"]
    },
    {
        "id": "3.234",
        "title": "Uniform Magnetic Field Inside Off-Axis Cylindrical Cavity",
        "difficulty": 2,
        "question": "Inside a long straight uniform wire of round cross-section carrying direct current of density $\\mathbf{j}$, there is a cylindrical cavity whose axis is parallel to the wire axis and displaced by vector $\\mathbf{l}$. Find the magnetic induction $\\mathbf{B}$ inside the cavity.",
        "hints": [
            "Use the superposition principle: a wire with a cavity is equivalent to a solid wire of current density $+\\mathbf{j}$ plus a smaller cylinder carrying current density $-\\mathbf{j}$ occupying the cavity.",
            "From Problem 3.233, inside a solid wire: $\\mathbf{B}(\\mathbf{r}) = \\frac{1}{2}\\mu_0 [\\mathbf{j} \\times \\mathbf{r}]$.",
            "Superpose: $\\mathbf{B} = \\frac{1}{2}\\mu_0 [\\mathbf{j} \\times \\mathbf{r}] - \\frac{1}{2}\\mu_0 [\\mathbf{j} \\times (\\mathbf{r} - \\mathbf{l})] = \\frac{1}{2}\\mu_0 [\\mathbf{j} \\times \\mathbf{l}]$."
        ],
        "answer": "$\\mathbf{B} = \\frac{1}{2} \\mu_0 [\\mathbf{j} \\times \\mathbf{l}]$ (completely uniform inside the cavity)",
        "solution": "**1. Superposition Model:**\nThe wire with a cavity can be represented as the superposition of:\n- A complete solid circular cylinder carrying current density $+\\mathbf{j}$;\n- A circular cylinder of current density $-\\mathbf{j}$ filling the cavity.\n\n**2. Field Inside the Cavity:**\nLet $\\mathbf{r}$ be the position vector from the wire axis, and $\\mathbf{r}' = \\mathbf{r} - \\mathbf{l}$ the position vector from the cavity axis.\nUsing the result from Problem 3.233:\n$$\\mathbf{B}_1 = \\frac{1}{2} \\mu_0 [\\mathbf{j} \\times \\mathbf{r}]$$\n$$\\mathbf{B}_2 = -\\frac{1}{2} \\mu_0 [\\mathbf{j} \\times \\mathbf{r}'] = -\\frac{1}{2} \\mu_0 [\\mathbf{j} \\times (\\mathbf{r} - \\mathbf{l})]$$\nSumming the two fields:\n$$\\mathbf{B} = \\mathbf{B}_1 + \\mathbf{B}_2 = \\frac{1}{2} \\mu_0 [\\mathbf{j} \\times \\mathbf{r}] - \\frac{1}{2} \\mu_0 [\\mathbf{j} \\times \\mathbf{r}] + \\frac{1}{2} \\mu_0 [\\mathbf{j} \\times \\mathbf{l}]$$\n$$\\mathbf{B} = \\frac{1}{2} \\mu_0 [\\mathbf{j} \\times \\mathbf{l}]$$\nNotice that $\\mathbf{r}$ cancels completely: the magnetic field inside the cavity is perfectly uniform.",
        "tags": ["off-axis cavity", "superposition", "uniform magnetic field", "cross product"]
    },
    {
        "id": "3.235",
        "title": "Current Density from Power-Law Magnetic Field Profile",
        "difficulty": 2,
        "question": "Find the current density $j(r)$ as a function of distance $r$ from the axis of a radially symmetric electron beam if the magnetic induction inside the stream varies as $B(r) = b r^\\alpha$, where $b$ and $\\alpha$ are positive constants.",
        "hints": [
            "Use Ampere's law in differential form in cylindrical coordinates: $(\\nabla \\times \\mathbf{B})_z = \\frac{1}{r} \\frac{d}{dr}(r B_\\theta) = \\mu_0 j(r)$.",
            "Substitute $B_\\theta(r) = b r^\\alpha$ into the derivative.",
            "Evaluate $\\frac{d}{dr}(b r^{\\alpha + 1}) = b(\\alpha + 1) r^\\alpha$."
        ],
        "answer": "$j(r) = \\frac{b(\\alpha + 1)}{\\mu_0} r^{\\alpha - 1}$",
        "solution": "**1. Differential Form of Ampere's Law:**\nIn cylindrical coordinates with azimuthal magnetic field $B_\\theta(r)$ and axial current density $j_z(r)$:\n$$(\\nabla \\times \\mathbf{B})_z = \\frac{1}{r} \\frac{d}{dr}\\left( r B_\\theta \\right) = \\mu_0 j(r)$$\n\n**2. Differentiating the Given Field:**\nGiven $B(r) = b r^\\alpha$:\n$$r B(r) = b r^{\\alpha + 1}$$\n$$\\frac{d}{dr}\\left( r B \\right) = b (\\alpha + 1) r^\\alpha$$\n\n**3. Current Density:**\n$$j(r) = \\frac{1}{\\mu_0 r} \\cdot b (\\alpha + 1) r^\\alpha = \\frac{b (\\alpha + 1)}{\\mu_0} r^{\\alpha - 1}$$",
        "tags": ["Ampere differential law", "curl in cylindrical coordinates", "electron beam", "power law"]
    },
    {
        "id": "3.236",
        "title": "Magnetic Induction at Centre of Finite Solenoid",
        "difficulty": 2,
        "question": "A single-layer solenoid has length $l$ and radius $R$, with $n$ turns per unit length. Find the magnetic induction at the centre of the coil when current $I$ flows through it.",
        "hints": [
            "Integrate the field of elementary circular loops of width $dx$: $dB = \\frac{\\mu_0 (n I dx) R^2}{2(R^2 + x^2)^{3/2}}$.",
            "At the centre, limits run from $x = -l/2$ to $+l/2$.",
            "$B = \\mu_0 n I \\frac{l}{\\sqrt{l^2 + 4R^2}} = \\frac{\\mu_0 n I}{\\sqrt{1 + 4R^2 / l^2}}$."
        ],
        "answer": "$B = \\frac{\\mu_0 n I}{\\sqrt{1 + (2R / l)^2}}$",
        "solution": "**1. Integral Formulation:**\nThe field contributed by a ring of width $dx$ at distance $x$ from the centre is:\n$$dB = \\frac{\\mu_0 (n I \\, dx) R^2}{2(R^2 + x^2)^{3/2}}$$\nIntegrating over the length of the solenoid from $x = -l/2$ to $x = +l/2$:\n$$B = \\frac{\\mu_0 n I R^2}{2} \\int_{-l/2}^{l/2} \\frac{dx}{(R^2 + x^2)^{3/2}} = \\frac{\\mu_0 n I R^2}{2} \\left[ \\frac{x}{R^2 \\sqrt{R^2 + x^2}} \\right]_{-l/2}^{l/2}$$\n\n**2. Evaluating the Limits:**\n$$B = \\frac{\\mu_0 n I}{2} \\cdot \\frac{2 (l/2)}{\\sqrt{R^2 + (l/2)^2}} = \\frac{\\mu_0 n I l}{\\sqrt{4R^2 + l^2}} = \\frac{\\mu_0 n I}{\\sqrt{1 + 4R^2 / l^2}} = \\frac{\\mu_0 n I}{\\sqrt{1 + (2R/l)^2}}$$",
        "tags": ["finite solenoid", "axial field", "Biot Savart integration", "centre field"]
    },
    {
        "id": "3.237",
        "title": "Axial Field Distribution Near End of Semi-Infinite Solenoid",
        "difficulty": 2,
        "question": "A very long straight solenoid has radius $R$ and $n$ turns per unit length carrying current $I$. Distance $x$ is measured from the end along the axis ($x > 0$ outside, $x < 0$ inside). Find:\n(a) the magnetic induction $B(x)$ on the axis;\n(b) the distance $x_0$ inside where $B$ differs by $\\eta = 1\\%$ from the central value $B_0 = \\mu_0 n I$.",
        "hints": [
            "(a) For a semi-infinite solenoid extending from $x = 0$ to $-\\infty$: $B(x) = \\frac{1}{2}\\mu_0 n I \\left( 1 - \\frac{x}{\\sqrt{x^2 + R^2}} \\right)$.",
            "(b) For $x < 0$ inside, $B = B_0 (1 - \\eta) \\implies \\frac{1}{2} \\left( 1 + \\frac{|x|}{\\sqrt{x^2 + R^2}} \\right) = 1 - \\eta$.",
            "Solve for $x_0 \\approx \\frac{R}{2\\sqrt{\\eta}} \\approx 5R$."
        ],
        "answer": "(a) $B(x) = \\frac{1}{2}\\mu_0 n I \\left( 1 - \\frac{x}{\\sqrt{x^2 + R^2}} \\right)$; (b) $x_0 \\approx \\frac{R}{2\\sqrt{\\eta}} = 5R$",
        "solution": "**(a) Axial Field Formula:**\nIntegrating rings of current from $x' = x$ to $\\infty$:\n$$B(x) = \\frac{1}{2}\\mu_0 n I \\int_x^\\infty \\frac{R^2 \\, dx'}{(R^2 + x'^2)^{3/2}} = \\frac{1}{2}\\mu_0 n I \\left( 1 - \\frac{x}{\\sqrt{x^2 + R^2}} \\right)$$\n- At the end ($x = 0$): $B(0) = \\frac{1}{2}\\mu_0 n I = \\frac{1}{2} B_0$.\n- Far inside ($x = -|x|$ with $|x| \\gg R$): $B \\to \\mu_0 n I = B_0$.\n\n**(b) Distance for 1% Deviation:**\nInside the solenoid ($x < 0$, let $x = -x_0$ with $x_0 > 0$):\n$$B = \\frac{1}{2} B_0 \\left( 1 + \\frac{x_0}{\\sqrt{x_0^2 + R^2}} \\right) = B_0 (1 - \\eta)$$\n$$1 + \\frac{x_0}{\\sqrt{x_0^2 + R^2}} = 2 - 2\\eta \\implies \\frac{x_0}{\\sqrt{x_0^2 + R^2}} = 1 - 2\\eta$$\nSquaring both sides:\n$$\\frac{x_0^2}{x_0^2 + R^2} \\approx 1 - 4\\eta \\implies 1 - \\frac{R^2}{x_0^2} \\approx 1 - 4\\eta \\implies \\frac{R^2}{x_0^2} \\approx 4\\eta$$\n$$x_0 \\approx \\frac{R}{2\\sqrt{\\eta}}$$\nWith $\\eta = 0.01$:\n$$x_0 = \\frac{R}{2\\sqrt{0.01}} = \\frac{R}{2(0.1)} = 5R$$",
        "tags": ["semi-infinite solenoid", "edge effects", "axial magnetic field", "approximation"]
    },
    {
        "id": "3.238",
        "title": "Magnetic Field of Solenoid Wound from Conducting Strip",
        "difficulty": 2,
        "question": "A thin conducting strip of width $h = 2.0\\text{ cm}$ is tightly wound into a long single-layer solenoid of radius $R = 2.5\\text{ cm}$ carrying current $I = 5.0\\text{ A}$. Find the magnetic induction inside and outside as a function of distance $r$ from the axis.",
        "hints": [
            "Current $I$ along the strip has an azimuthal component (forming a solenoid of linear density $n I = I/h$) and an axial component (forming a straight wire carrying current $I$).",
            "Inside the solenoid ($r < R$): only the azimuthal component creates field: $B = B_z = \\frac{\\mu_0 I}{h}$.",
            "Outside the solenoid ($r > R$): the axial current creates an azimuthal field: $B = B_\\varphi = \\frac{\\mu_0 I}{2\\pi r}$."
        ],
        "answer": "$B = \\begin{cases} \\frac{\\mu_0 I}{h} = 0.3\\text{ mT} & \\text{for } r < R \\\\ \\frac{\\mu_0 I}{2\\pi r} & \\text{for } r > R \\end{cases}$",
        "solution": "**1. Resolution of Strip Current:**\nA strip of width $h$ wound tightly into a single-layer helix advances pitch $h$ per turn.\nThe total current $I$ along the strip decomposes into:\n- An azimuthal current component with linear density $j_\\theta = I / h$;\n- An axial current component of total current $I_z = I$ flowing along the length of the cylinder.\n\n**2. Inside the Solenoid ($r < R$):**\n- The axial current along the cylinder creates zero field inside ($B_\\varphi = 0$).\n- The azimuthal current creates an axial field:\n  $$B_z = \\mu_0 j_\\theta = \\frac{\\mu_0 I}{h}$$\nNumerically:\n$$B_z = \\frac{(4\\pi \\times 10^{-7})(5.0)}{0.020} = 1.0\\pi \\times 10^{-4}\\text{ T} \\approx 0.31\\text{ mT} \\approx 0.3\\text{ mT}$$\n\n**3. Outside the Solenoid ($r > R$):**\n- The azimuthal current creates zero external field ($B_z = 0$).\n- The axial current creates an azimuthal field:\n  $$B_\\varphi(r) = \\frac{\\mu_0 I}{2\\pi r}$$",
        "tags": ["helical strip", "solenoid", "axial and azimuthal fields", "Ampere law"]
    },
    {
        "id": "3.239",
        "title": "Ratio of Core Field to Centre Field in Toroid",
        "difficulty": 1,
        "question": "$N = 2.5 \\times 10^3$ wire turns are uniformly wound on a wooden toroidal core of very small cross-section carrying current $I$. Find the ratio $\\eta$ of the magnetic induction inside the core to that at the centre of the toroid.",
        "hints": [
            "Inside the toroidal core of radius $R$: $B_{\\text{core}} = \\frac{\\mu_0 N I}{2\\pi R}$.",
            "At the centre of the toroid, the net current of all turns forms a circular loop of radius $R$ carrying current $I$: $B_{\\text{centre}} = \\frac{\\mu_0 I}{2R}$.",
            "Ratio is $\\eta = \\frac{B_{\\text{core}}}{B_{\\text{centre}}} = \\frac{N}{\\pi}$."
        ],
        "answer": "$\\eta = \\frac{N}{\\pi} \\approx 8 \\times 10^2$",
        "solution": "**1. Field Inside the Core:**\nBy Ampere's circuital law along the circular core of radius $R$:\n$$2\\pi R B_{\\text{core}} = \\mu_0 N I \\implies B_{\\text{core}} = \\frac{\\mu_0 N I}{2\\pi R}$$\n\n**2. Field at the Centre of the Toroid:**\nEach turn advances around the toroid, so the winding as a whole carries one net circular current $I$ around the perimeter of radius $R$.\nAt the centre of this effective single circular loop of radius $R$:\n$$B_{\\text{centre}} = \\frac{\\mu_0 I}{2R}$$\n\n**3. Ratio:**\n$$\\eta = \\frac{B_{\\text{core}}}{B_{\\text{centre}}} = \\frac{\\frac{\\mu_0 N I}{2\\pi R}}{\\frac{\\mu_0 I}{2R}} = \\frac{N}{\\pi}$$\nWith $N = 2500$:\n$$\\eta = \\frac{2500}{\\pi} \\approx 796 \\approx 8 \\times 10^2$$",
        "tags": ["toroid", "core field", "centre field", "ratio"]
    },
    {
        "id": "3.240",
        "title": "Internal Magnetic Flux Through Wire Half-Section",
        "difficulty": 1,
        "question": "A direct current $I = 10\\text{ A}$ flows in a long straight round conductor. Find the magnetic flux through a half of the wire's cross-section per one metre of its length.",
        "hints": [
            "Inside a wire of radius $R$, the magnetic field is $B(r) = \\frac{\\mu_0 I r}{2\\pi R^2}$.",
            "The flux through a longitudinal strip of width $dr$ and length $l = 1\\text{ m}$ from $r = 0$ to $R$ is $d\\Phi = B(r) l \\, dr$.",
            "Integrate $\\Phi_1 = \\int_0^R \\frac{\\mu_0 I r}{2\\pi R^2} \\, dr = \\frac{\\mu_0 I}{4\\pi}$."
        ],
        "answer": "$\\Phi = \\frac{\\mu_0 I}{4\\pi} = 1.0\\,\\mu\\text{Wb/m}$",
        "solution": "**1. Magnetic Field Inside the Conductor:**\nBy Ampere's law, inside a cylindrical conductor of radius $R$:\n$$B(r) = \\frac{\\mu_0 I r}{2\\pi R^2}$$\n\n**2. Flux Through Half-Cross-Section Per Unit Length:**\nConsider the rectangular strip of length $l = 1\\text{ m}$ extending from the wire axis ($r = 0$) to its surface ($r = R$):\n$$\\Phi = \\int_0^R B(r) \\cdot (l \\, dr) = \\frac{\\mu_0 I l}{2\\pi R^2} \\int_0^R r \\, dr = \\frac{\\mu_0 I l}{2\\pi R^2} \\frac{R^2}{2} = \\frac{\\mu_0 I l}{4\\pi}$$\n\n**3. Numerical Evaluation:**\nFor $l = 1.0\\text{ m}$ and $I = 10\\text{ A}$:\n$$\\Phi = \\frac{(4\\pi \\times 10^{-7})(10)}{4\\pi} = 1.0 \\times 10^{-6}\\text{ Wb/m} = 1.0\\,\\mu\\text{Wb/m}$$",
        "tags": ["internal magnetic flux", "Ampere law", "integration", "numerical value"]
    },
    {
        "id": "3.241",
        "title": "Magnetic Flux Through End Plane of Solenoid",
        "difficulty": 1,
        "question": "A very long straight solenoid of cross-sectional area $S$ and $n$ turns per unit length carries current $I$. Find the magnetic flux through the end plane of the solenoid.",
        "hints": [
            "Far inside the solenoid, the field is uniform: $B_0 = \\mu_0 n I$, and the total flux is $\\Phi_0 = B_0 S = \\mu_0 n I S$.",
            "At the open end, exactly half the magnetic flux lines diverge out into the sides: $\\Phi = \\frac{1}{2} \\Phi_0$."
        ],
        "answer": "$\\Phi = \\frac{1}{2} \\mu_0 n I S = \\frac{1}{2} \\Phi_0$",
        "solution": "**1. Solenoid Flux and Divergence:**\nFar inside the long solenoid, the magnetic field is uniform and parallel to the axis:\n$$B_0 = \\mu_0 n I$$\nThe total flux through a central cross-section is:\n$$\\Phi_0 = B_0 S = \\mu_0 n I S$$\n\n**2. Flux at the End Plane:**\nBy Gauss's theorem for the magnetic field ($\\nabla \\cdot \\mathbf{B} = 0$), magnetic flux lines are continuous.\nAt the end of a semi-infinite solenoid, the axial field on the end cross-section averages to half the interior value ($B_{\\text{end}} = \\frac{1}{2} B_0$), with the other half of the flux diverging laterally through the windings near the end.\nTherefore:\n$$\\Phi = \\frac{1}{2} \\Phi_0 = \\frac{1}{2} \\mu_0 n I S$$",
        "tags": ["solenoid end flux", "flux divergence", "Gauss law for B", "semi-infinite solenoid"]
    },
    {
        "id": "3.242",
        "title": "Magnetic Flux Through Rectangular Toroid",
        "difficulty": 2,
        "question": "A toroidal solenoid has a rectangular cross-section of height $h = 5.0\\text{ cm}$. The total number of turns is $N = 1000$, current is $I = 1.7\\text{ A}$, and the ratio of outer to inner diameter is $\\eta = 1.6$. Find the magnetic flux through this cross-section.",
        "hints": [
            "The field inside the toroid at radius $r$ is $B(r) = \\frac{\\mu_0 N I}{2\\pi r}$.",
            "The area element of the rectangular cross-section is $dA = h \\, dr$.",
            "Integrate $\\Phi = \\int_{r_1}^{r_2} B(r) h \\, dr = \\frac{\\mu_0 N I h}{2\\pi} \\ln\\left(\\frac{r_2}{r_1}\\right) = \\frac{\\mu_0 N I h}{2\\pi} \\ln\\eta$."
        ],
        "answer": "$\\Phi = \\frac{\\mu_0 N I h}{2\\pi} \\ln\\eta = 8.0\\,\\mu\\text{Wb}$",
        "solution": "**1. Field in the Toroidal Solenoid:**\nBy Ampere's circuital law, inside the toroid at distance $r$ from the axis of revolution:\n$$B(r) = \\frac{\\mu_0 N I}{2\\pi r}$$\n\n**2. Magnetic Flux Through Rectangular Section:**\nThe rectangular cross-section extends radially from inner radius $r_1$ to outer radius $r_2 = \\eta r_1$, with vertical height $h$.\nThe magnetic flux through one turn's cross-section is:\n$$\\Phi = \\int_{r_1}^{r_2} B(r) (h \\, dr) = \\frac{\\mu_0 N I h}{2\\pi} \\int_{r_1}^{r_2} \\frac{dr}{r} = \\frac{\\mu_0 N I h}{2\\pi} \\ln\\left( \\frac{r_2}{r_1} \\right) = \\frac{\\mu_0 N I h}{2\\pi} \\ln\\eta$$\n\n**3. Numerical Evaluation:**\nGiven $N = 1000$, $I = 1.7\\text{ A}$, $h = 0.050\\text{ m}$, $\\eta = 1.6$, and $\\ln 1.6 \\approx 0.470$:\n$$\\Phi = \\frac{(4\\pi \\times 10^{-7}) \\times 1000 \\times 1.7 \\times 0.050}{2\\pi} \\times 0.470 = 2 \\times 10^{-4} \\times 0.085 \\times 0.470 \\approx 8.0\\,\\mu\\text{Wb}$$",
        "tags": ["toroidal solenoid", "magnetic flux", "rectangular cross-section", "integration"]
    }
]
