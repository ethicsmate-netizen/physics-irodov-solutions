import React, { useRef, useEffect } from 'react';
import { 
  Search, 
  X, 
  Sun, 
  Moon, 
  Menu,
  BookMarked
} from 'lucide-react';

export default function Navbar({
  searchTerm,
  setSearchTerm,
  onOpenPractice,
  onOpenFormulas,
  onOpenStats,
  darkMode,
  setDarkMode,
  stats,
  toggleSidebar
}) {
  const searchInputRef = useRef(null);

  useEffect(() => {
    const handleKeyDown = (e) => {
      if ((e.key === '/' || (e.ctrlKey && e.key === 'k')) && document.activeElement !== searchInputRef.current) {
        e.preventDefault();
        searchInputRef.current?.focus();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  return (
    <header className="sticky top-0 z-30 bg-white/95 dark:bg-[#121212]/95 backdrop-blur-sm border-b border-neutral-200 dark:border-neutral-800 transition-colors">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 h-14 flex items-center justify-between gap-4">
        
        {/* Left: Minimal Title & Sidebar Toggle */}
        <div className="flex items-center gap-3">
          <button
            onClick={toggleSidebar}
            className="lg:hidden p-1.5 text-neutral-500 hover:text-neutral-900 dark:hover:text-neutral-100 rounded-md"
            title="Table of Contents"
          >
            <Menu className="w-5 h-5" />
          </button>

          <div className="flex items-baseline gap-2">
            <span className="font-serif font-bold text-base sm:text-lg tracking-tight text-neutral-900 dark:text-neutral-100">
              Irodov
            </span>
            <span className="hidden sm:inline text-xs text-neutral-400 dark:text-neutral-500 font-normal">
              Problems in General Physics
            </span>
          </div>
        </div>

        {/* Center: Clean Minimal Search */}
        <div className="flex-1 max-w-sm mx-2">
          <div className="relative">
            <Search className="w-3.5 h-3.5 text-neutral-400 absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none" />
            <input
              ref={searchInputRef}
              type="text"
              placeholder="Search problems, topics, or numbers..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-8 pr-8 py-1 text-xs bg-neutral-100/70 dark:bg-neutral-800/60 hover:bg-neutral-100 dark:hover:bg-neutral-800 focus:bg-white dark:focus:bg-neutral-900 border border-neutral-200 dark:border-neutral-700/80 focus:border-neutral-400 dark:focus:border-neutral-500 rounded-md outline-none text-neutral-900 dark:text-neutral-100 placeholder-neutral-400 transition-all"
            />
            {searchTerm ? (
              <button
                onClick={() => setSearchTerm('')}
                className="absolute right-2.5 top-1/2 -translate-y-1/2 text-neutral-400 hover:text-neutral-600 dark:hover:text-neutral-200"
              >
                <X className="w-3 h-3" />
              </button>
            ) : (
              <span className="hidden sm:inline absolute right-2.5 top-1/2 -translate-y-1/2 text-[10px] text-neutral-400 font-mono">
                /
              </span>
            )}
          </div>
        </div>

        {/* Right: Clean Text Actions */}
        <div className="flex items-center gap-1 sm:gap-2">
          <button
            onClick={onOpenPractice}
            className="px-2.5 py-1 text-xs font-medium text-neutral-600 dark:text-neutral-300 hover:text-neutral-900 dark:hover:text-neutral-100 rounded hover:bg-neutral-100 dark:hover:bg-neutral-800 transition-colors"
          >
            Practice
          </button>

          <button
            onClick={onOpenFormulas}
            className="px-2.5 py-1 text-xs font-medium text-neutral-600 dark:text-neutral-300 hover:text-neutral-900 dark:hover:text-neutral-100 rounded hover:bg-neutral-100 dark:hover:bg-neutral-800 transition-colors"
          >
            Formulas
          </button>

          <button
            onClick={onOpenStats}
            className="px-2 py-1 text-xs text-neutral-500 dark:text-neutral-400 hover:text-neutral-800 dark:hover:text-neutral-200 rounded hover:bg-neutral-100 dark:hover:bg-neutral-800 font-mono transition-colors"
            title="Study Progress"
          >
            {stats?.solved || 0}/{stats?.total || 0}
          </button>

          <button
            onClick={() => setDarkMode(!darkMode)}
            className="p-1.5 text-neutral-500 hover:text-neutral-800 dark:hover:text-neutral-200 rounded hover:bg-neutral-100 dark:hover:bg-neutral-800 transition-colors ml-1"
            title={darkMode ? "Switch to Light Mode" : "Switch to Dark Mode"}
          >
            {darkMode ? <Sun className="w-4 h-4" /> : <Moon className="w-4 h-4" />}
          </button>
        </div>

      </div>
    </header>
  );
}
