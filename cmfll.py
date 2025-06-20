from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

## Uncomment the following files if you're not using pipenv as your virtual environment manager
#from dotenv import load_dotenv, find_dotenv
#load_dotenv(find_dotenv())


# Step 1: Load raw PDF(s)
DATA_PATH="data/"
def load_pdf_files(data):
    loader = DirectoryLoader(data,
                             glob='*.pdf',
                             loader_cls=PyPDFLoader)
    
    documents=loader.load()
    return documents

documents=load_pdf_files(data=DATA_PATH)
#print("Length of PDF pages: ", len(documents))


