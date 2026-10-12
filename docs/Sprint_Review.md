# Sprint Review — Sprint 1

The team demonstrated the Sprint increment to the Product Owner.

## Checklist

- [x] Dataset downloaded (`data/iris.csv`, 150 rows)
- [x] Data cleaned (`data/iris_cleaned.csv`; duplicates dropped)
- [x] Model trained (`DecisionTreeClassifier`, `random_state=42`)
- [x] Accuracy generated (`Accuracy: 1.0`)

## Was the Sprint Goal achieved?

Yes. Sprint Goal was "Build the first working ML model." The Decision Tree trains from a local cleaned dataset, prints accuracy, and is saved under `models/`.

## What was delivered?

| Increment | Location |
|---|---|
| Working ML model | `models/iris_dt.joblib` |
| Python source | `src/iris_demo.py` |
| Documentation | `docs/` and `README.md` |
| Accuracy report | `docs/Accuracy_Report.md` |

The Product Owner accepted the increment. Accuracy 1.0 is above the 95% customer criterion.
