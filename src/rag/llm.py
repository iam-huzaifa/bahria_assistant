
from langchain_google_genai import ChatGoogleGenerativeAI
from src.utils.config import GOOGLE_API_KEY


def get_llm():

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.2,
        max_retries=2
    )

    return llm
