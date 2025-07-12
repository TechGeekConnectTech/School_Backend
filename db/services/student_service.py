from db.model import models as M
from sqlalchemy.orm import Session
from db.services.base_service import BaseService


class StudentServiceManager:
    def display_all_student_details(db: Session):
        q=db.query(M.StudentManager)
        try:
            return q.all()
        except Exception as e:
            return None