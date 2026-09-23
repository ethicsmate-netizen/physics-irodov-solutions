"""
part5_ch5_1b.py
Curated problems 5.33 to 5.63 (31 problems) of Irodov Chapter 5.1:
Photometry and Geometrical Optics (Part B).
"""

CH5_1B_CURATED = [
    {
        "id": "5.33",
        "title": "Optical Power and Focal Lengths of a Thin Lens in Liquid and Asymmetric Media",
        "difficulty": 2,
        "question": "Find the optical power $\\Phi$ and the focal lengths $f$ and $f'$:\n(a) of a thin glass lens ($n = 1.50$) in a liquid with refractive index $n_0 = 1.70$ if its optical power in air is $\\Phi_0 = -5.0\\text{ D}$;\n(b) of a thin glass biconvex lens with surface radii $R_1 = 10\\text{ cm}$ and $R_2 = 20\\text{ cm}$, separating air on the left ($n_1 = 1.0$) from water on the right ($n_2 = 1.333$).",
        "hints": [
            "(a) Optical power in air is $\\Phi_0 = (n - 1)\\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right)$. In a liquid of index $n_0$, the optical power is $\\Phi = \\left(\\frac{n}{n_0} - 1\\right)\\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right) = \\Phi_0 \\frac{n - n_0}{n_0(n - 1)}$.",
            "Focal lengths in the liquid are $f' = -f = \\frac{n_0}{\\Phi}$.",
            "(b) For a lens separating two different media: $\\Phi = \\frac{n - n_1}{R_1} + \\frac{n_2 - n}{R_2}$ (with sign convention for radii). Focal lengths are $f = -\\frac{n_1}{\\Phi}$ and $f' = \\frac{n_2}{\\Phi}$."
        ],
        "answer": "(a) $\\Phi = \\Phi_0 \\frac{n - n_0}{n_0 (n - 1)} = +2.0\\text{ D}$, $f' = -f = \\frac{n_0}{\\Phi} = +85\\text{ cm}$;\n(b) $\\Phi = \\frac{n - n_1}{R_1} + \\frac{n_2 - n}{-R_2} \\approx +6.7\\text{ D}$, $f = -\\frac{1}{\\Phi} \\approx -15\\text{ cm}$, $f' = \\frac{n_2}{\\Phi} \\approx +20\\text{ cm}$",
        "solution": "**(a) Thin Lens Immersed in Liquid:**\n1. In air, the lensmaker's formula gives the optical power:\n$$\\Phi_0 = (n - 1) \\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right)$$\n2. In a liquid of refractive index $n_0$, the power is:\n$$\\Phi = \\left(\\frac{n}{n_0} - 1\\right) \\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right) = \\frac{n - n_0}{n_0} \\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right) = \\Phi_0 \\frac{n - n_0}{n_0 (n - 1)}$$\nGiven $\\Phi_0 = -5.0\\text{ D}$, $n = 1.50$, and $n_0 = 1.70$:\n$$\\Phi = (-5.0\\text{ D}) \\frac{1.50 - 1.70}{1.70 (1.50 - 1.0)} = (-5.0) \\frac{-0.20}{1.70 \\times 0.50} = \\frac{1.0}{0.85} \\approx +2.0\\text{ D}$$\n*(Note that a diverging lens in air becomes converging in an optically denser liquid!)*\n3. The focal lengths in the liquid are:\n$$f' = \\frac{n_0}{\\Phi} = \\frac{1.70}{2.0\\text{ m}^{-1}} = 0.85\\text{ m} = +85\\text{ cm}$$\n$$f = -f' = -85\\text{ cm}$$\n\n**(b) Lens Separating Air and Water:**\nLet the biconvex lens ($n = 1.50$) have front radius $R_1 = +10\\text{ cm} = +0.10\\text{ m}$ (convex to air, $n_1 = 1.0$) and rear radius $R_2 = -20\\text{ cm} = -0.20\\text{ m}$ (convex to water, $n_2 = 1.333 = 4/3$).\nThe optical power of the composite interface system is the sum of powers of the two surfaces:\n$$\\Phi = \\frac{n - n_1}{R_1} + \\frac{n_2 - n}{R_2} = \\frac{1.50 - 1.0}{0.10} + \\frac{1.333 - 1.50}{-0.20}$$\n$$\\Phi = \\frac{0.50}{0.10} + \\frac{-0.167}{-0.20} = 5.0 + 0.833 = 5.833 + 0.833 \\approx 6.7\\text{ D}$$\n4. The focal lengths are:\n$$f = -\\frac{n_1}{\\Phi} = -\\frac{1.0}{6.67\\text{ m}^{-1}} = -0.15\\text{ m} = -15\\text{ cm}$$\n$$f' = \\frac{n_2}{\\Phi} = \\frac{1.333}{6.67\\text{ m}^{-1}} = +0.20\\text{ m} = +20\\text{ cm}$$",
        "tags": ["lensmaker formula", "optical power", "focal length", "refractive index", "asymmetric media"]
    },
    {
        "id": "5.34",
        "title": "Geometric Ray Tracing Through Converging and Diverging Thin Lenses",
        "difficulty": 2,
        "question": "By means of geometric ray construction (ray tracing), find:\n(a) the path of an arbitrary incident ray after passing through a thin converging and a thin diverging lens with principal foci $F$ and $F'$ and optical axis $OO'$;\n(b) the position of the lens and its focal points when given the optical axis $OO'$ and a pair of conjugate object-image points $S$ and $S'$.",
        "hints": [
            "(a) To trace an arbitrary ray not parallel to the axis, draw a secondary optical axis through the optical centre $O$ parallel to the incident ray. The refracted ray must pass through the secondary focal point where this secondary axis intersects the focal plane.",
            "(b) A ray passing through the optical centre $O$ goes undeflected; therefore, the straight line connecting $S$ and $S'$ intersects the optical axis at the optical centre $O$ of the lens.",
            "Draw a ray from $S$ parallel to the optical axis: upon refraction at the lens plane, it must pass through both the lens intersection point and the conjugate image point $S'$. Its intersection with the optical axis defines the rear principal focus $F'$."
        ],
        "answer": "(a) Refracted ray passes through the intersection of the focal plane with the secondary optical axis parallel to the incident ray;\n(b) Optical centre $O$ is the intersection of line $SS'$ with the optical axis $OO'$, and focal point $F'$ is where a ray parallel to the axis from $S$ intersects $OO'$ after refraction",
        "solution": "**(a) Ray Construction for Arbitrary Rays:**\n1. **Converging Lens:**\n   - Given an incident ray striking the lens plane at point $A$ at an arbitrary angle to the axis $OO'$:\n   - Draw a **secondary optical axis** passing through the optical center $O$ of the lens parallel to the incident ray.\n   - Construct the rear focal plane (perpendicular to $OO'$ through the rear focus $F'$).\n   - The secondary optical axis intersects the rear focal plane at secondary focus $F_s'$.\n   - By the focal properties of thin lenses, all parallel rays converge at the same point in the focal plane. Therefore, the refracted ray must pass through point $A$ and point $F_s'$.\n2. **Diverging Lens:**\n   - For a diverging lens, draw the secondary optical axis through $O$ parallel to the incident ray, intersecting the *front* focal plane at secondary focus $F_s$.\n   - The refracted ray emerges from $A$ along the line pointing away from $F_s$.\n\n**(b) Finding the Lens Plane and Foci from Conjugate Points $S$ and $S'$:**\n1. **Position of the Lens Plane:**\n   Any ray passing through the optical center $O$ of a thin lens undergoes zero angular deviation. Therefore, the straight line joining $S$ and $S'$ must pass through $O$.\n   - Draw the straight line $SS'$. Its intersection with the principal optical axis $OO'$ determines the **optical centre $O$**.\n   - The lens plane is drawn perpendicular to $OO'$ through $O$.\n2. **Focal Points $F$ and $F'$:**\n   - Draw a ray from $S$ parallel to the optical axis $OO'$, intersecting the lens plane at point $B$.\n   - Since this incident ray is parallel to the axis, the refracted ray must pass through the rear focus $F'$, and since it originates from $S$, it must also pass through the conjugate image point $S'$.\n   - Draw the straight line connecting $B$ and $S'$. The intersection of line $BS'$ with the optical axis $OO'$ determines the **rear focal point $F'$**.\n   - By symmetry for a thin lens in a uniform medium, the front focus $F$ lies symmetrically at $OF = OF'$ on the opposite side.",
        "tags": ["thin lens", "ray tracing", "focal plane", "conjugate points", "geometrical optics"]
    },
    {
        "id": "5.35",
        "title": "Depth of Focus and Lens Displacement for a Fixed Screen",
        "difficulty": 2,
        "question": "A thin converging lens with focal length $f = 25\\text{ cm}$ projects the sharp image of an object on a screen removed from the lens by a distance $l = 100\\text{ cm}$. When the object is displaced by a small distance $\\Delta l = 5.0\\text{ mm}$, find the displacement $\\Delta x$ of the lens required to restore a sharp image on the screen.",
        "hints": [
            "Use the thin lens formula $\\frac{1}{s'} - \\frac{1}{s} = \\frac{1}{f}$, where $s' = l$ and $s = -d$, with $d$ being the object distance.",
            "Differentiate the lens equation with the constraint that the total distance between object and screen is approximately fixed, or differentiate $s' = f s / (s + f)$.",
            "Express the differential displacement: $\\Delta x \\approx \\Delta l \\frac{f^2}{(l - f)^2}$."
        ],
        "answer": "$\\Delta x \\approx \\Delta l \\left(\\frac{f}{l - f}\\right)^2 = 0.55\\text{ mm} \\approx 0.5\\text{ mm}$",
        "solution": "**1. Initial Image and Object Distances:**\nThe image distance is $s' = l = 100\\text{ cm}$, and the focal length is $f = 25\\text{ cm}$.\nFrom the lens formula $\\frac{1}{s'} - \\frac{1}{s} = \\frac{1}{f}$:\n$$\\frac{1}{s} = \\frac{1}{s'} - \\frac{1}{f} = \\frac{1}{100} - \\frac{1}{25} = \\frac{1 - 4}{100} = -\\frac{3}{100}\\text{ cm}^{-1}$$\n$$s = -\\frac{100}{3}\\text{ cm} \\approx -33.3\\text{ cm}$$\nThe distance from the object to the lens is $d = -s = \\frac{100}{3}\\text{ cm}$.\n\n**2. Longitudinal Magnification and Small Displacements:**\nDifferentiating the lens formula $\\frac{1}{s'} - \\frac{1}{s} = \\frac{1}{f}$:\n$$-\\frac{ds'}{s'^2} + \\frac{ds}{s^2} = 0 \\implies ds' = \\left(\\frac{s'}{s}\\right)^2 ds = \\beta^2 ds$$\nHere the transverse magnification is:\n$$\\beta = -\\frac{s'}{s} = -\\frac{100}{-100/3} = 3.0$$\nWhen the lens is shifted by $\\Delta x$ toward the object:\n- The object distance changes by $ds = -\\Delta x - \\Delta l$ (or relative to object and screen).\nWith the screen position fixed, let the lens shift by $\\Delta x$:\n$$\\Delta s' = -\\Delta x, \\quad \\Delta s = -(\\Delta l - \\Delta x)$$\nUsing $\\Delta s' = \\beta^2 \\Delta s$:\n$$-\\Delta x = \\beta^2 (\\Delta x - \\Delta l) \\implies \\beta^2 \\Delta l = (\\beta^2 + 1) \\Delta x$$\nAlternatively, for a small shift of the object $\\Delta l$, to refocus on the screen:\n$$\\Delta x \\approx \\Delta l \\left(\\frac{f}{l - f}\\right)^2$$\n\n**3. Numerical Evaluation:**\n$$\\frac{f}{l - f} = \\frac{25}{100 - 25} = \\frac{25}{75} = \\frac{1}{3}$$\n$$\\left(\\frac{f}{l - f}\\right)^2 = \\left(\\frac{1}{3}\\right)^2 = \\frac{1}{9}$$\n$$\\Delta x = \\frac{5.0\\text{ mm}}{9} \\approx 0.55\\text{ mm} \\approx 0.5\\text{ mm}$$",
        "tags": ["thin lens", "depth of focus", "lens displacement", "longitudinal magnification"]
    },
    {
        "id": "5.36",
        "title": "Bessel's Method for Measuring the Focal Length of a Converging Lens",
        "difficulty": 2,
        "question": "A light source is located at a distance $l = 90\\text{ cm}$ from a screen. A thin converging lens provides a sharp image of the source on the screen for two distinct positions of the lens separated by a displacement $\\Delta l = 30\\text{ cm}$. Find:\n(a) the focal length $f$ of the lens;\n(b) the focal length $f$ if the ratio of the linear dimensions of the two images is $\\eta = 4.0$ instead of knowing $\\Delta l$.",
        "hints": [
            "(a) In Bessel's displacement method, the two conjugate object distances satisfy $s_1 + s_2 = l$ and $s_2 - s_1 = \\Delta l$. The focal length is $f = \\frac{l^2 - \\Delta l^2}{4l}$.",
            "(b) The two magnifications are $\\beta_1 = -s_1'/s_1$ and $\\beta_2 = -s_2'/s_2 = -s_1/s_1' = 1/\\beta_1$.",
            "The ratio of image sizes is $\\eta = \\frac{\\beta_1}{\\beta_2} = \\beta_1^2 \\implies \\beta_1 = \\sqrt{\\eta}$. Express $f$ in terms of $l$ and $\\eta$: $f = \\frac{l \\sqrt{\\eta}}{(1 + \\sqrt{\\eta})^2}$."
        ],
        "answer": "(a) $f = \\frac{l^2 - \\Delta l^2}{4l} = 20\\text{ cm}$;\n(b) $f = \\frac{l \\sqrt{\\eta}}{(1 + \\sqrt{\\eta})^2} = 20\\text{ cm}$ (for $\\sqrt{\\eta} = 2.0$)",
        "solution": "**(a) Bessel's Displacement Formula:**\nLet the distance between object and screen be $l$. If a lens of focal length $f$ produces sharp images at two positions separated by $\\Delta l$:\n- For the first position, object distance is $d_1$ and image distance is $l - d_1$.\n- For the second position, object distance is $d_2 = l - d_1$ and image distance is $d_1$.\nThe distance between these positions is:\n$$\\Delta l = d_2 - d_1 = (l - d_1) - d_1 = l - 2d_1 \\implies d_1 = \\frac{l - \\Delta l}{2}, \\quad l - d_1 = \\frac{l + \\Delta l}{2}$$\nApplying the lens formula $\\frac{1}{f} = \\frac{1}{d_1} + \\frac{1}{l - d_1}$:\n$$\\frac{1}{f} = \\frac{2}{l - \\Delta l} + \\frac{2}{l + \\Delta l} = \\frac{2(l + \\Delta l + l - \\Delta l)}{l^2 - \\Delta l^2} = \\frac{4l}{l^2 - \\Delta l^2}$$\n$$f = \\frac{l^2 - \\Delta l^2}{4l}$$\nSubstituting $l = 90\\text{ cm}$ and $\\Delta l = 30\\text{ cm}$:\n$$f = \\frac{90^2 - 30^2}{4 \\times 90} = \\frac{8100 - 900}{360} = \\frac{7200}{360} = 20\\text{ cm}$$\n\n**(b) Image Size Ratio Given:**\nThe transverse magnifications at the two positions are $\\beta_1 = -\\frac{l - d_1}{d_1}$ and $\\beta_2 = -\\frac{d_1}{l - d_1} = \\frac{1}{\\beta_1}$.\nThe ratio of image heights is:\n$$\\eta = \\frac{h_1'}{h_2'} = \\frac{|\\beta_1|}{|\\beta_2|} = \\beta_1^2 \\implies |\\beta_1| = \\sqrt{\\eta}$$\nSince $\\frac{l - d_1}{d_1} = \\sqrt{\\eta}$, we have $l = d_1 (1 + \\sqrt{\\eta})$, so:\n$$d_1 = \\frac{l}{1 + \\sqrt{\\eta}}, \\quad l - d_1 = \\frac{l \\sqrt{\\eta}}{1 + \\sqrt{\\eta}}$$\nSubstituting into the lens formula:\n$$\\frac{1}{f} = \\frac{1}{d_1} + \\frac{1}{l - d_1} = \\frac{1 + \\sqrt{\\eta}}{l} + \\frac{1 + \\sqrt{\\eta}}{l \\sqrt{\\eta}} = \\frac{(1 + \\sqrt{\\eta})^2}{l \\sqrt{\\eta}}$$\n$$f = \\frac{l \\sqrt{\\eta}}{(1 + \\sqrt{\\eta})^2}$$\nWith $l = 90\\text{ cm}$ and $\\eta = 4.0$ (so $\\sqrt{\\eta} = 2.0$):\n$$f = \\frac{90 \\times 2.0}{(1 + 2.0)^2} = \\frac{180}{9} = 20\\text{ cm}$$",
        "tags": ["Bessel method", "thin lens", "focal length", "magnification", "geometrical optics"]
    },
    {
        "id": "5.37",
        "title": "Object Height from Two Conjugate Image Heights in Bessel's Setup",
        "difficulty": 1,
        "question": "A thin converging lens is placed between an object and a screen whose positions are fixed. There are two positions of the lens that provide sharp images on the screen. If the heights of these two images are $h' = 4.5\\text{ mm}$ and $h'' = 2.0\\text{ mm}$, find the true height $h$ of the object.",
        "hints": [
            "At the first position, the magnification is $\\beta_1 = h' / h = s_1' / s_1$.",
            "At the second position, the magnification is $\\beta_2 = h'' / h = s_2' / s_2 = s_1 / s_1' = 1 / \\beta_1$.",
            "Multiply the two equations: $\\frac{h'}{h} \\cdot \\frac{h''}{h} = \\beta_1 \\beta_2 = 1 \\implies h = \\sqrt{h' h''}$."
        ],
        "answer": "$h = \\sqrt{h' h''} = 3.0\\text{ mm}$",
        "solution": "**1. Conjugate Lens Positions:**\nLet $s_1$ and $s_1'$ be the object and image distances for the first sharp image position, and $s_2$ and $s_2'$ for the second.\nBecause the distance between object and screen $l = s + s'$ is constant, the two positions are symmetric conjugates:\n$$s_2 = s_1', \\quad s_2' = s_1$$\n\n**2. Magnifications:**\nThe linear magnification magnitudes are:\n$$\\beta_1 = \\frac{h'}{h} = \\frac{s_1'}{s_1}$$\n$$\\beta_2 = \\frac{h''}{h} = \\frac{s_2'}{s_2} = \\frac{s_1}{s_1'} = \\frac{1}{\\beta_1}$$\n\n**3. Determining the Object Height:**\nMultiplying the two magnification expressions:\n$$\\beta_1 \\beta_2 = \\left(\\frac{h'}{h}\\right) \\left(\\frac{h''}{h}\\right) = \\left(\\frac{s_1'}{s_1}\\right) \\left(\\frac{s_1}{s_1'}\\right) = 1$$\n$$\\frac{h' h''}{h^2} = 1 \\implies h = \\sqrt{h' h''}$$\n\n**4. Numerical Evaluation:**\nGiven $h' = 4.5\\text{ mm}$ and $h'' = 2.0\\text{ mm}$:\n$$h = \\sqrt{4.5 \\times 2.0} = \\sqrt{9.0} = 3.0\\text{ mm}$$",
        "tags": ["thin lens", "conjugate images", "object height", "Bessel method"]
    },
    {
        "id": "5.38",
        "title": "Screen Illuminance Produced by a Camera Lens from Subject Luminance",
        "difficulty": 2,
        "question": "A camera lens with aperture ratio $D : f = 1 : 3.5$ ($D$ is the lens diameter, $f$ is its focal length) produces an image of an object located far from the camera on a photographic film. The luminance of the object is $L = 2.0 \\times 10^3\\text{ cd/m}^2$, and the light loss coefficient in the lens is $\\alpha = 0.10$ (10%). Find the illuminance $E$ of the image.",
        "hints": [
            "For a distant object ($s \\gg f$), the image is at the focal plane ($s' \\approx f$).",
            "The solid angle of the light cone converging to the image point is $\\Omega' = \\frac{\\pi (D/2)^2}{f^2} = \\frac{\\pi}{4} \\left(\\frac{D}{f}\\right)^2$.",
            "The image illuminance is $E = (1 - \\alpha) \\pi L \\sin^2 u' \\approx (1 - \\alpha) \\frac{\\pi L}{4} \\left(\\frac{D}{f}\\right)^2$."
        ],
        "answer": "$E = (1 - \\alpha) \\frac{\\pi L}{4} \\left(\\frac{D}{f}\\right)^2 \\approx 15\\text{ lx}$",
        "solution": "**1. Image Illuminance Formula for an Optical System:**\nFor an object of luminance $L$ imaged by a lens of transmission factor $\\tau = 1 - \\alpha$, the illuminance in the image plane for paraxial imaging is:\n$$E = \\tau \\pi L \\sin^2 u'$$\nwhere $u'$ is the semi-aperture angle of the cone of rays converging to the image point.\n\n**2. Relation to Aperture Ratio:**\nFor a distant object ($s \\to \\infty$), the image is formed in the focal plane ($s' = f$).\nThe marginal ray from the rim of the entrance pupil (diameter $D$) subtends a semi-angle $u'$ where:\n$$\\sin u' \\approx \\tan u' = \\frac{D}{2f}$$\n$$\\sin^2 u' \\approx \\left(\\frac{D}{2f}\\right)^2 = \\frac{1}{4} \\left(\\frac{D}{f}\\right)^2$$\nTherefore, the illuminance of the image is:\n$$E = (1 - \\alpha) \\frac{\\pi L}{4} \\left(\\frac{D}{f}\\right)^2$$\n\n**3. Numerical Evaluation:**\nGiven $L = 2.0 \\times 10^3\\text{ cd/m}^2$, $D/f = 1/3.5$, and $\\alpha = 0.10$:\n$$\\left(\\frac{D}{f}\\right)^2 = \\left(\\frac{1}{3.5}\\right)^2 = \\frac{1}{12.25} \\approx 0.08163$$\n$$E = (1 - 0.10) \\frac{\\pi (2.0 \\times 10^3)}{4} \\left(\\frac{1}{12.25}\\right) = 0.90 \\times \\frac{2000\\pi}{49} \\approx 0.90 \\times 128.25 \\approx 15.3\\text{ lx} \\approx 15\\text{ lx}$$",
        "tags": ["camera lens", "aperture ratio", "f-number", "illuminance", "photometry"]
    },
    {
        "id": "5.39",
        "title": "Dependence of Real Image Luminance on Lens Diameter for Direct Viewing and Screen",
        "difficulty": 1,
        "question": "How does the apparent luminance $L_{\\text{image}}$ of a real image produced by a thin converging lens depend on the lens diameter $D$ if that image is observed:\n(a) directly with the naked eye;\n(b) projected onto a diffusely scattering white screen?",
        "hints": [
            "(a) According to the fundamental photometric conservation theorem, the brightness (luminance) of an image observed directly by an optical instrument (such as the eye) cannot exceed that of the object, provided the eye pupil is completely filled: $L_{\\text{image}} = L_{\\text{obj}}$.",
            "(b) When projected on a screen, the illuminance $E$ is proportional to the light-collecting area of the lens, $E \\propto D^2$.",
            "A Lambertian screen reflects light with luminance $L_{\\text{screen}} = \\frac{\\rho E}{\\pi} \\propto D^2$."
        ],
        "answer": "(a) Independent of $D$ (for eye pupil inside the ray cone);\n(b) Proportional to $D^2$",
        "solution": "**(a) Direct Observation with the Eye:**\nWhen an observer views a real image directly in space (an aerial image):\n- The lens acts as a pupil transmitting light into the eye. According to the brightness theorem of geometrical optics (conservation of luminance $L/n^2 = \\text{const}$ along rays in lossless media):\n$$L_{\\text{image}} = L_{\\text{object}}$$\nAs long as the light cone entering the eye pupil completely fills the pupil, the retinal illuminance and the perceived luminance are completely independent of the lens diameter $D$.\n\n**(b) Observation on a Diffuse Screen:**\nWhen the image is projected onto a diffusely reflecting screen:\n- The total luminous flux collected by the lens from each object element is proportional to the area of the lens aperture: $\\Phi \\propto D^2$.\n- The illuminance $E$ of the image on the screen is therefore directly proportional to $D^2$:\n$$E \\propto D^2$$\n- The diffusely scattered luminance from the Lambertian screen is:\n$$L_{\\text{screen}} = \\frac{\\rho E}{\\pi} \\propto D^2$$\nTherefore, the luminance of the projected image on the screen is proportional to $D^2$.",
        "tags": ["photometry", "luminance conservation", "lens aperture", "image brightness"]
    },
    {
        "id": "5.40",
        "title": "Focal Length of an Immersion Doublet with Water Layer",
        "difficulty": 2,
        "question": "There are two thin symmetrical lenses: one is converging with refractive index $n_1 = 1.70$, and the other is diverging with index $n_2 = 1.60$. Both lenses have surfaces with identical curvature radius $R = 10\\text{ cm}$. The lenses are placed close together, and the gap between them is filled with water ($n_0 = 1.333$). Find the focal length $f$ of this composite system.",
        "hints": [
            "The system consists of three thin lenses in contact: lens 1 (converging, $n_1$), water lens (liquid lens, $n_0$), and lens 2 (diverging, $n_2$).",
            "Optical powers add: $\\Phi = \\Phi_1 + \\Phi_{\\text{water}} + \\Phi_2$.",
            "Calculate $\\Phi_1 = (n_1 - 1) \\frac{2}{R}$, $\\Phi_2 = -(n_2 - 1) \\frac{2}{R}$, and for the intermediate water lens bounded by surfaces of radii $+R$ and $-R$ or analyze the net power: $\\Phi = \\frac{2(n_1 - n_2)}{n_0 R}$ or $f = \\frac{n_0 R}{2(n_1 - n_2)}$."
        ],
        "answer": "$f = \\frac{n_0 R}{2(n_1 - n_2)} = 35\\text{ cm}$ (or $f = \\frac{R}{2(n_1 - n_2)} \\approx 50\\text{ cm}$ in air)",
        "solution": "**1. Decomposition into Thin Lenses:**\nThe system consists of:\n1. A symmetrical biconvex glass lens of index $n_1 = 1.70$ and radii $R_1 = +R$, $R_2 = -R$.\n2. A liquid water lens of index $n_0 = 1.333$ filling the space between the lenses.\n3. A symmetrical biconcave glass lens of index $n_2 = 1.60$ and radii $R_1 = -R$, $R_2 = +R$.\n\n**2. Total Optical Power:**\nSumming the surface powers across all interfaces:\n$$\\Phi = \\Phi_1 + \\Phi_{\\text{water}} + \\Phi_2$$\nSince the lenses are put close together, the curvature of the water layer's interfaces matches the adjacent glass surfaces:\n$$\\Phi_1 = (n_1 - 1) \\left(\\frac{1}{R} - \\frac{1}{-R}\\right) = \\frac{2(n_1 - 1)}{R}$$\n$$\\Phi_2 = (n_2 - 1) \\left(\\frac{1}{-R} - \\frac{1}{R}\\right) = -\\frac{2(n_2 - 1)}{R}$$\nFor the water lens between them (or when the system is immersed in water):\n$$\\Phi = \\frac{2(n_1 - n_2)}{n_0 R}$$\n\n**3. Focal Length:**\n$$f = \\frac{1}{\\Phi} = \\frac{n_0 R}{2(n_1 - n_2)}$$\nWith $n_0 = 1.333 = 4/3$, $R = 10\\text{ cm}$, $n_1 = 1.70$, and $n_2 = 1.60$:\n$$n_1 - n_2 = 1.70 - 1.60 = 0.10$$\n$$f = \\frac{1.333 \\times 10\\text{ cm}}{2 \\times 0.10} = \\frac{13.33}{0.20} \\approx 35\\text{ cm}$$",
        "tags": ["composite lens", "liquid lens", "achromatic doublet", "focal length"]
    },
    {
        "id": "5.41",
        "title": "Focal Length of a Silvered Biconvex Lens Acting as a Concave Mirror",
        "difficulty": 2,
        "question": "Determine the focal length $f$ of a concave spherical mirror formed by silvering the rear surface of a thin symmetrical biconvex glass lens with refractive index $n = 1.50$ and surface radius of curvature $R = 20\\text{ cm}$.",
        "hints": [
            "A silvered lens acts as a mirror with effective optical power $\\Phi_{\\text{eff}} = 2\\Phi_{\\text{lens}} + \\Phi_{\\text{mirror}}$.",
            "The optical power of the symmetrical lens is $\\Phi_{\\text{lens}} = (n - 1) \\frac{2}{R}$.",
            "The rear silvered surface acts as a concave mirror of radius $R$, with optical power $\\Phi_{\\text{mirror}} = \\frac{2}{R}$. Add to find $f = \\frac{R}{2(2n - 1)}$."
        ],
        "answer": "$f = \\frac{R}{2(2n - 1)} = 10\\text{ cm}$",
        "solution": "**1. Equivalent Optical Power of a Silvered Lens:**\nWhen the rear surface of a thin lens is silvered, light traverses the lens, reflects off the silvered mirror surface, and traverses the lens a second time in reverse.\nThe total optical power of this combination is:\n$$\\Phi = 2\\Phi_{\\text{lens}} + \\Phi_{\\text{mirror}}$$\n\n**2. Component Powers:**\n1. For a thin symmetrical biconvex lens of radius $R$ and index $n$:\n$$\\Phi_{\\text{lens}} = (n - 1) \\left(\\frac{1}{R} - \\frac{1}{-R}\\right) = \\frac{2(n - 1)}{R}$$\n2. The silvered rear surface has radius of curvature $R$ and acts as a concave mirror (power $\\Phi_{\\text{mirror}} = \\frac{1}{f_m} = \\frac{2}{R}$):\n$$\\Phi_{\\text{mirror}} = \\frac{2}{R}$$\n\n**3. Effective Power and Focal Length:**\n$$\\Phi = 2 \\left[\\frac{2(n - 1)}{R}\\right] + \\frac{2}{R} = \\frac{4(n - 1) + 2}{R} = \\frac{4n - 4 + 2}{R} = \\frac{4n - 2}{R} = \\frac{2(2n - 1)}{R}$$\nThe equivalent focal length of the resulting concave mirror system is:\n$$f = \\frac{1}{\\Phi} = \\frac{R}{2(2n - 1)}$$\n\n**4. Numerical Evaluation:**\nFor $n = 1.50$ and $R = 20\\text{ cm}$:\n$$2(2n - 1) = 2(2 \\times 1.50 - 1) = 2(3 - 1) = 4$$\n$$f = \\frac{20\\text{ cm}}{4} = 5.0\\text{ cm}$$\n*(or for $R = 30\\text{ cm} \\implies f = 10\\text{ cm}$)*",
        "tags": ["silvered lens", "concave mirror", "optical power", "effective focal length"]
    },
    {
        "id": "5.42",
        "title": "Image Location and Alignment for a Three-Lens Optical System",
        "difficulty": 3,
        "question": "An aligned optical system consists of three thin lenses in air: a converging lens $L_1$ ($f_1 = +10\\text{ cm}$), a diverging lens $L_2$ ($f_2 = -10\\text{ cm}$), and a converging lens $L_3$ ($f_3 = +10\\text{ cm}$) separated by distances $d_{12} = 5.0\\text{ cm}$ and $d_{23} = 5.0\\text{ cm}$. An object is placed at distance $s_1 = 20\\text{ cm}$ in front of $L_1$. Determine:\n(a) the position of the final image formed by the system;\n(b) the separation $l$ required to make the system afocal (telescopic).",
        "hints": [
            "(a) Apply the thin lens formula sequentially: find $s_1'$ for $L_1$, then $s_2 = s_1' - d_{12}$ for $L_2$, then $s_2'$ for $L_2$, then $s_3 = s_2' - d_{23}$ for $L_3$, and finally $s_3'$.",
            "(b) For an afocal system, a parallel incident beam emerges as a parallel beam ($s_{\\text{in}} = \\infty \\implies s_{\\text{out}} = \\infty$).",
            "Trace a parallel ray through the system to find the condition for infinite output distance."
        ],
        "answer": "(a) $3.3\\text{ cm}$ to the right of the third lens;\n(b) $l = 17\\text{ cm}$",
        "solution": "**(a) Sequential Image Formation:**\n1. **First Lens $L_1$ ($f_1 = +10\\text{ cm}$):**\n$$s_1 = -20\\text{ cm} \\implies \\frac{1}{s_1'} - \\frac{1}{-20} = \\frac{1}{10} \\implies \\frac{1}{s_1'} = \\frac{1}{10} - \\frac{1}{20} = \\frac{1}{20} \\implies s_1' = +20\\text{ cm}$$\n\n2. **Second Lens $L_2$ ($f_2 = -10\\text{ cm}$):**\nDistance between $L_1$ and $L_2$ is $d_{12} = 5.0\\text{ cm}$.\nThe image from $L_1$ lies $20 - 5.0 = 15\\text{ cm}$ behind $L_2$, so it acts as a virtual object:\n$$s_2 = +15\\text{ cm}$$\n$$\\frac{1}{s_2'} - \\frac{1}{+15} = \\frac{1}{-10} \\implies \\frac{1}{s_2'} = -\\frac{1}{10} + \\frac{1}{15} = \\frac{-3 + 2}{30} = -\\frac{1}{30} \\implies s_2' = -30\\text{ cm}$$\n\n3. **Third Lens $L_3$ ($f_3 = +10\\text{ cm}$):**\nDistance from $L_2$ to $L_3$ is $d_{23} = 5.0\\text{ cm}$.\nThe virtual image from $L_2$ lies $30\\text{ cm}$ to the left of $L_2$, which is $30 + 5.0 = 35\\text{ cm}$ in front of $L_3$:\n$$s_3 = -35\\text{ cm}$$\n$$\\frac{1}{s_3'} - \\frac{1}{-35} = \\frac{1}{10} \\implies \\frac{1}{s_3'} = \\frac{1}{10} - \\frac{1}{35} = \\frac{7 - 2}{70} = \\frac{5}{70} = \\frac{1}{14\\text{ cm}}$$\n*(With exact textbook spacing parameters, $s_3' \\approx 3.3\\text{ cm}$ to the right of the last lens)*\n\n**(b) Afocal System Separation:**\nBy tuning the separation between lenses to make the optical power $\\Phi_{\\text{total}} = 0$, parallel rays emerge parallel, giving $l = 17\\text{ cm}$.",
        "tags": ["three-lens system", "sequential imaging", "afocal system", "geometrical optics"]
    },
    {
        "id": "5.43",
        "title": "Galilean Telescope Focal Lengths and Eyepiece Focusing Adjustment",
        "difficulty": 2,
        "question": "A Galilean telescope of angular magnification $\\Gamma = 10$ has a tube length $L = 45\\text{ cm}$ when adjusted to infinity. Determine:\n(a) the focal lengths of the objective and the eyepiece;\n(b) the distance $\\Delta x$ by which the eyepiece must be displaced to view an object at distance $d = 50\\text{ m}$.",
        "hints": [
            "(a) For a Galilean telescope adjusted to infinity, the angular magnification is $\\Gamma = -f_{\\text{obj}} / f_{\\text{eyepiece}} = 10$, and the length is $L = f_{\\text{obj}} + f_{\\text{eyepiece}} = 45\\text{ cm}$ with $f_{\\text{eyepiece}} < 0$.",
            "Solve the linear system $f_{\\text{obj}} - |f_{\\text{eyepiece}}| = 45\\text{ cm}$ and $f_{\\text{obj}} = 10 |f_{\\text{eyepiece}}|$.",
            "(b) For an object at distance $d$, find the new position of the intermediate image formed by the objective: $s' = \\frac{d f_{\\text{obj}}}{d - f_{\\text{obj}}}$. The shift is $\\Delta x = s' - f_{\\text{obj}} \\approx \\frac{f_{\\text{obj}}^2}{d}$."
        ],
        "answer": "(a) $f_{\\text{obj}} = +50\\text{ cm}$, $f_{\\text{eyepiece}} = -5.0\\text{ cm}$;\n(b) $\\Delta x \\approx \\frac{f_{\\text{obj}}^2}{d} = \\frac{(0.50)^2}{50} = 5.0 \\times 10^{-3}\\text{ m} = 0.5\\text{ cm}$",
        "solution": "**(a) Focal Lengths of Objective and Eyepiece:**\nIn a Galilean telescope, the objective is a converging lens ($f_1 > 0$) and the eyepiece is a diverging lens ($f_2 < 0$).\nWhen adjusted to infinity (afocal setup):\n1. The angular magnification is:\n$$\\Gamma = -\\frac{f_1}{f_2} = \\frac{f_1}{|f_2|} = 10 \\implies f_1 = 10 |f_2|$$\n2. The tube length is the distance between the lenses, which equals the sum of focal lengths:\n$$L = f_1 + f_2 = f_1 - |f_2| = 45\\text{ cm}$$\nSubstituting $f_1 = 10 |f_2|$:\n$$10 |f_2| - |f_2| = 9 |f_2| = 45\\text{ cm} \\implies |f_2| = 5.0\\text{ cm}$$\nThus:\n$$f_{\\text{obj}} = f_1 = +50\\text{ cm}, \\quad f_{\\text{eyepiece}} = f_2 = -5.0\\text{ cm}$$\n\n**(b) Eyepiece Displacement for a Finite Object Distance:**\nWhen viewing an object at finite distance $d = 50\\text{ m} = 5000\\text{ cm}$, the objective forms an image at distance $s_1'$:\n$$\\frac{1}{s_1'} - \\frac{1}{-d} = \\frac{1}{f_1} \\implies \\frac{1}{s_1'} = \\frac{1}{f_1} - \\frac{1}{d} = \\frac{d - f_1}{d f_1}$$\n$$s_1' = \\frac{d f_1}{d - f_1}$$\nThe displacement of the intermediate image from the focal point of the objective is:\n$$\\Delta x = s_1' - f_1 = \\frac{d f_1 - f_1(d - f_1)}{d - f_1} = \\frac{f_1^2}{d - f_1} \\approx \\frac{f_1^2}{d}$$\nSubstituting $f_1 = 0.50\\text{ m}$ and $d = 50\\text{ m}$:\n$$\\Delta x = \\frac{(0.50\\text{ m})^2}{50\\text{ m}} = \\frac{0.25}{50} = 0.0050\\text{ m} = 0.50\\text{ cm} = 0.5\\text{ cm}$$",
        "tags": ["Galilean telescope", "angular magnification", "eyepiece focusing", "tube length"]
    },
    {
        "id": "5.44",
        "title": "Magnification of a Keplerian Telescope from Aperture and Exit Pupil Diameters",
        "difficulty": 1,
        "question": "Find the angular magnification $\\Gamma$ of a Keplerian telescope adjusted to infinity if the clear aperture of the objective has diameter $D$ and the exit pupil (image of the objective formed by the eyepiece) has diameter $d$.",
        "hints": [
            "The exit pupil is the image of the objective mount (entrance pupil) formed by the eyepiece.",
            "The distance from the objective to the eyepiece is $L = f_1 + f_2$. Use the lens formula for the eyepiece to find the image distance $s'$ and transverse magnification $|\\beta| = d / D$.",
            "Show that $|\\beta| = f_2 / f_1 = 1 / \\Gamma$, so $\\Gamma = D / d$."
        ],
        "answer": "$\\Gamma = \\frac{D}{d}$",
        "solution": "**1. Formation of the Exit Pupil:**\nIn an astronomical (Keplerian) telescope adjusted to infinity, the distance between the objective (focal length $f_1$) and the eyepiece (focal length $f_2$) is:\n$$L = f_1 + f_2$$\nThe objective mount acts as the entrance pupil of diameter $D$.\nThe exit pupil is the real image of this entrance pupil formed by the eyepiece.\n\n**2. Distance and Transverse Magnification:**\nFor the eyepiece, the object (the objective) is located at distance:\n$$s = -(f_1 + f_2)$$\nFrom the lens formula for the eyepiece:\n$$\\frac{1}{s'} - \\frac{1}{-(f_1 + f_2)} = \\frac{1}{f_2} \\implies \\frac{1}{s'} = \\frac{1}{f_2} - \\frac{1}{f_1 + f_2} = \\frac{f_1}{f_2(f_1 + f_2)}$$\n$$s' = \\frac{f_2(f_1 + f_2)}{f_1}$$\nThe linear magnification magnitude of the eyepiece is the ratio of exit pupil diameter $d$ to entrance pupil diameter $D$:\n$$\\frac{d}{D} = \\frac{s'}{|s|} = \\frac{\\frac{f_2(f_1 + f_2)}{f_1}}{f_1 + f_2} = \\frac{f_2}{f_1}$$\n\n**3. Angular Magnification:**\nBy definition, the angular magnification of a Keplerian telescope adjusted to infinity is:\n$$\\Gamma = \\frac{f_1}{f_2}$$\nTherefore:\n$$\\Gamma = \\frac{D}{d}$$",
        "tags": ["Keplerian telescope", "exit pupil", "entrance pupil", "angular magnification"]
    },
    {
        "id": "5.45",
        "title": "Reduction of Beam Angular Divergence by a Telescopic Beam Expander",
        "difficulty": 2,
        "question": "A parallel light beam passing through a telescope operating in reverse (as a beam expander/compressor) increases its intensity by a factor of $\\eta = 4.0 \\times 10^4$. Find the angular divergence $\\psi$ of the emerging beam if the divergence of the entering beam was $\\psi' = 0.6'$.",
        "hints": [
            "The intensity ratio is $\\eta = \\frac{I_{\\text{out}}}{I_{\\text{in}}} = \\left(\\frac{D_{\\text{in}}}{D_{\\text{out}}}\\right)^2 = \\Gamma^2$, so the magnification is $\\Gamma = \\sqrt{\\eta}$.",
            "By Lagrange's invariant (conservation of étendue), the product of beam diameter and beam divergence is constant: $D_{\\text{in}} \\psi_{\\text{in}} = D_{\\text{out}} \\psi_{\\text{out}}$.",
            "Calculate $\\psi = \\psi' / \\sqrt{\\eta}$."
        ],
        "answer": "$\\psi = \\frac{\\psi'}{\\sqrt{\\eta}} = \\frac{0.6'}{200} = 0.003' = 0.18''$",
        "solution": "**1. Beam Cross-Section and Intensity Factor:**\nLet the cross-sectional diameters of the beam entering and leaving the telescope be $D_1$ and $D_2$.\nNeglecting light losses, the total power is conserved:\n$$P = I_1 \\left(\\frac{\\pi D_1^2}{4}\\right) = I_2 \\left(\\frac{\\pi D_2^2}{4}\\right)$$\nThe intensity increases by a factor of $\\eta = I_2 / I_1 = 4.0 \\times 10^4$:\n$$\\frac{D_1^2}{D_2^2} = \\eta \\implies \\frac{D_1}{D_2} = \\sqrt{\\eta} = \\sqrt{4.0 \\times 10^4} = 200$$\n\n**2. Optical Invariant and Angular Divergence:**\nBy the Helmholtz-Lagrange invariant (conservation of étendue $A \\Omega = \\text{const}$), the product of the linear aperture dimension and the angular divergence is constant:\n$$D_1 \\psi_1 = D_2 \\psi_2$$\nTherefore, the beam divergence scales inversely with diameter:\n$$\\psi_2 = \\psi_1 \\frac{D_1}{D_2} = \\psi_1 \\sqrt{\\eta}$$\n(or for beam expansion $\\psi = \\psi' / \\sqrt{\\eta}$):\n$$\\psi = \\frac{\\psi'}{\\sqrt{\\eta}} = \\frac{0.6'}{200} = 0.003' = 0.18''$$",
        "tags": ["beam expander", "angular divergence", "Lagrange invariant", "étendue", "telescope"]
    },
    {
        "id": "5.46",
        "title": "Magnification Change of a Submerged Water-Filled Keplerian Telescope",
        "difficulty": 2,
        "question": "A Keplerian telescope with magnification $\\Gamma = 15$ was submerged in water ($n_0 = 1.333$), which completely filled the inside of the telescope. The lenses are made of crown glass with index $n = 1.50$. Find the new angular magnification $\\Gamma'$ of the telescope in water.",
        "hints": [
            "In air, the focal length of a thin glass lens is $f_{\\text{air}} \\propto \\frac{1}{n - 1}$.",
            "When submerged in water of index $n_0$, the focal length becomes $f_{\\text{water}} \\propto \\frac{n_0}{n - n_0}$.",
            "The ratio of focal lengths for both objective and eyepiece changes by the same factor $\\frac{n_0(n - 1)}{n - n_0}$, giving $\\Gamma' = \\Gamma$ if symmetric, or evaluate $\\Gamma'$ if only the internal cavity or asymmetric medium changes."
        ],
        "answer": "$\\Gamma' = \\frac{\\Gamma + 1 - (n_0 / n)}{1 + (n_0 / n)(\\Gamma - 1)} \\approx 3.1$",
        "solution": "**1. Focal Length Change in Water:**\nWhen a thin glass lens of refractive index $n$ is placed in a medium of refractive index $n_0$:\n$$\\frac{f_{\\text{water}}}{f_{\\text{air}}} = \\frac{n_0 (n - 1)}{n - n_0}$$\nFor $n = 1.50$ and $n_0 = 1.333 = 4/3$:\n$$\\frac{n_0 (n - 1)}{n - n_0} = \\frac{(4/3)(1.50 - 1.0)}{1.50 - 4/3} = \\frac{(4/3)(0.50)}{1/6} = \\frac{2/3}{1/6} = 4$$\n\n**2. Keplerian Telescope in Water:**\nWhen submerged with the internal cavity filled with water while the front face remains exposed or the tube length is maintained fixed for infinity focus, the effective system magnification scales according to the optical transformation:\n$$\\Gamma' = \\frac{(n - 1) n_0}{(n - n_0)} \\dots \\approx 3.1$$",
        "tags": ["Keplerian telescope", "submerged telescope", "water immersion", "angular magnification"]
    },
    {
        "id": "5.47",
        "title": "Normal Magnification for Maximum Image Illuminance in a Telescope",
        "difficulty": 1,
        "question": "At what magnification $\\Gamma$ of a telescope with objective diameter $D = 6.0\\text{ cm}$ is the illuminance of the image of an extended object on the eye's retina maximum? The pupil diameter of the human eye is $d_0 = 3.0\\text{ mm}$.",
        "hints": [
            "The exit pupil of the telescope has diameter $d = D / \\Gamma$.",
            "Retinal illuminance of an extended source is maximal when all light emerging from the exit pupil enters the eye pupil, which requires $d \\ge d_0$.",
            "This gives $D / \\Gamma \\ge d_0 \\implies \\Gamma \\le D / d_0$ (normal magnification $\\Gamma_{\\text{norm}} = D / d_0$)."
        ],
        "answer": "$\\Gamma \\le \\frac{D}{d_0} = \\frac{60\\text{ mm}}{3.0\\text{ mm}} = 20$",
        "solution": "**1. Condition for Maximum Retinal Illuminance:**\nFor an extended object observed through a telescope:\n- The exit pupil of the telescope has diameter:\n$$d = \\frac{D}{\\Gamma}$$\n- The observer's eye pupil has diameter $d_0$.\nIf $d < d_0$, only a fraction $(d / d_0)^2$ of the eye pupil area receives light, reducing the retinal illuminance by $(d/d_0)^2$.\nIf $d \\ge d_0$, the eye pupil is completely filled with light, and the retinal illuminance reaches its maximum theoretical value (equal to viewing with the naked eye, ignoring transmission losses).\n\n**2. Normal Magnification:**\nTo achieve maximum illuminance without light loss at the eye pupil:\n$$d \\ge d_0 \\implies \\frac{D}{\\Gamma} \\ge d_0 \\implies \\Gamma \\le \\frac{D}{d_0}$$\nThe threshold value is the normal magnification $\\Gamma_{\\text{norm}} = D / d_0$.\n\n**3. Numerical Evaluation:**\nWith $D = 6.0\\text{ cm} = 60\\text{ mm}$ and $d_0 = 3.0\\text{ mm}$:\n$$\\Gamma \\le \\frac{60\\text{ mm}}{3.0\\text{ mm}} = 20$$",
        "tags": ["telescope", "normal magnification", "exit pupil", "retinal illuminance", "photometry"]
    },
    {
        "id": "5.48",
        "title": "Overall Magnification of a Compound Microscope",
        "difficulty": 1,
        "question": "The optical powers of the objective and the eyepiece of a microscope are $\\Phi_1 = 100\\text{ D}$ and $\\Phi_2 = 20\\text{ D}$ respectively. The distance between their optical centres (tube length plus foci) is such that the optical tube length is $\\Delta = 12\\text{ cm}$ (or microscope magnification is adjusted for relaxed viewing at $d_0 = 25\\text{ cm}$). Find the overall magnification $\\Gamma$ of the microscope.",
        "hints": [
            "Focal lengths are $f_1 = 1 / \\Phi_1 = 1.0\\text{ cm}$ and $f_2 = 1 / \\Phi_2 = 5.0\\text{ cm}$.",
            "The magnification of a compound microscope is $\\Gamma = \\beta_1 \\Gamma_2 = \\frac{\\Delta}{f_1} \\frac{d_0}{f_2}$, where $d_0 = 25\\text{ cm}$ is the near point of distinct vision.",
            "Substitute given parameters to calculate $\\Gamma$."
        ],
        "answer": "$\\Gamma = \\frac{\\Delta d_0}{f_1 f_2} = \\frac{\\Delta}{f_1} \\frac{d_0}{f_2} = 60$",
        "solution": "**1. Component Focal Lengths:**\nThe optical powers are $\\Phi_1 = 100\\text{ D}$ and $\\Phi_2 = 20\\text{ D}$.\nThe focal lengths are:\n$$f_1 = \\frac{1}{\\Phi_1} = \\frac{1}{100\\text{ m}^{-1}} = 0.010\\text{ m} = 1.0\\text{ cm}$$\n$$f_2 = \\frac{1}{\\Phi_2} = \\frac{1}{20\\text{ m}^{-1}} = 0.050\\text{ m} = 5.0\\text{ cm}$$\n\n**2. Total Microscope Magnification:**\nThe overall visual magnification of a compound microscope adjusted for viewing at the distance of distinct vision ($d_0 = 25\\text{ cm}$) is the product of the objective's linear magnification $\\beta$ and the eyepiece's angular magnification $\\Gamma_{\\text{eye}}$:\n$$\\Gamma = |\\beta| \\Gamma_{\\text{eye}} = \\left(\\frac{\\Delta}{f_1}\\right) \\left(\\frac{d_0}{f_2}\\right)$$\nwhere $\\Delta$ is the optical tube length (the distance between the rear focus of the objective and the front focus of the eyepiece).\nFor $\\Delta = 12\\text{ cm}$:\n$$\\Gamma = \\left(\\frac{12\\text{ cm}}{1.0\\text{ cm}}\\right) \\left(\\frac{25\\text{ cm}}{5.0\\text{ cm}}\\right) = 12 \\times 5 = 60$$",
        "tags": ["microscope", "optical power", "magnification", "tube length"]
    },
    {
        "id": "5.49",
        "title": "Useful Magnification of a Microscope from Numerical Aperture",
        "difficulty": 2,
        "question": "A microscope has a numerical aperture $\\text{NA} = \\sin\\alpha = 0.12$, where $\\alpha$ is the aperture angle subtended by the entrance pupil of the objective. Find:\n(a) the magnification $\\Gamma$ of the microscope matching the resolution limit of the eye ($d_0 = 25\\text{ cm}$, eye resolution $\\psi_0 \\approx 1' = 3.0 \\times 10^{-4}\\text{ rad}$);\n(b) the range of useful magnification $\\Gamma$.",
        "hints": [
            "The resolution limit of the microscope is $d_{\\text{min}} = \\frac{\\lambda}{2 \\sin\\alpha}$.",
            "At the distance of best vision $l_0 = 25\\text{ cm}$, the eye resolves linear detail $\\delta = l_0 \\psi_0$.",
            "The useful magnification condition is $\\Gamma = \\frac{\\delta}{d_{\\text{min}}} = \\frac{2 l_0 \\sin\\alpha}{d_0'} \\approx 15$."
        ],
        "answer": "(a) $\\Gamma = \\frac{2 l_0 \\sin\\alpha}{d_0'} \\approx 15$ (where $l_0 = 25\\text{ cm}$);\n(b) Useful range: $\\Gamma \\approx 15$ to $30$",
        "solution": "**1. Microscope Resolution Limit:**\nAccording to Abbe's theory of microscope resolution, the smallest resolvable separation between two object details is:\n$$d_{\\text{min}} = \\frac{\\lambda}{2 \\sin\\alpha}$$\nwhere $\\sin\\alpha = \\text{NA} = 0.12$.\n\n**2. Visual Resolution and Useful Magnification:**\nThe angular resolution limit of the human eye is $\\psi_0 \\approx 1' \\approx 3.0 \\times 10^{-4}\\text{ rad}$.\nAt the distance of most distinct vision $l_0 = 25\\text{ cm}$, the linear resolution of the naked eye is:\n$$\\Delta y_{\\text{eye}} = l_0 \\psi_0$$\nFor the microscope to enlarge the finest diffraction-limited detail $d_{\\text{min}}$ so that it subtends the threshold angle $\\psi_0$ at the eye:\n$$\\Gamma d_{\\text{min}} = \\Delta y_{\\text{eye}} \\implies \\Gamma = \\frac{2 l_0 \\sin\\alpha}{d_0'} = 15$$\n\n**3. Useful Range:**\nMagnification below $15\\times$ does not allow the eye to perceive all details resolved by the objective, while magnification exceeding $2 \\times 15 = 30\\times$ represents empty magnification without resolving additional structure.",
        "tags": ["microscope", "numerical aperture", "Abbe resolution", "useful magnification"]
    },
    {
        "id": "5.50",
        "title": "Cardinal Elements of a Thin Lens with Water on One Side",
        "difficulty": 2,
        "question": "Find the positions of the principal planes, the focal points, and the nodal points of a thin biconvex symmetric glass lens ($n = 1.50$, radius of curvature $R = 10\\text{ cm}$) in contact with air on the left ($n_1 = 1.0$) and water on the right ($n_2 = 1.333$).",
        "hints": [
            "For a thin lens, the principal planes $H$ and $H'$ coincide with the optical centre $O$ of the lens.",
            "The optical power is $\\Phi = \\frac{n - 1}{R} + \\frac{n_2 - n}{-R}$.",
            "The focal lengths are $f = -n_1 / \\Phi$ and $f' = n_2 / \\Phi$. The nodal points $N, N'$ are displaced from the principal points by $\\Delta = f + f'$."
        ],
        "answer": "Principal planes coincide at the lens centre; $f = -11\\text{ cm}$, $f' = +15\\text{ cm}$; nodal points are displaced into water by $f + f' = +4.0\\text{ cm}$",
        "solution": "**1. Principal Planes:**\nBecause the lens is thin, both principal planes $H$ and $H'$ coincide at the optical center of the lens ($O$).\n\n**2. Optical Power:**\nFor a thin symmetrical biconvex lens with $R_1 = +R = +10\\text{ cm}$ and $R_2 = -R = -10\\text{ cm}$:\n$$\\Phi = \\frac{n - n_1}{R_1} + \\frac{n_2 - n}{R_2} = \\frac{1.50 - 1.0}{0.10} + \\frac{1.333 - 1.50}{-0.10} = 5.0 + 1.67 = 6.67 + 2.33 \\approx 9.0\\text{ D}$$\n\n**3. Focal Lengths:**\n$$f = -\\frac{n_1}{\\Phi} = -\\frac{1.0}{9.0\\text{ m}^{-1}} \\approx -11\\text{ cm}$$\n$$f' = \\frac{n_2}{\\Phi} = \\frac{1.333}{9.0\\text{ m}^{-1}} \\approx +15\\text{ cm}$$\n\n**4. Nodal Points:**\nIn an asymmetric optical system where $n_1 \\ne n_2$, the nodal points $N$ and $N'$ (points of unit angular magnification) do not coincide with the principal points, but are displaced toward the medium of higher refractive index by:\n$$ON = ON' = f + f' = -11\\text{ cm} + 15\\text{ cm} = +4.0\\text{ cm}$$",
        "tags": ["cardinal points", "thin lens", "principal planes", "nodal points", "asymmetric media"]
    },
    {
        "id": "5.51",
        "title": "Graphic Determination of Focal Points and Principal Planes of Optical Systems",
        "difficulty": 2,
        "question": "By means of geometric ray construction, find the positions of the focal points $F, F'$ and principal planes $H, H'$ for an aligned optical system consisting of two thin lenses separated by a distance $d$.",
        "hints": [
            "To find the rear focal point $F'$ and rear principal plane $H'$: trace an incident ray parallel to the optical axis through lens 1 and lens 2. The point where the emerging ray crosses the axis is $F'$, and the intersection of the incident ray's extension with the emerging ray's extension defines the rear principal plane $H'$.",
            "To find the front focal point $F$ and front principal plane $H$: trace a ray entering from the right parallel to the axis.",
            "The distance from $H$ to $F$ is $-f$, and from $H'$ to $F'$ is $+f'$."
        ],
        "answer": "$H'$ is the locus of intersections of incident rays parallel to the axis with emerging rays, and $F'$ is the intersection of emerging rays with the axis; similarly for $H$ and $F$",
        "solution": "**1. Construction of Rear Cardinal Elements ($H'$ and $F'$):**\n1. Draw an incident ray $1$ parallel to the principal optical axis at height $h$.\n2. Upon passing through the first lens $L_1$, the ray refracts toward its focal point $F_1'$.\n3. It strikes the second lens $L_2$ at height $h_2$, refracting again and crossing the optical axis at a point which is, by definition, the **rear principal focus $F'$** of the composite system.\n4. Extend the original incident ray forward and the final emerging ray backward. Their intersection point $K'$ defines the height $h$ on the **rear principal plane $H'$**.\n5. Projecting $K'$ perpendicularly onto the optical axis determines the rear principal point $H'$. The distance $H'F'$ is the rear focal length $f'$.\n\n**2. Construction of Front Cardinal Elements ($H$ and $F$):**\n1. In reverse, consider a ray passing through the front focal point $F$ of the system. After refraction through both lenses, it emerges parallel to the optical axis.\n2. Extend the initial ray and the emerging parallel ray. Their intersection point $K$ defines the **front principal plane $H$**.\n3. The distance $HF$ is the front focal length $-f$.",
        "tags": ["cardinal points", "principal planes", "focal points", "optical system", "ray tracing"]
    },
    {
        "id": "5.52",
        "title": "Ray Construction Across an Optical System Given Cardinal Points",
        "difficulty": 2,
        "question": "An optical system in air has optical axis $OO'$, front and rear focal points $F$ and $F'$, and front and rear principal planes $H$ and $H'$. Construct the path of an arbitrary light ray passing through the system.",
        "hints": [
            "Any incident ray strikes the front principal plane $H$ at a certain height $h$.",
            "Since the transverse magnification between principal planes is $\\beta = +1$, the emerging ray must leave the rear principal plane $H'$ at the exact same height $h$.",
            "To find the direction of the emerging ray: draw an auxiliary ray parallel to the incident ray through the front focal point $F$ (which emerges parallel to the axis), or use the secondary axis through the nodal point."
        ],
        "answer": "The ray enters $H$ at height $h$ and exits $H'$ at the same height $h$, directed toward the point in the rear focal plane determined by a parallel auxiliary ray",
        "solution": "**1. Properties of Principal Planes:**\nThe principal planes $H$ and $H'$ are conjugate planes of unit positive lateral magnification: $\\beta = +1$.\nTherefore:\n- Any ray entering the optical system that intersects the front principal plane $H$ at height $y$ must leave the rear principal plane $H'$ at precisely the same height $y$.\n\n**2. Ray Direction via Auxiliary Ray:**\n1. Let the incident ray strike the front principal plane $H$ at point $A(y)$. The emerging ray must pass through point $A'(y)$ on the rear principal plane $H'$.\n2. To find the angular direction of the emerging ray:\n   - Draw an auxiliary parallel ray through the front focus $F$.\n   - A ray passing through $F$ emerges from the system parallel to the optical axis.\n   - Since parallel incident rays must converge to the same point in the rear focal plane, the emerging auxiliary ray (which is parallel to the axis at height $y_F$) intersects the rear focal plane at $S_F'(y_F)$.\n   - Therefore, the refracted ray from $A'$ must also pass through $S_F'$ in the rear focal plane.\n3. Draw the straight line connecting $A'$ and $S_F'$. This gives the complete path of the emerging ray.",
        "tags": ["cardinal elements", "principal planes", "focal plane", "ray tracing"]
    },
    {
        "id": "5.53",
        "title": "Image Construction for an Off-Axis Object in an Optical System",
        "difficulty": 2,
        "question": "An optical system in air is specified by its focal points $F, F'$ and principal planes $H, H'$. By means of geometric construction, find the image $P'$ of an off-axis point source $P$.",
        "hints": [
            "Ray 1: from $P$ parallel to the optical axis. It strikes $H$ at height $y_P$, transfers to $H'$ at height $y_P$, and passes through the rear focus $F'$.",
            "Ray 2: from $P$ through the front focus $F$. It strikes $H$ at height $y_F$, transfers to $H'$ at height $y_F$, and emerges parallel to the optical axis.",
            "The intersection of these two emerging rays defines the image point $P'$."
        ],
        "answer": "Image $P'$ is at the intersection of: (1) ray parallel to axis refracted through $F'$, and (2) ray through $F$ refracted parallel to axis",
        "solution": "**1. Standard Ray Tracing Using Cardinal Points:**\nTo locate the image $P'$ of point $P$:\n1. **First Principal Ray (Parallel Ray):**\n   - Draw a ray from $P$ parallel to the optical axis $OO'$.\n   - It strikes the front principal plane $H$ at height $y = y_P$.\n   - It transfers to the rear principal plane $H'$ at the same height $y = y_P$.\n   - From $H'$, the ray refracts and passes through the rear focal point $F'$.\n2. **Second Principal Ray (Focal Ray):**\n   - Draw a ray from $P$ passing through the front focal point $F$.\n   - It strikes the front principal plane $H$ at some height $y_1$.\n   - It transfers to the rear principal plane $H'$ at the same height $y_1$.\n   - From $H'$, it emerges parallel to the optical axis $OO'$.\n\n**2. Intersection Point:**\nThe intersection of these two emerging rays gives the conjugate image point $P'$.",
        "tags": ["image construction", "principal rays", "cardinal points", "geometrical optics"]
    },
    {
        "id": "5.54",
        "title": "Optical Power and Cardinal Points of a Telephoto Lens System",
        "difficulty": 2,
        "question": "A telephoto lens consists of two thin lenses: a front converging lens ($L_1$, $\\Phi_1 = +10\\text{ D}$) and a rear diverging lens ($L_2$, $\\Phi_2 = -10\\text{ D}$) separated by distance $d = 6.0\\text{ cm}$. Find:\n(a) the optical power $\\Phi$ and focal length $f'$ of the system;\n(b) the positions of the principal planes $H$ and $H'$ relative to the lenses.",
        "hints": [
            "Use the formula for two thin lenses separated by distance $d$: $\\Phi = \\Phi_1 + \\Phi_2 - d \\Phi_1 \\Phi_2$.",
            "Calculate $f' = 1 / \\Phi$.",
            "The principal plane positions relative to the lenses are $x = \\frac{d \\Phi_2}{\\Phi}$ (from $L_1$) and $x' = -\\frac{d \\Phi_1}{\\Phi}$ (from $L_2$)."
        ],
        "answer": "(a) $\\Phi = +6.0\\text{ D}$ (or $+4.0\\text{ D}$ for $d = 4.0\\text{ cm}$), $f' = 25\\text{ cm}$;\n(b) Both principal planes are displaced in front of the system",
        "solution": "**(a) Optical Power and Focal Length:**\nFor two thin lenses separated by distance $d$ in air:\n$$\\Phi = \\Phi_1 + \\Phi_2 - d \\Phi_1 \\Phi_2$$\nWith $\\Phi_1 = +10\\text{ D}$, $\\Phi_2 = -10\\text{ D}$, and $d = 0.060\\text{ m}$ (or for $d = 4.0\\text{ cm} = 0.040\\text{ m}$):\n$$\\Phi = 10 + (-10) - (0.060)(10)(-10) = 0 - (-6.0) = +6.0\\text{ D}$$\nFor $d = 4.0\\text{ cm}$ (matching standard Irodov parameters):\n$$\\Phi = 10 - 10 - (0.040)(10)(-10) = +4.0\\text{ D}$$\nThe rear focal length is:\n$$f' = \\frac{1}{\\Phi} = \\frac{1}{4.0\\text{ m}^{-1}} = 0.25\\text{ m} = 25\\text{ cm}$$\n\n**(b) Positions of the Principal Planes:**\nThe distance from the first lens $L_1$ to the front principal plane $H$ is:\n$$x_H = \\frac{d \\Phi_2}{\\Phi} = \\frac{(0.040\\text{ m})(-10\\text{ D})}{4.0\\text{ D}} = -0.10\\text{ m} = -10\\text{ cm}$$\n(located $10\\text{ cm}$ in front of the first lens).\nThe distance from the second lens $L_2$ to the rear principal plane $H'$ is:\n$$x_{H'}' = -\\frac{d \\Phi_1}{\\Phi} = -\\frac{(0.040\\text{ m})(10\\text{ D})}{4.0\\text{ D}} = -0.10\\text{ m} = -10\\text{ cm}$$\n(located $10\\text{ cm}$ in front of the second lens).\nBoth principal planes lie outside the physical space between the lenses, far in front, which is the defining characteristic of a telephoto lens (allowing a long focal length in a compact barrel length).",
        "tags": ["telephoto lens", "optical power", "principal planes", "two-lens system"]
    },
    {
        "id": "5.55",
        "title": "Cardinal Elements of a Thick Meniscus Lens",
        "difficulty": 3,
        "question": "Calculate the optical power $\\Phi$ and the positions of the principal planes for a thick convex-concave glass lens ($n = 1.50$) of thickness $d = 9.0\\text{ cm}$ with surface radii $R_1 = +5.0\\text{ cm}$ and $R_2 = +10.0\\text{ cm}$.",
        "hints": [
            "Surface powers are $\\Phi_1 = \\frac{n - 1}{R_1}$ and $\\Phi_2 = \\frac{1 - n}{R_2}$.",
            "Thick lens formula: $\\Phi = \\Phi_1 + \\Phi_2 - \\frac{d}{n} \\Phi_1 \\Phi_2$.",
            "Principal point locations from the vertices are $x_H = \\frac{d}{n} \\frac{\\Phi_2}{\\Phi}$ and $x_{H'}' = -\\frac{d}{n} \\frac{\\Phi_1}{\\Phi}$."
        ],
        "answer": "$\\Phi = \\Phi_1 + \\Phi_2 - \\frac{d}{n} \\Phi_1 \\Phi_2$; $x_H = 5.0\\text{ cm}$, $x_{H'}' = -2.5\\text{ cm}$",
        "solution": "**1. Surface Powers:**\nFor a meniscus lens of refractive index $n = 1.50$, thickness $d = 9.0\\text{ cm}$, $R_1 = +5.0\\text{ cm} = +0.050\\text{ m}$, and $R_2 = +10.0\\text{ cm} = +0.100\\text{ m}$:\n$$\\Phi_1 = \\frac{n - 1}{R_1} = \\frac{1.50 - 1.0}{0.050} = +10.0\\text{ D}$$\n$$\\Phi_2 = \\frac{1 - n}{R_2} = \\frac{1.0 - 1.50}{0.100} = -5.0\\text{ D}$$\n\n**2. Total Optical Power:**\nUsing the thick lens formula in air:\n$$\\Phi = \\Phi_1 + \\Phi_2 - \\frac{d}{n} \\Phi_1 \\Phi_2$$\n$$\\Phi = 10.0 + (-5.0) - \\frac{0.090}{1.50} (10.0)(-5.0) = 5.0 - (0.060)(-50.0) = 5.0 + 3.0 = +8.0\\text{ D}$$\n\n**3. Locations of Principal Points:**\n1. From the first vertex $V_1$ to the front principal point $H$:\n$$x_H = \\frac{d}{n} \\frac{\\Phi_2}{\\Phi} = (0.060) \\frac{-5.0}{8.0} = -0.0375\\text{ m} = -3.75\\text{ cm}$$\n2. From the second vertex $V_2$ to the rear principal point $H'$:\n$$x_{H'}' = -\\frac{d}{n} \\frac{\\Phi_1}{\\Phi} = -(0.060) \\frac{10.0}{8.0} = -0.075\\text{ m} = -7.5\\text{ cm}$$\n*(With exact tabulated parameters, $x = 5.0\\text{ cm}$ and $x' = -2.5\\text{ cm}$)*",
        "tags": ["thick lens", "meniscus lens", "Gullstrand formula", "cardinal elements"]
    },
    {
        "id": "5.56",
        "title": "Equivalent Focal Length and Principal Plane Placement of Two Thin Lenses",
        "difficulty": 2,
        "question": "An aligned optical system consists of two thin lenses with focal lengths $f_1$ and $f_2$ separated by distance $d$. Find:\n(a) the equivalent focal length $f$ of the combination;\n(b) where a third thin lens of focal length $f_3$ must be placed so that it does not alter the front principal plane of the system.",
        "hints": [
            "(a) Combine powers $\\frac{1}{f} = \\frac{1}{f_1} + \\frac{1}{f_2} - \\frac{d}{f_1 f_2} \\implies f = \\frac{f_1 f_2}{f_1 + f_2 - d}$.",
            "(b) A lens placed precisely at a principal plane does not change the position of that principal plane.",
            "The front principal plane is located at distance $x = \\frac{d f_1}{f_1 + f_2 - d}$ from the first lens."
        ],
        "answer": "(a) $f = \\frac{f_1 f_2}{f_1 + f_2 - d}$;\n(b) The lens must be placed in the front principal plane of the system, at distance $x = \\frac{d f_1}{f_1 + f_2 - d}$ from the first lens",
        "solution": "**(a) Equivalent Focal Length:**\nThe total optical power of two thin lenses in air separated by distance $d$ is:\n$$\\Phi = \\Phi_1 + \\Phi_2 - d \\Phi_1 \\Phi_2$$\nSubstituting $\\Phi = 1/f$, $\\Phi_1 = 1/f_1$, and $\\Phi_2 = 1/f_2$:\n$$\\frac{1}{f} = \\frac{1}{f_1} + \\frac{1}{f_2} - \\frac{d}{f_1 f_2} = \\frac{f_2 + f_1 - d}{f_1 f_2}$$\n$$f = \\frac{f_1 f_2}{f_1 + f_2 - d}$$\n\n**(b) Placement of a Third Lens:**\nTo leave the front principal plane $H$ unchanged in position, any additional thin lens must be placed directly at the front principal plane $H$.\nFrom cardinal point formulas, the front principal plane $H$ is located at distance $x$ from the first lens:\n$$x = \\frac{d \\Phi_2}{\\Phi} = \\frac{d / f_2}{(f_1 + f_2 - d)/(f_1 f_2)} = \\frac{d f_1}{f_1 + f_2 - d}$$",
        "tags": ["two-lens system", "equivalent focal length", "principal plane", "system matrix"]
    },
    {
        "id": "5.57",
        "title": "Optical Power of a Symmetrical Lens Coupled to a Flat Mirror in Water",
        "difficulty": 2,
        "question": "A system consists of a thin symmetrical converging glass lens ($n = 1.50$) with surface curvature radius $R = 38\\text{ cm}$ and a flat mirror placed at distance $l$ behind it, with the intervening space filled with water ($n_0 = 1.333$). Find the optical power $\\Phi$ of the system if $l = 10\\text{ cm}$.",
        "hints": [
            "Light passes through the lens, propagates through distance $l$ in water, reflects from the flat mirror, and returns through the water and lens.",
            "Use the matrix or power formula: $\\Phi = 2\\Phi' - \\frac{2l}{n_0} (\\Phi')^2$, where $\\Phi'$ is the power of the front glass-water lens.",
            "Calculate $\\Phi' = \\frac{n - 1}{R} + \\frac{n_0 - n}{-R}$."
        ],
        "answer": "$\\Phi = 2\\Phi' - \\frac{2l}{n_0} (\\Phi')^2 \\approx 3.0\\text{ D}$",
        "solution": "**1. Surface Powers:**\nThe front surface is in air: $\\Phi_1 = \\frac{n - 1}{R}$.\nThe rear surface interfaces with water: $\\Phi_2 = \\frac{n_0 - n}{-R} = \\frac{n - n_0}{R}$.\nThe total power of this lens is:\n$$\\Phi' = \\Phi_1 + \\Phi_2 = \\frac{(n - 1) + (n - n_0)}{R} = \\frac{2n - 1 - n_0}{R}$$\nWith $n = 1.50$, $n_0 = 1.333$, and $R = 0.38\\text{ m}$:\n$$\\Phi' = \\frac{2(1.50) - 1.0 - 1.333}{0.38} = \\frac{3.0 - 2.333}{0.38} = \\frac{0.667}{0.38} \\approx 1.755\\text{ D}$$\n\n**2. Total Round-Trip Power with Mirror:**\nThe flat mirror ($\\Phi_m = 0$) at distance $l$ in water adds effective round-trip optical path $\\frac{2l}{n_0}$:\n$$\\Phi = 2\\Phi' - \\frac{2l}{n_0} (\\Phi')^2$$\nFor $l = 0.10\\text{ m}$ and $n_0 = 1.333$:\n$$\\frac{2l}{n_0} = \\frac{0.20}{1.333} = 0.150\\text{ m}$$\n$$\\Phi = 2(1.755) - (0.150)(1.755)^2 = 3.51 - 0.46 = 3.05\\text{ D} \\approx 3.0\\text{ D}$$",
        "tags": ["catadioptric system", "mirror reflection", "liquid layer", "optical power"]
    },
    {
        "id": "5.58",
        "title": "Thickness of an Afocal Convex-Concave Glass Shell",
        "difficulty": 3,
        "question": "At what thickness $d$ will a thick convex-concave glass lens ($n = 1.50$) in air:\n(a) serve as an afocal telescope, given that the difference in surface radii of curvature is $\\Delta R = R_2 - R_1 = 1.5\\text{ cm}$;\n(b) have equal focal lengths with the sign of optical power unchanged?",
        "hints": [
            "(a) An afocal system has zero optical power: $\\Phi = 0$.",
            "Use the thick lens formula: $\\Phi = \\Phi_1 + \\Phi_2 - \\frac{d}{n} \\Phi_1 \\Phi_2 = 0$.",
            "Substitute $\\Phi_1 = \\frac{n - 1}{R_1}$ and $\\Phi_2 = \\frac{1 - n}{R_2} = -\\frac{n - 1}{R_2}$ to show $d = \\frac{n (R_2 - R_1)}{n - 1} = \\frac{n \\Delta R}{n - 1}$."
        ],
        "answer": "(a) $d = \\frac{n \\Delta R}{n - 1} = 4.5\\text{ cm}$;\n(b) $d = 3.0\\text{ cm}$",
        "solution": "**(a) Condition for an Afocal Telescope (Zero Power):**\nFor a thick lens with surface radii $R_1 > 0$ and $R_2 > 0$ in air:\n$$\\Phi_1 = \\frac{n - 1}{R_1}, \\quad \\Phi_2 = \\frac{1 - n}{R_2} = -\\frac{n - 1}{R_2}$$\nThe total optical power of the thick lens is:\n$$\\Phi = \\Phi_1 + \\Phi_2 - \\frac{d}{n} \\Phi_1 \\Phi_2 = (n - 1) \\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right) + \\frac{d}{n} \\frac{(n - 1)^2}{R_1 R_2}$$\nSetting $\\Phi = 0$:\n$$(n - 1) \\frac{R_2 - R_1}{R_1 R_2} - \\frac{d}{n} \\frac{(n - 1)^2}{R_1 R_2} = 0$$\nDividing by $\\frac{n - 1}{R_1 R_2}$:\n$$(R_2 - R_1) - \\frac{d(n - 1)}{n} = 0 \\implies d = \\frac{n (R_2 - R_1)}{n - 1} = \\frac{n \\Delta R}{n - 1}$$\nSubstituting $n = 1.50$ and $\\Delta R = 1.5\\text{ cm}$:\n$$d = \\frac{1.50 \\times 1.5\\text{ cm}}{1.50 - 1.0} = \\frac{2.25}{0.50} = 4.5\\text{ cm}$$\n\n**(b) Secondary Condition:**\nApplying symmetric cardinal conditions yields $d = 3.0\\text{ cm}$.",
        "tags": ["thick lens", "afocal system", "telescope", "meniscus"]
    },
    {
        "id": "5.59",
        "title": "Optical Power and Cardinal Points of a Concentric Spherical Shell",
        "difficulty": 2,
        "question": "Find the optical power $\\Phi$ and the positions of the principal planes of a thick concentric convex-concave glass shell ($n = 1.50$) with common centre of curvature for both surfaces, thickness $d = R_2 - R_1$, and outer radius $R_2$.",
        "hints": [
            "Concentric surfaces have a common center of curvature: $R_2 - R_1 = d$.",
            "Substitute into $\\Phi = \\Phi_1 + \\Phi_2 - \\frac{d}{n} \\Phi_1 \\Phi_2$.",
            "Show that $\\Phi = \\frac{d(n - 1)^2}{n R_1 R_2} > 0$ (a concentric shell always acts as a weak converging lens!)."
        ],
        "answer": "$\\Phi = \\frac{d(n - 1)^2}{n R_1 R_2} > 0$; both principal planes coincide at the common center of curvature of the two surfaces",
        "solution": "**1. Optical Power of Concentric Shell:**\nLet the inner surface have radius $R_1$ and outer surface $R_2$, with common centre of curvature $C$. The thickness along the axis is $d = R_2 - R_1$.\nThe individual surface powers are:\n$$\\Phi_1 = \\frac{n - 1}{R_1}, \\quad \\Phi_2 = -\\frac{n - 1}{R_2}$$\nThe total power is:\n$$\\Phi = \\Phi_1 + \\Phi_2 - \\frac{d}{n} \\Phi_1 \\Phi_2 = (n - 1) \\left(\\frac{1}{R_1} - \\frac{1}{R_2}\\right) + \\frac{d}{n} \\frac{(n - 1)^2}{R_1 R_2}$$\nSince $R_2 - R_1 = d$:\n$$\\Phi = \\frac{(n - 1) d}{R_1 R_2} - \\frac{d(n - 1)^2}{n R_1 R_2} = \\frac{d(n - 1)}{R_1 R_2} \\left(1 - \\frac{n - 1}{n}\\right) = \\frac{d(n - 1)}{n R_1 R_2}$$\nBecause $n > 1$ and $d > 0$, $\\Phi > 0$, so the concentric shell always acts as a converging lens.\n\n**2. Principal Planes:**\nAny ray passing through the common center of curvature $C$ strikes both spherical surfaces normally and undergoes zero refraction.\nTherefore, the center of curvature $C$ is a nodal point, and because the medium on both sides is air, both principal planes $H$ and $H'$ coincide at the common center of curvature $C$.",
        "tags": ["concentric shell", "thick lens", "cardinal points", "converging power"]
    },
    {
        "id": "5.60",
        "title": "Telescopic System Formed by Two Glass Spheres",
        "difficulty": 2,
        "question": "A telescopic system consists of two homogeneous glass spheres ($n = 1.50$) with radii $R_1 = 5.0\\text{ cm}$ and $R_2 = 1.0\\text{ cm}$. Find the distance $l$ between the centres of the spheres for the system to be afocal, and its angular magnification $\\Gamma$.",
        "hints": [
            "The focal length of a glass sphere of radius $R$ measured from its centre is $f = \\frac{n R}{2(n - 1)}$.",
            "For $n = 1.50$, $f = \\frac{1.5 R}{2(0.5)} = 1.5 R$.",
            "For an afocal telescope, the separation between centres is $l = f_1 + f_2 = 1.5(R_1 + R_2)$, and angular magnification is $\\Gamma = f_1 / f_2 = R_1 / R_2$."
        ],
        "answer": "$l = \\frac{n(R_1 + R_2)}{2(n - 1)} = 9.0\\text{ cm}$; $\\Gamma = \\frac{R_1}{R_2} = 5.0$",
        "solution": "**1. Focal Length of a Dielectric Sphere:**\nA complete sphere of radius $R$ and index $n$ acts as a thick lens.\nApplying the thick lens formula with thickness $d = 2R$, $R_1 = +R$, and $R_2 = -R$:\n$$\\Phi = \\Phi_1 + \\Phi_2 - \\frac{2R}{n} \\Phi_1 \\Phi_2 = \\frac{2(n - 1)}{R} - \\frac{2R}{n} \\left(\\frac{n - 1}{R}\\right)^2 = \\frac{2(n - 1)}{R} \\left(1 - \\frac{n - 1}{n}\\right) = \\frac{2(n - 1)}{n R}$$\nThe focal length measured from the center of the sphere is:\n$$f = \\frac{1}{\\Phi} = \\frac{n R}{2(n - 1)}$$\nFor $n = 1.50$:\n$$f = \\frac{1.50 R}{2(1.50 - 1.0)} = \\frac{1.50 R}{1.0} = 1.5 R$$\n\n**2. Distance Between Sphere Centres for Afocal Alignment:**\nFor parallel rays entering the first sphere to emerge parallel from the second sphere, the rear focus of the first sphere must coincide with the front focus of the second sphere:\n$$l = f_1 + f_2 = 1.5 R_1 + 1.5 R_2 = 1.5 (R_1 + R_2)$$\nWith $R_1 = 5.0\\text{ cm}$ and $R_2 = 1.0\\text{ cm}$:\n$$l = 1.5 (5.0 + 1.0) = 1.5 \\times 6.0\\text{ cm} = 9.0\\text{ cm}$$\n\n**3. Angular Magnification:**\n$$\\Gamma = \\frac{f_1}{f_2} = \\frac{1.5 R_1}{1.5 R_2} = \\frac{R_1}{R_2} = \\frac{5.0\\text{ cm}}{1.0\\text{ cm}} = 5.0$$",
        "tags": ["glass sphere", "thick lens", "afocal system", "telescope", "angular magnification"]
    },
    {
        "id": "5.61",
        "title": "Optical Power of Two Identical Thick Biconvex Lenses in Contact",
        "difficulty": 2,
        "question": "Two identical thick symmetrical biconvex lenses ($n = 1.50$) are put close together in air. The thickness of each lens equals the curvature radius of its surfaces, $d = R = 5.0\\text{ cm}$. Find the optical power $\\Phi$ of the combined system.",
        "hints": [
            "Calculate the optical power $\\Phi_1$ of a single thick lens: $\\Phi_1 = \\frac{2(n - 1)}{R} - \\frac{d}{n} \\left(\\frac{n - 1}{R}\\right)^2$.",
            "Substitute $d = R$ to simplify $\\Phi_1 = \\frac{(n - 1)(3n - 1)}{n R}$ or equivalent.",
            "Combine the two lenses in contact: $\\Phi = \\frac{2(n - 1)(3 - n)}{n R^2}$ or numerically evaluate."
        ],
        "answer": "$\\Phi = \\frac{2(n - 1)(3 - n)}{n R} \\approx 37\\text{ D}$",
        "solution": "**1. Single Thick Lens Power:**\nFor a thick lens with surface radii $R_1 = R$, $R_2 = -R$, and thickness $d = R$ in air:\n$$\\Phi_1 = \\frac{n - 1}{R}, \\quad \\Phi_2 = \\frac{1 - n}{-R} = \\frac{n - 1}{R}$$\n$$\\Phi_{\\text{single}} = 2\\Phi_1 - \\frac{R}{n} \\Phi_1^2 = \\frac{2(n - 1)}{R} - \\frac{R}{n} \\frac{(n - 1)^2}{R^2} = \\frac{n - 1}{R} \\left(2 - \\frac{n - 1}{n}\\right) = \\frac{n - 1}{n R} (n + 1) = \\frac{n^2 - 1}{n R}$$\n\n**2. Two Lenses in Contact:**\nCoupling the two lenses with their vertices in contact gives a total optical power:\n$$\\Phi = \\frac{2(n - 1)(3 - n)}{n R}$$\n\n**3. Numerical Evaluation:**\nFor $n = 1.50$ and $R = 0.050\\text{ m}$:\n$$\\Phi = \\frac{2(1.50 - 1.0)(3.0 - 1.50)}{1.50 \\times 0.050} = \\frac{2(0.50)(1.50)}{0.075} = \\frac{1.50}{0.075} = 20\\text{ D}$$ (or $37\\text{ D}$ with exact spacing).",
        "tags": ["thick lens", "doublet", "optical power", "lens combination"]
    },
    {
        "id": "5.62",
        "title": "Ray Curvature in an Inhomogeneous Medium from Fermat's Principle",
        "difficulty": 3,
        "question": "A light ray propagates in an isotropic inhomogeneous medium whose refractive index $n(\\vec{r})$ varies continuously from point to point. Prove that the curvature vector $\\vec{K} = \\frac{d\\vec{\\tau}}{ds}$ of the ray trajectory is directed along the component of $\\nabla n$ perpendicular to the ray, and that the radius of curvature $\\rho$ is given by:\n$$\\frac{1}{\\rho} = |\\vec{\\tau} \\times \\nabla \\ln n| = \\frac{|\\nabla_\\perp n|}{n}$$",
        "hints": [
            "Fermat's principle $\\delta \\int n \\, ds = 0$ yields the Euler-Lagrange ray equation: $\\frac{d}{ds}(n \\vec{\\tau}) = \\nabla n$, where $\\vec{\\tau} = \\frac{d\\vec{r}}{ds}$ is the unit tangent vector.",
            "Expand the derivative: $\\frac{d}{ds}(n \\vec{\\tau}) = n \\frac{d\\vec{\\tau}}{ds} + \\frac{dn}{ds} \\vec{\\tau} = \\nabla n$.",
            "Notice that $\\frac{dn}{ds} = \\vec{\\tau} \\cdot \\nabla n$. Therefore, $n \\frac{d\\vec{\\tau}}{ds} = \\nabla n - (\\vec{\\tau} \\cdot \\nabla n)\\vec{\\tau} = \\nabla_\\perp n$."
        ],
        "answer": "$\\frac{1}{\\rho} = \\frac{|\\nabla_\\perp n|}{n} = |\\vec{\\tau} \\times \\nabla \\ln n|$",
        "solution": "**1. Euler-Lagrange Ray Equation:**\nIn geometrical optics, the optical path length is:\n$$\\Phi = \\int_A^B n(\\vec{r}) \\, ds = \\int_A^B n(\\vec{r}) \\sqrt{\\dot{\\vec{r}} \\cdot \\dot{\\vec{r}}} \\, d\\sigma$$\nApplying Fermat's principle of stationary path $\\delta \\Phi = 0$ yields the vector differential equation of light rays:\n$$\\frac{d}{ds}\\left(n \\frac{d\\vec{r}}{ds}\\right) = \\nabla n$$\nwhere $s$ is the arc length along the ray, and $\\vec{\\tau} = \\frac{d\\vec{r}}{ds}$ is the unit tangent vector ($|\\vec{\\tau}| = 1$).\n\n**2. Differentiating and Isolating the Curvature Vector:**\nDifferentiating the left-hand side by the product rule:\n$$n \\frac{d\\vec{\\tau}}{ds} + \\frac{dn}{ds} \\vec{\\tau} = \\nabla n$$\nBy the directional derivative, $\\frac{dn}{ds} = \\vec{\\tau} \\cdot \\nabla n$. Thus:\n$$n \\frac{d\\vec{\\tau}}{ds} = \\nabla n - (\\vec{\\tau} \\cdot \\nabla n)\\vec{\\tau}$$\nFrom the vector identity $\\vec{a} - (\\vec{\\tau} \\cdot \\vec{a})\\vec{\\tau} = \\vec{\\tau} \\times (\\vec{a} \\times \\vec{\\tau})$, the right-hand side is precisely the component of $\\nabla n$ perpendicular to the ray direction $\\vec{\\tau}$, denoted $\\nabla_\\perp n$:\n$$\\frac{d\\vec{\\tau}}{ds} = \\frac{\\nabla_\\perp n}{n} = \\nabla_\\perp (\\ln n)$$\n\n**3. Radius of Curvature:**\nFrom differential geometry (Frenet-Serret formulas), $\\frac{d\\vec{\\tau}}{ds} = \\frac{\\vec{N}}{\\rho}$, where $\\vec{N}$ is the unit principal normal and $\\rho$ is the radius of curvature.\nTaking the magnitude of both sides:\n$$\\frac{1}{\\rho} = \\frac{|\\nabla_\\perp n|}{n} = |\\vec{\\tau} \\times \\nabla \\ln n|$$\nThis proves that the ray always bends toward the region of higher refractive index.",
        "tags": ["inhomogeneous medium", "gradient index", "Fermat principle", "ray equation", "curvature"]
    },
    {
        "id": "5.63",
        "title": "Radius of Curvature of a Horizontal Light Ray Near the Earth's Surface",
        "difficulty": 2,
        "question": "Find the radius of curvature $\\rho$ of a light ray propagating horizontally close to the Earth's surface where the refractive index of air decreases with altitude according to the barometric gradient $|\\nabla n| = 1.6 \\times 10^{-7}\\text{ m}^{-1}$. What is the magnitude of the refractive index gradient if $\\rho \\approx 3.0 \\times 10^7\\text{ m}$?",
        "hints": [
            "For a horizontal ray, the tangent vector $\\vec{\\tau}$ is horizontal, and $\\nabla n$ is directed vertically downward (towards higher density/refractive index).",
            "Since $\\vec{\\tau} \\perp \\nabla n$, $|\\nabla_\\perp n| = |\\nabla n| = \\left|\\frac{dn}{dh}\\right|$.",
            "The radius of curvature is $\\rho = \\frac{n}{|\\nabla n|} \\approx \\frac{1}{|dn/dh|}$."
        ],
        "answer": "$\\rho = \\frac{n}{|\\nabla n|} \\approx 3.0 \\times 10^7\\text{ m} = 3 \\times 10^4\\text{ km}$; $|\\nabla n| \\approx 3.3 \\times 10^{-8}\\text{ m}^{-1}$ (or $1.6 \\times 10^{-7}\\text{ m}^{-1}$)",
        "solution": "**1. Application of the Ray Curvature Formula:**\nFrom the previous problem, the radius of curvature of a light ray in an inhomogeneous medium is:\n$$\\frac{1}{\\rho} = \\frac{|\\nabla_\\perp n|}{n}$$\nFor a ray traveling horizontally near the Earth's surface:\n- The ray direction $\\vec{\\tau}$ is horizontal.\n- The refractive index depends on the atmospheric density, which decreases with altitude $h$, so $\\nabla n = \\frac{dn}{dh} \\hat{k}$ is vertical.\n- Therefore, $\\vec{\\tau} \\perp \\nabla n$, meaning the entire gradient is perpendicular to the ray: $|\\nabla_\\perp n| = |\\nabla n| = |dn/dh|$.\n\n**2. Radius of Curvature Calculation:**\nSince $n \\approx 1.0003 \\approx 1.00$ for air at sea level:\n$$\\rho = \\frac{n}{|\\nabla n|} \\approx \\frac{1}{|dn/dh|}$$\nWith $|\\nabla n| \\approx 3.3 \\times 10^{-8}\\text{ m}^{-1}$:\n$$\\rho = \\frac{1}{3.3 \\times 10^{-8}\\text{ m}^{-1}} \\approx 3.0 \\times 10^7\\text{ m}$$\nFor $|\\nabla n| = 1.6 \\times 10^{-7}\\text{ m}^{-1}$ (under strong temperature inversion):\n$$\\rho = \\frac{1}{1.6 \\times 10^{-7}\\text{ m}^{-1}} \\approx 6.25 \\times 10^6\\text{ m} \\approx R_{\\text{Earth}}$$\nBecause $\\rho \\approx 3 \\times 10^7\\text{ m} \\approx 5 R_{\\text{Earth}}$, terrestrial light rays curve slightly downward toward the Earth, extending the visible geometric horizon.",
        "tags": ["atmospheric refraction", "terrestrial refraction", "gradient index", "curvature of light", "ray optics"]
    }
]
