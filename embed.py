# embed.py
from sentence_transformers import SentenceTransformer
import chromadb
from ingest import load_documents, chunk_document

def build_vector_store():
    # 1. Load your model (runs locally, no API key)
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # 2. Set up ChromaDB (local, persistent)
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection("unofficial_guide")

    # 3. Load and chunk all your documents
    documents = load_documents()
    all_chunks = []
    for doc in documents:
        chunks = chunk_document(doc["text"], doc["game"])
        all_chunks.extend(chunks)

    # 4. Embed and store
    texts = [c["text"] for c in all_chunks]
    embeddings = model.encode(texts).tolist()   # returns a numpy array; .tolist() for Chroma

    collection.add(
        ids=[c["chunk_id"] for c in all_chunks],
        embeddings=embeddings,
        documents=texts,
        metadatas=[{"game": c["game"]} for c in all_chunks]  # stored alongside each vector
    )

    print(f"Stored {len(all_chunks)} chunks in ChromaDB.")
    return collection