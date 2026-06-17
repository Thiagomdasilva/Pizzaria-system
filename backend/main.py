from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.pedido_routes import router

from infrastructure.database.base import Base
from infrastructure.database.connection import engine
from infrastructure.models.pedido_model import PedidoModel


app = FastAPI()


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():

    return {
        "mensagem": "API da Pizzaria funcionando"
    }