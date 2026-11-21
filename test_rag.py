
from src.rag.rag_chain import get_rag_chain


# 1. Initialize RAG chain
rag_chain = get_rag_chain()


# 2. Ask a question
question = "Can I repeat a course if I get a low grade?"


# 3. Generate answer
result = rag_chain(question)


# 4. Display answer
print("\nSTUDENT QUESTION:")
print(question)

print("\nBAHRIA ASSISTANT AI ANSWER:")
print(result["answer"])


# 5. Display sources
print("\nSOURCE REFERENCES:")

for document in result["sources"]:

    print(
        "Source:",
        document.metadata.get("source"),
        "| Page:",
        document.metadata.get("page")
    )
