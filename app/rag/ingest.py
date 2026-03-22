from langchain_classic.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings()

def create_vector_db(documents):
    vectordb = Chroma.from_texts(documents, embedding)
    return vectordb