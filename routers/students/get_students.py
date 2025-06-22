from fastapi import APIRouter,HTTPException
from starlette.responses import JSONResponse

from app.logger import setup_logging
import logging


setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()

@router.get("/get_all_students")
def get_all_students():
    logger.info("Request Received to get all students info")
    return JSONResponse(
        status_code=200,
        content={"message":"Testing OK"}
    )

@router.get("/get_students_by_id/{student_id}")
def get_students_by_id(student_id:int):
    logger.info("Request Received to get student by id")
    return JSONResponse(
        status_code=200,
        content={"message":"Testing OK"}
    )