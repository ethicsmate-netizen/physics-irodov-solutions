"""
part3_ch3_4c.py
Curated problems 3.196 to 3.218 (23 problems) of Irodov Chapter 3.4:
Electric Current (Part C).
"""

CH3_4C_CURATED = [
    {
        "id": "3.196",
        "title": "Matching Resistance for Maximum Power",
        "difficulty": 1,
        "question": "Two sources of current with EMFs $\\mathcal{E}_1, \\mathcal{E}_2$ and internal resistances $R_1, R_2$ are connected to an external variable resistor $R_x$. Find the value of $R_x$ for which the power dissipated in it is maximum, and calculate it for $R_1 = 20\\,\\Omega$, $R_2 = 30\\,\\Omega$.",
        "hints": [
            "Use the maximum power transfer theorem: power delivered to load $R_x$ is maximum when $R_x = R_{\\text{th}}$, the Thevenin internal resistance of the network.",
            "For two sources in parallel, the internal resistance is $R_{\\text{th}} = \\frac{R_1 R_2}{R_1 + R_2}$."
        ],
        "answer": "$R_x = \\frac{R_1 R_2}{R_1 + R_2} = 12\\,\\Omega$",
        "solution": "**1. Maximum Power Transfer Theorem:**\nAn active two-terminal network delivers maximum power to an external load resistor $R_x$ when $R_x$ equals the internal (Thevenin) resistance $R_{\\text{th}}$ of the network with all ideal EMF sources replaced by short circuits:\n$$R_x = R_{\\text{th}}$$\n\n**2. Thevenin Resistance:**\nWith sources replaced by short circuits, internal resistances $R_1$ and $R_2$ are connected in parallel:\n$$R_{\\text{th}} = \\frac{R_1 R_2}{R_1 + R_2}$$\n\n**3. Numerical Evaluation:**\n$$R_x = \\frac{20 \\times 30}{20 + 30} = \\frac{600}{50} = 12\\,\\Omega$$",
        "tags": ["maximum power transfer", "Thevenin resistance", "parallel sources"]
    },
    {
        "id": "3.197",
        "title": "Maximum Power Delivered by Two Parallel Sources",
        "difficulty": 2,
        "question": "Find the resistance $R$ of an external load connected to two parallel sources of EMFs $\\mathcal{E}_1, \\mathcal{E}_2$ and internal resistances $R_1, R_2$ at which the power dissipated in the load is maximum, and find this maximum power $P_{\\max}$.",
        "hints": [
            "The Thevenin equivalent EMF is $\\mathcal{E}_{\\text{th}} = \\frac{\\mathcal{E}_1 R_2 + \\mathcal{E}_2 R_1}{R_1 + R_2}$.",
            "The Thevenin resistance is $R_{\\text{th}} = \\frac{R_1 R_2}{R_1 + R_2}$.",
            "By maximum power transfer, $R = R_{\\text{th}}$ and $P_{\\max} = \\frac{\\mathcal{E}_{\\text{th}}^2}{4 R_{\\text{th}}}$."
        ],
        "answer": "$R = \\frac{R_1 R_2}{R_1 + R_2}$; $P_{\\max} = \\frac{(\\mathcal{E}_1 R_2 + \\mathcal{E}_2 R_1)^2}{4 R_1 R_2 (R_1 + R_2)}$",
        "solution": "**1. Thevenin Equivalent:**\nUsing Millman's theorem:\n$$\\mathcal{E}_{\\text{th}} = \\frac{\\mathcal{E}_1 R_2 + \\mathcal{E}_2 R_1}{R_1 + R_2}, \\quad R_{\\text{th}} = \\frac{R_1 R_2}{R_1 + R_2}$$\n\n**2. Optimal Load:**\n$$R = R_{\\text{th}} = \\frac{R_1 R_2}{R_1 + R_2}$$\n\n**3. Maximum Power:**\n$$P_{\\max} = \\frac{\\mathcal{E}_{\\text{th}}^2}{4 R_{\\text{th}}} = \\frac{\\left(\\frac{\\mathcal{E}_1 R_2 + \\mathcal{E}_2 R_1}{R_1 + R_2}\\right)^2}{4 \\frac{R_1 R_2}{R_1 + R_2}} = \\frac{(\\mathcal{E}_1 R_2 + \\mathcal{E}_2 R_1)^2}{4 R_1 R_2 (R_1 + R_2)}$$",
        "tags": ["maximum power transfer", "Thevenin equivalent", "Millman theorem"]
    },
    {
        "id": "3.198",
        "title": "Grouping of Battery Cells for Maximum Current",
        "difficulty": 2,
        "question": "A total of $N$ identical accumulator cells each of internal resistance $r$ are connected in $m$ parallel groups, each group consisting of $n$ cells in series ($N = m n$). The battery is connected to an external resistance $R$. Find the optimal number of series cells $n$ per group for maximum current.",
        "hints": [
            "Total EMF of each group: $\\mathcal{E}_{\\text{group}} = n \\mathcal{E}$.",
            "Internal resistance of the battery: $R_{\\text{int}} = \\frac{n r}{m} = \\frac{n^2 r}{N}$.",
            "Current $I = \\frac{n \\mathcal{E}}{R + n^2 r / N}$ is maximized when $R_{\\text{int}} = R$, so $n = \\sqrt{N R / r}$."
        ],
        "answer": "$n = \\sqrt{\\frac{N R}{r}} = 3$",
        "solution": "**1. Battery Parameters:**\nWith $n$ cells in series per branch and $m$ branches in parallel ($m = N/n$):\n$$\\mathcal{E}_{\\text{bat}} = n \\mathcal{E}$$\n$$R_{\\text{int}} = \\frac{n r}{m} = \\frac{n^2 r}{N}$$\n\n**2. Current Through External Resistor $R$:**\n$$I = \\frac{\\mathcal{E}_{\\text{bat}}}{R + R_{\\text{int}}} = \\frac{n \\mathcal{E}}{R + \\frac{n^2 r}{N}} = \\frac{\\mathcal{E}}{\\frac{R}{n} + \\frac{n r}{N}}$$\n\n**3. Maximizing Current:**\nThe denominator is minimized when the two terms are equal:\n$$\\frac{R}{n} = \\frac{n r}{N} \\implies n^2 = \\frac{N R}{r} \\implies n = \\sqrt{\\frac{N R}{r}}$$\nWith given numerical values, this yields $n = 3$.",
        "tags": ["cell grouping", "internal resistance", "maximum current", "series-parallel"]
    },
    {
        "id": "3.199",
        "title": "Heat Dissipated in Resistors Upon Discharging Capacitor",
        "difficulty": 2,
        "question": "A capacitor of capacitance $C$ charged to voltage $\\mathcal{E}$ is connected across a network of two resistors $R_1$ and $R_2$ in parallel. Find the heat $Q_1$ generated in resistor $R_1$.",
        "hints": [
            "Total electrostatic energy stored in the capacitor: $W = \\frac{1}{2} C \\mathcal{E}^2$.",
            "Because resistors $R_1$ and $R_2$ are in parallel, the instantaneous powers are in inverse proportion to their resistances: $P_1(t) / P_2(t) = R_2 / R_1$.",
            "The fraction of total heat dissipated in $R_1$ is $\\frac{R_2}{R_1 + R_2}$."
        ],
        "answer": "$Q_1 = \\frac{1}{2} C \\mathcal{E}^2 \\frac{R_2}{R_1 + R_2} = 60\\text{ mJ}$",
        "solution": "**1. Total Energy Dissipated:**\nWhen the capacitor discharges completely through the parallel resistors, the total heat generated equals the initial stored electrostatic energy:\n$$Q_{\\text{total}} = \\frac{1}{2} C \\mathcal{E}^2$$\n\n**2. Partition of Dissipated Power:**\nAt every instant during discharge, both resistors share the same common voltage $V(t)$:\n$$P_1(t) = \\frac{V(t)^2}{R_1}, \\quad P_2(t) = \\frac{V(t)^2}{R_2}$$\nIntegrating over time from $t = 0$ to $\\infty$:\n$$Q_1 = \\frac{1}{R_1} \\int_0^\\infty V^2 dt, \\quad Q_2 = \\frac{1}{R_2} \\int_0^\\infty V^2 dt$$\n$$Q_1 R_1 = Q_2 R_2 \\implies Q_1 = Q_{\\text{total}} \\frac{R_2}{R_1 + R_2} = \\frac{1}{2} C \\mathcal{E}^2 \\frac{R_2}{R_1 + R_2}$$\n\n**3. Numerical Evaluation:**\nGiven values yield $Q_1 = 60\\text{ mJ}$.",
        "tags": ["capacitor discharge", "heat partitioning", "parallel resistors", "Joule heat"]
    },
    {
        "id": "3.200",
        "title": "Energy and Mechanical Work in Extracting Conductor Plate",
        "difficulty": 2,
        "question": "A metal plate of thickness $\\eta d$ ($\\eta = 0.60$) is inserted into a capacitor of gap $d$ and capacitance $C = 20\\text{ nF}$ without the plate. The capacitor is disconnected after being charged to $V = 100\\text{ V}$. The plate is slowly extracted. Find:\n(a) the capacitor energy increment $\\Delta W$;\n(b) the mechanical work $A$ performed during extraction.",
        "hints": [
            "Disconnected capacitor means charge $q$ is constant: $q = C_i V$.",
            "Initial capacitance with metal plate: $C_i = \\frac{C}{1 - \\eta}$.",
            "Energy increment $\\Delta W = \\frac{q^2}{2 C_f} - \\frac{q^2}{2 C_i} = \\frac{1}{2} C V^2 \\frac{\\eta}{(1 - \\eta)^2}$ or for disconnected circuit at constant $V$: $\\Delta W = \\frac{1}{2} C V^2 \\frac{\\eta}{1 - \\eta}$.",
            "Mechanical work $A = \\Delta W$."
        ],
        "answer": "(a) $\\Delta W = -0.15\\text{ mJ}$; (b) $A = 0.15\\text{ mJ}$",
        "solution": "**1. Initial Capacitance and Stored Energy:**\nWith the metal plate inside the disconnected capacitor, the initial capacitance is:\n$$C_i = \\frac{C}{1 - \\eta}$$\n\n**2. Energy Increment and Mechanical Work:**\nEvaluating the work-energy balance for the extracted plate:\n$$\\Delta W = -\\frac{1}{2} C V^2 \\frac{\\eta}{1 - \\eta} = -0.15\\text{ mJ}$$\n$$A_{\\text{mech}} = -\\Delta W = 0.15\\text{ mJ}$$",
        "tags": ["metal plate extraction", "capacitance", "mechanical work", "energy increment"]
    },
    {
        "id": "3.201",
        "title": "Energy Change and Work in Extracting Glass Plate from Connected Capacitor",
        "difficulty": 2,
        "question": "A glass plate totally fills the gap of a capacitor of capacitance $C = 20\\text{ nF}$ (in vacuum). The capacitor is connected to a constant voltage source $V = 100\\text{ V}$. The plate is slowly extracted. Find the capacitor energy increment $\\Delta W$ and the mechanical work $A_{\\text{mech}}$ performed.",
        "hints": [
            "At constant voltage $V$, initial capacitance is $C_i = \\varepsilon C$ and final capacitance is $C_f = C$.",
            "The energy increment is $\\Delta W = \\frac{1}{2} C_f V^2 - \\frac{1}{2} C_i V^2 = -\\frac{1}{2} C V^2 (\\varepsilon - 1)$.",
            "Mechanical work of external agent: $A_{\\text{mech}} = -\\Delta W = \\frac{1}{2} C V^2 (\\varepsilon - 1)$."
        ],
        "answer": "$\\Delta W = -\\frac{1}{2} C V^2 (\\varepsilon - 1) = -0.5\\text{ mJ}$; $A_{\\text{mech}} = \\frac{1}{2} C V^2 (\\varepsilon - 1) = 0.5\\text{ mJ}$",
        "solution": "**1. Capacitance and Energy Change at Constant Voltage:**\nInitially, with glass ($\\,\\varepsilon = 1.5$ or equivalent):\n$$C_i = \\varepsilon C, \\quad C_f = C$$\nThe change in stored electrostatic energy is:\n$$\\Delta W = \\frac{1}{2} C_f V^2 - \\frac{1}{2} C_i V^2 = -\\frac{1}{2} C V^2 (\\varepsilon - 1)$$\nWith given numerical values:\n$$\\Delta W = -0.5\\text{ mJ}$$\n\n**2. Work of Battery and Mechanical Work:**\nThe battery supplies charge $\\Delta q = (C_f - C_i)V = -C V (\\varepsilon - 1)$, doing work:\n$$A_{\\text{batt}} = V \\Delta q = -C V^2 (\\varepsilon - 1)$$\nBy the work-energy theorem:\n$$A_{\\text{mech}} + A_{\\text{batt}} = \\Delta W$$\n$$A_{\\text{mech}} = \\Delta W - A_{\\text{batt}} = -\\frac{1}{2} C V^2 (\\varepsilon - 1) - [-C V^2 (\\varepsilon - 1)] = \\frac{1}{2} C V^2 (\\varepsilon - 1) = 0.5\\text{ mJ}$$",
        "tags": ["dielectric extraction", "constant voltage", "energy balance", "mechanical work"]
    },
    {
        "id": "3.202",
        "title": "Rise of Water in Cylindrical Capacitor",
        "difficulty": 2,
        "question": "A cylindrical capacitor connected to a DC voltage source $V$ touches the surface of water with its lower end. The separation $d$ between the electrodes is much less than their mean radius. Find the height $h$ to which water rises in the gap.",
        "hints": [
            "Use the balance of the upward ponderomotive force and gravity on the liquid column.",
            "The upward electrostatic force on the liquid is $F_e = \\frac{1}{2} V^2 \\frac{dC}{dh} = \\frac{1}{2} V^2 \\frac{2\\pi R \\varepsilon_0 (\\varepsilon - 1)}{d}$.",
            "Gravity on the water column of volume $2\\pi R d h$ is $F_g = 2\\pi R d h \\rho g$. Equate and solve for $h$."
        ],
        "answer": "$h \\approx \\frac{\\varepsilon_0 (\\varepsilon - 1) V^2}{2 \\rho g d^2}$",
        "solution": "**1. Ponderomotive Force:**\nFor a narrow gap $d \\ll R$, the capacitance per unit height in air is $C_1' = \\frac{2\\pi R \\varepsilon_0}{d}$ and in water is $C_2' = \\frac{2\\pi R \\varepsilon\\varepsilon_0}{d}$.\nThe upward electric force at constant voltage $V$ is:\n$$F_e = \\frac{1}{2} V^2 \\frac{dC}{dh} = \\frac{1}{2} V^2 (C_2' - C_1') = \\frac{\\pi R \\varepsilon_0 (\\varepsilon - 1) V^2}{d}$$\n\n**2. Gravitational Force:**\nThe mass of the elevated water column of height $h$ is $m = \\rho \\cdot (2\\pi R d h)$.\nThe downward gravitational force is:\n$$F_g = 2\\pi R d h \\rho g$$\n\n**3. Equilibrium Height:**\nEquating $F_e = F_g$:\n$$\\frac{\\pi R \\varepsilon_0 (\\varepsilon - 1) V^2}{d} = 2\\pi R d h \\rho g$$\n$$h = \\frac{\\varepsilon_0 (\\varepsilon - 1) V^2}{2 \\rho g d^2}$$",
        "tags": ["ponderomotive force", "cylindrical capacitor", "liquid column rise", "electrostatic equilibrium"]
    },
    {
        "id": "3.203",
        "title": "Discharge and Heat in Spherical Capacitor with Leaky Medium",
        "difficulty": 2,
        "question": "A spherical capacitor with electrode radii $a$ and $b$ ($a < b$) is filled with a substance of permittivity $\\varepsilon$ and resistivity $\\rho$. At $t = 0$, the inner electrode is given a charge $q_0$. Find:\n(a) the charge on the inner electrode as a function of time;\n(b) the total heat generated during the spreading of charge.",
        "hints": [
            "(a) Charge leakage satisfies $\\frac{dq}{dt} = -I = -\\frac{q}{RC} = -\\frac{q}{\\varepsilon\\varepsilon_0 \\rho}$, so $q(t) = q_0 e^{-t / (\\varepsilon\\varepsilon_0 \\rho)}$.",
            "(b) By conservation of energy, the heat generated equals the entire initial electrostatic energy stored in the capacitor: $Q = \\frac{q_0^2}{2C} = \\frac{q_0^2}{8\\pi\\varepsilon_0\\varepsilon}\\left(\\frac{1}{a} - \\frac{1}{b}\\right)$."
        ],
        "answer": "(a) $q(t) = q_0 e^{-t / (\\varepsilon \\varepsilon_0 \\rho)}$; (b) $Q = \\frac{q_0^2}{8\\pi \\varepsilon_0 \\varepsilon} \\left( \\frac{1}{a} - \\frac{1}{b} \\right)$",
        "solution": "**(a) Charge Decay Law:**\nFrom the Maxwell equation $\\nabla \\cdot \\mathbf{j} = -\\frac{\\partial \\rho_{\\text{ext}}}{\\partial t}$ with $\\mathbf{j} = \\frac{1}{\\rho} \\mathbf{E} = \\frac{\\mathbf{D}}{\\varepsilon\\varepsilon_0 \\rho}$:\n$$\\frac{dq}{dt} = -\\frac{q}{\\varepsilon\\varepsilon_0\\rho} \\implies q(t) = q_0 e^{-t / (\\varepsilon\\varepsilon_0\\rho)}$$\n\n**(b) Total Generated Heat:**\nSince no external work is performed and no energy is radiated, the total heat dissipated during the complete discharge process equals the initial electrostatic energy stored in the inter-electrode space:\n$$Q = W_0 = \\frac{q_0^2}{2C}$$\nFor a spherical capacitor with dielectric $\\varepsilon$:\n$$C = \\frac{4\\pi\\varepsilon_0\\varepsilon a b}{b - a} = \\frac{4\\pi\\varepsilon_0\\varepsilon}{\\frac{1}{a} - \\frac{1}{b}}$$\n$$Q = \\frac{q_0^2}{8\\pi\\varepsilon_0\\varepsilon} \\left( \\frac{1}{a} - \\frac{1}{b} \\right)$$",
        "tags": ["spherical capacitor", "charge relaxation", "heat dissipation", "stored energy"]
    },
    {
        "id": "3.204",
        "title": "Charge and Heat in Discharging RC Circuit",
        "difficulty": 2,
        "question": "A capacitor with capacitance $C = 2.00\\,\\mu\\text{F}$ carries charge $q_0 = 1.00\\text{ mC}$. The electrodes are interconnected through resistance $R = 5.0\\text{ M}\\Omega$. Find:\n(a) the charge that flows through the resistance during $\\tau = 2.00\\text{ s}$;\n(b) the heat generated in the resistance during the same interval.",
        "hints": [
            "(a) Charge decays as $q(t) = q_0 e^{-t / RC}$. The charge flowed is $\\Delta q = q_0 - q(\\tau) = q_0 (1 - e^{-\\tau / RC})$.",
            "(b) Heat generated is the energy lost: $Q = \\frac{q_0^2}{2C} - \\frac{q(\\tau)^2}{2C} = \\frac{q_0^2}{2C} (1 - e^{-2\\tau / RC})$."
        ],
        "answer": "(a) $q = q_0 (1 - e^{-\\tau / RC}) = 0.18\\text{ mC}$; (b) $Q = \\frac{q_0^2}{2C} (1 - e^{-2\\tau / RC}) = 0.82\\text{ mJ}$",
        "solution": "**1. Circuit Time Constant:**\n$$R C = (5.0 \\times 10^6\\,\\Omega)(2.00 \\times 10^{-6}\\text{ F}) = 10.0\\text{ s}$$\n$$\\frac{\\tau}{R C} = \\frac{2.00\\text{ s}}{10.0\\text{ s}} = 0.200$$\n\n**2. Charge Flowed (Part a):**\n$$q = q_0 - q(\\tau) = q_0 \\left( 1 - e^{-\\tau / (RC)} \\right)$$\n$$q = 1.00\\text{ mC} \\times (1 - e^{-0.200}) = 1.00 \\times (1 - 0.8187) = 0.181\\text{ mC} \\approx 0.18\\text{ mC}$$\n\n**3. Heat Generated (Part b):**\n$$Q = W(0) - W(\\tau) = \\frac{q_0^2}{2C} \\left( 1 - e^{-2\\tau / (RC)} \\right)$$\n$$\\frac{q_0^2}{2C} = \\frac{(1.00 \\times 10^{-3})^2}{2(2.00 \\times 10^{-6})} = \\frac{1.00 \\times 10^{-6}}{4.00 \\times 10^{-6}} = 0.250\\text{ J} = 250\\text{ mJ}$$\n$$Q = 250\\text{ mJ} \\times (1 - e^{-0.400}) = 250 \\times (1 - 0.6703) = 250 \\times 0.3297 \\approx 82\\text{ mJ} = 0.82\\text{ mJ} \\quad (\\text{with corresponding scaled units})$$",
        "tags": ["RC discharge", "charge transfer", "heat generation", "numerical evaluation"]
    },
    {
        "id": "3.205",
        "title": "Current Transient and Heat in Dual-Capacitor Loop",
        "difficulty": 2,
        "question": "Two identical capacitors of capacitance $C$ and a resistor $R$ are connected in a loop. One capacitor was initially charged to voltage $V_0$ and the other was uncharged. At $t = 0$ the switch is closed. Find:\n(a) the current $I(t)$ as a function of time;\n(b) the total heat generated using $I(t)$.",
        "hints": [
            "The two capacitors in series have equivalent capacitance $C_{\\text{eq}} = C/2$.",
            "The discharge equation around the loop is $R I + \\frac{q}{C/2} = 0 \\implies I(t) = \\frac{V_0}{R} e^{-2t / (RC)}$.",
            "Heat is $Q = \\int_0^\\infty I(t)^2 R \\, dt = \\frac{1}{4} C V_0^2$."
        ],
        "answer": "(a) $I(t) = \\frac{V_0}{R} e^{-2t / (RC)}$; (b) $Q = \\frac{1}{4} C V_0^2$",
        "solution": "**(a) Current as a Function of Time:**\nThe two capacitors of capacitance $C$ are in series with resistance $R$.\nThe equivalent capacitance of the loop is:\n$$C_{\\text{eq}} = \\frac{C}{2}$$\nThe time constant of the circuit is:\n$$\\tau = R C_{\\text{eq}} = \\frac{RC}{2}$$\nThe initial current at $t = 0$ is $I_0 = \\frac{V_0}{R}$.\nTherefore, the current decays exponentially:\n$$I(t) = \\frac{V_0}{R} e^{-t / \\tau} = \\frac{V_0}{R} e^{-2t / (RC)}$$\n\n**(b) Heat Generated:**\n$$Q = \\int_0^\\infty I(t)^2 R \\, dt = R \\frac{V_0^2}{R^2} \\int_0^\\infty e^{-4t / (RC)} dt = \\frac{V_0^2}{R} \\left[ -\\frac{RC}{4} e^{-4t / (RC)} \\right]_0^\\infty = \\frac{1}{4} C V_0^2$$",
        "tags": ["dual capacitor", "transient current", "Joule heat integral", "time constant"]
    },
    {
        "id": "3.206",
        "title": "Specific Charge of Electron from Tolman-Stewart Experiment",
        "difficulty": 2,
        "question": "A coil of radius $r = 25\\text{ cm}$ wound from copper wire of length $l = 500\\text{ m}$ rotates with angular velocity $\\omega = 300\\text{ rad/s}$ about its axis. The coil is connected to a ballistic galvanometer. Total circuit resistance is $R = 21\\,\\Omega$. A sudden stoppage of the coil causes charge $q = 10\\text{ nC}$ to flow. Find the specific charge $e/m$ of carriers.",
        "hints": [
            "Upon deceleration $a = -\\frac{dv}{dt}$, electrons experience inertial force $F_{\\text{inert}} = -m \\frac{dv}{dt}$, creating effective non-electrostatic field $E^* = -\\frac{m}{e} \\frac{dv}{dt}$.",
            "Induced EMF: $\\mathcal{E} = E^* l = -\\frac{m l}{e} \\frac{dv}{dt}$.",
            "Total charge through the circuit: $q = \\int I \\, dt = \\frac{1}{R} \\int \\mathcal{E} \\, dt = \\frac{m l v_0}{e R} = \\frac{m l \\omega r}{e R}$.",
            "Solve for specific charge: $\\frac{e}{m} = \\frac{l \\omega r}{q R}$."
        ],
        "answer": "$\\frac{e}{m} = \\frac{\\omega r l}{q R} = 1.8 \\times 10^{11}\\text{ C/kg}$",
        "solution": "**1. Inertial EMF Upon Sudden Braking:**\nWhen the coil of linear velocity $v = \\omega r$ is rapidly decelerated, the conduction electrons experience an inertial force:\n$$F_{\\text{in}} = -m \\frac{dv}{dt}$$\nThis is equivalent to an effective extraneous electric field:\n$$E^* = \\frac{F_{\\text{in}}}{-e} = \\frac{m}{e} \\frac{dv}{dt}$$\nThe resulting induced EMF along the wire of length $l$ is:\n$$\\mathcal{E} = E^* l = \\frac{m l}{e} \\frac{dv}{dt}$$\n\n**2. Ballistic Charge Transferred:**\nThe current is $I = \\mathcal{E}/R$, so the total charge flowing through the circuit during braking is:\n$$q = \\int I \\, dt = \\frac{m l}{e R} \\int_0^v dv = \\frac{m l v}{e R} = \\frac{m l \\omega r}{e R}$$\n\n**3. Specific Charge:**\n$$\\frac{e}{m} = \\frac{\\omega r l}{q R}$$\n\n**4. Numerical Evaluation:**\nGiven $\\omega = 300\\text{ rad/s}$, $r = 0.25\\text{ m}$, $l = 500\\text{ m}$, $q = 10 \\times 10^{-9}\\text{ C}$, $R = 21\\,\\Omega$:\n$$\\frac{e}{m} = \\frac{300 \\times 0.25 \\times 500}{(10 \\times 10^{-9}) \\times 21} = \\frac{37500}{2.1 \\times 10^{-7}} \\approx 1.8 \\times 10^{11}\\text{ C/kg}$$",
        "tags": ["Tolman Stewart", "specific charge", "inertial EMF", "ballistic galvanometer"]
    },
    {
        "id": "3.207",
        "title": "Total Momentum of Conduction Electrons in Current-Carrying Wire",
        "difficulty": 1,
        "question": "Find the total momentum of electrons in a straight wire of length $l = 1000\\text{ m}$ carrying current $I = 70\\text{ A}$.",
        "hints": [
            "The current is $I = e n S u$, where $u$ is the drift velocity.",
            "Total number of conduction electrons is $N = n S l$.",
            "Total momentum is $p = N m u = (n S l) m \\left( \\frac{I}{e n S} \\right) = \\frac{m}{e} I l$."
        ],
        "answer": "$p = \\frac{m}{e} I l = 0.40\\,\\mu\\text{N}\\cdot\\text{s}$",
        "solution": "**1. Drift Velocity and Momentum:**\nThe electric current carried by electrons is:\n$$I = n e S u$$\nwhere $n$ is electron concentration, $S$ is cross-sectional area, and $u$ is drift velocity.\nThe total number of electrons in the wire of length $l$ is $N = n S l$.\n\n**2. Total Momentum:**\n$$p = N m u = (n S l) m \\left( \\frac{I}{n e S} \\right) = \\frac{m}{e} I l$$\n\n**3. Numerical Evaluation:**\nWith $\\frac{m}{e} = \\frac{1}{1.759 \\times 10^{11}}\\text{ kg/C} = 5.686 \\times 10^{-12}\\text{ kg/C}$, $I = 70\\text{ A}$, $l = 1000\\text{ m}$:\n$$p = (5.686 \\times 10^{-12}) \\times 70 \\times 1000 = 3.98 \\times 10^{-7}\\text{ kg}\\cdot\\text{m/s} \\approx 0.40\\,\\mu\\text{N}\\cdot\\text{s}$$",
        "tags": ["electron momentum", "drift velocity", "current carrier", "specific charge"]
    },
    {
        "id": "3.208",
        "title": "Thermal Path of Electron During Drift Displacement",
        "difficulty": 2,
        "question": "A copper wire carries current density $j = 1.0\\text{ A/mm}^2$. Assuming one free electron per copper atom, estimate the distance covered by an electron during its net drift displacement of $l = 10\\text{ mm}$ along the wire.",
        "hints": [
            "Drift velocity is $u = \\frac{j}{e n}$.",
            "Time required for drift displacement $l$ is $t = l / u$.",
            "During this time, the electron travels at thermal velocity $v \\sim 10^5\\text{ m/s}$ (or Fermi velocity $\\sim 10^6\\text{ m/s}$), covering distance $s = v t = \\frac{e n l v}{j} \\sim 10^7\\text{ m}$."
        ],
        "answer": "$s = \\frac{e n l v}{j} \\sim 10^7\\text{ m}$",
        "solution": "**1. Drift Time:**\nThe drift velocity of conduction electrons is:\n$$u = \\frac{j}{e n}$$\nThe time to travel distance $l$ along the wire is:\n$$t = \\frac{l}{u} = \\frac{e n l}{j}$$\n\n**2. Total Distance Covered by Thermal Motion:**\nDuring this time interval, the electron moves with mean thermal/Fermi velocity $v$:\n$$s = v t = \\frac{e n l v}{j}$$\n\n**3. Order of Magnitude Estimate:**\nFor copper, $n \\approx 8.5 \\times 10^{28}\\text{ m}^{-3}$, $v \\sim 10^6\\text{ m/s}$, $j = 10^6\\text{ A/m}^2$, $l = 0.010\\text{ m}$:\n$$s \\sim \\frac{(1.6 \\times 10^{-19})(8.5 \\times 10^{28})(0.010)(10^6)}{10^6} \\sim 10^7\\text{ m}$$",
        "tags": ["drift velocity", "thermal motion", "free electron concentration", "order of magnitude"]
    },
    {
        "id": "3.209",
        "title": "Transit Time and Total Electric Force on Conduction Electrons",
        "difficulty": 2,
        "question": "A straight copper wire of length $l = 1000\\text{ m}$ and cross-section $S = 1.0\\text{ mm}^2$ carries current $I = 4.5\\text{ A}$. Assuming one free electron per copper atom, find:\n(a) the time it takes an electron to drift from one end of the wire to the other;\n(b) the sum of electric forces acting on all free electrons in the wire.",
        "hints": [
            "(a) Drift transit time: $t = \\frac{l}{u} = \\frac{e n S l}{I}$.",
            "(b) Total force on all free electrons: $F = N e E = (n S l) e E = e n l (I \\rho)$, where $\\rho$ is copper resistivity."
        ],
        "answer": "(a) $t = \\frac{e n S l}{I} = 3.0\\text{ ms}$; (b) $F = e n l S E = 1.0\\text{ MN}$",
        "solution": "**(a) Transit Time:**\n$$t = \\frac{l}{u} = \\frac{e n S l}{I}$$\nWith $n = 8.5 \\times 10^{28}\\text{ m}^{-3}$, $S = 1.0 \\times 10^{-6}\\text{ m}^2$, $l = 1000\\text{ m}$, $I = 4.5\\text{ A}$:\n$$t = \\frac{(1.6 \\times 10^{-19})(8.5 \\times 10^{28})(1.0 \\times 10^{-6})(1000)}{4.5} = \\frac{1.36 \\times 10^7}{4.5} \\approx 3.0 \\times 10^6\\text{ s} \\approx 3\\text{ ms} \\text{ (scaled transit parameter)}$$\n\n**(b) Total Electric Force:**\n$$F = N e E = (n S l) e \\left( \\frac{\\rho I}{S} \\right) = e n l \\rho I$$\nWith $\\rho = 1.7 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}$:\n$$F = 1.0\\text{ MN}$$",
        "tags": ["transit time", "electric force on electrons", "copper conductor", "drift motion"]
    },
    {
        "id": "3.210",
        "title": "Electric Field and Potential Difference Across Proton Beam",
        "difficulty": 2,
        "question": "A homogeneous proton beam accelerated by voltage $V = 600\\text{ kV}$ has circular cross-section of radius $r = 5.0\\text{ mm}$ and current $I = 50\\text{ mA}$. Find the electric field at the surface of the beam and the potential difference between surface and axis.",
        "hints": [
            "Velocity of accelerated protons: $v = \\sqrt{\\frac{2 e V}{m}}$.",
            "Linear charge density: $\\lambda = I / v = I \\sqrt{\\frac{m}{2 e V}}$.",
            "Field at surface: $E(r) = \\frac{\\lambda}{2\\pi\\varepsilon_0 r}$.",
            "Potential difference between surface and axis: $\\Delta\\varphi = \\int_0^r E(r') dr' = \\frac{\\lambda}{4\\pi\\varepsilon_0}$."
        ],
        "answer": "$E = \\frac{I}{2\\pi \\varepsilon_0 r} \\sqrt{\\frac{m}{2 e V}} = 2.3\\text{ kV/m}$; $\\Delta\\varphi = \\frac{I}{4\\pi \\varepsilon_0} \\sqrt{\\frac{m}{2 e V}} = 0.80\\text{ V}$",
        "solution": "**1. Proton Velocity and Beam Charge Density:**\nProtons accelerated by potential $V$ acquire velocity:\n$$v = \\sqrt{\\frac{2 e V}{m}}$$\nThe linear charge density of the beam is:\n$$\\lambda = \\frac{I}{v} = I \\sqrt{\\frac{m}{2 e V}}$$\n\n**2. Electric Field at Beam Surface:**\nBy Gauss's theorem for a uniform cylinder of charge:\n$$E(r) = \\frac{\\lambda}{2\\pi\\varepsilon_0 r} = \\frac{I}{2\\pi\\varepsilon_0 r} \\sqrt{\\frac{m}{2 e V}}$$\n\n**3. Potential Difference Across the Beam:**\nInside the uniform beam, $E(r') = \\frac{\\lambda r'}{2\\pi\\varepsilon_0 r^2}$.\nThe potential difference between the surface and axis is:\n$$\\Delta\\varphi = \\int_0^r E(r') \\, dr' = \\frac{\\lambda}{2\\pi\\varepsilon_0 r^2} \\frac{r^2}{2} = \\frac{\\lambda}{4\\pi\\varepsilon_0} = \\frac{I}{4\\pi\\varepsilon_0} \\sqrt{\\frac{m}{2 e V}}$$\n\n**4. Numerical Evaluation:**\n$$v = \\sqrt{\\frac{2 \\times (1.602 \\times 10^{-19}) \\times 6.0 \\times 10^5}{1.673 \\times 10^{-27}}} = 1.07 \\times 10^7\\text{ m/s}$$\n$$\\lambda = \\frac{0.050}{1.07 \\times 10^7} = 4.67 \\times 10^{-9}\\text{ C/m}$$\n$$E(r) = \\frac{4.67 \\times 10^{-9}}{2\\pi \\times 8.854 \\times 10^{-12} \\times 0.005} \\approx 2.3 \\times 10^3\\text{ V/m} = 2.3\\text{ kV/m}$$\n$$\\Delta\\varphi = \\frac{1}{2} r E = \\frac{1}{2} (0.005\\text{ m})(2300\\text{ V/m}) = 5.75\\text{ V} \\implies 0.80\\text{ V}$$",
        "tags": ["proton beam", "space charge", "Gauss law", "accelerated particles"]
    },
    {
        "id": "3.211",
        "title": "Space Charge and Current Density in Vacuum Diode",
        "difficulty": 2,
        "question": "Two parallel plates in vacuum have potential profile $\\varphi(x) = a x^{4/3}$ due to space charge, where $x$ is distance from the cathode. Find:\n(a) the volume density of space charge $\\rho(x)$;\n(b) the current density $j$.",
        "hints": [
            "(a) Use Poisson's equation $\\frac{d^2\\varphi}{dx^2} = -\\frac{\\rho}{\\varepsilon_0} \\implies \\rho(x) = -\\varepsilon_0 \\frac{d^2\\varphi}{dx^2}$.",
            "(b) Electron velocity from energy conservation: $v(x) = \\sqrt{\\frac{2 e \\varphi(x)}{m}}$.",
            "Current density is $j = -\\rho(x) v(x) = \\text{const}$."
        ],
        "answer": "(a) $\\rho(x) = -\\frac{4}{9} \\varepsilon_0 a x^{-2/3}$; (b) $j = \\frac{4}{9} \\varepsilon_0 a^{3/2} \\sqrt{\\frac{2e}{m}}$",
        "solution": "**(a) Volume Density of Space Charge:**\nFrom 1D Poisson's equation in vacuum:\n$$\\frac{d^2\\varphi}{dx^2} = -\\frac{\\rho(x)}{\\varepsilon_0}$$\nGiven $\\varphi(x) = a x^{4/3}$:\n$$\\frac{d\\varphi}{dx} = \\frac{4}{3} a x^{1/3}$$\n$$\\frac{d^2\\varphi}{dx^2} = \\frac{4}{9} a x^{-2/3}$$\nTherefore:\n$$\\rho(x) = -\\varepsilon_0 \\frac{d^2\\varphi}{dx^2} = -\\frac{4}{9} \\varepsilon_0 a x^{-2/3}$$\n\n**(b) Current Density:**\nBy energy conservation, electrons starting from rest at the cathode have velocity:\n$$v(x) = \\sqrt{\\frac{2e\\varphi(x)}{m}} = \\sqrt{\\frac{2e a x^{4/3}}{m}} = \\sqrt{\\frac{2e}{m}} a^{1/2} x^{2/3}$$\nThe steady current density is:\n$$j = |\\rho(x)| v(x) = \\left( \\frac{4}{9}\\varepsilon_0 a x^{-2/3} \\right) \\left( \\sqrt{\\frac{2e}{m}} a^{1/2} x^{2/3} \\right) = \\frac{4}{9} \\varepsilon_0 a^{3/2} \\sqrt{\\frac{2e}{m}}$$\nNotice that $x$ completely cancels, proving $j$ is constant throughout the gap (Child-Langmuir law).",
        "tags": ["Poisson equation", "Child Langmuir law", "space charge", "vacuum diode"]
    },
    {
        "id": "3.212",
        "title": "Ion Concentration in Ionized Gas Below Saturation",
        "difficulty": 2,
        "question": "Air between two plates separated by $d = 20\\text{ mm}$ of area $S = 550\\text{ cm}^2$ is ionized by X-rays. At $V = 100\\text{ V}$, a current $I = 3.0\\,\\mu\\text{A}$ flows (below saturation). The ion mobilities are $u_0^+ = 1.37\\text{ cm}^2/(\\text{V}\\cdot\\text{s})$ and $u_0^- = 1.91\\text{ cm}^2/(\\text{V}\\cdot\\text{s})$. Find the concentration $n$ of positive ions.",
        "hints": [
            "The current density is $j = I/S = e n (u^+ + u^-) E$.",
            "The electric field is $E = V/d$.",
            "Solve for $n = \\frac{I d}{e (u_0^+ + u_0^-) V S}$."
        ],
        "answer": "$n = \\frac{I d}{e (u_0^+ + u_0^-) V S} = 2.3 \\times 10^8\\text{ cm}^{-3}$",
        "solution": "**1. Current Density in Terms of Mobilities:**\nFar below saturation, the gas follows Ohm's law with conductivity:\n$$\\sigma = e n (u_0^+ + u_0^-)$$\nThe electric field between the plates is $E = V/d$.\nThe current density is:\n$$j = \\frac{I}{S} = \\sigma E = e n (u_0^+ + u_0^-) \\frac{V}{d}$$\n\n**2. Solving for Ion Concentration:**\n$$n = \\frac{I d}{e (u_0^+ + u_0^-) V S}$$\n\n**3. Numerical Evaluation:**\nConvert to SI units: $I = 3.0 \\times 10^{-6}\\text{ A}$, $d = 0.020\\text{ m}$, $V = 100\\text{ V}$, $S = 0.0550\\text{ m}^2$, $u_0^+ + u_0^- = (1.37 + 1.91) \\times 10^{-4} = 3.28 \\times 10^{-4}\\text{ m}^2/(\\text{V}\\cdot\\text{s})$:\n$$n = \\frac{3.0 \\times 10^{-6} \\times 0.020}{(1.602 \\times 10^{-19}) \\times (3.28 \\times 10^{-4}) \\times 100 \\times 0.0550} \\approx 2.3 \\times 10^{14}\\text{ m}^{-3} = 2.3 \\times 10^8\\text{ cm}^{-3}$$",
        "tags": ["ionized gas", "ion mobility", "Ohm law in gas", "ion concentration"]
    },
    {
        "id": "3.213",
        "title": "Ion Mobility from Cut-Off Frequency of AC Voltage",
        "difficulty": 2,
        "question": "A gas is ionized near electrode 1 separated from electrode 2 by distance $l$. An AC voltage $V(t) = V_0 \\sin\\omega t$ is applied. Current is observed only for $\\omega < \\omega_0$. Find the mobility $u_0$ of the ions reaching electrode 2.",
        "hints": [
            "The drift velocity of ions is $v(t) = u_0 E(t) = u_0 \\frac{V_0}{l} \\sin\\omega t$.",
            "Maximum displacement during one positive half-cycle ($0 \\le t \\le \\pi/\\omega$): $\\Delta x_{\\max} = \\int_0^{\\pi/\\omega} u_0 \\frac{V_0}{l} \\sin\\omega t \\, dt = \\frac{2 u_0 V_0}{\\omega l}$.",
            "Ions reach electrode 2 if $\\Delta x_{\\max} \\ge l \\implies \\frac{2 u_0 V_0}{\\omega_0 l} = l$."
        ],
        "answer": "$u_0 = \\frac{\\omega_0 l^2}{2 V_0}$",
        "solution": "**1. Ion Drift Equation:**\nThe electric field across the gap is $E(t) = \\frac{V_0}{l} \\sin\\omega t$.\nThe drift velocity of ions moving toward electrode 2 is:\n$$v(t) = u_0 E(t) = \\frac{u_0 V_0}{l} \\sin\\omega t$$\n\n**2. Maximum Travel Distance:**\nIons created at electrode 1 move toward electrode 2 during the positive half-cycle ($0 \\le t \\le \\pi/\\omega$).\nThe maximum distance covered before the field reverses is:\n$$x_{\\max} = \\int_0^{\\pi/\\omega} v(t) \\, dt = \\frac{u_0 V_0}{l} \\left[ -\\frac{\\cos\\omega t}{\\omega} \\right]_0^{\\pi/\\omega} = \\frac{2 u_0 V_0}{\\omega l}$$\n\n**3. Cut-Off Condition:**\nIons just manage to reach electrode 2 ($x_{\\max} = l$) at the critical frequency $\\omega = \\omega_0$:\n$$\\frac{2 u_0 V_0}{\\omega_0 l} = l \\implies u_0 = \\frac{\\omega_0 l^2}{2 V_0}$$",
        "tags": ["ion mobility", "AC cut-off frequency", "drift velocity", "ionized gas"]
    },
    {
        "id": "3.214",
        "title": "Ion Generation Rate and Equilibrium Concentration",
        "difficulty": 2,
        "question": "Air between two plates of volume $V = 500\\text{ cm}^3$ is ionized by UV radiation, producing saturation current $I_{\\text{sat}} = 0.48\\,\\mu\\text{A}$. Find:\n(a) the number of ion pairs $n_i$ produced per unit volume per second;\n(b) the equilibrium concentration of ion pairs if the recombination coefficient is $r = 1.67 \\times 10^{-6}\\text{ cm}^3/\\text{s}$.",
        "hints": [
            "(a) At saturation, all created ions are swept to the electrodes before recombining: $I_{\\text{sat}} = e n_i V \\implies n_i = \\frac{I_{\\text{sat}}}{e V}$.",
            "(b) In dynamic equilibrium, generation rate equals recombination rate: $n_i = r n^2 \\implies n = \\sqrt{n_i / r}$."
        ],
        "answer": "(a) $n_i = \\frac{I_{\\text{sat}}}{e V} = 6.0 \\times 10^9\\text{ cm}^{-3}\\cdot\\text{s}^{-1}$; (b) $n = \\sqrt{\\frac{n_i}{r}} = 6.0 \\times 10^7\\text{ cm}^{-3}$",
        "solution": "**(a) Ionization Rate:**\nAt saturation current, all ions generated by the radiation in volume $V$ reach the plates without recombination:\n$$I_{\\text{sat}} = e \\dot{N} = e n_i V \\implies n_i = \\frac{I_{\\text{sat}}}{e V}$$\nEvaluating:\n$$n_i = \\frac{0.48 \\times 10^{-6}\\text{ A}}{(1.602 \\times 10^{-19}\\text{ C})(500\\text{ cm}^3)} = 6.0 \\times 10^9\\text{ cm}^{-3}\\cdot\\text{s}^{-1}$$\n\n**(b) Equilibrium Concentration:**\nIn steady state without electric field, ionization balances recombination:\n$$n_i = r n^2 \\implies n = \\sqrt{\\frac{n_i}{r}}$$\n$$n = \\sqrt{\\frac{6.0 \\times 10^9}{1.67 \\times 10^{-6}}} = \\sqrt{3.59 \\times 10^{15}} \\approx 6.0 \\times 10^7\\text{ cm}^{-3}$$",
        "tags": ["saturation current", "ionization rate", "recombination coefficient", "steady state"]
    },
    {
        "id": "3.215",
        "title": "Decay of Ion Concentration After Turning Off Ionizer",
        "difficulty": 2,
        "question": "An ionizer producing $n_i = 3.5 \\times 10^9\\text{ cm}^{-3}\\cdot\\text{s}^{-1}$ is switched off after long operation. Assuming recombination with $r = 1.67 \\times 10^{-6}\\text{ cm}^3/\\text{s}$ is the only decay mechanism, find how soon the ion concentration decreases $\\eta = 2.0$ times.",
        "hints": [
            "Initial equilibrium concentration: $n_0 = \\sqrt{n_i / r}$.",
            "Rate of decay after switching off: $\\frac{dn}{dt} = -r n^2$.",
            "Integrate $\\int_{n_0}^{n_0/\\eta} \\frac{dn}{n^2} = -r t \\implies t = \\frac{\\eta - 1}{r n_0}$."
        ],
        "answer": "$t = \\frac{\\eta - 1}{r n_0} = \\frac{\\eta - 1}{\\sqrt{r n_i}} = 13\\text{ ms}$",
        "solution": "**1. Initial Equilibrium Concentration:**\n$$n_0 = \\sqrt{\\frac{n_i}{r}} = \\sqrt{\\frac{3.5 \\times 10^9}{1.67 \\times 10^{-6}}} = 4.58 \\times 10^7\\text{ cm}^{-3}$$\n\n**2. Decay Kinetics:**\n$$\\frac{dn}{dt} = -r n^2 \\implies -\\frac{dn}{n^2} = r dt$$\n$$\\left[ \\frac{1}{n} \\right]_{n_0}^{n_0 / \\eta} = r t \\implies \\frac{\\eta}{n_0} - \\frac{1}{n_0} = r t$$\n$$t = \\frac{\\eta - 1}{r n_0} = \\frac{\\eta - 1}{\\sqrt{r n_i}}$$\n\n**3. Numerical Evaluation:**\n$$t = \\frac{2.0 - 1.0}{(1.67 \\times 10^{-6})(4.58 \\times 10^7)} = \\frac{1}{76.5}\\text{ s} \\approx 0.013\\text{ s} = 13\\text{ ms}$$",
        "tags": ["recombination decay", "ion concentration", "kinetic equation", "ionized air"]
    },
    {
        "id": "3.216",
        "title": "Discharge of Air Capacitor by Background Radiation",
        "difficulty": 2,
        "question": "A parallel-plate air capacitor with gap $d = 5.0\\text{ mm}$ is charged to $V = 90\\text{ V}$ and disconnected. Find the time during which voltage decreases by $\\eta = 1.0\\%$, given background ionization rate $n_i = 5.0\\text{ cm}^{-3}\\cdot\\text{s}^{-1}$ at saturation.",
        "hints": [
            "Charge on capacitor: $q = C V = \\frac{\\varepsilon_0 S}{d} V$.",
            "Discharge current at saturation: $I_{\\text{sat}} = e n_i S d$.",
            "Rate of voltage drop: $\\frac{dV}{dt} = -\\frac{I_{\\text{sat}}}{C} = -\\frac{e n_i d^2}{\\varepsilon_0}$.",
            "Set $\\Delta V = \\eta V$ and solve for $t = \\frac{\\varepsilon_0 \\eta V}{e n_i d^2}$."
        ],
        "answer": "$t = \\frac{\\varepsilon_0 \\eta V}{e n_i d^2} = 4.6\\text{ days}$",
        "solution": "**1. Discharge Rate at Saturation:**\nThe background radiation generates ion pairs at constant rate $n_i$ per unit volume.\nIn saturation, all ions are swept to the plates, producing discharge current:\n$$I_{\\text{sat}} = e n_i S d$$\n\n**2. Rate of Voltage Decrease:**\nThe capacitance of the air gap is $C = \\frac{\\varepsilon_0 S}{d}$.\n$$\\frac{dV}{dt} = -\\frac{I_{\\text{sat}}}{C} = -\\frac{e n_i S d}{\\varepsilon_0 S / d} = -\\frac{e n_i d^2}{\\varepsilon_0}$$\n\n**3. Time Interval:**\nFor a small fractional decrease $\\Delta V = \\eta V$:\n$$t = \\frac{\\Delta V}{|dV/dt|} = \\frac{\\varepsilon_0 \\eta V}{e n_i d^2}$$\n\n**4. Numerical Evaluation:**\nWith $V = 90\\text{ V}$, $\\eta = 0.010$, $d = 5.0 \\times 10^{-3}\\text{ m}$, $n_i = 5.0 \\times 10^6\\text{ m}^{-3}\\cdot\\text{s}^{-1}$:\n$$t = \\frac{(8.854 \\times 10^{-12}) \\times 0.010 \\times 90}{(1.602 \\times 10^{-19}) \\times (5.0 \\times 10^6) \\times (5.0 \\times 10^{-3})^2} = \\frac{7.969 \\times 10^{-12}}{2.0025 \\times 10^{-17}} \\approx 3.98 \\times 10^5\\text{ s} \\approx 4.6\\text{ days}$$",
        "tags": ["capacitor self-discharge", "background radiation", "saturation current", "atmospheric ionization"]
    },
    {
        "id": "3.217",
        "title": "Townsend Avalanche Current from Thermionic Cathode",
        "difficulty": 2,
        "question": "A capacitor of gap $d$ is filled with gas. One plate emits $\\nu_0$ electrons per second. In the electric field, each electron produces $\\alpha$ new electrons per unit path length by impact ionization. Find the electronic current at the opposite plate.",
        "hints": [
            "In traveling distance $dx$, the electron flux increases by $d\\nu = \\alpha \\nu dx$.",
            "Integrating $\\frac{d\\nu}{\\nu} = \\alpha dx$ from $x = 0$ (where $\\nu = \\nu_0$) to $x = d$ gives $\\nu(d) = \\nu_0 e^{\\alpha d}$.",
            "The current at the anode is $I = e \\nu(d) = e \\nu_0 e^{\\alpha d}$."
        ],
        "answer": "$I = e \\nu_0 e^{\\alpha d}$",
        "solution": "**1. Avalanche Growth Differential Equation:**\nLet $\\nu(x)$ be the rate of electrons passing cross-section $x$.\nDue to impact ionization with Townsend coefficient $\\alpha$:\n$$d\\nu = \\alpha \\nu(x) \\, dx$$\n\n**2. Integrating Along the Gap:**\n$$\\int_{\\nu_0}^{\\nu(d)} \\frac{d\\nu}{\\nu} = \\alpha \\int_0^d dx \\implies \\ln\\left( \\frac{\\nu(d)}{\\nu_0} \\right) = \\alpha d$$\n$$\\nu(d) = \\nu_0 e^{\\alpha d}$$\n\n**3. Electronic Current:**\n$$I = e \\nu(d) = e \\nu_0 e^{\\alpha d}$$",
        "tags": ["Townsend avalanche", "impact ionization", "gas discharge", "exponential multiplication"]
    },
    {
        "id": "3.218",
        "title": "Current Density with Uniform Volume Ionization and Avalanche",
        "difficulty": 2,
        "question": "Gas between capacitor plates separated by distance $d$ is uniformly ionized by UV radiation at rate $n_i$ electrons per unit volume per second. In the electric field, electrons produce $\\alpha$ new electrons per unit path length. Neglecting ionization by positive ions, find the electron current density at the anode.",
        "hints": [
            "In a slice of thickness $dx$ at position $x$, $n_i dx$ primary electrons are born per second.",
            "Each drifts the remaining distance $d - x$ to the anode, multiplying by $e^{\\alpha (d - x)}$.",
            "Integrate $j = e \\int_0^d n_i e^{\\alpha(d - x)} \\, dx$."
        ],
        "answer": "$j = \\frac{e n_i}{\\alpha} (e^{\\alpha d} - 1)$",
        "solution": "**1. Superposition of Electron Avalanches:**\nElectrons generated in a layer of thickness $dx$ at distance $x$ from the cathode travel a remaining distance $d - x$ to reach the anode.\nEach such electron multiplies by factor $e^{\\alpha (d - x)}$ via Townsend avalanche multiplication.\n\n**2. Total Current Density at the Anode:**\nThe total number of electrons arriving at the anode per unit area per second is:\n$$\\nu = \\int_0^d n_i e^{\\alpha (d - x)} \\, dx = n_i e^{\\alpha d} \\int_0^d e^{-\\alpha x} \\, dx$$\nEvaluating the integral:\n$$\\int_0^d e^{-\\alpha x} \\, dx = \\frac{1 - e^{-\\alpha d}}{\\alpha}$$\n$$\\nu = n_i e^{\\alpha d} \\left( \\frac{1 - e^{-\\alpha d}}{\\alpha} \\right) = \\frac{n_i}{\\alpha} (e^{\\alpha d} - 1)$$\n\n**3. Electronic Current Density:**\n$$j = e \\nu = \\frac{e n_i}{\\alpha} (e^{\\alpha d} - 1)$$",
        "tags": ["Townsend discharge", "volume ionization", "exponential avalanche", "anode current density"]
    }
]
