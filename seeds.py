import random

from sqlalchemy.exc import SQLAlchemyError
from models import Teacher, Student, Group, Subject, Grade
from db import session
from faker import Faker

fake = Faker()

def create_data():
    teachers = [Teacher(fullname=fake.name()) for _ in range(3)]
    session.add_all(teachers)
    session.commit()

    groups = [Group(name=fake.word()) for _ in range(1, 4)]
    session.add_all(groups)
    session.commit()

    group_ids = session.query(Group).all()
    print([group_ids.name for group_ids in group_ids])

    students = [Student(fullname=fake.name(), group_id=random.choice(group_ids).id) for _ in range(30)]
    session.add_all(students)
    session.commit()

    teacher_ids = session.query(Teacher).all()

    subjects = [Subject(name=fake.word(), teacher_id=random.choice(teacher_ids).id) for _ in range(8)]
    session.add_all(subjects)
    session.commit()

    students_for_grades = session.query(Student).all()
    subjects_for_grades = session.query(Subject).all()

    for student in students_for_grades:
        for subject in subjects_for_grades:
            grades = [Grade(grade=random.uniform(2, 5), date=fake.date_this_year(), student_id=student.id, subjects_id=subject.id) for _ in range(random.randint(1, 20))]
            session.add_all(grades)
    

if __name__ == '__main__':
    try:
        create_data()
        session.commit()
    except SQLAlchemyError as err:
        print(err)
        session.rollback()
    finally:
        session.close()
