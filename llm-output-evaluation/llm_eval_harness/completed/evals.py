import argparse
import hashlib
import json
import logging
import os
from pathlib import Path
from statistics import fmean
from typing import Any

from dotenv import load_dotenv
from llm_eval.clients import ModelClient, OpenAIClient, ReplayClient
from llm_eval.graders import evaluate_response, grade_with_judge
from llm_eval.models import (
    CalibrationCase,
    EvalCase,
    Rubric,
    Trial,
)
from pydantic import BaseModel, ValidationError

LOGGER = logging.getLogger("llm_eval")
DEFAULT_DATA = Path("data/support_eval.jsonl")
DEFAULT_RUBRIC = Path("rubrics/support.json")
DEFAULT_CALIBRATION = Path("data/judge_calibration.jsonl")
DEFAULT_REPLAY = Path("data/replay")
DEFAULT_RESULTS = Path("results")
EXIT_CODES = {"PASS": 0, "FAIL": 1, "REVIEW": 2}


def load_model(path: Path, model: type[BaseModel]) -> BaseModel:
    """Load one JSON document into a Pydantic model."""
    return model.model_validate_json(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path, model: type[BaseModel]) -> list[Any]:
    """Load and validate one Pydantic model per nonempty line."""
    records = []
    for line_number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not line.strip():
            continue
        try:
            records.append(model.model_validate_json(line))
        except ValidationError as exc:
            raise ValueError(f"{path}:{line_number}: {exc}") from exc
    return records


def validate_project(rubric: Rubric, cases: list[EvalCase]) -> None:
    """Reject duplicate cases and unknown criterion references."""
    case_ids = [case.id for case in cases]
    if len(case_ids) != len(set(case_ids)):
        raise ValueError("evaluation case IDs must be unique")
    criterion_ids = {criterion.id for criterion in rubric.criteria}
    for case in cases:
        unknown = set(case.criteria) - criterion_ids
        if unknown:
            raise ValueError(
                f"{case.id!r} uses unknown criteria: {sorted(unknown)}"
            )


SPLITS = ("dev", "release", "regression")


def select_splits(cases: list[EvalCase], requested: str | None) -> list[EvalCase]:
    """Keep only the cases belonging to the requested splits."""
    if not requested:
        return cases
    wanted = {name.strip() for name in requested.split(",") if name.strip()}
    unknown = wanted - set(SPLITS)
    if unknown:
        raise ValueError(f"unknown splits: {sorted(unknown)}")
    selected = [case for case in cases if case.split in wanted]
    if not selected:
        raise ValueError(f"no cases in splits: {sorted(wanted)}")
    return selected


def support_input(case: EvalCase) -> str:
    """Build the application input from trusted policy and user text."""
    return (
        f"Support policy:\n{case.policy}\n\n"
        f"Customer message:\n{case.user_message}\n\n"
        "Write the support reply only."
    )


def evaluate_prompt(
    client: ModelClient,
    prompt_path: Path,
    cases: list[EvalCase],
    rubric: Rubric,
    generator_model: str,
    judge_model: str,
    deterministic_only: bool = False,
) -> list[Trial]:
    """Generate and grade one response for every evaluation case."""
    prompt_name = prompt_path.stem
    prompt = prompt_path.read_text(encoding="utf-8").strip()
    criteria = {criterion.id: criterion for criterion in rubric.criteria}
    trials = []
    for case in cases:
        response = client.generate_text(
            request_id=f"generate:{prompt_name}:{case.id}",
            model=generator_model,
            instructions=prompt,
            input_text=support_input(case),
        )
        metrics = evaluate_response(
            client=client,
            request_id=f"judge:{prompt_name}:{case.id}",
            model=judge_model,
            case=case,
            criteria=criteria,
            response=response,
            deterministic_only=deterministic_only,
        )
        trials.append(
            Trial(
                case_id=case.id,
                prompt_id=prompt_name,
                critical=case.critical,
                response=response,
                metrics=metrics,
            )
        )
    return trials


