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
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

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


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['English language']

lecturer_1 = Lecturer('Mariy', 'Serova')
lecturer_1.courses_attached = ['Django']
lecturer_2 = Lecturer('Cvetlana', 'Gorkina')
lecturer_2.courses_attached = ['Git']

student_2 = Student('Petr', 'Smirnov', 'your_gender')
student_2.courses_in_progress += ['Django']
student_2.finished_courses += ['Git']
student_2.rate_hw(lecturer_1, 'Django', 9)
student_2.rate_hw(lecturer_1, 'Django', 5)
student_2.rate_hw(lecturer_1, 'Django', 2)

student_1.rate_hw(lecturer_2, 'Git', 8)

reviewer_1 = Reviewer('Ivan', 'Petrov')
reviewer_1.courses_attached += ['Python', 'Django']

reviewer_2 = Reviewer('Gleb', 'Bokov')
reviewer_2.courses_attached += ['Git', 'Django']

reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 4)

reviewer_2.rate_hw(student_1, 'Git', 4)
reviewer_2.rate_hw(student_2, 'Django', 5)
reviewer_2.rate_hw(student_2, 'Django', 3)

#print(student_1.grades)
#print(student_2.grades)
#print(lecturer_1.grades)
#print(lecturer_2.grades)

print(reviewer_2)

print(lecturer_1)

print(student_1)

print(student_2)
print()
print(student_1.__lt__(student_2))
print(lecturer_1.__lt__(lecturer_2))



