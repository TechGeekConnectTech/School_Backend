from sqlalchemy import Column,Integer,String
from db import Base

class StudentManager(Base):
    __tablename__='students'
    student_id=Column(Integer,primary_key=True)
    student_name=Column(String(20))
    student_email=Column(String(50),unique=True)

class CourseManager(Base):
    __tablename__='course'
    course_id=Column(Integer,primary_key=True)
    course_name=Column(String(20))