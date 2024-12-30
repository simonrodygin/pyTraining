from teacher import Teacher
from student import Student
from user import User
from credentials import Credentials
from utils import average_in_list

class Director(Teacher):
    def raise_salary(self, raise_size: int, teacher: Teacher):
        teacher.salary += raise_size
        print(f'{teacher.name} salary increased to {teacher.salary} from {teacher.salary - raise_size}')
        Teacher.salaries.update({teacher.name: teacher.salary})
        Teacher.average_salary = average_in_list(list(Teacher.salaries.values()))

    def __init__(self, name: str, credentials: Credentials, salary: int):
        super().__init__(name, credentials, salary)
        Teacher.salaries.pop(name)
        Teacher.average_salary = average_in_list(list(Teacher.salaries.values()))
        Teacher.teacher_amount -= 1
        self.karma = 0
        print(f'{name} became director in our school')
    
    def hire(self, name: str, credentials: Credentials, salary: int):
        self.karma += 1

        print(f'{name} became teacher in our school')
        return Teacher(name, credentials, salary)
    
    def accept(self, name: str, credentials: Credentials): 
        self.karma += 1

        print(f'{name} became student in our school')
        return Student(name, credentials)
    
    # Можно ли удалить объект?
    def fire_expel(self, user):
        user.active = False
        self.karma -= 2
        print(f'{user.name} left our school')
        User.user_amount -= 1
        if type(user) is Teacher:
            Teacher.teacher_amount -= 1
        if type(user) is Student:
            Student.student_amount -= 1
