from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parent.parent
STUDENTS_CSV = ROOT / "data" / "students_scores.csv"
RUNS_CSV = ROOT / "data" / "model_runs.csv"
REPORT_PATH = ROOT / "reports" / "workshop_report.md"


def build_report() -> str:
    students = pd.read_csv(STUDENTS_CSV)
    runs = pd.read_csv(RUNS_CSV)

    group_summary = (
        students.groupby("group", as_index=False)
        .agg(
            assignment_mean=("assignment", "mean"),
            midterm_mean=("midterm", "mean"),
            final_mean=("final", "mean"),
            hours_mean=("hours_studied", "mean"),
            n=("student_id", "count"),
        )
        .round(2)
    )

    model_summary = (
        runs.groupby("model", as_index=False)
        .agg(
            avg_accuracy=("accuracy", "mean"),
            avg_latency_ms=("latency_ms", "mean"),
            avg_tokens=("tokens", "mean"),
        )
        .round(3)
    )

    lines = [
        "# Workshop Report",
        "",
        "This report is generated automatically from local CSV files.",
        "",
        "## Student Group Summary",
        "",
        group_summary.to_markdown(index=False),
        "",
        "## Model Run Summary",
        "",
        model_summary.to_markdown(index=False),
        "",
        "## Observations",
        "",
        "- `llm_assisted` group has higher average final scores in this toy dataset.",
        "- Larger models tend to have higher latency and higher token usage.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(build_report(), encoding="utf-8")
    print(f"Wrote report to: {REPORT_PATH}")


if __name__ == "__main__":
    main()

