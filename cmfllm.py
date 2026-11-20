import os
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DATA_PATH = "data/"
DB_FAISS_PATH = "vectorstore/db_faiss"

def load_pdf_files(data_path):
    print(f"Loading PDF files from '{data_path}'...")
    loader = DirectoryLoader(data_path, glob='*.pdf', loader_cls=PyPDFLoader)
    documents = loader.load()
    print(f"Loaded {len(documents)} pages from PDF(s).")
    return documents

def create_chunks(documents, chunk_size=500, chunk_overlap=50):
    print("Splitting documents into text chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    text_chunks = text_splitter.split_documents(documents)
    print(f"Created {len(text_chunks)} text chunks.")
    return text_chunks

def get_embedding_model(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    print(f"Loading embedding model: {model_name}...")
    snapshot = os.path.expanduser('~/.cache/huggingface/hub/models--sentence-transformers--all-MiniLM-L6-v2/snapshots/1110a243fdf4706b3f48f1d95db1a4f5529b4d41')
    target_model = snapshot if os.path.exists(snapshot) else model_name
    embeddings = HuggingFaceEmbeddings(
        model_name=target_model,
        model_kwargs={'device': 'cpu'}
    )
    return embeddings

def build_vector_db():
    # 1. Load documents
    documents = load_pdf_files(DATA_PATH)
    if not documents:
        print("No documents found in data folder!")
        return None

    # 2. Chunk documents
    text_chunks = create_chunks(documents)

    # 3. Load embedding model
    embeddings = get_embedding_model()

    # 4. Create and save FAISS vector store
    print("Building FAISS vector database (this may take a few minutes)...")
    os.makedirs(os.path.dirname(DB_FAISS_PATH), exist_ok=True)
    db = FAISS.from_documents(text_chunks, embeddings)
    db.save_local(DB_FAISS_PATH)
    print(f"FAISS vector store successfully saved to: {DB_FAISS_PATH}")
    return db

if __name__ == "__main__":
    build_vector_db()
