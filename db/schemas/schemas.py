from pydantic import BaseModel

class StudentBase(BaseModel):
    student_name:str
    student_email:str

class DeleteStudentBase(BaseModel):
    student_email:str

class CourseBase(BaseModel):
    course_name:str
