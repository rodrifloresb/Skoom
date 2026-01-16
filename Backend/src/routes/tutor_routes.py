from fastapi import APIRouter
from models.tutor import Tutor

router = APIRouter()

@router.get("/")
def get_tutors():
    return Tutor.get_all()

@router.post("/")
def post_tutor(
    firstName,
    lastName,
    mail,
    password,
    phoneNumber,
    address
    ):
    
    Tutor.create(firstName=firstName,
                 lastName=lastName,
                 mail=mail,
                 password=password,
                 phoneNumber=phoneNumber,
                 address=address)