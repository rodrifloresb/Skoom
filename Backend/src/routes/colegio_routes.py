from fastapi import APIRouter, HTTPException
from models.colegio import Colegio
#aca tengo que escribir el codigo necesario para utilizar lo escrito en modelos

router = APIRouter()

@router.get("/")
def get_colegios():
    return Colegio.get_all()

@router.get("/by")
def get_by(field:str, value):
    return Colegio.get_by(field = field, value=value)

@router.post("/")
def post_colegio(
    name,
    mail,
    password,
    phoneNumber,
    address
    ):
    
    result = Colegio.get_by(field="mail", value=mail)
    
    if result != []:
        raise HTTPException(status_code=409, detail="Este mail ya fue registrado")
    
    Colegio.create(
                 name = name, 
                 mail=mail,
                 password=password,
                 phoneNumber=phoneNumber,
                 address=address)
    
@router.delete("/{id}")
def delete_colegio(id: int):
    
    result = Colegio.get_by(field="id", value=id)
    
    if result == []:
        raise HTTPException(status_code=404, detail="No existe colegio con este id")
    
    Colegio.delete(id=id)
    
@router.put("/{id}")
def colegio_update(id: int, field: str, value):
    
    result = Colegio.get_by(field="id", value=id)
    
    if result == []:
        raise HTTPException(status_code=404, detail="No existe colegio con este id")
    
    Colegio.update(id=id, field=field, value=value)