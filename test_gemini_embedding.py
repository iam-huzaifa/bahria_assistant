
from src.rag.document_loader import load_pdf
from src.rag.text_splitter import split_documents
from src.rag.embeddings import get_embedding_model


# 1. Load the handbook
pdf_path = "data/documents/bahria_handbook_spring_2026.pdf"

documents = load_pdf(pdf_path)
print("Total PDF pages loaded:", len(documents))


# 2. Split into chunks
chunks = split_documents(documents)
print("Total chunks:", len(chunks))


# 3. Initialize Gemini embedding model
embedding_model = get_embedding_model()


# 4. Generate document embeddings
sample_chunks = chunks[:3]

document_vectors = embedding_model.embed_documents(
    [chunk.page_content for chunk in sample_chunks],
    task_type="RETRIEVAL_DOCUMENT"
)


# 5. Generate query embedding
question = "Can I repeat a course if I get a low grade?"

question_vector = embedding_model.embed_query(
    question,
    task_type="RETRIEVAL_QUERY"
)


# 6. Display results
print("\nDocument embeddings generated:", len(document_vectors))
print("Document vector dimensions:", len(document_vectors[0]))
print("Question vector dimensions:", len(question_vector))

print("\nFirst 10 values of document vector:")
print(document_vectors[0][:10])

print("\nGemini embedding test successful!")
