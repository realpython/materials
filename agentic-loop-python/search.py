import random


def cosine_similarity(vec_a, vec_b):
    """Return cosine similarity between two vectors."""
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    mag_a = sum(a**2 for a in vec_a) ** 0.5
    mag_b = sum(b**2 for b in vec_b) ** 0.5
    return dot / (mag_a * mag_b)


def load_vectors(count=500, dimensions=128):
    """Generate random vectors for the demo."""
    random.seed(42)
    return [
        [random.uniform(-1, 1) for _ in range(dimensions)]
        for _ in range(count)
    ]


def search_similar(query, stored, top_k=5):
    """Find the top_k most similar vectors to query."""
    scores = []
    for i, candidate in enumerate(stored):
        score = cosine_similarity(query, candidate)
        scores.append((i, score))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_k]
