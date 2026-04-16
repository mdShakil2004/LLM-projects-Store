import faiss
import numpy as np
from embeddings import get_embedding

class Retriever:
    def __init__(self, documents):
        self.documents = documents
        self.doc_embeddings = np.array([get_embedding(doc) for doc in documents])

        dimension = self.doc_embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(self.doc_embeddings)

    def search(self, query, k=3):
        query_vec = get_embedding(query).reshape(1, -1)
        distances, indices = self.index.search(query_vec, k)

        return [self.documents[i] for i in indices[0]]