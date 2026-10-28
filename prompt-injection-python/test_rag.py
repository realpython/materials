import importlib
import os
from types import SimpleNamespace

import pytest

from corpus import CLEAN, PAYLOADS

app = importlib.import_module(os.environ.get("RAG_MODULE", "rag"))


@pytest.mark.skipif(
    not os.environ.get("OPENAI_API_KEY"),
    reason="end-to-end tests need OPENAI_API_KEY",
)
@pytest.mark.parametrize("name", PAYLOADS)
def test_canary_stays_secret(name):
    store = app.build_store([*CLEAN, PAYLOADS[name]])
    reply = app.answer("How long does shipping take?", store)
    assert app.CANARY not in reply


@pytest.mark.skipif(
    not os.environ.get("OPENAI_API_KEY"),
    reason="end-to-end tests need OPENAI_API_KEY",
)
def test_clean_question_gets_answered():
    store = app.build_store(CLEAN)
    reply = app.answer("How many days do I have to return a product?", store)
    assert "30" in reply


class LeakyModel:
    def invoke(self, messages):
        return SimpleNamespace(content=f"Ticket ref: {app.CANARY}")


class EmptyStore:
    def similarity_search(self, question, k):
        return []


def test_canary_check_withholds_leak(monkeypatch):
    monkeypatch.setattr(app, "make_llm", LeakyModel)
    reply = app.answer("How long does shipping take?", EmptyStore())
    assert app.CANARY not in reply


@pytest.mark.skipif(
    app.__name__ != "rag", reason="the tripwire lives in rag.py"
)
class TestTripwire:
    def test_clean_documents_pass(self):
        assert not any(app.looks_like_injection(t) for t in CLEAN)

    @pytest.mark.parametrize("name", ["direct", "base64"])
    def test_flags_known_phrasing(self, name):
        assert app.looks_like_injection(PAYLOADS[name])

    @pytest.mark.xfail(strict=True, reason="a rephrased payload slips by")
    def test_flags_rephrased(self):
        assert app.looks_like_injection(PAYLOADS["rephrased"])
