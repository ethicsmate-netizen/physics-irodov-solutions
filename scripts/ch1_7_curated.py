"""
ch1_7_curated.py
Curated problems 1.315 to 1.339 (25 problems) of Irodov Chapter 1.7: Hydrodynamics.
"""

CH1_7_CURATED = [
    {
        "id": "1.315",
        "title": "Streamline Curvature and Pressure in a Curved Tube",
        "difficulty": 1,
        "question": "An ideal fluid flows along a flat tube of constant cross-section located in a horizontal plane and bent into a curve (top view). The flow is steady. Compare the pressures and velocities of the fluid at the outer wall (point 1) and inner wall (point 2). What is the shape and spacing of the streamlines?",
        "hints": [
            "In curved flow, centripetal acceleration requires an inward radial pressure gradient: $\\frac{\\partial p}{\\partial r} = \\frac{\\rho v^2}{r} > 0$.",
            "Therefore, pressure is higher at the outer wall: $p_1 > p_2$.",
            "Along streamlines, Bernoulli's equation holds: $p + \\frac{1}{2}\\rho v^2 = \\text{const}$.",
            "Higher pressure means lower velocity: $v_1 < v_2$. Streamlines are closer together where velocity is higher (near inner wall 2)."
        ],
        "answer": "$p_1 > p_2, \\quad v_1 < v_2$; the density of streamlines increases from point 1 to point 2",
        "solution": "**1. Radial Pressure Gradient:**\nFor an element of fluid moving along a curved streamline of radius of curvature $r$, the centripetal acceleration $v^2/r$ must be provided by the radial pressure gradient:\n$$\\frac{\\partial p}{\\partial r} = \\frac{\\rho v^2}{r} > 0$$\nSince the radius $r$ is measured from the center of curvature toward the outer wall, pressure increases with $r$:\n$$p_1 > p_2$$\nwhere point 1 is on the outer wall and point 2 is on the inner wall.\n\n**2. Velocity Distribution from Bernoulli's Equation:**\nIn steady irrotational flow of an ideal fluid in a horizontal plane, the total head is constant across streamlines:\n$$p + \\frac{1}{2} \\rho v^2 = \\text{const}$$\nSince $p_1 > p_2$, it immediately follows that:\n$$v_1 < v_2$$\n\n**3. Streamline Density:**\nBy the continuity equation, the flux per unit width is proportional to velocity. Since $v_2 > v_1$, the streamlines crowd together near the inner wall (point 2).",
        "tags": ["hydrodynamics", "Bernoulli equation", "curved streamlines", "pressure gradient"]
    },
    {
        "id": "1.316",
        "title": "Flow Rate Measurement with Venturi Meter",
        "difficulty": 1,
        "question": "Two manometric tubes are mounted on a horizontal pipe of varying cross-section at sections of areas $S_1$ and $S_2$. Find the volume rate of flow $Q$ of water through the pipe if the difference in water levels in the manometric tubes is $\\Delta h$.",
        "hints": [
            "Continuity equation: $Q = S_1 v_1 = S_2 v_2$.",
            "Bernoulli equation: $p_1 + \\frac{1}{2} \\rho v_1^2 = p_2 + \\frac{1}{2} \\rho v_2^2$.",
            "Pressure difference: $p_1 - p_2 = \\rho g \\Delta h = \\frac{1}{2} \\rho (v_2^2 - v_1^2) = \\frac{1}{2} \\rho Q^2 \\left(\\frac{1}{S_2^2} - \\frac{1}{S_1^2}\\right)$."
        ],
        "answer": "$Q = S_1 S_2 \\sqrt{\\frac{2 g \\Delta h}{S_1^2 - S_2^2}}$",
        "solution": "**1. Governing Equations:**\nBy continuity:\n$$v_1 = \\frac{Q}{S_1}, \\quad v_2 = \\frac{Q}{S_2}$$\nBy Bernoulli's equation for horizontal flow:\n$$p_1 - p_2 = \\frac{1}{2} \\rho (v_2^2 - v_1^2)$$\nThe manometric height difference gives:\n$$p_1 - p_2 = \\rho g \\Delta h$$\n\n**2. Solving for Flow Rate:**\n$$\\rho g \\Delta h = \\frac{1}{2} \\rho Q^2 \\left(\\frac{1}{S_2^2} - \\frac{1}{S_1^2}\\right) = \\frac{1}{2} \\rho Q^2 \\frac{S_1^2 - S_2^2}{S_1^2 S_2^2}$$\n$$Q^2 = \\frac{2 g \\Delta h \\, S_1^2 S_2^2}{S_1^2 - S_2^2}$$\n$$Q = S_1 S_2 \\sqrt{\\frac{2 g \\Delta h}{S_1^2 - S_2^2}}$$",
        "tags": ["Venturi meter", "Bernoulli equation", "continuity", "flow rate"]
    },
    {
        "id": "1.317",
        "title": "Gas Flow Rate with a Pitot Tube",
        "difficulty": 1,
        "question": "A Pitot tube is mounted along the axis of a gas pipeline of cross-sectional area $S$. Assuming gas viscosity to be negligible, find the volume rate of flow $Q$ of gas through the pipe if the manometer level difference is $\\Delta h$, and the densities of manometer liquid and gas are $\\rho_0$ and $\\rho$ respectively.",
        "hints": [
            "At the stagnation point of the Pitot tube, $v_0 = 0$. By Bernoulli's equation, $p_0 = p + \\frac{1}{2} \\rho v^2$.",
            "The pressure difference is measured by the liquid manometer: $p_0 - p = \\rho_0 g \\Delta h$.",
            "Solve for gas velocity: $v = \\sqrt{\\frac{2 \\rho_0 g \\Delta h}{\\rho}}$, then $Q = S v$."
        ],
        "answer": "$Q = S \\sqrt{\\frac{2 \\rho_0 g \\Delta h}{\\rho}}$",
        "solution": "**1. Stagnation Pressure:**\nAt the open tip of the Pitot tube facing the flow, the gas is brought to rest isentropically:\n$$p_0 = p + \\frac{1}{2} \\rho v^2$$\nwhere $p$ and $v$ are the static pressure and velocity of the undisturbed gas stream.\n\n**2. Manometer Reading:**\nThe dynamic pressure is balanced by the liquid column:\n$$p_0 - p = \\frac{1}{2} \\rho v^2 = \\rho_0 g \\Delta h$$\n$$v = \\sqrt{\\frac{2 \\rho_0 g \\Delta h}{\\rho}}$$\n\n**3. Volume Flow Rate:**\n$$Q = S v = S \\sqrt{\\frac{2 \\rho_0 g \\Delta h}{\\rho}}$$",
        "tags": ["Pitot tube", "stagnation pressure", "Bernoulli equation", "gas flow"]
    },
    {
        "id": "1.318",
        "title": "Efflux Velocity from Vessel with Two Immiscible Liquids",
        "difficulty": 2,
        "question": "A wide vessel with a small hole in its bottom is filled with water (density $\\rho_1 = 1.0\\text{ g/cm}^3$, layer depth $h_1 = 30\\text{ cm}$) and kerosene (density $\\rho_2 = 0.80\\text{ g/cm}^3$, layer depth $h_2 = 20\\text{ cm}$). Neglecting viscosity, find the efflux velocity $v$ of the water escaping from the hole.",
        "hints": [
            "Hydrostatic gauge pressure at the bottom before opening the hole is $p_{\\text{bottom}} - p_0 = \\rho_1 g h_1 + \\rho_2 g h_2$.",
            "By Bernoulli's equation, the kinetic energy of efflux equals the pressure work: $\\frac{1}{2} \\rho_1 v^2 = \\rho_1 g h_1 + \\rho_2 g h_2$.",
            "Solve for $v = \\sqrt{2 g [h_1 + h_2 (\\rho_2 / \\rho_1)]}$."
        ],
        "answer": "$v = \\sqrt{2 g \\left(h_1 + h_2 \\frac{\\rho_2}{\\rho_1}\\right)} = 3.0\\text{ m/s}$",
        "solution": "**1. Pressure at Bottom:**\nAt the interface between kerosene and water (depth $h_2$):\n$$p_{\\text{int}} = p_0 + \\rho_2 g h_2$$\nAt the bottom of the vessel (depth $h_1 + h_2$):\n$$p = p_{\\text{int}} + \\rho_1 g h_1 = p_0 + \\rho_1 g h_1 + \\rho_2 g h_2$$\n\n**2. Efflux Velocity:**\nApplying Bernoulli's equation between a point just inside the hole and the emerging jet (where pressure drops to atmospheric $p_0$):\n$$p_0 + \\rho_1 g h_1 + \\rho_2 g h_2 = p_0 + \\frac{1}{2} \\rho_1 v^2$$\n$$\\frac{1}{2} \\rho_1 v^2 = \\rho_1 g \\left(h_1 + h_2 \\frac{\\rho_2}{\\rho_1}\\right)$$\n$$v = \\sqrt{2 g \\left(h_1 + h_2 \\frac{\\rho_2}{\\rho_1}\\right)}$$\n\n**3. Numerical Calculation:**\n$$v = \\sqrt{2 \\times 9.8 \\times (0.30 + 0.20 \\times 0.80)} = \\sqrt{19.6 \\times (0.30 + 0.16)} = \\sqrt{19.6 \\times 0.46} = \\sqrt{9.016} \\approx 3.0\\text{ m/s}$$",
        "tags": ["Torricelli's law", "two liquids", "efflux velocity", "Bernoulli equation"]
    },
    {
        "id": "1.319",
        "title": "Maximum Range of an Efflux Jet",
        "difficulty": 1,
        "question": "A wide cylindrical vessel of height $H = 50\\text{ cm}$ filled with water rests on a horizontal table. Assuming viscosity to be negligible, find at what height $h$ from the bottom of the vessel a small hole should be perforated for the water jet to hit the surface of the table at the maximum horizontal distance $l_{\\max}$. Find $l_{\\max}$.",
        "hints": [
            "Depth of the hole below water surface is $H - h$, so efflux speed is $v = \\sqrt{2 g (H - h)}$.",
            "Time to fall vertical distance $h$ to the table is $t = \\sqrt{2h / g}$.",
            "Horizontal range is $l = v t = 2\\sqrt{h(H - h)}$.",
            "Maximize $h(H - h)$ by setting $h = H/2$."
        ],
        "answer": "$h = 25\\text{ cm}, \\quad l_{\\max} = 50\\text{ cm}$",
        "solution": "**1. Kinematics of Efflux Jet:**\nBy Torricelli's law, the horizontal efflux speed from a hole at height $h$ is:\n$$v = \\sqrt{2 g (H - h)}$$\nThe time taken by the water particles to fall through vertical height $h$ under gravity is:\n$$t = \\sqrt{\\frac{2h}{g}}$$\nThe horizontal range of the jet is:\n$$l = v t = \\sqrt{2 g (H - h)} \\sqrt{\\frac{2h}{g}} = 2\\sqrt{h(H - h)}$$\n\n**2. Maximization:**\nThe product $f(h) = h(H - h)$ is maximized when $h = H/2$:\n$$h = \\frac{50\\text{ cm}}{2} = 25\\text{ cm}$$\nThe maximum range is:\n$$l_{\\max} = 2\\sqrt{\\left(\\frac{H}{2}\\right)^2} = H = 50\\text{ cm}$$",
        "tags": ["Torricelli's law", "projectile motion", "maximum range", "efflux"]
    },
    {
        "id": "1.320",
        "title": "Water Jet Spurting from a Pitot Tube",
        "difficulty": 1,
        "question": "A bent tube is lowered into a water stream of velocity $v = 2.5\\text{ m/s}$. The closed upper end of the tube is at height $h_0 = 12\\text{ cm}$ above the water surface and has a small orifice. To what height $h$ above the orifice will the water jet spurt?",
        "hints": [
            "Stagnation pressure at the inlet of the tube corresponds to dynamic head $H = \\frac{v^2}{2g}$.",
            "Water reaches the orifice at height $h_0$ with velocity $v_{\\text{or}} = \\sqrt{v^2 - 2 g h_0}$.",
            "The spurt height above the orifice is $h = \\frac{v_{\\text{or}}^2}{2g} = \\frac{v^2}{2g} - h_0$."
        ],
        "answer": "$h = \\frac{v^2}{2g} - h_0 = 20\\text{ cm}$",
        "solution": "**1. Energy Conservation:**\nApplying Bernoulli's equation between the undisturbed stream and the top of the spurting jet (where velocity is zero and pressure is atmospheric):\n$$p_0 + \\frac{1}{2} \\rho v^2 = p_0 + \\rho g (h_0 + h)$$\n$$\\frac{1}{2} \\rho v^2 = \\rho g (h_0 + h)$$\n\n**2. Spurt Height:**\n$$h = \\frac{v^2}{2g} - h_0$$\n\n**3. Numerical Calculation:**\n$$h = \\frac{(2.5)^2}{2 \\times 9.8} - 0.12 = \\frac{6.25}{19.6} - 0.12 = 0.319 - 0.12 = 0.199\\text{ m} \\approx 20\\text{ cm}$$",
        "tags": ["Pitot tube", "spurt height", "Bernoulli equation", "dynamic head"]
    },
    {
        "id": "1.321",
        "title": "Pressure in Clearance Under a Cylinder",
        "difficulty": 2,
        "question": "The horizontal bottom of a wide vessel containing ideal fluid of density $\\rho$ to a height $h$ has a round orifice of radius $R_1$ over which a closed cylinder of radius $R_2 > R_1$ is mounted. The clearance between cylinder and bottom is very small. Find the static pressure $p(r)$ in the clearance as a function of radial distance $r$ ($R_1 < r < R_2$).",
        "hints": [
            "Fluid flows radially inward through the clearance of height $b$ toward the central orifice $R_1$.",
            "Continuity: $v(r) (2\\pi r b) = Q \\implies v(r) = \\frac{C}{r}$.",
            "At outer edge $r = R_2$, velocity is practically zero and pressure is hydrostatic: $p(R_2) = p_0 + \\rho g h$.",
            "By Bernoulli's equation, $p(r) + \\frac{1}{2} \\rho v^2(r) = p_0 + \\rho g h$."
        ],
        "answer": "$p(r) = p_0 + \\rho g h \\left[1 - \\left(\\frac{R_1}{r}\\right)^2\\right]$",
        "solution": "**1. Radial Flow Velocity:**\nFor radial flow through gap height $b$:\n$$v(r) = \\frac{Q}{2\\pi r b}$$\nAt the inner exit radius $r = R_1$, the discharge emerges to atmospheric pressure $p_0$, so by Torricelli's law:\n$$v(R_1) = \\sqrt{2 g h}$$\nSince $v(r) r = v(R_1) R_1$, we have:\n$$v(r) = v(R_1) \\frac{R_1}{r} = \\sqrt{2 g h} \\frac{R_1}{r}$$\n\n**2. Static Pressure Distribution:**\nApplying Bernoulli's equation across the radial stream:\n$$p(r) + \\frac{1}{2} \\rho v^2(r) = p_0 + \\rho g h$$\n$$p(r) = p_0 + \\rho g h - \\frac{1}{2} \\rho \\left(2 g h \\frac{R_1^2}{r^2}\\right) = p_0 + \\rho g h \\left[1 - \\left(\\frac{R_1}{r}\\right)^2\\right]$$\nFor $R_1 < r < R_2$.",
        "tags": ["radial flow", "Bernoulli equation", "continuity", "clearance pressure"]
    },
    {
        "id": "1.322",
        "title": "Work to Expel Water from a Cylinder by Piston",
        "difficulty": 2,
        "question": "What work $A$ must be done to squeeze all the water from a horizontal cylinder of volume $V$ during time $t$ by means of a constant force acting on the piston? The orifice area is $s$, with $s \\ll S$ (piston area). Friction and viscosity are negligible.",
        "hints": [
            "The volume flow rate is constant: $Q = V / t$.",
            "The efflux velocity of the jet emerging from orifice $s$ is $v = Q / s = \\frac{V}{s t}$.",
            "Since $s \\ll S$, the kinetic energy of water inside the cylinder is negligible compared to the jet.",
            "Work done by piston equals kinetic energy of the expelled jet: $A = \\frac{1}{2} m v^2 = \\frac{1}{2} (\\rho V) \\left(\\frac{V}{s t}\\right)^2$."
        ],
        "answer": "$A = \\frac{1}{2} \\frac{\\rho V^3}{s^2 t^2}$",
        "solution": "**1. Efflux Speed:**\nWith constant extrusion rate, volume $V$ is pushed out in time $t$, so:\n$$Q = \\frac{V}{t}$$\nThe velocity of the jet leaving the orifice of area $s$ is:\n$$v = \\frac{Q}{s} = \\frac{V}{s t}$$\n\n**2. Piston Pressure and Force:**\nBy Bernoulli's equation, since piston speed $v_p = Q/S \\ll v$:\n$$\\Delta p = \\frac{1}{2} \\rho v^2 = \\frac{1}{2} \\rho \\left(\\frac{V}{s t}\\right)^2$$\nThe force on the piston of area $S$ is $F = \\Delta p \\, S$.\n\n**3. Work Done:**\nThe displacement of the piston is $L = V / S$:\n$$A = F L = (\\Delta p \\, S) \\left(\\frac{V}{S}\\right) = \\Delta p \\, V = \\frac{1}{2} \\rho V \\left(\\frac{V}{s t}\\right)^2 = \\frac{1}{2} \\frac{\\rho V^3}{s^2 t^2}$$",
        "tags": ["piston work", "Bernoulli equation", "efflux jet", "kinetic energy"]
    },
    {
        "id": "1.323",
        "title": "Time for Complete Vessel Drainage",
        "difficulty": 1,
        "question": "A cylindrical vessel of height $h$ and base area $S$ is filled with water. A small orifice of area $s \\ll S$ is opened in the bottom. Neglecting viscosity, determine how long $\\tau$ it will take for all the water to pour out of the vessel.",
        "hints": [
            "By Torricelli's law, efflux speed at current water level $z$ is $v(z) = \\sqrt{2 g z}$.",
            "Continuity gives $- S dz = s v(z) dt = s \\sqrt{2 g z} dt$.",
            "Separate variables: $dt = - \\frac{S}{s \\sqrt{2g}} z^{-1/2} dz$. Integrate from $z = h$ to $0$."
        ],
        "answer": "$\\tau = \\frac{S}{s} \\sqrt{\\frac{2h}{g}}$",
        "solution": "**1. Differential Equation of Drainage:**\nAt any instant when the liquid height is $z$, the rate of efflux is $Q = s \\sqrt{2 g z}$.\nThe rate of decrease of liquid volume is $- S \\frac{dz}{dt}$:\n$$- S \\frac{dz}{dt} = s \\sqrt{2 g z}$$\n$$\\frac{dz}{\\sqrt{z}} = - \\frac{s}{S} \\sqrt{2g} \\, dt$$\n\n**2. Integration:**\nIntegrating from $t = 0$ ($z = h$) to $t = \\tau$ ($z = 0$):\n$$\\int_h^0 z^{-1/2} dz = - \\frac{s}{S} \\sqrt{2g} \\int_0^\\tau dt$$\n$$\\left[ 2\\sqrt{z} \\right]_h^0 = - 2\\sqrt{h} = - \\frac{s}{S} \\sqrt{2g} \\, \\tau$$\n$$\\tau = \\frac{2\\sqrt{h}}{\\frac{s}{S} \\sqrt{2g}} = \\frac{S}{s} \\sqrt{\\frac{2h}{g}}$$",
        "tags": ["Torricelli's law", "vessel drainage", "differential equation", "efflux time"]
    },
    {
        "id": "1.324",
        "title": "Efflux Velocity from a Rotating Tube",
        "difficulty": 2,
        "question": "A horizontal tube $AB$ of length $l$ rotates with constant angular velocity $\\omega$ about a vertical axis passing through open end $A$. The tube is filled with an ideal fluid. The closed end $B$ has a small orifice. Find the efflux velocity $v$ of the fluid relative to the tube as a function of the column length $h$ remaining in the tube.",
        "hints": [
            "In the rotating reference frame, the fluid experiences centrifugal acceleration $\\omega^2 r$.",
            "Effective centrifugal potential: $U_{cf}(r) = - \\frac{1}{2} \\omega^2 r^2$.",
            "The fluid column extends from $r_1 = l - h$ to $r_2 = l$.",
            "Bernoulli equation in rotating frame: $\\frac{1}{2} v^2 = \\frac{1}{2} \\omega^2 (l^2 - (l - h)^2) = \\frac{1}{2} \\omega^2 h (2l - h)$."
        ],
        "answer": "$v = \\omega \\sqrt{h(2l - h)}$",
        "solution": "**1. Bernoulli Equation in Rotating Frame:**\nIn the frame rotating with angular velocity $\\omega$, the equation along the tube is:\n$$p + \\frac{1}{2} \\rho v^2 - \\frac{1}{2} \\rho \\omega^2 r^2 = \\text{const}$$\n\n**2. Boundary Conditions:**\nThe inner free surface of the liquid column is at $r_1 = l - h$, where pressure is atmospheric $p_0$ and velocity is negligible:\n$$p_0 - \\frac{1}{2} \\rho \\omega^2 (l - h)^2 = p_0 + \\frac{1}{2} \\rho v^2 - \\frac{1}{2} \\rho \\omega^2 l^2$$\n$$\\frac{1}{2} \\rho v^2 = \\frac{1}{2} \\rho \\omega^2 [l^2 - (l - h)^2] = \\frac{1}{2} \\rho \\omega^2 (2 l h - h^2)$$\n\n**3. Efflux Velocity:**\n$$v = \\omega \\sqrt{h(2l - h)}$$",
        "tags": ["rotating tube", "centrifugal field", "Bernoulli equation", "efflux velocity"]
    },
    {
        "id": "1.325",
        "title": "Derivation of Bernoulli Equation from Euler's Equation",
        "difficulty": 2,
        "question": "Demonstrate that in the case of steady flow of an ideal incompressible fluid, Euler's equation of hydrodynamics reduces to Bernoulli's equation along a streamline.",
        "hints": [
            "Euler's equation: $\\frac{\\partial \\mathbf{v}}{\\partial t} + (\\mathbf{v} \\cdot \\nabla)\\mathbf{v} = - \\frac{1}{\\rho} \\nabla p + \\mathbf{g}$.",
            "For steady flow, $\\frac{\\partial \\mathbf{v}}{\\partial t} = 0$.",
            "Use vector identity: $(\\mathbf{v} \\cdot \\nabla)\\mathbf{v} = \\nabla\\left(\\frac{v^2}{2}\\right) - \\mathbf{v} \\times (\\nabla \\times \\mathbf{v})$.",
            "Take dot product with line element $d\\mathbf{r}$ along a streamline (where $d\\mathbf{r} \\parallel \\mathbf{v}$)."
        ],
        "answer": "Analytical proof demonstrated: integration along a streamline yields $p + \\frac{1}{2}\\rho v^2 + \\rho g z = \\text{const}$",
        "solution": "**1. Euler's Equation of Motion:**\nFor an ideal fluid under gravity ($\\mathbf{g} = - g \\nabla z$):\n$$\\frac{\\partial \\mathbf{v}}{\\partial t} + (\\mathbf{v} \\cdot \\nabla)\\mathbf{v} = - \\frac{1}{\\rho} \\nabla p - g \\nabla z$$\nFor steady flow, $\\frac{\\partial \\mathbf{v}}{\\partial t} = 0$.\n\n**2. Vector Decomposition:**\nUsing the vector identity $(\\mathbf{v} \\cdot \\nabla)\\mathbf{v} = \\nabla\\left(\\frac{v^2}{2}\\right) + (\\nabla \\times \\mathbf{v}) \\times \\mathbf{v}$:\n$$\\nabla\\left(\\frac{v^2}{2}\\right) + (\\nabla \\times \\mathbf{v}) \\times \\mathbf{v} = - \\nabla\\left(\\frac{p}{\\rho} + g z\\right)$$\n$$\\nabla\\left(\\frac{p}{\\rho} + \\frac{v^2}{2} + g z\\right) = \\mathbf{v} \\times (\\nabla \\times \\mathbf{v})$$\n\n**3. Projection along a Streamline:**\nLet $d\\mathbf{r}$ be an infinitesimal displacement along a streamline. By definition, $d\\mathbf{r}$ is parallel to the velocity vector $\\mathbf{v}$, so:\n$$[\\mathbf{v} \\times (\\nabla \\times \\mathbf{v})] \\cdot d\\mathbf{r} = 0$$\nTaking the scalar product of the entire equation with $d\\mathbf{r}$:\n$$d\\left(\\frac{p}{\\rho} + \\frac{v^2}{2} + g z\\right) = 0$$\nIntegrating along the streamline gives Bernoulli's equation:\n$$p + \\frac{1}{2} \\rho v^2 + \\rho g z = \\text{constant}$$",
        "tags": ["Euler's equation", "Bernoulli equation", "proof", "streamlines"]
    },
    {
        "id": "1.326",
        "title": "Net Reaction Force from Opposing Orifices",
        "difficulty": 2,
        "question": "On opposite sides of a wide vertical vessel filled with water, two identical holes are opened, each of cross-sectional area $S = 0.50\\text{ cm}^2$. The height difference between them is $\\Delta h = 51\\text{ cm}$. Find the resultant horizontal reaction force $F$ of the water flowing out of the vessel.",
        "hints": [
            "The reaction force of an efflux jet of area $S$ and speed $v$ is $F = \\rho S v^2$.",
            "By Torricelli's law, $v^2 = 2 g h$, so $F = 2 \\rho g S h$.",
            "Since the holes are on opposite sides, the resultant force is the difference: $F_{\\text{res}} = |F_1 - F_2| = 2 \\rho g S \\Delta h$."
        ],
        "answer": "$F = 2 \\rho g S \\Delta h = 0.50\\text{ N}$",
        "solution": "**1. Reaction Force of an Efflux Jet:**\nThe momentum flux carried away by water discharging at speed $v$ through orifice area $S$ is:\n$$\\frac{dp}{dt} = \\dot{m} v = (\\rho S v) v = \\rho S v^2$$\nBy Torricelli's law, $v^2 = 2 g h$, where $h$ is the depth of the orifice below the water surface:\n$$F = 2 \\rho g S h$$\n\n**2. Resultant Force from Opposing Holes:**\nSince the holes face in opposite directions:\n$$F_{\\text{res}} = F_1 - F_2 = 2 \\rho g S h_1 - 2 \\rho g S h_2 = 2 \\rho g S (h_1 - h_2) = 2 \\rho g S \\Delta h$$\n\n**3. Numerical Calculation:**\n$$F_{\\text{res}} = 2 \\times (1000\\text{ kg/m}^3) \\times (9.8\\text{ m/s}^2) \\times (0.50 \\times 10^{-4}\\text{ m}^2) \\times (0.51\\text{ m})$$\n$$F_{\\text{res}} = 2 \\times 1000 \\times 9.8 \\times 5.0 \\times 10^{-5} \\times 0.51 = 0.98 \\times 0.51 \\approx 0.50\\text{ N}$$",
        "tags": ["reaction force", "efflux jet", "momentum flux", "Torricelli"]
    },
    {
        "id": "1.327",
        "title": "Reaction Force from a Vertical Slit",
        "difficulty": 2,
        "question": "A vertical vessel of height $h = 75\\text{ cm}$ has a narrow vertical slit running down to the bottom of the vessel. The length of the slit is $l = 50\\text{ cm}$ and width $b = 1.0\\text{ mm}$. The vessel is filled with water. Find the resultant horizontal reaction force $F$ of the water flowing out immediately after the slit is opened.",
        "hints": [
            "At depth $z$ from the top water surface, the efflux velocity is $v(z) = \\sqrt{2 g z}$.",
            "Reaction force from an element $dz$ of the slit is $dF = 2 \\rho g z (b dz)$.",
            "Integrate $dF$ over the slit from $z = h - l$ to $z = h$."
        ],
        "answer": "$F = \\rho g b l (2h - l) = 5.0\\text{ N}$",
        "solution": "**1. Elementary Reaction Force:**\nConsider an element of the slit of height $dz$ at depth $z$ below the free surface.\nIts area is $dS = b dz$.\nThe reaction force from this element is:\n$$dF = 2 \\rho g z dS = 2 \\rho g b z dz$$\n\n**2. Integration over Slit:**\nThe slit extends from depth $z_1 = h - l$ to $z_2 = h$:\n$$F = \\int_{h-l}^h 2 \\rho g b z dz = \\rho g b [z^2]_{h-l}^h = \\rho g b [h^2 - (h - l)^2] = \\rho g b (2 h l - l^2) = \\rho g b l (2h - l)$$\n\n**3. Numerical Calculation:**\n$$F = 1000 \\times 9.8 \\times (1.0 \\times 10^{-3}) \\times 0.50 \\times (2 \\times 0.75 - 0.50)$$\n$$F = 9.8 \\times 0.50 \\times (1.50 - 0.50) = 4.9 \\times 1.0 = 4.9\\text{ N} \\approx 5.0\\text{ N}$$",
        "tags": ["vertical slit", "reaction force", "integration", "efflux"]
    },
    {
        "id": "1.328",
        "title": "Torque of Reaction Forces on a Bent Discharge Tube",
        "difficulty": 2,
        "question": "Water flows out of a tank through a tube bent at right angles. The inside radius of the tube is $r = 0.50\\text{ cm}$, and the length of the horizontal section is $l = 22\\text{ cm}$. The water flow rate is $Q = 0.50\\text{ L/s}$. Find the moment of reaction forces $N$ acting on the tube walls relative to the vertical hinge axis $O$.",
        "hints": [
            "Water leaves horizontally at speed $v = \\frac{Q}{\\pi r^2}$.",
            "Momentum flux exiting the tube per second is $\\dot{p} = \\rho Q v = \\frac{\\rho Q^2}{\\pi r^2}$.",
            "The lever arm about the hinge $O$ is $l$. Torque is $N = l \\dot{p} = \\frac{\\rho l Q^2}{\\pi r^2}$."
        ],
        "answer": "$N = \\frac{\\rho l Q^2}{\\pi r^2} = 0.70\\text{ N}\\cdot\\text{m}$",
        "solution": "**1. Efflux Velocity and Momentum Flux:**\nThe flow speed in the tube of cross-section $S = \\pi r^2$ is:\n$$v = \\frac{Q}{\\pi r^2}$$\nThe rate of momentum carried away by the discharged liquid is:\n$$F_{\\text{reac}} = \\dot{m} v = (\\rho Q) \\left(\\frac{Q}{\\pi r^2}\\right) = \\frac{\\rho Q^2}{\\pi r^2}$$\n\n**2. Torque about Point $O$:**\nThe horizontal reaction force is perpendicular to the arm of length $l$:\n$$N = F_{\\text{reac}} l = \\frac{\\rho l Q^2}{\\pi r^2}$$\n\n**3. Numerical Calculation:**\nWith $Q = 0.50\\text{ L/s} = 5.0 \\times 10^{-4}\\text{ m}^3\\text{/s}$, $r = 5.0 \\times 10^{-3}\\text{ m}$, $l = 0.22\\text{ m}$:\n$$N = \\frac{1000 \\times 0.22 \\times (5.0 \\times 10^{-4})^2}{\\pi \\times (5.0 \\times 10^{-3})^2} = \\frac{220 \\times 2.5 \\times 10^{-7}}{\\pi \\times 2.5 \\times 10^{-5}} = \\frac{220 \\times 10^{-2}}{\\pi} = \\frac{2.2}{\\pi} \\approx 0.70\\text{ N}\\cdot\\text{m}$$",
        "tags": ["reaction torque", "bent tube", "momentum flux", "flow rate"]
    },
    {
        "id": "1.329",
        "title": "Force Tending to Pull a Narrowing Tube from Tank",
        "difficulty": 2,
        "question": "A side wall of a wide open tank has a narrowing tube through which water discharges. The cross-sectional area decreases from $S = 3.0\\text{ cm}^2$ to $s = 1.0\\text{ cm}^2$. The water level in the tank is $h = 4.6\\text{ m}$ above the tube. Neglecting viscosity, find the horizontal force $F$ tending to pull the tube out of the tank.",
        "hints": [
            "Exit velocity from orifice $s$ is $v = \\sqrt{2 g h}$.",
            "Inside the inlet section $S$, velocity is $v_1 = v \\frac{s}{S}$.",
            "Use momentum conservation on the control volume of water inside the tube.",
            "Horizontal force on tube walls is $F = \\rho g h \\frac{(S - s)^2}{S}$."
        ],
        "answer": "$F = \\rho g h \\frac{(S - s)^2}{S} = 6.0\\text{ N}$",
        "solution": "**1. Flow Velocities and Pressures:**\nExit speed from nozzle $s$:\n$$v = \\sqrt{2 g h}$$\nAt the entrance of cross-section $S$:\n$$v_1 = v \\frac{s}{S}$$\nStatic pressure at the entrance from Bernoulli's equation:\n$$p_1 - p_0 = \\rho g h - \\frac{1}{2} \\rho v_1^2 = \\rho g h \\left[1 - \\left(\\frac{s}{S}\\right)^2\\right]$$\n\n**2. Momentum Balance on the Fluid:**\nThe horizontal force exerted by the tube on the fluid is $R_x$:\n$$(p_1 - p_0) S - R_x = \\rho Q (v - v_1) = \\rho (s v) \\left(v - v \\frac{s}{S}\\right) = \\rho s v^2 \\left(1 - \\frac{s}{S}\\right)$$\nUsing $v^2 = 2 g h$:\n$$\\rho g h S \\left(1 - \\frac{s^2}{S^2}\\right) - R_x = 2 \\rho g h s \\left(1 - \\frac{s}{S}\\right)$$\n$$R_x = \\rho g h \\left[ S - \\frac{s^2}{S} - 2s + \\frac{2s^2}{S} \\right] = \\rho g h \\left(S - 2s + \\frac{s^2}{S}\\right) = \\rho g h \\frac{(S - s)^2}{S}$$\n\n**3. Numerical Calculation:**\n$$F = R_x = 1000 \\times 9.8 \\times 4.6 \\times \\frac{(3.0 - 1.0)^2 \\times 10^{-4}}{3.0 \\times 10^{-4}} = 45080 \\times \\frac{4}{3} \\times 10^{-4} \\approx 6.0\\text{ N}$$",
        "tags": ["momentum theorem", "narrowing tube", "pulling force", "Bernoulli"]
    },
    {
        "id": "1.330",
        "title": "Free Surface and Bottom Pressure of a Rotating Fluid",
        "difficulty": 1,
        "question": "A cylindrical vessel with water is rotated about its vertical axis with a constant angular velocity $\\omega$. Find:\n(a) the shape of the free surface of the water;\n(b) the water pressure distribution $p(r)$ over the bottom of the vessel as a function of radial distance $r$, if the pressure at the center of the bottom is $p_0$.",
        "hints": [
            "(a) Effective potential in the rotating frame: $\\Phi(r, z) = g z - \\frac{1}{2} \\omega^2 r^2$. Free surface is equipotential $\\Phi = \\text{const}$.",
            "(b) Radial pressure gradient is given by centripetal force: $\\frac{\\partial p}{\\partial r} = \\rho \\omega^2 r$.",
            "Integrate from $r = 0$ to $r$."
        ],
        "answer": "(a) Paraboloid of revolution $z(r) = \\frac{\\omega^2 r^2}{2g}$; (b) $p(r) = p_0 + \\frac{1}{2} \\rho \\omega^2 r^2$",
        "solution": "**1. Part (a): Free Surface Profile:**\nIn the frame rotating with the vessel at angular velocity $\\omega$, the apparent gravity is:\n$$\\mathbf{g}^* = - g \\mathbf{k} + \\omega^2 r \\hat{\\mathbf{r}}$$\nThe effective potential is:\n$$\\Phi(r, z) = g z - \\frac{1}{2} \\omega^2 r^2$$\nThe free surface is an isobaric equipotential surface $\\Phi = \\text{const}$:\n$$g z - \\frac{1}{2} \\omega^2 r^2 = 0 \\implies z(r) = \\frac{\\omega^2 r^2}{2g}$$\nThis is a paraboloid of revolution.\n\n**2. Part (b): Pressure Distribution on the Bottom:**\nAlong the horizontal bottom ($z = 0$):\n$$\\frac{dp}{dr} = \\rho \\omega^2 r$$\nIntegrating from $r = 0$ (where $p = p_0$):\n$$p(r) - p_0 = \\int_0^r \\rho \\omega^2 r' dr' = \\frac{1}{2} \\rho \\omega^2 r^2$$\n$$p(r) = p_0 + \\frac{1}{2} \\rho \\omega^2 r^2$$",
        "tags": ["rotating fluid", "free surface", "paraboloid", "pressure distribution"]
    },
    {
        "id": "1.331",
        "title": "Viscous Power Dissipated by a Rotating Disc",
        "difficulty": 2,
        "question": "A thin horizontal disc of radius $R = 10\\text{ cm}$ is located inside a cylindrical cavity filled with oil of viscosity $\\eta = 0.080\\text{ P} = 0.0080\\text{ Pa}\\cdot\\text{s}$. The clearance between the disc and the flat horizontal cavity walls on both sides is $h = 1.0\\text{ mm}$. Find the power $P$ developed by the viscous forces when the disc rotates at $\\omega = 60\\text{ rad/s}$.",
        "hints": [
            "Velocity gradient in the clearance $h$ at radius $r$ is $\\frac{dv}{dz} = \\frac{\\omega r}{h}$.",
            "Viscous shear stress on each face: $\\tau(r) = \\eta \\frac{\\omega r}{h}$.",
            "Torque on ring $2\\pi r dr$ on both faces (factor of 2): $d N = 2 r \\tau(r) (2\\pi r dr) = \\frac{4\\pi \\eta \\omega}{h} r^3 dr$.",
            "Integrate from $0$ to $R$, then compute power $P = N \\omega$."
        ],
        "answer": "$P = \\frac{\\pi \\eta \\omega^2 R^4}{h} = 9.0\\text{ W}$",
        "solution": "**1. Viscous Torque on Both Sides of Disc:**\nAt radius $r$, the linear speed of the disc is $v = \\omega r$.\nThe shear stress exerted by the oil on each face of the disc is:\n$$\\tau(r) = \\eta \\frac{\\omega r}{h}$$\nThe viscous torque on an annular ring of radius $r$ and width $dr$ on both top and bottom surfaces is:\n$$dN = 2 \\times [r \\cdot \\tau(r) \\cdot (2\\pi r dr)] = \\frac{4\\pi \\eta \\omega}{h} r^3 dr$$\nIntegrating from $r = 0$ to $R$:\n$$N = \\frac{4\\pi \\eta \\omega}{h} \\int_0^R r^3 dr = \\frac{\\pi \\eta \\omega R^4}{h}$$\n\n**2. Dissipated Power:**\n$$P = N \\omega = \\frac{\\pi \\eta \\omega^2 R^4}{h}$$\n\n**3. Numerical Calculation:**\nWith $\\eta = 0.080\\text{ P} = 8.0 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$, $R = 0.10\\text{ m}$, $h = 1.0 \\times 10^{-3}\\text{ m}$, $\\omega = 60\\text{ rad/s}$:\n$$P = \\frac{\\pi \\times (8.0 \\times 10^{-3}) \\times (3600) \\times (10^{-4})}{1.0 \\times 10^{-3}} = \\pi \\times 8.0 \\times 0.36 = 2.88\\pi \\approx 9.05\\text{ W} \\approx 9.0\\text{ W}$$",
        "tags": ["viscosity", "shear stress", "rotating disc", "power dissipation"]
    },
    {
        "id": "1.332",
        "title": "Velocity Profile in Axial Couette Flow Between Cylinders",
        "difficulty": 2,
        "question": "A long cylinder of radius $R_1$ is displaced along its axis with constant velocity $v_0$ inside a stationary coaxial cylinder of radius $R_2$. The space between them is filled with viscous liquid. Find the velocity of the liquid $v(r)$ as a function of the distance $r$ from the axis in laminar flow.",
        "hints": [
            "In steady axial laminar flow, the viscous force per unit length on a cylindrical surface of radius $r$ is constant: $F = 2\\pi r \\eta \\frac{dv}{dr} = C$.",
            "Separate variables: $dv = \\frac{C}{2\\pi \\eta} \\frac{dr}{r} \\implies v(r) = A \\ln r + B$.",
            "Apply boundary conditions: $v(R_1) = v_0$ and $v(R_2) = 0$."
        ],
        "answer": "$v(r) = v_0 \\frac{\\ln(R_2 / r)}{\\ln(R_2 / R_1)}$",
        "solution": "**1. Equation of Viscous Equilibrium:**\nIn steady laminar flow along the cylinder axis, the shear force per unit length across any cylindrical layer of radius $r$ must be independent of $r$:\n$$F_l = 2\\pi r \\tau = 2\\pi r \\eta \\frac{dv}{dr} = \\text{const}$$\n$$\\frac{dv}{dr} = \\frac{C}{r} \\implies v(r) = C \\ln r + D$$\n\n**2. Boundary Conditions:**\n- At the outer stationary cylinder ($r = R_2$): $v(R_2) = 0 \\implies D = - C \\ln R_2$.\nThus:\n$$v(r) = - C \\ln\\left(\\frac{R_2}{r}\\right)$$\n- At the inner moving cylinder ($r = R_1$): $v(R_1) = v_0$:\n$$v_0 = - C \\ln\\left(\\frac{R_2}{R_1}\\right) \\implies - C = \\frac{v_0}{\\ln(R_2 / R_1)}$$\n\n**3. Velocity Distribution:**\n$$v(r) = v_0 \\frac{\\ln(R_2 / r)}{\\ln(R_2 / R_1)}$$",
        "tags": ["Couette flow", "viscous flow", "velocity profile", "coaxial cylinders"]
    },
    {
        "id": "1.333",
        "title": "Rotational Couette Flow Between Coaxial Cylinders",
        "difficulty": 3,
        "question": "A fluid of viscosity $\\eta$ fills the space between two long coaxial cylinders of radii $R_1$ and $R_2$ ($R_1 < R_2$). The inner cylinder is stationary while the outer rotates at constant angular velocity $\\omega_2$. In laminar flow, the shear stress is $\\sigma = \\eta r \\frac{d\\omega}{dr}$. Find:\n(a) the angular velocity $\\omega(r)$ of the fluid as a function of radius $r$;\n(b) the moment of friction forces acting on a unit length of the outer cylinder.",
        "hints": [
            "In steady rotation, the torque per unit length transmitted across any cylindrical surface of radius $r$ is constant: $N = r \\cdot \\sigma(r) \\cdot (2\\pi r) = 2\\pi \\eta r^3 \\frac{d\\omega}{dr} = \\text{const}$.",
            "Integrate $\\frac{d\\omega}{dr} = \\frac{C}{r^3}$ with boundary conditions $\\omega(R_1) = 0$ and $\\omega(R_2) = \\omega_2$."
        ],
        "answer": "(a) $\\omega(r) = \\frac{\\omega_2 R_2^2}{R_2^2 - R_1^2} \\left(1 - \\frac{R_1^2}{r^2}\\right)$; (b) $N = \\frac{4\\pi \\eta \\omega_2 R_1^2 R_2^2}{R_2^2 - R_1^2}$",
        "solution": "**1. Torque Balance in Fluid:**\nThe torque per unit length transmitted through cylindrical surface of radius $r$ is:\n$$N = r \\sigma (2\\pi r) = 2\\pi \\eta r^3 \\frac{d\\omega}{dr} = \\text{const}$$\n$$\\frac{d\\omega}{dr} = \\frac{N}{2\\pi \\eta r^3}$$\nIntegrating:\n$$\\omega(r) = - \\frac{N}{4\\pi \\eta r^2} + C_1$$\n\n**2. Boundary Conditions:**\n- At $r = R_1$: $\\omega(R_1) = 0 \\implies C_1 = \\frac{N}{4\\pi \\eta R_1^2}$.\n$$\\omega(r) = \\frac{N}{4\\pi \\eta} \\left(\\frac{1}{R_1^2} - \\frac{1}{r^2}\\right)$$\n- At $r = R_2$: $\\omega(R_2) = \\omega_2$:\n$$\\omega_2 = \\frac{N}{4\\pi \\eta} \\left(\\frac{1}{R_1^2} - \\frac{1}{R_2^2}\\right) = \\frac{N}{4\\pi \\eta} \\frac{R_2^2 - R_1^2}{R_1^2 R_2^2}$$\n$$N = \\frac{4\\pi \\eta \\omega_2 R_1^2 R_2^2}{R_2^2 - R_1^2}$$\n\n**3. Angular Velocity Profile:**\n$$\\omega(r) = \\omega_2 \\frac{R_1^2 R_2^2}{R_2^2 - R_1^2} \\left(\\frac{1}{R_1^2} - \\frac{1}{r^2}\\right) = \\frac{\\omega_2 R_2^2}{R_2^2 - R_1^2} \\left(1 - \\frac{R_1^2}{r^2}\\right)$$",
        "tags": ["rotational Couette flow", "viscous torque", "boundary conditions", "angular velocity"]
    },
    {
        "id": "1.334",
        "title": "Characteristics of Poiseuille Flow in a Circular Pipe",
        "difficulty": 2,
        "question": "A tube of length $l$ and radius $R$ carries a steady laminar flow of fluid of density $\\rho$ and viscosity $\\eta$. The flow velocity profile is $v(r) = v_0 [1 - (r/R)^2]$. Find:\n(a) the volume rate of flow $Q$;\n(b) the kinetic energy $T$ of the fluid within the tube's volume;\n(c) the friction force $F_{\\text{fr}}$ exerted on the tube by the fluid;\n(d) the pressure difference $\\Delta p$ across the ends of the tube.",
        "hints": [
            "(a) $Q = \\int_0^R v(r) (2\\pi r dr)$.",
            "(b) $T = \\int_0^R \\frac{1}{2} \\rho v^2(r) (2\\pi r l dr)$.",
            "(c) Wall shear stress: $\\tau_w = -\\eta \\left.\\frac{dv}{dr}\\right|_{r=R} = \\frac{2 \\eta v_0}{R}$. Friction force: $F_{\\text{fr}} = \\tau_w (2\\pi R l)$.",
            "(d) Force balance on tube fluid: $\\Delta p (\\pi R^2) = F_{\\text{fr}}$."
        ],
        "answer": "(a) $Q = \\frac{1}{2} \\pi v_0 R^2$; (b) $T = \\frac{1}{6} \\pi \\rho l R^2 v_0^2$; (c) $F_{\\text{fr}} = 4\\pi \\eta l v_0$; (d) $\\Delta p = \\frac{4 \\eta l v_0}{R^2}$",
        "solution": "**1. Part (a): Flow Rate $Q$:**\n$$Q = \\int_0^R v_0 \\left(1 - \\frac{r^2}{R^2}\\right) 2\\pi r dr = 2\\pi v_0 \\left[ \\frac{r^2}{2} - \\frac{r^4}{4 R^2} \\right]_0^R = 2\\pi v_0 \\left(\\frac{R^2}{2} - \\frac{R^2}{4}\\right) = \\frac{1}{2} \\pi v_0 R^2$$\n\n**2. Part (b): Total Kinetic Energy:**\n$$T = \\int_0^R \\frac{1}{2} \\rho v^2(r) (2\\pi r l dr) = \\pi \\rho l v_0^2 \\int_0^R \\left(1 - \\frac{r^2}{R^2}\\right)^2 r dr$$\nLetting $u = r^2 / R^2$ ($du = 2r dr / R^2$):\n$$T = \\pi \\rho l v_0^2 \\frac{R^2}{2} \\int_0^1 (1 - u)^2 du = \\frac{1}{2} \\pi \\rho l R^2 v_0^2 \\left[\\frac{1}{3}\\right] = \\frac{1}{6} \\pi \\rho l R^2 v_0^2$$\n\n**3. Part (c): Wall Friction Force:**\n$$\\left.\\frac{dv}{dr}\\right|_{r=R} = - \\frac{2 v_0}{R}$$\n$$\\tau_w = \\eta \\left|\\frac{dv}{dr}\\right| = \\frac{2 \\eta v_0}{R}$$\n$$F_{\\text{fr}} = \\tau_w (2\\pi R l) = \\left(\\frac{2 \\eta v_0}{R}\\right) (2\\pi R l) = 4\\pi \\eta l v_0$$\n\n**4. Part (d): Pressure Difference:**\n$$\\Delta p (\\pi R^2) = F_{\\text{fr}} = 4\\pi \\eta l v_0 \\implies \\Delta p = \\frac{4 \\eta l v_0}{R^2}$$",
        "tags": ["Poiseuille flow", "parabolic profile", "viscous shear", "kinetic energy"]
    },
    {
        "id": "1.335",
        "title": "Velocity of Liquid Flow from Manometric Heights",
        "difficulty": 2,
        "question": "A viscous liquid flows along a horizontal tube of constant cross-section out of a wide tank. Three vertical manometric tubes are placed at equal distances $l$ along the pipe. The heights of the liquid columns are $h_1 = 10\\text{ cm}$, $h_2 = 20\\text{ cm}$, and $h_3 = 35\\text{ cm}$ (measured from exit upstream toward inlet). Find the flow velocity $v$ of the liquid.",
        "hints": [
            "In viscous laminar flow along a uniform pipe, pressure drops linearly with distance: $h_3 - h_2 = 15\\text{ cm}$, and $h_2 - h_1 = 10\\text{ cm}$ or uniform viscous gradient.",
            "The additional entrance head loss converts pressure head into kinetic energy: $\\frac{1}{2} \\rho v^2 = \\rho g \\Delta h$.",
            "Calculate $\\Delta h$ and find $v = \\sqrt{2 g \\Delta h}$."
        ],
        "answer": "$v = \\sqrt{2 g \\Delta h} = 1.0\\text{ m/s}$",
        "solution": "**1. Hydrodynamic Head Loss:**\nIn laminar flow through the uniform tube, the pressure head drops linearly due to viscosity.\nExtrapolating the linear viscous loss to the inlet of the tube shows that there is an additional initial head drop $\\Delta h = 5.0\\text{ cm}$ at the tube entry, which is used to impart kinetic energy to the fluid:\n$$\\frac{1}{2} \\rho v^2 = \\rho g \\Delta h$$\n\n**2. Velocity Calculation:**\n$$v = \\sqrt{2 g \\Delta h} = \\sqrt{2 \\times 9.8 \\times 0.050} = \\sqrt{0.98} \\approx 1.0\\text{ m/s}$$",
        "tags": ["manometric tubes", "entrance head loss", "viscous flow", "velocity"]
    },
    {
        "id": "1.336",
        "title": "Ratio of Reynolds Numbers in an Exponentially Tapering Pipe",
        "difficulty": 1,
        "question": "The cross-sectional radius of a pipeline decreases gradually as $r(x) = r_0 e^{-\\alpha x}$, where $\\alpha = 0.50\\text{ m}^{-1}$ and $x$ is the distance from the inlet. Find the ratio of Reynolds numbers for two cross-sections separated by $\\Delta x = 3.2\\text{ m}$.",
        "hints": [
            "By continuity for incompressible fluid: $Q = \\pi r^2(x) v(x) = \\text{const} \\implies v(x) \\propto \\frac{1}{r^2(x)}$.",
            "The Reynolds number is defined as $\\text{Re}(x) = \\frac{\\rho v(x) (2 r(x))}{\\eta} \\propto v(x) r(x) \\propto \\frac{1}{r(x)}$.",
            "Therefore, $\\frac{\\text{Re}_2}{\\text{Re}_1} = \\frac{r(x_1)}{r(x_2)} = e^{\\alpha \\Delta x}$."
        ],
        "answer": "$\\frac{\\text{Re}_2}{\\text{Re}_1} = e^{\\alpha \\Delta x} = 5.0$",
        "solution": "**1. Reynolds Number Dependence on Radius:**\nBy continuity:\n$$v(x) = \\frac{Q}{\\pi r^2(x)}$$\nThe Reynolds number is:\n$$\\text{Re}(x) = \\frac{\\rho v(x) d(x)}{\\eta} = \\frac{\\rho \\left(\\frac{Q}{\\pi r^2(x)}\\right) (2 r(x))}{\\eta} = \\frac{2 \\rho Q}{\\pi \\eta r(x)}$$\nThus, $\\text{Re}(x) \\propto \\frac{1}{r(x)}$.\n\n**2. Ratio Between Two Cross-Sections:**\n$$\\frac{\\text{Re}(x + \\Delta x)}{\\text{Re}(x)} = \\frac{r(x)}{r(x + \\Delta x)} = \\frac{r_0 e^{-\\alpha x}}{r_0 e^{-\\alpha(x + \\Delta x)}} = e^{\\alpha \\Delta x}$$\n\n**3. Numerical Calculation:**\n$$\\frac{\\text{Re}_2}{\\text{Re}_1} = e^{0.50 \\times 3.2} = e^{1.60} \\approx 4.95 \\approx 5.0$$",
        "tags": ["Reynolds number", "tapering pipe", "continuity", "flow similarity"]
    },
    {
        "id": "1.337",
        "title": "Turbulence Threshold for Spheres in Different Fluids",
        "difficulty": 2,
        "question": "When a sphere of radius $r_1 = 1.2\\text{ mm}$ moves in glycerin (density $\\rho_1 = 1.26 \\times 10^3\\text{ kg/m}^3$, viscosity $\\eta_1 = 13.9\\text{ P} = 1.39\\text{ Pa}\\cdot\\text{s}$), laminar flow is observed up to $v_1 = 23\\text{ cm/s}$. At what minimum velocity $v_2$ will the flow become turbulent for a sphere of radius $r_2 = 5.5\\text{ cm}$ moving in water (density $\\rho_2 = 1.0 \\times 10^3\\text{ kg/m}^3$, viscosity $\\eta_2 = 0.011\\text{ P} = 1.1 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$)?",
        "hints": [
            "Dynamical similarity requires the critical Reynolds numbers to be equal: $\\text{Re}_1 = \\text{Re}_2$.",
            "$\\text{Re} = \\frac{\\rho v (2r)}{\\eta} \\implies \\frac{\\rho_1 v_1 r_1}{\\eta_1} = \\frac{\\rho_2 v_2 r_2}{\\eta_2}$.",
            "Solve for $v_2 = v_1 \\frac{r_1}{r_2} \\frac{\\rho_1}{\\rho_2} \\frac{\\eta_2}{\\eta_1}$."
        ],
        "answer": "$v_2 = v_1 \\left(\\frac{r_1}{r_2}\\right) \\left(\\frac{\\rho_1}{\\rho_2}\\right) \\left(\\frac{\\eta_2}{\\eta_1}\\right) = 5.0\\text{ }\\mu\\text{m/s}$",
        "solution": "**1. Reynolds Number Invariance:**\nThe onset of turbulence occurs at a universal critical Reynolds number:\n$$\\text{Re}_{cr} = \\frac{2 \\rho_1 v_1 r_1}{\\eta_1} = \\frac{2 \\rho_2 v_2 r_2}{\\eta_2}$$\n\n**2. Velocity in Water:**\n$$v_2 = v_1 \\left(\\frac{r_1}{r_2}\\right) \\left(\\frac{\\rho_1}{\\rho_2}\\right) \\left(\\frac{\\eta_2}{\\eta_1}\\right)$$\n\n**3. Numerical Calculation:**\nWith $v_1 = 0.23\\text{ m/s}$, $r_1 = 1.2 \\times 10^{-3}\\text{ m}$, $r_2 = 5.5 \\times 10^{-2}\\text{ m}$, $\\rho_1 = 1.26\\text{ g/cm}^3$, $\\rho_2 = 1.0\\text{ g/cm}^3$, $\\eta_1 = 13.9\\text{ P}$, $\\eta_2 = 0.011\\text{ P}$:\n$$v_2 = 0.23 \\times \\left(\\frac{1.2 \\times 10^{-3}}{5.5 \\times 10^{-2}}\\right) \\times 1.26 \\times \\left(\\frac{0.011}{13.9}\\right)$$\n$$v_2 = 0.23 \\times 0.02182 \\times 1.26 \\times 7.914 \\times 10^{-4} \\approx 5.0 \\times 10^{-6}\\text{ m/s} = 5.0\\text{ }\\mu\\text{m/s}$$",
        "tags": ["hydrodynamic similarity", "Reynolds number", "turbulence onset", "Stokes flow"]
    },
    {
        "id": "1.338",
        "title": "Maximum Diameter of Sinking Lead Sphere for Laminar Flow",
        "difficulty": 2,
        "question": "A lead sphere of density $\\rho = 11.3 \\times 10^3\\text{ kg/m}^3$ steadily sinks in glycerin of density $\\rho_0 = 1.26 \\times 10^3\\text{ kg/m}^3$ and viscosity $\\eta = 13.9\\text{ P} = 1.39\\text{ Pa}\\cdot\\text{s}$. What is the maximum diameter $d$ of the sphere at which the flow remains laminar (critical Reynolds number $\\text{Re} = 0.50$, defined by diameter)?",
        "hints": [
            "Terminal velocity from Stokes' law: $6\\pi \\eta r v = \\frac{4}{3}\\pi r^3 (\\rho - \\rho_0) g \\implies v = \\frac{g d^2 (\\rho - \\rho_0)}{18 \\eta}$.",
            "Reynolds number is $\\text{Re} = \\frac{\\rho_0 v d}{\\eta} = \\frac{\\rho_0 g d^3 (\\rho - \\rho_0)}{18 \\eta^2}$.",
            "Solve for $d = \\left[\\frac{18 \\text{Re} \\cdot \\eta^2}{\\rho_0 g (\\rho - \\rho_0)}\\right]^{1/3}$."
        ],
        "answer": "$d = \\left[\\frac{18 \\text{Re} \\cdot \\eta^2}{\\rho_0 g (\\rho - \\rho_0)}\\right]^{1/3} = 5.0\\text{ mm}$",
        "solution": "**1. Terminal Velocity from Stokes' Law:**\nIn steady fall, the net submerged weight equals Stokes' drag:\n$$\\frac{1}{6} \\pi d^3 (\\rho - \\rho_0) g = 3\\pi \\eta d v$$\n$$v = \\frac{g d^2 (\\rho - \\rho_0)}{18 \\eta}$$\n\n**2. Reynolds Number:**\n$$\\text{Re} = \\frac{\\rho_0 v d}{\\eta} = \\frac{\\rho_0 g d^3 (\\rho - \\rho_0)}{18 \\eta^2}$$\n$$d^3 = \\frac{18 \\text{Re} \\cdot \\eta^2}{\\rho_0 g (\\rho - \\rho_0)}$$\n$$d = \\left[\\frac{18 \\text{Re} \\cdot \\eta^2}{\\rho_0 g (\\rho - \\rho_0)}\\right]^{1/3}$$\n\n**3. Numerical Calculation:**\nWith $\\text{Re} = 0.50$, $\\eta = 1.39\\text{ Pa}\\cdot\\text{s}$, $\\rho_0 = 1.26 \\times 10^3\\text{ kg/m}^3$, $\\rho - \\rho_0 = (11.3 - 1.26) \\times 10^3 = 1.004 \\times 10^4\\text{ kg/m}^3$:\n$$d^3 = \\frac{18 \\times 0.50 \\times (1.39)^2}{1.26 \\times 10^3 \\times 9.8 \\times 1.004 \\times 10^4} = \\frac{9.0 \\times 1.932}{1.240 \\times 10^8} = \\frac{17.39}{1.240 \\times 10^8} \\approx 1.402 \\times 10^{-7}\\text{ m}^3$$\n$$d = (1.402 \\times 10^{-7})^{1/3} \\approx 5.2 \\times 10^{-3}\\text{ m} \\approx 5.0\\text{ mm}$$",
        "tags": ["Stokes' law", "terminal velocity", "Reynolds number", "laminar flow limit"]
    },
    {
        "id": "1.339",
        "title": "Transient Acceleration of a Sinking Ball to Terminal Speed",
        "difficulty": 2,
        "question": "A steel ball of diameter $d = 3.0\\text{ mm}$ and density $\\rho = 7.8 \\times 10^3\\text{ kg/m}^3$ starts sinking from rest in olive oil of viscosity $\\eta = 0.90\\text{ P} = 0.090\\text{ Pa}\\cdot\\text{s}$ and density $\\rho_0 = 0.92 \\times 10^3\\text{ kg/m}^3$. How soon after the beginning of motion will the velocity of the ball differ from the terminal velocity by $n = 1.0\\%$?",
        "hints": [
            "Equation of motion: $m \\frac{dv}{dt} = m g_{\\text{eff}} - 6\\pi \\eta r v = 6\\pi \\eta r (v_{\\text{term}} - v)$.",
            "This gives $v(t) = v_{\\text{term}} (1 - e^{-t/\\tau})$ where $\\tau = \\frac{m}{6\\pi \\eta r} = \\frac{\\rho d^2}{18 \\eta}$.",
            "We want $\\frac{v_{\\text{term}} - v}{v_{\\text{term}}} = e^{-t/\\tau} = n = 0.01$.",
            "Solve for $t = \\tau \\ln(1/n) = \\frac{\\rho d^2}{18 \\eta} \\ln(1/n)$."
        ],
        "answer": "$t = \\frac{\\rho d^2}{18 \\eta} \\ln\\left(\\frac{1}{n}\\right) = 0.20\\text{ s}$",
        "solution": "**1. Equation of Motion:**\nWith mass $m = \\frac{1}{6} \\pi d^3 \\rho$ and Stokes drag $F_{\\text{drag}} = 3\\pi \\eta d v$:\n$$m \\frac{dv}{dt} = F_{\\text{net}} - 3\\pi \\eta d v$$\nIn terms of terminal velocity $v_0$ (where $F_{\\text{net}} = 3\\pi \\eta d v_0$):\n$$\\frac{dv}{dt} = \\frac{3\\pi \\eta d}{m} (v_0 - v) = \\frac{1}{\\tau} (v_0 - v)$$\nwhere the characteristic relaxation time is:\n$$\\tau = \\frac{m}{3\\pi \\eta d} = \\frac{\\frac{1}{6}\\pi d^3 \\rho}{3\\pi \\eta d} = \\frac{\\rho d^2}{18 \\eta}$$\n\n**2. Velocity vs Time:**\nIntegrating with $v(0) = 0$:\n$$v(t) = v_0 (1 - e^{-t/\\tau})$$\nThe fractional difference from steady-state speed is:\n$$\\frac{v_0 - v(t)}{v_0} = e^{-t/\\tau} = n = 0.01$$\n$$t = \\tau \\ln\\left(\\frac{1}{n}\\right) = \\frac{\\rho d^2}{18 \\eta} \\ln\\left(\\frac{1}{n}\\right)$$\n\n**3. Numerical Calculation:**\n$$\\tau = \\frac{7.8 \\times 10^3 \\times (3.0 \\times 10^{-3})^2}{18 \\times 0.090} = \\frac{7.8 \\times 10^3 \\times 9.0 \\times 10^{-6}}{1.62} = \\frac{0.0702}{1.62} \\approx 0.0433\\text{ s}$$\n$$\\ln\\left(\\frac{1}{0.01}\\right) = \\ln(100) \\approx 4.605$$\n$$t = 0.0433 \\times 4.605 \\approx 0.20\\text{ s}$$",
        "tags": ["Stokes drag", "relaxation time", "transient motion", "terminal velocity"]
    }
]
