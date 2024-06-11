from sqlalchemy import func, desc, select, and_

from conf.models import Student, Group, Teacher, Grade, Subject
from conf.db import session


def  select_1 ():
    """
        Найти 5 студентов с самым средним баллом по всем предметам.
    """
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade'))\
        .select_from(Student).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()    
    
    return result

def  select_2 ():
    """
        Найти студента с высоким средним баллом по определенному предмету.
    """
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade'))\
        .select_from(Grade).join(Student).filter(Grade.subject_id == 1).group_by(Student.id).order_by(desc('average_grade')).limit(1).all()    
    
    return result


def  select_3 ():
    """
        Найти средний балл в группах по определенному предмету.
    """
    result = session.query(Student.group_id, func.round(func.avg(Grade.grade), 2).label('average_grade'))\
        .select_from(Grade).join(Student).filter(Grade.subject_id == 1).group_by(Student.group_id).order_by(Student.group_id).all()    
    
    return result

    
def  select_4 ():
    """
        Найдите средний балл на потоке (по всей таблице оценок).
    """
    
    result = session.query(func.round(func.avg(Grade.grade), 2).label('average_grade'))\
        .select_from(Grade).all()    
    
    return result

    
def  select_5 ():
    """
        Найти какие курсы читает определенный преподаватель.
    """

    result = session.query(Teacher.fullname, Subject.name)\
        .select_from(Teacher).join(Subject).filter(Teacher.id == 1).all()    
    
    return result

    
def  select_6 ():
    """
        Найдите список студентов в определенной группе.
    """
    result = session.query(Student.fullname)\
        .select_from(Student).filter(Student.group_id == 1).all()    
    
    return result


def  select_7 ():
    """
        Найти оценки студентов в отдельной группе по определенному предмету.
    """

    result = session.query(Student.fullname, Grade.grade)\
        .select_from(Student).join(Grade).filter(and_(Student.group_id == 1, Grade.subject_id == 1)).all()    
    
    return result

    
def  select_8 ():
    """
        Найдите средний балл, который ставит определенный преподаватель по своим предметам.
    """
    result = session.query(Teacher.fullname, Subject.name, func.round(func.avg(Grade.grade), 2).label('average_grade'))\
        .select_from(Teacher).join(Subject).join(Grade).filter(Teacher.id == 1).group_by(Teacher.fullname, Subject.name).all()    
    
    return result


def  select_9 ():
    """
        Найдите список курсов, которые посещает студент.
    """

    result = session.query(Subject.name)\
        .select_from(Grade).join(Subject).filter(Grade.student_id == 1).group_by(Subject.id).all()    
    
    return result
    
def  select_10 ():
    """
        Список курсов, которые студенту читает определенный преподаватель.
    """
    result = session.query(Subject.name)\
        .select_from(Grade).join(Subject).filter(and_(Subject.teacher_id == 1, Grade.student_id == 1)).group_by(Subject.name).all()    
    
    return result

    
# additional tasks
def  select_11 ():
    """
        Средний балл, который определенный преподаватель ставит студенту.
    """

    result = session.query(Teacher.fullname, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade'))\
        .select_from(Grade).join(Student).join(Subject).join(Teacher)\
        .filter(and_(Grade.student_id == 1, Teacher.id == 1)).group_by(Student.fullname, Teacher.fullname).all()    
    
    return result


def  select_12 ():
    """
        Оценки студентов в определенной группе по определенному предмету на последнем занятии.
    """
    subquery = (select(func.max(Grade.grade_date)).join(Student).filter(and_(
        Grade.subjects_id == 2, Student.group_id == 3
    ))).scalar_subquery()

    result = session.query(Student.id, Student.fullname, Grade.grade, Grade.grade_date) \
        .select_from(Grade) \
        .join(Student) \
        .filter(and_(Grade.subjects_id == 2, Student.group_id == 3, Grade.grade_date == subquery)).all()

    return result


if "__name__" == "__main__":
    print(select_1())
    print(select_2())
    print(select_3())
    print(select_4())
    print(select_5())
    print(select_6())
    print(select_7())
    print(select_8())
    print(select_9())
    print(select_10())
    print(select_11())
    print(select_12()) 