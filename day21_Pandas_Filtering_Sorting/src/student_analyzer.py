import pandas as pd

def analyze_students(df):
    df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
    df["Average"] = df["Total"] / 3

    def assign_grade(avg):
        if avg > 85:
            return "A"
        elif avg >= 70:
            return "B"
        else:
            return "C"

    df["Grade"] = df["Average"].apply(assign_grade)

    top_students = df[df["Average"] > 75]
    return top_students.sort_values("Average", ascending=False)


if __name__ == "__main__":
    data = {
        "Name": ["Anu", "Bala", "Charan", "Divya", "Eshan"],
        "Math": [85, 45, 78, 92, 60],
        "Science": [88, 55, 72, 95, 58],
        "English": [90, 40, 70, 93, 65]
    }

    df = pd.DataFrame(data)
    print(analyze_students(df))
