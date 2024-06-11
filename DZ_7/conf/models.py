from sqlalchemy import Colum, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = "teachers"
    id = Colum(Integer, primary_key=True)
    fullname = Colum(String(150), nullable =False)
    

class Group(Base):
    __tablename__ = "groups"
    id = Colum(Integer, primary_key=True)
    name = Colum(String(50), nullable =False)
    
    
class Student(Base):
   __tablename__ = "students"
   id = Colum(Integer, primary_key=True)
   fullname = Colum(String(150), nullable =False)   
   group_id = Colum('group_id', ForeignKey('groups.id', ondelete='CASCADE', onupdate='CASCADE'))
   group = relationship('Group', backref='students')
   
   
class Subject(Base):
   __tablename__ = "subjects"
   id = Colum(Integer, primary_key=True)
   name = Colum(String(150), nullable =False)   
   teacher_id = Colum('teacher_id', ForeignKey('teachers.id', ondelete='CASCADE', onupdate='CASCADE'))
   teacher = relationship('Teacher', backref='disciplines')
   
   
class Grade(Base):
   __tablename__ = "grades"
   id = Colum(Integer, primary_key=True)
   grade = Colum(Integer, nullable=False)
   grade_date = Colum('grade_date', Date, nullable =False)   
   student_id = Colum('student_id', ForeignKey('students.id', ondelete='CASCADE', onupdate='CASCADE'))
   subject_id = Colum('subject_id', ForeignKey('subjects.id', ondelete='CASCADE', onupdate='CASCADE'))
   student = relationship('Student', backref='grade')
   subject = relationship('Subject', backref='grade')