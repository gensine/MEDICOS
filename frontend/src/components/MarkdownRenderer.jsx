import React from 'react';

/**
 * Lightweight, zero-dependency Markdown & Rich Text Renderer for Medicos
 * Accurately formats **bold**, *italics*, headers (##, ###), bullet lists,
 * numbered steps, and special RAG status banners.
 */
export default function MarkdownRenderer({ content, className = '' }) {
  if (!content) return null;

  // Split lines
  const lines = content.split('\n');

  const renderFormattedText = (text) => {
    // Process bold (**text** or __text__)
    const parts = [];
    let remaining = text;
    let keyIdx = 0;

    // Regex for bold, italics, code
    const tokenRegex = /(\*\*[^*]+\*\*|__[^_]+__|`[^`]+`|\*[^*]+\*|_[^_]+_)/g;
    let lastIndex = 0;
    let match;

    while ((match = tokenRegex.exec(text)) !== null) {
      // Text before match
      if (match.index > lastIndex) {
        parts.push(text.substring(lastIndex, match.index));
      }

      const token = match[0];
      if (token.startsWith('**') && token.endsWith('**')) {
        parts.push(
          <strong key={keyIdx++} className="font-bold text-white tracking-wide">
            {token.slice(2, -2)}
          </strong>
        );
      } else if (token.startsWith('__') && token.endsWith('__')) {
        parts.push(
          <strong key={keyIdx++} className="font-bold text-white underline decoration-[#ff4d28]/60 underline-offset-2">
            {token.slice(2, -2)}
          </strong>
        );
      } else if (token.startsWith('`') && token.endsWith('`')) {
        parts.push(
          <code key={keyIdx++} className="px-1.5 py-0.5 rounded bg-zinc-800 text-[#ff4d28] font-mono text-[11px] border border-zinc-700/60">
            {token.slice(1, -1)}
          </code>
        );
      } else if ((token.startsWith('*') && token.endsWith('*')) || (token.startsWith('_') && token.endsWith('_'))) {
        parts.push(
          <em key={keyIdx++} className="italic text-zinc-300">
            {token.slice(1, -1)}
          </em>
        );
      }

      lastIndex = tokenRegex.lastIndex;
    }

    if (lastIndex < text.length) {
      parts.push(text.substring(lastIndex));
    }

    return parts;
  };

  const renderedElements = [];
  let inList = false;
  let listItems = [];
  let listType = 'bullet'; // or 'number'

  const flushList = () => {
    if (listItems.length > 0) {
      if (listType === 'number') {
        renderedElements.push(
          <ol key={`ol-${renderedElements.length}`} className="list-decimal pl-5 space-y-1.5 my-2 text-zinc-300">
            {listItems.map((item, idx) => (
              <li key={idx} className="leading-relaxed pl-1">
                {renderFormattedText(item)}
              </li>
            ))}
          </ol>
        );
      } else {
        renderedElements.push(
          <ul key={`ul-${renderedElements.length}`} className="space-y-1.5 my-2">
            {listItems.map((item, idx) => (
              <li key={idx} className="flex items-start gap-2 text-zinc-300 leading-relaxed">
                <span className="w-1.5 h-1.5 rounded-full bg-[#ff4d28] shrink-0 mt-2 shadow-[0_0_6px_#ff4d28]" />
                <span className="flex-1">{renderFormattedText(item)}</span>
              </li>
            ))}
          </ul>
        );
      }
      listItems = [];
      inList = false;
    }
  };

  for (let i = 0; i < lines.length; i++) {
    const rawLine = lines[i];
    const line = rawLine.trim();

    // Check for RAG Alert Notice
    if (line.includes('[RAG Retrieval Succeeded - Ollama is Offline]') || line.includes('[Ollama Offline]')) {
      flushList();
      renderedElements.push(
        <div key={`alert-${i}`} className="p-3 my-2.5 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-200 text-xs flex items-start gap-2.5 shadow-sm">
          <span className="w-2 h-2 rounded-full bg-amber-400 shrink-0 mt-1.5 animate-pulse" />
          <div>
            <span className="font-semibold text-amber-300 block">RAG Retrieval Active &bull; Ollama Synthesis Standby</span>
            <span className="text-zinc-300 text-[11px] mt-0.5 block">
              Verified clinical excerpts retrieved from <em>The Gale Encyclopedia of Medicine</em> below:
            </span>
          </div>
        </div>
      );
      continue;
    }

    // Headers
    if (line.startsWith('### ')) {
      flushList();
      renderedElements.push(
        <h4 key={`h4-${i}`} className="text-sm font-bold text-white mt-3.5 mb-1.5 tracking-tight flex items-center gap-1.5">
          <span className="w-1.5 h-3.5 rounded bg-[#ff4d28]" />
          {renderFormattedText(line.substring(4))}
        </h4>
      );
      continue;
    }
    if (line.startsWith('## ')) {
      flushList();
      renderedElements.push(
        <h3 key={`h3-${i}`} className="text-base font-bold text-white mt-4 mb-2 pb-1 border-b border-zinc-800 tracking-tight flex items-center gap-2">
          {renderFormattedText(line.substring(3))}
        </h3>
      );
      continue;
    }
    if (line.startsWith('# ')) {
      flushList();
      renderedElements.push(
        <h2 key={`h2-${i}`} className="text-lg font-extrabold text-white mt-4 mb-2 tracking-tight">
          {renderFormattedText(line.substring(2))}
        </h2>
      );
      continue;
    }

    // Numbered list (e.g. "1. ")
    const numMatch = line.match(/^(\d+)\.\s+(.*)/);
    if (numMatch) {
      if (!inList || listType !== 'number') {
        flushList();
        inList = true;
        listType = 'number';
      }
      listItems.push(numMatch[2]);
      continue;
    }

    // Bullet list (e.g. "- " or "* ")
    if (line.startsWith('- ') || line.startsWith('* ')) {
      if (!inList || listType !== 'bullet') {
        flushList();
        inList = true;
        listType = 'bullet';
      }
      listItems.push(line.substring(2));
      continue;
    }

    // Regular line / Paragraph
    if (line === '') {
      flushList();
      // Empty line adds natural spacing
      continue;
    }

    flushList();
    renderedElements.push(
      <p key={`p-${i}`} className="my-1.5 text-zinc-200 leading-relaxed text-xs sm:text-sm">
        {renderFormattedText(rawLine)}
      </p>
    );
  }

  flushList();

  return <div className={`space-y-1 ${className}`}>{renderedElements}</div>;
}
