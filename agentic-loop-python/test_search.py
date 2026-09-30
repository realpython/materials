"""Test suite for the vector similarity search module."""

import pytest

from search import (
    cosine_similarity,
    load_vectors,
    search_similar,
)


def test_identical_vectors():
    vec = [1.0, 2.0, 3.0]
    assert cosine_similarity(vec, vec) == pytest.approx(1.0)


def test_orthogonal_vectors():
    vec_a = [1.0, 0.0]
    vec_b = [0.0, 1.0]
    assert cosine_similarity(vec_a, vec_b) == pytest.approx(0.0)


def test_zero_vector():
    vec = [1.0, 2.0, 3.0]
    zero = [0.0, 0.0, 0.0]
    result = cosine_similarity(vec, zero)
    assert result == 0.0


def test_search_returns_top_k():
    stored = load_vectors(count=50, dimensions=8)
    query = stored[0]
    results = search_similar(query, stored, top_k=3)
    assert len(results) == 3
    assert results[0][0] == 0
