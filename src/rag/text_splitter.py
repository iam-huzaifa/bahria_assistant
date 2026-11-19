
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):

    """
    Divide extracted PDF documents into smaller chunks.
    Original metadata such as source and page is preserved.
    """

    if not documents:
        raise ValueError("No documents provided for splitting.")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=120,
        add_start_index=True
    )

    chunks = text_splitter.split_documents(documents)

    if not chunks:
        raise ValueError("No chunks were generated.")

    return chunks