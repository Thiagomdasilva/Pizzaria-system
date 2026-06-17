from pydantic import BaseModel

class PedidoRequest ( BaseModel):
    cliente: str
    pizza: str
    quantidade: int