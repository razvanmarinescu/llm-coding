from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


ROOT = Path(__file__).resolve().parent.parent
STUDENTS_CSV = ROOT / "data" / "students_scores.csv"
RUNS_CSV = ROOT / "data" / "model_runs.csv"
REPORTS_DIR = ROOT / "reports"


def plot_scores_by_group(students: pd.DataFrame) -> Path:
    out_path = REPORTS_DIR / "score_by_group.png"
    plt.figure(figsize=(7, 4))
    sns.boxplot(data=students, x="group", y="final")
    plt.title("Final Score Distribution by Group")
    plt.xlabel("Group")
    plt.ylabel("Final score")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
    return out_path


def plot_accuracy_vs_latency(runs: pd.DataFrame) -> Path:
    out_path = REPORTS_DIR / "accuracy_vs_latency.png"
    plt.figure(figsize=(7, 4))
    sns.scatterplot(
        data=runs,
        x="latency_ms",
        y="accuracy",
        hue="model",
        size="tokens",
        sizes=(40, 180),
    )
    plt.title("Accuracy vs Latency")
    plt.xlabel("Latency (ms)")
    plt.ylabel("Accuracy")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
    return out_path


def plot_tokens_by_model(runs: pd.DataFrame) -> Path:
    out_path = REPORTS_DIR / "tokens_by_model.png"
    plt.figure(figsize=(7, 4))
    sns.boxplot(data=runs, x="model", y="tokens")
    plt.title("Token Usage Distribution by Model")
    plt.xlabel("Model")
    plt.ylabel("Tokens")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
    return out_path


def main() -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    students = pd.read_csv(STUDENTS_CSV)
    runs = pd.read_csv(RUNS_CSV)

    a = plot_scores_by_group(students)
    b = plot_accuracy_vs_latency(runs)
    c = plot_tokens_by_model(runs)
    print(f"Wrote plot: {a}")
    print(f"Wrote plot: {b}")
    print(f"Wrote plot: {c}")


if __name__ == "__main__":
    main()

