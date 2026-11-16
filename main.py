
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.auth import router as auth_router
from routes.contatos import router as contatos_router

app = FastAPI()

# Configuração de acesso pelo Expo Web
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8081",
        "http://127.0.0.1:8081",
        "http://192.168.1.82:8081",
        "http://localhost:19006",
        "http://192.168.1.82:19006",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(auth_router)
app.include_router(contatos_router)

@app.get("/")
def inicio():
    return {"mensagem": "API Alerta+ funcionando!"}
