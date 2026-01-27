import io
from src.document_loader import load_pdf
from src.chunking import chunk_text
from src.embeddings import embed_texts
from src.vector_store import VectorStore


with open("data/documents/sample.pdf", "rb") as f:
    file_bytes = io.BytesIO(f.read())

text = load_pdf(file_bytes)
chunks = chunk_text(text)

embeddings = embed_texts(chunks)

store = VectorStore(embedding_dim=embeddings.shape[1])
store.add(embeddings, chunks)

query = "machine learning model deployment"
query_embedding = embed_texts([query])

results = store.search(query_embedding, top_k=3)

print("\nTop relevant chunks:\n")
for i, r in enumerate(results, 1):
    print(f"--- Result {i} ---")
    print(r[:300])
    print()

