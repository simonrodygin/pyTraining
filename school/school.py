# работает с таким импортом
from classes import Credentials
from classes import Director
from classes import Student
from classes import Teacher
from classes import User
# но не работает с импортом типа этого. Хочу чтобы классы были в разных файлах но не могу(
#import Credentials
#import Director
#import Student
#import Teacher
#import User

# Нанимаем директора
mcgill_creds = Credentials('bazuka', 'director228')
mr_mcgill = Director('Michel McGill', mcgill_creds, 95000)

# Принимаем учеников
peter_creds = Credentials('kazanova', 'yo_mama4325')
mr_bankman = mr_mcgill.accept('Peter Bankman', peter_creds)

tyron_creds = Credentials('nagibator', 'streetD.O.G')
mr_smith = mr_mcgill.accept('Tyron Smith', tyron_creds)

# Нанимаем учителей
shvets_creds = Credentials('pchelka', 'supersafepassword123')
mrs_shvets = mr_mcgill.hire('Helen Shvets', shvets_creds, 65000)

ortega_creds = Credentials('chikita', 'i333love7565bowling73482')
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


