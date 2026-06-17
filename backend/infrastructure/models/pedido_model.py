from sqlalchemy import Column, Integer, String

from infrastructure.database.base import Base


class PedidoModel(Base):

    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)

    cliente = Column(String(100))

    pizza = Column(String(100))
    
    quantidade = Column(Integer)