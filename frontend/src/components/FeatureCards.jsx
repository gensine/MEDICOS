import React from 'react';
import { Check, ShieldAlert, Stethoscope, Pill, ArrowUpRight } from 'lucide-react';

export default function FeatureCards({ onSelectSampleQuery }) {
  const cards = [
    {
      title: 'Symptom & Etiology',
      tag: 'Diagnostics',
      desc: 'Accurately cross-references patient symptoms against encyclopedic medical entries.',
      icon: Stethoscope,
      sampleQuery: 'What are the early warning symptoms and causes of Hepatitis B?',
      features: [
        'Differential symptoms mapping',
        'Pathology & risk factors',
        'Direct citation to Gale Medicine Encyclopedia'
      ]
    },
    {
      title: 'Treatments & Therapeutics',
      tag: 'Clinical Care',
      desc: 'Retrieves standard pharmacological interventions and established treatment guidelines.',
      icon: Pill,
      sampleQuery: 'What are standard treatment protocols for Acute Bronchitis?',
      highlight: true,
      features: [
        'First-line pharmacological options',
        'Alternative supportive therapies',
        'Verified medical literature grounding'
      ]
    },
    {
      title: 'Complications & Warnings',
      tag: 'Critical Triage',
      desc: 'Highlights critical red-flag symptoms and severe physiological complications.',
      icon: ShieldAlert,
      sampleQuery: 'What are the severe complications of Type 2 Diabetes Mellitus?',
      features: [
        'Red-flag symptom detection',
        'Long-term physiological complications',
        'Strict hallucination-free protocol'
      ]
    }
  ];

  return (
    <section id="features" className="py-16">
      <div className="text-center max-w-2xl mx-auto mb-12">
        <span className="text-[11px] font-bold text-[#ff4d28] uppercase tracking-widest bg-[#ff4d28]/10 border border-[#ff4d28]/20 px-3 py-1 rounded-full">
          Comprehensive Clinical Capabilities
        </span>
        <h2 className="text-2xl sm:text-3xl font-extrabold text-white mt-3 tracking-tight">
          Grounded In Clinical Literature
        </h2>
        <p className="text-sm text-zinc-400 mt-2">
          Every response is derived exclusively from verified medical sources to maintain clinical integrity.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {cards.map((card, idx) => {
          const Icon = card.icon;
          return (
            <div
              key={idx}
              className={`rounded-2xl p-6 flex flex-col justify-between transition-all duration-300 relative overflow-hidden ${
                card.highlight
                  ? 'bg-[#15151b] border-2 border-[#ff4d28]/60 shadow-xl shadow-[#ff4d28]/10'
                  : 'bg-[#121217]/90 border border-zinc-800/80 hover:border-zinc-700/80 shadow-lg'
              }`}
            >
              {card.highlight && (
                <div className="absolute top-0 right-0 bg-[#ff4d28] text-white text-[10px] font-bold px-3 py-0.5 rounded-bl-lg uppercase tracking-wider">
                  Most Queried
                </div>
              )}

              <div>
                <div className="flex items-center justify-between mb-4">
                  <div className={`w-10 h-10 rounded-xl flex items-center justify-center ${
                    card.highlight ? 'bg-[#ff4d28] text-white shadow-md shadow-[#ff4d28]/30' : 'bg-zinc-900 text-zinc-300 border border-zinc-800'
                  }`}>
                    <Icon className="w-5 h-5" />
                  </div>
                  <span className="text-xs font-semibold text-zinc-400 bg-zinc-900 border border-zinc-800 px-2.5 py-1 rounded-md">
                    {card.tag}
                  </span>
                </div>

                <h3 className="text-lg font-bold text-white tracking-tight">{card.title}</h3>
                <p className="text-xs text-zinc-400 mt-2 leading-relaxed">{card.desc}</p>

                <div className="mt-6 pt-5 border-t border-zinc-800/60 space-y-2.5">
                  <span className="text-[11px] font-bold text-zinc-400 uppercase tracking-wider block">
                    Capabilities:
                  </span>
                  {card.features.map((feat, fIdx) => (
                    <div key={fIdx} className="flex items-center gap-2 text-xs text-zinc-300">
                      <div className="w-4 h-4 rounded-full bg-emerald-500/10 text-emerald-400 flex items-center justify-center shrink-0 border border-emerald-500/20">
                        <Check className="w-2.5 h-2.5 stroke-[3]" />
                      </div>
                      <span>{feat}</span>
                    </div>
                  ))}
                </div>
              </div>

              <div className="mt-6 pt-4">
                <button
                  onClick={() => onSelectSampleQuery(card.sampleQuery)}
                  className={`w-full py-2.5 px-4 rounded-xl text-xs font-bold transition-all flex items-center justify-center gap-1.5 ${
                    card.highlight
                      ? 'bg-gradient-to-r from-[#ff4d28] to-[#e03a16] text-white shadow-lg shadow-[#ff4d28]/20 hover:opacity-95'
                      : 'bg-zinc-900 hover:bg-zinc-800 text-zinc-200 border border-zinc-800'
                  }`}
                >
                  <span>Query This Topic</span>
                  <ArrowUpRight className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>
          );
        })}
      </div>
    </section>
  );
}
