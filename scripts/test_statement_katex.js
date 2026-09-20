import fs from 'fs';
import path from 'path';
import katex from 'katex';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const questions = JSON.parse(fs.readFileSync(path.resolve(__dirname, '../data/questions_seed.json'), 'utf-8'));

let statementErrors = 0;
const samples = [];

for (const q of questions) {
  const text = q.statement || '';
  const inlineRegex = /\$([^\$\n]+?)\$/g;
  let match;
  while ((match = inlineRegex.exec(text)) !== null) {
    const expr = match[1].trim();
    try {
      katex.renderToString(expr, { displayMode: false, throwOnError: true, strict: 'error' });
    } catch (err) {
      statementErrors++;
      if (samples.length < 20) {
        samples.push({ id: q.id, expr, error: err.message });
      }
    }
  }
}

console.log(`Statement KaTeX errors: ${statementErrors}`);
for (const s of samples) {
  console.log(`[${s.id}] EXPR: ${s.expr} -> ERROR: ${s.error}`);
}
