import pickle
import numpy as np
import faiss

from sentence_transformers import (
    SentenceTransformer
)

# Load model
model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

# Load FAISS index
index = faiss.read_index(
    "data/legal_index.faiss"
)

# Load dataset
with open(
    "data/legal_data.pkl",
    "rb"
) as f:

    legal_data = pickle.load(f)

def retrieve_legal_context(query):

    query_embedding = model.encode(
        [query]
    )

    query_embedding = np.array(
        query_embedding,
        dtype=np.float32
    )

    distances, indices = index.search(
        query_embedding,
        1
    )

    best_match = legal_data[
        indices[0][0]
    ]

    return best_match["answer"]