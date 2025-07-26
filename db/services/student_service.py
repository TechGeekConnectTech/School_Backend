from db.model import models as M
from sqlalchemy.orm import Session
from sqlalchemy import select

from db.model.models import StudentManager
from db.schemas.schemas import StudentBase
from db.services.base_service import BaseService


class StudentServiceManager:
    def display_all_student_details(db: Session):
        q=db.query(M.StudentManager)
        try:
            return q.all()
        except Exception as e:
            return None

    def display_student_details_by_name(db: Session,student_name):
        q = db.query(M.StudentManager).filter_by(student_name=student_name).first()
        try:
            return q
        except Exception as e:
            return None

    def display_student_details_by_id(db: Session,student_id:int):
        q = db.query(M.StudentManager).filter_by(student_id=student_id).first()
        try:
            return q
        except Exception as e:
            return None


    def insert_student_details(db:Session,student_name,student_email):
        try:
            student=M.StudentManager(student_name=student_name,student_email=student_email)
            db.add(student)
            db.commit()
            q = db.query(M.StudentManager)
            return q.all()
        except Exception as e:
            return None

    def update_student_details_by_email_id(db:Session,student_name,student_email):
        try:
            student=db.query(M.StudentManager).filter_by(student_email=student_email).first()
            if student:
                student.student_name=student_name
                db.commit()
                q = db.query(M.StudentManager)
                return q.all()
            else:
                return None
        except Exception as e:
            return None

    def delete_student_details_by_email_id(db:Session,student_email):
        try:
            student=db.query(M.StudentManager).filter_by(student_email=student_email).first()
            if student:
                db.delete(student)
                db.commit()
                q = db.query(M.StudentManager)
                return q.all()
            else:
                return None
        except Exception as e:
            return None
