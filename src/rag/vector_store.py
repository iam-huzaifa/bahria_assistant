
from supabase import create_client
from langchain_community.vectorstores import SupabaseVectorStore

from src.utils.config import (
    SUPABASE_URL,
    SUPABASE_SERVICE_ROLE_KEY
)

from src.rag.embeddings import get_embedding_model


def get_vector_store():

    # Connect to Supabase
    supabase_client = create_client(
        SUPABASE_URL,
        SUPABASE_SERVICE_ROLE_KEY
    )

    # Initialize Gemini embeddings
    embedding_model = get_embedding_model()

    # Connect LangChain with Supabase pgvector
    vector_store = SupabaseVectorStore(
        client=supabase_client,
        embedding=embedding_model,
        table_name="documents",
        query_name="match_documents"
    )

    return vector_store
