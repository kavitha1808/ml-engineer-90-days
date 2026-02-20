import pandas as pd


def read_csv_file():
    df = pd.read_csv("employees.csv")

    print("First 5 rows:\n", df.head())
    print("\nShape:", df.shape)
    print("\nColumns:", df.columns)


if __name__ == "__main__":
    read_csv_file()
