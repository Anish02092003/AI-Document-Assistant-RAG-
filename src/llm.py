import subprocess
import shutil


def generate_answer(query, retrieved_chunks):
    """
    Generate a grounded answer using a LOCAL LLM via Ollama.
    """

    # Ensure ollama exists
    ollama_path = shutil.which("ollama")
    if not ollama_path:
        raise RuntimeError(
            "Ollama not found in PATH. "
            "Please install Ollama and restart your terminal."
        )

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
        [ollama_path, "run", "mistral"],
        input=prompt,
        text=True,
        capture_output=True,
        encoding="utf-8"
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result.stdout.strip()
