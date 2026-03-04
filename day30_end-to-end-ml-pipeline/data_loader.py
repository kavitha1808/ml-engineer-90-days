import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load CSV file into pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print("Error loading file:", e)
        raise
