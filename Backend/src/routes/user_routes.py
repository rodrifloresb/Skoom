from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_users():
    return["skoom","run"]

@router.get("/caro")
def get_caro():
    return ["caro"]