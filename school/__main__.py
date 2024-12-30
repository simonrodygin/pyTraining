from faker import Faker
from credentials import Credentials
from director import Director
from student import Student
from teacher import Teacher
from user import User

def main():
    fake = Faker()
    # Нанимаем директора
    mcgill_creds = Credentials(fake.text(), fake.text())
    mr_mcgill = Director('Michel McGill', mcgill_creds, 95000)

    # Принимаем учеников
    peter_creds = Credentials(fake.text(), fake.text())
    mr_bankman = mr_mcgill.accept('Peter Bankman', peter_creds)

    tyron_creds = Credentials(fake.text(), fake.text())
    mr_smith = mr_mcgill.accept('Tyron Smith', tyron_creds)

    # Нанимаем учителей
    shvets_creds = Credentials(fake.text(), fake.text())
    mrs_shvets = mr_mcgill.hire('Helen Shvets', shvets_creds, 65000)

    ortega_creds = Credentials(fake.text(), fake.text())
    mrs_ortega = mr_mcgill.hire('Maria Ortega', ortega_creds, 75000)

    # Учебный процесс
    for i in range(10):
        mrs_shvets.teach(mr_bankman)
        if i % 2 == 0 and i % 5 == 0:
            mrs_shvets.teach(mr_smith)
            mrs_shvets.grade(mr_smith, 3)
        elif i % 2 == 0:
            mrs_shvets.teach(mr_smith)
        elif i % 5 == 0:
            mrs_shvets.grade(mr_bankman, 5)
        else:
            mr_smith.skip_class()

    for i in range(15):
        mrs_ortega.teach(mr_smith)
        if i % 3 == 0 and i % 7 == 0:
            mrs_ortega.teach(mr_bankman)
            mrs_ortega.grade(mr_bankman, 4)
        elif i % 2 == 0:
            mrs_ortega.teach(mr_bankman)
        elif i % 5 == 0:
            mrs_ortega.grade(mr_smith, 6)
        else:
            mr_bankman.skip_class()

    # Повышаем зп
    mr_mcgill.raise_salary(5000, mrs_ortega)

    # Смотрим стату по школе
    print(f'средняя оценка {Student.average_grade}')
    print(f'средняя зп {Teacher.average_salary}')
    print(f'всего учителей {Teacher.teacher_amount}')
    print(f'всего студентов {Student.student_amount}')
    print(f'всего пользователей {User.user_amount}')
    print(f'карма директора {mr_mcgill.karma}')

    # Увольняем одного учителя и исключаем одного ученика
    mr_mcgill.fire_expel(mrs_ortega)
    mr_mcgill.fire_expel(mr_smith)
    print(f'всего учителей {Teacher.teacher_amount}')
    print(f'всего студентов {Student.student_amount}')
    print(f'всего пользователей {User.user_amount}')
    print(f'карма директора {mr_mcgill.karma}')
    print(mrs_ortega.active)
    print(mr_smith.active)


if __name__ == "__main__":
    main()