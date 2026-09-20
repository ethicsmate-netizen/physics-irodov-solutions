import React, { useState } from 'react';
import MathRenderer from './MathRenderer';
import { X, Search, Copy, Check } from 'lucide-react';

const FORMULAS_DATA = [
  {
    category: "Mechanics",
    sections: [
      {
        title: "Kinematics & Curvilinear Motion",
        formulas: [
          { name: "Radius of Curvature", latex: "R = \\frac{[1 + (y')^2]^{3/2}}{|y''|}" },
          { name: "Normal Acceleration", latex: "w_n = \\frac{v^2}{R}" },
          { name: "Tangential Acceleration", latex: "w_t = \\frac{dv}{dt}" },
          { name: "River Crossing (Minimum Time)", latex: "t_{\\min} = \\frac{l}{v}, \\quad \\theta = 90^\\circ" },
          { name: "River Crossing (Shortest Path)", latex: "t = \\frac{l}{\\sqrt{v^2 - u^2}}, \\quad \\sin\\alpha = \\frac{u}{v}" }
        ]
      },
      {
        title: "Rotational Dynamics & Solid Bodies",
        formulas: [
          { name: "Rotational Equation", latex: "\\vec{\\tau} = I \\vec{\\beta} = \\frac{d\\vec{L}}{dt}" },
          { name: "Thin Rod about End", latex: "I = \\frac{1}{3} m l^2" },
          { name: "Solid Cylinder about Axis", latex: "I = \\frac{1}{2} m R^2" },
          { name: "Physical Pendulum Period", latex: "T = 2\\pi \\sqrt{\\frac{I}{m g d}}" },
          { name: "Pure Rolling on Incline", latex: "w = \\frac{g \\sin\\alpha}{1 + I_c / (m R^2)}" }
        ]
      },
      {
        title: "Hydrodynamics & Gravitation",
        formulas: [
          { name: "Bernoulli Equation", latex: "p + \\frac{1}{2}\\rho v^2 + \\rho g z = \\text{const}" },
          { name: "Torricelli's Law", latex: "v = \\sqrt{2gh}" },
          { name: "Gravitational Potential", latex: "\\varphi = -\\frac{G M}{r}" }
        ]
      }
    ]
  },
  {
    category: "Thermodynamics",
    sections: [
      {
        title: "Ideal Gas & Polytropic Processes",
        formulas: [
          { name: "Equation of State", latex: "p V = \\nu R T = \\frac{m}{M} R T" },
          { name: "First Law of Thermodynamics", latex: "dQ = dU + dW = \\nu C_V dT + p dV" },
          { name: "Polytropic Heat Capacity", latex: "C = C_V + \\frac{R}{1 - n} = \\frac{R}{\\gamma - 1} - \\frac{R}{n - 1}" },
          { name: "Reversible Adiabatic", latex: "p V^\\gamma = \\text{const}, \\quad T V^{\\gamma - 1} = \\text{const}" }
        ]
      },
      {
        title: "Second Law & Entropy",
        formulas: [
          { name: "Entropy Definition", latex: "dS = \\frac{dQ_{rev}}{T}" },
          { name: "Ideal Gas Entropy Change", latex: "\\Delta S = \\nu C_V \\ln\\left(\\frac{T_2}{T_1}\\right) + \\nu R \\ln\\left(\\frac{V_2}{V_1}\\right)" },
          { name: "Isothermal Phase Change", latex: "\\Delta S = \\frac{m q}{T}" }
        ]
      }
    ]
  },
  {
    category: "Electrodynamics",
    sections: [
      {
        title: "Electrostatics & Current",
        formulas: [
          { name: "Charged Ring on Axis", latex: "E(x) = \\frac{q x}{4\\pi\\varepsilon_0 (R^2 + x^2)^{3/2}}" },
          { name: "Energy Density", latex: "w_e = \\frac{1}{2} \\varepsilon_0 \\varepsilon E^2" },
          { name: "Symmetric Resistor Cube", latex: "R_{body} = \\frac{5}{6} R, \\quad R_{face} = \\frac{3}{4} R, \\quad R_{edge} = \\frac{7}{12} R" }
        ]
      },
      {
        title: "Magnetostatics & Induction",
        formulas: [
          { name: "Rotating Rod Motional EMF", latex: "\\mathcal{E} = \\frac{1}{2} B \\omega l^2" },
          { name: "Faraday's Law", latex: "\\mathcal{E} = -\\frac{d\\Phi_B}{dt}" },
          { name: "Circular Loop on Axis", latex: "B(x) = \\frac{\\mu_0 I R^2}{2(R^2 + x^2)^{3/2}}" }
        ]
      }
    ]
  },
  {
    category: "Oscillations & Modern Physics",
    sections: [
      {
        title: "Oscillations & Waves",
        formulas: [
          { name: "SHM Initial Conditions", latex: "A = \\sqrt{x_0^2 + (v_0/\\omega)^2}, \\quad \\tan\\alpha = -\\frac{v_0}{\\omega x_0}" },
          { name: "Pipe Closed at One End", latex: "\\nu_n = (2n - 1) \\frac{v}{4l}" },
          { name: "Young's Slit Plate Shift", latex: "\\Delta x = \\frac{D}{d}(n - 1) h" },
          { name: "Single Slit Diffraction", latex: "\\Delta \\theta = \\frac{2\\lambda}{b}" }
        ]
      },
      {
        title: "Quantum & Atomic Physics",
        formulas: [
          { name: "Rutherford Impact Parameter", latex: "b = \\frac{z Z e^2}{8\\pi\\varepsilon_0 T} \\cot(\\theta/2)" },
          { name: "De Broglie Wavelength", latex: "\\lambda = \\frac{h}{p} = \\frac{h}{\\sqrt{2 m e V}}" },
          { name: "Heisenberg Uncertainty", latex: "\\Delta x \\Delta p \\ge \\frac{\\hbar}{2}" }
        ]
      }
    ]
  }
];

