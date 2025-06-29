from fastapi import FastAPI, APIRouter
from routers.staff import get_staffs
from routers.students import get_students
from routers.fees import get_fees

api_router=APIRouter()
api_router.include_router(get_students.router,prefix="/student",tags=["Student"])
api_router.include_router(get_staffs.router,prefix="/staff",tags=["Staff"])
api_router.include_router(get_fees.router,prefix="/fees",tags=["Fees"])
