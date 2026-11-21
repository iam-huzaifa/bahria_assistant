
from src.rag.retriever import get_retriever


# 1. Initialize retriever
retriever = get_retriever()


# 2. Ask a question
question = "Can I repeat a course if I get a low grade?"


# 3. Retrieve relevant documents
results = retriever.invoke(question)


# 4. Display results
print("\nQuestion:", question)
print("\nTotal retrieved chunks:", len(results))


for i, document in enumerate(results, start=1):

    print("\n" + "=" * 60)
    print(f"RESULT {i}")
    print("=" * 60)

    print("\nSource:", document.metadata.get("source"))
    print("Page:", document.metadata.get("page"))

    print("\nContent:")
    print(document.page_content)