def aggregate(trials: list[Trial], rubric: Rubric) -> dict[str, dict[str, Any]]:
    """Summarize categorical pass rates and ordinal mean scores."""
    summary: dict[str, dict[str, Any]] = {}
    for criterion in rubric.criteria:
        results = [
            metric
            for trial in trials
            for metric in trial.metrics
            if metric.criterion_id == criterion.id
        ]
        verdict_counts = {
            verdict: sum(item.verdict == verdict for item in results)
            for verdict in ("PASS", "FAIL", "REVIEW")
        }
        if criterion.result_type == "categorical":
            summary[criterion.id] = {
                "result_type": "categorical",
                "value": (
                    verdict_counts["PASS"] / len(results) if results else None
                ),
                "verdict_counts": verdict_counts,
            }
        else:
            scores = [item.score for item in results if item.score is not None]
            summary[criterion.id] = {
                "result_type": "ordinal",
                "value": fmean(scores) if scores else None,
                "scored": len(scores),
                "verdict_counts": verdict_counts,
            }
    return summary


def blocker_cases(trials: list[Trial], rubric: Rubric, verdict: str) -> set[str]:
    """Return case IDs with a blocker matching the requested verdict."""
    blockers = {
        criterion.id for criterion in rubric.criteria if criterion.blocker
    }
    return {
        trial.case_id
        for trial in trials
        if any(
            metric.criterion_id in blockers and metric.verdict == verdict
            for metric in trial.metrics
        )
    }


def release_decision(
    new_critical_failures: set[str],
    new_failures: set[str],
    candidate_reviews: set[str],
) -> tuple[str, str]:
    """Apply the release rules in order of severity."""
    if new_critical_failures:
        return "FAIL", "The candidate broke a blocker on a critical case."
    if new_failures:
        return "FAIL", "The candidate introduced a new blocker failure."
    if candidate_reviews:
        return "REVIEW", "A blocker could not be settled from the evidence."
    return "PASS", "The candidate introduced no new blocker failures."


def compare_trials(
    baseline: list[Trial],
    candidate: list[Trial],
    rubric: Rubric,
    cases: list[EvalCase],
) -> dict[str, Any]:
    """Compare paired trials and apply the hard release gate."""
    baseline_failures = blocker_cases(baseline, rubric, "FAIL")
    candidate_failures = blocker_cases(candidate, rubric, "FAIL")
    candidate_reviews = blocker_cases(candidate, rubric, "REVIEW")
    critical_ids = {case.id for case in cases if case.critical}

    new_failures = candidate_failures - baseline_failures
    new_critical_failures = new_failures & critical_ids
    fixed_failures = baseline_failures - candidate_failures
    carried_failures = baseline_failures & candidate_failures

    decision, reason = release_decision(
        new_critical_failures, new_failures, candidate_reviews
    )

    baseline_summary = aggregate(baseline, rubric)
    candidate_summary = aggregate(candidate, rubric)
    criteria = {}
    for criterion in rubric.criteria:
        before = baseline_summary[criterion.id]["value"]
        after = candidate_summary[criterion.id]["value"]
        if before is None or after is None:
            continue
        criterion_summary = {
            "result_type": criterion.result_type,
            "baseline": float(before),
            "candidate": float(after),
            "change": float(after) - float(before),
            "baseline_verdicts": baseline_summary[criterion.id][
                "verdict_counts"
            ],
            "candidate_verdicts": candidate_summary[criterion.id][
                "verdict_counts"
            ],
        }
        criteria[criterion.id] = criterion_summary
    return {
        "criteria": criteria,
        "new_blocker_failures": sorted(new_failures),
        "new_critical_failures": sorted(new_critical_failures),
        "carried_blocker_failures": sorted(carried_failures),
        "fixed_blocker_failures": sorted(fixed_failures),
        "review_cases": sorted(candidate_reviews),
        "release_decision": decision,
        "decision_reason": reason,
    }


