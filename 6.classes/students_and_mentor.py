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
    def __float__(self):
        return self.average_grades()

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
            return float(self) < float(lecturer)
        else:
            return 'Ошибка'
        pass
    def __eq__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return float(self) == float(lecturer)
        else:
            return 'Ошибка'
    def __float__(self):
        return self.average_grades()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def average_grades_students(students):
    res = sum([float(student) for student in students]) / len(students)
    return res

def average_grades_lecturers(lecturers):
    res = sum([float(lecturer) for lecturer in lecturers]) / len(lecturers)
    return res

first_student = Student('Ruoy', 'Eman', 'your_gender')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']
first_student.finished_courses += ['Введение в программирование']

second_student = Student('Evgeniy', 'Vakulenko', 'male')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']
second_student.finished_courses += ['Введение в программирование']

first_lecturer = Lecturer('Some', 'Buddy')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Jupalo', 'Marjupalo')
second_lecturer.courses_attached += ['Git']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

some_reviewer.rate_hw(first_student, 'Python', 9)
some_reviewer.rate_hw(first_student, 'Python', 10)
some_reviewer.rate_hw(first_student, 'Python', 9)
some_reviewer.rate_hw(first_student, 'Git', 10)

some_reviewer.rate_hw(second_student, 'Python', 8)
some_reviewer.rate_hw(second_student, 'Python', 4)
some_reviewer.rate_hw(second_student, 'Python', 9)
some_reviewer.rate_hw(second_student, 'Git', 10)

first_student.rate_hw(first_lecturer, 'Python', 10)
first_student.rate_hw(second_lecturer, 'Git', 10)

second_student.rate_hw(first_lecturer, 'Python', 8)
second_student.rate_hw(second_lecturer, 'Git', 6)

print(some_reviewer)
print()
print(first_lecturer)
print()
print(second_lecturer)
print()
print(first_student)
print()
print(second_student)
print()

if first_lecturer > second_lecturer:
    best_lecturer = first_lecturer
else:
    best_lecturer = second_lecturer
print(f'Лучший лектор:\n{best_lecturer}')
print()
print(f'Средняя оценка за домашние задания студентов: {average_grades_students([first_student, second_student])}')
print()
print(f'Средняя оценка за лекции всех лекторов: {average_grades_lecturers([first_lecturer, second_lecturer])}')
