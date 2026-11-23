
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.embeddings import Embeddings

from src.utils.config import GOOGLE_API_KEY


class GeminiRetrievalEmbeddings(Embeddings):

    def __init__(self):

        self.model = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-001",
            google_api_key=GOOGLE_API_KEY,
            output_dimensionality=768
        )

    def embed_documents(self, texts):

        return self.model.embed_documents(
            texts,
            task_type="RETRIEVAL_DOCUMENT"
        )

    def embed_query(self, text):

        return self.model.embed_query(
            text,
            task_type="RETRIEVAL_QUERY"
        )


def get_embedding_model():

    return GeminiRetrievalEmbeddings()
