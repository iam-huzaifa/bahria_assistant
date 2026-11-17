from src.rag.document_loader import load_pdf

pdf_path = "data/documents/bahria_handbook_spring_2026.pdf"

documents = load_pdf(pdf_path)

print("PDF loaded successfully!")
print("Total extracted pages:", len(documents))

print("\nFirst document metadata:")
print(documents[0].metadata)

print("\nFirst 500 characters:")
print(documents[0].page_content[:500])