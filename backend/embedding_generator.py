import json
import pickle
import numpy as np
import faiss

from sentence_transformers import (
    SentenceTransformer
)

# Load lightweight model
model = SentenceTransformer(
    'paraphrase-MiniLM-L3-v2'
)

# Load dataset
with open(
    "data/legal_dataset.json",
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)

questions = [
    item["question"]
    for item in data
]

# Generate embeddings
embeddings = model.encode(
    questions
)

embeddings = np.array(
    embeddings,
    dtype=np.float32
)

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(embeddings)

# Save FAISS index
faiss.write_index(
    index,
    "data/legal_index.faiss"
)

# Save dataset
with open(
    "data/legal_data.pkl",
    "wb"
) as f:

    pickle.dump(data, f)

print(
    "Embeddings generated successfully!"
)