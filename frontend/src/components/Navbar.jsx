import React from 'react';
import { Activity, ShieldCheck, Database, Cpu } from 'lucide-react';

export default function Navbar({ status }) {
  return (
    <header className="sticky top-0 z-50 backdrop-blur-xl bg-[#0a0a0d]/80 border-b border-zinc-800/60">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        {/* Brand */}
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-[#ff4d28] to-[#ff7a59] flex items-center justify-center shadow-lg shadow-[#ff4d28]/30">
            <Activity className="w-5 h-5 text-white stroke-[2.5]" />
          </div>
          <div className="flex flex-col">
            <span className="font-extrabold tracking-tight text-lg text-white">
              MEDICOS<span className="text-[#ff4d28]">.AI</span>
            </span>
            <span className="text-[10px] text-zinc-500 font-medium -mt-1 tracking-wider uppercase">
              Clinical RAG Assistant
            </span>
          </div>
        </div>

        {/* Center Links */}
        <nav className="hidden md:flex items-center gap-8 text-sm font-medium text-zinc-400">
          <a href="#pipeline" className="hover:text-white transition-colors">Architecture</a>
          <a href="#chat" className="hover:text-white transition-colors">Clinical Chat</a>
          <a href="#features" className="hover:text-white transition-colors">Knowledge Base</a>
          <a href="https://github.com/gensine/MEDICOS" target="_blank" rel="noreferrer" className="hover:text-white transition-colors">GitHub</a>
        </nav>

        {/* System Status Indicators & Action */}
        <div className="flex items-center gap-3">
          <div className="hidden sm:flex items-center gap-2 px-3 py-1.5 rounded-full bg-zinc-900/90 border border-zinc-800 text-xs">
            <div className={`w-2 h-2 rounded-full ${status.vector_db_ready ? 'bg-emerald-500 animate-pulse' : 'bg-amber-500'}`} />
            <span className="text-zinc-400 font-medium">
              {status.vector_db_ready ? 'FAISS Ready' : 'FAISS Index Pending'}
            </span>
          </div>

          <div className="hidden sm:flex items-center gap-2 px-3 py-1.5 rounded-full bg-zinc-900/90 border border-zinc-800 text-xs">
            <div className={`w-2 h-2 rounded-full ${status.ollama_ready ? 'bg-emerald-500 animate-pulse' : 'bg-zinc-600'}`} />
            <span className="text-zinc-400 font-medium">
              {status.ollama_ready ? 'Ollama Online' : 'Ollama Standby'}
            </span>
          </div>

          <a 
            href="#chat" 
            className="px-4 py-2 rounded-xl text-xs font-semibold text-white bg-gradient-to-r from-[#ff4d28] to-[#e03a16] shadow-md shadow-[#ff4d28]/25 hover:opacity-90 transition-all flex items-center gap-1.5"
          >
            Launch Chat
          </a>
        </div>
      </div>
    </header>
  );
}
