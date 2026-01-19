import subprocess


def generate_answer(query, retrieved_chunks):
    """
    Calls Ollama running on HOST machine.
    Windows-safe subprocess handling.
    """

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are a document assistant.
Answer the question ONLY using the information below.
If the answer is not present, say:
"The document does not contain this information."

DOCUMENT CONTEXT:
{context}

QUESTION:
{query}

ANSWER:
"""

    result = subprocess.run(
        ["ollama", "run", "phi3"],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8",   # ✅ force UTF-8 decoding
        errors="ignore"     # ✅ ignore invalid bytes
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result.stdout.strip()
