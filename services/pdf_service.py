import fitz  # PyMuPDF


def extract_text_from_pdf(uploaded_file):
    """
    Extract text and statistics from a PDF file.

    Returns:
        dict:
            text
            pages
            words
            characters
            reading_time
    """

    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    full_text = ""

    for page in pdf:
        full_text += page.get_text()

    pages = len(pdf)
    words = len(full_text.split())
    characters = len(full_text)
    reading_time = max(1, words // 200)

    pdf.close()

    return {
        "text": full_text,
        "pages": pages,
        "words": words,
        "characters": characters,
        "reading_time": reading_time,
    }