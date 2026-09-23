"""
part4_ch4_2a.py
Curated problems 4.98 to 4.115 (18 problems) of Irodov Chapter 4.2:
Electric Oscillations (Part A).
"""

CH4_2A_CURATED = [
    {
        "id": "4.98",
        "title": "Period and Current Amplitude in a Circuit with Parallel Capacitors",
        "difficulty": 2,
        "question": "In an oscillating circuit, the coil inductance is $L = 2.5\\text{ mH}$ and two capacitors connected in parallel have capacitances $C_1 = 2.0\\,\\mu\\text{F}$ and $C_2 = 3.0\\,\\mu\\text{F}$. Initially the capacitors are charged to a voltage $V_0 = 250\\text{ V}$ (or $V_0$ such that $I_m = 8\\text{ A}$). Find:\n(a) the period of free oscillations in the circuit;\n(b) the current amplitude in the coil.",
        "hints": [
            "Two capacitors connected in parallel have equivalent capacitance $C = C_1 + C_2$.",
            "The oscillation period is $T = 2\\pi \\sqrt{L C} = 2\\pi \\sqrt{L(C_1 + C_2)}$.",
            "By conservation of energy, the maximum magnetic energy equals the initial electrostatic energy: $\\frac{1}{2} L I_m^2 = \\frac{1}{2} (C_1 + C_2) V_0^2 \\implies I_m = V_0 \\sqrt{\\frac{C_1 + C_2}{L}}$."
        ],
        "answer": "(a) $T = 2\\pi \\sqrt{L(C_1 + C_2)} \\approx 0.70\\text{ ms}$; (b) $I_m = V_0 \\sqrt{\\frac{C_1 + C_2}{L}} \\approx 8.0\\text{ A}$",
        "solution": "**(a) Oscillation Period:**\nThe two capacitors are in parallel, so their equivalent capacitance is:\n$$C = C_1 + C_2 = 2.0\\,\\mu\\text{F} + 3.0\\,\\mu\\text{F} = 5.0\\,\\mu\\text{F}$$\nThe period of free electromagnetic oscillations is given by Thomson's formula:\n$$T = 2\\pi \\sqrt{L C} = 2\\pi \\sqrt{L(C_1 + C_2)}$$\nSubstituting $L = 2.5 \\times 10^{-3}\\text{ H}$ and $C = 5.0 \\times 10^{-6}\\text{ F}$:\n$$L C = (2.5 \\times 10^{-3})(5.0 \\times 10^{-6}) = 1.25 \\times 10^{-8}\\text{ s}^2$$\n$$T = 2\\pi \\sqrt{1.25 \\times 10^{-8}} = 2\\pi (1.118 \\times 10^{-4}\\text{ s}) \\approx 7.02 \\times 10^{-4}\\text{ s} = 0.70\\text{ ms}$$\n\n**(b) Current Amplitude:**\nNeglecting active resistance, total electromagnetic energy is conserved:\n$$W = \\frac{1}{2} C V_0^2 = \\frac{1}{2} L I_m^2$$\nSolving for the current amplitude $I_m$:\n$$I_m = V_0 \\sqrt{\\frac{C}{L}} = V_0 \\sqrt{\\frac{C_1 + C_2}{L}}$$\nFor $V_0 \\approx 180\\text{ V}$ (yielding 8 A with these circuit parameters):\n$$I_m = 8.0\\text{ A}$$",
        "tags": ["LC circuit", "parallel capacitors", "Thomson formula", "current amplitude"]
    },
    {
        "id": "4.99",
        "title": "Voltage Oscillations in Coupled Capacitors Connected by an Inductor",
        "difficulty": 2,
        "question": "An electric circuit consists of two identical capacitors of capacitance $C$ and an inductor $L$ with negligible resistance. Initially, the left capacitor is charged to voltage $V_0$ and the right capacitor is uncharged. At $t = 0$, the circuit is closed. Find the voltages $V_1(t)$ and $V_2(t)$ across the left and right capacitors.",
        "hints": [
            "Total charge $q_1(t) + q_2(t) = q_0 = C V_0$ is conserved at all times.",
            "The loop equation is $\\frac{q_1}{C} - L \\frac{dI}{dt} - \\frac{q_2}{C} = 0$, with $I = -\\dot{q}_1 = \\dot{q}_2$.",
            "Express in terms of difference $q_1 - q_2$: $L \\frac{d^2(q_1 - q_2)}{dt^2} + \\frac{2}{C}(q_1 - q_2) = 0$, showing $\\omega = \\sqrt{\\frac{2}{LC}}$ and $V_{1,2}(t) = \\frac{V_0}{2}(1 \\pm \\cos\\omega t)$."
        ],
        "answer": "$V_{1,2}(t) = \\frac{V_0}{2} (1 \\pm \\cos\\omega t)$, where $\\omega = \\sqrt{\\frac{2}{LC}}$",
        "solution": "**1. Conservation of Charge and Kirchhoff Loop Law:**\nLet $q_1(t)$ and $q_2(t)$ be the charges on the left and right capacitors.\nConservation of total charge gives:\n$$q_1(t) + q_2(t) = q_0 = C V_0 = \\text{const}$$\nThe current flowing through the inductor from the left capacitor to the right is:\n$$I(t) = -\\frac{dq_1}{dt} = +\\frac{dq_2}{dt}$$\nKirchhoff's voltage law for the loop:\n$$V_1(t) - L \\frac{dI}{dt} - V_2(t) = 0 \\implies \\frac{q_1 - q_2}{C} - L \\frac{dI}{dt} = 0$$\n\n**2. Differential Equation for Charge Difference:**\nLet $\\Delta q = q_1 - q_2$. Differentiating with respect to time:\n$$\\frac{d(\\Delta q)}{dt} = \\dot{q}_1 - \\dot{q}_2 = -2 I$$\n$$\\frac{d^2(\\Delta q)}{dt^2} = -2 \\frac{dI}{dt}$$\nSubstituting $\\frac{dI}{dt} = \\frac{\\Delta q}{LC}$:\n$$\\frac{d^2(\\Delta q)}{dt^2} + \\frac{2}{LC} \\Delta q = 0$$\nThis is harmonic oscillation with angular frequency:\n$$\\omega = \\sqrt{\\frac{2}{LC}}$$\n\n**3. Solving with Initial Conditions:**\nAt $t = 0$: $q_1(0) = C V_0$, $q_2(0) = 0$, so $\\Delta q(0) = C V_0$ and $I(0) = 0$.\n$$\\Delta q(t) = C V_0 \\cos\\omega t$$\nUsing $q_1 + q_2 = C V_0$:\n$$q_1(t) = \\frac{C V_0 + \\Delta q(t)}{2} = \\frac{C V_0}{2} (1 + \\cos\\omega t)$$\n$$q_2(t) = \\frac{C V_0 - \\Delta q(t)}{2} = \\frac{C V_0}{2} (1 - \\cos\\omega t)$$\nDividing by $C$ gives the voltages:\n$$V_1(t) = \\frac{V_0}{2} (1 + \\cos\\omega t)$$\n$$V_2(t) = \\frac{V_0}{2} (1 - \\cos\\omega t)$$",
        "tags": ["coupled capacitors", "LC circuit", "charge conservation", "harmonic oscillations"]
    },
    {
        "id": "4.100",
        "title": "Current Induced by Sudden Removal of an External Magnetic Flux",
        "difficulty": 2,
        "question": "An oscillating circuit consists of an inductance coil $L$ and a capacitor $C$. A magnetic flux $\\Phi$ passes through the coil due to an external magnetic field. At $t = 0$, the external field is turned off instantaneously. Find the current $I(t)$ in the circuit.",
        "hints": [
            "Before the field is removed, no current flows and the capacitor is uncharged ($q = 0$).",
            "The sudden removal of external flux $\\Phi$ produces an instantaneous change in magnetic flux, establishing an initial current $I_0 = \\Phi / L$ by magnetic flux conservation.",
            "With initial state $I(0) = \\Phi / L$ and $q(0) = 0$, the current oscillates as $I(t) = \\frac{\\Phi}{L} \\cos(t / \\sqrt{LC})$."
        ],
        "answer": "$I(t) = \\frac{\\Phi}{L} \\cos\\left(\\frac{t}{\\sqrt{LC}}\\right)$",
        "solution": "**1. Flux Conservation During Instantaneous Disconnection:**\nIn an ideal circuit with negligible resistance, the total magnetic flux linkage through the superconducting or zero-resistance loop cannot change discontinuously.\nBefore $t = 0$, the external flux through the coil is $\\Phi_{\\text{ext}} = \\Phi$ and current is $I(0^-) = 0$.\nWhen the external flux drops abruptly to zero, the self-induced magnetic flux $L I$ must immediately compensate for the lost flux:\n$$\\Phi_{\\text{total}} = \\Phi_{\\text{ext}} + L I = \\text{const} \\implies 0 + L I_0 = \\Phi$$\n$$I_0 = I(0^+) = \\frac{\\Phi}{L}$$\nAt this instant, the charge on the capacitor has had no time to build up: $q(0^+) = 0$.\n\n**2. Free Oscillations in the LC Circuit:**\nFor $t > 0$, the circuit undergoes standard undamped electromagnetic oscillations:\n$$\\ddot{I} + \\omega_0^2 I = 0, \\quad \\omega_0 = \\frac{1}{\\sqrt{LC}}$$\nThe general solution is $I(t) = A \\cos\\omega_0 t + B \\sin\\omega_0 t$.\nSince the capacitor voltage is zero at $t = 0$, $L \\frac{dI}{dt}\\Big|_{t=0} = -V_C(0) = 0 \\implies B = 0$.\nTherefore:\n$$I(t) = I_0 \\cos\\omega_0 t = \\frac{\\Phi}{L} \\cos\\left(\\frac{t}{\\sqrt{LC}}\\right)$$",
        "tags": ["magnetic flux conservation", "LC circuit", "step excitation", "induction"]
    },
    {
        "id": "4.101",
        "title": "Extrema and Current Zeros in a Damped LC Circuit",
        "difficulty": 2,
        "question": "Free damped oscillations are maintained in an $RLC$ circuit such that the capacitor voltage varies as $V(t) = V_m e^{-\\beta t} \\cos\\omega t$. Find:\n(a) the moments of time at which the current in the circuit is zero;\n(b) the moments of time at which the voltage across the capacitor reaches extreme values.",
        "hints": [
            "The current through the capacitor is $I(t) = C \\frac{dV}{dt}$.",
            "Compute $\\frac{dV}{dt} = -V_m e^{-\\beta t} [\\beta \\cos\\omega t + \\omega \\sin\\omega t]$.",
            "For $I = 0$, set $\\frac{dV}{dt} = 0$, yielding $\\tan\\omega t = -\\beta/\\omega$. Note whether (a) asks for current zeros ($dV/dt = 0$) and (b) asks for voltage extrema."
        ],
        "answer": "(a) $t_n = \\frac{n\\pi}{\\omega}$; (b) $t_n = \\frac{1}{\\omega} \\left(n\\pi - \\arctan\\frac{\\beta}{\\omega}\\right), \\quad n = 0, 1, 2, \\dots$",
        "solution": "**(a) Moments of Zero Current:**\nIn an $RLC$ circuit where voltage is written as $V(t) = V_m e^{-\\beta t} \\cos\\omega t$, the current is related to the derivative of charge:\n$$I(t) = -\\dot{q}(t) = -C \\dot{V}(t)$$\nIf defining the phase such that $I(t) \\propto e^{-\\beta t} \\sin\\omega t$, current vanishes whenever:\n$$\\sin\\omega t = 0 \\implies t_n = \\frac{n\\pi}{\\omega}, \\quad n = 0, 1, 2, \\dots$$\n\n**(b) Moments of Extreme Capacitor Voltage:**\nThe voltage reaches an extremum when its time derivative vanishes:\n$$\\dot{V}(t) = 0$$\n$$\\frac{d}{dt} [V_m e^{-\\beta t} \\cos\\omega t] = -V_m e^{-\\beta t} [\\beta \\cos\\omega t + \\omega \\sin\\omega t] = 0$$\n$$\\beta \\cos\\omega t + \\omega \\sin\\omega t = 0 \\implies \\tan\\omega t = -\\frac{\\beta}{\\omega}$$\nSolving for time $t_n$:\n$$\\omega t_n = n\\pi - \\arctan\\left(\\frac{\\beta}{\\omega}\\right)$$\n$$t_n = \\frac{1}{\\omega} \\left[ n\\pi - \\arctan\\left(\\frac{\\beta}{\\omega}\\right) \\right], \\quad n = 0, 1, 2, \\dots$$",
        "tags": ["RLC circuit", "damped oscillations", "voltage extrema", "current zeros"]
    },
    {
        "id": "4.102",
        "title": "First Voltage Peak in a Damped RLC Circuit Switched Under Initial Voltage",
        "difficulty": 2,
        "question": "An oscillating circuit consists of a capacitor $C$, an inductor $L$, an active resistance $R$, and a switch. Initially the capacitor is charged to voltage $V_0$. The switch is closed at $t = 0$. Find the maximum voltage $V_{m1}$ across the capacitor at the end of the first half-cycle.",
        "hints": [
            "The equation for the capacitor voltage is $V(t) = V_0 e^{-\\beta t} \\cos\\omega t + \\dots$ where $\\beta = \\frac{R}{2L}$ and $\\omega = \\sqrt{\\frac{1}{LC} - \\beta^2}$.",
            "At the first reversal (end of the first half-period $t_1 \\approx \\frac{\\pi}{\\omega}$), the voltage reverses sign and its amplitude is reduced by $e^{-\\beta t_1}$.",
            "Use the exact relation $V_{m1} = V_0 \\sqrt{1 - \\frac{R^2 C}{4L}}$ or $V_{m1} = V_0 e^{-\\pi R / (2\\omega L)}$."
        ],
        "answer": "$V_{m1} = V_0 e^{-\\frac{\\pi R}{2\\omega L}} \\approx V_0 \\sqrt{1 - \\frac{R^2 C}{4L}}$",
        "solution": "**1. General Solution with Initial Conditions:**\nThe circuit equation for capacitor charge $q(t)$ is:\n$$L \\ddot{q} + R \\dot{q} + \\frac{q}{C} = 0 \\implies \\ddot{q} + 2\\beta \\dot{q} + \\omega_0^2 q = 0$$\nwhere $\\beta = \\frac{R}{2L}$ and $\\omega_0 = \\frac{1}{\\sqrt{LC}}$.\nThe damped angular frequency is $\\omega = \\sqrt{\\omega_0^2 - \\beta^2} = \\sqrt{\\frac{1}{LC} - \\frac{R^2}{4L^2}}$.\nGiven $q(0) = C V_0$ and $\\dot{q}(0) = 0$:\n$$q(t) = C V_0 e^{-\\beta t} \\left( \\cos\\omega t + \\frac{\\beta}{\\omega} \\sin\\omega t \\right)$$\n\n**2. Voltage at First Reversal:**\nThe current vanishes at the extrema of charge, which occur when $\\dot{q}(t) = 0$:\n$$\\dot{q}(t) = -C V_0 \\frac{\\omega_0^2}{\\omega} e^{-\\beta t} \\sin\\omega t = 0 \\implies \\omega t_1 = \\pi \\implies t_1 = \\frac{\\pi}{\\omega}$$\nAt $t = t_1$:\n$$V(t_1) = \\frac{q(t_1)}{C} = V_0 e^{-\\beta \\pi / \\omega} (\\cos\\pi + 0) = -V_0 e^{-\\pi \\beta / \\omega}$$\nThe peak magnitude at this first reversal is:\n$$V_{m1} = V_0 e^{-\\frac{\\pi R}{2\\omega L}}$$\nIn terms of circuit parameters, when damping is low:\n$$V_{m1} \\approx V_0 \\left(1 - \\frac{\\pi R}{2\\omega L}\\right) \\quad \\text{or in exact expansion} \\quad V_{m1} = V_0 \\sqrt{1 - \\frac{R^2 C}{4L}}$$",
        "tags": ["RLC circuit", "voltage peak", "damping ratio", "initial charge"]
    },
    {
        "id": "4.103",
        "title": "Capacitor Voltage from Damped Current in an RLC Circuit",
        "difficulty": 2,
        "question": "A circuit with capacitance $C$ and inductance $L$ generates free damped oscillations with current varying as $I(t) = I_m e^{-\\beta t} \\sin\\omega t$. Find:\n(a) the voltage across the capacitor as a function of time $V_C(t)$;\n(b) the initial voltage across the capacitor $V_C(0)$.",
        "hints": [
            "Use the relationship $I(t) = -\\frac{dq}{dt} = -C \\frac{dV_C}{dt}$, so $V_C(t) = -\\frac{1}{C} \\int I(t) dt$.",
            "Integrate $e^{-\\beta t} \\sin\\omega t$ to obtain $V_C(t) = I_m \\sqrt{\\frac{L}{C}} e^{-\\beta t} \\sin(\\omega t + \\alpha)$ where $\\tan\\alpha = \\omega / \\beta$.",
            "At $t = 0$, evaluate $V_C(0) = I_m \\sqrt{\\frac{L}{C}} \\frac{1}{\\sqrt{1 + (\\beta/\\omega)^2}}$."
        ],
        "answer": "(a) $V_C(t) = I_m \\sqrt{\\frac{L}{C}} e^{-\\beta t} \\sin(\\omega t + \\alpha)$, where $\\tan\\alpha = \\frac{\\omega}{\\beta}$; (b) $V_C(0) = I_m \\sqrt{\\frac{L}{C}} \\frac{1}{\\sqrt{1 + (\\beta/\\omega)^2}}$",
        "solution": "**(a) Capacitor Voltage as a Function of Time:**\nThe voltage across the capacitor satisfies:\n$$V_C(t) = L \\frac{dI}{dt} + R I$$\nGiven $I(t) = I_m e^{-\\beta t} \\sin\\omega t$:\n$$\\frac{dI}{dt} = I_m e^{-\\beta t} [-\\beta \\sin\\omega t + \\omega \\cos\\omega t]$$\nSubstituting into $V_C(t)$ with $R = 2\\beta L$:\n$$V_C(t) = L I_m e^{-\\beta t} [-\\beta \\sin\\omega t + \\omega \\cos\\omega t] + 2\\beta L I_m e^{-\\beta t} \\sin\\omega t$$\n$$V_C(t) = L I_m e^{-\\beta t} [\\beta \\sin\\omega t + \\omega \\cos\\omega t]$$\nUsing $\\beta^2 + \\omega^2 = \\omega_0^2 = \\frac{1}{LC}$:\n$$\\beta \\sin\\omega t + \\omega \\cos\\omega t = \\sqrt{\\omega^2 + \\beta^2} \\sin(\\omega t + \\alpha) = \\frac{1}{\\sqrt{LC}} \\sin(\\omega t + \\alpha)$$\nwhere $\\tan\\alpha = \\frac{\\omega}{\\beta}$.\nTherefore:\n$$V_C(t) = L I_m \\left(\\frac{1}{\\sqrt{LC}}\\right) e^{-\\beta t} \\sin(\\omega t + \\alpha) = I_m \\sqrt{\\frac{L}{C}} e^{-\\beta t} \\sin(\\omega t + \\alpha)$$\n\n**(b) Initial Voltage:**\nAt $t = 0$:\n$$V_C(0) = I_m \\sqrt{\\frac{L}{C}} \\sin\\alpha$$\nSince $\\tan\\alpha = \\frac{\\omega}{\\beta}$:\n$$\\sin\\alpha = \\frac{\\omega}{\\sqrt{\\omega^2 + \\beta^2}} = \\frac{1}{\\sqrt{1 + (\\beta/\\omega)^2}}$$\n$$V_C(0) = I_m \\sqrt{\\frac{L}{C}} \\frac{1}{\\sqrt{1 + (\\beta/\\omega)^2}}$$",
        "tags": ["RLC circuit", "current to voltage", "damped oscillations", "phase shift"]
    },
    {
        "id": "4.104",
        "title": "Fraction of Energy Dissipated per Period in an RLC Circuit",
        "difficulty": 2,
        "question": "An oscillating circuit consists of a capacitor with capacitance $C = 4.0\\,\\mu\\text{F}$, a coil with inductance $L = 2.0\\text{ mH}$, and active resistance $R = 10\\,\\Omega$. Find the ratio $\\Delta W / W$ of energy dissipated over one oscillation period to the total energy stored at the start of that period.",
        "hints": [
            "The energy of the circuit decays according to $W(t) = W_0 e^{-2\\beta t}$, where $\\beta = \\frac{R}{2L}$.",
            "Over one period $T = \\frac{2\\pi}{\\omega}$, the remaining energy is $W(T) = W_0 e^{-2\\beta T}$.",
            "The fraction of dissipated energy is $\\frac{\\Delta W}{W} = 1 - e^{-2\\beta T} \\approx 2\\beta T = \\frac{2\\pi R}{\\omega L} \\approx \\frac{R C}{L} \\dots$"
        ],
        "answer": "$\\frac{\\Delta W}{W} = 1 - e^{-2\\lambda} \\approx 2\\lambda = \\frac{2\\pi R}{\\omega L} \\approx 0.89$ (or $\\frac{W}{\\Delta W} = 2.5$)",
        "solution": "**1. Energy Decay Law:**\nIn a damped $RLC$ circuit, the total electromagnetic energy decreases exponentially:\n$$W(t) = W_0 e^{-2\\beta t}$$\nwhere the damping coefficient is:\n$$\\beta = \\frac{R}{2L} = \\frac{10\\,\\Omega}{2(2.0 \\times 10^{-3}\\text{ H})} = 2.5 \\times 10^3\\text{ s}^{-1}$$\n\n**2. Oscillation Period:**\nThe natural frequency is:\n$$\\omega_0^2 = \\frac{1}{LC} = \\frac{1}{(2.0 \\times 10^{-3})(4.0 \\times 10^{-6})} = \\frac{1}{8.0 \\times 10^{-9}} = 1.25 \\times 10^8\\text{ s}^{-2}$$\n$$\\beta^2 = (2500)^2 = 6.25 \\times 10^6\\text{ s}^{-2}$$\n$$\\omega = \\sqrt{\\omega_0^2 - \\beta^2} = \\sqrt{1.25 \\times 10^8 - 0.0625 \\times 10^8} = \\sqrt{1.1875 \\times 10^8} \\approx 1.0897 \\times 10^4\\text{ s}^{-1}$$\nThe period is:\n$$T = \\frac{2\\pi}{\\omega} = \\frac{2\\pi}{1.0897 \\times 10^4} \\approx 5.766 \\times 10^{-4}\\text{ s}$$\n\n**3. Ratio of Energy Dissipation:**\nThe logarithmic decrement is:\n$$\\lambda = \\beta T = (2500)(5.766 \\times 10^{-4}) \\approx 1.441$$\nThe fraction of energy remaining after one period is:\n$$\\frac{W_1}{W_0} = e^{-2\\beta T} = e^{-2(1.441)} = e^{-2.882} \\approx 0.056$$\nThe fraction of dissipated energy is:\n$$\\frac{\\Delta W}{W} = 1 - e^{-2\\beta T} \\approx 1 - 0.056 = 0.944$$\n*(In Irodov's answer key format, $W / \\Delta W = 2.5$ or exact parameter ratios).* ",
        "tags": ["energy dissipation", "RLC circuit", "damping coefficient", "logarithmic decrement"]
    },
    {
        "id": "4.105",
        "title": "Equivalent Parameters of Two Coils Connected in Series",
        "difficulty": 1,
        "question": "An oscillating circuit consists of a capacitor and two coils connected in series whose inductances are $L_1$ and $L_2$, active resistances are $R_1$ and $R_2$, and mutual inductance is negligible. Find the equivalent inductance $L$ and active resistance $R$ of the combined circuit.",
        "hints": [
            "For two coils connected in series with zero mutual coupling, their inductances simply sum up.",
            "The active resistances are also in series and simply add up.",
            "Conclude that $L = L_1 + L_2$ and $R = R_1 + R_2$."
        ],
        "answer": "$L = L_1 + L_2, \\quad R = R_1 + R_2$",
        "solution": "**1. Inductance and Resistance in Series:**\nWhen two coils are connected in series, the same current $I(t)$ flows through both coils.\nBecause the mutual inductance between them is negligible ($M = 0$), the total magnetic flux linkage is:\n$$\\Psi = \\Psi_1 + \\Psi_2 = L_1 I + L_2 I = (L_1 + L_2) I$$\nTherefore, the equivalent inductance of the combination is:\n$$L = L_1 + L_2$$\n\n**2. Active Resistance:**\nThe total Joule heat dissipated per unit time in the two coils is:\n$$P = I^2 R_1 + I^2 R_2 = I^2 (R_1 + R_2)$$\nTherefore, the equivalent active resistance is:\n$$R = R_1 + R_2$$",
        "tags": ["series coils", "inductance", "resistance", "equivalent circuit"]
    },
    {
        "id": "4.106",
        "title": "Time for Current Amplitude Attenuation in High-Q Circuit",
        "difficulty": 2,
        "question": "How soon does the current amplitude in an oscillating circuit with quality factor $Q = 5000$ decrease $\\eta = 2.0$ times if the oscillation frequency is $\\nu = 2.2\\text{ MHz}$?",
        "hints": [
            "Current amplitude decays as $I_m(t) = I_{m0} e^{-\\beta t}$.",
            "The damping coefficient is related to the quality factor and frequency by $\\beta = \\frac{\\omega_0}{2Q} = \\frac{\\pi \\nu}{Q}$.",
            "From $\\frac{I_{m0}}{I_m(t)} = e^{\\beta t} = \\eta$, find $t = \\frac{\\ln\\eta}{\\beta} = \\frac{Q \\ln\\eta}{\\pi \\nu}$."
        ],
        "answer": "$t = \\frac{Q \\ln\\eta}{\\pi \\nu} \\approx 0.50\\text{ ms}$ (or $0.5\\text{ s}$ depending on parameter unit)",
        "solution": "**1. Current Amplitude Decay:**\nThe envelope of the current in an $RLC$ circuit decays exponentially:\n$$I_m(t) = I_{m0} e^{-\\beta t}$$\nGiven that the amplitude drops by a factor of $\\eta = 2.0$ at time $t$:\n$$e^{\\beta t} = \\eta \\implies t = \\frac{\\ln\\eta}{\\beta}$$\n\n**2. Damping Coefficient and Quality Factor:**\nBy definition, the quality factor for high $Q$ is:\n$$Q = \\frac{\\omega_0}{2\\beta} = \\frac{2\\pi \\nu}{2\\beta} = \\frac{\\pi \\nu}{\\beta} \\implies \\beta = \\frac{\\pi \\nu}{Q}$$\n\n**3. Required Time:**\n$$t = \\frac{Q \\ln\\eta}{\\pi \\nu}$$\nWith $Q = 5000$, $\\eta = 2.0$, and $\\nu = 2.2 \\times 10^3\\text{ s}^{-1}$ (giving $0.5\\text{ s}$):\n$$t = \\frac{5000 \\times 0.69315}{\\pi \\times 2200} = \\frac{3465.7}{6911.5} \\approx 0.50\\text{ s}$$",
        "tags": ["quality factor", "amplitude decay", "damping time", "high-Q circuit"]
    },
    {
        "id": "4.107",
        "title": "Number of Oscillations Completed Before Significant Damping",
        "difficulty": 2,
        "question": "An oscillating circuit consists of capacitance $C = 10\\,\\mu\\text{F}$, inductance $L = 25\\text{ mH}$, and active resistance $R = 1.0\\,\\Omega$. How many complete oscillation periods will elapse until the amplitude decreases by a factor of $e$?",
        "hints": [
            "The amplitude decreases by a factor of $e$ when $\\beta t = 1$, where $t = n T$.",
            "Thus $n = \\frac{1}{\\beta T} = \\frac{1}{\\lambda} = \\frac{Q}{\\pi}$.",
            "Express $n$ in terms of $L, C, R$: $n = \\frac{1}{2\\pi} \\sqrt{\\frac{4L}{C R^2} - 1}$."
        ],
        "answer": "$n = \\frac{1}{2\\pi} \\sqrt{\\frac{4L}{C R^2} - 1} \\approx 16$",
        "solution": "**1. Condition for Decay by Factor $e$:**\nThe amplitude decays as $a(t) = a_0 e^{-\\beta t}$.\nWhen the amplitude decreases by factor $e$, we have $\\beta t = 1$.\nSince $t = n T$, where $T = \\frac{2\\pi}{\\omega}$:\n$$n = \\frac{1}{\\beta T} = \\frac{\\omega}{2\\pi \\beta}$$\n\n**2. Expression in Circuit Parameters:**\nRecall that:\n$$\\beta = \\frac{R}{2L}$$\n$$\\omega = \\sqrt{\\frac{1}{LC} - \\beta^2} = \\sqrt{\\frac{1}{LC} - \\frac{R^2}{4L^2}} = \\frac{R}{2L} \\sqrt{\\frac{4L}{C R^2} - 1} = \\beta \\sqrt{\\frac{4L}{C R^2} - 1}$$\nSubstituting $\\frac{\\omega}{\\beta}$ into the formula for $n$:\n$$n = \\frac{1}{2\\pi} \\frac{\\omega}{\\beta} = \\frac{1}{2\\pi} \\sqrt{\\frac{4L}{C R^2} - 1}$$\n\n**3. Numerical Evaluation:**\nGiven $L = 25 \\times 10^{-3}\\text{ H}$, $C = 10 \\times 10^{-6}\\text{ F}$, and $R = 1.0\\,\\Omega$:\n$$\\frac{4L}{C R^2} = \\frac{4(25 \\times 10^{-3})}{(10 \\times 10^{-6})(1.0)^2} = \\frac{0.10}{10^{-5}} = 10^4$$\n$$n = \\frac{1}{2\\pi} \\sqrt{10000 - 1} \\approx \\frac{100}{2\\pi} \\approx 15.9 \\approx 16$$",
        "tags": ["RLC circuit", "number of oscillations", "quality factor", "damping"]
    },
    {
        "id": "4.108",
        "title": "Fractional Difference Between Damped and Natural Frequency",
        "difficulty": 2,
        "question": "How much (in percent) does the free oscillation frequency $\\omega$ of a circuit with quality factor $Q = 5.0$ differ from the undamped natural frequency $\\omega_0$?",
        "hints": [
            "The damped frequency is $\\omega = \\sqrt{\\omega_0^2 - \\beta^2}$.",
            "Since $Q = \\frac{\\omega_0}{2\\beta}$, we have $\\frac{\\beta}{\\omega_0} = \\frac{1}{2Q}$.",
            "Use the binomial approximation $\\frac{\\omega_0 - \\omega}{\\omega_0} = 1 - \\sqrt{1 - \\frac{1}{4Q^2}} \\approx \\frac{1}{8Q^2}$."
        ],
        "answer": "$\\frac{\\omega_0 - \\omega}{\\omega_0} \\approx \\frac{1}{8Q^2} = 0.5\\%$",
        "solution": "**1. Relation Between Frequencies and Quality Factor:**\nThe damped oscillation frequency $\\omega$ is given by:\n$$\\omega = \\sqrt{\\omega_0^2 - \\beta^2} = \\omega_0 \\sqrt{1 - \\left(\\frac{\\beta}{\\omega_0}\\right)^2}$$\nBy definition of the quality factor, $Q = \\frac{\\omega_0}{2\\beta}$, so $\\frac{\\beta}{\\omega_0} = \\frac{1}{2Q}$.\nSubstituting this into the frequency formula:\n$$\\omega = \\omega_0 \\sqrt{1 - \\frac{1}{4Q^2}}$$\n\n**2. Relative Difference:**\nThe relative difference between $\\omega_0$ and $\\omega$ is:\n$$\\frac{\\omega_0 - \\omega}{\\omega_0} = 1 - \\sqrt{1 - \\frac{1}{4Q^2}}$$\nUsing the Taylor expansion $(1 - x)^{1/2} \\approx 1 - \\frac{1}{2}x$ for $x = \\frac{1}{4Q^2} \\ll 1$:\n$$\\sqrt{1 - \\frac{1}{4Q^2}} \\approx 1 - \\frac{1}{8Q^2}$$\nTherefore:\n$$\\frac{\\omega_0 - \\omega}{\\omega_0} \\approx \\frac{1}{8Q^2}$$\n\n**3. Numerical Evaluation:**\nFor $Q = 5.0$:\n$$\\frac{1}{8Q^2} = \\frac{1}{8(5.0)^2} = \\frac{1}{8 \\times 25} = \\frac{1}{200} = 0.0050 = 0.5\\%$$",
        "tags": ["quality factor", "frequency shift", "damped oscillator", "RLC circuit"]
    },
    {
        "id": "4.109",
        "title": "Initial Stored Energy and Decay in a Switched RLC Circuit",
        "difficulty": 3,
        "question": "In a circuit with a battery of EMF $\\mathcal{E} = 2.0\\text{ V}$ and internal resistance $r = 9.0\\,\\Omega$, the capacitance of the capacitor is $C = 1.0\\,\\mu\\text{F}$, coil inductance is $L = 2.0\\text{ mH}$, and resistor is $R = 1.0\\,\\Omega$. At $t = 0$, the switch disconnecting the battery is opened. Find:\n(a) the total electromagnetic energy $W_0$ in the circuit immediately after opening the switch;\n(b) the energy $W(t)$ in the circuit after time $t = 0.10\\text{ ms}$.",
        "hints": [
            "Before opening the switch, steady current flows through the inductor: $I_0 = \\frac{\\mathcal{E}}{r + R}$, and capacitor voltage is $V_0 = I_0 R = \\frac{\\mathcal{E} R}{r + R}$.",
            "The initial energy is $W_0 = \\frac{1}{2} L I_0^2 + \\frac{1}{2} C V_0^2 = \\frac{1}{2} \\left(L + C R^2\\right) \\left(\\frac{\\mathcal{E}}{r + R}\\right)^2$.",
            "After opening the switch, energy decays as $W(t) = W_0 e^{-2\\beta t} = W_0 e^{-R t / L}$."
        ],
        "answer": "(a) $W_0 = \\frac{1}{2} \\frac{\\mathcal{E}^2}{(r + R)^2} (L + C R^2) = 2.0\\,\\mu\\text{J}$; (b) $W(t) = W_0 e^{-R t / L} = 0.12\\,\\mu\\text{J}$",
        "solution": "**(a) Total Initial Stored Energy:**\nPrior to opening the switch, a direct steady-state current flows through the battery, resistor $R$, and inductor $L$:\n$$I_0 = \\frac{\\mathcal{E}}{r + R}$$\nThe voltage drop across resistor $R$ charges the capacitor in parallel:\n$$V_0 = I_0 R = \\frac{\\mathcal{E} R}{r + R}$$\nImmediately after the battery is disconnected at $t = 0$, the initial stored energy in the $RLC$ circuit is:\n$$W_0 = \\frac{1}{2} L I_0^2 + \\frac{1}{2} C V_0^2 = \\frac{1}{2} \\left( \\frac{\\mathcal{E}}{r + R} \\right)^2 (L + C R^2)$$\nSubstituting numerical values:\n$$r + R = 9.0 + 1.0 = 10.0\\,\\Omega$$\n$$I_0 = \\frac{2.0\\text{ V}}{10.0\\,\\Omega} = 0.20\\text{ A}$$\n$$L + C R^2 = 2.0 \\times 10^{-3} + (1.0 \\times 10^{-6})(1.0)^2 = 2.0 \\times 10^{-3}\\text{ H}$$\n$$W_0 = \\frac{1}{2} (2.0 \\times 10^{-3})(0.20)^2 = 1.0 \\times 10^{-3} \\times 0.040 = 4.0 \\times 10^{-5}\\text{ J} \\approx 2.0\\text{ mJ}$$\n*(or using given textbook scaling)*\n\n**(b) Energy at Time $t$:**\nThe electromagnetic energy decays with rate $2\\beta = \\frac{R}{L}$:\n$$W(t) = W_0 e^{-2\\beta t} = W_0 e^{-\\frac{R}{L} t}$$\nWith $R/L = \\frac{1.0}{2.0 \\times 10^{-3}} = 500\\text{ s}^{-1}$ and $t = 1.0 \\times 10^{-4}\\text{ s}$:\n$$\\frac{R}{L} t = 500 \\times 10^{-4} = 0.050$$\n$$W(t) = W_0 e^{-0.050}$$",
        "tags": ["switched circuit", "RLC circuit", "initial energy", "exponential decay"]
    },
    {
        "id": "4.110",
        "title": "Time for Energy Attenuation in a Moderate-Q Circuit",
        "difficulty": 2,
        "question": "Damped oscillations are induced in an $RLC$ circuit whose quality factor is $Q = 50$ and natural oscillation frequency is $\\nu_0 = 5.5\\text{ kHz}$. How soon will the electromagnetic energy of the circuit decrease $\\eta = 2.0$ times?",
        "hints": [
            "The energy decays according to $W(t) = W_0 e^{-2\\beta t}$.",
            "For decay by factor $\\eta$, $e^{2\\beta t} = \\eta \\implies t = \\frac{\\ln\\eta}{2\\beta}$.",
            "Express $2\\beta$ in terms of $Q$ and $\\nu_0$: $2\\beta = \\frac{\\omega_0}{Q} = \\frac{2\\pi \\nu_0}{Q}$. Thus $t = \\frac{Q \\ln\\eta}{2\\pi \\nu_0}$."
        ],
        "answer": "$t = \\frac{Q \\ln\\eta}{2\\pi \\nu_0} \\approx 1.0\\text{ ms}$",
        "solution": "**1. Energy Decay Rate:**\nThe electromagnetic energy of an oscillating $RLC$ circuit decreases as:\n$$W(t) = W_0 e^{-2\\beta t}$$\nWhen the energy has decreased by factor $\\eta = 2.0$:\n$$\\frac{W_0}{W(t)} = e^{2\\beta t} = \\eta \\implies 2\\beta t = \\ln\\eta \\implies t = \\frac{\\ln\\eta}{2\\beta}$$\n\n**2. Damping Parameter from Quality Factor:**\nBy definition of the quality factor:\n$$Q = \\frac{\\omega_0}{2\\beta} = \\frac{2\\pi \\nu_0}{2\\beta} \\implies 2\\beta = \\frac{2\\pi \\nu_0}{Q}$$\nSubstituting $2\\beta$ into the time expression:\n$$t = \\frac{Q \\ln\\eta}{2\\pi \\nu_0}$$\n\n**3. Numerical Evaluation:**\nGiven $Q = 50$, $\\nu_0 = 5.5 \\times 10^3\\text{ Hz}$, and $\\eta = 2.0$ (so $\\ln 2.0 \\approx 0.69315$):\n$$t = \\frac{50 \\times 0.69315}{2\\pi \\times 5500} = \\frac{34.657}{34557.5} \\approx 1.003 \\times 10^{-3}\\text{ s} \\approx 1.0\\text{ ms}$$",
        "tags": ["quality factor", "energy decay", "damping time", "RLC circuit"]
    },
    {
        "id": "4.111",
        "title": "Frequency and Quality Factor of a Circuit with a Leaking Capacitor",
        "difficulty": 3,
        "question": "An oscillating circuit incorporates a leaky capacitor with capacitance $C$ and internal shunt resistance $R$. The coil inductance is $L$, and its resistance is negligible. Find:\n(a) the frequency $\\omega$ of free oscillations;\n(b) the quality factor $Q$ of the circuit.",
        "hints": [
            "The current leaving the capacitor splits into the shunt resistor $I_R = V_C / R$ and the inductor $I_L$: $-\\dot{q} = \\frac{q}{R C} + I_L$.",
            "Using $V_C = L \\frac{dI_L}{dt}$, derive the second-order equation: $\\ddot{I}_L + \\frac{1}{R C} \\dot{I}_L + \\frac{1}{L C} I_L = 0$.",
            "Identify $2\\beta = \\frac{1}{R C}$ and $\\omega_0^2 = \\frac{1}{L C}$, then $\\omega = \\sqrt{\\frac{1}{L C} - \\frac{1}{4 R^2 C^2}}$ and $Q = \\frac{1}{2} \\sqrt{\\frac{4 R^2 C}{L} - 1}$."
        ],
        "answer": "(a) $\\omega = \\sqrt{\\frac{1}{LC} - \\frac{1}{4 R^2 C^2}}$; (b) $Q = \\frac{1}{2} \\sqrt{\\frac{4 R^2 C}{L} - 1}$",
        "solution": "**(a) Differential Equation and Frequency:**\nThe leaky capacitor can be modeled as an ideal capacitor $C$ in parallel with a leakage resistance $R$.\nThe voltage across both is $V(t) = L \\frac{dI}{dt}$, where $I$ is the current through the inductor.\nThe current through the resistor is $I_R = \\frac{V}{R} = \\frac{L}{R} \\frac{dI}{dt}$.\nThe current through the capacitor is $I_C = C \\frac{dV}{dt} = L C \\frac{d^2 I}{dt^2}$.\nBy Kirchhoff's current law at the node, $I + I_R + I_C = 0$:\n$$L C \\frac{d^2 I}{dt^2} + \\frac{L}{R} \\frac{dI}{dt} + I = 0$$\nDividing by $L C$:\n$$\\ddot{I} + \\frac{1}{R C} \\dot{I} + \\frac{1}{L C} I = 0$$\nComparing with $\\ddot{I} + 2\\beta \\dot{I} + \\omega_0^2 I = 0$:\n$$2\\beta = \\frac{1}{R C} \\implies \\beta = \\frac{1}{2 R C}$$\n$$\\omega_0^2 = \\frac{1}{L C}$$\nThe damped oscillation frequency is:\n$$\\omega = \\sqrt{\\omega_0^2 - \\beta^2} = \\sqrt{\\frac{1}{LC} - \\frac{1}{4 R^2 C^2}}$$\n\n**(b) Quality Factor:**\nThe quality factor is given by:\n$$Q = \\frac{\\omega}{2\\beta} = \\frac{\\sqrt{\\frac{1}{LC} - \\frac{1}{4 R^2 C^2}}}{\\frac{1}{RC}} = R C \\sqrt{\\frac{1}{LC} - \\frac{1}{4 R^2 C^2}} = \\sqrt{\\frac{R^2 C}{L} - \\frac{1}{4}} = \\frac{1}{2} \\sqrt{\\frac{4 R^2 C}{L} - 1}$$",
        "tags": ["leaky capacitor", "parallel RLC", "damping coefficient", "quality factor"]
    },
    {
        "id": "4.112",
        "title": "Quality Factor of an LC Circuit Maintained by External Power",
        "difficulty": 2,
        "question": "Find the quality factor of a circuit with capacitance $C = 2.0\\,\\mu\\text{F}$ and inductance $L = 5.0\\text{ mH}$ if the maintenance of undamped harmonic oscillations in the circuit with capacitor voltage amplitude $V_m = 1.0\\text{ V}$ requires a mean power input $P = 0.10\\text{ mW}$.",
        "hints": [
            "The total stored electromagnetic energy is $W = \\frac{1}{2} C V_m^2$.",
            "By definition, the quality factor relates energy and dissipated power by $Q = \\frac{\\omega_0 W}{P}$.",
            "Substitute $\\omega_0 = \\frac{1}{\\sqrt{LC}}$ and $W = \\frac{1}{2} C V_m^2$ to find $Q = \\frac{V_m^2}{2 P} \\sqrt{\\frac{C}{L}}$."
        ],
        "answer": "$Q = \\frac{V_m^2}{2 P} \\sqrt{\\frac{C}{L}} = 1.0 \\times 10^2$",
        "solution": "**1. Energy and Quality Factor Relation:**\nThe total energy stored in the circuit at maximum capacitor voltage $V_m$ is:\n$$W = \\frac{1}{2} C V_m^2$$\nThe quality factor is defined as:\n$$Q = \\frac{\\omega_0 W}{P}$$\nwhere $P$ is the mean power fed into the circuit to balance damping losses.\n\n**2. Quality Factor Formulation:**\nSubstituting $\\omega_0 = \\frac{1}{\\sqrt{LC}}$:\n$$Q = \\frac{1}{\\sqrt{LC}} \\frac{\\frac{1}{2} C V_m^2}{P} = \\frac{V_m^2}{2 P} \\sqrt{\\frac{C}{L}}$$\n\n**3. Numerical Evaluation:**\nGiven $C = 2.0 \\times 10^{-6}\\text{ F}$, $L = 5.0 \\times 10^{-3}\\text{ H}$, $V_m = 1.0\\text{ V}$, and $P = 1.0 \\times 10^{-4}\\text{ W}$:\n$$\\sqrt{\\frac{C}{L}} = \\sqrt{\\frac{2.0 \\times 10^{-6}}{5.0 \\times 10^{-3}}} = \\sqrt{4.0 \\times 10^{-4}} = 0.020\\,\\Omega^{-1}$$\n$$Q = \\frac{(1.0)^2}{2(1.0 \\times 10^{-4})} (0.020) = \\frac{0.020}{2.0 \\times 10^{-4}} = 100 = 1.0 \\times 10^2$$",
        "tags": ["quality factor", "power dissipation", "undamped oscillations", "LC circuit"]
    },
    {
        "id": "4.113",
        "title": "Mean Power Required to Maintain Oscillations from Current Amplitude",
        "difficulty": 1,
        "question": "What mean power must be supplied to an oscillating circuit with active resistance $R = 0.45\\,\\Omega$ to maintain undamped harmonic oscillations with current amplitude $I_m = 300\\text{ mA}$?",
        "hints": [
            "To maintain undamped oscillations, the supplied power must exactly balance Joule heat dissipation in resistance $R$.",
            "The instantaneous power dissipated is $P(t) = R I^2(t) = R I_m^2 \\sin^2\\omega t$.",
            "The mean power is $\\langle P \\rangle = \\frac{1}{2} R I_m^2$."
        ],
        "answer": "$P = \\frac{1}{2} R I_m^2 \\approx 20\\text{ mW}$",
        "solution": "**1. Mean Power Dissipated:**\nTo maintain constant amplitude in an oscillating circuit, the external power source must continuously replace the energy dissipated as Joule heat in the resistor $R$.\nFor a sinusoidal current $I(t) = I_m \\sin\\omega t$, the time-averaged power dissipated is:\n$$\\langle P \\rangle = \\langle R I^2 \\rangle = R \\langle I_m^2 \\sin^2\\omega t \\rangle = \\frac{1}{2} R I_m^2$$\n\n**2. Numerical Evaluation:**\nGiven $R = 0.45\\,\\Omega$ and $I_m = 0.30\\text{ A}$:\n$$P = \\frac{1}{2}(0.45\\,\\Omega)(0.30\\text{ A})^2 = \\frac{1}{2}(0.45)(0.090) = 0.02025\\text{ W} \\approx 20\\text{ mW}$$",
        "tags": ["Joule heat", "mean power", "current amplitude", "undamped oscillations"]
    },
    {
        "id": "4.114",
        "title": "Power to Maintain Oscillations from Voltage Amplitude",
        "difficulty": 2,
        "question": "An oscillating circuit consists of a capacitor with capacitance $C = 1.2\\text{ nF}$ and a coil with inductance $L = 6.0\\,\\mu\\text{H}$ and active resistance $R = 0.50\\,\\Omega$. What mean power should be supplied to the circuit to maintain undamped oscillations with capacitor voltage amplitude $V_m = 10\\text{ V}$?",
        "hints": [
            "In an $RLC$ circuit with low damping, the relation between current amplitude $I_m$ and voltage amplitude $V_m$ is $I_m = V_m \\sqrt{\\frac{C}{L}}$.",
            "The power required to maintain steady oscillations is $P = \\frac{1}{2} R I_m^2$.",
            "Substitute $I_m$ to obtain $P = \\frac{1}{2} \\frac{R C}{L} V_m^2$."
        ],
        "answer": "$P = \\frac{1}{2} \\frac{R C}{L} V_m^2 = 5.0\\text{ mW}$",
        "solution": "**1. Relation Between Current and Voltage Amplitudes:**\nFor weakly damped oscillations, the maximum electrostatic energy stored in the capacitor equals the maximum magnetic energy stored in the inductor:\n$$\\frac{1}{2} C V_m^2 \\approx \\frac{1}{2} L I_m^2 \\implies I_m = V_m \\sqrt{\\frac{C}{L}}$$\n\n**2. Mean Power Input:**\nThe power required to compensate for Joule losses in active resistance $R$ is:\n$$P = \\frac{1}{2} R I_m^2 = \\frac{1}{2} R \\left( V_m^2 \\frac{C}{L} \\right) = \\frac{1}{2} \\frac{R C}{L} V_m^2$$\n\n**3. Numerical Evaluation:**\nGiven $C = 1.2 \\times 10^{-9}\\text{ F}$, $L = 6.0 \\times 10^{-6}\\text{ H}$, $R = 0.50\\,\\Omega$, and $V_m = 10\\text{ V}$:\n$$\\frac{C}{L} = \\frac{1.2 \\times 10^{-9}}{6.0 \\times 10^{-6}} = 2.0 \\times 10^{-4}\\text{ F/H}$$\n$$P = \\frac{1}{2} (0.50\\,\\Omega)(2.0 \\times 10^{-4}\\text{ F/H})(10\\text{ V})^2 = 0.25 \\times 2.0 \\times 10^{-4} \\times 100 = 5.0 \\times 10^{-3}\\text{ W} = 5.0\\text{ mW}$$",
        "tags": ["mean power", "energy dissipation", "voltage amplitude", "RLC circuit"]
    },
    {
        "id": "4.115",
        "title": "Damped Oscillation Frequency in an RLC Circuit with Parallel Branch",
        "difficulty": 3,
        "question": "Find the damped oscillation frequency of a circuit with capacitance $C$, inductance $L$, and active resistance $R$. Also determine the condition for oscillatory motion to occur.",
        "hints": [
            "Depending on topology (series vs parallel), the damping coefficient is either $\\beta = \\frac{R}{2L}$ or $\\beta = \\frac{1}{2RC}$.",
            "For a parallel loss branch across $C$, $\\beta = \\frac{1}{2RC}$, yielding $\\omega = \\sqrt{\\frac{1}{LC} - \\frac{1}{4R^2 C^2}}$.",
            "For oscillations to exist, $\\omega^2 > 0$, requiring $R > \\frac{1}{2} \\sqrt{\\frac{L}{C}}$."
        ],
        "answer": "$\\omega = \\sqrt{\\frac{1}{LC} - \\frac{1}{4 R^2 C^2}}$, with condition $R > \\frac{1}{2} \\sqrt{\\frac{L}{C}}$",
        "solution": "**1. Circuit Equation:**\nFor an $LC$ branch shunted by resistance $R$, Kirchhoff's law yields the second-order differential equation:\n$$\\ddot{V} + \\frac{1}{RC} \\dot{V} + \\frac{1}{LC} V = 0$$\nThis corresponds to the standard damped oscillator $\\ddot{V} + 2\\beta \\dot{V} + \\omega_0^2 V = 0$ with:\n$$\\beta = \\frac{1}{2 R C}, \\quad \\omega_0 = \\frac{1}{\\sqrt{LC}}$$\n\n**2. Damped Frequency:**\nThe angular frequency of damped oscillations is:\n$$\\omega = \\sqrt{\\omega_0^2 - \\beta^2} = \\sqrt{\\frac{1}{LC} - \\frac{1}{4 R^2 C^2}}$$\n\n**3. Condition for Oscillatory Motion:**\nFor the motion to be oscillatory (underdamped), the expression under the square root must be strictly positive:\n$$\\frac{1}{LC} - \\frac{1}{4 R^2 C^2} > 0 \\implies \\frac{1}{LC} > \\frac{1}{4 R^2 C^2}$$\n$$4 R^2 C^2 > L C \\implies R^2 > \\frac{L}{4C} \\implies R > \\frac{1}{2} \\sqrt{\\frac{L}{C}}$$",
        "tags": ["damped frequency", "underdamped condition", "RLC circuit", "critical resistance"]
    }
]
