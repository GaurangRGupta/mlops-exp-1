# Daily Scrum — Sprint 1

Facilitated by the Scrum Master. Each role answers: what was done yesterday, what is planned today, and what is blocking progress.

One student is speaking for every role.

## Product Owner

| | |
|---|---|
| Yesterday | Requirements finalized: Iris classifier with at least 95% accuracy. Product Backlog ordered. |
| Today | Review Sprint progress against the Sprint Goal. |
| Blockers | None. |

## Scrum Master

| | |
|---|---|
| Yesterday | Sprint planned. Sprint Goal set to "Build the first working ML model." |
| Today | Conduct Daily Scrum and keep the board updated. |
| Blockers | Git was not initialized in the experiment folder. Resolved by `git init` inside `exp-1`. |

## ML Engineer

| | |
|---|---|
| Yesterday | Selected Decision Tree Classifier for Sprint 1. |
| Today | Train the model once cleaned data is available. |
| Blockers | Dataset was not yet in `data/`. Unblocked after the Data Engineer saved `iris.csv`. |

## Data Engineer

| | |
|---|---|
| Yesterday | Downloaded the Iris dataset with `sklearn.datasets.load_iris`. |
| Today | Clean the table (missing values, duplicates), save `iris_cleaned.csv`, and split 80/20. |
| Blockers | `scikit-learn` was missing in the environment. Resolved with `uv add` / `uv sync`. |

## Tester

| | |
|---|---|
| Yesterday | Prepared the acceptance test: accuracy must be at least 0.95. |
| Today | Evaluate accuracy and run `uv run pytest`. |
| Blockers | None. |
