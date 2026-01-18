import io
from src.document_loader import load_pdf
from src.chunking import chunk_text
from src.embeddings import embed_texts
from src.rag_pipeline import answer_query

# Load document
with open("data/documents/sample.pdf", "rb") as f:
    file_bytes = io.BytesIO(f.read())

text = load_pdf(file_bytes)
chunks = chunk_text(text)
embeddings = embed_texts(chunks)

# Ask question
query = "What machine learning techniques are discussed?"

answer = answer_query(query, chunks, embeddings)

print("\nANSWER:\n")
print(answer)
