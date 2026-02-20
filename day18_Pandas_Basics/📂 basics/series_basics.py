import pandas as pd


def create_series():
    numbers = [5, 10, 15, 20, 25]

    series_default = pd.Series(numbers)
    series_custom = pd.Series(numbers, index=["a", "b", "c", "d", "e"])

    print("Default Index Series:\n", series_default)
    print("\nCustom Index Series:\n", series_custom)


if __name__ == "__main__":
    create_series()
