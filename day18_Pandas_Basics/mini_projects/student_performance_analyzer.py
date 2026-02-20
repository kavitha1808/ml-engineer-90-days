import pandas as pd


def analyze_students():
    df = pd.read_csv("students.csv")

    df["Total"] = df["Math"] + df["Science"] + df["English"]
    df["Average"] = df["Total"] / 3

    print("Updated Data:\n", df)

    topper = df.loc[df["Average"].idxmax()]
    print("\nTopper:\n", topper)

    below_70 = df[df["Average"] < 70]
    print("\nStudents Below 70 Average:\n", below_70)


if __name__ == "__main__":
    analyze_students()
