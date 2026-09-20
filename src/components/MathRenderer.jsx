import React, { useMemo } from 'react';
import katex from 'katex';

/**
 * Pre-processes and sanitizes a LaTeX expression for KaTeX.
 */
function sanitizeLaTeX(expr) {
  if (!expr) return '';
  let s = expr.trim();

  // Replace font/OCR artifacts
  s = s.replace(/\/c104\b|c104\b/g, '\\hbar ');
  s = s.replace(/\/c75\b|c75\b/g, '\\dots ');
  s = s.replace(/\/c245\b|c245\b/g, '\\dots ');
  s = s.replace(/\/c38\b|c38\b/g, '');

  // Replace common Unicode math symbols that KaTeX might choke on
  s = s.replace(/∆/g, '\\Delta ');
  s = s.replace(/µ/g, '\\mu ');
  s = s.replace(/Ω/g, '\\Omega ');
  s = s.replace(/⊥/g, '\\perp ');
  s = s.replace(/×/g, '\\times ');
  s = s.replace(/·/g, '\\cdot ');
  s = s.replace(/±/g, '\\pm ');
  s = s.replace(/≈/g, '\\approx ');
  s = s.replace(/≠/g, '\\neq ');
  s = s.replace(/≤/g, '\\le ');
  s = s.replace(/≥/g, '\\ge ');
  s = s.replace(/∝/g, '\\propto ');
  s = s.replace(/→/g, '\\to ');
  s = s.replace(/∂/g, '\\partial ');
  s = s.replace(/∫/g, '\\int ');
  s = s.replace(/∇/g, '\\nabla ');
  s = s.replace(/∞/g, '\\infty ');
  s = s.replace(/[–—]/g, '-');
  s = s.replace(/[′’‘]/g, "'");

  // Fix degree symbol
  s = s.replace(/°\s*(\d+)/g, '$1^{\\circ}');
  s = s.replace(/(\d+)\s*°/g, '$1^{\\circ}');
  s = s.replace(/°/g, '^{\\circ}');

  // Escape unescaped %
  s = s.replace(/([^\\])%/g, '$1\\%');

  // Strip multi-line bracket artifacts
  s = s.replace(/[]/g, '');
  s = s.replace(/[]/g, '(').replace(/[]/g, ')');
  s = s.replace(/[]/g, '[').replace(/[]/g, ']');

  // Fix consecutive primes
  s = s.replace(/'\s+'\s+'/g, "'''");
  s = s.replace(/'\s+'/g, "''");

  return s;
}

/**
 * Safely renders LaTeX expression to HTML string.
 * Returns null if parsing fails.
 */
function tryRenderKaTeX(expr, displayMode) {
  const cleaned = sanitizeLaTeX(expr);
  if (!cleaned) return null;

  try {
    const html = katex.renderToString(cleaned, {
      displayMode,
      throwOnError: true,
      strict: false,
    });
    return html;
  } catch {
    // If strict failed, try lenient render without throwing
    try {
      const fallbackHtml = katex.renderToString(cleaned, {
        displayMode,
        throwOnError: false,
        strict: false,
      });
      // Check if KaTeX emitted a red error span
      if (fallbackHtml.includes('katex-error')) {
        return null;
      }
      return fallbackHtml;
    } catch {
      return null;
    }
  }
}

/**
 * MathRenderer parses and renders mathematical expressions mixed with text.
 * Supports:
 * - Block math: $$ ... $$
 * - Inline math: $ ... $
 * - Markdown bold (**text**) and italics (*text*)
 * - Bulleted lists and line breaks
 */
export default function MathRenderer({ text = '', className = '' }) {
  const renderedContent = useMemo(() => {
    if (!text) return null;

    // Split text by block math $$ ... $$
    const blockParts = text.split(/(\$\$[\s\S]*?\$\$)/g);

    return blockParts.map((part, partIdx) => {
      // Check for block math
      if (part.startsWith('$$') && part.endsWith('$$') && part.length >= 4) {
        const mathExpr = part.slice(2, -2).trim();
        const html = tryRenderKaTeX(mathExpr, true);

        if (html) {
          return (
            <div
              key={partIdx}
              className="my-3 overflow-x-auto text-center py-1 text-neutral-900 dark:text-neutral-100"
              dangerouslySetInnerHTML={{ __html: html }}
            />
          );
        }

        // Fallback: render cleaned math in elegant serif font without red errors
        return (
          <div
            key={partIdx}
            className="my-3 text-center py-1 font-serif text-sm sm:text-base italic text-neutral-800 dark:text-neutral-200"
          >
            {sanitizeLaTeX(mathExpr)}
          </div>
        );
      }

      // Plain text and inline math
      const lines = part.split('\n');
      return (
        <div key={partIdx} className="space-y-1">
          {lines.map((line, lineIdx) => {
            if (line.trim() === '') {
              return <div key={lineIdx} className="h-1.5" />;
            }

            const isBullet = line.trim().startsWith('- ') || line.trim().startsWith('• ');
            const displayLine = isBullet ? line.trim().slice(2) : line;

            // Split line by inline math $ ... $
            const inlineParts = displayLine.split(/(\$[^\$\n]+?\$)/g);

            const renderedLine = inlineParts.map((subPart, subIdx) => {
              if (subPart.startsWith('$') && subPart.endsWith('$') && subPart.length >= 2) {
                const mathExpr = subPart.slice(1, -1).trim();
                const html = tryRenderKaTeX(mathExpr, false);

                if (html) {
                  return (
                    <span
                      key={subIdx}
                      className="inline-block px-0.5 text-neutral-900 dark:text-neutral-100"
                      dangerouslySetInnerHTML={{ __html: html }}
                    />
                  );
                }

                // Fallback for inline math
                return (
                  <span key={subIdx} className="font-serif italic text-neutral-900 dark:text-neutral-100 px-0.5">
                    {sanitizeLaTeX(mathExpr)}
                  </span>
                );
              }

              // Format bold **...**
              const boldParts = subPart.split(/(\*\*.*?\*\*)/g);
              return (
                <React.Fragment key={subIdx}>
                  {boldParts.map((bPart, bIdx) => {
                    if (bPart.startsWith('**') && bPart.endsWith('**') && bPart.length >= 4) {
                      return (
                        <strong key={bIdx} className="font-semibold text-neutral-900 dark:text-white">
                          {bPart.slice(2, -2)}
                        </strong>
                      );
                    }
                    return bPart;
                  })}
                </React.Fragment>
              );
            });

            if (isBullet) {
              return (
                <div key={lineIdx} className="flex items-start gap-2 pl-3">
                  <span className="text-neutral-400 font-bold leading-relaxed">•</span>
                  <div className="flex-1 leading-relaxed">{renderedLine}</div>
                </div>
              );
            }

            return (
              <div key={lineIdx} className="leading-relaxed">
                {renderedLine}
              </div>
            );
          })}
        </div>
      );
    });
  }, [text]);

  return <div className={`math-content ${className}`}>{renderedContent}</div>;
}
