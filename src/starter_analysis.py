from __future__ import annotations

from pathlib import Path
import pandas as pd


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "students_scores.csv"


def load_scores(csv_path: Path = DATA_PATH) -> pd.DataFrame:
    """Load workshop score data from a CSV file."""
    df = pd.read_csv(csv_path)
    return df


def compute_group_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    TODO for participants:
    Return a summary DataFrame grouped by 'group' with:
      - mean assignment, midterm, final
      - mean hours_studied
      - count of students
    """
    summary = (
        df.groupby("group", as_index=False)
        .agg(
            assignment_mean=("assignment", "mean"),
            midterm_mean=("midterm", "mean"),
            final_mean=("final", "mean"),
            hours_studied_mean=("hours_studied", "mean"),
            student_count=("student_id", "count"),
        )
        .round(2)
        .sort_values("group")
        .reset_index(drop=True)
    )
    return summary


def find_top_improvers(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """
    TODO for participants:
    Define improvement as (final - assignment).
    Return top n students sorted by highest improvement.
    Include columns: student_id, group, assignment, final, improvement.
    """
    with_improvement = df.assign(improvement=df["final"] - df["assignment"])
    top = (
        with_improvement.sort_values(
            by=["improvement", "student_id"], ascending=[False, True]
        )
        .head(n)
        .loc[:, ["student_id", "group", "assignment", "final", "improvement"]]
        .reset_index(drop=True)
    )
    return top


def main() -> None:
    df = load_scores()
    print("Loaded rows:", len(df))

    try:
        summary = compute_group_summary(df)
        print("\nGroup summary:")
        print(summary.to_string(index=False))
    except NotImplementedError as err:
        print(f"\n[Exercise A] {err}")

    try:
        top = find_top_improvers(df, n=5)
        print("\nTop improvers:")
        print(top.to_string(index=False))
    except NotImplementedError as err:
        print(f"\n[Exercise A] {err}")


if __name__ == "__main__":
    main()

