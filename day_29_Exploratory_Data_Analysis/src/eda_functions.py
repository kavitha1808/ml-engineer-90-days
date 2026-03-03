import pandas as pd

def basic_info(df):
    print("\n===== BASIC INFO =====")
    print("Shape:", df.shape)
    print("\nData Types:")
    print(df.dtypes)
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDuplicate Rows:", df.duplicated().sum())


def summary_statistics(df):
    print("\n===== SUMMARY STATISTICS =====")
    print(df.describe())


def correlation_matrix(df):
    print("\n===== CORRELATION MATRIX =====")
    print(df.corr())
