# Práctica 4 - Comunicación entre contenedores
# Alumno: Erick Alejandro Contreras Salas
# Expediente: 722185
# Desarrollo en la Nube - Primavera 2026 ITESO

from fastapi import FastAPI, UploadFile, File, Form
from services.boletin_services import create_boletin

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola desde el contenedor de FastAPI!"}

@app.post("/boletines")
async def create_boletin_endpoint(
    boletinFile: UploadFile = File(...),
    boletinMessage: str = Form(...),
    email: str = Form(...)
):
    boletinFileContent = await boletinFile.read()
    return create_boletin(boletinFileContent, boletinMessage, email)
