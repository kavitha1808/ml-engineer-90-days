import pandas as pd

def run_conditional_selection():
    data = {
        "Name": ["Asha", "Ravi", "Kiran", "Meena", "Arjun"],
        "Age": [22, 28, 35, 24, 30],
        "Salary": [40000, 60000, 80000, 45000, 70000]
    }

    df = pd.DataFrame(data)

    print("\n--- Using loc ---")
    print(df.loc[df["Age"] > 25, ["Name", "Salary"]])

    print("\n--- Using iloc ---")
    print(df.iloc[0:3, 0:2])

    df["High_Salary"] = df["Salary"] > 50000

    df["Category"] = df["Salary"].apply(
        lambda x: "High" if x > 50000 else "Low"
    )

    print("\n--- After Feature Engineering ---")
    print(df)


if __name__ == "__main__":
    run_conditional_selection()
