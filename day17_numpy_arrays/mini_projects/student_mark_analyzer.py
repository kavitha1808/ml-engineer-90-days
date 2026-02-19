import numpy as np

# Rows = Students, Columns = Subjects
marks = np.array([
    [85, 78, 92],
    [56, 45, 60],
    [90, 88, 94],
    [30, 40, 35]
])

# Student average
student_avg = np.mean(marks, axis=1)

# Subject average
subject_avg = np.mean(marks, axis=0)

# Topper
topper_index = np.argmax(student_avg)

# Failed students
fail_students = np.where(student_avg < 40)[0]

print("Student Average:", student_avg)
print("Subject Average:", subject_avg)
print("Topper Index:", topper_index)
print("Failed Students Index:", fail_students)
