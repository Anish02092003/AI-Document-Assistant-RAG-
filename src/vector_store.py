import faiss
import numpy as np


class VectorStore:
    def __init__(self, embedding_dim):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.texts = []

    def add(self, embeddings, texts):
        self.index.add(embeddings)
        self.texts.extend(texts)

    def search(self, query_embedding, top_k=3):
        distances, indices = self.index.search(query_embedding, top_k)
        results = [self.texts[i] for i in indices[0]]
        return results
