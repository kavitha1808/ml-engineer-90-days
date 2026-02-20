import pandas as pd


def create_dataframe():
    data = {
        "Name": ["Kavitha", "Arun", "Meena", "Rahul"],
        "Department": ["AI", "HR", "Finance", "IT"],
        "Salary": [50000, 40000, 45000, 60000]
    }

    df = pd.DataFrame(data)

    print("DataFrame:\n", df)
    print("\nShape:", df.shape)
    print("\nColumns:", df.columns)
    print("\nInfo:")
    print(df.info())
    print("\nStatistics:\n", df.describe())


if __name__ == "__main__":
    create_dataframe()
