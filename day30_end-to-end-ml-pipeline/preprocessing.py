import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle duplicates and missing values.
    """
    df = df.drop_duplicates()
    df = df.fillna(0)
    return df


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create additional useful features.
    Modify based on your dataset.
    """
    if {"math_score", "reading_score", "writing_score"}.issubset(df.columns):
        df["average_score"] = (
            df["math_score"] +
            df["reading_score"] +
            df["writing_score"]
        ) / 3

    return df


def split_data(df: pd.DataFrame, target_column: str):
    """
    Split dataset into train and test.
    """
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )

    return X_train, X_test, y_train, y_test


def scale_data(X_train, X_test):
    """
    Standardize numerical features.
    """
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled
