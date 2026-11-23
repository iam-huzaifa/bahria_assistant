
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.rag.retriever import get_retriever
from src.rag.llm import get_llm


def get_rag_chain():

    retriever = get_retriever()
    llm = get_llm()

    prompt = ChatPromptTemplate.from_template("""
    You are Bahria Assistant AI, an assistant for Bahria University students.

    Answer the student's question using ONLY the provided context.

    Rules:
    1. Do not invent university policies or information.
    2. If the answer is not available in the context, clearly say that
       the handbook does not provide enough information.
    3. Use simple and clear English.
    4. Include the handbook page number in your answer.
    5. If multiple pages support the answer, mention all relevant pages.

    Context:
    {context}

    Student Question:
    {question}

    Answer:
    """)

    def format_documents(documents):

        formatted_context = ""

        for document in documents:

            page = document.metadata.get("page", "Unknown")
            source = document.metadata.get("source", "Unknown")

            formatted_context += f"""
            Source: {source}
            Page: {page}

            Content:
            {document.page_content}

            -------------------------
            """

        return formatted_context

    def answer_question(question):

        documents = retriever.invoke(question)

        context = format_documents(documents)

        response = (
            prompt
            | llm
            | StrOutputParser()
        ).invoke({
            "context": context,
            "question": question
        })

        return {
            "answer": response,
            "sources": documents
        }

    return answer_question
