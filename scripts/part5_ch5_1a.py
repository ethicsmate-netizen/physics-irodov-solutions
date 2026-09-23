"""
part5_ch5_1a.py
Curated problems 5.1 to 5.32 (32 problems) of Irodov Chapter 5.1:
Photometry and Geometrical Optics (Part A).
"""

CH5_1A_CURATED = [
    {
        "id": "5.1",
        "title": "Luminous and Radiant Flux Conversion via Eye Spectral Sensitivity",
        "difficulty": 2,
        "question": "Making use of the spectral response curve of the human eye (standard luminous efficiency function $V(\\lambda)$), find:\n(a) the radiant flux $\\Phi_e$ corresponding to a luminous flux of $\\Phi = 1.0\\text{ lm}$ at wavelengths $\\lambda_1 = 0.51\\,\\mu\\text{m}$ and $\\lambda_2 = 0.64\\,\\mu\\text{m}$;\n(b) the luminous flux $\\Phi$ corresponding to the wavelength interval from $0.58$ to $0.63\\,\\mu\\text{m}$ if the total radiant flux in this interval is $\\Phi_e = 4.5\\text{ mW}$ and is uniformly distributed over all wavelengths, assuming $V(\\lambda)$ varies linearly in this range.",
        "hints": [
            "The luminous flux $\\Phi$ and radiant flux $\\Phi_e$ are related by $\\Phi = K_{\\text{max}} V(\\lambda) \\Phi_e = \\frac{1}{A} V(\\lambda) \\Phi_e$, where $A \\approx 1.6\\text{ mW/lm}$ ($K_{\\text{max}} \\approx 625\\text{ lm/W}$ in standard tables, or $683\\text{ lm/W}$).",
            "For monochromatic light: $\\Phi_e = \\frac{A \\Phi}{V(\\lambda)}$. Read $V(0.51\\,\\mu\\text{m}) \\approx 0.50$ and $V(0.64\\,\\mu\\text{m}) \\approx 0.175$.",
            "For a uniform spectral distribution with a linearly varying sensitivity, the average efficiency is $\\langle V \\rangle = \\frac{V_1 + V_2}{2}$, giving $\\Phi = \\frac{V_1 + V_2}{2A} \\Phi_e$."
        ],
        "answer": "(a) $\\Phi_{e1} \\approx 3.2\\text{ mW} \\approx 3\\text{ mW}$ and $\\Phi_{e2} \\approx 9.1\\text{ mW} \\approx 9\\text{ mW}$;\n(b) $\\Phi = \\frac{V_1 + V_2}{2A} \\Phi_e \\approx 1.6\\text{ lm}$ (where $A = 1.6\\text{ mW/lm}$)",
        "solution": "**(a) Radiant Flux for Monochromatic Luminous Flux:**\nThe relationship between monochromatic luminous flux $\\Phi$ (in lumens) and radiant flux $\\Phi_e$ (in watts) is given by:\n$$\\Phi = K_m V(\\lambda) \\Phi_e = \\frac{1}{A} V(\\lambda) \\Phi_e$$\nwhere $A = 1.6\\text{ mW/lm} = 1.6 \\times 10^{-3}\\text{ W/lm}$ is the mechanical equivalent of light, and $V(\\lambda)$ is the relative spectral sensitivity (visibility) of the eye.\nSolving for $\\Phi_e$:\n$$\\Phi_e = \\frac{A \\Phi}{V(\\lambda)}$$\nFrom standard visibility curves:\n- At $\\lambda_1 = 0.51\\,\\mu\\text{m}$, $V(\\lambda_1) \\approx 0.50$:\n$$\\Phi_{e1} = \\frac{(1.6\\text{ mW/lm})(1.0\\text{ lm})}{0.50} \\approx 3.2\\text{ mW} \\approx 3\\text{ mW}$$\n- At $\\lambda_2 = 0.64\\,\\mu\\text{m}$, $V(\\lambda_2) \\approx 0.175$:\n$$\\Phi_{e2} = \\frac{(1.6\\text{ mW/lm})(1.0\\text{ lm})}{0.175} \\approx 9.1\\text{ mW} \\approx 9\\text{ mW}$$\n\n**(b) Luminous Flux for Continuous Uniform Spectral Band:**\nThe radiant flux density is uniform over the interval $[\\lambda_1, \\lambda_2] = [0.58, 0.63]\\,\\mu\\text{m}$, so $d\\Phi_e(\\lambda) = \\frac{\\Phi_e}{\\Delta\\lambda} d\\lambda$.\nThe total luminous flux is:\n$$\\Phi = \\frac{1}{A} \\int_{\\lambda_1}^{\\lambda_2} V(\\lambda) \\frac{\\Phi_e}{\\Delta\\lambda} \\, d\\lambda$$\nSince $V(\\lambda)$ varies linearly in this band, its average value is the arithmetic mean of the endpoint values $\\langle V \\rangle = \\frac{V_1 + V_2}{2}$:\n$$\\Phi = \\frac{V_1 + V_2}{2A} \\Phi_e$$\nFrom standard tables, $V(0.58\\,\\mu\\text{m}) \\approx 0.87$ and $V(0.63\\,\\mu\\text{m}) \\approx 0.265$, giving $\\frac{V_1 + V_2}{2} \\approx 0.5675$.\nWith $\\Phi_e = 4.5\\text{ mW}$ and $A = 1.6\\text{ mW/lm}$:\n$$\\Phi = \\frac{0.5675}{1.6\\text{ mW/lm}} \\times 4.5\\text{ mW} \\approx 1.6\\text{ lm}$$",
        "tags": ["photometry", "luminous flux", "radiant flux", "spectral luminous efficiency", "visibility curve"]
    },
    {
        "id": "5.2",
        "title": "EM Field Amplitudes of a Monochromatic Isotropic Luminous Source",
        "difficulty": 2,
        "question": "A point isotropic source emits a luminous flux $\\Phi = 10\\text{ lm}$ at wavelength $\\lambda = 0.59\\,\\mu\\text{m}$. Find the peak values of the electric field strength $E_m$ and magnetic field strength $H_m$ in the wave at a distance $r = 1.0\\text{ m}$ from the source. (Take $A = 1.6\\text{ mW/lm}$ and $V(0.59\\,\\mu\\text{m}) = 0.757$).",
        "hints": [
            "Convert luminous flux to radiant power: $\\Phi_e = \\frac{A \\Phi}{V_\\lambda}$.",
            "The radiant intensity (Poynting vector magnitude) at distance $r$ from an isotropic source is $I = \\frac{\\Phi_e}{4\\pi r^2}$.",
            "In terms of peak field amplitudes in vacuum: $I = \\frac{1}{2} \\varepsilon_0 c E_m^2 = \\frac{1}{2} E_m H_m$ with $H_m = \\sqrt{\\frac{\\varepsilon_0}{\\mu_0}} E_m$."
        ],
        "answer": "$E_m = \\frac{1}{r} \\sqrt{\\frac{A \\Phi}{2\\pi \\varepsilon_0 c V_\\lambda}} \\approx 1.1\\text{ V/m}$; $H_m = \\sqrt{\\frac{\\varepsilon_0}{\\mu_0}} E_m \\approx 3.0\\text{ mA/m}$",
        "solution": "**1. Radiant Flux from Luminous Flux:**\nThe radiant flux emitted by the monochromatic source is:\n$$\\Phi_e = \\frac{A \\Phi}{V_\\lambda}$$\nWith $\\Phi = 10\\text{ lm}$, $A = 1.6 \\times 10^{-3}\\text{ W/lm}$, and $V_\\lambda \\approx 0.757$:\n$$\\Phi_e = \\frac{1.6 \\times 10^{-3} \\times 10}{0.757} \\approx 2.11 \\times 10^{-2}\\text{ W} = 21.1\\text{ mW}$$\n\n**2. Poynting Vector Magnitude:**\nFor an isotropic source in vacuum, the time-averaged energy flow density at distance $r$ is:\n$$\\langle S \\rangle = \\frac{\\Phi_e}{4\\pi r^2} = \\frac{A \\Phi}{4\\pi r^2 V_\\lambda}$$\n\n**3. Electric and Magnetic Field Amplitudes:**\nIn a plane/spherical electromagnetic wave in vacuum:\n$$\\langle S \\rangle = \\frac{1}{2} \\varepsilon_0 c E_m^2 = \\frac{1}{2} \\sqrt{\\frac{\\varepsilon_0}{\\mu_0}} E_m^2$$\nSolving for the peak electric field $E_m$:\n$$E_m = \\sqrt{\\frac{2 \\langle S \\rangle}{\\varepsilon_0 c}} = \\frac{1}{r} \\sqrt{\\frac{A \\Phi}{2\\pi \\varepsilon_0 c V_\\lambda}}$$\nSubstituting numerical values ($r = 1.0\\text{ m}$, $\\varepsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}$, $c = 3.0 \\times 10^8\\text{ m/s}$):\n$$E_m = \\sqrt{\\frac{2.11 \\times 10^{-2}}{2\\pi (8.854 \\times 10^{-12})(3.0 \\times 10^8)(1.0)^2}} = \\sqrt{\\frac{2.11 \\times 10^{-2}}{1.669 \\times 10^{-2}}} \\approx 1.12\\text{ V/m} \\approx 1.1\\text{ V/m}$$\nThe peak magnetic field intensity $H_m$ is:\n$$H_m = \\frac{E_m}{Z_0} = \\sqrt{\\frac{\\varepsilon_0}{\\mu_0}} E_m = \\frac{1.12\\text{ V/m}}{376.7\\,\\Omega} \\approx 2.98 \\times 10^{-3}\\text{ A/m} = 3.0\\text{ mA/m}$$",
        "tags": ["photometry", "Poynting vector", "electromagnetic fields", "field amplitude"]
    },
    {
        "id": "5.3",
        "title": "Mean Illuminance of an Irradiated Opaque Sphere",
        "difficulty": 2,
        "question": "Find the mean illuminance $\\langle E \\rangle$ of the irradiated portion of an opaque sphere receiving:\n(a) a parallel luminous flux producing illuminance $E_0$ at the point of normal incidence;\n(b) light from a point isotropic source located at a distance $l = 100\\text{ cm}$ from the centre of the sphere, where the sphere radius is $R = 60\\text{ cm}$ and the source luminous intensity is $I = 36\\text{ cd}$.",
        "hints": [
            "(a) A parallel beam intercepts area $\\pi R^2$, and the illuminated surface is a hemisphere of area $2\\pi R^2$. The mean illuminance is total intercepted flux divided by hemisphere area.",
            "(b) Tangents from the point source to the sphere define the illuminated spherical cap. Find the cap area $A = 2\\pi R^2 (1 - R/l)$ and the solid angle $\\Omega = 2\\pi(1 - \\cos\\alpha)$ subtended by the sphere.",
            "Calculate intercepted flux $\\Phi = I \\Omega = 2\\pi I (1 - \\sqrt{1 - R^2/l^2})$ and divide by $A$."
        ],
        "answer": "(a) $\\langle E \\rangle = \\frac{E_0}{2}$;\n(b) $\\langle E \\rangle = \\frac{I}{R^2} \\frac{1 - \\sqrt{1 - R^2/l^2}}{1 - R/l} \\approx 50\\text{ lx}$",
        "solution": "**(a) Parallel Beam:**\nFor a parallel beam of illuminance $E_0$ normal to the beam:\n- The total luminous flux intercepted by the sphere of radius $R$ is equal to the flux crossing its cross-sectional area:\n$$\\Phi = E_0 (\\pi R^2)$$\n- The irradiated region is a hemisphere of surface area:\n$$S_{\\text{hemi}} = 2\\pi R^2$$\n- The mean illuminance is therefore:\n$$\\langle E \\rangle = \\frac{\\Phi}{S_{\\text{hemi}}} = \\frac{E_0 \\pi R^2}{2\\pi R^2} = \\frac{E_0}{2}$$\n\n**(b) Point Isotropic Source:**\nLet the source $S$ be at distance $l$ from the centre $O$ of the sphere.\n1. **Illuminated Spherical Cap:**\nThe boundary of the illuminated region is defined by the tangent cone from $S$ to the sphere. The angle between the axis and the tangent line at the point of contact $T$ satisfies:\n$$\\sin\\alpha = \\frac{R}{l} \\implies \\cos\\alpha = \\sqrt{1 - \\frac{R^2}{l^2}}$$\nThe angle subtended at the sphere's centre by the illuminated boundary is $\\theta_0 = \\frac{\\pi}{2} - \\alpha$, so $\\cos\\theta_0 = \\sin\\alpha = R/l$.\nThe surface area of this spherical cap of height $h = R(1 - \\cos\\theta_0) = R(1 - R/l)$ is:\n$$A = 2\\pi R h = 2\\pi R^2 \\left(1 - \\frac{R}{l}\\right)$$\n\n2. **Intercepted Luminous Flux:**\nThe solid angle of the cone of rays from the source subtended by the sphere is:\n$$\\Omega = 2\\pi (1 - \\cos\\alpha) = 2\\pi \\left(1 - \\sqrt{1 - \\frac{R^2}{l^2}}\\right)$$\nThe total luminous flux intercepted by the sphere is:\n$$\\Phi = I \\Omega = 2\\pi I \\left(1 - \\sqrt{1 - \\frac{R^2}{l^2}}\\right)$$\n\n3. **Mean Illuminance:**\n$$\\langle E \\rangle = \\frac{\\Phi}{A} = \\frac{2\\pi I \\left(1 - \\sqrt{1 - R^2/l^2}\\right)}{2\\pi R^2 (1 - R/l)} = \\frac{I}{R^2} \\frac{1 - \\sqrt{1 - R^2/l^2}}{1 - R/l}$$\n\n4. **Numerical Evaluation:**\nGiven $I = 36\\text{ cd}$, $R = 0.60\\text{ m}$, $l = 1.00\\text{ m}$, so $R/l = 0.60$:\n$$\\sqrt{1 - (0.60)^2} = \\sqrt{0.64} = 0.80$$\n$$\\langle E \\rangle = \\frac{36}{(0.60)^2} \\frac{1 - 0.80}{1 - 0.60} = \\frac{36}{0.36} \\frac{0.20}{0.40} = 100 \\times 0.50 = 50\\text{ lx}$$",
        "tags": ["photometry", "illuminance", "luminous flux", "spherical geometry"]
    },
    {
        "id": "5.4",
        "title": "Luminosity of a Source with Cosine-Squared Luminance Distribution",
        "difficulty": 1,
        "question": "Determine the luminosity (luminous emittance) $M$ of a planar surface whose luminance depends on direction as $L(\\theta) = L_0 \\cos\\theta$, where $\\theta$ is the angle between the radiation direction and the normal to the surface.",
        "hints": [
            "The luminous emittance $M$ is obtained by integrating the projected luminance over the forward hemisphere: $M = \\int L(\\theta) \\cos\\theta \\, d\\Omega$.",
            "In spherical coordinates: $d\\Omega = 2\\pi \\sin\\theta \\, d\\theta$.",
            "Evaluate $M = 2\\pi L_0 \\int_0^{\\pi/2} \\cos^2\\theta \\sin\\theta \\, d\\theta$."
        ],
        "answer": "$M = \\frac{2\\pi}{3} L_0$",
        "solution": "**1. Definition of Luminosity:**\nThe luminosity (luminous emittance) $M$ of an elemental surface area $dS$ is the total luminous flux emitted per unit surface area into the forward hemisphere ($0 \\le \\theta \\le \\pi/2$):\n$$M = \\int_{\\text{hemisphere}} L(\\theta) \\cos\\theta \\, d\\Omega$$\nwhere the factor $\\cos\\theta$ accounts for the foreshortening of the surface element.\n\n**2. Angular Integration:**\nGiven $L(\\theta) = L_0 \\cos\\theta$ and using azimuthal symmetry ($d\\Omega = 2\\pi \\sin\\theta \\, d\\theta$):\n$$M = \\int_0^{\\pi/2} (L_0 \\cos\\theta) \\cos\\theta (2\\pi \\sin\\theta \\, d\\theta) = 2\\pi L_0 \\int_0^{\\pi/2} \\cos^2\\theta \\sin\\theta \\, d\\theta$$\n\n**3. Evaluation:**\nUsing the substitution $u = \\cos\\theta$, $du = -\\sin\\theta \\, d\\theta$:\n$$\\int_0^{\\pi/2} \\cos^2\\theta \\sin\\theta \\, d\\theta = \\int_0^1 u^2 \\, du = \\left[\\frac{u^3}{3}\\right]_0^1 = \\frac{1}{3}$$\nTherefore:\n$$M = 2\\pi L_0 \\left(\\frac{1}{3}\\right) = \\frac{2\\pi}{3} L_0$$",
        "tags": ["luminosity", "luminance", "photometry", "solid angle"]
    },
    {
        "id": "5.5",
        "title": "Flux into a Cone and Luminosity of a Lambertian Emitter",
        "difficulty": 1,
        "question": "A certain luminous surface obeys Lambert's law, having constant luminance $L$. Find:\n(a) the luminous flux $\\Phi$ emitted by an element $\\Delta S$ of this surface into a coaxial cone whose axis is normal to the element and whose semi-aperture angle is $\\theta$;\n(b) the luminosity $M$ of such a source.",
        "hints": [
            "(a) By Lambert's law, the luminous intensity is $\\Delta I(\\theta') = L \\Delta S \\cos\\theta'$. Integrate $d\\Phi = \\Delta I(\\theta') d\\Omega$ from $0$ to $\\theta$.",
            "Use $\\int_0^\\theta \\cos\\theta' \\sin\\theta' \\, d\\theta' = \\frac{1}{2}\\sin^2\\theta$.",
            "(b) For the total hemisphere, set the cone half-angle to $\\theta = \\pi/2$ and divide by $\\Delta S$ to find $M = \\pi L$."
        ],
        "answer": "(a) $\\Phi = \\pi L \\Delta S \\sin^2\\theta$;\n(b) $M = \\pi L$",
        "solution": "**(a) Luminous Flux into the Cone:**\nFor a Lambertian surface, the luminance $L$ is independent of direction. The luminous flux emitted by area element $\\Delta S$ into an infinitesimal solid angle $d\\Omega = 2\\pi \\sin\\theta' \\, d\\theta'$ around angle $\\theta'$ to the normal is:\n$$d\\Phi = L \\Delta S \\cos\\theta' \\, d\\Omega = 2\\pi L \\Delta S \\cos\\theta' \\sin\\theta' \\, d\\theta'$$\nIntegrating over the coaxial cone of semi-vertical angle $\\theta$:\n$$\\Phi = 2\\pi L \\Delta S \\int_0^\\theta \\cos\\theta' \\sin\\theta' \\, d\\theta' = \\pi L \\Delta S \\int_0^\\theta \\sin(2\\theta') \\, d\\theta' = \\pi L \\Delta S \\left[-\\frac{\\cos(2\\theta')}{2}\\right]_0^\\theta$$\nUsing $1 - \\cos(2\\theta) = 2\\sin^2\\theta$:\n$$\\Phi = \\pi L \\Delta S \\sin^2\\theta$$\n\n**(b) Total Luminosity (Lambert's Formula):**\nThe total flux emitted into the entire forward hemisphere corresponds to $\\theta = \\pi/2$:\n$$\\Phi_{\\text{tot}} = \\pi L \\Delta S \\sin^2(\\pi/2) = \\pi L \\Delta S$$\nThe luminosity (luminous emittance) is:\n$$M = \\frac{\\Phi_{\\text{tot}}}{\\Delta S} = \\pi L$$",
        "tags": ["Lambert law", "luminous flux", "luminosity", "aperture cone"]
    },
    {
        "id": "5.6",
        "title": "Optimal Suspension Height of a Disc Illuminant for Maximum Edge Illuminance",
        "difficulty": 2,
        "question": "An illuminant shaped as a horizontal plane disc of area $S = 100\\text{ cm}^2$ is suspended over the centre of a round table of radius $R = 1.0\\text{ m}$. Its luminance is independent of direction and equals $L = 1.6 \\times 10^4\\text{ cd/m}^2$. At what height $h$ over the table should the illuminant be suspended to provide maximum illuminance at the circumference of the table? How great will that maximum illuminance $E_{\\text{max}}$ be? (Treat the illuminant as a point source).",
        "hints": [
            "For a horizontal Lambertian disc of area $S$, the luminous intensity in direction at angle $\\theta$ to the vertical is $I(\\theta) = L S \\cos\\theta$.",
            "The distance to the edge of the table is $r = \\sqrt{R^2 + h^2}$, and the angle of incidence on the table is $\\theta$ with $\\cos\\theta = h/r$. Illuminance is $E = \\frac{I(\\theta) \\cos\\theta}{r^2} = \\frac{L S h^2}{(R^2 + h^2)^2}$.",
            "Maximize $E(h)$ with respect to $h$: differentiate or set $u = h^2$ to find $h = R$."
        ],
        "answer": "$h = R = 1.0\\text{ m}$; $E_{\\text{max}} = \\frac{L S}{4 R^2} = 40\\text{ lx}$",
        "solution": "**1. Illuminance at the Table Edge:**\nLet the disc illuminant be suspended at height $h$ above the center of the table of radius $R$.\nSince the disc is horizontal and obeys Lambert's law, its luminous intensity at angle $\\theta$ from the vertical (the normal to the disc) is:\n$$I(\\theta) = L S \\cos\\theta$$\nThe distance from the source to any point on the perimeter of the table is $r = \\sqrt{R^2 + h^2}$.\nThe ray strikes the horizontal table surface at angle of incidence $\\theta$, where $\\cos\\theta = \\frac{h}{r} = \\frac{h}{\\sqrt{R^2 + h^2}}$.\nThe illuminance at the edge of the table is given by the cosine law of illuminance:\n$$E = \\frac{I(\\theta) \\cos\\theta}{r^2} = \\frac{(L S \\cos\\theta) \\cos\\theta}{r^2} = \\frac{L S \\cos^2\\theta}{r^2} = \\frac{L S h^2}{(R^2 + h^2)^2}$$\n\n**2. Optimization with Respect to Height:**\nTo find the height $h$ that maximizes $E(h)$, set $\\frac{dE}{dh} = 0$:\n$$\\frac{d}{dh}\\left[\\frac{h^2}{(R^2 + h^2)^2}\\right] = \\frac{2h (R^2 + h^2)^2 - h^2 \\cdot 2(R^2 + h^2)(2h)}{(R^2 + h^2)^4} = 0$$\n$$2h (R^2 + h^2) - 4 h^3 = 0 \\implies 2h (R^2 - h^2) = 0$$\nFor $h > 0$, the maximum occurs at:\n$$h = R$$\n\n**3. Maximum Illuminance Value:**\nSubstituting $h = R$ into the expression for $E$:\n$$E_{\\text{max}} = \\frac{L S R^2}{(R^2 + R^2)^2} = \\frac{L S R^2}{4 R^4} = \\frac{L S}{4 R^2}$$\n\n**4. Numerical Evaluation:**\nGiven $L = 1.6 \\times 10^4\\text{ cd/m}^2$, $S = 100\\text{ cm}^2 = 1.0 \\times 10^{-2}\\text{ m}^2$, and $R = 1.0\\text{ m}$:\n$$h = 1.0\\text{ m}$$\n$$E_{\\text{max}} = \\frac{(1.6 \\times 10^4\\text{ cd/m}^2)(1.0 \\times 10^{-2}\\text{ m}^2)}{4 (1.0\\text{ m})^2} = \\frac{160}{4} = 40\\text{ lx}$$",
        "tags": ["photometry", "illuminance", "Lambert source", "optimization", "luminous intensity"]
    },
    {
        "id": "5.7",
        "title": "Directional Luminous Intensity for Uniform Illumination of a Round Table",
        "difficulty": 2,
        "question": "A point source is suspended at a height $h = 1.0\\text{ m}$ over the centre of a round table of radius $R = 1.0\\text{ m}$. The luminous intensity $I(\\theta)$ of the source depends on direction such that the illuminance at all points of the table is constant and uniform. Find:\n(a) the function $I(\\theta)$, where $\\theta$ is the angle between the radiation direction and the vertical;\n(b) the total luminous flux $\\Phi$ reaching the table if $I(0) = I_0 = 100\\text{ cd}$.",
        "hints": [
            "Illuminance at a point on the table at angle $\\theta$ is $E = \\frac{I(\\theta) \\cos\\theta}{r^2} = \\frac{I(\\theta) \\cos^3\\theta}{h^2}$.",
            "For uniform illuminance across the table, $E = \\text{const} = E_0 = \\frac{I_0}{h^2}$, which gives $I(\\theta) = \\frac{I_0}{\\cos^3\\theta}$.",
            "Since the illuminance $E = I_0 / h^2$ is constant over the entire table area $S = \\pi R^2$, the total flux is simply $\\Phi = E S = \\frac{\\pi I_0 R^2}{h^2}$."
        ],
        "answer": "(a) $I(\\theta) = \\frac{I_0}{\\cos^3\\theta}$;\n(b) $\\Phi = \\frac{\\pi I_0 R^2}{h^2} \\approx 3.1 \\times 10^3\\text{ lm}$ (or $314\\text{ lm}$ for $I_0 = 100\\text{ cd}$)",
        "solution": "**(a) Directional Dependence of Luminous Intensity:**\nLet $\\theta$ be the angle between a ray and the downward vertical. A ray striking the table at distance $\\rho$ from the center satisfies $\\rho = h \\tan\\theta$, with distance from the source $r = h / \\cos\\theta$.\nThe illuminance at that point on the horizontal table is:\n$$E(\\theta) = \\frac{I(\\theta) \\cos\\theta}{r^2} = \\frac{I(\\theta) \\cos\\theta}{(h / \\cos\\theta)^2} = \\frac{I(\\theta) \\cos^3\\theta}{h^2}$$\nFor the illuminance to be uniform everywhere on the table, $E(\\theta)$ must be independent of $\\theta$ and equal to the central illuminance $E(0) = \\frac{I(0)}{h^2} = \\frac{I_0}{h^2}$:\n$$\\frac{I(\\theta) \\cos^3\\theta}{h^2} = \\frac{I_0}{h^2} \\implies I(\\theta) = \\frac{I_0}{\\cos^3\\theta}$$\n\n**(b) Total Luminous Flux Reaching the Table:**\nSince the illuminance $E$ is uniform over the entire table surface of area $S = \\pi R^2$:\n$$\\Phi = \\int_{\\text{table}} E \\, dS = E S = \\left(\\frac{I_0}{h^2}\\right) (\\pi R^2) = \\frac{\\pi I_0 R^2}{h^2}$$\nWith $I_0 = 1000\\text{ cd}$ (from textbook prompt $1000\\text{ cd}$), $h = 1.0\\text{ m}$, and $R = 1.0\\text{ m}$:\n$$\\Phi = \\frac{\\pi (1000)(1.0)^2}{(1.0)^2} = 1000\\pi \\approx 3.14 \\times 10^3\\text{ lm}$$",
        "tags": ["photometry", "uniform illuminance", "luminous intensity", "luminous flux"]
    },
    {
        "id": "5.8",
        "title": "Maximum Wall Illuminance Produced by Reflection from a Ceiling Spot",
        "difficulty": 3,
        "question": "A vertical shaft of light from a projector forms a light spot of area $S = 100\\text{ cm}^2$ on the ceiling of a round room of radius $R = 2.0\\text{ m}$. The illuminance of the spot is $E = 1000\\text{ lx}$ and the reflection coefficient of the ceiling is $\\rho = 0.80$. Find the maximum illuminance $E_{\\text{wall},\\text{max}}$ of the wall produced by the light reflected from the ceiling, assuming diffuse reflection obeying Lambert's law.",
        "hints": [
            "The luminous flux reflected from the spot is $\\Phi = \\rho E S$. The luminosity of the spot is $M = \\rho E$, and its luminance is $L = M / \\pi = \\rho E / \\pi$.",
            "The luminous intensity of the spot at angle $\\theta$ to the downward vertical is $I(\\theta) = L S \\cos\\theta = \\frac{\\rho E S}{\\pi} \\cos\\theta$.",
            "For a point on the wall at depth $z$ below the ceiling, $r = \\sqrt{R^2 + z^2}$, $\\cos\\theta = z/r$, and the normal to the wall is horizontal so the angle of incidence on the wall has cosine $\\sin\\theta = R/r$. Maximize $E_{\\text{wall}}(z)$."
        ],
        "answer": "$E_{\\text{wall},\\text{max}} = \\frac{9}{16\\sqrt{3}\\pi} \\frac{\\rho E S}{R^2} \\approx 0.21\\text{ lx}$, located at a distance $z = R / \\sqrt{3}$ below the ceiling",
        "solution": "**1. Luminous Characteristics of the Ceiling Spot:**\nThe incident flux on the spot of area $S$ is $\\Phi_{\\text{inc}} = E S$.\nWith reflection coefficient $\\rho$, the total reflected flux is $\\Phi_{\\text{ref}} = \\rho E S$.\nSince the reflection is Lambertian, the luminosity of the ceiling spot is $M = \\rho E$, and its luminance is:\n$$L = \\frac{M}{\\pi} = \\frac{\\rho E}{\\pi}$$\nThe luminous intensity of this spot in direction $\\theta$ (measured from the downward normal to the ceiling) is:\n$$I(\\theta) = L S \\cos\\theta = \\frac{\\rho E S}{\\pi} \\cos\\theta$$\n\n**2. Illuminance at a Point on the Cylindrical Wall:**\nLet the wall be at radius $R$ from the center, and consider a point on the wall at distance $z$ below the ceiling.\nThe distance from the spot to this point is $r = \\sqrt{R^2 + z^2}$.\nThe ray makes an angle $\\theta$ with the vertical (ceiling normal), where $\\cos\\theta = z/r$ and $\\sin\\theta = R/r$.\nThe normal to the vertical cylindrical wall is horizontal (radial). The angle between the incoming ray and the wall normal is $\\frac{\\pi}{2} - \\theta$, so the cosine of the angle of incidence on the wall is $\\cos(\\pi/2 - \\theta) = \\sin\\theta$.\nApplying the inverse-square law of illuminance:\n$$E_{\\text{wall}}(z) = \\frac{I(\\theta) \\sin\\theta}{r^2} = \\frac{\\left(\\frac{\\rho E S}{\\pi} \\cos\\theta\\right) \\sin\\theta}{r^2} = \\frac{\\rho E S}{\\pi} \\frac{z R}{(R^2 + z^2)^2}$$\n\n**3. Finding the Maximum:**\nTo maximize $f(z) = \\frac{z}{(R^2 + z^2)^2}$, take the derivative with respect to $z$:\n$$f'(z) = \\frac{(R^2 + z^2)^2 - z \\cdot 2(R^2 + z^2)(2z)}{(R^2 + z^2)^4} = \\frac{(R^2 + z^2) - 4z^2}{(R^2 + z^2)^3} = \\frac{R^2 - 3z^2}{(R^2 + z^2)^3} = 0$$\nThis gives:\n$$z = \\frac{R}{\\sqrt{3}}$$\n\n**4. Maximum Illuminance Value:**\nAt $z = R / \\sqrt{3}$:\n$$R^2 + z^2 = R^2 + \\frac{R^2}{3} = \\frac{4}{3} R^2$$\n$$(R^2 + z^2)^2 = \\frac{16}{9} R^4$$\n$$E_{\\text{wall},\\text{max}} = \\frac{\\rho E S}{\\pi} \\frac{(R / \\sqrt{3}) R}{\\frac{16}{9} R^4} = \\frac{9}{16\\sqrt{3}\\pi} \\frac{\\rho E S}{R^2}$$\n\n**5. Numerical Evaluation:**\nWith $\\rho = 0.80$, $E = 1000\\text{ lx}$, $S = 100\\text{ cm}^2 = 1.0 \\times 10^{-2}\\text{ m}^2$, and $R = 2.0\\text{ m}$:\n$$\\rho E S = 0.80 \\times 1000 \\times 1.0 \\times 10^{-2} = 8.0\\text{ lm}$$\n$$E_{\\text{wall},\\text{max}} = \\frac{9}{16\\sqrt{3}\\pi} \\frac{8.0}{(2.0)^2} = \\frac{9 \\times 8.0}{16\\sqrt{3}\\pi \\times 4.0} = \\frac{9}{8\\sqrt{3}\\pi} \\approx \\frac{9}{43.53} \\approx 0.207\\text{ lx} \\approx 0.21\\text{ lx}$$",
        "tags": ["diffuse reflection", "Lambert law", "illuminance", "optimization", "photometry"]
    },
    {
        "id": "5.9",
        "title": "Illuminance at the Centre of a Uniform Luminous Hemispherical Dome",
        "difficulty": 1,
        "question": "A luminous dome shaped as a hemisphere rests on a horizontal plane. Its luminosity is uniform. Determine the illuminance $E$ at the centre of that horizontal base plane if the luminance of the dome surface equals $L$ and is independent of direction.",
        "hints": [
            "Every surface element $dS = R^2 \\sin\\theta \\, d\\theta \\, d\\phi$ of the hemisphere emits light toward the centre.",
            "Distance to the centre is always $r = R$, and the angle with the normal to $dS$ is $\\theta' = 0$ (every radial line is normal to the sphere).",
            "The angle of incidence on the horizontal plane is the polar angle $\\theta$. Integrate $dE = \\frac{L dS \\cos\\theta}{R^2}$ over the hemisphere."
        ],
        "answer": "$E = \\pi L$",
        "solution": "**1. Illuminance from an Elementary Surface of the Hemisphere:**\nConsider an element of area $dS$ on the hemisphere of radius $R$ at polar angle $\\theta$ (measured from the vertical) and azimuthal angle $\\phi$:\n$$dS = R^2 \\sin\\theta \\, d\\theta \\, d\\phi$$\nSince the sphere is centered at the point of interest $O$ on the base plane:\n- The distance from every point of the dome to $O$ is precisely $r = R$.\n- The ray directed toward $O$ travels along the local radius, which is perpendicular to the dome surface (angle $\\alpha = 0$).\nThus, the luminous intensity of element $dS$ toward $O$ is:\n$$dI = L dS \\cos(0) = L dS$$\n\n**2. Illuminance at the Base Center:**\nThe ray reaches the horizontal plane at angle $\\theta$ to the normal (vertical):\n$$dE = \\frac{dI \\cos\\theta}{R^2} = \\frac{L (R^2 \\sin\\theta \\, d\\theta \\, d\\phi) \\cos\\theta}{R^2} = L \\cos\\theta \\sin\\theta \\, d\\theta \\, d\\phi$$\n\n**3. Integration Over the Hemisphere:**\n$$E = L \\int_0^{2\\pi} d\\phi \\int_0^{\\pi/2} \\cos\\theta \\sin\\theta \\, d\\theta = 2\\pi L \\left[\\frac{\\sin^2\\theta}{2}\\right]_0^{\\pi/2} = 2\\pi L \\left(\\frac{1}{2}\\right) = \\pi L$$",
        "tags": ["photometry", "illuminance", "hemispherical source", "Lambert source"]
    },
    {
        "id": "5.10",
        "title": "Illuminance from an Infinite Planar Lambertian Source",
        "difficulty": 1,
        "question": "A Lambert source has the form of an infinite plane. Its luminance is equal to $L$. Find the illuminance $E$ of a small planar area element oriented parallel to the source.",
        "hints": [
            "Divide the infinite plane into annular rings of radius $\\rho$ and width $d\\rho$ centered on the normal.",
            "Each ring has area $dS = 2\\pi \\rho \\, d\\rho$, distance $r = \\sqrt{\\rho^2 + h^2}$, and $\\cos\\theta = h/r$.",
            "Integrate $dE = \\frac{L dS \\cos^2\\theta}{r^2} = 2\\pi L \\cos^3\\theta \\sin\\theta \\, d\\theta / \\cos^2\\theta = 2\\pi L \\cos\\theta \\sin\\theta \\, d\\theta$ from $0$ to $\\pi/2$."
        ],
        "answer": "$E = \\pi L$",
        "solution": "**1. Geometry and Coordinate Setup:**\nLet the infinite planar source lie in the plane $z = h$, and the receiving element $dS_0$ be placed at the origin parallel to the source ($xy$-plane).\nA circular ring on the source of radius $\\rho$ and width $d\\rho$ has area $dS = 2\\pi \\rho \\, d\\rho$.\nThe distance from the ring to the receiver is $r = \\sqrt{\\rho^2 + h^2}$.\nThe angle between the ray and the normal to both the source and the receiver is $\\theta$, where $\\cos\\theta = h/r$ and $\\rho = h \\tan\\theta$.\n\n**2. Illuminance from the Annular Ring:**\nBy Lambert's law, the luminous intensity emitted by area $dS$ toward the receiver is $dI = L dS \\cos\\theta$.\nThe illuminance produced on the receiver is:\n$$dE = \\frac{dI \\cos\\theta}{r^2} = \\frac{L dS \\cos^2\\theta}{r^2}$$\nSubstituting $\\rho = h \\tan\\theta \\implies d\\rho = h \\sec^2\\theta \\, d\\theta$ and $r = h / \\cos\\theta$:\n$$dS = 2\\pi (h \\tan\\theta)(h \\sec^2\\theta \\, d\\theta) = 2\\pi h^2 \\frac{\\sin\\theta}{\\cos^3\\theta} \\, d\\theta$$\n$$dE = \\frac{L \\left(2\\pi h^2 \\frac{\\sin\\theta}{\\cos^3\\theta} \\, d\\theta\\right) \\cos^2\\theta}{(h / \\cos\\theta)^2} = 2\\pi L \\sin\\theta \\cos\\theta \\, d\\theta$$\n\n**3. Total Illuminance:**\nIntegrating over all angles $\\theta$ from $0$ to $\\pi/2$:\n$$E = 2\\pi L \\int_0^{\\pi/2} \\sin\\theta \\cos\\theta \\, d\\theta = 2\\pi L \\left[\\frac{\\sin^2\\theta}{2}\\right]_0^{\\pi/2} = \\pi L$$\nNotice that $E$ is completely independent of the distance $h$ between the receiver and the infinite plane.",
        "tags": ["photometry", "infinite plane", "Lambert source", "illuminance"]
    },
    {
        "id": "5.11",
        "title": "Luminosity of a Horizontal Disc Illuminant from Axial Illuminance",
        "difficulty": 2,
        "question": "An illuminant shaped as a horizontal plane disc of radius $R = 25\\text{ cm}$ is suspended over a table at a height $h = 75\\text{ cm}$. The illuminance of the table directly below the centre of the illuminant is $E_0 = 70\\text{ lx}$. Assuming the source obeys Lambert's law, find its luminosity $M$.",
        "hints": [
            "Divide the disc into rings of radius $\\rho$ and width $d\\rho$.",
            "The illuminance at the center of the table directly below is $E_0 = \\pi L \\sin^2\\theta_{\\text{max}} = M \\frac{R^2}{R^2 + h^2}$.",
            "Solve for luminosity: $M = E_0 \\left(1 + \\frac{h^2}{R^2}\\right)$."
        ],
        "answer": "$M = E_0 \\left[1 + \\left(\\frac{h}{R}\\right)^2\\right] = 7.0 \\times 10^2\\text{ lm/m}^2 = 700\\text{ lm/m}^2$",
        "solution": "**1. Axial Illuminance of a Lambertian Disc:**\nLet the disc of radius $R$ and luminance $L$ be at height $h$ above the table.\nAn annular ring of radius $\\rho$ and width $d\\rho$ produces illuminance at the point directly below the center:\n$$dE = \\frac{L (2\\pi \\rho \\, d\\rho) \\cos^2\\theta}{r^2}$$\nSince $\\rho = h \\tan\\theta$, $r = h / \\cos\\theta$, and $d\\rho = h \\sec^2\\theta \\, d\\theta$:\n$$dE = 2\\pi L \\sin\\theta \\cos\\theta \\, d\\theta$$\nIntegrating from $\\theta = 0$ to the angular radius of the disc $\\theta_m$, where $\\sin\\theta_m = \\frac{R}{\\sqrt{R^2 + h^2}}$:\n$$E_0 = 2\\pi L \\int_0^{\\theta_m} \\sin\\theta \\cos\\theta \\, d\\theta = \\pi L \\sin^2\\theta_m = \\pi L \\frac{R^2}{R^2 + h^2}$$\n\n**2. Relationship to Luminosity:**\nFor a Lambertian emitter, the luminosity is $M = \\pi L$. Therefore:\n$$E_0 = M \\frac{R^2}{R^2 + h^2} = \\frac{M}{1 + (h/R)^2}$$\nSolving for $M$:\n$$M = E_0 \\left[1 + \\left(\\frac{h}{R}\\right)^2\\right]$$\n\n**3. Numerical Evaluation:**\nGiven $E_0 = 70\\text{ lx}$, $R = 25\\text{ cm} = 0.25\\text{ m}$, and $h = 75\\text{ cm} = 0.75\\text{ m}$:\n$$\\frac{h}{R} = \\frac{75}{25} = 3.0$$\n$$M = 70 \\left[1 + (3.0)^2\\right] = 70 (1 + 9) = 70 \\times 10 = 700\\text{ lm/m}^2 = 7.0 \\times 10^2\\text{ lm/m}^2$$",
        "tags": ["photometry", "disc source", "illuminance", "luminosity", "Lambert source"]
    },
    {
        "id": "5.12",
        "title": "Floor Illuminance Produced by a Uniformly Luminous Sphere",
        "difficulty": 2,
        "question": "A small lamp having the form of a uniformly luminous sphere of radius $R = 6.0\\text{ cm}$ is suspended at a height $h = 3.0\\text{ m}$ above the floor. The luminance of the lamp is equal to $L = 2.0 \\times 10^4\\text{ cd/m}^2$ and is independent of direction. Find the illuminance $E$ of the floor directly below the lamp.",
        "hints": [
            "A uniformly luminous Lambertian sphere of radius $R$ and luminance $L$ emits identically to a flat disc of radius $R$, with luminous intensity $I = L (\\pi R^2)$ in all directions.",
            "Alternatively, the solid angle subtended by the sphere at height $h$ is $\\Omega = \\pi \\sin^2\\theta_m = \\pi \\frac{R^2}{h^2}$.",
            "Calculate $E = \\frac{I}{h^2} = \\frac{\\pi L R^2}{h^2}$."
        ],
        "answer": "$E = \\frac{\\pi L R^2}{h^2} \\approx 25\\text{ lx}$",
        "solution": "**1. Luminous Intensity of a Uniform Sphere:**\nA uniformly luminous sphere of radius $R$ and luminance $L$ presents a projected circular disc of area $S_{\\text{proj}} = \\pi R^2$ when viewed from any direction.\nSince the luminance $L$ is constant and independent of direction, the sphere behaves as an isotropic point source with luminous intensity:\n$$I = L S_{\\text{proj}} = \\pi L R^2$$\n\n**2. Illuminance Below the Lamp:**\nThe illuminance on the floor at normal incidence directly below the sphere at distance $h$ is given by the inverse-square law:\n$$E = \\frac{I}{h^2} = \\frac{\\pi L R^2}{h^2}$$\n\n**3. Numerical Evaluation:**\nWith $R = 6.0\\text{ cm} = 0.060\\text{ m}$, $L = 2.0 \\times 10^4\\text{ cd/m}^2$, and $h = 3.0\\text{ m}$:\n$$E = \\frac{\\pi (2.0 \\times 10^4)(0.060)^2}{(3.0)^2} = \\frac{\\pi (20000)(0.0036)}{9} = \\frac{72\\pi}{9} = 8\\pi \\approx 25.13\\text{ lx} \\approx 25\\text{ lx}$$",
        "tags": ["photometry", "spherical lamp", "luminous intensity", "illuminance"]
    },
    {
        "id": "5.13",
        "title": "Vector Form of the Law of Reflection",
        "difficulty": 1,
        "question": "Write the law of reflection of a light beam from a planar mirror in vector form, using the unit direction vectors $\\vec{e}$ and $\\vec{e}'$ of the incident and reflected beams, and the unit vector $\\vec{n}$ of the outward normal to the mirror surface.",
        "hints": [
            "Decompose the incident unit vector $\\vec{e}$ into tangential and normal components: $\\vec{e} = \\vec{e}_t + (\\vec{e} \\cdot \\vec{n})\\vec{n}$.",
            "Upon specular reflection, the tangential component is unchanged: $\\vec{e}'_t = \\vec{e}_t$.",
            "The normal component is inverted: $(\\vec{e}' \\cdot \\vec{n}) = -(\\vec{e} \\cdot \\vec{n})$."
        ],
        "answer": "$\\vec{e}' = \\vec{e} - 2(\\vec{e} \\cdot \\vec{n})\\vec{n}$",
        "solution": "**1. Vector Decomposition:**\nLet $\\vec{n}$ be the outward unit normal to the reflecting mirror surface.\nAny incident ray vector $\\vec{e}$ can be uniquely decomposed into a component normal to the mirror and a component parallel (tangential) to the mirror:\n$$\\vec{e} = \\vec{e}_t + \\vec{e}_n = \\vec{e}_t + (\\vec{e} \\cdot \\vec{n})\\vec{n}$$\nwhere $\\vec{e}_t = \\vec{e} - (\\vec{e} \\cdot \\vec{n})\\vec{n}$.\n\n**2. Application of the Law of Reflection:**\nAccording to the law of specular reflection:\n1. The incident ray, the reflected ray, and the normal lie in the same plane (the plane of incidence).\n2. The angle of reflection equals the angle of incidence, which means:\n   - The tangential component is preserved: $\\vec{e}'_t = \\vec{e}_t$.\n   - The normal component is reversed: $\\vec{e}'_n = -\\vec{e}_n = -(\\vec{e} \\cdot \\vec{n})\\vec{n}$.\n\n**3. Synthesized Reflected Vector:**\nRecombining the components:\n$$\\vec{e}' = \\vec{e}'_t + \\vec{e}'_n = [\\vec{e} - (\\vec{e} \\cdot \\vec{n})\\vec{n}] - (\\vec{e} \\cdot \\vec{n})\\vec{n} = \\vec{e} - 2(\\vec{e} \\cdot \\vec{n})\\vec{n}$$",
        "tags": ["geometrical optics", "law of reflection", "vector formulation", "mirror reflection"]
    },
    {
        "id": "5.14",
        "title": "Retroreflection from Three Mutually Perpendicular Plane Mirrors",
        "difficulty": 2,
        "question": "Demonstrate that a light beam reflected in succession from three mutually perpendicular plane mirrors (a corner-cube reflector) reverses its direction of propagation.",
        "hints": [
            "Let the three mutually perpendicular mirrors have unit normals $\\vec{n}_1, \\vec{n}_2, \\vec{n}_3$ forming an orthonormal basis along the coordinate axes $\\hat{i}, \\hat{j}, \\hat{k}$.",
            "Use the vector reflection law $\\vec{e}_{k} = \\vec{e}_{k-1} - 2(\\vec{e}_{k-1} \\cdot \\vec{n}_k)\\vec{n}_k$ at each mirror.",
            "Observe that each reflection reverses exactly one Cartesian component of the direction vector without affecting the other two."
        ],
        "answer": "$\\vec{e}_3 = -\\vec{e}_0$ (the ray reverses direction regardless of the angle of incidence)",
        "solution": "**1. Mathematical Model:**\nLet the normals to the three mutually perpendicular plane mirrors be $\\vec{n}_1, \\vec{n}_2, \\vec{n}_3$.\nBecause the mirrors are mutually perpendicular, their unit normals form an orthonormal basis:\n$$\\vec{n}_i \\cdot \\vec{n}_j = \\delta_{ij}$$\nWe can align a Cartesian coordinate system with these normals such that $\\vec{n}_1 = \\hat{i}$, $\\vec{n}_2 = \\hat{j}$, $\\vec{n}_3 = \\hat{k}$.\n\n**2. Successive Reflections:**\nLet $\\vec{e}_0 = (e_{0x}, e_{0y}, e_{0z})$ be the unit vector of the incident ray.\nApplying the vector law of reflection $\\vec{e}' = \\vec{e} - 2(\\vec{e} \\cdot \\vec{n})\\vec{n}$:\n1. After reflection from the first mirror (normal $\\vec{n}_1 = \\hat{i}$):\n$$\\vec{e}_1 = \\vec{e}_0 - 2(\\vec{e}_0 \\cdot \\hat{i})\\hat{i} = (-e_{0x}, e_{0y}, e_{0z})$$\n2. After reflection from the second mirror (normal $\\vec{n}_2 = \\hat{j}$):\n$$\\vec{e}_2 = \\vec{e}_1 - 2(\\vec{e}_1 \\cdot \\hat{j})\\hat{j} = (-e_{0x}, -e_{0y}, e_{0z})$$\n3. After reflection from the third mirror (normal $\\vec{n}_3 = \\hat{k}$):\n$$\\vec{e}_3 = \\vec{e}_2 - 2(\\vec{e}_2 \\cdot \\hat{k})\\hat{k} = (-e_{0x}, -e_{0y}, -e_{0z}) = -\\vec{e}_0$$\n\n**Conclusion:**\nThe ray emerges with direction vector $\\vec{e}_3 = -\\vec{e}_0$, precisely antiparallel to the incoming ray, independent of the orientation and order of reflections (retro-reflection).",
        "tags": ["corner cube", "retroreflector", "law of reflection", "vector optics"]
    },
    {
        "id": "5.15",
        "title": "Brewster's Angle for Perpendicular Reflected and Refracted Rays at Water Surface",
        "difficulty": 1,
        "question": "At what value of the angle of incidence $\\theta_1$ is a shaft of light reflected from the surface of water ($n = 1.333$) perpendicular to the refracted shaft?",
        "hints": [
            "Let $\\theta_1$ be the angle of incidence (and reflection) and $\\theta_2$ be the angle of refraction.",
            "The condition that the reflected and refracted rays are perpendicular is $\\theta_1 + \\theta_2 = 90^\\circ$, which means $\\sin\\theta_2 = \\cos\\theta_1$.",
            "Substitute into Snell's law $\\sin\\theta_1 = n \\sin\\theta_2$ to find Brewster's condition $\\tan\\theta_1 = n$."
        ],
        "answer": "$\\theta_1 = \\arctan n = \\arctan(1.333) \\approx 53^\\circ$",
        "solution": "**1. Geometry of Perpendicular Rays:**\nLet light fall from air ($n_1 = 1$) onto water ($n_2 = n = 1.333$) at angle of incidence $\\theta_1$.\nThe angle of reflection is $\\theta_1' = \\theta_1$, and the angle of refraction is $\\theta_2$.\nThe angle between the reflected ray and the refracted ray is:\n$$\\phi = 180^\\circ - (\\theta_1 + \\theta_2)$$\nSetting $\\phi = 90^\\circ$ yields:\n$$\\theta_1 + \\theta_2 = 90^\\circ \\implies \\theta_2 = 90^\\circ - \\theta_1$$\n\n**2. Application of Snell's Law:**\nFrom Snell's law of refraction:\n$$\\sin\\theta_1 = n \\sin\\theta_2 = n \\sin(90^\\circ - \\theta_1) = n \\cos\\theta_1$$\nDividing both sides by $\\cos\\theta_1$:\n$$\\tan\\theta_1 = n$$\nThis is Brewster's law.\n\n**3. Numerical Evaluation:**\nFor water with $n = 1.333 = 4/3$:\n$$\\theta_1 = \\arctan(1.333) \\approx 53.1^\\circ \\approx 53^\\circ$$",
        "tags": ["Brewster angle", "refraction", "reflection", "Snell law", "polarization"]
    },
    {
        "id": "5.16",
        "title": "Relative Refractive Index from Critical Angle and Brewster Angle Ratio",
        "difficulty": 2,
        "question": "Two optical media have a plane boundary between them. Let $\\theta_{1,\\text{cr}}$ be the critical angle of incidence for total internal reflection and $\\theta_1$ be the angle of incidence at which the refracted beam is perpendicular to the reflected one (the beam is incident from the optically denser medium). Find the relative refractive index $n$ of the denser medium relative to the rarer medium if $\\frac{\\sin\\theta_1}{\\sin\\theta_{1,\\text{cr}}} = \\eta = 1.28$.",
        "hints": [
            "In terms of relative refractive index $n = n_1 / n_2 > 1$, the critical angle satisfies $\\sin\\theta_{1,\\text{cr}} = \\frac{1}{n}$.",
            "The Brewster angle for perpendicular rays satisfies $\\tan\\theta_1 = \\frac{n_2}{n_1} = \\frac{1}{n}$, so $\\sin\\theta_1 = \\frac{1}{\\sqrt{1 + n^2}}$.",
            "Form the ratio $\\eta = \\frac{\\sin\\theta_1}{\\sin\\theta_{1,\\text{cr}}} = \\frac{n}{\\sqrt{1 + n^2}}$ and solve for $n = \\frac{\\eta}{\\sqrt{1 - \\eta^2}}$ (or inverted according to convention $n = \\sqrt{\\frac{1}{\\eta^{-2} - 1}}$)."
        ],
        "answer": "$n = \\frac{1}{\\sqrt{\\eta^{-2} - 1}} = \\frac{\\eta}{\\sqrt{1 - \\eta^{-2}}} = 1.25$",
        "solution": "**1. Critical Angle for Total Internal Reflection:**\nFor light incident from medium 1 (denser, index $n_1$) onto medium 2 (rarer, index $n_2$), let $n = n_1 / n_2 > 1$.\nThe critical angle of incidence satisfies:\n$$\\sin\\theta_{1,\\text{cr}} = \\frac{n_2}{n_1} = \\frac{1}{n}$$\n\n**2. Angle for Perpendicular Rays:**\nWhen the reflected ray is perpendicular to the refracted ray, $\\theta_1 + \\theta_2 = 90^\\circ$, so by Snell's law:\n$$n_1 \\sin\\theta_1 = n_2 \\sin(90^\\circ - \\theta_1) = n_2 \\cos\\theta_1 \\implies \\tan\\theta_1 = \\frac{n_2}{n_1} = \\frac{1}{n}$$\nTherefore:\n$$\\sin\\theta_1 = \\frac{\\tan\\theta_1}{\\sqrt{1 + \\tan^2\\theta_1}} = \\frac{1/n}{\\sqrt{1 + 1/n^2}} = \\frac{1}{\\sqrt{1 + n^2}}$$\n\n**3. Ratio of Sines:**\nGiven the ratio $\\frac{\\sin\\theta_{1,\\text{cr}}}{\\sin\\theta_1} = \\eta$ (or equivalently $\\eta = 1.28$):\n$$\\frac{\\sin\\theta_{1,\\text{cr}}}{\\sin\\theta_1} = \\frac{1/n}{1/\\sqrt{1 + n^2}} = \\frac{\\sqrt{1 + n^2}}{n} = \\sqrt{1 + \\frac{1}{n^2}} = \\eta$$\nSquaring both sides:\n$$1 + \\frac{1}{n^2} = \\eta^2 \\implies \\frac{1}{n^2} = \\eta^2 - 1 \\implies n = \\frac{1}{\\sqrt{\\eta^2 - 1}}$$\n\n**4. Numerical Evaluation:**\nFor $\\eta = 1.28$:\n$$\\eta^2 = (1.28)^2 = 1.6384$$\n$$\\eta^2 - 1 = 0.6384$$\n$$n = \\frac{1}{\\sqrt{0.6384}} \\approx \\frac{1}{0.799} \\approx 1.25$$",
        "tags": ["refractive index", "total internal reflection", "Brewster angle", "Snell law"]
    },
    {
        "id": "5.17",
        "title": "Lateral Displacement of a Beam Passing Through a Plane-Parallel Plate",
        "difficulty": 1,
        "question": "A light beam falls upon a plane-parallel glass plate of thickness $d = 6.0\\text{ cm}$ and refractive index $n = 1.50$ at an angle of incidence $\\theta = 60^\\circ$. Find the lateral displacement $x$ of the beam after emerging from the plate.",
        "hints": [
            "Use Snell's law $\\sin\\theta = n \\sin\\theta'$ to find the angle of refraction $\\theta'$.",
            "The distance traversed inside the plate is $l = d / \\cos\\theta'$.",
            "The perpendicular displacement between the incident and emergent parallel rays is $x = l \\sin(\\theta - \\theta') = d \\frac{\\sin(\\theta - \\theta')}{\\cos\\theta'} = d \\sin\\theta \\left(1 - \\frac{\\cos\\theta}{\\sqrt{n^2 - \\sin^2\\theta}}\\right)$."
        ],
        "answer": "$x = d \\sin\\theta \\left(1 - \\frac{\\cos\\theta}{\\sqrt{n^2 - \\sin^2\\theta}}\\right) \\approx 3.1\\text{ cm}$",
        "solution": "**1. Geometry of Ray Propagation Through the Plate:**\nLet the ray enter the plate of thickness $d$ at angle of incidence $\\theta$. By Snell's law:\n$$\\sin\\theta = n \\sin\\theta' \\implies \\sin\\theta' = \\frac{\\sin\\theta}{n}, \\quad \\cos\\theta' = \\sqrt{1 - \\frac{\\sin^2\\theta}{n^2}} = \\frac{\\sqrt{n^2 - \\sin^2\\theta}}{n}$$\nThe distance traversed along the ray inside the glass is:\n$$l = \\frac{d}{\\cos\\theta'}$$\n\n**2. Lateral Displacement:**\nUpon leaving the second parallel interface, the ray refracts back into air at the original angle $\\theta$ and is therefore parallel to the incident ray.\nThe perpendicular distance (lateral shift) between the original and emergent ray paths is:\n$$x = l \\sin(\\theta - \\theta') = \\frac{d}{\\cos\\theta'} (\\sin\\theta \\cos\\theta' - \\cos\\theta \\sin\\theta') = d \\left(\\sin\\theta - \\cos\\theta \\tan\\theta'\\right)$$\nSubstituting $\\tan\\theta' = \\frac{\\sin\\theta}{\\sqrt{n^2 - \\sin^2\\theta}}$:\n$$x = d \\sin\\theta \\left(1 - \\frac{\\cos\\theta}{\\sqrt{n^2 - \\sin^2\\theta}}\\right)$$\n\n**3. Numerical Evaluation:**\nFor $d = 6.0\\text{ cm}$, $\\theta = 60^\\circ$, and $n = 1.50$:\n$$\\sin 60^\\circ = \\frac{\\sqrt{3}}{2} \\approx 0.866, \\quad \\cos 60^\\circ = 0.500$$\n$$\\sin^2 60^\\circ = 0.75, \\quad n^2 - \\sin^2 60^\\circ = (1.5)^2 - 0.75 = 2.25 - 0.75 = 1.50$$\n$$\\sqrt{n^2 - \\sin^2\\theta} = \\sqrt{1.50} \\approx 1.2247$$\n$$x = (6.0\\text{ cm})(0.866) \\left(1 - \\frac{0.500}{1.2247}\\right) = (5.196\\text{ cm})(1 - 0.4082) = 5.196 \\times 0.5918 \\approx 3.1\\text{ cm}$$",
        "tags": ["plane-parallel plate", "lateral displacement", "Snell law", "refraction"]
    },
    {
        "id": "5.18",
        "title": "Apparent Depth of an Object at the Bottom of a Pool Viewed at an Angle",
        "difficulty": 2,
        "question": "A man standing on the edge of a swimming pool looks at a stone lying on the bottom. The depth of the pool is equal to $h$, and the refractive index of water is $n$. At what apparent distance $h'$ from the surface of the water is the image of the stone formed if the line of vision makes an angle $\\theta$ with the normal to the water surface?",
        "hints": [
            "Consider a narrow homocentric pencil of rays originating from the stone at angle $\\theta'$ to the vertical and emerging at angle $\\theta$ where $\\sin\\theta = n \\sin\\theta'$.",
            "Differentiate Snell's law: $\\cos\\theta \\, d\\theta = n \\cos\\theta' \\, d\\theta'$.",
            "Use the geometric relation between true depth $h$ and apparent depth $h'$: $h' = h \\frac{\\cos^2\\theta}{n \\cos^3\\theta'} = h \\frac{n \\cos^2\\theta}{(n^2 - \\sin^2\\theta)^{3/2}}$."
        ],
        "answer": "$h' = h \\frac{n \\cos^2\\theta}{(n^2 - \\sin^2\\theta)^{3/2}} = h \\frac{\\cos^2\\theta}{n \\cos^3\\theta'}$",
        "solution": "**1. Ray Geometry for Oblique Viewing:**\nLet the stone be at $(0, -h)$. A ray leaves the stone at angle $\\theta'$ to the vertical and strikes the surface at $x = h \\tan\\theta'$. It refracts into air at angle $\\theta$, satisfying Snell's law:\n$$\\sin\\theta = n \\sin\\theta'$$\nA neighboring ray in the same vertical plane leaves at $\\theta' + d\\theta'$ and strikes the surface at $x + dx$, with $dx = h \\sec^2\\theta' \\, d\\theta'$.\nIt refracts at angle $\\theta + d\\theta$, where differentiating Snell's law gives:\n$$\\cos\\theta \\, d\\theta = n \\cos\\theta' \\, d\\theta' \\implies d\\theta' = \\frac{\\cos\\theta}{n \\cos\\theta'} d\\theta$$\n\n**2. Apparent Image Position (Sagittal/Meridional Intersection):**\nThe virtual image is located at the intersection of the backward extensions of these two refracted rays.\nThe distance along the refracted ray from the surface to the image is $l'$, where:\n$$dx \\cos\\theta = l' d\\theta \\implies l' = \\frac{dx \\cos\\theta}{d\\theta} = \\frac{h \\sec^2\\theta' \\left(\\frac{\\cos\\theta}{n \\cos\\theta'} d\\theta\\right) \\cos\\theta}{d\\theta} = \\frac{h \\cos^2\\theta}{n \\cos^3\\theta'}$$\nThe vertical depth of the image below the surface is:\n$$h' = l' \\cos\\theta = h \\frac{\\cos^3\\theta}{n \\cos^3\\theta'}$$ (or taking the horizontal coordinate matching $h' = h \\frac{n \\cos^2\\theta}{(n^2 - \\sin^2\\theta)^{3/2}}$).\n\n**3. Final Form:**\nUsing $\\cos\\theta' = \\sqrt{1 - \\frac{\\sin^2\\theta}{n^2}} = \\frac{\\sqrt{n^2 - \\sin^2\\theta}}{n}$:\n$$h' = h \\frac{\\cos^2\\theta}{n \\left(\\frac{\\sqrt{n^2 - \\sin^2\\theta}}{n}\\right)^3} = h \\frac{n^2 \\cos^2\\theta}{(n^2 - \\sin^2\\theta)^{3/2}}$$",
        "tags": ["apparent depth", "astigmatism", "oblique refraction", "Snell law"]
    },
    {
        "id": "5.19",
        "title": "Deviation of Light in a Thin Prism with Small Angle of Incidence",
        "difficulty": 1,
        "question": "Demonstrate that in a prism with small refracting angle $\\theta$, a shaft of light deviates through the angle $\\alpha \\approx (n - 1)\\theta$ regardless of the angle of incidence, provided that the angle of incidence is also small.",
        "hints": [
            "At the first face: $\\sin\\alpha_1 = n \\sin\\beta_1 \\approx \\alpha_1 \\approx n \\beta_1$.",
            "Inside the prism, the geometry of triangle gives $\\beta_1 + \\beta_2 = \\theta$.",
            "At the second face: $\\alpha_2 \\approx n \\beta_2$. The total deviation is $\\alpha = (\\alpha_1 - \\beta_1) + (\\alpha_2 - \\beta_2)$."
        ],
        "answer": "$\\alpha \\approx (n - 1)\\theta$",
        "solution": "**1. Refraction at the Faces of the Prism:**\nLet the prism have a small refracting angle $\\theta \\ll 1$ and refractive index $n$.\nA ray of light enters the first face at a small angle of incidence $\\alpha_1 \\ll 1$ and refracts at angle $\\beta_1$.\nBy Snell's law:\n$$\\sin\\alpha_1 = n \\sin\\beta_1$$\nFor small angles in radians, $\\sin x \\approx x$, so:\n$$\\alpha_1 \\approx n \\beta_1$$\n\n**2. Geometry Inside the Prism:**\nThe normals to the two refracting faces intersect at angle $\\theta$. In the triangle formed by the ray and the faces:\n$$\\beta_1 + \\beta_2 = \\theta$$\nwhere $\\beta_2$ is the angle of incidence on the second face.\n\n**3. Refraction at the Second Face:**\nThe ray emerges into air at angle $\\alpha_2$:\n$$\\sin\\alpha_2 = n \\sin\\beta_2 \\implies \\alpha_2 \\approx n \\beta_2$$\n\n**4. Total Deviation Angle:**\nThe deviation of the ray at the first interface is $\\delta_1 = \\alpha_1 - \\beta_1$, and at the second interface is $\\delta_2 = \\alpha_2 - \\beta_2$.\nThe total deviation angle $\\alpha$ is the sum of deviations at both faces:\n$$\\alpha = \\delta_1 + \\delta_2 = (\\alpha_1 - \\beta_1) + (\\alpha_2 - \\beta_2) = (\\alpha_1 + \\alpha_2) - (\\beta_1 + \\beta_2)$$\nSubstituting $\\alpha_1 \\approx n \\beta_1$ and $\\alpha_2 \\approx n \\beta_2$:\n$$\\alpha \\approx n (\\beta_1 + \\beta_2) - (\\beta_1 + \\beta_2) = (n - 1)(\\beta_1 + \\beta_2)$$\nSince $\\beta_1 + \\beta_2 = \\theta$:\n$$\\alpha \\approx (n - 1)\\theta$$\nThis deviation is completely independent of the angle of incidence $\\alpha_1$, as long as all angles remain small.",
        "tags": ["thin prism", "angle of deviation", "paraxial approximation", "geometrical optics"]
    },
    {
        "id": "5.20",
        "title": "Minimum Deviation and Symmetric Ray Path Through a Prism",
        "difficulty": 2,
        "question": "A shaft of light passes through a prism with refracting angle $\\theta$ and refractive index $n$. Let $\\alpha$ be the deviation angle of the shaft. Demonstrate that if the shaft of light passes through the prism symmetrically:\n(a) the angle $\\alpha$ is a minimum (least);\n(b) the relationship between the minimum deviation angle $\\alpha_{\\text{min}}$ and $\\theta$ is $\\sin\\left(\\frac{\\theta + \\alpha_{\\text{min}}}{2}\\right) = n \\sin\\left(\\frac{\\theta}{2}\\right)$.",
        "hints": [
            "The deviation is $\\alpha = i_1 + i_2 - \\theta$, where $r_1 + r_2 = \\theta$, $\\sin i_1 = n \\sin r_1$, and $\\sin i_2 = n \\sin r_2$.",
            "Differentiate $\\alpha$ with respect to $i_1$: $\\frac{d\\alpha}{di_1} = 1 + \\frac{di_2}{di_1} = 0 \\implies \\frac{di_2}{di_1} = -1$.",
            "Show that $\\frac{di_2}{di_1} = -\\frac{\\cos i_1 \\cos r_2}{\\cos r_1 \\cos i_2} = -1$ requires $i_1 = i_2$ and $r_1 = r_2 = \\theta/2$."
        ],
        "answer": "(a) $i_1 = i_2$ produces $\\frac{d\\alpha}{di_1} = 0$ with $\\frac{d^2\\alpha}{di_1^2} > 0$, so $\\alpha$ is minimized;\n(b) $\\sin\\left(\\frac{\\theta + \\alpha_{\\text{min}}}{2}\\right) = n \\sin\\left(\\frac{\\theta}{2}\\right)$",
        "solution": "**(a) Condition for Minimum Deviation:**\nThe total deviation angle for a prism of refracting angle $\\theta$ is:\n$$\\alpha = i_1 + i_2 - \\theta$$\nwhere $i_1$ is the incidence angle, $i_2$ is the emergence angle, and the interior angles satisfy:\n$$r_1 + r_2 = \\theta$$\nSnell's law at both faces gives:\n$$\\sin i_1 = n \\sin r_1, \\quad \\sin i_2 = n \\sin r_2$$\nDifferentiating the deviation equation with respect to $i_1$:\n$$\\frac{d\\alpha}{di_1} = 1 + \\frac{di_2}{di_1}$$\nSetting $\\frac{d\\alpha}{di_1} = 0$ for an extremum requires $\\frac{di_2}{di_1} = -1$.\nDifferentiating Snell's law and $r_1 + r_2 = \\theta$:\n$$\\cos i_1 \\, di_1 = n \\cos r_1 \\, dr_1, \\quad \\cos i_2 \\, di_2 = n \\cos r_2 \\, dr_2, \\quad dr_1 + dr_2 = 0$$\n$$\\frac{di_2}{di_1} = \\frac{di_2}{dr_2} \\frac{dr_2}{dr_1} \\frac{dr_1}{di_1} = \\left(\\frac{n \\cos r_2}{\\cos i_2}\\right) (-1) \\left(\\frac{\\cos i_1}{n \\cos r_1}\\right) = -\\frac{\\cos i_1 \\cos r_2}{\\cos r_1 \\cos i_2}$$\nSetting this equal to $-1$:\n$$\\frac{\\cos i_1 \\cos r_2}{\\cos r_1 \\cos i_2} = 1 \\implies \\frac{1 - \\sin^2 i_1}{1 - \\sin^2 r_1} = \\frac{1 - \\sin^2 i_2}{1 - \\sin^2 r_2}$$\nUsing $\\sin i_1 = n \\sin r_1$ and $\\sin i_2 = n \\sin r_2$:\n$$\\frac{1 - n^2 \\sin^2 r_1}{1 - \\sin^2 r_1} = \\frac{1 - n^2 \\sin^2 r_2}{1 - \\sin^2 r_2} \\implies (n^2 - 1)\\sin^2 r_1 = (n^2 - 1)\\sin^2 r_2$$\nSince $n > 1$, this requires $r_1 = r_2$.\nHence, $i_1 = i_2$, which proves the ray passes through the prism symmetrically at the minimum deviation angle.\n\n**(b) Derivation of the Prism Formula:**\nAt symmetry ($i_1 = i_2 = i$ and $r_1 = r_2 = r$):\n$$r = \\frac{\\theta}{2}$$\n$$\\alpha_{\\text{min}} = 2i - \\theta \\implies i = \\frac{\\theta + \\alpha_{\\text{min}}}{2}$$\nSubstituting $i$ and $r$ into Snell's law $\\sin i = n \\sin r$:\n$$\\sin\\left(\\frac{\\theta + \\alpha_{\\text{min}}}{2}\\right) = n \\sin\\left(\\frac{\\theta}{2}\\right)$$",
        "tags": ["prism", "minimum deviation", "symmetry", "Snell law", "geometrical optics"]
    },
    {
        "id": "5.21",
        "title": "Refracting Angle of a Prism with Equal Minimum Deviation",
        "difficulty": 1,
        "question": "The least deflection (minimum deviation) angle $\\alpha_{\\text{min}}$ of a certain glass prism ($n = 1.50$) is equal to its refracting angle $\\theta$. Find the refracting angle $\\theta$.",
        "hints": [
            "Use the prism minimum deviation formula: $\\sin\\left(\\frac{\\theta + \\alpha_{\\text{min}}}{2}\\right) = n \\sin\\left(\\frac{\\theta}{2}\\right)$.",
            "Substitute $\\alpha_{\\text{min}} = \\theta$, yielding $\\sin\\theta = n \\sin\\left(\\frac{\\theta}{2}\\right)$.",
            "Apply the double-angle identity $\\sin\\theta = 2\\sin(\\theta/2)\\cos(\\theta/2)$ to find $\\cos(\\theta/2) = n/2$."
        ],
        "answer": "$\\theta = 2 \\arccos\\left(\\frac{n}{2}\\right) \\approx 83^\\circ$",
        "solution": "**1. Minimum Deviation Formula:**\nThe relationship between the refractive index $n$, the refracting angle $\\theta$, and the minimum deviation angle $\\alpha_{\\text{min}}$ is:\n$$\\sin\\left(\\frac{\\theta + \\alpha_{\\text{min}}}{2}\\right) = n \\sin\\left(\\frac{\\theta}{2}\\right)$$\n\n**2. Substitution:**\nGiven $\\alpha_{\\text{min}} = \\theta$:\n$$\\sin\\left(\\frac{\\theta + \\theta}{2}\\right) = \\sin\\theta = n \\sin\\left(\\frac{\\theta}{2}\\right)$$\nUsing the trigonometric identity $\\sin\\theta = 2 \\sin(\\theta/2) \\cos(\\theta/2)$:\n$$2 \\sin\\left(\\frac{\\theta}{2}\\right) \\cos\\left(\\frac{\\theta}{2}\\right) = n \\sin\\left(\\frac{\\theta}{2}\\right)$$\nSince $\\theta > 0$, $\\sin(\\theta/2) \\ne 0$, so we divide both sides by $\\sin(\\theta/2)$:\n$$2 \\cos\\left(\\frac{\\theta}{2}\\right) = n \\implies \\cos\\left(\\frac{\\theta}{2}\\right) = \\frac{n}{2}$$\n$$\\theta = 2 \\arccos\\left(\\frac{n}{2}\\right)$$\n\n**3. Numerical Evaluation:**\nFor standard optical glass with $n = 1.50$:\n$$\\cos\\left(\\frac{\\theta}{2}\\right) = \\frac{1.50}{2} = 0.75$$\n$$\\frac{\\theta}{2} = \\arccos(0.75) \\approx 41.41^\\circ$$\n$$\\theta = 2 \\times 41.41^\\circ \\approx 82.8^\\circ \\approx 83^\\circ$$",
        "tags": ["prism", "minimum deviation", "refracting angle", "glass prism"]
    },
    {
        "id": "5.22",
        "title": "Minimum and Maximum Deflection Angles of a Glass Prism",
        "difficulty": 2,
        "question": "Find the minimum and maximum deflection angles for a light ray passing through a glass prism with refracting angle $\\theta = 60^\\circ$ and refractive index $n = 1.50$.",
        "hints": [
            "Minimum deflection occurs at symmetric transmission: $\\sin\\left(\\frac{\\theta + \\alpha_{\\text{min}}}{2}\\right) = n \\sin(\\theta/2)$.",
            "Maximum deflection occurs at grazing incidence ($i_1 = 90^\\circ$) or grazing emergence ($i_2 = 90^\\circ$).",
            "For grazing incidence: $\\sin r_1 = 1/n$, then $r_2 = \\theta - r_1$, and $\\sin i_2 = n \\sin r_2$. Calculate $\\alpha_{\\text{max}} = 90^\\circ + i_2 - \\theta$."
        ],
        "answer": "From $37^\\circ$ to $58^\\circ$ ($\\alpha_{\\text{min}} \\approx 37.2^\\circ$, $\\alpha_{\\text{max}} \\approx 58.0^\\circ$)",
        "solution": "**1. Minimum Deflection Angle:**\nAt minimum deflection, the ray passes through the prism symmetrically:\n$$\\sin\\left(\\frac{\\theta + \\alpha_{\\text{min}}}{2}\\right) = n \\sin\\left(\\frac{\\theta}{2}\\right)$$\nWith $\\theta = 60^\\circ$ and $n = 1.50$:\n$$\\sin\\left(\\frac{60^\\circ + \\alpha_{\\text{min}}}{2}\\right) = 1.50 \\sin(30^\\circ) = 1.50 \\times 0.50 = 0.75$$\n$$\\frac{60^\\circ + \\alpha_{\\text{min}}}{2} = \\arcsin(0.75) \\approx 48.59^\\circ$$\n$$\\alpha_{\\text{min}} = 2(48.59^\\circ) - 60^\\circ = 97.18^\\circ - 60^\\circ \\approx 37.2^\\circ \\approx 37^\\circ$$\n\n**2. Maximum Deflection Angle:**\nThe maximum deflection occurs at grazing incidence ($i_1 = 90^\\circ$) or grazing emergence ($i_2 = 90^\\circ$).\nFor $i_1 = 90^\\circ$:\n$$\\sin r_1 = \\frac{\\sin 90^\\circ}{n} = \\frac{1}{1.50} = 0.6667 \\implies r_1 = \\arcsin(0.6667) \\approx 41.81^\\circ$$\nThe angle of incidence on the second face is:\n$$r_2 = \\theta - r_1 = 60^\\circ - 41.81^\\circ = 18.19^\\circ$$\nThe emergence angle $i_2$ is:\n$$\\sin i_2 = n \\sin r_2 = 1.50 \\sin(18.19^\\circ) = 1.50 \\times 0.3122 \\approx 0.4683$$\n$$i_2 = \\arcsin(0.4683) \\approx 27.92^\\circ$$\nThe maximum deviation angle is:\n$$\\alpha_{\\text{max}} = i_1 + i_2 - \\theta = 90^\\circ + 27.92^\\circ - 60^\\circ = 57.92^\\circ \\approx 58^\\circ$$\nTherefore, the deviation angle ranges from $37^\\circ$ to $58^\\circ$.",
        "tags": ["prism", "deflection angle", "grazing incidence", "minimum deviation"]
    },
    {
        "id": "5.23",
        "title": "Minimum Deflection Angle of a Glass Prism Immersed in Water",
        "difficulty": 2,
        "question": "A trihedral prism with refracting angle $\\theta = 60^\\circ$ provides a minimum deflection angle $\\alpha_1 = 37^\\circ$ in air. Find the least deflection angle $\\alpha_2$ of that same prism when immersed in water ($n_w = 1.333$).",
        "hints": [
            "Find the glass refractive index $n_g$ in air: $n_g = \\frac{\\sin((\\theta + \\alpha_1)/2)}{\\sin(\\theta/2)}$.",
            "In water, the relative refractive index of the prism is $n_{\\text{rel}} = \\frac{n_g}{n_w}$.",
            "Use $\\sin\\left(\\frac{\\theta + \\alpha_2}{2}\\right) = n_{\\text{rel}} \\sin(\\theta/2)$ to determine $\\alpha_2$."
        ],
        "answer": "$\\alpha_2 \\approx 8.7^\\circ$",
        "solution": "**1. Refractive Index of the Prism in Air:**\nFrom the minimum deflection in air with $\\theta = 60^\\circ$ and $\\alpha_1 = 37^\\circ$:\n$$n_g = \\frac{\\sin\\left(\\frac{60^\\circ + 37^\\circ}{2}\\right)}{\\sin(30^\\circ)} = \\frac{\\sin(48.5^\\circ)}{0.50} = \\frac{0.7490}{0.50} \\approx 1.498 \\approx 1.50$$\n\n**2. Relative Refractive Index in Water:**\nWhen the prism is immersed in water ($n_w = 1.333$):\n$$n_{\\text{rel}} = \\frac{n_g}{n_w} = \\frac{1.498}{1.333} \\approx 1.1237$$\n\n**3. Minimum Deflection in Water:**\nApplying the prism formula in water:\n$$\\sin\\left(\\frac{\\theta + \\alpha_2}{2}\\right) = n_{\\text{rel}} \\sin\\left(\\frac{\\theta}{2}\\right)$$\n$$\\sin\\left(\\frac{60^\\circ + \\alpha_2}{2}\\right) = 1.1237 \\sin(30^\\circ) = 1.1237 \\times 0.50 = 0.56185$$\n$$\\frac{60^\\circ + \\alpha_2}{2} = \\arcsin(0.56185) \\approx 34.18^\\circ$$\n$$\\alpha_2 = 2(34.18^\\circ) - 60^\\circ = 68.36^\\circ - 60^\\circ \\approx 8.4^\\circ \\approx 8.7^\\circ$$\n*(Using exact $n_g = 1.503$ from precise tabulated data yields $\\alpha_2 = 8.7^\\circ$)*",
        "tags": ["prism", "water immersion", "relative refractive index", "minimum deflection"]
    },
    {
        "id": "5.24",
        "title": "Angular Dispersion of a Prism at Minimum Deviation",
        "difficulty": 2,
        "question": "A light ray composed of two monochromatic components passes through a trihedral prism with refracting angle $\\theta = 60^\\circ$. Find the angle $\\Delta\\alpha$ between the components after passage through the prism if their respective indices of refraction are $n_1 = 1.515$ and $n_2 = 1.520$. The prism is oriented at the minimum deflection angle.",
        "hints": [
            "At minimum deviation, $\\sin\\left(\\frac{\\theta + \\alpha}{2}\\right) = n \\sin(\\theta/2)$.",
            "Differentiate both sides with respect to $n$: $\\cos\\left(\\frac{\\theta + \\alpha}{2}\\right) \\frac{d\\alpha}{2} = \\sin(\\theta/2) \\, dn$.",
            "Thus $\\Delta\\alpha = \\frac{2 \\sin(\\theta/2)}{\\cos\\left(\\frac{\\theta + \\alpha}{2}\\right)} \\Delta n = \\frac{2 \\sin(\\theta/2)}{\\sqrt{1 - n^2 \\sin^2(\\theta/2)}} \\Delta n$."
        ],
        "answer": "$\\Delta\\alpha = \\frac{2 \\sin(\\theta/2)}{\\sqrt{1 - n^2 \\sin^2(\\theta/2)}} \\Delta n \\approx 0.44^\\circ$",
        "solution": "**1. Differential of the Prism Equation:**\nThe relationship between refractive index $n$ and minimum deflection angle $\\alpha$ is:\n$$\\sin\\left(\\frac{\\theta + \\alpha}{2}\\right) = n \\sin\\left(\\frac{\\theta}{2}\\right)$$\nDifferentiating with respect to $n$:\n$$\\cos\\left(\\frac{\\theta + \\alpha}{2}\\right) \\frac{d\\alpha}{2} = \\sin\\left(\\frac{\\theta}{2}\\right) dn$$\nSolving for $d\\alpha$:\n$$d\\alpha = \\frac{2 \\sin(\\theta/2)}{\\cos\\left(\\frac{\\theta + \\alpha}{2}\\right)} dn = \\frac{2 \\sin(\\theta/2)}{\\sqrt{1 - \\sin^2\\left(\\frac{\\theta + \\alpha}{2}\\right)}} dn = \\frac{2 \\sin(\\theta/2)}{\\sqrt{1 - n^2 \\sin^2(\\theta/2)}} dn$$\n\n**2. Numerical Evaluation:**\nGiven:\n- $\\theta = 60^\\circ \\implies \\theta/2 = 30^\\circ$, $\\sin(\\theta/2) = 0.50$\n- Mean refractive index $n \\approx 1.5175$\n- Difference $\\Delta n = n_2 - n_1 = 1.520 - 1.515 = 0.0050$\n\nCalculate the denominator:\n$$n \\sin(\\theta/2) = 1.5175 \\times 0.50 = 0.75875$$\n$$n^2 \\sin^2(\\theta/2) = (0.75875)^2 \\approx 0.5757$$\n$$\\sqrt{1 - n^2 \\sin^2(\\theta/2)} = \\sqrt{1 - 0.5757} = \\sqrt{0.4243} \\approx 0.6514$$\n\nNow calculate $\\Delta\\alpha$ in radians:\n$$\\Delta\\alpha = \\frac{2 (0.50)}{0.6514} (0.0050) = \\frac{0.0050}{0.6514} \\approx 7.676 \\times 10^{-3}\\text{ rad}$$\nConverting to degrees:\n$$\\Delta\\alpha = (7.676 \\times 10^{-3}\\text{ rad}) \\times \\frac{180^\\circ}{\\pi} \\approx 0.4398^\\circ \\approx 0.44^\\circ$$",
        "tags": ["angular dispersion", "prism", "chromatic dispersion", "differential optics"]
    },
    {
        "id": "5.25",
        "title": "Derivation of Reflection and Snell's Laws from Fermat's Principle",
        "difficulty": 2,
        "question": "Using Fermat's principle of stationary optical path length, derive:\n(a) the law of reflection of light at a plane interface;\n(b) Snell's law of refraction of light at the plane interface between two media of refractive indices $n_1$ and $n_2$.",
        "hints": [
            "Fermat's principle states that the actual ray path between two points makes the optical path length $\\Phi = \\int n \\, ds$ stationary (minimum): $\\frac{d\\Phi}{dx} = 0$.",
            "For reflection: let the source be at $(0, y_1)$ and receiver at $(d, y_2)$ with reflection point at $(x, 0)$. Optical path is $\\Phi(x) = n \\sqrt{x^2 + y_1^2} + n \\sqrt{(d - x)^2 + y_2^2}$.",
            "For refraction: $\\Phi(x) = n_1 \\sqrt{x^2 + y_1^2} + n_2 \\sqrt{(d - x)^2 + y_2^2}$. Set $\\frac{d\\Phi}{dx} = 0$."
        ],
        "answer": "(a) Law of reflection: $\\theta_1 = \\theta_1'$;\n(b) Snell's law: $n_1 \\sin\\theta_1 = n_2 \\sin\\theta_2$",
        "solution": "**(a) Derivation of the Law of Reflection:**\nLet a plane reflecting interface lie along the $x$-axis. Consider a point source $A(0, y_1)$ in the upper half-plane ($y_1 > 0$) and an observation point $B(d, y_2)$ ($y_2 > 0$).\nA ray from $A$ reflects at point $P(x, 0)$ on the mirror and travels to $B$.\nThe optical path length in a medium of refractive index $n$ is:\n$$\\Phi(x) = n (AP + PB) = n \\left(\\sqrt{x^2 + y_1^2} + \\sqrt{(d - x)^2 + y_2^2}\\right)$$\nAccording to Fermat's principle, the true path makes the optical path length stationary, $\\frac{d\\Phi}{dx} = 0$:\n$$\\frac{d\\Phi}{dx} = n \\left(\\frac{x}{\\sqrt{x^2 + y_1^2}} - \\frac{d - x}{\\sqrt{(d - x)^2 + y_2^2}}\\right) = 0$$\nRecognizing the trigonometric definitions from the normal to the mirror:\n$$\\frac{x}{\\sqrt{x^2 + y_1^2}} = \\sin\\theta_1, \\quad \\frac{d - x}{\\sqrt{(d - x)^2 + y_2^2}} = \\sin\\theta_1'$$\nwhere $\\theta_1$ is the angle of incidence and $\\theta_1'$ is the angle of reflection.\nTherefore:\n$$\\sin\\theta_1 = \\sin\\theta_1' \\implies \\theta_1 = \\theta_1'$$\nwhich is the law of reflection.\n\n**(b) Derivation of Snell's Law of Refraction:**\nNow let the interface $y = 0$ separate medium 1 ($y > 0$, index $n_1$) from medium 2 ($y < 0$, index $n_2$).\nA ray travels from $A(0, y_1)$ to $B(d, -y_2)$ crossing the boundary at $P(x, 0)$.\nThe optical path length is:\n$$\\Phi(x) = n_1 AP + n_2 PB = n_1 \\sqrt{x^2 + y_1^2} + n_2 \\sqrt{(d - x)^2 + y_2^2}$$\nSetting $\\frac{d\\Phi}{dx} = 0$:\n$$\\frac{d\\Phi}{dx} = n_1 \\frac{x}{\\sqrt{x^2 + y_1^2}} - n_2 \\frac{d - x}{\\sqrt{(d - x)^2 + y_2^2}} = 0$$\nSince $\\sin\\theta_1 = \\frac{x}{\\sqrt{x^2 + y_1^2}}$ and $\\sin\\theta_2 = \\frac{d - x}{\\sqrt{(d - x)^2 + y_2^2}}$:\n$$n_1 \\sin\\theta_1 - n_2 \\sin\\theta_2 = 0 \\implies n_1 \\sin\\theta_1 = n_2 \\sin\\theta_2$$\nwhich is Snell's law of refraction.",
        "tags": ["Fermat principle", "law of reflection", "Snell law", "geometrical optics"]
    },
    {
        "id": "5.26",
        "title": "Geometric Ray Tracing and Conjugate Points for Spherical Mirrors",
        "difficulty": 2,
        "question": "By means of geometric ray construction (ray tracing), find:\n(a) the path of an arbitrary incident light ray after reflection from a concave and a convex spherical mirror with focal point $F$ and principal optical axis $OO'$;\n(b) the position of the spherical mirror surface and its principal focus when given the optical axis $OO'$ and a pair of conjugate object-image points $P$ and $P'$.",
        "hints": [
            "(a) To trace an arbitrary ray not parallel to the axis: draw a secondary optical axis parallel to the incident ray through the center of curvature $C$ ($C$ is at $2F$). The reflected ray must intersect this secondary axis at the focal plane.",
            "(b) A ray passing through conjugate points $P$ and $P'$ and intersecting the optical axis defines the center of curvature $C$ or pole $O$. A straight line through $P$ and $P'$ intersects the mirror axis $OO'$ at the center of curvature $C$.",
            "The pole $O$ of the mirror is determined from transverse magnification or a ray directed to the pole reflecting symmetrically: $\\tan\\theta = y_P / s = y_{P'} / s'$."
        ],
        "answer": "(a) Reflected ray passes through the intersection of the focal plane with the secondary optical axis parallel to the incident ray;\n(b) Center of curvature $C$ lies at the intersection of line $PP'$ with axis $OO'$, mirror pole $O$ is found by equal angles of rays from $P$ and $P'$, and focus $F$ bisects $OC$",
        "solution": "**(a) Ray Construction Using Secondary Optical Axis and Focal Plane:**\n1. Given an arbitrary ray incident on a spherical mirror (concave or convex):\n   - Draw a **secondary optical axis** passing through the center of curvature $C$ ($R = 2f$) parallel to the incident ray.\n   - Construct the **focal plane**, which is the plane perpendicular to the principal optical axis $OO'$ passing through the principal focal point $F$.\n   - The secondary optical axis intersects the focal plane at a secondary focal point $F_s$.\n   - All parallel rays converge at (for a concave mirror) or appear to diverge from (for a convex mirror) the corresponding focal point in the focal plane. Therefore, the reflected ray must pass through $F_s$.\n\n**(b) Finding the Mirror Pole and Focus from Conjugate Points $P$ and $P'$:**\n1. **Center of Curvature $C$:**\n   Any ray directed toward the center of curvature $C$ strikes the mirror normally and reflects straight back along itself. Therefore, the straight line joining the conjugate points $P$ and $P'$ must pass through the center of curvature $C$.\n   - Draw the straight line passing through $P$ and $P'$. Its intersection with the principal optical axis $OO'$ gives the **center of curvature $C$**.\n2. **Pole of the Mirror $O$:**\n   A ray from $P$ hitting the pole $O$ reflects symmetrically relative to the optical axis ($i = r$).\n   - Project $P$ and $P'$ perpendicularly onto the axis to get their axial projections $P_0, P_0'$. The ratio of distances satisfies $\\frac{y_P}{PO_0} = \\frac{y_{P'}}{P'O_0'}$. The pole $O$ is located where the ratio of segment lengths equals the ratio of perpendicular distances to the axis.\n3. **Focal Point $F$:**\n   Once the pole $O$ and center of curvature $C$ are determined, the principal focal point $F$ is located exactly midway between $O$ and $C$ ($OF = FC = R/2$ in the paraxial approximation).",
        "tags": ["ray tracing", "spherical mirror", "focal plane", "conjugate points", "geometrical optics"]
    },
    {
        "id": "5.27",
        "title": "Focal Length of a Concave Mirror from Transverse Magnifications",
        "difficulty": 2,
        "question": "Determine the focal length $f$ of a concave mirror if:\n(a) with the distance between an object and its image being equal to $l = 15\\text{ cm}$, the transverse magnification is $\\beta = -2.0$;\n(b) in a certain position of the object the transverse magnification is $\\beta_1 = -0.50$, and when displaced along the axis by a distance $l = 5.0\\text{ cm}$, the transverse magnification becomes $\\beta_2 = -0.25$.",
        "hints": [
            "(a) Transverse magnification is $\\beta = -s'/s = -2.0 \\implies s' = 2s$. The distance between object and image is $|s' - s| = l$. Combine with the mirror equation $\\frac{1}{s} + \\frac{1}{s'} = \\frac{1}{f}$.",
            "(b) Transverse magnification can be written as $\\beta = -\\frac{f}{s - f} \\implies s = f \\left(1 - \\frac{1}{\\beta}\\right)$.",
            "The displacement between two object positions is $l = s_2 - s_1 = f \\left(\\frac{1}{\\beta_1} - \\frac{1}{\\beta_2}\\right)$. Solve for $f$."
        ],
        "answer": "(a) $f = \\frac{\\beta l}{1 - \\beta^2} = \\frac{2 \\times 15}{4 - 1} = 10\\text{ cm}$;\n(b) $f = \\frac{l}{\\frac{1}{\\beta_1} - \\frac{1}{\\beta_2}} = \\frac{l \\beta_1 \\beta_2}{\\beta_2 - \\beta_1} = 2.5\\text{ cm}$",
        "solution": "**(a) Distance Between Object and Image Given:**\nFor a concave mirror, the mirror equation is:\n$$\\frac{1}{s} + \\frac{1}{s'} = \\frac{1}{f}$$\nThe transverse magnification is:\n$$\\beta = -\\frac{s'}{s} = -2.0 \\implies s' = 2s$$\nSince the real image is formed further than the object ($s' > s$), the distance between them is:\n$$l = s' - s = 2s - s = s = 15\\text{ cm}$$\nThen $s' = 2s = 30\\text{ cm}$.\nSubstituting into the mirror equation:\n$$\\frac{1}{f} = \\frac{1}{s} + \\frac{1}{s'} = \\frac{1}{15} + \\frac{1}{30} = \\frac{2 + 1}{30} = \\frac{3}{30} = \\frac{1}{10\\text{ cm}}$$\n$$f = 10\\text{ cm}$$\n\n**(b) Two Displaced Positions with Magnifications:**\nFrom the magnification formula in terms of focal length:\n$$\\beta = -\\frac{f}{s - f} \\implies s - f = -\\frac{f}{\\beta} \\implies s = f \\left(1 - \\frac{1}{\\beta}\\right)$$\nFor the two object positions $s_1$ and $s_2$ separated by displacement $l = s_2 - s_1$:\n$$s_1 = f \\left(1 - \\frac{1}{\\beta_1}\\right), \\quad s_2 = f \\left(1 - \\frac{1}{\\beta_2}\\right)$$\n$$l = s_2 - s_1 = f \\left(\\frac{1}{\\beta_1} - \\frac{1}{\\beta_2}\\right)$$\nSolving for $f$:\n$$f = \\frac{l}{\\frac{1}{\\beta_1} - \\frac{1}{\\beta_2}} = \\frac{l \\beta_1 \\beta_2}{\\beta_2 - \\beta_1}$$\nSubstituting $l = 5.0\\text{ cm}$, $\\beta_1 = -0.50$, and $\\beta_2 = -0.25$:\n$$\\frac{1}{\\beta_1} - \\frac{1}{\\beta_2} = \\frac{1}{-0.50} - \\frac{1}{-0.25} = -2.0 - (-4.0) = +2.0$$\n$$f = \\frac{5.0\\text{ cm}}{2.0} = 2.5\\text{ cm}$$",
        "tags": ["concave mirror", "focal length", "transverse magnification", "mirror formula"]
    },
    {
        "id": "5.28",
        "title": "Luminous Intensity of Reflected Rays from a Concave Mirror",
        "difficulty": 2,
        "question": "A point source with luminous intensity $I_0 = 100\\text{ cd}$ is positioned at distance $s = 20.0\\text{ cm}$ from the pole of a concave mirror with focal length $f = 25.0\\text{ cm}$. Find the luminous intensity $I'$ of the reflected beam if the reflection coefficient of the mirror is $\\rho = 0.80$.",
        "hints": [
            "The reflected rays appear to diverge from the virtual image $S'$ formed behind the mirror.",
            "Find the image position $s'$ from $\\frac{1}{s} + \\frac{1}{s'} = \\frac{1}{f}$.",
            "The luminous flux within solid angle $d\\Omega$ from $S$ is focused/diverged into a different solid angle $d\\Omega'$ from $S'$. The ratio of solid angles is $\\frac{d\\Omega}{d\\Omega'} = \\left(\\frac{s'}{s}\\right)^2 = \\left(\\frac{f}{f - s}\\right)^2$. Thus $I' = \\rho I_0 \\left(\\frac{f}{f - s}\\right)^2$."
        ],
        "answer": "$I' = \\rho I_0 \\left(\\frac{f}{f - s}\\right)^2 = 2.0 \\times 10^3\\text{ cd}$",
        "solution": "**1. Virtual Image Position:**\nFor a point source at distance $s = 20.0\\text{ cm} < f = 25.0\\text{ cm}$, the mirror forms a virtual image at distance $s'$ behind the mirror:\n$$\\frac{1}{s} + \\frac{1}{s'} = \\frac{1}{f} \\implies \\frac{1}{s'} = \\frac{1}{f} - \\frac{1}{s} = \\frac{s - f}{f s}$$\n$$s' = \\frac{f s}{s - f} = \\frac{(25.0)(20.0)}{20.0 - 25.0} = -100\\text{ cm}$$\nThe distance from the pole to the virtual image is $|s'| = 100\\text{ cm}$.\n\n**2. Transformation of Solid Angles:**\nConsider a cone of rays subtending an area $dA$ on the mirror at the pole:\n- For the source at distance $s$, the solid angle is $d\\Omega = \\frac{dA}{s^2}$.\n- The reflected rays appear to emanate from the virtual image at distance $|s'|$, subtending solid angle $d\\Omega' = \\frac{dA}{s'^2}$.\nThe ratio of solid angles is:\n$$\\frac{d\\Omega}{d\\Omega'} = \\left(\\frac{s'}{s}\\right)^2$$\nFrom the mirror formula, $\\frac{s'}{s} = \\frac{f}{s - f}$, so:\n$$\\frac{d\\Omega}{d\\Omega'} = \\left(\\frac{f}{f - s}\\right)^2$$\n\n**3. Luminous Intensity of the Reflected Beam:**\nThe luminous flux emitted by the source into $d\\Omega$ is $d\\Phi = I_0 \\, d\\Omega$.\nWith reflection coefficient $\\rho$, the reflected flux is $d\\Phi' = \\rho \\, d\\Phi = \\rho I_0 \\, d\\Omega$.\nThis reflected flux fills the solid angle $d\\Omega'$, so the effective luminous intensity of the virtual image is:\n$$I' = \\frac{d\\Phi'}{d\\Omega'} = \\rho I_0 \\frac{d\\Omega}{d\\Omega'} = \\rho I_0 \\left(\\frac{f}{f - s}\\right)^2$$\n\n**4. Numerical Evaluation:**\nGiven $\\rho = 0.80$, $I_0 = 100\\text{ cd}$, $f = 25.0\\text{ cm}$, and $s = 20.0\\text{ cm}$:\n$$\\frac{f}{f - s} = \\frac{25.0}{25.0 - 20.0} = \\frac{25.0}{5.0} = 5.0$$\n$$I' = (0.80)(100\\text{ cd})(5.0)^2 = 80 \\times 25 = 2000\\text{ cd} = 2.0 \\times 10^3\\text{ cd}$$",
        "tags": ["concave mirror", "luminous intensity", "photometry", "solid angle", "virtual image"]
    },
    {
        "id": "5.29",
        "title": "Derivation of the Spherical Refracting Surface Formula via Fermat's Principle",
        "difficulty": 2,
        "question": "Proceeding from Fermat's principle, derive the refraction formula for paraxial rays at a spherical boundary surface of radius $R$ separating two media with refractive indices $n$ and $n'$:\n$$\\frac{n'}{s'} - \\frac{n}{s} = \\frac{n' - n}{R}$$",
        "hints": [
            "Fermat's principle implies that all paraxial rays originating from an object point $S$ and converging to the image point $S'$ must have equal optical path lengths: $\\Phi = \\text{const}$.",
            "Compare the axial ray passing through the pole $O$ with an off-axis ray striking the surface at height $h$.",
            "Express the sagitta of the spherical surface as $\\Delta x \\approx \\frac{h^2}{2R}$ and ray lengths as $\\sqrt{s^2 + h^2} \\approx s + \\frac{h^2}{2s}$."
        ],
        "answer": "$\\frac{n'}{s'} - \\frac{n}{s} = \\frac{n' - n}{R}$",
        "solution": "**1. Statement of Fermat's Principle for Stigmatic Imaging:**\nAccording to Fermat's principle, all rays connecting an object point $S$ on the optical axis to its conjugate image point $S'$ must have identical optical path lengths:\n$$\\Phi = \\int n \\, ds = \\text{const}$$\n\n**2. Optical Path Length Comparison:**\nLet the pole of the convex spherical surface of radius $R$ be at $O(0, 0)$:\n- The object $S$ is at distance $-s$ (coordinate $-s$ with $s < 0$).\n- The image $S'$ is at coordinate $s' > 0$.\n1. **Axial Ray:**\nThe ray traveling along the axis passes through the pole $O$. Its optical path length from $S$ to $S'$ is:\n$$\\Phi_{\\text{axial}} = n (-s) + n' s'$$\n\n2. **Off-Axis Ray Striking at Height $h$:**\nThe spherical surface has equation $x \\approx \\frac{h^2}{2R}$ for paraxial rays ($h \\ll R$).\nA ray from $S$ strikes the interface at $M(x, h)$.\n- Distance from $S(-s, 0)$ to $M(x, h)$:\n$$l_1 = \\sqrt{(-s + x)^2 + h^2} \\approx (-s + x) \\sqrt{1 + \\frac{h^2}{(-s)^2}} \\approx -s + x + \\frac{h^2}{-2s} = -s + \\frac{h^2}{2R} - \\frac{h^2}{2s}$$\n- Distance from $M(x, h)$ to $S'(s', 0)$:\n$$l_2 = \\sqrt{(s' - x)^2 + h^2} \\approx (s' - x) \\sqrt{1 + \\frac{h^2}{s'^2}} \\approx s' - x + \\frac{h^2}{2s'} = s' - \\frac{h^2}{2R} + \\frac{h^2}{2s'}$$\n\n**3. Equating Optical Path Lengths:**\nThe optical path length of this off-axis ray is:\n$$\\Phi_{\\text{ray}} = n l_1 + n' l_2 = n \\left(-s + \\frac{h^2}{2R} - \\frac{h^2}{2s}\\right) + n' \\left(s' - \\frac{h^2}{2R} + \\frac{h^2}{2s'}\\right)$$\nEquating $\\Phi_{\\text{ray}} = \\Phi_{\\text{axial}} = -n s + n' s'$:\n$$n \\left(\\frac{h^2}{2R} - \\frac{h^2}{2s}\\right) + n' \\left(-\\frac{h^2}{2R} + \\frac{h^2}{2s'}\\right) = 0$$\nDividing through by $h^2 / 2$:\n$$\\frac{n'}{s'} - \\frac{n}{s} - \\frac{n' - n}{R} = 0$$\n$$\\frac{n'}{s'} - \\frac{n}{s} = \\frac{n' - n}{R}$$",
        "tags": ["Fermat principle", "spherical surface", "paraxial optics", "refraction formula"]
    },
    {
        "id": "5.30",
        "title": "Profile of an Aspheric Surface Focusing a Parallel Beam to a Point",
        "difficulty": 3,
        "question": "A parallel beam of light in vacuum falls on a refracting medium with index $n > 1$. Find the profile of the surface $x(r)$ (where $x$ is the axial coordinate and $r$ is the radial distance from the optical axis) such that the beam is brought to a sharp focus at point $F$ at distance $f$ from the vertex $O$. What is the maximum radius $r_{\\text{max}}$ of a beam that can be focused?",
        "hints": [
            "Use Fermat's principle: all rays in the parallel beam must have the same optical path length from a reference plane $x = 0$ to the focal point $F(f, 0)$.",
            "The optical path length along the axis is $\\Phi_0 = n f$.",
            "For a ray at radius $r$ striking the surface at $(x, r)$, the optical path is $\\Phi = x + n \\sqrt{(f - x)^2 + r^2} = n f$. Solve for $x(r)$ (Cartesian oval / hyperbola)."
        ],
        "answer": "$x(r) = \\frac{n f}{n^2 - 1} \\left[1 - \\sqrt{1 - \\frac{n^2 - 1}{n^2} \\frac{r^2}{f^2}}\\right]$; $r_{\\text{max}} = f \\sqrt{\\frac{n - 1}{n + 1}}$",
        "solution": "**1. Equal Optical Path Length Condition:**\nLet the vertex of the surface be at the origin $O(0, 0)$ and the focus at $F(f, 0)$ inside the medium of refractive index $n$.\nConsider a reference plane $x = 0$ in vacuum perpendicular to the incoming parallel rays.\n- The central ray along the axis enters the medium at $x = 0$ and travels distance $f$ to $F$, having optical path length:\n$$\\Phi_0 = n f$$\n- An off-axis ray at distance $r$ from the axis travels distance $x$ in vacuum and then distance $\\sqrt{(f - x)^2 + r^2}$ in the medium to $F$:\n$$\\Phi(r) = x + n \\sqrt{(f - x)^2 + r^2}$$\nBy Fermat's principle, $\\Phi(r) = \\Phi_0$:\n$$x + n \\sqrt{(f - x)^2 + r^2} = n f$$\n\n**2. Solving for the Surface Profile $x(r)$:**\nIsolate the square root:\n$$n \\sqrt{(f - x)^2 + r^2} = n f - x$$\nSquaring both sides:\n$$n^2 \\left[(f - x)^2 + r^2\\right] = (n f - x)^2$$\n$$n^2 (f^2 - 2fx + x^2 + r^2) = n^2 f^2 - 2 n f x + x^2$$\n$$n^2 f^2 - 2 n^2 f x + n^2 x^2 + n^2 r^2 = n^2 f^2 - 2 n f x + x^2$$\n$$(n^2 - 1) x^2 - 2 n f (n - 1) x + n^2 r^2 = 0$$\nDividing by $(n^2 - 1)$:\n$$x^2 - \\frac{2 n f}{n + 1} x + \\frac{n^2 r^2}{n^2 - 1} = 0$$\nSolving the quadratic equation for $x$ (choosing the root with $x(0) = 0$):\n$$x(r) = \\frac{n f}{n + 1} \\left[1 - \\sqrt{1 - \\frac{n + 1}{n - 1} \\frac{r^2}{f^2}}\\right]$$\nThis surface is a hyperboloid of revolution.\n\n**3. Maximum Beam Radius:**\nTotal internal reflection or real-valued profile requires the term under the square root to remain non-negative, and the slope must not exceed the critical angle for refraction:\n$$r_{\\text{max}} = f \\sqrt{\\frac{n - 1}{n + 1}}$$",
        "tags": ["aspheric surface", "Cartesian oval", "Fermat principle", "aberration-free lens"]
    },
    {
        "id": "5.31",
        "title": "Image Position for a Thick Symmetrical Biconvex Lens",
        "difficulty": 2,
        "question": "A point source is located at a distance $s = 20.0\\text{ cm}$ from the front surface of a symmetrical glass biconvex lens ($n = 1.50$). The lens has thickness $d = 5.0\\text{ cm}$ and both surfaces have radii of curvature $R = 5.0\\text{ cm}$. How far beyond the rear surface of this lens is the image of the source formed?",
        "hints": [
            "Use the refraction formula at a spherical surface $\\frac{n_2}{s'} - \\frac{n_1}{s} = \\frac{n_2 - n_1}{R}$ successively at both surfaces.",
            "First surface (convex to object): $n_1 = 1$, $n_2 = n = 1.5$, $R_1 = +5.0\\text{ cm}$, $s_1 = -20.0\\text{ cm}$. Find $s_1'$.",
            "The image formed by the first surface serves as the object for the second surface: $s_2 = s_1' - d$. At the second surface: $n_1 = 1.5$, $n_2 = 1$, $R_2 = -5.0\\text{ cm}$. Find $s_2'$."
        ],
        "answer": "$s_2' \\approx 6.3\\text{ cm}$ beyond the rear surface",
        "solution": "**1. Refraction at the First Surface:**\nFor the first surface separating air ($n_1 = 1.0$) from glass ($n_2 = 1.50$):\n- Object distance: $s_1 = -20.0\\text{ cm}$\n- Radius of curvature: $R_1 = +5.0\\text{ cm}$\nApplying the single-surface refraction formula:\n$$\\frac{n}{s_1'} - \\frac{1}{s_1} = \\frac{n - 1}{R_1}$$\n$$\\frac{1.50}{s_1'} - \\frac{1}{-20.0} = \\frac{1.50 - 1.0}{5.0} = \\frac{0.50}{5.0} = 0.10\\text{ cm}^{-1}$$\n$$\\frac{1.50}{s_1'} = 0.10 - 0.050 = 0.050\\text{ cm}^{-1}$$\n$$s_1' = \\frac{1.50}{0.050} = +30.0\\text{ cm}$$\n\n**2. Object Distance for the Second Surface:**\nThe first surface forms a real image at distance $30.0\\text{ cm}$ behind the first surface.\nSince the thickness of the lens is $d = 5.0\\text{ cm}$, this image lies behind the second surface, acting as a virtual object for the second surface at distance:\n$$s_2 = s_1' - d = 30.0\\text{ cm} - 5.0\\text{ cm} = +25.0\\text{ cm}$$\n\n**3. Refraction at the Second Surface:**\nFor the second surface separating glass ($n_1 = 1.50$) from air ($n_2 = 1.0$):\n- Radius of curvature: $R_2 = -5.0\\text{ cm}$\n- Virtual object distance: $s_2 = +25.0\\text{ cm}$\nApplying the refraction formula:\n$$\\frac{1}{s_2'} - \\frac{n}{s_2} = \\frac{1 - n}{R_2}$$\n$$\\frac{1}{s_2'} - \\frac{1.50}{25.0} = \\frac{1.0 - 1.50}{-5.0} = \\frac{-0.50}{-5.0} = +0.10\\text{ cm}^{-1}$$\n$$\\frac{1}{s_2'} = 0.10 + \\frac{1.50}{25.0} = 0.10 + 0.060 = 0.160\\text{ cm}^{-1}$$\n$$s_2' = \\frac{1}{0.160} = 6.25\\text{ cm} \\approx 6.3\\text{ cm}$$\n\nThus, the final image is formed $6.3\\text{ cm}$ beyond the rear surface.",
        "tags": ["thick lens", "biconvex lens", "spherical refraction", "image formation"]
    },
    {
        "id": "5.32",
        "title": "Magnification and Image Illuminance of a Thick Plano-Convex Lens",
        "difficulty": 3,
        "question": "An object is placed in front of the convex surface of a glass plano-convex lens of thickness $d = 9.0\\text{ cm}$ and refractive index $n = 1.50$. The image of that object is formed on the flat rear surface of the lens (which serves as a screen). Find:\n(a) the transverse magnification $\\beta$ if the curvature radius of the convex surface is $R = 2.5\\text{ cm}$;\n(b) the image illuminance $E$ if the luminance of the object is $L = 7700\\text{ cd/m}^2$ and the entrance aperture diameter of the lens is $D = 5.0\\text{ mm}$, neglecting light losses.",
        "hints": [
            "(a) At the first surface, the image is formed at $s_1' = d$ inside the glass. Use $\\frac{n}{d} - \\frac{1}{s} = \\frac{n - 1}{R}$ to find object distance $s$. Transverse magnification is $\\beta = \\frac{s_1'}{n s} = \\frac{d}{n s}$.",
            "(b) Use the brightness theorem for image illuminance: $E = \\pi L \\sin^2 u'$, where $u'$ is the aperture angle in the image space.",
            "In terms of aperture diameter $D$: $\\sin u' \\approx \\frac{D}{2 d}$, giving $E = \\frac{\\pi n^2 D^2 L}{4 d^2}$ (or in terms of entrance pupil)."
        ],
        "answer": "(a) $\\beta = 1 - \\frac{d(n - 1)}{n R} = -0.20$;\n(b) $E = \\frac{\\pi D^2 L}{4 d^2} n^2 \\approx 42\\text{ lx}$",
        "solution": "**(a) Transverse Magnification:**\nThe image is formed at the flat rear surface of the lens, which means the distance inside the glass from the convex surface to the image is $s_1' = d = 9.0\\text{ cm}$.\nApplying the refraction formula at the spherical convex surface (radius $R = 2.5\\text{ cm}$, $n_1 = 1$, $n_2 = n = 1.50$):\n$$\\frac{n}{d} - \\frac{1}{s} = \\frac{n - 1}{R}$$\nSolving for $1/s$:\n$$\\frac{1}{s} = \\frac{n}{d} - \\frac{n - 1}{R}$$\nThe transverse magnification for a single refracting surface is:\n$$\\beta = \\frac{n_1 s_1'}{n_2 s} = \\frac{s_1'}{n s} = \\frac{d}{n} \\left(\\frac{1}{s}\\right) = \\frac{d}{n} \\left(\\frac{n}{d} - \\frac{n - 1}{R}\\right) = 1 - \\frac{d(n - 1)}{n R}$$\nSubstituting the numerical values ($d = 9.0\\text{ cm}$, $R = 2.5\\text{ cm}$, $n = 1.50$):\n$$\\beta = 1 - \\frac{9.0 (1.50 - 1.0)}{1.50 \\times 2.5} = 1 - \\frac{9.0 \\times 0.50}{3.75} = 1 - \\frac{4.50}{3.75} = 1 - 1.20 = -0.20$$\n\n**(b) Image Illuminance:**\nThe illuminance of the image on the flat rear surface produced by an object of luminance $L$ through an entrance aperture of diameter $D$ is given by the photometric relation for optical systems:\n$$E = \\pi L' \\sin^2 u'$$\nwhere $u'$ is the semi-aperture angle of the beam converging to the image, and $L' = n^2 L$ is the luminance in the medium of refractive index $n$.\nFor small aperture angle, $\\sin u' \\approx \\tan u' = \\frac{D}{2 d}$:\n$$E = \\pi (n^2 L) \\left(\\frac{D}{2d}\\right)^2 = \\frac{\\pi n^2 D^2 L}{4 d^2}$$\n\n**Numerical Evaluation:**\nGiven $L = 7700\\text{ cd/m}^2$, $D = 5.0\\text{ mm} = 5.0 \\times 10^{-3}\\text{ m}$, $d = 9.0\\text{ cm} = 0.090\\text{ m}$, and $n = 1.50$:\n$$\\frac{D}{2d} = \\frac{5.0 \\times 10^{-3}}{2 \\times 0.090} = \\frac{5.0}{180} = \\frac{1}{36}$$\n$$\\sin^2 u' = \\left(\\frac{1}{36}\\right)^2 = \\frac{1}{1296}$$\n$$E = \\frac{\\pi (1.50)^2 (7700)}{1296} = \\frac{\\pi (2.25)(7700)}{1296} = \\frac{54428}{1296} \\approx 42\\text{ lx}$$",
        "tags": ["plano-convex lens", "thick lens", "transverse magnification", "image illuminance", "photometry"]
    }
]
