class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and 0 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        all_grades = list(sum(self.grades.values(), []))
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_grades()}\n' \
              f'Курсы в процессе изучения: ' + \
              ', '.join(self.courses_in_progress) + \
              f'\nЗавершенные курсы: ' + \
              ', '.join(self.finished_courses)
        return res

    def __lt__(self, student):
        if isinstance(student, Student):
            return self.average_grades() < student.average_grades()
        else:
            return 'Ошибка'

    def __eq__(self, student):
        if isinstance(student, Student):
            return self.average_grades() == student.average_grades()
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        return Student.average_grades(self)

    def __str__(self):
        res = super().__str__() + f'\nСредняя оценка за лекции: {self.average_grades()}'
        return res
    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.average_grades() < lecturer.average_grades()
        else:
            return 'Ошибка'
        pass
    def __eq__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.average_grades() == lecturer.average_grades()
        else:
            return 'Ошибка'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Git', 10)

some_student.rate_hw(some_lecturer, 'Python', 10)

print(some_reviewer)
print(some_lecturer)
print(some_student)
