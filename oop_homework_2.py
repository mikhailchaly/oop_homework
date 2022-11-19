class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python', 'Git']

lecturer_1 = Lecturer('Mariy', 'Serova')
lecturer_1.courses_attached =['Django']

student_2 = Student('Petr', 'Smirnov', 'your_gender')
student_2.courses_in_progress += ['Django']
student_2.rate_hw(lecturer_1, 'Django', 9)

reviewer_1 = Reviewer('Ivan', 'Petrov')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Gleb', 'Bokov')
reviewer_2.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 4)

reviewer_2.rate_hw(student_1, 'Git', 4)

print(student_1.grades)
print(lecturer_1.grades)

