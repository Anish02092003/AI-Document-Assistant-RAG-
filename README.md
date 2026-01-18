✅ PART 1: README.md (RAG PROJECT)

Copy-paste this as README.md in your project root.

📄 AI Document Assistant (RAG – Fully Local)
🔹 Overview

This project is a Retrieval-Augmented Generation (RAG) based AI application that allows users to upload PDF documents and ask questions about their content.
The system retrieves relevant document sections using semantic search and generates grounded answers using a local LLM, completely free of external APIs.

🚀 Key Features

📄 Upload text-based or scanned PDFs (OCR supported)

✂️ Smart document chunking with overlap

🧠 Semantic search using embeddings + FAISS

🤖 Local LLM inference using Ollama (no API cost)

💬 Question-answering grounded strictly in documents

🌐 Flask-based web interface

🧠 Tech Stack

Python

Flask

SentenceTransformers

FAISS

Ollama (Mistral / Phi-3)

PyPDF2 + Tesseract OCR

🏗️ Project Architecture
PDF → Text Extraction → Chunking
     → Embeddings → FAISS Vector Store
     → Retrieve Top-K Chunks
     → Local LLM → Answer

▶️ How to Run
pip install -r requirements.txt
python app.py


Open:

http://127.0.0.1:5000

🧠 Interview Highlight

“I built a fully local RAG-based document assistant using FAISS and a local LLM, avoiding API costs while ensuring grounded responses.”

📌 Future Improvements

Chat history memory

Multiple document support

Docker deployment

Source citations per answer
