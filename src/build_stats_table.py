from __future__ import annotations

from itertools import combinations
from math import comb
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "students_scores.csv"
OUT_PATH = ROOT / "reports" / "stats_table.tex"

ROWS = ["baseline", "llm_assisted"]
METRICS = ["assignment", "midterm", "final"]


def _escape_latex(text: str) -> str:
    return text.replace("_", r"\_")


def _exact_permutation_pvalue(a: pd.Series, b: pd.Series) -> float:
    """Exact two-sided permutation p-value for difference in means."""
    a_vals = [float(x) for x in a]
    b_vals = [float(x) for x in b]
    all_vals = a_vals + b_vals
    n_a = len(a_vals)
    observed = abs(sum(a_vals) / n_a - sum(b_vals) / len(b_vals))

    extreme = 0
    total = comb(len(all_vals), n_a)
    all_indices = range(len(all_vals))
    for idxs in combinations(all_indices, n_a):
        idx_set = set(idxs)
        group_a = [all_vals[i] for i in idxs]
        group_b = [all_vals[i] for i in all_indices if i not in idx_set]
        diff = abs(sum(group_a) / n_a - sum(group_b) / len(group_b))
        if diff >= observed - 1e-12:
            extreme += 1

    return extreme / total


def _build_table(df: pd.DataFrame) -> str:
    headers = []
    for metric in METRICS:
        baseline = df.loc[df["group"] == ROWS[0], metric]
        assisted = df.loc[df["group"] == ROWS[1], metric]
        p_value = _exact_permutation_pvalue(baseline, assisted)
        star = "*" if p_value < 0.5 else ""
        headers.append(f"{metric}{star}")

    lines = [
        r"\begin{tabular}{lccc}",
        r"\toprule",
        "group & " + " & ".join(headers) + r" \\",
        r"\midrule",
    ]

    grouped = df.groupby("group")
    for group in ROWS:
        means = grouped[METRICS].mean().loc[group]
        stds = grouped[METRICS].std(ddof=1).loc[group]
        cells = [
            f"{means[m]:.2f} $\\pm$ {stds[m]:.2f}"
            for m in METRICS
        ]
        lines.append(f"{_escape_latex(group)} & " + " & ".join(cells) + r" \\")

    lines.extend([r"\bottomrule", r"\end{tabular}", ""])
    return "\n".join(lines)


def main() -> None:
    df = pd.read_csv(DATA_PATH)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(_build_table(df), encoding="utf-8")
    print(f"Wrote table to: {OUT_PATH}")


if __name__ == "__main__":
    main()


