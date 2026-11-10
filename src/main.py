"""Entry point: run with `python src/main.py` from the repository root."""
from data_prep import clean_data, get_features_and_target, load_data
from model import (evaluate_models, save_confusion_matrix,
                   save_feature_importance, split_data, train_models)
from plots import make_all_plots


def main():
    df = clean_data(load_data())
    make_all_plots(df)

    X, y = get_features_and_target(df)
    X_train, X_test, y_train, y_test = split_data(X, y)
    models = train_models(X_train, y_train)
    best_name, best_model = evaluate_models(models, X_test, y_test)

    save_confusion_matrix(best_model, X_test, y_test, best_name)
    save_feature_importance(models["Random Forest"], X.columns)


if __name__ == "__main__":
    main()
