from db import session
from sqlalchemy import desc, func
from models import Teacher, Group, Student, Subject, Grade


def select_1():
    result = session.query(Student.fullname, func.avg(Grade.grade).label('avg_score')) \
    .join(Grade) \
    .group_by(Student.id) \
    .order_by(func.avg(Grade.grade).desc()) \
    .limit(5) \
    .all()

    return result

def select_2():
   result = session.query(Student.fullname, func.avg(Grade.grade).label('avg_score')) \
    .join(Grade) \
    .group_by(Student.id) \
    .order_by(func.avg(Grade.grade).desc()) \
    .first()
   
   return result


def select_3():
    result = session.query(Group.name, func.avg(Grade.grade).label('avg_score')) \
    .join(Student, Group.students) \
    .join(Grade, Student.grades_received) \
    .join(Subject, Grade.subject) \
    .filter(Subject.id == 4) \
    .group_by(Group.name) \
    .all()
   
    return result
    


def select_4():
    result = session.query(func.avg(Grade.grade).label('avg_score')).scalar()
    return f'Середній бал на потоці {result}'

def select_5():
    result = session.query(Subject.name) \
    .join(Teacher, Subject.teacher) \
    .filter(Teacher.id == 1) \
    .all()

    return f'Викладач під першим id веде такі предмети: {result}'

def select_6():
    result = session.query(Student.fullname) \
    .join(Group, Student.group) \
    .filter(Group.id == 3) \
    .all()
   
    return result

def select_7():
    result = session.query(Student.fullname, Grade.grade) \
    .join(Group, Student.group) \
    .join(Grade, Student.grades_received) \
    .join(Subject, Grade.subject) \
    .filter(Group.id == 2, Subject.id == 2) \
    .all()

    return result

def select_8():
    result = session.query(func.avg(Grade.grade).label('avg_score')) \
    .join(Subject, Grade.subject) \
    .join(Teacher, Subject.teacher) \
    .filter(Teacher.id == 3) \
    .scalar()

    return result

def select_9():
    result = session.query(Subject.name) \
    .join(Grade, Subject.grades) \
    .join(Student, Grade.student) \
    .filter(Student.id == 17) \
    .all()

    return set(result)

def select_10():
    result = session.query(Subject.name) \
    .join(Teacher, Subject.teacher) \
    .join(Grade, Subject.grades) \
    .join(Student, Grade.student) \
    .filter(Teacher.id == 2, Student.id == 23) \
    .all()

    return set(result)



def main():
    funcs = {'1': select_1(), '2': select_2(), '3': select_3(), '4': select_4(), '5': select_5(), '6': select_6(), '7': select_7(), '8': select_8(), '9': select_9(), '10': select_10()}
    while True:
        print('Для закриття 0')
        result = input('Введіть номер запиту:>>>')
        if result:
            print(funcs.get(result))
        if result == '0':
            break


if __name__ == '__main__':
    main()
