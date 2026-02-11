# Workshop Report

This report is generated automatically from local CSV files.

## Student Group Summary

| group        |   assignment_mean |   midterm_mean |   final_mean |   hours_mean |   n |
|:-------------|------------------:|---------------:|-------------:|-------------:|----:|
| baseline     |             76.38 |          74    |        80.62 |         5.75 |   8 |
| llm_assisted |             88.62 |          85.38 |        91    |         8.5  |   8 |

## Model Run Summary

| model          |   avg_accuracy |   avg_latency_ms |   avg_tokens |
|:---------------|---------------:|-----------------:|-------------:|
| claude-sonnet  |          0.87  |         1760     |     1020     |
| deepseek-coder |          0.763 |          796.667 |      628.333 |
| gpt-4.1        |          0.88  |         1500     |      873.333 |
| gpt-4.1-mini   |          0.807 |          906.667 |      665     |

## Observations

- `llm_assisted` group has higher average final scores in this toy dataset.
- Larger models tend to have higher latency and higher token usage.

## Failure Modes

- Small sample size (n=8 per group) makes results sensitive to outliers.
- No control for prior experience; group differences may reflect selection bias.
- Model accuracy was measured on a single prompt set; results may not generalise to other tasks.
- High-temperature runs can introduce variance that masks true model capability.
