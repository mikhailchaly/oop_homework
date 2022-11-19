class Student:
    list_student = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0
        Student.list_student.append(self)


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

    def _average_rating(self):
        summa = 0
        k = 0
        for elem in self.grades.values():
            summa += sum(elem)
            k += len(elem)
            if k > 0:
                return round(summa / k, 2)
            else:
                return "Оценок пока нет"


    def __str__(self):
        return f"\nИмя: {self.name}\nФамииля: {self.surname}\nСредняя оценка за домашнее задание: {self._average_rating()}\n" \
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {','.join(self.finished_courses)}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Нет такого студента")
            return
        return self._average_rating() < other._average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    list_lecturer = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.list_lecturer.append(self)

    def _average_rating(self):
        summa = 0
        k = 0
        for elem in self.grades.values():
            summa += sum(elem)
            k += len(elem)
            if k > 0:
                return round(summa / k, 2)
            else:
                return "Оценок пока нет"

    def __str__(self):
        return f"\nИмя: {self.name}\nФамилия: {self.surname}\nСредний бал за лекции: {self._average_rating()}\n"


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("no lecturer")
            return
        return self._average_rating() < other._average_rating()


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

    def __str__(self):
        return f"\nИмя: {self.name}\nФамилия: {self.surname}"


student_1 = Student('Ruoy', 'Eman', 'male_gender')
student_2 = Student('Petr', 'Smirnov', 'male_gender')
lecturer_1 = Lecturer('Mariy', 'Serova')
lecturer_2 = Lecturer('Cvetlana', 'Gorkina')
reviewer_1 = Reviewer('Ivan', 'Petrov')
reviewer_2 = Reviewer('Gleb', 'Bokov')


student_1.courses_in_progress += ['Python', 'Git']
student_2.courses_in_progress += ['Django', 'Git']

student_1.finished_courses += ['English language']
student_2.finished_courses += ['English language']

lecturer_1.courses_attached = ['Django', "Python"]
lecturer_2.courses_attached = ['Git', "Django"]

reviewer_1.courses_attached += ['Python', 'Django']
reviewer_2.courses_attached += ['Git', 'Django', "Python"]

student_2.rate_hw(lecturer_1, 'Django', 9)
student_2.rate_hw(lecturer_1, 'Django', 7)

student_1.rate_hw(lecturer_2, 'Git', 10)
student_1.rate_hw(lecturer_2, 'Git', 8)

reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 4)

reviewer_2.rate_hw(student_1, 'Git', 4)
reviewer_2.rate_hw(student_2, 'Django', 5)
reviewer_2.rate_hw(student_2, 'Django', 3)


print(f"{student_1.surname} окончил {', '.join(student_1.finished_courses)}")
print(f"{student_2.surname} окончил {', '.join(student_2.finished_courses)}")
print(f"{student_1.surname} изучает {', '.join(student_1.courses_in_progress)}")
print(f"{student_2.surname} изучает {', '.join(student_2.courses_in_progress)}")
print(f"{lecturer_1.surname} преподает {', '.join(lecturer_1.courses_attached)}")
print(f"{lecturer_2.surname} преподает {', '.join(lecturer_2.courses_attached)}")
print(f"{reviewer_1.surname} проверяет работы {', '.join(reviewer_1.courses_attached)}")
print(f"{reviewer_2.surname} проверяет работы {', '.join(reviewer_2.courses_attached)}")
print()
print(f"{student_1.surname} предмет : оценки {student_1.grades}")
print(f"{student_2.surname} предмет : оценки {student_2.grades}")
print(f"{lecturer_1.surname} лекции : балы {lecturer_1.grades}")
print(f"{lecturer_2.surname} лекции : балы {lecturer_2.grades}")
print()

def average_grade_for_homework(course = "Git"):
    general_list = []
    for student in Student.list_student:
        if course in student.courses_in_progress or course in student.finished_courses:
            for grade in student.grades[course]:
                general_list.append(grade)
                medium = sum(general_list) / len(general_list)
                return print(medium)
average_grade_for_homework()

def average_mark_for_lectures(course = "Django"):
    general_list = []
    for lecturer in Lecturer.list_lecturer:
        if course in lecturer.courses_attached:
            for grade in lecturer.grades[course]:
                general_list.append(grade)
                medium = sum(general_list) / len(general_list)
                return print(medium)
average_mark_for_lectures()









