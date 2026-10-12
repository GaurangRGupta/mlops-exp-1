# Product Backlog

Owned by the Product Owner. Items are ordered by priority so the team can deliver a working increment in Sprint 1.

| ID | User Story | Priority | Status |
|---|---|---|---|
| US1 | As a data engineer, I want to download the Iris dataset so that training has a local, versioned copy. | High | Done |
| US2 | As a data engineer, I want to clean the dataset so that missing values and duplicates do not affect training. | High | Done |
| US3 | As an ML engineer, I want to train a Decision Tree model so that Iris species can be classified. | High | Done |
| US4 | As a tester, I want to evaluate accuracy so that we know whether the 95% acceptance criterion is met. | Medium | Done |
| US5 | As an ML engineer, I want to save the trained model so that the Sprint increment can be reused. | Medium | Done |
| US6 | As a product owner, I want documentation of Scrum ceremonies and results so that the process is reviewable. | Low | Done |

## Why High priority items are selected first

US1–US3 are High because they are the critical path to a working model:

- The model cannot be trained until the dataset exists (US1).
- Dirty data would make accuracy numbers untrustworthy (US2).
- Training (US3) is the core of the Sprint Goal.

US4 and US5 depend on a trained model, so they wait until US3 is done. US6 is Low because documentation can be finished after the increment exists, without blocking the Sprint Goal.
