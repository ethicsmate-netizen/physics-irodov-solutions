"""
part3_ch3_1b.py
Curated problems 3.26 to 3.53 (28 problems) of Irodov Chapter 3.1:
Constant Electric Field in Vacuum (Part B).
"""

CH3_1B_CURATED = [
    {
        "id": "3.26",
        "title": "Electric Field of a Uniformly Charged Cylinder",
        "difficulty": 1,
        "question": "An infinitely long cylinder of radius $R$ is uniformly charged with volume density $\\rho$. Find the electric field strength as a function of distance $r$ from the axis.",
        "hints": [
            "Use cylindrical symmetry and choose a coaxial Gaussian cylinder of length $l$ and radius $r$.",
            "The flux is $\\Phi = 2\\pi r l E(r)$.",
            "Inside ($r \\le R$): $q_{\\text{enc}} = \\rho \\pi r^2 l$. Outside ($r \\ge R$): $q_{\\text{enc}} = \\rho \\pi R^2 l$."
        ],
        "answer": "$E(r) = \\frac{\\rho r}{2\\varepsilon_0}$ for $r \\le R$; $\\quad E(r) = \\frac{\\rho R^2}{2\\varepsilon_0 r}$ for $r \\ge R$",
        "solution": "**1. Gauss's Law Application:**\nBy cylindrical symmetry, $\\mathbf{E}$ is everywhere directed radially away from the axis and depends only on $r$. Through a coaxial Gaussian cylinder of radius $r$ and length $l$:\n$$\\oint \\mathbf{E} \\cdot d\\mathbf{S} = 2\\pi r l E(r) = \\frac{q_{\\text{enc}}}{\\varepsilon_0}$$\n\n**2. Inside the Cylinder ($r \\le R$):**\n$$q_{\\text{enc}} = \\rho \\cdot (\\pi r^2 l)$$\n$$2\\pi r l E(r) = \\frac{\\rho \\pi r^2 l}{\\varepsilon_0} \\implies E(r) = \\frac{\\rho r}{2\\varepsilon_0}$$\n\n**3. Outside the Cylinder ($r \\ge R$):**\n$$q_{\\text{enc}} = \\rho \\cdot (\\pi R^2 l)$$\n$$2\\pi r l E(r) = \\frac{\\rho \\pi R^2 l}{\\varepsilon_0} \\implies E(r) = \\frac{\\rho R^2}{2\\varepsilon_0 r}$$",
        "tags": ["charged cylinder", "Gauss law", "cylindrical symmetry", "volume charge"]
    },
    {
        "id": "3.27",
        "title": "Uniform Field Inside a Spherical Cavity in a Charged Ball",
        "difficulty": 2,
        "question": "Inside a ball of radius $R$ with uniform volume density $\\rho$, there is a spherical cavity whose centre is shifted by vector $\\mathbf{a}$ relative to the ball's centre. Find the electric field strength vector inside the cavity.",
        "hints": [
            "Use the superposition principle: the configuration is a solid ball of charge $+\\rho$ plus a smaller sphere of charge $-\\rho$ filling the cavity.",
            "Inside a solid ball of charge $+\\rho$, $\\mathbf{E}_+(\\mathbf{r}) = \\frac{\\rho}{3\\varepsilon_0} \\mathbf{r}$.",
            "Inside the negative sphere centered at $\\mathbf{a}$, $\\mathbf{E}_-(\\mathbf{r}) = -\\frac{\\rho}{3\\varepsilon_0} (\\mathbf{r} - \\mathbf{a})$. Sum them."
        ],
        "answer": "$\\mathbf{E} = \\frac{\\rho}{3\\varepsilon_0} \\mathbf{a}$ (completely uniform inside the cavity)",
        "solution": "**1. Principle of Superposition:**\nThe hollow sphere with a cavity can be represented as the sum of:\n- A complete solid sphere of charge density $+\\rho$ centered at the origin $O$.\n- A smaller sphere of charge density $-\\rho$ occupying the cavity, centered at position $\\mathbf{a}$.\n\n**2. Field Inside the Cavity:**\nAt any point $\\mathbf{r}$ inside the cavity:\n- The field due to the large solid sphere is:\n  $$\\mathbf{E}_+(\\mathbf{r}) = \\frac{\\rho}{3\\varepsilon_0} \\mathbf{r}$$\n- The field due to the cavity sphere of density $-\\rho$ is:\n  $$\\mathbf{E}_-(\\mathbf{r}) = -\\frac{\\rho}{3\\varepsilon_0} (\\mathbf{r} - \\mathbf{a})$$\n\n**3. Net Field:**\n$$\\mathbf{E} = \\mathbf{E}_+ + \\mathbf{E}_- = \\frac{\\rho}{3\\varepsilon_0} \\mathbf{r} - \\frac{\\rho}{3\\varepsilon_0} (\\mathbf{r} - \\mathbf{a}) = \\frac{\\rho}{3\\varepsilon_0} \\mathbf{a}$$\nRemarkably, the field inside the cavity is strictly uniform, independent of position $\\mathbf{r}$, and directed parallel to the displacement vector $\\mathbf{a}$.",
        "tags": ["spherical cavity", "superposition", "uniform field", "charged ball"]
    },
    {
        "id": "3.28",
        "title": "Uniform Field Inside a Cylindrical Cavity in a Charged Cylinder",
        "difficulty": 2,
        "question": "Inside an infinitely long cylinder with uniform charge density $\\rho$, there is a cylindrical cavity whose axis is shifted by vector $\\mathbf{a}$ relative to the cylinder's axis. Find the electric field strength vector inside the cavity.",
        "hints": [
            "Superpose a solid cylinder of charge $+\\rho$ and a negative cylinder of charge $-\\rho$ occupying the cavity.",
            "Inside a solid cylinder of charge density $+\\rho$, $\\mathbf{E}_+(\\mathbf{r}) = \\frac{\\rho}{2\\varepsilon_0} \\mathbf{r}$.",
            "Inside the negative cylinder centered at $\\mathbf{a}$, $\\mathbf{E}_-(\\mathbf{r}) = -\\frac{\\rho}{2\\varepsilon_0} (\\mathbf{r} - \\mathbf{a})$."
        ],
        "answer": "$\\mathbf{E} = \\frac{\\rho}{2\\varepsilon_0} \\mathbf{a}$ (completely uniform inside the cavity)",
        "solution": "**1. Superposition Model:**\nRepresent the system as:\n- An infinite solid cylinder of charge density $+\\rho$ centered on the main axis.\n- A negative solid cylinder of charge density $-\\rho$ centered at $\\mathbf{a}$.\n\n**2. Field in the Cavity:**\nAt any point $\\mathbf{r}$ within the cavity:\n$$\\mathbf{E}(\\mathbf{r}) = \\mathbf{E}_+(\\mathbf{r}) + \\mathbf{E}_-(\\mathbf{r}) = \\frac{\\rho}{2\\varepsilon_0} \\mathbf{r} - \\frac{\\rho}{2\\varepsilon_0} (\\mathbf{r} - \\mathbf{a}) = \\frac{\\rho}{2\\varepsilon_0} \\mathbf{a}$$\nThe electric field inside the cylindrical cavity is uniform and parallel to $\\mathbf{a}$.",
        "tags": ["cylindrical cavity", "superposition", "uniform electric field", "Gauss law"]
    },
    {
        "id": "3.29",
        "title": "Electric Field of a Uniformly Charged Infinite Slab",
        "difficulty": 1,
        "question": "There is an infinite plane layer of thickness $2d$ with uniform volume charge density $\\rho$. Find the electric field strength as a function of distance $x$ from the midplane.",
        "hints": [
            "Use planar symmetry with a Gaussian pillbox centered at $x = 0$ extending to $\\pm x$.",
            "Inside the layer ($|x| \\le d$): $2 E(x) S = \\frac{\\rho (2x S)}{\\varepsilon_0} \\implies E(x) = \\frac{\\rho x}{\\varepsilon_0}$.",
            "Outside the layer ($|x| \\ge d$): $2 E(x) S = \\frac{\\rho (2d S)}{\\varepsilon_0} \\implies E(x) = \\frac{\\rho d}{\\varepsilon_0}$."
        ],
        "answer": "$E(x) = \\frac{\\rho x}{\\varepsilon_0}$ for $|x| \\le d$; $\\quad E(x) = \\frac{\\rho d}{\\varepsilon_0} \\operatorname{sgn}(x)$ for $|x| \\ge d$",
        "solution": "**1. Planar Symmetry:**\nBy symmetry, $\\mathbf{E}$ is perpendicular to the layer and points in opposite directions for $x > 0$ and $x < 0$:\n$$\\mathbf{E}(x) = E(x) \\operatorname{sgn}(x) \\mathbf{i}, \\quad E(0) = 0$$\n\n**2. Gaussian Surface:**\nChoose a cylinder of cross-sectional area $S$ extending symmetrically from $-x$ to $+x$ across the midplane:\n$$\\oint \\mathbf{E} \\cdot d\\mathbf{S} = 2 E(x) S = \\frac{q_{\\text{enc}}}{\\varepsilon_0}$$\n- For $|x| \\le d$:\n  $$q_{\\text{enc}} = \\rho (2x S) \\implies 2 E(x) S = \\frac{2\\rho x S}{\\varepsilon_0} \\implies E(x) = \\frac{\\rho x}{\\varepsilon_0}$$\n- For $|x| \\ge d$:\n  $$q_{\\text{enc}} = \\rho (2d S) \\implies 2 E(x) S = \\frac{2\\rho d S}{\\varepsilon_0} \\implies E(x) = \\frac{\\rho d}{\\varepsilon_0}$$",
        "tags": ["charged slab", "planar symmetry", "Gauss law", "stepwise field"]
    },
    {
        "id": "3.30",
        "title": "Field of a Slab with Cosine Charge Density",
        "difficulty": 2,
        "question": "An infinite plane layer of thickness $2d$ has a non-uniform charge density $\\rho = \\rho_0 \\cos(\\alpha x)$, where $x$ is the distance from the midplane, and $\\alpha = \\pi / (2d)$. Find the electric field strength as a function of $x$.",
        "hints": [
            "Use Gauss's law in differential form: $\\frac{dE}{dx} = \\frac{\\rho(x)}{\\varepsilon_0} = \\frac{\\rho_0}{\\varepsilon_0} \\cos(\\alpha x)$.",
            "Integrate with boundary condition $E(0) = 0$ by symmetry.",
            "For $|x| \\le d$, $E(x) = \\frac{\\rho_0}{\\alpha \\varepsilon_0} \\sin(\\alpha x)$."
        ],
        "answer": "$E(x) = \\frac{\\rho_0}{\\alpha \\varepsilon_0} \\sin(\\alpha x)$ for $|x| \\le d$; $\\quad E(x) = \\frac{\\rho_0}{\\alpha \\varepsilon_0} \\operatorname{sgn}(x)$ for $|x| \\ge d$",
        "solution": "**1. Differential Gauss's Law:**\nFrom Maxwell's first equation $\\nabla \\cdot \\mathbf{E} = \\frac{\\rho}{\\varepsilon_0}$ in 1D:\n$$\\frac{dE}{dx} = \\frac{\\rho_0}{\\varepsilon_0} \\cos(\\alpha x)$$\nIntegrating with $E(0) = 0$:\n$$E(x) = \\frac{\\rho_0}{\\varepsilon_0} \\int_0^x \\cos(\\alpha x') dx' = \\frac{\\rho_0}{\\alpha \\varepsilon_0} \\sin(\\alpha x)$$\n\n**2. Outside the Slab ($|x| \\ge d$):**\nAt the boundary $x = d$, with $\\alpha d = \\pi/2$, $\\sin(\\pi/2) = 1$:\n$$E(x) = \\frac{\\rho_0}{\\alpha \\varepsilon_0} \\operatorname{sgn}(x)$$",
        "tags": ["non-uniform slab", "cosine charge", "Gauss law", "differential equation"]
    },
    {
        "id": "3.31",
        "title": "Charge Density from Given Electric Field",
        "difficulty": 1,
        "question": "An electric field in a certain region of space is given by $\\mathbf{E} = a(x\\mathbf{i} + y\\mathbf{j})$, where $a$ is a constant. Find the volume charge density $\\rho$.",
        "hints": [
            "Use Gauss's law in differential form: $\\nabla \\cdot \\mathbf{E} = \\frac{\\rho}{\\varepsilon_0}$.",
            "Calculate divergence: $\\nabla \\cdot \\mathbf{E} = \\frac{\\partial E_x}{\\partial x} + \\frac{\\partial E_y}{\\partial y} + \\frac{\\partial E_z}{\\partial z}$.",
            "Substitute $\\frac{\\partial (ax)}{\\partial x} = a$ and $\\frac{\\partial (ay)}{\\partial y} = a$."
        ],
        "answer": "$\\rho = 2a\\varepsilon_0$",
        "solution": "**1. Divergence of Field:**\nGiven $\\mathbf{E} = ax\\mathbf{i} + ay\\mathbf{j}$:\n$$\\nabla \\cdot \\mathbf{E} = \\frac{\\partial E_x}{\\partial x} + \\frac{\\partial E_y}{\\partial y} + \\frac{\\partial E_z}{\\partial z} = \\frac{\\partial}{\\partial x}(ax) + \\frac{\\partial}{\\partial y}(ay) + 0 = a + a = 2a$$\n\n**2. Charge Density:**\nBy Poisson's / Gauss's equation:\n$$\\rho = \\varepsilon_0 (\\nabla \\cdot \\mathbf{E}) = 2a\\varepsilon_0$$",
        "tags": ["divergence", "charge density", "Gauss law in differential form", "Poisson equation"]
    },
    {
        "id": "3.32",
        "title": "Charge Density of a Transverse Cross-Coupled Field",
        "difficulty": 1,
        "question": "An electric field is given by $\\mathbf{E} = a(y\\mathbf{i} + x\\mathbf{j})$, where $a$ is a constant. Find the volume charge density $\\rho$ and the flux through a cylinder of radius $R$ and height $h$ centered on the $z$-axis.",
        "hints": [
            "Calculate divergence: $\\nabla \\cdot \\mathbf{E} = \\frac{\\partial (ay)}{\\partial x} + \\frac{\\partial (ax)}{\\partial y} = 0 + 0 = 0$.",
            "Since $\\nabla \\cdot \\mathbf{E} = 0$ everywhere, $\\rho = 0$.",
            "By the divergence theorem, the net flux through any closed surface is zero."
        ],
        "answer": "$\\rho = 0, \\quad \\Phi = 0$",
        "solution": "**1. Volume Charge Density:**\n$$\\rho = \\varepsilon_0 \\nabla \\cdot \\mathbf{E} = \\varepsilon_0 \\left( \\frac{\\partial(ay)}{\\partial x} + \\frac{\\partial(ax)}{\\partial y} \\right) = \\varepsilon_0 (0 + 0) = 0$$\n\n**2. Total Flux:**\nBy Gauss's divergence theorem:\n$$\\Phi = \\oint_S \\mathbf{E} \\cdot d\\mathbf{S} = \\int_V (\\nabla \\cdot \\mathbf{E}) \\, dV = 0$$",
        "tags": ["divergence", "zero charge density", "solenoidal field", "Gauss theorem"]
    },
    {
        "id": "3.33",
        "title": "Potential of a Uniformly Charged Sphere",
        "difficulty": 2,
        "question": "Find the electric field potential $\\varphi(r)$ of a uniformly charged ball of radius $R$ with total charge $q$, both inside and outside the ball, taking $\\varphi(\\infty) = 0$.",
        "hints": [
            "Electric field outside is $E(r) = \\frac{q}{4\\pi\\varepsilon_0 r^2}$; potential is $\\varphi(r) = \\frac{q}{4\\pi\\varepsilon_0 r}$ for $r \\ge R$.",
            "Inside: $E(r) = \\frac{q r}{4\\pi\\varepsilon_0 R^3}$.",
            "Integrate $\\varphi(r) = \\varphi(R) + \\int_r^R E(r') dr'$ to find $\\varphi(r) = \\frac{q}{8\\pi\\varepsilon_0 R} \\left(3 - \\frac{r^2}{R^2}\\right)$."
        ],
        "answer": "$\\varphi(r) = \\frac{q}{4\\pi\\varepsilon_0 r}$ for $r \\ge R$; $\\quad \\varphi(r) = \\frac{q}{8\\pi\\varepsilon_0 R} \\left( 3 - \\frac{r^2}{R^2} \\right)$ for $r \\le R$",
        "solution": "**1. Potential Outside ($r \\ge R$):**\n$$\\varphi(r) = \\int_r^\\infty E(r') dr' = \\int_r^\\infty \\frac{q}{4\\pi\\varepsilon_0 r'^2} dr' = \\frac{q}{4\\pi\\varepsilon_0 r}$$\nAt the surface $r = R$:\n$$\\varphi(R) = \\frac{q}{4\\pi\\varepsilon_0 R}$$\n\n**2. Potential Inside ($r \\le R$):**\n$$\\varphi(r) - \\varphi(R) = \\int_r^R E(r') dr' = \\int_r^R \\frac{q r'}{4\\pi\\varepsilon_0 R^3} dr' = \\frac{q}{4\\pi\\varepsilon_0 R^3} \\left[ \\frac{R^2 - r^2}{2} \\right]$$\n$$\\varphi(r) = \\frac{q}{4\\pi\\varepsilon_0 R} + \\frac{q(R^2 - r^2)}{8\\pi\\varepsilon_0 R^3} = \\frac{q}{8\\pi\\varepsilon_0 R} \\left( 3 - \\frac{r^2}{R^2} \\right)$$\nAt the center $r = 0$, $\\varphi(0) = \\frac{3q}{8\\pi\\varepsilon_0 R} = \\frac{3}{2}\\varphi(R)$.",
        "tags": ["potential", "charged sphere", "integration", "Gauss law"]
    },
    {
        "id": "3.34",
        "title": "Potential at Center of a Uniformly Charged Hemisphere",
        "difficulty": 1,
        "question": "Find the electric field potential at the center of curvature of a thin hemisphere of radius $R$ carrying a uniform surface charge of density $\\sigma$.",
        "hints": [
            "Every point on the hemisphere is at the exact same distance $R$ from the center of curvature.",
            "The potential is simply $\\varphi = \\int \\frac{\\sigma \\, dS}{4\\pi\\varepsilon_0 R} = \\frac{\\sigma}{4\\pi\\varepsilon_0 R} S$.",
            "Area of hemisphere is $S = 2\\pi R^2$."
        ],
        "answer": "$\\varphi = \\frac{\\sigma R}{2\\varepsilon_0}$",
        "solution": "**1. Potential from Surface Charge:**\nBecause every element of the hemisphere lies at a constant distance $r = R$ from the center of curvature:\n$$\\varphi = \\int_S \\frac{dq}{4\\pi\\varepsilon_0 R} = \\frac{1}{4\\pi\\varepsilon_0 R} \\int_S \\sigma \\, dS = \\frac{\\sigma S}{4\\pi\\varepsilon_0 R}$$\n\n**2. Area of Hemisphere:**\n$$S = 2\\pi R^2$$\n$$\\varphi = \\frac{\\sigma (2\\pi R^2)}{4\\pi\\varepsilon_0 R} = \\frac{\\sigma R}{2\\varepsilon_0}$$",
        "tags": ["hemisphere", "electrostatic potential", "surface charge", "center of curvature"]
    },
    {
        "id": "3.35",
        "title": "Potential of Hyperbolic Field",
        "difficulty": 1,
        "question": "Find the potential $\\varphi(x, y)$ of an electrostatic field $\\mathbf{E} = a(y\\mathbf{i} + x\\mathbf{j})$, where $a$ is a constant.",
        "hints": [
            "Use $\\mathbf{E} = -\\nabla \\varphi$, which means $-\\frac{\\partial \\varphi}{\\partial x} = ay$ and $-\\frac{\\partial \\varphi}{\\partial y} = ax$.",
            "Integrate $-\\frac{\\partial \\varphi}{\\partial x} = ay$ to get $\\varphi(x, y) = -axy + f(y)$.",
            "Differentiate with respect to $y$ to show $f'(y) = 0$, so $\\varphi = -axy + C$."
        ],
        "answer": "$\\varphi(x, y) = -axy + \\text{const}$",
        "solution": "**1. Component Relations:**\nFrom $\\mathbf{E} = -\\nabla\\varphi$:\n$$\\frac{\\partial \\varphi}{\\partial x} = -E_x = -ay$$\n$$\\frac{\\partial \\varphi}{\\partial y} = -E_y = -ax$$\n\n**2. Integration:**\n$$\\varphi(x, y) = \\int (-ay) dx = -axy + f(y)$$\nDifferentiating with respect to $y$:\n$$\\frac{\\partial \\varphi}{\\partial y} = -ax + f'(y) = -ax \\implies f'(y) = 0 \\implies f(y) = C$$\n$$\\varphi(x, y) = -axy + \\text{const}$$",
        "tags": ["potential", "gradient", "line integral", "hyperbolic field"]
    },
    {
        "id": "3.36",
        "title": "Electric Field from Quadrupolar Potential",
        "difficulty": 1,
        "question": "The field potential in a certain region of space has the form $\\varphi = a(x^2 - y^2)$, where $a$ is a constant. Find the vector of the electric field strength $\\mathbf{E}$ and its magnitude.",
        "hints": [
            "Use $\\mathbf{E} = -\\nabla\\varphi = -\\left(\\frac{\\partial \\varphi}{\\partial x}\\mathbf{i} + \\frac{\\partial \\varphi}{\\partial y}\\mathbf{j}\\right)$.",
            "Compute: $\\frac{\\partial \\varphi}{\\partial x} = 2ax$ and $\\frac{\\partial \\varphi}{\\partial y} = -2ay$.",
            "Combine into vector $\\mathbf{E} = -2a(x\\mathbf{i} - y\\mathbf{j})$ and find its norm."
        ],
        "answer": "$\\mathbf{E} = -2a(x\\mathbf{i} - y\\mathbf{j}), \\quad E = 2a\\sqrt{x^2 + y^2}$",
        "solution": "**1. Gradient Calculation:**\n$$\\mathbf{E} = -\\nabla\\varphi = -\\left( \\frac{\\partial \\varphi}{\\partial x}\\mathbf{i} + \\frac{\\partial \\varphi}{\\partial y}\\mathbf{j} \\right)$$\n$$\\frac{\\partial \\varphi}{\\partial x} = 2ax, \\quad \\frac{\\partial \\varphi}{\\partial y} = -2ay$$\n$$\\mathbf{E} = -2a(x\\mathbf{i} - y\\mathbf{j})$$\n\n**2. Field Magnitude:**\n$$E = \\sqrt{(-2ax)^2 + (2ay)^2} = 2a\\sqrt{x^2 + y^2}$$",
        "tags": ["electric field", "gradient", "quadrupole potential", "vector calculus"]
    },
    {
        "id": "3.37",
        "title": "Field Vector and Equipotential Surfaces of Quadratic Potential",
        "difficulty": 2,
        "question": "The field potential is given by $\\varphi = a(x^2 + y^2) + b z^2$, where $a$ and $b$ are constants. Find the electric field strength vector $\\mathbf{E}$, its magnitude, and the shape of the equipotential surfaces for:\n(a) $a > 0, b > 0$;\n(b) $a > 0, b < 0$.",
        "hints": [
            "Compute $\\mathbf{E} = -\\nabla\\varphi = -2(ax\\mathbf{i} + ay\\mathbf{j} + bz\\mathbf{k})$.",
            "Magnitude is $E = 2\\sqrt{a^2(x^2 + y^2) + b^2 z^2}$.",
            "Equipotential equation: $a(x^2 + y^2) + b z^2 = \\varphi_0$. If $a>0, b>0$, it is an ellipsoid of revolution; if $a>0, b<0$, it is a hyperboloid."
        ],
        "answer": "$\\mathbf{E} = -2(ax\\mathbf{i} + ay\\mathbf{j} + bz\\mathbf{k})$; (a) ellipsoid of revolution; (b) hyperboloid of revolution",
        "solution": "**1. Electric Field Vector:**\n$$\\mathbf{E} = -\\nabla\\varphi = -\\left( \\frac{\\partial\\varphi}{\\partial x}\\mathbf{i} + \\frac{\\partial\\varphi}{\\partial y}\\mathbf{j} + \\frac{\\partial\\varphi}{\\partial z}\\mathbf{k} \\right) = -2(ax\\mathbf{i} + ay\\mathbf{j} + bz\\mathbf{k})$$\n$$E = 2\\sqrt{a^2(x^2 + y^2) + b^2 z^2}$$\n\n**2. Equipotential Surfaces:**\nThe equation of an equipotential surface is:\n$$a(x^2 + y^2) + b z^2 = \\varphi = \\text{const}$$\n- **Case (a) ($a > 0, b > 0$):**\n  $$\\frac{x^2 + y^2}{\\varphi / a} + \\frac{z^2}{\\varphi / b} = 1$$\n  For $\\varphi > 0$, this represents an **ellipsoid of revolution** about the $z$-axis with semiaxes $\\sqrt{\\varphi/a}$ and $\\sqrt{\\varphi/b}$.\n- **Case (b) ($a > 0, b < 0$):**\n  For $\\varphi > 0$, it is a single-sheeted hyperboloid of revolution; for $\\varphi = 0$, a circular cone; for $\\varphi < 0$, a two-sheeted hyperboloid of revolution.",
        "tags": ["equipotential surfaces", "ellipsoid of revolution", "hyperboloid", "gradient"]
    },
    {
        "id": "3.38",
        "title": "Potential at Center and Profile Inside a Charged Ball",
        "difficulty": 2,
        "question": "A charge $q$ is uniformly distributed over the volume of a sphere of radius $R$. Assuming the permittivity to be equal to unity throughout, find the potential:\n(a) at the centre of the sphere;\n(b) inside the sphere as a function of distance $r$ from its centre.",
        "hints": [
            "(a) Divide into spherical shells of radius $r'$ and charge $dq = \\frac{3q}{R^3} r'^2 dr'$. Integrate $\\varphi_0 = \\int_0^R \\frac{dq}{4\\pi\\varepsilon_0 r'}$.",
            "(b) Use the relation $\\varphi(r) = \\varphi_0 \\left(1 - \\frac{r^2}{3R^2}\\right)$.",
            "Verify that at $r = R$, $\\varphi(R) = \\frac{2}{3}\\varphi_0 = \\frac{q}{4\\pi\\varepsilon_0 R}$."
        ],
        "answer": "(a) $\\varphi_0 = \\frac{3q}{8\\pi\\varepsilon_0 R}$; (b) $\\varphi(r) = \\varphi_0 \\left( 1 - \\frac{r^2}{3R^2} \\right)$ for $r \\le R$",
        "solution": "**1. Potential at the Center (Part a):**\n$$\\varphi_0 = \\int_0^R \\frac{dq(r')}{4\\pi\\varepsilon_0 r'} = \\int_0^R \\frac{\\rho (4\\pi r'^2 dr')}{4\\pi\\varepsilon_0 r'} = \\frac{\\rho}{\\varepsilon_0} \\int_0^R r' dr' = \\frac{\\rho R^2}{2\\varepsilon_0}$$\nSubstituting $\\rho = \\frac{q}{\\frac{4}{3}\\pi R^3} = \\frac{3q}{4\\pi R^3}$:\n$$\\varphi_0 = \\frac{3q}{8\\pi\\varepsilon_0 R}$$\n\n**2. Potential Inside the Sphere (Part b):**\nUsing $\\varphi(r) = \\varphi_0 - \\int_0^r E(r') dr'$ with $E(r') = \\frac{q r'}{4\\pi\\varepsilon_0 R^3}$:\n$$\\varphi(r) = \\varphi_0 - \\frac{q r^2}{8\\pi\\varepsilon_0 R^3} = \\varphi_0 - \\frac{\\varphi_0}{3} \\frac{r^2}{R^2} = \\varphi_0 \\left( 1 - \\frac{r^2}{3R^2} \\right)$$",
        "tags": ["potential inside sphere", "charged sphere", "Poisson equation", "electrostatic potential"]
    },
    {
        "id": "3.39",
        "title": "Potential and Electric Field of a Point Dipole",
        "difficulty": 2,
        "question": "Demonstrate that the potential of the field generated by a dipole with electric moment $\\mathbf{p}$ may be represented as $\\varphi = \\frac{\\mathbf{p} \\cdot \\mathbf{r}}{4\\pi\\varepsilon_0 r^3}$. Using this expression, find the magnitude of the electric field strength vector as a function of $r$ and $\\theta$.",
        "hints": [
            "In spherical coordinates with $\\mathbf{p}$ along the $z$-axis, $\\varphi(r, \\theta) = \\frac{p \\cos\\theta}{4\\pi\\varepsilon_0 r^2}$.",
            "Calculate components: $E_r = -\\frac{\\partial \\varphi}{\\partial r} = \\frac{2p \\cos\\theta}{4\\pi\\varepsilon_0 r^3}$ and $E_\\theta = -\\frac{1}{r}\\frac{\\partial \\varphi}{\\partial \\theta} = \\frac{p \\sin\\theta}{4\\pi\\varepsilon_0 r^3}$.",
            "Find the magnitude $E = \\sqrt{E_r^2 + E_\\theta^2} = \\frac{p}{4\\pi\\varepsilon_0 r^3} \\sqrt{1 + 3\\cos^2\\theta}$."
        ],
        "answer": "$E = \\frac{p}{4\\pi\\varepsilon_0 r^3} \\sqrt{1 + 3\\cos^2\\theta}$",
        "solution": "**1. Potential of a Dipole:**\nFor two charges $\\pm q$ separated by $\\mathbf{l}$, the potential at $\\mathbf{r}$ ($r \\gg l$) is:\n$$\\varphi = \\frac{q}{4\\pi\\varepsilon_0} \\left( \\frac{1}{|\\mathbf{r} - \\mathbf{l}/2|} - \\frac{1}{|\\mathbf{r} + \\mathbf{l}/2|} \\right) \\approx \\frac{q (\\mathbf{l} \\cdot \\hat{\\mathbf{r}})}{4\\pi\\varepsilon_0 r^2} = \\frac{\\mathbf{p} \\cdot \\mathbf{r}}{4\\pi\\varepsilon_0 r^3}$$\n\n**2. Electric Field Components in Spherical Coordinates:**\nWith $\\mathbf{p} \\cdot \\mathbf{r} = p r \\cos\\theta$, we have $\\varphi(r, \\theta) = \\frac{p \\cos\\theta}{4\\pi\\varepsilon_0 r^2}$:\n$$E_r = -\\frac{\\partial \\varphi}{\\partial r} = \\frac{2p \\cos\\theta}{4\\pi\\varepsilon_0 r^3}$$\n$$E_\\theta = -\\frac{1}{r} \\frac{\\partial \\varphi}{\\partial \\theta} = \\frac{p \\sin\\theta}{4\\pi\\varepsilon_0 r^3}$$\n\n**3. Field Magnitude:**\n$$E = \\sqrt{E_r^2 + E_\\theta^2} = \\frac{p}{4\\pi\\varepsilon_0 r^3} \\sqrt{4\\cos^2\\theta + \\sin^2\\theta} = \\frac{p}{4\\pi\\varepsilon_0 r^3} \\sqrt{1 + 3\\cos^2\\theta}$$",
        "tags": ["dipole potential", "spherical coordinates", "dipole field", "multipole expansion"]
    },
    {
        "id": "3.40",
        "title": "Components of Dipole Field and Orthogonality Condition",
        "difficulty": 2,
        "question": "A point dipole with electric moment $\\mathbf{p}$ oriented in the positive direction of the $z$-axis is located at the origin of coordinates. Find the projections $E_z$ and $E_\\perp$ of the electric field strength vector. At which points is $\\mathbf{E}$ perpendicular to $\\mathbf{p}$?",
        "hints": [
            "Project $E_r$ and $E_\\theta$ onto the $z$-axis and the perpendicular plane.",
            "$E_z = E_r \\cos\\theta - E_\\theta \\sin\\theta = \\frac{p}{4\\pi\\varepsilon_0 r^3} (2\\cos^2\\theta - \\sin^2\\theta) = \\frac{p}{4\\pi\\varepsilon_0 r^3} (3\\cos^2\\theta - 1)$.",
            "Condition $\\mathbf{E} \\perp \\mathbf{p}$ means $E_z = 0 \\implies 3\\cos^2\\theta - 1 = 0 \\implies \\cos\\theta = 1/\\sqrt{3}$."
        ],
        "answer": "$E_z = \\frac{p}{4\\pi\\varepsilon_0 r^3} (3\\cos^2\\theta - 1), \\; E_\\perp = \\frac{3p}{4\\pi\\varepsilon_0 r^3} \\sin\\theta\\cos\\theta$; $\\mathbf{E} \\perp \\mathbf{p}$ at $\\cos\\theta = \\frac{1}{\\sqrt{3}}$ ($\\theta \\approx 54.7^\\circ, 123.5^\\circ$)",
        "solution": "**1. Component Projections:**\nFrom spherical coordinates:\n- Component parallel to $\\mathbf{p}$ ($z$-direction):\n  $$E_z = E_r \\cos\\theta - E_\\theta \\sin\\theta = \\frac{p}{4\\pi\\varepsilon_0 r^3} (2\\cos^2\\theta - \\sin^2\\theta) = \\frac{p}{4\\pi\\varepsilon_0 r^3} (3\\cos^2\\theta - 1)$$\n- Component perpendicular to $\\mathbf{p}$ (radial in $xy$ plane):\n  $$E_\\perp = E_r \\sin\\theta + E_\\theta \\cos\\theta = \\frac{p}{4\\pi\\varepsilon_0 r^3} (2\\cos\\theta\\sin\\theta + \\sin\\theta\\cos\\theta) = \\frac{3p}{4\\pi\\varepsilon_0 r^3} \\sin\\theta \\cos\\theta$$\n\n**2. Condition for $\\mathbf{E} \\perp \\mathbf{p}$:**\nFor the field vector to be strictly perpendicular to the dipole moment, its parallel component must vanish:\n$$E_z = 0 \\implies 3\\cos^2\\theta - 1 = 0 \\implies \\cos\\theta = \\pm \\frac{1}{\\sqrt{3}}$$\n$$\\theta_1 = \\arccos(1/\\sqrt{3}) \\approx 54.7^\\circ, \\quad \\theta_2 = 180^\\circ - 54.7^\\circ = 123.5^\\circ$$\nThese points lie on the conical surfaces of semi-vertex angle $\\theta = 54.7^\\circ$. At these points:\n$$E = E_\\perp = \\frac{p}{4\\pi\\varepsilon_0 r^3} \\sqrt{2}$$",
        "tags": ["dipole field", "field components", "orthogonality", "cone angle"]
    },
    {
        "id": "3.41",
        "title": "Spherical Equipotential of Dipole in a Uniform External Field",
        "difficulty": 2,
        "question": "A point electric dipole with moment $\\mathbf{p}$ is placed in an external uniform electric field whose strength equals $\\mathbf{E}_0$, with $\\mathbf{p} \\parallel \\mathbf{E}_0$. In this case one of the equipotential surfaces enclosing the dipole forms a sphere. Find the radius of this sphere.",
        "hints": [
            "Total potential is $\\varphi(r, \\theta) = \\frac{p \\cos\\theta}{4\\pi\\varepsilon_0 r^2} - E_0 r \\cos\\theta$.",
            "Factor out $\\cos\\theta$: $\\varphi = \\left( \\frac{p}{4\\pi\\varepsilon_0 r^2} - E_0 r \\right) \\cos\\theta$.",
            "For $\\varphi = 0$ for all $\\theta$ at radius $R$, set the bracket to zero: $R = \\left( \\frac{p}{4\\pi\\varepsilon_0 E_0} \\right)^{1/3}$."
        ],
        "answer": "$R = \\left( \\frac{p}{4\\pi\\varepsilon_0 E_0} \\right)^{1/3}$",
        "solution": "**1. Total Potential Formulation:**\nAlign the $z$-axis with the dipole moment $\\mathbf{p}$ and uniform field $\\mathbf{E}_0 = E_0 \\mathbf{k}$. The total potential is:\n$$\\varphi(r, \\theta) = \\varphi_{\\text{dipole}} + \\varphi_{\\text{ext}} = \\frac{p \\cos\\theta}{4\\pi\\varepsilon_0 r^2} - E_0 z = \\left( \\frac{p}{4\\pi\\varepsilon_0 r^2} - E_0 r \\right) \\cos\\theta$$\n\n**2. Condition for Spherical Equipotential:**\nFor the sphere $r = R$ to be an equipotential surface (specifically $\\varphi = 0$ for all $\\theta$):\n$$\\frac{p}{4\\pi\\varepsilon_0 R^2} - E_0 R = 0$$\n$$R^3 = \\frac{p}{4\\pi\\varepsilon_0 E_0} \\implies R = \\left( \\frac{p}{4\\pi\\varepsilon_0 E_0} \\right)^{1/3}$$",
        "tags": ["dipole in uniform field", "spherical equipotential", "image charge", "potential superposition"]
    },
    {
        "id": "3.42",
        "title": "Field and Potential of Two Oppositely Charged Parallel Threads",
        "difficulty": 2,
        "question": "Two thin parallel threads carry uniform charges with linear densities $+\\lambda$ and $-\\lambda$. The distance between the threads is equal to $l$. Find the potential of the electric field and the magnitude of its strength vector at a distance $r \\gg l$ at an angle $\\theta$ to the displacement vector $\\mathbf{l}$.",
        "hints": [
            "This configuration forms a 2D line dipole with 2D dipole moment per unit length $\\mathbf{p}_{2D} = \\lambda \\mathbf{l}$.",
            "Potential of a single thread is $\\varphi = -\\frac{\\lambda}{2\\pi\\varepsilon_0} \\ln r$.",
            "For a dipole pair at $r \\gg l$: $\\varphi \\approx \\frac{\\lambda l \\cos\\theta}{2\\pi\\varepsilon_0 r}$ and $E = \\frac{\\lambda l}{2\\pi\\varepsilon_0 r^2}$."
        ],
        "answer": "$\\varphi \\approx \\frac{\\lambda l \\cos\\theta}{2\\pi\\varepsilon_0 r}, \\quad E \\approx \\frac{\\lambda l}{2\\pi\\varepsilon_0 r^2}$",
        "solution": "**1. Potential of Two Line Charges:**\n$$\\varphi = \\frac{\\lambda}{2\\pi\\varepsilon_0} \\ln\\left( \\frac{r_-}{r_+} \\right)$$\nFor $r \\gg l$, with $r_\\pm \\approx r \\mp \\frac{l}{2}\\cos\\theta$:\n$$\\frac{r_-}{r_+} \\approx \\frac{r + \\frac{l}{2}\\cos\\theta}{r - \\frac{l}{2}\\cos\\theta} \\approx 1 + \\frac{l}{r}\\cos\\theta$$\n$$\\varphi \\approx \\frac{\\lambda}{2\\pi\\varepsilon_0} \\ln\\left( 1 + \\frac{l}{r}\\cos\\theta \\right) \\approx \\frac{\\lambda l \\cos\\theta}{2\\pi\\varepsilon_0 r}$$\n\n**2. Electric Field Components in 2D Polar Coordinates:**\n$$E_r = -\\frac{\\partial \\varphi}{\\partial r} = \\frac{\\lambda l \\cos\\theta}{2\\pi\\varepsilon_0 r^2}$$\n$$E_\\theta = -\\frac{1}{r} \\frac{\\partial \\varphi}{\\partial \\theta} = \\frac{\\lambda l \\sin\\theta}{2\\pi\\varepsilon_0 r^2}$$\n$$E = \\sqrt{E_r^2 + E_\\theta^2} = \\frac{\\lambda l}{2\\pi\\varepsilon_0 r^2} \\sqrt{\\cos^2\\theta + \\sin^2\\theta} = \\frac{\\lambda l}{2\\pi\\varepsilon_0 r^2}$$",
        "tags": ["line dipole", "2D dipole", "parallel threads", "potential"]
    },
    {
        "id": "3.43",
        "title": "Field and Potential of Coaxial Opposite Rings",
        "difficulty": 2,
        "question": "Two coaxial rings, each of radius $R$, made of thin wire are separated by a small distance $l \\ll R$ and carry charges $+q$ and $-q$. Find the electric field potential and strength at the axis of the system as a function of the coordinate $x$. Investigate these functions at $|x| \\gg R$.",
        "hints": [
            "The potential is $\\varphi(x) = \\varphi_+(x - l/2) + \\varphi_-(x + l/2) \\approx -l \\frac{d\\varphi_{\\text{ring}}}{dx}$.",
            "Single ring potential: $\\varphi_{\\text{ring}}(x) = \\frac{q}{4\\pi\\varepsilon_0 \\sqrt{R^2 + x^2}}$.",
            "Differentiate: $\\varphi(x) = \\frac{q l x}{4\\pi\\varepsilon_0 (R^2 + x^2)^{3/2}}$, and $E_x = -\\frac{d\\varphi}{dx} = \\frac{q l (2x^2 - R^2)}{4\\pi\\varepsilon_0 (R^2 + x^2)^{5/2}}$."
        ],
        "answer": "$\\varphi(x) = \\frac{q l x}{4\\pi\\varepsilon_0 (R^2 + x^2)^{3/2}}, \\; E_x = \\frac{q l (2x^2 - R^2)}{4\\pi\\varepsilon_0 (R^2 + x^2)^{5/2}}$; for $|x| \\gg R$, $\\varphi \\approx \\frac{q l}{4\\pi\\varepsilon_0 x^2}, \\; E_x \\approx \\frac{2 q l}{4\\pi\\varepsilon_0 x^3}$",
        "solution": "**1. Potential Calculation:**\nSince $l \\ll R$, the potential is the spatial derivative of the single-ring potential:\n$$\\varphi(x) = -l \\frac{\\partial}{\\partial x} \\left[ \\frac{q}{4\\pi\\varepsilon_0 (R^2 + x^2)^{1/2}} \\right] = \\frac{q l x}{4\\pi\\varepsilon_0 (R^2 + x^2)^{3/2}}$$\n\n**2. Electric Field:**\n$$E_x = -\\frac{d\\varphi}{dx} = -\\frac{q l}{4\\pi\\varepsilon_0} \\frac{(R^2 + x^2)^{3/2} - x \\cdot \\frac{3}{2}(R^2 + x^2)^{1/2}(2x)}{(R^2 + x^2)^3} = \\frac{q l (2x^2 - R^2)}{4\\pi\\varepsilon_0 (R^2 + x^2)^{5/2}}$$\n\n**3. Asymptotic Form ($|x| \\gg R$):**\n$$\\varphi \\approx \\frac{q l}{4\\pi\\varepsilon_0 x^2} = \\frac{p}{4\\pi\\varepsilon_0 x^2}$$\n$$E_x \\approx \\frac{2 q l}{4\\pi\\varepsilon_0 x^3} = \\frac{2p}{4\\pi\\varepsilon_0 x^3}$$",
        "tags": ["coaxial rings", "dipole moment", "axial field", "Taylor expansion"]
    },
    {
        "id": "3.44",
        "title": "Field and Potential Along Axis of Opposite Planes with Circular Holes",
        "difficulty": 3,
        "question": "Two infinite planes separated by a distance $l$ carry uniform surface charges of densities $+\\sigma$ and $-\\sigma$. The planes have round coaxial holes of radius $R$, with $l \\ll R$. Taking the origin $O$ midway between the planes on the symmetry axis, find the potential and axial field strength $E_x$ as functions of $x$.",
        "hints": [
            "Use superposition: two solid planes with $\\pm\\sigma$ minus two round discs of radius $R$ with $\\pm\\sigma$.",
            "The two infinite planes produce uniform field $E_0 = \\frac{\\sigma}{\\varepsilon_0}$ between them and zero outside.",
            "The two circular discs of radius $R$ form a dipole sheet that subtracts from the solid plane field: $\\varphi(x) = \\frac{\\sigma l x}{2\\varepsilon_0 \\sqrt{x^2 + R^2}}$."
        ],
        "answer": "$\\varphi(x) = \\frac{\\sigma l x}{2\\varepsilon_0 \\sqrt{x^2 + R^2}}, \\quad E_x = -\\frac{\\sigma l R^2}{2\\varepsilon_0 (x^2 + R^2)^{3/2}}$",
        "solution": "**1. Superposition Model:**\nThe configuration of two perforated infinite planes equals:\n- Two complete infinite planes of charge densities $\\pm\\sigma$ separated by $l$.\n- Minus two round discs of radius $R$ of charge densities $\\pm\\sigma$ separated by $l$.\n\n**2. Potential along the Axis:**\nThe potential of a dipole layer of two circular discs with surface dipole density $\\tau = \\sigma l$ subtending solid angle $\\Omega(x)$ is:\n$$\\varphi(x) = \\frac{\\sigma l}{4\\pi\\varepsilon_0} \\Omega(x) = \\frac{\\sigma l}{2\\varepsilon_0} \\left( 1 - \\frac{x}{\\sqrt{x^2 + R^2}} \\right)$$\nSubtracting from the uniform potential of the complete capacitor plates yields:\n$$\\varphi(x) = \\frac{\\sigma l x}{2\\varepsilon_0 \\sqrt{x^2 + R^2}}$$\n\n**3. Electric Field:**\n$$E_x = -\\frac{d\\varphi}{dx} = -\\frac{\\sigma l}{2\\varepsilon_0} \\frac{\\sqrt{x^2 + R^2} - x \\cdot \\frac{x}{\\sqrt{x^2 + R^2}}}{x^2 + R^2} = -\\frac{\\sigma l R^2}{2\\varepsilon_0 (x^2 + R^2)^{3/2}}$$",
        "tags": ["perforated planes", "superposition", "circular aperture", "axial field"]
    },
    {
        "id": "3.45",
        "title": "Axial Field and Potential of a Circular Parallel-Plate Capacitor",
        "difficulty": 2,
        "question": "An electric capacitor consists of thin round parallel plates, each of radius $R$, separated by a distance $l \\ll R$ and uniformly charged with surface densities $+\\sigma$ and $-\\sigma$. Find the potential and field magnitude at the axis as functions of distance $x$ from the plates if $x \\gg l$.",
        "hints": [
            "The system is a circular disc dipole layer of radius $R$ and dipole moment per unit area $\\tau = \\sigma l$.",
            "The potential along the axis is $\\varphi(x) \\approx \\pm \\frac{\\sigma l}{2\\varepsilon_0} \\left(1 - \\frac{x}{\\sqrt{x^2 + R^2}}\\right)$.",
            "Differentiate to find $E(x) \\approx \\frac{\\sigma l R^2}{2\\varepsilon_0 (x^2 + R^2)^{3/2}}$."
        ],
        "answer": "$\\varphi(x) \\approx \\pm \\frac{\\sigma l}{2\\varepsilon_0} \\left( 1 - \\frac{x}{\\sqrt{x^2 + R^2}} \\right), \\quad E(x) \\approx \\frac{\\sigma l R^2}{2\\varepsilon_0 (x^2 + R^2)^{3/2}}$",
        "solution": "**1. Potential Formulation:**\nFor a circular disc of radius $R$ and charge density $\\sigma$, the axial potential is $\\varphi_+(x) = \\frac{\\sigma}{2\\varepsilon_0} (\\sqrt{x^2 + R^2} - x)$. For two plates separated by $l \\ll R$:\n$$\\varphi(x) \\approx -l \\frac{d\\varphi_+}{dx} = \\pm \\frac{\\sigma l}{2\\varepsilon_0} \\left( 1 - \\frac{x}{\\sqrt{x^2 + R^2}} \\right)$$\nwhere $+$ is outside the positive plate and $-$ outside the negative plate.\n\n**2. Electric Field:**\n$$E(x) = -\\frac{d\\varphi}{dx} = \\frac{\\sigma l R^2}{2\\varepsilon_0 (x^2 + R^2)^{3/2}}$$\nFor $x \\gg R$, $E \\approx \\frac{\\sigma l R^2}{2\\varepsilon_0 x^3} = \\frac{2p}{4\\pi\\varepsilon_0 x^3}$, where $p = \\pi R^2 \\sigma l$ is the total dipole moment.",
        "tags": ["circular capacitor", "dipole sheet", "axial potential", "field profile"]
    },
    {
        "id": "3.46",
        "title": "Force on a Dipole Near a Uniformly Charged Wire",
        "difficulty": 2,
        "question": "A dipole with electric moment $\\mathbf{p}$ is located at a distance $r$ from a long thread charged uniformly with a linear density $\\lambda$. Find the force $\\mathbf{F}$ acting on the dipole if the vector $\\mathbf{p}$ is oriented:\n(a) along the thread;\n(b) along the radius vector $\\mathbf{r}$;\n(c) at right angles to the thread and the radius vector $\\mathbf{r}$.",
        "hints": [
            "Force on a dipole in an inhomogeneous field: $\\mathbf{F} = (\\mathbf{p} \\cdot \\nabla) \\mathbf{E}$.",
            "Field of a long thread: $\\mathbf{E} = \\frac{\\lambda}{2\\pi\\varepsilon_0 r} \\hat{\\mathbf{r}}$.",
            "(a) Gradient along thread vanishes $\\implies F = 0$. (b) $F_r = p_r \\frac{dE_r}{dr} = -\\frac{p\\lambda}{2\\pi\\varepsilon_0 r^2}$. (c) In polar coordinates, $\\mathbf{F} = -\\frac{p\\lambda}{2\\pi\\varepsilon_0 r^2} \\hat{\\mathbf{r}}$."
        ],
        "answer": "(a) $F = 0$; (b) $\\mathbf{F} = -\\frac{p\\lambda}{2\\pi\\varepsilon_0 r^2} \\hat{\\mathbf{r}}$ (attraction); (c) $\\mathbf{F} = \\frac{p\\lambda}{2\\pi\\varepsilon_0 r^2} \\hat{\\mathbf{r}}$",
        "solution": "**1. General Force Formula:**\n$$\\mathbf{F} = (\\mathbf{p} \\cdot \\nabla)\\mathbf{E}$$\nThe electric field of the infinite thread is purely radial:\n$$\\mathbf{E}(r) = \\frac{\\lambda}{2\\pi\\varepsilon_0 r} \\hat{\\mathbf{r}}$$\n\n**2. Case (a): $\\mathbf{p} \\parallel$ thread ($z$-direction):**\n$$(\\mathbf{p} \\cdot \\nabla) = p_z \\frac{\\partial}{\\partial z}$$\nSince $\\mathbf{E}$ is independent of $z$, $\\mathbf{F} = 0$.\n\n**3. Case (b): $\\mathbf{p} \\parallel \\mathbf{r}$ (radial direction):**\n$$(\\mathbf{p} \\cdot \\nabla) = p_r \\frac{\\partial}{\\partial r}$$\n$$\\mathbf{F} = p \\frac{\\partial}{\\partial r} \\left( \\frac{\\lambda}{2\\pi\\varepsilon_0 r} \\hat{\\mathbf{r}} \\right) = -\\frac{p\\lambda}{2\\pi\\varepsilon_0 r^2} \\hat{\\mathbf{r}}$$\n(Attractive force towards the thread).\n\n**4. Case (c): $\\mathbf{p} \\perp$ thread and $\\mathbf{r}$ (azimuthal direction $\\hat{\\boldsymbol{\\varphi}}$):**\n$$(\\mathbf{p} \\cdot \\nabla) = \\frac{p_\\varphi}{r} \\frac{\\partial}{\\partial \\varphi}$$\nSince $\\frac{\\partial \\hat{\\mathbf{r}}}{\\partial \\varphi} = \\hat{\\boldsymbol{\\varphi}}$, the derivative of the unit vector yields a force:\n$$\\mathbf{F} = \\frac{p\\lambda}{2\\pi\\varepsilon_0 r^2} \\hat{\\mathbf{r}}$$",
        "tags": ["dipole force", "inhomogeneous field", "line charge", "gradient force"]
    },
    {
        "id": "3.47",
        "title": "Interaction Force Between Two Collinear Water Dipoles",
        "difficulty": 2,
        "question": "Find the interaction force between two water molecules separated by a distance $l = 10\\text{ nm}$ if their electric moments are oriented along the same straight line. The moment of each molecule equals $p = 0.62 \\times 10^{-29}\\text{ C}\\cdot\\text{m}$.",
        "hints": [
            "For two collinear dipoles aligned along the $z$-axis: $E_1(z) = \\frac{2p}{4\\pi\\varepsilon_0 z^3}$.",
            "The force on the second dipole is $F = p \\frac{dE_1}{dz} = p \\frac{d}{dz}\\left(\\frac{2p}{4\\pi\\varepsilon_0 z^3}\\right) = -\\frac{6p^2}{4\\pi\\varepsilon_0 l^4}$.",
            "Calculate magnitude $F = \\frac{6 p^2}{4\\pi\\varepsilon_0 l^4}$."
        ],
        "answer": "$F = \\frac{6 p^2}{4\\pi\\varepsilon_0 l^4} \\approx 2.1 \\times 10^{-16}\\text{ N}$",
        "solution": "**1. Collinear Dipole Interaction:**\nAlong the axis of dipole 1, the electric field is:\n$$E(z) = \\frac{2p}{4\\pi\\varepsilon_0 z^3}$$\nThe force experienced by dipole 2 (also oriented along the $z$-axis) is:\n$$F = p \\left| \\frac{dE}{dz} \\right| = p \\left( \\frac{6p}{4\\pi\\varepsilon_0 z^4} \\right) = \\frac{6 p^2}{4\\pi\\varepsilon_0 l^4}$$\n\n**2. Numerical Calculation:**\nWith $p = 0.62 \\times 10^{-29}\\text{ C}\\cdot\\text{m}$ and $l = 10 \\times 10^{-9}\\text{ m} = 1.0 \\times 10^{-8}\\text{ m}$:\n$$p^2 = (0.62 \\times 10^{-29})^2 = 3.844 \\times 10^{-59}\\text{ C}^2\\cdot\\text{m}^2$$\n$$l^4 = (1.0 \\times 10^{-8})^4 = 1.0 \\times 10^{-32}\\text{ m}^4$$\n$$F = 6 \\times (8.988 \\times 10^9) \\times \\frac{3.844 \\times 10^{-59}}{1.0 \\times 10^{-32}} = 53.93 \\times 3.844 \\times 10^{-18} \\approx 2.07 \\times 10^{-16}\\text{ N} \\approx 2.1 \\times 10^{-16}\\text{ N}$$",
        "tags": ["dipole-dipole interaction", "water molecules", "inverse-fourth power", "Coulomb force"]
    },
    {
        "id": "3.48",
        "title": "Electrostatic Potential from Field E = a(y i + x j)",
        "difficulty": 1,
        "question": "Find the potential $\\varphi(x, y)$ of an electrostatic field $\\mathbf{E} = a(y\\mathbf{i} + x\\mathbf{j})$, where $a$ is a constant.",
        "hints": [
            "Set $E_x = -\\frac{\\partial \\varphi}{\\partial x} = ay$ and $E_y = -\\frac{\\partial \\varphi}{\\partial y} = ax$.",
            "Integrate: $\\varphi(x, y) = -axy + C$."
        ],
        "answer": "$\\varphi(x, y) = -axy + \\text{const}$",
        "solution": "**1. Potential Formulation:**\nFrom $\\mathbf{E} = -\\nabla\\varphi$:\n$$-\\frac{\\partial\\varphi}{\\partial x} = ay \\implies \\varphi = -axy + f(y)$$\n$$-\\frac{\\partial\\varphi}{\\partial y} = ax - f'(y) = ax \\implies f'(y) = 0 \\implies f(y) = C$$\n$$\\varphi(x, y) = -axy + \\text{const}$$",
        "tags": ["potential", "electrostatic field", "line integral"]
    },
    {
        "id": "3.49",
        "title": "Potential of Non-Linear 2D Field",
        "difficulty": 2,
        "question": "Find the potential $\\varphi(x, y)$ of an electrostatic field $\\mathbf{E} = 2axy\\mathbf{i} + a(x^2 - y^2)\\mathbf{j}$, where $a$ is a constant.",
        "hints": [
            "Set $-\\frac{\\partial \\varphi}{\\partial x} = 2axy \\implies \\varphi(x, y) = -ax^2 y + f(y)$.",
            "Set $-\\frac{\\partial \\varphi}{\\partial y} = ax^2 - f'(y) = a(x^2 - y^2)$.",
            "Solve for $f'(y) = ay^2 \\implies f(y) = \\frac{a y^3}{3} + C$."
        ],
        "answer": "$\\varphi(x, y) = -ay \\left( x^2 - \\frac{y^2}{3} \\right) + \\text{const}$",
        "solution": "**1. Integration with Respect to $x$:**\n$$-\\frac{\\partial \\varphi}{\\partial x} = 2axy \\implies \\varphi(x, y) = -ax^2 y + f(y)$$\n\n**2. Differentiation with Respect to $y$:**\n$$-\\frac{\\partial \\varphi}{\\partial y} = ax^2 - f'(y)$$\nEquating to $E_y = a(x^2 - y^2)$:\n$$ax^2 - f'(y) = ax^2 - ay^2 \\implies f'(y) = ay^2 \\implies f(y) = \\frac{a y^3}{3} + C$$\n\n**3. Potential:**\n$$\\varphi(x, y) = -ax^2 y + \\frac{a y^3}{3} + C = -ay \\left( x^2 - \\frac{y^2}{3} \\right) + \\text{const}$$",
        "tags": ["electrostatic potential", "vector calculus", "exact differential"]
    },
    {
        "id": "3.50",
        "title": "Potential of a 3D Electrostatic Field",
        "difficulty": 2,
        "question": "Determine the potential $\\varphi(x, y, z)$ of an electrostatic field $\\mathbf{E} = ay\\mathbf{i} + (ax + bz)\\mathbf{j} + by\\mathbf{k}$, where $a$ and $b$ are constants.",
        "hints": [
            "Check that $\\nabla \\times \\mathbf{E} = 0$ (conservative field).",
            "Integrate $-\\frac{\\partial\\varphi}{\\partial x} = ay \\implies \\varphi = -axy + f(y, z)$.",
            "Match $\\frac{\\partial\\varphi}{\\partial y}$ and $\\frac{\\partial\\varphi}{\\partial z}$ to find $\\varphi = -y(ax + bz) + C$."
        ],
        "answer": "$\\varphi(x, y, z) = -y(ax + bz) + \\text{const}$",
        "solution": "**1. Conservative Check:**\n$$\\nabla \\times \\mathbf{E} = \\mathbf{i}\\left(\\frac{\\partial(by)}{\\partial y} - \\frac{\\partial(ax+bz)}{\\partial z}\\right) - \\mathbf{j}\\dots = \\mathbf{i}(b - b) - \\mathbf{j}(0 - 0) + \\mathbf{k}(a - a) = 0$$\n\n**2. Potential Integration:**\n$$d\\varphi = -\\mathbf{E} \\cdot d\\mathbf{r} = -(ay \\, dx + (ax + bz) \\, dy + by \\, dz)$$\nRecognizing the exact differential:\n$$d(axy) = ay \\, dx + ax \\, dy, \\quad d(byz) = bz \\, dy + by \\, dz$$\n$$d\\varphi = -d(axy + byz) = -d[y(ax + bz)]$$\n$$\\varphi(x, y, z) = -y(ax + bz) + \\text{const}$$",
        "tags": ["potential", "exact differential", "conservative field", "3D electrostatics"]
    },
    {
        "id": "3.51",
        "title": "Space Charge Distribution from Cubic Potential",
        "difficulty": 1,
        "question": "The field potential in a certain region of space depends only on the $x$ coordinate as $\\varphi(x) = -ax^3 + b$, where $a$ and $b$ are constants. Find the distribution of the space charge $\\rho(x)$.",
        "hints": [
            "Use Poisson's equation in 1D: $\\frac{d^2\\varphi}{dx^2} = -\\frac{\\rho(x)}{\\varepsilon_0}$.",
            "Compute $\\frac{d\\varphi}{dx} = -3ax^2$.",
            "Compute $\\frac{d^2\\varphi}{dx^2} = -6ax$, so $\\rho(x) = 6a\\varepsilon_0 x$."
        ],
        "answer": "$\\rho(x) = 6a\\varepsilon_0 x$",
        "solution": "**1. Poisson's Equation:**\nIn one dimension:\n$$\\frac{d^2\\varphi}{dx^2} = -\\frac{\\rho(x)}{\\varepsilon_0} \\implies \\rho(x) = -\\varepsilon_0 \\frac{d^2\\varphi}{dx^2}$$\n\n**2. Derivatives:**\n$$\\frac{d\\varphi}{dx} = \\frac{d}{dx}(-ax^3 + b) = -3ax^2$$\n$$\\frac{d^2\\varphi}{dx^2} = -6ax$$\n\n**3. Charge Distribution:**\n$$\\rho(x) = -\\varepsilon_0 (-6ax) = 6a\\varepsilon_0 x$$",
        "tags": ["Poisson equation", "space charge", "cubic potential"]
    },
    {
        "id": "3.52",
        "title": "Space Charge Between Parallel Plates for Zero Boundary Field",
        "difficulty": 2,
        "question": "A uniformly distributed space charge fills up the space between two large parallel plates separated by a distance $d$. The potential difference between the plates is equal to $\\Delta\\varphi$. At what value of charge density $\\rho$ is the field strength in the vicinity of one of the plates equal to zero? What will then be the field strength near the other plate?",
        "hints": [
            "Use 1D Poisson's equation: $\\frac{d^2\\varphi}{dx^2} = -\\frac{\\rho}{\\varepsilon_0}$.",
            "Integrate with $E(0) = -\\left.\\frac{d\\varphi}{dx}\\right|_{x=0} = 0$: $E(x) = \\frac{\\rho x}{\\varepsilon_0}$.",
            "Potential drop: $\\Delta\\varphi = \\int_0^d E(x) dx = \\frac{\\rho d^2}{2\\varepsilon_0}$, giving $\\rho = \\frac{2\\varepsilon_0 \\Delta\\varphi}{d^2}$ and $E(d) = \\frac{\\rho d}{\\varepsilon_0} = \\frac{2\\Delta\\varphi}{d}$."
        ],
        "answer": "$\\rho = \\frac{2\\varepsilon_0 \\Delta\\varphi}{d^2}; \\quad E = \\frac{\\rho d}{\\varepsilon_0} = \\frac{2\\Delta\\varphi}{d}$",
        "solution": "**1. Electric Field Profile:**\nFrom $\\frac{dE}{dx} = \\frac{\\rho}{\\varepsilon_0}$ with constant $\\rho$ and condition $E(0) = 0$ at the first plate ($x = 0$):\n$$E(x) = \\frac{\\rho}{\\varepsilon_0} x$$\n\n**2. Potential Difference:**\n$$\\Delta\\varphi = \\int_0^d E(x) dx = \\frac{\\rho}{\\varepsilon_0} \\int_0^d x \\, dx = \\frac{\\rho d^2}{2\\varepsilon_0}$$\nSolving for charge density:\n$$\\rho = \\frac{2\\varepsilon_0 \\Delta\\varphi}{d^2}$$\n\n**3. Field at the Other Plate ($x = d$):**\n$$E(d) = \\frac{\\rho d}{\\varepsilon_0} = \\frac{2\\Delta\\varphi}{d}$$",
        "tags": ["space charge", "parallel plates", "Poisson equation", "boundary field"]
    },
    {
        "id": "3.53",
        "title": "Space Charge Distribution for Quadratic Potential Inside a Ball",
        "difficulty": 2,
        "question": "The field potential inside a charged ball depends only on the distance from its centre as $\\varphi(r) = ar^2 + b$, where $a$ and $b$ are constants. Find the space charge distribution $\\rho(r)$ inside the ball.",
        "hints": [
            "Use Poisson's equation in spherical coordinates: $\\nabla^2\\varphi = \\frac{1}{r^2} \\frac{d}{dr}\\left(r^2 \\frac{d\\varphi}{dr}\\right) = -\\frac{\\rho(r)}{\\varepsilon_0}$.",
            "Compute $\\frac{d\\varphi}{dr} = 2ar$, so $r^2 \\frac{d\\varphi}{dr} = 2ar^3$.",
            "Differentiate: $\\frac{d}{dr}(2ar^3) = 6ar^2$, giving $\\nabla^2\\varphi = 6a$, hence $\\rho = -6a\\varepsilon_0$."
        ],
        "answer": "$\\rho = -6a\\varepsilon_0$ (uniform charge density)",
        "solution": "**1. Radial Laplacian in Spherical Coordinates:**\n$$\\nabla^2\\varphi = \\frac{1}{r^2} \\frac{d}{dr}\\left( r^2 \\frac{d\\varphi}{dr} \\right)$$\nGiven $\\varphi(r) = ar^2 + b$:\n$$\\frac{d\\varphi}{dr} = 2ar$$\n$$r^2 \\frac{d\\varphi}{dr} = 2ar^3$$\n$$\\frac{d}{dr}(2ar^3) = 6ar^2$$\n$$\\nabla^2\\varphi = \\frac{1}{r^2} (6ar^2) = 6a$$\n\n**2. Space Charge Density:**\nBy Poisson's equation $\\nabla^2\\varphi = -\\frac{\\rho}{\\varepsilon_0}$:\n$$\\rho = -\\varepsilon_0 \\nabla^2\\varphi = -6a\\varepsilon_0$$\nThe space charge is uniformly distributed throughout the interior of the ball.",
        "tags": ["Poisson equation", "spherical coordinates", "quadratic potential", "uniform space charge"]
    }
]
