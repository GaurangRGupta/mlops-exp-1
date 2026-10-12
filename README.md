# Experiment 1: Agile and Scrum Demo

Solo simulation of an Agile Scrum lifecycle for a small MLOps project: classify Iris flowers with a Decision Tree.

One student assumes all five Scrum roles (Product Owner, Scrum Master, ML Engineer, Data Engineer, Tester).

## Project layout

```
exp-1/
├── data/          # Iris dataset (raw and cleaned)
├── src/           # Python source
├── models/        # Saved trained model
├── docs/          # Scrum artifacts and accuracy report
├── tests/         # Tester acceptance checks
├── pyproject.toml
└── README.md
```

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for the Python environment.

```powershell
cd exp-1
uv sync
```

## Run the model

```powershell
uv run python src/iris_demo.py
```

Expected output: `Accuracy: 0.96` (or similar). Product Owner acceptance is at least 95%.

## Tests

```powershell
uv run pytest
```

## Scrum artifacts

| Artifact | File |
|---|---|
| Roles | [docs/Scrum_Roles.md](docs/Scrum_Roles.md) |
| Product Backlog | [docs/Product_Backlog.md](docs/Product_Backlog.md) |
| Sprint Planning | [docs/Sprint_Planning.md](docs/Sprint_Planning.md) |
| Daily Scrum | [docs/Daily_Scrum.md](docs/Daily_Scrum.md) |
| Sprint Review | [docs/Sprint_Review.md](docs/Sprint_Review.md) |
| Sprint Retrospective | [docs/Sprint_Retrospective.md](docs/Sprint_Retrospective.md) |
| Accuracy Report | [docs/Accuracy_Report.md](docs/Accuracy_Report.md) |
