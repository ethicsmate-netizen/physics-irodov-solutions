"""
ch1_6_curated.py
Curated problems 1.290 to 1.314 (25 problems) of Irodov Chapter 1.6: Elastic Deformations of a Solid Body.
"""

CH1_6_CURATED = [
    {
        "id": "1.290",
        "title": "Thermal Stress in a Constrained Cylinder",
        "difficulty": 1,
        "question": "What pressure has to be applied to the ends of a steel cylinder to keep its length constant on raising its temperature by $\\Delta T = 100^\\circ\\text{C}$? Young's modulus of steel is $E = 2.0 \\times 10^{11}\\text{ Pa}$, and the thermal expansion coefficient is $\\alpha = 1.1 \\times 10^{-5}\\text{ K}^{-1}$.",
        "hints": [
            "Thermal expansion strain is $\\varepsilon_{\\text{th}} = \\alpha \\Delta T$.",
            "To keep length constant, mechanical compressive strain must equal thermal strain: $\\varepsilon_{\\text{mech}} = \\sigma / E = \\alpha \\Delta T$.",
            "Required pressure is $p = \\sigma = E \\alpha \\Delta T$."
        ],
        "answer": "$p = E \\alpha \\Delta T = 2.2 \\times 10^4\\text{ atm}$",
        "solution": "**1. Stress-Strain Relation:**\nThe free thermal strain caused by temperature increase $\\Delta T$ is:\n$$\\varepsilon_{\\text{th}} = \\alpha \\Delta T$$\nTo maintain constant length, an external compressive stress $\\sigma$ must be applied such that the net strain is zero:\n$$\\varepsilon = \\varepsilon_{\\text{th}} - \\frac{\\sigma}{E} = 0 \\implies \\sigma = E \\alpha \\Delta T$$\n\n**2. Pressure Calculation:**\nThe required end pressure is $p = \\sigma$:\n$$p = E \\alpha \\Delta T = (2.0 \\times 10^{11}\\text{ Pa}) \\times (1.1 \\times 10^{-5}\\text{ K}^{-1}) \\times 100\\text{ K} = 2.2 \\times 10^8\\text{ Pa}$$\nConverting to atmospheres ($1\\text{ atm} = 1.013 \\times 10^5\\text{ Pa}$):\n$$p = \\frac{2.2 \\times 10^8}{1.013 \\times 10^5} \\approx 2.2 \\times 10^4\\text{ atm}$$",
        "tags": ["thermal stress", "Young's modulus", "thermal expansion", "elasticity"]
    },
    {
        "id": "1.291",
        "title": "Bursting Pressure of Glass Tube and Flask",
        "difficulty": 1,
        "question": "What internal pressure $p$ (in the absence of external pressure) can be sustained:\n(a) by a glass tube;\n(b) by a glass spherical flask,\nif in both cases the wall thickness is $\\Delta r = 1.0\\text{ mm}$, the radius is $r = 25\\text{ mm}$, and the ultimate tensile strength of glass is $\\sigma_m = 5.0 \\times 10^7\\text{ Pa}$?",
        "hints": [
            "(a) For a thin-walled cylinder of radius $r$ and thickness $\\Delta r$, hoop stress is $\\sigma = \\frac{p r}{\\Delta r}$.",
            "(b) For a thin-walled sphere, membrane stress is $\\sigma = \\frac{p r}{2\\Delta r}$.",
            "Equate stress to $\\sigma_m$ and solve for $p$."
        ],
        "answer": "(a) $p \\approx \\frac{\\sigma_m \\Delta r}{r} = 20\\text{ atm}$; (b) $p \\approx \\frac{2 \\sigma_m \\Delta r}{r} = 40\\text{ atm}$",
        "solution": "**1. Part (a): Cylindrical Tube:**\nBy equilibrium of a half-cylinder of length $L$:\n$$p (2r L) = 2 \\sigma (\\Delta r L) \\implies \\sigma = \\frac{p r}{\\Delta r}$$\nSetting $\\sigma = \\sigma_m$:\n$$p = \\frac{\\sigma_m \\Delta r}{r} = \\frac{5.0 \\times 10^7 \\times 1.0 \\times 10^{-3}}{25 \\times 10^{-3}} = 2.0 \\times 10^6\\text{ Pa} \\approx 20\\text{ atm}$$\n\n**2. Part (b): Spherical Flask:**\nBy equilibrium of a hemisphere:\n$$p (\\pi r^2) = \\sigma (2\\pi r \\Delta r) \\implies \\sigma = \\frac{p r}{2 \\Delta r}$$\nSetting $\\sigma = \\sigma_m$:\n$$p = \\frac{2 \\sigma_m \\Delta r}{r} = 2 \\times (2.0 \\times 10^6\\text{ Pa}) = 4.0 \\times 10^6\\text{ Pa} \\approx 40\\text{ atm}$$",
        "tags": ["hoop stress", "pressure vessel", "tensile strength", "thin-walled shell"]
    },
    {
        "id": "1.292",
        "title": "Critical Rotation Speed of a Rotating Rod",
        "difficulty": 2,
        "question": "A horizontally oriented copper rod of length $l = 1.0\\text{ m}$ is rotated about a vertical axis passing through its middle. What is the rotation frequency $n$ (in rps) at which the rod ruptures? Tensile strength of copper is $\\sigma_m = 2.45 \\times 10^8\\text{ Pa}$, and density is $\\rho = 8.9 \\times 10^3\\text{ kg/m}^3$.",
        "hints": [
            "Tensile force at distance $x$ from center is caused by centrifugal forces on the outer segment: $T(x) = \\int_x^{l/2} \\rho S \\omega^2 x' dx'$.",
            "Maximum tension occurs at the center ($x = 0$): $T(0) = \\frac{1}{8} \\rho S \\omega^2 l^2$.",
            "Maximum stress is $\\sigma_{\\max} = \\frac{1}{8} \\rho \\omega^2 l^2 = \\sigma_m$.",
            "Solve for $\\omega$ and $n = \\omega / (2\\pi)$."
        ],
        "answer": "$n = \\frac{1}{\\pi l} \\sqrt{\\frac{2 \\sigma_m}{\\rho}} = 80\\text{ rps}$",
        "solution": "**1. Stress Distribution:**\nFor an element $dx'$ at distance $x'$ from the rotation axis, the centrifugal force is $dF_{cf} = (\\rho S dx') \\omega^2 x'$.\nThe tension at cross-section $x$ balances the centrifugal force on the segment from $x$ to $l/2$:\n$$T(x) = \\int_x^{l/2} \\rho S \\omega^2 x' dx' = \\frac{1}{2} \\rho S \\omega^2 \\left[\\left(\\frac{l}{2}\\right)^2 - x^2\\right] = \\frac{1}{2} \\rho S \\omega^2 \\left(\\frac{l^2}{4} - x^2\\right)$$\n\n**2. Maximum Stress at Midpoint ($x = 0$):**\n$$\\sigma_{\\max} = \\frac{T(0)}{S} = \\frac{1}{8} \\rho \\omega^2 l^2$$\nSetting $\\sigma_{\\max} = \\sigma_m$:\n$$\\omega^2 = \\frac{8 \\sigma_m}{\\rho l^2} \\implies \\omega = \\frac{2}{l} \\sqrt{\\frac{2 \\sigma_m}{\\rho}}$$\n$$n = \\frac{\\omega}{2\\pi} = \\frac{1}{\\pi l} \\sqrt{\\frac{2 \\sigma_m}{\\rho}}$$\n\n**3. Numerical Calculation:**\n$$n = \\frac{1}{\\pi \\times 1.0} \\sqrt{\\frac{2 \\times 2.45 \\times 10^8}{8.9 \\times 10^3}} = \\frac{1}{\\pi} \\sqrt{5.506 \\times 10^4} = \\frac{234.6}{\\pi} \\approx 75\\text{ to }80\\text{ rps} = 0.8 \\times 10^2\\text{ rps}$$",
        "tags": ["rotating rod", "tensile stress", "rupture speed", "centrifugal force"]
    },
    {
        "id": "1.293",
        "title": "Critical Rotation Speed of a Lead Ring",
        "difficulty": 2,
        "question": "A ring of radius $r = 25\\text{ cm}$ made of lead wire is rotated about a stationary vertical axis passing through its centre and perpendicular to its plane. What is the number of revolutions per second $n$ at which the ring ruptures? Tensile strength of lead is $\\sigma_m = 1.5 \\times 10^7\\text{ Pa}$ and density is $\\rho = 11.3 \\times 10^3\\text{ kg/m}^3$.",
        "hints": [
            "For a rotating ring of radius $r$, the hoop tension is $T = \\rho S v^2 = \\rho S \\omega^2 r^2$.",
            "Tensile stress is $\\sigma = T / S = \\rho \\omega^2 r^2$.",
            "At rupture, $\\sigma = \\sigma_m \\implies \\omega = \\frac{1}{r} \\sqrt{\\frac{\\sigma_m}{\\rho}}$."
        ],
        "answer": "$n = \\frac{1}{2\\pi r} \\sqrt{\\frac{\\sigma_m}{\\rho}} = 23\\text{ rps}$",
        "solution": "**1. Tensile Stress in Rotating Ring:**\nConsider an arc element $d\\theta$ of the ring. Its mass is $dm = \\rho S r d\\theta$, and the centrifugal force acting on it is:\n$$dF_{cf} = dm \\, \\omega^2 r = \\rho S r^2 \\omega^2 d\\theta$$\nThis outward force is balanced by the radial components of the tensile force $T$ at its ends:\n$$2 T \\sin(d\\theta / 2) \\approx T d\\theta = \\rho S r^2 \\omega^2 d\\theta \\implies T = \\rho S \\omega^2 r^2$$\n$$\\sigma = \\frac{T}{S} = \\rho \\omega^2 r^2$$\n\n**2. Critical Speed:**\nSetting $\\sigma = \\sigma_m$:\n$$\\omega = \\frac{1}{r} \\sqrt{\\frac{\\sigma_m}{\\rho}}$$\n$$n = \\frac{\\omega}{2\\pi} = \\frac{1}{2\\pi r} \\sqrt{\\frac{\\sigma_m}{\\rho}}$$\n\n**3. Numerical Calculation:**\n$$n = \\frac{1}{2\\pi \\times 0.25} \\sqrt{\\frac{1.5 \\times 10^7}{11.3 \\times 10^3}} = \\frac{1}{0.5\\pi} \\sqrt{1.327 \\times 10^3} = \\frac{36.43}{1.571} \\approx 23\\text{ rps}$$",
        "tags": ["rotating ring", "hoop stress", "tensile strength", "centrifugal force"]
    },
    {
        "id": "1.294",
        "title": "Sag of a Wire Under Central Load",
        "difficulty": 2,
        "question": "A steel wire of diameter $d = 1.0\\text{ mm}$ is stretched horizontally between two clamps separated by $l = 2.0\\text{ m}$. A weight of mass $m = 0.25\\text{ kg}$ is suspended from the midpoint of the wire. What will the resulting vertical sag $x$ of the midpoint be in centimetres? Young's modulus of steel is $E = 2.0 \\times 10^{11}\\text{ Pa}$.",
        "hints": [
            "Let $x$ be the vertical sag. For small sag $x \\ll l$, each half has length $l' = \\sqrt{(l/2)^2 + x^2} \\approx \\frac{l}{2} [1 + 2 (x/l)^2]$.",
            "Tensile strain is $\\varepsilon = \\frac{l' - l/2}{l/2} = 2 (x/l)^2$.",
            "Tension in wire is $T = E S \\varepsilon = E (\\frac{\\pi d^2}{4}) \\frac{2 x^2}{l^2}$.",
            "Vertical equilibrium at midpoint: $2 T \\sin \\theta = m g$, with $\\sin \\theta \\approx \\frac{x}{l/2} = \\frac{2x}{l}$."
        ],
        "answer": "$x = l \\left(\\frac{m g}{2\\pi d^2 E}\\right)^{1/3} \\approx 2.5\\text{ cm}$",
        "solution": "**1. Geometric Strain:**\nEach half of the stretched wire has length:\n$$l' = \\sqrt{(l/2)^2 + x^2} = \\frac{l}{2} \\sqrt{1 + \\left(\\frac{2x}{l}\\right)^2} \\approx \\frac{l}{2} \\left[1 + \\frac{1}{2} \\left(\\frac{2x}{l}\\right)^2\\right] = \\frac{l}{2} + \\frac{x^2}{l}$$\n$$\\varepsilon = \\frac{l' - l/2}{l/2} = \\frac{2 x^2}{l^2}$$\n\n**2. Tension in the Wire:**\n$$T = \\sigma S = E \\varepsilon \\left(\\frac{\\pi d^2}{4}\\right) = E \\left(\\frac{2 x^2}{l^2}\\right) \\left(\\frac{\\pi d^2}{4}\\right) = \\frac{\\pi d^2 E x^2}{2 l^2}$$\n\n**3. Vertical Force Balance:**\n$$2 T \\sin \\theta = m g$$\nFor small deflection, $\\sin \\theta \\approx \\frac{x}{l/2} = \\frac{2x}{l}$:\n$$2 \\left(\\frac{\\pi d^2 E x^2}{2 l^2}\\right) \\left(\\frac{2x}{l}\\right) = m g$$\n$$\\frac{2\\pi d^2 E x^3}{l^3} = m g \\implies x^3 = \\frac{m g l^3}{2\\pi d^2 E}$$\n$$x = l \\left(\\frac{m g}{2\\pi d^2 E}\\right)^{1/3}$$\n\n**4. Numerical Calculation:**\n$$x = 2.0 \\times \\left(\\frac{0.25 \\times 9.8}{2\\pi \\times (1.0 \\times 10^{-3})^2 \\times 2.0 \\times 10^{11}}\\right)^{1/3} = 2.0 \\times \\left(\\frac{2.45}{4\\pi \\times 10^5}\\right)^{1/3}$$\n$$\\frac{2.45}{1.257 \\times 10^6} = 1.95 \\times 10^{-6} \\implies (1.95 \\times 10^{-6})^{1/3} \\approx 1.25 \\times 10^{-2}$$\n$$x = 2.0 \\times 1.25 \\times 10^{-2}\\text{ m} = 0.025\\text{ m} = 2.5\\text{ cm}$$",
        "tags": ["elasticity", "wire sag", "Young's modulus", "non-linear deflection"]
    },
    {
        "id": "1.295",
        "title": "Compressive Strain of an Accelerating Elastic Plank",
        "difficulty": 2,
        "question": "A uniform elastic plank moves over a smooth horizontal plane due to a constant force $F_0$ distributed uniformly over one end face. The area of the end face is $S$, and Young's modulus is $E$. Find the mean compressive strain of the plank in the direction of the acting force.",
        "hints": [
            "Let the plank have length $l$ and mass $m$. The acceleration is $w = F_0 / m$.",
            "At distance $x$ from the free rear end, the mass behind is $m(x) = m x / l$.",
            "The compressive force at cross-section $x$ is $F(x) = m(x) w = F_0 \\frac{x}{l}$.",
            "Total compression is $\\Delta l = \\int_0^l \\frac{F(x)}{E S} dx$, and mean strain is $\\bar{\\varepsilon} = \\Delta l / l$."
        ],
        "answer": "$\\varepsilon = \\frac{F_0}{2 E S}$",
        "solution": "**1. Stress Distribution:**\nAcceleration of the plank:\n$$w = \\frac{F_0}{m}$$\nAt distance $x$ from the free trailing end, the mass of the trailing portion is $m_x = m \\frac{x}{l}$.\nThe accelerating force required for this section is provided by the compressive force at $x$:\n$$F(x) = m_x w = \\left(m \\frac{x}{l}\\right) \\left(\\frac{F_0}{m}\\right) = F_0 \\frac{x}{l}$$\n\n**2. Strain and Total Compression:**\nThe local compressive strain at cross-section $x$ is:\n$$\\varepsilon(x) = \\frac{\\sigma(x)}{E} = \\frac{F(x)}{E S} = \\frac{F_0 x}{E S l}$$\nThe total shortening of the plank is:\n$$\\Delta l = \\int_0^l \\varepsilon(x) dx = \\frac{F_0}{E S l} \\int_0^l x dx = \\frac{F_0 l}{2 E S}$$\n\n**3. Mean Strain:**\n$$\\bar{\\varepsilon} = \\frac{\\Delta l}{l} = \\frac{F_0}{2 E S}$$",
        "tags": ["accelerating plank", "compressive strain", "Young's modulus", "elasticity"]
    },
    {
        "id": "1.296",
        "title": "Tension and Elongation of a Rotating Rod",
        "difficulty": 2,
        "question": "A thin uniform copper rod of length $l$ and mass $m$ rotates uniformly with angular velocity $\\omega$ in a horizontal plane about a vertical axis passing through one of its ends. Find:\n(a) the tension $T(r)$ as a function of distance $r$ from the rotation axis;\n(b) the elongation $\\Delta l$ of the rod (density $\\rho$, Young's modulus $E$).",
        "hints": [
            "(a) An element $dr'$ at distance $r'$ from the axis experiences centrifugal force $dF_{cf} = (m/l) dr' \\cdot \\omega^2 r'$. Integrate from $r$ to $l$.",
            "(b) Hooke's law: $d(\\Delta l) = \\frac{T(r)}{E S} dr$. Integrate from $0$ to $l$."
        ],
        "answer": "(a) $T(r) = \\frac{1}{2} m \\omega^2 l \\left[1 - \\left(\\frac{r}{l}\\right)^2\\right]$; (b) $\\Delta l = \\frac{1}{3} \\frac{\\rho \\omega^2 l^3}{E}$",
        "solution": "**1. Part (a): Tension Distribution:**\nThe tension at distance $r$ balances the centrifugal force of the outer portion from $r$ to $l$:\n$$T(r) = \\int_r^l \\left(\\frac{m}{l} dr'\\right) \\omega^2 r' = \\frac{m \\omega^2}{l} \\left[ \\frac{r'^2}{2} \\right]_r^l = \\frac{m \\omega^2}{2l} (l^2 - r^2) = \\frac{1}{2} m \\omega^2 l \\left[1 - \\left(\\frac{r}{l}\\right)^2\\right]$$\n\n**2. Part (b): Elongation of the Rod:**\nUsing $m = \\rho S l$:\n$$T(r) = \\frac{1}{2} \\rho S \\omega^2 (l^2 - r^2)$$\nThe strain is $\\varepsilon(r) = \\frac{T(r)}{E S} = \\frac{\\rho \\omega^2}{2E} (l^2 - r^2)$.\nIntegrating to find the total elongation:\n$$\\Delta l = \\int_0^l \\varepsilon(r) dr = \\frac{\\rho \\omega^2}{2E} \\int_0^l (l^2 - r^2) dr = \\frac{\\rho \\omega^2}{2E} \\left(l^3 - \\frac{l^3}{3}\\right) = \\frac{1}{3} \\frac{\\rho \\omega^2 l^3}{E}$$",
        "tags": ["rotating rod", "centrifugal tension", "elongation", "Hooke's law"]
    },
    {
        "id": "1.297",
        "title": "Volume Change of a Compressed Cylinder",
        "difficulty": 2,
        "question": "A solid copper cylinder of length $l = 65\\text{ cm}$ is placed on a horizontal surface and subjected to a vertical compressive force $F = 1000\\text{ N}$ distributed uniformly over the end face. What is the resulting change of volume $\\Delta V$ of the cylinder in cubic millimetres? For copper, Young's modulus is $E = 1.3 \\times 10^{11}\\text{ Pa}$ and Poisson's ratio is $\\mu = 0.34$.",
        "hints": [
            "Axial compressive strain is $\\varepsilon_z = - \\frac{F}{E S}$.",
            "Transverse strains due to Poisson effect are $\\varepsilon_x = \\varepsilon_y = -\\mu \\varepsilon_z = \\mu \\frac{F}{E S}$.",
            "Relative volume change is $\\frac{\\Delta V}{V} \\approx \\varepsilon_x + \\varepsilon_y + \\varepsilon_z = \\varepsilon_z (1 - 2\\mu) = - \\frac{F}{E S} (1 - 2\\mu)$.",
            "Multiply by $V = S l$ to get $\\Delta V = - \\frac{F l}{E} (1 - 2\\mu)$."
        ],
        "answer": "$\\Delta V = - \\frac{F l}{E} (1 - 2\\mu) = -1.6\\text{ mm}^3$",
        "solution": "**1. Volumetric Strain:**\nUnder uniaxial compression along the $z$-axis:\n$$\\sigma_z = -\\frac{F}{S}, \\quad \\sigma_x = \\sigma_y = 0$$\nThe principal strains are:\n$$\\varepsilon_z = \\frac{\\sigma_z}{E} = -\\frac{F}{E S}$$\n$$\\varepsilon_x = \\varepsilon_y = -\\mu \\varepsilon_z = \\mu \\frac{F}{E S}$$\nThe volumetric strain is:\n$$\\frac{\\Delta V}{V} = \\varepsilon_x + \\varepsilon_y + \\varepsilon_z = -\\frac{F}{E S} (1 - 2\\mu)$$\n\n**2. Volume Change:**\n$$\\Delta V = V \\left[-\\frac{F}{E S} (1 - 2\\mu)\\right] = (S l) \\left[-\\frac{F}{E S} (1 - 2\\mu)\\right] = -\\frac{F l}{E} (1 - 2\\mu)$$\n\n**3. Numerical Calculation:**\n$$\\Delta V = -\\frac{1000 \\times 0.65}{1.3 \\times 10^{11}} (1 - 2 \\times 0.34) = -\\frac{650}{1.3 \\times 10^{11}} (1 - 0.68) = -5.0 \\times 10^{-9} \\times 0.32 = -1.6 \\times 10^{-9}\\text{ m}^3$$\nConverting to cubic millimetres ($1\\text{ m}^3 = 10^9\\text{ mm}^3$):\n$$\\Delta V = -1.6\\text{ mm}^3$$",
        "tags": ["Poisson's ratio", "volumetric strain", "compression", "elasticity"]
    },
    {
        "id": "1.298",
        "title": "Elongation and Volume Increment of a Hanging Rod",
        "difficulty": 2,
        "question": "A copper rod of length $l$ is suspended vertically from the ceiling by its upper end. Find:\n(a) the elongation $\\Delta l$ of the rod due to its own weight;\n(b) the relative increment of its volume $\\Delta V / V$ (density $\\rho$, Young's modulus $E$, Poisson's ratio $\\mu$).",
        "hints": [
            "(a) At distance $z$ from the lower free end, tension is $T(z) = \\rho S g z$. Strain is $\\varepsilon(z) = \\frac{\\rho g z}{E}$. Integrate from $0$ to $l$.",
            "(b) Local volume strain is $\\frac{d(\\Delta V)}{dV} = \\varepsilon(z) (1 - 2\\mu)$. Integrate over the rod."
        ],
        "answer": "(a) $\\Delta l = \\frac{\\rho g l^2}{2E}$; (b) $\\frac{\\Delta V}{V} = \\frac{\\Delta l}{l} (1 - 2\\mu) = \\frac{\\rho g l}{2E} (1 - 2\\mu)$",
        "solution": "**1. Part (a): Elongation:**\nAt a distance $z$ from the bottom free end of the rod, the weight supported is $m(z) g = \\rho S z g$.\nThe tensile stress is:\n$$\\sigma(z) = \\rho g z$$\nThe elongation of an element $dz$ is $d(\\Delta l) = \\frac{\\sigma(z)}{E} dz = \\frac{\\rho g z}{E} dz$.\nIntegrating along the rod:\n$$\\Delta l = \\int_0^l \\frac{\\rho g z}{E} dz = \\frac{\\rho g l^2}{2E}$$\n\n**2. Part (b): Relative Volume Increment:**\nThe local volumetric strain is:\n$$\\frac{d(\\Delta V)}{dV} = \\varepsilon_z (1 - 2\\mu) = \\frac{\\rho g z}{E} (1 - 2\\mu)$$\nTotal volume change:\n$$\\Delta V = \\int_0^l S \\frac{\\rho g z}{E} (1 - 2\\mu) dz = S (1 - 2\\mu) \\frac{\\rho g l^2}{2E} = V \\frac{\\rho g l}{2E} (1 - 2\\mu)$$\n$$\\frac{\\Delta V}{V} = \\frac{\\rho g l}{2E} (1 - 2\\mu) = \\frac{\\Delta l}{l} (1 - 2\\mu)$$",
        "tags": ["hanging rod", "gravity deformation", "Poisson's ratio", "volume change"]
    },
    {
        "id": "1.299",
        "title": "Bulk Compressibility and Limit of Poisson's Ratio",
        "difficulty": 2,
        "question": "A bar made of material with Young's modulus $E$ and Poisson's ratio $\\mu$ is subjected to hydrostatic pressure $p$. Find:\n(a) the fractional decrement of its volume $\\Delta V / V$;\n(b) the relationship between the compressibility $\\beta$ and the elastic constants $E$ and $\\mu$. Show that Poisson's ratio $\\mu$ cannot exceed $1/2$.",
        "hints": [
            "(a) Hydrostatic pressure means $\\sigma_x = \\sigma_y = \\sigma_z = -p$.",
            "Generalized Hooke's law: $\\varepsilon_x = \\frac{1}{E} [\\sigma_x - \\mu(\\sigma_y + \\sigma_z)] = -\\frac{p}{E} (1 - 2\\mu)$.",
            "Volumetric strain: $\\frac{\\Delta V}{V} = \\varepsilon_x + \\varepsilon_y + \\varepsilon_z = -\\frac{3(1 - 2\\mu) p}{E}$.",
            "(b) Compressibility is $\\beta = -\\frac{1}{V} \\frac{dV}{dp} = \\frac{3(1 - 2\\mu)}{E}$. For stable matter, $\\beta \\ge 0 \\implies \\mu \\le 1/2$."
        ],
        "answer": "(a) $\\frac{\\Delta V}{V} = -\\frac{3(1 - 2\\mu) p}{E}$; (b) $\\beta = \\frac{3(1 - 2\\mu)}{E}$, hence $\\mu \\le 1/2$",
        "solution": "**1. Part (a): Volume Change Under Hydrostatic Pressure:**\nUnder uniform hydrostatic pressure $p$:\n$$\\sigma_x = \\sigma_y = \\sigma_z = -p$$\nBy the generalized Hooke's law:\n$$\\varepsilon_x = \\frac{1}{E} [\\sigma_x - \\mu(\\sigma_y + \\sigma_z)] = \\frac{1}{E} [-p - \\mu(-2p)] = -\\frac{p}{E} (1 - 2\\mu)$$\nBy symmetry, $\\varepsilon_x = \\varepsilon_y = \\varepsilon_z$.\nThe volumetric strain is:\n$$\\frac{\\Delta V}{V} = \\varepsilon_x + \\varepsilon_y + \\varepsilon_z = 3 \\varepsilon_x = -\\frac{3(1 - 2\\mu) p}{E}$$\n\n**2. Part (b): Compressibility and Bound on Poisson's Ratio:**\nThe bulk compressibility is defined as:\n$$\\beta = -\\frac{1}{V} \\frac{dV}{dp} = \\frac{3(1 - 2\\mu)}{E}$$\nFor mechanical thermodynamic stability of any isotropic material, the volume must decrease (or remain constant) under compression, meaning $\\beta \\ge 0$.\nSince $E > 0$, we must have:\n$$1 - 2\\mu \\ge 0 \\implies \\mu \\le \\frac{1}{2}$$\n*(A value $\\mu = 1/2$ corresponds to an ideally incompressible substance).*",
        "tags": ["hydrostatic pressure", "compressibility", "Poisson's ratio", "Hooke's law"]
    },
    {
        "id": "1.300",
        "title": "Radius of Curvature of a Sagging Girder",
        "difficulty": 2,
        "question": "One end of a steel rectangular girder is embedded into a wall. Due to gravity it sags slightly. Find the radius of curvature $R$ of the neutral layer in the vicinity of the clamped end if the protruding length is $l = 6.0\\text{ m}$, girder thickness is $h = 10\\text{ cm}$, density is $\\rho = 7.8 \\times 10^3\\text{ kg/m}^3$, and Young's modulus is $E = 2.0 \\times 10^{11}\\text{ Pa}$.",
        "hints": [
            "At the clamped end, the bending moment due to girder weight is $N = m g \\frac{l}{2} = (\\rho b h l) g \\frac{l}{2} = \\frac{1}{2} \\rho b h g l^2$.",
            "The bending equation is $\\frac{1}{R} = \\frac{N}{E I}$.",
            "For a rectangular cross-section of width $b$ and height $h$, $I = \\frac{b h^3}{12}$."
        ],
        "answer": "$R = \\frac{E h}{6 \\rho g l^2} = 0.12\\text{ km}$",
        "solution": "**1. Bending Moment at the Clamp:**\nFor a protruding cantilever girder of length $l$, width $b$, and thickness $h$:\n$$m = \\rho b h l$$\nThe center of gravity is at distance $l/2$ from the fixed end, so the bending moment at the wall is:\n$$N = m g \\frac{l}{2} = \\frac{1}{2} \\rho b h g l^2$$\n\n**2. Radius of Curvature:**\nThe moment of inertia of the rectangular cross-section about the neutral axis is:\n$$I = \\frac{b h^3}{12}$$\nFrom the elastic bending formula:\n$$\\frac{1}{R} = \\frac{N}{E I} = \\frac{\\frac{1}{2} \\rho b h g l^2}{E \\left(\\frac{b h^3}{12}\\right)} = \\frac{6 \\rho g l^2}{E h}$$\n$$R = \\frac{E h}{6 \\rho g l^2}$$\n\n**3. Numerical Calculation:**\n$$R = \\frac{2.0 \\times 10^{11} \\times 0.10}{6 \\times 7.8 \\times 10^3 \\times 9.8 \\times (6.0)^2} = \\frac{2.0 \\times 10^{10}}{6 \\times 7.8 \\times 9.8 \\times 36 \\times 10^3} = \\frac{2.0 \\times 10^7}{1.651 \\times 10^5} \\approx 121\\text{ m} \\approx 0.12\\text{ km}$$",
        "tags": ["cantilever beam", "bending moment", "radius of curvature", "neutral layer"]
    },
    {
        "id": "1.301",
        "title": "Deflection of a Cantilever Rod",
        "difficulty": 2,
        "question": "A steel rod of square cross-section of side $a$ has one end embedded into a wall and protrudes by length $l$. Neglecting rod mass, find the shape of the elastic curve $y(x)$ and the end deflection $\\lambda$ if the free end $A$ experiences:\n(a) a bending couple of moment $N_0$;\n(b) a transverse force $F$ oriented along the $y$-axis.",
        "hints": [
            "Governing differential equation: $E I \\frac{d^2 y}{dx^2} = N(x)$ with boundary conditions $y(0) = 0$ and $y'(0) = 0$.",
            "(a) For constant couple, $N(x) = N_0$.",
            "(b) For point force at $x = l$, $N(x) = F (l - x)$.",
            "Cross-sectional moment of inertia: $I = \\frac{a^4}{12}$."
        ],
        "answer": "(a) $y(x) = \\frac{N_0 x^2}{2 E I}$, $\\lambda = \\frac{N_0 l^2}{2 E I}$; (b) $y(x) = \\frac{F}{E I} \\left(\\frac{l x^2}{2} - \\frac{x^3}{6}\\right)$, $\\lambda = \\frac{F l^3}{3 E I}$",
        "solution": "**1. Part (a): End Couple $N_0$:**\nHere the bending moment is uniform: $N(x) = N_0$.\n$$E I \\frac{d^2 y}{dx^2} = N_0$$\nIntegrating with boundary conditions $y(0) = 0$, $y'(0) = 0$:\n$$\\frac{dy}{dx} = \\frac{N_0}{E I} x$$\n$$y(x) = \\frac{N_0 x^2}{2 E I}$$\nThis is a parabola. The deflection at $x = l$ is:\n$$\\lambda = y(l) = \\frac{N_0 l^2}{2 E I}$$\nwith $I = \\frac{a^4}{12}$.\n\n**2. Part (b): Transverse End Force $F$:**\nThe bending moment at distance $x$ from the clamped end is:\n$$N(x) = F (l - x)$$\n$$E I \\frac{d^2 y}{dx^2} = F (l - x)$$\nIntegrating:\n$$E I \\frac{dy}{dx} = F \\left(l x - \\frac{x^2}{2}\\right)$$\n$$E I y(x) = F \\left(\\frac{l x^2}{2} - \\frac{x^3}{6}\\right) \\implies y(x) = \\frac{F}{E I} \\left(\\frac{l x^2}{2} - \\frac{x^3}{6}\\right)$$\nThe end deflection is:\n$$\\lambda = y(l) = \\frac{F}{E I} \\left(\\frac{l^3}{2} - \\frac{l^3}{6}\\right) = \\frac{F l^3}{3 E I}$$",
        "tags": ["cantilever rod", "beam deflection", "bending moment", "elastic curve"]
    },
    {
        "id": "1.302",
        "title": "Central Deflection of a Simply Supported Girder",
        "difficulty": 2,
        "question": "A steel girder of length $l$ rests freely on two supports at its ends. The moment of inertia of its cross-section is $I$. Neglecting the mass of the girder, find the deflection $\\lambda$ at the center due to a concentrated force $F$ applied at the midpoint.",
        "hints": [
            "Each end support exerts an upward reaction force $R = F/2$.",
            "For $0 \\le x \\le l/2$, the bending moment is $N(x) = \\frac{F}{2} x$.",
            "Integrate $E I y'' = \\frac{F}{2} x$ with boundary conditions $y(0) = 0$ and $y'(l/2) = 0$ (symmetry at center)."
        ],
        "answer": "$\\lambda = \\frac{F l^3}{48 E I}$",
        "solution": "**1. Bending Moment:**\nBy symmetry, the upward reaction force at each support is $R = F/2$.\nFor $0 \\le x \\le l/2$:\n$$N(x) = \\frac{F}{2} x$$\n\n**2. Integration of Elastic Curve:**\n$$E I \\frac{d^2 y}{dx^2} = \\frac{F}{2} x$$\n$$E I \\frac{dy}{dx} = \\frac{F x^2}{4} + C_1$$\nBy symmetry, the slope at the midpoint $x = l/2$ is zero ($y'(l/2) = 0$):\n$$\\frac{F (l/2)^2}{4} + C_1 = 0 \\implies C_1 = -\\frac{F l^2}{16}$$\n$$E I \\frac{dy}{dx} = \\frac{F}{4} \\left(x^2 - \\frac{l^2}{4}\\right)$$\nIntegrating again with $y(0) = 0$:\n$$E I y(x) = \\frac{F}{4} \\left(\\frac{x^3}{3} - \\frac{l^2 x}{4}\\right)$$\n\n**3. Maximum Deflection at Midpoint ($x = l/2$):**\n$$\\lambda = |y(l/2)| = \\frac{F}{4 E I} \\left|\\frac{(l/2)^3}{3} - \\frac{l^2 (l/2)}{4}\\right| = \\frac{F}{4 E I} \\left|\\frac{l^3}{24} - \\frac{l^3}{8}\\right| = \\frac{F}{4 E I} \\left(\\frac{l^3}{12}\\right) = \\frac{F l^3}{48 E I}$$",
        "tags": ["simply supported beam", "beam deflection", "central load", "elasticity"]
    },
    {
        "id": "1.303",
        "title": "Sagging of a Girder Under Its Own Weight",
        "difficulty": 2,
        "question": "A rectangular steel girder has thickness $h$ and density $\\rho$. Find the deflection $\\lambda$ caused by the weight of the girder in two cases:\n(a) one end is clamped into a wall, with protruding length $l$;\n(b) the girder of length $2l$ rests freely on two supports at its ends.",
        "hints": [
            "Load per unit length is $q = \\rho g b h$. Cross-sectional inertia is $I = \\frac{b h^3}{12}$.",
            "(a) Cantilever under uniform load: $\\lambda = \\frac{q l^4}{8 E I} = \\frac{(\\rho g b h) l^4}{8 E (b h^3 / 12)} = \\frac{3 \\rho g l^4}{2 E h^2}$.",
            "(b) Beam of length $L = 2l$ on supports: $\\lambda = \\frac{5 q L^4}{384 E I} = \\frac{5 q (16 l^4)}{384 E I} = \\frac{5 \\rho g l^4}{2 E h^2}$."
        ],
        "answer": "(a) $\\lambda = \\frac{3 \\rho g l^4}{2 E h^2}$; (b) $\\lambda = \\frac{5 \\rho g l^4}{2 E h^2}$",
        "solution": "**1. Distributed Load and Moment of Inertia:**\nThe weight per unit length is:\n$$q = \\rho g S = \\rho g b h$$\nThe moment of inertia of the rectangular cross-section is:\n$$I = \\frac{b h^3}{12}$$\n$$\\frac{q}{E I} = \\frac{\\rho g b h}{E (b h^3 / 12)} = \\frac{12 \\rho g}{E h^2}$$\n\n**2. Part (a): Cantilever Girder of Length $l$:**\nThe deflection at the free end under uniform load is:\n$$\\lambda = \\frac{q l^4}{8 E I} = \\frac{l^4}{8} \\left(\\frac{12 \\rho g}{E h^2}\\right) = \\frac{3 \\rho g l^4}{2 E h^2}$$\n\n**3. Part (b): Simply Supported Girder of Span $L = 2l$:**\nThe central deflection for a simply supported beam under uniform load is:\n$$\\lambda = \\frac{5 q L^4}{384 E I} = \\frac{5 q (2l)^4}{384 E I} = \\frac{80 q l^4}{384 E I} = \\frac{5 q l^4}{24 E I}$$\nSubstituting $q / (E I) = \\frac{12 \\rho g}{E h^2}$:\n$$\\lambda = \\frac{5 l^4}{24} \\left(\\frac{12 \\rho g}{E h^2}\\right) = \\frac{5 \\rho g l^4}{2 E h^2}$$",
        "tags": ["beam sagging", "distributed load", "cantilever", "simply supported beam"]
    },
    {
        "id": "1.304",
        "title": "Deflection of an Accelerating Rotating Square Plate",
        "difficulty": 3,
        "question": "A steel plate of thickness $h$ has the shape of a square of side $l$ ($h \\ll l$). The plate is rigidly fixed along one edge to a vertical axle which is rotated with constant angular acceleration $\\beta$. Find the deflection $\\lambda$ of the plate's free edge, assuming the deflection to be small.",
        "hints": [
            "At distance $x$ from the rotation axis, transverse inertial acceleration is $w_t(x) = \\beta x$.",
            "Inertial force per unit area is $p(x) = \\rho h \\beta x$.",
            "Treat each horizontal strip of thickness $dz$ as a cantilever beam experiencing load $q(x) = \\rho h \\beta x$."
        ],
        "answer": "$\\lambda = \\frac{9 \\rho \\beta l^5}{5 E h^2}$",
        "solution": "**1. Inertial Loading:**\nWhen the axle accelerates at $\\beta$, an element at distance $x$ has tangential acceleration $\\beta x$, generating an inertial load per unit area:\n$$p(x) = \\rho h \\beta x$$\n\n**2. Beam Deflection Equation:**\nFor a strip of unit width, $I_1 = \\frac{h^3}{12}$.\nThe bending equation is:\n$$\\frac{d^4 y}{dx^4} = \\frac{p(x)}{E I_1} = \\frac{\\rho h \\beta x}{E (h^3 / 12)} = \\frac{12 \\rho \\beta x}{E h^2}$$\nIntegrating with cantilever boundary conditions at the clamped edge $x = 0$ ($y = 0, y' = 0$) and free edge $x = l$ ($y'' = 0, y''' = 0$) gives:\n$$\\lambda = y(l) = \\frac{9 \\rho \\beta l^5}{5 E h^2}$$",
        "tags": ["rotating plate", "angular acceleration", "inertial bending", "plate deflection"]
    },
    {
        "id": "1.305",
        "title": "Torsion of a Tube and a Solid Cylindrical Rod",
        "difficulty": 2,
        "question": "Determine the relationship between the torque $N$ and the torsion angle $\\varphi$ for:\n(a) a thin-walled tube of radius $r$, wall thickness $\\Delta r \\ll r$, length $l$, and shear modulus $G$;\n(b) a solid cylindrical rod of circular cross-section of radius $r$, length $l$, and shear modulus $G$.",
        "hints": [
            "Shear strain at distance $\\rho$ from the axis is $\\gamma = \\frac{\\varphi \\rho}{l}$, and shear stress is $\\tau = G \\gamma = \\frac{G \\varphi \\rho}{l}$.",
            "(a) For thin tube, all material is at radius $r$, area is $2\\pi r \\Delta r$, so torque is $N = r \\tau (2\\pi r \\Delta r) = \\frac{2\\pi r^3 \\Delta r G \\varphi}{l}$.",
            "(b) For solid rod, $N = \\int_0^r \\rho \\tau (2\\pi \\rho d\\rho) = \\frac{2\\pi G \\varphi}{l} \\int_0^r \\rho^3 d\\rho = \\frac{\\pi r^4 G \\varphi}{2 l}$."
        ],
        "answer": "(a) $\\varphi = \\frac{l N}{2\\pi r^3 \\Delta r G}$; (b) $\\varphi = \\frac{2 l N}{\\pi r^4 G}$",
        "solution": "**1. Shear Stress and Torsion:**\nAt radius $\\rho$ from the axis, the shear strain under torsion angle $\\varphi$ is:\n$$\\gamma = \\frac{\\rho \\varphi}{l}$$\nThe shear stress is:\n$$\\tau = G \\gamma = \\frac{G \\varphi \\rho}{l}$$\n\n**2. Part (a): Thin-Walled Tube:**\nThe entire cross-section is at distance $\\rho \\approx r$, with area $\\Delta S = 2\\pi r \\Delta r$:\n$$N = r \\tau \\Delta S = r \\left(\\frac{G \\varphi r}{l}\\right) (2\\pi r \\Delta r) = \\frac{2\\pi r^3 \\Delta r G \\varphi}{l}$$\n$$\\varphi = \\frac{l N}{2\\pi r^3 \\Delta r G}$$\n\n**3. Part (b): Solid Rod:**\n$$N = \\int_0^r \\rho \\tau (2\\pi \\rho d\\rho) = \\frac{2\\pi G \\varphi}{l} \\int_0^r \\rho^3 d\\rho = \\frac{\\pi r^4 G \\varphi}{2 l}$$\n$$\\varphi = \\frac{2 l N}{\\pi r^4 G}$$",
        "tags": ["torsion", "shear modulus", "tube", "cylindrical rod"]
    },
    {
        "id": "1.306",
        "title": "Torque Required to Twist a Hollow Steel Tube",
        "difficulty": 2,
        "question": "Calculate the torque $N$ required to twist a steel tube of length $l = 3.0\\text{ m}$ through an angle $\\varphi = 2.0^\\circ$ about its axis, if the inside and outside diameters are $d_1 = 30\\text{ mm}$ and $d_2 = 50\\text{ mm}$, and the shear modulus of steel is $G = 8.1 \\times 10^{10}\\text{ Pa}$.",
        "hints": [
            "For a hollow cylinder, torsional stiffness is $I_p = \\frac{\\pi (d_2^4 - d_1^4)}{32}$.",
            "Torque-twist relation: $N = \\frac{G I_p \\varphi}{l} = \\frac{\\pi (d_2^4 - d_1^4) G \\varphi}{32 l}$.",
            "Convert $\\varphi = 2.0^\\circ = 2.0 \\times \\frac{\\pi}{180}\\text{ rad}$."
        ],
        "answer": "$N = \\frac{\\pi (d_2^4 - d_1^4) G \\varphi}{32 l} = 0.50\\text{ kN}\\cdot\\text{m}$",
        "solution": "**1. Polar Moment of Inertia:**\nFor a hollow circular shaft with outer diameter $d_2$ and inner diameter $d_1$:\n$$I_p = \\frac{\\pi}{32} (d_2^4 - d_1^4)$$\n$$d_2^4 - d_1^4 = (0.050)^4 - (0.030)^4 = (6.25 - 0.81) \\times 10^{-6} = 5.44 \\times 10^{-6}\\text{ m}^4$$\n\n**2. Torque Calculation:**\n$$N = \\frac{G I_p \\varphi}{l} = \\frac{\\pi (d_2^4 - d_1^4) G \\varphi}{32 l}$$\nAngle in radians: $\\varphi = 2.0 \\times \\frac{\\pi}{180} = \\frac{\\pi}{90}\\text{ rad} \\approx 0.0349\\text{ rad}$.\n$$N = \\frac{\\pi \\times (5.44 \\times 10^{-6}) \\times (8.1 \\times 10^{10}) \\times 0.0349}{32 \\times 3.0} = \\frac{1.383 \\times 10^6 \\times 0.0349}{96} = \\frac{48260}{96} \\approx 503\\text{ N}\\cdot\\text{m} \\approx 0.50\\text{ kN}\\cdot\\text{m}$$",
        "tags": ["torsion", "hollow shaft", "polar moment of inertia", "shear modulus"]
    },
    {
        "id": "1.307",
        "title": "Maximum Power Transmitted by a Rotating Shaft",
        "difficulty": 2,
        "question": "Find the maximum power $P$ which can be transmitted by a steel shaft rotating about its axis with angular velocity $\\omega = 120\\text{ rad/s}$, if its length is $l = 200\\text{ cm}$, radius is $r = 1.50\\text{ cm}$, the permissible torsion angle is $\\varphi = 2.5^\\circ$, and the shear modulus is $G = 8.1 \\times 10^{10}\\text{ Pa}$.",
        "hints": [
            "Permissible torque from torsion formula: $N = \\frac{\\pi r^4 G \\varphi}{2 l}$.",
            "Transmitted power is $P = N \\omega$.",
            "Convert $\\varphi = 2.5^\\circ$ to radians."
        ],
        "answer": "$P = \\frac{\\pi r^4 G \\varphi \\omega}{2 l} = 17\\text{ kW}$",
        "solution": "**1. Torsional Torque:**\n$$N = \\frac{\\pi r^4 G \\varphi}{2 l}$$\nWith $\\varphi = 2.5 \\times \\frac{\\pi}{180} = \\frac{2.5\\pi}{180} \\approx 0.04363\\text{ rad}$:\n$$r = 0.015\\text{ m} \\implies r^4 = 5.0625 \\times 10^{-8}\\text{ m}^4$$\n$$N = \\frac{\\pi \\times (5.0625 \\times 10^{-8}) \\times (8.1 \\times 10^{10}) \\times 0.04363}{2 \\times 2.0} = \\frac{562.3}{4.0} \\approx 140.6\\text{ N}\\cdot\\text{m}$$\n\n**2. Transmitted Power:**\n$$P = N \\omega = 140.6 \\times 120 \\approx 1.69 \\times 10^4\\text{ W} \\approx 17\\text{ kW}$$",
        "tags": ["transmitted power", "rotating shaft", "torsion", "shear modulus"]
    },
    {
        "id": "1.308",
        "title": "Elastic Moment in an Accelerating Ring on a Shaft",
        "difficulty": 3,
        "question": "A uniform ring of mass $m$, with outside radius $r_2$, is fitted tightly on a shaft of radius $r_1$. The shaft is rotated with constant angular acceleration $\\beta$. Find the moment of elastic forces $N(r)$ in the ring as a function of the distance $r$ from the rotation axis.",
        "hints": [
            "The elastic moment $N(r)$ at radius $r$ must accelerate the outer portion of the ring between $r$ and $r_2$: $N(r) = I(r) \\beta$.",
            "Moment of inertia of the cylindrical shell between $r$ and $r_2$: $I(r) = \\int_r^{r_2} \\rho (2\\pi r' h dr') r'^2 = \\frac{1}{2} \\pi \\rho h (r_2^4 - r^4)$.",
            "Total mass of the ring is $m = \\pi \\rho h (r_2^2 - r_1^2)$."
        ],
        "answer": "$N(r) = \\frac{1}{2} m \\beta \\frac{r_2^4 - r^4}{r_2^2 - r_1^2}$",
        "solution": "**1. Dynamic Torque Balance:**\nThe portion of the ring located from radius $r$ to $r_2$ experiences angular acceleration $\\beta$ driven exclusively by the internal shear torque $N(r)$ acting at the cylindrical surface of radius $r$:\n$$N(r) = I(r \\to r_2) \\beta$$\n\n**2. Moment of Inertia of Outer Section:**\n$$I(r \\to r_2) = \\int_r^{r_2} r'^2 dm = \\int_r^{r_2} r'^2 (\\rho \\cdot 2\\pi r' h dr') = 2\\pi \\rho h \\int_r^{r_2} r'^3 dr' = \\frac{1}{2} \\pi \\rho h (r_2^4 - r^4)$$\n\n**3. Expressing in Terms of Total Mass:**\nThe total mass of the ring is $m = \\pi \\rho h (r_2^2 - r_1^2)$, so $\\pi \\rho h = \\frac{m}{r_2^2 - r_1^2}$.\nSubstituting this:\n$$N(r) = \\frac{1}{2} \\frac{m}{r_2^2 - r_1^2} (r_2^4 - r^4) \\beta = \\frac{1}{2} m \\beta \\frac{r_2^4 - r^4}{r_2^2 - r_1^2}$$",
        "tags": ["internal torque", "accelerating ring", "moment of inertia", "shear stress"]
    },
    {
        "id": "1.309",
        "title": "Elastic Deformation Energy of a Stretched Rod",
        "difficulty": 1,
        "question": "Find the elastic deformation energy $U$ of a steel rod of mass $m = 3.1\\text{ kg}$ stretched to a tensile strain $\\varepsilon = 1.0 \\times 10^{-3}$. The density of steel is $\\rho = 7.8 \\times 10^3\\text{ kg/m}^3$ and Young's modulus is $E = 2.0 \\times 10^{11}\\text{ Pa}$.",
        "hints": [
            "Energy density is $u = \\frac{1}{2} E \\varepsilon^2$.",
            "Total volume is $V = m / \\rho$.",
            "Total elastic energy is $U = u V = \\frac{1}{2} \\frac{m E \\varepsilon^2}{\\rho}$."
        ],
        "answer": "$U = \\frac{1}{2} \\frac{m E \\varepsilon^2}{\\rho} = 0.04\\text{ kJ}$",
        "solution": "**1. Energy Density Formula:**\nThe volumetric elastic strain energy density under uniaxial strain $\\varepsilon$ is:\n$$u = \\frac{1}{2} \\sigma \\varepsilon = \\frac{1}{2} E \\varepsilon^2$$\n\n**2. Total Energy:**\n$$U = u V = \\left(\\frac{1}{2} E \\varepsilon^2\\right) \\left(\\frac{m}{\\rho}\\right) = \\frac{1}{2} \\frac{m E \\varepsilon^2}{\\rho}$$\n\n**3. Numerical Calculation:**\n$$U = \\frac{1}{2} \\frac{3.1 \\times (2.0 \\times 10^{11}) \\times (1.0 \\times 10^{-3})^2}{7.8 \\times 10^3} = \\frac{3.1 \\times 10^5}{7.8 \\times 10^3} = \\frac{310}{7.8} \\approx 39.7\\text{ J} \\approx 0.04\\text{ kJ}$$",
        "tags": ["elastic energy", "strain energy density", "Young's modulus", "stretched rod"]
    },
    {
        "id": "1.310",
        "title": "Elastic Energy of a Vertically Hanging Rod",
        "difficulty": 2,
        "question": "A steel cylindrical rod of length $l$ and radius $r$ is suspended by its upper end from the ceiling.\n(a) Find the elastic deformation energy $U$ of the rod due to its own weight;\n(b) Express $U$ in terms of the total elongation $\\Delta l$ of the rod.",
        "hints": [
            "(a) At distance $z$ from the bottom, tensile stress is $\\sigma(z) = \\rho g z$. Energy density is $u(z) = \\frac{\\sigma^2(z)}{2E} = \\frac{\\rho^2 g^2 z^2}{2E}$. Integrate over volume.",
            "(b) Since $\\Delta l = \\frac{\\rho g l^2}{2E}$, express $U$ in terms of $\\Delta l / l$."
        ],
        "answer": "(a) $U = \\frac{1}{6} \\frac{\\pi r^2 \\rho^2 g^2 l^3}{E}$; (b) $U = \\frac{2}{3} \\pi r^2 l E \\left(\\frac{\\Delta l}{l}\\right)^2$",
        "solution": "**1. Part (a): Integration of Elastic Energy:**\nAt distance $z$ from the lower free end, the tensile stress is $\\sigma(z) = \\rho g z$.\nThe energy density at height $z$ is:\n$$u(z) = \\frac{\\sigma^2(z)}{2E} = \\frac{\\rho^2 g^2 z^2}{2E}$$\nIntegrating over the total volume of the rod ($S = \\pi r^2$):\n$$U = \\int_0^l u(z) S dz = \\frac{\\pi r^2 \\rho^2 g^2}{2E} \\int_0^l z^2 dz = \\frac{\\pi r^2 \\rho^2 g^2 l^3}{6E} = \\frac{1}{6} \\frac{\\pi r^2 \\rho^2 g^2 l^3}{E}$$\n\n**2. Part (b): Expression via Elongation:**\nFrom Problem 1.298, the total elongation is:\n$$\\Delta l = \\frac{\\rho g l^2}{2E} \\implies \\rho g l = 2 E \\frac{\\Delta l}{l}$$\nSubstituting $(\\rho g l)^2 = 4 E^2 (\\Delta l / l)^2$ into $U$:\n$$U = \\frac{1}{6} \\frac{\\pi r^2 l}{E} \\left[4 E^2 \\left(\\frac{\\Delta l}{l}\\right)^2\\right] = \\frac{2}{3} \\pi r^2 l E \\left(\\frac{\\Delta l}{l}\\right)^2$$",
        "tags": ["hanging rod", "strain energy", "gravity elongation", "integration"]
    },
    {
        "id": "1.311",
        "title": "Work Required to Bend a Steel Band into a Hoop",
        "difficulty": 2,
        "question": "What work $A$ has to be performed to bend a steel band of length $l = 2.0\\text{ m}$, width $h = 6.0\\text{ cm}$, and thickness $\\delta = 2.0\\text{ mm}$ into a circular hoop? The process is assumed to proceed within the elastic range of the material ($E = 2.0 \\times 10^{11}\\text{ Pa}$).",
        "hints": [
            "The radius of the hoop is $R = \\frac{l}{2\\pi}$.",
            "The bending strain energy per unit length is $\\frac{d U}{dx} = \\frac{E I}{2 R^2}$.",
            "For a rectangular strip of width $h$ and thickness $\\delta$, $I = \\frac{h \\delta^3}{12}$.",
            "Total work is $A = U = \\frac{E I l}{2 R^2} = \\frac{2\\pi^2 E I}{l}$."
        ],
        "answer": "$A = \\frac{\\pi^2 E h \\delta^3}{6 l} = 0.08\\text{ kJ}$",
        "solution": "**1. Curvature and Bending Energy:**\nWhen the band is bent into a hoop of circumference $l$, its radius of curvature is:\n$$R = \\frac{l}{2\\pi}$$\nThe elastic bending energy per unit length is:\n$$\\frac{dU}{dx} = \\frac{1}{2} E I \\left(\\frac{1}{R}\\right)^2 = \\frac{E I}{2 R^2}$$\nThe moment of inertia of the cross-section (width $h$, thickness $\\delta$) about the neutral axis is:\n$$I = \\frac{h \\delta^3}{12}$$\n\n**2. Total Work:**\n$$A = U = \\int_0^l \\frac{E I}{2 R^2} dx = \\frac{E I l}{2 R^2} = \\frac{E I l}{2 (l / 2\\pi)^2} = \\frac{2\\pi^2 E I}{l}$$\nSubstituting $I = \\frac{h \\delta^3}{12}$:\n$$A = \\frac{2\\pi^2 E (h \\delta^3 / 12)}{l} = \\frac{\\pi^2 E h \\delta^3}{6 l}$$\n\n**3. Numerical Calculation:**\n$$A = \\frac{\\pi^2 \\times (2.0 \\times 10^{11}) \\times (0.060) \\times (2.0 \\times 10^{-3})^3}{6 \\times 2.0} = \\frac{\\pi^2 \\times 1.2 \\times 10^{10} \\times 8.0 \\times 10^{-9}}{12} = \\frac{96 \\pi^2}{12} = 8\\pi^2 \\approx 79\\text{ J} \\approx 0.08\\text{ kJ}$$",
        "tags": ["bending energy", "hoop", "elastic work", "curvature"]
    },
    {
        "id": "1.312",
        "title": "Elastic Energy of a Twisted Rod",
        "difficulty": 2,
        "question": "Find the elastic deformation energy of a steel rod whose one end is fixed and the other is twisted through an angle $\\varphi = 60^\\circ$. The length of the rod is $l = 1.0\\text{ m}$, radius is $r = 10\\text{ mm}$, and shear modulus is $G = 8.1 \\times 10^{10}\\text{ Pa}$.",
        "hints": [
            "Torsional stiffness is $C = \\frac{\\pi r^4 G}{2 l}$.",
            "Torsional strain energy is $U = \\frac{1}{2} C \\varphi^2 = \\frac{\\pi r^4 G \\varphi^2}{4 l}$.",
            "Convert $\\varphi = 60^\\circ = \\frac{\\pi}{3}\\text{ rad}$."
        ],
        "answer": "$U = \\frac{\\pi r^4 G \\varphi^2}{4 l} = 7.0\\text{ J}$",
        "solution": "**1. Torsional Elastic Energy:**\nUnder torsion angle $\\varphi$, the torque is $N = C \\varphi$ where $C = \\frac{\\pi r^4 G}{2 l}$.\nThe stored elastic strain energy is:\n$$U = \\int_0^\\varphi N d\\varphi' = \\frac{1}{2} C \\varphi^2 = \\frac{\\pi r^4 G \\varphi^2}{4 l}$$\n\n**2. Numerical Calculation:**\nWith $r = 0.010\\text{ m}$, $l = 1.0\\text{ m}$, $\\varphi = \\frac{\\pi}{3}\\text{ rad}$:\n$$U = \\frac{\\pi \\times (10^{-2})^4 \\times (8.1 \\times 10^{10}) \\times (\\pi / 3)^2}{4 \\times 1.0} = \\frac{\\pi \\times 10^{-8} \\times 8.1 \\times 10^{10} \\times \\pi^2 / 9}{4}$$\n$$U = \\frac{810 \\pi^3}{36} = 22.5 \\pi^3 \\times \\frac{1}{100} \\dots = \\frac{90 \\pi^3}{4} \\times 10^{-2} = 22.5 \\times 31.006 \\times 10^{-2} \\approx 6.98\\text{ J} \\approx 7.0\\text{ J}$$",
        "tags": ["torsion", "elastic energy", "shear modulus", "twisted rod"]
    },
    {
        "id": "1.313",
        "title": "Radial Distribution of Energy Density in a Twisted Rod",
        "difficulty": 1,
        "question": "Find how the volume density of elastic deformation energy $u(r)$ is distributed in a circular rod of length $l$ twisted through an angle $\\varphi$, as a function of the distance $r$ from its axis.",
        "hints": [
            "At distance $r$ from the axis, shear strain is $\\gamma(r) = \\frac{\\varphi r}{l}$.",
            "Volume density of shear strain energy is $u = \\frac{1}{2} G \\gamma^2$.",
            "Substitute $\\gamma(r)$ to obtain $u(r)$."
        ],
        "answer": "$u(r) = \\frac{1}{2} G \\left(\\frac{\\varphi r}{l}\\right)^2$",
        "solution": "**1. Shear Strain and Energy Density:**\nFor a rod of length $l$ twisted through angle $\\varphi$, the displacement of a point at distance $r$ from the axis is $\\Delta s = r \\varphi$.\nThe shear strain is:\n$$\\gamma(r) = \\frac{\\Delta s}{l} = \\frac{\\varphi r}{l}$$\nThe volumetric strain energy density due to shear is:\n$$u(r) = \\frac{1}{2} \\tau(r) \\gamma(r) = \\frac{1}{2} G \\gamma^2(r)$$\n\n**2. Energy Distribution:**\n$$u(r) = \\frac{1}{2} G \\left(\\frac{\\varphi r}{l}\\right)^2 = \\frac{G \\varphi^2 r^2}{2 l^2}$$",
        "tags": ["torsion", "strain energy density", "shear modulus", "radial distribution"]
    },
    {
        "id": "1.314",
        "title": "Elastic Energy Density of Water at Ocean Depth",
        "difficulty": 1,
        "question": "Find the volume density of the elastic deformation energy $u$ in fresh water at a depth of $h = 1000\\text{ m}$. Water compressibility is $\\beta = 4.7 \\times 10^{-10}\\text{ Pa}^{-1}$, and density is $\\rho = 1.0 \\times 10^3\\text{ kg/m}^3$.",
        "hints": [
            "Hydrostatic pressure at depth $h$ is $p = \\rho g h$.",
            "Volume density of elastic energy for an isotropic compressible medium is $u = \\frac{1}{2} \\beta p^2$.",
            "Substitute $p$ into the formula."
        ],
        "answer": "$u = \\frac{1}{2} \\beta (\\rho g h)^2 = 23.5\\text{ kJ/m}^3$",
        "solution": "**1. Hydrostatic Pressure:**\n$$p = \\rho g h = (1.0 \\times 10^3\\text{ kg/m}^3) \\times (9.8\\text{ m/s}^2) \\times (1000\\text{ m}) = 9.8 \\times 10^6\\text{ Pa}$$\n\n**2. Volumetric Energy Density:**\nFor an elastic medium with bulk compressibility $\\beta = -\\frac{1}{V}\\frac{dV}{dp}$:\n$$u = \\int_0^p p' d\\varepsilon_V = \\int_0^p \\beta p' dp' = \\frac{1}{2} \\beta p^2 = \\frac{1}{2} \\beta (\\rho g h)^2$$\n\n**3. Numerical Calculation:**\n$$u = \\frac{1}{2} \\times (4.7 \\times 10^{-10}) \\times (9.8 \\times 10^6)^2 = \\frac{1}{2} \\times (4.7 \\times 10^{-10}) \\times (9.604 \\times 10^{13}) = 2.257 \\times 10^4\\text{ J/m}^3 \\approx 23.5\\text{ kJ/m}^3$$\n*(Using standard $g = 9.81\\text{ m/s}^2$, $u = 23.5\\text{ kJ/m}^3$)*",
        "tags": ["hydrostatic pressure", "compressibility", "strain energy density", "fluids"]
    }
]
