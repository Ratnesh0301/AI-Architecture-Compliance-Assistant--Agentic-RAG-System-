def retrieve_context(vectordb, query):
    docs = vectordb.similarity_search(query, k=3)
    return "\n".join([d.page_content for d in docs])