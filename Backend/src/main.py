from fastapi import FastAPI
from models.tutor import Tutor
from models.school import School
from models.student import Student
from routes.school_routes import router as school_routes
from routes.tutor_routes import router as tutor_router
from routes.student_routes import router as student_router
from config.database import get_connection
from config.seed import seed_database

# Conexion a la BD
get_connection()

# Crear la tabla si no existe.
Tutor.create_table()
School.create_table()
Student.create_table()

# SEED

seed_database()

# ROUTERS
app = FastAPI()

app.include_router(tutor_router, prefix="/tutors", tags=["Tutors"])
app.include_router(school_routes, prefix="/school", tags = ["Schools"])
app.include_router(student_router, prefix="/students", tags= ["Students"])

@app.get("/")
def health():
    return {"status": "ok"}