def render_comparison(
    baseline_name: str, candidate_name: str, summary: dict[str, Any]
) -> str:
    """Render the paired summary for a terminal."""
    lines = [
        f"Baseline: {baseline_name}",
        f"Candidate: {candidate_name}",
        "",
        f"{'Criterion':24} {'Baseline':>10} {'Candidate':>10} {'Change':>10}",
        "-" * 58,
    ]
    for criterion_id, values in summary["criteria"].items():
        before = values["baseline"]
        after = values["candidate"]
        change = values["change"]
        if values["result_type"] == "categorical":
            before_text = f"{before:.0%}"
            after_text = f"{after:.0%}"
            change_text = f"{change * 100:+.0f} pp"
        else:
            before_text = f"{before:.2f}"
            after_text = f"{after:.2f}"
            change_text = f"{change:+.2f}"
        lines.append(
            f"{criterion_id[:24]:24} {before_text:>10} "
            f"{after_text:>10} {change_text:>10}"
        )
        baseline_verdicts = values["baseline_verdicts"]
        candidate_verdicts = values["candidate_verdicts"]
        baseline_counts = (
            f"{baseline_verdicts['PASS']}/"
            f"{baseline_verdicts['FAIL']}/"
            f"{baseline_verdicts['REVIEW']}"
        )
        candidate_counts = (
            f"{candidate_verdicts['PASS']}/"
            f"{candidate_verdicts['FAIL']}/"
            f"{candidate_verdicts['REVIEW']}"
        )
        lines.append(
            f"{'  verdicts (P/F/R)':24} {baseline_counts:>10} "
            f"{candidate_counts:>10} {'':>10}"
        )
    lines.extend(
        [
            "",
            f"New critical failures: {len(summary['new_critical_failures'])}",
            f"New blocker failures:  {len(summary['new_blocker_failures'])}",
            f"Carried over failures: {len(summary['carried_blocker_failures'])}",
            f"Fixed failures:        {len(summary['fixed_blocker_failures'])}",
            f"Cases needing review:  {len(summary['review_cases'])}",
            "",
            f"Release decision: {summary['release_decision']}",
            f"Reason: {summary['decision_reason']}",
        ]
    )
    return "\n".join(lines)


def render_run_summary(
    prompt_name: str, mode: str, cases: int, summary: dict[str, Any]
) -> str:
    """Render one prompt's criterion summary for a terminal."""
    lines = [
        f"Prompt: {prompt_name} | mode: {mode} | cases: {cases}",
        "",
        f"{'Criterion':24} {'Value':>8} {'P/F/R':>10}",
        "-" * 44,
    ]
    for criterion_id, values in summary.items():
        value = values["value"]
        if value is None:
            value_text = "--"
        elif values["result_type"] == "categorical":
            value_text = f"{value:.0%}"
        else:
            value_text = f"{value:.2f}"
        counts = values["verdict_counts"]
        counts_text = f"{counts['PASS']}/{counts['FAIL']}/{counts['REVIEW']}"
        lines.append(f"{criterion_id[:24]:24} {value_text:>8} {counts_text:>10}")
    return "\n".join(lines)


