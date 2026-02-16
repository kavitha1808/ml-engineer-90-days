class Course:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def enroll(self, course):
        if len(self.courses) < 5 and course.capacity > 0:
            self.courses.append(course.name)
            course.capacity -= 1


class GraduateStudent(Student):
    def enroll(self, course):
        if len(self.courses) < 7 and course.capacity > 0:
            self.courses.append(course.name)
            course.capacity -= 1


c1 = Course("AI", 2)
s = GraduateStudent("Kavitha")
s.enroll(c1)
print(s.courses)
