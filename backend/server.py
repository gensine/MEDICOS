import os
import requests
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FAISS_PATH = os.path.join(BASE_DIR, "vectorstore", "db_faiss")
DATA_PATH = os.path.join(BASE_DIR, "data")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

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
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
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
            context_text = "\n\n".join([d.page_content for d in docs])
        except Exception as e:
            print(f"Error during FAISS similarity search: {e}")

    rag_active = len(sources) > 0

    # 2. Prompt Engineering for Medical Accuracy
    prompt = f"""You are Medicos, a specialized clinical AI assistant. Use the following retrieved medical context from The Gale Encyclopedia of Medicine to provide an accurate, clear, and professional response to the user's query.

If the answer is not contained in the context, state honestly that the specific detail is not found in the encyclopedia, but provide helpful verified general medical knowledge with an explicit disclaimer.

Context:
{context_text if context_text else 'No specific context retrieved.'}

User Query:
{query}

Answer:"""

    # 3. Call Ollama Generation
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
            timeout=60
        )
        if ollama_resp.status_code == 200:
            answer = ollama_resp.json().get("response", "").strip()
        else:
            answer = f"Ollama returned status code {ollama_resp.status_code}. Make sure model '{model_name}' is pulled."
    except requests.exceptions.ConnectionError:
        # Graceful fallback explaining that Ollama is offline but showing retrieved RAG excerpts
        if rag_active:
            answer = (
                f"**[RAG Retrieval Succeeded - Ollama is Offline]**\n\n"
                f"We retrieved **{len(sources)} verified medical passages** from *The Gale Encyclopedia of Medicine* matching your query: '{query}'.\n\n"
                f"To synthesize answers locally with a generative LLM, please start Ollama (`ollama run {model_name}`).\n\n"
                f"**Retrieved Medical Excerpts:**\n" +
                "\n\n".join([f"- *Page {s.page or 'N/A'}*: {s.content}" for s in sources])
            )
        else:
            answer = (
                "Ollama is currently unreachable at http://localhost:11434 and the vector index has not been built yet. "
                "Please run `python cmfllm.py` to index the medical encyclopedia, and start Ollama via `ollama run llama3`."
            )

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
