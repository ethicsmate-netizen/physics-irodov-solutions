import fs from 'fs';
import path from 'path';
import katex from 'katex';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const questionsPath = path.resolve(__dirname, '../data/questions_seed.json');
const questions = JSON.parse(fs.readFileSync(questionsPath, 'utf-8'));

console.log(`Loaded ${questions.length} questions. Testing KaTeX rendering...`);

let totalErrors = 0;
const errorSamples = [];

for (const q of questions) {
  const fields = ['statement', 'answer', 'solution'];
  for (const field of fields) {
    const text = q[field] || '';
    if (!text) continue;

    // 1. Block math $$...$$
    const blockRegex = /\$\$([\s\S]*?)\$\$/g;
    let match;
    while ((match = blockRegex.exec(text)) !== null) {
      const expr = match[1].trim();
      try {
        katex.renderToString(expr, { displayMode: true, throwOnError: true, strict: 'error' });
      } catch (err) {
        totalErrors++;
        if (errorSamples.length < 30) {
          errorSamples.push({ id: q.id, field, type: 'block', expr, error: err.message });
        }
      }
    }

    // 2. Inline math $...$
    // Split by block math first so we don't double count
    const nonBlock = text.replace(/\$\$[\s\S]*?\$\$/g, '');
    const inlineRegex = /\$([^\$\n]+?)\$/g;
    while ((match = inlineRegex.exec(nonBlock)) !== null) {
      const expr = match[1].trim();
      try {
        katex.renderToString(expr, { displayMode: false, throwOnError: true, strict: 'error' });
      } catch (err) {
        totalErrors++;
        if (errorSamples.length < 30) {
          errorSamples.push({ id: q.id, field, type: 'inline', expr, error: err.message });
        }
      }
    }
  }
}

console.log(`\nTotal KaTeX errors found: ${totalErrors}`);
console.log(`First ${errorSamples.length} error samples:`);
for (const sample of errorSamples) {
  console.log(`\n--- [${sample.id}] in ${sample.field} (${sample.type}) ---`);
  console.log(`EXPR:  ${sample.expr}`);
  console.log(`ERROR: ${sample.error}`);
}
