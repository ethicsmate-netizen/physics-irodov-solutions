import fs from 'fs';
import path from 'path';
import katex from 'katex';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const questions = JSON.parse(fs.readFileSync(path.resolve(__dirname, '../data/questions_seed.json'), 'utf-8'));

console.log("Checking questions 58 to 1866...");
let restErrors = 0;
let failingQuestions = new Set();
let errorTypes = {};

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
        restErrors++;
        failingQuestions.add(q.id);
        const errKey = err.message.slice(0, 40);
        errorTypes[errKey] = (errorTypes[errKey] || 0) + 1;
      }
    }

    // Inline math
    const nonBlock = text.replace(/\$\$[\s\S]*?\$\$/g, '');
    const inlineRegex = /\$([^\$\n]+?)\$/g;
    while ((match = inlineRegex.exec(nonBlock)) !== null) {
      try {
        katex.renderToString(match[1].trim(), { displayMode: false, throwOnError: true, strict: false });
      } catch (err) {
        restErrors++;
        failingQuestions.add(q.id);
        const errKey = err.message.slice(0, 40);
        errorTypes[errKey] = (errorTypes[errKey] || 0) + 1;
      }
    }
  }
}

console.log(`Questions 58-1866 total KaTeX errors: ${restErrors}`);
console.log(`Total questions affected: ${failingQuestions.size} out of ${questions.length - 58}`);
console.log("\nError breakdown:");
for (const [k, v] of Object.entries(errorTypes)) {
  console.log(`  ${v}x : ${k}`);
}
