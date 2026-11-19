
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from src.utils.config import GOOGLE_API_KEY


def get_embedding_model():

    embedding_model = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        google_api_key=GOOGLE_API_KEY,
        output_dimensionality=768
    )

    return embedding_model