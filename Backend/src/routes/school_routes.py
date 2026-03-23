from fastapi import APIRouter, HTTPException
from models.school import School

router = APIRouter()

@router.get("/")
def get_schools():
    return School.get_all()

@router.get("/by")
def get_by(field: str, value: str):

    result = School.get_by(field=field, value=value)

    if not result["ok"]:
        if "Campo no permitido" in result["error"]:
            raise HTTPException(status_code=400, detail=result["error"])
        else:
            raise HTTPException(status_code=500, detail="Error interno")

    if result["data"] == []:
        raise HTTPException(status_code=404, detail="No existe school")

    return result["data"]

@router.post("/")
def post_school(name: str, mail: str, password: str, phoneNumber: str, address: str):

    result = School.get_by(field="mail", value=mail)

    if not result["ok"]:
        raise HTTPException(status_code=500, detail=result["error"])

    if result["data"] != []:
        raise HTTPException(status_code=409, detail="Este mail ya fue registrado")

    result_create = School.create(
        name=name,
        mail=mail,
        password=password,
        phoneNumber=phoneNumber,
        address=address
    )

    return result_create

@router.delete("/")
def delete_school(id: int):

    result = School.get_by(field="id", value=id)

    if not result["ok"]:
        raise HTTPException(status_code=500, detail=result["error"])

    if result["data"] == []:
        raise HTTPException(status_code=404, detail="No existe school con este id")

    School.delete(id=id)

    return {"message": "School eliminado de la base de datos."}

@router.put("/")
def update_school(id: int, field: str, value: str):

    result = School.get_by(field="id", value=id)

    if not result["ok"]:
        if result["error"] == "Campo no permitido":
            raise HTTPException(status_code=400, detail=result["error"])
        else:
            raise HTTPException(status_code=500, detail="Error interno")

    if result["data"] == []:
        raise HTTPException(status_code=404, detail="No existe school con este id")

    update_result = School.update(id=id, field=field, value=value)

    if not update_result["ok"]:
        if update_result["error"] == "Campo no permitido":
            raise HTTPException(status_code=400, detail=update_result["error"])
        elif update_result["error"] == "School no encontrado":
            raise HTTPException(status_code=404, detail=update_result["error"])
        else:
            raise HTTPException(status_code=500, detail="Error interno")

    return {"message": "School actualizado correctamente"}