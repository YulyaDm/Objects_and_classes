class Student:
  def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}

  def rate_lecturer(self, lecturer, course, grades_lectur):
      if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
          if course in lecturer.grades_lecturer:
              lecturer.grades_lecturer[course] += [grades_lectur]
          else:
              lecturer.grades_lecturer[course] = [grades_lectur]
      else:
          return 'Ошибка'

  def average_grade_student(self):
      return sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))

  def __str__(self):
      return (f'Имя: {self.name}\n'
              f'Фамилия: {self.surname}\n'
              f'Средняя оценка за домашние задания: {self.average_grade_student()}\n'
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
              f'Завершенные курсы: {", ".join(self.finished_courses)}')

  def __lt__(self, other):
      return self.average_grade_student() < other.average_grade_student()

class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []

class Lecturer(Mentor):
  def __init__(self, name, surname):
      super().__init__(name, surname)
      self.grades_lecturer = {}

  def average_grade_lecturer(self):
      return sum(sum(self.grades_lecturer.values(), [])) / len(sum(self.grades_lecturer.values(), []))

  def __str__(self):
      return (f'Имя: {self.name}\n'
              f'Фамилия: {self.surname}\n'
              f'Средняя оценка за лекции: {self.average_grade_lecturer()}\n')

  def __lt__(self, other):
      return self.average_grade_lecturer() < other.average_grade_lecturer()

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
      return (f'Имя: {self.name}\n'
              f'Фамилия: {self.surname}')


def average_grade_all_students(students, course):
  all_grades = []
  for student in students:
    if course in student.grades:
      all_grades += student.grades[course]
    if all_grades:
      result = sum(all_grades) / len(all_grades)
      return result
    


def average_grade_all_lectors(lectors, course):
  all_grades = []
  for lector in lectors:
    if course in lector.grades_lecturer:
      all_grades += lector.grades_lecturer[course]
    if all_grades:
      result = sum(all_grades) / len(all_grades)
      return result
    


student_1 = Student('Marina', 'Ivanova', 'famale')
student_1.courses_in_progress += (['Финансовый аналитик'])
student_1.finished_courses = ['Маркетинг']

student_2 = Student('Alexandr', 'Dmitriev', 'male')
student_2.courses_in_progress += ['Дизайнер интерьера']
student_2.finished_courses = ['Дизайн']

rewiewer_1 = Reviewer('Konstantin', 'Pivkin')
rewiewer_1.courses_attached += ['Финансовый аналитик']

rewiewer_2 = Reviewer('Olga', 'Dubova')
rewiewer_2.courses_attached += ['Дизайнер интерьера']

lecturer_1 = Lecturer('Vladimir', 'Surkov')
lecturer_1.courses_attached += ['Финансовый аналитик']

lecturer_2 = Lecturer('Antonina', 'Petrova')
lecturer_2.courses_attached += ['Дизайнер интерьера']

student_1.rate_lecturer(lecturer_1, 'Финансовый аналитик', 10)
student_1.rate_lecturer(lecturer_1, 'Финансовый аналитик', 8)

student_2.rate_lecturer(lecturer_2, 'Дизайнер интерьера', 9)
student_2.rate_lecturer(lecturer_2, 'Дизайнер интерьера', 10)

rewiewer_1.rate_hw(student_1, 'Финансовый аналитик', 8)
rewiewer_1.rate_hw(student_1, 'Финансовый аналитик', 7)

rewiewer_2.rate_hw(student_2, 'Дизайнер интерьера', 7)
rewiewer_2.rate_hw(student_2, 'Дизайнер интерьера', 7)

students = []
students.append(student_1)
students.append(student_2)

lectors = []
lectors.append(lecturer_1)
lectors.append(lecturer_2)

lecturer_average_financial = average_grade_all_lectors(lectors, 'Финансовый аналитик')
lecturer_average_design = average_grade_all_lectors(lectors, 'Дизайнер интерьера')

student_average_financial = average_grade_all_students(students, 'Финансовый аналитик')
student_average_design = average_grade_all_students(students, 'Дизайнер интерьера')

print(student_1.__str__())
print(student_2.__str__())
print(lecturer_1.__str__())
print(lecturer_2.__str__())
print(rewiewer_1.__str__())
print(rewiewer_2.__str__())

print(student_1 > student_2)
print(student_1 < student_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 < lecturer_2)

print(lecturer_average_financial)
print(lecturer_average_design)
print(student_average_financial)
print(student_average_design)