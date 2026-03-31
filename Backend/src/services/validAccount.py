from fastapi import APIRouter, HTTPException
from models.tutor import Tutor
from models.school import School

router = APIRouter()

@router.get("/")
def validAccount(typeAccount: str, mail: str, password: str):
    
    if(typeAccount != "school" and typeAccount != "tutor"):
        raise HTTPException(status_code=404, detail="Tipo de cuenta invalido.")
    
    if(typeAccount == "school"):
        temp = School.get_by("mail", mail)
        
        if not temp["ok"]:
            raise HTTPException(status_code=500, detail="Error interno")
        
        if not temp["data"]:
            return {"ok": False, "data": "isNotValid"}
        
        passTemp = temp["data"][0][3]
        
        if(password == passTemp):
            return {"ok": True, "data": "isValid"}
        else:
            return {"ok": False, "data": "isNotValid"}

    if(typeAccount == "tutor"):
        temp = Tutor.get_by("mail", mail)
        
        if not temp["ok"]:
            raise HTTPException(status_code=500, detail="Error interno")
        
        if not temp["data"]:
            return {"ok": False, "data": "isNotValid"}
        
        passTemp = temp["data"][0][4]
        
        if(password == passTemp):
            return {"ok": True, "data": "isValid"}
        else:
            return {"ok": False, "data": "isNotValid"}
        
    return {"ok": False, "data": "Error"}