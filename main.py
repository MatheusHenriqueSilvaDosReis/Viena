from fastapi import FastAPI
from routes.auth import router as auth_router
from routes.contatos import router as contatos_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(contatos_router)

@app.get("/")
def inicio():
    return {"mensagem": "API Alerta+ funcionando!"}