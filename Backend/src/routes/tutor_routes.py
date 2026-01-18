from fastapi import APIRouter, HTTPException
from models.tutor import Tutor

router = APIRouter()

@router.get("/")
def get_tutors():
    return Tutor.get_all()

@router.get("/by")
def get_by(field: str, value):
    return Tutor.get_by(field=field, value=value)

@router.post("/")
def post_tutor(
    firstName,
    lastName,
    mail,
    password,
    phoneNumber,
    address
    ):
    
    result = Tutor.get_by(field="mail", value=mail)
    
    if result != []:
        raise HTTPException(status_code=409, detail="Este mail ya fue registrado")
    
    Tutor.create(firstName=firstName,
                 lastName=lastName,
                 mail=mail,
                 password=password,
                 phoneNumber=phoneNumber,
                 address=address)