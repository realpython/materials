from demo.ai_module import discount, run_report


def test_discount_gold():
    assert discount(100, "gold") == 80


def test_run_report():
    assert "report" in run_report("x")
