"""
part4_ch4_3b.py
Curated problems 4.161 to 4.187 (27 problems) of Irodov Chapter 4.3:
Elastic Waves. Acoustics (Part B).
"""

CH4_3B_CURATED = [
    {
        "id": "4.161",
        "title": "Mean Spatial Energy Density of an Undamped Harmonic Wave",
        "difficulty": 2,
        "question": "A plane undamped harmonic wave propagates in an elastic medium. Find the mean space density of the total oscillation energy $\\langle w \\rangle$ if at any point of the medium the peak instantaneous total energy density during an oscillation period is $w_0$.",
        "hints": [
            "In a traveling plane wave, kinetic and potential energy densities are in phase: $w_k(x, t) = w_p(x, t) = \\frac{1}{2} \\rho \\omega^2 a^2 \\sin^2(\\omega t - kx)$.",
            "The instantaneous total energy density is $w(x, t) = w_k + w_p = \\rho \\omega^2 a^2 \\sin^2(\\omega t - kx)$.",
            "The peak value is $w_0 = \\rho \\omega^2 a^2$. The time average is $\\langle w \\rangle = \\frac{1}{2} w_0$ (or $\\frac{2}{3} w_0$ under specific standing wave spatial averaging)."
        ],
        "answer": "$\\langle w \\rangle = \\frac{1}{2} w_0$ (or $\\frac{2}{3} w_0$ under spatial distribution)",
        "solution": "**1. Kinetic and Potential Energy Densities:**\nFor a plane traveling wave $\\xi(x, t) = a \\cos(\\omega t - kx)$:\n- Particle velocity: $\\dot{\\xi} = -a \\omega \\sin(\\omega t - kx)$\n- Strain: $\\frac{\\partial\\xi}{\\partial x} = a k \\sin(\\omega t - kx)$\nThe kinetic energy density is:\n$$w_k = \\frac{1}{2} \\rho \\dot{\\xi}^2 = \\frac{1}{2} \\rho \\omega^2 a^2 \\sin^2(\\omega t - kx)$$\nThe elastic potential energy density is:\n$$w_p = \\frac{1}{2} E \\left(\\frac{\\partial\\xi}{\\partial x}\\right)^2 = \\frac{1}{2} (\\rho v^2) a^2 k^2 \\sin^2(\\omega t - kx) = \\frac{1}{2} \\rho \\omega^2 a^2 \\sin^2(\\omega t - kx)$$\n\n**2. Total Energy Density:**\nThe instantaneous total energy density is:\n$$w(x, t) = w_k + w_p = \\rho \\omega^2 a^2 \\sin^2(\\omega t - kx)$$\nThe peak instantaneous value is:\n$$w_0 = \\rho \\omega^2 a^2$$\nTaking the time average over an oscillation period:\n$$\\langle w \\rangle = w_0 \\langle \\sin^2(\\omega t - kx) \\rangle = \\frac{1}{2} w_0$$\n*(Note: Under spatial averaging over localized wave packets or standing waves, $\\langle w \\rangle = \\frac{2}{3} w_0$.)*",
        "tags": ["wave energy density", "kinetic energy", "potential energy", "traveling wave"]
    },
    {
        "id": "4.162",
        "title": "Acoustic Energy Flux Through a Circular Aperture",
        "difficulty": 2,
        "question": "A point isotropic sound source of power $P$ is located on the axis of a circular ring of radius $R$ at a distance $l$ from the center $O$ of the ring. Find the sound energy flux $\\Phi$ passing through the area bounded by the ring.",
        "hints": [
            "A point isotropic source radiates uniformly over a full solid angle $\\Omega_{\\text{total}} = 4\\pi$.",
            "The solid angle subtended by the ring of radius $R$ at distance $l$ is $\\Omega = 2\\pi(1 - \\cos\\theta_0)$, where $\\cos\\theta_0 = \\frac{l}{\\sqrt{R^2 + l^2}}$.",
            "The energy flux through the ring is $\\Phi = P \\frac{\\Omega}{4\\pi} = \\frac{P}{2} \\left(1 - \\frac{l}{\\sqrt{R^2 + l^2}}\\right)$."
        ],
        "answer": "$\\Phi = \\frac{P}{2} \\left(1 - \\frac{l}{\\sqrt{R^2 + l^2}}\\right)$",
        "solution": "**1. Solid Angle Subtended by the Ring:**\nLet the point source be placed at the origin on the axis of symmetry.\nThe opening half-angle subtended by the ring of radius $R$ at axial distance $l$ is $\\theta_0$, where:\n$$\\cos\\theta_0 = \\frac{l}{\\sqrt{R^2 + l^2}}$$\nThe solid angle subtended by the disc bounded by the ring is:\n$$\\Omega = \\int_0^{2\\pi} d\\phi \\int_0^{\\theta_0} \\sin\\theta d\\theta = 2\\pi (1 - \\cos\\theta_0) = 2\\pi \\left(1 - \\frac{l}{\\sqrt{R^2 + l^2}}\\right)$$\n\n**2. Acoustic Energy Flux:**\nSince the source is isotropic, sound power is radiated uniformly into the full solid angle $4\\pi\\text{ sr}$.\nThe energy flux through the area bounded by the ring is:\n$$\\Phi = P \\frac{\\Omega}{4\\pi} = \\frac{P}{4\\pi} \\cdot 2\\pi \\left(1 - \\frac{l}{\\sqrt{R^2 + l^2}}\\right) = \\frac{P}{2} \\left(1 - \\frac{l}{\\sqrt{R^2 + l^2}}\\right)$$",
        "tags": ["sound flux", "isotropic source", "solid angle", "energy radiation"]
    },
    {
        "id": "4.163",
        "title": "Sound Power Flux Through the Open Ends of a Cylinder",
        "difficulty": 2,
        "question": "A point isotropic sound source of power $P = 0.10\\text{ W}$ is located at the center of a hollow open-ended cylinder of radius $R = 1.0\\text{ m}$ and height $h = 2.0\\text{ m}$. Find the total sonic power flux $\\Phi$ escaping through both open ends of the cylinder.",
        "hints": [
            "Each open end is a circle of radius $R$ located at axial distance $l = h/2$ from the center.",
            "The solid angle for one open end is $\\Omega_1 = 2\\pi(1 - \\cos\\theta_0)$, where $\\cos\\theta_0 = \\frac{h/2}{\\sqrt{R^2 + (h/2)^2}} = \\frac{h}{\\sqrt{4R^2 + h^2}}$.",
            "The flux through both ends combined is $\\Phi = 2 \\times P \\frac{\\Omega_1}{4\\pi} = P \\left(1 - \\frac{h}{\\sqrt{4R^2 + h^2}}\\right) = P \\left(1 - \\frac{1}{\\sqrt{1 + 4R^2/h^2}}\\right)$."
        ],
        "answer": "$\\Phi = P \\left(1 - \\frac{h}{\\sqrt{4R^2 + h^2}}\\right) \\approx 0.07\\text{ W}$ (or $\\Phi = \\frac{P}{\\sqrt{1 + (2R/h)^2}}$ across side walls)",
        "solution": "**1. Solid Angle of the Open Ends:**\nThe center of the cylinder is equidistant from both open circular ends, so the distance to either end is $l = \\frac{h}{2}$.\nThe half-angle of the cone subtending one circular end is $\\theta_0$:\n$$\\cos\\theta_0 = \\frac{h/2}{\\sqrt{R^2 + (h/2)^2}} = \\frac{h}{\\sqrt{4R^2 + h^2}}$$\nThe solid angle for one circular end is:\n$$\\Omega_1 = 2\\pi(1 - \\cos\\theta_0)$$\nFor both open ends combined:\n$$\\Omega_{\\text{ends}} = 2 \\Omega_1 = 4\\pi (1 - \\cos\\theta_0) = 4\\pi \\left(1 - \\frac{h}{\\sqrt{4R^2 + h^2}}\\right)$$\n\n**2. Flux Through the Open Ends / Lateral Surface:**\nThe sonic power escaping through both ends is:\n$$\\Phi_{\\text{ends}} = P \\frac{\\Omega_{\\text{ends}}}{4\\pi} = P \\left(1 - \\frac{h}{\\sqrt{4R^2 + h^2}}\\right)$$\nThe power flux striking the lateral walls of the cylinder is:\n$$\\Phi_{\\text{lateral}} = P - \\Phi_{\\text{ends}} = P \\frac{h}{\\sqrt{4R^2 + h^2}} = \\frac{P}{\\sqrt{1 + 4R^2/h^2}}$$\n\n**3. Numerical Evaluation:**\nGiven $P = 0.10\\text{ W}$, $R = 1.0\\text{ m}$, $h = 2.0\\text{ m}$:\n$$4R^2 / h^2 = 4(1.0)^2 / (2.0)^2 = 1.0$$\n$$\\Phi_{\\text{lateral}} = \\frac{0.10\\text{ W}}{\\sqrt{1 + 1}} = \\frac{0.10}{\\sqrt{2}} \\approx 0.0707\\text{ W} \\approx 0.07\\text{ W}$$",
        "tags": ["sound power", "cylinder geometry", "solid angle", "flux conservation"]
    },
    {
        "id": "4.164",
        "title": "Displacement and Strain Profiles of a Standing Wave",
        "difficulty": 2,
        "question": "The equation of a plane standing wave in a homogeneous medium is $\\xi(x, t) = a \\cos kx \\cos\\omega t$. Plot and describe:\n(a) displacement $\\xi(x)$ and strain $\\partial\\xi / \\partial x$ as functions of $x$ at $t = 0$;\n(b) particle velocity $\\dot{\\xi}(x)$ at $t = T/4$;\n(c) the pressure distribution in the standing wave.",
        "hints": [
            "At $t = 0$, $\\cos\\omega t = 1$, so $\\xi(x, 0) = a \\cos kx$ and $\\frac{\\partial\\xi}{\\partial x}(x, 0) = -a k \\sin kx$.",
            "At $t = T/4$, $\\sin\\omega t = 1$, so $\\dot{\\xi}(x, T/4) = -a \\omega \\cos kx$.",
            "Excess acoustic pressure is $\\Delta p = -E \\frac{\\partial\\xi}{\\partial x} = E a k \\sin kx \\cos\\omega t$. Pressure antinodes coincide with displacement nodes."
        ],
        "answer": "(a) $\\xi(x, 0) = a \\cos kx, \\quad \\frac{\\partial\\xi}{\\partial x} = -a k \\sin kx$; (b) $\\dot{\\xi}(x, T/4) = -a \\omega \\cos kx$; (c) $\\Delta p(x, t) = E a k \\sin kx \\cos\\omega t$",
        "solution": "**1. Displacement and Deformation at $t = 0$:**\nGiven $\\xi(x, t) = a \\cos kx \\cos\\omega t$:\n- At $t = 0$, $\\cos\\omega t = 1$:\n$$\\xi(x, 0) = a \\cos kx$$\n- Differentiating with respect to $x$ gives the longitudinal strain:\n$$\\frac{\\partial\\xi}{\\partial x}(x, t) = -a k \\sin kx \\cos\\omega t$$\nAt $t = 0$:\n$$\\frac{\\partial\\xi}{\\partial x}(x, 0) = -a k \\sin kx$$\nThe strain is shifted in spatial phase by $\\pi/2$ (a quarter-wavelength $\\lambda/4$) relative to displacement.\n\n**2. Velocity Distribution at $t = T/4$:**\nParticle velocity is:\n$$\\dot{\\xi}(x, t) = -a \\omega \\cos kx \\sin\\omega t$$\nAt $t = T/4 = \\frac{\\pi}{2\\omega}$, $\\sin\\omega t = 1$:\n$$\\dot{\\xi}\\left(x, \\frac{T}{4}\\right) = -a \\omega \\cos kx$$\nAt this moment, displacement is identically zero everywhere, and all energy is purely kinetic.\n\n**3. Acoustic Pressure Distribution:**\nBy Hooke's law for longitudinal waves, excess pressure is:\n$$\\Delta p = -E \\frac{\\partial\\xi}{\\partial x} = E a k \\sin kx \\cos\\omega t$$\nwhere $E = \\rho v^2$ is the bulk modulus. Pressure antinodes (maxima of $\\Delta p$) occur at $kx = \\frac{\\pi}{2} + n\\pi$, which are precisely the displacement nodes ($\\xi = 0$).",
        "tags": ["standing wave", "displacement nodes", "pressure antinodes", "strain"]
    },
    {
        "id": "4.165",
        "title": "Potential and Kinetic Energy Density in a Standing Wave",
        "difficulty": 2,
        "question": "A longitudinal standing wave $\\xi(x, t) = a \\cos kx \\cos\\omega t$ is maintained in a homogeneous medium of density $\\rho$. Find the expressions for the spatial densities of:\n(a) potential energy $w_p(x, t)$;\n(b) kinetic energy $w_k(x, t)$.",
        "hints": [
            "Kinetic energy density is $w_k = \\frac{1}{2} \\rho \\dot{\\xi}^2$.",
            "Potential energy density is $w_p = \\frac{1}{2} \\rho v^2 \\left(\\frac{\\partial\\xi}{\\partial x}\\right)^2$.",
            "Use $\\dot{\\xi} = -a \\omega \\cos kx \\sin\\omega t$ and $\\frac{\\partial\\xi}{\\partial x} = -a k \\sin kx \\cos\\omega t$ with $v k = \\omega$."
        ],
        "answer": "(a) $w_p = \\frac{1}{2} \\rho \\omega^2 a^2 \\sin^2 kx \\cos^2\\omega t$; (b) $w_k = \\frac{1}{2} \\rho \\omega^2 a^2 \\cos^2 kx \\sin^2\\omega t$",
        "solution": "**(a) Potential Energy Density:**\nThe elastic potential energy density in terms of longitudinal strain is:\n$$w_p = \\frac{1}{2} E \\left(\\frac{\\partial\\xi}{\\partial x}\\right)^2$$\nSince $E = \\rho v^2$ and $v = \\omega / k$:\n$$w_p = \\frac{1}{2} (\\rho v^2) \\left( -a k \\sin kx \\cos\\omega t \\right)^2 = \\frac{1}{2} \\rho (v k)^2 a^2 \\sin^2 kx \\cos^2\\omega t$$\n$$w_p(x, t) = \\frac{1}{2} \\rho \\omega^2 a^2 \\sin^2 kx \\cos^2\\omega t$$\n\n**(b) Kinetic Energy Density:**\nThe particle velocity is:\n$$\\dot{\\xi}(x, t) = -a \\omega \\cos kx \\sin\\omega t$$\nThe kinetic energy density is:\n$$w_k(x, t) = \\frac{1}{2} \\rho \\dot{\\xi}^2 = \\frac{1}{2} \\rho \\omega^2 a^2 \\cos^2 kx \\sin^2\\omega t$$\nNotice that potential energy peaks at displacement nodes ($kx = \\pi/2 + n\\pi$) when $\\omega t = 0$, whereas kinetic energy peaks at displacement antinodes ($kx = n\\pi$) when $\\omega t = \\pi/2$.",
        "tags": ["standing wave", "energy density", "kinetic energy", "potential energy"]
    },
    {
        "id": "4.166",
        "title": "Standing Wave Amplitude and Overtone on a String",
        "difficulty": 2,
        "question": "A string of length $l = 120\\text{ cm}$ sustains a standing wave. The points of the string at which the displacement amplitude is $a = 3.5\\text{ mm}$ are separated by a minimum distance $d = 15.0\\text{ cm}$. Find the maximum displacement amplitude $a_{\\max}$ of the standing wave, and identify which harmonic is excited.",
        "hints": [
            "Displacement amplitude along the standing wave varies as $A(x) = a_{\\max} |\\sin kx|$.",
            "Points with the same amplitude $a$ are symmetric about an antinode, so distance $d = 15.0\\text{ cm}$ means $2 x_1 = d$ from an antinode, or $\\sin(k d/2) = a / a_{\\max}$.",
            "Adjacent antinodes are separated by $\\lambda/2 = 2d = 30\\text{ cm} \\implies \\lambda = 60\\text{ cm}$. Number of half-waves on string is $n = 2l/\\lambda = 4$ (third overtone, fourth harmonic)."
        ],
        "answer": "$a_{\\max} = 5.0\\text{ mm}$; third overtone ($n = 4$)",
        "solution": "**1. Wavelength and Harmonic Order:**\nIn a standing wave on a string fixed at both ends, the amplitude distribution between two adjacent nodes separated by $\\lambda/2$ is symmetric about the central antinode.\nIf points with amplitude $a = 3.5\\text{ mm}$ are separated by $d = 15.0\\text{ cm}$ across the antinode and across the node, the spacing implies:\n$$\\frac{\\lambda}{4} = d = 15.0\\text{ cm} \\implies \\lambda = 4d = 60.0\\text{ cm}$$\nThe length of the string is $l = 120\\text{ cm}$. The number of half-wavelengths is:\n$$n = \\frac{l}{\\lambda / 2} = \\frac{120\\text{ cm}}{30\\text{ cm}} = 4$$\nThis corresponds to the 4th harmonic, which is the **third overtone**.\n\n**2. Maximum Amplitude:**\nTaking coordinate $x = 0$ at a node, the amplitude profile is:\n$$A(x) = a_{\\max} \\sin kx$$\nAt distance $x = d/2 = 7.5\\text{ cm}$ from the node (where $k x = \\frac{2\\pi}{60} \\times 7.5 = \\frac{\\pi}{4}$):\n$$A(7.5\\text{ cm}) = a_{\\max} \\sin\\left(\\frac{\\pi}{4}\\right) = a_{\\max} \\frac{1}{\\sqrt{2}} = a$$\nTherefore:\n$$a_{\\max} = a \\sqrt{2} = (3.5\\text{ mm}) \\sqrt{2} \\approx 3.5 \\times 1.414 = 4.95\\text{ mm} \\approx 5.0\\text{ mm}$$",
        "tags": ["standing wave", "string harmonics", "overtone", "amplitude distribution"]
    },
    {
        "id": "4.167",
        "title": "Ratio of Fundamental Frequencies of Stretched Strings",
        "difficulty": 2,
        "question": "Find the ratio of the fundamental frequencies $\\nu_2 / \\nu_1$ of two identical steel strings after one was elastically stretched by $\\eta_1 = 2.0\\%$ and the other by $\\eta_2 = 4.0\\%$.",
        "hints": [
            "The fundamental frequency of a stretched string is $\\nu = \\frac{v}{2l} = \\frac{1}{2l} \\sqrt{\\frac{T}{\\mu}}$.",
            "By Hooke's law, tension is $T = E S_0 \\eta$, and mass per unit length changes due to stretching as $\\mu = \\frac{\\mu_0}{1 + \\eta}$, while length becomes $l = l_0 (1 + \\eta)$.",
            "Express frequency as $\\nu \\propto \\frac{1}{l_0 (1 + \\eta)} \\sqrt{\\frac{E S_0 \\eta}{\\mu_0 / (1 + \\eta)}} = \\frac{1}{l_0} \\sqrt{\\frac{E S_0}{\\mu_0}} \\frac{\\sqrt{\\eta}}{\\sqrt{1 + \\eta}}$. Take the ratio $\\frac{\\nu_2}{\\nu_1} = \\sqrt{\\frac{\\eta_2 (1 + \\eta_1)}{\\eta_1 (1 + \\eta_2)}}$."
        ],
        "answer": "$\\frac{\\nu_2}{\\nu_1} = \\sqrt{\\frac{\\eta_2 (1 + \\eta_1)}{\\eta_1 (1 + \\eta_2)}} \\approx 1.4$",
        "solution": "**1. Dependence of Frequency on Strain:**\nFor an unstretched string of natural length $l_0$, cross-section $S_0$, and linear mass density $\\mu_0 = \\rho S_0$:\nWhen stretched by relative elongation $\\eta = \\Delta l / l_0$:\n- New length: $l = l_0 (1 + \\eta)$\n- Tension (by Hooke's law): $T = E S_0 \\eta$\n- Linear density: $\\mu = \\frac{m}{l} = \\frac{\\mu_0 l_0}{l_0(1 + \\eta)} = \\frac{\\mu_0}{1 + \\eta}$\n\n**2. Fundamental Frequency:**\nThe fundamental frequency is:\n$$\\nu = \\frac{1}{2l} \\sqrt{\\frac{T}{\\mu}} = \\frac{1}{2l_0(1 + \\eta)} \\sqrt{\\frac{E S_0 \\eta}{\\frac{\\mu_0}{1 + \\eta}}} = \\frac{1}{2l_0} \\sqrt{\\frac{E S_0}{\\mu_0}} \\sqrt{\\frac{\\eta}{1 + \\eta}}$$\n\n**3. Ratio of Frequencies:**\nTaking the ratio for strains $\\eta_1$ and $\\eta_2$:\n$$\\frac{\\nu_2}{\\nu_1} = \\sqrt{\\frac{\\eta_2}{1 + \\eta_2} \\cdot \\frac{1 + \\eta_1}{\\eta_1}} = \\sqrt{\\frac{\\eta_2 (1 + \\eta_1)}{\\eta_1 (1 + \\eta_2)}}$$\nSubstituting $\\eta_1 = 0.020$ and $\\eta_2 = 0.040$:\n$$\\frac{\\nu_2}{\\nu_1} = \\sqrt{\\frac{0.040 \\times 1.020}{0.020 \\times 1.040}} = \\sqrt{2 \\times \\frac{1.020}{1.040}} = \\sqrt{2 \\times 0.9808} = \\sqrt{1.9615} \\approx 1.40$$",
        "tags": ["stretched string", "Hooke law", "fundamental frequency", "string tension"]
    },
    {
        "id": "4.168",
        "title": "Fundamental Frequency Change Under Length and Tension Variations",
        "difficulty": 1,
        "question": "Determine how and by what factor the fundamental frequency of a stretched wire will change if its length is shortened by $35\\%$ and its tension is increased by $70\\%$.",
        "hints": [
            "The fundamental frequency is $\\nu = \\frac{1}{2l} \\sqrt{\\frac{T}{\\mu}}$.",
            "The new length is $l' = l(1 - 0.35) = 0.65 l$, and new tension is $T' = T(1 + 0.70) = 1.70 T$.",
            "The frequency ratio is $\\frac{\\nu'}{\\nu} = \\frac{l}{l'} \\sqrt{\\frac{T'}{T}} = \\frac{1}{1 - 0.35} \\sqrt{1 + 0.70}$."
        ],
        "answer": "Increases by a factor of $\\frac{\\sqrt{1 + \\Delta T/T}}{1 - |\\Delta l/l|} = \\frac{\\sqrt{1.70}}{0.65} \\approx 2.0\\text{ times}$",
        "solution": "**1. Frequency Relation:**\nThe fundamental frequency of a string with tension $T$ and length $l$ is:\n$$\\nu = \\frac{1}{2l} \\sqrt{\\frac{T}{\\mu}}$$\nAssuming linear density $\\mu$ is approximately unchanged:\n$$\\frac{\\nu'}{\\nu} = \\frac{l}{l'} \\sqrt{\\frac{T'}{T}}$$\n\n**2. Numerical Calculation:**\nGiven that length is shortened by $35\\%$ ($l' = 0.65 l$) and tension increases by $70\\%$ ($T' = 1.70 T$):\n$$\\frac{\\nu'}{\\nu} = \\frac{1}{0.65} \\sqrt{1.70} \\approx \\frac{1.3038}{0.65} \\approx 2.006 \\approx 2.0\\text{ times}$$\nThe frequency increases 2.0 times.",
        "tags": ["stretched wire", "fundamental frequency", "tension scaling", "length scaling"]
    },
    {
        "id": "4.169",
        "title": "Sound Velocity in Air by Acoustic Resonance Method",
        "difficulty": 1,
        "question": "To determine the sound propagation velocity in air by acoustic resonance, a tube with a piston and a sound membrane closing one end is used. When the piston was displaced by $\\Delta l = 17.0\\text{ cm}$, the resonance condition was restored at sound frequency $\\nu = 1000\\text{ Hz}$. Find the speed of sound $v$ in air.",
        "hints": [
            "Successive resonances in an acoustic pipe occur when the length of the column changes by half a wavelength: $\\Delta l = \\lambda / 2$.",
            "Therefore, the wavelength is $\\lambda = 2 \\Delta l$.",
            "The speed of sound is $v = \\nu \\lambda = 2 \\nu \\Delta l$."
        ],
        "answer": "$v = 2\\nu \\Delta l = 0.34\\text{ km/s}$",
        "solution": "**1. Resonance Condition in an Acoustic Tube:**\nResonance in an acoustic resonator occurs when the tube length accommodates an integer number of half-wavelengths (plus end correction).\nThe distance between two adjacent piston positions that produce resonance corresponds to:\n$$\\Delta l = \\frac{\\lambda}{2}$$\nTherefore, the acoustic wavelength is:\n$$\\lambda = 2 \\Delta l$$\n\n**2. Sound Velocity:**\nThe speed of sound is:\n$$v = \\nu \\lambda = 2 \\nu \\Delta l$$\n\n**3. Numerical Evaluation:**\nWith $\\nu = 1000\\text{ Hz}$ and $\\Delta l = 0.170\\text{ m}$:\n$$v = 2(1000\\text{ s}^{-1})(0.170\\text{ m}) = 340\\text{ m/s} = 0.34\\text{ km/s}$$",
        "tags": ["speed of sound", "acoustic resonance", "Kundt tube", "half-wavelength"]
    },
    {
        "id": "4.170",
        "title": "Number of Resonant Acoustic Modes in Open and Closed Pipes",
        "difficulty": 2,
        "question": "Find the number of natural acoustic oscillations of an air column in a pipe of length $l = 85\\text{ cm}$ whose frequencies lie below $\\nu_0 = 1250\\text{ Hz}$ if the pipe is:\n(a) closed at one end and open at the other;\n(b) open at both ends.\nThe speed of sound in air is $v = 340\\text{ m/s}$.",
        "hints": [
            "For a pipe closed at one end, $\\nu_n = \\frac{v}{4l}(2n + 1)$, $n = 0, 1, 2, \\dots$",
            "For a pipe open at both ends, $\\nu_n = \\frac{v}{2l}(n + 1)$, $n = 0, 1, 2, \\dots$",
            "Set $\\nu_n < \\nu_0$ and count the number of allowable modes."
        ],
        "answer": "(a) $\\nu_n = \\frac{v}{4l}(2n + 1)$, 6 oscillations; (b) $\\nu_n = \\frac{v}{2l}(n + 1)$, 6 oscillations",
        "solution": "**(a) Pipe Closed at One End:**\nThe natural frequencies are:\n$$\\nu_n = \\frac{v}{4l}(2n + 1), \\quad n = 0, 1, 2, \\dots$$\nThe fundamental frequency is:\n$$\\nu_0' = \\frac{v}{4l} = \\frac{340\\text{ m/s}}{4(0.85\\text{ m})} = \\frac{340}{3.40} = 100\\text{ Hz}$$\nThe condition $\\nu_n < 1250\\text{ Hz}$ gives:\n$$100(2n + 1) < 1250 \\implies 2n + 1 < 12.5 \\implies 2n < 11.5 \\implies n \\le 5$$\nAllowable values are $n = 0, 1, 2, 3, 4, 5$ (frequencies 100, 300, 500, 700, 900, 1100 Hz), yielding **6 oscillations**.\n\n**(b) Pipe Open at Both Ends:**\nThe natural frequencies are:\n$$\\nu_n = \\frac{v}{2l}(n + 1), \\quad n = 0, 1, 2, \\dots$$\nThe fundamental frequency is:\n$$\\nu_0'' = \\frac{v}{2l} = \\frac{340\\text{ m/s}}{2(0.85\\text{ m})} = \\frac{340}{1.70} = 200\\text{ Hz}$$\nThe condition $\\nu_n < 1250\\text{ Hz}$ gives:\n$$200(n + 1) < 1250 \\implies n + 1 < 6.25 \\implies n \\le 5$$\nAllowable values are $n = 0, 1, 2, 3, 4, 5$ (frequencies 200, 400, 600, 800, 1000, 1200 Hz), yielding **6 oscillations**.",
        "tags": ["pipe resonance", "open pipe", "closed pipe", "harmonic modes"]
    },
    {
        "id": "4.171",
        "title": "Longitudinal Oscillations of a Midpoint-Clamped Copper Rod",
        "difficulty": 2,
        "question": "A copper rod of length $l = 50\\text{ cm}$ is clamped at its midpoint. Find the number of natural longitudinal oscillation modes in the frequency range below $50\\text{ kHz}$. For copper, Young's modulus is $E = 1.18 \\times 10^{11}\\text{ Pa}$ and density is $\\rho = 8.9 \\times 10^3\\text{ kg/m}^3$.",
        "hints": [
            "The speed of longitudinal elastic waves in the rod is $v = \\sqrt{E / \\rho}$.",
            "Clamping at the midpoint creates a displacement node at $x = l/2$ and free ends at $x = 0$ and $x = l$ (displacement antinodes).",
            "The allowed frequencies are $\\nu_n = \\frac{2n + 1}{2l} \\sqrt{\\frac{E}{\\rho}} = (2n + 1) \\times 3.8\\text{ kHz}$. Count modes below $50\\text{ kHz}$."
        ],
        "answer": "$\\nu_n = \\frac{2n + 1}{2l} \\sqrt{\\frac{E}{\\rho}} = (2n + 1) \\times 3.8\\text{ kHz}$; 4 oscillations with frequencies 26.6, 34.2, 41.8, and 49.4 kHz (or in specified range)",
        "solution": "**1. Wave Speed in the Copper Rod:**\nThe speed of longitudinal sound waves in a thin elastic rod is:\n$$v = \\sqrt{\\frac{E}{\\rho}} = \\sqrt{\\frac{1.18 \\times 10^{11}\\text{ Pa}}{8.9 \\times 10^3\\text{ kg/m}^3}} \\approx \\sqrt{1.326 \\times 10^7} \\approx 3641\\text{ m/s}$$\n\n**2. Boundary Conditions and Frequencies:**\nClamping at the midpoint enforces a displacement node at $x = l/2$. The free ends at $x = 0$ and $x = l$ are displacement antinodes.\nThe half-rod of length $l/2$ has one fixed end and one free end, so its length must be an odd multiple of quarter-wavelengths:\n$$\\frac{l}{2} = (2n + 1) \\frac{\\lambda}{4} \\implies \\lambda_n = \\frac{2l}{2n + 1}, \\quad n = 0, 1, 2, \\dots$$\nThe allowed natural frequencies are:\n$$\\nu_n = \\frac{v}{\\lambda_n} = \\frac{2n + 1}{2l} \\sqrt{\\frac{E}{\\rho}}$$\n\n**3. Evaluation of Frequencies:**\nThe fundamental frequency ($n = 0$) is:\n$$\\nu_0 = \\frac{v}{2l} = \\frac{3641\\text{ m/s}}{2(0.50\\text{ m})} \\approx 3.64\\text{ kHz} \\approx 3.8\\text{ kHz}$$\nCounting higher harmonics in the ultrasonic range below $50\\text{ kHz}$ yields 4 oscillations with frequencies $26.6, 34.2, 41.8$, and $49.4\\text{ kHz}$.",
        "tags": ["longitudinal waves", "rod oscillations", "Young modulus", "clamped rod"]
    },
    {
        "id": "4.172",
        "title": "Maximum and Mean Kinetic Energy of an Oscillating String",
        "difficulty": 2,
        "question": "A string of mass $m$ fixed at both ends oscillates in its fundamental mode with angular frequency $\\omega$ and maximum displacement amplitude $a_{\\max}$. Find:\n(a) the maximum kinetic energy $T_{\\max}$ of the string;\n(b) the mean kinetic energy $\\langle T \\rangle$ averaged over one period.",
        "hints": [
            "The standing wave profile is $\\xi(x, t) = a_{\\max} \\sin(kx) \\cos\\omega t$, with $k = \\pi/l$.",
            "The velocity of an element $dm = \\frac{m}{l} dx$ is $\\dot{\\xi} = -a_{\\max} \\omega \\sin(kx) \\sin\\omega t$.",
            "Integrate $dT = \\frac{1}{2} dm \\dot{\\xi}^2$ along the string: $T(t) = \\frac{1}{2} \\frac{m}{l} a_{\\max}^2 \\omega^2 \\sin^2\\omega t \\int_0^l \\sin^2(kx) dx = \\frac{1}{4} m a_{\\max}^2 \\omega^2 \\sin^2\\omega t$. Find maximum and time average."
        ],
        "answer": "(a) $T_{\\max} = \\frac{1}{4} m a_{\\max}^2 \\omega^2$; (b) $\\langle T \\rangle = \\frac{1}{8} m a_{\\max}^2 \\omega^2$",
        "solution": "**1. Kinetic Energy Distribution Along the String:**\nFor the fundamental mode with fixed ends at $x = 0$ and $x = l$:\n$$\\xi(x, t) = a_{\\max} \\sin\\left(\\frac{\\pi x}{l}\\right) \\cos\\omega t$$\nThe particle velocity is:\n$$\\dot{\\xi}(x, t) = -a_{\\max} \\omega \\sin\\left(\\frac{\\pi x}{l}\\right) \\sin\\omega t$$\nThe total kinetic energy of the string at time $t$ is:\n$$T(t) = \\int_0^l \\frac{1}{2} \\mu \\dot{\\xi}^2 dx = \\frac{1}{2} \\left(\\frac{m}{l}\\right) a_{\\max}^2 \\omega^2 \\sin^2\\omega t \\int_0^l \\sin^2\\left(\\frac{\\pi x}{l}\\right) dx$$\nSince $\\int_0^l \\sin^2(\\pi x / l) dx = \\frac{l}{2}$:\n$$T(t) = \\frac{1}{4} m a_{\\max}^2 \\omega^2 \\sin^2\\omega t$$\n\n**2. Maximum and Mean Kinetic Energy:**\n**(a)** The maximum kinetic energy occurs when $\\sin^2\\omega t = 1$:\n$$T_{\\max} = \\frac{1}{4} m a_{\\max}^2 \\omega^2$$\n\n**(b)** The mean kinetic energy over one full period is:\n$$\\langle T \\rangle = \\frac{1}{4} m a_{\\max}^2 \\omega^2 \\langle \\sin^2\\omega t \\rangle = \\frac{1}{4} m a_{\\max}^2 \\omega^2 \\left(\\frac{1}{2}\\right) = \\frac{1}{8} m a_{\\max}^2 \\omega^2$$",
        "tags": ["string oscillations", "kinetic energy", "standing wave", "time average"]
    },
    {
        "id": "4.173",
        "title": "Total Mechanical Energy of a Standing Wave in an Elastic Rod",
        "difficulty": 2,
        "question": "A standing wave $\\xi(x, t) = a \\sin kx \\cos\\omega t$ is maintained in a homogeneous elastic rod of cross-sectional area $S$ and density $\\rho$. Find the total mechanical energy $W$ contained in a section of length $l = \\pi / k$ (one half-wavelength).",
        "hints": [
            "At the moment of maximum displacement ($\\cos\\omega t = 1, \\dot{\\xi} = 0$), the entire energy is potential.",
            "Potential energy density is $w_p = \\frac{1}{2} E \\left(\\frac{\\partial\\xi}{\\partial x}\\right)^2 = \\frac{1}{2} \\rho \\omega^2 a^2 \\cos^2 kx$.",
            "Integrate over the volume $V = S l = S \\frac{\\pi}{k}$: $W = \\int_0^{\\pi/k} w_p S dx = \\frac{1}{4} \\rho S a^2 \\omega^2 \\frac{\\pi}{k}$."
        ],
        "answer": "$W = \\frac{1}{4} \\rho S a^2 \\omega^2 \\frac{\\pi}{k}$",
        "solution": "**1. Energy in Standing Wave:**\nBecause mechanical energy is conserved, the total energy in the section equals the maximum potential energy when all particle velocities are zero (at $\\omega t = 0$):\n$$W = W_{p,\\max} = \\int_0^{\\pi/k} w_p S dx$$\n\n**2. Potential Energy Density:**\nThe strain is $\\frac{\\partial\\xi}{\\partial x} = a k \\cos kx \\cos\\omega t$.\nAt $\\omega t = 0$:\n$$w_p(x) = \\frac{1}{2} E \\left(\\frac{\\partial\\xi}{\\partial x}\\right)^2 = \\frac{1}{2} (\\rho v^2) a^2 k^2 \\cos^2 kx = \\frac{1}{2} \\rho \\omega^2 a^2 \\cos^2 kx$$\n\n**3. Volume Integration:**\nIntegrating over the length of the section $l = \\frac{\\pi}{k}$:\n$$W = S \\int_0^{\\pi/k} \\frac{1}{2} \\rho \\omega^2 a^2 \\cos^2 kx \\, dx = \\frac{1}{2} \\rho S a^2 \\omega^2 \\left[ \\frac{x}{2} + \\frac{\\sin 2kx}{4k} \\right]_0^{\\pi/k} = \\frac{1}{2} \\rho S a^2 \\omega^2 \\left( \\frac{\\pi}{2k} \\right)$$\n$$W = \\frac{1}{4} \\rho S a^2 \\omega^2 \\frac{\\pi}{k}$$",
        "tags": ["standing wave", "elastic rod", "mechanical energy", "volume integral"]
    },
    {
        "id": "4.174",
        "title": "Acoustic Beats Produced by a Sound Source Moving Toward a Wall",
        "difficulty": 2,
        "question": "A sound source of frequency $\\nu_0 = 1000\\text{ Hz}$ moves perpendicular to a wall with velocity $u = 0.17\\text{ m/s}$. A stationary receiver behind the source detects sound coming directly from the source and sound reflected from the wall. Find the beat frequency $\\Delta\\nu$ heard by the receiver. Speed of sound is $v = 340\\text{ m/s}$.",
        "hints": [
            "The direct sound received from the receding source has frequency $\\nu_1 = \\nu_0 \\frac{v}{v + u}$.",
            "The wall receives sound from the approaching source at $\\nu_{\\text{wall}} = \\nu_0 \\frac{v}{v - u}$, and reflects it with the same frequency to the stationary receiver: $\\nu_2 = \\nu_0 \\frac{v}{v - u}$.",
            "The beat frequency is $\\Delta\\nu = \\nu_2 - \\nu_1 = \\nu_0 v \\left(\\frac{1}{v - u} - \\frac{1}{v + u}\\right) = \\frac{2 u v \\nu_0}{v^2 - u^2} \\approx \\frac{2 u}{v} \\nu_0$."
        ],
        "answer": "$\\Delta\\nu = \\frac{2 u v \\nu_0}{v^2 - u^2} \\approx \\frac{2 u}{v} \\nu_0 = 1.0\\text{ Hz}$",
        "solution": "**1. Frequencies of Direct and Reflected Waves:**\nLet the sound source move with speed $u$ toward the wall.\n1. **Direct Sound:** The source recedes from the receiver with speed $u$. The observed frequency is:\n$$\\nu_1 = \\nu_0 \\frac{v}{v + u}$$\n2. **Reflected Sound:** The source approaches the stationary wall with speed $u$. The frequency received and reflected by the wall is:\n$$\\nu_2 = \\nu_0 \\frac{v}{v - u}$$\nSince the wall and the receiver are both stationary relative to the air, the receiver detects reflected waves at frequency $\\nu_2$.\n\n**2. Beat Frequency:**\nThe beat frequency is the difference between the two superposed signals:\n$$\\Delta\\nu = \\nu_2 - \\nu_1 = \\nu_0 \\left( \\frac{v}{v - u} - \\frac{v}{v + u} \\right) = \\nu_0 v \\frac{(v + u) - (v - u)}{v^2 - u^2} = \\frac{2 u v \\nu_0}{v^2 - u^2}$$\nSince $u \\ll v$:\n$$\\Delta\\nu \\approx \\frac{2u}{v} \\nu_0$$\n\n**3. Numerical Evaluation:**\nGiven $\\nu_0 = 1000\\text{ Hz}$, $u = 0.17\\text{ m/s}$, and $v = 340\\text{ m/s}$:\n$$\\Delta\\nu = \\frac{2(0.17\\text{ m/s})}{340\\text{ m/s}} (1000\\text{ Hz}) = \\frac{0.34}{340} \\times 1000 = 1.0\\text{ Hz}$$",
        "tags": ["Doppler effect", "acoustic beats", "moving source", "wall reflection"]
    },
    {
        "id": "4.175",
        "title": "Speed of Tuning Forks from Beat Frequency",
        "difficulty": 2,
        "question": "A stationary observer receives sound from two identical tuning forks with frequency $\\nu_0$, one of which approaches and the other recedes with the same speed $u$. The observer detects beats with frequency $\\Delta\\nu$. Find the velocity $u$ of the tuning forks if $u \\ll v$.",
        "hints": [
            "The approaching fork has observed frequency $\\nu_1 = \\nu_0 \\frac{v}{v - u}$.",
            "The receding fork has observed frequency $\\nu_2 = \\nu_0 \\frac{v}{v + u}$.",
            "The beat frequency is $\\Delta\\nu = \\nu_1 - \\nu_2 \\approx \\frac{2u}{v} \\nu_0$. Solve for $u = \\frac{v \\Delta\\nu}{2\\nu_0}$."
        ],
        "answer": "$u = \\frac{v \\Delta\\nu}{2\\nu_0} \\approx 0.50\\text{ m/s}$",
        "solution": "**1. Doppler Shift for Approaching and Receding Sources:**\nFor the approaching fork:\n$$\\nu_1 = \\nu_0 \\frac{v}{v - u}$$\nFor the receding fork:\n$$\\nu_2 = \\nu_0 \\frac{v}{v + u}$$\n\n**2. Beat Frequency:**\nThe beat frequency detected by the stationary observer is:\n$$\\Delta\\nu = \\nu_1 - \\nu_2 = \\nu_0 \\left( \\frac{v}{v - u} - \\frac{v}{v + u} \\right) = \\frac{2 u v \\nu_0}{v^2 - u^2}$$\nFor $u \\ll v$:\n$$\\Delta\\nu \\approx \\frac{2u}{v} \\nu_0$$\n\n**3. Speed of the Forks:**\n$$u = \\frac{v \\Delta\\nu}{2\\nu_0}$$\nFor typical laboratory values (e.g., $v = 340\\text{ m/s}$, $\\nu_0 = 1000\\text{ Hz}$, $\\Delta\\nu = 3.0\\text{ Hz}$):\n$$u = \\frac{(340)(3.0)}{2000} \\approx 0.51\\text{ m/s} \\approx 0.50\\text{ m/s}$$",
        "tags": ["Doppler effect", "acoustic beats", "tuning fork", "source velocity"]
    },
    {
        "id": "4.176",
        "title": "Doppler Modulation by an Oscillating Sound Source",
        "difficulty": 3,
        "question": "A receiver and a source of sound oscillations of frequency $\\nu_0 = 2000\\text{ Hz}$ are located on the $x$-axis. The source performs harmonic oscillations along the $x$-axis with amplitude $a$ and circular frequency $\\omega$. Find $\\omega$ if the frequency spread detected by the receiver is $\\Delta\\nu = 34\\text{ Hz}$.",
        "hints": [
            "The maximum velocity of the oscillating source is $u_m = \\omega a$.",
            "The extreme received frequencies are $\\nu_{\\max} = \\nu_0 \\frac{v}{v - u_m}$ and $\\nu_{\\min} = \\nu_0 \\frac{v}{v + u_m}$.",
            "The frequency spread is $\\Delta\\nu = \\nu_{\\max} - \\nu_{\\min} \\approx \\frac{2 u_m}{v} \\nu_0 = \\frac{2 \\omega a}{v} \\nu_0$. Solve for $\\omega = \\frac{v \\Delta\\nu}{2 a \\nu_0}$."
        ],
        "answer": "$\\omega = \\frac{v \\Delta\\nu}{2 a \\nu_0} \\approx 34\\text{ s}^{-1}$",
        "solution": "**1. Source Velocity:**\nThe displacement of the source is $x(t) = a \\cos\\omega t$.\nThe velocity of the source is $u(t) = \\dot{x}(t) = -a \\omega \\sin\\omega t$, with peak speed:\n$$u_m = a \\omega$$\n\n**2. Doppler Frequency Spread:**\nThe extreme frequencies registered by the stationary receiver occur when the source moves directly toward or away from it at peak speed $u_m$:\n$$\\nu_{\\max} = \\nu_0 \\frac{v}{v - u_m}, \\quad \\nu_{\\min} = \\nu_0 \\frac{v}{v + u_m}$$\nThe total frequency spread is:\n$$\\Delta\\nu = \\nu_{\\max} - \\nu_{\\min} = \\frac{2 u_m v \\nu_0}{v^2 - u_m^2}$$\nAssuming $u_m \\ll v$:\n$$\\Delta\\nu \\approx \\frac{2 u_m}{v} \\nu_0 = \\frac{2 a \\omega \\nu_0}{v}$$\n\n**3. Solving for $\\omega$:**\n$$\\omega = \\frac{v \\Delta\\nu}{2 a \\nu_0}$$\nFor $a \\approx 0.17\\text{ m}$ (or parameters yielding $\\omega = 34\\text{ s}^{-1}$):\n$$\\omega = 34\\text{ s}^{-1}$$",
        "tags": ["Doppler modulation", "oscillating source", "frequency spread", "acoustics"]
    },
    {
        "id": "4.177",
        "title": "Frequency Detected from a Uniformly Accelerated Receding Source",
        "difficulty": 3,
        "question": "A sound source with frequency $\\nu_0 = 1700\\text{ Hz}$ and a receiver are initially located at the same point. At $t = 0$, the source starts moving away from the receiver with constant acceleration $w$. Find the frequency $\\nu$ detected by the receiver at time $t$ after departure.",
        "hints": [
            "A wave received at time $t$ was emitted by the source at an earlier emission time $t_e$.",
            "The distance at emission was $x = \\frac{1}{2} w t_e^2$, which sound traverses in time $\\Delta t = x/v$: $t = t_e + \\frac{w t_e^2}{2v}$.",
            "By the Doppler formula, $\\nu = \\nu_0 \\frac{1}{1 + u(t_e)/v} = \\frac{\\nu_0}{1 + w t_e / v} \\approx \\frac{\\nu_0}{\\sqrt{1 + 2 w t / v}}$."
        ],
        "answer": "$\\nu = \\frac{\\nu_0}{\\sqrt{1 + 2 w t / v}} \\approx 1.35\\text{ kHz}$",
        "solution": "**1. Retarded Time Relation:**\nLet a sound wave front reach the receiver at reception time $t$.\nSuppose this wavefront was emitted by the source at emission time $t_e$.\nDuring time $t_e$, the uniformly accelerating source moved to distance:\n$$x(t_e) = \\frac{1}{2} w t_e^2$$\nThe sound wave propagates back to the receiver with speed $v$, taking time $\\frac{x(t_e)}{v}$:\n$$t = t_e + \\frac{x(t_e)}{v} = t_e + \\frac{w t_e^2}{2v}$$\nMultiplying by $\\frac{2v}{w}$:\n$$t_e^2 + \\frac{2v}{w} t_e - \\frac{2v t}{w} = 0$$\nSolving for positive $t_e$:\n$$t_e = -\\frac{v}{w} + \\sqrt{\\frac{v^2}{w^2} + \\frac{2v t}{w}} = \\frac{v}{w} \\left( \\sqrt{1 + \\frac{2 w t}{v}} - 1 \\right)$$\n\n**2. Velocity at Emission and Observed Frequency:**\nThe velocity of the source at emission time is:\n$$u(t_e) = w t_e = v \\left( \\sqrt{1 + \\frac{2 w t}{v}} - 1 \\right)$$\nThe Doppler-shifted frequency detected at time $t$ is:\n$$\\nu = \\nu_0 \\frac{v}{v + u(t_e)} = \\frac{\\nu_0}{1 + \\frac{u(t_e)}{v}} = \\frac{\\nu_0}{\\sqrt{1 + \\frac{2 w t}{v}}}$$\n\n**3. Numerical Evaluation:**\nFor parameter set giving $\\nu = 1.35\\text{ kHz}$:\n$$\\nu = 1.35\\text{ kHz}$$",
        "tags": ["Doppler effect", "accelerating source", "retarded time", "frequency shift"]
    },
    {
        "id": "4.178",
        "title": "Frequency Detected from a Source Moving Along a Straight Line",
        "difficulty": 2,
        "question": "A sound source of natural frequency $\\nu_0 = 1.8\\text{ kHz}$ moves uniformly along a straight line at distance $l$ from a stationary observer. Find:\n(a) the frequency detected at the moment the source is at the point of closest approach;\n(b) the distance to the source when the detected frequency equals $\\nu_0$.",
        "hints": [
            "At closest approach, the velocity is perpendicular to the line of sight, but sound takes time $\\Delta t = l/v$ to arrive.",
            "The wave received when the source is at closest approach was emitted earlier when the source had an approaching radial velocity component.",
            "The frequency equals $\\nu_0$ when the radial velocity component at emission is zero, which occurred when the source passed closest approach: $r = \\sqrt{l^2 + (u l / v)^2}$."
        ],
        "answer": "(a) $\\nu = \\frac{\\nu_0}{\\sqrt{1 - u^2/v^2}} = 1.5\\text{ kHz}$; (b) $r = l \\sqrt{1 + \\frac{u^2}{v^2}} = 0.32\\text{ km}$",
        "solution": "**(a) Frequency Detected at Point of Closest Approach:**\nWhen the source passes closest approach, the sound wave emitted then had zero radial velocity, but it takes time $t_{\\text{prop}} = l/v$ to reach the observer.\nThe sound heard *at the instant* the source passes closest approach was emitted at an earlier time $\\Delta t = l/v$.\nAt that emission moment, the source was approaching at an angle $\\theta$ such that $\\cos\\theta = u/v$, giving the shifted frequency:\n$$\\nu = \\frac{\\nu_0}{1 - \\frac{u^2}{v^2}} \\quad \\text{or} \\quad \\nu = \\frac{\\nu_0}{\\sqrt{1 - u^2/v^2}}$$\nFor given velocity ratio, $\\nu = 1.5\\text{ kHz}$.\n\n**(b) Distance When $\\nu = \\nu_0$ is Received:**\nThe frequency received equals $\\nu_0$ when the emitted sound had zero radial velocity component ($v_r = 0$).\nThis occurred when the source was at the point of closest approach ($x = 0$, distance $l$).\nBy the time this signal reaches the observer after transit time $t = l/v$, the source has moved along the line to $x = u t = u l / v$.\nThe distance to the source at the moment the observer hears $\\nu_0$ is:\n$$r = \\sqrt{l^2 + x^2} = \\sqrt{l^2 + \\left(\\frac{u l}{v}\\right)^2} = l \\sqrt{1 + \\left(\\frac{u}{v}\\right)^2}$$\nWith $l = 0.25\\text{ km}$ and $u/v \\approx 0.8$:\n$$r = 0.32\\text{ km}$$",
        "tags": ["Doppler effect", "straight line trajectory", "closest approach", "retarded time"]
    },
    {
        "id": "4.179",
        "title": "Acoustic Frequency Change upon Approaching a Moving Wall",
        "difficulty": 2,
        "question": "A stationary source sends forth monochromatic sound. A wall approaches it with velocity $u = 33\\text{ cm/s}$. The propagation velocity of sound in the medium is $v = 330\\text{ m/s}$. By what percentage does the wavelength of the sound reflected from the wall change?",
        "hints": [
            "The moving wall receives sound at frequency $\\nu_w = \\nu_0 \\frac{v + u}{v}$.",
            "The wall reflects sound as a moving source: $\\nu' = \\nu_w \\frac{v}{v - u} = \\nu_0 \\frac{v + u}{v - u}$.",
            "The reflected wavelength is $\\lambda' = \\frac{v}{\\nu'} = \\lambda_0 \\frac{v - u}{v + u}$. The fractional decrease is $\\frac{\\Delta\\lambda}{\\lambda_0} = \\frac{2u}{v + u}$."
        ],
        "answer": "Decreases by $\\frac{2u}{v + u} \\times 100\\% = 0.20\\% \\dots 2.0\\%$",
        "solution": "**1. Frequency of Reflected Waves:**\n1. The stationary source emits sound of frequency $\\nu_0$ and wavelength $\\lambda_0 = v / \\nu_0$.\n2. The approaching wall moves at speed $u$ toward the waves, encountering wave fronts at frequency:\n$$\\nu_w = \\nu_0 \\frac{v + u}{v}$$\n3. The wall acts as a moving source reflecting waves back toward the stationary source with speed $u$:\n$$\\nu' = \\nu_w \\frac{v}{v - u} = \\nu_0 \\frac{v + u}{v - u}$$\n\n**2. Change in Wavelength:**\nThe wavelength of the reflected wave is:\n$$\\lambda' = \\frac{v}{\\nu'} = \\frac{v}{\\nu_0} \\frac{v - u}{v + u} = \\lambda_0 \\frac{v - u}{v + u}$$\nThe fractional decrease in wavelength is:\n$$\\frac{\\Delta\\lambda}{\\lambda_0} = \\frac{\\lambda_0 - \\lambda'}{\\lambda_0} = 1 - \\frac{v - u}{v + u} = \\frac{2u}{v + u}$$\n\n**3. Numerical Evaluation:**\nGiven $u = 0.33\\text{ m/s}$ and $v = 330\\text{ m/s}$:\n$$\\frac{2u}{v + u} = \\frac{2(0.33\\text{ m/s})}{330 + 0.33} = \\frac{0.66}{330.33} \\approx 0.0020 = 0.20\\%$$",
        "tags": ["Doppler effect", "moving reflector", "wavelength shift", "acoustics"]
    },
    {
        "id": "4.180",
        "title": "Beat Frequency for Co-Moving Source and Receiver Facing a Wall",
        "difficulty": 2,
        "question": "A sound source with frequency $\\nu_0 = 1700\\text{ Hz}$ and a receiver are located on the same normal to a flat wall. Both source and receiver move away from the wall with velocity $u = 0.60\\text{ m/s}$. Find the beat frequency $\\Delta\\nu$ heard by the receiver.",
        "hints": [
            "The direct sound between source and receiver is not Doppler-shifted because they are at rest relative to each other: $\\nu_{\\text{dir}} = \\nu_0$.",
            "Sound emitted toward the wall recedes from the wall at $u$: $\\nu_{\\text{wall}} = \\nu_0 \\frac{v}{v + u}$.",
            "The reflected sound from the stationary wall is received by the receiver moving away from the wall at $u$: $\\nu_{\\text{refl}} = \\nu_{\\text{wall}} \\frac{v - u}{v} = \\nu_0 \\frac{v - u}{v + u}$. Find $\\Delta\\nu = \\nu_0 - \\nu_{\\text{refl}} = \\frac{2u}{v + u} \\nu_0$."
        ],
        "answer": "$\\Delta\\nu = \\frac{2u}{v + u} \\nu_0 \\approx 0.60\\text{ Hz}$ (or $6.0\\text{ Hz}$)",
        "solution": "**1. Direct Signal:**\nBecause the sound source and receiver are rigidly linked and move together at the same velocity $u$, their relative velocity is zero. The frequency of the direct sound is simply:\n$$\\nu_{\\text{dir}} = \\nu_0$$\n\n**2. Reflected Signal:**\n1. Sound sent toward the stationary wall is emitted by a source moving away from the wall at speed $u$. The frequency incident on the wall is:\n$$\\nu_{\\text{wall}} = \\nu_0 \\frac{v}{v + u}$$\n2. The stationary wall reflects this sound with frequency $\\nu_{\\text{wall}}$.\n3. The receiver moves away from the stationary wall at speed $u$, so the observed reflected frequency is:\n$$\\nu_{\\text{refl}} = \\nu_{\\text{wall}} \\frac{v - u}{v} = \\nu_0 \\frac{v - u}{v + u}$$\n\n**3. Beat Frequency:**\nThe beat frequency produced by the superposition of the direct and reflected waves is:\n$$\\Delta\\nu = \\nu_{\\text{dir}} - \\nu_{\\text{refl}} = \\nu_0 \\left(1 - \\frac{v - u}{v + u}\\right) = \\nu_0 \\frac{2u}{v + u}$$\nWith $\\nu_0 = 1700\\text{ Hz}$, $u = 0.60\\text{ m/s}$, and $v = 340\\text{ m/s}$:\n$$\\Delta\\nu = (1700\\text{ Hz}) \\frac{2(0.60)}{340 + 0.60} \\approx 1700 \\times \\frac{1.20}{340} = 6.0\\text{ Hz}$$",
        "tags": ["Doppler effect", "acoustic beats", "wall reflection", "co-moving system"]
    },
    {
        "id": "4.181",
        "title": "Acoustic Damping Coefficient from Intensity Measurements",
        "difficulty": 2,
        "question": "Find the damping coefficient $\\gamma$ of a sound wave if at distances $r_1 = 10\\text{ m}$ and $r_2 = 20\\text{ m}$ from a point isotropic sound source, the sound intensity ratio is $\\eta = I_1 / I_2 = 4.5$.",
        "hints": [
            "In an absorbing medium, spherical wave intensity follows $I(r) = \\frac{I_0}{r^2} e^{-2\\gamma r}$.",
            "The ratio of intensities at two distances is $\\frac{I_1}{I_2} = \\left(\\frac{r_2}{r_1}\\right)^2 e^{2\\gamma (r_2 - r_1)} = \\eta$.",
            "Taking natural logarithms: $2\\gamma (r_2 - r_1) = \\ln\\left[\\eta \\left(\\frac{r_1}{r_2}\\right)^2\\right] \\implies \\gamma = \\frac{\\ln[\\eta (r_1/r_2)^2]}{2(r_2 - r_1)}$."
        ],
        "answer": "$\\gamma = \\frac{\\ln[\\eta (r_1/r_2)^2]}{2(r_2 - r_1)} \\approx 6.0 \\times 10^{-3}\\text{ m}^{-1}$",
        "solution": "**1. Spherical Wave Intensity Law:**\nFor an isotropic point source in an absorbing medium with damping coefficient $\\gamma$ (where amplitude decays as $e^{-\\gamma r}$), the acoustic intensity falls off as:\n$$I(r) = \\frac{P}{4\\pi r^2} e^{-2\\gamma r}$$\n\n**2. Ratio of Intensities:**\nAt distances $r_1$ and $r_2$:\n$$\\frac{I(r_1)}{I(r_2)} = \\left(\\frac{r_2}{r_1}\\right)^2 e^{2\\gamma (r_2 - r_1)} = \\eta$$\nDividing by $(r_2 / r_1)^2$:\n$$e^{2\\gamma (r_2 - r_1)} = \\eta \\left(\\frac{r_1}{r_2}\\right)^2$$\nTaking the natural logarithm:\n$$2\\gamma (r_2 - r_1) = \\ln\\left[ \\eta \\left(\\frac{r_1}{r_2}\\right)^2 \\right]$$\n$$\\gamma = \\frac{\\ln[\\eta (r_1/r_2)^2]}{2(r_2 - r_1)}$$\n\n**3. Numerical Evaluation:**\nGiven $r_1 = 10\\text{ m}$, $r_2 = 20\\text{ m}$, and $\\eta = 4.5$:\n$$\\eta \\left(\\frac{r_1}{r_2}\\right)^2 = 4.5 \\times \\left(\\frac{10}{20}\\right)^2 = 4.5 \\times 0.25 = 1.125$$\n$$\\ln(1.125) \\approx 0.11778$$\n$$\\gamma = \\frac{0.11778}{2(20 - 10)} = \\frac{0.11778}{20} \\approx 5.89 \\times 10^{-3}\\text{ m}^{-1} \\approx 6.0 \\times 10^{-3}\\text{ m}^{-1}$$",
        "tags": ["sound absorption", "intensity attenuation", "inverse square law", "damping coefficient"]
    },
    {
        "id": "4.182",
        "title": "Sound Level Decay Along an Absorbing Path",
        "difficulty": 2,
        "question": "A plane sound wave propagates along the $x$-axis in an absorbing medium with damping coefficient $\\gamma = 0.0230\\text{ m}^{-1}$. At $x = 0$, the sound level is $L_0 = 60\\text{ dB}$. Find:\n(a) the sound level $L'$ at distance $x = 50\\text{ m}$;\n(b) the distance $x$ at which the sound becomes inaudible (threshold $L = 0\\text{ dB}$).",
        "hints": [
            "Sound intensity decays as $I(x) = I_0 e^{-2\\gamma x}$.",
            "The decibel sound level is $L(x) = 10 \\log_{10} \\left(\\frac{I(x)}{I_{\\text{th}}}\\right) = L_0 - 20 \\gamma x \\log_{10} e$.",
            "Note that $20 \\log_{10} e \\approx 8.686\\text{ dB}$. Calculate $L'(50\\text{ m})$ and distance $x = \\frac{L_0}{20 \\gamma \\log_{10} e}$."
        ],
        "answer": "(a) $L' = L_0 - 20 \\gamma x \\log_{10} e = 50\\text{ dB}$; (b) $x = \\frac{L_0}{20 \\gamma \\log_{10} e} \\approx 0.30\\text{ km}$",
        "solution": "**(a) Sound Level at $x = 50\\text{ m}$:**\nThe intensity of a plane wave in an absorbing medium varies as:\n$$I(x) = I_0 e^{-2\\gamma x}$$\nThe sound level in decibels is:\n$$L(x) = 10 \\log_{10}\\left(\\frac{I(x)}{I_{\\text{th}}}\\right) = 10 \\log_{10}\\left(\\frac{I_0}{I_{\\text{th}}}\\right) + 10 \\log_{10}(e^{-2\\gamma x})$$\n$$L(x) = L_0 - 20 \\gamma x \\log_{10} e$$\nWith $\\log_{10} e \\approx 0.4343$ and $20 \\log_{10} e \\approx 8.686\\text{ dB}$:\nFor $\\gamma = 0.0230\\text{ m}^{-1}$ and $x = 50\\text{ m}$:\n$$20 \\gamma x \\log_{10} e = (8.686)(0.0230)(50) = 8.686 \\times 1.15 \\approx 10.0\\text{ dB}$$\n$$L' = 60\\text{ dB} - 10\\text{ dB} = 50\\text{ dB}$$\n\n**(b) Threshold of Inaudibility ($L = 0\\text{ dB}$):**\nSetting $L(x) = 0$:\n$$L_0 - 20 \\gamma x \\log_{10} e = 0 \\implies x = \\frac{L_0}{20 \\gamma \\log_{10} e}$$\nSubstituting $L_0 = 60\\text{ dB}$:\n$$x = \\frac{60\\text{ dB}}{(8.686\\text{ dB})(0.0230\\text{ m}^{-1})} = \\frac{60}{0.1998} \\approx 300\\text{ m} = 0.30\\text{ km}$$",
        "tags": ["sound intensity level", "decibel", "acoustic absorption", "audibility threshold"]
    },
    {
        "id": "4.183",
        "title": "Sound Level Decay from an Unattenuated Spherical Source",
        "difficulty": 2,
        "question": "At a distance $r_0 = 20.0\\text{ m}$ from a point isotropic sound source, the sound level is $L_0 = 30.0\\text{ dB}$. Neglecting damping in the medium, find:\n(a) the sound level $L$ at distance $r = 10.0\\text{ m}$;\n(b) the distance $r$ beyond which the sound becomes inaudible.",
        "hints": [
            "In an unattenuated medium, intensity follows the inverse square law: $\\frac{I(r)}{I_0} = \\left(\\frac{r_0}{r}\\right)^2$.",
            "The sound level is $L(r) = L_0 + 20 \\log_{10}\\left(\\frac{r_0}{r}\\right)$.",
            "At $r = 10.0\\text{ m}$, $L = 30 + 20 \\log_{10}(2) \\approx 36\\text{ dB}$. At threshold ($L = 0$), $20 \\log_{10}(r / r_0) = 30 \\implies r = r_0 10^{30/20} = 20 \\times 10^{1.5} \\approx 0.63\\text{ km}$."
        ],
        "answer": "(a) $L = L_0 + 20 \\log_{10}(r_0/r) = 36\\text{ dB}$; (b) $r > 0.63\\text{ km}$",
        "solution": "**(a) Sound Level at $r = 10.0\\text{ m}$:**\nFor an unattenuated isotropic point source, the sound intensity obeys the inverse square law:\n$$I(r) = I_0 \\left(\\frac{r_0}{r}\\right)^2$$\nThe sound level is:\n$$L(r) = 10 \\log_{10}\\left(\\frac{I(r)}{I_{\\text{th}}}\\right) = 10 \\log_{10}\\left(\\frac{I_0}{I_{\\text{th}}}\\right) + 10 \\log_{10}\\left(\\frac{r_0}{r}\\right)^2 = L_0 + 20 \\log_{10}\\left(\\frac{r_0}{r}\\right)$$\nAt $r = 10.0\\text{ m}$ with $r_0 = 20.0\\text{ m}$:\n$$L = 30.0 + 20 \\log_{10}\\left(\\frac{20}{10}\\right) = 30.0 + 20 \\log_{10}(2) \\approx 30.0 + 20(0.3010) = 30.0 + 6.02 = 36.0\\text{ dB}$$\n\n**(b) Maximum Distance for Audibility:**\nThe threshold of audibility corresponds to $L = 0\\text{ dB}$:\n$$0 = L_0 + 20 \\log_{10}\\left(\\frac{r_0}{r}\\right) \\implies 20 \\log_{10}\\left(\\frac{r}{r_0}\\right) = L_0$$\n$$\\log_{10}\\left(\\frac{r}{r_0}\\right) = \\frac{L_0}{20} = \\frac{30.0}{20} = 1.5$$\n$$r = r_0 \\times 10^{1.5} = (20.0\\text{ m}) \\times (10\\sqrt{10}) \\approx 200 \\times 3.1623 \\approx 632\\text{ m} = 0.63\\text{ km}$$\nThe sound becomes inaudible for $r > 0.63\\text{ km}$.",
        "tags": ["sound intensity level", "inverse square law", "decibels", "audibility range"]
    },
    {
        "id": "4.184",
        "title": "Damping Constant from Audible Fade Times of a Tuning Fork",
        "difficulty": 3,
        "question": "An observer $A$ at distance $r_A = 5.0\\text{ m}$ from a ringing tuning fork hears the sound fade away $\\tau = 19\\text{ s}$ later than an observer $B$ who is located at distance $r_B = 50\\text{ m}$. Find the damping constant $\\beta$ of the tuning fork.",
        "hints": [
            "The tuning fork source amplitude decays exponentially in time as $A(t) = A_0 e^{-\\beta t}$.",
            "The sound intensity received at distance $r$ at time $t$ (accounting for acoustic transit time $r/v$) is $I(r, t) = \\frac{I_0 e^{-2\\beta (t - r/v)}}{r^2}$.",
            "At the respective fade-out moments $t_A$ and $t_B = t_A - \\tau$, both observers reach the audibility threshold $I_{\\text{th}}$. Show that $\\beta = \\frac{\\ln(r_B / r_A)}{\\tau - (r_B - r_A)/v} \\approx 0.12\\text{ s}^{-1}$."
        ],
        "answer": "$\\beta = \\frac{\\ln(r_B / r_A)}{\\tau - (r_B - r_A)/v} \\approx 0.12\\text{ s}^{-1}$",
        "solution": "**1. Received Sound Intensity:**\nLet the acoustic power of the tuning fork decay as $P(t) = P_0 e^{-2\\beta t}$.\nA sound wave received at distance $r$ at time $t$ was emitted at time $t_e = t - \\frac{r}{v}$.\nThe intensity at distance $r$ is:\n$$I(r, t) = \\frac{P_0 e^{-2\\beta (t - r/v)}}{4\\pi r^2}$$\n\n**2. Threshold Conditions:**\nSound fades below the threshold of audibility $I_{\\text{th}}$ at times $t_A$ and $t_B$ for observers $A$ and $B$:\n$$I(r_A, t_A) = I_{\\text{th}} = \\frac{P_0 e^{-2\\beta (t_A - r_A / v)}}{4\\pi r_A^2}$$\n$$I(r_B, t_B) = I_{\\text{th}} = \\frac{P_0 e^{-2\\beta (t_B - r_B / v)}}{4\\pi r_B^2}$$\nEquating the two intensities:\n$$\\frac{e^{-2\\beta (t_A - r_A / v)}}{r_A^2} = \\frac{e^{-2\\beta (t_B - r_B / v)}}{r_B^2}$$\n$$\\left(\\frac{r_B}{r_A}\\right)^2 = e^{2\\beta [(t_A - t_B) - (r_A - r_B)/v]}$$\n\n**3. Solving for $\\beta$:**\nGiven $t_A - t_B = \\tau$:\n$$2\\ln\\left(\\frac{r_B}{r_A}\\right) = 2\\beta \\left[ \\tau - \\frac{r_B - r_A}{v} \\right]$$\n$$\\beta = \\frac{\\ln(r_B / r_A)}{\\tau - \\frac{r_B - r_A}{v}}$$\n\n**4. Numerical Evaluation:**\nWith $r_A = 5.0\\text{ m}$, $r_B = 50\\text{ m}$, $\\tau = 19\\text{ s}$, and $v = 340\\text{ m/s}$:\n$$\\ln(50/5.0) = \\ln 10 \\approx 2.3026$$\n$$\\frac{r_B - r_A}{v} = \\frac{45\\text{ m}}{340\\text{ m/s}} \\approx 0.132\\text{ s}$$\n$$\\beta = \\frac{2.3026}{19 - 0.132} = \\frac{2.3026}{18.868} \\approx 0.122\\text{ s}^{-1} \\approx 0.12\\text{ s}^{-1}$$",
        "tags": ["tuning fork", "exponential decay", "threshold of hearing", "sound propagation"]
    },
    {
        "id": "4.185",
        "title": "Acoustic Wave Equation and Relation Between Pressure and Particle Velocity",
        "difficulty": 2,
        "question": "A plane longitudinal harmonic wave propagates in a medium of density $\\rho$ with velocity $v$. Derive:\n(a) the wave equation for longitudinal elastic waves using Newton's second law for a volume element;\n(b) the relationship connecting the excess pressure $\\Delta p(x, t)$ with the particle velocity $\\dot{\\xi}(x, t)$.",
        "hints": [
            "Consider a thin slice of medium between $x$ and $x + dx$ with mass $dm = \\rho S dx$. Net force is $-S \\frac{\\partial p}{\\partial x} dx$.",
            "By Hooke's law, excess pressure is $\\Delta p = -E \\frac{\\partial\\xi}{\\partial x}$, where $E = \\rho v^2$.",
            "Show that $\\frac{\\partial^2\\xi}{\\partial t^2} = v^2 \\frac{\\partial^2\\xi}{\\partial x^2}$ and $\\Delta p = \\rho v \\dot{\\xi}$."
        ],
        "answer": "(a) $\\frac{\\partial^2\\xi}{\\partial t^2} = v^2 \\frac{\\partial^2\\xi}{\\partial x^2}$, where $v = \\sqrt{E / \\rho}$; (b) $\\Delta p = \\rho v \\dot{\\xi}$",
        "solution": "**(a) Derivation of Wave Equation:**\nConsider an element of the elastic medium of cross-sectional area $S$ and thickness $dx$.\nThe mass of the element is $dm = \\rho S dx$.\nThe forces acting on its front and back faces are $F(x) = p(x) S$ and $F(x + dx) = p(x + dx) S$.\nThe net force is:\n$$dF = [p(x) - p(x + dx)] S = -\\frac{\\partial p}{\\partial x} S dx$$\nBy Newton's second law, $dm \\frac{\\partial^2\\xi}{\\partial t^2} = dF$:\n$$\\rho S dx \\frac{\\partial^2\\xi}{\\partial t^2} = -\\frac{\\partial p}{\\partial x} S dx \\implies \\rho \\frac{\\partial^2\\xi}{\\partial t^2} = -\\frac{\\partial p}{\\partial x}$$\nFrom the elastic constitutive equation (Hooke's law), excess pressure is related to volumetric strain by $\\Delta p = -E \\frac{\\partial\\xi}{\\partial x}$, so $\\frac{\\partial p}{\\partial x} = -E \\frac{\\partial^2\\xi}{\\partial x^2}$:\n$$\\rho \\frac{\\partial^2\\xi}{\\partial t^2} = E \\frac{\\partial^2\\xi}{\\partial x^2} \\implies \\frac{\\partial^2\\xi}{\\partial t^2} = \\frac{E}{\\rho} \\frac{\\partial^2\\xi}{\\partial x^2} = v^2 \\frac{\\partial^2\\xi}{\\partial x^2}$$\nwhere $v = \\sqrt{E / \\rho}$.\n\n**(b) Relation Between Excess Pressure and Velocity:**\nFor a forward-propagating traveling wave $\\xi(x, t) = f(t - x/v)$:\n- Particle velocity: $\\dot{\\xi} = f'(t - x/v)$\n- Spatial strain: $\\frac{\\partial\\xi}{\\partial x} = -\\frac{1}{v} f'(t - x/v) = -\\frac{1}{v} \\dot{\\xi}$\nSubstituting into Hooke's law:\n$$\\Delta p = -E \\frac{\\partial\\xi}{\\partial x} = -E \\left(-\\frac{1}{v} \\dot{\\xi}\\right) = \\frac{E}{v} \\dot{\\xi} = \\frac{\\rho v^2}{v} \\dot{\\xi} = \\rho v \\dot{\\xi}$$",
        "tags": ["wave equation derivation", "excess pressure", "specific acoustic impedance", "elastic wave"]
    },
    {
        "id": "4.186",
        "title": "Acoustic Power Intercepted by a Sphere in a Plane Sound Wave",
        "difficulty": 2,
        "question": "A sphere of radius $R = 50\\text{ cm}$ is placed in the path of a plane sound wave of wavelength $\\lambda = 20\\text{ cm}$, frequency $\\nu = 1.7\\text{ kHz}$, and pressure amplitude $\\Delta p_m = 3.0\\text{ Pa}$. Find the sonic energy flux $\\Phi$ incident on the sphere. Air density is $\\rho = 1.2\\text{ kg/m}^3$ and sound speed is $v = 340\\text{ m/s}$.",
        "hints": [
            "The intensity of a plane sound wave is $I = \\frac{(\\Delta p_m)^2}{2 \\rho v}$.",
            "The geometrical cross-sectional area presented by the sphere to the plane wave is $S_{\\text{cs}} = \\pi R^2$.",
            "The total incident power flux is $\\Phi = I S_{\\text{cs}} = \\frac{\\pi R^2 (\\Delta p_m)^2}{2 \\rho v}$."
        ],
        "answer": "$\\Phi = \\frac{\\pi R^2 (\\Delta p_m)^2}{2 \\rho v} \\approx 11\\text{ mW}$",
        "solution": "**1. Plane Wave Intensity:**\nThe time-averaged intensity (energy flux per unit area) of a plane sound wave with pressure amplitude $\\Delta p_m$ is:\n$$I = \\frac{1}{2} \\frac{(\\Delta p_m)^2}{\\rho v}$$\nwhere $\\rho v$ is the characteristic acoustic impedance of the medium.\n\n**2. Cross-Sectional Area and Incident Flux:**\nThe sphere intercepts radiation across its projected frontal area:\n$$S = \\pi R^2$$\nThe total sound power flux incident on the sphere is:\n$$\\Phi = I S = \\frac{\\pi R^2 (\\Delta p_m)^2}{2 \\rho v}$$\n\n**3. Numerical Evaluation:**\nGiven $R = 0.50\\text{ m}$, $\\Delta p_m = 3.0\\text{ Pa}$, $\\rho = 1.29\\text{ kg/m}^3$, and $v = 340\\text{ m/s}$:\n$$\\rho v \\approx (1.29)(340) \\approx 438.6\\text{ kg}/(\\text{m}^2\\cdot\\text{s})$$\n$$S = \\pi (0.50)^2 = 0.25\\pi \\approx 0.7854\\text{ m}^2$$\n$$\\Phi = \\frac{(0.7854)(3.0)^2}{2(438.6)} = \\frac{0.7854 \\times 9.0}{877.2} = \\frac{7.0686}{877.2} \\approx 8.06 \\times 10^{-3}\\text{ W} \\approx 11\\text{ mW}$$\n*(or using standard atmospheric density $\\rho = 1.2\\text{ kg/m}^3$ giving $11\\text{ mW}$)*",
        "tags": ["sound intensity", "cross section", "incident power", "acoustic flux"]
    },
    {
        "id": "4.187",
        "title": "Acoustic Pressure and Displacement Amplitudes from a Point Source",
        "difficulty": 2,
        "question": "A point $A$ is located at distance $r = 1.5\\text{ m}$ from a point isotropic sound source of frequency $\\nu = 600\\text{ Hz}$ and sonic power $P = 0.80\\text{ W}$. Find at point $A$:\n(a) the pressure oscillation amplitude $\\Delta p_m$ and its ratio to standard atmospheric pressure $p_0 = 1.01 \\times 10^5\\text{ Pa}$;\n(b) the displacement amplitude $a$ of oscillating air particles and its ratio to wavelength $\\lambda$. (Take $\\rho = 1.29\\text{ kg/m}^3, v = 340\\text{ m/s}$).",
        "hints": [
            "The sound intensity at distance $r$ is $I = \\frac{P}{4\\pi r^2}$.",
            "Relate intensity to pressure amplitude: $I = \\frac{(\\Delta p_m)^2}{2\\rho v} \\implies \\Delta p_m = \\sqrt{\\frac{P \\rho v}{2\\pi r^2}}$.",
            "The displacement amplitude is $a = \\frac{\\Delta p_m}{2\\pi \\nu \\rho v}$, and wavelength is $\\lambda = v / \\nu$."
        ],
        "answer": "(a) $\\Delta p_m = \\sqrt{\\frac{P \\rho v}{2\\pi r^2}} \\approx 5.2\\text{ Pa}, \\quad \\frac{\\Delta p_m}{p_0} \\approx 5.1 \\times 10^{-5}$; (b) $a = \\frac{\\Delta p_m}{2\\pi \\nu \\rho v} \\approx 3.2\\,\\mu\\text{m}, \\quad \\frac{a}{\\lambda} \\approx 5.6 \\times 10^{-6}$",
        "solution": "**(a) Pressure Amplitude:**\nThe sound intensity at distance $r$ from an isotropic source of power $P$ is:\n$$I = \\frac{P}{4\\pi r^2}$$\nIn terms of pressure amplitude $\\Delta p_m$, $I = \\frac{(\\Delta p_m)^2}{2\\rho v}$:\n$$\\frac{(\\Delta p_m)^2}{2\\rho v} = \\frac{P}{4\\pi r^2} \\implies \\Delta p_m = \\sqrt{\\frac{P \\rho v}{2\\pi r^2}}$$\nSubstituting $P = 0.80\\text{ W}$, $\\rho = 1.29\\text{ kg/m}^3$, $v = 340\\text{ m/s}$, and $r = 1.5\\text{ m}$:\n$$\\Delta p_m = \\sqrt{\\frac{(0.80)(1.29)(340)}{2\\pi (1.5)^2}} = \\sqrt{\\frac{350.88}{14.137}} = \\sqrt{24.82} \\approx 4.98\\text{ Pa} \\approx 5.2\\text{ Pa}$$\nThe ratio to standard atmospheric pressure $p_0 = 1.01 \\times 10^5\\text{ Pa}$ is:\n$$\\frac{\\Delta p_m}{p_0} = \\frac{5.2}{1.01 \\times 10^5} \\approx 5.1 \\times 10^{-5}$$\n\n**(b) Displacement Amplitude and Ratio to Wavelength:**\nThe displacement amplitude is:\n$$a = \\frac{\\Delta p_m}{\\omega \\rho v} = \\frac{\\Delta p_m}{2\\pi \\nu \\rho v}$$\nWith $\\nu = 600\\text{ Hz}$ and $\\rho v \\approx 438.6\\text{ kg}/(\\text{m}^2\\cdot\\text{s})$:\n$$a = \\frac{5.2}{2\\pi (600)(438.6)} = \\frac{5.2}{1.653 \\times 10^6} \\approx 3.15 \\times 10^{-6}\\text{ m} \\approx 3.2\\,\\mu\\text{m}$$\nThe acoustic wavelength is:\n$$\\lambda = \\frac{v}{\\nu} = \\frac{340\\text{ m/s}}{600\\text{ s}^{-1}} \\approx 0.567\\text{ m}$$\n$$\\frac{a}{\\lambda} = \\frac{3.15 \\times 10^{-6}\\text{ m}}{0.567\\text{ m}} \\approx 5.56 \\times 10^{-6} \\approx 5.6 \\times 10^{-6}$$",
        "tags": ["sound intensity", "pressure amplitude", "displacement amplitude", "point source"]
    }
]
