import User
import Student
import Credentials
from functions import average

class Teacher(User):
    teacher_amount = 0
    salaries = {}
    average_salary = 0
    
    def __init__(self, name: str, credentials: Credentials, salary: int):
        super(Teacher, self).__init__(name, credentials)
        self.salary = salary
        Teacher.salaries.update({name: self.salary})
        Teacher.average_salary = average(list(Teacher.salaries.values()))

    def teach(self, student: Student):
        student.knowledge += 1
        print(f'{student.name} knowledge increased to {student.knowledge} by {self.name}')

    def grade(self, student: Student, grade: int):
        Student.grades.append(grade)
        student.grades.append(grade)
        Student.average_grade = average(Student.grades)
        student.average_grade = average(student.grades)
        print(f'{student.name} was graded {grade} by {self.name}. Now his/her average grade is {student.average_grade}')
