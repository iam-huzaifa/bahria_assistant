
import time

from src.rag.document_loader import load_pdf
from src.rag.text_splitter import split_documents
from src.rag.vector_store import get_vector_store


# 1. Load handbook
pdf_path = "data/documents/bahria_handbook_spring_2026.pdf"

documents = load_pdf(pdf_path)

print("Documents loaded:", len(documents))


# 2. Split handbook into chunks
chunks = split_documents(documents)

print("Total chunks:", len(chunks))


# 3. Connect to Supabase vector store
vector_store = get_vector_store()


# 4. Process chunks in small batches
BATCH_SIZE = 50
WAIT_TIME = 65

total_chunks = len(chunks)

for start in range(0, total_chunks, BATCH_SIZE):

    end = min(start + BATCH_SIZE, total_chunks)

    # Select 5 chunks
    batch = chunks[start:end]

    print(f"\nProcessing chunks {start + 1} to {end}...")

    # Generate embeddings and store in Supabase
    vector_store.add_documents(batch)

    print(f"Successfully stored {end}/{total_chunks} chunks!")

    # Wait before processing the next batch
    if end < total_chunks:
        print(f"Waiting {WAIT_TIME} seconds...")
        time.sleep(WAIT_TIME)


print("\nHandbook successfully stored in Supabase!")
