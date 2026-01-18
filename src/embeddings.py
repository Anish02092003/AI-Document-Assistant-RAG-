from sentence_transformers import SentenceTransformer
import numpy as np

# Load once (important)
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_texts(texts):
    """
    Converts list of texts to embeddings
    """
    embeddings = model.encode(texts)
    return np.array(embeddings)
