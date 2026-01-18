import io
from src.document_loader import load_pdf
from src.chunking import chunk_text

with open("data/documents/sample.pdf", "rb") as f:
    file_bytes = io.BytesIO(f.read())

text = load_pdf(file_bytes)
chunks = chunk_text(text)

print("Total chunks:", len(chunks))
print("\nFirst chunk:\n")
print(chunks[0])
