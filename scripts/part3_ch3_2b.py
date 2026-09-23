"""
part3_ch3_2b.py
Curated problems 3.76 to 3.100 (25 problems) of Irodov Chapter 3.2:
Conductors and Dielectrics in an Electric Field (Part B).
"""

CH3_2B_CURATED = [
    {
        "id": "3.76",
        "title": "Bound Charges on Conductor in Dielectric",
        "difficulty": 2,
        "question": "A conductor of arbitrary shape, carrying a charge $q$, is surrounded by a uniform dielectric of permittivity $\\varepsilon$. Find the total bound charges at the inner and outer surfaces of the dielectric.",
        "hints": [
            "Use Gauss's law for the electric displacement vector: $\\oint \\mathbf{D} \\cdot d\\mathbf{S} = q_{\\text{ext}} = q$.",
            "Relate polarization to displacement in a linear dielectric: $\\mathbf{P} = \\frac{\\varepsilon - 1}{\\varepsilon} \\mathbf{D}$.",
            "The surface density of bound charge is $\\sigma' = \\mathbf{P} \\cdot \\mathbf{n}'$. On the inner surface the outward normal of the dielectric points toward the conductor, so $q'_{\\text{inn}} = -\\oint P_n dS$."
        ],
        "answer": "$q'_{\\text{inn}} = -q \\frac{\\varepsilon - 1}{\\varepsilon}$, $q'_{\\text{out}} = q \\frac{\\varepsilon - 1}{\\varepsilon}$",
        "solution": "**1. Displacement Vector in the Dielectric:**\nEnclosing the conductor with a Gaussian surface located inside the dielectric, Gauss's theorem for $\\mathbf{D}$ gives:\n$$\\oint \\mathbf{D} \\cdot d\\mathbf{S} = q_{\\text{ext}} = q$$\n\n**2. Relation between $\\mathbf{P}$ and $\\mathbf{D}$:**\nFor a linear isotropic dielectric:\n$$\\mathbf{D} = \\varepsilon\\varepsilon_0 \\mathbf{E}, \\quad \\mathbf{P} = (\\varepsilon - 1)\\varepsilon_0 \\mathbf{E} = \\frac{\\varepsilon - 1}{\\varepsilon} \\mathbf{D}$$\n\n**3. Bound Charge at the Inner Surface:**\nThe normal $\\mathbf{n}'$ pointing out of the dielectric at its inner boundary is opposite to the outward normal $\\mathbf{n}$ from the conductor ($\\mathbf{n}' = -\\mathbf{n}$):\n$$q'_{\\text{inn}} = \\oint \\mathbf{P} \\cdot d\\mathbf{S}' = -\\oint \\mathbf{P} \\cdot d\\mathbf{S} = -\\frac{\\varepsilon - 1}{\\varepsilon} \\oint \\mathbf{D} \\cdot d\\mathbf{S} = -q \\frac{\\varepsilon - 1}{\\varepsilon}$$\n\n**4. Bound Charge at the Outer Surface:**\nSince there are no extraneous charges within the volume of the homogeneous dielectric, $\\rho' = -\\nabla \\cdot \\mathbf{P} = 0$. By conservation of total bound charge ($q'_{\\text{total}} = 0$):\n$$q'_{\\text{out}} = -q'_{\\text{inn}} = q \\frac{\\varepsilon - 1}{\\varepsilon}$$",
        "tags": ["dielectrics", "bound charge", "polarization", "Gauss law for D"]
    },
    {
        "id": "3.77",
        "title": "Field and Potential of Spherical Dielectric Layer",
        "difficulty": 2,
        "question": "A uniform isotropic dielectric is shaped as a spherical layer with inner radius $a$ and outer radius $b$. Draw the approximate plots of the electric field strength $E$ and the potential $\\varphi$ vs the distance $r$ from the centre of the layer if the dielectric has a certain positive extraneous charge distributed uniformly:\n(a) over the internal surface of the layer;\n(b) over the volume of the layer.",
        "hints": [
            "Use spherical symmetry and Gauss's law for $\\mathbf{D}$: $\\oint \\mathbf{D} \\cdot d\\mathbf{S} = q_{\\text{ext}}(r)$.",
            "(a) For $r < a$, $q_{\\text{ext}} = 0 \\implies E = 0$. For $a < r < b$, $D = \\frac{q}{4\\pi r^2} \\implies E = \\frac{q}{4\\pi\\varepsilon_0\\varepsilon r^2}$. For $r > b$, $E = \\frac{q}{4\\pi\\varepsilon_0 r^2}$.",
            "(b) For $a < r < b$, $q_{\\text{ext}}(r) = q \\frac{r^3 - a^3}{b^3 - a^3}$, so $E(r) = \\frac{q(r^3 - a^3)}{4\\pi\\varepsilon_0\\varepsilon (b^3 - a^3) r^2}$."
        ],
        "answer": "(a) $E(r) = 0$ for $r < a$; $E(r) = \\frac{q}{4\\pi\\varepsilon_0\\varepsilon r^2}$ for $a < r < b$; $E(r) = \\frac{q}{4\\pi\\varepsilon_0 r^2}$ for $r > b$; (b) $E(r) = 0$ for $r < a$; $E(r) = \\frac{\\rho (r^3 - a^3)}{3\\varepsilon_0\\varepsilon r^2}$ for $a < r < b$; $E(r) = \\frac{q}{4\\pi\\varepsilon_0 r^2}$ for $r > b$",
        "solution": "**Case (a): Surface Charge $q$ at $r = a$:**\n1. For $r < a$:\n   $$q_{\\text{ext}} = 0 \\implies D = 0, \\quad E = 0, \\quad \\varphi = \\text{const}$$\n2. For $a < r < b$:\n   $$D = \\frac{q}{4\\pi r^2} \\implies E = \\frac{q}{4\\pi\\varepsilon_0\\varepsilon r^2}$$\n   $$\\varphi(r) = \\frac{q}{4\\pi\\varepsilon_0} \\left[ \\frac{1}{b} + \\frac{1}{\\varepsilon} \\left( \\frac{1}{r} - \\frac{1}{b} \\right) \\right]$$\n3. For $r > b$:\n   $$D = \\frac{q}{4\\pi r^2} \\implies E = \\frac{q}{4\\pi\\varepsilon_0 r^2}, \\quad \\varphi(r) = \\frac{q}{4\\pi\\varepsilon_0 r}$$\n   Note that $E(r)$ experiences a step increase by factor $\\varepsilon$ across the boundary $r = b$ from $E(b^-) = \\frac{q}{4\\pi\\varepsilon_0\\varepsilon b^2}$ to $E(b^+) = \\frac{q}{4\\pi\\varepsilon_0 b^2}$.\n\n**Case (b): Uniform Volume Charge Density $\\rho$ for $a < r < b$:**\n1. For $r < a$:\n   $$E = 0, \\quad \\varphi = \\text{const}$$\n2. For $a < r < b$:\n   $$D(r) = \\frac{\\rho(r^3 - a^3)}{3r^2} \\implies E(r) = \\frac{\\rho(r^3 - a^3)}{3\\varepsilon_0\\varepsilon r^2}$$\n3. For $r > b$:\n   $$E(r) = \\frac{q}{4\\pi\\varepsilon_0 r^2} = \\frac{\\rho(b^3 - a^3)}{3\\varepsilon_0 r^2}$$",
        "tags": ["spherical layer", "Gauss law for D", "electric field plot", "potential plot"]
    },
    {
        "id": "3.78",
        "title": "Refraction of Field Lines at Glass-Vacuum Boundary",
        "difficulty": 2,
        "question": "Near point $A$ lying on the boundary between glass and vacuum the electric field strength in vacuum is equal to $E_0 = 10.0\\text{ V/m}$, the angle between the vector $\\mathbf{E}_0$ and the normal $\\mathbf{n}$ to the boundary being $\\alpha_0 = 30^\\circ$. Find the field strength $E$ in glass near point $A$, the angle $\\alpha$ between $\\mathbf{E}$ and $\\mathbf{n}$, and the surface density of bound charges at point $A$ (glass permittivity $\\varepsilon = 6.0$).",
        "hints": [
            "Boundary conditions: the tangential component of electric field is continuous: $E_t = E_{0t} = E_0 \\sin\\alpha_0$.",
            "The normal component of displacement is continuous: $D_n = D_{0n} \\implies \\varepsilon\\varepsilon_0 E_n = \\varepsilon_0 E_{0n} \\implies E_n = \\frac{E_0 \\cos\\alpha_0}{\\varepsilon}$.",
            "Surface bound charge density: $\\sigma' = -P_n = -(\\varepsilon - 1)\\varepsilon_0 E_n = -\\varepsilon_0 \\frac{\\varepsilon - 1}{\\varepsilon} E_0 \\cos\\alpha_0$."
        ],
        "answer": "$E = E_0 \\sqrt{\\frac{\\cos^2\\alpha_0}{\\varepsilon^2} + \\sin^2\\alpha_0} = 5.2\\text{ V/m}$; $\\tan\\alpha = \\varepsilon\\tan\\alpha_0 \\implies \\alpha = 74^\\circ$; $\\sigma' = \\varepsilon_0 \\frac{\\varepsilon - 1}{\\varepsilon} E_0 \\cos\\alpha_0 = 64\\text{ pC/m}^2$",
        "solution": "**1. Boundary Conditions:**\nAt the interface between vacuum (permittivity $1$) and glass (permittivity $\\varepsilon$):\n- Tangential field continuity: $E_\\tau = E_{0\\tau} = E_0 \\sin\\alpha_0$\n- Normal displacement continuity: $D_n = D_{0n} \\implies \\varepsilon\\varepsilon_0 E_n = \\varepsilon_0 E_{0n} \\implies E_n = \\frac{E_0 \\cos\\alpha_0}{\\varepsilon}$\n\n**2. Resulting Field in Glass:**\n$$E = \\sqrt{E_n^2 + E_\\tau^2} = E_0 \\sqrt{\\frac{\\cos^2\\alpha_0}{\\varepsilon^2} + \\sin^2\\alpha_0}$$\nPlugging in $E_0 = 10.0\\text{ V/m}$, $\\alpha_0 = 30^\\circ$, and $\\varepsilon = 6.0$:\n$$E = 10.0 \\sqrt{\\frac{3/4}{36} + \\frac{1}{4}} = 10.0 \\sqrt{\\frac{1}{48} + \\frac{1}{4}} = 10.0 \\sqrt{0.2708} = 5.2\\text{ V/m}$$\n\n**3. Refraction Angle:**\n$$\\tan\\alpha = \\frac{E_\\tau}{E_n} = \\frac{E_0 \\sin\\alpha_0}{E_0 \\cos\\alpha_0 / \\varepsilon} = \\varepsilon \\tan\\alpha_0 = 6.0 \\tan 30^\\circ = 3.464 \\implies \\alpha = 74^\\circ$$\n\n**4. Bound Surface Charge Density:**\n$$\\sigma' = P_n = (\\varepsilon - 1)\\varepsilon_0 E_n = \\varepsilon_0 \\frac{\\varepsilon - 1}{\\varepsilon} E_0 \\cos\\alpha_0$$\n$$\\sigma' = 8.854 \\times 10^{-12} \\times \\frac{5}{6} \\times 10.0 \\times \\frac{\\sqrt{3}}{2} = 64\\text{ pC/m}^2$$",
        "tags": ["dielectric boundary conditions", "refraction of field lines", "bound surface charge"]
    },
    {
        "id": "3.79",
        "title": "Flux of E and Circulation of D at Dielectric Interface",
        "difficulty": 2,
        "question": "Near the plane surface of a uniform isotropic dielectric with permittivity $\\varepsilon$ the electric field strength in vacuum is equal to $E_0$, the vector $\\mathbf{E}_0$ forming an angle $\\theta$ with the normal to the dielectric's surface. Assuming the field to be uniform both inside and outside the dielectric, find:\n(a) the flux of the vector $\\mathbf{E}$ through a sphere of radius $R$ with centre located at the surface of the dielectric;\n(b) the circulation of the vector $\\mathbf{D}$ around a closed path $\\Gamma$ of length $l$ whose plane is perpendicular to the surface of the dielectric and parallel to $\\mathbf{E}_0$.",
        "hints": [
            "(a) By Gauss's theorem for $\\mathbf{E}$, $\\oint \\mathbf{E} \\cdot d\\mathbf{S} = \\frac{q_{\\text{total}}}{\\varepsilon_0} = \\frac{q'}{\\varepsilon_0}$. Bound surface charge enclosed is $\\sigma' \\pi R^2$.",
            "Surface bound charge density: $\\sigma' = -\\varepsilon_0 \\frac{\\varepsilon - 1}{\\varepsilon} E_0 \\cos\\theta$.",
            "(b) For circulation of $\\mathbf{D}$, $\\oint \\mathbf{D} \\cdot d\\mathbf{r} = \\oint (\\varepsilon_0\\mathbf{E} + \\mathbf{P}) \\cdot d\\mathbf{r} = \\oint \\mathbf{P} \\cdot d\\mathbf{r}$, since $\\oint \\mathbf{E} \\cdot d\\mathbf{r} = 0$."
        ],
        "answer": "(a) $\\Phi_E = -\\frac{\\varepsilon - 1}{\\varepsilon} \\pi R^2 E_0 \\cos\\theta$; (b) $\\oint \\mathbf{D} \\cdot d\\mathbf{r} = -\\varepsilon_0(\\varepsilon - 1) E_0 l \\sin\\theta$",
        "solution": "**(a) Flux of $\\mathbf{E}$ Through the Sphere:**\nInside the sphere there are no free charges, only the bound surface charges on the circular interface of area $S = \\pi R^2$.\nThe surface density of bound charge is:\n$$\\sigma' = -P_n = -(\\varepsilon - 1)\\varepsilon_0 E_n = -\\varepsilon_0 \\frac{\\varepsilon - 1}{\\varepsilon} E_0 \\cos\\theta$$\nThe total enclosed charge is $q_{\\text{encl}} = \\sigma' \\pi R^2$.\nBy Gauss's theorem for $\\mathbf{E}$:\n$$\\Phi_E = \\frac{q_{\\text{encl}}}{\\varepsilon_0} = -\\frac{\\varepsilon - 1}{\\varepsilon} \\pi R^2 E_0 \\cos\\theta$$\n\n**(b) Circulation of $\\mathbf{D}$ Around $\\Gamma$:**\n$$\\oint_\\Gamma \\mathbf{D} \\cdot d\\mathbf{r} = \\oint_\\Gamma (\\varepsilon_0 \\mathbf{E} + \\mathbf{P}) \\cdot d\\mathbf{r}$$\nSince the electrostatic field is conservative, $\\oint_\\Gamma \\mathbf{E} \\cdot d\\mathbf{r} = 0$.\nTherefore:\n$$\\oint_\\Gamma \\mathbf{D} \\cdot d\\mathbf{r} = \\oint_\\Gamma \\mathbf{P} \\cdot d\\mathbf{r}$$\nIn vacuum $\\mathbf{P} = 0$. In the dielectric, $\\mathbf{P}_\\tau = (\\varepsilon - 1)\\varepsilon_0 E_\\tau = (\\varepsilon - 1)\\varepsilon_0 E_0 \\sin\\theta$.\nTaking the closed rectangular loop of length along the boundary $l/2$ (or length segment $l$ traversed):\n$$\\oint \\mathbf{D} \\cdot d\\mathbf{r} = -\\varepsilon_0(\\varepsilon - 1) E_0 l \\sin\\theta$$",
        "tags": ["flux of E", "circulation of D", "dielectric boundary", "polarization"]
    },
    {
        "id": "3.80",
        "title": "Field and Bound Charges in Uniformly Charged Dielectric Plate",
        "difficulty": 2,
        "question": "An infinite plate of uniform dielectric with permittivity $\\varepsilon$ is uniformly charged with extraneous charge of space density $\\rho$. The thickness of the plate is $2d$. Find:\n(a) the magnitude of the electric field strength and the potential as functions of distance $x$ from the middle plane (where the potential is assumed zero);\n(b) the surface and space densities of the bound charge.",
        "hints": [
            "Use Gauss's law for $\\mathbf{D}$ with a cylindrical box of cross-section $S$ extending from $-x$ to $+x$: $2 D(x) S = \\rho (2x) S$ for $x \\le d$.",
            "Inside the plate ($|x| \\le d$): $D(x) = \\rho x \\implies E(x) = \\frac{\\rho x}{\\varepsilon\\varepsilon_0}$. Outside ($|x| > d$): $D(x) = \\rho d \\implies E(x) = \\frac{\\rho d}{\\varepsilon_0}$.",
            "Bound charges: space density $\\rho' = -\\nabla \\cdot \\mathbf{P} = -\\frac{\\varepsilon - 1}{\\varepsilon}\\rho$; surface density at $x = d$: $\\sigma' = P_n = \\frac{\\varepsilon - 1}{\\varepsilon}\\rho d$."
        ],
        "answer": "(a) For $|x| < d$: $E(x) = \\frac{\\rho x}{\\varepsilon\\varepsilon_0}$, $\\varphi(x) = -\\frac{\\rho x^2}{2\\varepsilon_0\\varepsilon}$; for $|x| > d$: $E(x) = \\frac{\\rho d}{\\varepsilon_0}$, $\\varphi(x) = -\\frac{\\rho d}{\\varepsilon_0} \\left( |x| - d + \\frac{d}{2\\varepsilon} \\right)$; (b) $\\sigma' = \\frac{\\varepsilon - 1}{\\varepsilon}\\rho d$, $\\rho' = -\\frac{\\varepsilon - 1}{\\varepsilon}\\rho$",
        "solution": "**(a) Field Strength and Potential:**\nBy symmetry, $\\mathbf{D}$ is directed along the $x$-axis perpendicular to the plate, with $D(0) = 0$.\n1. **Inside the plate ($|x| \\le d$):**\n   $$D(x) = \\rho x \\implies E(x) = \\frac{\\rho x}{\\varepsilon\\varepsilon_0}$$\n   $$\\varphi(x) = -\\int_0^x E(x') dx' = -\\frac{\\rho x^2}{2\\varepsilon_0\\varepsilon}$$\n2. **Outside the plate ($|x| \\ge d$):**\n   $$D(x) = \\rho d \\implies E(x) = \\frac{\\rho d}{\\varepsilon_0}$$\n   $$\\varphi(x) = \\varphi(d) - \\int_d^x E(x') dx' = -\\frac{\\rho d^2}{2\\varepsilon_0\\varepsilon} - \\frac{\\rho d}{\\varepsilon_0}(|x| - d)$$\n\n**(b) Bound Charge Densities:**\nInside the dielectric:\n$$\\mathbf{P} = \\frac{\\varepsilon - 1}{\\varepsilon} \\mathbf{D} = \\frac{\\varepsilon - 1}{\\varepsilon} \\rho x \\hat{\\mathbf{i}}$$\n$$\\rho' = -\\nabla \\cdot \\mathbf{P} = -\\frac{d P_x}{dx} = -\\frac{\\varepsilon - 1}{\\varepsilon} \\rho$$\nAt the surface $x = d$, the outward normal is $\\hat{\\mathbf{i}}$, so:\n$$\\sigma' = P_x(d) = \\frac{\\varepsilon - 1}{\\varepsilon} \\rho d$$",
        "tags": ["charged dielectric plate", "Gauss law for D", "electric potential", "bound charge densities"]
    },
    {
        "id": "3.81",
        "title": "Field and Bound Charges of Uniformly Charged Dielectric Ball",
        "difficulty": 2,
        "question": "Extraneous charges are uniformly distributed with space density $\\rho > 0$ over a ball of radius $R$ made of uniform isotropic dielectric with permittivity $\\varepsilon$. Find:\n(a) the magnitude of the electric field strength as a function of distance $r$ from the centre of the ball;\n(b) the space and surface densities of the bound charges.",
        "hints": [
            "Use spherical Gauss's law for $\\mathbf{D}$: $\\oint \\mathbf{D} \\cdot d\\mathbf{S} = q_{\\text{ext}}(r)$.",
            "Inside the ball ($r < R$): $D(r) = \\frac{1}{3}\\rho r \\implies E(r) = \\frac{\\rho r}{3\\varepsilon_0\\varepsilon}$. Outside ($r > R$): $D(r) = \\frac{\\rho R^3}{3r^2} \\implies E(r) = \\frac{\\rho R^3}{3\\varepsilon_0 r^2}$.",
            "Bound space density: $\\rho' = -\\nabla \\cdot \\mathbf{P} = -\\frac{\\varepsilon - 1}{\\varepsilon} \\rho$. Bound surface density at $r = R$: $\\sigma' = P_r(R) = \\frac{\\varepsilon - 1}{3\\varepsilon} \\rho R$."
        ],
        "answer": "(a) $E(r) = \\frac{\\rho r}{3\\varepsilon_0\\varepsilon}$ for $r < R$; $E(r) = \\frac{\\rho R^3}{3\\varepsilon_0 r^2}$ for $r > R$; (b) $\\rho' = -\\frac{\\varepsilon - 1}{\\varepsilon}\\rho$, $\\sigma' = \\frac{\\varepsilon - 1}{3\\varepsilon}\\rho R$",
        "solution": "**(a) Field Strength:**\nUsing Gauss's law for displacement vector $\\mathbf{D}$:\n- **Inside ($r < R$):**\n  $$4\\pi r^2 D(r) = \\frac{4}{3}\\pi r^3 \\rho \\implies D(r) = \\frac{1}{3}\\rho r$$\n  $$E(r) = \\frac{D(r)}{\\varepsilon_0\\varepsilon} = \\frac{\\rho r}{3\\varepsilon_0\\varepsilon}$$\n- **Outside ($r > R$):**\n  $$4\\pi r^2 D(r) = \\frac{4}{3}\\pi R^3 \\rho \\implies D(r) = \\frac{\\rho R^3}{3r^2}$$\n  $$E(r) = \\frac{D(r)}{\\varepsilon_0} = \\frac{\\rho R^3}{3\\varepsilon_0 r^2}$$\n\n**(b) Bound Charges:**\nThe polarization inside the ball is:\n$$\\mathbf{P}(r) = \\frac{\\varepsilon - 1}{\\varepsilon} \\mathbf{D}(r) = \\frac{\\varepsilon - 1}{3\\varepsilon} \\rho \\mathbf{r}$$\nVolume density of bound charge:\n$$\\rho' = -\\nabla \\cdot \\mathbf{P} = -\\frac{1}{r^2} \\frac{d}{dr}\\left( r^2 P_r \\right) = -\\frac{\\varepsilon - 1}{\\varepsilon} \\rho$$\nSurface density of bound charge at $r = R$:\n$$\\sigma' = P_r(R) = \\frac{\\varepsilon - 1}{3\\varepsilon} \\rho R$$\nNotice that total bound charge vanishes:\n$$q'_{\\text{vol}} + q'_{\\text{surf}} = \\rho' \\cdot \\frac{4}{3}\\pi R^3 + \\sigma' \\cdot 4\\pi R^2 = -\\frac{\\varepsilon - 1}{\\varepsilon}\\rho \\frac{4}{3}\\pi R^3 + \\frac{\\varepsilon - 1}{3\\varepsilon}\\rho R \\cdot 4\\pi R^2 = 0$$",
        "tags": ["dielectric ball", "Gauss law for D", "bound charge densities", "electric field"]
    },
    {
        "id": "3.82",
        "title": "Field at Centre of Thin Polarized Disc",
        "difficulty": 2,
        "question": "A round dielectric disc of radius $R$ and thickness $d$ is statically polarized so that it gains uniform polarization $\\mathbf{P}$, with the vector $\\mathbf{P}$ lying in the plane of the disc. Find the electric field strength $E$ at the centre of the disc if $d \\ll R$.",
        "hints": [
            "Since $\\mathbf{P} = \\text{const}$, the bulk bound charge is zero: $\\rho' = -\\nabla \\cdot \\mathbf{P} = 0$.",
            "Bound charges appear only on the cylindrical rim of the disc: $\\sigma' = \\mathbf{P} \\cdot \\mathbf{n} = P \\cos\\varphi$.",
            "Integrate the field produced at the centre by elements of the charged rim of height $d$ and radius $R$."
        ],
        "answer": "$E = -\\frac{P d}{4\\varepsilon_0 R}$",
        "solution": "**1. Bound Charges:**\nSince polarization $\\mathbf{P}$ is uniform in the plane of the disc, $\\rho' = -\\nabla \\cdot \\mathbf{P} = 0$.\nOn the top and bottom flat surfaces of the disc, the normal is perpendicular to $\\mathbf{P}$, so $\\sigma' = 0$.\nOn the cylindrical lateral surface of radius $R$ and thickness $d$, the outward normal makes angle $\\varphi$ with $\\mathbf{P}$:\n$$\\sigma'(\\varphi) = P \\cos\\varphi$$\n\n**2. Field at the Centre:**\nAn element of the rim of angular width $d\\varphi$ has area $dA = R d\\varphi \\cdot d$ and carries bound charge:\n$$dq' = \\sigma' dA = P \\cos\\varphi \\cdot R d\\varphi \\cdot d$$\nAt the centre, this element creates electric field:\n$$d\\mathbf{E} = -\\frac{dq'}{4\\pi\\varepsilon_0 R^2} \\hat{\\mathbf{r}}(\\varphi)$$\nBy symmetry, the resultant field is directed opposite to $\\mathbf{P}$ (along the $\\varphi = 0$ axis):\n$$E = -\\int_0^{2\\pi} \\frac{P \\cos\\varphi \\cdot R d \\cdot d\\varphi}{4\\pi\\varepsilon_0 R^2} \\cos\\varphi = -\\frac{P d}{4\\pi\\varepsilon_0 R} \\int_0^{2\\pi} \\cos^2\\varphi \\, d\\varphi$$\nSince $\\int_0^{2\\pi} \\cos^2\\varphi \\, d\\varphi = \\pi$:\n$$E = -\\frac{P d}{4\\varepsilon_0 R}$$",
        "tags": ["polarized disc", "bound surface charge", "depolarization field", "integration"]
    },
    {
        "id": "3.83",
        "title": "Field in Plate with Quadratic Polarization Profile",
        "difficulty": 2,
        "question": "Under certain conditions the polarization of an infinite uncharged dielectric plate takes the form $\\mathbf{P} = P_0 (1 - x^2/d^2) \\hat{\\mathbf{i}}$, where $P_0$ is a vector perpendicular to the plate, $x$ is the distance from the middle plane of the plate, and $d$ is its half-thickness. Find the electric field strength $E$ inside the plate and the potential difference between its surfaces.",
        "hints": [
            "There are no extraneous charges on or inside the plate, so displacement $D = 0$ everywhere.",
            "From $\\mathbf{D} = \\varepsilon_0 \\mathbf{E} + \\mathbf{P} = 0$, the electric field is $\\mathbf{E} = -\\frac{\\mathbf{P}}{\\varepsilon_0}$.",
            "The potential difference between the surfaces $x = -d$ and $x = +d$ is $V = \\int_{-d}^d E(x) \\, dx$."
        ],
        "answer": "$E(x) = -\\frac{P_0}{\\varepsilon_0}\\left(1 - \\frac{x^2}{d^2}\\right)$; $U = \\frac{4 P_0 d}{3\\varepsilon_0}$",
        "solution": "**1. Electric Field Inside the Plate:**\nSince there are no free (extraneous) charges anywhere in the system, by planar symmetry:\n$$\\mathbf{D} = 0$$\nTherefore, from $\\mathbf{D} = \\varepsilon_0 \\mathbf{E} + \\mathbf{P} = 0$:\n$$\\mathbf{E}(x) = -\\frac{\\mathbf{P}(x)}{\\varepsilon_0} = -\\frac{P_0}{\\varepsilon_0}\\left(1 - \\frac{x^2}{d^2}\\right) \\hat{\\mathbf{i}}$$\n\n**2. Potential Difference Between Surfaces:**\nThe potential difference between the two surfaces $x = -d$ and $x = +d$ is:\n$$U = \\left| \\int_{-d}^d E_x(x) \\, dx \\right| = \\frac{P_0}{\\varepsilon_0} \\int_{-d}^d \\left(1 - \\frac{x^2}{d^2}\\right) dx$$\nEvaluating the integral:\n$$\\int_{-d}^d \\left(1 - \\frac{x^2}{d^2}\\right) dx = 2 \\left[ x - \\frac{x^3}{3d^2} \\right]_0^d = 2\\left( d - \\frac{d}{3} \\right) = \\frac{4}{3}d$$\n$$U = \\frac{4 P_0 d}{3\\varepsilon_0}$$",
        "tags": ["nonuniform polarization", "potential difference", "displacement vector", "dielectric plate"]
    },
    {
        "id": "3.84",
        "title": "Capacitor with Half Gap Filled in Series",
        "difficulty": 2,
        "question": "Initially the space between the plates of a capacitor is filled with air, and the field strength in the gap is $E_0$. Then half the gap (layer of thickness $d/2$) is filled with uniform isotropic dielectric of permittivity $\\varepsilon$. Find the moduli of $\\mathbf{E}$ and $\\mathbf{D}$ in both parts of the gap (1 in air, 2 in dielectric) if the introduction of the dielectric:\n(a) does not change the voltage across the plates;\n(b) leaves the charges on the plates constant.",
        "hints": [
            "(a) Constant voltage $V = E_0 d$. With two layers in series: $V = E_1 \\frac{d}{2} + E_2 \\frac{d}{2}$. Continuity of displacement requires $D_1 = D_2 \\implies \\varepsilon_0 E_1 = \\varepsilon\\varepsilon_0 E_2$.",
            "(b) Constant charge means constant displacement $D_1 = D_2 = D_0 = \\varepsilon_0 E_0$.",
            "In each case solve for $E_1, E_2$ and $D_1, D_2$."
        ],
        "answer": "(a) $E_1 = \\frac{2\\varepsilon}{\\varepsilon + 1}E_0$, $E_2 = \\frac{2}{\\varepsilon + 1}E_0$, $D_1 = D_2 = \\frac{2\\varepsilon}{\\varepsilon + 1}\\varepsilon_0 E_0$; (b) $E_1 = E_0$, $E_2 = \\frac{E_0}{\\varepsilon}$, $D_1 = D_2 = \\varepsilon_0 E_0$",
        "solution": "**Case (a): Constant Voltage $V = E_0 d$:**\nBoundary condition across the parallel interface: $D_1 = D_2$.\n$$\\varepsilon_0 E_1 = \\varepsilon\\varepsilon_0 E_2 \\implies E_1 = \\varepsilon E_2$$\nThe voltage is the sum of potentials across both halves of thickness $d/2$:\n$$V = E_1 \\frac{d}{2} + E_2 \\frac{d}{2} = E_0 d \\implies E_1 + E_2 = 2E_0$$\nSubstituting $E_1 = \\varepsilon E_2$:\n$$(\\varepsilon + 1) E_2 = 2E_0 \\implies E_2 = \\frac{2}{\\varepsilon + 1} E_0$$\n$$E_1 = \\frac{2\\varepsilon}{\\varepsilon + 1} E_0$$\n$$D_1 = D_2 = \\varepsilon_0 E_1 = \\frac{2\\varepsilon}{\\varepsilon + 1}\\varepsilon_0 E_0$$\n\n**Case (b): Constant Charges on the Plates:**\nConstant charge density $\\sigma = \\varepsilon_0 E_0$ implies:\n$$D_1 = D_2 = \\sigma = \\varepsilon_0 E_0$$\nTherefore:\n$$E_1 = \\frac{D_1}{\\varepsilon_0} = E_0$$\n$$E_2 = \\frac{D_2}{\\varepsilon\\varepsilon_0} = \\frac{E_0}{\\varepsilon}$$",
        "tags": ["capacitor with dielectric", "boundary conditions", "displacement vector", "series dielectric"]
    },
    {
        "id": "3.85",
        "title": "Capacitor with Half Gap Filled in Parallel",
        "difficulty": 2,
        "question": "Solve the foregoing problem for the case when half the gap is filled with dielectric in parallel (i.e. splitting the area $S$ into two halves of area $S/2$, each spanning the full separation $d$):\n(a) the voltage across the plates remains constant;\n(b) the charges on the plates remain constant.",
        "hints": [
            "(a) Since plates are equipotentials spanning distance $d$, $E_1 = E_2 = V/d = E_0$. Displacement is $D_1 = \\varepsilon_0 E_0$ and $D_2 = \\varepsilon\\varepsilon_0 E_0$.",
            "(b) Total charge is conserved: $q = \\frac{S}{2} D_1 + \\frac{S}{2} D_2 = S D_0 = S \\varepsilon_0 E_0$.",
            "Since the electric field is uniform along $d$, $E_1 = E_2 = E$, so $D_1 + D_2 = 2\\varepsilon_0 E_0$."
        ],
        "answer": "(a) $E_1 = E_2 = E_0$, $D_1 = \\varepsilon_0 E_0$, $D_2 = \\varepsilon\\varepsilon_0 E_0$; (b) $E_1 = E_2 = \\frac{2}{\\varepsilon + 1}E_0$, $D_1 = \\frac{2}{\\varepsilon + 1}\\varepsilon_0 E_0$, $D_2 = \\frac{2\\varepsilon}{\\varepsilon + 1}\\varepsilon_0 E_0$",
        "solution": "**Case (a): Constant Voltage:**\nBoth halves connect the same two conducting plates separated by distance $d$. Therefore the electric field is uniform throughout:\n$$E_1 = E_2 = \\frac{V}{d} = E_0$$\nThe displacement vectors are:\n$$D_1 = \\varepsilon_0 E_1 = \\varepsilon_0 E_0$$\n$$D_2 = \\varepsilon\\varepsilon_0 E_2 = \\varepsilon\\varepsilon_0 E_0$$\n\n**Case (b): Constant Total Charge:**\nThe initial charge on each plate was $q = \\varepsilon_0 E_0 S$.\nBecause each section has area $S/2$ and thickness $d$, the potential difference is identical across both halves, so $E_1 = E_2 = E$.\nTotal charge conservation:\n$$q = \\frac{S}{2} D_1 + \\frac{S}{2} D_2 = \\frac{S}{2} (\\varepsilon_0 E + \\varepsilon\\varepsilon_0 E) = \\varepsilon_0 E_0 S$$\n$$\\frac{\\varepsilon + 1}{2} E = E_0 \\implies E = \\frac{2}{\\varepsilon + 1} E_0$$\nThus:\n$$E_1 = E_2 = \\frac{2}{\\varepsilon + 1} E_0$$\n$$D_1 = \\varepsilon_0 E = \\frac{2}{\\varepsilon + 1} \\varepsilon_0 E_0$$\n$$D_2 = \\varepsilon\\varepsilon_0 E = \\frac{2\\varepsilon}{\\varepsilon + 1} \\varepsilon_0 E_0$$",
        "tags": ["capacitor with dielectric", "parallel dielectric", "boundary conditions", "charge conservation"]
    },
    {
        "id": "3.86",
        "title": "Field in Hemispherically Filled Spherical Capacitor",
        "difficulty": 2,
        "question": "Half the space between two concentric spherical electrodes of a capacitor is filled (split by a diametral plane) with uniform isotropic dielectric of permittivity $\\varepsilon$. The total charge of the capacitor is $q$. Find the magnitude of the electric field strength between the electrodes as a function of distance $r$ from the centre.",
        "hints": [
            "Due to symmetry, the spherical electrodes are equipotential surfaces, so the electric field $\\mathbf{E}$ is radial and has the same magnitude $E(r)$ in both the air and dielectric hemispheres.",
            "Write the displacements: $D_1(r) = \\varepsilon_0 E(r)$ in air, and $D_2(r) = \\varepsilon\\varepsilon_0 E(r)$ in dielectric.",
            "Apply Gauss's law for $\\mathbf{D}$ over a sphere of radius $r$: $\\oint \\mathbf{D} \\cdot d\\mathbf{S} = 2\\pi r^2 D_1 + 2\\pi r^2 D_2 = q$."
        ],
        "answer": "$E(r) = \\frac{q}{2\\pi \\varepsilon_0 (\\varepsilon + 1) r^2}$",
        "solution": "**1. Symmetry and Equipotentials:**\nThe spherical electrodes are conductors, so each is an equipotential surface. Therefore the potential $\\varphi(r)$ and radial field $E(r) = -d\\varphi/dr$ must depend only on $r$ and must be identical at the same radius in both the air-filled and dielectric-filled hemispheres:\n$$E_1(r) = E_2(r) = E(r)$$\n\n**2. Displacements in the Two Hemispheres:**\n$$D_1(r) = \\varepsilon_0 E(r) \\quad (\\text{vacuum})$$\n$$D_2(r) = \\varepsilon\\varepsilon_0 E(r) \\quad (\\text{dielectric})$$\n\n**3. Gauss's Law for $\\mathbf{D}$:**\nConstruct a spherical Gaussian surface of radius $r$ between the electrodes:\n$$\\oint \\mathbf{D} \\cdot d\\mathbf{S} = D_1(r) \\cdot 2\\pi r^2 + D_2(r) \\cdot 2\\pi r^2 = 2\\pi r^2 \\varepsilon_0 (1 + \\varepsilon) E(r) = q$$\nSolving for $E(r)$:\n$$E(r) = \\frac{q}{2\\pi\\varepsilon_0(\\varepsilon + 1)r^2}$$",
        "tags": ["spherical capacitor", "dielectric boundary", "Gauss law for D", "electric field"]
    },
    {
        "id": "3.87",
        "title": "Equilibrium of Suspended Charged Balls in Kerosene",
        "difficulty": 2,
        "question": "Two small identical balls carrying charges of the same sign are suspended from the same point by insulating threads of equal length. When the surrounding space was filled with kerosene, the divergence angle between the threads remained constant. What is the density of the material of which the balls are made? (Kerosene permittivity $\\varepsilon = 2.0$, density $\\rho_0 = 0.8\\text{ g/cm}^3$)",
        "hints": [
            "In vacuum, equilibrium condition for small angle $\\theta$ is $\\tan\\theta = \\frac{F_e}{m g}$, where $F_e = \\frac{q^2}{4\\pi\\varepsilon_0 r^2}$.",
            "In kerosene, the electrostatic force decreases by factor $\\varepsilon$: $F'_e = F_e / \\varepsilon$.",
            "The effective weight in kerosene is reduced by Archimedes' buoyant force: $P' = m g (1 - \\rho_0/\\rho)$, where $\\rho$ is ball density.",
            "Equating $\\tan\\theta$ in both media: $\\frac{F_e}{m g} = \\frac{F_e / \\varepsilon}{m g (1 - \\rho_0/\\rho)}$."
        ],
        "answer": "$\\rho = \\rho_0 \\frac{\\varepsilon}{\\varepsilon - 1} = 1.6\\text{ g/cm}^3$",
        "solution": "**1. Equilibrium in Vacuum:**\nThe equilibrium condition is:\n$$\\tan\\theta = \\frac{F_e}{m g}$$\nwhere $m = \\rho V$ is the mass of each ball.\n\n**2. Equilibrium in Kerosene:**\nIn kerosene, the dielectric weakens the electrostatic interaction by factor $\\varepsilon$:\n$$F'_e = \\frac{F_e}{\\varepsilon}$$\nBuoyancy reduces the apparent weight:\n$$P' = m g - \\rho_0 V g = m g \\left(1 - \\frac{\\rho_0}{\\rho}\\right)$$\nFor the deflection angle to remain identical:\n$$\\tan\\theta = \\frac{F'_e}{P'} = \\frac{F_e / \\varepsilon}{m g (1 - \\rho_0/\\rho)}$$\n\n**3. Equating Expressions:**\n$$\\frac{F_e}{m g} = \\frac{F_e}{\\varepsilon m g (1 - \\rho_0/\\rho)} \\implies \\varepsilon \\left(1 - \\frac{\\rho_0}{\\rho}\\right) = 1$$\n$$1 - \\frac{\\rho_0}{\\rho} = \\frac{1}{\\varepsilon} \\implies \\frac{\\rho_0}{\\rho} = \\frac{\\varepsilon - 1}{\\varepsilon}$$\n$$\\rho = \\rho_0 \\frac{\\varepsilon}{\\varepsilon - 1}$$\nPlugging in $\\varepsilon = 2.0$ and $\\rho_0 = 0.8\\text{ g/cm}^3$:\n$$\\rho = 0.8 \\times \\frac{2.0}{2.0 - 1} = 1.6\\text{ g/cm}^3$$",
        "tags": ["dielectrics", "Archimedes force", "charged balls", "pendulum equilibrium"]
    },
    {
        "id": "3.88",
        "title": "Bound Charges of Uniformly Polarized Dielectric Ball",
        "difficulty": 2,
        "question": "A uniform electric field of strength $E = 100\\text{ V/m}$ is generated inside a ball made of uniform isotropic dielectric with permittivity $\\varepsilon = 5.00$. The radius of the ball is $R = 3.0\\text{ cm}$. Find the maximum surface density of bound charges and the total bound charge of one sign.",
        "hints": [
            "Uniform polarization inside the ball: $P = (\\varepsilon - 1)\\varepsilon_0 E$.",
            "The surface density of bound charge is $\\sigma'(\\theta) = P \\cos\\theta$, so $\\sigma'_{\\max} = P$.",
            "The total bound charge of one sign is obtained by integrating over a hemisphere: $q' = \\int_0^{\\pi/2} \\sigma'(\\theta) 2\\pi R^2 \\sin\\theta \\, d\\theta = \\pi R^2 P$."
        ],
        "answer": "$\\sigma'_{\\max} = (\\varepsilon - 1)\\varepsilon_0 E = 3.5\\text{ nC/m}^2$; $q' = \\pi R^2 (\\varepsilon - 1)\\varepsilon_0 E = 10\\text{ pC}$",
        "solution": "**1. Polarization Inside the Ball:**\nGiven that the electric field inside the ball is uniform with magnitude $E$:\n$$P = (\\varepsilon - 1)\\varepsilon_0 E$$\n\n**2. Maximum Surface Density:**\nThe surface density of bound charges is:\n$$\\sigma'(\\theta) = \\mathbf{P} \\cdot \\mathbf{n} = P \\cos\\theta$$\nwhere $\\theta$ is the angle with the field vector. Its maximum value occurs at $\\theta = 0$:\n$$\\sigma'_{\\max} = P = (\\varepsilon - 1)\\varepsilon_0 E$$\nNumerically:\n$$\\sigma'_{\\max} = (5.00 - 1) \\times 8.854 \\times 10^{-12} \\times 100 = 3.54 \\times 10^{-9}\\text{ C/m}^2 = 3.5\\text{ nC/m}^2$$\n\n**3. Total Bound Charge of One Sign:**\nIntegrating over the hemisphere where $\\cos\\theta > 0$:\n$$q' = \\int_0^{\\pi/2} (P \\cos\\theta) \\cdot (2\\pi R^2 \\sin\\theta \\, d\\theta) = 2\\pi R^2 P \\int_0^{\\pi/2} \\sin\\theta \\cos\\theta \\, d\\theta = \\pi R^2 P$$\n$$q' = \\pi R^2 (\\varepsilon - 1)\\varepsilon_0 E$$\nNumerically, with $R = 0.030\\text{ m}$:\n$$q' = \\pi \\times (0.030)^2 \\times 3.54 \\times 10^{-9} = 1.00 \\times 10^{-11}\\text{ C} = 10\\text{ pC}$$",
        "tags": ["dielectric ball", "polarization", "bound surface charge", "hemisphere integration"]
    },
    {
        "id": "3.89",
        "title": "Bound Charges on Dielectric Boundary Induced by Point Charge",
        "difficulty": 3,
        "question": "A point charge $q$ is located in vacuum at a distance $l$ from the plane surface of a uniform isotropic dielectric filling a half-space. The permittivity of the dielectric is $\\varepsilon$. Find:\n(a) the surface density of bound charges as a function of distance $r$ from the point charge $q$, and analyse the result for $l \\to 0$;\n(b) the total bound charge on the surface of the dielectric.",
        "hints": [
            "Use the method of images for dielectrics: the field in vacuum is due to $q$ and an image charge $q' = -\\frac{\\varepsilon - 1}{\\varepsilon + 1}q$ located symmetrically at distance $l$ inside the dielectric.",
            "The field in the dielectric is due to a charge $q'' = \\frac{2}{\\varepsilon + 1}q$ at the position of $q$.",
            "(a) Surface bound charge density is given by the discontinuity in normal electric field: $\\sigma' = \\varepsilon_0 (E_{2n} - E_{1n}) = -\\frac{q}{2\\pi} \\frac{\\varepsilon - 1}{\\varepsilon + 1} \\frac{l}{r^3}$.",
            "(b) Integrate $\\sigma'$ over the entire boundary plane."
        ],
        "answer": "(a) $\\sigma'(r) = -\\frac{q l}{2\\pi r^3} \\frac{\\varepsilon - 1}{\\varepsilon + 1}$; for $l \\to 0$, $\\sigma' \\to 0$ everywhere except at $r = 0$; (b) $q' = -q \\frac{\\varepsilon - 1}{\\varepsilon + 1}$",
        "solution": "**1. Method of Images for Planar Dielectric Boundary:**\nPlace the charge $q$ at $(0, 0, l)$ in vacuum ($z > 0$). The boundary is $z = 0$, and the dielectric occupies $z < 0$.\n- In vacuum ($z > 0$), the field is created by $q$ at $(0,0,l)$ and an image charge $q'$ at $(0,0,-l)$:\n  $$q' = -\\frac{\\varepsilon - 1}{\\varepsilon + 1} q$$\n- In dielectric ($z < 0$), the field is created by an effective charge $q''$ at $(0,0,l)$:\n  $$q'' = \\frac{2}{\\varepsilon + 1} q$$\n\n**2. Bound Surface Charge Density (Part a):**\nAt a point on the surface at distance $\\rho$ from the origin, $r = \\sqrt{\\rho^2 + l^2}$. The normal electric fields just above and below the surface are:\n$$E_{1z}(0^+) = -\\frac{q - q'}{4\\pi\\varepsilon_0} \\frac{l}{r^3} = -\\frac{q}{4\\pi\\varepsilon_0} \\frac{2\\varepsilon}{\\varepsilon + 1} \\frac{l}{r^3}$$\n$$E_{2z}(0^-) = -\\frac{q''}{4\\pi\\varepsilon_0\\varepsilon} \\frac{l}{r^3} = -\\frac{q}{4\\pi\\varepsilon_0} \\frac{2}{\\varepsilon(\\varepsilon + 1)} \\frac{l}{r^3}$$\nThe surface bound charge density is:\n$$\\sigma' = \\varepsilon_0 (E_{2z} - E_{1z}) = -\\frac{q}{2\\pi} \\frac{\\varepsilon - 1}{\\varepsilon + 1} \\frac{l}{r^3}$$\nAs $l \\to 0$, for any point $r = \\rho > 0$, $\\sigma' \\to 0$. At $\\rho = 0$, $\\sigma'$ diverges, concentrating into a point bound charge at the contact location.\n\n**3. Total Bound Charge (Part b):**\nIntegrating over the plane surface ($r^2 = \\rho^2 + l^2$, $2\\rho d\\rho = 2r dr$):\n$$q' = \\int_0^\\infty \\sigma' \\cdot 2\\pi \\rho \\, d\\rho = -q \\frac{\\varepsilon - 1}{\\varepsilon + 1} l \\int_l^\\infty \\frac{dr}{r^2} = -q \\frac{\\varepsilon - 1}{\\varepsilon + 1}$$",
        "tags": ["method of images", "dielectrics", "bound surface charge", "total bound charge"]
    },
    {
        "id": "3.90",
        "title": "Force Exerted by Bound Surface Charges on Point Charge",
        "difficulty": 2,
        "question": "Making use of the formulation and solution of Problem 3.89, find the magnitude of the force exerted by the bound surface charges of the dielectric on the point charge $q$.",
        "hints": [
            "The electric field produced by all the bound surface charges in the region $z > 0$ is identical to the field produced by the image charge $q' = -q \\frac{\\varepsilon - 1}{\\varepsilon + 1}$.",
            "The image charge is located at distance $2l$ from the real charge $q$.",
            "Calculate Coulomb's force between $q$ and $q'$: $F = \\frac{1}{4\\pi\\varepsilon_0} \\frac{|q q'|}{(2l)^2}$."
        ],
        "answer": "$F = \\frac{q^2}{16\\pi\\varepsilon_0 l^2} \\frac{\\varepsilon - 1}{\\varepsilon + 1}$",
        "solution": "**1. Equivalence to Image Charge:**\nIn the region $z > 0$ where the charge $q$ is located, the electric field created by all the polarized matter (bound surface charges) is identical to the field of a single point image charge:\n$$q' = -q \\frac{\\varepsilon - 1}{\\varepsilon + 1}$$\nlocated symmetrically behind the boundary at distance $2l$ from $q$.\n\n**2. Interaction Force:**\nThe force exerted by the dielectric surface charges on $q$ is therefore simply the Coulomb attraction to this image charge:\n$$F = \\frac{1}{4\\pi\\varepsilon_0} \\frac{|q q'|}{(2l)^2} = \\frac{1}{4\\pi\\varepsilon_0} \\frac{q^2 \\frac{\\varepsilon - 1}{\\varepsilon + 1}}{4l^2} = \\frac{q^2}{16\\pi\\varepsilon_0 l^2} \\frac{\\varepsilon - 1}{\\varepsilon + 1}$$",
        "tags": ["method of images", "dielectric force", "Coulomb attraction", "bound charges"]
    },
    {
        "id": "3.91",
        "title": "Point Charge on Boundary Between Vacuum and Dielectric",
        "difficulty": 2,
        "question": "A point charge $q$ is located on the plane dividing vacuum and an infinite uniform isotropic dielectric with permittivity $\\varepsilon$. Find the moduli of $\\mathbf{D}$ and $\\mathbf{E}$, and the potential $\\varphi$, as functions of distance $r$ from $q$.",
        "hints": [
            "By symmetry, the boundary conditions require the tangential component $E$ to be identical in both vacuum and dielectric at any radius $r$: $E_1(r) = E_2(r) = E(r)$.",
            "The displacement vectors are $D_1 = \\varepsilon_0 E$ in vacuum and $D_2 = \\varepsilon\\varepsilon_0 E$ in dielectric.",
            "Apply Gauss's theorem for $\\mathbf{D}$ over a sphere of radius $r$: $\\oint \\mathbf{D} \\cdot d\\mathbf{S} = 2\\pi r^2 D_1 + 2\\pi r^2 D_2 = q$."
        ],
        "answer": "$E(r) = \\frac{q}{2\\pi \\varepsilon_0 (\\varepsilon + 1) r^2}$; $D(r) = \\begin{cases} \\frac{q}{2\\pi (\\varepsilon + 1) r^2} & \\text{in vacuum} \\\\ \\frac{\\varepsilon q}{2\\pi (\\varepsilon + 1) r^2} & \\text{in dielectric} \\end{cases}$; $\\varphi(r) = \\frac{q}{2\\pi \\varepsilon_0 (\\varepsilon + 1) r}$",
        "solution": "**1. Symmetry and Continuity:**\nAt the dividing plane, the electric field is purely tangential to the interface by azimuthal and hemispherical symmetry. Therefore, the field strength $E(r)$ must be identical just above and just below the interface, and by radial symmetry, identical throughout both media at distance $r$:\n$$E_1(r) = E_2(r) = E(r)$$\n\n**2. Displacements in Both Media:**\n$$D_1(r) = \\varepsilon_0 E(r) \\quad (\\text{vacuum})$$\n$$D_2(r) = \\varepsilon\\varepsilon_0 E(r) \\quad (\\text{dielectric})$$\n\n**3. Gauss's Law for Displacement:**\nSurround charge $q$ with a sphere of radius $r$:\n$$\\oint \\mathbf{D} \\cdot d\\mathbf{S} = 2\\pi r^2 D_1 + 2\\pi r^2 D_2 = 2\\pi r^2 \\varepsilon_0 (1 + \\varepsilon) E(r) = q$$\nSolving for $E(r)$:\n$$E(r) = \\frac{q}{2\\pi\\varepsilon_0(\\varepsilon + 1)r^2}$$\n\n**4. Displacements and Potential:**\n$$D_1(r) = \\frac{q}{2\\pi(\\varepsilon + 1)r^2} \\quad (\\text{vacuum})$$\n$$D_2(r) = \\frac{\\varepsilon q}{2\\pi(\\varepsilon + 1)r^2} \\quad (\\text{dielectric})$$\nThe potential with $\\varphi(\\infty) = 0$ is:\n$$\\varphi(r) = \\int_r^\\infty E(r') dr' = \\frac{q}{2\\pi\\varepsilon_0(\\varepsilon + 1)r}$$",
        "tags": ["dielectric interface", "Gauss law for D", "electric displacement", "electric potential"]
    },
    {
        "id": "3.92",
        "title": "Charge in Dielectric Near Vacuum Boundary",
        "difficulty": 3,
        "question": "A small conducting ball carrying charge $q$ is located in a uniform isotropic dielectric of permittivity $\\varepsilon$ at distance $l$ from an infinite boundary plane with vacuum. Find the surface density of bound charges on the boundary plane as a function of distance $r$ from the ball. Analyse the result for $l \\to 0$.",
        "hints": [
            "Use the method of images: inside the dielectric, the effect of the vacuum interface is represented by an image charge $q' = \\frac{\\varepsilon - 1}{\\varepsilon + 1} q$ placed in vacuum at distance $l$ behind the boundary.",
            "In vacuum, the effective charge is $q'' = \\frac{2\\varepsilon}{\\varepsilon + 1} q$ at the location of $q$.",
            "Surface bound charge density: $\\sigma' = \\varepsilon_0 (E_{2n} - E_{1n}) = \\frac{q l}{2\\pi r^3} \\frac{\\varepsilon - 1}{\\varepsilon(\\varepsilon + 1)}$."
        ],
        "answer": "$\\sigma'(r) = \\frac{q l}{2\\pi r^3} \\frac{\\varepsilon - 1}{\\varepsilon(\\varepsilon + 1)}$; for $l \\to 0$, $\\sigma' \\to 0$ everywhere except at the point of contact",
        "solution": "**1. Method of Images:**\nPlace the dielectric in $z > 0$ and vacuum in $z < 0$. The charge $q$ is in the dielectric at $(0, 0, l)$.\n- In the dielectric ($z > 0$), the field is due to $q$ at $(0,0,l)$ and an image charge $q'$ at $(0,0,-l)$:\n  $$q' = \\frac{\\varepsilon - 1}{\\varepsilon + 1} q$$\n- In vacuum ($z < 0$), the field is due to effective charge $q''$ at $(0,0,l)$:\n  $$q'' = \\frac{2\\varepsilon}{\\varepsilon + 1} q$$\n\n**2. Normal Components of Electric Field:**\nAt a surface point at radius $\\rho$ (distance $r = \\sqrt{\\rho^2 + l^2}$ from the charge):\nIn the dielectric ($z = 0^+$):\n$$E_{1z} = \\frac{1}{4\\pi\\varepsilon_0\\varepsilon} \\left( -q \\frac{l}{r^3} - q' \\frac{l}{r^3} \\right) = -\\frac{q l}{4\\pi\\varepsilon_0\\varepsilon r^3} \\left( 1 + \\frac{\\varepsilon - 1}{\\varepsilon + 1} \\right) = -\\frac{q l}{2\\pi\\varepsilon_0(\\varepsilon + 1)r^3}$$\nIn vacuum ($z = 0^-$):\n$$E_{2z} = -\\frac{q'' l}{4\\pi\\varepsilon_0 r^3} = -\\frac{2\\varepsilon q l}{4\\pi\\varepsilon_0(\\varepsilon + 1)r^3}$$\n\n**3. Bound Surface Charge Density:**\n$$\\sigma' = -P_{1z} = -(\\varepsilon - 1)\\varepsilon_0 E_{1z} = \\frac{q l}{2\\pi r^3} \\frac{\\varepsilon - 1}{\\varepsilon(\\varepsilon + 1)}$$\nFor $l \\to 0$, $\\sigma' \\to 0$ for all $\\rho > 0$, concentrating into a singular point at $\\rho = 0$.",
        "tags": ["method of images", "dielectric-vacuum boundary", "bound surface charge"]
    },
    {
        "id": "3.93",
        "title": "Charge in Dielectric Near Conducting Plane",
        "difficulty": 2,
        "question": "A half-space filled with uniform isotropic dielectric of permittivity $\\varepsilon$ is bounded by a conducting plane. Inside the dielectric, at distance $l$ from the plane, is a small metal ball with charge $q$. Find the surface density of bound charges at the boundary plane as a function of distance $r$ from the ball.",
        "hints": [
            "In a dielectric medium bounded by a conductor, the image charge inside the conductor is $-q$ located at distance $l$ behind the plane.",
            "The total electric field at the conducting boundary is normal to the conductor: $E_n = \\frac{2 q l}{4\\pi\\varepsilon_0\\varepsilon r^3} = \\frac{q l}{2\\pi\\varepsilon_0\\varepsilon r^3}$.",
            "The bound surface charge density is $\\sigma' = P_n = (\\varepsilon - 1)\\varepsilon_0 E_n = \\frac{\\varepsilon - 1}{\\varepsilon} \\frac{q l}{2\\pi r^3}$."
        ],
        "answer": "$\\sigma'(r) = \\frac{\\varepsilon - 1}{\\varepsilon} \\frac{q l}{2\\pi r^3}$",
        "solution": "**1. Electric Field at Conducting Surface:**\nThe conducting plane at $z = 0$ is an equipotential surface. By the method of images, the electrostatic field in the dielectric ($z > 0$) is produced by the real charge $q$ at $(0,0,l)$ and an image charge $-q$ at $(0,0,-l)$ inside the conductor.\nAt the boundary $z = 0$, tangential field vanishes and the normal field in the dielectric is:\n$$E_n = 2 \\times \\frac{q}{4\\pi\\varepsilon_0\\varepsilon r^2} \\cos\\theta = \\frac{q l}{2\\pi\\varepsilon_0\\varepsilon r^3}$$\nwhere $r = \\sqrt{\\rho^2 + l^2}$.\n\n**2. Bound Surface Charge Density:**\nThe polarization at the boundary surface is:\n$$P_n = (\\varepsilon - 1)\\varepsilon_0 E_n = \\frac{\\varepsilon - 1}{\\varepsilon} \\frac{q l}{2\\pi r^3}$$\nSince the outward normal of the dielectric points into the conductor, the bound surface charge density is:\n$$\\sigma' = \\frac{\\varepsilon - 1}{\\varepsilon} \\frac{q l}{2\\pi r^3}$$",
        "tags": ["method of images", "conductor boundary", "dielectrics", "bound surface charge"]
    },
    {
        "id": "3.94",
        "title": "Field in Shorted Capacitor with Polarized Plate",
        "difficulty": 2,
        "question": "A plate of thickness $h$ made of uniform statically polarized dielectric with polarization $\\mathbf{P}$ perpendicular to the faces is placed inside a capacitor whose plates are interconnected by a wire. The separation between the capacitor plates is $d$. Find the field strength $\\mathbf{E}$ and displacement $\\mathbf{D}$ both in the gap and inside the dielectric.",
        "hints": [
            "Because the capacitor plates are connected together, the potential difference across them is zero: $\\Delta\\varphi = E_1 (d - h) + E_2 h = 0$, where region 1 is vacuum and region 2 is the dielectric.",
            "There are no free charges between the plates, so displacement $D$ is uniform throughout: $D_1 = D_2 = D$.",
            "In vacuum $D = \\varepsilon_0 E_1$. In the dielectric $D = \\varepsilon_0 E_2 + P$."
        ],
        "answer": "$E_1 = \\frac{P h}{\\varepsilon_0 d}$ (vacuum gap), $E_2 = -\\frac{P}{\\varepsilon_0}\\left(1 - \\frac{h}{d}\\right)$ (in dielectric); $D_1 = D_2 = P \\frac{h}{d}$",
        "solution": "**1. Boundary Conditions and Short Circuit:**\nLet $E_1$ be the electric field in the vacuum gap of thickness $d - h$, and $E_2$ the electric field inside the polarized dielectric plate of thickness $h$.\nSince the capacitor plates are shorted:\n$$\\int_0^d E \\, dx = E_1 (d - h) + E_2 h = 0$$\n\n**2. Continuity of Displacement:**\nWith no free charge between the plates, Gauss's law demands:\n$$D_1 = D_2 = D$$\nIn vacuum: $D = \\varepsilon_0 E_1 \\implies E_1 = \\frac{D}{\\varepsilon_0}$.\nIn the dielectric: $D = \\varepsilon_0 E_2 + P \\implies E_2 = \\frac{D - P}{\\varepsilon_0} = E_1 - \\frac{P}{\\varepsilon_0}$.\n\n**3. Solving for the Fields:**\nSubstitute $E_2 = E_1 - P/\\varepsilon_0$ into the zero-potential condition:\n$$E_1 (d - h) + \\left(E_1 - \\frac{P}{\\varepsilon_0}\\right) h = 0 \\implies E_1 d - \\frac{P h}{\\varepsilon_0} = 0$$\n$$E_1 = \\frac{P h}{\\varepsilon_0 d}$$\n$$E_2 = E_1 - \\frac{P}{\\varepsilon_0} = \\frac{P h}{\\varepsilon_0 d} - \\frac{P}{\\varepsilon_0} = -\\frac{P}{\\varepsilon_0}\\left(1 - \\frac{h}{d}\\right)$$\n$$D_1 = D_2 = \\varepsilon_0 E_1 = P \\frac{h}{d}$$",
        "tags": ["polarized dielectric", "shorted capacitor", "displacement continuity", "depolarization"]
    },
    {
        "id": "3.95",
        "title": "Space Density of Bound Charges in Radial Polarization",
        "difficulty": 1,
        "question": "A long round dielectric cylinder is polarized so that $\\mathbf{P} = \\alpha \\mathbf{r}$, where $\\alpha$ is a positive constant and $\\mathbf{r}$ is the radius vector from the cylinder axis. Find the space density $\\rho'$ of bound charges as a function of distance $r$ from the axis.",
        "hints": [
            "Use the general relation $\\rho' = -\\nabla \\cdot \\mathbf{P}$.",
            "In cylindrical coordinates with radial polarization $P_r(r) = \\alpha r$, the divergence is $\\nabla \\cdot \\mathbf{P} = \\frac{1}{r} \\frac{d}{dr}(r P_r)$.",
            "Substitute $P_r = \\alpha r$ and differentiate."
        ],
        "answer": "$\\rho' = -2\\alpha$ (independent of $r$)",
        "solution": "**1. Bound Volume Charge Density:**\nThe space density of bound charges is given by the negative divergence of polarization:\n$$\\rho' = -\\nabla \\cdot \\mathbf{P}$$\n\n**2. Divergence in Cylindrical Coordinates:**\nFor a vector with only a radial component $P_r(r) = \\alpha r$ depending only on $r$:\n$$\\nabla \\cdot \\mathbf{P} = \\frac{1}{r} \\frac{\\partial}{\\partial r}(r P_r) = \\frac{1}{r} \\frac{\\partial}{\\partial r}(\\alpha r^2) = \\frac{1}{r} (2\\alpha r) = 2\\alpha$$\n\n**3. Result:**\n$$\\rho' = -2\\alpha$$\nThe space density of bound charge is constant throughout the volume of the cylinder, independent of $r$.",
        "tags": ["bound charge density", "divergence", "cylindrical coordinates", "polarization"]
    },
    {
        "id": "3.96",
        "title": "Field of Uniformly Polarized Dielectric Sphere",
        "difficulty": 2,
        "question": "A dielectric ball of radius $R$ is polarized uniformly and statically with polarization $\\mathbf{P}$. Representing the ball as two uniformly charged spheres of charges $\\pm q$ with densities $\\pm\\rho$ slightly shifted by a displacement $\\mathbf{l}$:\n(a) find the electric field strength $\\mathbf{E}$ inside the ball;\n(b) demonstrate that the field outside the ball is that of a point dipole at the centre with dipole moment $\\mathbf{p}_0 = \\frac{4}{3}\\pi R^3 \\mathbf{P}$.",
        "hints": [
            "Inside a uniformly charged sphere of density $\\rho$, the field is $\\mathbf{E} = \\frac{\\rho \\mathbf{r}}{3\\varepsilon_0}$.",
            "Superpose the fields of two spheres displaced by $\\mathbf{l}$: $\\mathbf{E} = \\frac{\\rho \\mathbf{r}_+}{3\\varepsilon_0} - \\frac{\\rho \\mathbf{r}_-}{3\\varepsilon_0} = -\\frac{\\rho \\mathbf{l}}{3\\varepsilon_0} = -\\frac{\\mathbf{P}}{3\\varepsilon_0}$.",
            "Outside, each sphere acts as a point charge $\\pm q$ at its centre separated by $\\mathbf{l}$, which is an ideal dipole $\\mathbf{p}_0 = q\\mathbf{l} = \\frac{4}{3}\\pi R^3 \\mathbf{P}$."
        ],
        "answer": "(a) $\\mathbf{E} = -\\frac{\\mathbf{P}}{3\\varepsilon_0}$; (b) Outside, $\\varphi = \\frac{\\mathbf{p}_0 \\cdot \\mathbf{r}}{4\\pi\\varepsilon_0 r^3}$ with $\\mathbf{p}_0 = \\frac{4}{3}\\pi R^3 \\mathbf{P}$",
        "solution": "**(a) Field Inside the Ball:**\nA uniformly polarized sphere with $\\mathbf{P} = \\rho \\mathbf{l}$ is mathematically equivalent to two overlapping uniformly charged spheres of equal radius $R$ with volume charge densities $+\\rho$ and $-\\rho$, whose centres are displaced by vector $\\mathbf{l}$.\nInside a sphere of charge density $\\rho$, the electric field at radius vector $\\mathbf{r}$ from its centre is:\n$$\\mathbf{E}_+ = \\frac{\\rho}{3\\varepsilon_0} \\mathbf{r}_+, \\quad \\mathbf{E}_- = -\\frac{\\rho}{3\\varepsilon_0} \\mathbf{r}_-$$\nAt any point inside the intersection, $\\mathbf{r}_+ - \\mathbf{r}_- = -\\mathbf{l}$. Superposing the two fields:\n$$\\mathbf{E} = \\mathbf{E}_+ + \\mathbf{E}_- = \\frac{\\rho}{3\\varepsilon_0} (\\mathbf{r}_+ - \\mathbf{r}_-) = -\\frac{\\rho \\mathbf{l}}{3\\varepsilon_0} = -\\frac{\\mathbf{P}}{3\\varepsilon_0}$$\nThis depolarizing field is completely uniform throughout the sphere.\n\n**(b) Field Outside the Ball:**\nOutside both spheres, Gauss's law states that each sphere creates the exact electrostatic field of a point charge located at its centre:\n$$q_+ = +\\rho V = +\\frac{4}{3}\\pi R^3 \\rho, \\quad q_- = -\\frac{4}{3}\\pi R^3 \\rho$$\nseparated by displacement $\\mathbf{l}$. The system of two point charges $\\pm q$ separated by $\\mathbf{l}$ forms a dipole of moment:\n$$\\mathbf{p}_0 = q \\mathbf{l} = \\frac{4}{3}\\pi R^3 \\rho \\mathbf{l} = \\frac{4}{3}\\pi R^3 \\mathbf{P}$$\nTherefore, the potential and field outside the sphere are strictly identical to those of a point dipole $\\mathbf{p}_0$ located at the centre:\n$$\\varphi(\\mathbf{r}) = \\frac{\\mathbf{p}_0 \\cdot \\mathbf{r}}{4\\pi\\varepsilon_0 r^3}$$",
        "tags": ["uniformly polarized sphere", "depolarization factor", "dipole moment", "superposition"]
    },
    {
        "id": "3.97",
        "title": "Electric Field in a Spherical Cavity in a Dielectric",
        "difficulty": 2,
        "question": "Utilizing the solution of Problem 3.96, find the electric field strength $\\mathbf{E}_0$ in a spherical cavity in an infinite statically polarized uniform dielectric if the dielectric's polarization is $\\mathbf{P}$, and far from the cavity the field strength is $\\mathbf{E}$.",
        "hints": [
            "Use the principle of superposition: a medium without a cavity is equivalent to the medium with the cavity PLUS a polarized sphere of polarization $\\mathbf{P}$ filling the cavity.",
            "Therefore, $\\mathbf{E}_{\\text{solid}} = \\mathbf{E}_{\\text{cavity}} + \\mathbf{E}_{\\text{sphere}}$.",
            "From Problem 3.96, a polarized sphere creates inside itself field $\\mathbf{E}_{\\text{sphere}} = -\\frac{\\mathbf{P}}{3\\varepsilon_0}$."
        ],
        "answer": "$\\mathbf{E}_0 = \\mathbf{E} + \\frac{\\mathbf{P}}{3\\varepsilon_0}$",
        "solution": "**1. Superposition Principle:**\nConsider the continuous polarized dielectric with uniform macroscopic field $\\mathbf{E}$ and polarization $\\mathbf{P}$.\nImagine cutting out a sphere of dielectric from the medium. The field $\\mathbf{E}$ in the intact dielectric is the superposition of:\n- The field $\\mathbf{E}_0$ inside the cavity created by all external sources and the polarized dielectric surrounding the cavity;\n- The field $\\mathbf{E}_{\\text{sphere}}$ created inside the removed dielectric sphere by its own polarization $\\mathbf{P}$.\n\n$$\\mathbf{E} = \\mathbf{E}_0 + \\mathbf{E}_{\\text{sphere}}$$\n\n**2. Field of the Polarized Sphere:**\nFrom Problem 3.96, a uniformly polarized sphere of polarization $\\mathbf{P}$ produces an internal field:\n$$\\mathbf{E}_{\\text{sphere}} = -\\frac{\\mathbf{P}}{3\\varepsilon_0}$$\n\n**3. Field Inside the Cavity:**\n$$\\mathbf{E}_0 = \\mathbf{E} - \\mathbf{E}_{\\text{sphere}} = \\mathbf{E} - \\left(-\\frac{\\mathbf{P}}{3\\varepsilon_0}\\right) = \\mathbf{E} + \\frac{\\mathbf{P}}{3\\varepsilon_0}$$",
        "tags": ["spherical cavity", "superposition", "cavity field", "polarization"]
    },
    {
        "id": "3.98",
        "title": "Dielectric Ball in Uniform Electric Field",
        "difficulty": 2,
        "question": "A uniform dielectric ball of permittivity $\\varepsilon$ is placed in a uniform external electric field $\\mathbf{E}_0$. Under these conditions the dielectric becomes polarized uniformly. Find the electric field strength $\\mathbf{E}$ inside the ball and the polarization $\\mathbf{P}$.",
        "hints": [
            "The internal field is the sum of the external field and the depolarizing field of the polarized sphere: $\\mathbf{E} = \\mathbf{E}_0 - \\frac{\\mathbf{P}}{3\\varepsilon_0}$.",
            "The linear relation between polarization and internal field is $\\mathbf{P} = (\\varepsilon - 1)\\varepsilon_0 \\mathbf{E}$.",
            "Substitute $\\mathbf{P}$ into the field equation and solve for $\\mathbf{E}$ and $\\mathbf{P}$."
        ],
        "answer": "$\\mathbf{E} = \\frac{3}{\\varepsilon + 2}\\mathbf{E}_0$; $\\mathbf{P} = \\frac{3(\\varepsilon - 1)}{\\varepsilon + 2}\\varepsilon_0 \\mathbf{E}_0$",
        "solution": "**1. Superposition of Fields:**\nThe net electric field $\\mathbf{E}$ inside the sphere is the vector sum of the applied external field $\\mathbf{E}_0$ and the internal field due to bound surface charges (the depolarizing field):\n$$\\mathbf{E} = \\mathbf{E}_0 + \\mathbf{E}'$$\nFrom Problem 3.96, the depolarizing field of a uniformly polarized sphere is:\n$$\\mathbf{E}' = -\\frac{\\mathbf{P}}{3\\varepsilon_0} \\implies \\mathbf{E} = \\mathbf{E}_0 - \\frac{\\mathbf{P}}{3\\varepsilon_0}$$\n\n**2. Constitutive Equation:**\nIn an isotropic linear dielectric:\n$$\\mathbf{P} = (\\varepsilon - 1)\\varepsilon_0 \\mathbf{E}$$\n\n**3. Solving the System:**\nSubstitute $\\mathbf{P}$ into the field expression:\n$$\\mathbf{E} = \\mathbf{E}_0 - \\frac{\\varepsilon - 1}{3} \\mathbf{E}$$\n$$\\mathbf{E} \\left( 1 + \\frac{\\varepsilon - 1}{3} \\right) = \\mathbf{E}_0 \\implies \\mathbf{E} \\left( \\frac{\\varepsilon + 2}{3} \\right) = \\mathbf{E}_0$$\n$$\\mathbf{E} = \\frac{3}{\\varepsilon + 2}\\mathbf{E}_0$$\n\nSubstituting $\\mathbf{E}$ back to obtain $\\mathbf{P}$:\n$$\\mathbf{P} = (\\varepsilon - 1)\\varepsilon_0 \\frac{3}{\\varepsilon + 2}\\mathbf{E}_0 = \\frac{3(\\varepsilon - 1)}{\\varepsilon + 2}\\varepsilon_0 \\mathbf{E}_0$$",
        "tags": ["dielectric sphere in uniform field", "depolarization", "polarization", "internal field"]
    },
    {
        "id": "3.99",
        "title": "Field Inside Uniformly Transversely Polarized Cylinder",
        "difficulty": 2,
        "question": "An infinitely long round dielectric cylinder is polarized uniformly and statically, the polarization $\\mathbf{P}$ being perpendicular to the cylinder axis. Find the electric field strength $\\mathbf{E}$ inside the dielectric.",
        "hints": [
            "Represent the cylinder as two overlapping infinitely long cylinders of uniform volume charge densities $\\pm\\rho$ displaced by transverse vector $\\mathbf{l}$, where $\\mathbf{P} = \\rho \\mathbf{l}$.",
            "Inside a cylinder of uniform charge density $\\rho$, Gauss's law gives $\\mathbf{E} = \\frac{\\rho \\mathbf{r}}{2\\varepsilon_0}$.",
            "Superpose the fields of the two displaced cylinders: $\\mathbf{E} = \\frac{\\rho}{2\\varepsilon_0}(\\mathbf{r}_+ - \\mathbf{r}_-) = -\\frac{\\rho \\mathbf{l}}{2\\varepsilon_0} = -\\frac{\\mathbf{P}}{2\\varepsilon_0}$."
        ],
        "answer": "$\\mathbf{E} = -\\frac{\\mathbf{P}}{2\\varepsilon_0}$",
        "solution": "**1. Superposition Model:**\nAn infinitely long cylinder with uniform transverse polarization $\\mathbf{P} = \\rho \\mathbf{l}$ can be represented as two overlapping oppositely charged circular cylinders of volume charge densities $+\\rho$ and $-\\rho$, with their axes displaced by transverse vector $\\mathbf{l}$.\n\n**2. Electric Field of a Charged Cylinder:**\nBy Gauss's theorem in cylindrical coordinates, inside a cylinder carrying uniform charge density $\\rho$, the electric field at radius vector $\\mathbf{r}$ from the axis is:\n$$\\oint \\mathbf{E} \\cdot d\\mathbf{S} = E \\cdot (2\\pi r L) = \\frac{\\rho (\\pi r^2 L)}{\\varepsilon_0} \\implies \\mathbf{E}(\\mathbf{r}) = \\frac{\\rho \\mathbf{r}}{2\\varepsilon_0}$$\n\n**3. Field Inside the Polarized Cylinder:**\nAt any point in the overlap region:\n$$\\mathbf{E} = \\mathbf{E}_+ + \\mathbf{E}_- = \\frac{\\rho}{2\\varepsilon_0} \\mathbf{r}_+ - \\frac{\\rho}{2\\varepsilon_0} \\mathbf{r}_- = \\frac{\\rho}{2\\varepsilon_0} (\\mathbf{r}_+ - \\mathbf{r}_-)$$\nSince $\\mathbf{r}_+ - \\mathbf{r}_- = -\\mathbf{l}$:\n$$\\mathbf{E} = -\\frac{\\rho \\mathbf{l}}{2\\varepsilon_0} = -\\frac{\\mathbf{P}}{2\\varepsilon_0}$$\nThe depolarizing field inside the cylinder is uniform and directed opposite to $\\mathbf{P}$.",
        "tags": ["polarized cylinder", "depolarization factor", "superposition", "internal field"]
    },
    {
        "id": "3.100",
        "title": "Dielectric Cylinder in Perpendicular Uniform Field",
        "difficulty": 2,
        "question": "A long round cylinder made of uniform dielectric with permittivity $\\varepsilon$ is placed in a uniform electric field $\\mathbf{E}_0$, the cylinder axis being perpendicular to $\\mathbf{E}_0$. Under these conditions the cylinder becomes polarized uniformly. Making use of the result of Problem 3.99, find the electric field strength $\\mathbf{E}$ inside the cylinder and the polarization $\\mathbf{P}$.",
        "hints": [
            "The field inside the cylinder is $\\mathbf{E} = \\mathbf{E}_0 + \\mathbf{E}'$, where $\\mathbf{E}' = -\\frac{\\mathbf{P}}{2\\varepsilon_0}$ from Problem 3.99.",
            "Use the material equation $\\mathbf{P} = (\\varepsilon - 1)\\varepsilon_0 \\mathbf{E}$.",
            "Solve the system for $\\mathbf{E}$ and $\\mathbf{P}$."
        ],
        "answer": "$\\mathbf{E} = \\frac{2}{\\varepsilon + 1}\\mathbf{E}_0$; $\\mathbf{P} = \\frac{2(\\varepsilon - 1)}{\\varepsilon + 1}\\varepsilon_0 \\mathbf{E}_0$",
        "solution": "**1. Depolarizing Field in Cylinder:**\nFrom Problem 3.99, the bound charges of a cylinder with uniform transverse polarization $\\mathbf{P}$ create a uniform internal depolarizing field:\n$$\\mathbf{E}' = -\\frac{\\mathbf{P}}{2\\varepsilon_0}$$\n\n**2. Total Internal Field:**\nThe resultant electric field inside the cylinder is:\n$$\\mathbf{E} = \\mathbf{E}_0 + \\mathbf{E}' = \\mathbf{E}_0 - \\frac{\\mathbf{P}}{2\\varepsilon_0}$$\n\n**3. Constitutive Relation and Solution:**\nUsing $\\mathbf{P} = (\\varepsilon - 1)\\varepsilon_0 \\mathbf{E}$:\n$$\\mathbf{E} = \\mathbf{E}_0 - \\frac{\\varepsilon - 1}{2} \\mathbf{E}$$\n$$\\mathbf{E} \\left( 1 + \\frac{\\varepsilon - 1}{2} \\right) = \\mathbf{E}_0 \\implies \\mathbf{E} \\left( \\frac{\\varepsilon + 1}{2} \\right) = \\mathbf{E}_0$$\n$$\\mathbf{E} = \\frac{2}{\\varepsilon + 1}\\mathbf{E}_0$$\n\nSubstituting into the expression for $\\mathbf{P}$:\n$$\\mathbf{P} = (\\varepsilon - 1)\\varepsilon_0 \\frac{2}{\\varepsilon + 1}\\mathbf{E}_0 = \\frac{2(\\varepsilon - 1)}{\\varepsilon + 1}\\varepsilon_0 \\mathbf{E}_0$$",
        "tags": ["dielectric cylinder in uniform field", "depolarization factor", "internal field", "polarization"]
    }
]
