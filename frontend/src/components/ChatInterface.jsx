import React, { useState, useRef, useEffect } from 'react';
import { Send, Bot, User, BookOpen, AlertCircle, Sparkles, Loader2, RefreshCw, Mic, MicOff } from 'lucide-react';
import MarkdownRenderer from './MarkdownRenderer';

export default function ChatInterface({ inputQuery, setInputQuery, onSendMessage, messages, loading }) {
  const [showSources, setShowSources] = useState({});
  const [isListening, setIsListening] = useState(false);
  const [speechSupported, setSpeechSupported] = useState(true);
  const recognitionRef = useRef(null);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, loading]);

  // Voice to text (Web Speech API) setup
  useEffect(() => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (SpeechRecognition) {
      const recognition = new SpeechRecognition();
      recognition.continuous = false;
      recognition.interimResults = true;
      recognition.lang = 'en-US';

      recognition.onstart = () => {
        setIsListening(true);
      };

      recognition.onresult = (event) => {
        let transcript = '';
        for (let i = 0; i < event.results.length; i++) {
          transcript += event.results[i][0].transcript;
        }
        if (transcript) {
          setInputQuery(transcript);
        }
      };

      recognition.onerror = (event) => {
        console.warn('Speech recognition error:', event.error);
        setIsListening(false);
      };

      recognition.onend = () => {
        setIsListening(false);
      };

      recognitionRef.current = recognition;
    } else {
      setSpeechSupported(false);
    }

    return () => {
      if (recognitionRef.current) {
        recognitionRef.current.abort();
      }
    };
  }, [setInputQuery]);

  const toggleListening = () => {
    if (!speechSupported) {
      alert('Voice-to-Text is not supported by your current browser. Please try Chrome, Edge, or Safari.');
      return;
    }

    if (isListening) {
      recognitionRef.current?.stop();
      setIsListening(false);
    } else {
      try {
        recognitionRef.current?.start();
      } catch (err) {
        console.warn('Speech recognition start failed:', err);
      }
    }
  };

  const toggleSources = (index) => {
    setShowSources(prev => ({ ...prev, [index]: !prev[index] }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!inputQuery.trim() || loading) return;
    onSendMessage(inputQuery);
  };

  return (
    <div id="chat" className="bg-[#121217]/90 border border-zinc-800/80 rounded-2xl flex flex-col h-[560px] shadow-2xl backdrop-blur-xl relative overflow-hidden">
      {/* Top Header bar with glowing icon matching user reference screenshot 2 */}
      <div className="px-5 py-4 border-b border-zinc-800/80 bg-zinc-950/60 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-[#ff4d28] flex items-center justify-center text-white shadow-md shadow-[#ff4d28]/30 font-bold text-xs">
            M
          </div>
          <div>
            <h3 className="text-sm font-bold text-white tracking-tight flex items-center gap-2">
              Medicos Clinical RAG Chat
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            </h3>
            <p className="text-[11px] text-zinc-400">Grounded in The Gale Encyclopedia of Medicine</p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <span className="text-[10px] font-semibold tracking-wider text-zinc-400 bg-zinc-900 border border-zinc-800 px-2 py-1 rounded-md">
            MODEL: LLAMA3
          </span>
        </div>
      </div>

      {/* Messages Viewport */}
      <div className="flex-1 overflow-y-auto p-5 space-y-4">
        {messages.map((msg, idx) => {
          const isUser = msg.role === 'user';
          return (
            <div key={idx} className={`flex gap-3 ${isUser ? 'justify-end' : 'justify-start'}`}>
              {!isUser && (
                <div className="w-8 h-8 rounded-xl bg-zinc-800 border border-zinc-700/80 flex items-center justify-center shrink-0 text-[#ff4d28]">
                  <Bot className="w-4 h-4" />
                </div>
              )}

              <div className={`max-w-[85%] space-y-2 ${isUser ? 'items-end' : 'items-start'}`}>
                <div
                  className={`p-3.5 rounded-2xl text-xs sm:text-sm leading-relaxed ${
                    isUser
                      ? 'bg-gradient-to-r from-[#ff4d28] to-[#e03a16] text-white rounded-tr-sm shadow-md shadow-[#ff4d28]/20'
                      : 'bg-zinc-900/90 text-zinc-200 border border-zinc-800/80 rounded-tl-sm shadow-sm'
                  }`}
                >
                  {isUser ? (
                    <p className="whitespace-pre-line">{msg.content}</p>
                  ) : (
                    <MarkdownRenderer content={msg.content} />
                  )}
                </div>

                {/* Source Citations Drawer for AI responses */}
                {!isUser && msg.sources && msg.sources.length > 0 && (
                  <div className="mt-1">
                    <button
                      onClick={() => toggleSources(idx)}
                      className="text-[11px] font-medium text-zinc-400 hover:text-white flex items-center gap-1.5 py-1 px-2.5 rounded-lg bg-zinc-900/60 border border-zinc-800/60 hover:bg-zinc-800 transition-colors"
                    >
                      <BookOpen className="w-3 h-3 text-[#ff4d28]" />
                      <span>{msg.sources.length} Verified Citations from Gale Encyclopedia</span>
                    </button>

                    {showSources[idx] && (
                      <div className="mt-2 space-y-2 p-3 bg-zinc-950/80 border border-zinc-800/80 rounded-xl text-xs">
                        {msg.sources.map((src, sIdx) => (
                          <div key={sIdx} className="border-l-2 border-[#ff4d28] pl-2.5 py-1">
                            <span className="font-semibold text-zinc-300 text-[11px] block">
                              Source: {src.source} {src.page ? `(Page ${src.page})` : ''}
                            </span>
                            <p className="text-zinc-400 text-[11px] mt-0.5 leading-relaxed italic">
                              "{src.content}"
                            </p>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                )}
              </div>

              {isUser && (
                <div className="w-8 h-8 rounded-xl bg-zinc-800 border border-zinc-700/80 flex items-center justify-center shrink-0 text-zinc-300">
                  <User className="w-4 h-4" />
                </div>
              )}
            </div>
          );
        })}

        {loading && (
          <div className="flex gap-3 items-center text-xs text-zinc-400 bg-zinc-900/40 p-3 rounded-xl border border-zinc-800/60 w-fit">
            <Loader2 className="w-4 h-4 animate-spin text-[#ff4d28]" />
            <span>Searching FAISS vector database & generating answer with Ollama...</span>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Input Box with Voice-to-Text */}
      <form onSubmit={handleSubmit} className="p-3.5 bg-zinc-950/80 border-t border-zinc-800/80 flex flex-col gap-2 relative">
        {isListening && (
          <div className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-[#ff4d28]/10 border border-[#ff4d28]/30 w-fit text-xs text-[#ff4d28] animate-pulse">
            <span className="w-2 h-2 rounded-full bg-[#ff4d28] shadow-[0_0_8px_#ff4d28]" />
            <span className="font-medium text-[11px]">Listening to your voice... Speak your question now</span>
          </div>
        )}

        <div className="flex items-center gap-2">
          <input
            type="text"
            value={inputQuery}
            onChange={(e) => setInputQuery(e.target.value)}
            placeholder={isListening ? "Listening... speak now..." : "Ask a medical question (or click the microphone to speak)..."}
            className="flex-1 bg-zinc-900/90 border border-zinc-800 text-zinc-100 text-xs sm:text-sm rounded-xl px-4 py-2.5 focus:outline-none focus:border-[#ff4d28]/70 focus:ring-1 focus:ring-[#ff4d28]/70 transition-all placeholder:text-zinc-500"
          />

          {/* Voice to text Mic Button */}
          <button
            type="button"
            onClick={toggleListening}
            title={isListening ? "Listening... Click to stop" : "Voice-to-Text: Click to speak your question"}
            className={`p-2.5 rounded-xl border transition-all flex items-center justify-center shrink-0 ${
              isListening
                ? 'bg-[#ff4d28] text-white border-[#ff4d28] shadow-[0_0_15px_rgba(255,77,40,0.6)] animate-pulse'
                : 'bg-zinc-900/90 text-zinc-400 hover:text-white border-zinc-800 hover:border-zinc-700 hover:bg-zinc-800'
            }`}
          >
            {isListening ? <MicOff className="w-4 h-4 text-white" /> : <Mic className="w-4 h-4" />}
          </button>

          {/* Ask Button */}
          <button
            type="submit"
            disabled={loading || !inputQuery.trim()}
            className="px-4 py-2.5 rounded-xl bg-gradient-to-r from-[#ff4d28] to-[#e03a16] text-white font-medium text-xs sm:text-sm shadow-md shadow-[#ff4d28]/25 hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center gap-1.5 shrink-0"
          >
            <span>Ask</span>
            <Send className="w-3.5 h-3.5" />
          </button>
        </div>
      </form>
    </div>
  );
}
