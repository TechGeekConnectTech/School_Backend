from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from db.schemas.schemas import StudentBase
from app.logger import setup_logging
import logging
from db.services.student_service import StudentServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()

@router.patch("/update_student_record_by_emailid")
def patch_update_student_record(student:StudentBase,db:Session=Depends(get_db)):
    logger.info("Request Received to update student record")
    records=StudentServiceManager.update_student_details_by_email_id(db,student.student_name,student.student_email)
    if records:
        return_list = []
        for student in records:
            student_data = {}
            student_data['student_id'] = student.student_id
            student_data['student_name'] = student.student_name
            student_data['student_email'] = student.student_email
            return_list.append(student_data)

        return JSONResponse(
            status_code=201,
            content={"message": return_list}
        )
    else:
        raise HTTPException(status_code=500,detail="Error in updating Student Record")


