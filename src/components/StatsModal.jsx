import React from 'react';
import { X, RotateCcw } from 'lucide-react';

export default function StatsModal({
  isOpen,
  onClose,
  questions,
  catalog,
  userProgress,
  onResetProgress
}) {
  if (!isOpen) return null;

  const total = questions.length;
  const solved = Object.values(userProgress).filter(p => p.status === 'solved').length;
  const starred = Object.values(userProgress).filter(p => p.status === 'starred').length;
  const unsolved = total - solved;
  const solvedPct = total > 0 ? Math.round((solved / total) * 100) : 0;

  return (
    <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-xs flex items-center justify-center p-4 overflow-y-auto">
      <div className="bg-white dark:bg-[#181818] border border-neutral-200 dark:border-neutral-800 rounded-xl w-full max-w-lg shadow-xl overflow-hidden my-auto flex flex-col">
        
        {/* Header */}
        <div className="px-5 py-3 border-b border-neutral-100 dark:border-neutral-800 flex items-center justify-between">
          <span className="font-serif font-bold text-sm text-neutral-900 dark:text-neutral-100">
            Study Progress
          </span>
          <button
            onClick={onClose}
            className="p-1 text-neutral-400 hover:text-neutral-700 dark:hover:text-neutral-200"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Content */}
        <div className="p-5 sm:p-6 space-y-6 text-xs">
          
          {/* Summary Row */}
          <div className="flex items-baseline justify-between border-b border-neutral-100 dark:border-neutral-800 pb-4">
            <div>
              <div className="text-2xl font-serif font-bold text-neutral-900 dark:text-neutral-100">
                {solvedPct}%
              </div>
              <div className="text-neutral-400 text-[11px] mt-0.5">
                {solved} of {total} problems solved
              </div>
            </div>

            <div className="text-right space-y-0.5 text-neutral-500">
              <div>Starred: <span className="font-mono text-neutral-800 dark:text-neutral-200">{starred}</span></div>
              <div>Remaining: <span className="font-mono text-neutral-800 dark:text-neutral-200">{unsolved}</span></div>
            </div>
          </div>

          {/* Parts breakdown */}
          <div className="space-y-2.5">
            <span className="text-[11px] font-semibold text-neutral-400 uppercase tracking-wider block">
              Breakdown by Part
            </span>
            <div className="space-y-2">
              {catalog?.parts?.map(part => {
                const partQuestions = questions.filter(q => q.part_id === part.id);
                const partSolved = partQuestions.filter(q => userProgress[q.id]?.status === 'solved').length;
                const partPct = partQuestions.length > 0 ? Math.round((partSolved / partQuestions.length) * 100) : 0;

                return (
                  <div key={part.id} className="flex items-center justify-between text-neutral-700 dark:text-neutral-300">
                    <span className="truncate pr-2">
                      Part {part.id}. {part.short_title}
                    </span>
                    <span className="font-mono text-neutral-400 shrink-0">
                      {partSolved}/{partQuestions.length} ({partPct}%)
                    </span>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Reset progress */}
          <div className="pt-4 border-t border-neutral-100 dark:border-neutral-800 flex justify-between items-center text-[11px]">
            <span className="text-neutral-400">Data saved locally in browser</span>
            <button
              onClick={() => {
                if (window.confirm("Reset all solved status and notes?")) {
                  onResetProgress();
                }
              }}
              className="text-neutral-400 hover:text-neutral-700 dark:hover:text-neutral-200 flex items-center gap-1"
            >
              <RotateCcw className="w-3 h-3" /> Reset
            </button>
          </div>

        </div>

      </div>
    </div>
  );
}
