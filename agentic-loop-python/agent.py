"""An agentic loop that fixes and optimizes Python code."""

import json

from openai import OpenAI
from tools import (
    OPTIMIZATION_MENU,
    TOOL_DEFINITIONS,
    TOOL_REGISTRY,
    read_code,
)

client = OpenAI()
MODEL = "gpt-4o-mini"
MAX_ITERATIONS = 10


def call_tools(tool_calls):
    """Execute each tool call and return the results."""
    results = []
    for call in tool_calls:
        name = call.function.name
        if name not in TOOL_REGISTRY:
            output = f"Error: Unknown tool '{name}'"
        else:
            try:
                args = json.loads(call.function.arguments)
                args.pop("reasoning", None)
                output = TOOL_REGISTRY[name](**args)
            except Exception as err:
                output = f"Error: {err}"
        results.append(
            {
                "role": "tool",
                "tool_call_id": call.id,
                "content": str(output),
            }
        )
    return results


def run_phase(system_prompt, goal, phase_name):
    """Run one phase of the agentic loop."""
    print(f"\n{'=' * 50}")
    print(f" {phase_name}")
    print(f"{'=' * 50}\n")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": goal},
    ]

    last_good = read_code("search.py")

    for step in range(1, MAX_ITERATIONS + 1):
        print(f"[Step {step}]")

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOL_DEFINITIONS,
        )

        message = response.choices[0].message
        messages.append(message)

        if message.content:
            print(f"  Think: {message.content[:200]}")

        if not message.tool_calls:
            print(f"\n{phase_name} complete.\n")
            return message.content

        for call in message.tool_calls:
            name = call.function.name
            args = json.loads(call.function.arguments)
            reasoning = args.pop("reasoning", None)
            if reasoning:
                print(f"  Think: {reasoning}")
            short = str(args)[:80]
            print(f"  Act:   {name}({short})")

        results = call_tools(message.tool_calls)
        messages.extend(results)

        for call in message.tool_calls:
            if call.function.name == "write_code":
                test_out = TOOL_REGISTRY["run_tests"]()
                if "failed" in test_out.lower():
                    TOOL_REGISTRY["write_code"]("search.py", last_good)
                    messages.append(
                        {
                            "role": "user",
                            "content": (
                                "Your change broke a test."
                                " I reverted search.py. "
                                "Try a different approach."
                            ),
                        },
                    )
                else:
                    last_good = read_code("search.py")
                break

        for r in results:
            preview = r["content"][:120]
            print(f"  Observe: {preview}")

    print(f"\n{phase_name}: iteration cap reached.\n")
    return None


def main():
    """Run both phases of the agent."""
    source = read_code("search.py")
    print(f"Target program loaded ({len(source)} chars)")

    # Phase 1: Fix the correctness bug
    phase1_system = (
        "You are a Python debugging agent. Fix bugs "
        "in search.py by reading the code, running "
        "the test suite, and writing a corrected "
        "version. Only modify search.py. Stop when "
        "all tests pass."
    )
    phase1_goal = (
        "The test suite in test_search.py has a "
        "failing test. Start by running the test "
        "suite to see which test fails and why. "
        "Then find the bug in search.py and fix it."
    )
    run_phase(phase1_system, phase1_goal, "Phase 1: Fix")

    # Phase 2: Optimize performance
    phase2_system = (
        "You are a Python optimization agent. Speed "
        "up search_similar() in search.py. Run the "
        "benchmark first, then optimize using one of "
        "the techniques below. After optimizing, run "
        "both the tests and the benchmark to verify "
        "correctness and improvement.\n\n"
        f"{OPTIMIZATION_MENU}"
    )
    phase2_goal = (
        "Optimize search_similar() in search.py for "
        "speed. Measure before and after. Keep all "
        "tests passing."
    )
    run_phase(
        phase2_system,
        phase2_goal,
        "Phase 2: Optimize",
    )


if __name__ == "__main__":
    main()
