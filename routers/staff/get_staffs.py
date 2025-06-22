from fastapi import APIRouter,HTTPException
from starlette.responses import JSONResponse

from app.logger import setup_logging
import logging


setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()

@router.get("/")
def get_staff():
    logger.info("Request Received to get all staff info")
    return JSONResponse(
        status_code=200,
        content={"message":"Testing OK"}
    )