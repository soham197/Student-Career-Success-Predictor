#Model Functions
"""Model training and evaluation."""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (ConfusionMatrixDisplay, accuracy_score,
                             classification_report, f1_score)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from data_prep import OUTPUT_DIR

RANDOM_STATE = 42


def split_data(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y)


def train_models(X_train, y_train):
    """Train a baseline Logistic Regression and a Random Forest."""
    log_reg = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
    forest = RandomForestClassifier(n_estimators=100, random_state=RANDOM_STATE, n_jobs=-1)
    log_reg.fit(X_train, y_train)
    forest.fit(X_train, y_train)
    return {"Logistic Regression": log_reg, "Random Forest": forest}


def evaluate_models(models, X_test, y_test):
    """Print accuracy and F1 for each model, return the best one."""
    best_name, best_acc = None, -1
    for name, model in models.items():
        pred = model.predict(X_test)
        acc = accuracy_score(y_test, pred)
        f1 = f1_score(y_test, pred)
        print(f"Model: {name} | Accuracy: {acc:.4f} | F1: {f1:.4f}")
        if acc > best_acc:
            best_name, best_acc = name, acc
    print(f"\nBest model: {best_name}")
    print(classification_report(y_test, models[best_name].predict(X_test),
                                target_names=["Not Placed", "Placed"]))
    return best_name, models[best_name]


def save_confusion_matrix(model, X_test, y_test, name):
    ConfusionMatrixDisplay.from_estimator(
        model, X_test, y_test, display_labels=["Not Placed", "Placed"], cmap="Blues")
    plt.title(f"Confusion Matrix - {name}")
    OUTPUT_DIR.mkdir(exist_ok=True)
    plt.savefig(OUTPUT_DIR / "confusion_matrix.png", dpi=120, bbox_inches="tight")
    plt.close()
    print("Saved outputs/confusion_matrix.png")


def save_feature_importance(forest, feature_names, top_n=10):
    imp = pd.Series(forest.feature_importances_, index=feature_names)
    imp = imp.sort_values().tail(top_n)
    plt.figure(figsize=(7, 5))
    plt.barh(imp.index, imp.values, color="#264653")
    plt.title(f"Top {top_n} Features for Predicting Placement")
    plt.xlabel("Importance")
    OUTPUT_DIR.mkdir(exist_ok=True)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "feature_importance.png", dpi=120)
    plt.close()
    print("Saved outputs/feature_importance.png")
    print("Top features:", ", ".join(imp.index[::-1][:5]))
