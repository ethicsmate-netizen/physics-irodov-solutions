"""
ch1_batch1.py
Problems 1.1 through 1.20 of Irodov Chapter 1.1 Kinematics.
"""

BATCH_1 = [
    {
        "id": "1.1",
        "title": "Motorboat and Raft (Flow Velocity)",
        "difficulty": 1,
        "question": "A motorboat going downstream overcame a raft at a point $A$; $\\tau = 60\\text{ min}$ later it turned back and after some time passed the raft at a distance $l = 6.0\\text{ km}$ from the point $A$. Find the flow velocity assuming the duty of the engine to be constant.",
        "hints": [
            "Consider the reference frame attached to the water (flowing with the river).",
            "In the water frame, how does the raft move? How do the upstream and downstream speeds of the motorboat compare?",
            "Notice that the boat spends time $\\tau$ moving away from the raft in the water frame, so it must spend time $\\tau$ returning to it."
        ],
        "answer": "$v_{\\text{flow}} = \\frac{l}{2\\tau} = 3.0\\text{ km/h}$",
        "solution": "**Method: Reference Frame of River Water**\n\nIn the reference frame attached to the flowing water:\n1. The raft is stationary since it drifts with the current: $v_{\\text{raft}}' = 0$.\n2. The motorboat travels away from the raft with its engine speed $v_{\\text{boat}}$ for a time interval $\\tau$.\n3. When it turns around, it travels back toward the stationary raft at the same relative speed $v_{\\text{boat}}$.\n4. Therefore, the time taken to return to the raft is exactly equal to the time spent moving away: $t_{\\text{return}} = \\tau$.\n5. The total time elapsed from the first meeting at $A$ to the second meeting is $t_{\\text{total}} = \\tau + t_{\\text{return}} = 2\\tau$.\n\nIn the Earth reference frame:\nDuring this total time $2\\tau$, the raft has drifted downstream from $A$ by distance $l$.\n$$l = v_{\\text{flow}} \\cdot 2\\tau \\implies v_{\\text{flow}} = \\frac{l}{2\\tau}$$\n\n**Numerical Calculation:**\n$$v_{\\text{flow}} = \\frac{6.0\\text{ km}}{2 \\times 1.0\\text{ h}} = 3.0\\text{ km/h}$$",
        "tags": ["kinematics", "relative velocity", "frames of reference"]
    },
    {
        "id": "1.2",
        "title": "Average Velocity over Split Intervals",
        "difficulty": 1,
        "question": "A point traversed half the distance with a velocity $v_0$. The remaining part of the distance was covered with velocity $v_1$ for half the time, and with velocity $v_2$ for the other half of the time. Find the mean velocity of the point averaged over the whole time of motion.",
        "hints": [
            "Break the journey into two segments of distance $s/2$ each.",
            "Find the time $t_1$ for the first half of distance.",
            "For the second half of distance, express the distance in terms of $t_2$ and the two equal time halves."
        ],
        "answer": "$\\langle v \\rangle = \\frac{2v_0(v_1 + v_2)}{2v_0 + v_1 + v_2}$",
        "solution": "Let the total distance be $s$.\n\n1. **First half of the distance:**\n   $$s_1 = \\frac{s}{2}, \\quad t_1 = \\frac{s_1}{v_0} = \\frac{s}{2v_0}$$\n\n2. **Second half of the distance:**\n   Let $t_2$ be the total time for the second half. The point moves for time $t_2/2$ with velocity $v_1$ and time $t_2/2$ with velocity $v_2$:\n   $$s_2 = v_1 \\left(\\frac{t_2}{2}\\right) + v_2 \\left(\\frac{t_2}{2}\\right) = \\frac{v_1 + v_2}{2} t_2$$\n   Since $s_2 = s/2$:\n   $$t_2 = \\frac{s}{v_1 + v_2}$$\n\n3. **Total time and average velocity:**\n   $$t = t_1 + t_2 = \\frac{s}{2v_0} + \\frac{s}{v_1 + v_2} = s \\left[ \\frac{v_1 + v_2 + 2v_0}{2v_0(v_1 + v_2)} \\right]$$\n   $$\\langle v \\rangle = \\frac{s}{t} = \\frac{2v_0(v_1 + v_2)}{2v_0 + v_1 + v_2}$$",
        "tags": ["kinematics", "average velocity", "1D motion"]
    },
    {
        "id": "1.3",
        "title": "Trapezoidal Velocity-Time Profile",
        "difficulty": 1,
        "question": "A car starts moving rectilinearly, first with acceleration $w = 5.0\\text{ m/s}^2$ (the initial velocity is equal to zero), then uniformly, and finally, decelerating at the same rate $w$, comes to a stop. The total time of motion equals $\\tau = 25\\text{ s}$. The average velocity during that time is equal to $\\langle v \\rangle = 72\\text{ km/h}$. How long does the car move uniformly?",
        "hints": [
            "Draw a $v$-$t$ graph: it forms a symmetrical trapezoid.",
            "Let $t_1$ be the acceleration time (and deceleration time) and $\\Delta t$ be the uniform motion time, so $\\tau = 2t_1 + \\Delta t$.",
            "Express the maximum velocity $v_{\\max} = w t_1$ and total displacement as the trapezoid area."
        ],
        "answer": "$\\Delta t = \\tau \\sqrt{1 - \\frac{4\\langle v \\rangle}{w\\tau}} = 15\\text{ s}$",
        "solution": "Convert average velocity to SI units:\n$$\\langle v \\rangle = 72\\text{ km/h} = 20\\text{ m/s}$$\nTotal distance is $s = \\langle v \\rangle \\tau$.\n\nFrom the trapezoidal $v$-$t$ diagram:\n- Acceleration time: $t_1$\n- Deceleration time: $t_1$\n- Uniform motion time: $\\Delta t = \\tau - 2t_1$\n- Maximum velocity: $v_{\\max} = w t_1$\n\nThe area under the $v$-$t$ curve gives displacement $s$:\n$$s = \\frac{\\tau + \\Delta t}{2} v_{\\max} = \\frac{\\tau + \\Delta t}{2} \\cdot w \\left( \\frac{\\tau - \\Delta t}{2} \\right) = \\frac{w}{4} (\\tau^2 - \\Delta t^2)$$\n\nEquating to $s = \\langle v \\rangle \\tau$:\n$$\\langle v \\rangle \\tau = \\frac{w}{4} (\\tau^2 - \\Delta t^2) \\implies \\tau^2 - \\Delta t^2 = \\frac{4\\langle v \\rangle \\tau}{w}$$\n$$\\Delta t^2 = \\tau^2 \\left( 1 - \\frac{4\\langle v \\rangle}{w\\tau} \\right) \\implies \\Delta t = \\tau \\sqrt{1 - \\frac{4\\langle v \\rangle}{w\\tau}}$$\n\n**Numerical Calculation:**\n$$\\frac{4\\langle v \\rangle}{w\\tau} = \\frac{4 \\times 20}{5.0 \\times 25} = \\frac{80}{125} = 0.64$$\n$$\\Delta t = 25 \\times \\sqrt{1 - 0.64} = 25 \\times 0.6 = 15\\text{ s}$$",
        "tags": ["kinematics", "velocity-time graph", "1D motion"]
    },
    {
        "id": "1.4",
        "title": "Distance-Time Graph Analysis",
        "difficulty": 2,
        "question": "A point moves rectilinearly in one direction. The distance $s$ traversed by the point as a function of time $t$ is recorded over a total interval of $20\\text{ s}$ (starting from rest at $t=0$, covering $s = 2.0\\text{ m}$ at $t = 20\\text{ s}$, with maximum slope at $t \\approx 10\\text{ s}$). Using the plot, find:\n(a) the average velocity of the point during the total time of motion;\n(b) the maximum velocity $v_{\\max}$;\n(c) the time moment $t_0$ at which the instantaneous velocity is equal to the mean velocity averaged over the first $t_0$ seconds.",
        "hints": [
            "Mean velocity over the whole motion is simply total distance divided by total time.",
            "Maximum velocity corresponds to the maximum slope $ds/dt$ of the curve.",
            "The condition $v(t_0) = \\langle v \\rangle_{0 \\to t_0}$ means the tangent at $t_0$ passes through the origin $(0,0)$."
        ],
        "answer": "(a) $\\langle v \\rangle = 10\\text{ cm/s}$; (b) $v_{\\max} \\approx 25\\text{ cm/s}$; (c) $t_0 \\approx 16\\text{ s}$",
        "solution": "**(a) Average velocity during the total time of motion:**\n$$\\langle v \\rangle = \\frac{s_{\\text{total}}}{t_{\\text{total}}} = \\frac{2.0\\text{ m}}{20\\text{ s}} = 0.10\\text{ m/s} = 10\\text{ cm/s}$$\n\n**(b) Maximum velocity:**\nThe instantaneous velocity is $v = \\frac{ds}{dt}$. The maximum slope occurs at the inflection point ($t \\approx 10\\text{ s}$), where the steepest tangent gives:\n$$v_{\\max} \\approx 0.25\\text{ m/s} = 25\\text{ cm/s}$$\n\n**(c) Moment $t_0$ where instantaneous velocity equals average velocity:**\n$$\\langle v \\rangle_{0 \\to t_0} = \\frac{s(t_0)}{t_0}$$\nWe require $\\left.\\frac{ds}{dt}\\right|_{t_0} = \\frac{s(t_0)}{t_0}$, which means the tangent line to the $s(t)$ curve at $t = t_0$ must pass through the origin $(0,0)$. Drawing a secant from $(0,0)$ tangent to the graph yields $t_0 \\approx 16\\text{ s}$.",
        "tags": ["kinematics", "graphical analysis", "calculus"]
    },
    {
        "id": "1.5",
        "title": "Condition for Collision of Two Particles",
        "difficulty": 2,
        "question": "Two particles, 1 and 2, move with constant velocities $\\vec{v}_1$ and $\\vec{v}_2$. At the initial moment their radius vectors are equal to $\\vec{r}_1$ and $\\vec{r}_2$. How must these four vectors be interrelated for the particles to collide?",
        "hints": [
            "At collision time $t > 0$, both particles must occupy the exact same position.",
            "Set $\\vec{r}_1 + \\vec{v}_1 t = \\vec{r}_2 + \\vec{v}_2 t$.",
            "Equate unit vectors since $t > 0$ is a positive scalar."
        ],
        "answer": "$\\frac{\\vec{r}_1 - \\vec{r}_2}{|\\vec{r}_1 - \\vec{r}_2|} = \\frac{\\vec{v}_2 - \\vec{v}_1}{|\\vec{v}_2 - \\vec{v}_1|}$",
        "solution": "Let $t$ be the time of collision ($t > 0$). The position vectors at time $t$ are:\n$$\\vec{r}_1(t) = \\vec{r}_1 + \\vec{v}_1 t, \\quad \\vec{r}_2(t) = \\vec{r}_2 + \\vec{v}_2 t$$\n\nFor a collision to occur:\n$$\\vec{r}_1(t) = \\vec{r}_2(t) \\implies \\vec{r}_1 - \\vec{r}_2 = (\\vec{v}_2 - \\vec{v}_1) t$$\n\nTaking the magnitude of both sides:\n$$|\\vec{r}_1 - \\vec{r}_2| = |\\vec{v}_2 - \\vec{v}_1| t \\implies t = \\frac{|\\vec{r}_1 - \\vec{r}_2|}{|\\vec{v}_2 - \\vec{v}_1|}$$\n\nSubstituting $t$ back into the vector equation:\n$$\\vec{r}_1 - \\vec{r}_2 = (\\vec{v}_2 - \\vec{v}_1) \\frac{|\\vec{r}_1 - \\vec{r}_2|}{|\\vec{v}_2 - \\vec{v}_1|}$$\nDividing by $|\\vec{r}_1 - \\vec{r}_2|$ yields the condition of collinearity and co-direction:\n$$\\frac{\\vec{r}_1 - \\vec{r}_2}{|\\vec{r}_1 - \\vec{r}_2|} = \\frac{\\vec{v}_2 - \\vec{v}_1}{|\\vec{v}_2 - \\vec{v}_1|}$$",
        "tags": ["kinematics", "vectors", "relative motion"]
    },
    {
        "id": "1.6",
        "title": "Relative Wind Velocity on Moving Ship",
        "difficulty": 1,
        "question": "A ship moves along the equator to the east with velocity $v_0 = 30\\text{ km/h}$. The southeastern wind blows at an angle $\\varphi = 60^\\circ$ to the equator with velocity $v = 15\\text{ km/h}$. Find the wind velocity $v'$ relative to the ship and the angle $\\varphi'$ between the equator and the wind direction in the reference frame fixed to the ship.",
        "hints": [
            "Relative velocity of wind with respect to ship is $\\vec{v}' = \\vec{v} - \\vec{v}_0$.",
            "Set up coordinate axes: $\\hat{i}$ pointing East (along equator), $\\hat{j}$ pointing North.",
            "A southeast wind blows from Southeast toward Northwest."
        ],
        "answer": "$v' = \\sqrt{v_0^2 + v^2 + 2v_0 v \\cos\\varphi} \\approx 40\\text{ km/h}$, $\\varphi' \\approx 19^\\circ$",
        "solution": "Let the $x$-axis point East (along the equator) and the $y$-axis point North.\n- Ship velocity: $\\vec{v}_0 = v_0\\hat{i} = 30\\hat{i}\\text{ km/h}$.\n- Southeastern wind blows from SE toward NW (angle $\\varphi = 60^\\circ$ with the negative $x$-axis):\n  $$\\vec{v} = -v\\cos\\varphi\\hat{i} + v\\sin\\varphi\\hat{j}$$\n\nThe velocity of wind relative to the ship is:\n$$\\vec{v}' = \\vec{v} - \\vec{v}_0 = -(v_0 + v\\cos\\varphi)\\hat{i} + v\\sin\\varphi\\hat{j}$$\n\n1. **Magnitude of relative wind:**\n   $$v' = \\sqrt{(v_0 + v\\cos\\varphi)^2 + (v\\sin\\varphi)^2} = \\sqrt{v_0^2 + v^2 + 2v_0 v\\cos\\varphi}$$\n   $$v' = \\sqrt{30^2 + 15^2 + 2(30)(15)\\cos 60^\\circ} = \\sqrt{900 + 225 + 450} = \\sqrt{1575} \\approx 39.7\\text{ km/h} \\approx 40\\text{ km/h}$$\n\n2. **Angle $\\varphi'$ with the equator:**\n   $$\\tan\\varphi' = \\frac{|v'_y|}{|v'_x|} = \\frac{v\\sin\\varphi}{v_0 + v\\cos\\varphi} = \\frac{15\\sin 60^\\circ}{30 + 15\\cos 60^\\circ} = \\frac{15 \\times 0.866}{37.5} = 0.3464$$\n   $$\\varphi' = \\arctan(0.3464) \\approx 19.1^\\circ \\approx 19^\\circ$$",
        "tags": ["kinematics", "relative velocity", "vectors"]
    },
    {
        "id": "1.7",
        "title": "Two Swimmers Crossing a River",
        "difficulty": 2,
        "question": "Two swimmers leave point $A$ on one bank of a river to reach point $B$ lying right across on the opposite bank. One of them crosses along the straight line $AB$, while the other swims at right angles to the stream and then walks the distance carried away downstream to get to point $B$. What was the velocity $u$ of his walking if both swimmers reached $B$ simultaneously? Stream velocity $v_0 = 2.0\\text{ km/h}$, swimmer speed in water $v' = 2.5\\text{ km/h}$.",
        "hints": [
            "For the first swimmer, heading must compensate for drift: resultant velocity is $\\sqrt{v'^2 - v_0^2}$.",
            "For the second swimmer, time crossing is $d / v'$, and drift distance is $x = v_0 t_{\\text{swim}}$.",
            "Equate the two total times: $t_1 = t_2$."
        ],
        "answer": "$u = \\frac{v_0}{\\frac{v'}{\\sqrt{v'^2 - v_0^2}} - 1} = 3.0\\text{ km/h}$",
        "solution": "Let the river width be $d$.\n\n1. **First swimmer (straight path $AB$):**\n   To move perpendicular to the bank, the swimmer aims upstream at angle $\\sin\\theta = v_0/v'$.\n   Resultant speed across the river:\n   $$v_1 = \\sqrt{v'^2 - v_0^2}$$\n   Time taken:\n   $$t_1 = \\frac{d}{\\sqrt{v'^2 - v_0^2}}$$\n\n2. **Second swimmer (perpendicular heading + walk):**\n   Swimming time:\n   $$t_{\\text{swim}} = \\frac{d}{v'}$$\n   Drift distance downstream:\n   $$x = v_0 t_{\\text{swim}} = \\frac{v_0 d}{v'}$$\n   Walking time back to $B$ at speed $u$:\n   $$t_{\\text{walk}} = \\frac{x}{u} = \\frac{v_0 d}{u v'}$$\n   Total time:\n   $$t_2 = \\frac{d}{v'} + \\frac{v_0 d}{u v'} = \\frac{d}{v'}\\left(1 + \\frac{v_0}{u}\\right)$$\n\n3. **Equating $t_1 = t_2$:**\n   $$\\frac{d}{\\sqrt{v'^2 - v_0^2}} = \\frac{d}{v'}\\left(1 + \\frac{v_0}{u}\\right)$$\n   $$1 + \\frac{v_0}{u} = \\frac{v'}{\\sqrt{v'^2 - v_0^2}} \\implies u = \\frac{v_0}{\\frac{v'}{\\sqrt{v'^2 - v_0^2}} - 1}$$\n\n**Numerical Calculation:**\n$$\\sqrt{v'^2 - v_0^2} = \\sqrt{2.5^2 - 2.0^2} = \\sqrt{6.25 - 4.0} = 1.5\\text{ km/h}$$\n$$\\frac{v'}{\\sqrt{v'^2 - v_0^2}} = \\frac{2.5}{1.5} = \\frac{5}{3}$$\n$$u = \\frac{2.0}{5/3 - 1} = \\frac{2.0}{2/3} = 3.0\\text{ km/h}$$",
        "tags": ["kinematics", "relative motion", "river crossing"]
    },
    {
        "id": "1.8",
        "title": "Two Boats Along and Across Stream",
        "difficulty": 2,
        "question": "Two boats, $A$ and $B$, move away from a buoy anchored in the middle of a river along mutually perpendicular straight lines: boat $A$ along the river, and boat $B$ across the river. Having moved off an equal distance $l$ from the buoy, both boats return. Find the ratio of times of motion $\\tau_A / \\tau_B$ if the velocity of each boat relative to water is $\\eta = 1.2$ times greater than the stream velocity.",
        "hints": [
            "Let stream velocity be $v_0$, then boat speed relative to water is $v = \\eta v_0$.",
            "Calculate round-trip time along the river: $\\tau_A = \\frac{l}{\\eta v_0 + v_0} + \\frac{l}{\\eta v_0 - v_0}$.",
            "Calculate round-trip time across the river: $\\tau_B = \\frac{2l}{\\sqrt{(\\eta v_0)^2 - v_0^2}}$."
        ],
        "answer": "$\\frac{\\tau_A}{\\tau_B} = \\frac{\\eta}{\\sqrt{\\eta^2 - 1}} = 1.8$",
        "solution": "Let stream velocity be $v_0$. The boat speed in water is $v = \\eta v_0$.\n\n1. **Boat $A$ (along stream round-trip):**\n   Downstream speed: $v + v_0 = (\\eta + 1)v_0$.\n   Upstream speed: $v - v_0 = (\\eta - 1)v_0$.\n   $$\\tau_A = \\frac{l}{(\\eta + 1)v_0} + \\frac{l}{(\\eta - 1)v_0} = \\frac{l}{v_0}\\left[\\frac{(\\eta - 1) + (\\eta + 1)}{\\eta^2 - 1}\\right] = \\frac{2l\\eta}{v_0(\\eta^2 - 1)}$$\n\n2. **Boat $B$ (across stream round-trip):**\n   Resultant speed perpendicular to stream both ways: $\\sqrt{v^2 - v_0^2} = v_0\\sqrt{\\eta^2 - 1}$.\n   $$\\tau_B = \\frac{2l}{v_0\\sqrt{\\eta^2 - 1}}$$\n\n3. **Ratio of times:**\n   $$\\frac{\\tau_A}{\\tau_B} = \\frac{\\frac{2l\\eta}{v_0(\\eta^2 - 1)}}{\\frac{2l}{v_0\\sqrt{\\eta^2 - 1}}} = \\frac{\\eta}{\\sqrt{\\eta^2 - 1}}$$\n\n**Numerical Calculation:**\nFor $\\eta = 1.2$:\n$$\\sqrt{\\eta^2 - 1} = \\sqrt{1.44 - 1} = \\sqrt{0.44} \\approx 0.6633$$\n$$\\frac{\\tau_A}{\\tau_B} = \\frac{1.2}{0.6633} \\approx 1.8$$",
        "tags": ["kinematics", "relative velocity", "river motion"]
    },
    {
        "id": "1.9",
        "title": "Minimum Drift River Crossing",
        "difficulty": 2,
        "question": "A boat moves relative to water with a velocity which is $n = 2.0$ times less than the river flow velocity ($v = v_0 / n$). At what angle $\\theta$ to the stream direction must the boat move to minimize drifting?",
        "hints": [
            "Since boat speed is less than flow speed ($v < v_0$), drift cannot be zero.",
            "Write the drift $x$ in terms of river width $d$ and angle $\\theta$, or use velocity vector geometry.",
            "In velocity space, the resultant velocity vector $\\vec{v}_{\\text{res}} = \\vec{v}_0 + \\vec{v}$ traces a circle of radius $v$. Minimum drift corresponds to the tangent to this circle from the origin."
        ],
        "answer": "$\\theta = \\frac{\\pi}{2} + \\arcsin\\left(\\frac{1}{n}\\right) = 120^\\circ$",
        "solution": "**Method: Velocity Vector Geometry**\n\n1. Let flow velocity be $\\vec{v}_0$ along the $+x$-axis.\n2. Boat velocity relative to water has magnitude $v = v_0 / n$, making angle $\\alpha$ with the upstream direction (or angle $\\theta = \\pi - \\alpha$ with the downstream direction).\n3. In velocity space, the resultant velocity is $\\vec{V} = \\vec{v}_0 + \\vec{v}$. The vector $\\vec{v}$ can point in any direction on a circle of radius $v$ centered at the tip of $\\vec{v}_0$.\n4. The direction of motion across the river has angle $\\phi$ with the river bank, where $\\tan\\phi = \\frac{V_y}{V_x}$. To minimize drift $x = d / \\tan\\phi$, we must maximize $\\tan\\phi$, which means maximizing $\\phi$.\n5. Geometrically, the line from the origin tangent to the circle of radius $v = v_0/n$ gives the maximum angle $\\phi$. At tangency, the vector $\\vec{v}$ is perpendicular to the resultant velocity $\\vec{V}$:\n   $$\\sin\\alpha = \\frac{v}{v_0} = \\frac{1}{n}$$\n6. The angle with the downstream flow direction is:\n   $$\\theta = \\frac{\\pi}{2} + \\alpha = \\frac{\\pi}{2} + \\arcsin\\left(\\frac{1}{n}\\right)$$\n\n**Numerical Calculation:**\nFor $n = 2.0$:\n$$\\arcsin(1/2) = 30^\\circ \\implies \\theta = 90^\\circ + 30^\\circ = 120^\\circ$$",
        "tags": ["kinematics", "optimization", "vectors", "river crossing"]
    },
    {
        "id": "1.10",
        "title": "Distance Between Two Projectiles",
        "difficulty": 2,
        "question": "Two bodies were thrown simultaneously from the same point; one, straight up, and the other, at an angle of $\\theta = 60^\\circ$ to the horizontal. The initial velocity of each body is equal to $v_0 = 25\\text{ m/s}$. Neglecting air drag, find the distance between the bodies $t = 1.70\\text{ s}$ later.",
        "hints": [
            "Consider the relative motion of the two projectiles.",
            "Since both experience the exact same acceleration $\\vec{g}$, what is their relative acceleration?",
            "Relative velocity is constant: $\\vec{v}_{\\text{rel}} = \\vec{v}_1 - \\vec{v}_2$."
        ],
        "answer": "$l = v_0 t \\sqrt{2(1 - \\sin\\theta)} = 22\\text{ m}$",
        "solution": "1. **Relative Acceleration:**\n   Both bodies move in free fall under gravity:\n   $$\\vec{w}_1 = \\vec{g}, \\quad \\vec{w}_2 = \\vec{g} \\implies \\vec{w}_{\\text{rel}} = \\vec{w}_1 - \\vec{w}_2 = 0$$\n   Because relative acceleration is zero, the relative motion is purely uniform rectilinear motion with constant relative velocity $\\vec{v}_{\\text{rel}} = \\vec{v}_1(0) - \\vec{v}_2(0)$.\n\n2. **Relative Velocity Magnitude:**\n   - Body 1 (straight up): $\\vec{v}_1(0) = v_0\\hat{j}$.\n   - Body 2 (angle $\\theta$): $\\vec{v}_2(0) = v_0\\cos\\theta\\hat{i} + v_0\\sin\\theta\\hat{j}$.\n   $$\\vec{v}_{\\text{rel}} = -v_0\\cos\\theta\\hat{i} + v_0(1 - \\sin\\theta)\\hat{j}$$\n   $$v_{\\text{rel}}^2 = v_0^2\\cos^2\\theta + v_0^2(1 - \\sin\\theta)^2 = v_0^2 [\\cos^2\\theta + 1 - 2\\sin\\theta + \\sin^2\\theta] = 2v_0^2(1 - \\sin\\theta)$$\n   $$v_{\\text{rel}} = v_0 \\sqrt{2(1 - \\sin\\theta)}$$\n\n3. **Distance at time $t$:**\n   $$l = v_{\\text{rel}} t = v_0 t \\sqrt{2(1 - \\sin\\theta)}$$\n\n**Numerical Calculation:**\n$$l = 25 \\times 1.70 \\times \\sqrt{2(1 - \\sin 60^\\circ)} = 42.5 \\times \\sqrt{2(1 - 0.8660)} = 42.5 \\times \\sqrt{0.2679} = 42.5 \\times 0.5176 \\approx 22\\text{ m}$$",
        "tags": ["kinematics", "projectile motion", "relative motion"]
    },
    {
        "id": "1.11",
        "title": "Horizontally Projected Particles Separation",
        "difficulty": 2,
        "question": "Two particles move in a uniform gravitational field with acceleration $g$. At the initial moment the particles were located at one point and moved with velocities $v_1 = 3.0\\text{ m/s}$ and $v_2 = 4.0\\text{ m/s}$ horizontally in opposite directions. Find the distance between the particles at the moment when their velocity vectors become mutually perpendicular.",
        "hints": [
            "Write the velocity vectors $\\vec{v}_1(t)$ and $\\vec{v}_2(t)$ as functions of time.",
            "Condition for perpendicularity: $\\vec{v}_1 \\cdot \\vec{v}_2 = 0$.",
            "Once time $t$ is found, find the separation $\\Delta x$ and $\\Delta y$ between the particles."
        ],
        "answer": "$l = \\frac{v_1 + v_2}{g}\\sqrt{v_1 v_2} = 2.5\\text{ m}$",
        "solution": "1. **Velocity vectors as functions of time:**\n   $$\\vec{v}_1 = -v_1\\hat{i} + gt\\hat{j}, \\quad \\vec{v}_2 = v_2\\hat{i} + gt\\hat{j}$$\n\n2. **Condition for mutual perpendicularity:**\n   $$\\vec{v}_1 \\cdot \\vec{v}_2 = 0 \\implies (-v_1)(v_2) + (gt)(gt) = 0$$\n   $$g^2 t^2 = v_1 v_2 \\implies t = \\frac{\\sqrt{v_1 v_2}}{g}$$\n\n3. **Distance between particles:**\n   Since both particles fall with identical vertical acceleration from the same height, their vertical coordinates are identical at all times: $y_1(t) = y_2(t) = \\frac{1}{2}gt^2$.\n   The distance between them is purely horizontal:\n   $$l = |x_2 - x_1| = (v_1 + v_2)t = \\frac{v_1 + v_2}{g}\\sqrt{v_1 v_2}$$\n\n**Numerical Calculation:**\n$$l = \\frac{3.0 + 4.0}{9.8} \\sqrt{3.0 \\times 4.0} = \\frac{7.0 \\times \\sqrt{12}}{9.8} = \\frac{7.0 \\times 3.464}{9.8} = \\frac{24.25}{9.8} \\approx 2.5\\text{ m}$$",
        "tags": ["kinematics", "projectile motion", "vectors"]
    },
    {
        "id": "1.12",
        "title": "Three Pursuing Particles on Triangle",
        "difficulty": 2,
        "question": "Three points are located at the vertices of an equilateral triangle whose side equals $a$. They all start moving simultaneously with velocity $v$ constant in modulus, with the first point heading continually for the second, the second for the third, and the third for the first. How soon will the points converge?",
        "hints": [
            "By symmetry, the three points form a shrinking equilateral triangle that rotates.",
            "Consider the rate at which the distance between any two adjacent points decreases.",
            "At any instant, what is the projection of the velocity of the chased point onto the line connecting them?"
        ],
        "answer": "$t = \\frac{2a}{3v}$",
        "solution": "1. **Symmetry:**\n   Due to three-fold rotational symmetry, the three points always form an equilateral triangle of side length $r(t)$ with center at the centroid.\n\n2. **Relative approach rate:**\n   Consider points 1 and 2. Point 1 moves directly toward point 2 with speed $v$.\n   Point 2 moves toward point 3 at speed $v$, which makes an angle of $120^\\circ$ with the vector from 1 to 2 (exterior angle of equilateral triangle is $120^\\circ$, or angle between $\\vec{v}_2$ and line $1 \\to 2$ is $180^\\circ - 60^\\circ = 120^\\circ$).\n   The projection of velocity of point 2 along the line pointing away from 1 is $v\\cos 60^\\circ = v/2$.\n   Therefore, the rate at which the distance $r$ between points 1 and 2 decreases is:\n   $$-\\frac{dr}{dt} = v - v\\cos 120^\\circ = v - v\\left(-\\frac{1}{2}\\right) = v + \\frac{v}{2} = \\frac{3}{2}v$$\n\n3. **Time to converge:**\n   $$t = \\frac{a}{-\\frac{dr}{dt}} = \\frac{a}{\\frac{3}{2}v} = \\frac{2a}{3v}$$",
        "tags": ["kinematics", "pursuit problem", "symmetry"]
    },
    {
        "id": "1.13",
        "title": "Pursuit Problem (Point A Aimed at Moving B)",
        "difficulty": 3,
        "question": "Point $A$ moves uniformly with velocity $v$ so that the vector $\\vec{v}$ is continually aimed at point $B$ which in its turn moves rectilinearly and uniformly with velocity $u < v$. At the initial moment of time $\\vec{v} \\perp \\vec{u}$ and the points are separated by a distance $l$. How soon will the points converge?",
        "hints": [
            "Let the line connecting $A$ and $B$ make an angle $\\alpha(t)$ with the direction of motion of $B$.",
            "Write the rate of change of distance $r(t)$ between $A$ and $B$: $-dr/dt = v - u\\cos\\alpha$.",
            "Write the projection of displacement of $A$ along the direction of motion of $B$: $\\int v\\cos\\alpha\\, dt = u\\tau$."
        ],
        "answer": "$\\tau = \\frac{vl}{v^2 - u^2}$",
        "solution": "Let $r(t)$ be the separation between $A$ and $B$, and $\\alpha(t)$ be the angle between $\\vec{u}$ and the line from $A$ to $B$.\n\n1. **Rate of approach:**\n   Point $A$ moves toward $B$ with speed $v$, while point $B$ moves away with component $u\\cos\\alpha$ along the line of sight:\n   $$-\\frac{dr}{dt} = v - u\\cos\\alpha$$\n   Integrating from $t = 0$ to $t = \\tau$ (where $r(0) = l$ and $r(\\tau) = 0$):\n   $$\\int_0^l dr = \\int_0^\\tau (v - u\\cos\\alpha)\\,dt \\implies l = v\\tau - u\\int_0^\\tau \\cos\\alpha\\,dt \\quad \\text{--- (1)}$$\n\n2. **Displacement along the direction of $\\vec{u}$:**\n   Point $B$ moves with constant velocity $u$, so its total displacement is $u\\tau$.\n   Point $A$ catches up with $B$, so the displacement of $A$ along the direction of $\\vec{u}$ must equal the displacement of $B$ (since initially $\\vec{v} \\perp \\vec{u}$, so initial separation along $\\vec{u}$ is zero):\n   $$\\int_0^\\tau v\\cos\\alpha\\,dt = u\\tau \\implies \\int_0^\\tau \\cos\\alpha\\,dt = \\frac{u\\tau}{v} \\quad \\text{--- (2)}$$\n\n3. **Combining (1) and (2):**\n   $$l = v\\tau - u\\left(\\frac{u\\tau}{v}\\right) = \\frac{v^2 - u^2}{v}\\tau$$\n   $$\\tau = \\frac{vl}{v^2 - u^2}$$",
        "tags": ["kinematics", "pursuit problem", "integration"]
    },
    {
        "id": "1.14",
        "title": "Events on an Accelerating Train",
        "difficulty": 2,
        "question": "A train of length $l = 350\\text{ m}$ starts moving rectilinearly with constant acceleration $w = 3.0\\times 10^{-2}\\text{ m/s}^2$; $t = 30\\text{ s}$ after the start the locomotive headlight is switched on (event 1), and $\\tau = 60\\text{ s}$ after that event the tail signal light is switched on (event 2). Find the distance between these events in the reference frames fixed to the train and the Earth. At what constant velocity $V$ relative to the Earth must a reference frame $K$ move for the two events to occur in it at the same point?",
        "hints": [
            "In the train frame, the headlight is at the front and tail light is at the rear, separated by train length $l$.",
            "In the Earth frame, calculate the coordinate of event 1 at $t_1 = t$ and event 2 at $t_2 = t + \\tau$.",
            "For events to occur at the same spatial point in frame $K$, frame $K$ must travel distance $\\Delta x_{\\text{Earth}}$ in time $\\tau$."
        ],
        "answer": "In train frame: $\\Delta x' = l = 350\\text{ m}$; in Earth frame: $\\Delta x = l - w\\tau(t + \\tau/2) = 0.24\\text{ km}$; frame speed: $V = 4.0\\text{ m/s}$ towards the train.",
        "solution": "1. **In train's reference frame:**\n   The headlight is at the front and tail light is at the back. Both lights are rigidly attached to the train, separated by its length:\n   $$\\Delta x' = l = 350\\text{ m}$$\n\n2. **In Earth's reference frame:**\n   Let the rear of the train be at $x = 0$ at $t = 0$. The train accelerates with $w$.\n   - Event 1 occurs at time $t_1 = t = 30\\text{ s}$ at the front of the train:\n     $$x_1 = \\frac{1}{2}wt^2 + l$$\n   - Event 2 occurs at time $t_2 = t + \\tau = 30 + 60 = 90\\text{ s}$ at the rear of the train:\n     $$x_2 = \\frac{1}{2}w(t + \\tau)^2$$\n   The distance between the two events in the Earth frame is:\n   $$\\Delta x = x_1 - x_2 = l + \\frac{1}{2}wt^2 - \\frac{1}{2}w(t + \\tau)^2 = l - w\\tau\\left(t + \\frac{\\tau}{2}\\right)$$\n   **Numerical value:**\n   $$\\Delta x = 350 - 0.030 \\times 60 \\times (30 + 30) = 350 - 1.8 \\times 60 = 350 - 108 = 242\\text{ m} \\approx 0.24\\text{ km}$$\n\n3. **Velocity of reference frame $K$:**\n   In frame $K$, the two events occur at the same point, so $\\Delta x_K = 0$.\n   Since $\\Delta x_K = \\Delta x - V\\tau = 0$:\n   $$V = \\frac{\\Delta x}{\\tau} = \\frac{242\\text{ m}}{60\\text{ s}} \\approx 4.0\\text{ m/s}$$\n   Directed along the direction opposite to train acceleration (towards the train).",
        "tags": ["kinematics", "frames of reference", "relativity of position"]
    },
    {
        "id": "1.15",
        "title": "Falling Bolt in Ascending Elevator",
        "difficulty": 2,
        "question": "An elevator car whose floor-to-ceiling distance is $h = 2.7\\text{ m}$ starts ascending with constant acceleration $w = 1.2\\text{ m/s}^2$; $t_0 = 2.0\\text{ s}$ after the start a bolt begins falling from the ceiling of the car. Find:\n(a) the bolt's free fall time;\n(b) the displacement and the distance covered by the bolt during the free fall in the reference frame fixed to the elevator shaft.",
        "hints": [
            "Use the non-inertial frame of the elevator where effective gravity is $g_{\\text{eff}} = g + w$.",
            "In the elevator frame, the bolt falls distance $h$ from rest relative to the elevator.",
            "In the ground frame, the bolt starts with upward velocity $v_0 = w t_0$."
        ],
        "answer": "(a) $t = \\sqrt{\\frac{2h}{g+w}} = 0.70\\text{ s}$; (b) displacement $\\Delta y = 0.7\\text{ m}$, distance $s = 1.3\\text{ m}$",
        "solution": "**(a) Free fall time:**\nIn the frame of the accelerating elevator, the effective downward acceleration is $g_{\\text{eff}} = g + w = 9.8 + 1.2 = 11.0\\text{ m/s}^2$.\n$$h = \\frac{1}{2}(g + w)t^2 \\implies t = \\sqrt{\\frac{2h}{g + w}} = \\sqrt{\\frac{2 \\times 2.7}{11.0}} = \\sqrt{0.4909} \\approx 0.70\\text{ s}$$\n\n**(b) In the shaft (Earth) reference frame:**\nAt the instant of detachment ($t_0 = 2.0\\text{ s}$), the bolt has an upward initial velocity:\n$$v_0 = w t_0 = 1.2 \\times 2.0 = 2.4\\text{ m/s}$$\n\n1. **Displacement:**\n   $$\\Delta y = v_0 t - \\frac{1}{2}gt^2 = 2.4(0.70) - \\frac{1}{2}(9.8)(0.70)^2 = 1.68 - 2.40 = -0.72\\text{ m}$$\n   Modulus of displacement is $0.72\\text{ m} \\approx 0.7\\text{ m}$ downward.\n\n2. **Total distance covered:**\n   The bolt first rises to its maximum height, then falls back:\n   $$h_{\\text{rise}} = \\frac{v_0^2}{2g} = \\frac{2.4^2}{2 \\times 9.8} = \\frac{5.76}{19.6} \\approx 0.29\\text{ m}$$\n   Total distance is:\n   $$s = 2h_{\\text{rise}} + |\\Delta y| = 2(0.29) + 0.72 = 0.58 + 0.72 = 1.30\\text{ m} \\approx 1.3\\text{ m}$$",
        "tags": ["kinematics", "accelerated frames", "free fall"]
    },
    {
        "id": "1.16",
        "title": "Minimum Distance Between Two Perpendicular Movers",
        "difficulty": 2,
        "question": "Two particles, 1 and 2, move with constant velocities $v_1$ and $v_2$ along two mutually perpendicular straight lines toward the intersection point $O$. At $t = 0$ the particles were at distances $l_1$ and $l_2$ from $O$. How soon will the distance between the particles become the smallest? What is it equal to?",
        "hints": [
            "Write the coordinates of the particles as functions of time: $x_1(t) = l_1 - v_1 t$ and $y_2(t) = l_2 - v_2 t$.",
            "Express distance squared: $l^2(t) = (l_1 - v_1 t)^2 + (l_2 - v_2 t)^2$.",
            "Minimize with respect to $t$ by setting $d(l^2)/dt = 0$."
        ],
        "answer": "$t_{\\min} = \\frac{v_1 l_1 + v_2 l_2}{v_1^2 + v_2^2}$, $l_{\\min} = \\frac{|v_1 l_2 - v_2 l_1|}{\\sqrt{v_1^2 + v_2^2}}$",
        "solution": "Let the path of particle 1 be along the $x$-axis and particle 2 along the $y$-axis:\n$$x(t) = l_1 - v_1 t, \\quad y(t) = l_2 - v_2 t$$\n\nThe squared distance between them is:\n$$l^2(t) = (l_1 - v_1 t)^2 + (l_2 - v_2 t)^2 = (v_1^2 + v_2^2)t^2 - 2(v_1 l_1 + v_2 l_2)t + (l_1^2 + l_2^2)$$\n\n1. **Time of minimum separation:**\n   Differentiating with respect to $t$ and setting to zero:\n   $$\\frac{d(l^2)}{dt} = 2(v_1^2 + v_2^2)t - 2(v_1 l_1 + v_2 l_2) = 0$$\n   $$t_{\\min} = \\frac{v_1 l_1 + v_2 l_2}{v_1^2 + v_2^2}$$\n\n2. **Minimum separation distance:**\n   Substituting $t_{\\min}$ into $l^2$:\n   $$l_{\\min}^2 = (l_1^2 + l_2^2) - \\frac{(v_1 l_1 + v_2 l_2)^2}{v_1^2 + v_2^2} = \\frac{(l_1^2 + l_2^2)(v_1^2 + v_2^2) - (v_1 l_1 + v_2 l_2)^2}{v_1^2 + v_2^2}$$\n   $$= \\frac{v_1^2 l_2^2 + v_2^2 l_1^2 - 2v_1 v_2 l_1 l_2}{v_1^2 + v_2^2} = \\frac{(v_1 l_2 - v_2 l_1)^2}{v_1^2 + v_2^2}$$\n   $$l_{\\min} = \\frac{|v_1 l_2 - v_2 l_1|}{\\sqrt{v_1^2 + v_2^2}}$$",
        "tags": ["kinematics", "optimization", "relative motion"]
    },
    {
        "id": "1.17",
        "title": "Fermat's Principle for Highway and Field Route",
        "difficulty": 2,
        "question": "From point $A$ located on a straight highway, a car must travel as quickly as possible to point $B$ located in an adjacent field at a perpendicular distance $l$ from the highway. In the field the car moves $\\eta$ times slower than on the highway ($v_{\\text{field}} = v/\\eta$). At what distance $CD$ from point $D$ (the perpendicular projection of $B$ onto the highway) must the car turn off the highway?",
        "hints": [
            "This is directly analogous to Snell's law of refraction (Fermat's principle of least time).",
            "Let the turn-off point $C$ be at distance $x$ from $D$. The distance in the field is $\\sqrt{l^2 + x^2}$.",
            "Write total time $t(x)$ and minimize with respect to $x$."
        ],
        "answer": "$CD = \\frac{l}{\\sqrt{\\eta^2 - 1}}$",
        "solution": "Let the highway run along the $x$-axis, with point $D$ at the origin $(0,0)$ and point $B$ in the field at $(0, l)$. Point $A$ is on the highway at $(-L, 0)$.\nLet the car turn off the highway at point $C$ at distance $x = CD$ before $D$, so $C$ is at $(-x, 0)$.\n\n1. **Travel times:**\n   - Distance on highway $AC = L - x$ with speed $v$:\n     $$t_{\\text{highway}} = \\frac{L - x}{v}$$\n   - Distance in field $CB = \\sqrt{l^2 + x^2}$ with speed $v/\\eta$:\n     $$t_{\\text{field}} = \\frac{\\sqrt{l^2 + x^2}}{v/\\eta} = \\frac{\\eta \\sqrt{l^2 + x^2}}{v}$$\n   - Total travel time:\n     $$t(x) = \\frac{L - x}{v} + \\frac{\\eta \\sqrt{l^2 + x^2}}{v}$$\n\n2. **Minimizing total time:**\n   $$\\frac{dt}{dx} = -\\frac{1}{v} + \\frac{\\eta x}{v\\sqrt{l^2 + x^2}} = 0$$\n   $$\\frac{\\eta x}{\\sqrt{l^2 + x^2}} = 1 \\implies \\eta^2 x^2 = l^2 + x^2$$\n   $$x^2(\\eta^2 - 1) = l^2 \\implies x = \\frac{l}{\\sqrt{\\eta^2 - 1}}$$\n\nThus, the distance from point $D$ is $CD = \\frac{l}{\\sqrt{\\eta^2 - 1}}$.",
        "tags": ["kinematics", "optimization", "Fermat's principle"]
    },
    {
        "id": "1.18",
        "title": "Velocity Graph to Acceleration and Coordinate Plots",
        "difficulty": 2,
        "question": "A point travels along the $x$-axis with a velocity whose projection $v_x$ is presented as a function of time $t$ by a given plot. Assuming the coordinate of the point $x = 0$ at $t = 0$, determine the time dependence relations for the acceleration $w_x$, the coordinate $x$, and the distance covered $s$.",
        "hints": [
            "Instantaneous acceleration is the derivative of velocity: $w_x = dv_x/dt$.",
            "Coordinate is the integral of velocity: $x(t) = \\int_0^t v_x(t')\\,dt'$.",
            "Distance covered is the integral of speed: $s(t) = \\int_0^t |v_x(t')|\\,dt'$."
        ],
        "answer": "$w_x = \\frac{dv_x}{dt}$, $x = \\int_0^t v_x\\,dt$, $s = \\int_0^t |v_x|\\,dt$",
        "solution": "1. **Acceleration $w_x(t)$:**\n   Given by the slope of the $v_x(t)$ curve:\n   $$w_x = \\frac{dv_x}{dt}$$\n   On linear intervals of $v_x(t)$, $w_x$ is piecewise constant; where $v_x$ is constant, $w_x = 0$.\n\n2. **Coordinate $x(t)$:**\n   $$x(t) = x(0) + \\int_0^t v_x(t')\\,dt'$$\n   Geometrically, $x(t)$ equals the net signed area under the $v_x(t)$ curve from $0$ to $t$.\n\n3. **Distance covered $s(t)$:**\n   $$s(t) = \\int_0^t |v_x(t')|\\,dt'$$\n   Geometrically, $s(t)$ equals the total absolute area between the $v_x(t)$ curve and the time axis. It is monotonically non-decreasing.",
        "tags": ["kinematics", "calculus", "graphs"]
    },
    {
        "id": "1.19",
        "title": "Semicircular Motion Average Quantities",
        "difficulty": 2,
        "question": "A point traversed half a circle of radius $R = 160\\text{ cm}$ during time interval $\\tau = 10.0\\text{ s}$. Calculate the following quantities averaged over that time:\n(a) the mean speed $\\langle v \\rangle$;\n(b) the modulus of the mean velocity vector $|\\langle \\vec{v} \\rangle|$;\n(c) the modulus of the mean vector of total acceleration $|\\langle \\vec{w} \\rangle|$ if the point moved with constant tangential acceleration.",
        "hints": [
            "Path length along semicircle is $\\pi R$, while straight-line displacement is $2R$.",
            "Mean speed is path length divided by $\\tau$; mean velocity modulus is displacement divided by $\\tau$.",
            "Mean acceleration vector is $\\langle \\vec{w} \\rangle = \\frac{\\vec{v}(\\tau) - \\vec{v}(0)}{\\tau}$."
        ],
        "answer": "(a) $\\langle v \\rangle = \\frac{\\pi R}{\\tau} = 50\\text{ cm/s}$; (b) $|\\langle \\vec{v} \\rangle| = \\frac{2R}{\\tau} = 32\\text{ cm/s}$; (c) $|\\langle \\vec{w} \\rangle| = \\frac{2\\pi R}{\\tau^2} = 10\\text{ cm/s}^2$",
        "solution": "**(a) Mean speed:**\n$$\\langle v \\rangle = \\frac{s}{\\tau} = \\frac{\\pi R}{\\tau} = \\frac{\\pi \\times 160}{10.0} \\approx 50.3\\text{ cm/s} \\approx 50\\text{ cm/s}$$\n\n**(b) Modulus of mean velocity vector:**\nDisplacement magnitude is the diameter $2R$:\n$$|\\langle \\vec{v} \\rangle| = \\frac{|\\Delta \\vec{r}|}{\\tau} = \\frac{2R}{\\tau} = \\frac{2 \\times 160}{10.0} = 32\\text{ cm/s}$$\n\n**(c) Modulus of mean total acceleration vector:**\nFor motion with constant tangential acceleration starting from rest ($v(0) = 0$), $s = \\frac{1}{2}w_\\tau \\tau^2 = \\pi R \\implies w_\\tau = \\frac{2\\pi R}{\\tau^2}$.\nThe final speed is $v(\\tau) = w_\\tau \\tau = \\frac{2\\pi R}{\\tau}$.\nThe mean acceleration vector is:\n$$\\langle \\vec{w} \\rangle = \\frac{\\vec{v}(\\tau) - \\vec{v}(0)}{\\tau} = \\frac{\\vec{v}(\\tau)}{\\tau}$$\n$$|\\langle \\vec{w} \\rangle| = \\frac{v(\\tau)}{\\tau} = \\frac{2\\pi R}{\\tau^2} = \\frac{2\\pi \\times 160}{100} \\approx 10.1\\text{ cm/s}^2 \\approx 10\\text{ cm/s}^2$$",
        "tags": ["kinematics", "circular motion", "average velocity", "vectors"]
    },
    {
        "id": "1.20",
        "title": "Quadratic Radius Vector Motion",
        "difficulty": 2,
        "question": "A radius vector of a particle varies with time $t$ as $\\vec{r} = \\vec{a}t(1 - \\alpha t)$, where $\\vec{a}$ is a constant vector and $\\alpha$ is a positive constant. Find:\n(a) the velocity $\\vec{v}$ and the acceleration $\\vec{w}$ of the particle as functions of time;\n(b) the time interval $\\Delta t$ taken by the particle to return to the initial point, and the distance $s$ covered during that time.",
        "hints": [
            "Differentiate $\\vec{r}(t)$ once for velocity and twice for acceleration.",
            "Particle returns to origin when $\\vec{r}(t) = 0$ for $t > 0$.",
            "Velocity reverses direction when $\\vec{v}(t) = 0$ at $t = 1/(2\\alpha)$."
        ],
        "answer": "(a) $\\vec{v} = \\vec{a}(1 - 2\\alpha t)$, $\\vec{w} = -2\\alpha \\vec{a} = \\text{const}$; (b) $\\Delta t = 1/\\alpha$, $s = a/(2\\alpha)$",
        "solution": "**(a) Velocity and acceleration:**\n$$\\vec{v} = \\frac{d\\vec{r}}{dt} = \\vec{a}(1 - 2\\alpha t)$$\n$$\\vec{w} = \\frac{d\\vec{v}}{dt} = -2\\alpha\\vec{a} = \\text{constant}$$\n\n**(b) Return time and distance covered:**\n- The particle is at the origin $\\vec{r} = 0$ when $t(1 - \\alpha t) = 0$.\n  The non-zero root gives the return time:\n  $$\\Delta t = \\frac{1}{\\alpha}$$\n- The particle stops and turns around when $\\vec{v} = 0$, which occurs at $t_1 = \\frac{1}{2\\alpha}$.\n  Distance from origin to turnaround point:\n  $$r_{\\max} = |\\vec{r}(t_1)| = a \\left(\\frac{1}{2\\alpha}\\right)\\left(1 - \\frac{1}{2}\\right) = \\frac{a}{4\\alpha}$$\n  The total distance covered during $\\Delta t$ (out and back) is:\n  $$s = 2 r_{\\max} = 2 \\left(\\frac{a}{4\\alpha}\\right) = \\frac{a}{2\\alpha}$$",
        "tags": ["kinematics", "vectors", "calculus"]
    }
]
