import katex from 'katex';

function sanitizeMath(expr) {
  if (!expr) return '';
  return expr
    .replace(/∆/g, '\\Delta ')
    .replace(/µ/g, '\\mu ')
    .replace(/Ω/g, '\\Omega ')
    .replace(/′/g, "'")
    .replace(/’/g, "'")
    .replace(/°/g, '^\\circ ')
    .replace(/×/g, '\\times ')
    .replace(/·/g, '\\cdot ')
    .replace(/±/g, '\\pm ')
    .replace(/≈/g, '\\approx ')
    .replace(/≤/g, '\\le ')
    .replace(/≥/g, '\\ge ')
    .replace(/≠/g, '\\neq ')
    .replace(/∝/g, '\\propto ')
    .replace(/→/g, '\\to ')
    .replace(/∂/g, '\\partial ')
    .replace(/∫/g, '\\int ')
    .replace(/∇/g, '\\nabla ')
    .replace(/\/c104|c104/g, '\\hbar ')
    .replace(/\/c75|c75/g, '\\dots ')
    .replace(/\/c245|c245/g, '\\dots ')
    .replace(/[]/g, '')
    .replace(/[]/g, '(')
    .replace(/[]/g, ')')
    .replace(/[]/g, '[')
    .replace(/[]/g, ']');
}

const tests = [
  '∆m mw g w= +2 /( ).',
  'k = − + =[( )/( )] tanη η α2 2 1 1 0.16.',
  'ψ π π= = =  A nx l n A nx l n cos ( / ),,,, sin ( / ),,, if if 2, 1 3 5 4 6 /c75 /c75 Here, A l= 2/.',
  'The oscillation energy of a mole of a “crystal” is U R T x dx e x T = +     −      ∫Θ Θ Θ1 4 1 2 0 /, where x kT= /c104 ω /.',
  'N t N e e t t 3 10 1 2 2 1 1 2 1 ( ).= + − −       − −λ λ λ λ λ λ',
  'Q M M c K M M m c p d p d = − − − −( ) and ( ) 2 22 for decay - capture, for β β +    decay.'
];

for (const t of tests) {
  const sanitized = sanitizeMath(t);
  try {
    const html = katex.renderToString(sanitized, { displayMode: true, throwOnError: true, strict: false });
    console.log("SUCCESS:", sanitized.slice(0, 50));
  } catch (err) {
    console.log("STILL FAILS:", err.message.slice(0, 60), "in:", sanitized.slice(0, 40));
  }
}
