import pandas as pd

def run_filtering_examples():
    data = {
        "Name": ["Asha", "Ravi", "Kiran", "Meena", "Arjun"],
        "Age": [22, 28, 35, 24, 30],
        "Salary": [40000, 60000, 80000, 45000, 70000],
        "Department": ["HR", "IT", "IT", "HR", "Finance"]
    }

    df = pd.DataFrame(data)

    print("\n--- Salary > 50000 ---")
    print(df[df["Salary"] > 50000])

    print("\n--- Age between 25 and 35 ---")
    print(df[df["Age"].between(25, 35)])

    print("\n--- Department is IT or HR ---")
    print(df[df["Department"].isin(["IT", "HR"])])


if __name__ == "__main__":
    run_filtering_examples()
