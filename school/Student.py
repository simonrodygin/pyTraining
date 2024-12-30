from user import User
from credentials import Credentials

class Student(User):
    student_amount = 0
    grades = []  
    average_grade = 0
    
    def __init__(self, name: str, credentials: Credentials):
        super().__init__(name, credentials)
        Student.student_amount += 1
        self.knowledge = 0
        self.grades = []
        self.average_grade = 0

    def skip_class(self):
        self.knowledge -= 1
        print(f'{self.name} knowledge decreased to {self.knowledge}')
