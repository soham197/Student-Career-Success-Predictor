"""Data loading and cleaning for the Student Career Success Predictor."""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "student_career_success_dataset.csv"
OUTPUT_DIR = ROOT / "outputs"

TARGET = "Placement_Status"

# Columns removed to avoid data leakage (they are results of placement,
# or are derived from other columns) or because they carry no information.
DROP_COLS = [
    "Student_ID",
    "Company_Tier",
    "Career_Field",
    "Placement_Mode",
    "Starting_Salary_USD",
    "Employability_Score",
    "Interview_Score",
]


def load_data(path=DATA_PATH):
    """Load the CSV and print its shape."""
    df = pd.read_csv(path)
    print(f"Loaded data/{Path(path).name}: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


def clean_data(df):
    """Remove duplicates/missing rows and encode the target as 0/1."""
    df = df.drop_duplicates().dropna().copy()
    df["Placed"] = (df[TARGET] == "Placed").astype(int)
    return df


def get_features_and_target(df):
    """Return one-hot encoded features X and target y (1 = Placed)."""
    X = df.drop(columns=DROP_COLS + [TARGET, "Placed"])
    X = pd.get_dummies(X, drop_first=True)
    y = df["Placed"]
    return X, y
