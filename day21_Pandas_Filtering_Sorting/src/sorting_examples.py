import pandas as pd

def run_sorting_examples():
    data = {
        "Name": ["Asha", "Ravi", "Kiran", "Meena", "Arjun"],
        "Salary": [40000, 60000, 80000, 45000, 70000],
        "Department": ["HR", "IT", "IT", "HR", "Finance"]
    }

    df = pd.DataFrame(data)

    print("\n--- Sort by Salary Descending ---")
    print(df.sort_values("Salary", ascending=False))

    print("\n--- Sort by Department and Salary ---")
    print(df.sort_values(["Department", "Salary"]))


if __name__ == "__main__":
    run_sorting_examples()
