import pandas as pd

def calculate_risk(df):
    df["Risk"] = (
        (df["Credit_Score"] < 650) |
        (df["Loan_Amount"] > df["Income"])
    )

    df["Risk"] = df["Risk"].map({
        True: "High Risk",
        False: "Low Risk"
    })

    return df


if __name__ == "__main__":
    data = {
        "Customer": ["A", "B", "C", "D", "E"],
        "Income": [30000, 80000, 50000, 120000, 45000],
        "Loan_Amount": [20000, 50000, 40000, 90000, 30000],
        "Credit_Score": [600, 750, 680, 800, 620]
    }

    df = pd.DataFrame(data)
    result = calculate_risk(df)

    high_risk = result[result["Risk"] == "High Risk"]
    high_risk.to_csv("../outputs/high_risk_customers.csv", index=False)

    print(high_risk)
