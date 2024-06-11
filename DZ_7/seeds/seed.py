import logging
import random
from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Grade, Teacher, Student, Group, Subject

fake = Faker('uk-Ua')

# group
def insert_groups():
    for _ in range(3):
        group = Group( name=fake.word())
        session.add(group)


# teacher
def insert_teachers():
    for _ in range(3):
        teacher = Teacher( fullname=fake.name())
        session.add(teacher)


# subject
def insert_subjects():
    teachers = session.query(Teacher).all()
    
    for _ in range(5):
        subject = Subject(
            name = fake.word(),
            teacher_id = random.choice(teachers).id
            )
        session.add(subject)
        

# student
def insert_students():
    groups = session.query(Group).all()
    
    for _ in range(40):
        student = Student(
            fullname = fake.name(),
            group_id = random.choice(groups).id
            )
        session.add(student) 
        

#grade 
def insert_grades():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    
    for student in students:
        number_of_grades = random.randint(10, 20)
        for _ in range(number_of_grades):
            grade = Grade(
                grade = random.randint(0, 300),
                grade_date = fake.date_this_decade(),
                student_is=student.id,
                subjects_id = random.choice(subjects).id
                )
            
            session.add(grade)
            
if __name__ == '__main__':
    try:
        # Добавление групп
        insert_groups()
        # Добавление учителей
        insert_teachers()
        session.commit()
        
        # Добавление предметов
        insert_subjects()
        # Добавление студентов
        insert_students()
        session.commit
        
        # Добавление оценок
        insert_grades()
        session.commit()
        
    except SQLAlchemyError as e:
        logging.error(e)
        session.rollback()
    finally:
        session.close()       