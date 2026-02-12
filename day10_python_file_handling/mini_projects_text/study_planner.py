file = open("study_plan.txt", "a")

day = input("Enter day: ")
task = input("Enter study task: ")

file.write(day + " : " + task + "\n")
file.close()

print("Study plan saved!")

file = open("study_plan.txt", "r")
print("\n--- STUDY PLAN ---")
print(file.read())
file.close()
