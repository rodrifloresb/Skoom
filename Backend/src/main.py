from fastapi import FastAPI
from models.tutor import Tutor
from routes.tutor_routes import router as tutor_router
from config.database import get_connection

# Conexion a la BD
get_connection()

# Crear la tabla si no existe.
Tutor.create_table()

# ROUTERS
app = FastAPI()

app.include_router(tutor_router, prefix="/tutors", tags=["Tutors"])

@app.get("/")
def health():
    return {"status": "ok"}
