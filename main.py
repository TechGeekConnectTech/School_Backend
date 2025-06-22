from fastapi import FastAPI
from app.logger import setup_logging
from routers.students import get_students
from routers.staff import get_staffs
import logging

setup_logging()
logger=logging.getLogger(__name__)
app=FastAPI()
logger.info("School Backend Application is getting started")
app.include_router(get_students.router,prefix="/students",tags=["Students"])

