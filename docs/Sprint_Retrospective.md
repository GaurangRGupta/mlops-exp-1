# Sprint Retrospective — Sprint 1

Held after the Sprint Review. Goal: keep what worked, fix what slowed the team.

## What went well?

- Scrum artifacts (backlog, plan, daily, review) made a solo experiment easy to follow.
- `uv sync` produced a reproducible environment (`pyproject.toml` + `uv.lock`).
- The Iris Decision Tree met the 95% accuracy bar on the first training run.

## What problems occurred?

- Python packages were missing at the start of the Sprint (`scikit-learn`, `pandas`, `joblib`).
- Git was not initialized in the experiment folder, so early file changes were untracked.
- The handout path `D:\MLOps_Agile_Demo` could not be used; work had to stay inside `exp-1`.

## Improvements

- Run `uv sync` before Sprint work starts so library blockers do not appear on day one.
- Initialize git in the project folder as part of workspace setup (Step 1).
- Keep all experiment files under `exp-1/` so the next Sprint does not depend on a machine-specific drive path.
