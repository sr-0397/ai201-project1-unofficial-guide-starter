from ingest import chunk_document, load_documents
from generator import generate_response
from retrieve import embed_and_store, retrieve


def ingest_documents():
    """Load documents, chunk them, and embed the chunks into ChromaDB."""
    documents = load_documents()
    all_chunks = []
    for doc in documents:
        chunks = chunk_document(doc["text"], doc["game"])
        all_chunks.extend(chunks)

    if not all_chunks:
        raise RuntimeError("No chunks were created during ingestion. Check your documents folder and chunking logic.")

    embed_and_store(all_chunks)
    return len(all_chunks)


def ask(question):
    """Answer a question by retrieving relevant chunks and generating a grounded response."""
    retrieved_chunks = retrieve(question)
    answer = generate_response(question, retrieved_chunks)

    sources = []
    for chunk in retrieved_chunks:
        source = chunk.get("game") or "unknown"
        if source not in sources:
            sources.append(source)

    return {
        "answer": answer,
        "sources": sources,
        "retrieved_chunks": retrieved_chunks,
    }


if __name__ == "__main__":
    print("Ingesting documents into ChromaDB...")
    count = ingest_documents()
    print(f"Ingested {count} chunks into the vector store.")

    test_queries = [
        "What is the list of freshman year dorms?",
        "How many dining halls are there?"
    ]

    for query in test_queries:
        print(f"\nQUERY: {query}")
        results = retrieve(query)
        if not results:
            print("No results returned.")
            continue
        for i, chunk in enumerate(results, start=1):
            print(f"{i}. [{chunk['game']}] dist={chunk['distance']:.4f}: {chunk['text'][:200].strip()}\n")
