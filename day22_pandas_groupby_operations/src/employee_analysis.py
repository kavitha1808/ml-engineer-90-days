import pandas as pd


def run_employee_analysis():
    df = pd.read_csv("data/employee_data.csv")

    avg_salary = df.groupby("Department")["Salary"].mean()
    total_salary = df.groupby("Department")["Salary"].sum()
    emp_count = df.groupby("Department")["Employee"].count()
    salary_stats = df.groupby("Department")["Salary"].agg(
        ["mean", "sum", "max", "min"]
    )

    result = salary_stats.reset_index()
    result.to_csv("outputs/employee_results.csv", index=False)

    print("\nEmployee Analysis Completed")
    print(result)
