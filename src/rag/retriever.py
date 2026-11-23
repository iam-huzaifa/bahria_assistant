
from src.rag.vector_store import get_vector_store

def get_retriever():

    # Connect to our existing Supabase vector store
    vector_store = get_vector_store()

    # Configure similarity search
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 5
        }
    )

    return retriever
