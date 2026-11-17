
from src.rag.document_loader import load_pdf
from src.rag.text_splitter import split_documents


pdf_path = "data/documents/bahria_handbook_spring_2026.pdf"

# Step 1: Load PDF
documents = load_pdf(pdf_path)

print("Original documents:", len(documents))


# Step 2: Split documents
chunks = split_documents(documents)

print("Total chunks generated:", len(chunks))


# Step 3: Inspect first chunk
print("\n5th chunk:")
print(chunks[5].page_content)

print("\n5th chunk metadata:")
print(chunks[5].metadata)


# Step 4: Inspect chunk size
print("\n5th chunk character count:")
print(len(chunks[5].page_content))