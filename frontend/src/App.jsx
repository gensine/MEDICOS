import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import PipelineVisualizer from './components/PipelineVisualizer';
import ChatInterface from './components/ChatInterface';
import FeatureCards from './components/FeatureCards';
import { ArrowRight, Sparkles, BookOpen, ShieldAlert } from 'lucide-react';

export default function App() {
  const [inputQuery, setInputQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState({
    vector_db_ready: false,
    ollama_ready: false,
    available_models: [],
    knowledge_base: 'The Gale Encyclopedia of Medicine'
  });

  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content: 'Hello! I am Medicos, your offline medical AI assistant. I answer questions by retrieving verified entries directly from The Gale Encyclopedia of Medicine. What medical topic or condition would you like to explore today?',
      sources: []
    }
  ]);

  // Fetch API status on load
  const fetchStatus = async () => {
    try {
      const res = await fetch('http://localhost:8000/api/status');
      if (res.ok) {
        const data = await res.json();
        setStatus(data);
      }
    } catch (err) {
      console.log('Backend not yet reachable on port 8000.');
    }
  };

  useEffect(() => {
    fetchStatus();
    const interval = setInterval(fetchStatus, 8000);
    return () => clearInterval(interval);
  }, []);

  const handleSendMessage = async (queryText) => {
    const text = queryText || inputQuery;
    if (!text.trim() || loading) return;

    // Append user message
    const newMessages = [...messages, { role: 'user', content: text, sources: [] }];
    setMessages(newMessages);
    setInputQuery('');
    setLoading(true);

    try {
      const res = await fetch('http://localhost:8000/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: text, model: 'llama3' })
      });

      if (!res.ok) {
        throw new Error(`Server returned error: ${res.statusText}`);
      }

      const data = await res.json();
      setMessages([...newMessages, {
        role: 'assistant',
        content: data.answer,
        sources: data.sources || []
      }]);
    } catch (err) {
      setMessages([...newMessages, {
        role: 'assistant',
        content: `⚠️ Note: The Python backend on http://localhost:8000 is still starting up or initializing. Ensure 'python backend/server.py' is running!`,
        sources: []
      }]);
    } finally {
      setLoading(false);
    }
  };

  const handleSelectSampleQuery = (sample) => {
    setInputQuery(sample);
    const chatEl = document.getElementById('chat');
    if (chatEl) {
      chatEl.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <div className="min-h-screen bg-[#08080a] text-zinc-100 flex flex-col relative overflow-hidden">
      {/* Ambient background glow matching user reference images */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[450px] bg-gradient-to-b from-[#ff4d28]/20 via-[#ff4d28]/5 to-transparent blur-[120px] pointer-events-none -z-0" />
      
      {/* Top Navigation */}
      <Navbar status={status} />

      <main className="flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-20 relative z-10 w-full">
        {/* Hero Section */}
        <div className="text-center max-w-3xl mx-auto mb-14">
          {/* Glowing Top Pill Badge matching reference screenshot */}
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-zinc-900/90 border border-[#ff4d28]/30 shadow-lg shadow-[#ff4d28]/10 text-xs font-semibold text-zinc-300 mb-6">
            <span className="w-2 h-2 rounded-full bg-[#ff4d28] animate-ping" />
            <span className="text-[#ff4d28] uppercase tracking-wider font-bold text-[10px]">NEW</span>
            <span className="text-zinc-500">•</span>
            <span>Local RAG + Ollama Medical Pipeline</span>
            <ArrowRight className="w-3.5 h-3.5 text-zinc-400" />
          </div>

          {/* Main Hero Headline */}
          <h1 className="text-3xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight text-white leading-[1.15]">
            Search, Verify and Understand <br />
            <span className="bg-gradient-to-r from-[#ff4d28] via-[#ff7a59] to-[#ffab91] bg-clip-text text-transparent">
              Medical Knowledge
            </span>{' '}
            in Seconds
          </h1>

          {/* Subtitle */}
          <p className="text-sm sm:text-base text-zinc-400 mt-5 leading-relaxed max-w-2xl mx-auto">
            A privacy-first clinical assistant grounded in <span className="text-zinc-200 font-semibold">The Gale Encyclopedia of Medicine</span>. Powered by LangChain, Meta FAISS vector search, and local Ollama inference.
          </p>

          {/* Hero CTAs */}
          <div className="flex items-center justify-center gap-4 mt-8">
            <a
              href="#chat"
              className="px-6 py-3 rounded-xl bg-gradient-to-r from-[#ff4d28] to-[#e03a16] text-white font-semibold text-xs sm:text-sm shadow-xl shadow-[#ff4d28]/30 hover:opacity-90 transition-all flex items-center gap-2"
            >
              <span>Get Started</span>
              <ArrowRight className="w-4 h-4" />
            </a>
            <a
              href="#pipeline"
              className="px-6 py-3 rounded-xl bg-zinc-900/80 hover:bg-zinc-800 text-zinc-300 border border-zinc-800 font-semibold text-xs sm:text-sm transition-all"
            >
              View Architecture
            </a>
          </div>
        </div>

        {/* Dual Interactive Workspace Container (Matching Screenshot 2) */}
        <section id="pipeline" className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch mb-20">
          <div className="lg:col-span-5 flex flex-col">
            <PipelineVisualizer status={status} onSelectSampleQuery={handleSelectSampleQuery} />
          </div>
          <div className="lg:col-span-7 flex flex-col">
            <ChatInterface
              inputQuery={inputQuery}
              setInputQuery={setInputQuery}
              onSendMessage={handleSendMessage}
              messages={messages}
              loading={loading}
            />
          </div>
        </section>

        {/* Technology Partner / Engine Badges */}
        <div className="py-8 border-y border-zinc-800/60 mb-8">
          <p className="text-center text-xs font-semibold text-zinc-400 uppercase tracking-widest mb-6">
            Powered By Leading Open-Source AI Infrastructure
          </p>
          <div className="flex flex-wrap items-center justify-center gap-8 sm:gap-14 text-zinc-400 text-xs sm:text-sm font-bold tracking-wider">
            <span className="hover:text-white transition-colors">LANGCHAIN</span>
            <span className="hover:text-white transition-colors">META FAISS</span>
            <span className="hover:text-white transition-colors">HUGGING FACE</span>
            <span className="hover:text-white transition-colors">OLLAMA</span>
            <span className="hover:text-white transition-colors">PYTORCH</span>
          </div>
        </div>

        {/* Category & Query Cards (Matching Screenshot 3) */}
        <FeatureCards onSelectSampleQuery={handleSelectSampleQuery} />
      </main>

      {/* Footer & Medical Advisory */}
      <footer className="border-t border-zinc-800/80 bg-[#0a0a0d] py-10 mt-auto">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-zinc-400">
            <div className="flex items-center gap-2">
              <ShieldAlert className="w-4 h-4 text-[#ff4d28]" />
              <span>
                <strong>Medical Advisory:</strong> For research and informational purposes only. Consult a licensed physician for clinical diagnosis.
              </span>
            </div>
            <span>© 2026 MEDICOS · RAG Assistant</span>
          </div>
        </div>
      </footer>
    </div>
  );
}
