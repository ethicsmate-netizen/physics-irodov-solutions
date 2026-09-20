import fs from 'fs';
import path from 'path';
import katex from 'katex';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const questions = JSON.parse(fs.readFileSync(path.resolve(__dirname, '../data/questions_seed.json'), 'utf-8'));

console.log("Checking first 58 questions (Chapter 1.1)...");
let ch1Errors = 0;

for (let i = 0; i < 58; i++) {
  const q = questions[i];
  for (const field of ['statement', 'answer', 'solution']) {
    const text = q[field] || '';
    // Block math
    const blockRegex = /\$\$([\s\S]*?)\$\$/g;
    let match;
    while ((match = blockRegex.exec(text)) !== null) {
      try {
        katex.renderToString(match[1].trim(), { displayMode: true, throwOnError: true, strict: false });
      } catch (err) {
        ch1Errors++;
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
        ch1Errors++;
        console.log(`[${q.id}] ${field} (inline): ${err.message}`);
      }
    }
  }
}

console.log(`Chapter 1.1 total KaTeX errors: ${ch1Errors}`);
