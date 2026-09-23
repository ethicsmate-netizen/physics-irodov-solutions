import json
import subprocess
import sys
sys.stdout.reconfigure(encoding='utf-8')

from part5_ch5_7 import CH5_7_CURATED

# Write items temporarily to json
with open('temp_batch.json', 'w', encoding='utf-8') as f:
    json.dump(CH5_7_CURATED, f, ensure_ascii=False)

# Node tester
node_script = """
import fs from 'fs';
import katex from 'katex';

const items = JSON.parse(fs.readFileSync('temp_batch.json', 'utf-8'));
let errors = 0;

for (const q of items) {
  for (const field of ['question', 'answer', 'solution']) {
    const text = q[field] || '';
    
    // Block math
    const blockRegex = /\\$\\$([\\s\\S]*?)\\$\\$/g;
    let match;
    while ((match = blockRegex.exec(text)) !== null) {
      const expr = match[1].trim();
      try {
        katex.renderToString(expr, { displayMode: true, throwOnError: true, strict: 'error' });
      } catch (err) {
        errors++;
        console.error(`[${q.id}] Block KaTeX error in ${field}: ${err.message}\\nEXPR: ${expr}`);
      }
    }

    // Inline math
    const nonBlock = text.replace(/\\$\\$[\\s\\S]*?\\$\\$/g, '');
    const inlineRegex = /\\$([^\\$\\n]+?)\\$/g;
    while ((match = inlineRegex.exec(nonBlock)) !== null) {
      const expr = match[1].trim();
      try {
        katex.renderToString(expr, { displayMode: false, throwOnError: true, strict: 'error' });
      } catch (err) {
        errors++;
        console.error(`[${q.id}] Inline KaTeX error in ${field}: ${err.message}\\nEXPR: ${expr}`);
      }
    }
  }
}

console.log(`KaTeX test finished. Total errors: ${errors}`);
if (errors > 0) process.exit(1);
"""

with open('test_temp.mjs', 'w', encoding='utf-8') as f:
    f.write(node_script)

res = subprocess.run(['node', 'test_temp.mjs'], capture_output=True, text=True, encoding='utf-8')
print(res.stdout)
if res.stderr:
    print(res.stderr)

import os
if os.path.exists('temp_batch.json'): os.remove('temp_batch.json')
if os.path.exists('test_temp.mjs'): os.remove('test_temp.mjs')

if res.returncode != 0:
    sys.exit(1)
