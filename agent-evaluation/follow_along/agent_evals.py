"""An eval harness for a tool-calling agent."""

import argparse
import sys
from pathlib import Path

from models import (
    AgentCase,
    AgentRun,
    AgentTrace,
    MetricResult,
    Trial,
    Verdict,
)


def load_cases(path: Path = Path("cases.jsonl")) -> list[AgentCase]:
    with path.open() as file:
        return [AgentCase.model_validate_json(line) for line in file]


def load_runs(path: Path) -> list[AgentRun]:
    with path.open() as file:
        return [AgentRun.model_validate_json(line) for line in file]


def code_result(
    criterion_id: str, problems: list[str], score: float | None = None
) -> MetricResult:
    return MetricResult(
        criterion_id=criterion_id,
        result_type="categorical",
        verdict="FAIL" if problems else "PASS",
        score=score,
        source="code",
        reason="; ".join(problems) if problems else "all checks passed",
    )


def capture_trace(question: str, messages: list[dict]) -> AgentTrace:
    """Turn an agent's message history into a structured trace."""
    # TODO: Write this function in Step 1.
    raise NotImplementedError


def run_suite(prompt: Path, cases: list[AgentCase], trials: int) -> Path:
    """Run every case through the agent and save the traces."""
    from agent import run_agent

    instructions = prompt.read_text()
    output = Path("runs") / f"{prompt.stem}.jsonl"
    output.parent.mkdir(exist_ok=True)
    with output.open("w") as file:
        for case in cases:
            for trial in range(1, trials + 1):
                messages = run_agent(case.user_message, instructions)
                run = AgentRun(
                    case_id=case.id,
                    prompt_id=prompt.stem,
                    trial=trial,
                    trace=capture_trace(case.user_message, messages),
                )
                file.write(run.model_dump_json() + "\n")
    return output


def grade_answer(case: AgentCase, trace: AgentTrace) -> MetricResult:
    """Check the final answer against required and forbidden patterns."""
    # TODO: Write this function in Step 2.
    raise NotImplementedError


def follows(called: list[str], expected: list[str], match: str) -> bool:
    """Compare the called tools with the expected tools."""
    # TODO: Write this function in Step 3.
    raise NotImplementedError


def grade_trajectory(case: AgentCase, trace: AgentTrace) -> MetricResult:
    """Check the order and number of tool calls."""
    # TODO: Write this function in Step 3.
    raise NotImplementedError


def grade_tool_selection(case: AgentCase, trace: AgentTrace) -> MetricResult:
    """Check that the agent picked the right tools with the right arguments."""
    # TODO: Write this function in Step 4.
    raise NotImplementedError


def tool_stats(path: Path, cases: list[AgentCase]) -> tuple[float, float]:
    """Compute tool-selection precision and recall over all runs."""
    # TODO: Write this function in Step 4.
    raise NotImplementedError


# TODO (Steps 2 to 4): Add your graders to this list.
GRADERS = []


def grade_runs(path: Path, cases: list[AgentCase]) -> list[Trial]:
    cases_by_id = {case.id: case for case in cases}
    trials = []
    for run in load_runs(path):
        case = cases_by_id[run.case_id]
        trials.append(
            Trial(
                case_id=case.id,
                prompt_id=run.prompt_id,
                critical=case.critical,
                response=run.trace.answer,
                metrics=[grade(case, run.trace) for grade in GRADERS],
            )
        )
    return trials


def case_verdicts(trials: list[Trial]) -> dict[tuple[str, str], Verdict]:
    """Merge repeated trials into one verdict per case and criterion."""
    seen: dict[tuple[str, str], set[str]] = {}
    for trial in trials:
        for metric in trial.metrics:
            key = (trial.case_id, metric.criterion_id)
            seen.setdefault(key, set()).add(metric.verdict)
    return {
        key: verdicts.pop() if len(verdicts) == 1 else "REVIEW"
        for key, verdicts in seen.items()
    }


def keys_with(trials: list[Trial], verdict: Verdict) -> set[tuple[str, str]]:
    """Collect the (case, criterion) pairs with a given verdict."""
    verdicts = case_verdicts(trials)
    return {key for key, value in verdicts.items() if value == verdict}


def release_decision(
    new_critical_failures: set[str],
    new_failures: set[str],
    candidate_reviews: set[str],
) -> tuple[str, str]:
    """Apply the release rules in order of severity."""
    # TODO: Write this function in Step 5.
    raise NotImplementedError


def compare(baseline: Path, candidate: Path, cases: list[AgentCase]) -> str:
    """Gate a candidate run against a baseline run."""
    # TODO: Write this function in Step 5.
    raise NotImplementedError


def report(path: Path, cases: list[AgentCase]) -> None:
    trials = grade_runs(path, cases)
    verdicts = case_verdicts(trials)
    criteria = list(dict.fromkeys(key[1] for key in verdicts))
    case_count = len({key[0] for key in verdicts})
    print(f"Prompt: {trials[0].prompt_id} | cases: {case_count}\n")
    print(f"{'Criterion':<16} {'Pass rate':>9}    P/F/R")
    print("-" * 35)
    for criterion in criteria:
        values = [v for (_, c), v in verdicts.items() if c == criterion]
        passed, failed, review = (
            values.count("PASS"),
            values.count("FAIL"),
            values.count("REVIEW"),
        )
        rate = f"{passed / len(values):.0%}"
        print(f"{criterion:<16} {rate:>9}    {passed}/{failed}/{review}")
    if "tool_selection" in criteria:
        precision, recall = tool_stats(path, cases)
        print(f"\nTool precision: {precision:.2f} | recall: {recall:.2f}")
    printed = set()
    for trial in trials:
        for metric in trial.metrics:
            key = (trial.case_id, metric.criterion_id)
            if metric.verdict != "PASS" and key not in printed:
                printed.add(key)
                print(f"\n{verdicts[key]} {trial.case_id}: {key[1]}")
                for line in metric.reason.split("; "):
                    print(f"  {line}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    trace_cmd = commands.add_parser("trace", help="Run once, print trace")
    trace_cmd.add_argument("question")
    trace_cmd.add_argument("--prompt", type=Path, required=True)

    run_cmd = commands.add_parser("run", help="Run every case")
    run_cmd.add_argument("--prompt", type=Path, required=True)
    run_cmd.add_argument("--trials", type=int, default=1)

    report_cmd = commands.add_parser("report", help="Grade saved runs")
    report_cmd.add_argument("runs", type=Path)

    compare_cmd = commands.add_parser("compare", help="Gate a candidate")
    compare_cmd.add_argument("baseline", type=Path)
    compare_cmd.add_argument("candidate", type=Path)

    args = parser.parse_args()
    cases = load_cases()
    if args.command == "trace":
        from agent import run_agent

        messages = run_agent(args.question, args.prompt.read_text())
        trace = capture_trace(args.question, messages)
        print(trace.model_dump_json(indent=2))
    elif args.command == "run":
        output = run_suite(args.prompt, cases, args.trials)
        count = len(load_runs(output))
        print(f"Saved {count} runs to {output}")
    elif args.command == "report":
        report(args.runs, cases)
    else:
        decision = compare(args.baseline, args.candidate, cases)
        return {"PASS": 0, "FAIL": 1, "REVIEW": 2}[decision]
    return 0


if __name__ == "__main__":
    sys.exit(main())
