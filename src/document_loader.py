import PyPDF2
from PyPDF2.errors import PdfReadError
from pdf2image import convert_from_bytes
import pytesseract

# Windows path (adjust if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def load_pdf(file_bytes):
    """
    Loads text from:
    - text-based PDFs
    - scanned PDFs (OCR fallback)
    """

    # ---------- Try text extraction ----------
    try:
        reader = PyPDF2.PdfReader(file_bytes)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "

        if text.strip():
            return text

    except PdfReadError:
        pass
    except Exception:
        pass

    # ---------- OCR fallback ----------
    try:
        images = convert_from_bytes(file_bytes.getvalue())
        ocr_text = ""

        for img in images:
            ocr_text += pytesseract.image_to_string(img)

        if ocr_text.strip():
            return ocr_text

        raise ValueError("OCR failed: No readable text")

    except Exception:
        raise ValueError("Unable to extract text from PDF")
