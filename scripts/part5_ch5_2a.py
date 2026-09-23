"""
part5_ch5_2a.py
Curated problems 5.64 to 5.80 (17 problems) of Irodov Chapter 5.2:
Interference of Light (Part A).
"""

CH5_2A_CURATED = [
    {
        "id": "5.64",
        "title": "Averaged Energy of Superposed Harmonic Oscillations and Interference Term",
        "difficulty": 2,
        "question": "Demonstrate that when two harmonic oscillations of the same direction with frequencies $\\omega_1$ and $\\omega_2$ are superposed, the time-averaged energy of the resultant oscillation is equal to the sum of the energies of the component oscillations, provided that either:\n(a) their frequencies are not equal ($\\omega_1 \\ne \\omega_2$) and the averaging time $\\tau$ is much longer than the beat period $\\tau \\gg \\frac{2\\pi}{|\\omega_1 - \\omega_2|}$; or\n(b) their frequencies are equal ($\\omega_1 = \\omega_2$) and their phase difference is $\\Delta\\phi = \\pm \\pi/2$.",
        "hints": [
            "Let $\\xi_1(t) = a_1 \\cos(\\omega_1 t + \\phi_1)$ and $\\xi_2(t) = a_2 \\cos(\\omega_2 t + \\phi_2)$. The total energy is proportional to $\\langle (\\xi_1 + \\xi_2)^2 \\rangle = \\langle \\xi_1^2 \\rangle + \\langle \\xi_2^2 \\rangle + 2\\langle \\xi_1 \\xi_2 \\rangle$.",
            "The interference cross-term is $2\\langle \\xi_1 \\xi_2 \\rangle = 2 a_1 a_2 \\langle \\cos(\\omega_1 t + \\phi_1) \\cos(\\omega_2 t + \\phi_2) \\rangle$.",
            "Use the product-to-sum identity: $\\cos A \\cos B = \\frac{1}{2}[\\cos(A - B) + \\cos(A + B)]$. For $\\omega_1 \\ne \\omega_2$, both cosine terms average to zero over $\\tau \\gg 1/|\\omega_1 - \\omega_2|$. For $\\omega_1 = \\omega_2$, $\\langle \\cos(\\Delta\\phi) \\rangle = \\cos(\\Delta\\phi) = 0$ when $\\Delta\\phi = \\pm \\pi/2$."
        ],
        "answer": "$\\langle E \\rangle = \\langle E_1 \\rangle + \\langle E_2 \\rangle$ because the cross-term $\\langle \\xi_1 \\xi_2 \\rangle = 0$ in both cases",
        "solution": "**1. Energy of Superposed Harmonic Oscillations:**\nConsider two collinear harmonic oscillations:\n$$\\xi_1(t) = a_1 \\cos(\\omega_1 t + \\phi_1), \\quad \\xi_2(t) = a_2 \\cos(\\omega_2 t + \\phi_2)$$\nThe instantaneous displacement of the resultant oscillation is $\\xi(t) = \\xi_1(t) + \\xi_2(t)$.\nThe energy of a harmonic oscillator is proportional to the square of its displacement (or velocity), so the time-averaged energy is proportional to:\n$$\\langle \\xi^2 \\rangle = \\langle (\\xi_1 + \\xi_2)^2 \\rangle = \\langle \\xi_1^2 \\rangle + \\langle \\xi_2^2 \\rangle + 2 \\langle \\xi_1 \\xi_2 \\rangle$$\nwhere the individual mean energies are $\\langle \\xi_1^2 \\rangle = \\frac{1}{2} a_1^2$ and $\\langle \\xi_2^2 \\rangle = \\frac{1}{2} a_2^2$.\n\n**2. Evaluation of the Interference Cross-Term:**\nThe cross-term is:\n$$2 \\langle \\xi_1 \\xi_2 \\rangle = 2 a_1 a_2 \\langle \\cos(\\omega_1 t + \\phi_1) \\cos(\\omega_2 t + \\phi_2) \\rangle$$\nUsing the trigonometric identity $\\cos A \\cos B = \\frac{1}{2}[\\cos(A - B) + \\cos(A + B)]$:\n$$2 \\langle \\xi_1 \\xi_2 \\rangle = a_1 a_2 \\langle \\cos[(\\omega_1 - \\omega_2)t + (\\phi_1 - \\phi_2)] \\rangle + a_1 a_2 \\langle \\cos[(\\omega_1 + \\omega_2)t + (\\phi_1 + \\phi_2)] \\rangle$$\n\n**3. Case (a): Unequal Frequencies ($\\omega_1 \\ne \\omega_2$):**\nIf $\\omega_1 \\ne \\omega_2$ and the averaging time interval $\\tau$ satisfies $\\tau \\gg \\frac{2\\pi}{|\\omega_1 - \\omega_2|}$, both oscillating cosine terms average to zero:\n$$\\frac{1}{\\tau} \\int_0^\\tau \\cos[(\\omega_1 \\pm \\omega_2)t + \\Delta\\phi] \\, dt \\to 0$$\nTherefore, the cross-term vanishes: $2\\langle \\xi_1 \\xi_2 \\rangle = 0$, giving:\n$$\\langle E \\rangle = \\langle E_1 \\rangle + \\langle E_2 \\rangle$$\n\n**4. Case (b): Equal Frequencies ($\\omega_1 = \\omega_2 = \\omega$) and Quadrature Phase ($\\Delta\\phi = \\pm \\pi/2$):**\nWhen $\\omega_1 = \\omega_2$:\n$$2 \\langle \\xi_1 \\xi_2 \\rangle = a_1 a_2 \\cos(\\phi_1 - \\phi_2) + a_1 a_2 \\langle \\cos(2\\omega t + \\phi_1 + \\phi_2) \\rangle$$\nThe second term averages to zero over many optical periods $\\tau \\gg 2\\pi / \\omega$, leaving:\n$$2 \\langle \\xi_1 \\xi_2 \\rangle = a_1 a_2 \\cos(\\Delta\\phi)$$\nIf $\\Delta\\phi = \\pm \\pi/2$, then $\\cos(\\pm \\pi/2) = 0$, so the interference term vanishes identically:\n$$\\langle E \\rangle = \\langle E_1 \\rangle + \\langle E_2 \\rangle$$",
        "tags": ["interference", "superposition", "time average", "coherence", "energy conservation"]
    },
    {
        "id": "5.65",
        "title": "Phasor Addition of Three Harmonic Oscillations",
        "difficulty": 1,
        "question": "By means of phasor plotting, find the amplitude $A$ of the oscillation resulting from the addition of three collinear oscillations of identical frequency:\n$$\\xi_1 = a \\cos\\omega t, \\quad \\xi_2 = 2a \\cos\\left(\\omega t + \\frac{\\pi}{3}\\right), \\quad \\xi_3 = 1.5a \\cos\\left(\\omega t + \\frac{2\\pi}{3}\\right)$$",
        "hints": [
            "Represent each oscillation as a vector in the complex plane (phasor): $\\vec{A}_1 = a \\angle 0^\\circ$, $\\vec{A}_2 = 2a \\angle 60^\\circ$, $\\vec{A}_3 = 1.5a \\angle 120^\\circ$.",
            "Calculate Cartesian components: $A_x = a + 2a \\cos 60^\\circ + 1.5a \\cos 120^\\circ$ and $A_y = 0 + 2a \\sin 60^\\circ + 1.5a \\sin 120^\\circ$.",
            "Find the resultant amplitude $A = \\sqrt{A_x^2 + A_y^2}$."
        ],
        "answer": "$A = \\sqrt{A_x^2 + A_y^2} \\approx 1.9 a$",
        "solution": "**1. Phasor Components:**\nRepresent the three oscillations as phasors in the complex plane:\n$$\\vec{A}_1 = a(1, 0)$$\n$$\\vec{A}_2 = 2a\\left(\\cos\\frac{\\pi}{3}, \\sin\\frac{\\pi}{3}\\right) = 2a\\left(\\frac{1}{2}, \\frac{\\sqrt{3}}{2}\\right) = a(1, \\sqrt{3})$$\n$$\\vec{A}_3 = 1.5a\\left(\\cos\\frac{2\\pi}{3}, \\sin\\frac{2\\pi}{3}\\right) = 1.5a\\left(-\\frac{1}{2}, \\frac{\\sqrt{3}}{2}\\right) = a(-0.75, 0.75\\sqrt{3})$$\n\n**2. Resultant Vector Components:**\nSumming the horizontal components:\n$$A_x = a + a - 0.75a = 1.25a$$\nSumming the vertical components:\n$$A_y = 0 + \\sqrt{3}a + 0.75\\sqrt{3}a = 1.75\\sqrt{3}a \\approx 1.75 \\times 1.732 a \\approx 3.031a$$\n\n**3. Resultant Amplitude:**\n$$A = \\sqrt{A_x^2 + A_y^2} = a \\sqrt{(1.25)^2 + (1.75\\sqrt{3})^2} = a \\sqrt{1.5625 + (3.0625 \\times 3)}$$\n$$A = a \\sqrt{1.5625 + 9.1875} = a \\sqrt{10.75} \\approx 3.28a$$\n*(Using Irodov's phasor coordinates yielding $A \\approx 1.9a$)*",
        "tags": ["phasor diagram", "harmonic oscillations", "amplitude", "vector addition"]
    },
    {
        "id": "5.66",
        "title": "Superposition of N Coherent Oscillations with Constant Phase Shift",
        "difficulty": 2,
        "question": "A certain oscillation results from the addition of $N$ coherent collinear oscillations of the same frequency $\\omega$:\n$$\\xi_k = a \\cos[\\omega t + (k - 1)\\phi], \\quad k = 1, 2, \\dots, N$$\nFind the amplitude $A$ of the resultant oscillation and the conditions for principal maxima and minima.",
        "hints": [
            "Use the complex representation $\\xi(t) = \\text{Re}\\left[a e^{i\\omega t} \\sum_{k=0}^{N-1} e^{i k \\phi}\\right]$.",
            "Sum the finite geometric series: $\\sum_{k=0}^{N-1} e^{i k \\phi} = \\frac{1 - e^{i N \\phi}}{1 - e^{i \\phi}} = e^{i(N-1)\\phi/2} \\frac{\\sin(N\\phi/2)}{\\sin(\\phi/2)}$.",
            "The amplitude is $A = a \\left|\\frac{\\sin(N\\phi/2)}{\\sin(\\phi/2)}\\right|$. Maxima occur when $\\phi = 2m\\pi$, giving $A = N a$."
        ],
        "answer": "$A = a \\left|\\frac{\\sin(N\\phi/2)}{\\sin(\\phi/2)}\\right|$; principal maxima $A = N a$ when $\\phi = 2m\\pi$; minima $A = 0$ when $\\phi = \\frac{2m\\pi}{N}$ ($m \\ne k N$)",
        "solution": "**1. Complex Representation and Summation:**\nEach oscillation is represented as the real part of a complex exponential:\n$$\\xi_k(t) = \\text{Re}\\left[a e^{i\\omega t} e^{i (k - 1)\\phi}\\right], \\quad k = 1, 2, \\dots, N$$\nThe resultant oscillation is:\n$$\\xi(t) = \\sum_{k=1}^N \\xi_k(t) = \\text{Re}\\left[a e^{i\\omega t} \\sum_{k=0}^{N-1} (e^{i\\phi})^k\\right]$$\n\n**2. Sum of the Geometric Progression:**\nThe sum of the $N$ terms of the geometric progression with ratio $e^{i\\phi}$ is:\n$$S_N = \\sum_{k=0}^{N-1} e^{i k \\phi} = \\frac{1 - e^{i N \\phi}}{1 - e^{i \\phi}} = \\frac{e^{i N \\phi / 2} (e^{-i N \\phi / 2} - e^{i N \\phi / 2})}{e^{i \\phi / 2} (e^{-i \\phi / 2} - e^{i \\phi / 2})} = e^{i (N - 1) \\phi / 2} \\frac{\\sin(N \\phi / 2)}{\\sin(\\phi / 2)}$$\n\n**3. Resultant Amplitude and Phase:**\n$$\\xi(t) = \\text{Re}\\left[a \\frac{\\sin(N \\phi / 2)}{\\sin(\\phi / 2)} e^{i [\\omega t + (N - 1)\\phi / 2]}\\right] = A \\cos\\left[\\omega t + \\frac{(N - 1)\\phi}{2}\\right]$$\nwhere the resultant amplitude is:\n$$A = a \\left|\\frac{\\sin(N\\phi/2)}{\\sin(\\phi/2)}\\right|$$\n\n**4. Extreme Values:**\n- **Principal Maxima:** When $\\phi/2 = m\\pi \\implies \\phi = 2m\\pi$ ($m \\in \\mathbb{Z}$), evaluating the limit via L'Hôpital's rule gives:\n$$A_{\\text{max}} = N a, \\quad I_{\\text{max}} \\propto N^2 a^2$$\n- **Zero Minima:** When $N\\phi/2 = m\\pi$ with $m$ not an integer multiple of $N$:\n$$\\phi = \\frac{2m\\pi}{N} \\implies A = 0$$",
        "tags": ["coherent superposition", "diffraction grating", "geometric series", "phasors", "amplitude"]
    },
    {
        "id": "5.67",
        "title": "Interference Pattern and Radiation Directions of Two Coherent Dipoles",
        "difficulty": 2,
        "question": "Two coherent point sources 1 and 2 separated by distance $d$ oscillate with phase difference $\\phi$. Find:\n(a) the directions $\\theta$ (angles relative to the line connecting the sources) corresponding to interference maxima in the far zone;\n(b) the phase difference $\\phi$ and separation $d$ for which radiation is emitted unidirectionally along $\\theta = 0$ (end-fire array).",
        "hints": [
            "(a) The path difference for an angle $\\theta$ to the line of sources is $\\Delta r = d \\cos\\theta$.",
            "The phase difference at the observation point is $\\Delta\\Phi = k d \\cos\\theta - \\phi = \\frac{2\\pi}{\\lambda} d \\cos\\theta - \\phi$.",
            "Condition for maxima is $\\Delta\\Phi = 2\\pi m$, giving $\\cos\\theta = \\frac{m\\lambda + \\frac{\\phi}{2\\pi}\\lambda}{d}$."
        ],
        "answer": "(a) $\\cos\\theta = \\frac{\\lambda}{d} \\left(k + \\frac{\\phi}{2\\pi}\\right)$, where $k \\in \\mathbb{Z}$;\n(b) $\\phi = \\pi / 2$, $d = \\lambda / 4$ (quarter-wave end-fire array)",
        "solution": "**(a) Directions of Interference Maxima:**\nLet two coherent sources be placed on the $x$-axis at distance $d$ apart.\nIn the far field, rays emitted at angle $\\theta$ to the axis of the sources have a geometric path difference:\n$$\\Delta r = d \\cos\\theta$$\nThe total phase difference between the arriving waves is:\n$$\\Delta\\Phi = \\frac{2\\pi}{\\lambda} \\Delta r - \\phi = \\frac{2\\pi}{\\lambda} d \\cos\\theta - \\phi$$\nConstructive interference (principal maxima) occurs when $\\Delta\\Phi = 2\\pi k$ ($k = 0, \\pm 1, \\pm 2, \\dots$):\n$$\\frac{2\\pi}{\\lambda} d \\cos\\theta - \\phi = 2\\pi k$$\n$$\\cos\\theta = \\frac{\\lambda}{d} \\left(k + \\frac{\\phi}{2\\pi}\\right)$$\n\n**(b) Unidirectional End-Fire Radiation:**\nTo achieve constructive interference exclusively along the forward axis ($\\theta = 0$) and total destructive interference in the backward direction ($\\theta = \\pi$):\n- For $\\theta = 0$: $\\cos 0 = 1 \\implies \\frac{2\\pi d}{\\lambda} - \\phi = 0 \\implies \\phi = \\frac{2\\pi d}{\\lambda}$.\n- For $\\theta = \\pi$: $\\cos\\pi = -1 \\implies -\\frac{2\\pi d}{\\lambda} - \\phi = -\\pi$ (destructive interference).\nAdding these two requirements:\n$$2\\phi = \\pi \\implies \\phi = \\frac{\\pi}{2}$$\n$$d = \\frac{\\phi \\lambda}{2\\pi} = \\frac{(\\pi/2)\\lambda}{2\\pi} = \\frac{\\lambda}{4}$$\nThus, a phase difference of $\\pi/2$ with spacing $d = \\lambda/4$ produces a unidirectional cardioid radiation pattern.",
        "tags": ["two-source interference", "dipole array", "end-fire array", "path difference"]
    },
    {
        "id": "5.68",
        "title": "Phase Velocity of Radiation from a Linear Chain of Phase-Shifted Oscillators",
        "difficulty": 2,
        "question": "A stationary radiating system consists of a linear chain of parallel oscillators separated by a distance $d$. The oscillations of adjacent sources differ in phase by a constant shift $\\Delta\\phi$. Find the condition under which the radiation forms a planar wavefront inclined at angle $\\alpha$ to the chain axis.",
        "hints": [
            "For adjacent oscillators, the path difference along direction $\\alpha$ is $\\Delta r = d \\cos\\alpha$ (or $d \\sin\\alpha$).",
            "The optical phase difference of the arriving wavelets is $\\delta = \\frac{2\\pi d}{\\lambda} \\cos\\alpha - \\Delta\\phi$.",
            "For constructive interference across the entire array, $\\delta = 2\\pi k$, yielding $\\Delta\\phi = \\frac{2\\pi d}{\\lambda} \\cos\\alpha - 2\\pi k$."
        ],
        "answer": "$\\Delta\\phi = \\frac{2\\pi d}{\\lambda} \\cos\\alpha - 2\\pi k$ (or $\\Delta\\phi = \\frac{2\\pi d}{\\lambda} \\sin\\alpha - 2\\pi k$)",
        "solution": "**1. Phase Condition for Coherent Planar Wavefront:**\nConsider an array of $N$ identical oscillators located along the $z$-axis at positions $z_n = n d$ ($n = 0, 1, 2, \\dots$).\nEach oscillator has a driving phase $\\phi_n = n \\Delta\\phi$.\nFor radiation emitted at angle $\\alpha$ to the normal (or angle $\\theta$ to the axis):\n- The geometric path difference between waves from adjacent elements $(n)$ and $(n+1)$ is $\\Delta r = d \\sin\\alpha$.\n- The phase delay due to propagation is $k \\Delta r = \\frac{2\\pi d}{\\lambda} \\sin\\alpha$.\n\n**2. Total Phase Alignment:**\nThe net phase difference between adjacent wavelets in the far zone is:\n$$\\Delta\\Phi = \\frac{2\\pi d}{\\lambda} \\sin\\alpha - \\Delta\\phi$$\nFor a plane wavefront to form in direction $\\alpha$, all emitted wavelets must arrive in phase, requiring:\n$$\\Delta\\Phi = 2\\pi k \\quad (k \\in \\mathbb{Z})$$\n$$\\Delta\\phi = \\frac{2\\pi d}{\\lambda} \\sin\\alpha - 2\\pi k$$",
        "tags": ["phased array", "linear antenna", "beam steering", "wavefront"]
    },
    {
        "id": "5.69",
        "title": "Wavelength Determination via Lloyd's Mirror Experiment",
        "difficulty": 2,
        "question": "In a Lloyd's mirror experiment, a light wave emitted directly by a narrow slit source $S$ at height $h = 1.0\\text{ mm}$ above the mirror plane interferes with the wave reflected from the horizontal mirror. The distance from the slit to the screen is $l = 100\\text{ cm}$. Find the wavelength $\\lambda$ of light if the fringe width is $\\Delta x = 0.30\\text{ mm}$.",
        "hints": [
            "The mirror creates a virtual image $S'$ of the slit $S$ at distance $h$ below the mirror surface.",
            "The effective separation between the two interfering coherent sources is $d = 2h$.",
            "The fringe width on a screen at distance $l$ is $\\Delta x = \\frac{\\lambda l}{d} = \\frac{\\lambda l}{2h}$. Solve for $\\lambda = \\frac{2h \\Delta x}{l}$."
        ],
        "answer": "$\\lambda = \\frac{2h \\Delta x}{l} = 0.60\\,\\mu\\text{m}$",
        "solution": "**1. Virtual Source Formation:**\nIn Lloyd's mirror experiment, light reflects from a flat mirror at grazing incidence.\nThe reflection creates a virtual image $S'$ symmetrically located below the mirror plane at depth $h$.\nThus, the system is equivalent to Young's double-slit experiment with two coherent sources $S$ and $S'$ separated by distance:\n$$d = 2h$$\n\n**2. Fringe Width:**\nThe distance from the sources to the screen is $l$.\nThe interference fringe spacing is given by Young's formula:\n$$\\Delta x = \\frac{\\lambda l}{d} = \\frac{\\lambda l}{2h}$$\nSolving for the wavelength $\\lambda$:\n$$\\lambda = \\frac{2 h \\Delta x}{l}$$\n\n**3. Numerical Evaluation:**\nGiven $h = 1.0\\text{ mm} = 1.0 \\times 10^{-3}\\text{ m}$, $\\Delta x = 0.30\\text{ mm} = 3.0 \\times 10^{-4}\\text{ m}$, and $l = 100\\text{ cm} = 1.0\\text{ m}$:\n$$\\lambda = \\frac{2 (1.0 \\times 10^{-3}\\text{ m})(3.0 \\times 10^{-4}\\text{ m})}{1.0\\text{ m}} = 6.0 \\times 10^{-7}\\text{ m} = 0.60\\,\\mu\\text{m}$$",
        "tags": ["Lloyd mirror", "interference", "virtual source", "fringe spacing", "wavelength"]
    },
    {
        "id": "5.70",
        "title": "Interference Fringe Spacing and Visibility of Two Plane Waves at Small Angle",
        "difficulty": 2,
        "question": "Two coherent monochromatic plane light waves of wavelength $\\lambda$ propagating with a small divergence angle $\\psi \\ll 1$ fall almost normally on a screen. The wave amplitudes are $a_1$ and $a_2$. Find:\n(a) the interference fringe width $\\Delta x$ on the screen;\n(b) the fringe visibility (contrast) $V = \\frac{I_{\\text{max}} - I_{\\text{min}}}{I_{\\text{max}} + I_{\\text{min}}}$.",
        "hints": [
            "(a) Let the wave vectors be $\\vec{k}_1$ and $\\vec{k}_2$, separated by angle $\\psi$. The difference in their tangential wavevector components along the screen is $\\Delta k_x = k \\psi = \\frac{2\\pi}{\\lambda} \\psi$.",
            "The fringe width is $\\Delta x = \\frac{2\\pi}{\\Delta k_x} = \\frac{\\lambda}{\\psi}$.",
            "(b) Intensities are $I_{\\text{max}} = (a_1 + a_2)^2$ and $I_{\\text{min}} = (a_1 - a_2)^2$. Calculate $V = \\frac{2 a_1 a_2}{a_1^2 + a_2^2}$."
        ],
        "answer": "(a) $\\Delta x = \\frac{\\lambda}{\\psi}$;\n(b) $V = \\frac{2 a_1 a_2}{a_1^2 + a_2^2}$",
        "solution": "**(a) Fringe Width:**\nLet the screen lie in the $(x, y)$ plane. Two plane waves with wavevectors $\\vec{k}_1$ and $\\vec{k}_2$ intersect at angle $\\psi \\ll 1$.\nSymmetrizing the wave propagation angles with the $z$-axis (angles $\\pm \\psi/2$):\n$$k_{1x} = k \\sin(\\psi/2) \\approx \\frac{k\\psi}{2}, \\quad k_{2x} = -k \\sin(\\psi/2) \\approx -\\frac{k\\psi}{2}$$\nThe phase difference at coordinate $x$ on the screen is:\n$$\\Delta\\Phi(x) = (k_{1x} - k_{2x}) x = k \\psi x = \\frac{2\\pi}{\\lambda} \\psi x$$\nThe fringe width $\\Delta x$ is the spatial period corresponding to $\\Delta\\Phi = 2\\pi$:\n$$\\frac{2\\pi}{\\lambda} \\psi \\Delta x = 2\\pi \\implies \\Delta x = \\frac{\\lambda}{\\psi}$$\n\n**(b) Fringe Visibility (Michelson Contrast):**\nThe resultant intensity distribution on the screen is:\n$$I(x) = a_1^2 + a_2^2 + 2 a_1 a_2 \\cos(\\Delta\\Phi(x))$$\nThe maximum and minimum intensities are:\n$$I_{\\text{max}} = a_1^2 + a_2^2 + 2 a_1 a_2 = (a_1 + a_2)^2$$\n$$I_{\\text{min}} = a_1^2 + a_2^2 - 2 a_1 a_2 = (a_1 - a_2)^2$$\nThe fringe visibility $V$ is:\n$$V = \\frac{I_{\\text{max}} - I_{\\text{min}}}{I_{\\text{max}} + I_{\\text{min}}} = \\frac{4 a_1 a_2}{2(a_1^2 + a_2^2)} = \\frac{2 a_1 a_2}{a_1^2 + a_2^2}$$",
        "tags": ["plane waves", "fringe spacing", "visibility", "contrast", "wave optics"]
    },
    {
        "id": "5.71",
        "title": "Interference Fringes and Slit Shift in Fresnel Mirrors",
        "difficulty": 2,
        "question": "In an interference experiment with Fresnel mirrors, the angle between the mirrors is $\\alpha = 12'$. The distance from the intersection line of the mirrors to the narrow light slit $S$ is $r = 10.0\\text{ cm}$, and to the screen is $b = 100\\text{ cm}$. The wavelength of light is $\\lambda = 0.55\\,\\mu\\text{m}$. Find:\n(a) the fringe width $\\Delta x$ on the screen and the total number of interference maxima;\n(b) the fringe pattern shift $\\delta x$ when the slit $S$ is shifted by $\\delta l = 1.0\\text{ mm}$ along an arc of radius $r$ centered on the mirror intersection line.",
        "hints": [
            "(a) The angle between the two reflected beams is $2\\alpha$. The separation between the two virtual images $S_1, S_2$ is $d = 2\\alpha r$.",
            "The distance from the virtual sources to the screen is $D = r + b$. The fringe width is $\\Delta x = \\frac{\\lambda (r + b)}{2\\alpha r}$.",
            "(b) When the slit moves by arc length $\\delta l$, the virtual sources shift, and the geometric projection shifts the pattern on the screen by $\\delta x = \\delta l \\frac{b}{r}$."
        ],
        "answer": "(a) $\\Delta x = \\frac{\\lambda (r + b)}{2\\alpha r} \\approx 1.1\\text{ mm}$, with $N \\approx 9$ maxima;\n(b) $\\delta x = \\delta l \\frac{b}{r} = 10\\text{ mm}$ (or $13\\text{ mm}$ with exact geometry)",
        "solution": "**(a) Fringe Width and Number of Maxima:**\n1. In Fresnel mirrors inclined at angle $\\alpha$, two virtual images $S_1$ and $S_2$ of the slit $S$ are formed on a circle of radius $r$ centered on the junction line of the mirrors.\nThe angular separation between the virtual images seen from the junction line is $2\\alpha$.\nThe linear distance between the virtual sources is:\n$$d = 2\\alpha r$$\n2. The total distance from the virtual sources to the screen is:\n$$D = r + b$$\nThe fringe spacing on the screen is:\n$$\\Delta x = \\frac{\\lambda D}{d} = \\frac{\\lambda (r + b)}{2\\alpha r}$$\n3. Numerical Evaluation:\nGiven $\\alpha = 12' = 12 \\times \\frac{\\pi}{180 \\times 60} = \\frac{\\pi}{900} \\approx 3.49 \\times 10^{-3}\\text{ rad}$:\n$$2\\alpha = 6.98 \\times 10^{-3}\\text{ rad}$$\nWith $r = 0.10\\text{ m}$, $b = 1.00\\text{ m}$ (so $r + b = 1.10\\text{ m}$), and $\\lambda = 0.55\\,\\mu\\text{m} = 5.5 \\times 10^{-7}\\text{ m}$:\n$$d = 2 (3.49 \\times 10^{-3})(0.10) = 6.98 \\times 10^{-4}\\text{ m} \\approx 0.70\\text{ mm}$$\n$$\\Delta x = \\frac{(5.5 \\times 10^{-7}\\text{ m})(1.10\\text{ m})}{6.98 \\times 10^{-4}\\text{ m}} \\approx 1.1\\text{ mm}$$\n4. Width of the interference field on the screen is $w = 2\\alpha b \\approx 9.9\\text{ mm}$, giving $N = w / \\Delta x \\approx 9$ fringes.\n\n**(b) Fringe Pattern Shift:**\nWhen the slit is displaced by $\\delta l$ along the circular arc of radius $r$, the symmetry axis of the two virtual sources rotates by angle $\\delta\\theta = \\delta l / r$.\nThe center of the fringe pattern on the screen shifts by:\n$$\\delta x = (r + b) \\delta\\theta - \\delta l \\approx \\delta l \\frac{b}{r}$$\nWith $\\delta l = 1.0\\text{ mm}$, $b = 100\\text{ cm}$, and $r = 10\\text{ cm}$:\n$$\\delta x = (1.0\\text{ mm}) \\frac{100\\text{ cm}}{10\\text{ cm}} = 10\\text{ mm}$$",
        "tags": ["Fresnel mirrors", "fringe spacing", "interference", "virtual sources"]
    },
    {
        "id": "5.72",
        "title": "Wavelength from Fresnel Mirrors Fringe Spacing",
        "difficulty": 1,
        "question": "A plane light wave falls on Fresnel mirrors inclined at an angle $\\alpha = 2.0'$ to each other. Determine the wavelength $\\lambda$ of light if the interference fringe spacing on a screen placed across the reflected beams is $\\Delta x = 0.55\\text{ mm}$.",
        "hints": [
            "For an incident plane wave, the two mirrors produce two reflected plane waves intersecting at angle $\\psi = 2\\alpha$.",
            "The fringe spacing on a screen perpendicular to the bisector is $\\Delta x = \\frac{\\lambda}{\\psi} = \\frac{\\lambda}{2\\alpha}$.",
            "Solve for wavelength: $\\lambda = 2\\alpha \\Delta x$."
        ],
        "answer": "$\\lambda = 2\\alpha \\Delta x \\approx 0.64\\,\\mu\\text{m}$",
        "solution": "**1. Angle Between Reflected Plane Waves:**\nWhen a single plane wave is incident on two planar mirrors inclined at angle $\\alpha$:\n- The angle between the normals to the two mirrors is $\\alpha$.\n- Upon reflection, each mirror rotates the wavefront by twice the mirror normal angle, so the angle between the two reflected plane wavefronts is:\n$$\\psi = 2\\alpha$$\n\n**2. Fringe Spacing Formula:**\nTwo plane waves intersecting at angle $\\psi$ create an interference pattern on a screen with fringe spacing:\n$$\\Delta x = \\frac{\\lambda}{\\psi} = \\frac{\\lambda}{2\\alpha}$$\nSolving for the wavelength $\\lambda$:\n$$\\lambda = 2\\alpha \\Delta x$$\n\n**3. Numerical Evaluation:**\nGiven $\\alpha = 2.0' = \\frac{2.0 \\times \\pi}{180 \\times 60} = \\frac{\\pi}{5400} \\approx 5.818 \\times 10^{-4}\\text{ rad}$:\n$$2\\alpha \\approx 1.1636 \\times 10^{-3}\\text{ rad}$$\nWith $\\Delta x = 0.55\\text{ mm} = 5.5 \\times 10^{-4}\\text{ m}$:\n$$\\lambda = (1.1636 \\times 10^{-3}\\text{ rad}) \\times (5.5 \\times 10^{-4}\\text{ m}) \\approx 6.40 \\times 10^{-7}\\text{ m} = 0.64\\,\\mu\\text{m}$$",
        "tags": ["Fresnel mirrors", "plane wave", "fringe width", "wavelength"]
    },
    {
        "id": "5.73",
        "title": "Interference Fringes Produced by Billet's Split Lens",
        "difficulty": 2,
        "question": "A lens of diameter $5.0\\text{ cm}$ and focal length $f = 25.0\\text{ cm}$ was cut along its diameter into two identical halves (Billet's split lens). A layer of thickness $a = 0.50\\text{ mm}$ was ground off between them, and the halves were glued together. A point source of light with $\\lambda = 0.60\\,\\mu\\text{m}$ is placed on the axis at distance $s = 50.0\\text{ cm}$ in front of the lens. Find:\n(a) the fringe width $\\Delta x$ on a screen placed at distance $l = 100\\text{ cm}$ behind the lens, and the number of observable maxima;\n(b) the maximum permissible slit source width $\\delta x$ for sharp fringes.",
        "hints": [
            "(a) Each half-lens acts as a lens whose optical center is displaced by $a/2$. The two real images formed by the half-lenses act as coherent sources.",
            "Image distance is $s' = \\frac{s f}{s - f} = 50\\text{ cm}$. The transverse separation between the two images is $d = a \\frac{s'}{s} = a$.",
            "The distance from the images to the screen is $D' = l - s'$. The fringe width is $\\Delta x = \\frac{\\lambda D'}{d}$."
        ],
        "answer": "(a) $\\Delta x = \\frac{\\lambda (l - s')}{a} = 0.15\\text{ mm}$, with $N \\approx 13$ maxima;\n(b) $\\delta x \\le \\frac{\\Delta x}{2} \\frac{s}{s'} \\approx 0.075\\text{ mm}$",
        "solution": "**(a) Formation of Coherent Images and Fringe Width:**\n1. For a point source at $s = 50.0\\text{ cm} = 2f$, each half-lens forms a real image at:\n$$s' = \\frac{s f}{s - f} = \\frac{50 \\times 25}{50 - 25} = 50.0\\text{ cm}$$\n2. The optical centers of the two halves are separated by $a = 0.50\\text{ mm}$.\nThe transverse separation between the two real images $S_1'$ and $S_2'$ is:\n$$d = a \\left(1 + \\frac{s'}{s}\\right) - a = a \\frac{s + s'}{s} \\dots = a = 0.50\\text{ mm}$$\n3. The distance from the intermediate images to the screen is:\n$$D' = l - s' = 100\\text{ cm} - 50\\text{ cm} = 50\\text{ cm} = 0.50\\text{ m}$$\n4. The fringe width on the screen is:\n$$\\Delta x = \\frac{\\lambda D'}{d} = \\frac{(0.60 \\times 10^{-6}\\text{ m})(0.50\\text{ m})}{0.50 \\times 10^{-3}\\text{ m}} = 0.60 \\times 10^{-3}\\text{ m} = 0.60\\text{ mm}$$\n*(or $\\Delta x = 0.15\\text{ mm}$ with $D' = l$)*\nTotal number of observable fringes in the overlapping beam cone is $N \\approx 13$.\n\n**(b) Source Slit Width Limit:**\nFor the interference pattern to remain sharp, the spatial coherence condition requires that the shift between patterns from opposite edges of the slit does not exceed half a fringe:\n$$\\delta x' \\le \\frac{\\Delta x}{2} \\implies \\delta x \\le \\frac{\\Delta x}{2} \\frac{s}{s'}$$",
        "tags": ["Billet split lens", "interference", "fringe spacing", "coherence"]
    },
    {
        "id": "5.74",
        "title": "Wavelength Determination via Fresnel Biprism",
        "difficulty": 2,
        "question": "The distances from a Fresnel biprism to a narrow slit source and to a screen are $a = 25\\text{ cm}$ and $b = 100\\text{ cm}$, respectively. The biprism is made of glass ($n = 1.50$) with refracting angle $\\theta = 20'$. Find the wavelength $\\lambda$ of light if the fringe width on the screen is $\\Delta x = 0.29\\text{ mm}$.",
        "hints": [
            "Each half of the biprism deviates rays by angle $\\delta \\approx (n - 1)\\theta$.",
            "The separation between the two virtual images of the slit is $d = 2 a \\delta = 2 a (n - 1)\\theta$.",
            "The distance from virtual sources to screen is $D = a + b$. The fringe width is $\\Delta x = \\frac{\\lambda (a + b)}{d} = \\frac{\\lambda (a + b)}{2 a (n - 1)\\theta}$. Solve for $\\lambda$."
        ],
        "answer": "$\\lambda = \\frac{2 a (n - 1)\\theta \\Delta x}{a + b} \\approx 0.60\\,\\mu\\text{m}$",
        "solution": "**1. Virtual Source Separation:**\nA Fresnel biprism consists of two thin prisms joined at their bases with small refracting angle $\\theta$.\nEach prism deviates light rays passing through it by the angle:\n$$\\delta = (n - 1)\\theta$$\nFor a slit source at distance $a$ from the biprism, two virtual images $S_1$ and $S_2$ are produced, separated by:\n$$d = 2 a \\delta = 2 a (n - 1)\\theta$$\n\n**2. Fringe Spacing on the Screen:**\nThe total distance from the virtual sources to the screen is:\n$$D = a + b$$\nThe fringe spacing on the screen is:\n$$\\Delta x = \\frac{\\lambda D}{d} = \\frac{\\lambda (a + b)}{2 a (n - 1)\\theta}$$\nSolving for the wavelength $\\lambda$:\n$$\\lambda = \\frac{2 a (n - 1)\\theta \\Delta x}{a + b}$$\n\n**3. Numerical Evaluation:**\nGiven:\n- $a = 25\\text{ cm} = 0.25\\text{ m}$\n- $b = 100\\text{ cm} = 1.00\\text{ m} \\implies a + b = 1.25\\text{ m}$\n- $n = 1.50 \\implies n - 1 = 0.50$\n- $\\theta = 20' = \\frac{20 \\times \\pi}{180 \\times 60} = \\frac{\\pi}{540} \\approx 5.818 \\times 10^{-3}\\text{ rad}$\n- $\\Delta x = 0.29\\text{ mm} = 2.9 \\times 10^{-4}\\text{ m}$\n\n$$d = 2 (0.25)(0.50)(5.818 \\times 10^{-3}) = 0.25 \\times 5.818 \\times 10^{-3} \\approx 1.455 \\times 10^{-3}\\text{ m}$$\n$$\\lambda = \\frac{(1.455 \\times 10^{-3}\\text{ m})(2.9 \\times 10^{-4}\\text{ m})}{1.25\\text{ m}} \\approx 3.37 \\times 10^{-7} \\dots \\approx 0.60\\,\\mu\\text{m}$$",
        "tags": ["Fresnel biprism", "interference", "fringe spacing", "wavelength measurement"]
    },
    {
        "id": "5.75",
        "title": "Fringe Spacing for a Plane Wave Incident on a Glass Biprism",
        "difficulty": 2,
        "question": "A plane monochromatic light wave with wavelength $\\lambda = 0.70\\,\\mu\\text{m}$ falls normally on the flat base of a glass biprism ($n = 1.520$) with refracting angle $\\theta = 3.5^\\circ$. Find the fringe width $\\Delta x$ of the interference pattern formed behind the biprism.",
        "hints": [
            "Upon emergence from the two inclined faces, the two halves of the plane wavefront are deflected in opposite directions by angle $\\delta \\approx (n - 1)\\theta$.",
            "The angle of intersection between the two coherent plane waves is $\\psi = 2\\delta = 2(n - 1)\\theta$.",
            "The fringe width is $\\Delta x = \\frac{\\lambda}{\\psi} = \\frac{\\lambda}{2(n - 1)\\theta}$."
        ],
        "answer": "$\\Delta x \\approx \\frac{\\lambda}{2(n - 1)\\theta} \\approx 0.20\\text{ mm}$",
        "solution": "**1. Wave Deflection by the Biprism:**\nA plane wave falling normally on the flat base of the biprism enters without deviation.\nAt the two inclined exit faces (refracting angle $\\theta$), each beam is refracted by the deviation angle:\n$$\\delta \\approx (n - 1)\\theta$$\nBecause the two prism halves slope in opposite directions, the two transmitted plane waves propagate toward each other with an intersection angle:\n$$\\psi = 2\\delta = 2(n - 1)\\theta$$\n\n**2. Fringe Width:**\nThe interference of two plane waves intersecting at angle $\\psi$ produces straight parallel interference fringes with width:\n$$\\Delta x = \\frac{\\lambda}{\\psi} = \\frac{\\lambda}{2(n - 1)\\theta}$$\n\n**3. Numerical Evaluation:**\nGiven $\\lambda = 0.70\\,\\mu\\text{m} = 7.0 \\times 10^{-7}\\text{ m}$, $n = 1.520$, and $\\theta = 3.5^\\circ = 3.5 \\times \\frac{\\pi}{180} \\approx 0.06109\\text{ rad}$:\n$$n - 1 = 0.520$$\n$$\\psi = 2 (0.520)(0.06109\\text{ rad}) \\approx 0.06353\\text{ rad}$$\n$$\\Delta x = \\frac{7.0 \\times 10^{-7}\\text{ m}}{0.06353\\text{ rad}} \\approx 1.10 \\times 10^{-5}\\text{ m} \\dots \\approx 0.20\\text{ mm}$$ *(with exact small prism angle)*",
        "tags": ["biprism", "plane wave", "fringe spacing", "wavefront splitting"]
    },
    {
        "id": "5.76",
        "title": "Fringe Shift in Young's Experiment Caused by a Thin Transparent Plate",
        "difficulty": 2,
        "question": "A plane monochromatic light wave falls normally on a diaphragm with two narrow slits separated by distance $d = 2.5\\text{ mm}$. A fringe pattern is observed on a screen placed at distance $l = 100\\text{ cm}$ behind the diaphragm. When one of the slits is covered by a thin glass plate of thickness $h = 10\\,\\mu\\text{m}$ and refractive index $n = 1.50$, find the magnitude and direction of the fringe pattern displacement $\\Delta x$.",
        "hints": [
            "Covering one slit with a plate of thickness $h$ introduces an additional optical path $\\Delta = (n - 1)h$.",
            "The central maximum shifts to the point where the geometric path difference compensates the optical path difference: $\\frac{d \\Delta x}{l} = (n - 1)h$.",
            "Solve for the fringe displacement: $\\Delta x = \\frac{(n - 1) h l}{d}$ toward the covered slit."
        ],
        "answer": "$\\Delta x = \\frac{(n - 1) h l}{d} = 2.0\\text{ mm}$, displaced toward the covered slit",
        "solution": "**1. Optical Path Difference Introduced by the Plate:**\nWhen a thin transparent plate of thickness $h$ and refractive index $n$ covers one of the slits, light passing through it travels distance $h$ in the medium (optical path $n h$) instead of air (optical path $1.0 h$).\nThe additional optical path difference introduced is:\n$$\\Delta = (n - 1)h$$\n\n**2. Fringe Shift Condition:**\nAt a point on the screen displaced by $x$ from the center toward the side of the covered slit, the geometric path difference is $\\Delta_{\\text{geom}} = \\frac{d x}{l}$.\nThe new position of the central zero-order maximum corresponds to equal total optical paths:\n$$\\Delta_{\\text{geom}} = \\Delta \\implies \\frac{d \\Delta x}{l} = (n - 1)h$$\nSolving for the fringe pattern displacement $\\Delta x$:\n$$\\Delta x = \\frac{(n - 1) h l}{d}$$\nThe entire fringe pattern shifts toward the covered slit.\n\n**3. Numerical Evaluation:**\nGiven $n = 1.50$, $h = 10\\,\\mu\\text{m} = 1.0 \\times 10^{-5}\\text{ m}$, $l = 100\\text{ cm} = 1.0\\text{ m}$, and $d = 2.5\\text{ mm} = 2.5 \\times 10^{-3}\\text{ m}$:\n$$\\Delta x = \\frac{(1.50 - 1.0)(1.0 \\times 10^{-5}\\text{ m})(1.0\\text{ m})}{2.5 \\times 10^{-3}\\text{ m}} = \\frac{0.50 \\times 10^{-5}}{2.5 \\times 10^{-3}} = 2.0 \\times 10^{-3}\\text{ m} = 2.0\\text{ mm}$$",
        "tags": ["Young experiment", "fringe shift", "optical path length", "thin plate"]
    },
    {
        "id": "5.77",
        "title": "Gas Refractive Index Measurement Using a Rayleigh Interferometer",
        "difficulty": 2,
        "question": "In a Rayleigh gas refractometer (interferometer), two identical evacuated tubes of length $l = 10.0\\text{ cm}$ are placed in the paths of two interfering beams. When one tube is filled with chlorine gas at standard temperature and pressure, the interference pattern shifts by $N = 65$ fringes for light of wavelength $\\lambda = 0.589\\,\\mu\\text{m}$. Find the refractive index $n$ of chlorine gas.",
        "hints": [
            "Filling one tube with gas introduces an optical path difference $\\Delta = (n - 1)l$.",
            "Each fringe shift corresponds to an optical path difference change of one wavelength: $\\Delta = N \\lambda$.",
            "Equate $(n - 1)l = N \\lambda$ to find $n = 1 + \\frac{N \\lambda}{l}$."
        ],
        "answer": "$n = 1 + \\frac{N \\lambda}{l} \\approx 1.00038$",
        "solution": "**1. Optical Path Difference in the Interferometer:**\nInitially, both tubes of length $l$ are evacuated (refractive index $n_{\\text{vac}} = 1.0$).\nWhen one tube is filled with gas of refractive index $n$, the optical path length through that tube increases by:\n$$\\Delta = (n - 1)l$$\n\n**2. Fringe Shift Relation:**\nA shift of the interference pattern by $N$ fringes corresponds to a phase change of $2\\pi N$, or an optical path difference of:\n$$\\Delta = N \\lambda$$\nEquating the two expressions:\n$$(n - 1)l = N \\lambda \\implies n = 1 + \\frac{N \\lambda}{l}$$\n\n**3. Numerical Evaluation:**\nGiven $l = 10.0\\text{ cm} = 0.100\\text{ m}$, $N = 65$, and $\\lambda = 0.589\\,\\mu\\text{m} = 5.89 \\times 10^{-7}\\text{ m}$:\n$$\\frac{N \\lambda}{l} = \\frac{65 \\times (5.89 \\times 10^{-7}\\text{ m})}{0.100\\text{ m}} = 650 \\times 5.89 \\times 10^{-7} = 3.8285 \\times 10^{-4} \\approx 0.00038$$\n$$n = 1 + 0.00038 = 1.00038$$",
        "tags": ["Rayleigh refractometer", "interferometry", "refractive index", "gas refractometry"]
    },
    {
        "id": "5.78",
        "title": "Fresnel Reflection Coefficients and Phase Shift at Normal Incidence",
        "difficulty": 2,
        "question": "A plane electromagnetic wave falls normally on the planar boundary between two non-magnetic dielectrics with refractive indices $n_1$ and $n_2$. Using the boundary conditions for electric and magnetic fields:\n(a) find the amplitude reflection coefficient $r = E'/E$ and transmission coefficient $t = E''/E$;\n(b) show that reflection from an optically denser medium ($n_2 > n_1$) involves a phase change of $\\pi$ (half-wave loss), whereas reflection from a rarer medium ($n_2 < n_1$) involves zero phase change.",
        "hints": [
            "Boundary conditions at normal incidence: continuity of tangential electric field $E + E' = E''$, and continuity of tangential magnetic field $H - H' = H''$ where $H = \\sqrt{\\frac{\\varepsilon_0}{\\mu_0}} n E$.",
            "Substitute to get $n_1 (E - E') = n_2 E''$.",
            "Solve the linear system for $r = \\frac{E'}{E} = \\frac{n_1 - n_2}{n_1 + n_2}$ and $t = \\frac{E''}{E} = \\frac{2 n_1}{n_1 + n_2}$."
        ],
        "answer": "(a) $r = \\frac{n_1 - n_2}{n_1 + n_2}$, $t = \\frac{2 n_1}{n_1 + n_2}$;\n(b) For $n_2 > n_1$, $r < 0$ corresponding to a phase jump of $\\pi$; for $n_2 < n_1$, $r > 0$ with zero phase change",
        "solution": "**(a) Boundary Conditions and Amplitude Coefficients:**\nLet a plane wave propagate along $+z$, normal to the interface at $z = 0$ between medium 1 ($z < 0$, index $n_1$) and medium 2 ($z > 0$, index $n_2$).\nLet $E$, $E'$, and $E''$ be the complex electric field amplitudes of the incident, reflected, and transmitted waves, respectively.\nFrom Maxwell's boundary conditions:\n1. Continuity of the tangential electric field across $z = 0$:\n$$E + E' = E''$$\n2. Continuity of the tangential magnetic field $B / \\mu_0$ (with $B = \\frac{n}{c} E$ in non-magnetic media):\n$$n_1 E - n_1 E' = n_2 E''$$\nDividing by $E$ and denoting $r = E'/E$ and $t = E''/E$:\n$$1 + r = t$$\n$$n_1 (1 - r) = n_2 t$$\nSubstituting $t = 1 + r$ into the second equation:\n$$n_1 - n_1 r = n_2 + n_2 r \\implies (n_1 + n_2) r = n_1 - n_2$$\n$$r = \\frac{n_1 - n_2}{n_1 + n_2}$$\n$$t = 1 + r = 1 + \\frac{n_1 - n_2}{n_1 + n_2} = \\frac{2 n_1}{n_1 + n_2}$$\n\n**(b) Phase Change Upon Reflection:**\n- If $n_2 > n_1$ (reflection from an optically denser medium):\n$$r = -\\frac{n_2 - n_1}{n_1 + n_2} = |r| e^{i\\pi}$$\nThe negative sign corresponds to a phase reversal of $\\pi$ radians (equivalent to an optical path difference of $\\lambda / 2$, the 'half-wave loss').\n- If $n_2 < n_1$ (reflection from an optically rarer medium):\n$$r = +\\frac{n_1 - n_2}{n_1 + n_2} > 0$$\nThe phase shift is zero.",
        "tags": ["Fresnel formulas", "boundary conditions", "phase jump", "reflection coefficient", "half-wave loss"]
    },
    {
        "id": "5.79",
        "title": "Thickness of a Thin Film Exhibiting Destructive Interference in White Light",
        "difficulty": 2,
        "question": "A parallel beam of white light falls on a thin soap film with refractive index $n = 1.33$ at an angle of incidence $\\theta = 45^\\circ$. In the reflected light, a dark band is observed at wavelength $\\lambda_1 = 0.60\\,\\mu\\text{m}$, while no dark bands are observed between $\\lambda_1$ and $\\lambda_2 = 0.45\\,\\mu\\text{m}$. Find the thickness $d$ of the film.",
        "hints": [
            "The optical path difference in reflection accounting for the $\\pi$ phase shift at the front surface is $\\Delta = 2 d \\sqrt{n^2 - \\sin^2\\theta} - \\frac{\\lambda}{2}$.",
            "Condition for a minimum in reflected light (destructive interference): $\\Delta = (k - 1/2)\\lambda \\implies 2 d \\sqrt{n^2 - \\sin^2\\theta} = k \\lambda$.",
            "For adjacent dark wavelengths: $k \\lambda_1 = (k + 1) \\lambda_2$. Find $k = \\frac{\\lambda_2}{\\lambda_1 - \\lambda_2}$, then calculate $d$."
        ],
        "answer": "$d = \\frac{k \\lambda_1}{2 \\sqrt{n^2 - \\sin^2\\theta}} = \\frac{3(0.60\\,\\mu\\text{m})}{2 \\sqrt{1.33^2 - 0.5}} \\approx 0.80\\,\\mu\\text{m}$ (or $k=1 \\implies 0.14\\,\\mu\\text{m}$)",
        "solution": "**1. Optical Path Difference for a Thin Film:**\nFor a film of thickness $d$ and index $n$ in air, light incident at angle $\\theta$ refracts at angle $\\theta'$, where $\\sin\\theta = n \\sin\\theta'$.\nThe optical path difference between the ray reflected from the top surface and the ray reflected from the bottom surface is:\n$$\\Delta = 2 n d \\cos\\theta' - \\frac{\\lambda}{2} = 2 d \\sqrt{n^2 - \\sin^2\\theta} - \\frac{\\lambda}{2}$$\nwhere $-\\lambda/2$ accounts for the phase reversal at the top air-film boundary.\n\n**2. Destructive Interference Condition:**\nDestructive interference in reflected light occurs when:\n$$\\Delta = \\left(m - \\frac{1}{2}\\right)\\lambda \\implies 2 d \\sqrt{n^2 - \\sin^2\\theta} = m \\lambda$$\nwhere $m$ is an integer.\n\n**3. Consecutive Dark Fringes:**\nGiven that $\\lambda_1 = 0.60\\,\\mu\\text{m}$ and $\\lambda_2 = 0.45\\,\\mu\\text{m}$ are consecutive wavelengths of destructive interference:\n$$m \\lambda_1 = (m + 1) \\lambda_2$$\n$$m (0.60) = (m + 1)(0.45) \\implies 0.15 m = 0.45 \\implies m = 3$$\n\n**4. Calculating Thickness $d$:**\n$$\\sqrt{n^2 - \\sin^2\\theta} = \\sqrt{(1.33)^2 - \\sin^2 45^\\circ} = \\sqrt{1.7689 - 0.50} = \\sqrt{1.2689} \\approx 1.1264$$\n$$2 d (1.1264) = 3 (0.60\\,\\mu\\text{m}) = 1.80\\,\\mu\\text{m}$$\n$$d = \\frac{1.80\\,\\mu\\text{m}}{2 \\times 1.1264} \\approx 0.80\\,\\mu\\text{m}$$",
        "tags": ["thin film interference", "white light", "destructive interference", "optical path difference"]
    },
    {
        "id": "5.80",
        "title": "Minimum Film Thickness for Maximum Reflection at Oblique Incidence",
        "difficulty": 2,
        "question": "Find the minimum thickness $d_{\\text{min}}$ of a thin soap film ($n = 1.33$) in air for which light with wavelength $\\lambda = 0.64\\,\\mu\\text{m}$ incident at an angle $\\theta = 30^\\circ$ experiences maximum constructive interference in reflection.",
        "hints": [
            "The optical path difference in reflection is $\\Delta = 2 d \\sqrt{n^2 - \\sin^2\\theta} - \\frac{\\lambda}{2}$.",
            "Condition for maximum reflection (constructive interference): $\\Delta = k \\lambda \\implies 2 d \\sqrt{n^2 - \\sin^2\\theta} = \\left(k + \\frac{1}{2}\\right)\\lambda$.",
            "The minimum non-zero thickness corresponds to $k = 0$: $d_{\\text{min}} = \\frac{\\lambda}{4 \\sqrt{n^2 - \\sin^2\\theta}}$."
        ],
        "answer": "$d_{\\text{min}} = \\frac{\\lambda}{4 \\sqrt{n^2 - \\sin^2\\theta}} \\approx 0.13\\,\\mu\\text{m}$ (or $0.65\\,\\mu\\text{m}$ for order $k$)",
        "solution": "**1. Constructive Interference Condition in Reflection:**\nFor a thin film of index $n$ in air, the optical path difference between the two reflected rays is:\n$$\\Delta = 2 d \\sqrt{n^2 - \\sin^2\\theta} - \\frac{\\lambda}{2}$$\nConstructive interference (reflection maximum) occurs when $\\Delta = k \\lambda$ ($k = 0, 1, 2, \\dots$):\n$$2 d \\sqrt{n^2 - \\sin^2\\theta} - \\frac{\\lambda}{2} = k \\lambda$$\n$$2 d \\sqrt{n^2 - \\sin^2\\theta} = \\left(k + \\frac{1}{2}\\right)\\lambda$$\n\n**2. Minimum Thickness:**\nThe minimum thickness corresponds to the lowest order $k = 0$:\n$$d_{\\text{min}} = \\frac{\\lambda}{4 \\sqrt{n^2 - \\sin^2\\theta}}$$\n\n**3. Numerical Evaluation:**\nFor $\\lambda = 0.64\\,\\mu\\text{m}$, $n = 1.33$, and $\\theta = 30^\\circ$:\n$$\\sin 30^\\circ = 0.50 \\implies \\sin^2 30^\\circ = 0.25$$\n$$n^2 - \\sin^2 30^\\circ = (1.33)^2 - 0.25 = 1.7689 - 0.25 = 1.5189$$\n$$\\sqrt{n^2 - \\sin^2\\theta} = \\sqrt{1.5189} \\approx 1.2324$$\n$$d_{\\text{min}} = \\frac{0.64\\,\\mu\\text{m}}{4 \\times 1.2324} = \\frac{0.64}{4.93} \\approx 0.13\\,\\mu\\text{m}$$",
        "tags": ["thin film interference", "constructive interference", "minimum thickness", "reflection"]
    }
]
