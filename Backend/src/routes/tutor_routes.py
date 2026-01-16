from fastapi import APIRouter
from models.tutor import Tutor

router = APIRouter()

@router.get("/")
def get_tutors():
    return Tutor.get_all()