def file_hash(path: Path) -> str:
    """Return a SHA-256 hash for a checked-in evaluation input."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_artifacts(
    result_dir: Path,
    trials: list[Trial],
    summary: dict[str, Any],
    inputs: dict[str, Path],
    mode: str,
    generator_model: str,
    judge_model: str,
) -> None:
    """Write auditable machine-readable run artifacts."""
    result_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "mode": mode,
        "generator_model": generator_model,
        "judge_model": judge_model,
        "input_hashes": {
            name: file_hash(path) for name, path in inputs.items()
        },
    }
    (result_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    trial_text = "\n".join(
        json.dumps(trial.model_dump(mode="json")) for trial in trials
    )
    (result_dir / "trials.jsonl").write_text(
        trial_text + "\n", encoding="utf-8"
    )
    (result_dir / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )


def calibrate_judge(
    client: ModelClient,
    records: list[CalibrationCase],
    cases: list[EvalCase],
    rubric: Rubric,
    judge_model: str,
) -> dict[str, Any]:
    """Compare judge labels with adjudicated human labels and canaries."""
    if not records:
        raise ValueError("the calibration set is empty")
    cases_by_id = {case.id: case for case in cases}
    criteria = {criterion.id: criterion for criterion in rubric.criteria}
    rows = []
    for record in records:
        results = grade_with_judge(
            client=client,
            request_id=f"calibrate:{record.id}",
            model=judge_model,
            case=cases_by_id[record.case_id],
            criteria=[criteria[record.criterion_id]],
            response=record.candidate_response,
        )
        rows.append(
            {
                "id": record.id,
                "expected": record.adjudicated_label,
                "predicted": results[0].verdict,
                "critical": record.critical,
                "canary": record.canary,
            }
        )
    agreement = sum(row["expected"] == row["predicted"] for row in rows)
    false_passes = sum(
        row["critical"]
        and row["expected"] == "FAIL"
        and row["predicted"] == "PASS"
        for row in rows
    )
    canaries = [row for row in rows if row["canary"]]
    detected = sum(row["expected"] == row["predicted"] for row in canaries)
    return {
        "records": len(rows),
        "exact_agreement": agreement / len(rows),
        "critical_false_passes": false_passes,
        "canaries_detected": detected,
        "canaries_total": len(canaries),
        "results": rows,
    }


def make_client(live: bool, replay_dir: Path) -> tuple[ModelClient, str]:
    """Select deterministic replay or live OpenAI execution."""
    if live:
        return OpenAIClient(), "live"
    return ReplayClient(replay_dir), "replay"


def add_common_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--rubric", type=Path, default=DEFAULT_RUBRIC)
    parser.add_argument(
        "--live",
        action="store_true",
        help="call the model API instead of replaying recorded responses",
    )
    parser.add_argument("--replay-dir", type=Path, default=DEFAULT_REPLAY)
    parser.add_argument(
        "--split",
        help="comma-separated splits to evaluate, such as release,regression",
    )
    parser.add_argument("--results", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument(
        "--generator-model",
        default=os.getenv("EVAL_GENERATOR_MODEL", "gpt-5.6-luna"),
    )
    parser.add_argument(
        "--judge-model",
        default=os.getenv("EVAL_JUDGE_MODEL", "gpt-5.6-terra"),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    validate = commands.add_parser("validate")
    validate.add_argument("--data", type=Path, default=DEFAULT_DATA)
    validate.add_argument("--rubric", type=Path, default=DEFAULT_RUBRIC)

    run = commands.add_parser("run")
    run.add_argument("--prompt", type=Path, required=True)
    run.add_argument(
        "--deterministic-only",
        action="store_true",
        help="run the code graders and skip every LLM judge call",
    )
    add_common_options(run)

    calibrate = commands.add_parser("calibrate")
    calibrate.add_argument("--labels", type=Path, default=DEFAULT_CALIBRATION)
    add_common_options(calibrate)

    compare = commands.add_parser("compare")
    compare.add_argument("--baseline", type=Path, required=True)
    compare.add_argument("--candidate", type=Path, required=True)
    add_common_options(compare)
    return parser


def load_inputs(args: argparse.Namespace) -> tuple[Rubric, list[EvalCase]]:
    rubric = load_model(args.rubric, Rubric)
    cases = load_jsonl(args.data, EvalCase)
    validate_project(rubric, cases)
    return rubric, select_splits(cases, getattr(args, "split", None))


def command_validate(args: argparse.Namespace) -> int:
    rubric, cases = load_inputs(args)
    blockers = sum(criterion.blocker for criterion in rubric.criteria)
    counts = {name: sum(case.split == name for case in cases) for name in SPLITS}
    LOGGER.info(
        "%d valid cases | %d criteria | %d blockers",
        len(cases),
        len(rubric.criteria),
        blockers,
    )
    LOGGER.info(
        "Splits: dev=%d, release=%d, regression=%d",
        counts["dev"],
        counts["release"],
        counts["regression"],
    )
    LOGGER.info(
        "Critical cases: %d", sum(case.critical for case in cases)
    )
    return 0


def command_run(args: argparse.Namespace) -> int:
    rubric, cases = load_inputs(args)
    client, mode = make_client(args.live, args.replay_dir)
    if args.deterministic_only:
        mode = f"{mode}+deterministic-only"
    trials = evaluate_prompt(
        client=client,
        prompt_path=args.prompt,
        cases=cases,
        rubric=rubric,
        generator_model=args.generator_model,
        judge_model=args.judge_model,
        deterministic_only=args.deterministic_only,
    )
    summary = aggregate(trials, rubric)
    LOGGER.info(
        render_run_summary(args.prompt.stem, mode, len(cases), summary)
    )
    write_artifacts(
        result_dir=args.results / args.prompt.stem,
        trials=trials,
        summary={"criteria": summary},
        inputs={
            "prompt": args.prompt,
            "data": args.data,
            "rubric": args.rubric,
        },
        mode=mode,
        generator_model=args.generator_model,
        judge_model=args.judge_model,
    )
    return 0


def command_calibrate(args: argparse.Namespace) -> int:
    rubric, cases = load_inputs(args)
    records = load_jsonl(args.labels, CalibrationCase)
    client, _ = make_client(args.live, args.replay_dir)
    report = calibrate_judge(
        client=client,
        records=records,
        cases=cases,
        rubric=rubric,
        judge_model=args.judge_model,
    )
    LOGGER.info("Calibration records: %d", report["records"])
    LOGGER.info("Exact agreement: %.1f%%", report["exact_agreement"] * 100)
    LOGGER.info("Critical false passes: %d", report["critical_false_passes"])
    LOGGER.info(
        "Injection canaries detected: %d/%d",
        report["canaries_detected"],
        report["canaries_total"],
    )
    args.results.mkdir(parents=True, exist_ok=True)
    (args.results / "calibration.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    return 1 if report["critical_false_passes"] else 0


def command_compare(args: argparse.Namespace) -> int:
    rubric, cases = load_inputs(args)
    client, mode = make_client(args.live, args.replay_dir)
    common = {
        "client": client,
        "cases": cases,
        "rubric": rubric,
        "generator_model": args.generator_model,
        "judge_model": args.judge_model,
    }
    baseline = evaluate_prompt(prompt_path=args.baseline, **common)
    candidate = evaluate_prompt(prompt_path=args.candidate, **common)
    summary = compare_trials(baseline, candidate, rubric, cases)
    LOGGER.info(
        render_comparison(args.baseline.stem, args.candidate.stem, summary)
    )
    result_dir = args.results / f"{args.baseline.stem}-vs-{args.candidate.stem}"
    write_artifacts(
        result_dir=result_dir,
        trials=[*baseline, *candidate],
        summary=summary,
        inputs={
            "baseline": args.baseline,
            "candidate": args.candidate,
            "data": args.data,
            "rubric": args.rubric,
        },
        mode=mode,
        generator_model=args.generator_model,
        judge_model=args.judge_model,
    )
    return EXIT_CODES[summary["release_decision"]]


COMMANDS = {
    "validate": command_validate,
    "run": command_run,
    "calibrate": command_calibrate,
    "compare": command_compare,
}


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    args = build_parser().parse_args(argv)
    try:
        return COMMANDS[args.command](args)
    except (
        FileNotFoundError,
        KeyError,
        RuntimeError,
        TypeError,
        ValidationError,
        ValueError,
    ) as exc:
        LOGGER.error("error: %s", exc)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())