from pydantic import BaseModel

class  PedidoResponse(BaseModel):
    id: int
    cliente: str
    pizza: str
    quantidade: int
    
    class Config:
        from_attributes = True