from utils.marks import calculate_average
from utils.grade import assign_grade

marks = [78, 82, 90]
avg = calculate_average(marks)

print("Average:", avg)
print("Grade:", assign_grade(avg))
