import os
from dotenv import load_dotenv

load_dotenv()

# Files and folders
DOCS_PATH = os.getenv("DOCS_PATH", "./documents")
CHROMA_PATH = os.getenv("CHROMA_PATH", "./chroma_db")
CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION", "unofficial_guide")

# Embedding model
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
N_RESULTS = int(os.getenv("N_RESULTS", "5"))

# LLM configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "llama-3.3-70b-versatile")
