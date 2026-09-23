"""
part5_ch5_5.py
Curated problems 5.200 to 5.223 (24 problems) of Irodov Chapter 5.5:
Dispersion and Absorption of Light.
"""

CH5_5_CURATED = [
    {
        "id": "5.200",
        "title": "Motion of a Free Electron in a Monochromatic Light Wave",
        "difficulty": 2,
        "question": "A free electron is located in the field of a monochromatic light wave of intensity $I = 150\\text{ W/m}^2$ and angular frequency $\\omega = 3.4 \\times 10^{15}\\text{ s}^{-1}$. Find:\n(a) the electron's oscillation amplitude $a$ and velocity amplitude $v$;\n(b) the ratio $F_m / F_e$ of the magnetic force amplitude to the electric force amplitude acting on the electron, and demonstrate that $F_m / F_e = \\frac{1}{2} \\frac{v}{c}$, where $c$ is the speed of light.",
        "hints": [
            "(a) Relate the light intensity to the electric field amplitude: $I = \\frac{1}{2} \\epsilon_0 c E_0^2 \\implies E_0 = \\sqrt{\\frac{2I}{\\epsilon_0 c}}$. The equation of motion is $m \\ddot{x} = -e E_0 \\cos\\omega t$, giving amplitude $a = \\frac{e E_0}{m \\omega^2}$ and velocity $v = \\omega a = \\frac{e E_0}{m \\omega}$.",
            "(b) In an electromagnetic plane wave, the magnetic field amplitude is $B_0 = E_0 / c$. The magnetic force is $F_m = e v B$, and the electric force is $F_e = e E$.",
            "Because $v(t)$ and $B(t)$ oscillate in quadrature with equal frequency, the maximum magnetic force is $F_m = \\frac{1}{2} e v B_0 = \\frac{e v E_0}{2 c}$. The ratio is $\\frac{F_m}{F_e} = \\frac{1}{2} \\frac{v}{c}$."
        ],
        "answer": "(a) $a = \\frac{e E_0}{m \\omega^2} = 5.0 \\times 10^{-16}\\text{ cm}$, $v = 1.7\\text{ cm/s}$ where $E_0 = \\sqrt{2I / (\\epsilon_0 c)}$;\n(b) $\\frac{F_m}{F_e} = \\frac{1}{2} \\frac{v}{c} = 2.9 \\times 10^{-11}$",
        "solution": "**1. Part (a): Electric Field and Electron Kinematics:**\nThe intensity of an electromagnetic wave in vacuum is:\n$$I = \\frac{1}{2} \\epsilon_0 c E_0^2 \\implies E_0 = \\sqrt{\\frac{2I}{\\epsilon_0 c}}$$\nFor $I = 150\\text{ W/m}^2$, $\\epsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}$, and $c = 3.0 \\times 10^8\\text{ m/s}$:\n$$E_0 = \\sqrt{\\frac{300}{(8.854 \\times 10^{-12})(3.0 \\times 10^8)}} = \\sqrt{\\frac{300}{2.656 \\times 10^{-3}}} \\approx \\sqrt{1.129 \\times 10^5} \\approx 336\\text{ V/m}$$\nThe equation of motion for a free electron of mass $m$ and charge $-e$ is:\n$$m \\ddot{x} = -e E_0 \\cos(\\omega t)$$\nIntegrating twice gives the oscillation displacement and velocity:\n$$x(t) = a \\cos(\\omega t), \\quad v(t) = -v_0 \\sin(\\omega t)$$\nwhere:\n$$a = \\frac{e E_0}{m \\omega^2}, \\quad v_0 = \\omega a = \\frac{e E_0}{m \\omega}$$\nSubstituting numerical values ($e = 1.602 \\times 10^{-19}\\text{ C}$, $m = 9.109 \\times 10^{-31}\\text{ kg}$, $\\omega = 3.4 \\times 10^{15}\\text{ s}^{-1}$):\n$$v_0 = \\frac{(1.602 \\times 10^{-19}\\text{ C})(336\\text{ V/m})}{(9.109 \\times 10^{-31}\\text{ kg})(3.4 \\times 10^{15}\\text{ s}^{-1})} = \\frac{5.383 \\times 10^{-17}}{3.097 \\times 10^{-15}} \\approx 0.0174\\text{ m/s} = 1.7\\text{ cm/s}$$\n$$a = \\frac{v_0}{\\omega} = \\frac{0.0174\\text{ m/s}}{3.4 \\times 10^{15}\\text{ s}^{-1}} \\approx 5.1 \\times 10^{-18}\\text{ m} = 5.1 \\times 10^{-16}\\text{ cm} \\approx 5.0 \\times 10^{-16}\\text{ cm}$$\n\n**2. Part (b): Ratio of Magnetic to Electric Forces:**\nThe Lorentz force is $\\mathbf{F} = -e (\\mathbf{E} + \\mathbf{v} \\times \\mathbf{B})$.\nThe electric force amplitude is $F_e = e E_0$.\nIn a plane wave, $B(t) = \\frac{E_0}{c} \\cos(\\omega t)$, while $v(t) = -v_0 \\sin(\\omega t)$.\nThe magnetic force is:\n$$F_m(t) = e |v(t) B(t)| = \\frac{e v_0 E_0}{c} |\\sin(\\omega t) \\cos(\\omega t)| = \\frac{e v_0 E_0}{2 c} |\\sin(2\\omega t)|$$\nThe peak magnetic force amplitude is:\n$$F_m = \\frac{1}{2} \\frac{e v_0 E_0}{c}$$\nTherefore, the ratio of force amplitudes is:\n$$\\frac{F_m}{F_e} = \\frac{\\frac{1}{2} e v_0 E_0 / c}{e E_0} = \\frac{1}{2} \\frac{v_0}{c}$$\nEvaluating numerically:\n$$\\frac{F_m}{F_e} = \\frac{1}{2} \\frac{0.0174\\text{ m/s}}{3.0 \\times 10^8\\text{ m/s}} \\approx 2.9 \\times 10^{-11}$$\nBecause this ratio is $\\sim 10^{-11}$, the magnetic force on the electron is completely negligible.",
        "tags": ["free electron", "Lorentz force", "oscillation amplitude", "light wave", "radiation force"]
    },
    {
        "id": "5.201",
        "title": "Permittivity and Phase Velocity of Waves in a Dilute Plasma",
        "difficulty": 2,
        "question": "An electromagnetic wave of frequency $\\omega$ propagates in a dilute plasma with free electron concentration $n_0$. Neglecting ion motion and collisions, find:\n(a) the frequency dependence of the plasma permittivity $\\epsilon(\\omega)$;\n(b) how the phase velocity $v$ of the wave depends on its wavelength $\\lambda$ in the plasma.",
        "hints": [
            "(a) For a free electron driven by $E(t) = E_0 e^{-i\\omega t}$, the displacement is $x = \\frac{e E_0}{m \\omega^2}$. The polarization is $P = -n_0 e x = -\\frac{n_0 e^2}{m \\omega^2} E$, which gives $\\epsilon(\\omega) = 1 + \\frac{P}{\\epsilon_0 E} = 1 - \\frac{n_0 e^2}{\\epsilon_0 m \\omega^2}$.",
            "(b) The dispersion relation is $k^2 = \\frac{\\omega^2}{c^2} \\epsilon(\\omega) = \\frac{\\omega^2 - \\omega_p^2}{c^2}$, where $\\omega_p^2 = \\frac{n_0 e^2}{\\epsilon_0 m}$.",
            "Express the phase velocity $v = \\frac{\\omega}{k}$ in terms of the wavelength in plasma $\\lambda = \\frac{2\\pi}{k}$: $\\omega^2 = c^2 k^2 + \\omega_p^2 = c^2 \\left(\\frac{2\\pi}{\\lambda}\\right)^2 + \\omega_p^2$, giving $v = c \\sqrt{1 + \\frac{n_0 e^2 \\lambda^2}{4\\pi^2 \\epsilon_0 m c^2}}$."
        ],
        "answer": "(a) $\\epsilon = 1 - \\frac{n_0 e^2}{\\epsilon_0 m \\omega^2}$;\n(b) $v = c \\sqrt{1 + \\frac{n_0 e^2 \\lambda^2}{4\\pi^2 \\epsilon_0 m c^2}}$",
        "solution": "**1. Part (a): Permittivity of Dilute Plasma:**\nAn electron in the wave's electric field $E(t) = E_0 e^{-i\\omega t}$ obeys:\n$$m \\ddot{x} = -e E \\implies -m \\omega^2 x = -e E \\implies x = \\frac{e E}{m \\omega^2}$$\nThe macroscopic polarization is:\n$$P = -n_0 e x = -\\frac{n_0 e^2}{m \\omega^2} E$$\nThe electric displacement is $D = \\epsilon_0 E + P = \\epsilon_0 \\epsilon E$, which yields:\n$$\\epsilon(\\omega) = 1 + \\frac{P}{\\epsilon_0 E} = 1 - \\frac{n_0 e^2}{\\epsilon_0 m \\omega^2} = 1 - \\frac{\\omega_p^2}{\\omega^2}$$\nwhere $\\omega_p = \\sqrt{\\frac{n_0 e^2}{\\epsilon_0 m}}$ is the plasma frequency.\n\n**2. Part (b): Phase Velocity vs Wavelength in Plasma:**\nThe wave equation yields the dispersion relation:\n$$k^2 = \\frac{\\omega^2}{c^2} \\epsilon(\\omega) = \\frac{\\omega^2}{c^2} \\left(1 - \\frac{\\omega_p^2}{\\omega^2}\\right) = \\frac{\\omega^2 - \\omega_p^2}{c^2}$$\nRearranging for $\\omega^2$:\n$$\\omega^2 = c^2 k^2 + \\omega_p^2$$\nThe phase velocity is $v = \\frac{\\omega}{k}$:\n$$v^2 = \\frac{\\omega^2}{k^2} = c^2 + \\frac{\\omega_p^2}{k^2}$$\nIn the plasma, the wavelength of the wave is $\\lambda = \\frac{2\\pi}{k}$, so $k = \\frac{2\\pi}{\\lambda}$:\n$$v = \\sqrt{c^2 + \\omega_p^2 \\left(\\frac{\\lambda}{2\\pi}\\right)^2} = c \\sqrt{1 + \\frac{\\omega_p^2 \\lambda^2}{4\\pi^2 c^2}}$$\nSubstituting $\\omega_p^2 = \\frac{n_0 e^2}{\\epsilon_0 m}$:\n$$v = c \\sqrt{1 + \\frac{n_0 e^2 \\lambda^2}{4\\pi^2 \\epsilon_0 m c^2}}$$\nSince the term inside the square root exceeds 1, the phase velocity in a plasma is always greater than $c$.",
        "tags": ["plasma", "permittivity", "phase velocity", "dispersion relation", "plasma frequency"]
    },
    {
        "id": "5.202",
        "title": "Electron Density in the Ionosphere from Radio Refraction",
        "difficulty": 2,
        "question": "Find the free electron concentration $n_0$ in the ionosphere if its refractive index is $n = 0.90$ for radio waves of frequency $\\nu = 100\\text{ MHz}$.",
        "hints": [
            "Use the plasma dispersion relation for the refractive index: $n^2 = 1 - \\frac{n_0 e^2}{\\epsilon_0 m \\omega^2}$, where $\\omega = 2\\pi\\nu$.",
            "Rearrange to solve for the electron concentration: $n_0 = \\frac{4\\pi^2 \\epsilon_0 m \\nu^2 (1 - n^2)}{e^2}$.",
            "Substitute $\\nu = 1.0 \\times 10^8\\text{ Hz}$, $n = 0.90$, and physical constants."
        ],
        "answer": "$n_0 = \\frac{4\\pi^2 \\epsilon_0 m \\nu^2 (1 - n^2)}{e^2} = 2.4 \\times 10^7\\text{ cm}^{-3}$",
        "solution": "**1. Formula for Refractive Index:**\nFor an electromagnetic wave in a collisionless plasma, the refractive index is given by:\n$$n = \\sqrt{1 - \\frac{\\omega_p^2}{\\omega^2}} = \\sqrt{1 - \\frac{n_0 e^2}{4\\pi^2 \\epsilon_0 m \\nu^2}}$$\nSquaring both sides:\n$$n^2 = 1 - \\frac{n_0 e^2}{4\\pi^2 \\epsilon_0 m \\nu^2} \\implies 1 - n^2 = \\frac{n_0 e^2}{4\\pi^2 \\epsilon_0 m \\nu^2}$$\n\n**2. Electron Density Formula:**\n$$n_0 = \\frac{4\\pi^2 \\epsilon_0 m \\nu^2 (1 - n^2)}{e^2}$$\n\n**3. Numerical Evaluation:**\nGiven $\\nu = 100\\text{ MHz} = 1.0 \\times 10^8\\text{ Hz}$ and $n = 0.90$:\n$$1 - n^2 = 1 - (0.90)^2 = 1 - 0.81 = 0.19$$\nUsing $m = 9.109 \\times 10^{-31}\\text{ kg}$, $e = 1.602 \\times 10^{-19}\\text{ C}$, $\\epsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}$:\n$$n_0 = \\frac{4\\pi^2 (8.854 \\times 10^{-12})(9.109 \\times 10^{-31})(1.0 \\times 10^8)^2 (0.19)}{(1.602 \\times 10^{-19})^2}$$\n$$4\\pi^2 \\approx 39.478$$\n$$\\text{Numerator} = 39.478 \\times 8.854 \\times 9.109 \\times 0.19 \\times 10^{-12} \\times 10^{-31} \\times 10^{16} = 604.2 \\times 10^{-27}$$\n$$\\text{Denominator} = (1.602 \\times 10^{-19})^2 \\approx 2.566 \\times 10^{-38}$$\n$$n_0 = \\frac{604.2 \\times 10^{-27}}{2.566 \\times 10^{-38}} \\approx 2.355 \\times 10^{13}\\text{ m}^{-3}$$\nConverting to $\\text{cm}^{-3}$ ($1\\text{ m}^3 = 10^6\\text{ cm}^3$):\n$$n_0 = 2.355 \\times 10^7\\text{ cm}^{-3} \\approx 2.4 \\times 10^7\\text{ cm}^{-3}$$",
        "tags": ["ionosphere", "electron density", "plasma frequency", "radio waves", "refractive index"]
    },
    {
        "id": "5.203",
        "title": "X-Ray Refraction in Graphite (Free-Electron Approximation)",
        "difficulty": 2,
        "question": "Assuming electrons of a substance to behave as free particles when subjected to hard X-rays, determine by what magnitude the refractive index of graphite differs from unity for X-rays whose vacuum wavelength is $\\lambda = 50\\text{ pm}$. The density of graphite is $\\rho = 2.2\\text{ g/cm}^3$.",
        "hints": [
            "For hard X-rays (frequency $\\omega \\gg \\omega_0$), the refractive index of matter is $n = 1 - \\delta$, where $\\delta = \\frac{n_0 e^2 \\lambda^2}{8\\pi^2 \\epsilon_0 m c^2}$.",
            "Calculate the electron concentration $n_0$ in graphite: $n_0 = \\frac{\\rho N_A Z}{M}$, where $Z = 6$ is the atomic number of carbon and $M = 12\\text{ g/mol}$.",
            "Evaluate $n - 1 = -\\delta$ using $\\lambda = 50 \\times 10^{-12}\\text{ m}$."
        ],
        "answer": "$n - 1 = -\\frac{n_0 e^2 \\lambda^2}{8\\pi^2 \\epsilon_0 m c^2} = -5.4 \\times 10^{-7}$",
        "solution": "**1. Free Electron Dispersion for Hard X-Rays:**\nWhen the incident X-ray frequency $\\omega = \\frac{2\\pi c}{\\lambda}$ is much greater than the characteristic atomic binding frequencies, all $Z$ electrons per atom oscillate like free particles:\n$$n = \\sqrt{1 - \\frac{\\omega_p^2}{\\omega^2}} \\approx 1 - \\frac{1}{2} \\frac{\\omega_p^2}{\\omega^2} = 1 - \\frac{n_0 e^2}{2 \\epsilon_0 m \\omega^2}$$\nSubstituting $\\omega = \\frac{2\\pi c}{\\lambda}$:\n$$n - 1 = -\\frac{n_0 e^2 \\lambda^2}{8\\pi^2 \\epsilon_0 m c^2}$$\n\n**2. Electron Concentration in Graphite:**\nFor carbon ($Z = 6$, molar mass $M = 12.01\\text{ g/mol} = 12.01 \\times 10^{-3}\\text{ kg/mol}$):\n$$n_0 = \\frac{\\rho N_A Z}{M}$$\nWith $\\rho = 2.2\\text{ g/cm}^3 = 2.2 \\times 10^6\\text{ g/m}^3$ and $N_A = 6.022 \\times 10^{23}\\text{ mol}^{-1}$:\n$$n_0 = \\frac{(2.2 \\times 10^6\\text{ g/m}^3)(6.022 \\times 10^{23}\\text{ mol}^{-1})(6)}{12\\text{ g/mol}} = 6.624 \\times 10^{29}\\text{ m}^{-3}$$\n\n**3. Numerical Evaluation:**\nFor $\\lambda = 50\\text{ pm} = 5.0 \\times 10^{-11}\\text{ m}$:\n$$n - 1 = -\\frac{(6.624 \\times 10^{29})(1.602 \\times 10^{-19})^2 (5.0 \\times 10^{-11})^2}{8\\pi^2 (8.854 \\times 10^{-12})(9.109 \\times 10^{-31})(3.0 \\times 10^8)^2}$$\n$$\\text{Numerator} = (6.624 \\times 10^{29})(2.566 \\times 10^{-38})(2.5 \\times 10^{-21}) = 4.249 \\times 10^{-29}$$\n$$\\text{Denominator} = 8\\pi^2 (8.854 \\times 10^{-12})(9.109 \\times 10^{-31})(9.0 \\times 10^{16}) = 78.96 \\times 7.243 \\times 10^{-24} \\approx 5.719 \\times 10^{-22}$$\n$$n - 1 = -\\frac{4.249 \\times 10^{-29}}{5.719 \\times 10^{-22}} \\approx -5.4 \\times 10^{-7}$$\n(Notice that $n < 1$, which explains why X-rays undergo total external reflection at grazing angles from matter).",
        "tags": ["X-rays", "graphite", "refractive index", "free electrons", "dispersion"]
    },
    {
        "id": "5.204",
        "title": "Damped Bound Electron Motion and Resonant Absorption of Radiation",
        "difficulty": 3,
        "question": "An electron experiences a quasi-elastic restoring force $-k x$ and a damping friction force $-\\gamma \\dot{x}$ in the field of an electromagnetic wave whose electric field is $E(t) = E_0 \\cos\\omega t$. Neglecting the magnetic force, find:\n(a) the equation of steady-state motion of the electron;\n(b) the mean power $\\langle P \\rangle$ absorbed by the electron, the resonance frequency at which this power is maximized, and the maximum mean power $\\langle P \\rangle_{\\text{max}}$.",
        "hints": [
            "(a) Write the differential equation $\\ddot{x} + 2\\beta \\dot{x} + \\omega_0^2 x = -\\frac{e E_0}{m} \\cos\\omega t$, with $\\beta = \\frac{\\gamma}{2m}$ and $\\omega_0^2 = \\frac{k}{m}$. Solve for the steady-state displacement $x(t) = a \\cos(\\omega t + \\varphi)$.",
            "(b) The instantaneous absorbed power is $P(t) = F(t) \\dot{x}(t) = -e E(t) \\dot{x}(t)$. Take the time average $\\langle P \\rangle = \\frac{1}{2} e E_0 \\omega a \\sin(-\\varphi) = \\gamma \\langle \\dot{x}^2 \\rangle$.",
            "Show that $\\langle P \\rangle = \\frac{e^2 E_0^2 \\beta \\omega^2 / m}{(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2}$, which is maximized at $\\omega = \\omega_0$ with value $\\frac{e^2 E_0^2}{4 m \\beta}$."
        ],
        "answer": "(a) $x(t) = a \\cos(\\omega t + \\varphi)$, with $a = \\frac{e E_0 / m}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2}}$ and $\\tan\\varphi = -\\frac{2\\beta\\omega}{\\omega_0^2 - \\omega^2}$;\n(b) $\\langle P \\rangle = \\frac{(e^2 E_0^2 / m) \\beta \\omega^2}{(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2}$; maximum occurs at $\\omega = \\omega_0$ with $\\langle P \\rangle_{\\text{max}} = \\frac{e^2 E_0^2}{4 m \\beta}$",
        "solution": "**1. Part (a): Equation of Motion and Steady-State Solution:**\nThe equation of motion for the bound electron in the driving field is:\n$$m \\ddot{x} + \\gamma \\dot{x} + k x = -e E_0 \\cos(\\omega t)$$\nDividing by $m$ and setting $2\\beta = \\gamma / m$ and $\\omega_0^2 = k / m$:\n$$\\ddot{x} + 2\\beta \\dot{x} + \\omega_0^2 x = -\\frac{e E_0}{m} \\cos(\\omega t)$$\nIn complex notation, let $E(t) = E_0 e^{-i\\omega t}$ and $x(t) = x_0 e^{-i\\omega t}$:\n$$(-\\omega^2 - 2i\\beta\\omega + \\omega_0^2) x_0 = -\\frac{e E_0}{m}$$\n$$x_0 = \\frac{-e E_0 / m}{\\omega_0^2 - \\omega^2 - 2i\\beta\\omega}$$\nThe real steady-state displacement is:\n$$x(t) = a \\cos(\\omega t + \\varphi)$$\nwhere the amplitude and phase angle are:\n$$a = \\frac{e E_0 / m}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2}}$$\n$$\\tan\\varphi = -\\frac{2\\beta\\omega}{\\omega_0^2 - \\omega^2}$$\n\n**2. Part (b): Mean Absorbed Power:**\nEnergy is absorbed by the electron from the field and dissipated by the friction force.\nThe instantaneous power absorbed from the field is:\n$$P(t) = -e E(t) \\dot{x}(t) = -e E_0 \\cos(\\omega t) [-\\omega a \\sin(\\omega t + \\varphi)] = e E_0 \\omega a \\cos(\\omega t) [\\sin(\\omega t)\\cos\\varphi + \\cos(\\omega t)\\sin\\varphi]$$\nTaking the time average over a cycle ($\\langle \\cos^2\\omega t \\rangle = 1/2$, $\\langle \\cos\\omega t \\sin\\omega t \\rangle = 0$):\n$$\\langle P \\rangle = \\frac{1}{2} e E_0 \\omega a \\sin\\varphi$$\nFrom the complex impedance triangle, $\\sin\\varphi = \\frac{2\\beta\\omega}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2}}$:\n$$\\langle P \\rangle = \\frac{1}{2} e E_0 \\omega \\left[ \\frac{e E_0 / m}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2}} \\right] \\left[ \\frac{2\\beta\\omega}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2}} \\right]$$\n$$\\langle P \\rangle = \\frac{e^2 E_0^2}{m} \\frac{\\beta \\omega^2}{(\\omega_0^2 - \\omega^2)^2 + 4\\beta^2 \\omega^2}$$\n\n**3. Maximum Power at Resonance:**\nThe power is maximized when the denominator term $(\\omega_0^2 - \\omega^2)^2 / \\omega^2$ is minimized, which occurs exactly at:\n$$\\omega = \\omega_0$$\nAt this resonant frequency:\n$$\\langle P \\rangle_{\\text{max}} = \\frac{e^2 E_0^2}{m} \\frac{\\beta \\omega_0^2}{4\\beta^2 \\omega_0^2} = \\frac{e^2 E_0^2}{4 m \\beta}$$",
        "tags": ["Lorentz oscillator", "dispersion", "resonance", "absorbed power", "damping"]
    },
    {
        "id": "5.205",
        "title": "Wave Propagation for Complex and Imaginary Refractive Indices",
        "difficulty": 2,
        "question": "In some media, the permittivity is a complex or negative quantity, so the refractive index is complex ($n = n' + i n''$) or purely imaginary ($n = i n''$). Write the plane-wave equations for both cases and explain their physical meaning.",
        "hints": [
            "Write the complex plane wave as $E(x, t) = E_0 e^{-i(\\omega t - k x)}$ where the wave number in the medium is $k = \\frac{\\omega}{c} n = \\frac{2\\pi}{\\lambda_0} n$.",
            "For $n = n' + i n''$, substitute $k = \\frac{2\\pi}{\\lambda_0} n' + i \\frac{2\\pi}{\\lambda_0} n''$ and separate the real exponential decay factor and the oscillatory factor.",
            "For $n = i n''$, the real oscillatory wave vector vanishes ($k$ is purely imaginary), yielding an evanescent, non-propagating wave corresponding to total reflection without absorption."
        ],
        "answer": "Complex $n = n' + i n''$: propagating wave with exponential attenuation (absorption), $E(x, t) = E_0 e^{-\\frac{2\\pi n''}{\\lambda_0} x} \\cos(\\omega t - \\frac{2\\pi n'}{\\lambda_0} x)$; Imaginary $n = i n''$: evanescent standing wave $E(x, t) = E_0 e^{-\\frac{2\\pi n''}{\\lambda_0} x} \\cos(\\omega t)$, representing total reflection without dissipation.",
        "solution": "**1. General Plane Wave Expression:**\nA plane electromagnetic wave traveling in the $+x$ direction is represented in complex form as:\n$$E(x, t) = E_0 e^{-i(\\omega t - k x)}$$\nwhere the complex wavenumber is related to the vacuum wavelength $\\lambda_0$ and the complex refractive index $n$ by:\n$$k = \\frac{\\omega}{c} n = \\frac{2\\pi}{\\lambda_0} n$$\n\n**2. Case 1: Complex Refractive Index ($n = n' + i n''$):**\nSubstituting $n = n' + i n''$:\n$$k = \\frac{2\\pi}{\\lambda_0} n' + i \\frac{2\\pi}{\\lambda_0} n''$$\n$$E(x, t) = E_0 e^{-i \\left[\\omega t - \\frac{2\\pi n'}{\\lambda_0} x - i \\frac{2\\pi n''}{\\lambda_0} x\\right]} = E_0 e^{-\\frac{2\\pi n''}{\\lambda_0} x} e^{-i \\left(\\omega t - \\frac{2\\pi n'}{\\lambda_0} x\\right)}$$\nTaking the real part:\n$$E(x, t) = E_0 e^{-\\frac{2\\pi n''}{\\lambda_0} x} \\cos\\left(\\omega t - \\frac{2\\pi n'}{\\lambda_0} x\\right)$$\n**Physical Meaning:**\nThis describes a propagating wave with phase velocity $v = c / n'$ whose amplitude decays exponentially along the direction of propagation with absorption coefficient $\\kappa = \\frac{4\\pi n''}{\\lambda_0}$. The loss of wave amplitude represents true dissipation of electromagnetic energy into the medium (Beer-Lambert absorption).\n\n**3. Case 2: Purely Imaginary Refractive Index ($n = i n''$):**\nHere the real refractive index $n' = 0$ (e.g. in a plasma below the plasma frequency $\\omega < \\omega_p$, or in a metal below cutoff):\n$$k = i \\frac{2\\pi n''}{\\lambda_0}$$\n$$E(x, t) = E_0 e^{-\\frac{2\\pi n''}{\\lambda_0} x} e^{-i\\omega t}$$\nTaking the real part:\n$$E(x, t) = E_0 e^{-\\frac{2\\pi n''}{\\lambda_0} x} \\cos(\\omega t)$$\n**Physical Meaning:**\nIn this case, there is no spatial phase propagation ($k_{\\text{real}} = 0$). All points in space oscillate in phase. This represents an **evanescent wave** (or non-propagating skin field). The Poynting vector averaged over a cycle is zero ($\\langle S \\rangle = 0$), meaning no net energy is absorbed or transported into the medium; the incident radiation experiences **total reflection** at the interface.",
        "tags": ["complex refractive index", "absorption", "evanescent wave", "total reflection", "extinction coefficient"]
    },
    {
        "id": "5.206",
        "title": "Plasma Electron Concentration from Total Internal Reflection of Radiowaves",
        "difficulty": 2,
        "question": "A sounding of dilute plasma by radiowaves of various frequencies reveals that radiowaves with wavelengths exceeding $\\lambda_0 = 0.75\\text{ m}$ experience total reflection. Find the free electron concentration $n_0$ in that plasma.",
        "hints": [
            "Total reflection occurs when the plasma permittivity becomes zero or negative: $\\epsilon(\\omega) \\le 0$, which corresponds to frequencies below the plasma frequency: $\\omega \\le \\omega_p$.",
            "The threshold wavelength $\\lambda_0$ corresponds to $\\omega = \\omega_p = \\frac{2\\pi c}{\\lambda_0}$.",
            "Equating $\\omega_p^2 = \\frac{n_0 e^2}{\\epsilon_0 m} = \\left(\\frac{2\\pi c}{\\lambda_0}\\right)^2$, solve for $n_0 = \\frac{4\\pi^2 \\epsilon_0 m c^2}{e^2 \\lambda_0^2}$."
        ],
        "answer": "$n_0 = \\frac{4\\pi^2 \\epsilon_0 m c^2}{e^2 \\lambda_0^2} = 2.0 \\times 10^9\\text{ cm}^{-3}$",
        "solution": "**1. Cutoff Condition for Plasma Reflection:**\nThe refractive index of a collisionless plasma is:\n$$n^2 = \\epsilon(\\omega) = 1 - \\frac{\\omega_p^2}{\\omega^2}$$\nWaves can propagate only when $\\omega > \\omega_p$ (so that $n$ is real).\nWhen $\\omega \\le \\omega_p$, $n$ becomes purely imaginary, and the wave is totally reflected by the plasma layer.\nIn terms of vacuum wavelength $\\lambda = \\frac{2\\pi c}{\\omega}$, reflection occurs for all wavelengths longer than the critical wavelength $\\lambda_0$:\n$$\\lambda \\ge \\lambda_0 \\implies \\omega \\le \\omega_p = \\frac{2\\pi c}{\\lambda_0}$$\n\n**2. Electron Density Formula:**\nThe plasma frequency is:\n$$\\omega_p^2 = \\frac{n_0 e^2}{\\epsilon_0 m} = \\frac{4\\pi^2 c^2}{\\lambda_0^2}$$\nSolving for the electron concentration $n_0$:\n$$n_0 = \\frac{4\\pi^2 \\epsilon_0 m c^2}{e^2 \\lambda_0^2}$$\n\n**3. Numerical Evaluation:**\nFor $\\lambda_0 = 0.75\\text{ m}$:\n$$n_0 = \\frac{4\\pi^2 (8.854 \\times 10^{-12}\\text{ F/m})(9.109 \\times 10^{-31}\\text{ kg})(3.0 \\times 10^8\\text{ m/s})^2}{(1.602 \\times 10^{-19}\\text{ C})^2 (0.75\\text{ m})^2}$$\n$$\\text{Numerator} = 39.478 \\times 8.854 \\times 9.109 \\times 9.0 \\times 10^{-14} = 2.863 \\times 10^{-11}$$\n$$\\text{Denominator} = (2.566 \\times 10^{-38})(0.5625) = 1.443 \\times 10^{-38}$$\n$$n_0 = \\frac{2.863 \\times 10^{-11}}{1.443 \\times 10^{-38}} \\approx 1.984 \\times 10^{15}\\text{ m}^{-3} \\approx 2.0 \\times 10^{15}\\text{ m}^{-3}$$\nConverting to $\\text{cm}^{-3}$ ($1\\text{ m}^{-3} = 10^{-6}\\text{ cm}^{-3}$):\n$$n_0 = 1.984 \\times 10^9\\text{ cm}^{-3} \\approx 2.0 \\times 10^9\\text{ cm}^{-3}$$",
        "tags": ["plasma sounding", "cutoff wavelength", "plasma frequency", "electron concentration"]
    },
    {
        "id": "5.207",
        "title": "Derivation and Geometric Interpretation of Rayleigh's Group Velocity Formula",
        "difficulty": 2,
        "question": "Using the definition of group velocity $u = \\frac{d\\omega}{dk}$, derive Rayleigh's formula:\n$$u = v - \\lambda \\frac{dv}{d\\lambda}$$\nwhere $v$ is the phase velocity and $\\lambda$ is the wavelength. Demonstrate that on a graph of $v(\\lambda)$, the group velocity $u$ at wavelength $\\lambda'$ is equal to the intercept cut by the tangent to the curve at $\\lambda'$ on the vertical axis ($\\lambda = 0$).",
        "hints": [
            "Use $\\omega = v k$ and $k = \\frac{2\\pi}{\\lambda}$. Differentiate $k$ with respect to $\\lambda$ to find $dk = -\\frac{2\\pi}{\\lambda^2} d\\lambda$.",
            "Differentiate $\\omega = v(k) k$ to obtain $d\\omega = v dk + k dv$, and divide by $dk$.",
            "Write the equation of the tangent line to the curve $v(\\lambda)$ at point $(\\lambda', v')$: $y - v' = \\left.\\frac{dv}{d\\lambda}\\right|_{\\lambda'} (x - \\lambda')$, and find the $y$-intercept at $x = 0$."
        ],
        "answer": "Derivation: $u = \\frac{d(vk)}{dk} = v + k \\frac{dv}{dk} = v - \\lambda \\frac{dv}{d\\lambda}$; the tangent intercept at $\\lambda = 0$ is $v' - \\lambda' \\left.\\frac{dv}{d\\lambda}\\right|_{\\lambda'} = u$",
        "solution": "**1. Analytic Derivation of Rayleigh's Formula:**\nBy definition, the group velocity is:\n$$u = \\frac{d\\omega}{dk}$$\nThe phase velocity is $v = \\frac{\\omega}{k}$, so $\\omega = v k$.\nDifferentiating the product:\n$$u = \\frac{d(v k)}{dk} = v + k \\frac{dv}{dk}$$\nThe wavenumber is related to the wavelength by $k = \\frac{2\\pi}{\\lambda}$. Differentiating:\n$$dk = -\\frac{2\\pi}{\\lambda^2} d\\lambda \\implies \\frac{dk}{d\\lambda} = -\\frac{k}{\\lambda} \\implies \\frac{dv}{dk} = \\frac{dv / d\\lambda}{dk / d\\lambda} = -\\frac{\\lambda}{k} \\frac{dv}{d\\lambda}$$\nSubstituting this back into the expression for $u$:\n$$u = v + k \\left(-\\frac{\\lambda}{k} \\frac{dv}{d\\lambda}\\right) = v - \\lambda \\frac{dv}{d\\lambda}$$\nThis is **Rayleigh's formula**.\n\n**2. Geometric Interpretation:**\nConsider the curve of phase velocity versus wavelength, $v = v(\\lambda)$, plotted with $\\lambda$ on the horizontal axis and $v$ on the vertical axis.\nAt a specific wavelength $\\lambda'$, the slope of the curve is $\\left.\\frac{dv}{d\\lambda}\\right|_{\\lambda'}$.\nThe equation of the tangent line to the curve at the point $(\\lambda', v(\\lambda'))$ is:\n$$V(\\lambda) - v(\\lambda') = \\left.\\frac{dv}{d\\lambda}\\right|_{\\lambda'} (\\lambda - \\lambda')$$\nSetting $\\lambda = 0$ to find the vertical intercept $V(0)$:\n$$V(0) = v(\\lambda') - \\lambda' \\left.\\frac{dv}{d\\lambda}\\right|_{\\lambda'}$$\nComparing this with Rayleigh's formula evaluated at $\\lambda'$:\n$$V(0) = u(\\lambda')$$\nThus, the group velocity $u$ at any wavelength $\\lambda'$ is geometrically represented by the vertical intercept of the tangent line to the dispersion curve at that point.",
        "tags": ["Rayleigh's formula", "group velocity", "phase velocity", "dispersion", "geometric proof"]
    },
    {
        "id": "5.208",
        "title": "Group Velocity for Power-Law Dispersion Relations",
        "difficulty": 2,
        "question": "Find the relation between the group velocity $u$ and the phase velocity $v$ for media with the following dispersion laws:\n(a) $v \\propto 1/\\sqrt{\\lambda}$;\n(b) $v \\propto k$;\n(c) $v \\propto 1/\\omega^2$.\nHere $\\lambda$, $k$, and $\\omega$ are the wavelength, wavenumber, and angular frequency.",
        "hints": [
            "(a) Use Rayleigh's formula $u = v - \\lambda \\frac{dv}{d\\lambda}$. If $v = C \\lambda^{-1/2}$, then $\\frac{dv}{d\\lambda} = -\\frac{1}{2} C \\lambda^{-3/2} = -\\frac{v}{2\\lambda}$.",
            "(b) Express $v = C k$. Since $k = 2\\pi / \\lambda$, $v \\propto 1/\\lambda$, so $\\frac{dv}{d\\lambda} = -\\frac{v}{\\lambda}$. Then $u = v - \\lambda(-v/\\lambda) = 2v$.",
            "(c) If $v = C / \\omega^2$, write $\\omega = v k = C k / \\omega^2 \\implies \\omega^3 = C k$. Differentiate to find $u = \\frac{d\\omega}{dk} = \\frac{1}{3} \\frac{\\omega}{k} = \\frac{v}{3}$."
        ],
        "answer": "(a) $u = \\frac{3}{2} v$;\n(b) $u = 2v$;\n(c) $u = \\frac{1}{3} v$",
        "solution": "**1. Part (a): Dispersion Law $v \\propto 1/\\sqrt{\\lambda}$:**\nLet $v = C \\lambda^{-1/2}$ (such as gravity waves on deep water).\nDifferentiating with respect to $\\lambda$:\n$$\\frac{dv}{d\\lambda} = -\\frac{1}{2} C \\lambda^{-3/2} = -\\frac{1}{2} \\frac{v}{\\lambda}$$\nUsing Rayleigh's formula:\n$$u = v - \\lambda \\frac{dv}{d\\lambda} = v - \\lambda \\left(-\\frac{v}{2\\lambda}\\right) = v + \\frac{1}{2} v = \\frac{3}{2} v$$\n\n**2. Part (b): Dispersion Law $v \\propto k$:**\nSince $k = \\frac{2\\pi}{\\lambda}$, this implies $v = \\frac{C'}{\\lambda}$ (such as capillary waves on a liquid surface).\nDifferentiating:\n$$\\frac{dv}{d\\lambda} = -\\frac{C'}{\\lambda^2} = -\\frac{v}{\\lambda}$$\nApplying Rayleigh's formula:\n$$u = v - \\lambda \\left(-\\frac{v}{\\lambda}\\right) = v + v = 2v$$\n\n**3. Part (c): Dispersion Law $v \\propto 1/\\omega^2$:**\nFrom the definition of phase velocity, $v = \\frac{\\omega}{k}$, so:\n$$\\frac{\\omega}{k} = \\frac{C}{\\omega^2} \\implies \\omega^3 = C k$$\nTaking the logarithm and differentiating with respect to $k$:\n$$3 \\ln\\omega = \\ln C + \\ln k \\implies \\frac{3}{\\omega} \\frac{d\\omega}{dk} = \\frac{1}{k}$$\n$$u = \\frac{d\\omega}{dk} = \\frac{1}{3} \\frac{\\omega}{k} = \\frac{1}{3} v$$",
        "tags": ["group velocity", "phase velocity", "dispersion laws", "Rayleigh formula"]
    },
    {
        "id": "5.209",
        "title": "Permittivity Frequency Dependence for a Medium with Constant uv Product",
        "difficulty": 2,
        "question": "In a certain medium, the relationship between the group velocity $u$ and phase velocity $v$ of an electromagnetic wave has the form $u v = c^2$, where $c$ is the speed of light in vacuum. Find the dependence of the permittivity of that medium on wave frequency, $\\epsilon(\\omega)$.",
        "hints": [
            "Use the definitions $u = \\frac{d\\omega}{dk}$ and $v = \\frac{\\omega}{k}$.",
            "The given relation becomes $\\frac{\\omega}{k} \\frac{d\\omega}{dk} = c^2 \\implies \\omega \\, d\\omega = c^2 k \\, dk$.",
            "Integrate to find $\\omega^2 = c^2 k^2 + A$, then substitute into $\\epsilon(\\omega) = \\frac{c^2}{v^2} = \\frac{c^2 k^2}{\\omega^2}$."
        ],
        "answer": "$\\epsilon(\\omega) = 1 + \\frac{A}{\\omega^2}$, where $A$ is an integration constant",
        "solution": "**1. Differential Equation for Dispersion:**\nUsing the definitions of group velocity $u = \\frac{d\\omega}{dk}$ and phase velocity $v = \\frac{\\omega}{k}$:\n$$u v = \\left(\\frac{d\\omega}{dk}\\right) \\left(\\frac{\\omega}{k}\\right) = c^2$$\nMultiplying both sides by $k \\, dk$:\n$$\\omega \\, d\\omega = c^2 k \\, dk$$\n\n**2. Integration:**\nIntegrating both sides:\n$$\\int \\omega \\, d\\omega = c^2 \\int k \\, dk$$\n$$\\frac{1}{2} \\omega^2 = \\frac{1}{2} c^2 k^2 - \\frac{1}{2} A$$\n$$\\omega^2 = c^2 k^2 - A \\implies c^2 k^2 = \\omega^2 + A$$\nwhere $A$ is an arbitrary constant of integration.\n\n**3. Determining Permittivity $\\epsilon(\\omega)$:**\nThe refractive index is $n = \\frac{c}{v} = \\frac{c k}{\\omega}$, and the permittivity of a non-magnetic medium is $\\epsilon = n^2$:\n$$\\epsilon(\\omega) = \\left(\\frac{c k}{\\omega}\\right)^2 = \\frac{c^2 k^2}{\\omega^2}$$\nSubstituting $c^2 k^2 = \\omega^2 + A$:\n$$\\epsilon(\\omega) = \\frac{\\omega^2 + A}{\\omega^2} = 1 + \\frac{A}{\\omega^2}$$\n(For a dilute plasma, $A = -\\omega_p^2$, in which case $u v = c^2$ holds identically!).",
        "tags": ["dispersion", "group velocity", "permittivity", "phase velocity", "plasma"]
    },
    {
        "id": "5.210",
        "title": "Phase and Group Velocities of Light in Carbon Dioxide",
        "difficulty": 2,
        "question": "The refractive index of carbon dioxide gas at wavelengths $509\\text{ nm}$, $534\\text{ nm}$, and $589\\text{ nm}$ is $1.647$, $1.640$, and $1.630$ respectively. Calculate the phase velocity $v$ and group velocity $u$ of light in the vicinity of $\\lambda = 534\\text{ nm}$.",
        "hints": [
            "Calculate phase velocity directly from $v = c / n$ at $\\lambda = 534\\text{ nm}$ ($n = 1.640$).",
            "Estimate the dispersion derivative $\\frac{dn}{d\\lambda}$ using finite differences: $\\frac{dn}{d\\lambda} \\approx \\frac{n(589) - n(509)}{589 - 509}$.",
            "Use the group velocity formula in terms of refractive index: $u = \\frac{c}{n - \\lambda \\frac{dn}{d\\lambda}}$."
        ],
        "answer": "$v = 1.83 \\times 10^8\\text{ m/s}$, $u = 1.70 \\times 10^8\\text{ m/s}$",
        "solution": "**1. Phase Velocity at $\\lambda = 534\\text{ nm}$:**\nAt $\\lambda = 534\\text{ nm}$, the refractive index is $n = 1.640$:\n$$v = \\frac{c}{n} = \\frac{3.00 \\times 10^8\\text{ m/s}}{1.640} \\approx 1.829 \\times 10^8\\text{ m/s} \\approx 1.83 \\times 10^8\\text{ m/s}$$\n\n**2. Derivative $\\frac{dn}{d\\lambda}$:**\nUsing the symmetric interval between $509\\text{ nm}$ and $589\\text{ nm}$ (width $\\Delta\\lambda = 80\\text{ nm}$):\n$$\\frac{dn}{d\\lambda} \\approx \\frac{1.630 - 1.647}{589 - 509} = \\frac{-0.017}{80\\text{ nm}} = -2.125 \\times 10^{-4}\\text{ nm}^{-1}$$\n\n**3. Group Velocity Formula:**\nFrom $v = c / n$ and $u = v - \\lambda \\frac{dv}{d\\lambda}$:\n$$\\frac{dv}{d\\lambda} = -\\frac{c}{n^2} \\frac{dn}{d\\lambda}$$\n$$u = \\frac{c}{n} - \\lambda \\left(-\\frac{c}{n^2} \\frac{dn}{d\\lambda}\\right) = \\frac{c}{n} \\left(1 + \\frac{\\lambda}{n} \\frac{dn}{d\\lambda}\\right) \\approx \\frac{c}{n - \\lambda \\frac{dn}{d\\lambda}}$$\nComputing the denominator:\n$$n - \\lambda \\frac{dn}{d\\lambda} = 1.640 - (534\\text{ nm})(-2.125 \\times 10^{-4}\\text{ nm}^{-1}) = 1.640 + 0.1135 = 1.7535$$\nTherefore:\n$$u = \\frac{3.00 \\times 10^8\\text{ m/s}}{1.7535} \\approx 1.711 \\times 10^8\\text{ m/s} \\approx 1.70 \\times 10^8\\text{ m/s}$$",
        "tags": ["phase velocity", "group velocity", "carbon dioxide", "dispersion", "refractive index"]
    },
    {
        "id": "5.211",
        "title": "Shape Restoration of a Light Wave Train in a Linear Dispersion Medium",
        "difficulty": 2,
        "question": "A train of plane light waves propagates in a medium where the phase velocity depends linearly on wavelength: $v(\\lambda) = a + b \\lambda$, where $a$ and $b$ are positive constants. Demonstrate that the shape of an arbitrary wave packet is restored after a time interval $\\tau = 1/b$.",
        "hints": [
            "Write the phase of an arbitrary spectral component of wavelength $\\lambda$ at position $x$ and time $t$: $\\Phi(x, t) = \\frac{2\\pi}{\\lambda}(x - v t)$.",
            "Substitute $v = a + b\\lambda$ into the phase: $\\Phi(x, t) = \\frac{2\\pi}{\\lambda}(x - a t) - 2\\pi b t$.",
            "At time $t + \\tau$ with $\\tau = 1/b$, observe that the extra phase accumulated by all components is $2\\pi b \\tau = 2\\pi$, which leaves their relative phases invariant."
        ],
        "answer": "The relative phases of all spectral components are invariant modulo $2\\pi$ after $\\tau = 1/b$ in the frame moving at velocity $a$",
        "solution": "**1. Phase of an Arbitrary Spectral Component:**\nAn arbitrary wave train can be expressed as a Fourier superposition of harmonic plane waves:\n$$E(x, t) = \\int A(\\lambda) \\cos[\\Phi_\\lambda(x, t)] \\, d\\lambda$$\nwhere the phase of the component with wavelength $\\lambda$ is:\n$$\\Phi_\\lambda(x, t) = k(x - v t) = \\frac{2\\pi}{\\lambda}[x - v(\\lambda) t]$$\n\n**2. Substituting the Linear Dispersion Law:**\nGiven $v(\\lambda) = a + b \\lambda$:\n$$\\Phi_\\lambda(x, t) = \\frac{2\\pi}{\\lambda}[x - (a + b\\lambda) t] = \\frac{2\\pi}{\\lambda}(x - a t) - 2\\pi b t$$\n\n**3. Evaluation at Time $t + \\tau$:**\nConsider the wave at time $t + \\tau$ at the shifted position $x + a \\tau$ (in a coordinate frame moving with speed $a$):\n$$\\Phi_\\lambda(x + a \\tau, t + \\tau) = \\frac{2\\pi}{\\lambda}[(x + a \\tau) - a(t + \\tau)] - 2\\pi b (t + \\tau)$$\n$$\\Phi_\\lambda(x + a \\tau, t + \\tau) = \\frac{2\\pi}{\\lambda}(x - a t) - 2\\pi b t - 2\\pi b \\tau = \\Phi_\\lambda(x, t) - 2\\pi b \\tau$$\n\n**4. Condition for Waveform Restoration:**\nIf we choose $\\tau$ such that:\n$$2\\pi b \\tau = 2\\pi \\implies \\tau = \\frac{1}{b}$$\nthen for every spectral component $\\lambda$, the phase changes by exactly an integer multiple of $2\\pi$:\n$$\\cos[\\Phi_\\lambda(x + a\\tau, t + \\tau)] = \\cos[\\Phi_\\lambda(x, t) - 2\\pi] = \\cos[\\Phi_\\lambda(x, t)]$$\nSince every Fourier component maintains its exact amplitude and relative phase, the complete waveform is perfectly restored after time interval $\\tau = 1/b$.",
        "tags": ["wave packet", "dispersion", "linear dispersion", "waveform restoration", "Fourier superposition"]
    },
    {
        "id": "5.212",
        "title": "Light Transmission Through an Absorbing Faraday Solution Between Crossed Nicols",
        "difficulty": 2,
        "question": "A beam of natural light of intensity $I_0$ falls on a system of two crossed Nicol prisms containing a tube of length $l$ filled with a solution in a longitudinal magnetic field $H$. The linear absorption coefficient of the solution is $\\kappa$, and its Verdet constant is $V$. Find the intensity $I$ of light transmitted through the system.",
        "hints": [
            "Natural light passing through the first Nicol becomes linearly polarized with intensity $I_1 = \\frac{1}{2} I_0$.",
            "Traversing the absorbing solution of length $l$ attenuates the light by the Beer-Lambert factor $e^{-\\kappa l}$.",
            "The Faraday effect rotates the polarization plane by $\\varphi = V H l$. For crossed Nicols, the transmission factor is $\\sin^2\\varphi$. Multiply all factors together."
        ],
        "answer": "$I = \\frac{1}{2} I_0 e^{-\\kappa l} \\sin^2(V H l)$",
        "solution": "**1. Polarization by the First Nicol:**\nNatural light of intensity $I_0$ entering the first Nicol prism is converted into linearly polarized light with transmitted intensity:\n$$I_1 = \\frac{1}{2} I_0$$\n\n**2. Absorption in the Solution:**\nAs the light propagates through the solution of length $l$ with linear absorption coefficient $\\kappa$, its intensity is attenuated according to the Beer-Lambert law:\n$$I_2 = I_1 e^{-\\kappa l} = \\frac{1}{2} I_0 e^{-\\kappa l}$$\n\n**3. Faraday Rotation and Analyzer Transmission:**\nIn the presence of the longitudinal magnetic field $H$, the plane of polarization rotates by angle:\n$$\\varphi = V H l$$\nBecause the second Nicol prism is crossed at $90^\\circ$ relative to the first, the angle between the rotated polarization plane and the analyzer axis is $90^\\circ - \\varphi$.\nBy Malus's law, the transmitted intensity is:\n$$I = I_2 \\cos^2(90^\\circ - \\varphi) = I_2 \\sin^2\\varphi$$\n\n**4. Final Expression:**\n$$I = \\frac{1}{2} I_0 e^{-\\kappa l} \\sin^2(V H l)$$",
        "tags": ["Faraday effect", "Beer-Lambert law", "crossed Nicols", "absorption", "Verdet constant"]
    },
    {
        "id": "5.213",
        "title": "Transmission of Light Through a Plate with Multiple Internal Reflections",
        "difficulty": 2,
        "question": "A plane monochromatic light wave of intensity $I_0$ falls normally on a plane-parallel plate whose surfaces each have reflection coefficient $\\rho$. Taking into account multiple internal reflections, find the transmitted intensity $I$ if:\n(a) the plate is perfectly transparent (no absorption);\n(b) the plate has thickness $d$ and linear absorption coefficient $\\kappa$.",
        "hints": [
            "(a) At each surface, the transmission is $1 - \\rho$. Sum the geometric series of successive transmitted rays: $I = I_0 (1 - \\rho)^2 [1 + \\rho^2 + \\rho^4 + \\dots]$.",
            "(b) With absorption, each pass across the plate multiplies the intensity by $\\sigma = e^{-\\kappa d}$. The successive transmitted intensities are $I_0 (1 - \\rho)^2 \\sigma [1 + \\rho^2 \\sigma^2 + \\rho^4 \\sigma^4 + \\dots]$.",
            "Sum the geometric series $1 + x + x^2 + \\dots = \\frac{1}{1 - x}$ with $x = \\rho^2$ for (a) and $x = \\rho^2 \\sigma^2$ for (b)."
        ],
        "answer": "(a) $I = I_0 \\frac{1 - \\rho}{1 + \\rho}$;\n(b) $I = I_0 \\frac{(1 - \\rho)^2 \\sigma}{1 - \\rho^2 \\sigma^2}$, where $\\sigma = e^{-\\kappa d}$",
        "solution": "**1. Part (a): Perfectly Transparent Plate:**\nThe beam strikes the first surface: fraction $(1 - \\rho)$ enters the plate.\nAt the second surface, fraction $(1 - \\rho)$ emerges directly: $I_1 = I_0 (1 - \\rho)^2$.\nThe remaining fraction $\\rho$ reflects back, reflects again at the first surface (fraction $\\rho$), and reaches the second surface with amplitude squared factor $\\rho^2$.\nEach round-trip inside the plate introduces a factor of $\\rho^2$ in intensity.\nSumming all incoherent transmitted beams:\n$$I = I_0 (1 - \\rho)^2 (1 + \\rho^2 + \\rho^4 + \\dots) = I_0 (1 - \\rho)^2 \\sum_{n=0}^\\infty (\\rho^2)^n$$\n$$I = I_0 \\frac{(1 - \\rho)^2}{1 - \\rho^2} = I_0 \\frac{(1 - \\rho)^2}{(1 - \\rho)(1 + \\rho)} = I_0 \\frac{1 - \\rho}{1 + \\rho}$$\n\n**2. Part (b): Plate with Absorption:**\nLet $\\sigma = e^{-\\kappa d}$ be the transmission factor for a single pass through the plate.\n- First transmitted beam: undergoes transmission at surface 1, traversal across $d$, transmission at surface 2:\n  $$I_1 = I_0 (1 - \\rho)^2 \\sigma$$\n- Second transmitted beam: undergoes two internal reflections and two additional traversals (round trip $\\sigma^2 \\rho^2$):\n  $$I_2 = I_1 (\\rho \\sigma)^2 = I_0 (1 - \\rho)^2 \\sigma (\\rho^2 \\sigma^2)$$\nSumming all terms:\n$$I = I_0 (1 - \\rho)^2 \\sigma [1 + \\rho^2 \\sigma^2 + (\\rho^2 \\sigma^2)^2 + \\dots]$$\n$$I = I_0 \\frac{(1 - \\rho)^2 \\sigma}{1 - \\rho^2 \\sigma^2}$$\nwhere $\\sigma = e^{-\\kappa d}$.",
        "tags": ["multiple reflections", "Airy formula", "absorption", "transmittance", "geometric series"]
    },
    {
        "id": "5.214",
        "title": "Linear Absorption Coefficient from Plates of Different Thicknesses",
        "difficulty": 1,
        "question": "Two plates made of the same substance have thicknesses $d_1 = 3.8\\text{ mm}$ and $d_2 = 9.0\\text{ mm}$. When placed normally in the path of monochromatic light, the first plate transmits a fraction $\\tau_1 = 0.84$ of the luminous flux, and the second transmits $\\tau_2 = 0.70$. Neglecting secondary reflections, find the linear absorption coefficient $\\kappa$ of the substance.",
        "hints": [
            "Neglecting secondary reflections, the transmission of a plate of thickness $d$ is $\\tau = (1 - \\rho)^2 e^{-\\kappa d}$, where $\\rho$ is the surface reflectance.",
            "Take the ratio of transmittances for the two plates: $\\frac{\\tau_1}{\\tau_2} = \\frac{(1 - \\rho)^2 e^{-\\kappa d_1}}{(1 - \\rho)^2 e^{-\\kappa d_2}} = e^{\\kappa (d_2 - d_1)}$.",
            "Solve for $\\kappa = \\frac{\\ln(\\tau_1 / \\tau_2)}{d_2 - d_1}$."
        ],
        "answer": "$\\kappa = \\frac{\\ln(\\tau_1 / \\tau_2)}{d_2 - d_1} = 0.35\\text{ cm}^{-1}$",
        "solution": "**1. Transmission Formula:**\nFor normal incidence on a plate of thickness $d$, neglecting secondary reflections, light suffers reflection losses at the two surfaces and exponential absorption within the bulk:\n$$\\tau = (1 - \\rho)^2 e^{-\\kappa d}$$\nFor the two plates:\n$$\\tau_1 = (1 - \\rho)^2 e^{-\\kappa d_1}$$\n$$\\tau_2 = (1 - \\rho)^2 e^{-\\kappa d_2}$$\n\n**2. Eliminating Reflection Losses:**\nDividing $\\tau_1$ by $\\tau_2$ eliminates the unknown reflection coefficient $\\rho$:\n$$\\frac{\\tau_1}{\\tau_2} = \\frac{e^{-\\kappa d_1}}{e^{-\\kappa d_2}} = e^{\\kappa (d_2 - d_1)}$$\nTaking the natural logarithm:\n$$\\ln\\left(\\frac{\\tau_1}{\\tau_2}\\right) = \\kappa (d_2 - d_1) \\implies \\kappa = \\frac{\\ln(\\tau_1 / \\tau_2)}{d_2 - d_1}$$\n\n**3. Numerical Evaluation:**\nGiven $d_1 = 3.8\\text{ mm} = 0.38\\text{ cm}$, $d_2 = 9.0\\text{ mm} = 0.90\\text{ cm}$, $\\tau_1 = 0.84$, and $\\tau_2 = 0.70$:\n$$d_2 - d_1 = 0.90 - 0.38 = 0.52\\text{ cm}$$\n$$\\frac{\\tau_1}{\\tau_2} = \\frac{0.84}{0.70} = 1.20$$\n$$\\ln(1.20) \\approx 0.18232$$\n$$\\kappa = \\frac{0.18232}{0.52\\text{ cm}} \\approx 0.3506\\text{ cm}^{-1} \\approx 0.35\\text{ cm}^{-1}$$",
        "tags": ["absorption coefficient", "Beer-Lambert law", "thickness variation", "photometry"]
    },
    {
        "id": "5.215",
        "title": "Absorption Coefficient of Glass from Transmission Through a Pile of Plates",
        "difficulty": 2,
        "question": "A beam of monochromatic light passes through a stack of $N = 5$ identical plane-parallel glass plates, each of thickness $l = 0.50\\text{ cm}$. The reflection coefficient at each surface is $\\rho = 0.050$. The ratio of transmitted to incident light intensity is $\\tau = 0.55$. Neglecting secondary reflections, find the linear absorption coefficient $\\kappa$ of the glass.",
        "hints": [
            "The stack consists of $N$ plates, meaning light traverses a total thickness $L = N l$ and passes through $2N$ glass-air interfaces.",
            "Neglecting secondary reflections, the overall transmission is $\\tau = (1 - \\rho)^{2N} e^{-\\kappa N l}$.",
            "Solve for $\\kappa = \\frac{1}{N l} \\ln\\left[\\frac{(1 - \\rho)^{2N}}{\\tau}\\right]$."
        ],
        "answer": "$\\kappa = \\frac{1}{N l} \\ln\\left[\\frac{(1 - \\rho)^{2N}}{\\tau}\\right] = 0.034\\text{ cm}^{-1}$",
        "solution": "**1. Total Transmission Model:**\nFor $N = 5$ plates:\n- There are $2N = 10$ boundaries, each with transmission factor $(1 - \\rho)$.\n- The total path length traveled inside the absorbing glass is $L = N l = 5 \\times 0.50\\text{ cm} = 2.50\\text{ cm}$.\nNeglecting internal secondary reflections, the net transmission is:\n$$\\tau = (1 - \\rho)^{2N} e^{-\\kappa N l}$$\n\n**2. Solving for $\\kappa$:**\n$$e^{-\\kappa N l} = \\frac{\\tau}{(1 - \\rho)^{2N}}$$\n$$-\\kappa N l = \\ln\\left[\\frac{\\tau}{(1 - \\rho)^{2N}}\\right] \\implies \\kappa = \\frac{1}{N l} \\ln\\left[\\frac{(1 - \\rho)^{2N}}{\\tau}\\right]$$\n\n**3. Numerical Evaluation:**\nFor $\\rho = 0.050$, $1 - \\rho = 0.950$:\n$$(1 - \\rho)^{2N} = (0.950)^{10} \\approx 0.59874$$\nGiven $\\tau = 0.55$:\n$$\\frac{(1 - \\rho)^{2N}}{\\tau} = \\frac{0.59874}{0.55} \\approx 1.0886$$\n$$\\ln(1.0886) \\approx 0.08490$$\nWith $N l = 2.50\\text{ cm}$:\n$$\\kappa = \\frac{0.08490}{2.50\\text{ cm}} \\approx 0.03396\\text{ cm}^{-1} \\approx 0.034\\text{ cm}^{-1}$$",
        "tags": ["pile of plates", "absorption coefficient", "glass", "reflection loss", "Beer-Lambert law"]
    },
    {
        "id": "5.216",
        "title": "Transmission of a Plate with Linearly Varying Absorption Coefficient",
        "difficulty": 2,
        "question": "A beam of monochromatic light falls normally on a plane-parallel plate of thickness $l$. The absorption coefficient of the plate varies linearly along the normal from $\\kappa_1$ at the front surface to $\\kappa_2$ at the rear surface. The reflection coefficient at each surface is $\\rho$. Neglecting secondary reflections, find the transmission coefficient $\\tau$ of the plate.",
        "hints": [
            "Write the absorption coefficient as a function of depth $x$: $\\kappa(x) = \\kappa_1 + \\frac{\\kappa_2 - \\kappa_1}{l} x$.",
            "The optical depth across the plate is $\\int_0^l \\kappa(x) dx$.",
            "Evaluate the integral to get $\\frac{\\kappa_1 + \\kappa_2}{2} l$, and include the reflection losses $(1 - \\rho)^2$ at both faces."
        ],
        "answer": "$\\tau = (1 - \\rho)^2 \\exp\\left(-\\frac{\\kappa_1 + \\kappa_2}{2} l\\right)$",
        "solution": "**1. Depth Dependence of Absorption Coefficient:**\nLet $x$ be the coordinate along the normal, with $x = 0$ at the entrance face and $x = l$ at the exit face.\nThe linear variation of $\\kappa(x)$ is:\n$$\\kappa(x) = \\kappa_1 + \\frac{\\kappa_2 - \\kappa_1}{l} x$$\n\n**2. Total Optical Depth:**\nAccording to the differential Beer-Lambert law $dI = -\\kappa(x) I dx$:\n$$\\int_{I_{\\text{in}}}^{I_{\\text{out}}} \\frac{dI}{I} = -\\int_0^l \\kappa(x) \\, dx$$\n$$\\int_0^l \\kappa(x) \\, dx = \\int_0^l \\left(\\kappa_1 + \\frac{\\kappa_2 - \\kappa_1}{l} x\\right) dx = \\left[ \\kappa_1 x + \\frac{\\kappa_2 - \\kappa_1}{2l} x^2 \\right]_0^l$$\n$$\\int_0^l \\kappa(x) \\, dx = \\kappa_1 l + \\frac{\\kappa_2 - \\kappa_1}{2} l = \\frac{\\kappa_1 + \\kappa_2}{2} l$$\nThus, the bulk attenuation factor is:\n$$e^{-\\int_0^l \\kappa(x) dx} = \\exp\\left(-\\frac{\\kappa_1 + \\kappa_2}{2} l\\right)$$\n\n**3. Transmission Coefficient:**\nIncluding reflection losses $(1 - \\rho)$ at both interfaces:\n$$\\tau = (1 - \\rho)^2 \\exp\\left(-\\frac{\\kappa_1 + \\kappa_2}{2} l\\right)$$",
        "tags": ["inhomogeneous medium", "absorption coefficient", "transmission coefficient", "Beer-Lambert law"]
    },
    {
        "id": "5.217",
        "title": "Transmission of Polychromatic Light with Linearly Dispersive Absorption",
        "difficulty": 2,
        "question": "A beam of light of total intensity $I_0$ falls normally on a transparent plane-parallel plate of thickness $l$. The beam contains all wavelengths in the interval from $\\lambda_1$ to $\\lambda_2$ with constant spectral intensity. In this wavelength interval, the absorption coefficient is a linear function of $\\lambda$ with boundary values $\\kappa_1$ and $\\kappa_2$. The reflection coefficient at each surface is $\\rho$. Neglecting secondary reflections, find the transmitted intensity $I$.",
        "hints": [
            "The incident spectral intensity density is $i_0 = \\frac{I_0}{\\lambda_2 - \\lambda_1}$.",
            "Since $\\kappa(\\lambda)$ varies linearly with $\\lambda$, substitute $d\\kappa = \\frac{\\kappa_2 - \\kappa_1}{\\lambda_2 - \\lambda_1} d\\lambda$ to change the integration variable from $\\lambda$ to $\\kappa$.",
            "Evaluate $\\int_{\\kappa_1}^{\\kappa_2} e^{-\\kappa l} d\\kappa = \\frac{e^{-\\kappa_1 l} - e^{-\\kappa_2 l}}{l}$, and multiply by $(1 - \\rho)^2$."
        ],
        "answer": "$I = I_0 (1 - \\rho)^2 \\frac{e^{-\\kappa_1 l} - e^{-\\kappa_2 l}}{(\\kappa_2 - \\kappa_1) l}$",
        "solution": "**1. Spectral Density of the Incident Beam:**\nThe total incident intensity $I_0$ is distributed uniformly over the wavelength interval $\\Delta\\lambda = \\lambda_2 - \\lambda_1$:\n$$i_0 = \\frac{dI_0}{d\\lambda} = \\frac{I_0}{\\lambda_2 - \\lambda_1}$$\n\n**2. Integration Over Wavelength:**\nFor each wavelength component, the transmitted spectral intensity (neglecting secondary reflections) is:\n$$dI = (1 - \\rho)^2 i_0 e^{-\\kappa(\\lambda) l} \\, d\\lambda$$\nThe total transmitted intensity is:\n$$I = (1 - \\rho)^2 \\frac{I_0}{\\lambda_2 - \\lambda_1} \\int_{\\lambda_1}^{\\lambda_2} e^{-\\kappa(\\lambda) l} \\, d\\lambda$$\n\n**3. Change of Variable:**\nBecause $\\kappa$ is a linear function of $\\lambda$:\n$$d\\kappa = \\frac{\\kappa_2 - \\kappa_1}{\\lambda_2 - \\lambda_1} \\, d\\lambda \\implies d\\lambda = \\frac{\\lambda_2 - \\lambda_1}{\\kappa_2 - \\kappa_1} \\, d\\kappa$$\nSubstituting this into the integral:\n$$I = (1 - \\rho)^2 \\frac{I_0}{\\lambda_2 - \\lambda_1} \\left(\\frac{\\lambda_2 - \\lambda_1}{\\kappa_2 - \\kappa_1}\\right) \\int_{\\kappa_1}^{\\kappa_2} e^{-\\kappa l} \\, d\\kappa$$\n$$I = \\frac{I_0 (1 - \\rho)^2}{\\kappa_2 - \\kappa_1} \\left[ -\\frac{e^{-\\kappa l}}{l} \\right]_{\\kappa_1}^{\\kappa_2} = I_0 (1 - \\rho)^2 \\frac{e^{-\\kappa_1 l} - e^{-\\kappa_2 l}}{(\\kappa_2 - \\kappa_1) l}$$",
        "tags": ["polychromatic light", "spectral integration", "absorption", "dispersion", "transmittance"]
    },
    {
        "id": "5.218",
        "title": "Passband of an Optical Filter with Quadratic Absorption Profile",
        "difficulty": 2,
        "question": "An optical filter is a plate of thickness $d$ whose absorption coefficient depends on wavelength $\\lambda$ as $\\kappa(\\lambda) = \\alpha (\\lambda - \\lambda_0)^2$, where $\\alpha$ and $\\lambda_0$ are constants. Find the passband $\\Delta\\lambda$ of this filter, defined as the wavelength interval at whose edges the attenuation of light is $\\eta$ times that at the central wavelength $\\lambda_0$. Assume the surface reflection coefficient is constant across all wavelengths.",
        "hints": [
            "At the central wavelength $\\lambda_0$, the absorption coefficient is $\\kappa(\\lambda_0) = 0$, so the transmitted intensity is $I(\\lambda_0) = I_0 (1 - \\rho)^2$.",
            "At the band edges $\\lambda_0 \\pm \\Delta\\lambda/2$, the transmitted intensity is attenuated by factor $\\eta$: $\\frac{I(\\lambda_0)}{I(\\lambda)} = \\eta$.",
            "From the Beer-Lambert law, $\\frac{I(\\lambda_0)}{I(\\lambda)} = e^{\\kappa(\\lambda) d} = \\eta \\implies \\kappa(\\lambda) d = \\ln\\eta$. Substitute $\\kappa = \\alpha (\\Delta\\lambda/2)^2$ and solve for $\\Delta\\lambda$."
        ],
        "answer": "$\\Delta\\lambda = 2 \\sqrt{\\frac{\\ln\\eta}{\\alpha d}}$",
        "solution": "**1. Transmitted Intensity at Center and Edges:**\nNeglecting secondary reflections, the transmitted intensity as a function of $\\lambda$ is:\n$$I(\\lambda) = I_0 (1 - \\rho)^2 e^{-\\kappa(\\lambda) d}$$\nAt the central transmission maximum $\\lambda = \\lambda_0$:\n$$\\kappa(\\lambda_0) = 0 \\implies I(\\lambda_0) = I_0 (1 - \\rho)^2$$\nAt the edges of the passband $\\lambda = \\lambda_0 \\pm \\frac{\\Delta\\lambda}{2}$:\n$$\\kappa = \\alpha \\left(\\frac{\\Delta\\lambda}{2}\\right)^2$$\n$$I = I_0 (1 - \\rho)^2 e^{-\\alpha (\\Delta\\lambda / 2)^2 d}$$\n\n**2. Attenuation Factor Condition:**\nThe problem specifies that at the band edges, the intensity is attenuated by factor $\\eta$ relative to the central maximum:\n$$\\frac{I(\\lambda_0)}{I} = \\eta$$\n$$e^{\\alpha (\\Delta\\lambda / 2)^2 d} = \\eta$$\n\n**3. Solving for Passband $\\Delta\\lambda$:**\nTaking the natural logarithm:\n$$\\alpha \\left(\\frac{\\Delta\\lambda}{2}\\right)^2 d = \\ln\\eta$$\n$$\\left(\\frac{\\Delta\\lambda}{2}\\right)^2 = \\frac{\\ln\\eta}{\\alpha d}$$\n$$\\frac{\\Delta\\lambda}{2} = \\sqrt{\\frac{\\ln\\eta}{\\alpha d}}$$\n$$\\Delta\\lambda = 2 \\sqrt{\\frac{\\ln\\eta}{\\alpha d}}$$",
        "tags": ["optical filter", "passband", "quadratic absorption", "Beer-Lambert law", "filter bandwidth"]
    },
    {
        "id": "5.219",
        "title": "Radiation Intensity Outside an Absorbing Spherical Shell",
        "difficulty": 2,
        "question": "A point source of monochromatic light emitting a luminous flux $\\Phi$ is positioned at the center of a spherical shell of substance with inner radius $a$ and outer radius $b$. The linear absorption coefficient of the substance is $\\kappa$, and the reflection coefficient of both spherical surfaces is $\\rho$. Neglecting secondary reflections, find the intensity $I$ of light emerging at the outer surface of the shell.",
        "hints": [
            "A point source emits uniformly into $4\\pi$ steradians. At the inner surface $r = a$, the flux entering the shell is $\\Phi_1 = (1 - \\rho) \\Phi$.",
            "Inside the shell, rays travel radially outward over path length $b - a$, suffering absorption: $\\Phi_2 = \\Phi_1 e^{-\\kappa(b - a)}$.",
            "At the outer surface $r = b$, transmission is $(1 - \\rho)$. The emerging flux is spread over the outer sphere area $4\\pi b^2$, giving $I = \\frac{\\Phi (1 - \\rho)^2 e^{-\\kappa(b - a)}}{4\\pi b^2}$."
        ],
        "answer": "$I = \\frac{\\Phi (1 - \\rho)^2 e^{-\\kappa(b - a)}}{4\\pi b^2}$",
        "solution": "**1. Luminous Flux Transmission Through the Shell:**\nConsider an isotropic point source emitting total luminous flux $\\Phi$.\n- At the inner spherical boundary ($r = a$), the light strikes at normal incidence everywhere. The fraction transmitted into the substance is:\n  $$\\Phi(a) = (1 - \\rho) \\Phi$$\n- The light propagates strictly radially outward through the absorbing substance from $r = a$ to $r = b$. The path length for all rays is $\\Delta r = b - a$.\n  By the Beer-Lambert law, the flux reaching the outer boundary is:\n  $$\\Phi(b^-) = \\Phi(a) e^{-\\kappa(b - a)} = (1 - \\rho) \\Phi e^{-\\kappa(b - a)}$$\n- At the outer boundary ($r = b$), transmission into the surrounding medium is $(1 - \\rho)$:\n  $$\\Phi_{\\text{out}} = (1 - \\rho) \\Phi(b^-) = (1 - \\rho)^2 \\Phi e^{-\\kappa(b - a)}$$\n\n**2. Intensity at the Outer Surface:**\nIntensity $I$ is defined as the flux per unit area perpendicular to the beam.\nAt the outer surface of the sphere of radius $b$, the total surface area is $4\\pi b^2$:\n$$I = \\frac{\\Phi_{\\text{out}}}{4\\pi b^2} = \\frac{\\Phi (1 - \\rho)^2 e^{-\\kappa(b - a)}}{4\\pi b^2}$$",
        "tags": ["spherical shell", "absorption", "point source", "Beer-Lambert law", "reflection loss"]
    },
    {
        "id": "5.220",
        "title": "Attenuation of an X-Ray Beam in a Lead Plate",
        "difficulty": 1,
        "question": "How many times will the intensity of a narrow X-ray beam of wavelength $\\lambda = 20\\text{ pm}$ decrease after passing through a lead plate of thickness $d = 1.0\\text{ mm}$ if the mass absorption coefficient for this wavelength is $\\mu / \\rho = 3.6\\text{ cm}^2/\\text{g}$? The density of lead is $\\rho = 11.3\\text{ g/cm}^3$.",
        "hints": [
            "The linear attenuation coefficient is $\\mu = \\left(\\frac{\\mu}{\\rho}\\right) \\rho$.",
            "The attenuation factor is $\\eta = \\frac{I_0}{I} = e^{\\mu d}$.",
            "Calculate $\\mu = 3.6 \\times 11.3\\text{ cm}^{-1}$, and evaluate $e^{\\mu d}$ for $d = 0.10\\text{ cm}$."
        ],
        "answer": "Will decrease by a factor of $e^{\\mu d} \\approx 0.6 \\times 10^2$ times",
        "solution": "**1. Linear Absorption Coefficient:**\nThe linear absorption coefficient $\\mu$ is related to the mass absorption coefficient $\\mu/\\rho$ and density $\\rho$ by:\n$$\\mu = \\left(\\frac{\\mu}{\\rho}\\right) \\rho$$\nGiven $\\mu/\\rho = 3.6\\text{ cm}^2/\\text{g}$ and $\\rho = 11.3\\text{ g/cm}^3$:\n$$\\mu = (3.6\\text{ cm}^2/\\text{g})(11.3\\text{ g/cm}^3) = 40.68\\text{ cm}^{-1}$$\n\n**2. Attenuation Factor:**\nFor a plate of thickness $d = 1.0\\text{ mm} = 0.10\\text{ cm}$:\n$$\\mu d = (40.68\\text{ cm}^{-1})(0.10\\text{ cm}) = 4.068$$\nThe intensity decreases by a factor of:\n$$\\eta = \\frac{I_0}{I} = e^{\\mu d} = e^{4.068} \\approx 58.4 \\approx 60 = 0.6 \\times 10^2$$",
        "tags": ["X-ray attenuation", "mass absorption coefficient", "lead plate", "Beer-Lambert law"]
    },
    {
        "id": "5.221",
        "title": "Equivalent Shielding Thickness of Lead and Aluminium for X-Rays",
        "difficulty": 2,
        "question": "A narrow beam of X-rays of wavelength $\\lambda = 62\\text{ pm}$ penetrates an aluminium screen of thickness $d_{\\text{Al}} = 2.6\\text{ cm}$. How thick must a lead screen be to attenuate the beam by the same factor? The mass absorption coefficients of aluminium and lead for this radiation are $3.48\\text{ cm}^2/\\text{g}$ and $72.0\\text{ cm}^2/\\text{g}$ respectively. (Densities: $\\rho_{\\text{Al}} = 2.70\\text{ g/cm}^3$, $\\rho_{\\text{Pb}} = 11.3\\text{ g/cm}^3$).",
        "hints": [
            "Equal attenuation means equal optical depth: $\\mu_{\\text{Al}} d_{\\text{Al}} = \\mu_{\\text{Pb}} d_{\\text{Pb}}$.",
            "Compute the linear absorption coefficients: $\\mu_{\\text{Al}} = (\\mu/\\rho)_{\\text{Al}} \\rho_{\\text{Al}}$ and $\\mu_{\\text{Pb}} = (\\mu/\\rho)_{\\text{Pb}} \\rho_{\\text{Pb}}$.",
            "Solve for $d_{\\text{Pb}} = d_{\\text{Al}} \\frac{\\mu_{\\text{Al}}}{\\mu_{\\text{Pb}}}$."
        ],
        "answer": "$d_{\\text{Pb}} = 0.3\\text{ mm}$",
        "solution": "**1. Condition for Equal Attenuation:**\nThe attenuation factors are $\\eta = e^{\\mu_{\\text{Al}} d_{\\text{Al}}}$ and $\\eta = e^{\\mu_{\\text{Pb}} d_{\\text{Pb}}}$.\nFor equal attenuation:\n$$\\mu_{\\text{Pb}} d_{\\text{Pb}} = \\mu_{\\text{Al}} d_{\\text{Al}} \\implies d_{\\text{Pb}} = d_{\\text{Al}} \\frac{\\mu_{\\text{Al}}}{\\mu_{\\text{Pb}}}$$\n\n**2. Linear Absorption Coefficients:**\n- For aluminium:\n  $$\\mu_{\\text{Al}} = \\left(\\frac{\\mu}{\\rho}\\right)_{\\text{Al}} \\rho_{\\text{Al}} = (3.48\\text{ cm}^2/\\text{g})(2.70\\text{ g/cm}^3) = 9.396\\text{ cm}^{-1}$$\n- For lead:\n  $$\\mu_{\\text{Pb}} = \\left(\\frac{\\mu}{\\rho}\\right)_{\\text{Pb}} \\rho_{\\text{Pb}} = (72.0\\text{ cm}^2/\\text{g})(11.3\\text{ g/cm}^3) = 813.6\\text{ cm}^{-1}$$\n\n**3. Required Lead Thickness:**\n$$d_{\\text{Pb}} = (2.6\\text{ cm}) \\frac{9.396\\text{ cm}^{-1}}{813.6\\text{ cm}^{-1}} = 2.6 \\times 0.011549\\text{ cm} \\approx 0.0300\\text{ cm} = 0.30\\text{ mm} \\approx 0.3\\text{ mm}$$",
        "tags": ["X-ray shielding", "mass absorption coefficient", "aluminium", "lead", "equivalent thickness"]
    },
    {
        "id": "5.222",
        "title": "Half-Value Layer Thickness of Aluminium for X-Rays",
        "difficulty": 1,
        "question": "Find the thickness $d_{1/2}$ of an aluminium layer that reduces by half the intensity of a narrow monochromatic X-ray beam if the corresponding mass absorption coefficient is $\\mu / \\rho = 0.32\\text{ cm}^2/\\text{g}$. (Density of aluminium $\\rho = 2.70\\text{ g/cm}^3$).",
        "hints": [
            "The linear absorption coefficient is $\\mu = \\left(\\frac{\\mu}{\\rho}\\right) \\rho$.",
            "The half-value layer condition is $e^{-\\mu d_{1/2}} = 1/2 \\implies d_{1/2} = \\frac{\\ln 2}{\\mu}$.",
            "Evaluate $d_{1/2} = \\frac{0.693}{\\mu}$ in millimeters."
        ],
        "answer": "$d_{1/2} = \\frac{\\ln 2}{\\mu} = 8\\text{ mm}$",
        "solution": "**1. Linear Absorption Coefficient:**\n$$\\mu = \\left(\\frac{\\mu}{\\rho}\\right) \\rho = (0.32\\text{ cm}^2/\\text{g})(2.70\\text{ g/cm}^3) = 0.864\\text{ cm}^{-1}$$\n\n**2. Half-Value Thickness (HVL):**\nBy definition, the half-value thickness satisfies:\n$$\\frac{I}{I_0} = e^{-\\mu d_{1/2}} = \\frac{1}{2}$$\n$$\\mu d_{1/2} = \\ln 2 \\implies d_{1/2} = \\frac{\\ln 2}{\\mu}$$\n\n**3. Numerical Evaluation:**\n$$d_{1/2} = \\frac{0.69315}{0.864\\text{ cm}^{-1}} \\approx 0.802\\text{ cm} = 8.02\\text{ mm} \\approx 8\\text{ mm}$$",
        "tags": ["half-value layer", "X-ray absorption", "aluminium", "Beer-Lambert law"]
    },
    {
        "id": "5.223",
        "title": "Number of Half-Value Layers for a Given Attenuation Factor",
        "difficulty": 1,
        "question": "How many $50\\%$-absorption (half-value) layers are there in a plate that reduces the intensity of a narrow X-ray beam by a factor of $\\eta = 50$?",
        "hints": [
            "Each half-value layer reduces the intensity by a factor of $2$.",
            "After $N$ half-value layers, the attenuation factor is $2^N = \\eta$.",
            "Solve for $N = \\frac{\\ln\\eta}{\\ln 2}$."
        ],
        "answer": "$N = \\frac{\\ln\\eta}{\\ln 2} = 5.6$",
        "solution": "**1. Attenuation in Terms of Half-Value Layers:**\nBy definition, each half-value layer (HVL) reduces the transmitted beam intensity by $50\\%$, i.e. by a factor of $2$.\nAfter passing through $N$ such layers, the beam intensity is reduced by:\n$$\\frac{I_0}{I} = 2^N = \\eta$$\n\n**2. Calculating $N$:**\nTaking the natural logarithm of both sides:\n$$N \\ln 2 = \\ln\\eta \\implies N = \\frac{\\ln\\eta}{\\ln 2}$$\n\n**3. Numerical Evaluation:**\nFor $\\eta = 50$:\n$$\\ln 50 \\approx 3.9120, \\quad \\ln 2 \\approx 0.69315$$\n$$N = \\frac{3.9120}{0.69315} \\approx 5.643 \\approx 5.6$$",
        "tags": ["half-value layers", "X-ray attenuation", "shielding", "exponential decay"]
    }
]
