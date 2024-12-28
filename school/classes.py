def average(list):
    if len(list) == 0:
        return 0
    else:
        return sum(list) / len(list)

class Credentials():
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

class User:
    user_amount = 0
    
    def __init__(self, name: str, credentials: Credentials):
        User.user_amount += 1
        print('new user was made')
        self.active = True
        self.name = name
        self.credentials = credentials

class Student(User):
    student_amount = 0
    grades = []  
    average_grade = 0
    
    def __init__(self, name: str, credentials: Credentials):
        super(Student, self).__init__(name, credentials)
        self.knowledge = 0
        self.grades = []
        self.average_grade = 0

    def skip_class(self):
        self.knowledge -= 1
        print(f'{self.name} knowledge decreased to {self.knowledge}')

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

class Director(Teacher):
    def raise_salary(self, raise_size: int, teacher: Teacher):
        teacher.salary += raise_size
        print(f'{teacher.name} salary increased to {teacher.salary} from {teacher.salary - raise_size}')
        Teacher.salaries.update({teacher.name: teacher.salary})
        Teacher.average_salary = average(list(Teacher.salaries.values()))

    def __init__(self, name: str, credentials: Credentials, salary: int):
        super(Director, self).__init__(name, credentials, salary)
        Teacher.salaries.pop(name)
        Teacher.average_salary = average(list(Teacher.salaries.values()))
        self.karma = 0
        print(f'{name} became director in our school')
    
    def hire(self, name: str, credentials: Credentials, salary: int):
        self.karma += 1
        Teacher.teacher_amount += 1

        print(f'{name} became teacher in our school')
        return Teacher(name, credentials, salary)
    
    def accept(self, name: str, credentials: Credentials): 
        self.karma += 1
        Student.student_amount += 1

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
        del user
