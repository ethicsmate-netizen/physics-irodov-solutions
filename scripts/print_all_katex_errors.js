import fs from 'fs';
import path from 'path';
import katex from 'katex';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const questions = JSON.parse(fs.readFileSync(path.resolve(__dirname, '../data/questions_seed.json'), 'utf-8'));

for (let i = 58; i < questions.length; i++) {
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
        console.log(`[${q.id}] ${field} (BLOCK) -> ERROR: ${err.message}`);
        console.log(`   EXPR: ${match[1].trim()}`);
      }
    }

    // Inline math
    const nonBlock = text.replace(/\$\$[\s\S]*?\$\$/g, '');
    const inlineRegex = /\$([^\$\n]+?)\$/g;
    while ((match = inlineRegex.exec(nonBlock)) !== null) {
      try {
        katex.renderToString(match[1].trim(), { displayMode: false, throwOnError: true, strict: false });
      } catch (err) {
        console.log(`[${q.id}] ${field} (INLINE) -> ERROR: ${err.message}`);
        console.log(`   EXPR: ${match[1].trim()}`);
      }
    }
  }
}
