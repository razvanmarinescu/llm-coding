.PHONY: test analysis report plots all

test:
	uv run pytest -q

analysis:
	uv run python src/starter_analysis.py

report:
	uv run python src/generate_report.py

plots:
	uv run python src/plot_metrics.py

all: test analysis report plots

