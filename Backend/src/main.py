from fastapi import FastAPI
from models.tutor import Tutor
from models.colegio import Colegio
from routes.colegio_routes import router as colegio_router 
from routes.tutor_routes import router as tutor_router
from config.database import get_connection

# Conexion a la BD
get_connection()

# Crear la tabla si no existe.
Tutor.create_table()
Colegio.create_table()

# ROUTERS
app = FastAPI()

app.include_router(tutor_router, prefix="/tutors", tags=["Tutors"])
app.include_router(colegio_router, prefix="/colegios", tags = ["Colegios"])

@app.get("/")
def health():
    return {"status": "ok"}
