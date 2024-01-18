import faiss, os, json
import unicodedata as ud
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import time


model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
)

BASE_DIR = os.path.dirname(__file__)


index = faiss.read_index("src/core/pnst.index")


with open("src/core/index_to_ids.json", "r", encoding="utf8") as f:
    index_to_ids = json.load(f)


def search(query, top_k):
    t = time.time()
    query_vector = model.encode([query])
    rates, top_k = index.search(query_vector, top_k)
    rates = rates[0]

    rates = [100 * float(rate) // 10 for rate in rates]

    print(">>>> Results in Total Time: {}".format(time.time() - t))
    top_k_ids = top_k.tolist()[0]
    top_k_ids = list(np.unique(top_k_ids))
    results = [
        {"id": index_to_ids[str(idx)], "rate": rate}
        for idx, rate in zip(top_k_ids, rates)
    ]

    return results


def compare_vectors(source, target):
    source_vectors = model.encode(source)
    target_vector = model.encode(target)

    source_vectors = np.array(source_vectors)
    print(
        "shapeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
        source_vectors.shape,
        target_vector.shape,
    )

    # Calculate cosine similarity for each pair of source and target paragraphs
    similarity_scores = [
        cosine_similarity([source_vector], [target_vector])[0][0]
        for source_vector in source_vectors.tolist()
    ]

    return similarity_scores
