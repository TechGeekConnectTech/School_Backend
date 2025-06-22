from fastapi import FastAPI
from app.logger import setup_logging

import logging

from routers.router import api_router

setup_logging()
logger=logging.getLogger(__name__)
app=FastAPI()
logger.info("School Backend Application is getting started")
app.include_router(api_router,prefix="/api")

