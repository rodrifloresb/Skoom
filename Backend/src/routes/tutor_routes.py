from fastapi import APIRouter, HTTPException
from models.tutor import Tutor

router = APIRouter()

@router.get("/")
def get_tutors():
    return Tutor.get_all()

@router.get("/by")
def get_by(field: str, value: str):

    result = Tutor.get_by(field=field, value=value)

    if not result["ok"]:
        if "Campo no permitido" in result["error"]:
            raise HTTPException(status_code=400, detail=result["error"])
        else:
            raise HTTPException(status_code=500, detail="Error interno")


    if result["data"] == []:
        raise HTTPException(status_code=404, detail="No existe tutor")

    return result["data"]


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

    if not result["ok"]:
        raise HTTPException(status_code=500, detail=result["error"])

    if result["data"] != []:
        raise HTTPException(status_code=409, detail="Este mail ya fue registrado")
    
    Tutor.create(firstName=firstName,
                 lastName=lastName,
                 mail=mail,
                 password=password,
                 phoneNumber=phoneNumber,
                 address=address)
    
@router.delete("/{id}")
def delete_tutor(id: int):
    
    result = Tutor.get_by(field="id", value=id)
    
    if result["data"] == []:
        raise HTTPException(status_code=404, detail="No existe tutor con este id")
    
    Tutor.delete(id=id)
    
@router.put("/{id}")
def update_tutor(id: int, field: str, value: str):

    result = Tutor.get_by(field="id", value=id)

    if not result["ok"]:
        if result["error"] == "Campo no permitido":
            raise HTTPException(status_code=400, detail=result["error"])
        else:
            raise HTTPException(status_code=500, detail="Error interno")

    if result["data"] == []:
        raise HTTPException(status_code=404, detail="No existe tutor con este id")

    update_result = Tutor.update(id=id, field=field, value=value)

    if not update_result["ok"]:
        if update_result["error"] == "Campo no permitido":
            raise HTTPException(status_code=400, detail=update_result["error"])
        elif update_result["error"] == "Tutor no encontrado":
            raise HTTPException(status_code=404, detail=update_result["error"])
        else:
            raise HTTPException(status_code=500, detail="Error interno")

    return {"message": "Tutor actualizado correctamente"}
