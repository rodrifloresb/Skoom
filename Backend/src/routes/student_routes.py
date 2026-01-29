from fastapi import APIRouter, HTTPException
from models.student import Student

router = APIRouter()

@router.get("/")
def get_students():
    return Student.get_all()

@router.get("/by")
def get_by(field:str, value):
    
    result = Student.get_by(field=field,value=value)
    
    if not result["ok"]:
        if "Campo no permitido" in result["error"]:
            raise HTTPException(status_code=400, detail=result["error"])
        else:
            raise HTTPException(status_code=500, detail="Error interno")


    if result["data"] == []:
        raise HTTPException(status_code=404, detail="No existe estudiante")

    return result["data"]

@router.post("/")
def post_student(firstName, lastName, tuition, course, tutor_id: int, colegio_id: int):
    
    result = Student.get_by(field="tuition", value=tuition)

    if not result["ok"]:
        raise HTTPException(status_code=500, detail=result["error"])

    if result["data"] != []:
        raise HTTPException(status_code=409, detail="Numero de matricula no disponible")
    
    result_create  = Student.create(firstName=firstName,
                            lastName=lastName,
                            tuition=tuition,
                            course=course,
                            tutor_id=tutor_id,
                            colegio_id=colegio_id)
    
    return result_create
    

@router.delete("/")
def delete_student(id: int):
    result = Student.get_by(field="id", value=id)
    
    if result["data"] == []:
        raise HTTPException(status_code=404, detail="No existe estudiante con este id")
    
    Student.delete(id=id)
    
    return {"message": "Estudiante eliminado de la base de datos."}
    
@router.put("/")
def update_student(id: int, field: str, value: str):
    result = Student.get_by(field="id", value=id)

    if not result["ok"]:
        if result["error"] == "Campo no permitido":
            raise HTTPException(status_code=400, detail=result["error"])
        else:
            raise HTTPException(status_code=500, detail="Error interno")

    if result["data"] == []:
        raise HTTPException(status_code=404, detail="No existe estudiante con este id")

    update_result = Student.update(id=id, field=field, value=value)

    if not update_result["ok"]:
        if update_result["error"] == "Campo no permitido":
            raise HTTPException(status_code=400, detail=update_result["error"])
        elif update_result["error"] == "Estudiante no encontrado":
            raise HTTPException(status_code=404, detail=update_result["error"])
        else:
            raise HTTPException(status_code=500, detail="Error interno")

    return {"message": "Estudiante actualizado correctamente"}