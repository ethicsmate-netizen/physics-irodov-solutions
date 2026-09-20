import fs from 'fs';
import path from 'path';
import katex from 'katex';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const questions = JSON.parse(fs.readFileSync(path.resolve(__dirname, '../data/questions_seed.json'), 'utf-8'));

const ch1_3 = questions.filter(q => {
  const parts = q.id.split('.');
  return parts[0] === '1' && parseInt(parts[1]) >= 118 && parseInt(parts[1]) <= 199;
});

console.log(`Checking KaTeX rendering for ${ch1_3.length} Chapter 1.3 questions (1.118 to 1.199)...`);
let errors = 0;

for (const q of ch1_3) {
  for (const field of ['statement', 'answer', 'solution']) {
    const text = q[field] || '';
    // Block math
    const blockRegex = /\$\$([\s\S]*?)\$\$/g;
    let match;
    while ((match = blockRegex.exec(text)) !== null) {
      try {
        katex.renderToString(match[1].trim(), { displayMode: true, throwOnError: true, strict: false });
      } catch (err) {
        errors++;
        console.log(`[${q.id}] ${field} (block): ${err.message}`);
      }
    }

    // Inline math
    const nonBlock = text.replace(/\$\$[\s\S]*?\$\$/g, '');
    const inlineRegex = /\$([^\$\n]+?)\$/g;
    while ((match = inlineRegex.exec(nonBlock)) !== null) {
      try {
        katex.renderToString(match[1].trim(), { displayMode: false, throwOnError: true, strict: false });
      } catch (err) {
        errors++;
        console.log(`[${q.id}] ${field} (inline): ${err.message}`);
      }
    }
  }

  if (q.hints) {
    q.hints.forEach((h, idx) => {
      const inlineRegex = /\$([^\$\n]+?)\$/g;
      let match;
      while ((match = inlineRegex.exec(h)) !== null) {
        try {
          katex.renderToString(match[1].trim(), { displayMode: false, throwOnError: true, strict: false });
        } catch (err) {
          errors++;
          console.log(`[${q.id}] hint ${idx}: ${err.message}`);
        }
      }
    });
  }
}

console.log(`Chapter 1.3 total KaTeX errors: ${errors}`);
process.exit(errors === 0 ? 0 : 1);
