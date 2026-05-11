import json
import pickle
import numpy as np
import faiss

from sentence_transformers import (
    SentenceTransformer
)

model = SentenceTransformer(
    'paraphrase-MiniLM-L3-v2'
)

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

embeddings = model.encode(
    questions
)

embeddings = np.array(
    embeddings,
    dtype=np.float32
)
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(embeddings)

faiss.write_index(
    index,
    "data/legal_index.faiss"
)

with open(
    "data/legal_data.pkl",
    "wb"
) as f:

    pickle.dump(data, f)

print(
    "Embeddings generated successfully!"
)