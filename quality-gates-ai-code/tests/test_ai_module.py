import pytest

from demo.ai_module import api_token, discount, parse_age, run_report


def test_discount_gold() -> None:
    assert discount(100, "gold") == 80


def test_discount_silver_and_none() -> None:
    assert discount(100, "silver") == 90
    assert discount(100, "bronze") == 100


def test_run_report() -> None:
    assert run_report("x") == "report for x\n"


def test_parse_age() -> None:
    assert parse_age("42") == 42


def test_api_token(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("API_TOKEN", "abc")
    assert api_token() == "abc"
