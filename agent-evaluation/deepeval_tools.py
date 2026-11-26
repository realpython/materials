from deepeval.metrics import ToolCorrectnessMetric
from deepeval.test_case import LLMTestCase, ToolCall

test_case = LLMTestCase(
    input="What's the latest billing-client and its minimum Python?",
    actual_output="Version 3.2.0 is the latest. It needs Python 3.11+.",
    tools_called=[
        ToolCall(name="search_docs"),
        ToolCall(name="lookup_package"),
    ],
    expected_tools=[ToolCall(name="lookup_package")],
)

for exact in (False, True):
    metric = ToolCorrectnessMetric(should_exact_match=exact)
    metric.measure(test_case)
    print(f"should_exact_match={exact}: score {metric.score}")
