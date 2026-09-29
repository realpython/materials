from deepeval import assert_test
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams


def test_defective_return_policy() -> None:
    policy_correctness = GEval(
        name="Policy correctness",
        criteria=(
            "Determine whether the actual output agrees "
            "with the expected policy "
            "decision. Preserve the defective-item exception, "
            "avoid guaranteeing "
            "a refund before review, and provide the escalation path."
        ),
        evaluation_params=[
            SingleTurnParams.INPUT,
            SingleTurnParams.ACTUAL_OUTPUT,
            SingleTurnParams.EXPECTED_OUTPUT,
        ],
        threshold=0.8,
    )
    test_case = LLMTestCase(
        input="I bought these boots 45 days ago, but the sole separated.",
        actual_output=(
            "The 30-day window has passed, but a defective item can still be "
            "reviewed. Send support your order number and photos."
        ),
        expected_output=(
            "Preserve the defective-item review exception "
            "and provide the next step."
        ),
    )
    assert_test(test_case, [policy_correctness])
