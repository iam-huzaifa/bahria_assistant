from pathlib import Path
import pymupdf
from langchain_core.documents import Document


def load_pdf(pdf_path):
    """
    Extract text from a PDF and return LangChain Documents.

    Each page becomes a separate Document.
    Page numbers are preserved in metadata.
    """

    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(
            f"PDF file not found: {pdf_path}"
        )

    documents = []

    pdf = pymupdf.open(pdf_path)

    try:
        total_pages = len(pdf)

        for page_number, page in enumerate(pdf, start=1):

            page_text = page.get_text("text").strip()

            # Skip pages containing no extractable text.
            if not page_text:
                continue

            document = Document(
                page_content=page_text,
                metadata={
                    "source": pdf_path.name,
                    "page": page_number,
                    "total_pages": total_pages
                }
            )

            documents.append(document)

    finally:
        pdf.close()

    if not documents:
        raise ValueError(
            "No extractable text found in this PDF."
        )

    return documents