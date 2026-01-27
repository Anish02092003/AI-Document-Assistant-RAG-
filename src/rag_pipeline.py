from src.embeddings import embed_texts
from src.vector_store import VectorStore
from src.llm import generate_answer

ANSWER_CACHE = {}

VECTOR_STORE = None


def answer_query(query, chunks, embeddings, history=None):
    """
    Full RAG flow:
    - Inject chat history
    - Embed query
    - Retrieve relevant chunks
    - Generate grounded answer
    """

    global VECTOR_STORE


    if history:
        recent_history = "\n".join(history[-6:])
        query = recent_history + "\nUser: " + query

    
    cache_key = query.lower().strip()
    if cache_key in ANSWER_CACHE:
        return ANSWER_CACHE[cache_key]

    
    if VECTOR_STORE is None:
        VECTOR_STORE = VectorStore(embedding_dim=embeddings.shape[1])
        VECTOR_STORE.add(embeddings, chunks)

    
    query_embedding = embed_texts([query])
    retrieved_chunks = VECTOR_STORE.search(query_embedding, top_k=2)

    
    retrieved_chunks = [c[:800] for c in retrieved_chunks]

    
    answer = generate_answer(query, retrieved_chunks)

    
    ANSWER_CACHE[cache_key] = answer

    return answer

