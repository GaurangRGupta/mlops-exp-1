"""Iris flower classification — Sprint 1 increment.

Downloads the Iris dataset, cleans it, trains a Decision Tree,
prints accuracy, and saves the model.
"""

from pathlib import Path

import joblib
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
MODELS_DIR = ROOT / "models"
RAW_DATA_PATH = DATA_DIR / "iris.csv"
CLEAN_DATA_PATH = DATA_DIR / "iris_cleaned.csv"
MODEL_PATH = MODELS_DIR / "iris_dt.joblib"


def download_iris() -> pd.DataFrame:
    """US1: persist the Iris dataset to data/iris.csv."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    iris = load_iris(as_frame=True)
    frame = iris.frame
    frame.to_csv(RAW_DATA_PATH, index=False)
    return frame


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """US2: drop missing values and duplicates, then save the cleaned copy."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    cleaned = df.dropna().drop_duplicates().reset_index(drop=True)
    cleaned.to_csv(CLEAN_DATA_PATH, index=False)
    return cleaned


def train_and_evaluate(df: pd.DataFrame) -> tuple[DecisionTreeClassifier, float]:
    """US3 + US4: train a Decision Tree and return test accuracy."""
    features = df.drop(columns=["target"])
    labels = df["target"]
    x_train, x_test, y_train, y_test = train_test_split(
        features,
        labels,
        test_size=0.2,
        random_state=42,
    )
    model = DecisionTreeClassifier(random_state=42)
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    accuracy = accuracy_score(y_test, prediction)
    return model, float(accuracy)


def save_model(model: DecisionTreeClassifier) -> Path:
    """US5: write the trained model to models/."""
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    return MODEL_PATH


def main() -> None:
    raw = download_iris()
    cleaned = clean_dataset(raw)
    model, accuracy = train_and_evaluate(cleaned)
    save_model(model)
    print("Accuracy:", accuracy)


if __name__ == "__main__":
    main()
