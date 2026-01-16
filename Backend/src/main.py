from fastapi import FastAPI
from models.tutor import Tutor
from routes.tutor_routes import router as tutor_router

# Crear la tabla si no existe.
Tutor.create_table()

app = FastAPI()

# ROUTERS
app.include_router(tutor_router, prefix="/tutors", tags=["Tutors"])

@app.get("/")
def health():
    return {"status": "ok"}
