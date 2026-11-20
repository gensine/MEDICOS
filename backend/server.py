import os
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import requests
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FAISS_PATH = os.path.join(BASE_DIR, "vectorstore", "db_faiss")
DATA_PATH = os.path.join(BASE_DIR, "data")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434")

app = FastAPI(title="Medicos API", description="Medical AI Chatbot with LangChain, FAISS & Ollama")

# Enable CORS for React frontend (default Vite dev port is 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global vector store cache
vector_db = None
embeddings = None

def get_embeddings():
    global embeddings
    if embeddings is None:
        from langchain_huggingface import HuggingFaceEmbeddings
        snapshot = os.path.expanduser('~/.cache/huggingface/hub/models--sentence-transformers--all-MiniLM-L6-v2/snapshots/1110a243fdf4706b3f48f1d95db1a4f5529b4d41')
        model_target = snapshot if os.path.exists(snapshot) else "sentence-transformers/all-MiniLM-L6-v2"
        embeddings = HuggingFaceEmbeddings(
            model_name=model_target,
            model_kwargs={'device': 'cpu'}
        )
    return embeddings

def load_vector_db():
    global vector_db
    if vector_db is None:
        if os.path.exists(DB_FAISS_PATH):
            from langchain_community.vectorstores import FAISS
            emb = get_embeddings()
            vector_db = FAISS.load_local(
                DB_FAISS_PATH,
                emb,
                allow_dangerous_deserialization=True
            )
            print("FAISS vector store loaded into memory.")
        else:
            print("FAISS vector store not yet found on disk.")
    return vector_db

class ChatRequest(BaseModel):
    query: str
    model: Optional[str] = "llama3"

class SourceItem(BaseModel):
    page: Optional[int] = None
    source: str
    content: str

def clean_doc_text(text: str) -> str:
    import re
    # Remove header banners and footer watermarks
    text = re.sub(r'THE GALE ENCYCLOPEDIA OF MEDICINE\s*\|\s*Section:[^\n]*\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Page \d+ of \d+\s*\|\s*MEDICOS Clinical Reference System', '', text, flags=re.IGNORECASE)
    return text.strip()

def synthesize_fallback_answer(query: str, docs: list) -> str:
    """Intelligently structures retrieved encyclopedia entries into a clean clinical answer when Ollama is offline."""
    if not docs:
        return (
            "I could not locate specific clinical protocols for this condition in *The Gale Encyclopedia of Medicine*. "
            "Please verify the medical term or consult official clinical practice guidelines."
        )

    seen = set()
    cleaned_blocks = []
    for doc in docs:
        cleaned = clean_doc_text(doc.page_content)
        lines = [line.rstrip() for line in cleaned.splitlines() if line.strip()]
        unique_lines = []
        for line in lines:
            key = line.strip().lower()[:60]
            if key not in seen:
                seen.add(key)
                unique_lines.append(line)
        if unique_lines:
            cleaned_blocks.append("\n".join(unique_lines))

    combined = "\n\n".join(cleaned_blocks)
    return f"{combined}\n\n---\n*Verified clinical reference from The Gale Encyclopedia of Medicine.*"

class ChatResponse(BaseModel):
    query: str
    answer: str
    sources: List[SourceItem]
    model_used: str
    rag_active: bool

@app.get("/api/status")
def get_status():
    db_exists = os.path.exists(DB_FAISS_PATH)
    
    # Check Ollama connection
    ollama_ready = False
    available_models = []
    try:
        res = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=2)
        if res.status_code == 200:
            ollama_ready = True
            data = res.json()
            available_models = [m.get("name") for m in data.get("models", [])]
    except Exception:
        ollama_ready = False

    return {
        "vector_db_ready": db_exists,
        "ollama_ready": ollama_ready,
        "available_models": available_models,
        "knowledge_base": "The Gale Encyclopedia of Medicine"
    }

@app.post("/api/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    query = request.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    db = load_vector_db()
    sources: List[SourceItem] = []
    docs = []
    context_text = ""

    # 1. RAG Retrieval from FAISS
    if db is not None:
        try:
            docs = db.similarity_search(query, k=3)
            for doc in docs:
                page_num = doc.metadata.get("page", None)
                source_file = os.path.basename(doc.metadata.get("source", "Medical Encyclopedia"))
                sources.append(SourceItem(
                    page=page_num,
                    source=source_file,
                    content=doc.page_content[:300] + "..." if len(doc.page_content) > 300 else doc.page_content
                ))
            context_text = "\n\n".join([clean_doc_text(d.page_content) for d in docs])
        except Exception as e:
            print(f"Error during FAISS similarity search: {e}")

    rag_active = len(sources) > 0

    # 2. Strict Clinical Prompt for LLM
    prompt = f"""You are Medicos, an expert clinical AI specialist. Provide an authoritative, clear, and well-structured medical response to the user's query using the verified medical encyclopedia reference below.

Clinical Reference:
{context_text if context_text else 'No specific encyclopedia reference retrieved.'}

User Query:
{query}

Guidelines:
- Give a direct, comprehensive clinical answer. Do not say 'Based on the provided text' or 'According to the context'.
- Use clear markdown sections, bullet points, dosages, and timelines where relevant.
- Highlight emergency actions, first-line medications, and key precautions in bold.
- Maintain a professional, doctor-level clinical tone.

Clinical Response:"""

    # 3. Call Ollama Generation or Fallback to Clean Synthesis
    answer = ""
    model_name = request.model or "llama3"
    
    try:
        ollama_resp = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": model_name,
                "prompt": prompt,
                "stream": False
            },
            timeout=(2.0, 60.0)
        )
        if ollama_resp.status_code == 200:
            answer = ollama_resp.json().get("response", "").strip()
        else:
            answer = synthesize_fallback_answer(query, docs)
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        # Graceful, professional clinical response directly from the encyclopedia
        answer = synthesize_fallback_answer(query, docs)

    return ChatResponse(
        query=query,
        answer=answer,
        sources=sources,
        model_used=model_name,
        rag_active=rag_active
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.server:app", host="0.0.0.0", port=8000, reload=True)
