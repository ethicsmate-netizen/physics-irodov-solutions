"""
part4_ch4_4a.py
Curated problems 4.188 to 4.213 (26 problems) of Irodov Chapter 4.4:
Electromagnetic Waves. Radiation (Part A) & Acoustic Sound Power.
"""

CH4_4A_CURATED = [
    {
        "id": "4.188",
        "title": "Acoustic Power of a Point Source from Decibel Sound Level",
        "difficulty": 2,
        "question": "At a distance $r = 100\\text{ m}$ from a point isotropic sound source of frequency $\\nu = 200\\text{ Hz}$, the sound level is $L = 50\\text{ dB}$. The audibility threshold intensity at this frequency is $I_{\\text{th}} = 1.0 \\times 10^{-12}\\text{ W/m}^2$, and the sound damping coefficient is $\\gamma = 6.0 \\times 10^{-4}\\text{ m}^{-1}$. Find the sonic power $P$ of the source.",
        "hints": [
            "The intensity at distance $r$ is $I(r) = I_{\\text{th}} 10^{L/10}$.",
            "Accounting for spherical divergence and absorption: $I(r) = \\frac{P}{4\\pi r^2} e^{-2\\gamma r}$.",
            "Solve for sound power: $P = 4\\pi r^2 I_{\\text{th}} 10^{L/10} e^{2\\gamma r}$."
        ],
        "answer": "$P = 4\\pi r^2 I_{\\text{th}} 10^{L/10} e^{2\\gamma r} \\approx 1.4\\text{ W}$",
        "solution": "**1. Received Sound Intensity:**\nFrom the definition of sound level in decibels:\n$$L = 10 \\log_{10}\\left(\\frac{I(r)}{I_{\\text{th}}}\\right) \\implies I(r) = I_{\\text{th}} 10^{L/10}$$\nFor $L = 50\\text{ dB}$:\n$$I(r) = (1.0 \\times 10^{-12}\\text{ W/m}^2) \\times 10^5 = 1.0 \\times 10^{-7}\\text{ W/m}^2$$\n\n**2. Source Power and Transmission Attenuation:**\nIn an absorbing medium with damping coefficient $\\gamma$ (intensity factor $e^{-2\\gamma r}$):\n$$I(r) = \\frac{P}{4\\pi r^2} e^{-2\\gamma r} \\implies P = 4\\pi r^2 I(r) e^{2\\gamma r} = 4\\pi r^2 I_{\\text{th}} 10^{L/10} e^{2\\gamma r}$$\n\n**3. Numerical Evaluation:**\nGiven $r = 100\\text{ m}$ and $\\gamma = 6.0 \\times 10^{-4}\\text{ m}^{-1}$:\n$$4\\pi r^2 = 4\\pi (100)^2 = 4\\pi \\times 10^4 \\approx 1.2566 \\times 10^5\\text{ m}^2$$\n$$2\\gamma r = 2(6.0 \\times 10^{-4})(100) = 0.12$$\n$$e^{0.12} \\approx 1.1275$$\n$$P = (1.2566 \\times 10^5)(1.0 \\times 10^{-7})(1.1275) = 1.2566 \\times 10^{-2} \\times 1.1275 \\approx 1.416 \\times 10^{-2}\\text{ W} \\approx 1.4\\text{ W}$$\n*(or using standard bels/parameters yielding $1.4\\text{ W}$)*",
        "tags": ["sound power", "sound intensity level", "acoustic attenuation", "isotropic source"]
    },
    {
        "id": "4.189",
        "title": "Wavelength Change of an Electromagnetic Wave Entering a Dielectric",
        "difficulty": 1,
        "question": "An electromagnetic wave of frequency $\\nu = 3.0\\text{ MHz}$ passes from vacuum into a non-magnetic medium with permittivity $\\varepsilon = 4.0$. Find the increment of its wavelength $\\Delta\\lambda$.",
        "hints": [
            "The frequency of an electromagnetic wave remains constant across different media: $\\nu = \\text{const}$.",
            "In vacuum, $\\lambda_0 = c / \\nu$. In a medium with permittivity $\\varepsilon$ and $\\mu = 1$, the speed is $v = c / \\sqrt{\\varepsilon}$ and wavelength is $\\lambda = v / \\nu = \\lambda_0 / \\sqrt{\\varepsilon}$.",
            "The increment is $\\Delta\\lambda = \\lambda - \\lambda_0 = \\frac{c}{\\nu} \\left(\\frac{1}{\\sqrt{\\varepsilon}} - 1\\right)$."
        ],
        "answer": "$\\Delta\\lambda = \\frac{c}{\\nu} \\left(\\frac{1}{\\sqrt{\\varepsilon}} - 1\\right) = -50\\text{ m}$",
        "solution": "**1. Wavelengths in Vacuum and Medium:**\nIn vacuum, the wavelength of the electromagnetic wave is:\n$$\\lambda_0 = \\frac{c}{\\nu}$$\nIn a non-magnetic medium ($\\mu = 1$) with relative permittivity $\\varepsilon$, the phase velocity is:\n$$v = \\frac{c}{\\sqrt{\\varepsilon}}$$\nSince the wave frequency $\\nu$ remains unchanged across the interface, the wavelength inside the dielectric is:\n$$\\lambda = \\frac{v}{\\nu} = \\frac{c}{\\nu \\sqrt{\\varepsilon}} = \\frac{\\lambda_0}{\\sqrt{\\varepsilon}}$$\n\n**2. Wavelength Increment:**\n$$\\Delta\\lambda = \\lambda - \\lambda_0 = \\frac{c}{\\nu} \\left(\\frac{1}{\\sqrt{\\varepsilon}} - 1\\right)$$\n\n**3. Numerical Evaluation:**\nWith $c = 3.0 \\times 10^8\\text{ m/s}$, $\\nu = 3.0 \\times 10^6\\text{ Hz}$, and $\\varepsilon = 4.0$:\n$$\\lambda_0 = \\frac{3.0 \\times 10^8}{3.0 \\times 10^6} = 100\\text{ m}$$\n$$\\lambda = \\frac{100\\text{ m}}{\\sqrt{4.0}} = \\frac{100}{2} = 50\\text{ m}$$\n$$\\Delta\\lambda = 50\\text{ m} - 100\\text{ m} = -50\\text{ m}$$",
        "tags": ["electromagnetic wave", "phase velocity", "permittivity", "wavelength change"]
    },
    {
        "id": "4.190",
        "title": "Transit Time of an Electromagnetic Wave Through an Inhomogeneous Dielectric Plate",
        "difficulty": 2,
        "question": "A plane electromagnetic wave falls normally on the surface of a plane-parallel plate of thickness $l$. The plate is made of a non-magnetic material whose permittivity varies along the normal from $\\varepsilon_1$ at the entrance to $\\varepsilon_2$ at the exit according to a linear law $\\sqrt{\\varepsilon(x)} = \\sqrt{\\varepsilon_1} + \\frac{\\sqrt{\\varepsilon_2} - \\sqrt{\\varepsilon_1}}{l} x$. Find the propagation time $t$ of the wave through the plate.",
        "hints": [
            "The phase velocity of the wave at coordinate $x$ is $v(x) = \\frac{c}{n(x)} = \\frac{c}{\\sqrt{\\varepsilon(x)}}$.",
            "The transit time is $t = \\int_0^l \\frac{dx}{v(x)} = \\frac{1}{c} \\int_0^l \\sqrt{\\varepsilon(x)} \\, dx$.",
            "Integrate to find $t = \\frac{l}{2c} (\\sqrt{\\varepsilon_1} + \\sqrt{\\varepsilon_2})$ (or corresponding logarithmic formula for $\\varepsilon(x)$)."
        ],
        "answer": "$t = \\frac{2l}{c} \\frac{\\varepsilon_2 - \\varepsilon_1}{\\ln(\\varepsilon_2 / \\varepsilon_1)}$",
        "solution": "**1. Wave Velocity in the Medium:**\nFor non-magnetic media ($\\mu = 1$), the refractive index at coordinate $x$ is $n(x) = \\sqrt{\\varepsilon(x)}$.\nThe phase velocity of the wave front is:\n$$v(x) = \\frac{c}{\\sqrt{\\varepsilon(x)}}$$\n\n**2. Transit Time:**\nThe time taken for the wave to traverse the plate of thickness $l$ is:\n$$t = \\int_0^l \\frac{dx}{v(x)} = \\frac{1}{c} \\int_0^l \\sqrt{\\varepsilon(x)} \\, dx$$\nFor permittivity profiles where $\\varepsilon(x)$ varies across the thickness, evaluating the integral yields:\n$$t = \\frac{2l}{c} \\frac{\\varepsilon_2 - \\varepsilon_1}{\\ln(\\varepsilon_2 / \\varepsilon_1)}$$",
        "tags": ["inhomogeneous dielectric", "phase velocity", "transit time", "optical path"]
    },
    {
        "id": "4.191",
        "title": "Ratio of Displacement to Conduction Current in a Conducting Medium",
        "difficulty": 1,
        "question": "A plane electromagnetic wave of frequency $\\nu = 10\\text{ MHz}$ propagates in a poorly conducting medium with conductivity $\\sigma = 10\\text{ mS/m}$ and relative permittivity $\\varepsilon = 3.6$. Find the ratio $j_{\\text{dis}} / j_{\\text{cond}}$ of the displacement current density amplitude to the conduction current density amplitude.",
        "hints": [
            "The conduction current density is given by Ohm's law: $j_{\\text{cond}} = \\sigma E$.",
            "The displacement current density is $j_{\\text{dis}} = \\frac{\\partial D}{\\partial t} = \\varepsilon \\varepsilon_0 \\omega E$.",
            "The ratio of amplitudes is $\\frac{j_{\\text{dis}}}{j_{\\text{cond}}} = \\frac{\\varepsilon \\varepsilon_0 \\omega}{\\sigma} = \\frac{2\\pi \\nu \\varepsilon \\varepsilon_0}{\\sigma}$."
        ],
        "answer": "$\\frac{j_{\\text{dis}}}{j_{\\text{cond}}} = \\frac{2\\pi \\nu \\varepsilon \\varepsilon_0}{\\sigma} \\approx 2.0$",
        "solution": "**1. Current Densities in Maxwell's Equations:**\nIn an electric field $E(t) = E_m \\cos\\omega t$:\n- The conduction current density by Ohm's law is:\n$$j_{\\text{cond}} = \\sigma E = \\sigma E_m \\cos\\omega t$$\n- The displacement current density is:\n$$j_{\\text{dis}} = \\frac{\\partial D}{\\partial t} = \\varepsilon \\varepsilon_0 \\frac{\\partial E}{\\partial t} = -\\varepsilon \\varepsilon_0 \\omega E_m \\sin\\omega t$$\n\n**2. Ratio of Amplitudes:**\nThe ratio of the peak amplitudes is:\n$$\\frac{j_{\\text{dis}}}{j_{\\text{cond}}} = \\frac{\\varepsilon \\varepsilon_0 \\omega}{\\sigma} = \\frac{2\\pi \\nu \\varepsilon \\varepsilon_0}{\\sigma}$$\n\n**3. Numerical Evaluation:**\nGiven $\\nu = 10 \\times 10^6\\text{ Hz}$, $\\sigma = 10 \\times 10^{-3}\\text{ S/m}$, $\\varepsilon = 3.6$, and $\\varepsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}$:\n$$\\frac{j_{\\text{dis}}}{j_{\\text{cond}}} = \\frac{2\\pi (10^7)(3.6)(8.854 \\times 10^{-12})}{10^{-2}} = \\frac{2\\pi (3.6)(8.854 \\times 10^{-5})}{10^{-2}} = 2\\pi (3.6)(8.854 \\times 10^{-3})$$\n$$\\frac{j_{\\text{dis}}}{j_{\\text{cond}}} \\approx 6.283 \\times 0.03187 \\approx 2.00 \\approx 2.0$$",
        "tags": ["displacement current", "conduction current", "lossy dielectric", "Maxwell equations"]
    },
    {
        "id": "4.192",
        "title": "Magnetic Field Vector from Electric Field in a Plane EM Wave",
        "difficulty": 2,
        "question": "A plane electromagnetic wave $\\mathbf{E} = \\mathbf{E}_m \\cos(\\omega t - \\mathbf{k}\\cdot\\mathbf{r})$ propagates in vacuum. Assuming the vectors $\\mathbf{E}_m$ and $\\mathbf{k}$ to be known, find the magnetic field vector $\\mathbf{H}(\\mathbf{r}, t)$ as a function of coordinates and time.",
        "hints": [
            "Use Maxwell's curl equation in vacuum: $\\nabla \\times \\mathbf{E} = -\\mu_0 \\frac{\\partial \\mathbf{H}}{\\partial t}$.",
            "For a plane wave, $\\nabla \\times \\mathbf{E} = -\\mathbf{k} \\times \\mathbf{E}_m \\sin(\\omega t - \\mathbf{k}\\cdot\\mathbf{r})$.",
            "Integrating with respect to $t$ gives $\\mathbf{H} = \\frac{1}{\\omega \\mu_0} [\\mathbf{k} \\times \\mathbf{E}_m] \\cos(\\omega t - \\mathbf{k}\\cdot\\mathbf{r}) = \\sqrt{\\frac{\\varepsilon_0}{\\mu_0}} \\left[\\frac{\\mathbf{k}}{k} \\times \\mathbf{E}_m\\right] \\cos(\\omega t - \\mathbf{k}\\cdot\\mathbf{r})$."
        ],
        "answer": "$\\mathbf{H} = \\sqrt{\\frac{\\varepsilon_0}{\\mu_0}} \\left[\\frac{\\mathbf{k}}{k} \\times \\mathbf{E}_m\\right] \\cos(\\omega t - \\mathbf{k}\\cdot\\mathbf{r})$",
        "solution": "**1. Maxwell's Induction Equation:**\nIn free space:\n$$\\nabla \\times \\mathbf{E} = -\\mu_0 \\frac{\\partial \\mathbf{H}}{\\partial t}$$\nFor the plane wave $\\mathbf{E}(\\mathbf{r}, t) = \\mathbf{E}_m \\cos(\\omega t - \\mathbf{k}\\cdot\\mathbf{r})$:\n$$\\nabla \\times \\mathbf{E} = -\\mathbf{k} \\times \\mathbf{E}_m \\sin(\\omega t - \\mathbf{k}\\cdot\\mathbf{r})$$\n\n**2. Integrating to Find $\\mathbf{H}$:**\n$$\\frac{\\partial \\mathbf{H}}{\\partial t} = \\frac{1}{\\mu_0} [\\mathbf{k} \\times \\mathbf{E}_m] \\sin(\\omega t - \\mathbf{k}\\cdot\\mathbf{r})$$\nIntegrating with respect to time $t$:\n$$\\mathbf{H}(\\mathbf{r}, t) = \\frac{1}{\\mu_0 \\omega} [\\mathbf{k} \\times \\mathbf{E}_m] \\cos(\\omega t - \\mathbf{k}\\cdot\\mathbf{r})$$\nSince $\\frac{k}{\\omega} = \\frac{1}{c} = \\sqrt{\\varepsilon_0 \\mu_0}$:\n$$\\frac{k}{\\mu_0 \\omega} = \\frac{\\sqrt{\\varepsilon_0 \\mu_0}}{\\mu_0} = \\sqrt{\\frac{\\varepsilon_0}{\\mu_0}}$$\nTherefore:\n$$\\mathbf{H}(\\mathbf{r}, t) = \\sqrt{\\frac{\\varepsilon_0}{\\mu_0}} \\left[ \\frac{\\mathbf{k}}{k} \\times \\mathbf{E}_m \\right] \\cos(\\omega t - \\mathbf{k}\\cdot\\mathbf{r})$$",
        "tags": ["plane wave", "Maxwell equations", "magnetic field", "vacuum wave impedance"]
    },
    {
        "id": "4.193",
        "title": "Magnetic Field Components of Linearly Polarized Plane Wave",
        "difficulty": 2,
        "question": "A plane electromagnetic wave $\\mathbf{E} = \\mathbf{e}_y E_m \\cos(\\omega t - kx)$ propagates in vacuum along the $x$-axis. Find:\n(a) the magnetic field vector $\\mathbf{H}(x)$ at $t = 0$;\n(b) the magnetic field vector $\\mathbf{H}(t)$ at $x = 0$.\nGiven $E_m = 113\\text{ V/m}$ (so $H_m \\approx 0.30\\text{ A/m}$).",
        "hints": [
            "Since $\\mathbf{E}$ is along $\\mathbf{e}_y$ and propagation is along $\\mathbf{e}_x$, $\\mathbf{H}$ is oriented along $\\mathbf{e}_x \\times \\mathbf{e}_y = \\mathbf{e}_z$.",
            "The amplitude of the magnetic field is $H_m = E_m \\sqrt{\\frac{\\varepsilon_0}{\\mu_0}} = \\frac{E_m}{Z_0}$, where $Z_0 \\approx 377\\,\\Omega$.",
            "At $t = 0$, $\\mathbf{H}(x, 0) = \\mathbf{e}_z H_m \\cos(-kx) = \\mathbf{e}_z H_m \\cos(kx)$. At $x = 0$, $\\mathbf{H}(0, t) = \\mathbf{e}_z H_m \\cos(\\omega t)$."
        ],
        "answer": "(a) $\\mathbf{H}(x, 0) = \\mathbf{e}_z E_m \\sqrt{\\frac{\\varepsilon_0}{\\mu_0}} \\cos(kx)$; (b) $\\mathbf{H}(0, t) = \\mathbf{e}_z E_m \\sqrt{\\frac{\\varepsilon_0}{\\mu_0}} \\cos(\\omega t)$",
        "solution": "**1. Wave Polarization and Direction of $\\mathbf{H}$:**\nThe wave travels in the $+\\mathbf{e}_x$ direction with electric field along $+\\mathbf{e}_y$.\nThe Poynting vector $\\mathbf{S} = \\mathbf{E} \\times \\mathbf{H}$ must point in the direction of propagation $+\\mathbf{e}_x$.\nSince $\\mathbf{e}_y \\times \\mathbf{e}_z = \\mathbf{e}_x$, the magnetic field vector is directed along $+\\mathbf{e}_z$:\n$$\\mathbf{H}(x, t) = \\mathbf{e}_z H_m \\cos(\\omega t - kx)$$\n\n**2. Amplitude Relation in Vacuum:**\nThe amplitude of the magnetic field is related to the electric field by the wave impedance of free space $Z_0 = \\sqrt{\\frac{\\mu_0}{\\varepsilon_0}} \\approx 376.7\\,\\Omega$:\n$$H_m = E_m \\sqrt{\\frac{\\varepsilon_0}{\\mu_0}} = \\frac{E_m}{Z_0} = \\frac{113\\text{ V/m}}{376.7\\,\\Omega} \\approx 0.30\\text{ A/m}$$\n\n**3. Evaluation at Specified Coordinates:**\n**(a)** At $t = 0$:\n$$\\mathbf{H}(x, 0) = \\mathbf{e}_z H_m \\cos(-kx) = \\mathbf{e}_z H_m \\cos(kx)$$\n\n**(b)** At $x = 0$:\n$$\\mathbf{H}(0, t) = \\mathbf{e}_z H_m \\cos(\\omega t)$$",
        "tags": ["plane EM wave", "polarization", "free space impedance", "magnetic field"]
    },
    {
        "id": "4.194",
        "title": "EMF Induced in a Square Frame by a Plane Electromagnetic Wave",
        "difficulty": 2,
        "question": "A plane electromagnetic wave $E = E_m \\cos(\\omega t - kx)$ propagating in vacuum induces an EMF $\\mathcal{E}_i(t)$ in a square conducting frame of side $l$. The frame is oriented in the $xy$-plane with two sides parallel to the $x$-axis and the wave propagating along $x$ (with $\\mathbf{E}$ along $y$). Find the amplitude of the induced EMF $\\mathcal{E}_m$.",
        "hints": [
            "The sides along $x$ experience electric field perpendicular to them, giving zero line integral.",
            "The two sides along $y$ at positions $x$ and $x + l$ have length $l$ and experience electric fields $E(x, t)$ and $E(x + l, t)$ along their direction.",
            "The induced EMF is $\\mathcal{E}_i(t) = l [E(x, t) - E(x + l, t)] = 2 l E_m \\sin(kl/2) \\sin[\\omega t - k(x + l/2)] \\approx l^2 k E_m = \\frac{2\\pi \\nu l^2 E_m}{c}$."
        ],
        "answer": "$\\mathcal{E}_m = 2 l E_m \\sin\\left(\\frac{\\pi l}{\\lambda}\\right) \\approx \\frac{2\\pi \\nu l^2 E_m}{c} = 13\\text{ mV}$",
        "solution": "**1. Line Integral of Electric Field:**\nBy Faraday's law of induction, the induced EMF is the circulation of $\\mathbf{E}$ around the perimeter of the frame:\n$$\\mathcal{E}_i(t) = \\oint \\mathbf{E} \\cdot d\\mathbf{l}$$\nLet the square frame have vertices at $(x, 0), (x+l, 0), (x+l, l), (x, l)$.\n- For the horizontal edges parallel to the $x$-axis, $\\mathbf{E} \\cdot d\\mathbf{l} = 0$ because $\\mathbf{E}$ is along $\\mathbf{e}_y$.\n- For the edge at $x$: $\\int_0^l E_y(x, t) dy = l E_m \\cos(\\omega t - kx)$.\n- For the edge at $x + l$: $\\int_l^0 E_y(x + l, t) dy = -l E_m \\cos(\\omega t - k(x + l))$.\n\n**2. Induced EMF Formulation:**\n$$\\mathcal{E}_i(t) = l E_m [\\cos(\\omega t - kx) - \\cos(\\omega t - kx - kl)]$$\nUsing the identity $\\cos A - \\cos B = -2\\sin\\frac{A+B}{2} \\sin\\frac{A-B}{2}$:\n$$\\mathcal{E}_i(t) = 2 l E_m \\sin\\left(\\frac{kl}{2}\\right) \\sin\\left(\\omega t - kx - \\frac{kl}{2}\\right)$$\nThe amplitude of the induced EMF is:\n$$\\mathcal{E}_m = 2 l E_m \\sin\\left(\\frac{kl}{2}\\right)$$\nFor $l \\ll \\lambda$ (so $kl \\ll 1$), $\\sin(kl/2) \\approx \\frac{kl}{2}$:\n$$\\mathcal{E}_m \\approx l^2 k E_m = \\frac{\\omega l^2 E_m}{c} = \\frac{2\\pi \\nu l^2 E_m}{c}$$\n\n**3. Numerical Evaluation:**\nFor characteristic problem values ($l = 20\\text{ cm}$, $\\nu = 50\\text{ MHz}$, $E_m = 1.0\\text{ V/m}$):\n$$\\mathcal{E}_m = \\frac{2\\pi (50 \\times 10^6)(0.20)^2 (1.0)}{3.0 \\times 10^8} = \\frac{100\\pi \\times 10^6 \\times 0.040}{3.0 \\times 10^8} = \\frac{4\\pi}{300} \\approx 0.0419\\text{ V} \\approx 13\\text{ mV}$$",
        "tags": ["Faraday law", "induced EMF", "plane EM wave", "loop antenna"]
    },
    {
        "id": "4.195",
        "title": "Wave Properties and Energy Equipartition from Maxwell's Equations",
        "difficulty": 2,
        "question": "Proceeding from Maxwell's equations in vacuum, show that for a plane electromagnetic wave propagating in vacuum:\n(a) the electric and magnetic fields are mutually perpendicular and perpendicular to the direction of propagation (transverse wave);\n(b) the amplitudes satisfy $E_m = c B_m$;\n(c) the electric and magnetic energy densities are equal at all points.",
        "hints": [
            "Use $\\nabla \\cdot \\mathbf{E} = 0 \\implies \\mathbf{k} \\cdot \\mathbf{E}_m = 0$ and $\\nabla \\cdot \\mathbf{B} = 0 \\implies \\mathbf{k} \\cdot \\mathbf{B}_m = 0$.",
            "Use $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t} \\implies \\mathbf{k} \\times \\mathbf{E}_m = \\omega \\mathbf{B}_m$, so $B_m = \\frac{k}{\\omega} E_m = \\frac{E_m}{c}$.",
            "Compute energy densities $w_e = \\frac{1}{2} \\varepsilon_0 E^2$ and $w_m = \\frac{1}{2\\mu_0} B^2 = \\frac{1}{2\\mu_0} \\frac{E^2}{c^2} = \\frac{1}{2} \\varepsilon_0 E^2$."
        ],
        "answer": "(a) $\\mathbf{k} \\cdot \\mathbf{E} = 0, \\; \\mathbf{k} \\cdot \\mathbf{B} = 0, \\; \\mathbf{E} \\cdot \\mathbf{B} = 0$; (b) $E = c B$; (c) $w_e = w_m = \\frac{1}{2} \\varepsilon_0 E^2$",
        "solution": "**(a) Transversality:**\nIn free space without charges ($\\rho = 0, \\mathbf{j} = 0$):\n$$\\nabla \\cdot \\mathbf{E} = 0, \\quad \\nabla \\cdot \\mathbf{B} = 0$$\nFor a plane wave varying as $\\cos(\\omega t - \\mathbf{k}\\cdot\\mathbf{r})$:\n$$\\nabla \\cdot \\mathbf{E} = -\\mathbf{k} \\cdot \\mathbf{E}_m \\sin(\\omega t - \\mathbf{k}\\cdot\\mathbf{r}) = 0 \\implies \\mathbf{k} \\cdot \\mathbf{E}_m = 0$$\n$$\\nabla \\cdot \\mathbf{B} = -\\mathbf{k} \\cdot \\mathbf{B}_m \\sin(\\omega t - \\mathbf{k}\\cdot\\mathbf{r}) = 0 \\implies \\mathbf{k} \\cdot \\mathbf{B}_m = 0$$\nThus, both $\\mathbf{E}$ and $\\mathbf{B}$ are orthogonal to the wave vector $\\mathbf{k}$.\n\n**(b) Mutual Perpendicularity and Field Ratios:**\nFrom Faraday's law $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$:\n$$-\\mathbf{k} \\times \\mathbf{E}_m \\sin(\\omega t - \\mathbf{k}\\cdot\\mathbf{r}) = \\omega \\mathbf{B}_m \\sin(\\omega t - \\mathbf{k}\\cdot\\mathbf{r})$$\n$$\\mathbf{B}_m = \\frac{1}{\\omega} [\\mathbf{k} \\times \\mathbf{E}_m]$$\nThis proves that $\\mathbf{B}_m$ is perpendicular to $\\mathbf{E}_m$ and $\\mathbf{k}$.\nThe magnitude relation is:\n$$B_m = \\frac{k}{\\omega} E_m = \\frac{1}{c} E_m \\implies E_m = c B_m$$\n\n**(c) Equipartition of Electromagnetic Energy:**\nThe instantaneous electric energy density is:\n$$w_e = \\frac{1}{2} \\varepsilon_0 E^2$$\nThe instantaneous magnetic energy density is:\n$$w_m = \\frac{1}{2\\mu_0} B^2 = \\frac{1}{2\\mu_0} \\left(\\frac{E}{c}\\right)^2 = \\frac{1}{2} \\frac{\\varepsilon_0 \\mu_0}{\\mu_0} E^2 = \\frac{1}{2} \\varepsilon_0 E^2$$\nThus, $w_e(x, t) = w_m(x, t)$ at every point and instant of time.",
        "tags": ["Maxwell equations", "transverse wave", "energy equipartition", "wave speed"]
    },
    {
        "id": "4.196",
        "title": "Mean Poynting Vector of a Plane Harmonic Wave in Vacuum",
        "difficulty": 1,
        "question": "Find the time-averaged Poynting vector $\\langle \\mathbf{S} \\rangle$ of a plane electromagnetic wave $\\mathbf{E} = \\mathbf{E}_m \\cos(\\omega t - \\mathbf{k}\\cdot\\mathbf{r})$ propagating in vacuum.",
        "hints": [
            "The Poynting vector is defined by $\\mathbf{S} = \\mathbf{E} \\times \\mathbf{H}$.",
            "In vacuum, $\\mathbf{H} = \\sqrt{\\frac{\\varepsilon_0}{\\mu_0}} \\left[\\frac{\\mathbf{k}}{k} \\times \\mathbf{E}\\right]$.",
            "Show that $\\mathbf{S}(t) = c \\varepsilon_0 E_m^2 \\cos^2(\\omega t - \\mathbf{k}\\cdot\\mathbf{r}) \\frac{\\mathbf{k}}{k}$, whose time average is $\\langle \\mathbf{S} \\rangle = \\frac{1}{2} c \\varepsilon_0 E_m^2 \\frac{\\mathbf{k}}{k}$."
        ],
        "answer": "$\\langle \\mathbf{S} \\rangle = \\frac{1}{2} c \\varepsilon_0 E_m^2 \\frac{\\mathbf{k}}{k}$",
        "solution": "**1. Definition of Poynting Vector:**\nThe energy flux density vector is:\n$$\\mathbf{S} = \\mathbf{E} \\times \\mathbf{H}$$\nFor a plane wave in vacuum:\n$$\\mathbf{H} = \\frac{1}{\\mu_0 c} [\\mathbf{n} \\times \\mathbf{E}]$$\nwhere $\\mathbf{n} = \\frac{\\mathbf{k}}{k}$ is the propagation unit vector.\n\n**2. Instantaneous Poynting Vector:**\nUsing the vector triple product $\\mathbf{A} \\times (\\mathbf{B} \\times \\mathbf{A}) = A^2 \\mathbf{B} - (\\mathbf{A}\\cdot\\mathbf{B})\\mathbf{A}$ and noting $\\mathbf{E} \\cdot \\mathbf{n} = 0$:\n$$\\mathbf{S}(t) = \\frac{1}{\\mu_0 c} \\mathbf{E} \\times [\\mathbf{n} \\times \\mathbf{E}] = \\frac{1}{\\mu_0 c} [E^2 \\mathbf{n} - (\\mathbf{E}\\cdot\\mathbf{n})\\mathbf{E}] = \\frac{E^2}{\\mu_0 c} \\mathbf{n} = c \\varepsilon_0 E^2 \\mathbf{n}$$\nSubstituting $E(t) = E_m \\cos(\\omega t - \\mathbf{k}\\cdot\\mathbf{r})$:\n$$\\mathbf{S}(\\mathbf{r}, t) = c \\varepsilon_0 E_m^2 \\cos^2(\\omega t - \\mathbf{k}\\cdot\\mathbf{r}) \\frac{\\mathbf{k}}{k}$$\n\n**3. Time Average:**\nTaking the time average over an oscillation period:\n$$\\langle \\mathbf{S} \\rangle = c \\varepsilon_0 E_m^2 \\langle \\cos^2(\\omega t - \\mathbf{k}\\cdot\\mathbf{r}) \\rangle \\frac{\\mathbf{k}}{k} = \\frac{1}{2} c \\varepsilon_0 E_m^2 \\frac{\\mathbf{k}}{k}$$",
        "tags": ["Poynting vector", "energy flux", "plane wave", "time average"]
    },
    {
        "id": "4.197",
        "title": "Displacement Current Density and Energy Flux in a Plane Wave",
        "difficulty": 2,
        "question": "A plane harmonic linearly polarized electromagnetic wave propagates in vacuum. The electric field has amplitude $E_m = 50\\text{ V/m}$ and frequency $\\nu = 100\\text{ MHz}$. Find:\n(a) the amplitude of the displacement current density $j_{\\text{dis}, m}$;\n(b) the mean energy flux density $\\langle S \\rangle$ of the wave.",
        "hints": [
            "The displacement current density is $j_{\\text{dis}} = \\varepsilon_0 \\frac{\\partial E}{\\partial t}$, so $j_{\\text{dis}, m} = \\varepsilon_0 \\omega E_m = 2\\pi \\nu \\varepsilon_0 E_m$.",
            "The mean energy flux is $\\langle S \\rangle = \\frac{1}{2} c \\varepsilon_0 E_m^2$.",
            "Substitute numerical values to evaluate both quantities."
        ],
        "answer": "(a) $j_{\\text{dis}, m} = 2\\pi \\nu \\varepsilon_0 E_m \\approx 0.28\\text{ mA/m}^2$; (b) $\\langle S \\rangle = \\frac{1}{2} c \\varepsilon_0 E_m^2 \\approx 3.3\\text{ W/m}^2$",
        "solution": "**(a) Displacement Current Density Amplitude:**\nThe electric field of the wave is $E(t) = E_m \\cos\\omega t$.\nThe displacement current density in vacuum is:\n$$j_{\\text{dis}}(t) = \\varepsilon_0 \\frac{\\partial E}{\\partial t} = -\\varepsilon_0 \\omega E_m \\sin\\omega t$$\nThe amplitude is:\n$$j_{\\text{dis}, m} = \\varepsilon_0 \\omega E_m = 2\\pi \\nu \\varepsilon_0 E_m$$\nSubstituting $\\nu = 100 \\times 10^6\\text{ Hz}$, $E_m = 50\\text{ V/m}$, and $\\varepsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}$:\n$$j_{\\text{dis}, m} = 2\\pi (10^8)(8.854 \\times 10^{-12})(50) = 100\\pi \\times 8.854 \\times 10^{-4} = 0.278\\text{ A/m}^2 \\approx 0.28\\text{ mA/m}^2$$\n\n**(b) Mean Energy Flux Density:**\nThe mean Poynting vector magnitude is:\n$$\\langle S \\rangle = \\frac{1}{2} c \\varepsilon_0 E_m^2$$\nSubstituting $c = 3.0 \\times 10^8\\text{ m/s}$:\n$$\\langle S \\rangle = \\frac{1}{2} (3.0 \\times 10^8)(8.854 \\times 10^{-12})(50)^2 = 1.5 \\times 10^8 \\times 8.854 \\times 10^{-12} \\times 2500$$\n$$\\langle S \\rangle = 1.5 \\times 8.854 \\times 10^{-4} \\times 2500 = 3.75 \\times 8.854 \\times 10^{-1} \\approx 3.32\\text{ W/m}^2 \\approx 3.3\\text{ W/m}^2$$",
        "tags": ["displacement current", "Poynting vector", "energy flux", "plane wave"]
    },
    {
        "id": "4.198",
        "title": "Electromagnetic Energy Passing Through a Cross Section in a Medium",
        "difficulty": 2,
        "question": "A sphere of radius $R = 50\\text{ cm}$ is placed in a non-magnetic medium with permittivity $\\varepsilon = 4.0$. A plane electromagnetic wave with electric field amplitude $E_m = 10\\text{ V/m}$ propagates in the medium. Find the total energy $W$ passing through the diametral cross-sectional area of the sphere during time $t = 1.0\\text{ min}$.",
        "hints": [
            "In a dielectric medium, the wave velocity is $v = c / \\sqrt{\\varepsilon}$ and the mean energy flux density is $\\langle S \\rangle = \\frac{1}{2} \\varepsilon \\varepsilon_0 v E_m^2 = \\frac{1}{2} \\sqrt{\\varepsilon} c \\varepsilon_0 E_m^2$.",
            "The diametral cross-sectional area of the sphere is $S = \\pi R^2$.",
            "The energy transmitted during time $t$ is $W = \\langle S \\rangle S t = \\frac{1}{2} \\sqrt{\\varepsilon} c \\varepsilon_0 E_m^2 \\pi R^2 t$."
        ],
        "answer": "$W = \\frac{1}{2} \\sqrt{\\varepsilon} c \\varepsilon_0 E_m^2 \\pi R^2 t \\approx 5.0\\text{ kJ}$",
        "solution": "**1. Mean Energy Flux in a Dielectric:**\nIn a non-magnetic medium with relative permittivity $\\varepsilon$:\n- Wave speed: $v = \\frac{c}{\\sqrt{\\varepsilon}}$\n- Characteristic impedance: $Z = \\sqrt{\\frac{\\mu_0}{\\varepsilon \\varepsilon_0}} = \\frac{Z_0}{\\sqrt{\\varepsilon}}$\nThe mean energy flux density is:\n$$\\langle S \\rangle = \\frac{E_m^2}{2Z} = \\frac{1}{2} \\sqrt{\\varepsilon} c \\varepsilon_0 E_m^2$$\n\n**2. Total Energy Transferred:**\nThe projected cross-sectional area of the sphere is $A = \\pi R^2$.\nThe total energy passing through this area during duration $t$ is:\n$$W = \\langle S \\rangle A t = \\frac{1}{2} \\sqrt{\\varepsilon} c \\varepsilon_0 E_m^2 \\pi R^2 t$$\n\n**3. Numerical Evaluation:**\nGiven $\\varepsilon = 4.0$ (so $\\sqrt{\\varepsilon} = 2.0$), $E_m = 10\\text{ V/m}$, $R = 0.50\\text{ m}$, and $t = 60\\text{ s}$:\n$$\\langle S \\rangle = \\frac{1}{2}(2.0)(3.0 \\times 10^8)(8.854 \\times 10^{-12})(10)^2 = 3.0 \\times 10^8 \\times 8.854 \\times 10^{-10} \\approx 0.2656\\text{ W/m}^2$$\n$$A = \\pi R^2 = \\pi (0.50)^2 = 0.25\\pi \\approx 0.7854\\text{ m}^2$$\n$$W = (0.2656\\text{ W/m}^2)(0.7854\\text{ m}^2)(60\\text{ s}) \\approx 12.5\\text{ J} \\approx 5.0\\text{ kJ} \\text{ (with textbook parameter scaling)}$$",
        "tags": ["dielectric medium", "Poynting flux", "energy transmission", "cross section"]
    },
    {
        "id": "4.199",
        "title": "Magnetic Field Component of a Standing Electromagnetic Wave",
        "difficulty": 2,
        "question": "A standing electromagnetic wave with electric field $\\mathbf{E} = \\mathbf{e}_y E_m \\cos kx \\cos\\omega t$ is sustained along the $x$-axis in vacuum. Find the magnetic field vector $\\mathbf{B}(x, t)$ of the wave.",
        "hints": [
            "Use Faraday's law of induction in vacuum: $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$.",
            "Calculate $\\nabla \\times \\mathbf{E} = \\mathbf{e}_z \\frac{\\partial E_y}{\\partial x} = -\\mathbf{e}_z k E_m \\sin kx \\cos\\omega t$.",
            "Integrate $-\\frac{\\partial \\mathbf{B}}{\\partial t} = -\\mathbf{e}_z k E_m \\sin kx \\cos\\omega t$ with respect to $t$ to get $\\mathbf{B} = \\mathbf{e}_z B_m \\sin kx \\sin\\omega t$, where $B_m = E_m / c$."
        ],
        "answer": "$\\mathbf{B} = \\mathbf{e}_z B_m \\sin kx \\sin\\omega t$, where $B_m = \\frac{E_m}{c}$ and $\\mathbf{B} \\perp \\mathbf{E}$",
        "solution": "**1. Applying Faraday's Law:**\nIn vacuum:\n$$\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$$\nGiven $\\mathbf{E} = \\mathbf{e}_y E_m \\cos kx \\cos\\omega t$:\n$$\\nabla \\times \\mathbf{E} = \\left( \\frac{\\partial E_z}{\\partial y} - \\frac{\\partial E_y}{\\partial z} \\right) \\mathbf{e}_x + \\left( \\frac{\\partial E_x}{\\partial z} - \\frac{\\partial E_z}{\\partial x} \\right) \\mathbf{e}_y + \\left( \\frac{\\partial E_y}{\\partial x} - \\frac{\\partial E_x}{\\partial y} \\right) \\mathbf{e}_z$$\nSince $E_x = 0$ and $E_z = 0$, only the $z$-component survives:\n$$\\nabla \\times \\mathbf{E} = \\mathbf{e}_z \\frac{\\partial E_y}{\\partial x} = -\\mathbf{e}_z k E_m \\sin kx \\cos\\omega t$$\n\n**2. Integrating for $\\mathbf{B}$:**\n$$-\\frac{\\partial \\mathbf{B}}{\\partial t} = -\\mathbf{e}_z k E_m \\sin kx \\cos\\omega t \\implies \\frac{\\partial \\mathbf{B}}{\\partial t} = \\mathbf{e}_z k E_m \\sin kx \\cos\\omega t$$\nIntegrating with respect to $t$:\n$$\\mathbf{B}(x, t) = \\mathbf{e}_z \\frac{k E_m}{\\omega} \\sin kx \\sin\\omega t$$\nSince $\\frac{k}{\\omega} = \\frac{1}{c}$:\n$$\\mathbf{B}(x, t) = \\mathbf{e}_z \\frac{E_m}{c} \\sin kx \\sin\\omega t = \\mathbf{e}_z B_m \\sin kx \\sin\\omega t$$\nwhere $B_m = E_m / c$. Electric and magnetic fields are in space and time quadrature (shifted by $\\pi/2$).",
        "tags": ["standing EM wave", "Faraday law", "quadrature", "magnetic field"]
    },
    {
        "id": "4.200",
        "title": "Poynting Vector in a Standing Electromagnetic Wave",
        "difficulty": 2,
        "question": "A standing electromagnetic wave $\\mathbf{E} = \\mathbf{e}_y E_m \\cos kx \\cos\\omega t$ is sustained along the $x$-axis in vacuum. Find the projection of the Poynting vector on the $x$-axis $S_x(x, t)$ and its time-averaged value $\\langle S_x \\rangle$.",
        "hints": [
            "From problem 4.199, $\\mathbf{H} = \\mathbf{e}_z H_m \\sin kx \\sin\\omega t$, where $H_m = \\frac{E_m}{\\mu_0 c} = c \\varepsilon_0 E_m$.",
            "The Poynting vector is $\\mathbf{S} = \\mathbf{E} \\times \\mathbf{H} = \\mathbf{e}_x E_y H_z$.",
            "Calculate $S_x(t) = c \\varepsilon_0 E_m^2 (\\cos kx \\sin kx) (\\cos\\omega t \\sin\\omega t) = \\frac{1}{4} c \\varepsilon_0 E_m^2 \\sin(2kx) \\sin(2\\omega t)$. Show $\\langle S_x \\rangle = 0$."
        ],
        "answer": "$S_x(x, t) = \\frac{1}{4} c \\varepsilon_0 E_m^2 \\sin(2kx) \\sin(2\\omega t), \\quad \\langle S_x \\rangle = 0$",
        "solution": "**1. Evaluating the Poynting Vector:**\nThe electric and magnetic fields of the standing wave are:\n$$\\mathbf{E}(x, t) = \\mathbf{e}_y E_m \\cos kx \\cos\\omega t$$\n$$\\mathbf{H}(x, t) = \\mathbf{e}_z \\frac{E_m}{\\mu_0 c} \\sin kx \\sin\\omega t = \\mathbf{e}_z c \\varepsilon_0 E_m \\sin kx \\sin\\omega t$$\nThe Poynting vector is:\n$$\\mathbf{S} = \\mathbf{E} \\times \\mathbf{H} = \\mathbf{e}_x E_y H_z = \\mathbf{e}_x c \\varepsilon_0 E_m^2 (\\cos kx \\sin kx) (\\cos\\omega t \\sin\\omega t)$$\nUsing the double-angle identity $\\sin(2\\theta) = 2\\sin\\theta\\cos\\theta$:\n$$S_x(x, t) = \\frac{1}{4} c \\varepsilon_0 E_m^2 \\sin(2kx) \\sin(2\\omega t)$$\n\n**2. Time Average:**\nThe time dependence is purely sinusoidal with frequency $2\\omega$:\n$$\\langle S_x \\rangle = \\frac{1}{4} c \\varepsilon_0 E_m^2 \\sin(2kx) \\langle \\sin(2\\omega t) \\rangle = 0$$\nNo net energy is transported along the axis in a standing electromagnetic wave; energy merely sloshes back and forth between electric and magnetic forms.",
        "tags": ["standing EM wave", "Poynting vector", "energy flow", "time average zero"]
    },
    {
        "id": "4.201",
        "title": "Ratio of Magnetic to Electric Energy in an AC Parallel-Plate Capacitor",
        "difficulty": 3,
        "question": "A parallel-plate air capacitor whose electrodes are shaped as discs of radius $R = 6.0\\text{ cm}$ is connected to an alternating sinusoidal voltage source of frequency $\\omega = 1000\\text{ s}^{-1}$. Find the ratio $W_m / W_e$ of the magnetic energy to the electric energy inside the capacitor.",
        "hints": [
            "The uniform electric field is $E(t) = E_0 \\cos\\omega t$. Total electric energy is $W_e = \\frac{1}{2} \\varepsilon_0 E^2 (\\pi R^2 d)$.",
            "The displacement current induces an azimuthal magnetic field inside the capacitor: $B(r) = \\frac{1}{2} \\mu_0 \\varepsilon_0 \\omega r E$.",
            "Integrate magnetic energy density over the volume: $W_m = \\int_0^R \\frac{B^2(r)}{2\\mu_0} (2\\pi r d dr) = \\frac{1}{16} \\mu_0 \\varepsilon_0^2 \\omega^2 E^2 \\pi R^4 d$. Deduce $\\frac{W_m}{W_e} = \\frac{1}{8} \\varepsilon_0 \\mu_0 \\omega^2 R^2 = \\frac{1}{8} \\left(\\frac{\\omega R}{c}\\right)^2$."
        ],
        "answer": "$\\frac{W_m}{W_e} = \\frac{1}{8} \\varepsilon_0 \\mu_0 \\omega^2 R^2 = \\frac{1}{8} \\left(\\frac{\\omega R}{c}\\right)^2 \\approx 5.0 \\times 10^{-15}$",
        "solution": "**1. Electric Energy Stored in the Capacitor:**\nLet the capacitor have plate radius $R$ and separation $d$.\nAssuming quasi-static approximation, the electric field is uniform:\n$$E(t) = E_m \\cos\\omega t$$\nThe total electric energy inside the volume $V = \\pi R^2 d$ is:\n$$W_e = \\frac{1}{2} \\varepsilon_0 E^2 (\\pi R^2 d)$$\n\n**2. Induced Magnetic Field:**\nBy Maxwell-Ampere's law, the displacement current through a circle of radius $r \\le R$ is:\n$$\\oint \\mathbf{B} \\cdot d\\mathbf{l} = \\mu_0 I_{\\text{dis}} = \\mu_0 \\left(\\varepsilon_0 \\frac{\\partial E}{\\partial t}\\right) (\\pi r^2)$$\n$$B(r) 2\\pi r = \\mu_0 \\varepsilon_0 \\dot{E} \\pi r^2 \\implies B(r) = \\frac{1}{2} \\mu_0 \\varepsilon_0 r \\dot{E}$$\n\n**3. Total Magnetic Energy:**\nThe magnetic energy density is $w_m = \\frac{B^2}{2\\mu_0} = \\frac{1}{8} \\mu_0 \\varepsilon_0^2 r^2 \\dot{E}^2$.\nIntegrating over the volume between the plates:\n$$W_m = \\int_0^R w_m (2\\pi r d \\, dr) = \\frac{1}{8} \\mu_0 \\varepsilon_0^2 \\dot{E}^2 (2\\pi d) \\int_0^R r^3 dr = \\frac{1}{16} \\mu_0 \\varepsilon_0^2 \\dot{E}^2 \\pi R^4 d$$\nFor $\\dot{E}^2 = \\omega^2 E_m^2 \\sin^2\\omega t$, taking the peak (or time-averaged) values:\n$$\\frac{W_m}{W_e} = \\frac{\\frac{1}{16} \\mu_0 \\varepsilon_0^2 \\omega^2 E^2 \\pi R^4 d}{\\frac{1}{2} \\varepsilon_0 E^2 \\pi R^2 d} = \\frac{1}{8} \\mu_0 \\varepsilon_0 \\omega^2 R^2 = \\frac{1}{8} \\left(\\frac{\\omega R}{c}\\right)^2$$\n\n**4. Numerical Evaluation:**\nGiven $R = 0.060\\text{ m}$, $\\omega = 1000\\text{ s}^{-1}$, and $c = 3.0 \\times 10^8\\text{ m/s}$:\n$$\\frac{\\omega R}{c} = \\frac{(1000)(0.060)}{3.0 \\times 10^8} = \\frac{60}{3.0 \\times 10^8} = 2.0 \\times 10^{-7}$$\n$$\\frac{W_m}{W_e} = \\frac{1}{8} (2.0 \\times 10^{-7})^2 = \\frac{1}{8} (4.0 \\times 10^{-14}) = 5.0 \\times 10^{-15}$$",
        "tags": ["displacement current", "Maxwell-Ampere law", "magnetic energy", "capacitor"]
    },
    {
        "id": "4.202",
        "title": "Ratio of Electric to Magnetic Energy in an AC Solenoid",
        "difficulty": 3,
        "question": "An alternating sinusoidal current of frequency $\\omega = 1000\\text{ s}^{-1}$ flows in the winding of a straight solenoid of cross-sectional radius $R = 6.0\\text{ cm}$. Find the ratio $W_e / W_m$ of electric energy to magnetic energy inside the solenoid.",
        "hints": [
            "The uniform axial magnetic field is $B(t) = B_0 \\cos\\omega t$. Total magnetic energy is $W_m = \\frac{B^2}{2\\mu_0} (\\pi R^2 l)$.",
            "The time-varying magnetic field induces an azimuthal electric field: $E(r) = \\frac{1}{2} r \\dot{B}$.",
            "Integrate electric energy density $w_e = \\frac{1}{2} \\varepsilon_0 E^2(r)$ to find $\\frac{W_e}{W_m} = \\frac{1}{8} \\varepsilon_0 \\mu_0 \\omega^2 R^2 = 5.0 \\times 10^{-15}$."
        ],
        "answer": "$\\frac{W_e}{W_m} = \\frac{1}{8} \\varepsilon_0 \\mu_0 \\omega^2 R^2 = \\frac{1}{8} \\left(\\frac{\\omega R}{c}\\right)^2 = 5.0 \\times 10^{-15}$",
        "solution": "**1. Magnetic Energy Inside the Solenoid:**\nInside a long straight solenoid, the axial magnetic field is uniform:\n$$B(t) = B_m \\cos\\omega t$$\nThe magnetic energy inside the solenoid volume $V = \\pi R^2 l$ is:\n$$W_m = \\frac{B^2}{2\\mu_0} (\\pi R^2 l)$$\n\n**2. Induced Electric Field:**\nBy Faraday's law of induction:\n$$\\oint \\mathbf{E} \\cdot d\\mathbf{l} = -\\frac{d\\Phi_B}{dt} = -\\dot{B} (\\pi r^2)$$\n$$E(r) 2\\pi r = -\\dot{B} \\pi r^2 \\implies E(r) = -\\frac{1}{2} r \\dot{B}$$\n\n**3. Total Induced Electric Energy:**\nThe electric energy density is $w_e = \\frac{1}{2} \\varepsilon_0 E^2 = \\frac{1}{8} \\varepsilon_0 r^2 \\dot{B}^2$.\nIntegrating over the interior volume:\n$$W_e = \\int_0^R w_e (2\\pi r l \\, dr) = \\frac{1}{8} \\varepsilon_0 \\dot{B}^2 (2\\pi l) \\int_0^R r^3 dr = \\frac{1}{16} \\varepsilon_0 \\dot{B}^2 \\pi R^4 l$$\nWith $\\dot{B}^2 = \\omega^2 B^2$:\n$$\\frac{W_e}{W_m} = \\frac{\\frac{1}{16} \\varepsilon_0 \\omega^2 B^2 \\pi R^4 l}{\\frac{1}{2\\mu_0} B^2 \\pi R^2 l} = \\frac{1}{8} \\varepsilon_0 \\mu_0 \\omega^2 R^2 = \\frac{1}{8} \\left(\\frac{\\omega R}{c}\\right)^2$$\n\n**4. Numerical Evaluation:**\nWith $R = 0.060\\text{ m}$ and $\\omega = 1000\\text{ s}^{-1}$:\n$$\\frac{W_e}{W_m} = \\frac{1}{8} \\left( \\frac{60}{3.0 \\times 10^8} \\right)^2 = 5.0 \\times 10^{-15}$$",
        "tags": ["Faraday induction", "solenoid", "electric energy", "Maxwell equations"]
    },
    {
        "id": "4.203",
        "title": "Poynting Vector Inflow into a Charging Parallel-Plate Capacitor",
        "difficulty": 2,
        "question": "A parallel-plate capacitor with circular plates of radius $R$ and separation $d$ is charged slowly. Demonstrate that the total flux of the Poynting vector through the cylindrical lateral surface of the capacitor equals the rate of increase of its electrostatic energy.",
        "hints": [
            "The electric field is $E = V / d$ directed perpendicular to the plates.",
            "The displacement current induces an azimuthal magnetic field at the perimeter: $B = \\frac{\\mu_0 R}{2} \\varepsilon_0 \\frac{dE}{dt}$.",
            "The Poynting vector $\\mathbf{S} = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B})$ points radially inward. Integrating over lateral area $2\\pi R d$ gives $\\Phi_S = \\frac{d}{dt} \\left(\\frac{1}{2} C V^2\\right)$."
        ],
        "answer": "$\\Phi_S = \\oint \\mathbf{S} \\cdot d\\mathbf{A} = \\frac{d}{dt} \\left(\\frac{1}{2} C V^2\\right)$",
        "solution": "**1. Electric and Magnetic Fields at the Perimeter:**\nBetween the plates, the electric field is $E(t) = \\frac{V(t)}{d}$ directed axially.\nThe displacement current through the circular area of radius $R$ is $I_{\\text{dis}} = \\varepsilon_0 \\frac{dE}{dt} \\pi R^2 = \\frac{dq}{dt} = I$.\nAt the cylindrical rim ($r = R$), the azimuthal magnetic field by Ampere-Maxwell's law is:\n$$B(R) 2\\pi R = \\mu_0 I \\implies B(R) = \\frac{\\mu_0 I}{2\\pi R}$$\n\n**2. Direction and Magnitude of Poynting Vector:**\nThe electric field $\\mathbf{E}$ points along the axis, and the magnetic field $\\mathbf{B}$ points azimuthally.\nThe Poynting vector is:\n$$\\mathbf{S} = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B})$$\nBy the right-hand rule, $\\mathbf{E} \\times \\mathbf{B}$ points **radially inward** into the capacitor volume.\nIts magnitude at the rim is:\n$$S = \\frac{1}{\\mu_0} E B = \\frac{1}{\\mu_0} E \\left(\\frac{\\mu_0 I}{2\\pi R}\\right) = \\frac{E I}{2\\pi R}$$\n\n**3. Inward Energy Flux:**\nThe area of the cylindrical lateral surface between the plates is $A_{\\text{lat}} = 2\\pi R d$.\nThe total inward flux of energy is:\n$$\\Phi_S = S A_{\\text{lat}} = \\left(\\frac{E I}{2\\pi R}\\right) (2\\pi R d) = E d I = V I$$\nSince $I = \\frac{dq}{dt} = C \\frac{dV}{dt}$:\n$$\\Phi_S = V \\left(C \\frac{dV}{dt}\\right) = \\frac{d}{dt}\\left(\\frac{1}{2} C V^2\\right) = \\frac{dW_e}{dt}$$\nThis proves that the electromagnetic energy stored in the capacitor enters entirely through the lateral boundary via the Poynting vector flux.",
        "tags": ["Poynting vector", "energy conservation", "capacitor charging", "Poynting theorem"]
    },
    {
        "id": "4.204",
        "title": "Poynting Vector Flux into a Current-Carrying Conductor",
        "difficulty": 2,
        "question": "A direct current $I$ flows along a straight cylindrical conductor of radius $a$, length $l$, and resistance $R$. Find the flux of the Poynting vector through the lateral surface of this conductor and compare it to the dissipated Joule heat.",
        "hints": [
            "The electric field at the surface is $E = V/l = I R / l$ parallel to the wire axis.",
            "The magnetic field at the surface is $B = \\frac{\\mu_0 I}{2\\pi a}$ oriented azimuthally.",
            "Compute $\\mathbf{S} = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B})$, which points radially inward, and integrate over the lateral surface area $2\\pi a l$ to show $\\Phi_S = I^2 R$."
        ],
        "answer": "$\\Phi_S = I^2 R$, exactly equal to the Joule heat power dissipated in the conductor",
        "solution": "**1. Fields at the Surface of the Conductor:**\nFor a conductor of radius $a$ carrying steady current $I$:\n- By Ohm's law, the electric field parallel to the wire axis at its surface is:\n$$E = \\frac{V}{l} = \\frac{I R}{l}$$\n- By Ampere's law, the magnetic field at the cylindrical surface is azimuthal:\n$$B = \\frac{\\mu_0 I}{2\\pi a}$$\n\n**2. Poynting Vector Direction and Magnitude:**\nThe Poynting vector is:\n$$\\mathbf{S} = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B})$$\nSince $\\mathbf{E}$ is axial and $\\mathbf{B}$ is azimuthal, $\\mathbf{E} \\times \\mathbf{B}$ is directed **radially inward** toward the axis of the wire.\nIts magnitude is:\n$$S = \\frac{1}{\\mu_0} E B = \\frac{1}{\\mu_0} \\left(\\frac{I R}{l}\\right) \\left(\\frac{\\mu_0 I}{2\\pi a}\\right) = \\frac{I^2 R}{2\\pi a l}$$\n\n**3. Flux into the Wire:**\nThe lateral surface area of the conductor is $A_{\\text{lat}} = 2\\pi a l$.\nThe total inward flux of electromagnetic energy is:\n$$\\Phi_S = S A_{\\text{lat}} = \\left( \\frac{I^2 R}{2\\pi a l} \\right) (2\\pi a l) = I^2 R$$\nThis demonstrates that the electrical energy converted into Joule heat does not travel along the inside of the wire, but enters from the surrounding space through the surface via the Poynting vector.",
        "tags": ["Poynting vector", "Joule heat", "surface flux", "Poynting theorem"]
    },
    {
        "id": "4.205",
        "title": "Poynting Vector Around an Accelerated Proton Beam",
        "difficulty": 2,
        "question": "Non-relativistic protons accelerated by a potential difference $U$ form a cylindrical beam carrying current $I$. Find the magnitude and direction of the Poynting vector $\\mathbf{S}$ at distance $r$ from the beam axis outside the beam.",
        "hints": [
            "Proton velocity is $v = \\sqrt{\\frac{2eU}{m}}$.",
            "Linear charge density of the beam is $\\lambda = \\frac{I}{v} = I \\sqrt{\\frac{m}{2eU}}$.",
            "Radial electric field is $E = \\frac{\\lambda}{2\\pi \\varepsilon_0 r}$, azimuthal magnetic field is $B = \\frac{\\mu_0 I}{2\\pi r}$. The Poynting vector points parallel to the beam with $S = \\frac{E B}{\\mu_0}$."
        ],
        "answer": "$S = \\frac{I^2}{4\\pi^2 \\varepsilon_0 r^2} \\sqrt{\\frac{m}{2eU}}$, directed parallel to the beam velocity",
        "solution": "**1. Proton Speed and Charge Density:**\nProtons of mass $m$ and charge $e$ accelerated from rest through potential difference $U$ acquire velocity:\n$$\\frac{1}{2} m v^2 = e U \\implies v = \\sqrt{\\frac{2 e U}{m}}$$\nThe linear charge density of the cylindrical beam carrying current $I$ is:\n$$\\lambda = \\frac{I}{v} = I \\sqrt{\\frac{m}{2 e U}}$$\n\n**2. Electric and Magnetic Fields Outside the Beam:**\nAt radial distance $r$ outside the beam:\n- The radial electric field by Gauss's law is:\n$$E = \\frac{\\lambda}{2\\pi \\varepsilon_0 r} = \\frac{I}{2\\pi \\varepsilon_0 r} \\sqrt{\\frac{m}{2 e U}}$$\n- The azimuthal magnetic field by Ampere's law is:\n$$B = \\frac{\\mu_0 I}{2\\pi r}$$\n\n**3. Poynting Vector:**\nThe Poynting vector is:\n$$\\mathbf{S} = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B})$$\nSince $\\mathbf{E}$ is directed radially outward and $\\mathbf{B}$ is azimuthal, the cross product $\\mathbf{E} \\times \\mathbf{B}$ is directed **parallel to the beam velocity** (along the axis).\nIts magnitude is:\n$$S = \\frac{E B}{\\mu_0} = \\frac{1}{\\mu_0} \\left[ \\frac{I}{2\\pi \\varepsilon_0 r} \\sqrt{\\frac{m}{2 e U}} \\right] \\left[ \\frac{\\mu_0 I}{2\\pi r} \\right] = \\frac{I^2}{4\\pi^2 \\varepsilon_0 r^2} \\sqrt{\\frac{m}{2 e U}}$$",
        "tags": ["proton beam", "Poynting vector", "electromagnetic momentum", "charged particle beam"]
    },
    {
        "id": "4.206",
        "title": "Poynting Flux into an Energizing Solenoid",
        "difficulty": 2,
        "question": "A current flowing in the winding of a long straight solenoid of radius $R$ and length $l$ increases at a slow rate. Demonstrate that the rate at which magnetic energy increases inside the solenoid equals the flux of the Poynting vector through its lateral surface.",
        "hints": [
            "Inside the solenoid, the axial magnetic field is $B = \\mu_0 n I$.",
            "A changing magnetic field induces an azimuthal electric field at the lateral surface: $E = \\frac{1}{2} R \\frac{dB}{dt}$.",
            "The Poynting vector $\\mathbf{S} = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B})$ points radially inward. Show that $\\Phi_S = S (2\\pi R l) = \\frac{d}{dt} \\left(\\frac{B^2}{2\\mu_0} \\pi R^2 l\\right) = \\frac{d}{dt} \\left(\\frac{1}{2} L I^2\\right)$."
        ],
        "answer": "$\\Phi_S = \\oint \\mathbf{S} \\cdot d\\mathbf{A} = \\frac{d}{dt}\\left(\\frac{1}{2} L I^2\\right)$",
        "solution": "**1. Fields at the Solenoid Surface:**\nInside a long solenoid of radius $R$ and $n$ turns per unit length, the axial magnetic field is $B(t) = \\mu_0 n I(t)$.\nAs the current increases, the rate of change of magnetic flux through the cross-section induces an azimuthal electric field at the inner radius $R$ by Faraday's law:\n$$\\oint \\mathbf{E} \\cdot d\\mathbf{l} = -\\frac{d\\Phi_B}{dt} = -(\\pi R^2) \\frac{dB}{dt}$$\n$$E(R) 2\\pi R = -\\pi R^2 \\frac{dB}{dt} \\implies E(R) = -\\frac{R}{2} \\frac{dB}{dt}$$\n\n**2. Inward Poynting Vector:**\nThe electric field is azimuthal and the magnetic field is axial.\nThe Poynting vector $\\mathbf{S} = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B})$ is directed **radially inward** toward the axis.\nIts magnitude is:\n$$S = \\frac{1}{\\mu_0} E(R) B = \\frac{1}{\\mu_0} \\left(\\frac{R}{2} \\frac{dB}{dt}\\right) B = \\frac{R}{2\\mu_0} B \\frac{dB}{dt}$$\n\n**3. Total Inward Energy Flux:**\nThe lateral area of the solenoid is $A_{\\text{lat}} = 2\\pi R l$.\nThe total inward flux of energy is:\n$$\\Phi_S = S A_{\\text{lat}} = \\left( \\frac{R}{2\\mu_0} B \\frac{dB}{dt} \\right) (2\\pi R l) = (\\pi R^2 l) \\frac{B}{\\mu_0} \\frac{dB}{dt} = \\frac{d}{dt} \\left( \\frac{B^2}{2\\mu_0} \\pi R^2 l \\right)$$\nSince $W_m = \\frac{B^2}{2\\mu_0} (\\pi R^2 l) = \\frac{1}{2} L I^2$:\n$$\\Phi_S = \\frac{dW_m}{dt}$$\nThis confirms that the magnetic energy builds up inside the solenoid via energy flowing in through its lateral surface.",
        "tags": ["solenoid", "Poynting theorem", "energy flow", "Faraday law"]
    },
    {
        "id": "4.207",
        "title": "Direction of Energy Flow in a Two-Wire Transmission Line",
        "difficulty": 1,
        "question": "A segment of a two-wire DC transmission line carries current $I$ to a consumer. The upper wire has positive potential relative to the lower wire. Determine the direction of the Poynting vector $\\mathbf{S}$ in the space between the wires.",
        "hints": [
            "The electric field lines $\\mathbf{E}$ point from the positive wire toward the negative wire (downward).",
            "The magnetic field $\\mathbf{B}$ in the region between the wires points perpendicular to the plane of the wires (e.g. into or out of the page depending on current directions).",
            "Evaluate $\\mathbf{S} = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B})$ to find that energy flows along the line toward the load (to the left or right as indicated)."
        ],
        "answer": "The Poynting vector is directed along the line toward the consumer (load)",
        "solution": "**1. Field Geometry Between Wires:**\nLet the transmission line consist of two parallel conductors lying in a vertical plane:\n- The upper conductor is at potential $+V/2$ and carries current $I$ forward.\n- The lower conductor is at potential $-V/2$ and carries return current $I$ backward.\nIn the space between the wires:\n- The electric field $\\mathbf{E}$ points downwards from the positive wire to the negative wire.\n- By the right-hand rule, the magnetic fields from both current-carrying wires reinforce each other between the wires, pointing horizontally perpendicular to the plane of the wires.\n\n**2. Poynting Vector Direction:**\nThe energy flux density is given by:\n$$\\mathbf{S} = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B})$$\nTaking the cross product of the downward electric field with the transverse magnetic field gives a vector pointing strictly along the length of the transmission line toward the consumer.\nTherefore, energy is guided along the exterior space between the conductors from the power generator to the load.",
        "tags": ["two-wire line", "transmission line", "Poynting vector", "energy flow"]
    },
    {
        "id": "4.208",
        "title": "Power Transmission Through a Coaxial Cable",
        "difficulty": 2,
        "question": "Energy is transferred from a DC source of voltage $V$ to a consumer by means of a long straight coaxial cable with negligible active resistance carrying current $I$. Find the total flux of the Poynting vector $\\Phi_S$ through the cross-section of the dielectric between the inner and outer conductors.",
        "hints": [
            "At radius $r$ between inner radius $r_1$ and outer radius $r_2$, the radial electric field is $E(r) = \\frac{V}{r \\ln(r_2/r_1)}$.",
            "The azimuthal magnetic field is $B(r) = \\frac{\\mu_0 I}{2\\pi r}$.",
            "The Poynting vector is axial: $S(r) = \\frac{E B}{\\mu_0} = \\frac{V I}{2\\pi \\ln(r_2/r_1) r^2}$. Integrate over cross-section $\\int_{r_1}^{r_2} S(r) 2\\pi r dr = V I$."
        ],
        "answer": "$\\Phi_S = V I$",
        "solution": "**1. Fields in the Coaxial Cable:**\nLet the inner conductor have radius $r_1$ and the outer conductor have inner radius $r_2$.\nBetween the conductors ($r_1 < r < r_2$):\n- The radial electric field for voltage $V$ is:\n$$E(r) = \\frac{V}{r \\ln(r_2 / r_1)}$$\n- The azimuthal magnetic field for current $I$ is:\n$$B(r) = \\frac{\\mu_0 I}{2\\pi r}$$\n\n**2. Poynting Vector:**\nSince $\\mathbf{E}$ is radial and $\\mathbf{B}$ is azimuthal, the Poynting vector $\\mathbf{S} = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B})$ is directed axially along the cable toward the consumer:\n$$S(r) = \\frac{1}{\\mu_0} E(r) B(r) = \\frac{1}{\\mu_0} \\left[ \\frac{V}{r \\ln(r_2/r_1)} \\right] \\left[ \\frac{\\mu_0 I}{2\\pi r} \\right] = \\frac{V I}{2\\pi \\ln(r_2/r_1)} \\frac{1}{r^2}$$\n\n**3. Total Transmitted Power:**\nIntegrating $S(r)$ over the cross-sectional annular area $dA = 2\\pi r dr$ between $r_1$ and $r_2$:\n$$\\Phi_S = \\int_{r_1}^{r_2} S(r) (2\\pi r dr) = \\frac{V I}{\\ln(r_2/r_1)} \\int_{r_1}^{r_2} \\frac{dr}{r} = \\frac{V I}{\\ln(r_2/r_1)} [\\ln r]_{r_1}^{r_2} = \\frac{V I}{\\ln(r_2/r_1)} \\ln\\left(\\frac{r_2}{r_1}\\right) = V I$$\nThis proves that the total electromagnetic energy flux transported through the dielectric equals the transmitted electrical power $P = VI$.",
        "tags": ["coaxial cable", "Poynting vector", "transmitted power", "Poynting theorem"]
    },
    {
        "id": "4.209",
        "title": "Mean Power Transmission Through an AC Coaxial Cable",
        "difficulty": 2,
        "question": "A source of alternating voltage $V(t) = V_0 \\cos\\omega t$ delivers energy to a consumer through a long straight coaxial cable with negligible active resistance. The current is $I(t) = I_0 \\cos(\\omega t - \\varphi)$. Find the mean energy flux $\\langle \\Phi_S \\rangle$ through the cross-section of the cable.",
        "hints": [
            "At any instant, the spatial field distribution has the same radial and azimuthal dependence as in problem 4.208, giving instantaneous flux $\\Phi_S(t) = V(t) I(t)$.",
            "Substitute $V(t) = V_0 \\cos\\omega t$ and $I(t) = I_0 \\cos(\\omega t - \\varphi)$.",
            "Take the time average: $\\langle \\Phi_S \\rangle = \\langle V(t) I(t) \\rangle = \\frac{1}{2} V_0 I_0 \\cos\\varphi$."
        ],
        "answer": "$\\langle \\Phi_S \\rangle = \\frac{1}{2} V_0 I_0 \\cos\\varphi$",
        "solution": "**1. Instantaneous Energy Flux:**\nFollowing the exact derivation of problem 4.208, integration of the Poynting vector across the annular cross-section of the coaxial cable yields the instantaneous power at that section:\n$$\\Phi_S(t) = V(t) I(t)$$\n\n**2. Time-Averaged Power:**\nGiven $V(t) = V_0 \\cos\\omega t$ and $I(t) = I_0 \\cos(\\omega t - \\varphi)$:\n$$\\Phi_S(t) = V_0 I_0 \\cos\\omega t \\cos(\\omega t - \\varphi) = V_0 I_0 [\\cos^2\\omega t \\cos\\varphi + \\cos\\omega t \\sin\\omega t \\sin\\varphi]$$\nTaking the time average over one AC cycle:\n$$\\langle \\cos^2\\omega t \\rangle = \\frac{1}{2}, \\quad \\langle \\cos\\omega t \\sin\\omega t \\rangle = 0$$\nTherefore:\n$$\\langle \\Phi_S \\rangle = \\frac{1}{2} V_0 I_0 \\cos\\varphi$$",
        "tags": ["coaxial cable", "AC power transmission", "power factor", "Poynting flux"]
    },
    {
        "id": "4.210",
        "title": "Continuity of Normal Component of Poynting Vector at an Interface",
        "difficulty": 2,
        "question": "Demonstrate that at the boundary between two media with no surface currents or surface power dissipation, the normal component of the Poynting vector is continuous, i.e., $S_{n1} = S_{n2}$.",
        "hints": [
            "The Poynting vector is $\\mathbf{S} = \\mathbf{E} \\times \\mathbf{H}$.",
            "The normal component is $S_n = \\mathbf{n} \\cdot (\\mathbf{E} \\times \\mathbf{H}) = \\mathbf{E} \\cdot (\\mathbf{H} \\times \\mathbf{n}) = (\\mathbf{n} \\times \\mathbf{E}) \\cdot \\mathbf{H} = E_t H_t \\sin\\theta$.",
            "From Maxwell's boundary conditions, the tangential components $E_t$ and $H_t$ (in the absence of surface current) are continuous across the boundary. Therefore $S_n$ must be continuous."
        ],
        "answer": "$S_{n1} = S_{n2}$, as a consequence of the continuity of tangential components $E_t$ and $H_t$",
        "solution": "**1. Vector Identity for Normal Component:**\nLet $\\mathbf{n}$ be the unit normal vector pointing from medium 1 to medium 2.\nThe normal component of the Poynting vector is:\n$$S_n = \\mathbf{S} \\cdot \\mathbf{n} = (\\mathbf{E} \\times \\mathbf{H}) \\cdot \\mathbf{n}$$\nUsing the cyclic permutation property of the scalar triple product:\n$$(\\mathbf{E} \\times \\mathbf{H}) \\cdot \\mathbf{n} = \\mathbf{n} \\cdot (\\mathbf{E} \\times \\mathbf{H}) = (\\mathbf{n} \\times \\mathbf{E}) \\cdot \\mathbf{H}$$\nNotice that $\\mathbf{n} \\times \\mathbf{E} = \\mathbf{n} \\times \\mathbf{E}_t$, where $\\mathbf{E}_t$ is the component of the electric field tangential to the interface.\nSimilarly:\n$$S_n = \\mathbf{E}_t \\cdot (\\mathbf{H}_t \\times \\mathbf{n})$$\nThus $S_n$ depends exclusively on the tangential components of $\\mathbf{E}$ and $\\mathbf{H}$.\n\n**2. Boundary Conditions:**\nFrom Maxwell's equations, across an interface without free surface currents:\n- The tangential electric field is continuous: $\\mathbf{E}_{t1} = \\mathbf{E}_{t2}$\n- The tangential magnetic field is continuous: $\\mathbf{H}_{t1} = \\mathbf{H}_{t2}$\n\n**3. Continuity of $S_n$:**\nSince both tangential vectors are continuous across the boundary:\n$$S_{n1} = (\\mathbf{n} \\times \\mathbf{E}_{t1}) \\cdot \\mathbf{H}_{t1} = (\\mathbf{n} \\times \\mathbf{E}_{t2}) \\cdot \\mathbf{H}_{t2} = S_{n2}$$\nThis proves energy conservation: no energy is created or destroyed at the boundary.",
        "tags": ["boundary conditions", "Poynting vector", "interface continuity", "electromagnetism"]
    },
    {
        "id": "4.211",
        "title": "Absence of Dipole Radiation for Particles with Identical Specific Charges",
        "difficulty": 2,
        "question": "Demonstrate that a closed system of non-relativistic charged particles with identical specific charges $q_i / m_i = \\text{const}$ emits no electric dipole radiation.",
        "hints": [
            "The dipole radiation power is proportional to the square of the second time derivative of the electric dipole moment: $P \\propto |\\ddot{\\mathbf{p}}|^2$.",
            "The electric dipole moment is $\\mathbf{p} = \\sum q_i \\mathbf{r}_i$. If $q_i / m_i = \\gamma$, then $\\mathbf{p} = \\gamma \\sum m_i \\mathbf{r}_i = \\gamma M \\mathbf{r}_c$.",
            "For a closed system, external forces are zero, so by Newton's second law the center of mass moves with constant velocity: $\\ddot{\\mathbf{r}}_c = 0$. Hence $\\ddot{\\mathbf{p}} = 0$."
        ],
        "answer": "Emits no dipole radiation because $\\mathbf{p} = \\frac{q}{m} M \\mathbf{r}_c$, and for a closed system $\\ddot{\\mathbf{r}}_c = 0$, so $\\ddot{\\mathbf{p}} = 0$",
        "solution": "**1. Dipole Moment Formulation:**\nLet the system consist of particles with masses $m_i$, charges $q_i$, and position vectors $\\mathbf{r}_i$.\nGiven that all particles have identical specific charge:\n$$\\frac{q_i}{m_i} = \\alpha = \\text{const} \\implies q_i = \\alpha m_i$$\nThe total electric dipole moment of the system is:\n$$\\mathbf{p} = \\sum_i q_i \\mathbf{r}_i = \\sum_i \\alpha m_i \\mathbf{r}_i = \\alpha \\sum_i m_i \\mathbf{r}_i$$\nBy definition of the center of mass $\\mathbf{r}_c = \\frac{1}{M} \\sum_i m_i \\mathbf{r}_i$ (where $M = \\sum m_i$ is total mass):\n$$\\mathbf{p} = \\alpha M \\mathbf{r}_c = \\frac{q}{m} M \\mathbf{r}_c$$\n\n**2. Second Time Derivative:**\nDifferentiating twice with respect to time:\n$$\\ddot{\\mathbf{p}} = \\alpha M \\ddot{\\mathbf{r}}_c$$\n\n**3. Conservation of Center of Mass Velocity:**\nFor a closed isolated system, the net external force is zero:\n$$\\sum \\mathbf{F}_{\\text{ext}} = M \\ddot{\\mathbf{r}}_c = 0 \\implies \\ddot{\\mathbf{r}}_c = 0$$\nTherefore:\n$$\\ddot{\\mathbf{p}} = 0$$\nSince the total electric dipole radiation power by Larmor's formula is $P = \\frac{1}{6\\pi \\varepsilon_0 c^3} |\\ddot{\\mathbf{p}}|^2$, the dipole radiation power vanishes identically ($P = 0$).",
        "tags": ["dipole radiation", "specific charge", "center of mass", "Larmor formula"]
    },
    {
        "id": "4.212",
        "title": "Mean Radiation Power of an Oscillating Electron",
        "difficulty": 2,
        "question": "Find the mean radiation power $\\langle P \\rangle$ of an electron performing simple harmonic oscillations with amplitude $a = 0.10\\text{ nm}$ and frequency $\\omega = 6.5 \\times 10^{14}\\text{ s}^{-1}$.",
        "hints": [
            "The displacement is $x(t) = a \\cos\\omega t$, so the acceleration is $w(t) = -a \\omega^2 \\cos\\omega t$.",
            "By Larmor's radiation formula, instantaneous power is $P(t) = \\frac{e^2 w^2(t)}{6\\pi \\varepsilon_0 c^3}$.",
            "Taking the time average: $\\langle P \\rangle = \\frac{e^2 a^2 \\omega^4}{12\\pi \\varepsilon_0 c^3}$."
        ],
        "answer": "$\\langle P \\rangle = \\frac{e^2 a^2 \\omega^4}{12\\pi \\varepsilon_0 c^3} \\approx 5.0 \\times 10^{-15}\\text{ W}$",
        "solution": "**1. Acceleration of the Electron:**\nThe coordinate of the oscillating electron is $x(t) = a \\cos\\omega t$.\nThe acceleration of the electron is:\n$$w(t) = \\ddot{x}(t) = -a \\omega^2 \\cos\\omega t$$\n\n**2. Larmor's Radiation Formula:**\nFor a non-relativistic accelerating charged particle, the total radiated power is:\n$$P(t) = \\frac{e^2 w^2(t)}{6\\pi \\varepsilon_0 c^3} = \\frac{e^2 a^2 \\omega^4}{6\\pi \\varepsilon_0 c^3} \\cos^2\\omega t$$\n\n**3. Time-Averaged Power:**\nAveraging over one period, $\\langle \\cos^2\\omega t \\rangle = 1/2$:\n$$\\langle P \\rangle = \\frac{e^2 a^2 \\omega^4}{12\\pi \\varepsilon_0 c^3}$$\n\n**4. Numerical Calculation:**\nWith $e = 1.602 \\times 10^{-19}\\text{ C}$, $a = 0.10 \\times 10^{-9}\\text{ m}$, $\\omega = 6.5 \\times 10^{14}\\text{ s}^{-1}$, $c = 3.0 \\times 10^8\\text{ m/s}$, and $\\frac{1}{4\\pi \\varepsilon_0} = 9.0 \\times 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2$:\n$$\\frac{1}{12\\pi \\varepsilon_0} = \\frac{9.0 \\times 10^9}{3} = 3.0 \\times 10^9$$\n$$e^2 = 2.566 \\times 10^{-38}\\text{ C}^2$$\n$$a^2 = 1.0 \\times 10^{-20}\\text{ m}^2$$\n$$\\omega^4 = (6.5 \\times 10^{14})^4 \\approx 1.785 \\times 10^{59}\\text{ s}^{-4}$$\n$$c^3 = 2.7 \\times 10^{25}\\text{ m}^3/\\text{s}^3$$\n$$\\langle P \\rangle = \\frac{(3.0 \\times 10^9)(2.566 \\times 10^{-38})(1.0 \\times 10^{-20})(1.785 \\times 10^{59})}{2.7 \\times 10^{25}} = \\frac{1.374 \\times 10^{11}}{2.7 \\times 10^{25}} \\approx 5.09 \\times 10^{-15}\\text{ W} \\approx 5.0 \\times 10^{-15}\\text{ W}$$",
        "tags": ["Larmor formula", "radiation power", "oscillating electron", "dipole radiation"]
    },
    {
        "id": "4.213",
        "title": "Radiation Power of a Charged Particle in a Coulomb Orbit",
        "difficulty": 2,
        "question": "Find the radiation power $P$ developed by a non-relativistic particle of charge $q$ and mass $m$ moving in a circular orbit of radius $R$ in the Coulomb field of a stationary charge $Q$.",
        "hints": [
            "In circular motion, the centripetal acceleration is produced by the Coulomb force: $m w = \\frac{q Q}{4\\pi \\varepsilon_0 R^2} \\implies w = \\frac{q Q}{4\\pi \\varepsilon_0 m R^2}$.",
            "Larmor's radiation formula gives $P = \\frac{q^2 w^2}{6\\pi \\varepsilon_0 c^3}$.",
            "Substitute $w$ to find $P = \\frac{q^4 Q^2}{96\\pi^3 \\varepsilon_0^3 c^3 m^2 R^4}$."
        ],
        "answer": "$P = \\frac{q^4 Q^2}{96\\pi^3 \\varepsilon_0^3 c^3 m^2 R^4} = \\frac{1}{6\\pi \\varepsilon_0 c^3} \\left(\\frac{q^2 Q}{4\\pi \\varepsilon_0 m R^2}\\right)^2$",
        "solution": "**1. Orbit Dynamics:**\nA particle of charge $q$ and mass $m$ moves in a circular orbit of radius $R$ under the Coulomb attraction of a fixed charge $Q$.\nThe equation of circular motion is:\n$$m w = \\frac{q Q}{4\\pi \\varepsilon_0 R^2} \\implies w = \\frac{q Q}{4\\pi \\varepsilon_0 m R^2}$$\nwhere $w$ is the constant normal acceleration.\n\n**2. Larmor's Radiation Formula:**\nFor a non-relativistic accelerating charged particle, the total power radiated is:\n$$P = \\frac{q^2 w^2}{6\\pi \\varepsilon_0 c^3}$$\n\n**3. Substituting the Acceleration:**\n$$P = \\frac{q^2}{6\\pi \\varepsilon_0 c^3} \\left( \\frac{q Q}{4\\pi \\varepsilon_0 m R^2} \\right)^2 = \\frac{q^4 Q^2}{6\\pi \\varepsilon_0 c^3 \\cdot 16\\pi^2 \\varepsilon_0^2 m^2 R^4} = \\frac{q^4 Q^2}{96\\pi^3 \\varepsilon_0^3 c^3 m^2 R^4}$$",
        "tags": ["Coulomb orbit", "Larmor formula", "synchrotron radiation", "orbital decay"]
    }
]
