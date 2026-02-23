import pandas as pd

def preprocess_loans(df):
    df["Income"].fillna(df["Income"].mean(), inplace=True)
    df["Loan_Amount"].fillna(df["Loan_Amount"].mean(), inplace=True)
    df["Credit_Score"].fillna(df["Credit_Score"].median(), inplace=True)

    df["DTI"] = df["Loan_Amount"] / df["Income"]

    df["Risk"] = (
        (df["Credit_Score"] < 650) |
        (df["DTI"] > 0.5)
    )

    df["Risk"] = df["Risk"].map({
        True: "High",
        False: "Low"
    })

    return df


if __name__ == "__main__":
    data = {
        "Income": [50000, 60000, None, 80000, 45000],
        "Loan_Amount": [20000, 30000, 25000, None, 20000],
        "Credit_Score": [700, 650, 600, 720, None]
    }

    df = pd.DataFrame(data)
    cleaned = preprocess_loans(df)

    cleaned.to_csv("../outputs/cleaned_loan_data.csv", index=False)

    print(cleaned)