export default function FormulaSheet({ isOpen, onClose }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [activeCategory, setActiveCategory] = useState('All');
  const [copiedFormula, setCopiedFormula] = useState(null);

  if (!isOpen) return null;

  const handleCopy = (latex) => {
    navigator.clipboard.writeText(latex);
    setCopiedFormula(latex);
    setTimeout(() => setCopiedFormula(null), 1800);
  };

  const filteredCategories = FORMULAS_DATA.filter(cat => {
    if (activeCategory !== 'All' && cat.category !== activeCategory) return false;
    return true;
  });

  return (
    <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-xs flex items-center justify-center p-4 overflow-y-auto">
      <div className="bg-white dark:bg-[#181818] border border-neutral-200 dark:border-neutral-800 rounded-xl w-full max-w-3xl shadow-xl overflow-hidden my-auto flex flex-col max-h-[90vh]">
        
        {/* Minimal Header */}
        <div className="px-5 py-3 border-b border-neutral-100 dark:border-neutral-800 flex items-center justify-between">
          <div className="flex items-baseline gap-2">
            <span className="font-serif font-bold text-sm text-neutral-900 dark:text-neutral-100">
              Formulas Reference
            </span>
            <span className="text-xs text-neutral-400">Essential Relations</span>
          </div>
          <button
            onClick={onClose}
            className="p-1 text-neutral-400 hover:text-neutral-700 dark:hover:text-neutral-200"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Minimal Search & Tabs */}
        <div className="px-5 py-2.5 border-b border-neutral-100 dark:border-neutral-800/80 flex flex-wrap items-center justify-between gap-3 text-xs">
          <div className="flex items-center gap-1.5 overflow-x-auto">
            {['All', 'Mechanics', 'Thermodynamics', 'Electrodynamics', 'Oscillations & Modern Physics'].map(cat => (
              <button
                key={cat}
                onClick={() => setActiveCategory(cat)}
                className={`px-2 py-1 rounded transition-colors whitespace-nowrap ${
                  activeCategory === cat
                    ? 'bg-neutral-900 text-white dark:bg-neutral-100 dark:text-neutral-900 font-medium'
                    : 'text-neutral-500 hover:text-neutral-900 dark:hover:text-neutral-100'
                }`}
              >
                {cat}
              </button>
            ))}
          </div>

          <div className="relative">
            <Search className="w-3 h-3 text-neutral-400 absolute left-2.5 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              placeholder="Search formulas..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="pl-7 pr-2.5 py-1 text-xs bg-neutral-100 dark:bg-neutral-800 rounded border border-transparent focus:border-neutral-300 dark:focus:border-neutral-600 outline-none w-44"
            />
          </div>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-y-auto p-5 sm:p-6 space-y-6">
          {filteredCategories.map(cat => (
            <div key={cat.category} className="space-y-3">
              <h3 className="text-xs font-semibold text-neutral-400 uppercase tracking-wider">
                {cat.category}
              </h3>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                {cat.sections.map(sec => {
                  const filtered = sec.formulas.filter(f => 
                    !searchTerm || 
                    f.name.toLowerCase().includes(searchTerm.toLowerCase()) || 
                    f.latex.toLowerCase().includes(searchTerm.toLowerCase())
                  );

                  if (filtered.length === 0) return null;

                  return (
                    <div key={sec.title} className="p-3.5 rounded-lg border border-neutral-100 dark:border-neutral-800 bg-neutral-50/50 dark:bg-neutral-900/30 space-y-2">
                      <div className="text-xs font-medium text-neutral-700 dark:text-neutral-300">
                        {sec.title}
                      </div>
                      <div className="space-y-1.5">
                        {filtered.map(f => (
                          <div 
                            key={f.name}
                            className="group p-2 rounded bg-white dark:bg-neutral-900 border border-neutral-100 dark:border-neutral-800/80 hover:border-neutral-200 text-xs"
                          >
                            <div className="flex items-center justify-between text-[11px] text-neutral-500 mb-0.5">
                              <span>{f.name}</span>
                              <button
                                onClick={() => handleCopy(f.latex)}
                                className="opacity-0 group-hover:opacity-100 text-neutral-400 hover:text-neutral-700 transition-opacity"
                                title="Copy LaTeX"
                              >
                                {copiedFormula === f.latex ? <Check className="w-3 h-3 text-emerald-500" /> : <Copy className="w-3 h-3" />}
                              </button>
                            </div>
                            <div className="font-mono text-neutral-800 dark:text-neutral-200 overflow-x-auto">
                              <MathRenderer text={`$$${f.latex}$$`} />
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          ))}
        </div>

      </div>
    </div>
  );
}
