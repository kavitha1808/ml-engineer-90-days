import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer

from config_loader import load_config


def main():
    # Load config
    config = load_config()

    # Read config values
    data_path = config["data"]["path"]
    target_col = config["data"]["target"]
    drop_cols = config["data"]["drop_columns"]

    test_size = config["split"]["test_size"]
    random_state = config["split"]["random_state"]

    n_estimators = config["model"]["n_estimators"]
    max_depth = config["model"]["max_depth"]
    min_samples_split = config["model"]["min_samples_split"]

    model_path = config["output"]["model_path"]
    metrics_path = config["output"]["metrics_path"]

    # Create output folders
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    os.makedirs(os.path.dirname(metrics_path), exist_ok=True)

    # Load dataset
    df = pd.read_csv(data_path)

    # Drop unwanted columns if present
    df = df.drop(columns=[col for col in drop_cols if col in df.columns], errors="ignore")

    # Separate target before encoding
    y = df[target_col]
    X = df.drop(columns=[target_col])

    # One-hot encode categorical features
    X = pd.get_dummies(X, drop_first=True)

    # Fill missing values
    imputer = SimpleImputer(strategy="median")
    X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Model
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=random_state
    )

    # Train
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Metrics
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    # Save model
    joblib.dump(model, model_path)

    # Save metrics
    with open(metrics_path, "w", encoding="utf-8") as f:
        f.write(f"Accuracy: {acc:.4f}\n\n")
        f.write("Classification Report:\n")
        f.write(report)

    print(f"Model saved to: {model_path}")
    print(f"Metrics saved to: {metrics_path}")
    print(f"Accuracy: {acc:.4f}")


if __name__ == "__main__":
    main()
