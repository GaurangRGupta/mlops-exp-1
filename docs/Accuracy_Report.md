# Accuracy Report

Tester validation of the Sprint 1 increment against the Product Owner criterion (accuracy at least 95%).

## How it was run

```powershell
cd exp-1
uv sync
uv run python src/iris_demo.py
uv run pytest
```

## Result

| Item | Value |
|---|---|
| Algorithm | Decision Tree Classifier |
| Split | 80% train / 20% test, `random_state=42` |
| Command output | `Accuracy: 1.0` |
| pytest | 1 passed |
| Acceptance criterion | accuracy >= 0.95 |
| Verdict | Pass |

The handout expected about 0.96. This split of Iris is linearly simple enough that the tree classified every hold-out row correctly, so the printed score is 1.0. That is within the allowed "or similar" range and meets the 95% bar.

## Files checked

- Source: `src/iris_demo.py`
- Raw data: `data/iris.csv`
- Cleaned data: `data/iris_cleaned.csv`
- Saved model: `models/iris_dt.joblib`
