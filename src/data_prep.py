"""Data loading and cleaning for the Student Career Success Predictor."""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "student_career_success_dataset.csv"
OUTPUT_DIR = ROOT / "outputs"

TARGET = "Placement_Status"

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
    """Return explicitly selected features X and target y (1 = Placed)."""
    
    # 1. Convert 'Placed' / 'Not Placed' into 1 and 0
    y = (df[TARGET] == "Placed").astype(int)
    
    # 2. Whitelist of strictly academic and skill-based features
    safe_features = [
        "CGPA", "Attendance_Percentage", "Study_Hours_Per_Week",
        "Programming_Skill", "Projects_Completed", "Certifications",
        "Hackathons", "Internships", "Resume_Score"
    ]
    
    X = df[safe_features]
    
    return X, y
