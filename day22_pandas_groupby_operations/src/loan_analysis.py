import pandas as pd


def run_loan_analysis():
    df = pd.read_csv("data/loan_data.csv")

    avg_loan = df.groupby("City")["Loan_Amount"].mean()
    total_loan = df.groupby("City")["Loan_Amount"].sum()

    high_risk = (
        df[df["Risk"] == "High"]
        .groupby("City")["Customer"]
        .count()
    )

    result = pd.DataFrame({
        "Average_Loan": avg_loan,
        "Total_Loan": total_loan,
        "High_Risk_Count": high_risk
    }).fillna(0)

    result.reset_index().to_csv("outputs/loan_results.csv", index=False)

    print("\nLoan Analysis Completed")
    print(result)
