# Medicos - Medical AI Chatbot

A private, offline Medical Assistant chatbot powered by **Retrieval-Augmented Generation (RAG)**. Built with **LangChain**, **FAISS Vector Database**, and **Ollama**, it provides context-grounded answers to medical queries by directly retrieving authoritative knowledge from *The Gale Encyclopedia of Medicine*.

---

## 📖 Overview

Standard Large Language Models often produce confident but factually incorrect statements—an issue known as *hallucination*, which can be dangerous in medical contexts. 

**Medicos** solves this by implementing a **Retrieval-Augmented Generation (RAG)** pipeline. Instead of relying purely on an LLM's parametric memory, Medicos:
1. Indexes medical literature into a local vector database.
2. Performs semantic similarity search on the user's question to extract only the most relevant verified excerpts.
3. Augments an LLM prompt with those excerpts so the model synthesizes an answer directly grounded in verified medical text.
4. Executes the entire pipeline locally using **Ollama**, ensuring complete medical data privacy and zero API costs.

---

## ✨ Key Features

- **Authoritative Grounding:** Answers are sourced directly from verified medical literature (*The Gale Encyclopedia of Medicine*).
- **Reduced Hallucinations:** Strict RAG prompting instructs the model to rely only on retrieved passages.
- **100% Local & Privacy-Preserving:** No patient queries or medical questions leave your machine; all inference is run locally via Ollama.
- **Sub-millisecond Retrieval:** Powered by Meta's FAISS (Facebook AI Similarity Search) index for high-speed similarity search across thousands of pages.
- **Modular Pipeline:** Built on LangChain, making it easy to swap embedding models, vector stores, or LLM backends.

---

## 🏛️ System Architecture

The project is split into two core phases: **Indexing (Offline Pipeline)** and **Retrieval & Generation (Online Pipeline)**.

```
═══════════════════════════════════════════════════════════════════════════
                     PHASE 1: DOCUMENT INDEXING PIPELINE
═══════════════════════════════════════════════════════════════════════════

   [Medical PDF Source]
   data/The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND.pdf
            │
            ▼
   [Document Ingestion] ──── LangChain PyPDFLoader / DirectoryLoader
            │
            ▼
   [Text Splitting] ──────── LangChain RecursiveCharacterTextSplitter
            │                 (Splits into semantically coherent overlapping chunks)
            ▼
   [Embedding Model] ─────── HuggingFace Embeddings (e.g., sentence-transformers)
            │                 (Converts text chunks into dense mathematical vectors)
            ▼
   [Vector Database] ─────── Meta FAISS (Facebook AI Similarity Search)
                              (Stores vectors & chunk text locally in vectorstore/db_faiss)

═══════════════════════════════════════════════════════════════════════════
                 PHASE 2: RETRIEVAL & GENERATION PIPELINE (RAG)
═══════════════════════════════════════════════════════════════════════════

   User Query: "What are the symptoms and treatments of Diabetes Mellitus?"
            │
            ▼
   [Query Embedding] ─────── Encoded with identical HuggingFace embedding model
            │
            ▼
   [Similarity Search] ───── FAISS Vector Database finds Top-K relevant text chunks
            │
            ▼
   [Context Augmentation] ── Combines retrieved medical excerpts + user query
            │                 into a structured system prompt template
            ▼
   [Local LLM] ───────────── Ollama (LLaMA 3 / Mistral / BioMistral / Meditron)
            │                 (Synthesizes the answer based strictly on the context)
            ▼
   Accurate, Context-Grounded Medical Answer
```

### Detailed Pipeline Components:

1. **Document Loading (`PyPDFLoader` & `DirectoryLoader`):**  
   Reads and parses pages from high-volume medical reference documents stored in `data/`.
2. **Text Chunking (`RecursiveCharacterTextSplitter`):**  
   Splits large medical documents into smaller, overlapping segments (e.g., 500-1000 tokens with 50-100 token overlap). Overlap preserves continuity and context across page boundaries.
3. **Dense Vector Embeddings (`HuggingFaceEmbeddings`):**  
   Translates each text chunk into high-dimensional vector representations capturing semantic meaning.
4. **Vector Storage & Indexing (`FAISS`):**  
   Indexes the vectors for ultra-fast cosine or L2 similarity queries, persisted locally on disk without requiring a cloud database.
5. **Retrieval-Augmented Generation (`LangChain RetrievalQA` / `LCEL`):**  
   Retrieves the top matching passages when a query is received and feeds them alongside a specialized medical prompt to the generator.
6. **Local Generation (`Ollama`):**  
   Executes open-weight foundation models locally, preventing data leakage and guaranteeing offline availability.

---

## 🛠️ Tech Stack

| Technology | Purpose | Description |
| :--- | :--- | :--- |
| **LangChain** | Framework Orchestration | Coordinates loaders, splitters, vector stores, prompt templates, and LLM chains. |
| **RAG** | Architecture Strategy | Bridges external reference knowledge to the generative model to eliminate hallucinations. |
| **FAISS** | Vector Database | Meta's similarity search engine used to store and retrieve dense vector embeddings. |
| **Hugging Face** | Embedding Generation | Pre-trained transformer models (e.g., `sentence-transformers/all-MiniLM-L6-v2`) for embeddings. |
| **Ollama** | Local LLM Engine | Efficient local inference server running models such as LLaMA 3, Mistral, or BioMistral. |
| **PyPDF** | PDF Parsing | Extracts text and structure from medical PDF documents. |

---

## 📂 Project Directory Structure

```
MEDICOS/
├── data/
│   └── The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND.pdf   # Source medical encyclopedia
├── vectorstore/
│   └── db_faiss/                                      # Persisted FAISS vector index & metadata
├── cmfllm.py                                          # Document ingestion, chunking & vector DB creation
├── main.py / app.py                                   # Chatbot interface & RAG query execution pipeline
├── requirements.txt                                   # Python project dependencies
└── README.md                                          # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites

- **Python 3.10+**
- **Ollama**: Download and install from [ollama.com](https://ollama.com/)

### 2. Set Up Virtual Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/MEDICOS.git
cd MEDICOS

# Create and activate a virtual environment
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On Linux/macOS:
source .venv/bin/activate
```

### 3. Install Required Dependencies

Create or update your `requirements.txt`:
```txt
langchain
langchain-community
langchain-huggingface
sentence-transformers
faiss-cpu
pypdf
```

Install them:
```bash
pip install -r requirements.txt
```

### 4. Pull and Start a Model in Ollama

Open a terminal and pull your preferred model:
```bash
# General purpose high-performance model
ollama run llama3

# Or Mistral:
ollama run mistral
```

Make sure the Ollama background daemon is running (`http://localhost:11434`).

### 5. Build the Vector Database

Run the ingestion script to process the medical PDF, chunk the text, compute embeddings, and build the local FAISS index:

```bash
python cmfllm.py
```
> *Note: Depending on the size of the medical encyclopedia and whether you are using a GPU or CPU, generating embeddings may take several minutes on the initial run.*

### 6. Run the Chatbot

Start the interactive terminal or web interface:

```bash
python main.py
```

---

## ⚠️ Medical Disclaimer

> **IMPORTANT:** This project is intended for educational, informational, and research purposes only. It is **not** a diagnostic tool and does not provide formal medical advice, diagnosis, or treatment recommendations. Always consult a qualified physician or healthcare professional for medical concerns or emergency care.
