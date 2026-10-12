"""Tester checks for the Sprint 1 Iris increment."""

import iris_demo


def test_accuracy_meets_acceptance_criterion():
    raw = iris_demo.download_iris()
    cleaned = iris_demo.clean_dataset(raw)
    _, accuracy = iris_demo.train_and_evaluate(cleaned)
    assert accuracy >= 0.95
