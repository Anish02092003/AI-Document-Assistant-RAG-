from flask import Flask, render_template, request
import io

from src.document_loader import load_pdf
from src.chunking import chunk_text
from src.embeddings import embed_texts
from src.rag_pipeline import answer_query

app = Flask(__name__)


DOCUMENT_CHUNKS = []
DOCUMENT_EMBEDDINGS = None


@app.route("/", methods=["GET", "POST"])
def home():
    global DOCUMENT_CHUNKS, DOCUMENT_EMBEDDINGS

    answer = None
    error = None

    if request.method == "POST":

        
        if "pdf" in request.files and request.files["pdf"].filename != "":
            try:
                pdf_file = request.files["pdf"]
                pdf_bytes = io.BytesIO(pdf_file.read())

                text = load_pdf(pdf_bytes)
                DOCUMENT_CHUNKS = chunk_text(text)
                DOCUMENT_EMBEDDINGS = embed_texts(DOCUMENT_CHUNKS)

            except Exception as e:
                error = str(e)

        
        if "question" in request.form and DOCUMENT_EMBEDDINGS is not None:
            try:
                question = request.form["question"]
                answer = answer_query(
                    question,
                    DOCUMENT_CHUNKS,
                    DOCUMENT_EMBEDDINGS
                )
            except Exception as e:
                error = str(e)

    return render_template(
        "index.html",
        answer=answer,
        error=error,
        ready=DOCUMENT_EMBEDDINGS is not None
    )


if __name__ == "__main__":
    app.run(debug=True)

