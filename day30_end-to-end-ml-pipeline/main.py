from src.data_loader import load_data
from src.preprocessing import clean_data, feature_engineering, split_data, scale_data
from src.model import train_model
from src.evaluation import evaluate_model


def main():
    # Step 1: Load data
    df = load_data("data/student_performance.csv")

    # Step 2: Clean data
    df = clean_data(df)

    # Step 3: Feature engineering
    df = feature_engineering(df)

    # IMPORTANT:
    # Change "pass" to your actual target column name
    target_column = "pass"

    # Step 4: Split data
    X_train, X_test, y_train, y_test = split_data(df, target_column)

    # Step 5: Scale data
    X_train_scaled, X_test_scaled = scale_data(X_train, X_test)

    # Step 6: Train model
    model = train_model(X_train_scaled, y_train)

    # Step 7: Evaluate model
    accuracy, report = evaluate_model(model, X_test_scaled, y_test)

    print("Model Accuracy:", accuracy)
    print("\nClassification Report:\n", report)


if __name__ == "__main__":
    main()
