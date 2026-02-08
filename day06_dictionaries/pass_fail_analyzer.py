# Mini Project 3: Pass / Fail Analyzer

marks = {
    "Maths": 45,
    "Science": 72,
    "English": 30,
    "Social": 66
}

for subject, score in marks.items():
    if score >= 40:
        print(subject, ": Pass")
    else:
        print(subject, ": Fail")
