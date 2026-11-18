import React, { useState } from 'react';
import { FileText, Cpu, Database, CheckCircle2, ChevronRight, Layers, Sparkles } from 'lucide-react';

export default function PipelineVisualizer({ status, onSelectSampleQuery }) {
  const [activeTab, setActiveTab] = useState('pipeline');
  const [activeStep, setActiveStep] = useState(1);

  const steps = [
    {
      id: 1,
      title: 'Ingest & Chunk',
      desc: 'LangChain splits The Gale Encyclopedia (20MB) into 500-char semantic chunks.',
      icon: FileText,
      tag: 'Preprocessing',
      status: 'Ready'
    },
    {
      id: 2,
      title: 'FAISS Vector Database',
      desc: 'HuggingFace MiniLM converts chunks into 384-dimensional dense vectors.',
      icon: Database,
      tag: 'Meta FAISS',
      status: status.vector_db_ready ? 'Indexed' : 'Building'
    },
    {
      id: 3,
      title: 'Ollama Local LLM',
      desc: 'Local Llama3/Mistral synthesizes responses using only retrieved medical passages.',
      icon: Cpu,
      tag: '100% Private',
      status: status.ollama_ready ? 'Connected' : 'Standby'
    }
  ];

  return (
    <div className="bg-[#121217]/90 border border-zinc-800/80 rounded-2xl p-6 backdrop-blur-xl flex flex-col justify-between shadow-2xl relative overflow-hidden group">
      {/* Subtle background card glow */}
      <div className="absolute -top-24 -left-24 w-48 h-48 bg-[#ff4d28]/10 rounded-full blur-3xl pointer-events-none" />

      <div>
        {/* Tab switch matching user reference image */}
        <div className="flex items-center justify-between mb-6">
          <div className="flex p-1 bg-zinc-900/90 border border-zinc-800/90 rounded-xl">
            <button
              onClick={() => setActiveTab('pipeline')}
              className={`px-4 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                activeTab === 'pipeline'
                  ? 'bg-zinc-800 text-white shadow-sm'
                  : 'text-zinc-400 hover:text-zinc-200'
              }`}
            >
              Pipeline
            </button>
            <button
              onClick={() => setActiveTab('specs')}
              className={`px-4 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                activeTab === 'specs'
                  ? 'bg-zinc-800 text-white shadow-sm'
                  : 'text-zinc-400 hover:text-zinc-200'
              }`}
            >
              Components
            </button>
          </div>

          <span className="text-[11px] font-medium text-[#ff4d28] bg-[#ff4d28]/10 border border-[#ff4d28]/20 px-2.5 py-1 rounded-full flex items-center gap-1">
            <Sparkles className="w-3 h-3" /> Zero Hallucination
          </span>
        </div>

        {activeTab === 'pipeline' ? (
          <div className="space-y-3 relative">
            {/* Connector line */}
            <div className="absolute left-[27px] top-6 bottom-6 w-[2px] bg-gradient-to-b from-zinc-700 via-[#ff4d28]/40 to-zinc-800 -z-0" />

            {steps.map((step) => {
              const Icon = step.icon;
              const isSelected = activeStep === step.id;
              return (
                <div
                  key={step.id}
                  onClick={() => setActiveStep(step.id)}
                  className={`relative z-10 flex items-start gap-4 p-3.5 rounded-xl border transition-all cursor-pointer ${
                    isSelected
                      ? 'bg-zinc-900/90 border-[#ff4d28]/40 shadow-lg shadow-[#ff4d28]/5'
                      : 'bg-zinc-950/40 border-zinc-800/60 hover:border-zinc-700/80 hover:bg-zinc-900/40'
                  }`}
                >
                  <div
                    className={`w-9 h-9 rounded-xl flex items-center justify-center shrink-0 border transition-all ${
                      isSelected
                        ? 'bg-[#ff4d28] border-[#ff4d28] text-white shadow-md shadow-[#ff4d28]/30'
                        : 'bg-zinc-900 border-zinc-800 text-zinc-400'
                    }`}
                  >
                    <Icon className="w-4 h-4" />
                  </div>

                  <div className="flex-1 min-w-0">
                    <div className="flex items-center justify-between">
                      <h4 className="text-sm font-semibold text-white tracking-tight">{step.title}</h4>
                      <span className="text-[10px] font-medium text-zinc-400 px-2 py-0.5 rounded-md bg-zinc-800/80 border border-zinc-700/50">
                        {step.tag}
                      </span>
                    </div>
                    <p className="text-xs text-zinc-400 mt-1 leading-relaxed">{step.desc}</p>
                  </div>
                </div>
              );
            })}
          </div>
        ) : (
          <div className="space-y-3 text-xs text-zinc-300">
            <div className="p-3.5 rounded-xl bg-zinc-900/50 border border-zinc-800/80">
              <span className="text-zinc-500 uppercase tracking-wider text-[10px] block font-semibold">Knowledge Source</span>
              <p className="font-semibold text-white mt-0.5">The Gale Encyclopedia of Medicine (2nd Edition)</p>
              <p className="text-zinc-400 mt-1">4,000+ medical topics, symptoms, causes, and treatments indexed.</p>
            </div>
            <div className="p-3.5 rounded-xl bg-zinc-900/50 border border-zinc-800/80">
              <span className="text-zinc-500 uppercase tracking-wider text-[10px] block font-semibold">Vector Index</span>
              <p className="font-semibold text-white mt-0.5">Meta FAISS (IndexFlatL2)</p>
              <p className="text-zinc-400 mt-1">Local dense vector similarity search with sub-5ms latency.</p>
            </div>
            <div className="p-3.5 rounded-xl bg-zinc-900/50 border border-zinc-800/80">
              <span className="text-zinc-500 uppercase tracking-wider text-[10px] block font-semibold">Inference Engine</span>
              <p className="font-semibold text-white mt-0.5">Ollama (Llama 3 / Mistral)</p>
              <p className="text-zinc-400 mt-1">Zero data leaks. Fully offline-capable clinical chat.</p>
            </div>
          </div>
        )}
      </div>

      {/* Quick Prompts at the bottom */}
      <div className="mt-6 pt-4 border-t border-zinc-800/60">
        <span className="text-[11px] font-semibold text-zinc-400 uppercase tracking-wider block mb-2">
          Try Clinical Queries:
        </span>
        <div className="flex flex-wrap gap-1.5">
          {[
            'Symptoms of Acute Bronchitis',
            'Complications of Type 2 Diabetes',
            'Hypertension treatment protocol'
          ].map((sample, idx) => (
            <button
              key={idx}
              onClick={() => onSelectSampleQuery(sample)}
              className="text-xs text-zinc-300 hover:text-white bg-zinc-900/80 hover:bg-zinc-800 border border-zinc-800 px-2.5 py-1 rounded-lg transition-colors text-left"
            >
              {sample}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
