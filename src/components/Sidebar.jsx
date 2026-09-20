import React, { useState } from 'react';
import { 
  ChevronDown, 
  ChevronRight, 
  RotateCcw
} from 'lucide-react';

export default function Sidebar({
  catalog,
  selectedPart,
  setSelectedPart,
  selectedChapter,
  setSelectedChapter,
  statusFilter,
  setStatusFilter,
  difficultyFilter,
  setDifficultyFilter,
  userProgress,
  questions,
  isOpen,
  onClose
}) {
  const [expandedParts, setExpandedParts] = useState({ 1: true });

  const togglePartExpand = (partId) => {
    setExpandedParts(prev => ({
      ...prev,
      [partId]: !prev[partId]
    }));
  };

  const getSolvedCount = (partId, chapterId = null) => {
    return questions.filter(q => {
      if (chapterId && q.chapter_id !== chapterId) return false;
      if (!chapterId && q.part_id !== partId) return false;
      return userProgress[q.id]?.status === 'solved';
    }).length;
  };

  const getLoadedCount = (partId, chapterId = null) => {
    return questions.filter(q => {
      if (chapterId && q.chapter_id !== chapterId) return false;
      if (!chapterId && q.part_id !== partId) return false;
      return true;
    }).length;
  };

  const resetFilters = () => {
    setSelectedPart(null);
    setSelectedChapter(null);
    setStatusFilter('all');
    setDifficultyFilter('all');
  };

  const hasActiveFilters = selectedPart !== null || selectedChapter !== null || statusFilter !== 'all' || difficultyFilter !== 'all';

  return (
    <>
      {/* Mobile backdrop */}
      {isOpen && (
        <div 
          onClick={onClose}
          className="fixed inset-0 bg-black/20 backdrop-blur-xs z-40 lg:hidden"
        />
      )}

      <aside className={`
        fixed top-14 bottom-0 left-0 z-40 w-72 bg-white dark:bg-[#121212] border-r border-neutral-200 dark:border-neutral-800 flex flex-col transition-transform duration-200 lg:translate-x-0 lg:static lg:z-0
        ${isOpen ? 'translate-x-0' : '-translate-x-full'}
      `}>
        {/* Table of Contents Header */}
        <div className="px-4 py-3 border-b border-neutral-100 dark:border-neutral-800/80 flex items-center justify-between">
          <span className="text-xs font-semibold text-neutral-400 dark:text-neutral-500 uppercase tracking-wider">
            Contents
          </span>
          {hasActiveFilters && (
            <button
              onClick={resetFilters}
              className="text-[11px] text-neutral-400 hover:text-neutral-700 dark:hover:text-neutral-200 flex items-center gap-1 transition-colors"
            >
              <RotateCcw className="w-2.5 h-2.5" />
              Reset
            </button>
          )}
        </div>

        {/* Minimal Status & Filter Bar */}
        <div className="px-4 py-2.5 border-b border-neutral-100 dark:border-neutral-800/80 space-y-2 text-xs">
          <div className="flex items-center gap-2 text-neutral-500 dark:text-neutral-400">
            <button
              onClick={() => setStatusFilter('all')}
              className={`pb-0.5 border-b transition-colors ${
                statusFilter === 'all' 
                  ? 'border-neutral-900 dark:border-neutral-100 text-neutral-900 dark:text-neutral-100 font-medium' 
                  : 'border-transparent hover:text-neutral-800'
              }`}
            >
              All ({questions.length})
            </button>
            <span>·</span>
            <button
              onClick={() => setStatusFilter('solved')}
              className={`pb-0.5 border-b transition-colors ${
                statusFilter === 'solved' 
                  ? 'border-neutral-900 dark:border-neutral-100 text-neutral-900 dark:text-neutral-100 font-medium' 
                  : 'border-transparent hover:text-neutral-800'
              }`}
            >
              Solved ({Object.values(userProgress).filter(p => p.status === 'solved').length})
            </button>
            <span>·</span>
            <button
              onClick={() => setStatusFilter('starred')}
              className={`pb-0.5 border-b transition-colors ${
                statusFilter === 'starred' 
                  ? 'border-neutral-900 dark:border-neutral-100 text-neutral-900 dark:text-neutral-100 font-medium' 
                  : 'border-transparent hover:text-neutral-800'
              }`}
            >
              Starred ({Object.values(userProgress).filter(p => p.status === 'starred').length})
            </button>
          </div>

          <div className="flex items-center gap-2 text-[11px] text-neutral-400 dark:text-neutral-500 pt-0.5">
            <span>Difficulty:</span>
            {['all', 1, 2, 3].map(d => (
              <button
                key={d}
                onClick={() => setDifficultyFilter(d)}
                className={`px-1.5 py-0.5 rounded text-[11px] transition-colors ${
                  difficultyFilter === d
                    ? 'bg-neutral-900 text-white dark:bg-neutral-100 dark:text-neutral-900 font-medium'
                    : 'hover:text-neutral-700 dark:hover:text-neutral-300'
                }`}
              >
                {d === 'all' ? 'All' : `L${d}`}
              </button>
            ))}
          </div>
        </div>

        {/* Chapters List */}
        <div className="flex-1 overflow-y-auto px-3 py-2 space-y-0.5">
          {catalog?.parts?.map(part => {
            const isPartSelected = selectedPart === part.id && !selectedChapter;
            const isExpanded = !!expandedParts[part.id];
            const loadedPartCount = getLoadedCount(part.id);
            const solvedPartCount = getSolvedCount(part.id);

            return (
              <div key={part.id} className="py-0.5">
                {/* Part line */}
                <div 
                  className={`w-full flex items-center justify-between px-2 py-1.5 rounded cursor-pointer transition-colors text-xs ${
                    isPartSelected
                      ? 'bg-neutral-100 dark:bg-neutral-800/70 text-neutral-900 dark:text-neutral-100 font-semibold'
                      : 'text-neutral-700 dark:text-neutral-300 hover:bg-neutral-50 dark:hover:bg-neutral-800/40'
                  }`}
                  onClick={() => {
                    if (selectedPart === part.id && !selectedChapter) {
                      setSelectedPart(null);
                    } else {
                      setSelectedPart(part.id);
                      setSelectedChapter(null);
                    }
                  }}
                >
                  <div className="flex items-center gap-1.5 min-w-0 pr-2">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        togglePartExpand(part.id);
                      }}
                      className="p-0.5 text-neutral-400 hover:text-neutral-600 rounded"
                    >
                      {isExpanded ? <ChevronDown className="w-3 h-3" /> : <ChevronRight className="w-3 h-3" />}
                    </button>
                    <span className="truncate font-medium">
                      Part {part.id}. {part.short_title}
                    </span>
                  </div>
                  <span className="text-[10px] text-neutral-400 font-mono shrink-0">
                    {solvedPartCount > 0 && <span className="text-neutral-600 dark:text-neutral-300 mr-1">✓</span>}
                    {loadedPartCount}
                  </span>
                </div>

                {/* Subchapters */}
                {isExpanded && (
                  <div className="pl-5 pr-1 py-0.5 space-y-0.5">
                    {part.chapters?.map(chapter => {
                      const isChapterSelected = selectedChapter === chapter.id;
                      const loadedChCount = getLoadedCount(part.id, chapter.id);
                      const solvedChCount = getSolvedCount(part.id, chapter.id);

                      return (
                        <button
                          key={chapter.id}
                          onClick={() => {
                            if (isChapterSelected) {
                              setSelectedChapter(null);
                            } else {
                              setSelectedPart(part.id);
                              setSelectedChapter(chapter.id);
                            }
                          }}
                          className={`w-full text-left px-2 py-1 rounded text-xs flex items-center justify-between transition-colors ${
                            isChapterSelected
                              ? 'bg-neutral-900 text-white dark:bg-neutral-100 dark:text-neutral-900 font-medium'
                              : 'text-neutral-600 dark:text-neutral-400 hover:bg-neutral-50 dark:hover:bg-neutral-800/50 hover:text-neutral-900 dark:hover:text-neutral-200'
                          }`}
                        >
                          <span className="truncate pr-2">
                            {chapter.id} {chapter.title}
                          </span>
                          <span className="text-[10px] opacity-60 font-mono shrink-0">
                            {solvedChCount > 0 ? '✓' : loadedChCount > 0 ? loadedChCount : ''}
                          </span>
                        </button>
                      );
                    })}
                  </div>
                )}
              </div>
            );
          })}
        </div>

        {/* Footer */}
        <div className="px-4 py-2 border-t border-neutral-100 dark:border-neutral-800/80 text-[11px] text-neutral-400">
          1,877 problems · Mir Publishers
        </div>
      </aside>
    </>
  );
}
