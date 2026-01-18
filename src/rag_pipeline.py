from src.embeddings import embed_texts
from src.vector_store import VectorStore
from src.llm import generate_answer


def answer_query(query, chunks, embeddings):
    """
    Full RAG flow:
    - Embed query
    - Retrieve relevant chunks
    - Generate grounded answer
    """

    store = VectorStore(embedding_dim=embeddings.shape[1])
    store.add(embeddings, chunks)

    query_embedding = embed_texts([query])
    retrieved_chunks = store.search(query_embedding, top_k=3)

    answer = generate_answer(query, retrieved_chunks)

    return answer
