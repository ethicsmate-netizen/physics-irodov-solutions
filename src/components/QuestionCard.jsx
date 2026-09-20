import React, { useState } from 'react';
import MathRenderer from './MathRenderer';
import { 
  Star, 
  Check, 
  ChevronDown, 
  ChevronUp, 
  Copy, 
  Edit3, 
  Save
} from 'lucide-react';

export default function QuestionCard({
  question,
  userProgress = {},
  onUpdateStatus,
  onUpdateNotes,
  onTagClick
}) {
  const [showHints, setShowHints] = useState(false);
  const [showAnswer, setShowAnswer] = useState(false);
  const [showSolution, setShowSolution] = useState(false);
  const [isEditingNotes, setIsEditingNotes] = useState(false);
  const [copiedPrompt, setCopiedPrompt] = useState(false);
  const [notesText, setNotesText] = useState(userProgress.notes || '');

  const currentStatus = userProgress.status || 'unsolved';
  const isStarred = currentStatus === 'starred';
  const isSolved = currentStatus === 'solved';

  const handleCopyPrompt = () => {
    const prompt = `Please solve and clearly explain the following physics problem from I.E. Irodov's "Problems in General Physics" (Problem ${question.id}, ${question.chapter_title}):\n\n"${question.statement}"\n\nShow the physical reasoning, relevant formulas, analytical derivation, and final numerical/symbolic result.`;
    navigator.clipboard.writeText(prompt);
    setCopiedPrompt(true);
    setTimeout(() => setCopiedPrompt(false), 2000);
  };

  const handleSaveNotes = () => {
    onUpdateNotes(question.id, notesText);
    setIsEditingNotes(false);
  };

  return (
    <article className={`
      bg-white dark:bg-[#181818] border transition-colors rounded-xl overflow-hidden
      ${isSolved 
        ? 'border-neutral-300 dark:border-neutral-700' 
        : isStarred 
        ? 'border-neutral-300 dark:border-neutral-700' 
        : 'border-neutral-200 dark:border-neutral-800'
      }
    `}>
      {/* Question Header */}
      <div className="px-5 py-3.5 border-b border-neutral-100 dark:border-neutral-800/80 flex items-center justify-between gap-3 text-xs">
        
        {/* Left: Problem number & Chapter info */}
        <div className="flex items-baseline gap-2">
          <span className="font-mono font-semibold text-sm text-neutral-900 dark:text-neutral-100">
            {question.id}
          </span>
          <span className="text-neutral-400 dark:text-neutral-500">·</span>
          <span className="text-neutral-500 dark:text-neutral-400">
            {question.chapter_title}
          </span>
          {question.difficulty && (
            <>
              <span className="text-neutral-400 dark:text-neutral-500">·</span>
              <span className="text-neutral-400 dark:text-neutral-500 font-mono">
                {'★'.repeat(question.difficulty)}{'☆'.repeat(3 - question.difficulty)}
              </span>
            </>
          )}
        </div>

        {/* Right: Understated Controls */}
        <div className="flex items-center gap-1.5 text-neutral-500 dark:text-neutral-400">
          
          {/* Star */}
          <button
            onClick={() => onUpdateStatus(question.id, isStarred ? 'unsolved' : 'starred')}
            className={`p-1.5 rounded transition-colors ${
              isStarred 
                ? 'text-neutral-900 dark:text-neutral-100 font-bold' 
                : 'hover:text-neutral-800 dark:hover:text-neutral-200'
            }`}
            title={isStarred ? "Starred" : "Star"}
          >
            <Star className={`w-3.5 h-3.5 ${isStarred ? 'fill-current text-amber-500 dark:text-amber-400' : ''}`} />
          </button>

          {/* Solved Status */}
          <button
            onClick={() => onUpdateStatus(question.id, isSolved ? 'unsolved' : 'solved')}
            className={`px-2 py-0.5 rounded text-xs transition-colors flex items-center gap-1 ${
              isSolved 
                ? 'bg-neutral-100 dark:bg-neutral-800 text-neutral-900 dark:text-neutral-100 font-medium' 
                : 'hover:bg-neutral-50 dark:hover:bg-neutral-800/50 text-neutral-500'
            }`}
            title="Toggle Solved"
          >
            <Check className={`w-3 h-3 ${isSolved ? 'text-emerald-600 dark:text-emerald-400' : 'text-neutral-400'}`} />
            <span>{isSolved ? 'Solved' : 'Mark solved'}</span>
          </button>

          {/* Copy Prompt */}
          <button
            onClick={handleCopyPrompt}
            className="p-1.5 rounded hover:text-neutral-800 dark:hover:text-neutral-200 hover:bg-neutral-50 dark:hover:bg-neutral-800/50 transition-colors"
            title="Copy problem statement for AI solver"
          >
            {copiedPrompt ? (
              <span className="text-[11px] text-emerald-600 dark:text-emerald-400 font-sans">Copied</span>
            ) : (
              <Copy className="w-3.5 h-3.5" />
            )}
          </button>

          {/* Notes Toggle */}
          <button
            onClick={() => setIsEditingNotes(!isEditingNotes)}
            className={`p-1.5 rounded hover:text-neutral-800 dark:hover:text-neutral-200 hover:bg-neutral-50 dark:hover:bg-neutral-800/50 transition-colors ${
              userProgress.notes ? 'text-neutral-900 dark:text-neutral-100 font-medium' : ''
            }`}
            title="Personal Notes"
          >
            <Edit3 className="w-3.5 h-3.5" />
          </button>
        </div>

      </div>

      {/* Question Body */}
      <div className="p-5 sm:p-6 space-y-4">
        <div className="text-neutral-800 dark:text-neutral-200 leading-relaxed text-sm sm:text-base font-serif">
          <MathRenderer text={question.statement} />
        </div>

        {/* Tags */}
        {question.tags && question.tags.length > 0 && (
          <div className="flex flex-wrap items-center gap-2 pt-1 text-[11px] text-neutral-400 dark:text-neutral-500">
            {question.tags.map(tag => (
              <button
                key={tag}
                onClick={() => onTagClick?.(tag)}
                className="hover:text-neutral-700 dark:hover:text-neutral-300 transition-colors"
              >
                #{tag}
              </button>
            ))}
          </div>
        )}

        {/* Notes Editor */}
        {isEditingNotes && (
          <div className="pt-2 space-y-2">
            <div className="flex items-center justify-between text-xs text-neutral-500">
              <span>Personal Notes</span>
              <button
                onClick={handleSaveNotes}
                className="flex items-center gap-1 px-2 py-0.5 rounded bg-neutral-900 dark:bg-neutral-100 text-white dark:text-neutral-900 text-xs font-medium"
              >
                <Save className="w-3 h-3" /> Save
              </button>
            </div>
            <textarea
              value={notesText}
              onChange={(e) => setNotesText(e.target.value)}
              placeholder="Your thoughts, formulas, or working notes..."
              rows={3}
              className="w-full text-xs p-2.5 rounded-md bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 focus:outline-none focus:border-neutral-400 text-neutral-800 dark:text-neutral-200 font-mono"
            />
          </div>
        )}

        {/* Display Note if saved */}
        {!isEditingNotes && userProgress.notes && (
          <div 
            onClick={() => setIsEditingNotes(true)}
            className="p-3 bg-neutral-50 dark:bg-neutral-900/60 rounded-md text-xs text-neutral-600 dark:text-neutral-400 cursor-pointer border border-neutral-100 dark:border-neutral-800/80"
          >
            <span className="font-semibold text-neutral-700 dark:text-neutral-300 mr-1">Note:</span>
            {userProgress.notes}
          </div>
        )}

        {/* Disclosures: Hint, Answer, Solution */}
        <div className="pt-3 border-t border-neutral-100 dark:border-neutral-800/80 space-y-2">
          
          {/* Hints */}
          {question.hints && question.hints.length > 0 && (
            <div className="border border-neutral-100 dark:border-neutral-800/60 rounded-md overflow-hidden">
              <button
                onClick={() => setShowHints(!showHints)}
                className="w-full px-3 py-2 flex items-center justify-between text-xs text-neutral-600 dark:text-neutral-400 hover:bg-neutral-50 dark:hover:bg-neutral-800/40 transition-colors"
              >
                <span>Hints ({question.hints.length})</span>
                {showHints ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
              </button>

              {showHints && (
                <div className="px-4 py-3 bg-neutral-50/60 dark:bg-neutral-900/40 border-t border-neutral-100 dark:border-neutral-800/60 text-xs text-neutral-700 dark:text-neutral-300 space-y-2">
                  {question.hints.map((hint, hIdx) => (
                    <div key={hIdx} className="flex items-start gap-2">
                      <span className="font-mono text-neutral-400 shrink-0">{hIdx + 1}.</span>
                      <div className="flex-1">
                        <MathRenderer text={hint} />
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}

          {/* Answer */}
          {question.answer && (
            <div className="border border-neutral-100 dark:border-neutral-800/60 rounded-md overflow-hidden">
              <button
                onClick={() => setShowAnswer(!showAnswer)}
                className="w-full px-3 py-2 flex items-center justify-between text-xs text-neutral-600 dark:text-neutral-400 hover:bg-neutral-50 dark:hover:bg-neutral-800/40 transition-colors"
              >
                <span>Answer</span>
                {showAnswer ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
              </button>

              {showAnswer && (
                <div className="px-4 py-3 bg-neutral-50/60 dark:bg-neutral-900/40 border-t border-neutral-100 dark:border-neutral-800/60 text-xs sm:text-sm text-neutral-800 dark:text-neutral-200 font-mono">
                  <MathRenderer text={question.answer} />
                </div>
              )}
            </div>
          )}

          {/* Full Solution */}
          {question.solution && (
            <div className="border border-neutral-100 dark:border-neutral-800/60 rounded-md overflow-hidden">
              <button
                onClick={() => setShowSolution(!showSolution)}
                className="w-full px-3 py-2 flex items-center justify-between text-xs text-neutral-600 dark:text-neutral-400 hover:bg-neutral-50 dark:hover:bg-neutral-800/40 transition-colors"
              >
                <span>Step-by-Step Derivation</span>
                {showSolution ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
              </button>

              {showSolution && (
                <div className="px-4 py-3.5 bg-neutral-50/60 dark:bg-neutral-900/40 border-t border-neutral-100 dark:border-neutral-800/60 text-xs sm:text-sm text-neutral-800 dark:text-neutral-200 leading-relaxed font-serif">
                  <MathRenderer text={question.solution} />
                </div>
              )}
            </div>
          )}

        </div>

      </div>
    </article>
  );
}
