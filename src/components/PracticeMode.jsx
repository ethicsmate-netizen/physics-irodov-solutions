import React, { useState, useEffect } from 'react';
import MathRenderer from './MathRenderer';
import { X, ChevronLeft, ChevronRight } from 'lucide-react';

export default function PracticeMode({
  isOpen,
  onClose,
  allQuestions,
  catalog
}) {
  const [stage, setStage] = useState('setup'); // 'setup', 'active', 'completed'
  const [selectedPart, setSelectedPart] = useState('all');
  const [questionCount, setQuestionCount] = useState(5);
  const [timeLimitMinutes, setTimeLimitMinutes] = useState(15);
  
  const [testQuestions, setTestQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [secondsRemaining, setSecondsRemaining] = useState(0);
  const [userAnswers, setUserAnswers] = useState({});
  const [selfAssessment, setSelfAssessment] = useState({});

  useEffect(() => {
    if (stage !== 'active' || timeLimitMinutes === 0) return;

    if (secondsRemaining <= 0) {
      handleFinishTest();
      return;
    }

    const timer = setInterval(() => {
      setSecondsRemaining(prev => prev - 1);
    }, 1000);

    return () => clearInterval(timer);
  }, [stage, secondsRemaining, timeLimitMinutes]);

  if (!isOpen) return null;

  const handleStartTest = () => {
    let pool = [...allQuestions];
    if (selectedPart !== 'all') {
      pool = pool.filter(q => q.part_id === Number(selectedPart));
    }

    const shuffled = pool.sort(() => 0.5 - Math.random());
    const selected = shuffled.slice(0, Math.min(questionCount, shuffled.length));

    setTestQuestions(selected);
    setCurrentIndex(0);
    setSecondsRemaining(timeLimitMinutes * 60);
    setUserAnswers({});
    setSelfAssessment({});
    setStage('active');
  };

  const handleFinishTest = () => {
    setStage('completed');
  };

  const handleAnswerChange = (qId, val) => {
    setUserAnswers(prev => ({ ...prev, [qId]: val }));
  };

  const formatTime = (secs) => {
    const mins = Math.floor(secs / 60);
    const remSecs = secs % 60;
    return `${mins.toString().padStart(2, '0')}:${remSecs.toString().padStart(2, '0')}`;
  };

  const currentQ = testQuestions[currentIndex];

  return (
    <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-xs flex items-center justify-center p-4 overflow-y-auto">
      <div className="bg-white dark:bg-[#181818] border border-neutral-200 dark:border-neutral-800 rounded-xl w-full max-w-3xl shadow-xl overflow-hidden my-auto flex flex-col max-h-[90vh]">
        
        {/* Minimal Header */}
        <div className="px-5 py-3 border-b border-neutral-100 dark:border-neutral-800 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <span className="font-serif font-bold text-sm text-neutral-900 dark:text-neutral-100">
              {stage === 'setup' && 'Practice Test Setup'}
              {stage === 'active' && `Problem ${currentIndex + 1} of ${testQuestions.length}`}
              {stage === 'completed' && 'Test Review & Solutions'}
            </span>
            {stage === 'active' && timeLimitMinutes > 0 && (
              <span className="text-xs font-mono text-neutral-500 dark:text-neutral-400">
                · {formatTime(secondsRemaining)} remaining
              </span>
            )}
          </div>
          <button
            onClick={onClose}
            className="p-1 text-neutral-400 hover:text-neutral-700 dark:hover:text-neutral-200"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Modal Body */}
        <div className="flex-1 overflow-y-auto p-5 sm:p-6">
          
          {/* SETUP STAGE */}
          {stage === 'setup' && (
            <div className="space-y-5 max-w-md mx-auto py-3">
              <div className="space-y-1">
                <h3 className="font-serif font-bold text-base text-neutral-900 dark:text-neutral-100">
                  Timed Practice Session
                </h3>
                <p className="text-xs text-neutral-500">
                  Select your topics and time limit. Questions are drawn at random from the catalog.
                </p>
              </div>

              <div className="space-y-4 pt-2">
                <div className="space-y-1">
                  <label className="text-xs font-medium text-neutral-700 dark:text-neutral-300">
                    Syllabus:
                  </label>
                  <select
                    value={selectedPart}
                    onChange={(e) => setSelectedPart(e.target.value)}
                    className="w-full text-xs p-2 rounded-md bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 text-neutral-800 dark:text-neutral-200 outline-none"
                  >
                    <option value="all">All Parts</option>
                    {catalog?.parts?.map(p => (
                      <option key={p.id} value={p.id}>
                        Part {p.id}: {p.title}
                      </option>
                    ))}
                  </select>
                </div>

                <div className="space-y-1">
                  <label className="text-xs font-medium text-neutral-700 dark:text-neutral-300">
                    Questions:
                  </label>
                  <div className="flex gap-2">
                    {[3, 5, 8, 10].map(cnt => (
                      <button
                        key={cnt}
                        type="button"
                        onClick={() => setQuestionCount(cnt)}
                        className={`flex-1 py-1.5 rounded text-xs transition-colors ${
                          questionCount === cnt
                            ? 'bg-neutral-900 text-white dark:bg-neutral-100 dark:text-neutral-900 font-medium'
                            : 'border border-neutral-200 dark:border-neutral-800 text-neutral-600 dark:text-neutral-400 hover:bg-neutral-50'
                        }`}
                      >
                        {cnt}
                      </button>
                    ))}
                  </div>
                </div>

                <div className="space-y-1">
                  <label className="text-xs font-medium text-neutral-700 dark:text-neutral-300">
                    Time Limit:
                  </label>
                  <div className="flex gap-2">
                    {[
                      { label: '10m', mins: 10 },
                      { label: '20m', mins: 20 },
                      { label: '45m', mins: 45 },
                      { label: 'None', mins: 0 }
                    ].map(t => (
                      <button
                        key={t.label}
                        type="button"
                        onClick={() => setTimeLimitMinutes(t.mins)}
                        className={`flex-1 py-1.5 rounded text-xs transition-colors ${
                          timeLimitMinutes === t.mins
                            ? 'bg-neutral-900 text-white dark:bg-neutral-100 dark:text-neutral-900 font-medium'
                            : 'border border-neutral-200 dark:border-neutral-800 text-neutral-600 dark:text-neutral-400 hover:bg-neutral-50'
                        }`}
                      >
                        {t.label}
                      </button>
                    ))}
                  </div>
                </div>
              </div>

              <div className="pt-4">
                <button
                  onClick={handleStartTest}
                  className="w-full py-2.5 rounded-md bg-neutral-900 dark:bg-neutral-100 text-white dark:text-neutral-900 text-xs font-medium hover:bg-neutral-800 dark:hover:bg-neutral-200 transition-colors"
                >
                  Start Practice
                </button>
              </div>
            </div>
          )}

          {/* ACTIVE TEST STAGE */}
          {stage === 'active' && currentQ && (
            <div className="space-y-5">
              {/* Question numbers pagination */}
              <div className="flex items-center justify-between border-b border-neutral-100 dark:border-neutral-800 pb-3">
                <div className="flex gap-1.5">
                  {testQuestions.map((q, idx) => (
                    <button
                      key={q.id}
                      onClick={() => setCurrentIndex(idx)}
                      className={`w-6 h-6 rounded text-xs font-mono transition-colors ${
                        idx === currentIndex
                          ? 'bg-neutral-900 text-white dark:bg-neutral-100 dark:text-neutral-900 font-medium'
                          : userAnswers[q.id]?.trim()
                          ? 'bg-neutral-100 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300'
                          : 'text-neutral-400 hover:text-neutral-600'
                      }`}
                    >
                      {idx + 1}
                    </button>
                  ))}
                </div>

                <button
                  onClick={handleFinishTest}
                  className="px-2.5 py-1 text-xs border border-neutral-200 dark:border-neutral-700 rounded hover:bg-neutral-50 dark:hover:bg-neutral-800 text-neutral-700 dark:text-neutral-300"
                >
                  Submit
                </button>
              </div>

              {/* Problem statement */}
              <div className="space-y-2">
                <div className="text-xs text-neutral-400">
                  Irodov {currentQ.id} · {currentQ.chapter_title}
                </div>
                <div className="p-4 bg-neutral-50/50 dark:bg-neutral-900/30 rounded-lg border border-neutral-100 dark:border-neutral-800/80 font-serif leading-relaxed text-sm">
                  <MathRenderer text={currentQ.statement} />
                </div>
              </div>

              {/* Answer input */}
              <div className="space-y-1">
                <label className="text-xs text-neutral-500">Your Working / Answer:</label>
                <textarea
                  rows={3}
                  value={userAnswers[currentQ.id] || ''}
                  onChange={(e) => handleAnswerChange(currentQ.id, e.target.value)}
                  placeholder="Type symbolic expression or numerical answer..."
                  className="w-full text-xs p-2.5 rounded-md bg-neutral-50 dark:bg-neutral-900 border border-neutral-200 dark:border-neutral-800 font-mono text-neutral-800 dark:text-neutral-200 outline-none"
                />
              </div>

              {/* Prev / Next buttons */}
              <div className="flex items-center justify-between pt-2">
                <button
                  disabled={currentIndex === 0}
                  onClick={() => setCurrentIndex(prev => prev - 1)}
                  className="flex items-center gap-1 text-xs text-neutral-500 disabled:opacity-30 hover:text-neutral-800"
                >
                  <ChevronLeft className="w-3.5 h-3.5" /> Previous
                </button>
                {currentIndex < testQuestions.length - 1 ? (
                  <button
                    onClick={() => setCurrentIndex(prev => prev + 1)}
                    className="flex items-center gap-1 text-xs font-medium text-neutral-900 dark:text-neutral-100 hover:underline"
                  >
                    Next <ChevronRight className="w-3.5 h-3.5" />
                  </button>
                ) : (
                  <button
                    onClick={handleFinishTest}
                    className="text-xs font-medium text-neutral-900 dark:text-neutral-100 hover:underline"
                  >
                    Finish
                  </button>
                )}
              </div>
            </div>
          )}

          {/* COMPLETED / RESULTS STAGE */}
          {stage === 'completed' && (
            <div className="space-y-5">
              <div className="border-b border-neutral-100 dark:border-neutral-800 pb-3">
                <h3 className="font-serif font-bold text-base text-neutral-900 dark:text-neutral-100">
                  Review & Self-Evaluation
                </h3>
                <p className="text-xs text-neutral-500">Compare your response with the official solutions.</p>
              </div>

              <div className="space-y-5">
                {testQuestions.map((q, idx) => (
                  <div key={q.id} className="border border-neutral-200 dark:border-neutral-800 rounded-lg p-4 space-y-3">
                    <div className="flex items-center justify-between text-xs text-neutral-400">
                      <span className="font-semibold text-neutral-700 dark:text-neutral-300">
                        {idx + 1}. Irodov {q.id} ({q.chapter_title})
                      </span>
                      <div className="flex gap-2">
                        <button
                          onClick={() => setSelfAssessment(prev => ({ ...prev, [q.id]: 'correct' }))}
                          className={`px-2 py-0.5 rounded text-xs ${
                            selfAssessment[q.id] === 'correct' 
                              ? 'bg-neutral-900 text-white dark:bg-neutral-100 dark:text-neutral-900' 
                              : 'text-neutral-400 hover:text-neutral-700'
                          }`}
                        >
                          Correct
                        </button>
                        <button
                          onClick={() => setSelfAssessment(prev => ({ ...prev, [q.id]: 'incorrect' }))}
                          className={`px-2 py-0.5 rounded text-xs ${
                            selfAssessment[q.id] === 'incorrect' 
                              ? 'bg-neutral-900 text-white dark:bg-neutral-100 dark:text-neutral-900' 
                              : 'text-neutral-400 hover:text-neutral-700'
                          }`}
                        >
                          Incorrect
                        </button>
                      </div>
                    </div>

                    <div className="text-xs sm:text-sm font-serif text-neutral-800 dark:text-neutral-200">
                      <MathRenderer text={q.statement} />
                    </div>

                    {userAnswers[q.id] && (
                      <div className="text-xs text-neutral-500 bg-neutral-50 dark:bg-neutral-900 p-2.5 rounded font-mono">
                        <span className="font-sans text-[11px] block text-neutral-400">Your Answer:</span>
                        {userAnswers[q.id]}
                      </div>
                    )}

                    <div className="text-xs sm:text-sm text-neutral-900 dark:text-neutral-100 font-mono bg-neutral-50 dark:bg-neutral-900 p-2.5 rounded">
                      <span className="font-sans text-[11px] block text-neutral-400">Official Answer:</span>
                      <MathRenderer text={q.answer} />
                    </div>

                    <details className="text-xs text-neutral-600 dark:text-neutral-400">
                      <summary className="cursor-pointer font-medium hover:underline">
                        View Step-by-Step Derivation
                      </summary>
                      <div className="pt-2 font-serif leading-relaxed">
                        <MathRenderer text={q.solution} />
                      </div>
                    </details>
                  </div>
                ))}
              </div>

              <div className="flex justify-end gap-2 pt-3">
                <button
                  onClick={() => setStage('setup')}
                  className="px-3 py-1.5 text-xs bg-neutral-900 dark:bg-neutral-100 text-white dark:text-neutral-900 rounded"
                >
                  New Test
                </button>
                <button
                  onClick={onClose}
                  className="px-3 py-1.5 text-xs text-neutral-500 hover:text-neutral-800"
                >
                  Close
                </button>
              </div>
            </div>
          )}

        </div>
      </div>
    </div>
  );
}
