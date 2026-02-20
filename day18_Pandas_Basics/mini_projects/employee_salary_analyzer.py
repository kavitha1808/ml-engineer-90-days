import pandas as pd


def analyze_salaries():
    df = pd.read_csv("employees.csv")

    print("Average Salary:", df["Salary"].mean())

    highest_paid = df.loc[df["Salary"].idxmax()]
    print("\nHighest Paid Employee:\n", highest_paid)

    dept_avg = df.groupby("Department")["Salary"].mean()
    print("\nAverage Salary Per Department:\n", dept_avg)

    high_earners = df[df["Salary"] > 50000]
    print("\nEmployees earning > 50000:\n", high_earners)


if __name__ == "__main__":
    analyze_salaries()
