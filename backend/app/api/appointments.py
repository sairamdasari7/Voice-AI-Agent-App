
from fastapi import APIRouter
from app.scheduling.scheduler import list_appointments

router = APIRouter(prefix="/appointments")

@router.get("/")
def get_all():
    return list_appointments()
