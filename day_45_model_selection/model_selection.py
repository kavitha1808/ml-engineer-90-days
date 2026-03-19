import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report

def load_data():
    """Load dataset"""
    data = load_iris()
    return data.data, data.target


def split_data(X, y):
    """Split dataset into train and test sets"""
    return train_test_split(X, y, test_size=0.2, random_state=42)


def perform_cross_validation(model, X, y):
    """Perform K-Fold Cross Validation"""
    scores = cross_val_score(model, X, y, cv=5)
    print(f"CV Scores: {scores}")
    print(f"Mean CV Score: {np.mean(scores):.4f}")


def tune_hyperparameters(model, X_train, y_train):
    """Hyperparameter tuning using GridSearch"""
    param_grid = {
        "C": [0.1, 1, 10]
    }

    grid = GridSearchCV(model, param_grid, cv=5)
    grid.fit(X_train, y_train)

    print(f"Best Parameters: {grid.best_params_}")
    return grid.best_estimator_


def evaluate_model(model, X_test, y_test):
    """Evaluate final model"""
    predictions = model.predict(X_test)

    print(f"Accuracy: {accuracy_score(y_test, predictions):.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))


def main():
    # Load data
    X, y = load_data()

    # Split data
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Initialize model
    model = LogisticRegression(max_iter=200)

    # Cross Validation
    perform_cross_validation(model, X, y)

    # Hyperparameter tuning
    best_model = tune_hyperparameters(model, X_train, y_train)

    # Final evaluation
    evaluate_model(best_model, X_test, y_test)


if __name__ == "__main__":
    main()
