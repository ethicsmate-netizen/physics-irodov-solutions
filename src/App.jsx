import React, { useState, useEffect, useMemo } from 'react';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import QuestionCard from './components/QuestionCard';
import PracticeMode from './components/PracticeMode';
import FormulaSheet from './components/FormulaSheet';
import StatsModal from './components/StatsModal';
import catalogData from '../data/irodov_catalog.json';
import questionsSeedData from '../data/questions_seed.json';
import { Shuffle, Download, RotateCcw } from 'lucide-react';

const STORAGE_PROGRESS_KEY = 'irodov_question_bank_progress';
const STORAGE_DARKMODE_KEY = 'irodov_dark_mode';

export default function App() {
  const [questions] = useState(questionsSeedData);
  const [catalog] = useState(catalogData);

  // Filters
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedPart, setSelectedPart] = useState(null);
  const [selectedChapter, setSelectedChapter] = useState(null);
  const [difficultyFilter, setDifficultyFilter] = useState('all');
  const [statusFilter, setStatusFilter] = useState('all');
  const [activeTag, setActiveTag] = useState(null);

  // Modals & Drawers
  const [isPracticeOpen, setIsPracticeOpen] = useState(false);
  const [isFormulasOpen, setIsFormulasOpen] = useState(false);
  const [isStatsOpen, setIsStatsOpen] = useState(false);
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  // Theme - defaults to calm clean light mode or user preference
  const [darkMode, setDarkMode] = useState(() => {
    const saved = localStorage.getItem(STORAGE_DARKMODE_KEY);
    return saved !== null ? JSON.parse(saved) : false;
  });

  // User Progress
  const [userProgress, setUserProgress] = useState(() => {
    try {
      const saved = localStorage.getItem(STORAGE_PROGRESS_KEY);
      return saved ? JSON.parse(saved) : {};
    } catch {
      return {};
    }
  });

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    localStorage.setItem(STORAGE_DARKMODE_KEY, JSON.stringify(darkMode));
  }, [darkMode]);

  useEffect(() => {
    localStorage.setItem(STORAGE_PROGRESS_KEY, JSON.stringify(userProgress));
  }, [userProgress]);

  const handleUpdateStatus = (qId, newStatus) => {
    setUserProgress(prev => ({
      ...prev,
      [qId]: {
        ...prev[qId],
        status: newStatus
      }
    }));
  };

  const handleUpdateNotes = (qId, notes) => {
    setUserProgress(prev => ({
      ...prev,
      [qId]: {
        ...prev[qId],
        notes
      }
    }));
  };

  const handleResetProgress = () => {
    setUserProgress({});
  };

  const filteredQuestions = useMemo(() => {
    return questions.filter(q => {
      if (searchTerm) {
        const term = searchTerm.toLowerCase().trim();
        const matchesId = q.id.toLowerCase().includes(term);
        const matchesStatement = q.statement.toLowerCase().includes(term);
        const matchesChapter = q.chapter_title.toLowerCase().includes(term);
        const matchesTags = q.tags?.some(t => t.toLowerCase().includes(term));
        const matchesAnswer = q.answer?.toLowerCase().includes(term);
        if (!matchesId && !matchesStatement && !matchesChapter && !matchesTags && !matchesAnswer) {
          return false;
        }
      }

      if (selectedPart && q.part_id !== selectedPart) return false;
      if (selectedChapter && q.chapter_id !== selectedChapter) return false;
      if (difficultyFilter !== 'all' && q.difficulty !== difficultyFilter) return false;
      if (activeTag && (!q.tags || !q.tags.includes(activeTag))) return false;

      const qStatus = userProgress[q.id]?.status || 'unsolved';
      if (statusFilter === 'solved' && qStatus !== 'solved') return false;
      if (statusFilter === 'starred' && qStatus !== 'starred') return false;
      if (statusFilter === 'in_progress' && qStatus !== 'in_progress') return false;
      if (statusFilter === 'unsolved' && qStatus === 'solved') return false;

      return true;
    });
  }, [questions, searchTerm, selectedPart, selectedChapter, difficultyFilter, statusFilter, activeTag, userProgress]);

  const overallStats = useMemo(() => {
    const total = questions.length;
    const solved = Object.values(userProgress).filter(p => p.status === 'solved').length;
    return { total, solved };
  }, [questions, userProgress]);

  const handleRandomQuestion = () => {
    if (filteredQuestions.length === 0) return;
    const randomQ = filteredQuestions[Math.floor(Math.random() * filteredQuestions.length)];
    setSearchTerm(randomQ.id);
  };

  const handleExportMarkdown = () => {
    let md = `# I.E. Irodov - Practice Problem Set\n\n`;
    md += `*Generated on ${new Date().toLocaleDateString()} (${filteredQuestions.length} problems)*\n\n---\n\n`;

    filteredQuestions.forEach((q, idx) => {
      md += `### Problem ${idx + 1} (Irodov ${q.id})\n`;
      md += `*${q.chapter_title}*\n\n`;
      md += `${q.statement}\n\n`;
      if (q.hints?.length) {
        md += `**Hints:**\n`;
        q.hints.forEach((h, hIdx) => {
          md += `${hIdx + 1}. ${h}\n`;
        });
        md += `\n`;
      }
      md += `> **Answer**: ${q.answer}\n\n`;
      md += `<details><summary>Solution</summary>\n\n${q.solution}\n\n</details>\n\n---\n\n`;
    });

    const blob = new Blob([md], { type: 'text/markdown;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `irodov_problems_${new Date().toISOString().slice(0, 10)}.md`;
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#fcfcfc] dark:bg-[#121212] text-neutral-900 dark:text-neutral-100">
      
      {/* Top Navbar */}
      <Navbar
        searchTerm={searchTerm}
        setSearchTerm={setSearchTerm}
        onOpenPractice={() => setIsPracticeOpen(true)}
        onOpenFormulas={() => setIsFormulasOpen(true)}
        onOpenStats={() => setIsStatsOpen(true)}
        darkMode={darkMode}
        setDarkMode={setDarkMode}
        stats={overallStats}
        toggleSidebar={() => setIsSidebarOpen(!isSidebarOpen)}
      />

      {/* Main Container */}
      <div className="flex-1 flex max-w-6xl w-full mx-auto">
        
        {/* Left Sidebar Table of Contents */}
        <Sidebar
          catalog={catalog}
          selectedPart={selectedPart}
          setSelectedPart={setSelectedPart}
          selectedChapter={selectedChapter}
          setSelectedChapter={setSelectedChapter}
          statusFilter={statusFilter}
          setStatusFilter={setStatusFilter}
          difficultyFilter={difficultyFilter}
          setDifficultyFilter={setDifficultyFilter}
          userProgress={userProgress}
          questions={questions}
          isOpen={isSidebarOpen}
          onClose={() => setIsSidebarOpen(false)}
        />

        {/* Reading & Problem Feed */}
        <main className="flex-1 min-w-0 px-4 sm:px-8 py-6 space-y-6">
          
          {/* Subheader */}
          <div className="flex flex-wrap items-baseline justify-between gap-3 border-b border-neutral-100 dark:border-neutral-800/80 pb-3">
            <div className="flex items-baseline gap-2">
              <h1 className="font-serif font-bold text-lg text-neutral-900 dark:text-neutral-100">
                {selectedChapter 
                  ? `${selectedChapter} ${catalog?.parts?.flatMap(p => p.chapters).find(c => c.id === selectedChapter)?.title || ''}` 
                  : selectedPart 
                  ? `Part ${selectedPart}: ${catalog?.parts?.find(p => p.id === selectedPart)?.title}` 
                  : 'All Problems'}
              </h1>
              <span className="text-xs text-neutral-400 font-mono">
                ({filteredQuestions.length})
              </span>
              {activeTag && (
                <button
                  onClick={() => setActiveTag(null)}
                  className="text-xs text-neutral-500 hover:text-neutral-800 underline ml-2"
                >
                  clear tag #{activeTag}
                </button>
              )}
            </div>

            {/* Actions */}
            <div className="flex items-center gap-3 text-xs text-neutral-500">
              <button
                onClick={handleRandomQuestion}
                className="hover:text-neutral-900 dark:hover:text-neutral-200 transition-colors flex items-center gap-1"
                title="Random Problem"
              >
                <Shuffle className="w-3 h-3" /> Random
              </button>
              <span>·</span>
              <button
                onClick={handleExportMarkdown}
                className="hover:text-neutral-900 dark:hover:text-neutral-200 transition-colors flex items-center gap-1"
                title="Export selected problems"
              >
                <Download className="w-3 h-3" /> Export
              </button>
            </div>
          </div>

          {/* Question Cards Feed */}
          {filteredQuestions.length > 0 ? (
            <div className="space-y-6">
              {filteredQuestions.map(q => (
                <QuestionCard
                  key={q.id}
                  question={q}
                  userProgress={userProgress[q.id] || {}}
                  onUpdateStatus={handleUpdateStatus}
                  onUpdateNotes={handleUpdateNotes}
                  onTagClick={(tag) => setActiveTag(tag)}
                />
              ))}
            </div>
          ) : (
            <div className="py-16 text-center text-neutral-400 space-y-2">
              <p className="text-sm">No problems match your selection.</p>
              <button
                onClick={() => {
                  setSearchTerm('');
                  setSelectedPart(null);
                  setSelectedChapter(null);
                  setDifficultyFilter('all');
                  setStatusFilter('all');
                  setActiveTag(null);
                }}
                className="text-xs text-neutral-600 dark:text-neutral-300 underline"
              >
                Reset filters
              </button>
            </div>
          )}

        </main>
      </div>

      {/* Modals */}
      <PracticeMode
        isOpen={isPracticeOpen}
        onClose={() => setIsPracticeOpen(false)}
        allQuestions={questions}
        catalog={catalog}
      />

      <FormulaSheet
        isOpen={isFormulasOpen}
        onClose={() => setIsFormulasOpen(false)}
      />

      <StatsModal
        isOpen={isStatsOpen}
        onClose={() => setIsStatsOpen(false)}
        questions={questions}
        catalog={catalog}
        userProgress={userProgress}
        onResetProgress={handleResetProgress}
      />

    </div>
  );
}
