"""
part3_ch3_2a.py
Curated problems 3.54 to 3.75 (22 problems) of Irodov Chapter 3.2:
Conductors and Dielectrics in an Electric Field (Part A).
"""

CH3_2A_CURATED = [
    {
        "id": "3.54",
        "title": "Equilibrium of Charged Ball Near Conducting Plane",
        "difficulty": 2,
        "question": "A small conducting ball of mass $m$ is suspended on an insulating thread of length $l$ at a distance $l$ from an infinite conducting plane. What charge $q$ must be deposited on the ball so that the horizontal electrostatic force of attraction deflects the ball towards the plane by a small displacement $x \\ll l$?",
        "hints": [
            "Use the method of images: the conducting plane creates an image charge $-q$ at distance $2l$ behind the initial plane position.",
            "For deflection $x \\ll l$, the distance to the plane is $l - x \\approx l$, and distance to the image charge is $2l$.",
            "Balance the electrostatic attraction $F_e = \\frac{q^2}{4\\pi\\varepsilon_0 (2l)^2}$ with the restoring gravity force $F_g = mg \\frac{x}{l}$."
        ],
        "answer": "$q = 4l \\sqrt{\\pi \\varepsilon_0 m g x / l} = 4 \\sqrt{\\pi \\varepsilon_0 m g l x}$",
        "solution": "**1. Method of Images:**\nThe grounded infinite conducting plane creates an image charge $-q$ at distance $2(l - x) \\approx 2l$ from the real charge $+q$. The attractive image force is:\n$$F_e = \\frac{1}{4\\pi\\varepsilon_0} \\frac{q^2}{(2l)^2} = \\frac{q^2}{16\\pi\\varepsilon_0 l^2}$$\n\n**2. Restoring Force:**\nFor small deflection angle $\\theta \\approx x/l$, the pendulum restoring force is:\n$$F_{\\text{rest}} = m g \\sin\\theta \\approx m g \\frac{x}{l}$$\n\n**3. Equilibrium:**\nEquating $F_e = F_{\\text{rest}}$:\n$$\\frac{q^2}{16\\pi\\varepsilon_0 l^2} = \\frac{m g x}{l} \\implies q^2 = 16\\pi\\varepsilon_0 m g l x$$\n$$q = 4\\sqrt{\\pi\\varepsilon_0 m g l x}$$",
        "tags": ["method of images", "conducting plane", "pendulum equilibrium", "small oscillations"]
    },
    {
        "id": "3.55",
        "title": "Work to Remove Point Charge from Conducting Plane",
        "difficulty": 1,
        "question": "A point charge $q$ is located at a distance $l$ from an infinite conducting plane. What amount of work has to be performed in order to slowly remove this charge very far from the plane?",
        "hints": [
            "By the method of images, at any distance $x$ from the plane, the attractive force is $F(x) = \\frac{q^2}{4\\pi\\varepsilon_0 (2x)^2} = \\frac{q^2}{16\\pi\\varepsilon_0 x^2}$.",
            "To remove the charge slowly, the external agent must apply an opposing force $F_{\\text{ext}} = F(x)$.",
            "Calculate work $A = \\int_l^\\infty F(x) \\, dx = \\frac{q^2}{16\\pi\\varepsilon_0} \\int_l^\\infty \\frac{dx}{x^2}$."
        ],
        "answer": "$A = \\frac{q^2}{16\\pi\\varepsilon_0 l}$",
        "solution": "**1. Image Force as a Function of Distance:**\nAt distance $x$ from the conducting plane, the image charge $-q$ is at distance $2x$ from the real charge. The force of attraction toward the plane is:\n$$F(x) = \\frac{q^2}{4\\pi\\varepsilon_0 (2x)^2} = \\frac{q^2}{16\\pi\\varepsilon_0 x^2}$$\n\n**2. Work of External Force:**\n$$\nA = \\int_l^\\infty F(x) \\, dx = \\frac{q^2}{16\\pi\\varepsilon_0} \\int_l^\\infty \\frac{dx}{x^2} = \\frac{q^2}{16\\pi\\varepsilon_0} \\left[ -\\frac{1}{x} \\right]_l^\\infty = \\frac{q^2}{16\\pi\\varepsilon_0 l}\n$$\n(Note: this is half of the interaction energy $\\frac{q^2}{8\\pi\\varepsilon_0 l}$ between the real charge and image charge, because work was also expended to rearrange surface charges on the conductor).",
        "tags": ["method of images", "conducting plane", "work done", "image force"]
    },
    {
        "id": "3.56",
        "title": "Forces and Field of Dipole Near Conducting Plane",
        "difficulty": 2,
        "question": "Two point charges, $+q$ and $-q$, are separated by a distance $l$, both being located at a distance $l/2$ from an infinite conducting plane. Find:\n(a) the modulus of the vector of the electric force acting on each charge;\n(b) the magnitude of the electric field strength vector at the midpoint between these charges.",
        "hints": [
            "The image system consists of $-q$ opposite to $+q$ and $+q$ opposite to $-q$, both at distance $l/2$ behind the plane.",
            "(a) On charge $+q$, forces come from $-q$ (real), $-q$ (image), and $+q$ (image). Vector sum yields $F = \\frac{q^2}{4\\pi\\varepsilon_0 l^2} \\left(1 - \\frac{1}{2\\sqrt{2}}\\right)$.",
            "(b) At the midpoint, calculate the vector sum of electric fields from all 4 charges."
        ],
        "answer": "(a) $F = \\frac{q^2}{4\\pi\\varepsilon_0 l^2} \\left( 1 - \\frac{1}{2\\sqrt{2}} \\right)$; (b) $E = \\frac{2q}{\\pi\\varepsilon_0 l^2} \\left( 1 - \\frac{1}{5\\sqrt{5}} \\right)$",
        "solution": "**1. Image Charge Configuration:**\nPlace the conducting plane at $y = 0$. The real charges are:\n- $q_1 = +q$ at $(l/2, l/2)$\n- $q_2 = -q$ at $(-l/2, l/2)$\nThe image charges behind the plane ($y < 0$) are:\n- $q'_1 = -q$ at $(l/2, -l/2)$\n- $q'_2 = +q$ at $(-l/2, -l/2)$\n\n**2. Force on Charge $+q$ (Part a):**\n- Attractive force from real $-q$ along $-\\mathbf{i}$: $F_{12} = \\frac{q^2}{4\\pi\\varepsilon_0 l^2}$\n- Attractive force from image $-q'_1$ along $-\\mathbf{j}$ at distance $l$: $F_{11'} = \\frac{q^2}{4\\pi\\varepsilon_0 l^2}$\n- Repulsive force from image $+q'_2$ along diagonal $(\\mathbf{i} + \\mathbf{j})/\\sqrt{2}$ at distance $l\\sqrt{2}$: $F_{12'} = \\frac{q^2}{4\\pi\\varepsilon_0 (2l^2)}$\nSumming forces:\n$$F = \\frac{q^2}{4\\pi\\varepsilon_0 l^2} \\left( 1 - \\frac{1}{2\\sqrt{2}} \\right)$$\n\n**3. Field at Midpoint $(0, l/2)$ (Part b):**\n- Real charges $+q$ and $-q$ produce fields directed along $-\\mathbf{i}$:\n  $$E_{\\text{real}} = 2 \\times \\frac{q}{4\\pi\\varepsilon_0 (l/2)^2} = \\frac{2q}{\\pi\\varepsilon_0 l^2}$$\n- Image charges $-q$ and $+q$ at distance $r = \\sqrt{(l/2)^2 + l^2} = \\frac{\\sqrt{5}}{2}l$ produce opposing field along $+\\mathbf{i}$:\n  $$E_{\\text{image}} = \\frac{2q}{\\pi\\varepsilon_0 l^2} \\frac{1}{5\\sqrt{5}}$$\n$$E = \\frac{2q}{\\pi\\varepsilon_0 l^2} \\left( 1 - \\frac{1}{5\\sqrt{5}} \\right)$$",
        "tags": ["method of images", "dipole", "conducting plane", "force on charge"]
    },
    {
        "id": "3.57",
        "title": "Force on a Charge in a Right-Angled Conducting Corner",
        "difficulty": 2,
        "question": "A point charge $q$ is located between two mutually perpendicular conducting half-planes, at a distance $l$ from each half-plane. Find the modulus of the vector of the force acting on the charge.",
        "hints": [
            "A $90^\\circ$ wedge requires 3 image charges: $-q$ at $(l, -l)$, $-q$ at $(-l, l)$, and $+q$ at $(-l, -l)$.",
            "The real charge is attracted by two image charges $-q$ at distance $2l$ with force $\\frac{q^2}{16\\pi\\varepsilon_0 l^2}$ each.",
            "It is repelled by the image charge $+q$ along the diagonal at distance $2\\sqrt{2}l$ with force $\\frac{q^2}{32\\pi\\varepsilon_0 l^2}$."
        ],
        "answer": "$F = \\frac{q^2}{32\\pi\\varepsilon_0 l^2} (2\\sqrt{2} - 1)$",
        "solution": "**1. Image Charge System:**\nLet the half-planes be $x = 0$ ($y \\ge 0$) and $y = 0$ ($x \\ge 0$). The charge $q$ is at $(l, l)$.\nThe image system satisfying zero potential on both planes consists of:\n- $q_1 = -q$ at $(-l, l)$ (distance $2l$ along $x$)\n- $q_2 = -q$ at $(l, -l)$ (distance $2l$ along $y$)\n- $q_3 = +q$ at $(-l, -l)$ (distance $2\\sqrt{2}l$ along the diagonal)\n\n**2. Force Calculation:**\n- Attraction towards $x = 0$: $F_x = -\\frac{q^2}{4\\pi\\varepsilon_0 (2l)^2} = -\\frac{q^2}{16\\pi\\varepsilon_0 l^2}$\n- Attraction towards $y = 0$: $F_y = -\\frac{q^2}{4\\pi\\varepsilon_0 (2l)^2} = -\\frac{q^2}{16\\pi\\varepsilon_0 l^2}$\nThe resultant attractive force toward the corner along the diagonal is:\n$$F_{\\text{attr}} = \\sqrt{F_x^2 + F_y^2} = \\sqrt{2} \\frac{q^2}{16\\pi\\varepsilon_0 l^2} = \\frac{\\sqrt{2} q^2}{16\\pi\\varepsilon_0 l^2}$$\n- Repulsive force from $+q$ directed away from the corner along the diagonal:\n$$F_{\\text{rep}} = \\frac{q^2}{4\\pi\\varepsilon_0 (2\\sqrt{2}l)^2} = \\frac{q^2}{32\\pi\\varepsilon_0 l^2}$$\n\n**3. Net Force Magnitude:**\n$$F = F_{\\text{attr}} - F_{\\text{rep}} = \\frac{\\sqrt{2} q^2}{16\\pi\\varepsilon_0 l^2} - \\frac{q^2}{32\\pi\\varepsilon_0 l^2} = \\frac{q^2}{32\\pi\\varepsilon_0 l^2} (2\\sqrt{2} - 1)$$",
        "tags": ["conducting corner", "right-angle wedge", "method of images", "Coulomb force"]
    },
    {
        "id": "3.58",
        "title": "Force on a Perpendicular Dipole Near Conducting Plane",
        "difficulty": 2,
        "question": "A point dipole with electric moment $\\mathbf{p}$ is located at a distance $l$ from an infinite conducting plane. Find the modulus of the vector of the force acting on the dipole if the vector $\\mathbf{p}$ is perpendicular to the plane.",
        "hints": [
            "For a dipole $\\mathbf{p} = p\\mathbf{k}$ perpendicular to the grounded plane at $z = 0$, the image dipole is $\\mathbf{p}' = p\\mathbf{k}$ located at $z = -l$.",
            "The separation between the real and image dipoles is $2l$, oriented collinearly.",
            "Use the collinear dipole-dipole force formula: $F = \\frac{6 p p'}{4\\pi\\varepsilon_0 (2l)^4} = \\frac{3p^2}{32\\pi\\varepsilon_0 l^4}$."
        ],
        "answer": "$F = \\frac{3p^2}{32\\pi\\varepsilon_0 l^4}$",
        "solution": "**1. Image Dipole:**\nLet the conducting plane be $z = 0$, and the dipole $\\mathbf{p} = p\\mathbf{k}$ be at $z = l$.\nThe image dipole that maintains $\\varphi = 0$ on the plane has the exact same direction $\\mathbf{p}' = p\\mathbf{k}$ located at $z = -l$.\n\n**2. Force Between Collinear Dipoles:**\nThe real and image dipoles lie on the same $z$-axis separated by distance $r = 2l$.\nThe field of the image dipole along its axis at the real dipole's position is:\n$$E_{\\text{im}}(z) = \\frac{2p}{4\\pi\\varepsilon_0 (z + l)^3}$$\nThe force exerted on the real dipole is:\n$$F = p \\left| \\frac{\\partial E_{\\text{im}}}{\\partial z} \\right|_{z=l} = p \\left[ \\frac{6p}{4\\pi\\varepsilon_0 (z + l)^4} \\right]_{z=l} = \\frac{6p^2}{4\\pi\\varepsilon_0 (2l)^4} = \\frac{6p^2}{4\\pi\\varepsilon_0 (16 l^4)} = \\frac{3p^2}{32\\pi\\varepsilon_0 l^4}$$",
        "tags": ["dipole", "method of images", "conducting plane", "interaction force"]
    },
    {
        "id": "3.59",
        "title": "Induced Charge Distribution on a Conducting Plane",
        "difficulty": 2,
        "question": "A point charge $q$ is located at a distance $l$ from an infinite conducting plane. Determine the surface density of charges induced on the plane as a function of separation $r$ from the base of the perpendicular drawn to the plane from the charge, and find the total induced charge.",
        "hints": [
            "Use the image charge $-q$ at distance $l$ behind the plane.",
            "The normal electric field at the plane's surface is $E_n = 2 \\times \\frac{q \\cos\\theta}{4\\pi\\varepsilon_0 R^2} = \\frac{q l}{2\\pi\\varepsilon_0 (l^2 + r^2)^{3/2}}$.",
            "Surface charge density is $\\sigma(r) = -\\varepsilon_0 E_n = -\\frac{q l}{2\\pi (l^2 + r^2)^{3/2}}$. Integrate over the plane to find $q_{\\text{ind}} = -q$."
        ],
        "answer": "$\\sigma(r) = -\\frac{q l}{2\\pi (l^2 + r^2)^{3/2}}; \\quad q_{\\text{ind}} = -q$",
        "solution": "**1. Electric Field at Plane Surface:**\nWith the real charge $+q$ at $(0, 0, l)$ and image $-q$ at $(0, 0, -l)$, the parallel field components cancel on the plane $z = 0$. The normal component directed into the conductor ($-\\mathbf{k}$) is:\n$$E_n = 2 \\left( \\frac{q}{4\\pi\\varepsilon_0 (r^2 + l^2)} \\right) \\frac{l}{\\sqrt{r^2 + l^2}} = \\frac{q l}{2\\pi\\varepsilon_0 (r^2 + l^2)^{3/2}}$$\n\n**2. Induced Surface Density:**\nFrom the boundary condition for conductors $\\sigma = -\\varepsilon_0 E_n$:\n$$\\sigma(r) = -\\frac{q l}{2\\pi (r^2 + l^2)^{3/2}}$$\n\n**3. Total Induced Charge:**\n$$q_{\\text{ind}} = \\int_0^\\infty \\sigma(r) 2\\pi r \\, dr = -q l \\int_0^\\infty \\frac{r \\, dr}{(r^2 + l^2)^{3/2}} = -q l \\left[ -\\frac{1}{\\sqrt{r^2 + l^2}} \\right]_0^\\infty = -q l \\left( 0 + \\frac{1}{l} \\right) = -q$$",
        "tags": ["induced charge", "conducting plane", "surface density", "method of images"]
    },
    {
        "id": "3.60",
        "title": "Force and Induced Charge for Line Charge Parallel to Conducting Plane",
        "difficulty": 2,
        "question": "A thin infinitely long thread carrying a charge $\\lambda$ per unit length is oriented parallel to an infinite conducting plane at distance $l$. Find:\n(a) the modulus of the vector of the force acting on a unit length of the thread;\n(b) the distribution of surface charge density $\\sigma(x)$ over the plane.",
        "hints": [
            "(a) The image is a thread of linear density $-\\lambda$ at distance $2l$. The force per unit length is $F_1 = \\frac{\\lambda^2}{2\\pi\\varepsilon_0 (2l)} = \\frac{\\lambda^2}{4\\pi\\varepsilon_0 l}$.",
            "(b) Find $E_n(x)$ at distance $x$ from the perpendicular foot: $E_n(x) = 2 \\times \\frac{\\lambda}{2\\pi\\varepsilon_0 \\sqrt{l^2 + x^2}} \\frac{l}{\\sqrt{l^2 + x^2}}$.",
            "Surface charge density is $\\sigma(x) = -\\varepsilon_0 E_n(x) = -\\frac{\\lambda l}{\\pi (l^2 + x^2)}$."
        ],
        "answer": "(a) $F_1 = \\frac{\\lambda^2}{4\\pi\\varepsilon_0 l}$; (b) $\\sigma(x) = -\\frac{\\lambda l}{\\pi (l^2 + x^2)}$",
        "solution": "**1. Force on Unit Length (Part a):**\nThe image is a line charge of linear density $-\\lambda$ located at distance $2l$ from the real thread. The electric field of the image at the thread is:\n$$E_{\\text{im}} = \\frac{\\lambda}{2\\pi\\varepsilon_0 (2l)} = \\frac{\\lambda}{4\\pi\\varepsilon_0 l}$$\nThe attractive force per unit length is:\n$$F_1 = \\lambda E_{\\text{im}} = \\frac{\\lambda^2}{4\\pi\\varepsilon_0 l}$$\n\n**2. Surface Charge Density on Plane (Part b):**\nAt a point on the plane at distance $x$ from the projection of the thread, the distance to both real and image line charges is $\\sqrt{l^2 + x^2}$.\nThe normal electric field is:\n$$E_n = 2 \\left( \\frac{\\lambda}{2\\pi\\varepsilon_0 \\sqrt{l^2 + x^2}} \\right) \\cos\\theta = \\frac{\\lambda}{\\pi\\varepsilon_0 \\sqrt{l^2 + x^2}} \\frac{l}{\\sqrt{l^2 + x^2}} = \\frac{\\lambda l}{\\pi\\varepsilon_0 (l^2 + x^2)}$$\nBy the conductor boundary condition $\\sigma = -\\varepsilon_0 E_n$:\n$$\\sigma(x) = -\\frac{\\lambda l}{\\pi (l^2 + x^2)}$$",
        "tags": ["line charge", "conducting plane", "method of images", "surface charge density"]
    },
    {
        "id": "3.61",
        "title": "Induced Charge from Perpendicular Semi-Infinite Thread",
        "difficulty": 2,
        "question": "A very long straight thread is oriented at right angles to an infinite conducting plane; its end is separated from the plane by a distance $l$. The thread carries a uniform charge of linear density $\\lambda$. Find the surface density of the induced charge on the plane:\n(a) at the point $O$ directly below the thread;\n(b) as a function of distance $r$ from point $O$.",
        "hints": [
            "Use the image method: the semi-infinite thread from $z = l$ to $\\infty$ with charge $+\\lambda$ has an image semi-infinite thread from $z = -l$ to $-\\infty$ with charge $-\\lambda$.",
            "(a) At $r = 0$, $E_n = 2 \\int_l^\\infty \\frac{\\lambda \\, dz}{4\\pi\\varepsilon_0 z^2} = \\frac{\\lambda}{2\\pi\\varepsilon_0 l}$, so $\\sigma(0) = -\\frac{\\lambda}{2\\pi l}$.",
            "(b) For arbitrary $r$, evaluate $\\sigma(r) = -\\frac{\\lambda}{2\\pi \\sqrt{l^2 + r^2}}$ or similar integral."
        ],
        "answer": "(a) $\\sigma(0) = -\\frac{\\lambda}{2\\pi l}$; (b) $\\sigma(r) = -\\frac{\\lambda}{2\\pi \\sqrt{l^2 + r^2}}$",
        "solution": "**1. Image Charge Setup:**\nThe semi-infinite thread extends along the $z$-axis from $z = l$ to $z = \\infty$ with density $+\\lambda$. The image thread extends from $z = -l$ to $z = -\\infty$ with density $-\\lambda$.\n\n**2. Normal Electric Field on the Plane:**\nAt a distance $r$ from the origin on the conducting plane $z = 0$, an element $dz$ at height $z$ on the real thread and its image element at $-z$ contribute a normal electric field directed toward the conductor:\n$$dE_n = 2 \\left( \\frac{\\lambda \\, dz}{4\\pi\\varepsilon_0 (z^2 + r^2)} \\right) \\frac{z}{\\sqrt{z^2 + r^2}} = \\frac{\\lambda z \\, dz}{2\\pi\\varepsilon_0 (z^2 + r^2)^{3/2}}$$\nIntegrating over the semi-infinite thread from $z = l$ to $\\infty$:\n$$E_n = \\frac{\\lambda}{2\\pi\\varepsilon_0} \\int_l^\\infty \\frac{z \\, dz}{(z^2 + r^2)^{3/2}} = \\frac{\\lambda}{2\\pi\\varepsilon_0} \\left[ -\\frac{1}{\\sqrt{z^2 + r^2}} \\right]_l^\\infty = \\frac{\\lambda}{2\\pi\\varepsilon_0 \\sqrt{l^2 + r^2}}$$\n\n**3. Surface Charge Density:**\n$$\\sigma(r) = -\\varepsilon_0 E_n = -\\frac{\\lambda}{2\\pi \\sqrt{l^2 + r^2}}$$\nAt the center $r = 0$:\n$$\\sigma(0) = -\\frac{\\lambda}{2\\pi l}$$",
        "tags": ["semi-infinite thread", "perpendicular line charge", "method of images", "induced charge"]
    },
    {
        "id": "3.62",
        "title": "Field and Potential of Charged Ring Parallel to Conducting Plane",
        "difficulty": 2,
        "question": "A thin wire ring of radius $R$ carries a charge $q$. The ring is oriented parallel to an infinite conducting plane and is separated by a distance $l$ from it. Find:\n(a) the surface charge density on the plane at the point symmetrical with respect to the ring;\n(b) the strength and potential of the electric field at the centre of the ring.",
        "hints": [
            "Use an image ring of radius $R$ with charge $-q$ at distance $l$ behind the plane (total separation $2l$).",
            "(a) Every element of the real ring is at distance $\\sqrt{R^2 + l^2}$ from the point $O$. The normal field is $E_n = \\frac{2 q l}{4\\pi\\varepsilon_0 (R^2 + l^2)^{3/2}}$, so $\\sigma = -\\frac{q l}{2\\pi (R^2 + l^2)^{3/2}}$.",
            "(b) At the ring center, the ring itself produces zero field, so $\\mathbf{E}$ comes entirely from the image ring at distance $2l$."
        ],
        "answer": "(a) $\\sigma = -\\frac{q l}{2\\pi (R^2 + l^2)^{3/2}}$; (b) $E = \\frac{q l}{2\\pi\\varepsilon_0 (R^2 + 4l^2)^{3/2}}, \\; \\varphi = \\frac{q}{4\\pi\\varepsilon_0} \\left( \\frac{1}{R} - \\frac{1}{\\sqrt{R^2 + 4l^2}} \\right)$",
        "solution": "**1. Induced Charge at Symmetry Point (Part a):**\nThe image ring of charge $-q$ is at distance $2l$ behind the real ring. At the point $O$ on the plane directly under the ring center, all elements of both rings are at distance $\\sqrt{R^2 + l^2}$.\nThe normal electric field at $O$ is:\n$$E_n = 2 \\times \\frac{q}{4\\pi\\varepsilon_0 (R^2 + l^2)} \\frac{l}{\\sqrt{R^2 + l^2}} = \\frac{q l}{2\\pi\\varepsilon_0 (R^2 + l^2)^{3/2}}$$\n$$\\sigma = -\\varepsilon_0 E_n = -\\frac{q l}{2\\pi (R^2 + l^2)^{3/2}}$$\n\n**2. Field and Potential at Ring Center (Part b):**\n- By symmetry, the real ring creates zero electric field at its own center. The electric field is entirely due to the image ring of charge $-q$ at distance $2l$:\n  $$E = \\frac{q (2l)}{4\\pi\\varepsilon_0 (R^2 + (2l)^2)^{3/2}} = \\frac{q l}{2\\pi\\varepsilon_0 (R^2 + 4l^2)^{3/2}}$$\n- The potential is the sum of potentials from the ring and the image ring:\n  $$\\varphi = \\frac{q}{4\\pi\\varepsilon_0 R} - \\frac{q}{4\\pi\\varepsilon_0 \\sqrt{R^2 + (2l)^2}} = \\frac{q}{4\\pi\\varepsilon_0} \\left( \\frac{1}{R} - \\frac{1}{\\sqrt{R^2 + 4l^2}} \\right)$$",
        "tags": ["charged ring", "conducting plane", "method of images", "potential"]
    },
    {
        "id": "3.63",
        "title": "Potential of Uncharged Conducting Sphere Outside a Point Charge",
        "difficulty": 1,
        "question": "Find the potential $\\varphi$ of an uncharged conducting sphere outside of which a point charge $q$ is located at a distance $l$ from the sphere's centre.",
        "hints": [
            "A conductor is an equipotential body in electrostatics, so its potential is uniform throughout its volume and surface.",
            "The potential of the sphere can be evaluated at its centre $O$.",
            "At the center, the total induced surface charge produces zero net potential because $\\oint \\frac{dq_{\\text{ind}}}{4\\pi\\varepsilon_0 R} = \\frac{q_{\\text{tot, ind}}}{4\\pi\\varepsilon_0 R} = 0$."
        ],
        "answer": "$\\varphi = \\frac{q}{4\\pi\\varepsilon_0 l}$",
        "solution": "**1. Equipotential Nature of Conductor:**\nIn electrostatic equilibrium, every point of the conducting sphere has the same potential $\\varphi$. In particular, $\\varphi = \\varphi(O)$, where $O$ is the center of the sphere.\n\n**2. Potential at the Center:**\nThe potential at $O$ is the sum of the potential due to the external charge $q$ and the potential due to the induced surface charge $\\sigma_{\\text{ind}}$ on the sphere of radius $R$:\n$$\\varphi(O) = \\frac{q}{4\\pi\\varepsilon_0 l} + \\int_S \\frac{dq_{\\text{ind}}}{4\\pi\\varepsilon_0 R} = \\frac{q}{4\\pi\\varepsilon_0 l} + \\frac{1}{4\\pi\\varepsilon_0 R} \\int_S dq_{\\text{ind}}$$\n\n**3. Charge Conservation:**\nSince the sphere is uncharged and isolated, $\\int_S dq_{\\text{ind}} = q_{\\text{tot, ind}} = 0$:\n$$\\varphi = \\frac{q}{4\\pi\\varepsilon_0 l}$$",
        "tags": ["conducting sphere", "uncharged conductor", "equipotential", "induced charge"]
    },
    {
        "id": "3.64",
        "title": "Potential at Center of Spherical Shell with Internal Charge",
        "difficulty": 2,
        "question": "A point charge $q$ is located at a distance $r$ from the centre $O$ of an uncharged conducting spherical layer whose inside and outside radii are equal to $R_1$ and $R_2$ respectively. Find the potential at point $O$ if $r < R_1$.",
        "hints": [
            "The point charge $q$ induces $-q$ on the inner surface ($r = R_1$) and $+q$ on the outer surface ($r = R_2$).",
            "The potential at the center $O$ is the sum of contributions from: the point charge $q$ at distance $r$, the induced charge $-q$ at radius $R_1$, and $+q$ uniformly distributed on $R_2$.",
            "Compute $\\varphi(O) = \\frac{q}{4\\pi\\varepsilon_0} \\left( \\frac{1}{r} - \\frac{1}{R_1} + \\frac{1}{R_2} \\right)$."
        ],
        "answer": "$\\varphi(O) = \\frac{q}{4\\pi\\varepsilon_0} \\left( \\frac{1}{r} - \\frac{1}{R_1} + \\frac{1}{R_2} \\right)$",
        "solution": "**1. Induced Charges on Shell:**\nBy Gauss's law, a charge $q$ inside the cavity induces an equal and opposite charge $q_{\\text{in}} = -q$ on the inner cavity surface of radius $R_1$.\nSince the conducting shell is uncharged, by charge conservation a charge $q_{\\text{out}} = +q$ must appear on the outer surface of radius $R_2$.\n\n**2. Potential at the Center $O$:**\nBy the principle of superposition, the potential at $O$ is:\n$$\\varphi(O) = \\varphi_q + \\varphi_{\\text{in}} + \\varphi_{\\text{out}}$$\n- From the point charge $q$ at distance $r$: $\\varphi_q = \\frac{q}{4\\pi\\varepsilon_0 r}$\n- From the inner surface charge $-q$ (every element is at distance $R_1$ from $O$):\n  $$\\varphi_{\\text{in}} = \\int \\frac{dq_{\\text{in}}}{4\\pi\\varepsilon_0 R_1} = \\frac{-q}{4\\pi\\varepsilon_0 R_1}$$\n- From the outer surface charge $+q$ (every element is at distance $R_2$ from $O$):\n  $$\\varphi_{\\text{out}} = \\int \\frac{dq_{\\text{out}}}{4\\pi\\varepsilon_0 R_2} = \\frac{+q}{4\\pi\\varepsilon_0 R_2}$$\n\n**3. Summing Contributions:**\n$$\\varphi(O) = \\frac{q}{4\\pi\\varepsilon_0} \\left( \\frac{1}{r} - \\frac{1}{R_1} + \\frac{1}{R_2} \\right)$$",
        "tags": ["spherical shell", "electrostatic shielding", "induced charges", "cavity potential"]
    },
    {
        "id": "3.65",
        "title": "Concentric Spheres: Zeroing the Inner Sphere Potential",
        "difficulty": 2,
        "question": "A system consists of two concentric conducting spheres, with the inside sphere of radius $a$ carrying a positive charge $q_1$. What charge $q_2$ has to be deposited on the outside sphere of radius $b$ to reduce the potential of the inside sphere to zero? How does the potential $\\varphi$ depend in this case on distance $r$ from the centre of the system?",
        "hints": [
            "The potential of the inner sphere is $\\varphi_a = \\frac{1}{4\\pi\\varepsilon_0} \\left( \\frac{q_1}{a} + \\frac{q_2}{b} \\right)$.",
            "Setting $\\varphi_a = 0$ gives $q_2 = -\\frac{b}{a} q_1$.",
            "For $a \\le r \\le b$: $\\varphi(r) = \\frac{q_1}{4\\pi\\varepsilon_0} \\left( \\frac{1}{r} - \\frac{1}{a} \\right)$. For $r \\ge b$: $\\varphi(r) = \\frac{q_1 + q_2}{4\\pi\\varepsilon_0 r} = \\frac{q_1}{4\\pi\\varepsilon_0 r} \\left( 1 - \\frac{b}{a} \\right)$."
        ],
        "answer": "$q_2 = -\\frac{b}{a} q_1; \\quad \\varphi(r) = \\begin{cases} 0, & r \\le a \\\\ \\frac{q_1}{4\\pi\\varepsilon_0} \\left( \\frac{1}{r} - \\frac{1}{a} \\right), & a \\le r \\le b \\\\ \\frac{q_1}{4\\pi\\varepsilon_0 r} \\left( 1 - \\frac{b}{a} \\right), & r \\ge b \\end{cases}$",
        "solution": "**1. Potential of the Inner Sphere:**\nThe potential on the inner sphere of radius $a$ is:\n$$\\varphi_a = \\frac{q_1}{4\\pi\\varepsilon_0 a} + \\frac{q_2}{4\\pi\\varepsilon_0 b}$$\nSetting $\\varphi_a = 0$:\n$$\\frac{q_1}{a} + \\frac{q_2}{b} = 0 \\implies q_2 = -\\frac{b}{a} q_1$$\n\n**2. Potential Distribution $\\varphi(r)$:**\n- Inside sphere ($r \\le a$): conductor is equipotential $\\implies \\varphi(r) = 0$.\n- Between spheres ($a \\le r \\le b$):\n  $$\\varphi(r) = \\frac{q_1}{4\\pi\\varepsilon_0 r} + \\frac{q_2}{4\\pi\\varepsilon_0 b} = \\frac{q_1}{4\\pi\\varepsilon_0} \\left( \\frac{1}{r} - \\frac{1}{a} \\right)$$\n- Outside outer sphere ($r \\ge b$):\n  $$\\varphi(r) = \\frac{q_1 + q_2}{4\\pi\\varepsilon_0 r} = \\frac{q_1}{4\\pi\\varepsilon_0 r} \\left( 1 - \\frac{b}{a} \\right)$$",
        "tags": ["concentric spheres", "grounding", "potential distribution", "capacitance"]
    },
    {
        "id": "3.66",
        "title": "Four Metal Plates with Interconnected Outer Plates",
        "difficulty": 2,
        "question": "Four large metal plates are located at equal small distance $d$ from one another. The extreme plates (1 and 4) are interconnected by means of a conductor while a potential difference $\\Delta\\varphi$ is applied to internal plates (plates 2 and 3). Find:\n(a) the values of the electric field strength between neighbouring plates;\n(b) the total charge per unit area of each plate.",
        "hints": [
            "The system forms three capacitors in series/parallel: $C_{12}, C_{23}, C_{34}$, each with $C = \\frac{\\varepsilon_0 S}{d}$.",
            "(a) Since plates 1 and 4 are at the same potential, $E_{12} d + E_{23} d + E_{34} d = 0$. Here $E_{23} = \\frac{\\Delta\\varphi}{d}$ and $E_{12} = E_{34} = \\frac{\\Delta\\varphi}{2d}$.",
            "(b) Charge densities: $\\sigma_1 = \\sigma_4 = \\frac{\\varepsilon_0 \\Delta\\varphi}{2d}$ and $\\sigma_2 = \\sigma_3 = \\frac{3\\varepsilon_0 \\Delta\\varphi}{2d}$."
        ],
        "answer": "(a) $E_{23} = \\frac{\\Delta\\varphi}{d}, \\; E_{12} = E_{34} = \\frac{\\Delta\\varphi}{2d}$; (b) $|\\sigma_1| = |\\sigma_4| = \\frac{\\varepsilon_0 \\Delta\\varphi}{2d}, \\; |\\sigma_2| = |\\sigma_3| = \\frac{3\\varepsilon_0 \\Delta\\varphi}{2d}$",
        "solution": "**1. Electric Fields Between Plates:**\nLet plates 1 and 4 be connected, so $\\varphi_1 = \\varphi_4 = 0$. A voltage $\\Delta\\varphi = \\varphi_2 - \\varphi_3$ is applied between plates 2 and 3.\nBy symmetry with respect to the center:\n$$\\varphi_2 = \\frac{\\Delta\\varphi}{2}, \\quad \\varphi_3 = -\\frac{\\Delta\\varphi}{2}$$\n- Between plates 1 and 2: $E_{12} = \\frac{\\varphi_2 - \\varphi_1}{d} = \\frac{\\Delta\\varphi}{2d}$\n- Between plates 2 and 3: $E_{23} = \\frac{\\varphi_2 - \\varphi_3}{d} = \\frac{\\Delta\\varphi}{d}$\n- Between plates 3 and 4: $E_{34} = \\frac{\\varphi_4 - \\varphi_3}{d} = \\frac{\\Delta\\varphi}{2d}$\n\n**2. Surface Charge Densities:**\nBy Gauss's law for conductors $\\sigma = \\varepsilon_0 \\Delta E$:\n- Plate 1: $\\sigma_1 = -\\varepsilon_0 E_{12} = -\\frac{\\varepsilon_0 \\Delta\\varphi}{2d}$\n- Plate 2: receives charge on both faces $\\sigma_2 = \\varepsilon_0 E_{12} + \\varepsilon_0 E_{23} = \\varepsilon_0 \\left( \\frac{\\Delta\\varphi}{2d} + \\frac{\\Delta\\varphi}{d} \\right) = \\frac{3\\varepsilon_0 \\Delta\\varphi}{2d}$\n- Plate 3: $\\sigma_3 = -\\frac{3\\varepsilon_0 \\Delta\\varphi}{2d}$\n- Plate 4: $\\sigma_4 = +\\frac{\\varepsilon_0 \\Delta\\varphi}{2d}$",
        "tags": ["parallel plates", "capacitor network", "surface charge density", "potential difference"]
    },
    {
        "id": "3.67",
        "title": "Charges Induced on Two Parallel Grounded Plates",
        "difficulty": 2,
        "question": "Two infinite conducting plates 1 and 2 are separated by a distance $l$. A point charge $q$ is located between the plates at a distance $x$ from plate 1. Find the charges $q_1$ and $q_2$ induced on each plate.",
        "hints": [
            "Use Green's reciprocity theorem or imagine spreading the charge $q$ uniformly over a parallel plane at distance $x$.",
            "Between plate 1 and the charge sheet: field is $E_1$; between charge sheet and plate 2: field is $E_2$.",
            "Boundary condition $\\varphi_1 = \\varphi_2 = 0$ implies $E_1 x = E_2 (l - x)$, and Gauss's law gives $\\varepsilon_0 (E_1 + E_2) = \\sigma = q/S$."
        ],
        "answer": "$q_1 = -q \\frac{l - x}{l}, \\quad q_2 = -q \\frac{x}{l}$",
        "solution": "**1. Equivalence to Charge Sheet:**\nBy Green's reciprocity theorem, the total charges induced on the infinite grounded plates 1 and 2 by a point charge $q$ at distance $x$ from plate 1 are identical to those induced by a uniform sheet of charge $q$ over area $S$ at position $x$.\n\n**2. Field Balance:**\nLet $E_1$ be the electric field in region $1$ ($0 < z < x$) and $E_2$ in region $2$ ($x < z < l$):\n- Potential difference across plates is zero:\n  $$\\int_0^l E \\, dz = 0 \\implies E_1 x - E_2 (l - x) = 0 \\implies \\frac{E_1}{E_2} = \\frac{l - x}{x}$$\n- Discontinuity across the charge sheet:\n  $$\\varepsilon_0 (E_1 + E_2) = \\frac{q}{S}$$\n\n**3. Induced Charges:**\n- On plate 1: $q_1 = -\\varepsilon_0 E_1 S = -q \\frac{E_1}{E_1 + E_2} = -q \\frac{l - x}{l}$\n- On plate 2: $q_2 = -\\varepsilon_0 E_2 S = -q \\frac{x}{l}$\nNote that $q_1 + q_2 = -q$, in exact agreement with charge conservation.",
        "tags": ["induced charges", "Green reciprocity theorem", "grounded plates", "point charge"]
    },
    {
        "id": "3.68",
        "title": "Electrostatic Pressure on a Conductor Surface",
        "difficulty": 1,
        "question": "Find the electric force experienced by a charge reduced to a unit area of an arbitrary conductor if the surface density of the charge equals $\\sigma$.",
        "hints": [
            "The field just outside the conductor is $E = \\frac{\\sigma}{\\varepsilon_0}$ and inside it is $0$.",
            "The effective field acting on the surface charge itself is the average of inside and outside fields: $E_{\\text{eff}} = \\frac{1}{2} \\left( 0 + \\frac{\\sigma}{\\varepsilon_0} \\right) = \\frac{\\sigma}{2\\varepsilon_0}$.",
            "The force per unit area (electrostatic pressure) is $P = \\frac{dF}{dS} = \\sigma E_{\\text{eff}} = \\frac{\\sigma^2}{2\\varepsilon_0}$."
        ],
        "answer": "$\\frac{dF}{dS} = \\frac{\\sigma^2}{2\\varepsilon_0}$",
        "solution": "**1. Effective Field Acting on Surface Layer:**\nThe electric field just outside the surface of a conductor is $E_{\\text{out}} = \\frac{\\sigma}{\\varepsilon_0}$, while the field inside the conductor is $E_{\\text{in}} = 0$.\nThe surface charge layer cannot exert a net force on itself. The self-field of a planar patch of density $\\sigma$ is $\\pm \\frac{\\sigma}{2\\varepsilon_0}$ on either side. Subtracting this self-field, the field produced by the rest of the conductor acting on the charge element is:\n$$E_{\\text{eff}} = E_{\\text{out}} - \\frac{\\sigma}{2\\varepsilon_0} = \\frac{\\sigma}{\\varepsilon_0} - \\frac{\\sigma}{2\\varepsilon_0} = \\frac{\\sigma}{2\\varepsilon_0}$$\n\n**2. Force per Unit Area:**\n$$P = \\frac{dF}{dS} = \\sigma E_{\\text{eff}} = \\frac{\\sigma^2}{2\\varepsilon_0}$$",
        "tags": ["electrostatic pressure", "conductor surface", "force per unit area", "self-field"]
    },
    {
        "id": "3.69",
        "title": "Repulsion Force Between Hemispheres of a Charged Metal Ball",
        "difficulty": 2,
        "question": "A metal ball of radius $R = 1.5\\text{ cm}$ has a charge $q = 10\\,\\mu\\text{C}$. Find the modulus of the vector of the resultant force acting on a charge located on one half of the ball.",
        "hints": [
            "Surface charge density is uniform: $\\sigma = \\frac{q}{4\\pi R^2}$.",
            "Electrostatic pressure is $P = \\frac{\\sigma^2}{2\\varepsilon_0}$.",
            "Integrate the axial component of pressure over the hemisphere: $F = P \\times (\\pi R^2) = \\frac{\\sigma^2}{2\\varepsilon_0} (\\pi R^2) = \\frac{q^2}{32\\pi\\varepsilon_0 R^2}$."
        ],
        "answer": "$F = \\frac{q^2}{32\\pi\\varepsilon_0 R^2} \\approx 0.20\\text{ kN}$",
        "solution": "**1. Electrostatic Pressure:**\nFor a spherical conductor with charge $q$:\n$$\\sigma = \\frac{q}{4\\pi R^2}$$\n$$P = \\frac{\\sigma^2}{2\\varepsilon_0} = \\frac{q^2}{32\\pi^2 \\varepsilon_0 R^4}$$\n\n**2. Resultant Force on Hemisphere:**\nBy symmetry, the net force on the hemisphere points along its axis of symmetry. The projection of the hemisphere's area perpendicular to this axis is a circular disc of area $\\pi R^2$:\n$$F = \\int_{\\text{hemi}} P \\cos\\theta \\, dS = P \\int_{\\text{hemi}} \\cos\\theta \\, dS = P (\\pi R^2)$$\n$$F = \\frac{q^2}{32\\pi^2 \\varepsilon_0 R^4} (\\pi R^2) = \\frac{q^2}{32\\pi\\varepsilon_0 R^2}$$\n\n**3. Numerical Evaluation:**\nWith $q = 10 \\times 10^{-6}\\text{ C}$ and $R = 0.015\\text{ m}$:\n$$F = \\frac{(10^{-5})^2}{32\\pi \\times (8.854 \\times 10^{-12}) \\times (0.015)^2} = \\frac{10^{-10}}{2.003 \\times 10^{-13}} \\approx 499\\text{ N} \\approx 0.20\\text{ kN}$$\n(or $\\approx 0.50\\text{ kN}$ with $g$).",
        "tags": ["charged hemisphere", "electrostatic repulsion", "pressure integration", "Coulomb force"]
    },
    {
        "id": "3.70",
        "title": "Force on Induced Charges on Conducting Ball in Uniform Field",
        "difficulty": 2,
        "question": "When an uncharged conducting ball of radius $R$ is placed in an external uniform electric field, a surface charge density $\\sigma = \\sigma_0 \\cos\\theta$ is induced on the ball's surface. Find the magnitude of the resultant electric force acting on the induced charge of the same sign (one hemisphere).",
        "hints": [
            "The electrostatic pressure on the surface is $P(\\theta) = \\frac{\\sigma^2(\\theta)}{2\\varepsilon_0} = \\frac{\\sigma_0^2 \\cos^2\\theta}{2\\varepsilon_0}$.",
            "Integrate the axial force component over the hemisphere $0 \\le \\theta \\le \\pi/2$: $dF_z = P(\\theta) \\cos\\theta (2\\pi R^2 \\sin\\theta \\, d\\theta)$.",
            "Calculate $F = \\frac{\\pi R^2 \\sigma_0^2}{\\varepsilon_0} \\int_0^{\\pi/2} \\cos^3\\theta \\sin\\theta \\, d\\theta = \\frac{1}{4\\varepsilon_0} \\pi R^2 \\sigma_0^2$."
        ],
        "answer": "$F = \\frac{\\pi R^2 \\sigma_0^2}{4\\varepsilon_0}$",
        "solution": "**1. Electrostatic Pressure:**\nAt any point on the conducting ball, the outward electrostatic pressure is:\n$$P(\\theta) = \\frac{\\sigma^2(\\theta)}{2\\varepsilon_0} = \\frac{\\sigma_0^2 \\cos^2\\theta}{2\\varepsilon_0}$$\n\n**2. Force on One Sign of Induced Charge ($0 \\le \\theta \\le \\pi/2$):**\nBy symmetry, the resultant force points along the polar axis ($z$-axis):\n$$F = \\int_0^{\\pi/2} P(\\theta) \\cos\\theta \\, (2\\pi R^2 \\sin\\theta \\, d\\theta) = \\frac{\\pi R^2 \\sigma_0^2}{\\varepsilon_0} \\int_0^{\\pi/2} \\cos^3\\theta \\sin\\theta \\, d\\theta$$\nUsing $\\int_0^{\\pi/2} \\cos^3\\theta \\sin\\theta \\, d\\theta = \\left[ -\\frac{\\cos^4\\theta}{4} \\right]_0^{\\pi/2} = \\frac{1}{4}$:\n$$F = \\frac{\\pi R^2 \\sigma_0^2}{4\\varepsilon_0}$$",
        "tags": ["conducting ball", "induced charge", "electrostatic pressure", "integration"]
    },
    {
        "id": "3.71",
        "title": "Fraction of Aligned Water Dipoles in an Electric Field",
        "difficulty": 2,
        "question": "An electric field of strength $E = 1.0\\text{ kV/cm}$ produces polarization in water equivalent to the correct orientation of only one out of $N$ molecules. Find $N$. The electric dipole moment of a water molecule equals $p = 0.62 \\times 10^{-29}\\text{ C}\\cdot\\text{m}$, and the permittivity of water is $\\varepsilon = 81$.",
        "hints": [
            "Polarization of water is $P = \\varepsilon_0 (\\varepsilon - 1) E$.",
            "On the other hand, $P = n_{\\text{aligned}} p = \\frac{n_0}{N} p$, where $n_0 = \\frac{\\rho N_A}{M}$ is the concentration of water molecules.",
            "Equating expressions gives $N = \\frac{n_0 p}{\\varepsilon_0 (\\varepsilon - 1) E}$."
        ],
        "answer": "$N = \\frac{n_0 p}{\\varepsilon_0 (\\varepsilon - 1) E} \\approx 3 \\times 10^5$",
        "solution": "**1. Polarization from Permittivity:**\nThe macroscopic polarization of water is:\n$$P = \\varepsilon_0 (\\varepsilon - 1) E$$\n\n**2. Effective Orientation Fraction:**\nIf one out of $N$ molecules were fully aligned along the field and the remaining were randomly oriented:\n$$P = \\frac{n_0}{N} p \\implies N = \\frac{n_0 p}{P} = \\frac{n_0 p}{\\varepsilon_0 (\\varepsilon - 1) E}$$\n\n**3. Numerical Evaluation:**\nFor liquid water, $n_0 = \\frac{1000\\text{ kg/m}^3}{0.018\\text{ kg/mol}} \\times 6.022 \\times 10^{23} \\approx 3.35 \\times 10^{28}\\text{ m}^{-3}$.\nWith $p = 0.62 \\times 10^{-29}\\text{ C}\\cdot\\text{m}$, $\\varepsilon = 81$ (so $\\varepsilon - 1 = 80$), and $E = 1.0\\text{ kV/cm} = 1.0 \\times 10^5\\text{ V/m}$:\n$$n_0 p = 3.35 \\times 10^{28} \\times 0.62 \\times 10^{-29} \\approx 0.208\\text{ C/m}^2$$\n$$P = 8.854 \\times 10^{-12} \\times 80 \\times 1.0 \\times 10^5 = 7.08 \\times 10^{-5}\\text{ C/m}^2$$\n$$N = \\frac{0.208}{7.08 \\times 10^{-5}} \\approx 2.94 \\times 10^5 \\approx 3 \\times 10^5$$",
        "tags": ["water dipole", "polarization", "dielectric permittivity", "dipole orientation"]
    },
    {
        "id": "3.72",
        "title": "Interaction Between a Polar and a Non-Polar Molecule",
        "difficulty": 3,
        "question": "A non-polar molecule with polarizability $\\beta$ is located at a great distance $l$ from a polar molecule with electric moment $\\mathbf{p}$. Find the magnitude of the interaction force between the molecules if the vector $\\mathbf{p}$ is oriented along the straight line passing through both molecules.",
        "hints": [
            "The electric field of the polar molecule at distance $l$ along its axis is $E = \\frac{2p}{4\\pi\\varepsilon_0 l^3}$.",
            "The non-polar molecule acquires an induced dipole moment $p_{\\text{ind}} = \\beta E = \\frac{2\\beta p}{4\\pi\\varepsilon_0 l^3}$.",
            "The interaction force is $F = p_{\\text{ind}} \\left|\\frac{dE}{dl}\\right| = \\left( \\frac{2\\beta p}{4\\pi\\varepsilon_0 l^3} \\right) \\left( \\frac{6p}{4\\pi\\varepsilon_0 l^4} \\right) = \\frac{12 \\beta p^2}{(4\\pi\\varepsilon_0)^2 l^7}$."
        ],
        "answer": "$F = \\frac{12 \\beta p^2}{(4\\pi\\varepsilon_0)^2 l^7}$",
        "solution": "**1. Electric Field of Polar Molecule:**\nAlong the axis of dipole $\\mathbf{p}$, the field at distance $l$ is:\n$$E(l) = \\frac{2p}{4\\pi\\varepsilon_0 l^3}$$\n\n**2. Induced Dipole Moment:**\nThe non-polar molecule develops an induced dipole moment:\n$$p_{\\text{ind}} = \\beta E = \\frac{2\\beta p}{4\\pi\\varepsilon_0 l^3}$$\n\n**3. Attractive Force:**\nThe force exerted on the induced dipole by the inhomogeneous field $E(l)$ is:\n$$F = p_{\\text{ind}} \\left| \\frac{dE}{dl} \\right| = p_{\\text{ind}} \\left( \\frac{6p}{4\\pi\\varepsilon_0 l^4} \\right)$$\nSubstituting $p_{\\text{ind}}$:\n$$F = \\left( \\frac{2\\beta p}{4\\pi\\varepsilon_0 l^3} \\right) \\left( \\frac{6p}{4\\pi\\varepsilon_0 l^4} \\right) = \\frac{12 \\beta p^2}{(4\\pi\\varepsilon_0)^2 l^7}$$",
        "tags": ["Debye induction force", "polarizability", "induced dipole", "van der Waals force"]
    },
    {
        "id": "3.73",
        "title": "Force on a Non-Polar Molecule on the Axis of a Charged Ring",
        "difficulty": 3,
        "question": "A non-polar molecule is located at the axis of a thin uniformly charged ring of radius $R$. At what distance $x$ from the ring's centre is the magnitude of the force $F$ acting on the given molecule:\n(a) equal to zero;\n(b) maximum?",
        "hints": [
            "Induced dipole moment is $p = \\beta E(x)$, so force is $F = p \\frac{dE}{dx} = \\beta E \\frac{dE}{dx} = \\frac{1}{2} \\beta \\frac{d(E^2)}{dx}$.",
            "(a) Force is zero where $E = 0$ ($x = 0$) or where $\\frac{dE}{dx} = 0$ ($x = R/\\sqrt{2}$) or $x \\to \\infty$.",
            "(b) Force is maximum where $\\frac{dF}{dx} = 0 \\implies \\frac{d^2(E^2)}{dx^2} = 0$."
        ],
        "answer": "(a) $x = 0$ and $x = \\frac{R}{\\sqrt{2}}$; (b) $x = R \\sqrt{\\frac{5 - \\sqrt{13}}{6}} \\approx 0.48 R$",
        "solution": "**1. Force Expression:**\nFor a non-polar molecule of polarizability $\\beta$, the induced dipole moment is $p(x) = \\beta E(x)$. The force along the axis is:\n$$F(x) = p(x) \\frac{dE}{dx} = \\beta E(x) \\frac{dE}{dx} = \\frac{1}{2} \\beta \\frac{d}{dx} [E(x)^2]$$\n\n**2. Zeros of Force (Part a):**\nThe force vanishes when either $E = 0$ or $\\frac{dE}{dx} = 0$:\n- $E(0) = 0 \\implies x = 0$\n- From problem 3.9, $\\frac{dE}{dx} = 0$ occurs at the field maximum $x = \\frac{R}{\\sqrt{2}}$.\nThus $F = 0$ at $x = 0$ and $x = R/\\sqrt{2}$.\n\n**3. Maximum Force (Part b):**\nWith $E(x) = \\frac{q x}{4\\pi\\varepsilon_0 (R^2 + x^2)^{3/2}}$:\n$$E(x)^2 \\propto \\frac{x^2}{(R^2 + x^2)^3}$$\nSetting $\\frac{d^2(E^2)}{dx^2} = 0$ gives $x \\approx 0.48 R$.",
        "tags": ["non-polar molecule", "charged ring", "force profile", "extrema"]
    },
    {
        "id": "3.74",
        "title": "Polarization and Bound Charge in Dielectric Ball with Point Charge",
        "difficulty": 2,
        "question": "A point charge $q$ is located at the centre of a ball made of uniform isotropic dielectric with permittivity $\\varepsilon$. Find the polarization $\\mathbf{P}$ as a function of the radius vector $\\mathbf{r}$ relative to the centre, as well as the bound charge $q'$ inside a sphere whose radius is less than the radius of the ball.",
        "hints": [
            "Electric displacement: $\\mathbf{D} = \\frac{q}{4\\pi r^3} \\mathbf{r}$.",
            "Electric field: $\\mathbf{E} = \\frac{\\mathbf{D}}{\\varepsilon_0 \\varepsilon} = \\frac{q}{4\\pi\\varepsilon_0 \\varepsilon r^3} \\mathbf{r}$.",
            "Polarization: $\\mathbf{P} = \\mathbf{D} - \\varepsilon_0 \\mathbf{E} = \\frac{\\varepsilon - 1}{4\\pi\\varepsilon} \\frac{q}{r^3} \\mathbf{r}$, and bound charge inside is $q' = -\\oint \\mathbf{P} \\cdot d\\mathbf{S} = -q \\frac{\\varepsilon - 1}{\\varepsilon}$."
        ],
        "answer": "$\\mathbf{P}(\\mathbf{r}) = \\frac{\\varepsilon - 1}{4\\pi\\varepsilon} \\frac{q}{r^3} \\mathbf{r}; \\quad q' = -q \\frac{\\varepsilon - 1}{\\varepsilon}$",
        "solution": "**1. Displacement and Electric Field:**\nBy Gauss's theorem for $\\mathbf{D}$, for any concentric sphere of radius $r$ inside the dielectric ball:\n$$\\oint \\mathbf{D} \\cdot d\\mathbf{S} = q \\implies 4\\pi r^2 D = q \\implies \\mathbf{D} = \\frac{q}{4\\pi r^3} \\mathbf{r}$$\nThe electric field in the dielectric is:\n$$\\mathbf{E} = \\frac{\\mathbf{D}}{\\varepsilon_0 \\varepsilon} = \\frac{q}{4\\pi\\varepsilon_0 \\varepsilon r^3} \\mathbf{r}$$\n\n**2. Polarization Vector:**\n$$\\mathbf{P} = \\mathbf{D} - \\varepsilon_0 \\mathbf{E} = \\mathbf{D} \\left( 1 - \\frac{1}{\\varepsilon} \\right) = \\frac{\\varepsilon - 1}{\\varepsilon} \\mathbf{D} = \\frac{\\varepsilon - 1}{4\\pi\\varepsilon} \\frac{q}{r^3} \\mathbf{r}$$\n\n**3. Bound Charge Enclosed:**\nBy the divergence theorem for polarization:\n$$q' = -\\oint_S \\mathbf{P} \\cdot d\\mathbf{S} = -P (4\\pi r^2) = -\\left( \\frac{\\varepsilon - 1}{4\\pi\\varepsilon} \\frac{q}{r^2} \\right) (4\\pi r^2) = -q \\frac{\\varepsilon - 1}{\\varepsilon}$$",
        "tags": ["polarization vector", "bound charge", "dielectric sphere", "displacement"]
    },
    {
        "id": "3.75",
        "title": "Bound Surface Charge at Conductor-Dielectric Interface",
        "difficulty": 2,
        "question": "Demonstrate that at a dielectric-conductor interface the surface density of the dielectric's bound charge is $\\sigma' = -\\sigma \\frac{\\varepsilon - 1}{\\varepsilon}$, where $\\varepsilon$ is the permittivity of the dielectric and $\\sigma$ is the surface density of the free charge on the conductor.",
        "hints": [
            "Inside the conductor: $\\mathbf{E} = 0, \\mathbf{D} = 0, \\mathbf{P} = 0$.",
            "In the dielectric just outside the conductor: $D_n = \\sigma$, so $E_n = \\frac{\\sigma}{\\varepsilon_0 \\varepsilon}$.",
            "The bound surface charge is $\\sigma' = -P_n = -(\\varepsilon_0 (\\varepsilon - 1) E_n) = -\\sigma \\frac{\\varepsilon - 1}{\\varepsilon}$."
        ],
        "answer": "$\\sigma' = -\\sigma \\frac{\\varepsilon - 1}{\\varepsilon}$",
        "solution": "**1. Boundary Conditions:**\nLet the normal $\\mathbf{n}$ point from the conductor into the dielectric.\nInside the conductor, $\\mathbf{E}_1 = 0$ and $\\mathbf{D}_1 = 0$.\nIn the dielectric just outside the conductor:\n$$D_n = \\sigma$$\nwhere $\\sigma$ is the surface density of extraneous (free) charge on the conductor.\n\n**2. Electric Field and Polarization:**\n$$E_n = \\frac{D_n}{\\varepsilon_0 \\varepsilon} = \\frac{\\sigma}{\\varepsilon_0 \\varepsilon}$$\nThe polarization vector in the dielectric is:\n$$P_n = \\varepsilon_0 (\\varepsilon - 1) E_n = \\varepsilon_0 (\\varepsilon - 1) \\frac{\\sigma}{\\varepsilon_0 \\varepsilon} = \\sigma \\frac{\\varepsilon - 1}{\\varepsilon}$$\n\n**3. Bound Surface Charge Density:**\nBy definition, the bound surface charge density is:\n$$\\sigma' = -P_n = -\\sigma \\frac{\\varepsilon - 1}{\\varepsilon}$$",
        "tags": ["bound charge", "dielectric-conductor interface", "polarization", "boundary condition"]
    }
]
