from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.train import train_model
from src.evaluate import evaluate_model
from src.utils import print_separator

def main():
    df = load_data("data/titanic.csv")

    X_train, X_test, y_train, y_test = preprocess_data(df)

    model = train_model(X_train, y_train)

    acc, cm, report = evaluate_model(model, X_test, y_test)

    print_separator()
    print("Model Accuracy:", round(acc, 4))
    print_separator()
    print("Confusion Matrix:")
    print(cm)
    print_separator()
    print("Classification Report:")
    print(report)
    print_separator()

if __name__ == "__main__":
    main()
